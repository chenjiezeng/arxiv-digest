# Research digest report — 2026-07-29

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-23 12:00Z → 2026-07-29 06:37Z** (~6 days since the last
committed report at `reports/2026-07-23-research-digest.md`). A multi-day
catch-up window; expect a larger HIGH pool than the daily reports.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-07-24.md` → `2026-07-29.md`) | 07-24 → 07-29 (10:30Z crons) | Six daily digests. 07-25 and 07-26 empty; 07-24, 07-27, and 07-29 each surfaced 1 paper; 07-28 surfaced 3. Total = 6 unique papers this week, ranging score 1–2. Standouts: `oci-agent` (Chou/Kallus, causal-inference agentic pipeline, score 2) and GraphRareBench (HPO-driven rare-disease diagnosis benchmark). |
| NCBI "My NCBI What's New" — "All of Us" | 07-24, 07-25, 07-26, 07-27, 07-28 batches | Five daily AoU batches — 07-28 alone had 4 items; earlier days were dominated by the Lemieux JAMIA Open + Żebrowska circadian trio already reported 07-23. No new high-priority AoU-native GWAS this week. |
| NCBI "My NCBI What's New" — "UK Biobank" | 07-24, 07-25, 07-26, 07-27, 07-28 batches | Higher-volume feed — 07-28 alone carried 28 items. Real HIGH signal: multi-ancestry lipid-PRS multi-omics (Shan et al.), hematopoietic loss-of-Y × PAD (Li et al., CHIP-thread relevant), somatic-mutation contamination in germline studies (Ji et al.), CYP2D6 × early antidepressant discontinuation (Cohen et al., Psy-PGx pharmacogenomics). |
| NCBI "My NCBI What's New" — "drug repurposing" | 07-24 → 07-28 batches | Mostly infectious-disease / molecular-docking repurposing (Bunyaviruses, Oropouche, coronaviruses, Toxoplasma) — off-thread from the EHR-based / KG-based repurposing angles the interest file emphasizes. Two HIGH-adjacent: Huang & Ovcharenko deep-learning gene-regulation for drug prioritization, and Zhang et al. multi-transcriptomic ccRCC–hypertension comorbidity repurposing. |
| Google Scholar author + keyword feeds | 07-26, 07-27 (large batch) | Two feed-cluster fires — 07-26 (~15 alerts) mostly re-surfacing the Żebrowska circadian paper across Denny/Bastarache-adjacent feeds; 07-27 (~30 alerts) dominated by the HPRC2 pangenome bioRxiv (Lucas, Hebbar, Liao et al.), Feng cross-ancestry imaging pleiotropy for depression, and the Ma *Science* Alzheimer single-cell multiomics paper. One direct citation to Chenjie's colorectal work (Ma et al., *Eur J Histochem*). |
| Rare disease / mendelian keyword feeds | 07-26 | Song et al. LLM specialty-triage for rare disease (JMIR); García et al. variant curation & classification review — both routine (already tracked by wglab-adjacent methods class). |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and a
> snippet only — the reports below contextualize that metadata against
> your research threads; nothing here reflects full-text reading.
> `arxiv-digest` entries include the full abstract because the pipeline
> captures it.

---

## Executive summary

- **`oci-agent` — human-in-the-loop agentic workflow for observational
  causal inference (Netflix, Kallus lab).** Chou, Alexandre, Olds, Zhang,
  Kallus, *A Human-Augmenting Agentic Workflow for Observational Causal
  Inference* (arXiv 2607.22443, 07-24; `digests/2026-07-27.md`). Open-source
  Python package automating covariate-balance checking, PS trimming,
  sensitivity analysis; supports doubly-robust ATE, HTE estimation, and
  multiple continuous treatments via partially linear models. In use for
  ~100 analyses / month at Netflix since June 2026. Score 2 (propensity
  score + causal inference hits). Directly on the causal-inference &
  pharmacoepi thread — a serious reference implementation of the
  agentic-DR-ML pattern for observational studies. **HIGH — read first.**
- **GraphRareBench — HPO-driven rare-disease diagnostic benchmark with
  provenance-preserving evidence records.** Guo, Yang, Xu, Zheng, Sun, Li,
  *GraphRareBench: An Auditable Graph-Evidence Benchmark for
  Phenotype-Driven Rare-Disease Diagnosis* (arXiv 2607.24878, 07-27;
  `digests/2026-07-29.md`). 2,365 ontology-derived cases, 18,093
  target-confounder pairs, agent evaluation (Agents-A1, DeepSeek-V4-Flash)
  with target-evidence-coverage as a *separable* metric from MRR. Directly
  on the rare-disease + HPO threads; a natural benchmark to run
  Phenolyzer / Phen2Gene / PhenoSV / PhenoGPT2 against. **HIGH.**
- **Multi-Omics + PRS for lipid traits, multi-ancestry in UKB.** Shan,
  Qiu, Hou, Wang, *Multi-Omics Integration Improves Polygenic Risk
  Prediction for Lipid Traits: A Multi-Ancestry Study in UK Biobank*
  (*Genes* 2026-07-22; NCBI UKB feed 07-28). Cross-ancestry PGS + omics
  layering for lipids — directly on the trans-ancestry portability
  sub-thread and pairs with the Jo *et al.* East Asian meta-analysis
  flagged in the 07-23 report. **HIGH.**
- **Hematopoietic loss-of-Y (LOY) × symptomatic peripheral artery
  disease in men.** Li, Tang, Hussain, Liu, Qiu, Wang, Zhou, *Hematopoietic
  loss of Y chromosome and risk of symptomatic peripheral artery disease
  in men* (*Atherosclerosis* 2026-07-25; NCBI UKB feed 07-28). LOY is
  the male-specific analogue of CHIP as a somatic-mosaicism cardiovascular
  driver — directly on the CHIP/VEXAS/somatic-mosaicism disease thread,
  extending the phenotypic footprint from CAD/HF into PAD. **HIGH.**
- **CYP2D6 metabolizer phenotype × early antidepressant discontinuation
  in UKB — Psy-PGx consortium.** Cohen, Rebibo Demry, Young, Kleine
  Schaars, Juruena, Schulze, Kaprio, Psy-PGx Consortium, van Westrhenen,
  Shomron, *CYP2D6 Metabolizer Phenotype Is Associated with Early
  Antidepressant Discontinuation in the UK Biobank* (*Pharmaceuticals*
  2026-07-01; NCBI UKB feed 07-28). Pharmacogenomics + real-world
  medication-persistence outcome in UKB — a clean template for CFTR-
  modulator persistence, statin discontinuation, and other
  pharmacogenomic-persistence phenotypes in AoU/BioVU. **HIGH.**
- **Evaluating somatic mutational contamination in large-scale germline
  studies.** Ji, Bai, He, Yan, Wang, Tang, Chen, Cui, *Evaluating
  Somatic Mutational Contamination in Large-Scale Germline Genomic
  Studies* (*Biology (Basel)* 2026-07-21; NCBI UKB feed 07-28). Directly
  on the variant-interpretation QC thread — CHIP / clonal-mosaicism
  contamination is a persistent confound in UKB / AoU WES rare-variant
  scans. **HIGH (QC utility).**
- **Cell — longitudinal EHR data for cancer detection / treatment
  (International Consortium of Digital Twins).** Liu, Wang, Xu, Tang,
  Shen, ..., Loupy, Rasko, Ideker, Luo, Oermann, Zhang, *Advancing cancer
  detection and treatment using longitudinal routine clinical data*
  (*Cell* 2026-07-27; NCBI UKB feed 07-28). *Cell* paper on EHR-driven
  cancer trajectories — directly on the EHR-phenotyping + ML-for-precision-
  health threads, and touches the digital-twin literature the interest
  file's "ML for precision health" section flags. **HIGH (broad-audience
  landmark).**
- **Kopal et al. — mapping genetic convergence across brain structure,
  mental health, and cardiometabolic disease.** Kopal, Shadrin, van der
  Meer, Smeland, Stinson, Rødevand, Parker, O'Connell, Frei, Djurovic,
  Dale, Andreassen, *Mapping genetic convergence across brain structure,
  mental health, and cardiometabolic disease* (*Commun Med* 2026-07-27;
  NCBI UKB feed 07-28). Andreassen-lab shared-genetic-architecture
  triangulation across neuroimaging + psychiatric + cardiometabolic
  phecodes — pairs conceptually with the Streit *Nature Genetics* BPD
  paper from the 07-23 report (both are "psychiatric-GWAS ↔ somatic
  comorbidity" mappings). **HIGH.**
- **Feng et al. cross-ancestry pleiotropic imaging-derived phenotypes for
  depression risk stratification.** Feng, Guo, Huang, Jia, Hu, Yang,
  *Cross-ancestry pleiotropic analysis of imaging-derived phenotypes
  enhances risk stratification of depression* (*Molecular Psychiatry*
  2026; Scholar Denny related-research 07-27). Cross-ancestry pleiotropy
  design applied to depression + neuroimaging phenotypes — cleanly on
  the PRS + trans-ancestry portability thread. **HIGH.**
- **HPRC2 human pangenome reference.** Lucas, Hebbar, Liao, Macias-Velasco
  et al., *HPRC2: A human pangenome reference with near-complete coverage
  of common genetic variation* (bioRxiv 2026; Scholar Denny + Karczewski +
  Yang + Montgomery + Callahan feeds 07-27, quintuple-hit). Pangenome
  reference is a foundational-resource update. **HIGH (reference-update).**
- **Ran et al. — longitudinal plasma proteomics predicts phenoconversion
  to clinically manifest ALS.** Ran, Wuu, Qin, McDermott, Cooper-Knock,
  Li, Granit, Grignon, Lin, Fernandez, Colato, Carberry, Lill, Piazza,
  Malaspina, Benatar, *Longitudinal plasma proteomics predict phenoconversion
  to clinically manifest ALS* (*Nat Med* 2026-07-27; NCBI UKB feed 07-28).
  Proteomic-trajectory-to-clinical-onset design — a template for
  pre-clinical detection of monogenic-carrier phenoconversion (BRCA
  incident cancer, HTT preclinical HD, APOL1 CKD conversion). **HIGH
  (methods-template).**
- **oci-adjacent RCT-estimator selection framework (Parikh, Kallus, Jordan,
  Volfovsky).** Parikh, Levin-Konigsberg, Tripuraneni, Madeka, Jordan,
  Foster, Perrault-Joncas, Volfovsky, *Towards Optimal Estimators for
  Randomized Control Trials* (arXiv 2607.23254, 07-25; `digests/2026-07-28.md`).
  Sample-splitting framework for choosing among precision-enhancing RCT
  estimators (weighted least squares vs. difference-in-means) with
  asymptotic guarantees, on Amazon SCOT + Strengthening Democracy
  Challenge data. Score 1 (causal inference hit). On thread for the
  causal-inference / heterogeneous-treatment-effect sub-thread even
  though the datasets are non-clinical. **METHODS-WATCH.**
- **Deep-learning gene-regulation → drug prioritization (Huang &
  Ovcharenko).** Huang & Ovcharenko, *Using Deep Learning Models of Gene
  Regulation to Guide Drug Prioritization* (*Pharmaceuticals* 2026-07-16;
  NCBI drug-repurposing feed 07-28). Gene-regulation FM-driven drug
  prioritization — on the drug-repurposing thread (the interest file
  emphasizes explainable KG/GNN drug-repurposing pipelines). **MEDIUM-HIGH.**
- **Zhang et al. multi-transcriptomic repurposing for ccRCC × hypertension
  comorbidity.** Zhang, Kho, Wang, Lu, Zhu, Zhu, Wang, *Integrative
  Multi-Transcriptomic Uncovers Actionable Signatures and Drug Repurposing
  Candidates for ccRCC-Hypertension Comorbidity* (*Cancers* 2026-07-14;
  NCBI drug-repurposing feed 07-28). Comorbidity-driven repurposing is
  a live subclass; pairs with the multimorbidity-clustering thread.
  **MEDIUM.**

Everything else in this window is either off-thread (dietary indices,
brain imaging × pain MR spam, veterinary genomics, molecular-docking
repurposing for infectious disease), or a METHODS-WATCH-only entry
summarized in the tail section.

---

## Detailed reports

### 1. A Human-Augmenting Agentic Workflow for Observational Causal Inference (`oci-agent`)

**Authors.** Winston Chou, Adrien Alexandre, Lars Olds, Yi Zhang, Nathan Kallus (Netflix / Cornell).
**Venue.** arXiv preprint 2607.22443, submitted 2026-07-24.
**Signal source.** `arxiv-digest` `digests/2026-07-27.md` — score 2, keyword hits
`propensity score` + `causal inference`. Sole surfaced paper that day.
**Bucket.** HIGH.
**Threads served.** Causal inference and pharmacoepidemiology (agentic
DR-ML pipeline); ML for precision health (HTE estimation).

**What the paper does (from full abstract in the digest).** Introduces
`oci-agent`, an open-source Python package implementing a
human-in-the-loop agentic workflow for observational causal inference —
automating covariate-balance checking, propensity-score trimming, and
sensitivity analysis so the human can focus on question framing,
assumption scrutiny, and result interpretation. Initially open-sourced
June 2026 with doubly-robust ATE for a single binary treatment; since
extended to heterogeneous treatment effects and multiple continuous
treatments via partially linear models. Netflix internal-use metric:
"more than 100 analyses per month" since June. Reports outperformance
of unstructured baselines and parity with hand-tuned benchmarks across
public and internal evaluations.

**Why it matters for your work.**
1. **Agentic causal-inference pipelines are directly on-thread.** The
   causal-inference / pharmacoepi thread has been pattern-matching
   agentic-DR-ML frameworks for months — this is a reference
   implementation from the Kallus group (who wrote much of the
   contemporary DR-ML literature) at a company (Netflix) with genuine
   causal-inference-in-production experience. It's not a toy.
2. **HTE + multiple-continuous-treatment support is unusual in
   open-source packages.** Most contemporary causal-inference
   packages (EconML, DoWhy, CausalPy) either force you to a binary
   treatment or handle HTE via `EconML` wrappers with awkward
   ergonomics. `oci-agent` claiming native support for partially
   linear models over multiple continuous treatments is directly
   applicable to drug-dose-response and biomarker-as-exposure
   analyses in your pharmacoepi work.
3. **Pattern-match against Netflix's application domain — but the
   pipeline is domain-agnostic.** Netflix RCTs / observational
   studies of streaming behavior are structurally similar to
   EHR-linked biobank observational studies of medication effects:
   large N, high-dim covariates, treatment defined by observed
   behavior, outcome time-series. The `oci-agent` DR-ML +
   auto-diagnostics pipeline should port cleanly to AoU-based
   pharmacoepi (GLP-1 RA effects, SGLT2i effects, CFTR-modulator
   persistence).
4. **The human-in-the-loop framing is worth reading for the
   sociology of agent adoption.** How Netflix ended up with humans
   focused on "framing questions, scrutinizing assumptions, and
   evaluating diagnostics" while the agent does the mechanical
   work is a workflow model directly relevant to your own agentic
   research infrastructure (arxiv-digest itself, PheTK-adjacent
   pipelines).

**Follow-ups.** Pull the paper; check (a) which DR-ML backbone is used
(EconML DR-Learner? CausalML? R-Learner? in-house?), (b) how covariate
balance is auto-checked (SMD thresholds? c-statistic?), (c) whether
sensitivity analysis is E-value-based or Rosenbaum bounds, (d) GitHub
license and reproducibility, (e) whether the "100 analyses / month"
number is public via a Netflix tech blog. Then: try a minimal
`oci-agent` run on an AoU-derived GLP-1 RA vs. metformin cohort
alongside a hand-tuned baseline (PheTK-based cohort build → DR-ML in
`EconML`) to benchmark ergonomics + fidelity of the agentic diagnostics.

---

### 2. GraphRareBench: An Auditable Graph-Evidence Benchmark for Phenotype-Driven Rare-Disease Diagnosis

**Authors.** Guiling Guo, Jia Yang, Jiahao Xu, Shuyuan Zheng, Zhonghai Sun, Qiyuan Li.
**Venue.** arXiv preprint 2607.24878, submitted 2026-07-27.
**Signal source.** `arxiv-digest` `digests/2026-07-29.md` — score 1,
keyword hit `hpo`. Sole surfaced paper that day (2 previously-surfaced
suppressed).
**Bucket.** HIGH.
**Threads served.** Rare disease (phenotype-driven diagnosis); HPO /
ontology thread; knowledge graphs (evidence-grounded graph reasoning);
methods-watch for LLM-agent evaluation.

**What the paper does (from full abstract in the digest).** Introduces
a benchmark of **2,365 ontology-derived rare-disease cases with 18,093
target-confounder pairs**, where each case comprises a coarsened HPO
query, a fixed candidate pool, graph-defined *hard confounders*, and
source-linked evidence records. On a 237-case gene-component-disjoint
test split, supervised rankers over a shared 21-feature interface
reach MRRs of 0.640–0.740, with case-averaged target-over-confounder
accuracies of 0.898–0.916. Two agentic systems — Agents-A1 and
DeepSeek-V4-Flash — achieve MRRs of 0.746 and 0.718 respectively (paired
difference not statistically significant), but their *target-evidence
coverage* differs by 0.561 — meaning near-identical ranking accuracy
but very different evidence access. A telling observation: on
Hit@10-successful cases, **22.1%–43.7% still ranked at least one
graph-defined hard confounder above the target** — MRR flatters the
underlying failure mode. The authors argue full-pool retrieval,
hard-confounder discrimination, and observable evidence access are
three separable dimensions of model behavior that need to be measured
independently. Code + data at
`https://github.com/GUI0609/GraphRareBench`.

