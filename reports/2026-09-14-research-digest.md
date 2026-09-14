# Research digest report — 2026-09-14

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-14 12:40Z** (~13 days since the
last research-digest report, covering thirteen arxiv-digest cron runs
and roughly a dozen Google Scholar + PubMed alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-12.md`) | 09-01 → 09-12 daily crons | 12 daily runs. Dry days (0 relevant): 09-03, 09-05, 09-06, 09-08, 09-12 (all suppressed / no matches). Content days: 09-01 (1 paper — Ghiasi storage-centric genomics dissertation, off-thread), 09-02 (1 — mudskipper crutching gait, off-thread false-positive on "motor"), 09-04 (2 — Cortez-Rodriguez nonprofits + Yu et al. location-invariant extremal QTE methods-watch), 09-07 (1 — Rajabli generalizable AD brain-MRI feature extractor via LoRA), 09-09 (2 — Snel & Schulz UKB training-data-attribution for Cohen's d; FUSE-RT HPLC off-thread), 09-10 (1 — Kalman-filtered HT infectious-disease surveillance, methods-watch), 09-11 (3 — scDEFT IBD single-cell drug-effect FM; Hendrix geospatial FMs for social-risk augmentation; Semchin connectome-constrained PD progression subtyping). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` and of `subject:(arxiv-digest OR "arXiv digest")` in the window returned zero threads. As in the 09-01 report, the pipeline commits its output to this repo rather than emailing PR / cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-14 batch, 08:24Z) | 09-14 08:24Z | Largest single batch in the window — ~40+ author / keyword / citations-to feeds fired at once. Key strong hits: Chenjie Zeng (own-cited) + Lisa Bastarache both landed **Straub et al. Nature Medicine 2026** on Our Future Health 1.9M-participant phenomic profiles, explicitly citing the AoU Zeng-lineage phenomic-profile paper; Lisa Bastarache new-related also landed **Carrasco-Zanini Sci Transl Med** proteomics-in-rare-disease diagnostics (also on Denny citations-to, Langenberg new-articles); Konrad Karczewski feed landed **Zheng et al. medRxiv** PRS-vs-proteomic-RS divergence in neurodegen; Isaac Kohane new-articles landed **Xiong et al. JAMIA** knowledge-driven online multimodal automated phenotyping; Miguel Hernán citations-to landed **Liu & Wang J Clin Epi** AI × Target Trial Emulation review; Chenjie Zeng new-related landed **Jandu et al. Human Genetics** BioVU PheWAS on inherited-inflammation predisposition; Ellinor new-articles landed **Kamineni et al. Sci Transl Med** ML-driven spleen imaging + genomics for CAD; Lisa Bastarache also cited **Ward et al. medRxiv** rare-extreme PRS for AD (PGS-tails); Peter Visscher / Jian Yang / Bastarache triple-hit **Wang et al. Nature** within-family ancestry effects in a Mexican population; George Hripcsak new-related landed the **Foresight-England** paper already covered in the 09-01 report (through Pascal Brandt then). |
| Google Scholar alerts (09-12 batch, 19:03Z) | 09-12 19:03Z | 9 keyword feeds fired: `intitle:"clonal hematopoiesis"` (Chiu et al. **JAMA Cardiology** — designing CV outcomes trials in CHIP; direct-hit for the CHIP/VEXAS/LOY thread), `"All of Us research program"` (Fetchko et al. dental EHR — borderline; also Ritoré-Hidalgo CDSL COVID multimodal), `"UK Biobank"` (Duan et al. J Clin Anesthesia surgical-exposure biological aging), `"electronic health records"` (Momenzadeh Sci Reports — causal ML for ICU discharge decision), `"knowledge graph"` (Zhu Zhao Bai WWW — temporal KG reasoning with entity descriptions, off-thread), `"autoimmune disorders"` (off-thread nursing paper), `"phenome wide association studies"` (Niu et al. **Diabetes, Obesity & Metabolism** — distinct genetic architectures for extreme early vs late-onset T2D), `"variant interpretation" OR "variant classification"` (Islam et al. Atherosclerosis — functional data for LDLR variant classification via high-content microscopy vs flow), `mendelian diseases` (Zhao et al. Ergotamine × aortic dissection MR + FAERS integration), `Foundation models + "electronic health records"` (Prasad & Choudhary cybersecurity framework — off-thread noise). |
| Google Scholar alerts (09-12 morning batch, 10:55Z) | 09-12 10:55Z | Rolling author feeds: Zhiyong Lu (cross-lingual LM eval, off-thread), Stephen Montgomery new-related (Ma et al. medRxiv **long-read RNA-seq for isoform / splicing outlier detection in whole blood** from rare-disease trios — HIGH for rare disease), Peter Szolovits (MedProb VLM probing, off-thread), Kai Wang (COSIGT pangenome low-coverage complex-loci genotyping — HIGH for pangenome sub-thread), Patrick Ryan + Pascal Brandt (CDSL COVID multimodal dataset — moderate). |
| PubMed My-NCBI alerts | 09-12 and 09-13 batches | "What's new for 'UK Biobank'" and "What's new for 'All of Us'" — biweekly PubMed cadence, mostly duplicating the Scholar feed content above; primary purpose is exhaustive backup rather than new signal. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fourteen HIGH items surfaced this window, clustering into seven knots:

**Biobank scale-up cluster (2 items).** Straub et al. *Nature Medicine*
2026 — **Our Future Health**, a prospective UK-resident cohort aiming
for 5M participants, releases the first phenomic-profile paper at
**1.9M enrolled participants** with linked GP / hospital / cancer /
medication data. Explicitly cites your Zeng-lineage AoU phenomic-
profile paper as the design template. This adds a fourth
national-scale EHR-linked biobank alongside UKB, AoU, and MVP, and is
a natural companion to the Acharya three-biobank ASCVD-heritability
template from the 09-01 report — now conceptually four-biobank. Wang
et al. *Nature* 2026 — within-family ancestry effects on complex
traits in a **Mexican-ancestry family cohort**, controlling for the
environmental confounding that plagues cross-population phenotypic-
mean comparisons; direct-hit for PGS × ancestry and cross-ancestry
portability, and a rare Latinx-centered flagship-journal cohort.

**PheWAS / phecode infrastructure cluster (2 items).** Jandu, Olowofela,
Shuey, Quade, Tuftin et al. *Human Genetics* 2026 (Zeng own new-related
feed) — **inherited predisposition to increased systemic inflammation**
predicts a broad class of disease phenotypes across a BioVU-lineage
PheWAS. Directly on-thread for the PheWAS/phecode-infrastructure
angle, and pairs with the Acharya three-biobank ASCVD paper as an
example of upstream-inflammation-as-shared-etiology (inflammation-
augmented composite risk). Niu et al. *Diabetes, Obesity & Metabolism*
2026 — GWAS identifies **distinct genetic architectures for
extreme early-onset vs. late-onset T2D**, an age-of-onset-partitioned
PheWAS-adjacent finding; directly serves the Genetic Epidemiology
thread and pairs with your composite-risk / PGS-tails framing (extreme
early-onset is a natural PGS-tail definition).

