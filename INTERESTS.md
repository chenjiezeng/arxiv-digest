# Research interests

This file anchors what I (Claude) read before triaging each new
arxiv-digest. The keyword list in `config/tracked.yaml` controls
*recall* (which papers the script surfaces); this file controls
*triage* (which surfaced papers count as high-priority signal).

The pipeline runs at `--min-score 1` so the net is wide. Triage
narrows it to what fits the active research threads below.

Last updated: 2026-07-29 (added agentic/federated causal-inference
sub-threads, expanded PGS composite-risk framing with polygenic-deviation
and GxE, added LOY under somatic mosaicism, added LLM-agent HPO-diagnosis
benchmarking and pre-symptomatic phenoconversion trajectories under rare
disease, added digital-twins-from-EHR under EHR foundation models, added
pharmacogenomic-modifier-of-medication-persistence under pharmacoepi).

## Active research threads

### PheWAS / phecode infrastructure
PheWAS and PheRS methodology applied to biobank cohorts, with emphasis
on calibration, ancestry-aware risk scores, and phecode-based outcome
definitions. Particular interest in penetrance estimation for monogenic
variants under population-screening conditions (vs. clinically
ascertained cohorts).

### Biobanks with EHR linkage: All of Us, UK Biobank, MVP, BioVU
EHR-linked biobank analysis is a core theme — anything that combines
genomic data with longitudinal real-world clinical records is
high-priority. This includes phenotype validation against EHR-derived
outcomes, ancestry-stratified risk in EHR-linked cohorts, and methods
that exploit the depth of EHR follow-up (medications, labs, imaging
codes) for genetic studies. Methods papers using AoU / UKB / MVP /
BioVU are high-priority; clinical-question papers using these cohorts
are medium unless they overlap with a tracked disease.

### EHR phenotyping & OMOP
Computable phenotype development, OMOP-CDM-based studies, and tools
for clinical phenotyping at scale (LLM-assisted or rules-based).
Includes NLP / LLM extraction from clinical notes for phecode and HPO
term assignment.

### Causal inference and pharmacoepidemiology
Target trial emulation, propensity score / IPW, g-methods, and modern
causal ML (causal forest, double / debiased ML). Active drug-class
threads: GLP-1 RAs, SGLT2is, CFTR modulators (Trikafta / ivacaftor),
hormone replacement therapy. Real-world evidence with explicit
attention to confounding and selection bias.
Rising sub-threads I want the digest to prioritize:
- **Agentic / human-in-the-loop observational-causal-inference
  pipelines** (`oci-agent` Chou/Kallus arXiv 2607.22443, Netflix in
  production; EHR-derived HTE for trial design Li et al. arXiv
  2607.16934). Automating covariate-balance / PS-trimming / sensitivity
  analysis so the human focuses on assumptions and interpretation.
- **Federated / privacy-preserving EHR causal analytics** (distributed
  mediation, cross-network TTE) — the Jang et al. arXiv 2607.17958
  design pattern.
- **Pharmacogenomic modifiers of medication persistence** — real-world
  discontinuation / MPR as an outcome modulated by CYP2D6 /
  metabolizer-phenotype PGx (Cohen et al. *Pharmaceuticals* 2026;
  Psy-PGx UKB lineage). Portable to CFTR-modulator persistence,
  statin discontinuation, HRT persistence, GLP-1 RA persistence.
- **Drug-target Mendelian randomisation triangulated with observational
  cohort estimates** (Saxby et al. metformin × AAA; MR-ALasso lineage).

### Variant interpretation (ACMG / ClinGen)
ACMG-AMP variant classification, ClinGen VCEP guidelines, splicing /
RNA evidence for VUS resolution, and variant curation tooling
(InterVar, AnFiSA-style DSLs). LOFTEE and pLoF burden methods.

### Genetic epidemiology
GWAS, PRS / polygenic scores, TWAS, fine-mapping, and cross / trans-
ancestry portability. Phenome-wide MR, biomarker-as-exposure scans.
Composite risk models stacking PRS with rare pathogenic variants.
Expanded composite-risk / PGS-tails framing I want the digest to
prioritize:
- **PGS residuals / polygenic-deviation designs** as a discovery lever
  for pathogenic rare variants — the Baya *AJHG* 2026 "misaligned
  individuals" framing, perpendicular to Souaiaia *Nature* PGS-tails
  and Vazquez *Genetics* low-risk-group designs. Together the three
  give a "tails-and-residuals" taxonomy of PGS as a discovery
  instrument.
- **GxE and PGS × exposure / environment interactions** (Nagpal &
  Gibson *Nature Genetics* 2026 on pervasive PGS × exposure
  interactions; GxE reframes PGS portability).
- **Multi-omics-augmented PRS** (Nightingale NMR / Olink proteomics /
  metabolomics stacked with PGS for lipid, cardiometabolic, and
  psychiatric traits; Shan et al. UKB 2026; Feng et al. cross-ancestry
  IDP pleiotropy for depression).
- **Pangenome-informed variant calling and its downstream PGS-portability
  consequences** (HPRC v2 update — reference-bias reduction as a
  cross-ancestry portability lever).
