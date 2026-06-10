# Research digest — 2026-06-10

Synthesizes (a) the local `arxiv-digest` runs from the past week and (b)
research-alert email traffic from Gmail (Google Scholar keyword + author
alerts, PubMed `drug repurposing` / `All of Us`, medRxiv collections).
Triaged against `INTERESTS.md` (last updated 2026-04-30).

## Inbox summary

| Source | Last 24–48h volume | Signal vs noise |
|---|---|---|
| arXiv daily mailings (`stat`, `q-bio`, `cs`) | 3 emails/day, autoforwarded | Driven by the pipeline; see `digests/` |
| Google Scholar keyword alerts (UK Biobank, AoU, drug repurposing, EHR, rare diseases, KG, autoimmune) | 7 emails (2026-06-09) | Mixed — ~25% on-thread |
| Google Scholar author alerts (Szolovits, Zitnik, Hripcsak, Denny, Hernán, Callahan, Yang, Shendure, Chute, Kastner, Natarajan, Le, van der Schaar, Montgomery, Luo) | 12+ emails | Mostly tangential except Denny/Hernán/Callahan threads |
| PubMed saved searches (`drug repurposing`, `All of Us`) | 2 emails (10 + 1 hits) | Half on-thread |
| medRxiv collections (Epi, Genetic/Genomic Med, Health Informatics, Nephrology, Onc, Peds) | 1 digest (2026-06-09) | High signal — included below |
| JAMA Network, justhealthcare, etc. | 4 emails | Skipped — clinical news, not research |
| `arxiv-digest` repo (local script output) | digests for 2026-06-02 → 2026-06-09 | 5 surfaced papers across window |

No GitHub-emailed `arxiv-digest` notifications were found (`from:notifications@github.com` + `arxiv-digest` returned empty); the
digests reviewed here are the locally-generated ones in `digests/`.

---

## HIGH-priority studies (direct hits on active threads)

### 1. STELLAR: ensemble framework integrating rare variants for polygenic risk prediction
- **Authors:** Tony Chen, Xihao Li, Rahul Mazumder, Haoyu Zhang, Xihong Lin
- **Source:** medRxiv 2026.06.07.26355109 (posted 2026-06-09) — Genetic & Genomic Medicine
- **Why it matters (threads: Genetic epidemiology + Composite risk models):** Directly addresses one of your stated active angles — stacking rare pathogenic variants with PRS. The Lin group's prior STAAR/SCANG infrastructure makes this credible methods to crib for composite (PRS + rare-variant burden) scoring you've been building for biobank workflows.
- **What to extract:** Their ensemble weighting scheme between common-variant PRS and rare-variant aggregate scores, and whether they demonstrate cross-ancestry portability (an explicit ongoing concern in `INTERESTS.md`).
- **Action:** Read in full. Worth checking whether they release weights / scripts for AoU or UKB exome cohorts.

### 2. CKM Syndrome and risk of MCI/Dementia in UK Biobank *and* All of Us
- **Authors:** Y. Yoshida, Y. Zu, You Lu, Xiu Wu (Diabetes 2026 Suppl., 2180-P)
- **Source:** Scholar alert ("UK Biobank" keyword)
- **Why it matters (threads: Biobanks with EHR linkage + Chronic disease clustering/multimorbidity):** Cross-biobank replication (UKB n=109,137; AoU n=15,265) using CKM staging — exactly the kind of "two-biobank" methods anchor you said you want to see more of. Maps cardiometabolic multimorbidity onto cognitive outcomes.
- **What to extract:** How they aligned CKM stage definitions across UKB and AoU coding systems (OMOP vs UKB native fields) — that crosswalk is generally useful for any cross-biobank phenotype project.
- **Action:** Pull the abstract; if they describe a phenotype crosswalk, save the supplement for your OMOP/phecode reference.

