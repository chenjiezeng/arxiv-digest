# Research digest report — 2026-07-14

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-14** (since the prior 2026-06-20 report;
this is a catch-up sweep covering ~3.5 weeks in one pass).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 07-14 | ~200 alert threads over the window across author feeds (Bastarache, Denny, Hripcsak, Szolovits, Zitnik, Callahan, Karczewski, Yang, Pritchard, Kastner, Natarajan, Luo, Hernán, Brandt, Ryan, Chenjie Zeng self-feed) and keyword feeds (UK Biobank, All of Us, electronic health records, foundation models + EHR, phenome-wide association, cystic fibrosis carriers, mendelian diseases, autoimmune, rare diseases, knowledge graph, drug repurposing, variant interpretation). |
| `arxiv-digest` repo (`digests/`) | 2026-06-25 → 07-14 | 20 days, of which 8 fired ≥1 paper. Fired days: **06-25** (2 papers, both foundation-model/methods), **06-26** (1 AMR KG paper), **06-30** (4 papers), **07-01** (7 papers — highest of the window), **07-02** (1 paper), **07-03** (1 paper), **07-07** (3 papers), **07-08** (1 paper), **07-09** (1 paper), **07-14** (1 paper). Dry days: 06-27 through 06-29, 07-04 through 07-06, 07-10 through 07-13 — several of these read as fetch failures (0.13 KB placeholder files, same pattern as 06-20). |

> ⚠️ **`arxiv-digest` fetch-failure pattern is now systematic.** Nine of
> the twenty days in the window produced a ~138-byte placeholder digest
> (0 papers, no error surfaced), matching the shape flagged in the 06-20
> report. The 07-04 → 07-06 and 07-10 → 07-13 clusters are the
> concerning ones — three or four consecutive placeholder days is
> extremely unlikely to be a genuine dry period across four q-bio
> subcategories. The workflow needs (a) a distinct placeholder-vs-real-
> 0-papers signal, and (b) either backoff+retry or category splitting.
> This is the third window in a row this has come up unaddressed.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a *double-feed* AoU computational-
  phenotyping paper on your own related-research feed.** Shi, Xia,
  Weissman, Li, Yang — *Computational phenotyping of sexually
  transmitted infections with the All of Us Research Program from 2010
  to 2023* (*JAMIA open*, 2026) — surfaces in (a) the *Joshua C. Denny —
  new related research* feed **and** (b) **your own Chenjie Zeng — new
  related research** feed. Explicit AoU-based EHR computational-
  phenotyping over 13 years of longitudinal follow-up is squarely on your
  EHR-phenotyping + AoU biobank thread; the fact that Google's relevance
  model surfaced it to your own author feed suggests it either cites your
  AoU phenotyping work or shares strong methodological overlap.
  **Read first.**
