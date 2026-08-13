# Research digest report — 2026-08-13

Triage of research-related email + the GitHub `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS-LOY/IBD disease
threads, EHR foundation models, KGs/ontologies, drug repurposing, rare
disease, ML for precision health, multimorbidity, knowledge
representation in EHRs).

Window: **2026-08-08 12:36Z → 2026-08-13 12:41Z** (~5 days since the
last research-digest report, covering five arxiv-digest cron runs, two
Google Scholar batches on 08-11 and 08-13, one keyword batch on 08-12,
and daily NCBI What's-New PubMed fires).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-08.md` → `2026-08-13.md`) | 08-08 → 08-13 (10:30Z crons) | 5 daily runs. 08-08: 0 papers (8 previously surfaced, suppressed); 08-10: 0 papers; 08-11: 5 papers (largest batch — clustering-informed IPW, UKB cardiac shape flow model, CHIP zero-inflated longitudinal, motor-insurance DAG, VOICE H&E→scRNA); 08-12: 2 (LLM-assisted egg-computation for causal effects on timings; pregnancy TTE design paper, 4 suppressed); 08-13: 1 (Porotsky ICA for confounding significance, 5 suppressed). |
| Google Scholar alerts — author feeds (08-11 batch) | 08-11 23:58Z | 15+ author feeds fired: Chenjie Zeng (self), Lisa Bastarache, Joshua C Denny, Patrick Ryan, Kai Wang, Ali G Gharavi, David Baker, Jay Shendure, Tiffany J Callahan, George Hripcsak, Konrad Karczewski, Stephen B Montgomery, Jure Leskovec, Jonathan K Pritchard. Densest on-thread signal from Bastarache (Li et al. SV PheWAS framework + Dutta et al. PRS×proteomics 21 cancers) and Ryan (Mann et al. SELECT/FLOW/SOUL pooled semaglutide kidney). |
| Google Scholar alerts — keyword feeds (08-12 batch) | 08-12 13:04Z | 12 keyword feeds fired: `electronic health records`, `rare diseases`, `Foundation models + electronic health records`, `All of Us research program`, `UK Biobank`, `variant interpretation`/`variant classification`, `intitle:"clonal hematopoiesis"`, `mendelian diseases`, `autoimmune diseases`, `knowledge graph`, `drug repurposing`, plus a duplicate FM/EHR correction. Lightest batch of the window — mostly one-item alerts, several are review pieces or author corrections. |
| Google Scholar alerts — author feeds (08-13 batch) | 08-13 09:13Z | 20+ feeds fired: Chenjie Zeng (self), Joshua Denny (×2), Miguel Hernán, Jian Yang (×2 including "new related"), Konrad Karczewski (×2), Lisa Bastarache, Pascal Brandt, George Hripcsak (×2), Patrick Ryan, Peter Szolovits (×2), Marinka Zitnik, Zhiyong Lu, Kai Wang, Yuan Luo, Stephen Montgomery (×2), Tiffany Callahan, Vivek Natarajan, Jonathan Pritchard, Daniel Kastner. Densest on-thread signal from Denny (Qi Ghostknockoffs sample-relatedness GWAS), Jian Yang (Nøhr CRC PRS + registry screening, Naderian PRS+FamHx CHD, He CIT-Lasso fine-mapping), Karczewski (Hernandez rare-variant mutation-selection-drift), Hernán (Szmulewicz lithium suicide TTE), and Zeng self-alert (HNC-TACTIC EHR AI protocol). |
| NCBI My-NCBI What's-New (PubMed) | 08-08 → 08-13 (daily) | Six daily fires each for saved searches `All of Us`, `UK Biobank`, `drug repurposing`. 08-13 AoU batch alone surfaced 4 papers including Kather et al. cholangiocarcinoma population-level ML risk prediction (EBioMedicine) and Chatzipanagiotou et al. genetic ancestry × CRC in AoU (JAMA Network Open). |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated to first
> 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced this window. They cluster into four knots
that each stand on their own:

**Composite risk (PRS + rare + registry/family) cluster (4 items).**
Naderian et al. *AJHG* — additive value of PRS, monogenic FH, and family
history for CHD risk prediction across self-identified race/ethnicity
groups in two diverse US cohorts: the reference paper for the
"PRS is one instrument, family history and monogenic status are
separate instruments, they stack" thesis your composite-risk sub-thread
tracks. Multi-ancestry framing is a bonus. Nøhr et al. *BJC* — genome-wide
PRS combined with registry data for CRC risk-based screening, comparing
against faecal immunochemical test (FIT): the applied-screening companion
to Naderian, showing what composite risk actually does when confronted
with the current standard. Dutta et al. *Cell Genomics* — PRS for 21
cancers integrated with 4,955 plasma proteins in cancer-free UKB
participants, identifying cancer-related proteins and trans-regulated
protein networks: this is the *multi-omics-augmented PRS* rising
sub-thread on your INTERESTS.md, executed across a pan-cancer landscape
and directly relevant to Zeng's cancer-genetic-epi lineage. Ciardulli
et al. arXiv 2608.03200 previously surfaced (08-05) — but see now
Wang et al. *iScience* (Jian Yang feed) — cross-trait genetic
architecture between breast cancer and psychiatric disorders: the
BC-side companion to your Denny-lineage PheWAS-of-PheWAS design
instinct, delivering the shared-architecture inventory that
transdiagnostic-psychiatry work now converges on.

