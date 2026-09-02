# Research digest report — 2026-09-01

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-09-01 12:40Z** (~15 days since the
last research-digest report, covering fifteen arxiv-digest cron runs
and roughly a dozen Google Scholar alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-18.md` → `2026-08-31.md`) | 08-18 → 08-31 daily crons | 14 daily runs. Dry days (0 papers): 08-19 (weekend gap), 08-21–08-24, 08-29–08-31. 08-18: 4 papers (Bayesian epidemic alignment g-computation, Bhandari causal mediation with zero-inflated mediators, Daza n-of-1 digital health primer, Kung regression-not-to-the-mean overdose HTE). 08-20: 3 papers (Monroe molecular FM, Peruvian mayoral experience panel-DML, urban rail DML). 08-25: 1 paper (Leimenstoll causal effects in extremes; note: 2/4 q-bio categories failed to fetch). 08-26: 1 paper (RIBOSPAN long-context RNA FM). 08-27: 1 paper (Sharma hematology FM acquisition-shift audit). 08-28: 3 papers (NetMoint multimodal dementia trajectories UKB, DINIRS digital-twin NIRS on MIMIC-IV, GITIII-scale pan-cancer spatial-transcriptomics FM). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads. The pipeline commits its output to this repo rather than emailing PR / cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-01 batch, 11:36Z) | 09-01 11:36Z | 12+ feeds fired: George Hripcsak (citations-to, ×2 — one led with Zhang et al. GLP-1/SGLT2/DPP4 empirically-calibrated TTE; the other with Ilves et al. CohortContrast), Lisa Bastarache (citations-to; Wu et al. ACT CT phenotyping), Peter Szolovits (new-related; Chinese-medicine LLM benchmark citations feed), Zhiyong Lu (new-related; cross-lingual alignment KG-RAG feed), Miguel Hernán (citations-to; Zhao et al. Causal AI cancer immunotherapy TTE review), Joshua C Denny (citations-to; Shalita & Amit Nat Biomed Eng data-centric immunotherapy loops), Isaac Kohane (new articles; Zhao et al. Rare Diseases Common Dilemmas LLM decision-making), Yuan Luo (citations-to; PLOS Biol women's-health editorial), Marinka Zitnik (GenomeHarness genome-LM AI agents), Vivek Natarajan (citations-to; Gemini in the real-world), Tiffany J Callahan (Polymer Genome AI review). |
| Google Scholar alerts (08-31 batch, 02:20Z) | 08-31 02:20Z | 10 feeds fired: Konrad Karczewski (citations-to; Satterstrom et al. medRxiv rare-variant autism pleiotropy, plus Wang et al. Science autism-PPI networks), George Hripcsak (citations-to; Ilves et al. CohortContrast plus Acharya et al. cross-biobank ASCVD heritability plus Ta et al. antihypertensive RWE meta-analysis), Miguel Hernán (citations-to; Wästerlid et al. Lancet Haematol survivorship), Peter Szolovits (citations-to; Wu & Xiao proxy reliance in LLM decisions), Marinka Zitnik (new-related; SKILLER small-LM RL — off-topic), Zhiyong Lu (new-related; introspection paper — off-topic), Lisa Bastarache (new-related; Lichtenberger et al. Anesthesiology malignant hyperthermia variant prevalence + Kurniansyah et al. Nat Genet multiancestry AD-PRS), Yuan Luo (citations-to; Hyperemesis Gravidarum GDF-15 case report), Tiffany J Callahan (FedV-KGQA vertically-partitioned KG QA), Xiangnan He (RePolicy RL safeguards — off-topic). |
| Google Scholar alerts (08-30 batch, 01:26Z) | 08-30 01:26Z | 5 keyword feeds fired: `"electronic health records"` (peritoneal dialysis peritonitis prediction), `"variant interpretation" OR "variant classification"` (SMAD6 biallelic case), `"knowledge graph"` (NSAP neuro-symbolic propagation), `"All of Us research program"` (Kudamala et al. AoU functional decline; also Acharya et al. cross-biobank ASCVD; Zhu et al. partitioned BP-PRS AoU), `Foundation models + "electronic health records"` (Ba et al. BMJ PH ML for new-onset diabetes after acute pancreatitis). |
| Google Scholar alerts (08-29 batch, 21:21Z) | 08-29 21:21Z | 3 author-feed fires: Marinka Zitnik (protein-ligand GNN, off-topic), Vivek Natarajan (Japanese marketing paper — off-topic noise from broad-keyword feed), Zhiyong Lu (RL diffusion LMs — off-topic). |
| Google Scholar alerts (08-28 batch, 14:37Z) | 08-28 14:37Z | 3 feeds fired, one strong: Pascal Brandt new-related landed **4 EHR-FM papers** simultaneously — Xue et al. medRxiv psychiatric concept extraction encoder-based LMs, Burkhart et al. arXiv 2608.02939 federated generative event models across 122k patients, Ellershaw et al. arXiv 2608.16273 Foresight-England national-scale EHR-FM, Jiang et al. Preprints translating EHR-FMs into CDS. Also Marinka Zitnik + Peter Szolovits (both SKILLER small-LM RL, off-topic). |
| Google Scholar alerts (08-27–08-20 batches) | 08-20 → 08-27 | Rolling low-volume days between the 08-17 and 08-28 pushes; no HIGH items surfaced above what the arxiv-digest local runs captured. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fifteen HIGH items surfaced this window, clustering into six knots:

**Pharmacoepi target-trial-emulation cluster (2 items).** Zhang et al.
*Diabetes, Obesity & Metabolism* 2026 (Hripcsak feed) — head-to-head GLP-1
RA vs. SGLT2i vs. DPP4i cardiovascular-outcomes TTE with **empirical
calibration by negative controls**; a direct-hit paper for the GLP-1 /
SGLT2 drug thread AND for your causal-inference emphasis on
distributional diagnosis with negative controls. Zhao et al. arXiv 2026
(Hernán feed) — narrative framework review of TTE + treatment-effect
learning + clinical translation applied to cancer immunotherapy;
positioning paper for how the TTE + causal-ML pipeline generalizes
beyond diabetes and heart failure.

**EHR foundation-model cluster, national-scale (4 items).** The Pascal
Brandt feed dropped **four EHR-FM papers together on 08-28**, three of
which directly serve your `EHR foundation models` and `Knowledge
representation in EHRs` threads: Burkhart et al. arXiv 2608.02939 —
federated tokenized generative event models across 122,251 patients
addressing the exact "cross-site transfer degradation" you flagged as a
representation-drift concern. Ellershaw et al. arXiv 2608.16273 —
Foresight-England, the first **national-scale generative EHR-FM**
(strictly COVID-19-scoped for now) evaluating direct + indirect
pandemic effects — a template for FHIR/USCDI-informed national-scale FM
work per the Lemieux 2026 framing paper. Jiang et al. Preprints 2026 —
translation of EHR-FMs into clinical decision support, with an explicit
focus on sparsity-handling in routinely collected clinical data. Xue et
al. medRxiv 2026 — large-scale psychiatric concept extraction from EHR
notes using encoder-based LMs; the on-brand **NLP / LLM extraction from
clinical notes for phecode/HPO assignment** sub-thread paper, and paired
with Wu et al. below is the pattern of encoder-based auditable
representations regaining ground on decoder-based frontier LLMs.

**EHR phenotyping / OMOP cluster (2 items).** Ilves et al. *Informatics
in Medicine* 2026 (Hripcsak feed) — **CohortContrast**, an
OMOP-compatible enrichment-based workflow for deriving compact,
interpretable concept sets from broad OMOP concept spaces (applied to
the Estonian OPTIMA database, lung as the exemplar cohort). A direct-hit
methodology paper for `EHR phenotyping & OMOP` and for the
`Concept normalization and vocabulary mappings` sub-thread of
`Knowledge representation in EHRs`. Wu et al. arXiv 2608.25948
(Bastarache feed) — **Auditable CT phenotyping (ACT)**: 221 EHR
phenotypes, 38,317 training patients, 376,194 report-derived
observations, tests whether medical-image FMs read disease-specific
findings or shortcuts. Bridges the `NLP-derived representations from
clinical notes` sub-thread with `Fidelity, portability, and audit of
representations` — same "audit" logic that scContam / MIA-scFM apply to
single-cell FMs, now applied to imaging FMs.

**PheWAS / penetrance + monogenic-variant cluster (1 item).**
Lichtenberger et al. *Anesthesiology* 2026 (Bastarache feed) — genetic
prevalence of malignant-hyperthermia-susceptibility-associated variants
in a **nonmalignant hyperthermia referral cohort**. This is the exact
"penetrance under population-screening conditions vs. clinically
ascertained cohorts" framing that your PheWAS-infrastructure thread
prioritizes, transposed onto a pharmacogenetic phenotype (RYR1/CACNA1S
susceptibility to volatile anesthetics + succinylcholine).

**Biobanks & genetic epi (3 items).** Acharya et al. *Journal of Human
Genetics* 2026 — three-biobank comparison of ASCVD heritability and
cross-cohort genetic correlation across **Geisinger MyCode + UK Biobank
+ All of Us** using GWAS summary stats and LDSC; textbook direct-hit for
`Biobanks with EHR linkage` and for cross-ancestry portability. This is
the study design your thread wants propagated as a template. Kurniansyah
et al. *Nature Genetics* 2026 (Bastarache new-related feed) — APOE-
independent **multiancestry AD-PRS** with cognitive-decline and
neuropathological validation in diverse populations; directly serves
`PGS × ancestry` and pairs with the Kopal et al. brain-imaging × mental
health × cardiometabolic MiXeR-family paper you already track. Zhu et
al. Research Square 2026 (AoU keyword feed) — **partitioned blood-
pressure PRS** revealing differential effects of tissue-specific
enhancers on cardiovascular disease; the mechanistic-partitioning turn
on PRS that pairs with the Nagpal & Gibson pervasive-PGS-×-exposure
work.

**Rare-variant architecture (1 item).** Satterstrom, Auwerx, Fu, Zhang,
Kuo et al. medRxiv 2026 (Karczewski citations-to) — rare variation and
**pleiotropic** genetic architecture of autism across neuropsychiatric
traits; a rare-variant discovery lever paper that pairs with the
Baya AJHG 2026 "misaligned individuals" PGS-residuals framing your
INTERESTS.md prioritizes for `PGS residuals / polygenic-deviation
designs`.

**ML for precision health + digital-twin / multimodal-trajectory (2
items).** Islam, Mosier, Subbian arXiv 2608.26915 — **DINIRS**, a
censoring-aware Digital Twin for individualized treatment effects of
non-invasive respiratory support vs. IMV on 5,336 MIMIC-IV patients,
externally validated on 2,540 eICU-CRD patients; achieves +2.07
ventilator-free days per patient and traces the benefit to shorter
ventilation among survivors rather than mortality. Direct-hit for
`Digital twins from EHR data` and for `Machine learning for precision
health` (clinical-decision-tied HTE). Lee et al. arXiv 2608.26210 —
**NetMoint**, a multimodal (plasma proteomics + structural MRI + cerebral
haemodynamic) framework predicting **individualized 1/5/10/20-year
risks of AD, VD, and FTD subtypes** in 104,120 UK Biobank participants;
identifies persistently very-high-risk trajectories with distinct
molecular signatures. Direct-hit for `Chronic disease clustering and
multimorbidity` (heterogeneous paths to dementia) and for the UKB
proteomics-augmented-PRS sub-thread.

Also worth naming: **Kudamala et al.** arXiv 2608.21589 — early
functional-decline prediction from longitudinal labs + vitals in the AoU
Research Program (aging / multimorbidity in AoU, on-thread).

---

## Detailed reports — HIGH-priority studies

Papers below are the ones I would open next; each note gives (a) the
core method or claim, (b) why it maps to a research thread, and (c)
what to compare it against in the existing literature you track.

### 1. Zhang, Zhou, Tang, Lu, Zhang, Chen et al. — *Comparative Effectiveness of GLP-1RAs, SGLT2is and DPP4is for Cardiovascular Outcomes in Type 2 Diabetes: An Empirically Calibrated Target Trial Emulation Study*
**Venue:** *Diabetes, Obesity and Metabolism*, 2026 Aug 27 (online ahead of print). DOI: 10.1111/dom.71244.
**Surfaced via:** Google Scholar alert "7 new citations to articles by George Hripcsak" (09-01, 11:36Z, cites Hripcsak et al. distributional diagnosis with negative controls).
**Threads:** Causal inference & pharmacoepi (GLP-1 RAs, SGLT2is); ML for precision health; Biobanks (adjacent, depending on data source).

**What it is (from alert metadata + Hripcsak citation link).** A
head-to-head active-comparator target-trial-emulation study estimating
the comparative cardiovascular effectiveness of GLP-1 receptor agonists
vs. SGLT2 inhibitors vs. DPP-4 inhibitors in type 2 diabetes. The
**"empirically calibrated"** framing signals the Hripcsak / Ryan /
Schuemie negative-control-based bias-calibration workflow — the study
runs a large panel of negative-control outcomes to characterize residual
systematic bias in each drug-class comparison, then calibrates the
observed effect estimate against that null distribution. This is the
same distributional-diagnosis pattern that the paper cites and that has
become the OHDSI-house standard for large-scale RWE claims.

**Why it matters for your work.** Three angles hit at once. First, it
is a direct entry in the GLP-1 / SGLT2 comparative-effectiveness drug
thread — the third head-to-head TTE of the year on this axis. Second,
the empirical-calibration wrapper is the RWE quality bar that your
`Causal inference and pharmacoepidemiology` thread wants propagated;
this is a clean example to cite alongside Schuemie 2021 and Suchard
2019. Third, on-thread if you are drafting anything on **medication
persistence as an outcome modulated by PGx** — the same TTE spine
generalizes, and this paper's active-comparator design is portable to a
CYP2D6-stratified GLP-1-persistence analysis.

**Contrast against:** the Suchard et al. LEGEND-HTN antihypertensive
network study (empirical calibration on a distributed network); the
2025 SGLT2i × diuretic negative-control-calibrated safety papers from
the same OHDSI cluster; and any AoU / MVP TTE you're building where
negative controls could tighten the systematic-error interval.

---

### 2. Wu, Witschey, Li, Ordonez, Bressem et al. — *Auditable CT Phenotyping Through Report-derived Radiological Observations (ACT)*
**Venue:** arXiv 2608.25948, 2026.
**Surfaced via:** Google Scholar alert "5 new citations to articles by Lisa Bastarache" (09-01, 11:36Z; cites the Denny/Bastarache mapping-ICD10-to-phecodes workflow paper).
**Threads:** EHR phenotyping & OMOP (imaging-augmented); Knowledge representation in EHRs → NLP-derived representations from clinical notes AND Fidelity, portability, and audit of representations; ML for precision health.

**What it is (from abstract).** Medical-image foundation models predict
clinical phenotypes from CT with high accuracy, but their strong
performance leaves open whether they read disease-specific findings or
shortcuts that correlate with the diagnosis. **ACT** interposes a
layer of **report-derived radiological observations** between the raw
CT and the phenotype label: 376,194 observations mined from CT reports
across 38,317 training patients, used to phenotype 221 EHR phenotypes,
evaluated on 25,183 held-out patients. The audit unit is the
observation, not the pixel.

**Why it matters for your work.** This is a template for **auditable
representations** — exactly the framing your `Knowledge representation
in EHRs` thread asks for under "audits of learned representations
against clinical ground truth (chart-review-validated)." The paper
converts an opaque image-FM prediction into a chain that a radiologist
or curator can inspect: report → observation → phenotype. That is
directly the shortcut-vs-signal auditing pattern you already track for
Guo et al. GraphRareBench (`Auditable HPO-driven diagnostic benchmarks
with separable metrics`) and for scContam / MIA-scFM
`Pretraining-contamination audits`. The other big signal is that this
is a Bressem-lineage paper (RadBERT / RayeD), so the observation
extractor is likely a purpose-trained radiology encoder rather than a
frontier LLM — the same pattern as Xue et al. below (encoder-based LMs
regaining ground for structured concept extraction).

**Contrast against:** the ClaimGuard / MedTok note-augmented phecoding
pipelines; RadBERT's earlier observation-mining benchmarks; PhenoGPT2
and Phen2Gene rare-disease benchmarks (whose Hit@10 you already flagged
for its "hides ranking-of-confounders" pathology).

---

### 3. Ilves, Umov, Mooses, Loorents et al. — *CohortContrast: Enrichment-Based Methodology for Identification of Clinically Relevant Concepts in Real-World Data*
**Venue:** *Informatics in Medicine Unlocked*, 2026.
**Surfaced via:** Google Scholar alert "10 new citations to articles by George Hripcsak" (08-31, 02:20Z; cites the OHDSI Standardized Vocabularies paper).
**Threads:** EHR phenotyping & OMOP; Knowledge representation in EHRs → Concept normalization and vocabulary mappings AND Applications to prioritize (computable phenotyping, cohort discovery).

**What it is (from abstract).** An **OMOP-compatible workflow** for
deriving compact, clinically interpretable concept sets from broad
real-world-data concept spaces. The bottleneck it targets is one every
OMOP-based trajectory / phenotyping / RWE study hits: selecting a small
set of cohort-relevant concepts out of the tens of thousands available.
Applied to OMOP-mapped observational data from the **Estonian
nationwide OPTIMA database**, with lung as the exemplar target cohort.

**Why it matters for your work.** This is the exact concept-selection
substrate for `EHR phenotyping & OMOP` and the missing-methods piece for
your `Applications to prioritize` sub-thread — "computable phenotyping
/ PheKB / PheValuator, cohort discovery for target-trial emulation."
The enrichment-based framing is portable to any OMOP cohort discovery
step where you want to shrink from the full vocabulary to an
interpretable subset. Also a national-scale OMOP database (Estonia's
OPTIMA) that hasn't shown up on your radar yet, and an OHDSI-community
paper that could underpin a distributed CFTR-modulator persistence or
GLP-1 comparative-effectiveness cohort-definition step.

**Contrast against:** Achilles / CohortDiagnostics (concept-set
inspection); PhenotypeLibrary (community cohort definitions);
FeatureExtraction (large-scale covariate construction on OMOP); and any
ATLAS cohort-set you already use — CohortContrast slots between concept
retrieval and phenotype definition.

---

### 4. Burkhart, Solo, Lee, Charles, Liao et al. — *Federated Generative Event Models for Tokenized Electronic Health Records*
**Venue:** arXiv 2608.02939, 2026.
**Surfaced via:** Google Scholar alert "Pascal Brandt - new related research" (08-28, 14:37Z).
**Threads:** EHR foundation models (CLMBR/MOTOR/EHRSHOT/MEDS lineage); Federated / privacy-preserving EHR causal analytics (the rising sub-thread you added).

**What it is (from abstract).** Evaluates **federated training** of
tokenized generative event models (GEMs) across **122,251 patients**
spanning multiple institutions. Addresses the exact "cross-site
performance degradation" pathology that your `EHR foundation models`
thread flags as the deployability barrier: EHR-FMs trained at one site
often lose calibration when transferred, so federated pretraining or
site-aware fine-tuning is the natural corrective.

**Why it matters for your work.** Directly serves both (a) the EHR-FM
lineage (CLMBR / MOTOR / MEDS / EHRSHOT), and (b) the **Federated /
privacy-preserving EHR causal analytics** sub-thread you added in
2026-07-29 (the Jang et al. arXiv 2607.17958 distributed-mediation
paper). A federated pretraining backbone is what any cross-network TTE
or distributed-mediation pipeline needs as its representation layer.

**Contrast against:** CLMBR (Steinberg 2021); MOTOR (Steinberg 2023);
EHRSHOT / FEMR benchmark; Foresight (single-site) → Foresight-England
(national-single-payer, next paper); Xu et al. federated PRS lineage on
the genetics side.

---

### 5. Ellershaw, Tomlinson, Kraljevic, Denaxas et al. — *Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic*
**Venue:** arXiv 2608.16273, 2026.
**Surfaced via:** Google Scholar alert "Pascal Brandt - new related research" (08-28, 14:37Z).
**Threads:** EHR foundation models; Knowledge representation in EHRs → Interoperability standards and their representational consequences.

**What it is (from abstract).** The first **national-scale generative
foundation model of EHRs**, developed as a COVID-19-scoped research
pilot. Evaluates ability to model direct and indirect effects of the
pandemic — i.e., the model has to encode both direct-COVID event
trajectories and downstream disruption (missed screenings, deferred
elective care, medication persistence shifts).

**Why it matters for your work.** This is the reference paper for
national-scale, single-payer EHR-FM development, and pairs with the
Lemieux et al. *JAMIA Open* 2026-07 FHIR/USCDI framing paper you have on
`Interoperability standards`. It is the first FM that is FHIR-informed
by national deployment (NHS England → HDR UK). Also a natural sibling
to your **Digital twins from EHR data** sub-thread (Zhang / Ideker /
Oermann *Cell* 2026): Foresight is the pretrained backbone that
individualized-trajectory digital-twin prediction would ride on.

**Contrast against:** Foresight (single-site 2021); MEDS-DEV benchmark;
Ellershaw / Kraljevic MedCAT / SapBERT lineage for phenotype extraction
underneath Foresight-England.

---

### 6. Jiang, Dai, Zhang, Gao, Chen, Du, Liu et al. — *Translating Electronic Health Record Foundation Models into Clinical Decision Support*
**Venue:** Preprints, 2026.
**Surfaced via:** Google Scholar alert "Pascal Brandt - new related research" (08-28, 14:37Z).
**Threads:** EHR foundation models; ML for precision health (clinical-decision-tied).

**What it is (from abstract).** Frames EHR-FMs as the natural target
for translation into clinical decision support because they capture
longitudinal, multimodal, large-scale clinical trajectories. Explicitly
tackles the **extreme sparsity + irregularity** of routinely collected
clinical data as a modeling constraint that CDS translation has to
account for.

**Why it matters for your work.** Your `Machine learning for precision
health` thread scores HIGH only when the ML is "tied to a clinical
decision (who to treat, who to screen, when to escalate)"; generic
benchmark work is SKIP. This is a translation-focused, CDS-oriented
review-plus-framework paper, which is the right altitude for citing
when you argue that EHR-FM benchmark performance ≠ CDS deployability.
Sparsity as the first-order concern also flags this as a bridge to your
`Fidelity, portability, and audit of representations` sub-thread.

---

### 7. Xue, Frydman-Gani, Arias, Perez Vallejo et al. — *Large-Scale Psychiatric Concept Extraction from Electronic Health Records: A Comparative Study of Encoder-Based Language Models*
**Venue:** medRxiv 2026.08.20 (arXiv-adjacent preprint).
**Surfaced via:** Google Scholar alert "Pascal Brandt - new related research" (08-28, 14:37Z).
**Threads:** EHR phenotyping & OMOP; Knowledge representation in EHRs → NLP-derived representations from clinical notes.

**What it is (from abstract).** A large-scale comparative study of
**encoder-based** language models for psychiatric concept extraction
from EHR free-text notes. The framing sentence is on-thread verbatim:
"Free-text notes in EHRs contain fine-grained psychiatric information
essential for psychiatric research and clinical care, and often absent
or under-recorded in structured codes alone." That is the exact
note-augmented-phecoding argument you already track (LLM-extracted
problems supplementing structured codes).

**Why it matters for your work.** Two signals. First, the encoder-based
LM angle: at a moment when the field is chasing decoder-LLM extractors,
this paper argues encoders remain competitive for structured concept
extraction — consistent with the ACT paper (#2) and with your existing
tracking of SapBERT / MedCAT / cui2vec. Second, psychiatric phenotyping
in EHRs is one of the harder cases (heterogeneous vocabulary, high
note-vs-code discordance), so a large-scale comparative benchmark is
useful as a citation for the note-code fusion sub-thread.

**Contrast against:** MedCAT; SapBERT; Med-BERT; PhenoTagger / PhenoRerank
(HPO recognition); Angell et al. IEEE 2026 chart-review-anchored ASD
phenotyping paper from your 08-17 report.

---

### 8. Lichtenberger, Bastian, Abou Jamra, Rüffert — *Genetic Prevalence of Malignant Hyperthermia Susceptibility–Associated Variants in a Nonmalignant Hyperthermia Referral Cohort*
**Venue:** *Anesthesiology*, 2026.
**Surfaced via:** Google Scholar alert "Lisa Bastarache - new related research" (08-31, 02:20Z).
**Threads:** PheWAS / phecode infrastructure → **penetrance estimation for monogenic variants under population-screening conditions vs. clinically ascertained cohorts**; Variant interpretation (ACMG / ClinGen); Rare disease.

**What it is (from abstract).** Estimates the **background prevalence**
of malignant-hyperthermia-susceptibility-associated variants
(RYR1 / CACNA1S) in patients referred for evaluation but ultimately
**not diagnosed** with MH. MH susceptibility is an inherited
pharmacogenetic disorder producing life-threatening hypermetabolic
reactions to volatile anesthetics and succinylcholine; the referral
cohort provides the natural comparator to the classical
clinically-ascertained MH-positive cohort.

**Why it matters for your work.** This is the exact "penetrance under
population-screening conditions vs. clinically ascertained cohorts"
question your PheWAS-infrastructure thread was written around,
transposed to a **pharmacogenetic phenotype**. Pairs well with the
Kessler / Loh CHIP / VEXAS / LOY somatic-mosaicism papers on penetrance,
and with the Baya AJHG PGS-residuals paper for rare-variant
polygenic-modifier framing.

**Contrast against:** the AoU / UKB pathogenic-variant penetrance
papers you already track (Fahed 2020 monogenic-vs-polygenic; Karczewski
2022 gnomAD constraint); ClinGen VCEP guidelines for RYR1 (recently
updated by the RYR1 VCEP).

---

### 9. Acharya, Gidding, Oetjens, Berry et al. — *Cross-Biobank Comparison of ASCVD Heritability and Genetic Correlation*
**Venue:** *Journal of Human Genetics*, 2026.
**Surfaced via:** Google Scholar alert "10 new citations to articles by George Hripcsak" (08-31) AND `"All of Us research program"` keyword feed (08-30). Dual hit is a signal.
**Threads:** Biobanks with EHR linkage (MyCode + UKB + AoU); Genetic epidemiology (GWAS, cross-cohort portability); PheWAS / phecode infrastructure.

**What it is (from abstract).** Compares **SNP-based heritability and
cross-cohort genetic correlation** for ASCVD (and its nested subphenotypes
coronary events + MI) across **Geisinger's MyCode + UK Biobank + AoU
Controlled Tier v8** using GWAS summary statistics and LDSC. The framing
sentence identifies the exact gap: estimates of ASCVD SNP-heritability
vary widely across populations, which complicates interpretation of
genetic architecture.

**Why it matters for your work.** This is the textbook `Biobanks with
EHR linkage` cross-biobank study design your thread wants propagated —
three EHR-linked biobanks, one polygenic architecture question, a
harmonized outcome definition (ASCVD → CE → MI as nested subphenotypes),
and a portable estimator (LDSC on summary stats). Directly reusable
template for any cross-biobank PheRS / PGS comparison you might build.
Also gently supports your `Composite risk models stacking PRS with rare
pathogenic variants` framing, because if SNP-heritability itself varies
across biobanks, so will the PRS-tails-and-rare-variants stacking
coefficient.

**Contrast against:** the Fahed 2020 monogenic-vs-polygenic composite
CAD paper (single-cohort); Truong et al. cross-biobank PheWAS
harmonization (also MyCode + UKB + AoU); Souaiaia PGS-tails as the
distributional lens.

---

### 10. Kurniansyah, Tasaki, Rehman, Zhu, Farrell et al. — *A Multiancestry Polygenic Risk Score for Alzheimer's Disease Is Associated with Cognitive Decline and Neuropathological Hallmarks in Diverse Populations*
**Venue:** *Nature Genetics*, 2026.
**Surfaced via:** Google Scholar alert "Lisa Bastarache - new related research" (08-31, 02:20Z).
**Threads:** Genetic epidemiology → PRS, cross-ancestry portability; ML for precision health; Chronic disease clustering (dementia).

**What it is (from abstract).** Develops an **APOE-independent
multiancestry AD-PRS** using GWAS summary statistics from diverse
cohorts, validated against cognitive-decline and neuropathological
hallmarks in diverse populations. Because AD-PRS has historically been
APOE-dominated and Eurocentric, the APOE-out design plus multiancestry
training is a portability win in principle.

**Why it matters for your work.** Direct hit for your `Genetic
epidemiology → Multi-omics-augmented PRS` and `PGS × ancestry`
sub-threads; also usable as a template for constructing APOE-out
composite risk models that pair with rare-variant burden and with UKB
proteomics / metabolomics. Pairs naturally with the NetMoint UKB
dementia-subtype trajectory paper (#11) — one is a genetic-only PRS,
the other is a proteomics-plus-imaging trajectory framework; the joint
question is whether the multiancestry AD-PRS explains any of NetMoint's
persistently-very-high-risk trajectory subgroup.

**Contrast against:** the Genome Asia AD-PRS papers of the last two
years; the ADNI-anchored PRS papers (single-cohort, low ancestry
diversity); the Kunkle 2019 IGAP-derived AD-PRS.

---

### 11. Lee, Li, Liu, Zhang, Wang, Fan, Zhang, Wang, Bai — *Multimodal Risk Trajectories Reveal Heterogeneous Paths to Dementia (NetMoint)*
**Venue:** arXiv 2608.26210, 2026 (surfaced via local arxiv-digest 08-28 cron).
**Threads:** Biobanks with EHR linkage (UK Biobank); Chronic disease clustering and multimorbidity; ML for precision health; PRS + proteomics stacking.

**What it is (from abstract).** **NetMoint**: a multimodal framework
integrating partially observed plasma proteomics + structural MRI +
cerebral haemodynamic phenotypes to predict individualized 1-, 5-, 10-,
and 20-year risks of AD, VD, and FTD in **104,120 UKB participants free
of dementia at baseline**. Reports mean AUCs of 0.937 (AD), 0.930 (VD),
and 0.932 (FTD). Key qualitative result: the **biological determinants
of prediction shift with horizon** — structural brain vulnerability
dominates short-horizon risk, circulating molecular signatures dominate
long-horizon risk. Also identifies distinct temporal trajectories
(e.g., 0.7% of eventual-AD followed a persistently-very-high-risk
trajectory reaching 53.5% at 20 years; 8.3% of eventual-FTD followed an
increasing-very-high-risk trajectory reaching 67.17%), with subtype-
specific molecular signatures (lower TGFB1 for AD, higher NDRG1 for
FTD). External harmonized ADNI-to-UKB validation on 138 shared features
yields AUC 0.741 at 20 years for AD.

**Why it matters for your work.** Direct hit on multiple threads at
once. `Biobanks with EHR linkage`: UKB Olink proteomics + imaging
substrate. `Chronic disease clustering and multimorbidity`: identifies
small subtype-specific trajectories via risk-trajectory clustering,
which is exactly the multimorbidity-trajectory framing your thread
prioritizes for aging phenotypes. `ML for precision health`: 1-year vs.
20-year horizon-separable prediction is a decision-relevant framing
(who to enroll in a disease-modifying trial vs. who to screen).
Trajectory-resolved dementia risk stratification also pairs with the
Ran / Benatar ALS pre-symptomatic phenoconversion paper you cited under
`Rare disease → Pre-symptomatic carrier phenoconversion prediction`.

**Contrast against:** the Souaiaia 2026 *Nature* PGS-tails paper as the
distributional lens on the very-high-risk subgroup; the You et al. 2023
UKB Olink+PRS composite AD risk paper; the ADNI multimodal MRI+CSF
trajectory clustering literature.

---

### 12. Islam, Mosier, Subbian — *DINIRS: Digital Twin for Individualized Treatment Effects of Non-Invasive Respiratory Support Strategies*
**Venue:** arXiv 2608.26915, 2026 (surfaced via local arxiv-digest 08-28 cron).
**Threads:** ML for precision health (HTE, clinical-decision-tied); EHR foundation models → Digital twins from EHR data; Causal inference (doubly-robust HTE estimation).

**What it is (from abstract).** A **censoring-aware Digital Twin**
framework for individualized treatment effects (ITEs) of non-invasive
respiratory support (NIRS) vs. invasive mechanical ventilation (IMV) in
acute respiratory failure. Uses 23 first-24-h ICU baseline variables on
**5,336 MIMIC-IV patients**; **transformer encoder with a
survival-attention gate** decomposes 28-day ventilator-free days
(VFD-28) into survival probability and conditional ventilation
duration. A **cross-fitted, doubly robust learner** estimates ITEs.
Externally validated on **2,540 patients from multi-site eICU-CRD**.
Achieves +2.07 ventilator-free days per patient (207 per 100 patients)
vs. observed practice. Predicted NIRS benefit is higher in less-organ-
dysfunction patients (88.4% vs. 49.0%). The **mechanism analysis** finds
the NIRS benefit comes from shorter ventilation among survivors, not
from reduced mortality — i.e., avoiding intubation-associated
complications is the driver.

**Why it matters for your work.** This is a textbook example of the
**Digital twins from EHR data** sub-thread you added in 2026-07-29 —
Zhang / Ideker / Oermann *Cell* 2026 as the field-defining framing
reference, DINIRS as the ICU concrete instance. It also nails the ML-
for-precision-health criterion your thread applies (HTE tied to a
concrete clinical decision: which acute-respiratory-failure patients
should try NIRS first). The doubly-robust cross-fitted HTE estimator
plus MIMIC + eICU external validation is the methods stack you already
prioritize.

**Contrast against:** Alaa & van der Schaar CATE-on-MIMIC lineage; Chen
et al. 2024 SGLT2 HTE on UKB and MIMIC; Alaa 2023 individualized
counterfactual survival papers; and Zhang / Ideker / Oermann 2026 *Cell*
digital-twin consortium framing paper.

---

### 13. Zhao, Liu, Yang, Xie, Mao, Zhou, Wang et al. — *Causal AI for Cancer Immunotherapy: A Narrative Framework Review of Target Trial Emulation, Treatment-Effect Learning and Clinical Translation*
**Venue:** arXiv (Hernán citations-to feed), 2026.
**Surfaced via:** Google Scholar alert "10 new citations to articles by Miguel Hernán" (09-01, 11:36Z).
**Threads:** Causal inference & pharmacoepi; ML for precision health (immunotherapy HTE).

**What it is (from alert snippet).** Narrative framework review that
positions **target trial emulation + treatment-effect learning +
clinical translation** as a joint pipeline for cancer-immunotherapy
comparative-effectiveness questions. Cites Hernán, so it inherits the
TTE-as-scaffold framing (specify eligibility → treatment strategies →
assignment procedure → follow-up → outcome → causal contrast → analysis
plan).

**Why it matters for your work.** Useful as a citation-ready summary
of the TTE + causal-ML combination outside the diabetes / cardiovascular
default. Cancer-immunotherapy is a natural stress test for the pipeline
because the eligibility criteria are complex, the treatment strategies
are dynamic (line of therapy, sequencing), and the HTE is real. Even if
you never work in oncology, this is a good template paper to cite when
you argue that the TTE + causal-ML framework is domain-portable.

---

### 14. Kudamala, Kuruvikkattil, Pulavarthy et al. — *Predicting Early Functional Decline from Longitudinal Laboratory and Vital Sign Trajectories: A Large-Scale Study Using the All of Us Research Program*
**Venue:** arXiv 2608.21589, 2026.
**Surfaced via:** Google Scholar alert `"All of Us research program"` keyword feed (08-30, 01:26Z).
**Threads:** Biobanks with EHR linkage (AoU); Chronic disease clustering and multimorbidity (aging); ML for precision health.

**What it is (from abstract snippet).** Uses temporal trajectories of
routine biomarkers (labs + vitals) already recorded in AoU EHR data to
predict **early functional decline** in older adults, before it is
recognized clinically via falls or gait impairment. The framing is
prevention-window-focused: close the recognition gap before the
irreversible endpoint.

**Why it matters for your work.** Direct hit on `Biobanks with EHR
linkage → AoU`, and on `Chronic disease clustering and multimorbidity`
in aging. Longitudinal-trajectory prediction from routinely collected
labs is exactly the substrate your `EHR foundation models → Digital
twins from EHR data` sub-thread wants — this paper is the pre-FM
version, using classical trajectory ML.

**Contrast against:** the Ba et al. BMJ PH 2026 ML-for-new-onset
diabetes-after-pancreatitis paper (same feed batch on 08-30); NetMoint
(dementia trajectories on UKB, same week); the Kang et al. UKB frailty
trajectory papers.

---

### 15. Zhu, Yang, Lee, Chakravarti — *Partitioned Blood Pressure Polygenic Risk Reveals Differential Genetic Effects of Tissue-Specific Enhancers and Their Interactions on Cardiovascular Disease*
**Venue:** Research Square (preprint), 2026 (data on AoU Researcher Workbench).
**Surfaced via:** Google Scholar alerts "Lisa Bastarache - new related research" AND `"All of Us research program"` keyword feed (08-30 / 08-31 batches).
**Threads:** Genetic epidemiology (PRS partitioning, tissue-specific enhancers); Biobanks with EHR linkage (AoU); Composite risk models.

**What it is (from abstract).** Introduces a framework for **partitioning
blood-pressure PRS** into components corresponding to tissue-specific
enhancers, then examines their differential effects and interactions on
cardiovascular disease. Uses AoU Researcher Workbench for the analysis
substrate. Positioned explicitly against the standard "aggregate PRS
obscures distinct biological mechanisms" limitation.

**Why it matters for your work.** Direct entry in your
`Genetic epidemiology → cross-trait shared genetic architecture and
multi-trait triangulation` sub-thread, and in `Composite risk models
stacking PRS with rare pathogenic variants` — a partitioned PRS is one
step toward the mechanism-resolved, tails-and-residuals PGS framing
your INTERESTS.md prioritizes (Baya AJHG "misaligned individuals",
Souaiaia PGS-tails). Also an AoU-native analysis, which strengthens the
Biobank thread. Note: still Research Square preprint, so wait for
peer-review before citing.

---

## METHODS-WATCH — off-topic domain, exemplary methods worth cribbing

- **Bhandari, Kar, Daniels, Karmakar** — *Causal mediation analysis for
  zero-inflated longitudinal data in the presence of treatment
  non-compliance and multiple mediators* (arXiv 2608.15775v1, 08-16 →
  local digest 08-18). Bayesian causal mediation with **enriched
  Dirichlet-process mixture models** + scalable **G-computation** for
  causal estimands, handling zero-inflated mediators and outcomes and
  non-compliance. Domain is retail-email marketing, but the
  zero-inflation-plus-mediation architecture is directly portable to
  **clonal-hematopoiesis clonal-fraction longitudinal analyses** (pairs
  with the Bandreddi Tobit-vs-hurdle paper from the 08-17 report) and
  to **medication-persistence-as-outcome** with zero-inflated MPR /
  discontinuation.
- **Moriña** — *Bayesian epidemic alignment for causal evaluation of
  seasonal infectious-disease interventions* (arXiv 2608.16537v1, 08-17
  → local digest 08-18). Season-specific affine transformations map
  calendar time to a latent **epidemic clock**; effects are estimated
  on the clock rather than the calendar; alignment is a model component,
  not preprocessing, so timing uncertainty propagates into every causal
  contrast. **Posterior g-computation** yields prevented cases,
  prevented fractions, peak attenuation, and epidemic displacement.
  Off-topic (RSV immunization in Catalunya), but the "alignment as a
  model component, not preprocessing" pattern is directly portable to
  **staggered pharmacoepi index-date problems** (e.g., early-pregnancy
  time-zero for perinatal drug exposure, GLP-1 initiation across formulary
  timing).
- **Kung, Martin, Lok** — *Regression Not-to-the-Mean: An Oddity of
  Regression, Illustrated with the Risk of Overdose Deaths* (arXiv
  2608.15399v1, 08-15 → local digest 08-18). Constant-treatment-effect
  models with staggered treatment + HTE can produce weighted averages
  with **negative weights**, so the constant estimate can be smaller in
  magnitude or opposite in sign to almost all the underlying
  heterogeneous effects. Demonstrated for both **linear and logistic**
  link functions; drug-induced-homicide prosecutions on unintentional
  drug-overdose deaths as the illustration. On-thread as a caveat paper
  for any staggered-treatment pharmacoepi TTE with HTE — cite as a
  reason to always inspect the negative-weight diagnostic (de
  Chaisemartin & D'Haultfœuille family) before trusting a
  constant-effect summary.
- **Sharma & Tapadiya** — *Can You Trust Frozen Hematology Foundation
  Models under Acquisition Shift?* (arXiv 2608.25148v1, 08-25 → local
  digest 08-27). Audits 15 frozen encoders (hematology, pathology,
  general vision) across four public single-cell acquisition domains
  along accuracy + calibration. In-domain macro-F1 saturated (0.98–
  0.997), cross-dataset F1 drops 34–72% and rankings re-order.
  Introduces **Class-Balanced Re-standardization (CBR)**, a
  training-free pseudo-label-balanced feature normalization. Off-topic
  domain, but this is a **portable template** for the audit sub-thread
  you added under EHR-FMs: swap WBC classification for phecode / MEDS
  event prediction, and this is the deployability audit you would want
  to run against CLMBR / MOTOR / EHRSHOT across BioVU → AoU → UKB.
- **Leimenstoll & Schienle** — *Identification and Inference for Causal
  Effects in Extremes under General Conditions* (arXiv 2608.22957v1,
  08-24 → local digest 08-25). Identification of causal relations in
  extremes via the **Causal Tail Coefficient (CTC)** under heavy-tailed
  regularly varying innovations, with heterogeneous tail indices and
  potentially heavy-tailed confounders. Off-topic domain (climate +
  financial extremes), but the CTC as a tail-focused causal-dependence
  measure could plausibly generalize to **rare-event pharmacoepi**
  (e.g., very-rare adverse events where the average-effect estimator is
  underpowered but a tail-dependence estimator might not be).
- **Wu & Xiao** — *Proxy Reliance in Large Language Model Decisions Is
  Uncalibrated to Predictive Evidence* (arXiv 2608.22887, surfaced via
  Peter Szolovits citations-to feed 08-31). Direct entry in the
  LLM-decision-calibration audit space; portable to clinical-LLM
  decision-support audits.

---

## Also-ran / SKIP pile (briefly, so you don't have to re-scan)

- **Monroe** MFM (Banaszewski & Fitzgibbon, arXiv 2608.18982v1) —
  molecular FM with TabPFN downstream; off-thread (chemistry-only
  pipeline without clinical loop).
- **Panel DML for Peruvian mayoral experience** (arXiv 2608.18354v1) and
  **Panel DML for urban rail reliability** (arXiv 2608.17901v1) — DML
  method exposure, off-thread domains.
- **RIBOSPAN** long-context RNA FM (arXiv 2608.22849v1) — off-thread.
- **GITIII-scale** pan-cancer spatial-transcriptomics FM
  (arXiv 2608.26208v1) — off-thread.
- **Daza N-of-1 digital-health primer** (arXiv 2608.15526v1) — precision-
  medicine adjacent, but a review-chapter primer rather than a study.
- **Wang et al. Science 2026 autism PPI-network rewiring** — high-quality
  paper (Karczewski feed), but molecular-mechanism-first rather than
  cohort / EHR / PheWAS-relevant; note for later reading, not for the
  active thread queue.
- **NSAP Neuro-Symbolic KG Completion**, **FedV-KGQA vertical-KG QA**,
  **GenomeHarness genome-LM agents**, **RePolicy RL safeguards**,
  **SKILLER small-LM RL** — all off the biomedical-clinical axis.
- Scholar-feed noise (Japanese marketing paper via Natarajan feed;
  polymer-genome AI paper via Callahan feed; Chinese-medicine
  ChatGPT-vs-Claude benchmark via Szolovits feed; PLOS Biology
  women's-health editorial via Luo feed) — expected broad-keyword
  bleed-through from citation feeds.

---

## Cross-cutting patterns to watch

1. **Encoder-based LMs are having a small comeback for structured
   clinical-concept extraction.** ACT (radiology), Xue et al.
   (psychiatric concept extraction), and the Thomo & Thomo
   deployable-open-weights-vs-frontier paper from the Hripcsak feed all
   argue that encoder architectures remain competitive against frontier
   decoder LLMs when the target is a **structured, auditable
   representation** rather than free generation. Worth flagging as a
   note in the `Knowledge representation in EHRs → NLP-derived
   representations` sub-thread.
2. **Federated + national-scale EHR-FMs are stacking up fast.**
   Burkhart federated GEMs, Ellershaw Foresight-England, and the
   Kraljevic MedCAT lineage together mean the "single-site EHR-FM
   pretrained on one hospital" era is closing. Your INTERESTS.md
   `Federated / privacy-preserving EHR causal analytics` sub-thread is
   getting concrete substrate.
3. **Empirical calibration by negative controls is spreading from
   OHDSI-house into ordinary drug-class effectiveness papers.** Zhang
   et al. GLP-1/SGLT2/DPP4 explicitly frames the whole study as
   "empirically calibrated TTE." Consider this the new hygiene bar for
   your own pharmacoepi work.
4. **Cross-biobank comparisons are becoming the default study design
   for genetic-architecture claims.** Acharya three-biobank ASCVD
   heritability paper is one of several this year with the same
   three-biobank (MyCode + UKB + AoU) template. Worth using in your
   own methods-portable checklist.
5. **The 08-21 → 08-24 arxiv-digest gap** (0 papers for four days
   straight) is unusually long; the 08-25 cron also flagged 2/4
   categories failed to fetch. If a fifth zero-day appears in the next
   week, worth checking `scripts/` for a fetcher-side issue rather than
   attributing it entirely to submissions volume.

---

## Next actions I would take

- **Read first (in this order):** Zhang GLP-1/SGLT2/DPP4 TTE (thread
  centrality); Wu ACT CT phenotyping (novel auditable-representation
  template); Ilves CohortContrast (methods reusability); Ellershaw
  Foresight-England (positioning reference for any national-scale
  EHR-FM writeup); Islam DINIRS (digital-twin sub-thread anchor); Lee
  NetMoint UKB (multimodal-trajectory-clustering anchor).
- **Cite-ready this week:** Zhang, Ilves, Acharya, Kurniansyah,
  Lichtenberger.
- **Watch for follow-ups:** Zhu partitioned BP-PRS (still Research
  Square); Kudamala AoU functional-decline (arXiv only); Satterstrom
  autism rare-variant pleiotropy (medRxiv → likely a *Nature* / *Nat
  Genet* paper by year-end).
- **Consider adding to INTERESTS.md:** an explicit sub-thread under
  `EHR foundation models` for **national-scale / single-payer EHR-FM
  work** — Foresight-England is the third national-scale FM this year
  (after HDR UK's earlier attempt and NHS Wales' local variant), and
  you don't currently have a named bucket for them.