**Why it matters for your work.**
1. **The evaluation framework — separating ranking accuracy from
   evidence-coverage — is portable.** Every phenotype-driven
   diagnostic tool (Phenolyzer, Phen2Gene, PhenoSV, LIRICAL, Exomiser,
   PhenoGPT/PhenoGPT2 from the wglab lineage) reports rank / MRR
   only. The graph-defined-hard-confounder + evidence-coverage
   metrics let you distinguish "ranked correctly but by accident"
   from "ranked correctly with the right supporting evidence chain."
   Directly relevant to any HPO-driven pipeline benchmarking work in
   the rare-disease thread.
2. **2,365-case benchmark is a middleweight — bigger than Exomiser's
   original benchmark, smaller than the full Undiagnosed Diseases
   Network cohort — so easy to run new tools against.** A natural
   next step is to run PhenoGPT2 and the Phen2Gene / PhenoSV toolchain
   through GraphRareBench and publish the head-to-head — that's a
   short methods-note-scale paper that would map cleanly onto the
   rare-disease sub-thread and the wglab-lineage skill.
3. **Ontology-derived → auditable is on the "explainable rare-disease
   diagnosis" thread.** Interest file explicitly flags KG/GNN
   approaches with **explainable hypothesis output (path or subgraph
   rationales rather than opaque link-prediction scores)** as the
   drug-repurposing preference — the same principle applies to
   diagnosis, and GraphRareBench operationalizes it by making
   *evidence records* first-class objects in the benchmark.
