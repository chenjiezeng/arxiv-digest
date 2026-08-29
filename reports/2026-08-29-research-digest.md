# Research digest — 2026-08-29

Scheduled routine run at 2026-08-29 12:36 UTC. Sources:

- Gmail research alerts (Google Scholar keyword / author / citation alerts,
  My-NCBI PubMed alerts) — last 14 days.
- `arxiv-digest` markdown output in `digests/` for the last week
  (2026-08-25 through 2026-08-28).

Triage against `INTERESTS.md` (last updated 2026-07-29). Buckets are
**HIGH** (directly serves an active thread), **METHODS-WATCH** (off-topic
disease but exemplary methods), and **SKIP** (recorded here in aggregate,
not detailed).

Only papers that received a **HIGH** or a strong **METHODS-WATCH** verdict
get a detailed section below. Weak matches are collapsed at the bottom.

## Executive summary

- **Variant interpretation & penetrance.** Two convergent moves this week:
  P-KNN's joint calibration of multiple pathogenicity predictors (Lin &
  Brandes, *Genetics in Medicine*) turns the "which score do I trust"
  question into one calibrated posterior; and Hanson et al.'s UK RET
  incidental-finding guidance (*Endocrine-Related Cancer*) cites the
  Guidance-for-estimating-penetrance framework and applies it to
  incidentally discovered germline RET carriers — direct penetrance-under-
  screening territory. ENIGMA's BRCA1 exon-18 RNA splicing paper (*AJHG*)
  adds a template for how splicing evidence resolves VUS.
- **Somatic mosaicism / CHIP + LOY.** Sun et al. (*npj Aging*) report
  **independent** and additive associations of CHIP and mLOY with
  all-cause and cause-specific mortality in men — the cleanest
  disentanglement to date, directly on the CHIP + LOY thread in
  `INTERESTS.md`. Two supporting reviews (Caiado *Seminars in
  Immunology*; Ogawa *Immunological Medicine*) round out the mechanism +
  neuro/immune-disease context.
- **EHR foundation models & multimodal patient timelines.** PULSE (Wu et
  al., *Nature Computational Science*) — a longitudinal multimodal
  imputation framework — is exactly the "reconstruct the unmeasured
  molecular profile from a patient's own history" claim that maps onto
  the digital-twin-from-EHR sub-thread. Companion "News & Views" also in
  the alert.
- **Real-world causal inference on OMOP-CDM.** Min et al.
  (*Pharmaceuticals*) run a multi-center OMOP-CDM comparative-safety
  study of antidepressants (1999–2026) — direct pharmacoepi template,
  cites the aortic-aneurysm follow-up-drug study.
- **PGS in the tails / IBD-specific PRS-outcome mapping.** Yuan et al.
  (*Scientific Reports*, UK Biobank n = 5,021 IBD) push PRS beyond
  incidence to *within-disease* outcomes — intestinal surgery, GI
  cancer, all-cause mortality. Complements the composite-risk-and-tails
  framing in the interests file.
- **KG-augmented LLM diagnosis.** Kespechara & Mingkhwan's
  multi-source-KG-RAG framework for LLM diagnosis (AI in Healthcare
  2026) is a direct fit for the KG + rare-disease-diagnosis threads and
  should be read alongside GraphRareBench.

Full detailed reports below, grouped by research thread.

---

## Variant interpretation, penetrance, and monogenic disease

### 1. P-KNN: joint calibration of multiple pathogenicity prediction tools streamlines variant classification

- **Authors:** PY Lin, N Brandes
- **Venue:** *Genetics in Medicine*, 2026
- **Source:** Gmail — Scholar alert `"variant interpretation" OR "variant classification" OR "Causal Variant" - new results` (2026-08-29)
- **URL:** https://www.gimjournal.org/article/S1098-3600(26)01010-5/pdf
- **Bucket:** **HIGH** — Variant interpretation (ACMG/AMP) thread.

**What it does.** Instead of picking one in-silico pathogenicity score
(REVEL, AlphaMissense, EVE, etc.) and forcing it into a PP3/BP4 tier,
P-KNN calibrates *multiple* predictors jointly into a single
probability-of-pathogenicity. Explicit target: streamline the
ACMG/AMP PP3/BP4 assignment, which is currently arbitrary when scores
disagree.

