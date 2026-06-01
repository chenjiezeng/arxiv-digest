# Research digest report — 2026-05-29

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | ~2026-05-24 → 05-29 | Author alerts (Denny, Bick, Bastarache, Callahan, Karczewski, Hripcsak, Ryan, Montgomery, Celi, Brandt, …) + keyword alerts (UK Biobank, All of Us, drug repurposing, variant interpretation, rare diseases, EHR, knowledge graph). |
| `arxiv-digest` repo (`digests/`) | 2026-05-25 → 05-28 | Auto-triaged q-bio.QM/GN/PE + stat.AP. Recent days are thin — all score-1 incidental keyword hits. |
| Raw arXiv daily mailings (`no-reply@arxiv.org`) | daily | Full unfiltered cs/q-bio/stat listings to a list address; not individually triaged here (this is exactly what the digest pipeline is meant to filter). |

> Caveat: Scholar alert emails contain title, authors, venue, and the first
> ~2–3 lines of each abstract only. The "detailed report" per study below
> contextualizes that metadata against your research threads; it does not
> reflect a full-text read, and no quantitative result is stated unless it
> appeared in the alert.

---

## Executive summary

- **Causal inference / pharmacoepi is the hottest cluster this week.** A
  target-trial-emulation (TTE) paper on NSAIDs → periodontitis is rippling
  through your Hernán + Denny alerts, and a JAHA paper does a head-to-head
  TTE of *individual* SGLT2 inhibitors — directly on your SGLT2 drug-class
  thread. Three arXiv stat.ME/stat.ML methods papers (IPW/AIPW for win
  measures, semiparametric functional DiD, kernelized IPS) are
  methods-watch fodder.
- **CHIP had a strong week** (Bick author alert): an 800k-individual,
  3-cohort stroke-risk paper and a *Nature Communications* paper on
  co-occurring CHIP + mosaic chromosomal alterations with high leukemia
  risk. Both serve your clonal-hematopoiesis disease thread.
- **EHR phenotyping + rare disease + OMOP** all surfaced concrete items:
  a hierarchical set-to-sequence model for early rare-disease detection
  from structured EHR, an automated OMOP-CDM ETL pipeline (Callahan
  alert), and a SHANK3 "reverse phenotyping" autism subtype paper
  (Bastarache alert).
- **Genetic epi**: multi-ancestry endometriosis GWAS + multi-omics
  (*Nature Genetics*, Karczewski alert); two proteome-wide MR
  drug-target papers (lung function; CD58/PARP1 immune targets) and a
  cross-ancestry proteome-wide MR for breast cancer.
- **Biobank/All of Us**: a depression-after-GI-cancer All of Us study
  appeared in *your own* "new related research" alert.
- **Low-signal:** the `arxiv-digest` repo's last four days are all
  score-1 hits; the "knowledge graph" keyword alert is returning
  non-biomedical KG papers (geographic KG, educational KG) that you can
  ignore per the INTERESTS.md "lower interest in non-biomedical KG" note.

Counts: **15 HIGH**, **6 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. NSAIDs and the Risk of Periodontitis Among Adults With Osteoarthritis: A Target Trial Emulation
- **Authors / venue:** I. Leiva-Escobar, A.P. Chennas, Z. Alayash, et al. — *Journal of Clinical Periodontology*, 2026.
- **Surfaced by:** Joshua C. Denny + Miguel Hernán "new related research", and citation alerts to Denny/Hernán (it cites foundational TTE methodology).
- **Thread:** Causal inference & pharmacoepidemiology (target trial emulation).
- **What it is:** A target-trial emulation testing whether long-term NSAID
  exposure lowers periodontitis risk in adults with osteoarthritis — the
  mechanistic premise being COX inhibition slowing periodontal tissue
  breakdown. The alert snippet states the long-term effect "remains
  unclear" and that they emulate a trial in an observational (OA) cohort.