4. **The 22–44% "Hit@10 hides ranking-of-confounders" finding is a
   red flag for existing benchmarks.** If it replicates on other
   tools, it argues that the field's dominant metric (top-K recall)
   systematically under-diagnoses failure modes — the kind of QC
   argument the interest file's "how to make interpretability
   claims rigorous" theme has been circling.

**Follow-ups.** Pull the paper; check (a) which HPO release / version
was used for the coarsening protocol, (b) the 21-feature interface —
what standard features are shared across supervised rankers, (c) how
"graph-defined hard confounders" are constructed (shared HPO-term
overlap? shared gene-neighborhood?), (d) full Agents-A1 configuration
(is it a shared-agent framework or paper-specific?), (e) whether the
GitHub release includes both cases and rankings for reproducibility.
Then: benchmark PhenoGPT2, Phen2Gene, and LIRICAL on the 237-case test
split; report evidence-coverage separately from MRR to test whether
the 22–44%-confounder observation generalizes.

---

### 3. Multi-Omics Integration Improves Polygenic Risk Prediction for Lipid Traits: A Multi-Ancestry Study in UK Biobank

**Authors.** Nan Shan, Yiwei Qiu, Lei Hou, Zhengming Wang.
**Venue.** *Genes (Basel)* 17(7):840, 2026-07-22 (PMID 42510880).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed" (07-28
15:18Z; item 15 of 28).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (PRS + multi-omics stacking);
biobanks with EHR linkage (UKB); trans-ancestry portability.