**PheWAS / phenotyping infrastructure cluster (3 items).** Li et al.
medRxiv (Bastarache + Denny author feeds) — a scalable framework
enabling *phenome-wide association of structural variants* in biobank
cohorts: bridging the SV-genetics literature (which has been mostly
locus-focused) with the phecode-based PheWAS pipeline your
infrastructure thread tracks. If the framework scales as advertised,
AoU / UKB SV callsets get a phecode-scale first-look at every SV in
one pass — that's a new discovery instrument, not just a methods
update. Qi et al. *Genetic Epidemiology* (Denny author feed) — robust
inference with Ghostknockoffs in GWAS with sample relatedness: extends
the knockoff-based causal-variant identification framework to the
related-sample setting that AoU / UKB / MVP routinely present.
Complements the CIT-Lasso and MUGO fine-mapping methods from the
Yang / Montgomery feeds in the same batch. Hartwell & Kember review
(carry-over from prior report) sits alongside these as the substance-use
extension. He et al. *Genome Biology* — CIT-Lasso: summary-statistics
fine-mapping distinguishing likely causal variants from correlated
tag variants, without individual-level data. Directly on-thread for
the PheWAS + downstream causal-variant identification pipeline.

**Pharmacoepi / TTE / drug-effect cluster (3 items).** Mann et al.
*Lancet Diabetes & Endocrinology* — SELECT + FLOW + SOUL prespecified
pooled analysis of semaglutide on kidney outcomes: definitive
across-trial synthesis for GLP-1 RA renoprotection, directly hitting
your active GLP-1 RA drug-class watchlist and adjacent to the
CFTR-modulator persistence framing (both are "drug that reshapes a
chronic-disease trajectory" cases). Szmulewicz et al. *BMJ Mental
Health* (Hernán citation feed) — target trial emulation of lithium
initiation and continuation for suicide prevention in US veterans
with bipolar or MDD, using EHR + administrative claims: canonical
TTE-in-EHR execution from Hernán's group, portable template for the
CFTR-modulator persistence / statin-adherence / HRT-persistence
outcomes on your pharmacoepi list. Wood et al. arXiv 2608.11108
(surfaced 08-12) — perinatal pharmacoepidemiology study design for
pregestational treatment regime changes, using T2D as the exemplar:
extends TTE to the pregnancy-window special case where left-truncation,
right-censoring, and etiologically susceptible periods break standard
approaches. Combined with the Noma TTE R-package tutorial from the
prior report, this is a consolidating tooling and design moment for
the pharmacoepi thread.

**LLM-assisted causal inference / clinical prediction cluster (2 items).**
Vossler et al. arXiv 2608.10339 (`egg-computation`) — LLM-assisted
g-computation that combines expert Gantt-chart reasoning (the qualitative
QI tradition) with formal DAG-based identification for hospital
length-of-stay improvement; validated against human-expert output on
11 QI interventions at an urban safety-net hospital. This is the
*agentic / human-in-the-loop observational causal inference* rising
sub-thread on INTERESTS.md executed on a real hospital-ops question,
extending beyond the Chou/Kallus `oci-agent` framing. Kather et al.
*EBioMedicine* (NCBI AoU feed) — machine learning for population-level
risk prediction of future cholangiocarcinoma: a rare-cancer analog to
the population-screening framing that PRS + registry work is converging
on, and the *ML tied to a clinical decision* pattern your
`Machine learning for precision health` thread wants (who to screen,
who to escalate) rather than a benchmark-only piece.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-08 → 2026-08-13)

#### HIGH — Vossler P, Ouyang J, Guo FR, Huang A, Shojaie A, Zier L, Xia F, Feng J. *Expert-Guided g-computation with Large Language Models for Estimating Causal Effects on Timings: Applications to Hospital Quality Improvement.* arXiv 2608.10339v1 (stat.ME, 2026-08-11). Score 2.

Introduces `egg-computation` — a causal model over Gantt charts of
patient trajectories, with identification via a variant of g-computation
that solicits expert input only for components unidentifiable from data.
The LLM-assisted pipeline scales the expert-reasoning step; validation
uses 11 candidate QI interventions at an urban safety-net hospital,
where LLM-generated causal graphs and time-saving estimates were
"highly concordant" with human experts. Directly serves the *agentic /
human-in-the-loop observational causal inference* rising sub-thread on
INTERESTS.md — the Chou/Kallus `oci-agent` pattern extended to the
qualitative-expert-input side of the analysis. Portable to any
pharmacoepi setting where the causal DAG has expert-known edges the
data can't disambiguate (dose escalation → discontinuation causal
paths, CFTR-modulator adherence → exacerbation sequencing). Also
useful for hospital-flow / LOS-oriented ML-for-precision-health work
where the intervention is hypothetical (never seen in historical data).

#### HIGH — Wood ME, Platt RW, Hutcheon JA, Cohen JM, Latour CD, Margulis AV, Petito LC, Grandi SM. *Early Pregnancy Treatment Decisions: Designing Perinatal Pharmacoepidemiology Studies using Real-World Data.* arXiv 2608.11108v1 (stat.AP, 2026-08-11). Score 1.

Extends target trial emulation from point-intervention pregnancy questions
(vaccine, antibiotic) to the *pregestational treatment-regime change*
setting, using T2D as the exemplar. Reviews how to identify pregnancy
episodes in routinely-collected healthcare data, discusses time-zero
candidates aligned with real clinical decision points, and lays out
analytic strategies for the left-truncation / right-censoring /
competing-events / gestational-length / susceptible-period tangle
that pregnancy TTE has to handle. Directly on-thread for the *TTE-in-EHR*
work on INTERESTS.md's causal-inference bench, and a natural companion
to the Noma TTE R-package tutorial from the prior report. Portable to
adjacent settings where the exposure is a *change* in a chronic-disease
regime rather than a new initiation (statin switch, GLP-1 RA add-on,
CFTR-modulator titration).

#### HIGH — Chen R, Zuo S, Stevens W, Pollack S, Xi W, Petito L, Zhao L, Zhang H. *Clustering Informed Inverse Probability Weighting Strategies for Causal Effect Estimation in Observational Studies.* arXiv 2608.09839v1 (stat.ME, 2026-08-10). Score 2.

