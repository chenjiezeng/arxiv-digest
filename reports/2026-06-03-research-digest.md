# Research digest report — 2026-06-03

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-06-01 09:00 UTC → 2026-06-03 03:00 UTC** (since the prior
2026-06-01 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 06-01 09:00 → 06-03 03:00 UTC | Two batches: 06-02 06:56 UTC (author + citation alerts, ~25 threads) and 06-03 00:23 UTC (keyword alerts, 12 threads). |
| `arxiv-digest` repo (`digests/`) | 06-01 → 06-03 | **Empty / silent.** 06-02 = 0 relevant; 06-01 and 06-03 not generated; 05-31 still logged 3/4 q-bio fetch failures (carried over). Pipeline remains silent. |
| PubMed/NCBI alerts (AoU, UKB, drug repurposing) | 06-01 14:28, 06-02 12:42 UTC | Reviewed as confirmation source for keyword overlap. |
| bioRxiv / medRxiv subject alerts | daily | Aggregate digests, not individually triaged. |
| Raw arXiv daily mailings (`no-reply@arxiv.org`) | daily | Unfiltered cs/q-bio/stat to a list address; not triaged. |

> ⚠️ **`arxiv-digest` pipeline is still silent.** Same recommendation as the
> last two reports: investigate q-bio fetch failures + consider adding
> cs.LG, stat.ME, and a medRxiv / bioRxiv source. The pipeline has now
> emitted zero relevant papers for 8 consecutive days (05-26 was the last
> non-trivial digest).

> Caveat: Scholar alert emails contain title, authors, venue, and the first
> ~2-3 lines of each abstract only. The reports below contextualize that
> metadata against your research threads; nothing here reflects full-text
> reading.

---

## Executive summary

- **Causal inference / pharmacoepi is the dominant cluster this window.**
  Five distinct target-trial / new-user-design papers landed across
  Patrick Ryan and Miguel Hernán author alerts — a GLP-1 vs DPP-4 head-to-
  head in hemodialysis (KIR), a statins-in-breast-cancer-survivors primary
  prevention trial emulation (JNCI), an SGLT2i pharmacogenetics
  rationale/design (CTS), a GLP-1 RA → hematologic-cancer-risk ASCO
  abstract, and a CHIP → ICI-efficacy real-world analysis. Three of these
  squarely hit your GLP-1/SGLT2i drug-class threads.
- **PheWAS + AoU**: a methodologically interesting **pre-cancer-diagnosis
  PheWAS in AoU** (Rich et al., medRxiv) — large, full-paper preprint that
  inverts the usual outcome direction (PheWAS *of* a future cancer
  diagnosis using pre-diagnosis EHR). Closest hit to the PheWAS thread
  this window.
- **CHIP**: a *Cancer* real-world data paper on CHIP and ICI efficacy /
  adverse events (Fujita et al.) — links somatic mosaicism to drug-class
  outcomes, useful for your CHIP-pharmacoepi crossover.
- **Multimorbidity / ML for precision health**: Forrest et al. (Ron Do
  lab) in *Med* — a *spectrum-of-disease* ML model from routine labs +
  vitals. Direct hit on the multimorbidity / chronic-disease-clustering
  thread.
- **EHR foundation models**: a second strong week — Chandak et al.
  "EveryQuery" zero-shot clinical prediction via task-conditioned
  pretraining (Kohane group, ICML 2026 Structured-Data-for-AI workshop) —
  complements last week's patient-aware-sampling paper. Plus a KG-FM
  in-context-learning paper (KGPFN) from the Callahan-related feed.
- **PheWAS / variant-interpretation methodology** also returns one
  X-linked-hearing-loss gene-specific evidence paper (EBioMedicine) —
  template for VCEP-style gene-specific specifications.

Counts: **9 HIGH**, **5 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. Capturing multi-disease states on a spectrum with machine learning and routine clinical data
- **Authors / venue:** I.S. Forrest, B.O. Petrazzini, R. Chen, A.D. Blazer et al. (Ron Do lab) — *Med*, 2026.
- **Surfaced by:** **Ron Do "new articles"** alert (06-02 06:56 UTC).
- **Thread:** Chronic disease clustering & multimorbidity **+** ML for
  precision health **+** EHR phenotyping (lab/vital-based).
- **What it is:** Argues that diseases exist on continuous *spectra* of
  risk factors, cellular perturbations, and clinical manifestations, and
  shows that ML on routine laboratory tests + vitals can capture
  multi-disease states along those spectra. Direct quote from the snippet:
  "Diseases exist on spectra of risk factors, cellular perturbations,
  organ dysfunction, and clinical manifestations. It is unknown whether
  the analysis of routine laboratory tests and vitals using artificial
  intelligence presents a scalable and …"
- **Why it matters to you:** Hits the multimorbidity thread head-on with
  a method that does *not* require curated diagnosis codes — just routine
  labs/vitals. Useful as a counterpoint to your phecode-based
  multimorbidity work because it uses orthogonal inputs (lab continua vs.
  diagnosis codes). The Do lab is a strong methodological signal — they
  have prior work on biobank-scale ML for cardiometabolic spectra.
  Particularly worth comparing against the Rahemi & Omidi "deterministic
  overlapping multimorbidity phenotypes" paper from last week's report
  (which uses diagnosis-based phenotypes for the same multimorbidity
  framing).
- **Action:** **HIGH** — read for the labs/vitals featurization, the
  spectrum-vs-cluster choice, and how disease boundaries are operationalized.
  Pair with last week's Rahemi/Omidi paper for a labs-vs-codes contrast.

### 2. Target Trial of GLP-1s versus DPP-4s and Mortality in Hemodialysis
- **Authors / venue:** D. Le, M. Kilpatrick, W.K. Kraft, M.E. Grams, B.G.
  Jaar et al. — *Kidney International Reports*, 2026.
- **Surfaced by:** **Patrick Ryan "new related research"** alert (06-02 06:56 UTC).
- **Thread:** Causal inference / pharmacoepi (target trial emulation) **+**
  GLP-1 drug-class thread.
- **What it is:** Target-trial-emulation comparing GLP-1 RAs vs DPP-4
  inhibitors on mortality in hemodialysis patients, using 2011–2021 US
  Renal Data System (USRDS) + Medicare claims data. The KDIGO-aligned
  hemodialysis subpopulation is a meaningful clinical niche because
  comparative-effectiveness evidence for GLP-1 RAs is sparse in advanced
  CKD/dialysis (most landmark trials excluded these patients).
- **Why it matters to you:** Three things make this a tight fit:
  (i) it's a *formal* target trial emulation rather than the more common
  Cox-with-PS, so it's a clean reference for design choices
  (eligibility, treatment strategies, assignment, censoring); (ii) it's
  GLP-1, which is your active drug-class thread; (iii) the USRDS+Medicare
  data structure is parallel to AoU-EHR-linked-claims work — patterns
  transfer to AoU pharmacoepi designs. Grams is a kidney-disease causal-
  inference heavyweight (related: kidney function trajectories, APOL1).
- **Action:** **HIGH** — read for the protocol section (target trial
  specification table), treatment-strategy definition (was there a
  grace period? new-user design?), and how survivor / immortal-time bias
  was handled with claims-based exposure.

### 3. Statins and risk of cardiovascular disease: Emulating a primary prevention trial in breast cancer survivors
- **Authors / venue:** R.G. Russo, **M.A. Hernán**, I.J. Dahabreh, E.B.
  Rimm et al. — *JNCI: Journal of the National Cancer Institute*, 2026.
- **Surfaced by:** **Miguel Hernán "new articles"** alert (06-02 06:56 UTC).
- **Thread:** Causal inference / pharmacoepi (target trial emulation) **+**
  cardiovascular prevention.
- **What it is:** Emulates a primary-prevention RCT for statins in breast
  cancer survivors, anchored in Hernán's standard target-trial-emulation
  framework. The "primary prevention" framing in a *prior-cancer* cohort
  is methodologically interesting — survivors carry treatment-related CV
  risk that distorts conventional new-user designs.
- **Why it matters to you:** Hernán + Dahabreh is the canonical target-
  trial-emulation citation pair. Reading their methods/protocol section
  is high-yield even when the clinical question is off-thread. The breast-
  cancer-survivor cohort is a useful template for *survivors-as-an-eligible-
  population* designs that you might consider for prostate-cancer hormone-
  therapy work (your own line of work — see prior report #3, the AoU PCa
  hormone-therapy paper). Specifically: how do they handle competing
  risks (cancer recurrence), treatment-confounded baseline period, and
  censoring on cancer-death?
- **Action:** **HIGH** — read the protocol / eligibility section; the
  estimand definition will be reusable for AoU prostate-cancer pharmacoepi
  designs.

### 4. A real‐world data analysis of the impact of clonal hematopoiesis of indeterminate potential on therapeutic efficacy and adverse events of immune checkpoint inhibitors
- **Authors / venue:** T. Fujita, N. Ishibashi, S. Aoyama, Y. Kobayashi et
  al. — *Cancer*, 2026.
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert (06-03 00:23 UTC).
- **Thread:** Clonal hematopoiesis (CHIP) disease thread **+** pharmacoepi.
- **What it is:** Real-world-data analysis of CHIP carriers receiving
  immune checkpoint inhibitors (ICIs), examining both efficacy (likely
  PFS/OS) and adverse events (likely immune-related AEs / irAEs). The
  hypothesis is mechanistically grounded: CHIP variants (especially
  DNMT3A/TET2/ASXL1) drive baseline systemic inflammation, which could
  plausibly modulate ICI response and irAE risk in either direction.
- **Why it matters to you:** Extends the CHIP→outcome literature into a
  *drug-class-conditional* outcome — joins the CHIP-and-CV-outcomes papers
  from prior reports as a complementary CHIP-and-cancer-immunotherapy
  finding. The methodological shape (RWD + CHIP exposure + drug-class
  outcome) is directly portable to your AoU work where ICI exposure and
  CHIP variants are both ascertainable. Note this is *Cancer* (Wiley), not
  *Blood* or *Nature*, so audit the cohort size and CHIP-ascertainment
  method carefully (targeted panel? WES? VAF threshold?).
- **Action:** **HIGH** — read for CHIP detection methodology (panel,
  VAF cutoff), effect size on ICI efficacy by CHIP gene class, and the
  irAE direction.

### 5. Phenome-Wide Association Study of Pre-Cancer Diagnosis Electronic Health Records Identifies Risk and Inverse Associations in the All of Us Research Program
- **Authors / venue:** C.C.D. Rich, E.J. Bang, A.B. Bair, B.E. Richardson
  et al. — *medRxiv*, 2026 (preprint, posted 2026-05-26).
- **Surfaced by:** **Lisa Bastarache "new related research"** alert (06-02 06:56 UTC).
- **Thread:** **PheWAS / phecode infrastructure** **+** EHR-linked
  biobanks (AoU) **+** EHR phenotyping.
- **What it is:** A PheWAS run over **pre-cancer-diagnosis** EHR data in
  the All of Us cohort (400,000+ participants with WGS + linked EHR),
  identifying phecode/diagnostic associations that predict (or
  inversely-associate with) future cancer diagnosis. Direct quote: "The
  All of Us Research Program represents a rich resource for cancer
  epidemiology research, with over 400,000 participants with whole genome
  sequences linked to electronic health records (EHR). Large cancer
  datasets often …"
- **Why it matters to you:** **Closest single-paper hit to your PheWAS
  thread this window.** The pre-diagnosis framing is a clever inversion
  — instead of using PheWAS to map variant → phenotypes, this uses PheWAS
  to map *future cancer outcome* → pre-diagnostic phenotype patterns,
  which is methodologically analogous to PheRS construction. Direct
  parallels to your own AoU work (and your coauthored Yang/Schaffer/Tran/
  Zeng/Park prostate-cancer paper from the prior report — that paper used
  metabolic/inflammatory markers in PCa patients; this paper goes further
  upstream to the pre-diagnosis window). Bastarache lab adjacency is also
  relevant (she's the phecode-infrastructure anchor).
- **Action:** **HIGH** — read for the pre-diagnosis observation-window
  definition (how far before dx? how is the index date set?), the multiple-
  testing strategy across hundreds of phecodes × tens of cancers, and
  whether the "inverse associations" are interpreted as protective
  (treatment effects) or detection-bias artifacts. **Top-priority read of
  the window.**

### 6. EveryQuery: Zero-Shot Clinical Prediction via Task-Conditioned Pretraining
- **Authors / venue:** P. Chandak, G. Kondas, **I.S. Kohane**, M.B.A.
  McDermott — ICML 2026 Workshop on Structured Data for AI, 2026.
- **Surfaced by:** **Isaac Kohane "new articles"** alert (06-02 06:56 UTC).
- **Thread:** EHR foundation models (CLMBR/MOTOR/FEMR/MEDS lineage) **+**
  zero-shot clinical prediction.
- **What it is:** A *task-conditioned* pretraining approach to EHR
  foundation models that enables zero-shot prediction across arbitrary
  downstream clinical-prediction tasks ("EveryQuery"). Conditioning on a
  task descriptor at pretraining time is the key design idea — analogous
  to instruction-tuning for LLMs but for EHR sequences. McDermott is the
  same author as the MEDS standard (which surfaced in the Hripcsak/Shah
  alerts last week), so this slots into the MEDS ecosystem.
- **Why it matters to you:** A second strong EHR-FM paper in two weeks,
  both at the *same* ICML 2026 Structured-Data-for-AI workshop. The
  workshop is becoming the de facto venue for FEMR/MEDS/CLMBR follow-on
  work — worth tracking the full program. EveryQuery's task-conditioning
  is methodologically different from the Placidi et al. *patient-aware
  sampling* paper from the prior report — together they sketch two
  orthogonal axes of EHR-FM design choice (input-side patient structure
  vs. output-side task conditioning).
- **Action:** **HIGH** — read alongside the Placidi paper from last week
  for a side-by-side on EHR-FM design axes. Also worth checking whether
  the full ICML 2026 workshop proceedings have other on-thread papers.

### 7. KGPFN: Unlocking the Potential of Knowledge Graph Foundation Model via In-Context Learning
- **Authors / venue:** Y. Gao, J. Bai, H. Huang, Z. Xie, Y. Li, H.T. Tsang,
  S. Han et al. — arXiv preprint, 2026.
- **Surfaced by:** **Tiffany J. Callahan "new related research"** alert (06-02 06:56 UTC).
- **Thread:** Knowledge graphs & ontologies **+** drug repurposing (KG-ML
  angle).
- **What it is:** A *knowledge-graph foundation model* that uses
  in-context learning (ICL) to generalize across heterogeneous KGs without
  task-specific fine-tuning. Snippet: "Knowledge graph (KG) [foundation
  models …]" — likely framed as the KG analog of LLM ICL.
- **Why it matters to you:** KG-FMs with ICL are interesting for your
  drug-repurposing thread because they remove the per-KG fine-tuning step
  — meaning a single FM could plausibly transfer across DrugBank / Hetionet
  / SPOKE / a custom HPO-anchored rare-disease KG without retraining. The
  Callahan signal is also relevant — she's a biomedical-KG anchor (PheKnowLator,
  ROBOT, OMOP-mapped ontologies). Whether the paper actually evaluates on
  biomedical KGs is the question; if yes, this is a clean fit; if it's
  primarily Freebase/Wikidata, it's still methods-watch.