### 3. Multimorbidity Phenotypes in Diabetes: Latent Class Analysis in UK Biobank (10-yr mortality and dementia)
- **Authors:** J. Calvo-Marin, F. R. Salazar, V. Mora-Gomez et al. (Diabetes 2026 Suppl., 2266-P and 2265-P — two companion abstracts)
- **Source:** Scholar alert ("UK Biobank" keyword)
- **Why it matters (thread: Chronic disease clustering and multimorbidity):** Classic LCA-on-comorbidity-pattern setup applied to 28,043 UKB diabetes participants, with mortality and dementia as anchored outcomes. Methodologically aligned with the multimorbidity-clustering thread you flagged, especially cardiometabolic.
- **What to extract:** Class-enumeration criteria and how they validated the latent classes against an independent outcome (mortality vs dementia). Their pair of papers using the *same* latent-class solution against different outcomes is a useful template.
- **Action:** Skim both; mine for a clean class-validation template.

### 4. Distinct and shared genetics of kidney filtration function vs albuminuria — multi-trait GWAS
- **Authors:** Hannah Cathrin de Hesselle, Barbara-Frederike Garben, Klaus J. Stark, … Thomas W. Winkler
- **Source:** medRxiv 2026.06.08.26355141 — Genetic & Genomic Medicine
- **Why it matters (threads: Genetic epidemiology + APOL1/kidney disease):** Multi-trait GWAS dissecting eGFR vs albuminuria genetic architecture is directly relevant to the APOL1 kidney-risk thread (where albuminuria-vs-eGFR architecture matters for ancestry-stratified risk).
- **What to extract:** Whether APOL1 emerges with differential weighting between the two phenotypes; check supplement for ancestry stratification.
- **Action:** Read methods + the APOL1 locus section.

### 5. Alport Syndrome — genotype, proteinuria, eGFR with long-term outcomes (UK RaDaR registry)
- **Authors:** Katie Wong, David Pitcher, … Daniel P. Gale (RaDaR consortium)
- **Source:** medRxiv 2026.06.08.26355110 — Nephrology
- **Why it matters (thread: Rare disease + Variant interpretation):** Genotype-stratified long-term kidney outcomes in a national rare-disease registry — exactly the kind of penetrance-by-variant-class work you flagged for monogenic conditions under population vs ascertained conditions. The pharma co-authors (Francke, Inan-Eroglu, Abdelgawwad, Liu, Dasmahaptra, Lin) suggest there's a trial-readiness angle as well.
- **What to extract:** Their grouping of variants (truncating vs missense, autosomal recessive vs X-linked) and the slope of decline against genotype class.
- **Action:** Read in full — closest study this week to your "penetrance under screening vs clinical ascertainment" framing.

### 6. Autosomal type IV collagen genes — sex differences in genetic risk for hematuria (UK Biobank)
- **Authors:** F. Lona-Durazo, I. R. Dinsmore, M. T. McNulty et al. — *Kidney International Reports*, 2026
- **Source:** Scholar alert ("UK Biobank" keyword)
- **Why it matters (threads: Genetic epidemiology + Variant interpretation):** COL4A3/4/5 variant-level work in UKB with sex-stratified effects (including testosterone interaction). Relevant to Alport / thin-basement-membrane interpretation, and methodologically a model for sex-stratified GWAS in a biobank.
- **Action:** Skim for the COL4A variant set and whether they report ClinVar overlap.

### 7. G.AI: AI-driven platform for phenotype standardization, variant interpretation, and structured clinical reporting in rare disease genomic diagnosis
- **Authors:** Z. Wang, X. Chen, L. Tang, X. Wu, A. Huang, H. Zhang — *J. Translational Medicine*, 2026
- **Source:** Scholar alert ("rare diseases" keyword)
- **Why it matters (threads: Variant interpretation (ACMG/ClinGen) + Rare disease + EHR phenotyping):** Combines HPO standardization, ACMG-style variant interpretation, and structured clinical reporting — i.e., the entire variant-curation pipeline you've been tracking via InterVar/AnFiSA-style DSLs. Worth comparing to the tools you've already cataloged.
- **What to extract:** Whether the ACMG criteria assignment is rules-based or LLM-derived, and how they handle PS3/BS3 (functional evidence) ingestion.
- **Action:** Pull PDF; this overlaps your "LLM-assisted phecode/HPO" interest as well.

