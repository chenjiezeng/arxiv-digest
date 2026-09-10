# Research digest report — 2026-09-10

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease
threads, EHR foundation models, KGs/ontologies, drug repurposing, rare
disease, ML for precision health, multimorbidity, knowledge
representation in EHRs).

Window: **2026-09-01 12:40Z → 2026-09-10 12:36Z** (~9 days since the
last research-digest report, covering nine arxiv-digest cron runs
and six Google Scholar alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-09.md`) | 09-01 → 09-09 daily crons | 9 daily runs. Dry days (0 papers): 09-03, 09-05, 09-06, 09-08. 09-01: 1 paper (Ghiasi PhD-thesis dissertation on storage-centric genomic-analysis systems — hardware/systems, SKIP). 09-02: 1 paper (Ramesh et al. mudskipper locomotion; `motor` keyword false positive, SKIP). 09-04: 2 papers (Cortez-Rodriguez natural-disaster nonprofit panel causal inference — off-topic, SKIP; Yu et al. location-invariant extremal QTE via IPW — METHODS-WATCH). 09-07: 1 paper (Rajabli & Collins compact brain-age CNN adapted with LoRA — METHODS-WATCH). 09-09: 2 papers (Snel & Schulz UKB training-data-attribution for Cohen's d in normative age biomarkers — **HIGH**; FUSE-RT HPLC Sim2Real foundation model — off-topic chromatography, SKIP). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads. Same pattern as last window: the pipeline commits its output to this repo rather than emailing PR/cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-09 batch, 16:04Z + 22:32Z) | 09-09 16:04Z, 22:32Z | 40+ feeds fired across two same-day pushes. Recurring HIGH item across five feeds: Wu et al. Alzheimer's-disease drug-repurposing TTE on decentralised RWD (Yong Chen new-articles, Patrick Ryan new-related, Pascal Brandt 1-new-citation, George Hripcsak 10-new-citations, Miguel Hernán 10-new-citations). Also: Ju et al. UDCA-Parkinson's TTE in UK EHR (EHR + FM feed), Zhang et al. Bayesian colocalization × MR benchmarking (Jian Yang new-related), Aguilar-Ordoñez oriGen 1,427 Mexican WGS (Denny citations), Bellucci et al. Agentic-AI EHR + KG for RWE (Zhiyong Lu new-related), Fu et al. long-read trio-barcoded adaptive sequencing (Stephen Montgomery, Kai Wang, Lisa Bastarache new-related), Somatic Mosaicism across Human Tissues Network 25-individual mosaicism map (Karczewski citations), Jandu et al. inherited systemic-inflammation predisposition PheRS-style (Bastarache citations). |
| Google Scholar alerts (09-07 batch, 16:17Z) | 09-07 16:17Z | 27 feeds fired. HIGH items: Hysong et al. sickle-cell-trait phenome+lab-WAS (Bastarache/Denny citations), Roberts et al. Polygenic Pharmacotherapy evidence map (Denny new-related), Pajusalu et al. Syrona OMOP-CDM pairwise dataset comparison (Patrick Ryan new-related), Bhattacharjee et al. longitudinal African mental-health data migrated to OMOP (Hripcsak new-related), Ma et al. long-read RNA-seq for rare-disease trios splicing outliers (Stephen Montgomery new-related), Brunello et al. GenPhenia HPO-DL rare-disease diagnosis (Bastarache new-related), Bai et al. relation-aware multimodal KG for DDI (Hripcsak citations — METHODS-WATCH). |
| Google Scholar alerts (09-06 batch, 06:02Z + 13:58Z) | 09-06 06:02Z, 13:58Z | 17 feeds fired. HIGH items: Garg et al. UKB + Scottish PGx determinants of T2D drug response (`UK Biobank` feed), Perée et al. IBD cis-eQTL entrectinib repurposing (Pritchard citations — direct hit for IBD + drug repurposing threads). Also: Ong et al. cardiometabolic wearable phenotyping (Chenjie Zeng new-related — METHODS-WATCH), Yao et al. CHIP + ASCVD narrative review (`intitle:"clonal hematopoiesis"` — CHIP thread, review-only). |
| Google Scholar alerts (09-04 batch, 16:08Z + 21:26Z) | 09-04 16:08Z, 21:26Z | 25 feeds fired. HIGH items: Park et al. cross-ancestry cross-disorder PRS portability for OCD (Karczewski/Denny/Bastarache/Chenjie Zeng — quadruple feed hit; **HIGH**), DeVito & Gymrek nonlinear + spatiotemporal × nongenetic PGS interactions Nat Comms (Jian Yang, Karczewski citations — direct hit for GxE + PGS × exposure sub-thread), Boceck et al. aiDIVA hybrid AI for rare-disease diagnostics (Bastarache/Kai Wang/Montgomery citations — triple-feed hit), Zhou et al. cardiorenal illness trajectories after antihypertensives × ADHD (Hripcsak citations — pharmacoepi cardiorenal), Galderisi et al. CGM during elexacaftor/tezacaftor/ivacaftor in CF youth (Patrick Ryan new-related — direct hit for CF/CFTR thread). |
| Google Scholar alerts (09-03 batch, 13:02Z) | 09-03 13:02Z | 12 feeds fired. HIGH items: Kırboğa DMS of CYP2C9/CYP2C19/NUDT15 shows pharmacogene variant interpretation needs assay-specific data (`variant interpretation OR variant classification` — ACMG/PGx crossover), Yao et al. CHIP + ASCVD review (`intitle:"clonal hematopoiesis"` — CHIP thread). Also: Song et al. characterization of predicated pathogenic missense variants (`mendelian diseases` — METHODS-WATCH), Luo et al. Mendelian-randomization selection-bias correction in UKB (`UK Biobank` — METHODS-WATCH). |
| Google Scholar alerts (09-02 batch, 02:01Z) | 09-02 02:01Z | 10 feeds fired. HIGH items: Garofalo et al. multi-ancestry sequencing in 293,141 participants across HCC-risk DNA-repair genes (`All of Us research program` — direct hit for AoU + variant interpretation + cross-ancestry). Also: Chovatiya et al. Abrocitinib RWE from EHR + claims (`electronic health records` — pharmacoepi/dermatology), Zhang et al. proteomics + ML for osteoporosis UKB (`UK Biobank` — METHODS-WATCH). |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets. Where multiple author feeds surfaced the
> same paper (e.g. Wu et al. AD-repurposing hit five feeds), the item
> is written up once with all surfacing feeds noted.

---

## Executive summary (HIGH-priority studies, ranked)

Nineteen HIGH items surfaced this window, clustering into seven knots:

**Drug repurposing × TTE cluster (3 items).** Wu et al. (JMIR-Aging-family
2026 preprint, Yong Chen lab) — **decentralised RWD target-trial
emulation for Alzheimer's-disease drug repurposing** — surfaced
simultaneously in the Yong Chen, Patrick Ryan, Pascal Brandt, George
Hripcsak, and Miguel Hernán feeds, which is the strongest cross-feed
signal this window. Ju et al. — **UDCA (ursodeoxycholic acid) and
Parkinson's-disease risk: an emulated target trial in UK electronic
health records** — direct-hit crossover of pharmacoepi TTE, EHR-based
repurposing signal mining, and a rare-drug reindication candidate. Perée
et al. *Nature (Genetics-adjacent)* 2026 — **cell-type-specific
blood + gut eQTL analyses matching 140 IBD risk loci to entrectinib as a
repurposing candidate** — the exact eQTL-to-drug-repurposing framing
your `Drug repurposing` thread flags as high-priority (KG/eQTL evidence,
not opaque link prediction).

**PheWAS / composite-risk + PheRS cluster (2 items).** Hysong et al.
*American Journal of Human Genetics* 2026 — **phenome- and
laboratory-wide meta-analyses of sickle-cell trait revealing multi-system
disease associations** — direct hit for PheWAS/phecode infrastructure
plus ancestry-aware risk (SCT frequency is African-ancestry–concentrated
and the ascertainment biases you flag under monogenic-carrier
population-screening apply here). Jandu et al. *Human Genetics and
Genomics Advances* 2026 — **inherited predisposition to increased
systemic inflammation predicts a broad class of disease phenotypes** —
the composite-PheRS-style architecture your PheRS/composite-risk
sub-thread prioritizes.

**PGS composite-risk / GxE cluster (3 items).** DeVito & Gymrek *Nature
Communications* 2026 — **nonlinear and interaction effects of
spatiotemporal and nongenetic factors improving complex-trait
prediction** — a direct hit for the Nagpal & Gibson "pervasive PGS ×
exposure interactions" framing you flagged. Park et al. *Translational
Psychiatry* 2026 — **cross-ancestry cross-disorder PRS transferability
for OCD** — quadruple-feed cross-referenced (Karczewski, Denny,
Bastarache, and Chenjie Zeng feeds all picked it up), textbook direct
hit for the cross/trans-ancestry PGS portability sub-thread. Roberts et
al. arXiv 2026 — **polygenic pharmacotherapy: an evidence map of scores,
interactions, ancestry transferability, and clinical utility** — bridges
PGS composite risk and the pharmacogenomic-modifier-of-medication-persistence
sub-thread; positions PGS-based prescribing beyond single-gene rules.

**Somatic mosaicism / CHIP cluster (2 items).** Somatic Mosaicism across
Human Tissues Network *bioRxiv* 2026 — **integrated map of somatic
mosaicism across human tissues in 25 individuals** — the reference
dataset for the somatic-mosaicism thread; portable audit template for
CHIP/VEXAS/LOY germline-scan contamination concerns per Ji et al.
2026 (previously flagged). Yao et al. *review* 2026 — **CHIP and
atherosclerotic cardiovascular disease: clinical implications,
mechanisms, emerging therapies** — thread-anchor review; use for
citation-graph seeding rather than primary methods.

**EHR phenotyping / OMOP + agentic RWE cluster (3 items).** Bellucci et
al. *Frontiers in AI* 2026 — **an agentic AI framework connecting LMs to
EHR + biomedical knowledge graph for real-world evidence** — direct hit
for `Agentic / human-in-the-loop observational-causal-inference
pipelines` (Chou/Kallus oci-agent lineage) crossed with the
KG-augmented-LLM-for-RWE line. Pajusalu et al. *BMC Medical Informatics*
2026 — **Syrona, an open-source visual analytics tool for pairwise
comparison of health datasets in OMOP CDM** — hits the
`Fidelity, portability, and audit of representations` sub-thread of
`Knowledge representation in EHRs`. Bhattacharjee et al.
*Biostatistics in Africa* 2026 — **migrating longitudinal African
mental-health data from staging to the OMOP CDM** — direct hit for OMOP
infrastructure + expansion of representation-drift audits into
underrepresented sites (BioVU/AoU/MIMIC/UKB is your usual comparator
axis; adding Africa is important).

**Rare disease / variant interpretation cluster (5 items).** Kırboğa
*G3* 2026 — **deep mutational scanning of CYP2C9, CYP2C19, and NUDT15
shows pharmacogene variant interpretation requires assay-specific
functional data** — direct hit for ACMG/AMP variant curation + PGx
(this is the assay-context ACMG PS3-code discussion generalized to
metabolizer-phenotype genes). Fu et al. *Nature Communications* 2026 —
**cost-efficient long-read trio-barcoded adaptive sequencing improves
rare-disease diagnosis** — reference for the pre-symptomatic phenoconversion
diagnostic-yield sub-thread. Ma et al. *medRxiv* 2026 — **long-read RNA
sequencing improves isoform and splicing outlier detection in
whole-blood rare-disease trios** — direct hit for splicing/RNA evidence
for VUS resolution. Boceck et al. *npj Genomic Medicine* 2026 — **aiDIVA
hybrid AI for rare-disease diagnostics using evidence-based ML and
language models** — three-feed cross-hit; adds a hybrid-symbolic /
LLM benchmarking point for Phen2Gene / PhenoSV / LIRICAL / PhenoGPT2
comparisons per GraphRareBench framing. Brunello et al. *Human Genomics*
2026 — **GenPhenia: deep NNs to accelerate rare-disease diagnosis** —
another Phen2Gene-adjacent benchmark candidate.

**Biobanks / EHR-linked cohorts + genetic epi (3 items).**
Aguilar-Ordoñez et al. *Nature Communications* 2026 — **whole-genome
sequencing of 1,427 Mexican individuals from the oriGen cohort** —
cross-ancestry portability reference dataset; complements the
Acharya et al. tri-biobank ASCVD paper flagged in the prior report.
Garg et al. *Diabetes* 2026 — **genetic and clinical determinants of
T2D drug response in Scottish + UK Biobank cohorts** — direct hit for
pharmacogenomic modifiers of medication persistence sub-thread and
overlaps with the GLP-1/SGLT2 drug-class threads. W. Zhang et al.
*Genomics Proteomics & Bioinformatics* 2026 — **benchmarking Bayesian
colocalization methods for validating MR-identified targets** —
methods-paper for the drug-target-MR-triangulated-with-observational
sub-thread (Saxby metformin × AAA lineage).

**Specific-disease threads (1 item).** Galderisi et al. *CF-clinical
journal* 2026 — **continuous glucose monitoring to track metabolic
changes in youths with cystic fibrosis before and after
elexacaftor/tezacaftor/ivacaftor** — direct hit for CF/CFTR modulator
thread; adds a mechanistic-endpoint sub-endpoint to modulator-pharmacoepi
work.

**METHODS-WATCH honorable mentions (8 items):**

- Chen et al. *JAMA Network Open* 2026 — oral anticoagulants in AF +
  advanced CKD (Hernán feed). Rigorous CV-outcomes RWE outside your
  tracked drug classes; useful as a design template.
- Zhou et al. *Nature Communications*(?) 2026 — long-term cardiorenal
  illness trajectories after antihypertensives × ADHD (Hripcsak feed).
  Design pattern for pharmacoepi with psychiatric comorbidity strata.
- Yu et al. arXiv `2609.04018` 2026 — location-invariant extremal QTE
  estimator with IPW (arxiv-digest 09-04). Novel causal-ML method for
  heavy-tailed potential outcomes; portable to biomarker-tail HTE.
- Rajabli & Collins arXiv `2609.05400` 2026 — compact brain-age CNN as
  reusable neuroimaging FM adapted with LoRA (arxiv-digest 09-07).
  Compact-FM-with-LoRA pattern is portable to structured-EHR FMs.
- Snel & Schulz arXiv `2609.07729` 2026 — training-data attribution for
  Cohen's d in UKB normative age biomarkers (arxiv-digest 09-09).
  Influence functions on effect size (not loss) — cleanly portable to
  auditing PGS/PheRS training-cohort composition.
- Loay et al. *AJHG* 2026 — mutation-rate heterogeneity biases variant
  effect prediction (Karczewski feed). Variant-interpretation methods.
- Bai et al. *Scientific Reports* 2026 — relation-aware multimodal KG
  for drug-drug interaction prediction (Hripcsak citations). KG-for-DDI
  reference; complements DKL, PLRA-KG references from prior windows.
- Ong et al. *2026* — cardiometabolic wearable phenotyping (Chenjie
  Zeng new-related feed). Adjacent to your multimorbidity /
  cardiometabolic subtyping thread.

---

## Detailed writeups (HIGH items)

### 1. Wu et al. — Discovering repurposable drugs for Alzheimer's disease and related dementias: target trial emulation using decentralised real-world data (2026)

**Feeds:** Yong Chen new-articles (09-09 16:04Z), Patrick Ryan
new-related (09-09), Pascal Brandt 1-new-citation (09-09), George
Hripcsak 10-new-citations (09-09), Miguel Hernán 10-new-citations
(09-09). Five-feed cross-hit — the strongest cross-referenced signal
this window.

**Threads served:** `Drug repurposing` (EHR-based repurposing signals,
causal framing of off-label use); `Causal inference and
pharmacoepidemiology` (TTE + decentralised RWD); tangentially `Rare
disease` (AD/ADRD screening yields).

**What's there:** From Scholar-snippet metadata alone, this is a
**target-trial emulation study using decentralised real-world data** to
identify **repurposing candidates for Alzheimer's disease and related
dementias (ADRD)**. Yong Chen (Penn) is the anchor author; the paper
appears with the same title in Patrick Ryan's OHDSI-facing feed and in
the Hernán/Hripcsak citation graphs, which suggests it is TTE-formal
enough to have been cited immediately by the causal-inference and
pharmacoepi communities. The Pascal Brandt feed picking it up as a
single-citation event to *his own* work indicates the paper likely
references FM-adjacent phenotyping or EHR-scale data-federation
infrastructure. Decentralised RWD framing (rather than single-site EHR)
is unusual for ADRD and directly overlaps with the "federated /
privacy-preserving EHR causal analytics" sub-thread you flagged
(Jang et al. arXiv 2607.17958 lineage).

**Why it's high-priority:** Your `Drug repurposing` thread rubric weights
EHR-based repurposing signals + causal-inference framing of off-label
use above target-only pipelines. This paper is precisely that
combination applied to a disease where off-label repurposing signals
have historically been noisy (blood-pressure meds, GLP-1s, metformin,
sildenafil, statins, PPIs, valacyclovir have all been repurposing
candidates for AD with contradictory results). A properly-emulated TTE
on decentralised RWD is the design that could adjudicate. Cross-check
against the Zhao et al. cancer-immunotherapy TTE review from the last
window: same TTE + treatment-effect-learning + clinical-translation
scaffold, transposed onto ADRD.

**What to read the paper for:** (a) which drugs surface as candidates
after empirical calibration (does metformin or GLP-1 signal survive?);
(b) whether they used propensity-score trimming and negative-control
outcomes (the Zhang et al. GLP-1/SGLT2/DPP4i paper from last window
established that as the gold-standard TTE pattern for cardiovascular
outcomes); (c) how decentralised RWD is stitched — federated queries
across TriNetX / OHDSI-network sites or something more novel; (d)
whether ADRD phenotyping uses billing-only or note-augmented phecodes
(and if the latter, this is a Wu et al. ACT-style representation-audit
opportunity).

**Follow-up:** Pull the PDF, look for the decentralised-RWD stack
diagram, and cross-reference with Ju et al. UDCA-PD (below) — same
neurodegeneration-repurposing TTE pattern.

---

### 2. Ju et al. — Ursodeoxycholic acid and Parkinson's disease risk: an emulated target trial in UK electronic health records (2026)

**Feeds:** `Foundation models and "electronic health records"` keyword
feed (09-09 22:32Z); `"electronic health records"` keyword feed (09-09
22:32Z).

**Threads served:** `Causal inference and pharmacoepidemiology` (TTE);
`Drug repurposing` (off-label neurodegenerative use of a hepatobiliary
drug); `EHR phenotyping & OMOP` (UK EHR provenance).

**What's there:** Authors listed as Ju C, Schrag A, Carroll C, Xiong X
et al. Anette Schrag (UCL neurology) is a well-known movement-disorders
epidemiologist; Camille Carroll is a Parkinson's clinical trialist.
Title is unambiguous: an **emulated target trial** of UDCA on
Parkinson's-disease risk in UK EHR (CPRD/HES most likely). UDCA has a
strong mechanistic case for PD-neuroprotection from mitochondrial /
proteostatic work at Sheffield (Bandmann lab), which is the trial arm
UP study rationale.

**Why it's high-priority:** This is the exact "rare-disease repurposing
where HPO-based phenotype matching connects to candidate compounds"
crossover you flagged, transposed onto a common neurodegenerative
disease. The UK-EHR provenance also gates it as a real EHR-phenotyping
paper, not a summary-stat exercise. Direct pair to the Wu et al. ADRD
paper above — same TTE-for-repurposing pattern.

**What to read the paper for:** (a) how PD is phenotyped in CPRD/HES —
CPRD-gold code lists vs. Read-code cascades; (b) UDCA exposure window
and censoring for competing events (liver disease, biliary events); (c)
whether the study is a re-emulation of the UP-PD RCT (Bandmann's trial)
— if so, TTE-vs-RCT concordance is publishable in itself; (d) negative
control outcomes and E-values.

**Follow-up:** Compare with the Zhao et al. TTE-review lineage from last
window; extract the UDCA-PD exposure definition for possible re-use in
AoU or BioVU replication studies.

---

### 3. Hysong et al. — Phenome- and laboratory-wide meta-analyses of sickle cell trait reveal multi-system disease associations (2026)

**Feeds:** Bastarache 6-new-citations (09-07); Denny 10-new-citations
(09-07). Authors: Hysong MR, Shuey MM, Miller-Fleming TW, Keat K et al.
Published in *American Journal of Human Genetics*.

**Threads served:** `PheWAS / phecode infrastructure` (direct hit);
`Biobanks with EHR linkage` (multi-cohort meta-analysis is only
tractable in EHR-linked biobanks); `Genetic epidemiology` (SCT
carrier-state; frequency is African-ancestry–concentrated).

**What's there:** Multi-cohort phenome-wide + laboratory-wide
meta-analysis of **sickle-cell trait carrier status** (HbAS
heterozygotes). Miller-Fleming and Shuey are BioVU/VUMC investigators;
Keat is Penn. The design is textbook Bastarache/Denny lineage — extend
a monogenic-variant PheWAS to a laboratory-wide (LabWAS) axis so that
the analysis captures both diagnostic codes and continuous biomarker
signatures.

**Why it's high-priority:** This is the exact "penetrance under
population-screening conditions vs. clinically ascertained cohorts"
framing your PheWAS-infrastructure thread prioritizes. SCT is a
prototypical case where clinically ascertained SCT (referral cohorts,
military cohorts) systematically over-reports adverse outcomes vs.
population-based EHR-linked ascertainment. LabWAS captures the subclinical
biomarker footprint that PheWAS-alone would miss. The paper also
generalizes the malignant-hyperthermia (Lichtenberger et al. 2026)
pharmacogenetic penetrance framing from last window to a
population-genetics carrier framing.

**What to read the paper for:** (a) which lab traits drive most of the
new signal (haematocrit, LDH, potassium, creatinine, urine
concentration); (b) ancestry-stratification and whether the analysis
uses admixture-adjusted LabWAS or simple African-ancestry–restricted
LabWAS; (c) any novel non-renal / non-thrombotic disease associations
(the "multi-system" phrasing suggests yes); (d) how they handle
comorbid SS/Sβ0 (compound heterozygotes) — are those censored, treated
as separate arm, or misclassified?

**Follow-up:** This paper is the SCT template that generalizes cleanly
to APOL1 G1/G2 carrier state (your APOL1 thread) — a LabWAS on APOL1
G1/G2 with the same design would be publishable.

---

### 4. Jandu et al. — Inherited Predisposition to Increased Systemic Inflammation Predicts a Broad Class of Disease Phenotypes (2026)

**Feeds:** Bastarache 4-new-citations (09-09). Authors: Jandu HK,
Olowofela A, Shuey M, Quade K, Tuftin B et al. Published in *Human
Genetics and Genomics Advances*. VUMC/BioVU lineage.

**Threads served:** `PheWAS / phecode infrastructure` (PheRS on a
composite inflammation-liability score); `Chronic disease clustering
and multimorbidity`; `Machine learning for precision health`.

**What's there:** From the snippet: "**Chronic** inherited predisposition
to increased systemic inflammation" — this is a **composite PGS/PheRS
built on inflammatory biomarker signatures** (probably CRP-PGS or a
proteomic-augmented inflammation composite) tested for PheWAS-wide
disease associations across a broad phenome (BioVU). Shuey / Quade are
frequent VUMC PheWAS collaborators.

**Why it's high-priority:** Direct hit for the composite-risk framing
in your genetic-epi thread — stack a PRS (or in this case a
biomarker-liability score) with rare pathogenic variants and score
against a phenome. It's PheRS in structure but the "score" is a
biomarker-inflammation liability rather than a disease-liability. Bridges
naturally to Nagpal & Gibson pervasive PGS × exposure, and to
multi-omics-augmented PRS (Nightingale NMR, Olink) which you flagged.

**What to read the paper for:** (a) score construction (CRP-PGS,
IL-6-PGS, a composite Olink-stack, or a phecode-derived inflammation
liability from prior admissions?); (b) which disease clusters light up
disproportionately — cardiometabolic vs autoimmune vs psychiatric; (c)
whether they run a sensitivity analysis excluding people with active
inflammatory conditions at baseline (guarding against reverse
causation); (d) any decomposition into PGS-tails-vs-residuals per the
Baya *AJHG* 2026 framing you flagged.

---

### 5. DeVito & Gymrek — Modeling nonlinear and interaction effects of spatiotemporal and nongenetic factors improves prediction for complex traits (Nature Communications 2026)

**Feeds:** Jian Yang new-related (09-04); Karczewski 10-new-citations
(09-04). Melissa Gymrek's UCSD group.

**Threads served:** `Genetic epidemiology` (PGS × exposure); `Machine
learning for precision health`; `Chronic disease clustering and
multimorbidity`.

**What's there:** Complex-trait prediction that explicitly models
**nonlinear interactions between PGS and spatiotemporal + nongenetic
factors**. This is the empirical follow-up to the Nagpal & Gibson
*Nature Genetics* 2026 review of pervasive PGS × exposure interactions
that you flagged as high-priority for the digest, moved from
"conceptual claim" to "prediction-improvement claim with cross-validated
gain."

**Why it's high-priority:** Directly serves the GxE / PGS × exposure /
environment sub-thread of your `Genetic epidemiology` thread. The
"spatiotemporal + nongenetic" framing also overlaps with your
`Chronic disease clustering` interest — spatiotemporal is the environment
axis that latent-class trajectory models often ignore.

**What to read the paper for:** (a) which traits gain the most from
interaction modeling (probably lipid/BMI/BP first, psychiatric last);
(b) the parameterization — GAM vs random-forest vs neural — since the
portability claim rests on whether the nonlinearity is transportable
across cohorts; (c) any test in ancestry-stratified UKB or in a
non-UKB cohort (AoU / MVP / MyCode), which is required to satisfy your
portability threshold.

**Follow-up:** This is the paper that lets you write the Nagpal & Gibson
review citation with a specific "and see DeVito & Gymrek 2026 for
empirical confirmation in [X traits]" sentence.

---

### 6. Park et al. — Cross-ancestry and cross-disorder transferability of polygenic risk scores for obsessive-compulsive disorder (Translational Psychiatry 2026)

**Feeds:** Karczewski, Denny, Bastarache, Chenjie Zeng new-related feeds
(all 09-04). Quadruple-feed cross-hit — the second-strongest signal
this window after Wu et al. ADRD.

**Threads served:** `Genetic epidemiology` (cross-ancestry PGS
portability + cross-disorder liability); `Machine learning for
precision health`.

**What's there:** OCD-PRS constructed on European-ancestry summary stats,
evaluated for **cross-ancestry transfer** and **cross-disorder transfer**
(likely to the OCD-adjacent phenome — Tourette's, hoarding, autism,
depression, anxiety). Park CI is Korean psychiatry-genetics, so the
non-European ancestry test is likely Korean-cohort or East-Asian
biobank.

**Why it's high-priority:** Direct hit for the cross-ancestry PGS
portability sub-thread. Cross-disorder transfer also lands in the
`Cross-trait shared genetic architecture and multi-trait triangulation`
sub-thread (MiXeR / conditional-FDR lineage you flagged). Four separate
feeds picking it up is a signal that the paper triangulates both
technical portability methods and their biological interpretability.

**What to read the paper for:** (a) which PGS construction method
(PRS-CS-x, PolyPred, MUSSEL, or a bespoke local-ancestry-aware method);
(b) transfer R² by ancestry and how it compares to the European-derived
baseline; (c) whether cross-disorder PGS transfer for OCD is stronger
to Tourette (shared architecture expected) than to depression (weaker
sharing); (d) any AoU or East-Asian-biobank replication.

---

### 7. Roberts et al. — Polygenic Pharmacotherapy beyond Single-Gene Rules: An Evidence Map of Scores, Interactions, Ancestry Transferability, and Clinical Utility (2026)

**Feeds:** Joshua Denny new-related (09-07). PDF, arXiv-style
preprint.

**Threads served:** `Genetic epidemiology` (PGS clinical utility);
`Causal inference and pharmacoepidemiology` — specifically the
**pharmacogenomic modifiers of medication persistence** sub-thread.

**What's there:** An **evidence map** (systematic scoping-style survey)
of **polygenic scores as pharmacotherapy guides**, explicitly moving
beyond CPIC-style single-gene PGx rules. Covers PGS × drug interactions,
cross-ancestry PGS transferability for drug response, and clinical-utility
evidence.

**Why it's high-priority:** Direct-hit positioning paper for the
pharmacogenomic-modifier-of-medication-persistence sub-thread you added
under `Causal inference and pharmacoepidemiology`. Together with the
Cohen et al. *Pharmaceuticals* 2026 and Psy-PGx UKB papers you flagged
under that sub-thread, this is the meta-view that lets you cite the
sub-field as an entity rather than a case-list.

**What to read the paper for:** (a) which drug-response outcomes have
the strongest polygenic-modifier evidence (statins first, warfarin next
via CYP2C9 + VKORC1, then SSRIs); (b) how the review handles the
"single-gene high-effect + PGS-background" combined model vs pure PGS;
(c) any recommendation on threshold-selection for polygenic
pharmacotherapy in clinical decision support (this is the AoU /
BioVU / MVP implementation lever); (d) whether the review covers
CFTR-modulator response — that's the CF thread crossover.

---

### 8. Perée et al. — Cell-type specific analyses in blood and gut identify cis-eQTL matching 140 IBD risk loci and entrectinib as repurposing candidate (Nature 2026)

**Feeds:** Jonathan K Pritchard 10-new-citations (09-06). Authors:
Perée H, Petrov VA, Tokunaga Y, Kvasz A, Farnir F et al. *Nature* 2026.

**Threads served:** `Specific disease threads → IBD`; `Drug repurposing`
(the eQTL-to-drug-repurposing pattern you explicitly prioritize).

**What's there:** Cell-type-specific eQTL analyses in blood and gut
matched to **140 IBD GWAS risk loci**, surfacing entrectinib (a
TRK/ROS1/ALK inhibitor) as a **novel repurposing candidate**. Entrectinib
is currently oncology-licensed (Rozlytrek); repurposing to IBD is a
substantial pivot.

**Why it's high-priority:** Your `Drug repurposing` thread specifically
flags "knowledge-graph / GNN approaches with *explainable* hypothesis
output" and "EHR-based repurposing signals" as high-priority. Perée et
al. is one step earlier in the pipeline — eQTL/GWAS-to-drug — but the
mechanism-linked hypothesis output (specific loci → specific cell type
→ specific druggable target) is exactly the "path or subgraph rationale"
rather than opaque link-prediction score that your rubric weights. It's
also the IBD-thread anchor of this window.

**What to read the paper for:** (a) what fraction of the 140 loci have
a cell-type-specific eQTL match — this is the "PheWAS/loci-yield" scale
for cell-type specificity; (b) how the entrectinib candidate is scored
against existing IBD biologics (anti-TNF, anti-integrin, JAK
inhibitors); (c) any orthogonal MR or colocalization evidence for the
TRK/ROS1/ALK loci; (d) whether the paper triangulates with any EHR
signal (post-marketing entrectinib patients with incident IBD — likely
too rare to detect but the design is worth checking).

**Follow-up:** Compare to Bai et al. relation-aware KG-for-DDI paper
(same window, Hripcsak feed) for the KG-inference-vs-cell-type-eQTL
axis.

---

### 9. Somatic Mosaicism across Human Tissues Network — Integrated map of somatic mosaicism across human tissues in 25 individuals (bioRxiv 2026)

**Feeds:** Karczewski 10-new-citations (09-09). Consortium paper.

**Threads served:** `Specific disease threads → CHIP/VEXAS/LOY / somatic
mosaicism`; germline-rare-variant QC.

**What's there:** Consortium-scale **cross-tissue somatic mosaicism map**
across 25 individuals. This is a reference dataset comparable in ambition
to GTEx-for-somatic-mutations — deep tissue sampling per donor, unified
variant-calling pipeline, tissue-of-origin resolution.

**Why it's high-priority:** Direct anchor for the somatic-mosaicism
sub-thread. Also serves as the "how much somatic mosaicism should we
expect in a rare-variant scan?" QC baseline that Ji et al. *Biology* 2026
germline-rare-variant contamination paper (you flagged that one) motivates.
Reference dataset — every downstream CHIP/VEXAS/LOY paper this year will
cite it.

**What to read the paper for:** (a) tissue-specificity of clonal
expansion (blood-dominated for CHIP as expected, but any surprises in
skin/gut?); (b) the extent to which somatic mosaicism leaks into
non-blood tissues at frequencies visible to germline-variant callers;
(c) any age-stratified layer that gives you a tissue-by-age baseline
rate; (d) resource files — VCF, browser, tissue-of-origin QC pipelines.

---

### 10. Bellucci et al. — An Agentic AI Framework Connecting Language Models to Electronic Health Records and a Biomedical Knowledge Graph for Real-World Evidence (Frontiers in AI 2026)

**Feeds:** Zhiyong Lu new-related (09-09). Authors: Bellucci G, Gu W,
Rose PW, Baranzini SE. Baranzini is the SPOKE knowledge-graph lab (UCSF)
— so this is very likely a SPOKE-based agentic pipeline.

**Threads served:** `Causal inference and pharmacoepidemiology` (agentic
observational-causal-inference pipelines sub-thread); `Knowledge graphs
& ontologies`; `Knowledge representation in EHRs and applications`
(SPOKE crossover); `Drug repurposing` (SPOKE has a long repurposing
lineage).

**What's there:** An **agentic AI framework** that connects LMs to EHRs
+ SPOKE-family biomedical KG for real-world evidence generation. Very
likely an implementation of the "LLM asks EHR and KG in coordinated
turns" pattern that Chou/Kallus oci-agent (arXiv 2607.22443) and the
Netflix in-production system exemplify, transposed to biomedicine.

**Why it's high-priority:** Direct hit for the agentic-observational-causal-inference
sub-thread. Also crosses into KG + EHR + repurposing — three of your
active threads simultaneously.

**What to read the paper for:** (a) the tool contract — what does the
agent call on EHR side (SQL / OMOP-CDM / FHIR)? What does it call on
KG side (SPOKE, PrimeKG, other)?; (b) which RWE tasks the agent solves
(cohort discovery, ATE estimation, drug-drug interaction hypothesis
generation, adverse-event surveillance); (c) benchmarks vs a
human-analyst baseline; (d) failure modes — where does the agent
hallucinate cohorts vs. where does it correctly abstain.

---

### 11. Pajusalu et al. — Syrona: an open-source visual analytics tool for pairwise comparison of health datasets in OMOP CDM (BMC Medical Informatics 2026)

**Feeds:** Patrick Ryan new-related (09-07). Authors: Pajusalu M, Oja M,
Mooses K, Heinsar S, Laisk T et al. — Estonian OMOP group (OPTIMA
lineage from last window's Ilves et al. CohortContrast).

**Threads served:** `EHR phenotyping & OMOP`; `Knowledge representation
in EHRs → Fidelity, portability, and audit of representations` sub-thread
(direct hit).

**What's there:** **Syrona**, an open-source visual analytics tool for
**pairwise comparison of two OMOP-CDM health datasets**. The natural use
case is site-to-site portability audit: BioVU-vs-AoU, UKB-vs-MVP,
Estonian OPTIMA-vs-Finnish FinnGen, or two-time-window comparisons at
the same site (representational drift). This is the tool layer on top of
DataQualityDashboard / Achilles.

**Why it's high-priority:** Direct hit for the fidelity-portability-audit
sub-thread of `Knowledge representation in EHRs`. Also directly usable
in your own AoU-vs-BioVU comparisons. Complements CohortContrast from
last window — CohortContrast is the enrichment-based cohort-derivation
tool, Syrona is the dataset-comparison tool.

**What to read the paper for:** (a) which OMOP domains it covers
(condition, drug, measurement, observation, procedure, visit); (b)
which comparison metrics it exposes (concept-prevalence deltas,
temporal drift, feature-marginal distributions, embedding-space
distances); (c) whether it handles the vocabulary-mapping-version
question (SNOMED release drift is a real portability killer); (d)
GitHub link + install path.

---

### 12. Bhattacharjee et al. — Migrating longitudinal African mental health data from staging to the OMOP common data model (Biostatistics in Africa 2026)

**Feeds:** George Hripcsak new-related (09-07).

**Threads served:** `EHR phenotyping & OMOP`; `Knowledge representation
in EHRs → Interoperability standards and their representational
consequences`; expansion of representation audits into
underrepresented sites.

**What's there:** OMOP-CDM migration of a **longitudinal African
mental-health data source**. Mental health OMOP mappings are historically
weak (SNOMED coverage for psychiatric constructs is patchy, and the DSM
↔ SNOMED bridge is not clean), so the migration itself is
methodologically interesting.

**Why it's high-priority:** African EHR data are wildly underrepresented
in OMOP-CDM literature; the ancestry-and-site drift concerns you flag
under `Fidelity, portability, and audit of representations` apply *first*
to whether the CDM can even represent the data. This is the "does OMOP
work at all here?" step-zero paper for African cohorts, and it's a
Hripcsak-adjacent lineage which is closer to the OHDSI-network core than
most Africa OMOP work.

**What to read the paper for:** (a) which African country / cohort; (b)
which mental-health constructs failed to map cleanly (predictable: local
idioms of distress, culturally bound syndromes); (c) whether they had
to add source-concept extensions or requested new SNOMED entries; (d)
downstream analyses attempted on the migrated data.

---

### 13. Kırboğa — Deep mutational scanning of CYP2C9, CYP2C19, and NUDT15 shows that pharmacogene variant interpretation requires assay-specific functional data (G3 2026)

**Feeds:** `variant interpretation OR variant classification` keyword
feed (09-03).

**Threads served:** `Variant interpretation (ACMG / ClinGen)`;
pharmacogenomics.

**What's there:** **Deep mutational scanning** of three canonical
metabolizer-phenotype PGx genes (**CYP2C9, CYP2C19, NUDT15**) with the
central claim that **assay context materially changes the functional
readout**, and therefore ACMG PS3 evidence for PGx variants cannot be
lifted cleanly across assays. NUDT15 is a thiopurine-metabolism gene
(azathioprine / 6-MP dosing in IBD, ALL); CYP2C9 governs warfarin +
NSAID metabolism; CYP2C19 governs clopidogrel + PPI + SSRI metabolism.

**Why it's high-priority:** Direct hit for ACMG/AMP variant curation
(PS3 code evidence in particular is the assay-context-sensitive one
your ClinGen VCEP interest maps to). Also crosses into pharmacoepi via
NUDT15 → IBD, CYP2C9 → warfarin, CYP2C19 → clopidogrel — three of your
tracked-drug or tracked-disease intersections.

**What to read the paper for:** (a) which assays disagree the most —
substrate-specific enzymatic activity, cell-viability at drug dose,
protein stability, mRNA abundance; (b) whether the disagreement is
random or ordered by substrate class; (c) any variant-specific
recommendations (e.g., variant X reads LoF in assay 1 but neutral in
assay 2, and the clinical evidence favors 2); (d) implications for
PS3-code use in ClinGen VCEPs.

---

### 14. Fu et al. — Cost-efficient long-read trio-barcoded adaptive sequencing improves rare disease diagnosis (Nature Communications 2026)

**Feeds:** Stephen B Montgomery new-related (09-09); Kai Wang new-related
(09-09); Lisa Bastarache new-related (09-09). Three-feed cross-hit.

**Threads served:** `Rare disease`; `Variant interpretation` (long-read
resolves structural / repeat / methylation variants that short-read
misses).

**What's there:** **Long-read (likely Nanopore or PacBio) adaptive
sequencing** with **trio-barcoded** multiplex — three probands + parents
run in one adaptive-sequencing flow-cell, dynamically enriching for
regions of interest. "Cost-efficient" is the punchline: this closes the
long-read-affordability gap for clinical rare-disease diagnostic labs.

**Why it's high-priority:** Direct hit for the rare-disease
diagnostic-yield sub-thread. Complements Ma et al. long-read RNA-seq
below — Fu = DNA long-read, Ma = RNA long-read, same lab-workflow
generation.

**What to read the paper for:** (a) per-trio cost vs. short-read
trio-WGS; (b) diagnostic-yield uplift for previously-unsolved trios
(critical); (c) which variant classes drive the uplift — SVs, repeats,
methylation, or de novo detection sensitivity; (d) infrastructure
required (adaptive sequencing needs Nanopore MinION/PromethION real-time
control).

---

### 15. Ma et al. — Long-read RNA sequencing improves isoform and splicing outlier detection in whole blood from rare disease trios (medRxiv 2026)

**Feeds:** Stephen B Montgomery new-related (09-07).

**Threads served:** `Rare disease`; `Variant interpretation (splicing /
RNA evidence for VUS resolution)`.

**What's there:** **Long-read RNA-seq** applied to **whole-blood
rare-disease trios** for **isoform-level and splicing-outlier detection**
— i.e., the RNA-evidence axis for VUS resolution, moved from short-read
DROP/OUTRIDER/FRASER pipelines to long-read.

**Why it's high-priority:** Direct hit for "splicing / RNA evidence
for VUS resolution" — one of the specific bullets under your
`Variant interpretation` thread. Whole-blood accessibility is critical
because most clinical labs cannot do fibroblast RNA-seq at scale.

**What to read the paper for:** (a) diagnostic-yield uplift over
short-read RNA-seq; (b) which gene classes benefit most (large genes
with many isoforms are expected winners); (c) sensitivity/specificity
for pathogenic splicing outliers in known-answer training set; (d)
runtime + cost.

---

### 16. Boceck et al. — aiDIVA: hybrid AI for rare disease diagnostics using evidence-based, machine learning and language models (npj Genomic Medicine 2026)

**Feeds:** Lisa Bastarache 10-new-citations (09-04); Kai Wang
10-new-citations (09-04); Stephen B Montgomery 10-new-citations (09-04).
Triple-feed cross-hit. Authors: Boceck D, Laugwitz L, Sturm M, Bezdan D,
Gschwind A et al.

**Threads served:** `Rare disease` (HPO-based diagnostic benchmarks
sub-thread); `Machine learning for precision health`.

**What's there:** **aiDIVA**, a **hybrid AI** rare-disease diagnostic
tool combining rule/evidence-based logic + ML + LM components. This is
in the same family as PhenoGPT2 / Exomiser-plus-LLM / Phen2Gene — but
the "hybrid" framing suggests the authors have separated evidence
retrieval (transparent) from ML/LLM ranking (opaque), which is exactly
the GraphRareBench observation that Hit@10 hides the "ranking of
confounders" problem.

**Why it's high-priority:** Direct hit for the auditable-HPO-driven
diagnostic-benchmarks sub-thread you added under `Rare disease` — the
GraphRareBench framing you want propagated across the Phen2Gene /
LIRICAL / Exomiser / PhenoGPT2 benchmarking axis.

**What to read the paper for:** (a) separable metrics for ranking vs.
evidence coverage; (b) benchmark head-to-head against PhenoGPT2 and
Phen2Gene on a shared test set; (c) reproducibility infrastructure
(code + weights, or paper-only).

---

### 17. Brunello et al. — GenPhenia: using deep neural networks to accelerate rare-disease diagnosis (Human Genomics 2026)

**Feeds:** Lisa Bastarache new-related (09-07). Authors: Brunello FG,
Colangelo G, Rius A, Erra L, Lugones AC et al.

**Threads served:** `Rare disease` (HPO-based diagnostic benchmarks).

**What's there:** **GenPhenia**, a deep-NN HPO-based rare-disease
diagnostic tool. Latin-American authorship (Argentina/Chile lineage) —
notable because the training/validation cohort may include
underrepresented ancestry cases.

**Why it's high-priority:** Same sub-thread as aiDIVA/Boceck; treat
these two as head-to-head competitor benchmarks worth reading together.

**What to read the paper for:** (a) architecture — GNN over HPO ontology
vs. transformer over phenotype-term sequences vs. Phen2Gene-style
term-weighting; (b) test set — CAGI-style shared, or bespoke; (c)
whether it reports per-ancestry accuracy (this would be a differentiator
vs. Anglo-centric Phen2Gene benchmarks).

---

### 18. Galderisi et al. — Continuous glucose monitoring to track metabolic changes in youths with cystic fibrosis before and after initiation of elexacaftor/tezacaftor/ivacaftor (2026)

**Feeds:** Patrick Ryan new-related (09-04). Authors: Galderisi A,
Marchiori H, Weiss L, A [truncated]. Likely Padua CF centre + US
CF endocrinology collaborators.

**Threads served:** `Specific disease threads → CF / CFTR`; adjacent
to CFTR-modulator pharmacoepi.

**What's there:** **Continuous glucose monitoring (CGM)** in **CF
youth** before and after **elexacaftor/tezacaftor/ivacaftor (Trikafta)**
initiation — quantifies metabolic (glucose-tolerance) changes on ETI.
CFRD (CF-related diabetes) is a major long-term CF morbidity; whether
ETI blunts or accelerates it is unresolved and the CGM-endpoint design
is the sensitive-endpoint alternative to HbA1c or OGTT.

**Why it's high-priority:** Direct hit for the CFTR-modulator
pharmacoepi thread with a mechanistically-interpretable endpoint (CGM
metrics — time-in-range, glucose variability, dawn phenomenon) rather
than the coarser "diagnosed CFRD" phecode endpoint. Bridges pharmacoepi
to real-world modulator effectiveness.

**What to read the paper for:** (a) direction and magnitude of glucose
change; (b) whether the design is a within-subject pre/post or a
matched-cohort comparison; (c) baseline pancreatic-sufficiency status
of the cohort (this stratifies expected response strongly).

---

### 19. Aguilar-Ordoñez et al. — Whole genome sequencing of 1,427 Mexican individuals from the oriGen cohort (Nature Communications 2026)

**Feeds:** Joshua C. Denny 10-new-citations (09-09). Latin-American
population-genomics reference.

**Threads served:** `Biobanks with EHR linkage` (oriGen is
building-toward EHR-linked); `Genetic epidemiology` (cross-ancestry
portability reference set).

**What's there:** **oriGen cohort** — 1,427 Mexican-ancestry WGS. This
is a mid-scale ancestry-underrepresented reference cohort. Latin-American
allele-frequency coverage has historically been the biggest gap in
gnomAD; MXL and PEL 1000G reference are underpowered compared to CEU/YRI.
oriGen extends what SIGMA / MexOMICS / HCHS-SOL did in the exome era to
WGS.

**Why it's high-priority:** Cross-ancestry portability without a Mexican
reference is not really possible. Any AoU-Hispanic-ancestry PheWAS or
PGS-portability analysis benefits from oriGen allele-frequency support.
Pairs with the Acharya et al. tri-biobank ASCVD paper from last window.

**What to read the paper for:** (a) admixture composition of the cohort
(NAT / EUR / AFR proportions); (b) novel variants relative to gnomAD;
(c) any medically-actionable-gene analysis at the ACMG SF list; (d)
data-access / dbGaP / GEUVADIS-style release.

---

### 20. Garg et al. — Genetic and Clinical Determinants of Variation in Drug Response in Type 2 Diabetes: Insights From the Scottish and UK Biobank Cohorts (Diabetes 2026)

**Feeds:** `UK Biobank` keyword feed (09-06). Authors: Garg S, Kitchen R,
Gupta R, Donnelly L, Pearson ER (Dundee — the DIRECT / MASTERMIND
lineage of T2D-pharmacogenomics).

**Threads served:** `Causal inference and pharmacoepidemiology`
(specifically the pharmacogenomic-modifier-of-medication-persistence
sub-thread); overlaps GLP-1 / SGLT2 drug-class threads; `Biobanks with
EHR linkage` (UKB + Scottish record-linkage).

**What's there:** Genetic and clinical determinants of **T2D drug
response** in **Scottish (SDRN/SCI-Diabetes)** and **UK Biobank**
cohorts. The Pearson lab has anchored T2D pharmacogenomics for a decade
(SLC22A1/metformin, ATM/metformin, PPARγ/pioglitazone); this appears to
be their latest integrative sweep.

**Why it's high-priority:** Direct hit for the PGx-modifier-of-medication-persistence
sub-thread you added, with T2D drugs which overlap GLP-1 / SGLT2 /
metformin.

**What to read the paper for:** (a) which drug-response phenotype
(HbA1c-drop, weight change, treatment persistence, or discontinuation);
(b) whether both PGS and single-variant PGx variants are modelled
jointly; (c) any AoU replication (unlikely but the Pearson lab has been
building AoU-collaboration links); (d) implications for
prescribing-decision-support.

---

### 21. Snel & Schulz — Attributing Cohen's d: Training Data Attribution for Disease-Related Effects in Normative Age Biomarkers (arXiv 2609.07729 2026)

**Feeds:** arxiv-digest 2026-09-09 local run. Score 2 (uk biobank,
biobank).

**Threads served:** `Machine learning for precision health` (biomarker
attribution); `Biobanks with EHR linkage → UK Biobank`.

**What's there:** Training-data attribution (TDA) applied to **Cohen's
d** — the effect-size gap between healthy training and case-control
held-out — rather than to prediction-level loss. Closed-form influence
functional validated against LOO retraining, ranks training samples by
their effect on held-out case-control separation. **Applied to 4
diseases × 2 biomarker modalities in UKB**; removing the top-10% most
influential training samples doubles the metabolomic-age effect for
type-2 diabetes and raises brain-age effect for MS by ~1/3. Flagged
samples carry subclinical cardiometabolic burden invisible to
diagnosis-based exclusion. Released as `pyinfluence` package.

**Why it's high-priority:** UKB-anchored + biomarker-composite + audit
framing. The influence-function-on-effect-size (rather than on loss)
trick is directly portable to PheRS / PRS training-cohort composition
audits — "which of the healthy-cohort exemplars are dragging the
composite score toward or away from the case group?" This is the
disease-effect-size version of the scContam / MIA-scFM pretraining-audit
protocols you flagged for CLMBR/MOTOR/MEDS benchmark contamination.

**What to read the paper for:** (a) which four diseases and which two
biomarker modalities (metabolomic-age + brain-age are the two mentioned);
(b) computational cost of the influence functional at UKB scale; (c)
whether the same subjects are flagged across modalities (a joint
audit-target hypothesis); (d) pyinfluence API and reproducibility.

---

### 22. W. Zhang et al. — Benchmarking Bayesian Colocalization Methods in Validating Mendelian Randomization-identified Targets (Genomics Proteomics & Bioinformatics 2026)

**Feeds:** Jian Yang new-related (09-09). Authors: Zhang W, Yoshiji S,
Sladek R, Dupuis J, Lu T.

**Threads served:** `Genetic epidemiology` (specifically drug-target-MR-triangulated-with-observational);
methods for MR validation.

**What's there:** **Benchmarking of Bayesian colocalization methods**
(likely coloc, coloc-SuSiE, HyPrColoc, mrlocus) as **validation layers
for MR-identified targets**. Yoshiji is McGill drug-target-MR
lineage; the Saxby metformin × AAA drug-target MR you flagged is in
this family.

**Why it's high-priority:** Direct hit for the drug-target-MR-triangulated-with-observational
sub-thread you added under `Genetic epidemiology`. MR-alone is often
picked apart by pleiotropy and window-selection choices; colocalization
is the standard "is this really the same causal variant?" adjudication
step. A benchmark tells you which colocalization method to trust for
which MR configuration.

**What to read the paper for:** (a) which coloc method wins under which
LD architecture; (b) sample-size sensitivity — do MR-based drug-target
studies still colocalize at N=50k eQTL discovery, or do you need
N=500k+; (c) implications for MR-Alasso / MR-Bayes / MR-Egger
downstream.

---

## METHODS-WATCH detail (brief)

### Yu et al. — Location-invariant estimator of extremal quantile treatment effects for heavy-tailed distributions (arXiv 2609.04018 2026)

Adapts the location-invariant Fraga EVI estimator to the causal setting
via IPW, then uses a difference-based extrapolation scheme so that
extremal QTE is location-invariant. Consistency + asymptotic normality
proved; simulation study only. **Portable to** biomarker-tail HTE work
(quantile treatment effects on extreme biomarker changes — HbA1c, LDL,
BP tails).

### Rajabli & Collins — Generalizable feature extractor for Alzheimer's-related brain-MRI tasks (arXiv 2609.05400 2026)

A **7.18 M-parameter 3D CNN** trained for brain-age prediction is
**frozen and adapted via LoRA** (~1% additional trainable parameters)
across 6 downstream Alzheimer's tasks, achieving cross-cohort transfer
(ADNI → OASIS-3 AUC 0.87 with no retraining). **Portable to** the
compact-EHR-FM-plus-LoRA design pattern for structured-EHR CLMBR-style
models, and demonstrates that small-supervised-pretrained-then-LoRA
sometimes beats U-Net direct training.

### Chen Q et al. — Oral Anticoagulants in AF + Advanced CKD Not Requiring Dialysis (JAMA Netw Open 2026)

Hernán-adjacent RWE / pharmacoepi design. Not on tracked drug classes,
but the AF-CKD confounder architecture is a template you can borrow
for other decision-making studies in specific-population strata.

### Zhou et al. — Long-term cardiorenal illness trajectories after antihypertensives × ADHD (Hripcsak citations 09-04)

Large-cohort pharmacoepi with a psychiatric-comorbidity stratifier; the
"medication class × comorbidity" design is a portable template.

### Bai et al. — Relation-aware multimodal KG for DDI prediction (Sci Rep 2026, Hripcsak citations 09-07)

Multimodal KG-based DDI. Complements DKL / PLRA-KG from prior windows.

### Ong et al. — Cardiometabolic phenotyping from wearable monitoring (Chenjie Zeng new-related 09-06)

Wearable-derived cardiometabolic subtyping; adjacent to your
`Chronic disease clustering and multimorbidity` thread but with a
sensor-first rather than EHR-first framing.

### Loay et al. — Mutation rate heterogeneity biases variant effect prediction (AJHG 2026, Karczewski citations 09-07)

Fundamental variant-interpretation methods paper; worth reading for
any downstream PS3 / PP3 code use.

### Yao et al. — CHIP and atherosclerotic cardiovascular disease review (2026)

Thread-anchor review for CHIP → ASCVD literature; use for
citation-graph seeding of the CHIP thread rather than primary methods.

---

## Cross-thread patterns worth naming

**Pattern 1 — TTE + RWD + repurposing has hit critical mass.** Wu et al.
ADRD (5-feed hit) + Ju et al. UDCA-PD + Perée et al. IBD-entrectinib
show three separate teams landing repurposing-through-causal-inference
papers in the same 10-day window. The generic scaffold is: (i)
gene/eQTL/target link → (ii) TTE emulation in EHR/RWD → (iii)
colocalization / MR triangulation. The W. Zhang colocalization
benchmark and the Roberts polygenic-pharmacotherapy evidence map are
the methods scaffolds this scaffold rests on. **Actionable**: this is
the shape of the CFTR-modulator-repurposing narrative you can build
next — pick a CFTR-adjacent indication (bronchiectasis? COPD? primary
ciliary dyskinesia?), run the TTE on AoU or MyCode, colocalize.

**Pattern 2 — HPO-based rare-disease diagnostic benchmarks are
converging on the aiDIVA / GenPhenia / PhenoGPT2 axis.** aiDIVA
(triple-feed hit) and GenPhenia both surfaced in the same window; both
sit alongside Phen2Gene / LIRICAL / Exomiser / PhenoGPT2. The
GraphRareBench observation you already flagged — Hit@10 hides the
"ranking-of-confounders" problem — should be the audit lens applied to
this whole family. **Actionable**: a small write-up that benchmarks
aiDIVA + GenPhenia + PhenoGPT2 on the GraphRareBench separable-metrics
scheme is a low-cost paper.

**Pattern 3 — OMOP-CDM tooling is professionalizing at the audit layer.**
Syrona (Pajusalu, this window) + CohortContrast (Ilves, last window) +
the Bhattacharjee African-mental-health migration are three snapshots of
the same shift — from "get data into OMOP" to "audit what OMOP
representation choices do to downstream analyses." This is the
`Fidelity, portability, and audit of representations` sub-thread going
mainstream. **Actionable**: pin Syrona for your next AoU-vs-BioVU
representation audit; it may be plug-and-play.

**Pattern 4 — PGS-composite-risk + GxE are moving from framework to
empirical result.** DeVito & Gymrek (PGS × spatiotemporal × nongenetic)
+ Park et al. (cross-ancestry cross-disorder OCD PRS) + Jandu et al.
(inherited inflammation liability as broad-phenome PheRS) all show up
in this window. Combined with the Baya / Souaiaia / Vazquez tails-and-residuals
taxonomy you had already flagged, the PGS-tails-and-residuals discovery
lens now has both methods papers and empirical demonstrations. **Actionable**:
this is a coherent seminar / lab-meeting topic — three papers, one
narrative arc.

---

## Housekeeping / next actions

1. **Follow-up on Wu et al. ADRD repurposing TTE.** Pull the full text
   and check whether the decentralised-RWD pipeline references OHDSI
   network federation or a TriNetX-style construct. If OHDSI-federated,
   consider whether the same federated pattern is portable to your
   CFTR-modulator persistence study.

2. **Add Syrona to the AoU-vs-BioVU audit toolkit.** After reading the
   Pajusalu paper, if the tool covers all five OMOP domains you care
   about (condition / drug / measurement / observation / procedure),
   pin it as the default pairwise-comparison lens for the
   `representation portability under site shift` sub-thread.

3. **Add Somatic Mosaicism Network map + Fu et al. long-read trio to
   the CHIP/VEXAS/LOY + rare-disease reference reading list.** Both
   are reference-dataset papers everyone in these threads will cite for
   the next year.

4. **Update INTERESTS.md?** No structural update needed — every HIGH
   item this window fits an existing thread. The `Drug repurposing
   via TTE-on-EHR/RWD` sub-thread is now saturated enough that it may
   deserve its own explicit bullet under `Drug repurposing` (currently
   captured as "causal-inference framings of off-label use"). Consider
   a one-line edit to name-check "TTE-on-decentralised-RWD" the same
   way you name-check MR-triangulation.

5. **No `arxiv-digest` GitHub-email traffic in the window.** Same
   pattern as last window — the pipeline commits to this repo rather
   than emailing notifications, so the on-disk digests are the feed.
   The `seen.json` guard is doing its job (many of the near-empty daily
   digests are "0 new, N previously surfaced, suppressed").
