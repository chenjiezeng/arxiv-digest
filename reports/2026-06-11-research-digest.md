# Research digest report — 2026-06-11

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity). Picks up where the 2026-05-29 report
left off.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | ~2026-05-30 → 06-11 | Author alerts (Denny, Bick, Bastarache, Callahan, Chute, Hripcsak, Karczewski, Ryan, Brandt, Hernán, Yang, Pritchard, Montgomery, Kastner, Sontag, Celi, Collins, Snyder, Natarajan, Szolovits, Zitnik) + keyword alerts (UK Biobank, All of Us, drug repurposing, variant interpretation, rare diseases, EHR, knowledge graph, PheWAS, mendelian, foundation models + EHR). |
| `arxiv-digest` repo (`digests/`) | 2026-05-30 → 06-10 | Auto-triaged q-bio.QM/GN/PE + stat.AP. Five days were empty (`No matches`) or category-fetch failures; only 06-06, 06-09, 06-10 produced relevant hits — and all score-1/2 incidental. |
| Raw arXiv daily mailings (`no-reply@arxiv.org`) | daily | Full unfiltered cs/q-bio/stat listings to a list address; not individually triaged here (this is exactly what the digest pipeline is meant to filter). |

> Caveat: Scholar alert emails contain title, authors, venue, and the first
> ~2–3 lines of each abstract only. The "detailed report" per study below
> contextualizes that metadata against your research threads; it does not
> reflect a full-text read, and no quantitative result is stated unless it
> appeared in the alert.

---

## Executive summary

- **OMOP + LLM-assisted phenotyping is the standout cluster.** Two
  agentic / LLM-driven OMOP & rare-disease tools surfaced in the same
  week — *Agentic Authoring of OMOP Concept Sets from Natural Language*
  (Chute alert) and *MARRVEL-MCP*, an agentic interface for Mendelian
  disease discovery (Bastarache alert). A third, *Genosolver*, uses LLM
  reasoning over unstructured clinical narratives for rare-disease
  diagnosis (Chute alert). All three sit squarely at the intersection of
  your EHR phenotyping / rare-disease / KG threads and your `INTERESTS.md`
  flag for "LLM-assisted phecode and HPO assignment."
- **Pharmacoepi / TTE has a notable rare-disease example.** A real-world
  TTE of three Duchenne MD exon-skipping antisense oligonucleotides
  (eteplirsen, casimersen, golodirsen) for survival — Hernán alert.
  Combines your TTE methods thread with rare-disease real-world evidence.
- **Cross-ancestry PRS gets a foundation-model angle.** *Bridging
  Ancestry Gaps in Genomic Risk Prediction with Tabular Foundation Models*
  (Karczewski alert) directly targets cross/trans-ancestry portability of
  PRS — one of your stated genetic-epi priorities — using a tabular FM
  rather than the usual transfer-learning machinery.
- **PRS-in-pharmacoepi**: ICI thyroid-toxicity PRS across ancestries
  (Fritsche et al., *Clinical Cancer Research*) appeared in both Denny
  and Bastarache alerts — predictive PRS tied to a drug-safety decision,
  with multi-ancestry framing.
- **arXiv-digest repo continues to under-recall on-thread items.** Six of
  the eleven days in the window had zero relevant papers; the highest
  score across the whole window was 2 (the LBM/embedding-geometry paper),
  and even on-topic hits like the external-controls-for-treatment-switching
  TTE were score-1 keyword grazes. The Scholar feed is doing nearly all
  the work. See "Suggestions for the pipeline" at the bottom — most of
  the 2026-05-29 recommendations still apply and at least one (medRxiv
  ingestion) is becoming critical.
- **Low-signal channels:** "knowledge graph" keyword alert again pulled
  non-biomedical KGs (PESatNet recommendation, Memory-KGC, frequency-
  tendency forecasting); LLM-decoding papers (SAID, SimSD, BioMamba) keep
  showing up under Zitnik/Szolovits — all SKIP.

