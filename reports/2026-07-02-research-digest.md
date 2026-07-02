# Research digest report — 2026-07-02

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-02** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 07-02 | Large batch on 07-01 06:15Z (≈20+ author-feed alerts: Bastarache, Karczewski, Denny/Hripcsak, Yang, Montgomery, Szolovits, Chute, Shendure, Zitnik, Natarajan, Pritchard, Ryan, Brandt, Collins, Celi, Vogelstein). Second keyword batch 07-01 22:24Z (UKB, EHR, foundation-models-in-EHR, rare-diseases, drug-repurposing, KG, PheWAS, autoimmune, APOL1, mendelian). |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-02 | 06-23: 2 papers (CF causal inference — on-thread); 06-25: 2 papers; 06-26: 1 paper; 06-30: 4 papers; 07-01: 7 papers (one strong UKB on-thread, one causal-inference-methodology on-thread); 07-02: 1 paper (Airbnb, off-thread). Empty/near-empty days: 06-21, 06-22, 06-24, 06-27, 06-28, 06-29. |
| NCBI "My NCBI What's New" (UK Biobank, All of Us) | 2026-07-01 | Aggregate PubMed digest emails; not individually triaged here — worth a manual pass if you want the peer-reviewed slice. |
| medRxiv Collection Alert (Endocrinology / Diabetes / Metabolic) | 2026-07-02 | Aggregate; not individually triaged. |
| JAMA / JAMA Network Open online-first | daily | Table-of-contents alerts; not individually triaged. Nothing screamed on-thread from subject lines. |
| alphaXiv weekly digest | 2026-07-01 | Trending-papers roundup; not individually triaged. |

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. The `arxiv-digest` entries include the full abstract
> as pulled by the pipeline.

---

## Executive summary

- **The standout in the Scholar feed is a phecode-methodology paper by
  the Bastarache group — arriving on the Bastarache new-articles alert
  the day it indexed.** Padovani-Claudio, Lewis, Bastarache, He —
  *Determination and GWAS validation of optimal minimal phecode count
  for eye disease cohort generation* (*Investigative Ophthalmology &
  Visual Science*, 2026). Directly on the **PheWAS / phecode
  infrastructure** thread: it addresses the *how many phecode
  occurrences make a case?* threshold-setting problem that shows up in
  every phecode-based cohort you build, and validates the answer
  against GWAS signal recovery. Bastarache is a core author in the
  phecode-methodology network. **HIGH — read first.**
- **The standout on `arxiv-digest` is a UK Biobank cardiometabolic
  proteomics paper that fuses curated-DB priors with covariate-
  dependent Gaussian-graphical-model estimation.** Mapelli, Massi,
  Cuccuru, Di Angelantonio, Ieva — *Prior-informed conditional Gaussian
  graphical models: an application to protein interaction network
  reconstruction* (arXiv 2606.31805v1, 2026-06-30, stat.AP). n=49,129
  UKB participants, 366 proteins, T2D-associated network perturbations,
  34 network-central candidate biomarkers. Hits the **biobanks with EHR
  linkage** + **ML for precision health** + **multimorbidity**
  intersection at once. **HIGH.**
- **A directly-usable causal-inference alternative to AIPW/TMLE when
  positivity is thin.** Naimi, Jin, Yu, Parisi, Bodnar — *Residual-on-
  Residual Regression as a Tool for Effect Estimation in Observational
  Data* (arXiv 2606.30976v1, 2026-06-29, stat.ME). Argues that when the
  exposure effect is approximately constant (partially linear model),
  residual-on-residual OLS is competitive with AIPW/TMLE and
  *outperforms* both under positivity violations. Directly relevant to
  the **causal inference & pharmacoepidemiology** thread — this is the
  kind of triangulation-check you want in a GLP-1 / SGLT2i / CFTR
  modulator real-world comparison. **HIGH (methods).**
