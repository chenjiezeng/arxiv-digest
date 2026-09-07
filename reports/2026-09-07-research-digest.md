# Research digest report — 2026-09-07

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-07 13:00Z** (~6 days since
`reports/2026-09-01-research-digest.md`, covering six arxiv-digest cron
runs and three Google Scholar alert batches plus rolling NCBI /
bioRxiv-medRxiv feeds).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-06.md`) | 09-01 → 09-06 daily crons | 6 daily runs. Dry days (0 papers): 09-03, 09-05, 09-06 (suppressed already-seen). Content days: 09-01 (1 paper: Ghiasi storage-centric metagenomics — off-thread, `precision medicine` keyword hit only), 09-02 (1 paper: mudskipper tail thrusting — off-thread, `motor` keyword hit only), 09-04 (2 papers: Cortez-Rodriguez natural-disasters × nonprofit panel-DML, Yu et al. location-invariant extremal QTE via IPW). Highest-scoring hit: score 1 across the board — a low-yield arXiv week for the tracked threads. |
| No `arxiv-digest` email hits from GitHub | — | Same as prior window: `from:notifications@github.com` × `arxiv-digest` returned zero threads. The pipeline commits to this repo; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-06 batch, 06:02Z + 13:58Z) | 09-06 06:02Z + 13:58Z | The densest batch of the window: ~30 author + keyword feeds fired across two waves. Author-feed wave (06:02Z) landed the two headline items — **Bal et al. multiancestry HCM-PRS in Nat Cardiovasc Res** (Denny feed) and **Kadesjö et al. SGLT2i-ketoacidosis Scandinavian cohort in Lancet Diabetes Endocrinol** (Ryan feed). Keyword-feed wave (13:58Z) added the **Pearson-group T2D drug-response paper (Garg et al., Diabetes Obes Metab)** and the **Perée et al. Nat Commun IBD-eQTL entrectinib repurposing** (already prominent in the Pritchard + Montgomery + Hripcsak feeds). |
| Google Scholar alerts (09-04 batch, 16:08Z + 21:26Z) | 09-04 16:08Z + 21:26Z | Two waves: 16:08Z author-feed batch (~24 feeds) — Hripcsak citations delivered **Zhou et al. Nature Cardiovasc Res: long-term cardiorenal trajectories after antihypertensive initiation in ADHD adults**, Bastarache "new articles" delivered **Chin et al. J Human Immunity: temporal windowing of recurrent sinusitis for EHR-based immunodeficiency classification**, and four separate feeds (Karczewski, Denny, Bastarache-related, Chenjie Zeng) all led with **Park et al. Translational Psychiatry: cross-ancestry × cross-disorder PRS transferability for OCD**. 21:26Z keyword-feed batch added APOL1 transplant P4.810 case and mostly review-heavy items. |
| Google Scholar (mid-window: 09-02 → 09-03) | Sparse | Small trickle only; no HIGH items above what the 09-04 and 09-06 batches surfaced. |
| NCBI "My NCBI What's New" (AoU / UKB / drug repurposing) | 09-03, 09-04, 09-05, 09-06 | Four daily batches per topic (12 in-window). AoU and UKB volumes ordinary; drug-repurposing steady with mostly review-tier hits. Densest hits captured through the Scholar-alert cross-references. |
| bioRxiv / medRxiv Subject Collection Alerts | daily (09-03 → 09-07) | Aggregate feeds, metadata-only. Same caveat as prior reports; not individually itemized below unless promoted through a keyword feed. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and only
> the first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated to first
> 3–5 as they appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced this window, clustering into six knots:

**Denny-lineage AoU/BioVU composite-PRS cluster (2 items).** Bal,
Pampana, Nayak, Gaonkar, Patel et al. — *A multiancestry polygenic
risk score improves stratification in patients with hypertrophic
cardiomyopathy* (**Nature Cardiovascular Research** 2026, Denny feed).
HCM is historically framed as Mendelian, but sarcomere P/LP variants
(SARC-HCM-P/LP) explain only ~1/3 of cases; the paper formalizes PRS
addition to the P/LP-only framework across ancestries and shows
incremental stratification — a direct-hit for `PheWAS / phecode
infrastructure` (penetrance under population-screening) AND for the
`Composite risk models stacking PRS with rare pathogenic variants`
sub-thread of `Genetic epidemiology`. DePaolo, Smelser, Guo,
Abramowitz, Sisti et al. — *Thoracic aortic disease: prognostic role
of gene variants and polygenic risk scores* (**European Heart Journal**
2026, Bastarache feed). Prognostic model combining rare variants in 11
HTAAD genes with a TAAD-PRS in a Geisinger MyCode + external cohort;
same composite-risk template as the HCM paper, transposed to a
different Mendelian-vs-common-genetic-risk architecture. Together
these two are the strongest signal this window that the composite-risk
framing is consolidating into first-line cardiovascular-genomics
practice.

**Pharmacoepi / target-trial-emulation cluster (3 items).** Kadesjö,
Söderling, Hviid, Wintzell et al. — *Ketoacidosis with SGLT2
inhibitors in routine clinical practice of type 2 diabetes:
Scandinavian cohort and nested case–control study* (**Lancet Diabetes
& Endocrinology** 2026, Patrick Ryan feed). Nationwide-registers
design assessing SGLT2i-DKA incidence, risk factors, and prognosis;
directly serves the SGLT2 drug thread AND is a Scandinavian-register
TTE-adjacent template your INTERESTS.md prioritizes. Zhou, Postmus,
Li, van Lammeren et al. — *Long-term cardiorenal illness trajectories
after initiation of antihypertensive medications in adults with and
without ADHD: a nationwide cohort study* (**Nature Cardiovascular
Research** 2026, Hripcsak citations feed). ADHD × antihypertensive
persistence is exactly the intersection the
`pharmacogenomic-modifier-of-medication-persistence` sub-thread flags,
and the trajectory framing threads through the multimorbidity thread;
methodologically it's a well-powered nationwide-cohort TTE that
handles the immortal-time / channeling confounders characteristic of
the space. Heudel, Blay — *Primary care physician documentation in
oncology electronic health records: prognostic marker or immortal-time
bias?* (**ESMO Real World Data and Digital Oncology** 2026, Hernán
citations feed). Retrospective French cohort testing whether dated
PCP documentation predicts survival after accounting for documentation
timing — an on-brand `causal inference and pharmacoepidemiology`
methods paper for immortal-time-bias-in-EHR that will be portable
across any dated-observation exposure definition (medication start
dates included).

**Drug-target-QTL × drug-repurposing cluster (2 items).** Perée,
Petrov, Tokunaga, Kvasz, Farnir et al. — *Cell-type specific analyses
in blood and gut identify cis-eQTL matching 140 IBD risk loci and
entrectinib as repurposing candidate* (**Nature Communications** 2026;
appeared this window in Pritchard, Montgomery, and Hripcsak feeds).
cis-eQTL in 27 sorted blood populations + 43 intestinal cell types
(scRNA-seq of ileum/colon/rectum), >95K cis-eQTL, >13K e-genes, and
entrectinib flagged as an IBD repurposing candidate through the
eQTL-drug link. Direct-hit for `Drug repurposing` (the paper is a
canonical *EHR-agnostic* cell-type-eQTL-to-drug pipeline that the
computational-repurposing thread prioritizes) AND for the IBD sub-
thread of `Specific disease threads`. Nguyen, Jeejan, Iwasaki, Kales,
Chakraborty et al. — *Germline noncoding risk variants influence
clonal hematopoiesis via hematopoietic enhancer activity* (**Blood
Cancer Discovery** 2026, `intitle:clonal hematopoiesis` feed).
MSI2 upregulation in Tet2+/- HSPCs as a model of early CH; the paper
establishes noncoding-germline → enhancer → CH-driver-expression
mechanism, which is the mechanistic complement to the CH-epidemiology
work the CHIP thread already tracks. Both fit
`Cross-trait shared genetic architecture and multi-trait
triangulation` and support the `variant interpretation → clinical
translation` translation pattern.

**Cross-ancestry / cross-disorder PGS portability cluster (2 items).**
Park, Kim, Myung, Jung, Kim, Park et al. — *Cross-ancestry and
cross-disorder transferability of polygenic risk scores for
obsessive-compulsive disorder* (**Translational Psychiatry** 2026;
surfaced simultaneously across the Karczewski, Denny, Bastarache-
related, and Chenjie Zeng feeds on 09-04). The four-feed
simultaneous surfacing is a strong salience signal; the paper is a
direct-hit for `Genetic epidemiology → cross / trans-ancestry
portability` and for the `GxE and PGS × exposure` framing since the
cross-*disorder* axis is a shared-architecture reframing of PGS
portability. Garg, Kitchen, Gupta, Donnelly, Pearson — *Genetic and
Clinical Determinants of Variation in Drug Response in Type 2 Diabetes:
Insights From the Scottish and UK Biobank Cohorts* (**Diabetes,
Obesity & Metabolism** 2026, `UK Biobank` feed). Partitioned PRS
(pPRS) quantifying genetic vs clinical contribution to T2D treatment
response; direct-hit for `pharmacogenomic-modifier-of-medication-
persistence` (transposed onto T2D-first-line-drug response rather
than persistence) AND for the `Biobanks with EHR linkage` thread
(Scottish clinical cohort + UKB replication is the multi-cohort
pattern the thread prioritizes). Together with the Bal HCM-PRS paper
these three are the biggest PGS-methodology signals of the window.

**EHR phenotyping & OMOP cluster (2 items).** Chin, Mester, Tozzo,
Stephens et al. — *Temporal windowing of recurrent sinusitis improves
EHR-based immunodeficiency classification* (**Journal of Human
Immunity** 2026, Bastarache "new articles" feed). Recurrent-
sinopulmonary phenotype refinement with explicit temporal-window
handling — this is the class of `Structural and temporal
representation of the patient timeline` methodology paper from your
`Knowledge representation in EHRs and applications` thread, and it
inherits the auditable-phenotyping methodology from the Bastarache
lineage (ACT / PheKB). Priya, Yan, Wangensteen, Wu, Luehrs et al. —
*Subtyping metabolic dysfunction-associated steatotic liver disease
using electronic health record-linked genomic cohorts reveals diverse
etiologies and progression* (**Nature Communications** 2026,
Bastarache citations feed). Latent-class analysis identifies 5 MASLD
subgroups replicated across two EHR-linked cohorts, with PRS + rare
variant analysis showing subgroup-specific genetic drivers. Direct-
hit for `Chronic disease clustering and multimorbidity` (LCA on
diagnosis + lab trajectories) AND for `Biobanks with EHR linkage`.

**Rare-disease diagnostic + wearable-phenotyping bonus (1 item).**
Boceck, Laugwitz, Sturm, Bezdan, Gschwind et al. — *aiDIVA — hybrid
AI for rare disease diagnostics using evidence-based, machine
learning and language models* (**npj Genomic Medicine** 2026; appeared
in Montgomery, Kai Wang, and Szolovits feeds simultaneously on 09-04).
Hybrid rules-plus-LM classifier for rare-variant prioritization; a
direct auditable-benchmarks-for-rare-disease item that pairs with
the GraphRareBench (Guo et al. 2607.24878) reference in your
`Auditable HPO-driven diagnostic benchmarks with separable metrics
for ranking vs evidence coverage` sub-thread.

---

## METHODS-WATCH bench

Papers that are exemplary methods but off-thread on disease/context;
worth cribbing:

- **Yu, Huang, Liu, Tang, Wang, Zhang, Zhao** — *A location-invariant
  estimator of extremal quantile treatment effects for heavy-tailed
  distributions* (arXiv 2609.04018, in `digests/2026-09-04.md`,
  score 1 on `propensity score`). IPW-based causal EVI estimator with
  a difference-based extrapolation that cancels the location parameter;
  portable to any TTE where the QTE tail matters (medication-cost
  distributions, hospital-stay length, PheRS-tail penetrance).
- **Cortez-Rodriguez** — *Natural Disasters and the Nonprofit Sector*
  (arXiv 2609.04136, in `digests/2026-09-04.md`, score 1 on
  `causal inference`). Panel-DML applied to 1991–2021 county-level
  data; the panel-DML template stays useful for any longitudinal-
  county-level exposure design.
- **DeVito, Gymrek** — *Modeling nonlinear and interaction effects of
  spatiotemporal and nongenetic factors improves prediction for
  complex traits* (**Nature Communications** 2026, Jian Yang related
  feed). GxE-style prediction that argues nonlinear + interaction
  spatiotemporal-and-nongenetic factors add measurable prediction
  gains — dovetails with the `PGS × exposure / environment
  interactions` sub-thread of `Genetic epidemiology`.
- **Fang, Jin, Tian, He, Geer, Naffakh et al.** — *Towards AI-Assisted
  Clinical Trial Matching: Practical Considerations, Multicenter
  Evaluation, and Real-World Deployment* (arXiv 2609.01202, Zhiyong
  Lu feed). Multicenter-deployment case study for LLM trial
  matching; useful reference for how LLM-based trial-matching
  workflows survive real-world site heterogeneity.
- **Jiang, Dai, Zhang, Gao, Chen, Du, Liu et al.** — *Translating
  Electronic Health Record Foundation Models into Clinical Decision
  Support* (Preprints 2026, Hripcsak related feed). Re-surfaces from
  the 08-28 Pascal Brandt cluster — sparsity handling for EHR-FM →
  CDS translation.
- **Wang, Wang, Yin** — *GWAS-by-Subtraction Resolves Coronary Artery
  Disease-Related and Model-Defined Residual Genetic Components of
  Ischaemic Stroke* (**Genes** 2026, Jian Yang related feed).
  Cholesky-modelling on GIGASTROKE + UKB/CARDIoGRAMplusC4D; a shared-
  architecture cross-trait pattern relevant to the `MiXeR /
  conditional-FDR` sub-thread.
- **Bai, Gao, Zhang, Yue, Qiao, Feng** — *Relation-aware multimodal
  knowledge graph learning for drug–drug interaction prediction*
  (**Scientific Reports** 2026, `knowledge graph` feed). Explainable
  KG-for-DDI is on-brand for the `Drug repurposing` thread's
  auditable-KG sub-preference.
- **Todorovic** — *Integrating real-world Patient Reported Outcomes
  into the OMOP common data model* (Hripcsak citations feed). PRO-
  extension to OMOP CDM; direct methods paper for `EHR phenotyping &
  OMOP`.

---

## Detailed study reports (HIGH items only)

### 1. Bal, Pampana, Nayak, Gaonkar, Patel et al. — *A multiancestry PRS improves stratification in patients with hypertrophic cardiomyopathy* (Nature Cardiovascular Research, 2026)

**Feed:** Joshua C. Denny — new related research (Scholar, 09-06 06:02Z).

**Why HIGH:** Explicit multiancestry PRS on top of SARC-HCM-P/LP —
the paradigmatic composite-risk-model architecture your INTERESTS.md
`Composite risk models stacking PRS with rare pathogenic variants`
sub-thread names. Sarcomere P/LP variants explain only ~1/3 of HCM
cases; the paper quantifies the incremental stratification value of
PRS across ancestries in the remaining variance. Also directly
serves the PheWAS-infrastructure thread's `penetrance estimation for
monogenic variants under population-screening conditions` framing —
HCM is one of the ACMG SF genes for which population-screening
penetrance is the open question.

**Actions to consider (self-note):** Look for whether the PRS was
derived in ancestry-stratified GWAS or single-population summary
stats + PRS-CSx-style transfer; the multiancestry framing implies
the former or a portability audit. Cross-reference against the
Bastarache TAAD-PRS paper (item 2) for a shared architecture in
cardiovascular Mendelian-plus-common composite risk.

---

### 2. DePaolo, Smelser, Guo, Abramowitz, Sisti et al. — *Thoracic aortic disease: prognostic role of gene variants and polygenic risk scores* (European Heart Journal, 2026)

**Feed:** Lisa Bastarache — new related research (Scholar, 09-06 06:02Z).

**Why HIGH:** Same composite-risk architecture as the Bal HCM paper,
transposed to TAAD. 11 HTAAD genes on top of TAAD-PRS in an
EHR-linked cohort (Geisinger MyCode + external replication implied
by the venue). Direct-hit for `Genetic epidemiology → Composite risk
models`, `PheWAS / phecode infrastructure`, and `Biobanks with EHR
linkage`. This pair (item 1 + item 2) is the strongest single-window
signal that composite Mendelian-plus-common risk is consolidating
as cardiovascular-genomics standard.

**Actions to consider (self-note):** Fits a broader emerging "P/LP
plus PRS plus clinical" three-way risk stack; worth building a
mini-review pattern-match across HCM, TAAD, DCM, LQTS in the next
digest window.

---

### 3. Kadesjö, Söderling, Hviid, Wintzell et al. — *Ketoacidosis with SGLT2 inhibitors in routine clinical practice of type 2 diabetes: Scandinavian cohort and nested case–control study* (Lancet Diabetes & Endocrinology, 2026)

**Feed:** Patrick Ryan — new related research (Scholar, 09-06 06:02Z).

**Why HIGH:** Direct-hit for the SGLT2i drug thread AND the
`pharmacoepidemiology` thread. Nationwide Scandinavian registers +
nested case-control is the design pattern the pharmacoepi thread
prioritizes for rare-adverse-outcome causal inference (DKA under
SGLT2i has an incidence rate of ~1–3 per 1000 person-years, so
nested case-control gets exposure resolution the full cohort can't
efficiently). Ketoacidosis is the on-label boxed-warning outcome, so
this is the class-effect epidemiology paper that the thread has been
waiting for as a companion to the Wästerlid Lancet Haematol
survivorship reference (08-31 batch, prior report).

**Actions to consider (self-note):** Watch whether the paper uses
active-comparator design (SGLT2i vs DPP4i is the standard) or
prevalent-user; the nested case-control specification will drive
whether it substitutes for or complements a TTE reanalysis.

---

### 4. Zhou, Postmus, Li, van Lammeren et al. — *Long-term cardiorenal illness trajectories after initiation of antihypertensive medications in adults with and without ADHD: a nationwide cohort study* (Nature Cardiovascular Research, 2026)

**Feed:** George Hripcsak — 5 new citations (Scholar, 09-04 16:08Z).

**Why HIGH:** Cardiorenal trajectory analysis stratified by ADHD is
the intersection of `Causal inference and pharmacoepidemiology` and
the `pharmacogenomic-modifier-of-medication-persistence` sub-thread
(ADHD-medication-adherence interaction with antihypertensives is
the well-documented confounder). Also serves `Chronic disease
clustering and multimorbidity` via the trajectory framing.
Nationwide-cohort framing is the sample-size regime that lets you
resolve trajectory-heterogeneity by comorbidity.

**Actions to consider (self-note):** Compare method against Kadesjö
Scandinavian design (item 3) — both are Nordic-register nationwide
cohorts, so combined they define this window's pharmacoepi backbone.

---

### 5. Heudel, Blay — *Primary care physician documentation in oncology electronic health records: prognostic marker or immortal-time bias?* (ESMO Real World Data and Digital Oncology, 2026)

**Feed:** Miguel Hernán — 10 new citations (Scholar, 09-06 06:02Z).

**Why HIGH:** Immortal-time-bias-in-EHR is a foundational
methods-audit topic your `Causal inference and pharmacoepidemiology`
thread cares about; the paper is a direct empirical audit of whether
PCP-documentation-timing survives an immortal-time adjustment. The
methodological principle generalizes to any dated-observation
exposure (medication-start dates, test-order dates, referral dates
— all common EHR-derived exposures in TTE work).

**Actions to consider (self-note):** Portable QC template for any
`documentation-of-X predicts survival` claim in an EHR-based
observational study.

---

### 6. Perée, Petrov, Tokunaga, Kvasz, Farnir et al. — *Cell-type specific analyses in blood and gut identify cis-eQTL matching 140 IBD risk loci and entrectinib as repurposing candidate* (Nature Communications, 2026)

**Feeds:** Jonathan K Pritchard (10 new citations), Stephen B
Montgomery (new related), George Hripcsak (10 new citations) —
Scholar, 09-06 06:02Z (multi-feed).

**Why HIGH:** Triple-feed surfacing is a strong salience signal.
Direct-hit for `Drug repurposing` (this is the eQTL-to-drug pipeline
the thread's "explainable knowledge-graph / GNN approaches with path
or subgraph rationales" preference approximates in the cell-type-
eQTL idiom — the `path` here is `variant → eQTL cell type → gene →
drug target`). Also directly serves the IBD sub-thread of
`Specific disease threads` and the `Cell-type specific eQTLs` genetics
literature. Entrectinib was originally an NTRK/ROS1 inhibitor —
IBD repurposing is a genuine novel indication if the eQTL evidence
holds up.

**Actions to consider (self-note):** Cross-check entrectinib safety
profile against IBD immune-modulator baseline (kinase-inhibitor
class effects on infection risk are the main concern); this is the
kind of hypothesis where a downstream EHR-based repurposing signal
audit (target-trial emulation of off-label use, or a
prescribing-outcome mining pass) would be the natural next
question.

---

### 7. Nguyen, Jeejan, Iwasaki, Kales, Chakraborty et al. — *Germline noncoding risk variants influence clonal hematopoiesis via hematopoietic enhancer activity* (Blood Cancer Discovery, 2026)

**Feed:** `intitle:"clonal hematopoiesis"` — new results (Scholar, 09-06 13:58Z).

**Why HIGH:** Direct-hit for the CHIP/VEXAS/LOY sub-thread of
`Specific disease threads`. Mechanistic complement to the CH
epidemiology work: establishes that germline noncoding variants
influence CH through enhancer activity (MSI2 upregulation in
Tet2+/- HSPCs as the model). The `noncoding → enhancer → CH-driver`
pattern is the methodology template that would be portable to
mosaic-LOY too (the `LOY analogue of CHIP` sub-thread), even though
the paper is CHIP-specific.

---

### 8. Park, Kim, Myung, Jung, Kim, Park et al. — *Cross-ancestry and cross-disorder transferability of polygenic risk scores for obsessive-compulsive disorder* (Translational Psychiatry, 2026)

**Feeds:** Konrad Karczewski (new related), Joshua C. Denny (new
related), Lisa Bastarache (new related), Chenjie Zeng (new related)
— Scholar, 09-04 16:08Z (four-feed surfacing).

**Why HIGH:** The four-feed simultaneous surfacing (including your
own author feed) is a strong salience signal. Direct-hit for
`Genetic epidemiology → cross / trans-ancestry portability` and for
the `GxE and PGS × exposure` framing — the cross-*disorder* axis
tests whether shared genetic architecture across psychiatric
phenotypes translates to portable PRS, which is the shared-
architecture reframing of PGS portability that the
`Cross-trait shared genetic architecture and multi-trait
triangulation` sub-thread prioritizes.

---

### 9. Garg, Kitchen, Gupta, Donnelly, Pearson — *Genetic and Clinical Determinants of Variation in Drug Response in Type 2 Diabetes: Insights From the Scottish and UK Biobank Cohorts* (Diabetes, Obesity & Metabolism, 2026)

**Feed:** `"UK Biobank"` — new results (Scholar, 09-06 13:58Z).

**Why HIGH:** Partitioned PRS (pPRS) quantifying genetic vs clinical
contribution to T2D treatment response — a methodology paper for
`pharmacogenomic-modifier-of-medication-response` (sibling of the
`persistence` sub-thread) on a Pearson-group T2D cohort with UKB
replication. Directly serves the `Biobanks with EHR linkage` thread
(Scottish cohort + UKB = the multi-cohort-EHR-linked pattern) AND
the `Causal inference and pharmacoepidemiology` thread (the GLP-1
RA / SGLT2i / DPP-4i drug-class threads all live in the same T2D
first/second-line-drug space).

**Actions to consider (self-note):** Cross-check whether the pPRS
methodology used here is portable to the CFTR-modulator persistence
and HRT persistence sub-threads.

---

### 10. Chin, Mester, Tozzo, Stephens et al. — *Temporal windowing of recurrent sinusitis improves EHR-based immunodeficiency classification* (Journal of Human Immunity, 2026)

**Feed:** Lisa Bastarache — new articles (Scholar, 09-04 16:08Z).

**Why HIGH:** Direct methods paper for `EHR phenotyping & OMOP` and
for the `Structural and temporal representation of the patient
timeline` sub-thread of `Knowledge representation in EHRs and
applications`. Recurrent-sinopulmonary phenotype refinement with
explicit temporal-window handling; inherits the auditable-phenotyping
methodology from the Bastarache lineage (ACT / PheKB / PheValuator).
Immunodeficiency classification is also a rare-disease phenotyping
task, which threads to the `Rare disease` thread.

---

### 11. Priya, Yan, Wangensteen, Wu, Luehrs et al. — *Subtyping metabolic dysfunction-associated steatotic liver disease using electronic health record-linked genomic cohorts reveals diverse etiologies and progression* (Nature Communications, 2026)

**Feed:** Lisa Bastarache — 2 new citations (Scholar, 09-06 06:02Z).

**Why HIGH:** Latent-class analysis identifies 5 MASLD subgroups
replicated across two EHR-linked cohorts, with PRS + rare variant
analysis showing subgroup-specific genetic drivers. Direct-hit for
`Chronic disease clustering and multimorbidity` (LCA on lab +
diagnosis trajectories in cardiometabolic disease — one of the two
disease areas the thread explicitly names). Also `Biobanks with EHR
linkage` (two-cohort EHR-linked-genomic replication is the pattern
the thread prioritizes).

---

### 12. Boceck, Laugwitz, Sturm, Bezdan, Gschwind et al. — *aiDIVA — hybrid AI for rare disease diagnostics using evidence-based, machine learning and language models* (npj Genomic Medicine, 2026)

**Feeds:** Stephen B Montgomery (10 new citations), Kai Wang (10 new
citations), Peter Szolovits (new related) — Scholar, 09-04 16:08Z
(triple-feed).

**Why HIGH:** Hybrid rules-plus-LM classifier for rare-variant
prioritization; directly bench-mates with GraphRareBench (Guo et al.
2607.24878) as an auditable-benchmark item for the `Auditable
HPO-driven diagnostic benchmarks with separable metrics for ranking
vs evidence coverage` sub-thread of `Rare disease`. The "hybrid"
framing (evidence rules + ML + LM) is on-brand for the thread's
preference for auditable-over-opaque diagnostic tooling.

---

## Housekeeping notes

- `digests/2026-09-01.md` and `2026-09-02.md` each surfaced 1 paper
  scoring 1 on a single-keyword hit (`precision medicine`, `motor`);
  both were off-thread. `2026-09-04.md` had two score-1 items
  (`causal inference`, `propensity score`) that fit METHODS-WATCH but
  not HIGH. This is a low-yield arXiv week for the tracked threads —
  Scholar and NCBI carried the report.
- No `arxiv-digest` PR / commit failure / GitHub Action notification
  hit the inbox this window (confirmed via
  `from:notifications@github.com` × `arxiv-digest` empty search).
  The daily crons all landed a commit; the two 0-paper days (09-03,
  09-05) and one 0-relevant day (09-06) are expected suppression
  behavior, not a pipeline problem.
- Four-feed surfacing pattern: the Park et al. OCD-PRS paper hit
  Karczewski, Denny, Bastarache-related, and Chenjie Zeng feeds
  simultaneously. If cross-ancestry-PGS-portability keeps hitting
  multiple author feeds like this, it's worth promoting to its own
  named sub-thread rather than nesting under `Genetic epidemiology`.
- Bastarache lineage was the single most productive author feed this
  window: 4 HIGH items across new-articles / new-related / citations
  (Chin sinusitis, DePaolo TAAD-PRS, Priya MASLD-LCA, plus Bal HCM-
  PRS via cross-feed). Worth noting for prioritization.

---

_Generated by the arxiv-digest scheduled routine on 2026-09-07._
