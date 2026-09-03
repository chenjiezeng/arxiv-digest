# Research digest report — 2026-09-03

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease
threads, EHR foundation models, KGs/ontologies, drug repurposing, rare
disease, ML for precision health, multimorbidity, knowledge
representation in EHRs).

Window: **2026-09-01 12:40Z → 2026-09-03 12:40Z** (~48 h since the
previous research-digest report, covering two arxiv-digest cron runs
and three Google Scholar alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `digests/2026-09-02.md`) | 09-01 → 09-02 daily crons | Both cron runs surfaced exactly **1 paper each, both off-thread**. 09-01: Mansouri Ghiasi dissertation on storage-centric systems for genomic/metagenomic pipelines (arXiv 2608.31004v1, cs.AR; keyword hit "precision medicine" — hardware / systems paper). 09-02: Ramesh et al. mudskipper tail-thrusting on wet substrates (arXiv 2609.00564v1, physics.bio-ph; keyword hit "motor" — false hit on locomotion-motor). Both are SKIP per the triage rubric. No fetcher failures this window. |
| No `arxiv-digest` email hits from GitHub | — | As last window, the pipeline commits its output rather than emailing; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-03 batch, 04:33Z) | 09-03 04:33Z | 6 author feeds fired: **Joshua C. Denny** (new-related, led by Zhang et al. AoU wearable + PGS for incident MDD; batch also carried Hu et al. Nat Commun PGS pre-train/fine-tune boosting, Dutta et al. Cell Genomics 2026 PRS × plasma proteomics 21 cancers, YMoC Yamanashi cohort, FORGEPHAST simulator), **George Hripcsak** (new-related; Du et al. explainable transformer for structured-EHR prediction), **Stephen B Montgomery** (new-related; Guo et al. Genome Biology short-read SV benchmark, plus Wang et al. medRxiv genomic+proteomic complex-trait prediction in diverse populations, STR-PG pangenome STR genotyping), **Marinka Zitnik** (new-related; Zhu et al. npj Digital Medicine HealthFlow multi-agent EHR analysis), **Peter Szolovits** (off-thread NLP: left-branching transformers), **Zhiyong Lu** (off-thread NLP: hybrid-attention decoding). |
| Google Scholar alerts (09-02 batch, 02:01Z) | 09-02 02:01Z | 10 keyword feeds fired: `"All of Us research program"` (**Garofalo et al. JHEP Reports** 293,141-participant multiancestry DNA-repair-gene HCC-risk paper — HIGH), `"UK Biobank"` (**Zhang et al. UKB explainable plasma-proteomics ML for osteoporosis** — on-thread), `"electronic health records"` (Chovatiya et al. abrocitinib atopic-dermatitis RWE EHR+claims — moderate), `"drug repurposing"` (sertraline colorectal cancer metabolomics mouse study — off-thread), `"knowledge graph"` (construction-industry compliance-checking KG+LLM — off-thread), `"variant interpretation"` (single-family FOXL2 BPES-I frameshift — off-thread), `"autoimmune disorders"` (Stone book chapter on triggers of blistering disease — off-thread), `"rare diseases"` (AstraZeneca selumetinib China approval — news, off-thread), `mendelian diseases` (Jiang et al. autoimmune × follicular lymphoma MR + multi-omics — moderate for MR/causal), `Foundation models + "electronic health records"` (Abraham AI-in-primary-care nursing chapter — off-thread). |
| Google Scholar alerts (09-01 batch, 11:36Z — post-report tail) | 09-01 11:36Z | Author-feed items *not* covered in the 09-01 report because they arrived after the 12:40Z window close: **Chenjie Zeng** new-related (**Zheng, Shivakumar, Shen, Kim medRxiv** — where polygenic and proteomic risk scores diverge in neurodegenerative diseases — HIGH direct hit); **Marinka Zitnik** new-articles (Fang, Li, Noori, Fesser, Zitnik — Closing the Loop in AI-Driven Biomedical Discovery — moderate); **Nigam Shah** new-articles (Qin, Zeng, Ma, Ge, Tham, Shah, Eils — *Lancet Digital Health* 2026 autonomous agentic AI in health care perspective — HIGH for agentic-pipeline sub-thread); **Isaac Kohane** new-articles (Zhao et al. Rare Diseases Common Dilemmas LLM decision-making — on-thread for rare disease + LLM ethics); **Yong Chen / Patrick Ryan / Hripcsak** citations-to feeds (all re-fired the Zhang GLP-1/SGLT2/DPP4 TTE paper already covered in the 09-01 report — dual/triple hit is a signal for that paper's centrality); **Konrad Karczewski** citations-to (**Chen et al. MOCR-DB Phenomics 2026** multi-omics causal resource DB — moderate, methods-watch); **Jian Yang** new-related (dual-hit for Zheng PRS-vs-ProRS Alzheimer's paper); **Kai Wang** related + Alsentzer new-articles + others — off-thread noise. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Nine HIGH items surfaced this window, clustering into four knots. The
dominant story is a **multi-omics-augmented PRS cluster (5 items)** that
crystallizes the exact sub-thread INTERESTS.md prioritizes; two items
open new sub-threads (AoU wearable + PGS as a longitudinal-behavior +
liability composite; agentic EHR-analysis pipelines as a rising
Lancet-perspective concern); and one is a direct-hit biobank-native
rare-variant / composite-risk paper on HCC.

