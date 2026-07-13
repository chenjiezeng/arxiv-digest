# Research digest report — 2026-07-13

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-28 → 2026-07-12** (rolling two-week catch-up covering
15 daily arxiv-digest runs and the current backlog of Google Scholar /
NCBI PubMed alerts). This is the first synthesis report since the
2026-06-20 report — the intervening ~3-week gap is closed here.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/`) | 2026-06-28 → 07-12 | 15 daily runs. **Signal-bearing days: 07-01 (7 papers), 07-07 (3), 07-09 (1 on-thread), 07-02 / 07-03 / 07-08 (1 each, methods-watch).** Nine "0-relevant" days (06-28, 06-29, 06-30, 07-04, 07-05, 07-06, 07-10, 07-11, 07-12) — these look like true dry days rather than fetch failures (categories present in header, not "3 of 4 failed"). |
| Google Scholar alerts (author + keyword) | 2026-06-28 → 07-12 | ~200+ threads; author feeds fire on Saturday overnight in a single burst (last big drop 2026-07-11 18:31Z). Followed feeds surveyed: Denny, Hripcsak, Bastarache, Karczewski, Karczewski citations, Yang, Yang citations, Pritchard, Montgomery, Kastner, Shendure, Chute, Chute citations, Hernán, van der Schaar, Ryan, Brandt, Rajpurkar, Wendy Chung, Eichler, James Zou, Zhiyong Lu, Gerstein, Bastarache citations, Denny citations, Vogelstein, Ma, Bastarache citations, Alexander Gusev, Gusev citations, Chenjie Zeng self-feed, plus keyword feeds: `All of Us research program`, `UK Biobank`, `electronic health records`, `Foundation models + EHR`, `intitle:"clonal hematopoiesis"`, `rare diseases`, `drug repurposing`, `knowledge graph`, `variant interpretation`, `mendelian diseases`, `autoimmune diseases`. |
| NCBI "My NCBI What's New" | daily, 06-28 → 07-12 | Daily `UK Biobank`, `All of Us`, `drug repurposing` digests — used as coverage backstop; not individually re-triaged where an item already appeared in a Scholar feed. |

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. The arxiv-digest items include full abstracts (all
> keyword-scored papers this window scored 1-3, so none crossed the
> deep-summary threshold of 4).

---

## Executive summary

- **The single highest-signal item this window is a pharmacoepi target-
  trial-emulation paper from the Schneeweiss / Kim Lin / OHDSI-adjacent
  group.** Mahesri, Schneeweiss, Kim Lin, Zabotka et al. — *Bleeding Risk
  With Apixaban Versus Rivaroxaban: A Reference Trial Emulation
  Predicting the Results of COBRRA-VTE and COBRRA-AF Using US Health Care
  Claims* — appears in the **Patrick Ryan related-research** feed. Two
  things make it stand out: (a) it's an *a priori* reference-trial
  emulation — the TTE is timed and published *before* the RCT reads out
  (predicting COBRRA-VTE and COBRRA-AF), which is the design pattern that
  makes RWE credible enough to be actionable, and (b) it comes from the
  Brigham/DEcIDE stable, where the group has been building the reference-
  trial-emulation methodology across the anticoagulant class for years.
  Directly on your causal-inference + pharmacoepi thread. **HIGH — read
  first.** See #1 below.
- **A second causal-inference / TTE paper in the same feed elevates
  exposure-definition sensitivity as a diagnostic.** Dai, Hao, Shen, Ren,
  Jin — *Exposure definition sensitivity unmasks hidden confounding in
  crystalloid target trial emulation* (iScience, 2026, *Patrick Ryan*
  feed). The take: emulating a balanced-crystalloid-vs-saline trial in
  MIMIC and finding that passing standard TTE diagnostics is *insufficient*
  — a targeted exposure-definition sensitivity analysis exposes residual
  confounding that the standard love-plot / SMD / positivity checks
  miss. This is exactly the kind of "your TTE is not as credible as your
  Table 1 says" methods paper worth citing when reviewers demand more
  than SMD balance. **HIGH.** See #2.
- **Regularized PS + doubly-robust methods calibration under
  rare-exposure/rare-outcome regimes — a plasmode benchmark that could
  become a reference-class figure for real-world-data pipelines.** Karim
  & Hu — *Which Regularized Propensity-Score and Doubly Robust Methods
  Are Best Calibrated When Exposures or Outcomes Are Rare? A Plasmode
  Study of Proxy-Based Confounding Adjustment* (arXiv 2607.07065,
  2026-07-08 arxiv-digest, score 3). Systematic head-to-head of ten
  pipelines (OAL, GLiDeR, HAL × IPTW/TMLE/G-computation) on NHANES-anchored
  plasmode simulations with 25 investigator-specified covariates + 142
  prescription-derived proxies, evaluating bias / SE / 95% coverage /
  runtime under a known null risk difference across three prevalence
  regimes (frequent, rare-exposure, rare-outcome). The methods panel is
  the same one your MVP / AoU pharmacoepi work is choosing from; the
  benchmark methodology (three-scenario × two-estimator × five-selector
  factorial with a null-RD ground truth) is directly cribbable for
  drug-class TTE work. **HIGH.** See #3.
- **UK Biobank multimorbidity comorbidity-network paper deploys the
  design pattern you've been tracking.** Fontana, Mapelli, Di
  Angelantonio, Ieva — *Enhancing comorbidity network inference with
  risk-enriched health trajectories embedding* (arXiv 2607.04702,
  2026-07-07 arxiv-digest, score 3). Sparse GGM + Lasso with prior
  clinical knowledge on shared risk factors, applied to UK Biobank
  cardiometabolic multimorbidity (24 diseases, 76 risk factors). Yields
  four cardiometabolic communities and derives community-based patient
  representations that cluster into progression phenotypes with distinct
  survival — exactly the trajectory-clustering + subtype-discovery
  framing on your multimorbidity thread. **HIGH.** See #4.
- **Same group, one week earlier: a UK Biobank cardiometabolic-proteomics
  GGM paper — worth pairing with #4 as the same methodological family
  applied one layer up (proteomics rather than diagnoses).** Mapelli,
  Massi, Cuccuru, Di Angelantonio, Ieva — *Prior-informed conditional
  Gaussian graphical models: an application to protein interaction
  network reconstruction* (arXiv 2606.31805, 2026-07-01 arxiv-digest,
  score 3). n=49,129, 366 UKB proteins; recovers 34 network-central T2D-
  associated candidate biomarkers, some visible only through connectivity
  (not differential expression). Both papers together define the
  "prior-informed GGM on UKB" template — worth reading as a pair.
  **HIGH.** See #5.
- **Computational phenotyping of STIs in All of Us — an AoU-native
  phenotype-development paper for a category your existing computable-
  phenotype work touches only tangentially.** Shi, Xia, Weissman, Li,
  Yang — *Computational phenotyping of sexually transmitted infections
  with the All of Us Research Program from 2010 to 2023* (JAMIA open,
  2026, *"All of Us research program"* keyword feed). Directly on the
  AoU + EHR-phenotyping thread. **HIGH.** See #6.
- **CHIP + genetic susceptibility × age-related macular degeneration —
  a novel disease outcome for the CHIP thread.** Li, Peng, Lin, Zhou,
  Yuan, Jin et al. — *Clonal Hematopoiesis of Indeterminate Potential
  and Genetic Susceptibility in Incident Age-Related Macular Degeneration:
  A Cohort Study* (American Journal of Ophthalmology, 2026,
  *intitle:"clonal hematopoiesis"* feed). Prospective incident-AMD cohort
  with CHIP as an inflammation-mediated somatic-mutation exposure and PGS
  as the germline anchor. Extends the CHIP-outcome catalogue beyond the
  cardiovascular / hematologic domain that dominates your current CHIP
  reading. **HIGH.** See #7.
- **Polygenic scores as modifiers in Mendelian diseases — review that
  frames the PRS × monogenic penetrance-modifier question for your
  penetrance-estimation thread.** Schmidt, Ludwig, Heyne — *Polygenic
  scores as modifiers in Mendelian diseases* (Medizinische Genetik,
  2026, *Hripcsak citations* feed; cites "Polygenic risk alters the
  penetrance of monogenic kidney disease"). This is the direct
  descriptive frame for your composite risk-model thread (PRS × rare
  pathogenic variant stacking, penetrance under population-screening
  conditions). **HIGH.** See #8.
- **Explainable KG + gene-perturbation model for drug-response
  prediction — on the drug-repurposing / knowledge-graph thread.** Bang,
  An, Sung, Yun, S. Kim, S. Lee — *Predicting Therapeutic Outcome via
  Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation
  Representations* (arXiv 2607.04557, 2026-07-07 arxiv-digest, score 1
  but on-thread). Two-view CLIP-style alignment of an individualized
  gene-regulatory-network embedding (DysRegNet + DrugBank drug-target
  edges) with a frozen LINCS-L1000-pretrained gene-gene attention model,
  contrasted with drug-context hard negatives. TCGA multi-split evaluation
  + zero-shot transfer to I-SPY2 (+5.6% AUROC). The mechanism-grounded
  attribution — pathway attributions that recover known mechanisms — is
  exactly the *explainable* repurposing hypothesis output the interests
  file flags as high-priority. **HIGH.** See #9.
- **GLP medications and severe post-COVID-19 outcomes in T2D — a GLP-1
  RA effectiveness study on the drug-class thread.** Butzin-Dozier, Wang,
  Ji, M. Kumar, Anzalone et al. — *GLP Medications and Severe Post-COVID-19
  Outcomes Among Individuals with Type 2 Diabetes Mellitus* (medRxiv,
  2026, *Patrick Ryan* feed). Directly on the GLP-1 RA drug-class thread;
  target-trial-adjacent RWE. **HIGH-tier for that thread, with the
  standard "medRxiv preprint, hasn't peer-reviewed yet" caveat.**
- **Rare noteworthy self-citation blip.** *2 new citations to articles
  by Chenjie Zeng* fired 2026-07-11 — the flagged citing article is
  Adu-Amankwaah et al., *Calcium and TRPML-Mediated Autophagy: Implications
  in Cancer, Cardiovascular Diseases, and Cardio-Oncology* (Cardiovascular
  Toxicology, 2026). This is a mechanistic autophagy review that cites
  a Zeng paper; not on any active thread, but noted for completeness.

## Secondary items surfaced

Not written up in full, but flagged for the record:

- **Sun, Ding, Nie, Guo — *Sequential analysis for post-marketing drug
  safety surveillance using routinely collected electronic healthcare
  data: a scoping review*** (Therapeutic Advances in Drug Safety, 2026,
  *Hripcsak citations* feed). Scoping review of sequential-analysis
  designs for pharmacovigilance in EHR / claims — relevant background
  for pharmacoepi thread; scoping-review depth. **MEDIUM.**
- **Sona, Rohan, Rose, Kumar — *Temporal Foundation Models for
  Longitudinal EHRs: Interpretable Risk Forecasting for Multi-Morbidity
  Using Attention at Scale*** (2026 conference proceedings, *Foundation
  models + EHR* keyword feed). On-thread for EHR-FMs (CLMBR/MOTOR/EHRSHOT
  lineage). Attention-based multi-morbidity forecasting with an
  interpretability angle. **MEDIUM-HIGH** — one to read if the FM-fairness
  / calibration sub-thread is active.
- **Estévez, Chiu, van der Schaar — *Automatic Construction of Clinical
  Scoring Systems with LLM Agents*** (ICML 2026, *van der Schaar
  articles* feed). LLM-agent generation of clinical scoring systems from
  guideline text — relevant to the "ML tied to a clinical decision" bar in
  the ML-for-precision-health thread. **METHODS-WATCH.**
- **Zhou, Rodman, Liu, Rajpurkar, T.Y. Hu et al. — *Large reasoning models
  as thinking machines for medicine*** (Nature Biomedical Engineering,
  2026, *Rajpurkar articles* feed). Position/perspective on LRMs (o1-class)
  in medicine; useful framing paper but not a new empirical result.
  **METHODS-WATCH.**
- **Valle, Vo, Castillo, Kawano, Santacroce et al. — *Comparison of
  Rule‐Based Algorithms to Identify Patients With Idiopathic Inflammatory
  Myopathies in Electronic Health Records*** (ACR Open, 2026, *EHR* feed).
  Rule-based computable phenotype comparison — narrow disease scope
  (IIM) but exactly the phenotype-validation genre on the EHR-phenotyping
  thread. **MEDIUM.**
- **Loe, Murry, Wu — *Dynamic Prediction of Alternating Recurrent
  Events via Neural Network*** (arXiv 2606.30889, 2026-07-01 arxiv-digest,
  score 1; keyword: inverse probability). NN + IPW pseudo-observations
  for alternating-recurrent-event dynamic prediction; applied to periods
  of low mood in first-year medical residents. **METHODS-WATCH** —
  relevant if longitudinal alternating-recurrent-event structure comes up
  in EHR outcome modeling.
- **Asiedu & Watson — *Causal ASCEND: Scalable Two-tier Causal Discovery
  on High Dimensional Multi-omics Data*** (arXiv 2607.04527, 2026-07-07
  arxiv-digest, score 1; keyword: causal inference). Two-tier constraint-
  based causal discovery for the SNP/methylation → expression setting.
  Off the core threads, but adjacent to genetic-epi if TWAS-style
  directed-network questions come up. **METHODS-WATCH.**
- **Gálvez-Carvajal, Comino-Méndez, López-López et al. — *THE LANDSCAPE
  OF CLONAL HEMATOPOIESIS OF INDETERMINATE POTENTIAL IN LONG-TERM BREAST
  CANCER SURVIVORS*** (The Breast, 2026, *intitle:"clonal hematopoiesis"*
  feed). On-thread for CHIP × cancer-therapy fitness-landscape
  literature; therapy-related-CHIP is the highest-value subthread there.
  **MEDIUM.**
- **AoU-native dermatology papers — a cluster.** Craver, Leasure, Jones,
  Cohen (statin use in psoriasis, Archives of Dermatological Research);
  Chin, Bai, Patel, Khodadad, Sullivan, Paller (congenital ichthyosis
  metabolic/joint disease, JAAD 73774); G. Pathak, Syed, Tan, Murrell
  (malignancy risk in bullous pemphigoid, JAAD 75990); Herrera, Bordeaux
  (new-onset hair loss with semaglutide / tirzepatide, JAAD 75371). All
  are AoU case-control / cohort designs. Individually LOW-MEDIUM, but the
  cluster shows AoU is now the default dermatology-epi backend — worth
  a note if the AoU EHR-phenotyping design patterns for skin phecodes
  are being audited.
- **Naimi, Jin, Yu, Parisi, Bodnar — *Residual-on-Residual Regression as
  a Tool for Effect Estimation in Observational Data*** (arXiv 2606.30976,
  2026-07-01 arxiv-digest, score 2; keywords: inverse probability,
  causal inference). Head-to-head with AIPW and TMLE on nuMoM2b; a
  triangulation-strategy paper for partially linear causal models under
  positivity violations. **METHODS-WATCH.**

---

## Detailed reports

### 1. Mahesri, Schneeweiss, Kim Lin, Zabotka et al. — *Bleeding Risk With Apixaban Versus Rivaroxaban: A Reference Trial Emulation Predicting the Results of COBRRA-VTE and COBRRA-AF Using US Health Care Claims*

**Venue:** *… : Population Health and …* (Aetion / DEcIDE-adjacent series), 2026.
**Alert path:** *Patrick Ryan — new related research*, 2026-07-11.
**Thread anchors:** causal inference & pharmacoepi (target-trial
emulation, propensity-score methods, drug-class safety); real-world
evidence for regulatory / clinical use.

**Why it's the top item this window.** Two structural properties elevate
this above the pharmacoepi noise floor:

1. **Reference-trial emulation posture.** The paper *predicts* the
   results of two RCTs (COBRRA-VTE and COBRRA-AF) that have not yet read
   out, from US health-care claims. That's the strongest possible
   external-validity setup for RWE: it makes the emulation falsifiable
   before the fact, and it puts the group's methodology through the
   "will the RCT vindicate you" gauntlet. The RCT-DUPLICATE / RWE-2027
   playbook depends on this design pattern surviving.
2. **Author stack.** Schneeweiss + Kim Lin + the Aetion / DEcIDE lineage
   is where most of the current PS-methods pharmacoepi practice — long-
   term-safety comparisons across the DOAC class, in particular — has
   been forged. Reading the paper for its methods (cohort entry, exposure
   definition, active-comparator design, PS approach) has value beyond
   the specific outcome.

**Design read (from the alert / snippet).** Cohort study in US health-
care claims comparing apixaban vs. rivaroxaban with bleeding as the
primary safety endpoint, anchored to two upcoming RCTs (VTE and AF
indications). No abstract text available yet from the Scholar snippet —
full text at PMC13336243 needed to characterize the PS specification,
exposure definition, negative-control outcomes, and the pre-specified
sensitivity analyses.

**Cribbable / actionable.** For pharmacoepi TTE work you touch:
- The reference-trial-emulation *specification protocol* (pre-registered
  prediction of an ongoing RCT) is the design template to imitate for
  any DOAC / anticoagulant / GLP-1 / SGLT2i safety comparison.
- The negative-control-outcome + PS diagnostics stack is likely the
  Schneeweiss/Wang/Kim Lin house style; worth pulling the diagnostic
  suite as a checklist.

**Verdict.** **HIGH — read first.** Pair with #2 (Dai et al.) as a
credibility contrast: this paper builds a maximally credible TTE up
front; that paper shows a TTE that passes standard diagnostics can still
be wrong.

---

### 2. Dai, Hao, Shen, Ren, Jin — *Exposure definition sensitivity unmasks hidden confounding in crystalloid target trial emulation*

**Venue:** *iScience*, 2026.
**Alert path:** *Patrick Ryan — new related research*, 2026-07-11.
**Thread anchors:** causal inference & pharmacoepi (target-trial
emulation, diagnostics, sensitivity analysis).

**The claim, translated.** The authors emulate a balanced-crystalloid
vs. 0.9%-saline trial in MIMIC (ICU EHR), meeting standard TTE
diagnostics (balance, positivity, negative-control outcomes), and then
introduce a targeted exposure-definition sensitivity analysis that
exposes residual confounding standard diagnostics miss. The reframe:
"my SMDs are <0.1, my positivity looks fine" is insufficient reassurance
if you have not stress-tested the exposure definition itself.

**Why it matters for your work.** Every TTE you review (or write) has an
exposure-definition step whose sensitivity is under-audited. This paper
proposes a diagnostic that plugs into the sensitivity-analysis section
of the TTE playbook. Directly cribbable for AoU / MVP TTE
methodology.

**Read priority.** **HIGH.** Short (iScience), tractable, and pairs
naturally with the Mahesri reference-trial-emulation paper as the
"here's what your TTE diagnostics still miss" companion.

---

### 3. Karim & Hu — *Which Regularized Propensity-Score and Doubly Robust Methods Are Best Calibrated When Exposures or Outcomes Are Rare? A Plasmode Study of Proxy-Based Confounding Adjustment*

**Venue:** arXiv 2607.07065, 2026-07-08 (stat.AP). Surfaced 2026-07-09
arxiv-digest, score 3 (`propensity score`, `inverse probability`,
`g-computation`).
**Thread anchors:** causal inference & pharmacoepi (regularized PS,
doubly robust estimation, RWE calibration).

**Design.** Plasmode simulation anchored on NHANES 2013–2018 (25
investigator-specified covariates + 142 prescription-derived proxy
covariates), evaluating ten pipelines under a *known* null risk
difference across three prevalence scenarios: frequent, rare-exposure,
rare-outcome.

Pipelines:
- **Variable selection:** outcome-adaptive LASSO (OAL), group LASSO /
  GLiDeR, highly adaptive LASSO (HAL).
- **Estimation:** IPTW, TMLE, and (for HAL only) direct G-computation.

Metrics: bias, SE, relative error, 95% coverage, runtime.

**Headline results.**
- **HAL (G-Computation):** near-zero bias but very concentrated
  estimates → near-unity coverage and enormous relative error
  (106–186%). Statistically "correct on average" but practically
  degenerate.
- **OAL (IPTW), GLiDeR, HAL (TMLE):** best calibrated across scenarios.
- **Regularized-LASSO TMLE pipelines:** modest under-coverage (91–93%)
  in the rare scenarios — still workable but with a nominal-coverage tax.
- **Rare-exposure LASSO-IPTW:** the pathology — largest bias, inflated
  SE, over-covers conservatively. TMLE removes both.
- **On real data:** methods agree, RD ≈ 0.07–0.085.
- **Runtimes:** <1 s to >16 h — a real compute-vs-calibration tradeoff.

**Bottom line the paper draws.** Pair *outcome-aware selection* (OAL,
GLiDeR) or *doubly robust estimation* (TMLE) with regularized models to
balance bias, calibration, and robustness to rarity. Rare-exposure
regimes expose the largest method-choice gaps; method choice should
weigh the prioritized metric against compute cost.

**Why it's HIGH for your work.**
- The 10-pipeline factorial × 3-prevalence-regime × null-RD anchor is a
  reusable benchmarking harness — worth cribbing wholesale for any AoU
  / MVP methods paper that needs to justify a PS-adjustment choice.
- The "142 prescription-derived proxies" setup is the RWE-database
  regime you're operating in.
- The runtime accounting is unusual in this literature — many methods
  papers ignore compute — and it matters when the answer is "yes it's
  calibrated, but it takes 16 hours."

**Verdict.** **HIGH.** One of the best methods-transfer targets in the
window.

---

### 4. Fontana, Mapelli, Di Angelantonio, Ieva — *Enhancing comorbidity network inference with risk-enriched health trajectories embedding*

**Venue:** arXiv 2607.04702, 2026-07-06 (stat.AP). Surfaced 2026-07-07
arxiv-digest, score 3 (`uk biobank`, `biobank`, `multimorbidity`).
**Thread anchors:** chronic disease clustering & multimorbidity;
biobanks with EHR linkage (UK Biobank); ML for precision health.

**Design.** Population-level disease-network inference from individual
health trajectories, applied to UK Biobank (24 cardiometabolic diseases,
76 risk factors). Sparse network via Gaussian Graphical Models with
Lasso regularization, informed by prior clinical knowledge on shared
risk factors derived from a dedicated *confounding-evaluation step*.
Trajectory embeddings capture semantic similarity + temporal
co-occurrence.

**Findings.**
- Recovers clinically meaningful cardiometabolic patterns; topological
  analysis identifies pathological hubs and "potential actionable
  targets" for multimorbidity management.
- Four disease communities aligning with the established
  cardiometabolic taxonomy.
- Community-based patient representations → clustering yields four
  progression phenotypes with *significantly different long-term
  survival trajectories*.

**Why HIGH.**
- Directly on the multimorbidity + trajectory-clustering thread; UK
  Biobank as the substrate.
- The methodological chain — trajectory embedding → risk-factor-informed
  sparse GGM → community detection → community-embedded patient
  clustering → survival — is a full end-to-end template you can point
  to when someone asks "how do I go from EHR trajectories to
  clinically-actionable multimorbidity subtypes." No single step is
  novel, but the composition is coherent and (crucially) the survival
  differentiation across the four progression phenotypes is what makes
  the subtyping actionable rather than descriptive.
- Cardiometabolic focus overlaps with your active disease slice.

**Sibling paper.** Same lead-adjacent authors (Alessia Mapelli) — see
#5 below — apply the *same GGM machinery one layer up*, on UKB
cardiometabolic *proteomics*, one week earlier. Reading them together
gives you the "one method, two data modalities" template.

---

### 5. Mapelli, Massi, Cuccuru, Di Angelantonio, Ieva — *Prior-informed conditional Gaussian graphical models: an application to protein interaction network reconstruction*

**Venue:** arXiv 2606.31805, 2026-06-30 (stat.AP). Surfaced 2026-07-01
arxiv-digest, score 3 (`uk biobank`, `biobank`, `precision medicine`).
**Thread anchors:** UK Biobank; multi-omics; precision medicine; ML for
precision health (methods layer).

**Contribution.** Prior-informed *conditional* GGM that (a) integrates
database-derived interaction priors and (b) allows covariate-dependent
network structure — the two innovations existing GGM applications have
addressed separately, not together. The key methodological move is a
structured, weighted penalty that selectively incorporates curated-
database priors into population-level network estimation while leaving
context-specific perturbations entirely data-driven.

**Application.** UKB cardiometabolic proteomics, n = 49,129, p = 366
proteins. Recovers T2D-associated network perturbations, identifies 34
network-central candidate biomarkers — several detectable *only through
connectivity, not differential expression* — and reveals six biologically
coherent protein communities with metabolic / cardiovascular / cancer-
related pathway enrichments. Code: `AlessiaMapelli/Prior-informed-conditional-GGMs`.

**Why HIGH.**
- The "biomarker visible only through connectivity" finding is the class
  of result that GGM-on-proteomics buys over differential-expression
  analyses — worth reading for the concrete demonstration.
- Same methodological family as #4 (both use prior-informed GGMs on
  UKB), applied one omic layer above. If you're planning any GGM /
  network-inference work on UKB proteomics, PPP / Olink data, or MVP
  proteomics, this is the reference implementation.
- The UKB-cardiometabolic-proteomics-only substrate is a portable
  sub-cohort — n=49k is large enough that the network inference is
  meaningful rather than variance-limited.

---

### 6. Shi, Xia, Weissman, Li, Yang — *Computational phenotyping of sexually transmitted infections with the All of Us Research Program from 2010 to 2023*

**Venue:** JAMIA open, 2026.
**Alert path:** `"All of Us research program"` keyword feed, 2026-07-12.
**Thread anchors:** EHR phenotyping & OMOP; biobanks with EHR linkage
(AoU); computable phenotype development.

**Why HIGH.**
- **AoU-native phenotyping paper published in JAMIA-Open.** These are
  the design templates that other AoU-linked phenotype work then cites;
  worth reading for the code-set logic and validation approach.
- **STI phecodes are a category your existing phenotyping work touches
  only tangentially.** Adds a target-disease-agnostic reference for how
  the AoU controlled-tier code / lab / medication tables were combined
  for a category with substantial coding heterogeneity and stigma-linked
  underreporting.
- 2010→2023 window means the paper spans the OMOP-CDM v5.x era; the
  algorithm choices are portable.

**Read priority.** **HIGH** for the phenotyping thread, MEDIUM for
disease-specific interest.

---

### 7. Li, Peng, Lin, Zhou, Yuan, Jin et al. — *Clonal Hematopoiesis of Indeterminate Potential and Genetic Susceptibility in Incident Age-Related Macular Degeneration: A Cohort Study*

**Venue:** American Journal of Ophthalmology, 2026.
**Alert path:** `intitle:"clonal hematopoiesis"` keyword feed,
2026-07-12.
**Thread anchors:** CHIP disease thread; genetic epi (PRS as germline
anchor alongside a somatic-mutation exposure).

**Design read (from snippet).** Prospective incident-AMD cohort. CHIP
positioned as a novel biologically-plausible risk factor for AMD
alongside inherited (germline) susceptibility. Framing that inflammation
is the mediator matches the CHIP → cardiovascular literature template.

**Why HIGH for the CHIP thread.**
- Extends the CHIP-outcome catalog beyond CV / hematologic outcomes into
  ophthalmic aging outcomes — a novel disease category for the CHIP-
  outcomes literature.
- Uses the "germline PGS + CHIP-status" joint-exposure design, i.e., the
  composite germline-plus-somatic model you have on the radar. Worth
  reading for the interaction / mediation strategy and how the paper
  handles the "does PGS predict CHIP acquisition" collider problem.
- AMD is a large, well-phenotyped outcome in UKB / AoU — the design is
  portable to your cohorts.

**Verdict.** **HIGH.** New disease category on-thread with the composite-
risk-model methodology you care about.

---

### 8. Schmidt, Ludwig, Heyne — *Polygenic scores as modifiers in Mendelian diseases*

**Venue:** Medizinische Genetik, 2026.
**Alert path:** *10 new citations to articles by George Hripcsak*,
2026-07-11 (cites "Polygenic risk alters the penetrance of monogenic
kidney disease").
**Thread anchors:** Genetic epi (PRS × rare pathogenic variants;
penetrance under population-screening conditions); PheWAS / phecode
infrastructure (penetrance estimation for monogenic variants); variant
interpretation.

**Why HIGH.** This is the framing paper for the composite-risk / PRS-
as-penetrance-modifier line of work — exactly the sub-thread the
interests file calls out ("penetrance estimation for monogenic variants
under population-screening conditions vs. clinically ascertained
cohorts" and "composite risk models stacking PRS with rare pathogenic
variants"). The specific citation trail — this paper cites *Polygenic
risk alters the penetrance of monogenic kidney disease* — signals a
review that consolidates the case-studies (Mendelian disease × PRS
modifier) with the design-and-inference machinery for making the
modifier claim credible.

**Read priority.** **HIGH.** Review / perspective — read for the framing
and the case-study reference class, not for a new empirical result.

---

### 9. Bang, An, Sung, Yun, S. Kim, S. Lee — *Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations* (PREDIKTOR)

**Venue:** arXiv 2607.04557, 2026-07-06 (cs.LG). Surfaced 2026-07-07
arxiv-digest, score 1 (`knowledge graph`).
**Thread anchors:** Drug repurposing (explainable KG / GNN with
mechanistic rationale); knowledge graphs & ontologies; ML for precision
health.

**What it does.**
- Two-view framework:
  1. **Patient-specific KG view.** For each patient, construct an
     *individualized gene regulatory network* from tumor expression via
     DysRegNet, then augment with drug-target links from DrugBank. A
     graph neural encoder yields a drug-centric, mechanistically-
     grounded embedding.
  2. **Perturbation view.** A frozen condition-specific gene-gene
     attention model, pretrained on LINCS L1000, generates a *simulated
     post-perturbation transcriptomic profile* for the same patient-
     drug pair.
- Align the two views in a shared latent space via a **CLIP-style
  contrastive objective with drug-context hard negatives**.
- Concatenate for end-to-end drug-response classification.

**Results.**
- On TCGA: consistently outperforms SOTA baselines under **patient-,
  drug-, and tissue-split** evaluations — the split diversity is unusual
  and correct for a heterogeneous-treatment-effect setting.
- **Zero-shot transfer to the I-SPY2 trial: +5.6% AUROC** over
  competing methods. This is the external-validation signal that
  distinguishes it from KG-only or LINCS-only baselines.
- Aligned embeddings yield stable **gene and pathway attributions that
  recover known mechanisms** — the "explainable hypothesis output" the
  interests file flags as high-priority for repurposing work.

**Why HIGH.**
- The `INTERESTS.md` drug-repurposing section explicitly prioritizes KG /
  GNN approaches with **explainable hypothesis output (path or subgraph
  rationales rather than opaque link-prediction scores)**, and PREDIKTOR
  is the cleanest current-cycle instance. The pathway attributions
  recovering known mechanisms are exactly that explainability property.
- The DysRegNet patient-specific network + LINCS-L1000 perturbation
  view alignment is a portable design template — the two-view CLIP-
  style alignment is a design pattern to remember for any
  patient-specific-KG + perturbation-signature integration you might
  build.
- Zero-shot transfer to I-SPY2 (a real trial) is the credibility jump
  most repurposing papers duck by staying on TCGA.

**Verdict.** **HIGH for the drug-repurposing / KG thread.**

---

## Housekeeping notes

- **arxiv-digest empty-days audit.** Nine days this window produced 0
  keyword-scored papers: 06-28, 06-29, 06-30, 07-04, 07-05, 07-06,
  07-10, 07-11, 07-12. The digest headers on the empty days all show
  `Categories: q-bio.QM, q-bio.GN, q-bio.PE, stat.AP` and do **not**
  contain the "3 of 4 categories failed" pipeline-warning banner that
  the previous 2026-06-20 digest had. These look like *true dry days*
  driven by (a) weekends and (b) the beginning-of-July arXiv-submission
  slowdown, not fetch failures — but if the July 10/11/12 zero-day
  streak continues past 07-13 with q-bio.QM / q-bio.GN listings on
  arxiv.org showing non-zero submissions, a workflow-log check would be
  worth it.
- **Deep-summary threshold not exceeded.** No paper this window scored
  ≥4, so no auto-extracted section snippets appear in the digests —
  every paper listed above was triaged from abstract text only. If you
  want deep summaries to fire more often for the biobank-adjacent
  papers, either lower `--deep-score` to 3 (would have picked up
  Mapelli #5, Fontana #4, Karim #3, and any 3-keyword paper) or add
  higher-multiplicity phrases so scoring inflates more readily.
- **Self-citation flag.** The *2 new citations to articles by Chenjie
  Zeng* on 2026-07-11 is worth noting — one is a mechanistic autophagy
  review not on any research thread; the other flagged citation was not
  named in the snippet.

