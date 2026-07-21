# Research digest report — 2026-07-21

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-18 → 2026-07-21** (rolling four-day window since the
prior report; covers the weekend so the volume is compressed).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-07-18 → 07-21 | Large 07-20 20:52Z author batch (Denny, Hripcsak, Bastarache, Hernán, Yang, Montgomery, Karczewski, Szolovits, Callahan, Zitnik, Natarajan, Luo, Ryan, Brandt, Chenjie Zeng self-feed) + 07-19 tail + 07-18 batch. Keyword feeds (`All of Us`, `UK Biobank`, `APOL1`, `phenome wide association studies`, `clonal hematopoiesis`, `electronic health records`, `rare diseases`, `variant interpretation`, `foundation models & EHR`, `knowledge graph`) fired 07-19 and 07-21. |
| `arxiv-digest` repo (`digests/`) | 2026-07-18 → 07-21 | **07-18 = 0 papers** (1 previously surfaced, suppressed); **07-19 = 0 papers**; **07-20 = 0 papers**; **07-21 = 4 papers** (2 on-thread — an EHR-HTE target-trial-emulation paper and a federated GLP-1 mediation paper). The three empty days are consistent with a quiet weekend (Fri–Sun submissions), not a fetch failure — the 07-21 run pulled a 96h backfill cleanly. |
| NCBI "My NCBI What's New" (`All of Us`) | 07-20, 07-21 | Two aggregate digests. |
| medRxiv Collection Alert | 07-20 | Epidemiology / Genetic & Genomic Medicine / Health Informatics / Obstetrics collections; not individually triaged here. |

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The arxiv-digest paper block
> below is the full abstract (the digest fetches those verbatim). The
> reports on Scholar-sourced papers contextualize the alert snippet
> against your research threads; nothing there reflects full-text reading.

---

## Executive summary

- **Two papers this window collapse the PheWAS ↔ PGS ↔ rare-variant
  triangle you keep circling.** Baya, Lassen, Hill, Venkatesh, Currant
  et al. — *Individuals who deviate from polygenic expectation are
  enriched for damaging variants in genes linked to rare disease*
  (*Am J Hum Genet*, 2026) — surfaces in the **Joshua Denny** and
  **Stephen Montgomery** related-research feeds. The design *inverts* the
  usual PGS-tails question: instead of asking "what's the phenotype of
  the PGS-high tail?", it asks "who deviates *from* their PGS-predicted
  phenotype, and are those individuals enriched for pathogenic rare
  variants in OMIM-linked genes?" This is directly the **composite-risk-
  models-stacking-PRS-with-rare-pathogenic-variants** thread in
  `INTERESTS.md` — but with the discovery direction reversed, so it
  functions as a *screening design* for penetrant monogenic variants
  hidden inside common-disease cohorts (the same population-screening
  vs clinically-ascertained distinction you flag under PheWAS/PheRS).
  **HIGH — read first.** Pair-read with the Shelley/Bastarache/Mosley
  correction (below) which is doing the mirror-image thing —
  characterizing how PGS *modifies* penetrance of a known monogenic
  variant (Duffy-null → neutropenia). Together they bracket both
  directions of the composite-risk question.
- **A Nature paper on longitudinal EHR + genetic discovery you should
  not miss.** Urbut, Ding, Nakao, Koyama, Misra et al. — *A Bayesian
  Framework for longitudinal EHR and genetic discovery* (*Nature*, 2026,
  *Lisa Bastarache citations* feed). Only the citation notice is in
  hand — no abstract snippet was included in the alert — but the venue,
  the framing ("longitudinal EHR and genetic discovery"), and the
  Bastarache citation together mark this as **the** EHR-genomics
  methods paper of the window. Directly on the EHR-linked-biobank +
  PheWAS + genetic-epi threads simultaneously. **HIGH.**
- **A GxE-on-PGS paper in Nature Genetics reframes PGS transportability
  as an interaction problem.** Nagpal & Gibson — *Pervasive interactions
  between exposures and polygenic risk can inform more effective clinical
  and behavioral interventions* (*Nature Genetics*, 2026, *Denny
  related-research* feed). The claim that PGS×exposure interactions are
  *pervasive* — not the exception — reshapes the "why doesn't my UKB PGS
  work in AoU?" question from an ancestry-transportability story to
  (partly) an environment-transportability story. Directly on the
  ancestry-aware-risk-scores / PGS portability thread. **HIGH.**
- **Today's arxiv-digest #1: EHR-derived heterogeneous treatment effects
  emulating DAPA-HF at Mayo.** Li, Lee, Li, Liu, James, Pellikka, Tao,
  Zong — *Optimizing Clinical Trial Protocols Using EHR-Derived
  Heterogeneous Treatment Effects* (arXiv 2607.16934, stat.AP,
  submitted 07-18). Two-arm Meta-S learner + decision-tree HTE
  stratification of dapagliflozin vs placebo in HFrEF from Mayo Clinic
  Cloud EHR; overall null (HR 1.68, p=0.15) but the HTE-defined
  "beneficial" subgroup shows HR 0.20 (p=0.0002) and the "harmful"
  subgroup HR 6.68 (p<0.0001). Directly on the causal-ML +
  target-trial-emulation + ML-for-precision-health threads
  simultaneously. **HIGH — full abstract in §1 below.** Read with the
  usual HTE-optimism-bias caveat: dendrogram-defined subgroups in a
  single EHR are the classic overfit risk.
