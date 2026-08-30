# Research digest report — 2026-08-30

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-30 01:26Z** (~13 days since the
last research-digest report, covering the arxiv-digest cron runs for
2026-08-18 through 2026-08-28 and Scholar / PubMed alert batches on
08-22 through 08-30).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-18.md` → `2026-08-28.md`) | 08-18 → 08-28 daily crons | 08-18 (4 papers), 08-20 (3), 08-25 (1, but 2/4 categories 429'd), 08-26 (1), 08-27 (1), 08-28 (3). 08-21, 08-22, 08-23, 08-24, 08-29 dry. |
| No `arxiv-digest` email hits from GitHub | — | Same as prior report: `arxiv-digest` commits to the repo rather than emailing; the on-disk `digests/` tree is the feed. Search `from:notifications@github.com arxiv-digest newer_than:14d` returned zero threads. |
| PubMed My-NCBI alerts | 08-22 → 08-29 daily | Three saved searches (`"UK Biobank"`, `"All of Us"`, `"drug repurposing"`) fired daily. Densest single day was 08-29 (`"UK Biobank"` = 22 items). |
| Google Scholar alerts (keyword feeds, 08-30 batch, 01:26Z) | 08-30 01:26Z | 11 keyword feeds fired simultaneously (`variant interpretation`/`variant classification`, `autoimmune diseases`, `electronic health records`, `UK Biobank`, `knowledge graph`, `drug repurposing`, `rare diseases`, `All of Us research program`, `mendelian diseases`, `clonal hematopoiesis`, `Foundation models + electronic health records`). |
| Google Scholar alerts (author + citation feeds, 08-29 batch, 21:21Z) | 08-29 21:21Z | 20+ author / citation feeds: Chenjie Zeng (self × 2: new-related + citations-to), Lisa Bastarache (× 2), Joshua C Denny (citations-to), Kai Wang (× 2), Konrad Karczewski (new-related), Peter Szolovits (citations-to), Marinka Zitnik (new-related), Stephen B Montgomery (× 2), Jonathan K Pritchard (citations-to), Jian Yang (citations-to), Daniel Kastner (citations-to), George Hripcsak (citations-to), Miguel Hernán (citations-to), Vivek Natarajan (citations-to), Patrick Ryan (new-related). |

> Caveat: Scholar and PubMed emails contain title, authors, venue, and
> only a snippet of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced this window, clustering into five knots.

**Cross-biobank & PGS-in-EHR knot (4 items).** Acharya et al. *J Hum
Genet* 2026-08-28 is the anchor: heritability and genetic correlations
for ASCVD, coronary events, and cerebral events estimated in parallel
across UKB, MyCode, and AoU on **CDR v8**. Cross-biobank agreement is
imperfect and higher in UKB than MyCode/AoU — exactly the kind of
site-shift audit your *Knowledge representation in EHRs and
applications* → *Fidelity, portability, and audit of representations*
sub-thread wants. Wu et al. *Diabetes Care* 2026 (Denny + Crosslin
co-author list) uses UKB as discovery and AoU as replication for a joint
Life's Essential 8 × PGS interaction on dementia risk among people with
diabetes — a clean **PGS × modifiable-environment** paper directly on
your Nagpal/Gibson-style rising sub-thread. Xu, Zheng, Hu, Lin, Zhao,
Wang, Liu, Zhao (T Liu / H Zhao lab, Bastarache citation feed) —
**phenotype-embedding integration of EHR into PGS**: EHR-derived
phenotype embeddings materially improve PGS prediction on UKB / MVP. This
is a direct upstream method for your PheRS + PGS composite-risk work.
Zhu, Yang, Lee, Chakravarti *ResearchSquare* 2026 — **enhancer-partitioned
blood-pressure PGS** with tissue-specific interactions on CVD, replicated
on AoU CDR v8; a partitioned-PGS complement to the multi-omics-augmented
PRS sub-thread.

**Multiancestry PGS + admixture knot (2 items).** Kurniansyah et al.
*Nature Genetics* 2026 — **APOE-independent multiancestry AD PRS**
associated with cognitive decline and neuropath endpoints across diverse
populations; the definitive current answer to "does an AD PRS transfer
across ancestries once you strip APOE?" and paired with #5, an anchor
for your **cross / trans-ancestry portability** sub-thread. Molck et al.
*Genetics and Molecular Biology* 2026 (dual hit: Bastarache + Denny
citation feeds) is the admixed-Brazilian review reference for PGS in
admixed populations.

**Rare disease + variant interpretation knot (2 items).** Lin & Brandes,
**P-KNN** *Genetics in Medicine* 2026 (Denny citation feed) — joint
calibration of *multiple* pathogenicity predictors into a single
well-calibrated ACMG-usable probability. Solves the "which one predictor
do we trust" problem that has blocked PP3 stacking; near-drop-in for
InterVar / ClinGen pipelines. HIGH for your ACMG/ClinGen thread.
Uria-Regojo et al.–style but noted only as citation — pair with #8,
Guzauskas et al. *GIM* 2026 on **cost-effectiveness of BRCA1/BRCA2 VUS
reclassification and recontact** (from the Chenjie Zeng new-related
feed): the health-economics side of periodic variant reinterpretation,
directly relevant to your variant interpretation + BRCA-adjacent lines.

**CHIP / CF-modulator disease-thread knot (2 items).** Lee et al.
*Hepatology International* 2026 — **CHIP × MASLD** in a Korean biopsy
cohort, extending CHIP's downstream-disease map into metabolic liver
disease. HIGH for the CHIP/VEXAS/LOY somatic-mosaicism thread. Tillman
et al. *Pediatric Pulmonology* 2026 — a case series of **sustained
fluid-associated weight gain on CFTR modulators** (from a PK study of
CFTR-modulator adverse events): a rare-but-clinically-important
persistent-AE signal, portable to CFTR-modulator persistence work.

**Digital-twin / EHR foundation-model knot (2 items).** Lee Z et al.
arXiv 2608.26210 — **NetMoint**, a multimodal FM over UKB plasma
proteomics + brain MRI + haemodynamics for dementia-subtype-specific
1/5/10/20-year risk trajectories in 104,120 UKB participants. Directly
serves your **digital-twins from EHR data** rising sub-thread and the
**multi-omics-augmented PRS** sub-thread. Islam, Mosier & Subbian arXiv
2608.26915 — **DINIRS**, a censoring-aware digital-twin transformer
for individualized NIRS vs. IMV treatment effects using MIMIC-IV +
eICU-CRD; explicitly frames itself as "Digital Twin for Individualized
Treatment Effects" and uses a cross-fitted doubly-robust learner. HIGH
for both your **HTE / causal-forest** and **digital-twins from EHR** rising
sub-threads.

Beyond these HIGH picks, five METHODS-WATCH items are worth noting for
future toolkits: (a) Sui et al. *JACC* 2026 — **LDL-C drug-target MR ×
VTE**, a clean drug-target-MR triangulation exemplar (Pirruccello /
Natarajan / Ellinor group); (b) Gao et al. *Cardiovasc Ther* 2026 —
proteome-wide MR with cross-platform + experimental validation for
coronary atherosclerosis; (c) Vuong et al. *Cell Metabolism* 2026 —
**immunometabolic endotypes of T2D** via unsupervised clustering (SIND /
MIND …) — canonical chronic-disease-clustering paper; (d) Li D et al.
arXiv 2608.21712 (**ATHENA**) — knowledge-guided agentic neural
architecture search for AutoFormer-based EHR models — the "agentic +
EHR FM" nexus; (e) Leimenstoll & Schienle arXiv 2608.22957 — Causal
Tail Coefficient inference under heavy-tailed confounders, a portable
sensitivity method.

---

## Per-study reports

Ordered HIGH first, then METHODS-WATCH. Bucket assignment reflects
the triage rubric in `INTERESTS.md`.

---

### [HIGH] Cross-biobank comparison of ASCVD heritability and genetic correlation

- **Authors:** Acharya HB, Gidding SS, Oetjens MT, Berry ASF
- **Venue:** *Journal of Human Genetics*, 2026 Aug 28 (online ahead of print), doi:10.1038/s10038-026-01508-4, PMID 42665654
- **Sources surfacing this:** PubMed `"UK Biobank"` alert 08-29; PubMed `"All of Us"` alert 08-29; Scholar `"All of Us research program"` keyword feed 08-30; Scholar `"UK Biobank"` keyword feed 08-30 (quadruple hit).
- **What they did (from snippet):** Estimated SNP heritability and pairwise genetic correlation for atherosclerotic cardiovascular disease (ASCVD), coronary events (CE), and cerebral events across three EHR-linked biobanks in parallel: **UK Biobank**, **Geisinger MyCode**, and **All of Us Controlled Tier Dataset v8**. Heritability for ASCVD and CE was significantly higher in UKB than MyCode or AoU (adjusted P < 0.05); higher in UKB and AoU relative to MyCode for other phenotypes; AoU and UKB did not significantly differ from each other for several endpoints.
- **Why it matters for your threads:** Directly serves **Biobanks with EHR linkage** and **Genetic epidemiology**, and it is a first-class instance of your new **Knowledge representation in EHRs and applications → Fidelity, portability, and audit of representations** sub-thread. This is a cross-site heritability audit where the differences are attributable to some mix of phenotype definition drift, ascertainment, ancestry mix, and imputation quality — a template for the phecode-vs-EHR-derived-outcome portability question you are tracking.
- **What to do with it:** Read for the AoU CDR v8 phenotype definitions used for ASCVD / CE and compare with your BioVU phecode-derived definitions for the same endpoints; this is a candidate replication substrate for your own biobank-linkage work. Cite as a portability anchor next to Xu et al. #3.

---

### [HIGH] The Joint Effects of Life's Essential 8 and Genetics on Mild Cognitive Impairment and Dementia Risk in People With Diabetes: Findings From the UK Biobank and All of Us

- **Authors:** Wu X, Zu Y, Lu Y, Zhao Y, Crosslin D, Fonseca V, et al.
- **Venue:** *Diabetes Care*, 2026 (online ahead of print), doi:10.2337/dc25-3126
- **Sources surfacing this:** Scholar `"UK Biobank"` keyword feed 08-30 (top of feed).
- **What they did (from snippet):** Primary analysis in UKB (~500,000 adults aged 40–69 at enrolment 2006–2010), replicated in the All of Us Research Program. Estimates the **joint effect of Life's Essential 8 (LE8) modifiable cardiovascular-health score and genetic predisposition** on incident MCI and dementia in people with diabetes.
- **Why it matters for your threads:** Directly on the **PGS × modifiable-environment / GxE** rising sub-thread (Nagpal & Gibson *Nat Gen* 2026 style). Also **Biobanks with EHR linkage: UKB + AoU**, and the discovery-in-UKB / replicate-in-AoU design is your standing template. Diabetes + cognition also connects to the **chronic disease clustering and multimorbidity** thread.
- **What to do with it:** Read for the joint-effect estimand — is it a multiplicative interaction on the log-hazard scale, or something more explicit (RERI, joint categories, PGS × LE8 tertile grid)? The AoU replication section is worth reading closely for definition drift of LE8 components under CDR-v8 vocabulary. Consider adapting the design for a **PGS × LE8 → CKD progression in APOL1 carriers** analysis on your APOL1 thread.

---

### [HIGH] Improving polygenic risk prediction performance through integrating electronic health records by phenotype embedding

- **Authors:** Xu L, Zheng W, Hu J, Lin Y, Zhao J, Wang G, Liu T, Zhao H
- **Venue:** Preprint (ResearchGate 394599700; T Liu / H Zhao group), 2026
- **Sources surfacing this:** Scholar Denny citation feed 08-29; Scholar Bastarache citation feed 08-29 (dual hit).
- **What they did (from snippet):** Large-scale biobanks like UKB and MVP have structured (diagnosis codes) + unstructured (notes) EHR alongside genetics. This work proposes **phenotype embeddings** derived from EHRs and integrates them into PGS models to improve disease-risk prediction. The paper cites your group's *R PheWAS* toolkit.
- **Why it matters for your threads:** Direct **Genetic epidemiology → composite-risk / PGS-augmented** work, with an EHR side that fits **Knowledge representation in EHRs** (specifically concept-embedding models and how they transfer across sites). Also on your PheWAS/phecode infrastructure thread — phecode-derived phenotypes are the natural target vocabulary for these embeddings.
- **What to do with it:** Get the manuscript; the two decisions worth understanding are (a) how phecodes / OMOP concepts get embedded (is this a supervised embedding trained on the outcome, or an unsupervised concept-embedding like cui2vec / SapBERT / MedTok?) and (b) whether the PGS + phenotype-embedding integration is early fusion (concatenation) or late fusion (stacking / ensemble). This is a direct upstream method for your own PheRS + PGS composite-risk analyses; benchmark it against your existing PheRS × PGS models on BioVU.

---

### [HIGH] Partitioned blood pressure polygenic risk reveals differential genetic effects of tissue-specific enhancers and their interactions on cardiovascular disease

- **Authors:** Zhu X, Yang Y, Lee D, Chakravarti A
- **Venue:** ResearchSquare rs-10406003, 2026 (preprint)
- **Sources surfacing this:** Scholar `"All of Us research program"` keyword feed 08-30.
- **What they did (from snippet):** Partitions blood-pressure PGS by **tissue-specific enhancer annotation** and evaluates the differential genetic effects and interactions on CVD. Uses individual-level All of Us Researcher Workbench data.
- **Why it matters for your threads:** Serves **Genetic epidemiology → composite-risk / PGS-tails** by moving the PGS from a scalar to a *partitioned* score keyed to tissue biology — a variant of the tails-and-residuals taxonomy where the residual is defined at the level of tissue-of-action rather than individual-level misalignment. Complements the Baya / Souaiaia / Vazquez trio in the INTERESTS anchor. Also **Biobanks with EHR linkage: All of Us** on the CDR-v8 substrate.
- **What to do with it:** Read for whether the partition uses ROADMAP / ENCODE tissue enhancers and whether the tissue-specific interactions replicate across ancestries in AoU. If yes, this is a template for **CFTR / APOL1 tissue-partitioned rare-variant burden × tissue-PGS** interactions in your disease threads. Watch for the peer-reviewed venue.

---

### [HIGH] A multiancestry polygenic risk score for Alzheimer's disease is associated with cognitive decline and neuropathological hallmarks in diverse populations

- **Authors:** Kurniansyah N, Tasaki S, Rehman H, Zhu C, Farrell J, et al.
- **Venue:** *Nature Genetics*, 2026, doi:10.1038/s41588-026-02722-8
- **Sources surfacing this:** Scholar `"All of Us research program"` keyword feed 08-30.
- **What they did (from snippet):** Existing AD PRSs transfer inconsistently across ancestries. This work builds an **APOE-independent multiancestry AD PRS** from cross-ancestry GWAS summary statistics and validates it against cognitive-decline and neuropathological endpoints in ancestrally diverse cohorts.
- **Why it matters for your threads:** Direct **Genetic epidemiology → cross/trans-ancestry PGS portability** anchor, and a benchmark to compare against for any AD-PRS work in AoU or BioVU. APOE-independent framing sidesteps the usual APOE-swamps-everything problem and gives a cleaner substrate for **PGS residuals / polygenic-deviation designs** on the non-APOE portion of the AD architecture.
- **What to do with it:** Read Methods for how APOE-independence was operationalised (is the APOE region masked entirely, or a conditional GWAS?). Neuropath endpoints (CERAD, Braak, Thal) are a stronger validation surface than clinical AD — worth checking replication in ROSMAP / ADSP against AoU's clinical-AD-only substrate.

---

### [HIGH] P-KNN: joint calibration of multiple pathogenicity prediction tools streamlines variant classification

- **Authors:** Lin PY, Brandes N
- **Venue:** *Genetics in Medicine*, 2026, doi.org/10.1016/j.gim.2026.101010 (S1098-3600(26)01010-5)
- **Sources surfacing this:** Scholar Denny citation feed 08-29.
- **What they did (from snippet):** ACMG clinical guidelines for interpreting Mendelian-disease variants require **converting pathogenicity-tool outputs into well-calibrated probabilities**. The existing calibration approach requires pre-committing to one tool. **Pathogenicity K-Nearest Neighbors (P-KNN)** jointly calibrates *multiple* tools with complementary strengths, so a clinical lab can combine them without over-counting.
- **Why it matters for your threads:** Directly on the **Variant interpretation (ACMG / ClinGen)** thread. The PP3 evidence code and its calibrated-thresholds recommendation (Pejaver et al. *AJHG* 2022) implicitly force a single-tool commitment; P-KNN is the natural methods response and belongs alongside your InterVar / AnFiSA-style tooling.
- **What to do with it:** Read. If it's drop-in for your VCEP variant-curation pipelines, prototype on BRCA1/BRCA2 VUSs where multiple predictors disagree. Pair the read with Guzauskas et al. #8 (BRCA VUS reclassification cost-effectiveness) — one paper on the *method*, one on the *policy*.

---

### [HIGH] Cost-effectiveness of BRCA1/BRCA2 Variant Reclassification and Recontact for Hereditary Breast and Ovarian Cancer in the United States

- **Authors:** Guzauskas GF, Berger SM, O'Connor R, Kim S, et al.
- **Venue:** *Genetics in Medicine*, 2026 (S1098-3600(26)01015-4)
- **Sources surfacing this:** Scholar Chenjie Zeng new-related feed 08-29.
- **What they did (from snippet):** Cost-effectiveness analysis of **reinterpreting BRCA1/BRCA2 VUSs and recontacting patients** when reclassified. Evaluates the impact of reclassification on clinical management, health outcomes, and healthcare costs; asks about optimal timing of reinterpretation.
- **Why it matters for your threads:** Serves **Variant interpretation (ACMG / ClinGen)** on the *policy / implementation* axis, complementing the methods axis P-KNN sits on. Directly relevant to your existing hereditary-breast-cancer work and citation-worthy for any recommendation about VUS-reinterpretation cadence in EHR-linked biobank returns.
- **What to do with it:** Read for the model assumptions on VUS reclassification rate over time (does it use a Bayesian rate that decays as ClinVar submissions saturate?) and on the age-window over which reinterpretation stays cost-effective. Directly informs any BioVU / AoU BRCA return-of-results protocol.

---

### [HIGH] Clonal hematopoiesis of indeterminate potential and metabolic dysfunction-associated steatotic liver disease: Korean biopsy cohort

- **Authors:** Lee YK, Sim H, Joo SK, Jang H, Lee DH, Park JH, et al.
- **Venue:** *Hepatology International*, 2026, PMID 42658470
- **Sources surfacing this:** Scholar `intitle:"clonal hematopoiesis"` keyword feed 08-30.
- **What they did (from snippet):** Investigated the association of **CHIP with metabolic dysfunction-associated steatotic liver disease (MASLD)** in a Korean biopsy-anchored cohort.
- **Why it matters for your threads:** Directly on the **CHIP / VEXAS / LOY** somatic-mosaicism thread. CHIP's downstream-disease map has been dominated by cardiovascular and hematologic outcomes (Loh *Nature* 2018, Kessler *Nature* 2022 lineage). MASLD is a live extension. Biopsy anchoring is the gold-standard-adjacent design — most CHIP × liver work has relied on FIB-4 or ICD codes.
- **What to do with it:** Get the methods to see which CHIP-defining panel + VAF cutoff (typically 2%) was used and whether the association survives adjustment for age, sex, and metabolic covariates. Extending this to LOY × MASLD in UKB would be a natural next analysis on your rising **male-specific LOY analogue of CHIP** sub-thread.

---

### [HIGH] Case Series of Sustained Fluid-Associated Weight Gain Following Cystic Fibrosis Transmembrane Conductance Regulator (CFTR) Modulator Therapy

- **Authors:** Tillman EM, Lazutina A, Robinson RC, Colwell A, et al.
- **Venue:** *Pediatric Pulmonology*, 2026, doi:10.1002/ppul.71813
- **Sources surfacing this:** Scholar Chenjie Zeng new-related feed 08-29.
- **What they did (from snippet):** Case series drawn from screening for a PK study of **CFTR-modulator adverse events**, describing sustained fluid-associated weight gain following CFTR modulator (Trikafta family) therapy.
- **Why it matters for your threads:** Directly on the **Cystic fibrosis / CFTR** specific-disease thread — this is a rare-but-clinically-important persistent-AE signal, portable to the **CFTR-modulator persistence** sub-thread under pharmacoepidemiology (in what fraction does this AE drive discontinuation, and does that fraction move under PGx modifiers of modulator PK?).
- **What to do with it:** Read for whether the AE reverses on drug holiday or dose reduction, and whether it is enriched in a specific *CFTR* genotype. Consider a follow-on analysis in AoU or BioVU: incident weight-gain phecodes after modulator initiation in CF patients, HTE by baseline BMI and by CYP3A4 metabolizer status.

---

### [HIGH] Predicting Early Functional Decline from Longitudinal Laboratory and Vital Sign Trajectories: A Large-Scale Study Using the All of Us Research Program

- **Authors:** Kudamala R, Kuruvikkattil AV, Pulavarthy LP, et al.
- **Venue:** arXiv 2608.21589, 2026
- **Sources surfacing this:** Scholar `"All of Us research program"` keyword feed 08-30 (top of feed).
- **What they did (from snippet):** Functional decline in older adults is usually recognized only after falls or gait impairment. This work tests whether **temporal trajectories of routine biomarkers** (labs + vitals) already sitting in the AoU record can predict early functional decline, moving detection into a prevention window.
- **Why it matters for your threads:** Serves **Biobanks with EHR linkage: All of Us**, **Machine learning for precision health** (tied to a clinical decision — who to screen for falls), and the **temporal trajectory** side of **Knowledge representation in EHRs → Structural and temporal representation of the patient timeline**. Functional-decline endpoints in AoU are a fresh outcome surface that has not been beaten to death yet.
- **What to do with it:** Read Methods for how they handled AoU's characteristic sparsity of routine labs (many participants only contribute survey + EHR-linkage-quality events, not densely sampled labs). This is a candidate methodology to port to **incident CKD prediction from creatinine trajectories in APOL1 carriers**.

---

### [HIGH] Multimodal risk trajectories reveal heterogeneous paths to dementia

- **Authors:** Lee Z, Li H, Liu T, Zhang S, Wang B, Fan J, Zhang Y, Wang Z, Bai L
- **Venue:** arXiv 2608.26210v1, submitted 2026-08-26
- **Sources surfacing this:** Local `arxiv-digest` `digests/2026-08-28.md` (keyword hits: `uk biobank`, `biobank`; score 2).
- **What they did (from abstract):** Built **NetMoint**, a multimodal framework integrating **partially observed plasma proteomics + structural MRI + cerebral haemodynamics** to predict individualized 1/5/10/20-year risks of AD, VD, and FTD in 104,120 UKB participants free of dementia at baseline. AUCs: 0.937 / 0.930 / 0.932. Biological determinants of the prediction shift with horizon (structural brain vulnerability short-term → circulating molecular signatures long-term). Multi-horizon risk profiling identifies distinct temporal trajectories of dementia susceptibility — e.g., 0.7% of eventual AD cases follow a persistently very-high-risk trajectory (reaching 53.5% predicted risk at 20 years); 8.3% of eventual FTD cases follow an increasing very-high-risk trajectory (reaching 67.2%). Distinct molecular signatures characterize the high-risk groups (lower TGFB1 for AD; higher NDRG1 for FTD). Independent ADNI-to-UKB analysis: AUC 0.741 at 20 years after feature harmonization to 138 shared features.
- **Why it matters for your threads:** Serves the **EHR foundation models → digital-twins from EHR data** rising sub-thread (individualized trajectory prediction is exactly the Zhang / Ideker / Oermann *Cell* 2026 framing endpoint); **Multi-omics-augmented PRS** rising sub-thread (proteomics + imaging + haemodynamics as the multi-omics stack); and **Chronic disease clustering / trajectory clustering** on the trajectory side. The horizon-shifting biology (structure → molecules over time) is a substantive finding beyond ML-benchmarking.
- **What to do with it:** Read the trajectory-clustering section carefully — the small-but-high-risk trajectory subgroups are the phenotype your PheRS composite-risk work is aiming for on Mendelian carriers. The 138-feature harmonization for ADNI-to-UKB is a portable template for **UKB-to-AoU biomarker harmonization**. Watch for a peer-reviewed venue.

---

### [HIGH] DINIRS: Digital Twin for Individualized Treatment Effects of Non-Invasive Respiratory Support Strategies

- **Authors:** Islam MF, Mosier J, Subbian V
- **Venue:** arXiv 2608.26915v1, submitted 2026-08-27
- **Sources surfacing this:** Local `arxiv-digest` `digests/2026-08-28.md` (keyword hit: `heterogeneous treatment effects`; score 1).
- **What they did (from abstract):** Choice between NIRS and IMV in acute respiratory failure is time-sensitive with heterogeneous effects. **DINIRS** is a censoring-aware digital-twin framework for **individualized treatment effects on 28-day ventilator-free days (VFD-28)**, trained on 23 baseline clinical variables from the first 24 ICU hours in **5,336 MIMIC-IV patients** and externally validated in **2,540 eICU-CRD patients**. Uses a transformer encoder with a survival attention gate to decompose VFD-28 into survival probability + conditional ventilation duration; a **cross-fitted, doubly-robust learner** estimates ITEs. The DINIRS policy achieves +2.07 VFD per patient vs observed practice. Predicted NIRS benefit was concentrated in patients with less organ dysfunction (88.4% vs 49.0%). External validation reproduced the pattern without retraining. Mechanism: benefit stems from shorter ventilation among survivors, not reduced mortality — avoiding intubation-associated complications is the primary route.
- **Why it matters for your threads:** Sits at the intersection of **EHR foundation models → digital twins**, **Causal inference & pharmacoepi → HTE / meta-learners / doubly-robust methods**, and **Machine learning for precision health** (tied to a real ICU decision). The doubly-robust cross-fit design is exactly the toolkit your rising **agentic / human-in-the-loop OCI** sub-thread should be using. The MIMIC-IV → eICU external validation is a design pattern worth propagating.
- **What to do with it:** Read Methods for the survival-attention-gate architecture — it is a specific answer to the "how do you fold survival censoring into a transformer-derived HTE estimator" question. Consider adapting the framework to a **CFTR-modulator initiation vs delay HTE analysis** on AoU with the same doubly-robust wrapper. Prospective validation is a stated next step — worth watching for a peer-reviewed venue.

---

### [METHODS-WATCH] Genetically Mediated Differences in LDL Cholesterol and Risk of Venous Thromboembolism

- **Authors:** Sui Y, Kany S, Khurshid S, Supriami K, Rämö JT, Jurgens SJ, Enzan N, Choi SH, Yu Z, Li L, Truong B, Chen X, Kim MS, Shim I, Twerenbold R, Pirruccello JP, Natarajan P, Ellinor PT, Fahed AC
- **Venue:** *Journal of the American College of Cardiology*, 2026 Aug 4 (online ahead of print), doi:10.1016/j.jacc.2026.06.026, PMID 42663354
- **Sources surfacing this:** PubMed `"UK Biobank"` and `"All of Us"` alerts 08-29.
- **Why it's METHODS-WATCH:** Drug-target / instrument-lipid **Mendelian randomisation triangulated with cohort risk of VTE** in linked biobanks — Ellinor / Natarajan / Pirruccello / Fahed authorship signals a well-designed MR-RCT triangulation. Directly parallel to the **drug-target MR triangulated with observational cohort estimates** rising sub-thread (Saxby metformin × AAA lineage), though not on your target-disease list.
- **What to do with it:** Skim Methods for the MR instrument selection (LDLR, PCSK9, HMGCR panels?) and the sensitivity analyses (MR-PRESSO, MR-Egger, MR-cML / MR-ALasso). If they use MR-ALasso, cite alongside Saxby et al. as instrument-lipid-MR method exemplars.

---

### [METHODS-WATCH] Uncovering Potential Druggable Targets in Coronary Atherosclerosis: A Proteome-Wide Mendelian Randomization Study With Cross-Platform and Experimental Validation

- **Authors:** Gao D, Lin H, Wang S, Wang Y, Yang H, Wang Z
- **Venue:** *Cardiovascular Therapeutics*, 2026;2026(1):e7359278, PMID 42666106
- **Sources surfacing this:** PubMed `"UK Biobank"` alert 08-29.
- **Why it's METHODS-WATCH:** **Proteome-wide MR** for coronary atherosclerosis with cross-platform (Olink × SomaScan?) and experimental validation. Portable methods template for **drug-target MR + multi-omics-augmented risk** work, particularly for cardiometabolic disease on your composite-risk axis.
- **What to do with it:** Skim for how they reconciled platform-specific pQTL panels and whether the "experimental validation" is CRISPRi / MPRA / cell-based. Template-worthy for future proteome-wide MR analyses in UKB Olink.

---

### [METHODS-WATCH] Identifying novel druggable targets and repurposable drugs for premature ovarian insufficiency by integrated multiomics and causal inference analysis

- **Authors:** Liu C, Wang R, Liu X, Li Y, Ren L, Zhao Z, Fan Z, Xiao J
- **Venue:** *Geroscience*, 2026 Aug 28 (online ahead of print), doi:10.1007/s11357-026-02491-6, PMID 42663799
- **Sources surfacing this:** PubMed `"UK Biobank"` and `"drug repurposing"` alerts 08-29.
- **Why it's METHODS-WATCH:** Integrated multi-omics + causal inference for **drug repurposing**. Not on your target-disease list, but the pipeline design is a portable template for the **causal-inference framings of off-label use** angle under your Drug repurposing thread.
- **What to do with it:** Skim Methods to see whether the "causal inference" is MR-based, TTE-based, or something else. If MR-based, note as a template for **MR-driven repurposing** in your rare-disease → HPO-based repurposing sub-thread.

---

### [METHODS-WATCH] Immunometabolic endotypes define distinct clinical trajectories in type 2 diabetes

- **Authors:** Vuong BT, Delépine CM, Ratter-Rieck JM, Rinaldi E, et al.
- **Venue:** *Cell Metabolism*, 2026 (S1550-4131(26)00325-6)
- **Sources surfacing this:** Scholar Denny citation feed 08-29.
- **Why it's METHODS-WATCH:** **Unsupervised clustering** on routine blood-immune-cell counts across >1,500 newly-diagnosed T2D patients from three European cohorts identifies four reproducible endotypes (**SIND** severe inflammatory, **MIND** mild inflammatory, and two others). Trajectory-linked. Canonical **chronic disease clustering / multimorbidity** exemplar; also a validation-across-cohort clustering pattern that is unusual — most clustering papers do not reproduce across cohorts.
- **What to do with it:** Read to understand the clustering objective (k-means vs. LCA vs. GMM) and how endotype-stability was tested across the three cohorts. Portable template for **HTE + endotype** analyses on your **cardiometabolic multimorbidity** and **autoimmune multimorbidity** sub-threads.

---

### [METHODS-WATCH] ATHENA: Knowledge-guided agentic neural architecture search for AutoFormer-based electronic health record modeling

- **Authors:** Li D, Xu Q, Li L, Wang T, Liang M, Liu M
- **Venue:** arXiv 2608.21712, 2026
- **Sources surfacing this:** Scholar `"electronic health records"` keyword feed 08-30; Scholar `Foundation models + "electronic health records"` keyword feed 08-30.
- **Why it's METHODS-WATCH:** **Agentic NAS for EHR transformers** — the exact "agents + EHR FM" nexus that ties your **EHR foundation models** thread to the **agentic / human-in-the-loop OCI** sub-thread. AutoFormer-based; knowledge-guided.
- **What to do with it:** Skim for the "knowledge" component — is it OMOP-vocabulary-guided, or a phecode hierarchy, or something else? If it uses phecode/OMOP structure as a NAS prior, this is directly relevant.

---

### [METHODS-WATCH] SynEHR: Joint Modeling Inter-visit Temporal Evolution and Intra-visit Clinical Structure for Longitudinal EHR Synthesis

- **Authors:** Li X, Jiang L, Xu R, Yu D, He Z, Wang G
- **Venue:** arXiv 2608.21673, 2026
- **Sources surfacing this:** Scholar `Foundation models + "electronic health records"` keyword feed 08-30.
- **Why it's METHODS-WATCH:** **Synthetic longitudinal EHR generation** that jointly models inter-visit temporal evolution and intra-visit structure. A candidate benchmark generator for **pretraining-contamination audits for foundation-model benchmarks** — your Ali arXiv 2607.20572 (scContam) / MIA-scFM sub-thread. Also a candidate baseline for privacy-preserving EHR pretraining sets.
- **What to do with it:** Skim to see how visit sequences (irregular time, admissions as containers, medication-exposure windows) are encoded — the same representation choices from the **Knowledge representation in EHRs → Structural and temporal representation** sub-topic.

---

### [METHODS-WATCH] Identification and Inference for Causal Effects in Extremes under General Conditions

- **Authors:** Leimenstoll L, Schienle M
- **Venue:** arXiv 2608.22957v1, submitted 2026-08-24
- **Sources surfacing this:** Local `arxiv-digest` `digests/2026-08-25.md` (keyword hit: `causal inference`; score 1).
- **Why it's METHODS-WATCH:** Causal identification of **effects in extremes** with heavy-tailed confounders, via the Causal Tail Coefficient (CTC) in a linear structural causal model. Light-tailed confounders are asymptotically negligible; sufficiently heavy-tailed confounders can induce extremal dependence patterns indistinguishable from direct causal effects — a subtle new source of confounding-by-design. Estimation + inference + tests for direction and heavy-tailed confounding.
- **What to do with it:** Skim to see whether the sensitivity-analysis machinery is portable to **rare-outcome EHR analyses** (e.g., anaphylaxis, VEXAS incidence). Even if not directly applicable, worth reading as a portable **sensitivity method for tail-event outcomes**.

---

### [METHODS-WATCH] A multi-dimensional framework for predicting taxane-induced peripheral neuropathy in Black women with breast cancer: findings from ECOG-ACRIN EAZ171

- **Authors:** Schneider BP, Jiang G, Zhao F, Sparano JA, Garcia SF, et al.
- **Venue:** *npj Breast Cancer*, 2026, s41523-026-01009-9
- **Sources surfacing this:** Scholar Chenjie Zeng new-related feed 08-29.
- **Why it's METHODS-WATCH:** ECOG-ACRIN EAZ171 previously found docetaxel Q3W had less TIPN than weekly paclitaxel in Black patients. This paper builds a **multi-dimensional prediction framework** for TIPN — a canonical **PGx-modifier-of-medication-toxicity** setup adjacent to your **pharmacogenomic modifiers of medication persistence** sub-thread (Cohen et al. *Pharmaceuticals* 2026 lineage).
- **What to do with it:** Read to see whether *CYP2C8* / *CYP3A4* / *SLCO1B3* metabolizer status is one of the dimensions and whether the prediction is prospectively actionable (dose reduction, alternative regimen). Portable template for **CFTR-modulator toxicity prediction in CF patients**.

---

## SKIP (surfaced but off-thread)

Not itemized in detail — the following came up in the feeds but do not
warrant per-study reports for your active threads:

- *Metabolic, inflammatory, and lipoprotein(a)-related risk profiling
  for incident ASCVD* — biomarker profiling, not on your composite-risk
  or PheWAS thread axis.
- *Association of serum uric acid, gout with incident sepsis* — UKB
  epi, not on tracked disease threads.
- *Mediterranean vs DASH Diets and Heart Failure Risk: A UK Biobank
  Study* — dietary epi, not on tracked threads.
- *Retina-specific foundation model for ocular and systemic disease
  detection* — retinal FM, not on your EHR-FM axis.
- *Plasma proteomic signatures associated with ulcerative colitis risk
  in overweight/obesity individuals: a UK Biobank study* — adjacent to
  IBD thread but proteomics-first, not a phenotyping/pharmacoepi
  contribution.
- *Machine Learning-derived dietary pattern for aging* — biomarker /
  dietary-pattern discovery.
- *Cell-type-specific eQTLs underlie the genetic architecture of
  complex traits* (Chen M et al., *Nature* 2026, from Montgomery /
  Pritchard feeds) — landmark eQTL paper, worth noting for citation
  but not directly on your active threads. Consider adding to reading
  list.
- *Machine learning-driven drug repurposing and computational
  validation for Nipah virus*, *Multitargeted drug strategies for
  Alzheimer's and Parkinson's diseases*, *Dihydroartemisinin inhibits
  Epstein-Barr virus reactivation*, RExPO26 conference abstracts, other
  computational drug-repurposing papers — off-thread for the
  EHR-based / KG-explainable / MR-triangulated repurposing angles you
  prioritize.
- *Digital Phenotyping in Health Research: Scoping Review* — scoping
  review; not new methodology.
- *Third Patient With Biallelic Variants in SMAD6* — variant curation
  case report, not on your ACMG/ClinGen thread axis.
- *RIBOSPAN: Long-Context RNA Foundation Model*, *Frozen Hematology
  Foundation Models under Acquisition Shift* — foundation-model papers
  outside the EHR-FM lane.
- *Learning Interpretable Tumor Microenvironment Representations by
  Fitting Pan-Cancer Cell State-Niche Correlation* — spatial-omics FM,
  not clinical.

---

## What to do next

1. **Read first (this week):** Acharya *J Hum Genet* (cross-biobank
   ASCVD heritability), Wu *Diabetes Care* (LE8 × PGS on dementia in
   diabetes UKB→AoU), Lin & Brandes P-KNN *GIM* (ACMG multi-tool
   calibration), Lee Z NetMoint arXiv (multimodal dementia trajectory
   FM on UKB), Islam DINIRS arXiv (digital-twin HTE on MIMIC-IV).
2. **Read soon (next 2 weeks):** Kurniansyah *Nat Gen* (multiancestry
   AD PRS), Xu et al. phenotype-embedding-augmented PGS, Guzauskas
   *GIM* BRCA VUS reclassification cost-effectiveness, Lee Y CHIP ×
   MASLD, Tillman CFTR-modulator sustained weight gain.
3. **Watch for peer-reviewed venue:** NetMoint (Lee Z), DINIRS (Islam),
   Zhu tissue-partitioned BP-PGS, Xu phenotype-embedding-augmented PGS.
4. **Portable-methods candidates to prototype:** DINIRS
   doubly-robust-transformer HTE stack (port to CFTR modulator HTE);
   NetMoint horizon-shifting molecular-signature framework (port to
   CKD trajectory in APOL1 carriers); Xu et al. phenotype-embedding
   PGS (port to your PheRS + PGS composite-risk work).