**Why this is HIGH for you.** Sits directly on the "variant curation
tooling" and ACMG-AMP thread. Naturally pairs with the Pejaver
Bayesian-thresholds work and with recent work on PP3/BP4 calibration
for missense classifiers. Actionable: a candidate default for VCEP
pipelines where a single score is currently forced.

**Open questions.**
- Which predictors form the calibrated ensemble, and does adding more
  degrade calibration once redundancy is accounted for?
- Does the calibration hold across gene-classes with unusual prior
  pathogenic:benign ratios (e.g. tumor suppressors vs. late-onset
  cardiac genes)?
- Where does it break down for splicing / non-canonical variants?

### 2. RNA splicing evidence enables robust classification of BRCA1 exon 18 variants — ENIGMA consortium

- **Authors:** J Domènech-Vivó, H Tubeuf, RLS Mesman, A Drouet, et al.
- **Venue:** *American Journal of Human Genetics*, 2026
- **Source:** Same Scholar alert as above.
- **URL:** https://www.cell.com/ajhg/abstract/S0002-9297(26)00302-2
- **Bucket:** **HIGH** — Variant interpretation, splicing-evidence sub-thread.

**What it does.** ENIGMA pools allele-specific expression and
minigene splicing data to reclassify BRCA1 exon 18 variants against
prior ENIGMA classifications on ClinVar. Explicit contribution of RNA
splicing evidence to reclassification is quantified.

**Why this matters.** A concrete template for how to weight splicing
assays in a ClinGen-style VCEP tier, and a portable methodology for
BRCA1 exon-14 / BRCA2 exon-16-style splice-critical regions.

### 3. Functional characterization of 42 GAA missense variants using a validated in vitro cellular functional assay

- **Authors:** S Goomber, E Huggins, CW Rehder, GE Crawford, et al.
- **Venue:** *Molecular Genetics and Metabolism*, 2026
- **Source:** Same Scholar alert.
- **Bucket:** **HIGH** — Variant interpretation / Pompe disease.

**What it does.** In-vitro functional-assay classification of 42 GAA
missense variants, with Duke Pompe-clinic case examples showing how
the assay's read-out changes VUS resolution.

**Value.** GAA is a good stress-test case for AoU / UKB penetrance
scans against ClinVar VUS, and this assay gives functional PS3-strength
evidence for a large tranche of variants. Useful ground-truth layer if
we ever cross-tab GAA carrier phenotypes in EHR-linked cohorts.

### 4. Guidance on the reporting and clinical follow-up of individuals with incidentally discovered germline RET variants in the UK

- **Authors:** H Hanson, K Snape, RP Dias, SM Park, MG Shaikh, et al.
- **Venue:** *Endocrine-Related Cancer*, 2026
- **Source:** Gmail — Scholar alert on citations to "Guidance for estimating penetrance of monogenic disease-causing variants in population cohorts" (2026-08-29).
- **Bucket:** **HIGH** — Penetrance under population screening; variant interpretation.

**What it does.** UK-consortium guidance for what to do with incidentally
found germline pathogenic RET variants (i.e., discovered outside the
context of an MEN2 workup). Cites the "Guidance for estimating
penetrance…" paper, applying the population-vs-ascertained framework
in a specific gene with an actionable surveillance program.

**Why this matters for the interests file.** The paper is a real-world
worked example of penetrance-under-screening for a monogenic
cancer-syndrome gene — exactly the framing under **PheWAS / phecode
infrastructure → penetrance estimation for monogenic variants under
population-screening conditions**. Also useful as a citation target for
methods work applying the guidance to *AoU/UKB* incidental-finding
returns.

### 5. Resolving the complex CES1 genomic locus with Cas9-directed targeted long-read sequencing

- **Authors:** E Lekka, A Ambrodji, A Nater, A Ballah, U Amstutz, et al.
- **Venue:** *npj Genomic Medicine*, 2026
- **Source:** Gmail — Scholar alert on Kai Wang related research (2026-08-28).
- **Bucket:** **HIGH** — Variant interpretation in PGx-critical regions; pharmacogenomics of medication persistence sub-thread.