- **Today's arxiv-digest #2: federated mediation across an EHR
  network — a template you could reuse.** Jang, Radwan, Risk, Lee,
  Bian, Shi, Guo, Zhao — *Privacy-preserving causal mediation analysis
  using distributed EHR networks* (arXiv 2607.17958, stat.AP, submitted
  07-20). Renewable-learning + counterfactual mediation; only
  low-dimensional summary statistics exchanged; validated on 32,146
  patients in Indiana Network for Patient Care asking what fraction of
  GLP-1RA → HbA1c effect is mediated through BMI (answer: small).
  Directly on the GLP-1 pharmacoepi + federated-EHR + causal-inference
  threads. **HIGH.**
- **A Vanderbilt/AoU-adjacent SSRI pregnancy-outcomes paper in JAMA
  Network Open.** Aref, Hughey, Shirazi, Sucre, Bastarache — *Neonatal
  Outcomes Following Selective Serotonin Reuptake Inhibitor Use During
  Pregnancy* (*JAMA Netw Open*, 2026, *Denny related-research* feed).
  Bastarache-group EHR pharmacoepi in pregnancy — a design pattern
  worth cataloging even if pregnancy isn't your primary thread. **HIGH
  (methods-pattern-adjacent).**
- **A "low-risk-groups" GWAS design that cites All of Us.** Vazquez, Li,
  Lu, Neelam, Bray, Shrestha et al. — *Hiding in plain sight: uncovering
  the genetic basis of complex phenotypes through low-risk groups*
  (*Genetics*, 2026, *Denny citations* feed). Reverses the usual
  case-enriched design — leverage individuals who are polygenically
  low-risk but still develop disease (or vice versa) — cites AoU. Same
  design logic as Baya et al. above; the two are complementary.
  **HIGH.**
- **A big multi-biobank GWAS of healthcare expenditure (1.4M
  individuals).** May-Wilson, Lee, Nakanishi, van der Laan et al. —
  *Quantifying the contribution of genetic variation to healthcare
  expenditure across diverse healthcare systems* (medRxiv, 2026,
  *Denny citations* feed). 11 studies, 7 countries, up to 1,429,889
  individuals. Novel outcome (economic outcomes as heritable trait
  across health systems), cites AoU APOE-PheWAS. **HIGH for the design
  novelty and the scale; medium for direct thread-fit** — genetic
  economics is adjacent to, not squarely on, your active threads.
- **A colorectal-cancer PRS + registry paper directly on your
  disease-of-record thread.** Nøhr, Overby, Nielsen, Torp et al. —
  *Combining genome-wide polygenic scores with registry data for
  colorectal cancer risk-based screening: Genetics and Genomics* (*Br J
  Cancer*, 2026, *Jian Yang related-research* feed). CRC PRS + national
  registry — risk-based screening deployment. Directly on your CRC-
  susceptibility line of work. **HIGH.**
- **A Chenjie-Zeng self-feed near-miss** — the alert titled
  "*Feasibility & clinical utility of Comprehensive Geriatric Assessment
  … in older adults with prostate cancer on Androgen Deprivation
  Therapy*" (Balachandran et al., 2026) appears in your own
  new-related-research feed but is only tangentially tied (geriatric
  onco co-management, not genetic-epi or PheWAS). **SKIP.**

---

## Detailed reports — HIGH-priority studies

### 1. Li et al. — Optimizing Clinical Trial Protocols Using EHR-Derived Heterogeneous Treatment Effects

- **Authors:** Xiaodi Li, Munhuwan Lee, Pengyang Li, Xiaoke Liu, Jose K. James, Patricia A. Pellikka, Cui Tao, Nansu Zong
- **Venue:** arXiv 2607.16934v1 (stat.AP), submitted 2026-07-18
- **Source:** GitHub `arxiv-digest/digests/2026-07-21.md` (score 2 — hit
  on `electronic health records` + `heterogeneous treatment effects`)
- **Threads:** causal-ML, target-trial emulation, ML-for-precision-
  health, EHR-linked biobanks (Mayo Clinic Cloud), pharmacoepidemiology
  (SGLT2i)

**Design.** Emulation of the DAPA-HF trial (dapagliflozin vs placebo in
HFrEF) using Mayo Clinic Cloud (MCC) EHR data. All-cause mortality is
the outcome, Cox proportional hazards is the estimator, HTEs are
estimated with a Meta-S learner, and subgroups are defined via a
decision-tree thresholding of the estimated CATE surface. Two
subgroups: "beneficial" (low HTE, expected large benefit from
dapagliflozin) and "harmful" (high HTE, expected excess mortality).

