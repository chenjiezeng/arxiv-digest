# Research digest report — 2026-08-08

Triage of research-related email + the GitHub `arxiv-digest` repo against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-08-02 12:30Z → 2026-08-08 12:36Z** (~6 days since the
last research-digest report, covering six arxiv-digest cron runs and two
Google Scholar alert batches on 08-07 and 08-08).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-04.md` → `2026-08-08.md`) | 08-04 → 08-08 (10:30Z crons) | 5 daily runs. 08-04: 6 papers; 08-05: 5 (with a score-4 UKB × functional causal inference hit); 08-06: 3; 08-07: 7 (largest batch, incl. AoU MDD PRS × Fitbit at score-4); 08-08: 0 (all previously surfaced). |
| Google Scholar alerts (keyword feeds, 08-08 batch) | 08-08 05:21Z | 12 keyword feeds fired simultaneously (`APOL1`, `knowledge graph`, `UK Biobank`, `variant interpretation`/`variant classification`, `phenome wide association studies`, `electronic health records`, `mendelian diseases`, `autoimmune diseases`, `intitle:"clonal hematopoiesis"`, `rare diseases`, `drug repurposing`, `All of Us research program`, `Foundation models + electronic health records`). Dense APOL1 cluster (3 papers) and HIGH-signal breast-cancer preprint via Bastarache author feed. |
| Google Scholar alerts (author feeds, 08-07 batch) | 08-07 20:16Z | 15+ author feeds fired: Chenjie Zeng (self), Lisa Bastarache, Daniel Kastner, Vivek Natarajan, Zhiyong Lu, Peter Szolovits (2 threads), Marinka Zitnik, Stephen B Montgomery, Kai Wang, Jian Yang (×2 with new-related), Konrad Karczewski, Joshua C Denny (×2), Yuan Luo, George Hripcsak, Jonathan K Pritchard. Densest signal from Bastarache and Denny feeds (Peng et al. early-onset BC + Khan et al. UMOD × PGS). |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated to first
> 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fourteen HIGH items surfaced this window, clustering into five knots
that each stand on their own:

**All of Us + biobank × PGS / functional-longitudinal cluster (3 items).**
Zhang et al. arXiv 2608.06063 — AoU MDD PRS integrated with 180-day
Fitbit wearable trajectories and EHR-defined incident MDD in n=3,030;
C-index climbs 0.637 → 0.705 when PRS + wearable + interaction terms
are stacked, and PRS-stratified HRs show behavior compensates for
inherited liability. This is the endgame for the *composite risk /
PGS × modifiable environment* sub-thread. Ciardulli et al. arXiv
2608.03200 (score-4) — functional propensity score weighting on UKB
BMI trajectories → T2D and HbA1c: extends causal inference to
function-valued exposures, dual-formulation optimization scales to
UKB-sized cohorts. Sasson et al. arXiv 2608.02208 — self-supervised
JEPA on 11k DXA scans, externalized to 47k UKB scans, learns
biological-aging embeddings that predict incident T2D/arthrosis and
whose age-gap *narrows after HRT initiation* — clean modifiable-signal
demo and a template for imaging FMs on biobank data.

**Rare-variant × polygenic composite-risk cluster (2 items).** Khan
et al. medRxiv (Bastarache/Denny author feed) — UMOD T62P intermediate-
penetrance variant × age × PGS interaction for tubular injury: perfect
example of the *rare-variant penetrance modified by polygenic
background* framing your INTERESTS.md variant-interpretation and
composite-risk threads jointly track. Peng et al. medRxiv (Bastarache
author feed) — early-onset breast cancer GWAS + PheWAS in a single
manuscript: directly overlaps Zeng's early-onset BC lineage; the "> 50%
missing heritability" framing signals composite rare+common architecture.

**APOL1 cluster (3 items, all in one 08-08 keyword alert).** Gaheer &
Lanktree *Kidney International* — Q1-vs-Q5 APOL1 proteomic risk score
stratifies CKD from 3% to 62%, outperforms both African-ancestry
proxy and low-risk APOL1 genotype for stratification. Chen et al.
*JASN* — p.N264K protective variant against CKD in HIV+ APOL1
high-risk carriers: the *modifier-variant-rescues-penetrance* story
that mirrors your CFTR-modulator eligibility framing in a different
disease. Kim & Lee *Sclerosis* — first-in-class small-molecule APOL1
inhibitor clinical evidence in APOL1-FSGS. Together these three
transform APOL1 from "high-risk genotype" to a full precision-medicine
disease with a biomarker (proteomic score), a genetic modifier
(N264K), and a therapy (inhibitor) — INTERESTS.md APOL1 thread should
propagate this triad.

**EHR foundation models + causal-inference-in-EHR cluster (3 items).**
Burkhart et al. arXiv (via 08-08 keyword feed) — federated generative
event models on tokenized EHR: directly hits your
*federated / privacy-preserving EHR causal analytics* rising sub-thread.
Foulkes et al. arXiv 2608.04918 — IPW for auxiliary-variable-dependent
sampling in Long COVID RECOVER cohort: this is the *selective-testing
bias in EHR* problem that plagues AoU / UKB analyses whenever an outcome
requires a lab that's only ordered under specific conditions. Noma
arXiv 2608.01625 — R package `TTE` tutorial for target trial emulation,
end-to-end with SGLT2 vs DPP-4 and ARB-vs-CCB examples: this is the
tool your causal-inference thread should adopt for the pharmacoepi
drug-class watchlist (GLP-1 RA, SGLT2i, HRT, CFTR modulator).

**PheWAS / phenotyping infrastructure cluster (3 items).** Hartwell &
Kember *Biol Psy Global Open Sci* — PheWAS pleiotropy review across
alcohol/opioid/tobacco/cannabis + transdiagnostic addiction factor:
canonical review-format piece for the substance-use extension of
PheWAS-thinking. Falzone et al. arXiv 2608.05345 — IL-10 rs1800896
predicts biochemical remission on biologics in IBD (n=197): small,
but exactly the *pharmacogenomic modifier of medication persistence*
rising sub-thread applied to biologics response. Boehler & Cheng
*npj Genomic Medicine* — IMPACT open-source workflow for
phenotype-driven variant interpretation: HPO-driven filtering that
bridges the *variant interpretation* thread and the *rare disease*
HPO-diagnostic-benchmarking thread.

**Drug repurposing / KG cluster (1 item; big).** Siu et al. arXiv
2608.05982 — THBKG temporal biomedical knowledge graph (110k
entities, 11M edges, each with year-stamped evidence) benchmarked
on Phase II → Phase III advancement prediction with *decision-aligned*
evaluation. The novelty is scoring the graph *only on evidence
available at the decision date* — exactly the retrospective-validity
discipline that separates real KG drug-repurposing signal from
leakage-inflated benchmarks. Path-based explainer + release as
continually updated substrate. This is the reference paper your
drug-repurposing thread should crib for KG-with-explainable-hypothesis
work.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-04 → 2026-08-08)

#### HIGH — Zhang Y, Folarin AA, Zhong R, Kim H, Sun S, Stewart C, Dobson RJB. *Longitudinal wearable monitoring and polygenic risk for incident major depressive disorder in the All of Us Research Program.* arXiv 2608.06063v1 (stat.AP, 2026-08-06). Score 4.

n=3,030 European-ancestry AoU adults with ≥180-day baseline wearable
data; 284 incident EHR-defined MDD cases. Time-varying Cox models
stack MDD PRS + monthly Fitbit-derived activity/sleep features +
their interactions. Key findings: higher PRS, lower step count, lower
light/vigorous PA, lower sleep efficiency, and greater sleep-duration
variability all associate with incident MDD. Interaction structure is
biologically satisfying — sedentary time and sleep-variability associations
were *stronger* among high-PRS participants (behavior matters more for
the genetically vulnerable), and equivalent risk in high-PRS participants
required more favorable behavior than in low-PRS peers. Sequential model
build takes C-index from 0.637 (baseline) → 0.705 (full stack). Directly
serves the *composite risk models / PGS × modifiable exposure* rising
sub-thread and the *AoU biobank + wearables* intersection. Portable
template for hereditary-cancer PGS × physical activity / sleep in AoU,
or for CFTR-modulator persistence × behavioral phenotype. AoU-native
so ready for cross-cohort validation in UKB Fitbit substudy.

#### HIGH — Ciardulli S, Fontana N, Vantini S, Ieva F. *Generalized propensity score weighting for functional causal inference framework.* arXiv 2608.03200v1 (stat.ME, 2026-08-04). Score 4.

Extends propensity-score weighting to *function-valued* treatments
(exposure trajectories over continuous time), covariates, and outcomes.
Dual-formulation optimization is smooth/unconstrained and scales to
UKB-sized data. Applied to UKB midlife BMI trajectories → T2D risk and
subsequent HbA1c trajectory (function-on-function marginal structural
model). This is the *methods generalization* your INTERESTS.md causal-
inference and pharmacoepi threads have wanted: it treats time-varying
exposure profiles as first-class objects rather than collapsing them to
a scalar (baseline BMI, mean BMI, area-under-BMI). Direct portability:
CFTR-modulator ppFEV1 trajectory as exposure → BMI/exacerbation
outcome; GLP-1 RA weight-loss trajectory → cardiometabolic outcome;
HRT duration/pattern → dementia risk trajectory. Solves the
"exposure isn't a scalar" objection to observational drug-effect studies.

#### HIGH — Sasson G, Levine Z, Shilo S, Kohn S, Lutsker G, Godneva A, Gabet A, Krongauz D, Weinberger A, LeCun Y, Balestriero R, Segal E. *Self-supervised DXA representations encode multi-system disease risk, biological aging and heritability.* arXiv 2608.02208v1 (cs.CV, 2026-08-03). Score 2.

LeDXA is a JEPA-style vision model trained from scratch on 11,540
unlabeled Human Phenotype Project DXA scans, evaluated on 47,400
external UKB scans. It beats DINOv3 with ~150,000× less data and 40×
fewer parameters, and beats tabular DXA measures for incident disease
prediction (median 4.3-year UKB follow-up), largest gains for hip/knee
arthrosis and T2D (66% of incident hip arthrosis in top-risk quartile
vs. 41% for tabular). Age prediction from embeddings r=0.88 (MAE 2.9y),
biological-age gap tracks disease burden + 45% higher mortality hazard
in the "oldest-appearing" quartile — and the *age gap narrows in women
who started HRT*, a clean pharmacoepi-relevant modifiable signal.
Embeddings recover known body-composition GWAS loci and are more
heritable than DINOv3's. Multiple threads collide here: (1) *imaging
foundation models on biobank data* — DXA as the underused modality;
(2) *biological aging as a modifiable, druggable endpoint*; (3) HRT
persistence in the pharmacoepi thread gets an imaging-biomarker
readout. Template for AoU multi-omics × imaging FM work when AoU
imaging arm matures.

#### HIGH — Noma H. *Target Trial Emulation with the R Package TTE: A Tutorial and Methodological Guide.* arXiv 2608.01625v1 (stat.ME, 2026-08-03). Score 2.

End-to-end tutorial for a new R package covering the full TTE stack:
protocol → eligibility → ITT vs. per-protocol estimands → baseline
and person-period data structures → stabilized treatment/censoring
weights → weight truncation → balance & effective-sample-size
diagnostics → weighted pooled discrete-time survival → model-based
standardization → competing-risk → weighted KM/Aalen-Johansen →
cluster bootstrap. Two synthetic examples: SGLT2i vs DPP-4i initiation
with all-cause death (relevant to your pharmacoepi drug-class thread),
and sequentially-nested ARB-vs-CCB trials with HF hospitalization
+ competing death. If your pharmacoepi work has been split between
ad-hoc scripts and various HERMES-style R packages, this is the
consolidation point. Fits the *TTE-in-EHR* thread and adjacent to
Foulkes et al. below on selection-bias adjustment.

#### HIGH — Foulkes AS, Thaweethai T, Scharfstein DO, Huang W, Reeder HT. *Inverse probability weighting for auxiliary variable dependent sampling in observational studies of Long COVID.* arXiv 2608.04918v1 (stat.ME, 2026-08-05). Score 1.

Two-phase sampling design where testing depends on auxiliary variables
is *ubiquitous in EHR* — every lab that's ordered under specific
clinical suspicion, every specialist-visit-triggered assay. Motivated
by RECOVER Adult + Pediatric cohort. Provides an IPW-based analytic
approach and lays out common pitfalls. Directly addresses the
implicit-selection problem in AoU / UKB / MVP outcome definitions
where the outcome-defining measurement isn't universal. Should be
propagated across every EHR-based cohort study on your pharmacoepi
watchlist (statin-adherence, GLP-1 RA persistence, CFTR modulator
outcomes all rely on outcomes ascertained via non-uniform testing).

#### HIGH — Siu PC, Cabrera C, Mudaliar M, Zubiaga A. *THBKG: A Temporal Biomedical Knowledge Graph for Decision-Aligned Clinical Advancement Prediction.* arXiv 2608.05982v1 (cs.LG, 2026-08-06). Score 1.

Novel angle: existing biomedical KGs let you look up target-disease
evidence *as it stands today*, not as it stood when a Phase II → III
decision was made. THBKG (110,396 entities, 11.1M edges, 19 relation
types, every edge year-stamped) lets you reconstruct evidence
landscape "as of past date X" and benchmark drug-development
advancement predictions with a *decision-aligned* protocol.
Graph-propagation model reaches 4.3–4.5× relative success at top-10
pairs per therapeutic area — and the *gain concentrates on the 72.8%
of pairs with no direct evidence at decision time* (i.e., propagated
biology, not memorized ground truth). Path-based explainer adapted
to the decision-time subgraph gives evidence decomposition. Directly
serves your drug-repurposing thread's stated preference for
"KG/GNN approaches with explainable hypothesis output (path or
subgraph rationales rather than opaque link-prediction scores)."
The retrospective-validity discipline is the transferable idea:
apply the same year-stamp-and-mask protocol to your own
KG-based repurposing benchmarks.

#### HIGH — Falzone MH, Ribaldone DG, Buglione M, Cottone I, Vernero M, Pitoni D, Armandi A, et al. *IL-10 rs1800896 polymorphism predicts biochemical remission in IBD patients undergoing biologic therapy.* arXiv 2608.05345v1 (q-bio.QM, 2026-08-05). Score 1.

n=197 IBD (142 CD, 55 UC) on targeted biologics; 4 cytokine SNPs
tested for association with 12-month biochemical remission (CRP < 5.0
mg/L + calprotectin < 250 µg/g off corticosteroids). IL-10 rs1800896
variant allele → adjusted OR 4.15 (95% CI 1.49–11.56, p=0.007) for
remission. IL-6 rs1800795 C associated with younger diagnosis; TNF-α
rs1800629 A more common in CD than UC. Small sample and open to
selection concerns, but the design is a clean pharmacogenomic-modifier-
of-response study in exactly the framing your INTERESTS.md
pharmacoepi thread wants — *response* as the modifiable outcome, SNPs
as candidate modifiers. Portable to CFTR-modulator response
(ppFEV1 change, exacerbation reduction), GLP-1 RA response, HRT
response.

#### METHODS-WATCH — Datta N, Shatabda S, Rahman MS. *Frozen but Not Always Accessible: A Representation Analysis of Genomic Language Models.* arXiv 2608.05329v1 (q-bio.GN, 2026-08-05). Score 1.

Representation-accessibility audit of DNABERT-2, Nucleotide Transformer,
HyenaDNA, GENERATOR-v2, Omni-DNA under frozen-probing. Frozen probes
recover 95–100% of fine-tuned performance on promoter tasks but only
60–88% on splice site. Layer-wise probing and in silico mutagenesis
suggest local biological signal is present but not accessible via final
pooled embeddings. Not on-thread for clinical work, but useful
methods-watch for foundation-model audits — the same probing protocol
generalizes to EHR-FM benchmarking where "MEDS pretraining performance"
often depends on which layer you probe.

#### METHODS-WATCH — Bouvier F, Peyrot E, Petit F, Porcher R. *Evaluating the influence of treatment-effect heterogeneity on discrimination.* arXiv 2608.06002v1 (stat.AP, 2026-08-06). Score 1.

Explicit study of the relationship between underlying TE heterogeneity
and the discriminative ability of CATE-based individualized treatment
rules (c-statistic-for-benefit, concentration-of-benefit, PAPE) across
20 simulated distributions. Concentration-of-benefit can indicate
perfect discrimination even under negligible heterogeneity — an
important QC warning for any HTE-based analysis you review. Bookmark
alongside Kennedy debiased-ML CATE work.

#### METHODS-WATCH — Xu DA, Tchetgen Tchetgen EJ, Schisterman EF, Blackwell SC, Caniglia EC. *Regression-Based Proximal Reconciliation of Conflicting Trials with Unmeasured Effect Modifiers.* arXiv 2608.04202v1 (stat.ME, 2026-08-04). Score 1.

Proximal / proxy-variable framework for evaluating whether conflicting
RCTs can be reconciled by unmeasured effect modifiers, on additive and
multiplicative scales; illustrated with Meis vs. PROLONG 17-α-hydroxy-
progesterone caproate for preventing preterm birth. Relevant when
your INTERESTS.md pharmacoepi thread encounters conflicting RCT +
observational estimates for the same drug class (statin CV outcomes,
HRT CVD signal).

#### METHODS-WATCH — Maung AA, Zheng Q. *Evaluating Treatment Effects using Group Testing with Retesting of Positive Groups.* arXiv 2608.03224v1 (stat.ME, 2026-08-04). Score 2.

IPW embedded in a pooled pseudo-likelihood for group-testing designs
(pool a bunch of samples, test the pool, retest positives). Purges
selection bias in influenza vaccine effectiveness data. Niche design
but transferable to any surveillance-plus-selective-testing pattern in
EHR/lab data.

#### METHODS-WATCH — Krol A, Rondeau V, Choi Y-H, Briollais L. *Correlated frailty model for analysis of genetic association in family studies.* arXiv 2608.02127v1 (stat.AP, 2026-08-03). Score 1.

Correlated frailty model with residual familial + IBD-based
region-specific correlation structure for testing sets of common /
rare variants against right-censored time-to-event outcomes in
family cancer studies. Marginal likelihood maximized via Marquardt.
Portable to hereditary-cancer syndrome families with time-to-diagnosis
outcomes.

#### SKIP — Chauhan RS, Ghadimi M, Liu L. *Estimating Heterogeneity in Travel Mode Choice Shifts with Causal Forests.* arXiv 2608.04208v1 (stat.AP, 2026-08-04). Score 2.

Off-topic (transportation).

#### SKIP — Iluppangama M, Abeywardana D. *Long-Term Mortality Following STN-DBS in Parkinson's Disease: A Survival Analysis.* arXiv 2608.05609v1 (stat.AP, 2026-08-06). Score 1.

Off-topic (surgical outcome).

#### SKIP — Qian Y, Yin Z, Scott DM, Yan X. *Modeling E-Bike Route Choice in Washington, DC.* arXiv 2608.05449v1 (stat.AP, 2026-08-05). Score 1.

Off-topic (transportation).

#### SKIP — Joshi B. *The Persistence of the Dirty Air Penalty: A Causal Analysis of Formula 1's 2022 Ground Effect Regulations.* arXiv 2608.03192v1 (stat.AP, 2026-08-04). Score 2.

Off-topic (motorsport).

#### SKIP — Yin T et al. *CorePath: A Breast-Specialized Pathology Foundation Model for Core Needle Biopsy Diagnosis.* arXiv 2608.03079v1 (cs.CV, 2026-08-04). Score 1.

Adjacent to breast-cancer thread but no genomic / EHR component;
pathology-specialty FM only.

#### SKIP — Sharipov A, Mukhtarov Y, Molybog I. *Scaling an Autoregressive Transformer for Single-Cell Generation.* arXiv 2608.02961v1 (cs.LG, 2026-08-03). Score 1.

Off-thread (single-cell FM benchmark).

#### SKIP — Xiong J et al. *Beyond Gene Reconstruction: Learning Cell Representations through Complementary Transcriptomic Views.* arXiv 2608.00985v1 (cs.LG, 2026-08-02). Score 1.

Off-thread (single-cell FM benchmark).

#### SKIP — Yu M, Wu Z, Hood MM, Karvonen-Gutierrez CA, Bu F, Elliott MR. *Bayesian Joint Modeling of Longitudinal Symptomatology Scale Responses and Fall Outcomes via Heterogeneous Latent Transition Analysis.* arXiv 2608.00898v1 (stat.AP, 2026-08-01). Score 1.

Adjacent to multimorbidity-clustering but scope is midlife-women SWAN
symptom trajectories → fall outcomes; noted for the SWAN-lineage
readers, not on your active threads.

---

### Scholar alerts — author feeds (08-07 batch)

#### HIGH — Peng S, Jackson VE, Alpen K, Ye Z, Southey MC, Li S. *Genetic susceptibility and causes for early-onset breast cancer: insights from genome-wide and phenome-wide analyses.* medRxiv 2026 (Bastarache author feed).

Single-manuscript GWAS + PheWAS for early-onset breast cancer.
Snippet notes rare pathogenic variants in multiple genes + >200
known common variants leave >50% of familial risk unexplained —
i.e., the target for composite rare + common architecture. Directly
adjacent to Zeng's Nashville Breast Health Study lineage and the
early-onset BC / hereditary cancer thread. This is the paper
to read first from the whole 08-07 author-feed batch: same disease
you've published on, same PheWAS design, same missing-heritability
question. Follow-ups worth checking on full-text: whether they used
UKB or a dedicated case-control cohort, whether PheWAS was pre- or
post-diagnosis (predictor vs. consequence), and whether they stratified
by ER/HER2 subtype (relevant to your JAMA Oncology lineage).

#### HIGH — Khan A, Gresch A, Olinger E, Mariniello M, Shang N, et al. *Uromodulin T62P variant causes kidney tubular stress and injury modulated by age and polygenic risk.* medRxiv 2026 (Bastarache + Denny + Hripcsak author feeds).

"Ultra-rare missense UMOD variants → highly penetrant autosomal
dominant tubulointerstitial kidney disease; the more frequent UMOD
T62P conveys intermediate risk with variable penetrance." Modeled
here as *age × polygenic risk* modifying penetrance. This is
exactly the archetype your INTERESTS.md variant-interpretation and
composite-risk threads jointly track: an intermediate-penetrance
variant whose penetrance is decomposable into age and background
PGS. Portable framework for BRCA1/2 intermediate-effect variants,
CFTR mild variants, and other ACMG "moderate" bucket VUS. Also
gives your rare-variant threading a concrete monogenic × polygenic
interaction story for kidney disease that mirrors what LDLR ×
PGS did for lipid genetics.

#### HIGH — Hudson-Phillips SP, Nanda A, Attia M, AlYaqout W, et al. *The impact of expanded access to germline high penetrance genetic testing for women with a new diagnosis of invasive breast cancer or high-grade DCIS.* Clinical Breast Cancer 2026 (Bastarache author feed).

Germline testing at diagnosis for BRCA1/BRCA2/PALB2 → surgical
decision-making. Directly on-thread for Zeng's cancer-genetic-testing
lineage. Small nuance to watch on full-text: whether "expanded access"
means changed *eligibility criteria* (removing age/family-history
gatekeeping — the NCCN 2020+ policy shift) or *logistical access*
(reduced turnaround, embedded genetic counselors), because these have
different implications for the population-genetics-informed testing
literature.

#### MEDIUM — Turco F, Gillessen S, Tombal B. *PCWG4: A Missed Opportunity to Make Bone-Protective Agents Mandatory for Patients With Bone Metastatic Castration-Resistant Prostate Cancer.* J Clin Oncol 2026 (Chenjie Zeng self-citation feed).

Editorial / commentary from the PCWG lineage on the new Prostate Cancer
Working Group 4 criteria. Downstream of Zeng's prostate-cancer
epidemiology publications (this is why it hit the self-citation feed).
Read if the prostate CRPC subthread is being reactivated; otherwise
low-signal.

#### MEDIUM — Yarman Y. *Mechanistic Insights and Clinical Implications of the Thrombotic Risks of a Highly Prevalent GRK5 Polymorphism Affecting Platelets.* 2027 (2 new citations to Bastarache).

Thesis-formatted piece citing Bastarache-lineage PheWAS work.
Interesting only if the GRK5 signal is used as a case study for
common-variant × pharmacogenomic interaction; otherwise dissertation-tier
depth.

#### METHODS-WATCH — Hilmarsson H, Kumar AS, Barrabés M, Rastogi R, et al. *Scalable high resolution ancestry deconvolution for genomic data.* Nature Communications 2026 (Denny author feed).

Local-ancestry deconvolution methods at higher resolution than
existing tools — matters for ancestry-informed PGS work in AoU /
MVP admixed cohorts. Bookmark alongside Kore et al. (in the prior
report) on local-ancestry-informed rare-variant burden.

### Scholar alerts — keyword feeds (08-08 batch)

#### HIGH — Gaheer PS, Lanktree MB. *CKD Risk Stratification using a Proteomic Risk Score in APOL1 Mediated Kidney Disease.* Kidney International 2026 (APOL1 keyword feed).

Proteomic risk score for APOL1-mediated kidney disease stratifies CKD
risk from 3% (Q1) to 62% (Q5); outperforms both African-ancestry
proxy and low-risk APOL1 genotype baseline for those with a high-risk
APOL1 genotype. Direct win for the APOL1 thread — moves the field
from "test genotype, done" to "genotype + proteomic biomarker,
here's your risk quintile." Read alongside Chen et al. (below)
for the *protective-variant* modifier and Kim & Lee for the
*therapeutic-target* layer.

#### HIGH — Chen J, Mather J, Hung RKY, Hui Q, Winkler C, et al. *Protective Effect of the APOL1 p.N264K Variant Against CKD among People with HIV Carrying APOL1 High-Risk Genotypes.* JASN 2026 (APOL1 keyword feed).

p.N264K as a modifier variant that rescues APOL1 G1/G2 high-risk
carriers from CKD — in the HIV+ population where APOL1 risk is
otherwise strongly manifest. Establishes a within-locus modifier
architecture that changes population-screening implications: reporting
the G1/G2 genotype alone overcalls risk without the modifier check.
Mirrors the CFTR-modifier landscape and the LDLR-null-with-PCSK9-
loss-of-function protective interaction. Perfect *penetrance-modifier*
paper for your variant-interpretation thread.

#### METHODS-WATCH — Kim JY, Lee JY. *Glomerulosclerosis in 2026: From Pathophysiological Mechanisms to Precision Therapeutics.* Sclerosis 2026 (APOL1 keyword feed).

Review-format piece with a mention of first small-molecule APOL1
inhibitor clinical evidence in APOL1-FSGS. Read only for the
therapeutic-development section — pairs with the two APOL1 primary
papers above to complete the biomarker + modifier + therapy triad.

#### HIGH — Hartwell EE, Kember RL. *Exploring the pleiotropic genetic architecture of substance use disorders: Findings from phenome-wide association studies.* Biological Psychiatry Global Open Science 2026 (`phenome wide association studies` keyword feed).

Review of PheWAS results for alcohol, opioid, tobacco, cannabis, and
a transdiagnostic addiction factor. Positions PheWAS as the tool for
mapping pleiotropic architecture of SUDs; canonical review-format
citation for anyone extending PheWAS-thinking into substance-use
genetics. Read for the *transdiagnostic factor* framing especially —
that pattern is portable to the psychiatric multimorbidity thread and
to your PheWAS-of-PheWAS design instinct.

#### HIGH — Burkhart MC, Solo L, Lee I, Charles SK, Liao Z, et al. *Federated generative event models for tokenized electronic health records.* arXiv preprint 2026 (`Foundation models + electronic health records` keyword feed).

Federated generative model over tokenized EHR events — hits directly
on the *federated / privacy-preserving EHR causal analytics* rising
sub-thread. Read for the tokenization scheme and federation protocol;
compare to MEDS event schema. Whether "generative" means synthetic-
patient generation vs. next-event prediction determines which
downstream use it supports (imputation, synthetic-cohort augmentation,
autoregressive prediction).

#### HIGH — Boehler NA, Cheng HYM. *IMPACT: an open-source workflow for unified variant interpretation using phenotype-driven filtering.* npj Genomic Medicine 2026 (`variant interpretation` keyword feed).

Open-source workflow for phenotype-driven variant filtering. Bridges
the *variant interpretation* and *rare disease HPO-diagnostic* threads
of INTERESTS.md. Sits alongside Phenolyzer, Phen2Gene, PhenoSV,
LIRICAL, Exomiser, PhenoGPT2. Read to compare the phenotype-input
layer (HPO vs. clinical text) and whether they use ClinVar/ClinGen
scoring integration.

#### HIGH — Bravo-Perez C, Gurnari C, Durmaz A, Ruiz M, et al. *Multilineage lymphoid clonal hematopoiesis: a cross-sectional, correlative analysis of plasma cell dyscrasias and large granular lymphocytic leukemia.* [Journal TBD] 2026 (`intitle:"clonal hematopoiesis"` keyword feed).

Lymphoid-lineage CHIP correlated with plasma cell dyscrasias / LGL
leukemia. Extends the CHIP thread beyond the canonical myeloid focus
into lymphoid mosaicism. Read for the definition of "lymphoid CHIP"
and how it's operationalized (VAF thresholds, driver gene panel), then
consider whether AoU/UKB WGS could redetect it at population scale.

#### MEDIUM — Raisi-Estabragh Z, Petersen SE, Neubauer S. *Ten Years of Scientific Discovery With the UK Biobank Cardiovascular Magnetic Resonance Imaging Study.* Circulation 2026 (`UK Biobank` keyword feed).

Ten-year retrospective / methods overview of the UKB CMR imaging arm.
Read as reference context for the imaging × biobank thread; not new
primary science but useful for a methods citation when writing about
imaging FMs on biobank data.

#### MEDIUM — Markt SC, Drachenberg C, Zhou A, et al. *Social Determinants of Health, Clinical Outcomes, and Healthcare Resource Utilization in Participants With and Without Narcolepsy in the All of Us Research Program.* [Journal TBD] 2026 (`All of Us research program` keyword feed).

Cohort description with SDoH overlay in AoU. Read only if the narcolepsy
sub-thread is active; otherwise generic AoU descriptive paper.

#### MEDIUM — Zhong H, Zhu J, Liu S, Wong HTH, Zhang Y, Luu HN, et al. *Cross-population proteome-wide mendelian randomization study identifies likely causal proteins for cardiovascular diseases.* Molecular Genetics 2026 (`mendelian diseases` keyword feed).

Cross-population proteome-wide MR for CVD — a growing template for
multi-ancestry drug-target MR. Read alongside the drug-target MR
sub-thread and the multi-omics-augmented PRS thread.

#### MEDIUM — Eriksson D, Kuja-Halkola R, Holmqvist ME, Larsson H, et al. *Tissue-specific clustering of genetic correlations across autoimmune diseases in a nationwide sibling study.* J Clin Invest 2026 (`autoimmune diseases` keyword feed).

Sibling-design for tissue-clustered autoimmune genetic correlations —
family-based design partly controls unmeasured shared environment.
Adjacent to the IBD sub-thread; read if extending IBD work into a
pan-autoimmune framing.

#### MEDIUM — Ng C, Singhera GK, Chang EC, Samra A, Adolphs KA, et al. *Therapeutic Target Mapping to Advance Drug Repurposing for Cardiovascular Disease: A Perspective from an Explanted Heart Biobank.* Journal of [TBD] 2026 (`drug repurposing` keyword feed).

Cardiac tissue biobank–driven target mapping for repurposing. Read for
the sample-provenance-to-target-hypothesis logic — could inspire an
analogous framing where AoU/UKB EHR + genomics drives target
prioritization for a repurposed drug.

#### METHODS-WATCH — Shi D, Chen Z, Song K, Han Y. *Large language model-assisted knowledge graph construction for catalytic systems: Challenges and practical insights.* Chinese Journal of Chemical Engineering 2026 (`knowledge graph` keyword feed).

Off-domain (catalysis), but the "LLM-assisted KG construction"
methodology is portable — if you're using LLMs to expand biomedical KGs,
this is a mirror-image case study of the tooling.

#### METHODS-WATCH — Zhou Y, Huang X, She X, Hao Q, Mi Z, Yang Y. *Mapping the immune-genetic architecture of Epstein-Barr virus-related phenotypes and multiple sclerosis through a single-cell genetic framework for target prioritization.* Mult Scler Relat Disord 2026 (`phenome wide association studies` keyword feed).

Single-cell genetic framework for EBV × MS target prioritization —
adjacent to the pathogen-triggered-autoimmunity story; niche for the
KG × drug-target thread if targeting immune-mediated diseases.

#### METHODS-WATCH — Hernandez-Diaz CA, Vazquez B, Fuentes-Pineda G. *Deep learning for multivariate time series analysis in electronic health records: a scoping review.* Evolutionary Intelligence 2026 (`electronic health records` keyword feed).

Scoping review of DL for EHR time series. Reference-list mining candidate
only — probably nothing new for the EHR-FM sub-thread.

#### LOW — Suprianto S, Messe Y, Hamzah RAH, et al. *Gene therapy for rare diseases marks a new era in precision medicine: Insights from clinical trials.* Narra X 2026 (`rare diseases` keyword feed).

Broad clinical-trial review; low-signal.

#### LOW — Kim Y, Gu K, Park C, Park C, Schmidgall S, Heydari AA, et al. *Capable language models can outgrow the benefits of collaboration.* Nature Machine Intelligence 2026 (Zhiyong Lu author feed).

Multi-agent LLM benchmarking result. Adjacent to LLM-agent-tooling
threads but not on your clinical-agent sub-threads.

#### LOW — Xu Z, Agrawal P, Asadi K, Chen T, Hu C, Johnson J, et al. *The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers.* arXiv 2026 (Marinka Zitnik author feed).

LLM retrieval architecture argument — off-thread for clinical work.

#### LOW — Woo HJ, Kim MG. *A hybrid Monte Carlo–LLM framework quantifies model-and architecture-dependent variability in synthetic-patient simulations.* Scientific Reports 2026 (10 new citations to Vivek Natarajan).

Model-variability audit for synthetic-patient simulations — read only
if extending the LLM-for-synthetic-EHR-generation sub-thread.

#### LOW — Jiang YF, Guo Y, Yao WY, Qiu A, Wang CL, Xu RH, et al. *Genome-wide DNA methylation analysis in pigs using long-read sequencing unveils high-altitude adaptation and allele-specific regulation.* BMC Genomics 2026 (Stephen B Montgomery author feed).

Off-species; low-signal for human-EHR-focused work.

#### LOW — Wang W, Lu Z, Liu F, Chen C, Peng Y, Chen W, Li C, et al. *GenoGraphNet: Pathway-Level Genomic Reasoning with Clinical Language Alignment for Idiopathic Male Infertility Prediction.* IEEE Access 2026 (7 new citations to Kai Wang).

Pathway-level GNN for infertility prediction — off-thread.

#### LOW — Li Y, Yi Z, Dong X, Sun R, Gao L, Zheng Y, Liu H. *Genome-wide association study identifies toll-like receptor four protein-mediated metabolic remodelling affecting gout pathogenesis.* Journal of [TBD] 2026 (multiple author feeds: Jian Yang, Jonathan Pritchard, Chenjie Zeng self-citation).

Gout GWAS with TLR4 metabolic angle. This one pinged three separate
author feeds — read only if extending into gout / TLR4 as an
inflammation-genetics vertex.

#### LOW — Akillioglu M, Cuceoglu MK, Bilginer Y, Ozen S. *Immune Dysregulation and Lymphoma Risk in Deficiency of Adenosine Deaminase 2.* Int J Rheum Dis 2026 (6 new citations to Daniel Kastner).

DADA2 vasculitis / immune-dysregulation single-disease piece — read
only if the DADA2 / VEXAS sub-thread is active.

#### LOW — Mukhi A. *A Silver Trauma Score: Development and Validation of a Geriatric Trauma Risk Stratification Framework for Mortality Prediction and ED-to-ICU Triage.* 2026 (6 new citations to Yuan Luo).

Geriatric trauma triage — off-thread.

#### LOW — He Z, Chu B, Yang J, Gu J, Chen Z, Liu L, Morrison T, et al. *CIT-Lasso: a scalable approach beyond guilty by association for identifying causal variants from genome-wide summary statistics.* Genome [TBD] 2026 (Jian Yang author feed).

Fine-mapping methods paper — bookmark for the fine-mapping /
colocalization sub-thread if pursued.

#### LOW — Shinsato RN, Lovato DV, Vaz IM, Herai RH. *A rare heterozygous non-synonymous PCDH19 variant of uncertain significance associated with female-limited epilepsy caused by cellular-interference—Case report.* [Journal TBD] 2026 (9 new citations to Konrad Karczewski).

Single-case-report for PCDH19 female-limited epilepsy — off-thread.

---

## What's NOT in the report

- **NCBI My-NCBI What's-New batches** (AoU / UKB / drug repurposing) —
  none fired in the searched window; the last batch was in the 08-02
  report. Next fire due should be captured in the next report.
- **bioRxiv / medRxiv Subject Collection Alerts** — none surfaced in the
  searched window; the on-thread medRxiv items above (Peng et al. early-
  onset BC; Khan et al. UMOD) came via the Bastarache author-feed cross-
  reference rather than the subject-collection alert.
- **Substack / newsletters** — the AI News, State AI, and Paperclip
  emails in this window were noted but none had biomedical content that
  crossed the on-thread threshold.
- **arxiv.org daily category mailings** — the raw `cs`, `stat.AP`,
  `q-bio` daily mailings from no-reply@arxiv.org are the upstream source
  that feeds the arxiv-digest pipeline; individual papers surfaced via
  the digest are covered in the arxiv-digest section above rather than
  re-listed from the raw mailings.

## Next steps to consider

1. **Read Peng et al. early-onset BC medRxiv full text.** Highest-signal
   single item for the Zeng cancer-genetics lineage in months.
2. **Bundle the three APOL1 papers** (Gaheer/Lanktree proteomic score +
   Chen et al. N264K + Kim/Lee inhibitor review) into a short APOL1
   thread update — the field just gained a biomarker, a modifier, and a
   therapy in the same week.
3. **Add Noma TTE R-package** to the pharmacoepi tooling shortlist for
   the next drug-class analysis (SGLT2i / GLP-1 RA / HRT / CFTR
   modulator).
4. **Consider a follow-up composite-risk-review piece** stitching
   Zhang AoU MDD PRS × wearable + Khan UMOD × PGS + Baya-lineage
   PGS-residuals framing (from the 07-27 report) into a single
   PGS-as-discovery-instrument argument.
5. **Cite THBKG in the drug-repurposing KG discussion** — the year-
   stamped decision-aligned evaluation is a novel methods lever.

_Report generated 2026-08-08 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-08 → next scheduled run._