**What it does.** Cas9-directed long-read sequencing to resolve the
CES1 locus, which is problematic for short-read pipelines due to
paralog homology. CES1 metabolizes many ester-containing drugs
(clopidogrel, methylphenidate, oseltamivir, dabigatran etexilate).

**Why this matters.** Directly relevant to the "pharmacogenomic
modifiers of medication persistence" sub-thread — clopidogrel is a
textbook target — and to any UKB / AoU / MVP CES1-based PGx scan where
short-read calls are systematically wrong. Also a template for other
PGx-critical paralogous loci (CYP2D6, CYP2A6).

---

## Somatic mosaicism: CHIP, VEXAS, LOY

### 6. Independent associations of CHIP and mosaic Y loss with all-cause and cause-specific mortality in men

- **Authors:** Y Sun, Y Yu, C Zhu, L Cai, X Tan, Y Lu, N Wang, et al.
- **Venue:** *npj Aging*, 2026
- **Source:** Gmail — Scholar alert `intitle:"clonal hematopoiesis"` (2026-08-29).
- **Bucket:** **HIGH** — CHIP + LOY sub-thread (the male-specific LOY analogue of CHIP is an active watch).

**What it does.** In a men-only cohort, jointly models CHIP and mLOY
against all-cause and cause-specific mortality, and reports
**independent and additive** associations rather than one being a
proxy for the other.

**Why this is HIGH.** This is exactly the "male-specific LOY analogue
of CHIP" watch item in `INTERESTS.md`. Cleanest test to date of whether
LOY is a nuisance readout of hematopoietic aging or an independent
risk axis. Complements Li et al. *Atherosclerosis* 2026 (LOY × PAD)
and the Loh 2018 / Kessler 2022 lineage. Actionable follow-up: does
the additive pattern hold in AoU / MVP for cause-specific CVD subtypes?

### 7. IL-1-mediated cancer-adapted hematopoiesis in aging and clonal hematopoiesis

- **Authors:** F Caiado, NG Gonullu, MG Manz
- **Venue:** *Seminars in Immunology*, 2026
- **Source:** Same Scholar alert.
- **Bucket:** **HIGH (mechanism)** — CHIP thread.

**What it does.** Review linking IL-1 signalling to demand-adapted
hematopoiesis, aging, and cancer-associated selection of CHIP clones.
Frames anti-IL-1β as a candidate CHIP-modifying therapy — worth
citing when discussing the CANTOS-era case for CHIP as an actionable
risk axis rather than a passive biomarker.

### 8. Clonal hematopoiesis in immune-related and neurological disorders

- **Authors:** K Ogawa, T Yata, Y Hayashi, T Okuno
- **Venue:** *Immunological Medicine*, 2026
- **Source:** Same Scholar alert.
- **Bucket:** **METHODS-WATCH** — CHIP thread, expanding phenotype menu.

Review of CHIP × immune-mediated and neurological disease
(rheumatologic, neurodegenerative). Useful as a jumping-off point for
CHIP × phecode scans that extend beyond the classical CVD / hematologic
outcomes.

---

## EHR foundation models, digital twins, and multimodal patient trajectories

### 9. PULSE — Longitudinal alignments and syntheses of multimodal clinical data for personalized medicine

- **Authors:** W Wu, G Li, K Wang, H Xu, H Xiao, C Hu, S Liu, C Tang, et al.
- **Venue:** *Nature Computational Science*, 2026
- **Source:** Gmail — Scholar alert on citations to "Personalized lab test models to quantify disease potentials in healthy individuals" (2026-08-29). Companion News & Views: "A patient's longitudinal history reconstructs their unmeasured molecular profile" (Tanis, Lopez Alvarez, Davidson).
- **Bucket:** **HIGH** — Digital twins from EHR data sub-thread; multimodal EHR FMs.

**What it does.** PULSE aligns longitudinal, mosaic (partially observed)
multimodal patient measurements and *imputes* unmeasured molecular /
lab measurements from the patient's own history. Directly frames itself
as reconstructing the "unmeasured molecular profile."

**Why this is HIGH.** This is the clearest new instantiation of the
digital-twins-from-EHR framing (Zhang / Ideker / Oermann *Cell* 2026)
we've seen this quarter — individualized trajectory prediction from
mosaic longitudinal signal is the endgame of the CLMBR / MOTOR / MEDS
lineage. Also relevant to the representation-choice-and-downstream-use
thread: PULSE's alignment scheme *is* the representation choice.

