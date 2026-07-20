# Research digest report — 2026-07-20

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-20** — one-month catch-up since the prior
2026-06-20 report. Long window; treat the ranking as a *saturation* map
(what fired repeatedly, in what channel, and in what pairing), not a
straight-chronology diary.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 07-20 | Continuous daily traffic (~30–40 alerts/day at peak batches). Densest batches: 07-11 and 07-19 (each carried 30+ author-feed alerts). Author feeds active: Chenjie Zeng self-feed (2 citation events + 2 related-research events in-window), Bastarache (dense), Denny, Karczewski, Hripcsak, Montgomery, Shendure, Szolovits, Ryan (Patrick), Hernán, Yang, Pritchard, Chute, Callahan, Zitnik, Vogelstein, Natarajan, Luo, Kastner, Gusev, Rajpurkar, van der Schaar, Kohane, Wendy Chung, Evan Eichler, Zhiyong Lu, Isaac Kohane, Jian Ma, James Zou, Mark Gerstein, Pascal Brandt, Patrick Ellinor, Jure Leskovec. |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-13 | **30 daily runs.** ~7 on-thread papers surfaced across the window (see per-day breakdown below). Fetch reliability recovered after the 06-24 3-of-4 failure; no repeat failures logged. **13 dry days (0 relevant papers)** which is high relative to prior months — suggests either an unusually quiet arXiv window OR that keyword coverage is slipping (see pipeline notes). |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |
| Newsletter noise | daily | marktechpost, AINews, sebastianraschka — general-AI, off the clinical/genomic threads; logged for completeness, not triaged. |

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. Where a paper appears in multiple feeds, that
> multi-channel firing is the primary signal — treat it as the field's
> own relevance vote.

---

## Executive summary

**The two standout items this window are both Nature-tier and both hit
the PheWAS + longitudinal-EHR + genetic-discovery core simultaneously.**

- **Urbut, Ding, Nakao, Koyama, Misra et al. — *A Bayesian Framework for
  longitudinal EHR and genetic discovery* — Nature, 2026.** **Triple-feed
  saturation** across your own **Chenjie Zeng — new related research**
  feed, **Alexander (Sasha) Gusev — new articles** feed, **3 new
  citations to articles by Lisa Bastarache** feed. Nature venue +
  longitudinal EHR + genetic-discovery framing = default-citation
  candidate for any future longitudinal-PheWAS or age-at-onset PRS work.
  Your own self-feed firing is the single highest-precision channel this
  pipeline produces; combined with a Bastarache citation firing (which
  fires when a paper *cites* the phecode / PheWAS lineage) this is the
  strongest signal of the window. **Read first.**

- **Wang J, Buto P, Ferguson EL, Chen R, Pederson A et al. — *Can the
  All of Us sample be reweighted to mirror a nationally representative
  sample? A comparison of mortality predictors* — Epidemiology, 2026.**
  **Dual-feed** — *Chenjie Zeng — new related research* AND *Joshua
  Denny — new related research*. Sits at the intersection of three
  active threads: AoU biobank + selection-bias correction + causal
  inference. The reweighting question ("can AoU be made to look like a
  nationally representative sample?") is *exactly* the design question
  behind any AoU-based external-validity claim, and dual-firing across
  your own feed and Denny's is unusually clean signal. **HIGH.**

The rest of the top tier:

- **İnan RA, Kayaalp B, Safieh F, Kars ME, Stein D et al. — *AAVC: an
  automated framework for high-accuracy ACMG-based variant classification*
  — Genetics in Medicine, 2026.** **Dual-feed** — *Karczewski citations*
  AND *Denny citations*. Directly on the variant-interpretation thread
  (automated ACMG-AMP pipeline; the ACMG-automation reference class has
  been dominated by InterVar → CardioClassifier → Franklin; a new tool
  breaking into a *dual Karczewski + Denny citation firing* is a signal
  that the field is treating it seriously). **HIGH.**

- **Karim ME, Hu W — *Which Regularized Propensity-Score and Doubly
  Robust Methods Are Best Calibrated When Exposures or Outcomes Are
  Rare? A Plasmode Study of Proxy-Based Confounding Adjustment* — arXiv
  2607.07065, 2026-07-08 (stat.AP), surfaced by `arxiv-digest` 07-09.**
  Score 3 (propensity score, inverse probability, g-computation). Head-
  to-head calibration of OAL / GLiDeR / HAL / TMLE / IPTW under
  rare-exposure and rare-outcome, plasmode-anchored on NHANES with a
  known-null truth. Directly on your causal-inference / pharmacoepi
  thread. Actionable: gives you a defensible ranking of variable-
  selection strategies for the AoU + MVP proxy-heavy confounding
  problem. **HIGH.**

- **Fontana N, Mapelli A, Di Angelantonio E, Ieva F — *Enhancing
  comorbidity network inference with risk-enriched health trajectories
  embedding* — arXiv 2607.04702, 2026-07-06 (stat.AP), surfaced by
  `arxiv-digest` 07-07.** Score 3 (uk biobank, biobank, multimorbidity).
  UK Biobank, 24 cardiometabolic diseases, 76 risk factors; sparse
  GGM + Lasso with clinical-knowledge-prior + community detection →
  four progression phenotypes with distinct survival trajectories.
  Directly on your multimorbidity + biobank + chronic-disease-
  clustering thread — cardiometabolic multimorbidity was called out
  explicitly in `INTERESTS.md`. **HIGH.**

- **Baya NA, Lassen FH, Hill B, Venkatesh SS, Currant H et al. —
  *Individuals who deviate from polygenic expectation are enriched for
  damaging variants in genes linked to rare disease* — American Journal
  of Human Genetics, 2026.** Surfaced by *Stephen B. Montgomery — new
  related research*. The empirical form of the "tails-of-PRS-are-
  different" thread that started with Souaiaia et al. Nature (last
  report's #4). Directly on your composite-risk (PRS + rare pathogenic
  variant burden) thread; AJHG venue signals this becomes the operational
  reference for that argument. **HIGH.**