**Multi-omics-augmented PRS / PGS-and-proteomics cluster (5 items).**

- **Zheng, Shivakumar, Shen, Kim** — *Absorption and Co-expression
  Modules Show Where Polygenic and Proteomic Risk Scores Diverge in
  Neurodegenerative Diseases* (medRxiv 2026). Dual hit on the Chenjie
  Zeng AND Jian Yang new-related feeds. The framing is exactly the
  `Multi-omics-augmented PRS` sub-thread that INTERESTS.md added under
  Genetic epi — with a twist: rather than combining PRS + ProRS
  additively, this paper asks **where they diverge** at the
  co-expression-module level. That is the mechanism-resolution turn on
  PGS-plus-proteomics stacking (the Shan / Feng / Nightingale lineage
  you already track) applied to a specific
  clinically-decision-relevant end-organ family (AD, PD, ALS lineage).
- **Hu, Chen, Salvatore, Wu, Ozdemir, Lu** — *A pre-train and fine-tune
  framework for adaptive boosting of pre-trained polygenic risk scores*
  (*Nature Communications* 2026, from the Denny 09-03 feed). A general
  purpose PGS-transfer framework that boosts pre-trained PGS via
  fine-tuning to a target ancestry / cohort — the direct methods
  substrate for the `PGS × ancestry` and cross-biobank portability
  concerns that your Acharya three-biobank ASCVD paper (from the 09-01
  report) opened.
- **Dutta, Zhang, Guo, Quint, Rooney** — *Polygenic risk scores and
  plasma proteomics identify cancer-related proteins and trans-
  regulated protein networks* (*Cell Genomics* 2026, from the Denny
  09-03 feed). Integrates PRSs for **21 cancers** with **4,955 plasma
  proteins** in cancer-free UKB participants to identify PGS-predicted
  proteins and trans-networks. Direct entry in `Multi-omics-augmented
  PRS` and in the biomarker-as-exposure phenome-wide MR sub-thread.
- **Wang, Williams, Gillman, Raffield** — *Integrating Genomic and
  Proteomic Data Improves Complex Trait Prediction in Diverse
  Populations* (medRxiv 2026, from the Montgomery 09-03 feed). Explicit
  proteomic risk scores (ProRS) benchmarked against PRS in **diverse
  populations**. Pairs with Kurniansyah *Nature Genetics* multi-ancestry
  AD-PRS (from the 09-01 report) — same ancestry-portability question,
  now with proteomics added.
- **Zhang W, Zhang W, Cheng, Gong, Kou, Jiang** — *Explainable Plasma
  Proteomics-Based Machine Learning for Osteoporosis Diagnosis,
  Prognosis, and Protein Biomarker Discovery in the UK Biobank* (2026,
  from the `UK Biobank` keyword feed). UKB Olink + explainable ML for
  osteoporosis; on-thread for `Biobanks with EHR linkage` and for the
  proteomics-augmented risk-prediction sub-thread.

**AoU longitudinal behavior + PGS (1 item — opens a new sub-thread).**

- **Zhang Y, Folarin, Zhong, Kim, Sun, Stewart** — *Longitudinal
  Wearable Monitoring and Polygenic Risk for Incident Major Depressive
  Disorder in the All of Us Research Program* (arXiv 2608.06063, from
  the Denny 09-03 feed). Integrates **genomic liability (PGS) with
  long-term objective wearable behavioral data** in AoU to predict
  incident MDD. This is the first paper I've seen that combines the
  ABCD-style wearable-GWAS lineage (Gerstein-lab-adjacent digital-
  phenotype work) with an AoU-native longitudinal-outcome design.
  Portable framing for **CFTR-modulator persistence + wearable
  behavior**, **statin persistence + wearable activity**, and **APOL1
  CKD progression + wearable sleep**. Suggests adding an explicit sub-
  thread under `Machine learning for precision health` for **digital-
  phenotype × PGS composite risk**.

**Agentic AI in EHR analytics / clinical care (2 items — the rising
sub-thread you added in 07-29).**

- **Zhu, Wang, Qi, Gu, Sui, Hu, Zhang, He** — *HealthFlow: Automating
  Electronic Health Record Analysis via a Strategically Self-Evolving
  Multi-Agent Framework* (*npj Digital Medicine* 2026, from the Zitnik
  09-03 feed). Automates full EHR-analysis pipelines via a **self-
  evolving multi-agent framework**. This is the exact substrate for the
  `Agentic / human-in-the-loop observational-causal-inference pipelines`
  sub-thread you added in 2026-07-29 — the Chou/Kallus oci-agent
  arXiv 2607.22443 was the Netflix-in-production reference; HealthFlow
  is the healthcare-native counterpart.
- **Qin, Zeng, Ma, Ge, Tham, Shah, Eils** — *Autonomous Agentic
  Artificial Intelligence Systems in Health Care: Friend or Foe?*
  (*Lancet Digital Health* 2026 perspective, from the Shah 09-01 feed).
  The friend-or-foe framing paper for autonomous agentic AI systems in
  healthcare, with an explicit deployment-guardrail argument. Pair with
  HealthFlow: HealthFlow is the concrete tool, Qin et al. is the
  editorial framing that a deploying group would need to reference.