Compares three IPW strategies for handling treatment-assignment
heterogeneity in the presence of latent cluster structure: standard IPW,
clustering-augmented IPW with cluster-specific PS models, and a global
PS model with estimated cluster membership as a covariate. Applied to
966 breast-cancer patients on carboplatin using generalized PS for the
dose–response of treatment cycles → hypersensitivity reaction risk.
Neither cluster-informed strategy uniformly dominates: augmented IPW is
better under real latent structure; the global-with-membership model
gives better bias / coverage at small N. Directly on-thread for the
causal-inference thread as a *when-your-PS-model-is-misspecified-do-this*
tool. Also feeds the pharmacoepi drug-class thread — carboplatin dose
response is a template for CFTR-modulator dose-adjustment or GLP-1 RA
titration analyses, and the "subgroup-specific estimates + diagnostic
profiles" ancillary output is exactly what the HTE-methods sub-thread
values.

#### HIGH — Porotsky S. *Inverse Confounding Analysis: An Exact Method for Quantifying the Significance of Confounding.* arXiv 2608.11991v1 (stat.ME, 2026-08-12). Score 1.

Sensitivity-analysis method that extends the widely-used E-value
approach beyond worst-case bounds: given the marginal frequencies of
exposure, confounder, and outcome, it reconstructs the full set of
admissible joint distributions and derives the exact analytical range
of the stratification-based Risk Ratio over that set. Solves the
reconstruction as a system of nonlinear equations, obtaining a
one-parameter linear family of admissible configurations, with the RR
as a fractional-linear function of the free parameter. Directly on-thread
for the causal-inference / pharmacoepi thread as an upgrade path from
E-value to a *full-range* sensitivity output — useful whenever a
reviewer asks "how sensitive is this to unmeasured confounding" and
"E-value = 1.8" is a weaker answer than "here's the exact RR envelope
under all admissible configurations." Try on the next drug-effect
observational estimate on the pharmacoepi watchlist (SGLT2i, GLP-1 RA,
HRT persistence).

#### METHODS-WATCH — Bandreddi S, Zhang P, Kelly RL, Machiela MJ, Albert PS. *Comparing Tobit and Two-Part Hurdle Models for Semi-Continuous Longitudinal Data with an Application to Clonal Hematopoiesis.* arXiv 2608.09725v1 (stat.AP, 2026-08-10). Score 1.

Systematic comparison of Tobit vs. two-part hurdle mixed models for
zero-inflated non-negative longitudinal outcomes; shows the Tobit is a
special case of the hurdle with probit link on the binary component,
and recommends the hurdle unless Tobit assumptions are scientifically
plausible. Applied to longitudinal clonal-fraction measurements from the
Prostate/Lung/Colorectal/Ovarian (PLCO) study for somatic mosaicism
across mCAs. Directly relevant to the *CHIP / mCA / LOY* somatic
mosaicism sub-thread on INTERESTS.md — for anyone modeling VAF
trajectories over time (repeat blood draws in AoU, longitudinal MVP,
etc.), this settles a modeling-choice question that has been
under-specified. Bookmark for the next longitudinal-mosaicism analysis.

#### METHODS-WATCH — Kevopoulos K, Moscoloni B, Alheit B, Beeche C, Chirinos JA, Heinlein A, Peirlinck M. *Flow-based conditional cardiac anatomy generation for virtual cohorts.* arXiv 2608.09460v1 (cs.LG, 2026-08-10). Score 2.

CAN-FLOW: a two-step conditional-normalizing-flow generator for
diffeomorphic cardiac shape momenta, conditioned on sex, age, and BMI,
trained on 2,208 healthy UKB subjects. Beats cVAE on subgroup variability,
metadata-dependent trend reproduction, and high-dimensional shape
variability. Not on the primary EHR-genomics thread, but useful
methods-watch for the *digital twins from EHR data* rising sub-thread —
if virtual-cohort generation for cardiac anatomy is now a shareable
framework tied to UKB metadata, the same normalizing-flow discipline
should port to trajectory-generation for EHR-code sequences (compare
to MEDS / EHRSHOT synthetic-cohort work).

#### METHODS-WATCH — Luo X, Tao Y, Zeng H, Wang S, Ouyang C, Zhu M, Liu K, Chen S, Liu J. *VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression.* arXiv 2608.08366v1 (cs.CV, 2026-08-08). Score 1.

Multimodal FM predicting single-cell gene expression from H&E images via
paired Xenium data; contrastive alignment of cell-centered H&E morphology
(pathology FM) with single-cell expression embeddings (transcriptome FM)
over 23M cells, followed by a two-branch expression predictor that fuses
direct regression with retrieval-based recovery. Off primary threads
but a candidate reference for the *pretraining-contamination audit*
sub-thread if anyone extends membership-inference protocols from
scContam to H&E-expression foundation models. Also useful if the
digital-twins-of-tumors framing bridges into imaging-molecular FMs.

#### SKIP — Charpentier A. *From Rating Factors to Crash Mechanisms: A Multiscale Causal DAG Framework Linking Motor Insurance and Road Safety.* arXiv 2608.09441v1 (stat.AP, 2026-08-10). Score 1.

Off-topic (motor insurance).

---

### Scholar alerts — author feeds (08-11 batch)

#### HIGH — Li M, Peng W, Zhang L, Huang T, Wei C, Liu Z, Fang L. *A scalable framework enables phenome-wide association of structural variants in biobank cohorts.* medRxiv/Research Square 2026 (Bastarache + Denny author feeds).

"Genomic structural variants (SVs) constitute a major source of human
genetic diversity and disease susceptibility. Yet, population-scale SV
genetics lacks a viable mechanism to synthesize massive individualized
callsets into reliable cohort [associations]." Directly on-thread for
the PheWAS / phecode infrastructure thread — SV-PheWAS has been a
scaling-bottleneck problem for years, and a scalable framework that
delivers phecode-scale first-look at biobank SV callsets is a discovery
instrument, not just a methods paper. Cross-listed on Bastarache and
Denny author feeds, i.e. exactly the lineage this belongs to. Follow-ups
worth checking on full-text: (1) how they handle SV genotype uncertainty
across UKB/AoU/MVP callsets; (2) whether phecode aggregation is
per-SV or gene/interval-aggregated; (3) inflation-control strategy for
SV × phecode grid; (4) whether they release the framework as portable
tooling for BioVU-scale replication.