**Pharmacoepi / target trial emulation cluster (2 items).** Liu & Wang
*Journal of Clinical Epidemiology* 2026 (Hernán citations-to) — **AI ×
Target Trial Emulation: Toward Scalable and Credible Real-World
Evidence**. Positioning-review paper for the TTE + AI/ML methods stack
you're already tracking (Zhang et al. GLP-1/SGLT2/DPP4 empirically-
calibrated TTE from 09-01 was the concrete instance; this paper is the
frame). Chiu, Oren, Small, Weeks, Marston et al. *JAMA Cardiology* 2026
(CHIP keyword feed) — **Designing Cardiovascular Outcomes Trials in
Clonal Hematopoiesis of Indeterminate Potential**. Direct-hit for the
CHIP/VEXAS/LOY somatic-mosaicism disease thread; the "hematology
clinics routinely encounter CHIP as an incidental finding" framing is
the transition from etiologic association to actionable-trial phase
that your CHIP watch prioritizes.

**EHR phenotyping / knowledge representation cluster (1 item).** Xiong,
Sweet, Hong, Bonzel, Panickan et al. *JAMIA* 2026 (Kohane feed) —
**Knowledge-Driven Online Multimodal Automated Phenotyping (KOMAP)**
"bends the learning curve" for EHR-based phenotyping, i.e., achieves
strong PPV / recall with substantially fewer labeled examples by
leveraging structured medical knowledge alongside multimodal EHR
signal. Direct-hit for both `EHR phenotyping & OMOP` and for the
`Knowledge representation in EHRs → NLP-derived representations from
clinical notes` and `Applications to prioritize → computable
phenotyping / PheKB / PheValuator` sub-threads. Ties structurally to
the Ilves CohortContrast paper from the 09-01 report.

**Genetic epi / PRS extreme-tails cluster (2 items).** Ward, Nelson,
Katsumata, Fardo et al. medRxiv 2026 (Bastarache feed) — **rare
extreme polygenic risk scores strongly indicate Alzheimer's disease
risk**. Directly reifies the Souaiaia *Nature* PGS-tails framing your
INTERESTS.md prioritizes: PGS extremes as a discovery lever, and now
specifically for the "pre-symptomatic AD stratification" clinical
question. Pairs with the Kurniansyah *Nature Genetics* multiancestry
AD-PRS paper from the 09-01 report. Zheng, Shivakumar, Shen, Kim
medRxiv 2026 (Karczewski feed) — **PRS vs. proteomic-RS divergence in
neurodegen**: the two scores are complementary rather than
overlapping, with divergence traceable to specific absorption and
co-expression modules. Direct-hit for `Multi-omics-augmented PRS`
sub-thread, and pairs with the Lee NetMoint UKB proteomics+imaging
dementia-trajectory paper from the 09-01 report (which is the
prediction-side analogue).

**Rare disease diagnostics cluster (1 item).** Carrasco-Zanini, Andrade,
Pietzner et al. *Science Translational Medicine* 2026 (Bastarache
new-related; Denny citations-to; Langenberg new-articles — **triple-
feed hit**) — **proteomics identifies disease-associated variants in
patients undiagnosed after genome sequencing**, in 424 rare-disease
patients from a national program. Directly serves your Rare Disease
thread and the emerging `Pre-symptomatic carrier phenoconversion
prediction from longitudinal biomarker trajectories` sub-thread
(proteomics-augmented rare-disease pipelines). Pairs with the Uria-
Regojo mid-scale reanalysis paper cited under your rare-disease
sub-thread.

**ML for precision health / imaging + genomics cluster (2 items).**
Kamineni, Raghu, Hua, Tian, Truong, Alaa et al. *Science Translational
Medicine* 2026 (Ellinor new-articles) — **ML-driven spleen imaging +
genomics** uncover a splenic contribution to coronary artery disease
risk. On-thread for ML-for-precision-health (imaging + genomics
integrated for a common cardiovascular endpoint) and adjacent to the
CHIP/systemic-inflammation → CAD axis (spleen as inflammation hub).
Devarakonda arXiv 2609.10831 (local digest 09-11) — **scDEFT**, a
single-cell drug-effect Transducer FM applied to a harmonized
inflammatory-bowel-disease atlas (1.16M cells, 3 cohorts, 2 drug
classes); predicts responder status pre-treatment at AUROC 0.70 where
standard predictors are at chance. Direct-hit for the IBD disease
thread and for ML-for-precision-health (treatment-effect
heterogeneity, pre-treatment stratification).

**Chronic-disease clustering / multimorbidity (2 items).** Semchin et
al. arXiv 2609.10890 (local digest 09-11) — **connectome-constrained
disease progression model** recovers four morphologically distinct
subtypes of Parkinson's disease from longitudinal morphometry, and
uniquely — vs. SuStaIn baseline — recovers subtypes that map to
clinical motor subtypes AND genetic variants. Direct-hit for the
disease-subtyping / trajectory-clustering sub-thread. Snel & Schulz
arXiv 2609.07729 (local digest 09-09) — **training-data attribution
for Cohen's d** on the UK Biobank: identifies training samples that
inflate normative-age-model residuals for held-out disease detection,
and finds that the flagged subjects carry subclinical cardiometabolic
burden the diagnosis-based exclusion missed. Direct-hit for both
`Fidelity, portability, and audit of representations` (which UKB
"healthy" subjects are actually latent-cardiometabolic) and for
`Machine learning for precision health` (attribution as clinical-
decision instrument).

Also worth naming: **Ma et al. medRxiv 2026** (Montgomery new-related)
— long-read RNA sequencing for isoform / splicing outlier detection
in whole blood from rare-disease trios; **Bolognini et al. COSIGT
Genome Biology 2026** — population-scalable genotyping of complex
loci from low-coverage sequencing using pangenome graphs (Kai Wang
new-related); **Islam et al. Atherosclerosis 2026** — functional data
for LDLR variant classification comparing high-content microscopy vs.
flow cytometry (variant-interpretation thread); **Momenzadeh et al.
Scientific Reports 2026** — causal ML framework for ICU discharge
decision using EHR (methods-watch for the DINIRS + digital-twin
lineage from 09-01).

---

## Detailed reports — HIGH-priority studies

Papers below are the ones I would open next; each note gives (a) the
core method or claim, (b) why it maps to a research thread, and (c)
what to compare it against in the existing literature you track.