- **A cystic-fibrosis pharmacoepi methods paper hitting your CF + causal
  threads simultaneously.** Murali, Barnatchez, Hoppe, Wagner, Keller,
  Josey — *Causal Inference with Multiple Misclassified Exposures: A
  Control Variate-Adjusted Calibration Weighting Approach* (arXiv
  2606.23656v1, 2026-06-22, stat.ME). Throat swab vs. sputum culture
  misclassification of *P. aeruginosa* and *S. aureus* in a n=651 CF
  cohort; swab-based estimates attenuate the FEV1 effect by ~69%.
  Two-keyword `causal inference` + `cystic fibrosis` hit. **HIGH.**
- **HPO-based cell-type contextualisation of the human phenome, aimed
  at rare-disease systematic treatment.** Schilder, Murphy, Dash, Zhang
  et al. — *Cell type-specific contextualisation of the human phenome:
  towards the systematic treatment of all rare diseases* (*Genome
  Medicine*, 2026, Bastarache related-research feed). Sits at the
  intersection of the **HPO / ontologies**, **rare disease**, and
  **drug repurposing** threads (systematic treatment = drug-target /
  repurposing angle for rare disease). **HIGH.**
- **Record linkage of de-identified research datasets using diagnosis
  codes.** Hejblum et al. — *Probabilistic record linkage of
  de-identified research datasets with discrepancies using diagnosis
  codes* (*Scientific Data*, 2026, Szolovits new-articles feed).
  Directly on the **EHR phenotyping** thread — the ICD-code-driven
  linkage pattern is exactly what shows up when you try to link two
  de-identified biobank slices. **HIGH.**
- **OMOP + multi-agent LLM for Chinese medical text standardisation.**
  Lv, Wang, Wang, Li — *DIMAS-OMOP: A Deliberative Intelligence-Based
  Multi-Agent System for Chinese Medical Text Standardization toward
  OMOP* (Multilinguality Workshop 2026, Patrick Ryan related-research
  feed). On the **EHR phenotyping & OMOP** + LLM-assisted phenotyping
  intersection. **METHODS-WATCH → HIGH** if the eval quality holds up;
  worth pulling the paper.
- **arxiv-digest pipeline health is back to normal after the 06-20
  fetch-failure blip.** All 12 windows since the last report produced
  either real hits or a clean "0 relevant" (no partial-fetch warnings).
  Empty-day rate is high (roughly half the window), which is a keyword
  problem, not a pipeline problem — see closing note.

Counts (rough): **6 HIGH**, **4 METHODS-WATCH**, rest SKIP. The window
is dense in the Scholar feed but sparse on `arxiv-digest`, with the
sparsity concentrated in a run of small-hits days.

---

## Detailed reports — HIGH bucket