**Headline result.** Overall cohort: **HR 1.681, 95% CI 0.828–3.413,
p=0.1507** — a null (and directionally the wrong sign — trend toward
harm — which is already a warning about confounding by indication
compared to the trial's benefit). Beneficial subgroup: **HR 0.203, 95%
CI 0.087–0.476, p=0.0002**. Harmful subgroup: **HR 6.680, 95% CI
2.759–16.171, p<0.0001**. The authors frame this as "HTE-guided
stratification uncovers clinically meaningful beneficial and harmful
treatment-effect patterns that are masked in full-cohort emulation."

**Why it lands on your threads.** This paper is directly the
intersection of three of your active lines: causal ML on real-world
data (meta-learner HTE estimation), target-trial emulation as a design
discipline, and ML-for-precision-health tied to a concrete clinical
decision (who should be started on dapagliflozin?). The trial being
emulated (DAPA-HF) is a canonical target-trial example, and MCC is a
credible single-site EHR source. The paper also implicitly participates
in the GLP-1/SGLT2i pharmacoepi thread you've kept warm.

**Why to be skeptical.** Two red flags that deserve a careful read of
the methods before you cite this:

1. **Overall-cohort HR 1.68 in the wrong direction.** DAPA-HF's
   randomized ATE was HR ~0.83 for all-cause mortality. If the
   emulated cohort in aggregate is producing HR 1.68, then either the
   confounding-by-indication adjustment (propensity score / IPW /
   g-formula — the abstract doesn't say which) is failing badly, or the
   cohort selection differs materially from DAPA-HF's inclusion
   criteria in ways that flip the sign. Splitting a mis-estimated ATE
   into "beneficial" and "harmful" subgroups is exactly the setup where
   a decision-tree HTE model recovers *artifactual* heterogeneity that
   is really just uncorrected confounding leaking through the CATE
   surface.
2. **Decision-tree HTE-subgroup thresholds are the classic
   internal-validation-only trap.** The HR 0.20 and HR 6.68 are
   sample-split estimates that will shrink substantially under
   cross-validation or external validation. If the paper doesn't
   present a held-out MCC subset or an external-site replication
   (Vanderbilt / AoU / MVP would all be natural), the effect sizes
   should be read as upper bounds.

**Handle for a comment / follow-up.** This is a citable comparator for
any HTE-in-EHR paper you draft in the next year, and it's a natural
external-replication candidate for the DAPA-HF emulation on the AoU
CDR (v9 srWGS-linked EHR would give you SGLT2i initiators and a Cox
follow-up out of the box). Worth flagging for the *Advances* Zeng-group
seminar deck.

---

### 2. Jang et al. — Privacy-preserving causal mediation analysis using distributed EHR networks

- **Authors:** Hyojung Jang, Rotana Radwan, Malcolm Risk, Yao Lee, Jiang
  Bian, Xu Shi, Serena Guo, Lili Zhao
- **Venue:** arXiv 2607.17958v1 (stat.AP), submitted 2026-07-20
- **Source:** GitHub `arxiv-digest/digests/2026-07-21.md` (score 1,
  keyword hit `glp-1`)
- **Threads:** causal inference, GLP-1 pharmacoepi, EHR-linked
  biobanks (Indiana Network for Patient Care as the applied cohort),
  federated learning

**Design.** Renewable-learning-based federated framework for
counterfactual causal-mediation analysis: sites exchange only
low-dimensional summary statistics rather than patient-level records,
so natural direct and indirect effects (NDE / NIE) can be estimated
without an IRB-blocking data-transfer step. Validated by simulation
(federated ≈ pooled estimator) and by a real analysis in 32,146
patients from the Indiana Network for Patient Care asking: **what
fraction of the GLP-1 RA → HbA1c reduction is mediated by BMI change?**

**Headline result.** The BMI-mediated pathway accounts for **only a
small proportion** of the overall GLP-1 → HbA1c effect, i.e. most of
the glycemic benefit is *not* via weight loss. Consistent with the
now-established RCT / DPP-4 comparator literature that GLP-1s have a
weight-independent glycemic mechanism.

**Why it lands on your threads.** Three-way hit:
- **GLP-1 pharmacoepi thread** — the applied question (mechanism of
  glycemic benefit) is exactly the kind of question your GLP-1 real-
  world-evidence work has been circling.
- **Causal-inference / g-methods thread** — proper counterfactual
  mediation (NDE/NIE) rather than the older Baron-Kenny difference-in-
  coefficients approach.
- **Federated / privacy-preserving EHR thread** — a genuinely reusable
  method for the AoU + multi-site EHR consortium designs where central
  pooling is blocked. This is a template you could apply to a
  CFTR-modulator mediation question (e.g. how much of Trikafta's FEV₁
  benefit is mediated by sweat-chloride change vs. direct effect)
  where the constituent CFTR-modulator cohorts sit inside different
  registries that don't share raw data.

**Skeptic's note.** "Renewable learning" is a specific stream (Luo &
Song, Ma & Song) — the estimator relies on parametric assumptions for
the mediator model and outcome model, and the CI coverage in the
low-communication regime typically depends on a working parametric
family. The abstract doesn't specify sensitivity to unmeasured-
mediator-outcome-confounding, which is where mediation analysis on
observational EHR data most often breaks. A read of the full paper
should focus on (a) which counterfactual estimator is used (natural vs
interventional NDE), and (b) whether the authors ran an E-value or
similar sensitivity analysis for unmeasured M-Y confounding.

---

### 3. Baya et al. — Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease

- **Authors:** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh, H. Currant, et al.
- **Venue:** *American Journal of Human Genetics*, 2026 (Cell Press)
- **Source:** Google Scholar — *Joshua Denny related-research* feed
  (07-18) AND *Stephen Montgomery related-research* feed (07-19); the
  double surfacing is a strong "read this" signal.
- **Threads:** genetic epidemiology (PRS × rare-variant composite),
  PheWAS/penetrance, rare disease, variant interpretation

**Snippet from alert:** *"Polygenic scores (PGSs) stratify disease risk
but often fail to capture individual variation. 'Misaligned'
individuals, whose observed phenotypes deviate from their genetically
expected values based on PGS, provide a powerful model for identifying
[damaging variants in rare-disease-linked genes]."* — cell.com/ajhg,
S0002-9297(26)00200-4.

**Why it lands squarely on your `INTERESTS.md`.** The `Genetic
epidemiology` thread flags "**composite risk models stacking PRS with
rare pathogenic variants**" as a priority. This paper realizes the
composite-risk idea in the *inverse* direction: instead of stacking PRS
+ rare variants as parallel predictors, it uses the *residual* between
PGS-expected phenotype and observed phenotype as an enrichment signal
for penetrant rare variants. This is a screening design — a way to
find monogenic disease hiding inside a large biobank whose members are
not clinically ascertained for rare disease. Combined with the
"penetrance-estimation-in-population-screening-vs-clinically-
ascertained-cohorts" bullet under PheWAS/PheRS, this paper is
methodologically load-bearing for you.

**Reading strategy.** Priority questions to answer on a full-text
read:
1. Which biobanks were used (UKB alone, or UKB + something else)? If
   UKB-only, the method's generalization to AoU (more diverse, more
   missing labs) is an open question you could answer in a companion.