**Follow-up:** is PULSE benchmarked against the pretraining-contamination
audit templates (scContam, MIA-scFM) referenced in the interests file?

### 10. NetMoint — Multimodal risk trajectories reveal heterogeneous paths to dementia (UK Biobank)

- **Authors:** Z Lee, H Li, T Liu, S Zhang, B Wang, J Fan, Y Zhang, Z Wang, L Bai
- **Venue:** arXiv 2608.26210v1 (2026-08-26)
- **Source:** `digests/2026-08-28.md`
- **Bucket:** **HIGH** — Biobank ML for precision health; trajectory-clustering; PGS-adjacent multi-omics thread.

**What it does.** Multimodal (plasma proteomics + structural MRI +
cerebral haemodynamics) subtype-specific risk prediction for AD / VD /
FTD across 1-, 5-, 10-, 20-year horizons in 104,120 UK Biobank
participants. Reports AUCs 0.930–0.937 in-cohort and 0.741 at 20 years
after harmonization to 138 shared features in an ADNI-to-UKB
external-validation slice. Multi-horizon risk profiling identifies
small (0.7% AD, 8.3% FTD) subgroups on very-high-risk trajectories
with distinct molecular signatures (lower TGFB1 in the AD group,
higher NDRG1 in FTD).

**Why HIGH.** Sits at the intersection of three threads:
(1) biobank ML tied to a clinical decision (who to screen), (2) chronic
disease trajectory clustering, (3) multi-omics-augmented risk stacking.
The temporal shift from structural to molecular predictors as horizon
lengthens is the interesting methodological claim.

**Watch-outs.** External validation is only ADNI → UKB (both
volunteer-biased Western cohorts), not to AoU / MVP. Trajectory
discovery on outcomes is prone to survivor / competing-risk bias —
the 20-year risks quoted assume the participant reached that horizon.

### 11. DINIRS — Digital Twin for Individualized Treatment Effects of Non-Invasive Respiratory Support

- **Authors:** MF Islam, J Mosier, V Subbian
- **Venue:** arXiv 2608.26915v1 (2026-08-27)
- **Source:** `digests/2026-08-28.md`
- **Bucket:** **HIGH** — Digital twins from EHR data; causal ML for HTE; ML for precision health tied to a clinical decision.

**What it does.** Censoring-aware digital-twin ITE framework for the
NIRS-vs-IMV choice in acute respiratory failure. Trained on MIMIC-IV
(n = 5,336), externally validated on eICU-CRD (n = 2,540). Transformer
encoder with a survival-attention gate decomposes 28-day
ventilator-free days into a survival probability × conditional
ventilation duration, and a cross-fitted, doubly robust learner
estimates ITEs.

**Result.** The DINIRS policy would yield +2.07 ventilator-free days
per patient vs observed practice, with benefit concentrated in
patients with less organ dysfunction. Mechanism: shorter ventilation
among survivors, not lower mortality. External validation reproduces
this without retraining.

**Why HIGH.** Combines three interests file lines cleanly: doubly-robust
causal-ML for HTE, digital-twin framing, and a decision-relevant
outcome (who benefits from NIRS). Prospective validation is
appropriately flagged as necessary before deployment.

### 12. Multi-source Knowledge Graph RAG for LLM-Based Medical Diagnosis

- **Authors:** K Kespechara, A Mingkhwan
- **Venue:** International Conference on AI in Healthcare, 2026
- **Source:** Gmail — Scholar alert on Zhiyong Lu related research (2026-08-28).
- **Bucket:** **HIGH** — Knowledge graphs & ontologies; rare disease diagnostic benchmarks; LLM-agent HPO diagnosis.

**What it does.** A multi-source KG-RAG framework that fuses
retrievals across complementary biomedical KGs (rather than a single
source) to ground LLM diagnostic outputs. Explicit claim: single-source
retrieval leaves diagnostic signals unexploited.

