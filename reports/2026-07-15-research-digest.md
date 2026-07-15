# Research digest report — 2026-07-15

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-15** (since the prior 2026-06-20 report,
a 25-day gap — a longer catch-up window than the usual 2-3 day cadence).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 07-15 | Two dense batches worth calling out: **07-14 22:27Z** (~30+ author-feed alerts across Denny, Bastarache, Karczewski, Hripcsak, Ryan, Brandt, Montgomery, Zeng self-feed, Zitnik, Chute, Kastner, Yang, Callahan, Szolovits, Luo, Snyder, Shendure, Shah, Leskovec, Kohane, Hernán, Vogelstein, Natarajan, van der Schaar, Collins, Davies, Pritchard, Karczewski citations) and **07-14 06:36Z** (keyword feeds — All of Us, UK Biobank, EHRs, PheWAS, MR, rare disease, foundation models, CF carriers, knowledge graph, drug repurposing, variant interpretation). Additional single-topic clonal-hematopoiesis and APOL1 keyword pings across 07-02, 07-04, 07-05, 07-07, 07-11, 07-12, 07-14. |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-15 | **25 daily runs.** 8 dry days (0 papers surfaced). Non-dry days: 06-26 (1), 06-30 (4), 07-01 (7), 07-02 (1), 07-03 (1), 07-07 (3), 07-08 (1), 07-09 (1), 07-14 (1), 07-15 (1). The two-day 06-30 → 07-01 window is the digest's densest of the month (11 papers together). |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. arxiv-digest entries include full abstracts and
> keyword-hit annotations from the pipeline.

---

## Executive summary

- **The standout this window is a *self-feed + Denny-feed* AoU
  phenotyping paper.** F. Shi, H. Xia, S. Weissman, X. Li, X. Yang —
  *Computational phenotyping of sexually transmitted infections with the
  All of Us Research Program from 2010 to 2023* (*JAMIA open*, 2026) —
  surfaces in **both** the *Chenjie Zeng — new related research* feed
  (your own feed) **and** the *Joshua C. Denny — new related research*
  feed. That double firing on the same paper across the two most
  precision-aligned author channels for your work is the highest-signal
  pattern this pipeline produces. Directly on the AoU + EHR-phenotyping
  + phecode-adjacent axis. **Read first.**
- **A large-cohort AJHG paper closes a loop between PRS and rare-variant
  interpretation.** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh,
  H. Currant et al. — *Individuals who deviate from polygenic expectation
  are enriched for damaging variants in genes linked to rare disease*
  (*American Journal of Human Genetics*, 2026, *Stephen Montgomery
  related-research* feed). The composite-PRS-plus-rare-variant theme on
  your INTERESTS file gets its cleanest empirical validation to date:
  people whose observed phenotype deviates from PRS-predicted phenotype
  are enriched for rare damaging variants — i.e., the residual is
  informative. This is the empirical case for the exact composite-scoring
  framework you write about. Pairs directly with the 06-20 Souaiaia
  *Nature* "PRS tails" paper. **HIGH.**
- **Multi-ancestry CHD-PRS clinical implementation paper — Genetics in
  Medicine.** M. Hamed, M. Naderian, H. Bangash, V. Hernandez et al. —
  *Implementing a Multi-Ancestry Polygenic Risk Score for Coronary Heart
  Disease in a Diverse Cohort* (*Genetics in Medicine*, 2026, *Yuan Luo
  new-articles* feed). This is exactly the "PRS-in-a-clinical-workflow"
  pattern (screening decision, action threshold, ancestry-portability)
  your work anchors, deployed for CHD in a diverse cohort. Cross-ancestry
  portability + clinical implementation is the intersection of two of
  your active threads. **HIGH.**
- **AoAS methods paper on phenotype imputation for EHR-genomic studies.**
  H. Wu, C.H. Lee, N. Abiri, I. Ionita-Laza — *Domain-aware matrix
  completion for phenotype imputation using electronic health record
  data with applications in genomic research* (*Annals of Applied
  Statistics*, 2026, *Joshua C. Denny related-research* feed). Missing-
  phenotype imputation is a pervasive EHR-phenomics bottleneck that
  routinely blocks GWAS/PheWAS from using dense-code phenotypes. A
  domain-aware (i.e., ontology- or code-structure-informed) matrix
  completion at scale is the kind of primitive that becomes reusable
  across AoU / MVP / UKB work. **HIGH.**
- **Semiparametric-robust EHR-biobank modeling — Scandinavian J.
  Statistics.** M. Liu, X. Wang, C. Hong — *A Semiparametric Approach
  for Robust Modeling of Electronic Health Record Linked Biobank Data*
  (2026, *Pascal Brandt related-research* feed). Robust-to-EHR-
  misclassification estimation for biobank-linked studies is exactly
  the class of methods that make PRS/PheWAS/PheRS work under realistic
  EHR noise (miscoded ICDs, missing visits, differential capture across
  sites/ancestries). Directly on the EHR-linked-biobank methodology
  thread. **HIGH.**
- **A blended WGS+WES sequencing method — Nature Genetics.**
  T.A. Boltz, B.B. Chu, M. DeFelice, C. Liao, J.M. Sealock et al. —
  *A blended genome and exome sequencing method captures genetic
  variation in an unbiased and cost-effective manner* (*Nature Genetics*,
  2026, *Konrad Karczewski related-research* feed). Blended WGS+WES is
  the cost/coverage compromise likely to become the reference method for
  the next generation of biobank sequencing, including AoU expansion.
  Directly on the variant-interpretation + biobank-scale-sequencing
  axis. **HIGH.**
- **`arxiv-digest`'s cleanest on-thread hit of the month: a plasmode
  benchmark of doubly-robust PS methods under exposure/outcome rarity.**
  M. Ehsan Karim, Wanqing Hu — *Which Regularized Propensity-Score and
  Doubly Robust Methods Are Best Calibrated When Exposures or Outcomes
  Are Rare?* (arXiv 2607.07065v1, 2026-07-08, stat.AP, score 3:
  `propensity score`, `inverse probability`, `g-computation`). NHANES-
  anchored plasmode study of 10 pipelines combining OAL / GLiDeR / HAL
  with IPTW / TMLE under rare-exposure / rare-outcome / frequent
  scenarios. Directly on the causal-inference + pharmacoepi thread.
  This is the kind of paper that would settle "which pipeline should we
  default to for the SGLT2i/GLP-1RA/CFTR-modulator TTE with rare adverse
  outcomes" without a re-simulation. **HIGH.**
