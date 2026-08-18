# Research digest report — 2026-08-17

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-08 12:36Z → 2026-08-17 12:40Z** (~9 days since the
last research-digest report, covering ten arxiv-digest cron runs and
three Google Scholar alert batches on 08-15, 08-16, and 08-17).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-08.md` → `2026-08-17.md`) | 08-08 → 08-17 daily crons | 10 daily runs. 08-08, 08-10, 08-14, 08-15, 08-16, 08-17: 0 relevant papers (dry). 08-11: 5 papers (largest batch — clustering IPW, CAN-FLOW UKB DXA generation, Tobit-vs-hurdle clonal hematopoiesis, DAG × motor insurance, VOICE H&E-to-scRNA FM). 08-12: 2 papers (egg-computation LLM-assisted g-computation + perinatal pharmacoepi TTE). 08-13: 1 paper (Inverse Confounding Analysis sensitivity method). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest`, `chenjiezeng`, and `arxiv` returned zero threads in the last 30 days. The `arxiv-digest` pipeline commits its output to the local repo (this branch) rather than emailing PR / cron notifications. Digest files under `digests/` are the primary artifact; the on-disk repo *is* the arxiv-digest feed. |
| Google Scholar alerts (keyword feeds, 08-17 batch, 05:05Z) | 08-17 05:05Z | 10 keyword feeds fired simultaneously (`variant interpretation`/`variant classification`, `autoimmune diseases`, `electronic health records`, `UK Biobank`, `knowledge graph`, `drug repurposing`, `rare diseases`, `All of Us research program`, `mendelian diseases`, `Foundation models + electronic health records`). |
| Google Scholar alerts (author + citation feeds, 08-16 batch, 21:35Z) | 08-16 21:35Z | 20+ author / citation feeds fired: Chenjie Zeng (self), Lisa Bastarache (×2: new-related + citations-to), Joshua C Denny (citations-to), Kai Wang (×2: new-related + citations-to), Konrad Karczewski (×2: new-related + citations-to), Peter Szolovits (×2), Marinka Zitnik, Zhiyong Lu, Tiffany J Callahan, Jian Yang (×2: new-related + citations-to), Stephen B Montgomery (citations-to), Yuan Luo (citations-to), Daniel Kastner (citations-to), George Hripcsak (new articles + new-related + citations-to via Pascal Brandt feed), Mark Daly, David Baker, Vivek Natarajan (citations-to), Bing Ren, Patrick Ryan. |
| Google Scholar alerts (08-15 batch, 18:09Z + 20:57Z) | 08-15 18:09Z–20:57Z | 8+ feeds fired: George Hripcsak, Patrick Ryan, Peter Szolovits, Kai Wang, Tiffany J Callahan, Marinka Zitnik, Vivek Natarajan (citations-to), plus `knowledge graph` keyword. Densest signal from the Szolovits + Callahan + Ryan cluster (EHR-FM adjacent) and one epilepsy-phenotyping-with-transformers paper. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Ten HIGH items surfaced this window, clustering into four knots:

**Agentic / LLM-assisted causal inference cluster (2 items).** Vossler
et al. arXiv 2608.10339 — **egg-computation** (expert-guided
g-computation) uses Gantt-chart representations of patient trajectories
with an LLM pipeline that scales expert reasoning; validated on eleven
hospital QI interventions against human experts at an urban safety-net
hospital. This is the **exact "agentic / human-in-the-loop
observational-causal-inference pipeline" rising sub-thread** you added
to INTERESTS.md — an LLM does the trajectory-mapping busywork while the
human owns identifying assumptions. Directly comparable to `oci-agent`
Chou/Kallus. Wood et al. arXiv 2608.11108 — perinatal pharmacoepi TTE
tutorial for treatment-decision-driven time-zero specification (T2D
pregestational treatment as the running example). This is the reference
methods paper for the **early-pregnancy time-zero-selection problem**
that has bedeviled every AoU / UKB pregnancy pharmacoepi analysis on
your watchlist (immortal time from imperfect pregnancy-onset dating).