- **Action:** **HIGH (pending biomedical-eval check)** — skim the
  evaluation section first; if biomedical KGs are included, read in full
  for the ICL prompt format and transfer behavior. If not, downgrade to
  methods-watch.

### 8. Glucagon-like peptide-1 receptor agonist (GLP-1 RA) and hematologic cancer risk among older adults with type 2 diabetes
- **Authors / venue:** W.H. Chen, R.M. Radwan, H. Salman, T.J. George, L.
  Han et al. — ASCO 2026 (JCO Suppl. abstract 6592).
- **Surfaced by:** **Patrick Ryan "new related research"** alert (06-02 06:56 UTC).
- **Thread:** Pharmacoepi (GLP-1 drug-class) **+** cancer risk (hematologic).
- **What it is:** ASCO 2026 abstract on GLP-1 RA exposure and hematologic
  (blood/lymphatic) cancer risk in older T2D adults. The biological
  premise — that GLP-1 RAs modulate inflammation and could therefore
  modify cancer risk — is mechanistically interesting but the conference-
  abstract level evidence is preliminary. Likely Medicare-claims-based
  given the "older adults" framing.
- **Why it matters to you:** Adds to a now-substantial GLP-1-cancer-risk
  signal cluster (last week had the AoU GLP-1/liver paper; this is the
  *adverse-outcome* angle in a different organ system). Hematologic
  cancers are particularly worth tracking given the CHIP overlap — if GLP-
  1 RAs modulate clonal hematopoiesis expansion, hematologic-cancer risk
  is the downstream readout. Abstract-only for now — wait for the full
  paper.
