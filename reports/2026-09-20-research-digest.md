# Research digest report — 2026-09-20

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-20 12:40Z** (~19 days since the
last research-digest report, covering eighteen arxiv-digest cron runs
and roughly two weeks of Google Scholar alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-02.md` → `2026-09-19.md`) | 09-02 → 09-19 daily crons | 18 daily runs. Dry days (0 papers): 09-03, 09-05–06, 09-08, 09-12, 09-19. 09-02: 1 paper (Ramesh mudskippers — off-thread `motor` keyword). 09-04: 2 papers (Cortez-Rodriguez disaster×nonprofit panel-CI; Yu et al. location-invariant extremal-QTE estimator — METHODS-WATCH). 09-07: 1 paper (Rajabli & Collins brain-age LoRA-adapted FM for AD — METHODS-WATCH). 09-09: 2 papers (Snel & Schulz `pyinfluence` Cohen's d attribution in UKB — **HIGH**; Wu et al. FUSE-RT HPLC Sim2Real FM — off-thread). 09-10: 1 paper (Lee et al. Kalman-filtered HT prevalence — METHODS-WATCH). 09-11: 3 papers (Devarakonda scDEFT drug-effect / counterfactual on 1.16M-cell IBD atlas — **HIGH**; Hendrix et al. geospatial FM on CDC PLACES — METHODS-WATCH; Semchin et al. connectome-constrained PD progression subtypes — HIGH). 09-16: 2 papers (Wang et al. NTM/CF ABM→PDE mucociliary-clearance digital-twin — **HIGH**; Zhang et al. scKITE knowledge-enhanced scFM — METHODS-WATCH). 09-17: 1 paper (Fujita & Hattori Information-Set Emulation causal certificates for AI-derived EHR features — **HIGH**). 09-18: 2 papers (Ghasemnejad et al. LLM ReAct+RAG agent for HPO-scale genetic-disease severity classification with ACMG+ACOG guidelines — **HIGH**; Csillag Finger & Possebom semiparametric contamination bias for multi-valued treatments — METHODS-WATCH). |
| No `arxiv-digest` email hits from GitHub | — | Same pattern as prior windows: `arxiv-digest` writes to `digests/` on-disk via the daily cron, and GitHub does not send notification email for cron commits on your own repo, so the on-disk digests remain the feed. Queries for `arxiv-digest`, `chenjiezeng`, and `from:notifications@github.com` × 14d/30d all returned zero threads. |
| Google Scholar alerts (09-19 → 09-20 batches) | 09-19 22:22Z + 09-20 03:33Z | 25+ feeds fired across two days; below is the on-thread subset. Author-feed HIGHs: **Joshua C. Denny** (your own JCF 2026 poster — Zeng, Raraigh, Cutting, Denny — longitudinal CFTR-modulator disease burden + safety in AoU); **George Hripcsak** (Gronsbell/Cai/Mukherjee/Varghese *Responsible AI with EHR data*; Ostropolets et al. real-world use of controlled terminologies across a large OHDSI network); **Lisa Bastarache** (Liu et al. plasma-proteomic atlas of the ocular-disease phenome — PheWAS × Olink); **Tiffany J Callahan** (Spahiu & Roveda embodied KGs — off-thread); **Marinka Zitnik** (Ho et al. LMs controlling their own attention — off-thread); **Zhiyong Lu** (Wang et al. CLEAR cross-source evidence adjudication for medical LLMs); **Pranav Rajpurkar** (Yuan et al. Asclepius adaptive harness for long-horizon clinical agents); **Peter Szolovits** (Brodeur & Rodman AI and Clinical Reasoning). Keyword-feed HIGHs: **`"phenotype risk scores"`** (Johnson et al. JACC Case Reports — **PheRS-triggered e-visit pathway for TTR V142I** in a heart-failure population); **`rare diseases`** (Zaripova et al. arXiv 2609.18431 — **HPOQuest active-phenotype-acquisition rare-disease agent**); **`"variant interpretation" OR "variant classification"`** (Jodarski et al. Front Pharmacol — **KCNMA1 multi-evidence variant-interpretation framework**); **`intitle:"clonal hematopoiesis"`** (Wang et al. J Immunol — **TET2-driven CH exacerbates inflammatory bone loss**; Timonina EPFL thesis — **CH in people with HIV**); **`"phenome wide association studies"`** (Luo et al. PLOS Medicine — **accelerometer-derived sleep-stage PheWAS in UKB**); **`"All of Us research program"`** (Celik 2026 — patient-reported global physical health × postop AKI in AoU); **`"electronic health records"`** (Jayanthi et al. Sci Reports — hepatitis survival DNN); **`"UK Biobank"`** (Ge et al. J Transl Genet Genomics — gout multi-dimensional risk-factor review); **`Foundation models and "electronic health records"`** (Samuel 2026 — chronic-disease prevention national model, thesis-level, LOW). |
| Google Scholar alerts (09-18 batch, 16:43Z) | 09-18 16:43Z | Feeds fired: Peter Szolovits (Brodeur & Rodman AI-and-Clinical-Reasoning book chapter), Leo Anthony Celi (Ordóñez et al. ModaLens image-sensitivity audit for report-conditioned medical VLMs), Marinka Zitnik (Liu et al. Gene-Chronos parameter-efficient developmental-time inference on scFM), Vivek Natarajan (Schaekermann et al. Nat Med "prospective evidence for conversational medical AI is hard, but non-negotiable"), Zhiyong Lu (Tiwari et al. competence-gated pooling for event forecasting — off-thread). |
| Google Scholar alerts (09-01 → 09-17 backlog) | 09-01 → 09-17 | Between the prior report and the recent push, several keyword feeds fired but the highest-signal items already surfaced in the 09-19/09-20 batches (the alerts often re-fire once a paper picks up citations). The `mendelian diseases`, `"autoimmune disorders"`, `"drug repurposing"`, and `"Cystic fibrosis carriers"` feeds fired 09-20 with no HIGH new items relative to your active threads. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Thirteen HIGH items surfaced this window, clustering into six knots:

**Your own new work (1 item — top of the digest).** Zeng, Raraigh,
Cutting, Denny *J Cystic Fibrosis* 2026 (NACFC 2026 Poster 646) —
**Longitudinal disease burden and drug-safety profiles of CFTR modulator
therapy in cystic fibrosis: a real-world analysis from the NIH All of
Us Research Program**. Denny author-feed picked it up on 09-19. This is
the CFTR-modulator pharmacoepi × AoU × real-world-safety intersection
that anchors your active `Specific disease threads → Cystic fibrosis /
CFTR` sub-thread, so it is called out separately from the other twelve
items. Detailed report §1.

**PheWAS / PheRS operationalization cluster (2 items).** Johnson et al.
*JACC: Case Reports* 2026 (Vanderbilt / VUMC PheRS lineage) —
**PheRS-triggered e-visit pathway to capture TTR V142I in a heart-failure
population**. First-in-print operationalization of a PheRS score into a
prospective care-delivery workflow to identify carriers of a
population-specific pathogenic variant. Direct-hit paper for `PheWAS /
phecode infrastructure` and for the `penetrance under population-
screening conditions` framing. Luo et al. *PLOS Medicine* 2026 —
**Accelerometer-derived real-world sleep stages and risk of incident
diseases: A UK Biobank cohort study and PheWAS**. Uses UKB accelerometer
sleep-stage exposure with a phecode-based PheWAS outcome grid; embeds
the phecode-vs-CCS-vs-ICD9 comparison and cites it explicitly. Both
serve the PheWAS thread but from opposite ends (score → care vs.
exposure → phenome). Detailed reports §2–3.

**Variant interpretation + HPO-driven diagnosis cluster (3 items).**
Ghasemnejad et al. arXiv 2609.19569 (`digests/2026-09-18.md`) —
**LLM ReAct+RAG agent** for HPO-scale disease-severity classification
across 10,211 HPO terms, aligned to ACMG severity + ACOG QoL guidelines,
with PubMed literature retrieval, 93.55% phenotype-level accuracy,
82.6–91.4% claim-support rate, and 95.2% concordance with Mackenzie's
Mission on external validation. Zaripova et al. arXiv 2609.18431
(rare-diseases keyword feed) — **HPOQuest** rare-disease diagnostic
agent with active phenotype acquisition; positioned as an update in the
**Auditable HPO-driven diagnostic benchmarks** sub-thread you flagged
alongside GraphRareBench, Phenolyzer, Phen2Gene, PhenoSV, LIRICAL,
Exomiser, and PhenoGPT2. Jodarski et al. *Front Pharmacol* 2026 —
**KCNMA1 multi-evidence variant-interpretation framework** combining
population frequency, segregation, computational predictions, and
functional evidence in the ClinGen-style multi-evidence idiom. Detailed
reports §4–6.

**EHR foundation-models / causal-representation-audit cluster (3
items).** Fujita & Hattori arXiv 2609.17777 (`digests/2026-09-17.md`) —
**Information-Set Emulation: Causal Certificates for AI-Derived EHR
Features**. A typed-lift/certificate architecture for auditing whether
LLM-extracted EHR features can support causal roles under a locked
target-trial estimand, with cross-fitted AIPW estimation and an
"EHR compression-drift" identity — reads as a formal specification of
the same "when representation choices leak or preserve information at
prediction time" concern you called out in `Knowledge representation in
EHRs and applications → Structural and temporal representation of the
patient timeline`. Gronsbell, Cai, Mukherjee, Varghese 2026
(Hripcsak-feed-adjacent) — **Responsible AI with EHR data**: framing
paper on AI decision-making, evaluation, and fairness against EHR data.
Snel & Schulz arXiv 2609.07729 (`digests/2026-09-09.md`) — **`pyinfluence`
Cohen's-d training-data attribution** in UKB normative-age biomarker
models: removing 10% of most influential training samples more than
doubles the metabolomic-age effect for type-2 diabetes and raises the
brain-age effect for MS by ~1/3, recovering HbA1c as the marker driving
the T2D gain even though the model never sees it. A portable audit
template for the `Fidelity, portability, and audit of representations`
sub-thread. Detailed reports §7–9.

**Somatic mosaicism / CHIP cluster (1 item).** Wang et al.
*J Immunology* 2026 (Vanderbilt-adjacent lineage) — **TET2-driven
CHIP exacerbates inflammatory bone loss**. Mechanistic BM-niche paper
in the somatic-mosaicism / CHIP thread; complements the CHIP-cardiac
and CHIP-hematologic lines already in your INTERESTS.md and gives a
new comorbidity axis (bone loss / periodontal) to layer onto AoU + UKB
PheWAS scans of TET2 CH carriers. Detailed report §10.

**Chronic-disease clustering / disease-progression cluster (2 items).**
Semchin et al. arXiv 2609.10890 (`digests/2026-09-11.md`) —
**Connectome-constrained dynamic model** of Parkinson's disease
progression on PPMI, recovering four data-driven subtypes that
correspond significantly to clinical motor subtypes AND genetic
variants; benchmarks against SuStaIn. Wang et al. arXiv 2609.15584
(`digests/2026-09-16.md`) — **Multiscale ABM→PDE model of NTM×CF
mucociliary clearance**; explicitly ends with the "patient-specific
digital twins" framing that maps to your `EHR foundation models →
Digital twins from EHR data` sub-thread, transposed to a
respiratory-infection setting in CF. Devarakonda arXiv 2609.10831
(`digests/2026-09-11.md`) — **scDEFT** drug-effect prediction and
**counterfactual reasoning** on a harmonized 1.16M-cell IBD atlas
across three cohorts and two drug classes, with pre-treatment
responder stratification at AUROC 0.70 where standard predictors are
at chance. Bridges `IBD` disease thread × causal ML × precision-health.
Detailed reports §11–13.

---

## Detailed study reports

### §1. Zeng, Raraigh, Cutting, Denny — *J Cystic Fibrosis* 2026 (Poster 646, NACFC 2026)

- **Title:** *Longitudinal disease burden and drug-safety profiles of
  CFTR modulator therapy in cystic fibrosis: a real-world analysis from
  the NIH All of Us Research Program.*
- **Venue / ID:** *J Cystic Fibrosis* 2026, poster abstract
  (S1569199326023611). NACFC 2026 Poster 646.
- **Alert path:** Joshua C. Denny author-feed, 09-19 22:22Z.
- **Thread hit:** `Specific disease threads → Cystic fibrosis / CFTR`
  (real-world modulator outcomes and safety); `Biobanks → All of Us`;
  `Causal inference and pharmacoepidemiology`.
- **What the abstract snippet says:** CFTR modulators have transformed
  CF care but real-world data on long-term multi-organ outcomes and
  drug safety remain limited. The abstract sets up the question as
  "the trajectory of CF-specific disease burden and the distinction
  between improving [and worsening manifestations]…" — snippet
  truncated. First author is you; senior author is Denny.
- **Why HIGH:** This is your own work landing in the venue that anchors
  the CF modulator field, using the AoU EHR-linked cohort as the
  real-world substrate — the precise intersection of `Cystic fibrosis
  / CFTR`, `Biobanks with EHR linkage`, and `Causal inference and
  pharmacoepidemiology` in your INTERESTS.md.
- **Follow-up:** Confirm the poster listing shows on the JCF NACFC
  2026 supplement page and pull the full poster PDF from your local
  archive if you want the graphics for the report thread. No action
  from this digest — this row is here as a marker so the alert doesn't
  read as "someone else scooped you."

### §2. Johnson et al. — *JACC: Case Reports* 2026

- **Title:** *A Phenotype Risk Score-Triggered E-Visit Pathway to
  Capture TTR V142I in a Heart Failure Population.*
- **Venue / ID:** *JACC: Case Reports* 2026,
  10.1016/j.jaccas.2026.110259.
- **Alert path:** `"phenotype risk scores"` keyword feed, 09-20 03:33Z.
- **Thread hit:** `PheWAS / phecode infrastructure → penetrance
  estimation for monogenic variants under population-screening
  conditions`; secondary hit on `Machine learning for precision health
  → tied to a clinical decision`.
- **What the abstract says:** Variant transthyretin amyloidosis
  (ATTRv) is under-diagnosed as a cause of heart failure and typically
  caught only at late disease stages. TTR p.Val142Ile (V142I) is found
  in ~4% of African American individuals and is the most common
  amyloidogenic TTR variant. The paper describes a PheRS-triggered
  e-visit pathway operationalized in a heart-failure population to
  prospectively identify likely V142I carriers for confirmatory testing.
- **Why HIGH:** This is the direct clinical operationalization of the
  PheRS score class you work in — the first case-report-level
  demonstration of PheRS-triggered *care delivery* (not just PheRS-
  triggered screening). It closes the loop from `Bastarache-style PheRS`
  → `identified variant carriers` → `care-delivery mechanism (e-visit)`
  in an ancestry-enriched cohort. The V142I ~4% AA prevalence framing
  also touches the `ancestry-aware risk scores` sub-thread.
- **Follow-up:** Worth reading full-text to see what PheRS training set
  was used, threshold calibration, and how e-visit conversion rate
  compared to background referral. A one-paragraph note might slot into
  the PheRS-methods section of any current writeup you're drafting.

### §3. Luo et al. — *PLOS Medicine* 2026

- **Title:** *Accelerometer-derived real-world sleep stages and risk of
  incident diseases: A UK Biobank cohort study and phenome-wide
  association analysis.*
- **Venue / ID:** *PLOS Medicine* 2026,
  10.1371/journal.pmed.1005213.
- **Alert path:** `"phenome wide association studies"` keyword feed,
  09-20 03:33Z.
- **Thread hit:** `PheWAS / phecode infrastructure`; `Biobanks with EHR
  linkage → UK Biobank`; `Chronic disease clustering and multimorbidity
  → sleep-EHR pattern connections`.
- **What the abstract snippet says:** UK Biobank cohort with wrist
  accelerometer-derived sleep-stage percentages as the exposure and an
  incident-disease PheWAS as the outcome grid. FDR-adjusted phenome
  scans across incident phecodes, with an explicit methodological
  section citing the phecode-vs-CCS-vs-ICD9 comparison for PheWAS.
- **Why HIGH:** Direct-hit PheWAS methodology paper: real-world
  exposure × phecode outcome grid at UK Biobank scale. The exposure
  side (accelerometry-derived multi-state sleep) is the kind of
  wearable-derived quantitative exposure that increasingly shows up in
  UKB PheWAS, and the outcome side is the phecode PheWAS grammar you
  work in. The paper explicitly compares phecodes vs CCS vs ICD9-CM
  for PheWAS — worth cribbing for methods citations.
- **Follow-up:** Pull for methods citations. If sleep exposure is
  something the CF-modulator side wants to look at (sleep-disordered
  breathing is a common comorbidity in CF adults), this becomes a
  double-thread hit.

### §4. Ghasemnejad et al. — arXiv 2609.19569 (`digests/2026-09-18.md`)

- **Title:** *Large Language Model Agents for Evidence Based Genetic
  Disease Severity Classification.*
- **Authors:** Ghasemnejad, Argha, Grosser, Wang, Yang, Porntaveetus,
  Roscioli, Lovell, Aarabi, Alinejad-Rokny.
- **Venue / ID:** arXiv 2609.19569v1, 2026-09-17.
- **Alert path:** `arxiv-digest` local cron, `digests/2026-09-18.md`;
  keyword hits `acmg` and `human phenotype ontology`; score 2.
- **Thread hit:** `Variant interpretation (ACMG / ClinGen)`; `Rare
  disease → auditable HPO-driven diagnostic benchmarks`;
  `Knowledge representation in EHRs → NLP-derived representations` and
  `Applications to prioritize`.
- **What the abstract says:** ReAct-agent + RAG architecture over the
  full 10,211-term HPO, aligned to ACMG-endorsed severity guidelines
  and ACOG quality-of-life criteria, retrieving PubMed literature and
  generating interpretable reasoning chains with independent claim
  verification. At the phenotype level, 93.55% accuracy (MCC 0.9237)
  vs. expert-curated cohorts, with 82.6-91.4% of claims supported by
  direct evidence or valid inferences. Gene-level aggregation across
  8,738 pairs identified 3,283 autosomal-recessive severe/profound
  presentations. External validation: 95.2% concordance with
  Mackenzie's Mission gene list. Framed as an aid to panel design.
- **Why HIGH:** This is the most rigorous ACMG-aligned LLM-agent
  paper the digest has surfaced this year. Two things stand out for
  your threads: (1) the *evidence-coverage-rate* metric (82.6-91.4%)
  is exactly the kind of separable "ranking vs. evidence" audit you
  called out in the GraphRareBench sub-thread — it forces the agent
  to earn its severity call, not just make it; (2) the 95.2%
  concordance with Mackenzie's Mission is a real external-validation
  benchmark, not a benchmark leaderboard.
- **Follow-up:** Cross-link this in the INTERESTS.md `auditable HPO-
  driven diagnostic benchmarks` sub-thread alongside GraphRareBench
  and PhenoGPT2. The claim-support metric is directly portable to
  ClinGen VCEP work and to any CFTR-VCEP variant-severity tooling
  you're auditing.

### §5. Zaripova et al. — arXiv 2609.18431

- **Title:** *HPOQuest: A Rare-Disease Diagnostic Agent Using Active
  Phenotype Acquisition.*
- **Authors:** Zaripova, Navab, Farshad, Marsico.
- **Venue / ID:** arXiv 2609.18431, 2026 preprint (TUM Navab lab).
- **Alert path:** `rare diseases` keyword feed, 09-20 03:33Z.
- **Thread hit:** `Rare disease → auditable HPO-driven diagnostic
  benchmarks with separable metrics for ranking vs. evidence coverage`;
  `Knowledge graphs & ontologies → HPO`.
- **What the abstract snippet says:** Framed as an LLM agent for rare-
  disease diagnosis that *actively* acquires phenotypes (as opposed to
  ingesting a fixed HPO list) — i.e., adaptive query strategies for
  the phenotyping side of the pipeline. Full text needed to know the
  benchmark, but from the TUM group's prior work this is likely on
  the MyGene2 / Human Phenotype Ontology test cohorts.
- **Why HIGH:** Fits directly into the same INTERESTS.md sub-thread
  as §4 and as GraphRareBench (Guo et al. arXiv 2607.24878), and
  extends the sub-thread's "ranking vs. evidence coverage" separable-
  metrics agenda to *what phenotypes the agent chooses to ask about
  next* — active phenotype acquisition is a distinct axis of
  auditability from claim-verification (which §4 handles) and from
  ranking-of-confounders (which GraphRareBench handles).
- **Follow-up:** Worth reading in parallel with §4 as a joint mini-
  review of "auditable HPO-driven diagnostic agents in Sept 2026." A
  brief note into INTERESTS.md linking §4 + §5 + GraphRareBench as the
  current state of that sub-thread would keep the anchor current.

### §6. Jodarski et al. — *Frontiers in Pharmacology* 2026

- **Title:** *Bridging Genotype and Clinical Phenotype: A Multi-Evidence
  Framework for KCNMA1 Variant Interpretation.*
- **Authors:** Jodarski, Shomali, Harvey, Keros et al.
- **Venue / ID:** *Front Pharmacol* 2026,
  10.3389/fphar.2026.1944273.
- **Alert path:** `"variant interpretation" OR "variant classification"`
  keyword feed, 09-20 03:33Z.
- **Thread hit:** `Variant interpretation (ACMG / ClinGen)` — direct
  hit. Secondary hit on `Rare disease` (KCNMA1 syndrome is ultra-rare).
- **What the abstract snippet says:** A multi-evidence variant-
  interpretation framework for KCNMA1 spanning population frequency,
  segregation and allelic data, computational predictions, and
  functional studies. Positions itself as a standardized replacement
  for the ad-hoc classifications in current KCNMA1 literature.
- **Why HIGH:** Textbook example of the ClinGen VCEP-style multi-
  evidence idiom for a single gene, in a pharmacology venue. Uses
  exactly the population-frequency + segregation + computational +
  functional-evidence layering pattern your ACMG-AMP thread tracks,
  transferable in structure to CFTR and other genes.
- **Follow-up:** Bookmark as a template for how a small gene-specific
  VCEP writeup can look when it lands in a pharmacology venue rather
  than a genetics venue.

### §7. Fujita & Hattori — arXiv 2609.17777 (`digests/2026-09-17.md`)

- **Title:** *Information Set Emulation: Causal Certificates for AI
  Derived EHR Features.*
- **Venue / ID:** arXiv 2609.17777v1, 2026-09-15 (stat.ME primary).
- **Alert path:** `arxiv-digest` local cron; keyword hits `electronic
  health records`, `inverse probability`, `causal inference`; score 3.
- **Thread hit:** `Causal inference and pharmacoepidemiology`;
  `EHR foundation models → Pretraining-contamination audits`;
  `Knowledge representation in EHRs → Structural and temporal
  representation of the patient timeline`.
- **What the abstract says:** Introduces "information set emulation":
  a typed lift attaching to each LLM-extracted EHR feature (a) source
  evidence, (b) clinical and recording times, (c) decision-time
  availability, (d) representation version, (e) proposed causal role,
  and (f) unresolved ambiguity — under a *locked* target-trial
  estimand. "Causal certificates" record the auditable evidence for
  each proposed role, and features with unresolved downstream roles
  are routed to compatible reporting rather than into the primary
  analysis. The typed evidence defines an observational fiber; the
  squared Chebyshev radius equals the residual minimax MSE when the
  compatible image is nonempty and compact. Cross-fitted AIPW
  estimation. Establishes an "EHR compression-drift" identity that
  separates the roles of frame presence, treatment assignment, and
  outcome observation. All experiments are synthetic (this is a
  framework paper).
- **Why HIGH:** This paper is the most explicit *formal* answer yet to
  the concern your `Knowledge representation in EHRs` thread flags
  under "representation choices that leak or preserve label
  information at prediction time." Instead of asking "does this LLM-
  extracted feature help prediction?" it asks "under this locked
  target-trial estimand, can this feature carry the causal role you
  are about to assign to it, and how much information ambiguity does
  it introduce?" The certificate architecture is portable to any TTE
  pipeline that uses LLM-derived structured features, including the
  CFTR-modulator pharmacoepi work.
- **Follow-up:** Worth reading properly (framework paper, so full
  read is needed). Flag it in the causal-inference thread and next to
  the OCI-agent / Chou-Kallus paper as another item in the
  "auditable-features-under-a-locked-estimand" family.

### §8. Gronsbell, Cai, Mukherjee, Varghese — *Responsible AI with EHR Data* 2026

- **Title:** *Responsible AI with Electronic Health Records Data.*
- **Venue / ID:** 2026 (venue not confirmed from snippet; likely a
  perspective/review piece — no journal-line in the alert).
- **Alert path:** George Hripcsak new-related-research feed,
  09-19 22:22Z.
- **Thread hit:** `EHR foundation models → Foundation-model fairness
  and calibration audits when grounded in EHR data`; secondary hit on
  `Knowledge representation in EHRs → Fidelity, portability, and audit
  of representations`.
- **What the abstract snippet says:** Framing piece: AI has immense
  potential in healthcare decision-making; the piece is aimed at the
  responsible-AI question around EHR-grounded models. From the author
  set (Gronsbell + Cai + Mukherjee + Varghese) this reads as an EHR-
  statistics-methods perspective, not a policy piece.
- **Why HIGH-ish:** This is a perspective/methods piece from a
  cross-institution author list that has authored several of the
  reference audits in your representation-thread. Even the abstract-
  snippet framing ("decision making across healthcare") suggests it
  will be a useful citation-anchor for the *responsible-use* wrapper
  around EHR-FM work you already track (CLMBR / MOTOR / EHRSHOT /
  MedTok / FEMR / MEDS lineage in your INTERESTS.md).
- **Follow-up:** Pull the full text when it becomes available (Scholar
  usually indexes new-related items a few days ahead of PMC).

### §9. Snel & Schulz — arXiv 2609.07729 (`digests/2026-09-09.md`)

- **Title:** *Attributing Cohen's d: Training Data Attribution for
  Disease-Related Effects in Normative Age Biomarkers.*
- **Venue / ID:** arXiv 2609.07729v1, 2026-09-07 (cs.LG primary).
- **Alert path:** `arxiv-digest` local cron; keyword hits `uk biobank`,
  `biobank`; score 2.
- **Thread hit:** `Biobanks with EHR linkage → UK Biobank`; `Genetic
  epidemiology → biomarker-as-exposure scans`; `Knowledge
  representation in EHRs → Fidelity, portability, and audit of
  representations`.
- **What the abstract says:** Normative-age models are trained on
  nominally healthy cohorts to predict chronological age. Applied to
  patients, the *age gap* is read as disease risk. This paper attributes
  the disease-related Cohen's d of that age gap directly to individual
  training samples (a closed-form influence functional, validated
  against leave-one-out). Across four diseases × two biomarker
  modalities in UK Biobank, removing the 10% most influential training
  samples raises the held-out case/control effect size in every seed:
  the metabolomic-age effect for T2D more than doubles; the brain-age
  effect for MS rises by ~1/3. Random removal leaves effect flat at
  even 50%. Flagged subjects carry subclinical cardiometabolic burden
  that diagnosis-based exclusion misses — for T2D, the recovered
  driver is HbA1c on markers the model never sees. Releases
  `pyinfluence`.
- **Why HIGH:** Directly serves the *audit-representations-against-
  ground-truth* sub-thread. The paper is a UKB-native audit tool that
  can be pointed at any biomarker model (Olink proteomic-age, NMR
  metabolomic-age, brain-age, etc.) to identify subclinical-burden
  subjects hiding in the "healthy" reference cohort. The `pyinfluence`
  release makes it directly reproducible on AoU-derived biomarker
  models.
- **Follow-up:** `pyinfluence` is worth taking for a spin against any
  ancestry-stratified UKB-derived biomarker model you're building.
  Especially useful for the `PGS residuals / polygenic-deviation
  designs` sub-thread of your Genetic epidemiology thread: it gives a
  training-data-level attribution complementary to the outcome-level
  "misaligned individuals" framing.

### §10. Wang et al. — *The Journal of Immunology* 2026

- **Title:** *Exacerbation of inflammatory bone loss in TET2-driven
  clonal hematopoiesis.*
- **Authors:** Wang, Hu, Barovic, Pan, Cheng, X. Li, Y. Li et al.
- **Venue / ID:** *J Immunol* 2026, 215(9): vkag248.
- **Alert path:** `intitle:"clonal hematopoiesis"` keyword feed,
  09-20 03:33Z.
- **Thread hit:** `Specific disease threads → CHIP, VEXAS, and mosaic
  Loss of Y (LOY) → somatic mosaicism generally`.
- **What the abstract snippet says:** CHIP arises from age-related
  somatic mutations in HSCs, with clonal expansion and altered
  phenotypes; loss-of-function mutations in TET2 are among the most
  common drivers. This paper reports that TET2-driven CH exacerbates
  inflammatory bone loss in a BM-niche model.
- **Why HIGH:** Direct-hit on the CHIP thread with a new comorbidity
  axis (bone loss, likely periodontal / osteoporotic) added on top of
  the CHIP × cardiovascular and CHIP × hematologic lines you already
  track. In an AoU or UKB PheWAS scan of TET2 CH carriers, this
  suggests scanning phecodes 731.* (osteoporosis / bone-density loss)
  and 523.* (periodontal disease) as pre-registered hypothesis-driven
  hits, not exploratory noise.
- **Follow-up:** Companion review paper in the same alert batch —
  "Silent, but Not Innocent" (Emre Unsal *Front Oncol* 2026) — is a
  useful review-anchor for the CHIP → therapy-related myeloid
  neoplasms edge. Timonina EPFL 2026 thesis on CH in people with HIV
  is a methods thesis you can pull if you ever want the sensitivity
  analyses around HIV-related VAF calibration.

### §11. Semchin et al. — arXiv 2609.10890 (`digests/2026-09-11.md`)

- **Title:** *Discovering Subtypes of Neurodegenerative Progression
  with a Scalable Connectome-Constrained Dynamic Model.*
- **Authors:** Semchin, d'Angremont, Ding, Antar, Lorenzi, Arfanakis,
  van der Werf, Thompson, Gutman.
- **Venue / ID:** arXiv 2609.10890v1, 2026-09-09 (q-bio.QM primary).
- **Alert path:** `arxiv-digest` local cron; keyword hit `motor`;
  score 1.
- **Thread hit:** `Chronic disease clustering and multimorbidity`;
  secondary hit on `Machine learning for precision health`.
- **What the abstract says:** A connectome-constrained disease-
  progression model that jointly estimates subject-specific disease
  time and data-driven subtypes from longitudinal morphometry. Applied
  to 85 imaging + clinical biomarkers from PPMI. Recovers four
  morphologically distinct progression subtypes. Validated on a hold-
  out cross-sectional dataset; benchmarked against SuStaIn. Only this
  method (per the authors) recovers subtypes that correspond
  significantly to clinical motor subtypes *and* genetic variants of
  Parkinson's disease.
- **Why HIGH:** This is the kind of disease-trajectory / progression-
  subtype paper your `Chronic disease clustering and multimorbidity`
  thread targets, done in a way that ties subtypes to *both* clinical
  motor phenotypes and genetics — which most SuStaIn-style analyses
  don't achieve. Portable in principle to any longitudinal biobank
  imaging cohort. In an AoU imaging-substudy or UKB imaging-cohort
  world, the same idiom (longitudinal morphometry → subject-specific
  disease-time + subtype → correspondence to clinical + genetic
  labels) is directly applicable.
- **Follow-up:** Keep as a methods citation for any progression-
  subtype work you plan. Note the benchmark-against-SuStaIn detail —
  SuStaIn is the standard baseline in this space, and any manuscript
  in this area should include it.

### §12. Wang et al. — arXiv 2609.15584 (`digests/2026-09-16.md`)

- **Title:** *Multiscale modeling of host-pathogen interactions and
  mucociliary clearance during non-tuberculous mycobacterial pulmonary
  infection.*
- **Authors:** J. Wang, Konstantinopoulos, Kuo, Cai, Wei, Pienaar, Hao.
- **Venue / ID:** arXiv 2609.15584v1, 2026-09-14 (q-bio.QM primary).
- **Alert path:** `arxiv-digest` local cron; keyword hit `cystic
  fibrosis`; score 1.
- **Thread hit:** `Specific disease threads → Cystic fibrosis / CFTR`
  (NTM comorbidity); `EHR foundation models → Digital twins from EHR
  data` (framing).
- **What the abstract says:** ABM (agent-based model) → PDE
  (partial-differential-equation) coupling for NTM infection in CF-
  like airway conditions: mucus viscosity, bacterial diffusivity, and
  macrophage mobility identified as key regulators; mucolytic-therapy
  simulations show that *excessive* viscosity reduction can push
  bacteria into lung tissue. The paper closes with the explicit
  framing: "provides a quantitative platform for studying pulmonary
  infections, evaluating therapies, and developing patient-specific
  digital twins."
- **Why HIGH:** Two threads. (1) Direct hit on the CF disease thread
  as a mechanistic model of an NTM comorbidity that is clinically
  relevant to CF-modulator-treated patients (NTM prevalence in adult
  CF is 10-20% depending on cohort). (2) An external, non-EHR
  instantiation of the *digital-twin* framing you flagged in
  `EHR foundation models → Digital twins from EHR data` — a good
  reference for how physics-based digital twins can pair with EHR-
  learned digital twins.
- **Follow-up:** If any of the AoU-CFTR-modulator work touches NTM
  as a co-outcome, this paper is a useful mechanistic anchor for
  why NTM burden should not be treated as a static covariate.

### §13. Devarakonda — arXiv 2609.10831 (`digests/2026-09-11.md`)

- **Title:** *scDEFT: A deep learning framework for drug-effect
  prediction and counterfactual reasoning.*
- **Venue / ID:** arXiv 2609.10831v1, 2026-09-09 (q-bio.QM primary).
- **Alert path:** `arxiv-digest` local cron; keyword hits
  `inflammatory bowel disease`, `patient stratification`; score 2.
- **Thread hit:** `Specific disease threads → Inflammatory bowel
  disease`; `Machine learning for precision health → treatment-
  effect heterogeneity`; `Causal inference and pharmacoepidemiology`
  (counterfactual reasoning).
- **What the abstract says:** Treats a drug as a conditioning operator
  on single-cell representations (FiLM-based) and uses two heads to
  predict drug-induced state change AND responder status. Backward
  stage ranks latent dimensions by responder-nonresponder separation
  and maps them to genes under a cell-composition control. On a
  harmonized IBD atlas of 1.16M cells across three cohorts and two
  drug classes: predicts state change at 45% of the reproducibility-
  ceiling headroom and stratifies responders *before treatment* at
  AUROC 0.70, where standard predictors are at chance. Supports
  target-and-co-target nomination, patient stratification, and
  counterfactual prediction of unseen drug-cohort effects.
- **Why HIGH:** Triple-thread hit — the IBD disease thread, causal-
  inference (counterfactual scDEFT predictions), and precision-health
  (pre-treatment responder stratification tied to a clinical
  decision). AUROC-0.70 pre-treatment responder stratification is a
  clinically meaningful gain in IBD.
- **Follow-up:** Fits neatly next to the pre-treatment-responder /
  HTE work in your causal-ML pipeline. If any current writeup touches
  responder-vs-non-responder stratification, this is a citation-anchor.

---

## METHODS-WATCH (worth remembering, not deep-reading)

- **Csillag Finger & Possebom** arXiv 2609.20473 (`digests/2026-09-
  18.md`) — semiparametric solutions to contamination bias with
  *multi-valued* treatments. Reanalyzes 18 regressions across 11
  studies. Direct utility for any TTE work using multi-arm drug
  comparisons (e.g., GLP-1 RA vs. SGLT2i vs. DPP4i, or the CFTR-
  modulator triple-therapy vs. dual vs. monotherapy design).
- **Yu et al.** arXiv 2609.04018 (`digests/2026-09-04.md`) — location-
  invariant extremal QTE estimator with IPW. For heavy-tailed potential
  outcomes; matters whenever the outcome is a hospitalization-cost or
  length-of-stay measure that is heavy-tailed and where the tail is
  the clinically interesting part.
- **Lee, Rempala, Schnell** arXiv 2609.09325 (`digests/2026-09-10.md`)
  — Kalman-filtered Horvitz-Thompson prevalence estimation for real-
  time infectious-disease surveillance. Off-thread for main threads
  but useful methods-anchor for any real-time-surveillance work.
- **Rajabli & Collins** arXiv 2609.05400 (`digests/2026-09-07.md`) —
  LoRA-adapted 7.18M-parameter brain-age 3D CNN as a reusable
  foundation model for AD tasks (~1% extra parameters). A compact
  counter-example to the "bigger FM is always better" narrative;
  worth flagging in the `EHR foundation models → Pretraining-
  contamination audits` sub-thread as evidence that a supervised
  compact backbone can serve as a foundation model.
- **Hendrix et al.** arXiv 2609.11689 (`digests/2026-09-11.md`) —
  geospatial FM audit against ADI/SDI/SVI; up to 54% of residual
  variance in health-behavior outcomes captured beyond social-risk
  indices. Useful for any AoU-place-based analysis where you want to
  argue that geospatial-FM covariates are non-redundant with the
  standard SDoH bundle.
- **Zhang et al.** *scKITE* arXiv 2609.14970 (`digests/2026-09-
  16.md`) — knowledge-enhanced scFM that outperforms strong scFMs with
  <0.5% of pretraining data by using cell-annotation and gene-
  regulatory supervision. Method-anchor for the *KG-augmented FM*
  design pattern.
- **Ostropolets et al.** *"George Hripcsak - new articles"* — Real-
  World Use of Controlled Terminologies, Ontologies, and Vocabularies
  for Evidence Generation Across a Large International Observational
  Network. Directly serves the OMOP-CDM vocabulary sub-thread.
- **Ihara et al.** *"Patrick Ryan - new related research"* — active
  vs. non-active comparators in PPI × ICI mortality studies. Comparator-
  choice methods paper, useful reference for the comparator-selection
  subtlety in any drug-safety TTE.
- **Yuan et al.** *Asclepius* arXiv 2609.13543 — adaptive harness for
  long-horizon clinical LLM agents (Rajpurkar feed). Off-thread for
  your primary threads but a bookmark-worthy benchmarking scaffold.
- **Wang et al.** *CLEAR* arXiv 2609.16301 — cross-source evidence
  adjudication for medical LLMs (Lu feed). Adjacent to §4/§5 in the
  auditable-agent family.
- **Hu et al.** *"Dynamic medical knowledge graph updating method
  based on LLM decision control"* (*Sci Reports* 2026) — medical-KG
  maintenance via LLM. Methods-watch item for the KG thread.
- **Liu et al.** *"A plasma proteomic atlas of the ocular disease
  phenome"* (*Science China Life Sci* 2026, Bastarache feed) — Olink
  proteomic PheWAS of ocular disease. Useful reference for the
  proteomics-PheWAS combination and for the `Multi-omics-augmented
  PRS` sub-thread.

---

## SKIP-worthy noise (documented for completeness, not for reading)

- Ramesh et al. mudskippers (`digests/2026-09-02.md`) — `motor`
  keyword false-positive.
- Wu et al. FUSE-RT HPLC retention-time FM (`digests/2026-09-09.md`)
  — `foundation model` keyword, off-thread.
- Cortez-Rodriguez natural-disaster nonprofit CI (`digests/2026-09-
  04.md`) — `causal inference` keyword, off-thread.
- Samuel 2026 "AI for Sustainable Healthcare" thesis-style piece —
  broad-keyword hit on `Foundation models and "electronic health
  records"`; not a research paper in the sense the digest tracks.
- Spahiu & Roveda embodied KGs (Callahan feed) — off-thread.
- Ho et al. LMs controlling their own attention (Zitnik feed) —
  off-thread ML.
- Jayanthi et al. hepatitis DNN (*Sci Reports* 2026) — broad EHR
  keyword hit, off-thread.
- Various rare-disease case reports (Phacomatosis pigmentovascularis,
  Langerhans cell histiocytosis, biotinidase deficiency, chorea-
  predominant SCA5, cytochrome P450 oxidoreductase deficiency, TBX1
  hypoparathyroidism) — case reports, useful anchors if a specific
  gene comes up, otherwise SKIP.

---

## What to update in `INTERESTS.md`

- **`Rare disease → Auditable HPO-driven diagnostic benchmarks`** —
  extend the anchor line to reference Ghasemnejad et al. arXiv
  2609.19569 (claim-support-rate metric, ACMG+ACOG-aligned) and
  Zaripova et al. arXiv 2609.18431 (HPOQuest, active phenotype
  acquisition) as the September 2026 update to the sub-thread. The
  three papers (GraphRareBench, HPOQuest, Ghasemnejad-agent) span
  ranking, active-acquisition, and evidence-verification as three
  distinct auditability axes.
- **`Specific disease threads → CHIP / VEXAS / LOY`** — add a note
  about the bone-loss / periodontal comorbidity axis raised by Wang et
  al. *J Immunol* 2026, complementing the cardiovascular and
  hematologic edges already listed.
- **`Knowledge representation in EHRs → Structural and temporal
  representation`** — flag Fujita & Hattori arXiv 2609.17777 as the
  reference paper for the "typed evidence + certificate architecture
  under a locked estimand" idiom.
- **`Knowledge representation in EHRs → Fidelity, portability, and
  audit of representations`** — flag Snel & Schulz `pyinfluence` as
  the training-data-attribution complement to outcome-level audit
  approaches.
- **No new threads needed**: everything in this window slots into
  existing threads.

---

*Report generated 2026-09-20 as a scheduled routine run. This report
reflects the state of the arxiv-digest repository at commit `94ffea7`
(Daily digest 2026-09-19) and the Gmail research-alert inbox through
approximately 09-20 12:30Z.*