### 8. Targeted reflex RNA-seq for enhanced variant classification on exome/genome sequencing
- **Authors:** X. Zhao, R. Rigobello, M. Driver, S. Lau, M. L. Chong et al. — *npj Genomic Medicine*, 2026
- **Source:** Scholar alert ("rare diseases" keyword)
- **Why it matters (thread: Variant interpretation — splicing/RNA evidence for VUS resolution):** Quantifies the diagnostic-yield delta from reflex RNA-seq for splicing-VUS resolution (+1.6% diagnostic yield in their cohort). This is the splicing-evidence angle you explicitly listed under ACMG/ClinGen.
- **What to extract:** Their reflex-trigger criteria (which variants get sent to RNA-seq) — directly usable as a decision rule.
- **Action:** Read; cite-worthy for any VUS-reclassification methods doc.

### 9. β2-adrenergic receptor agonists for cognitive function — PharmLines retrospective cohort
- **Authors:** Alghamdi A., Combrtg E., Balafas S., Bos J. H. J., Van Munster B. C., Schmidt M., Hak E. — *J. Alzheimers Dis.*, 2026 (online ahead of print)
- **Source:** PubMed alert ("drug repurposing")
- **Why it matters (thread: Drug repurposing + Causal inference and pharmacoepi):** Real-world prescribing data → cognitive outcomes is exactly the "EHR-based repurposing signals" angle you specifically highlighted, *with* a clinical-evidence loop. β2-agonist → AD cognition is a genuinely interesting repurposing hypothesis (locus coeruleus / noradrenergic angle).
- **What to extract:** Their confounding adjustment (active-comparator? new-user?) and whether they emulate a target trial.
- **Action:** Read in full; this is the most thread-aligned drug-repurposing paper of the batch.

### 10. Metformin and GLP-1RA use in adults with hidradenitis suppurativa (All of Us)
- **Authors:** R. Shrestha, G. Nguyen, R. McCoy (Diabetes 2026 Suppl., 2281-P)
- **Source:** Scholar alert ("All of Us research program")
- **Why it matters (threads: Causal inference and pharmacoepi (GLP-1 RAs) + Drug repurposing + Biobanks):** GLP-1 RA repurposing for an inflammatory dermatologic condition, in AoU — multi-thread hit. McCoy's group does careful pharmacoepi.
- **Action:** Skim — abstract is short; check whether they did new-user / active-comparator design.

### 11. Real-world trajectories of T2D pharmacotherapy: nationwide clustering of EHRs
- **Authors:** P. Kukhareva (Diabetes 2026 Suppl., 2317-P)
- **Source:** Scholar alert ("electronic health records")
- **Why it matters (threads: EHR phenotyping + Causal inference and pharmacoepi + ML for precision health):** Sequence-clustering on medication trajectories from EHRs at national scale is methodologically close to your interest in trajectory clustering and topic-model-style approaches over diagnosis/Rx sequences.
- **Action:** Look for the clustering approach (k-means on embeddings vs HMM vs topic model) and which EHR network they used.

### 12. Multi-ethnic reference map of T cell receptor germline diversity (All of Us)
- **Authors:** S. Mantena, R. Edahiro, Y. Okada, A. Akbari et al. — *Nature Communications*, 2026
- **Source:** Scholar alert ("All of Us research program")
- **Why it matters (threads: Biobanks with EHR linkage + Genetic epidemiology — ancestry):** Uses AoU's multi-ancestry depth to characterize TCR germline diversity — methodologically useful as an exemplar of AoU's value-add for ancestry-stratified work.
- **Action:** Skim; useful citation when justifying AoU for ancestry-aware analyses.

---