**What the paper does (from title + venue).** Extends standard PGS
lipid-trait prediction (LDL, HDL, TG, TC) in the UKB with multi-omics
layers (likely metabolomics / proteomics — the *Genes* venue and
UKB provenance make this a Nightingale-metabolomics or Olink-proteomics
integration play), stratified across multi-ancestry subpopulations of
UKB. The claim in the title is that omics-integrated PRS beats PRS-only
prediction — the interesting parameter is whether that improvement
holds cross-ancestry.

**Why it matters for your work.**
1. **PRS + omics stacking is a direct extension of the "composite
   risk" sub-thread** already flagged around Baya *AJHG*, Souaiaia
   *Nature*, and Vazquez *Genetics* in earlier reports. Adds omics
   as a third axis alongside PGS and rare pathogenic variants.
   Directly applicable to cardiometabolic-carrier phenotypes in AoU
   (which has Olink proteomics rolling out) and hereditary-cancer
   modifier work.
2. **Multi-ancestry framing is the discriminator.** Cross-ancestry
   PGS portability is one of the harder open problems; if omics
   integration attenuates the drop-off in non-European ancestries,
   that's a genuinely useful methodological contribution — pairs
   with the Jo *et al.* East Asian meta-analysis (07-23 report) and
   the Kore *et al.* local-ancestry rare-variant paper (07-22
   report) to give a fuller picture of the trans-ancestry-portability
   toolkit.
3. **Lipid traits are a natural test-bed** because the effect sizes
   are large, the PGS is mature, and multi-omics quantification is
   well-established (Nightingale NMR, Olink) — so any omics-integration
   improvement over the PRS-only baseline is credible.

**Follow-ups.** Pull the paper; check (a) which omics layer is used
(Nightingale NMR? Olink? liver-tissue proxy metabolomics?), (b) the
integration architecture (concatenation? two-stage?
stacked-regression?), (c) whether it uses PRSice / LDpred2 / PRS-CS
as the base PGS, (d) ancestry-stratified R² deltas relative to
PGS-only baseline, (e) whether the omics-integrated model transfers
across ancestries without omics-panel re-training.

---

### 4. Hematopoietic Loss of Y Chromosome and Risk of Symptomatic Peripheral Artery Disease in Men

**Authors.** Chao Li, Dan Tang, Salman M Hussain, Kai Liu, Peijun Qiu, Ruimeng Wang, Zheng Zhou.
**Venue.** *Atherosclerosis* 420:121859, 2026-07-25 (online ahead of print; PMID 42508147).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed" (07-28
15:18Z; item 25 of 28).
**Bucket.** HIGH.
**Threads served.** Clonal hematopoiesis (CHIP) and somatic-mosaicism
disease thread — LOY is the male-specific analogue; genetic
epidemiology; biobanks with EHR linkage (UKB).

**What the paper does (from title + venue).** Tests the association
between hematopoietic **mosaic loss of Y chromosome (mLOY)** and
symptomatic peripheral artery disease (PAD) in men, almost certainly
in UKB (given the NCBI-UKB-feed provenance). PAD is a well-defined
UKB EHR outcome (ICD-10 I73.9, I74.x; procedural OPCS-4 codes for
lower-limb revascularization). LOY is inferred from array data via
BAF/LRR shifts on chromosome Y — the standard method (Thompson
*Nature* 2019, Kessler *Nature* 2022).

**Why it matters for your work.**
1. **LOY is the male-specific complement to CHIP** as a somatic-mosaicism
   cardiovascular driver. The interest file's CHIP/VEXAS thread has
   been tracking cardiovascular and hematologic outcomes — this
   paper extends the phenotypic footprint from CAD/HF (Loh *Nature*
   2018) into PAD, which is an underexplored outcome for LOY.
2. **PAD is an EHR-derived phenotype that's easy to define in AoU** —
   pairs cleanly with a natural follow-up: replicate the LOY×PAD
   association in AoU's ~245k WGS + ~245k array subset, and then
   run PheWAS-style analyses of LOY across the phecode space
   (something the interest file's PheWAS thread would prioritize).
3. **Somatic-mosaicism × cardiovascular is where CHIP work is
   headed clinically** — the interest file explicitly calls out
   "cardiovascular and hematologic outcomes" of CHIP/VEXAS. LOY is
   ~7% prevalence in men over 70 in UKB, making it a common enough
   exposure that PheWAS across the phecode space is well-powered.

**Follow-ups.** Pull the paper; check (a) LOY calling method (mLRRY?
MoChA?), (b) LOY threshold / cell-fraction cutoff, (c) PAD definition
(ICD only? OPCS revascularization included? ABI-based?), (d) whether
they adjust for smoking (LOY is strongly smoking-associated —
mediation vs. confounding is the key question), (e) HR effect sizes
by LOY cell fraction bin.

---

### 5. CYP2D6 Metabolizer Phenotype Is Associated with Early Antidepressant Discontinuation in the UK Biobank

**Authors.** T Cohen, E Rebibo Demry, AH Young, K Kleine Schaars, M Juruena, TG Schulze, J Kaprio, Psy-PGx Consortium, R van Westrhenen, N Shomron.
**Venue.** *Pharmaceuticals (Basel)* 19(7):1028, 2026-07-01 (PMID 42515713).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed" (07-28
15:18Z; item 8 of 28).
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi (medication-persistence
outcomes); pharmacogenomics; biobanks with EHR linkage (UKB).