**LLM-assisted computable phenotyping cluster (3 items).** Chang et al.
*npj Digital Medicine* 2026 (Szolovits feed) — automated epilepsy /
seizure-type phenotyping with transformer LMs; a canonical example of
the **NLP / LLM extraction from clinical notes for phecode assignment**
sub-thread. Angell et al. IEEE 2026 (Kai Wang citations-to feed) —
Autism Spectrum Disorder computable phenotyping using EHR with
*verified* autism diagnoses (chart-review anchor). This is the
gold-standard-anchored validation study your **EHR phenotyping / OMOP**
thread wants to propagate — most computable-phenotype papers ship
without a chart-review ground truth. Pérez-García et al. *iScience*
2026 (Kai Wang new-related feed) — text-mining + ontology (HPO-based)
literature retrieval for rare-disease diagnosis; bridges the
**KG / ontology** and **rare disease** threads.

**Genetic-epi + biobank cluster (3 items).** Abner, Johnson, Vujkovic,
Daly et al. *Nature* 2026 (Karczewski + Mark Daly feeds, dual hits) —
genetic variants affect *diurnal* glucose levels throughout the day,
using UKB CGM-like data. This turns a scalar HbA1c GWAS into a
**time-of-day function-valued exposure GWAS**, and pairs perfectly with
the Ciardulli et al. functional-propensity-score paper from the 08-08
report. Reads as an anchor for the **PGS × modifiable-environment**
thread (chronotype × PGS). Kevopoulos et al. arXiv 2608.09460 — CAN-FLOW
generates conditional cardiac anatomies from 2,208 UKB CMR subjects
(sex × age × BMI conditioning); template for **imaging FMs on
biobank data** and for **virtual-cohort in-silico trial** work.
Bandreddi et al. arXiv 2608.09725 — Tobit vs. two-part hurdle models
for **longitudinal clonal hematopoiesis clonal-fraction data with excess
zeros** (PLCO cohort). Direct methods addition to the **CHIP / VEXAS /
LOY somatic-mosaicism** thread; every AoU / UKB WGS-derived CHIP-VAF
analysis needs to choose one of these two model families.

**Pharmacoepi + variant-interpretation infrastructure cluster (2 items).**
Reho et al. *Annual Review of Pharmacology and Toxicology* 2026
(Hripcsak new-articles feed) — **Pharmacoexposomics**: the environmental
complement to pharmacogenomics; formal framing of drug-exposome
interaction as a first-class variable in precision-medicine studies.
This slots directly into the **PGS × exposure / environment
interactions** rising sub-thread (Nagpal & Gibson lineage) but on the
*drug-effect* side rather than the *disease-risk* side. Perfect
theoretical scaffold for the CFTR-modulator × environment,
GLP-1 RA × diet, HRT × HRT-formulation-and-route work you've been
prototyping. Mitev *Frontiers in Genetics* 2026 (`variant interpretation`
keyword feed) — methodological framework for **real-world performance
studies of clinical variant-classification platforms at early
organizational stages**. Reference paper for the **ACMG / ClinGen
variant curation** thread; especially useful if you're evaluating
InterVar / CancerVar / Franklin / VarSome in a health-system deployment
context.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-08 → 2026-08-17)

#### HIGH — Vossler P, Ouyang J, Guo FR, Huang A, Shojaie A, Zier L, Xia F, Feng J. *Expert-Guided g-computation with Large Language Models for Estimating Causal Effects on Timings: Applications to Hospital Quality Improvement.* arXiv 2608.10339v1 (stat.ME, 2026-08-11). Score 2.

Introduces **egg-computation** (expert-guided g-computation): connects
the Gantt charts clinicians already use to map patient trajectories to
formal causal DAGs, then estimates the average time saved by a
candidate QI intervention using a g-computation variant that seeks
expert input only for components unidentifiable from data. An
LLM-assisted pipeline scales up the expert-reasoning step
(mapping trajectories, proposing DAG edges). Validated on eleven
candidate QI interventions at an urban safety-net hospital; LLM-generated
graphs and time-saving estimates were highly concordant with the
human-expert reference. This is the **direct-hit paper** for the
"agentic / human-in-the-loop observational-causal-inference pipelines"
rising sub-thread in INTERESTS.md (line ~52). Directly comparable to
Chou/Kallus `oci-agent` (arXiv 2607.22443); egg-computation lives on
the *timing/pathway* estimand side while `oci-agent` lives on the
covariate-balance / PS-trimming side — together they carve out a
credible "LLM does the mechanical steps, human owns the identification
assumptions" division of labor. Portable well beyond hospital ops:
any target-trial emulation with variable start-of-follow-up (SGLT2i
initiation, HRT initiation, CFTR-modulator initiation) can borrow
the Gantt-chart DAG scaffold to reason about *why* time-zero was
where it was.