## Locally-surfaced arxiv-digest papers (2026-06-02 → 2026-06-09)

The local pipeline surfaced 5 papers; only one is directly thread-aligned.

### A. "Leveraging External Controls for Treatment Switching in RCTs" (Shen, Fu, Lin, stat.ME)
- arXiv 2606.06441v1 (digest 2026-06-06; score 1, keyword: causal inference)
- **Thread:** Causal inference and pharmacoepi.
- **Why useful:** Weighted causal-inference framework combining synthetic controls + balancing weights for treatment-switching bias in oncology OS endpoints. Methodologically transferable to any setting with non-ignorable post-randomization treatment changes — relevant if you're emulating GLP-1 / SGLT2 trial-like designs in EHR data.
- **Triage:** **METHODS-WATCH** (oncology disease focus, but the estimator is general).

### B. "Federated SPARQL querying for genomic variant functional annotation" (Bodrug-Schepers, Bourcier, Redon, Gaignard)
- arXiv 2606.05918v1 (digest 2026-06-06; score 1, keyword: knowledge graph)
- **Thread:** Knowledge graphs & ontologies + Variant interpretation.
- **Why useful:** Variant annotation via federated SPARQL over UniProtKB without duplicating reference data — clean FAIR-aligned pattern for keeping clinical-genomic KGs on-site.
- **Triage:** **METHODS-WATCH** (infrastructure rather than scientific).

### C. "Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery" (Biswas, Gupta, Mukherjee, cs.AI)
- arXiv 2606.09672v1 (digest 2026-06-09; score 2)
- **Thread:** EHR foundation models + KG.
- **Why useful:** Demonstrates that biomedical encoders (BioBERT/PubMedBERT/BioM-ELECTRA) produce spuriously high similarity for unrelated cross-domain pairs and propose a contrastive fix (BODHI) using biomedical-KG-absent edges as hard negatives. Relevant if you build LLM-judged or embedding-based feature engineering on top of EHR foundation models.
- **Triage:** **METHODS-WATCH** (note for the foundation-model-fairness/calibration audit angle).

### D. "scTransformer: gene regulatory priors into Transformer attention" (Milia et al., q-bio.GN)
- arXiv 2606.09558v1 (digest 2026-06-09; score 1)
- **Triage:** SKIP for your active threads (single-cell, not EHR-anchored).

### E. "SpineAgent: multi-agent system for spine MRI report generation" (Xiao et al., cs.CV)
- arXiv 2606.08897v1 (digest 2026-06-09; score 1)
- **Triage:** SKIP (imaging-only; no clinical-decision loop relevant to your threads).

Days 06-02, 06-03, 06-07, 06-08 had no matches in the lookback window.

---

## Notes / things to watch

- **arxiv-digest coverage gap:** 2026-06-03 had 3/4 q-bio categories fail to fetch — worth checking the script ran cleanly that day, as some of the methods papers above (medRxiv) didn't surface in the local digest at all because they're not on arXiv. Consider whether to add a medRxiv collection pull to the pipeline.
- **GitHub-emailed `arxiv-digest`:** no Gmail evidence of a GitHub Actions email pipeline. If you'd like the daily digest pushed by email, that's a 10-line workflow addition.
- **Author-alert noise:** Vivek Natarajan and Marinka Zitnik alerts surfaced VLM / diffusion-LM papers this week — off-thread. If those alerts keep returning noise, consider narrowing to keyword alerts only.

---

## Suggested reading order

1. STELLAR (rare-variant + PRS ensemble) — most directly on-thread methods.
2. Alport / RaDaR (penetrance + genotype-stratified outcomes in rare-disease registry).
3. CKM × dementia in UKB + AoU (cross-biobank multimorbidity).
4. β2-agonist cognitive repurposing (drug-repurposing + pharmacoepi with EHR signal).
5. Reflex RNA-seq for VUS / splicing (variant interpretation).
6. Multi-trait kidney GWAS (eGFR vs albuminuria; APOL1 angle).