**What the paper does (from title + venue).** UKB-based analysis
(Psy-PGx Consortium) testing whether CYP2D6 metabolizer phenotype
(poor / intermediate / normal / ultra-rapid — inferred from imputed
star-allele genotypes) predicts **early antidepressant discontinuation**
— a real-world persistence outcome derived from UKB prescription /
primary-care records. Kaprio (FinnGen) and Schulze (BiDirect) on the
author list place this in the Psy-PGx consortium's cross-cohort
antidepressant-persistence lineage.

**Why it matters for your work.**
1. **Medication-persistence-as-outcome is an EHR-native phenotype**
   that the pharmacoepi thread should be tracking more heavily.
   Discontinuation timing, gaps between refills, and MPR are all
   derivable from AoU's prescription table and BioVU's medication
   codes. This paper is a template for CFTR-modulator persistence,
   statin discontinuation, HRT persistence, and GLP-1 RA persistence
   — all of which are on the interest file.
2. **CYP2D6 star-allele inference from arrays is now standard** but
   still poorly validated at the phenotype level. This paper adds
   one more piece of the phenotypic-consequence evidence base —
   worth reading for the star-allele → metabolizer-phenotype
   inference procedure (which one they use: PharmVar, PharmGKB,
   Aldy, StellarPGx).
3. **Persistence outcomes are less confounded by
   indication-selection than efficacy outcomes** — a pragmatic
   reason to use them for pharmacogenomic-×-drug interaction
   tests, since the persistence event doesn't require you to
   pin down the initial indication precisely. Directly relevant
   to the pharmacoepi thread's causal-identification concerns.

**Follow-ups.** Pull the paper; check (a) CYP2D6 star-allele
inference tool, (b) discontinuation window (30-day gap? 90-day?),
(c) which antidepressants are pooled (SSRIs only? TCAs?), (d) whether
they account for physician-clustering, (e) whether the Psy-PGx
consortium releases the UKB-derived phenotype for replication.

---

### 6. Evaluating Somatic Mutational Contamination in Large-Scale Germline Genomic Studies

**Authors.** Xiao Ji, Xiaoxiang Bai, Guangchuang He, Kai Yan, Enze Wang, Yi-Da Tang, Lin Chen, Qinghua Cui.
**Venue.** *Biology (Basel)* 15(14):1204, 2026-07-21 (PMID 42510750).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed" (07-28
15:18Z; item 17 of 28).
**Bucket.** HIGH (QC utility).
**Threads served.** Variant interpretation (QC layer); genetic
epidemiology (CHIP-contamination in germline scans); CHIP thread.

**What the paper does (from title + venue).** A QC / methods paper
evaluating how much somatic-mutational contamination (primarily
CHIP-derived) leaks into large-scale germline association scans and
biases rare-variant burden estimates. Almost certainly benchmarked
against UKB WES/WGS given the NCBI-UKB feed provenance.

**Why it matters for your work.**
1. **CHIP contamination is the single most under-reported confound
   in UKB rare-variant scans.** It preferentially inflates apparent
   effects for genes on the CHIP-mutation "hotlist" (DNMT3A, TET2,
   ASXL1, TP53, JAK2) and depresses effects for genes whose apparent
   pLoF rate is inflated by clonal expansion in blood. Every burden
   scan on the pLoF-methods thread would benefit from this being an
   explicit QC step. Directly on the variant-interpretation +
   CHIP-VEXAS threads.
2. **Portable to AoU.** AoU WGS calls are subject to the same
   contamination risk. A natural extension is to test whether the
   Ji et al. QC approach flags AoU-specific hotspot variants
   before they contaminate downstream PheWAS burden analyses.
3. **Directly protects the composite-risk methodology** the
   genetic-epi thread cares about — misclassifying somatic
   variants as germline pathogenic biases carrier-status
   assignment and hence any PGS × rare-variant analysis.

**Follow-ups.** Pull the paper; check (a) which contamination-detection
metric they use (VAF distribution? paired-tissue heteroplasmy? blood-vs-buccal
comparison?), (b) recommended VAF thresholds by variant type, (c) whether
they provide a callable Python / R tool, (d) list of affected genes /
regions.

---

### 7. Advancing cancer detection and treatment using longitudinal routine clinical data

**Authors.** F Liu, K Wang, H Xu, C Tang, X Shen, M Wang, L Yang, L Yang, L Liu, C Hu, G Li, W Wu, Z Zou, B Li, S Liu, J Kang, J Kong, T Li, IN Wong, X Huang, G Chen, W Lu, I Ziyar, CL Zhang, Y Sun, W Lin, C Ou, M Fok, T Hou, W Wang, K Xue, Y Yin, H Zhu, J Gootenberg, OO Abudayyeh, M Karin, A Loupy, JEJ Rasko, T Ideker, H Luo, E Oermann, K Zhang; International Consortium of Digital Twins in Healthcare and Medicine.
**Venue.** *Cell* — online ahead of print 2026-07-27 (S0092-8674(26)00807-X; PMID 42508404).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed" (07-28
15:18Z; item 24 of 28).
**Bucket.** HIGH (broad-audience landmark).
**Threads served.** EHR phenotyping & OMOP; ML for precision health;
biobanks with EHR linkage (UKB — implied by the NCBI-UKB feed catch).

**What the paper does (from title + author panel).** A *Cell* paper
under the "International Consortium of Digital Twins in Healthcare and
Medicine" banner, framed as advancing cancer detection and treatment
using longitudinal routine clinical data. Kang Zhang as senior; Trey
Ideker (network biology, digital twins), Michael Karin (cancer
inflammation), Alexandre Loupy (transplant / RWD), John Rasko (gene
therapy) on the author list — a broad panel that suggests this is a
review-plus-roadmap paper anchoring the digital-twins-in-healthcare
research agenda. Anthony Gootenberg / Omar Abudayyeh on the CRISPR
side; Eric Oermann on the ML side.