#### HIGH — Dutta D, Zhang J, Guo X, Quint R, Rooney MR, et al. *Polygenic risk scores and plasma proteomics identify cancer-related proteins and trans-regulated protein networks.* Cell Genomics 2026 (Bastarache author feed).

"We integrate polygenic risk scores (PRSs) for 21 cancers with 4,955
plasma proteins measured in cancer-free [participants]." Directly on
the *multi-omics-augmented PRS* rising sub-thread on INTERESTS.md, and
directly overlapping Zeng's pan-cancer genetic-epi lineage. Executes the
"PRS-as-instrument-to-discover-mediators" logic across a pan-cancer
landscape via Olink/proteomics, with trans-regulated protein network
inference. Follow-ups worth checking on full-text: which cohort (UKB
Olink most likely; possibly AoU proteomics as a secondary), whether
they stratify by ancestry, and whether the trans-regulated networks
converge on the same targets across cancer types (which would argue for
shared trans-hubs vs. cancer-specific proteomes). Perfect substrate for
a Zeng-lineage follow-up scoring pan-cancer PRS against AoU proteomics
when that arm matures.

#### HIGH — Mann JFE, Badve SV, Baeres FMM, Belmar N, et al. *Effect of semaglutide on kidney outcomes in the SELECT, FLOW, and SOUL trials: a prespecified pooled analysis.* The Lancet Diabetes & Endocrinology 2026 (Patrick Ryan author feed).

Prespecified pooled analysis across the three largest semaglutide
outcome trials (SELECT, FLOW, SOUL) for kidney endpoints in T2D + CKD
populations. This is the definitive across-trial synthesis for GLP-1 RA
renoprotection and lands directly on the pharmacoepi drug-class thread
(GLP-1 RA is explicitly on your active watchlist). Read the full paper
for the subgroup-heterogeneity structure (baseline eGFR strata, T2D vs.
non-diabetic obesity, CKD stage) and whether the pooled estimate
generalizes to the CFTR-modulator-persistence-style framing where the
outcome is a slope of a chronic-disease trajectory. Sets the RCT
benchmark that any AoU/UKB/MVP observational GLP-1 RA renal analysis
must triangulate against.

#### MEDIUM — Demeule C, Amoureux L, Huet F, Allou N, Le Naour C, et al. *Pathogenic respiratory microbiota in cystic fibrosis: impact of 2 years of triple CFTR modulator therapy.* Clinical Microbiology and Infection 2026 (Patrick Ryan author feed).

Two-year longitudinal microbiome data on people with CF on
elexacaftor/tezacaftor/ivacaftor (ETI, Trikafta). Directly on the CF
disease thread — read for the microbial-shift story alongside the
psychosocial-impact and modulator-persistence literature. The two-year
window is the sweet spot for real-world durability questions that
short-follow-up RCTs can't answer. Not a HIGH because it's a single-modality
outcome (microbiome) rather than a clinical endpoint, but the
integration with your pharmacoepi CFTR-modulator sub-thread should be
noted.

#### MEDIUM — Zyryanov SK, Kondratyeva EI, Zhekaite EK, et al. *The relationship between the pharmacogenetics and pharmacokinetics of CFTR modulators in a population of children with cystic fibrosis.* Pharm & Pharmacology (Russian J) 2026 (Patrick Ryan author feed).

n=32 pediatric CF patients on ETI or dual combos; pharmacogenetics
× pharmacokinetics correlation. Small sample, single-center, Russian-
language journal, but directly on the *pharmacogenomic modifiers of
medication persistence* rising sub-thread applied to CFTR modulators
(mirrors the CYP2D6 × metabolizer-phenotype PGx framing). Would be
higher-priority at biobank-scale replication; noted here for the
tracker.

#### MEDIUM — Carretero-García J, Varillas-Delgado D. *Polygenic Profiles Are Associated with Multidomain Biochemical Adaptations Across a Competitive Season in Professional Football Players.* [J TBD] 2026 (Stephen B Montgomery citations feed).

Longitudinal PRS × environment/behavior interaction study — a
sports-medicine analog to the AoU MDD PRS × Fitbit wearable trajectory
paper from the prior report. Low direct clinical utility but a useful
data point for the PGS × modifiable-exposure sub-thread's argument that
behavior interacts with polygenic liability across many domains.

#### METHODS-WATCH — Griffin CP, Garcia DL, Grossman GH. *Global Biobank Awareness: An Initiative to Showcase Impact and Increase Global Visibility of Biobanks.* Biopreservation and Biobanking 2026 (Bastarache author feed).

Meta / policy piece on biobank visibility; note only for a
biobank-methods citation slot when writing about AoU/UKB/MVP/BioVU
comparability.

#### LOW — Bender A, Thomas MC, Scannell JW, Shaywitz DA, et al. *Artificial intelligence in drug discovery—what it is, where we stand and the path forward.* Nature Reviews Drug Discovery 2026 (Karczewski citations + Pritchard citations feeds).

Broad review; low signal for on-thread work but a candidate reference-list
citation for anyone writing about the ML-for-precision-health / drug
discovery boundary.

### Scholar alerts — keyword feeds (08-12 batch)

#### HIGH — Ding L, Tian P, Yu F, Jiang Z, Qi Y, Zhang A, Liu Y, et al. *Effect of clonal hematopoiesis of indeterminate potential on long-term survival in patients with arrhythmias.* Journal of Translational Medicine 2026 (`intitle:"clonal hematopoiesis"` keyword feed).

CHIP × arrhythmia long-term survival — extends the CHIP → cardiovascular
outcomes story from the canonical MI / heart-failure axis into the
arrhythmia population specifically. Directly on the CHIP sub-thread of
INTERESTS.md. Read for effect-size magnitude and whether they stratify
by driver-gene (DNMT3A vs. TET2 vs. ASXL1 patterns), which is where the
mechanistic differentiation of CHIP-CVD associations is currently
active.