#### HIGH — Wood ME, Platt RW, Hutcheon JA, Cohen JM, Latour CD, Margulis AV, Petito LC, Grandi SM. *Early Pregnancy Treatment Decisions: Designing Perinatal Pharmacoepidemiology Studies using Real-World Data.* arXiv 2608.11108v1 (stat.AP, 2026-08-11). Score 1.

Focused methods paper on **target trial emulation for changes to
*pregestational* treatment regimes** during early pregnancy — the
setting where standard "new-user, active-comparator" TTE breaks down
because eligibility, treatment initiation, and start-of-follow-up all
need to line up with a treatment-decision time point that isn't
observable directly (pregnancy dating is ascertainment-dependent).
Running example is type 2 diabetes pharmacotherapy in early pregnancy.
Reviews methods for **identifying pregnancy episodes in routinely
collected healthcare data**, introduces candidate time-zero choices,
and lays out analytic approaches that minimize selection and
immortal-person-time bias. This is the methods anchor for the
**early-pregnancy-time-zero-selection problem** that has haunted
essentially every AoU / UKB / MVP / OPTUM pregnancy pharmacoepi
analysis (dating uncertainty compounds with censoring, competing
events, and etiologically-susceptible-period-specific effects).
Portable to the **CFTR-modulator persistence in pregnancy** question,
**GLP-1 RA discontinuation in early pregnancy**, and **HRT / SERM
discontinuation on menopause onset** — all of which share the
"treatment change is triggered by a state transition that is itself
ascertained with error" pattern. Should sit alongside Noma TTE R
package (08-08 report) in the pharmacoepi toolkit.

#### METHODS-WATCH — Chen R, Zuo S, Stevens W, Pollack S, Xi W, Petito L, Zhao L, Zhang H. *Clustering Informed Inverse Probability Weighting Strategies for Causal Effect Estimation in Observational Studies.* arXiv 2608.09839v1 (stat.ME, 2026-08-11). Score 2.

Compares three IPW strategies under treatment-assignment
heterogeneity: standard IPW, clustering-augmented IPW (cluster-specific
PS models), and a global PS model with estimated cluster membership as
a covariate. Simulations with/without latent cluster structure show
neither cluster-informed strategy uniformly dominates: clustering-
augmented IPW wins on MSE when latent cluster structure is present;
the global model gives lower bias and better coverage at small samples.
Applied to 966 breast-cancer patients on carboplatin (generalized PS
for dose-response → hypersensitivity risk). **Bookmark this for any
observational drug-effect analysis where patient subgroups likely
differ in treatment-assignment mechanisms** — highly relevant to
CFTR-modulator eligibility (F508del status × age × exacerbation
history), HRT initiation (menopausal-symptom severity × prior
CVD risk × formulary access), and multi-center EHR pharmacoepi
where site-level treatment cultures vary.

#### METHODS-WATCH — Kevopoulos K, Moscoloni B, Alheit B, Beeche C, Chirinos JA, Heinlein A, Peirlinck M. *Flow-based conditional cardiac anatomy generation for virtual cohorts.* arXiv 2608.09460v1 (cs.LG, 2026-08-10). Score 2.

CAN-FLOW is a two-step conditional normalizing-flow generator for
biventricular cardiac anatomies conditioned on sex, age, and BMI,
trained on 2,208 healthy UKB CMR subjects. It first learns geometry-
only latent representations of diffeomorphic cardiac shape momenta,
then models their metadata-dependent distribution with a conditional
normalizing flow. Beats conditional VAE baselines across regularization
strengths on phenotype-distribution reproduction, subgroup variability,
point-cloud coverage, and high-dimensional shape variability. **Directly
relevant to the "imaging foundation models on biobank data" thread**
and to the *digital-twins-from-EHR* rising sub-thread (line ~117): once
CAN-FLOW-style generators are conditioned on the *disease-relevant*
covariates (e.g., BMI + HbA1c + age for diabetic cardiomyopathy),
they become in-silico control arms for **virtual-cohort trial design**
— an alternative substrate to real-EHR TTE when the required contrast
is rare. Worth pairing with the LeDXA DXA-FM paper (08-08 report) as
the two biobank-imaging FM anchors of the summer.

#### METHODS-WATCH — Bandreddi S, Zhang P, Kelly RL, Machiela MJ, Albert PS. *Comparing Tobit and Two-Part Hurdle Models for Semi-Continuous Longitudinal Data with an Application to Clonal Hematopoiesis.* arXiv 2608.09725v1 (stat.AP, 2026-08-10). Score 1.