**Why HIGH.** The rare-disease sub-thread in `INTERESTS.md` calls out
GraphRareBench and separable metrics for ranking vs evidence coverage
in HPO-driven diagnosis. Multi-source KG RAG is a natural upstream
change that would move the "evidence coverage" metric, and should be
benchmarked against Phenolyzer / Phen2Gene / PhenoSV / LIRICAL /
Exomiser / PhenoGPT2 with the ranking-vs-coverage decomposition.

---

## Real-world causal inference & pharmacoepidemiology

### 13. Real-World Antidepressant Prescribing Patterns and Comparative Safety Outcomes — Multicenter OMOP-CDM Study

- **Authors:** J Min, S Shin, S Park, J Yun, K Park, SJ Rhie
- **Venue:** *Pharmaceuticals*, 2026
- **Source:** Gmail — Scholar alert on citations to George Hripcsak's articles (2026-08-28). Cites: "Risk of aortic aneurysm or dissection following use of…"
- **Bucket:** **HIGH** — Pharmacoepi / OMOP-CDM / real-world safety.

**What it does.** Retrospective multicenter observational study
using OMOP-CDM-standardized EHR data (1999–2026) in adults with newly
diagnosed depressive disorder — characterizes prescribing pathways
and comparative-safety outcomes across commonly prescribed
antidepressants.

**Why HIGH.** A direct exemplar of the OMOP-CDM comparative-safety
template we'd want to emulate for CFTR-modulator persistence, HRT
persistence, or GLP-1-RA persistence sub-threads. Reasonable to mine
for confounder-adjustment strategy (PS trimming, negative-control
outcomes) and reporting standards.

### 14. Performance, Generalizability, and Fairness of a PAD Detection Model Across Patient Phenotypes and Health Systems

- **Authors:** K Kallis, CR Quitevis, M Ramsis, NK Kabutey, et al.
- **Venue:** *medRxiv*, 2026
- **Source:** Gmail — Scholar alert on George Hripcsak citations.
- **Bucket:** **HIGH** — ML for precision health tied to a clinical decision; representation portability across sites (matches the fidelity-portability-audit sub-thread under Knowledge Representation in EHRs).

**What it does.** Uses the UC-Health data warehouse (five health
systems) to train and validate an EHR-based PAD-detection model, with
explicit fairness and generalizability audits across subgroups.

**Why HIGH.** Directly relevant to the "fidelity, portability, and
audit of representations — how representation choices drift across
sites" sub-thread. Also tied to a real screening decision (PAD is a
canonical under-diagnosed cardiovascular phenotype in EHR).

### 15. QResearch primary care records linked to national hospital and cancer registry data: a validation study

- **Authors:** S Kulkarni, V Perletta, Z Wang, JW Tomlinson, et al.
- **Venue:** *ESMO Real World Data and Digital Oncology*, 2026
- **Source:** Gmail — Scholar alert on Gary S. Collins new articles (2026-08-28).
- **Bucket:** **METHODS-WATCH → HIGH** for EHR phenotyping / interoperability sub-thread.

**What it does.** Validation of the QResearch primary-care linkage
(primary care ↔ HES ↔ cancer registry ↔ mortality) against the
national cancer population. Explicit statement of what the linkage
represents, and where it under-represents.

**Why HIGH.** The Lemieux et al. *JAMIA Open* 2026-07 framing in the
interests file wants interoperability-consequences papers; this is a
direct data-quality-of-representation paper for a widely used
UK EHR resource.

---

## PGS, GWAS, and genetic epidemiology

### 16. Associations of polygenic risk scores with intestinal surgery, gastrointestinal cancer, and all-cause mortality in 5,021 UK Biobank IBD patients

- **Authors:** Y Yuan, Y Feng, D Wang, J Xie, H An, H Zhou, W Shi, et al.
- **Venue:** *Scientific Reports*, 2026
- **Source:** Gmail — Scholar alert `"UK Biobank"` (2026-08-26).
- **Bucket:** **HIGH** — PGS/PRS thread; IBD sub-thread.

**What it does.** In 5,021 UKB IBD participants (CD n = 1,427; UC
n = 3,594), disease-specific standardized PRSs are related to
downstream outcomes (intestinal surgery, GI cancer, all-cause
mortality). Cox-model estimates pooled across 20 imputations. A
clinically extended PRS is compared to a "baseline PRS."

