# Research digest report — 2026-09-18

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-18 12:40Z** (~17 days since the
2026-09-01 research-digest report, covering fourteen arxiv-digest cron
runs and roughly a dozen Google Scholar alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-02.md` → `2026-09-17.md`) | 09-02 → 09-17 daily crons | 14 daily runs. Dry days (0 or de-dup only): 09-03, 09-05, 09-06, 09-08, 09-12; also missing files for 09-13/09-14/09-15 (weekend + a Monday no-file gap). 09-02: 1 paper (Ramesh mudskipper locomotion — off-thread noise). 09-04: 2 papers (Cortez-Rodriguez natural-disasters × nonprofits panel causal, Yu et al. location-invariant extremal QTE). 09-07: 1 paper (Rajabli compact AD-MRI foundation model with LoRA). 09-09: 2 papers (Snel & Schulz pyinfluence Cohen's-d attribution on UKB, Wu FUSE-RT chromatography FM). 09-10: 1 paper (Lee et al. Kalman-filter HT surveillance). 09-11: 3 papers (Devarakonda scDEFT IBD atlas drug-effect + patient stratification, Hendrix geospatial FMs augment social-risk indices, Semchin connectome-constrained Parkinson subtypes). 09-16: 2 papers (Wang et al. CF NTM mucus-rheology multiscale model, Zhang scKITE knowledge-enhanced single-cell FM). 09-17: 1 paper (Fujita & Hattori Information Set Emulation — causal certificates for AI-derived EHR features). |
| No `arxiv-digest` email hits from GitHub | — | Same as prior windows: search of `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads. The pipeline commits its output to this repo rather than emailing notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-17 batches, 05:47Z + 10:48Z) | 09-17 | Very heavy batch. ~15 author feeds + 12 keyword feeds fired. Author-feed HIGH items: **Denny + Bastarache + Jian Yang + Karczewski citations-to** all landed the same Walker et al. medRxiv AoU + Pharmlines antidepressant PGS-persistence paper (a quadruple hit is unusual and a strong signal for the pharmacogenomic-modifier-of-medication-persistence sub-thread). Denny new-related also landed **Zheng et al. medRxiv** PGS-vs-proteomic risk-score divergence in neurodegenerative disease + **Bal et al. Nature Cardiovasc** multiancestry HCM PGS + **Chen et al. Nature** cell-type-specific eQTLs. Chenjie-Zeng (self) new-related landed **O'Malley et al. J Cystic Fibrosis** CFTR-modulator × pancreatic-cancer signaling. Hripcsak citations-to landed **Y Wang 2026** digital-twin mechanistic-model methodological pipelines. Keyword-feed HIGH items: `"UK Biobank"` **Zhou et al.** T2D operational-definition sensitivity + **Tsuo et al. Nature Genetics** AoU-scale PRS diversity paper; `"All of Us research program"` also flags Tsuo et al. + **Krueger 2026** AoU multi-ancestral plasma-proteome fine-mapping + Jiang et al. arXiv opioid-use-disorder survey-augmented AoU prediction; `intitle:"clonal hematopoiesis"` **Chien & Garcia-Manero Cancer** CHIP clinical-management review; `APOL1` Huang et al. AJP-Renal IFN-induced APOL1 podocyte regulation. |
| Google Scholar alerts (09-15/09-16 batches, 17:30Z / 06:34Z) | 09-15 → 09-16 | 10+ feeds fired. Notable: **Hripcsak citations-to (8 new)** led with Branigan et al. cardiorenal GLP-1RA vs. SGLT2i systematic review — plus Krueger PWAS multi-ancestral (AoU) via `"All of Us"` keyword feed and Yang et al. UKB PA-timing hypertension via `"UK Biobank"` feed. **Mihaela van der Schaar new-articles** on 09-15 (Jones et al. UK-wide DCE for AI-based skin-cancer detection — off-thread but tracks). |
| Google Scholar alerts (09-09 batches, 16:04Z + 22:32Z) | 09-09 | 20+ feeds fired. Two dominant results: (a) **Wu, Li, Lei, Zhou, Tang, Zhang, Lu et al.** *Discovering Repurposable Drugs for Alzheimer's Disease and Related Dementias: Target Trial Emulation Using Decentralised Real-World Data* — landed simultaneously on **Yong Chen, Patrick Ryan, and Hripcsak citations-to** feeds; a triple hit is a strong signal for the drug-repurposing thread. (b) **Ju, Schrag, Carroll et al.** *Ursodeoxycholic Acid and Parkinson's Disease Risk: An Emulated Target Trial in UK EHRs* — landed on both `"electronic health records"` and `Foundation models + "electronic health records"` keyword feeds. **Bellucci, Gu, Rose, Baranzini** *An Agentic AI Framework Connecting Language Models to Electronic Health Records and a Biomedical Knowledge Graph for Real-World Evidence* — via Zhiyong Lu new-related; direct-hit for the agentic-observational-causal-inference sub-thread added in 07-29. **Ellershaw et al. Foresight-England** re-surfaced on Pascal Brandt new-related for backfill. Also fired: Chen et al. *JAMA Netw Open* AF-and-advanced-CKD anticoagulant TTE (Hernán); Fu et al. *Nat Commun* trio-barcoded adaptive sequencing for rare disease (Montgomery + Kai Wang); Zhou et al. STAR Protocols cross-ancestry local-ancestry PGS protocol (Denny); Aguilar-Ordoñez et al. Nat Commun oriGen 1,427-genome Mexican WGS (Denny). |
| Google Scholar alerts (09-01 → 09-08 batches) | 09-01 → 09-08 | Rolling low-volume days between the 09-01 and 09-09 pushes; nothing HIGH surfaced that isn't already captured under the 09-01 report or subsumed by the 09-09 + 09-17 batches. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Roughly fifteen HIGH items surfaced this window, clustering into six knots:

**Biobank-scale PRS methodology (2 items, one landmark).** Tsuo, Shi, Ge,
Mandla, Hou, Ding et al. *Nature Genetics* 2026 — **"All of Us diversity
and scale yield context-dependent improvements in polygenic prediction"**
— develops multiancestry PRSs for 32 traits and diseases using 245,388
whole-genome sequences from the **AoU Research Program** together with
UK Biobank data, and evaluates how ancestry, methodology, and genetic
architecture jointly determine when combining biobanks helps vs. hurts.
The framing sentence — "maximizing sample size by meta-analyzing AoU and
UKB was not universally optimal" — is the paper's *portable* finding, and
it is a direct hit for your `Biobanks with EHR linkage` and `Genetic
epidemiology → PGS × ancestry` threads. Complemented by **Zhou, Yolou,
Xie, Zhao** *STAR Protocols* 2026 — a **local-ancestry-plus-cross-ancestry
protocol for PGS in admixed populations** — as the methods-recipe
companion.

**Pharmacogenomic modifier of medication persistence (1 item, quadruple
hit).** Walker, Wang, Bos, Lin, Klont, Nolte et al. **medRxiv 2026** —
*Polygenic and familial contributions to antidepressant continuation,
switching, discontinuation and augmentation in the All of Us and Pharmlines
cohorts* — landed simultaneously on the **Denny + Bastarache + Jian Yang
+ Karczewski** new-related feeds (a quadruple hit is unusual and a strong
signal). This is a **direct-hit paper for the pharmacogenomic-modifier-of-
medication-persistence sub-thread** that INTERESTS.md added in 07-29:
polygenic vs. familial contributions decomposed against a
continuation/switching/discontinuation/augmentation outcome family, in the
exact two-cohort AoU + Pharmlines setup that the Cohen et al.
*Pharmaceuticals* 2026 CYP2D6 × persistence paper was pointing toward.