Counts: **11 HIGH**, **4 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. Agentic Authoring of OMOP Concept Sets from Natural Language
- **Authors / venue:** H. Chen, X. He, H. Dai, Y. Huang, M. Liu, J. Bian — *medRxiv*, 2026.
- **Surfaced by:** Christopher G. Chute "new related research".
- **Thread:** EHR phenotyping & OMOP; knowledge graphs & ontologies; LLM-assisted phenotyping.
- **What it is:** An agentic LLM workflow that produces OMOP-CDM concept
  sets directly from free-text descriptions. The alert framing is that
  "authoring OMOP concept sets from free-text descriptions remains a
  major" bottleneck — i.e., this is targeted at the manual cohort-
  definition / value-set authoring step in OMOP studies.
- **Why it matters to you:** Sits at the exact junction of your
  EHR-phenotyping thread (computable phenotypes), OMOP thread, and
  `INTERESTS.md` line "NLP / LLM extraction from clinical notes for
  phecode and HPO term assignment." The "agentic" part is worth
  scrutinizing — whether it's tool-augmented retrieval over the OMOP
  vocabulary (defensible) or unconstrained LLM generation (hallucination
  risk for codes). Pair-reads with the 2026-05-29 OMOP ETL automation
  paper (Mayrhuber et al.) — together they cover the two main OMOP
  authoring frictions (ETL + concept sets).
- **Action:** HIGH — read the agent architecture and check whether
  outputs are grounded against the OMOP vocabulary or post-hoc validated.

### 2. MARRVEL-MCP: An Agentic Interface for Mendelian Disease Discovery via Tool-Augmented Context Engineering
- **Authors / venue:** Z. Everton, J. Botas, S.Y. Kim, L. Yao, Z. Liu, H.H. Jeong — *The American Journal of Human Genetics*, 2026.
- **Surfaced by:** Lisa Bastarache "new related research".
- **Thread:** Rare disease + variant interpretation + knowledge graphs.
- **What it is:** An MCP (Model Context Protocol) tool-augmented agentic
  layer over MARRVEL (the established multi-resource variant/gene
  exploration tool for Mendelian disease) — i.e., wrapping curated
  variant/gene knowledge sources as tools an LLM agent can call during
  rare-disease case work-up.
- **Why it matters to you:** Directly serves the rare-disease and
  variant-interpretation threads, and is the kind of *explainable*,
  tool-grounded agentic system your `INTERESTS.md` prefers over opaque
  link-prediction. MCP-wrapped clinical/genomic KGs is also a credible
  pattern for your KG-for-clinical-reasoning interest. *AJHG* venue
  raises its credibility above the typical preprint-only agentic-tool
  paper.
- **Action:** HIGH — read for the tool catalog and how it grounds
  variant interpretation against ClinVar / OMIM / HPO.

### 3. Genosolver: Rare Disease Diagnosis through Holistic Integration of Unstructured Clinical Narratives Using Large Language and Reasoning Models
- **Authors / venue:** T. Islam, M. Danner, Z. Ziad, M. Begemann, D. Beijer, et al. — 2026 (preprint per Scholar snippet).
- **Surfaced by:** "7 new citations to articles by Christopher G. Chute".
- **Thread:** Rare disease + EHR phenotyping (clinical NLP) + ML for precision health.
- **What it is:** Uses LLM + reasoning-model pipelines to extract and
  integrate phenotype evidence from *unstructured* clinical narratives
  (the hard input modality) for rare-disease diagnostic suggestions.
