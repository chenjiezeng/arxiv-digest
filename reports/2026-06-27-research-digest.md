# Research digest report — 2026-06-27

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-06-27** (seven days since the prior
2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 06-27 | Large 06-27 batch (~30 author-feed alerts: **Chenjie Zeng self-feed**, Bastarache×2, Denny×2, Hripcsak×2, Hernán, Yang×2, Pritchard, Montgomery×2, Szolovits, Callahan, Zitnik, Shendure, Karczewski, Kastner×2, Chute×2, Daly, Patrick Ryan, Pascal Brandt, Natarajan, Luo). Lighter mid-week tail. One promotional digest (alphaXiv "Autoresearch for arXiv Papers", 06-24) — infrastructure, not research. |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 06-27 | **06-23 = 2 papers** (one on-thread CF causal-inference paper; one off-thread motor-neuron paper); **06-24 = 0 papers, 3 of 4 categories failed**; **06-25 = 2 papers** (foundation-model microbiome paper + federated tensor-decomposition paper); **06-26 = 1 paper** (neuro-symbolic AMR KG); **06-27 = 0 papers** (1 suppressed dup). See pipeline note below. |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |

> ⚠️ **`arxiv-digest` 06-24 had the same 3-of-4-category fetch failure
> as 06-20** (`q-bio.GN`, `q-bio.PE`, `stat.AP` all failed; only
> `q-bio.QM` returned). The 06-20 report flagged this and recommended
> jittered retry-with-backoff or doubling the inter-category pause; the
> repeat instance four days later confirms the issue is *not* a one-off
> arXiv-side hiccup but the new client-delay + inter-category-pause
> tuning is still being hit by arXiv's rate limiter on roughly weekly
> cadence. See the pipeline section.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a *deviation-from-polygenic-expectation*
  paper that lands directly on the PRS + rare-variant composite-risk
  thread and saturates 6+ Scholar feeds.** Baya, Lassen, Hill,
  Venkatesh, Currant et al. — *Individuals who deviate from polygenic
  expectation are enriched for damaging variants in genes linked to
  rare disease* (*American Journal of Human Genetics*, 2026, S0002-9297
  (26)00200-4). Surfaces simultaneously in **your own Chenjie Zeng
  new-related-research feed**, Lisa Bastarache, Joshua C. Denny (×2 —
  related-research and 10 new citations), George Hripcsak (10 new
  citations), and Jian Yang (related-research). The single highest-
  saturation paper of 2026 H1 so far, and the conceptual content is
  *exactly* on the INTERESTS-file thread "composite risk models stacking
  PRS with rare pathogenic variants." Operationally: identify
  individuals whose observed phenotype deviates from PRS-expected
  phenotype, then show those "misaligned" individuals are enriched for
  damaging variants in rare-disease genes — i.e., **PRS-residuals as a
  rare-variant prioritization screen**. **Read first.**
- **Cystic-fibrosis causal-inference paper from arxiv-digest is the
  cleanest single on-thread `arxiv-digest` hit this month.** Murali,
  Barnatchez, Hoppe, Wagner, Keller, Josey — *Causal Inference with
  Multiple Misclassified Exposures: A Control Variate-Adjusted
  Calibration Weighting Approach* (arXiv 2606.23656, stat.ME,
  surfaced 06-23). Two-keyword match: `causal inference` + `cystic
  fibrosis`. Applied to a 651-patient pediatric CF cohort to estimate
  the causal effect of *P. aeruginosa* vs *S. aureus* on
  percent-predicted FEV₁, comparing swab- vs sputum-based exposure
  classification. **HIGH** — sits squarely on three INTERESTS threads
  (causal inference + CF disease thread + EHR-derived exposure
  misclassification, which is the everyday biobank problem when
  defining exposures from claims/codes vs gold-standard structured
  fields).
- **Low-dose lithium vs valproate, incident-dementia propensity-matched
  cohort using EHR data.** da Silva, Santos, Júnior, Camacho et al. —
  *Low-Dose Lithium vs Valproate and Incident Dementia Diagnoses in
  Older Adults: A Propensity-Matched Cohort Study Using Electronic
  Health Record Data* (2026, surfaced in *Pascal Brandt — new related
  research* feed). Active-comparator design (lithium vs valproate, both
  mood stabilizers, both prescribed in older adults — head-to-head
  controls for confounding-by-indication) with propensity matching on
  EHR-derived baseline covariates and incident-dementia outcome
  ascertainment from EHR. **HIGH** on the causal-inference /
  pharmacoepi thread + active-comparator design template directly
  applicable to your GLP-1 / SGLT2 / HRT drug-class work.
- **Timing of antidiabetic medication initiation and cardiovascular
  outcomes, JAMA Network Open.** Ko, Shin, Jung, Bea, Hong, Noh, Bae et
  al. — *Timing of Antidiabetic Medication Initiation and Risk of
  Cardiovascular Events and Mortality* (*JAMA Network Open*, 2026,
  surfaced in *Miguel Hernán — 10 new citations* feed). Drug-class-
  initiation-timing analysis directly on the target-trial-emulation
  template (early-vs-late-treatment within a defined eligibility
  window). The citation to Hernán is the tell that this is using TTE
  methodology rather than naive cohort comparison. **HIGH on the
  GLP-1 / SGLT2-class TTE thread** if antidiabetic class includes
  either, which it almost certainly does given the framing.
- **Integrating social determinants of health and genetic risk in
  disease risk models, AJHG.** Biji, Ferar, Pejaver, Kenny, Liu, Asgari
  — *Integrating social determinants of health and genetic risk in
  disease risk models* (*American Journal of Human Genetics*, 2026,
  surfaced in *Joshua C. Denny — new related research* and *4 new
  citations to articles by Lisa Bastarache*). EE Kenny senior-authored,
  AJHG venue, dual EHR-FM-grandee saturation. Directly on the genetic
  epi + EHR-linked biobank thread and one of the cleaner
  operationalizations of SDoH-by-PRS interaction in EHR cohorts.
  **HIGH.**
- **Co-expression-based TWAS gains in schizophrenia.** Rossi, Sportelli,
  Kikidis, Grassi, Di Carlo et al. — *Co-expression-based models
  improve eQTL predictions for transcriptome-wide association studies
  and highlight new schizophrenia-associated genes* (2026, surfaced in
  *Jonathan K. Pritchard — 10 new citations* feed). On the genetic
  epidemiology / TWAS thread. The co-expression-augmented TWAS is the
  modern second-generation TWAS framing (PrediXcan + S-PrediXcan + co-
  expression layer); useful for any AoU / UKB TWAS scaffold you're
  building. **HIGH on the genetic-epi TWAS sub-thread; METHODS-WATCH
  on the variant-interpretation thread.**
- **LLM-based physical-activity extraction from EHR.** Yang, Niu, Li,
  Zhou, Xiao et al. — *Benchmarking information extraction of physical
  activity from electronic health record with large language models:
  an natural language processing pipeline and …* (2026, surfaced in
  both *Tiffany J. Callahan — new related research* and *George
  Hripcsak — new related research* feeds — dual EHR-NLP feed
  saturation). Directly on the **EHR phenotyping & OMOP** thread, sub-
  axis "NLP / LLM extraction from clinical notes for phecode and HPO
  term assignment." Physical activity as an EHR-extracted lifestyle
  exposure is also methodologically interesting because it sits
  between structured (vital-sign-adjacent) and unstructured (note-
  embedded) — a clean LLM-extraction benchmark. **HIGH.**
- **Cell-type-resolved noncoding variant effects in human immunity,
  medRxiv.** Liu, Zhang, Zhu, Wang, Zhang, Zhang et al. — *In vivo
  measurement and prediction of cell-type-resolved non-coding variant
  effects in human immunity* (medRxiv, 2026, surfaced in *9 new
  citations to articles by Stephen B. Montgomery* and *10 new citations
  to articles by Jian Yang*). Pairs with the 06-20 report's Marderstein
  et al. *Nature Genetics* noncoding-variant paper — the same week's
  citation network is converging on cell-type-resolved noncoding
  interpretation as the new reference class for variant interpretation.
  **HIGH on the variant-interpretation thread.**
- **PGS Browser, Nature Communications.** Kolosov, Reeve, Briotta
  Parolo, Kurki et al. — *PGS Browser: a public platform for
  personalized polygenic score analysis and interpretation* (*Nature
  Communications*, 2026; surfaced in **your own Chenjie Zeng feed**
  and *Mark Daly — new articles*). FIMM / FinnGen-lineage public PGS
  platform with population reference distribution. Daly co-authorship
  + self-feed surfacing makes this a default citation for any future
  AoU- or MVP-scale PRS-translation write-up. **HIGH** on the PRS
  thread.
- **Distinct genetic architecture in the tails of complex traits —
  *Nature*, carry-forward.** Souaiaia, Wu, Ori, Choi, Hoggart et al.
  (*Nature*, 2026, *Stephen Montgomery — new related research* —
  re-fired on 06-27). **Already covered in detail in the 06-20
  report (HIGH #4).** Listed here only to note that the Scholar
  related-research engine re-surfaces high-relevance papers when they
  get cited; this is one of the highest-precision signals available.
  See 06-20 report for the detailed action items.
- **Three more single-feed HIGH-adjacent items worth a glance** —
  Chiang et al. cluster-RCT for cascade testing in hereditary cancer
  (JCO 2026, Chenjie Zeng self-feed); Tarhini et al. PRS for immune-
  related thyroiditis in melanoma ICI (JITC 2026, Chenjie Zeng self-
  feed); Curation of a Cardiology Interface Terminology with ML
  (arXiv 2606.×, Patrick Ryan related-research). See METHODS-WATCH
  section for triage.

Counts: **9 HIGH (one carry-forward)**, **6 METHODS-WATCH**, rest SKIP.
This is a higher-than-average HIGH count, driven by the AJHG-week
saturation (Baya tails-of-PRS, Biji SDoH-x-genetic-risk, and the
Nature Communications PGS Browser all surfacing in the same window) and
by the unusually strong `arxiv-digest` 06-23 hit (Murali CF causal-
inference, two-keyword match including a disease thread).

---

## HIGH priority — detailed reports

### 1. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
- **Authors / venue:** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh,
  H. Currant et al. — *American Journal of Human Genetics*, 2026
  (S0002-9297(26)00200-4; cell.com/ajhg/fulltext/S0002-9297(26)00200-4).
- **Surfaced by:** **Six-feed saturation** — (a) *Chenjie Zeng — new
  related research* (**your own feed**), (b) *Lisa Bastarache — new
  related research*, (c) *Joshua C. Denny — new related research*,
  (d) *10 new citations to articles by Joshua C. Denny*, (e) *10 new
  citations to articles by George Hripcsak*, (f) *Jian Yang — new
  related research*. Six-feed firing is the highest saturation
  observed in this digest's history; surpasses the 06-20 triple-feed
  reports. The fact that it hits *both* related-research and citations
  feeds for Denny means he's already cited it in 2026.
- **Thread:** **Genetic epidemiology / PRS** (deviation-from-PRS
  framing) **+** **Variant interpretation / ACMG-ClinGen** (rare-disease
  damaging-variant enrichment) **+** **Composite risk models stacking
  PRS with rare pathogenic variants** (this thread is the single
  closest match in the INTERESTS file) **+** **Rare disease**
  (rare-disease genes as the enrichment target).
- **What it is:** From the snippet: "Polygenic scores (PGSs) stratify
  disease risk but often fail to capture individual variation.
  'Misaligned' individuals, whose observed phenotypes deviate from
  their genetically expected values based on PGS, provide a powerful
  model for identifying [rare-variant contributions]." Operationally:
  fit PGS → phenotype regression in a large biobank, compute residuals,
  flag tails of the residual distribution as "misaligned," then test
  whether misaligned individuals are enriched for damaging variants in
  rare-disease gene panels. The framing inverts standard PRS use —
  rather than using PRS to *predict* phenotype, it uses PRS-residuals
  as a **rare-variant prioritization screen**. The expected paper
  structure is (i) define misalignment in a discovery biobank (likely
  UK Biobank given the FinnGen-adjacent author pattern, or possibly
  AoU), (ii) sequence or pull WES on the misaligned tails, (iii) test
  rare-variant burden against gene panels (likely Mendelian gene
  panels from PanelApp or OMIM Morbid).
- **Why it matters to you:** Five converging hits.
  (a) **Direct match to your composite-risk thread.** The INTERESTS
  file explicitly names "Composite risk models stacking PRS with rare
  pathogenic variants" as a target. This paper is one of the cleanest
  operationalizations of that idea — not a *sum* of PRS and pLoF
  burden (the usual stacking approach) but a *conditional* model
  where PRS-residuals drive the rare-variant search. The conditional
  framing is methodologically tighter because it avoids the double-
  counting problem when a variant contributes to both the PRS and the
  rare-variant burden score.
  (b) **Self-feed firing.** Paper appears in your own Scholar related-
  research feed, which Google's relevance model only triggers when
  the new work is close to your published corpus. Six-feed saturation
  with self-feed inclusion is the highest-signal pattern available.
  (c) **Pairs with the Souaiaia tails-of-PRS paper from 06-20.**
  Souaiaia argues that the *genetic architecture* of PRS tails
  differs from the bulk; Baya argues that the *phenotypic-deviation*
  tails of PRS-by-phenotype regression are enriched for rare-variant
  effects. Together these compose into a coherent argument: PRS is
  miscalibrated at the tails *because* tails are partly driven by
  rare variants the PRS doesn't see. This is now a publishable
  citation pair.
  (d) **Operational fit for AoU / UKB / MVP.** All three biobanks now
  have WES at scale and rich phenotype data, so the misalignment-
  enrichment design is directly portable. AoU's underrepresented-
  population enrichment makes it especially useful for testing
  whether the misalignment-rare-variant signal generalizes across
  ancestries — which is the obvious cross-ancestry-portability
  extension.
  (e) **Rare-disease gene panel methodology overlap.** Your INTERESTS
  file lists rare-disease (HPO-based deep phenotyping) as a thread;
  the gene-panel-enrichment test is the standard tool, and this paper
  is likely a methodological reference for any AoU rare-variant
  cross-phenotype scan you'd do.
- **Action:** **HIGH — read first.**
  (i) **Identify the discovery biobank.** Currant + Lassen + Hill +
  Venkatesh author cluster strongly suggests UK Biobank WES (Currant
  is UKB cardiometabolic; Venkatesh is Oxford-genomics-lineage). If
  AoU is the discovery cohort, that's a more directly portable
  result for the AoU work you publish in.
  (ii) **Identify the PGS used.** PGS Catalog–sourced PGS, FinnGen-
  derived PGS, or de novo PGS? The choice affects how the
  misalignment-tails are computed and how transferable the
  enrichment-test design is.
  (iii) **Identify the rare-disease gene panel.** PanelApp,
  OMIM Morbid, or a curated subset? Panel composition affects power
  and interpretation of the enrichment.
  (iv) **Check the misalignment definition.** Per-phenotype Z-score
  residuals, percentile-based tail definition, or model-based outlier
  test? The choice affects how robust the result is to PRS-
  miscalibration vs PRS-noise.
  (v) **Check the reference list for your work.** Six-feed
  saturation including your own and Bastarache's almost guarantees
  citation of at least one of: your AoU PRS paper, PheTK,
  Bastarache's phecode catalog, or Denny's eMERGE/AoU phenome-wide
  work.
  (vi) **Consider the explicit "PRS-residuals → rare-variant
  prioritization" design as a methods primitive** for any forthcoming
  AoU rare-variant work. Worth a methods-paper conversation.
  (vii) **Frame against the Souaiaia 06-20 paper** in any
  forthcoming PRS-robustness or composite-risk writing — they are
  complementary, not redundant.

### 2. Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach
- **Authors / venue:** Nandini Murali, Keith Barnatchez, Jordana E.
  Hoppe, Brandie D. Wagner, Kayleigh P. Keller, Kevin P. Josey — arXiv
  2606.23656v1 (stat.ME), submitted 2026-06-22, surfaced in
  `arxiv-digest` 2026-06-23. Score 2 (`causal inference` + `cystic
  fibrosis`).
- **Surfaced by:** `arxiv-digest` 06-23 keyword pipeline. **The first
  arxiv-digest two-keyword hit since 06-19** and one of the cleanest
  matches the pipeline has produced in the past month — both keywords
  are on tracked threads and the paper is not a tangential leak.
- **Thread:** **Causal inference and pharmacoepidemiology** (calibration
  weighting / double-robust estimation under misclassification) **+**
  **CF / CFTR disease thread** (applied to *P. aeruginosa* and *S.
  aureus* in pediatric CF) **+** **EHR phenotyping** (exposure
  misclassification is the daily problem when defining exposures from
  swabs/codes/notes vs gold-standard sputum/labs).
- **What it is:** The paper develops calibration-weighted and control-
  variate estimators for causal inference when **multiple binary
  exposures are misclassified simultaneously**, in clustered
  observations. The calibration approach treats misclassification as
  a missing-data problem (no parametric model for the
  misclassification mechanism required), and the control-variate
  adjustment uses error-prone observations to reduce variance while
  preserving consistency of the gold-standard estimator. The
  resulting estimator inherits double robustness from its components.
  They derive a **structural efficiency ceiling** in the bivariate
  setting where joint correct-classification of both exposures limits
  variance reduction. Empirically: 651-patient pediatric CF cohort
  (ages 6-21); swab-based exposure estimates attenuate the *P.
  aeruginosa* effect on FEV₁ percent-predicted by ~69% relative to
  sputum-based estimates (-2.67 vs -8.52 percentage points; 95% CI
  for sputum: -13.40, -3.63). The clinical conclusion: "relying on
  throat swabs may lead to under-treatment of *P. aeruginosa*
  infections."
- **Why it matters to you:** Four reasons.
  (a) **Direct overlap with your CF / CFTR thread.** Real CF
  pediatric cohort, real clinical exposure (Pa vs SA), real outcome
  (FEV₁ percent-predicted) — this is the exact dataset shape that
  comes out of CF Foundation Patient Registry and CF center clinical
  data. If you do any modulator-eligibility or CFTR pharmacoepi work
  that requires Pa colonization status as a covariate, this paper's
  estimator framework is the right way to handle the swab/sputum
  misclassification.
  (b) **Multiple-misclassified-exposures is a generic EHR problem,
  not just CF.** Any EHR-defined exposure (drug class derived from
  RxNorm + days-supply + ICD indication code) has misclassification
  error. The methodology here — calibration weighting with control
  variates — is portable to any AoU / MVP / BioVU exposure
  definition.
  (c) **Double-robustness inheritance.** The double-robust property
  inherited from components is methodologically important — it means
  the estimator stays consistent if either the outcome model or the
  propensity model is correctly specified, even under misclassified
  exposures. This is the gold standard for modern causal pharmacoepi
  and worth knowing as a primitive.
  (d) **arxiv-digest pipeline validation.** A two-keyword match
  including a disease thread (`cystic fibrosis`) is exactly the
  signal the pipeline was designed for. Worth noting in the pipeline
  retrospective that the cystic-fibrosis keyword is one of the
  highest-precision keyword channels on the tracked list.
- **Action:** **HIGH — read.**
  (i) Read for the estimator construction — calibration-weight
  derivation, control-variate-adjustment framework, and the
  bivariate-efficiency-ceiling result. The efficiency ceiling is
  potentially generalizable beyond CF.
  (ii) Note the simulation setup — does it cover EHR-realistic
  misclassification structures (e.g., asymmetric sens/spec, time-
  varying misclassification) or only the simple binary-misclass
  setup?
  (iii) Check the dataset — is the CF cohort the CF Foundation
  Patient Registry, EPIC, or a single-center cohort? Cohort identity
  affects how transferable the empirical result is.
  (iv) Worth a save / R-package check — Josey's group typically
  releases R packages for these estimators. If yes, it's directly
  usable for any CF or non-CF exposure-misclassification problem.
  (v) **Possible citation for any modulator-eligibility or modulator-
  outcome paper you write**, especially if Pa-colonization status is
  a stratifier and you only have swab-based assessment.

### 3. Low-Dose Lithium vs Valproate and Incident Dementia Diagnoses in Older Adults: A Propensity-Matched Cohort Study Using Electronic Health Record Data
- **Authors / venue:** A.M.P. da Silva, D.H. Santos, D.V.S.L. Júnior,
  L.J.C. Camacho et al. — venue truncated in snippet, almost certainly
  *American Journal of Geriatric Psychiatry* / *Drugs & Aging* / *JAMA
  Network Open* family (mood-stabilizer dementia outcomes is the
  characteristic topic). 2026.
- **Surfaced by:** *Pascal Brandt — new related research* feed. Brandt's
  feed is the EHR-pharmacoepi-methods adjacency.
- **Thread:** **Causal inference and pharmacoepidemiology** (active-
  comparator propensity-matched design — the cleanest pharmacoepi
  template) **+** **EHR-linked biobank analysis** (EHR-derived
  exposure and outcome) **+** **Multimorbidity / aging** (incident-
  dementia outcome in older adults).
- **What it is:** **Active-comparator** propensity-matched cohort
  study using EHR data, comparing low-dose lithium vs valproate (both
  mood stabilizers, both prescribed in older adults — so confounding-
  by-indication is partially controlled by within-class active-
  comparator design). Outcome = incident dementia diagnosis (EHR-
  derived). The "low-dose lithium" framing is interesting because
  there's a recurring lithium-as-neuroprotectant signal in
  epidemiology but the prior literature is dominated by population-
  registry observational designs in lithium-treated bipolar patients
  with no clean active comparator. This paper picks valproate as the
  active comparator — a real methodological improvement.
- **Why it matters to you:** Three reasons.
  (a) **Active-comparator + propensity-matching is the canonical
  pharmacoepi template** for the GLP-1 / SGLT2 / HRT drug-class work
  you publish in. Reading a current example of the template applied
  to a non-tracked drug class is useful for understanding what the
  current "publishable" pharmacoepi design looks like.
  (b) **EHR-based incident-dementia outcome ascertainment is non-
  trivial.** Dementia is famously under-coded in EHRs (especially
  early-stage); how this paper handles the outcome (single ICD code?
  validated phenotype algorithm? death-certificate supplementation?)
  is the methodologically interesting choice. If they validate the
  outcome algorithm in a held-out sample, that's a citable EHR-
  phenotype-validation contribution.
  (c) **Lithium-dementia signal**, separately from methodology, is
  one of the more interesting drug-repurposing candidates for
  cognitive aging — fits the drug-repurposing INTERESTS thread (off-
  label use of an approved drug for a new indication), and the
  active-comparator design is precisely the "causal-inference framing
  of off-label use" that the INTERESTS file calls out as high-
  priority for repurposing.
- **Action:** **HIGH.**
  (i) Read for the EHR phenotype algorithm for incident dementia —
  single-code vs multi-code, look-back window, validation.
  (ii) Note the propensity model covariate set — minimum-viable or
  expansive? EHR-derived covariates only or augmented with
  structured baseline assessment?
  (iii) Check the time-zero / new-user definition — first
  prescription with washout? This is the design-pinch-point for
  pharmacoepi rigor.
  (iv) Check whether they do a negative control outcome (e.g.,
  appendicitis, or fracture) to detect residual confounding. This
  is the modern best practice for pharmacoepi pre-registration.
  (v) Consider this design as a citable template for any forthcoming
  *modulator vs symptomatic-care* active-comparator study in CF, or
  for any *GLP-1 RA vs other anti-hyperglycemic* dementia-outcome
  study.

### 4. Timing of Antidiabetic Medication Initiation and Risk of Cardiovascular Events and Mortality
- **Authors / venue:** H.Y. Ko, J.Y. Shin, K. Jung, S. Bea, B. Hong, Y.
  Noh, J.H. Bae et al. — *JAMA Network Open*, 2026 (PDF, surfaced via
  Miguel Hernán citation feed — "Cites: Transparent …" suggesting they
  cite *Hernández-Díaz's Transparent Emulation* paper or a Hernán
  target-trial-emulation methods paper).
- **Surfaced by:** *10 new citations to articles by Miguel Hernán* feed.
  The Hernán citation feed is the highest-precision channel for target-
  trial-emulation work.
- **Thread:** **Causal inference and pharmacoepidemiology** (target-
  trial emulation of antidiabetic-initiation timing) **+** likely
  **GLP-1 RA / SGLT2i drug-class threads** (any modern "antidiabetic
  initiation timing" paper studying CV outcomes will include both
  classes given the post-2018 CV-benefit literature).
- **What it is:** Target-trial-emulated study of *timing* of
  antidiabetic medication initiation in (probably) a Korean or
  US claims/EHR cohort — early-initiation vs delayed-initiation
  comparison within an HbA1c-defined eligibility window — with CV
  events and all-cause mortality as outcomes. The Korean author
  cluster (Ko / Shin / Jung / Bea / Noh / Bae) suggests Korean
  National Health Insurance data, which has the advantage of
  population-scale prescription claims linked to vital-status outcome.
- **Why it matters to you:** Three reasons.
  (a) **TTE template directly portable to your GLP-1 / SGLT2 /
  HRT / Trikafta work.** The "timing of initiation" framing is
  exactly the design pattern for the modulator-initiation-timing
  question in CFTR work, the GLP-1-initiation-timing question in
  AoU, and the HRT-timing-after-menopause question.
  (b) **Korean claims-data design as a comparator for US-EHR
  designs.** When you write up an AoU or MVP TTE paper, having a
  Korean-population comparator with a similar design is useful for
  the cross-population-portability discussion.
  (c) **Hernán-citation channel is high-precision.** This is the
  second TTE-on-thread paper from the Hernán citation feed in two
  reports (06-20 had the Al-Aly COVID-vaccine-MACE paper, which I
  scored down because it was off your specific drug classes — but
  structurally the same template).
- **Action:** **HIGH.**
  (i) Read for the eligibility window definition and time-zero
  alignment — these are the TTE-rigor pinch-points.
  (ii) Note the drug classes — does it cover GLP-1 RAs and SGLT2is
  specifically, or only metformin / sulfonylureas / DPP-4s?
  (iii) Check the outcome ascertainment — claims-based ICD MACE
  composite, or curated MACE? The latter is more rigorous.
  (iv) Note the comparator group — "delayed initiation" defined how
  (no initiation within X months? initiation after Y months of
  pre-diabetic care?). Comparator definition is the most-contested
  design choice in initiation-timing TTE.
  (v) Possible citation template for any GLP-1-RA initiation-timing
  TTE you do in AoU or MVP.

### 5. Integrating social determinants of health and genetic risk in disease risk models
- **Authors / venue:** A. Biji, K. Ferar, V. Pejaver, E.E. Kenny, B.
  Liu, S. Asgari — *American Journal of Human Genetics*, 2026.
- **Surfaced by:** Dual-feed — (a) *Joshua C. Denny — new related
  research*, (b) *4 new citations to articles by Lisa Bastarache*. The
  Denny + Bastarache dual saturation is field-consensus signal for
  genetic-risk-in-EHR papers.
- **Thread:** **Genetic epidemiology / PRS** (genetic risk modeling)
  **+** **EHR-linked biobank infrastructure** (EHR-derived covariates,
  including SDoH) **+** **Machine learning for precision health**
  (multi-modality risk models tied to a clinical decision) **+**
  **Health-equity / ancestry portability** (SDoH is the systematic
  covariate that tracks underrepresented-population risk).
- **What it is:** From the snippet: "Complex diseases are [shaped by
  both genetic risk and SDoH]." Methods paper combining PRS with
  EHR-derived SDoH covariates in a unified disease-risk model.
  E.E. Kenny as senior author is the Mt. Sinai genomics-equity lineage
  (BioMe biobank); Pejaver is the variant-interpretation-meets-equity
  lineage. The AJHG venue + EE Kenny authorship suggests a careful
  methodological framing rather than a generic "add SDoH covariates"
  paper.
- **Why it matters to you:** Three reasons.
  (a) **The PRS + SDoH integration question is a core open problem
  in clinical PRS translation.** Pure-PRS models systematically
  under-represent risk in low-SES and underrepresented-ancestry
  populations because (i) the PRS itself is European-trained, and
  (ii) the model ignores environmental drivers that SDoH proxies.
  Any AoU-anchored work — which is the cohort with the richest
  SDoH-by-genetic-ancestry interaction — needs this paper as a
  reference.
  (b) **Bastarache-citation channel is on-thread.** Bastarache's
  recent work on PRS-by-EHR phenotypes naturally cites SDoH
  literature; the citation-feed firing means this paper is in the
  active-citation network for phecode-PRS work.
  (c) **Operationally portable to AoU.** AoU collects ZIP-code-level
  SDoH proxies, survey-derived SDoH measures, and EHR-derived
  utilization indicators — all of which fit the framework
  described.
- **Action:** **HIGH.**
  (i) Read for the model architecture — additive PRS-plus-SDoH-
  covariate, multiplicative interaction, hierarchical Bayesian, or
  causally framed mediation?
  (ii) Note the SDoH measurement source — ZIP-code-derived (ACS-
  based area-level), survey-derived (PROMIS-style), or EHR-derived
  utilization markers?
  (iii) Check the disease examples — diabetes, hypertension, CVD?
  Whether the framework generalizes to autoimmune / CF / rare-
  disease is the open extension.
  (iv) Note any ancestry-stratified analysis — PRS-by-SDoH
  interaction may differ across ancestry groups, and this is the
  most actionable result for AoU work.
  (v) Possible citation for any AoU PRS-translation manuscript.

### 6. Co-expression-based models improve eQTL predictions for transcriptome-wide association studies and highlight new schizophrenia-associated genes
- **Authors / venue:** F. Rossi, L. Sportelli, G.C. Kikidis, G. Grassi,
  F. Di Carlo et al. — venue truncated; likely Nature Genetics / Genome
  Biology / Molecular Psychiatry. 2026.
- **Surfaced by:** *10 new citations to articles by Jonathan K.
  Pritchard* feed. Pritchard citation channel = the methodological
  axis of TWAS / coregulation / omnigenic-model work.
- **Thread:** **Genetic epidemiology / TWAS** (co-expression-augmented
  TWAS framework) **+** **Variant interpretation** (eQTL prediction
  improvements feed into noncoding variant interpretation) **+**
  schizophrenia-specific (off-thread substantively but methodologically
  generalizable).
- **What it is:** Methods paper extending TWAS by augmenting eQTL-
  prediction models with co-expression-network information. Standard
  TWAS (PrediXcan, S-PrediXcan, FUSION) trains a per-gene prediction
  model from cis-SNPs to expression, then tests gene-trait
  association. The co-expression augmentation borrows information
  across coregulated genes to improve the per-gene prediction model,
  which (a) improves prediction R² for genes with few cis-eQTLs and
  (b) recovers trans-effect signal embedded in the co-expression
  module. Applied to schizophrenia GWAS to highlight new associated
  genes.
- **Why it matters to you:** Three reasons.
  (a) **Second-generation TWAS framework on the genetic-epi thread.**
  Your INTERESTS file names TWAS as a tracked sub-area; the modern
  TWAS methods conversation is moving from per-gene prediction to
  module-based or coregulation-augmented prediction. This is one of
  the cleaner methodological examples in 2026.
  (b) **Disease-agnostic methodology, schizophrenia-only empirical
  demonstration.** The framework is portable to any GWAS+
  transcriptomic-reference combination — relevant to any AoU-scale
  TWAS work you'd run on tracked diseases.
  (c) **Pritchard citation-feed adjacency.** Pritchard's omnigenic-
  model line and his recent co-expression-network work make this a
  default citation for the next-generation TWAS literature.
- **Action:** **HIGH on genetic-epi TWAS sub-thread; METHODS-WATCH on
  variant-interpretation thread.**
  (i) Read for the eQTL-prediction model architecture — does the co-
  expression layer come in as a regularization, as a multi-task
  prediction over coregulated genes, or as an explicit module-
  effect term?
  (ii) Note the transcriptomic reference — GTEx v8, single-cell
  bulk-pseudobulk, or PsychENCODE? Reference choice bounds
  applicability.
  (iii) Check whether the framework releases pre-computed weights
  (PrediXcan-style); if yes, directly usable for AoU TWAS.
  (iv) Methods watch only on variant-interpretation thread — the
  noncoding-variant interpretation gain is downstream of the eQTL-
  prediction gain.

### 7. Benchmarking information extraction of physical activity from electronic health record with large language models: an natural language processing pipeline and …
- **Authors / venue:** H. Yang, Z. Niu, M. Li, H. Zhou, Y. Xiao, S. …
  — venue truncated; likely *JAMIA* or *Journal of Biomedical
  Informatics*. 2026.
- **Surfaced by:** Dual-feed — (a) *Tiffany J. Callahan — new related
  research*, (b) *George Hripcsak — new related research*. Callahan +
  Hripcsak dual saturation = field-consensus signal for EHR-NLP / OMOP
  phenotyping methods work.
- **Thread:** **EHR phenotyping & OMOP** (LLM-based extraction from
  notes — explicitly on-thread per the INTERESTS file) **+**
  **Machine learning for precision health** (physical activity is a
  cross-disease lifestyle exposure for risk-prediction work).
- **What it is:** LLM-based NLP pipeline for extracting **physical
  activity** mentions from EHR clinical notes, with a benchmarking
  framework against curated annotations. Physical activity is
  interesting as an EHR-extracted exposure because (i) it's only
  partially captured in structured fields (no ICD/RxNorm code for
  "exercises 3x/week"), (ii) it has well-documented prognostic effect
  across cardiometabolic and aging outcomes, and (iii) it has
  consistent narrative patterns in primary-care and cardiology notes
  that LLMs can exploit. Benchmark framing means standardized
  evaluation metrics and likely a publicly released annotation
  schema.
- **Why it matters to you:** Three reasons.
  (a) **Directly on the EHR phenotyping LLM thread.** Your INTERESTS
  file calls out "NLP / LLM extraction from clinical notes for
  phecode and HPO term assignment"; physical activity is the same
  problem class one level over — lifestyle-exposure extraction
  rather than condition-extraction. Methodology transfers.
  (b) **Physical activity as covariate for any cardiometabolic or
  multimorbidity work.** AoU has self-reported physical activity in
  the Lifestyle module, but EHR-derived activity adds depth and
  longitudinal granularity. If this paper's pipeline is open-source,
  it's directly applicable to any AoU EHR-derived physical-activity
  covariate.
  (c) **LLM benchmarking framework is methodologically valuable.**
  EHR-LLM evaluation lacks standardized benchmarks (vs the
  CRAFT / i2b2 challenges for older NLP). A new benchmark gets
  cited as the canonical reference for the next two years if the
  schema is well-designed.
- **Action:** **HIGH.**
  (i) Read for the LLM choice and prompting strategy — fine-tuned
  small LLM, few-shot prompting of a frontier LLM, or RAG-augmented?
  (ii) Check the annotation schema — frequency, intensity, duration
  separately, or aggregated? Separate fields support more downstream
  use cases.
  (iii) Note the EHR corpus — MIMIC, single-center, multi-center?
  Multi-center generalization is the usual gap.
  (iv) Check whether code + annotations are released — if yes,
  directly usable for any AoU lifestyle-exposure work.
  (v) Frame as a methods primitive for any forthcoming AoU or MVP
  multimorbidity / cardiometabolic-trajectory work that needs
  physical-activity covariates.

### 8. In vivo measurement and prediction of cell-type-resolved non-coding variant effects in human immunity
- **Authors / venue:** Q. Liu, J. Zhang, Y. Zhu, K. Wang, C. Zhang, J.
  Zhang et al. — *medRxiv*, 2026. PDF surfaced.
- **Surfaced by:** Dual citation-feed — (a) *9 new citations to articles
  by Stephen B. Montgomery*, (b) *10 new citations to articles by Jian
  Yang*. Citation-feed firing (vs related-research) means this paper is
  already in the active-citation network of the field.
- **Thread:** **Variant interpretation** (noncoding-variant resolution —
  the gap ACMG least-addresses) **+** **Cell-type-resolved regulatory
  variant effects** (the next reference-class for noncoding-VUS
  resolution) **+** immunology-specific empirical demonstration.
- **What it is:** medRxiv preprint extending the noncoding-variant-
  effect prediction problem with **in vivo** measurements (vs the
  more standard MPRA / lentiMPRA + computational prediction
  paradigm). Cell-type-resolution restricted to human immunity
  (likely PBMC subsets or specific lymphocyte / myeloid lineages).
  Pairs directly with the Marderstein et al. *Nature Genetics*
  noncoding-variant paper from the 06-20 report — same conceptual
  axis, different empirical platform (in vivo vs MPRA-derived).
- **Why it matters to you:** Three reasons.
  (a) **Noncoding-variant interpretation is the unresolved ACMG
  gap.** Any methodological advance compounds — and now the field
  has two reference-class papers in two weeks (Marderstein at
  Nature Genetics, Liu at medRxiv).
  (b) **In vivo vs MPRA validation matters for clinical adoption.**
  ClinGen VCEPs are increasingly likely to require *physiological*
  evidence rather than reporter-assay evidence for noncoding-VUS
  reclassification; an in vivo platform is the missing link.
  (c) **Citation-feed dual firing** (Montgomery + Yang) is the
  Stanford-genomics + Westlake-population-genetics axis converging
  on this paper — high-signal.
- **Action:** **HIGH on variant-interpretation thread.**
  (i) Read for the in vivo platform — humanized mouse, organoid,
  patient-derived primary cells, or in-human edit-and-measure?
  (ii) Note the cell-type panel — broad immune (T/B/myeloid/NK) or
  fine-grained (specific lymphocyte / myeloid subsets)?
  (iii) Pair with Marderstein — does the in vivo measurement
  agree with Marderstein's MPRA-derived effects, or are there
  systematic discrepancies? The discrepancy literature is the next
  reference-class question.
  (iv) Check whether they release a per-variant effect-size score
  for the panel of variants tested — if yes, that score becomes a
  citation in any rare-noncoding-variant interpretation write-up.

### 9. PGS Browser: a public platform for personalized polygenic score analysis and interpretation
- **Authors / venue:** N. Kolosov, M.P. Reeve, P.D. Briotta Parolo,
  M.I. Kurki et al. — *Nature Communications*, 2026
  (s41467-026-74461-7).
- **Surfaced by:** Dual-feed — (a) **Chenjie Zeng — new related
  research** (your own feed), (b) *Mark Daly — new articles*. Self-
  feed + Daly-new-article dual firing is the FinnGen-axis signal.
- **Thread:** **Genetic epidemiology / PRS** (PRS-translation
  infrastructure) **+** **Machine learning for precision health**
  (interpretation framework tied to risk-stratification decisions).
- **What it is:** From the snippet: "Polygenic scores (PGSs) quantify
  individual genetic susceptibility to complex diseases and can
  identify high-risk individuals well before clinical onset. Their
  clinical translation, however, requires population-based reference
  resources." Public web platform for personalized PGS analysis with
  population-reference distributions. Mark Daly + FIMM authorship +
  Nature Communications venue makes this the likely default citation
  for population-PRS-distribution infrastructure for the next 2-3
  years, paralleling the PGS Catalog's role as the PRS-weights
  registry.
- **Why it matters to you:** Three reasons.
  (a) **Self-feed firing.** Google Scholar's relevance model judged
  this close enough to your published work to surface in your own
  related-research alert.
  (b) **PRS-translation infrastructure overlap with AoU.** AoU is
  building its own PGS-platform infrastructure (AoU Genomic Data
  Portal / DRC). A FinnGen-anchored reference resource is a useful
  comparator and may share design patterns.
  (c) **Daly senior-authorship.** Mark Daly's FIMM/FinnGen work is
  the European-population reference for biobank-scale PRS, and
  any FinnGen-PRS-platform paper becomes a default citation for
  cross-population PRS portability arguments.
- **Action:** **HIGH.**
  (i) Read for the reference-distribution construction — FinnGen-
  only, or FinnGen + UKB + AoU pooled? Pooled distributions are
  more useful but raise weighting questions.
  (ii) Note the diseases / traits covered — is it a CAD / T2D / IBD
  focus, or all major complex diseases? Disease coverage drives
  reuse.
  (iii) Note the interpretation framing — percentile rank only, or
  with absolute-risk conversion via baseline incidence rate? The
  latter is much more clinically actionable.
  (iv) Possible citation template for any AoU PGS-platform write-up
  you do.

### 10. Distinct genetic architecture in the tails of complex traits — *carry-forward from 06-20*
- **Authors / venue:** T. Souaiaia, H.M. Wu, A.P.S. Ori, S.W. Choi,
  C.J. Hoggart et al. — *Nature*, 2026.
- **Surfaced by:** *Stephen B. Montgomery — new related research* feed
  (re-fired 06-27).
- **Status:** **Already covered in detail in the 06-20 report (HIGH
  #4).** Listed here for completeness — the related-research re-firing
  on 06-27 reflects new in-press citations of the Nature paper, which
  is the Google Scholar engine's way of telling you the paper is
  becoming a citation hub. Worth noting only because (a) it re-fired,
  which doesn't always happen, and (b) it pairs structurally with
  this report's HIGH #1 (Baya AJHG paper on PRS-residuals → rare-
  variant enrichment). The two compose into a coherent **PRS-tails-
  miscalibration** sub-literature.
- **Action:** See 06-20 report. No additional action items.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Privacy-preserving federated tensor decomposition of single-cell
  immune data: recovering multicellular programs across institutions**
  — Axel Faes, Stephanie M. van den Berg, Maryam Amir Haeri — arXiv
  2606.24938 (q-bio.GN), 2026-06-22, surfaced by `arxiv-digest`
  06-25. Score 1 (`cross-ancestry`). **Strong methods paper:**
  federated tensor decomposition with stacked-SVD aggregation under
  global-mean centering, provably equivalent to centralized decomp.
  Empirical: 261-donor SLE atlas, three real COVID-19 sites, ILD
  atlas — recovers canonical interferon program and predicts ILD
  better than the best single cell type (AUC 0.96 vs 0.91).
  Membership-inference attack reduced from AUC 0.91 to 0.61 with
  secure aggregation. **METHODS-WATCH** for any future multi-site
  AoU + MVP + UKB federated single-cell or immune-program work, and
  as a citable comparator design for federated PRS / TWAS.

- **Are Tabular Foundation Models Robust to Realistic Query
  Distribution Shifts in Microbiome Data?** — Giulia Perciballi,
  Ahmad Fall, Federica Granese, Edi Prifti, Jean-Daniel Zucker —
  arXiv 2606.24995 (cs.LG), 2026-06-23, surfaced by `arxiv-digest`
  06-25. Score 1 (`foundation model`). Tabular FMs evaluated on
  gut-microbiome perturbation benchmarks; zero-imputation
  perturbation degrades all models, sparsification disproportionately
  affects TFMs vs random forest. **METHODS-WATCH** for FM-robustness-
  audit references in any clinical-FM evaluation write-up. Off-thread
  substantively (microbiome).

- **KG-TRACE: A Neuro-Symbolic Framework for Mechanistic Grounding in
  Antimicrobial Resistance Prediction** — Naman Garg, Sarika Jain,
  Sourav Yadav, Bharat K. Bhargava, Ghanapriya Singh, Abhishek
  Srivastava, Parimal Kar — arXiv 2606.26179 (cs.LG), 2026-06-24,
  surfaced by `arxiv-digest` 06-26. Score 1 (`knowledge graph`).
  Neuro-symbolic framework fusing WHO mutation KG with neural genomic
  model via "epistemic trust gate" for AMR prediction. Introduces a
  *Biological Grounding Ratio* metric that quantifies neural-
  attribution alignment with KG biology (92.5% symbolic coverage on
  isoniazid). **METHODS-WATCH** for the KG-grounding-of-neural-
  predictions design pattern, which is the right idea for explainable
  drug-repurposing on the INTERESTS thread "knowledge-graph / GNN
  approaches with *explainable* hypothesis output." Off-thread
  substantively (AMR-TB).

- **Curation of a Cardiology Interface Terminology for Highlighting
  Electronic Health Records using Machine Learning** — M.K.H.
  Dehkordi, S. Zhou, Y. Perl, F.P. Deek, J. Geller et al. — arXiv
  preprint, 2026 (Patrick Ryan related-research). Interface-
  terminology curation with ML — sits on the **EHR phenotyping /
  ontology curation** thread. Worth a glance if any forthcoming
  cardiology-phenotype work needs terminology infrastructure;
  otherwise log.

- **Doubling cascade testing uptake for hereditary cancer syndromes:
  Results from a cluster randomized controlled trial of a registry-
  aided outreach approach** — J. Chiang, C. Victoria, J. Yuen, M.
  Karthikeyan, R. Caeser et al. — JCO 2026 supplement abstract
  (ascopubs.org/doi/abs/10.1200/JCO.2026.44.16_suppl.11007),
  surfaced in Chenjie Zeng self-feed. **METHODS-WATCH** —
  implementation-science RCT in genetic counseling / cascade testing.
  Self-feed firing means it's adjacent to your published corpus
  (likely the cancer-genetics-screening axis), but it's an
  implementation paper rather than a methods paper. Note it for any
  future hereditary-cancer cascade-testing implementation write-up.

- **Predicting immune-related thyroiditis using polygenic risk scores
  in patients with advanced melanoma** — A.A. Tarhini, M.A. Khaksar,
  Z. Chen, S.J. Lee, F.S. Hodi, T. Li et al. — *Journal for
  ImmunoTherapy of Cancer*, 2026 (jitc.bmj.com/content/14/6/e015413),
  surfaced in Chenjie Zeng self-feed. PRS to predict immune-related
  adverse events (thyroiditis) from ICI therapy in melanoma.
  **METHODS-WATCH** — PRS-for-AE prediction is an emerging
  pharmacogenomics-adjacent application class, and the self-feed
  firing means it's in your broader citation network. Off the core
  drug-class thread but conceptually close to the GLP-1 / SGLT2
  pharmacogenomics question of who benefits and who has AEs.

---

## SKIP / noise (logged, no action)

- **alphaXiv "Autoresearch for arXiv Papers" promotional digest**
  (contact@alphaxiv.org, 06-24) — infrastructure/marketing email, not
  research. Tool announces an "autoresearch" feature where the user
  can change `arxiv.org/abs/...` to `autoarxiv.org/abs/...` and an
  agent resolves the paper to a research output. Logged as
  infrastructure to evaluate later; not a research signal.
- **CellBRIDGE: Learning Cellular Trajectories via Interaction-Aware
  Alignment** (van der Schaar feed) — single-cell trajectory ML; off
  the clinical-FM thread.
- **Engineered Lipid Nanoparticles with Promoted Endosomal Escape and
  R283S-Mediated STING Activation for Pancreatic Cancer** (Kastner
  citation) — drug-delivery / immuno-oncology, off-thread.
- **Prevalence and Associations of MEPS-Defined Long COVID Among
  Adults** (Chute citation) — descriptive epidemiology, off the EHR-
  phenotyping methods thread.
- **Estimating common synaptic inputs to spinal motor neurons from
  motor unit spike trains using openhdemg** (arxiv-digest 06-23,
  score 1, keyword `motor`) — neurophysiology tutorial, off-thread.
  Clean keyword leak from the `motor` keyword via the muscle-
  physiology literature; not a tracked context.
- **Vaccine effectiveness against COVID-19 in-hospital mortality in
  people living with HIV across SARS-CoV-2 variant waves** (Chute
  related-research) — global-health COVID epidemiology, off the
  pharmacoepi / drug-class threads.
- **Fever of unknown origin: adult-onset Still's disease as the
  hidden culprit—a case report** (Kastner related-research) — case
  report, off-thread.
- **The New Tumor Predisposition Syndromes with Neuro-Oncological
  Relevance—A Comprehensive Review for Neuroradiologists**
  (Karczewski citation) — review-tier, off-thread.
- **Unified Energy for Invariant and Independent Decoding in
  Diffusion Language Models** (Zitnik related-research) — LLM-
  methods paper, off the clinical-FM thread; pure ML-methods leak.
- **Prime editing-mediated microhomology enables efficient
  replacement of large DNA** (Shendure related-research) — genome-
  engineering methods, off the variant-interpretation thread.
- **Patient Representation Learning from Clinical Notes Using Text
  Embeddings (Czech oncology thesis)** (Yuan Luo citation) —
  thesis-level, off-thread.
- **Toward Sustainable Ubiquitous AI** (Natarajan citation) — generic
  AI / sustainability essay, off-thread.
- **Cross-lingual Self-Consistency for Multilingual Reasoning with
  Language Models** (Szolovits related-research) — generic LLM-
  reasoning, off the clinical-FM thread.
- **Artificial Intelligence in Orthopedics: Essential Knowledge,
  Applications, and Responsible Integration for Residents and
  Surgeons** (Szolovits citation) — domain review, off-thread.

---

## Suggestions for the pipeline

Carries forward most prior recommendations (still unactioned). Today's
items add two confirmed-recurring issues plus one new keyword pattern.

1. **The `arxiv-digest` rate-limit failure recurred on 06-24, 4 days
   after the same failure on 06-20.** Same pattern (3-of-4 categories
   429'd; only one fetched). This is now confirmed recurrent, not a
   one-off. Recommended fix (carried forward and now urgent):
   (a) jittered retry-with-backoff per category (1-2 retries with
   30-60 s pause + random jitter), (b) split the four categories into
   two workflow runs separated by 90 minutes, or (c) further-double
   the inter-category pause to 30 seconds. The 06-24 digest also
   produced the "3/4 failed" warning correctly, which is good — the
   distinct-from-real-zero-day signal is preserved. The fix is on the
   fetch side, not the messaging side.

2. **`knowledge graph` keyword: 8th consecutive window of off-
   biomedical hits.** Today's KG-TRACE paper (AMR-TB prediction in
   M. tuberculosis) is at least biomedical and arguably methods-
   watch-worthy for the KG-grounding-of-neural-predictions pattern,
   but it's still off the daily disease threads. Recommended fix
   (carried forward): change keyword to `biomedical knowledge graph`
   OR `clinical knowledge graph` OR a compound filter `(knowledge
   graph) AND (medical OR biomedical OR clinical OR EHR OR phenotype
   OR drug OR disease)`.

3. **`foundation model` keyword leaked again** — the 06-25 microbiome-
   TFM paper is methods-interesting but off the EHR-FM / clinical-FM
   thread. Recommended fix: tighten to `EHR foundation model` OR
   `clinical foundation model` OR `medical foundation model` OR a
   compound filter `(foundation model) AND (EHR OR clinical OR
   medical OR patient OR health)`.

4. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds**
   (carry-forward, unaddressed). Today's items #1 (Baya AJHG), #3
   (da Silva dementia), #4 (Ko JAMA Network Open), #5 (Biji AJHG), #6
   (Rossi TWAS), #7 (Yang EHR-LLM), #8 (Liu noncoding immunity), #9
   (Kolosov PGS Browser) all appeared in Scholar feeds because they
   are in journal or medRxiv venues, not in q-bio / stat.AP arXiv
   categories. The current `arxiv-digest` pipeline can never reach
   these without source expansion. **The 06-23 Murali CF causal-
   inference paper was in `stat.ME` and was the lone two-keyword
   on-thread hit of the week** — adding `stat.ME` would
   straightforwardly increase the hit rate.

5. **Add PRS-robustness / PRS-tails keyword set** (carry-forward,
   now strengthened). Items #1 (Baya AJHG, PRS-residuals → rare-
   variant enrichment) and #10 (Souaiaia Nature, PRS-tails
   architecture, carry-forward) form a sustained sub-thread. Add:
   `PRS residual`, `polygenic residual`, `polygenic tails`, `PGS
   tails`, `misaligned individuals`, `polygenic deviation`.

