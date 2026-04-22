# Daily arXiv digest

Nightly GitHub Action that pulls new submissions from `q-bio.QM`, `q-bio.GN`,
`q-bio.PE`, and `stat.AP`, scores each paper against a list of topic keywords,
and commits a ranked markdown digest to `digests/YYYY-MM-DD.md`.

## Files

| Path | Purpose |
| --- | --- |
| `scripts/arxiv_digest.py` | Fetch, score, and format |
| `config/tracked.yaml` | Categories and topic keywords |
| `.github/workflows/daily-arxiv-digest.yml` | Nightly cron at 10:30 UTC |
| `digests/YYYY-MM-DD.md` | Generated output (one file per day) |

## Output URL

```
https://github.com/chenjiezeng/arxiv-digest/blob/main/digests/YYYY-MM-DD.md
```

## Scoring

Each paper gets +1 for every keyword that appears in the title or abstract.
Author tracking is intentionally not in scope here — Gmail Scholar alerts
already cover that.

Short single-word keywords (≤5 characters, e.g. `chip`, `prs`, `gwas`, `hpo`)
use word-boundary regex to avoid matching inside unrelated words like
`chipset`. Longer phrases use plain substring matching, after lowercasing
and stripping diacritics.

Default `--min-score 2` requires at least two keyword hits, which filters
out papers that incidentally mention one of your terms but aren't really
about it.

## API politeness

arXiv's API rate-limits aggressively. The fetcher uses a 5-second client
delay (above arXiv's 3-second recommendation), only 2 retries (since most
failures are rate-limit and retrying immediately makes them worse), and
a 15-second pause between categories. If a single category 429s, the run
logs a warning and skips it rather than crashing.

## Push robustness

The commit step uses a 5-attempt retry loop with rebase-on-failure.
GitHub Actions runners can race against each other or against manual
pushes — the loop fetches and rebases on each conflict before retrying.

`concurrency: daily-arxiv-digest` at the workflow level prevents two runs
of this workflow from executing simultaneously.

## Manual trigger

Actions tab → *Daily arXiv digest* → *Run workflow* → set
`Lookback window in hours` (default 30, use 168 for a week of backfill,
720 for a month) → click *Run workflow*.

## Local run

```bash
pip install arxiv PyYAML
python scripts/arxiv_digest.py --config config/tracked.yaml --lookback-hours 30
```

Useful flags:

- `--lookback-hours N` — window size. Default 30.
- `--min-score N` — drop papers below this score. Default 2.

## Editing tracked topics

Edit `config/tracked.yaml`. Keywords are matched case-insensitively after
diacritic stripping. Group related terms — overlap is fine, just slightly
inflates scores on multi-concept papers without breaking ranking.