- **Mahesri M, Schneeweiss S, Lin KJ, Zabotka L et al. — *Bleeding Risk
  With Apixaban Versus Rivaroxaban: A Reference Trial Emulation
  Predicting the Results of COBRRA-VTE and COBRRA-AF Using US Health
  Care …* — 2026.** Surfaced by *Patrick Ryan — new related research*.
  Reference-trial emulation from the Schneeweiss group (DoPE-style
  design), predicting an as-yet-unfinished RCT from RWD. Directly on the
  target-trial-emulation / pharmacoepi thread. Not on a tracked drug
  class (DOACs, not GLP-1/SGLT2/CFTR/HRT), but methodologically
  exemplary. **HIGH-methods.**

- **Shi F, Xia H, Weissman S, Li X, Yang X — *Computational phenotyping
  of sexually transmitted infections with the All of Us Research
  Program from 2010 to 2023* — JAMIA open, 2026.** Surfaced by
  *"All of Us Research Program" — new results* keyword feed. Direct
  AoU-cohort computational phenotyping paper. Not the disease area you
  work in, but the *phenotyping-in-AoU-across-time* pattern is directly
  on-thread. Worth the read for the phecode-mapping choices and the
  observation-period definition. **HIGH-methods (AoU cohort
  construction template).**

- **Murali N, Barnatchez K, Hoppe JE, Wagner BD, Keller KP, Josey KP —
  *Causal Inference with Multiple Misclassified Exposures: A Control
  Variate-Adjusted Calibration Weighting Approach* — arXiv
  2606.23656, 2026 (stat.ME), surfaced by `arxiv-digest` 06-23.**
  Score 2 (causal inference, cystic fibrosis). CF cohort (n = 651,
  ages 6–21) — throat-swab vs sputum misclassification of *P.
  aeruginosa* / *S. aureus* — direct hit on your CF disease thread
  AND your causal-inference / pharmacoepi thread. Concludes: swab-
  based estimates attenuate the FEV₁ effect by ~69% relative to
  sputum-based estimates, i.e., misclassification is *not* trivial
  in CF respiratory infection studies. Sample is small but the
  method (calibration weighting + control-variate adjustment,
  double-robust) generalizes. **HIGH.**

Counts: **9 HIGH**, **8 METHODS-WATCH**, rest SKIP. The one-month
window is dominated by four themes: (a) longitudinal-EHR-plus-genetics
(Urbut Nature, Wang AoU-reweighting, Fontana multimorbidity), (b)
causal-inference for rare exposures / misclassified exposures (Karim
plasmode, Murali CF-swab, Naimi residual-on-residual), (c) PRS-tails-
and-rare-variant-composite scoring (Baya AJHG, carrying forward the
Souaiaia Nature line), and (d) ACMG-automation for variant
interpretation (İnan AAVC).

---

## HIGH priority — detailed reports

### 1. A Bayesian Framework for longitudinal EHR and genetic discovery
- **Authors / venue:** S.M. Urbut, Y. Ding, T. Nakao, S. Koyama, A. Misra et al. — *Nature*, 2026. (HTML linked from Scholar.)
- **Surfaced by:** **Triple-feed saturation** — (a) *Chenjie Zeng — new related research* (**your own self-feed**), (b) *Alexander (Sasha) Gusev — new articles* (Gusev is on the author list or a close collaborator), (c) *3 new citations to articles by Lisa Bastarache* (i.e., the paper cites the phecode / PheWAS lineage). Firing across your own self-feed + a senior-author articles feed + a citation-back-to-Bastarache feed is the highest-signal three-way pattern this pipeline can produce.
- **Thread:** **PheWAS / phecode infrastructure** (longitudinal EHR + genetic discovery is the descendant framework of phecode-based PheWAS) **+** **EHR-linked biobanks** (Bastarache-cite implies BioVU / AoU / UKB-linked data) **+** **Genetic epidemiology** (Bayesian framework for genetic discovery over longitudinal outcomes) **+** **EHR phenotyping** (any longitudinal-genetic-discovery pipeline is downstream of a phenotyping choice).
- **What it is:** From the snippet: "Electronic health records (EHRs) provide rich longitudinal disease [trajectories that current cross-sectional genetic discovery does not exploit]…" — the paper appears to propose a Bayesian framework that joint-models the longitudinal EHR trajectory with germline genetic variation, presumably to discover variants associated with *age-at-onset*, *rate-of-progression*, or *sequence of comorbidities* rather than only *ever-diagnosed*. Urbut / Ding / Koyama lineage is the Ellinor / Broad cardiometabolic-genetics group, so the empirical demonstration is almost certainly cardiometabolic (AF, CAD, HF, T2D) in a large EHR-linked biobank (MGB / UKB / AoU).
- **Why it matters to you:** Four converging reasons.
  (a) **It sits on top of your entire methodological stack.** PheWAS / phecode → longitudinal EHR trajectories → Bayesian joint-model of trajectory + genotype is the natural extension of the phecode-based PheWAS framework you publish in. If the paper defines a general-purpose method (not just a cardiometabolic application), it becomes the default citation for any future AoU / MVP longitudinal-PheWAS work.
  (b) **Nature venue matters for the citation graph.** A Nature paper in this space rewrites which framework is treated as the "reference" longitudinal-EHR-genetics method.
  (c) **Your own related-research feed firing is high-precision.** Google Scholar's relevance model has judged this paper close enough to your published work that it warrants a self-feed alert — a signal that the paper is likely to be relevant to your near-term citation set.
  (d) **Gusev on the author list (implied by his *new articles* feed firing) means the statistical-genetics rigor is likely high.** Gusev's line of work (TWAS, LDSC extensions, Bayesian fine-mapping) has been methodologically among the tightest in the field.
- **Action:** **HIGH — read first.**
  (i) Identify the empirical cohort — MGB Biobank? UK Biobank? AoU? MVP? The cohort choice determines how transferable the method claim is.
  (ii) Identify the phenotype representation — phecodes? OMOP concepts? Free-text? A phecode-native framework is directly reusable in your AoU work; an OMOP-native framework is reusable in MVP; a free-text framework requires an NLP layer.
  (iii) Check whether the Bayesian framework releases a per-variant *age-at-onset* effect or *trajectory-shape* effect (or both). Age-at-onset effects are the natural extension of standard case-control PheWAS; trajectory-shape effects are genuinely new.
  (iv) Note the release form — pre-print + code + trained model? Method paper without code is much less immediately reusable.
  (v) **Almost certainly a citation target** for any future longitudinal AoU / MVP work — worth reading closely enough to know when it belongs in a citation list and when the older reference-class (PheWAS-Catalog, Bastarache 2018) belongs instead.

