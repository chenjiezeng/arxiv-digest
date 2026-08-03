# Research digest report — 2026-08-03

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-08-01 12:35Z → 2026-08-03 12:35Z** (~2 days since the
last committed report at `reports/2026-08-01-research-digest.md`). Two
big Google Scholar batches fired in this window — 04:32Z and 10:51Z on
08-03 — after the 07-30 to 08-01 stretch of near-silence. Dense with
GLP-1 pharmacoepi and EHR-foundation-model methods work.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-01.md`, `08-02.md`) | 08-01, 08-02 (10:30Z crons) | Both empty (0 new; 2 + 1 previously-suppressed). Prior day (07-31) surfaced 1 causal-inference methods paper (DR-FRL, Ran/Shen/Guan) already covered in the 08-01 report. |
| Google Scholar author + keyword alerts | 08-01 21:30Z, 08-03 04:32Z, 08-03 10:51Z | 3 batches, ~45 author/keyword feeds fired. Densest signal this window. Notable: Chenjie Zeng, Denny, Bastarache, Karczewski, Hripcsak, Patrick Ryan, Hernán, Zitnik, Pascal Brandt, James Zou, Foundation-models-EHR keyword. |
| NCBI "My NCBI What's New" — AoU / UKB / drug repurposing | 08-01 17:14Z + 08-02 17:55Z | Six batches (three topics × two days). AoU: 0 + 1 (Kim et al. Neurosurg Focus grief framing — off-thread) = 1 item. UKB: 9 + 10 = 19 items (mostly cardiometabolic + nutrition; 2–3 on-thread flagged below). Drug repurposing: ~5 in 08-02 batch (mostly in-silico ADMET / preclinical — 0 on-thread). |
| JAMA Network Online First / New Online | 08-01 (AIDS 2026 Opti-DOR), 07-31 (New This Week) | Doravirine weight-gain trial (AIDS 2026), tau blood tests / AAIC 2026 coverage — not on-thread. |
| bioRxiv / medRxiv Subject Collection Alerts | daily | Aggregate feeds; on-thread preprints surfaced upstream (Wang/Hripcsak medRxiv appears via Hripcsak/Ryan author feeds — de-duped below). |

> Caveat: NCBI emails include title, authors, journal, DOI, and PMID
> but no abstract text. The reports below contextualize that metadata
> against research threads plus, where available, prior context from
> earlier reports and — for Scholar alerts — the 200–300 character
> Scholar snippet. Nothing here reflects full-text reading.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced in this 2-day window, clustering into four
knots.

**GLP-1 / SGLT2 pharmacoepi (5 items).** Dominant signal of the window,
riding the causal-inference + drug-target-triangulation sub-threads.

1. **Wang, Zhang, Lei, Lu, Zhang, Jian, Zhu et al. medRxiv 2026 (Hripcsak / Ryan lab)** —
   "Distributional Diagnosis and Calibration with Negative Controls for
   Outcome-wide Real-world Evidence." Fired on BOTH Hripcsak-articles
   and Ryan-articles feeds simultaneously — strong marker that this is
   the OHDSI group's next-generation OMOP outcome-wide calibration
   methodology, applied to GLP-1 RAs. Direct methods extension of
   Schuemie negative-control calibration.
2. **Xu, Maas, Huang, Wang, Créon et al. Kidney International 2026** —
   Heterogeneous treatment effects of GLP-1RA on kidney outcomes in
   T2D (target trial emulation vs DPP-4i, n>28k). Directly hits both
   the ML-for-precision-health (HTE) thread and the pharmacoepi thread.
3. **Hamad, Wiener, Golzar, Kaur, Henein et al. JAMA Network Open 2026** —
   GLP-1 RA and 3-year fragility fracture risk in T2D vs DPP-4i (Hernán
   citation). Fills the skeletal-outcome gap in the GLP-1 phenomic scan.
4. **Chen, Chang, Jhou, Chen, Huang et al. eClinicalMedicine 2026** —
   SGLT2 inhibitors and distant metastasis risk in breast cancer + T2D
   patients, target trial emulation with biological plausibility
   analysis (Ryan related-research). Rare drug × cancer × pharmacoepi
   triangulation.
5. **Matson, Venkatakrishnan, Murugadoss et al. Biology Methods 2026** —
   Semaglutide use associated with lower COVID-19 and influenza severity
   and better renal outcomes (Ryan related-research). Expands the GLP-1
   "pleiotropic-effect" phenomic literature.

**AoU-native genetics & CFTR carrier phenomics (3 items).**

6. **Zhang, Hong, Wang, Jurgens, Liu et al. Nat Commun 2026** —
   Transcript-aware rare genetic variant association analyses of
   cardiopulmonary traits in All of Us. Fired on Chenjie Zeng
   related-research feed. Direct methods extension of AoU rare-variant
   burden testing — pairs with Kore et al. local-ancestry burden (from
   the 08-01 report) as the "next AoU rare-variant methods you should
   read" pair.
7. **Turner, Boone, Haidar, Yang et al. Clin Transl Sci 2026** — CYP2C19
   c.681G>A LD-based pharmacogenetic testing miscalls, using All of Us.
   Directly on the "pharmacogenomic modifier of medication persistence"
   sub-thread from INTERESTS.md — a QC/methods paper every AoU PGx
   analysis needs to cite.
8. **Jiang, Sun. Digestive Diseases and Sciences 2026** — Elevated
   post-ERCP pancreatitis risk in heterozygous CFTR carriers. Directly
   on the CF/CFTR carrier phenomics thread — a discrete post-procedural
   endpoint modifiable by heterozygous status.

**EHR foundation models (3 items).** Aug 1 batch of the Foundation-models
+ EHR keyword alert fired with an unusually coherent trio.

9. **Placidi, Liu, Han, Rei, Faisal arXiv 2607.22114 (2026)** —
   Pretraining EHR foundation models with patient-aware sampling.
   Design-choice ablation on how sequence-construction affects
   downstream. Paired with #10 below (same lab, complementary paper).
10. **Liu, Placidi, Han, Balston, Rei, Faisal arXiv 2607.22264 (2026)** —
    Autoregressive EHR foundation models with multimodal inputs
    (adds ECG waveforms to tokenized EHRs). Directly on the multimodal
    EHR-FM sub-thread from INTERESTS.md.
11. **Lu, Chen, Treggiari, Blessing, Zhuo, Weng et al. arXiv 2607.22954
    (2026)** — Automated detection of documentation inconsistencies
    in EHRs (Weng lab, Columbia). On the EHR-representation-fidelity
    sub-thread — a portable QC layer for note-code coherence.

**One outstanding cross-thread item.**

12. **Diao, Sanchez, Sommer, Cohen et al. arXiv 2607.22504 (2026,
    Zitnik lab)** — Kidney function and kidney failure prediction in
    a large multiethnic population. Hits ML-for-precision-health,
    ancestry-stratified risk, and APOL1-adjacent CKD-progression
    signal simultaneously.

---

## Detailed writeups (HIGH items)

### 1. Wang, Zhang, Lei et al. — Distributional diagnosis + negative-control calibration for outcome-wide RWE (medRxiv 2026)

- **Thread:** Causal inference & pharmacoepi (distributional
  diagnostics sub-thread); GLP-1 RAs disease thread.
- **Signal strength:** HIGH. Fired on both Hripcsak-articles and
  Ryan-articles simultaneously — near-perfect provenance for an
  OHDSI-methodology paper.
- **What it does (from snippet):** GLP-1 RAs are linked to
  heterogeneous, potentially pleiotropic effects across organ
  systems, motivating outcome-wide comparative risk profiling in
  RWD. Central challenge is systematic bias from unmeasured
  confounding at scale; paper proposes distributional diagnosis
  (checking whether treatment-effect distributions across a bank of
  negative controls concentrate around the null) plus calibration
  against those negative controls, run at outcome-wide scale.
  Applied to GLP-1 RA comparative effectiveness.
- **Why it matters:** Extends Schuemie-style empirical calibration
  from point-estimate to distributional diagnostics. Portable across
  every OHDSI outcome-wide analysis you run — Trikafta, HRT,
  statins, GLP-1s.
- **Follow-ups:** medRxiv PMC13409211. Read the negative-control
  bank composition — will need OMOP concept IDs that map cleanly to
  AoU CDR v9. Check whether authors published code.

### 2. Xu et al. — HTE of GLP-1RA on kidney outcomes (Kidney International 2026)

- **Thread:** Causal inference & pharmacoepi (HTE sub-thread);
  ML-for-precision-health.
- **Signal strength:** HIGH.
- **What it does (from snippet):** Target trial emulation, new-user
  active-comparator design, n>28,000 initiating GLP-1RA vs DPP-4i.
  Identifies patient subgroups with differential kidney benefit —
  the "who to treat" question rather than the average.
- **Why it matters:** Directly targets the sub-thread from
  INTERESTS.md — "ML papers are HIGH when they're tied to a clinical
  decision (who to treat, who to screen)." This is that. Also fills
  a gap: the FLOW trial (SEMA-CKD 2024) gave the ATE; this gives the
  HTE.
- **Follow-ups:** Read the meta-learner architecture; check whether
  they used causal forest or a T/S/X-learner. Portable to your CFTR
  modulator persistence and HRT persistence pipelines if the
  covariate set overlaps.

### 3. Hamad et al. — GLP-1 RA and fragility fracture risk (JAMA Netw Open 2026)

- **Thread:** Causal inference & pharmacoepi; skeletal-outcome
  extension of GLP-1 phenomic scans.
- **Signal strength:** HIGH.
- **What it does (from snippet):** Comparative TTE, GLP-1 RA vs
  DPP-4i, 3-year fragility fracture endpoint. Cites Hernán's TARGET
  trial guidance paper.
- **Why it matters:** Weight-loss-associated bone loss has been a
  standing concern in the GLP-1 phenomic literature; this closes the
  loop with a clean TTE. Complements the Wang et al.
  outcome-wide-calibration paper by giving a single-endpoint anchor
  point.
- **Follow-ups:** Read whether they stratified by age × sex × baseline
  T-score. Consider replicating in AoU with a bone-loss phecode
  cluster.

### 4. Chen et al. — SGLT2i and breast cancer distant metastasis (eClinicalMedicine 2026)

- **Thread:** Causal inference & pharmacoepi (SGLT2i sub-thread);
  drug-repurposing (off-label cancer signal).
- **Signal strength:** HIGH.
- **What it does (from snippet):** TTE in patients with breast cancer
  + T2D; SGLT2i initiators vs non-initiators; primary endpoint
  distant metastasis. Includes a biological plausibility analysis
  layer.
- **Why it matters:** Drug-repurposing signal via
  causal-inference lens — matches the drug-repurposing sub-thread
  ("causal-inference framings of off-label use"). Also directly
  bridges pharmacoepi and cancer epi threads.
- **Follow-ups:** Read whether the biological plausibility analysis
  is pathway-level (glucose-transporter expression in tumor
  microenvironment) or MR-triangulated. Complements the CIRCS 2026
  SGLT2i cancer literature building since Bakris.

### 5. Matson et al. — Semaglutide and infection outcomes (Biology Methods 2026)

- **Thread:** GLP-1 pharmacoepi (pleiotropic effects).
- **Signal strength:** METHODS-WATCH → HIGH given the growing
  "everything gets better on GLP-1s" phenomic scan noise problem.
- **What it does (from snippet):** Prior semaglutide exposure
  associated with lower COVID-19 and influenza severity and better
  post-infection renal outcomes in older adults with cardiometabolic
  disease.
- **Why it matters:** Adds infection endpoints to the GLP-1 phenomic
  scan. Combined with the Wang et al. distributional-diagnosis paper
  (#1), this window's signal is that GLP-1 phenomic breadth needs
  the negative-control calibration layer before more discovery
  claims land.
- **Follow-ups:** Read the negative-control set. Check whether
  susceptibility bias (healthier patients get semaglutide, then
  also get vaccinated) was addressed.

### 6. Zhang, Hong, Wang, Jurgens, Liu et al. — Transcript-aware AoU rare-variant methods (Nat Commun 2026)

- **Thread:** PheWAS / phecode infrastructure; EHR-linked biobanks
  (AoU); genetic epi.
- **Signal strength:** HIGH. Fired on Chenjie Zeng related-research
  feed.
- **What it does (from snippet):** Framework for aggregating rare
  variants at the transcript level rather than the gene level.
  Simulations show it maintains false-positive control while
  capturing transcript-specific effects that gene-level burden
  tests miss. Applied to AoU cardiopulmonary traits.
- **Why it matters:** Directly complements the Kore et al.
  local-ancestry-informed burden paper flagged in the 08-01 report.
  Together they form the "you should re-score every AoU rare-variant
  burden test under both frameworks" pair. Transcript-aware is
  particularly relevant for genes with multiple annotated
  transcripts and tissue-specific isoform usage (CFTR is a classic
  example — different transcripts in airway vs pancreatic epithelium).
- **Follow-ups:** Read whether they published code. Check whether
  the transcript-aware aggregator is compatible with SAIGE-GENE+ or
  requires their own solver. Directly applicable to your CFTR
  carrier phenomic scans and to hereditary cancer gene burden tests.

### 7. Turner, Boone, Haidar, Yang et al. — CYP2C19 LD miscalls in AoU (Clin Transl Sci 2026)

- **Thread:** Pharmacogenomic modifier of medication persistence
  sub-thread; variant interpretation.
- **Signal strength:** HIGH.
- **What it does (from snippet):** CYP2C19 c.681G>A and c.332-23A>G
  are NOT in complete LD as often assumed. Documented in All of Us
  participants. Implications for pharmacogenetic testing accuracy.
- **Why it matters:** Standing pharmacogenetic assays often infer
  one variant from the other under an LD assumption. If broken in
  admixed populations (which AoU oversamples), that's a systematic
  miscall of CYP2C19 metabolizer status → miscalled
  clopidogrel/PPI/SSRI/statin metabolism.
- **Follow-ups:** Extract the specific ancestry groups where LD
  breaks. Directly relevant to any PGx-modifier-of-persistence
  analysis in AoU (e.g., statin discontinuation stratified by
  CYP2C19 phenotype).

### 8. Jiang, Sun — Post-ERCP pancreatitis in CFTR heterozygotes (Dig Dis Sci 2026)

- **Thread:** CF / CFTR carrier phenomics.
- **Signal strength:** HIGH — hits the CF/CFTR carrier thread
  precisely.
- **What it does (from snippet):** Post-ERCP pancreatitis (PEP)
  incidence up to 15% overall; paper reviews evidence that CFTR
  heterozygotes are at elevated PEP risk. Framing is heterozygous
  carrier state as a modifier of a common procedural complication.
- **Why it matters:** Adds a discrete peri-procedural endpoint to
  the CFTR heterozygote phenomic literature — historically dominated
  by chronic pancreatitis and sinusitis. If replicable in AoU / MVP,
  a candidate for pre-procedure CFTR screening in high-risk ERCP.
- **Follow-ups:** Check whether it's a primary cohort or a review;
  if primary, extract the OR and n. Consider a phecode-based
  replication in AoU (K85 acute pancreatitis phecode + ICD procedure
  code for ERCP within a defined window).

### 9. Placidi, Liu, Han, Rei, Faisal — Patient-aware sampling for EHR-FM pretraining (arXiv 2607.22114)

- **Thread:** EHR foundation models (CLMBR/MOTOR/EHRSHOT lineage).
- **Signal strength:** HIGH.
- **What it does (from snippet):** Autoregressive EHR-FMs typically
  inherit pretraining recipes from LM (random windowing, uniform
  sampling across patients). Paper argues patient-aware sampling
  (weighting by patient trajectory density, length, or diagnostic
  richness) is an important-but-underexplored design axis.
- **Why it matters:** The "which representation choice drives
  downstream performance vs. the model architecture" question from
  the INTERESTS.md knowledge-representation thread — this is a
  representation-ablation on pretraining data itself. Direct read
  for anyone planning CLMBR/MOTOR fine-tunes.
- **Follow-ups:** Read whether the fair-cohort ablations tested
  ancestry-stratified pretraining recall. If so, portable to
  ancestry-fairness audits of EHR-FMs.

### 10. Liu, Placidi, Han, Balston, Rei, Faisal — Multimodal autoregressive EHR-FM (arXiv 2607.22264)

- **Thread:** EHR foundation models (multimodal sub-thread — notes
  + codes + waveforms + imaging).
- **Signal strength:** HIGH. Same lab as #9, released together.
- **What it does (from snippet):** Framework for conditioning
  autoregressive EHR-FMs on auxiliary clinical modalities, starting
  with ECG waveforms fused with tokenized EHR events. Zero-shot
  clinical prediction is the stated downstream.
- **Why it matters:** Multimodal EHR-FMs are the frontier and
  papers with actual reproducible fusion architectures are still
  rare — MedTok did codes+notes, this adds waveform. Pairs with
  the Zhang trustworthy patient-trajectory dissertation surfaced
  in the same Scholar batch.
- **Follow-ups:** Check waveform tokenization strategy (VQ-VAE?
  continuous embedding + gating?) and whether it can be swapped
  for imaging-derived embeddings later.

### 11. Lu, Chen, Treggiari, Blessing, Zhuo, Weng et al. — Documentation-inconsistency detection in EHR (arXiv 2607.22954)

- **Thread:** EHR phenotyping & OMOP; representation fidelity /
  audit sub-thread.
- **Signal strength:** HIGH — Weng (Columbia, Chunhua Weng lab)
  is a reliable signal source for EHR-phenotyping methodology.
- **What it does (from snippet):** LLM-based framework for detecting
  when EHR codes and free-text notes disagree about a diagnosis or
  clinical event — a two-stage LLM pipeline that first generates
  candidate inconsistency pairs and then reasons about each. Framed
  as an ontology-and-schema-grounded framework, not a black-box
  classifier.
- **Why it matters:** EHR phenotypes assume codes and notes reflect
  the same underlying event. That assumption breaks systematically
  (billing-driven overcoding, negation in notes, temporal
  displacement). This is a portable QC layer for note-code coherence
  audits — directly applicable when validating AoU phecode
  definitions against unstructured note text.
- **Follow-ups:** Read the ontology framework (SNOMED-anchored?
  UMLS?), check whether they released the LLM prompts, and whether
  they benchmark on MIMIC-IV.

### 12. Diao, Sanchez, Sommer, Cohen et al. — Multiethnic CKD/kidney-failure prediction (arXiv 2607.22504)

- **Thread:** ML for precision health; ancestry-stratified risk in
  EHR-linked cohorts; APOL1-adjacent.
- **Signal strength:** HIGH. Zitnik-authored feed.
- **What it does (from snippet):** Prediction of current kidney
  function and progression to kidney failure in a large multiethnic
  population. Framed around the need for accurate individualized
  trajectory estimates in CKD.
- **Why it matters:** Directly hits the ancestry-stratified /
  APOL1-adjacent thread. Historic CKD risk equations (CKD-EPI, KFRE)
  have well-documented recalibration failures across ancestries;
  this appears to be an ML alternative on a multiethnic training
  set. Whether it explicitly modeled APOL1 genotype as a feature
  will determine how much it advances the APOL1-progression
  question specifically vs. the general multiethnic-recalibration
  question.
- **Follow-ups:** Read whether APOL1 is a feature; whether the
  fairness audit is per-ancestry decision-curve analysis; and
  whether the training cohort is UKB + AoU + something else. Pair
  with the Xu et al. GLP-1RA kidney HTE paper (#2) as the
  "who benefits from what CKD intervention" pair.

---

## METHODS-WATCH (off-thread disease but exemplary methods)

- **Silberg, Eckmann, Boen, Zou. Circulation 2026** — "Agentic and
  Generative AI for Drug Discovery." Zou-lab framing paper in a
  cardiovascular venue. Useful as a citation anchor for agentic-AI
  framing but methods themselves are review-level, not new.
- **Chen, Cong, Jin et al. arXiv 2607.25242** — "Medical world models
  in healthcare: foundations, applications, and challenges for
  trustworthy clinical translation." Review-level survey of the
  medical-world-model literature; useful for the CLAUDE.md context
  file, not a primary source.
- **Rodriguez, Hauke, Kayali et al. Leukemia 2026** — JAK2 V617F
  clonal hematopoiesis in germline BRCA1 vs BRCA2 carriers. Sits at
  the CHIP × hereditary-cancer intersection but the cohort is
  Cologne single-center. Watch as background for BRCA carrier
  phenomic scans that include hematologic outcomes.
- **Weeks, Neuberg, Limerick et al. Blood 2026** — Donor and recipient
  clonal hematopoiesis in non-myeloablative transplant for sickle
  cell disease. Interesting for the "somatic mosaicism after cellular
  therapy" question raised by CHIP + gene-therapy safety.
- **Beger, Strobach, Schäfermeier et al. J Biomed Semantics 2026** —
  TOP framework for collaborative phenotyping algorithm development.
  Another entry in the crowded phenotype-algorithm-authoring space
  (alongside PheKB, Phenoflow, etc.). Read only if you're planning a
  new phenotype-sharing infrastructure decision.
- **Jang, Sultana, Yao et al. JMIR AI 2026** — LLM identification of
  important medical jargon in EHR notes for patient-facing
  translation. Note-side NLP; potentially useful for note-code fusion
  pipelines but framed as a patient-comprehension tool.
- **Márquez-Luna, Tournaire, Rocheleau, Do, Verbanck. Genet Epidemiol
  2026** — "The Omnicausal Model Reveals the Highly Polyfactorial
  Nature of Complex Diseases" (Do lab, UKB). Framing paper for
  composite-risk / everything-is-polygenic argument. Read for
  positioning your own PGS residuals / polygenic-deviation work
  vis-à-vis the omnigenic → omnicausal literature.
- **Li, Ge, Du et al. Advanced Science 2026** — Large-scale WES
  (356,982 UKB) defining the protein-coding architecture of retinal
  structure, visual function, and blinding diseases. Karczewski
  citation. Cross-tissue reference for the exome-wide association
  framework.
- **Seow, Mina, Hebrard, Sadhu, Bellis et al. Nat Genet 2026** —
  Singapore National Precision Medicine (NPM) program phase II. Not
  on any specific thread, but the international comparator for AoU;
  cites Denny's AoU genomics paper. Useful as the "how other
  national programs frame their translation strategy" reference for
  cross-biobank grant/manuscript framing.
- **Burkhardt, Blach, Burugapalli et al. JAMIA Open 2026** — Truveta
  RWD platform description. Not immediately usable, but Truveta is
  the largest US health-system-federated RWD contender to Optum and
  IQVIA; worth knowing exists.
- **Chen, Zahedi, Chhuo, Nguyen et al. arXiv 2026 (Zitnik related)** —
  Harmonised benchmarking of single-cell and spatial transcriptomics
  foundation models, context-dependent generalisation. Portable
  benchmarking framework, transferable to EHR-FM audit design.

---

## SKIP (surfaced but off-thread)

- Google Scholar batch: STEM automated defect fabrication (Callahan
  related), sports cardiology LLMs (Szolovits related), Greek GLP-1
  neurodegeneration review (Luo citation), Ghana EHR user survey
  (Hripcsak related), Vision-language-model self-reflection (Szolovits
  related), Nature MI "collaboration outgrown" (Natarajan citation),
  humanoid surgical robots (Rajpurkar), CKD West African dietary
  patterns (APOL1 keyword hit, not APOL1 biology).
- UKB NCBI 08-02: TMAO-microbiome-AFib (JCI), body-shape × preeclampsia
  cross-trait, evolutionary constraint × RBP variant burden — all
  off-thread.
- Drug repurposing NCBI 08-02: flavoxate for Alzheimer's (in-silico
  only), dengue haemorrhagic fever repurposing (in-silico only),
  atorvastatin frankincense hydrogel (preclinical) — no clinical-
  evidence-loop signal.
- CRISPR breast-cancer risk-loci thesis (Sevgi 2025) — thesis-only,
  cites Chenjie Zeng's paper for context. Not a peer-reviewed primary
  source to prioritize.
- Bastarache citation batch: mostly off-thread (orthopedic-rare-disease
  LLM, PONV RCT, allergy/immunology AI, sex chromosome aneuploidies
  advocacy).
- Hripcsak related: HFrEF best-practice-advisory quality-improvement
  study (Velez Oquendo et al.), FHIR pattern languages — infrastructure
  papers, not phenotyping methods.
- Cystic fibrosis (Ryan related): pulmonary exacerbation FVC vs FEV1
  (McElvaney et al. J Cyst Fibros) — clinical, not on the pharmacoepi
  / modulator-persistence sub-thread. Elexacaftor peripheral leukocyte
  profiles (Pyzia et al. Respir Med) — mechanistic biomarker, not
  outcome pharmacoepi.

---

## Continuity items to watch next window

- **Wang/Hripcsak distributional-diagnosis** appeared on medRxiv
  this window; watch for the peer-review venue and whether the
  negative-control bank is released as an OMOP concept set.
- **Placidi/Liu/Faisal EHR-FM pair** (patient-aware sampling +
  multimodal) — watch for a benchmark comparison against CLMBR /
  MOTOR when the next EHRSHOT leaderboard update lands.
- **Scholar batch is now firing on the 04:32Z + 10:51Z schedule
  again after the 07-30 → 08-01 quiet window** — the next report
  window should expect a full batch (not the sparse pattern of last
  week).