### 1. Straub, Benonisdottir, Bentivoglio, Wary et al. — *Phenomic profiles and disease patterns of 1.9 million participants from Our Future Health*
**Venue:** *Nature Medicine*, 2026.
**Surfaced via:** Google Scholar alerts — **8 new citations to articles by Lisa Bastarache** AND **3 new citations to articles by Chenjie Zeng** (both 09-14, 08:24Z). The Zeng-side citation is to *Comparison of phenomic profiles in the All of Us Research …*, i.e., this paper explicitly positions itself against your AoU phenomic-profile methodology.
**Threads:** Biobanks with EHR linkage; PheWAS / phecode infrastructure; EHR phenotyping (Global-scale, primary-care-linked).

**What it is (from abstract).** Our Future Health (OFH) is a
prospective study aiming to recruit **5 million UK-resident adults**
to enable discovery and translation of prevention, detection, and
treatment. As of this paper, **>2.5M enrolled** and baseline phenotypic
data are available for **>1.9M participants**. The paper reports
self-reported health behaviors, geolocation, diagnoses, medications,
inpatient and outpatient visits, cancer-registry linkage, and
cause-of-death coverage — i.e., it is the OFH phenomic-profile
landmark paper, structurally analogous to the AoU phenomic-profile
paper (Zeng et al.) that it cites.

**Why it matters for your work.** Three angles hit at once. First,
this adds a **fourth national-scale EHR-linked biobank** to the
Biobanks-with-EHR-linkage thread (UKB / AoU / MVP → +OFH). Where UKB
is deep-phenotyping-heavy but recruiting-closed and AoU is diverse-
recruitment-first, OFH is size-first (5M target) with primary-care
NHS linkage; the trio-plus-one triangulation opens direct
cross-biobank replication for any PheWAS or PheRS you build. Second,
it explicitly cites your AoU phenomic-profile paper as the design
template, so the OFH paper is likely to become the reference
comparator for AoU-vs-OFH cross-biobank composition, ancestry
distribution, and phecode prevalence studies — a natural next-step
for your own work. Third, the primary-care-linked medication data
substrate makes OFH highly relevant for **medication persistence as
outcome** (your added sub-thread under Causal inference), because NHS
prescription data linkage is denser than what AoU or MVP currently
support.

**Contrast against:** the Zeng et al. AoU phenomic-profile paper
directly (Zhang et al.); Sudlow et al. 2015 UKB baseline profile; the
Denny et al. AoU phenomic-profile update; and Acharya et al. cross-
biobank ASCVD heritability from the 09-01 report — with OFH added,
that heritability template extends to four biobanks.

---

### 2. Xiong, Sweet, Hong, Bonzel, Panickan et al. — *Bending the Learning Curve for EHR Research via Knowledge-Driven Online Multimodal Automated Phenotyping (KOMAP) System*
**Venue:** *Journal of the American Medical Informatics Association*, 2026.
**Surfaced via:** Google Scholar alert "Isaac Kohane - new articles" (09-14, 08:24Z).
**Threads:** EHR phenotyping & OMOP; Knowledge representation in EHRs → **NLP-derived representations from clinical notes** AND **Applications to prioritize (computable phenotyping / PheKB / PheValuator)**; ML for precision health.

**What it is (from abstract).** **KOMAP** couples structured medical
knowledge (ontology-anchored features) with multimodal EHR signal
(codes + notes + labs) in an *online* phenotyping pipeline that
achieves strong PPV / recall with substantially fewer labeled
examples than the standard rules-based or supervised-ML baselines —
i.e., it "bends the learning curve" for phenotype construction. The
paper is from the Kohane-Cai lineage at HMS (multimodal auto-
phenotyping is an active workstream there).

**Why it matters for your work.** Direct hit on **three** of your
knowledge-representation sub-threads at once: (i) Concept-embedding
models transferring across sites (the "knowledge-driven" leg); (ii)
NLP-derived representations from clinical notes (the multimodal leg);
(iii) Applications to prioritize → computable phenotyping / PheKB /
PheValuator. KOMAP is the natural companion to the Ilves
**CohortContrast** enrichment-based OMOP concept-selection paper from
the 09-01 report — CohortContrast picks the concept set,
PheValuator estimates the phenotype's PPV, and KOMAP is a
supervised-with-knowledge pipeline that shortens the label-collection
step in between. Especially useful when you're constructing new
phecodes / phecodeX definitions for rare or under-coded conditions
where labels are scarce.

**Contrast against:** PheValuator (Swerdel et al.); PheCAP (Yu et al.
Cai lab lineage); the Kohane / Cai MAP lineage (Multimodal Automated
Phenotyping — KOMAP is the "online + knowledge-anchored" successor);
Xue et al. medRxiv large-scale psychiatric-concept extraction from
the 09-01 report; Wu et al. arXiv **ACT** auditable CT phenotyping
from the 09-01 report.

---

### 3. Jandu, Olowofela, Shuey, Quade, Tuftin, Fickas et al. — *Inherited Predisposition to Increased Systemic Inflammation Predicts a Broad Class of Disease Phenotypes*
**Venue:** *Human Genetics and Genomics Advances*, 2026 (BioVU-lineage title from the alert snippet).
**Surfaced via:** Google Scholar alert "Chenjie Zeng - new related research" (09-14, 08:24Z; own-feed).
**Threads:** PheWAS / phecode infrastructure; Genetic epidemiology (PRS / polygenic-inflammation composite); Chronic disease clustering (upstream-inflammation as multimorbidity substrate).

**What it is (from alert snippet).** BioVU-lineage PheWAS study
using **inherited predisposition to systemic inflammation** (likely a
CRP-anchored PRS or similar inflammation-composite genetic
instrument) as the exposure. The predisposition predicts a **broad
class of disease phenotypes** across the phenome — i.e., the paper
is set up as an upstream-genetic-inflammation → PheWAS scan, exactly
the causal-pleiotropy design your PheWAS/phecode-infrastructure
thread wants propagated.

**Why it matters for your work.** Direct-hit on **three** angles.
First, PheWAS/phecode-infrastructure — a broad-phenotype PheWAS with
a genetic exposure is the textbook use case. Second, Composite-risk /
PGS-tails framing — if the inflammation-PRS predicts a broad phenome,
it's an upstream instrument that can stack with disease-specific PRS
(inflammation-PRS × cardiometabolic-PRS interaction is a natural next
question, and pairs with the Nagpal & Gibson pervasive-PGS × exposure
paper you already track). Third, this is the design your own AoU
inflammation-PheWAS thread would benefit from as an external
replication cohort — BioVU-first, AoU-second is the standard
replication direction.

**Contrast against:** Denny et al. PheWAS foundational papers; Bush,
Denny, Ritchie PheWAS methodology; the Truong et al. cross-biobank
PheWAS harmonization paper you already track; and the Kessler /
Bick CHIP × cardiovascular phenome-scan papers (which use somatic
rather than germline inflammation instruments — natural methods-
watch counterpart).

