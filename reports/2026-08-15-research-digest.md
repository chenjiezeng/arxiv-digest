# Research digest report — 2026-08-15

Triage of research-related email + the GitHub `arxiv-digest` repo against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS-LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in EHRs).

Window: **2026-08-08 12:36Z → 2026-08-15 12:35Z** (~7 days since the
last research-digest report, covering seven arxiv-digest cron runs, two
Google Scholar batches on 08-13 and 08-14, five daily NCBI PubMed
alerts, and daily medRxiv/bioRxiv collection alerts).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-08.md` → `2026-08-15.md`) | 08-08 → 08-15 (10:30Z crons) | 7 daily runs. 08-08: 0; 08-10: 0; 08-11: 5 (largest batch; incl. Ciardulli-style clustering IPW, CAN-FLOW UKB cardiac digital twin, Bandreddi CH longitudinal, Charpentier motor-insurance DAG, VOICE H&E→scRNA); 08-12: 2 (Vossler egg-computation causal, Wood perinatal TTE); 08-13: 1 (Porotsky Inverse Confounding); 08-14: 0; 08-15: 0. |
| Google Scholar alerts (author feeds, 08-14 15:18Z batch) | 08-14 15:18Z | ~24 author-feed threads fired simultaneously: Chenjie Zeng (self + related), Lisa Bastarache (related), Joshua C Denny (×2: new-related + cite feed with Nature Med T2D-prevention), Nigam Shah (ChatEHR at Stanford, Nature Med), Miguel Hernán (Medicare Advantage × T2D JAMA IM, Per-Protocol Effect Epidemiology), Konrad Karczewski (CoCoRV-nf ALS rare-variant leverage), Pascal Brandt (Venkatesh & Ritchie Nat Rev Genet), Jonathan Pritchard (Salamone et al. asthma DANDELION), Kai Wang, Yong Chen (federated HIV TTE Latin America), Peter Szolovits, Stephen B Montgomery (single-cell sQTL × splicing under influenza), Yuan Luo, Emily Alsentzer, Vivek Natarajan, Marinka Zitnik, Daniel Kastner, Xiangnan He, Shuibing Chen (VOICE), Jian Yang (×2), James Zou, Tiffany J Callahan, George Hripcsak (Lähteenmaa HTE thesis). |
| Google Scholar alerts (keyword feeds, 08-13 and 08-14 19:16Z batches) | 08-13 13:33Z, 08-14 19:16Z | 4 threads on 08-13 (`UK Biobank`, `intitle:"clonal hematopoiesis"`, `drug repurposing`, `APOL1`), 13 threads on 08-14 (`UK Biobank`, `intitle:"clonal hematopoiesis"`, `mendelian diseases`, `autoimmune diseases`, `Undiagnosed Diseases Network`, `electronic health records`, `drug repurposing`, `All of Us research program`, `variant interpretation`/`variant classification`, `knowledge graph`, `rare diseases`, `Foundation models + electronic health records`). Densest APOL1 hit (lupus-nephritis meta-analysis) and Denny-related CT-phenotype causal-mediation preprint. |
| NCBI PubMed alerts (`All of Us`, `UK Biobank`, `drug repurposing`) | 08-10 → 08-14 daily | Baseline coverage; most items overlap with Scholar keyword feeds and are folded into the clusters below. |
| openRxiv daily collection alerts (bioRxiv Bioinformatics/Genetics/Genomics/Immunology/Pathology, medRxiv Epi/Genet/Health-Info/Endo/Oncology) | 08-10 → 08-15 daily | Reviewed for signal only; volume high but few HIGH-priority items beyond those already surfaced by Scholar and arxiv-digest. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated to first
> 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Sixteen HIGH items surfaced this window, clustering into six knots that
each stand on their own:

**EHR × genomics multimodal-integration cluster (2 items, both venue-defining).**
Venkatesh & Ritchie, *Nature Reviews Genetics* 2026 — the review that
your `EHR foundation models` and `Knowledge representation in EHRs and
applications` threads have been building toward: a canonical framing of
AI-based multimodal integration of genomics and EHR (cites AoU and
target trial emulation). Shah, Sehgal, Ashley, Pfeffer, *Nature Medicine*
2026 — deployment lessons from ChatEHR at Stanford Medicine, arguing
that benchmark-based evaluations are insufficient for clinician-driven
LLM interactions in an active medical center. Together these two papers
supply the *"what does the mature field look like"* framing paragraph
for any grant or manuscript that touches EHR-FM or clinical-LLM
deployment.

**Ancestry-aware biobank genetics cluster (4 items, all methods-forward).**
Yap & Morris medRxiv (PANACEA framework to maximise genetic diversity
in GWAS meta-analyses); Hu et al. medRxiv (unified local-ancestry-aware
association framework across biobanks — handles admixed genomes that
current pipelines either exclude or ignore); Smeriglio, Moreno-Grau,
Mas Montserrat et al. medRxiv (multi-ancestry admixture mapping in UKB
recovers ancestry-associated disease loci); Li et al. Research Square
(scalable framework for phenome-wide association of *structural
variants* in biobank cohorts, directly extending PheWAS to SV). These
four collectively push the `Genetic epidemiology` thread and its
composite-risk-and-PGS-portability sub-thread past ancestry-adjustment
and into ancestry-aware inference at biobank scale.

**Causal inference / pharmacoepi cluster (5 items).** Berkowitz et al.
*JAMA Internal Medicine* — Medicare Advantage vs Original Medicare
and T2D outcomes (Miguel Hernán cite feed; cites the TRIP target-trial
reporting paper): high-visibility RWE piece with target-trial framing
directly relevant to the SGLT2/GLP-1 pharmacoepi watchlist. Lu, Esen,
Ross *Epidemiology* — "Toward a Clearer Definition of the Per-Protocol
Effect": the ITT-vs-PP framing every drug-persistence analysis has to
navigate. Vossler et al. arXiv 2608.10339 — Expert-Guided g-computation
with LLMs (egg-computation) for causal effects on timings in hospital
QI: directly hits the *agentic / human-in-the-loop causal-inference*
sub-thread. Wood et al. arXiv 2608.11108 — perinatal pharmacoepi TTE
design for pregestational treatment changes (T2D example), important
because it explicitly names left/right censoring, competing events,
gestational length, and etiologically susceptible periods that plague
this study class. Keat, Zhang, Caruth, Duda, Beeche et al. medRxiv
(Denny-lab feed) — computational framework leveraging AI-derived CT
phenotypes for causal mediation between genetic variants and disease:
this is the bridge between the `EHR foundation models` and
`Causal inference` threads that your composite-risk sub-thread has
been asking for.

**Federated / privacy-preserving EHR cluster (1 item, exactly on
sub-thread).** Liu, Liang, Paredes, Moreira, Caro-Vega et al. arXiv
(Yong Chen feed) — Authentic Multinational Federated Time-to-Event
Analyses among People with HIV in Latin America. This is the same
design pattern as your Jang et al. 2607.17958 anchor, in a new
region and with a real-cohort HIV outcome, further validating the
*federated / privacy-preserving EHR causal analytics* sub-thread.

**Rare variant × biobank leverage cluster (1 headline item, plus
pediatric-IMID complement).** Tithi, Cooper-Knock, Benatar, Wuu,
Taylor et al. *Human Molecular Genetics* — CoCoRV-nf: powerful and
cost-effective rare-variant analysis leveraging *external biobank
sequence data*, identifying new candidate predisposition genes in ALS
and other diseases. Directly serves the rare-variant + biobank
leverage crosswalk and inherits from Karczewski/Kirov design. Li,
Qu, March, Glessner, Fu, Chen et al. *Ann Rheum Dis* — shared genetic
architecture and therapeutic targets across 24 paediatric IMIDs
(autoimmune, polygenic-autoinflammatory, mixed, allergic): a
transdiagnostic composite-risk lens on the pediatric autoimmune
spectrum that mirrors adult-IMID work in your IBD thread.

**Disease-specific singles: APOL1, CHIP, T2D-prevention, functional
genomics (4 items).** Aldana Peréz, Domínguez-Vargas et al.
*Frontiers in Medicine* — systematic review + meta-analysis of APOL1
high-risk genotypes and lupus-nephritis-associated kidney failure in
SLE: extends the APOL1 thread from HIV-associated and hypertensive
CKD into the SLE nephritis compartment (a genotype × interferon-
signature story). Motisi, Di Salvo, Balistreri *Ageing Research
Reviews* — CHIP as a determinant of inflammageing and age-related
diseases, potential role as biomarker and target: framing paper for
the CHIP arm of your somatic-mosaicism thread. Wang, Sargent,
Mathieu, Vazquez-Arreola et al. *Nature Medicine* — Type 2 diabetes
prevention across the life course, reframing prevention around
prediabetes remission (Denny cite feed): the T2D life-course framing
paper for any pharmacoepi thread analyzing GLP-1 RAs / SGLT2is /
metformin across age strata. Salamone, Tian, Qi et al. *Cell*
(Pritchard feed) — DANDELION, a mediation-inspired framework
prioritizing "disease-proximal genes" (DPGs) via trans-regulatory
mapping in asthma: goes past GWAS-locus-cataloguing into
disease-driver identification, a template your `Genetic epidemiology`
and `Knowledge representation` threads should watch.

**Methods-watch (not HIGH but worth cribbing).** Vossler et al.
arXiv 2608.10339 (egg-computation) also sits in Methods-Watch as an
LLM-assisted-pipeline template. Kevopoulos et al. arXiv 2608.09460
CAN-FLOW normalizing flows for cardiac digital twins from 2,208 UKB
subjects, externalized to 47k — clean template for the
*digital-twins-from-EHR-data* rising sub-thread but the outcome is
imaging-only, not longitudinal-EHR. Chen, Zuo, Stevens et al. arXiv
2608.09839 — clustering-informed IPW strategies for causal-effect
estimation under omitted-covariate misspecification (breast-cancer
carboplatin application). Bandreddi, Zhang, Kelly, Machiela, Albert
arXiv 2608.09725 — Tobit vs two-part Hurdle models for semi-continuous
longitudinal clonal-fraction data (PLCO); methodology for the CHIP
longitudinal-trajectory framing. Porotsky arXiv 2608.11991 —
Inverse Confounding Analysis extending E-value to the full admissible
set. Cameron et al. *Clin Biochem* — NSAIDs × CYP2C9 phenoconversion
(pharmacogenomic-modifier sub-thread). Weaver, Petry, Cauwels, Lupu
et al. *Clin Pharmacol Ther* — LLM prompt-engineered medication-dose
extraction from EHR (five public LLMs; Denny-cite feed).

---

## Detailed reports (per HIGH-priority study)

### 1. Venkatesh & Ritchie — AI-based multimodal integration of genomics and EHR (*Nature Reviews Genetics* 2026)

**Citation.** R Venkatesh, MD Ritchie. AI-based multimodal integration
of genomics and electronic health records. *Nature Reviews Genetics*,
2026. Article s41576-026-00992-w.

**Source.** Google Scholar author feed — *Pascal Brandt — new related
research*; also cross-cited in the *Miguel Hernán cite* feed (Aug-14
15:18Z batch, same session).

**Alert-visible abstract lead.**
> The widespread adoption of electronic health records (EHRs), which
> capture patient-specific longitudinal information on diagnoses,
> laboratory tests, clinical procedures, and outcomes, has created
> unprecedented opportunities to study diseases at scale. Integrating
> EHR data with genomic information offers novel ways to understand
> disease heterogeneity, identify biomarkers and therapeutic targets,
> and predict disease risk to improve clinical decision-making at
> scale. Recent methodological …

**Why it fits (INTERESTS.md → high priority).**
Simultaneously anchors three of your active threads:

- `EHR foundation models` — a *Nature Reviews Genetics* framing paper
  for the EHR × genomics integration space is exactly the
  field-defining reference the thread needs.
- `Knowledge representation in EHRs and applications` — the review
  explicitly discusses representation-choice consequences (biomarker
  discovery, therapeutic-target identification, decision support),
  which is the *"which representation choice drives downstream
  performance"* framing you flagged.
- `Biobanks with EHR linkage` — cited passages include the *All of Us
  research program* genomic paper as an example, aligning it with
  your AoU/UKB/MVP/BioVU set.

**What to do with it.** This is the *"cite in the intro of any grant
or manuscript that touches EHR-FM"* paper for 2026. Read the full
review, extract the sub-taxonomies of multimodal integration (early,
intermediate, late fusion; concept vs sequence vs graph
representations) and use them to sharpen the KR/EHR-FM thread wording
in `INTERESTS.md`. Also verify whether the review cites the digital-
twins-from-EHR (Zhang / Ideker / Oermann Cell 2026) framing paper;
if not, that's a manuscript-opportunity gap.

**Triage.** HIGH — read priority #1 this window.

---

### 2. Shah, Sehgal, Ashley, Pfeffer — Lessons from deploying ChatEHR at Stanford Medicine (*Nature Medicine* 2026)

**Citation.** NH Shah, N Sehgal, EA Ashley, MA Pfeffer. Lessons from
deploying the ChatEHR system at Stanford Medicine. *Nature Medicine*,
2026. Article s41591-026-04574-5.

**Source.** Google Scholar author feed — *Nigam Shah — new articles*
(Aug-14 15:18Z batch).

**Alert-visible abstract lead.**
> In piloting and deploying a large language model within a large
> medical center, we learned that benchmark-based evaluations are
> insufficient for monitoring and evaluating interactions driven by
> clinicians, and that this requires new methods for …

**Why it fits.** Sits at the intersection of `EHR foundation models`
and `EHR phenotyping & OMOP`. The key HIGH-priority claim (visible
even from the alert lead) is the argument that **benchmark leaderboards
do not extrapolate to production LLM behavior in an EHR-integrated
setting**, which is directly relevant to any downstream LLM-assisted
phenotyping pipeline (HPO extraction from notes, phecode assignment,
clinical NLP evaluation). Same author-feed message also carried
Chatrath et al. arXiv 2608.07796 *CliniCARE-Bench* (calibrated audit
of medical reasoning in EHR); the two pieces bookend the
*benchmark-vs-deployment* argument for the same audience.

**Triage.** HIGH — read full text and mine the deployment audit
protocol for adaptation to the note-code fusion sub-topic under
`Knowledge representation in EHRs`.

---

### 3. Keat, Zhang, Caruth, Duda, Beeche et al. — Framework leveraging AI-derived CT phenotypes for causal mediation between genetic variants and disease (medRxiv 2026)

**Citation.** K Keat, DY Zhang, L Caruth, J Duda, C Beeche et al.
A Computational and Statistical Framework Leveraging AI-Derived CT
Phenotypes for Causal Mediation Effects Between Genetic Variants and
Disease. *medRxiv*, 2026. DOI 10.64898/2026.08.05.26359812.

**Source.** Google Scholar author feed — *Joshua C. Denny — new related
research* (Aug-14 15:18Z batch).

**Alert-visible abstract lead.**
> As the costs of genetic sequencing continue to drop and human
> genomic biobanks grow in scale, the challenge in genomics has
> shifted increasingly towards disentangling whether and how associated
> genetic variants cause disease. Clinical …

**Why it fits.** Directly serves three threads in one preprint:

- `EHR foundation models` (AI-derived CT imaging phenotypes as
  mediators — the same *imaging-FM-on-biobank-data* framing as Sasson
  et al. 2608.02208 DXA from the previous digest window);
- `Causal inference and pharmacoepidemiology` (causal mediation
  between genetic variants and disease, which is the mechanistic
  extension of MR/TWAS);
- `Genetic epidemiology / composite risk` (variant → mediator →
  disease as an identification strategy for how PGS or rare variants
  actually act).

Beeche appears in both this study and the CAN-FLOW cardiac digital-
twin paper from arxiv-digest 08-11 (Kevopoulos et al. 2608.09460),
signaling an active Penn Medicine effort on AI-imaging-mediator
causal-mediation methods across UKB imaging modalities. This is a
methods paper you want mapped onto the CFTR / APOL1 / CHIP disease
threads.

**Triage.** HIGH — read full text and cross-reference to your notes on
Baya AJHG 2026 polygenic-deviation designs; the two share the "PGS or
rare variant as *distal* cause; measured biology as *proximal*
mediator" logic.

---

### 4. Berkowitz, LaPoint, Kuhn, Basu et al. — Medicare Advantage and Type 2 Diabetes Outcomes (*JAMA Internal Medicine* 2026)

**Citation.** SA Berkowitz, M LaPoint, ML Kuhn, S Basu et al.
Medicare Advantage and Type 2 Diabetes Outcomes. *JAMA Internal
Medicine*, 2026. Article 2852477.

**Source.** Google Scholar cite feed — *10 new citations to articles
by Miguel Hernán* (Aug-14 15:18Z batch); paper cites the transparent-
reporting TRIP target-trial-emulation reference.

**Alert-visible abstract lead.**
> Importance Medicare Advantage (MA) costs 22% more than original
> Medicare (OM) for a given individual ($83 billion in annual excess
> public costs). However, MA may improve type 2 diabetes (T2D)
> outcomes compared with OM by providing financial protections (eg,
> annual out-of-pocket spending caps) and supplemental benefits (eg,
> healthy food assistance) that OM cannot. Objective To determine
> whether MA coverage is associated with better T2D outcomes than OM.
> Design, Setting, and …

**Why it fits.** Anchors your `Causal inference and pharmacoepidemiology`
thread's pharmacoepi drug-class watchlist (T2D → GLP-1 RA / SGLT2i is
your active watch). The design is target-trial-emulation-style on a
large observational payer contrast (MA vs OM) with a hard cardiometabolic
outcome. Two things to check on full read: (i) how the cohort handles
selection into MA (channeling of healthier or higher-benefit-need
individuals), and (ii) whether medication class effects
(SGLT2i/GLP-1RA prescribing rates) are treated as mediators or as
confounders.

**Triage.** HIGH — read full text; this is a candidate anchor for
teaching-example status in a target-trial-emulation methods lecture.

---

### 5. Lu, Esen, Ross — Toward a Clearer Definition of the Per-Protocol Effect (*Epidemiology* 2026)

**Citation.** H Lu, BÖ Esen, RK Ross. Toward a Clearer Definition of the
Per-Protocol Effect. *Epidemiology*, 2026.
DOI 10.1097/ede.0000000000002035.

**Source.** Google Scholar cite feed — *10 new citations to articles by
Miguel Hernán* (Aug-14 15:18Z batch).

**Alert-visible abstract lead.**
> A randomized controlled trial typically involves one or more causal
> contrasts of interest, including intention-to-treat (ITT) and
> per-protocol effects. The ITT effect refers to the effect of
> treatment assignment, regardless of adherence. A per-protocol effect
> commonly refers to the effect of adhering to an assigned treatment
> protocol. The ITT comparison is often regarded as the preferred
> approach for randomized trials, largely because it preserves the
> benefits of randomization and can therefore be …

**Why it fits.** This is the ITT-vs-PP framing paper every
drug-persistence and medication-adherence analysis under your
`Pharmacogenomic modifiers of medication persistence` sub-thread has
to navigate. Especially relevant for CFTR-modulator persistence,
statin discontinuation, HRT persistence, GLP-1 RA persistence — all
of which have contested PP definitions in the current literature.

**Triage.** HIGH (methods) — pull PDF and add to the causal-inference
teaching-reference set alongside Hernán & Robins *Causal Inference:
What If*.

---

### 6. Vossler, Ouyang, Guo, Huang, Shojaie, Zier, Xia, Feng — Expert-Guided g-computation (egg-computation) with LLMs for causal effects on timings (arXiv 2608.10339)

**Citation.** P Vossler, J Ouyang, FR Guo, A Huang, A Shojaie, L Zier,
F Xia, J Feng. Expert-Guided g-computation with Large Language Models
for Estimating Causal Effects on Timings: Applications to Hospital
Quality Improvement. arXiv 2608.10339v1, submitted 2026-08-11.

**Source.** `arxiv-digest/digests/2026-08-12.md` (stat.ME; score 2 —
`causal inference` + `g-computation`).

**Full-abstract summary.** Hospital QI programs face many candidate
interventions on hospital flow; egg-computation combines expert
Gantt-chart mapping of patient trajectories with a causal DAG variant
of g-computation, using an LLM-assisted pipeline that seeks expert
input only for components not identifiable from data. In simulations
they outperform conventional causal inference when patients have
diverse causal structures. In an 11-intervention study at an urban
safety-net hospital, LLM-generated graphs and time-saving estimates
were highly concordant with human experts. Framing is generalizable
beyond healthcare to any average-time-saved question representable in
Gantt charts.

**Why it fits.** Directly serves the *Agentic / human-in-the-loop
observational-causal-inference pipelines* rising sub-thread under
`Causal inference`. Same lineage as Chou/Kallus `oci-agent` arXiv
2607.22443 and Li et al. arXiv 2607.16934 (both anchored in `INTERESTS.md`
2026-07-29 update). The clever move here is using LLMs *only for the
non-identifiable components*, which is a defensible boundary — the
model isn't estimating effects, it's specifying structure.

**Triage.** HIGH — this is a template you can lift for any
CFTR-modulator or GLP-1-RA target-trial emulation where the
mechanistic story requires expert Gantt-chart-style time reasoning
(e.g., time-to-modulator-initiation as a function of eligibility
review workflow).

---

### 7. Wood, Platt, Hutcheon, Cohen, Latour, Margulis, Petito, Grandi — Perinatal pharmacoepi TTE for early-pregnancy treatment decisions (arXiv 2608.11108)

**Citation.** ME Wood, RW Platt, JA Hutcheon, JM Cohen, CD Latour,
AV Margulis, LC Petito, SM Grandi. Early Pregnancy Treatment
Decisions: Designing Perinatal Pharmacoepidemiology Studies using
Real-World Data. arXiv 2608.11108v1, submitted 2026-08-11.

**Source.** `arxiv-digest/digests/2026-08-12.md` (stat.AP; score 1 —
`target trial emulation`).

**Full-abstract summary.** Target trial emulation extended from
initiation-vs-non-initiation of point treatments (vaccines,
antibiotics) in pregnancy to *changes in pregestational treatment
regimes*, using T2D as the worked example. Reviews methods for
identifying pregnancy episodes in routinely collected healthcare
data, introduces candidate time-zero definitions, and discusses
analytic approaches that minimize bias from selection and immortal
person-time — all the machinery specific to pregnancy: right/left
censoring, competing events, gestational length differences,
etiologically susceptible periods.

**Why it fits.** Serves both `Causal inference and pharmacoepidemiology`
(TTE for pregnancy pharmacoepi is under-tooled) and the *Pharmacogenomic
modifiers of medication persistence* sub-thread when persistence
outcomes span pregnancy episodes (a real issue for antidepressants,
metformin, and increasingly GLP-1 RAs). Portable directly to a CFTR-
modulator-in-pregnancy target-trial question if AoU or MVP develop
that cohort.

**Triage.** HIGH — read full text; useful as a design-mechanics
reference for any future perinatal pharmacoepi analysis on
AoU/MVP/BioVU.

---

### 8. Yap & Morris — PANACEA framework for maximising genetic diversity in GWAS meta-analyses (medRxiv 2026)

**Citation.** CF Yap, A Morris. PANACEA: a framework to maximise
genetic diversity in genome-wide association study meta-analyses.
*medRxiv*, 2026. DOI 10.64898/2026.08.06.26359891.

**Source.** Google Scholar author feed — *Joshua C. Denny — new
related research* (Aug-14 15:18Z batch).

**Alert-visible abstract lead.**
> There have been recent efforts by the human genetics research
> community to increase the genetic diversity of participants
> contributing to genome-wide association studies (GWAS) of complex
> human traits and diseases. The traditional multi-ancestry …

**Why it fits.** Serves `Genetic epidemiology` — specifically the
*cross / trans-ancestry portability* line and its downstream impact
on PGS. The value of a *framework* rather than another applied paper
is that it can be reused across your active disease threads (CFTR,
APOL1, breast-cancer PRS lineage) whenever you need to justify
particular meta-analytic weighting or subset choices for a diverse
cohort. Same batch also flags Hu et al. and Smeriglio et al. (below),
suggesting this is a small clustered release of local-ancestry-aware
methodology.

**Triage.** HIGH — pull the preprint and compare its meta-analytic
architecture to the standard fixed-effect / MR-MEGA / trans-ancestry
inverse-variance families before deciding whether to adopt it as the
default for future cross-ancestry meta-analyses.

---

### 9. Hu, Tan, Yuan, Wang, Gorissen, Lin et al. — Unified framework for local-ancestry-aware genetic association across biobanks (medRxiv 2026)

**Citation.** L Hu, T Tan, K Yuan, Y Wang, BL Gorissen, YS Lin et al.
A unified framework for local-ancestry-aware genetic association
analysis across biobanks. *medRxiv*, 2026.
DOI 10.64898/2026.08.09.26360047.

**Source.** Google Scholar author feed — *Joshua C. Denny — new
related research* and *Lisa Bastarache — new related research*
(same 08-14 batch, cross-listed).

**Alert-visible abstract lead.**
> Biobanks increasingly include individuals with admixed genomes, yet
> conventional genome-wide association study frameworks either exclude
> participants who cannot be confidently assigned to a discrete
> ancestry group or ignore ancestry-specific …

**Why it fits.** Directly targets the *biobanks with EHR linkage:
AoU / UKB / MVP / BioVU* thread's most acute open problem: how to
run association analyses on admixed genomes without either dropping
those participants (which is what BioVU has historically had to do)
or ignoring local-ancestry heterogeneity (which is what most single-
cohort UKB pipelines do). If the framework is compatible with
imputed-genotype pipelines and PheWAS-scale QC, this could be a
default addition to your AoU/MVP pipeline stack.

**Triage.** HIGH — verify data availability and pipeline license;
if permissive, evaluate on a small AoU PheWAS scan as a shakedown.

---

### 10. Smeriglio, Moreno-Grau, Mas Montserrat et al. — Multi-ancestry admixture mapping in UKB (medRxiv 2026)

**Citation.** R Smeriglio, S Moreno-Grau, D Mas Montserrat et al.
Multi-ancestry admixture mapping reveals ancestry-associated disease
loci in the UK Biobank. *medRxiv*, 2026.
DOI 10.64898/2026.08.06.26359859.

**Source.** Google Scholar author feeds — *Joshua C. Denny — new
related research* and *Konrad Karczewski — new related research*
(Aug-14 15:18Z batch, cross-listed).

**Alert-visible abstract lead.**
> Genome-wide association studies have successfully identified
> thousands of genetic associations, yet their predominant reliance on
> European-descent populations limits insights into the full spectrum
> of human genetic diversity and its impact on disease …

**Why it fits.** Companion to the Hu et al. paper (above) — admixture
mapping is a distinct signal from local-ancestry-aware association;
they answer complementary questions ("which segment of the genome
carries ancestry-linked risk?" vs "given a specific variant, how
does its effect vary by local ancestry?"). Together they upgrade the
UKB analytic toolkit for the composite-risk / PGS-portability sub-thread.

**Triage.** HIGH — read the two together, decide which fits which of
your active UKB PheWAS threads (APOL1 for the ancestry-specific side,
early-onset BC for the portability side).

---

### 11. Li, Peng, Zhang, Huang, Wei, Liu, Fang — Scalable framework for phenome-wide association of structural variants in biobank cohorts (Research Square 2026)

**Citation.** M Li, W Peng, L Zhang, T Huang, C Wei, Z Liu, L Fang.
A scalable framework enables phenome-wide association of structural
variants in biobank cohorts. Research Square, 2026. rs-10237876.

**Source.** Google Scholar author feed — *Konrad Karczewski — new
related research* (Aug-14 15:18Z batch).

**Alert-visible abstract lead.**
> Genomic structural variants (SVs) constitute a major source of
> human genetic diversity and disease susceptibility. Yet,
> population-scale SV genetics lacks a viable mechanism to
> synthesize massive individualized callsets into reliable cohort …

**Why it fits.** Directly extends your `PheWAS / phecode infrastructure`
thread from SNV/indel PheWAS to structural-variant PheWAS at biobank
scale. SV-PheWAS is a category that until recently had been either
avoided or run per-locus; a scalable framework would let existing
phecode outcome definitions inherit into SV analyses without a
custom cohort-build.

**Triage.** HIGH — pull the preprint; if the framework is
phecode-compatible and outputs are standard summary-stat format, it
could slot directly into your PheWAS pipeline stack.

---

### 12. Tithi, Cooper-Knock, Benatar, Wuu, Taylor et al. — CoCoRV-nf: cost-effective rare-variant analysis leveraging external biobank sequence data (*Human Molecular Genetics* 2026)

**Citation.** SS Tithi, J Cooper-Knock, M Benatar, J Wuu, JP Taylor et al.
CoCoRV-nf: a powerful and cost-effective tool for rare variant
analysis leveraging external biobank sequence data identified new
candidate predisposition genes in amyotrophic lateral sclerosis and …
*Human Molecular Genetics*, 2026. 35(17):ddag076.

**Source.** Google Scholar author feed — *Konrad Karczewski — new
related research* (Aug-14 15:18Z batch).

**Alert-visible abstract lead.**
> Although sequencing costs have steadily decreased with advances in
> technology, they remain high for large scale studies. The design of
> traditional individual-disease sequencing studies is either case
> only or cases with relatively few controls, resulting …

**Why it fits.** Serves three threads at once:

- `Variant interpretation (ACMG / ClinGen)` and `Rare disease` — a
  cost-effective rare-variant burden framework that leverages *external*
  biobank controls (e.g., gnomAD, UKB WES) is exactly the tooling
  category ACMG-AMP practitioners have been waiting for.
- `Genetic epidemiology / composite risk` — new candidate ALS
  predisposition genes feeds directly into the Ran/Benatar
  pre-symptomatic phenoconversion trajectories sub-thread (Benatar is
  an author here).
- The ALS anchor connects to Ran/Benatar *Nature Medicine* 2026 template
  from your `Rare disease` thread — the two together give a variant-
  discovery-plus-phenoconversion-trajectory story that other rare-disease
  domains (CFTR, APOL1, hereditary cancer) could copy.

**Triage.** HIGH — read full paper for the exact external-control
handling (bias correction, ancestry matching); then decide whether to
apply to a CFTR-modifier-search or BRCA-modifier-search of your own.

---

### 13. Liu, Liang, Paredes, Moreira, Caro-Vega et al. — Authentic Multinational Federated Time-to-Event Analyses among People with HIV in Latin America (arXiv 2026)

**Citation.** K Liu, ZJ Liang, F Paredes, RI Moreira, Y Caro-Vega et al.
Authentic Multinational Federated Time-to-Event Analyses Among People
with HIV in Latin America. arXiv preprint, 2026.

**Source.** Google Scholar author feed — *Yong Chen — new articles*
(Aug-14 15:18Z batch).

**Alert-visible abstract lead.**
> Multinational …

(Abstract truncated in Scholar snippet; the paper is a federated TTE
analysis across Latin American HIV sites.)

**Why it fits.** Directly serves the *Federated / privacy-preserving
EHR causal analytics* rising sub-thread under `Causal inference`.
The same Jang et al. arXiv 2607.17958 design pattern (from your
`INTERESTS.md` 2026-07-29 update), now applied to a real multinational
HIV cohort in Latin America. This is the kind of "in-production
federated TTE across health systems" study that turns the sub-thread
from methods-watch into a working pattern.

**Triage.** HIGH — read for design of the network (site-level
privacy budget, meta-analytic aggregation strategy) and for
generalizability to any All-of-Us × VA × BioVU cross-network TTE
you might want to propose.

---

### 14. Aldana Peréz, Domínguez-Vargas et al. — APOL1 risk genotypes and lupus nephritis-associated kidney failure in SLE: systematic review + meta-analysis (*Frontiers in Medicine* 2026)

**Citation.** SA Aldana Peréz, A Domínguez-Vargas et al. Apolipoprotein
L1 Risk Genotypes and Odds of Lupus Nephritis-Associated Kidney
Failure in Systemic Lupus Erythematosus: A Systematic Review and
Meta-Analysis. *Frontiers in Medicine*, 2026.
DOI 10.3389/fmed.2026.1903888.

**Source.** Google Scholar keyword feed — *APOL1 — new results*
(Aug-13 13:33Z batch).

**Alert-visible abstract lead.**
> … interferon signature that upregulates apolipoprotein L1 (APOL1)
> expression. High-risk APOL1 genotypes have been associated with
> end-stage … Methods: We conducted a systematic review and
> meta-analysis of observational studies to evaluate the …

**Why it fits.** Extends the APOL1 disease thread from HIV-associated
nephropathy, hypertensive CKD, and FSGS (Chen et al. *JASN* p.N264K,
Kim & Lee *Sclerosis* inhibitor, Gaheer & Lanktree KI proteomic score
from the prior digest window) into the *SLE lupus-nephritis*
compartment. The mechanistic hinge (SLE interferon signature
upregulating APOL1 → high-risk-genotype-dependent kidney failure) is
important because it means the APOL1 pharmacological inhibitor
program has a candidate second indication beyond FSGS.

**Triage.** HIGH — read the pooled OR and heterogeneity, and update
the APOL1 mini-review in `INTERESTS.md` to list *four* disease-
compartment evidence points (HIVAN → hypertensive/FSGS → CKD →
lupus-nephritis-SLE) rather than three.

---

### 15. Motisi, Di Salvo, Balistreri — CHIP as an emerging determinant of inflammageing and age-related disease (*Ageing Research Reviews* 2026)

**Citation.** C Motisi, A Di Salvo, CR Balistreri. Clonal hematopoiesis
of undetermined potential as an emerging determinant of inflammageing,
and age-related diseases: potential role as biomarker and target.
*Ageing Research Reviews* (or *Ageing Res* family), 2026.

**Source.** Google Scholar keyword feed — *intitle:"clonal
hematopoiesis" — new results* (Aug-14 19:16Z batch).

**Alert-visible abstract lead.**
> Clonal hematopoiesis of undetermined potential as an emerging
> determinant of inflammageing, and age-related diseases: potential
> role as biomarker and target …

**Why it fits.** Framing-paper anchor for the CHIP arm of the
somatic-mosaicism thread (`CHIP, VEXAS, and mosaic Loss of Y (LOY)`).
Ageing-Research-Reviews is a high-visibility conceptual venue —
useful as a citation when you need one sentence for the introduction
of a manuscript on CHIP × cardiovascular or CHIP × solid-tumor risk,
or when explaining the *biomarker-and-target* pitch that motivates
CHIP-directed therapy development.

**Triage.** HIGH — read for how the review frames inflammageing (as
distinct from cellular senescence or immunosenescence) and whether it
covers LOY in the same breath; if it doesn't cover LOY, that is a
gap worth noting for your `LOY × PAD` line (Li et al.
*Atherosclerosis* 2026).

---

### 16. Wang, Sargent, Mathieu, Vazquez-Arreola et al. — Type 2 diabetes prevention across the life course (*Nature Medicine* 2026)

**Citation.** Y Wang, JL Sargent, C Mathieu, E Vazquez-Arreola et al.
Type 2 diabetes prevention across the life course. *Nature Medicine*,
2026. Article s41591-026-04550-z.

**Source.** Google Scholar cite feed — *10 new citations to articles by
Joshua C. Denny* (Aug-14 15:18Z batch). Cites: *Genetic drivers of
heterogeneity in type 2 diabetes pathophysiology* (Denny-lineage).

**Alert-visible abstract lead.**
> Abstract Type 2 diabetes (T2D) prevention efforts have largely
> focused on intervening when dysglycemia is already established. We
> propose that T2D prevention be reframed around prediabetes remission,
> with preservation and restoration of normoglycemia as the optimal
> clinical goal. The transition from normoglycemia through increasing
> dysglycemia to T2D is progressive and cumulatively shaped by
> biological, behavioral and environmental exposures across …

**Why it fits.** Framing paper for the T2D leg of the `Causal inference
and pharmacoepidemiology` drug-class watchlist (GLP-1 RA / SGLT2i /
metformin), because it explicitly reframes prevention as
prediabetes-remission and normoglycemia-restoration — that framing
shifts the pharmacoepi question from "does drug X reduce incident T2D"
to "does drug X *reverse* dysglycemia," which is a different target-trial
estimand. Also connects to the Berkowitz *JAMA IM* Medicare-Advantage
piece above (both are T2D-outcomes framings, one at insurance-benefit
level and one at life-course level).

**Triage.** HIGH — read as a co-anchor with Berkowitz et al. and use
the two together as the T2D-pharmacoepi framing pair for the next 12
months of that watchlist.

---

## Bonus: Cell paper worth flagging under Genetic epidemiology

### 17. Salamone, Tian, Qi, Zhao, Zhang, Tan, Li et al. — DANDELION: trans-regulatory gene mapping prioritizes disease-proximal genes in asthma (*Cell* 2026)

**Citation.** IM Salamone, P Tian, Z Qi, J Zhao, L Zhang, Q Tan, J Li et al.
Trans-regulatory gene mapping prioritizes disease drivers in asthma.
*Cell*, 2026. Article S0092867426008664.

**Source.** Google Scholar cite feed — *10 new citations to articles by
Jonathan K Pritchard* (Aug-14 15:18Z batch).

**Alert-visible abstract lead.**
> Deciphering which genes are most important to disease etiology is a
> central challenge in human genetics. While genome-wide association
> studies have cataloged thousands of variants, it's been proposed that
> most are indirect regulators of a limited, currently unidentified set
> of central disease-driving genes, defined here as disease-proximal
> genes (DPGs). Here, we introduce DANDELION, a mediation-inspired
> statistical framework that prioritizes DPGs by integrating
> trans-regulatory …

**Why it fits.** Directly serves `Genetic epidemiology` — a
disease-proximal-gene framework built on trans-regulatory mediation is
the natural methodological successor to the omnigenic-model /
core-vs-peripheral-gene lineage that Pritchard's lab has been pursuing.
Asthma is the anchor disease here, but the framework is portable.
Cross-references your `Knowledge representation in EHRs` thread's
"which representation choice drives downstream performance" sub-topic
in an oblique but relevant way (the representation choice here is at
the *regulatory-network* layer, not the *EHR-code* layer, but the
question shape is the same).

**Triage.** HIGH — read full text; consider whether DANDELION could be
retrofitted onto a UKB/AoU IBD or CFTR modifier scan by swapping the
trans-eQTL input for a UKB blood/proteomics trans layer.

---

## Methods-watch appendix (short entries, not HIGH)

- **Kevopoulos, Moscoloni, Alheit, Beeche, Chirinos, Heinlein, Peirlinck.
  CAN-FLOW: two-step Conditional ANatomy generation via normalizing FLOWs
  from 2,208 UK Biobank subjects → 47k UKB scans externalized.**
  (`arxiv-digest/digests/2026-08-11.md`, arXiv 2608.09460.) Cardiac
  digital-twin thread. Sex/age/BMI-conditioned generative model of
  biventricular anatomy that outperforms conditional-VAEs on
  metadata-dependent trends and subgroup variability. Adjacent to your
  *digital-twins-from-EHR-data* rising sub-thread but the modality is
  imaging-only.

- **Chen, Zuo, Stevens, Pollack, Xi, Petito, Zhao, Zhang. Clustering
  Informed Inverse Probability Weighting for causal-effect estimation
  in observational studies.** (`arxiv-digest/digests/2026-08-11.md`,
  arXiv 2608.09839.) Compares standard IPW, cluster-augmented IPW with
  cluster-specific PS models, and a global PS model with cluster
  membership as covariate. Applied to n=966 breast-cancer patients on
  carboplatin with a generalized-PS dose-response for hypersensitivity
  reactions. Methods-watch under `Causal inference and pharmacoepi`.

- **Bandreddi, Zhang, Kelly, Machiela, Albert. Comparing Tobit and
  Two-Part Hurdle Models for semi-continuous longitudinal CH data.**
  (`arxiv-digest/digests/2026-08-11.md`, arXiv 2608.09725.) Derives
  the equivalence conditions (Tobit is a hurdle special case when the
  binary process uses a probit link) and applies to longitudinal
  clonal-fraction dynamics from the PLCO study. Methodology for the
  CHIP longitudinal-trajectory arm.

- **Porotsky. Inverse Confounding Analysis (ICA): an exact method for
  quantifying the significance of confounding.**
  (`arxiv-digest/digests/2026-08-13.md`, arXiv 2608.11991.) Extends
  the E-value approach past worst-case bounds to the *complete*
  admissible-configuration set via an analytical inverse-problem
  formulation. Adds a sensitivity-analysis primitive that the causal-
  inference thread should evaluate as an alternative to E-value defaults.

- **Cameron, Katzman, Lalonde, Tetreault. NSAIDs and CYP2C9 — Impacts of
  genetics and phenoconversion on the risk of adverse effects.**
  (*Clin Biochem* 2026; Denny cite feed.) Extends the *pharmacogenomic
  modifier of medication persistence* sub-thread from CYP2D6 to CYP2C9
  and from psychiatric to analgesic classes. Relevant as a template for
  any pharmacogenomic-persistence analysis on AoU or MVP.

- **Weaver, Petry, Cauwels, Lupu et al. Prompt engineering of LLMs for
  medication dose calculation.** (*Clin Pharmacol Ther* 2026; Denny cite
  feed.) Five LLMs (Mistral-small, Llama 3-70B, Nova lite, DeepSeek,
  Claude 3.5 Sonnet) tested via iterative prompt engineering on 4,295
  manually annotated medications across 9 therapeutic classes. Cites
  medExtractR. Relevant as an EHR NLP infrastructure piece for the
  `EHR phenotyping & OMOP` thread.

- **Li, Qu, March, Glessner, Fu, Chen et al. Shared genetic architecture
  and therapeutic targets across 24 paediatric immune-mediated
  diseases.** (*Ann Rheum Dis* 2026; Denny cite feed.) Autoimmune vs
  polygenic-autoinflammatory vs mixed-pattern vs allergic classification.
  Complements the IBD leg of your disease thread with a pediatric
  transdiagnostic view.

- **Lähteenmaa. How Do Causal Structures Affect Model Selection?
  Heterogeneous Treatment Effect Estimation with Observational Data.**
  (Univ. Helsinki thesis via Hripcsak related-research feed.) HTE model
  selection as a function of underlying causal DAG structure — a topic
  your `Machine learning for precision health` thread's HTE sub-line
  should track.

- **Charpentier. From Rating Factors to Crash Mechanisms: Multiscale
  Causal DAG framework linking motor insurance and road safety.**
  (`arxiv-digest/digests/2026-08-11.md`, arXiv 2608.09441.) Not on-topic
  clinically but the *set-valued identification framework* — characterizing
  which mechanism laws are compatible with an observed contrast rather
  than estimating a single effect — is a useful pattern to remember for
  the causal-inference thread when observational evidence is inherently
  under-identified.

- **Bandreddi et al. and Porotsky are also both in `arxiv-digest`;**
  they overlap between HIGH-priority (CH thread) and methods-watch (CI
  thread) — listed here for the second framing only.

---

## Update suggestions for INTERESTS.md

Based on this window's surfacing:

1. Under `EHR foundation models`, add Venkatesh & Ritchie *Nat Rev
   Genet* 2026 as the *field-defining review reference for multimodal
   EHR × genomics integration*. This is the paragraph-opener.
2. Under `Causal inference and pharmacoepidemiology → agentic /
   human-in-the-loop`, add Vossler et al. arXiv 2608.10339
   (*egg-computation*) to the anchor list alongside Chou/Kallus and
   Li et al.
3. Under `Causal inference and pharmacoepidemiology → federated /
   privacy-preserving`, add Liu et al. HIV-Latin-America federated TTE
   as a *deployed* companion to the Jang et al. anchor.
4. Under `Specific disease threads → APOL1`, expand from three
   evidence-points to four: HIVAN → hypertensive/FSGS → CKD proteomic
   score → **lupus-nephritis-SLE** (Aldana Peréz et al. 2026).
5. Under `Rare disease`, keep the Ran/Benatar template but add
   CoCoRV-nf (Tithi et al. 2026 Benatar co-authored) as the paired
   *variant-discovery* infrastructure that makes the phenoconversion
   template actionable.
6. Under `Genetic epidemiology`, add Salamone/DANDELION *Cell* 2026 as
   a reference framework for *disease-proximal-gene* prioritization —
   the mediation-inspired successor to omnigenic-model literature that
   your composite-risk sub-thread should track.
