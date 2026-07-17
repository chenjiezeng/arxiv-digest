# Research digest report — 2026-07-17

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-17** (since the prior 2026-06-20 report;
a 27-day catch-up window with heavier-than-usual paper density).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 07-17 | ~200+ author-feed and keyword-feed alerts across the window. Author feeds contributing HIGH-priority items: Chenjie Zeng (self-related + citations, 3 papers cite her work), Joshua Denny, Lisa Bastarache, George Hripcsak, Konrad Karczewski, Miguel Hernán, Stephen Montgomery, Jay Shendure, Jian Yang, Patrick Ryan, Pascal Brandt, Yuan Luo, Fei Wang, Heidi Rehm, Mark Daly, Ron Do, Marinka Zitnik, Jonathan Pritchard, Nigam Shah, Christopher Chute. Keyword feeds contributing: "UK Biobank", "All of Us research program", "autoimmune disorders", "phenome wide association studies". |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-17 | 27 daily digests. **14 days with ≥1 relevant paper (7/1 was the biggest, 7 papers); 13 dry days** — the standard stub pattern, consistent with weekend arXiv slowdowns; pipeline healthy (no fetch failures this window, unlike 2026-06-20). See per-day count at the bottom. |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate; not individually triaged (dedup with scholar alerts). |

> Caveat: Scholar alert emails give only title, authors, venue, and the
> first ~2-3 lines of each abstract. The write-ups below place that
> metadata in context against your research threads; nothing here
> reflects full-text reading — treat each entry as a "read-first"
> recommendation, not a summary of the paper.

---

## Executive summary

- **Standout of the window — sextuple-feed on-thread PRS/rare-variant
  paper.** Baya, Lassen, Hill, Venkatesh, Currant et al. — *Individuals
  who deviate from polygenic expectation are enriched for damaging
  variants in genes linked to rare disease* (*AJHG*, 2026). Surfaced
  simultaneously on **six** feeds (Stephen Montgomery ×3 dates, Chenjie
  Zeng-related, Lisa Bastarache-related, Jian Yang-related, George
  Hripcsak citations, Joshua Denny citations). Inverts the usual
  PRS→disease direction: uses the *residual* between measured phenotype
  and PRS-predicted phenotype as an anomaly signal that flags
  individuals enriched for undiagnosed monogenic-disease variants.
  Directly operationalizes the "PRS-as-background + rare-variant-as-
  driver" logic underlying your penetrance work. **Read first.**
- **Chenjie is cited three times this window.** (a) Salvatore, Kundu,
  Du, Friese, Mondul et al. — *Outcome and Exposure PRSs Can Help
  Reduce Information Bias and Selection Bias in Regression Estimates
  From Biobank Data* (*Genetic Epidemiology*, 2026), directly on the
  healthy-volunteer bias problem that shapes AoU/UKB penetrance work;
  (b) Baker et al. — DRIVE v3 IBD haplotype clustering (*Genetic
  Epidemiology*, 2026); (c) Sriram — thesis on causal ML for precision
  medicine (contextual). Salvatore et al. is the highest-signal cite;
  it should be read alongside Wang et al. (AoU reweighting, below).
- **Two independent All-of-Us healthy-volunteer / representativeness
  papers.** Wang, Buto, Ferguson, Chen, Pederson et al. — *Can the
  All of Us sample be reweighted to mirror a nationally representative
  sample? A comparison of mortality predictors* (*Epidemiology*, 2026)
  — the most direct methodological engagement to date with AoU's
  healthy-volunteer bias, using post-stratification against NHIS.
  Pairs with Salvatore et al. above (PRS-as-instrument bias
  correction) as complementary bias-correction strategies. Together
  these are essential reading for any AoU penetrance estimate. **HIGH,
  paired.**
- **Cross-biobank FHIR vs OMOP head-to-head in All of Us.** Patterson,
  Minto, Beaton et al. — *A comparison of FHIR and OMOP electronic
  health record data within the All of Us Research Program* (2026),
  **triple-feed** (Hripcsak, Patrick Ryan-related, Pascal Brandt-
  related; plus AoU keyword). Foundational reference for any AoU EHR
  analysis — quantifies concordance/disagreement between the two
  dominant data models. Both are on the platform and both are used in
  live analyses; this is the paper that lets you decide which side of
  a discrepancy to trust. **HIGH.**