Derives rigorous mathematical conditions under which Tobit and two-part
hurdle models are equivalent — showing Tobit is a special case of the
hurdle model when the binary-process link is probit. Simulations show
the hurdle is more flexible and robust; Tobit is preferable when its
assumptions are met (simpler interpretation, no separate inference on
binary + continuous processes). **Applied to longitudinal clonal-
fraction measurements from the PLCO cohort for studying somatic
mosaicism dynamics** (zero-inflated when CH-driver-mutation VAF is
below detection). This directly addresses a modeling choice every
**CHIP / VEXAS / LOY** longitudinal analysis has to make (INTERESTS.md
line ~103): VAF trajectories in AoU and UKB WGS are precisely
zero-inflated-continuous. Reference paper for the somatic-mosaicism
sub-thread; the Machiela co-authorship also signals NCI intramural
methodological continuity with the Loh 2018 / Kessler 2022 lineage.

#### METHODS-WATCH — Porotsky S. *Inverse Confounding Analysis: An Exact Method for Quantifying the Significance of Confounding.* arXiv 2608.11991v1 (stat.ME, 2026-08-12). Score 1.

Sensitivity-analysis method that extends the widely-used E-value
approach by giving the **complete range of stratification-based Risk
Ratios** over all joint distributions compatible with observed
frequencies, rather than a worst-case lower bound. Formulates the
reconstruction as a system of nonlinear equations, obtains an
analytical solution, and shows the complete solution set can be
parameterized linearly by a single free parameter (RR becomes a
fractional-linear function of that parameter). **Complement to the
E-value / Rosenbaum bounds arsenal** in the causal-inference thread.
Useful for pharmacoepi papers where a single worst-case E-value
overstates the vulnerability and reviewers ask for a more informative
sensitivity landscape.

#### SKIP — Charpentier A. *From Rating Factors to Crash Mechanisms: A Multiscale Causal DAG Framework Linking Motor Insurance and Road Safety.* arXiv 2608.09441v1 (stat.AP, 2026-08-10). Score 1.

Off-topic (motor-insurance / road-safety). The multiscale-DAG framing
is clean and the mediation-with-partial-identification treatment is
pedagogically useful, but nothing biomedical.

#### SKIP — Luo X, Tao Y, Zeng H, Wang S, Ouyang C, Zhu M, Liu K, Chen S, Liu J. *VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression.* arXiv 2608.08366v1 (cs.CV, 2026-08-08). Score 1.

Predicts single-cell expression from H&E morphology using paired
Xenium data, with a two-branch (direct-regression + retrieval)
architecture and per-gene fusion weight. Beats prior methods on
seven metrics on held-out patients/slides/panels. Off your active
threads (no EHR / genomic-medicine hook), but worth a **future re-
visit if AoU or UKB acquire spatial transcriptomics** as an -omics
layer.

### Scholar alerts — author / citation feeds (08-16 batch)

#### HIGH — Chang E, Xie K, Zhou DJ, Korzun J, Conrad EC, Roth D, et al. *Automated epilepsy and seizure type phenotyping with transformer-based language models.* npj Digital Medicine 2026 (Peter Szolovits new-related feed).

**Automated epilepsy phenotyping with transformer LMs from clinical
text.** Snippet frames the problem as classifying epilepsy status and
seizure type from clinical notes. Direct hit on the **"NLP / LLM
extraction from clinical notes for phecode and HPO term assignment"**
sub-thread inside `EHR phenotyping & OMOP` (INTERESTS.md line ~40).
Read full-text for: (1) the exact fine-tuning corpus (which health
system, note types), (2) the phenotype-label ontology (ILAE seizure
classification vs. phecodes), (3) whether they used a chart-review
gold standard or ICD-9/10 as silver, (4) how they handled note-level
vs. patient-level aggregation. This paper should feed directly into
the LLM-based-phenotyping benchmark shortlist alongside PhenoTagger,
IMPACT (08-08 report), and PhenoGPT2.

#### HIGH — Angell A, Li Y, Hakimjavadi H, Parchment C, Yin L, et al. *Autism Spectrum Disorder Computable Phenotyping Using Electronic Health Records with Verified Autism Diagnoses.* 2026 IEEE 14th [Conf-name-truncated-in-snippet] 2026 (Kai Wang citations-to feed).