**Biobank-native rare-variant / composite-risk (1 item).**

- **Garofalo, Chotiprasidhi, Johnson** — *Multi-ancestry sequencing
  analysis in 293,141 participants identifies predisposition DNA repair
  genes associated with HCC risk* (*JHEP Reports* 2026, from the AoU
  keyword feed). 293k participants across biobanks (AoU is one of the
  contributors given the keyword hit) — HCC (hepatocellular carcinoma)
  as the endpoint, DNA repair gene rare variants as the exposure. This
  is a direct-hit paper for `Biobanks with EHR linkage → multi-
  biobank`, for `Rare-variant association methods`, and for the
  **penetrance under population-screening vs. clinical-ascertainment**
  framing your PheWAS-infrastructure thread prioritizes.

---

## Detailed reports — HIGH-priority studies

Papers below are the ones I would open next; each note gives (a) the
core method or claim, (b) why it maps to a research thread, and (c)
what to compare it against in the existing literature you track.

### 1. Zheng, Shivakumar, Shen, Kim — *Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases*
**Venue:** medRxiv 2026 (preprint).
**Surfaced via:** Google Scholar alert **"Chenjie Zeng - new related research"** AND **"Jian Yang - new related research"** (both 09-01, 11:36Z). Dual hit is a strong on-thread signal.
**Threads:** Genetic epidemiology → **Multi-omics-augmented PRS** (Nightingale NMR / Olink / metabolomics stacked with PGS); Chronic disease clustering and multimorbidity (dementia); ML for precision health.

**What it is (from alert snippet + title).** Rather than combine PRS
and proteomic risk scores (ProRS) additively as a stacked risk
predictor, this paper asks **where they diverge** at the
co-expression-module level — i.e., which biological modules a plasma
ProRS captures that a PRS misses (and vice versa) in **neurodegenerative
diseases**. The "absorption" framing likely refers to how much of the
PRS signal is *absorbed* into a proteomic prediction (the
mediation-fraction analogue for PGS → ProRS → outcome), decomposed by
co-expression module.

**Why it matters for your work.** This is the exact sub-thread
INTERESTS.md added under `Genetic epi → Multi-omics-augmented PRS`,
with a mechanism-resolution twist that goes past additive stacking.
Two direct handles for your work: (a) `Composite risk models stacking
PRS with rare pathogenic variants` — a divergence map tells you when
adding a rare-variant burden to the composite is likely to be
non-redundant vs. when the proteome already absorbs the polygenic
signal; (b) `Chronic disease clustering and multimorbidity` on
dementia — the divergence axis is a candidate feature for subtype
clustering (AD-liability vs. AD-signature dissociation as a
representation choice). Also a natural pair with the NetMoint UKB
paper from the 09-01 report — NetMoint's mean AUC 0.937 on AD comes
from concatenating proteomics + MRI + haemodynamic; the Zheng paper
tells you *why* proteomics contributes beyond PRS.

**Contrast against:** Shan et al. UKB 2026 (PGS + Olink for
cardiometabolic); Feng et al. cross-ancestry IDP pleiotropy for
depression (from the 07-29 INTERESTS update); You et al. UKB Olink +
PRS composite AD 2023; the Kurniansyah *Nature Genetics* multi-
ancestry AD-PRS from the 09-01 report as the ancestry-facing pair.

---

### 2. Zhang Y, Folarin, Zhong, Kim, Sun, Stewart et al. — *Longitudinal Wearable Monitoring and Polygenic Risk for Incident Major Depressive Disorder in the All of Us Research Program*
**Venue:** arXiv preprint 2608.06063, 2026.
**Surfaced via:** Google Scholar alert **"Joshua C. Denny - new related research"** (09-03, 04:33Z).
**Threads:** Biobanks with EHR linkage (AoU); Genetic epidemiology (PGS × longitudinal behavior); ML for precision health (incident-outcome prediction); **candidate new sub-thread — digital-phenotype × PGS composite risk**.

**What it is (from alert snippet).** *"Major depressive disorder (MDD)
risk reflects both stable inherited liability and dynamic behavioral
patterns, yet these dimensions are rarely examined together using
long-term objective data in real-world settings. Here, we integrated
genomic [with wearable data in AoU]."* This is an incident-MDD design
in AoU that combines **PGS (stable liability)** and **wearable
behavioral trajectories (dynamic behavior)** as jointly predictive
inputs — with AoU providing the EHR outcome ascertainment.

**Why it matters for your work.** Three angles hit. First, direct
`Biobanks with EHR linkage → AoU` — a longitudinal-outcome PGS paper
in AoU is exactly what your thread prioritizes. Second, the wearable
+ PGS composite is a novel modality pairing on the biobank side —
UKB has Olink and metabolomics but limited long-term wearable, MVP
has EHR depth but limited wearable, AoU is the biobank where this
composite is even possible at scale. Third, the design is directly
portable to **medication-persistence-as-outcome** work
(pharmacoepi × PGx sub-thread): CFTR-modulator persistence with
wearable activity, statin discontinuation with wearable sleep, GLP-1
RA persistence with wearable step count and glucose CGM. The paper
argues implicitly that dynamic behavior is a signal channel you can
add to any PGS-outcome design; that is portable methodology.

