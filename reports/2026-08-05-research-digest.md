# Research digest report — 2026-08-05

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-08-01 12:35Z → 2026-08-05 12:00Z** (~4 days since the
last committed report at `reports/2026-08-01-research-digest.md`).
The window covers three NCBI My-NCBI batches per topic, three Scholar
alert cycles, and four arxiv-digest cron runs (08-02 empty; 08-04 and
08-05 dense; no 08-03 file).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-02.md`, `2026-08-04.md`, `2026-08-05.md`) | 08-02, 08-04, 08-05 (10:30Z crons) | Three daily runs. 08-02 empty (1 previously-seen suppressed). 08-04 surfaced 6 papers — two HIGH (Sasson LeDXA UKB DXA foundation model; Noma TTE R-package tutorial) and three METHODS-WATCH. 08-05 surfaced 5 papers — one HIGH (Ciardulli functional PS weighting on UKB BMI × T2D). |
| NCBI "My NCBI What's New" — AoU / UKB / drug repurposing | 08-02 17:55Z, 08-03 16:58Z, 08-04 15:21Z | Nine batches (three topics × three days). AoU: 1 + 0 + 4 = 5 items (all off-thread this window — signal reverting to baseline after the 07-30/07-31 spike). UKB: 10 + 0 + 15 = 25 items (three HIGH: Márquez-Luna omnicausal model, Domzaridou UKB harmonised outcomes, Vaura Estonian Biobank hypertension pharmacogenomics). Drug repurposing: 0 + 2 + 0 = 2 items (both off-thread — Zhong cross-population proteome-wide MR; Asiri antiviral docking). |
| Google Scholar author + keyword alerts | 08-03 04:32Z, 08-04 19:46Z, 08-05 05:27Z | **Three batches fired.** 08-03: 4 alerts (mostly off-thread; KG-ACE citation resurfacing across multiple author feeds). 08-04: 26 alerts — the largest batch of the window, with two HIGH items (Motsinger-Reif AoU polyexposure/polysocial/polygenic composite scores from the Denny author feed; Rahman opioid-overdose ML from the Zeng self-citation feed as a re-surface of the 07-31 NCBI item already written up in the 08-01 report). 08-05 morning: 11 keyword-alert digests (all incidental to the UKB / EHR / KG / rare disease keywords). |
| bioRxiv / medRxiv Subject Collection Alerts | daily | Aggregate feeds — individual on-thread preprints already surfaced upstream via NCBI. Not a separate net. |

> Caveat: NCBI emails include title, authors, journal, DOI, and PMID
> but no abstract text. The reports below contextualize that metadata
> against your research threads plus, where available, prior context
> from earlier reports; nothing here reflects full-text reading.
> `arxiv-digest` entries include the full abstract because the pipeline
> captures it.

---

## Executive summary (HIGH-priority studies, ranked)

Seven HIGH items surfaced in this 4-day window, clustering into three
knots. The volume is normal for a 4-day window (last report's 8 HIGH
items over 2 days was unusually dense due to the AoU-genetics
publication cluster; this window reverts to steady state, with
signal shifting from AoU discovery genetics to *methods and
infrastructure* — foundation-model DXA, target-trial-emulation
tutorials, functional-data causal inference, pharmacogenomic
prescribing outcomes, and a polyfactorial-architecture theory paper).

**Causal-inference & pharmacoepi methods (3 items).** The dominant
signal of the window.

1. **Ciardulli et al. arXiv 2608.03200 (08-05 arxiv-digest)** —
   Generalized functional propensity score weighting; applied to UK
   Biobank BMI trajectories → T2D risk and HbA1c trajectories. First
   scalable functional-PS estimator with a dual formulation. Directly
   extends target-trial-emulation to functional exposures.
2. **Noma arXiv 2608.01625 (08-04 arxiv-digest)** — Target Trial
   Emulation with the R Package `TTE`: tutorial and methodological
   guide. Two worked examples (SGLT2i vs DPP4i mortality; ARB vs CCB
   heart-failure hospitalisation with competing death). Directly
   plugs into the Tang / Hwang / Wang GLP-1 pharmacoepi cluster
   flagged in the 07-30 and 08-01 reports.
3. **Márquez-Luna, Tournaire, Rocheleau, Do, Verbanck — Genet
   Epidemiol 2026** — Omnicausal Model reveals highly polyfactorial
   nature of complex diseases. Framework paper for genetic
   epidemiology; sits with Baya AJHG polygenic-deviation and
   Souaiaia Nature PGS-tails as an architecture-of-complex-disease
   triad.

**All of Us composite risk (Denny lab) + Foundation-model biobank
phenotyping (2 items).** Both hit the PGS composite-risk sub-thread
and the EHR-linked-biobank thread.

4. **Motsinger-Reif, Lloyd, Akhtari, House, Patel, **Denny** et al.
   — Polyexposure, Polysocial, and Polygenic Scores for Common,
   Complex Disease Classification and the Creation of a Clinical
   Exposure Assessment** — Google Scholar Denny author-feed
   (08-04). AoU-native; the composite-score classification design
   directly serves the "PGS residuals / polygenic-deviation" and
   "composite risk models stacking PRS with rare pathogenic
   variants" sub-threads.
5. **Sasson, Levine, Shilo, Kohn, Lutsker, Godneva, Gabet, Krongauz,
   Weinberger, LeCun, Balestriero, Segal — LeDXA arXiv 2608.02208
   (08-04 arxiv-digest)** — Self-supervised DXA (JEPA) foundation
   model on Human Phenotype Project + UKB (n=47,400 external);
   incident hip / knee arthrosis + T2D prediction, biological-age
   gap tracking mortality, HRT modifies the age gap in women.

**Pharmacogenomics of medication side effects + EHR data
harmonisation (2 items).** Both are practical infrastructure /
sub-thread items rather than headline discovery.

6. **Vaura, Krebs, Kiiskinen, Rämö, Tamlander, Estonian Biobank,
   Rubinacci, Milani, Ripatti — Side effects in hypertension
   treatment: a pharmacogenomic analysis** — Eur Heart J 2026, PMID
   42545033. Directly on the "pharmacogenomic modifiers of
   medication persistence" sub-thread added to INTERESTS.md on
   07-29.
7. **Domzaridou, Lacey, Conroy, Allen, Li — Harmonised Health
   Outcomes Across Administrative Data: Lessons, Opportunities, and
   Challenges from UK Biobank** — Int J Popul Data Sci 2026, PMID
   42540745. Directly on the "Knowledge representation in EHRs and
   applications" thread (interoperability standards & their
   representational consequences sub-topic).

Six adjacent items sit in the METHODS-WATCH bucket:

- **Krol et al. arXiv 2608.02127 (08-04 arxiv-digest)** — correlated
  frailty model for family-based rare-variant + SNP tests on
  survival outcomes. Off your primary threads but worth logging for
  the family-cancer-cohort design pattern.
- **Peña-Tauber et al. Ann Neurol 2026** — Genetic modifiers of
  ABCA1 activity × APOE isoforms in Alzheimer's risk. Not on your
  disease threads, but the gene-modifier × isoform-context design
  is portable to APOL1 × G1/G2 modifier work.
- **Kanagasingam, Parlar, Liu, Gan-Or, Senkevich — Mov Disord 2026**
  — Rare-variant burden of dystonia genes in Parkinson's disease.
  Methods-watch for cross-phenotype rare-variant burden design.
- **Wu Y et al. Front Immunol 2026** — Multi-omics MR integrating
  GWAS + eQTL + mQTL + pQTL for nephrolithiasis (FXN). Off-thread
  disease but a well-executed 4-layer multi-omics MR pipeline.
- **Bate, Dong, Liu, Seviiri, Brown, Atkins et al. (Gusev-lab
  adjacent)** — Investigating repurposing potential of immune
  checkpoint inhibition via Mendelian randomisation. Drug-target-MR
  for oncology repurposing.
- **Xie H, Xue F, Wang X — Lifetime Data Anal 2026** — Transition
  dynamics modeling of pre-trained accelerometry representations
  for time to PD diagnosis. Pairs with the LeDXA paper as a
  "pretrained-representation-then-survival-model" design pattern.

---

## HIGH — full write-ups

### 1. Ciardulli, Fontana, Vantini, Ieva, *Generalized propensity score weighting for functional causal inference framework* — **arXiv 2608.03200 (08-05 arxiv-digest)**

**Feed:** `arxiv-digest` (`digests/2026-08-05.md`), score 4 (keyword
hits: uk biobank, biobank, propensity score, causal inference),
primary category stat.ME, submitted 2026-08-04.

**Why HIGH — methods-and-application together.** This is the
highest-scoring paper of the window (score 4) and it lands squarely
at the intersection of two of your active threads:

- **Causal inference and pharmacoepidemiology** — the paper extends
  propensity-score weighting from scalar treatments to *functional*
  treatments observed over a continuous domain. Their dual
  formulation yields a smooth unconstrained optimisation that
  scales to `p × L` rather than `n`, which is the practical bottleneck
  that has kept functional-PS methods out of biobank-scale pipelines
  until now.
- **Biobanks with EHR linkage: UK Biobank** — the application is a
  UKB analysis of the causal effect of **midlife BMI trajectories**
  on subsequent Type 2 Diabetes risk and glycated haemoglobin
  trajectories. Explicit contrast with Wainberg et al. 2019 (which
  used a single baseline BMI summary). This exact study design is
  portable to any longitudinal AoU / MVP / BioVU biomarker exposure
  where you'd otherwise collapse to a baseline scalar.

**Where it fits the causal-inference-methods lane.** Pairs with the
Ran et al. DR-FRL paper (07-31 arxiv, item 8 in the 08-01 report),
which handles the *representation* side of functional exposures for
doubly-robust estimation. Ciardulli et al. handles the
*propensity-score* side. Together the two papers now bracket the
functional-covariate causal-inference stack:

| Layer | Paper | Handles |
|---|---|---|
| Representation | Ran et al. DR-FRL (arXiv 2607.28567) | Encoding irregular functional histories into EIF-supporting states |
| Weighting | Ciardulli et al. (arXiv 2608.03200) | Functional propensity-score weights with scalable dual formulation |

Both should be tracked as complementary tools for the
`causal-inference-os` skill's reference stack.

**Actions.**
- Read Methods for the dual formulation. If the code is released
  alongside the preprint, add to the `causal-inference-os` skill's
  tool inventory next to `oci-agent` and DR-FRL.
- The BMI × T2D functional-exposure analysis is a direct template
  for a **CFTR-modulator persistence-trajectory × cystic-fibrosis
  clinical-outcome** analysis in future AoU / MVP work — modulator
  exposure is functional (persistence over time) rather than
  scalar, and the metabolic response is a functional trajectory
  itself.
- Also portable to **statin persistence-trajectory × CHIP acquisition**
  as an extension of the Carter et al. medRxiv paper (item 6 in the
  08-01 report) — where the current statin × CHIP MR uses a scalar
  ever/never exposure, the functional-PS approach would use the
  full persistence curve.

**Full abstract** (from arxiv-digest):

> Estimating causal effects in observational studies requires
> adjustment for confounding, a task that becomes challenging when
> the exposure is a function observed over a continuous domain
> rather than a scalar variable. We develop a functional propensity
> score weighting framework that achieves covariate balance by
> removing dependence between time-varying treatments and observed
> confounders, thereby enabling estimation of marginal causal
> effects in settings with functional treatments, covariates, and
> outcomes. We propose a dual formulation of the weight estimation
> problem that yields a smooth unconstrained optimization and
> improves computational scalability. The proposed framework
> extends naturally to settings with time-varying covariates and to
> longitudinal outcomes via a function-on-function marginal
> structural model, allowing estimation of causal effect surfaces.
> The proposed method improves covariate balance, estimation
> accuracy, and computational efficiency compared to the existing
> approach and retains these properties when extended to functional
> covariates and outcomes. We apply the method to data from the UK
> Biobank to estimate the causal effect of body mass index
> trajectories on the risk of Type 2 Diabetes and on subsequent
> glycated hemoglobin trajectories, a functional measure of
> metabolic status.

---

### 2. Noma H, *Target Trial Emulation with the R Package TTE: A Tutorial and Methodological Guide* — **arXiv 2608.01625 (08-04 arxiv-digest)**

**Feed:** `arxiv-digest` (`digests/2026-08-04.md`), score 2 (keyword
hits: target trial emulation, inverse probability), primary category
stat.ME, submitted 2026-08-03.

**Why HIGH — plug-and-play tutorial for the causal-inference
workflow you already run.** The paper is a self-contained
methodological guide + tutorial for the `TTE` R package for target
trial emulation on longitudinal observational data. It covers the
full pipeline in one document:

- Target-trial protocol construction (eligibility, treatment
  assignment, time zero, follow-up alignment)
- ITT vs per-protocol estimands
- Identification assumptions (all four: consistency, exchangeability,
  positivity, non-interference)
- Baseline and person-period data structures with temporal ordering
  for longitudinal weights
- Stabilised treatment + censoring weights, weight truncation
- Balance and effective-sample-size diagnostics
- Weighted pooled discrete-time survival models
- Model-based standardisation
- Competing-risk analysis
- Weighted Kaplan-Meier + Aalen-Johansen estimation
- Cluster bootstrap at the original-individual level

Two worked examples are directly on your pharmacoepi threads:

1. **SGLT2i vs DPP4i initiation with all-cause death** — the
   textbook glucose-lowering-drug TTE, and a direct template for
   the AoU / MVP GLP-1 pharmacoepi work in the 07-30 and 08-01
   reports (Tang BMJ hair loss TTE, Hwang AoU comparative
   effectiveness). The `TTE` package gives you a reproducible R
   implementation for the same class of analysis with the same
   diagnostic set.
2. **Sequentially nested ARB vs CCB with heart-failure
   hospitalisation and competing death** — extends the tutorial to
   the sequential-trials framework and to competing-risk endpoints.
   Directly portable to CFTR-modulator persistence with
   pulmonary-exacerbation hospitalisation and competing death.

**Where it fits the toolkit.** This becomes the recommended
tutorial reference for any target-trial-emulation manuscript methods
section. Alongside the Hernán textbook and the OHDSI CohortMethod R
package (see `ohdsi` skill), the `TTE` package is a more compact
alternative for one-off TTE analyses that don't need the full
OHDSI federated-network infrastructure.

**Actions.**
- Install and try `TTE` on a small AoU cohort to compare against
  CohortMethod outputs on a known analysis — start with
  metformin-vs-insulin all-cause mortality (matched published
  reference values from Hernán, González-González, Sabin — good
  ground truth) as a validation run.
- Add `TTE` to the `causal-inference-os` skill's R-package
  inventory next to `CohortMethod`, `WeightIt`, `MatchIt`,
  `survey`, `boot`.
- If your ongoing GLP-1 pharmacoepi work is being written up,
  cite this tutorial in the Methods section as the reference
  implementation for the discrete-time weighted pooled logistic
  model with cluster bootstrap SEs.
- Cross-reference against the OHDSI `Strategus` and HADES `TrialR`
  packages to check whether the diagnostic set here (particularly
  the ESS thresholds and truncation cutoffs) matches the OHDSI
  defaults.

---

### 3. Márquez-Luna, Tournaire, Rocheleau, Do, Verbanck, *The Omnicausal Model Reveals the Highly Polyfactorial Nature of Complex Diseases* — **Genet Epidemiol 2026;50(6):e70052 (PMID 42541367)**

**Feed:** NCBI My NCBI "UK Biobank" search (08-02 17:55Z batch, item 6/10).

**Why HIGH — architecture-of-complex-disease framework.** From the
Ron Do lab (Icahn Mount Sinai). Even without the abstract, the title
signals a **theoretical model paper** rather than a discovery result
— the "omnicausal" framing extends Boyle-Li-Pritchard's *Cell* 2017
"omnigenic" model to include **non-genetic causes**, positioning the
paper as a synthesis that reframes both PGS interpretation and
GWAS-hit prioritisation.

Why it hits your threads:

- **Genetic epidemiology** — sits directly with the
  polygenic-deviation / PGS-tails / GxE cluster added to
  INTERESTS.md on 07-29. If the omnicausal framing is correct, then
  PGS residuals and PGS-tails work (Baya AJHG 2026; Souaiaia
  *Nature* PGS-tails; Vazquez *Genetics* low-risk designs) inherit
  a natural interpretation: the residual variance is *not*
  environmental noise, it's polyfactorial signal from unmeasured
  causes.
- **Ron Do senior authorship** — Ron Do runs the Icahn
  Charles-Bronfman Institute for Personalised Medicine PheWAS lab
  and one of the strongest big-biobank genetic-epidemiology groups
  currently publishing. Verbanck is a strong senior methods
  co-author. Rocheleau is a long-time Do-lab statistical geneticist.
- **Genet Epidemiol venue** — signals a methodology-and-theory
  paper rather than a hypothesis-testing one, which is where you'd
  want a framework paper of this scope.

**Actions.**
- **Read end-to-end** as soon as the paper is available. This is
  the kind of framework paper that gets cited in every PGS or
  genetic-epidemiology intro paragraph for the next 2–3 years, and
  you'll want the citation live in your reference manager before it
  starts appearing in reviewer requests.
- Cross-check whether they cite Baya AJHG polygenic-deviation and
  the Nagpal & Gibson pervasive-GxE Nat Genet paper — if yes,
  those three together become the frame for the composite-risk /
  PGS-tails sub-thread in INTERESTS.md.
- Consider adding a paragraph to the `phewas-thinking` and
  `zeng-writing-style` skill glossaries defining "omnicausal" as
  the polyfactorial extension of Boyle et al.'s omnigenic model,
  so future manuscripts can use the term without redefining it
  each time.

---

### 4. Motsinger-Reif, Lloyd, Akhtari, House, Patel, **Denny** et al., *Polyexposure, Polysocial, and Polygenic Scores for Common, Complex Disease Classification and the Creation of a Clinical Exposure Assessment* — **preprint (Google Scholar Denny author-feed, 08-04)**

**Feed:** Google Scholar "Joshua C. Denny — new articles" (08-04 19:46Z batch).

**Why HIGH — Denny-lab AoU composite-score paper.** This paper
combines three score types into a single classification framework
on All of Us data — a direct hit on:

- **Genetic epidemiology composite risk sub-thread.** INTERESTS.md
  explicitly calls out "composite risk models stacking PRS with
  rare pathogenic variants." This paper generalises the composite
  framing beyond genetics to include *polyexposure* (environmental)
  and *polysocial* (social-determinants) scores. That's a natural
  extension of the composite-risk agenda — and one you'll want to
  understand before writing about PGS composite risk in AoU.
- **Biobanks with EHR linkage: All of Us.** AoU-native, Motsinger-
  Reif senior (NIEHS), Denny author, Chirag Patel (Harvard —
  exposome methodology) as a listed co-author. This is a
  cross-institutional AoU flagship analysis.
- **The "creation of a clinical exposure assessment" framing** is
  the interesting operational hook. It suggests the paper is
  proposing a *deployable* composite score for use in clinical
  workflows — which fits the ML-for-precision-health thread's
  weighting for "ML papers HIGH when they're tied to a clinical
  decision."

**Where it sits in the AoU composite-score landscape.** Compare
against:

- Kore et al. medRxiv (08-01 report item 4) — local-ancestry
  informed rare-variant burden testing on AoU admixed samples.
- Bujnis et al. Nat Genet Hashimoto's GWAS (08-01 report item 3) —
  multi-ancestry PGS for autoimmune thyroid.
- Ahn et al. Res Sq HLA architecture (08-01 report item 2) — HLA
  trans-ancestry disease risk in AoU.

Motsinger-Reif et al. sits at the *risk-scoring assembly* layer,
downstream from the discovery genetics (Bujnis, Ahn) and orthogonal
to the rare-variant methods layer (Kore).

**Actions.**
- **Read Methods first** to understand: (1) how polyexposure and
  polysocial scores were constructed on AoU (which data elements —
  survey, EHR-derived, geospatial imputed?); (2) how the three
  scores are combined for classification (concatenation? stacking?
  learned weighting?); (3) which disease outcomes were the test
  set.
- Because this is Denny-lab plus Chirag Patel plus AoU, this paper
  is going to be highly cited within the AoU community. Get it
  into your reference manager and Google Scholar profile-tracked
  citation network in the next 24–48 h.
- Consider whether the "clinical exposure assessment" score can be
  used as an adjustment covariate in your ongoing PheWAS work on
  AoU — if the composite score meaningfully absorbs SES / lifestyle
  confounding, it could tighten PheWAS effect estimates for
  disease outcomes where SES is a known confounder (e.g. cancer,
  cardiometabolic, mental health).
- Watch for the peer-reviewed follow-up — a Motsinger-Reif + Denny
  + Patel + AoU composite-score paper likely lands in *Nature
  Medicine* or *Nat Genet* or *JAMA*.

---

### 5. Sasson, Levine, Shilo, Kohn, Lutsker, Godneva, Gabet, Krongauz, Weinberger, LeCun, Balestriero, Segal, *Self-supervised DXA representations encode multi-system disease risk, biological aging and heritability* — **arXiv 2608.02208 (08-04 arxiv-digest)**

**Feed:** `arxiv-digest` (`digests/2026-08-04.md`), score 2 (keyword
hits: uk biobank, biobank), primary category cs.CV, submitted
2026-08-03.

**Why HIGH — foundation-model biobank phenotyping done right.**
The paper introduces **LeDXA**, a self-supervised JEPA-style vision
model trained on 11,540 unlabeled Human Phenotype Project DXA scans
and evaluated on **47,400 external UK Biobank scans**. The
architecture predicts latent representations rather than pixels
(the LeCun JEPA line — LeCun is a listed co-author) and beats both
scanner-derived DXA measures and DINOv3 despite ~150,000× fewer
training images and ~40× fewer parameters.

Why this hits your threads on multiple axes:

- **EHR foundation models** — the paper is a **domain-specialised
  foundation model** rather than a generic vision backbone.
  INTERESTS.md flags high interest in the CLMBR / MOTOR / EHRSHOT
  / MedTok / FEMR / MEDS lineage; LeDXA is that same design
  pattern applied to DXA imaging. The methodological choice —
  small, focused pretraining beats large generic pretraining on
  domain-specific downstream tasks — is directly relevant to how
  you'd critique or defend CLMBR-style EHR-FM pretraining budgets.
- **Biobanks with EHR linkage: UK Biobank** — 47,400 external UKB
  scans as the evaluation cohort; median 4.3-year follow-up for
  incident disease prediction (hip and knee arthrosis, T2D).
  Uses UKB longitudinal EHR outcomes as the evaluation set, which
  is exactly the pattern INTERESTS.md prioritises ("Methods papers
  using AoU / UKB / MVP / BioVU are high-priority").
- **Genetic epidemiology (heritability + GWAS)** — the paper
  reports that LeDXA embeddings are **more heritable** than
  DINOv3 embeddings, and that GWAS on the embeddings recovers
  mostly-known body-composition and bone-density loci. This is
  the increasingly-common "image-derived phenotype GWAS" pattern
  where the *embedding itself* becomes the GWAS trait. Directly
  relevant to the multi-omics-augmented PRS sub-thread and to
  future image-derived-phenotype PheWAS work on UKB CMR and DXA.
- **Biological aging + HRT** — the paper reports a **biological-
  age gap** (predicted-minus-chronological age from the embedding)
  that tracks broader disease burden, mortality (45% higher hazard
  in the oldest-appearing quartile), and — importantly —
  **decreases in women after starting HRT**. That HRT finding
  hits the hormone-replacement-therapy pharmacoepi thread from
  INTERESTS.md ("HRT persistence" and pharmacoepi drug-classes).
  The "biological-age gap as a modifiable HRT outcome" reframing
  is genuinely interesting.
- **Case-density hook.** "For hip arthrosis, 66% of incident cases
  occurred in the highest-risk quartile versus 41% for tabular
  measures." That's a big lift for a foundation-model biobank
  paper and gives a directly-quotable comparison metric to use in
  your own foundation-model methods sections when arguing for
  richer representations over tabular DXA readouts.

**Actions.**
- Read for four things in parallel: (1) the JEPA pretraining
  objective and how it compares to CLMBR-style masked-code
  autoregressive pretraining; (2) the incident-disease prediction
  calibration (they report top-quartile enrichment but not
  calibration curves — check the appendix); (3) the HRT
  biological-age-gap analysis — is it a naive comparison or a
  target-trial-emulation with propensity adjustment; and (4)
  whether they release LeDXA weights (would be an immediate
  candidate for UKB DXA-based PheWAS on AoU / UKB cohorts).
- Track whether the LeDXA-derived biological-age-gap trait gets
  used downstream by other groups as a **biomarker-as-exposure**
  in MR studies — this is exactly the kind of phenotype that
  gets rapidly picked up as an MR exposure once it's shown to be
  heritable and disease-associated.
- Consider a companion analysis: **PGS × LeDXA biological-age-gap
  interaction** as a test of the Nagpal & Gibson pervasive-PGS-×-
  exposure-interaction framing. If PGS effects on incident
  disease attenuate at high biological-age-gap (i.e., biological-
  age dominates), that's a testable hypothesis using LeDXA
  embeddings as the modifier.
- Add to the `beautiful-figures` skill's foundation-model biobank
  paper reference stack as a design template for pretraining-
  budget-vs-performance figures — the "150,000× fewer images, 40×
  fewer parameters, better performance" story is nicely made.

---

### 6. Vaura, Krebs, Kiiskinen, Rämö, Tamlander, **Estonian Biobank research team**, Rubinacci, Milani, Ripatti, *Side effects in hypertension treatment: a pharmacogenomic analysis* — **Eur Heart J 2026 (doi 10.1093/eurheartj/ehag575, PMID 42545033)**

**Feed:** NCBI My NCBI "UK Biobank" search (08-04 15:21Z batch, item 14/15).

**Why HIGH — direct hit on the pharmacogenomic-modifier-of-
medication-persistence sub-thread.** INTERESTS.md, updated on
07-29, added exactly this sub-thread:

> **Pharmacogenomic modifiers of medication persistence** —
> real-world discontinuation / MPR as an outcome modulated by
> CYP2D6 / metabolizer-phenotype PGx (Cohen et al. *Pharmaceuticals*
> 2026; Psy-PGx UKB lineage). Portable to CFTR-modulator
> persistence, statin discontinuation, HRT persistence, GLP-1 RA
> persistence.

This paper generalises that agenda to **antihypertensive side
effects** — a real-world outcome that plausibly modulates
persistence and adherence to blood-pressure medications, which are
the largest chronic-disease drug class by prescription volume.

- **Estonian Biobank as the primary cohort** — Ripatti-lab (Helsinki)
  + Estonian Biobank team, with Rämö and Kiiskinen as expected
  co-authors. The Estonian Biobank has one of the deepest linked-
  Rx-registry infrastructures in Europe, which makes it the best
  place in the world (with FinnGen) to run a side-effect × PGx
  analysis at scale.
- **Vaura & Ripatti seniorship** — Ripatti is the senior on this;
  his lab has been publishing high-quality pharmacogenomics-on-
  biobanks work for years. Vaura is a strong first author with
  prior CVD-genomics track record.
- **Rubinacci co-author** — Simone Rubinacci is a statistical-
  geneticist known for imputation and haplotype methods. His
  presence signals the paper has a strong technical GWAS /
  imputation backbone, likely for CYP2C9 / CYP3A4 / ACE / AGT /
  ADRB1 variant calling from array data.
- **Eur Heart J venue** — high-impact cardiology journal;
  positions the paper for clinical uptake by hypertension
  guideline committees.

**Where it fits.** This is the first published biobank-scale
pharmacogenomic analysis of *side-effect burden* (rather than
efficacy) for a major chronic-disease drug class. It complements
the Cohen et al. Pharmaceuticals 2026 CYP2D6 / Psy-PGx lineage
already cited in INTERESTS.md, and it's a template for:

- **CFTR-modulator side-effect pharmacogenomics** — modulator
  adherence in real-world CF cohorts (Trikafta / ivacaftor
  hepatotoxicity, mental-health side effects) modulated by PGx.
- **Statin persistence × PGx** — SLCO1B1 rs4149056 × statin
  myopathy is the classic case; extending to a broader statin
  side-effect PheWAS-on-AoU with CYP + SLCO annotations would be
  a natural follow-up.
- **HRT persistence × PGx** — CYP1A2 / CYP3A4 / SULT1A1 modifiers
  of oestrogen metabolism as candidates for HRT side-effect burden.

**Actions.**
- Read Methods for: (1) which side effects were the endpoint
  (electrolyte abnormalities? cough? angioedema? erectile
  dysfunction? postural hypotension?); (2) which variants were
  the exposure (CYP2D6 metaboliser status? SLCO1B1? ACE I/D?
  ADRB1 Arg389Gly?); (3) how persistence was operationalised
  (MPR, PDC, time-to-discontinuation).
- If the paper reports actionable PGx-variant × side-effect
  associations, cross-check whether the same variants are covered
  by the AoU short-read WGS PGx caller (PharmCAT / Aldy / StellarPGx
  — check the aou-workbench-2 skill for current recommended
  caller). Any hit that reproduces in AoU is a candidate for a
  short follow-up letter or replication note.
- Add to the pharmacoepi + PGx cross-reference list in the
  `causal-inference-os` skill's pharmacoepidemiology examples
  section, alongside the Cohen Pharmaceuticals 2026 CYP2D6
  citation.
- Consider whether the paper's design is directly portable to
  **GLP-1 RA persistence × PGx** — the AoU / MVP GLP-1 pharmacoepi
  cluster (Tang, Hwang, Wang from 07-30 / 08-01 reports) has not
  yet published a PGx-persistence arm; this is a natural next
  paper.

---

### 7. Domzaridou, Lacey, Conroy, Allen, Li Nuffield, *Harmonised Health Outcomes Across Administrative Data: Lessons, Opportunities, and Challenges from UK Biobank* — **Int J Popul Data Sci 2026;11(5):3675 (PMID 42540745, Free PMC article)**

**Feed:** NCBI My NCBI "UK Biobank" search (08-02 17:55Z batch, item 9/10).

**Why HIGH — direct hit on the Knowledge Representation in EHRs
thread.** INTERESTS.md, updated on 07-29, added a dedicated thread
for this class of paper:

> **Knowledge representation in EHRs and applications** — How
> structured and unstructured clinical data get encoded, aligned,
> and made computable — and what those representations enable
> downstream…
> - **Interoperability standards and their representational
>   consequences** — FHIR, USCDI, C-CDA, and how their design
>   choices shape what phenotypes are computable at national
>   scale (Lemieux et al. *JAMIA Open* 2026-07 as the reference
>   framing paper; N3C / OHDSI lineage).

Domzaridou et al. is the UK Biobank analogue of the Lemieux et
al. JAMIA Open framing paper — it addresses the same
representational-choice-and-downstream-use question, but from
inside the UKB group (Naomi Allen, Ben Lacey, Megan Conroy — the
core UKB Nuffield Department of Population Health epidemiology
crew).

Why this hits the thread:

- **The UKB harmonised health outcomes pipeline** underlies every
  single UKB paper that uses an "incident disease" endpoint. If
  you're going to run a PheWAS-on-UKB or a target-trial-emulation
  on UKB, the harmonised-outcome mappings from HES / SUS / SMR /
  PEDW / cancer registry / death registry / mental-health minimum
  dataset are the *ground truth* your ascertainment depends on.
  This paper documents the choices they made.
- **Cross-biobank portability.** The paper is explicitly about
  what UKB learned from harmonising outcomes across administrative
  sources. Every one of those lessons is potentially portable to
  AoU (which is still building out its equivalent harmonisation
  layer), MVP (which has VA-national administrative data with
  different quirks), and BioVU (which is single-site EHR without
  administrative data).
- **Free PMC article** — the paper is open-access, so it's
  citable in any UKB Methods section without paywall friction.
- **Neale et al. companion paper same-issue** (`Int J Popul Data
  Sci 11(5):3586`, PMID 42540803, from the same NCBI batch) —
  Identifying and linking individuals participating in multiple
  UK longitudinal population studies. The two papers together
  represent an infrastructure-paper cluster from IJPDS 11(5) on
  UK population-data linkage; worth reading as a pair.

**Actions.**
- **Read end-to-end** — this is an infrastructure paper that
  goes into your `writing-project-os` skill's "reference framing
  papers" list, alongside Lemieux et al. JAMIA Open 2026, N3C
  papers, and any OHDSI network-study infrastructure paper.
- Extract the specific outcome-harmonisation decisions
  (e.g., how they align cancer-registry vs HES vs death-registry
  cancer incidence; how they handle mental-health data from the
  MHMDS vs primary-care linkage) and add to the
  `ehr-phenotyping-os` skill's reference section on outcome
  ascertainment across administrative sources.
- Compare with the AoU harmonisation choices documented in the
  `aou-workbench-2` and `verily-workbench-aou` skills — if UKB
  and AoU are making incompatible choices for the same disease
  ascertainment (e.g., MI = ICD I21 only vs I21 + I22 + I23 +
  I24.1), that's a portability tax you'd want to know about
  before running a UKB → AoU replication.
- Consider drafting a short methods-glossary entry defining
  "harmonised health outcome" and citing this paper as the UKB
  reference definition — the term is used inconsistently across
  biobank papers and standardising your own use is worth 15
  minutes.

---

## METHODS-WATCH — brief write-ups

### M1. Krol, Rondeau, Choi, Briollais, *Correlated frailty model for analysis of genetic association in family studies* — **arXiv 2608.02127 (08-04 arxiv-digest)**

Family-based frailty model for jointly analysing common SNPs and
rare variants against survival endpoints in family cancer cohorts.
Uses kinship matrices + IBD-probability matrices for residual and
genomic correlation structures. Not on your primary threads (which
focus on unrelated biobank samples) but worth logging as an
alternative-design paper for the rare occasion you're asked to
review a hereditary-cancer-family paper.

### M2. Peña-Tauber, Hernández Arriaza, Reil, Muntaner, Park, Grenier-Boley, Hulsman, Amouyel, Bellenguez et al., *Genetic Modifiers of ABCA1 Activity Interact with APOE Isoforms to Mediate Alzheimer's Disease Risk* — **Ann Neurol 2026 (PMID 42548036)**

Multi-cohort European-consortium Alzheimer paper (EADI / GERAD /
Rotterdam / IGAP lineage). Design: **genetic modifiers of a
druggable pathway (ABCA1)** interacting with **isoform-context
variation (APOE ε2 / ε3 / ε4)** to modulate disease risk. Not on
your disease threads, but the design pattern is portable to
**APOL1 G1/G2 risk modifiers × ancestry-context** work, which is
a live INTERESTS.md thread. Worth an abstract read for the
statistical framing.

### M3. Kanagasingam, Parlar, Liu, Gan-Or, Senkevich, *Rare-Variant Burden Analysis of Dystonia Genes in Parkinson's Disease* — **Mov Disord 2026 (PMID 42541459)**

Cross-phenotype rare-variant burden testing (dystonia genes tested
in a PD cohort). McGill group (Gan-Or lab). Not on-thread as a
disease, but the "test disease-A genes in disease-B cohort" design
is directly the pattern used in hereditary-cancer × PheWAS work,
which is on your INTERESTS.md active threads. Log for design
reference.

### M4. Wu Y, Ye S, Li P, Wu Z, Guo Z, Bian J, Sheng M, Lai D, *Multi-omics Mendelian randomization integrating GWAS, eQTL, mQTL and pQTL data prioritizes mitochondrial gene FXN as a hypothesis-generating candidate for nephrolithiasis* — **Front Immunol 2026 (PMID 42548648, Free PMC article)**

Four-layer multi-omics MR pipeline (GWAS + eQTL + mQTL + pQTL) as
a target-prioritisation framework. Off-thread disease
(nephrolithiasis) but a well-executed multi-omics-MR reference
implementation. Compare against the Liu et al. Front Pharmacol
diabetic retinopathy druggable-MR from the 08-01 report (M2 in
that report). Both are candidates for the "reference implementations
of multi-omics MR" list in the `causal-inference-os` skill's
Mendelian randomisation section.

### M5. Bate, Dong, Liu, Seviiri, Brown, Atkins et al., *Investigating the repurposing potential of immune checkpoint inhibition for cancer treatment using Mendelian randomisation* — **preprint (Google Scholar Sasha Gusev author-feed, 08-04)**

Drug-target MR for immune checkpoint blockade in oncology
repurposing. Directly on the drug-repurposing thread's
"causal-inference framings of off-label use (target-trial
emulation of repurposing candidates)" sub-topic. Worth reading
for the target-selection methodology — immune checkpoint
inhibitors are a natural test case because the target biology
(PD-1, CTLA-4, LAG-3) is well-characterised and the drugs are
FDA-approved for defined cancer indications, so any predicted
off-label indication has clear translational read-outs.

### M6. Xie H, Xue F, Wang X, *Transition dynamics modeling of pre-trained accelerometry representations for time to diagnosis of Parkinson's disease* — **Lifetime Data Anal 2026;32(3):45 (PMID 42545552)**

Wearable-data foundation-model → survival endpoint. Pairs with the
LeDXA paper above as a "pretrained-representation-then-survival-
model" design pattern for chronic disease incidence prediction
from biobank data. Off-thread as a disease (PD), but the
methodological approach — pretrained accelerometry representations
+ transition-dynamics survival modelling — is directly portable to
UKB Fitbit + AoU wearable substudies for other chronic diseases.
Log for the ML-for-precision-health thread's reference list.

---

## Off-thread (recorded, no write-up)

**Arxiv-digest off-thread (08-04, 08-05):**
- Hut & Masoero — AI Agents simulate A/B test outcomes (marketing
  A/B tests, not clinical).
- Xiong et al. — contrastive pretraining for single-cell
  transcriptomics (off your specific threads).
- Yu M et al. — Bayesian joint modelling of longitudinal symptom
  responses and falls in SWAN. Design is nice (latent transition
  model + additional clustering layer + joint modelling with
  outcome) but SWAN cohort and falls outcome are both off-thread.
- Maung & Zheng — group testing with retesting for causal
  inference (public-health-surveillance design; off your specific
  threads).
- Joshi — Formula 1 dirty-air causal analysis (impressive
  Causal-Forest / DML application, but F1 racing is off-thread by
  a wide margin).
- Yin et al. CorePath — breast-specialised pathology foundation
  model for CNB. Off-thread as a disease (breast pathology
  imaging) but the domain-specialised-foundation-model + conformal-
  risk-control design is worth a mention alongside the LeDXA paper
  as a same-week domain-specialised-FM example.
- Sharipov et al. — autoregressive transformer for single-cell
  generation, scaling law.

**All of Us feed off-thread (08-02, 08-04):**
- Zimmer K — Nature commentary on peer review (not research).
- Lv Q et al. — bearing fault diagnosis engineering paper
  (mistagged AoU search hit).
- PLOS Genet Staff — Correction to earlier Meta-evolutionary exome
  analysis T2D paper (already surfaced; not a new result).
- Chen J et al. — Bruceine A alcoholic liver disease preclinical
  pharmacology (off-thread).
- Kim M et al. — grief framing model neurosurgery (off-thread).

**UK Biobank feed off-thread (08-02, 08-04):**
- Davies NL et al. — anxiety symptoms after ART (systematic
  review, off-thread).
- Xie S et al. — SES × atrial fibrillation MR (small, off-thread).
- Candussi CJ et al. — vegetarian diet × CKD (nutrition
  epidemiology, off-thread).
- Raisi-Estabragh, Petersen, Neubauer — 10 years of UKB CMR
  study (Circulation review — worth flagging but off your
  specific threads; useful reference for a review section on
  biobank imaging-derived phenotypes).
- Krost KM et al. — ultra-processed food × hypertension (nutrition
  epi).
- Auger et al. — APOB / estimated APOB ratio for APOE2 screening
  (clinical chemistry).
- Zhang Z et al. comment on deficit accumulation frailty × CKD
  (letter, no abstract).
- Chen Q et al. CRP-TyG index cardio-renal-metabolic multimorbidity
  in UKB + CHARLS (multimorbidity thread hit but too general;
  logging for record only).
- Kim NJ et al. GWAS subcortical aging (Geroscience — brain-aging
  paper, off-thread).
- Hu P et al. lifestyle × metabolomic signatures × T2D transitions
  (metabolomics epi).
- Shouma et al. diabetic arterial transcriptome (RNA-seq).
- Zhao X et al. water hardness × MASLD gene-environment
  (nutrition-adjacent GxE, off-thread).
- Luan S et al. insulin resistance × vitamin D (nutrition epi).
- Gao M et al. sarcopenia × infectious diseases (large-cohort
  descriptive epi).
- Peña-Tauber et al. ABCA1 × APOE — logged in METHODS-WATCH M2.
- Zhong H et al. cross-population proteome-wide MR CVD — logged
  in METHODS-WATCH cluster as a multi-omics MR reference.

**Drug repurposing feed off-thread (08-03):**
- Asiri M et al. — ganciclovir / acyclovir docking against RSV
  nucleoprotein (in silico screening, off-thread).

**Google Scholar 08-05 morning batch (keyword feeds — all
off-thread as individual items):**
- Sachdeva et al. AI in CVD prevention (review).
- Guo J et al. IBD × ankylosing spondylitis MR + meta-analysis
  (redundant with prior IBD literature).
- Chen Q et al. CRP-TyG UKB (dup with NCBI feed).
- Velardi et al. autoimmune polyendocrine syndromes in T1D
  (case series).
- Mirchandani — Population and Evolutionary Genomics thesis
  (mistagged AoU hit).
- Singh R et al. Molecular autopsy in unexplained sudden death
  (meta-analysis — worth noting as an ACMG-yield paper; not on
  your specific disease threads).
- Qureshi — PROJECT ERDAM rare disease early warning framework
  (proposal, not a research result).
- Huerne K et al. simulated EHR summative assessment (medical
  education RCT).
- APOL1 alert — "PROJECTS & COLLABORATIONS" newsletter, no
  research result.
- Ma Y et al. neural-symbolic temporal KG reasoning (KG methods
  but for general reasoning, not biomedical).
- De Souza et al. nanoformulated triclabendazole for
  neurocysticercosis (drug delivery, off-thread).

**Google Scholar 08-04 evening batch (author feeds — off-thread
individual items):**
- Ao X et al. — exome-wide association of chronic pain in UKB
  (large scale, but chronic pain off your specific disease
  threads).
- Liu S et al. Nat Genet 2026 — GWAS of gestational phenotypes
  (Kanai co-author). METHODS-WATCH adjacent — context-specific
  genetic effects framing is interesting but off your specific
  threads.
- Chen X et al. Lyme disease post-infectious autoimmunity
  (infectious immunology).
- Costa & Penadés Molecular Cell perspective on AI in molecular
  biology (opinion piece).
- Carriere et al. TRIM21 inflammasome pathology (immunology).
- Chen X et al. X-chromosome L1 mutagenesis Science paper
  (Denny citation feed, but the paper itself is genome-biology
  not on-thread).
- De los Rios Barreda et al. XCI × L1 mutagenesis Science
  (same paper).
- Dearman AR et al. medRxiv — polygenic indices of neuropsychiatric
  conditions in four UK samples (PGS validation; adjacent to
  composite-risk work but not on your specific disease threads).
- Kamyab TIA / stroke AoU (already noted in 08-01 report as
  off-thread).
- Ma / Sun / Shan neural-symbolic KG (KG reasoning, off-thread).
- Wang JC et al. Cell brain vasculature atlas (spatial-omics,
  off-thread).

**Other 08-03/08-04 alert clusters (already covered above or
off-thread):**
- KG-ACE (Sun et al. Information Processing & Management 2027) —
  appeared across three different Scholar author feeds (Lu,
  Callahan, "knowledge graph" keyword). Off-thread as a
  general-medical-reasoning KG paper without a specific
  biomedical-KG contribution.

---

## Cross-report continuity notes

- **AoU multi-ancestry OUD GWAS (Gu et al.)** — no fresh
  re-surface this window (was resolved in 08-01 report). Still
  on the reading queue.
- **Streit et al. Nature Genetics BPD GWAS + BPD-PheWAS** (07-23
  report) — no re-surface. Still on the reading queue.
- **Baya et al. AJHG polygenic-deviation** (07-23 report) — no
  re-surface directly, but the **Márquez-Luna omnicausal-model
  paper (item 3 above)** now provides the theoretical framework
  that PGS-tails / polygenic-deviation / PGS-residuals designs
  are exploring empirically. Consider reading Baya + Márquez-Luna
  together as a paired theory-and-empirical mini-cluster.
- **DRIVE v3** (Bastarache lab, 07-23 report) — no re-surface.
  Still on the reading queue.
- **Lemieux et al. JAMIA Open EHR interoperability** (07-23 and
  07-30 reports) — the **Domzaridou UKB harmonised outcomes
  paper (item 7 above)** is the UKB-side companion to Lemieux
  (US-side interoperability); the two together bracket the
  transatlantic representation-of-EHR-outcomes literature.
- **Chou et al. `oci-agent` + Ran et al. DR-FRL** (07-27 arxiv,
  07-31 arxiv, 07-30/08-01 reports) — now joined by
  **Ciardulli et al. functional-PS (item 1 above)** and
  **Noma TTE R package (item 2 above)** as a four-paper
  causal-inference-methods mini-cluster:

  | Paper | Contribution |
  |---|---|
  | Chou `oci-agent` (07-27) | Agentic workflow orchestrating covariate balance / trimming / sensitivity |
  | Parikh/Volfovsky (07-28) | RCT estimator selection framework |
  | Ran DR-FRL (07-31) | Functional-representation learning for DR estimators |
  | Ciardulli fPS (08-05) | Functional propensity-score weighting with scalable dual formulation |
  | Noma TTE R package (08-04) | Practical R-package tutorial for the standard TTE workflow |

  Together these five papers now form a **modern causal-ML on EHR
  data toolkit** worth having in the `causal-inference-os` skill's
  reference stack.

- **Tang / Eze / Hwang / Wang GLP-1 pharmacoepi cluster** (07-30
  and 08-01 reports) — no direct re-surface this window, but the
  **Noma TTE R-package paper (item 2)** provides the R
  implementation that any GLP-1 TTE follow-up would use, and the
  **Vaura Estonian Biobank hypertension PGx paper (item 6)** is
  the direct template for a future GLP-1-persistence-×-PGx paper.
- **Bujnis et al. Nat Genet Hashimoto's GWAS** (08-01 report,
  Zeng co-author) — no additional citation surfacing yet, but
  Scholar author-feed citation tracking should pick it up within
  1–2 weeks.
- **GraphRareBench** (07-29 arxiv, 07-30 report) — clone-and-run
  action item still open.
- **Carter et al. medRxiv statin × CHIP MR** (08-01 report, item 6
  — highest-value read of last week) — no re-surface this window.
  Should be a top-priority read this week.

---

## Suggested next actions

1. **Read Ciardulli et al. functional PS (arxiv-digest 08-05) and
   Noma TTE tutorial (arxiv-digest 08-04) as a causal-inference
   methods pair.** Together they extend the toolkit you use for
   AoU / UKB pharmacoepi to functional exposures (Ciardulli) and
   to a lower-friction R-package workflow (Noma). Both are
   directly-actionable methods reads.
2. **Read Márquez-Luna, Do, Verbanck omnicausal-model paper
   (Genet Epidemiol).** Framework paper of the year for
   architecture-of-complex-disease — get it read before it starts
   appearing in reviewer requests. Cross-reference with Baya AJHG
   polygenic-deviation to see whether the omnicausal model
   provides the theoretical basis for PGS-residual discovery
   designs.
3. **Read Motsinger-Reif / Denny / Patel AoU polyexposure /
   polysocial / polygenic composite-score paper.** Directly on
   your composite-risk sub-thread. Extract the score-construction
   choices and consider whether the composite score is a useful
   adjustment covariate in your ongoing PheWAS-on-AoU work.
4. **Read Sasson et al. LeDXA (arxiv-digest 08-04).** JEPA
   foundation model on DXA with UKB external validation. Read for
   the incident-disease-prediction methodology, the biological-age-
   gap × HRT finding, and the GWAS-of-embedding heritability
   claim. Track for a released-weights follow-up (would enable
   immediate downstream use on AoU DXA if AoU adds DXA imaging
   to future CDR releases).
5. **Read Vaura et al. Estonian Biobank antihypertensive
   pharmacogenomics (Eur Heart J).** Directly on the
   pharmacogenomic-persistence sub-thread. Use as a template
   design for a future GLP-1-persistence-×-PGx or CFTR-
   modulator-persistence-×-PGx paper.
6. **Read Domzaridou et al. UKB harmonised health outcomes
   (Int J Popul Data Sci, Free PMC).** Infrastructure paper for
   the knowledge-representation-in-EHRs thread. Extract the
   harmonisation choices and reconcile against the AoU / MVP /
   BioVU equivalents. Read alongside Neale et al. same-issue
   linkage paper.
7. **Backlog priority order** for last week's HIGH items that
   still need reading: (a) Carter et al. medRxiv statin × HMG-CoA
   MR × CHIP (highest single-item value of the prior window),
   (b) Gu et al. AoU multi-ancestry OUD GWAS, (c) Ahn et al. AoU
   HLA architecture, (d) Kore et al. medRxiv local-ancestry burden
   testing.
