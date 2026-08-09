# Research digest report — 2026-08-09

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-08-04 → 2026-08-09 09:00Z** (~1 week since the last
committed report at `reports/2026-07-30-research-digest.md`). This is a
**multi-day catch-up** covering five `arxiv-digest` daily runs (Aug 4-8,
one empty) and two batches of Google Scholar author-feed alerts (Aug 7
20:16Z; Aug 9 01:10Z + 08:53Z).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-04.md` → `2026-08-08.md`) | 08-04 → 08-08 (10:30Z crons) | 5 daily runs. 4 non-empty (04, 05, 06, 07); 08 empty. ~21 papers surfaced total (10 previously-seen suppressed). Two are HIGH (Ciardulli functional-PS UK Biobank 08-05, score 4; Zhang wearable-PGS AoU 08-07, score 4); three METHODS-WATCH (Noma TTE R-package 08-04; Foulkes IPW-auxiliary-sampling 08-06; Sasson DXA SSL 08-04); rest score-1 off-thread. |
| Google Scholar alerts (author-feed cluster, Aug 7 20:16Z) | 07-30 → 08-07 | 12 author feeds fired — Denny (2), Bastarache, Karczewski, Yang, Ryan (2), Kai Wang, Callahan, Peter Szolovits, Montgomery, Chenjie Zeng. |
| Google Scholar alerts (author-feed cluster, Aug 9 01:10Z + keyword feed 08:53Z) | 08-07 → 08-09 | 13 author + 1 keyword feed. Denny (proteome MR CVD), Bastarache (hypophosphatasia NGS screening), Karczewski (organoid biobank Nature), Yang, Ryan, Kai Wang, Callahan, Szolovits, Montgomery, Zhiyong Lu, Marinka Zitnik, Hripcsak (federated FM), Chenjie Zeng (Lu et al. prostate cancer mortality); AoU keyword feed (Hysong et al. Comms Health, Markt et al. narcolepsy). |
| JAMA Network updates | 08-07 | Two batches — general Med News and JAMA Network Open weekly. No on-thread items surfaced. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and a
> snippet-length preview of each abstract only. The reports below
> contextualize that metadata against your research threads; nothing
> here reflects full-text reading. `arxiv-digest` entries include the
> full abstract because the pipeline captures it.

---

## Executive summary (HIGH-priority studies, ranked)

Ten HIGH items surfaced this week, clustering into four dense knots:

**Cancer genetic epidemiology + PheWAS (2 items, both direct-fit to
Zeng thread).** Lu et al. *Prostate Cancer and Prostatic Diseases*
2026 — germline genetic risk and prostate-cancer-specific mortality
in a population-based incident cohort (Chenjie Zeng self-citation
alert; the "germline PRS meets survival endpoint" design directly
mirrors your published work). Peng et al. medRxiv 2026 — early-onset
breast cancer combined **GWAS + PheWAS** on genetic susceptibility
and causes (Lisa Bastarache alert; hits your breast cancer
susceptibility + PheWAS/phecode infrastructure threads simultaneously,
with a young-onset ascertainment that has been under-served by
population-scale genomic work).

**All of Us + polygenic × behavioral / SDoH (2 items).** Zhang et al.
arXiv 2608.06063 — longitudinal Fitbit + MDD PRS + EHR-recorded
incident MDD in All of Us (3,030 EUR participants, 284 cases,
C-index 0.637 → 0.705 by stacking PGS with monthly wearable + PGS ×
wearable interaction). This is the cleanest **PGS × environment**
paper you'll see this month and it uses the AoU tri-modal (EHR +
PRS + Fitbit) design your composite-risk / PGS-tails framing calls
out. Hysong et al. *Communications Health* 2026 — practical
considerations for **social-determinant-based disease prediction in
All of Us** (AoU keyword feed; a methods-first framing paper for
AoU SDoH prediction that the digital-twins-from-EHR sub-thread
directly borrows from).

**Causal inference & pharmacoepi (3 items — one methods-first, two
GLP-1 / cardio-nephro).** Ciardulli et al. arXiv 2608.03200 —
**functional-propensity-score weighting** for time-varying UK Biobank
BMI trajectories → T2D and HbA1c (the g-methods extension your
"causal ML" branch tracks, with an unusually thorough UKB
illustration; score 4 in the digest). Noma arXiv 2608.01625 — the
**R package `TTE`** for target trial emulation, with SGLT2i vs DPP4i
and ARB vs CCB worked examples end-to-end (a "grab-and-use" tool for
your TTE / IPW pipeline). Liu et al. — cardiovascular outcomes of
**GLP-1 RAs vs DPP4i in ESKD patients with heart failure** (Patrick
Ryan feed; extends the GLP-1 pharmacoepi active thread into the
kidney-failure sub-population where trial evidence is thinnest).

**Genetic epi methodology + rare-variant × PGS (3 items).** Hilmarsson
et al. *Nature Communications* 2026 — **scalable high-resolution
ancestry deconvolution** for genomic data (Denny alert; the local-
ancestry infrastructure that the ancestry-aware PheWAS / cross-
ancestry PGS-portability threads depend on). Zhong et al. *Molecular
Genetics* — **cross-population proteome-wide MR** for cardiovascular
disease (Denny alert; the drug-target-MR + multi-omics-augmented-PRS
axis, cross-ancestry). Khan et al. medRxiv — **Uromodulin T62P
variant × age × polygenic risk** for kidney tubular stress and
injury (Karczewski alert; a canonical composite-risk paper —
Mendelian variant meets PGS meets aging as effect modifier — with
tissue phenotype anchoring).

**Additional HIGH.** Nadarajah et al. *Circulation* 2026 — **risk-
guided screening for atrial fibrillation using EHR** (Pascal Brandt
alert; slots directly into your EHR phenotyping + ML-for-precision-
health thread where the AF-screening question has been a canonical
test-bed). Burkhart et al. arXiv — **federated generative event
models for tokenized EHR** (Hripcsak alert; the federated-EHR-FM
sub-thread under EHR foundation models, distinct from centralized
CLMBR/MOTOR/MEDS work).

Three METHODS-WATCH sit adjacent: Foulkes et al. arXiv 2608.04918
(**IPW for auxiliary-variable dependent sampling in Long COVID**,
directly transferable to EHR two-phase-sampling designs); Sasson et
al. arXiv 2608.02208 (**self-supervised DXA JEPA** on UKB imaging,
biological-aging framing); Krol et al. arXiv 2608.02127 (**correlated
frailty model** for family-based rare-variant × survival — niche but
methods-clean).

---

## HIGH-priority detailed reports

### 1. Lu et al. — Germline genetic risk and prostate cancer-specific mortality in a population-based incident cohort

**Citation:** Lu L, Xu J, Shi Z, Engelmann V, Tran H, Wei J, et al.
*Prostate Cancer and Prostatic Diseases* 2026.

**Source:** Google Scholar alert (Chenjie Zeng — new related research;
2026-08-09 01:10Z).

**Why HIGH — threads served:** cancer genetic epidemiology (germline
predisposition genes); cancer survival disparity; PRS on hard
mortality endpoints; direct Zeng-thread continuity (a spiritual
successor to your published Zeng et al. germline-variant × cancer-
survival lines).

**What the study appears to do (from the snippet + venue):**
Population-based incident prostate-cancer cohort, followed for
prostate-cancer-specific mortality (PCSM). Germline genetic risk is
the exposure — the venue and title pattern make PRS the most likely
operational definition, with either a stacked pathogenic-rare-variant
layer (BRCA2 / ATM / HOXB13) or an ancestry-adjusted PRS
recalibration as the anchoring methodological piece. Endpoint is
PCSM (specific-cause mortality) rather than overall mortality — a
harder ascertainment problem that requires either registry linkage
or adjudicated cause-of-death coding in the underlying cohort.

**What to look for in the full paper (from the INTERESTS framing):**

1. **Ascertainment window and cohort framing.** "Population-based
   incident cohort" is the key phrase — is this a screening-detected
   cohort (PLCO-style) or a clinically diagnosed one? The
   penetrance-vs-severity story you care about depends on it.
2. **PRS composition and calibration.** Which PRS (Conti et al. 269
   variants? Multi-ancestry PRS?) and how are the effect sizes
   recalibrated in the mortality endpoint rather than the incidence
   endpoint from which most PRS were derived.
3. **Ancestry stratification.** Prostate cancer mortality has one of
   the largest ancestry disparities of any solid tumor — any PRS-
   mortality paper that doesn't stratify by AFR/EUR/EAS is missing
   the point.
4. **PSA screening / lead-time confounding.** A PRS-PCSM association
   that survives PSA-screening adjustment is a much stronger
   biological claim than one that doesn't.
5. **Interaction with rare-variant / clinical grade / stage.** Does
   the PRS-mortality signal remain in low-grade tumors (Gleason
   6-7)? That would matter for active-surveillance triage.

**Cross-references in your interest map:** zeng-publications skill
(cancer genetic epidemiology, germline variants, cancer survival
disparity), phers-hpo-phecodex (survival endpoint composite risk),
genetic epidemiology thread in `INTERESTS.md` (PRS composite risk
models, cross-ancestry portability).

**Action:** Fetch full text (open access on Prostate Cancer and
Prostatic Diseases if published open, otherwise via ScienceDirect /
Springer). Compare against the Denny / Vanderbilt PCa PRS
literature to see whether Lu et al. cites your prior work.

---

### 2. Peng et al. — Genetic susceptibility and causes for early-onset breast cancer: insights from genome-wide and phenome-wide analyses

**Citation:** Peng S, Jackson VE, Alpen K, Ye Z, Southey MC, Li S.
*medRxiv* 2026.

**Source:** Google Scholar alert (Lisa Bastarache — new related
research; 2026-08-07 20:16Z).

**Why HIGH — threads served:** PheWAS / phecode infrastructure
(genome-wide + phenome-wide dual scan); genetic epidemiology (GWAS,
young-onset ascertainment); zeng-publications (breast cancer
susceptibility genes); rare disease meets population genetics
(early-onset carries higher enrichment for high-penetrance variants).

**What the study appears to do:** Combines a genome-wide association
scan with a phenome-wide association scan, both anchored to
**early-onset breast cancer** (a cohort selection choice that
enriches for BRCA1/2/ATM/CHEK2/PALB2 carriers and shifts the effect-
size / risk-allele distribution relative to unselected breast-cancer
GWAS). Southey and Li at Monash / Ontario are established in the
young-onset breast-cancer literature.

**Why the design matters for your thread:**

- Most breast-cancer GWAS pool ages of onset; a young-onset-only
  design is a **PGS-tails / high-penetrance-enriched** cohort that
  can reveal effect-size shifts (larger for oncogenic loci, smaller
  for age-modifying loci) that averaging masks.
- The **PheWAS layer** anchored to early-onset BC lets you ask: what
  else — beyond breast — is enriched in the same genetic-liability
  strata? For BRCA/PALB2, that gives ovarian, pancreatic, and
  contralateral-BC pleiotropy on a phenome-wide grid. For lower-
  penetrance PGS loci, it gives insight into whether the
  "susceptibility" phenotype extends into benign breast disease,
  mammographic density, or other reproductive-oncology precursors.
- Ties directly to Bastarache et al. penetrance methodology and
  your prior BRCA / hereditary-cancer PheWAS work.

**What to look for in the full paper:**

1. **Age cutoff.** ≤50? ≤45? ≤40? Each shifts the rare-variant
   enrichment dramatically.
2. **Case-control design.** How were controls selected —
   population-matched (UKB-style), family-based (case-parent trio),
   or cascade-tested-negative?
3. **PheWAS scaffolding.** Phecode v1.2 or phecodeX 1.0/1.1? Which
   biobank(s) provide the phenotype substrate? If AoU, look at how
   they handled EHR follow-up for young women (short intervals,
   fewer non-cancer diagnoses).
4. **"Causes" framing.** The title uses "causes" — read carefully
   to see whether that is (a) MR-style causal-inference language,
   (b) mediation-based causal decomposition, or (c) descriptive
   attribution across variant categories. The interpretation shifts.
5. **Novel loci vs. replication.** How much is discovery vs.
   confirmation of Michailidou / BCAC loci?

**Cross-references:** zeng-publications skill (breast cancer
susceptibility, TWAS lineage), phewas-thinking, ehr-phenotyping-os
(case ascertainment for young-onset).

**Action:** Fetch the medRxiv PDF for full methods. Watch for a
follow-up published version at a genetic-epi journal (Am J Hum
Genet, Genet Med, JNCI).

---

### 3. Zhang et al. — Longitudinal wearable monitoring and polygenic risk for incident MDD in All of Us

**Citation:** Zhang Y, Folarin AA, Zhong R, Kim H, Sun S, Stewart C,
Dobson RJB. arXiv 2608.06063v1, submitted 2026-08-06.

**Source:** `arxiv-digest/digests/2026-08-07.md` (score 4 — keyword
hits: all of us, polygenic risk, polygenic, prs).

**Why HIGH — threads served:** biobanks with EHR linkage (All of
Us); PGS × environment interactions (Nagpal & Gibson lineage);
digital phenotyping for genetically informed risk monitoring
(digital-twins-from-EHR sub-thread); composite risk models stacking
PRS with real-world behavioral data.

**Design (from the digest abstract):**

- **Population:** 3,030 adults of genetically inferred European
  ancestry in All of Us, of whom 284 had EHR-recorded incident MDD
  after a 180-day baseline period.
- **Data streams:** genomic (MDD PRS), EHR (incident MDD
  ascertainment), and longitudinal Fitbit wearable data (physical
  activity + sleep features).
- **Models:** time-varying Cox with three exposure blocks —
  (i) baseline MDD PRS, (ii) monthly wearable-derived activity /
  sleep features, (iii) PRS × wearable-feature interactions.
- **Discrimination:** C-index climbs from **0.637** (PRS alone) to
  **0.705** when baseline wearable + monthly wearable + interactions
  are stacked on top of PRS.

**Key findings (from the abstract):**

1. Higher MDD PRS is associated with higher incident-MDD hazard —
   expected direction, worth confirming the effect size in AoU
   given the modest N.
2. **Lower daily steps, lower light + vigorous PA, lower sleep
   efficiency, and greater sleep-duration variability** all
   independently associate with higher MDD hazard — the two
   modifiable behavioral axes (activity + sleep-quality) both
   show independent effects.
3. **Sedentary time and sleep-duration variability interact with
   MDD PRS** — the association is stronger among high-PRS
   participants. That's the PGS × behavior interaction Nagpal &
   Gibson called "pervasive" — this paper delivers it for MDD in
   AoU rather than UKB.
4. **PRS-stratified HR curves:** the same estimated risk level is
   reached at *more favorable* behavioral profiles among high-PRS
   participants than low-PRS ones — the actionable interpretation
   is that high-PRS individuals may need "cleaner" behavioral
   profiles to achieve equivalent risk, or equivalently that
   behavioral targets should be genotype-informed.

**Why this is high-value for your thread:**

- Direct implementation of the **PGS × environment / GxE** frame
  from the `INTERESTS.md` genetic-epi block.
- Uses the AoU tri-modal (PRS + EHR + Fitbit) stack that is your
  cleanest sandbox for **genetically-informed digital phenotyping**.
- Time-varying Cox with monthly-updated behavioral exposures is a
  useful template for the **CFTR / GLP-1 modulator persistence**
  pharmacoepi lines you track — the same design pattern with
  medication-persistence as the time-varying exposure and PRS as
  the modifier.
- The C-index gain (0.637 → 0.705) is a legitimate clinical-utility
  improvement, not just a p-value story.

**Limitations to watch:**

- **EUR-only** — the PGS × wearable interaction is likely to
  attenuate in AFR/AMR strata where MDD PRS is less-well
  calibrated. A follow-up cross-ancestry version would be the
  natural extension.
- **Small N of events (284)** — the interaction estimates will be
  wide-CI. Verify that the C-index gain replicates on a held-out
  slice rather than reflecting in-sample overfitting.
- **Fitbit selection bias** — AoU Fitbit consenters are a
  self-selected sub-cohort with higher SES / better health-
  literacy. That both attenuates PRS gradient (healthier baseline)
  and inflates activity-sleep gradient (better tracker adherence).
  A sensitivity analysis under IPW for Fitbit-consent probability
  would strengthen the claim substantially.
- **MDD ascertainment via EHR codes** — the 284 incident-MDD case
  count depends on the phecode / OMOP concept definition used;
  compare against Bastarache / phecodeX MDD definitions.

**Action:** Read the full arXiv PDF (v1). This is a strong candidate
for cross-citation in any composite-risk / PGS-tails methods paper
you write on AoU data.

---

### 4. Hysong et al. — Practical considerations for social determinant-based disease prediction in the All of Us Research Program

**Citation:** Hysong MR, Manning AK, Green MD, Konigsberg IR, et al.
*Communications Health* 2026.

**Source:** Google Scholar keyword alert ("All of Us research
program" — new results; 2026-08-09 08:53Z).

**Why HIGH — threads served:** biobanks with EHR linkage (AoU
methods paper); ML for precision health (SDoH-based prediction is
the "who to screen" axis of your ML thread); ehr-phenotyping-os
(SDoH ascertainment is a phenotyping-adjacent problem).

**What the study appears to do:** Methodological / framing paper
on how to use AoU's **social-determinants-of-health survey and
neighborhood-level linkages** for disease-prediction modeling. The
"practical considerations" title strongly implies a set of pitfalls
and best-practices (survey missingness patterns, neighborhood-
linkage granularity, differential SDoH-measurement by ancestry /
region, calibration under distribution shift) rather than a
disease-specific claim.

**Why this is high-value for your thread:**

- AoU's SDoH data is under-exploited relative to its EHR + WGS
  data. This paper likely lays out the ascertainment protocol
  and metadata caveats that any future AoU-based SDoH-augmented
  PRS paper would need to cite.
- Slots into the **digital twins from EHR** sub-thread — an SDoH
  layer on top of EHR is exactly the demographic-and-context
  substrate the Cell 2026 digital-twins paper called for.
- Feeds directly into any composite-risk model that stacks PRS +
  EHR-derived features + neighborhood context (e.g., colorectal
  cancer screening uptake).

**What to look for:**

1. **Which SDoH domains** are covered — AoU's Personal Medical
   History, Social Determinants of Health, and Lifestyle surveys
   each have different completeness patterns.
2. **Neighborhood linkage granularity** — census tract vs. ZIP-9?
   Public-vs-controlled tier?
3. **Missingness handling** — MAR assumption for survey completion?
   IPW for consent?
4. **Fairness / calibration audit** — do SDoH-augmented prediction
   models drift across race/ethnicity strata differently than
   EHR-only models?

**Cross-references:** aou-workbench-2 skill (v9 AoU CDR reference),
verily-workbench-aou (SDoH survey handling), ehr-phenotyping-os.

**Action:** Fetch the *Communications Health* article. Consider
whether the pipeline described is portable to your AoU CFTR-
modulator and BRCA-cascade work where SDoH strongly modulates
uptake but has been treated crudely to date.

---

### 5. Ciardulli et al. — Generalized propensity score weighting for functional causal inference (UK Biobank BMI → T2D)

**Citation:** Ciardulli S, Fontana N, Vantini S, Ieva F. arXiv
2608.03200v1, submitted 2026-08-04.

**Source:** `arxiv-digest/digests/2026-08-05.md` (score 4 — keyword
hits: uk biobank, biobank, propensity score, causal inference).

**Why HIGH — threads served:** causal inference & pharmacoepi
(g-methods extension for time-varying exposures); biobanks with EHR
linkage (UKB longitudinal BMI); machine learning for precision
health (functional-data-analysis for irregular longitudinal
biomarkers).

**What the study does (from the digest abstract + deep summary):**

- **Methodological contribution:** extends propensity-score
  weighting to **functional treatments** — exposures observed
  continuously over time rather than as scalars. Existing PS
  methods handle scalar treatments; this paper builds a covariate-
  balance weighting scheme that removes dependence between a
  time-varying trajectory and observed confounders.
- **Dual formulation:** they cast weight estimation as a smooth
  unconstrained optimization, avoiding the proportionality
  constraint and sequential line search of prior functional-PS
  work. Computationally, the estimator scales with `p × L` (number
  of covariates × basis dimension) rather than sample size.
- **Extensions:** framework naturally extends to
  time-varying covariates and to longitudinal outcomes via
  **function-on-function marginal structural models**, allowing
  estimation of causal effect *surfaces* rather than point effects.
- **UK Biobank application:** estimate the causal effect of
  **midlife BMI trajectories** on incident Type 2 Diabetes risk
  and on subsequent **HbA1c trajectories** — a natural test case
  for the functional-treatment framing since the standard baseline-
  BMI Wainberg et al. 2019 causal analysis on UKB is explicitly
  the comparator they cite.

**Why this matters for your thread:**

- Extends **marginal structural models** to a functional-treatment
  regime — directly applicable to CFTR modulator persistence
  (treatment is a trajectory, not a point), GLP-1 RA dosing over
  time, HRT duration, and any pharmacoepi question where the
  "dose × time" surface matters more than "on / off".
- The **effect-surface** output aligns with the digital-twins-from-
  EHR line: a per-patient predicted counterfactual trajectory
  under alternative BMI paths.
- The computational scaling (independent of N) matters for AoU /
  UKB-scale analysis where the alternative (repeated inverse-
  probability weighting per time-point) becomes intractable.

**What to watch:**

- **Assumptions** — sequential exchangeability, positivity, and no
  interference all get harder under functional treatments.
  Ciardulli et al.'s formal assumption set is the piece to read
  carefully.
- **Robustness to trajectory misspecification** — how much
  smoothness is imposed on the BMI trajectory, and how does
  effect estimation degrade under sparse-visit / irregular-
  sampling conditions typical of AoU EHR data?
- **Comparison to g-computation and TMLE** — Ciardulli et al. is
  a PS-weighting paper; a functional-TMLE alternative would give
  doubly-robust guarantees.

**Cross-references:** causal-inference-os skill (g-methods,
marginal structural models, target-trial-emulation), waxse (UKB
BigQuery-based genomics), tam (PheTK-based cohort building).

**Action:** Fetch the full arXiv PDF. Evaluate whether the R
implementation (typically these papers ship one) is mature enough
to prototype on your CFTR modulator persistence question in AoU
CDRv9.

---

### 6. Noma — Target Trial Emulation with the R Package TTE: A Tutorial and Methodological Guide

**Citation:** Noma H. arXiv 2608.01625v1, submitted 2026-08-03.

**Source:** `arxiv-digest/digests/2026-08-04.md` (score 2).

**Why HIGH — threads served:** causal inference & pharmacoepi (TTE
is the load-bearing framework for the entire pharmacoepi thread);
methods-tooling.

**What the study does:** A self-contained methodological guide +
practical tutorial for the R package **`TTE`** for target trial
emulations on longitudinal observational data. Covers the full
pipeline: target-trial protocol, ITT vs per-protocol estimands,
identification assumptions, baseline vs person-period data
structures, temporal ordering for longitudinal weights, stabilized
treatment + censoring weights, weight truncation, balance +
effective-sample-size diagnostics, weighted pooled discrete-time
survival models, model-based standardization, competing-risk
analysis, weighted Kaplan-Meier + Aalen-Johansen estimation, and
cluster bootstrap.

**Two worked examples** — end-to-end:

1. **SGLT2 inhibitor vs DPP4 inhibitor initiation** with all-cause
   death (canonical pharmacoepi TTE example).
2. **Sequentially nested ARB vs CCB** trials with heart-failure
   hospitalization and competing death (extending to nested-trial
   design + competing risks).

**Why this is HIGH:**

- The **`TTE` R package** is a direct alternative to `CausalTrialEmulator`
  and hand-rolled Cornfield/Robins pipelines. Having a maintained
  package with vignette-style tutorials substantially lowers the
  cost of doing pharmacoepi TTE for your GLP-1 / SGLT2i / CFTR /
  HRT lines.
- The competing-risks handling is often the sloppiest part of
  hand-rolled TTE code — Noma's package presents it as a
  first-class citizen.
- The sequentially-nested-trials example is the design pattern
  you need for the **medication-persistence** questions
  (initiator vs continuer vs re-initiator).

**Caveats:**

- Author-only paper — need to check for adoption / community around
  the package (GitHub stars, issue activity, cross-citations).
  R packages with one author frequently go unmaintained.
- Framework choices need to be compared to the Hernán/Robins
  reference implementations before you trust downstream inference.
- Watch for how the package handles clustering (person-period
  observations within individual within clinic) — cluster
  bootstrap is mentioned but the implementation details matter.

**Action:** Skim the tutorial. If the package is on CRAN, install
and reproduce the SGLT2i vs DPP4i example against your AoU
prescription data as a smoke test. If it works well, this is a
candidate to add to the `causal-inference-os` skill as a
"first-try" pipeline.

---

### 7. Liu et al. — Cardiovascular outcomes of GLP-1 RAs vs DPP4 inhibitor in ESKD patients with heart failure

**Citation:** Liu PY, Shih CK, Hsieh MHC, et al. Journal not in
snippet; 2026 (Patrick Ryan feed).

**Source:** Google Scholar alert (Patrick Ryan — new related
research; 2026-08-07 20:16Z).

**Why HIGH — threads served:** causal inference & pharmacoepi (GLP-1
active thread — extension into end-stage kidney disease + heart
failure comorbidity where the trial evidence is thinnest).

**What the study appears to do:** Real-world comparison of
cardiovascular outcomes between **GLP-1 RA initiators** and **DPP4
inhibitor initiators** among patients with **end-stage kidney
disease (ESKD) AND heart failure** — a sub-population that is
consistently under-represented or excluded in the pivotal GLP-1 RCTs
(LEADER, SUSTAIN-6, REWIND, HARMONY, PIONEER-6). The exclusion
matters because ESKD-HF patients are precisely the group at highest
cardiovascular risk and with least clean prior evidence.

**Why this is a high-value pharmacoepi target:**

- **Real-world evidence in an RCT-excluded sub-population** is the
  canonical use-case for observational pharmacoepi. The design
  choices to look at are:
  1. Active-comparator (DPP4i vs GLP-1 RA) is correct — avoids
     the healthy-user bias of a placebo comparator.
  2. New-user design and index-date alignment.
  3. Confounding by indication — ESKD + HF is a heavy
     multimorbidity load, and clinicians probably choose GLP-1 vs
     DPP4i based on BMI / A1c trajectory / cost, not randomly.
  4. Immortal-time bias if follow-up starts before drug
     initiation.
  5. Positivity concerns — does DPP4i-initiation actually happen
     in the sickest ESKD-HF stratum? If not, marginal-structural-
     model interpretation is limited.
- Slots into the **cardiovascular-outcome pharmacoepi triangulation**
  you already track (Tang BMJ / Eze systematic review / Hwang AoU
  from the 07-30 report).

**What to look for:**

1. **Data source** — Taiwan NHI is the most common data source for
   this author cluster; that shifts the ESKD-dialysis-modality
   distribution and outcome ascertainment.
2. **Endpoint definition** — composite MACE? All-cause CV death?
   Heart-failure hospitalization?
3. **Sensitivity to unmeasured confounding** — E-value or Rosenbaum
   bounds.
4. **Whether the study explicitly follows target-trial-emulation
   protocol** or is a legacy new-user active-comparator design.

**Action:** Retrieve the full PDF via the journal listed in the
Scholar-alert link. Compare effect sizes against the ESKD-adjacent
sub-group analyses in the FLOW trial (semaglutide in DKD) if any
are reported.

---

### 8. Hilmarsson et al. — Scalable high-resolution ancestry deconvolution for genomic data

**Citation:** Hilmarsson H, Kumar AS, Barrabés M, Rastogi R, et al.
*Nature Communications* 2026.

**Source:** Google Scholar alert (Joshua C. Denny — new related
research; 2026-08-07 20:16Z).

**Why HIGH — threads served:** genetic epidemiology (ancestry-aware
PGS and cross-ancestry portability); PheWAS / phecode infrastructure
(ancestry-aware effect estimation is the load-bearing dependency
for cross-ancestry PheWAS); pangenome-informed variant calling
sub-thread.

**What the study appears to do (from snippet + venue):** Presents a
**scalable, high-resolution local-ancestry inference (LAI)** method,
positioning it against the RFMix / Gnomix / HAPMIX generation. High
resolution likely means (a) fine-scale ancestry categories beyond
super-population labels (e.g., specific European sub-populations,
West-African vs East-African, admixed-American granularity), and
(b) small ancestry-tract detection sensitivity (short recent-
migration signals).

**Why this matters for your thread:**

- **PGS portability** across ancestry is the biggest unsolved
  problem in PGS-based composite risk (Martin, Kachuri, Baya).
  Higher-resolution LAI lets you (a) compute PRS per local-ancestry
  segment (partial-PGS in Marnetto et al.'s framing) rather than
  globally, and (b) audit PGS attenuation across sub-populations
  within a super-population label.
- The digital-twins-from-EHR and composite-risk lines both need
  ancestry-aware calibration; global-ancestry proxies (proportions
  of AFR / EUR / AMR) mask the tract-level heterogeneity that
  actually drives PRS-effect drift.
- Nature Communications venue suggests a substantial methods
  contribution with released software — check for a GitHub / PyPI
  package.

**What to look for:**

1. **Speed / memory profile** — "scalable" claims in LAI usually
   mean "runs on WGS-scale data without an HPC cluster."
   Benchmark against Gnomix.
2. **Training reference panel composition** — the fine-scale
   ancestry labels are only as good as the training panel. If it
   uses HGDP, HRC, or 1000G Phase 3 + AoU + UKB, that's the
   modern gold standard.
3. **Performance on admixed populations** — the AA / Hispanic /
   Native Hawaiian / Pacific Islander stratifications in AoU are
   the acid test.
4. **Availability of trained models** — is there a pretrained
   model to run on AoU / UKB out-of-the-box, or does one need to
   retrain?

**Cross-references:** waxse (WGS/Hail lineage), aou-workbench-2
(AoU genomics), broad-genomics (Karczewski cluster).

**Action:** Fetch the *Nature Communications* article and the
associated GitHub repository. Consider it as a candidate to run
on the AoU v9 WGS VDS as prep work for any ancestry-stratified
PheWAS on AoU.

---

### 9. Zhong et al. — Cross-population proteome-wide Mendelian randomization for cardiovascular disease

**Citation:** Zhong H, Zhu J, Liu S, Wong HTH, Zhang Y, Luu HN, et al.
*Molecular Genetics* [journal exact name from snippet is "Molecular
Genetics"; likely *Molecular Genetics and Metabolism* or *Human
Molecular Genetics* — confirm from full record] 2026.

**Source:** Google Scholar alert (Joshua C. Denny — new related
research; 2026-08-09 01:10Z).

**Why HIGH — threads served:** genetic epidemiology (drug-target MR,
proteome-wide MR); multi-omics-augmented PRS thread (proteomics-as-
exposure); causal-inference triangulation (MR complementing
observational).

**What the study appears to do:** Proteome-wide Mendelian
randomization across **multiple population strata** for
**cardiovascular disease outcomes** — the design pattern that
identifies proteins with genetic-instrument-supported causal
associations with CVD, then compares effect sizes across ancestries
to distinguish reproducible drug-target signals from ancestry-
specific artefacts.

**Why this matters for your thread:**

- **Drug-target MR** is the highest-yield MR design for the
  pharmacoepi / drug-repurposing crossover — it identifies proteins
  whose genetically-instrumented perturbation predicts disease
  outcome, giving repurposing candidates and dose-response
  guidance.
- **Cross-population** framing is the correction to prior single-
  ancestry pQTL-MR work — pQTL effect sizes attenuate across
  ancestries (Sun et al. UK-Biobank Olink work is the primary
  reference; ARIC + AoU proteomics is the counterweight).
- Ties to the **Saxby et al. metformin × AAA** and **MR-ALasso**
  lineage on drug-target MR that the INTERESTS pharmacoepi block
  calls out.

**What to look for:**

1. **Instrument selection** — cis-pQTL only? cis+trans? MR-Egger
   sensitivity for horizontal pleiotropy?
2. **Ancestry strata** — EUR + EAS + AFR? How much AFR pQTL data
   was available?
3. **Colocalization** — pQTL-CVD colocalization is the strong
   sufficient condition for a causal-protein claim; without it,
   MR alone can be confounded by LD.
4. **Replication** — do effect sizes triangulate across INTERVAL /
   deCODE / UKB Olink / AoU (if included)?
5. **Novel targets** — how many new drug-repurposing candidates
   emerge, and how many are already-known targets (validation) vs
   truly novel?

**Action:** Fetch the full paper. Cross-reference against
Sun-Butterworth pQTL-MR review and the AoU proteomics rollout
timeline for candidate replication.

---

### 10. Khan et al. — Uromodulin T62P variant × age × polygenic risk in kidney tubular stress and injury

**Citation:** Khan A, Gresch A, Olinger E, Mariniello M, Shang N, et al.
*medRxiv* 2026.

**Source:** Google Scholar alert (Konrad Karczewski — new related
research; 2026-08-07 20:16Z).

**Why HIGH — threads served:** APOL1 / kidney-disease specific
thread (uromodulin is the second key kidney-disease genetic story
after APOL1); genetic epidemiology (composite-risk: rare variant ×
PGS × age modifier — the Baya AJHG-style "misaligned individuals"
frame); variant interpretation (T62P — a specific missense variant
with functional characterization).

**What the study appears to do (from snippet):** Functional +
population-genetic characterization of an **ultra-rare missense
variant** in **UMOD (uromodulin)** — T62P — with kidney tubular
stress and injury as the phenotype. The variant effect is modulated
by **age** (penetrance rises with age, an important precondition for
using cross-sectional biobank prevalence to infer lifetime risk) and
by **polygenic risk** (composite-risk sandwich — rare pathogenic
variant + PRS jointly predict, more than either alone).

**Why this matters for your thread:**

- **UMOD is the second big kidney-genetics story after APOL1** and
  has been undercovered in the composite-risk literature. This
  paper adds a specific variant with mechanistic anchoring (tubular
  stress phenotype in cell / mouse models, presumably).
- **Rare-variant × PGS × age** is the exact composite-risk framing
  Baya (AJHG 2026), Souaiaia (Nature PGS-tails), and Vazquez
  (Genetics low-risk-group designs) call out. Having a canonical
  kidney example strengthens the general template.
- Ties to the CHIP / VEXAS / LOY somatic-mosaicism-as-modifier
  thread indirectly — age-as-modifier for a germline variant
  behaves analogously to somatic-mosaic-accumulation-as-modifier.

**What to look for:**

1. **Population sample** — BioMe, AoU, UKB? Which cohorts
   contributed to the age × PGS interaction?
2. **Effect size at each variant × PGS × age cell** — the
   penetrance heatmap is the money-figure to look for.
3. **Functional readout** — tubular stress markers (KIM-1,
   NGAL)? Kidney biopsy? Cell-line vs organoid model?
4. **Clinical actionability** — is a T62P carrier with high PRS
   and age > 60 already at 3-4× risk for CKD progression?
5. **Comparison to APOL1 G1/G2 × PGS × age** — parallel design
   patterns.

**Cross-references:** wglab (variant classification), waxse (WGS
+ EHR pipelines), broad-genomics (Karczewski / gnomAD orbit).

**Action:** Fetch the medRxiv PDF. Consider whether the design
pattern is portable to a CFTR-modifier composite-risk analysis on
AoU (rare CFTR variant + modifier PGS + age for CF-carrier
penetrance).

---

### 11. Nadarajah et al. — Risk-Guided Screening for Atrial Fibrillation Using Electronic Health Records

**Citation:** Nadarajah R, Wu J, Wahab A, Reynolds C, Haris M, et al.
*Circulation* 2026.

**Source:** Google Scholar alert (Pascal Brandt — new related
research; 2026-08-09 01:10Z).

**Why HIGH — threads served:** EHR phenotyping & OMOP (large-scale
EHR-based screening pipeline); ML for precision health (who to
screen for AF — a canonical "clinical decision-tied" ML question);
biobanks with EHR linkage.

**What the study appears to do:** Evaluates a **risk-guided AF
screening** protocol driven by EHR-derived risk features — i.e.,
instead of universal age-based screening (per USPSTF 65+), use
EHR-mined predictors (BMI, HTN, prior stroke, HFpEF risk markers)
to target screening to the highest-risk stratum. *Circulation* venue
means this is either a cluster-RCT-style pragmatic screening trial
or a rigorous prospective cohort — the abstract snippet ("BACKGROUND:
Screening for atrial fibrillation") is consistent with either.

**Why this matters for your thread:**

- **Risk-model-driven screening** is the endgame for the ML-for-
  precision-health thread — the "who to treat / who to screen"
  clinical decision anchor.
- EHR-derived risk prediction for AF has canonical models (CHARGE-AF,
  C2HEST, HAVOC) — this paper likely benchmarks against or extends
  those with ML approaches.
- Extending to a **PGS-augmented** version (AF PRS + EHR features
  jointly) is the natural composite-risk follow-up.

**What to look for:**

1. **Study design** — cluster-randomized? Observational cohort with
   simulated screening?
2. **Model performance vs current guideline** — sensitivity /
   specificity at various risk-score cutoffs vs. USPSTF 65+ rule.
3. **Downstream anticoagulation and stroke outcomes** —
   discrimination is one thing, but reduction in ischemic stroke
   at population level is the outcome that matters.
4. **Portability** — was the model trained + tested in the same
   health system? Cross-system validation is the gold standard.

**Action:** Fetch the *Circulation* full text. Compare against
NHS AF-screening pilot literature (which has been the reference
cohort for this line).

---

### 12. Burkhart et al. — Federated generative event models for tokenized electronic health records

**Citation:** Burkhart MC, Solo L, Lee I, Charles SK, Liao Z, et al.
*arXiv* 2026.

**Source:** Google Scholar alert (George Hripcsak — new related
research; 2026-08-09 01:10Z).

**Why HIGH — threads served:** EHR foundation models (federated
sub-thread — the counterpart to centralized CLMBR/MOTOR/MEDS);
knowledge representation in EHRs (tokenization choices under
federated constraints); privacy-preserving EHR analytics.

**What the study appears to do:** A **federated** framework for
training **generative event models** on **tokenized EHR data** —
i.e., an EHR foundation model that can be pretrained without
centralizing patient data. The setup is directly analogous to
FedGPT / federated-LLM work but adapted to EHR event-sequence
tokenization.

**Why this matters for your thread:**

- **Federated EHR foundation models** are the practical answer to
  the impossibility of centralizing AoU + UKB + BioVU + Optum for
  a single-instance FM. This paper is likely one of the first to
  demonstrate the design pattern at reasonable scale.
- Slots into the **federated / privacy-preserving EHR causal
  analytics** sub-thread (Jang et al. arXiv 2607.17958 lineage
  called out in `INTERESTS.md`) — same design pattern extended
  from causal analytics to generative modeling.
- Sits at the intersection of Knowledge Representation in EHRs
  (tokenization) + EHR FM architecture — a paper that touches
  both threads simultaneously.

**What to look for:**

1. **Federation topology** — FedAvg? FedProx? SCAFFOLD?
   Communication cost is the key practical constraint.
2. **Tokenization scheme** — MEDS-compliant? OMOP-concept-ID
   based? BPE-over-events?
3. **Benchmarking** — vs centralized CLMBR / FEMR / MOTOR
   baselines on a shared benchmark (EHRSHOT?).
4. **Privacy guarantees** — differential-privacy noise?
   Membership-inference-attack resistance?
5. **Site heterogeneity handling** — how does the model handle
   the OMOP-concept-drift and phenotype-prevalence-drift across
   participating sites?

**Cross-references:** ehr-foundation-models skill, waxse (AoU
pipelines), tam (PheTK / OMOP).

**Action:** Read the arXiv PDF. Compare against Jang et al. 2607.17958
federated causal analytics and against the centralized MOTOR / MEDS
lineage.

---

## METHODS-WATCH (worth a bookmark, but off your primary threads)

### M1. Foulkes et al. — IPW for auxiliary variable dependent sampling in Long COVID

- **arXiv:** 2608.04918v1 (`digests/2026-08-06.md`).
- **Design:** Methodological guidance for **two-phase sampling** in
  observational studies — the design pattern where selective
  testing / measurement based on auxiliary-variable values is
  used to enrich the analytic sample. Motivated by RECOVER Adult
  and Pediatric Long COVID cohorts.
- **Why worth watching:** Two-phase sampling is **ubiquitous in
  EHR studies** (selective genotyping, selective outcome adjudication,
  selective imaging) — this paper's IPW-based analytic framework
  translates directly to any EHR-cohort where the analytic subset
  is selection-dependent on prior EHR values.
- **Take-away for INTERESTS threads:** Portable technique for any
  AoU / UKB analysis where consent-to-genomics or Fitbit-enrollment
  induces a selection bias — pair the exposure-of-interest analysis
  with an auxiliary-variable dependent sampling correction.

### M2. Sasson et al. — Self-supervised DXA JEPA on UK Biobank

- **arXiv:** 2608.02208v1 (`digests/2026-08-04.md`).
- **Design:** Self-supervised joint-embedding predictive
  architecture (**JEPA**) applied to raw DXA scans — 11,540
  unlabeled Human Phenotype Project scans for training, 47,400
  UK Biobank DXA scans for external evaluation. Outperforms
  scanner-derived DXA measurements and general-purpose DINOv3
  on prevalent + incident disease prediction; 66% of incident
  hip arthrosis cases in the top-quartile of the LeDXA risk score
  (vs 41% for tabular measures). Biological-age gap tracks
  mortality hazard and is modifiable by HRT.
- **Why worth watching:** The **biological-age gap decreases in
  women after starting HRT** is a striking finding that directly
  ties into your HRT pharmacoepi active thread — a modifiable
  imaging biomarker for aging response to hormone therapy.
- **Take-away:** Even outside your primary imaging-genomics
  interest, the paper is a strong template for **imaging-embedding
  × PGS × EHR-outcome** composite-risk modeling in UK Biobank.

### M3. Krol et al. — Correlated frailty model for family-based rare-variant survival analysis

- **arXiv:** 2608.02127v1 (`digests/2026-08-04.md`).
- **Design:** Family-based **correlated frailty** model for
  survival outcomes with residual familial-component (kinship
  matrix) + region-specific IBD-probability-matrix random effects,
  for testing common SNPs, rare variants, or both, against
  time-to-cancer-onset.
- **Why worth watching:** Niche but well-scoped — for
  hereditary-cancer family cohorts (BRCA / Lynch / Li-Fraumeni),
  this is a technically correct alternative to unrelated-cohort
  SKAT / burden testing that respects the family structure.
  Directly portable to Lynch-syndrome cohort work.
- **Take-away:** Bookmark for any future family-based rare-variant
  survival analysis; not immediately actionable but the correct
  method to use if you enter that data regime.

---

## SKIP — surfaced but off-thread

From `arxiv-digest`:

- **Bouvier et al. (08-07)** — Treatment-effect heterogeneity
  discrimination metrics (theoretical, no EHR / biobank
  application).
- **Siu et al. THBKG (08-07)** — Temporal biomedical knowledge
  graph for target-disease advancement prediction (drug-development
  angle, not drug-repurposing with EHR loop).
- **Iluppangama & Abeywardana (08-07)** — STN-DBS long-term
  mortality in Parkinson's (single-institution 214-patient chart
  review, off-thread).
- **Qian et al. (08-07)** — E-bike route choice in Washington DC
  (obvious keyword-only match on "motor").
- **Datta et al. (08-07)** — Genomic language model representation
  analysis (methods-only, not tied to EHR / clinical questions
  you track).
- **Chauhan et al. (08-06)** — Causal forests for travel mode
  choice (transportation-planning application, off-thread).
- **Xu et al. (08-06)** — Regression-based proximal reconciliation
  of conflicting trials (methodological; interesting but not
  actionable for your threads).
- **Joshi (08-05)** — Formula 1 dirty-air causal analysis (obvious
  off-topic on "causal forest" + "debiased ML" keyword hits).
- **Maung & Zheng (08-05)** — IPW for group-testing surveillance
  (COVID-adjacent, off-thread).
- **Yin et al. CorePath (08-05)** — Breast pathology foundation
  model for CNB (pathology-imaging, not EHR-genomic).
- **Sharipov et al. (08-05)** — Autoregressive transformer for
  single-cell generation (single-cell FM, off your EHR-FM thread).
- **Hut & Masoero (08-04)** — AI-agent A/B test simulation for
  marketing (off-thread even though "foundation model" scored).
- **Xiong et al. (08-04)** — Contrastive pretraining for single-cell
  representations (off-thread).
- **Yu et al. (08-04)** — Bayesian latent transition for
  SWAN symptomatology-falls (menopause epi; off unless HRT-adjacent
  is upgraded to primary).
- **Falzone et al. IL-10 rs1800896 IBD biologics (08-07)** —
  candidate-gene-only pharmacogenomics for IBD biologic response;
  N=134 is too small to update the IBD pharmacoepi thread; note
  the direction (IL-10 variant → remission OR 2.15) but no action.

From Scholar alerts (off-thread but noted):

- Turco et al. PCWG4 editorial (bone-protective agents for
  bone-metastatic CRPC) — opinion piece, not new evidence.
- Markt et al. narcolepsy in AoU — SDoH + clinical outcomes in
  a specific disease, off primary threads.
- Ma et al. RModBlock ASO — RNA modification therapeutics, off-
  thread.
- Turco et al. / Kim et al. — LLM-collaboration / capable-language-
  models — off-thread for your EHR/genomics focus.
- Aali et al. medical text validation (npj Digital Medicine) —
  clinical-NLP validation, adjacent but not a claim-worth-
  citing update.
- Pushkov et al. hypophosphatasia NGS screening — rare disease
  screening, off primary rare-disease sub-threads.
- Zhang et al. pig long-read methylation — off-thread.
- Hilmarsson (already promoted to HIGH #8 above).

---

## What to do next (recommended reading order)

1. **Peng et al.** — the early-onset breast-cancer GWAS+PheWAS is
   the highest-signal-for-your-time item this week (medRxiv full
   text is free; direct overlap with your published work).
2. **Zhang et al. AoU wearable + MDD PRS** — the design template
   most directly reusable for a CFTR-modulator persistence + PGS
   × behavior sandbox in AoU CDRv9.
3. **Lu et al. prostate cancer PCSM** — Zeng-thread continuity;
   worth cross-checking whether it cites your prior work and
   whether the PRS is Conti-multi-ancestry-compatible.
4. **Noma TTE R package** — 30-min skim + one-hour hands-on
   install-and-run test; if it passes, this becomes your default
   pharmacoepi TTE tool.
5. **Ciardulli et al. functional PS on UKB** — read the assumption
   set carefully before committing; potential mid-term methods
   investment for CFTR / GLP-1 persistence work.
6. Hilmarsson LAI + Khan UMOD × PGS in parallel — both are
   composite-risk / ancestry-portability infrastructure that a
   later paper you write will likely need to cite.
7. Nadarajah AF screening + Burkhart federated EHR-FM — read after
   the top-five above; both are strong reference points for
   respective threads.

---

## Housekeeping

- No pull-request-worthy code changes surfaced this week — the
  reading is all upstream literature.
- `arxiv-digest` empty on 2026-08-08 (only "previously surfaced,
  suppressed" hits). This is expected — the pipeline dedupes
  aggressively.
- Next scheduled run of this report: whenever the following week's
  batch arrives (or on manual invocation via the same routine).

_Report generated by the automated research-triage routine
(`claude/brave-ride-b310k2` branch). Sources: `digests/2026-08-04.md`
→ `digests/2026-08-08.md`; Google Scholar author-feed alerts for
2026-08-07 and 2026-08-09; AoU keyword feed 2026-08-09._