2. What phenotypes were tested? If they're anthropometric / quantitative
   biomarker only, the extension to phecode-defined disease outcomes is
   your Zeng-group differentiator.
3. What was the enrichment odds ratio for OMIM-gene damaging variants
   in the misaligned tail, and how does it scale with PGS
   heritability?
4. Does the enrichment hold for VUSes (or only known-P/LP)? If it holds
   for VUSes, this is a variant-reclassification signal (ACMG PS3-
   equivalent evidence at population scale).

**Skeptic's note.** The design has a subtle circularity risk: if the
GWAS underlying the PGS included any of the pathogenic-variant
carriers, the "deviation from PGS" is partly capturing the same
signal. The paper's LOO / independent-validation strategy is worth
checking closely.

**Pair-read.** Read alongside Vazquez et al. (§7 below) — same design
logic in mirror-image, published in *Genetics*, so the field is
converging on this idea in the same week.

---

### 4. Shelley et al. (correction) — Polygenic Variation Underlying Neutrophil Counts Modifies the Penetrance of Duffy-Null Neutropenia

- **Authors:** J.P. Shelley, M. Shi, L. Bastarache, C.P. Chung, J.D. Mosley
- **Venue:** *American Journal of Hematology*, 2026 (correction notice)
- **Source:** Google Scholar — *Joshua Denny related-research* feed
  (07-18)
- **Threads:** PheWAS/PheRS penetrance-estimation, ancestry-aware risk
  scoring, APOL1-adjacent (Duffy-null is an ancestry-informative allele
  with health disparity implications), composite risk

**What this is.** A correction to the previously published Shelley
et al. paper showing that individual polygenic variation in neutrophil
counts modifies the penetrance of the Duffy-null (ACKR1) neutropenia
phenotype in African-ancestry individuals. The parent paper is a
canonical instance of the population-screening-penetrance vs
clinically-ascertained-penetrance distinction you flag in
`INTERESTS.md`: Duffy-null is common (~two-thirds of African-ancestry
individuals), the phenotypic penetrance to clinically-significant
neutropenia is highly variable, and a polygenic-neutrophil-count PRS
captures a substantial fraction of that variance in penetrance.

**Why it matters even though it's "just a correction."** Two reasons:

1. **The correction itself is a signal to re-examine any downstream
   analyses.** Correction notices in AJH usually come out because a
   figure, effect-size, or covariate specification was mis-stated —
   check what changed before citing the original numbers.
2. **The paper is the *mirror image* of Baya et al. above.** Baya asks
   "who deviates from PGS and are they enriched for rare variants?"
   Shelley asks "given a known monogenic-ish variant (Duffy-null), does
   the PGS modify its penetrance?" Together they bracket both
   directions of the composite-risk question. Cite them side by side.

**Handle.** For the AoU CFTR-modulator penetrance line: this is the
same architecture — a known variant (CFTR F508del), a PGS on a
quantitative modifier (e.g., a lung-function or sweat-chloride
polygenic score), and a penetrance-modification test.

---

### 5. Urbut et al. — A Bayesian Framework for longitudinal EHR and genetic discovery

- **Authors:** S.M. Urbut, Y. Ding, T. Nakao, S. Koyama, A. Misra, et al.
- **Venue:** *Nature*, 2026
- **Source:** Google Scholar — *Lisa Bastarache citations* feed (07-19)
- **Threads:** EHR-linked biobanks, PheWAS, genetic epidemiology, EHR
  phenotyping

**What we have.** Only the citation notice (Bastarache-cited) — no
abstract snippet was included in the alert. The title and the venue
are enough to flag it as a must-read: *Nature* rarely publishes
methods for longitudinal-EHR-plus-genetics without a first-author-
statistical-genetics profile, so the Bayesian framework here is
likely a new class of longitudinal joint model.

**Best guess at what's inside** (to be confirmed on full-text read):
This is likely a Bayesian latent-trajectory model over EHR-derived
longitudinal phenotypes with genetic effects as trajectory modifiers
— i.e., generalizing PheWAS-of-slopes and trajectory-cluster models to
a coherent Bayesian generative framework. If so, it directly serves
the "chronic-disease-clustering-and-multimorbidity" thread as well as
PheWAS.

**Action item.** Fetch the full text (Nature paywalled — check institutional
access) before the next report; if the model can be run on AoU CDRv9
srWGS-linked longitudinal labs, this is a candidate methods paper for
the CFTR-modulator lung-function-trajectory analysis and for the
APOL1 → CKD-trajectory analysis. **HIGH — top item to full-text read
this week.**

---

### 6. Nagpal & Gibson — Pervasive interactions between exposures and polygenic risk

- **Authors:** S. Nagpal, G. Gibson
- **Venue:** *Nature Genetics*, 2026
- **Source:** Google Scholar — *Joshua Denny related-research* feed
  (07-18)
- **Threads:** genetic epidemiology (PGS portability), PheWAS,
  ancestry / social-strata risk

