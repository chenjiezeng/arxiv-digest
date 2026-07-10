# Research inbox summary — 2026-07-10

**Sources covered**

- `arxiv-digest` runs committed to the repo: `digests/2026-07-07.md`,
  `2026-07-08.md`, `2026-07-09.md` (today's `2026-07-10.md` has not
  been committed yet as of this run).
- Gmail: Google Scholar alerts landing today (2026-07-10 05:04 UTC),
  filtered against `INTERESTS.md` (PheWAS, biobanks/EHR, OMOP, causal
  inference, variant interpretation, PRS/TWAS, EHR foundation models,
  KGs, drug repurposing, rare disease, multimorbidity).

**High-level shape**

Twelve studies clear the triage bar. The dominant cluster this week is
**polygenic scores** — three separate angles (multi-ancestry portability,
rare-variant integration, patient-level robustness / clinical
translation). One TWAS methods paper hits the Chenjie-Zeng alert
directly. Two EHR-cohort methods papers (multimorbidity network on UK
Biobank; regularized PS + doubly robust under rare exposures) sit
squarely on the multimorbidity and causal-inference threads. One All of
Us / HBOC paper hits the variant-interpretation ×
population-screening-penetrance thread.

---

## HIGH — PRS / TWAS methods and clinical translation

### 1. Multi-ancestry gene expression models amplify TWAS discovery and validation
Bledsoe, Watkins, Bowen-Moore, Shaw et al. **Nature Communications**, 2026
Alert: *Chenjie Zeng — new related research* · [PDF](https://www.nature.com/articles/s41467-026-75193-4_reference.pdf)

**Why HIGH:** Direct hit on the genetic-epidemiology thread — TWAS,
multi-ancestry portability, and cross-ancestry gene-expression prediction.
Google Scholar surfaced it against the user's own author profile, which
is a strong signal it overlaps the user's published TWAS work.

**Detailed summary (from snippet + title):**
The paper trains gene-expression prediction models jointly across ancestral
backgrounds and evaluates the incremental discovery + validation benefit
when those multi-ancestry expression models are plugged into TWAS
scans. The framing calls out that our understanding of how ancestral
background shapes genetically-determined expression is limited,
especially when models trained in one population are applied to studies
from different or multiple populations. The empirical demonstration is
that multi-ancestry training amplifies both the number of transcriptome-
wide significant associations discovered and the replicability of those
findings when carried across populations.

**Read next:** Fetch the Nature Comms PDF and check (a) which reference
panels they combined (GTEx / MESA / TOPMed?), (b) whether they benchmark
against JTI / UTMOST / MultiXcan, and (c) whether they release fitted
models — the alert flagged this as reference-list; the user's own TWAS
pipelines may want to switch prediction models.

---

### 2. MIXPRS — multi-population and multi-method PRS from summary statistics
Xu, Dong, Zeng, Bian, Zhou, Guan, Zhao. **Nature Genetics**, 2026
Alert: *Jian Yang — new related research* · [Article](https://www.nature.com/articles/s41588-026-02637-4)

**Why HIGH:** PRS / cross-ancestry portability is an explicit active
thread. "Combining multiple methods" is exactly the problem — no single
PRS method wins in every scenario, so ensembling is where the
gains are.

**Detailed summary (from snippet):**
Many multi-population PRS methods have been proposed (PRS-CSx, PROSPER,
BridgePRS, etc.) to improve prediction in underrepresented populations,
but no single method dominates. MIXPRS integrates PRSs across multiple
methods *and* multiple ancestry-specific training sources using only
GWAS summary statistics, giving a single portable score. Publication in
Nature Genetics implies substantial empirical wins over the standard
per-method baselines.

**Read next:** Confirm whether MIXPRS integrates *at the SNP-weight
level* (weighted mixture of PGS weights) or *at the score level* (linear
combination of trained scores) — the two have very different portability
properties in EHR-linked biobanks where a validation cohort is often
too small to refit weights per ancestry. Also check the software release
and whether All of Us / MVP-scale application is supported.

---

### 3. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
Baya, Lassen, Hill, Venkatesh, Currant et al. **American Journal of Human Genetics**, 2026
Alert: *Stephen B. Montgomery — new related research*

**Why HIGH:** This is a direct instance of the interest listed in
INTERESTS.md under Genetic epidemiology — "composite risk models
stacking PRS with rare pathogenic variants" — and cleanly bridges into
Rare disease.

**Detailed summary (from snippet + AJHG venue):**
The premise: individuals whose *observed* trait value deviates
substantially from what their PRS predicts (i.e., outliers on the
residual axis after PRS regression) are enriched for damaging rare
variants in genes associated with Mendelian / rare-disease forms of the
trait. This provides a population-scale, PRS-orthogonal way to prioritize
carriers of high-impact rare variants without waiting for a diagnostic
workup — you flag them by their PRS-residual.

**Read next:** Pull the PDF. Key questions the user's INTERESTS.md
implies: (a) which biobank(s) — UKB, FinnGen, AoU? (b) does the outlier-
enrichment hold on the *low-tail* symmetric to the high-tail, or is it
only high-outliers-for-disease-traits? (c) what's the sensitivity /
precision at operationally useful PRS-residual thresholds — could this
inform a population-screening funnel to increase clinical yield in
biobank-embedded return-of-results programs?

---

### 4. STELLAR — ensemble learning integrating rare variants to enhance PRS
Chen, Li, Mazumder, Zhang, Lin. **medRxiv**, 2026
Alert: *Jian Yang — new related research* · [PDF](https://www.medrxiv.org/content/10.64898/2026.06.07.26355109.full.pdf)

**Why HIGH:** Same composite (rare + common) genetic risk thread as #3
but from the methods side rather than the empirical side. Combined
methodological + empirical papers arriving in the same week is a strong
signal that composite PRS-plus-rare-burden is the current center of the
field.

**Detailed summary (from snippet):**
Existing rare-variant association tests (SKAT, burden, ACAT-V, STAAR)
aren't well-suited for direct integration into polygenic risk prediction.
STELLAR proposes a flexible ensemble framework that combines common-
variant PRS weights with rare-variant burden signal to produce a single
predictor. medRxiv preprint from the X. Lin (Harvard Biostat) group,
which typically ships open-source R/Python packages.

**Read next:** Check whether STELLAR's ensemble is a simple linear
stacking or something more expressive (kernel / gradient-boosted /
neural), and how it handles the ancestry-portability problem — since
rare-variant burdens are extremely ancestry-dependent, naïvely stacking
a EUR-trained PRS with a EUR-trained burden score can worsen disparity.

---

### 5. Advancing Clinical Implementation of Cardiovascular PRS Through Patient-Level Robustness Assessment
de la Harpe, Vaucher, Kutalik, Fellay et al. **medRxiv**, 2026
Alert: *Jian Yang — new related research* · [PDF](https://www.medrxiv.org/content/10.64898/2026.06.10.26355357.full.pdf)

**Why HIGH:** Sits at the PRS × ML-for-precision-health intersection.
The pitch — "PRSs for ASCVD can perform equivalently at the population
level yet disagree for individual patients" — is exactly the calibration
concern flagged in INTERESTS.md ("calibration, ancestry-aware risk
scores").

**Detailed summary (from snippet):**
When two PRSs report the same C-statistic on a population, they can
still classify the *same* individual into very different deciles. The
paper introduces patient-level robustness assessment — asking, for each
patient, whether the risk category is stable across reasonable PRS
choices — and evaluates it in a real cardiovascular cohort. This is the
kind of framing a return-of-results program would need before
operationalizing a PRS.

**Read next:** Whether the "disagreement" metric is a per-patient
Brier-type decomposition or a rank-shift measure, and whether they
recommend a decision rule ("only return if robust across ≥K scores") that
could plug into an EHR-embedded PRS deployment.

---

### 6. PGS Browser — a public platform for personalized polygenic score analysis and interpretation
Kolosov, Reeve, Briotta Parolo, Kurki et al. **Nature Communications**, 2026
Alert: *Jian Yang — new related research* · [PDF](https://www.nature.com/articles/s41467-026-74461-7_reference.pdf)

**Why HIGH:** Infrastructure for personalized PRS interpretation — feeds
directly into any return-of-results / clinical-translation project.
Reference-panel + interactive browser tooling would slot into the user's
biobank workflows (UKB, AoU) if the underlying reference set is diverse
enough.

**Detailed summary (from snippet):**
Positions PGSs as clinically translatable only if there is a population-
based reference resource so that any patient score can be interpreted
percentile-wise. PGS Browser makes those reference distributions
publicly queryable. Given the FinnGen-adjacent author list (Kurki, Reeve,
Briotta Parolo), the reference is likely FinnGen-anchored, which is
worth checking for AoU-portability.

**Read next:** Which populations are in the reference set, whether
ancestry-stratified percentiles are exposed, and whether the API allows
programmatic scoring (for a batch of biobank participants) or only single-
patient lookups.

---

## HIGH — All of Us / variant interpretation / population screening

### 7. Documented clinical genetic testing among carriers of HBOC variants — ancestry and socioeconomic disparities in All of Us
Yerukala Sathipati & Scott. **medRxiv**, 2026
Alert: *Joshua C. Denny — new related research* · [PDF](https://www.medrxiv.org/content/medrxiv/early/2026/06/10/2026.06.09.26355262.full.pdf)

**Why HIGH:** Combines three active threads — All of Us EHR-linked
biobank; variant interpretation × real-world clinical follow-through;
and population-screening penetrance / equity. This is the classic
"biobank finds carriers, EHR tells us how many were actually acted on"
design.

**Detailed summary (from snippet):**
HBOC (Hereditary Breast and Ovarian Cancer — BRCA1/2, PALB2, and the
ClinGen-defined moderate-penetrance genes) variant carriers benefit from
risk-reducing surgery / enhanced screening — but only when they are
identified. Using All of Us, the authors ask: among genotypically
identified carriers, what fraction have documented clinical genetic
testing in their EHR, and how does that fraction vary by genetic
ancestry and socioeconomic strata? Expected finding pattern (given the
framing "whether recognition is equitable across diverse [populations]"):
non-European-ancestry and lower-SES carriers show markedly lower
documented testing rates.

**Read next:** Which HBOC gene panel they used (ACMG SF v3.2? the wider
ClinGen-VCEP panel?), the variant classification threshold (P/LP only, or
P/LP/VUS?), and — most importantly — whether the disparity persists
after adjusting for total EHR-visit density, since undocumented testing
could be a documentation artifact rather than a true care gap.

---

## HIGH — Causal inference / pharmacoepidemiology

### 8. Which regularized propensity-score and doubly robust methods are best calibrated when exposures or outcomes are rare?
Karim & Hu. arXiv:2607.07065v1 · **stat.AP** · surfaced by `digests/2026-07-09.md`

**Why HIGH:** This is exactly the causal-inference thread — plasmode
simulation, TMLE vs IPTW, OAL / GLiDeR / HAL regularization, rare-
exposure and rare-outcome scenarios anchored on NHANES. Slots directly
into any pharmacoepi analysis using EHR-derived proxies for confounding
adjustment (the >100 prescription-derived proxy setting is the CFTR-
modulator / GLP-1 / SGLT2 scenario).

**Detailed summary (from arxiv-digest abstract):**
Plasmode simulation anchored on NHANES 2013–2018 (25 investigator-
specified covariates + 142 prescription-derived proxies) comparing 10
pipelines (regularized selection × IPTW / TMLE) under known null (true
RD = 0) across frequent, rare-exposure, and rare-outcome scenarios.
Key findings:

- **HAL + G-Computation** — near-zero bias but tightly concentrated
  estimates → over-covers to near-unity with 106–186 % relative error
  (the "conservative but useless CI" failure mode).
- **OAL-IPTW, GLiDeR, HAL-TMLE** — best-calibrated across scenarios.
- Regularized-LASSO TMLE pipelines slightly under-cover (91–93 %) in
  the rare regimes.
- Under rare exposure, LASSO-IPTW gives the largest bias and inflated
  SE — TMLE removes this failure mode.
- On real data, all methods converge to RD ≈ 0.07–0.085.
- Runtimes range < 1 s to > 16 h — the compute vs. calibration tradeoff
  is real and worth budgeting for.

**Practical takeaway:** For a real-world evidence study with rare
exposures or rare outcomes, pair outcome-aware selection (OAL / GLiDeR)
with a doubly robust estimator (TMLE). Report both compute cost and the
prioritized metric.

---

## HIGH — Multimorbidity / chronic disease clustering

### 9. Enhancing comorbidity network inference with risk-enriched health trajectories embedding
Fontana, Mapelli, Di Angelantonio, Ieva. arXiv:2607.04702v1 · **stat.AP** · surfaced by `digests/2026-07-07.md`

**Why HIGH:** Chronic disease clustering / multimorbidity thread — UK
Biobank cohort, cardiometabolic focus, and it goes beyond raw
co-occurrence by explicitly modeling shared risk factors as confounders.
The community-based patient representations → progression phenotype
clusters is exactly the "trajectory clustering" INTERESTS.md line.

**Detailed summary (from arxiv-digest abstract):**
Framework combines individual health trajectories → sparse network
estimation via Gaussian Graphical Models + LASSO, with a dedicated
confounding-evaluation step that leverages prior clinical knowledge on
shared risk factors so the network isn't dominated by trivial "both
diseases share obesity" edges. Applied to UK Biobank, 24 cardiometabolic
diseases × 76 risk factors. Recovers four disease communities aligning
with established cardiometabolic taxonomy; downstream patient
representations built from the community structure cluster into four
progression phenotypes with significantly different long-term survival.

**Read next:** How they handle the temporal / lag dimension in the GGM
step (concurrent vs lagged co-occurrence), and whether the four
progression phenotypes are interpretable enough for stratified care
pathways.

---

## MEDIUM — worth a skim

### 10. Colocalization of eQTLs with T2D and glycemic traits using WGS in diverse populations (TOPMed)
Wang, DiCorpo, Zhang, Kleinbrink, Arnett et al. **Diabetes**, 2026 · [Article](https://diabetesjournals.org/diabetes/article/doi/10.2337/db25-0557/172031)

Multi-ancestry T2D + eQTL colocalization from whole-genome sequencing
rather than imputed arrays — pulls in low-frequency and rare variants.
Adjacent to the TWAS work in #1 and useful for cross-ancestry portability
of T2D-linked expression signals.

### 11. Within-sibling attenuation of PRS accuracy — effects of PCA, LDSC, and mixed models
Kelly, Onuorah, Gilbert. 2026 · Alert: *Joshua C. Denny / George Hripcsak*

Within-sibling designs strip population stratification; PRS accuracy
that survives this filter is closer to a causal-genetic-only estimate.
Useful methods-watch for calibration audits of ancestry-aware scores.

### 12. Sex-stratified PRS for CAD incidence — 20-year cohort
Najd-Hassan-Bonab et al. **BMC Cardiovascular Disorders**, 2026

CAD PRS calibration across sex strata over 20 years — small-cohort but
relevant to the calibration thread and to the PRS-for-CV work covered by
#5. Skim for effect-size differential magnitude and whether they
recommend a sex-stratified threshold.

---

## SKIP (surfaced but off-thread)

Included so the count is honest — 25+ Scholar-alert items landed today.
The ones that scored on interest keywords but don't fit an active thread:

- *Bifocal Diffusion Language Models* (Marinka Zitnik alert) — generic
  LLM architecture, no biomedical grounding.
- *Citation-Aware Continual Pre-Training for Biomedical LMs* (Peter
  Szolovits alert) — BioNLP infra, no clinical-application loop.
- *AutoTrainess: teaching LMs to improve LMs* (Marinka Zitnik alert) —
  generic LM training method.
- *Prostate cancer TWAS* (Jonathan Pritchard citation) — narrow disease
  application, no methods novelty.
- *Foveal development GWAS* (Jian Yang alert) — ophthalmology.
- *SARS-CoV-2 Japan seroepi* (Christopher Chute alert) — off-thread.
- *Antiphospholipid Ab + Afib* (Miguel Hernán citation) — off-thread.
- *Antiviral medications review* ("drug repurposing" keyword alert) —
  narrative review, no computational-drug-repurposing angle.
- *Ghana EHR utilization survey* (George Hripcsak alert) — off-thread.
- *Causal Inference with Video Features as Treatments* (surfaced by
  `digests/2026-07-08.md`) — beautiful methods paper, but the
  application domain (video ads / Super Mario levels) is orthogonal.
  Retained as METHODS-WATCH per the INTERESTS.md rubric — the
  longitudinal-neural-network estimator under dynamic stochastic
  interventions is exactly the shape of estimator any EHR-video
  (echocardiogram, ophthalmology, endoscopy) causal-effect analysis
  will need.
- *NRF2 saturation-seq* (Jay Shendure alert), *Multiancestral dental
  malocclusion GWAS*, *brain-imaging × osteoporosis colocalization* —
  domain-specific GWAS, not on active disease threads.

---

## Suggested next steps

1. **Pull PDFs for #1, #3, #7** — those are the three that most directly
   feed the user's own writing pipeline (TWAS multi-ancestry, PRS-residual
   outliers for rare-variant discovery, and AoU HBOC penetrance / equity).
2. **Bench MIXPRS (#2) vs the current PRS-CSx pipeline** on any
   in-flight biobank scoring task.
3. **Add "PRS + rare variant integration" as a distinct sub-thread** in
   INTERESTS.md — three papers in one week (Baya, STELLAR, plus adjacent
   MIXPRS) suggests it deserves its own bucket rather than living under
   Genetic epidemiology as a one-liner.
