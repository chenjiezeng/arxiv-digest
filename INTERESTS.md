# Research interests

This file anchors what I (Claude) read before triaging each new
arxiv-digest. The keyword list in `config/tracked.yaml` controls
*recall* (which papers the script surfaces); this file controls
*triage* (which surfaced papers count as high-priority signal).

The pipeline runs at `--min-score 1` so the net is wide. Triage
narrows it to what fits the active research threads below.

Last updated: 2026-04-26 (added ML-for-precision-health and chronic-disease-clustering threads).

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

### Variant interpretation (ACMG / ClinGen)
ACMG-AMP variant classification, ClinGen VCEP guidelines, splicing /
RNA evidence for VUS resolution, and variant curation tooling
(InterVar, AnFiSA-style DSLs). LOFTEE and pLoF burden methods.

### Genetic epidemiology
GWAS, PRS / polygenic scores, TWAS, fine-mapping, and cross / trans-
ancestry portability. Phenome-wide MR, biomarker-as-exposure scans.
Composite risk models stacking PRS with rare pathogenic variants.

### Specific disease threads
- **Cystic fibrosis / CFTR**: modulator pharmacoepi, real-world
  outcomes, modulator eligibility & psychosocial impact.
- **APOL1**: kidney disease risk, transplant decision-making, ancestry
  considerations.
- **Clonal hematopoiesis (CHIP) and VEXAS**: somatic mosaicism,
  cardiovascular and hematologic outcomes.
- **Inflammatory bowel disease**: shared with broader autoimmune work.

### EHR foundation models
CLMBR, MOTOR, EHRSHOT, MedTok, FEMR, MEDS lineage. Multimodal EHR FMs
(notes + codes + waveforms + imaging). Foundation-model fairness and
calibration audits when grounded in EHR data.

### Knowledge graphs & ontologies
HPO, SNOMED, biomedical KG construction for clinical reasoning.
Lower interest in non-biomedical KG infrastructure.

### Rare disease
Rare-variant association methods, deep phenotyping for rare-disease
diagnosis (HPO-based), ultra-rare clinical NLP.

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