- **Nature: distinct genetic architecture in the tails of complex
  traits.** Souaiaia, Wu, Ori, Choi, Hoggart et al. (*Nature*, 2026,
  Montgomery-related feed). Genetic architecture at PRS extremes
  *differs* from the bulk of the distribution — direct implications
  for how top-percentile-PRS individuals (the ones actually flagged in
  clinical use) should be modeled and calibrated. Pairs with Xu et al.
  (MIXPRS, *Nat Genet*) and the Bledsoe et al. multi-ancestry TWAS
  paper below as the "PRS methodology reset" cluster for this window.
  **HIGH.**
- **Two GLP-1 × autoimmune target-trial-emulation papers land in the
  same window.** Dai et al. — GLP-1 RA CV outcomes in obesity +
  autoimmune disease (2026) and Yeh et al. — adjunctive GLP-1 in IBD +
  obesity/diabetes (*Clin Gastroenterol Hepatol*, 2026). Both use TTE.
  Together they mark the GLP-1 × autoimmune subthread as an emerging
  field-level pattern (matching your active drug threads: GLP-1 RA,
  IBD as autoimmune). **HIGH, paired.**
- **HPO-anchored rare-disease drug repurposing hits the sweet spot of
  your drug-repurposing thread.** Schilder, Murphy, Dash, Zhang et al.
  — *Cell type-specific contextualisation of the human phenome:
  towards the systematic treatment of all rare diseases* (*Genome
  Medicine*, 2026) — maps HPO phenotypes to single-cell atlases to
  generate cross-rare-disease repurposing hypotheses. Explainable,
  ontology-anchored, rare-disease-focused — three of your four
  high-priority angles in one paper. **HIGH.**
- **arxiv-digest window: 14 days with ≥1 relevant paper, biggest single
  day 7/1 (7 papers).** Notable arxiv-only on-thread finds not covered
  by scholar alerts: the *Prior-informed conditional GGM on UK Biobank
  proteomics* paper (Mapelli et al., 7/1) and *PREDIKTOR* (patient-KG
  aligned with LINCS L1000 perturbations for drug response, Bang et
  al., 7/7). Enhancing-comorbidity-network paper (Fontana et al., 7/7)
  is a direct hit for the multimorbidity clustering thread.

---

## PheWAS / phecodes / penetrance / PheRS

### 1. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
Baya, Lassen, Hill, Venkatesh, Currant et al. — *American Journal of Human Genetics*, 2026.
**Threads:** PheWAS methodology (residual-as-signal), PRS + rare-variant stacking, rare disease.
**Feed saturation:** Six feeds — Montgomery (×3 dates), Chenjie Zeng-related, Bastarache-related, Jian Yang-related, Hripcsak citations, Denny citations.

The paper inverts the usual PRS→outcome direction. For each individual,
compute the residual between measured phenotype and PRS-predicted
phenotype; individuals with large negative or positive residuals
("polygenic outliers") are enriched for damaging rare variants in
Mendelian disease genes. In effect: PRS acts as a *background subtractor*,
and the residual is a monogenic-disease-flag score. This is the exact
inference logic that penetrance estimation with monogenic + polygenic
components has been reaching for — and now there's a Nature-family paper
that formalizes it end-to-end. Priority read; likely to become a
reference-class citation for the PRS-anchored-monogenic-detection frame.

### 2. Outcome and Exposure Polygenic Risk Scores Can Help Reduce Information Bias and Selection Bias in Regression Estimates From Biobank Data
Salvatore, Kundu, Du, Friese, Mondul et al. — *Genetic Epidemiology*, 2026.
**Threads:** PheWAS methodology, biobank bias correction, causal inference.
**Feed saturation:** "2 new citations to articles by Chenjie Zeng" (6/29) + Chenjie-related.

Uses outcome- and exposure-PRSs as auxiliary instruments to correct
information bias (misclassification) and selection bias (healthy-volunteer,
non-random participation) in biobank regressions. Cites your work.
Directly addresses the two headline biases you keep flagging in
AoU/UKB analyses. Should be read alongside Wang et al. (AoU reweighting,
below) as complementary bias-correction toolkits: Salvatore et al.
correct at the estimator level using PRS instruments; Wang et al.
correct at the sample level using post-stratification.

### 3. Determination and GWAS validation of optimal minimal phecode count for eye disease cohort generation
Padovani-Claudio, Lewis, Bastarache, He — *IOVS*, 2026.
**Threads:** PheWAS methodology, EHR phenotyping.
**Feed saturation:** Lisa Bastarache new articles (7/1).