**Drug repurposing via TTE + decentralised RWE (2 items, one landmark).**
Wu, Li, Lei, Zhou, Tang, Zhang, Lu et al. 2026 — **"Discovering
Repurposable Drugs for Alzheimer's Disease and Related Dementias: Target
Trial Emulation Using Decentralised Real-World Data"** — landed on
**Yong Chen + Patrick Ryan + Hripcsak citations-to** feeds; a triple hit,
plus a fourth surface from a Nick-Furlotte-adjacent search. Direct hit
for `Drug repurposing → causal-inference framings of off-label use
(target-trial emulation of repurposing candidates)` AND for `Causal
inference and pharmacoepi → Federated / privacy-preserving EHR causal
analytics` (the decentralised-RWE architecture is the federated
substrate). Ju, Schrag, Carroll, Xiong et al. **medRxiv 2026** —
*Ursodeoxycholic acid and Parkinson's Disease Risk: An Emulated Target
Trial in UK EHRs* — the disease-specific instance of the same pattern
(TTE + drug repurposing, this time in UK primary-care EHR data), and a
direct-hit for the disease-adjacent Parkinson watch under `Drug
repurposing → EHR-based repurposing signals`.

**PGS × proteomics + composite-risk framing (2 items).** Zheng,
Shivakumar, Shen, Kim **medRxiv 2026** (Denny new-related) — *Absorption
and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores
Diverge in Neurodegenerative Diseases* — quantifies **overlap vs.
complementarity** between polygenic and proteomic risk scores across
neurodegenerative disease, using absorption + co-expression modules as
the analytic lens; direct hit for `Genetic epidemiology →
Multi-omics-augmented PRS` AND for `Composite risk models stacking PRS
with rare pathogenic variants` (proteomics slots into the same
"stack-on-PRS" architecture that the You et al. 2023 UKB Olink+PRS paper
established for AD). Krueger 2026 — *Genetic Fine-Mapping of the Plasma
Proteome Across Multi-Ancestral Populations* — PWAS in 10 cardiometabolic
phenotypes within the AoU Research Program, positioned as the multi-
ancestral counterpart to UKB Olink PWAS; a natural companion paper for
Zheng et al. and for the Kurniansyah *Nat Genet* AD-PRS paper from the
09-01 report.

**Multiancestry-PGS-for-disease-stratification cluster (1 item).** Bal,
Pampana, Nayak, Gaonkar, Patel et al. *Nature Cardiovascular Research*
2026 — **"A multiancestry polygenic risk score improves stratification
in patients with hypertrophic cardiomyopathy"**. HCM has classically been
framed as Mendelian (SARC-HCM-P/LP explains ~one-third of cases), so the
multiancestry-PGS-as-modifier design is the exact **composite risk model
stacking PRS with rare pathogenic variants** pattern your INTERESTS.md
prioritizes — the same shape as Fahed 2020 monogenic-vs-polygenic CAD,
now in HCM.

**EHR foundation-model + auditable-representation cluster (3 items).**
Fujita & Hattori **arXiv 2609.17777, 2026** (surfaced via local
arxiv-digest 09-17 cron; score 3, keyword hits `electronic health
records + inverse probability + causal inference`) — *Information Set
Emulation: Causal Certificates for AI-Derived EHR Features*. Introduces
**causal certificates** as an auditable-representation layer that
attaches source evidence, clinical + recording times, decision-time
availability, representation version, and proposed causal roles to
AI-extracted EHR features under a locked target trial. Direct hit for
`Knowledge representation in EHRs → Fidelity, portability, and audit of
representations` AND for `Causal inference & pharmacoepi`. Bellucci, Gu,
Rose, Baranzini *Frontiers* 2026 (Zhiyong Lu new-related) — *An Agentic
AI Framework Connecting Language Models to Electronic Health Records and
a Biomedical Knowledge Graph for Real-World Evidence*. Direct hit for
the `Agentic / human-in-the-loop observational-causal-inference
pipelines` sub-thread you added in 07-29 (oci-agent lineage), and for
the `Knowledge graphs & ontologies × EHR` intersection. Snel & Schulz
**arXiv 2609.07729, 2026** (local arxiv-digest 09-09) — *Attributing
Cohen's d: Training Data Attribution for Disease-Related Effects in
Normative Age Biomarkers*. Closed-form influence functional for Cohen's
d — an interpretable **auditable-attribution** tool for UKB biomarker
models. Chen et al. *Nature* 2026 (Denny new-related) — *Cell-type-
specific eQTLs underlie the genetic architecture of complex traits* — is
the ancillary landmark paper that pairs with all three by giving the
gene-regulatory substrate that eQTL-aware EHR-FM representations should
be evaluated against.

**Disease-specific hits (3 items).** O'Malley, Keen, Thornell, Campbell,
Prouty et al. *Journal of Cystic Fibrosis* 2026 (Chenjie-Zeng self
new-related) — *CFTR modulation alters pancreatic cancer cell growth and
signaling: implications for cancer risk in cystic fibrosis*. Direct hit
for the **CF / CFTR** disease thread and specifically for the
modulator-eligibility / long-term-outcomes sub-thread (elexacaftor-
tezacaftor-ivacaftor is named), because pancreatic-cancer risk under
modulator therapy is exactly the kind of downstream signal that a CFTR
modulator-persistence pharmacoepi TTE would want to interrogate. Wang,
Konstantinopoulos, Kuo, Cai, Wei, Pienaar, Hao **arXiv 2609.15584, 2026**
(local arxiv-digest 09-16) — multiscale ABM + PDE for **non-tuberculous
mycobacterial (NTM) infection in cystic fibrosis** with explicit
mucociliary-clearance + mucus-rheology mechanisms; a bench-modeling
companion to the O'Malley paper for the same CF disease thread, and its
framing points at **patient-specific digital twins for CF pulmonary
infection** as an aspirational target (matches the Ideker / Zhang /
Oermann 2026 *Cell* digital-twin consortium sub-thread). Chien & Garcia-
Manero *Cancer* 2026 (CHIP keyword feed) — *Clinical management of
clonal hematopoiesis*. Direct hit for the **CHIP / VEXAS / LOY somatic
mosaicism** disease thread; a clinical-management review that closes a
gap in the 09-01 report where the CHIP / LOY thread had only mechanistic
papers.

**Additional single-thread hits worth naming.** Zhou, Han, Beulens,
Ahmadizar *Diabetes Research and Clinical Practice* 2026 (`"UK Biobank"`
keyword feed) — **five T2D definition families in 501,936 UKB
participants** show that operational definitions of T2D materially shift
case composition, diagnosis timing, polygenic profiles, and outcome
associations. Direct hit for `EHR phenotyping & OMOP` (definitional
sensitivity) AND for `Biobanks with EHR linkage` (as a template for T2D
in AoU / MVP / BioVU). Y Wang 2026 (Hripcsak citations-to) —
*Methodological Pipelines for Digital Twin Mechanistic Model Parameter
Estimation, Forecasts, Interpretation, and Translation to Enhance Next-
Generation Clinical Care* — one of two digital-twin methodology hits in
this window (the other is the CF one above); reinforces that the
`Digital twins from EHR data` sub-thread you added in 07-29 is now the
default paradigm in the papers *citing* the OMOP + Foundation-model
literature. Devarakonda **arXiv 2609.10831, 2026** (local arxiv-digest
09-11) — **scDEFT**: drug-conditioned single-cell latents on a harmonized
**inflammatory bowel disease atlas of 1.16 million cells** across three
cohorts and two drug classes; stratifies responders before treatment at
AUROC 0.70 with mechanistic-interpretable driver ranking. Direct hit for
the **IBD** disease thread AND for `ML for precision health → HTE tied
to clinical decision`.

---

## Detailed reports — HIGH-priority studies

Papers below are the ones I would open next; each note gives (a) the
core method or claim, (b) why it maps to a research thread, and (c)
what to compare it against in the existing literature you track.

### 1. Tsuo, Shi, Ge, Mandla, Hou, Ding et al. — *All of Us Diversity and Scale Yield Context-Dependent Improvements in Polygenic Prediction*
**Venue:** *Nature Genetics*, 2026.
**Surfaced via:** Google Scholar alerts `"UK Biobank"` keyword feed AND `"All of Us research program"` keyword feed (09-17, 10:48Z; dual-keyword hit is a signal).
**Threads:** Biobanks with EHR linkage (AoU + UKB); Genetic epidemiology → PGS × ancestry AND cross-ancestry portability; ML for precision health.

