# Research digest report — 2026-07-31

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS-LOY/IBD disease
threads, EHR foundation models, KGs/ontologies, drug repurposing, rare
disease, ML for precision health, multimorbidity).

Window: **2026-07-30 12:35Z → 2026-07-31 12:35Z** (~24 h since
`reports/2026-07-30-research-digest.md`). This is a **single-day
follow-on** to the multi-day 07-30 catch-up — shorter HIGH list, and
mostly built on the NCBI batch that fired 07-30 15:20Z plus the
overnight bioRxiv/medRxiv collection alerts.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-07-31.md`) | 07-31 10:30Z cron | 1 relevant paper (2 previously seen suppressed): Ran et al. DR-FRL (causal-inference methods, longitudinal EHR-like functional histories). |
| NCBI "My NCBI What's New" — AoU / UKB / drug repurposing | 07-30 15:20Z batch | Three feeds fired together: AoU 6/6 shown, UKB 19/19 shown, drug repurposing 10/14 shown. Dense AoU batch this time — several Denny-lineage and Motsinger-Reif-lineage papers. |
| Google Scholar alerts (author + keyword feeds) | 07-30 12:35Z → 07-31 12:35Z | **No new Scholar-alert cluster in the window** — the last big fan-out was the 07-27 14:34Z batch already covered in the 07-30 report. |
| bioRxiv / medRxiv Subject Collection Alerts | 07-31 00:01Z (bioRxiv) + 07-31 00:05Z (medRxiv) | Aggregate overnight feeds. Standard note: papers get surfaced upstream via Scholar / NCBI; individual triage below only where a paper doesn't already appear in another feed. |
| JAMA / JAMA Network Open "Online First" | 07-30 17:47Z / 18:42Z / 19:04Z | One SGLT2i-adjacent trial (dapagliflozin AKI post-CT surgery). |

> Caveat: NCBI / Scholar emails contain title, authors, venue, and PMID
> only (no abstract). The reports below contextualize that metadata
> against your research threads; nothing here reflects full-text
> reading. The single `arxiv-digest` entry includes the full abstract
> because the pipeline captures it.

---

## Executive summary (HIGH-priority studies, ranked)

Eleven HIGH items surfaced in this 24 h window, clustering into four
knots. The single densest is the **AoU / Denny-lineage** cluster
driven by the 07-30 15:20Z NCBI batch — five studies at once.

**Author-of-record note.** The Bujnis et al. multi-ancestry
Hashimoto's thyroiditis GWAS (Nat Genet, item #1) lists **Zeng C** in
the author block — this is your own paper being surfaced via the AoU
NCBI feed the day it went online-ahead. Flagging first so it doesn't
get triaged as a generic feed hit.

**AoU / Denny-lineage cluster (5 items).** Bujnis et al. Nat Genet —
multi-ancestry GWAS of Hashimoto's thyroiditis (your own paper +
Denny). Ahn et al. Res Sq — shared trans-ancestry architecture of
HLA-mediated disease risk in AoU (Denny + Motsinger-Reif). Gu et al.
medRxiv — GWAS + deep-learning functional annotation of opioid use
disorder across three ancestries in AoU. Young et al. J Clin Lipidol —
PREVENT-ASCVD vs pooled cohort equations on statin eligibility in AoU
(risk-score-swap policy question). Kore, Atkinson et al. medRxiv —
local-ancestry-informed rare-variant burden testing improving gene
discovery in admixed populations (the method arm of the trans-ancestry
theme).

**Pharmacoepi + genetic triangulation (2 items).** Carter, Kar, Burgess
et al. medRxiv — statin use + genetically-predicted HMG-CoA reductase
inhibition in relation to clonal hematopoiesis (the CHIP thread meets
drug-target MR in a natural way). Abegaz & Frietze — ML for predicting
glycemic-control and weight-loss outcomes in GLP-1 RA users (GLP-1
thread + ML-for-precision-health, first-visible AoU-adjacent AI/ML
paper this week).

**PheWAS / composite-phenotype methodology (2 items).** Albiñana,
Richmond, Wang et al. medRxiv — population-scale molecular
reconstruction of human circadian phase from blood biomarkers
(FinnGen + Wray group). Direct continuation of the 07-30 Circadian
Imbalance Index HIGH thread — same three-legged construct-phenotype +
biobank + biomarker template. Liu et al. Int J Nurs Stud —
accelerometer step-count PheWAS in ~60,000 UKB adults (behavioral
exposure PheWAS at scale).

**Causal inference & interpretable-ML methods (2 items).** Ran, Shen,
Guan arXiv 2607.28567 — DR-FRL: doubly-robust functional
representation learning for longitudinal causal inference with
irregular histories (the estimator directly targets EHR-shaped data —
labs, physiologic signals, sensor streams at unequal times). Upmeier
zu Belzen et al. medRxiv — interpretable omnigenic neural network
architecture for the human genome (Eils/Theis lineage; the omnigenic
model rendered as an NN with interpretability).

---

## HIGH — full write-ups

### 1. Bujnis, Sterenborg, Li, Åsvold, Brčić, Boraska Perica, Babbar, Denny JC, Fritsche LG, Kanai M, Konrade I, Leese G, Marouli E, Metspalu A, Moksnes MR, Mukherjee B, Okada Y, Palmer CNA, Papadopoulou A, Peculis R, Rovite V, Sauer PJ, Soto-Pedre E, Srinivasan S, Steinbrenner I, Teder-Laving M, Wang B, Weihs A, **Zeng C**, Zhou J; Biobank Japan Project; Song X, Jorde LB, Medici M, Teumer A. *Multi-ancestry genome-wide association analyses provide insights into the genetic basis of Hashimoto's thyroiditis* — **Nat Genet 2026 Jul 29 (online ahead of print)**, doi:10.1038/s41588-026-02704-w. PMID 42527560.

**Feed:** NCBI PubMed "What's new for 'All of Us'" (07-30 15:20Z).

**Why HIGH — flagged for a special reason.** This is a paper you are
listed as a co-author on. The AoU NCBI feed picked it up on the same
day it went online-ahead-of-print at Nat Genet. Flag it at the top of
the digest because:
- Confirm the author-block ordering / affiliation string reflects what
  you agreed to. Nat Genet OAP versions have historically been the
  frozen record for author-order questions — check now, not after
  print.
- Confirm the data-availability + code-availability statements match
  what your consortium agreed on. Multi-ancestry GWAS with a Biobank
  Japan arm has structured DAS requirements; check that AoU-arm
  handling is what you expected.
- Note the DOI (10.1038/s41588-026-02704-w) so you have it for
  citing internally.
- Push a version to bioRxiv / consortium sites per your usual practice,
  and update your Google Scholar profile so the citation lands
  cleanly.

**What it is (from the alert):** Multi-ancestry GWAS meta-analysis of
Hashimoto's thyroiditis, spanning European + East-Asian (Biobank Japan)
+ likely additional ancestry arms. Author list includes Denny (AoU
program lineage), Fritsche (Michigan Genomics Initiative lineage),
Kanai (BBJ), Okada (BBJ), Palmer (Generation Scotland), Metspalu
(EstBB), and Mukherjee (statistical genetics) — the standard
biobank-consortium roster.

**Where it links to your work.** Directly. Also relevant to the
autoimmune-diseases thread (Hashimoto's is the archetypal autoimmune
endocrinopathy) and could be a template for how to structure future
multi-ancestry AoU-arm contributions to consortium GWAS.

---

### 2. Ahn K, House JS, Burkholder A, Tran TC, Breeyear JH, Justice CM, Durney J, Jones AM, Reyes PS, Bailey MH, Davis MF, Vicenti AT, Karnes JH, Hollenbach JA, Fargo DC, Ginsburg GS, Woychik RP, Denny JC, Motsinger-Reif AA. *Shared trans-ancestry architecture of HLA-mediated disease risk in the All of Us Research Program* — **Res Sq [Preprint] 2026 Jul 14**, doi:10.21203/rs.3.rs-10157403/v1. PMID 42523503. Free PMC article.

**Feed:** NCBI PubMed "What's new for 'All of Us'" (07-30 15:20Z).

**Why HIGH.** Serves three threads:
1. **AoU-native methods work** — HLA imputation and disease-association
   testing on the AoU cohort is a foundational reference for anyone
   doing autoimmune-adjacent PheWAS on AoU.
2. **Trans-ancestry portability** — HLA is *the* place where
   trans-ancestry issues bite hardest (extreme LD, different tag SNPs,
   ancestry-specific alleles). A shared-architecture claim is a strong
   statement worth reading carefully.
3. **PheWAS / disease-risk cataloging** — the Denny + Motsinger-Reif
   axis is exactly the PheWAS infrastructure your interests file
   tracks. This looks like a phecode-level or phenotype-domain scan.

**Actionable follow-on.** Read for:
- **Which HLA imputation reference panel** (T1DGC + Michigan
  imputation, or the newer AoU-native HLA panel? The choice bounds
  trans-ancestry claims.)
- **Ancestry stratification** — EUR / AFR / AMR / EAS / SAS breakouts,
  and what the *shared* architecture claim rests on statistically
  (LDSC-based cross-ancestry rg, meta-analysis P-value convergence,
  fine-mapping consistency?).
- **Phenotype list** — which HLA-associated diseases were tested
  (T1D, RA, celiac, MS, IBD, SLE, thyroid autoimmunity are the usual
  suspects), and did they include any typically-underpowered ones like
  Behçet's or narcolepsy?

**Where it links to your work.** Reference for HLA-arm methodology on
any AoU project. Also feeds the autoimmune-diseases + IBD threads.

---

### 3. Gu S, Petrovitch D, Hall OT, Lambert JW, Kember RL, Nahid NA, Ma Q, Sprague JE, McDonough CW, Johnson JA. *Genome-Wide Association Studies and Deep-Learning Functional Annotation of Opioid Use Disorder across Three Ancestries in the All of Us Research Program* — **medRxiv [Preprint] 2026 Jul 17**, doi:10.64898/2026.07.15.26358096. PMID 42528495. Free PMC article.

**Feed:** NCBI PubMed "What's new for 'All of Us'" (07-30 15:20Z).

**Why HIGH.** Three overlapping angles:
- **AoU multi-ancestry GWAS** — three-ancestry OUD GWAS in AoU is a
  meaningful sample-size contribution to a small existing literature
  (MVP is the other main OUD-genetics cohort; AoU adds a very
  different case-ascertainment profile).
- **Phenotyping question** — OUD case definition in AoU is non-trivial
  (ICD-derived, EHR-mention-derived, self-reported, or medication-
  based). The phenotyping choice will drive interpretability of the
  hits.
- **Deep-learning functional annotation** — Kember + Johnson lineage on
  the functional side; this is the "GWAS + DL prior" template that's
  becoming standard for post-GWAS follow-up.

**Actionable follow-on.** Read for:
- **OUD case definition** (phecode-based? DSM-mapped? ICD 10-based? A
  hierarchy?). This is exactly the phenotyping question your `ehr-
  phenotyping-os` framing targets.
- **Ancestry breakdown** — which three ancestries, and were AMR or
  African-ancestry OUD signals different from European
  (pharmacogenomics of OUD has known CYP2B6 / OPRM1 ancestry
  differences)?
- **Which DL annotation tool** (Enformer, DeepSEA-like, or a bespoke
  fine-tune?). Portability of DL-annotation gains across ancestries is
  the live methodological question.

**Where it links to your work.** Template for AoU multi-ancestry GWAS
+ DL functional-annotation follow-up. Also useful for the
`pharmacogenomic-modifier-of-medication-persistence` sub-thread
under pharmacoepi (OUD → opioid persistence framing).

---

### 4. Young C, Golden F, Fan W, Wong ND. *Impact of PREVENT-ASCVD vs pooled cohort equations on statin eligibility across demographic groups: Insights from the NIH All of Us Research Program* — **J Clin Lipidol 2026 Jul 7 (online ahead of print)**, doi:10.1016/j.jacl.2026.07.003. PMID 42527268.

**Feed:** NCBI PubMed "What's new for 'All of Us'" (07-30 15:20Z).

**Why HIGH.** Combines two live threads:
- **AoU-based pharmacoepi / preventive-medicine** — statin eligibility
  under two competing risk equations (AHA/ACC pooled cohort equations
  vs. the newer AHA PREVENT-ASCVD score) on the AoU cohort. Real
  policy question with immediate translational implications.
- **Ancestry-stratified risk-score portability** — the pooled cohort
  equations have documented calibration failures in non-European
  groups; PREVENT was rebuilt with contemporary + more diverse data.
  How the *difference* in eligibility distributes across AoU
  demographic groups is a direct measure of who benefits or loses from
  the equation swap.

**Actionable follow-on.** Read for:
- **Demographic-group breakdown** — race/ethnicity, age bands, sex —
  and where eligibility shifts most.
- **Whether they consider PRS augmentation** — a well-known angle in
  this space is stacking a CVD PRS on top of either risk equation;
  did they do that?
- **Sensitivity analysis on the LDL-C measurement variability** — AoU
  EHR-derived lipids have heterogeneous measurement timing; how did
  they handle it?

**Where it links to your work.** Reference example for the AoU +
preventive-medicine + risk-score-comparison framing. Feeds the
"downstream use of representations" angle of your Knowledge
representation in EHRs thread — a risk equation is a specific kind of
patient-representation, and equation swaps are a natural
representation-ablation experiment.

---

### 5. Kore P, Tan T, Lu W, Manuel-Friedman A, Hu L, Chatterjee N, Zhou W, Dhindsa RS, Atkinson EG. *Local ancestry-informed rare variant burden testing improves gene discovery in admixed populations* — **medRxiv [Preprint] 2026 Jul 15**, doi:10.64898/2026.07.13.26357993. PMID 42523458. Free PMC article.

**Feed:** NCBI PubMed "What's new for 'All of Us'" (07-30 15:20Z).

**Why HIGH.** Three-thread hit:
- **Rare-variant burden method** (variant-interpretation / genetic-epi
  thread) — the burden-test literature has historically been
  ancestry-monolithic; local-ancestry-aware burden testing is the
  natural admixed-population extension.
- **Ancestry portability** (genetic-epi thread) — AoU is
  ancestry-admixed at population scale, so any method that fixes
  reference-panel-driven bias in burden testing directly improves what
  you can do on AoU rare-variant analyses.
- **AoU / MVP / diverse-cohort infrastructure** (Atkinson lab has been
  driving admixed-population methods; Dhindsa is Regeneron rare-
  variant lineage). This is a methods paper for a real cohort-
  operational problem.

**Actionable follow-on.** Read for:
- **Local-ancestry inference tool** used (RFMix v2, Gnomix, FLARE?) and
  what deconvolution granularity — chunk size drives test power.
- **Which burden test framework** (SKAT / SKAT-O / STAAR / a bespoke
  reweighting?) and whether the local-ancestry weighting rides on
  functional-annotation weights.
- **Comparison to naive burden** — how much gene discovery improves,
  and does the improvement concentrate in genes with ancestry-
  differential allele frequency?

**Where it links to your work.** File as a candidate method for any
AoU-based rare-variant burden analysis, especially anything targeting
non-European ancestry contributions. Also relevant to the composite-
risk / PGS-tails framing under genetic epi (rare-variant burden ×
common-variant PGS is where composite risk gets its power).

---

### 6. Abegaz TM, Frietze G. *Machine learning algorithms for predicting glycemic control and weight loss outcomes in GLP-1 receptor agonist users* — **Front Artif Intell 2026 Jul 15;9:1861563**, doi:10.3389/frai.2026.1861563. PMID 42529241. Free PMC article.

**Feed:** NCBI PubMed "What's new for 'All of Us'" (07-30 15:20Z).

**Why HIGH.** Direct hit on two active threads:
- **GLP-1 pharmacoepi** — predicting *individual* glycemic-control and
  weight-loss outcomes among GLP-1 RA users is the ML companion to the
  Hwang et al. AoU real-world weight-loss comparison paper (item #3 in
  the 07-30 report). Where Hwang gave you the *average*, this gives
  you the *heterogeneity*.
- **ML for precision health** — heterogeneous treatment-effect
  prediction tied to a clinical decision (whether/who to prescribe
  which GLP-1) is exactly the version of ML-for-precision-health your
  INTERESTS.md flags as HIGH.

**Actionable follow-on.** Read for:
- **Data source** — AoU, TriNetX, single-EHR, or claims? The AoU
  NCBI feed picked it up which is *suggestive* but not definitive of
  AoU-source (the NCBI query is broader than title text).
- **ML method** — gradient-boosting / random-forest / DL / causal
  forest? For a treatment-response prediction, the appropriate
  framing is causal HTE, not associative prediction; whether the
  paper distinguishes them matters.
- **External validation** — did they hold out a site or a time
  period for validation?
- **Sample size + weight ascertainment** — same question as for Hwang
  et al.

**Where it links to your work.** Direct reference for any AoU or
biobank-based GLP-1 heterogeneity-of-response work. If AoU-sourced,
this is another AoU-GLP-1 anchor.

---

### 7. Carter PR, Gozdecka M, Wen S, Quirós PM, Lockhart SM, Dudek M, Bond L, Richenberg G, Larsson SC, Bromage D, Mitchell J, Huntly B, Libby P, Clarke MCH, Fabre M, Vassiliou GS, Burgess S, Kar SP. *Statin Use and Genetically Predicted HMG-CoA Reductase Inhibition in Relation to Clonal Hematopoiesis* — **medRxiv [Preprint] 2026 Jul 13**, doi:10.64898/2026.07.08.26357595. PMID 42528572. Free PMC article.

**Feed:** NCBI PubMed "What's new for 'UK Biobank'" (07-30 15:20Z).

**Why HIGH.** Three-thread convergence:
- **CHIP / somatic mosaicism** (your active CHIP–VEXAS–LOY thread) —
  statin use vs. CHIP is a plausible causal question with prior signal
  from Libby's group (Libby is a co-author here, so this is the
  established-lab lineage).
- **Drug-target Mendelian randomisation** (your rising sub-thread) —
  HMG-CoA-reductase-inhibition MR (as a genetic proxy for statin
  exposure) *triangulated with observational statin use* is exactly
  the design pattern the Saxby et al. metformin × AAA paper flagged in
  the interests file exemplifies.
- **Pharmacoepi** — Vassiliou (CHIP genetics), Burgess (MR methods),
  and Kar (MR + CHIP) is a very strong methods roster — if the
  triangulation converges you can trust the direction.

**Actionable follow-on.** Read for:
- **Which CH definition** — VAF threshold, gene panel (DNMT3A, TET2,
  ASXL1 core vs. broader), and whether they separated CH-PD from
  clonal mosaicism generally.
- **MR design** — one-sample MR in UKB, two-sample MR with GLGC as
  exposure GWAS, or MR-Egger / IVW / weighted median for
  pleiotropy sensitivity.
- **Whether the observational-and-MR estimates agree in direction and
  magnitude** — this is the whole point of the triangulation.
- **Effect on LOY** if reported — LOY is the male-specific analogue
  you're watching, and a statin-vs-LOY signal would be worth
  standalone attention.

**Where it links to your work.** Direct reference for the CHIP +
pharmacoepi intersection. Also a template for how to write a
drug-target-MR + observational-triangulation paper if you want to
apply the pattern to any of your other drug-class threads
(CFTR-modulator persistence, GLP-1 RA cardiovascular effects, HRT).

---

### 8. Albiñana C, Richmond R, Wang B, Urpa L, Crouse JJ, Zeng Y, Rosoff DB, Abdi S; FinnGen; Li L, Chen Z, Millwood IY, Ollila HM, Hickie IB, Gachon F, Kramer A, Ray DW, Wray NR. *Population-scale molecular reconstruction of human circadian phase from blood biomarkers* — **medRxiv [Preprint] 2026 Jul 13**, doi:10.64898/2026.07.08.26356418. PMID 42528586. Free PMC article.

**Feed:** NCBI PubMed "What's new for 'UK Biobank'" (07-30 15:20Z).

**Why HIGH.** Direct follow-on to the 07-30 Żebrowska et al.
Circadian Imbalance Index study (item #4 in the 07-30 report). The
Żebrowska paper built a *phenotype* on top of self-report / activity;
this paper reconstructs *circadian phase* itself from blood-biomarker
signatures at population scale. Together they define the *construct*
side (Żebrowska: the composite phenotype) and the *biology* side
(Albiñana: the underlying phase estimator) of the same active research
programme. The FinnGen affiliation + Wray as senior author signal
credibility on the population-scale claim.

**Actionable follow-on.** Read for:
- **Which biomarkers** enter the reconstruction (cortisol,
  melatonin, temperature-proxy metabolites, mRNA?). If it works from
  UKB Nightingale NMR + Olink alone, it becomes portable to any UKB /
  AoU cohort.
- **Reconstruction accuracy** vs. gold-standard DLMO (dim-light
  melatonin onset) — how far off, and is the error direction
  systematic?
- **PheWAS-ready output** — is the reconstructed phase available as a
  numeric trait, ready for GWAS / PheWAS follow-up? That determines
  reusability.

**Where it links to your work.** Reference for composite-phenotype /
biomarker-derived-trait design. If they release phase estimates as an
add-on to UKB, that's a usable exposure for any downstream PheWAS
(shift work, sleep disorders, cardiometabolic outcomes are the
obvious targets). Pairs with Żebrowska for a two-paper mini-arc in
the PheWAS-methodology thread.

---

### 9. Liu HY, Liu YY, Ge XX, Zhang LW, Bai JZ, Li QM, Liu L, Gong TT, Wu QJ, Sun W, Gao SY. *Associations of accelerometer-derived daily step counts with future health risks: A phenome-wide association study among over 60,000 UK adults* — **Int J Nurs Stud 2026 Jul 13;183:105638**, doi:10.1016/j.ijnurstu.2026.105638. PMID 42526147.

**Feed:** NCBI PubMed "What's new for 'UK Biobank'" (07-30 15:20Z).

**Why HIGH.** PheWAS methodology hit:
- **Exposure-PheWAS** (behavioral exposure → phecode outcomes) at
  large scale on the accelerometer sub-cohort. Distinct from
  variant-PheWAS but the same phenotype-space discipline (phecode
  outcomes, Bonferroni or FDR correction, ancestry / age / sex
  covariate handling).
- **The 60k accelerometer sub-cohort** is the widely-used UKB actigraphy
  sample; a PheWAS in it is a reference dataset for anyone who wants
  to compare their own step-based exposure-PheWAS results.

**Actionable follow-on.** Read for:
- **Phecode mapping used** — phecode 1.2 or phecodeX? Sex-specific
  exclusion handling?
- **Whether they used incident vs. prevalent phenotypes** and how they
  handled reverse causation (worse health → lower steps is the
  obvious confounder).
- **Multiple-testing correction** and how many phenotypes survive at
  what threshold.

**Where it links to your work.** Directly serves the PheWAS-
methodology thread. Also a reference for the exposure-PheWAS pattern
if you ever want to run a comparable exposure-PheWAS on AoU (which
has Fitbit / wearables data in the emerging vwb-aou-datasets-controlled
v9 collection per the `aou-workbench-2` skill).

---

### 10. Ran M, Shen Y, Guan R. *Doubly Robust Functional Representation Learning for Longitudinal Causal Inference with Irregular Histories* — **arXiv:2607.28567v1 (2026-07-30)**.

**Feed:** `arxiv-digest` repo `digests/2026-07-31.md` (score 1; keyword
hit "causal inference"; not deep-fetched).

**Why HIGH.** The abstract explicitly frames the target setting as
"laboratory values, physiologic signals, sensor streams, and image-
derived summaries measured at unequal and informative times" — this is
EHR-shaped data described in the exact language your causal-inference
+ EHR-phenotyping intersection would use. Serves:
- **Causal inference & pharmacoepi** (main thread) — a doubly-robust
  representation-learning framework with a claimed asymptotic
  linearity result under explicit rate / overlap / calibration /
  stability conditions is a serious methodological contribution to
  the longitudinal-EHR-causal-inference literature.
- **EHR foundation models** (adjacent) — the "functional and temporal
  encoders map point clouds and prior histories into states" framing
  is what CLMBR / MOTOR / MEDS-style encoders do; DR-FRL is what you
  *do with* those states when the target is a causal estimand rather
  than a prediction.

**Actionable follow-on.** Read the paper (not just the abstract) for:
- **The EIF-targeted validation diagnostic** — this is the core
  contribution. If the diagnostic is practical to run on real
  data, this is a directly usable tool for AoU longitudinal
  drug-effect analyses.
- **The VitalDB audit** — Ran et al. run their method on an
  ICU-disposition endpoint and report a *negative* finding (scalar
  laboratory summaries were already sufficient). Negative-finding
  audits are highly informative — they bound when the fancier
  method is worth the complexity.
- **Comparison to the Chou/Kallus oci-agent** (07-27 HIGH from the
  07-30 report) — where oci-agent automates *pipeline decisions*,
  DR-FRL automates *representation-of-history*. These are the two
  poles of "modernize causal inference for EHR-longitudinal data";
  they should be read as a pair.

**Where it links to your work.** Direct methods reference for any
AoU / UKB / BioVU longitudinal drug-effect analysis. Also a
candidate addition to the `causal-inference-os` skill's tool table
if the code is public.

---

### 11. Upmeier zu Belzen J, Arnoldt L, Hollmann N, Herrmann L, Nguyen KM, Eckhoff L, Kohleick L, Abou Ghaloun S, Schmidt H, Hegselmann S, Theis FJ, Buergel T, Steinfeldt J, Wild B, Eils R. *An interpretable omnigenic neural network architecture for the human genome* — **medRxiv [Preprint] 2026 Jul 28**, doi:10.64898/2026.07.28.26359187.

**Feed:** medRxiv Genetic and Genomic Medicine collection alert (07-31 00:05Z).

**Why HIGH.** Two-thread hit:
- **Omnigenic model as an NN with interpretability** — the omnigenic
  hypothesis (Pritchard/Boyle/Li) has been mostly a *conceptual*
  framework; a neural-network implementation with interpretability
  is a serious attempt at operationalizing it. The Eils/Theis roster
  is heavy on interpretable-ML and single-cell foundation models, so
  the interpretability claim probably has real machinery behind it.
- **EHR foundation model lineage** — Steinfeldt / Wild / Eils are the
  BB-DL / cardio-DL lineage that has been publishing EHR-genomic
  fusion models. Their interpretability work is relevant to the
  Knowledge-representation-in-EHRs thread.

**Actionable follow-on.** Read for:
- **What "interpretable" means** — attention-based saliency,
  concept-bottleneck, or a bespoke omnigenic-inspired
  factorization? The omnigenic model would suggest a *core-vs-
  peripheral gene decomposition* architecture, which would be new.
- **Which traits / phenotypes** the NN was tested on, and how it
  compares to sparse PGS (LDpred2 / PRScs) on prediction and on
  interpretability.
- **Whether the code / weights are released** — a released model is
  much more useful than a paper alone.

**Where it links to your work.** Adjacent to the composite-risk / PGS
thread — omnigenic-NN is an implicit alternative to PGS-tails +
rare-variant burden stacking. Also complementary to the EHR
foundation-model thread where interpretability is a rising sub-topic.

---

## METHODS-WATCH (compact list)

Off-thread on disease but worth tracking as design references:

- **Matsumoto N, Choi H, Freda PJ, Hernandez ME, Wang ZP, Moore JH.**
  *EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial
  Intelligence and Biomedical Discovery* — bioRxiv 2026 Jul 23,
  PMID 42523383. Free PMC. **Watch:** agentic-XAI framework applied
  to biomedical discovery — pairs with oci-agent (07-27) and DR-FRL
  (07-30) as the "modernize the pipeline" trio; Jason Moore lab
  lineage lends credibility.

- **Leary JR, Pattey S, Bacher R.** *LLM-powered Functional Gene Set
  Summarization with genesetGPT* — bioRxiv 2026 Jul 30. **Watch:**
  LLM-based functional annotation of gene sets; a lighter-weight
  companion to the GeneAgent (NCBI-NLP lineage) approach — worth
  cross-comparing to see which produces more auditable summaries.

- **Zhang Y-Z, Xu L, Imoto S.** *General-purpose language models
  integrate structured biological evidence for explainable biological
  interaction prediction* — bioRxiv 2026 Jul 30 (v2). **Watch:** LLM
  + structured biological evidence for *explainable* interaction
  prediction — sits at the intersection of the KG-based drug-
  repurposing thread and the "explainable hypothesis output" priority
  in INTERESTS.md.

- **Xie S, Chen W, Zhang B, Weng S.** *Interpretable ML-driven
  multi-omics risk stratification and drug repurposing… as a
  prognostic and druggable biomarker for glioblastoma* — Front Oncol
  2026 Jul 14, PMID 42523610. **Watch:** an interpretable-ML +
  multi-omics + drug-repurposing loop applied to a specific cancer.
  Structure is worth studying even if GBM isn't a target disease.

- **Ayubcha C, Dennis E, Bhattacharyya U, John J, Lam M, Lencz T, Ge T,
  Chen CY.** *Characterizing the impact of plasma protein levels on
  human brain structure and disorders leveraging integrative
  multi-omics analysis* — medRxiv 2026 Jul 15, PMID 42528609. Free
  PMC. **Watch:** multi-omics (proteomics + imaging + PGS) integration
  in UKB; feeds the multi-omics-augmented-PRS sub-thread.

- **Aydin B, Okutan BN, Sara FE, Gulseren G, Sinha R.** *Integrative
  Network-Based Transcriptomic Analysis Identifies Niclosamide as a
  Candidate Repositioned Drug for Breast Cancer* — Breast Cancer
  (Dove) 2026 Jul 24, PMID 42524299. **Watch:** classical network-
  based transcriptomic repurposing — off the EHR-evidence-loop angle
  you prefer, but a reference for the older/comparison methodology.

- **Diambra L, Sookoian S, Pirola CJ.** *Proteomic resolution of the
  MASLD cardiometabolic spectrum identifies sex-driven endotypes and
  predicts systemic mortality* — Gut 2026 Jul 29, PMID 42527119.
  **Watch:** proteomics-derived endotypes with a mortality outcome —
  template for proteomics-augmented cardiometabolic phenotyping.

- **Liu X, Zhang N, Wu S, Zhang M, Sun B, Chen L.** *Druggable
  Mendelian randomization prioritizes CDH2 and supports finerenone
  as a candidate therapeutic strategy for diabetic retinopathy* —
  Front Pharmacol 2026 Jul 15, PMID 42528538. Free PMC. **Watch:**
  drug-target MR generating a specific-drug candidate — same design
  family as the Saxby et al. metformin × AAA paper flagged in
  INTERESTS.md.

- **Kore et al. (item #5) is the AoU-side of local-ancestry burden
  testing.** The UKB-side reference in this window is **CuGen** —
  Kiiskinen T, Richland J, Wang W, Lu S, Narasimhan B, Hastie T,
  Tibshirani R, Rivas MA. *CuGen: A GPU-accelerated framework for
  large-scale genomics* — medRxiv 2026 Jul 17, PMID 42523429. Free
  PMC. **Watch:** GPU-accelerated genomics from the Rivas lab — a
  compute-infrastructure paper worth checking for AoU/UKB analysis
  throughput.

- **Gao X, Chen S, Mahabub S, Cao B, Deng J, Ye W, Yang H, Zou Z.**
  *A modified frailty index to identify high-risk groups for
  amyotrophic lateral sclerosis* — Front Neurol 2026 Jul 15, PMID
  42528798. Free PMC. **Watch:** ALS pre-onset / high-risk-group
  identification is adjacent to the Ran/Benatar pre-symptomatic
  ALS-phenoconversion template you're tracking under rare disease.

- **Schecter DR, Tinker RJ, Danieletto M, MacDonald G, Kozicz T,
  Morava E, Glicksberg BS.** *ArchSpiral: An iPad-Based Digital
  Archimedean Spiral Assessment for Objective Motor Evaluation in
  Rare Diseases* — medRxiv 2026 Jul 27. **Watch:** digital-
  phenotyping template for rare-disease motor assessment (Glicksberg
  lineage, Mount Sinai); could be portable to the pre-symptomatic
  phenoconversion sub-thread.

- **Collier A.** *First-Day Documentation Patterns and Mortality or
  Continued ICU Occupancy Across Four Critical Care Datasets: A
  Fixed-Window Retrospective Study* — medRxiv 2026 Jun 04 (v2 posted
  2026-07-30). **Watch:** cross-dataset EHR-representation robustness
  question — same idea as your "representation choices drift across
  sites" sub-topic under Knowledge representation in EHRs.

- **Dapagliflozin to Reduce Acute Kidney Injury After Cardiac Surgery**
  — JAMA Online First (07-30 18:42Z; item title only, no PMID
  extracted from the alert). **Watch:** SGLT2i-thread trial; add to
  the SGLT2i drug-class watchlist.

---

## SKIP-worthy (noted for the record)

Non-exhaustive; items surfaced by feeds that don't survive triage
against active threads:

- Modeling myeloid cell development iPSC review (Tesakov et al.,
  Front Immunol) — off-thread.
- Pramocaine × fluconazole biofilms (Hang et al., Biochem Pharmacol)
  — off-thread.
- Organoid-validation drug-repurposing review (Gulisano, Pharmacol
  Res) — general review, not sufficiently on-thread.
- DL DTIs for SARS-CoV-2 (de Souza et al.) — off-thread.
- Cariprazine repurposing hypothesis for anorexia nervosa (Kovacs et
  al.) — hypothesis paper, off-thread.
- Absolute quantitative proteomics + repurposing in ccRCC (Figueiredo
  et al., bioRxiv) — off-thread.
- Physical activity × RA genetic risk (Zhong et al.) — off-thread.
- Genetic correlation UKB IDPs × externalizing behavior (Wei & Peng)
  — LDSC PheWAS-adjacent but off-thread.
- Flavonoid intake × psoriasis genetic risk (Zhang et al., Food
  Funct) — nutritional epi, off-thread.
- Lp(a) & aortic diseases review (Xia et al.) — off-thread despite
  drug-target-MR angle.
- Unified prostate-cancer GRS (Shi et al., J Med Genet) — potentially
  cite-worthy for prostate-cancer-genetics context, but off your
  active threads.
- Clinical Obesity Beyond BMI (Liu et al., Am J Prev Med) —
  off-thread.
- Lp(a) HTA (Morton et al., Atherosclerosis) — off-thread.
- Menopausal HRT + BPPV (Li et al., Maturitas) — HRT-adjacent but
  outcome (BPPV) is off-thread.
- Sugar restriction in utero + dementia (Zheng et al., Neurology) —
  developmental origins, off-thread.
- Gut-brain-adipose in UPF & obesity review (Louie, Curr Obes Rep)
  — review, off-thread.
- Subthalamic connectivity in PD (Wang et al., Brain) — off-thread.
- Omega-3 & cardiometabolic UKB systematic review (Firdous &
  Calder, Lipids) — nutritional epi, off-thread.
- Genotype-Phenotype in HCM NHLBI Registry (Goel et al.) — cardio
  genetics, off your active disease threads (no CFTR/APOL1/CHIP
  angle).
- Polygenic burden of ubiquitin genes in schizophrenia (Riquelme
  Alacid et al.) — off-thread.
- Genetically nominated CKM features & weight-loss response (Hsueh
  et al.) — GLP-1-adjacent but the framing is negative
  ("not preferentially responsive"), lower priority than the
  positive-signal GLP-1 items.
- LACHESIS: real-time inference of malignant transformation (Eggle
  et al.) — cancer-genomics tool, off your active disease threads.
- LMNA R541C DCM iPSC-cardiomyocyte functional study (Keller et al.)
  — variant-interpretation angle but disease off-thread.

---

## Anchors from the 07-30 report still active

The following items from `reports/2026-07-30-research-digest.md`
remain open reading tasks — none of them have follow-on items in the
07-30-→07-31 window:

- Tang et al. BMJ TTE for GLP-1 × hair loss (HIGH #1)
- Eze et al. GLP-1 × cancer outcomes systematic review (HIGH #2)
- Hwang et al. AoU real-world GLP-1 weight-loss head-to-head (HIGH
  #3)
- Żebrowska et al. eBioMedicine Circadian Imbalance Index — now
  paired with the Albiñana et al. phase reconstruction (HIGH #8
  above) as a mini-arc
- Feng et al. cross-ancestry pleiotropic IDP-PGS for depression
  (HIGH #5)
- Wang et al. arXiv silver labels in EHR computable phenotyping
  (HIGH #6)
- Nguyen et al. PrimeKG-Plus (HIGH #7)
- Corsi-Zuelli et al. methotrexate × psychosis EHR (HIGH #8)
- Song et al. LLM specialty triage in rare diseases (HIGH #9)
- Ekici et al. Mendelian kidney-disease diagnostic yield (HIGH
  #10)
- Liu et al. Neurotherapeutics DL + WGS repurposing across 92 CNS
  conditions (HIGH #11)
- García et al. Archives of Medical Research variant-curation
  standards review (HIGH #12)
- Guo et al. GraphRareBench arXiv (HIGH #13)
- Jin et al. Nature Protocols LLMs-for-medical-research tutorial
  (HIGH #14)
- Chou et al. oci-agent arXiv (HIGH #15) — now paired with Ran et
  al. DR-FRL (HIGH #10 above) as a mini-arc

---

## Suggested next-step actions

1. **Verify authorship + DAS on the Bujnis et al. Nat Genet
   Hashimoto's paper** (item #1). Confirm the author string and check
   the DOI resolves to the version you signed off on.
2. **Read paired reads** — DR-FRL + oci-agent (07-30 anchor) as the
   causal-inference-methods mini-arc; Żebrowska (07-30 anchor) +
   Albiñana (item #8) as the circadian-phenotyping mini-arc.
3. **File Carter et al. HMG-CoA-CH triangulation as a template
   design** — this is the drug-target-MR + observational-
   triangulation pattern INTERESTS.md flags, applied to your CHIP
   thread. Worth a short writeup for the `causal-inference-os` skill.
4. **Ahn et al. AoU HLA + Kore et al. local-ancestry burden** — two
   AoU-methods anchors from the same day. If you're planning any
   admixed-population autoimmune-adjacent work on AoU, read both
   before scoping.