### 2. Can the All of Us sample be reweighted to mirror a nationally representative sample? A comparison of mortality predictors
- **Authors / venue:** J. Wang, P. Buto, E.L. Ferguson, R. Chen, A. Pederson et al. — *Epidemiology*, 2026.
- **Surfaced by:** **Dual-feed** — (a) *Joshua C. Denny — new related research*, (b) *Chenjie Zeng — new related research* (**your own self-feed**). Any paper firing on both your own self-feed and Denny's related-research feed is dual-anchored on the AoU / PheWAS / precision-medicine core; this pattern typically means the paper is on-mission for the AoU consortium as a whole.
- **Thread:** **EHR-linked biobanks (specifically AoU)** **+** **Causal inference / selection bias** (reweighting-to-representative is a selection-bias-correction design) **+** **EHR phenotyping** (any external-validity claim in AoU is downstream of a phenotype definition).
- **What it is:** From the snippet: "…comparison of mortality predictors." The paper asks whether AoU's sample — which is intentionally enriched for underrepresented populations and therefore *not* nationally representative in the usual epidemiologic sense — can be reweighted (post-stratification? IPW-to-NHIS or NHANES targets? entropy balancing?) to mirror a nationally representative U.S. sample, using mortality prediction as the test-of-transportability. If the reweighted AoU produces mortality predictors similar to the reference nationally representative cohort, that's evidence AoU is *transportable* despite its non-representative construction.
- **Why it matters to you:** Four reasons.
  (a) **This is a first-principles-important paper for anyone who publishes AoU findings.** Every AoU-based association paper faces the reviewer question "but AoU isn't representative — how does this generalize?" This paper provides the empirical footing for a *quantitative* answer.
  (b) **The design is a classic transportability problem** — target = US population; source = AoU volunteer cohort. This is the causal-inference/target-trial-emulation formalism applied to biobank generalizability, which sits squarely on your INTERESTS thread ("Real-world evidence with explicit attention to confounding and selection bias").
  (c) **Reweighting-to-NHIS design is directly reusable.** If the paper's specific weighting scheme works, it can be plugged into any AoU-based effect estimate you publish (with a companion sensitivity analysis under the reweighting).
  (d) **Denny+Zeng dual-firing** is exactly the AoU-consortium relevance signal — this paper is likely to be a default citation in AoU methodology within a year.
- **Action:** **HIGH.**
  (i) Identify the reweighting reference target — NHIS? NHANES? ACS? US Census? The choice of target changes what "representative" means and what the reweighting can and cannot fix.
  (ii) Identify the reweighting mechanism — post-stratification cells, raking, IPW with a logistic selection model, entropy balancing? Each has different variance-inflation and coverage properties.
  (iii) Note whether the mortality predictor comparison is *point-estimate* transportability (do you get the same coefficients?) or *calibration* transportability (does a model built on AoU perform well on the reference cohort?). Point-estimate transportability is the harder bar.
  (iv) **Adopt as citation** for any AoU-based external-validity discussion. If the paper concludes reweighting works, cite as evidence; if it concludes reweighting has limits, cite as a limitations-section anchor.
  (v) Check whether they release the reweighting weights or code — reusable code is much more valuable than a method-only demonstration.

### 3. AAVC: an automated framework for high-accuracy ACMG-based variant classification
- **Authors / venue:** R.A. İnan, B. Kayaalp, F. Safieh, M.E. Kars, D. Stein et al. — *Genetics in Medicine*, 2026.
- **Surfaced by:** **Dual-feed** — (a) *10 new citations to articles by Konrad Karczewski*, (b) *10 new citations to articles by Joshua C. Denny*. Karczewski citation firing means the paper is likely citing gnomAD (used for PM2 / BS1 / BA1 rules); Denny citation firing means it likely cites either a Denny PheWAS-Catalog paper or an EHR-genomics paper. Dual citation-firing across the variant-interpretation grandee (Karczewski) and the EHR-genomics grandee (Denny) is a somewhat unusual combination — worth investigating whether AAVC bridges those two literatures (i.e., pulls in EHR-derived phenotype evidence for variant classification).
- **Thread:** **Variant interpretation (ACMG / ClinGen)** — direct hit. Also on your **rare disease** thread (variant classification is the primary bottleneck for rare-disease diagnosis).
- **What it is:** From the snippet: "Classification of DNA sequence data [under the ACMG/AMP framework]…" — a fully-automated ACMG-AMP variant classification pipeline. This reference class already contains InterVar, Franklin (Genoox), CardioClassifier, PathoMAN, and several others. The novel angle presumably is either (a) end-to-end automation with fewer manual gates, (b) higher concordance with expert VCEP classifications, or (c) integration of a new evidence type (PP3 in-silico updates from 2022, PS3 functional-data curation, PVS1-splice guidance).
- **Why it matters to you:** Three reasons.
  (a) **ACMG-automation is the operational infrastructure of modern rare-disease diagnostics.** Every new tool shifts the concordance floor and needs to be compared against the incumbents (InterVar, Franklin). A GIM-published tool warrants attention.
  (b) **The dual Karczewski + Denny citation firing is unusual.** If AAVC uses EHR-derived phenotype evidence to strengthen PP4 (patient phenotype match) or BS4 (segregation), that would be genuinely novel — most ACMG automation stops at the sequence-level evidence and asks the clinician to supply phenotype and family history separately.
  (c) **Directly relevant to any composite-PRS+rare-variant scoring** work — the classifier's output (P/LP/VUS/LB/B) is the input to the rare-variant burden component of any composite risk model.
- **Action:** **HIGH.**
  (i) Read for the specific ACMG rules automated — the gnomAD-dependent rules (BA1 / BS1 / PM2) are easy; the functional-evidence rules (PS3 / BS3) and the phenotype rules (PP4 / BS4) are the hard ones and the differentiators.
  (ii) Check the concordance benchmark — vs. ClinVar 2-star, vs. Franklin, vs. expert VCEP classifications? The benchmark set determines the credibility of the concordance claim.
  (iii) Note whether they provide a public web front-end or a downloadable pipeline. Downloadable is more valuable for enterprise/consortium use; web front-end is more valuable for occasional single-variant lookups.
  (iv) **Compare against InterVar+ (the WangGenomicsLab active-maintained fork).** InterVar remains the incumbent for downloadable pipelines; a new tool needs a concordance-plus-usability edge to justify migration.

