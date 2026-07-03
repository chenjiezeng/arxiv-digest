# Research digest report — 2026-07-03

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-03** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 07-03 | Two large batches (07-01 06:15Z, 07-02 15:04Z) plus daily keyword-alert emails. ≈45+ author/keyword feeds sampled: Chenjie Zeng self-feed (citation + related-research), Bastarache (articles + related + citations), Karczewski, Denny, Hripcsak, Yang, Pritchard, Montgomery (new-articles hit for the Marderstein noncoding paper), Szolovits, Callahan, Zitnik, Natarajan, Luo, Chute, Kastner, Patrick Ryan, Vivek Natarajan, Miguel Hernán. |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-03 | **13 daily runs, 12 papers surfaced across 8 non-empty days** (06-23: 2 papers; 06-25: 2; 06-26: 1; 06-30: 4; 07-01: 7 [3 previously surfaced]; 07-02: 1; 07-03: 1; other days empty or suppressed as previously seen). **06-24 had a 3/4-category fetch failure** (repeat of the pattern flagged in the 06-20 report — see pipeline note below). |
| NCBI My-NCBI "What's new" (UK Biobank / All of Us / drug repurposing) | daily | Aggregate digests received every day since 06-21; not individually triaged (aggregate volume). |
| medRxiv / bioRxiv subject-collection alerts | daily | Aggregate digests received every day since 06-21; not individually triaged (aggregate volume). |
| alphaXiv weekly digest (06-24) | weekly | Announcement of "autoresearch" URL rewriting for arXiv papers — infrastructure, not a paper. Logged and ignored. |

> ⚠️ **arxiv-digest 06-24 had a 3-of-4-category fetch failure** — same
> pattern flagged after 06-20. `q-bio.GN`, `q-bio.PE`, and `stat.AP` all
> failed to fetch; only `q-bio.QM` succeeded, and it had no matches. Since
> the 06-20 report the pipeline has produced non-empty output on 06-23,
> 06-25, 06-26, 06-30, 07-01, 07-02, and 07-03, so this appears to be an
> intermittent rate-limit issue rather than a persistent break. If it
> repeats within the next two windows, the mitigations from the 06-20
> report (jittered per-category retry-with-backoff, longer inter-category
> pause, or splitting the four categories into two workflow runs 90
> minutes apart) should be actioned. **See suggestions below.**

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. arxiv-digest entries include the full abstract, so
> those reads are somewhat deeper.

---

## Executive summary

- **A double-feed hit that includes your own self-citation feed.** Baker,
  Chen, Evans, Scartozzi et al. — *DRIVE v3: Command Line Application for
  Identity-by-Descent Haplotype Clustering in Large Biobank Scale Data*
  (*Genetic Epidemiology*, 2026). Surfaces simultaneously in (a) **your
  own 1-new-citation-to-articles-by-Chenjie-Zeng feed** and (b) the *1
  new citation to Lisa Bastarache* feed. The user's own *citations* feed
  is the highest-precision channel in this pipeline (only fires when a
  new paper actually cites your work); double-feed with Bastarache marks
  this as a Vanderbilt phecode-lineage tool paper that cites your and
  Lisa's IBD/phecode work. IBD-based haplotype clustering at biobank
  scale is directly on your genetic-epi + PheWAS-infrastructure threads.
  **Read first.**
- **The Marderstein noncoding-variant paper is now confirmed a
  Nature-briefing Montgomery *new article*.** Marderstein & Montgomery
  *Research briefing* — accompanying the Nature Genetics paper flagged
  in the 06-20 report — has now surfaced as a Montgomery **new-articles**
  hit (not just related-research), confirming Montgomery co-authorship
  and elevating this paper to *senior-author* signal on your variant-
  interpretation thread. Same paper, upgraded evidence. **HIGH,
  carry-forward priority.**
- **Padovani-Claudio, Lewis, Bastarache & He — optimal minimal phecode
  count for eye-disease cohort generation (IOVS, 2026).** Bastarache is
  a co-author, and this is a direct **methods paper on phecode-based
  cohort definition** — specifically, the sample-size / phecode-count
  threshold trade-off for GWAS-validated eye-disease cohorts. Directly
  serves the PheWAS/phecode-infrastructure thread and is written by the
  group that maintains the phecode catalog. **HIGH.**
- **Multi-ancestry + multi-trait PRS for lung cancer — quadruple-feed
  Nature Communications hit.** Zhang, Dai, Gu, Zhao, Christiani, Chen
  et al. — *Development and validation of a multiancestry and multitrait
  polygenic risk score for lung cancer* (*Nature Communications*, 2026).
  Surfaces in **four** independent feeds: 8 citations to Jian Yang, 4
  citations to Joshua C. Denny, Joshua C. Denny related-research, and
  Lisa Bastarache related-research. Quadruple-feed saturation across
  three of the most-relevant senior-author maps in the field. Directly
  on the genetic-epi / PRS / cross-ancestry thread; the multi-trait
  formulation (jointly modeling lung cancer plus correlated traits) is
  the methodologically novel piece. **HIGH.**
- **UKB-PPP proteomic PPI method paper surfaces on arxiv-digest at
  Score 3.** Mapelli, Massi, Cuccuru, Di Angelantonio & Ieva — *Prior-
  informed conditional Gaussian graphical models: an application to
  protein interaction network reconstruction* (arXiv 2606.31805, stat.AP,
  2026-06-30). Score 3, keywords `uk biobank + biobank + precision
  medicine`. Applied to n=49,129 UKB cardiometabolic proteomics with 366
  Olink proteins. Directly on the UKB-PPP / proteomic-composite-risk sub-
  thread flagged in the 06-20 report (Ding et al. Nat Med aging-
  proteomic). Second UKB-PPP-adjacent paper in two windows. **HIGH.**
