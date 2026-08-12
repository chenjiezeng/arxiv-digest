# Research digest report — 2026-08-12

Triage of research-related email + the GitHub `arxiv-digest` repo against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, EHR knowledge representation).

Window: **2026-08-08 12:36Z → 2026-08-12 12:38Z** (~4 days since the
last research-digest report, covering four arxiv-digest cron runs and
five Google Scholar alert batches on 08-09, 08-10, and 08-11).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-08.md` → `2026-08-12.md`) | 08-08 → 08-12 (10:30Z crons) | 4 daily runs. 08-08 and 08-10: 0 papers (all previously surfaced or empty window). 08-11: 5 papers (2 causal-inference / propensity score, 1 CHIP zero-inflated longitudinal, 1 UKB imaging FM, 1 motor insurance DAG). 08-12: 2 papers (LLM-assisted g-computation, perinatal pharmacoepi TTE). |
| Google Scholar alerts (author feeds, 08-09 batch, 01:11Z) | 08-09 01:11Z | ~15 author feeds fired: Kai Wang, Jonathan Marchini, Pascal Brandt, Miguel Hernán, Joshua C Denny, George Hripcsak, Yuan Luo, Konrad Karczewski, Michael Snyder, John A Capra, Marinka Zitnik, Zhiyong Lu, James Zou, Stephen B Montgomery, Jian Yang. Densest signal: Kai Wang (GABA-A LOF/GOF predictor, UKB germline prostate PCSM), Marchini (FNIP1 Nature 1M humans), Brandt (AF-screening Circulation + federated GEMs). |
| Google Scholar alerts (keyword feeds, 08-09 batch, 08:53Z) | 08-09 08:53Z | Partial keyword-feed fire: `Foundation models + EHR`, `rare diseases`, `intitle:"clonal hematopoiesis"`, `knowledge graph`, `electronic health records`. Highest signal: Jiang et al. Translating EHR FMs into clinical decision support. |
| Google Scholar alerts (author feeds, 08-10 batch, 06:32Z) | 08-10 06:32Z | 13 author feeds fired but mostly incidental cites. Signal: Cruz-Gonzalez methylation clocks generalization failure across admixed individuals (via Capra feed) — direct hit on portability / fairness sub-thread. |
| Google Scholar alerts (keyword feeds, 08-11 batch, 01:46Z) | 08-11 01:46Z | 12 keyword feeds fired: APOL1 (cluster of 5), variant interpretation (cluster of 6, incl. ClinGen concordance benchmark), PheWAS (KGGSV structural variants), All of Us (cluster of 6, incl. MR alcohol × mental health), UK Biobank, rare diseases, autoimmune, foundation-models, EHR, drug repurposing, mendelian diseases, clonal hematopoiesis. |
| Google Scholar alerts (author feeds, 08-11 batch, 23:58Z) | 08-11 23:58Z | ~25 author feeds fired. Dense signal from Chenjie Zeng self-feed (Prokunina-Olsson multi-pop bladder cancer GWAS in Nat Commun), Patrick Ryan (Mann SELECT+FLOW+SOUL semaglutide kidney), Denny+Bastarache (KGGSV SV-PheWAS again), Karczewski (CTNND1 hereditary gastric), Kastner (CDC42 inflammasome pair), Miguel Hernán (Yu insulin initiation T2D), Jian Yang (Dutta cancer PRS+proteomics Cell Genomics), Szolovits (dynamic red-teaming health LLMs Nature Health). |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated to first
> 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Nineteen HIGH items surfaced this window, clustering into six knots that
each stand on their own:

**Structural-variant PheWAS at biobank scale (1 item, cross-fed).**
Li et al. medRxiv/Research Square — **KGGSV**, a high-performance
framework that bridges individualized SV callsets to phenome-wide
association at biobank scale. Landed in three separate alerts
(`phenome wide association studies` keyword, plus Bastarache and Denny
author feeds), which is the pattern you get when a paper crosses
methods-provider *and* two curators-of-record for the field. Directly
serves the *PheWAS / phecode infrastructure* thread: SVs have been the
missing modality in most PheWAS pipelines (SAIGE-QT and REGENIE
naturally handle SNV/indels, SV integration lags), and a scalable SV-
PheWAS puts them into the same phecode-based outcome layer as everything
else. Immediate crib for extending KGGSV to phecodeX and to All of Us
long-read SV callsets when they land.

**Variant interpretation cluster (3 items).** Sulaiman & Oyeyemi
(Research Square) — first systematic **ClinGen Evidence Repository**
benchmark of automated ACMG/AMP tools, exactly the missing
audit-of-audit study you would want before wiring any automated
classifier into an operational pipeline. Boßelmann et al. *EBioMedicine*
— an accurate **GOF/LOF missense predictor for GABA-A receptors**
built from 505 affected individuals × 272 (likely) pathogenic variants,
with the tie to treatment response that makes it a *variant-directs-therapy*
model rather than a *variant-classifies-pathogenicity* model. De Souza
et al. *Gastric Cancer* — germline WES in a large Brazilian gastric
cancer cohort nominating **CTNND1** as a candidate hereditary gastric
cancer gene, extending the CDH1/CTNND1 axis that Zeng's hereditary
cancer lineage already engages. Together these cover the three regions
of the variant-interpretation triangle: audit (Sulaiman), functional
prediction (Boßelmann), and novel-gene curation (de Souza).

**APOL1 cluster (5 items).** Poudel & Susztak *Circulation* response
letter — reaffirms the **podocyte cell-type hierarchy** driving the
mouse APOL1-hypertension-renal-damage phenotype, with the reply-letter
by Hu et al. flagging effect modification by comorbid conditions as
the next testable question. Papasavva et al. *Blood Advances* — the
**inaxaplin (APOL1 small-molecule inhibitor)** thread now expanding
into sickle cell disease and other β-hemoglobinopathies, corroborating
the "APOL1 is becoming a full precision-medicine disease" arc from
the 08-08 report. West UW dissertation — sociocultural / community-
engagement framing of APOL1 testing in African American populations,
useful counterweight to the mostly-mechanism/therapy content in the
same alert. Combined with the last window's Chen JASN N264K modifier
and Gaheer/Lanktree proteomic risk score, APOL1 remains the highest-
velocity single-gene precision-medicine story in your alert stream
this month.

**EHR foundation models + causal-inference-in-EHR cluster (3 items).**
Jiang et al. Preprints.org — **Translating EHR foundation models into
clinical decision support**: a translational-pipeline framing paper
spanning data resources, model choice, and real-world deployment.
Reads as the "what does it take to move CLMBR / MOTOR / MEDS into an
actual CDS panel" survey the field has been missing. Burkhart et al.
arXiv 2608.02939 — **federated training of tokenized generative event
models across 122k patients**, directly the *federated / privacy-
preserving EHR analytics* rising sub-thread from INTERESTS.md, with
"substantial performance degradation under cross-site transfer" as the
explicit motivation. Nadarajah et al. *Circulation* — **risk-guided
AF screening** ML model on EHRs, externally validated and
*prospectively tested*: crosses from "yet another AF risk model" to
"AF risk model with the deployment story", making it the reference
for how to structure an EHR-derived ML → RCT translational chain.

**AoU / biobank pharmacoepi + composite-risk cluster (4 items).**
Cornell et al. *Military Medicine* — two-sample **Mendelian
randomization in AoU** of alcohol → depression/anxiety/PTSD/AUD; first
substantial military-mental-health MR piggyback on AoU I've seen, and
importantly a *methods portability* demo that AoU can host MR studies
alongside its more standard cohort work. Mann et al. *Lancet Diabetes
& Endocrinology* — prespecified pooled analysis of **SELECT + FLOW +
SOUL semaglutide trials** for kidney outcomes: the trials your
GLP-1-RA pharmacoepi thread needs a citation for whenever anyone asks
"but are the observational kidney signals confirmed in trials?" Dutta
et al. *Cell Genomics* — **PRSs for 21 cancers × 4,955 plasma proteins**
in cancer-free UKB participants, mapping trans-regulated protein
networks under polygenic liability. Cleanly hits the *multi-omics-
augmented PRS* rising sub-thread; sets up the composite-risk framing
where PRS *residuals* pick out proteomic cascades rather than SNP-level
noise. Hindy et al. *Nature* — **FNIP1 protein-truncating variants in
~1M humans** associated with a favorable-metabolism profile: an
exemplar rare-variant-with-favorable-effect discovery in a
biobank-scale rare-variant aggregation, mirroring the SLC30A8, PCSK9,
GPR75 lineage.

**Somatic mosaicism / CHIP-methods cluster (2 items).** Bandreddi &
Machiela et al. arXiv 2608.09725 (via 08-11 digest) — mixed-model
Tobit vs two-part hurdle for **zero-inflated longitudinal clonal
fraction data** in the PLCO cohort, deriving the mathematical
condition under which the two models are equivalent (probit link on
the binary process). This is a small paper but exactly the *statistical
plumbing for CHIP-VAF trajectories* that every CHIP longitudinal
analysis quietly gets wrong. Portable to LOY VAF trajectories directly.
Okazawa-Sakai et al. *J Gyn Onc* — **cfDNA-inferred putative clonal
hematopoiesis during platinum → PARP-inhibitor maintenance in
ovarian cancer**, a therapy-induced CH signal from routine tumor
sequencing residuals, portable to any solid-tumor cohort with
comprehensive cfDNA panels. Together these keep the CHIP thread
alive with a methods paper + a therapy-induced-CH signal.

**Genetic epidemiology + hereditary cancer (2 items).**
Prokunina-Olsson et al. *Nature Communications* (via Chenjie Zeng
self-feed) — **multi-population GWAS meta-analysis of bladder cancer**
with 32,470 cases across populations, highlighting genetic regulation
of smoking-related risk. Direct extension of Zeng's multi-ancestry
cancer-genetics lineage, with cross-population smoking-interaction
architecture that reads as a template you should have on hand for
the next similar analysis. Lu et al. *Prostate Cancer & Prostatic
Diseases* (via Kai Wang citation feed) — **germline risk and prostate
cancer-specific mortality in n=14,644 UKB incident cases**, tightening
the association between germline architecture and mortality endpoints
rather than incidence — the harder and more clinically actionable
comparison.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest (2026-08-08 → 2026-08-12)

**HIGH — Bandreddi, Zhang, Kelly, Machiela, Albert.** *Comparing Tobit
and Two-Part Hurdle Models for Semi-Continuous Longitudinal Data with
an Application to Clonal Hematopoiesis.* arXiv 2608.09725 (stat.AP),
2026-08-10. **Thread: CHIP / VEXAS / LOY & somatic mosaicism +
statistical plumbing.** This is a small but genuinely useful
methods-of-record paper: they derive the mathematical conditions under
which the mixed-model Tobit and two-part hurdle formulations are
equivalent (probit link on the binary process → Tobit reduces to a
hurdle special case), show via simulation that the hurdle is more
robust when Tobit assumptions fail, and apply both to longitudinal
clonal-fraction VAF trajectories in the Prostate/Lung/Colorectal/
Ovarian (PLCO) cohort. The applied punchline is that estimates from
Tobit, hurdle, and a standard linear model that *ignores* zero
inflation were broadly consistent for the PLCO CHIP/mCA associations —
which is reassuring for prior literature but doesn't argue against
adopting the hurdle model prospectively. This is directly portable to
LOY-VAF longitudinal analyses (Kessler-lineage) where the zero-
inflation problem is even more pronounced because most men don't
carry detectable LOY at any given draw. Recommend crib as the
statistical reference the next time anyone in the CHIP/LOY thread
proposes a longitudinal VAF model.

**HIGH — Vossler, Ouyang, Guo, Huang, Shojaie, Zier, Xia, Feng.**
*Expert-Guided g-computation with Large Language Models for Estimating
Causal Effects on Timings: Applications to Hospital Quality
Improvement.* arXiv 2608.10339 (stat.ME), 2026-08-11. **Thread: Causal
inference + agentic / LLM-assisted causal pipelines.** They propose
"egg-computation" — an LLM-scaffolded variant of g-computation that
uses expert reasoning encoded through Gantt-chart-style patient
trajectories to identify components that are unidentifiable from data
alone, then delegates the identifiable pieces to standard causal
estimation. In simulations they beat conventional causal-inference
methods when patients have diverse causal structures / intervention
mechanisms, and in an eleven-intervention hospital quality-improvement
study at an urban safety-net hospital the LLM-generated causal graphs
and time-saving estimates were highly concordant with human experts.
This lands squarely in your rising *agentic / human-in-the-loop
observational-causal-inference pipelines* sub-thread (Chou/Kallus
oci-agent lineage): same pattern of automating the scalable pieces and
routing expert judgment to what only experts can decide. Framework is
broadly applicable beyond healthcare, which raises portability
questions worth prototyping on an EHR quality-improvement problem you
already have (readmission LOS, ICU boarding).

**HIGH — Chen, Zuo, Stevens, Pollack, Xi, Petito, Zhao, Zhang.**
*Clustering Informed Inverse Probability Weighting Strategies for
Causal Effect Estimation in Observational Studies.* arXiv 2608.09839
(stat.ME), 2026-08-10. **Thread: Causal inference & pharmacoepi.**
Compares three IPW strategies — standard IPW, clustering-augmented IPW
with cluster-specific propensity score models, and a global PS model
with estimated cluster membership as a covariate — under both
correctly-specified and omitted-covariate propensity models across
n=100 to 500. Neither cluster-informed strategy dominates: clustering-
augmented IPW wins on MSE when latent structure is present, the global
model wins on bias and CI coverage at small samples. Applied to n=966
breast cancer patients on carboplatin using generalized PS to model
dose-response of treatment cycles → hypersensitivity reaction risk.
Standard vs clustered analyses produce similar *pooled* estimates but
the clustered analysis surfaces subgroup-specific dose-responses. The
practical takeaway is a reminder that IPW misspecification is a
subgroup-structure question, not just a covariate-selection question,
and that clustering can serve as a diagnostic. Modest sample size
limits how far you'd push it; useful reference for the pharmacoepi
target-trial-emulation thread when subgroup HTE is on the table.

**METHODS-WATCH — Kevopoulos, Moscoloni, Alheit, Beeche, Chirinos,
Heinlein, Peirlinck.** *Flow-based conditional cardiac anatomy
generation for virtual cohorts.* arXiv 2608.09460 (cs.LG), 2026-08-10.
**Thread: Biobanks with EHR linkage — UK Biobank + imaging FMs.**
CAN-FLOW: two-step conditional normalizing-flow generative model for
biventricular cardiac anatomy conditioned on sex/age/BMI, trained on
2,208 healthy UKB subjects. Not clinically actionable for the disease
threads you track, but the modeling pattern — geometry-only latents
first, metadata-conditioned flow second — is a clean template if you
ever want to build a virtual-cohort augmentation for a rare-disease
imaging phenotype where the real cohort is too small. Cross-references
against the "digital twins from EHR" rising sub-thread as the imaging
half of the twin.

**METHODS-WATCH — Wood, Platt, Hutcheon, Cohen, Latour, Margulis,
Petito, Grandi.** *Early Pregnancy Treatment Decisions: Designing
Perinatal Pharmacoepidemiology Studies using Real-World Data.* arXiv
2608.11108 (stat.AP), 2026-08-11. **Thread: Causal inference &
pharmacoepi + target trial emulation.** Extends TTE to pregnancy-
specific challenges (right-and-left censoring, competing events,
etiologically susceptible periods, gestational length differences),
with a worked example on T2DM medication regime changes. Not directly
in your disease scope but a portable methods reference for TTE
extensions when the eligibility window has structural complications.
Note this and the Ciardulli / Noma TTE tutorials from the last window
form a coherent methods trilogy worth flagging in the pharmacoepi
methods watchlist.

**SKIP — Charpentier.** *From Rating Factors to Crash Mechanisms: A
Multiscale Causal DAG Framework Linking Motor Insurance and Road
Safety.* arXiv 2608.09441 (stat.AP). Motor insurance and road safety;
matched on `motor` keyword. Solid causal-DAG framing but no biomedical
relevance for your threads.

**SKIP — Luo, Tao, Zeng, Wang, Ouyang, Zhu, Liu, Chen, Liu.** *VOICE:
A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based
Prediction of In-situ Single-Cell Gene Expression.* arXiv 2608.08366
(cs.CV). Spatial-transcriptomics foundation model; matched on
`foundation model` keyword. Not clinically actionable for your
active-thread rubric even though the multimodal FM pattern is elegant.

---

### Scholar alerts (2026-08-09 → 2026-08-11)

**HIGH — Li, Peng, Zhang, Huang, Wei, Liu, Fang.** *A scalable
framework enables phenome-wide association of structural variants in
biobank cohorts.* medRxiv/Research Square rs-10237876, 2026. **Thread:
PheWAS / phecode infrastructure.** Introduces KGGSV, a high-performance
framework bridging raw individualized SV callsets to biobank-scale
PheWAS. Surfaced simultaneously in three alerts (`phenome wide
association studies` keyword feed + Bastarache and Denny author
"related research" feeds), which is the pattern for
methods-infrastructure papers that the field's PheWAS-adjacent
curators consider load-bearing. Structural variants are a persistent
gap in PheWAS because standard mixed-model pipelines (SAIGE, REGENIE)
assume SNV/indel calls; SVs land through separate callers and are
usually analyzed in bespoke frameworks that never make it to the
phecode-outcome layer. KGGSV's contribution is exactly that plumbing.
Immediate downstream implication: retrofittable to All of Us long-read
SV callsets when v9 lands, and to any hospital biobank with WGS.
Recommend pulling the preprint and reading in full before the next
time you propose an SV analysis.

**HIGH — Sulaiman, Oyeyemi.** *Concordance of Automated ACMG Variant
Classification with Expert-Curated Assertions: A Systematic Evaluation
Using the ClinGen Evidence Repository.* Research Square rs-10615801,
2026. **Thread: Variant interpretation.** First systematic benchmark
of the field's automated ACMG/AMP tools against ClinGen Expert Panel
gold-standard assertions from the Evidence Repository. This is the
"audit-the-audit" paper the field has needed — most automated ACMG
tools are validated against ClinVar assertions of variable quality,
not the tighter ClinGen VCEP curations. The result matters
independent of the tool ranking: whatever tool you're using in a
pipeline, this becomes the appropriate calibration reference. Fits
your variant-interpretation thread directly and is worth reading for
the tool-by-tool breakdown when it fully publishes.

**HIGH — Boßelmann, Ortiz, Dahl, Liao, et al.** *Accurate prediction
of gain-and loss-of-function missense variants in GABA-A receptors.*
EBioMedicine, 2026. **Thread: Variant interpretation + rare-disease
HPO-driven diagnostics.** Trained on 505 affected individuals × 272
(likely) pathogenic GABA-A receptor missense variants, with variant
effects on channel biophysical function tied to key clinical
characteristics and treatment response. This is the *variant-directs-
therapy* framing that argues variant interpretation should aim beyond
pathogenic/benign and into functional-consequence prediction with
therapy implications — an important sub-thread for the epilepsies and
for other channelopathies where GOF vs LOF distinguishes drug class.
Portable modeling pattern (functional-outcome-driven curation instead
of ClinVar-driven curation) worth cribbing for other ion-channel
gene families and for KCNQ / SCN.

**HIGH — De Souza, Buranello, Neto, Pisani, et al.** *Germline
whole-exome sequencing identifies CTNND1 as a candidate gene for
hereditary gastric cancer in a large Brazilian cohort.* Gastric
Cancer, 2026. **Thread: Variant interpretation + hereditary cancer +
genetic epi.** Extends the CDH1 / CTNND1 (p120-catenin) axis in
hereditary diffuse gastric cancer using a Brazilian founder-population
cohort. CTNND1 is already tentatively on the HDGC-candidate list;
this adds another population's evidence for elevating it. Directly
relevant to Zeng's hereditary cancer lineage; also a useful data
point for the *ancestry-stratified rare-variant burden in hereditary
cancer* sub-thread. Should propagate to any HDGC gene-panel discussion
you contribute to.

**HIGH — Hindy, Adam, Sosina, Pryce, Blair, et al.** *FNIP1 variants
are associated with favourable metabolism in 1 million humans.*
Nature, 2026. **Thread: Genetic epidemiology + biobank-scale rare
variant.** Rare-variant meta-analysis at ~1M-human scale identifying
FNIP1 protein-truncating variants that produce a favorable
cardiometabolic profile. This joins the lineage of favorable-effect
loss-of-function discoveries (SLC30A8 → T2D protection, PCSK9 → LDL
lowering, GPR75 → obesity protection, INHBE → adiposity) that
motivates the pharma-target-search framing of biobank rare-variant
work. Immediate ripple for the *drug-target Mendelian randomisation*
sub-thread: FNIP1 becomes a candidate for MR triangulation
(FNIP1-lowering as therapeutic proxy → cardiometabolic outcomes).

**HIGH — Dutta, Zhang, Guo, Quint, Rooney, et al.** *Polygenic risk
scores and plasma proteomics identify cancer-related proteins and
trans-regulated protein networks.* Cell Genomics, 2026. **Thread:
Genetic epi (multi-omics-augmented PRS) + composite risk.** Integrates
PRSs for 21 cancers with 4,955 plasma proteins in cancer-*free* UKB
participants to map trans-regulated protein networks that light up
under polygenic liability. This is exactly the *multi-omics-augmented
PRS* rising sub-thread in INTERESTS.md and complements the
composite-risk framing where PRS residuals / cancer-related proteomic
cascades can serve as either intermediate phenotypes or additional
prediction features. Cross-cancer scope (21 sites) is unusual — most
PRS × proteomics work is single-cancer — so the network structure
across cancers is the novel signal. Should be a citation the next time
a proteomics × cancer-PRS analysis surfaces.

**HIGH — Jiang, Dai, Zhang, Gao, Chen, Du, Liu, et al.** *Translating
Electronic Health Record Foundation Models into Clinical Decision
Support.* Preprints.org 202608.0522, 2026. **Thread: EHR foundation
models + digital twins from EHR.** Translational-pipeline framing
paper covering the full CLMBR → MOTOR → MEDS → deployed CDS chain:
data resources, model choice, evaluation, and real-world integration.
The field has plenty of "we built a foundation model on 10M patients"
papers and very few "here is what breaks when you try to route the
model's predictions to a clinician" papers; this is the second type.
Direct read-first candidate for your EHR-FM thread this week — it
should sharpen the vocabulary you use when discussing what any given
EHR-FM benchmark paper actually promises.

**HIGH — Burkhart, Solo, Lee, Charles, Liao, et al.** *Federated
generative event models for tokenized electronic health records.*
arXiv 2608.02939, 2026. **Thread: EHR FMs + federated / privacy-
preserving EHR causal analytics.** Evaluates federated training of
tokenized generative event models (GEMs) across 122,251 patients,
motivated explicitly by the "substantial performance degradation
under cross-site transfer" problem that CLMBR/MOTOR-lineage models
inherit whenever they're trained at one site and deployed at another.
This lands squarely on the *federated / privacy-preserving EHR
causal analytics* rising sub-thread from INTERESTS.md (companion to
the Jang et al. distributed-mediation design pattern already logged).
The tokenized-generative-event framing is portable to counterfactual
patient-trajectory generation for causal analysis, so this is worth
tracking through peer review.

**HIGH — Cornell, Shukla, McMillan, Gdovin, Smetana, et al.**
*Estimating the Causal Effect of Alcohol Consumption on
Military-Relevant Mental Health Conditions: A Mendelian Randomization
Study Using the All of Us Research Program.* Military Medicine, 2026.
**Thread: Biobanks with EHR linkage (AoU) + causal inference.**
Two-sample MR in AoU estimating causal effects of alcohol consumption
on depression, anxiety, PTSD, and alcohol conditions. This is the
first substantial military-mental-health MR piggyback on AoU I've
seen surfaced, and importantly is a *methods portability
demonstration* — AoU can host MR studies alongside its more standard
cohort/PheWAS work, which unlocks the entire biomarker-as-exposure
scan menu for AoU. Recommend as the AoU-MR reference case if anyone
in your circle proposes an MR analysis and asks whether AoU is a
plausible substrate.

**HIGH — Nadarajah, Wu, Wahab, Reynolds, Haris, et al.**
*Risk-Guided Screening for Atrial Fibrillation Using Electronic
Health Records.* Circulation, 2026. **Thread: EHR phenotyping + ML
for precision health.** ML prediction model on EHRs to guide risk-
based AF screening — developed, externally validated, *and
prospectively tested*. Most EHR-derived risk-model papers stop at
external validation; the prospective-test layer is what moves this
from "yet another AF risk score" to a reference example for how the
EHR-derived-risk → RCT-tested-screening translational chain should
be structured. Directly the *ML → clinical decision* framing your
INTERESTS.md ML-for-precision-health thread specifies as HIGH. Read
this in full if AF or arrhythmia is anywhere in the next collaboration
you take on.

**HIGH — Mann, Badve, Baeres, Belmar, et al.** *Effect of semaglutide
on kidney outcomes in the SELECT, FLOW, and SOUL trials: a
prespecified pooled analysis.* Lancet Diabetes & Endocrinology, 2026.
**Thread: Pharmacoepi — GLP-1 RA pharmacoepi thread.** Prespecified
pooled analysis across the three largest semaglutide trials with
kidney outcomes. This is the trials-level anchor that the
observational GLP-1 kidney signals you've been tracking need to be
triangulated against, and it should sharpen your causal-inference
discussions about the observational-vs-trial concordance question
that drives the pharmacoepi thread. High-priority read for the
GLP-1-RA sub-thread.

**HIGH — Krüger, Schneeweiss, Wang.** *Tirzepatide and the risk of
atherosclerotic cardiovascular events: population based cohort study.*
BMJ, 2026. **Thread: Pharmacoepi — GLP-1 RA lineage.** Population-
based cohort estimating tirzepatide → ASCVD event reduction
magnitude. Schneeweiss authorship signals rigorous pharmacoepi design
(likely TTE + high-dimensional PS). This is the observational
tirzepatide-CV story that the SURPASS-CVOT trial won't answer for
years; useful pairing with the Mann pooled semaglutide analysis for
a "GLP-1-adjacent-agent CV signal" narrative.

**HIGH — Yu, Zhang, Zapata-Bravo, Platt, Reynier, et al.** *Time to
Insulin Initiation Among Patients With Type 2 Diabetes Treated With
Second-Line Antidiabetic Drugs.* Diabetes, Obesity and Metabolism,
2026. **Thread: Pharmacoepi — T2D drug-class watchlist + medication
persistence.** Real-world time-to-insulin comparison across second-
line T2D drug classes. Platt authorship signals pharmacoepi-methods
rigor (TTE + treatment-strategy comparisons). Directly relevant to
the *pharmacogenomic modifiers of medication persistence* rising
sub-thread, though this paper is likely non-genetic; the outcome
definition (time-to-insulin-initiation as a durability proxy) is
worth cribbing for any PGx × persistence design in the same
disease-drug matrix.

**HIGH — Prokunina-Olsson, Florez-Vargas, Levin, et al.**
*Multi-population GWAS meta-analysis identifies bladder cancer
susceptibility loci and highlights genetic regulation of smoking-
related risk.* Nature Communications, 2026. **Thread: Genetic
epidemiology + cross-ancestry portability + Zeng self-feed.**
Multi-population meta-analysis with 32,470 individuals with bladder
cancer, highlighting genetic regulation of *smoking-related risk* —
which is the interesting angle because it moves from
main-effect GWAS to gene-by-environment for the strongest bladder-
cancer risk factor. Landed via your own Google Scholar feed
(citations tracker), so it is either citing your work or a related
Zeng-lineage paper. Read in full both for the cross-ancestry
architecture and for the smoking-interaction methodology (which
should port cleanly to lung and other tobacco-attributable cancers).

**HIGH — Lu, Xu, Shi, Engelmann, Tran, Wei, et al.** *Germline
genetic risk and prostate cancer–specific mortality in a
population-based incident cohort.* Prostate Cancer and Prostatic
Diseases, 2026. **Thread: Genetic epidemiology + hereditary cancer
+ biobank.** Evaluates germline PRS + reported germline risk against
prostate-cancer-specific mortality in n=14,644 UKB incident cases —
i.e., mortality among cases (harder and more clinically actionable
endpoint) rather than incidence. This is the "germline risk for
lethality, not just diagnosis" framing that turns PRS-of-diagnosis
into PRS-of-lethal-disease, portable to breast and colorectal
lineages you already work in.

**HIGH — Poudel, Susztak; Hu, Liu, Zhou.** *Response by Poudel and
Susztak to Letter Regarding Article "Cell-Specific Inducible Human
APOL1 Risk Variant Expression in Mice Causes Hypertension and Renal
Damage".* Circulation, 2026 (response + originating letter, both in
same alert). **Thread: APOL1.** Reaffirms podocyte-specific APOL1
expression as the dominant renal-phenotype driver and defines the
causal pathway from APOL1 risk variant → hypertension. Hu et al.'s
letter flags effect modification by comorbid conditions as the next
question. This is mechanism confirmation more than new discovery, but
combined with the 08-08 Chen JASN N264K modifier and Gaheer/Lanktree
proteomic-risk-score cluster, keeps the APOL1 arc coherent —
mechanism (Susztak podocyte), modifier genetics (Chen N264K),
biomarker (Gaheer proteomic score), therapy (Kim inaxaplin +
Papasavva β-hemoglobinopathy extension). This is now a full
precision-medicine disease story you can cite as a template for
similar single-gene high-penetrance conditions.

**HIGH — Papasavva, Dosunmu-Ogunbi, Oni, et al.** *Modifying quality
and equity of care: emerging roles of genetic disease modifiers in
β-hemoglobinopathies.* Blood Advances, 2026. **Thread: APOL1 (via
inaxaplin therapy extension) + variant interpretation.** Genetic
disease modifiers in β-hemoglobinopathies, with the notable APOL1-
adjacent point that inaxaplin is under clinical evaluation in
individuals with high-risk APOL1 genotypes *and* sickle-cell-
associated disease. This is the drug crossing over from one indication
(APOL1-FSGS) to another (sickle cell + APOL1) — a small but
significant expansion of the inaxaplin story that widens the
population impact estimate whenever you write about APOL1-targeted
therapy.

**HIGH — Cruz-Gonzalez, Okpala, Gu, Gomez, Mews, et al.** *Methylation
clocks fail to generalize across genetically admixed individuals.*
eLife, 2026 (via John Capra author feed). **Thread: Foundation-model
fairness / calibration audits + ancestry-stratified risk.** Direct
audit of epigenetic aging clocks (Horvath, Hannum, PhenoAge, GrimAge
lineage) in genetically admixed cohorts, documenting systematic
generalization failure. Directly parallels the calibration-under-
site-shift and calibration-under-ancestry-shift concerns your EHR-FM
and PRS-portability threads already carry, and provides an
epigenetics-side reference for "the model fits well in the
discovery ancestry and breaks elsewhere" as a phenotype. Portable
audit template for methylation-clock work in AoU (which has
substantial admixed populations by design).

**HIGH — Okazawa-Sakai, Fujisawa, Chiyoda, Yagi, et al.**
*cfDNA-inferred putative clonal hematopoiesis during first-line
platinum-to-PARP inhibitor maintenance in ovarian cancer.* Journal of
Gynecologic Oncology, 2026. **Thread: Clonal hematopoiesis + solid
tumor + therapy-induced CH.** Detects putative CH signals from cfDNA
residuals during platinum → PARP maintenance in ovarian cancer. This
is the *therapy-induced CH from routine tumor cfDNA* pattern — the
sample already exists in nearly every modern solid-tumor pipeline,
you just have to look for the CH signal. Portable template to any
solid-tumor cohort with cfDNA panel data, and complements the
Bandreddi longitudinal CHIP-VAF paper: Okazawa-Sakai gives you the
signal, Bandreddi gives you the model to fit it.

**METHODS-WATCH — Wang, Wu, Zhu, Kang, Feng, Wu, Cheng.** *Scalable
penalized regression boosts accuracy and computational efficiency for
single-and cross-ancestry polygenic prediction.* Research Square
rs-10235713, 2026 (via Jian Yang related-research). **Thread:
Genetic epi — PGS methods, cross-ancestry portability.** Addresses
the trade-off between adaptive SNP shrinkage and computational
efficiency in cross-ancestry PGS. Not a discovery paper but a methods
paper for the PGS-portability pipeline; adopt if you're building
cross-ancestry PGS in AoU / UKB pipelines.

**METHODS-WATCH — Song, Wang, Du, Buckner, Lin.** *Synthetic
phenotype-assisted analysis enhances rare variant association
discovery in biobank-scale WGS studies with missing phenotypes.*
Openreview LobqYjqXEb, 2026. **Thread: PheWAS + rare-variant methods
+ EHR phenotyping.** Uses synthetic (imputed) phenotypes to boost RV
association power under missing-phenotype conditions — the exact
problem AoU / UKB analyses hit when the outcome depends on a
selectively-ordered lab. Portable to your rare-variant × phecode
analyses; complements the Foulkes et al. IPW-for-auxiliary-variable-
dependent-sampling paper from the 08-08 report.

**METHODS-WATCH — Shen, Dupuis, Zhang.** *Multi-ancestry
colocalization approaches.* PLoS Genetics, 2026 (via Jian Yang
feed). **Thread: Genetic epi — cross-ancestry fine-mapping.**
Methods survey for multi-ancestry colocalization; useful reference
when the next cross-ancestry GWAS + eQTL colocalization comes up in
your pipeline (which is often).

**METHODS-WATCH — Qasim, Wang, Bhatt.** *Adaptive Penalization and
Bootstrap-Smoothed Inference for Two-Sample Mendelian Randomization
with Summary Data.* arXiv 2607.18503, 2026. **Thread: Genetic epi —
MR methodology.** Addresses horizontal pleiotropy invalidation of
standard MR estimators via adaptive penalization + bootstrap
smoothing. Adopt-when-relevant reference for the drug-target MR
sub-thread; complements the Saxby MR-ALasso lineage already logged.

**MEDIUM — Rujchanarong, Fujii.** *Identifying metabolic factors
associated with the incidence of brain metastasis in breast cancer
using All of Us Research Program data.* Neuro-Oncology Advances,
2026 (conference abstract). **Thread: AoU + Zeng breast-cancer
lineage.** Small abstract but direct hit on breast-cancer + AoU
combination; abstract-only for now.

**MEDIUM — Son, Hwang, Lee, Kim.** *Safety and Efficacy of GLP-1
Receptor Agonists in Adults With Epilepsy, Obesity, and Type 2
Diabetes.* Annals of Clinical and Translational Neurology, 2026.
**Thread: AoU + pharmacoepi (GLP-1 RA).** New-user cohort in AoU
comparing GLP-1 RA initiators to matched non-initiators in a
comorbid-epilepsy-T2D-obesity population. Small niche but
directly extends the GLP-1 pharmacoepi thread into a new
comorbidity slice.

**MEDIUM — Aditi, Blackwell, Fang, Sharma, Mendoza, et al.**
*Long-term risk of dementia following encephalitis: a large-scale
retrospective cohort study of electronic health records.* Journal
of Neurology, 2026. **Thread: EHR phenotyping — long-term outcomes.**
Retrospective EHR cohort estimating long-term dementia risk
following encephalitis. Standard-format EHR outcomes study but
useful reference for EHR long-term-follow-up design when the
exposure is a discrete hospitalization event.

**MEDIUM — Rayens, Skela, Ackerson, Pomichowski, et al.**
*Identification of invasive aspergillosis in electronic health
records.* Open Forum Infectious Diseases, 2026. **Thread: EHR
phenotyping — computable phenotype definition.** Phenotype algorithm
for invasive aspergillosis in EHR data. Not on your active disease
threads but a canonical phenotype-development paper worth noting
for anyone building similar computable phenotypes for uncommon
infections.

**MEDIUM — Pellesi, Guerzoni.** *Medication-overuse headache in
migraine: could GLP-1 receptor agonists treat the addiction-like
phenotype?* Expert Opinion on Pharmacotherapy, 2026. **Thread:
Pharmacoepi — GLP-1 RA lineage + AoU.** Referenced nested case-
control of ~142k adults from AoU showing GLP-1 RA exposure
associated with lower SUD odds. This is the *GLP-1 → substance use*
observational signal, which is a rising secondary indication for
GLP-1 RAs and worth tagging on the pharmacoepi watchlist.

**METHODS-WATCH — Lu, Chen, Treggiari, Blessing, Zhuo, Weng, et al.**
*Toward Automated Detection of Documentation Inconsistencies in
Electronic Health Records.* arXiv 2607.22954, 2026. **Thread: EHR
knowledge representation + NLP-derived representations.** LLM-based
detection of internal documentation inconsistencies in discharge
summaries, with recurring failure-mode analysis. Directly relevant
to the *NLP-derived representations from clinical notes*
sub-thread; useful pattern for QC on any note-derived phenotype
extraction pipeline.

**METHODS-WATCH — Zhu, Wang, Gu, Sui, Wang, Harrison, Fu.** *OneEHR:
Reproducible and AI Agent-Ready Longitudinal EHR Analysis Toolkit.*
Proceedings of the 32nd ACM SIGKDD Conference, 2026. **Thread: EHR
FMs + reproducibility.** Toolkit for reproducible longitudinal EHR
analyses aimed at agent-based workflows. Worth watching if your
EHR-FM work moves toward agentized analysis pipelines.

**METHODS-WATCH — Chen, Li, Zhang, Wang.** *HazardFlow: Enhancing
Health Status Representations via Score-based Energy Modeling.*
Proceedings of the 32nd ACM SIGKDD Conference, 2026. **Thread: EHR
FMs.** Score-based energy-modeling approach for EHR-derived health-
status representations — an unusual generative-modeling angle
distinct from the tokenized-event lineage.

**SKIP — Numerous items across alerts, per the SKIP rubric.** Cattle
belted-phenotype CNV (Kai Wang related); LLaDA MoE v2 (generic LLM);
string2string Studio (generic NLP tooling); Debaryomyces innate
immune signaling (mouse gut); RNF186 UC negative association Korean
cohort (single-locus null); UNet rice stem phenotyping (agriculture);
Xu discriminative LM (generic); protocadherin bipolar-cell mouse
retina (developmental neuro); CDC42 M45L / T43I inflammasome pair
(mechanism, not phenotype-thread relevant); Ebola vaccine nanoparticle
(vaccine); polyimide polymer property prediction (materials);
prostate PGCC case report; ADCs mCRPC (therapy review); Naehrig
CFTR bilirubin case series (small n, off-target for
modulator-eligibility framing); Query2Box (older Leskovec paper);
Bender AI drug discovery review (multi-citations, generic); Villa
AI oncology trials (review); DILI KG (drug-safety KG but not on
active drug-repurposing lineage); FedMed medication recommendation
(federated but not on causal / phenotyping axis); ARMD-UTSW
antimicrobial dataset (useful data resource but off-thread);
Machado explainable ML clinical diagnosis (generic); homeopathy
autoimmune review (skip).

---

## Cross-window continuity notes

- **Structural-variant PheWAS (KGGSV)** is a *new* infrastructure
  entry in the PheWAS thread; add to the PheWAS-methods reading list
  and consider retrofitting the next SV-aware analysis you propose.
- **APOL1** continues to accumulate story-completion (mechanism →
  modifier → biomarker → therapy) across consecutive windows;
  INTERESTS.md APOL1 entry should be updated to reflect the mature
  precision-medicine framing rather than the earlier
  "high-risk-genotype-in-CKD" framing.
- **EHR-FM translational + federated** entries (Jiang + Burkhart)
  jointly move the EHR-FM sub-thread from
  "here are new architectures" to "here is what deployment and
  cross-site transfer actually require" — worth a reading pair.
- **GLP-1 RA cluster** now spans trial (Mann pooled), observational
  drug-class comparison (Krüger BMJ), pharmacoepi (Yu insulin
  initiation), and secondary-indication signal (Pellesi migraine +
  Son epilepsy) in one window; this is the density that argues for
  a standing pharmacoepi tracking sheet if you don't already have
  one.
- **Multi-omics × PGS** (Dutta cancer PRS × plasma proteomics)
  strengthens the composite-risk framing; the FNIP1 Nature paper is
  a complementary rare-variant-side finding that should sit in the
  same reading batch.
- **Methylation clocks fail across admixed** (Cruz-Gonzalez eLife)
  provides an epigenetics-side companion to the ongoing
  PGS-portability and EHR-FM-calibration threads — useful when you
  need a fairness-audit example outside the PRS/PheWAS canon.

## Suggested reads (in priority order)

1. Jiang et al. — Translating EHR FMs into Clinical Decision Support
   (framing paper, will sharpen your EHR-FM vocabulary).
2. Li et al. — KGGSV scalable SV-PheWAS (missing modality now
   pluggable into your PheWAS thinking).
3. Dutta et al. Cell Genomics — PRS × plasma proteomics across 21
   cancers (multi-omics-augmented PRS reference).
4. Mann et al. Lancet D&E — SELECT+FLOW+SOUL semaglutide kidney
   pooled analysis (trial anchor for GLP-1 kidney observational
   signals).
5. Prokunina-Olsson et al. Nature Communications — multi-population
   bladder cancer GWAS with smoking GxE (Zeng-lineage adjacency).
6. Vossler et al. arXiv 2608.10339 — egg-computation LLM-assisted
   g-computation (agentic-causal sub-thread).
7. Burkhart et al. arXiv 2608.02939 — federated GEMs on tokenized
   EHR (federated / privacy-preserving sub-thread).
8. Bandreddi et al. arXiv 2608.09725 — Tobit vs hurdle for CHIP VAF
   longitudinal (portable to LOY).
9. Sulaiman & Oyeyemi — ClinGen concordance ACMG benchmark
   (variant-interpretation audit reference).
10. Cruz-Gonzalez et al. eLife — methylation clocks fail across
    admixed (fairness / portability audit template).