**Computable phenotyping with a chart-review-verified gold standard**
is the study design INTERESTS.md wants propagated. Snippet notes it
uses EHR data with verified autism diagnoses (implying chart-review
or clinical-diagnosis anchor). Direct hit on `EHR phenotyping & OMOP`.
Read full-text for: (1) PPV / sensitivity metrics against the verified
ground truth, (2) whether they compared rule-based vs. ML phenotypes,
(3) transferability to non-training sites — the *portability under site
shift* concern under `Knowledge representation in EHRs` (line ~168).
Also of interest: whether the verified-diagnosis subset can be reused
as a PheValuator-style validation cohort for AoU / BioVU autism
phenotype development.

#### HIGH — Reho P, Thaker VV, Athreya AP, Cremers S, Go YM, et al. *Pharmacoexposomics: The Environmental Complement to Pharmacogenomics to Advance Precision Medicine.* Annual Review of Pharmacology and Toxicology 2026 (George Hripcsak new-articles feed).

**Coins/formalizes "pharmacoexposomics"** — the environmental
complement to pharmacogenomics. This is the theoretical scaffold your
**PGS × exposure / environment interactions** rising sub-thread has
been circling around, but applied to the *drug-effect* side rather
than the *disease-risk* side (Nagpal & Gibson lineage handles disease
risk). Directly serves the **pharmacoepi drug-class watchlist**
(GLP-1 RA, SGLT2i, CFTR modulator, HRT) by giving a language for
drug-response-modifier-by-environment (diet, air pollution,
socioeconomic exposure, medication co-exposure). Read for: (1) the
proposed operational definition (is it just "add environmental
covariates" or a more principled decomposition), (2) study designs
they recommend (cohort-embedded vs. crossover vs. real-world
digital), (3) whether they explicitly cite AoU / UKB / MVP as the
substrate. Should become a *citable framing paper* for the pharmacoepi
+ exposome interaction argument in future methods pieces.

#### HIGH — Abner E, Johnson JP, Valliere J, Vujkovic M, Daly M, et al. *Genetic variants affect diurnal glucose levels throughout the day.* Nature 2026 (Konrad Karczewski + Mark Daly feeds, dual hit).

**Functional-time GWAS of diurnal glucose trajectories** rather than a
single scalar HbA1c. Circadian rhythms coordinate wake–sleep and
metabolic rhythms; this paper takes CGM-like or repeated-glucose data
across the day as the phenotype and runs a time-resolved GWAS.
Dual-feed hit (Karczewski + Daly) signals genome-wide-scale QC and
gnomAD-lineage authorship weight. Directly connects to two INTERESTS.md
threads: (1) the **PGS × exposure / environment** thread — chronotype
and meal timing become genotype-modifiable exposures; (2) the
**GWAS / genetic epi** thread — anchor paper for "phenotype-as-a-
function" GWAS design that pairs with Ciardulli et al.
(functional propensity score, 08-08 report). Read for: (1) discovery
cohort composition (UKB CGM subset?), (2) whether new loci beyond
canonical T2D GWAS emerge only when the phenotype is time-resolved,
(3) any PGS built from the temporal loci and its portability across
ancestries.

#### HIGH — Mitev V. *A Methodological Framework for Real-World Performance Studies of Clinical Variant Classification Platforms at Early Organizational Stages.* Frontiers in Genetics 2026 (`variant interpretation` / `variant classification` keyword feed).

**Framework paper for evaluating clinical variant-classification
platforms in real deployment** (InterVar / CancerVar / Franklin /
VarSome / Emedgene / N-of-One class). Directly serves the ACMG /
ClinGen thread (INTERESTS.md line ~66). Read full-text for: (1) the
performance metrics recommended (agreement with expert curators?
concordance with ClinVar 2-star+?), (2) whether they distinguish
platform-versus-guideline drift, (3) applicability to health-system
deployment decisions (which platform to adopt for BRCA / cardiomyopathy
/ CFTR panels). Useful reference when the CF thread's variant-
interpretation subarm needs a benchmarking methodology.

#### HIGH — Pérez-García J, García-Criado F, Pazos M, Chagoyen [+], et al. *A text mining and ontology-based approach using phenotypes to obtain relevant literature for rare diseases.* iScience 2026 (Kai Wang new-related feed).

**HPO-driven literature-retrieval tool for rare-disease diagnosis.**
Bridges two INTERESTS.md threads: `Knowledge graphs & ontologies` and
`Rare disease`. Snippet frames the problem as "diagnosing rare"
diseases from phenotype descriptions. Read full-text for: (1) whether
they benchmark against Phenolyzer / Phen2Gene / PhenoSV / PhenoGPT2
as ranking baselines, (2) how they operationalize the phenotype-input
layer (structured HPO codes vs. free-text extraction), (3) whether
the evaluation cohort has separable metrics for *ranking* vs.
*evidence coverage* (the GraphRareBench concern from the 07-29 report).
If they don't, this is a natural extension paper.

#### MEDIUM — Meng Y, Shen M, Guo SY, Yang MY, T[+]. *Whole-exome sequencing reveals the genetic landscape and polygenic susceptibility in 1241 patients with clinically suspected hemophagocytic lymphohistiocytosis.* [Journal TBD] 2026 (Lisa Bastarache new-related feed).

n=1241 clinically-suspected HLH cases with WES; genetic landscape +
polygenic susceptibility framing. Adjacent to the **rare-variant +
composite-risk** thread since HLH sits at the mendelian /
inflammatory-multifactorial boundary. Read only if extending into
immune-dysregulation composite-risk work; otherwise low-signal for
your active EHR / phenotyping / pharmacoepi projects.

#### MEDIUM — Qiu Q, Liu Y, Xue H, Pandey R, Liu J, He L, Liu P, et al. *A cross-organ single-cell analysis of hypertension.* Science 2026 (Lisa Bastarache citations-to feed).

Cross-organ single-cell hypertension atlas; big-tent paper in Science.
Downstream of Bastarache's PheWAS work (probably cited for the
phecode-based hypertension outcome definition). Off your immediate
methods work, but the atlas is a resource paper worth flagging for
future BP-related pharmacoepi analyses.