Empirically calibrates the ≥N-occurrence threshold for phecode-based
case ascertainment in eye disease and validates the resulting cohorts
via GWAS replication. Directly interrogates the ≥2-count rule that most
phecode-based studies apply as default — the paper likely produces
disease-family-specific calibration curves useful for BioVU / AoU work.
Bastarache-group work, high fidelity to the phecode ecosystem.

### 4. Domain-aware matrix completion for phenotype imputation using electronic health record data with applications in genomic research
Wu, Lee, Abiri, Ionita-Laza — *Annals of Applied Statistics*, 2026.
**Threads:** PheRS-adjacent methodology, EHR phenotyping, genetic epi.
**Feed saturation:** Denny (7/14, 6/29), Bastarache-related (6/29).

Matrix-completion imputation for missing EHR phenotypes, targeted at
downstream genomic association studies. Solves the "wide phecode matrix
is very sparse and MNAR" problem that PheRS and rare-variant burden
methods trip over. Likely usable as a preprocessing layer for PheRS
computation on AoU/UKB/BioVU phecode grids.

### 5. Rare-variant risk scores complement common-variant polygenic scores for disease risk prediction and stratification
Qin, Wu, Yang, Cheng, Feng, Yu, Ge et al. — *medRxiv*, 2026.
**Threads:** Rare-variant + common-variant risk stacking, PheWAS methodology.
**Feed saturation:** Karczewski-related (7/4), Denny-related (7/4).

Constructs rare-variant burden scores (RVRS) and shows additive risk
stratification when combined with common-variant PRS across a bank of
diseases. Direct continuation of the "monogenic + polygenic composite
risk model" thread — will pair with Baya et al. (above) as the two
complementary framings (residual anomaly vs. additive burden).

### 6. PGS Browser: a public platform for personalized polygenic score analysis and interpretation
Kolosov, Reeve, Briotta Parolo, Kurki et al. — *Nature Communications*, 2026.
**Threads:** PheWAS-of-PRS, genetic epi.
**Feed saturation:** Mark Daly new articles (6/27), "phenome wide association studies" keyword (6/26).

FinnGen-linked public platform that runs PheWAS-of-PRS analyses and
returns personalized PGS interpretations. Worth benchmarking against
any in-house PheWAS-of-PRS pipeline; the interface + underlying summary
statistics may be reusable as a comparator or ground-truth reference for
AoU/BioVU replications.

---

## Biobanks (All of Us / UK Biobank) — infrastructure & representativeness

### 7. A comparison of Fast Healthcare Interoperability Resources and Observational Medical Outcomes Partnership electronic health record data within the All of Us Research Program
Patterson, Minto, Beaton et al. — 2026.
**Threads:** All of Us, OMOP.
**Feed saturation:** Triple-feed — Hripcsak (6/29), Patrick Ryan-related (6/29), Pascal Brandt-related (6/29); plus AoU keyword feed (6/28).

Head-to-head comparison of FHIR vs. OMOP representations of AoU EHR
data. Both are on the platform and analysts routinely pick one; this
paper quantifies concordance and where the two data models disagree.
Foundational reference — should be pinned to any AoU EHR project
CLAUDE.md.

### 8. Can the All of Us sample be reweighted to mirror a nationally representative sample? A comparison of mortality predictors
Wang, Buto, Ferguson, Chen, Pederson et al. — *Epidemiology*, 2026.
**Threads:** All of Us, selection bias.
**Feed saturation:** Denny-related (7/11) + Chenjie-related (7/11).