### 1. Padovani-Claudio, Lewis, Bastarache, He — *Determination and GWAS validation of optimal minimal phecode count for eye disease cohort generation*
- **Venue / date:** Investigative Ophthalmology & Visual Science, 2026 (Scholar-indexed 2026-07-01).
- **Source:** Lisa Bastarache new-articles Scholar feed.
- **Fit:** PheWAS / phecode infrastructure (core); genetic epi (secondary — GWAS validation of case definition).
- **What the abstract snippet says:** the paper determines the optimal minimum count of phecode occurrences required to call an eye-disease case in EHR-derived cohorts, then validates the resulting case definition by demonstrating recovery of known GWAS signal for those eye conditions.
- **Why it matters:** the "how many phecode occurrences = a case" threshold is one of the perennial ambiguities in PheWAS pipelines (Denny 2010 used ≥2; Wei 2017 and Bastarache's later work formalised it; many downstream users still pick thresholds by convention). Using GWAS-signal recovery as the *validation criterion* is exactly the right move — the case definition is only as good as its ability to preserve heritability. This is the kind of paper that becomes an infrastructure reference the next time you have to justify a phecode-count threshold in a manuscript.
- **What to do with it:** pull the PDF and check (a) whether the optimal threshold is disease-specific or generalisable across the eye-disease phecode subtree, (b) whether the ancestry breakdown affects the threshold, and (c) whether the validation method is reusable outside ophthalmology. If it generalises, add it to the phecode-methodology reference set.
- **Priority:** HIGH — read first.

### 2. Mapelli, Massi, Cuccuru, Di Angelantonio, Ieva — *Prior-informed conditional Gaussian graphical models: an application to protein interaction network reconstruction*
- **Venue / date:** arXiv 2606.31805v1, 2026-06-30, stat.AP.
- **Source:** `arxiv-digest` 2026-07-01 (score 3: `uk biobank`, `biobank`, `precision medicine`).
- **Fit:** biobanks with EHR linkage (UKB proteomics); ML for precision health; multimorbidity (cardiometabolic, T2D-adjacent).
- **Method:** conditional Gaussian graphical model with a structured weighted penalty that selectively incorporates database-derived interaction priors into population-level network estimation, while covariate-dependent perturbations remain data-driven. Simulation shows robust improvement even when priors are imperfect.
- **Application:** UK Biobank cardiometabolic proteomics, **n = 49,129, p = 366 proteins**. Recovers T2D-associated network perturbations; identifies **34 network-central candidate biomarkers** — several detectable *only* through connectivity, not differential expression. Reveals six biologically coherent protein communities spanning metabolic, cardiovascular, and cancer-related pathways.
- **Why it matters:** three things converge here that fit your threads. (1) It's a **UKB proteomics** paper at real biobank scale — n≈50K, not a boutique subcohort. (2) It's a **network-centrality biomarker discovery** paper — some candidates are only detectable via their graph position, which is the "biomarker discovery beyond differential expression" pattern you flagged in INTERESTS. (3) It's **T2D cardiometabolic** — which is the shared multimorbidity substrate under GLP-1 / SGLT2i pharmacoepi.
- **What to do with it:** the code is on GitHub (`AlessiaMapelli/Prior-informed-conditional-GGMs`) — worth checking whether the prior-informed penalty is a general framework or specific to their protein setup. If general, it's a candidate for the phenome-wide MR / biomarker-scan work in the genetic-epi thread.
- **Priority:** HIGH.

### 3. Naimi, Jin, Yu, Parisi, Bodnar — *Residual-on-Residual Regression as a Tool for Effect Estimation in Observational Data*
- **Venue / date:** arXiv 2606.30976v1, 2026-06-29, stat.ME.
- **Source:** `arxiv-digest` 2026-07-01 (score 2: `inverse probability`, `causal inference`).
- **Fit:** causal inference & pharmacoepidemiology (core); ML for precision health (secondary).
- **Argument:** epidemiologists are increasingly leaning on ML for high-dim confounding. AIPW and TMLE are the two dominant estimators, but they can diverge from each other and both are unstable under weak positivity. **Residual-on-residual (RoR)** — fit confounder-adjusted models for outcome and exposure, then OLS the outcome-residuals on the exposure-residuals — is a stable partially-linear-model alternative.
- **Empirical:** nuMoM2b cohort (**n = 7,923**), estimating association between high vegetable intake density and preeclampsia. RoR, AIPW, and TMLE **converge** on a modest protective estimate; RoR simulations show near-nominal coverage and comparable performance to AIPW/TMLE in general, and **substantially better performance than AIPW/TMLE under positivity violations** when the true effect is partially-linear-model coded.
- **Why it matters:** this is a direct triangulation tool for the drug-class threads (GLP-1 RAs, SGLT2is, CFTR modulators, HRT). Positivity is exactly the problem in modulator-eligibility cohorts (CFTR: everyone with an eligible genotype gets prescribed; almost no untreated concurrent controls at some sites) — RoR is a natural third estimator to add alongside AIPW/TMLE when you want to demonstrate the estimate isn't AIPW-specific.
- **Caveat:** the "approximately constant effect" assumption matters. For heterogeneous-treatment-effect work (causal forests, meta-learners), RoR loses its interpretability edge.
- **What to do with it:** file as a triangulation-estimator reference in the causal-inference toolkit. Worth writing the RoR pass into the next real-world modulator or SGLT2i analysis as a sensitivity.
- **Priority:** HIGH (methods).

### 4. Murali, Barnatchez, Hoppe, Wagner, Keller, Josey — *Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach*
- **Venue / date:** arXiv 2606.23656v1, 2026-06-22, stat.ME.
- **Source:** `arxiv-digest` 2026-06-23 (score 2: `causal inference`, `cystic fibrosis`).
- **Fit:** CF disease thread (core); causal inference & pharmacoepi (core).
- **Setup:** in CF respiratory infection studies, throat swabs are frequently used as a proxy for sputum culture for *P. aeruginosa* and *S. aureus*, but throat swabs have imperfect sensitivity/specificity — i.e. the exposure is misclassified. The paper develops **calibration weighting** and **control-variate-adjusted** estimators for causal inference with *multiple* misclassified binary exposures under clustered observations.
- **Method:** calibration treats misclassification as a missing-data problem (consistent without modelling the misclassification mechanism). Control-variate integrates the error-prone observations to reduce variance while preserving the gold-standard estimator's consistency. Doubly robust.
- **Empirical:** **n = 651 CF patients**, ages 6–21. **Swab-based estimates attenuate the effect of *P. aeruginosa* on percent-predicted FEV1 by ~69% vs. sputum** (−2.67 vs. −8.52 percentage points; sputum 95% CI −13.40, −3.63). Interpretation: swab-based surveillance materially underestimates *P. aeruginosa*'s pulmonary impact, which would lead to under-treatment.
- **Why it matters:** it lands on both your CF thread and your causal-inference thread at once, with a clinically actionable takeaway (swab surveillance may drive under-treatment). It also generalises — misclassified categorical exposure is a broader problem than CF respiratory culture; the framework is reusable anywhere you have a gold-standard-vs-proxy comparison (e.g., EHR-derived medication vs. dispensing-record medication).
- **What to do with it:** worth full-reading — the CF real-world use case is directly usable as prior art for any CF modulator + infection interaction analysis, and the misclassification framework is more broadly usable across EHR pharmacoepi where the "exposure" is really a proxy.
- **Priority:** HIGH.

### 5. Schilder, Murphy, Dash, Zhang, et al. — *Cell type-specific contextualisation of the human phenome: towards the systematic treatment of all rare diseases*
- **Venue / date:** *Genome Medicine*, 2026 (Bastarache related-research feed, Scholar-indexed 2026-07-01).
- **Fit:** knowledge graphs & ontologies (HPO); rare disease; drug repurposing.
- **What the snippet says:** the paper appears to contextualise the human phenome by cell type, with the explicit framing of *systematic treatment of all rare diseases* — implying HPO-level phenotype-to-cell-type mapping used to drive treatment hypotheses.
- **Why it matters:** this is a rare instance where three of your threads converge in one paper: (a) **HPO / ontology** (phenome contextualisation), (b) **rare disease** (target population), (c) **drug repurposing** (systematic-treatment framing). The "explainable hypothesis output" criterion you flagged in INTERESTS for drug repurposing — path or subgraph rationales rather than opaque link-prediction scores — is exactly what a cell-type-anchored phenome-to-treatment map should produce.
- **What to do with it:** pull the paper. Two key checks: (1) how granular is the cell-type resolution (single-cell atlas–derived? bulk-tissue-derived?), and (2) how does the treatment recommendation flow — is it phenome → cell-type → target → compound, or does it short-circuit? If it's the former, this is a reference architecture for your drug-repurposing thread.
- **Priority:** HIGH.

### 6. Hejblum et al. — *Probabilistic record linkage of de-identified research datasets with discrepancies using diagnosis codes*
- **Venue / date:** *Scientific Data*, 2026 (Peter Szolovits new-articles feed, Scholar-indexed 2026-07-01).
- **Fit:** EHR phenotyping (core); biobanks with EHR linkage (secondary — cross-cohort matching).
- **What the snippet says:** probabilistic record-linkage method for de-identified research datasets when diagnosis codes disagree between the source datasets. Boris Hejblum first-author (French biostatistics group with a long track record in survival / competing-risks).
- **Why it matters:** whenever you have to combine two de-identified biobank slices (or a biobank + external claims / registry), diagnosis-code disagreements are the norm, not the exception — the same person's records disagree on ICD codes between two systems because the coding practices diverged. A principled probabilistic linkage that *models the discrepancy* instead of requiring exact match is directly useful for the AoU × MVP × BioVU × UKB cross-cohort work you flagged.
- **What to do with it:** pull the paper. Key questions: (a) does the model require gold-standard training pairs or is it fully unsupervised, (b) does it degrade gracefully when the two datasets are on different ICD versions (ICD-9 vs ICD-10) or different code systems (ICD vs phecode vs OMOP concept), and (c) is there a reference implementation.
- **Priority:** HIGH.

---

## Detailed reports — METHODS-WATCH bucket

### 7. Lv, Wang, Wang, Li — *DIMAS-OMOP: A Deliberative Intelligence-Based Multi-Agent System for Chinese Medical Text Standardization toward OMOP*
- **Venue / date:** 1st Workshop on Multilinguality in the Era of LLMs, 2026 (Patrick Ryan related-research feed).
- **Fit:** EHR phenotyping & OMOP.
- **Snippet:** multi-agent LLM system for standardising Chinese-language clinical text into OMOP-CDM concepts.
- **Why it matters:** the OMOP-CDM concept-mapping problem is exactly the bottleneck for multilingual EHR federation. If the deliberative multi-agent framing produces measurable gains over single-LLM baselines on Chinese → OMOP, the same architecture is a candidate for other under-represented languages, and the deliberation traces are useful for auditability.
- **Caveat:** workshop paper, so the eval may be small; multi-agent LLM standardisation frameworks proliferate and most don't beat well-prompted single-LLM baselines. Worth a skim before committing time.
- **Priority:** METHODS-WATCH.

### 8. Faes, van den Berg, Amir Haeri — *Privacy-preserving federated tensor decomposition of single-cell immune data: recovering multicellular programs across institutions*
- **Venue / date:** arXiv 2606.24938v1, 2026-06-22, q-bio.GN.
- **Source:** `arxiv-digest` 2026-06-25 (score 1: `cross-ancestry`).
- **Fit:** cross-ancestry portability (genetic epi thread); EHR-linked biobank federation (adjacent — same federation problem, single-cell substrate).
- **Method:** each site computes a local program subspace; a coordinator merges by stacked SVD under federated global-mean centering — provably equivalent (up to truncation) to the centralised decomposition. Compatible with secure aggregation.
- **Empirical:** 261-donor SLE atlas — canonical interferon program recovered (ISG enrichment AUC 0.998); ILD atlas — recovered program predicts disease better than the best single cell type; three real COVID-19 sites cross-institution recovery. Membership-inference attack AUC drops from 0.91 to 0.61 under secure aggregation.
- **Why it matters:** the federated-multi-site pattern (each site keeps its cells, only subspaces leave) is the same pattern that unblocks cross-consortium biobank analysis where cell-level or individual-level pooling is governance-blocked. Not immediately reusable for your bulk-EHR + variant work, but architecturally instructive.
- **Priority:** METHODS-WATCH.

### 9. Böhringer, Holzmann — *Evaluating HWE and Association in Genome Wide Association Studies: A Unified Procedure*
- **Venue / date:** arXiv 2606.30311v1, 2026-06-29, stat.ME.
- **Source:** `arxiv-digest` 2026-06-30 (score 1: `fine mapping`).
- **Fit:** genetic epi (GWAS methods, fine-mapping downstream).
- **Method:** conditional genotype-based test that conditions the Pearson χ² of the 3×2 SNP-genotype-vs-phenotype table on the HWE χ² in the control group — asymptotic theory developed. Removes the arbitrary-threshold HWE QC step and improves SNP ranking. Simulation shows it's more powerful than two competing retrospective procedures.
- **Why it matters:** HWE thresholds are the classic "arbitrary QC decision" in GWAS pipelines. Unifying them with the association test is nicer than post-hoc filtering. Improved SNP ranking flows into fine-mapping downstream.
- **Priority:** METHODS-WATCH (only relevant if you're QC-authoring GWAS pipelines rather than consuming summary stats).

### 10. Loe, Murry, Wu — *Dynamic Prediction of Alternating Recurrent Events via Neural Network*
- **Venue / date:** arXiv 2606.30889v1, 2026-06-29, stat.ML.
- **Source:** `arxiv-digest` 2026-07-01 (score 1: `inverse probability`).
- **Fit:** ML for precision health (dynamic prediction); adjacent to causal inference (IPW pseudo-observations).
- **Method:** neural network for online dynamic prediction of alternating recurrent event-free time; uses inverse-probability-weighted pseudo-observations to handle censoring. Application: predicting low-mood periods in first-year medical residents.
- **Why it matters:** alternating recurrent events (event → refractory period → event) show up in EHR longitudinal data — hospitalisation → recovery → readmission, exacerbation → remission → exacerbation. The IPW pseudo-observation framing is directly compatible with your causal-inference toolkit.
- **Priority:** METHODS-WATCH.

---

## Skimmed / SKIP

- **07-02 `arxiv-digest`** — Wu, Schmierer, *Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example* (cs.LG). Keyword hit: `causal inference`. SKIP — marketplace optimisation, wrong domain.
- **07-01 `arxiv-digest`** — Wu, Schmierer, Zylberglejd, *Estimating Supply Incrementality in Two-sided Marketplaces* (cs.LG); Wu, Gu, Deng, Zhu, Chen, *Hierarchical Clustering As a Novel Solution to the Notorious Multicollinearity Problem in Observational Causal Inference* (stat.ME). Both cs.LG marketplace-flavored — SKIP for research, though the multicollinearity paper's clustering trick could be a curiosity read.
- **07-01 `arxiv-digest`** — Guan et al., *Can Tabular In-Context Learners Generalize to Biomolecular Property Prediction?* (cs.LG). Foundation-model-on-biomolecules; not on your EHR-FM thread. SKIP.
- **07-01 `arxiv-digest`** — Tan et al., *DiSTILL: A Hybrid Cloud-HPC Workflow System for Reproducible Spatial Transcriptomics Analysis* (q-bio.GN). Keyword hit `inflammatory bowel disease` because they use an IBD spatial transcriptomics dataset as the demo — but the paper is a workflow-orchestration systems paper, not an IBD-biology paper. **SKIP for IBD thread; false positive.**
- **06-30 `arxiv-digest`** — Karpinsky, Mozziconacci, Delcey, *DNA Language Models: Assessment of Pre-Training for Fine-Tuning Tasks* (q-bio.GN). Foundation models on DNA sequences; not the EHR-FM lineage you track. SKIP.
- **06-30 `arxiv-digest`** — Winter et al., *Data-Efficient Multimodal Alignment for Histopathology-based Molecular Prediction* (eess.IV). Histopathology + RNA-seq FM; not on-thread. SKIP.
- **06-30 `arxiv-digest`** — Blier-Wong, Kusmenko, *Semantic insurance pricing with large language models* (stat.AP). Keyword hit `motor` = motor third-party liability insurance. **SKIP (false hit).**
- **06-26 `arxiv-digest`** — Garg et al., *KG-TRACE: A Neuro-Symbolic Framework for Mechanistic Grounding in Antimicrobial Resistance Prediction* (cs.LG). KG-grounded AMR prediction on M. tuberculosis. Architecturally interesting (neuro-symbolic KG + neural attribution audit trail); off-thread for your biomedical KG work but a useful reference if you ever build an explainable KG-guided predictor. **METHODS-WATCH, borderline SKIP.**
- **06-25 `arxiv-digest`** — Perciballi et al., *Are Tabular Foundation Models Robust to Realistic Query Distribution Shifts in Microbiome Data?* (cs.LG). Off-thread. SKIP.
- **06-23 `arxiv-digest`** — Cabral et al., *Estimating common synaptic inputs to spinal motor neurons* (q-bio.NC). Keyword `motor` = motor neuron. SKIP.
- **07-01 Scholar** — Zhang, Bao, Zeng et al., *scalable framework for single-cell eQTL mapping … pig meat production traits* (surfaced on the *phenome wide association studies* alert). False positive — pig-agriculture context. SKIP.
- **07-01 Scholar** — Das, Mondal, *Computational Drug Repurposing Utilizing AI: A Comprehensive Review* (drug-repurposing alert). Review chapter; secondary read at best. SKIP unless you want a comprehensive-review citation.
- **07-01 Scholar** — Yang, Li, *Graph Attention Cognitive Weight Diagnosis Model Based on Knowledge Graph and Cognitive Features* (KG alert). Non-biomedical KG. SKIP per your INTERESTS ("Lower interest in non-biomedical KG infrastructure").
- **07-01 Scholar** — Mishra, Diwan, *Explainable Multimodal Systems in Electronic Health Records and Predictive Analytics* (EHR alert). Book-chapter survey. LOW; SKIP unless you want an XAI-EHR citation.
- **07-01 Scholar** — Kiran, *Applied Healthcare Science: Bridging Theory, Technology, and Public Health Practice* (Foundation-models-EHR alert). Textbook. SKIP.
- **07-01 Scholar** — Nakayama, Wu, Morley, Regatieri, Celi et al., *Embedding-Based Representations of BRSET and mBRSET for Low-Resource Ophthalmic AI* (Celi new-articles). Ophthalmic-AI benchmark. LOW; SKIP for your threads.
- **07-01 Scholar** — Facal, Pérez-Gutiérrez et al., *Dissecting the polygenic architecture of psychopathology via SVD of eight psychiatric GWAS* (Jian Yang related-research feed). Psychiatric GWAS — MEDIUM for genetic-epi if you have a psychiatric-comorbidity angle, otherwise SKIP.
- **07-01 Scholar** — Levin, *Integrating whole-body MRI-derived body composition with multi-omics data in the UK Biobank study* (UK Biobank alert). Thesis. LOW-MEDIUM — skim only if a specific proteomics-imaging integration question is live.
- **07-01 Scholar** — Nava-Ramírez, Cuevas-Velazquez et al., *Intrinsically Disordered Regions in the NLRP Family of Receptors act as regulatory hubs for inflammasome condensation and activation* (autoimmune alert). Molecular immunology; SKIP.
- **07-01 Scholar** — Drouin, Michalik et al., *Longitudinal monitoring exposes correlated temporal protein variations in the female plasma proteome* (APOL1 alert). False positive — plasma proteomics longitudinal, not APOL1-focused. SKIP for APOL1; MEDIUM-adjacent for the UKB-proteomics work if you skim.
- **07-01 Scholar** — Parker, Hartney, Nab, Amirthalingam et al., *Factors associated with severe COVID-19 in immunocompromised subgroups in England from 2020 to 2024: an OpenSAFELY cohort study* (Hernán citations). Real-world OpenSAFELY EHR cohort — MEDIUM for the EHR-linked-cohort thread if immunocompromised COVID is on-topic; SKIP if not.
- **07-01 Scholar** — Vigna, Riboni et al., *Twelve-year trends in sex and age of patients with COPD and chronic respiratory failure undergoing pulmonary rehabilitation* (Hripcsak citations). Descriptive trend paper; SKIP.
- **07-01 Scholar** — Park, *Integrative Multi-Omics Analysis of Retinoic Acid-Mediated GRN Linking Prefrontal Cortex Development to Psychiatric Disease Risk* (Pritchard citations). Thesis; SKIP.
- **07-01 Scholar** — Cipri et al., *Pediatric High-Grade Gliomas and Cancer Predisposition Syndromes: A Retrospective Study* (Karczewski citations). Off-thread cancer-genetics; SKIP.
- **07-01 Scholar** — Yan, Yang et al., *Insights from adaptive immune regulation for disease resistance breeding in livestock and poultry* (Jian Yang citations). Livestock; SKIP.
- **07-01 Scholar** — Zhao et al., *Enhancing prime editing by fusing polymerase substrate-binding proteins to reverse transcriptase* (Shendure related-research). Molecular tool development; SKIP unless you have a prime-editing sub-thread.
- **07-01 Scholar** — Ofori, Turaga, *ASO Author Reflections: Biological Limitations of ctDNA Surveillance in Colon Cancer* (Vogelstein citations). Editorial; SKIP.
- **07-01 Scholar** — Iacob et al., *The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators* (Natarajan citations); Yu, Zhou et al., *Uncovering Hidden Triggers: Backdoor Attribution in Language Models* (Zitnik related-research); Neubauer et al., *Orchestrating Black-Box Schema Converters* (Chute citations); Choudhury, Collins et al., *A scoping review of guidance on sharing trial results with patients* (Collins new-articles); Bleuze et al., *Grands modèles de langue pour prédire la santé mentale* (Szolovits citations); Khare, Nadimi et al., *Multi-Modal AI Approach in Depression Detection and Treatment: A Systematic Review* (Brandt citation); Goel, *Epigenetic Equilibrium in Chromatinopathies* (Montgomery citations); Portugal-CENTURY DNA (mendelian alert); Yang, Li graph-attention (KG); Lyons et al., *Patient Support and Real-World Evidence Generation in Rare Disease: Case Study in Hypophosphatasia* (rare-diseases alert). All either off-thread or descriptive/editorial. SKIP.
- **JAMA / JAMA Network Open online-first (multiple 07-01, 07-02)** — Football-Specific On-Pitch Concussion Assessment Protocol, Social Media Use in Children, Amnioinfusions and Survival in Fetal Kidney Failure, JAMA+ Trials: Deescalation and Discontinuation. No on-thread hits from subject lines. SKIP.

---

## Pipeline note

**Empty-day rate is high this window.** Six of 12 days (06-21, 06-22, 06-24, 06-27, 06-28, 06-29) produced trivially small digests (<300 bytes = "no relevant papers" header only). No fetch failures were logged, so this appears to be a *keyword-recall* problem, not a pipeline problem. Two suggestions worth considering:

1. **Weekend/holiday effect.** Several of the empty days are weekends (06-21 Sun, 06-22 Sat by 2026 calendar check — verify locally). arXiv submission rate drops on weekends; the digest is doing the right thing by not surfacing marginal hits.
2. **Consider a scheduled "weekly rollup" of low-recall days.** For weeks with a lot of empty days, the pipeline could produce a Sunday-evening rollup that lowers `--min-score` to 1 for the week's window as a whole and surfaces the top-N — this would catch single-keyword-hit papers that would otherwise fall through. Not urgent, but a possible enhancement.

Nothing to fix in the workflow this window. The Scholar feed is where the real signal was concentrated (items #1, #5, #6) — a good reminder that `arxiv-digest` and Scholar alerts are complementary, not redundant.

---

## Reading order suggestion

1. **Padovani-Claudio, Bastarache et al.** (item #1) — phecode threshold + GWAS validation.
2. **Mapelli et al.** (item #2) — UKB proteomics + prior-informed GGM.
3. **Naimi et al.** (item #3) — RoR causal-inference triangulation.
4. **Murali et al.** (item #4) — CF misclassified exposure causal inference.
5. **Schilder et al.** (item #5) — HPO cell-type contextualisation for rare-disease treatment.
6. **Hejblum et al.** (item #6) — probabilistic record linkage with ICD discrepancies.
7. Skim METHODS-WATCH #7-#10 in one pass; log or discard as they fit.