#### MEDIUM — Pratap A, Mooney S, Heagerty PJ, Areán P, et al. *[All of Us Research Program article title in TXT alert].* 2026 (`All of Us research program` keyword feed).

AoU-cohort descriptive / methods paper. Read the alert-linked article
for whether it introduces a re-usable AoU analytic pattern (mHealth,
depression, WA-cohort composition are typical Pratap topics) or a
one-off descriptive study.

#### MEDIUM — Pelicioni PHS, Waller S, Chan L, Krishnan AV, Lord SR, et al. *Real-world gait changes preceding Parkinson's disease diagnosis in a population-scale UK biobank cohort.* Journal of Neural Transmission 2026 (`UK Biobank` keyword feed).

Prodromal-PD gait phenotypes from wearables in UKB — sits on the
*pre-symptomatic carrier phenoconversion prediction from longitudinal
biomarker trajectories* rising sub-thread (Ran/Benatar Nature Medicine
ALS template). Portable framing for BRCA incident-cancer, APOL1 CKD
conversion, or hereditary-cancer-syndrome trajectory work. Not the
primary rare-disease disease of interest, but the *pre-symptomatic
trajectory prediction from wearable-derived phenotypes* methodology is
directly on-thread.

#### MEDIUM — Zheng H, Wang S, Shafrin J, Bheema S, Spurrier K, et al. *Clinical and Economic Burden of Diseases with Accelerated Approval Therapies: Evidence of Unmet Patient Need.* Therapeutic Innovation & Regulatory Science 2026 (`rare diseases` keyword feed).

Regulatory-science piece on burden of disease for rare / accelerated-
approval-therapy indications. Reference-list mining candidate for the
rare-disease sub-thread; low methodological novelty but useful policy
context for the CF / APOL1 / hereditary-cancer therapeutic-development
side.

#### METHODS-WATCH — Zhu Y, Ye Z. *Prioritizing Parkinson's disease risk-associated mitochondrial candidate genes via multi-omics integrative analysis.* Clinical Neurology and Neurosurgery 2026 (`variant interpretation` + `mendelian diseases` keyword feeds).

Multi-omics integrative analysis to prioritize candidate genes at
GWAS loci; adjacent to the fine-mapping and multi-omics-augmented PRS
sub-threads. Read for the integration protocol (which omics layers are
stacked, and how disagreements are resolved), not the PD content per se.

#### LOW — Yakdan S, Warner B, Ghogawala Z, Ray WZ, Bydon M, et al. *Author Correction: Clinically-guided models or foundation models? predicting cervical spondylotic myelopathy from electronic health records.* npj [Digital Medicine / Health, TBD] 2026 (`electronic health records` + `Foundation models + EHR` keyword feeds).

Author correction on a previously-tracked FM-vs-clinically-guided model
comparison piece. Note only for citation-tracking accuracy.

#### LOW — Xu SW. *Knowledge proliferation: a domain-driven framework for multi-faceted knowledge graph generation from business data.* World Wide Web 2026 (`knowledge graph` keyword feed).

Off-domain (business KG). Skip.

#### LOW — Onwanezi OG, Ikebudu AP, Adione NMB, Ojiakor EJ. *Drug repurposing for diabetes: In silico determination of approved drugs against human glucokinase receptor.* Open Access Research J 2026 (`drug repurposing` keyword feed).