- **Why it matters to you:** Hits the "ultra-rare clinical NLP" line in
  your rare-disease thread and the LLM-assisted-phenotyping line in your
  EHR-phenotyping thread. Worth comparing to MARRVEL-MCP (#2) — one is
  structured-KG-grounded, the other is narrative-grounded; together
  they sketch the two-pronged approach (KG + NLP) needed for production
  rare-disease pipelines.
- **Action:** HIGH — read for how grounding/citation is handled (open
  hallucination risk with LLM reasoning over narratives).

### 4. G.AI: An AI-driven Platform for Phenotype Standardization, Variant Interpretation and Structured Clinical Reporting in Rare Disease Genomic Diagnosis
- **Authors / venue:** Z. Wang, X. Chen, L. Tang, X. Wu, A. Huang, H. … — 2026 (per "rare diseases" keyword alert).
- **Surfaced by:** "rare diseases - new results".
- **Thread:** Variant interpretation (ACMG / ClinGen) + rare disease + EHR phenotyping.
- **What it is:** End-to-end platform claim spanning phenotype
  standardization (likely HPO-anchored), variant interpretation, and
  structured reporting for rare-disease genomic diagnostics.
- **Why it matters to you:** End-to-end positioning means it touches
  *three* of your threads at once. Whether it's a real platform or a
  preprint demo will determine action priority. The interesting question
  is what variant-interpretation logic it implements — naive LLM
  classification would be a red flag against your variant-interpretation
  priorities (ACMG/ClinGen rigor), whereas an InterVar-style rules
  engine with LLM-assisted evidence collection would be on-thread.
- **Action:** HIGH — skim to confirm ACMG-AMP rule fidelity; downgrade
  to SKIP if it's another LLM-only classifier.

### 5. A Real-World Target Trial Emulation of Eteplirsen, Casimersen, and Golodirsen to Evaluate Survival Among Patients with Duchenne Muscular Dystrophy
- **Authors / venue:** S. Dharmarajan, S. Grabich, R. Baxter, A. Nadkar, et al. — 2026 (per alert).
- **Surfaced by:** "10 new citations to articles by Miguel Hernán".
- **Thread:** Causal inference / pharmacoepi (TTE) + rare disease.
- **What it is:** A target-trial emulation comparing survival under three
  exon-skipping antisense oligonucleotide therapies in DMD using
  real-world data.
- **Why it matters to you:** A clean *rare-disease TTE* example. Your
  active drug-class TTE threads (GLP-1, SGLT2, CFTR modulators, HRT) are
  all common-disease; DMD is structurally similar to your CFTR modulator
  thread (small population, registry/EHR follow-up, expensive targeted
  therapy, hard to RCT head-to-head). The eligibility/grace-period/
  cloning design choices are likely transferable to a Trikafta-vs-
  ivacaftor TTE. The cite into Hernán's corpus signals the methods
  framing.
- **Action:** HIGH — read for the rare-disease cohort construction and
  censoring rules; potential design template for CFTR-modulator work.

### 6. Bridging Ancestry Gaps in Genomic Risk Prediction with Tabular Foundation Models
- **Authors / venue:** A. Das, Y. Cui — *bioRxiv*, 2026.
- **Surfaced by:** Konrad Karczewski "new related research".
- **Thread:** Genetic epidemiology (PRS, trans-ancestry portability) + EHR foundation models.
- **What it is:** Tabular foundation model applied to the cross-ancestry
  PRS-portability problem. Snippet motivates with the standard
  observation that "models deployed for genomic prediction of diseases
  perform unevenly" across ancestries.
- **Why it matters to you:** Trans-ancestry PRS portability is an
  explicit `INTERESTS.md` priority. The tabular-FM angle (vs. classic
  transfer learning / multi-ancestry shrinkage like PRS-CSx) is
  novel — worth checking whether the FM is genotype-tabular (likely) or
  EHR-tabular, and whether ancestry covariates leak into representations
  (a fairness pitfall flagged in your FM-fairness sub-line).
- **Action:** HIGH — read the architecture and the cross-ancestry
  evaluation; compare reported gains to PRS-CSx / Bridge-PRS baselines.

### 7. Polygenic Risk Scores for Prediction of Immune Checkpoint Inhibitor Thyroid Toxicity in Diverse Populations
- **Authors / venue:** L.G. Fritsche, L.M. Higgins, M. Schipper, G. Strohbehn, et al. — *Clinical Cancer Research*, 2026.
- **Surfaced by:** Lisa Bastarache + Joshua C. Denny "new related research" (concurrent).
- **Thread:** Genetic epidemiology (PRS) + pharmacoepidemiology + ML for precision health + ancestry-stratified risk.
- **What it is:** PRS for ICI-induced thyroid immune-related adverse
  event (irAE), evaluated in ancestrally diverse populations.
- **Why it matters to you:** Cross-thread: PRS construction + ancestry
  portability + drug-safety pharmacoepi + a *clinical-decision* angle
  (who to escalate monitoring on under ICI therapy). Fritsche is a
  long-running PRS-in-EHR-biobank methodologist (PRSWeb at Michigan).
  This is exactly the "ML papers are HIGH when tied to a clinical
  decision" pattern in your `INTERESTS.md`.
- **Action:** HIGH — read for the cross-ancestry calibration step and
  decision-curve analysis (if present); cite-worthy template for
  drug-AE PRS work in CHIP/CF/APOL1 cohorts.

### 8. Predicting Acute Care Utilization by People with Diabetes Using EHR Data (ADA 2026 abstract 2045-P)
- **Authors / venue:** H. Sharma, G. Yu, J. Lee, Z. Obradovic, R. McCoy, et al. — *Diabetes*, 2026 (ADA Scientific Sessions late-breaking poster).
- **Surfaced by:** George Hripcsak "new related research".
- **Thread:** EHR phenotyping + ML for precision health + chronic-disease multimorbidity.
- **What it is:** EHR-based predictive model for acute-care utilization
  (likely ED visits / hospitalization) among people with diabetes.
- **Why it matters to you:** A practical risk-prediction-tied-to-
  clinical-decision paper in your multimorbidity / precision-health
  zone. McCoy is a Mayo endocrinology + outcomes group with strong AoU
  / OptumLabs use. Caveat: ADA poster, so abstract-level only — the
  read is mostly the design choices (label definition for "acute care
  utilization," feature set, cohort).
- **Action:** Medium-HIGH — skim the abstract; chase the full paper if
  the feature engineering uses interesting time-windowed phecodes /
  meds.

### 9. Autosomal Type IV Collagen Genes Display Sex Differences in Genetic Risk for Hematuria
- **Authors / venue:** F. Lona-Durazo, I.R. Dinsmore, M.T. McNulty, et al. — *Kidney International Reports*, 2026.
- **Surfaced by:** "5 new citations to articles by George Hripcsak".
- **Thread:** Genetic epidemiology + EHR-linked biobank phenotyping; APOL1-adjacent kidney disease.
- **What it is:** Sex-stratified genetic association of autosomal type IV
  collagen genes (COL4A3/4/5 — Alport syndrome / thin basement membrane
  spectrum) with EHR-defined hematuria.
- **Why it matters to you:** Hits your APOL1 / kidney-genetics thread
  laterally (different gene family, same nephrogenomics population). The
  *sex-stratified* GWAS framing is methodologically interesting for
  monogenic / nearly-monogenic conditions where sex modifies penetrance —
  transferable shape to your monogenic-penetrance-under-population-
  screening priority.
- **Action:** HIGH — read for sex × variant interaction modeling.

### 10. Dissecting the Polygenic Architecture of Psychopathology via Singular Value Decomposition of Eight Psychiatric GWAS
- **Authors / venue:** F. Facal, A.M. Pérez-Gutiérrez, J. … — 2026 (per alert).
- **Surfaced by:** Joshua C. Denny "new related research".
- **Thread:** Genetic epidemiology (cross-trait shared genetic architecture) + multimorbidity (psychiatric).
- **What it is:** SVD over the summary statistics of eight psychiatric
  GWAS to extract shared latent components of polygenic risk.
- **Why it matters to you:** Methodologically interesting for your
  multimorbidity / disease-clustering thread — applying matrix
  decomposition to GWAS summary stats is a structural-genetic analog of
  the latent-class / topic-model approaches you flag for diagnosis
  trajectories. Caveat: psychiatric isn't on your disease list, so this
  is METHODS-priority HIGH rather than disease-priority HIGH.
- **Action:** HIGH (methods) — read the SVD-on-summary-stats setup;
  cribbable for a cardiometabolic-multimorbidity polygenic decomposition.

### 11. Bridging Methods Note — When Can Whole-Genome SNP Heritability Be Reliably Estimated From Summary Statistics?
- **Authors / venue:** B.K. Pham, S. Davenport, D. Azriel, A. Schwartzman — *bioRxiv*, 2026.
- **Surfaced by:** Jian Yang "new related research" (also surfaces under Karczewski).
- **Thread:** Genetic epidemiology methods (LDSC, h² estimation).
- **What it is:** A theoretical/empirical analysis of when LD Score
  Regression-style summary-statistic heritability estimation is
  *reliable* — i.e., the validity envelope of the workhorse method.
- **Why it matters to you:** Useful guardrails reference for any work
  that consumes LDSC heritabilities, cross-trait genetic correlations,
  or partitioned heritability. Pairs with the 2026-05-29 "Causal ML is
  not a panacea" paper as a methods-skepticism citation pack.
- **Action:** HIGH (methods) — keep as a reference; check the
  failure-mode taxonomy.

---

## METHODS-WATCH (off-thread disease/topic, exemplary methods)

These four are the closest things the `arxiv-digest` repo + Scholar
turned up that aren't on a disease thread but have transferable methods.

- **Leveraging External Controls for Treatment Switching in Randomized Controlled Trials: A Weighted Causal Inference Framework for Overall Survival** — A.A. Shen, C. Fu, R. Lin (stat.ME, arXiv:2606.06441; arxiv-digest 06-06). Synthetic-control + balancing-weights with multiple imputation and time-varying weights to handle treatment switching in oncology RCTs. *Watch for:* the time-varying weight construction; cribbable for active-comparator TTE designs where crossover/switching is common.
- **Federated SPARQL Querying for Genomic Variant Functional Annotation** — A. Bodrug-Schepers, R. Bourcier, R. Redon, A. Gaignard (q-bio.QM, arXiv:2606.05918; arxiv-digest 06-06). Federated SPARQL over biomedical KGs (UniProtKB, etc.) for variant annotation without bulk-replicating reference data. *Watch for:* the privacy/FAIR architecture — useful pattern if you do multi-site annotation on data that can't leave a site.
- **Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery** — S. Biswas, S. Gupta, P. Mukherjee (cs.AI, arXiv:2606.09672; arxiv-digest 06-09, score 2). Shows that biomedical text encoders (BioBERT, PubMedBERT, BioM-ELECTRA) assign ~0.83 cosine similarity to mechanism-unrelated cross-domain phrases, then uses KG-mined hard negatives ("BODHI") to debias them. *Watch for:* the hard-negative-mining protocol — relevant if you build any retrieval/RAG over biomedical embeddings (the failure mode they describe is real and under-reported). Caveat: the framing as a "Large Behavioural Model" is product-y, but the diagnostic finding stands on its own.
- **Predicting Hospitalization from a Whole-Person Health Score with Incomplete EHR Data** — G.E. Weavil, J. Rigdon, S.C. Lotspeich (stat.AP, arXiv:2606.10093; arxiv-digest 06-10). Allostatic Load Index (10 components across 3 body systems) for hospitalization prediction, comparing imputation strategies and pattern-submodel approaches on n=1,000. *Watch for:* the pattern-submodel approach to systematic EHR missingness (AUC 0.73 in-sample, 0.63 out-of-sample) — relevant if you've been thinking about missingness in your phecode/lab feature pipelines, though the sample is small and the AUC drop on CV is a warning sign about generalizability.

---

## SKIP / noise (logged, no action)

- **arxiv-digest 06-09:** *Integrating Gene Regulatory Priors into Transformer Attention with scTransformer* (Milia et al.) — scRNA-seq cell-type classification, not clinical EHR. SKIP per "non-EHR foundation-model" guideline.
- **arxiv-digest 06-09:** *A Multi-Agent System for Spine MRI Report Generation* (Xiao et al.) — imaging-FM agent system; off-thread.
- **arxiv-digest 06-10:** *Flexible Flows for Biological Sequence Design* (Verma et al.) — DNA/peptide generative model; off-thread (incidental "latent class" keyword hit).
- **"knowledge graph" keyword alert:** PESatNet (recommendation KGs), Memory-KGC (graph embedding), *Explainable Temporal KG Forecasting via Frequency-Tendency Modeling* — all non-biomedical KG infrastructure. SKIP per `INTERESTS.md`.
- **"drug repurposing" keyword alert:** *Network pharmacology identifies repurposable drugs targeting host pathways across the oral-gut-lung axis* — network-pharmacology / target-only repurposing with no clinical-evidence loop. SKIP per `INTERESTS.md` ("lower interest in target-only or chemistry-only pipelines without a clinical-evidence loop").
- **"mendelian diseases" keyword alert:** *Association of antihypertensive drugs, intestinal ischemia, and breast diseases: A drug-target MR study* — keyword is "mendelian randomization" the method, not Mendelian disease; off-thread.
- **Zitnik / Szolovits LLM-decoding drift:** *SAID: Scaffold-Aware Iterative Decoding*, *SimSD: Simple Speculative Decoding in Diffusion LMs*, *BioMamba* — generic LLM decoding/architecture papers surfacing under biomedical-author alerts. SKIP.
- **Natarajan alerts:** *Text-guided few-shot liver and tumor segmentation*; *Towards World Models in Biomedical Research* — off-thread (imaging / position).
- **David Baker, Michael Snyder, Francis Collins author alerts:** all off-thread this week (protein design; meal-response in diabetes; pancreatic-islet multiomics).
- **Citation churn:** various "N new citations to articles by X" alerts where the cite is on an off-thread paper (e.g., Pritchard cited in a prostate-cancer CRISPR review). SKIP.

---

## arxiv-digest pipeline health check

Eleven-day window (2026-05-30 → 06-10):

| Status | Days |
| --- | --- |
| `Relevant papers: 0` (clean empty) | 05-30, 05-31\*, 06-02, 06-03\*, 06-07, 06-08 |
| Hits | 06-06 (2), 06-09 (3), 06-10 (2) |

\* indicates 3/4 arXiv categories failed to fetch (rate-limit or
upstream issue) — flagging because two of the empty days were actually
*fetch-failed*, not "no relevant papers." The 05-31 and 06-03 runs may
be hiding on-thread papers; consider a backfill (`--lookback-hours
720`) once arXiv is responsive.

The highest-scoring paper in the window was score 2 ("Correlation Is
Not Enough", `foundation model` + `knowledge graph`). No paper crossed
the deep-summary threshold (`--deep-score 4`) all week.

## Suggestions for the pipeline (carry-over + new)

Most of these were also in the 2026-05-29 report; reasserting because
they would have caught items the current pipeline missed *this* week:

1. **Add medRxiv / bioRxiv ingestion.** Five of this week's HIGH items
   (#1 Chen et al. agentic OMOP, #3 Genosolver, #4 G.AI, #6 Das & Cui
   tabular FM, #11 Pham et al. LDSC) were preprints on medRxiv or
   bioRxiv — completely outside the four tracked arXiv categories.
   Without a preprint-server source, the digest will keep missing this
   class of paper indefinitely.
2. **Add `cs.LG`, `stat.ME`, `q-bio.MN`.** The external-controls /
   treatment-switching paper (#METHODS-WATCH-1) sits in stat.ME; the LBM
   paper in cs.AI. Your existing `q-bio.QM/GN/PE + stat.AP` net misses
   most causal-ML methods venues.
3. **Tighten `knowledge graph` keyword.** Still pulling
   recommendation-KGs and forecasting-KGs. Suggest requiring co-
   occurrence with a biomedical anchor (`biomedical`, `clinical`,
   `HPO`, `SNOMED`, `OMOP`, `phenotype`).
4. **Add keywords for shapes you keep manually triaging in:**
   `target trial emulation`, `proteome-wide MR` / `pwmr`,
   `colocalization`, `tabular foundation model`, `agentic` /
   `tool-augmented` (when paired with `clinical` or `OMOP` or `HPO`).
5. **Surface fetch failures more loudly.** The 05-31 and 06-03 runs
   showed "Relevant papers: 0" but had `WARNING: 3/4 categories failed
   to fetch` — these should arguably show up as a non-zero exit / a
   distinct status line at the top of the digest so they don't read as
   "quiet week."
