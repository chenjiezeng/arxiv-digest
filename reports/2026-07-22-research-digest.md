# Research digest report — 2026-07-22

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-18 → 2026-07-22** (five-day catch-up since the last
committed report at `reports/2026-06-20-research-digest.md`).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword feeds) | 2026-07-20 → 07-21 | Two large batches — 07-20 20:52Z (author-feed cluster: Denny, Hripcsak, Bastarache, Pritchard, Montgomery, Yang, and related-research feeds for the same panel) and 07-21 10:49Z (keyword feeds: `phenome wide association studies`, `variant interpretation`, `All of Us research program`, `UK Biobank`, `mendelian diseases`). |
| `arxiv-digest` repo (`digests/`) | 2026-07-18 → 07-22 | **07-18/07-19/07-20 = 0 papers** (dry weekend); **07-21 = 4 papers**, two directly on-thread (HTE-guided target trial emulation + federated causal mediation of GLP-1); **07-22 = 2 papers** (MR-Lasso variant + breast-cancer EHR clustering). |
| NCBI "My NCBI What's New" ("All of Us", "UK Biobank") | daily | Light week — one high-signal hit on 07-22 (target trial × disparities framework). |
| bioRxiv / medRxiv Subject Collection Alerts | daily | Aggregate feeds; individual papers surfaced upstream via Scholar. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries in the summary section
> include the full abstract because the pipeline captures it.

---

## Executive summary

- **Biobank-scale GWAS on healthcare cost, 1.4M individuals across 11
  studies and 7 countries — double-feed saturation.** May-Wilson, Lee,
  Nakanishi, van der Laan et al., *Quantifying the contribution of
  genetic variation to healthcare expenditure across diverse healthcare
  systems* (medRxiv 2026-07-14; PDF surfaces in **both** Joshua Denny
  and Lisa Bastarache citation feeds). "Hundreds of common genetic
  variants robustly" associated with healthcare spend across inpatient,
  outpatient, primary-care, and prescription channels. Explicitly cites
  the AoU APOE-PheWAS paper (i.e., anchors on the PheWAS-of-a-major-
  Mendelian-gene reference pattern) — bears directly on your PheWAS +
  biobank + genetic-epi thread, and gives a natural cost-utility angle
  on penetrance-of-monogenic-variant work. **HIGH — read first.**
- **The first "target trial × disparities" framework paper — landed in
  the AoU NCBI feed on 07-22.** Sun, Iwashyna, Drabo, Crews, Ferryman,
  Jackson, *Nesting a Target Study within a Target Trial: A Framework
  for Evaluating Intervention Effects on Disparities* (*Epidemiology*,
  2026-07-21, PMID 42479539). Extends target trial emulation to
  interventions whose *effect on disparities* is the estimand. Directly
  serves your causal-inference & pharmacoepi thread and, because the
  authors sit at the intersection of kidney-disparities work (Crews)
  and epidemiologic-methods (Iwashyna, Jackson), it's likely to become
  a reference citation for any AoU / MVP paper claiming a disparities-
  reducing effect from a real-world intervention. **HIGH.**
- **HTE-guided target-trial emulation of DAPA-HF using Mayo Clinic EHR
  data — the on-thread `arxiv-digest` standout.** Li, Lee, Li, Liu,
  James, Pellikka, Tao, Zong, *Optimizing Clinical Trial Protocols
  Using EHR-Derived Heterogeneous Treatment Effects* (arXiv 2607.16934,
  stat.AP). Meta-S-learner + decision-tree stratification on the DAPA-
  HF emulation identifies a beneficial subgroup (HR 0.20; 95% CI
  0.09–0.48) and a harmful subgroup (HR 6.68; 95% CI 2.76–16.17) that
  are both masked by the pooled null (HR 1.68, p=0.15). Directly serves
  the causal-inference + ML-for-precision-health double-thread; the
  SGLT2 drug class also puts it in the active pharmacoepi thread.
  **HIGH.**