- **Cystic-fibrosis-specific causal-inference method (throat-swab vs
  sputum misclassification of Pseudomonas / Staphylococcus) surfaces on
  arxiv-digest at Score 2.** Murali, Barnatchez, Hoppe, Wagner, Keller,
  Josey — *Causal Inference with Multiple Misclassified Exposures: A
  Control Variate-Adjusted Calibration Weighting Approach* (arXiv
  2606.23656, stat.ME, 2026-06-22). Applied to n=651 CF patients aged
  6-21. Throat swabs attenuate the estimated P. aeruginosa effect on
  ppFEV1 by ~69% relative to sputum. Directly on the CF thread AND on
  causal-inference/pharmacoepi, with a concrete clinical implication
  (under-treatment of P. aeruginosa if only swab data). **HIGH on the
  CF thread; HIGH on the misclassification-causal-inference methods
  thread.**
- **Cell-type-specific contextualisation of the human phenome — rare-
  disease phenotype-driven paper in Genome Medicine.** Schilder, Murphy,
  Dash, Zhang et al. — *Cell type-specific contextualisation of the human
  phenome: towards the systematic treatment of all rare diseases*
  (*Genome Medicine*, 2026, Bastarache related-research feed). Rare-
  disease + phenome (HPO-style) work in a lineage that Bastarache flags
  as related. Directly serves the rare-disease + HPO/ontology thread.
  **HIGH.**
- **Semaglutide and neovascular AMD — OHDSI network study, Ryan +
  Hripcsak new-articles double-hit.** Cai, Toy, Martin, Fan, Westlund,
  Tran et al. — *Semaglutide and Neovascular Age Related Macular
  Degeneration: An OHDSI Network Study* (*Ophthalmology & Visual
  Sciences*, 2026). Surfaces as **new article** in both Patrick Ryan and
  George Hripcsak feeds — both are OHDSI grandees, so a double-new-
  article hit is a strong indicator this is an OHDSI consortium paper.
  Semaglutide is a GLP-1 RA (tracked drug class); OHDSI network study
  is a federated design template for GLP-1 pharmacoepi. **HIGH on the
  GLP-1 pharmacoepi thread.**
- **Residual-on-residual regression for causal inference in nuMoM2b
  (preeclampsia).** Naimi, Jin, Yu, Parisi, Bodnar — *Residual-on-
  Residual Regression as a Tool for Effect Estimation in Observational
  Data* (arXiv 2606.30976, stat.ME, 2026-06-29). Score 2, keywords
  `inverse probability + causal inference`. Compares to AIPW and TMLE
  under positivity violations. Directly on the causal-inference /
  pharmacoepi methods thread; ROR is the newer alternative when TMLE
  becomes unstable. **METHODS-WATCH → HIGH-for-causal-methods.**
- **Federated tensor decomposition for multicellular immune programs
  (privacy-preserving).** Faes, van den Berg, Amir Haeri —
  *Privacy-preserving federated tensor decomposition of single-cell
  immune data: recovering multicellular programs across institutions*
  (arXiv 2606.24938, q-bio.GN, 2026-06-22, surfaced by arxiv-digest
  06-25). Score 1, keyword `cross-ancestry`. Federated method for cross-
  institution single-cell immune atlases with secure-aggregation
  membership-inference guarantees. Adjacent to the AoU/MVP/UKB federation
  question flagged in the 06-20 report (Kundu, Salvatore, Patel, Ohno-
  Machado). **METHODS-WATCH.**
- **arxiv-digest bulk 07-01: 7 surfaced (3 previously seen).** Notable
  in the non-priority set: three Airbnb-marketplace causal-inference
  papers by Yufei Wu et al. that hit `causal inference` /
  `debiased machine learning` / `causal inference` keywords with no
  clinical hook — carry-forward keyword-tightening note (`causal
  inference` needs a `clinical OR medical OR EHR OR biobank` co-filter).