- **Action:** **HIGH (low intensity)** — log in the GLP-1-cancer-risk
  cluster; revisit when the full paper drops. Watch for whether CHIP is
  considered as a mediator.

### 9. Genetics of Response to Canagliflozin (GRC) Study: Rationale, Design, and Pharmacodynamic Responses
- **Authors / venue:** M.E. Montasser, S.A. Bargal, E.A. Streeten, H.B.
  Whitlatch et al. — *Clinical and Translational Science*, 2026.
- **Surfaced by:** **Patrick Ryan "new related research"** alert (06-02 06:56 UTC).
- **Thread:** Pharmacoepi (SGLT2 inhibitor drug-class thread) **+**
  pharmacogenomics **+** genetic epidemiology (response-to-drug).
- **What it is:** A rationale/design paper for a study of *genetic*
  predictors of response to canagliflozin (an SGLT2 inhibitor). Snippet:
  "Sodium glucose cotransporter-2 (SGLT2) inhibitors are a class of
  antidiabetics with benefits including HbA1c-lowering, weight loss,
  cardiovascular and renal protection in addition to adverse effects
  including genitourinary tract …"
- **Why it matters to you:** Your active SGLT2i thread is mostly
  pharmacoepi (real-world outcomes), but pharmacogenomics is an adjacent
  axis — variants modulating response are a candidate explanation for
  the response heterogeneity that drives treatment-effect-heterogeneity
  work. Specifically: if there are common variants modulating SGLT2i
  response, that's a target for causal-forest / meta-learner HTE estimation
  in your composite-risk modeling. Design paper only at this stage —
  pharmacodynamic readouts (glucose-lowering, weight, GU-AE) but probably
  no GWAS results yet.