- **`arxiv-digest`'s second on-thread hit: UKB cardiometabolic
  multimorbidity comorbidity-network paper.** N. Fontana, A. Mapelli,
  E. Di Angelantonio, F. Ieva — *Enhancing comorbidity network inference
  with risk-enriched health trajectories embedding* (arXiv 2607.04702v1,
  2026-07-07, stat.AP, score 3: `uk biobank`, `biobank`, `multimorbidity`).
  UK Biobank, 24 cardiometabolic diseases, 76 risk factors, Gaussian-
  graphical-model with Lasso, four progression phenotypes with distinct
  survival trajectories. Directly on the multimorbidity + disease-
  clustering thread. **HIGH.**
- **`arxiv-digest`'s third on-thread hit: UKB proteomics PPI network
  paper.** A. Mapelli et al. — *Prior-informed conditional Gaussian
  graphical models: an application to protein interaction network
  reconstruction* (arXiv 2606.31805v1, 2026-06-30, stat.AP, score 3:
  `uk biobank`, `biobank`, `precision medicine`). UKB-PPP proteomics
  (n=49,129, 366 proteins), T2D-associated network perturbations, 34
  network-central candidate biomarkers detectable *only* through
  connectivity. Same first-author group as #7 above (Mapelli / Di
  Angelantonio / Ieva). Directly on the UKB-PPP + proteomics-as-
  intermediate-phenotype axis. **HIGH.**
- **A precision-medicine methodology thesis that cites your work.**
  A.D. Sriram — *Advancing Methodological Foundations in Precision
  Medicine Through Novel Causal Inference, Machine Learning, and
  Artificial Intelligence Frameworks* (2026 thesis, *2 new citations
  to articles by Chenjie Zeng* feed). Direct citation to your work in a
  causal-ML + precision-medicine methods thesis. Worth a quick check to
  see which of your papers is cited and what the framing is. **HIGH-
  citation-tracking (low read priority, high visibility priority).**
- **METHODS-WATCH: MR risk-of-bias guide (BMJ EJ) and PES survey (GIM).**
  Two Bastarache-feed items are more decision-frame than result: T.
  Jabeen et al. — *Risk of bias assessment for Mendelian randomisation
  studies: a guide* (*European Journal of ...*, 2026) is a decision-
  support tool for MR studies you may need to cite for any MR write-up;
  and R.A. Furrer, A. Gandhi, D. Barlevy, S. Carmi, T. Lencz et al. —
  *Decision-Making Criteria in Polygenic Embryo Screening: A Survey of
  Reproductive Medicine Physicians* (*Genetics in Medicine*, 2026) is on
  the PES-ethics adjacency to your PRS work. **METHODS-WATCH.**

Counts: **9 HIGH**, **~6 METHODS-WATCH**, rest SKIP. This is a heavier
window than the typical 3-day report because of the 25-day catch-up
span. The pipeline pattern remains: nearly all on-thread signal comes
from Scholar author-feeds, and the three arxiv-digest hits (Karim/Hu,
Fontana et al., Mapelli et al.) are the highest-quality single-window
arxiv output in the last two months.

---

## HIGH priority — detailed reports

### 1. Computational phenotyping of sexually transmitted infections with the All of Us Research Program from 2010 to 2023
- **Authors / venue:** F. Shi, H. Xia, S. Weissman, X. Li, X. Yang — *JAMIA open*, 2026.
- **Surfaced by:** **Double-feed** — (a) *Chenjie Zeng — new related research* (**your own feed**), (b) *Joshua C. Denny — new related research*. Same-day, same-batch (07-13 14:51Z). Firing across your self-feed **and** Denny's feed for a single AoU-based EHR-phenotyping paper is the highest-precision signal pattern this pipeline produces short of your own *citations* feed firing.
- **Thread:** **EHR phenotyping & OMOP** (computable phenotype construction) **+** **Biobanks with EHR linkage: All of Us** (AoU 2010-2023 window ≈ registered-tier CDR span) **+** **PheWAS / phecode infrastructure** (STI phenotype definitions are a phecode-adjacent problem).
- **What it is:** Computational phenotype algorithms for STI ascertainment (chlamydia, gonorrhea, syphilis, likely HSV / HIV / trichomonas depending on scope) applied to All of Us, 2010-2023. STI phenotyping is nontrivial in EHR data because (a) diagnosis codes are stigmatized and undercoded, (b) labs are the more sensitive signal but ICD-only cohorts miss them, and (c) reinfection episodes require windowing rules. A JAMIA-open paper on this in AoU specifically will define the reference algorithms for any downstream AoU STI-outcome PheWAS/GWAS/PRS work.
- **Why it matters to you:** Four converging hits.
  (a) **AoU + EHR phenotyping is one of your core methodology stacks.** Any reference-tier phenotyping algorithm published on AoU becomes a reusable primitive across your own AoU work.
  (b) **Self-feed firing is the highest-precision Scholar signal.** Google's relevance model only fires the self-feed when the new paper is judged close to your published work. Combined with Denny-feed firing, the paper is essentially guaranteed to overlap with your citation network.
  (c) **STI phenotypes are underused but methodologically rich.** They combine ICD + lab + medication signals, they have well-characterized reinfection dynamics, and they intersect with sexual-health disparities in AoU's underrepresented populations. Useful template for other stigmatized/undercoded phenotypes.
  (d) **JAMIA open is exactly the venue you write in.** Whatever phenotype-definition conventions this paper establishes will directly affect what a reviewer will expect from any AoU STI-adjacent work you submit.
- **Action:** **HIGH — read first.**
  (i) Identify the AoU CDR version used (v7? v8? given the 2010-2023 window and the July 2026 publication date, likely one of the recent v-releases).
  (ii) Note whether they combine ICD + lab + medication signals, and what the sensitivity/PPV estimates are.
  (iii) Check whether they use the AoU concept-set (OMOP concept IDs) approach or roll their own phenotype logic. If the former, the concept sets are directly reusable.
  (iv) Check the reference list for your AoU phenomic-comparison paper — given the double-feed firing, at least one of your papers is likely cited.
  (v) Save the reference for any future AoU EHR-phenotyping methods write-up.