- **Why it matters to you:** This is a clean, citable worked example of TTE
  applied to a drug-class question with confounding-by-indication risk —
  the exact design pattern in your active drug-class threads (GLP-1, SGLT2,
  CFTR modulators, HRT). Worth reading for the protocol table (eligibility,
  treatment strategies, grace period, cloning/censoring/weighting) as a
  template. The fact that it shows up in *both* Denny and Hernán alerts
  signals it's anchoring its methods on canonical TTE references.
- **Action:** Read for design methodology; low direct disease relevance.

### 2. Comparative Effectiveness of Individual SGLT2 Inhibitors on Cardiovascular Outcomes in Type 2 Diabetes With Moderate Cardiovascular Risk: Emulation of a Target Trial
- **Authors / venue:** A. Zehra, Y. Deng, K.S. Swarna, J. Herrin, E.C. Polley, et al. — *Journal of the American Heart Association*, 2026.
- **Surfaced by:** Patrick Ryan "new related research".
- **Thread:** Pharmacoepidemiology (SGLT2 drug-class thread) + causal inference (TTE).
- **What it is:** Head-to-head comparative-effectiveness TTE of *individual*
  SGLT2 inhibitors (not class-vs-other) on MACE in T2D patients at moderate
  CV risk. The snippet explicitly notes "no direct comparison of individual
  SGLT2 inhibitor drugs has been conducted, particularly" in this risk
  stratum — i.e., it fills a within-class head-to-head gap. Author roster
  (Herrin, Polley) points to an OptumLabs/Mayo real-world-data shop.
- **Why it matters to you:** Squarely on your SGLT2 thread and your
  TTE-with-confounding agenda. The within-class active-comparator design
  is the gold-standard way to blunt confounding-by-indication, and the
  "moderate CV risk" framing is a heterogeneity-of-treatment-effect angle
  that connects to your precision-health thread (who benefits most).
- **Action:** HIGH — read in full; strong fit for both methods and the drug thread.

### 3. Automatic ETL Pipeline Generation for Mapping Heterogeneous Clinical Data into the OMOP Common Data Model
- **Authors / venue:** E. Mayrhuber, P. Stampfer, S.P.K. Veeranki, L. Steininger, et al. — *dHealth 2026* (IOS Press).
- **Surfaced by:** Tiffany J. Callahan "new related research".
- **Thread:** EHR phenotyping & OMOP.
- **What it is:** An automated, mapping-driven ETL pipeline that reduces the
  manual effort of transforming heterogeneous clinical data into the
  OMOP-CDM. Positioned against the usual pain point that "ETL development
  remains complex and manually intensive."
- **Why it matters to you:** OMOP-CDM is core plumbing for your EHR
  phenotyping and multi-site biobank work. Tooling that lowers ETL cost is
  directly useful infrastructure; worth checking whether the
  "mapping-driven" approach is rules-based or LLM-assisted (your INTERESTS
  flag LLM-assisted phenotyping specifically).
- **Action:** HIGH — skim for the mapping representation and any LLM component.

### 4. Clonal Hematopoiesis and Risk of Stroke: Evidence From Over 800,000 Individuals Across 3 Cohorts
- **Authors / venue:** A.G. Bick — *Stroke*, 2026.
- **Surfaced by:** Alexander Bick "new articles".
- **Thread:** Clonal hematopoiesis (CHIP) disease thread; large biobank scale.
- **What it is:** A pooled analysis across three cohorts (>800k individuals)
  estimating the association between clonal hematopoiesis and stroke risk.
- **Why it matters to you:** Direct CHIP→cardiovascular-outcome evidence at
  biobank scale — exactly your CHIP thread (somatic mosaicism,
  cardiovascular/hematologic outcomes). The 3-cohort design is also a
  cross-cohort replication template relevant to your biobank work.
- **Action:** HIGH — read for effect sizes and cohort composition (likely UKB/MVP/BioVU-type sources).