**What it is (from alert snippet).** Develops **multiancestry PRSs for
32 traits and diseases** using **245,388 whole-genome sequences** from
the AoU Research Program together with UK Biobank data. Evaluates how
ancestry, methodology, and genetic architecture jointly determine when
combining the two biobanks helps vs. hurts. The framing sentence carries
the paper's most portable claim: "maximizing sample size by meta-analyzing
AoU and UKB was not universally optimal" — i.e., for some traits and some
ancestries, single-biobank PRS beats the meta-analytic PRS, and the paper
provides a **context-dependent decision rule** for which is preferred.

**Why it matters for your work.** This is the biobank-scale PRS methods
paper the field has been waiting for, and it settles a question that
INTERESTS.md's `PGS × ancestry` and `cross-ancestry portability` sub-
threads have been circling since the 07-29 update. Three concrete uses:
(a) it is the citation-ready reference for any AoU-PRS or AoU-plus-UKB
PRS methods argument in your own future manuscripts; (b) the 32-trait
scan is a template for a **PheRS-analog trans-ancestry portability
audit** that could ride on top of your composite-risk stacking work; and
(c) it pairs directly with Kurniansyah *Nat Genet* AD-PRS (09-01 report,
Bastarache feed) — Kurniansyah is the single-disease APOE-independent
multiancestry PGS; Tsuo is the pan-trait methods paper. Add to your
methods-portable checklist and use as the reference for "when to combine
biobanks."

**Contrast against:** Kurniansyah *Nat Genet* 2026 multiancestry AD-PRS
(09-01 report); the Genome-wide PRS Portfolio (Wang / Kanai / Martin
2020 lineage) as the baseline; the Zhou / Yolou / Xie / Zhao *STAR
Protocols* 2026 local-ancestry protocol below as the methods-recipe
companion; Acharya cross-biobank ASCVD heritability (09-01 report) as
the harmonized-outcome sibling.

---

### 2. Walker, Wang, Bos, Lin, Klont, Nolte et al. — *Polygenic and Familial Contributions to Antidepressant Continuation, Switching, Discontinuation and Augmentation in the All of Us and Pharmlines Cohorts*
**Venue:** medRxiv 2026 (posted 2026-08-24, doi 10.1101/2026.08.14.26360458).
**Surfaced via:** Google Scholar alerts **Denny + Bastarache + Jian Yang + Karczewski** new-related feeds (all 09-17, 05:47Z). Quadruple new-related hit; unusual and diagnostic.
**Threads:** Pharmacogenomic modifier of medication persistence (the 07-29 sub-thread INTERESTS.md prioritizes); Causal inference and pharmacoepi; Biobanks with EHR linkage (AoU); Genetic epidemiology → PRS.

**What it is (from abstract snippet).** Predicting antidepressant
response has been a long-running challenge, and it is unclear whether
reported polygenic associations reflect **drug-specific non-response**
or a **broader propensity for treatment modification**. This study
decomposes polygenic and familial contributions across four adjacent
outcomes — continuation, switching, discontinuation, augmentation — in
two cohorts: **AoU** (US biobank, EHR-linked) and **Pharmlines**
(Netherlands, pharmacy + biobank linkage). The decomposition disentangles
the drug-specific from the general-modification component.

**Why it matters for your work.** This is the exact study your 07-29
`Pharmacogenomic modifiers of medication persistence` sub-thread was
written to catch. The Cohen et al. *Pharmaceuticals* 2026 CYP2D6 ×
persistence paper (which INTERESTS.md cites as the anchor) is
single-gene-Pharmlines-lineage; Walker et al. is the **polygenic**
generalization on top of AoU + Pharmlines, with a four-outcome family
that mirrors the MPR / discontinuation / augmentation vocabulary you use
elsewhere. Portable to CFTR-modulator persistence, statin
discontinuation, HRT persistence, GLP-1 RA persistence. The
quadruple-alert hit (Denny + Bastarache + Karczewski + Jian Yang all
picked it up on the same 09-17 batch) is unusual and suggests the paper
sits at the intersection of PheWAS-infrastructure + EHR + rare-variant-
adjacent + PRS communities, which is exactly your working intersection.

**Contrast against:** Cohen et al. *Pharmaceuticals* 2026 CYP2D6 ×
persistence (single-gene, Pharmlines-lineage); Psy-PGx UKB lineage (the
INTERESTS.md-cited anchor); the Roberts et al. *IJPRAS* 2026 polygenic-
pharmacotherapy evidence-map review (also on the same Denny feed) as
the framing-review companion.

---

### 3. Wu, Li, Lei, Zhou, Tang, Zhang, Lu et al. — *Discovering Repurposable Drugs for Alzheimer's Disease and Related Dementias: Target Trial Emulation Using Decentralised Real-World Data*
**Venue:** likely medRxiv → *JAMA Netw Open* or *Nat Med* trajectory (venue withheld in the alert snippet; landing on Chen + Ryan + Hripcsak lineage suggests OHDSI-house).
**Surfaced via:** Google Scholar alerts **Yong Chen + Patrick Ryan + George Hripcsak** citations-to feeds simultaneously (all 09-09, 16:04Z). Triple hit is a strong signal.
**Threads:** Drug repurposing → causal-inference framings of off-label use (TTE of repurposing candidates); Causal inference and pharmacoepi (TTE); Federated / privacy-preserving EHR causal analytics (decentralised RWE = federated substrate); Chronic disease clustering (dementia).

**What it is (from alert snippet).** Uses **decentralised real-world
data** to run **target trial emulation** for candidate drugs that could
be repurposed for AD and related dementias. The "decentralised RWE"
architecture aligns with the Jang et al. arXiv 2607.17958
distributed-mediation design pattern that INTERESTS.md cites under
`Federated / privacy-preserving EHR causal analytics`. The paper is a
direct entry in the drug-repurposing TTE pipeline framing that Zhao et
al. *arXiv 2026* narrative-framework-for-cancer-immunotherapy (09-01
report) argued was domain-portable — here it is landed in dementia.

**Why it matters for your work.** Three angles hit at once. First,
`Drug repurposing → causal-inference framings of off-label use` gets a
concrete landmark paper for **AD/ADRD**, a disease where repurposing is
active (GLP-1 RA, SGLT2i, statins, and now UDCA all have live TTE
studies). Second, `Federated / privacy-preserving EHR causal analytics`
gets a landmark on the observational-causal side that pairs with the
Burkhart federated GEM 2608.02939 paper on the EHR-FM side. Third, the
triple citations-to hit tells you the paper is being read as canon by
Ryan (OHDSI methods), Hripcsak (OHDSI methods), AND Yong Chen (federated
EHR methods) — three communities you already track.