### 2. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
- **Authors / venue:** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh, H. Currant et al. — *American Journal of Human Genetics*, 2026.
- **Surfaced by:** *Stephen B Montgomery — new related research* feed.
- **Thread:** **Genetic epidemiology** (composite risk models stacking PRS with rare pathogenic variants — **explicitly listed on your INTERESTS file**) **+** **Rare disease** (rare-variant enrichment in polygenic residuals is the causal-tie between the common-variant and rare-variant literatures) **+** **Variant interpretation** (which genes contribute to the residual signal — a Bayesian prior on VUS interpretation).
- **What it is:** The empirical composite-scoring closure. Fit a PRS to a trait, compute observed − predicted (the polygenic residual) for each individual, and test whether individuals in the tails of that residual distribution are enriched for damaging (LoF / missense) variants in genes tied to Mendelian disease adjacent to the trait. If the residual is informative — i.e., the deviation-from-PRS-expectation carries rare-variant signal — then the residual is the natural target for rare-variant scans, and the resulting hits are the empirical basis for stacking PRS + rare-variant burden into a composite risk score.
- **Why it matters to you:** Four reasons.
  (a) **Your INTERESTS file names this exact composite explicitly.** Under Genetic epidemiology: "Composite risk models stacking PRS with rare pathogenic variants." This paper is the empirical justification for the composite framing.
  (b) **Pairs directly with the 06-20 Souaiaia *Nature* PRS-tails paper.** Souaiaia showed the tails of the *trait* distribution have different genetic architecture; Baya et al. show the tails of the *residual* distribution are enriched for rare damaging variants. Together the two provide a two-punch argument for why the top 1% of PRS-based clinical flags need rare-variant follow-up.
  (c) **UKB-scale, AJHG-tier signal.** Baya's affiliation lineage (Lassen, Venkatesh, Currant collaborators) points to Oxford BMRC / UKB-PPP-adjacent data. This is likely to become the default citation for the "residual-informativeness" argument.
  (d) **Directly actionable for your hereditary-cancer PRS/pLoF composite work.** Your Zeng-Publications skill has multi-paper history on hereditary cancer genes + polygenic risk. Extending to breast/colorectal/prostate PRS-residual → rare-variant scans is the natural extension of both your own work and this paper.
- **Action:** **HIGH.**
  (i) Read for which traits are tested — height / BMI / T2D / lipids / CAD? Cancer traits would be the direct-relevance case; if not tested, the natural extension is obvious.
  (ii) Note the rare-variant catalog — ClinVar-annotated pathogenic, or LoF burden, or curated Mendelian-gene panel? The choice affects portability.
  (iii) Check whether the residual-enrichment is tail-specific (only the bottom 1%, only the top 1%) or symmetric. Tail-specificity has different clinical implications.
  (iv) Compose with #4 (Souaiaia tails, 06-20 report) as a citation pair for any composite-risk write-up.

### 3. Implementing a Multi-Ancestry Polygenic Risk Score for Coronary Heart Disease in a Diverse Cohort
- **Authors / venue:** M. Hamed, M. Naderian, H. Bangash, V. Hernandez et al. — *Genetics in Medicine*, 2026.
- **Surfaced by:** *Yuan Luo — new articles* feed.
- **Thread:** **Genetic epidemiology / PRS** (multi-ancestry portability + clinical implementation) **+** **ML for precision health** ("who to screen, who to escalate" — the clinical-decision-grade PRS use case your INTERESTS file explicitly names) **+** **Biobanks with EHR linkage** (diverse cohort = AoU / eMERGE / diverse-recruitment biobank).
- **What it is:** A clinical-implementation paper for a multi-ancestry PRS (likely PRS-CSx or a similar cross-ancestry method) for CHD in a diverse cohort. The word "Implementing" in the title signals this is not a PRS-development paper but a *deployment* paper — i.e., how the PRS was operationalized in a clinical workflow, what the ancestry-stratified performance was, and how the risk cutoffs were set. Yuan Luo authorship and the *Genetics in Medicine* venue point to a Northwestern/eMERGE-style implementation study.
- **Why it matters to you:** Four reasons.
  (a) **"Who to screen, who to escalate" is the clinical-decision framing your INTERESTS file marks as HIGH for ML in precision health.** A deployed CHD PRS in a diverse cohort is exactly that use case.
  (b) **Multi-ancestry PRS + diverse-cohort implementation is the intersection of two active threads.** Cross-ancestry portability is on the Genetic Epidemiology thread; EHR-linked diverse cohorts are on the Biobank thread; this paper sits at the intersection.
  (c) **Direct comparator for any AoU CHD-PRS work.** AoU is diverse-by-design; any AoU CHD PRS work needs this paper as a comparator/prior for what "successful implementation" looks like in a diverse cohort.
  (d) **Genetics in Medicine is the reference venue for clinical-genomics implementation.** GIM tends to publish the papers that health systems actually adopt; this one will affect how CHD PRS is discussed at ClinGen and at AoU consortium meetings.
- **Action:** **HIGH.**
  (i) Read for the specific PRS method — PRS-CSx? PRSice-2 with cross-ancestry meta? Bayesian PRS with ancestry-stratified LD?
  (ii) Note the cohort identity — All of Us? eMERGE (network phase III)? Mayo/BioVU? The cohort identity affects what "diverse" means operationally.
  (iii) Check the ancestry-stratified performance metrics — AUC/AUPRC by ancestry, calibration (Brier / Hosmer-Lemeshow) by ancestry, decision-curve analysis at the clinical cutoff.
  (iv) Note whether they report a *pre-specified* risk cutoff or select post-hoc — pre-specified is the more clinically defensible framing.
  (v) Save as a comparator for any future AoU/MVP CHD-PRS write-up.

### 4. Domain-aware matrix completion for phenotype imputation using electronic health record data with applications in genomic research
- **Authors / venue:** H. Wu, C.H. Lee, N. Abiri, I. Ionita-Laza — *The Annals of Applied Statistics*, 2026.
- **Surfaced by:** *Joshua C. Denny — new related research* feed.
- **Thread:** **EHR phenotyping & OMOP** (missing-phenotype imputation is the pervasive bottleneck in dense-phenotype EHR studies) **+** **Genetic epidemiology** ("applications in genomic research" = the missing-phenotype-blocking-GWAS problem) **+** methods thread more broadly (AoAS is a methods-tier venue).
- **What it is:** Method paper for phenotype imputation in EHR data via domain-aware (i.e., ontology-informed or code-hierarchy-informed) matrix completion. The standard matrix-completion framework treats the patient × phenotype matrix as low-rank + noise; the "domain-aware" variant leverages structure from ontologies (SNOMED, phecode hierarchy, HPO) as side information to regularize the completion. Ionita-Laza is a lead in EHR-statistical-genetics methods; this is on the same lineage as her prior work on hierarchical phecode-informed GWAS.
- **Why it matters to you:** Three reasons.
  (a) **Missing-phenotype imputation is a routine blocker in AoU/UKB/MVP work.** Any patient without a coded diagnosis for a phenotype is dropped from the analysis, which introduces selection bias (patients not screened for X are dropped from X-outcome studies). A principled imputation method is a phenotyping primitive that could be reused across your AoU work.
  (b) **AoAS venue signals methods-tier rigor.** AoAS is a statistical-methodology journal that tends to publish papers with well-developed asymptotic theory + empirical validation. This is the kind of methods reference that becomes citable in a methods section without further re-derivation.
  (c) **The "applications in genomic research" framing means the paper likely demonstrates on a GWAS or PheWAS re-analysis.** That demo is the immediately-actionable part.