### 5. Co-occurring Clonal Hematopoiesis Exhibits Strong Selection and High Leukemia Risk
- **Authors / venue:** K.M. Barnao, A.K. Hubbard, I.C.C. Chan, W. Zhou, et al. — *Nature Communications*, 2026.
- **Surfaced by:** Alexander Bick "new articles".
- **Thread:** Clonal hematopoiesis (CHIP) + mosaic chromosomal alterations (mCAs).
- **What it is:** Genomic analysis showing that co-occurrence of CHIP and
  mCAs (the two main classes of clonal hematopoiesis) is under strong
  positive selection and confers high leukemia risk.
- **Why it matters to you:** Sharpens the CHIP thread by moving from single
  clonal events to *co-occurring* somatic lesions and malignancy risk
  stratification — relevant if you're building composite somatic-risk
  models. Pairs naturally with #4.
- **Action:** HIGH — read alongside #4 for the CHIP somatic-risk picture.

### 6. Early Detection of Rare Disease Using Hierarchical Set-to-Sequence Modeling of Structured Electronic Health Records
- **Authors / venue:** Y. Ma, L. Chinthala, A. Mohammed, R.L. Davis, V. Colonna — *medRxiv*, 2026.
- **Surfaced by:** Pascal Brandt "new related research".
- **Thread:** Rare disease + EHR phenotyping + ML for precision health.
- **What it is:** A hierarchical set-to-sequence neural architecture for
  early rare-disease detection from longitudinal structured EHR, explicitly
  designed for "heterogeneous, weak, and sparse phenotypic signals that
  emerge gradually across visits."
- **Why it matters to you:** Hits the intersection of three threads —
  rare-disease diagnosis, computable phenotyping, and clinically-anchored
  ML. The set-to-sequence framing (sets of codes per visit → sequence over
  visits) is a modeling idea worth cribbing for phecode-sequence work and
  EHR foundation-model tokenization (cf. your MEDS/FEMR/MOTOR interest).
- **Action:** HIGH — read the architecture + how they define the rare-disease label.

### 7. Genome-wide association study of asthma with high treatment burden and/or worse outcomes defined using electronic healthcare data in UK Biobank
- **Authors / venue:** N.N. Piga, M.A. Portelli, N. Shrine, J. Chen, R. Packer, et al. — UK Biobank, 2026.
- **Surfaced by:** Jian Yang "new related research".
- **Thread:** EHR phenotyping + genetic epidemiology + UK Biobank.
- **What it is:** A GWAS where the *phenotype itself* — "asthma with high
  treatment burden / worse outcomes" — is defined from linked EHR
  prescribing and outcome data in UKB.