- **Federated causal mediation of GLP-1 → HbA1c through BMI — the
  second on-thread `arxiv-digest` paper.** Jang, Radwan, Risk, Lee,
  Bian, Shi, Guo, Zhao, *Privacy-preserving causal mediation analysis
  using distributed electronic health record networks* (arXiv
  2607.17958, stat.AP). Federated natural-direct/indirect-effects
  estimator applied to 32,146 patients in the Indiana Network for
  Patient Care; finds BMI-mediation accounts for only a small share of
  GLP-1's HbA1c benefit. Serves the GLP-1 sub-thread inside pharmacoepi
  and the multi-site EHR + privacy work that showed up in the June
  Denny-related feed (Kundu et al.). **HIGH.**
- **TEDDY: pediatric EHR foundation model on 73M ICD-10 codes from 1.6M
  children.** Neeley, Botas, Jia, Yao, Palacios, Choi et al. (arXiv
  2607.14191, 2026; Denny author-citation feed). 1.84M-parameter
  decoder transformer trained on longitudinal pediatric diagnosis
  trajectories with visit timing — an explicit pediatric addition to
  the CLMBR / MOTOR / EHRSHOT / MEDS lineage in your EHR-FM thread.
  **HIGH (EHR foundation models).**
- **Two ancestry-aware genetic-epi methods papers on 07-20 — both
  worth cribbing.** (i) Taliun & Gagliano Taliun, *Empirical estimation
  of multiple-testing burden for population-based HLA association
  studies using sequencing-derived HLA alleles across genetic
  ancestries* (bioRxiv 2026-07-12) — recalibrated significance threshold
  for HLA scans, ancestry-stratified. (ii) Kore, Tan, Lu,
  Manuel-Friedman, Hu et al., *Local ancestry-informed rare variant
  burden testing improves gene discovery in admixed populations*
  (medRxiv 2026-07-13). Both directly on the trans-ancestry portability
  sub-thread inside genetic epi. **HIGH.**
- **GenoSiS: biobank-scale genotype similarity search for dynamic
  patient-matched cohort creation.** Schneider, Chowdhury, Tepper, Khan
  et al., *Biobank-scale genotype similarity search and dynamic
  patient-matched cohort creation with GenoSiS* (Genome Research 2026;
  Bastarache related-research feed). Genotype-embedding + Intel SVS
  vector search for on-demand ancestry- and phenotype-matched control
  selection. Directly on the biobanks-with-EHR-linkage infrastructure
  thread. **HIGH.**
- **All-of-Us usability paper in AJPH.** Lewis, D'Angelo, Zhong,
  *Strengths and Limitations of All of Us Data Use for Public Health
  Research* (AJPH 2026; Denny related-research feed). Timing is
  convenient — a cohort-profile-style paper worth citing whenever your
  own AoU work needs a one-line summary of coverage and known
  limitations. **HIGH (reference utility).**
- **MR methods: a lasso variant that fixes MR-Lasso's identification +
  post-selection inference.** Qasim, Wang, Bhatt, *Adaptive
  Penalization and Bootstrap-Smoothed Inference for Two-Sample
  Mendelian Randomization with Summary Data* (arXiv 2607.18503, 07-22,
  stat.ME). MR-ALasso improves invalid-instrument identification;
  MR-ALasso-B combines it with bootstrap smoothing for reliable
  post-selection intervals; R package `MRAlasso` provided. Pairs
  cleanly with the *Reassessing Instrument Strength in Two-Sample MR*
  medRxiv preprint from Liu/Sofer that also surfaced this window.
  **HIGH (MR methods).**
- **Two "sex-specific AD sub-phenotype" + "genetic architecture of
  low-risk groups" papers land — both from the multimorbidity /
  clustering thread.** (i) Meng, Yang, Xu, Huang, Wang, Song et al.,
  *Identifying sex-specific sub-phenotypes of Alzheimer's disease
  progression using longitudinal electronic health records*
  (EBioMedicine 2026; deep-learning framework on longitudinal EHRs,
  cites both phecode and PheWAS foundational papers). (ii) Vazquez, Li,
  Lu, Neelam, Bray, Shrestha et al., *Hiding in plain sight: uncovering
  the genetic basis of complex phenotypes through low-risk groups*
  (Genetics 2026; cites AoU) — reframes GWAS by anchoring on the
  *resistance* tail rather than the case tail. Both **HIGH**; #(ii)
  should be paired with the PRS-tails Nature paper from the 06-20
  report (Souaiaia et al.) since they attack the same problem from
  opposite ends of the risk distribution.