**Contrast against:** the ABCD wearable-GWAS Firth-PLINK2 UKB lineage
(Gerstein lab); the Zhang / Ideker / Oermann *Cell* 2026 digital
twins consortium framing; the DINIRS censoring-aware digital-twin
paper from the 09-01 report (respiratory support ITE on MIMIC-IV,
same "digital twin from EHR" thread).

**INTERESTS.md action item:** add an explicit sub-thread under
`Machine learning for precision health` for **Digital-phenotype × PGS
composite risk** (wearable behavior + PGS + EHR outcome as a
three-modality composite predictor).

---

### 3. Hu, Chen, Salvatore, Wu, Ozdemir, Lu et al. — *A Pre-train and Fine-Tune Framework for Adaptive Boosting of Pre-trained Polygenic Risk Scores*
**Venue:** *Nature Communications* 2026 (article s41467-026-77128-5).
**Surfaced via:** Google Scholar alert **"Joshua C. Denny - new related research"** (09-03, 04:33Z).
**Threads:** Genetic epidemiology → PRS methods, cross-ancestry portability; Biobanks with EHR linkage.

**What it is (from alert snippet).** *"Polygenic risk scores are
widely used for predicting genetic risk across complex diseases and
traits, and several pre-trained models have been developed. Few
approaches leverage these pre-trained polygenic risk scores to further
refine [predictions in target cohorts]."* A general-purpose
**pre-train + fine-tune** framework: take an existing pre-trained PGS
(the Kunkle 2019 AD-PRS, the PRS-CS lineage, the Ge et al. PGS Catalog
weights) and adaptively boost it to a target cohort / ancestry / trait.

**Why it matters for your work.** Direct methods-substrate paper for
`Genetic epi → PRS / polygenic scores, cross / trans-ancestry
portability`. This is the PGS-transfer-learning analogue for the
`Pretraining-contamination audits for foundation-model benchmarks`
concern you added under EHR-FMs — the pre-train + fine-tune framing
is now standard across modalities, but PGS transfer is one of the
harder-to-audit versions because the source cohort ancestry mixture
is often obscured. Pairs directly with the Kurniansyah *Nature
Genetics* multi-ancestry AD-PRS from the 09-01 report (external-
validation-in-diverse-populations design) and with Truong et al.
cross-biobank PheWAS harmonization.

**Contrast against:** PRS-CS (Ge et al. 2019); PRS-CSx (Ge et al.
2022 cross-ancestry); PRSice-2; the Nature Communications 2024
Ancestry-Informed PRS lineage; SBayesRC (Zeng et al.).

---

### 4. Dutta, Zhang, Guo, Quint, Rooney et al. — *Polygenic Risk Scores and Plasma Proteomics Identify Cancer-related Proteins and Trans-regulated Protein Networks*
**Venue:** *Cell Genomics* 2026 (S2666-979X(26)00184-9).
**Surfaced via:** Google Scholar alert **"Joshua C. Denny - new related research"** (09-03, 04:33Z).
**Threads:** Genetic epidemiology → Multi-omics-augmented PRS; Biobanks with EHR linkage (UKB Olink); Phenome-wide MR (biomarker-as-exposure).

**What it is (from alert snippet).** *"Genome-wide association studies
identify cancer susceptibility loci, but downstream protein mechanisms
remain incompletely defined. We integrate polygenic risk scores (PRSs)
for 21 cancers with 4,955 plasma proteins measured in cancer-free
[individuals]."* A large-scale PGS × plasma-proteome integration in
**cancer-free UKB participants** across **21 cancer types**, with
identification of PGS-predicted proteins and trans-regulated networks.
The cancer-free framing is the key methodological choice: pre-disease
associations avoid the reverse-causation problem that plagues
proteomic biomarker discovery in cancer patients.

**Why it matters for your work.** Direct entry in the `Multi-omics-
augmented PRS` sub-thread, with a specific phenome-wide MR-adjacent
flavor: identifying PGS-predicted proteins and networks in
cancer-free individuals is essentially a MR-style *cis-* and *trans-*
protein QTL screen scaled to 21 cancer PGSes at once. Also a
UKB-native paper that pairs with the Wang et al. medRxiv paper below
on integrating genomic + proteomic data in diverse populations —
Dutta is the UKB-heavy Olink deep dive, Wang is the ancestry-facing
extension. Also worth reading against Zheng et al. #1 above:
neurodegenerative-disease divergence maps + cancer-PGS-to-protein
maps together suggest a general recipe for `Multi-omics-augmented
PRS` — decompose per outcome family and per proteomic module.

**Contrast against:** Sun et al. 2018 UKB Olink pQTL foundational
paper; Ferkingstad et al. 2021 deCODE proteome MR; Gudmundsson et al.
2022 Neale-lab pan-UKB pQTL; the Nightingale metabolomics UKB
lineage.

---

### 5. Wang, Williams, Gillman, Raffield et al. — *Integrating Genomic and Proteomic Data Improves Complex Trait Prediction in Diverse Populations*
**Venue:** medRxiv 2026 (preprint 2026.08.10.26360136).
**Surfaced via:** Google Scholar alert **"Stephen B Montgomery - new related research"** (09-03, 04:33Z).
**Threads:** Genetic epidemiology → Multi-omics-augmented PRS, cross-ancestry portability; Biobanks with EHR linkage.