**Contrast against:** the Wu, Li, Lei et al. team's dementia-TTE lineage
(likely descends from Zhou 2023 CarnegieMellon / Weill Cornell dementia-
repurposing pipeline); Ju et al. UDCA-Parkinson TTE (#4 below) as the
disease-specific instance of the same architecture; Jang et al.
distributed-mediation (INTERESTS.md-cited); Suchard LEGEND-HTN.

---

### 4. Ju, Schrag, Carroll, Xiong et al. — *Ursodeoxycholic Acid and Parkinson's Disease Risk: An Emulated Target Trial in UK Electronic Health Records*
**Venue:** medRxiv preprint, 2026 (in-press per running-title conventions).
**Surfaced via:** Google Scholar alerts `"electronic health records"` keyword feed AND `Foundation models + "electronic health records"` keyword feed (both 09-09, 22:32Z). Dual keyword hit.
**Threads:** Drug repurposing → EHR-based repurposing signals + causal-inference framings of off-label use; Causal inference and pharmacoepi (TTE); EHR phenotyping & OMOP.

**What it is (from alert snippet).** Emulated target trial of
**ursodeoxycholic acid (UDCA)** — a repurposing candidate for **Parkinson's
disease** — using UK EHR data. UDCA has been a translational drug-
repurposing candidate for PD for several years on the basis of
mitochondrial-function preclinical work; this paper takes the next step
into real-world-evidence testing via TTE.

**Why it matters for your work.** Concrete disease instance of the
Wu et al. *AD/ADRD* pattern above (#3), and a template you might reuse
for your own CFTR-modulator or GLP-1 RA repurposing / off-label questions.
The UK EHR base is the same substrate as the Foresight-England EHR-FM
paper from the 09-01 report — meaning the same underlying data resource
now supports both a generative-FM approach and a TTE approach for the
same question class. Also useful as a citation when arguing that
**"EHR-based TTE for repurposing"** has become a defined study design
with a growing peer-reviewed portfolio, not a one-off.

**Contrast against:** Zhang et al. GLP-1/SGLT2/DPP4 empirically-calibrated
TTE (09-01 report) as the "TTE + negative-control-calibration" gold
standard; Wu et al. AD/ADRD repurposing TTE (#3 above) as the
decentralised-RWE sibling.

---

### 5. Zheng, Shivakumar, Shen, Kim — *Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases*
**Venue:** medRxiv 2026, 2026-08-24, doi 10.64898/2026.08.24.26361271.
**Surfaced via:** Google Scholar alert "Joshua C. Denny - new related research" (09-17, 05:47Z).
**Threads:** Genetic epidemiology → Multi-omics-augmented PRS; Composite risk models stacking PRS with rare pathogenic variants (proteomics-augmented version); Chronic disease clustering (neurodegeneration).

**What it is (from abstract snippet).** Polygenic and proteomic risk
scores are both proposed for **pre-symptomatic stratification**, but the
extent to which they provide **overlapping vs. complementary** information
has not been measured across neurodegenerative disease. The paper
introduces an **absorption + co-expression module** framework to quantify
overlap and localize divergence — which genes / pathways are polygenic-
only, proteomic-only, or shared.

**Why it matters for your work.** This is the multi-omics-augmented PRS
paper the field has been waiting for on the neurodegeneration axis. Your
INTERESTS.md `Multi-omics-augmented PRS` sub-thread names Nightingale NMR
/ Olink proteomics stacking with PGS as a lipid + cardiometabolic +
psychiatric priority; Zheng et al. lands the equivalent framework in
neurodegeneration, which sits under `Chronic disease clustering` in
INTERESTS.md. Also directly serves `Composite risk models stacking PRS
with rare pathogenic variants` — the proteomics-augmented framing is the
same "stack on top of PGS" architecture, with proteomics standing in
for rare variants as the additional layer. Especially valuable in
conjunction with the Kurniansyah *Nat Genet* AD-PRS paper (09-01 report)
which is the APOE-out PRS, and with NetMoint UKB multimodal-trajectory
paper (09-01 report) which is the proteomics-plus-imaging trajectory
framework — Zheng et al. is the bridge that says *where* the two agree
and disagree.

**Contrast against:** You et al. 2023 UKB Olink + PRS composite AD risk;
NetMoint (09-01 report) UKB multimodal proteomics + imaging trajectory
framework; Kurniansyah *Nat Genet* 2026 APOE-out AD-PRS.

---

### 6. Bal, Pampana, Nayak, Gaonkar, Patel et al. — *A Multiancestry Polygenic Risk Score Improves Stratification in Patients with Hypertrophic Cardiomyopathy*
**Venue:** *Nature Cardiovascular Research*, 2026, doi 10.1038/s44161-026-00866-8.
**Surfaced via:** Google Scholar alert "Joshua C. Denny - new related research" (09-17, 05:47Z).
**Threads:** Genetic epidemiology → PGS × ancestry + Composite risk models; Variant interpretation (ACMG / ClinGen); PheWAS / phecode infrastructure → penetrance framing for monogenic variants.

**What it is (from abstract snippet).** Hypertrophic cardiomyopathy (HCM)
has traditionally been considered a Mendelian disease driven by
**pathogenic or likely-pathogenic variants in sarcomere-encoding genes
(SARC-HCM-P/LP)**, but these variants explain only **one-third of cases**.
The paper builds a **multiancestry PGS for HCM** and shows it improves
patient stratification — including within the SARC-negative fraction and
across ancestry groups where standard PGS have historically been
Eurocentric.

**Why it matters for your work.** This is a textbook **composite risk
model stacking PRS with rare pathogenic variants** — exactly the sub-
thread INTERESTS.md prioritizes for `Genetic epidemiology`. The SARC-
HCM-P/LP framing plus multiancestry PGS in the SARC-negative fraction is
the same design shape as Fahed 2020 monogenic-vs-polygenic CAD, the same
"tails-and-residuals" instrument that Baya *AJHG* 2026 "misaligned
individuals" argues is a rare-variant discovery lever, and one of the
first HCM-specific PGS papers to hit *Nature Cardiovascular Research*.
Directly reusable as a template for a **CFTR** or **APOL1** composite-risk
paper. Also relevant to `PheWAS / phecode infrastructure` framing
because the SARC-HCM-P/LP penetrance in the unselected multiancestry
group is a natural population-screening comparator.

**Contrast against:** Fahed 2020 monogenic-vs-polygenic CAD; Kurniansyah
*Nat Genet* 2026 multiancestry AD-PRS (09-01 report); the RYR1/CACNA1S
malignant-hyperthermia paper (09-01 report) as the pharmacogenetic
sibling to a monogenic-plus-modifier framing.

---

### 7. Chen, Wang, Krockenberger, Tyebally, Berg et al. — *Cell-Type-Specific eQTLs Underlie the Genetic Architecture of Complex Traits*
**Venue:** *Nature*, 2026, doi 10.1038/s41586-026-10577-6.
**Surfaced via:** Google Scholar alert "Joshua C. Denny - new related research" (09-17, 05:47Z).
**Threads:** Genetic epidemiology (GWAS, eQTL, TWAS); Knowledge representation in EHRs → Applications (as the substrate for TWAS-based phenotype prediction).

**What it is (from abstract snippet).** Establishes that genetic effects
on complex traits act primarily by **regulating gene expression**, and
that **cell-type-specific eQTLs** are the granularity at which that
regulation happens. The paper is positioned as the field-defining
reference for how GWAS-mapped variants translate into gene-regulatory
mechanism through **cell-type-resolved eQTL evidence**.

**Why it matters for your work.** This is the landmark paper the field
was waiting on for cell-type-specific eQTL / TWAS foundations, and it is
citation-ready for any downstream analysis where you want to argue that
**partitioned PRS** (like Zhu et al. AoU BP-PRS on tissue-specific
enhancers, 09-01 report) or **cell-type-resolved TWAS** is doing
mechanistic work rather than statistical partitioning. Also relevant for
`Genetic epidemiology → cross-trait shared genetic architecture and
multi-trait triangulation` — cell-type-specific eQTLs are the substrate
on which cross-trait sharing gets its biological interpretation.

**Contrast against:** GTEx v10; DICE; Onek1K single-cell eQTL atlas;
Zhu et al. AoU partitioned BP-PRS (09-01 report); Yazar *Science* 2022
disease-associated peripheral immune eQTLs.

---

### 8. Fujita & Hattori — *Information Set Emulation: Causal Certificates for AI-Derived EHR Features*
**Venue:** arXiv 2609.17777, 2026, primary category stat.ME.
**Surfaced via:** Local `arxiv-digest` 09-17 cron (score 3; keyword hits **electronic health records + inverse probability + causal inference**).
**Threads:** Knowledge representation in EHRs → Fidelity, portability, and audit of representations; Causal inference and pharmacoepi; EHR foundation models.

**What it is (from abstract).** AI and large language models can recover
clinically meaningful features from EHRs, but predictive usefulness does
not establish admissibility for causal inference. The paper introduces
**information set emulation**: an AI-typed lift that attaches **source
evidence, clinical and recording times, decision-time availability,
representation version, proposed causal roles, and unresolved ambiguity**
to extracted features under a **locked target trial**. **Causal
certificates** record auditable evidence for those roles. Features with
unresolved downstream roles are routed to compatible reporting or
separate analyses. Under explicit exchangeability, positivity, and
nuisance-consistency conditions, it gives identification and cross-
fitted augmented-IPW estimation and distinguishes empirical from
population targets. An **EHR compression-drift identity** separates the
roles of frame presence, treatment assignment, and outcome observation.

**Why it matters for your work.** Extraordinary direct hit for the
convergence of three of your threads: (a) `Knowledge representation in
EHRs → Fidelity, portability, and audit of representations` — the causal
certificate is *exactly* the auditable-representation layer INTERESTS.md
asks for; (b) `Causal inference and pharmacoepi` — the identification +
cross-fitted AIPW estimation under explicit assumptions is the estimator
stack you already prioritize; (c) `EHR foundation models` — the paper
takes as given that AI/LLM extractors will be used, and specifies the
governance layer that turns them from predictive tools into causal-
admissible ones. Also lands the **compression-drift identity** which is
a portable diagnostic for FM-extracted EHR features. Cite alongside
Wu ACT CT phenotyping (09-01 report), which is the imaging-side auditable
representation, and scContam / MIA-scFM pretraining-contamination audits
from INTERESTS.md.

**Contrast against:** Hernán target-trial-emulation scaffold; Wu ACT CT
phenotyping (09-01 report) as the imaging-side auditable representation;
Schuemie empirical-calibration diagnostics; scContam / MIA-scFM
contamination audits (INTERESTS.md-cited).

---

### 9. Bellucci, Gu, Rose, Baranzini — *An Agentic AI Framework Connecting Language Models to Electronic Health Records and a Biomedical Knowledge Graph for Real-World Evidence*
**Venue:** *Frontiers* (family), 2026.
**Surfaced via:** Google Scholar alert "Zhiyong Lu - new related research" (09-09, 16:04Z).
**Threads:** Agentic / human-in-the-loop observational-causal-inference pipelines (INTERESTS.md 07-29 sub-thread); Knowledge graphs & ontologies; EHR phenotyping & OMOP; Drug repurposing (KG-based).

**What it is (from alert snippet).** An **agentic AI framework** that
connects **language models** to **electronic health records** and a
**biomedical knowledge graph** for real-world-evidence generation. The
architecture is a natural companion to the Chou/Kallus oci-agent (arXiv
2607.22443) and Li et al. EHR-derived-HTE (arXiv 2607.16934) lineage
that INTERESTS.md cites — an LLM agent that consults an EHR + a KG (SNOMED
/ UMLS / RxNorm / phecodeX) to structure an RWE analysis.

**Why it matters for your work.** Direct hit for the **`Agentic /
human-in-the-loop observational-causal-inference pipelines`** sub-thread
you added in 07-29. Also directly serves `Drug repurposing → KG / GNN
approaches with explainable hypothesis output (path or subgraph
rationales)` because KG + LLM + EHR is the natural substrate for
explainable KG-based repurposing evidence. Third — Baranzini is a co-
author on the **SPOKE** biomedical knowledge graph (UCSF) with a long
history of KG-based drug repurposing for MS and other autoimmune
disease; the paper likely rides on SPOKE, which pairs it directly with
your `Knowledge graphs & ontologies` thread.

**Contrast against:** oci-agent (Chou/Kallus arXiv 2607.22443, INTERESTS.md
cited); Li et al. EHR-derived HTE (arXiv 2607.16934, INTERESTS.md-cited);
SPOKE lineage (Nelson / Baranzini 2019 → 2023); GraphPert transcriptional-
signature drug repurposing (also on the 09-09 `"drug repurposing"` feed
in this batch).

---

### 10. Krueger — *Genetic Fine-Mapping of the Plasma Proteome Across Multi-Ancestral Populations*
**Venue:** thesis or preprint, 2026 (AoU-Researcher-Workbench-anchored analysis).
**Surfaced via:** Google Scholar alert `"All of Us research program"` keyword feed (09-16, 06:34Z).
**Threads:** Biobanks with EHR linkage (AoU); Genetic epidemiology → PGS × ancestry AND cross-trait shared genetic architecture; Composite risk models.

**What it is (from alert snippet).** Genetic fine-mapping of the plasma
proteome across **multi-ancestral populations**, applied to **PWAS in ten
cardiometabolic phenotypes within the All of Us Research Program**. The
PWAS-in-AoU angle is unusual — most large PWAS to date has been UKB /
Olink; AoU's SomaScan / Olink coverage is smaller and more diverse, so a
PWAS-in-AoU paper is a portability paper by construction.

**Why it matters for your work.** Companion paper for the Zheng
absorption/co-expression PGS-vs-proteomic-RS paper above — Zheng is the
disease-focused framework, Krueger is the cardiometabolic PWAS instance
in AoU. Together they anchor the **`Multi-omics-augmented PRS`** sub-
thread on both sides (methods framework + disease instance). Also serves
`Biobanks with EHR linkage → AoU` and pairs with the Tsuo *Nat Genet*
PRS paper above (Tsuo is the PRS side; Krueger is the PWAS side; both
land AoU-side).

**Contrast against:** UKB Olink PWAS (Sun 2023 *Nature* + Katz 2023
*Nature*); Zheng et al. absorption/co-expression PGS-vs-proteomic RS (#5
above); Kurniansyah *Nat Genet* 2026 multiancestry AD-PRS (09-01 report).

---

### 11. Zhou, Han, Beulens, Ahmadizar — *Operational Definitions of Type 2 Diabetes Influence Study Population Characteristics and Outcome Associations: Empirical Evidence from the UK Biobank*
**Venue:** *Diabetes Research and Clinical Practice*, 2026, doi 10.1016/j.diabres.2026.04869 (per alert URL).
**Surfaced via:** Google Scholar alert `"UK Biobank"` keyword feed (09-17, 10:48Z).
**Threads:** EHR phenotyping & OMOP → definitional sensitivity; Biobanks with EHR linkage (UKB); Causal inference and pharmacoepi (as a design-sensitivity caveat).

**What it is (from abstract snippet).** Implements **five T2D definition
families** in **501,936 UKB participants**, distinguishing diagnosed T2D
from HbA1c-defined undiagnosed diabetes, and compares **case composition,
diagnosis timing, and polygenic and clinical profiles** across
definitions. This is the empirical version of an argument that the
PheKB / phecode / PheValuator community has been making for a decade:
which computable phenotype you pick changes who you count as a case.

**Why it matters for your work.** Direct hit for **`EHR phenotyping &
OMOP → definitional sensitivity`** — the T2D definition families
Zhou et al. compare will map cleanly onto the phecode / phecodeX / OMOP
concept-set choices in AoU, MyCode, MVP, and BioVU. Portable as a
template: run the same five-definition matrix in AoU and compare
against Truong et al. cross-biobank PheWAS harmonization + Acharya et
al. ASCVD cross-biobank heritability (09-01 report). Also useful as a
citation when arguing that phecode / OMOP definition choice is not
downstream nuance but a first-order determinant of PRS performance,
TTE effect estimates, and heritability estimates in EHR-linked biobanks.

**Contrast against:** Truong et al. cross-biobank PheWAS harmonization;
CohortContrast (Ilves et al. 09-01 report) as the OMOP concept-selection
methods companion; PheValuator (Ryan) for a validity-anchored companion.

---

### 12. O'Malley, Keen, Thornell, Campbell, Prouty et al. — *CFTR Modulation Alters Pancreatic Cancer Cell Growth and Signaling: Implications for Cancer Risk in Cystic Fibrosis*
**Venue:** *Journal of Cystic Fibrosis*, 2026, doi 10.1016/j.jcf.2026.09.037343 (per alert URL).
**Surfaced via:** Google Scholar alert "Chenjie Zeng - new related research" (09-17, 05:47Z; self-related-research feed).
**Threads:** Cystic fibrosis / CFTR (modulator eligibility, real-world outcomes, long-horizon safety); Causal inference and pharmacoepi (adjacent, for downstream CFTR-modulator persistence work).

**What it is (from alert snippet).** People with cystic fibrosis (PwCF)
have an increased risk of **pancreatic cancer**, likely related to
chronic pancreatic inflammation and CFTR dysfunction. With the
widespread use of **CFTR modulators such as elexacaftor/tezacaftor/
ivacaftor** (Trikafta), the paper investigates whether modulator therapy
alters pancreatic cancer cell growth and signaling — i.e., whether the
long-horizon cancer risk profile of PwCF is being changed by chronic
modulator exposure.

**Why it matters for your work.** Direct hit for the **CF / CFTR**
disease thread and specifically for the modulator-eligibility / long-
horizon-safety / real-world-outcomes sub-thread INTERESTS.md
prioritizes. The paper is bench + cell-signaling, not epidemiologic —
but the framing sentence about "cancer risk in CF" under chronic modulator
therapy is exactly the kind of long-horizon signal your `Causal
inference and pharmacoepi` thread would want to ground-truth
epidemiologically. Cite as motivating evidence for a **CFTR-modulator
persistence TTE with pancreatic-cancer as a downstream outcome** — a
study you could imagine building on CFF Patient Registry data or on the
UK CF Registry + primary-care EHR combination that the Ju et al. UDCA-
Parkinson paper (#4) demonstrated is now analytically tractable. Also
useful as a co-citation with the Sharma & Tapadiya frozen hematology-FM
acquisition-shift audit (09-01 report), because both flag that chronic-
therapy long-horizon monitoring is the next frontier for AI-augmented
CF research.

**Contrast against:** MacDonald et al. *J Cyst Fibros* 2024
elexacaftor-tezacaftor-ivacaftor long-horizon outcomes; CFF Patient
Registry Annual Reports on modulator-era cancer incidence; the Wang
et al. NTM CF mucus multiscale paper (#13) as the bench-modeling
companion.

---

### 13. Wang, Konstantinopoulos, Kuo, Cai, Wei, Pienaar, Hao — *Multiscale Modeling of Host-Pathogen Interactions and Mucociliary Clearance during Non-Tuberculous Mycobacterial Pulmonary Infection*
**Venue:** arXiv 2609.15584, 2026.
**Surfaced via:** Local `arxiv-digest` 09-16 cron (score 1; keyword hit **cystic fibrosis**).
**Threads:** Cystic fibrosis / CFTR (comorbidity — NTM infection in CF); EHR foundation models → Digital twins from EHR data (aspirational endpoint the paper names); ML for precision health (mechanism-informed).

**What it is (from abstract).** A computational framework bridging an
**agent-based model (ABM)** of NTM infection with a spatially-resolved
**partial-differential-equation (PDE)** model of mucus + tissue dynamics
in the CF lung. The PDE couples bacterial proliferation, macrophage
chemotaxis, immune-mediated clearance, mucus degradation, and
viscoelastic transport in a two-compartment geometry (mucus + lung
tissue). **Mucus viscosity, bacterial diffusivity, and macrophage
mobility** are the key regulators of bacterial persistence identified by
sensitivity analysis. Nonlinear finding on therapy: enhanced clearance
reduces bacterial burden in mucus, but **excessive viscosity reduction
may promote migration into lung tissue**, arguing for combination with
antibacterial treatment. The paper closes by naming **patient-specific
digital twins** for pulmonary infection as the aspirational endpoint.

**Why it matters for your work.** Direct hit for CF as a disease
(NTM in CF is a well-known clinical problem) AND for the **`Digital
twins from EHR data`** sub-thread — the paper is bench-modeling now, but
the framing is explicitly digital-twin-aspirational. Interesting as a
companion to the O'Malley pancreatic-cancer-in-CF paper (#12): both are
signaling that CF pharmacoepi + digital-twin work is expanding beyond
the airway-clearance / lung-function axis into (a) long-horizon cancer
risk under chronic modulator therapy and (b) mechanism-informed
patient-specific infection modeling.

**Contrast against:** Islam DINIRS 2608.26915 (09-01 report) as the
digital-twin sibling in acute respiratory failure / non-invasive
ventilation; the Ideker / Zhang / Oermann *Cell* 2026 digital-twin
consortium framing paper (INTERESTS.md-cited).

---

### 14. Chien & Garcia-Manero — *Clinical Management of Clonal Hematopoiesis*
**Venue:** *Cancer*, 2026, doi 10.1002/cncr.70588.
**Surfaced via:** Google Scholar alert `intitle:"clonal hematopoiesis"` keyword feed (09-17, 10:48Z).
**Threads:** Clonal hematopoiesis (CHIP), VEXAS, and mosaic Loss of Y (LOY); Somatic mosaicism.

**What it is (from alert snippet).** A **clinical-management review** of
clonal hematopoiesis, focusing on **CHIP** specifically, its
malignant-transformation and cardiovascular / hematologic outcome
associations, and what practicing hematologists should do about it. Not
a research-methods paper — a clinical-guidance paper.

**Why it matters for your work.** Closes a gap in the 09-01 report
where the CHIP / LOY / VEXAS thread had picked up only mechanistic and
epidemiologic papers (Loh, Kessler, Li) but nothing on the clinical-
management side. Chien & Garcia-Manero (MD Anderson) is a leading CHIP
clinical group, so this is likely the reference clinical-management paper
for the year. Useful as a citation when arguing that CHIP is on the
transition from "biomarker" to "actionable clinical entity" — the same
transition your INTERESTS.md thread predicts for LOY.

**Contrast against:** Steensma 2015 CHIP framing; Jaiswal *NEJM* 2017
CHIP CV; Bick *Nature* 2020 driver gene review; Kessler *Nature* 2022 LOY;
Li et al. *Atherosclerosis* 2026 LOY × PAD (INTERESTS.md-cited).

---

### 15. Snel & Schulz — *Attributing Cohen's d: Training Data Attribution for Disease-Related Effects in Normative Age Biomarkers*
**Venue:** arXiv 2609.07729, 2026.
**Surfaced via:** Local `arxiv-digest` 09-09 cron (score 2; keyword hits **uk biobank + biobank**).
**Threads:** Biobanks with EHR linkage (UKB); ML for precision health (auditable attribution); Knowledge representation in EHRs → Fidelity + audit.

**What it is (from abstract).** Normative age models are trained to
predict chronological age in a nominally-healthy cohort; applied to
patients, they deviate, and the gap between predicted and chronological
age is read as disease risk. This paper attributes the **disease-related
effect size** of the age gap directly to **individual training samples**,
rather than to a prediction-level loss. For **Cohen's d**, the paper
derives a **closed-form influence functional**, validated against
leave-one-out retraining, that ranks training samples by their effect on
held-out case-control separation. Across four diseases and two biomarker
modalities in UK Biobank, removing the 10% most influential training
samples raises held-out disease-related effect size in every seed; for
type-2 diabetes, this **more than doubles** the metabolomic-age effect.
Random removal leaves effect size flat even at 50% removal. Flagged
subjects carry subclinical cardiometabolic burden that diagnosis-based
exclusion misses (HbA1c recovered as the T2D marker the model never sees).
Releases **pyinfluence** for reuse.

**Why it matters for your work.** Direct hit for `ML for precision
health` and for `Fidelity, portability, and audit of representations`:
the pyinfluence tool is a portable auditable-attribution machinery for
any UKB / AoU normative-age model. Also connects to `PheWAS / phecode
infrastructure → penetrance estimation for monogenic variants under
population-screening conditions` because the mechanism the paper
demonstrates — that subclinical burden hidden by diagnosis-based
exclusion contaminates a "healthy" reference — is the same nuisance you
face when interpreting monogenic-variant penetrance in UKB or AoU (the
"healthy" reference contains undiagnosed carriers). The T2D-HbA1c
recovery finding is a proof-of-concept that pyinfluence recovers a
mechanistically-correct marker, which is the auditable-representation
argument in miniature.

**Contrast against:** the Wu ACT CT-phenotyping auditable representation
(09-01 report); the influence-function classical literature (Koh &
Liang 2017 ICML); Bethlehem *Nature* 2022 brain-age reference; the
scContam pretraining-contamination audits (INTERESTS.md-cited).

---

## METHODS-WATCH — off-topic domain, exemplary methods worth cribbing

- **Devarakonda** — *scDEFT: A deep learning framework for drug-effect
  prediction and counterfactual reasoning* (arXiv 2609.10831, 09-11
  local digest, score 2 on **inflammatory bowel disease + patient
  stratification**). Treats a drug as a **conditioning operator** on
  cell representations; **feature-wise linear modulation** produces
  drug-conditioned cell latents, learned under abundant per-cell
  supervision and then frozen. Two independent heads aggregate latents
  over shared transcriptional neighborhoods to predict drug-induced state
  change and responder status. Backward stage ranks latent dimensions by
  responder-vs-non-responder separation and maps them to genes under a
  cell-composition control. On a harmonized IBD atlas of 1.16 million
  cells, three cohorts, two drug classes: predicts state change at 45%
  of the baseline-to-reproducibility ceiling headroom; **stratifies
  responders before treatment at AUROC 0.70** where standard predictors
  are at chance. Also on-thread for **IBD** — this is one of the first
  large single-cell drug-effect papers that names patient stratification
  as its primary application, so it belongs on both a `Drug repurposing
  → EHR-based repurposing signals` watch (with counterfactual reasoning
  as the mechanism) and on your IBD disease thread.
- **Y Wang** — *Methodological Pipelines for Digital Twin Mechanistic
  Model Parameter Estimation, Forecasts, Interpretation, and Translation
  to Enhance Next-Generation Clinical Care* (2026, Hripcsak citations-to
  feed 09-17). A methods-review-plus-pipeline paper for the digital-twin
  parameter-estimation → forecast → interpretation → translation chain.
  Reinforces that the **`Digital twins from EHR data`** sub-thread you
  added in 07-29 is being systematized into pipeline recipes — cite as
  the methods-pipeline companion to the Ideker / Zhang / Oermann *Cell*
  2026 consortium framing paper.
- **Yu, Huang, Liu, Tang, Wang, Zhang, Zhao** — *A Location-Invariant
  Estimator of Extremal Quantile Treatment Effects for Heavy-Tailed
  Distributions* (arXiv 2609.04018v1, 09-04 local digest, score 1
  **propensity score**). Adapts the location-invariant Fraga EVI to the
  causal setting using inverse-propensity-score weighting, then replaces
  the extrapolation formula with a difference-based scheme so the
  location parameter cancels. On-thread as a portable estimator for
  **rare-event pharmacoepi** — the same use-case Leimenstoll & Schienle
  causal-tail-coefficient paper flagged in the 09-01 report. Pair the
  two on your rare-event-pharmacoepi reading list.
- **Lee, Rempala, Schnell** — *Kalman Filtering and Smoothing for
  Improving Precision in Horvitz–Thompson Estimation of Infectious
  Disease Prevalence* (arXiv 2609.09325v1, 09-10 local digest, score 1
  **inverse probability**). State-space wrapper on the HT survey-
  weighting estimator; borrows information across days to reduce variance
  and handle no-testing-day gaps. Off-thread domain (COVID surveillance)
  but the **latent-slope local-linear-trend HT wrapper** is portable to
  **IPW-weighted incidence estimation** in EHR-linked cohorts where the
  weights have high day-to-day variability (e.g., staggered-index-date
  pharmacoepi).
- **Rajabli & Collins** — *A Generalizable Feature Extractor for
  Alzheimer's-Related Brain MRI Tasks* (arXiv 2609.05400v1, 09-07 local
  digest, score 1 **foundation model**). Freezes a **compact 3D CNN
  supervised for brain-age** and adapts to six neuroimaging tasks with
  LoRA (~1% trainable params). AUC 0.964 for AD vs. CN on ADNI, 0.871
  transfer to OASIS-3 without retraining. Domain is imaging FMs, not
  EHR-FMs — but the "compact supervised backbone + LoRA transfer without
  retraining" pattern is a portable template for **AoU → UKB** or
  **BioVU → MIMIC-IV** EHR-FM transfer where you want to avoid the
  compute cost of retraining a frontier decoder LLM for each new site.
- **Hendrix, Zhang, Heitzig, Bazemore, Rehkopf** — *Geospatial Foundation
  Models Capture Health-Relevant Dimensions of Place Beyond Conventional
  Social Risk Indices* (arXiv 2609.11689v1, 09-11 local digest, score 1
  **foundation model**). LightGBM over four geospatial-FM families
  (2022 satellite data) explains up to 54% of variance left unexplained
  by ADI / SDI / SVI across 82,646 US census tracts for 40 CDC PLACES
  outcomes. Off-thread domain (geospatial FMs) but the framing —
  "learned-representation family beats a hand-engineered index at
  explaining outcome variance" — is a portable auditable-representation
  argument for your `Fidelity, portability, and audit of representations`
  sub-thread.
- **Semchin, d'Angremont, Ding, Antar, Lorenzi, Arfanakis, van der Werf,
  Thompson, Gutman** — *Discovering Subtypes of Neurodegenerative
  Progression with a Scalable Connectome-Constrained Dynamic Model*
  (arXiv 2609.10890v1, 09-11 local digest, score 1 **motor**). A
  connectome-constrained disease-progression model that jointly
  estimates subject-specific disease time and data-driven subtypes from
  longitudinal morphometry on PPMI; recovers four Parkinson subtypes
  that match clinical motor subtypes AND genetic variants, whereas the
  SuStaIn baseline does not. Off-thread as a Parkinson-specific study,
  but the **connectome-constrained trajectory model that recovers
  genetic-variant-aligned subtypes** is directly portable to `Chronic
  disease clustering and multimorbidity` (subtype discovery aligned with
  genetics) and pairs with NetMoint UKB dementia-trajectory subtypes
  (09-01 report) as a same-year methods sibling.
- **Wu, Han, Mito, Watabe, Hayashi, Takaya, Kubo, Yoshida** — *FUSE-RT
  Simulation-Supervised Foundation Models for Retention Time Prediction*
  (arXiv 2609.07531v1, 09-09 local digest). **Sim2Real transfer**
  substrate for foundation models applied to sparse experimental data —
  power-law scaling in simulation-data size. Off-thread chemistry
  domain, but the Sim2Real substrate is portable to **synthetic EHR
  pretraining** for EHR-FMs (e.g., MIMIC-IV-Synthea → real MIMIC-IV
  transfer curves).

---

## Also-ran / SKIP pile (briefly, so you don't have to re-scan)

- **Ramesh, Sadalgekar, Tan, Li** mudskipper locomotion (arXiv 2609.00564
  v1, 09-02 local digest) — bio-mechanics; off-thread; a keyword `motor`
  hit only.
- **Cortez-Rodriguez** natural-disasters-and-nonprofits panel causal
  (arXiv 2609.04136v1, 09-04 local digest) — nonprofit-sector econ; off-
  thread `causal inference` hit only.
- **Zhang, Bao, Ma, Liu, Ma, Liu, Li, Li, Gong, Ca** — **scKITE** *Towards
  a knowledge-enhanced single-cell foundation model* (arXiv 2609.14970v1,
  09-16 local digest). Interesting single-cell-FM engineering (cell-
  annotation + gene-regulatory supervision through auxiliary decoders
  discarded post-pretraining, 0.5% of the prior FM data volume matches
  or beats SOTA), but off the EHR / clinical axis.
- **Jiang, Ding, Han, Liu, Rosenthal, Wang** *Patient-Reported Survey
  Data Improve Prediction of Opioid Use Disorder* (arXiv 2609.12224,
  surfaced via `"All of Us"` keyword feed 09-17). AoU-based OUD
  prediction; adjacent to `ML for precision health` and to `Biobanks
  with EHR linkage → AoU`, but the "add survey to EHR" framing is
  incremental against Hyland *Sci Rep* 2024 same-cohort survey-augmented
  models. Consider a light read only.
- **Spence & Patel** *Insights into human evolution from large genetic
  biobanks* (arXiv 2609.12297, surfaced via `"All of Us"` keyword feed
  09-17). Review of biobank-scale evolutionary genetics; off the clinical
  / phenotype axis.
- **Roberts, Thompson, Anderson, Smith** *Polygenic Pharmacotherapy
  beyond Single-Gene Rules: An Evidence Map of Scores, Interactions,
  Ancestry Transferability, and Clinical Utility* (Int J Pharm Res
  Allied Sci 2026, surfaced via Denny new-related 09-17). Evidence-map
  review of polygenic pharmacotherapy — useful as an orientation citation
  but low-impact venue; treat as background reading for the Walker et al.
  (#2) paper.
- **Aguilar-Ordoñez et al.** *Whole genome sequencing of 1,427 Mexican
  individuals from the oriGen cohort* (Nat Commun 2026, via Denny
  citations-to 09-09). Latin-American population WGS — relevant to
  `PGS × ancestry` as a resource paper, but not a methods or disease
  paper for this window. Note for later.
- **Huang, Wu, Bartolomeo, O'Toole, Sedor** *Differential regulation of
  basal and interferon-induced APOL1 gene expression in podocytes*
  (Am J Physiol Renal 2026, via APOL1 keyword feed 09-17). APOL1
  mechanism paper; useful as background for the APOL1 disease thread but
  not epidemiologic.
- **Hendrix et al.** geospatial-FMs augment social-risk indices — listed
  under METHODS-WATCH above because the framing is portable, but the
  application domain is off-thread.
- **Sun, Liang, Ou, Gao, Wang, Yuan** bidirectional MR IBD × common
  diseases (via `mendelian diseases` keyword feed 09-09) — MR is not
  currently high-priority per INTERESTS.md unless drug-target MR; this
  is generic disease-wide MR.
- **Chen et al.** *Oral Anticoagulants in AF and Advanced CKD Not
  Requiring Dialysis* (JAMA Netw Open 2026, via Hernán citations-to
  09-09) — clean TTE in a clinically-tight population but off your
  specific drug-thread priorities (GLP-1 / SGLT2 / CFTR modulators /
  HRT).
- **Fu et al.** *Cost-Efficient Long-Read Trio-Barcoded Adaptive
  Sequencing for Rare Disease Diagnosis* (Nat Commun 2026, via Montgomery
  + Kai Wang new-related 09-09) — relevant to `Rare disease` but not to
  your rising sub-threads (auditable HPO benchmarks / phenoconversion /
  data-driven reanalysis at 10k+ scale); a sequencing-methods paper.
- **Ellershaw Foresight-England** re-surfaced 09-09 (Pascal Brandt
  new-related) — already covered as HIGH item #5 in the 09-01 report.
  Suppressed here to avoid double-counting.
- **Scholar-feed noise this window:** Wei ANK3 oral-microbiome / OM
  paper (Jian Yang citations-to); van der Schaar's Jones et al. UK-wide
  DCE for AI-based skin-cancer detection (van der Schaar new-articles,
  off-thread patient-preference research); GenomeHarness genome-LM AI
  agents (Zitnik new-related, already covered in the 09-01 report as
  SKIP); "Council of Councils Working Group on Fostering Transformative
  Biomedical Research" (NIH DPCPSI, via `"All of Us"` — administrative
  update, not research); ATRX condensates in enhancer-associated
  neuroblastoma (Karczewski citations-to, off-thread cell biology);
  Structure-Guided Fusion Semantic Denoising for Multi-modal KG
  Completion (`"knowledge graph"` feed — non-biomedical KG). Expected
  broad-keyword bleed-through.

---

## Cross-cutting patterns to watch

1. **The AoU × UKB "context-dependent PRS" era.** Tsuo et al. *Nature
   Genetics* is the field-defining paper for how those two biobanks
   should be combined (or not) for PRS. Combined with Krueger multi-
   ancestral PWAS in AoU and Zhou et al. STAR Protocols cross-ancestry
   local-ancestry protocol, this window contains the methodological
   substrate for **cross-biobank PGS work under ancestry
   heterogeneity**. Add "Tsuo 2026 rule for when to meta-analyze biobanks"
   to your working methods checklist.
2. **Pharmacogenomic-modifier-of-medication-persistence is now a defined
   study design.** The Walker et al. AoU + Pharmlines paper (four-outcome
   decomposition) is the field-defining polygenic version of what Cohen
   et al. 2026 CYP2D6 × persistence had done in single-gene mode. The
   design pattern is portable across CFTR-modulator, statin, HRT,
   GLP-1 RA persistence. INTERESTS.md correctly anticipated this thread
   in the 07-29 update.
3. **TTE-for-drug-repurposing has hit critical mass.** Wu et al.
   AD/ADRD decentralised-RWE + Ju et al. UDCA-Parkinson-UK-EHR are two
   independent instances of the same TTE-for-repurposing pattern
   published within a two-week window. The design pattern is now cite-
   ready as a family, not as a one-off. Zhao et al. narrative-framework
   review of TTE + causal-ML in cancer immunotherapy (09-01 report) is
   the umbrella paper.
4. **Auditable representations for AI-derived EHR features are becoming
   formalized.** Fujita & Hattori (**arXiv 2609.17777**) provides an
   actual formal apparatus — **causal certificates + information set
   emulation + compression-drift identity** — for the auditable-
   representation problem that Wu ACT CT phenotyping (09-01 report)
   posed at the imaging-level. Snel & Schulz pyinfluence sits alongside
   as the training-data-attribution component. This pattern is
   accelerating and INTERESTS.md's `Fidelity, portability, and audit of
   representations` sub-thread is now the fastest-growing area in this
   digest.
5. **Digital twins are stacking up fast.** Wang et al. CF NTM PDE + ABM
   (#13) and Y Wang methodological pipelines (methods-watch above) and
   the Islam DINIRS paper from the 09-01 report all sit in the same
   `Digital twins from EHR data` sub-thread that INTERESTS.md added in
   07-29. Three independent papers in six weeks is not a coincidence;
   consider making the sub-thread its own named INTERESTS.md heading
   rather than a rising sub-thread.
6. **The 09-13, 09-14, 09-15 arxiv-digest gap** is unexplained (no
   files at all for those dates, breaking the daily cadence for the first
   time this month). If a fourth zero-file day appears in the next week,
   worth checking `scripts/arxiv_digest.py` for a fetcher-side issue
   rather than attributing it entirely to submissions volume.

---

## Next actions I would take

- **Read first (in this order):** Tsuo *Nat Genet* AoU + UKB PRS
  context-dependent (thread centrality); Walker medRxiv antidepressant
  persistence in AoU + Pharmlines (direct sub-thread hit); Fujita &
  Hattori Information Set Emulation (adds a formal apparatus you can
  cite); Wu AD/ADRD TTE repurposing (drug-repurposing landmark);
  Zheng absorption/co-expression PGS-vs-proteomic-RS (multi-omics-
  augmented PRS anchor); Bal HCM multiancestry-PRS (composite-risk
  template).
- **Cite-ready this week:** Tsuo, Walker, Wu (AD/ADRD), Ju (UDCA-PD),
  Bal (HCM), Chien & Garcia-Manero (CHIP).
- **Watch for follow-ups:** Zheng et al. (still medRxiv, likely
  *Nat Genet* / *AJHG* trajectory); Krueger multi-ancestral PWAS-in-AoU
  (venue not yet clear); Walker et al. (medRxiv → JAMA Psychiatry or
  *Am J Psychiatry* trajectory); Wu, Li, Lei et al. (venue withheld —
  watch for the peer-review landing).
- **Consider adding to INTERESTS.md:** promote **Digital twins from
  EHR data** from a `EHR foundation models` sub-thread to its own named
  heading; add a **National-scale / single-payer EHR-FM** sub-thread
  under EHR foundation models (still open from the 09-01 report);
  refine `Drug repurposing → causal-inference framings of off-label use`
  to specifically call out **TTE + decentralised RWE** as the current
  landmark study design; add a **causal certificates / auditable-
  representation formalism** cross-reference between
  `Knowledge representation in EHRs → Fidelity` and `Causal inference
  and pharmacoepi`.