Counts: **7 HIGH**, **4 METHODS-WATCH**, rest SKIP. Window (13 days)
delivers a slightly *lower* HIGH-per-day rate than 06-20 (which was 6
HIGH in 1 day), but the DRIVE v3 self-citation hit (item #1) is the
highest-precision surfacing pattern this pipeline can produce, and the
double CF (Murali) + UKB-PPP (Mapelli) arxiv-digest hits are the first
time in recent memory the `arxiv-digest` pipeline has surfaced two
clearly on-thread papers in a single window.

---

## HIGH priority — detailed reports

### 1. DRIVE v3: Command Line Application for Identity-by-Descent Haplotype Clustering in Large Biobank Scale Data
- **Authors / venue:** J.T. Baker, H.H. Chen, G.F. Evans, A.C. Scartozzi et al. — *Genetic Epidemiology*, 2026.
- **Surfaced by:** **Double-feed hit including your own citations feed** — (a) *1 new citation to articles by Chenjie Zeng* (**your own citation feed** — the highest-precision channel), (b) *1 new citation to articles by Lisa Bastarache*. Author list "Baker, Chen, Evans, Scartozzi" reads like a Vanderbilt / VGI-lineage authorship (Scartozzi is Vanderbilt).
- **Thread:** **PheWAS / phecode infrastructure** (Vanderbilt lineage) **+** **Genetic epidemiology / rare-variant discovery** (IBD-haplotype clustering is a primary tool for finding shared segments that harbor rare pathogenic variants — the same population-genetics primitive underlying rare-variant PheWAS designs) **+** **Biobank scale** (title explicitly says "Large Biobank Scale Data").
- **What it is:** DRIVE v3 is a command-line application for identity-by-descent (IBD) haplotype clustering at biobank scale. IBD clustering identifies groups of individuals sharing extended haplotypes inherited from a recent common ancestor — a primitive for rare-variant discovery, founder-effect analysis, cryptic-relatedness detection, and population-structure control. "v3" implies iterated tool development with a paper on the versioned release — typical for the VGI / phecode-catalog toolchain that Bastarache's lineage maintains.
- **Why it matters to you:** Four converging hits.
  (a) **Your own citations feed fired.** The paper cites something *you wrote*. Given the tool's IBD-focus and Bastarache co-citation, the most likely citations are (i) your APOL1 / kidney IBD-haplotype work, (ii) your BioVU-based rare-variant work, (iii) your phenomic-comparison paper, or (iv) *PheTK*. Any of these means a Vanderbilt-lineage biobank tool paper is treating your methods as prior art.
  (b) **The tool is directly usable in your workflows.** IBD clustering is a general-purpose primitive; if the CLI performance scales to AoU / MVP / UKB, you can drop it into any rare-variant PheWAS pipeline where cryptic relatedness or founder-population identification is a step.
  (c) **Double-feed with Bastarache confirms the phecode lineage.** DRIVE v3 was likely developed alongside phecode-adjacent tooling — the same shop that maintains PheWAS-Bioportal / PheTK / phecode catalog is a plausible source. This aligns tool provenance with your default toolchain.
  (d) **Biobank scale in the title.** Most IBD tools (Germline, iLASH, hap-IBD, Rapid) have documented scaling issues at UKB-and-larger scale; a *v3* release explicitly framed as "large biobank scale" suggests they've solved something engineering-wise.
- **Action:** **HIGH — read first.**
  (i) **Check the citation to you.** Highest-value context: which of your papers cited, in what section (methods / background / discussion)? That tells you which of your methodological threads is being adopted.
  (ii) **Note the IBD algorithm and its scaling curve.** Is it hap-IBD-based, HapNe-based, or novel? What's the wall-clock at 500k / 1M / 5M samples?
  (iii) **Note the downstream applications demonstrated.** If the paper shows a use-case in rare-variant discovery, founder-population identification, or APOL1 haplotype segmentation, that's a direct hook into your existing work.
  (iv) **Consider adopting** for AoU rare-variant PheWAS pipelines if the memory / wall-clock permits. `pip install`-able CLI + published v3 means low integration cost.

### 2. Determination and GWAS validation of optimal minimal phecode count for eye disease cohort generation
- **Authors / venue:** D.A. Padovani-Claudio, A. Lewis, L.A. Bastarache, J. He — *Investigative Ophthalmology & Visual Science* (IOVS), 2026.
- **Surfaced by:** *Lisa Bastarache — new articles* feed (Lisa is an **author**, not just related-research — highest-signal Bastarache-feed variant).
- **Thread:** **PheWAS / phecode infrastructure** (direct: this is a paper *on how to threshold phecode counts* — one of the central methodological questions for phecode-based cohort definition) **+** **EHR phenotyping** (cohort-generation method).
- **What it is:** Methods paper addressing the question "how many occurrences of a phecode does a patient need before we count them as a case?" A single phecode occurrence is noisy (rule-out billing, transient coding); two-or-more is the common default; three-or-more is stricter. This paper *validates* the choice by GWAS-power: they compute association statistics for eye-disease phecode cohorts under different minimum-count thresholds, and identify the threshold that maximizes GWAS-detectable signal. Bastarache is a senior co-author, so this is expected to become the phecode-catalog's official recommendation for the eye-disease specialty.
- **Why it matters to you:** Three reasons.
  (a) **The minimum-phecode-count question is a first-order methodological question in every PheWAS / phecode analysis you do.** You already choose 2+ occurrences (the current default) implicitly; this paper interrogates whether that choice is optimal, and gives an *empirical* justification tied to GWAS-replication signal.
  (b) **Bastarache authorship signals that the recommendation will be adopted upstream** — phecode-catalog defaults may shift as a result, and pipelines built on old defaults will silently disagree with pipelines built on the new ones. Worth catching now, before your next AoU / BioVU cohort-definition step.
  (c) **The eye-disease result may generalize to other specialty phecode families** — kidney (APOL1), CF respiratory-code family, IBD codes, CH-adjacent hematology codes. Padovani-Claudio's methodology (GWAS-power as validation) can be replicated on any specialty tree.
- **Action:** **HIGH.**
  (i) Read for the recommended minimum count for eye-disease phecodes (likely 2+ or 3+).
  (ii) Note whether the methodology (GWAS-power as validation) is presented as a *general* framework or a *specialty-specific* tuning; if the former, this is a *tool* you can port to your specialty families.
  (iii) Check whether the tuning changes for **EHR-linked biobanks** with different follow-up lengths — AoU (short follow-up, ~5 years median) will give different optima than BioVU (>20 years).
  (iv) Save as a citation for any phecode-cohort methods description in your next PheWAS write-up.

### 3. Development and validation of a multiancestry and multitrait polygenic risk score for lung cancer
- **Authors / venue:** Y. Zhang, J. Dai, P. Gu, Y. Zhao, D.C. Christiani, F. Chen et al. — *Nature Communications*, 2026.
- **Surfaced by:** **Quadruple-feed saturation** — (a) *8 new citations to articles by Jian Yang*, (b) *4 new citations to articles by Joshua C. Denny*, (c) *Joshua C. Denny — new related research*, (d) *Lisa Bastarache — new related research*. Four independent feeds firing on one paper is the same signal-density pattern flagged in the 06-20 report for the Chen et al. nephro PRS+PheWAS paper and the Sivarajkumar EHR-FM paper.
- **Thread:** **Genetic epidemiology / PRS** (PRS development + validation) **+** **cross-ancestry portability** (multi-ancestry design) **+** **multi-trait modeling** (jointly modeling correlated traits — a PRS-CS or PRS-CS-x extension into the multi-trait regime).
- **What it is:** Multi-ancestry + multi-trait PRS for lung cancer. Two axes of novelty: (i) *multi-ancestry* means the PRS is trained or calibrated across multiple ancestral populations (European, East Asian, likely African-American given the Christiani lineage), (ii) *multi-trait* means the PRS jointly models lung cancer with correlated traits (smoking behavior, FEV1, COPD, other cancers) rather than the univariate default. Christiani is Harvard-Boston lung-cancer epi lineage; Dai / Chen are Nanjing Medical / Chinese GWAS lineage. The pairing means this uses both Western and Chinese cohorts.
- **Why it matters to you:** Three reasons.
  (a) **Multi-ancestry PRS is a core thread on your INTERESTS file** ("cross / trans-ancestry portability"). Lung cancer is not a tracked disease, but the method template — multi-ancestry + multi-trait joint modeling — transfers to any disease where you have Western + East Asian summary statistics. This is the methods reference for that pattern in 2026 H2.
  (b) **Multi-trait modeling is the direction PRS is going.** Univariate PRS is a solved problem; joint-modeling with correlated traits (e.g., PRS-CS-multi, MTAG-informed PRS) improves calibration and portability. A Nature Communications paper with a validated multi-trait design is the default citation for arguing for that design in your next AoU / MVP work.
  (c) **Quadruple-feed firing.** Denny + Bastarache related-research + Jian Yang citations + Denny citations means the paper is *simultaneously* being flagged as citing eMERGE-lineage work (Denny), the phecode literature (Bastarache), and Chinese GWAS lineage (Yang). That's a heavy signal-density; the paper is likely to become a top-15 citation in the multi-ancestry PRS literature by end of 2026.
- **Action:** **HIGH.**
  (i) Read for the multi-ancestry method — is it PRS-CSx, MEGA-PRS, PolyPred+, or a new estimator? The estimator choice is the entire methodological question.
  (ii) Note the multi-trait formulation — MTAG-style meta-analysis with genetic-correlation weights, or a joint likelihood?
  (iii) Check the validation cohorts — UK Biobank + China Kadoorie Biobank + MVP would be the strongest combination; UKB + BioVU would be typical Western-only; UKB + Taiwan Biobank would signal an East-Asian-specific validation.
  (iv) Save as a template for any future multi-ancestry composite-PRS write-up. If the paper releases the PRS on the PGS Catalog, it's a benchmark-comparable model for other cancers via cross-ancestry-portable substitution.

### 4. Prior-informed conditional Gaussian graphical models applied to UK Biobank cardiometabolic proteomics (n=49,129)
- **Authors / venue:** A. Mapelli, M.C. Massi, G. Cuccuru, E. Di Angelantonio, F. Ieva — arXiv 2606.31805, stat.AP, 2026-06-30 (surfaced by `arxiv-digest` 07-01 at Score 3).
- **Surfaced by:** `arxiv-digest` 07-01, keyword hits `uk biobank + biobank + precision medicine`. Highest-scoring `arxiv-digest` paper this window.
- **Thread:** **EHR-linked biobank (UK Biobank)** **+** **Proteomic composite-risk sub-thread** (paired with the Ding et al. Nat Med aging-proteomic paper from the 06-20 report and the UKB-PPP infrastructure question) **+** **ML for precision health** (T2D biomarker discovery).
- **What it is:** Gaussian graphical model (GGM) for protein-protein interaction (PPI) network estimation, with two extensions over the standard GGM: (i) *prior-informed* — canonical PPI databases (STRING, IntAct) inform the sparsity penalty, so known interactions are less penalized while novel edges remain data-driven; (ii) *conditional* — the network depends on covariates (age, sex, disease status), enabling *personalized* subnetwork estimation. Applied to UK Biobank cardiometabolic proteomics (n=49,129, 366 Olink proteins). Identifies 34 network-central T2D biomarker candidates (some invisible to differential-expression analysis) and 6 biologically coherent protein communities.
- **Why it matters to you:** Three reasons.
  (a) **UKB-PPP infrastructure is on-thread.** Your INTERESTS file flags proteomic-composite-risk modeling (PRS + proteomic layer) as a sub-thread — see the 06-20 Ding et al. Nat Med report. This paper uses the same UKB-PPP cardiometabolic subset (n=~49k, 366 proteins) and provides a *network-based* alternative to the univariate differential-expression baseline. The "biomarkers only detectable through connectivity" claim is the most interesting piece — it means the PPI-network view surfaces candidates that univariate proteomic-PRS misses.
  (b) **Prior-informed + covariate-dependent networks fit the AoU / MVP framing.** As proteomic data lands in AoU sub-cohorts (or MVP's proteomic pilots), the same method (prior from STRING + covariate-dependency on ancestry, sex, comorbidity structure) is directly reusable. Code is released at `github.com/AlessiaMapelli/Prior-informed-conditional-GGMs`.
  (c) **T2D is a tracked disease.** T2D pharmacoepi (SGLT2i, GLP-1 RA) is on your active drug-class thread. A proteomic-network view of T2D that identifies novel connectivity biomarkers is directly usable as a covariate layer in TTE for these drug classes.
- **Action:** **HIGH.**
  (i) Read for the prior-weight tuning — how strong is the STRING/IntAct prior relative to the data-driven penalty? Sensitivity of the discovered PPI-communities to prior weight is the key robustness test.
  (ii) Note the covariate-dependency parameterization — additive to the mean-vector, or entering the precision matrix directly? Precision-matrix-level covariate effects are the more expressive (and more novel) framing.
  (iii) Grab the 34 candidate biomarkers and check overlap with the Ding et al. Nat Med aging-proteomic signature. Overlap = biomarkers that reflect *both* T2D-network centrality and organ-specific aging = strongest composite-risk candidates.
  (iv) Test-drive the code on any proteomic-adjacent PheWAS you have queued — it's plug-in-able where standard glasso would go.

### 5. Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach — applied to n=651 cystic fibrosis patients
- **Authors / venue:** N. Murali, K. Barnatchez, J.E. Hoppe, B.D. Wagner, K.P. Keller, K.P. Josey — arXiv 2606.23656, stat.ME, 2026-06-22 (surfaced by `arxiv-digest` 06-23 at Score 2).
- **Surfaced by:** `arxiv-digest` 06-23, keyword hits `causal inference + cystic fibrosis`. Score 2, and *not* an incidental keyword hit — the CF cohort is the primary application.
- **Thread:** **Cystic fibrosis / CFTR** disease thread (direct — n=651 CF patients ages 6-21) **+** **Causal inference / pharmacoepi** (exposure-misclassification methods) **+** **EHR phenotyping** (measurement-error framing generalizes to any imperfect-code phenotype).
- **What it is:** Method + empirical CF application. Method: calibration weighting + control-variate adjustment for causal inference when *multiple* binary exposures are misclassified simultaneously — a genuinely novel setting (most misclassification-causal-inference is single-exposure). The calibration approach treats misclassification as missing data and achieves consistency *without* modeling the misclassification mechanism explicitly. Control-variate adjustment uses error-prone observations to reduce variance while preserving consistency. Double-robustness inherited from AIPW-like construction. Application: CF cohort where the exposures are throat-swab-detected P. aeruginosa and S. aureus (imperfect sensitivity + specificity relative to sputum culture, the gold standard). Result: throat-swab-based causal estimates attenuate the effect of P. aeruginosa on % predicted FEV1 by ≈**69%** relative to sputum-based estimates (-2.67 vs. -8.52 percentage points; 95% CI for sputum: -13.40, -3.63). Clinical implication: relying on throat swabs may lead to *under-treatment* of P. aeruginosa infections.
- **Why it matters to you:** Four reasons.
  (a) **Cystic fibrosis is a tracked disease.** CF pharmacoepi (Trikafta / ivacaftor + long-term outcomes) is on your active thread. The paper is directly usable as a citation for any CF real-world-evidence write-up where lab-detected exposures are imperfect.
  (b) **The 69% attenuation result is a huge effect.** Under-treatment of Pseudomonas is a policy-relevant clinical finding, not just a methods paper. Any CFTR-modulator work that models P. aeruginosa exposure as a mediator or confounder needs to account for this level of misclassification bias.
  (c) **The method generalizes beyond CF.** Multiple-misclassified-exposure causal inference is the setup for any EHR-based drug/disease exposure where ICD or lab codes are imperfect proxies for underlying disease — which is *most* pharmacoepi. This is a portable methodological tool.
  (d) **Structural ceiling on efficiency gains.** The paper's characterization that joint correct classification of both exposures caps the variance-reduction achievable is a subtle but important point — it prevents naive over-optimism about control-variate gains in multi-exposure settings.
- **Action:** **HIGH.**
  (i) Read for the calibration-weighting estimator formulation. Is it a Horvitz-Thompson-style weighted average with a validation-subset calibration term, or a fully-doubly-robust construction?
  (ii) Note the CFF Patient Registry linkage — if the n=651 comes from CFF Registry data with gold-standard sputum sub-sampling, this is a template for CFF-Registry-based methods work you might want to replicate.
  (iii) Save the -69% attenuation number as a citation for the "throat-swab-underestimates" argument in any CFTR-modulator write-up.
  (iv) Consider applying the method to any of your own exposure-misclassification problems — e.g., APOL1 kidney-disease exposure ascertained from ICD vs. lab-confirmed proteinuria, or ClinVar-annotated variant status when the underlying evidence is heterogeneous.

### 6. Cell type-specific contextualisation of the human phenome: towards the systematic treatment of all rare diseases
- **Authors / venue:** B.M. Schilder, K.B. Murphy, H. Dash, Y. Zhang et al. — *Genome Medicine*, 2026.
- **Surfaced by:** *Lisa Bastarache — new related research* feed.
- **Thread:** **Rare disease** (title explicitly: "systematic treatment of all rare diseases") **+** **Knowledge graphs & ontologies** (HPO / phenome contextualization) **+** **EHR phenotyping** (cell-type-specific phenome mapping is a phenotype-refinement primitive).
- **What it is:** From the surfaced snippet: cell-type-specific contextualization of the human phenome, framed as a rare-disease systematic-treatment tool. The likely design is a mapping from HPO phenotypes to cell-type-of-origin (via scRNA-seq atlases or CellxGene), enabling per-phenotype cell-type prioritization for drug-target discovery. Genome Medicine venue signals empirical validation on rare-disease diagnostic cohorts. The Bastarache related-research hit indicates it likely cites the phecode literature or HPO-phecode mapping work.
- **Why it matters to you:** Three reasons.
  (a) **Rare disease is a tracked thread.** Any HPO-driven rare-disease diagnostic framework that adds cell-type-of-origin as a phenotype coordinate is a candidate for adoption in rare-disease phenotyping pipelines you might set up in AoU (RaDx-adjacent) or MVP.
  (b) **The drug-repurposing hook is explicit** ("systematic treatment"). Cell-type-of-origin maps directly onto candidate drug targets (via GTEx / DrugCentral / L1000-style perturbation databases). If the paper releases per-HPO-term cell-type scores, that becomes a joinable annotation for rare-disease drug-repurposing scoring.
  (c) **Bastarache-related surfacing suggests a HPO ↔ phecode bridge** may be part of the tooling — worth checking whether HPO terms are mapped to phecodes for EHR-linkage purposes.
- **Action:** **HIGH.**
  (i) Check whether cell-type scores are released per HPO term or aggregated by disease. Per-term release is more useful for downstream integration.
  (ii) Check the scRNA-seq atlases used (Tabula Sapiens? CellxGene? HuBMAP?). Atlas choice bounds the cell-type resolution.
  (iii) Note whether any EHR-side validation is included — if HPO-derived cell-type scores stratify EHR-observed rare-disease patients by outcome, that's a much stronger claim.
  (iv) Save for rare-disease phenotyping work and for HPO-driven drug-repurposing lookups.

### 7. Semaglutide and Neovascular Age-Related Macular Degeneration: An OHDSI Network Study
- **Authors / venue:** C.X. Cai, B.C. Toy, B. Martin, R. Fan, E. Westlund, D. Tran et al. — *Ophthalmology & Visual Sciences*, 2026.
- **Surfaced by:** **Double new-articles hit** — (a) *Patrick Ryan — new articles*, (b) *George Hripcsak — new articles*. Both are OHDSI grandees; double-new-article hit signals both are co-authors, i.e., this is a canonical OHDSI network study.
- **Thread:** **Causal inference & pharmacoepi** (safety-signal detection for GLP-1 RA) **+** **GLP-1 RAs** (active tracked drug class) **+** **EHR-linked federated pharmacoepi** (OHDSI network study = multi-site federated design).
- **What it is:** OHDSI network study assessing whether semaglutide is associated with incident neovascular AMD. Semaglutide is the GLP-1 RA of the moment; ocular safety signals (early reports of NAION, questions about wet AMD) have been the pharmacovigilance concern. An OHDSI network study means the analysis runs against multiple OMOP-CDM instances and aggregates estimates — the field-standard federated design for RWE-based safety signals. Ryan + Hripcsak double-authorship marks this as a canonical OHDSI paper (probably run through OHDSI's LEGEND framework or its safety-signal analogue).
- **Why it matters to you:** Three reasons.
  (a) **GLP-1 RA pharmacoepi is a tracked drug class.** Any OHDSI-scale safety-signal or effectiveness study of semaglutide is directly on-thread. The AMD outcome is off your primary metabolic focus but is a rare/serious adverse-event outcome that pharmacoepi TTE designs need to interrogate.
  (b) **Template value for federated design.** The design — OHDSI network, likely LEGEND-adjacent — is a template for any future AoU / MVP / OHDSI federated GLP-1 or SGLT2i study. Read specifically for cohort-definition (new-user cohort? active-comparator?), outcome definition, and effect-estimation stack (Cox with PS-stratification is the OHDSI default).
  (c) **Ryan + Hripcsak co-authorship** signals this will become the OHDSI reference-implementation for GLP-1-adjacent ocular-safety analyses.
- **Action:** **HIGH.**
  (i) Read for the cohort design — new-user active-comparator (vs. DPP-4i? vs. SGLT2i? vs. sulfonylurea?), and whether the negative-control-outcome calibration is applied.
  (ii) Check the effect estimate — hazard ratio, direction, and calibration-adjusted CI. Note whether the paper concludes null / positive / negative signal for AMD.
  (iii) Note the data partners — HealthVerity, HIRA-Korea, IQVIA, and academic OMOP sites are the typical OHDSI network partners.
  (iv) Save as an OHDSI reference-design when you next scope a GLP-1 or SGLT2i federated pharmacoepi study.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Residual-on-Residual Regression as a Tool for Effect Estimation in Observational Data** — A.I. Naimi, Q. Jin, Y.-H. Yu, S.M. Parisi, L.M. Bodnar — arXiv 2606.30976, stat.ME, 2026-06-29 (surfaced by `arxiv-digest` 07-01, Score 2). Estimator for partially-linear-model effects: fit ML-based outcome and exposure models, then OLS regress the residuals. Applied to nuMoM2b (n=7,923) preeclampsia vs. vegetable intake density; concordant with AIPW and TMLE, but *outperforms* both under positivity violations when the partially-linear-model assumption holds. **Directly on your causal-inference / pharmacoepi methods thread.** ROR is the simpler-and-more-stable alternative to AIPW/TMLE for effect estimation when the exposure effect is roughly constant across covariate profiles; the arguments for using it in nutritional epi transfer to pharmacoepi where positivity is fragile (e.g., new-user cohorts with narrow eligibility). **METHODS-WATCH → borderline HIGH** — save for any TTE work where TMLE has been unstable.

- **Privacy-preserving federated tensor decomposition of single-cell immune data** — A. Faes, S.M. van den Berg, M. Amir Haeri — arXiv 2606.24938, q-bio.GN, 2026-06-22 (surfaced by `arxiv-digest` 06-25). Cross-institution / cross-ancestry federated recovery of multicellular immune programs from single-cell data. Applied to 261-donor SLE atlas, 3 real COVID-19 sites, and an ILD atlas. Secure aggregation reduces membership-inference AUC from 0.91 to 0.61. Off-thread substantively (single-cell immunology), but **methodologically directly relevant** to the Kundu, Salvatore, Patel, Ohno-Machado federated-multi-site-EHR paper from the 06-20 report. The tensor-decomposition primitive with federated global-mean centering is a design idea that transfers to any federated multi-site EHR analysis where the sites see different cell-types / phenotypes / measurement modalities. **METHODS-WATCH.**

- **CPAgents: Agentic Composite Phenotype Generation for Cardiac Disease Association** — Z. Li, W. Zhao, K. Yu, W. Zhang, P.M. Matthews, W. Bai et al. — arXiv preprint, 2026 (surfaced by *"phenome wide association studies" — new results* feed). Agent-based composite phenotype generation for cardiac PheWAS — LLM agents propose and refine cardiac phenotype definitions, presumably validated against outcomes. Matthews / Bai are Imperial College imaging-genomics lineage. **METHODS-WATCH:** the agentic-phenotype-generation pattern is worth tracking as it directly overlaps with your interest in LLM-assisted phecode / phenotype development, but the paper is preprint-only and not yet Bastarache-lineage-adjacent.

- **DIMAS-OMOP: A Deliberative Intelligence-Based Multi-Agent System for Chinese Medical Text Standardization toward OMOP** — H. Lv, X. Wang, L. Wang, L. Li — Workshop paper, 2026 (surfaced by *Patrick Ryan — new related research*). Multi-agent LLM system for mapping Chinese clinical text to OMOP-CDM standard vocabularies. **METHODS-WATCH:** interesting as an OMOP-vocabulary bridge for Chinese biobank data (potential future AoU-analogous data source), but off-thread for daily work.

- **An empirical Bayes framework for burden and dispersion association tests helps prioritize rare variants associated with Alzheimer's disease** — A. Das, C.M. Lakhani, V.M. Mazeeva, T. Raj, D.A. Knowles — 2026 (surfaced by *Stephen B. Montgomery — new related research*). Empirical-Bayes prior on rare-variant burden and dispersion tests, applied to AD. Off-disease (not your CF/APOL1/CH threads), but **methodologically on-thread** for rare-variant PheWAS: EB priors that borrow strength across genes or across ancestries are a design pattern that transfers to APOL1 kidney-disease burden work, CFTR variant burden work, and DNMT3A / TET2 clonal-hematopoiesis burden work. **METHODS-WATCH.**

- **Novel Alzheimer's disease-associated variants and genetic interactions identified from UK Biobank whole-exome sequencing data using IBI-DT** — J. Ren, R. Yin, J. Zhao, J. Liu — Scientific Reports, 2026 (surfaced by *Konrad Karczewski — new related research*). Iterative-Bayesian-Interaction Decision Tree method for gene-gene interaction detection in UKB WES for AD. Off-thread substantively (AD, epistasis, not one of your active disease threads), but the interaction-detection design in UKB WES is a template for CFTR-modifier discovery or APOL1-modifier discovery in AoU / MVP. **METHODS-WATCH, borderline SKIP.**

- **Research briefing (Marderstein & Montgomery) — carry-forward from 06-20.** The Marderstein noncoding-variant paper (Nature Genetics) flagged in the 06-20 report now has a **Nature Research Briefing** by Marderstein & Montgomery surfaced under *Stephen B. Montgomery — new articles*. This confirms Montgomery co-authorship (senior-author signal, not just related-research signal) and the briefing itself is a shorter, more accessible read than the full Nat Genet paper. Read the briefing first if the full paper is queued but unread. **Priority carry-forward: HIGH.**

---

## SKIP / noise (logged, no action)

- **Foundation-model + EHR keyword feed** — three feed hits in the window (07-01 & 07-02 batches) all surfaced generic FL / privacy-preserving oncology-imaging papers with no clinical-EHR-FM hook. Keyword is broad; recall drift is manageable, but consider tightening to require a co-occurring `clinical` OR `phenotyping` OR `MEDS` OR `MIMIC` OR `AoU` OR `UKB` term.
- **UK Biobank keyword feed** — most hits are diet / lifestyle / imaging-composition papers that use UKB as a large cohort but are off your genetic-epi + EHR-phenotyping threads. Aggregate rather than triage.
- **Marketplace / Airbnb causal-inference papers by Yufei Wu et al.** (three papers, `arxiv-digest` 06-30, 07-01, 07-02, all Score 1) — off-thread pharmacology / clinical. Keyword-tightening candidate: `causal inference` should probably require a co-occurring clinical / biomedical / EHR term.
- **Semantic insurance pricing with LLMs (French motor third-party liability)** — Blier-Wong & Kusmenko, `arxiv-digest` 06-30. The `motor` keyword hit is spurious (motor insurance, not motor neurons or motor learning). Same class as the openhdemg synaptic-input paper on 06-23 (motor units). **`motor` keyword is producing consistent noise** — either tighten to `motor neuron` / `motor unit` / `motor learning`, or remove entirely if it's not tied to an active thread.
- **DNA Language Models: Pre-Training Assessment (Karpinsky, Mozziconacci, Delcey)** — `arxiv-digest` 06-30, Score 1 (`foundation model`). Off-thread — DNA-LM benchmarking, not clinical-EHR-FM.
- **Data-Efficient Multimodal Alignment for Histopathology-Molecular Prediction (Winter et al.)** — `arxiv-digest` 06-30, Score 1 (`foundation model`). Histopathology + RNA-seq, off your EHR-FM thread.
- **DiSTILL: Hybrid Cloud-HPC Workflow System for Spatial Transcriptomics (IBD application)** — `arxiv-digest` 07-01, Score 1 (`inflammatory bowel disease`). Workflow-systems paper that uses IBD ST as the demo pipeline; the paper is *not* an IBD-genetics or IBD-EHR paper — the `inflammatory bowel disease` keyword hit is incidental. **SKIP.** (Keyword tuning: `IBD` combined with `spatial transcriptomics` or `workflow` triggers off-thread hits — but at aggregate volume this is low-cost.)
- **KG-TRACE: Neuro-Symbolic AMR Prediction (Garg et al.)** — `arxiv-digest` 06-26, Score 1 (`knowledge graph`). WHO mutation KG grounded prediction of M. tuberculosis antimicrobial resistance. Off-thread (AMR bacteriology, not clinical KG); **8th consecutive window of `knowledge graph` keyword non-biomedical-clinical noise** — carry-forward tightening recommendation from the 06-20 report is now urgent.
- **Are Tabular Foundation Models Robust to Query Distribution Shifts in Microbiome Data? (Perciballi et al.)** — `arxiv-digest` 06-25, Score 1 (`foundation model`). Off-thread — microbiome + TFM robustness, no clinical hook.
- **Can Tabular In-Context Learners Generalize to Biomolecular Property Prediction? (Guan et al.)** — `arxiv-digest` 07-01, Score 1 (`foundation model`). Off-thread — protein-fitness and small-molecule ADMET, not clinical-FM.
- **The Turning Point of 3D Plant Phenotyping (Jia et al.)** — `arxiv-digest` 07-03, Score 1 (`foundation model`). Plant phenotyping — off-thread.
- **Estimating common synaptic inputs to spinal motor neurons via openhdemg (Cabral et al.)** — `arxiv-digest` 06-23, Score 1 (`motor`). Off-thread. **`motor` keyword noise, second instance this window.**
- **Evaluating HWE and Association in GWAS: A Unified Procedure (Böhringer & Holzmann)** — `arxiv-digest` 06-30, Score 1 (`fine mapping`). Statistical methods for combining HWE and association tests in GWAS. **Adjacent-to-thread** but old-school methods paper; the `fine mapping` keyword hit is via the improvement-of-fine-mapping-downstream framing. **SKIP-leaning METHODS-WATCH** — cite if you need a HWE-adjusted p-value method.
- **Scholar author-feed noise** — Yuan Luo, Christopher Chute, Peter Szolovits, Daniel Kastner citation feeds all surfaced generic LLM / VLM / ML papers with no clinical hook (VLM textual-prior benchmarks, LLM backdoor attribution, on-policy self-distillation for diffusion LMs, RiskLab for multi-agent LLM risks). These are citation-graph leaks — the cited authors are in the LLM/ML space too, so their `new citations` surfaces every LLM paper that references any of their prior work.
- **Nishiyama & Nishiura: SARS-CoV-2 infections averted by COVID-19 vaccination in Japan** (Chute related-research) — off-thread, epidemiologic-modeling paper.
- **Patient-Reported Experiences with Patient Portals (Hripcsak related-research)** — off-thread health-informatics HCI paper.
- **A novel cystic fibrosis-mimetic Pseudomonas auxotrophic vaccine (Sereme et al., Patrick Ryan related-research)** — surfaces because of "cystic fibrosis" title match, but is a **basic-immunology vaccine paper**, not clinical CF pharmacoepi. **SKIP** despite the CF keyword hit — the paper is about a Pseudomonas vaccine that *models* CF-like environments, not CF patient outcomes.
- **Clonal Hematopoiesis and Type 2 Diabetes: A Narrative Review (Liu, Liu, Gurung, Lim, Dorajoo)** — `intitle:clonal hematopoiesis` feed. Review, not primary literature. **Log as a candidate short reference** if you're working on the CHIP-metabolism intersection; otherwise SKIP.
- **Padovani-Claudio / Bastarache eye-disease phecode article was double-cited** — appears both as "new articles" (item HIGH #2 above) and as a "1 new citation to articles by Chenjie Zeng" candidate — but is different from the DRIVE v3 paper. Cross-reference check: your citations feed *only* surfaced DRIVE v3, so the phecode-eye-disease paper does not cite you.

---

## Suggestions for the pipeline

Carry-forward from the 06-20 report + two new items:

1. **arxiv-digest 06-24 had another 3-of-4-category fetch failure** — repeat of 06-20. If the pipeline fires again with `q-bio.GN / q-bio.PE / stat.AP` failing while `q-bio.QM` succeeds, the fix set from the 06-20 report should be actioned: (a) jittered per-category retry-with-backoff, (b) further-doubling the inter-category pause to 30s, or (c) splitting the four categories into two workflow runs 90 minutes apart. **New addition:** the digest should emit a distinct exit status (or a machine-parseable "PARTIAL_FETCH" line) when N/4 categories fail — currently the 06-24 output looks similar to a genuine 0-paper day and requires reading the WARNING banner to distinguish.

2. **`knowledge graph` keyword non-biomedical noise — now 8th consecutive window.** This is the highest-priority pipeline change. Rewrite: `knowledge graph` → `(knowledge graph OR biomedical KG OR clinical KG) AND (medical OR biomedical OR clinical OR EHR OR phenotype OR drug OR disease OR patient OR gene OR variant)`. Nothing on-thread has been surfaced by the current keyword in the last 8 windows.

3. **`motor` keyword produces consistent off-thread noise.** Two off-thread hits this window alone (motor units, motor insurance). If `motor` is tied to an active thread — motor-neuron disease? — it needs the disease-specific compound form (`motor neuron` or `motor unit`); if it's not tied to an active thread, remove.

4. **`causal inference` keyword needs a clinical/biomedical co-filter.** Three off-thread Airbnb marketplace hits this window. Suggested: `causal inference AND (medical OR clinical OR EHR OR biobank OR patient OR disease OR drug OR treatment OR trial OR cohort OR epidemiology)`.

5. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds** (carry-forward from 06-20, unaddressed). The Naimi ROR paper (stat.ME) and the Murali CF-causal paper (stat.ME) both were flagged this window by `arxiv-digest` because we're already scraping stat.ME implicitly through Cross-list detection — but the recall of `stat.ME` remains inconsistent. Explicit inclusion would remove the ambiguity. medRxiv / bioRxiv remain unscraped.

6. **Add `PRS stability` / `polygenic score stability` / `PRS robustness` / `polygenic tails` as keywords** (carry-forward, unaddressed). The 06-20 report's Souaiaia-Nature tails paper remains a strong signal that this sub-thread needs direct keyword coverage; nothing new this window but the recommendation stands.

7. **Add `proteomic signature` / `UKB-PPP` / `aging clock` / `organ-specific aging` keywords** (carry-forward from 06-20). This window's Mapelli UKB-PPP paper (item HIGH #4) was caught by `uk biobank + biobank + precision medicine` at Score 3 — the direct UKB-PPP tag would catch narrower on-thread proteomic-network papers with more precision.

8. **Add `noncoding variant interpretation` / `MPRA` / `regulatory variant effect` keywords** (carry-forward from 06-20). The Marderstein Nature Genetics paper continued surfacing this window as a briefing — the sub-thread is coherent.

9. **Continue tracking your own citations feed as the single highest-precision channel** (carry-forward from 06-20). The DRIVE v3 paper (item HIGH #1) surfaced *only* via that feed + Bastarache; the pattern remains gold-standard for triage.

10. **New:** Add `Vanderbilt` / `BioVU` / `PheTK` / `phecode catalog` as author-adjacent keyword filters. The DRIVE v3 hit is a Vanderbilt-lineage tool paper; if the pipeline can catch Vanderbilt-lineage tool releases directly, the same class of paper doesn't need to wait for the Bastarache related-research feed to fire.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 7 | (1) Baker et al. DRIVE v3 IBD haplotype CLI [self-citation + Bastarache-citation double-feed], (2) Padovani-Claudio, Lewis, Bastarache, He phecode-count for eye disease [Bastarache-authored, IOVS], (3) Zhang et al. multi-ancestry multi-trait lung cancer PRS [quadruple feed, Nat Commun], (4) Mapelli et al. prior-informed conditional GGM on UKB-PPP T2D proteomics [arxiv-digest Score 3], (5) Murali et al. misclassified-exposure causal inference in CF [arxiv-digest Score 2, CF direct], (6) Schilder et al. cell-type-specific phenome / rare disease [Genome Medicine, Bastarache-related], (7) Cai et al. semaglutide-AMD OHDSI network study [Ryan + Hripcsak double new-articles] |
| METHODS-WATCH | 6 | Naimi et al. residual-on-residual regression, Faes et al. federated tensor decomp SLE/COVID/ILD, CPAgents cardiac PheWAS agents, DIMAS-OMOP Chinese OMOP standardization, Das et al. EB rare-variant burden AD, Ren et al. IBI-DT UKB WES AD; Marderstein & Montgomery Nature Research Briefing (carry-forward from 06-20) |
| SKIP | ~20 | See SKIP/noise section |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH over a single
day), this 13-day window delivers 7 HIGH / 6 METHODS-WATCH — a lower
per-day rate as expected for a longer aggregation, but with two
standout patterns: (a) a **self-citation hit** on DRIVE v3 (item #1),
which is the pipeline's highest-precision surfacing pattern, and (b)
the `arxiv-digest` pipeline producing **two clearly on-thread papers**
in one window (Mapelli UKB-PPP + Murali CF-causal), the strongest
`arxiv-digest` yield this quarter. Persistent pipeline hygiene issues
(knowledge-graph noise, motor-keyword noise, occasional fetch
failures) remain the top ops items.