Everything else in this window is either off-thread (breast-cancer
UMAP clustering, snRNA discovery, single-cell FM benchmark), or a
methods-watch entry summarized in the section below.

---

## Detailed reports

### 1. Quantifying the contribution of genetic variation to healthcare expenditure across diverse healthcare systems

**Authors.** S May-Wilson, J Lee, T Nakanishi, CM van der Laan et al.
**Venue.** medRxiv, 2026-07-14.
**Signal source.** Google Scholar author-feeds for Joshua C. Denny (07-20 20:52Z) **and** Lisa Bastarache (07-20 20:52Z) — double-feed saturation.
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology; PheWAS/PheRS-adjacent (uses AoU APOE PheWAS reference); biobanks with EHR linkage.

**What the paper does (from abstract).** GWAS of healthcare
expenditure — inpatient, outpatient, primary care, and prescription
drug costs — in up to **1,429,889 individuals across 11 studies and 7
countries**. Reports hundreds of common variants robustly associated
with cost, and cites the *Phenome-wide association of APOE alleles in
the All of Us* paper (i.e., anchors on a familiar reference in your
own bibliography).

**Why it matters for your work.**
1. **Scale.** ~1.4M is the largest cross-country biobank meta-analysis
   you'll cite this quarter; useful as a background reference wherever
   you need to justify AoU's addition to global consortia.
2. **Cost as a phenotype.** Reframes health-economic burden as a
   GWAS-tractable trait — a natural adjacent phenotype to any
   penetrance / life-course-cost estimate you produce from
   monogenic-variant carriers in AoU (CFTR, APOL1, BRCA1/2, etc.). If
   the paper's summary stats become publicly available, they'd support
   a downstream PheRS-of-cost or MR-of-cost analysis in AoU.
3. **AoU APOE citation.** They explicitly cite the AoU APOE PheWAS —
   worth checking whether they replicated it as a positive control and
   whether the healthcare-cost effect of APOE-e4 aligns with published
   morbidity effects (a cross-check on their pipeline).

**Follow-ups.** Pull the PDF and check (a) which biobanks are
included (AoU? MVP? BioVU? All UK? Estonia?), (b) whether they release
summary stats, (c) their handling of insurance-based cost differences
across countries.

---

### 2. Nesting a Target Study within a Target Trial: A Framework for Evaluating Intervention Effects on Disparities

