# Research digest report — 2026-09-16

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-16 12:40Z** (~15 days since the
last research-digest report, covering twelve arxiv-digest cron runs
and roughly ten Google Scholar / NCBI PubMed alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-12.md`) | 09-01 → 09-12 daily crons | 12 daily runs. Dry days (0 papers or off-topic only): 09-01 (storage-centric genomic systems, off-topic), 09-03, 09-05, 09-06, 09-08, 09-12. Surfacing days: 09-02 (Mudskippers, off-topic keyword hit on "motor"), 09-04 (Cortez-Rodriguez nonprofit-sector natural-disaster causal panel; Yu et al. location-invariant extremal QTE with IPW), 09-07 (Rajabli 3D-CNN Alzheimer's brain-age foundation model), 09-09 (Snel & Schulz UKB Cohen's-d influence functions; Wu et al. HPLC Sim2Real FM), 09-10 (Lee et al. Kalman filter + IPW for infectious-disease HT estimation), 09-11 (Devarakonda scDEFT IBD cell-perturbation FM; Hendrix et al. geospatial FMs beyond SVI/ADI; Semchin et al. Parkinson's SuStaIn-competitor). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads. The pipeline commits its output to this repo rather than emailing PR / cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-15 batch, 17:30Z) | 09-15 17:30Z | Largest single batch of the window — ~30 feeds fired. Direct-relevance highlights: **1 new-citation to Chenjie Zeng** (Feng et al. *Annals of Human Genetics* 2026, MR of LTL/EAA vs. healthspan); **Chenjie Zeng new-related** (Diaby et al. *Addictive Behaviors* AoU poly-tobacco disparities; ATM germline testing in hereditary cancer; SLE-schizophrenia pleiotropy KCL); **Joshua C. Denny cited-by** (Landman et al. *Nature Metabolism* HCHS/SOL paediatric proteomic signatures; STAWISKI et al. somatic-likelihood tiering for tumor-only WES; Arditi et al. adult-onset prenatal diagnosis with eMERGE secondary findings citation); **George Hripcsak cited-by** (Branigan Cureus GLP-1 vs SGLT2 cardiorenal review; Islam et al. JMIR Formative HSV-1 dementia with 17,000-covariate HD-PS; Weigl et al. JAMIA Open EHR implementation workflow prospective); **Hripcsak new-related** (Schulte-Althoff et al. *npj Health Systems* SHAP fall-risk EHR; Du et al. arXiv 2608.20315 explainable transformer EHR; Chen et al. medRxiv 2026 rethinking input complexity in transformer EHR); **Lisa Bastarache new-related, Kai Wang new-related, Stephen Montgomery new-related** all convergent on Pitsava et al. medRxiv 2026 long-read GS yield in SR-negative rare-disease cases; **Stephen Montgomery new-related** also Ma et al. medRxiv lrRNA-seq splicing outliers in whole blood, Zheng et al. medRxiv proteomic-vs-polygenic risk score neurodegeneration divergence, Khodasevich et al. *Genome Medicine* MVP ancestry-specific methylation of smoking → ASCVD, Zhou et al. STAR protocols admixed AoU polygenic prediction; **Konrad Karczewski new-related** (Park et al. *Translational Psychiatry* cross-ancestry OCD-PRS transferability; Idris et al. *Human Molecular Genetics* 46,XY DSD in understudied population); **Patrick Ryan new-related** (Islam et al. HSV-1 dementia, same paper as Hripcsak feed); **Pascal Brandt new-related** (Schulte-Althoff SHAP fall-risk, same paper); **Miguel Hernán cited-by** (Shi et al. *AJE* "Questions asked and, maybe, answered with Mendelian randomization"). |
| Google Scholar alerts (09-16 batch, 06:34Z) | 09-16 06:34Z | 10 keyword feeds fired. Direct-relevance: **"All of Us research program"** (Krueger 2026 dissertation Genetic Fine-Mapping of Plasma Proteome across Multi-Ancestral Populations — AoU PWAS in 10 cardiometabolic phenotypes with Pan-UKB replication; Devore 2026 dissertation Genomic Sequencing of Novel Disease-Associated Alleles in Friedreich Ataxia using AoU+TOPMed+UKB); **"UK Biobank"** (Yang et al. UKB accelerometer physical activity vs pericardial adiposity prospective cohort); **Foundation models + "electronic health records"** (Ala 2026 SCALE-FHIR data engineering, non-methodological); **"electronic health records"** (Cheptora 2026 MedicalTV nurse-call integration, non-research); **"drug repurposing"** (Lu & Wang *BMC Medicine* diacerein for glioma via pyroptosis, chem-only). Peripheral: mendelian-diseases feed (Deng et al. *Genes* multi-omics MR lipids × brain cell types × kidney disease); rare diseases feed (Dianderas et al. Latin America scoping review, non-methodological); variant-interpretation feed (Meena et al. *EJIFCC* CLCN7 osteopetrosis case, non-methodological). |
| Google Scholar alerts (09-14 batch, 14:22Z) | 09-14 14:22Z | 8 keyword feeds fired. Direct-relevance: **Foundation models + EHR** (Liang et al. *BMJ* 2026 PREDICT-1o Diabetes CVD prediction NZ vs China EHR simultaneous derivation/validation; Kim & Gha-hyun *J Psychosom Res* EHR subtype-dependent depression↔GI directionality; Seker et al. *IJMPR* NLP mood-instability EHR from 13,025 adolescents in ADHD/depression cannabis-use prediction); **AoU feed** (Diaby et al. AoU poly-tobacco, same as 09-15 batch); **UKB feed** (Zhang et al. UKB + Chinese hospital external-validation of MCI in CAD-hypertension); **mendelian-diseases feed** (Liang et al. *PLOS Medicine* protein mediators of CKD in T2D via MR). |
| NCBI PubMed alerts (09-16 batch, 12:34Z) | 09-16 12:34Z | 3 feeds fired: `UK Biobank`, `All of Us`, `drug repurposing`. Bodies re-index Scholar-covered items; nothing new not already surfaced. |
| Nature Medicine Vol 32 Issue 9 (09-16 email, 06:40Z) | 09-16 06:40Z | Table-of-contents alert. Full triage against issue not conducted within this run; flag for a follow-up read when a manuscript task calls for it. |
| Sundry AI/tech newsletters (AINews, RohanPaul, SemiAnalysis, alphaXiv, swyx substack) | 09-15 → 09-16 | Off-topic for research threads; not further triaged. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fourteen HIGH items surfaced this window, clustering into six knots:

**Direct citation to your own work (1 item).** Feng et al. *Annals of
Human Genetics* 2026 (Chenjie Zeng cited-by feed) — genetically proxied
LTL and EAA vs. healthspan two-sample MR. Cites the "Association between
telomere length and risk of cancer and non-cancer" work in your
authorship line. First direct-cite fire of the window.

**EHR + real-world causal inference cluster (3 items).** Islam et al.
*JMIR Formative Research* 2026 (Hripcsak + Patrick Ryan feeds) — HSV-1
and dementia outcomes in real-world EHR data using **~17,000-covariate
high-dimensional propensity scores** with equipoise-sensitivity Cox
models. Direct-hit for both `Causal inference and pharmacoepidemiology`
and `EHR phenotyping & OMOP`. Kim & Gha-hyun *J Psychosom Res* 2026
(EHR keyword feed) — subtype-dependent bidirectional depression ↔ GI
Cox modeling with base-vs-full adjustment strata, stratified by GI
subtype. Liang et al. *BMJ* 2026 (EHR-FM keyword feed) — simultaneous
derivation, validation, and comparison of CVD-in-diabetes prediction
equations from NZ vs Chinese EHR (PREDICT-1o Diabetes as base). All
three exemplify the design-discipline patterns the pharmacoepi thread
wants to see propagated.

**EHR foundation models + explainable clinical prediction (4 items).**
Schulte-Althoff et al. *npj Health Systems* 2026 (Hripcsak, Pascal
Brandt, EHR-FM feeds all converged) — SHAP-space fall risk profiling
translating individual-level EHR effects into clinically meaningful
group-level risk profiles. Du et al. arXiv 2608.20315 (Hripcsak-related
feed) — explainable transformer models for structured EHR emphasizing
quantitative lab information and event-level interpretability. Chen et
al. medRxiv 2026 (Hripcsak-related feed) — **rethinking input complexity
in transformer-based clinical prediction**: challenges the "more data,
more history = better performance" premise; directly extends your
`Fidelity, portability, and audit of representations` sub-thread.
Rajabli & Collins arXiv 2609.05400 (arxiv-digest 09-07) — a compact 7.18M-param
3D-CNN brain-age model as a **reusable foundation model for
Alzheimer's-related MRI tasks**, adapted via LoRA (~1% additional
params), transferring ADNI→OASIS-3 without retraining. A concrete
demonstration of the "small pretrained + LoRA vs. huge FM" trade-off
that also applies to structured-EHR FMs.

**Rare-disease / long-read genomics cluster (2 items).** Pitsava et al.
medRxiv 2026 (Lisa Bastarache, Kai Wang, Stephen Montgomery feeds
converged) — **yield of long-read genome sequencing in SR-GS-negative
rare-disease cases**; direct-hit for `Rare disease` → `Data-driven
reanalysis of unsolved cases`. Ma et al. medRxiv 2026 (Montgomery feed)
— **long-read RNA-seq for splicing-outlier detection in whole blood from
rare-disease trios**; extends the splicing/RNA-evidence lever in your
`Variant interpretation (ACMG / ClinGen)` thread beyond fibroblast /
muscle to a scalable whole-blood pipeline.

**Genetic epi + biobank cluster (3 items).** Krueger 2026 dissertation
(AoU keyword feed) — **genetic fine-mapping of the plasma proteome
across multi-ancestral populations**: PWAS in 10 cardiometabolic
phenotypes within AoU with Pan-UKB replication. Direct-hit for
`Biobanks with EHR linkage: All of Us` and for `Multi-omics-augmented
PRS`. Landman et al. *Nature Metabolism* 2026 (Denny cited-by feed) —
**paediatric proteomic signatures of cardiometabolic disease-associated
traits predict adult disease outcomes** in HCHS/SOL Hispanic/Latino
children; the CKMD-cluster pediatric extension of the adult
proteomic-risk-score work. Khodasevich et al. *Genome Medicine* 2026
(Montgomery feed) — **MVP ancestry-specific DNA methylation signatures
of smoking and ASCVD risk**, direct-hit for `Biobanks with EHR linkage:
MVP` and for the epigenetic-mediator angle of PGx / composite-risk work.

**Cross-thread methods watch (1 item).** Snel & Schulz arXiv 2609.07729
(arxiv-digest 09-09) — **Cohen's-d influence functions on UK Biobank**
across 4 diseases and 2 biomarker modalities: removes the 10% most
influential training samples and raises disease-related effect size for
every seed (T2D metabolomic-age effect >2×, MS brain-age effect +~⅓).
`pyinfluence` open-source. Directly serves both `Fidelity, portability,
and audit of representations` (via subclinical-cardiometabolic
mislabelling audit) and the `Pretraining-contamination audits for
foundation-model benchmarks` sub-thread.

---

## Detailed HIGH-priority reports

### 1. Feng et al. *Annals of Human Genetics* 2026 — LTL / EAA vs. healthspan MR (Chenjie Zeng cited-by)

- **Citation.** Feng B, Yang R, Wang GR, Hu Q, Zhao C. Genetically
  Proxied Leukocyte Telomere Length and Epigenetic Age Acceleration in
  Relation to Healthspan: A Mendelian Randomization Study. *Annals of
  Human Genetics* 2026. `doi:10.1111/ahg.70057`.
- **Design.** Two-sample MR using published GWAS instruments for LTL and
  four EAA biomarkers, with healthspan as the outcome. Cites the
  "Association between telomere length and risk of cancer and non-cancer
  diseases" reference in the Chenjie Zeng authorship line as one of its
  motivating priors.
- **Why HIGH.** First direct-cite fire of the window on your own work.
  Puts LTL-healthspan back on the map as an MR-instrumentable exposure
  and gives you a fresh reference to point to when discussing biological
  aging biomarkers as MR exposures.
- **Follow-up.** Worth pulling the PDF to confirm which of the multiple
  Zeng-authored telomere papers is cited, and whether the EAA arm
  survives the four-biomarker MR-Egger / MR-PRESSO stability checks.
- **Thread.** Genetic epidemiology → biomarker-as-exposure scans.

### 2. Islam et al. *JMIR Formative Research* 2026 — HSV-1 × dementia with 17k-covariate HD-PS (Hripcsak + Patrick Ryan feeds)

- **Citation.** Islam MM, Foraker R, Hossain MS, Arnold WD, et al.
  Association of Herpes Simplex Virus Type-1 With Dementia Outcomes: A
  Longitudinal Retrospective Cohort Study Using Real-World EHR Data.
  *JMIR Formative Research* 2026; 1: e83028.
- **Design.** High-dimensional propensity score with ~17,000 baseline
  covariates estimated via regularized logistic regression; four strata
  weights fed into a Cox model, with equipoise sensitivity analyses.
  Cites the Hripcsak lineage on "empirical confidence interval
  calibration for population-level effect estimation."
- **Why HIGH.** Direct-hit exemplar of the design pattern your
  `Causal inference and pharmacoepidemiology` thread wants propagated —
  systematic HD-PS with calibration, applied to a modifiable
  exposure–outcome pair with real translational weight (HSV-1 →
  dementia, in the ongoing pre-print debate of whether antiviral
  prescribing modifies dementia risk). Cross-listed under `Biobanks with
  EHR linkage` because the JMIR-Formative population is EHR-derived.
- **Follow-up.** Compare estimator diagnostics (SMDs after weighting,
  equipoise thresholds) to the Ilves et al. CohortContrast pattern
  flagged in the previous digest report — same "empirical calibration"
  lineage, different phenotype geometry.
- **Thread.** Causal inference / pharmacoepi + EHR phenotyping.

### 3. Kim & Gha-hyun *J Psychosom Res* 2026 — subtype-dependent depression ↔ GI directionality (EHR keyword feed)

- **Citation.** Kim NM, Gha-hyun JK. Leveraging electronic health
  records for subtype-dependent directionality in depression and
  gastrointestinal disease: a retrospective cohort study. *Journal of
  Psychosomatic Research* 2026.
- **Design.** Cox models estimating bidirectional hazard ratios,
  stratified by GI subtype and replicated across sub-cohorts. Base
  models adjust for age/sex; full models add additional confounders;
  compares top-down (CNS-first) vs. bottom-up (gut-first) models.
- **Why HIGH.** Directly serves `Chronic disease clustering and
  multimorbidity` and provides a template for subtype-stratified
  bidirectional survival modeling that is portable to your IBD +
  autoimmune subthread and to GLP-1-RA persistence work where
  depression is a candidate mediator/modifier.
- **Follow-up.** Worth checking whether the paper uses phecodes vs.
  ICD-10 as its GI-subtype definition; if phecode-based, a direct pull
  into your `PheWAS / phecode infrastructure` methods library.
- **Thread.** Multimorbidity + EHR phenotyping.

### 4. Liang et al. *BMJ* 2026 — CVD-in-diabetes prediction, NZ vs China EHR (EHR-FM keyword feed)

- **Citation.** Liang J, Choi Y, Shen P, Wells S, Poppe K, Fu Z, et al.
  Simultaneous derivation, validation, and comparison of predictor
  hazard ratios for cardiovascular risk prediction equations in patients
  with diabetes from high versus non-high income countries. *BMJ* 2026;
  394: bmj-2026-100535.
- **Design.** Equivalent NZ and Chinese EHR cohorts of adults 30–74 with
  diabetes and no baseline CVD. Uses **PREDICT-1o Diabetes model** as the
  precursor and foundation, and performs simultaneous derivation +
  external validation for direct HR-comparability across settings.
- **Why HIGH.** Cross-country external validation of a diabetes-CVD risk
  equation from EHR data is the exact `ML for precision health →
  external validation across sites or ancestries` bullet in your
  interests file. The dual-cohort simultaneous-derivation design also
  matches the pattern your `Fidelity, portability, and audit of
  representations` sub-thread wants exemplified.
- **Follow-up.** Check whether the paper reports calibration slopes
  and decision-curve utility (not just discrimination) — the missing
  pieces that make ML-precision-health papers HIGH vs. METHODS-WATCH.
- **Thread.** ML for precision health + causal-adjacent EHR analytics.

### 5. Schulte-Althoff et al. *npj Health Systems* 2026 — SHAP-space fall risk profiling (Hripcsak + Brandt + EHR-FM feeds)

- **Citation.** Schulte-Althoff M, Krappen P, Bießmann F, Jäger S, et
  al. Explainable SHAP-space fall risk profiling from electronic health
  records for inpatient prevention planning. *npj Health Systems* 2026.
  `doi:10.1038/s44401-026-00138-4`.
- **Design.** Retrospective observational EHR study at a large hospital
  translating individual-level SHAP contributions into clinically
  meaningful group-level risk profiles for fall-prevention planning.
  Explicit critique of one-size-fits-all fall prevention.
- **Why HIGH.** Three of your author-feeds converged on this on the same
  day (Hripcsak, Brandt, and the EHR-FM keyword feed) — a strong signal.
  Directly addresses the `NLP-derived representations from clinical
  notes` → `Applications to prioritize → care-gap identification` axis of
  the `Knowledge representation in EHRs` thread, transposed to a
  high-volume inpatient-safety endpoint.
- **Thread.** Knowledge representation in EHRs + ML for precision health.

### 6. Du et al. arXiv 2608.20315 — Explainable transformer models for structured EHR (Hripcsak-related feed)

- **Citation.** Du JN, Adamek L, Kryukov M, Dormont F, Bar-Joseph Z, et
  al. Explainable Transformer Models for Clinical Prediction Tasks on
  Structured Electronic Health Records. *arXiv:2608.20315* 2026.
- **Design.** Jointly emphasises quantitative laboratory information
  and interpretability with respect to input medical events on
  structured EHRs — an interpretability-first take on the transformer
  clinical-prediction stack.
- **Why HIGH.** Fills the explicit gap in the FEMR/MEDS/CLMBR lineage
  where quantitative labs are usually bucket-tokenised and lose
  numeric information. Sub-thread hit on `Structural and temporal
  representation of the patient timeline` and on `Fidelity, portability,
  and audit of representations`.
- **Thread.** EHR foundation models + knowledge representation in EHRs.

### 7. Chen et al. medRxiv 2026 — Rethinking input complexity in transformer clinical prediction (Hripcsak-related feed)

- **Citation.** Chen W, Zhou B, Zeiger RS, Crawford WW, Schatz M, et al.
  Rethinking Input Complexity in Transformer-Based Clinical Prediction:
  Implications for Feature Dimensionality and Sequence Length in
  Longitudinal EHR Data. *medRxiv* 2026.
- **Design.** Challenges the assumption that more features and longer
  patient histories improve transformer-based clinical prediction, on
  longitudinal EHR data. Systematic ablation study.
- **Why HIGH.** This is the exact "representation-ablation study that
  shows *which representation choice* drives downstream performance vs.
  the model architecture" bullet from your `Applications to prioritize`
  section under `Knowledge representation in EHRs`. Paired with Du et
  al. above, the same-day pair looks like a coordinated methodological
  push for representation-audit discipline in transformer EHR-FMs.
- **Thread.** Knowledge representation in EHRs → representation-ablation
  audit.

### 8. Rajabli & Collins arXiv 2609.05400 — Compact brain-age FM + LoRA (arxiv-digest 09-07)

- **Citation.** Rajabli R, Collins DL. A Generalizable Feature Extractor
  for Alzheimer's-Related Brain MRI Tasks. *arXiv:2609.05400* 2026.
- **Design.** Freezes 7.18M weights of a supervised 3D-CNN trained for
  brain-age prediction; adapts to each downstream task via LoRA with
  ~1% additional trainable parameters. Six-experiment eval:
  CN-vs-dementia ADNI AUC 0.964; unchanged transfer to OASIS-3 AUC
  0.871; MCI-progression AUC 0.828; amyloid-positivity-from-T1w AUC
  0.804; ICV-normalized hippocampal + WMH volume R² 0.80 / 0.91.
- **Why HIGH.** Serves as a concrete counter-example to the "must be
  huge to be a foundation model" framing — a compact supervised
  brain-age backbone + LoRA transfers across cohorts without any
  retraining. The same design pattern is portable to structured-EHR-FM
  work where CLMBR/MEDS-style pretraining is compute-heavy and
  contamination-audit-prone (per the scContam / MIA-scFM lineage
  flagged in prior reports).
- **Thread.** EHR foundation models (portable methods) + ML for
  precision health.

### 9. Pitsava et al. medRxiv 2026 — Long-read GS yield in SR-negative rare-disease cases (Bastarache + Kai Wang + Montgomery feeds)

- **Citation.** Pitsava G, Bluske K, Barrick R, De Dios I, Duong C, et
  al. Yield of Long-Read Genome Sequencing for Rare Disease Diagnosis
  in Short-Read Genome Negative Cases. *medRxiv* 2026.
  `2026.09.09.26362331`.
- **Design.** Prospective cohort of SR-GS-negative rare-disease
  probands reflexed to LR-GS; quantifies incremental diagnostic yield
  and variant-class contribution (SV, tandem repeat, complex rearr).
- **Why HIGH.** Direct-hit for `Rare disease → Data-driven reanalysis
  of unsolved cases at 10k+ cohort scale` (though this is a smaller-N
  focused study, it's the natural upstream reference for the
  Uria-Regojo medRxiv 2026 mid-scale reanalysis paper). Three
  independent author-feeds converged on it same-day — a strong signal
  of field consensus that this is the reference point for LR-GS in
  clinical rare disease.
- **Thread.** Rare disease + variant interpretation.

### 10. Ma et al. medRxiv 2026 — Long-read RNA-seq splicing outliers in whole blood (Montgomery feed)

- **Citation.** Ma J, Weisburd B, DiTroia S, Romo L, Covill LE, et al.
  Long-read RNA sequencing improves isoform and splicing outlier
  detection in whole blood from rare disease trios. *medRxiv* 2026.
- **Design.** Rare-disease trios with lrRNA-seq on whole blood; compares
  isoform / splicing outlier detection against short-read baseline.
- **Why HIGH.** Splicing / RNA evidence for VUS resolution is an
  explicit sub-bullet under your `Variant interpretation (ACMG /
  ClinGen)` thread; moving from fibroblast / muscle to whole-blood
  lrRNA-seq is the practical scalability step that unlocks routine
  RNA-evidence layering in ACMG-AMP re-classification workflows.
- **Thread.** Variant interpretation + rare disease.

### 11. Krueger 2026 dissertation — Genetic fine-mapping of plasma proteome across multi-ancestral populations (AoU keyword feed)

- **Citation.** Krueger CJ. Genetic Fine-Mapping of the Plasma Proteome
  Across Multi-Ancestral Populations. Dissertation, 2026.
- **Design.** PWAS in **ten cardiometabolic phenotypes** within the AoU
  Research Program, with replication in Pan-UK Biobank (Pan-UKB), under
  the hypothesis that multi-ancestry modeling improves discovery and
  protein-disease attribution.
- **Why HIGH.** Direct-hit for `Biobanks with EHR linkage: All of Us`
  and for the `Multi-omics-augmented PRS` sub-thread (proteomic-instead-
  of-genotype layering). The multi-ancestry AoU-primary / Pan-UKB-
  replication design is exactly the portability-first template your
  interests file prioritises.
- **Follow-up.** Since this is a dissertation, look for the eventual
  peer-reviewed version — will likely land in *Nature Genetics* or
  *AJHG*.
- **Thread.** Biobanks + genetic epi + multi-omics-augmented PRS.

### 12. Landman et al. *Nature Metabolism* 2026 — Paediatric proteomic signatures of CKMD (Denny cited-by)

- **Citation.** Landman JM, Highland HM, Perry AS, Howard AG, et al.
  Paediatric proteomic signatures of cardiometabolic disease-associated
  traits predict adult disease outcomes. *Nature Metabolism* 2026.
  `doi:10.1038/s42255-026-01589-7`.
- **Design.** Linked 25 CKMD phenotypes (liver, adipose, vascular,
  dysglycaemia) to the circulating proteome in 273 Hispanic / Latino
  children (13.1 ± 2.7 years). Cites the Denny lineage on "Genetic
  drivers of heterogeneity in type 2 diabetes pathophysiology."
- **Why HIGH.** The pediatric extension of adult proteomic-risk-score
  work with genuine translational implications — current adult risk
  thresholds miss a substantial fraction of children at high CKMD risk,
  and pediatric-proteome→adult-outcome prediction is the earliest
  possible intervention window. Direct-hit for `Multi-omics-augmented
  PRS` and cross-thread `Rare disease → Pre-symptomatic carrier
  phenoconversion prediction from longitudinal biomarker trajectories`
  (though HCHS/SOL is not a rare-disease cohort, the trajectory-
  prediction framing is the same).
- **Thread.** Genetic epi + biobank + ML for precision health.

### 13. Khodasevich et al. *Genome Medicine* 2026 — MVP smoking methylation × ASCVD (Montgomery feed)

- **Citation.** Khodasevich D, Hilliard AT, Barad A, Zhou J, et al.
  Ancestry-specific DNA methylation signatures of smoking and
  associations with atherosclerotic cardiovascular disease risk:
  findings from the Million Veteran Program. *Genome Medicine* 2026.
  `doi:10.1186/s13073-026-01761-4`.
- **Design.** Ancestry-stratified EWAS of smoking within MVP, with
  methylation-ASCVD association tests, addressing the limitation that
  even the largest EWAS have been dominated by European-ancestry data.
- **Why HIGH.** Direct-hit for `Biobanks with EHR linkage: MVP` and for
  the epigenetic-mediator angle of composite-risk models. Portable to
  your PGx-modifier-of-medication-persistence work if the same
  ancestry-stratified methylation pattern shows up for cessation
  outcomes or nicotine-replacement adherence.
- **Thread.** Biobanks + genetic epi (epigenetic layer).

### 14. Snel & Schulz arXiv 2609.07729 — Cohen's-d influence functions on UK Biobank (arxiv-digest 09-09)

- **Citation.** Snel J, Schulz MA. Attributing Cohen's d: Training Data
  Attribution for Disease-Related Effects in Normative Age Biomarkers.
  *arXiv:2609.07729* 2026.
- **Design.** Closed-form influence functional for Cohen's *d*,
  validated against LOO retraining. Applied to 4 diseases × 2 biomarker
  modalities on UK Biobank normative-age models. Removing top-10%
  influential training samples raises held-out disease-related effect
  size in every seed — T2D metabolomic-age >2× effect, MS brain-age
  +~⅓. Random removal leaves effect size flat at up to 50% removal.
  Flagged subjects carry subclinical cardiometabolic burden that
  diagnosis-based exclusion misses; for T2D the recovered marker is
  HbA1c. Releases `pyinfluence`.
- **Why HIGH.** Serves two of your rising sub-threads at once:
  (a) `Fidelity, portability, and audit of representations` — this is
  a training-data-attribution audit of biomarker-normative-age models,
  revealing hidden subclinical-cardiometabolic mislabelling in
  "healthy" controls; (b) `Pretraining-contamination audits for
  foundation-model benchmarks` — the same influence-function machinery
  is portable to CLMBR / MOTOR / MEDS-benchmark contamination audits,
  parallel to the scContam / MIA-scFM protocols. The `pyinfluence`
  release lowers the barrier to running the audit yourself.
- **Thread.** EHR foundation models (audit sub-thread) + genetic epi
  (biomarker-as-exposure) + ML for precision health.

---

## METHODS-WATCH items (brief)

- **Cortez-Rodriguez arXiv 2609.04136** (arxiv-digest 09-04) — panel-data
  causal inference on natural-disaster damage → nonprofit-sector
  outcomes. Off-topic disease, but exemplary panel-DID with negative
  finding overturning prior lit; template for null-result reporting
  in panel-causal work.
- **Yu et al. arXiv 2609.04018** (arxiv-digest 09-04) — location-invariant
  extremal quantile treatment effects with IPW; matters if extremal
  QTEs enter your pharmacoepi toolkit (e.g., high-tail HbA1c under GLP-1
  vs. SGLT2i).
- **Lee et al. arXiv 2609.09325** (arxiv-digest 09-10) — Kalman filter /
  smoother atop Horvitz–Thompson IPW estimators for prevalence with
  missing days; portable design pattern for any IPW-noisy time-series
  clinical estimator (e.g., real-time drug-utilisation dashboards).
- **Devarakonda arXiv 2609.10831 (scDEFT)** (arxiv-digest 09-11) —
  drug-conditioning FiLM on cell latents applied to a harmonized IBD
  atlas (1.16M cells, 3 cohorts, 2 drug classes); pre-treatment
  responder-stratification AUROC 0.70. Direct methodological
  interest as an IBD single-cell-drug-response reference; only
  METHODS-WATCH rather than HIGH because it's cell-level rather
  than EHR-linked.
- **Hendrix et al. arXiv 2609.11689** (arxiv-digest 09-11) — geospatial
  FMs from 2022 satellite imagery capture health-relevant place
  features **beyond conventional social risk indices (ADI/SDI/SVI)**,
  explaining up to 54% of residual variance in CDC PLACES outcomes
  across 82,646 tracts. Useful reference when discussing SDoH residual
  confounding in EHR-linked biobank causal-inference work.
- **Semchin et al. arXiv 2609.10890** (arxiv-digest 09-11) — connectome-
  constrained disease-progression model with data-driven subtyping on
  PPMI Parkinson's imaging + clinical; **beats SuStaIn on subtype-clinical
  correspondence**. Portable trajectory-clustering method for your
  multimorbidity + neurodegeneration work.
- **Shi et al. *AJE* 2026 "Questions asked and, maybe, answered with
  Mendelian randomization"** (Hernán cited-by) — instrumental-variables
  perspective piece; useful teaching-reference when framing MR-based
  target-trial-emulation triangulations (per your Saxby-metformin×AAA
  sub-thread).
- **Zheng et al. medRxiv 2026** (Montgomery feed) — proteomic-vs-polygenic
  risk score divergence in neurodegenerative disease via absorption /
  co-expression modules. Cross-thread with the tails-and-residuals PGS
  framing.
- **Zhou et al. STAR protocols 2026** (Montgomery + Karczewski + Denny
  feeds) — protocol for leveraging local ancestry + cross-ancestry
  genetic architecture to improve polygenic prediction in admixed
  populations using AoU. Useful reference for the AoU-admixed
  polygenic-prediction sub-thread.
- **Park et al. *Translational Psychiatry* 2026** (Karczewski feed) —
  cross-ancestry and cross-disorder transferability of PRS for OCD.
  Instance of the cross-ancestry portability + cross-trait shared
  architecture double-thread.

---

## SKIP / low-signal noise

- **Mudskippers-on-mud (arxiv-digest 09-02)** — off-topic
  physics.bio-ph, keyword-hit on "motor."
- **Wu et al. HPLC FUSE-RT (arxiv-digest 09-09)** — chemistry-domain
  FM, no clinical hook.
- **Lu & Wang *BMC Medicine* diacerein glioma repurposing** — chem-only
  pipeline without a clinical-evidence loop, matches the "lower interest"
  clause of the drug-repurposing thread.
- **Cheptora MedicalTV integration** — infrastructure, not research.
- **AI/tech newsletters (AINews, RohanPaul, alphaXiv weekly)** — off-topic.

---

## Notes for the next report

- Chase down the Feng et al. *Ann Hum Genet* PDF to confirm the
  Zeng-citation locus and MR-Egger stability.
- Nature Medicine Vol 32 Issue 9 arrived same-day as this run —
  worth a dedicated triage pass before the next report if a manuscript
  task calls for it (particularly for rare-disease / precision-medicine
  headliners).
- The Hripcsak-family feeds (Ryan / Brandt / Hripcsak-cited-by /
  Hripcsak-new-related) converged 4-ways on a single fall-risk-SHAP
  paper this window, and 3-ways on the HSV-1-dementia paper. The
  overlap-suppression logic in the digest pipeline could probably fold
  cross-feed duplicates for these; noting the pattern for now.
- Twelve arxiv-digest crons produced 8 relevant papers this window
  (~0.67/day), a bit under the ~1.0/day rate of the July–August window.
  Suggests either genuine August–September submission slowdown or that
  the `--min-score 1` net is now over-suppressed by `seen.json` dedup.