6. **Add `noncoding variant interpretation` / `regulatory variant
   effect` / `MPRA` keywords** (carry-forward from 06-20, now
   strengthened). Item #8 (Liu medRxiv, in vivo noncoding immune)
   pairs with last report's Marderstein Nature Genetics paper —
   the cell-type-resolved noncoding interpretation literature is
   now a sustained sub-thread.

7. **Add `proteomic signature` / `aging clock` / `organ-specific
   aging` keywords** (carry-forward from 06-20, no new instance
   this week but the recommendation stands).

8. **Add `SDoH` / `social determinants of health` keyword on the
   genetic-epi axis** (new). Item #5 (Biji AJHG) is the first major
   SDoH-by-genetic-risk methods paper this digest's history; pairs
   with the cross-ancestry portability axis.

9. **`mendelian diseases` and `drug repurposing` keyword fixes**
   (carry-forward, 8th consecutive window).

10. **Continue tracking your own self-citation feed as the single
    highest-precision channel.** This window confirms the pattern:
    items #1 (Baya, 6-feed including self), #9 (Kolosov PGS Browser,
    self + Daly), plus two METHODS-WATCH items (Chiang JCO cascade-
    testing RCT, Tarhini JITC PRS-thyroiditis) all surfaced through
    the self-feed. Self-feed precision remains the gold standard.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 9 (+1 carry-forward) | (1) Baya AJHG PRS-residuals→rare-disease genes [6-feed inc. self], (2) Murali arXiv CF causal-inference misclassified exposures [arxiv-digest 06-23], (3) da Silva EHR low-dose lithium vs valproate dementia [Brandt], (4) Ko JAMA Net Open antidiabetic-initiation timing [Hernán citations], (5) Biji AJHG SDoH+genetic-risk integration [Denny+Bastarache], (6) Rossi co-expression TWAS [Pritchard citations], (7) Yang EHR-LLM physical-activity extraction [Callahan+Hripcsak], (8) Liu medRxiv in vivo noncoding immune variant effects [Montgomery+Yang citations], (9) Kolosov Nat Commun PGS Browser [self+Daly], (10) Souaiaia Nature PRS tails [re-fired, carry-forward from 06-20] |
| METHODS-WATCH | 6 | Faes federated tensor-decomp single-cell [arxiv-digest 06-25], Perciballi TFM microbiome robustness [arxiv-digest 06-25], Garg KG-TRACE AMR neuro-symbolic [arxiv-digest 06-26], Dehkordi cardiology terminology curation [Patrick Ryan], Chiang JCO cascade-testing RCT [self], Tarhini JITC PRS-thyroiditis [self] |
| SKIP | ~14 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 4-6 METHODS-WATCH), this
seven-day window delivers a higher HIGH count, driven by the AJHG
publication week (items #1 and #5 both AJHG) plus the unusual six-feed
saturation of the Baya paper. The `arxiv-digest` pipeline produced
**one strong on-thread paper (Murali CF causal-inference, item #2)
across the week** — the highest-quality digest hit in over a month —
plus three methods-watch instances and one fetch-failure day. The
recurring fetch failure (06-20 + 06-24) is now confirmed recurrent and
warrants the workflow-side fix recommended above.
