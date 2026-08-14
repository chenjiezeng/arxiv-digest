# Research digest report — 2026-08-14

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-08-08 12:36Z → 2026-08-14 13:00Z** (~6 days since the
last research-digest report, covering four arxiv-digest cron runs
[08-10 empty, 08-11 five, 08-12 two, 08-13 one] plus three
Google Scholar alert batches [08-11 night author-feed, 08-12 day
keyword, 08-13 both], the 08-13 medRxiv Collection Alert and the
08-14 bioRxiv Collection Alert, three PubMed What's-New batches
[08-12, 08-13, 08-14], and the 08-14 Nature Medicine v32 n8 issue).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-10.md` → `2026-08-13.md`) | 08-10 → 08-13 (02:56Z crons) | 4 daily runs. 08-10: 0 (empty). 08-11: 5 (Chen IPW clustering on carboplatin BC, CAN-FLOW UKB CMR, Bandreddi Tobit/hurdle CHIP, motor-insurance DAG skip, VOICE spatial txm skip). 08-12: 2 (egg-computation LOS + Wood perinatal TTE). 08-13: 1 (Porotsky ICA sensitivity). |
| Google Scholar alerts (author feeds, 08-11 batch) | 08-11 23:58Z | ~25 author feeds fired: Lisa Bastarache (**Li M SV-PheWAS scalable framework**), Joshua C Denny (same paper cross-hit), Jian Yang (**Dutta PGS × plasma proteomics Cell Genomics**), Chenjie Zeng self (Prokunina-Olsson bladder cancer GWAS meta-analysis), Konrad Karczewski (CTNND1 gastric-cancer WES), Peter Szolovits (LLM benchmarking + explainability review), Daniel Kastner (CDC42 pyrin inflammasome variants ×2), Pritchard/Natarajan/Karczewski (Bender NRDD AI-in-drug-discovery review — 3 cross-hits), George Hripcsak (GLP-1 RA vs anti-diabetic drugs prostate cancer / ADT), Miguel Hernán (Yu YH insulin-initiation TTE), Yuan Luo (BC × RA multi-omics), Leo Anthony Celi (AI-authorship-governance MIT Case). |
| Google Scholar alerts (keyword feeds, 08-12 batch) | 08-12 13:04Z | 11 keyword feeds fired: `electronic health records` + `Foundation models × EHR` (Yakdan npj Digit Med correction — off-thread), `rare diseases` (Zheng orphan-drug economic burden), `All of Us research program` (Pratap AoU + digital-health perspective), `UK Biobank` (Pelicioni gait-changes-preceding-PD), `variant interpretation` and `mendelian diseases` (Zhu multi-omics PD candidate genes), `clonal hematopoiesis` (Ding CHIP × arrhythmia survival — HIGH for CHIP thread), `knowledge graph` (Xu domain-driven KG generation — off-thread), `drug repurposing` (glucokinase docking — off-thread), `autoimmune diseases` (granuloma histology — off-thread). |
| Google Scholar alerts (author + keyword feeds, 08-13 batch) | 08-13 09:13Z + 13:33Z | ~30 feeds fired. **HIGH-signal**: Ritchie group's *AI-based multimodal integration of genomics and EHRs* (Nat Rev Genet 2026; hit `electronic health records` + `Foundation models × EHR` + author-feeds); Bandreddi Tobit/hurdle CHIP (cross-hit `intitle:"clonal hematopoiesis"`); APOL1 Aldana Peréz SLE-LN meta-analysis; `All of Us` Kachhadia retinal-artery-occlusion → dementia with prespecified negative-control outcomes; Chenjie Zeng self-feed Mehanna HNC-TACTIC EHR protocol; Denny/Bastarache/Hripcsak cross-hit Zhou EHR annotation with interface terminologies + Qi *Ghostknockoffs* Genet Epi 2026. Notable multi-author-feed hit: Zheng T2D × atherosclerosis Genomics Proteomics Bioinformatics (Denny + Pritchard). |
| PubMed What's-New (efback / My-NCBI), 08-12 batch | 08-12 12:30Z | 3 saved-search batches (drug repurposing, UK Biobank, All of Us). |
| PubMed What's-New (efback / My-NCBI), 08-13 batch | 08-13 12:32Z | Same 3 saved searches; incremental. |
| PubMed What's-New (efback / My-NCBI), 08-14 batch | 08-14 12:45Z | Same 3 saved searches. UK Biobank batch = 16 items; key hits: **Zhang MJ *Nat Genet* 2026 proximal-SNP causal-effect correlations under stabilizing selection** (Alkes Price group); **Kodji E PLoS Comput Biol Mondrian cross-conformal PGS for CV/renal complications in T2D across ancestries**; **Gkatzionis *Stat Med* negative-control outcomes for selection bias in MR**; UKB Feng physical-activity × T2D age-specific dose-response; He UKB proteomics pre-diagnostic liver-cirrhosis biomarkers. All of Us batch = 6 items (mostly small; Parasuraman actinic-keratosis PGS is the notable one). Drug-repurposing batch = 9 items (Alasbily SGLT2i Th17/Treg mechanism review the notable one). |
| bioRxiv Subject Collection Alert (08-14) | 08-14 00:06Z | Bioinformatics + Genetics + Genomics + Immunology. Standout: **Huynh et al. "Human-supervised Agentic AI for Hypothesis Generation and Experimental Assistance in Drug Repurposing"** (bioRxiv 2026.04.20.719538v2) hits both the drug-repurposing thread and the agentic-LLM thread. Also **Nishu Nehra "A Guided AI Framework for Customizable and Efficient Harmonisation to the OMOP Common Data Model"** on the EHR-phenotyping/OMOP thread. |
| medRxiv Subject Collection Alert (08-13) | 08-13 00:05Z | Endocrinology + Epidemiology + Genetic & Genomic Medicine + Health Informatics + Nephrology + Oncology + Pediatrics. Standouts: **Zolensky/Damrauer/Verma "Longitudinal Clinical Foundation Models Augmented with Genomics for Early Detection and Risk Stratification of Inherited Cardiomyopathy"** (EHR-FM × composite-risk trifecta); **Rentsch CT et al. "Genotype-predicted drug response phenotypes and their co-occurrence with dispensed medicines among 738,531 UK Our Future Health participants"** (PGx-modifier-of-persistence rising sub-thread, huge n); **Kramer & Rzhetsky "Clinical care intensity atlas of 505 diseases from 90 million people"** (EHR phenotyping at unprecedented scale); **Rowan CG "Integrating Causal Inference into Pharmacovigilance: TTE for Proactive Signal Detection of Atorvastatin Initiation in Medicare"**; **Bowers MVP DASH-diet × kidney-decline**; **Wang W multi-omics-augmented PRS in diverse populations**; **Morgan/Kenny FH-implementation-genomics ASCVD** (Geisinger MyCode-lineage). |
| Nature Medicine v32 n8 (08-14 ealert) | 08-14 06:42Z | TOC-only alert; no per-article deep-read yet. |

> Caveat: Scholar / NCBI / rxiv-collection emails contain title, authors,
> venue, and the first ~2–3 lines of each abstract only. The reports
> below contextualize that metadata against your research threads;
> nothing here reflects full-text reading. `arxiv-digest` entries include
> the full abstract because the pipeline captures it. Author lists are
> truncated to first 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Seventeen HIGH items surfaced this window, clustering into six knots
each of which stands on its own:

**EHR foundation models × composite genomic risk cluster (3 items).**
Venkatesh & Ritchie *Nat Rev Genet* 2026 — the field-defining
*"AI-based multimodal integration of genomics and EHRs"* review that
fires simultaneously across three of your keyword feeds and reads as
the canonical framing citation for the EHR-FM thread going forward.
Zolensky/Damrauer/Verma medRxiv 2026 — **longitudinal clinical
foundation model augmented with genomics** for early detection +
risk stratification of inherited cardiomyopathy in Penn Medicine EHR;
this is the *first paper I've seen* that stacks CLMBR/MEDS-lineage EHR
sequence models with a genomic layer for a specific ACMG-actionable
disease. Verma et al. earn a re-cite in your composite-risk thread.
Kim MG & Woo HJ *Sci Rep* 2026 (via Vivek Natarajan cross-hit) — a
Monte Carlo × LLM framework quantifying model-and-architecture-dependent
variability in synthetic-patient simulations: bookmarks the audit layer
your *pretraining-contamination audits for foundation-model benchmarks*
rising sub-thread wants for the LLM-synthetic-EHR-generation branch.

**PheWAS / structural-variant infrastructure cluster (1 big item).**
Li M, Peng W, Zhang L, Huang T, Wei C, Liu Z, Fang L 2026 (Research
Square rs-10237876; Bastarache + Denny author-feed cross-hit) — *A
scalable framework enables phenome-wide association of structural
variants in biobank cohorts.* This is the SV-PheWAS
infrastructure paper the *PheWAS / phecode infrastructure* thread
has wanted: population-scale SV callsets → cohort-level PheWAS at a
scale that lets SVs sit alongside SNVs and CNVs in the variant
interpretation stack. Directly portable to AoU / UKB / MVP once SV
callsets stabilize. Read for the "synthesis into cohort-level SV
matrix" method and its scaling behavior; this is a candidate to
propagate through the PheWAS-of-PheWAS design instinct.

**Composite-risk / PGS × multi-omics × ancestry cluster (3 items).**
Dutta D, Zhang J, Guo X, Quint R, Rooney MR et al. *Cell Genomics*
2026 (Jian Yang author feed) — 21-cancer PRSs × 4,955 plasma proteins
in cancer-free UKB participants, identifying cancer-related proteins
and trans-regulated protein networks. This is the *multi-omics-augmented
PRS for cancer* extension that your rising sub-thread has been tracking
in cardiometabolic/psychiatric traits. Cross-check against your
Nightingale/Olink stack instinct. Wang W, Williams J, Gillman MG,
Raffield LM, Franceschini N, Ibrahim JG, Zhang H, Li X medRxiv
2026.08.10.26360136 — *Integrating genomic and proteomic data improves
complex trait prediction in diverse populations.* On-thread for
multi-omics-augmented PRS AND for cross-ancestry portability
simultaneously; ~65k n implied by the diverse-population framing.
Kodji E, Attaoua R, Haloui M, Hishmih C et al. *PLoS Comput Biol*
2026 — **Mondrian Cross-Conformal Prediction for PGS-based CV/renal
complication prediction across ancestries in T2D.** This is the
*PGS calibration under ancestry shift* paper, formalized with a
conformal-prediction machinery — bookmark for the PGS-portability
sub-thread. Together the three items advance the PGS discussion from
"add proteomics" and "add ancestry" to a proper calibration
methodology.

**Causal inference & pharmacoepi cluster (5 items).** Vossler P,
Ouyang J, Guo FR, Huang A, Shojaie A, Zier L, Xia F, Feng J arXiv
2608.10339 — *Expert-guided g-computation with LLMs* for causal
effects on care-timing outcomes (LOS). This is the highest-yield
match yet for your *agentic / human-in-the-loop
observational-causal-inference pipelines* rising sub-thread: the
LLM-assisted layer scales expert reasoning *only for the components
unidentifiable from data*, keeping the causal DAG discipline intact.
Read against Chou/Kallus oci-agent and Li et al. HTE-for-trial-design.
Wood ME, Platt RW, Hutcheon JA, Cohen JM, Latour CD, Margulis AV,
Petito LC, Grandi SM arXiv 2608.11108 — perinatal-pharmacoepi TTE
extension covering *changes to pregestational treatment regimes*
(e.g., T2D meds continued vs. modified at conception); the natural
follow-on to Noma's TTE R-package tutorial from the prior window's
report. Directly applicable to your GLP-1 RA / SGLT2i / HRT / CFTR
modulator watchlist whenever the exposure is a *regime change* not a
point initiation. Rowan CG, Tazare J, Tran M, Srivastava S, Dreyer NA
medRxiv 2026.07.01.26356874 — **TTE for proactive signal detection**
in pharmacovigilance, applied to atorvastatin initiation in Medicare.
This is the *pharmacovigilance-as-TTE* framing your causal-inference
thread should track — competes with the classical
disproportionality/self-controlled-case-series stack. Chen R, Zuo S,
Stevens W, Pollack S, Xi W, Petito L, Zhao L, Zhang H arXiv
2608.09839 — clustering-informed IPW for the *carboplatin dose
response × hypersensitivity risk in 966 breast-cancer patients*;
directly on both the causal-inference + BC (Zeng lineage) threads,
delivers subgroup profiles you'd want for chemo-tolerability
research. Vossler egg-computation + Wood pregnancy TTE + Rowan
atorvastatin-TTE are the three you'd bundle for a
*TTE-in-EHR-and-pharmacovigilance* pipeline update.

**Somatic mosaicism / CHIP cluster (2 items).** Bandreddi S, Zhang P,
Kelly RL, Machiela MJ, Albert PS arXiv 2608.09725 — *Tobit vs. two-part
hurdle mixed models* for longitudinal clonal fraction from the PLCO
study; the direct answer to "which mixed model do I use for
zero-inflated longitudinal clonal-fraction / VAF data?" Portable
methods paper for any longitudinal CHIP / mCA / LOY analysis in AoU
or UKB. Ding L, Tian P, Yu F, Jiang Z et al. *J Transl Med* 2026 —
CHIP × long-term survival in patients with arrhythmias. Directly on
the CV-outcomes-for-CHIP branch of your somatic-mosaicism thread;
adds the arrhythmia readout that sits alongside coronary/PAD in the
CHIP CV outcomes literature.

**Drug repurposing × agentic AI + OMOP harmonization cluster (2
items).** Huynh D-L, Asp E, Ballante F, Carreras Puigvert J, DeGrave A,
Karki R, Nader K, Östling P, Pokharel B, Rietdijk J, Schlotawa L,
Schmidt L, Seal S, Seashore-Ludlow B, Aittokallio T, Spjuth O bioRxiv
2026.04.20.719538v2 — *Human-supervised agentic AI for hypothesis
generation and experimental assistance in drug repurposing.* Hits
your drug-repurposing thread's explicit preference for
*explainable-hypothesis output* AND the *agentic / human-in-the-loop*
rising sub-thread simultaneously; note this v2 revision (posted
08-13) is worth pulling in the loop with the THBKG paper from the
prior report (Siu et al. 2608.05982) for a KG-plus-agentic-AI
repurposing framing. Nishu Nehra, Rohit Swami, Dharani Dadi, Ritika
Mishra, Umang Sharma, Pawan Verma, Manimala Sen, Nobal Kishor Dhruw,
Abhishek K Jha bioRxiv 2026.08.07.742453 — *A Guided AI Framework
for Customizable and Efficient Harmonisation to the OMOP Common Data
Model.* Directly on the *EHR phenotyping / OMOP* thread and the
knowledge-representation thread; read for how the "customizable"
angle handles concept-mapping heterogeneity across sites (BioVU vs.
AoU vs. MIMIC vs. UKB), a fidelity/portability question your
Knowledge-representation-in-EHRs thread explicitly tracks.

**Methods watch: MR + genetic-effect architecture (2 items).**
Gkatzionis A, Smith GD, Tilling K *Stat Med* 2026 — *Using
negative-control outcomes to detect selection bias in MR studies.*
Directly on the MR / triangulation sub-thread and cross-cuts the
prespecified-negative-control-outcomes approach used in the Kachhadia
AoU retinal-artery-occlusion → dementia study elsewhere in the
window. Bookmark alongside the Kachhadia paper for a NCO-in-EHR-and-MR
paired citation. Zhang MJ, Durvasula A, Chiang C, Koch EM, Strober BJ,
Shi H, Barton AR, Kim SS, Weissbrod O, Loh PR, Gazal S, Sunyaev S,
Price AL *Nat Genet* 2026 — *Correlations between causal effect sizes
of proximal SNPs vary with functional annotations and implicate
stabilizing selection.* Alkes Price group; deep genetic-architecture
methods that inform the *PGS residuals / polygenic-deviation designs*
framing (fine-mapping, LDSC-adjacent inference on selection
pressure at proximal SNPs). Bookmark for the PGS-tails-and-residuals
sub-thread.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-10 → 2026-08-13)

#### HIGH — Vossler P, Ouyang J, Guo FR, Huang A, Shojaie A, Zier L, Xia F, Feng J. *Expert-Guided g-computation with Large Language Models for Estimating Causal Effects on Timings: Applications to Hospital Quality Improvement.* arXiv 2608.10339v1 (stat.ME, 2026-08-11). Score 2.

Introduces *egg-computation*: pairs the causal-DAG literature with the
Gantt-chart representation of patient trajectories, and uses an LLM
pipeline to elicit expert reasoning *only for graph components that
are not identifiable from data*. Establishes identification under a
Gantt-chart causal model and shows in simulations that egg-computation
outperforms conventional causal inference when patient trajectories
have diverse causal structures and when interventions have no
historical data. Empirically applied to eleven candidate QI
interventions in an urban safety-net hospital, where the LLM-assisted
graphs and time-saved estimates were highly concordant with those of
human experts. This is the most on-thread hit yet for your rising
*agentic / human-in-the-loop observational-causal-inference pipelines*
sub-thread — LLMs used surgically for the identification-gap step,
not as end-to-end causal engines. Read alongside Chou/Kallus
oci-agent (arXiv 2607.22443) and Li et al. EHR-derived HTE for trial
design (arXiv 2607.16934); the three together sketch a design pattern
for LLM-augmented causal pipelines that keeps the causal discipline
intact. Directly portable to your pharmacoepi drug-class watchlist
whenever the "expert reasoning" step is where you get stuck (e.g.,
SGLT2 vs DPP-4 initiation graphs where clinical exclusions vary by
site).

#### HIGH — Wood ME, Platt RW, Hutcheon JA, Cohen JM, Latour CD, Margulis AV, Petito LC, Grandi SM. *Early Pregnancy Treatment Decisions: Designing Perinatal Pharmacoepidemiology Studies using Real-World Data.* arXiv 2608.11108v1 (stat.AP, 2026-08-11). Score 1.

Extends target trial emulation to the perinatal setting for the
under-treated case of *changes to pregestational treatment regimes*
(e.g., T2D medications continued, modified, or discontinued at
conception), where prior TTE-in-pregnancy work has focused on
initiation-vs-non-initiation for point treatments (vaccines,
antibiotics). Reviews methods for identifying pregnancy episodes in
routinely collected data, introduces candidate time-zero definitions,
and treats the immortal-time and selection-bias risks that dominate
this setting (right/left censoring, competing events, differences in
gestational length, varying etiologically susceptible periods). Fits
your *causal inference & pharmacoepidemiology* thread as the *regime
change* companion to Noma's TTE R-package tutorial from the previous
report (arXiv 2608.01625). Directly portable to (a) GLP-1 RA
persistence peri-pregnancy, (b) SGLT2i / statin peri-conception
discontinuation, (c) CFTR-modulator peri-pregnancy persistence
(actively debated in CF care), (d) HRT peri-menopause regime changes
(a similar life-stage TTE framing).

#### HIGH — Chen R, Zuo S, Stevens W, Pollack S, Xi W, Petito L, Zhao L, Zhang H. *Clustering Informed Inverse Probability Weighting Strategies for Causal Effect Estimation in Observational Studies.* arXiv 2608.09839v1 (stat.ME, 2026-08-10). Score 2.

Compares three IPW strategies for causal effect estimation when
treatment assignment is heterogeneous across subgroups: (i) standard
IPW, (ii) cluster-augmented IPW with cluster-specific PS models, and
(iii) a global PS model with estimated cluster membership as a
covariate. Simulations across n = 100–500 with/without latent
cluster structure show cluster-informed strategies reduce bias and
MSE under PS-omitted-covariate misspecification; MSE is lowest for
cluster-augmented IPW when true clusters exist, but the
membership-as-covariate global model gives lower bias and better CI
coverage at small n. Applied to 966 breast-cancer patients treated
with carboplatin, using generalized PSs to estimate the dose-response
relationship between number of treatment cycles and hypersensitivity
reaction risk — where clustering additionally yields
subgroup-specific dose-response profiles and PS diagnostic profiles.
This is a clean methods contribution for your causal-inference thread
that also lands in the BC lineage (Zeng disease-thread overlap).
Directly portable to any pharmacoepi setting where treatment
selection is site-heterogeneous (e.g., statin adherence across health
systems in the atorvastatin-TTE work below).

#### HIGH — Bandreddi S, Zhang P, Kelly RL, Machiela MJ, Albert PS. *Comparing Tobit and Two-Part Hurdle Models for Semi-Continuous Longitudinal Data with an Application to Clonal Hematopoiesis.* arXiv 2608.09725v1 (stat.AP, 2026-08-10). Score 1.

Rigorous mathematical treatment of when the mixed Tobit and two-part
hurdle models are equivalent for zero-inflated non-negative
longitudinal outcomes — with the elegant result that Tobit is a
special case of the hurdle model under a probit link for the binary
process. Simulations show the hurdle model is more flexible and
robust when its distributional assumptions match; the paper's
recommendation is to use Tobit only when its assumptions are
scientifically plausible and empirically supported. Applied to
longitudinal clonal-fraction measurements in the PLCO study for
somatic mosaicism dynamics with excess zeros, with estimates broadly
consistent with a naive linear model that ignored zero inflation but
with better inferential guarantees. This is exactly the *methodology
choice* your INTERESTS.md CHIP / VEXAS / LOY sub-thread has been
punting on: for any AoU / UKB longitudinal CHIP-VAF / mCA / LOY-cell-
fraction analysis, this paper gives you the framework and the
citation for the choice. Adjacent to Ji et al. *Biology* 2026 QC
layer for germline-vs-somatic contamination that INTERESTS.md
already tracks.

#### METHODS-WATCH — Porotsky S. *Inverse Confounding Analysis: An Exact Method for Quantifying the Significance of Confounding.* arXiv 2608.11991v1 (stat.ME, 2026-08-12). Score 1.

Extends E-value-style sensitivity analysis by parameterizing the
*complete* admissible set of joint distributions compatible with
observed exposure/confounder/outcome frequencies and pairwise
associations, and characterizes the stratification-based Risk Ratio
as a fractional-linear function of a single free parameter. Yields
exact analytic bounds over the entire configuration space rather than
only the worst case. Requires additional input parameters (marginal
frequencies) but rewards them with a much tighter and more
interpretable sensitivity range. Bookmark for the *causal inference &
pharmacoepidemiology* thread as a companion / competitor to
VanderWeele's E-value — worth trying on one of your existing
target-trial emulations to see how the admissible-range boundaries
compare to E-value lower bounds. Not on-thread by disease but exemplary
methods worth cribbing.

#### METHODS-WATCH — Kevopoulos K, Moscoloni B, Alheit B, Beeche C, Chirinos JA, Heinlein A, Peirlinck M. *Flow-based conditional cardiac anatomy generation for virtual cohorts.* arXiv 2608.09460v1 (cs.LG, 2026-08-10). Score 2.

CAN-FLOW is a two-step conditional normalizing-flow generator for
biventricular cardiac anatomies conditioned on sex / age / BMI,
trained on n=2,208 healthy UKB subjects. Beats cVAE baselines on
clinical-phenotype distributions, metadata-dependent trends, subgroup
variability, point-cloud coverage, and high-dimensional shape
variability — with the intended use of *virtual cohort* generation
for in silico clinical trial workflows. Adjacent to the biobank +
imaging thread (companion to the Sasson DXA JEPA paper in the prior
report) and to the *digital twins from EHR data* rising sub-thread on
EHR foundation models. Not directly on the clinical-outcome pipeline,
but worth bookmarking for the *virtual cohort as substrate for
counterfactual analyses* method — natural bridge to egg-computation-
style HTE analyses.

#### SKIP — Luo X, Tao Y, Zeng H, Wang S, Ouyang C, Zhu M, Liu K, Chen S, Liu J. *VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression.* arXiv 2608.08366v1 (cs.CV, 2026-08-08). Score 1.

Off-thread (single-cell H&E → spatial expression prediction FM).

#### SKIP — Charpentier A. *From Rating Factors to Crash Mechanisms: A Multiscale Causal DAG Framework Linking Motor Insurance and Road Safety.* arXiv 2608.09441v1 (stat.AP, 2026-08-10). Score 1.

Off-thread (motor insurance).

---

### medRxiv Collection Alert (08-13, covering 08-12 postings)

#### HIGH — Zolensky AL, Kripke CM, Keat K, Damrauer SM, Levin MG, Verma A. *Longitudinal Clinical Foundation Models Augmented with Genomics for Early Detection and Risk Stratification of Inherited Cardiomyopathy.* medRxiv 2026.08.10.26360107 (Health Informatics collection, 2026-08-12).

The Penn Medicine EHR-FM + genomics stack, applied to inherited
cardiomyopathy detection. Multiple threads collide here: (1) *EHR
foundation models* — takes CLMBR/MEDS-lineage longitudinal EHR
representation seriously; (2) *composite risk models stacking PRS
with rare pathogenic variants* — the "augmented with genomics" is
almost certainly the composite-risk pattern; (3) *variant
interpretation × ACMG-actionable disease* — inherited cardiomyopathy
is the archetypal ACMG-actionable + variable-penetrance setting where
adding EHR-FM risk should sharpen VUS resolution. Read this first
from the medRxiv batch: it's the paper that operationalizes the
argument the Venkatesh & Ritchie NRG review makes. Follow-ups worth
checking on full-text: which EHR-FM backbone (Penn CLMBR? MOTOR?
MedTok?), how the genomics layer is fused (concatenation vs.
attention vs. two-tower), which cardiomyopathy genes (TTN?
MYBPC3/MYH7 archetype?), and whether ancestry is stratified.

#### HIGH — Rentsch CT, Bhaskaran K, Pavicic M, Warren HR, Matthewman J, Barry E, Rafi I, Hayward J, Gerada C, Shah A, Munroe PB, Silver MJ, Pirmohamed M. *Genotype-predicted drug response phenotypes and their co-occurrence with dispensed medicines among 738,531 participants in the UK Our Future Health study.* medRxiv 2026.08.11.26360205 (Genetic and Genomic Medicine collection, 2026-08-12).

n = 738,531 — this is the *scale* your *pharmacogenomic modifier of
medication persistence* rising sub-thread needs. UK Our Future Health
is the new large biobank on the block (post-UKB architecture, active
recruitment target 5M). The paper's angle is
*genotype-predicted-response × dispensed medicines* co-occurrence —
i.e., how often the drugs people actually get are the ones their
PGx-predicted response supports. Directly portable to CFTR-modulator
persistence, statin discontinuation, HRT persistence, GLP-1 RA
persistence, and the CYP2D6-metabolizer-phenotype × antidepressant
persistence lineage (Psy-PGx UKB / Cohen Pharmaceuticals 2026).
Follow-ups: which drug-gene pairs are covered? Any signal for CFTR /
CFTR modulators specifically? What's the ancestry stratification?

#### HIGH — Kramer B, Rzhetsky A. *A clinical care intensity atlas of 505 diseases from 90 million people.* medRxiv 2026.08.10.26360114 (Epidemiology collection, 2026-08-12).

n ≈ 90 million people, 505 diseases — this is EHR phenotyping at a
scale that has direct bearing on your *chronic disease clustering and
multimorbidity* thread and on the *EHR phenotyping & OMOP* thread.
"Care intensity" as an outcome creates a novel abstraction layer over
raw diagnoses that could be usable as a phenotype-severity axis. Read
for the disease definitions (ICD → phecode? bespoke Rzhetsky-lab
categories?) and for the atlas's downstream utility (disease
trajectory clustering? multimorbidity network construction?
detection-bias adjustment?). Rzhetsky lab has form for
disease-network work (Blair et al. Cell 2013 lineage).

#### HIGH — Rowan CG, Tazare J, Tran M, Srivastava S, Dreyer NA. *Integrating Causal Inference into Pharmacovigilance: Target Trial Emulations for Proactive Signal Detection of Atorvastatin Initiation in Medicare Beneficiaries.* medRxiv 2026.07.01.26356874 (Epidemiology collection, 2026-08-12).

Reframes pharmacovigilance from disproportionality analysis /
self-controlled case series to *target trial emulation* for
proactive signal detection. Applied to atorvastatin initiation in
Medicare beneficiaries. Sits at the exact intersection of your
*causal inference & pharmacoepidemiology* thread and the pharmacoepi
statin-adherence / statin-discontinuation sub-thread. Read alongside
Vossler egg-computation and Wood pregnancy TTE for the
"TTE-as-general-purpose-tooling" argument, and against the classical
FDA-Sentinel Signal-detection literature. Directly portable: run the
same protocol on your GLP-1 RA / SGLT2i / HRT / CFTR-modulator
watchlist as proactive-signal exercises.

#### HIGH — Wang W, Williams J, Gillman MG, Raffield LM, Franceschini N, Ibrahim JG, Zhang H, Li X. *Integrating Genomic and Proteomic Data Improves Complex Trait Prediction in Diverse Populations.* medRxiv 2026.08.10.26360136 (Genetic and Genomic Medicine collection, 2026-08-12).

*Multi-omics-augmented PRS × cross-ancestry portability* in the same
paper — the two rising sub-threads of your composite-risk / PGS-tails
framing fused. Read for (a) which traits (cardiometabolic?
lipids?), (b) which proteomic assay (Olink 3k / 5k?), (c) how the
diverse-population design is structured (MESA + JHS + WHI Hispanic?
AoU-linked?), and (d) whether the improvement over PGS-only is
uniform across ancestries or ancestry-stratified. Reads as the
methodological answer to "does adding proteomics recover the
ancestry-portability gap that PGS-alone leaves?" Bookmark alongside
Feng et al. cross-ancestry IDP pleiotropy for depression from your
INTERESTS.md multi-omics stack.

#### HIGH — Bowers JE, Yu Z, Triozzi JL, Terker AS, Ikizler TA, Wilson O, Cho K, Gaziano JM, Giri A, Perez L, Tao R, Roumie CL, Ivey KL, Hung AM. *The Dietary Approaches to Stop Hypertension (DASH) diet score and its association with the Risk of Kidney Function Decline and Mortality among Veterans in the Million Veteran Program.* medRxiv 2026.08.11.26360178 (Nephrology collection, 2026-08-12).

MVP paper on your active biobanks list. DASH-diet-score → kidney
function decline and mortality; large-N MVP causal-adjacent design.
Read for the MVP methods (cohort definition, dietary questionnaire
handling, kidney-outcome ascertainment) — MVP-methods citation
material for your MVP-related future work.

#### HIGH — Morgan KM, Campbell-Salome G, Salvati ZM, Kunnmann M, Cawley D, Carr L, Ceballos L, Gidding SS, Kenny EE, Kontorovich AR, Naib T, Oetjens MT, Pejaver V, Suckiel SA, Tomey MI, Jones LK, Hallquist MLG. *Designing to Implement Genomics Informed ASCVD Risk Assessment: Patient and Clinician Perspectives about Identifying and Managing the Underlying Causes of Severe Hypercholesterolemia.* medRxiv 2026.08.10.26360146 (Genetic and Genomic Medicine collection, 2026-08-12).

Implementation-science paper for genomics-informed ASCVD / severe
hypercholesterolemia — Geisinger MyCode + Mount Sinai BioMe lineage
(Kenny, Suckiel, Kontorovich are the tell). Directly on the *FH
implementation genomics* branch of your variant-interpretation and
composite-risk threads. Read for the *patient + clinician
perspectives* framing — this is the qualitative substrate that
future population-screening implementations need. Adjacent to the
Zolensky inherited-cardiomyopathy EHR-FM paper above; the two
together sketch a *how do we deploy genomics-augmented risk models
in cardiology* stack.

#### METHODS-WATCH — Salazar AN, Tesi N, van der Lee SJ, Koopmans F, Li KW, Rohde S, Luimes M, Rozemuller A, Smit AB, Hulsman M, Holstege H. *TMEM106B haplotypes show distinct associations with tau and TDP-43 pathologies in the aging brain.* medRxiv 2026.08.11.26359568 (Genetic and Genomic Medicine collection, 2026-08-12).

TMEM106B haplotype × neuropathology phenotype dissection — the kind
of *within-locus modifier* architecture your variant-interpretation
thread tracks in APOL1 N264K and CFTR. Read for the modifier logic
even if the disease (FTLD-TDP / AD) is off-primary threads. Adjacent
to the CHIP-lineage neuroinflammation angle if that sub-thread
reactivates.

#### METHODS-WATCH — the Bipolar Disorder Working Group of the PGC, van der Veen T, Tesfaye M, Yang JMK, Boltz T, David FS, Crinion S, Koromina M, Alda M, Ophoff RA, O'Connell KS, Mullins N, Forstner AJ, Grigoroiu-Serbanescu M, Edenberg HJ, McMahon FJ, Andreassen OA, Di Florio A, McQuillin A. *Genomic dimensions deconstruct the clinical heterogeneity of bipolar disorder.* medRxiv 2025.06.23.25330155v8 (Genetic and Genomic Medicine collection, 2026-08-12).

PGC-BIP dissection of clinical heterogeneity by genomic dimensions.
Adjacent to your PheWAS-of-PheWAS and psychiatric-multimorbidity
instincts (transdiagnostic-factor framing from the Hartwell & Kember
review last window). Read only if extending the substance-use /
psychiatric-multimorbidity sub-thread.

#### MEDIUM — Dagli C, Armstrong ND, Patel PG, Adjei Boakye E, Ament Z, Demopoulos A, Tiwari H, Howard VJ, Kimberly WT, Irvin MR. *Metabolomic and Lipidomic Signatures of Depressive Symptoms in the REGARDS Study.* medRxiv 2026.08.10.26360141 (Genetic and Genomic Medicine collection, 2026-08-12).

REGARDS cohort × metabolomics × depression symptoms. Adjacent to the
Nightingale-NMR-augmented PGS thread; secondary priority.

---

### bioRxiv Collection Alert (08-14, covering 08-13 postings)

#### HIGH — Huynh D-L, Asp E, Ballante F, Carreras Puigvert J, DeGrave A, Karki R, Nader K, Östling P, Pokharel B, Rietdijk J, Schlotawa L, Schmidt L, Seal S, Seashore-Ludlow B, Aittokallio T, Spjuth O. *Human-supervised Agentic AI for Hypothesis Generation and Experimental Assistance in Drug Repurposing.* bioRxiv 2026.04.20.719538v2 (Bioinformatics collection, 2026-08-13).

Karolinska / Spjuth / Aittokallio group. Hits both the *drug
repurposing* thread's explicit preference for
"explainable-hypothesis output" AND the *agentic / human-in-the-loop
observational-causal-inference pipelines* rising sub-thread. Read as
the "wet-lab-adjacent" counterpart to the THBKG KG-based repurposing
paper from the previous report (Siu et al. arXiv 2608.05982), and to
the DrugKLM / GeneAgent NCBI-BioNLP lineage tools your
ncbi-nlp skill catalogues. Together: KG-substrate (THBKG) + agentic
hypothesis generation (this paper) + LLM-verified gene-set / target
reasoning (GeneAgent, PhenoGPT2) = a plausible three-layer
repurposing pipeline. Follow-up worth checking on full-text: what's
the *supervision loop* structure, and which experimental modality
(cell viability, RNA-seq, phenotypic imaging) is the closed-loop
signal.

#### HIGH — Nehra N, Swami R, Dadi D, Mishra R, Sharma U, Verma P, Sen M, Dhruw NK, Jha AK. *A Guided AI Framework for Customizable and Efficient Harmonisation to the OMOP Common Data Model.* bioRxiv 2026.08.07.742453v1 (Bioinformatics collection, 2026-08-12).

Directly on your *EHR phenotyping / OMOP* thread and on the
*knowledge representation in EHRs* thread's *concept normalization
and vocabulary mappings* sub-topic. AI-assisted OMOP mapping is one
of the highest-leverage nodes in the pipeline (SNOMED / LOINC /
RxNorm / ICD → OMOP standard concept). Read for how the
*customizable* angle handles site-specific vocabulary drift (BioVU
vs. AoU vs. MIMIC vs. UKB) — that's the fidelity-and-portability
question your Knowledge-representation-in-EHRs thread explicitly
tracks. If the tooling is usable, it could shortcut a chunk of any
new-site OMOP onboarding on your project stack.

---

### Google Scholar author + keyword feeds (08-11 → 08-13 batches)

#### HIGH — Li M, Peng W, Zhang L, Huang T, Wei C, Liu Z, Fang L. *A scalable framework enables phenome-wide association of structural variants in biobank cohorts.* Research Square rs-10237876 (2026, Bastarache + Denny author-feed cross-hit).

SV-PheWAS scalable framework. The single most on-thread hit for
*PheWAS / phecode infrastructure* in months: population-scale SV
callsets → cohort-level PheWAS. Directly portable to AoU / UKB / MVP
once SV callsets stabilize; complements SNV and CNV pipelines by
adding the SV modality (deletions, duplications, inversions,
translocations, MEIs) to the variant-vs-phecode association engine.
Read for (a) the SV-callset synthesis method (per-individual VCFs →
cohort SV matrix — this is the historically hard part), (b) the
association model (burden vs. single-variant vs. gene-based
collapsing), (c) how they handle SV genotype uncertainty and callset
drift, and (d) which biobank(s) they demonstrate on. Follow-ups
worth checking on full-text: whether they include mosaic mCA / LOY as
SV-adjacent events (which would bridge your somatic-mosaicism
thread), and whether they release the SV-PheWAS matrix as a shared
resource.

#### HIGH — Venkatesh R, Ritchie MD. *AI-based multimodal integration of genomics and electronic health records.* Nature Reviews Genetics 2026 (fires on `electronic health records`, `Foundation models × EHR`, and Ritchie author feeds simultaneously).

The field-defining review for your *EHR foundation models* thread.
Fires across three of your keyword feeds and reads as the citation
you'll want as the framing reference for all your EHR-FM +
composite-genomic-risk work going forward. Priority read on
full-text — expect coverage of CLMBR, MOTOR, MEDS, EHRSHOT, MedTok,
FEMR, plus multimodal (notes + codes + waveforms + imaging) fusion
strategies. Ritchie group's involvement suggests the review will be
biobank-friendly (Penn BioBank / MyCode lineage) with special
attention to PRS + rare-variant + EHR-FM stacking. Bookmark alongside
the *digital twins from EHR data* rising sub-thread — this review is
likely the survey that maps out where the field sits *before* the
digital-twin endgame.

#### HIGH — Dutta D, Zhang J, Guo X, Quint R, Rooney MR, et al. *Polygenic risk scores and plasma proteomics identify cancer-related proteins and trans-regulated protein networks.* Cell Genomics 2026 (Jian Yang author feed).

21-cancer PRSs × 4,955 plasma proteins measured in cancer-free UKB
participants. Direct hit on the *multi-omics-augmented PRS* rising
sub-thread AND on the cancer-genetic-epi lineage that includes
Zeng's early-onset BC work. Read for the *trans-regulated protein
networks* — that's the innovative angle beyond "PRS + protein
biomarker" association: trans networks give you a mechanistic
handle on how PRS liability manifests through the proteome. Read
alongside Peng et al. early-onset BC (last report) and the Wang W
diverse-populations multi-omics PRS paper (this report) for a
*cancer-PRS × multi-omics × ancestry* cluster.

#### HIGH — Ding L, Tian P, Yu F, Jiang Z, Qi Y, Zhang A, Liu Y, et al. *Effect of clonal hematopoiesis of indeterminate potential on long-term survival in patients with arrhythmias.* Journal of Translational Medicine 2026 (`intitle:"clonal hematopoiesis"` keyword feed).

CHIP × arrhythmia survival. Directly on the CV-outcomes branch of
your CHIP / VEXAS / LOY thread. Adds arrhythmia to the coronary-heart-
disease / PAD outcomes literature for CHIP. Read for the CHIP
definition (VAF threshold, driver-gene panel), the arrhythmia case
mix (atrial fibrillation? ventricular?), and whether they stratify by
driver gene (DNMT3A/TET2/ASXL1 differential CV signal).

#### HIGH — Kim MG & Woo HJ. *A hybrid Monte Carlo–LLM framework quantifies model-and architecture-dependent variability in synthetic-patient simulations.* Scientific Reports 2026 (10 new citations to Vivek Natarajan).

Audit-layer paper for LLM-generated synthetic patients — quantifies
how much of the variability in downstream analyses is attributable to
LLM choice vs. architecture vs. sampling temperature. Bookmarks the
*pretraining-contamination audits for foundation-model benchmarks*
rising sub-thread, extending it from CLMBR/MOTOR benchmarks (scContam
/ MIA-scFM) to the LLM-synthetic-EHR generation branch. Read for the
Monte Carlo protocol (what's being sampled, at what layer), and for
its portability to the audit of synthetic patients used in your
egg-computation-style LLM-augmented causal pipelines.

#### HIGH — Kachhadia MP, Puri P, Topiwala U, Shaikh JD, Green G. *Retinal Artery Occlusion and Incident Dementia in the All of Us Research Program: Detection Bias Calibration with Prespecified Negative-Control Outcomes.* medRxiv/preprint 2026 (`All of Us research program` keyword feed).

AoU cohort with prespecified negative-control outcomes for
*detection-bias calibration* — the design your *causal inference in
EHR* thread wants to see spread. Directly complements Foulkes et al.
IPW-for-auxiliary-variable-dependent sampling from the previous
report on selection bias in RECOVER. Read alongside the Gkatzionis
NCOs-for-MR paper (this report) for a paired citation covering NCO
use in both EHR-cohort selection bias and MR selection bias.

#### HIGH — Kodji E, Attaoua R, Haloui M, Hishmih C, Seitz M, Woodward M, Hussin JG, Hamet P, Tremblay J. *Improving the reliability of polygenic risk score-based prediction for cardiovascular and renal complications across ancestries in type 2 diabetes using Mondrian Cross-Conformal Prediction.* PLoS Comput Biol 2026 (UK Biobank keyword feed via 08-14 PubMed batch).

Mondrian cross-conformal prediction on PGS for T2D-related CV/renal
outcomes across ancestries. This is the *calibration methodology* to
bring into the *PGS residuals / polygenic-deviation designs* framing
and the *PGS × ancestry portability* rising sub-thread. Conformal
prediction gives you distribution-free coverage guarantees at each
ancestry stratum — potentially the cleanest fix to the "PGS overshoots
in ancestry X, undershoots in ancestry Y" problem that plagues
population-screening deployments. Read for the ancestry-stratum
definitions and whether the conformal machinery is applied at the
PGS-tail (Baya-lineage misaligned-individuals framing) or across the
full distribution.

#### METHODS-WATCH — Gkatzionis A, Smith GD, Tilling K. *Using Negative Control Outcomes to Detect Selection Bias in Mendelian Randomization Studies.* Statistics in Medicine 2026 (UK Biobank keyword feed via 08-14 PubMed batch).

Formalizes NCO use in MR for selection bias — the analog to the
Kachhadia AoU retinal-artery-occlusion → dementia paper (this report)
but for the MR setting. Read alongside for a paired NCO methodology
citation across cohort selection bias and MR selection bias.
Directly bookmarkable for the drug-target-MR sub-thread; a
sensitivity-analysis layer for MR that most MR papers still don't
run.

#### METHODS-WATCH — Zhang MJ, Durvasula A, Chiang C, Koch EM, Strober BJ, Shi H, Barton AR, Kim SS, Weissbrod O, Loh PR, Gazal S, Sunyaev S, Price AL. *Correlations between causal effect sizes of proximal SNPs vary with functional annotations and implicate stabilizing selection.* Nature Genetics 2026 (UK Biobank keyword feed via 08-14 PubMed batch).

Alkes Price group. Genetic-architecture methods paper on how causal
effect-size correlations at proximal SNPs vary with functional
annotations — with implications for negative / stabilizing selection.
Deep-methods bookmark for the *PGS residuals / polygenic-deviation
designs* framing (the Baya *AJHG* 2026 "misaligned individuals"
lineage). Also relevant to fine-mapping and to the composite rare +
common architecture argument. Not directly clinical, but exemplary
methods on the genetic-epi thread.

#### METHODS-WATCH — Qi X, Belloy ME, Gu J, Liu X, Tang H, He Z. *Robust Inference With Ghostknockoffs in Genome-Wide Association Studies With Sample Relatedness.* Genetic Epidemiology 2026 (Denny author feed).

Extension of the ghostknockoff / knockoff-filter machinery to
GWAS-with-sample-relatedness. Robust FDR control at the variant
level under relatedness — bookmark for the fine-mapping and
variant-interpretation threads.

#### MEDIUM — Aldana Peréz SA, Domínguez-Vargas A, et al. *Apolipoprotein L1 Risk Genotypes and Odds of Lupus Nephritis-Associated Kidney Failure in Systemic Lupus Erythematosus: A Systematic Review and Meta-Analysis.* [Journal TBD] 2026 (APOL1 keyword feed).

Extends the APOL1 → kidney-failure literature to the SLE-LN
population. Sits alongside last report's Gaheer/Lanktree proteomic
score + Chen et al. N264K + Kim/Lee inhibitor triad. Adds
SLE-nephritis as the third disease context (after APOL1-FSGS and
APOL1 + HIV nephropathy) for the same genotype architecture.

#### MEDIUM — Prokunina-Olsson L, Florez-Vargas O, Levin MG, et al. *Multi-population GWAS meta-analysis identifies bladder cancer susceptibility loci and highlights genetic regulation of smoking-related risk.* [Journal TBD] 2026 (Chenjie Zeng self-related-research feed).

Bladder cancer GWAS multi-ancestry meta-analysis with smoking
gene-environment focus. Read if extending the bladder-cancer /
cancer-epi lineage into a cross-population design.

#### MEDIUM — Yakdan S, Warner B, Ghogawala Z, Ray WZ, Bydon M, et al. *Author Correction: Clinically-guided models or foundation models? predicting cervical spondylotic myelopathy from EHR.* npj Digital Medicine 2026 (Aug 12 keyword hit).

Author correction, not the primary paper — but flags the *foundation
models vs. clinically-guided models* comparison in EHR prediction as
a live debate on the EHR-FM thread. If the primary paper wasn't read,
worth catching up.

#### MEDIUM — Chenjie Zeng self-feed: Mehanna H, Rogado J, Calvo AC, et al. *Toward a Better Paradigm for Head and Neck Cancer Treatment Applying AI (HNC-TACTIC): Protocol for an International Cohort Study of Electronic Health Records.* [Journal TBD] 2026.

International cohort study protocol for HNC treatment with an AI +
EHR angle. Read if extending the head-and-neck-cancer sub-thread; the
international EHR-cohort methodology could be a citation target for
cross-site EHR-FM work.

#### MEDIUM — Bender A, Thomas MC, Scannell JW, Shaywitz DA, et al. *Artificial intelligence in drug discovery—what it is, where we stand and the path forward.* Nature Reviews Drug Discovery 2026 (fires on Pritchard + Natarajan + Karczewski feeds simultaneously).

High-profile NRDD survey. Not on-thread by disease, but a plausible
citation-context piece for the *drug repurposing* thread's framing
paragraphs and for the *agentic / LLM-in-drug-discovery* discussions.
Reference-list-mining candidate.

#### MEDIUM — Zheng H, Wang S, Shafrin J, Bheema S, Spurrier K, et al. *Clinical and Economic Burden of Diseases with Accelerated Approval Therapies: Evidence of Unmet Patient Need.* Therapeutic Innovation & Regulatory Science 2026 (`rare diseases` keyword feed).

Rare-disease + accelerated-approval economic-burden design; relevant
if extending the CF / CFTR-modulator eligibility discussion into
regulatory-context arguments.

#### MEDIUM — Fletcher L. *Expanding population frequency data in VarSome: Introducing Korean and Japanese frequency databases.* [HTML preprint] 2026 (`variant interpretation` keyword feed).

Population-frequency-database addition for ACMG-AMP variant
interpretation. Bookmark for the ACMG PS/PM2/BS/BA1 evidence-code
side of the variant-interpretation thread — helps with East-Asian
population BA1/BS1 cutoffs.

#### MEDIUM — Yu Y-H, Zhang Q, Zapata-Bravo E, Platt RW, Reynier P. *Time to Insulin Initiation Among Patients With Type 2 Diabetes Treated With Second-Line Antidiabetic Drugs.* Diabetes, Obesity and Metabolism 2026 (Miguel Hernán author feed).

Directly on the T2D / diabetes-management pharmacoepi arc. Read for
the second-line drug landscape (DPP-4i / SU / GLP-1 RA / SGLT2i) and
the time-to-insulin outcome definition; a design that is close to the
target-trial-emulation setup on your watchlist.

#### MEDIUM — Alasbily H, Sherif FM. *Immunometabolic Effects of SGLT2 Inhibitors on the Th17/Treg Axis: Mechanisms, Evidence, and Implications for Therapeutic Repurposing.* Molecular Biology Reports 2026 (drug repurposing PubMed batch).

Mechanism review of SGLT2i × immune-metabolism → repurposing angle.
Adjacent to the SGLT2i drug-class thread; secondary.

#### MEDIUM — Zhang MJ / Y Zhang et al. proximal-SNP causal-effect correlation paper is already covered above. Also flagged from Aug 13/14 with cross-hits from `UK Biobank` and Nat Genet.

#### MEDIUM — Feng Q, Noordam R, Hu D, Albalak G, Willems van Dijk K, van Heemst D. *Age-Specific Associations of Moderate-to-Vigorous Physical Activity With Relative and Absolute Risk of Type 2 Diabetes in UK Biobank Participants.* Diabetes Obes Metab 2026 (UKB PubMed batch).

UKB physical-activity × T2D age-specific dose-response. Adjacent to
the Zhang AoU MDD-PRS × wearable paper from the previous report
(behavior compensates for inherited liability); this one gives the
age-stratification angle for the same phenotype-behavior interaction
family.

#### MEDIUM — He J, Li B, Yan Y, Wang Y, Zhang M, Sun R, Hou B, Huang S, Zhen L, Wang D, Zhang C. *Identification of Pre-Diagnostic Protein Biomarkers for Liver Cirrhosis Based on Prospective Analysis of a Large-Scale Plasma Proteomics in the UK Biobank.* Proteomics Clin Appl 2026 (UKB PubMed batch).

UKB Olink pre-diagnostic biomarker discovery for liver cirrhosis.
Adjacent to the *pre-symptomatic carrier phenoconversion prediction*
rising sub-thread (Ran/Benatar ALS lineage) but for cirrhosis rather
than a Mendelian condition. Directly portable-template for
BRCA/HTT/APOL1 preclinical biomarker work.

#### MEDIUM — Parasuraman A, Eltayib R, Pandeya N, Olsen CM, Law MH, Whiteman DC, MacGregor S, Seviiri M. *Polygenic prediction of actinic keratosis identifies transplant recipients at risk of extreme lesion burden.* American Journal of Transplantation 2026 (UKB + AoU PubMed batches).

Small-niche PGS-tails-in-transplant paper. On-thread for the
*PGS-tails as discovery lever* framing (Souaiaia lineage) but in a
narrow disease context.

#### MEDIUM — Kodji E paper (Mondrian cross-conformal PGS) covered above as HIGH.

#### MEDIUM — Reeves MM, Aviles Carpintero S, Zanovello M, Jansen-West K, Yue M, Calliari A, Song Y, Dunmore J et al. *The UNC13A cryptic exon associates with cognitive impairment in Alzheimer's disease.* Alzheimer's Research & Therapy 2026 (UKB PubMed batch).

Genetic-variant-to-phenotype paper with a specific splice-variant
mechanism angle. Off-primary threads but bookmarkable for the
UNC13A-lineage splicing-variant discussion.

#### MEDIUM — Gao J, Chalitsios CV, Bennett D, Doherty A, Turner MR, Thompson AG. *Associations of self-reported and objectively measured physical activity and amyotrophic lateral sclerosis risk.* J Neurol Neurosurg Psychiatry 2026 (UKB PubMed batch).

UKB PA × ALS risk; adjacent to the ALS pre-symptomatic-conversion
sub-thread (Ran/Benatar Nature Medicine 2026) but a lower-signal
observational design.

#### LOW — Zheng S, Wu Y, Li A, Wu Z, Liu Z, Wang H, Jia X et al. *Genetic Predisposition and Pharmacological Effects Shape the Divergent Effects of Type 2 Diabetes on Atherosclerosis.* Genomics, Proteomics & Bioinformatics 2026 (Denny + Pritchard cross-hit).

T2D-PGS × atherosclerosis modification with PGx-drug angle. Adjacent
to the composite-risk × pharmacoepi crossover but with limited
translational bite.

#### LOW — Yakdan et al. author correction on cervical spondylotic myelopathy foundation-model paper (repeats above).

#### LOW — Xu Z, Agrawal P, Asadi K, Chen T, Hu C, Johnson J et al. *The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers.* arXiv 2026 (Marinka Zitnik author feed; repeat from previous report). Off-thread.

#### LOW — Kim Y, Gu K, Park C, Park C, Schmidgall S, Heydari AA et al. *Capable language models can outgrow the benefits of collaboration.* Nature Machine Intelligence 2026 (Zhiyong Lu author feed; repeat from previous report). Off-thread for clinical work.

#### LOW — Zhu F, Xu S, Ou J, You Z, Xing Y, Liu H, Zhang X. *LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models.* arXiv 2026 (Zitnik + Zhiyong Lu author feeds). LLM architecture paper; off-thread.

#### LOW — Ju J, Kim Y, Seo SJ, Jin Y, Ahn JY, Shin M. *Adenosine Triphosphate Nanoparticles with Blood-Brain Barrier Permeability for Prevention of Cerebral Ischemic Injury via Mitochondrial Homeostasis.* ACS Nano 2026 (10 new citations to Stephen Montgomery). Off-thread nanotech.

#### LOW — Simmons J, Hyder S, Lertwilaiwittaya P, Smith C et al. *Hypertrophic Cardiomyopathy in a Patient With BAG3-Associated Charcot-Marie-Tooth Disease: A Rare Cardiac Manifestation.* Circulation 2025 (3 new citations to Bastarache). Single-case report; off-thread.

#### LOW — Groeneveld J, Perlaza D, Olivé C, Grangeon L, Tesi N et al. *APOE and genetic risk variants influence Alzheimer's disease onset in carriers of an extra copy of APP, with and without Down syndrome.* [J TBD] 2026 (Konrad Karczewski author feed). Off-primary threads.

#### LOW — Wu D, Xu Z, Li Y, Zhang M, Lin J, Lü Y, Guan D, Qin G. *Prediction and verification of therapeutic drugs for triple-negative breast cancer using a knowledge graph-based drug repurposing model.* Nan Fang Yi Ke Da Xue Xue Bao 2026 (`drug repurposing` keyword feed). Adjacent to the drug-repurposing thread but no obvious methodological novelty beyond TNBC-specific application; low-signal citation for the KG-repurposing sub-thread.

#### LOW — Onwanezi OG, Ikebudu AP, Adione NMB, Ojiakor EJ. *Drug repurposing for diabetes: In silico determination of approved drugs against human glucokinase receptor.* Open Access Research 2026 (`drug repurposing` keyword feed). Docking-only.

#### LOW — Zhu Y, Ye Z. *Prioritizing Parkinson's disease risk-associated mitochondrial candidate genes via multi-omics integrative analysis.* Clinical Neurology 2026 (`variant interpretation` + `mendelian diseases`). Off-primary threads.

#### LOW — Hou Y, Zhi R, Zeng J. *An ontology-based framework for multimodal real-time battlefield situation knowledge graph construction and application.* Computers and Electrical Engineering 2026 (`knowledge graph` keyword feed). Off-domain.

#### LOW — Ding MMG, Liu PHDY, Zhao PHDY, Chen MMX. *Metabolic Vulnerability Indices and Alzheimer's Disease Risk: A Prospective Analysis of the UK Biobank Cohort.* Journal of Nutrition 2026 (`UK Biobank` keyword feed). Adjacent to metabolic-risk-modeling but off-primary threads.

#### LOW — Kachhadia UKB paper details, single-author-title repeats, and various small-signal citations (Sahoo movement disorders review; Miliard Hugo Bellen interview; Jiomekong knowledge-graph semantification review) all noted as low-signal in-window items but not detailed here.

---

### PubMed What's-New (efback / My-NCBI) — 08-14 batches

The UK Biobank, All of Us, and drug-repurposing PubMed batches were
processed inline above (Zhang MJ *Nat Genet* proximal-SNP paper,
Kodji cross-conformal PGS, Gkatzionis NCO for MR, Alasbily SGLT2i
Th17/Treg, and the smaller items). No additional entries beyond
those already elevated / bucketed above.

---

## What's NOT in the report

- **arxiv-digest 08-10 empty run** — no items surfaced; expected
  behavior for a slow arxiv day, not a pipeline issue.
- **Substack / newsletters** (State AI, AI News, Paperclip) — in this
  window flagged Grok 4.6 launch, ScientistOne autonomous agent, and
  discriminative-retrieval papers; noted but none crossed the
  on-thread biomedical threshold.
- **arxiv.org raw daily category mailings** (`no-reply@arxiv.org` for
  `cs`, `stat.AP`, `q-bio`) — the raw upstream feed for arxiv-digest.
  Individual on-thread papers surfaced via the digest are covered in
  the arxiv-digest section above rather than re-listed from the raw
  mailings.
- **Nature Medicine v32 n8 TOC (08-14 06:42Z)** — TOC-only alert
  received during report authorship; no per-article deep-read yet.
  Next report should catch specific articles once they appear via
  keyword / author feed cross-hits.
- **The Aug 11 medRxiv Collection Alert (thread 19ff34b95ac31a8f)** —
  the Aug 13 alert (this report's medRxiv source) already covers the
  Aug 12 postings; papers from the Aug 11 alert (covering Aug 11
  postings) were not deep-read this cycle. Recover in next report if
  the delta matters.
- **GitHub `notifications@github.com` `arxiv-digest` repo emails** —
  none surfaced in Gmail this window; the arxiv-digest pipeline is a
  local cron that writes to `digests/` and commits directly rather
  than routing through GitHub notifications, so all pipeline output
  is captured via the `digests/` file scan above.

## Next steps to consider

1. **Read the Venkatesh & Ritchie NRG review full text first** — it's
   the framing reference for the whole EHR-FM thread and will
   determine which other papers in this window need deep-read
   priority.
2. **Bundle three papers for a "TTE as general-purpose tooling"
   thread update** — Vossler egg-computation (LLM-assisted g-comp) +
   Wood pregnancy-regime TTE + Rowan atorvastatin pharmacovigilance
   TTE. Companion to the Noma TTE R-package tutorial from the
   previous report.
3. **Add Li M SV-PheWAS scalable framework to the PheWAS
   infrastructure shortlist** — pair it with your existing PheWAS /
   PheRS methods citations and consider whether an AoU or UKB SV-PheWAS
   pilot is now feasible.
4. **Deep-read the Zolensky/Damrauer/Verma inherited-cardiomyopathy
   EHR-FM paper next** — it operationalizes the Venkatesh & Ritchie
   review's argument for a specific ACMG-actionable disease and would
   be a direct citation for any composite-risk × EHR-FM stack work.
5. **Read Rentsch et al. 738,531-participant PGx paper** as the
   new anchor for the *pharmacogenomic modifier of medication
   persistence* rising sub-thread — likely to require a rethink of
   which drug-gene pairs are the highest priority for CFTR-modulator /
   HRT / GLP-1 RA persistence analysis.
6. **Add Wang W diverse-populations multi-omics PRS paper + Kodji
   Mondrian cross-conformal PGS paper as a paired citation** for
   PGS-portability-under-ancestry-shift discussions. Together they
   move the field from "add proteomics" and "add ancestry" to a
   proper calibration methodology.
7. **Consider a somatic-mosaicism methods update** — Bandreddi
   Tobit-vs-hurdle paper is the statistical-methodology answer for
   longitudinal clonal-fraction analysis in AoU / UKB; pair it with
   Ji et al. QC layer and Ding CHIP-arrhythmia survival paper for a
   coherent CHIP-methods + CHIP-outcomes update.
8. **Cross-cite Gkatzionis NCO-for-MR and Kachhadia AoU-NCO papers**
   in any triangulation-methodology paragraph for future work — NCOs
   as a shared idiom across MR and EHR cohort studies.

_Report generated 2026-08-14 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-14 → next scheduled run,
including the Aug 11 medRxiv collection catch-up and any per-article
deep-reads from the Nature Medicine v32 n8 issue._