**Why HIGH.** Sits at the intersection of the PGS-as-discovery /
composite-risk thread and the IBD sub-thread. The interesting move is
PRS-as-prognostic within already-diagnosed disease — closer to
disease-modifier PRS than to incidence PRS. Complements the
Souaiaia-tails and Baya-residuals framing (though from a different
angle: not discovery but prognostication).

**Watch-out.** UKB IBD is small (5k) and healthy-volunteer-selected.
External validation in an EHR-linked cohort (BioVU / AoU / MVP) is
the natural next step.

### 17. Patient and primary care clinician perspectives on polygenic risk scores for prostate cancer screening — national qualitative study

- **Authors:** MPHL Cheam, PDC Gillespie, MPHAA Antwi, et al.
- **Venue:** *Genetics in Medicine*, 2026
- **Source:** Gmail — Scholar alert on George Hripcsak citations. Cites: "Returning integrated genomic risk and clinical recommendations…"
- **Bucket:** **METHODS-WATCH** — PGS clinical translation.

Not methods-heavy, but worth logging as an implementation-science
data point for PGS-informed shared decision-making — the human-side
constraints that will shape whether PGS scans in AoU / MVP have any
clinical uptake.

### 18. Hofmeister & Kutalik — 245,884 UKB + 194,325 Estonian Biobank, 69 complex traits (Research briefing)

- **Authors:** RJ Hofmeister, Z Kutalik
- **Venue:** *Nature Human Behaviour* (research briefing), 2026
- **Source:** Scholar alert `"UK Biobank"` (2026-08-26).
- **Bucket:** **METHODS-WATCH** — PGS / GWAS methodology across two large biobanks.

Method applied jointly to UKB and Estonian Biobank across 69 traits.
Worth pulling the full paper for the methods contribution
(Augustine Kong quoted in briefing).

---

## Weaker matches (recorded, not detailed)

Not detailed, but noted for context. These were surfaced by the recall
step but do not clearly advance an active thread.

- **arxiv-digest 2026-08-27**: *Can You Trust Frozen Hematology
  Foundation Models under Acquisition Shift?* (Sharma & Tapadiya) —
  interesting FM-robustness audit, off-thread (hematology-image FMs).
- **arxiv-digest 2026-08-26**: *RIBOSPAN: Long-Context RNA Foundation
  Model* — off-thread (RNA FM).
- **arxiv-digest 2026-08-25**: *Identification and Inference for Causal
  Effects in Extremes* — off-thread (climate/finance).
- Several UKB Scholar alerts on liver-eye / cardiovascular / lifestyle
  associations (Ying et al. CKM × blinding eye; Huang et al. TyG × ocular
  disease; López-Bueno cardiorespiratory fitness; Kozin Porat ADHD ×
  lifestyle; Zhang puberty × cancer survival; Jiang multisystem
  physiology × depression; He planetary diet × sleep; Shi PIVA × depression
  in COPD; Meng bitter foods GWAS) — SKIP unless a specific overlap
  emerges. Cataloged but not detailed.
- Multiple LLM/KG/reasoning arXiv papers surfaced via the Zhiyong Lu
  alert (Chain-of-Experience, Depth Division of Labor, Reasoning
  Breadth, Vocabulary-based corpus estimation) — off-thread.
- APOL3/GBP1 antigen cross-presentation paper — this is on
  APOL3 (immunity), not APOL1 kidney disease; SKIP for the APOL1
  kidney/transplant sub-thread.

---

## Reading order recommendation

1. **P-KNN** (#1) and **BRCA1 ENIGMA splicing** (#2) — small, actionable, ready to cite.
2. **CHIP + mLOY mortality** (#6) — closes an open question in the LOY
   watch, do this before another CHIP paper reopens it.
3. **PULSE** (#9) + **DINIRS** (#11) — the two clearest instantiations
   of the digital-twin-from-EHR framing this month.
4. **Multi-source KG-RAG for medical diagnosis** (#12) — for the
   rare-disease + KG evidence-coverage discussion.
5. **RET incidental-finding guidance** (#4) — for the penetrance-
   under-screening thread.
6. **UKB IBD PRS-outcome** (#16) — for the PGS composite-risk framing.

Everything else is background reading.