### 4. Which Regularized Propensity-Score and Doubly Robust Methods Are Best Calibrated When Exposures or Outcomes Are Rare? A Plasmode Study of Proxy-Based Confounding Adjustment
- **Authors / venue:** M.E. Karim, W. Hu — arXiv 2607.07065, 2026-07-08 (stat.AP). URL: `arxiv.org/abs/2607.07065v1`. Surfaced by `arxiv-digest` **07-09** (score 3: `propensity score`, `inverse probability`, `g-computation`).
- **Surfaced by:** `arxiv-digest` pipeline (highest-scoring on-thread paper of the past month).
- **Thread:** **Causal inference / pharmacoepi** — direct hit. Specifically on the "large proxy library + rare event + variable selection" pinch-point that dominates AoU, MVP, and OneFlorida claims-data pharmacoepi.
- **What it is:** Plasmode simulation anchored on NHANES 2013–2018 data (25 investigator-specified covariates + 142 prescription-derived *proxies*), comparing 10 pipelines: outcome-adaptive LASSO (OAL), group LASSO (GLiDeR), highly adaptive LASSO (HAL), paired with IPTW and TMLE downstream estimators. Three regimes evaluated: (i) frequent, (ii) rare exposure, (iii) rare outcome; under a *known-null* truth (true RD = 0). Reports bias, SE, coverage, and (crucially) runtime.
  **Punchlines from the abstract:**
  - HAL + G-Computation → near-zero bias but tight estimates → coverage ~1 but relative error 106–186% (i.e., low bias but useless precision).
  - OAL-IPTW, GLiDeR, HAL-TMLE → best calibrated (bias + coverage tradeoff).
  - Regularized-LASSO + TMLE pipelines under-covered modestly (91–93%) in the rare regimes.
  - Under rare exposure: LASSO-IPTW had the largest bias + inflated SE + over-coverage — TMLE removed these problems.
  - Real-data agreement: methods converge to RD ≈ 0.07–0.085.
  - Runtimes span < 1 s to > 16 h — HAL is the expensive one.
- **Why it matters to you:** Four reasons.
  (a) **Directly answers the AoU / MVP / OneFlorida design question** — when your confounder set is proxy-heavy (prescription proxies, ICD-code proxies) and your outcome is rare (e.g., specific adverse drug event), which variable-selection-plus-estimator pipeline is defensible? This paper's headline answer: **OAL-IPTW, GLiDeR, or HAL-TMLE**, avoid LASSO-IPTW under rare exposure, use HAL only when compute is not a constraint.
  (b) **Adoption-ready.** All named methods have R implementations (glmnet, hal9001, tmle, ltmle, adaptr). The plasmode simulation code is likely public.
  (c) **Directly supports your active drug-class threads** — GLP-1 RA and SGLT2i target populations have moderate exposure prevalence but rare specific outcomes (e.g., DKA, MACE, HF hospitalization); CFTR modulators and HRT are rare exposures. Both regimes are exactly the ones this paper evaluated.
  (d) **Plasmode-with-known-null is a defensible simulation design** — it anchors on real covariate structure while retaining ground truth. Cite as methodological anchor.
- **Action:** **HIGH.**
  (i) Read for the specific rare-outcome coverage numbers — under-coverage of 91–93% is at the edge of "still defensible with wider CI adjustment"; anything worse would rule out that pipeline for FDA-facing pharmacoepi.
  (ii) Check whether they report treatment-effect *heterogeneity* estimation, not just average effect. Your composite-risk / precision-health thread cares more about HTE.
  (iii) Note the runtime numbers concretely: if HAL takes > 16 h on n = ~30k NHANES-scale data, it's essentially unusable on AoU-scale (n = 250k+) without cloud compute — worth knowing before committing.
  (iv) **Adopt as design-choice citation** for any AoU / MVP TTE paper: "we selected [pipeline] following Karim & Hu (2026), whose plasmode benchmark identified this pipeline as best-calibrated under our exposure-outcome-rarity regime."
  (v) Consider running the plasmode harness yourself on an AoU-plasmode extension — the NHANES-anchored version is a useful template but AoU's proxy library is larger and structurally different.