**Why it matters for your work.**
1. **Digital twins from EHR data is the conceptual endgame** of
   the ML-for-precision-health thread. This *Cell* paper will
   become one of the most-cited framing references for anyone
   pitching an EHR-foundation-model + individualized-risk-prediction
   research program in the next 12 months.
2. **UKB is one of the benchmark cohorts** — the NCBI UKB feed
   catch implies the paper uses UKB data in at least one demonstration.
   Worth reading for the specific UKB use case they highlight and
   whether the framework's applicability to AoU is explicit.
3. **The author panel bridges biology (Karin, Ideker) and
   clinical AI (Zhang, Oermann)** — the interdisciplinary
   framing signals that the paper is positioning digital twins
   as a bridge concept between systems biology and clinical
   deployment. Directly on the "ML for precision health, tied
   to a clinical decision" framing in the interest file.
4. **Cell landing is a signal that the digital-twins subfield has
   reached mainstream biomedical acceptance** — worth citing
   whenever you write a grant aim referencing digital-twin /
   individualized-risk methodology.

**Follow-ups.** Pull the paper; note (a) the concrete digital-twin
architecture (variational autoencoder over trajectories?
sequence-to-sequence over EHR events? counterfactual generation?),
(b) which cancers are the primary demonstrations, (c) the UKB use
case specifically, (d) whether they release code / models, (e) how
they handle the identifiability challenge of digital-twin
counterfactuals.

---

### 8. Mapping Genetic Convergence across Brain Structure, Mental Health, and Cardiometabolic Disease

**Authors.** J Kopal, AA Shadrin, D van der Meer, OB Smeland, SE Stinson, L Rødevand, N Parker, KS O'Connell, O Frei, S Djurovic, AM Dale, OA Andreassen.
**Venue.** *Communications Medicine* 6(1):416, 2026-07-27 (PMID 42509310).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed" (07-28
15:18Z; item 22 of 28).
**Bucket.** HIGH.
**Threads served.** Multimorbidity / chronic-disease clustering; genetic
epidemiology (cross-trait shared genetic architecture); biobanks with
EHR linkage (UKB imaging + phecodes).

**What the paper does (from title + venue).** Cross-trait shared-genetic-architecture analysis linking (a) UKB brain-imaging-derived phenotypes,
(b) psychiatric outcomes, and (c) cardiometabolic disease. Andreassen
lab has been the leader in the MiXeR / bivariate-causal-mixture-model
approach to shared genetic architecture; this paper likely applies that
methodology to a three-way convergence pattern with imaging as the
biological substrate. Dale on the ADNI/UKB imaging side; Stinson on the
cardiometabolic side; Shadrin/Frei on the MiXeR methodology.

**Why it matters for your work.**
1. **Directly on the multimorbidity thread** — the interest file
   flags "cardiometabolic disease, autoimmune disease, or
   aging-related multimorbidity" for chronic-disease clustering.
   This paper uses genetic architecture (rather than EHR
   co-occurrence) as the shared substrate, which is a complementary
   approach to phenotype-based clustering.
2. **Bridges to the Streit BPD paper (07-23 report).** Streit
   showed BPD-PGS is associated with COPD phecode in BioVU + UKB
   — a psychiatric-PGS × somatic-outcome pattern. Kopal et al. do
   the same three-way triangulation more broadly, with brain
   imaging as the missing intermediate biological layer. Reading
   the two together gives you the neurogenetic-architecture-cardiometabolic
   triangle in one sitting.
3. **Andreassen lab is the reference class for cross-trait shared
   genetic architecture.** MiXeR, bivariate causal-mixture models,
   and conditional/conjunctional FDR are all this group's tools —
   worth reading for methodological updates you might want to
   apply to hereditary-cancer × cardiometabolic multimorbidity
   analyses in AoU.