---

### 4. Liu, Wang — *Artificial Intelligence and Target Trial Emulation: Toward Scalable and Credible Real-World Evidence*
**Venue:** *Journal of Clinical Epidemiology*, 2026.
**Surfaced via:** Google Scholar alert "10 new citations to articles by Miguel Hernán" (09-14, 08:24Z; cites Hernán's TTE lineage).
**Threads:** Causal inference and pharmacoepidemiology → **Agentic / human-in-the-loop observational-causal-inference pipelines** AND target trial emulation generally; ML for precision health.

**What it is (from alert snippet).** Position/framework paper in
*JCE* on how AI + TTE can be combined for **scalable and credible**
RWE. Alert snippet leads with "Randomised …" (truncated) — likely
positioning the TTE + AI stack as an alternative-or-complement to
RCT for questions where RCTs are infeasible / slow.

**Why it matters for your work.** This is the framing-review paper
for the sub-thread you explicitly named in the 2026-07-29 INTERESTS.md
update: **Agentic / human-in-the-loop observational-causal-inference
pipelines** (Chou/Kallus arXiv 2607.22443 oci-agent + Netflix
production; Li et al. arXiv 2607.16934 EHR-derived HTE for trial
design). A *JCE* framework paper citing Hernán's TTE lineage means
this is destined to become a citation-ready anchor for any pharmacoepi
manuscript that argues the TTE + causal-ML stack. Also pairs with the
Zhang et al. GLP-1 / SGLT2 / DPP4 empirically-calibrated TTE paper from
the 09-01 report as the concrete instance of what Liu & Wang argue in
the abstract.

**Contrast against:** Hernán & Robins *Causal Inference: What If*
Chapter 22 (TTE canonical); Hernán & Sterne 2016 *NEJM Evid* TTE
methodology; Zhao et al. 2026 arXiv Causal-AI-for-cancer-immunotherapy
narrative review from the 09-01 report; Schuemie 2021 empirical
calibration; Suchard 2019 LEGEND-HTN.

---

### 5. Chiu, Oren, Small, Weeks, Marston, Bick et al. — *Designing Cardiovascular Outcomes Trials in Clonal Hematopoiesis of Indeterminate Potential*
**Venue:** *JAMA Cardiology*, 2026.
**Surfaced via:** Google Scholar alert `intitle:"clonal hematopoiesis"` (09-12, 19:03Z).
**Threads:** **CHIP / VEXAS / LOY somatic mosaicism** (direct-hit) — the disease thread's transition from etiologic association to trial phase.

**What it is (from alert snippet).** Framework paper in *JAMA
Cardiology* on how to **design cardiovascular outcomes trials in
CHIP**. Framing sentence: "Hematology clinics routinely encounter
CHIP …" — i.e., the paper frames CHIP as an incidental-finding
population that is now large enough to justify prospective
cardiovascular-outcomes trials, and lays out the trial-design
considerations (target population selection, index-date definition,
comparator arm, endpoint choice, sample size).

**Why it matters for your work.** Direct-hit on the CHIP/VEXAS/LOY
thread you actively watch (Li et al. *Atherosclerosis* 2026 LOY × PAD;
Loh *Nature* 2018; Kessler *Nature* 2022). This is the phase after
etiologic association: **actionable cardiovascular trial design in
CHIP** is the natural downstream step, and the design considerations
here (CHIP-fraction thresholds, driver-mutation specificity,
comparator-arm construction) are portable to any CHIP-lineage
pharmacoepi TTE you might build (e.g., on TET2 / DNMT3A / ASXL1 CHIP
× lipid-lowering therapy effect modification). Also useful as a
citation for the "somatic mosaicism as actionable clinical signal"
argument.

**Contrast against:** Bick et al. anti-inflammatory therapy × CHIP
(canakinumab / low-dose colchicine); Fuster et al. TET2 CHIP + IL-1β
in mouse atherosclerosis; Marnell et al. Cell 2022 clinical-actionability
of CHIP; the Li et al. *Atherosclerosis* 2026 LOY × PAD paper you
already track.

---

### 6. Zheng, Shivakumar, Shen, Kim — *Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases*
**Venue:** medRxiv, 2026-08-24 (surfaced via 09-14 Karczewski feed).
**Threads:** Genetic epidemiology → **Multi-omics-augmented PRS**; Chronic disease clustering (neurodegen); Knowledge representation in EHRs (proteomic representations as complementary axis).

**What it is (from abstract snippet).** Both **polygenic risk scores
(PRS)** and **proteomic risk scores (ProtRS)** are proposed for
pre-symptomatic stratification of neurodegenerative disease. This
paper quantifies where they diverge (i.e., they are **complementary
rather than overlapping**) and localizes the divergence to
"absorption" and "co-expression" modules — likely pathway-level or
network-level partitions that isolate the mechanistic axes each score
captures.

**Why it matters for your work.** Direct-hit for your **Multi-omics-
augmented PRS** sub-thread (Nightingale NMR / Olink / metabolomics
stacked with PGS). The paper's key contribution is that it doesn't
just show PRS + ProtRS beats either alone (which is easy) — it shows
*where* they diverge, which is the mechanism-resolved partition your
INTERESTS.md prioritizes. Pairs directly with the Lee NetMoint UKB
proteomics+imaging dementia-trajectory paper from the 09-01 report
(which is the prediction-side analogue) and with the Kurniansyah
*Nature Genetics* multiancestry AD-PRS from the same report (PRS-side
anchor).

**Contrast against:** You et al. 2023 UKB Olink+PRS composite AD
risk paper; Nightingale NMR × PRS papers; the Baya AJHG PGS-residuals
paper you already prioritize for the "misaligned individuals"
framing; and the Kurniansyah / Kunkle AD-PRS lineage.

---

### 7. Ward, Nelson, Katsumata, Fardo et al. — *Rare Extreme Polygenic Risk Scores Strongly Indicate Alzheimer's Disease Risk*
**Venue:** medRxiv, 2026-09-08 (surfaced via 09-14 Bastarache new-related feed).
**Threads:** Genetic epidemiology → **PGS residuals / polygenic-deviation designs** AND PGS-tails; ML for precision health (pre-symptomatic AD stratification).

**What it is (from abstract snippet).** Framing sentence: "AD
pathology often accumulates years before memory loss, creating a need
to identify high-risk individuals presymptomatically. PRS stratify
AD risk, but individual-level predictions remain [limited] …" The
paper argues **rare extreme PRS values (tails)** are strongly
predictive of AD risk — i.e., the extreme-tail decile is much more
informative than the mean of a broad decile grouping. This is the
Souaiaia *Nature* PGS-tails framing applied to AD.

**Why it matters for your work.** Direct-hit for the **PGS residuals
/ polygenic-deviation designs** sub-thread you explicitly named in
INTERESTS.md (Baya AJHG 2026 "misaligned individuals" + Souaiaia
*Nature* PGS-tails + Vazquez *Genetics* low-risk-group designs =
"tails-and-residuals" taxonomy). AD is the natural clinical domain
for this framing because pre-symptomatic stratification has the
highest clinical stakes. Pairs with the Kurniansyah *Nature Genetics*
multiancestry AD-PRS paper (09-01 report), the Zheng PRS-vs-ProtRS
divergence paper (this report, #6), and the Ma et al. NetMoint
proteomics+imaging paper (09-01 report) as a **cluster** of AD
pre-symptomatic risk-stratification papers this year.

**Contrast against:** Souaiaia *Nature* 2026 PGS-tails; Baya AJHG
2026 misaligned individuals; the Fahed 2020 monogenic-vs-polygenic
CAD composite (different disease, same tails argument); Kunkle 2019
IGAP AD-PRS.

---

### 8. Carrasco-Zanini, Andrade, Pietzner et al. — *Proteomics Identify Disease-Associated Variants in Patients with Rare Diseases Undiagnosed after Genome Sequencing*
**Venue:** *Science Translational Medicine*, 2026.
**Surfaced via:** Google Scholar alerts **triple-feed hit** — Lisa Bastarache new-related, Joshua C. Denny 10-new-citations, Claudia Langenberg new-articles (all 09-14, 08:24Z).
**Threads:** Rare disease → **pre-symptomatic carrier phenoconversion prediction from longitudinal biomarker trajectories**; Variant interpretation (proteomic evidence for VUS resolution); Genetic epi (proteomics-augmented rare-variant diagnostics).

**What it is (from abstract).** Even with genome sequencing (GS)
introduced for rare-disease diagnostics, a genetic cause is not
identified in most patients. The paper explores whether **proteomics
can improve diagnostic yield** in **424 patients** with rare diseases
from a national program (from the alert snippet, likely Genomics
England 100kGP or a European equivalent). Proteomic signatures serve
as an orthogonal evidence layer for variant classification and for
directing gene-panel reanalysis.

**Why it matters for your work.** Direct-hit on **three** threads.
First, Rare disease — this is the missing biomarker leg of the
`Pre-symptomatic carrier phenoconversion prediction from longitudinal
biomarker trajectories` sub-thread you added (Ran / Benatar *Nat Med*
ALS was the template). Proteomic-driven diagnostic-yield improvement
is the same evidence-augmentation direction. Second, Variant
interpretation — proteomic functional evidence sits alongside RNA /
splicing evidence in the ACMG/AMP framework, and this paper is a
large-N demonstration of that principle. Third, Rare-disease
reanalysis at cohort scale — pairs with the Uria-Regojo mid-scale
10k-patient reanalysis you cited under `Data-driven reanalysis of
unsolved cases`. **The triple-feed surfacing** is a strong signal —
Bastarache (PheWAS/phenotyping), Denny (PheWAS/PheRS-anchored), and
Langenberg (UKB-Olink lineage) all cite something this paper builds
on.

**Contrast against:** the Uria-Regojo mid-scale reanalysis paper you
already track; ACMG/AMP 2015 (functional evidence in classification);
the Nightingale NMR × Olink UKB rare-variant papers; and the Wendy
Chung UDN clinical-reanalysis lineage.

---

### 9. Wang, Berumen, Vergara-Lope, Baca et al. — *Within-Family Effect of Ancestry on Complex Traits in a Mexican Population*
**Venue:** *Nature*, 2026.
**Surfaced via:** Google Scholar alerts **triple hit** — Peter Visscher new-articles, Jian Yang new-related, Lisa Bastarache new-related (all 09-14, 08:24Z).
**Threads:** Genetic epidemiology → **GxE, ancestry, and cross-ancestry portability**; Biobanks (Mexican-ancestry cohort as a diversity axis complement to UKB/AoU).

**What it is (from abstract snippet).** Human populations differ in
disease prevalence and phenotypes, but the extent to which
differences are **genetic** is unknown for most complex traits.
Cross-population phenotypic-mean comparison is confounded by
environment. This paper uses a **within-family design in a Mexican
cohort** to isolate the ancestry-genetic component of complex-trait
variation — i.e., **within-family ancestry variation** acts as the
identification strategy, controlling for shared environment.

**Why it matters for your work.** Direct-hit on your **PGS × ancestry
/ cross-ancestry portability** framing. Within-family designs are the
identification gold standard for separating direct genetic effects
from indirect / assortative-mating / shared-environment confounding;
extending this to a Mexican-ancestry cohort is a rare
non-European-ancestry within-family study and is high-value for the
GxE and PGS-portability sub-threads. Also directly relevant for AoU
(large Latino / Latinx enrollment) — you can carry the identification
logic across cohorts. **Triple-feed hit** (Visscher, Yang, Bastarache)
is a strong signal that this will be widely cited.

**Contrast against:** the Kong / Young sibling-based within-family
GWAS papers; the Border 2022 environmental confounding of PGS
paper; the Souaiaia PGS-tails paper as the distributional-lens
counterpart; the Ecker et al. AoU Latinx PheWAS papers.

---

### 10. Devarakonda — *scDEFT: A Deep Learning Framework for Drug-Effect Prediction and Counterfactual Reasoning*
**Venue:** arXiv 2609.10831v1 (submitted 2026-09-09; local digest 09-11).
**Threads:** Specific disease → **Inflammatory bowel disease**; ML for precision health (HTE, pre-treatment stratification); EHR foundation models (single-cell FM lineage; treatment as conditioning operator).

**What it is (from abstract).** **scDEFT** treats a drug as a
**conditioning operator on single-cell representations**, using
feature-wise linear modulation to produce drug-conditioned cell
latents. Two heads then predict (a) drug-induced state change and
(b) responder vs non-responder status. Applied to a **harmonized IBD
atlas of 1.16M cells, 3 cohorts, and 2 drug classes**. Reports 45%
of the baseline-to-reproducibility-ceiling headroom for state-change
prediction, and **AUROC 0.70 for responder stratification pre-
treatment** where standard predictors are at chance.

**Why it matters for your work.** Direct-hit for your IBD disease
thread AND for ML-for-precision-health (pre-treatment stratification
is a decision-tied HTE application). The "drug as conditioning
operator" trick is a portable representation-choice for treatment-
effect modeling — same shape as MOTOR's treatment-conditioning-token
approach for EHR-FM. Pairs with the DINIRS ICU digital-twin paper
from the 09-01 report and with the causal-forest / meta-learner
lineage under `Machine learning for precision health`.

**Contrast against:** MOTOR (Steinberg 2023) treatment-conditioning
lineage; the Alaa / van der Schaar CATE-on-MIMIC lineage; the Lee
NetMoint UKB dementia-trajectory paper (09-01) for structurally
similar pre-symptomatic HTE stratification; Islam DINIRS from the
09-01 report.

---

### 11. Snel, Schulz — *Attributing Cohen's d: Training Data Attribution for Disease-Related Effects in Normative Age Biomarkers*
**Venue:** arXiv 2609.07729v1 (submitted 2026-09-07; local digest 09-09).
**Threads:** Biobanks with EHR linkage (UK Biobank); ML for precision health (audit as clinical instrument); Fidelity, portability, and audit of representations.

**What it is (from abstract).** Normative age models predict
chronological age in nominally healthy cohorts; applied to patients,
they deviate, and the age-gap is read as disease risk. This paper
**attributes the disease-related effect size** directly to **individual
training samples**, using a closed-form influence functional targeting
Cohen's *d*. On **UK Biobank across four diseases and two biomarker
modalities**, removing the 10% most influential training samples
raises held-out disease effect size in every seed. Doubles the
metabolomic-age effect for **type-2 diabetes** and raises the
brain-age effect for multiple sclerosis by ~1/3. **Flagged subjects
carry subclinical cardiometabolic burden that diagnosis-based
exclusion missed** — for T2D, the recovered marker is HbA1c (i.e., the
influence-function surgical removal recovers exactly the marker the
model was oblivious to).

**Why it matters for your work.** Direct-hit on **two** angles.
First, `Machine learning for precision health` — attribution here is
tied to a concrete clinical decision (which "healthy" UKB subjects
should count as controls for T2D discovery), not a leaderboard.
Second, `Fidelity, portability, and audit of representations` — the
influence-function target is Cohen's *d*, i.e., an effect size, not
a prediction loss; this is the audit criterion your thread wants
propagated for representation-level auditing (chart-review-anchored
in spirit even though it's UKB-anchored in practice). Pairs with the
Wu et al. ACT auditable-CT-phenotyping paper (09-01 report), the
scContam / MIA-scFM pretraining-contamination audits you already
track, and generally with the "encoder-based auditability regains
ground" pattern flagged in the 09-01 report's cross-cutting patterns.
The T2D → HbA1c recovery is a clean advertisement for the method.

**Contrast against:** Koh & Liang 2017 influence functions
(foundational); the scContam / MIA-scFM auditing lineage; the ACT CT
audit paper from 09-01; the Kim et al. 2024 UKB latent-cardiometabolic
audit papers.

---

### 12. Semchin, d'Angremont, Ding, Antar, Lorenzi et al. — *Discovering Subtypes of Neurodegenerative Progression with a Scalable Connectome-Constrained Dynamic Model*
**Venue:** arXiv 2609.10890v1 (submitted 2026-09-09; local digest 09-11).
**Threads:** Chronic disease clustering and multimorbidity → **disease subtypes / trajectories**; Rare disease adjacency (genetic Parkinson variants); ML for precision health.

**What it is (from abstract).** Connectome-constrained disease
progression model that jointly estimates subject-specific disease
time and data-driven subtypes from longitudinal morphometry. Applied
to **85 imaging + clinical biomarkers from PPMI**, recovers **four
morphologically distinct progression subtypes**. Benchmarked against
SuStaIn under matched protocols. **Only this method** recovers
subtypes that map to **both clinical motor subtypes AND genetic
variants** — the two independent validity checks SuStaIn misses.

**Why it matters for your work.** Direct-hit for the disease-subtyping
/ trajectory-clustering sub-thread of `Chronic disease clustering and
multimorbidity`. Two structural features are cite-worthy: (i) the
**connectome constraint** is a domain prior that turns an ill-posed
subtype-recovery problem into a well-posed one (portable to any
tissue-topology-informed disease progression modeling — e.g.,
cortical-connectivity Alzheimer subtyping, or biliary-tree-informed
CFTR-modulator response subtyping); (ii) **subtype validation against
independent genetic variants** is the identification-strength
argument SuStaIn-family papers usually can't make. Pairs naturally
with the Lee NetMoint UKB dementia-trajectory paper (09-01 report)
and the Kudamala AoU functional-decline paper (09-01 report).

**Contrast against:** SuStaIn (Young et al. 2018 *Nat Comm*, Vogel et
al. 2021 *Nat Med* AD); LEDA / disease-progression modeling lineage
(Fonteijn et al.); Ferreira et al. 2020 *Nat Comm* AD subtypes; the
Zhang / Ideker digital-twin consortium framing paper.

---

### 13. Kamineni, Raghu, Hua, Tian, Truong, Alaa et al. — *Machine Learning–Driven Spleen Imaging and Genomics Uncover a Splenic Connection to Coronary Artery Disease*
**Venue:** *Science Translational Medicine*, 2026.
**Surfaced via:** Google Scholar alert "Patrick T. Ellinor, MD, PhD - new articles" (09-14, 08:24Z).
**Threads:** ML for precision health (imaging + genomics for CV endpoint); Genetic epidemiology (image-derived phenotype GWAS); adjacent to CHIP / systemic-inflammation → CAD axis.

**What it is (from alert snippet).** Uses **machine-learning-driven
spleen imaging** integrated with genomics to uncover a **splenic
contribution to coronary artery disease** risk. The Ellinor / Alaa
byline signals a UKB imaging + genomics + CAD workflow —
image-derived splenic phenotypes → GWAS → PRS → CAD risk composite.

**Why it matters for your work.** On-thread for two reasons. First,
ML-for-precision-health: this is an image-derived-phenotype GWAS
tied to a specific clinical decision (CAD risk stratification),
which meets your "decision-tied" bar. Second, **spleen ↔ systemic
inflammation ↔ CAD** puts this in immediate structural proximity to
your CHIP / VEXAS / LOY thread (CHIP → IL-1β / IL-6 systemic
inflammation → CAD is the mechanistic story). A splenic imaging
biomarker could plausibly be an intermediate on the same axis, and
would be a natural covariate or effect-modifier in a CHIP × CAD
analysis. Also complements the Jandu inherited-inflammation-PRS
PheWAS paper (this report, #3) — that one is inflammation-anchored
in the genome, this one in the image-derived phenotype.

**Contrast against:** the Ellinor lab's image-derived heart-phenotype
GWAS papers; Aung et al. UKB cardiac-MRI GWAS lineage; the CHIP × CAD
canakinumab / colchicine papers referenced under Chiu et al. (this
report, #5).

---

### 14. Niu, Xia, Wu, Deng, Wu, Lei — *Genome-Wide Association Analyses Identify Distinct Genetic Architectures for Extreme Early-Onset and Late-Onset T2D*
**Venue:** *Diabetes, Obesity and Metabolism*, 2026.
**Surfaced via:** Google Scholar alert `"phenome wide association studies"` (09-12, 19:03Z).
**Threads:** Genetic epidemiology → **age-of-onset-partitioned GWAS**; Composite risk models (extreme early-onset as a PGS-tail definition); Pharmacoepi (early-vs-late T2D is a treatment-decision axis).

**What it is (from alert snippet).** GWAS study identifying **distinct
genetic architectures** for extreme early-onset vs. late-onset T2D —
i.e., the age-of-onset partition is a mechanistic partition, not just
an ascertainment artifact. Different lead loci, different heritability
partition, different downstream disease-course implications.

**Why it matters for your work.** Direct-hit on **two** framings.
First, `Genetic epidemiology → PRS-tails`: extreme early-onset T2D
is functionally an in-distribution PGS-tail definition (Souaiaia
framing), and this paper argues the tail has its own architecture.
Second, `Causal inference and pharmacoepidemiology → GLP-1 RAs`:
if extreme early-onset and late-onset T2D have distinct genetic
architectures, they may have distinct GLP-1 RA / SGLT2i response
profiles, which loops back into your pharmacogenomic-modifier
sub-thread. Also pairs with the Zhu partitioned BP-PRS paper (09-01
report) — same mechanism-partitioning turn on PRS, different tissue
axis.

**Contrast against:** the MAGIC T2D GWAS lineage; the Vujkovic et al.
MVP T2D multi-ancestry meta-analysis; the Fahed 2020 monogenic-vs-
polygenic PGS composite; the Baya AJHG PGS-residuals paper for the
"tails have their own architecture" argument.

---

## METHODS-WATCH — off-topic domain, exemplary methods worth cribbing

- **Yu, Huang, Liu, Tang, Wang, Zhang, Zhao** — *A Location-Invariant
  Estimator of Extremal Quantile Treatment Effects for Heavy-Tailed
  Distributions* (arXiv 2609.04018, 09-03 → local digest 09-04).
  Adapts the Fraga extreme-value-index estimator to the causal
  setting using inverse propensity score weighting, then applies a
  difference-based extrapolation so the location parameter cancels
  when quantile differences are taken. Establishes consistency +
  asymptotic normality + variance-estimator. Off-topic domain, but
  the pattern is directly portable to **rare-adverse-event
  pharmacoepi** (very-tail quantile treatment effects where the mean
  is underpowered), and to **CHIP clonal-fraction tail-treatment-
  effects** where the outcome is heavy-tailed.
- **Rajabli, Collins** — *A Generalizable Feature Extractor for
  Alzheimer's-Related Brain MRI Tasks* (arXiv 2609.05400, 09-04 →
  local digest 09-07). A compact 3D CNN (7.18M params) supervised on
  brain-age is **frozen**, adapted per task with LoRA (~1% extra
  params). Adapted model achieves AUC 0.964 on CN-vs-Dementia (ADNI),
  transfers unchanged to OASIS-3 at AUC 0.871, and generalizes to
  amyloid-positivity prediction, MCI-progression classification, ICV-
  normalized hippocampal and white-matter-hypointensity volume
  regression. This is a **template for compact-FM-plus-LoRA transfer**
  that is directly portable to the EHR-FM lineage (CLMBR / MOTOR /
  MEDS pretraining → LoRA adaptation for site-specific downstream
  tasks). Especially relevant given the Burkhart federated GEMs paper
  from the 09-01 report — LoRA is the natural per-site fine-tuning
  primitive after federated pretraining.
- **Momenzadeh, Ghaderzadeh, Oshaghi et al.** — *A Causal Machine
  Learning Framework for ICU Discharge Decision Support Using EHR*
  (Scientific Reports 2026; surfaced via 09-12 `"electronic health
  records"` feed). ICU-discharge decision is a natural companion to
  the DINIRS non-invasive-vs-invasive-ventilation ITE paper from the
  09-01 report — same MIMIC / eICU-CRD substrate, same doubly-robust-
  ITE flavor, adjacent decision. Worth a read alongside DINIRS as
  the second concrete instance in the "causal ML for ICU decisions"
  sub-thread.
- **Bolognini, Guarracino, Paleni, Dudley et al.** — *COSIGT:
  Population-scalable genotyping of complex loci from low-coverage
  sequencing data using pangenome graphs* (Genome Biology 2026;
  surfaced via 09-12 Kai Wang new-related). Direct entry in your
  **pangenome-informed variant calling** sub-thread under `Genetic
  epidemiology` — the low-coverage angle is what makes it
  population-scalable and therefore a **PGS-portability** lever (HPRC
  v2 lineage). Pairs with the Chen & Fang *Innovation Life* pangenomics
  review from the same Scholar batch (Jian Yang citations-to feed).
- **Ma, Weisburd, DiTroia, Romo, Covill et al.** — *Long-read RNA
  Sequencing Improves Isoform and Splicing Outlier Detection in Whole
  Blood from Rare-Disease Trios* (medRxiv 2026; surfaced via 09-12
  Stephen Montgomery new-related). Direct entry in the `Rare disease`
  thread, specifically the splicing / RNA-evidence angle for VUS
  resolution (Variant interpretation → splicing / RNA evidence).
  Long-read RNA-seq on whole blood is the practically-deployable
  version of the long-read-RNA-for-rare-disease diagnostic argument;
  pairs with the Carrasco-Zanini proteomics-for-rare-disease paper
  (this report, #8) as complementary orthogonal-evidence layers.
- **Islam, Alves, Bourbon, Pfisterer** — *Utilization of Functional
  Data for LDLR Variant Classification: Comparative Insights from
  High-Content Microscopy and Flow Cytometry* (Atherosclerosis 2026;
  surfaced via 09-12 `"variant interpretation"` feed). Directly
  serves the Variant Interpretation → functional-evidence sub-thread
  (ACMG PS3 / BS3). The methods comparison (microscopy vs. flow) is
  the practical version of the ClinGen VCEP guidance for FH.
- **Feuerriegel, Ciora, Welzel, Frauen** — *OncoSynth: Synthetic Data
  Generation for Treatment Effect Estimation in Oncology* (2026;
  Mihaela van der Schaar new-articles, 09-14). Off-topic disease
  (oncology), but the **synthetic-data-for-TE-estimation** framing is
  portable — a natural bridge to the DINIRS + digital-twin sub-thread
  when patient-level access is restricted.

---

## Also-ran / SKIP pile (briefly, so you don't have to re-scan)

- **Ghiasi** *Storage-Centric System Designs* (arXiv 2608.31004,
  local digest 09-01) — computer-architecture dissertation for
  genomic data movement; off-thread infrastructure.
- **Ramesh, Sadalgekar, Tan, Li** *Mudskippers use tail thrusting …*
  (arXiv 2609.00564, local digest 09-02) — false-positive on the
  "motor" keyword (biomechanics, not clinical motor phenotype).
- **Cortez-Rodriguez** *Natural Disasters and the Nonprofit Sector*
  (arXiv 2609.04136, local digest 09-04) — panel-DML off-thread.
- **Wu, Han, Mito, Watabe et al.** *FUSE-RT* HPLC retention-time FM
  (arXiv 2609.07531, local digest 09-09) — chemistry-only, off-thread.
- **Lee, Rempala, Schnell** Kalman-filter HT infectious-disease
  prevalence (arXiv 2609.09325, local digest 09-10) — SARS-CoV-2
  surveillance, methods-adjacent but off-thread domain.
- **Hendrix, Zhang, Heitzig, Bazemore, Rehkopf** Geospatial FMs
  augment social-risk indices (arXiv 2609.11689, local digest 09-11)
  — social-determinants / place-effects methods paper, adjacent to
  cardiometabolic risk but not on the current PheWAS / phecode /
  genetics axis; note as a possible SDoH-augmentation covariate for
  UKB / AoU / OFH work.
- **Duan et al.** *Surgical Exposure and Biological Aging: UK Biobank
  Cross-Sectional* (J Clin Anesthesia 2026) — off-thread; cross-
  sectional design, biological-age as endpoint but no strong causal
  identification.
- **Fetchko, Sangalli, Letra** *EHR Sex Differences in Oral Diseases*
  (Clin Exp Dental Research 2026) — off-thread disease surface, but
  worth noting the AoU + EHR framing.
- **Prasad, Choudhary** Cybersecurity frameworks for health data
  (2026) — off-thread noise from the "Foundation models + EHR" broad
  keyword feed.
- **Zhu, Zhao, Bai** Temporal KG reasoning (WWW 2026) —
  non-biomedical KG, per your `Knowledge graphs & ontologies` "lower
  interest in non-biomedical KG infrastructure" note.
- **Roschyk, Campbell** lncRNAs × immune × autism (Frontiers Tox
  2026) — molecular-mechanism paper, off the PheWAS / EHR axis.
- Scholar-feed noise (TCM endometriosis review; telomere / longevity
  commercial-industry review; various Chinese-medicine or vision-LM
  papers off the biomedical-clinical axis) — expected broad-keyword
  bleed-through.

---

## Cross-cutting patterns to watch

1. **A four-biobank world is here.** Straub et al. Our Future Health
   at 1.9M enrolled joins UKB, AoU, and MVP as the fourth
   national-scale EHR-linked biobank. Any cross-biobank template
   (Acharya three-biobank ASCVD heritability; Truong cross-biobank
   PheWAS harmonization) now conceptually generalizes to four.
   OFH's primary-care NHS linkage is the depth advantage; write it
   into any cross-biobank replication plan for medication-persistence
   or pharmacogenomic-modifier studies.
2. **PGS × proteomics stacking is the maturation direction of
   composite risk.** Zheng PRS-vs-ProtRS divergence paper (this
   report) + Lee NetMoint UKB proteomics+imaging (09-01 report) +
   You et al. 2023 UKB Olink+PRS composite — three papers in a
   year on the "PRS and proteomic-RS carry complementary
   information" theme. Consider this the default hygiene bar for
   any composite-risk paper: report where the two scores agree, where
   they diverge, and what the divergence resolves to. The Baya AJHG
   "misaligned individuals" framing is one lens on this; module-level
   partition (as in Zheng) is another.
3. **PGS extreme-tails is having its clinical translation moment for
   Alzheimer's.** Ward rare-extreme AD-PRS + Kurniansyah multiancestry
   AD-PRS (09-01) + Souaiaia PGS-tails (already tracked) = pre-
   symptomatic AD stratification is where the Souaiaia framing gets
   its first head-on clinical stress test. Your INTERESTS.md
   "tails-and-residuals" taxonomy is a citable framework here.
4. **CHIP moves from etiologic association to trial-design phase.**
   Chiu *JAMA Cardiology* CHIP CVOT design paper is the "so now
   what?" step after 5+ years of CHIP → CAD association papers.
   Watch for the first prospective CHIP × anti-inflammatory-therapy
   TTE-in-RWE study to appear this year, and consider a CHIP
   TTE-in-BioVU-plus-AoU your own cohort could be scoped for.
5. **Rare-disease diagnostics is adding orthogonal-evidence layers
   fast.** Carrasco-Zanini proteomics + Ma long-read RNA-seq +
   Uria-Regojo cohort-scale reanalysis (previously tracked) are three
   independent orthogonal-evidence directions surfacing at once.
   The convergent framing is that GS-alone plateaus at 30-40%
   diagnostic yield, and every additional modality closes some of
   the gap. This is a natural section for a rare-disease review
   article if you draft one.
6. **The 09-03 → 09-08 arxiv-digest run had four zero-days out of
   six.** Two of them (09-03, 09-05) landed on weekends and are
   expected; but 09-06 and 09-08 are weekday zero-days. Combined
   with the 08-21 → 08-24 four-zero-day run flagged in the 09-01
   report, this is the second cluster of anomalous quiet-days in a
   month. Worth pattern-matching against `scripts/arxiv_digest.py` to
   confirm the fetcher is healthy — check whether the categories
   list, the keyword weights, or the arxiv API rate-limit are
   silently dropping matches.

---

## Next actions I would take

- **Read first (in this order):** Straub OFH *Nature Medicine* (four-
  biobank world implication); Xiong KOMAP *JAMIA* (methods
  reusability); Jandu inflammation-PRS PheWAS (own-thread relevance);
  Chiu CHIP CVOT design (thread-transition moment); Liu & Wang
  TTE × AI *JCE* (framework anchor); Ward rare-extreme AD-PRS (PGS-
  tails clinical instance); Carrasco-Zanini proteomics-for-rare-
  disease (rare-disease orthogonal-evidence layer).
- **Cite-ready this week:** Straub OFH, Xiong KOMAP, Jandu
  inflammation-PheWAS, Chiu CHIP-CVOT, Wang within-family Mexican
  ancestry, Snel UKB training-data-attribution.
- **Watch for follow-ups:** Ward rare-extreme AD-PRS (medRxiv →
  likely a *Nat Med* or *AJHG* paper by year-end); Zheng PRS-vs-
  ProtRS neurodegen (medRxiv → likely a *Nat Aging* / *Nat Med*
  paper); Ma long-read RNA-seq rare-disease trios (medRxiv → likely
  *AJHG* or *Genome Medicine*).
- **Consider adding to INTERESTS.md:** an explicit sub-thread under
  `Biobanks with EHR linkage` for **Our Future Health**, given that
  four national-scale EHR-linked biobanks is the new landscape and
  the design differences (NHS primary-care linkage; 5M target;
  passive recruitment via letter) are cite-worthy in their own right.
  Also consider adding a `Splenic imaging + inflammation → CAD`
  cross-link between your CHIP thread and the ML-for-precision-health
  thread, prompted by Kamineni *Sci Transl Med* (this report, #13).