Chemistry-only in-silico repurposing without a clinical-evidence loop —
explicitly the class INTERESTS.md deprioritizes ("Lower interest in
target-only or chemistry-only pipelines without a clinical-evidence
loop"). Skip.

#### LOW — Azmat J, Shehzad K, Siddiqui SH, Zafar R, Nadeem S, et al. *Correlation between clinical presentation and histological patterns in granulomatous inflammation.* Genetics and Molecular Research 2026 (`autoimmune disorders` OR `autoimmune diseases` keyword feed).

Off-thread (histopathology). Skip.

### Scholar alerts — author feeds (08-13 batch)

#### HIGH — Naderian M, Smith JL, Dikilitas O, Hamed ME, et al. *Additive value of polygenic risk and family history for coronary heart disease risk stratification in two diverse US cohorts.* American Journal of Human Genetics 2026 (Jian Yang author feed).

Whether PRS, monogenic familial hypercholesterolemia, and family history
are additively informative for CHD risk prediction across self-identified
race/ethnicity groups in two diverse US cohorts (likely MVP + one other
US biobank based on cohort framing). Directly on the *composite risk
models stacking PRS with rare pathogenic variants* rising sub-thread on
INTERESTS.md, executed as an AJHG-tier paper with explicit multi-ancestry
framing. Follow-ups worth checking on full-text: (1) exactly which two
US cohorts (MVP + AoU is the strongest read); (2) whether the additive
model wins consistently across SIRE strata or only in some; (3) whether
FH prevalence is derived from ClinVar-based variant curation or
laboratory-reported PVs; (4) whether they report reclassification /
NRI vs. Framingham baseline. This is the CHD companion to the Peng
et al. early-onset BC framing from the prior report — both are
composite-risk papers, both are lineage-adjacent, both should be read
alongside.

#### HIGH — Nøhr AK, Overby MG, Nielsen MM, Torp EA, et al. *Combining genome-wide polygenic scores with registry data for colorectal cancer risk-based screening.* British Journal of Cancer 2026 (Jian Yang author feed).

PRS + registry data for CRC risk-based screening across diverse
ancestries and tumor characteristics, compared against the current
standard (faecal immunochemical test / FIT). Directly on-thread for
Zeng's CRC genetic-epi lineage AND the *composite-risk-tied-to-a-clinical-
decision* framing that INTERESTS.md's ML-for-precision-health thread
prioritizes ("who to screen"). Read for whether the PRS + registry stack
outperforms FIT at fixed specificity, and whether the ancestry
comparison finds portability degradation of the PRS component (which
would motivate the multi-ancestry-PGS work as a screening-utility
argument, not just a fairness argument).

#### HIGH — Qi X, Belloy ME, Gu J, Liu X, Tang H, He Z. *Robust Inference With Ghostknockoffs in Genome-Wide Association Studies With Sample Relatedness.* Genetic Epidemiology 2026 (Joshua C Denny author feed).

Extends the knockoff-based causal-variant identification framework to
GWAS with sample relatedness — the setting AoU/UKB/MVP/BioVU
routinely present, and one that has been a stumbling block for
individual-level knockoff methods. If robust, this is the tool the
PheWAS / genetic-epi thread should adopt for the causal-variant
identification step downstream of PheWAS discovery. Read alongside
CIT-Lasso (same batch) as the summary-statistics counterpart and the
He et al. Genome Biology piece for cross-check. Also read for whether
the "sample relatedness" they handle spans the full family / cryptic-
relatedness / population-structure spectrum or just one slice.

#### HIGH — Szmulewicz AG, Gerlovin H, Rezaee N, Robb W, et al. *Lithium for the prevention of suicide in US veterans: a target trial emulation.* BMJ Mental Health 2026 (Miguel Hernán citations feed).

Target trial emulation using EHR + administrative claims from US
veterans with bipolar or MDD to estimate effects of lithium initiation
and continuation on suicide deaths and non-lethal suicidal behaviors.
Canonical TTE-in-EHR execution from Hernán's lineage, directly on-thread
for both the causal-inference-and-pharmacoepi bench and the substance-
use / psychiatric multimorbidity applications. Read for the specific
choices around treatment-adherence definition, the two nested trial
structure (initiation vs. continuation as separate estimands), and how
they handle prescription-fill vs. drug-taking mismatch. Directly
portable to the CFTR-modulator persistence / HRT-persistence questions
where the same "initiation vs. continuation" decomposition is the
right estimand structure.

#### HIGH — He Z, Chu B, Yang J, Gu J, Chen Z, Liu L, Morrison T, et al. *CIT-Lasso: a scalable approach beyond guilty by association for identifying causal variants from genome-wide summary statistics.* Genome Biology 2026 (Jian Yang author feed).

Summary-statistics-only fine-mapping to distinguish likely causal variants
from correlated tag variants; genome-wide, doesn't require individual-
level data. Directly on-thread for the genetic-epi / fine-mapping
sub-thread. Compare against the Ghostknockoffs approach above (which
also targets causal-variant ID, but through a different framework);
together these two pieces are a good cross-check for whether summary-
stat and individual-level methods now converge. Bookmark for the next
GWAS-follow-up analysis on the pharmacogenomic-modifiers / drug-target
MR sub-thread.

#### HIGH — Chatzipanagiotou OP, Charalampous CM, Cordle A, Elemosho A, Alizai Q, Mevawalla A, Arena L, Ejaz R, Pawlik TM. *Genetic Ancestry and Colorectal Cancer in the All of Us Dataset.* JAMA Network Open 2026 (NCBI AoU PubMed alert, 08-13).

Genetic ancestry × CRC in AoU — sits at the intersection of Zeng's CRC
genetic-epi lineage AND the AoU-biobank-methods thread. JAMA Network
Open placement suggests a clinical-epi framing rather than a
methods-first paper. Read for the ancestry-classification protocol
(genetic-PCA vs. self-identified), the case ascertainment (EHR
phecode-based vs. registry-linked), and the effect-size direction
relative to prior SEER / registry-based ancestry work.

#### HIGH — Kather JN et al. (van Haag F, Clusmann J, ... Kather JN, Schneider KM, Schneider CV). *Machine learning for population-level risk prediction of future cholangiocarcinoma.* EBioMedicine 2026 (NCBI AoU PubMed alert, 08-13).

Population-level ML risk prediction for a rare cancer using cross-cohort
EHR + biobank data. Directly on-thread for the *ML tied to a clinical
decision* framing that INTERESTS.md's precision-health thread requires
("who to screen"); rare-cancer application means small event count and
positive-predictive-value challenges are front-and-center. Read for the
cohort composition (US contribution likely includes AoU based on the
saved-search hit), the validation strategy, and whether the model's
top-risk stratum has actionable follow-up (imaging, biomarker
surveillance).

#### HIGH — Mehanna H, Rogado J, Calvo AC, González V, et al. *Toward a Better Paradigm for Head and Neck Cancer Treatment Applying AI (HNC-TACTIC): Protocol for an International Cohort Study of Electronic Health Records.* JMIR Research Protocols 2026 (Chenjie Zeng author self-alert).

International-cohort EHR study protocol for AI-assisted HNSCC treatment
optimization. On the Zeng self-citation feed (means it links to Zeng's
own work). Read as a *cohort-design template* for the EHR-based
multi-site outcomes work the KGs-and-EHR-representation thread now
needs — this is the kind of protocol that codifies eligibility,
outcome-definition, and interoperability decisions before data flow
starts, which is exactly the *interoperability-consequences* sub-thread
of your knowledge-representation-in-EHRs framing. Follow-ups worth
checking: registered outcome set, whether it uses OMOP / FHIR
harmonization, and whether it publishes the phenotype definitions
computable-openly.

#### HIGH — Wang C, Hu J, Lei Y, Li J, Zhang Y, Hu K, Liu L, Su X, et al. *Cross-trait genetic architecture between breast cancer and psychiatric disorders.* iScience 2026 (Jian Yang author feed).

Cross-trait genetic-correlation and overlap between BC and psychiatric
disorders using GWAS summary statistics. Directly on the *cross-trait
shared genetic architecture and multi-trait triangulation* rising
sub-thread on INTERESTS.md, and adjacent to Zeng's early-onset BC
lineage. The BC × psychiatric axis is under-explored relative to
BC × cardiometabolic; this fills a hole. Read for the specific
psychiatric traits covered (MDD, BIP, SCZ, ANX, PTSD each have
different genetic-arch profiles), the MiXeR / LDSC / conditional-FDR
family method used, and any local-genetic-correlation hits at loci
Zeng has published on.

#### METHODS-WATCH — Hu S, Zhu P, Wu S, Gao S, Wang R, Liu F, He Y, Han Z, et al. *Genome-wide association study highlights 44 loci for transient ischemic attack and shared genetic architecture with stroke.* medRxiv 2026 (Jian Yang author feed).

Largest TIA GWAS meta-analysis (n≈1.3M European) with 44 loci and
shared-architecture analysis with stroke. Adjacent to the cardiovascular-
genetics thread; useful as a locus-set citation, not primary interest
for the current disease list. Bookmark.

#### METHODS-WATCH — Hernandez U, Mawass W, Matheson J, Masel J. *Rare variants drive high variance in human ancestral fitness at mutation-selection-drift balance.* bioRxiv 2026 (Konrad Karczewski author feed).

Population-genetics theory / simulation piece on how rare variants
drive high fitness variance at mutation-selection-drift balance —
speaks to why rare-variant burden analyses need careful
allele-frequency stratification and why "rare = deleterious" doesn't
uniformly hold across selection regimes. Bookmark for the *variant
interpretation* thread as a theoretical framing citation.

#### METHODS-WATCH — Sun SD, Liu J, Xu P, Hu Y, Zhang MJ, Zhang J. *MUGO: Differentiable Combinatorial Optimization for Causal Variant Discovery in the Non-coding Genome.* KDD V.2 2026 (Stephen B Montgomery author feed).

Differentiable combinatorial optimization for non-coding causal-variant
discovery — companion in spirit to CIT-Lasso and Ghostknockoffs above,
but with an ML-optimization framing. Bookmark for the fine-mapping /
non-coding-variant sub-thread if it's reactivated.

#### METHODS-WATCH — Reichenpfader D, Zaghir J, Cécilia-Joseph E, et al. *The consensus-based CINEX guideline for reporting clinical information extraction studies.* JAMIA 2026 (9 new citations to Vivek Natarajan).

Reporting-guideline for clinical information-extraction studies. On the
knowledge-representation-in-EHRs / NLP-derived-representations
sub-thread. Read for the reporting-checklist items (which representation
choices to report, which evaluation metrics to standardize on) —
directly useful when writing a note-to-phecode / note-to-HPO extraction
methods paper.

#### METHODS-WATCH — Velioğlu H, Çiçek Y, Çelik M, Bayraktar A. *A cross-platform Mendelian randomization study of mitochondrial DNA copy number across psychiatric disorders.* Research Square 2026 (Jian Yang author feed).

Cross-platform MR for mtDNA-CN → psychiatric disorders. Adjacent to
somatic-mosaicism thread (mtDNA-CN is a biomarker of mitochondrial
biology and blood cell composition, both of which show CHIP-related
drift). Bookmark.

#### MEDIUM — Zheng S, Wu Y, Li A, Wu Z, Liu Z, Wang H, Jia X, et al. *Genetic Predisposition and Pharmacological Effects Shape the Divergent Effects of Type 2 Diabetes on Atherosclerosis.* Genomics, Proteomics & [Bioinformatics TBD] 2026 (Denny + Pritchard citations feeds).

T2D × atherosclerosis with a genetic-predisposition-plus-pharmacology
decomposition. Adjacent to the drug-target MR / pharmacogenomic-modifier
sub-threads. Read only if extending into T2D-CVD interaction analyses.

#### MEDIUM — Son H, Hwang I, Lee SW, Kim Y. *Safety and Efficacy of GLP-1 Receptor Agonists in Adults With Epilepsy, Obesity, and Type 2 Diabetes.* Annals of Clinical and Translational Neurology 2026 (Joshua C Denny author feed).

GLP-1 RA in the epilepsy + obesity + T2D triple-comorbidity population.
On-thread for the GLP-1 RA drug-class watch as a triple-comorbidity
subgroup analysis; complements the Mann pooled analysis above. Bookmark.

#### MEDIUM — Groeneveld J, Perlaza D, Olivé C, Grangeon L, Tesi N, et al. *APOE and genetic risk variants influence Alzheimer's disease onset in carriers of an extra copy of APP, with and without Down syndrome.* [J TBD] 2026 (6 new citations to Konrad Karczewski).

Genetic-modifier study for AD onset in APP-duplication and DS carriers.
Composite-risk framing (genotype × background modifier) analogous to the
APOL1 N264K story from prior report, but for AD. Read only if extending
into the AD / neurodegeneration lineage.

#### LOW — Kim Y, Gu K, Park C, Park C, Schmidgall S, Heydari AA, et al. *Capable language models can outgrow the benefits of collaboration.* Nature Machine Intelligence 2026 (Zhiyong Lu author feed).

LLM multi-agent architecture argument. Off primary clinical-agent
sub-thread.

#### LOW — Vo T, Luu ST, Nguyen LM. *An unsupervised graph attention network empowered by large language models for knowledge graph grounded medical question answering.* Computers and Electrical Engineering 2026 (Peter Szolovits author feed).

KG-grounded medical QA with LLM+GAN attention. Off the clinical-decision-
grounded LLM sub-thread; note only.

#### LOW — Xu Z, Agrawal P, Asadi K, Chen T, Hu C, Johnson J, et al. *The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers.* arXiv 2026 (Marinka Zitnik author feed).

Retrieval-architecture argument; off-thread.

#### LOW — Zhou S, Dehkordi MKH, Yao W, Liu H, Sen P, Deek FP, et al. *Enhancing Electronic Health Records Annotation with a Cluster-Focused Combination Algorithm and Interface Terminologies.* [Engineering Systems TBD] 2026 (George Hripcsak + Pascal Brandt author feeds).

Interface-terminology / EHR-annotation clustering algorithm — adjacent
to knowledge-representation-in-EHRs / concept-normalization sub-thread
but the venue and framing look non-clinical; note only.

#### LOW — Jiomekong A, Tiwari S, Auer S. *Semantification of scientific articles using knowledge graphs.* The Electronic Library 2026 (Tiffany J Callahan author feed).

Off-domain KG (scientific-article semantification). Skip for clinical
KG work.

#### LOW — Simmons J, Hyder S, Lertwilaiwittaya P, Smith C, et al. *Hypertrophic Cardiomyopathy in a Patient With BAG3-Associated Charcot-Marie-Tooth Disease: A Rare Cardiac Manifestation.* Circulation 2025 (3 new citations to Lisa Bastarache).

Single case report cross-referencing Bastarache-lineage PheWAS work
(BAG3 pleiotropy). Note only.

#### LOW — Zhang Y, Li J, Luo Y, Liu S, Liu J. *Integrative Analysis of Gut Microbiota, Plasma Metabolome, and Gene Expression Identifies Causal Mediators in Graves' Disease Pathogenesis.* Frontiers [J TBD] 2026 (4 new citations to Kai Wang).

Multi-omics for Graves' disease — off-thread.

#### LOW — Rogness DC, Sievert EP, Vartabedian VF, Bernard SM, et al. *Chemoproteomic discovery of a brain-penetrant, covalent NLRP3 inhibitor that binds a novel allosteric pocket.* British Journal of Pharmacology 2026 (3 new citations to Daniel Kastner).

Chemistry-only NLRP3 discovery — off the clinical-VEXAS/CHIP thread.

#### LOW — Ikeda N, Mizukami K, Yamada R, Toyoda H, Aoi T, et al. *Characterization of putative germline pathogenic variants in 27 candidate cancer-predisposing genes in 813 cats using a feline-specific multiplex targeted sequencing.* Scientific Reports 2026 (Chenjie Zeng author feed).

Off-species. Note only that it hits the Zeng "hereditary cancer" author
feed due to keyword overlap.

#### LOW — Tranberg A, Creignou M, Mortera-Blanco T, Bernard E, et al. *Real-world investigation of germline predisposition to myelodysplastic syndromes.* Blood Advances 2026 (Chenjie Zeng author feed).

MDS germline predisposition real-world study; adjacent to the CHIP /
somatic-mosaicism thread if extending toward MDS-related germline
questions. Otherwise medium-low.

#### LOW — Oshi M, Kawashima K, Sugimori M, Yamada A, Shah Z, et al. *Somatic BRCA alterations in breast cancer are associated with distinct biological and clinical patterns according to germline BRCA status.* ESMO open 2026 (Chenjie Zeng author feed).

Germline × somatic BRCA interaction in BC; adjacent to Zeng's BC lineage
but not a HIGH because it's a single-institution-tier finding rather
than a population-genetics or PGS paper. Bookmark.

#### LOW — La J, Jafari O, Nannini K, Do NV, Brophy MT, et al. *Temporal Validation of the Electronic Health Record Cancer-Associated Thrombosis Model in Patients with Low Bleeding Risk.* Research and Practice in Thrombosis and Haemostasis 2026 (Chenjie Zeng author feed).

External temporal validation of an EHR-based cancer-associated VTE
model. Adjacent to the ML-for-precision-health thread as a
model-validation exemplar; note only.

---

### Scholar alerts — carry-over items reaffirmed

Several 08-13 alerts re-featured papers already flagged in the 08-08
report (e.g. Bender AI-drug-discovery Nature Reviews review;
Jiang pig DNA methylation from the Montgomery feed). Not re-analyzed
here.

---

## What's NOT in the report

- **bioRxiv / medRxiv Subject Collection Alerts** — none surfaced in the
  searched window; the on-thread medRxiv items above (Li et al. SV
  PheWAS framework; Hu et al. TIA GWAS) came via author-feed
  cross-references rather than subject-collection alerts.
- **NCBI My-NCBI What's-New batches** — I sampled the 08-13 AoU batch
  (see two HIGH entries above) but did not open every daily UKB or
  drug-repurposing fire in the window. Anything of on-thread interest
  that was missed will be recaptured in the next report; the volume
  suggests these three saved searches together fired ~18 emails in
  the window with mostly single-item on-thread yield.
- **Substack / newsletters** — none flagged on-thread in this window;
  the ML / AI newsletter stream was noise for the clinical-EHR-genomics
  focus.
- **arxiv.org daily category mailings** — the raw `cs`, `stat.AP`,
  `q-bio` daily mailings from no-reply@arxiv.org are the upstream source
  that feeds the arxiv-digest pipeline; individual papers surfaced via
  the digest are covered in the arxiv-digest section above rather than
  re-listed from the raw mailings.

## Next steps to consider

1. **Read Li et al. SV PheWAS framework medRxiv full text.** Highest-
   signal single item for the PheWAS-infrastructure thread this window —
   if the framework is portable to AoU/BioVU, this changes what SV
   discovery looks like at scale.
2. **Bundle Naderian AJHG + Nøhr BJC + Dutta Cell Genomics** into a
   short composite-risk / PGS-as-instrument thread update — three
   independent-cohort applications of the PRS-stacked-with-something-else
   framing (family history, screening test, proteomics) landed in one
   week.
3. **Add Vossler egg-computation and Wood perinatal-TTE to the
   causal-inference tooling shortlist**, alongside the Noma TTE R-package
   from the prior report. The LLM-assisted variant is a candidate for
   the next hospital-flow / pharmacoepi analysis where the causal DAG
   has expert-known edges.
4. **Compare Ghostknockoffs (Qi/Denny), CIT-Lasso (He/Yang), and MUGO
   (Sun/Montgomery)** side-by-side for the next post-PheWAS causal-
   variant identification stage — three converging methods, three
   different framings, worth benchmarking on one shared locus.
5. **Cite Szmulewicz lithium TTE** as the reference case for the
   initiation-vs-continuation two-nested-trial structure when writing
   up the CFTR-modulator persistence or HRT-persistence analyses.
6. **Follow-up on the Mann SELECT/FLOW/SOUL pooled paper** for the
   subgroup / eGFR-strata heterogeneity structure — sets the RCT
   triangulation benchmark for any AoU / MVP observational
   GLP-1 RA renal analysis.

_Report generated 2026-08-13 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-13 → next scheduled run._
