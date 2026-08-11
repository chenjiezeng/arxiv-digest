# Research digest report — 2026-08-11

Triage of research-related email + the GitHub `arxiv-digest` repo against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-08-08 12:36Z → 2026-08-11 12:00Z** (~3 days since the
last research-digest report, covering three `arxiv-digest` cron runs
(08-08, 08-10, 08-11) and three Google Scholar alert batches on 08-09,
08-10 (author feeds), and 08-11 (keyword feeds)).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-08.md` → `2026-08-11.md`) | 08-08 → 08-11 (10:30Z crons) | 3 daily runs. 08-08: 0 hits (all previously surfaced). 08-10: 0 hits (empty lookback). 08-11: 5 papers (UKB DXA-adjacent virtual cohort + CHIP semi-continuous + IPW clustering + VOICE + F1 SKIP). |
| Google Scholar alerts (keyword feeds, 08-11 batch) | 08-11 01:46Z | 13 keyword feeds fired: `APOL1`, `knowledge graph`, `UK Biobank`, `variant interpretation`/`variant classification`, `phenome wide association studies`, `electronic health records`, `mendelian diseases`, `autoimmune diseases`, `intitle:"clonal hematopoiesis"`, `rare diseases`, `drug repurposing`, `All of Us research program`, `Foundation models + electronic health records`. Densest signal: AoU (Cornell MR + Rujchanarong metabolic BC brain-mets + Son GLP-1 epilepsy) and PheWAS-of-SV (Li et al. KGGSV). |
| Google Scholar alerts (author feeds, 08-10 batch) | 08-10 06:32Z | 20+ author feeds fired: Chenjie Zeng (self), Lisa Bastarache (×2 keyword + cite), Daniel Kastner, Zhiyong Lu, Peter Szolovits (×2), Marinka Zitnik (×2), Stephen B Montgomery (×2), Kai Wang (×2), Jian Yang (×2), Konrad Karczewski (×2), Joshua C Denny (×2), Yuan Luo, George Hripcsak, Jonathan K Pritchard, Xingyi Guo, Miguel Hernán, Pascal Brandt, Patrick Ryan (×2), Vivek Natarajan, Tiffany J Callahan. Densest signal: Bastarache-adjacent (Olayinka AD PGS × rare variant, Onoja UKB post-AMI multimorbidity JAMIA), Chenjie Zeng self-related (Hysong AoU SDoH prediction, Xu proteomics 640k CVD, Rajueni multi-biobank dermatochalasis), Patrick Ryan (Kern REWARD drug-repurposing JAMIA + Liang SCCS vaccine safety). |
| Google Scholar alerts (keyword feeds, 08-09 batch) | 08-09 08:53Z | 8 keyword feeds fired: `Cystic fibrosis carriers`, `Guidance for estimating penetrance of monogenic ...`, `variant interpretation` / `variant classification`, `Foundation models + electronic health records`, `rare diseases`, `autoimmune disorders/diseases`, `intitle:"clonal hematopoiesis"`. Densest signal: Mikaeeli et al. CFTR p.Phe508del × lifestyle → bronchiectasis (direct CF thread hit) and Jiang et al. EHR-FM → CDS translation review. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated to first
> 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fifteen HIGH items surfaced this 3-day window, clustering into six knots:

**All of Us / biobank pharmacoepi cluster (5 items).** The AoU signal is
denser than usual this cycle — five different AoU studies fired.
Cornell et al. *Military Medicine* — Mendelian randomization of alcohol
consumption on depression / anxiety / PTSD / alcohol conditions using
AoU as the outcome cohort (military-relevant mental health).
Rujchanarong & Fujii *Neuro-Oncology Advances* — AoU longitudinal EHR
data for metabolic factors × brain metastasis in breast cancer
(directly overlaps Zeng's early-onset BC / metastasis lineage). Son
et al. *Ann Clin Transl Neurol* — GLP-1 RA safety & efficacy in adults
with comorbid epilepsy + T2D + obesity in AoU (matched-cohort design,
new-user framework) — perfect drug-class pharmacoepi in AoU with a
neurologic outcome. Pellesi & Guerzoni *Expert Opin Pharmacother* —
references a nested case-control of n=142,000 in AoU showing GLP-1 RA
exposure associated with lower substance-use-disorder onset (a
repurposing-signal-from-EHR win that fits both the pharmacoepi and the
drug-repurposing threads). Hysong et al. *Communications Health* —
practical considerations for SDoH-based disease prediction in AoU
(pinged the Chenjie-Zeng-related feed; this is the SDoH-augmented AoU
methods paper that anyone building AoU predictive models will need
to cite).

**PheWAS / phenotyping infrastructure cluster (2 items).**
Li et al. medRxiv/Research Square — **KGGSV**, high-performance
framework for phenome-wide association of structural variants in
biobank cohorts. This is a *scaling* paper for the underused SV-PheWAS
combination and slots directly into the PheWAS/phecode infrastructure
thread. Onoja et al. *JAMIA* — explainable temporal ML of
multimorbidity trajectories after AMI in 12,701 UK Biobank participants,
using dynamic-time-warping k-means + LDA topic modelling of diagnosis
sequences (cites phecodeX). Textbook chronic-disease-clustering paper
for the multimorbidity thread; the framework is portable to
post-diagnosis trajectories after MI, cancer, or any index event
across your AoU/UKB work.

**Composite risk / PGS × rare variant cluster (2 items).**
Olayinka et al. *Alzheimer's & Dementia* (Bastarache-related feed) —
Alzheimer's disease **PRS stratification aids rare-variant discovery**
in ADSP European-ancestry participants. Continues the "tails-and-
residuals" taxonomy of PGS as a discovery instrument (Souaiaia PGS
tails / Baya polygenic-deviation / Vazquez low-risk-group / this
paper's PRS-stratified enrichment). This should be added to the PGS
composite-risk sub-thread's core citation list. Sasson et al. arXiv
**LeDXA** (also surfaced in this window but detailed in the 08-08
report) — biological-age gap embedding whose value is modified by HRT
initiation — remains the exemplar for imaging-FM × modifiable-exposure
in biobank data.

**EHR-FM / EHR-representation cluster (3 items).**
Jiang et al. *Preprints 2026* — **"Translating EHR foundation models
into clinical decision support"** — a review-format piece surveying
the translational pipeline for EHR-FMs, data resources, model choices,
and CDS deployment. Reference-format piece for the *EHR foundation
models* thread (MEDS / EHRSHOT / MOTOR / CLMBR lineage). Zhu et al.
SIGKDD 2026 — **OneEHR** reproducible + AI-agent-ready longitudinal
EHR analysis toolkit (MIT SIGKDD track). Positions itself as the
model-comparison-and-reproducibility scaffold that MEDS / EHRSHOT don't
directly provide; fits the *knowledge representation in EHRs* thread's
representation-ablation-study interest. Chen et al. SIGKDD 2026 —
**HazardFlow** score-based energy modelling for enhanced health-status
representations from EHR (SIGKDD). Adjacent methods paper for EHR-FM
representation quality.

**Variant interpretation / ACMG cluster (3 items).**
Sulaiman & Oyeyemi Research Square — **concordance of automated
ACMG/AMP variant classification tools against ClinGen Evidence
Repository expert-curated assertions**. This is exactly the systematic
evaluation the *variant interpretation* thread has needed as a QC
citation for InterVar / CardioClassifier / Varsome / Franklin
comparisons. Boehler & Cheng *npj Genomic Medicine* — IMPACT
open-source workflow for phenotype-driven variant interpretation
(also flagged in the 08-08 report, appears again here via the 08-11
keyword-alert batch). Ellard et al. *Journal of Medical Genetics*
(British Society for Genetic Medicine) — updated **guidance on
managing incidental findings** during rare-disease genomic testing.
Reference-level policy document your ACMG-track needs.

**Drug repurposing / OMOP-native cluster (1 item; big).**
Kern et al. *JAMIA* (Patrick Ryan senior) — **REWARD** open-source
framework for identifying unknown benefits of existing medications
across administrative claims + EMR data to inform repurposing hypotheses.
This is the OMOP-CDM-native counterpart to the THBKG temporal KG paper
from the 08-08 report — one is graph-based, the other is real-world-
prescribing-signal-based, and both give explainable rationales. The
drug-repurposing thread now has *two* complementary reference tools
surfaced in successive weeks — worth stitching into a single review of
"explainable EHR-anchored drug-repurposing pipelines."

**CFTR / disease-specific cluster (2 items).**
Mikaeeli et al. *ERJ Open Research* — **lifestyle exposures × CFTR
p.Phe508del carriers → bronchiectasis risk** (smoking + alcohol
interaction with CFTR heterozygosity for non-CF pulmonary/GI disease).
This is a direct CF/CFTR thread hit and it's the "CFTR carrier
penetrance modified by environment" analogue to the "APOL1 penetrance
modified by N264K" story from the prior report. Portable framework
for BRCA1/2 carrier × environmental risk factor interactions. Öz et
al. *Pediatric Pulmonology* — systematic reanalysis of WES in
unsolved pediatric **primary ciliary dyskinesia** (adjacent to CF /
bronchiectasis phenotype thread) — data-driven reanalysis at
mid-cohort scale, complementing the Uria-Regojo et al. medRxiv 2026
paper flagged earlier in INTERESTS.md.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
by source, then by bucket.

### arxiv-digest surfacings (2026-08-08 → 2026-08-11)

Only the 08-11 run produced hits; 08-08 and 08-10 were empty
lookbacks (all previously surfaced or no matches).

#### METHODS-WATCH — Chen R, Zuo S, Stevens W, Pollack S, Xi W, Petito L, Zhao L, Zhang H. *Clustering Informed Inverse Probability Weighting Strategies for Causal Effect Estimation in Observational Studies.* arXiv 2608.09839v1 (stat.ME, 2026-08-10). Score 2.

Head-to-head comparison of standard IPW vs. cluster-specific IPW vs.
global IPW with cluster-membership covariate in observational settings
with latent cluster structure. Simulation grid: n = 100–500, cluster
structure present/absent, correctly vs. omitted covariate PS model.
Application to 966 breast-cancer patients on carboplatin using
generalized PS for dose–response (cycles → hypersensitivity risk).
Cluster-informed strategies reduced bias/MSE from omitted covariate
misspecification but neither uniformly dominated — clustered-IPW wins
on MSE when true latent clusters exist; global model wins on bias +
coverage at small n. Bookmark for the pharmacoepi thread where
cohorts have clear cluster structure (drug-class subtypes, hospital
site, or trial center) and PS model specification is uncertain. Small-
sample warning: none of these methods stabilizes below n≈200.

#### HIGH — Kevopoulos K, Moscoloni B, Alheit B, Beeche C, Chirinos JA, Heinlein A, Peirlinck M. *Flow-based conditional cardiac anatomy generation for virtual cohorts.* arXiv 2608.09460v1 (cs.LG, 2026-08-10). Score 2.

CAN-FLOW: two-stage conditional generative model on 2,208 healthy UK
Biobank subjects using normalizing flows to generate biventricular
cardiac anatomies conditioned on sex, age, BMI. Beats cVAEs across
regularization strengths, reproduces clinical phenotype distributions
and metadata-dependent trends. Directly serves the **digital-twins-from-
EHR/biobank** rising sub-thread (Zhang/Ideker/Oermann *Cell* 2026
framing) — this is the *cardiac* analogue to the DXA-JEPA LeDXA work
you flagged in 08-07. Practical use: virtual-cohort augmentation for
underrepresented subgroups (e.g. Black women in cardiac-imaging
studies) where UKB is Eurocentric. Watch for whether CAN-FLOW
preserves the *disease-outcome-relevant* geometric features (LV mass,
ejection fraction proxies) vs. only the aesthetic anatomy.

#### METHODS-WATCH — Bandreddi S, Zhang P, Kelly RL, Machiela MJ, Albert PS. *Comparing Tobit and Two-Part Hurdle Models for Semi-Continuous Longitudinal Data with an Application to Clonal Hematopoiesis.* arXiv 2608.09725v1 (stat.AP, 2026-08-10). Score 1.

Head-to-head comparison of mixed-effects Tobit vs. two-part hurdle
model for zero-inflated non-negative continuous longitudinal data,
applied to CHIP clonal fractions in the PLCO cohort. Result: Tobit is
a special case of hurdle when the binary process uses a probit link;
hurdle is more flexible/robust; use Tobit only when its assumptions
are scientifically plausible. Directly relevant to the **CHIP /
somatic mosaicism** thread — CHIP VAFs are exactly this kind of
zero-inflated semi-continuous longitudinal outcome. The Machiela
authorship (PLCO CHIP lineage) makes this a citation-ready methods
paper for any longitudinal CHIP / mLOY / mLOX / VEXAS clonal-dynamics
analysis. Portable to circulating tumor DNA fractions, mCA VAFs, and
telomere-length outcomes.

#### SKIP — Charpentier A. *From Rating Factors to Crash Mechanisms: A Multiscale Causal DAG Framework Linking Motor Insurance and Road Safety.* arXiv 2608.09441v1 (stat.AP, 2026-08-10). Score 1.

Off-topic (insurance / road safety); keyword hit on "motor."

#### METHODS-WATCH — Luo X, Tao Y, Zeng H, Wang S, Ouyang C, Zhu M, Liu K, Chen S, Liu J. *VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression.* arXiv 2608.08366v1 (cs.CV, 2026-08-08). Score 1.

Multimodal foundation model predicting single-cell expression from
H&E morphology using paired Xenium data; contrastive alignment on 23M
cells, then dual-branch prediction (direct regression + retrieval
from reference cells) with per-gene weighting. Off-thread for
clinical EHR work but methods-watch: the *retrieval-then-regression
per-feature-weighted* architecture is portable to any multimodal
EHR-FM problem where some outcomes are morphology/imaging-predictable
and others require retrieval from similar patients.

---

### Scholar alerts — keyword feeds (08-11 batch)

#### HIGH — Cornell L, Shukla T, McMillan K, Gdovin M, Smetana C, et al. *Estimating the Causal Effect of Alcohol Consumption on Military-Relevant Mental Health Conditions: A Mendelian Randomization Study Using the All of Us Research Program.* Military Medicine 2026 (`All of Us research program` keyword feed).

MR on AoU cohort estimating causal effects of alcohol on depression,
anxiety, PTSD, and alcohol conditions in a military-relevant framing.
Serves both the **AoU biobank** thread and the **drug-target /
exposure MR** sub-thread. Small nuance to check on full-text: whether
the MR instruments are the standard AUDIT / drinks-per-week SNPs
(rs1229984 ADH1B etc.), whether they stratified by military-service
history (self-report in AoU), and whether they addressed the AoU
alcohol-underreporting bias that plagues survey-based exposure
definitions. Portable framework for AoU MR studies of any behavioral
exposure with an EHR-defined psychiatric outcome (opioid × chronic
pain, cannabis × psychosis, coffee × sleep).

#### HIGH — Rujchanarong D, Fujii T. *Identifying Metabolic Factors Associated with the Incidence of Brain Metastasis in Breast Cancer Using All of Us Research Program Data.* Neuro-Oncology Advances 2026 (`All of Us research program` keyword feed).

AoU longitudinal EHR analysis of metabolic factors associated with
breast cancer brain metastasis (BCBM) incidence, univariate logistic +
regression build. Directly overlaps Zeng's early-onset BC / breast
cancer metastasis lineage. Read to see: (1) which specific metabolic
factors ranked (BMI trajectory, HbA1c, LDL, TG?), (2) whether they
stratified by ER/HER2 subtype, (3) how BCBM was ascertained (ICD-10
C79.31 vs. imaging notes vs. tumor registry). The methodological angle
matters for downstream AoU cancer-outcome work: BCBM is a rare
event in EHR, so ascertainment sensitivity strongly influences effect
sizes. Small nuance: AoU's tumor registry linkage is uneven across
sites, so effect estimates may be attenuated.

#### HIGH — Son H, Hwang I, Lee SW, Kim Y. *Safety and Efficacy of GLP-1 Receptor Agonists in Adults With Epilepsy, Obesity, and Type 2 Diabetes.* Annals of Clinical and Translational Neurology 2026 (`All of Us research program` keyword feed).

Retrospective cohort using AoU database of adults with **triple
comorbidity** (epilepsy + T2D + obesity) comparing GLP-1 RA new
initiators to matched non-initiators. Directly serves your active
**GLP-1 RA pharmacoepi** watchlist. The triple-comorbidity design is
interesting: it's a natural real-world-clinical-question about
whether GLP-1 use in patients with epilepsy is safe and effective for
metabolic outcomes, at a time when semaglutide/tirzepatide are being
prescribed broadly in T2D. Read to check: (1) whether seizure
frequency was captured (probably not in EHR alone) vs. status-
epilepticus admissions, (2) whether new-user active-comparator was
DPP-4i or SGLT2i or nothing, (3) whether the target-trial-emulation
frame is explicit. Portable template for CFTR-modulator persistence
studies with comorbid mental-health conditions.

#### MEDIUM — Pellesi L, Guerzoni S. *Medication-overuse headache in migraine: could GLP-1 receptor agonists treat the addiction-like phenotype?* Expert Opinion on Pharmacotherapy 2026 (`All of Us research program` keyword feed).

Editorial / mechanism piece proposing GLP-1 RA as therapy for
medication-overuse-headache addiction-like phenotype. Cites a *nested
case-control of n>142,000 adults with T2D or obesity in AoU showing
GLP-1 RA exposure was associated with substantially lower odds of
developing substance-use disorders*. That underlying AoU nested-CC
study is the real signal here — sounds like a Wang/Xu 2024-lineage
finding operationalized in AoU. Chase the primary citation. Direct
match to the **drug repurposing** thread's preferred angle
("EHR-based repurposing signals mined from real-world prescribing
and outcomes").

#### MEDIUM — Lees N. *Association of Fine Particulate Matter (PM2.5) Component Mixtures and Inpatient Hospitalization Incidence Among Chronic Kidney Disease (CKD) Participants in the All of Us Research Program, 2010–2019.* Research Square 2026 (`All of Us research program` keyword feed).

Environmental exposure × CKD hospitalization in AoU. Adjacent to the
APOL1/CKD thread if the exposure–outcome model included APOL1-
genotype stratification (unlikely). Read only if the environmental-
exposure × genetic-susceptibility framing (GxE for CKD) is being
extended.

#### HIGH — Li M, Peng W, Zhang L, Huang T, Wei C, Liu Z, Fang L. *A scalable framework enables phenome-wide association of structural variants in biobank cohorts.* Research Square 2026 (`phenome wide association studies` keyword feed).

**KGGSV** — high-performance framework bridging raw individualized
SV callsets to population-scale PheWAS in biobank cohorts. Addresses
computational bottlenecks that have kept SV-PheWAS underused compared
to SNP-based PheWAS. Fits the **PheWAS/phecode infrastructure**
thread and the **variant interpretation** thread simultaneously
(structural variants are the underserved category in ACMG-style
scoring). Small nuance to check: (1) which SV callers are supported
(Manta, DELLY, Sniffles?), (2) how CNV vs. indel vs. inversion vs.
translocation are handled distinctly, (3) whether phecodeX v1.1 is
supported for the phenotype axis. Portable to AoU (GATK-SV callsets)
and UKB WGS interim release SVs.

#### HIGH — Sulaiman MA, Oyeyemi BF. *Concordance of Automated ACMG Variant Classification with Expert-Curated Assertions: A Systematic Evaluation Using the ClinGen Evidence Repository.* Research Square 2026 (`variant interpretation` keyword feed).

Systematic evaluation of automated ACMG/AMP variant classifiers
against ClinGen Evidence Repository Expert-Panel–curated assertions.
This is exactly the reference-standard QC study the **variant
interpretation** thread has been missing. Read on full-text: (1)
which automated tools (InterVar, CardioClassifier, Franklin, Varsome,
ACMGuru, PSST?), (2) concordance metrics (Cohen's kappa, agreement
by criterion PVS1/PS3/PM1/etc.), (3) failure mode analysis. Should
become the citation of record whenever using an automated ACMG
classifier in a paper — sits alongside Nicora et al.'s 2022 comparison
and Rehm's 2023 assessment.

#### HIGH — Öz TH, Eyüboğlu TŞ, Aslan AT, Kula N, Kayhan G. *Systematic Reanalysis of Whole-Exome Sequencing in Genetically Unsolved Pediatric Primary Ciliary Dyskinesia.* Pediatric Pulmonology 2026 (`variant interpretation` keyword feed).

Systematic reanalysis of WES in genetically unsolved pediatric PCD
cases. Directly fits the **rare disease** thread's *data-driven
reanalysis of unsolved cases* rising sub-thread (Uria-Regojo et al.
medRxiv 2026 as the reference). PCD is a bronchiectasis-adjacent
ciliopathy so this also has weak overlap with the CF/CFTR
bronchiectasis-outcome thread. Read for the reanalysis workflow (which
databases updated, which classifier rerun) — portable to CF, BRCA,
hereditary-cancer-panel reanalysis.

#### HIGH — Lim MPHRS, Zhang PDY, Lim BSTST, Goh MSM, et al. *Precision Nephrology in Practice: National Clinical Implementation Pilot of Genomic Testing for Kidney Diseases and Its Clinical Impact in Singapore.* Kidney Medicine 2026 (`variant interpretation` keyword feed).

National clinical implementation pilot of genomic testing for
monogenic kidney disease in Singapore. Serves both the **APOL1 /
CKD** thread (national-scale genomic testing infrastructure for
kidney disease) and the **variant interpretation** thread. Read to
compare: diagnostic yield, cost per diagnosis, downstream clinical
actionability, and whether ancestry-stratified testing panels (South
Asian, Chinese, Malay) mattered. This mirrors the Genomics England /
100,000 Genomes / eMERGE-lineage implementation-science work that
should inform the AoU return-of-results discussion.

#### METHODS-WATCH — Sun SD, Liu J, Xu P, Hu Y, Zhang MJ, Zhang J. *MUGO: Differentiable Combinatorial Optimization for Causal Variant Discovery in the Non-coding Genome.* SIGKDD 2026 (`variant interpretation` keyword feed).

Differentiable combinatorial optimization for causal variant
discovery in the non-coding genome. Adjacent to the **fine-mapping /
colocalization** sub-thread flagged in prior reports (CIT-Lasso,
CAVIAR/FINEMAP lineage). Bookmark for methods comparison; not
immediately actionable unless a non-coding fine-mapping pipeline is
being built.

#### HIGH — Xu Y, Loesch D, Taylor HJ, Keating MF, Ritchie SC, et al. *A proteome-wide association study of cardiovascular diseases in 640,000 participants of multiple ancestries.* medRxiv 2026 (Chenjie Zeng cited-by feed).

**640,000-participant multi-ancestry proteome-wide association
study of CVD.** Genetic imputation models for 2,594 proteins across
ancestries. This is a landmark-scale multi-ancestry proteomics paper
that hits the **multi-omics-augmented PRS** and **drug-target MR**
sub-threads directly. Combined with the Zhong et al. proteome-wide MR
paper from the 08-08 report, cross-population proteomics for CVD is
having a moment. Read for: (1) which proteins had highest
cross-ancestry imputation accuracy, (2) which CVD sub-phenotypes were
most amenable (AF, HF, MI, PAD), (3) whether the proteome-PGS
outperforms genotype-alone PGS.

#### HIGH — Rajueni K, Koskimaki F, Salo V, Pasanen A, Sliz E, et al. *Multi-biobank genome-wide association study of dermatochalasis implicates genes involved in skin biology and morphology.* medRxiv 2026 (Joshua Denny + Chenjie Zeng feeds).

Multi-biobank GWAS meta-analysis of dermatochalasis (n=13,200 cases)
across three cohorts. On-thread for the **multi-biobank GWAS**
methodology (this is exactly the FinnGen-style meta-analysis of
underserved phenotypes your PheWAS thread values). Read for cohort
composition (probably FinnGen + Estonian Biobank + UKB or BioVU) and
whether the dermatochalasis phenotype was defined via ICD-10 H02.83
+ CPT 15822 or via image-derived measures.

#### MEDIUM — Yang Y, Liu Y, Li X, An Z, Li S, Q… - UK Biobank. *Metabolomic profiling identifies metabolically heterogeneous phenotypes with divergent cardiovascular and diabetes risk: metabolomic characterization from the UK biobank.* 2026 (`UK Biobank` keyword feed).

UKB Nightingale NMR metabolomics × latent metabolic phenotype
clustering with divergent CVD/T2D risk. Fits the
**chronic-disease-clustering / multimorbidity** thread and the
**multi-omics-augmented PRS** thread. Read to see whether cluster
labels reproduce Ala-Korpela's Nightingale-lineage metabolic subtypes
(atherogenic dyslipidemia, small-HDL, etc.).

#### MEDIUM — Poudel B, Susztak K. *Response by Poudel and Susztak to Letter Regarding Article, "Cell-Specific Inducible Human APOL1 Risk Variant Expression in Mice Causes Hypertension and Renal Injury."* Circulation 2026 (`APOL1` keyword feed).

Author response to letter about the Poudel/Susztak APOL1 mouse
model. Adjacent to the **APOL1** thread; read only for the mechanism
discussion around cell-specific vs. tissue-wide APOL1 expression and
whether it affects the human-genetic interpretation. Low priority
compared to the APOL1 primary papers from the 08-08 report
(Gaheer/Lanktree proteomic score + Chen N264K + Kim/Lee inhibitor).

#### MEDIUM — Chen Y, Chen X. *Genetic evidence for a causal role of depression in late-onset Alzheimer disease: A Mendelian randomization study.* Medicine 2026 (`mendelian diseases` keyword feed).

MR study of depression → AD. Adjacent to the **PGS × psychiatry**
thread (Zhang AoU MDD PRS × wearable, Olayinka AD PRS × rare variant
below). Read for the instrument choice and whether pleiotropy through
sleep/exercise phenotypes was addressed.

#### LOW — Han B, Xu Y, Li R, Huang PG, Chen ZS, Xiao M. *Drug repurposing: Losartan reverses cancer drug resistance via microenvironment reprogramming.* Genes & Diseases 2026 (`drug repurposing` keyword feed).

Mechanistic drug-repurposing hypothesis paper. Off-thread for the
EHR/biobank-focused repurposing lens.

#### LOW — Okazawa-Sakai M, Fujisawa T, Chiyoda T, Yagi H, et al. *cfDNA-inferred putative clonal hematopoiesis during first-line platinum-to-PARP inhibitor maintenance in ovarian cancer.* Journal of Gynecologic Oncology 2026 (`intitle:"clonal hematopoiesis"` keyword feed).

cfDNA-inferred CHIP during PARP-inhibitor maintenance in ovarian
cancer. Read only if extending the **CHIP × cancer-therapy** angle;
otherwise off-your-EHR-cohort-focused CHIP interest.

#### LOW — Dollfus H, Arzimanoglou A, Evangelista T, Graessner H, et al. *Crisis readiness for rare disease populations: learnings and recommendations by the European Reference Networks.* Lancet Regional Health 2026 (`rare diseases` keyword feed).

ERN policy piece. Low signal for the technical rare-disease thread.

---

### Scholar alerts — author feeds (08-10 batch)

#### HIGH — Hysong MR, Manning AK, Green MD, Konigsberg IR, et al. *Practical considerations for social determinant-based disease prediction in the All of Us research program.* Communications Health 2026 (Chenjie Zeng related-research + Lisa Bastarache cited-by feeds).

Methods-cum-guidance paper for how to incorporate SDoH into disease
prediction models on AoU. Cites the phenome-wide association studies
foundational literature. This should become a *methods reference* for
anyone (including your team) building AoU predictive models with
SDoH inputs. Read for: (1) which SDoH domains (housing, food security,
neighborhood socioeconomics, discrimination) were operationalized,
(2) whether they used the AoU Basics-survey items or ZIP-linked area-
level indices, (3) what happens to model calibration by
race/ethnicity when SDoH is added vs. excluded. Direct match to the
**EHR-linked biobank** thread + the **ML for precision health**
thread.

#### HIGH — Olayinka O, Farrell JJ, Zhu C, Khurshid Z, Martin ER, et al. *Stratification by a polygenic risk score of common variation aids in Alzheimer's disease rare variant discovery.* Alzheimer's & Dementia 2026 (Bastarache related-research feed).

**PRS-stratified rare variant discovery** in the AD Sequencing
Project (ADSP). Method: build AD PRS for European-ancestry
participants, then discover rare-variant associations in PRS-defined
strata. This directly extends the **PGS composite-risk / PGS-tails**
sub-thread taxonomy — pairs with Souaiaia (PGS tails), Vazquez
(low-risk-group), Baya (polygenic-deviation) as the fourth cornerstone.
The unifying idea: PRS is not just a predictor; it's a stratifier
that changes the yield and enrichment of rare-variant screens. Direct
citation for anyone extending the PRS-tails design to AoU / UKB /
BioVU. Read on full-text: which PRS strata were used (top/bottom 5%
vs. quintiles), what the rare-variant enrichment factor was, and
whether the pattern held for APOE ε4 stratification.

#### HIGH — Onoja A, Elomaa K, Whetton AD, Geifman N. *Explainable temporal machine learning of multimorbidity trajectories after acute myocardial infarction: complementing clinical risk scores with mechanistic phenotypes.* JAMIA 2026 (Bastarache cited-by feed via phecodeX).

n=12,701 UK Biobank participants with post-AMI multimorbidity
trajectories. Dynamic Time Warping k-means clustering on diagnostic
sequences + Latent Dirichlet Allocation for cluster themes +
CatBoost/XGBoost multiclass classifiers. Cites phecodeX. Textbook
**chronic disease clustering / multimorbidity** paper for the
INTERESTS.md thread. The DTW+k-means+LDA stack is a portable pipeline
for post-index-event trajectories — could be re-run on
post-cancer-diagnosis, post-stroke, post-COVID cohorts. Watch: (1)
how they handled left-censoring at AMI (medications pre-existing?),
(2) whether phecodeX-mapped diagnoses beat raw ICD-10 for cluster
interpretability, (3) how biological (Olink? metabolomics?) features
enriched the mechanistic phenotype interpretation.

#### HIGH — Kern DM, Bohn J, Gilbert JP, Knoll C, Ryan PB. *REWARD—an open-source framework for identifying the unknown benefits of existing medications to inform drug discovery, development, and repurposing.* JAMIA 2026 (Patrick Ryan author feed).

Ryan-lab OMOP-native tool for mining real-world outcomes data
(claims + EMR) to identify unknown benefits of already-approved
medications. Directly serves the **drug repurposing** thread's stated
preference for "EHR-based repurposing signals mined from real-world
prescribing and outcomes; causal-inference framings of off-label use."
This is the OMOP-CDM-side counterpart to the THBKG temporal-KG paper
(08-08 report) — one is knowledge-graph-based with year-stamped
evidence, one is prescribing-outcome-based with real-world signal.
Both are on-thread; both have explainable output. Consider a paired
review of the two as a "spectrum of EHR-anchored drug-repurposing"
frame. Read on full-text: which OMOP concept sets / outcome
definitions REWARD ships with, and whether the framework integrates
target-trial emulation for candidate hypothesis testing.

#### MEDIUM — Liang C, Chilson EL, Wu J, Kelly SP, Liu Q, et al. *Can We Compare Adverse Event's Attributable Risk Using a Self-Controlled Case Series Design for Vaccine Safety? A Guillain-Barré Syndrome Use Case.* [Journal TBD] 2026 (Patrick Ryan related-research feed).

SCCS design for vaccine-adverse-event surveillance (GBS after
vaccination). Methods-watch for the **pharmacoepi** thread — SCCS is
underused compared to cohort designs in vaccine studies, and this is
a good comparative use case. Bookmark for the pharmacovigilance /
adverse-event methods shortlist.

#### MEDIUM — Villa A, Eadie AL, Synnott D, Romanò R, Piffoux M, et al. *AI-based augmentation of oncology clinical trials.* Nature Reviews Clinical Oncology 2026 (Miguel Hernán cited-by feed).

Review of AI/ML use in oncology trials (enrollment, endpoint
adjudication, synthetic controls). Adjacent to the **causal
inference in RWE** thread — synthetic controls from EHR/registry
data is a Hernán-adjacent methods area. Read for the RWE-synthetic-
control section.

#### METHODS-WATCH — Cooper LN, Beauchamp AM, Ingle TA, Diaz MI, et al. *Antimicrobial Resistance Microbiological Dataset (ARMD-UTSW): Electronic Health Record Based Data for Research.* Scientific Data 2026 (George Hripcsak related-research feed).

New public EHR-based AMR microbiology dataset. Bookmark for the
**EHR phenotyping / OMOP** thread as a template for building
purpose-built EHR datasets from a single institution and releasing
under governed access. Adjacent to the antimicrobial-stewardship
target-trial-emulation opportunity.

#### METHODS-WATCH — Tiwari V, Jha S, Geddam R, Awais M, Khan MA, et al. *Deconstructing the Interoperability Stack: A Comparative Technical Analysis of HL7 v2, CDA, and the FHIR Resource Framework.* Computational and Structural Biotechnology 2026 (Pascal Brandt related-research feed).

Comparative technical analysis of HL7v2 / CDA / FHIR. Bookmark for
the **knowledge representation in EHRs** thread's *interoperability
standards and their representational consequences* sub-topic —
useful reference companion to Lemieux et al. *JAMIA Open* 2026-07 you
already track.

#### LOW — Ong AQC, Ang CS, Bojic I, Johnson CL, Aggour H, et al. *Artificial intelligence in cardiovascular care: a systematic review and meta-analysis of randomised controlled trials.* eClinicalMedicine 2026 (Vivek Natarajan cited-by feed).

Systematic review of RCTs of AI in CV care. Low signal for the
methods threads (RCT-of-AI level, not primary tool development).

#### LOW — Peet CJ, Orchard T, Cruz CHB, Hernandez-Cordero A, et al. *A TBK1 mutation disrupting IRF3 activation is associated with familial recurrent myopericarditis.* Frontiers in Immunology 2026 (Konrad Karczewski cited-by feed).

Single-family rare-variant myopericarditis paper. Low signal unless
extending the autoinflammatory-genetics work.

#### LOW — Grentzinger V, Artesi M, Palmeira L, Renotte N, et al. *Long Read Sequencing of Filaggrin identifies extensive copy number variation in exon 3 and detects rare loss of function variants.* JID 2026 (Kai Wang + Karczewski related-research feeds).

Filaggrin CNV/LoF variant characterization via long-read sequencing.
Off-thread unless the atopic-dermatitis PheWAS angle is being pursued.

#### LOW — Zhu Q, Jing Y, Zheng Y, Khan MZ, Liu A, Peng Y, et al. *Genome-Wide Identification and Characterization of the Wnt Gene Family in Donkey (Equus asinus): Phylogenetic Analysis and Expression Profiling.* [Journal TBD] 2026 (Tiffany J Callahan related-research feed).

Off-species (donkey Wnt family GWAS). Low signal for human-EHR-focused
work.

#### LOW — Yan L, Qiu Y, Mo Z, Li M, Huang X, Gao Y, Yan B, Hu Q, et al. *Identification of novel loci regulating circulating melatonin and its causal relationship with hypertension.* Human Genetics 2026 (Jian Yang cited-by feed).

Melatonin GWAS + MR → hypertension. Off-thread unless a chrono-
biology MR angle is being pursued.

#### LOW — Yang F, Tang Q, Wang X, Chen J, Li Y, Liu W, Ma B, et al. *A Vicious Cycle of Microglial Dysfunction: Bridging Synaptic Pruning and Neuroinflammation Across the Neurodevelopmental Continuum.* Frontiers in Aging Neuroscience 2026 (Kai Wang cited-by feed).

Neurodevelopmental review; off-thread.

#### LOW — Zhang Z, Lyu J, Bai Y, Guo Z, Bo Q, Liu K, Dai X. *OTULIN: A Master Regulator of Linear Ubiquitin Homeostasis in Immune Signaling, Inflammation, and Disease.* Frontiers in Immunology 2026 (Daniel Kastner cited-by feed).

OTULIN autoinflammation review. Off-thread unless extending the
autoinflammatory-disease genetics work (adjacent to VEXAS / DADA2 but
low signal in isolation).

#### LOW — Kim Y, Gu K, Park C, Park C, Schmidgall S, Heydari AA, et al. *Capable language models can outgrow the benefits of collaboration.* Nature Machine Intelligence 2026 (Zhiyong Lu related-research feed).

Multi-agent LLM scaling result. Adjacent but off-thread for clinical
LLM-agent work.

---

### Scholar alerts — keyword feeds (08-09 batch)

#### HIGH — Mikaeeli S, Zheng TM, Li PZ, Nakanishi T, Soulé A, et al. *Lifestyle exposures and bronchiectasis risk in CFTR p.Phe508del carriers.* ERJ Open Research 2026 (`Cystic fibrosis carriers` keyword feed).

**CFTR p.Phe508del heterozygosity × smoking + alcohol → non-CF
bronchiectasis + GI disease.** Direct hit on the **CFTR / cystic
fibrosis** thread. This is the *carrier penetrance modified by
environment* analogue to the APOL1 modifier-variant story from the
08-08 report. The design is a GxE study operationalized in a biobank
(likely CARTaGENE or UKB based on the author list) — read to see
which biobank, sample size of Phe508del carriers, and whether the
effect held in Phe508del compound heterozygotes vs. simple
heterozygotes. Portable framework for CFTR-modulator eligibility
studies and for BRCA1/2 carrier × environmental risk factor
interactions. Direct citation for CFTR-carrier phenotype work in AoU.

#### HIGH — Jiang Y, Dai R, Zhang Z, Gao S, Chen Y, Du Y, Liu J, et al. *Translating Electronic Health Record Foundation Models into Clinical Decision Support.* Preprints 2026 (`Foundation models + electronic health records` keyword feed).

Review-format survey of the translational pipeline for EHR foundation
models: data resources, model architecture choices, CDS deployment
patterns, and translational bottlenecks. Fits the **EHR foundation
models** thread as a reference/framing citation. Read alongside
Zhang/Ideker/Oermann *Cell* 2026 digital-twins framing paper. This
should become a top-of-thread citation for anyone framing an EHR-FM
paper's motivation.

#### HIGH — Ellard S, Hanson H, Cassidy EJ, Thomson K, Durkie M, et al. *The British Society for Genetic Medicine guidance on managing incidental findings identified during rare disease genomic testing.* Journal of Medical Genetics 2026 (`Guidance for estimating penetrance of monogenic ...` cited-by feed).

BSGM policy guidance on incidental findings during rare-disease
genomic testing. Directly relevant to the **variant interpretation
(ACMG/ClinGen)** thread and to any return-of-results discussion
around AoU / MVP / eMERGE. Read for: (1) how they operationalize
penetrance estimation for reporting, (2) which gene panels count as
"actionable" secondary findings, (3) whether they align with
ACMG SF v3.x. Should be added to the ACMG-track references shortlist.

#### METHODS-WATCH — Zhu Y, Wang Z, Gu L, Sui D, Wang Y, Harrison E, Fu T, et al. *OneEHR: Reproducible and AI Agent-Ready Longitudinal EHR Analysis Toolkit.* SIGKDD 2026 (`Foundation models + electronic health records` keyword feed).

OneEHR positions itself as the reproducibility + agent-ready
scaffold for longitudinal EHR research — a layer above MEDS/EHRSHOT
that standardizes model comparison. Bookmark for the **EHR foundation
models** thread as a benchmarking-infrastructure candidate. Read to
see: (1) which cohorts are supported (MIMIC-IV, eICU, MEDS-EHRSHOT,
AoU?), (2) which prediction tasks are standardized, (3) whether it
integrates with the LangChain / AutoGen agent frameworks that the
LLM-clinical-agent thread cares about.

#### METHODS-WATCH — Chen Q, Li X, Zhang Y, Wang M. *HazardFlow: Enhancing Health Status Representations via Score-based Energy Modeling.* SIGKDD 2026 (`Foundation models + electronic health records` keyword feed).

Score-based energy modelling for enhanced EHR health-status
representations. Bookmark for the **EHR foundation models** thread's
representation-quality sub-topic. Read to see how it compares to
diffusion-based or contrastive representation learning on longitudinal
EHR.

#### MEDIUM — Li A, Casiraghi E, Rousu J. *FedMed: Federated Learning-Based Personalized and Safe Medication Recommendation.* SIGKDD 2026 (`Foundation models + electronic health records` keyword feed).

Federated medication recommendation on EHR datasets. Adjacent to the
**federated / privacy-preserving EHR causal analytics** rising
sub-thread (paired with Burkhart et al. from the 08-08 report). Read
to compare federation protocols and whether medication safety metrics
were operationalized (contraindication rate, drug-drug interaction
rate).

#### METHODS-WATCH — Sun SD, Liu J, Xu P, Hu Y, Zhang MJ, Zhang J. *MUGO: Differentiable Combinatorial Optimization for Causal Variant Discovery in the Non-coding Genome.* SIGKDD 2026 (`variant interpretation` keyword feed; also in 08-11 batch).

Duplicated from 08-11 batch — same paper hit two consecutive keyword
feeds. Same triage as above.

#### MEDIUM — Schwengber WK, Sanders J, Pinteric A, Armitage L, et al. *Hematologic Consequences of Radiopharmaceutical Therapy: From Clonal Hematopoiesis to Therapy-Related Myeloid Neoplasms.* Journal of Nuclear Medicine 2026 (`intitle:"clonal hematopoiesis"` keyword feed).

CHIP → t-MN in the context of radiopharmaceutical therapy (177Lu-PSMA
and related). Combines with the Okazawa-Sakai cfDNA-CHIP × PARP-i
paper in the same window — CHIP as a *therapy-modulated somatic
mosaic* is having a moment. Read for the incidence estimate and
whether pre-treatment CHIP screening was proposed as a decision tool.

#### MEDIUM — Wang J, Yang J, Guo R. *Stepwise Diagnostic Evaluation of Chinese Large Language Models: Comparative Study of Common and Rare Diseases.* Journal of Medical Internet Research 2026 (`rare diseases` keyword feed).

LLM diagnostic benchmark on Chinese common + rare diseases.
Adjacent to the **auditable HPO-driven diagnostic benchmarks** rising
sub-thread (GraphRareBench as the reference). Read to see whether
ranking-vs-evidence-coverage was separated and whether Chinese HPO
mapping was audited.

#### LOW — Hu CJ, Zeng XF. *Chinese guidelines on clinical application of autoimmune bullous diseases related autoantibodies (2026).* Zhonghua Nei Ke Za Zhi 2026 (`autoimmune disorders/diseases` keyword feed).

Chinese autoimmune bullous disease guideline. Off-thread.

---

## Cross-cutting observations for this window

1. **AoU has a very dense presence this cycle** — 5 different papers
   flagged from AoU across MR (Cornell), pharmacoepi (Son, Pellesi
   citing another AoU study), oncology (Rujchanarong), prediction
   methodology (Hysong), and environmental exposure (Lees). This is
   consistent with AoU maturing as a publication platform.

2. **PGS-as-discovery-instrument taxonomy now has a fourth cornerstone.**
   Adding Olayinka *Alz & Dementia* (PRS-stratified rare-variant
   discovery in AD) to Souaiaia (PGS tails) + Vazquez (low-risk-group)
   + Baya (polygenic-deviation) completes a compact citation
   quartet — worth documenting once in a methods review.

3. **The drug-repurposing thread now has paired reference tools.**
   THBKG (temporal biomedical KG with decision-aligned evaluation,
   flagged 08-08) + REWARD (OMOP-native real-world-benefit-mining
   framework, flagged 08-10) span the "graph-based, evidence-aligned"
   vs. "real-world-outcome-based" halves of explainable drug
   repurposing. A short review stitching them would be timely.

4. **CFTR + APOL1 are on the same modifier-variant-and-modifiable-
   environment arc.** Chen et al. APOL1 p.N264K rescue (08-08 report)
   + Mikaeeli et al. CFTR × smoking/alcohol (08-09) both instantiate
   the *carrier penetrance modified by X* framing — X = genetic
   modifier for APOL1, X = environmental modifier for CFTR. Both are
   templates for BRCA1/2 penetrance-modifier work.

5. **Structural variant PheWAS is finally getting infrastructure.**
   KGGSV (Li et al. Research Square) is the first SV-focused
   PheWAS-scaling framework surfaced this cycle. Watch whether AoU's
   GATK-SV callset gets deployed against it before UKB WGS SVs do.

## What's NOT in the report

- **NCBI My-NCBI What's-New batches** — none fired in the searched
  window; last batch was in the 08-02 report.
- **bioRxiv / medRxiv Subject Collection Alerts** — none surfaced;
  the medRxiv items above (Xu proteomics, Rajueni dermatochalasis)
  came via the Chenjie Zeng / Denny author cross-reference feeds.
- **Substack / newsletters** — the AI News, State AI, and Paperclip
  emails in this window were noted but none had biomedical content
  that crossed the on-thread threshold.
- **arxiv.org daily category mailings** (raw `cs`, `stat.AP`,
  `q-bio` mailings from no-reply@arxiv.org) — upstream source for
  the arxiv-digest pipeline; individual papers surfaced via the
  digest are covered in the arxiv-digest section above.

## Next steps to consider

1. **Chase the primary AoU nested case-control that Pellesi &
   Guerzoni cite** — a GLP-1 RA × SUD onset study in n=142k in AoU
   is directly on the drug-repurposing + pharmacoepi thread and
   sounds high-signal.
2. **Bundle the KGGSV + THBKG + REWARD trio** into a short thread
   update on infrastructure-for-explainable-EHR-genomics-repurposing.
3. **Add Sulaiman & Oyeyemi ACMG-vs-ClinGen concordance** to the
   variant-interpretation citation shortlist as a QC reference.
4. **Read Rujchanarong & Fujii AoU BCBM full-text** — closest to
   Zeng's cancer lineage in this cycle and worth checking for AoU
   tumor-registry ascertainment behavior.
5. **Consider requesting a short KGGSV feature-comparison** against
   REGENIE-SV / SAIGE-QT for SV-PheWAS in AoU; the underserved
   phenotype × structural variant combination is a plausible AoU-first
   study.

_Report generated 2026-08-11 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-11 → next scheduled run._
