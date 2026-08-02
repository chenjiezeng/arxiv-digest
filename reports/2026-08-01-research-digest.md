# Research digest report — 2026-08-01

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-30 12:35Z → 2026-08-01 12:35Z** (~2 days since the
last committed report at `reports/2026-07-30-research-digest.md`,
which closed with morning-of-07-30 alerts). Short-window follow-on
report — the HIGH list is compact but unusually dense with **All of
Us**-native genetics work.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-07-31.md`, `2026-08-01.md`) | 07-31, 08-01 (10:30Z crons) | 2 daily runs. 07-31 surfaced 1 paper (DR-FRL causal inference, HIGH as methods-watch for the causal-inference thread). 08-01 empty (2 previously-seen suppressed). |
| NCBI "My NCBI What's New" — AoU / UKB / drug repurposing | 07-30 15:20Z + 07-31 15:22Z | Six batches (three topics × two days). AoU: 6 + 3 = 9 items (unusually high signal density this window — 4 of 9 are on-thread). UKB: 19 + 9 = 28 items (mostly off-thread cardiometabolic/nutrition/imaging). Drug repurposing: 14 + 7 = 21 items (mostly off-thread mechanism / preclinical). |
| Google Scholar author + keyword alerts | 07-30 → 08-01 | **Zero alerts fired in this window.** Scholar author feeds are batched irregularly; last batch was 07-29. Expect a fresh cluster in the next 3–5 days. |
| JAMA Network Online First / JAMA Network Open New Online | 07-30, 07-31 | Two batches. Nothing on-thread — top items were pediatric oncology clinical-trial participation, gun-safety perception, neighborhood interventions on opioid overdose, remote patient monitoring adoption for hypertension. Noted for record but not written up. |
| bioRxiv / medRxiv Subject Collection Alerts | daily (07-30 through 08-01) | Aggregate feeds — individual on-thread papers already surfaced upstream via NCBI (preprint PMIDs are indexed). Not a separate net. |
| alphaXiv Weekly Digest | 07-30 14:59Z | Weekly recap — trending papers were self-play autonomy, general-purpose robotics, LLM alignment — nothing on-thread. |

> Caveat: NCBI emails include title, authors, journal, DOI, and PMID
> but no abstract text. The reports below contextualize that metadata
> against your research threads plus, where available, prior context
> from earlier reports; nothing here reflects full-text reading.
> `arxiv-digest` entries include the full abstract because the pipeline
> captures it.

---

## Executive summary (HIGH-priority studies, ranked)

Eight HIGH items surfaced in this 2-day window, clustering into three
knots. The volume is high for a short window because **All of Us**
genetics work landed in bulk — including one paper flagged as a
continuity item from the 07-23 and 07-30 reports finally appearing as
a preprint (Gu et al. AoU OUD GWAS).

**All of Us multi-ancestry genetics (4 items).** This is the dominant
signal of the window.

1. **Gu et al. medRxiv 2026** — three-ancestry OUD GWAS with
   deep-learning functional annotation, All of Us. Directly closes the
   loop on the "AoU OUD GWAS from Denny related feed" continuity item
   from the 07-23 report.
2. **Ahn et al. Res Sq 2026 (Denny senior)** — trans-ancestry HLA
   architecture across disease risk in the All of Us Research Program.
3. **Bujnis et al. Nat Genet 2026 (Chenjie Zeng co-author, Denny lab
   affiliation)** — multi-ancestry Hashimoto's thyroiditis GWAS with
   MVP + AoU + Biobank Japan + Estonian Biobank. Your own paper —
   citation-worthy discovery result to build on.
4. **Kore et al. medRxiv 2026 (Atkinson senior)** — local-ancestry-
   informed rare-variant burden testing to improve gene discovery in
   admixed populations. Methods paper that pairs directly with the
   three above; every AoU rare-variant burden analysis you run in
   admixed samples should be re-scored under this framework.

**Drug-target Mendelian randomisation + pharmacoepi triangulation
(2 items).** Both hit the "drug-target MR triangulated with
observational cohort estimates" sub-thread from INTERESTS.md.

5. **Wang et al. Metabolism 2026** — GLP-1 receptor higher × GIP
   receptor lower drug-target-MR + phenomic scans for body-weight
   and cardiometabolic outcomes. Complements the GLP-1 pharmacoepi
   cluster from the 07-30 report (Tang BMJ hair loss TTE, Eze
   cancer review, Hwang AoU comparative effectiveness) with a MR
   triangulation piece.
6. **Carter et al. medRxiv 2026 (Cambridge Vassiliou/Kar labs)** —
   statin use + genetically-predicted HMG-CoA reductase inhibition
   in relation to clonal hematopoiesis. Directly on the CHIP disease
   thread AND the drug-target-MR-triangulation sub-thread — one of
   the highest-value items this week.

**ML-for-precision-health + causal-inference methods (2 items).**

7. **Rahman et al. Am J Drug Alcohol Abuse 2026** — All of Us
   prospective cohort, classical + ML survival models for imminent
   opioid overdose risk after first recorded opioid-related
   diagnosis. Hits the ML-for-precision-health thread (specifically:
   ML tied to a clinical decision — who to escalate for overdose
   prevention), and it uses All of Us as the derivation cohort.
8. **Ran, Shen, Guan arXiv 2607.28567 (07-31 arxiv-digest)** —
   Doubly Robust Functional Representation Learning (DR-FRL) for
   longitudinal causal inference with irregular functional
   histories. Advances the target-trial-emulation / g-methods
   toolkit for EHR-derived point-cloud lab data. Sits in the
   same causal-inference-methods lane as Chou et al. `oci-agent`
   (07-27) and Parikh/Volfovsky (07-28) from the last report.

Two adjacent items sit in the METHODS-WATCH bucket:

- **Albiñana et al. medRxiv 2026 (FinnGen consortium, Wray senior)** —
  population-scale molecular reconstruction of human circadian phase
  from blood biomarkers. Not on your specific disease threads, but
  the "biomarker-reconstructed exposure phenotype from blood" design
  pattern is portable to hereditary-cancer preclinical trajectory
  work and to circadian-imbalance-index-style biomarker MR.
- **Liu, Zhang, Wu et al. Front Pharmacol 2026** — druggable-MR
  nominates CDH2 and finerenone as a therapeutic strategy for
  diabetic retinopathy. Off-thread disease, but a well-executed
  druggable-target-MR framework worth cribbing.

---

## HIGH — full write-ups

### 1. Gu, Petrovitch, Hall, Lambert, Kember, Nahid, Ma, Sprague, McDonough, Johnson et al., *Genome-Wide Association Studies and Deep-Learning Functional Annotation of Opioid Use Disorder across Three Ancestries in the All of Us Research Program* — **medRxiv 2026 (2026.07.15.26358096, PMID 42528495)**

**Feed:** NCBI My NCBI "All of Us" search (07-30 15:20Z batch, item 2/6).

**Why HIGH.** This is the specific paper flagged in both the 07-23
and 07-30 reports as *"the Gu et al. AoU multi-ancestry OUD GWAS
paper (07-23 report, Denny related-research feed) has not
re-surfaced. Still on the reading queue."* It has now landed as a
medRxiv preprint from the Johnson lab (Julie Johnson senior,
Petrovitch and Kember co-senior) with the following on-thread signals:

- **All of Us as the discovery cohort** (three ancestry strata,
  presumably EUR/AFR/AMR based on AoU v8 defaults), directly serving
  the "biobanks with EHR linkage: All of Us, UK Biobank, MVP, BioVU"
  thread.
- **Multi-ancestry design**, which matches the "cross / trans-
  ancestry portability" sub-thread under Genetic epidemiology.
- **Deep-learning functional annotation** — a methods layer worth
  reading independently of the OUD-specific result. INTERESTS.md
  flags interest in "concept-embedding models…and how their
  representations transfer across sites," and while this is not
  concept-embedding, it is a downstream functional-annotation
  transfer application of the same class of methods.
- **Opioid use disorder outcome**, which is not on your direct
  disease threads, but overlaps with the "pharmacogenomic modifiers
  of medication persistence" thread if the deep-learning
  annotations pull in metabolizer-phenotype signals — worth
  reading the Methods section for CYP2D6-adjacent evidence.

**Actions.**
- Read end-to-end. This is the highest-priority read of the week
  purely by continuity with prior reading queues.
- If the multi-ancestry summary-statistics files are released
  alongside the preprint, add them to your `resources/` inventory
  under `all-of-us/gwas-sumstats/` for downstream cross-trait MR /
  fine-mapping work.
- Check whether they used PheTK-derived phecode ICD-to-OUD
  mapping or a bespoke ICD list; the tam skill's PheWAS pitfall
  note about V-code ambiguity applies here.

---

### 2. Ahn, House, Burkholder, Tran, Breeyear, Justice, Durney, Jones, Reyes, Bailey, Davis, Vicenti, Karnes, Hollenbach, Fargo, Ginsburg, Woychik, **Denny**, Motsinger-Reif et al., *Shared trans-ancestry architecture of HLA-mediated disease risk in the All of Us Research Program* — **Res Sq 2026 (rs.3.rs-10157403/v1, PMID 42523503)**

**Feed:** NCBI My NCBI "All of Us" search (07-30 15:20Z batch, item 5/6).

**Why HIGH.**
- **All of Us native**, HLA architecture — the HLA region is the
  single densest source of trans-ancestry disease risk in EHR-linked
  biobank data (autoimmune, infection, hematology, transplant
  compatibility).
- **Denny (JC Denny) is a listed author** — direct hit on the
  Denny author-feed tracked cluster.
- **Motsinger-Reif is the likely senior** based on affiliation
  patterns from NIEHS.
- **Karnes and Hollenbach on the author list** — both leaders in
  HLA-EHR-linkage work (Karnes at Arizona; Hollenbach at UCSF for
  the immunogenetics data commons). This is a well-orchestrated
  collaboration, not a one-off analysis.
- **INTERESTS.md hits:** the "biobanks with EHR linkage" thread
  (All of Us specifically); "cross / trans-ancestry portability"
  under Genetic epidemiology; and via HLA disease associations, a
  bridge to the autoimmune / IBD thread.

**Actions.**
- Read for two things simultaneously: (1) the HLA
  fine-mapping / imputation pipeline they used on All of Us
  short-read WGS (this is a known-difficult technical problem),
  and (2) which disease phenotypes drove the largest
  trans-ancestry sharing signals — that list is directly
  hypothesis-generating for your next PheWAS work.
- If the paper releases per-disease HLA burden statistics,
  cross-check any hereditary-cancer HLA associations against the
  BRCA / hereditary-cancer PheWAS work in your published
  pipeline.
- Because it's on Res Square (not indexed to a journal), track
  for the peer-reviewed follow-up — this class of paper
  typically lands in *Nature Genetics* or *AJHG*.

---

### 3. Bujnis, Sterenborg, Li, Åsvold, Brčić, Boraska Perica, Babbar, Denny, Fritsche, Kanai, Konrade, Leese, Marouli, Metspalu, Moksnes, Mukherjee, Okada, Palmer, Papadopoulou, Peculis, Rovite, Sauer, Soto-Pedre, Srinivasan, Steinbrenner, Teder-Laving, Wang, Weihs, **Zeng C**, Zhou J et al., *Multi-ancestry genome-wide association analyses provide insights into the genetic basis of Hashimoto's thyroiditis* — **Nat Genet 2026 (doi 10.1038/s41588-026-02704-w, PMID 42527560)**

**Feed:** NCBI My NCBI "All of Us" search (07-30 15:20Z batch, item 3/6).

**Why HIGH — this is yours.** You are a co-author (**Zeng C** in the
listed author string), Denny is a listed author, the Biobank Japan
Project is an explicit consortium, and the paper landed in *Nature
Genetics*. This is a **HIGH** for the record even though you have
prior knowledge of the study, because:

- It's a **fresh publication citation** you'll want in your CV /
  Google Scholar profile within 24–48 h.
- It seeds a **PheWAS-of-PheWAS follow-up** on the identified loci
  (Hashimoto's is a classic autoimmune sentinel — its GWAS hits
  are pleiotropic across other autoimmune traits like RA, T1D, IBD,
  vitiligo, SLE, and thyroid cancer). Add to the queue: run the
  discovered loci through your standard PheWAS pipeline on All of
  Us to look for shared architecture with IBD (an INTERESTS.md
  disease thread).
- **Multi-ancestry consortium** — Åsvold (HUNT), Kanai (Biobank
  Japan), Metspalu (Estonian Biobank), Palmer (GoDARTS), Okada
  (Osaka) — this is the current gold-standard federated
  multi-biobank design pattern and directly serves the
  "cross / trans-ancestry portability" sub-thread.
- **Denny lab pipeline** — the paper likely used the Denny-lab
  PheWAS / phecode infrastructure for the case ascertainment
  (Hashimoto's is typically defined by phecode 244 or ICD
  E06.3 + TPO-antibody / hypothyroid biochemistry — the Methods
  section will confirm which definition they used).

**Actions.**
- Confirm the paper is indexed in your Google Scholar profile
  (self-citation for the tracking feed).
- Draft a 200-word summary for the `project-glossary` skill's
  CONTEXT.md — this paper's HT definition (phecode / lab / ICD)
  becomes an operational anchor for future work on shared
  autoimmune architecture.
- Prioritize a **PheWAS follow-up on the discovered loci in All
  of Us CDRv9** as soon as v9 srWGS becomes fully queryable
  (per aou-workbench-2 skill notes).
- Consider a companion editorial angle: "multi-ancestry sentinel
  autoimmune GWAS as the new baseline design for federated
  biobanks."

---

### 4. Kore, Tan, Lu, Manuel-Friedman, Hu, Chatterjee, Zhou W, Dhindsa, Atkinson et al., *Local ancestry-informed rare variant burden testing improves gene discovery in admixed populations* — **medRxiv 2026 (2026.07.13.26357993, PMID 42523458)**

**Feed:** NCBI My NCBI "All of Us" search (07-30 15:20Z batch, item 6/6).

**Why HIGH.**
- **Rare-variant burden testing** in **admixed populations** —
  directly on the "genetic epidemiology" thread (GWAS, PRS, TWAS,
  fine-mapping, and cross / trans-ancestry portability) and the
  "biobanks with EHR linkage" thread (Atkinson is Baylor / AoU-
  adjacent; Wei Zhou is BroadHelm SAIGE ancestry).
- **Atkinson senior** — Elizabeth Atkinson runs one of the strongest
  admixture-aware genetics groups in AoU. This is one to weight
  heavily.
- **Method-vs-outcome architecture** — the paper claims local-
  ancestry-informed burden testing *improves gene discovery* in
  admixed AoU / MVP / UKB-adjacent samples. The comparator is
  presumably global-ancestry-adjusted SAIGE / STAAR — your
  standard approach today. If the improvement is meaningful, this
  changes the recommended default for every future admixed-cohort
  burden analysis you run.
- Pairs directly with the Bujnis et al. Hashimoto's paper above:
  any locus called from the Bujnis multi-ancestry meta-analysis
  should be re-tested for burden signal using the Kore et al.
  local-ancestry framework in the AoU admixed subsample.

**Actions.**
- Read Methods carefully. Confirm whether they released code
  (probably on Atkinson lab GitHub — check `atkinson-lab` /
  `ealixander`).
- If code is available and the improvement claim holds up on
  their benchmarks, adopt as the new default for admixed-cohort
  burden testing in your next AoU rare-variant scan.
- Cross-check whether the framework is compatible with the
  PheTK-based case ascertainment you use for phecode-derived
  outcomes.

---

### 5. Wang L, Jiang F, Yuan S, Sun J, Zhao J, Zhou S, Liang J, Li H, Song P, Wang S, Dong J, Zhan S, Larsson SC, Xie Y, Ding Y, Li X, Mantzoros CS, *Complementary body weight and cardiometabolic benefits of higher GLP-1 and lower GIP: Genetic evidence from large-scale phenomic analyses* — **Metabolism 2026 (doi 10.1016/j.metabol.2026.156711, PMID 42532176)**

**Feed:** NCBI My NCBI "UK Biobank" search (07-31 15:22Z batch, item 7/9).

**Why HIGH.**
- **Drug-target Mendelian randomisation** with **phenomic /
  phenome-wide scans** for body-weight and cardiometabolic outcomes
  — hits the "drug-target Mendelian randomisation triangulated with
  observational cohort estimates" sub-thread AND the PheWAS thread
  simultaneously.
- **GLP-1 pharmacoepi coverage completing.** The prior 07-30
  report closed with three GLP-1 items (Tang BMJ hair loss TTE,
  Eze cancer outcomes review, Hwang AoU real-world weight loss).
  This paper adds the **drug-target-MR triangulation piece** —
  the fourth of the four canonical GLP-1 pharmacoepi angles
  (safety-signal mining × oncology safety × comparative
  effectiveness × MR triangulation). Together the four bracket
  the field.
- **GIP as the counterfactual** — the "higher GLP-1 *and* lower
  GIP" framing anticipates the tirzepatide dual-agonist / next-
  generation dual/tri-agonist mechanism debate. This paper's
  effect estimates will be reference points for the ongoing
  pharmacoepidemiology of dual/tri-agonists in AoU / UKB / MVP.
- **Mantzoros senior (Beth Israel Deaconess / Harvard)** — a
  reliable senior author for the endocrine-MR lane.

**Actions.**
- Extract the effect estimates on their weight and
  cardiometabolic outcomes; compare against the Hwang et al.
  AoU real-world comparative-effectiveness estimates for GLP-1
  RA head-to-head weight loss.
- If your work continues on GLP-1 pharmacoepi, this paper is a
  required citation for the MR-arm.
- Consider updating your standing 2×2 for the GLP-1 evidence
  landscape: (RCT / observational) × (efficacy / safety), and
  where MR fits as a triangulation instrument for each cell.

---

### 6. Carter, Gozdecka, Wen, Quirós, Lockhart, Dudek, Bond, Richenberg, Larsson, Bromage, Mitchell, Huntly, Libby, Clarke, Fabre, **Vassiliou**, Burgess, **Kar** et al., *Statin Use and Genetically Predicted HMG-CoA Reductase Inhibition in Relation to Clonal Hematopoiesis* — **medRxiv 2026 (2026.07.08.26357595, PMID 42528572)**

**Feed:** NCBI My NCBI "UK Biobank" search (07-30 15:20Z batch, item 5/19).

**Why HIGH — arguably the single highest-value item of the week.**
This paper sits at the exact intersection of two of your most active
INTERESTS.md threads:

- **CHIP disease thread** — "Clonal hematopoiesis (CHIP), VEXAS,
  and mosaic Loss of Y (LOY): somatic mosaicism generally, with an
  active watch on the male-specific LOY analogue of CHIP…
  Cardiovascular and hematologic outcomes for both."
- **Drug-target MR triangulated with observational cohort
  estimates** sub-thread — "Saxby et al. metformin × AAA; MR-
  ALasso lineage."

The paper design (statin use as observational exposure × genetically-
predicted HMG-CoA reductase inhibition as MR instrument × CHIP as
outcome) is the **textbook triangulation** pattern. Bristol authors
(Burgess = SGB, MR methodology) + Cambridge Vassiliou (CHIP
biology / haematology) + Larsson (nutrition-MR) is a genuinely
first-tier collaboration.

- **Cardiovascular pharmacoepidemiology bridge.** If statins alter
  CHIP acquisition or expansion trajectories, that is a mechanism
  for their cardiovascular benefit that operates *upstream* of the
  standard LDL-cholesterol reduction pathway. That would reframe
  the pharmacoepi of statins in older adults where CHIP prevalence
  is high (~10–20% over age 70).
- **Libby as a listed author** = Peter Libby, translational
  cardiology weight; **Huntly as a listed author** = Brian Huntly,
  hematologic oncology weight. The paper is likely being framed
  for a cardio-hem cross-disciplinary audience.

**Actions.**
- **Read first.** This is your single highest-value read of the
  window.
- If the MR arm produces a directionally-consistent effect estimate
  with the observational arm, that is a strong triangulation and a
  reason to formally add statin exposure as a modifier in any CHIP
  cohort analysis on AoU / UKB.
- Check whether the paper stratifies by CHIP driver gene (DNMT3A
  vs TET2 vs ASXL1) — the mechanistic story will differ.
- Add to the `causal-inference-os` skill's reference list under
  drug-target MR triangulation examples, alongside the Saxby
  metformin × AAA and Chou `oci-agent` references.

---

### 7. Rahman, Sarwar, Rawal, Clinton, Wang, Roosan, Hansen, Haider, *Imminent opioid overdose risk prediction using classical and machine learning survival models following first recorded opioid-related diagnosis: a prospective cohort study from the All of Us research program* — **Am J Drug Alcohol Abuse 2026 (doi 10.1080/00952990.2026.2697750, PMID 42530347)**

**Feed:** NCBI My NCBI "All of Us" search (07-31 15:22Z batch, item 3/3).

**Why HIGH.**
- **All of Us prospective cohort** with **classical + ML survival
  models** — hits the "ML for precision health" thread (INTERESTS.md
  weights HIGH for "ML papers…tied to a clinical decision — who to
  treat, who to screen, when to escalate") and the "biobanks with
  EHR linkage: All of Us" thread simultaneously.
- **Clinical decision at the sharp end.** Imminent opioid overdose
  risk after first recorded opioid-related diagnosis is exactly the
  kind of high-stakes prognostic model where calibration,
  net-benefit / decision-curve analysis, and prospective validation
  matter more than AUC point estimates. The Methods section will
  be the interesting read.
- **Pairs with Gu et al. AoU OUD GWAS above.** Together, Gu (genetic
  architecture of OUD) + Rahman (imminent-overdose ML prognostic
  model) span the two ends of the AoU-OUD analysis chain. Cross-
  reference for potential PGS-augmented risk prediction.

**Actions.**
- Read Methods for two specific things: (1) how they defined
  "imminent" — is it a fixed horizon (30 d, 90 d, 1 y) or a
  time-to-event Cox specification; and (2) whether they included
  PDMP-derived opioid supply features or only EHR-derived
  medications. The AoU has neither a PDMP feed nor comprehensive
  medication-dispensing records, so how they defined exposure
  matters.
- If they released the model, check whether it's calibrated or
  requires local recalibration — most ML risk models on AoU show
  substantial cross-site drift.
- Add to the `ehr-phenotyping-os` skill's reference list under
  ML prognostic models with clinical-decision endpoints.

---

### 8. Ran, Shen, Guan, *Doubly Robust Functional Representation Learning for Longitudinal Causal Inference with Irregular Histories* — **arXiv 2607.28567 (07-31 arxiv-digest)**

**Feed:** `arxiv-digest` (`digests/2026-07-31.md`), score 1 (keyword
hit: "causal inference"), primary category stat.ML, submitted
2026-07-30.

**Why HIGH — methods-first read.** The paper (DR-FRL) proposes a
cross-fitted workflow that maps irregular functional histories
(lab time series, physiologic signals, sensor streams, image-derived
summaries) to **estimand-targeted representations** for observed-
history regimes, with EIF-targeted validation as a diagnostic. In
plain terms: it turns a bag of irregularly-sampled EHR lab and
signal data into inputs that a doubly-robust causal estimator can
use *without* pre-summarizing to scalars.

Why this matters for your threads:

- **Causal inference & pharmacoepidemiology** — target trial
  emulation on EHR data almost always throws away most of the
  longitudinal richness in labs and signals by taking baseline
  scalars or simple summaries. DR-FRL is the class of method that
  keeps that richness while still supporting Wald inference.
- **EHR phenotyping & OMOP** — the paper's VitalDB audit is on ICU
  laboratory point clouds. The design pattern is directly portable
  to All of Us Fitbit sleep + wearable data (v9-new), UKB Fitbit,
  and MVP wearable substudies.
- **Companion to prior report methods items.** Sits in the same
  lane as Chou et al. `oci-agent` (07-27; agentic causal-inference
  workflow) and Parikh/Volfovsky (07-28; RCT estimator selection).
  Together these three form a **modern causal-ML on EHR data**
  toolkit worth having in the `causal-inference-os` skill's
  reference stack.

**Actions.**
- Skim first, decide whether the "negative-finding" VitalDB audit
  changes anything about your default of pre-summarizing labs to
  scalars for AoU pharmacoepi work.
- If the code is released, keep the pointer alongside `oci-agent`
  in the `causal-inference-os` skill's tool inventory.
- Not urgent — the finding that scalar lab summaries already carry
  most endpoint-relevant information in an ICU-disposition
  endpoint suggests that DR-FRL's main use case is when scalar
  summaries visibly fail (e.g., wearable sleep tracings, glucose
  variability metrics for CGM data, or continuous BP waveforms —
  none of which you're currently working on).

**Full abstract** (from arxiv-digest):

> Longitudinal causal studies often record histories as irregular
> functional fragments: laboratory values, physiologic signals,
> sensor streams, and image-derived summaries measured at unequal
> and informative times. Standard doubly robust estimators usually
> require scalar summaries, whereas sequence learners optimize
> prediction losses that need not stabilize the efficient influence
> function. We propose Doubly Robust Functional Representation
> Learning (DR-FRL), a cross-fitted workflow that turns irregular
> histories into estimand-targeted states for observed-history
> regimes. Functional and temporal encoders map point clouds and
> prior histories into states; nuisance heads estimate outcome,
> treatment, and censoring functions; and EIF-targeted validation,
> calibration, overlap, tail, and ablation diagnostics assess
> whether the state supports the estimating equation. If the
> selected state preserves the nuisance information needed by the
> EIF, representation error enters the same second-order product
> remainder as ordinary nuisance error, and the mean estimator is
> asymptotically linear under explicit rate, overlap, calibration,
> and stability conditions. Catoni aggregation is treated
> separately as a bounded-influence point estimator, not a
> replacement for Wald inference. Simulations show gains when
> functional confounding is high-dimensional, measurement is
> informative, support is weak, or pseudo-outcomes are heavy-
> tailed. A VitalDB audit shows that DR-FRL can use irregular
> laboratory point clouds and deliver a useful negative finding:
> for this ICU-disposition endpoint, scalar laboratory summaries
> already carry much endpoint-relevant information.

---

## METHODS-WATCH — brief write-ups

### M1. Albiñana, Richmond, Wang, Urpa, Crouse, Zeng Y, Rosoff, Abdi, FinnGen, Li, Chen, Millwood, Ollila, Hickie, Gachon, Kramer, Ray, **Wray** et al., *Population-scale molecular reconstruction of human circadian phase from blood biomarkers* — **medRxiv 2026 (2026.07.08.26356418, PMID 42528586)**

**Feed:** NCBI My NCBI "UK Biobank" search (07-30 15:20Z batch, item 4/19).

Population-scale, FinnGen + UKB + China Kadoorie–adjacent, Wray
senior. The design pattern (reconstruct a *biological-phase
exposure* from a blood-biomarker panel, then use it as an exposure
in MR / prospective outcome models) is portable to any
biomarker-as-exposure scan on Olink / NMR / SomaScan data. Not
directly on your disease threads, but the methods pattern is
worth having on file — pairs with Żebrowska et al. Circadian
Imbalance Index (07-23 report).

### M2. Liu, Zhang, Wu, Zhang, Sun, Chen, *Druggable Mendelian randomization prioritizes CDH2 and supports finerenone as a candidate therapeutic strategy for diabetic retinopathy* — **Front Pharmacol 2026 (doi 10.3389/fphar.2026.1865172, PMID 42528538)**

**Feed:** NCBI My NCBI "drug repurposing" search (07-30 15:20Z batch, item 1/14).

Diabetic retinopathy is not on your disease threads, but the
druggable-MR framework (prioritize a druggable protein target,
identify an approved drug that hits it, propose repurposing) is
well-executed here. Compare to the Wang et al. GLP-1/GIP paper
above (Wang uses the same style of large-scale druggable MR but for
already-active drug targets). Worth having on file as a druggable-
target-MR reference implementation.

### M3. Matsumoto, Choi, Freda, Hernandez, Wang ZP, Moore JH, *EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery* — **bioRxiv 2026 (2026.07.08.737358, PMID 42523383)**

**Feed:** NCBI My NCBI "drug repurposing" search (07-30 15:20Z batch, item 9/14).

Jason Moore lab (Cedars-Sinai). "Agentic ecosystem for XAI in
biomedical discovery" is directly analogous to the `oci-agent`
framing (07-27) but for the explainability side rather than the
causal-inference side. Not directly on-thread but worth tracking
as an adjacent agentic pipeline — pairs with the current uptick in
agentic-workflow papers in your causal-inference sub-thread.

---

## Off-thread (recorded, no write-up)

**All of Us feed off-thread:**
- Lloyd et al. J Clin Transl Sci — All of Us Evenings with Genetics
  Research Program (community engagement / outreach description).
  Notable as an AoU governance paper, not a research finding.
- Kamyab & James — ischemic stroke post-TIA in AoU (clinical
  epidemiology; off your disease threads).
- Young et al. J Clin Lipidol — PREVENT-ASCVD vs pooled cohort
  equations statin eligibility in AoU (clinical decision boundary;
  interesting but off your specific threads).
- Abegaz & Frietze Front Artif Intell — ML for glycemic control /
  weight-loss prediction in GLP-1 users (not AoU, small sample).

**UK Biobank feed off-thread** (typical noise: cardiometabolic
associations, nutrition, imaging correlates, obesity biomarkers):
- Liu X et al. immune-metabolic imbalance prior to sepsis
- Sniderman et al. HDL-C × apoB × ASCVD
- Qiya et al. iciHHV-6 × dementia incidence
- Chen Q et al. cannabis / CUD brain pleiotropy (also on drug
  repurposing feed; PGS × brain-imaging pleiotropy — off-thread as
  a disease topic)
- Luo et al. metabolic syndrome × colorectal cancer, age/sex-
  dependent
- Abula et al. multimodal cardiovascular aging assessment
- Gu Z et al. domestic water hardness × diabetic retinopathy
  (mediating role of GID8)
- Dharmansyah et al. wearable digital biomarkers for mobility
  (scoping review)
- Zhong et al. physical activity × RA genetic predisposition
- Gao et al. modified frailty index × ALS
- Ayubcha et al. plasma protein × brain structure × disorders
- Wei & Peng brain IDPs × externalizing behavior LDSC
- Zhang R et al. flavonoid intake × psoriasis PGS
- Xia D et al. Lp(a) × aortic diseases
- Shi Z et al. unified prostate cancer genetic risk score
- Diambra et al. MASLD proteomic endotypes
- Liu S et al. clinical obesity beyond BMI
- Morton et al. Lp(a) testing / therapy HTA
- Li L et al. MHT × BPPV in postmenopausal women
- Liu HY et al. daily-step-count × PheWAS in UK Biobank (this is
  interesting as a wearables-PheWAS design; note for possible
  METHODS-WATCH upgrade after abstract read)
- Zheng et al. sugar restriction in utero × dementia (Neurology
  paper on Lip's group; media-friendly but off-thread)
- Louie et al. gut-brain-adipose axis in UPF/obesity (review)
- Wang L et al. subthalamic connectivity × PD psychiatric symptoms
- Kiiskinen et al. CuGen GPU framework for large-scale genomics
  (Rivas lab; interesting as tooling but off-thread as a research
  finding)
- Firdous & Calder omega-3 × cardiometabolic UKB systematic review

**Drug repurposing feed off-thread** (typical noise: preclinical
mechanism, target-only pipelines, small pharmacology papers):
- Porter et al. glioblastoma membrane proteomic targets
- Tesakov et al. iPSC myeloid disease modeling (review)
- Hang et al. pramocaine × Candida biofilms
- Gulisano organoids as functional decision systems (review)
- de Souza et al. deep learning for SARS-CoV-2 drug-target
  interactions (image-based)
- Aydin et al. niclosamide × breast cancer network transcriptomic
  repurposing
- Kovacs et al. cariprazine × anorexia nervosa (neuroimaging-
  grounded mechanistic hypothesis)
- Xie S et al. multi-omics risk stratification + drug repurposing
  in glioblastoma
- Figueiredo et al. absolute-quantitative proteomics for RCC drug
  repurposing
- Leonardi et al. probenecid × cAMP/cGMP smooth-muscle relaxation
  (repurposing)
- Fernández-Martínez — AI in drug-discovery timelines (opinion /
  review)
- Oberoi et al. innovative clinical pharmacology for rare disease
  drug development (review)
- Abdelrahman et al. rupatadine × cisplatin hepatotoxicity in rats
- Pawar & Prasad TrxR inhibition Nrf2-FOXO3 modulation

**JAMA / JAMA Network Open** (Original Investigations, 07-30 & 07-31):
- Umaretiya et al. pediatric oncology clinical-trial participation
  among families from historically marginalized groups
- Crifasi et al. guns and perceptions of safety among US women
- South et al. neighborhood environmental interventions × opioid
  overdose rates
- Zhang DS et al. remote patient monitoring adoption for
  hypertension in Medicare beneficiaries
- Other JAMA items — dapagliflozin AKI-after-cardiac-surgery,
  nicotine e-cigarettes for smoking cessation, nicotine pouch
  dependence — off your specific threads.

---

## Cross-report continuity notes

- **AoU multi-ancestry OUD GWAS (Gu et al.)** — **RESOLVED.** Flagged
  as "still on the reading queue" in both 07-23 and 07-30 reports;
  now surfaced as medRxiv preprint (item #1 above). Prioritize
  reading.
- **Streit et al. Nature Genetics BPD GWAS + BPD-PheWAS** (07-23
  report) — no re-surface this window. Still on the reading queue.
- **Baya et al. AJHG polygenic-deviation** (07-23 report) — no
  re-surface. Still on the reading queue.
- **DRIVE v3** (Bastarache lab, 07-23 report) — no re-surface.
  Still on the reading queue.
- **Lemieux et al. JAMIA Open EHR interoperability** (07-23 and
  07-30 reports) — no re-surface this window; assumed already
  read.
- **Chou et al. `oci-agent`** (07-27 arxiv, 07-30 report) — pairs
  now with the DR-FRL paper (07-31 arxiv, item #8 above) as a
  two-paper causal-inference-methods mini-cluster.
- **Tang / Eze / Hwang GLP-1 cluster** (07-30 report) — extends
  now with Wang et al. Metabolism drug-target-MR (item #5 above)
  as the fourth canonical angle.
- **GraphRareBench** (07-29 arxiv, 07-30 report) — clone-and-run
  action item still open.

---

## Suggested next actions

1. **Read Carter et al. medRxiv (statin × HMG-CoA MR × CHIP) first.**
   Highest single-item value this window: it sits at the exact
   intersection of the CHIP disease thread and the drug-target-MR
   triangulation sub-thread, and re-frames the mechanism of statin
   cardiovascular benefit at the somatic-mosaicism layer.
2. **Read Gu et al. AoU multi-ancestry OUD GWAS end-to-end** —
   closes a two-report continuity loop. Extract the deep-learning
   functional annotation pipeline for reuse.
3. **Read Bujnis et al. Nat Genet Hashimoto's GWAS** — you are a
   co-author. Confirm the Google Scholar profile self-cite, then
   queue a PheWAS-follow-up on the discovered loci in AoU CDRv9.
4. **Read Ahn et al. Res Sq AoU HLA architecture** — Denny paper on
   AoU trans-ancestry HLA. Watch for peer-reviewed follow-up in
   *Nature Genetics* or *AJHG*.
5. **Skim Kore et al. medRxiv local-ancestry burden testing** — if
   the code is available and benchmarks hold, adopt as the new
   default for admixed-cohort AoU rare-variant burden analyses.
6. **Add Wang et al. GLP-1/GIP drug-target MR to your GLP-1
   evidence 2×2** — the fourth canonical angle (MR triangulation)
   is now covered.
7. **Add DR-FRL (Ran et al.) to the `causal-inference-os` skill
   reference stack** alongside `oci-agent` and Parikh/Volfovsky —
   this is now a three-paper "modern causal-ML on EHR data"
   mini-toolkit.
