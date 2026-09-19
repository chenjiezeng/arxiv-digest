# Research digest report — 2026-09-19

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-19 12:40Z** (~18 days since the
last research-digest report, covering eighteen arxiv-digest cron runs
and roughly a dozen Google Scholar alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-18.md`) | 09-01 → 09-18 daily crons | 18 daily runs. Dry days (0 papers): 09-03, 09-05, 09-06, 09-08, 09-12–09-15 (weekend gaps and quiet stretch). Non-dry days: 09-01 (1), 09-02 (1), 09-04 (2), 09-07 (1), 09-09 (2), 09-10 (1), 09-11 (3), 09-16 (2), 09-17 (1), 09-18 (2). Highest-signal picks flagged below in the arxiv-digest cluster. |
| No `arxiv-digest` email hits from GitHub | — | Confirmed again this window: `from:notifications@github.com` × `arxiv-digest` returned zero threads. The pipeline commits its output to this repo; on-disk digests *are* the feed. |
| Google Scholar alerts (09-18 batch, 23:18Z + 16:43Z) | 09-18 | 40+ feed fires. The 16:43Z author-feed sweep dropped Tsuo et al. AoU-PGS *Nature Genetics* across three feeds (Denny, Karczewski, Zeng-related). Bastarache 09-18: Armstrong et al. functional-annotation ancestry-specific stroke PRS. Denny/Karczewski/Zeng-related: Nam et al. medRxiv novel T1D PS in diverse populations. Kai Wang: Ma et al. long-read RNA-seq splicing outliers in rare-disease trios. Ryan: Kim et al. ETI on work productivity in Canadian CF cohort. Callahan: Yao et al. cross-scale ML for polymers (off-topic). Zitnik: Gene-Chronos scFM developmental time (off-topic disease). |
| Google Scholar alerts (09-17 batch, 10:48Z) | 09-17 | 8 keyword feeds fired: knowledge graph (Mazu culture — off-topic), autoimmune (CRISPR review — off-topic), Foundation models + EHR (multimodal healthcare intro — off-topic), EHR (care-gap detection AI, timely), rare diseases (methodological guidance scoping review — methods-watch), drug repurposing (MAFLD repurposing evidence — methods-watch), variant interpretation (SCN4A channelopathy — methods-watch), AoU (spinal deformity mental-health TTE letter). |
| Google Scholar alerts (09-16 batch, 06:34Z) | 09-16 | 10 keyword feeds: rare diseases (LatAm scoping — off-topic), autoimmune (Kikuchi-Fujimoto case — off-topic), mendelian (multi-omics MR lipid-brain-kidney — direct hit for cross-trait MR), EHR (FHIR-medical TV integration — off-topic), knowledge graph (urban RegionKG — off-topic), variant interpretation (Osteopetrosis CLCN7 — case study, methods-watch), Foundation models + EHR (FHIR data engineering — off-topic), UK Biobank (accelerometer × pericardial adiposity — methods-watch), AoU (Krueger PWAS thesis — direct hit for PWAS in AoU + multi-ancestry proteomics), drug repurposing (pyroptosis-oriented glioma diacerein — methods-watch). |
| Google Scholar alerts (09-15 batch, 17:30Z) | 09-15 | 20+ author-feed sweep. Direct hits: Kai Wang / Kai Wang author feed → Pitsava et al. long-read genome sequencing for rare-disease diagnosis (medRxiv). Miguel Hernán → Zhang et al. hip PJI single vs two-stage TTE emulation using EHR (INFORM). Also Shi et al. AJE MR questions review. George Hripcsak / Ryan → Islam et al. HSV-1 × dementia RWE EHR cohort; Schulte-Althoff et al. SHAP fall risk from EHR. Karczewski → Park et al. Trans Psych OCD cross-ancestry / cross-disorder PRS transferability. Ryan → Islam HSV-1 (dementia RWE, methods-watch). |
| Google Scholar alerts (09-12 batch, 19:03Z + 10:55Z) | 09-12 | Very high-signal batch. The 10:55Z sweep dropped **Zeng, Waxse, Denny — npj Digital Public Health "Robust replication of associations across patient-mediated and provider-sourced EHR data in AoU"** simultaneously across the Chenjie-Zeng, Denny, and 1-new-citation feeds. Blostein et al. medRxiv sex-stratified 508-trait EHR quant-trait GWAS. Hernán → Zhang et al. hip PJI TTE (repeat). Ryan/Brandt → CDSL COVID EHR-imaging dataset. The 19:03Z keyword sweep also dropped Momenzadeh et al. Sci Rep causal ML for ICU discharge; Chiu et al. JAMA Cardiol CHIP outcomes-trial design; Liu et al. DrugReason KG+LLM repurposing; Carrasco-Zanini et al. Sci Transl Med proteomics for undiagnosed rare disease; Hwang et al. Genet Med UDN diagnostic strategies. |
| Google Scholar alerts (09-07/09-08 batches) | 09-07 → 09-08 | Bastarache 09-07 (Hysong et al. AJHG **Phenome- and laboratory-wide meta-analyses of sickle cell trait**) — the anchor PheWAS/LabWAS paper for this window; also cited by Denny feed 09-07. Karczewski 09-07: Loay et al. AJHG mutation-rate heterogeneity biases variant-effect prediction. Roberts 09-07 (Denny-related): polygenic pharmacotherapy evidence map. Ryan 09-08: Kim et al. ETI work productivity (repeat, first surface). van Hougenhouk-Tulleken 09-08: APOL1 × blood-pressure in South African dialysis cohort. Da Silva Faria 09-08: CHIP × autoimmune hemolytic anemia (Blood Advances). Liu et al. 09-08: Mother-Child AI agent Nature Medicine EHR longitudinal prediction. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twenty-two HIGH items surfaced this window, clustering into eight knots:

**Your own work published (1 item).** **Zeng, Waxse, Denny — *npj Digital
Public Health* 2026 — "Robust replication of associations across
patient-mediated and provider-sourced EHR data in the All of Us research
program"** landed 09-12 across three separate Scholar feeds (your own
"new articles" feed, the Denny feed, and a "1 new citation" feed that
fired simultaneously — the paper is already being read). This is your
own publication, so it doesn't need a detailed report, but flagging its
publication surface here is the point of this section: it is now in the
Scholar graph and citation feeds are firing on it. Downstream, expect
`Knowledge representation in EHRs` and `EHR phenotyping & OMOP`
follow-ups from other groups to reference it. The npj Digital Public
Health venue is new for you and worth citing back in future methods
sections.

**AoU polygenic-prediction blockbuster (1 item).** **Tsuo, Shi, Ge,
Mandla, Hou, Ding et al. — *Nature Genetics* 2026 — "All of Us diversity
and scale yield context-dependent improvements in polygenic prediction"**
(245,388 AoU whole-genome sequences + UK Biobank; multiancestry PRSs for
32 traits/diseases). This lands on three feeds at once (Denny, Karczewski,
Zeng-related) and is the direct-hit paper for `Genetic epidemiology` /
cross-ancestry PRS portability. The "context-dependent" framing —
methodology × ancestry × genetic architecture interactions — is exactly
the tails-and-residuals taxonomy your interests file is tracking. Read
first this window.

**Your PheWAS-infrastructure thread cluster (2 items).** Hysong,
Shuey, Miller-Fleming, Keat et al. — *AJHG* 2026 — **"Phenome- and
laboratory-wide meta-analyses of sickle cell trait reveal multi-system
disease associations"** — the on-brand PheWAS/LabWAS anchor for this
window; sickle-cell trait as the "monogenic-variant-under-population-
screening" exemplar exactly like the malignant-hyperthermia paper from
the last report. Blostein, Bose, Hill, Actkins, Lake et al. — medRxiv
2026 — **"Sex differences in the genetic architecture of clinical
quantitative traits in the electronic health record"** — 508 EHR clinical
traits, sex-stratified GWAS. First author list overlaps with the
Vanderbilt/BioVU circle (Actkins, Lake); this is the sex-difference
companion piece to the traits-in-EHR framing.

**Causal inference & pharmacoepi cluster (3 items).**
Zhang, Li, Su et al. — 2026 — **"Comparative effectiveness of
single-stage versus two-stage revision for hip prosthetic joint
infection: emulation of the INFORM target trial using electronic health
record data"** (Hernán feed) — textbook TTE-emulation-with-EHR paper,
the pattern portable to CFTR-modulator persistence / GLP-1 / statin
studies. Momenzadeh et al. — *Sci Rep* 2026 — **"A causal machine
learning framework for ICU discharge decision support using EHR"** —
causal-ML pipeline for a decision-relevant clinical endpoint, direct
hit for the `Machine learning for precision health` × causal-inference
overlap. Fujita & Hattori — arXiv 2609.17777 — **"Information Set
Emulation: Causal Certificates for AI Derived EHR Features"** — the
missing piece for the `NLP-derived representations from clinical notes`
sub-thread: an explicit typing layer that decides when AI-extracted EHR
features are admissible for causal inference vs. only for prediction,
with cross-fitted AIPW under exchangeability / positivity /
nuisance-consistency. Score 3 on the arxiv-digest fetch (electronic
health records + inverse probability + causal inference) — one of the
highest arxiv-digest scores this window.

**AoU-based studies (3 items).** Krueger — 2026 (thesis) — **"Genetic
Fine-Mapping of the Plasma Proteome Across Multi-Ancestral Populations"**
(AoU PWAS on 10 cardiometabolic phenotypes). Long, Karnati, Ying, Touma,
Smith et al. — *Journal of Human Immunity* 2026 — **"Linkage between
HLA-B8 and HLA-DQ2.5 contributes to ancestry-dependent risk for celiac
disease"** (3,481 AoU CeD cases; 2,899 with an established risk allele —
ancestry-stratified). Jiang, Ding, Han, Liu, Rosenthal, Wang — arXiv
2609.12224 — **"Patient-Reported Survey Data Improve Prediction of
Opioid Use Disorder"** (267,747 AoU participants with documented opioid
exposure, 15,287 OUD cases). All three exercise the AoU "EHR + genetics"
or "EHR + survey" join in exactly the direction you flagged as
`Biobanks with EHR linkage` high-priority.

**Rare-disease diagnostics (5 items).** Carrasco-Zanini, Andrade,
Pietzner et al. — *Sci Transl Med* 2026 — **"Proteomics identify
disease-associated variants in patients with rare diseases undiagnosed
after genome sequencing"** (bridges the `Multi-omics-augmented PRS` and
`Rare disease reanalysis` sub-threads). Pitsava, Bluske, Barrick, De Dios,
Duong et al. — medRxiv 2026 — **"Yield of Long-Read Genome Sequencing
for Rare Disease Diagnosis in Short-Read Genome Negative Cases"**
(complements the reanalysis-at-cohort-scale reference paper in
INTERESTS.md). Ma, Weisburd, DiTroia, Romo, Covill et al. — medRxiv
2026 — **"Long-read RNA sequencing improves isoform and splicing outlier
detection in whole blood from rare disease trios"** (RNA evidence
for splicing-driven VUS — direct hit for `Variant interpretation` ×
`Rare disease`). Hwang, Brown, Baldridge, Baldwin et al. — *Genetics
in Medicine* 2026 — **"Arriving at a diagnosis: Effective strategies used
by the Undiagnosed Diseases Network"** (methods paper for the UDN
diagnostic workflow). Ghasemnejad, Argha, Grosser, Wang, Yang, Porntaveetus,
Roscioli, Lovell, Aarabi, Alinejad-Rokny — arXiv 2609.19569 — **"Large
Language Model Agents for Evidence Based Genetic Disease Severity
Classification"** (ReAct + RAG LLM agent over 10,211 HPO terms using
ACMG-endorsed severity + ACOG QoL criteria; 93.55% accuracy vs
expert-curated cohorts, 95.2% concordance with Mackenzie's Mission gene
list) — a **direct-hit** for your rare-disease auditable-LLM-benchmark
sub-thread (GraphRareBench portable template).

**CHIP / clonal hematopoiesis / APOL1 cluster (4 items).** Chiu, Oren,
Small, Weeks, Marston et al. — *JAMA Cardiology* 2026 — **"Designing
Cardiovascular Outcomes Trials in Clonal Hematopoiesis of Indeterminate
Potential"** (design-primer paper — high signal for the CHIP thread).
Zhao, Ma, Zhao, Zhao, Li, Y et al. — 2026 — **"Association of Clonal
Hematopoiesis of Indeterminate Potential with Cardiovascular Mortality
in Cardiovascular-Kidney-Metabolic Syndrome"** (large prospective).
Da Silva Faria, Moisan, Lecluze, Pincez — *Blood Advances* 2026 —
**"Clonal Hematopoiesis in Autoimmune Hemolytic Anemia"** (extends CHIP
outside cardiovascular endpoints — new autoimmune direction).
van Hougenhouk-Tulleken, Rheeder et al. — *Clinical Kidney Journal*
2026 — **"Blood pressure and APOL1 risk variants in a South African
chronic haemodialysis population of African ancestry"** — on-brand
APOL1 direct-hit study.

**CF / CFTR modulator (1 item).** Kim, Wong, Rayment, Bilodeau, Tullis
et al. — *J Cyst Fibros* 2026 — **"Assessing the impact of elexacaftor/
tezacaftor/ivacaftor on work productivity and activity impairment in
people living with cystic fibrosis in Canada"** — the CFTR-modulator
"psychosocial-and-real-world-outcome" hit you flagged as high-priority.

**Variant interpretation (2 items).** Islam, Alves, Bourbon, Pfisterer
— *Atherosclerosis* 2026 — **"Utilization of Functional Data for LDLR
Variant Classification: Comparative Insights from High-Content Microscopy
and Flow Cytometry"** (ACMG/AMP functional-evidence PS3/BS3 study —
direct hit for `Variant interpretation`). Hull, Mero, Hankey, K Lee,
Sullivan et al. — *Human Genetics* 2026 — **"Development of RS1-specific
ACMG/AMP variant classification criteria with pilot variant curation"**
(new ClinGen VCEP criteria for RS1 — direct hit).

---

Now the detailed reports on each HIGH-priority study, grouped by cluster.

---

## Cluster 1 — Your own work published

### Zeng, Waxse, Denny — *npj Digital Public Health* 2026

**Title.** Robust replication of associations across patient-mediated
and provider-sourced EHR data in the All of Us research program.

**Why this matters for you.** This is your own paper. Landing 09-12
on the Chenjie-Zeng, Denny, and 1-new-citation feeds simultaneously
means the paper is already indexed and picking up traffic. No further
action required, but two secondary observations worth noting:

- npj Digital Public Health is a relatively new Nature journal (Springer
  Nature launched the digital-public-health family in 2024–2025). Track
  it as a home venue for future EHR-representation and patient-mediated-
  data papers you write; the fact that they took this piece is a signal
  it will consider methodologically-focused AoU papers.
- The abstract framing ("HPO-sourced EHRs and patient-mediated EHR data
  … robust replication of associations") is exactly the
  `Concept normalization and vocabulary mappings` × `Fidelity, portability,
  and audit of representations` bridge in INTERESTS.md — you can cite
  yourself in the next audit / drift-across-sites paper.

---

## Cluster 2 — AoU polygenic-prediction blockbuster

### Tsuo, Shi, Ge, Mandla, Hou, Ding et al. — *Nature Genetics* 2026

**Title.** All of Us diversity and scale yield context-dependent
improvements in polygenic prediction.

**Setup.** 245,388 whole-genome sequences from AoU + UK Biobank. 32
traits and diseases. Multiancestry PRSs. Evaluate how ancestry,
methodology, and genetic architecture influence PRS performance.

**Why HIGH.**
- Direct hit for `Genetic epidemiology` × cross-ancestry PRS
  portability, the tails-and-residuals sub-thread, and
  `Biobanks with EHR linkage`.
- 245k WGS is the current-largest AoU WGS release you'd cite for
  cross-ancestry scale; this paper effectively defines the
  state-of-the-art multiancestry PRS reference in AoU going forward.
- "Context-dependent" is the operative word: performance depends on
  ancestry × methodology × trait genetic architecture jointly. This
  aligns with the Nagpal & Gibson *Nature Genetics* 2026 GxE / PGS ×
  exposure interactions framing in your INTERESTS.md — different
  contexts, but the same "portability is not a scalar" argument.
- Ge/Ding/Mandla are the Broad multiancestry-PRS methods circle
  (PRS-CSx and related). Expect a follow-up wave of AoU-based
  disease-specific PRS papers citing this as the reference multiancestry
  scaffold.

**Read priority.** First this window. Skim methods for how the AoU
WGS was subset for training vs. evaluation, and how they defined the
"32 traits" (phecode-based or curated?). If curated, extract the list.

---

## Cluster 3 — Your PheWAS-infrastructure thread

### Hysong, Shuey, Miller-Fleming, Keat et al. — *AJHG* 2026

**Title.** Phenome- and laboratory-wide meta-analyses of sickle cell
trait reveal multi-system disease associations.

**Setup.** Sickle cell trait (heterozygous HBB S allele) as the
exposure; PheWAS (phecode-based) + LabWAS (laboratory-value-wide)
meta-analyses. First author is Miranda Hysong (Vanderbilt / Bastarache
lab). This is the follow-on to the Bastarache PheWAS + LabWAS pattern
you're familiar with.

**Why HIGH.**
- Sickle-cell trait is the paradigm "carrier heterozygote under
  population-screening conditions" phenotype — clinically ascertained
  cohorts underestimate its impact, and PheWAS/LabWAS in biobanks are
  the right instrument.
- The multi-system phenotype spread (renal, cardiovascular, hematologic,
  possibly reproductive) is the signal you'd expect if SCT has
  low-penetrance systemic effects that clinical guidelines have
  underestimated.
- Direct-hit paper for `PheWAS / phecode infrastructure` and specifically
  the "penetrance under population-screening" framing you flagged.
- Same-cohort methodology likely portable to your APOL1, CFTR-carrier,
  and RYR1-MHS work.

**Read priority.** Second this window. Check whether they used
phecodeX or classic phecodes, and whether they meta-analyzed across
BioVU + AoU + UKB (the direction you'd expect).

### Blostein, Bose, Hill, Actkins, Lake et al. — medRxiv 2026

**Title.** Sex differences in the genetic architecture of clinical
quantitative traits in the electronic health record.

**Setup.** Sex-stratified GWAS of 508 EHR quantitative clinical traits.
Author list overlaps with the Vanderbilt / BioVU circle (Actkins, Lake).

**Why HIGH.**
- Sex differences in genetic architecture is a component of the
  broader `Composite risk models` sub-thread you're tracking (Nagpal &
  Gibson-style interactions).
- 508 EHR-derived quantitative traits at scale is a large-N companion
  to any lab-value-based analysis; it also anchors the `Structural and
  temporal representation of the patient timeline` sub-thread — how
  they defined the 508 traits (labs? vitals? note-derived?) is worth
  the read.
- Direct hit for `PheWAS / phecode infrastructure` × sex-specific
  effects.

**Read priority.** Third this window. Extract the trait list definitions
and check overlap with AoU labs you'd want to replicate in.

---

## Cluster 4 — Causal inference & pharmacoepi

### Zhang, Li, Su et al. — 2026 (Hernán citations feed)

**Title.** Comparative effectiveness of single-stage versus two-stage
revision for hip prosthetic joint infection: emulation of the INFORM
target trial using electronic health record data.

**Setup.** Target-trial emulation of the INFORM trial using EHR data
for a comparative-effectiveness question in orthopedic revision surgery.

**Why HIGH.**
- Textbook TTE-emulation-with-EHR — the pattern you want to lift for
  CFTR-modulator persistence, GLP-1 discontinuation, HRT persistence.
- Emulating a specific published RCT (INFORM) rather than a generic
  drug-vs-drug comparison is the harder version of the TTE recipe —
  eligibility, treatment strategies, and outcomes must all mirror the
  published protocol.
- Direct hit for `Causal inference and pharmacoepidemiology` and
  specifically for the target-trial-emulation sub-thread.

**Read priority.** Fourth this window. The methods section (eligibility,
grace period, and how they handled crossover) is the extractable pattern.

### Momenzadeh et al. — *Sci Rep* 2026

**Title.** A causal machine learning framework for ICU discharge
decision support using electronic health records.

**Setup.** Causal-ML pipeline (likely double-ML / causal forest family)
applied to ICU discharge decisions using EHR features.

**Why HIGH.**
- Direct hit for `Machine learning for precision health` × causal ML.
- ICU discharge is a decision-relevant clinical endpoint — matches your
  "ML papers are HIGH when they're tied to a clinical decision"
  criterion in INTERESTS.md.
- Pipeline-level paper; extractable pattern for the "who to treat, when
  to escalate" framing you already emphasize.

**Read priority.** Fifth this window. Extract the causal-ML method
(causal forest? DML? metalearner?), the confounder set, and how they
handled the ICU-specific selection / immortal-time issues.

### Fujita & Hattori — arXiv 2609.17777 (2026-09-15 submission)

**Title.** Information Set Emulation: Causal Certificates for AI
Derived EHR Features.

**Setup.** Introduces "information set emulation": an AI-typed lift
that attaches source evidence, clinical and recording times,
decision-time availability, representation version, proposed causal
roles, and unresolved ambiguity to extracted EHR features under a
locked target trial. Causal certificates record auditable evidence.
Cross-fitted augmented inverse probability weighted (AIPW) estimation
under exchangeability / positivity / nuisance-consistency. Introduces
an EHR compression-drift identity separating frame presence, treatment
assignment, and outcome observation.

**Why HIGH.**
- Arxiv-digest score 3 on `electronic health records + inverse probability
  + causal inference` — the highest single-paper score this window
  from the automated feed.
- Sits precisely at the intersection of `NLP-derived representations
  from clinical notes` (extracted-feature admissibility for downstream
  use) and `Causal inference and pharmacoepidemiology` (when can an
  LLM-derived feature be used as a treatment, a covariate, or an outcome
  in a target trial?).
- "Locked target trial" phrasing is unusually rigorous — the paper
  seems to argue that AI-extracted features need explicit typing
  ("proposed causal roles") before they can be admitted, and provides
  a certificate architecture for this.
- Directly addresses the "AI-extraction is admissible for prediction
  but not automatically for causal inference" concern that you'd need
  to answer whenever an LLM-extracted phecode or HPO term feeds
  downstream causal analysis.

**Read priority.** Sixth this window. This is a small-lab preprint, so
verify identifiability claims carefully — but the framing is worth
extracting as a design pattern for your own EHR representation-and-audit
work. Cite in your next paper on note-derived phecode extraction.

---

## Cluster 5 — AoU-based studies

### Krueger — 2026 (thesis / preprint)

**Title.** Genetic Fine-Mapping of the Plasma Proteome Across
Multi-Ancestral Populations.

**Setup.** PWAS (proteome-wide association study) using AoU on ten
cardiometabolic phenotypes; multi-ancestry.

**Why HIGH.**
- AoU + proteomics is exactly the `Multi-omics-augmented PRS` sub-thread
  (Nightingale NMR / Olink stacked with PGS).
- Ten cardiometabolic phenotypes overlap heavily with what you'd want
  from any AoU PWAS pass (T2D, lipid traits, BP, CKD, likely CAD).
- Fine-mapping across ancestries in the plasma proteome specifically
  is a mid-scale reference for multi-ancestral biomarker discovery.

**Read priority.** Seventh this window. Confirm the ancestry-stratified
sample sizes and which Olink / SomaScan panel was used.

### Long, Karnati, Ying, Touma, Smith et al. — *Journal of Human Immunity* 2026

**Title.** Linkage between HLA-B8 and HLA-DQ2.5 contributes to
ancestry-dependent risk for celiac disease.

**Setup.** 3,481 AoU celiac disease cases; 2,899 carried one of the four
well-established HLA risk haplotypes. Ancestry-stratified analysis.

**Why HIGH.**
- Ancestry-dependent HLA linkage patterns in AoU is a direct
  `Biobanks with EHR linkage` × `Cross-trait shared genetic architecture`
  hit.
- CeD is on the extended autoimmune list; the same ancestry-conditional-
  LD framing is portable to other HLA-driven autoimmune / drug-hypersensitivity
  phenotypes (T1D, ankylosing spondylitis, abacavir-HSR, etc.).
- Case-count (3,481) is substantial for AoU-derived celiac — this is
  now a citeable AoU-CeD-cohort reference paper.

**Read priority.** Eighth this window.

### Jiang, Ding, Han, Liu, Rosenthal, Wang — arXiv 2609.12224 (2026-09)

**Title.** Patient-Reported Survey Data Improve Prediction of Opioid
Use Disorder.

**Setup.** 267,747 AoU participants with documented opioid exposure;
15,287 OUD cases. Compare EHR-only vs. EHR + survey models across 6/12/24-
month lookback windows using logistic regression, RF, XGBoost, LightGBM
family.

**Why HIGH.**
- Directly demonstrates that patient-reported survey data (an AoU-
  distinctive resource) adds predictive signal beyond structured EHR
  codes — same replication-across-data-sources framing as your own
  npj DPH paper, just for prediction rather than association.
- Fits `NLP-derived representations from clinical notes` and `Applications
  to prioritize` (drug-safety surveillance).
- OUD as an outcome is a good stress test — heavily under-coded in
  billing data, so survey augmentation would be expected to help.

**Read priority.** Ninth this window. Extract the survey-item set and
the model-family AUCs — likely portable to CFTR-modulator persistence
or GLP-1 discontinuation prediction as an ablation pattern.

---

## Cluster 6 — Rare-disease diagnostics

### Carrasco-Zanini, Andrade, Pietzner et al. — *Sci Transl Med* 2026

**Title.** Proteomics identify disease-associated variants in patients
with rare diseases undiagnosed after genome sequencing.

**Setup.** Proteomics on patients with rare diseases who remain
undiagnosed after genome sequencing.

**Why HIGH.**
- Bridges `Multi-omics-augmented PRS` (proteomics as evidence) and
  `Rare disease` × `Pre-symptomatic carrier phenoconversion prediction`
  sub-threads.
- Direct-hit for the reanalysis-of-unsolved-cases direction (Uria-Regojo
  medRxiv reference in your INTERESTS.md).
- Sci Transl Med is a high-signal home for translational rare-disease
  work.

**Read priority.** Tenth this window. Check whether they used Olink,
SomaScan, or a targeted panel; and how they linked protein-level
signals back to specific genomic variants.

### Pitsava, Bluske, Barrick, De Dios, Duong et al. — medRxiv 2026

**Title.** Yield of Long-Read Genome Sequencing for Rare Disease
Diagnosis in Short-Read Genome Negative Cases.

**Setup.** Long-read genome sequencing yield in cases negative on short-read
genome sequencing. Diagnostic-yield paper.

**Why HIGH.**
- Companion to the Uria-Regojo mid-scale reanalysis paper in
  INTERESTS.md — same "unsolved-after-standard-workflow" framing but
  with long-read as the added modality.
- Direct-hit for `Rare disease` × VUS-resolution × long-read applications.
- Yield numbers from this paper become the reference you'd cite for
  "what fraction of short-read-negative cases get resolved by long-read"
  in any grant or review.

**Read priority.** Eleventh this window.

### Ma, Weisburd, DiTroia, Romo, Covill et al. — medRxiv 2026

**Title.** Long-read RNA sequencing improves isoform and splicing outlier
detection in whole blood from rare disease trios.

**Setup.** Long-read RNA-seq on whole blood in rare-disease trios; isoform
+ splicing outlier detection.

**Why HIGH.**
- Direct hit for `Variant interpretation` × splicing / RNA evidence for
  VUS resolution (an explicit ACMG PS3 / BS3 direction).
- Long-read RNA-seq is the emerging standard for splicing outlier
  detection and this is a Broad-lineage paper (Weisburd is Broad).
- Whole-blood tractability matters for scaling to biobank cohorts —
  worth checking whether they benchmark against Illumina short-read
  RNA-seq for a fair comparison.

**Read priority.** Twelfth this window.

### Hwang, Brown, Baldridge, Baldwin et al. — *Genetics in Medicine* 2026

**Title.** Arriving at a diagnosis: Effective strategies used by the
Undiagnosed Diseases Network.

**Setup.** Case-series / process paper describing the diagnostic
strategies the UDN uses.

**Why HIGH.**
- Methods paper for the UDN diagnostic workflow — the reference
  citation for anyone wanting to describe how a modern rare-disease
  diagnostic pipeline actually works in practice.
- Overlaps with `Data-driven reanalysis of unsolved cases` sub-thread
  and with any downstream LLM-agent or KG-based rare-disease pipeline
  (portable pattern for evaluation).

**Read priority.** Thirteenth this window. Skim for the taxonomy of
"effective strategies" — extract into a table you can benchmark future
LLM-agent papers against.

### Ghasemnejad, Argha, Grosser, Wang, Yang, Porntaveetus, Roscioli, Lovell, Aarabi, Alinejad-Rokny — arXiv 2609.19569 (2026-09-17)

**Title.** Large Language Model Agents for Evidence Based Genetic
Disease Severity Classification.

**Setup.** Autonomous AI agent integrating ReAct (Reasoning and Acting)
+ RAG (Retrieval-Augmented Generation) to classify 10,211 HPO terms
using ACMG-endorsed severity guidelines and ACOG QoL criteria. Retrieves
PubMed literature, generates interpretable reasoning chains,
independently verifies claims. **Results:** 93.55% accuracy (MCC 0.9237)
at the phenotype level on expert-curated cohorts; 82.6%–91.4% of claims
supported by direct evidence or valid inferences. Gene-level aggregation
across 8,738 pairs identifies 3,283 autosomal recessive pairs with
severe/profound presentations. 95.2% concordance with Mackenzie's
Mission gene list on external validation.

**Why HIGH.**
- Direct-hit for the `Rare disease` × auditable HPO-driven LLM-agent
  benchmark sub-thread you flagged as rising (GraphRareBench template
  in INTERESTS.md).
- The "separable metrics for ranking vs. evidence coverage" framing you
  want is here — claim-support percentages (82.6%–91.4%) are exactly
  the evidence-coverage metric type, distinct from top-level accuracy.
- ACMG-severity + ACOG-QoL scaffolding gives clinical anchoring; the
  external validation against Mackenzie's Mission gives portability
  evidence.
- Combined with the Hwang UDN paper above, this bracket the "manual
  UDN workflow → automated LLM agent" comparison space for a review
  or methods paper.

**Read priority.** Fourteenth this window. Verify the 93.55% accuracy
against expert-curated cohorts is honest (not train-test leaked); check
whether the 82.6%–91.4% claim-support range separates confident from
brittle assertions.

---

## Cluster 7 — CHIP / clonal hematopoiesis / APOL1

### Chiu, Oren, Small, Weeks, Marston et al. — *JAMA Cardiology* 2026

**Title.** Designing Cardiovascular Outcomes Trials in Clonal
Hematopoiesis of Indeterminate Potential.

**Setup.** Design-primer viewpoint / perspective article on how to run
CV outcomes trials in CHIP populations.

**Why HIGH.**
- Direct hit for the CHIP sub-thread.
- JAMA Cardiology tier means this becomes the citeable design reference
  for CHIP RCTs going forward.
- The clonal-selection kinetics + outcomes-window trade-offs that CV
  outcomes trials must handle in CHIP are the same trade-offs you'd
  handle in an LOY-based analog (Li et al. *Atherosclerosis* 2026 LOY
  × PAD in INTERESTS.md).

**Read priority.** Fifteenth this window. Extract the design elements
(eligibility by clone size threshold, endpoint choice, follow-up
duration).

### Zhao, Ma, Zhao, Zhao, Li et al. — 2026

**Title.** Association of Clonal Hematopoiesis of Indeterminate Potential
with Cardiovascular Mortality in Cardiovascular-Kidney-Metabolic
Syndrome: a Large Prospective Study.

**Setup.** Prospective cohort study associating CHIP with CV mortality
in CKM syndrome patients.

**Why HIGH.**
- CHIP × CKM is a joint-condition endpoint framing — cardiovascular +
  kidney + metabolic all interact, and CHIP appears to amplify the
  cardiovascular arm.
- Prospective design is stronger evidence than the case-control /
  cross-sectional CHIP CV literature.
- Direct hit for `Somatic mosaicism` and the CHIP CV thread.

**Read priority.** Sixteenth this window.

### Da Silva Faria, Moisan, Lecluze, Pincez — *Blood Advances* 2026

**Title.** Clonal Hematopoiesis in Autoimmune Hemolytic Anemia.

**Setup.** Investigates CHIP prevalence and effects in AIHA (autoimmune
hemolytic anemia).

**Why HIGH.**
- Extends CHIP outside the cardiovascular endpoint to an autoimmune-
  hematologic condition — new direction in the CHIP literature.
- Bridges `Somatic mosaicism` with the autoimmune / IBD thread.

**Read priority.** Seventeenth this window.

### van Hougenhouk-Tulleken, Rheeder et al. — *Clinical Kidney Journal* 2026

**Title.** Blood pressure and APOL1 risk variants in a South African
chronic haemodialysis population of African ancestry.

**Setup.** APOL1 risk-variant analysis in a South African hemodialysis
cohort, with blood pressure as the co-analyzed exposure.

**Why HIGH.**
- Direct-hit for the APOL1 thread.
- African-continent cohort (rather than African-ancestry-in-US) is
  distinct from the AoU APOL1 studies and gives a portability check for
  the two-risk-allele model.
- Hemodialysis-population framing means these are already advanced-CKD
  patients — different from screening-population penetrance studies.

**Read priority.** Eighteenth this window.

---

## Cluster 8 — CF / CFTR modulator

### Kim, Wong, Rayment, Bilodeau, Tullis et al. — *J Cyst Fibros* 2026

**Title.** Assessing the impact of elexacaftor/tezacaftor/ivacaftor on
work productivity and activity impairment in people living with cystic
fibrosis in Canada.

**Setup.** ETI (Trikafta) impact on work productivity + activity
impairment; Canadian CF cohort.

**Why HIGH.**
- CFTR-modulator × real-world psychosocial-outcomes is exactly the
  angle you flagged as high-priority (`CF / CFTR: modulator pharmacoepi,
  real-world outcomes, modulator eligibility & psychosocial impact`).
- Work-productivity / activity-impairment scales (likely WPAI:CF) are
  patient-reported outcomes — direct hit for the "psychosocial impact"
  direction.
- Canadian data means CFTR-Canada cohort access + likely provincial
  linkages; portable to your BioVU / AoU CF work.

**Read priority.** Nineteenth this window.

---

## Cluster 9 — Variant interpretation

### Islam, Alves, Bourbon, Pfisterer — *Atherosclerosis* 2026

**Title.** Utilization of Functional Data for LDLR Variant
Classification: Comparative Insights from High-Content Microscopy and
Flow Cytometry.

**Setup.** ACMG/AMP functional evidence (PS3/BS3) for LDLR variants
using high-content microscopy vs. flow cytometry as the assay platforms.

**Why HIGH.**
- Direct hit for `Variant interpretation` and specifically the PS3
  functional-evidence tier.
- LDLR is the classical monogenic FH gene; portable to any hereditary-
  cancer or cardiomyopathy VCEP.
- Comparative-assay-platform framing is unusual — most VCEP-guideline
  papers pick one assay; here they benchmark two.

**Read priority.** Twentieth this window.

### Hull, Mero, Hankey, K Lee, Sullivan et al. — *Human Genetics* 2026

**Title.** Development of RS1-specific ACMG/AMP variant classification
criteria with pilot variant curation.

**Setup.** New ClinGen VCEP criteria for RS1 (X-linked juvenile
retinoschisis).

**Why HIGH.**
- Direct hit for `Variant interpretation` × ClinGen VCEP guidelines.
- RS1 is a gene-therapy target — VCEP criteria matter for eligibility
  decisions, which is a downstream clinical-decision use case.
- Adds to the extendable list of ClinGen VCEP references you cite in
  methods sections.

**Read priority.** Twenty-first this window.

---

## Methods-watch / lower-priority (surfaced but not deeply reported)

The following surfaced this window but do not need standalone reports.
Listed for completeness so you can grep back later:

- **DrugReason** (Liu et al. arXiv 2026) — KG + LLM drug repurposing;
  extends the KG-with-explainable-rationale sub-thread of drug
  repurposing but no immediate hook to a tracked disease.
- **Data-driven repurposable drugs for ALS** (Saez-Atienzar et al. npj
  Digital Medicine 2026) — genetics-based screen using 150k samples;
  methods-watch pattern for CFTR- or IBD-analogous scans.
- **Polygenic Pharmacotherapy beyond Single-Gene Rules** (Roberts et al.
  2026) — evidence-map review; methods-watch reference for the
  `Pharmacogenomic modifiers of medication persistence` sub-thread.
- **Multi-Omics MR: lipid × brain-cell × kidney** (Deng et al. Genes 2026)
  — cross-trait MR triangulation exercise; methods-watch reference.
- **Mother-Child AI agent for maternal/infant EHR prediction** (Liu et al.
  Nature Medicine 2026) — LLM-agent + longitudinal EHR + Nature Medicine
  venue; possibly high-priority if they get to phenoconversion trajectory
  prediction, but based on the snippet it's a predictive-rather-than-
  causal application. Skim only.
- **Sanchez-Santos frailty prediction** — off-topic disease for you.
- **HSV-1 × dementia RWE cohort** (Islam et al. via Ryan feed) — off-topic
  disease.
- **Schulte-Althoff fall-risk SHAP EHR** — methods-watch (SHAP-space
  patient profiling from EHR).
- **Park et al. cross-ancestry / cross-disorder OCD PRS transferability**
  (Karczewski feed) — methods-watch for cross-ancestry PRS.
- **Loay et al. AJHG mutation-rate heterogeneity biases variant-effect
  prediction** (Karczewski feed) — methods-watch reference.
- **Novel T1D PGS in diverse populations** (Nam et al. medRxiv, via
  Denny/Karczewski feeds) — methods-watch for diverse-ancestry PGS.
- **Armstrong et al. functional-annotation ancestry-specific stroke PRS**
  (Bastarache feed) — methods-watch.
- **arxiv-digest 09-11 scDEFT IBD counterfactual reasoning** (Devarakonda)
  — IBD-thread relevant, single-cell + drug response + patient
  stratification, worth noting but score-2 arxiv-digest pick.
- **arxiv-digest 09-09 Snel & Schulz UKB training-data attribution for
  Cohen's d** — UKB + biomarker × influence functions, methods-watch
  for effect-size-attribution in normative age models.
- **arxiv-digest 09-16 Wang et al. CF mucociliary NTM digital twin** —
  CF thread, but the digital-twin framing is at the mechanistic-modeling
  end rather than the EHR-derived-twin end you flagged.
- **arxiv-digest 09-11 Hendrix et al. Geospatial FMs beyond social risk
  indices** — foundation-model + place-based health; methods-watch for
  the FM-augmented-index pattern.

---

## Sub-thread coverage this window

| Thread | HIGH items | Notes |
| --- | --- | --- |
| PheWAS / phecode infrastructure | 2 | Hysong SCT PheWAS/LabWAS; Blostein sex-stratified 508-trait GWAS. |
| Biobanks with EHR linkage | 5 (partial) | Zeng (own); Tsuo AoU-PGS; Krueger AoU PWAS; Long AoU CeD; Jiang AoU OUD. |
| EHR phenotyping & OMOP | 1 | Fujita AI-derived-feature causal certificates (bridges to representation). |
| Causal inference & pharmacoepi | 3 | Zhang hip PJI TTE; Momenzadeh ICU causal ML; Fujita AI-typed causal certificates. |
| Variant interpretation | 3 | Islam LDLR functional; Hull RS1 VCEP; Ma long-read RNA splicing outliers. |
| Genetic epidemiology | 1 | Tsuo AoU-PGS blockbuster. |
| CF / CFTR | 1 | Kim ETI work productivity. |
| APOL1 | 1 | van Hougenhouk-Tulleken SA-dialysis. |
| CHIP / somatic mosaicism | 3 | Chiu CV trial design; Zhao CKM syndrome CV mortality; Da Silva Faria AIHA. |
| EHR foundation models | 0 (this window) | The 09-01 cluster from prior report still dominates; nothing new added. |
| Knowledge representation in EHRs | 1 | Zeng (own); Fujita (bridges). |
| Drug repurposing | 0 HIGH | Two methods-watch items (DrugReason, ALS repurposing). |
| Rare disease | 5 | Carrasco-Zanini proteomics; Pitsava long-read WGS; Ma long-read RNA; Hwang UDN strategies; Ghasemnejad LLM-agent HPO severity. |
| ML for precision health | 1 | Momenzadeh ICU causal ML. |
| Multimorbidity / clustering | 0 | — |
| Knowledge graphs & ontologies | 0 HIGH | DrugReason methods-watch. |

---

## Suggested reading order (top 5, if time-boxed)

1. Zeng, Waxse, Denny (own paper — not for re-reading, but check citations
   have propagated correctly and add to your CV).
2. Tsuo et al. — Nature Genetics AoU-PGS.
3. Hysong et al. — AJHG sickle-cell PheWAS/LabWAS.
4. Fujita & Hattori — arXiv Information Set Emulation (causal
   certificates for AI-derived EHR features).
5. Ghasemnejad et al. — arXiv LLM agents for HPO-based genetic disease
   severity.