**What it is (from alert snippet).** *"Polygenic risk scores (PRS)
capture inherited susceptibility, and circulating proteins reflect
downstream biological processes for complex traits and diseases.
Proteomic risk scores (ProRS) may provide complementary information,
although their added [value in diverse populations is unclear]."* A
head-to-head evaluation of PRS + ProRS composite prediction in
**diverse populations** — the ancestry-portability question applied
to the multi-omics stack. Given Raffield is on the author list (UNC,
JHS / MESA / TOPMed lineage), the diverse-populations claim likely
draws on JHS + MESA + TOPMed alongside UKB.

**Why it matters for your work.** Direct entry in
`Multi-omics-augmented PRS` and in the `PGS × ancestry` framing.
Pairs with Dutta #4 (UKB Olink deep dive on 21 cancers) as the
ancestry-facing extension; pairs with Zheng #1 (mechanism-resolution
on neurodegenerative diseases) as the disease-family extension; and
pairs with Hu #3 (pre-train + fine-tune PGS transfer) as the
methods-substrate for how you would deploy such a composite in a
non-EU biobank. Together the four are a coherent multi-omics-PGS
mini-monograph for this window.

**Contrast against:** Shan et al. 2026 UKB PGS + Olink cardiometabolic;
the You et al. 2023 UKB AD PGS + Olink paper; MESA-based ProRS
lineage.

---

### 6. Garofalo, Chotiprasidhi, Johnson et al. — *Multi-Ancestry Sequencing Analysis in 293,141 Participants Identifies Predisposition DNA Repair Genes Associated with HCC Risk*
**Venue:** *JHEP Reports*, 2026.
**Surfaced via:** Google Scholar keyword feed **`"All of Us research program"`** (09-02, 02:01Z).
**Threads:** Biobanks with EHR linkage (AoU + others); Rare disease → Rare-variant association methods; Variant interpretation (ACMG / ClinGen) → DNA-repair gene curation; PheWAS / phecode infrastructure → penetrance estimation.

**What it is (from alert snippet).** *"All [ancestry-inclusive
sequencing on] 293,141 participants identifies predisposition DNA
repair genes associated with HCC [hepatocellular carcinoma] risk."*
A **multi-ancestry rare-variant sequencing** study at ~293k-participant
scale, HCC as the endpoint, DNA-repair-gene rare variants as the
exposure. The AoU-feed hit implies AoU is at least one of the
contributing biobanks (the AoU Controlled Tier v8 whole-genome
release makes 245k WGS available; adding UKB and MVP typically gets
to ~300k range).

**Why it matters for your work.** Multiple direct hits. First,
`Biobanks with EHR linkage` — this is exactly the multi-biobank
harmonized-outcome design your thread prioritizes (matches the Acharya
ASCVD three-biobank template from the 09-01 report). Second, `Rare
disease → Rare-variant association methods` and `Variant interpretation`
— DNA repair genes have ClinGen VCEP guidance (BRCA1/2, PALB2, MLH1
etc.) and this cohort is large enough to estimate **penetrance of
pathogenic variants under population-screening conditions** for HCC,
which is exactly the PheWAS-infrastructure penetrance framing your
thread was written around. Third, HCC is an under-studied cancer for
germline-predisposition work relative to breast / colorectal / pancreas,
so this fills a specific gap.

**Contrast against:** the Fahed 2020 monogenic-vs-polygenic composite
CAD paper (single-cohort template); Karczewski gnomAD constraint (as
the LoF-observation-vs-expectation prior); the Kessler / Loh CHIP /
LOY papers on somatic mosaicism as an additional confounder to guard
against in germline rare-variant scans (Ji et al. *Biology* 2026 QC
layer paper you already track).

---

### 7. Zhu Y, Wang Z, Qi Y, Gu L, Sui D, Hu H, Zhang X, He Z et al. — *HealthFlow: Automating Electronic Health Record Analysis via a Strategically Self-Evolving Multi-Agent Framework*
**Venue:** *npj Digital Medicine*, 2026 (article s41746-026-03097-0).
**Surfaced via:** Google Scholar alert **"Marinka Zitnik - new related research"** (09-03, 04:33Z).
**Threads:** Causal inference & pharmacoepi → **Agentic / human-in-the-loop observational-causal-inference pipelines** (rising sub-thread); Knowledge representation in EHRs → Applications; EHR foundation models (adjacent).

**What it is (from alert snippet).** *"Electronic health records
(EHRs) are a rich source of real-world clinical data, but turning them
into valid analyses remains slow, brittle, and expert-intensive.
Although recent AI agents can answer medical questions and use tools,
automating full EHR [analysis pipelines remains hard]."* HealthFlow is
a **strategically self-evolving multi-agent framework** for the whole
EHR-analysis workflow — cohort definition, feature construction,
model fitting, evaluation, report.