**Authors.** X Sun, TJ Iwashyna, EF Drabo, DC Crews, K Ferryman, JW Jackson.
**Venue.** *Epidemiology*, published online 2026-07-21. PMID **42479539**. doi:10.1097/EDE.0000000000002024.
**Signal source.** NCBI "What's new for 'All of Us' in PubMed" (07-22 11:42Z; sole hit in that day's alert).
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi (target trial emulation); AoU / EHR-cohort work (implicit — the alert triggered on AoU).

**What the paper does (from title + author panel).** Extends the
*target trial* framework (Hernán, Robins) to interventions whose estimand
is a *change in a disparity*, not just an average effect. The "target
study within a target trial" nesting formalizes the distinction between
(a) the trial you'd have run to estimate the ATE and (b) the study
you'd have run to estimate whether the ATE differs across a socially
patterned group (i.e., the effect on the disparity itself).

**Why it matters for your work.**
1. **Direct methodological asset for AoU-style work.** Every time an
   AoU or MVP paper claims an intervention *reduces a disparity*,
   this becomes the identifiability spine to cite. Given the panel
   (Iwashyna's ICU / mortality work; Crews's kidney-disparities
   record; Jackson's decomposition-of-disparities methods), the paper
   will move fast into the reference class.
2. **Pairs with the Kundu privacy-enhanced multi-site paper** from the
   06-20 window (federated selection-bias-corrected learning). Together
   they cover the two most-cited weaknesses in AoU-based disparity
   claims: heterogeneous selection across sites (Kundu) and the
   ill-defined estimand of "effect on disparity" (Sun).
3. **APOL1 fit.** Directly applicable to APOL1 modulator work — where
   any effect of a candidate therapeutic on kidney-disease disparity
   requires a well-specified estimand.

**Follow-ups.** Pull the paper; identify the estimand notation they
adopt (Jackson's decomposition vs. VanderWeele's four-way
decomposition vs. a de-novo notation); check whether the worked example
is a kidney / APOL1 setting.

---

### 3. Optimizing Clinical Trial Protocols Using EHR-Derived Heterogeneous Treatment Effects

**Authors.** Xiaodi Li, Munhuwan Lee, Pengyang Li, Xiaoke Liu, Jose K. James, Patricia A. Pellikka, Cui Tao, Nansu Zong.
**Venue.** arXiv 2607.16934v1, submitted 2026-07-18 (stat.AP).
**Signal source.** `arxiv-digest` 2026-07-21 (keyword hits: `electronic health records`, `heterogeneous treatment effects`; score 2).
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi; ML for precision health; biobanks-with-EHR (Mayo Clinic Cloud); GLP-1 / SGLT2 sub-thread (dapagliflozin).

**What the paper does.** Emulates the DAPA-HF trial in the Mayo
Clinic Cloud EHR — dapagliflozin vs placebo in HFrEF patients — and
uses a **Meta-S learner** to estimate individual heterogeneous
treatment effects on all-cause mortality, then a decision-tree
thresholding pass to define subgroups. Reports:

- **Pooled emulation.** HR 1.68 (95% CI 0.83–3.41; p=0.15) — the
  full-cohort emulation misses the DAPA-HF benefit.
- **Low-HTE (beneficial) subgroup.** HR 0.20 (95% CI 0.09–0.48;
  p=0.0002) — dapagliflozin looks strongly protective.
- **High-HTE (harmful) subgroup.** HR 6.68 (95% CI 2.76–16.17;
  p<0.0001) — dapagliflozin looks strongly harmful.

**Why it matters for your work.**
1. **Concrete instance of "the null hides two effects" in a
   pharmacoepi target trial.** Cleanest example this quarter of an
   emulation flipping from null to bidirectionally significant under
   HTE stratification. Directly applicable when you emulate CFTR-
   modulator, GLP-1, or SGLT2 comparisons in AoU.
2. **Caveat to flag.** The magnitude of the "harmful" subgroup HR
   (6.68) is *implausibly large* for an SGLT2 in HFrEF given the
   original DAPA-HF results. Two live concerns: (a) severe unmeasured
   confounding by indication concentrated in the harmful subgroup —
   the tree-defined stratum may be capturing patients too sick to
   benefit; (b) overfitting from the S-learner on a modest EHR cohort.
   Worth pulling to check subgroup n's, positivity, and whether they
   ran negative-control outcomes.
3. **Meta-S-learner + decision-tree pattern is portable.** The exact
   pipeline (S-learner → tree thresholding → subgroup HR reporting)
   is what your ML-for-precision-health thread is looking to see
   translated to AoU cohorts.

**Follow-ups.** Read Methods for how they handled (a) time-zero
alignment / immortal-time bias, (b) positivity in tree leaves, (c)
whether "harmful" subgroup passed a negative-control test.

---

### 4. Privacy-preserving causal mediation analysis using distributed electronic health record networks

**Authors.** Hyojung Jang, Rotana Radwan, Malcolm Risk, Yao Lee, Jiang Bian, Xu Shi, Serena Guo, Lili Zhao.
**Venue.** arXiv 2607.17958v1, submitted 2026-07-20 (stat.AP).
**Signal source.** `arxiv-digest` 2026-07-21 (keyword hit: `glp-1`; score 1).
**Bucket.** HIGH.
**Threads served.** GLP-1 pharmacoepi sub-thread; causal inference; multi-site EHR / federated methods.

**What the paper does.** Federated (privacy-preserving) causal
mediation analysis for **natural direct and indirect effects** across
sites, exchanging only low-dimensional summary statistics. Applied to
**32,146 patients in the Indiana Network for Patient Care**, they
decompose the effect of **GLP-1 receptor agonists on HbA1c** into
BMI-mediated vs. direct pathways. **BMI mediation was small** — i.e.,
most of GLP-1's glycemic benefit is *not* through weight loss.

**Why it matters for your work.**
1. **Mechanistic-quantification of a first-line diabetes drug class**
   using a federated pipeline that scales to AoU + MVP + BioVU without
   patient-level pooling. This is exactly the design pattern the AoU
   pharmacoepi threads should be borrowing.
2. **Substantive claim worth citing.** "BMI mediation is small" is the
   kind of clean, quotable finding that unlocks the "GLP-1 has
   weight-independent effects" narrative in your GLP-1 work.
3. **Pairs with the Sun et al. target-trial-of-disparities paper**
   above: both attack the same class of identifiability challenge
   (multi-site, selection-heterogeneous EHR causal claims), from
   complementary angles.

**Follow-ups.** Check whether the federated estimator carried through
to natural indirect effect confidence intervals that were valid across
sites, and whether the code is on GitHub.

---

### 5. TEDDY: A Pediatric Foundation Model for Risk Forewarning from ICD-Coded Diagnostic Histories

**Authors.** MB Neeley, J Botas, J Jia, L Yao, D Palacios, B Choi et al.
**Venue.** arXiv 2607.14191, 2026.
**Signal source.** Google Scholar new-citations feed for Joshua C. Denny (07-20 20:52Z).
**Bucket.** HIGH.
**Threads served.** EHR foundation models.

**What the paper does (from abstract).** Trains **TEDDY** (Temporal
Event Decoder for Disease in Youth), a **1.84M-parameter decoder
transformer** on ~**73M ICD-10 diagnoses from 1.6M children at a single
pediatric institution**. Models longitudinal diagnosis trajectories
*and* visit timing.

**Why it matters for your work.**
1. **First serious pediatric entry in the CLMBR / MOTOR / EHRSHOT /
   FEMR / MEDS lineage.** Every FM in the thread so far has been
   adult-centric — TEDDY fills the "under-18" hole with
   developmentally-structured trajectories.
2. **Cites your reference class.** The Scholar feed shows it cites
   "Foundation Models to Unlock Real-World Evidence from …", i.e.,
   it self-positions inside the EHR-FM lineage rather than as generic
   sequence modeling.
3. **Single-site limitation.** 1.6M children at one institution is
   an obvious external-validation gap; a natural extension is a MEDS-
   formatted multi-site pediatric FM. Worth watching whether a v2 lands
   in q-bio in the coming quarter.

**Follow-ups.** Skim Methods for tokenizer (ICD-10 code vocabulary
handling — the "80,000 diagnosis codes" problem is worse in pediatrics
because rare-disease coverage matters more); check whether they release
weights and whether prediction targets include phecode-mapped outcomes.

---

### 6. Empirical estimation of multiple-testing burden for population-based HLA association studies using sequencing-derived HLA alleles across genetic ancestries

**Authors.** D Taliun, SA Gagliano Taliun.
**Venue.** bioRxiv, 2026-07-12.
**Signal source.** Google Scholar related-research feed for Joshua C. Denny (07-20 20:52Z).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology; ancestry portability.

**What the paper does (from abstract).** Empirical recalibration of
the significance threshold for HLA association scans as WGS-derived
HLA typing (rather than SNP-imputed) becomes routine in biobank-scale
data. Explicitly ancestry-stratified.

**Why it matters for your work.** Recalibrated HLA significance
thresholds are directly relevant to any AoU srWGS-based phecode-HLA
PheWAS (e.g., in autoimmune disease, transplantation, or
drug-hypersensitivity). Pairs with the R PheWAS multiple-testing
default, which was never calibrated for HLA-allele-count testing.

**Follow-ups.** Extract the recommended ancestry-specific thresholds
and file them in your methods notes for the next HLA-adjacent PheWAS.

---

### 7. Local ancestry-informed rare variant burden testing improves gene discovery in admixed populations

**Authors.** P Kore, T Tan, W Lu, A Manuel-Friedman, L Hu et al.
**Venue.** medRxiv, 2026-07-13.
**Signal source.** Google Scholar related-research feed for Joshua C. Denny (07-20 20:52Z).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (rare-variant methods, admixed populations); variant interpretation (LOFTEE / pLoF burden methods sub-thread).

**What the paper does (from abstract).** Local-ancestry-informed rare
variant burden test — extends SKAT / burden methods to weight variants
by local-ancestry context in admixed cohorts, addressing the miscall
that global-ancestry burden tests make when frequency and effect vary
by local ancestry.

**Why it matters for your work.** Directly applicable to AoU's
admixed sub-cohorts (African-ancestry, Hispanic/Latino), where rare-
variant burden tests without local-ancestry conditioning have been
known to under- and over-count. Pairs with your existing pLoF burden
work in AoU.

**Follow-ups.** Check whether the method is packaged (R / Python) and
whether they benchmark against SAIGE-GENE+.

---

### 8. Biobank-scale genotype similarity search and dynamic patient-matched cohort creation with GenoSiS

**Authors.** K Schneider, M Chowdhury, M Tepper, JB Khan et al.
**Venue.** *Genome Research*, 2026-07-10.
**Signal source.** Google Scholar related-research feed for Lisa Bastarache (07-20 20:52Z).
**Bucket.** HIGH.
**Threads served.** Biobanks with EHR linkage (infrastructure).

**What the paper does (from abstract).** GenoSiS builds a **genotype
embedding** and uses **Intel scalable vector search (SVS)** to return
top-k genotype-similar patients on demand — enabling *dynamic* cohort
matching for any query patient (rather than up-front batched matching).

**Why it matters for your work.** Dynamic genotype-similarity matching
is exactly the primitive PheWAS + phenome-scale case-control needs
when the case set is a rare-variant carrier group and you want an
ancestry-matched control per carrier rather than a global control pool.
Worth watching whether the AoU Researcher Workbench acquires this as a
primitive.

**Follow-ups.** Check whether GenoSiS is open source and whether it
runs on AoU-scale (~245K WGS) with the vector-search index feasibly
built in-workspace.

---

### 9. Strengths and Limitations of All of Us Data Use for Public Health Research

**Authors.** C Lewis V, D D'Angelo, J Zhong.
**Venue.** *American Journal of Public Health*, 2026.
**Signal source.** Google Scholar related-research feed for Joshua C. Denny (07-20 20:52Z).
**Bucket.** HIGH (reference utility).
**Threads served.** Biobanks with EHR linkage (AoU meta / cohort profile).

**What the paper does (from abstract).** Cohort-profile-style paper
on AoU — coverage, representation of historically underrepresented
groups, and known limitations for population-health inference.

**Why it matters.** File as your default "what is AoU" citation for
any manuscript introduction where you don't want to burn a citation
on the 2018 or 2019 program-design papers. Especially useful when the
target audience is public-health rather than genomics-native.

---

### 10. Adaptive Penalization and Bootstrap-Smoothed Inference for Two-Sample Mendelian Randomization with Summary Data

**Authors.** M Qasim, K Wang, IS Bhatt.
**Venue.** arXiv 2607.18503v1, submitted 2026-07-20 (stat.ME).
**Signal source.** `arxiv-digest` 2026-07-22 (keyword hits: `causal inference`, `mendelian randomization`; score 2).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (Mendelian randomization); causal inference.

**What the paper does.** Two lasso-type procedures for two-sample MR
on summary data:

- **MR-ALasso** — MR-Lasso with adaptive penalty weights on
  pleiotropic effects; oracle-type post-selection behavior and
  consistent identification of invalid instruments (theory shown under
  the two-sample summary-data framework).
- **MR-ALasso-B** — MR-ALasso + bootstrap smoothing for reliable
  post-selection coverage / type-I control.

R package **`MRAlasso`** released.

**Why it matters.** MR-Lasso's known weakness — brittle
invalid-instrument identification and unreliable post-selection
inference — is precisely what MR-ALasso is designed to fix. Adopt this
as the default two-sample MR lasso variant going forward; pair with
`MendelianRandomization` and `TwoSampleMR` in R.

**Related-context flag.** Also this window in the Denny feed: Liu,
Huang, Purushotham, Sofer, *Reassessing Instrument Strength in
Two-Sample Mendelian Randomization Analysis* (medRxiv 2026-06-16) —
argues that conventional F-statistic thresholds understate instrument
weakness in two-sample MR. Read the two together: MR-ALasso addresses
invalid-instrument selection; Liu/Sofer addresses weak-instrument
diagnosis. Both are pre-analysis checks you'd want in place before
publishing an MR estimate.

---

### 11. Identifying sex-specific sub-phenotypes of Alzheimer's disease progression using longitudinal electronic health records

**Authors.** W Meng, Q Yang, J Xu, Y Huang, C Wang, Q Song et al.
**Venue.** *EBioMedicine*, 2026.
**Signal source.** Google Scholar author feeds for **both** Joshua C. Denny and Lisa Bastarache (07-20 20:52Z). Cites "PheWAS: demonstrating the feasibility of a phenome-wide scan…" (Denny 2010) and "Using phecodes for research with the electronic health record" (Bastarache 2021).
**Bucket.** HIGH.
**Threads served.** Chronic disease clustering & multimorbidity; EHR phenotyping.

**What the paper does (from abstract).** Deep-learning framework for
uncovering sex-specific AD sub-phenotypes from longitudinal EHRs.
Motivation: women are ~2/3 of AD patients but sex-specific progression
heterogeneity is under-characterized.

**Why it matters for your work.** Direct instance of the "unsupervised
sub-phenotyping from longitudinal EHR" pattern the multimorbidity /
clustering thread cares about — with the extra angle that stratifying
by sex materially changes what clusters emerge. The dual PheWAS +
phecode citation profile suggests it will show up as a reference
citation in future AD sub-phenotype work.

**Follow-ups.** Check whether they externally validated in a second
EHR site; check whether the discovered clusters map to phecode
neighborhoods or to novel patterns.

---

### 12. Hiding in plain sight: uncovering the genetic basis of complex phenotypes through low-risk groups

**Authors.** AI Vazquez, Y Li, G Lu, H Neelam, MS Bray, S Shrestha et al.
**Venue.** *Genetics*, 2026.
**Signal source.** Google Scholar new-citations feed for Joshua C. Denny (07-20 20:52Z). Cites "The 'All of Us' research program".
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (PRS / trait-architecture).

**What the paper does (from title + citation).** Reframes GWAS by
anchoring on the *low-risk* (resistance) tail of the phenotype
distribution rather than the case tail. Argues that low-risk groups
carry information about the genetic architecture that is systematically
under-analyzed.

**Why it matters for your work.** Pairs with the Souaiaia et al.
*Nature* paper from the 06-20 report — which argued that PRS tails
have distinct genetic architecture from the bulk. Vazquez comes at the
same problem from the resistance side; together they suggest a
sub-thread on **"the two tails of a polygenic distribution differ from
the bulk and from each other."** Directly relevant when you're
communicating why an AoU top-1% PRS carrier is *not* a
scaled-up-median-effect person.

**Follow-ups.** Read to see whether they operationalize "low-risk" as
(a) age-of-onset extremes among unaffected, (b) high-risk-exposure
survivors, or (c) something else — the definition changes what the
finding means for PRS cutoffs.

---

## Methods-watch (log-only)

- **Novel associations of Claudin gene variants with kidney stone
  disease** (Liu, Haverfield, MacKenzie, Dufresne, Ryan et al.,
  *Clinical Kidney Journal*, 2026; Denny + Bastarache feeds). PheWAS
  methods applied to CLDN family variants and kidney stones. Reference
  instance of R PheWAS in a claudin-family scan.
- **Integrating Genetic Data and Electronic Medical Records to
  Reassess Variant Pathogenicity in the Taiwanese Han Population**
  (Lin, Liu, Chen, Liao, Tsai, *Genes*, 2026; keyword hit on `variant
  interpretation`). ACMG-style reclassification in a new-ancestry EMR
  cohort. Worth citing whenever the "population-specific
  reclassification" claim is made.
- **BoltzOmics: Predicting genetic variant effects on drug binding
  with Boltz-2** (Ngo, Carraway, Clancy, Amini, *iScience*, 2026;
  Denny feed). Structure-prediction-based variant-effect on
  drug binding. Adjacent to variant interpretation but heavier on
  molecular modeling than the ACMG lane; log-only unless the tool
  becomes a reference in your work.
- **Comparing Missing Data Methods for Estimating ATEs Under
  Time-Varying Confounding** (Swallow, Brestrich, Velasco-Pardo,
  arXiv 2607.17775, stat.ME; `arxiv-digest` 07-21). Simulation
  comparison of MICE / hot-deck / single-mode / complete-case under
  ATE + PS weighting with MAR/MNAR + time-varying confounding. Useful
  reference-table paper — file for the next AoU emulation with
  substantial missingness.
- **An unsupervised clustering analysis of breast cancer data derived
  from EHRs enhanced through UMAP dimensionality reduction** (Chicco,
  Benvenuto, arXiv 2607.19089, cs.LG; `arxiv-digest` 07-22). UMAP+
  DBSCAN on three EHR breast-cancer datasets. Off-thread as a
  substantive contribution but a natural methods reference when your
  multimorbidity / clustering thread needs a UMAP-then-density
  pipeline citation.

## Off-thread this window (log-only)

- **Modular PheWAS reveals the therapeutic heterogeneity landscape of
  Danghong injection on stable angina pectoris** (Li et al.,
  *Molecular Biomedicine*, 2026; `phenome wide association studies`
  keyword feed). PheWAS applied to a traditional-Chinese-medicine
  injection formulation — methodologically real, substantively off-
  thread. Log-only.
- **Whole-genome discovery of pathogenic snRNA variants and efficient
  extended-exome screening** (Nakano et al., *iScience*, 2026; Denny
  feed). Rare-disease WGS reanalysis of 1,578 probands surfacing
  pathogenic RNU4-2 / RNU2-2 / RNU5B variants. Adjacent to the rare-
  disease thread but the paper's contribution is in the snRNA-loci
  gap, which doesn't intersect your active work.
- **Harmonised benchmarking of foundation models for single-cell and
  spatial transcriptomics reveals context-dependent generalisation**
  (Chen et al., arXiv 2607.17227, q-bio.GN; `arxiv-digest` 07-21).
  Single-cell FM benchmark — worth being aware of for method-comparison
  arguments but off-thread here.
- **Interpretable ML survival prediction of breast cancer from
  lifestyle factors — UK Biobank** (Yao et al., *Breast Cancer*, 2026;
  UK Biobank keyword feed). Off the current active-disease threads.
- **XTSE-Net: A Unified Offline and Online Target Speaker Extraction
  System** (Meng et al., speech-processing conference paper). False
  positive on the `variant interpretation` keyword — matched on
  "variant of the system" or similar; not biomedical.
- **Depression, Antidepressant Use, and Glycemic Control Among
  Adults with Diabetes — AoU (APHA 2026 abstract)** (Sule et al.).
  Conference-abstract level; note as a datapoint that AoU is being used
  for antidepressant-glycemic-control questions but nothing further to
  extract from the abstract snippet.

## Pipeline notes

- **arxiv-digest weekend fetch was uneventful.** 07-18 through 07-20
  produced zero-match digests (dry weekend, no rate-limit failure);
  07-21 came back with 4 papers and 07-22 with 2. The aggressive 5-s
  client delay + 15-s inter-category pause introduced after the 06-20
  429 storms appears to be holding.
- **No signal from the arxiv daily category mailing list this window
  that isn't already captured upstream.** Those emails route to
  `rabble@arxiv.org` and aren't triaged here.
- **NCBI "All of Us" alert was quiet for four days then hit high on
  07-22.** Consider whether the search string could be tightened —
  the four preceding-day emails had no on-thread hits, which suggests
  the search is either broader than needed or that the AoU literature
  had a quiet week.

---

*Generated 2026-07-22 as a scheduled routine run against the last five
days of email + `digests/` output. Nothing here reflects full-text
reading beyond arxiv-digest's own abstract-only capture.*