**Snippet from alert:** *"The generalizability of polygenic scores
(PGS) remains a major hurdle in the pursuit of equitable genomic
medicine. Differences in disease prevalence across groups, potentially
including social strata, influence the relationship between PGS and
risk…"* — nature.com/articles/s41588-026-02674-z

**The reframe.** The transportability failure of PGS across ancestries
and cohorts is usually attributed to LD and allele-frequency
mismatch. Nagpal & Gibson's claim (as far as the snippet reveals) is
that **exposure × PGS interactions are pervasive** — i.e., the same
PGS produces different effect sizes across environmental strata
(diet, socioeconomic status, medication history, ancestry-correlated
exposures) even holding the genetic architecture constant. If true and
robust, this reframes half of the "PGS doesn't work in AoU" narrative
from an ancestry story to a shared-exposure-distribution story.

**Why it lands on your threads.** Directly on the ancestry-aware PGS
thread — but with a much larger implication: the composite PGS + rare
variant model in Baya et al. (§3) may itself need to be stratified by
exposure. If a PGS-expectation baseline shifts by 0.3 SD depending on
whether the individual is a smoker, the "deviates from PGS" signal for
finding rare-variant carriers becomes conditional on the smoking model.

**Reading strategy.**
1. Which exposures were tested? A short list of major lifestyle
   exposures vs a phenome-wide-exposure-scan changes the interpretation.
2. Are the interactions *quantitative* (change in slope) or
   *qualitative* (change in sign)? Qualitative interactions are the
   ones that break clinical use.
3. Does the pattern replicate across UKB and AoU? If it's UKB-only,
   the ascertainment (healthy-volunteer bias) is doing part of the
   work.

**Handle.** This is a citable framing paper for any grant aim on
PGS-clinical-implementation you draft in the next 12 months.

---

### 7. Vazquez et al. — Hiding in plain sight: uncovering the genetic basis of complex phenotypes through low-risk groups

- **Authors:** A.I. Vazquez, Y. Li, G. Lu, H. Neelam, M.S. Bray, S. Shrestha et al.
- **Venue:** *Genetics*, 2026 (Genetics Society of America)
- **Source:** Google Scholar — *Joshua Denny citations* feed (07-20);
  alert also flags this paper cites the AoU program paper.
- **Threads:** genetic epidemiology, PheWAS, All of Us

**The design (from the title).** Instead of doing case-enriched GWAS
in a case-control frame, focus on the *low-risk* group — individuals
who by all known factors *should not* have the phenotype — and search
for what genetic architecture is differential in that subset. This is
the same inversion as Baya et al. (§3), applied at the trait level
rather than the individual-deviation level.

**Why it lands on your threads.** The paper cites the AoU program
paper, so the applied cohort is at least partly AoU. Combined with
Baya et al., this is a *second* paper in the same week arguing that
inverse designs (look at the low-risk tail) recover signal that
case-enriched designs miss. If both papers hold up on close reading,
this is a real methods shift worth tracking.

**Pair with:** Baya et al. (§3) — direction-inverted but complementary
design logic.

---

### 8. May-Wilson et al. — Quantifying the contribution of genetic variation to healthcare expenditure across diverse healthcare systems

- **Authors:** S. May-Wilson, J. Lee, T. Nakanishi, C.M. van der Laan et al.
- **Venue:** medRxiv, 2026-07-15 (preprint)
- **Source:** Google Scholar — *Joshua Denny citations* feed (07-20);
  alert flags citation of *Phenome-wide association of APOE alleles in
  the All of Us …*
- **Threads:** genetic epidemiology, PheWAS/PheRS, EHR-linked
  biobanks (11-cohort international)

**Snippet from alert:** *"…we examine how genome-wide genetic
variation contributes to healthcare costs, analysing inpatient,
outpatient, primary care and prescription drug expenditure in up to
1,429,889 individuals from 11 studies across 7 countries. We identify
hundreds of common genetic variants robustly [associated with
healthcare expenditure]."*

**Why it's notable at all.** Healthcare-cost-as-heritable-trait is a
novel outcome for a GWAS meta-analysis, and 1.43M individuals across
11 biobanks is on the scale of the largest GWAS ever done. The
policy-relevance angle is obvious (which trait clusters drive cost?
are there ancestry disparities in cost attributable to genetic
architecture?), but the causal-inference framing needs care —
healthcare cost is downstream of access, insurance, and country-level
policy, so the effect sizes will confound biology with health-system
structure.

**Why it lands on your threads.** Direct citation of AoU-APOE-PheWAS
puts this paper in the same design family as your work. The
11-biobank meta-analysis machinery (harmonized expenditure phenotype
across countries) is a methods asset — even if the outcome is not
your primary interest, the harmonization strategy is directly reusable
for a cross-biobank rare-cancer PheRS or cross-biobank CFTR-modulator
outcomes comparison.

**Handle.** Skim for the harmonization protocol. If the authors
document a reproducible ETL from OMOP-CDM / TriNetX / FinnGen /
BioBank Japan billing data to a common expenditure phenotype, that
protocol has independent value.

---

### 9. Aref et al. — Neonatal Outcomes Following Selective Serotonin Reuptake Inhibitor Use During Pregnancy

- **Authors:** L. Aref, J.J. Hughey, S. Shirazi, J.M.S. Sucre, L. Bastarache
- **Venue:** *JAMA Network Open*, 2026
- **Source:** Google Scholar — *Joshua Denny related-research* feed
  (07-18)
- **Threads:** causal inference / pharmacoepi, EHR phenotyping,
  Vanderbilt/BioVU-adjacent