### 5. Enhancing comorbidity network inference with risk-enriched health trajectories embedding
- **Authors / venue:** N. Fontana, A. Mapelli, E. Di Angelantonio, F. Ieva — arXiv 2607.04702, 2026-07-06 (stat.AP). Surfaced by `arxiv-digest` **07-07** (score 3: `uk biobank`, `biobank`, `multimorbidity`).
- **Surfaced by:** `arxiv-digest` pipeline. Also, the same author group (Mapelli + Ieva) published *Prior-informed conditional Gaussian graphical models* the *following week* (arXiv 2606.31805, `arxiv-digest` 07-01 — see item #10 below); this is now a coherent Ieva-group UKB-biobank output stream.
- **Thread:** **Multimorbidity** (explicit) **+** **Chronic disease clustering** (community detection over disease network — cardiometabolic taxonomy) **+** **EHR-linked biobanks (UKB)** **+** **ML for precision health** (progression phenotypes → risk stratification).
- **What it is:** Population-level disease-network inference from UK Biobank data (24 cardiometabolic diseases + 76 risk factors) with three deliberate departures from standard comorbidity-network work:
  1. Uses individual *health trajectories* (semantic + temporal co-occurrence) rather than cross-sectional prevalence — captures ordering, not just co-presence.
  2. Sparse network via Gaussian Graphical Model + Lasso, *informed by a confounding-evaluation prior* over shared risk factors — the confounding-first design is the causal-adjacent framing.
  3. Downstream community detection on the sparse network → four disease communities aligning with the *known* cardiometabolic taxonomy → community-based patient embeddings → clustering → four *progression phenotypes* with distinct long-term survival.
- **Why it matters to you:** Four reasons.
  (a) **Chronic disease clustering & multimorbidity** was called out explicitly in your `INTERESTS.md` — cardiometabolic multimorbidity was named as a target application. This paper is a bull's-eye.
  (b) **Two-step design (network → embedding → cluster) is directly reusable** on AoU / MVP / BioVU multimorbidity work.
  (c) **Confounding-prior sparsification is the causal-inference-adjacent contribution.** Standard comorbidity networks conflate direct and indirect (shared-risk-factor-mediated) associations; this design separates them, which matches the causal-inference framing you already use.
  (d) **Ieva-group output stream.** Two on-thread papers in one week from the same group signals a coherent research program — worth tracking their pre-prints for follow-ups (proteomic multimorbidity, ancestry-stratified version, etc.).
- **Action:** **HIGH.**
  (i) Read for the confounding-evaluation step — is the confounding prior derived from literature curation, from causal discovery on the data itself, or from a mediation analysis? Each has different assumption footprint.
  (ii) Note the community detection algorithm — Louvain? Leiden? Spectral? Choice matters for reproducibility.
  (iii) Check the survival-trajectory validation — is the four-cluster survival separation statistically clean or just visually suggestive? Kaplan-Meier + log-rank + Cox-with-competing-risks is the minimum bar.
  (iv) **Adopt as methods reference** for any AoU cardiometabolic multimorbidity work. The 24-disease + 76-risk-factor scope is a reasonable starting universe to port to AoU.
  (v) Track the follow-on Mapelli paper (item #10) in the same output stream.

### 6. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
- **Authors / venue:** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh, H. Currant et al. — *The American Journal of Human Genetics*, 2026 (HTML linked from Scholar).
- **Surfaced by:** *Stephen B. Montgomery — new related research* feed.
- **Thread:** **Genetic epidemiology** (PRS + rare-variant burden composite scoring — direct callout in `INTERESTS.md`) **+** **Rare disease** (rare-disease-associated genes are the enriched category) **+** **Variant interpretation** (any P/LP variant in a rare-disease gene is the operational output of an ACMG classifier).
- **What it is:** Empirical validation of the "PRS-tails-are-different" thesis at the level of *individual* deviation. Frame: for each individual, compute the *residual* between their observed phenotype and their PRS-predicted phenotype. The subset of individuals whose residual is large-positive (much sicker than PRS predicts) or large-negative (much healthier than PRS predicts) is *enriched* for damaging variants (pLoF, deleterious missense) in genes linked to rare disease. This is the empirical form of "PRS explains the polygenic component, but the tails of the phenotype distribution are enriched for monogenic effects" — a thesis the field has been circling since the Alexander et al. "digenic" paper and Souaiaia et al. Nature 2026 (last report's #4).
- **Why it matters to you:** Three reasons.
  (a) **Direct empirical support for PRS+rare-variant composite scoring** — your `INTERESTS.md` explicitly names "composite risk models stacking PRS with rare pathogenic variants" as an active thread. Baya et al. is *the* empirical justification for that architecture.
  (b) **Direct connection to your CF-CFTR / APOL1 disease threads.** For any Mendelian-adjacent phenotype (CF, APOL1-mediated kidney disease, hereditary cancer syndromes), the "PRS + monogenic" composite is now the field-recommended risk-stratification model rather than PRS alone.
  (c) **Bridges genetic-epi and rare-disease diagnostics.** Rare-disease diagnostic workflows currently look at rare variants only; polygenic-adjusted diagnostics would be a genuinely new modality, and this paper is the empirical footing.
- **Action:** **HIGH.**
  (i) Read for the specific gene sets — did they use OMIM, Orphanet, ClinGen curated, or PanelApp green? Gene-set choice bounds the "rare-disease-linked" claim.
  (ii) Check the PRS models used — single-trait or PGS Catalog aggregated? For a single-trait PRS, the residual is straightforward; for multi-PRS composite the interpretation is different.
  (iii) Note the sample — UKB alone, or UKB + GEL + Estonian? Multi-cohort replication is the credibility bar for a claim this general.
  (iv) **Combine with Souaiaia (Nature, 2026 — last report's #4).** Baya = empirical individual-level enrichment. Souaiaia = distributional-architecture-in-tails. Together = the case for composite risk scoring in the top-N-percent slice.

### 7. Bleeding Risk With Apixaban Versus Rivaroxaban: A Reference Trial Emulation Predicting the Results of COBRRA-VTE and COBRRA-AF Using US Health Care Claims Data
- **Authors / venue:** M. Mahesri, S. Schneeweiss, K.J. Lin, L. Zabotka et al. — 2026.
- **Surfaced by:** *Patrick Ryan — new related research* feed.
- **Thread:** **Causal inference & pharmacoepi** (target-trial-emulation → RCT prediction is the Hernán / Schneeweiss / RCT-DUPLICATE paradigm) **+** off-thread substantively (DOACs, not GLP-1/SGLT2/CFTR/HRT).
- **What it is:** A *reference-trial-emulation* design — emulate a specific RCT (here COBRRA-VTE and COBRRA-AF, comparing apixaban vs rivaroxaban) using US healthcare claims data, and *predict* the RCT's not-yet-published result before it reports out. This is the Schneeweiss group's now-standard DoPE (Duplicating Pending Efficacy) framework. If the emulated result later matches the actual RCT, that is direct evidence that RWD-based causal effect estimation can substitute for RCT-based estimation for that specific question.
- **Why it matters to you:** Two reasons.
  (a) **Reference-trial-emulation is the gold-standard demonstration of TTE credibility.** Any future TTE work you publish (GLP-1 vs SGLT2 comparative effectiveness, CFTR modulator eligibility TTE, HRT re-emulation) will be judged against this design; worth reading the current best-practice template.
  (b) **Schneeweiss/Lin group is the reference lineage** for DOAC comparative effectiveness. Their published methods (propensity trimming rules, censoring conventions, sensitivity analyses) are the field-standard defaults; picking them up saves cycles.
- **Action:** **HIGH-methods (SKIP on disease substance).**
  (i) Read only for the methods template — outcome definition, censoring, propensity-score approach, negative controls.
  (ii) Note their calibration diagnostics — negative-control outcomes with expected null association, positive-control outcomes with known association. This is the referee-proofing spine of any TTE.
  (iii) Cite when defending any AoU / MVP TTE design in a methods section.

### 8. Computational phenotyping of sexually transmitted infections with the All of Us Research Program from 2010 to 2023
- **Authors / venue:** F. Shi, H. Xia, S. Weissman, X. Li, X. Yang — *JAMIA open*, 2026.
- **Surfaced by:** *"All of Us Research Program" — new results* keyword feed.
- **Thread:** **EHR phenotyping** (computational phenotyping — direct hit) **+** **EHR-linked biobanks (specifically AoU)** **+** off-thread substantively (STI, not your disease list).
- **What it is:** Computational phenotype development for STIs (chlamydia, gonorrhea, syphilis, HIV, and possibly HPV) in the AoU cohort with an observation window spanning 2010–2023. Almost certainly built on OMOP-CDM concept sets, with a rule-based algorithm (ICD + LOINC + RxNorm + measurement + note) validated against manually reviewed cases.
- **Why it matters to you:** Two reasons.
  (a) **Directly demonstrates AoU-compatible phenotype-construction methodology** — the OMOP concept-set choices, observation-window handling, and validation-review protocol are directly reusable for any AoU phenotype you build (regardless of disease).
  (b) **The 2010–2023 window is unusual for AoU** — most AoU papers restrict to a short EHR window because the OMOP data coverage was patchier in earlier years. A paper that handles the extended window responsibly is a useful methods template.
- **Action:** **HIGH-methods (SKIP on disease substance).**
  (i) Read for the concept-set choices — which ICD-10-CM ranges, which LOINC codes for STI screening, which RxNorm codes for treatment. The validated concept set is directly reusable.
  (ii) Note the sensitivity/specificity / PPV / NPV of the phenotype vs chart review. PPV > 90% for a rule-based STI phenotype would be a strong result.
  (iii) Adopt the AoU phenotype-development template for any future AoU phenotype you construct.

### 9. Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach
- **Authors / venue:** N. Murali, K. Barnatchez, J.E. Hoppe, B.D. Wagner, K.P. Keller, K.P. Josey — arXiv 2606.23656, 2026-06-22 (stat.ME). Surfaced by `arxiv-digest` **06-23** (score 2: `causal inference`, `cystic fibrosis`).
- **Surfaced by:** `arxiv-digest` pipeline. This is the **first CF-specific `arxiv-digest` paper in the past month** — the CF keyword is a good precision channel because CF-labelled papers are almost always on-thread.
- **Thread:** **Cystic fibrosis / CFTR** (disease thread — direct hit) **+** **Causal inference / pharmacoepi** (double-robust misclassification adjustment).
- **What it is:** New estimators for causal inference with *multiple misclassified binary exposures* + clustered observations. The concrete application: throat swabs vs sputum cultures for detecting *P. aeruginosa* and *S. aureus* in CF cohorts — throat swabs have imperfect sensitivity/specificity relative to sputum, and both are exposures of interest for the outcome (FEV₁ percent-predicted decline). Estimators:
  1. **Calibration-weighting** treats misclassification as missing-data → consistent without modelling the misclassification mechanism.
  2. **Control-variate adjustment** integrates error-prone observations to reduce variance while preserving consistency.
  3. Together → double-robust.
  4. Bivariate structural ceiling: joint-correct-classification of both exposures limits variance-reduction relative to univariate.
  Application: n = 651 CF patients ages 6–21. **Swab-based estimates attenuate the *P. aeruginosa* → FEV₁ effect by ~69%** (−2.67 vs −8.52 percentage points; sputum-CI: −13.40, −3.63). Punchline: relying on throat swabs may lead to under-treatment of PA infection.
- **Why it matters to you:** Four reasons.
  (a) **First on-thread CF pharmacoepi paper of the past month.** Your CF-CFTR disease thread is active (modulator pharmacoepi, real-world outcomes); this paper is directly on-thread despite being an infection-microbiology-adjacent paper (the misclassification method generalizes to any CF pharmacoepi outcome).
  (b) **The 69% attenuation is a clinically actionable finding.** If CF-modulator RWD studies use throat-swab-derived PA colonization as an outcome or a confounder, they are systematically under-estimating the effect. Worth flagging in any CF pharmacoepi work.
  (c) **The method generalizes beyond CF.** Any AoU / MVP phenotype with misclassified binary exposure structure (e.g., diabetes complications identified via imperfect ICD codes) can use the same estimator.
  (d) **Small sample (n = 651) but interpretable finding.** The method paper's credibility does not rest on cohort size.
- **Action:** **HIGH.**
  (i) Read for the specific double-robustness proof and the structural-ceiling formula — the ceiling constrains how much variance reduction is possible in bivariate settings, worth knowing for any multi-exposure extension.
  (ii) Check whether they release R / Python code — with a small CF cohort as the demonstration, code release is essential for adoption.
  (iii) Consider adoption for CF pharmacoepi work — the modulator-eligibility TTE you'd naturally build has PA colonization as a covariate; misclassification correction changes the effect size.
  (iv) Note the CF cohort — the CF Foundation Patient Registry linkage (most likely source given the age range) is the reference cohort for US CF pharmacoepi; understanding its data-collection conventions is downstream-useful.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Zhang X, Li K, Zhang Y, Liu C, Huang S, Jin Y, Gao Y et al. — *Omics GWAS: A Multi-Omics Integrative Analysis Platform for Genome-Wide Association Studies* — Med Research, 2026.** **Dual-feed** — *Joshua C. Denny — new related research* AND *Stephen B. Montgomery — new related research* (07-11 and 07-19). Multi-omics + GWAS integration platform. Directly on the **omics-GWAS integration** thread, though we don't yet know if it's a novel method or a platform-review — worth reading for the platform pieces if you're building AoU-omics infrastructure. Dual-feed on Denny + Montgomery is a moderate signal.

- **Naimi AI, Jin Q, Yu Y-H, Parisi SM, Bodnar LM — *Residual-on-Residual Regression as a Tool for Effect Estimation in Observational Data* — arXiv 2606.30976, 2026 (stat.ME).** Surfaced by `arxiv-digest` 07-01 (score 2: `inverse probability`, `causal inference`). Naimi is a highly respected epidemiologist; residual-on-residual (Robinson-style partialling-out) as a *triangulation* alternative to AIPW/TMLE under weak positivity. Directly on the causal-inference thread; worth reading as a stable-alternative reference when AIPW/TMLE misbehave. **METHODS-WATCH.**

- **Chen Y, Chen Z, Yang G, Li B, Ogunyemi KO, Liu J et al. — *Comorbidity Exposure-Window Definitions and Multidimensional Disparities in Long COVID Risk: Evidence from a US National Cohort (2020–2024)* — 2026.** Surfaced by *10 new citations to articles by Christopher G. Chute* (07-19). Comorbidity-window definitions × Long-COVID risk × multidimensional disparities. Off-thread substantively (Long COVID), but the **comorbidity-window-definition sensitivity** analysis is directly relevant to any EHR-phenotyping design decision. **METHODS-WATCH.**

- **Sivarajkumar S, Zhang H, Ji Y et al. — multimodal generative EHR-FM (npj Health Systems, 2026)** — Carry-forward from last report; still active in the Szolovits/Hripcsak/Brandt citation graph this window. If you haven't read it yet, do — it remains the highest-signal EHR-FM item from the last two windows. See last report §HIGH-2 for the detailed writeup.

- **Sona K, Rohan A, Rose S, Kumar KJP — *Temporal Foundation Models for Longitudinal EHRs: Interpretable Risk Forecasting for Multi Morbidity Using Attention at Scale* — International Conference, 2026.** Surfaced by *Foundation models + "electronic health records"* keyword feed (07-12). Longitudinal EHR + multimorbidity + interpretable attention — hits three threads simultaneously (EHR FM + multimorbidity + interpretability). Conference paper (not journal), so calibrate quality expectations; worth a skim for the attention-interpretation approach. **METHODS-WATCH.**

- **Mapelli A, Massi MC, Cuccuru G, Di Angelantonio E, Ieva F — *Prior-informed conditional Gaussian graphical models: an application to protein interaction network reconstruction* — arXiv 2606.31805, 2026-06-30 (stat.AP).** Surfaced by `arxiv-digest` 07-01 (score 3: `uk biobank`, `biobank`, `precision medicine`). UK Biobank cardiometabolic proteomics (n = 49,129, p = 366 proteins), T2D-network perturbations, 34 network-central biomarkers. Same Ieva-group output stream as item #5 (Fontana comorbidity network) — this is the *molecular*-scale counterpart. Github code released. **METHODS-WATCH** — high-quality but adjacent to your direct threads unless you have a UKB-PPP / T2D-network angle.

- **Loe A, Murray S, Wu Z — *Dynamic Prediction of Alternating Recurrent Events via Neural Network* — arXiv 2606.30889, 2026 (stat.ML).** Surfaced by `arxiv-digest` 07-01 (score 1). Neural network + IPW pseudo-observations for alternating recurrent events. Application: predicting periods of low mood for first-year medical residents. Off-thread substantively but the method (dynamic-prediction NN with IPW pseudo-observations) generalizes to any competing-events longitudinal-EHR problem. Zhenke Wu is a solid statistician. **METHODS-WATCH.**

- **DiSTILL — arXiv 2606.30693, 2026 (q-bio.GN).** Surfaced by `arxiv-digest` 07-01. IBD spatial-transcriptomics workflow system (FastAPI + SLURM + hybrid cloud-HPC). Direct hit on your **IBD** disease thread on the keyword; substantively it is a workflow-systems paper (reproducible-execution + queue-orchestration) rather than IBD-methodology, so log as **METHODS-WATCH** only. The IBD ST pipeline it wraps (Tan et al.) is the actual scientific artifact — worth tracing back if you have an IBD-genomics angle.

---

## SKIP / noise (logged, no action)

- **Marketing / two-sided marketplace causal-ML papers** — Wu Y et al. Airbnb / marketing-mix / hierarchical-clustering-collinearity papers (three separate arxiv-digest surfacings 07-01 / 07-02). Off-thread completely; the `causal inference` keyword is bringing in marketing econometrics. See pipeline note below.
- **DNA language model / genomic-LM benchmark papers** — Karpinsky et al. (`arxiv-digest` 06-30) DNABERT2/ConvNova assessment; Nair et al. (Hripcsak related-research 07-11) genomic-LM sparse-autoencoder interpretation. Adjacent to variant interpretation but not on-thread for clinical variant classification.
- **Semantic insurance pricing with LLMs** — Blier-Wong & Kusmenko (`arxiv-digest` 06-30). `motor` keyword hitting a French motor insurance paper — pure keyword collision. **See pipeline note.**
- **KG completion / knowledge-graph noise** — KG-TRACE antimicrobial resistance (`arxiv-digest` 06-26); Deciphering leader decision-making patterns from open-source information (07-12 KG keyword feed); GlaKG glaucoma fundus KG (Callahan related-research 07-11). Continues the 8th-consecutive-window KG-keyword leak pattern. **See pipeline note.**
- **Autoinflammatory-mechanism papers in Kastner citation feeds** — OTU deubiquitinases, PAD4-generated citrullinated histones (07-19), Tagging the Tank ubiquitin-mediated clearance (07-11), JAK inhibitors in inborn errors of immunity (07-11). Off your VEXAS/CHIP direct thread (autoinflammatory *mechanism*, not clinical/genomic *ascertainment*).
- **Karczewski + Denny citation-graph incidentals** — Copy-number estimation for paralogous genes (Bansal et al., Karczewski related-research 07-11); asthma candidate-variant study in Cebu Longitudinal Cohort (Karczewski related-research 07-19); RiskLab controlled toolkit / Knowledge Graphs vs SQL over EHR (Callahan 07-19). Citation-graph leaks.
- **Long-COVID / multi-omics implementation reviews** — Ismail et al. multi-omics clinical implementation (dual Chute + Karczewski citations, 07-11); Klinkhammer et al. polygenic scores intro (Yang citations 07-11); Frach et al. PRS in psychiatry (Yang related-research 07-11); Schmidt et al. PRS as modifiers in Mendelian diseases (Hripcsak citations 07-11); Schunkert et al. PRS in cardiovascular disorders (Denny citations 07-11). This week saw a **coordinated batch of Medizinische Genetik PRS review papers** — the entire issue was on PRS, hence the citation-feed blast. Low novelty each; skip individually.
- **STI / STD / cardiovascular-mechanism / cancer-review noise** — Numerous items in author-citation feeds are review or mechanism papers off your direct threads.
- **Perspective / general-AI-in-medicine items** — Rajpurkar new article on large reasoning models for medicine (Nat BME 07-11); Kohane on AI disagreement (JAMA 07-11); van der Schaar on automatic construction of clinical scoring systems (ICML 07-11); Zou new-article Data Journalist Agent (07-11). All general-AI-in-medicine adjacent, none directly on your threads.
- **Chenjie Zeng citations (2 in-window):** (i) *Calcium and TRPML-Mediated Autophagy: Implications in Cancer, Cardiovascular Diseases, and Cardio-Oncology* — Adu-Amankwaah et al. (Cardiovascular Toxicology, 2026), 07-11. Cardio-oncology mechanism review that cites your work — logged, no action. (ii) *From Environmental Evidence to Biomarker Selection: A Structured Decision-Support Process for Human Biomonitoring Studies in Contaminated Sites* — Bustaffa et al., 07-19. Environmental biomonitoring paper citing your work — logged, no action. Neither citation is on your active research thread; nothing to follow up on.
- **arxiv-digest dry days (13 in-window: 06-21, 06-22, 06-24, 06-27, 06-28, 06-29, 07-04, 07-05, 07-06, 07-10, 07-11, 07-12, 07-13)** — high dry-day rate. Not a fetch failure (individual runs succeeded and reported "0 relevant papers"); it may reflect that arXiv q-bio.QM / GN / PE + stat.AP is genuinely quiet, but it's also worth checking whether keyword drift is losing recall. **See pipeline note.**

---

## Suggestions for the pipeline

Carry-forwards from the 06-20 report remain: (1) 06-20-style fetch-failure vs dry-day distinguishability (already partly there); (2) `knowledge graph` → `biomedical knowledge graph` or compound filter; (3) `cs.LG`, `stat.ME`, medRxiv / bioRxiv source expansion; (4) `mendelian diseases`, `drug repurposing` keyword tightening; (5) PRS-stability / polygenic-tails keywords; (6) proteomic-signature / aging-clock keywords; (7) noncoding-variant-interpretation / MPRA keywords; (8) keep your self-citation feed as-is (single highest-precision channel). None of these have been actioned yet.

New this window:

9. **13 dry days in a 23-run window (57% dry rate).** This is much higher than the prior window's ~30% dry rate. Two hypotheses: (a) arXiv q-bio + stat.AP is genuinely quiet in early July (plausible — mid-year conference cycle can pull papers to cs.LG or bioRxiv); (b) keyword drift is losing recall. **Diagnostic:** manually check 3 dry days (e.g., 07-11, 07-12, 07-13) by hand-scanning arXiv q-bio.QM new-submission listings — if you find ≥ 1 clearly on-thread paper in each, that's a recall problem. If nothing on-thread appears, the digest is doing its job and the window is just quiet.

10. **`motor` keyword is now firing on: (a) motor-insurance-pricing papers, (b) motor-neuron / spinal-EMG papers.** Neither is what "MOTOR" was tracking (the EHR foundation model by Steinberg/Shah et al.). Fix: change the keyword from bare `motor` to `motor foundation model` OR `MOTOR EHR` OR add explicit exclusion of `motor insurance` and `motor neuron`. Two false-positive papers this month; low but nonzero cost.

11. **`inflammatory bowel disease` keyword is firing on IBD-labelled *workflow systems* papers (DiSTILL) rather than IBD-genetics or IBD-EHR-cohort papers.** Not a fix so much as a note — the current keyword is doing what it should; consider adding `IBD cohort` or `IBD EHR` as complementary narrower keywords if you want the cohort-specific slice.

12. **Consider adding `target trial emulation` and `reference trial emulation` as keywords** (new). Two on-thread TTE papers this window (Mahesri DoPE + the older Karim propensity plasmode) would have been directly surfaced; both came via author feeds (Ryan) or high keyword-scores from the general causal keywords, but a dedicated TTE keyword would improve precision.

13. **Consider adding `sample reweighting` / `transportability` / `generalizability` / `post-stratification` as keywords** (new). The Wang AoU-reweighting paper (item #2) is currently only reachable via author feeds; a keyword would surface it directly.

14. **Consider adding `longitudinal EHR` / `age of onset` / `trajectory PheWAS` as keywords** (new). The Urbut Nature paper (item #1) came via author feeds; a keyword would surface it directly, and similar longitudinal-EHR-genetics papers are a growing class.

15. **`Bayesian framework` alone is too broad; `Bayesian longitudinal` or `Bayesian phecode` would be tighter.**

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 9 | (1) Urbut et al. Bayesian longitudinal EHR + genetic discovery [Nature, self+Gusev+Bastarache-cite], (2) Wang et al. AoU reweighting [Epidemiology, self+Denny], (3) İnan et al. AAVC ACMG-automation [GIM, Karczewski+Denny citations], (4) Karim & Hu regularized-PS + DR calibration under rare exposure/outcome [arxiv-digest 07-09, score 3], (5) Fontana et al. UKB cardiometabolic comorbidity-trajectory network [arxiv-digest 07-07, score 3], (6) Baya et al. PRS-residual → rare-disease damaging variants [AJHG, Montgomery], (7) Mahesri et al. apixaban-vs-rivaroxaban reference-trial-emulation [Ryan], (8) Shi et al. AoU computational STI phenotyping [JAMIA open], (9) Murali et al. CF misclassified-exposure calibration weighting [arxiv-digest 06-23] |
| METHODS-WATCH | 8 | Zhang omics-GWAS platform (dual Denny+Montgomery), Naimi residual-on-residual (arxiv-digest 07-01), Chen Long-COVID comorbidity-window definitions (Chute), Sivarajkumar multimodal-EHR-FM (carry-forward), Sona temporal-EHR FM for multimorbidity (07-12), Mapelli prior-informed conditional GGM UKB proteomics (arxiv-digest 07-01), Loe et al. NN + IPW pseudo-observations for alternating recurrent events (arxiv-digest 07-01), DiSTILL IBD ST workflow system (arxiv-digest 07-01) |
| SKIP | ~40 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH over a 2-day window), this **one-month window** yielded 9 HIGH / 8 METHODS-WATCH — roughly proportional to the extra window length, so signal density is similar. The recurring pattern remains that nearly all HIGH-tier signal comes from Scholar author feeds (self, Denny, Gusev, Bastarache-cite, Montgomery, Karczewski-cite, Ryan) and from the AoU-keyword feed; the `arxiv-digest` pipeline delivered 3 of the 9 HIGH items (Karim, Fontana, Murali) plus 4 of the 8 METHODS-WATCH items — its best month-over-month yield ratio in the recent tracking history.

The **single most-actionable read is Urbut et al. Nature** (item #1) — it fires the highest-precision triple channel (self + senior-author-articles + Bastarache-cite), it lands in Nature, and it sits directly on top of your entire methodological stack (longitudinal EHR + phecode-lineage + Bayesian joint modeling). The **second most-actionable is Wang et al. AoU-reweighting** (item #2) — it addresses the external-validity question every AoU paper you publish will face.