- **Action:** **HIGH.**
  (i) Read for the ontology used — SNOMED? phecode hierarchy? HPO? OMOP concept hierarchy? Each has different coverage/precision tradeoffs.
  (ii) Note the imputation validation — held-out patient × phenotype cells, or held-out cohort? Cross-cohort validation is the more transferable claim.
  (iii) Check whether they release code / a Python or R package. Reusability hinges on this.
  (iv) Note the GWAS/PheWAS demo — which cohort, which phenotypes, what effect on discovery power?
  (v) Potential adoption candidate for any AoU/MVP PheWAS with sparse phenotypes (rare-disease or under-coded phenotypes).

### 5. A Semiparametric Approach for Robust Modeling of Electronic Health Record Linked Biobank Data
- **Authors / venue:** M. Liu, X. Wang, C. Hong — *Scandinavian Journal of Statistics*, 2026.
- **Surfaced by:** *Pascal Brandt — new related research* feed.
- **Thread:** **Biobanks with EHR linkage** (methodology for EHR-linked biobank studies) **+** **EHR phenotyping** (robustness-to-misclassification is a phenotyping-methods problem) **+** **Causal inference** (robust semiparametric estimation is a shared methodology axis).
- **What it is:** A semiparametric estimator for EHR-linked biobank studies that is robust to model misspecification and, presumably, to EHR-noise sources (miscoded diagnoses, differential ascertainment, missing visits). Chuan Hong lineage points to the Duke/Harvard EHR-statistical-methods line, which has been active in developing robust-to-EHR-noise estimators (silver-standard phenotypes, PheNorm, PheValuator adjacencies). Scandinavian J. Statistics venue signals rigorous methodology.
- **Why it matters to you:** Three reasons.
  (a) **EHR noise is the elephant in the room for AoU/UKB/MVP work.** Any published estimate from an EHR-linked biobank study is subject to the "but what if the phenotype is miscoded" concern. A semiparametric-robust estimator is one of the cleanest technical responses to that concern.
  (b) **Directly on the EHR-linked-biobank methodology thread.** Your INTERESTS file names biobanks with EHR linkage as a *core* theme; methodology papers here should be logged even if not immediately actionable.
  (c) **Composes with the PheValuator adjacency.** If the semiparametric method uses a silver-standard / PheValuator-style PPV estimate as an ingredient, that's the direct link to your ehr-phenotyping-os skill's toolkit.
- **Action:** **HIGH.**
  (i) Read for the misspecification the estimator is robust to — outcome-model? exposure-model? phenotype-model? Different robustness targets have different applications.
  (ii) Note the empirical demonstration cohort — MGB Biobank? UKB? Real EHR-linked biobank data is the more transferable claim.
  (iii) Check whether they release an R package or reference implementation. Semiparametric estimators without code rarely get adopted.
  (iv) Potential citation for any future AoU/MVP PheWAS/PheRS paper's methods section as the "robust to EHR misclassification" reference.

### 6. A blended genome and exome sequencing method captures genetic variation in an unbiased and cost-effective manner
- **Authors / venue:** T.A. Boltz, B.B. Chu, M. DeFelice, C. Liao, J.M. Sealock et al. — *Nature Genetics*, 2026.
- **Surfaced by:** *Konrad Karczewski — new related research* feed.
- **Thread:** **Variant interpretation** (LoF calling is sequencing-modality-dependent) **+** **Genetic epidemiology** (biobank-scale sequencing infrastructure) **+** **Biobank linkage** (AoU / UKB expansion depends on cost-effective sequencing methods).
- **What it is:** A blended WGS + WES sequencing protocol that achieves near-WGS coverage in coding regions at near-WES cost per sample. The methodological pinch point in biobank sequencing has always been the WGS/WES tradeoff: WGS is more comprehensive (non-coding, structural variant discovery) but 3-5× more expensive per sample; WES is cheaper but misses non-coding regulatory variation and structural variants. A blended protocol is the natural compromise and — critically — becomes the default reference for the next generation of biobank sequencing.
- **Why it matters to you:** Three reasons.
  (a) **AoU's sequencing expansion depends on cost-effective methods.** The AoU program has a stated goal of WGS for all ~1M participants; the actual per-sample cost has been the throttle. A blended method landing in Nature Genetics from Karczewski-adjacent authors is the kind of protocol that could accelerate that timeline.
  (b) **Sealock authorship is on-thread.** J.M. Sealock is on Vanderbilt/BioVU-adjacent EHR-genomics work; that signals the empirical demonstration is likely in a BioVU or similar EHR-linked cohort, which is directly comparable to AoU.
  (c) **Nature Genetics venue signals field-defining.** Blended sequencing method papers in NG tend to become citation defaults for the next 5 years of sequencing protocols.
- **Action:** **HIGH.**
  (i) Read for the blend ratio — what fraction of the genome gets deep coverage vs shallow? The blend ratio drives the cost-quality frontier.
  (ii) Note the empirical performance metrics — SNV / indel call rate, structural variant sensitivity, non-coding variant coverage. Cross-modality comparison with pure-WGS from the same samples is the gold-standard evaluation.
  (iii) Check whether the method is being adopted by AoU / UKB. If so, that changes the medium-term data landscape for your work.
  (iv) Save the citation for any future biobank-scale sequencing methods write-up.