#### MEDIUM — Gaisbauer S. *VEXAS Syndrom-Fallbericht und aktueller Stand der Wissenschaft.* 2026 (Daniel Kastner citations-to feed).

German-language VEXAS case report + review. Adds a small clinical case
to the VEXAS thread (INTERESTS.md line ~103). Read only if maintaining
the VEXAS case series watchlist; otherwise dissertation-tier depth.

#### MEDIUM — Saad F, Shore N, Vjaters E, Olmos D, N[+]. *Darolutamide Plus Androgen-deprivation Therapy in Metastatic Hormone-sensitive Prostate Cancer by Disease Volume and Risk Subgroups in the Phase 3 [ARANOTE / ARASENS-lineage trial].* [Journal TBD] 2026 (Chenjie Zeng self-citation feed).

Phase 3 subgroup analysis of darolutamide + ADT in mHSPC. Fires the
self-citation feed because it's downstream of Zeng's prostate-cancer
epidemiology lineage. Read only if the prostate CRPC / mHSPC subthread
is reactivated (relevant to the PCWG4 commentary in the 08-08 report).

#### METHODS-WATCH — Qasim M, Wang K, Bhatt IS. *Adaptive Penalization and Bootstrap-Smoothed Inference for Two-Sample Mendelian Randomization with Summary Data.* arXiv 2607.18503 2026 (Jian Yang new-related feed).

Two-sample MR method with adaptive penalization + bootstrap-smoothed
inference. Bookmark for the **drug-target MR** rising sub-thread
(INTERESTS.md line ~64). Compare to MR-ALasso and the Saxby et al.
metformin × AAA lineage cited there.

#### METHODS-WATCH — Zhang H, Shi Y, Zhang S, Jian Z, Liang M, Zhang S, et al. *Temporal graph transformer for next visit diagnosis prediction on electronic health records.* Scientific Reports 2026 (`electronic health records` keyword feed).

Temporal-graph-transformer for next-visit diagnosis prediction on EHR.
Adjacent to the **`Patient-level and cohort-level knowledge graphs from
EHR`** sub-topic under `Knowledge representation in EHRs and applications`
(INTERESTS.md line ~148). Read for architecture (how temporal edges are
encoded) and whether they benchmark against MEDS / EHRSHOT models.
Downgrade to LOW if it's yet-another-transformer-on-MIMIC with no
explicit graph-representation choice ablation.

#### METHODS-WATCH — de Andrés-Galiana EJ, Fernandez-Martinez JL [+]. *Identifying candidate therapeutic targets in amyotrophic lateral sclerosis through a transcriptome-wide machine-learning consensus approach for drug repurposing.* [Journal TBD] 2026 (`drug repurposing` keyword feed).