- **Action:** **HIGH (low intensity)** — log the cohort design; revisit
  when the actual GWAS / variant-stratified response paper drops.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Sensor wide association studies in digital medicine** — N. Steckhan,
  F. Broghammer, D. Powell — *npj Digital Medicine*, 2026. Surfaced by
  the "All of Us research program" keyword alert (06-03 00:23). Snippet
  explicitly mentions UKB accelerometry and AoU plans to integrate
  wearable data for >1M participants. *Watch for:* the SWAS analog of
  PheWAS — wearable-derived continuous phenotypes scanned across
  outcomes. If wearables become first-class in AoU, this is the
  methodological template. Borderline HIGH if you ever extend phecodes
  into sensor-derived phenotypes; currently methods-watch.
- **Optimising POU3F4 variant interpretation through gene-specific
  evidence in X-linked hearing loss** — J. Geng, Y. Zhao, Y. Huang, W.
  Xiong, M. Zhong, C. Wang et al. — *EBioMedicine*, 2026. (Variant
  interpretation keyword.) Single-gene VCEP-style specification for a
  rare hearing-loss gene. *Watch for:* the gene-specific evidence-code
  weighting framework — directly portable to other genes (CFTR, APOL1,
  CDH1) in your ClinGen-adjacent variant-interpretation thread. Template
  even though POU3F4 is off-disease-thread.