- **Cross-trait shared genetic architecture and multi-trait
  triangulation** (MiXeR / conditional-FDR family; Kopal et al.
  brain-imaging × mental health × cardiometabolic).

### Specific disease threads
- **Cystic fibrosis / CFTR**: modulator pharmacoepi, real-world
  outcomes, modulator eligibility & psychosocial impact.
- **APOL1**: kidney disease risk, transplant decision-making, ancestry
  considerations.
- **Clonal hematopoiesis (CHIP), VEXAS, and mosaic Loss of Y (LOY)**:
  somatic mosaicism generally, with an active watch on the male-specific
  LOY analogue of CHIP (Li et al. *Atherosclerosis* 2026 LOY × PAD;
  Loh *Nature* 2018, Kessler *Nature* 2022 lineage). Cardiovascular and
  hematologic outcomes for both; also somatic-mutation contamination
  of germline rare-variant scans (Ji et al. *Biology* 2026 QC layer)
  as a downstream confounder to guard against.
- **Inflammatory bowel disease**: shared with broader autoimmune work.

### EHR foundation models
CLMBR, MOTOR, EHRSHOT, MedTok, FEMR, MEDS lineage. Multimodal EHR FMs
(notes + codes + waveforms + imaging). Foundation-model fairness and
calibration audits when grounded in EHR data. Rising sub-threads:
- **Digital twins from EHR data** — Zhang / Ideker / Oermann *Cell*
  2026 (International Consortium of Digital Twins in Healthcare and
  Medicine) as the field-defining framing reference; individualized
  trajectory prediction as the endgame of EHR-FM work.
- **Pretraining-contamination audits for foundation-model
  benchmarks** — scContam (Ali arXiv 2607.20572) and MIA-scFM
  membership-inference protocols are portable templates for auditing
  CLMBR / MOTOR / MEDS benchmark contamination.

### Knowledge graphs & ontologies
HPO, SNOMED, biomedical KG construction for clinical reasoning.
Lower interest in non-biomedical KG infrastructure.

### Drug repurposing
Computational identification of new indications for approved drugs.
High-priority angles: knowledge-graph / GNN approaches with
*explainable* hypothesis output (path or subgraph rationales rather
than opaque link-prediction scores); EHR-based repurposing signals
mined from real-world prescribing and outcomes; causal-inference
framings of off-label use (target-trial emulation of repurposing
candidates); and rare-disease repurposing where HPO-based phenotype
matching connects to candidate compounds. Lower interest in
target-only or chemistry-only pipelines without a clinical-evidence
loop.

### Rare disease
Rare-variant association methods, deep phenotyping for rare-disease
diagnosis (HPO-based), ultra-rare clinical NLP. Rising sub-threads:
- **Auditable HPO-driven diagnostic benchmarks with separable
  metrics for ranking vs. evidence coverage** — GraphRareBench
  (Guo et al. arXiv 2607.24878) as the reference-benchmark update;
  the 22–44% "Hit@10 hides ranking-of-confounders" observation is a
  QC argument I want propagated across Phenolyzer / Phen2Gene /
  PhenoSV / LIRICAL / Exomiser / PhenoGPT2 benchmarking.
- **Pre-symptomatic carrier phenoconversion prediction from
  longitudinal biomarker trajectories** — Ran / Benatar *Nature
  Medicine* 2026 for ALS as the template. Directly portable to
  BRCA incident-cancer prediction, HTT preclinical HD, APOL1 CKD
  conversion, and hereditary-cancer syndromes with UKB Olink /
  AoU proteomics.
- **Data-driven reanalysis of unsolved cases at 10k+ cohort scale**
  — Uria-Regojo et al. medRxiv 2026 as the mid-scale reference
  between single-center reanalysis and biobank-scale approaches.

### Machine learning for precision health
Individualized risk prediction, treatment-effect heterogeneity, and
prognostic modeling grounded in real-world clinical data. Includes
heterogeneous-treatment-effect methods (causal forests, meta-learners),
calibration and decision-curve analysis, and external validation across
sites or ancestries. ML papers are HIGH when they're tied to a
clinical decision (who to treat, who to screen, when to escalate);
generic benchmark / leaderboard papers are SKIP.

### Chronic disease clustering and multimorbidity
Unsupervised and semi-supervised methods for discovering disease
subtypes, multimorbidity patterns, and disease trajectories from EHR
or biobank data. Latent class / latent profile analysis, topic models
on diagnosis sequences, graph-based comorbidity networks, and trajectory
clustering. Particularly interested when applied to cardiometabolic
disease, autoimmune disease, or aging-related multimorbidity.

## Triage rubric

For each surfaced paper I'll assign one of three buckets:

- **HIGH** — directly serves an active thread above. Read first.
- **METHODS-WATCH** — off-topic disease but exemplary methods worth
  cribbing (e.g., causal-ML pipelines, large-cohort design choices).
- **SKIP** — incidental keyword hit, not worth attention.

## How to update

When research priorities shift, edit the relevant section above (or
add a new one) and commit — I read this file at the start of each
triage. A one-line nudge in chat ("drop the autism thread, add MVP
veterans cohort work") is also fine; I'll mirror the change back into
this file so the anchor stays current.