**Why it's on your radar.** Bastarache-group Vanderbilt pharmacoepi
paper — Aref, Hughey, and Sucre are all in the VUMC informatics /
pediatrics orbit. The design pattern (drug exposure during pregnancy
→ neonatal outcome, EHR-derived) is exactly the kind of PheRS-adjacent
target-trial-emulation your CFTR modulator work will need to reproduce
when Trikafta-in-pregnancy safety data matures.

**Why to read even though pregnancy isn't your primary thread.**
- The **EHR-based pregnancy phenotyping** (gestational age
  determination, trimester-specific exposure windows, neonate-linkage
  from mother-infant pairs) is the hard part, and BioVU has developed
  this pipeline over the last few years. Any documented pipeline is
  reusable.
- The **negative-control-outcome / negative-control-exposure** strategy
  Bastarache-group typically uses is worth cataloging.
- **Sucre** is a NICU/pulmonary co-author — this may be one of the
  first VUMC papers linking BioVU maternal-fetal cohort work to
  pediatric pulmonary outcomes, which is directly the CF-adjacent
  design pattern.

**Skip unless.** If you're not actively drafting a
CFTR-modulator-in-pregnancy analysis or a peripartum pharmacoepi paper,
this can be filed for reference only.

---

### 10. Nøhr et al. — Combining genome-wide polygenic scores with registry data for colorectal cancer risk-based screening

- **Authors:** A.K. Nøhr, M.G. Overby, M.M. Nielsen, E.A. Torp et al.
- **Venue:** *British Journal of Cancer*, 2026
- **Source:** Google Scholar — *Jian Yang related-research* feed
  (07-19)
- **Threads:** genetic epidemiology (PRS), cancer genetic epidemiology
  (colorectal — one of your first-author disease areas), rare disease
  (Lynch overlap), pharmacoepi (screening as intervention)

**Why it's directly on your Zeng-group work.** Colorectal-cancer PRS
combined with national registry data for **risk-based screening
allocation** is exactly the deployment step for the CRC susceptibility
work you have first-authored. The Danish registry (implied by author
names) is a fully-linked EHR-genome-outcomes setting where the
"who-to-screen" clinical decision can be tested end-to-end.

**Priority questions on read.**
1. Which PGS was used (GECCO-derived, PRS-CS-derived, or a new
   Danish-specific score)? PRS choice is the load-bearing input.
2. What CRC subtype resolution — right- vs left-sided vs rectal, and
   MSI-H vs MSS? Your prior work has flagged subtype-specific PRS as
   under-explored.
3. What ancestry composition? Denmark is mostly Northern European —
   how transportable are these thresholds to a US All-of-Us CRC
   cohort?
4. What's the number-needed-to-screen tradeoff at different PGS
   thresholds? This is the actual clinical decision-relevance
   question.

**Handle.** This is a natural companion citation for any Zeng-group
CRC-PRS-implementation paper. Also worth checking whether it cites
your prior CRC work — the *Jian Yang related-research* feed
suggests likely.

---

### 11. Li et al. — Modular PheWAS reveals the therapeutic heterogeneity landscape of Danghong injection on stable angina pectoris

- **Authors:** B. Li, J. Liu, S. Tian, L. Zhu, D.D. Duan, Z. Wang
- **Venue:** *Molecular Biomedicine*, 2026
- **Source:** Google Scholar — `"phenome wide association studies"`
  keyword feed (07-21)
- **Threads:** PheWAS methodology, pharmacoepi (traditional Chinese
  medicine drug repurposing)

**Why it's interesting despite being TCM.** "Modular PheWAS" as a
term hasn't been formally defined in the mainstream PheWAS lineage
(Denny/Bastarache/Wei). The paper is using PheWAS in a
therapy-heterogeneity framing — mapping which phenotypes stratify
response to a specific compound — which if the "modular" formalism is
principled would be reusable for repurposing questions in Western
drug classes too (e.g., which phecode modules stratify GLP-1 response,
or SGLT2i response).

**Skeptic's note.** TCM-adjacent PheWAS papers frequently mis-apply
the framework (case-control-inflation, no phecode-exclusion-range
handling, no ancestry PCs). Read the methods to see whether "modular
PheWAS" is a real formalism or a rebranding.

**Filed as:** METHODS-WATCH, low-medium priority.

---

### 12. Coronado-Volta 2025 — Comparison of Chronic Disease Prevalence Using All of Us, NHIS, and NHANES

- **Author:** H.A. Coronado-Volta (dissertation, 2025)
- **Venue:** ProQuest dissertation
- **Source:** Google Scholar — *Joshua Denny citations* feed (07-20);
  cites the AoU implementation paper.
- **Threads:** All of Us methodology, external-validity /
  generalizability

**Why it lands on your threads.** The AoU generalizability question
(does AoU's chronic-disease prevalence match nationally representative
surveys?) is the load-bearing epidemiological question for every AoU
PheWAS or PheRS you run. If chronic-disease prevalence in AoU is
systematically shifted from NHIS/NHANES for a given condition, that's
either (a) evidence of enrichment worth reporting, or (b) evidence of
ascertainment / definition mismatch worth adjusting for.

**Reading strategy.** Just the abstract and the chronic-disease-
by-condition prevalence table are worth grabbing. The comparison
against NHANES (which includes biomarker measurements, not just
self-report) is the most informative slice.

---

### 13. Meng et al. — Identifying sex-specific sub-phenotypes of Alzheimer's disease progression using longitudinal EHRs

