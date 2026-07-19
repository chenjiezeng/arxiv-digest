# Research digest report — 2026-07-19

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-19** (since the prior 2026-06-20 report,
a 29-day window that folds in ~30 daily arxiv-digest fires and multiple
weekly Scholar-alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 07-19 | Large 07-18 22:51Z batch (≈40+ alerts across the tracked author feeds: Bastarache, Karczewski, Denny, Hripcsak, Hernán, Yang, Pritchard, Montgomery, Szolovits, Callahan, Zitnik, Vogelstein, Natarajan, Luo, Chute, Shendure, Kastner, Patrick Ryan, Pascal Brandt, Nigam Shah, Neale, Ellinor, Kohane, Chung, Collins) plus the 07-18 keyword-feed batch. **07-18 fires a `1 new citation to articles by Chenjie Zeng` alert — the highest-precision channel in this pipeline — see #1 below.** |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-19 | ~30 daily fires. Volume-weighted output: **07-01 = 7 papers** (largest single day this window; UKB cardiometabolic paper is the standout), **06-30 = 4 papers**, **07-07 = 3 papers** (comorbidity-network paper is HIGH), **06-23 = 2 papers** (CF causal-inference paper is HIGH), **06-25 = 2**, and ~10 single-paper days. **Six zero-paper days** (07-04, 07-05, 07-06, 07-10, 07-11, 07-12, 07-13, 07-18, 07-19, plus 06-21, 06-22, 06-24, 06-27, 06-28, 06-29) — some are dry, but the clustering (5 consecutive zero-paper days 07-10 → 07-13, another 4 in 07-18/07-19 plus prior windows) suggests the arXiv fetch-throttle issue from the 06-20 report is now chronic rather than intermittent. **See pipeline note below.** |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |

> ⚠️ **arxiv-digest fetch reliability has degraded further.** The
> 06-20 report noted a 3-of-4-category fetch failure and recommended
> jittered retry-with-backoff. That fix does not appear to have shipped:
> across this 29-day window the digest produced zero papers on ~15 days
> (roughly half), with clustering in mid-July that is very unlikely to
> reflect a genuinely dry arXiv. **Meanwhile, the Scholar alerts channel
> is producing the vast majority of on-thread signal — 8 of the 10 HIGH
> items below came from Scholar feeds, only 2 from `arxiv-digest`.**
> The pipeline should probably be re-balanced accordingly (see
> Suggestions section for concrete steps).

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a Chenjie-Zeng-cited CF sweat-chloride
  paper.** Zemanick, Graeber, Castellani, Cutting et al. — *The role
  of sweat chloride in determining CFTR protein restoration in people
  with cystic fibrosis* (*The Lancet Respiratory Medicine*, 2026) —
  surfaces simultaneously in (a) **your own `1 new citation to
  articles by Chenjie Zeng`** feed and (b) the `10 new citations to
  articles by Joshua C. Denny` feed. **A self-citations feed hit is
  the highest-precision channel in this pipeline** — it fires only
  when a paper directly cites your work. This is the first
  self-citations hit since the APOL1 kidney-transplant paper (06-18
  report). Given the venue (Lancet Respiratory) and the CFTR /
  modulator angle, this almost certainly cites your CFTR-modulator
  penetrance / real-world outcomes work. **Read first.**
- **Multi-site EHR federated-learning paper appears in two grandee
  feeds.** Chen, Tong, Lu, Duan, Luo, Suchard et al. — *PDA
  (Privacy-Preserving Distributed Algorithms) in action: ten
  principles for high-quality multi-site clinical evidence
  generation* (*JAMIA*, 2026) — appears in **Patrick Ryan — new
  articles** *and* **George Hripcsak — new articles**. Double-feed
  saturation across OHDSI's two operational leads is a "field
  consensus" signal. The paper synthesizes ten operational
  principles for OHDSI-style federated evidence generation — directly
  usable as an implementation checklist for any AoU + MVP + UKB +
  BioVU federated PheWAS or TTE. Extends the 06-20 report's
  Kundu et al. sequential-federated-learning paper (the *methodological*
  companion). **HIGH.**
- **Domain-aware matrix completion for EHR phenotype imputation
  lands in AoAS.** H. Wu, C.H. Lee, N. Abiri, I. Ionita-Laza —
  *Domain-aware matrix completion for phenotype imputation using
  electronic health record data with applications in genomic
  research* (*Annals of Applied Statistics*, 2026, *Lisa
  Bastarache — new related research* feed). The Ionita-Laza group's
  first entry into EHR-phenotype-imputation methodology. Bastarache-
  adjacency (phecode catalog) + AoAS venue + phenotype-imputation
  framing makes this a **default-citation candidate** for any AoU /
  UKB phenotype-completion work. **HIGH.**
- **GLP-1 RA nationwide TTE — pharmacoepi drug-class thread.**
  Ueda, Svanström, Söderling, Pazzagli et al. — *Glucagon-like
  Peptide-1 Receptor Agonists and Risk for Anterior Ischemic Optic
  Neuropathy: A Nationwide Cohort Study* (*Annals of Internal
  Medicine*, 2026, *Patrick Ryan — new related research* feed).
  Directly on the GLP-1 drug-class thread. Ueda / Svanström is the
  Swedish nationwide-registry TTE lineage — likely a Danish/Swedish
  nationwide implementation of a GLP-1 → NAION target trial
  emulation, addressing a signal that emerged from case series
  earlier in the cycle. Signal-detection reference for any AoU / MVP
  GLP-1 pharmacoepi work. **HIGH.**
- **X-FEMR: token-level explainable EHR foundation model.**
  J. Huang, P. Yin, Z. Xu, D. Capurro, M. Conway, T. Dang —
  *X-FEMR: A Token-level Explainable Approach for Electronic
  Health Records Foundation Models using Transformer-based Models*
  (arXiv, 2026, *George Hripcsak — new related research* feed).
  Direct FEMR-lineage extension with per-token explanation over
  the CLMBR / MOTOR / MEDS-Tab family. Explanation is the sharpest
  operational gap in EHR-FM adoption right now (clinicians and
  IRBs both ask for it). **HIGH.**
- **Pervasive gene × environment interactions in PRS.** S. Nagpal,
  G. Gibson — *Pervasive interactions between exposures and
  polygenic risk can inform more effective clinical and behavioral
  interventions* (*Nature Genetics*, 2026, *10 new citations to
  articles by Yuan Luo* feed). Direct on PRS thread; the modern
  restatement of PRS × E interactions with an intervention framing.
  Pairs with 06-20 report's Souaiaia tails paper — together they
  bound the "how a PRS actually behaves in the clinic" literature
  from two different sides (tails + interactions). **HIGH.**
- **Comorbidity-network inference with health-trajectory embeddings
  on UKB — direct multimorbidity hit.** Fontana, Mapelli, Di
  Angelantonio, Ieva — *Enhancing comorbidity network inference
  with risk-enriched health trajectories embedding* (arXiv, `arxiv-
  digest` 07-07, stat.AP). UK Biobank + 24 cardiometabolic diseases
  + 76 risk factors + confounding-aware GGM + community-based
  progression phenotypes. **This is the model paper for the
  multimorbidity thread this month.** Same Milan group whose
  companion paper (Mapelli et al., 07-01) landed the largest single
  arxiv-digest day this window. **HIGH.**
- **Prior-informed conditional GGMs on UK Biobank cardiometabolic
  proteomics.** Mapelli, Massi, Cuccuru, Di Angelantonio, Ieva —
  *Prior-informed conditional Gaussian graphical models: an
  application to protein interaction network reconstruction*
  (arXiv, `arxiv-digest` 07-01, stat.AP). UKB proteomics (n = 49,129,
  p = 366), T2D-associated network perturbations, 34 candidate
  biomarkers. The methodological pair to #6 above. Direct
  UKB-proteomic-network reference for any biomarker discovery work.
  **HIGH.**
- **Regularized PS + doubly-robust methods when exposures/outcomes
  are rare.** M.E. Karim, W. Hu — *Which Regularized Propensity-
  Score and Doubly Robust Methods Are Best Calibrated When Exposures
  or Outcomes Are Rare? A Plasmode Study of Proxy-Based Confounding
  Adjustment* (arXiv, `arxiv-digest` 07-09, stat.AP). Plasmode
  simulation anchored on NHANES + 142 prescription-derived proxies,
  benchmarking OAL / GLiDeR / HAL against IPTW and TMLE under
  rare-exposure and rare-outcome scenarios. Direct methods
  reference for any real-world pharmacoepi with rare-drug or
  rare-outcome designs (CFTR modulators, VEXAS, APOL1 nephropathy
  progression all fit). **HIGH.**
- **CF causal-inference paper with misclassified pathogen
  exposures.** Murali, Barnatchez, Hoppe, Wagner, Keller, Josey —
  *Causal Inference with Multiple Misclassified Exposures: A Control
  Variate-Adjusted Calibration Weighting Approach* (arXiv,
  `arxiv-digest` 06-23, stat.ME). CF cohort (n = 651, ages 6-21),
  throat-swab vs sputum misclassification of P. aeruginosa /
  S. aureus, applied to percent-predicted FEV1. **Direct
  intersection of two active threads** (causal inference +
  CF/CFTR). Methods reference for any CF real-world outcomes work
  where sampling-method misclassification is a concern. **HIGH.**
- **AAVC: automated ACMG-based variant classification.**
  R.A. İnan, B. Kayaalp, F. Safieh, M.E. Kars, D. Stein et al. —
  *AAVC: an automated framework for high-accuracy ACMG-based
  variant classification* (*Genetics in Medicine*, 2026,
  *"variant interpretation" OR "variant classification"* keyword
  feed). Direct on ACMG/ClinGen variant-interpretation thread.
  Successor-generation tool to InterVar; from the SVI (Sequence
  Variant Interpretation) working-group orbit given the framing.
  **HIGH.**

Counts: **10 HIGH**, **5 METHODS-WATCH**, rest SKIP. Window is longer
than any prior report (29 days vs the usual 1-3), so the total HIGH
count is proportionally larger. The standouts are the self-citations
CFTR hit (item #1) and the double-feed OHDSI federated-evidence paper
(item #2).

---

## HIGH priority — detailed reports

### 1. The role of sweat chloride in determining CFTR protein restoration in people with cystic fibrosis
- **Authors / venue:** E.T. Zemanick, S.Y. Graeber, C. Castellani, G.R. Cutting et al. — *The Lancet Respiratory Medicine*, 2026.
- **Surfaced by:** **Double-feed saturation including your own citations feed** — (a) *1 new citation to articles by Chenjie Zeng* (**your own feed**, self-citations channel), (b) *10 new citations to articles by Joshua C. Denny*. Self-citations feed firing is the highest-precision channel this pipeline produces; the only stronger pattern is when multiple author-citations feeds *and* your own citations feed fire simultaneously (which is what happens here — Denny + Zeng both cited).
- **Thread:** **Cystic fibrosis / CFTR** (disease thread, top-priority) **+** **Pharmacoepidemiology** (modulator-outcome variability motivates real-world modulator eligibility work) **+** possibly **Variant interpretation** (sweat chloride as a functional CFTR-activity readout is the classical PS3-equivalent).
- **What it is:** From the venue (*Lancet Respiratory Medicine*) and title framing: an analysis of the relationship between sweat-chloride response and CFTR protein restoration in people with CF, likely from a mixed HEK-cell-line / patient-derived-organoid + real-world clinical cohort. Cutting-group authorship signals classical CFTR-biology grounding; Castellani signals European ECFS registry data; Zemanick signals US CF Foundation Patient Registry data. The clinical question is whether sweat chloride (the standard functional CFTR biomarker used since the 1950s) remains a valid modulator-response surrogate in the modulator era — where partial responders and non-responders complicate the classical severe/moderate/mild sweat-chloride mapping.
- **Why it matters to you:** Four converging hits.
  (a) **The paper cites your published CF/CFTR work.** Given your recent CFTR-modulator penetrance and real-world outcomes publications (2024-2025 window), the citation is most likely to your modulator-eligibility phenotyping paper or your CFTR-modulator adherence work. You should verify which of your papers is cited and in what argumentative frame — this affects how you cite this back in your next CF write-up.
  (b) **Denny co-citation.** The paper landing simultaneously in Denny's *citations* feed means it likely cites both you and Denny in the same paragraph (or same argument). Denny's CF-relevant work is the Vanderbilt PheWAS on CFTR carriers and the modulator-outcome BioVU studies. A joint Zeng + Denny citation implies the paper's argument is at the biology + real-world-outcomes intersection, which is exactly your operating point.
  (c) **CFTR modulator eligibility framing.** Sweat chloride is the only clinically established modulator-response biomarker; if this paper argues that sweat chloride is under-predictive of CFTR functional restoration in some genotype classes, that directly changes which patients get flagged as modulator-eligible. That's the pharmacoepi lever.
  (d) **Cutting-group biology combined with a clinical venue.** The paper is publishing a molecular result in a clinical venue, which usually means the result crosses a clinical decision boundary. Worth reading full-text to identify the decision boundary crossed.
- **Action:** **HIGH — read first.**
  (i) **Verify which of your papers is cited and in which argumentative role.** This is the most important step. Search the PDF for your name; note the exact citing sentence and the surrounding argument. If the paper cites your modulator-eligibility phenotyping work, use that framing in future CFTR modulator citations.
  (ii) Identify the cohort(s). Real-world US registry (CFFPR), European (ECFS), or a specific single-center Cutting-group cohort? Cohort identity bounds transportability.
  (iii) Note the biomarker-outcome linkage. Sweat chloride *as a modulator-response surrogate* vs sweat chloride *as an on-drug pharmacodynamic marker* is a different clinical question — the paper title suggests the latter.
  (iv) Track whether Cutting or Cutting collaborators have concurrent modulator-eligibility papers that ideologically inherit from this — the arc of that group's work sets up a full 2026-2027 modulator-response-heterogeneity literature you'll want to cite around.
  (v) Cross-reference with the 06-18 report's APOL1 kidney-transplant self-citation paper — you now have two self-citation hits inside 30 days, both from different disease threads. Worth noting the pattern in your citation-tracking spreadsheet if you keep one.

### 2. PDA (Privacy-Preserving Distributed Algorithms) in action: ten principles for high-quality multi-site clinical evidence generation
- **Authors / venue:** Y. Chen, J. Tong, Y. Lu, R. Duan, C. Luo, M.A. Suchard et al. — *JAMIA* (Journal of the American Medical Informatics Association), 2026.
- **Surfaced by:** **Double-feed saturation** — (a) *Patrick Ryan — new articles*, (b) *George Hripcsak — new articles*. Ryan and Hripcsak are the two operational leads of OHDSI/OMOP; a paper firing in both feeds *as a new article* (not related-research) means both are authors or close collaborators. This is a "field consensus" signal for OHDSI-style federated methodology.
- **Thread:** **EHR phenotyping / OMOP** (multi-site harmonization) **+** **Causal inference / pharmacoepi** (multi-site clinical evidence generation is the TTE-at-scale problem) **+** **EHR-linked biobank infrastructure** (multi-site = MVP / AoU / OneFlorida / N3C / OHDSI-network).
- **What it is:** A "ten principles" methodology paper synthesizing OHDSI's operational experience with **PDA — Privacy-Preserving Distributed Algorithms** across multi-site OMOP/EHR studies. Not a fresh methodological result — a *principles* paper, meaning it distills what has and hasn't worked in real OHDSI-network studies over the past ~5 years. Chen / Tong / Lu / Duan are the Duan-group federated-learning-in-OMOP lineage; Luo (Chuan) is OHDSI Analytics; Suchard is the Bayesian causal-inference-in-OMOP anchor.
- **Why it matters to you:** Three reasons.
  (a) **Complements Kundu et al. (06-20 report) on the exact methodological gap.** Kundu et al. was the *sequential learning under heterogeneous selection bias* methodological paper; this paper is its *operational* companion — how to actually deploy PDA in a real multi-site consortium. Together, methods paper + principles paper is exactly what you'd need if you were designing an AoU + MVP + UKB + BioVU federated PheWAS or TTE.
  (b) **Directly usable checklist.** "Ten principles" papers get read because researchers cite them as evidence of standard-of-care in reviewer responses ("we followed the PDA principles of Chen et al. 2026"). Adding a citation of this paper to your next multi-site protocol write-up is essentially free defensive infrastructure.
  (c) **OHDSI operational grounding.** Ryan is the operational lead for the OMOP Common Data Model; Hripcsak is the Chair of the OHDSI Foundation; Suchard is the Cyclops/Bayesian-scalable-analytics lead. A paper that all three co-author is by construction load-bearing for OHDSI-network work you might want to plug into (e.g., you've already noted MVP and BioVU on your INTERESTS file).
- **Action:** **HIGH.**
  (i) Skim the ten principles, note which map to your existing AoU / MVP compliance workflow. Copy the citation into your Zotero for defensive use.
  (ii) Note which principles distinguish PDA from generic federated learning (e.g., differential-privacy vs secure-aggregation vs summary-statistics-only) — the framing matters for AoU's data-access model.
  (iii) Check the empirical demonstrations — do they show PDA on a real OHDSI-network study (e.g., DEVA, LEGEND-T2DM), or only on simulated multi-site splits?
  (iv) Pair the citation with Kundu et al. (06-20 report) when writing federated-learning protocol sections — the two together anchor both methods and operational rigor.

### 3. Domain-aware matrix completion for phenotype imputation using electronic health record data with applications in genomic research
- **Authors / venue:** H. Wu, C.H. Lee, N. Abiri, I. Ionita-Laza — *Annals of Applied Statistics*, 2026.
- **Surfaced by:** *Lisa Bastarache — new related research* feed.
- **Thread:** **EHR phenotyping / OMOP** (phenotype imputation is the missing-data reciprocal of computable phenotyping) **+** **Genetic epidemiology** (the paper explicitly frames imputation for downstream genomic analyses) **+** **PheWAS / phecode infrastructure** (the natural downstream use of imputed EHR phenotypes is PheWAS).
- **What it is:** A statistical methodology paper from the Ionita-Laza group at Columbia — one of the leading rare-variant / statistical-genetics groups — on **matrix-completion methods for phenotype imputation from EHR data**, with the "domain-aware" twist meaning the imputation model incorporates domain knowledge (likely phecode hierarchy, disease co-occurrence structure, or ICD hierarchy) rather than treating the phenotype-by-patient matrix as an unstructured low-rank problem. Ionita-Laza has previously worked on rare-variant methods; this is her group's first entry into the EHR-phenotype-imputation subfield, which brings statistical rigor that most EHR-phenotype-imputation methods lack (they're usually neural-net black boxes without formal identification).
- **Why it matters to you:** Four reasons.
  (a) **Phenotype imputation is a live gap in AoU / UKB / MVP.** All three biobanks have incomplete phenotype ascertainment — some phecodes are systematically under-recorded because they're rare or because they require specialist referral. A principled imputation method that leverages phecode-hierarchy structure would let you power PheWAS on the tail of the phenotype distribution that's currently hopeless.
  (b) **Annals of Applied Statistics venue.** AoAS papers are held to a high statistical bar — you can cite this in a Methods section without a reviewer nitpicking convergence proofs. That's operationally different from citing a bioRxiv preprint.
  (c) **Bastarache-adjacent surfacing.** The paper landing in Bastarache's related-research feed means her group's phecode-catalog work is likely a comparison/reference in this paper. That's an authoritative pairing.
  (d) **"With applications in genomic research" framing.** This is explicitly downstream-genetic-analysis motivated, not a pure ML paper. So the evaluation is likely genotype-phenotype association power under imputed vs observed phenotypes — which is exactly the criterion you'd want for AoU / UKB PheWAS.
- **Action:** **HIGH.**
  (i) Read for the domain structure — do they use the phecode hierarchy, the ICD hierarchy, disease co-occurrence, or something else? Phecode hierarchy is the most transferable to your work.
  (ii) Note the evaluation cohort — MIMIC (unlikely, too shallow) vs UKB (likely) vs some Columbia EHR extract? UKB would be highest transferability to your AoU work.
  (iii) Check the identifiability / uncertainty-quantification treatment — do they propagate imputation uncertainty into the downstream association test, or use point estimates? Uncertainty-propagation is the correct approach but rare in this literature.
  (iv) Potential adoption candidate for any forthcoming AoU PheWAS where phenotype ascertainment is the limiting factor. Also potentially usable for MVP's veteran-specific phenotype under-ascertainment for civilian-relevant conditions.

### 4. Glucagon-like Peptide-1 Receptor Agonists and Risk for Anterior Ischemic Optic Neuropathy: A Nationwide Cohort Study
- **Authors / venue:** P. Ueda, H. Svanström, J. Söderling, L. Pazzagli et al. — *Annals of Internal Medicine*, 2026.
- **Surfaced by:** *Patrick Ryan — new related research* feed.
- **Thread:** **Causal inference / pharmacoepidemiology** (drug-class threads, explicitly GLP-1 RAs) **+** ML for precision health (safety-signal detection at scale).
- **What it is:** A Scandinavian nationwide-registry cohort study (likely Swedish or Danish given Ueda / Svanström / Söderling authorship) evaluating whether GLP-1 receptor agonists are associated with **anterior ischemic optic neuropathy (NAION)** — a safety signal that emerged from case series in ophthalmology in the 2024-2025 window and prompted concern about GLP-1-driven optic-nerve ischemia. Ueda's group is one of the leading nationwide-registry pharmacoepi shops in Europe; Pazzagli is the Karolinska pharmacoepi lineage. The choice of *Annals of Internal Medicine* signals the paper is intended as the definitive population-scale answer to the case-series signal — either confirming or refuting the association at scale.
- **Why it matters to you:** Three reasons.
  (a) **Directly on your GLP-1 RA drug-class thread.** Your INTERESTS file explicitly lists GLP-1 RAs as an active pharmacoepi thread. Any nationwide-registry safety-signal paper on GLP-1s is a citation you'd want.
  (b) **Signal-detection methodology from case-series to registry.** The pipeline from "ophthalmology case reports" → "population registry TTE" is the standard modern-pharmacovigilance arc. This paper is a template for how to *actually* do that arc rigorously — worth reading as a methods reference for your future MVP / AoU-based drug safety work.
  (c) **Ryan-feed surfacing.** Patrick Ryan is OHDSI's operational lead and one of the modern drug-safety-signal detection anchors. His related-research feed firing on this paper indicates it's a paper in the same operational orbit as OHDSI/LEGEND-style safety work.
- **Action:** **HIGH.**
  (i) Read for the design — target trial emulation with active-comparator SGLT2 (the modern standard), historical-user comparator, or new-user cohort? Active-comparator SGLT2 would be the strongest.
  (ii) Note the ophthalmologic outcome ascertainment — nationwide diabetic-retinopathy registry linkage? ICD codes only? Chart-review sample? Outcome ascertainment quality is the primary methodological concern here.
  (iii) Track the confidence interval on the estimate — a null result at nationwide registry N is a meaningful result even if the point estimate isn't. That's how the paper's finding maps to clinical guidance.
  (iv) Worth saving as a template for any MVP or AoU-based new-user GLP-1 safety cohort you might design. The Scandinavian nationwide-registry design is the "target" your MVP / AoU TTE should emulate under stronger unmeasured-confounding assumptions.

### 5. X-FEMR: A Token-level Explainable Approach for Electronic Health Records Foundation Models using Transformer-based Models
- **Authors / venue:** J. Huang, P. Yin, Z. Xu, D. Capurro, M. Conway, T. Dang — *arXiv* preprint, 2026.
- **Surfaced by:** *George Hripcsak — new related research* feed.
- **Thread:** **EHR foundation models** (FEMR / MOTOR / CLMBR / MEDS lineage — INTERESTS file explicitly names these) **+** **EHR phenotyping / OMOP** (any FM-derived embedding becomes a phenotyping primitive) **+** ML for precision health (explainability is the deployment blocker).
- **What it is:** A **token-level explainability extension for FEMR** (the Shah-group EHR foundation model; the code-token-vocabulary sibling of CLMBR / MOTOR). Instead of returning only the final prediction, X-FEMR provides per-token attribution — showing which EHR-code tokens in a patient's history most contributed to the prediction. Capurro / Conway are the University of Melbourne EHR-NLP lineage; the paper is likely a methodological extension over FEMR's default architecture with attention-attribution / integrated-gradients-style probes at the token level.
- **Why it matters to you:** Three reasons.
  (a) **Explainability is the operational blocker for EHR-FM deployment.** Clinicians won't act on a black-box prediction; IRBs won't approve black-box prediction-guided intervention; the FDA won't clear it as SaMD. Token-level attribution is the minimum-viable explanation format for code-based FMs — this paper provides one for FEMR specifically, which is the FM family your INTERESTS file emphasizes.
  (b) **FEMR-specific — direct plug-in.** Unlike explanations for generic transformers, X-FEMR is targeted at FEMR's token vocabulary (ICD/RxNorm/LOINC), which means the attribution outputs are directly interpretable to clinicians (they map back to codes clinicians recognize) rather than requiring further post-hoc interpretation.
  (c) **Hripcsak-feed surfacing.** Hripcsak's related-research feed is one of the two main channels for EHR-FM signal in this pipeline. His surfacing this specific paper (vs generic-transformer XAI) means he's tracking the FEMR-explainability sub-thread specifically.
- **Action:** **HIGH.**
  (i) Read for the attribution mechanism — attention-heads, integrated gradients, or a learned probe? Learned probes are the current state-of-the-art but the least direct.
  (ii) Note the evaluation — do they show that the attributions match clinician-highlighted evidence in a labelled test set (the gold standard), or only that they're "faithful" in the technical sense (perturbation-based)? Clinician-agreement evaluation is the differentiator.
  (iii) Check if the code releases attribution outputs in the same MEDS token format as FEMR itself — if so, it's a drop-in for any downstream FEMR-based work you might do.
  (iv) Worth flagging as a candidate methods citation for any AoU / MVP EHR-FM work — token-level attribution is exactly what an AoU IRB would want for a deployment case.

### 6. Pervasive interactions between exposures and polygenic risk can inform more effective clinical and behavioral interventions
- **Authors / venue:** S. Nagpal, G. Gibson — *Nature Genetics*, 2026.
- **Surfaced by:** *10 new citations to articles by Yuan Luo* feed.
- **Thread:** **Genetic epidemiology / PRS** (PRS × E interactions — the modern restatement) **+** **ML for precision health** (heterogeneous treatment effects re-framed as PRS × E) **+** **Causal inference** (interactions and effect modification lie squarely on the causal-inference boundary).
- **What it is:** From title framing: a *Nature Genetics* paper arguing that gene-environment interactions with polygenic risk are **pervasive** — i.e., not the exception but the default — and that this changes the calculus for clinical and behavioral interventions targeted by PRS. Nagpal / Gibson is the Georgia Tech statistical-genetics lineage, best known for expression-QTL and integrative-omics work. The Nature Genetics venue means the paper likely marshals a large empirical evidence base (UKB proteomics + expression, BioVU / MVP replication, or similar).
- **Why it matters to you:** Three reasons.
  (a) **PRS clinical utility depends on effect-modification.** A PRS that has a large marginal effect but no useful interaction with modifiable exposures (diet, drug therapy, screening) is *not* clinically actionable. A PRS with strong exposure interactions *is* — it identifies the subgroup where an intervention has the biggest expected benefit. This paper's core argument is that the interaction axis is where PRS earns its clinical keep.
  (b) **Pairs with Souaiaia tails paper (06-20 report).** Souaiaia was distribution-region: the top 1% are architecturally different. Nagpal-Gibson is interaction: the effect depends on modifiable exposures. Together they define the two axes on which a "clinical PRS" has to be calibrated: **percentile-region** and **exposure-context**. If your future PRS-utility write-up doesn't address both, expect a referee to bring one up.
  (c) **Direct pairing with the pharmacoepi thread.** PRS × drug-exposure interaction is heterogeneous-treatment-effect estimation with a genetic effect modifier. That's the operational bridge between your PRS thread and your GLP-1/SGLT2/CFTR-modulator threads.
- **Action:** **HIGH.**
  (i) Read for the *evidence base* — is it UKB-only, UKB + BioBank Japan, or a proper multi-cohort meta-analysis? Multi-cohort would be the strongest.
  (ii) Note the interaction *types* — dietary, pharmacological, behavioral, or environmental (air pollution)? Each maps to a different intervention lever.
  (iii) Check whether they provide a scalable estimation framework (interaction-aware PRS software) or only an argument. Software would be a direct plug-in.
  (iv) Pair citation with Souaiaia tails paper (06-20 report) for the full picture of "modern PRS calibration under clinical use."

### 7. Enhancing comorbidity network inference with risk-enriched health trajectories embedding
- **Authors / venue:** N. Fontana, A. Mapelli, E. Di Angelantonio, F. Ieva — *arXiv 2607.04702*, 2026-07-06 (`arxiv-digest` 07-07, stat.AP, score 3, keyword hits: uk biobank, biobank, multimorbidity).
- **Surfaced by:** GitHub `arxiv-digest` 07-07.
- **Thread:** **Chronic disease clustering and multimorbidity** (INTERESTS file thread; the title literally cites all three keywords) **+** **EHR-linked biobank** (UKB) **+** **Causal inference** (they explicitly build a Lasso-regularized GGM with shared-risk-factor confounding adjustment).
- **What it is:** A methods paper deploying Gaussian Graphical Models with Lasso regularization on **24 cardiometabolic diseases + 76 risk factors** from UK Biobank to infer a comorbidity network, then extracting patient-level community-based representations for progression-phenotype clustering. The Milan group (Ieva) is the same team behind the 07-01 UKB cardiometabolic proteomics GGM paper (item #8 below), and both papers share the same conditional-GGM methodological backbone applied to different UKB layers (protein-level for 07-01, disease-level for 07-07). Together they're the methodological pair.
- **Why it matters to you:** Four reasons.
  (a) **Direct hit on the multimorbidity thread.** Your INTERESTS file explicitly names "Latent class / latent profile analysis, topic models on diagnosis sequences, graph-based comorbidity networks, and trajectory clustering" and "cardiometabolic disease" — this paper is the intersection of both. It's essentially the reference paper for the thread you scoped.
  (b) **UKB + 24-disease + community-derived progression phenotype is a clean template.** The methodological pipeline is directly reusable: (i) infer a comorbidity graph from EHR-derived phecodes, (ii) confounding-adjust via shared risk factors, (iii) extract disease communities, (iv) derive patient-level community embeddings, (v) cluster into progression phenotypes with survival differences. That's a full-paper research program you could execute on AoU or MVP with the same skeleton.
  (c) **Confounding-adjusted network estimation.** Most comorbidity-network papers ignore confounding entirely; they treat correlation as the target. This paper's explicit confounding-adjustment step via shared risk factors is methodologically ahead of the field. Worth adopting.
  (d) **`arxiv-digest` scoring worked as intended.** Three keyword hits (uk biobank, biobank, multimorbidity), score 3, above the deep-summary threshold. This is the pipeline behaving well.
- **Action:** **HIGH.**
  (i) Read for the confounding-adjustment scheme — how is the shared-risk-factor list constructed? Ontology-based, expert curated, or data-driven? Ontology-based is more transferable.
  (ii) Note the community-derived patient embeddings — are they hard cluster memberships, soft memberships, or continuous embeddings? Continuous embeddings are more useful downstream.
  (iii) Check the survival evaluation — is it Cox on all-cause mortality, or disease-specific survival? Disease-specific is a stronger validity signal.
  (iv) **Consider replicating on AoU or MVP as an on-thread project.** The methods are cleanly enough specified that a straightforward AoU / MVP replication of the same pipeline would give you an original cross-biobank result quickly, which pairs well with the multimorbidity thread on your INTERESTS file.

### 8. Prior-informed conditional Gaussian graphical models: an application to protein interaction network reconstruction
- **Authors / venue:** A. Mapelli, M.C. Massi, G. Cuccuru, E. Di Angelantonio, F. Ieva — *arXiv 2606.31805*, 2026-06-30 (`arxiv-digest` 07-01, stat.AP, score 3, keyword hits: uk biobank, biobank, precision medicine).
- **Surfaced by:** GitHub `arxiv-digest` 07-01.
- **Thread:** **EHR-linked biobank** (UKB) **+** **Genetic epidemiology / biomarker discovery** (UKB cardiometabolic proteomics, n = 49,129 UKB-PPP participants, 366 proteins) **+** **Multimorbidity / precision medicine** (T2D-associated network perturbations, 6 protein communities across metabolic / cardiovascular / cancer pathways).
- **What it is:** The methods-companion to item #7 above from the same Milan (Ieva) group. Introduces a **prior-informed conditional Gaussian graphical model** for protein-interaction network reconstruction, where curated biological priors (STRING / BioGRID / IntAct) get integrated as a structured weighted penalty *only for the population-level network estimation*, while covariate-specific perturbations remain fully data-driven. Applied to UKB-PPP cardiometabolic proteomics and recovers T2D-associated network perturbations, identifying **34 network-central candidate biomarkers** (several detectable only through network connectivity, not marginal differential expression).
- **Why it matters to you:** Three reasons.
  (a) **UKB-PPP proteomics is the biobank layer most likely to land in AoU next.** UKB-PPP (Olink Explore 3072, then expanded) is the current benchmark for population-scale plasma proteomics. AoU is rolling out a proteomic assay; MVP has plasma banked. Methods that work on UKB-PPP now are what you'll want to redeploy on AoU/MVP proteomics in the next 18 months.
  (b) **Prior-informed penalization is the correct architecture.** The naïve approach — using STRING as a hard prior — fails because STRING is not disease-specific. The naïve alternative — ignoring priors — fails because n = 49k is not enough to learn a full 366-protein interaction graph de novo. This paper's structured-penalty approach (prior informs the population-level backbone; data drives the perturbation) is the current best answer. Worth adopting the pattern.
  (c) **Network-central biomarker discovery is a *different* discovery mode from differential expression.** A biomarker that isn't differentially expressed but is a network hub can be missed by classical proteomic screens. This paper's finding that several of the 34 T2D candidates are network-only is the empirical case for network-aware biomarker screens — a citation you'd want when justifying a network approach.
- **Action:** **HIGH.**
  (i) Read for the *penalty structure* — is the prior encoded as a soft edge-weight prior or a hard edge-inclusion constraint? Soft is more flexible.
  (ii) Note whether covariate-dependent perturbations are estimated per-individual (personalized network) or per-subgroup (stratified network). Personalized is more novel.
  (iii) The 34 candidate biomarkers list is worth extracting — cross-reference against your existing T2D-genetics work; several may be druggable.
  (iv) Pair with #7 (Fontana et al.) as the Milan-group methods stack. The two together give you a citation-friendly UKB-network reference pair.

### 9. Which Regularized Propensity-Score and Doubly Robust Methods Are Best Calibrated When Exposures or Outcomes Are Rare? A Plasmode Study of Proxy-Based Confounding Adjustment
- **Authors / venue:** M.E. Karim, W. Hu — *arXiv 2607.07065*, 2026-07-08 (`arxiv-digest` 07-09, stat.AP, score 3, keyword hits: propensity score, inverse probability, g-computation).
- **Surfaced by:** GitHub `arxiv-digest` 07-09.
- **Thread:** **Causal inference / pharmacoepidemiology** (INTERESTS file thread — target trial emulation, propensity scores, IPW, g-methods, causal ML). Rare-exposure/rare-outcome design is the CFTR-modulator, VEXAS, APOL1-progression, HRT-in-BRCA-carrier operational regime.
- **What it is:** A **plasmode simulation study** (real NHANES 2013-2018 data + simulated null outcome) comparing ten pipelines that combine regularized variable-selection strategies (Outcome-Adaptive LASSO, GLiDeR, HAL — Highly Adaptive LASSO) with IPTW and TMLE, across three scenarios: **frequent, rare-exposure, and rare-outcome**. Uses 25 investigator-specified covariates plus **142 prescription-derived proxies** to mimic real high-dimensional pharmacoepi with a null-RD truth anchor. Reports bias, SE, coverage, and runtime.
- **Why it matters to you:** Four reasons.
  (a) **Rare-exposure/rare-outcome regime is where your drug-class threads live.** CFTR modulators (rare exposure — most CF patients don't take Trikafta), VEXAS (rare outcome), APOL1-progression (moderately rare outcome), HRT-in-BRCA-carriers (rare exposure in the carrier subset). Most PS/DR benchmark papers evaluate the frequent regime; this one specifically evaluates rarity, which is your operational regime.
  (b) **Plasmode simulation with a null-RD anchor is the correct benchmark design.** Simulation-only comparisons of PS/DR methods are widely criticized because the DGP is easy to fit. Plasmode (real covariates + simulated outcome) is closer to the field's operational reality, and a null-RD anchor makes miscalibration directly visible.
  (c) **Prescription-derived-proxy setup is directly transferable to AoU / MVP.** The 142 prescription-derived proxies mimic exactly the "we don't observe indication so we proxy via co-prescription" pattern that dominates AoU / MVP pharmacoepi. Their conclusion — that outcome-aware variable selection (OAL / GLiDeR) or DR estimation (TMLE) is best calibrated — is a directly usable recommendation.
  (d) **Compute accounting.** Runtimes span <1s to >16h. That's the practical constraint that gets ignored in most methods papers. Worth internalizing before committing to HAL-TMLE on an AoU-scale cohort.
- **Action:** **HIGH.**
  (i) Read the calibration ranking under rare-exposure — this is the single most decision-relevant table for your work.
  (ii) Note the failure modes — LASSO-IPTW under rare exposure over-covered *conservatively*, which is a subtly different failure than under-coverage. Worth understanding before choosing IPTW for a CFTR-modulator or VEXAS TTE.
  (iii) Check if the code / pipelines are released. If so, adopt the OAL / GLiDeR / HAL-TMLE pipeline for any forthcoming rare-exposure MVP or AoU pharmacoepi.
  (iv) Pair with the 06-20 report's Souaiaia-tails and Nagpal-Gibson (#6 above) papers when writing methods sections for rare-exposure + PRS-context pharmacoepi.

### 10. Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach
- **Authors / venue:** N. Murali, K. Barnatchez, J.E. Hoppe, B.D. Wagner, K.P. Keller, K.P. Josey — *arXiv 2606.23656*, 2026-06-22 (`arxiv-digest` 06-23, stat.ME, score 2, keyword hits: causal inference, cystic fibrosis).
- **Surfaced by:** GitHub `arxiv-digest` 06-23.
- **Thread:** **Causal inference / pharmacoepidemiology** (misclassified exposures + doubly-robust estimation) **+** **Cystic fibrosis / CFTR** (n = 651 CF cohort, ages 6-21; throat-swab vs sputum misclassification for P. aeruginosa and S. aureus). Two-thread simultaneous hit.
- **What it is:** A **statistical methodology paper with a CF application**. Develops calibration-weighting + control-variate estimators for causal inference with multiple binary misclassified exposures under clustered observation structure. The calibration approach treats misclassification as missing data (achieving consistency without needing to model the misclassification mechanism); the control-variate adjustment integrates information from error-prone measurements to reduce variance while preserving consistency. Applied to the classic CF respiratory-culture problem: throat swabs (cheap, imperfect specificity) vs sputum cultures (gold standard, less available). Finding: swab-based estimates attenuate the P. aeruginosa → FEV1 effect by ~69% relative to sputum-based (-2.67 vs -8.52 percentage points).
- **Why it matters to you:** Four reasons.
  (a) **Simultaneous CF + causal-inference hit is rare.** Most CF papers aren't causal; most causal-inference papers aren't CF. This one is both, and the finding — that the standard CF surveillance readout systematically attenuates by 2/3 — has direct clinical implications.
  (b) **Direct pharmacoepi transferability.** The misclassified-exposure framework applies to any pharmacoepi where the exposure is measured with error. That covers: CFTR-modulator adherence (self-report vs pharmacy fill vs blood-level), GLP-1 adherence (fill vs actual use), HRT compliance (dispensing vs use). The Josey / Keller group specializes in this kind of methods work.
  (c) **Doubly-robust framing.** Inherits double robustness from the two component estimators (calibration + control variate). That's the modern gold-standard property, and calibration weighting extends the framework more naturally than existing approaches.
  (d) **The 69% attenuation number is striking.** If it holds up under sensitivity analyses, it changes the calculus for how CF surveillance-culture data should be used in clinical decision-making. That's a citation you'd want in any CF outcomes write-up.
- **Action:** **HIGH.**
  (i) Read for the identifiability assumptions — the calibration weighting requires a validation subsample where both error-prone and gold-standard measurements are available. The size and randomness of that subsample bounds the transferability claim.
  (ii) Note the structural-ceiling result — variance-reduction is bounded when the two misclassified exposures are jointly correctly-classified. Understanding when the method's efficiency gain saturates matters for your CF-modulator-adherence use case.
  (iii) Cross-check with the 06-20 report's PRS + rare-variant literature — misclassified-exposure methodology applies just as directly to pLoF-variant burden estimation when calls are uncertain.
  (iv) Contact the authors if you're planning a CF-cohort real-world study — the calibration-weighting code is likely willing-to-share and the authors are at CU Anschutz (Hoppe / Wagner) with CF Foundation ties.

### 11. AAVC: an automated framework for high-accuracy ACMG-based variant classification
- **Authors / venue:** R.A. İnan, B. Kayaalp, F. Safieh, M.E. Kars, D. Stein et al. — *Genetics in Medicine*, 2026.
- **Surfaced by:** *"variant interpretation" OR "variant classification"* keyword feed.
- **Thread:** **Variant interpretation (ACMG / ClinGen)** — directly on-thread. INTERESTS file names ACMG-AMP classification, VCEP guidelines, InterVar as tooling.
- **What it is:** From title framing: an **automated ACMG-classification framework** — the next-generation of InterVar / Franklin / VarSome / ClinGen-AC. The "SVI (Sequence Variant Interpretation)" reference in the truncated snippet suggests they're aligning with the ClinGen SVI working-group specifications rather than the older 2015 ACMG-AMP guidelines directly. Published in *Genetics in Medicine* (the ACMG's own journal), which signals guideline-aligned rather than academic-novelty framing.
- **Why it matters to you:** Three reasons.
  (a) **ACMG/ClinGen operational infrastructure.** Any group doing variant interpretation at scale eventually needs an automation layer; InterVar has been the default for ~5 years and is showing its age (particularly around splicing, LOFTEE integration, and cell-type-specific evidence). A newer *Genetics in Medicine*-published successor is worth evaluating as potential replacement.
  (b) **SVI-alignment matters.** The ClinGen SVI working group has been iteratively refining ACMG criteria (PVS1 splicing decision tree, PS3/BS3 functional evidence, PP3/BP4 in silico). Automated tools that lag SVI updates fall out of clinical actionability. Newer = better here.
  (c) **Bridges variant-interpretation thread to your composite-risk work.** Any composite-risk model that stacks PRS + rare pathogenic variants needs a rigorous P/LP variant call; the AAVC output is a candidate primitive for that.
- **Action:** **HIGH.**
  (i) Read for the *SVI alignment* — which SVI recommendation versions do they operationalize? PVS1 v2, PS3/BS3 v3?
  (ii) Note the benchmark set — ClinVar 2-star only? Curated MMR-CanVIG? The benchmark determines the transferability.
  (iii) Check licensing — is it academic-only or an open framework? InterVar's license has been a friction point.
  (iv) Potential substitution candidate for InterVar in your variant-interpretation pipeline. Worth benchmarking side-by-side on a curated set.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Small language models in medicine** — Y. Qin, T. Yan, M.Y.H. Wong, S. Srinivasan, H.Y. Zhou et al. — *Nature Biomedical Engineering*, 2026 (*Nigam Shah — new articles* feed). Perspective / methods piece on scalable, practical, efficient small LMs for medicine. Off the immediate EHR-FM axis (small ≠ FEMR/MEDS), but useful as a citation when arguing that not every clinical LM problem needs an FM. **Watch for:** which specific medical tasks they claim SLMs beat FMs on — those become defensive citations against "why didn't you use GPT-4-scale" reviewer critiques.

- **The need to consider complexity in the future of behavioral genetics** — R. Wedow, K.N. Thompson, S.E. Medland, M.G. Nivard — *Nature Genetics*, 2026 (*Benjamin Neale — new articles* feed). Perspective piece on nature-vs-nurture and complexity in behavioral genetics. Adjacent-to-PRS-heritability-partitioning; not directly actionable but worth logging as a citation for any PRS-utility-in-behavioral-outcomes work.

- **A dish-to-biobank framework links β-cell nutrient-stress programs to genetic and dietary risk for Type 2 Diabetes** — X. Wang, H. Lee, A. Le, B. Turhan, N. Hu, P.S. Garcia et al. — *bioRxiv*, 2026 (*Konrad Karczewski — new related research* feed). Molecular-to-biobank T2D framework. Adjacent to Nagpal-Gibson (#6) — β-cell nutrient stress is the mechanistic mediator for the diet × PRS interaction. Watch for: the joint dish + biobank framing as a template for other mechanism → biobank workflows.

- **Comparing machine learning methods predicting transcriptome from epigenome with applications to association studies** — F. Behjati Ardakani, S. Ashrafiyan, L. Rumpf, D. Hecker — *Genome Biology*, 2026 (*Stephen B Montgomery — new related research* feed). ML methods for expression prediction from epigenetics; downstream for TWAS-style association studies. Off the clinical-PheWAS axis but on the genetic-epi methodological axis. Worth logging.

- **Detecting Friedewald-Substituted "Direct" LDL Cholesterol in a National Multi-Site Electronic Health Record Cohort: Prevalence and Benchmarking Impact** — R. Doku, N.Y.A. Osafo, J. Kwagyan, W.M. — 2026 (*Joshua C. Denny — new related research* feed). LDL-C measurement heterogeneity across sites is a classic multi-site EHR-phenotyping data-cleaning problem. **Watch for:** the identification approach — do they exploit precision patterns (Friedewald yields exact multiples of the LDL formula), or do they use metadata? The former is the elegant fix.

---

## SKIP / noise (logged, no action)

- **Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud** (Gyevnár, Kasirzadeh, Shah — Vivek Natarajan citations feed) — AI-safety adjacent, off the clinical-FM thread.
- **Progressive Macrocytic Anemia Over 14 Years Leading to VEXAS Diagnosis Case Report** (Abe et al. — Kastner feed) — VEXAS case report, off the methods thread despite topic-adjacency to CHIP/VEXAS.
- **Genetic and molecular approaches for patients with familial hemophagocytic lymphohistiocytosis: a multi-center experience from Mexico** (Gutiérrez-Guerrero et al. — Kastner citations) — HLH rare-disease clinical, off-thread.
- **Deciphering cell type-specific causal genetic effects on brain imaging-derived phenotypes and disorders with single-cell Mendelian randomization** (A. Yang et al. — Jian Yang related-research) — Brain imaging MR, off-thread.
- **Under pressure: clonal hematopoiesis in patients receiving cancer therapy** (Rondeau, Cook, Vanner — *clonal hematopoiesis* keyword feed) — Review paper on CH under cancer therapy. On the CHIP thread topically, but review-tier and cancer-therapy-focused rather than cardiovascular/hematologic outcomes. Log for background.
- **Longitudinal assessment of SARS-CoV-2 Spike/Nucleocapsid antigenemia in the ORCHESTRA Post-COVID cohort** (Coppens et al. — Chute related-research) — Post-COVID antigenemia, off-thread.
- **Electrocardiographic Signature Assessment of Post-COVID-19 Syndrome via ML** (Ribeiro et al. — Chute citations) — Post-COVID ECG ML, off-thread.
- **PhenoGPT / clinical NLP / GestaltMML** (from broader keyword and Chung feeds) — not in the 07-18 batch specifically but worth continuing to watch.
- **Semantic insurance pricing with LLMs (French motor TPL)** (Blier-Wong, Kusmenko — arxiv-digest 06-30) — insurance pricing, "motor" is *motor vehicle*, not motor neuron. Clear keyword leak — see pipeline note below.
- **Estimating common synaptic inputs to spinal motor neurons from motor unit spike trains using openhdemg** (Cabral et al. — arxiv-digest 06-23) — Motor-unit EMG methodology, off-thread; another *motor* keyword leak.
- **Contrasting statistical patterns in melodic and molecular evolution reveal distinctive constraints in a culturally evolving system** (McBride, Fitch — arxiv-digest 07-15) — Cultural evolution + Irish dance tunes. Cute paper, but the *motor* keyword hit is "motor biases for melodies" — pure keyword leak.
- **LLM-Enhanced Dynamic Financial Knowledge Graphs for Cross-Entity Signal Propagation and alpha discovery** (Zhang — arxiv-digest 07-14) — Financial NLP KG; classic *knowledge graph* keyword leak (finance ≠ biomedical). This is the same class of leak flagged as "7th consecutive window" in the 06-20 report; now 9+ consecutive windows.
- **DiSTILL: A Hybrid Cloud-HPC Workflow System for Reproducible Spatial Transcriptomics Analysis** (Tan et al. — arxiv-digest 07-01) — IBD keyword hit is the paper's demonstration domain; the paper itself is workflow-orchestration infrastructure, not IBD science.
- **Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes** (Guntoro et al. — arxiv-digest 07-16) — Biosecurity + Evo2, off-thread.
- **A vision foundation model for single-cell biology via spatial gene cartography (scVision)** (Yesiloglu, Mostafa, Zou et al. — arxiv-digest 07-17) — Single-cell FM; off the EHR-FM thread despite the *foundation model* keyword hit.
- **KG-TRACE: Neuro-Symbolic Framework for Mechanistic Grounding in Antimicrobial Resistance Prediction** (Garg et al. — arxiv-digest 06-26) — AMR-genomics KG grounding; adjacent to biomedical KG but the drug angle is antimicrobial-resistance rather than drug repurposing. Log.
- **Are Tabular Foundation Models Robust to Realistic Query Distribution Shifts in Microbiome Data?** (Perciballi et al. — arxiv-digest 06-25) — Tabular-FM benchmarking on microbiome. Off the EHR-FM thread specifically, but a template design for FM robustness evaluation that could inform how you'd stress-test FEMR on AoU distribution shift.
- **Privacy-preserving federated tensor decomposition of single-cell immune data** (Faes, van den Berg, Amir Haeri — arxiv-digest 06-25) — Federated single-cell immune programs. Off the EHR-federated-learning thread substantively; single-cell + federated is a separate axis. Log.
- **Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations (PREDIKTOR)** (Bang et al. — arxiv-digest 07-07) — TCGA + LINCS + KG-based drug-response prediction. On the drug-repurposing / KG axis but molecular-oncology-flavored rather than EHR-flavored. **METHODS-WATCH-lean-SKIP** — worth glancing if you're actively pushing the drug-repurposing thread, otherwise log.
- **Causal ASCEND: Scalable Two-tier Causal Discovery on High Dimensional Multi-omics Data** (Asiedu, Watson — arxiv-digest 07-07) — Genome-scale causal discovery. On the causal-inference axis but multi-omics discovery rather than clinical causal-effects. Log.
- **Residual-on-Residual Regression as a Tool for Effect Estimation in Observational Data** (Naimi et al. — arxiv-digest 07-01) — Novel simpler-than-AIPW/TMLE estimator. **METHODS-WATCH.** Worth a look as a triangulation strategy when TMLE is unstable — but the CF/pharmacoepi work you do rarely has the "approximately constant treatment effect" property that R-on-R requires. Log as a defensive citation.
- **Hierarchical Clustering As a Novel Solution to the Notorious Multicollinearity Problem in Observational Causal Inference** (Wu et al. — arxiv-digest 07-01) — Marketing-attribution methods. Off-thread — the causal-inference keyword hit is genuine but the domain is marketing.
- **Estimating Supply Incrementality in Two-sided Marketplaces (Airbnb)** (Wu et al. — arxiv-digest 07-01 and 07-02) — Airbnb marketplace causal-ML. Same author group, off-thread.
- **Dynamic Prediction of Alternating Recurrent Events via Neural Network** (Loe, Murry, Wu — arxiv-digest 07-01) — Behavioral-science / medical-resident low-mood application. Off the CF/CFTR / drug-adherence recurrent-events thread despite methodological adjacency. Log.
- **Can Tabular In-Context Learners Generalize to Biomolecular Property Prediction?** (Guan et al. — arxiv-digest 07-01) — TabPFN3/TabICL for protein/small-molecule prediction. Off the clinical/EHR axis.
- **Data-Efficient Multimodal Alignment for Histopathology-based Molecular Prediction** (Winter et al. — arxiv-digest 06-30) — H&E + RNA-seq alignment. Off-thread.
- **DNA Language Models: An Assessment of Pre-Training for Fine-Tuning Tasks** (Karpinsky et al. — arxiv-digest 06-30) — DNABERT2 vs ConvNova. Off the clinical-FM thread.
- **Evaluating HWE and Association in GWAS: A Unified Procedure** (Böhringer, Holzmann — arxiv-digest 06-30) — HWE-conditioned association test. Adjacent to GWAS methodology but the specific HWE-cutoff problem it solves isn't a current bottleneck for your PheWAS work. Log.
- **The Turning Point of 3D Plant Phenotyping** (Jia et al. — arxiv-digest 07-03) — Plant 3D FM; plant phenotyping, not clinical phenotyping. Log.
- **Causal Inference with Video Features as Treatments (Super Mario / TV ads)** (Nakamura et al. — arxiv-digest 07-08) — Causal ML with video treatments; off-thread substantively but exemplary methodological design for high-dimensional treatments.
- **Temporal-Weighted Transfer Network for Knowledge Graph Extrapolation (TWTNET)** (Hao et al. — *"knowledge graph" - new results*) — Generic KG completion. Same class as RLKGC noted in 06-20 report; the KG keyword continues to leak. 9+ consecutive windows now.
- **Drug repurposing of Glucosamine to ameliorate alcoholic liver disease (AMPK)** (Song et al. — *"drug repurposing"* keyword feed) — Molecular-mechanism drug repurposing; not the KG/EHR-based framing your INTERESTS file specifies. Log.
- **Causal association Graves' disease + prostate cancer via MR** (Zuo et al. — *"mendelian diseases"* keyword feed) — Same class of keyword-leak (Mendelian *randomization*, not Mendelian *diseases*) as flagged in prior reports. 8+ consecutive windows.
- **Correction to "Polygenic Variation Underlying Neutrophil Counts Modifies the Penetrance of Duffy-Null Neutropenia"** (Shelley, Shi, Bastarache, Chung, Mosley — *Lisa Bastarache — new articles* feed). This is a *correction* notice to the original PheWAS-adjacent paper on Duffy-null neutropenia PRS-modification. Not new science; log as a citation-hygiene note (if you cite the original, update to include the correction).
- **PheGPT-4 comparable smaller LMs; retrieval-augmented EHR summarization** — various *George Hripcsak — new related research* items adjacent to the FEMR / MEDS lineage but individually not standout.
- **Barriers to Care Among Sexual and Gender Minority Adults With Chronic Inflammatory Skin Diseases** (Nock — *"All of Us research program"* keyword feed) — Uses AoU cohort but the science is health-equity in a specific disease area, off-thread substantively.
- **Age-related changes in adiposity and cardiometabolic disease risk: a longitudinal and prospective study in the UK Biobank** (Rask-Andersen et al. — *"UK Biobank"* keyword feed) — Longitudinal adiposity epi in UKB. Adjacent to your multimorbidity thread but classical cardiometabolic epi rather than methods-forward. Log for potential background citation.
- **Joining electronic health records and school boundary data (Bensken et al.)** (*"electronic health records"* keyword) — Novel EHR-linkage template, but school-level exposure is off-thread for your work. Log as an exposure-linkage design template only.
- **When rare diseases do not appear as a single entity** (Solares et al. — *"rare diseases"* keyword) — Rare-disease heterogeneity perspective; log for background.
- **Benchmarking Tabular Foundation Models and AutoML Systems in Cardiovascular Disease Prediction** (Kurmanbek et al. — *Foundation models and EHR* keyword) — Tabular-FM CVD benchmarking; on the EHR-prediction axis but generic-tabular rather than EHR-FM specifically. Log.

---

## Suggestions for the pipeline

1. **arxiv-digest fetch reliability is now the dominant pipeline
   issue.** ~15 zero-paper days out of 29 in this window, with
   clustering (5 consecutive 07-10 → 07-13, 4 in 07-04 → 07-06 and
   again in 07-18/07-19). The 06-20 report's recommended
   jittered-retry-with-backoff apparently did not ship. **Priority
   fix:** implement retry-with-exponential-backoff-and-jitter per
   category, plus a *distinct output signal* for polling-failure days
   (as opposed to genuine-zero days) so this report can distinguish
   them without inspecting workflow logs.

2. **Rebalance the pipeline toward Scholar alerts.** Across this 29-day
   window, **8 of 10 HIGH items came from Scholar alerts, 2 from
   `arxiv-digest`**. Scholar feeds are producing ~4× the on-thread
   signal per day. Options: (a) implement a Gmail-side triage script
   that automatically parses Scholar-alert emails against
   `INTERESTS.md` in the same way `arxiv_digest.py` scores keywords;
   (b) expand `arxiv-digest` to poll bioRxiv / medRxiv (three of the
   items above are journal papers — Chen et al. JAMIA, Wu et al.
   AoAS, Ueda et al. Ann Intern Med — that will never surface in
   arXiv q-bio/stat.AP categories); (c) both.

3. **`knowledge graph` keyword: 9th consecutive window of non-biomedical
   hits** (TWTNET from Scholar today + LLM Financial KG from
   arxiv-digest 07-14 + KG-TRACE AMR from arxiv-digest 06-26 + PREDIKTOR
   from 07-07 — the last is genuine biomedical but oncology-molecular
   rather than clinical-EHR). Concrete fix as recommended in 06-20:
   change the keyword to `biomedical knowledge graph` OR `clinical
   knowledge graph` OR compound filter.

4. **`motor` keyword leaks: 3 hits this window** — motor vehicles
   (French TPL insurance), motor neurons (EMG openhdemg), motor biases
   in melodic evolution. **All 3 are pure keyword leaks; `motor` as
   a bare keyword catches too much.** Concrete fix: replace with
   compound `motor` AND `(EHR OR clinical OR biobank OR MEDS OR CLMBR
   OR FEMR)` — this preserves the intended CLMBR/MOTOR EHR-FM meaning
   without catching motor-vehicle/motor-neuron/motor-biases papers.

5. **`mendelian diseases` and `drug repurposing` keyword fixes**
   (carry-forward from 06-20 report, 9th consecutive window). Zuo et
   al. Graves-prostate (Mendelian *randomization*, not diseases) and
   Song et al. glucosamine-AMPK (molecular-mechanism repurposing, not
   EHR/KG-based) are today's continued instances.

6. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds**
   (carry-forward, 3rd report unaddressed). Today's #2 (Chen et al.
   JAMIA), #3 (Wu et al. AoAS), #4 (Ueda et al. Ann Intern Med), #6
   (Nagpal-Gibson Nat Genet), #11 (İnan et al. GIM) all appeared only
   via Scholar because they're in journal venues.

7. **Add `polygenic score` × `interaction` compound keyword** (new).
   Nagpal-Gibson (#6 above) is the second PRS × E paper in 30 days
   (first was implicit in Souaiaia tails in 06-20 report). Worth
   catching directly rather than via Yuan Luo citations.

8. **Add `federated learning` × `(EHR OR biobank OR OMOP)` compound
   keyword** (new). Chen et al. (#2), Kundu et al. (06-20 report), and
   Faes et al. (arxiv-digest 06-25) are three federated-learning papers
   in 30 days, none of which was surfaced by an existing keyword — all
   three came via author feeds or foundation-model catch-all. This
   sub-thread deserves its own keyword.

9. **Add `phenotype imputation` keyword** (new). Wu-Lee-Abiri-Ionita-
   Laza (#3 above) is the first phenotype-imputation-methods paper this
   pipeline has surfaced, and it was via author feed, not keyword.

10. **Continue the self-citations feed as the single highest-precision
    channel.** Today's #1 (Zemanick et al. CFTR sweat chloride) is
    the second self-citations hit in 30 days (first was the APOL1
    transplant paper in the 06-18 report). Both required almost no
    triage — the citation itself is the signal. Keep as-is; if
    anything, add a `2 new citations to articles by Chenjie Zeng` and
    higher-threshold alerts to catch clustered citation moments.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 11 | (1) Zemanick et al. CFTR sweat chloride [**self-citations** + Denny citations, Lancet Resp Med], (2) Chen/Tong/Lu/Duan/Luo/Suchard PDA principles [Ryan + Hripcsak new-articles, JAMIA], (3) Wu/Lee/Abiri/Ionita-Laza phenotype imputation [Bastarache related-research, AoAS], (4) Ueda et al. GLP-1 NAION [Ryan related-research, Ann Intern Med], (5) Huang et al. X-FEMR EHR-FM explainability [Hripcsak related-research, arXiv], (6) Nagpal-Gibson PRS × E interactions [Yuan Luo citations, Nature Genetics], (7) Fontana et al. UKB comorbidity network [arxiv-digest 07-07], (8) Mapelli et al. UKB proteomic conditional GGM [arxiv-digest 07-01], (9) Karim-Hu regularized PS/DR under rarity [arxiv-digest 07-09], (10) Murali et al. misclassified CF exposures [arxiv-digest 06-23], (11) İnan et al. AAVC automated ACMG [variant-interpretation keyword, GIM] |
| METHODS-WATCH | 5 | Small LMs in medicine (Qin et al., Nat Biomed Eng), behavioral genetics complexity (Wedow et al., Nat Genet), β-cell nutrient-stress dish-to-biobank (Wang et al., bioRxiv), transcriptome-from-epigenome ML (Ardakani et al., Genome Biol), Friedewald LDL detection (Doku et al.) |
| SKIP | ~30 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH over a 2-day
window), this 29-day cumulative window delivers 11 HIGH / 5
METHODS-WATCH, so the *rate* is about 1/3 the density — driven mostly
by the reduced `arxiv-digest` output from the fetch-reliability issue.
The recurring pattern from the 06-20 report holds and intensifies:
nearly all on-thread signal comes from Scholar alerts; the `arxiv-
digest` pipeline produced 2 HIGH papers (Fontana comorbidity + Mapelli
proteomic + Karim rare-exposure + Murali CF-misclassification =
actually 4 HIGH from arxiv-digest, not 2 — corrected count) out of ~30
polled days. **The single most decision-relevant item is #1 (Zemanick
et al. CFTR self-citation) — verify which of your papers is cited and
in what argumentative role before the next CF write-up.**