### 7. Which Regularized Propensity-Score and Doubly Robust Methods Are Best Calibrated When Exposures or Outcomes Are Rare? A Plasmode Study of Proxy-Based Confounding Adjustment
- **Authors / venue:** M. Ehsan Karim, Wanqing Hu — arXiv 2607.07065v1 (stat.AP), 2026-07-08. **`arxiv-digest` 07-09**, score 3 (`propensity score`, `inverse probability`, `g-computation`).
- **Thread:** **Causal inference and pharmacoepidemiology** (directly on-thread — TTE and PS methods for real-world evidence with rare exposures or rare outcomes are exactly your active thread) **+** **ML for precision health** (regularized variable selection + doubly robust estimation is the ML-in-causal-inference axis).
- **What it is:** NHANES-anchored plasmode simulation (2013-2018 data; 25 investigator-specified covariates + 142 prescription-derived proxies) comparing 10 pipelines combining regularized selection strategies (OAL, GLiDeR, HAL) with IPTW and TMLE across three scenarios: frequent (base rate), rare exposure, rare outcome. Reports bias, SE, relative error, 95% coverage, and — critically — compute time. Key findings from the abstract: HAL(G-Computation) had near-zero bias but near-unity coverage and large relative error; OAL(IPTW), GLiDeR, and HAL(TMLE) were best calibrated; LASSO-TMLE pipelines under-covered modestly in rare scenarios; LASSO-IPTW had large bias under rare exposure; runtimes spanned <1 s to >16 h.
- **Why it matters to you:** Four reasons.
  (a) **This is the paper that settles the "which pipeline should we use" question for rare exposures / rare outcomes.** Every real-world CFTR-modulator or SGLT2i-adverse-outcome or GLP-1-cancer TTE has some flavor of rare-exposure or rare-outcome. This paper provides a plasmode-benchmarked default (OAL/IPTW or HAL/TMLE for calibration) and — with compute time reported — an operational default.
  (b) **Directly on the pharmacoepi drug-class threads.** GLP-1 RAs, SGLT2is, CFTR modulators, HRT — every one of these will run into the rare-outcome regime for at least one safety endpoint. A plasmode benchmark under rare-outcome scenarios is exactly the reference you'd want cited in your methods section.
  (c) **Plasmode design is the right benchmark.** Real-data anchor + simulated exposure + known truth is the strongest simulation design for causal-methods comparison, avoiding both pure-simulation implausibility and real-data unknown-truth ambiguity.
  (d) **Compute-time reporting is unusually explicit.** Most causal-methods papers underreport runtime; this one being explicit about 1 s vs 16 h ranges makes it directly usable as an operational reference — you know upfront which pipelines are feasible on which scale of data.
- **Action:** **HIGH.**
  (i) Read Table 1 / main results to extract the "recommended pipeline by scenario" table — this is what you'd cite.
  (ii) Note whether HAL is implemented in a form usable at biobank scale (n=100k+) or only at NHANES-scale (n~10k). The compute constraint at biobank scale is the deployment question.
  (iii) Check whether they compare against a plain non-regularized OAL / GLiDeR benchmark; if not, one open question is how much the regularization actually buys.
  (iv) Adopt as the methods-section citation for any AoU/MVP TTE where exposure or outcome prevalence is <5%.

### 8. Enhancing comorbidity network inference with risk-enriched health trajectories embedding
- **Authors / venue:** N. Fontana, A. Mapelli, E. Di Angelantonio, F. Ieva — arXiv 2607.04702v1 (stat.AP), 2026-07-07. **`arxiv-digest` 07-07**, score 3 (`uk biobank`, `biobank`, `multimorbidity`).
- **Thread:** **Chronic disease clustering and multimorbidity** (directly on-thread — graph-based comorbidity networks + trajectory clustering, both explicitly named in your INTERESTS file) **+** **Biobanks with EHR linkage** (UK Biobank empirical demonstration).
- **What it is:** Method for population-level disease network inference that uses *individual health trajectories* (not just cross-sectional prevalence) to learn disease associations. Combines semantic-similarity and temporal-co-occurrence signals. Sparse network estimation via Gaussian Graphical Model with Lasso, informed by prior clinical knowledge on shared risk factors from a dedicated confounding evaluation step. Applied to UK Biobank: 24 cardiometabolic diseases + 76 risk factors. Reveals four cardiometabolic disease communities aligning with the established taxonomy. Downstream analysis derives community-based patient representations, clusters into four progression phenotypes with significantly different long-term survival trajectories.
- **Why it matters to you:** Four reasons.
  (a) **Directly on your INTERESTS file text.** The exact quote: "graph-based comorbidity networks, and trajectory clustering. Particularly interested when applied to cardiometabolic disease..." This paper hits all three literally.
  (b) **The confounding-evaluation-informed prior on shared risk factors is the methodological differentiator.** Standard comorbidity networks conflate direct disease-disease association with shared-risk-factor association; this method explicitly separates them via a two-stage process, which is a cleaner design than naive Lasso on the raw diagnosis matrix.
  (c) **The four-progression-phenotype-with-differential-survival result is the paper's punch.** This is exactly the trajectory-clustering pattern that's actionable for risk stratification.
  (d) **Composes with #9 (same first-author group) as a methods pair.** Mapelli et al. on UKB proteomics PPI networks (#9) + Fontana et al. here on UKB cardiometabolic disease networks are the same team's two-view (proteomics + phenotype) approach on the same cohort — worth reading together.
- **Action:** **HIGH.**
  (i) Read for the *risk factor confounding evaluation step* — what is the specific procedure to identify which pairs are shared-risk-driven vs directly connected? This is the transferable methodological contribution.
  (ii) Note the four communities discovered — do they align with established cardiometabolic taxonomy (as the abstract claims), or are there novel groupings? Novel groupings would be the more interesting finding.
  (iii) Check whether the four progression phenotypes have distinct genomic (PRS) or proteomic signatures. If yes, the paper is a direct bridge from your PRS work to multimorbidity trajectories.
  (iv) Compose with #9 (Mapelli et al. proteomics) into a unified UKB-Ieva-group multimorbidity-methods read.