- **PRS-as-modifier-of-Mendelian-penetrance is now a distinct sub-
  literature.** Schmidt, Ludwig, Heyne — *Polygenic scores as modifiers
  in Mendelian diseases* (*Medizinische Genetik*, 2026, surfaced by the
  *George Hripcsak citations* feed, citing "Polygenic risk alters the
  penetrance of monogenic kidney disease"). This is exactly the
  "penetrance estimation for monogenic variants under population-
  screening conditions" bullet in your INTERESTS file, formalized as a
  review. **HIGH.**
- **Multimorbidity network + trajectory clustering on UK Biobank
  (arxiv-digest 07-07).** Fontana, Mapelli, Di Angelantonio, Ieva —
  *Enhancing comorbidity network inference with risk-enriched health
  trajectories embedding* (arXiv 2607.04702, stat.AP). UKB, 24
  cardiometabolic diseases + 76 risk factors, sparse GGM with Lasso and
  confounder-informed prior, four disease progression phenotypes with
  significantly different long-term survival. Squarely on the chronic-
  disease clustering + multimorbidity thread; the risk-factor-aware
  Lasso is a cleaner design than most comorbidity-network work.
  **HIGH.**
- **Rare-outcome / rare-exposure calibration study for regularized PS
  and DR methods (arxiv-digest 07-09).** Karim & Hu — *Which Regularized
  Propensity-Score and Doubly Robust Methods Are Best Calibrated When
  Exposures or Outcomes Are Rare?* (arXiv 2607.07065, stat.AP). Plasmode
  simulation anchored on NHANES with 25 investigator-specified covariates
  and 142 prescription-derived proxies; ten pipelines combining OAL,
  GLiDeR, HAL with IPTW and TMLE; three scenarios (frequent, rare
  exposure, rare outcome) under a null-RD truth. Directly relevant to
  your GLP-1 / SGLT2 / CFTR-modulator pharmacoepi work — the *early-
  adoption years* of any drug class are exactly the "rare exposure"
  regime this paper characterizes. **HIGH.**
- **Prior-informed conditional GGM on UKB proteomics (arxiv-digest
  07-01).** Mapelli, Massi, Cuccuru, Di Angelantonio, Ieva — *Prior-
  informed conditional Gaussian graphical models: an application to
  protein interaction network reconstruction* (arXiv 2606.31805, stat.AP;
  same senior author as the multimorbidity paper above). UKB
  cardiometabolic proteomics (n = 49,129, p = 366 Olink proteins) with
  covariate-dependent, prior-informed network estimation; recovers 34
  T2D-associated network-central candidate biomarkers, several
  detectable only via connectivity (not differential expression). Pairs
  with the multimorbidity paper as a methodological set from the same
  group. **HIGH.**
- **Patient-specific knowledge-graph + LINCS perturbation for drug
  response (arxiv-digest 07-07).** Bang, An, Sung, Yun, Kim, Lee —
  *Predicting Therapeutic Outcome via Aligning Patient-Specific
  Knowledge Graph and Gene-Level Perturbation Representations* ("PREDIKTOR",
  arXiv 2607.04557, cs.LG). Individualized gene-regulatory network per
  patient from tumor RNA-seq (DysRegNet), augmented with DrugBank drug-
  target links; CLIP-style contrastive alignment to a frozen LINCS-L1000
  perturbation model. Zero-shot transfer to the I-SPY2 trial. On the
  drug-repurposing + ML-for-precision-health axis; the *patient-specific*
  KG framing (rather than a single population-level KG) is the
  differentiating move and matches your INTERESTS preference for
  *explainable* KG output over opaque link-prediction. **HIGH.**
- **Residual-on-residual regression as a stable alternative to AIPW /
  TMLE (arxiv-digest 07-01).** Naimi, Jin, Yu, Parisi, Bodnar —
  *Residual-on-Residual Regression as a Tool for Effect Estimation in
  Observational Data* (arXiv 2606.30976, stat.ME). Applied to
  nuMoM2b pregnancy cohort; residual-on-residual regression is
  concordant with AIPW/TMLE under near-nominal conditions and
  *outperforms* both under positivity violations when the true effect is
  approximately constant. Directly usable as a triangulation strategy
  for your causal-inference pharmacoepi work — worth a slot in the
  standard-analysis playbook next to IPW and TMLE. **HIGH-methods.**
- **Complexity of genomic diagnosis: UKB + Generation Study newborn
  genome sequencing (Bone, 2026).** Sethuraman et al. — *Complexity of
  genomic diagnosis: Lessons learnt from the UK Biobank and Generation
  study newborn genome sequencing analyses*. Double-feed: surfaces on
  the **"UK Biobank" keyword** alert **and** the **"variant
  interpretation" / "variant classification" keyword** alert. Newborn
  genome sequencing at population scale is the frontier for VUS-density
  and penetrance-under-population-screening questions — directly on your
  variant-interpretation + UKB threads. **HIGH.**
- **Uncertainty-calibrated adaptation of clinical transformer FMs (npj
  Health Systems).** Chung & Yoon — *Uncertainty-calibrated adaptation
  of clinical transformer foundation models enhances in-hospital
  mortality and hospital readmission prediction* (surfaced by the
  *Yuan Luo citations* feed). Directly on your EHR-FM thread with the
  *calibration* twist your INTERESTS file calls out explicitly
  ("Foundation-model fairness and calibration audits when grounded in
  EHR data"). **HIGH.**

Counts: **8 HIGH**, **5 METHODS-WATCH**, rest SKIP. Volume is
comparable to a normal 3-week window despite the arxiv-digest fetch
gaps; the standout is the double-feed AoU phenotyping paper on your own
author feed (item #1) and the twin UKB-cardiometabolic papers from the
Mapelli/Ieva group (items #3 and #4).

---

## HIGH priority — detailed reports

### 1. Computational phenotyping of sexually transmitted infections with the All of Us Research Program from 2010 to 2023

- **Authors / venue:** F. Shi, H. Xia, S. Weissman, X. Li, X. Yang —
  *JAMIA open*, 2026.
- **Surfaced by:** **Double-feed** — (a) *Joshua C. Denny — new related
  research*, (b) ***Chenjie Zeng — new related research (your own
  feed).*** Two independent Scholar-relevance channels for one paper,
  including your own author feed, is a high-signal pattern; the last
  time the pipeline saw this was the Chen et al. nephrolithiasis
  PheWAS+PRS paper in the 06-20 report.
- **Thread:** **EHR phenotyping & OMOP** (computational phenotype
  development is the paper's central contribution) **+ All of Us
  biobank** (the paper's cohort) **+** possibly **infectious-disease
  pharmacoepi** (STI treatment cascades in AoU are a natural
  target-trial-emulation target if the phenotype is validated).
- **What it is (from the abstract):** "Objectives: This study aimed to
  [develop a computational phenotype for sexually transmitted infections
  (STIs) in the All of Us Research Program]." The 2010-2023 window (13
  years of longitudinal follow-up) is one of the longer AoU windows in
  the literature, and JAMIA open is the standard venue for EHR-
  phenotype-validation papers of this class. Given the author list
  (Yang and Li are the Columbia/USC EHR-phenotyping lineage), this is
  almost certainly a validated phecode-or-equivalent computational
  phenotype with chart-review or claims-external validation.
- **Why it matters to you:** Four reasons.
  (a) **Your own feed firing is the highest-precision channel this
  pipeline has.** Google's relevance model rarely surfaces papers to a
  named-author feed unless there's citation overlap or strong
  methodological similarity. This paper is more likely than average to
  cite your AoU phenotyping work.
  (b) **AoU + computational-phenotyping is the core stack** of your EHR-
  phenotyping thread. Any newly validated computational phenotype on
  AoU is a candidate primitive for downstream PheWAS / MR / TTE work.
  (c) **STI phenotyping specifically has been an underused AoU
  primitive.** Most AoU phenotyping papers so far have been on cardio-
  metabolic (T2D, HTN, CAD) or major-outcome (mortality, HF, stroke)
  targets; STI is a genuinely new phenotype family and the 13-year
  window enables incidence-and-reinfection modeling that most AoU
  studies don't have.
  (d) **The Denny feed pairing.** Denny (former AoU CSO, now Vanderbilt)
  is the AoU-phenotyping methodological locus; his feed lighting up on
  this paper is field-consensus signal that this is a citation-worthy
  AoU phenotyping paper.
- **Action:** **HIGH — read first.**
  (i) Check whether it cites your AoU phenotyping / PheTK / phecode-x
  work. Given the double-feed firing, at least one citation is likely.
  (ii) Note the phenotype-definition strategy — pure ICD/phecode? phecode
  + medication (antibiotics with STI indication)? phecode + lab (RPR,
  chlamydia/gonorrhea NAAT)? The medication + lab combination is the
  more rigorous design and would be the citation-worthy piece.
  (iii) Check the validation strategy — chart review, claims comparison,
  or self-report survey. AoU has the WEAR / social-history survey
  linkage that could be used for STI-phenotype validation.
  (iv) Worth noting for any future STI-adjacent phenotype work (e.g.,
  HIV / HBV comorbidity phenotyping in AoU) and as a possible template
  for validated AoU phenotypes in general.

### 2. Polygenic scores as modifiers in Mendelian diseases

- **Authors / venue:** A. Schmidt, K.U. Ludwig, H.O. Heyne —
  *Medizinische Genetik*, 2026.
- **Surfaced by:** *10 new citations to articles by George Hripcsak*
  feed; explicitly cites "Polygenic risk alters the penetrance of
  monogenic kidney disease."
- **Thread:** **Variant interpretation (ACMG/ClinGen)** — specifically
  the penetrance / modifier axis, which ACMG hasn't formalized **+
  Genetic epidemiology / PRS** (PRS as a modifier is the emerging
  composite-risk framing) **+ Rare disease** (the population being
  modified consists of Mendelian variant carriers).
- **What it is:** A review-tier paper (venue = *Medizinische Genetik*,
  German-language medical-genetics journal, English-language review
  literature-adjacent) synthesizing the PRS-as-modifier-of-Mendelian-
  penetrance literature. Ludwig is a Bonn cleft/PRS methodologist;
  Heyne is Berlin (epilepsy genetics). The cited article ("Polygenic
  risk alters the penetrance of monogenic kidney disease") is likely
  Yu et al. or the Van der Ven / Cheng lineage that has been running
  this analysis in UKB and All of Us.
- **Why it matters to you:** Four reasons.
  (a) **Directly instantiates the INTERESTS bullet** "penetrance
  estimation for monogenic variants under population-screening
  conditions (vs. clinically ascertained cohorts)." PRS-as-modifier is
  the *quantitative* half of that bullet — how much does polygenic
  background shift Mendelian variant penetrance in
  population-ascertained cohorts?
  (b) **The kidney-monogenic anchor** connects directly to your APOL1
  work. APOL1 is not strictly Mendelian but is a high-effect risk
  variant with variable penetrance — the same PRS-as-modifier
  methodology applies, and the review likely covers ADPKD / COL4A5 /
  Alport as adjacent monogenic-kidney anchors.
  (c) **Composite-risk-model framing.** Your INTERESTS file lists
  "composite risk models stacking PRS with rare pathogenic variants"
  explicitly. A review of the modifier literature is a useful default
  citation for framing this composite-scoring work.
  (d) **Hripcsak citation-graph firing.** Hripcsak's group does not
  usually publish on monogenic penetrance directly, so this paper
  citing his work implies methodological (rather than substantive)
  overlap — likely on the observational-cohort penetrance-estimation
  side.
- **Action:** **HIGH — read as a review to anchor citations.**
  (i) Extract the review's canonical disease list — which Mendelian
  diseases have PRS-modifier evidence in 2026 (T1D, BRCA-cancer, LDLR-
  hypercholesterolemia, LQT1/2/3, HCM, ADPKD, etc.).
  (ii) Note the *methodological framings* the review distinguishes —
  effect-modification on the absolute-risk scale vs. relative-risk
  scale, main-effects vs. interaction terms, penetrance-shift vs.
  age-at-onset-shift.
  (iii) Cite in any composite-risk write-up you'd be asked to produce.
  (iv) Worth cross-checking against the ClinGen VCEP monogenic-
  penetrance guidance — no formal VCEP guidance on PRS-modifier
  incorporation exists as of this writing.

### 3. Enhancing comorbidity network inference with risk-enriched health trajectories embedding

- **Authors / venue:** N. Fontana, A. Mapelli, E. Di Angelantonio, F.
  Ieva — *arXiv 2607.04702*, stat.AP, 2026-07-06.
- **Surfaced by:** `arxiv-digest` 2026-07-07 (score 3: `uk biobank`,
  `biobank`, `multimorbidity` keyword hits).
- **Thread:** **Chronic disease clustering & multimorbidity** (this is
  the paper's central topic) **+ EHR-linked biobank** (UKB) **+**
  adjacent to **causal inference** (they explicitly do a confounding-
  evaluation step to inform the sparsity penalty).
- **What it is:** Comorbidity-network inference paper that addresses
  three limitations of prior work: (i) cross-sectional statistics
  ignoring temporal information, (ii) confounding by shared risk
  factors, (iii) no direct-vs-indirect distinction (yielding fully-
  connected networks). Their solution: individual health-trajectory
  embeddings capturing semantic similarity + temporal co-occurrence,
  fed into a sparse GGM with Lasso regularization *weighted by a prior*
  derived from a dedicated confounding-evaluation step over 76 shared
  risk factors. Applied to 24 cardiometabolic diseases in UK Biobank;
  identifies four disease communities aligned with the cardiometabolic
  taxonomy, then derives community-based patient representations,
  clusters those into four *progression phenotypes* with significantly
  different long-term survival.
- **Why it matters to you:** Four reasons.
  (a) **Directly on the multimorbidity / disease-trajectory-clustering
  thread.** Cardiometabolic multimorbidity is one of your INTERESTS
  file's specific application areas. Four progression phenotypes from
  UKB is a citation-worthy empirical result.
  (b) **The confounder-prior into the Lasso is methodologically
  cleaner than most comorbidity-network work.** Standard comorbidity
  networks (Hidalgo, Rzhetsky lineage) treat shared-risk-factor
  confounding poorly; this paper formalizes it as a prior on the
  sparsity penalty, which is a design worth cribbing for other
  network-inference work (e.g., proteomic networks, medication
  networks).
  (c) **The temporal-embedding-of-trajectories primitive** is
  transferable — semantic similarity + temporal co-occurrence maps
  onto phecode-sequence embeddings, which is a natural downstream
  primitive for EHR foundation-model-adjacent work.
  (d) **Same senior author (Ieva) publishes item #4 below** on UKB
  proteomics. The Politecnico di Milano / HDR UK group is running a
  coherent UKB-cardiometabolic-network research program; the two
  papers should be read together.
- **Action:** **HIGH.**
  (i) Read for the confounder-prior construction — how are 76 risk
  factors mapped into a per-edge prior weight? This is the main
  methodological innovation.
  (ii) Note the survival-analysis validation of the four progression
  phenotypes — hazard ratios, K-M curves, or restricted mean survival
  time? RMST is more clinically actionable.
  (iii) Compare against the Hidalgo / Rzhetsky comorbidity-network
  literature explicitly — is the direct-vs-indirect distinction
  quantitatively better?
  (iv) Potential template for any cardiometabolic-multimorbidity
  network you might build in All of Us; UKB→AoU replication of the
  four progression phenotypes would be a strong paper.

### 4. Prior-informed conditional Gaussian graphical models: an application to protein interaction network reconstruction

- **Authors / venue:** A. Mapelli, M.C. Massi, G. Cuccuru, E. Di
  Angelantonio, F. Ieva — *arXiv 2606.31805*, stat.AP, 2026-06-30. Code
  released at github.com/AlessiaMapelli/Prior-informed-conditional-GGMs.
- **Surfaced by:** `arxiv-digest` 2026-07-01 (score 3: `uk biobank`,
  `biobank`, `precision medicine`).
- **Thread:** **Biobank + omics** (UKB-PPP proteomics n = 49,129, p =
  366 Olink proteins) **+ ML for precision health** (biomarker
  discovery, network-central-only detectable candidates) **+ adjacent
  to multimorbidity** (T2D-network perturbations recovered, cardio-
  metabolic + cancer pathways enriched).
- **What it is:** Prior-informed conditional GGM that (i) integrates
  database-derived interaction priors as structured penalty weights
  and (ii) supports covariate-dependent, personalized network
  perturbations. The structured penalty selectively incorporates
  priors into population-level network estimation while leaving
  context-specific perturbations entirely data-driven — the key
  observation being that curated databases capture canonical
  interactions, not disease-specific signals, so the prior should
  regularize the *canonical* network only, not the *perturbation*.
  Applied to UKB cardiometabolic proteomics (n = 49,129, p = 366);
  recovers 34 T2D-associated network-central candidate biomarkers,
  several detectable *only through connectivity, not differential
  expression*, and identifies six biologically coherent protein
  communities with distinct pathway enrichments.
- **Why it matters to you:** Three reasons.
  (a) **UKB-PPP is the leading population-scale proteomics resource,
  and the field's citation graph is now consolidating around it.** Any
  proteomic-signature / proteomic-PRS / proteomic-aging work you'd do
  in AoU or MVP starts from UKB-PPP methodology.
  (b) **The "network-central-only detectable" biomarkers** are the
  methodologically interesting piece — a biomarker with no univariate
  signal but strong network centrality is exactly what standard
  DE-analysis misses. This is a useful frame for arguing against
  univariate biomarker screens in composite-risk-model work.
  (c) **Composability with the multimorbidity paper (item #3).** Both
  papers are from the same senior author (Ieva) and both operate on UK
  Biobank cardiometabolic data — one on disease networks, one on
  protein networks. A natural next step is to bridge them (proteomic
  perturbation → disease-network propagation), which is not yet
  reported in the abstract set.
- **Action:** **HIGH.**
  (i) Read for the structured-penalty construction — how are database
  priors converted into per-edge weights, and how is the "trust the
  prior on canonical, ignore it on perturbation" split operationalized?
  (ii) Note the *six protein communities* and their pathway
  enrichments; these become a default cross-reference for any
  proteomic-signature work.
  (iii) Clone the released code (github link above) if a proteomic-
  network primitive is on your roadmap; the covariate-dependent
  personalization is unusual and worth prototyping.
  (iv) Pair with the Fontana multimorbidity paper (#3) as a
  methodological unit from the same group.

### 5. Which Regularized Propensity-Score and Doubly Robust Methods Are Best Calibrated When Exposures or Outcomes Are Rare? A Plasmode Study of Proxy-Based Confounding Adjustment

- **Authors / venue:** M.E. Karim, W. Hu — *arXiv 2607.07065*, stat.AP,
  2026-07-08.
- **Surfaced by:** `arxiv-digest` 2026-07-09 (score 3: `propensity
  score`, `inverse probability`, `g-computation`).
- **Thread:** **Causal inference & pharmacoepidemiology** — this is a
  methods-comparison paper directly on the design decisions you make
  every time you spec a target-trial emulation. Also relevant to the
  **variable-selection sub-thread** (OAL vs GLiDeR vs HAL) and to
  **debiased ML** in the causal ML sub-thread.
- **What it is:** Plasmode simulation anchored on National Health and
  Nutrition Examination Survey (NHANES 2013-2018, 25 investigator-
  specified covariates + 142 prescription-derived proxies) with a known
  null RD (true risk difference = 0). Compares ten pipelines combining
  three regularized variable-selection strategies (outcome-adaptive
  LASSO [OAL], group LASSO / GLiDeR, highly-adaptive LASSO [HAL]) with
  two doubly-robust estimators (IPTW, TMLE). Three scenarios: frequent,
  rare exposure, rare outcome. Reports bias, SE, relative error, 95%
  coverage, and runtime. Key findings: OAL-IPTW, GLiDeR, and HAL-TMLE
  are best-calibrated overall; LASSO-TMLE pipelines under-cover
  modestly (91-93%) in the rare scenarios; under rare exposure,
  LASSO-IPTW has the largest bias and inflated SE (over-covers
  conservatively) — TMLE removes these problems. Runtimes span <1 s
  to >16 h.
- **Why it matters to you:** Four reasons.
  (a) **Directly informs your pharmacoepi design choices.** Your
  INTERESTS file names GLP-1 RAs, SGLT2is, CFTR modulators, and HRT
  as active drug-class threads. Early years of adoption for GLP-1 RAs
  in AoU, SGLT2is in older cohorts, and CFTR modulators broadly are
  *rare-exposure* regimes exactly — this paper's rare-exposure
  scenario is the modal design pattern for your drug-class TTE work.
  (b) **The variable-selection-times-estimator design matrix is the
  right level of detail** for a methods paper — it separates the
  variable-selection question (LASSO vs OAL vs GLiDeR vs HAL) from the
  estimator question (IPTW vs TMLE) rather than confounding the two.
  Useful as a reference-class methods paper.
  (c) **The null-RD-truth anchor** is under-used in the pharmacoepi
  methods literature and is the correct calibration baseline. Expect
  this to become a template design for future PS-method comparisons.
  (d) **Compute accounting.** The 1 s → 16 h runtime spread is
  operationally meaningful — HAL is theoretically ideal but not
  runnable at biobank scale; the paper's calibration ranking should
  be read jointly with the compute cost when choosing a default
  pipeline for AoU / MVP work.
- **Action:** **HIGH — read as methods reference.**
  (i) Note the recommended default: OAL (IPTW), GLiDeR, or HAL (TMLE)
  for best calibration. GLiDeR is the interesting new-to-you option
  (group LASSO on outcome+treatment models jointly).
  (ii) Under rare exposure, TMLE > IPTW for LASSO — flip the default
  in your GLP-1 early-adoption analyses.
  (iii) Track the compute footprint: HAL-TMLE > 16 h is likely
  prohibitive at AoU scale; if it's the best-calibrated pipeline, that
  motivates a scaled-down evaluation strategy (subsample, then run HAL,
  then extrapolate).
  (iv) Cite in any TTE methods write-up alongside Hernán & Robins.

### 6. Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations (PREDIKTOR)

- **Authors / venue:** D. Bang, S. An, I. Sung, I. Yun, S. Kim, S. Lee
  — *arXiv 2607.04557*, cs.LG, 2026-07-06.
- **Surfaced by:** `arxiv-digest` 2026-07-07 (score 1: `knowledge
  graph`).
- **Thread:** **Drug repurposing** (specifically the *explainable KG*
  sub-bullet in INTERESTS — "GNN approaches with explainable hypothesis
  output — path or subgraph rationales") **+ ML for precision health**
  (treatment-effect heterogeneity, patient-specific model) **+**
  adjacent to **variant interpretation** (individualized gene-regulatory
  network from tumor RNA-seq).
- **What it is:** Patient-centered multi-view drug-response prediction
  framework. For each patient: (i) construct an individualized gene-
  regulatory network from tumor expression via DysRegNet, augmented
  with drug-target links from DrugBank; (ii) a graph neural encoder
  yields a drug-centric embedding grounded in patient-specific
  mechanism; (iii) in parallel, a frozen condition-specific gene-gene
  attention model pretrained on LINCS L1000 generates a simulated
  post-perturbation transcriptomic profile for the same patient-drug
  pair; (iv) the two views are aligned via a CLIP-style contrastive
  objective with drug-context hard negatives; (v) concatenated
  representations feed end-to-end response classification. Evaluated on
  TCGA under patient-, drug-, and tissue-split evaluations; zero-shot
  transfer to I-SPY2 clinical trial improves AUROC by 5.6% over
  baselines. Aligned embeddings yield stable gene and pathway
  attributions that recover known mechanisms.
- **Why it matters to you:** Four reasons.
  (a) **Directly on your explainable-KG drug-repurposing preference.**
  Your INTERESTS file favors "explainable hypothesis output (path or
  subgraph rationales rather than opaque link-prediction scores)" — the
  gene / pathway attributions here are exactly that pattern.
  (b) **Patient-specific KG rather than population-level KG** is the
  differentiating design choice. Most drug-repurposing KG methods
  (DTI-net, MOLI, DeepPurpose lineage) build one KG per drug or one
  population KG; a *patient-specific* KG is what enables treatment-
  effect heterogeneity claims. This is the methodological pattern to
  watch as GNN-based drug-repurposing matures.
  (c) **Zero-shot I-SPY2 transfer is a meaningful external validity
  check.** Most drug-repurposing benchmark work stops at cross-
  validation on TCGA / CCLE / GDSC; zero-shot transfer to a real
  clinical trial is a stronger claim.
  (d) **LINCS L1000 as a *frozen* perturbation-model backbone** is a
  design pattern likely to spread — perturbation FMs (Perturb-Seq,
  Prep-Seq) will increasingly be used as frozen backbones rather than
  end-to-end trained. Track for the general pattern.
- **Action:** **HIGH.**
  (i) Note the DysRegNet-augmented-with-DrugBank construction — that
  primitive is directly reusable for non-oncology drug-repurposing
  work (rare-disease repurposing in particular, where DysRegNet gives
  you an individualized regulatory graph even from small patient
  cohorts).
  (ii) Extract the gene / pathway attribution methodology — is it
  attention-weight-based, gradient-based, or subgraph-explainer-based?
  Subgraph explanations are the most clinically defensible.
  (iii) Compare against ExplainableGNN-DR / MolePathXplain / DR-KG
  baselines if any of those are reported.
  (iv) Consider whether the CLIP-style contrastive objective could
  bridge phecode-embedding + PRS-embedding for a related
  "patient-specific risk KG" idea.

### 7. Residual-on-Residual Regression as a Tool for Effect Estimation in Observational Data

- **Authors / venue:** A.I. Naimi, Q. Jin, Y.-H. Yu, S.M. Parisi, L.M.
  Bodnar — *arXiv 2606.30976*, stat.ME, 2026-06-29.
- **Surfaced by:** `arxiv-digest` 2026-07-01 (score 2: `inverse
  probability`, `causal inference`).
- **Thread:** **Causal inference & pharmacoepidemiology** — methods
  paper directly on IPW/AIPW/TMLE alternatives. Naimi is a well-known
  epidemiologic-methods author; the paper is a triangulation-strategy
  proposal.
- **What it is:** Residual-on-residual regression (RoR) as a stable
  alternative to AIPW and TMLE under weak-positivity violations. Fit
  confounder-adjusted models for outcome and exposure, then regress
  outcome-residuals against exposure-residuals via OLS. Illustrated on
  the nuMoM2b (Nulliparous Pregnancy Outcomes Study, n = 7,923)
  estimating the association between high vegetable intake density and
  preeclampsia. RoR yields near-identical point estimates to AIPW and
  TMLE (modest preeclampsia risk reduction), with **comparable performance
  under standard conditions and substantially better performance than a
  misspecified parametric model when the exposure effect is
  approximately constant**. Under simulated positivity violations, RoR
  *outperforms* AIPW and TMLE when the true effect is coded in a
  partially linear model.
- **Why it matters to you:** Three reasons.
  (a) **Triangulation across estimators is now standard for pharmacoepi
  claims;** your GLP-1 / SGLT2 / CFTR-modulator TTE work already runs
  ≥2 estimators (IPW + TMLE, typically). RoR adds a third leg that is
  cheap, interpretable, and works under positivity violations — exactly
  the setting where IPW and TMLE are least stable.
  (b) **Partially-linear-model assumption is not always innocuous** —
  the paper is careful to note RoR is best when the effect is
  approximately constant. In your CFTR-modulator work (large effect
  heterogeneity across CFTR genotype) this may not hold, so read
  carefully before adopting.
  (c) **Computational simplicity.** RoR is OLS of residuals — trivial
  to run at any scale, whereas TMLE and DML have engineering overhead.
  This makes RoR a useful *sensitivity-analysis* estimator even when
  your primary estimator is TMLE.
- **Action:** **HIGH-methods — add to the standard-analysis playbook.**
  (i) Add RoR as a third-leg triangulation in any TTE spec.
  (ii) Under positivity violations (large-effect drug-class exposures
  in small subpopulations), promote RoR from sensitivity to co-primary.
  (iii) Note the "approximately constant effect" caveat — flag when
  RoR is inappropriate (e.g., CFTR-genotype-stratified modulator
  effects).
  (iv) Cite alongside Karim & Hu (item #5) as the pair of 2026
  pharmacoepi-methods references.

### 8. Complexity of genomic diagnosis: Lessons learnt from the UK Biobank and Generation Study newborn genome sequencing analyses

- **Authors / venue:** C. Sethuraman, S. Keigwin, S. Delaney, S.
  Makino, J. Hirst et al. — *Bone*, 2026.
- **Surfaced by:** **Double-feed** — (a) *"UK Biobank" keyword* alert,
  (b) *"variant interpretation" OR "variant classification" keyword*
  alert.
- **Thread:** **Variant interpretation (ACMG/ClinGen)** — the paper's
  central topic **+ EHR-linked biobank (UK Biobank)** as one of the two
  data sources **+ rare disease** — the Generation Study is the UK's
  newborn genome-sequencing program, with rare-disease diagnosis as its
  central use case.
- **What it is:** From the abstract snippet, the paper reports lessons
  learnt from parallel analyses of two large sequencing programs — the
  UK Biobank (adult population-scale WGS, n ≈ 500k) and the Generation
  Study (UK's newborn genome-sequencing program targeting ~200k babies).
  These two cohorts represent opposite ascertainment strategies —
  adult healthy-volunteer bias vs. newborn population-screening — but
  share the technical challenges of high-throughput variant
  interpretation at population scale.
- **Why it matters to you:** Four reasons.
  (a) **Newborn genome sequencing at population scale is the frontier
  for penetrance-under-population-screening questions** — exactly the
  INTERESTS bullet under PheWAS/phecode ("penetrance estimation for
  monogenic variants under population-screening conditions vs.
  clinically ascertained cohorts"). The Generation Study is the largest
  such cohort in the world; its published-lessons paper is a default
  citation for any population-screening-penetrance work.
  (b) **UK Biobank as the paired comparator** gives you within-paper
  the exact contrast your INTERESTS file specifies: adult population
  cohort vs. newborn population screen — different ascertainment,
  different age distribution, different diagnostic priors, same
  variant-interpretation challenges. This is unusually clean for a
  methods-lessons paper.
  (c) **Double-feed firing on both UKB and variant-interpretation
  keywords** means the pipeline treats this as high-signal from two
  independent angles; that's the kind of cross-cutting paper that
  gets cited across sub-communities.
  (d) **Publication in *Bone*** is unusual — likely because a specific
  disease-family example (osteogenesis imperfecta, hypophosphatasia,
  monogenic skeletal dysplasias) anchors the paper. Worth checking if
  a specific ClinGen VCEP is referenced — bone/skeletal-dysplasia
  VCEP guidance is one of the more recently formalized VCEP outputs.
- **Action:** **HIGH.**
  (i) Read for the ACMG-criteria application patterns — how do UKB
  and Generation Study differ in evidence weightings? PS4
  (case-control) is harder in population-screening, PP1 (segregation)
  is easier in newborn-trio designs.
  (ii) Extract the reported diagnostic-yield numbers if any — Generation
  Study reported yield is a benchmark for other newborn-sequencing
  programs.
  (iii) Cross-check with GUARDIAN / BabyScreen / BabySeq2 as adjacent
  newborn-sequencing programs — those cohort comparisons drive the
  operational-scaling narrative.
  (iv) Cite in any population-screening-penetrance write-up.

### 9. Uncertainty-calibrated adaptation of clinical transformer foundation models enhances in-hospital mortality and hospital readmission prediction

- **Authors / venue:** P.H. Chung, B.J. Yoon — *npj Health Systems*,
  2026.
- **Surfaced by:** *10 new citations to articles by Yuan Luo* feed.
- **Thread:** **EHR foundation models** (clinical transformer FMs are
  the CLMBR / MOTOR / EHRSHOT / FEMR / MEDS lineage) **+** the
  **calibration** sub-bullet ("Foundation-model fairness and calibration
  audits when grounded in EHR data") **+ ML for precision health**
  (mortality / readmission are decision-adjacent).
- **What it is:** Method paper for adapting pretrained clinical
  transformer FMs to downstream tasks (in-hospital mortality and
  30-day readmission) with an explicit *uncertainty-calibration*
  step, rather than a standard fine-tuning-plus-Platt-scaling
  pipeline. The npj Health Systems venue is the emerging home for
  clinical-FM adaptation papers (as distinct from foundation-model
  pretraining papers, which land in Nature Medicine / npj Digital
  Medicine). Yoon is Texas A&M / Brookhaven; Yuan Luo's citation is
  the Northwestern EHR-FM lineage.
- **Why it matters to you:** Three reasons.
  (a) **Calibration-aware adaptation is the missing operational layer**
  between "we pretrained an EHR FM" and "we deployed it clinically."
  Pretrained models are miscalibrated in-distribution and worse under
  distribution shift; this paper's contribution is exactly at that gap.
  (b) **In-hospital mortality + readmission are the two canonical
  benchmarks** (EHRSHOT, MEDS-Tab-baseline). Any new EHR-FM adaptation
  method uses these; adopting uncertainty-calibrated adaptation as a
  default is easy to evaluate against those baselines.
  (c) **Adjacent to your INTERESTS bullet on FM calibration audits.**
  If you're auditing an FM for fairness/calibration in AoU or MVP,
  starting from a calibration-aware adaptation baseline is a stronger
  design than starting from vanilla fine-tuning.
- **Action:** **HIGH.**
  (i) Read for the calibration method — temperature scaling
  post-hoc? Bayesian last-layer? Deep ensembles? Focal-loss
  fine-tuning? The method choice constrains the compute footprint.
  (ii) Note the benchmarks — MIMIC-IV? EHRSHOT? UPMC? Cohort identity
  matters for transferability.
  (iii) Compare against MEDS-Tab-calibrated baselines if reported.
  (iv) Consider incorporating into any FM-audit work in AoU / MVP.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **KG-TRACE: A Neuro-Symbolic Framework for Mechanistic Grounding in
  Antimicrobial Resistance Prediction** — N. Garg, S. Jain, S. Yadav, B.K.
  Bhargava, G. Singh, A. Srivastava, P. Kar — *arXiv 2606.26179*, cs.LG,
  2026-06-24 (`arxiv-digest` 06-26). Neuro-symbolic KG-grounded ML for
  AMR prediction on *M. tuberculosis* (CRyPTIC cohort). Off your
  clinical-EHR threads (this is bacterial genomics), but the
  **Biological Grounding Ratio (BGR)** metric — dataset-level alignment
  between neural attributions and symbolic biology — is a
  transferable primitive for any explainable-drug-repurposing work
  where you have a symbolic ground truth (e.g., ATC hierarchy for
  drug classes, HPO for phenotypes). **METHODS-WATCH.**

- **Privacy-preserving federated tensor decomposition of single-cell
  immune data: recovering multicellular programs across institutions**
  — A. Faes, S.M. van den Berg, M.A. Haeri — *arXiv 2606.24938*, q-bio.GN,
  2026-06-22 (`arxiv-digest` 06-25). Federated single-cell tensor
  decomposition with secure aggregation. Off your EHR-federation
  thread substantively (single-cell rather than EHR), but the design
  pattern — local subspace estimation + coordinator-side stacked SVD +
  federated global-mean centering — is *directly translatable* to
  federated EHR-FM training under privacy constraints. If your AoU /
  MVP / UKB federated work advances, this is the reference-class
  design. **METHODS-WATCH.**

- **Universal cell embedding provides a foundation model for cell
  biology** — Y. Rosen, Y. Roohani, A. Agrawal, L. Samotorčan et al. —
  *Nature*, 2026 (surfaced by *Jure Leskovec — new articles*).
  Single-cell FM (UCE / Universal Cell Embedding); off-thread for
  clinical EHR-FM work but relevant if you want the field's leading
  citation on "what a biology-FM looks like at Nature-tier scale."
  **METHODS-WATCH.**

- **FaceMesh2HPO: Hierarchical Classification via Cascading Feature
  Elimination — Application to Human Phenotype Ontology-Aligned Facial
  Phenotyping** — F. Hellmann, A. Hustinx, B.D. Solomon, T.C. Hsieh et
  al. — 2026 (surfaced by *Lisa Bastarache — new related research*
  feed). HPO-term assignment from facial-mesh phenotypes; on the HPO /
  rare-disease-diagnosis axis but the facial-mesh modality is narrow.
  Track as a template for cascade-elimination hierarchical
  classification over an ontology (HPO or SNOMED) — the design
  pattern generalizes. **METHODS-WATCH.**

- **DiSTILL: A Hybrid Cloud-HPC Workflow System for Reproducible
  Spatial Transcriptomics Analysis** — M.J.T. Tan, V.G.H. Fuentes, N.
  Yerra, M. Kapetanaki, P. Rashidi, K. Huang, P.V. Benos — *arXiv
  2606.30693*, q-bio.GN, 2026-06-28 (`arxiv-digest` 07-01). Reproducible
  workflow-system contribution operationalizing IBD spatial-
  transcriptomics analysis over a hybrid cloud-HPC architecture. Off-
  thread for you substantively (spatial transcriptomics rather than
  clinical EHR), but the **IBD anchor** and the reproducible-workflow
  framing may be worth a scan if IBD spatial-omics enters your rare-
  disease repurposing thread. **METHODS-WATCH.**

- **IMGL-AWNN: Incomplete Multiview Graph Learning With Adaptive
  Weighted Nuclear Norm for Drug Repurposing in Biomedical Systems** —
  Y. Qian, Q. Zou, L. Liu, W. Ding, Y. Ding, X. Guo — *IEEE Trans.
  Systems …*, 2026 (surfaced by *"drug repurposing" keyword* alert).
  Multiview graph-learning for drug-target-disease link prediction with
  incomplete-view handling. Framework-heavy, low-signal on the
  explainable / EHR-grounded axes your INTERESTS file prefers. **METHODS-
  WATCH-leaning-SKIP.** Logged for completeness only.

---

## SKIP / noise (logged, no action)

- **LLM-Enhanced Dynamic Financial Knowledge Graphs for Cross-Entity
  Signal Propagation** (Zhang, arxiv-digest 07-14, score 1) — financial
  NLP, incidental KG keyword hit. This is the *only* paper the arxiv-
  digest surfaced today; the fact that a finance paper is what fires on
  your queue is exactly the `knowledge graph` keyword-noise pattern
  flagged in prior reports.
- **Causal Inference with Video Features as Treatments** (Nakamura et
  al., arxiv-digest 07-08) — political-science / 2020 U.S. presidential
  ad application, causal keyword hit but off-thread.
- **Understanding Guest Preferences and Optimizing Two-sided
  Marketplaces: Airbnb as an Example** (Wu & Schmierer, arxiv-digest
  07-02) — Airbnb marketplace paper. Same authors as the marketplace
  causal-ML paper on 06-30; two consecutive Airbnb-marketplace papers
  in the same window is a noise pattern.
- **Estimating Supply Incrementality in Two-sided Marketplaces
  (Airbnb)** (Wu et al., arxiv-digest 07-01) — Airbnb again. Debiased
  ML applied to marketplace supply; methodology is on-topic (double/
  debiased ML), but the marketplace application is off-thread.
- **Hierarchical Clustering As a Novel Solution to the Notorious
  Multicollinearity Problem in Observational Causal Inference** (Wu et
  al., arxiv-digest 07-01) — marketing application, causal inference
  keyword hit but off-thread.
- **Dynamic Prediction of Alternating Recurrent Events via Neural
  Network** (Loe et al., arxiv-digest 07-01) — mood-of-medical-residents
  application; methodology is on the recurrent-events axis but the
  application is niche.
- **Can Tabular In-Context Learners Generalize to Biomolecular Property
  Prediction?** (Guan et al., arxiv-digest 07-01) — protein / small-
  molecule property prediction; adjacent to drug-repurposing but the
  paper is a benchmark eval, not a repurposing method.
- **The Turning Point of 3D Plant Phenotyping** (Jia et al., arxiv-
  digest 07-03) — plant phenotyping, off-thread despite the "phenotyping"
  keyword hit.
- **Are Tabular Foundation Models Robust to Realistic Query Distribution
  Shifts in Microbiome Data?** (Perciballi et al., arxiv-digest 06-25) —
  microbiome, off-thread.
- **Evaluating HWE and Association in GWAS: A Unified Procedure**
  (Böhringer & Holzmann, arxiv-digest 06-30) — GWAS QC method, on-thread
  but narrow (HWE conditioning); worth a glance only if you're revising
  a GWAS QC pipeline.
- **DNA Language Models: An Assessment of Pre-Training for Fine-Tuning
  Tasks** (Karpinsky et al., arxiv-digest 06-30) — DNA-LM benchmark;
  off your clinical-EHR-FM thread but adjacent to the FM literature.
- **Data-Efficient Multimodal Alignment for Histopathology-based
  Molecular Prediction** (Winter et al., arxiv-digest 06-30) — H&E-
  molecular alignment, oncology-FM, off-thread.
- **Semantic insurance pricing with LLMs** (Blier-Wong & Kusmenko,
  arxiv-digest 06-30) — insurance, false-positive on `motor` keyword
  (motor third-party liability, not "MOTOR" the EHR FM). Classic
  keyword collision.
- **Causal ASCEND: Scalable Two-tier Causal Discovery on High
  Dimensional Multi-omics Data** (Asiedu & Watson, arxiv-digest 07-07)
  — multi-omics causal discovery; interesting but not clinical.
  Track only if a specific multi-omics analysis lands on your queue.
- **Hereditary Pancreatitis** (Sehmbhi & Lucas, *Gastroenterology
  Clinics* 2026, surfaced by "Cystic fibrosis carriers" keyword alert)
  — CF-adjacent (CFTR mutations cause pancreatitis) but this is a
  clinical review of hereditary pancreatitis, not a modulator or
  pharmacoepi paper. **Logged, not read.**
- **No association between alcohol consumption and hip osteoarthritis
  in the "All of Us" research program** (Patel et al., 2026) — AoU
  cohort but topic (alcohol / hip OA) is off your tracked disease
  threads.
- Miscellaneous LLM / AI-safety / methods-review papers surfaced by
  Szolovits / Zitnik / Natarajan / Hripcsak feeds (SPATIA cell
  phenotypes, ChemFlow KG-attention EGFR modulators, Data Journalist
  Agent, AutoTrainess, Bifocal Diffusion LLMs, Citation-Aware
  Continual Pre-Training, MOSAIC, DrugDiscoveryBench, JAMA LLM-
  disagreement piece, adversarial-testing dental LLMs, glaucoma
  fundus KG, Kohane commentary) — all in the general
  LLM/biomedical-AI space, none on your specific clinical-decision
  threads.
- **Systemic Autoimmune Rheumatic Disease-Associated ILD** review
  (Ozduygu et al., 2026) — autoimmune-keyword hit, review-tier,
  off-thread.
- **Alzheimer's / eye-examination MR study** (Kiser et al., 2026,
  mendelian-diseases keyword feed) — MR of eye-exam-derived features
  vs. AD; keyword-collision on `mendelian` (Mendelian randomization ≠
  Mendelian disease), classic pattern flagged in prior reports.
- **SMR Analysis Integrating GWAS and eQTL Data Reveals UHRF1BP1 and
  SNRPC as Potential Drug Targets for Low Back Pain** (Xie et al., 2026,
  PheWAS keyword feed) — SMR for back-pain drug targets; on the
  MR/eQTL methods axis but specific application is niche.
- Various miscellaneous author-feed citation-graph leaks (pediatric-
  EHR NLP, HPV vaccine safety Japan, obesity prevention, biliprotein
  redesign, etc.) — off-thread.

---

## Suggestions for the pipeline

Carrying forward all prior-report suggestions (none actioned) and
adding three new observations:

1. **`arxiv-digest` fetch failures are now a persistent operational
   issue** — nine of twenty days in this window produced ~138-byte
   placeholder digests, matching the 06-20 pattern. Extended zero-
   paper runs (07-04 → 07-06, 07-10 → 07-13) are almost certainly
   polling failures, not genuine dry days. Suggest:
   (a) distinguish placeholder-vs-real-zero output explicitly in the
   generated markdown (e.g., produce `2026-07-11.md` with a
   `**Pipeline error: 4/4 categories failed to fetch**` block
   rather than a bare "Relevant papers: 0");
   (b) add jittered retry-with-backoff per category;
   (c) if the failure repeats within a run, escalate to a workflow
   annotation so the failure is visible in the GitHub Actions UI
   without opening the log.

2. **`knowledge graph` keyword continues to leak non-biomedical
   papers** — today's 07-14 arxiv-digest is a *finance* paper; earlier
   in the window (07-07, PREDIKTOR — on-thread) got in on the same
   keyword, but the signal-to-noise on this keyword is now ~1:3 over
   the window. Concrete fix as suggested in the 06-20 report:
   compound-filter to `(knowledge graph) AND (medical OR biomedical
   OR clinical OR EHR OR phenotype OR drug OR disease OR patient OR
   gene)`; a keyword change to `biomedical knowledge graph` OR
   `clinical knowledge graph` is a lower-recall alternative.

3. **New pattern: single-group cluster from Politecnico di Milano /
   HDR UK.** The Fontana (07-07) and Mapelli (07-01) papers are from
   the same senior author (Ieva) on the same cohort (UK Biobank
   cardiometabolic) with related methodology (sparse network
   inference with structured priors). Two papers from one group in
   one window on your top thread is worth noting but not automating
   — flag as a possible collaboration / citation cluster to watch,
   not a keyword to add.

4. **Consider adding an "AoU + phenotyping" specific alert** — item
   #1 (Shi et al. STI phenotyping) surfaced via a general author feed
   (Denny), not by keyword. A `"All of Us" AND phenotyping` compound
   alert would catch this class of paper directly without waiting for
   an author-feed forward.

5. **Carry-forward: add `cs.LG` and `stat.ME` source categories** —
   items #5 (Karim & Hu, stat.AP), #6 (Bang et al., cs.LG), and #7
   (Naimi et al., stat.ME) are already in the current source set;
   this suggestion has been actioned or partially actioned. Kept for
   confirmation.

6. **Carry-forward from 06-20:** `mendelian diseases` keyword continues
   to fire mostly on Mendelian *randomization* studies rather than
   Mendelian *disease* studies (item today: Kiser et al. eye-AD MR).
   Same suggestion: change to `Mendelian disease` (singular, with a
   trailing space) OR compound filter `(mendelian OR monogenic) AND
   (disease OR variant OR carrier OR penetrance)`.

7. **Carry-forward:** track `proteomic signature` / `PRS stability` /
   `noncoding variant interpretation` keywords, all first suggested in
   06-20 and none actioned.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 9 | (1) Shi et al. AoU STI computational phenotyping [Denny + self-feed], (2) Schmidt et al. PRS-as-Mendelian-modifier review [Hripcsak citations], (3) Fontana et al. UKB comorbidity-network trajectory clustering [arxiv-digest 07-07], (4) Mapelli et al. UKB-PPP prior-informed conditional GGM [arxiv-digest 07-01], (5) Karim & Hu rare-exposure/outcome PS-DR calibration [arxiv-digest 07-09], (6) Bang et al. PREDIKTOR patient-specific KG drug response [arxiv-digest 07-07], (7) Naimi et al. residual-on-residual regression triangulation [arxiv-digest 07-01], (8) Sethuraman et al. UKB+Generation Study variant-interpretation lessons [UKB + variant-interp double keyword], (9) Chung & Yoon uncertainty-calibrated clinical-transformer adaptation [Yuan Luo citations] |
| METHODS-WATCH | 6 | KG-TRACE (neuro-symbolic AMR), Faes et al. (federated tensor decomp), UCE / Universal Cell Embedding (Nature), FaceMesh2HPO (HPO cascade), DiSTILL (IBD spatial-omics workflow), IMGL-AWNN (drug-repurposing multiview GL) |
| SKIP | ~30 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH over one
window), this catch-up sweep delivers 9 HIGH over ~3.5 weeks, i.e.,
comparable HIGH-density per calendar week. Two notable patterns:
(a) the double-feed AoU phenotyping paper on your own author feed
(item #1) is the highest-precision signal this window; (b) the twin
Mapelli/Ieva UKB-cardiometabolic papers (#3 and #4) mark a
methodological research program worth tracking as a cluster. The
outstanding operational issue is the persistent `arxiv-digest` fetch-
failure pattern — nine placeholder days out of twenty is a large
enough coverage gap that on-thread papers may be silently missed.