- **Authors:** W. Meng, Q. Yang, J. Xu, Y. Huang, C. Wang, Q. Song et al.
- **Venue:** *EBioMedicine*, 2026
- **Source:** Google Scholar — *Joshua Denny citations* feed (07-20);
  cites the Denny PheWAS-feasibility paper.
- **Threads:** chronic disease clustering / multimorbidity, EHR
  phenotyping, sex-stratified analysis

**Snippet from alert:** *"…women comprising nearly two-thirds of
individuals with AD. However, sex-specific heterogeneity in AD
progression remains insufficiently understood. A data-driven approach
is needed to characterise such heterogeneity from longitudinal EHRs.
… we developed a deep learning-based framework to uncover sex-specific
AD sub-phenotypes using longitudinal EHRs from…"*

**Why it lands on your threads.** Directly on the disease-subtype-
discovery / trajectory-clustering thread (`INTERESTS.md` §"Chronic
disease clustering and multimorbidity"). Sex-stratified sub-phenotypes
in AD is a specific instance of a design pattern that generalizes to
any complex disease where trajectory heterogeneity matters (CKD in
APOL1 carriers, CF-modulator response, IBD subtypes).

**METHODS-WATCH.** Worth checking whether the deep-learning framework
is CLMBR / MOTOR / FEMR lineage or a bespoke architecture; if it's
architecture-generic, this is a reusable pipeline.

---

### 14. Liu et al. — Novel associations of Claudin gene variants with kidney stone disease

- **Authors:** I.Y. Liu, J. Haverfield, E. MacKenzie, L. Dufresne, A.K. Ryan et al.
- **Venue:** *Clinical Kidney Journal*, 2026
- **Source:** Google Scholar — *Joshua Denny citations* feed (07-20);
  cites R PheWAS.
- **Threads:** PheWAS methodology, rare disease (FHHNC — rare
  autosomal-recessive tubulopathy), variant interpretation

**Design (from snippet).** Rare recessive variants in CLDN16 / CLDN19
cause FHHNC, and common variants in CLDN2 / CLDN10 / CLDN14 associate
with kidney stones. The paper looks phenome-wide across the *CLDN*
gene family for new stone-associated variants — a classic PheWAS-in-
a-gene-family design (cf. your CFTR-family PheWAS work).

**Why it lands on your threads.** PheWAS in a gene family with mixed
common-and-rare architecture is exactly the framing of a lot of your
first-author work. Method transferable to CFTR + ABCC1/ABCC7 family,
or to the APOL1-locus with APOL2 and MYH9 as co-tested loci.

---

### 15. Doku et al. — Detecting Friedewald-Substituted "Direct" LDL Cholesterol in a National Multi-Site EHR Cohort

- **Authors:** R. Doku, N.Y.A. Osafo, J. Kwagyan, W.M. Southerland
- **Venue:** *Journal of Applied Laboratory Medicine*, 2026
- **Source:** Google Scholar — *Joshua Denny related-research* feed
  (07-18)
- **Threads:** EHR phenotyping, lab-value QC in EHR / OMOP

**Why it lands on your threads.** A specific EHR-phenotyping-hygiene
problem: some sites report Friedewald-calculated LDL as "direct" LDL,
mixing the two lab codes. If you're doing an LDL-based PheWAS or a
PRS-vs-LDL analysis in AoU, this is a lab-QC gotcha to check. Same
pattern likely exists for other calculated-vs-measured biomarkers
(bilirubin, eGFR variants).

**Handle.** Note the paper as a QC-checklist reference; not a
must-read cover-to-cover.

---

### 16. Sajal et al. — Integrative analysis prioritizes proteins associated with renal cell carcinoma and its risk factors

- **Authors:** I.H. Sajal, A.J. Song, K.M. Brown, M.J. Machiela, P. Kraft et al.
- **Venue:** *JNCI Cancer Spectrum*, 2026
- **Source:** Google Scholar — *Konrad Karczewski citations* feed
  (07-18)
- **Threads:** genetic epidemiology (two-step MR, pQTL, cancer),
  UK Biobank

**Snippet.** *"…two-step Mendelian randomization (TSMR). In step 1,
we identified plasma proteins influenced by each risk factor
(obesity, hypertension, smoking), leveraging GWAS summary-statistics
from the UK Biobank Proteomics [Project]…"* then step 2 tests
protein → RCC.

**Why it lands on your threads.** Cancer PheWAS-adjacent methods —
plasma-protein MR is now the standard mechanism for going from
GWAS-hit to "which protein mediates the risk-factor → cancer
pathway." Directly applicable to CRC and breast cancer where your
first-author work sits. The UKB Proteomics resource (Olink 3K panel)
is publicly available and this design pattern is directly reusable
in AoU once/if AoU releases a comparable proteomic assay.

---

### 17. Jo et al. — Large-scale meta-analysis of over one million individuals reveals the genetic architecture of 127 complex traits in East Asian populations

- **Authors:** J. Jo, S.S. Khor, S.K. Chu, Y. Ji, K. Ueno, A. Ono, C.W. Chen et al.
- **Venue:** (per snippet — venue-of-record unclear from snippet;
  likely *Nature Genetics* / *Nat Comm* / *Cell Genom*)
- **Source:** Google Scholar — *Jian Yang related-research* feed (07-20)
- **Threads:** cross-ancestry / trans-ancestry portability, genetic
  epidemiology at scale

**Why it lands on your threads.** East Asian meta-analysis at 1M+
individuals is the counterpart to the UKB EUR-dominated GWAS
literature — a critical input to any trans-ancestry PGS or fine-
mapping work. Direct impact on any downstream AoU trans-ancestry
analysis you run (AoU has ~1.5% East Asian ancestry — this paper's
summary stats are the transferable input).

---

### 18. Yao et al. — Interpretable machine-learning survival prediction of breast cancer prognosis from lifestyle factors: evidence from UK Biobank

- **Authors:** Y. Yao, X. Zhai, Z. Liang, C.K. Lam, H. Xie, H.H.Y. Tong et al.
- **Venue:** *Breast Cancer (Tokyo)*, 2026
- **Source:** Google Scholar — `"UK Biobank"` keyword feed (07-21)
- **Threads:** breast cancer (your first-author disease area), ML for
  precision health, UK Biobank

**Why it's flagged.** Direct disease-area hit. Interpretability +
survival-prediction on UKB breast cancer with lifestyle factors is a
design pattern you may want to compare against for any BC-survival
manuscript. Whether the paper adds anything methodologically new
beyond the existing UKB BC survival GWAS + lifestyle-Cox literature
is the question to answer on read.

---

### 19. Sule et al. — Depression, Antidepressant Use, and Glycemic Control Among Adults with Diabetes: Evidence from All of Us

- **Authors:** P. Sule, A. Bhuiyan, A.T. Monika, F.A. Imran, D. Noor
- **Venue:** APHA 2026 Annual Meeting abstract
- **Source:** Google Scholar — `"All of Us research program"` keyword
  feed (07-21)
- **Threads:** All of Us pharmacoepi

**Why it's flagged.** A conference-abstract-tier AoU pharmacoepi
paper. Depression + antidepressant × diabetes-glycemic-control is a
GLP-1-adjacent question (SSRI-associated weight change and glycemic
effects are relevant to any GLP-1 mediation analysis). Read only if
you're actively working on the AoU-antidepressant slice; otherwise
file.

---

## METHODS-WATCH (skim, don't dive)

- **Neeley et al. — TEDDY: A Pediatric Foundation Model for Risk
  Forewarning from ICD-Coded Diagnostic Histories** (arXiv, 2026,
  *Denny citations* feed). 1.84M-parameter decoder transformer on 73M
  ICD-10 codes from 1.6M children at a single pediatric institution.
  Adjacent to the CLMBR/MOTOR/EHRSHOT/FEMR lineage in `INTERESTS.md`.
- **Karami — Deep Learning Foundations for Irregular EHR Time Series**
  (2026 dissertation, `Foundation models & EHR` keyword feed). Same
  family; skim for irregular-time-sampling tricks reusable in AoU
  labs data.
- **Chen et al. — Harmonised benchmarking of foundation models for
  single-cell and spatial transcriptomics** (arxiv-digest 2026-07-21).
  Cell-level FM, tangential to your threads (no direct EHR/biobank
  link). SKIP unless working on Perturb-seq downstream.
- **Ardakani et al. — Comparing ML methods predicting transcriptome
  from epigenome** (Genome Biology, 2026, cross-feed). TWAS-adjacent
  methods paper — matters only if you're actively running an
  epigenome-informed TWAS.
- **Ancestry-informative tobacco carcinogen metabolism study**
  (Lanade et al., Arch Toxicol, 2026, *Karczewski citations* feed).
  N=274 smokers, small — but the ancestry-AIM design in a
  pharmacometabolomic setting is a design template.

## SKIP

- Congenital-heart-disease case report (Cadena-Ullauri et al.,
  *Karczewski citations*).
- Postzygotic mutations in >11K rare-disease trios (Garcia-Salinas
  et al., AJHG, *Karczewski citations*) — interesting rare-disease
  methods but not on active threads.
- Schizophrenia animal models review (*Karczewski citations*).
- Danghong-injection PheWAS (already discussed above — filed
  METHODS-WATCH not SKIP).
- All Substack / AINews / MarkTechpost newsletters (not research
  literature).
- Bifocal Diffusion LM / ARMOR / MEDLAYXPLAIN and other pure-ML
  benchmarking papers unless tied to clinical decisions.
- Foundation model chest X-ray / gene-embedding papers (not on active
  thread unless multimodal-EHR — not the case here).

---

## Pipeline note

- The arxiv-digest pipeline behaved correctly across 07-18 → 07-21
  (no fetch failures; three quiet days followed by a healthy 4-paper
  digest on 07-21 with lookback covering the weekend). No workflow-log
  investigation needed.
- Scholar-alert delivery is on the normal cadence (07-18 daily batch,
  07-19 mid-day, 07-20 late-day, 07-21 morning). Volume is elevated
  vs baseline (~30+ alerts across the window) because 07-20 was a
  Sunday-Monday transition and Google batches accordingly.

## Follow-ups to schedule

1. **Full-text read Urbut et al. (Nature) this week.** Top item; a
   Bayesian longitudinal EHR-genetic framework in *Nature* is the
   single most-load-bearing paper of the window for your active
   methods threads. (§5)
2. **Full-text read Baya et al. (AJHG) — with Vazquez et al.
   (Genetics) as pair-read.** Composite-risk-inverse-design (§3, §7).
3. **Full-text read Nagpal & Gibson (Nature Genetics).** PGS × exposure
   interaction reframing (§6).
4. **Skim Nøhr et al. (BJC) for the CRC-PRS deployment protocol** —
   directly your Zeng-group disease line (§10).
5. **Log the pipeline design of Jang et al. federated-mediation
   paper as a reusable template** for CFTR-modulator federated
   mediation work (§2).
6. **Note the DAPA-HF-emulation HTE red flags** before citing Li et
   al. (§1) — the overall-cohort HR reversal is a real concern.