- **Genomics-Informed Approach Identifies Which Cell Types Regulate the
  Metabolome** — H. Krupkin, E.M. Padhi, D. Nachun, J. Kain, J.Z. Long et
  al. — *Bioinformatics*, 2026. (Stephen Montgomery alert.) Maps GWAS /
  eQTL signal onto cell-type-specific metabolite regulation. *Watch for:*
  the cell-type prioritization method — complements proteome-MR /
  colocalization methods that have been a recurring shape; gives you a
  metabolite-side analog for target-prioritization triangulation.
- **High-resolution analysis of recent population structure using rare
  variants** — L. Huang, T.C. Lamnidis, S. Schiffels — *G3: Genes,
  Genomes, Genetics*, 2026. (Pritchard 10 cites.) Rare-variant-based
  recent-ancestry inference. *Watch for:* the rare-variant ancestry
  granularity, which matters for your cross-ancestry portability work —
  recent admixture is often invisible to common-variant PCs but shows up
  in rare-variant sharing.
- **Effects of ambient air pollution exposure on lung function in cystic
  fibrosis: old stories or breaking news?** — A.M. Schaffer, C. Rass, S.
  Schlagenhaufen, F. Singer — *Thorax*, 2026. (Patrick Ryan alert.)
  Commentary / mini-review on PM/NO₂ exposure and lung function in CF.
  *Watch for:* exposure-window operationalization for environmental
  confounders — useful background when integrating environmental data
  with CF-modulator pharmacoepi.