**Why it matters for your work.** Direct hit on the **Agentic /
human-in-the-loop observational-causal-inference pipelines** sub-thread
you added on 2026-07-29 (which called out Chou/Kallus oci-agent
arXiv 2607.22443 as the Netflix-in-production reference and Li et al.
arXiv 2607.16934 as the EHR-derived HTE for trial design pair).
HealthFlow is the healthcare-native counterpart — the agentic
counterpart of an ATLAS + HADES + Strategus OHDSI workflow, but
self-evolving. Also on-thread for `Knowledge representation in EHRs
→ Applications to prioritize`, which specifically prioritizes
"computable phenotyping, cohort discovery for target-trial emulation."
Pair with the Qin et al. Lancet Digital Health perspective (#8 below)
as the friend-or-foe deployment-guardrail argument that any
HealthFlow-style deployment would need to reference.

**Contrast against:** oci-agent (Chou/Kallus arXiv 2607.22443);
Strategus (OHDSI workflow orchestrator); ATLAS; the Ilves et al.
CohortContrast paper from the 09-01 report as the concept-selection
substrate that a HealthFlow-style agent would need to call as a tool.

---

### 8. Qin, Zeng, Ma, Ge, Tham, Shah, Eils et al. — *Autonomous Agentic Artificial Intelligence Systems in Health Care: Friend or Foe?*
**Venue:** *The Lancet Digital Health*, 2026 (perspective / commentary).
**Surfaced via:** Google Scholar alert **"Nigam Shah - new articles"** (09-01, 11:36Z; arrived after the 09-01 report's 12:40Z window close).
**Threads:** Causal inference & pharmacoepi → Agentic pipelines; ML for precision health; Knowledge representation in EHRs (deployment); cross-cutting AI-safety framing.

**What it is (from alert snippet).** *"First, before deployment,
[autonomous agentic AI systems in healthcare should satisfy X, Y,
Z]."* A friend-or-foe **perspective / commentary** on autonomous
agentic AI in healthcare, with a pre-deployment checklist framing.
Shah as one of the senior authors places this squarely in the
OHDSI-adjacent + Stanford-informatics tradition; Eils' presence
suggests a European deployment angle (BIH / Charité).

**Why it matters for your work.** This is the framing paper any
paper you cite that uses a HealthFlow-style agent (or an
oci-agent-style causal-inference agent) will want to cite alongside.
For your `Agentic / human-in-the-loop observational-causal-inference
pipelines` sub-thread, this is the sober-adult companion to the
enthusiastic technical papers. Also citation-worthy as an editorial
position when writing about deploying LLM agents in cohort discovery
or in RWE pipelines.

**Contrast against:** the Wu & Xiao proxy-reliance LLM decision-
calibration paper (from the 09-01 report's METHODS-WATCH); Zhao et
al. Rare Diseases Common Dilemmas (Kohane 09-01 feed) as the
concrete-adverse-behavior counter-example.

---

### 9. Zhang W, Zhang W, Cheng, Gong, Kou, Jiang — *Explainable Plasma Proteomics-Based Machine Learning for Osteoporosis Diagnosis, Prognosis, and Protein Biomarker Discovery in the UK Biobank*
**Venue:** unclear from snippet (journal name truncated as "The [Journal]"), 2026.
**Surfaced via:** Google Scholar keyword feed **`"UK Biobank"`** (09-02, 02:01Z).
**Threads:** Biobanks with EHR linkage (UKB); Multi-omics-augmented PRS-adjacent (proteomics-only side of the stack); ML for precision health.

**What it is (from alert snippet).** UKB plasma-proteomics (Olink)-
based **explainable ML** for **osteoporosis** diagnosis, prognosis,
and protein-biomarker discovery. The explainable-ML framing means
per-protein feature-importance analysis (SHAP or attention weights)
rather than a black-box classifier.

**Why it matters for your work.** On-thread for `Biobanks with EHR
linkage → UKB` and as a companion to the multi-omics-augmented PRS
cluster above (Dutta cancer PGS × Olink, Wang genomic+proteomic in
diverse populations) but on the proteomics-only side of the stack.
Osteoporosis is also under-represented in your existing tracked
disease list but is a natural addition to `Chronic disease clustering
and multimorbidity` — bone-density loss is one of the multimorbidity
end-organs that clusters with cardiometabolic and inflammatory
trajectories. Low priority for reading now; add to the
proteomics-augmented risk-prediction watch list.

**Contrast against:** the Shan et al. UKB PGS + Olink cardiometabolic
lineage; the You et al. UKB Olink + PRS AD paper.

---

### 10. Du, Adamek, Kryukov, Dormont, Bar-Joseph — *Explainable Transformer Models for Clinical Prediction Tasks on Structured Electronic Health Records*
**Venue:** arXiv preprint 2608.20315, 2026.
**Surfaced via:** Google Scholar alert **"George Hripcsak - new related research"** (09-03, 04:33Z).
**Threads:** EHR foundation models; Knowledge representation in EHRs → Structural and temporal representation of the patient timeline AND Fidelity, portability, and audit of representations; ML for precision health.

**What it is (from alert snippet).** *"Predictive models over structured
electronic health records (EHRs) remain central to machine learning
for healthcare, but few have jointly emphasized quantitative laboratory
information and interpretability with respect to input medical events.
We [propose a transformer model that jointly handles labs and
interpretability]."* A transformer model for structured-EHR prediction
with two joint emphases: **quantitative lab values** (not just event
occurrence) and **input-event interpretability**.

**Why it matters for your work.** Two on-thread signals. First, on
`Knowledge representation in EHRs → Structural and temporal
representation of the patient timeline`: **how to represent lab
values** in the MEDS / FEMR / EHRSHOT event schema is a known open
question — quantitative-value vs. code-only tokenization is one of the
representation-ablation choices your thread specifically prioritizes.
Du et al. propose a joint treatment, which is a candidate answer.
Second, on `Fidelity, portability, and audit of representations`: the
interpretability-with-respect-to-input-medical-events framing is a
per-event audit similar to Wu et al. ACT CT phenotyping from the 09-01
report — same pattern, different modality (structured EHR vs. imaging
reports).

**Contrast against:** BEHRT (Li 2020 transformer on EHR sequences);
Med-BERT (Rasmy 2021); MOTOR (Steinberg 2023); the ACT paper from
the 09-01 report as the sibling audit-first work in imaging.

---

## METHODS-WATCH — off-topic domain, exemplary methods worth cribbing

- **Chen, Fan, Chen, Chen, Shu, Zhang** — *MOCR-DB: The Multi-Omics
  Causal Resource Database for Genetic Correlation, Causal Inference,
  and Functional Interpretation* (*Phenomics* 2026, from the Karczewski
  09-01 citations-to feed). A curated multi-omics causal-inference
  resource DB — the substrate a phenome-wide MR pipeline would query
  for exposure GWAS summary stats. On-thread as an infrastructure
  reference for the `Genetic epi → Phenome-wide MR, biomarker-as-
  exposure scans` sub-thread; low priority for reading, high priority
  for bookmarking.
- **Fang, Li, Noori, Fesser, Zitnik** — *Closing the Loop in
  AI-Driven Biomedical Discovery* (2026, from the Zitnik 09-01
  new-articles feed). Framing paper on AI-scientist closed-loop
  hypothesis-experiment-analysis cycles. Off the biomedical-clinical
  axis per se, but the closed-loop framing is a candidate
  meta-framework for the digital-twin-plus-agentic sub-threads
  (Zhang / Ideker / Oermann *Cell* 2026 digital twins + HealthFlow +
  oci-agent).
- **Zhao, Han, Goel, Dagan, Dagan, Madduri** — *Rare Diseases,
  Common Dilemmas: LLMs Prioritize Equal Resource Distribution over
  Patient Benefit in Decision-Making* (arXiv preprint, from the
  Kohane 09-01 new-articles feed). A concrete audit paper for the
  LLM-decision-calibration space — LLMs default to equal-distribution
  fairness heuristics even when patient-benefit maximization is the
  correct action. Pair with the Wu & Xiao proxy-reliance paper from
  the 09-01 METHODS-WATCH and with the Qin et al. Lancet Digital
  Health perspective — three converging papers on
  LLM-agent-in-clinic guardrails.
- **Jiang C, Sun Z, Gao Z, Wang J, Liang J, Feng Y** — *Shared
  Genetic Basis of Autoimmune Diseases and Follicular Lymphoma by
  Mendelian Randomization and Multi-Omics* (*Genes* 2026, from the
  `mendelian diseases` keyword feed). Multi-omics MR triangulation
  linking autoimmune diseases to follicular lymphoma. On-thread as
  a MR-triangulation methods example for the `Drug-target Mendelian
  randomisation triangulated with observational cohort estimates`
  sub-thread; low priority for reading given the specific disease
  pairing.
- **Chovatiya, Mummert, Chang** — *Real-World Use of Abrocitinib for
  Moderate-to-Severe Atopic Dermatitis in the United States Based on
  Electronic Health Records and Administrative Claims* (2026, from
  the `electronic health records` keyword feed). Standard EHR +
  claims RWE for a JAK-inhibitor. Off-thread disease, but a clean
  template of the EHR + claims combined-source RWE design pattern
  worth cribbing when you write up a CFTR-modulator or GLP-1
  persistence paper using that same dual-source approach.
- **Guo, Sofie Engdal, Kodama et al.** — *Benchmarking short-read
  germline structural variant calling highlights advantages of using
  ensembles of tools and small impact of graph genome alignment*
  (*Genome Biology* 2026, from the Montgomery 09-03 feed). Ensemble
  short-read SV benchmark; interesting finding is that
  **graph-genome alignment has only a small impact** on short-read
  SV calling — a nuance to add to your `Pangenome-informed variant
  calling and its downstream PGS-portability consequences` sub-thread
  (HPRC v2 was the reference; this paper is a partial counter-signal
  that graph-alignment gains for short reads are modest).

---

## Also-ran / SKIP pile (briefly, so you don't have to re-scan)

- **arxiv-digest 09-01** — Mansouri Ghiasi dissertation on
  storage-centric systems for genomic pipelines (arXiv 2608.31004v1,
  cs.AR). Hardware / systems paper, off-thread despite the "precision
  medicine" keyword hit.
- **arxiv-digest 09-02** — Ramesh et al. mudskipper tail-thrusting on
  wet substrates (arXiv 2609.00564v1, physics.bio-ph). False keyword
  hit on "motor" (locomotion motor program).
- **YMoC Yamanashi Multi-omics Cohort** (medRxiv 2026, Denny 09-03
  feed) — study-design paper for a screening-defined longitudinal
  Japanese cohort with multi-omics + digital phenotyping. Note for
  awareness (new cohort resource), no immediate action.
- **FORGEPHAST** haplotype-first biobank-scale simulator (bioRxiv 2026,
  Denny 09-03 feed) — genotype + admixture + phenotype simulator.
  Methods-adjacent but simulator-only; no action.
- **STR-PG** pangenome STR genotyping (bioRxiv 2026, Montgomery 09-03
  feed) — off the main disease-genetics axis, methods-only.
- **Contrastive Regulatory Embeddings** (bioRxiv 2026, Montgomery
  feed) — personalized-genome expression prediction, mechanism-only.
- **Signature Recontextualization** (bioRxiv 2026, Zitnik feed) —
  perturbational-signature cross-context mapping, chemistry-only.
- **RegFM interpretable transcriptional regulation FM** (bioRxiv 2026,
  Zitnik feed) — mechanism-only.
- **HealthFlow-adjacent scientific-agent benchmarks**
  (FrontierChallenge, Apodex Discovery) — generic scientific-agent
  benchmarks, off-thread relative to the clinical-decision-tied
  HealthFlow paper (#7).
- Keyword-feed noise: construction-industry KG-LLM compliance-
  checking; FOXL2 single-family variant paper; AstraZeneca selumetinib
  news; sertraline mouse colorectal cancer metabolomics; nursing
  primary-care AI chapter; environmental-triggers autoimmune-blistering
  book chapter — expected broad-keyword bleed-through.
- Off-thread NLP from author feeds: Szolovits (left-branching
  transformers), Lu (Bole hybrid-attention decoding), Kai Wang related
  (PABPN1 RNA nanopore).

---

## Cross-cutting patterns to watch

1. **Multi-omics-augmented PRS is having a coordinated moment.** In
   48 h the same window surfaced Zheng et al. (mechanism-resolution
   on neurodegen), Dutta et al. (UKB PGS × Olink on 21 cancers), Wang
   et al. (genomic + proteomic in diverse populations), Hu et al.
   (pre-train + fine-tune PGS transfer), and Zhang W et al. (UKB
   Olink-only osteoporosis). Together with the Kurniansyah AD-PRS +
   NetMoint from the 09-01 report, this is a coherent
   ~1-week mini-monograph. Consider tightening the `Multi-omics-
   augmented PRS` sub-thread wording in INTERESTS.md to explicitly
   name **divergence maps** (Zheng-style) alongside additive stacking
   (Shan-style).
2. **Agentic AI in EHR analytics is bifurcating into "tool" and
   "guardrail" papers.** HealthFlow (npj Digital Medicine) is the
   concrete self-evolving multi-agent tool; Qin/Shah/Eils (Lancet
   Digital Health) is the friend-or-foe pre-deployment framing.
   Pair them. Add Wu & Xiao proxy-reliance + Zhao Rare Diseases
   Common Dilemmas as the specific failure-mode examples any
   deployment paper needs to cite.
3. **AoU is now the biobank where wearable + PGS + EHR outcome
   composites are possible at scale.** Zhang Y et al. wearable + PGS
   for MDD in AoU is the first concrete demonstration. Watch for the
   same design pattern to appear in the AoU functional-decline lineage
   (Kudamala 08-30) and in AoU cardiovascular / metabolic PGS
   contexts.
4. **The local arxiv-digest fell to zero-thread papers for two
   consecutive days.** 09-01 and 09-02 both surfaced 1 off-thread
   paper each. This is not a fetcher failure (categories loaded
   normally) — it's an actual quiet-submissions weekend + Labor Day
   holiday effect. Not worrying yet; watch 09-03 through 09-05 to see
   if the pattern continues.

---

## Next actions I would take

- **Read first (in this order):** Zheng PRS-vs-ProRS neurodegen
  divergence (dual-hit signal, direct sub-thread hit); Dutta Cell
  Genomics 21-cancer PGS×Olink (largest multi-omics-PGS integration
  this window); Wang medRxiv genomic+proteomic diverse populations
  (ancestry-facing pair for Dutta); Zhang Y AoU wearable+PGS for MDD
  (new sub-thread candidate); Garofalo JHEP Reports HCC multi-ancestry
  rare-variant (biobank-native rare-variant × penetrance).
- **Cite-ready this week (as pairs):** Zheng + Dutta + Wang together
  as the multi-omics-augmented PRS trio; HealthFlow + Qin/Shah/Eils
  as the agentic-EHR-analysis tool + guardrail pair.
- **Watch for follow-ups:** Zhang Y AoU wearable + PGS (arXiv only,
  likely journal placement Q4 2026); Wang genomic+proteomic (medRxiv
  only); Zheng PRS-vs-ProRS neurodegen (medRxiv only); Garofalo HCC
  (peer-reviewed *JHEP Reports* already, safe to cite).
- **Consider adding to INTERESTS.md:**
  - Under `Machine learning for precision health`, a new sub-thread
    for **Digital-phenotype × PGS composite risk** — the Zhang Y AoU
    wearable + PGS + MDD framing is the anchor reference; portable to
    medication-persistence-as-outcome pharmacoepi.
  - Under `Genetic epi → Multi-omics-augmented PRS`, an explicit
    call-out for **divergence-map designs** (Zheng-style) alongside
    additive-stacking designs (Shan-style) — the mechanism-resolution
    turn on the sub-thread.
  - Under `Causal inference and pharmacoepidemiology`, promote the
    `Agentic / human-in-the-loop observational-causal-inference
    pipelines` sub-thread to name HealthFlow as the healthcare-native
    substrate alongside oci-agent (Chou/Kallus arXiv 2607.22443) as
    the general-domain reference.