Post-stratification / reweighting of AoU against NHIS to correct
healthy-volunteer bias, evaluated against mortality-predictor
consistency. The most direct methodological engagement so far with
the AoU representativeness problem. Read as a pair with Salvatore et
al. (paper #2): sample-level reweighting vs. estimator-level PRS-
instrument correction.

### 9. Cardiovascular Disease Subtypes and Alzheimer's Disease: Phenotypic and Genetic Associations in the UK Biobank and All of Us Research Program
Toyli, Zhao, Su, Shen, Deng, Chen et al. — 2026.
**Threads:** All of Us + UK Biobank cross-biobank, genetic epi, multimorbidity.
**Feed saturation:** Chenjie-related (6/23).

Cross-biobank AoU + UKB phenotype-and-genetics analysis of CVD subtypes
vs. AD. Notable because the UKB + AoU cross-biobank design is exactly
the stack you routinely use — a good methods-template reference for
harmonizing phecodes and PRS across the two platforms.

### 10. Documented clinical genetic testing among carriers of hereditary breast and ovarian cancer variants: Ancestry and socioeconomic disparities in the All of Us research program
Sathipati et al. — 2026.
**Threads:** All of Us, variant interpretation follow-through, ML for precision health.
**Feed saturation:** Denny-related (7/6, 7/10).

Ancestry and SES disparities in genetic-test uptake among HBOC pathogenic
variant carriers in AoU. Direct hit on the ascertainment / clinical
follow-through gap that under-counts affected carriers in AoU-based
penetrance work — the "denominators are wrong" problem operationalized
with numbers.

### 11. Computational phenotyping of sexually transmitted infections with the All of Us Research Program from 2010 to 2023
Shi, Xia, Weissman, Li, Yang — *JAMIA open*, 2026.
**Threads:** All of Us, EHR phenotyping.
**Feed saturation:** Denny-related (7/13), Chenjie-related (7/13); plus AoU keyword feed (7/12).

Rule-based EHR phenotypes for STIs across 13 years of AoU EHR data — a
concrete case study of AoU phenotyping over a long horizon. Useful as a
template for temporally deep phenotype development on the AoU CDR.

---

## EHR phenotyping & OMOP

### 12. PhenoAgent: agentic LLM framework for phenotyping electronic health records via structured query decomposition and self-correction
Kashiwada, Sakurai, Yokokawa, Ando et al. — 2026.
**Threads:** EHR phenotyping (LLM), OMOP.
**Feed saturation:** Hripcsak-related (7/5).

Agentic LLM that decomposes phenotype definitions into structured
queries and self-corrects on execution failure. Exemplar of the current
LLM-agent-for-computable-phenotype wave; important comparator for any
LLM+phecode work you'd propose. Worth checking whether the decomposition
schema is publishable / reusable.

### 13. TimeX: Phenotype Onset Extraction from Clinical Narratives
Chen, Jiang, Nguyen, Ta, Wang — *npj Health Systems*, 2026.
**Threads:** EHR phenotyping (NLP), PheRS index-date methodology.
**Feed saturation:** Wendy Chung-adjacent (6/23), Chute citations (6/23).

NLP extraction of phenotype onset dates from clinical notes. Directly
addresses the phecode-incidence-date problem that PheRS and time-to-
event phecode analyses require. Onset extraction has been the weakest
link in EHR-derived cohorts; this is a plausible tool to plug in.

### 14. An EHR-based framework for modeling growth curves and constructing growth centile charts for genetic disorders
Shyr, Tinker, Brown, Wright, Peterson — *npj Genomic Medicine*, 2026.
**Threads:** EHR phenotyping, rare disease.
**Feed saturation:** Bastarache new articles (7/6).

Vanderbilt EHR-derived growth-curve modeling to build disorder-specific
centile charts for rare genetic diseases. A methodological complement
to PheRS — offering a *quantitative-trait*-based phenotype for rare
disease alongside phecode-based case definitions.

---

## Causal inference & pharmacoepidemiology

### 15. Bleeding Risk With Apixaban Versus Rivaroxaban: A Reference Trial Emulation Predicting the Results of COBRRA-VTE and COBRRA-AF
Mahesri, Schneeweiss, Lin, Zabotka — *Circulation*, 2026.
**Threads:** Target trial emulation.
**Feed saturation:** Patrick Ryan-related (7/11).

Prospective target-trial emulation in US claims used to *predict*
the results of ongoing RCTs (COBRRA-VTE and COBRRA-AF). This is the
canonical use of TTE — as pre-registered RCT prediction — and the
paper is a template for future drug-thread TTEs. Cite alongside
Hernán's target-trial framework as the exemplar.

### 16. Real-world performance of large-scale propensity score adjustment strategies: Matching, weighting, and stratification
Li KM, Schuemie, Ryan, Zhang, Chen — 2026.
**Threads:** Causal inference (IPW).
**Feed saturation:** Patrick Ryan (7/5), Hripcsak (7/5).

OHDSI benchmark of PS strategies (matching / weighting / stratification)
across many drug-outcome studies. Empirical PS-method calibration from
the OHDSI leadership team — useful for method choice on AoU/BioVU drug
studies. Pairs with the Karim & Hu plasmode study in METHODS-WATCH
below.

### 17. Glucagon-Like Peptide-1 Receptor Agonists and Cardiovascular Events in Adults With Obesity and Autoimmune Disease: A Target Trial Emulation
Dai, Lee, Natalie, Jackson, Pham, Levine et al. — 2026.
**Threads:** GLP-1 RA pharmacoepi, autoimmune/IBD overlap.
**Feed saturation:** Patrick Ryan-related (7/6).

GLP-1 RA vs. non-user CV outcomes among adults with obesity + autoimmune
disease using TTE. Direct hit on the GLP-1 × autoimmune subthread.

### 18. Adjunctive GLP-1 Receptor Agonists in Patients with Inflammatory Bowel Diseases and Obesity and/or Diabetes: A Target Trial Emulation
Yeh, Ahuja, Patel, Xu, Park, Gold et al. — *Clinical Gastroenterology & Hepatology*, 2026.
**Threads:** GLP-1 RA pharmacoepi, IBD.
**Feed saturation:** Miguel Hernán citation feed (6/21).

TTE of GLP-1 RA add-on in IBD patients with metabolic comorbidities.
Second GLP-1 × IBD/autoimmune TTE in the window (with #17), marking
an emerging pattern — worth watching whether a coordinated set of
TTEs on GLP-1 across autoimmune subtypes is forming.

### 19. Sodium-Glucose Cotransporter 2 Inhibitors and Dementia Risk in Patients With Psychiatric Disorders
Liebers, He, Betensky, Zheng et al. — *JAMA Network Open*, 2026.
**Threads:** SGLT2 pharmacoepi.
**Feed saturation:** Miguel Hernán citation feed (7/4).

SGLT2i vs. comparator new-user cohort on dementia risk in a psychiatric
population. Adds to the SGLT2i-and-dementia body relevant to your active
drug threads.

---

## Genetic epidemiology (GWAS / PRS / TWAS / cross-ancestry)

### 20. Distinct genetic architecture in the tails of complex traits
Souaiaia, Wu, Ori, Choi, Hoggart et al. — *Nature*, 2026.
**Threads:** GWAS / PRS calibration.
**Feed saturation:** Montgomery-related (6/25, 6/27).

Genetic architecture at the extremes of quantitative traits differs
from the bulk — with direct implications for how the top 1-5% of a
PRS distribution (the *clinical decision* slice) should be modeled and
calibrated. Should influence any PRS-based screening threshold design.

### 21. MIXPRS enables multi-population and multi-method polygenic risk scores using summary statistics
Xu, Dong, Zeng, Bian, Zhou, Guan, Zhao — *Nature Genetics*, 2026.
**Threads:** PRS methodology, cross-ancestry.
**Feed saturation:** Triple-feed — Jian Yang-related (×3 dates: 7/4, 7/6, 7/10). (Xiang Zeng is co-author — not Chenjie.)

Combines multiple PRS methods across ancestries using only summary
statistics. Sets a new baseline for multi-ancestry PRS construction —
directly relevant to any AoU / UKB / BioVU PRS work aiming for
portability across ancestries.

### 22. Multi-ancestry gene expression models amplify transcriptome-wide association study discovery and validation
Bledsoe, Watkins, Bowen-Moore, Shaw et al. — *Nature Communications*, 2026.
**Threads:** TWAS, cross-ancestry.
**Feed saturation:** Karczewski-related (7/10), Chenjie-related (7/10).

Trains expression-prediction models across ancestries to power TWAS
discovery and validation. Vanderbilt-adjacent multi-ancestry TWAS work,
directly on your cross-ancestry interest.

### 23. Multi-ancestry polygenic risk score methods improve glaucoma prediction across diverse populations in three large biobanks
Segre, Bartolo, Aboobakar, Vy et al. — *IOVS*, 2026.
**Threads:** PRS, cross-ancestry.
**Feed saturation:** Ron Do new articles (6/29).

Three-biobank cross-ancestry PRS for glaucoma. Design template — how
to assemble a three-biobank multi-ancestry PRS validation.

### 24. Development and validation of a multiancestry and multitrait polygenic risk score for lung cancer
Zhang, Dai, Gu, Zhao, Christiani, Chen et al. — *Nature Communications*, 2026.
**Threads:** PRS, multi-ancestry, cancer.
**Feed saturation:** Five-feed — Jian Yang cite (7/2), Denny cite (7/2), Denny-related (7/2), Karczewski-related (7/2), Bastarache-related (7/2).

Multi-trait, multi-ancestry PRS for lung cancer with cross-cohort
validation. Heavily saturated across feeds; sets the current bar for
multi-ancestry cancer PRS. Directly germane to your cancer PRS interests.

### 25. Integrating social determinants of health and genetic risk in disease risk models
Biji, Ferar, Pejaver, Kenny, Liu, Asgari — *AJHG*, 2026.
**Threads:** PRS + SDoH stacking, ML for precision health.
**Feed saturation:** Triple-feed — Bastarache cite (6/27), Denny-related (6/27), Karczewski-related (6/27).

Combines SDoH with polygenic risk in prediction models across diseases.
PRS + SDoH integration has been a live gap in AoU work; this will likely
become an anchor citation for stacked-risk-model discussions.

### 26. Analysis of 173,303 exomes and genomes in the Pakistan Genome Resource
Koch, Khalid, Khan, Bandyadka, Doyon et al. — *Nature*, 2026.
**Threads:** LOFTEE / pLoF, ancestry, variant interpretation.
**Feed saturation:** Denny cite (6/21).

Large-scale South Asian variant catalog with novel biallelic LoF
findings. The gnomAD-adjacent underrepresented-population sequencing
resource of the year; expands the reference space for ancestry-aware
variant interpretation and pLoF burden analyses.

---

## Variant interpretation (ACMG / ClinGen / VUS)

### 27. Automated reanalysis of genomic data for rare disease diagnostics at scale
Welland, Ahlquist, De Fazio, Austin-Tse et al. — *Nature Medicine*, 2026.
**Threads:** Variant interpretation, rare disease.
**Feed saturation:** Heidi Rehm new articles (6/29).

Automated periodic reanalysis pipeline for unsolved rare-disease
exomes/genomes with LLM assistance. Broad-adjacent ACMG-scale
reanalysis tooling; template for the downstream VUS-resolution
workflows that any large-cohort penetrance program must support.

### 28. AI-CURA, an automated LLM workflow for high-accuracy genetic variant classification
Ma, Fong, Lai, Wu, Hue, Ying, Chen et al. — *Science Translational Medicine*, 2026.
**Threads:** Variant interpretation (ACMG/AMP), LLM extraction.
**Feed saturation:** Variant-interpretation keyword feed (6/28).

End-to-end LLM pipeline classifying variants under ACMG/AMP with
reported high accuracy. The class of tool your monogenic penetrance
work depends on downstream; worth benchmarking against InterVar and
ClinGen VCEP outputs.

### 29. Harmonizing standards and resources for the medical genome
Ashley, Alizadeh, Armitage, Bhatt et al. — *Nature*, 2026.
**Threads:** Variant interpretation, clinical genomics standards.
**Feed saturation:** Heidi Rehm new articles (7/5).

Position paper on clinical-grade genome standards. Sets the standards
discussion for ACMG/ClinGen infrastructure and is likely to be cited
extensively in the coming quarter's ACMG/AMP papers.

### 30. CATVariant: a web server for integrated protein variant interpretation across sequence, structure, population, and clinical evidence
Ngo, Amini, Vorobyov, Clancy — *NAR*, 2026.
**Threads:** Variant interpretation.
**Feed saturation:** Karczewski-related (6/23).

Unified web tool aggregating sequence / structure / population / clinical
evidence per variant. Candidate front-end for the VUS resolution
workflows Chenjie's group runs on cancer / cardiac / rare-disease VUS.

### 31. When Genomic Reanalysis Leaves the Laboratory—Clinical Genetics in the Age of Consumer AI
Finlayson, Rehm — *NEJM AI*, 2026.
**Threads:** Variant interpretation, clinical genomics policy.
**Feed saturation:** Heidi Rehm new articles (6/23).

Commentary on consumer AI reanalyzing raw genomic data outside clinical
labs. Rare NEJM AI perspective piece on ACMG / consumer-genomics
fault lines; useful for framing when discussing return-of-results
policy in AoU / BioVU.

---

## EHR foundation models

### 32. Uncertainty-calibrated adaptation of clinical transformer foundation models enhances in-hospital mortality and hospital readmission prediction
Chung, Yoon — *npj Health Systems*, 2026.
**Threads:** EHR foundation models, calibration / ML for precision health.
**Feed saturation:** Yuan Luo-cite (7/13).

Calibration-aware fine-tuning of clinical foundation models for
mortality and readmission. One of the few papers combining EHR
foundation models with the calibration / HTE angle you keep flagging —
important for arguing FMs into decision-relevant use.

### 33. Cohort-Anchored Foundation Models for Electronic Health Records: From Risk Scores to Auditable Peer Cohorts
Zheng — *arXiv* 2606.21885, 2026.
**Threads:** EHR foundation models, ML for precision health.
**Feed saturation:** Hripcsak-related (6/29) + FM+EHR keyword (6/28).

Cohort-anchored FM that emits auditable peer cohorts alongside risk
scores. Interpretable-cohort framing for EHR FMs — CLMBR / MOTOR /
EHRSHOT lineage with a transparency angle; useful precedent for any
FM work aiming at clinical adoption.

---

## Drug repurposing (KG / GNN / agent)

### 34. Cell type-specific contextualisation of the human phenome: towards the systematic treatment of all rare diseases
Schilder, Murphy, Dash, Zhang et al. — *Genome Medicine*, 2026.
**Threads:** HPO / ontologies, drug repurposing (rare disease), rare disease.
**Feed saturation:** Bastarache-related (7/1).

Maps HPO phenotypes to single-cell atlases to generate cross-rare-disease
repurposing hypotheses. Hits three of your four high-priority drug-
repurposing angles at once: explainable, ontology-anchored, rare-disease-
focused. **Top drug-repurposing pick of the window.**

### 35. An AI agent for treatment reasoning over a biomedical tool universe
Gao, Noori, Zhu, Ginder, Kong, Su, Zitnik — 2026.
**Threads:** Drug repurposing (KG + agentic).
**Feed saturation:** Marinka Zitnik new articles (7/4).

LLM agent that reasons over drug / target / knowledge-graph tools for
treatment recommendation. A leading example of tool-augmented drug-
repurposing agents that matches your "explainable + clinical loop"
criterion.

### 36. Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations (PREDIKTOR)
Bang, An, Sung, Yun, Kim, Lee — *arXiv* 2607.04557, 2026-07-06.
**Threads:** Drug repurposing (KG / GNN with explainable output), ML for precision health.
**Feed saturation:** arxiv-digest 7/7.

Aligns patient-specific KG with LINCS L1000 perturbation embeddings
via CLIP-style contrastive loss for drug response prediction,
validated on TCGA + I-SPY2. Explainable-KG drug-response predictor
with a clinical-loop validation — directly on your explainability
criterion.

### 37. Empowering clinical trial design with agentic intelligence and real-world data
Li, Pan, Rajendran, Zang, Wang — *Nature Communications*, 2026.
**Threads:** Causal inference, clinical trial design, ML for precision health.
**Feed saturation:** Fei Wang new articles (7/13).

Agent + RWD pipeline for automating clinical trial design.
Complements the TTE thread — bridges LLM agents into trial-design work.

---

## Multimorbidity / chronic disease clustering

### 38. Enhancing comorbidity network inference with risk-enriched health trajectories embedding
Fontana, Mapelli, Di Angelantonio, Ieva — *arXiv* 2607.04702, 2026-07-06.
**Threads:** UK Biobank, multimorbidity, chronic disease clustering.
**Feed saturation:** arxiv-digest 7/7.

Gaussian Graphical Models with clinical-prior Lasso on UK Biobank
cardiometabolic trajectories. Yields four progression phenotypes with
distinct survival. Direct hit for the multimorbidity-clustering thread
with the substrate (UKB) you actively use.

### 39. Prior-informed conditional Gaussian graphical models: an application to protein interaction network reconstruction
Mapelli, Massi, Cuccuru, Di Angelantonio, Ieva — *arXiv* 2606.31805, 2026-06-30.
**Threads:** UK Biobank, genetic epi, multimorbidity.
**Feed saturation:** arxiv-digest 7/1.

Prior-informed conditional GGM applied to UK Biobank cardiometabolic
proteomics (n=49,129), identifying 34 network-central T2D biomarkers.
Companion method to #38 from the same group.

### 40. Unsupervised characterization of 100,272 EHR patients identifies high-risk groups and comorbidities linked to premature aging
Xian, Smoller, Luo, Walunas, Liu, Khan et al. — *npj Digital Medicine*, 2026.
**Threads:** Multimorbidity, chronic disease clustering.
**Feed saturation:** Yuan Luo new articles (6/29).

Large-scale unsupervised clustering of EHR trajectories surfacing
premature-aging comorbidity subtypes. Broad exemplar for the
unsupervised-clustering framing across a very large EHR corpus.

---

## Also-cites-you (context, not for reading list)

### 41. DRIVE v3: haplotype-clustering methods for IBD
Baker et al. — *Genetic Epidemiology*, 2026. **Cites Chenjie Zeng.**
Methodological haplotype-clustering paper for identity-by-descent
detection. Contextual; likely a methods-tools citation.

### 42. Causal ML / AI for precision medicine (thesis)
Sriram — 2026. **Cites Chenjie Zeng.**
Thesis-level contextual citation.

---

## METHODS-WATCH

- **Causal Inference with Multiple Misclassified Exposures: A Control
  Variate-Adjusted Calibration Weighting Approach** (Murali, Barnatchez,
  Hoppe, Wagner, Keller, Josey — *arXiv* 2606.23656, 6/22; arxiv-digest
  6/23). Double-robust estimator for misclassified exposures, applied
  to CF (throat swab vs. sputum for Pseudomonas). Both methods-watch
  and CF-thread relevant — arguably HIGH for the CF subthread.
- **Which Regularized Propensity-Score and Doubly Robust Methods Are
  Best Calibrated When Exposures or Outcomes Are Rare? A Plasmode
  Study of Proxy-Based Confounding Adjustment** (Karim, Hu — *arXiv*
  2607.07065, 7/8; arxiv-digest 7/9). Directly relevant to rare-
  exposure AoU/BioVU drug studies.
- **Residual-on-Residual Regression as a Tool for Effect Estimation in
  Observational Data** (Naimi, Jin, Yu, Parisi, Bodnar — *arXiv*
  2606.30976, 6/29; arxiv-digest 7/1). Simple, stable alternative to
  AIPW/TMLE under weak positivity.
- **The Agentic Garden of Forking Paths** (Miao, Pritchard, Zou —
  *arXiv* 2607.01507, 2026). LLM-agent-driven exploration of the
  multiverse of analytic choices. Feed saturation: Pritchard (7/6),
  Zou (7/6). Any TTE / PheWAS analysis plan should be stress-tested
  against this framing.
- **Position: Benchmarks Cannot Establish Deployment Readiness of
  Clinical AI** (Zhang, Jeong, Salaudeen, Gerych, Shah — *ICML 2026*).
  Nigam Shah's position paper: benchmark performance ≠ deployment
  readiness. Useful anchor citation for the calibration / decision-
  curve arguments in the ML-for-precision-health thread.
- **Causal Inference and Digital Twins: A Roadmap for the Future of
  Clinical Trials** (Ruhrberg Estévez, Peck, McKinney, Weatherall et
  al. — *npj Digital Medicine*, 2026). Feed: van der Schaar (6/29).
  Bridges causal inference with digital-twin simulation.
- **Causal ASCEND: Scalable Two-tier Causal Discovery on High
  Dimensional Multi-omics Data** (Asiedu, Watson — *arXiv* 2607.04527,
  7/5; arxiv-digest 7/7). Two-tier causal discovery exploiting SNP /
  methylation → expression ordering; scalable to genomics-scale
  conditioning sets.

---

## arxiv-digest pipeline notes

Window: 27 daily digests, 2026-06-21 → 2026-07-17. No fetch failures
this window (contrast with 2026-06-20 which had 3/4 category timeouts).

**Days with ≥1 relevant paper (14 days):** 6/23 (2), 6/25 (2), 6/26 (1),
6/30 (4), **7/1 (7 — biggest single day of the window)**, 7/2 (1),
7/3 (1), 7/7 (3), 7/8 (1), 7/9 (1), 7/14 (1), 7/15 (1), 7/16 (1),
7/17 (1).

**Dry days (13):** 6/21, 6/22, 6/24, 6/27, 6/28, 6/29, 7/4, 7/5, 7/6,
7/10, 7/11, 7/12, 7/13 — standard "no relevant papers" stubs, pipeline
healthy. Weekend / holiday-adjacent bias consistent with historical
patterns (weekends surface fewer q-bio submissions).

**On-thread arxiv-only picks called out in body:** #33 (Cohort-Anchored
FM, 6/29 → arxiv-digest via later date), #36 (PREDIKTOR, 7/7), #38
(Fontana comorbidity networks, 7/7), #39 (Mapelli GGM on UKB proteomics,
7/1), plus the four METHODS-WATCH arxiv finds.