Transcriptome-wide ML consensus for ALS drug repurposing. Adjacent to
the **drug repurposing** thread; ALS is off-thread but the
transcriptome-wide-consensus method is worth a look if it's
model-architecture-agnostic (as opposed to a single-model
prioritization). Compare to Boyle et al. transcriptome-based
repurposing lineage.

#### METHODS-WATCH — Cheng Z, Bai R, Diao Y. *Integrative Transcriptomics and Mendelian Randomization Identify RGS1 as a Causal Immune Regulator in Alzheimer's Disease.* Current Issues in Molecular Biology 2026 (`mendelian diseases` keyword feed).

MR + integrative transcriptomics for AD target discovery. Standard
template; RGS1 is a known immune-regulation locus. Bookmark for
comparison with the ALS repurposing paper above if extending into a
**neuroinflammation MR** vertex.

#### METHODS-WATCH — Liao X, Li B, Broyd T, Han S, Tang C, Li N. *Integrating Information Flow-Knowledge Graphs and Fine-tuning LLM for Knowledge-Guided Process Engineering in Domain-Specific Task.* Knowledge-Based Systems 2026 (Tiffany J Callahan new-related feed).

LLM + KG for domain-specific engineering (non-biomedical). Read only
for the **LLM-fine-tuning-with-KG-context recipe** — that architecture
is portable to biomedical KG work in the `Knowledge representation in
EHRs` thread (concept-normalization, phecode assignment).

#### METHODS-WATCH — Roine L, Kasepalu T, Loorents H, Elmet M, Irs A, et al. *Heterogeneity in diagnosing heart failure — real world data from electronic health records.* BMC Cardiovascular Disorders 2026 (George Hripcsak new-related + Pascal Brandt new-related feeds, dual hit).

Real-world variability in HF diagnosis from EHR. Dual-feed hit
(Hripcsak + Brandt) means it's a *phenotype-heterogeneity across sites*
paper — directly relevant to the **`Fidelity, portability, and audit
of representations`** sub-topic (INTERESTS.md line ~168). Read if
extending phecode-based HF outcomes across BioVU / AoU / MIMIC / UKB;
the concordance-across-institutions estimate becomes a validation
benchmark.

#### LOW — O'Neill TJ, Graß C, Gewies A, Coelho S, Gehring T. *MALT1 alternative splicing — A molecular rheostat for balancing immune activation and homeostasis.* Science Advances 2026 (Denny + Karczewski citations-to feeds, dual hit).

Basic-science splicing / immune-regulation paper cited from the
Denny + Karczewski lineage. Off your immediate methods work.

#### LOW — Lin Z, Wei J, Zhou H. *Unraveling the Pathogenic Mechanisms of Osteoarthritis and Obesity: An Integration of GWAS, Cellular Specificity, and Spatial Transcriptomics.* Osteoarthritis and Cartilage 2026 (Jian Yang citations-to feed).

GWAS + single-cell integration for OA + obesity. Off-thread.

#### LOW — Marquez G, Crowhurst K, Sinemus H, Karakis N, et al. *All of Us Consortium Training Summary Report.* 2026 (`All of Us research program` keyword feed).

Program-training report; not primary science.

#### LOW — Kozin Porat M, Aronis A, Weinstein G. *The association between adult attention-deficit/hyperactivity disorder and lifestyle factors: findings from the UK Biobank.* BMC Psychiatry 2026 (`UK Biobank` keyword feed).

UKB descriptive ADHD × lifestyle association. Standard-format
observational analysis; off your active methods threads.

#### LOW — Douglas CMW, Kleinhout-Vliek T, Hagendijk R, et al. *Social pharmaceutical innovation (SPIN): A sensitizing concept for challenges in rare diseases.* Journal of Pharmaceutical Science and Practice 2026 (`rare diseases` keyword feed).

Policy / sociology-of-science piece. Off methods thread.

#### LOW — Selviyanti E, Subriadi AP, Haryanti T. *Integrating Technology, Human, and Knowledge Dimensions in Electronic Health Record Implementation: A Systematic Literature Review of Socio-Technical [Framing].* [Conf/Journal TBD] 2026 (`Foundation models + electronic health records` keyword feed).

Sociotechnical / implementation-science review. Off your primary
methods thread.

#### LOW — Wang F, Al-Lawati A, Bektas I, Fang J, Melenski A, et al. *Unified Multi-Dimensional Benchmark for Complex Graph Reasoning in Large Language Models.* arXiv 2026 (Marinka Zitnik new-related feed).

