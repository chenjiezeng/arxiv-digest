# Research digest report — 2026-08-25

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-25 12:39Z** (~8 days since the
last research-digest report, covering eight arxiv-digest cron runs and
four Google Scholar alert batches on 08-22, 08-23, 08-24, and 08-25).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-18.md` → `2026-08-25.md`) | 08-18 → 08-25 daily crons | 8 daily runs. 08-19, 08-21, 08-22, 08-23, 08-24: dry (0 relevant / all previously surfaced). 08-18: 4 papers (Bayesian epidemic alignment g-computation, causal mediation for zero-inflated longitudinal, digital-health n-of-1 primer, regression-not-to-the-mean for overdose deaths). 08-20: 3 papers (Monroe molecular FM, mayoral experience DML, urban rail DML). 08-25: 1 paper (Causal Tail Coefficient under general conditions — warning: 2/4 categories failed to fetch). |
| No `arxiv-digest` email hits from GitHub | — | Same finding as the 08-17 report: no GitHub-side email traffic for the pipeline (it commits daily digest files to the local repo rather than emailing). The on-disk repo *is* the arxiv-digest feed. |
| Google Scholar alerts (keyword feeds, 08-25 batch, 04:13Z) | 08-25 04:13Z | 11 keyword feeds fired: `variant interpretation`/`variant classification`, `autoimmune diseases`, `electronic health records`, `UK Biobank`, `knowledge graph`, `drug repurposing`, `rare diseases`, `All of Us research program`, `mendelian diseases`, `APOL1`, `Foundation models + electronic health records`. |
| Google Scholar alerts (author + citation feeds, 08-24 batch, 13:41Z) | 08-24 13:41Z | 20+ author / citation feeds fired: Chenjie Zeng (self, new-related), Lisa Bastarache (×2), Joshua C Denny (×2), Kai Wang (×2), Konrad Karczewski (×2), Peter Szolovits, Marinka Zitnik, Zhiyong Lu, Tiffany J Callahan, Jian Yang (×2), Stephen B Montgomery (×2), Yuan Luo, Daniel Kastner, George Hripcsak, Miguel Hernán, Vivek Natarajan, Pascal Brandt, Selçuk Korkmaz, Jonathan Pritchard, Patrick Ryan. |
| Google Scholar alerts (08-23 batch, 11:34Z) | 08-23 11:34Z | 10 keyword feeds: `variant interpretation`, `autoimmune diseases`, `electronic health records`, `UK Biobank`, `knowledge graph`, `drug repurposing`, `rare diseases`, `All of Us research program`, `mendelian diseases`, `Foundation models + EHR`. |
| Google Scholar alerts (08-22 + 08-23 author batches) | 08-22 → 08-23 | Author feeds fired for Peter Szolovits, Zhiyong Lu, Marinka Zitnik, Tiffany J Callahan, Vivek Natarajan, Pascal Brandt, James Zou. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets. Note that arxiv-digest 08-25 flagged a
> partial-fetch warning (q-bio.GN, q-bio.PE failed) — the single paper
> surfaced that day is stat.ME-primary, and any genomics-tagged submissions
> from 08-24 will need to be rescanned on the next successful cron.

---

## Executive summary (HIGH-priority studies, ranked)

Fourteen HIGH items surfaced this window, clustering into five knots:

**All of Us cohort + GxE / rare-variant × exposure cluster (3 items).**
Cornell et al. *Military Medicine* 2026 — **AoU MR study of alcohol
consumption on depression / anxiety / PTSD** in the military-relevant
context; surfaced under the Chenjie Zeng new-related-research feed
(likely because it uses AoU + MR, both of which recur in your first-author
work). Suresh et al. *Clinics and Research in Hepatology* 2026 — the
**PNPLA3 rs738409 × heavy alcohol use interaction on incident cirrhosis
in AoU Controlled Tier v8**. This is the exact **PGS × exposure /
environment interactions** rising sub-thread (Nagpal & Gibson lineage)
you called out in INTERESTS.md, executed on AoU with a *diverse US
cohort* framing — direct hit for both the AoU and GxE threads. Cheng,
Butler-Laporte, Nakanishi et al. *Genetics in Medicine* 2026 — **clinical
score to prioritize detection of severe alpha-1 antitrypsin deficiency
with PiZZ genotype** in AoU. Direct hit for the rare-disease + AoU +
variant-interpretation triad (a monogenic variant screened at
population scale, then anchored to a clinically actionable phenotype).
Portable methods template for CFTR-modulator eligibility screening and
APOL1 kidney-disease screening — both on your active watch list.

**Pharmacoepi / TTE cluster (2 items).** Peng et al. *Europace* 2026
(Hernán citations-to feed) — **TTE of oral-anticoagulation discontinuation
after AF ablation** at a 6-month landmark, using a multicentre Chinese
registry. Direct addition to the causal-inference / pharmacoepi thread;
the landmark specification and CHA2DS2-VA-restricted eligibility are the
practical scaffold. Wartko et al. (Patrick Ryan new-related feed) —
**GLP-1 RA + SGLT2i + metabolic bariatric surgery utilization trends in
US adults**. This is the utilization backdrop for every GLP-1 / SGLT2i
pharmacoepi study you're prototyping; the trend context is the
denominator to any TTE-emulation contrast you emulate.

**EHR foundation-model + portability / phenotyping cluster (3 items).**
Walsh, Ripperger, McCoy et al. *npj Digital Medicine* 2026 (Pascal Brandt
new-related feed) — **transportability failures of EHR-based risk models
for treatment-resistant depression**. Direct hit for the EHR-FM
portability audit sub-thread and for the more general "does this
computable phenotype travel across sites" question that BioVU / AoU
external-validation work depends on. Wang et al. *JAMA Network Open*
2026 (Natarajan citations-to feed) — **EHR-integrated LLM-powered tool
for surgical patient triage**. Deployment-scale example of the LLM /
transformer clinical-note extraction sub-thread; JAMA Netw Open is a
signal that this cluster of tools is crossing into peer-reviewed
clinical deployment. Brunello et al. *Human Genomics* 2026 (Lisa
Bastarache new-related feed) — **GenPhenia: DNN for rare-disease
diagnosis from HPO phenotypes**. Direct hit for the "auditable
HPO-driven diagnostic benchmarks with separable metrics for ranking vs.
evidence coverage" sub-thread (GraphRareBench lineage). Should be
benchmarked head-to-head against Phenolyzer / Phen2Gene / PhenoSV /
LIRICAL / Exomiser / PhenoGPT2 on the same eval set.

**Genetic-epi + biobank cluster (4 items).** Álvarez Sirvent, Tesi,
Hulsman, Salazar et al. *npj Aging* 2026 (Josh Denny new-related feed)
— **HLA alleles decrease chance of reaching healthy old age**; feeds the
variant-interpretation-in-the-context-of-aging thread and pairs with
the CHIP / LOY / VEXAS somatic-mosaicism → aging phenotype chain.
Castañeda, Hasbani, Heath, Alquicira et al. *Scientific Reports* 2026
(Jian Yang citations-to feed) — **cardiometabolic PGS performance in a
high-altitude Peruvian cohort (CRONICAS)**. Direct hit for the PGS
portability / cross-ancestry sub-thread; the high-altitude ecological
context adds a genotype × environment layer on top of ancestry
mismatch. Duerinckx et al. *Epilepsia* 2026 (Karczewski new-related
feed) — **systematic exome-wide analysis of oligogenic inheritance in
epilepsy**. Direct hit for rare disease + variant interpretation +
Mendelian-vs-oligogenic architecture, and a clean methodological
scaffold for the "how many co-inherited variants together explain
the phenotype" question outside epilepsy (e.g., CF modifier hunts,
APOL1-adjacent kidney-disease modifier hunts). Zhai, Mälarstig, Shen
*Nature Reviews Genetics* 2026 (Lisa Bastarache citations-to feed) —
**Proteogenomics in human populations**. Field-level review for the
multi-omics-augmented PRS rising sub-thread — the reference paper for
Nightingale NMR / Olink stacking with PGS.

**Longitudinal digital-phenotyping + multimorbidity cluster (2 items).**
Shim & Onnela *Nature Communications* 2026 (AoU keyword feed) —
**Longitudinal digital phenotyping of activity rhythms and biological
aging using commercial wearables**, integrating multi-year Fitbit
data from AoU with PhenoAge from 2,222 participants (8,447 person-years).
This is a rare AoU-native digital-phenotyping paper that pairs a *device
sensor* with a *biomarker-derived aging clock* — direct hit for the
"digital twins from EHR data" rising sub-thread. Pham, Madakkatel,
Mulugeta, Lumsden, Hill et al. *Seminars in Arthritis and Rheumatism*
2026 (UKB keyword feed) — **data-driven discovery of candidate
predictors of future rheumatoid arthritis diagnosis in UKB**. Feeds
the multimorbidity thread (RA sits at the autoimmune / cardiometabolic
crossroads) and is a good template for prospective-EHR / biobank incident
outcome prediction.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-18 → 2026-08-25)

#### HIGH — Daza EJ. *A Primer on Digital Health N-of-1 Studies and Single-Case Designs.* arXiv 2608.15526v1 (stat.AP, 2026-08-16). Score 1. [digest: 2026-08-18]

Book-chapter primer on **n-of-1 studies, single-case designs, and other
"multitudinal" approaches for digital-health applications**. Argues
that population-average estimands undersell an individual patient's
recurring health pattern, and proposes "esametry" — the statistics of
the digitized multitudes within each person — as the individualized
counterpart to subgrouping. This is directly the **"individualized risk
prediction, treatment-effect heterogeneity" ML-for-precision-health
thread** — most relevant methodologically as a rebuttal to the
"HTE = subgroup analysis" reflex. Pair with Kung et al. (below) on
regression-not-to-the-mean and with the CGM continuous-monitoring
literature (Alkabbani et al., citation feed): the same person-year is
the substrate. Portable to CFTR-modulator response, HRT-symptom
response, and any biobank-adjacent longitudinal setting where you can
get repeated within-person measures.

#### METHODS-WATCH — Moriña D. *Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions.* arXiv 2608.16537v1 (stat.ME, 2026-08-17). Score 1. [digest: 2026-08-18]

**Bayesian causal count model** in which season-specific affine
transformations map calendar time to a latent epidemic clock, and
intervention effects are estimated on the *clock* rather than on the
calendar. Uses a negative-binomial observation distribution,
hierarchical area / season / area-season effects, a shrunk Fourier
epidemic curve, and a continuous programme-intensity exposure.
Posterior g-computation yields prevented cases, prevented fractions,
peak attenuation, and epidemic displacement, under both a controlled
and a dynamic contrast. Illustrated on Catalan primary-care surveillance
+ RSV immunisation data. **METHODS-WATCH** because the *aligned-clock*
trick is a portable pattern — any TTE-emulation where the correct
follow-up clock is not calendar time (e.g., early pregnancy
gestational-age dating from Wood et al. 08-11, or menopause-onset
dating for HRT-persistence work) can borrow the *treat alignment as a
model component, not a preprocessing step* discipline.

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. *Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.* arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1. [digest: 2026-08-18]

Bayesian causal-mediation framework using **enriched Dirichlet-process
mixture models** with scalable **G-computation** estimation, handling
(i) treatment non-compliance (email non-opening), (ii) multiple
longitudinal mediators, and (iii) zero-inflated mediators + outcomes.
Application is a marketing dataset (promotional emails × free shipping
vs. discount), *not* clinical — but the methods are the exact pattern
needed for **zero-inflated longitudinal clonal-hematopoiesis VAF data**
(pair with Bandreddi et al. 08-11 hurdle vs. Tobit paper) *with* a
mediation angle (e.g., CHIP → inflammatory-mediator → cardiovascular
outcome), and for CFTR-modulator adherence-as-mediator work where
adherence itself is zero-inflated. Bookmark as the reference for
zero-inflated causal-mediation.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. *Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.* arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1. [digest: 2026-08-18]

Shows that in longitudinal settings with **staggered treatment and
heterogeneous treatment effects**, the estimated constant treatment
effect can be a *weighted average with negative weights* of duration-
specific HTEs, so the constant estimate can be *smaller in magnitude or
opposite in sign* to nearly every HTE. Illustrated on drug-induced-
homicide prosecutions × overdose deaths in the US, under both linear
and logistic links (showing the negative-weight issue is not a
linear-model artifact). **METHODS-WATCH** because your GLP-1 RA,
SGLT2i, CFTR-modulator, and HRT threads are all "staggered
initiation, potentially duration-varying effect" designs — the
negative-weighting caveat should be in the pre-analysis discipline
alongside the standard TTE / IPW checklist. Direct methods complement
to Daza's n-of-1 primer above and Chen et al. clustering-informed
IPW (08-11 report).

#### SKIP — Banaszewski B, Fitzgibbon AW. *Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference.* arXiv 2608.18982v1 (cs.LG, 2026-08-19). Score 1. [digest: 2026-08-20]

Molecular foundation model with a **TabPFN-based downstream
in-context predictor**, pre-trained on 81M molecules from PM6 quantum
chemistry data. Improves Polaris + activity-cliff benchmarks over
prior MFMs; also yields MiniMol_PFN and CheMeleon_PFN variants. Skip
for our threads: bioassay activity prediction / drug discovery lives
outside the clinical / EHR side of the pipeline. Flag only in case the
PFN-based downstream adapter shows up in medical-imaging or clinical
tabular-prediction FM work later.

#### SKIP — Machacuay C, Lincovil J, Rojas H. *Mayoral Experience or Municipal Capacity? Negative-Outcome Evidence on Municipal Budget Execution in Peru.* arXiv 2608.18354v1 (stat.AP, 2026-08-18). Score 1. [digest: 2026-08-20]

Panel DML on Peruvian municipal-budget execution using **negative-
outcome controls**; the substantive claim is that within-municipality
DML recovers a positive experience → budget-execution association, but
partial-identification bounds don't support clean causal
interpretation. Skip on substance — but the **negative-outcome-control
+ panel-DML** design is worth mentally bookmarking for any biobank /
EHR pharmacoepi where you can find a plausible negative control
outcome (e.g., a phenotype that shouldn't be affected by the exposure
by any known mechanism), especially in the CFTR-modulator and HRT
threads.

#### SKIP — Yao Y, Zhang N, Graham DJ. *Quantifying the Causal Operational Determinants of Service Reliability in Urban Rail Transit: Evidence from Panel Double/Debiased Machine Learning.* arXiv 2608.17901v1 (stat.AP, 2026-08-18). Score 1. [digest: 2026-08-20]

Panel DML on 46 international metro operators (1994–2024) using the
CoMET benchmarking database. Off-topic on substance. The domain-
knowledge-driven variable-construction step (three theorized
mechanisms: demand pressure, service supply, demand–supply imbalance)
is a clean pattern for **structural / causal DAG scaffolding in
observational settings with a lot of correlated predictors** — could
transfer to health-system operational studies (e.g., hospital LOS →
readmission-risk work adjacent to Vossler / egg-computation from
08-17).

#### METHODS-WATCH — Leimenstoll L, Schienle M. *Identification and Inference for Causal Effects in Extremes under General Conditions.* arXiv 2608.22957v1 (stat.ME, 2026-08-24). Score 1. [digest: 2026-08-25]

Studies identification of causal relations in the **tails** using the
Causal Tail Coefficient (CTC) in a linear structural causal model with
heavy-tailed regularly varying innovations, allowing heterogeneous tail
indices and heavy-tailed confounders. Shows heavy-tailed confounders can
induce extremal patterns *observationally indistinguishable* from direct
causal effects — an important caveat for any biomarker-tails causal
analysis. Applications are climate + financial. **METHODS-WATCH** for
any downstream question about extreme-tail health outcomes (e.g.,
extreme HbA1c excursions, extreme HDL/LDL/Lp(a) values, extreme
inflammatory-marker episodes) — the "confounder that only bites in
the tail" issue is under-appreciated in current PGS-tails-as-discovery
work (Souaiaia lineage).

### Google Scholar alerts (2026-08-22 → 2026-08-25)

#### HIGH — Cornell L, Shukla T, McMillan K, Gdovin M, Smetana C, et al. *Estimating the Causal Effect of Alcohol Consumption on Military-Relevant Mental Health Conditions: A Mendelian Randomization Study Using the All of Us Research Program.* Military Medicine, 2026 (advance article, doi:10.1093/milmed/usag368). [Chenjie Zeng new-related feed, 08-24]

MR analysis of alcohol consumption as an exposure on **depression,
anxiety, and PTSD** in a military-relevant framing, using **All of Us
Research Program data**. This is a compact worked example of the AoU
+ MR combination — MR-based causal identification in the AoU cohort
against psychiatric outcomes — and it surfaced under your own
new-related-research feed (Google Scholar inferring topic similarity
to your first-author work). Direct hit for the **biobank + causal
inference** intersection. Worth reading for: (i) how the authors
handled AoU-specific PGS construction and instrument selection,
(ii) whether they used AoU EHR-derived psychiatric phecodes or survey
instruments as outcomes, and (iii) sensitivity to horizontal
pleiotropy in an alcohol-instrument MR. A useful template for
**AoU-native MR studies of modifiable exposures against EHR-derived
phecodes** — a pattern portable across cardiometabolic and
autoimmune outcomes.

#### HIGH — Suresh KB, Bhatia R, Sajawal M, Sabet O, Zahedi I, et al. *Gene–Environment Interaction Between Heavy Alcohol Use and PNPLA3 rs738409 in Incident Cirrhosis: Evidence From a Diverse US Cohort.* Clinics and Research in Hepatology, 2026 (S2210740126001555). [All of Us keyword feed, 08-25]

**PNPLA3 rs738409 × heavy alcohol use interaction on incident cirrhosis
in All of Us Controlled Tier v8**, using the **diverse-cohort** angle
as its methodological pitch. This is the exact **PGS × exposure /
environment interactions** rising sub-thread you added to INTERESTS.md
(Nagpal & Gibson lineage), executed on AoU. Direct triple-thread hit
(AoU + GxE + hepatology). Notes to verify on read: (i) how they handled
ancestry stratification vs. pooled GxE modeling (ancestry-conditional
interactions vs. pooled with ancestry × interaction), (ii) whether the
"heavy alcohol use" phenotype was self-report or EHR-derived (or a
combined instrument), (iii) how they defined incident cirrhosis
(phecode-based vs. LOINC-lab-based vs. imaging-derived), and (iv)
whether they replicated in an external cohort (UKB / MVP / BioVU).
Directly portable pattern for PNPLA3 × obesity in MASLD, HFE C282Y ×
iron intake, and CFTR-heterozygote × environmental exposure work.

#### HIGH — Peng X, He L, Wang J, Li S, Li Q, Zhao Z, Yang Z, Li M, et al. *Residual thromboembolic risk and outcomes of oral anticoagulation discontinuation after atrial fibrillation ablation: a target trial emulation.* Europace, 2026 (advance article, doi:10.1093/europace/euag197). [Miguel Hernán citations-to feed, 08-24]

**TTE of oral-anticoagulation discontinuation vs. continuation at a
6-month post-ablation landmark**, using a multicentre Chinese
prospective registry. Restricts to CHA2DS2-VA ≥ 2, no prior TE, no
atrial arrhythmia at landmark — a clean eligibility spec. Evaluates
thromboembolic + bleeding outcomes. HIGH because it's a well-scoped TTE
in a common clinical decision, exactly the shape of TTE work most
portable to **CFTR-modulator persistence**, **statin discontinuation
after adverse events**, and **HRT discontinuation on symptom
resolution**. Read for: (i) landmark specification and how they
handled the "OAC-eligible-at-landmark" clone, (ii) censoring rules for
loss to follow-up vs. protocol deviation, and (iii) how they modeled
pre-landmark discontinuation. The Hernán citation-to route is a signal
this paper explicitly follows the Hernán / Robins TTE framework.

#### HIGH — Álvarez Sirvent D, Tesi N, Hulsman M, Salazar AN, et al. *Carrying specific HLA alleles decreases the chance of reaching healthy old age.* npj Aging, 2026. [Joshua C Denny new-related feed, 08-24]

HLA-allele-level analysis of **healthy-old-age attainment** — the
inverse of the standard aging-outcomes framing (studying who *reaches*
a favorable aging phenotype rather than who develops a disease
outcome). Direct hit for the **variant-interpretation × aging**
intersection and the **healthy aging as a phenotype** thread that has
been growing across the biobank literature. Two useful sub-questions
for on-read: (i) how "healthy old age" was operationalized (chronic-
disease-free, functional-status-based, biomarker-based, or composite),
and (ii) whether HLA effects were specific to particular disease
avoidance (autoimmune, infectious, cancer) or general. Pair with the
CHIP / LOY somatic-mosaicism → healthy-aging trajectory watchlist
items — HLA + CHIP + LOY are three parallel axes of "genetic
architecture of aging" you're tracking.

#### HIGH — Wartko PD, Zhang R, Johnson E, Begle C, et al. *Trends in utilization of glucagon-like peptide-1 receptor agonists, sodium–glucose cotransporter-2 inhibitors, and metabolic bariatric surgery in US Adults with [...].* 2026. [Patrick Ryan new-related feed, 08-24]

**Utilization trends of GLP-1 RAs, SGLT2is, and bariatric surgery in
US adults** — the utilization backdrop for every GLP-1 / SGLT2i
pharmacoepi study in your active drug-class threads. Direct hit for
the pharmacoepi thread. HIGH because you need the *denominator*
context (uptake, discontinuation, class-switching rates by patient
subgroup) to interpret any TTE-emulation contrast on GLP-1 RA or
SGLT2i effects, and because trend-shift artifacts are a real
confounder in longitudinal effect estimates. Also useful as a
current-utilization reference to cite in your own GLP-1 / SGLT2i
methods writeups.

#### HIGH — Cheng Y, Butler-Laporte G, Nakanishi T, Lu T. *Development of a simple clinical score to prioritize detection of severe alpha-1 antitrypsin deficiency with PiZZ genotype.* Genetics in Medicine, 2026. [All of Us keyword feed, 08-23]

**Clinical score for prioritizing detection of PiZZ severe AAT
deficiency** carriers using EHR-derived features. Direct hit for:
(i) rare disease (AAT deficiency), (ii) variant interpretation
(PiZZ / SERPINA1), (iii) All of Us (implied by keyword feed match),
and (iv) computable phenotyping (clinical-score → who to sequence).
This is exactly the pattern you want to steal for **CFTR carrier
detection** and **APOL1 high-risk-genotype detection** at
population-screening scale — turn EHR-visible phenotypic clues into
a low-cost enrichment for targeted sequencing. Read for: (i) which
phecodes / labs / medications entered the score, (ii) whether the
score was internally cross-validated or externally validated in a
different biobank, (iii) sensitivity / PPV at operating thresholds
compared to blanket screening.

#### HIGH — Brunello FG, Colangelo G, Rius A, Erra L, Lugones AC, et al. *GenPhenia: using deep neural networks to accelerate rare-disease diagnosis.* Human Genomics, 2026. [Lisa Bastarache new-related feed, 08-24]

**Deep-learning method for rare-disease diagnosis** from patient
phenotypic profiles (HPO terms). Direct hit for the **HPO-driven rare
disease diagnosis** sub-thread and the "auditable HPO-driven
diagnostic benchmarks with separable metrics for ranking vs. evidence
coverage" line you added to INTERESTS.md (GraphRareBench, Guo et al.
2607.24878). Should be **benchmarked head-to-head** against Phenolyzer,
Phen2Gene, PhenoSV, LIRICAL, Exomiser, PhenoGPT2 on the same eval set
before believing any headline-metric improvement. Read for: (i) train
/ eval split methodology and whether the eval set overlaps with
public HPO annotations the DNN could have memorized, (ii) whether
the Hit@10 metric hides the "ranking-of-confounders" failure mode
you flagged, and (iii) whether the paper reports evidence-coverage
metrics or only ranking metrics.

#### HIGH — Walsh CG, Ripperger M, McCoy TH Jr, Castro V, Hu Y, et al. *Evaluating transportability failures of electronic health record-based risk models for treatment-resistant depression.* npj Digital Medicine, 2026. [Pascal Brandt new-related feed, 08-23]

**Transportability audit of EHR-based risk models for treatment-
resistant depression (TRD)**. Direct hit for the "fidelity, portability,
and audit of representations" sub-thread inside knowledge representation
in EHRs (INTERESTS.md), and for EHR-FM portability audits more broadly.
This is the *external validation* pattern most computable-phenotype and
EHR-risk-model papers ship without — Walsh's group is a
methodologically-serious source for this style of audit. Read for:
(i) which sites the model was trained / evaluated at (BioVU-adjacent?
MGH/BWH network?), (ii) whether transportability failure was
mechanistically attributed (feature drift vs. label drift vs.
population shift), and (iii) what the recommended fix pattern is
(retraining, feature-set change, calibration recalibration). Portable
directly to any AoU-trained model you'd validate on UKB / MVP / BioVU
or vice versa.

#### HIGH — Wang J, Keyes T, Liang AS, Ma SP, Shen J, Liu J, et al. *An Electronic Health Record–Integrated, Large Language Model–Powered Tool to Triage Surgical Patients.* JAMA Network Open, 2026. [Vivek Natarajan citations-to feed, 08-24]

**LLM-powered EHR-integrated surgical triage tool** — a
deployment-scale example of the LLM / transformer clinical-note
extraction sub-thread. HIGH because JAMA Network Open is a signal
that this pattern is crossing into peer-reviewed clinical deployment
(not just methods-arXiv). Read for: (i) prospective vs. retrospective
evaluation design, (ii) how they built the LLM ↔ EHR integration
layer (FHIR? SMART-on-FHIR? in-house middleware?), (iii) their
prompt-engineering + guardrail strategy, and (iv) equity-audit
metrics across patient subgroups. Direct hit for the "LLM /
transformer-based concept extraction, negation and temporality
detection, HPO / SNOMED term assignment from free-text problem
lists and discharge summaries" sub-thread in INTERESTS.md.

#### HIGH — Shim J, Onnela JP. *Longitudinal digital phenotyping of activity rhythms and biological aging using commercial wearables.* Nature Communications, 2026 (article 76147-6). [All of Us keyword feed, 08-25]

Integrates **multi-year Fitbit activity data from the All of Us
Research Program with clinical biomarker-derived PhenoAge from 2,222
participants (8,447 person-years)**. High-dimensional digital
phenotyping links activity-rhythm features to biological aging clocks.
Direct hit for **digital twins from EHR data** (Zhang / Ideker /
Oermann rising sub-thread) — this is a rare AoU-native paper pairing
a *device sensor stream* with a *biomarker-derived aging clock*.
Portable to CHIP / LOY somatic-mosaicism × aging trajectories once
AoU WGS + LOY status becomes standard. Also relevant to the
multimorbidity + aging phenotype thread and to any HRT / statin
pharmacoepi work that could use wearable-derived activity as a
mediator. Read for: (i) how they handled Fitbit-adoption selection
bias (Fitbit users ≠ AoU representative), (ii) which activity-rhythm
features carried the aging signal (rest-activity fragmentation vs.
peak activity vs. inter-daily stability), and (iii) whether PhenoAge
gap was cross-sectional or longitudinal.

#### HIGH — Pham K, Madakkatel I, Mulugeta A, Lumsden A, Hill C, et al. *Data-Driven Discovery of Candidate Predictors of Future Rheumatoid Arthritis Diagnosis in the UK Biobank.* Seminars in Arthritis and Rheumatism, 2026. [UK Biobank keyword feed, 08-23]

**UKB-scale data-driven predictor discovery for incident RA**. Direct
hit for: (i) UKB + incident-outcome discovery, (ii) autoimmune + IBD-
adjacent thread (RA sits at the autoimmune / cardiometabolic
crossroads), (iii) multimorbidity via RA's comorbidity network, and
(iv) EHR + biobank prospective prediction. Read for: (i) predictor
family (baseline biomarkers vs. Olink proteomics vs. NMR metabolomics
vs. lifestyle vs. genetic), (ii) whether the paper reports
external-validation in an EHR biobank (AoU / MVP / BioVU), (iii)
calibration + decision-curve analysis (not just AUC), and (iv)
whether ancestry-stratified performance was reported. Portable to
other autoimmune incident-diagnosis predictors (IBD, SLE, MS).

#### HIGH — Castañeda A, Hasbani NR, Heath AS, Alquicira O, et al. *Performance of cardiometabolic polygenic scores in a high-altitude Peruvian population: the CRONICAS cohort.* Scientific Reports, 2026. [Jian Yang citations-to feed, 08-24]

**Cardiometabolic PGS performance evaluated in a high-altitude
Peruvian cohort (CRONICAS)**. Direct hit for the PGS portability
sub-thread. The high-altitude ecological context is the interesting
addition — it layers a **G × environment** confounder on top of
ancestry mismatch, and Andean adaptation genetics
(*EPAS1*/*EGLN1*-style variants) means portability failure could be
population-specific *and* environment-specific in ways UKB-derived
scores can't diagnose alone. Read for: (i) which PGS were tested and
their source cohort (UKB vs. multi-ancestry), (ii) whether
performance was decomposed into ancestry effects vs. altitude
effects, and (iii) implications for the pangenome-informed
variant-calling angle (HPRC v2 as a portability lever) — Andean
populations are underrepresented in HPRC.

#### HIGH — Duerinckx S, Gravel B, Soblet J, Legros B, Santos SF, et al. *Oligogenic inheritance in epilepsy: A systematic exome-wide analysis.* Epilepsia, 2026. [Konrad Karczewski new-related feed, 08-24]

**Systematic exome-wide analysis of oligogenic inheritance in
epilepsy**. Direct hit for rare disease + variant interpretation +
Mendelian-vs-oligogenic architecture. Read for: (i) the operational
definition of "oligogenic" (# of variants, effect-size threshold,
overlap with recognized PheKB/GA4GH disease-gene lists), (ii) how
they controlled for coincidental co-occurrence of common risk
alleles vs. mechanistically-relevant co-inheritance, and (iii) how
the ClinGen / ACMG framework would classify the second variants —
usually the ACMG-AMP framework struggles with modifier-role variants
and this paper may propose extensions worth stealing. Portable
scaffold for **oligogenic architecture questions in CFTR modifier
hunts** and in **APOL1-adjacent kidney-disease modifier hunts**.

#### HIGH — Zhai R, Mälarstig A, Shen X. *Proteogenomics in human populations.* Nature Reviews Genetics, 2026. [Lisa Bastarache citations-to feed, 08-24]

Nature Reviews Genetics **field-level review of proteogenomics in
human populations** — the reference paper for the **multi-omics-
augmented PRS rising sub-thread** you added to INTERESTS.md
(Nightingale NMR / Olink stacking with PGS for lipid, cardiometabolic,
and psychiatric traits). Read for: (i) the current gold-standard
integration architectures (Olink pQTL discovery → protein-PGS →
stacking with disease PGS), (ii) recommended handling of
tissue-specificity vs. plasma-proteome measurement, (iii) proteogenomic
Mendelian-randomization designs, and (iv) the paper's own
recommendations for what "next-generation" proteogenomic biobanks
should measure. Anchor citation for any grant / methods framing on
multi-omics PGS.

#### METHODS-WATCH — John S, Boone EC, Yoo B, Ramsey LB, Gaedigk A. *Characterization of NAT2 Using Long-Read Sequencing: Allele, Diplotype, and Phenotype Call Accuracy Compared to Other Testing Strategies.* Clinical Pharmacology & Therapeutics, 2026. [Kai Wang new-related feed, 08-24]

Pharmacogenomic phenotyping of **NAT2** using long-read sequencing,
comparing allele / diplotype / phenotype call accuracy against
alternative testing strategies. METHODS-WATCH because: (i) long-read
PGx phenotyping is the direction of travel for AoU / All of Us PGx
studies, (ii) NAT2 sits in isoniazid / hydralazine / sulfonamide
pharmacoepi work adjacent to your pharmacogenomic-modifier-of-
medication-persistence sub-thread, and (iii) it's a methods anchor
for CYP2D6 / CYP2C19 phenotyping infrastructure. Not a direct thread
hit, but the accuracy-comparison framework is exactly the pattern
you'd use to evaluate a PGx-testing strategy before deploying it in
an AoU study.

#### METHODS-WATCH — Wang L, Wang W, Hao Y, Chen L, Qi C, Liang D, L. *DIA proteomics of FFPE renal biopsies reveals two molecular subtypes of lupus nephritis and identifies APOL1 as candidate biomarker for stratification.* 2026. [APOL1 keyword feed, 08-25]

**FFPE renal-biopsy DIA proteomics identifies APOL1 as a stratification
biomarker for lupus nephritis molecular subtypes**. Off-topic
diagnostically (lupus nephritis, not APOL1-associated CKD), but
METHODS-WATCH because it puts APOL1 protein levels in tissue as a
readout — the *tissue-proteomics APOL1* signal is a complementary
axis to the *plasma-proteomics APOL1* and *genotype-APOL1* signals
you're already tracking. Portable pattern for APOL1 in transplant
decision-making biopsy substrates.

#### METHODS-WATCH — Oskotsky TT, Tang X, Arthurs E, Govil A, Abbasi F, et al. *A transcriptomics-based computational drug repurposing pipeline identifies simvastatin and primaquine as therapeutics for endometriosis.* 2026. [Drug repurposing keyword feed, 08-25]

**Transcriptomics-based drug repurposing pipeline** identifying
simvastatin and primaquine as endometriosis candidates. METHODS-WATCH
because the pipeline structure (signature-reversal via LINCS L1000 →
candidate drug list → orthogonal validation) is the reference
pattern for **explainable drug repurposing**. Direct-hit-adjacent for
your drug-repurposing thread — but strong preference for pipelines
that include an EHR-based real-world-prescribing validation step (the
Oskotsky lab does this for other indications, verify whether this
paper includes an EHR-signal loop).

#### METHODS-WATCH — Garcia-Argibay M, Faraone SV, Chang Z, Cortese S, et al. *From prediction to decision: prediction-based decision rules and target trial emulation in ADHD.* The Lancet Psychiatry, 2026. [Miguel Hernán citations-to feed, 08-24]

Personal View arguing that most ADHD prediction models fail to reach
clinical practice because they lack **prediction-based decision rules**
mapping model outputs to specific clinical actions — and proposes
**TTE as the framework** to evaluate whether a decision rule
improves outcomes. METHODS-WATCH because this is the exact "from
prediction to decision" gap that your ML-for-precision-health thread
watches, and the TTE-as-evaluation-framework framing is portable to
CFTR-modulator initiation rules, APOL1-genotype-informed transplant
decisions, and any biobank-derived risk model you'd want to deploy.

#### METHODS-WATCH — Alkabbani W, Cromer SJ, Patorno E. *Beyond Glycemia: Entering the Era of Hard Outcomes for Continuous Glucose Monitoring.* Diabetes Care, 2026. [Miguel Hernán citations-to feed, 08-24]

Editorial framing that continuous glucose monitoring (CGM) studies
are moving past HbA1c/time-in-range surrogates to **hard outcomes**
(MACE, hospitalization, mortality) — and that TTE-emulation is the
right framework for that transition. METHODS-WATCH for your CGM /
diurnal-glucose-GWAS work (Abner-Johnson-Vujkovic-Daly *Nature* 2026
from the 08-17 report), the Ciardulli functional-propensity-score
paper (08-08 report), and the GLP-1 RA / SGLT2i drug-class threads
above. This is the citation to reach for when arguing that a CGM
outcome measure warrants a hard-endpoint TTE — a common framing need
in AoU pharmacoepi grant writing.

#### METHODS-WATCH — Zhao Y, Chen Z. *Mapping social determinants of health in NIH research funding with large language models.* 2026. [Yuan Luo citations-to feed, 08-24]

**LLM-based mapping of SDoH in NIH research funding** — a portable
LLM-annotation pattern for grant-level meta-research, and adjacent
to the broader NLP-derived-representations-from-clinical-notes
sub-thread. Not a direct thread hit, but useful as a citation for
SDoH-representation work in EHR studies.

#### SKIP — Pierre D, Karima B. *From Literature Overload to Knowledge Graph: An Automated Pipeline for Literature Reviews.* 2026 IEEE Annual Computers, Software, and [...]. [Knowledge graph keyword feed, 08-25]

Automated KG-construction pipeline for literature review. Off-topic —
non-biomedical KG infrastructure — which INTERESTS.md flags as lower
interest.

#### SKIP — Jiang Z, Xu W, Peng M, Liu B, Xiao Y, Shan Z, Jia X. *Structure-aware generative framework for temporal knowledge graph reasoning with historical evidence.* World Wide Web, 2026. [Knowledge graph keyword feed, 08-23]

General temporal-KG reasoning method. Off-topic on biomedical
grounding.

#### SKIP — Thomsen MK, Dalby HR, Schram A, Jensen SK, et al. *Regional Electronic Health Records in Denmark: Research Potential for Clinical Epidemiology.* Clinical Epidemiology, 2026. [Multiple EHR keyword feeds, 08-23 and 08-24]

Descriptive paper on Danish regional EHR data. Useful as a **reference
for Danish-registry-based clinical epidemiology** if you ever need to
cite the data source, but no methodological or study-design lift here.

---

## Cross-cutting takeaways

1. **AoU is producing an outsized share of HIGH-priority signal this
   window.** Suresh (PNPLA3 × alcohol), Cheng (PiZZ AAT screening),
   Cornell (alcohol × mental-health MR), and Shim & Onnela (Fitbit ×
   PhenoAge) are all AoU-native and all hit multiple threads
   simultaneously. This is the kind of density that argues for
   *biobank-native writing* — starting from AoU as the substrate and
   asking what question its unique data profile unlocks.

2. **The "PGS × exposure / environment" sub-thread is compounding.**
   Suresh (PNPLA3 × alcohol) sits alongside Castañeda (cardiometabolic
   PGS × high altitude); together with the Nagpal & Gibson lineage
   anchor and the Abner-Johnson-Vujkovic-Daly *Nature* 2026 diurnal-
   glucose GWAS from the 08-17 report, we now have a four-paper cluster
   on **G × E in biobanks**. This is starting to look like a natural
   grant-level framing.

3. **TTE frameworks are landing in specialty-clinical journals.** Peng
   (Europace, post-AF-ablation OAC), Garcia-Argibay (Lancet Psychiatry,
   ADHD decision rules), Wood (from 08-11, perinatal T2D) — TTE has
   crossed from the *Am J Epidemiol* methodological literature into
   specialty clinical outlets. This is a good moment for a TTE-focused
   methodology cite-cluster in any pharmacoepi grant.

4. **Rare-disease HPO / DNN benchmarking is heating up.** GenPhenia
   (Brunello, this window) joins GraphRareBench (Guo 08-17) as fresh
   entries in the auditable HPO-driven diagnostic benchmark space.
   Time to consider a head-to-head evaluation across Phenolyzer /
   Phen2Gene / PhenoSV / LIRICAL / Exomiser / PhenoGPT2 / GenPhenia
   on a common eval set with separable ranking-vs-evidence metrics
   as the deliverable.

5. **EHR-model portability audits are a live methodological front.**
   Walsh et al. (npj Digital Medicine, TRD transportability) is the
   first major methodological entry in what INTERESTS.md flags as
   a rising sub-thread (external-validation across BioVU / AoU /
   MIMIC / UKB). This should be a citation anchor in any new
   biobank-model validation paper.

6. **Digital phenotyping via wearables is reaching AoU-native
   analyses.** Shim & Onnela (*Nature Communications*) is a
   template-quality integration of Fitbit + AoU PhenoAge. Portable to
   the digital-twins-from-EHR agenda and to any lifestyle-mediation
   analysis you'd run alongside a pharmacoepi TTE.

## Next-step suggestions

- **Pull the full text on Suresh (PNPLA3 × alcohol in AoU)** — direct
  cite for any G × E writeup you draft on the AoU platform, and
  possibly a comparable-methods citation if you're prototyping
  another AoU G × E analysis.
- **Pull Cheng (PiZZ AAT screening in AoU)** — the *EHR-clinical-score
  → sequencing enrichment* pattern is directly stealable for CFTR
  and APOL1 population-screening work. Extract their
  phecode-feature-set + score-derivation methodology.
- **Pull Walsh (TRD model transportability)** — establish it as your
  citation anchor for the EHR-model-portability sub-thread and
  reference it in any AoU-derived model you take through
  external-validation.
- **Add Zhai *Nat Rev Genet* proteogenomics review** to your reading
  list — this is the "field-defining review" citation for
  multi-omics-augmented PGS grant / methods writeups.
- **Consider a short methods post** on the Kung (regression-not-to-the-
  mean) + Bhandari (zero-inflated causal mediation) pair as pre-TTE
  discipline checks — both fit naturally in a "pre-analysis discipline
  for staggered-initiation pharmacoepi" note.