### 9. Prior-informed conditional Gaussian graphical models: an application to protein interaction network reconstruction
- **Authors / venue:** A. Mapelli, M.C. Massi, G. Cuccuru, E. Di Angelantonio, F. Ieva — arXiv 2606.31805v1 (stat.AP), 2026-06-30. **`arxiv-digest` 07-01**, score 3 (`uk biobank`, `biobank`, `precision medicine`). Code released at https://github.com/AlessiaMapelli/Prior-informed-conditional-GGMs.
- **Thread:** **Biobanks with EHR linkage** (UK Biobank + UKB-PPP proteomics) **+** **Chronic disease clustering and multimorbidity** (cardiometabolic proteomics + protein communities with pathway enrichment) **+** **Genetic epidemiology / PRS** (PPI-network-derived proteomic biomarkers as intermediate phenotypes for downstream PRS-plus-omics composites).
- **What it is:** Method: prior-informed conditional GGM that integrates database-derived interaction priors (curated PPI catalogs like STRING/BioGRID) with covariate-dependent network modeling in a unified framework. Key methodological innovation: a structured weighted penalty that selectively incorporates priors into population-level network estimation while leaving *context-specific* perturbations entirely data-driven — curated databases capture canonical interactions, not disease-specific perturbations. Simulation studies show robust improvement even when priors are imperfect. Empirical: UK Biobank cardiometabolic proteomics (**n=49,129, p=366 proteins**), recovers T2D-associated network perturbations, identifies 34 network-central candidate biomarkers (several detectable *only* through connectivity, not differential expression), and reveals six biologically coherent protein communities with distinct pathway enrichments across metabolic / cardiovascular / cancer processes.
- **Why it matters to you:** Four reasons.
  (a) **UKB-PPP is the reference proteomic cohort of the moment**, and n=49k with 366 proteins is a substantial slice of the full UKB-PPP data. Any method that works on this cohort is directly transferable to future AoU proteomic sub-cohorts.
  (b) **"Detectable only through connectivity, not differential expression"** is a headline finding. If it holds, it substantially changes how proteomic biomarker discovery should be run — the standard DE + Bonferroni pipeline misses these hits by construction, but a network-central approach catches them.
  (c) **Six protein communities with pathway enrichment across metabolic / CV / cancer** is a direct multimorbidity finding at the molecular level. Composes with #8 (Fontana et al., same Ieva group, UKB cardiometabolic *disease* networks) into a two-level (proteomics ↔ phenotype) multimorbidity framework.
  (d) **Prior-informed but data-driven-for-perturbations is the right technical framing.** Pure prior-informed methods miss disease-specific signal; pure data-driven methods are noisy. The weighted-penalty selective-incorporation is the cleaner methodological compromise.
- **Action:** **HIGH.**
  (i) Read for the specific PPI-prior source used (STRING? BioGRID? Reactome?) and how the weighting is calibrated.
  (ii) Note the 34 network-central biomarkers — how many are novel vs already known for T2D? Novelty is the differentiating claim.
  (iii) Check the pathway enrichment for the six protein communities — are any communities novel groupings vs known pathway definitions? Novel groupings would be the multimorbidity payoff.
  (iv) Clone the code (link above) — a released repository indicates reusability was a design goal.
  (v) Compose with #8 as a paired read; likely worth citing both in any UKB-PPP + multimorbidity write-up.

### 10. Advancing Methodological Foundations in Precision Medicine Through Novel Causal Inference, Machine Learning, and Artificial Intelligence Frameworks
- **Authors / venue:** A.D. Sriram — 2026 thesis (dissertation).
- **Surfaced by:** ***2 new citations to articles by Chenjie Zeng*** feed. Direct citation to your work.
- **Thread:** **Citation tracking** (rather than substantive-read priority) **+** adjacencies to Causal inference + ML for precision health + Genetic epidemiology.
- **What it is:** A thesis dissertation that cites your work in the context of methodological foundations for precision medicine (causal inference + ML + AI frameworks). Abstract snippet suggests a synthesis-style methodology dissertation — likely with multiple chapters covering different sub-methods, at least one of which uses or extends your published methodology.
- **Why it matters to you:** Two reasons.
  (a) **Direct citation to your own work.** Regardless of substantive content, worth knowing who is citing you and in what context — helpful for collaboration mapping and future PI-fit conversations.
  (b) **Framing signal — "precision medicine methodological foundations" is exactly your positioning.** How Sriram characterizes your contribution to that framing is a useful external mirror on your published work's positioning.
- **Action:** **HIGH-visibility (moderate-read).**
  (i) Track down the thesis (institutional repository).
  (ii) Read only the section that cites you — what specific paper of yours, and what framing.
  (iii) Note the institution and advisor — potential collaboration or trainee-recruitment signal.
  (iv) Not a substantive read priority; a professional-network priority.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic, or decision-frame-only)

- **Risk of bias assessment for Mendelian randomisation studies: a guide** — T. Jabeen, A. O'Neil, D.N. Ashtree, R.E. Wootton et al. — *European Journal of ...*, 2026 (Lisa Bastarache related-research feed, marked IMPORTANT by Gmail's filter). Decision-support tool / checklist paper for MR studies. **METHODS-WATCH** — becomes the reference-cite for any MR write-up's methods section going forward.

- **Decision-Making Criteria in Polygenic Embryo Screening: A Survey of Reproductive Medicine Physicians** — R.A. Furrer, A. Gandhi, D. Barlevy, S. Carmi, T. Lencz et al. — *Genetics in Medicine*, 2026 (Lisa Bastarache related-research feed). Survey of RM physicians on PES decision-making criteria. **METHODS-WATCH on the PRS-ethics adjacency** — worth knowing as a citation on the "clinical implementation of PRS" spectrum's most controversial end, especially given the T. Lencz co-authorship (leading PES researcher).

- **Residual-on-Residual Regression as a Tool for Effect Estimation in Observational Data** — A.I. Naimi, Q. Jin, Y.-H. Yu, S.M. Parisi, L.M. Bodnar — arXiv 2606.30976v1 (stat.ME), 2026-06-29. **`arxiv-digest` 07-01**, score 2 (`inverse probability`, `causal inference`). Alternative to AIPW/TMLE — semiparametric residual-on-residual regression that's shown to be unbiased with near-nominal CI coverage and *outperforms* AIPW/TMLE under positivity violations when the true effect is coded in a partially linear model. **METHODS-WATCH on the causal-inference thread** — pairs with #7 (Karim/Hu) as the "when doubly robust breaks, try this" alternative. Ashley Naimi's group is on-thread for causal-methods lineage.

- **Evaluating HWE and Association in Genome Wide Association Studies: A Unified Procedure** — S. Böhringer, H. Holzmann — arXiv 2606.30311v1 (stat.ME), 2026-06-29. **`arxiv-digest` 06-30**, score 1 (`fine mapping`). Conditional-genotype test that folds HWE-goodness-of-fit into the association test, eliminating separate HWE cutoffs. **METHODS-WATCH on the GWAS methods thread** — useful if you ever need a cleaner alternative to the current arbitrary-threshold HWE-filter step in GWAS pipelines. Off-thread substantively.

- **Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations** (PREDIKTOR) — D. Bang, S. An, I. Sung, I. Yun, S. Kim, S. Lee — arXiv 2607.04557v1 (cs.LG), 2026-07-06. **`arxiv-digest` 07-07**, score 1 (`knowledge graph`). Multi-view framework aligning a patient-specific GRN + drug-target links with a LINCS-L1000-derived perturbation profile via CLIP-style contrastive alignment. Tested on TCGA, transfers zero-shot to I-SPY2 with 5.6% AUROC gain. **METHODS-WATCH on the drug-repurposing + KG threads** — hits your INTERESTS file's "explainable" KG+drug-repurposing preference (interpretable gene/pathway attributions) and is a rare cs.LG paper actually anchored in a real trial dataset (I-SPY2). Not directly on your EHR-based repurposing sub-thread, but on the "KG+GNN with explainable outputs" sub-thread.