---

## NOTABLE: Patrick Ryan "new related research" cluster

The 06-02 Patrick Ryan alert was unusually rich — 5 papers in a single
alert, spanning **target-trial emulation (GLP-1 vs DPP-4 in HD)**, **AoU
IBD data quality** (Spotnitz — already triaged in the prior report as
#2), **CF lung function** (Schaffer), **SGLT2i pharmacogenetics**
(Montasser), and **GLP-1 hematologic-cancer risk** (Chen). Four of the
five are on your active threads. This is the densest single-alert hit of
the last three windows and suggests Ryan's citation neighborhood
(OHDSI/pharmacoepi-causal-inference) overlaps your interests almost
exactly. Worth treating that alert as a near-mandatory read each
batch.

---

## NOTABLE: keyword-alert noise pattern (carried forward)

The 06-03 00:23 UTC keyword batch (12 alerts) had a worse signal-to-
noise ratio than the 06-02 author batch:

- **"drug repurposing"** → Li et al. "In silico analysis of LGR6 as a
  tumor suppressor in prostate cancer" (*J Cancer Metastasis*) — pure
  bioinformatics / in-silico target identification with no clinical-
  evidence loop. SKIP per INTERESTS (low interest in target-/chemistry-
  only pipelines).
- **"knowledge graph"** → "Transforming Natural Language into Knowledge
  Graph Queries with LinkQ" — agentic NL→SPARQL interface, non-biomedical
  KG. SKIP. (4th consecutive week of non-biomedical KG noise —
  recommendation to require biomedical co-occurrence still stands.)
- **"autoimmune disorders" or "autoimmune diseases"** → an Italian
  master's thesis on electronic stethoscope vibrating membranes that
  happens to mention ANCA. Pure false hit. SKIP.
- **"mendelian diseases"** → Zhang et al. two-sample MR + GraphBAN for
  kidney clear cell carcinoma. Same false-hit pattern as last week
  (mendelian randomization ≠ mendelian disease). SKIP. Recommendation
  from last report stands.
- **"electronic health records"** → Nemane et al. federated learning
  review in a non-MEDLINE journal. SKIP (review, low-tier venue).
- **"Foundation models and 'electronic health records'"** → Li & Zhang
  "AI-driven big data analysis and predictive modeling of infectious
  disease immunity" (*Archives of Microbiology*) — review, off-thread.
  SKIP.
- **"UK Biobank"** → Yu et al. birth weight × bone mineral density
  GWPA — single-trait UKB GWAS, not on a tracked disease. Borderline
  SKIP (methods-watch only if you care about GWPA-style epigenetic /
  developmental designs).
- **"rare diseases"** → Le Jeannic et al. DMD/BMD French national
  registry linked to insurance — registry-linked rare-disease
  pharmacoepi. METHODS-WATCH (registry-linkage template is reusable
  even though DMD is off-thread).

---

## arxiv-digest GitHub pipeline status

| Date | Relevant | Notes |
| --- | --- | --- |
| 2026-06-02 | 0 | Pipeline ran clean, zero matches in lookback window. |
| 2026-06-01 | — | No digest file generated for this date. |
| 2026-05-31 | 0 | 3/4 q-bio category fetch failures (q-bio.QM, q-bio.GN, q-bio.PE). |
| 2026-05-30 | 0 | No matches. |

The pipeline has now produced **zero on-thread papers for the last 8
days**. Same diagnosis as the prior two reports: the q-bio fetch
failures suggest an upstream arXiv API issue or a missing retry loop,
and the categorical scope is too narrow for where the genuinely on-
thread papers live (journals + bioRxiv/medRxiv + cs.LG + stat.ME).
Recommend prioritizing pipeline repair before the next cycle — eight
empty days is now a meaningful regression.

---

## Suggestions for the pipeline

Carrying forward and refining from the prior two reports:

1. **🔴 `arxiv-digest` pipeline is the top action item.** Eight days of
   zero relevant output. (a) Add retry-with-backoff on q-bio fetches.
   (b) Add `cs.LG`, `stat.ME`, and a medRxiv / bioRxiv source — based on
   the last three windows, ~85% of on-thread papers are journal /
   biorxiv. (c) Consider lowering `--min-score` for medRxiv/bioRxiv
   sources to catch preprints earlier (the Rich et al. AoU pre-cancer
   PheWAS would have been a HIGH match at min-score 1 if medRxiv were
   sourced).
2. **`knowledge graph` keyword remains noisy** (4th consecutive week).
   Require biomedical co-occurrence (e.g., `biomedical knowledge graph`
   OR `clinical knowledge graph` OR `medical knowledge graph`), or
   exclude obvious non-biomedical contexts (`manufacturing`,
   `industrial`, `SPARQL`-only).
3. **`mendelian diseases` keyword catching MR papers** (2nd consecutive
   week). Either exclude `-randomization` or merge into the genetic-epi
   `mendelian randomization` keyword.
4. **`autoimmune disorders`/`autoimmune diseases` keyword has now
   produced false hits two weeks running** (last week: NK-cell
   endocrine-autoimmunity review; this week: stethoscope thesis).
   Consider tightening to require co-occurrence with a tracked-cohort
   keyword.
5. **Patrick Ryan author alert is unusually high-value** — 4 of 5 papers
   on-thread in the latest batch. Consider promoting his author alert
   to a "near-mandatory" read tier; conversely, several author alerts
   (Szolovits citation churn, Vogelstein, Shendure, Natarajan) have not
   surfaced an on-thread paper in 3+ weeks and could be pruned.
6. **Add `proteome-wide` / `colocalization` / `cell-type-prioritization`
   keywords** — 4+ MR/coloc/cell-type-eQTL papers in the last three
   windows; the methodological shape is recurring and on-thread.
7. **Self-citation handling** (carried from prior report): Yang/
   Schaffer/Tran/Zeng/Park surfaced again in the AoU keyword feed via
   the related-research path. Decide whether to filter `-author:zeng`
   or leave as a citation-tracking signal.