Generic LLM-graph-reasoning benchmark. Off clinical-agent thread.

#### LOW — Lee W, Kim J, Ko J, Rhee W. *Beyond On-Policy Exploration: Integrating External Policy Rollouts for Reinforcement Learning in Diffusion Language Models.* arXiv 2608.01717 2026 (Zhiyong Lu new-related feed).

Generic RL-for-LLM paper. Off clinical-agent thread.

#### LOW — Dang C, Xiong S, He C, Li W. *SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models.* arXiv 2608.10538 2026 (Marinka Zitnik new-related feed).

Generic small-LM RL paper. Off clinical thread.

#### LOW — Strobl EV. *COMPACT: Spectral Adjustment Scores from a Complete and Irreducible Causal Criterion.* arXiv 2608.10305 2026 (Patrick Ryan new-related feed).

Adjustment-set criterion for causal DAGs. Adjacent to the causal-
inference thread but a criterion / theory paper rather than an
applied-methods contribution; only cite if writing about complete
adjustment criteria.

#### LOW — Oh G, Kim S, Park S, Kim BH. *Model and Task-Aware Test-Time Scaling Strategies for Large Language and Vision-Language Models in Medicine: Evaluation Study.* Journal of Medical Internet Research 2026 (Peter Szolovits new-related feed).

Test-time-scaling benchmark study for medical LLMs. Off your active
clinical-agent sub-threads unless you're building a medical-LLM
inference-time-budget policy.

#### LOW — Gil JP, Coquery E, Samuel J, Gesquière G. *ConVer-G: A Suite for Versioning, Querying and Visualization of Dynamic Knowledge Graphs.* Journal of Open Source Software 2026 (Tiffany J Callahan new-related feed).

Non-biomedical KG-versioning tool. Off-thread.

---

## What's NOT in the report

- **GitHub `arxiv-digest` cron / PR notifications** — none surfaced in
  Gmail search; the local repo commits and the on-disk `digests/`
  directory serve as the digest artifact.
- **NCBI My-NCBI What's-New batches** (AoU / UKB / drug repurposing) —
  none fired in the searched window.
- **bioRxiv / medRxiv Subject Collection Alerts** — none surfaced;
  scholar author feeds carried what medRxiv content there was.
- **arxiv.org daily category mailings** (`no-reply@arxiv.org`) — the
  raw upstream feed that supplies the `arxiv-digest` pipeline; papers
  surfaced via the digest are covered in the arxiv-digest section
  above.
- **Substack / newsletters** — noted but no biomedical content in this
  window crossed the on-thread threshold.

## Next steps to consider

1. **Read Vossler et al. egg-computation arXiv 2608.10339 full text.**
   Highest-signal single item for the agentic-causal-inference
   sub-thread this window. Pairs with Chou/Kallus `oci-agent` for a
   short methods commentary on the "LLM does mechanical steps, human
   owns identification assumptions" division of labor.
2. **Bundle Wood et al. perinatal TTE + Noma TTE R package (08-08)**
   into a pharmacoepi-tooling shortlist for the pregnancy pharmacoepi
   subproject (T2D / SSRIs / GLP-1 RA continuation).
3. **Read Reho et al. Pharmacoexposomics** (Annual Reviews) as the
   framing citation for pharmacoepi × exposome writing; slot it beside
   Nagpal & Gibson on PGS × exposure.
4. **Adopt Bandreddi et al. Tobit-vs-hurdle result** as the modeling
   decision anchor for any longitudinal CHIP / LOY VAF analysis in
   AoU / UKB WGS. Default to hurdle unless the Tobit assumptions can
   be empirically supported.
5. **Add CAN-FLOW (Kevopoulos et al.) to the imaging-FM reading list**
   alongside LeDXA (08-08 report) — the two form a coherent "biobank
   imaging FM" pair for a future methods essay.
6. **Read Chang et al. (transformer epilepsy phenotyping, npj Digital
   Medicine) and Angell et al. (verified-diagnosis autism computable
   phenotype, IEEE 2026)** back-to-back as reference points for the
   next LLM-computable-phenotyping methods audit — the Chang paper
   for the *note-level* extraction template, the Angell paper for the
   *chart-review anchor* validation template.
7. **Cite Mitev variant-classification-platform framework** whenever
   evaluating InterVar / CancerVar / Franklin / VarSome deployments
   for the CF / ACMG thread.

_Report generated 2026-08-17 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-17 → next scheduled run._