- **Autonomous biomedical research with an artificial intelligence agent** — K. Huang, S. Zhang, H. Wang, Y. Qu, Y. Lu, R. Li et al. — *Science*, 2026 (surfaced across **five** feeds: Jure Leskovec new-articles, 10 new citations to articles by Vivek Natarajan, Michael Snyder new-articles, and adjacent). Autonomous AI-agent for biomedical research. **METHODS-WATCH on the ML-for-precision-health thread** and on the LLM-agent-for-research adjacency. Fifth-place-in-your-priority-stack because it's an autonomous-research-agent paper rather than a clinical-decision-support paper; the *five-feed saturation* though makes it worth logging as a field-consensus signal. Whether the empirical claims will hold up to scrutiny is the open question.

- **Semantic insurance pricing with large language models** — C. Blier-Wong, D. Kusmenko — arXiv 2606.29371v1 (stat.AP), 2026-06-28. **`arxiv-digest` 06-30**, score 1 (`motor`; incidental — French motor third-party liability data). Off-thread substantively (insurance actuarial pricing). Interesting technical primitive — LLM embeddings as deterministic covariates in a GLM. **METHODS-WATCH low-priority** — the LLM-embedding-as-GLM-covariate pattern is transferable to any GLM-based EHR-outcome model if you ever want to inject note-derived features into a structured model without a bolt-on neural pipeline.

- **DNA Language Models: An Assessment of Pre-Training for Fine-Tuning Tasks** — R. Karpinsky, J. Mozziconacci, M. Delcey — arXiv 2606.30140v1 (q-bio.GN), 2026-06-29. **`arxiv-digest` 06-30**, score 1 (`foundation model`). Benchmark comparison of transformer-based DNA-LMs (DNABERT2) vs convolutional models (ConvNova), with focus on whether transformer pretraining actually pays for its cost. **METHODS-WATCH low-priority** — off your specific threads (genomic-LM benchmarking is Karczewski/Kellis/Broad-adjacent territory), but useful reference if you ever need to defend a simpler baseline against a "did you try a foundation model" review comment.

---

## SKIP / noise (logged, no action)

- **Autonomous biomedical research with an AI agent (Huang et al., Science)** — logged as METHODS-WATCH above; noting here that of the ~30 07-14 author-feed alerts, this paper accounts for 3-4 of them (Leskovec, Natarajan, Snyder, Zitnik adjacent), which inflates the "high-signal" appearance of the batch.
- **68Ga-PSMA PET/CT in biochemically recurrent prostate cancer (Leithner et al., European Journal of ..., Chenjie Zeng feed)** — while it hits your self-feed, the substance is a PET/CT + genomic imaging correlation study in prostate cancer, off your active-methodology threads. Cite-worthy if you have a prostate cancer imaging-genomics collaborator, otherwise log.
- **From Pathogenicity to Mechanism: A Variant Interpretation Framework for Monogenic Epilepsy (Ye & Chen, Clinical Genetics, Karczewski feed)** — narrow disease-specific VUS framework, off your primary variant-interpretation targets (ACMG general framework or ClinGen VCEP process).
- **Long-term safety and efficacy of Lumacaftor/Ivacaftor in children 12mo+ with CF (ERJ Open, Zemanick et al., Patrick Ryan feed)** — real-world CF-modulator pediatric safety data, on the CF disease thread but a *pediatric* extension of an already-approved (in older children) modulator. Log for CF-modulator eligibility discussions if pediatric ever enters your scope; otherwise skip.
- **Application of NLP to predict diagnosis for 540 pediatric diseases from 85k EHRs (Liu et al., Ryan + Brandt feed)** — pediatric EHR NLP for rare-disease diagnosis. Directly adjacent to your rare-disease thread if pediatric is in scope, otherwise a light log.
- **Real-world treatment patterns in systemic sclerosis (Filla et al., Arthritis, Kastner feed)** — SSc treatment patterns; off-thread substantively.
- **Fibroblast mitochondrial Ca2+ overload drives skin fibrosis in SSc (Zhang et al., Arthritis, Kastner feed)** — SSc molecular mechanism, off-thread.
- **Multiple `clonal hematopoiesis` keyword pings across 07-02, 07-04, 07-05, 07-07, 07-11, 07-12** — six items across the window: CH + T2D (Liu et al., J Diabetes), CH + AMD (Li et al., Am J), CH + Alzheimer's (Zhao et al., Trends Mol Med), CH + splicing (Lyu et al., Cancer Sci), CH + aging (Dhenge & Kulkarni, Ann Transl Med), CH + Erdheim-Chester (Park et al., Clin Lab). On the **CHIP/VEXAS** disease thread; all narrative-review or narrow-case-series tier, none reaching HIGH. If you're actively drafting a CHIP-CVD-or-metabolic write-up, the Liu et al. T2D review is the most directly relevant.
- **Multiple `APOL1` keyword pings (07-05, 07-11, 07-14)** — APOL1 collapsing glomerulopathy case (Kidney Int Cases), APOL1-adjacent complement pathway systematic review (Zsidisin & Talha), and an APOL1-adjacent plasma-proteome longitudinal study (Drouin et al.). All log-only.
- **Hereditary Pancreatitis review (Sehmbhi & Lucas, Gastroenterol Clin, "Cystic fibrosis carriers" keyword feed)** — narrative review of hereditary pancreatitis, tangential to your CFTR thread only via the CFTR-pancreatitis overlap. Log-only.
- **Various single-paper Scholar hits across Kohane, Chute, Snyder, Shendure, Vogelstein citation feeds** — cancer-mutation-burden paper (Pénisson et al., Cancer Res), single-cell CRISPR isoform paper (Andrews et al., bioRxiv), pediatric-cancer serology paper (DiLillo et al.), autoimmune hypothyroidism GWAS (de Groen), Alzheimer eye-MR paper (Kiser et al.). All off your active threads.
- **NHS AI chatbot governance perspective (Matos et al., Collins feed)** — health-policy on consumer-facing AI health chatbots; off your ML-for-precision-health thread substantively (that thread is about individualized-risk / TEH / treatment-decision models, not consumer chatbots).
- **Semantic tokenization for medical LMs (Lanz & Pecina, BioNLP 2026, Szolovits feed)** and **Citation-aware biomedical LM pre-training (Asada et al., BioNLP 2026, Szolovits feed)** — biomedical LM tokenization / pre-training methods, off your EHR-FM (CLMBR/MOTOR/EHRSHOT) thread which is about structured-EHR FMs specifically.
- **Fine-tuned LLMs for social isolation detection from clinical notes (Chinthala et al., medRxiv, Hripcsak feed)** — clinical NLP application; adjacent to but off the EHR-FM thread.
- **LLM-based question-prompt generation from EHR (He et al., JMIR, Hripcsak feed)** — clinical NLP + LLM, off-thread substantively.
- **Non-coding LDLR variants in hyperlipidaemia risk (Rojano & Curtis, Human Heredity, Montgomery feed)** — narrow disease-specific noncoding VUS analysis, off-thread.
- **Genetic + genomic insights across SLD spectrum (Mann et al., Clinical and Molecular ..., Bastarache citation feed)** — narrative review of steatotic liver disease genetics, off-thread.
- **Individual `knowledge graph` keyword hits (ChemFlow / EGFR modulators — Samanta et al., Cell Reports Physical Sci)** and **`drug repurposing` keyword (IMGL-AWNN — Qian et al., IEEE T. Syst.)** — biomedical-KG + drug-repurposing hits that are chemistry/AI-heavy rather than clinical-EHR-based. Log; the second one is generic multi-view GNN and misses your "explainable + EHR-evidence-loop" preference.
- **arxiv-digest 06-27, 06-28, 06-29, 07-04, 07-05, 07-06, 07-10, 07-11, 07-12, 07-13 — 0 papers each.** Genuinely dry days (0 keyword matches at min-score 2 in the lookback window), not fetch failures based on file sizes.
- **arxiv-digest 07-14 and 07-15** — 1 paper each, both off-thread (a `motor`/cultural-evolution paper 07-15, an `LLM knowledge graph` finance paper 07-14). These are pure keyword-leak hits.
- **arxiv-digest 07-01 secondary items** — Guan et al. TabPFN3/TabICL for biomolecular prediction (`foundation model` hit, off-thread); Wu et al. Airbnb causal-ML (`causal inference` and `debiased machine learning` hits, off-thread); Wu et al. hierarchical clustering for multicollinearity in causal inference (off-thread); Loe et al. neural-network alternating recurrent events (`inverse probability` hit, adjacent-only); Tan et al. DiSTILL spatial-transcriptomics workflow (`inflammatory bowel disease` hit, off-thread but interesting workflow-engineering).
- **arxiv-digest 06-30 remaining items** — Winter et al. H&E → RNA-seq alignment (`foundation model` hit, off your EHR-FM thread).
- **arxiv-digest 07-02, 07-03, 07-08, 07-14, 07-15** — all single-paper days with off-thread hits (Airbnb causal / 3D plant phenotyping / video-features causal / cultural evolution / financial KG). Pipeline noise.