- **Why it matters to you:** Textbook example of EHR-derived outcome
  definitions powering a genetic study (your "exploit EHR depth —
  medications, labs — for genetic studies" priority). Useful for how they
  operationalize "treatment burden" from prescription records into a
  GWAS-able phenotype.
- **Action:** HIGH — read the phenotyping algorithm specifically.

### 8. Causal Machine Learning Is Not a Panacea: A Roadmap for Observational Causal Inference in Health
- **Authors / venue:** D. Tjandra, T. Chang, S. Parbhoo, R. Ranganath, et al. — arXiv:2605.20782, 2026.
- **Surfaced by:** Leo Anthony Celi "new articles".
- **Thread:** Causal inference; ML for precision health (HTE/causal ML).
- **What it is:** A position/roadmap paper cautioning against naive use of
  causal ML on large observational clinical datasets, motivated by the
  difficulty of RCTs and the enthusiasm for causal-ML shortcuts.
- **Why it matters to you:** Directly relevant framing for your causal-ML
  toolkit (causal forests, DML/debiased ML, TTE). Likely a good
  assumptions-and-pitfalls checklist to cite when defending design choices
  (positivity, overlap, unmeasured confounding) in RWE work.
- **Action:** HIGH (methods) — read as a guardrails reference for the causal-ML thread.

### 9. Multi-ancestry genome-wide association and integrated multi-omics analyses of endometriosis and its clinical manifestations
- **Authors / venue:** D. Koller, J. He, S. Løkhammer, S. Aranda, D. Qiu, et al. — *Nature Genetics*, 2026.
- **Surfaced by:** Konrad Karczewski "new related research".
- **Thread:** Genetic epidemiology (GWAS, cross/trans-ancestry, multi-omics integration).
- **What it is:** Multi-ancestry GWAS of endometriosis integrated with
  multi-omics, also dissecting clinical manifestations/subphenotypes.
- **Why it matters to you:** A current, high-profile template for
  cross-ancestry GWAS + multi-omics integration + sub-phenotyping — the
  methodological shape you care about (trans-ancestry portability,
  manifestation-level phenotyping) even though the disease isn't a tracked
  thread. Methods-transferable to your PRS/fine-mapping work.
- **Action:** HIGH — read for the cross-ancestry + manifestation-stratified design.

### 10. Onset of Depression Among Gastrointestinal Cancer Survivors: An "All of Us" Research Program Study
- **Authors / venue:** R. Bega, C.M. Charalampous, A. Mevawalla, Q. Alizai, et al. — *Journal of Gastrointestinal …*, 2026.
- **Surfaced by:** **Chenjie Zeng** "new related research" (i.e., adjacent to your own work).
- **Thread:** EHR-linked biobanks (All of Us).
- **What it is:** An All of Us Research Program study of incident depression
  in GI-cancer survivors using the program's EHR + survey data.
- **Why it matters to you:** It's an All of Us applied study surfacing in
  *your* author-related feed — useful both as a citation-landscape signal
  and as an example of AoU outcome-ascertainment (depression onset) for
  the biobank thread. Per your rubric this is a clinical-question AoU paper
  = medium-high; flagging because it's tied to your own alert.
- **Action:** Medium-HIGH — scan for AoU phenotype/outcome definitions and cohort construction.

### 11. Proteome-wide Mendelian Randomization and Colocalization Nominate CD58, PARP1, and Immune Co-stimulatory Pathways as Genetically Supported Targets
- **Authors / venue:** Z. Wang, Y. Sun, Z. Bai, M. Li, D. Kong, G. Wu — 2026.
- **Surfaced by:** "UK Biobank" keyword alert.
- **Thread:** Genetic epidemiology (MR) + UK Biobank + drug-target/repurposing.
- **What it is:** Proteome-wide MR + colocalization to nominate genetically
  supported drug targets (CD58, PARP1, immune co-stimulatory pathways).
- **Why it matters to you:** MR-for-target-prioritization is a recurring
  shape across your alerts this week (#11, #12, #13) and connects genetic
  epi to your drug-repurposing thread (target identification with a
  genetic-evidence loop). Colocalization is the key rigor step
  distinguishing causal targets from LD artifacts.
- **Action:** HIGH (methods + repurposing) — note the MR+coloc pipeline.

### 12. Proteome-wide Mendelian randomisation of lung function to identify potential therapeutic targets for respiratory disease
- **Authors / venue:** J. Chen, N. Shrine, K. Coley, R.J. Packer, A. Edris, et al. — *ERJ Open Research*, 2026.
- **Surfaced by:** Stephen B. Montgomery "new related research".
- **Thread:** Genetic epidemiology (MR) + drug-target nomination.
- **What it is:** Proteome-wide MR using lung-function phenotypes to
  prioritize druggable targets for respiratory disease.
- **Why it matters to you:** Same MR-target-prioritization template as #11,
  on a quantitative phenotype (lung function). Good companion read for the
  drug-repurposing-with-genetic-evidence angle.
- **Action:** HIGH — read with #11 as a pair of proteome-MR target papers.

### 13. Cross-ancestry proteome-wide Mendelian randomization prioritizes 12 plasma protein candidates for breast cancer risk
- **Authors / venue:** X. Wu, D. Godbole, J. Williams, J. Sharma, J. Choi, Z. Liu, et al. — *medRxiv*, 2026.
- **Surfaced by:** Joshua C. Denny "new related research".
- **Thread:** Genetic epidemiology (MR, cross-ancestry).
- **What it is:** Cross-ancestry proteome-wide MR nominating 12 plasma
  proteins for breast-cancer susceptibility; explicitly tackles
  ancestry-portability of proteomic instruments.
- **Why it matters to you:** Adds the cross-ancestry dimension (your
  trans-ancestry portability interest) to the proteome-MR cluster.
  Open-access on medRxiv for a full read.
- **Action:** HIGH — read for the cross-ancestry instrument construction.

### 14. Experimental and Computational Approaches to Identify Noncoding Pathogenic Variation in Rare Disease
- **Authors / venue:** L.E. Covill, L. Romo, A. O'Donnell-Luria — *Annual Review of Genomics and Human Genetics*, 2026.
- **Surfaced by:** "rare diseases" keyword alert.
- **Thread:** Variant interpretation (ACMG/ClinGen, splicing/RNA evidence) + rare disease.
- **What it is:** A review of methods (experimental + computational) for
  resolving noncoding pathogenic variation in rare disease — the hard
  frontier of variant interpretation beyond coding LoF.
- **Why it matters to you:** O'Donnell-Luria is a ClinGen/variant-curation
  authority; this is a high-value reference for your VUS-resolution and
  splicing/RNA-evidence interests. Annual Review = good consolidated
  background to cite.
- **Action:** HIGH — keep as a reference review for the variant-interpretation thread.

### 15. SHANK3-anchored reverse phenotyping identifies a rare-variant-enriched cognitive-motor subgroup of autism
- **Authors / venue:** A. Udeshi, S. Smout, M. Caballero, A. Rapp, A. Kolevzon, et al. — *medRxiv*, 2026.
- **Surfaced by:** Lisa Bastarache "new related research".
- **Thread:** Rare-variant association + deep phenotyping (reverse phenotyping) — adjacent to PheWAS/PheRS.
- **What it is:** "Reverse phenotyping" anchored on SHANK3 — starting from a
  gene/variant and characterizing the EHR/clinical phenotype it enriches —
  identifying a rare-variant-enriched cognitive-motor autism subgroup.
- **Why it matters to you:** Reverse-phenotyping is methodologically next to
  your PheWAS/PheRS and penetrance-in-population-screening interests (Lisa
  Bastarache is a phecode/PheWAS principal). The "variant → enriched
  phenotype cluster" design is directly transferable to your monogenic
  penetrance work.
- **Action:** HIGH — read for the reverse-phenotyping methodology.

---

## METHODS-WATCH (off-thread disease/topic, exemplary methods)

These are mostly from the `arxiv-digest` repo (score-1 keyword hits) plus
one Scholar item. None are on a disease thread, but the methods are worth a
skim.

- **Estimation and Inference for Win Measures with Multiple Ordinal Endpoints Subject to Missingness** — Y. Liu, H. Barnhart, S. O'Brien, Y. Lokhnygina, R.A. Matsouaka (stat.ME, arXiv:2605.27085). IPW + augmented-IPW (double-robust) estimators for win ratio / win odds / DOOR under missing hierarchical endpoints; closed-form influence-function variances; R package `WinMO`. *Watch for:* the AIPW/EIF construction — same machinery you use in TTE/causal work.
- **Semiparametric Inference for Causal Effects on Functional Outcomes** — J. Nie, C. Ling, M. Ran (stat.ME, arXiv:2605.26964). Difference-in-differences for functional outcomes with efficient influence function, Neyman-orthogonal cross-fitted debiased estimator, uniform confidence bands. *Watch for:* the cross-fitting/orthogonality pattern (transfers to DML).
- **Insurance Pricing Optimization via Off-Policy Evaluation** — S. Günther, D. Semenovich, M.V. Wüthrich (stat.ML, arXiv:2605.28327). Kernelized inverse-propensity-score estimator with variance reduction; off-policy evaluation framing. *Watch for:* the kernelized IPS variance-reduction trick — borrowable for policy/treatment-rule estimation. (Non-health domain.)
- **BIRDNet: Mining and Encoding Boolean Implication Knowledge Graphs as Interpretable Deep Neural Networks** — T. Dash (cs.LG, arXiv:2605.28739). Mines Boolean-implication rules from tabular omics data into a sparse, interpretable neural net; recovers known biological signatures on transcriptomic/proteomic benchmarks. *Watch for:* the interpretable-by-construction KG→NN idea (fits your "explainable hypothesis output" preference for KG/GNN methods, though here it's omics not clinical).
- **UniRiskP: Multimodal fusion-based in-hospital mortality prediction and phenotyping** — X. Zhang et al. (*J King Saud Univ*, 2026; Hripcsak alert). Multimodal structured-time-series + notes fusion for IHM + phenotyping. *Watch for:* the fusion architecture; otherwise a fairly generic ICU-benchmark paper (borderline SKIP by your "generic benchmark = SKIP" rule).
- **Connecting polygenic disease risk to cell states and regulatory programs through single-cell chromatin accessibility** — L. Yu, L.T. Deary, Q. Liu, Q. Zhang, S. Zhao (bioRxiv, 2026; Denny alert). scATAC-seq + GWAS enrichment to map polygenic risk to cell states. *Watch for:* functional-genomics interpretation of PRS/GWAS signal (adjacent to your fine-mapping/TWAS thread).

---

## SKIP / noise (logged, no action)

- **arxiv-digest repo, 05-27 & 05-28:** "Benchmarking Ultrasound Foundation
  Models for Fetal Plane Classification" (foundation model, but imaging not
  EHR) — SKIP.
- **"knowledge graph" keyword alert:** "Addressing Trustworthiness and
  Explainability Using Knowledge Graphs", "Hierarchical Adaptive
  Meta-Learning for Geographic KG", "Co-creating a Community-focused
  Educational KG (Yanyuwa)" — all non-biomedical KG; SKIP per INTERESTS.md.
- **"drug repurposing" keyword alert:** "Glycosylation-Related Biomarkers in
  the Hippocampus for Alzheimer's Diagnosis and Drug Repurposing" (Mu et
  al.) — biomarker/chemistry-led repurposing without a clinical-evidence
  loop; your INTERESTS explicitly down-weights target-/chemistry-only
  pipelines. SKIP (borderline).
- **Author-alert LLM/ML drift:** several Szolovits / Zitnik / Natarajan
  alerts returned generic LLM papers (STARFlow2, LambdaPO, RISE,
  multimodal VLM pretraining, "Forecasting Scientific Progress with AI").
  Off-thread — SKIP.
- **Citation-only churn:** many "N new citations to articles by X" alerts
  point to unrelated downstream cites (e.g., colon-adenocarcinoma
  crotonylation citing Pritchard/Jian Yang). SKIP.

---

## Suggestions for the pipeline (optional)

1. **The repo digest is under-recalling vs. your Scholar alerts.** The last
   four `digests/` days are all score-1 incidental hits, while the genuinely
   on-thread papers (TTE SGLT2, CHIP×2, rare-disease set-to-sequence, OMOP
   ETL) all came from Scholar — because they're in journals / med-bio-rxiv
   and outside the four tracked arXiv categories (q-bio.QM/GN/PE, stat.AP).
   Consider adding `cs.LG`/`stat.ME`/`q-bio.MN` or wiring a medRxiv/bioRxiv
   source if you want the digest to catch these.
2. **`knowledge graph` keyword is noisy.** It's pulling geographic/educational
   KGs. Consider requiring co-occurrence with a biomedical term
   (`biomedical`, `clinical`, `HPO`, `SNOMED`) or splitting into
   `biomedical knowledge graph`.
3. **Proteome-wide MR is a recurring high-value shape** (3 papers this week)
   but isn't a tracked keyword — consider adding `proteome-wide` /
   `pwmr` / `colocalization` to `tracked.yaml` under genetic epi.
