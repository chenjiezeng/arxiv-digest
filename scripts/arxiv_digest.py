#!/usr/bin/env python3
"""Daily arXiv digest.

Pulls new submissions from the configured arXiv categories within a lookback
window, scores each paper against a list of tracked authors and topic
keywords, and writes a ranked markdown digest to ``digests/YYYY-MM-DD.md``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path

import arxiv
import yaml


USER_AGENT = "arxiv-digest/1.0 (+https://github.com/chenjiezeng/arxiv-digest)"


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #

@dataclass
class Config:
    categories: list[str]
    authors: list[str]
    keywords: list[str]
    output_dir: Path


def load_config(path: Path) -> Config:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return Config(
        categories=list(data["categories"]),
        authors=[a.strip() for a in data.get("authors", []) if a.strip()],
        keywords=[k.strip().lower() for k in data.get("keywords", []) if k.strip()],
        output_dir=Path(data.get("output_dir", "digests")),
    )


# --------------------------------------------------------------------------- #
# Matching helpers
# --------------------------------------------------------------------------- #

def _strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def _norm(s: str) -> str:
    return _strip_accents(s).lower()


def _author_match(target: str, author_names: list[str]) -> bool:
    """True if `target` (e.g. 'Miguel Hernán') matches any of the arXiv author names.

    Diacritics and case are normalized. Match succeeds if either:
      (a) the full normalized target appears as a substring in the author name, or
      (b) the target's last name appears as a word boundary in the author name AND
          the author's first token either (i) is an initial matching the target's
          first initial, or (ii) is a full first name equal to — or a prefix of,
          or prefixed by — the target's first name.
    """
    tgt_norm = _norm(target)
    tgt_tokens = tgt_norm.split()
    if not tgt_tokens:
        return False
    tgt_last = tgt_tokens[-1]
    tgt_first = tgt_tokens[0]
    last_re = re.compile(rf"\b{re.escape(tgt_last)}\b")

    for name in author_names:
        n = _norm(name)
        if tgt_norm in n:
            return True
        if not last_re.search(n):
            continue
        tokens = n.split()
        if not tokens:
            continue
        first_tok = tokens[0]
        bare = first_tok.rstrip(".,")
        if len(bare) == 1:
            # First name is an initial — match on initial only
            if bare == tgt_first[0]:
                return True
        else:
            # Full first name — require equality or prefix containment in either direction
            if (
                first_tok == tgt_first
                or first_tok.startswith(tgt_first)
                or tgt_first.startswith(first_tok)
            ):
                return True
    return False


def score_paper(
    paper: arxiv.Result, cfg: Config
) -> tuple[int, list[str], list[str]]:
    """Return (score, matched_authors, matched_keywords).

    Short single-word keywords (≤5 chars, e.g. 'chip', 'prs', 'gwas') use
    word-boundary regex to avoid matching inside unrelated words like
    'chipset' or 'dipress'. Longer keywords and multi-word phrases use plain
    substring match.
    """
    author_names = [a.name for a in paper.authors]
    matched_authors = [
        t for t in cfg.authors if _author_match(t, author_names)
    ]
    text_norm = _norm(paper.title + " " + paper.summary)
    matched_keywords: list[str] = []
    for kw in cfg.keywords:
        if len(kw) <= 5 and " " not in kw:
            if re.search(rf"\b{re.escape(kw)}\b", text_norm):
                matched_keywords.append(kw)
        else:
            if kw in text_norm:
                matched_keywords.append(kw)
    score = 10 * len(matched_authors) + len(matched_keywords)
    return score, matched_authors, matched_keywords


# --------------------------------------------------------------------------- #
# Deep summary (full-text section harvest for priority papers)
# --------------------------------------------------------------------------- #

# Headings worth surfacing from the rendered arXiv HTML. Matched case-
# insensitively as substrings against the heading text.
_INTERESTING_HEADINGS = (
    "introduction",
    "background",
    "data",
    "cohort",
    "method",
    "approach",
    "model",
    "result",
    "finding",
    "experiment",
    "benchmark",
    "discussion",
    "conclusion",
    "limitation",
)

# Per-section snippet cap (chars) and total sections cap.
_DEEP_SECTION_CHARS = 600
_DEEP_MAX_SECTIONS = 6


class _SectionExtractor(HTMLParser):
    """Harvest (heading, opening-paragraph) pairs from arXiv HTML.

    The arXiv HTML render uses <h2>/<h3> for section/subsection headings
    followed by <p> bodies. We capture each heading and the first paragraph
    of running text below it (capped at _DEEP_SECTION_CHARS).
    """

    def __init__(self) -> None:
        super().__init__()
        self.sections: list[tuple[str, str]] = []
        self._heading_buf: list[str] = []
        self._body_buf: list[str] = []
        self._cur_heading: str | None = None
        self._in_heading = False
        self._in_para = False
        self._body_chars = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3"):
            self._flush()
            self._in_heading = True
            self._heading_buf = []
        elif tag == "p" and self._cur_heading and self._body_chars < _DEEP_SECTION_CHARS:
            self._in_para = True

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3"):
            self._in_heading = False
            self._cur_heading = "".join(self._heading_buf).strip()
            self._body_buf = []
            self._body_chars = 0
        elif tag == "p":
            self._in_para = False
            if self._body_buf and not self._body_buf[-1].endswith(" "):
                self._body_buf.append(" ")

    def handle_data(self, data):
        if self._in_heading:
            self._heading_buf.append(data)
        elif self._in_para and self._body_chars < _DEEP_SECTION_CHARS:
            remaining = _DEEP_SECTION_CHARS - self._body_chars
            chunk = data[:remaining]
            self._body_buf.append(chunk)
            self._body_chars += len(chunk)

    def _flush(self) -> None:
        if self._cur_heading:
            body = "".join(self._body_buf).strip()
            if body:
                self.sections.append((self._cur_heading, body))
        self._cur_heading = None
        self._body_buf = []
        self._body_chars = 0

    def close(self) -> None:
        super().close()
        self._flush()


def _arxiv_html_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/html/{arxiv_id}"


def fetch_deep_summary(arxiv_id: str, *, timeout: float = 15.0) -> str | None:
    """Fetch arXiv HTML for `arxiv_id` and extract a markdown deep-summary block.

    Returns None on any failure — empty HTML, non-200, parse error, or no
    interesting sections found. The caller should treat this as best-effort
    enrichment, not a hard requirement.
    """
    url = _arxiv_html_url(arxiv_id)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if r.status != 200:
                return None
            html = r.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
        print(f"WARN: deep-summary fetch failed for {arxiv_id}: {e}", file=sys.stderr)
        return None

    parser = _SectionExtractor()
    try:
        parser.feed(html)
        parser.close()
    except Exception as e:
        print(f"WARN: deep-summary parse failed for {arxiv_id}: {e}", file=sys.stderr)
        return None

    selected: list[tuple[str, str]] = []
    for heading, body in parser.sections:
        if any(k in heading.lower() for k in _INTERESTING_HEADINGS):
            selected.append((heading, body))
        if len(selected) >= _DEEP_MAX_SECTIONS:
            break
    if not selected:
        return None

    lines = ["**Deep summary (auto-extracted from full text):**", ""]
    for heading, body in selected:
        snippet = body.rstrip()
        if len(snippet) >= _DEEP_SECTION_CHARS:
            snippet = snippet.rstrip(" .,;:") + "…"
        lines.extend([f"_{heading}_", "", snippet, ""])
    return "\n".join(lines).rstrip() + "\n"


# --------------------------------------------------------------------------- #
# Fetch
# --------------------------------------------------------------------------- #

def fetch_papers(
    cfg: Config, lookback_hours: float
) -> tuple[list[arxiv.Result], list[str]]:
    """Fetch newly submitted papers across categories within lookback window.

    Conservative on arXiv API: 5s between requests, only 2 retries (since most
    failures here are rate-limiting and retrying immediately makes it worse),
    and a 15s pause between categories. If a category 429s, we log and skip
    rather than crashing the whole run.

    Returns (papers, failed_categories) so the caller can distinguish a
    genuine empty day from a silent fetch failure.
    """
    client = arxiv.Client(page_size=100, delay_seconds=5.0, num_retries=2)
    # arXiv 403s default urllib UAs ("Python-urllib/3.x"). Identify ourselves
    # so requests aren't fingerprinted as an unauthenticated bot.
    client._session.headers["User-Agent"] = USER_AGENT
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    seen: set[str] = set()
    papers: list[arxiv.Result] = []
    failed: list[str] = []

    for cat in cfg.categories:
        search = arxiv.Search(
            query=f"cat:{cat}",
            max_results=500,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        cat_count = 0
        # arXiv occasionally returns results slightly out of submitted-date
        # order (cross-listings, v2/v3 reclassifications keep their original
        # `published` date). Stop only after K consecutive old results so a
        # single old straggler at the top of the page doesn't truncate the
        # window prematurely.
        old_streak = 0
        OLD_STREAK_LIMIT = 10
        try:
            for result in client.results(search):
                if result.published < cutoff:
                    old_streak += 1
                    if old_streak >= OLD_STREAK_LIMIT:
                        break
                    continue
                old_streak = 0
                base_id = result.entry_id.rsplit("/", 1)[-1].split("v")[0]
                if base_id in seen:
                    continue
                seen.add(base_id)
                papers.append(result)
                cat_count += 1
        except (arxiv.HTTPError, arxiv.UnexpectedEmptyPageError, urllib.error.URLError) as e:
            print(
                f"WARN: arXiv API error fetching {cat}: {e}. Skipping category.",
                file=sys.stderr,
            )
            failed.append(cat)
        else:
            # Distinguish "API succeeded, genuinely zero submissions" from a
            # silent-empty rate-limit response. The caller can't tell from
            # `papers` alone, so emit a per-category signal.
            if cat_count == 0:
                print(
                    f"WARN: category {cat} returned 0 results within lookback.",
                    file=sys.stderr,
                )
        # Longer pause between categories — arXiv 429s are sticky.
        time.sleep(15)

    return papers, failed


# --------------------------------------------------------------------------- #
# Output
# --------------------------------------------------------------------------- #

def format_markdown(
    scored: list[tuple[arxiv.Result, int, list[str], list[str]]],
    cfg: Config,
    failed_categories: list[str] | None = None,
    deep_summaries: dict[str, str] | None = None,
) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        f"# arXiv digest — {today}",
        "",
        f"Categories: {', '.join(cfg.categories)}",
        f"Relevant papers: {len(scored)}",
        "",
    ]
    if failed_categories:
        lines.append(
            f"> WARNING: {len(failed_categories)}/{len(cfg.categories)} "
            f"categories failed to fetch ({', '.join(failed_categories)}); "
            f"results may be incomplete."
        )
        lines.append("")
    if not scored:
        lines.append("_No matches in the lookback window._")
        lines.append("")
        return "\n".join(lines)

    for paper, s, matched_authors, matched_keywords in scored:
        arxiv_id = paper.entry_id.rsplit("/", 1)[-1]
        lines.extend([
            f"## {paper.title.strip()}",
            "",
            f"**Authors:** {', '.join(a.name for a in paper.authors)}",
            "",
            f"**Primary category:** {paper.primary_category}",
            "",
            f"**arXiv:** [{arxiv_id}]({paper.entry_id})",
            "",
            f"**Submitted:** {paper.published.strftime('%Y-%m-%d')}",
            "",
        ])
        if matched_authors:
            lines.append(f"**Tracked authors:** {', '.join(matched_authors)}")
            lines.append("")
        if matched_keywords:
            lines.append(f"**Keyword hits:** {', '.join(matched_keywords)}")
            lines.append("")
        lines.append(f"**Score:** {s}")
        lines.append("")
        lines.append("**Abstract:**")
        lines.append("")
        lines.append(paper.summary.strip())
        lines.append("")
        if deep_summaries:
            base_id = _arxiv_base_id(paper.entry_id)
            block = deep_summaries.get(base_id)
            if block:
                lines.append(block)
                lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Seen-paper cache (cross-run deduplication)
# --------------------------------------------------------------------------- #

def _arxiv_base_id(entry_id: str) -> str:
    """Extract the version-less arXiv ID from an entry URL.

    e.g. 'http://arxiv.org/abs/2604.11824v2' -> '2604.11824'.
    """
    return entry_id.rsplit("/", 1)[-1].split("v")[0]


def load_seen(path: Path) -> set[str]:
    if not path.exists():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return set(data.get("seen", []))
    except (json.JSONDecodeError, KeyError) as e:
        print(f"WARN: Could not parse {path}: {e}. Starting fresh.", file=sys.stderr)
        return set()


def save_seen(path: Path, seen: set[str], cap: int = 5000) -> None:
    """Persist seen IDs. Caps at `cap` most-recently-added IDs to bound disk
    growth — sets in Python 3.7+ preserve insertion order, so newer IDs win."""
    if len(seen) > cap:
        seen = set(list(seen)[-cap:])
    path.write_text(
        json.dumps({"seen": sorted(seen)}, indent=2) + "\n",
        encoding="utf-8",
    )


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", type=Path, default=Path("config/tracked.yaml"))
    ap.add_argument("--lookback-hours", type=float, default=30.0)
    ap.add_argument("--min-score", type=int, default=2)
    ap.add_argument(
        "--seen-cache",
        type=Path,
        default=Path("seen.json"),
        help="Path to JSON cache of arXiv IDs already surfaced. "
        "Pass /dev/null to disable deduplication.",
    )
    ap.add_argument(
        "--deep-score",
        type=int,
        default=4,
        help="Score threshold above which papers get a full-text deep summary "
        "fetched from arxiv.org/html/<id>. Default 4 (≥4 keyword hits).",
    )
    ap.add_argument(
        "--no-deep",
        action="store_true",
        help="Disable deep-summary fetching entirely (e.g. for offline testing).",
    )
    ap.add_argument(
        "--deep-timeout",
        type=float,
        default=15.0,
        help="Per-paper HTTP timeout for deep-summary fetch, in seconds.",
    )
    args = ap.parse_args()

    cfg = load_config(args.config)
    print(
        f"Fetching {len(cfg.categories)} categories, lookback {args.lookback_hours}h",
        file=sys.stderr,
    )
    papers, failed_categories = fetch_papers(cfg, args.lookback_hours)
    print(f"Fetched {len(papers)} candidate papers", file=sys.stderr)

    # If every category failed, an empty digest would be a silent lie. Fail
    # loud so the workflow turns red and the issue gets noticed instead of
    # accumulating "no matches" days that mask a broken fetch.
    if failed_categories and len(failed_categories) == len(cfg.categories):
        print(
            f"ERROR: all {len(cfg.categories)} categories failed to fetch — "
            f"refusing to write a misleading empty digest.",
            file=sys.stderr,
        )
        return 1

    # Score everything that meets the threshold, tracking which were seen before.
    matched: list[tuple[arxiv.Result, int, list[str], list[str]]] = []
    for p in papers:
        s, ma, mk = score_paper(p, cfg)
        if s >= args.min_score:
            matched.append((p, s, ma, mk))
    print(f"Matched {len(matched)} papers (before dedup)", file=sys.stderr)

    # Deduplicate against the seen cache.
    seen = load_seen(args.seen_cache)
    new_papers = [t for t in matched if _arxiv_base_id(t[0].entry_id) not in seen]
    suppressed = len(matched) - len(new_papers)
    print(
        f"After dedup: {len(new_papers)} new, {suppressed} previously surfaced",
        file=sys.stderr,
    )

    # Sort and write the digest.
    new_papers.sort(key=lambda t: (-t[1], -t[0].published.timestamp()))

    # For papers above --deep-score, fetch the rendered HTML and harvest
    # section-level snippets. Best-effort: any failure falls back to the
    # abstract-only rendering.
    deep_summaries: dict[str, str] = {}
    if not args.no_deep:
        priority = [t for t in new_papers if t[1] >= args.deep_score]
        if priority:
            print(
                f"Fetching deep summaries for {len(priority)} priority papers "
                f"(score ≥ {args.deep_score})",
                file=sys.stderr,
            )
        for i, (paper, _, _, _) in enumerate(priority):
            base_id = _arxiv_base_id(paper.entry_id)
            block = fetch_deep_summary(base_id, timeout=args.deep_timeout)
            if block:
                deep_summaries[base_id] = block
            # Polite pause between HTML fetches; arxiv.org throttles aggressively.
            if i < len(priority) - 1:
                time.sleep(2)

    cfg.output_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = cfg.output_dir / f"{today}.md"
    md = format_markdown(new_papers, cfg, failed_categories, deep_summaries)
    if suppressed > 0:
        # Add a transparency note to the header.
        md = md.replace(
            f"Relevant papers: {len(new_papers)}",
            f"Relevant papers: {len(new_papers)} ({suppressed} previously surfaced, suppressed)",
            1,
        )
    out.write_text(md, encoding="utf-8")
    print(f"Wrote {out}", file=sys.stderr)

    # Update the seen cache with the IDs we just surfaced.
    for p, _, _, _ in new_papers:
        seen.add(_arxiv_base_id(p.entry_id))
    save_seen(args.seen_cache, seen)
    print(f"Updated {args.seen_cache} ({len(seen)} IDs total)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