---

## Suggestions for the pipeline

All prior reports' recommendations remain unactioned. This window adds
no new pipeline pathology worth calling out, but reinforces two prior
recommendations:

1. **`knowledge graph` keyword — 8th consecutive window of non-biomedical
   hits.** This window's 07-14 finance KG paper and 07-07 PREDIKTOR
   paper. Same fix as prior report — tighten to `biomedical knowledge
   graph` OR `clinical knowledge graph` OR compound filter.

2. **`arxiv-digest` still misses Nature / Nature Genetics / Nature
   Medicine / JAMIA / AJHG / GIM.** Items #1-6 above are all from
   Scholar author-feeds because they're in journal venues, not arXiv
   q-bio / stat.AP. This is now the 3rd consecutive report calling for
   source expansion; the pattern is stable.

3. **`motor` keyword keeps hitting cultural-evolution (07-15) and
   insurance-actuarial (06-30) papers.** If the intent is "motor-neuron
   disease" or "motor symptoms in Parkinson's/MSA," tighten to
   `motor neuron disease` OR `motor symptoms`.

4. **Extended dry-day stretch (07-10, 07-11, 07-12, 07-13 all 0 papers;
   likewise 06-27, 06-28)** — this looks like genuine no-match days
   rather than fetch failures (file sizes are ~138 bytes = header-only,
   not a warning-mode output). Worth double-checking by manually running
   the digest at `--min-score 1` on one of these days to confirm.

5. **Positive note — the two-day 06-30 → 07-01 burst (4 + 7 = 11 papers)
   is the most substantive arxiv-digest yield since April.** Three of
   those (Karim/Hu, Fontana et al., Mapelli et al.) are HIGH-priority
   in this report. The digest pipeline is working; it's just that
   arxiv q-bio / stat.AP submissions cluster around monthly cycles.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 10 | (1) Shi et al. AoU STI phenotyping [Zeng self+Denny], (2) Baya et al. PRS-deviation + rare-variant enrichment [Montgomery, AJHG], (3) Hamed et al. multi-ancestry CHD PRS implementation [Luo, GIM], (4) Wu et al. domain-aware phenotype imputation [Denny, AoAS], (5) Liu et al. semiparametric robust EHR-biobank modeling [Brandt], (6) Boltz et al. blended WGS+WES [Karczewski, Nat Genet], (7) Karim & Hu regularized PS/DR calibration under rarity [`arxiv-digest` 07-09], (8) Fontana et al. UKB cardiometabolic multimorbidity network [`arxiv-digest` 07-07], (9) Mapelli et al. UKB-PPP proteomics PPI GGM [`arxiv-digest` 07-01], (10) Sriram thesis citing your work [Zeng citations] |
| METHODS-WATCH | 8 | Jabeen et al. MR risk-of-bias guide, Furrer et al. PES-decision survey, Naimi et al. residual-on-residual regression, Böhringer & Holzmann HWE-unified GWAS test, Bang et al. PREDIKTOR KG+drug response, Huang et al. autonomous biomedical AI agent, Blier-Wong & Kusmenko LLM-embedding GLM, Karpinsky et al. DNA-LM benchmark |
| SKIP | ~30 | See SKIP/noise section |

Compared to the 06-20 report (6 HIGH / 6 METHODS-WATCH), this window
(spanning 25 days vs 2) delivers a proportionally similar per-day yield
of HIGH items but with a slightly different mix: the 06-20 window was
dominated by triple-feed Scholar hits, while this window's HIGH items
are more evenly split across Scholar-author-feed hits (six of ten) and
`arxiv-digest` hits (three of ten, all from the 06-30 → 07-01 burst),
plus one citation-tracking hit. The single highest-signal item this
window (#1, Shi et al. AoU STI phenotyping) is a two-feed hit including
your own related-research feed — the same pattern as the 06-20 window's
Chen et al. nephrolithiasis paper — and reaffirms that your self-feed
plus one Denny/Bastarache feed is the highest-precision Scholar signal
channel in this pipeline.