**Follow-ups.** Pull the paper; check (a) MiXeR vs. newer method
(what's the specific model?), (b) which imaging phenotypes were
included (structural? functional? both?), (c) which psychiatric
diagnoses were included (specifically BPD, MDD, SCZ?), (d) which
cardiometabolic outcomes (specifically T2D, MI, HTN?), (e) the
biological interpretability of the shared components.

---

### 9. Cross-Ancestry Pleiotropic Analysis of Imaging-Derived Phenotypes Enhances Risk Stratification of Depression

**Authors.** Y Feng, X Guo, P Huang, N Jia, S Hu, S Yang.
**Venue.** *Molecular Psychiatry*, 2026 (in press).
**Signal source.** Google Scholar author-feed for Joshua C. Denny —
new related research (07-27 14:34Z).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (cross-ancestry PGS); biobanks
with EHR linkage (UKB / ENIGMA / East Asian cohorts implied);
ML for precision health (risk stratification).

**What the paper does (from title + snippet).** Cross-ancestry
pleiotropic analysis of neuroimaging-derived phenotypes (IDPs) to
build a depression-risk-stratification tool. The design uses
neuroimaging as an intermediate phenotype layer to boost PRS
portability across ancestries — a variation on the omics-augmented
PRS design that Shan et al. use for lipids (this report's #3), but
with IDPs instead of omics.

**Why it matters for your work.**
1. **Cross-ancestry PGS portability continues to be a hard
   problem.** IDPs as an intermediate biological substrate is a
   plausible portability booster because neuroimaging effect sizes
   are less ancestry-dependent than SNP effect sizes. Directly on
   the trans-ancestry portability sub-thread.
2. **Depression is the phenotype of interest** — worth checking
   whether the underlying depression definitions are PHQ-9-derived,
   EHR-derived, or interview-based, because depression phenotyping
   is a persistent friction point in cross-cohort work.
3. **Pattern-matches the composite-risk pipeline** — PGS + imaging
   substrate + risk stratification is a natural template for
   psychiatric-comorbidity work in hereditary-cancer or CFTR
   populations, where imaging is often available.

**Follow-ups.** Pull the paper; check (a) discovery cohort ancestry
composition, (b) IDP selection (structural? DTI? functional?), (c)
the specific cross-ancestry pleiotropy method (MTAG? PLEIO?
cross-population PRS?), (d) risk-stratification net benefit vs. PRS
alone (calibration plots, decision-curve analysis).

---

### 10. HPRC2 — Human Pangenome Reference with Near-Complete Coverage of Common Genetic Variation

**Authors.** JK Lucas, P Hebbar, WW Liao, JF Macias-Velasco et al. (HPRC).
**Venue.** bioRxiv, 2026.
**Signal source.** Google Scholar — surfaces across FIVE author-feeds
on 07-27: Denny + Karczewski + Yang + Montgomery + Callahan
related-research. Quintuple-hit — near-universal signal.
**Bucket.** HIGH (reference-update).
**Threads served.** Variant interpretation (pangenome-informed variant
calling); genetic epidemiology (reference infrastructure); biobanks
with EHR linkage (all downstream biobank analyses).

**What the paper does (from title + snippet).** HPRC v2 pangenome
reference — updated draft human pangenome with near-complete coverage
of common genetic variation. The v1 draft was Liao *Nature* 2023; v2
is an accuracy / completeness update, presumably with more assemblies
(v1 had 47, v2 likely 100+) and improved variant coverage.

**Why it matters for your work.**
1. **Pangenome-based variant calling changes rare-variant
   interpretation.** Reference-bias effects on variant calling —
   particularly in non-European ancestries — are the fundamental
   reason PGS portability drops off. A better pangenome reference
   directly reduces reference bias and hence improves rare-variant
   discovery and PGS transfer.
2. **Quintuple-hit across author feeds signals field-wide
   importance.** Denny (biobanks), Karczewski (gnomAD), Yang
   (statistical genetics), Montgomery (functional genomics),
   Callahan (biomedical KGs) — every subfield your interest file
   tracks flagged this paper. That's a canonical reference-update
   signal.
3. **AoU / UKB downstream applicability.** Whenever AoU or UKB
   updates their variant-calling pipeline to a new reference, PGS
   coefficients need re-training. HPRC2 is a leading candidate for
   the next reference update.

**Follow-ups.** Pull the bioRxiv; check (a) v1 → v2 assembly-count
delta, (b) added ancestries, (c) benchmark rare-variant discovery
in previously under-represented ancestries, (d) which release
schedule / IGV support is planned.

---

### 11. Longitudinal Plasma Proteomics Predict Phenoconversion to Clinically Manifest ALS

**Authors.** X Ran, J Wuu, ZS Qin, MP McDermott, J Cooper-Knock, Y Li, V Granit, AL Grignon, E Lin, MC Fernandez, D Colato, N Carberry, CM Lill, P Piazza, A Malaspina, M Benatar.
**Venue.** *Nature Medicine*, online ahead of print 2026-07-27 (PMID 42509371).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed" (07-28
15:18Z; item 21 of 28).
**Bucket.** HIGH (methods-template).
**Threads served.** ML for precision health (individualized risk +
biomarker trajectories); rare disease (ALS as monogenic-carrier-adjacent
phenotype); pharmacoepi (biomarker-guided decision-support).

**What the paper does (from title + venue).** *Nature Medicine* paper
demonstrating that **longitudinal plasma-proteomic trajectories**
predict *phenoconversion* — the transition from pre-symptomatic
carrier state to clinically manifest ALS. Benatar lab (Pre-fALS
cohort) as senior; Cooper-Knock and Lill add UK and German
consortium data; the study is likely built on serial-sampling
cohorts of C9orf72 and SOD1 pre-symptomatic carriers.

**Why it matters for your work.**
1. **Phenoconversion prediction from longitudinal proteomics is a
   directly portable methodology** to other pre-symptomatic carrier
   cohorts — BRCA1/2 incident cancer, HTT preclinical HD, APOL1
   CKD conversion, hereditary-cancer syndromes generally. The
   design (serial biomarker sampling → time-varying-covariate
   survival model or ML equivalent) is the template.
2. **UKB Olink proteomics on ~53k participants** (with additional
   panels on the way) makes this exact design tractable in UKB
   itself — a natural next step is to test whether the ALS
   phenoconversion proteomic signature is detectable in the UKB
   incident-ALS subcohort as an external validation.
3. **Bridges rare-disease and precision-medicine threads.** ALS
   is rare-disease-adjacent (~5% clearly Mendelian, most
   sporadic); the pre-symptomatic-carrier framework is the same
   whether the "carrier" is genetic (C9orf72 expansion) or
   biomarker-defined (proteomic signature). A conceptual bridge
   worth citing when framing hereditary-cancer pre-clinical
   detection work.

**Follow-ups.** Pull the paper; check (a) proteomic-panel platform
(Olink? SomaScan?), (b) discovery vs. replication cohort composition,
(c) the specific ML architecture for trajectory prediction, (d)
lead-time distribution (how many months / years pre-onset), (e) UKB
replication feasibility (Olink Explore 3072).

---

## METHODS-WATCH (short entries)

### `arxiv-digest` 2026-07-28 — Towards Optimal Estimators for Randomized Control Trials
**Authors.** Harsh Parikh, Gabriel Levin-Konigsberg, Nilesh Tripuraneni, Dhruv Madeka, Michael I. Jordan, Dean Foster, Dominique Perrault-Joncas, Alexander Volfovsky (Amazon SCOT + Berkeley + Duke).
**Signal.** `arxiv-digest` today, keyword `causal inference`, score 1.
**Take.** Sample-splitting framework for estimator selection across
families of RCTs, with asymptotic guarantees. Demonstrated on Amazon
SCOT trials and the Strengthening Democracy Challenge dataset. Key
finding: **weighted least squares dominates for inference goals,
difference-in-means minimizes regret for decision goals** — the
estimator that's best for a hypothesis test is not the estimator
that's best for a policy decision. On thread for the causal-inference
sub-thread even though the datasets are non-clinical; the
optimal-estimator-per-family framing is directly portable to
target-trial-emulation methodological work. **METHODS-WATCH.**

### `arxiv-digest` 2026-07-28 — TCellAlign
**Authors.** Pengyu Xie, Rongjia Zhou, Zhilin Ou, Junyuan Zhang, Xiang Zhou, Xiaobo Sun, Jiaying Lu, Wenjing Ma (q-bio.QM).
**Signal.** `arxiv-digest` today, keyword `foundation model`, score 1.
**Take.** Multi-agent workflow (literature retrieval + info extraction +
nomenclature-guided label alignment + evidence-based adjudication) for
cross-study T-cell population alignment against Cell Ontology / CZ
CELLxGENE annotations. Benchmark dataset spans 44 studies / 7M cells.
Off the primary disease threads, but the multi-agent evidence-adjudication
pattern is a portable template for ontology-alignment work — including
HPO term harmonization across rare-disease databases. **METHODS-WATCH.**

### `arxiv-digest` 2026-07-28 — SCTA (Single-Cell Target Agent)
**Authors.** Shuyu Chen, Chen Zhu, Ye Zhang, Yang Li, Qiqi Xie, Haohan Wang (cs.LG).
**Signal.** `arxiv-digest` today, keyword `precision medicine`, score 1.
**Take.** Decision-centric agentic framework for single-cell target
discovery from scRNA-seq. Decomposes the pipeline into specialized
agents aligned with key decision points (preprocessing → cell
population selection → DE analysis → biological interpretation). Case
study on hereditary chronic pancreatitis. The **decision-aware agent
decomposition** pattern is portable to phenotype-driven analysis
workflows including PheTK-based PheWAS. Off-thread for the primary
disease list but on the ML-for-precision-health thread. **METHODS-WATCH.**

### `arxiv-digest` 2026-07-24 — scContam: auditing pretraining contamination in single-cell foundation models
**Authors.** Sarwan Ali (q-bio.GN).
**Signal.** `arxiv-digest` 07-24, keyword `foundation model`, score 1.
**Take.** MinHash-based fingerprint + loss-based membership-inference
attack (MIA-scFM) for detecting pretraining-corpus overlap in scFM
benchmarks. Finds 80.4% and 77.0% pretraining-overlap evidence in
PBMC 3k and CELLxGENE pancreatic islets respectively — two of the
most-cited scFM benchmarks. AIDA v2 / Tahoe-100M post-cutoff datasets
show 0% overlap. Directly relevant to the EHR-foundation-model thread's
"contamination audits should accompany benchmark reporting" theme
— cleanly portable to CLMBR / MOTOR / MEDS benchmark evaluation.
**METHODS-WATCH — high strategic value for the EHR-FM thread.**

### `arxiv-digest` 2026-07-23 — Plausibility-Driven Prioritization of Candidate Biomedical Annotations
(Already covered in 07-23 report; noted here only for continuity.)

### NCBI drug-repurposing — Huang & Ovcharenko, deep-learning gene regulation for drug prioritization
**Authors.** Xin Huang, Ivan Ovcharenko (NCBI/NIH).
**Venue.** *Pharmaceuticals (Basel)* 19(7):1097, 2026-07-16.
**Take.** Uses deep-learning models of gene regulation (likely
Enformer / DNABERT / Nucleotide Transformer family) to guide drug
prioritization. On the drug-repurposing sub-thread; the interest file
prefers explainable KG/GNN approaches, but a gene-regulation FM
prioritization pipeline is a complementary axis. **MEDIUM-HIGH** in
the drug-repurposing sub-thread.

### NCBI drug-repurposing — Zhang et al., ccRCC × hypertension comorbidity repurposing
**Authors.** Y Zhang, BS Kho, X Wang, H Lu, M Zhu, R Zhu, Y Wang.
**Venue.** *Cancers* 18(14):2250, 2026-07-14.
**Take.** Multi-transcriptomic integration to identify repurposing
candidates for ccRCC-hypertension comorbidity. Comorbidity-driven
repurposing is a live sub-class; pairs with the multimorbidity /
disease-clustering thread. **MEDIUM.**

### NCBI drug-repurposing — Repurposing small-molecule inhibitors against Bunyaviruses (Liu et al., *Curr Med Chem*)
**Take.** Molecular-docking / structural review — off the EHR-based
repurposing angle the interest file emphasizes. **SKIP.**

### NCBI drug-repurposing — Drug Repurposing as a Broad-Spectrum Strategy Against Coronaviruses (Du et al., *Viruses*)
**Take.** Infectious-disease repurposing review — off-thread. **SKIP.**

---

## Off-thread / SKIP (representative — not exhaustive)

- Multiple UKB dietary-index → outcome papers (WCRF/AICR × lung cancer,
  vitamin C × MS, vitamin D × infection hospitalization, dietary
  flavonoids × AAA, sugar rationing × early-onset cancer) — routine
  UKB nutrition-epi, no thread-crossover.
- Multiple UKB imaging-MR × phenotype papers (brain functional networks
  × stroke recovery, brain imaging-wide × site-specific pain, depression
  × Alzheimer's MR, macular thickness × AMD) — routine MR methodology,
  no thread-crossover.
- Comparative insulin-resistance indices × hyperuricemia CV risk (UKB
  + Shanghai Pudong), fracture-PRS × FRAX validation, BMI-SBP trajectory
  multi-omics for HF subtyping — cardiometabolic epi, standard.
- Non-clinical animal-genomics feeds (Bombus, kingfish, snake
  phylogeography, veterinary eQTL in pigs) — spillover from Yang /
  Montgomery author feeds.
- Ma et al. *Science* single-cell multiomics in AD (Jian Ma feed) —
  neuroscience methods paper; off the clinical PheWAS / EHR thread but
  a notable *Science* landing.
- Zhou et al. *Science* human body single-cell 3D genome + methylation
  atlas (Snyder feed) — off-thread genomics methods paper.
- Grant et al. *Science* three-dimensional chromatin × heart disease
  TF (Bing Ren feed) — off-thread developmental genomics.
- Layeghifard et al. *Nature* prior-therapy mutation profiles in
  childhood cancer relapse (Karczewski citation feed) — off-thread
  pediatric oncology methods.
- LncRNA RP11-708J19.2 promotes CRC progression via SIRT7 (Ma et al.,
  *Eur J Histochem*, 07-27) — a **direct citation to Chenjie's
  colorectal work** but the paper itself is molecular biology, not
  on any active methods thread. Cite-count noted; skip for detailed
  reading.
- Song et al. LLM initial-visit specialty triage in rare disease
  (*JMIR*, 07-26) — rare-disease-adjacent but the LLM-triage angle
  is far from the phenotype-driven-diagnosis focus of the interest
  file. **SKIP for now.**
- García et al. variant curation & classification for rare disease
  SNVs (*Arch Med Res*, 07-26) — a general review, no primary
  methodological contribution. **SKIP.**
- Van der Velden et al. PSMA imaging in mCSPC (CAPRI-3 registry,
  Chenjie related-research feed) — pattern-matches Chenjie's
  prostate-cancer-imaging background but the current interest file
  is methods-heavy rather than clinical oncology. **SKIP.**

---

*Prepared 2026-07-29 for the multi-day window 2026-07-23 → 2026-07-29.
Full `arxiv-digest` for today at `digests/2026-07-29.md` (1 paper).
Next report expected as new signal accumulates.*
