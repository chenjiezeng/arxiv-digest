# Research digest report — 2026-08-16

Triage of research-related email + the GitHub `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant interpretation,
genetic epi, disease threads incl. CF/APOL1/CHIP-VEXAS-LOY/IBD, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity, knowledge representation in EHRs).

Window: **2026-08-09 12:36Z → 2026-08-16 12:35Z** (~8 days since the last
research-digest report on 2026-08-08). Covers six `arxiv-digest` cron runs
with content (08-11 → 08-13) and three Google Scholar alert batches
(08-13, 08-14, 08-15).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-09.md` → `2026-08-16.md`) | 08-09 → 08-16 (10:30Z crons) | Cron ran daily. 08-09/10 no content files (weekend arXiv gap). **08-11: 5 papers** (2 causal-inference / IPW, 1 UKB imaging, 1 clonal hematopoiesis, 1 spatial omics FM). **08-12: 2 papers** (LLM-assisted g-computation, perinatal target trial emulation). **08-13: 1 paper** (Inverse Confounding Analysis; 5 previously surfaced suppressed). **08-14 → 08-16: 0 net-new** (2 → 1 → 0 previously-surfaced suppressed). Quiet week overall — the 08-11 batch is the anchor. |
| Google Scholar alerts (author feeds, 08-14 batch) | 08-14 15:18Z | ~15 author feeds fired. Highlights: **Nigam Shah** new-articles (ChatEHR Nat Med), **Emily Alsentzer** (clinical-FM privacy), **James Zou** (conversational clinical measurement), **Marinka Zitnik / Peter Szolovits / Zhiyong Lu / Pascal Brandt** (all surfacing the *Scaling Inherently Interpretable Language Models* Goodfire team paper), **Yong Chen** (federated time-to-event in HIV Latin America), **Vivek Natarajan** (real-time medical video consultation AI). |
| Google Scholar alerts (author + keyword feeds, 08-15 batch) | 08-15 18:09Z + 20:57Z | ~30 alerts. Highest signal: **Chenjie Zeng self-alert** (Kachhadia et al. — RAO × incident dementia in All of Us using prespecified negative-control outcomes), **Joshua C Denny** (same Kachhadia et al.), **Miguel Hernán** citation cluster (Burgess et al. AJE on emulating drug-development phases; 3 fresh TTE applications), **Lisa Bastarache related** (Lin et al. East-Asian GGT cross-biobank), **Jian Yang related** (Ao et al. Genome Med — UKB chronic-pain ExWAS n=327,642), **Konrad Karczewski / Denny** (Hansen et al. AJHG — sub-Saharan African cardiometabolic GWAS), **Kai Wang** (Trucco multimodal variant prioritization), **George Hripcsak related** (Linz et al. PLOS ONE — Lyme-disease EHR phenotyping), and keyword feeds on APOL1 / knowledge graph / UK Biobank / rare disease / autoimmune / drug repurposing / All of Us / variant interpretation / clonal hematopoiesis. |
| Google Scholar alerts (`clonal hematopoiesis` + `Foundation models` × EHR keyword feeds, 08-13 batch) | 08-13 13:33Z | 2 keyword-feed batches. Confirmed the Bandreddi et al. Tobit-vs-hurdle paper already caught by `arxiv-digest`, and surfaced the **Venkatesh & Ritchie *Nature Reviews Genetics*** review on AI-based multimodal genomics × EHR integration. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract. The reports below contextualize that
> metadata against the tracked threads; nothing here reflects full-text
> reading. `arxiv-digest` entries include the full abstract because the
> pipeline captures it. Author lists are truncated to the first 3–5 as
> they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Six HIGH-priority items surfaced this window, clustering into three knots:

**Detection-bias-calibrated AoU + negative-control-outcomes cluster (1 item, top of stack).**
Kachhadia et al. *J Clin Med* — RAO × incident dementia in All of Us with
prespecified negative-control outcomes as a detection-bias calibrator. This
appeared in *both* the Chenjie Zeng self-alert feed and the Denny feed on
08-15, which is the strongest possible signal-of-signal: the paper sits
directly on the AoU-EHR + calibrated-cohort-inference methodology line and
mirrors your own methodological work. Full writeup below.

**Causal inference / pharmacoepi methods cluster (3 items, all `arxiv-digest`).**
Vossler et al. arXiv 2608.10339 — **egg-computation** wraps g-computation with
LLM-assisted expert elicitation over Gantt-chart-derived DAGs; validated on
11 hospital QI interventions at an urban safety-net hospital with LLM/expert
concordance on time-saved estimates. Directly overlaps the *agentic /
human-in-the-loop observational causal-inference pipelines* sub-thread you
added in July. Wood et al. arXiv 2608.11108 — perinatal pharmacoepi TTE
design for pregestational treatment regimes (T2DM as worked example),
with immortal-time-and-selection-bias treatment aligned to early-pregnancy
treatment decision points; extends the existing prenatal TTE literature
which had focused on point-treatment initiation. Burgess et al. *AJE* —
maps the drug-development-phase framework onto epidemiological emulation:
which trial phases can and cannot be emulated; adjacency to MR / drug-target
MR literature. This closes a longstanding gap in the TTE-emulation literature
that your CFTR-modulator and GLP-1 threads both intersect.

**AI × genomics × EHR foundational-review cluster (2 items).**
Venkatesh & Ritchie *Nature Reviews Genetics* — field-defining review on
AI-based multimodal integration of genomics and EHR, prioritizing FM-based
architectures. This is the reference paper for your *EHR foundation models*
thread (Ritchie lab pedigree, NRG venue, FM-centered framing). Shah et al.
*Nature Medicine* — Stanford ChatEHR real-world-deployment lessons; explicit
message is that benchmark-based evaluations are insufficient for
clinician-driven LLM interactions, requiring new interaction-monitoring
methods. Direct feed into the EHR-FM audit / calibration thread.

**Emerging: single-paper items still worth tracking.**
Bandreddi et al. arXiv 2608.09725 — Tobit-vs-hurdle formal equivalence
conditions for zero-inflated longitudinal clonal-fraction data, PLCO
application. This closes a methodological hole in the CHIP / mosaic-CA
longitudinal-modeling literature that your CHIP-VEXAS-LOY thread flags.
Ao et al. *Genome Medicine* — UKB exome-wide association study of chronic
pain in n=327,642 with joint common+rare coding-variant analysis. HIGH on
methods (largest ExWAS-of-pain to date, joint framing) even though pain is
not a primary disease thread.

---

## Detailed writeups (HIGH items)

### 1. Kachhadia et al. 2026 — Retinal Artery Occlusion and Incident Dementia in the All of Us Research Program: Detection Bias Calibration with Prespecified Negative-Control Outcomes

- **Venue:** *Journal of Clinical Medicine* (2026), PMC13456938
- **Authors (first 5):** MP Kachhadia, P Puri, U Topiwala, JD Shaikh, G Gill et al.
- **Feeds that surfaced it:** Chenjie Zeng self-alert (08-15); Joshua C Denny related-research (08-15). Two-feed convergence.
- **INTERESTS.md threads:** Biobanks with EHR linkage (AoU), EHR phenotyping & OMOP, causal inference / pharmacoepi (detection-bias calibration is the OHDSI / Schuemie negative-control lineage), ML for precision health.

**Snippet (from the alert):**
> Background: Retinal artery occlusion (RAO) shares vascular pathophysiology
> with cerebrovascular disease, and its relationship to incident dementia
> remains unsettled. Reported associations may reflect shared vascular
> pathology, differential [surveillance/detection] …

**Why it matters here.** The methodological hook is *prespecified*
negative-control outcomes as a calibrator for detection bias — the exact
design pattern you're likely to want to import for any AoU-based
association study where surveillance for the outcome (dementia here) is
differential between exposed vs. unexposed. RAO patients have vastly more
ophthalmology and neurology follow-up than matched controls, so a naïve
RAO → dementia association is confounded by ascertainment; the prespecified
NC-outcomes design lets you empirically estimate and back out that
detection-bias component. This is precisely the framing you'd apply to
several of the CFTR-modulator persistence and hereditary-cancer surveillance
questions in your active-threads list. Read the methods section carefully
for how they chose the NC set and calibrated point estimates.

**Do next:** pull the full paper (PMC13456938 open access). Note the AoU
release used, the phecode / condition-occurrence definitions of dementia,
and the negative-control panel; that panel is likely reusable across your
own AoU analyses. Cross-check against Schuemie/Ryan/Hripcsak
empirical-calibration papers to make sure the estimator matches (they use
a null-distribution parameter estimated from NCs, then shift the
target-outcome effect estimate).

### 2. Vossler et al. 2026 — Expert-Guided g-computation with Large Language Models for Estimating Causal Effects on Timings: Applications to Hospital Quality Improvement (arXiv 2608.10339, "egg-computation")

- **Venue:** arXiv 2608.10339v1 (stat.ME), submitted 2026-08-11
- **Authors:** Patrick Vossler, Jialin Ouyang, F. Richard Guo, Anran Huang, Ali Shojaie, Lucas Zier, Fan Xia, Jean Feng
- **`arxiv-digest` keyword hits:** causal inference, g-computation (score 2)
- **INTERESTS.md threads:** Causal inference & pharmacoepi (agentic / HITL sub-thread), EHR foundation models (LLM-agent tie-in), ML for precision health.

**Abstract highlights.** Hospital QI programs juggle multiple candidate
interventions on the same flow metric (LOS). Qualitative expert-DAG
approaches suffer from cognitive bias; quantitative approaches fail when
interventions are hypothetical (no historical data) or when clinical
reasoning is needed alongside data. The authors introduce a causal model
over Gantt charts and establish identification via a variant of
g-computation that asks the expert only for the components *unidentifiable
from data*. They then implement an LLM-assisted pipeline for the
expert-elicitation step. Simulations beat conventional CI when patients
have heterogeneous causal structure. Applied to 11 QI candidates at an
urban safety-net hospital; LLM-generated DAGs and time-saved estimates
were highly concordant with human experts.

**Why it matters here.** This is a clean instantiation of the *agentic /
human-in-the-loop observational-causal-inference pipeline* sub-thread you
added to INTERESTS.md in July (Chou/Kallus `oci-agent`, Li et al. EHR HTE
for trial design). The Gantt-chart-to-DAG bridge is a general-purpose
identification trick: any temporal healthcare workflow where you can
articulate the process visually can now be run through the same LLM +
g-computation pipeline. Portable to CFTR-modulator initiation-and-persistence
workflow analyses and to any medication-adherence intervention.

**Do next:** grab the code (usually released with the arXiv preprint for
this author group) and try it on one of your existing LOS / adherence
questions. Watch for: how do they identify which DAG components are
*unidentifiable from data*? That's the load-bearing step — if it's just
"whatever the LLM can't recover from the observed graph structure", it
imports the LLM's biases into the causal model.

### 3. Wood et al. 2026 — Early Pregnancy Treatment Decisions: Designing Perinatal Pharmacoepidemiology Studies using Real-World Data (arXiv 2608.11108)

- **Venue:** arXiv 2608.11108v1 (stat.AP), submitted 2026-08-11
- **Authors:** Mollie E. Wood, Robert W. Platt, Jennifer A. Hutcheon, Jacqueline M. Cohen, Chase D. Latour, Andrea V. Margulis, Lucia C. Petito, Sonia M. Grandi
- **`arxiv-digest` keyword hits:** target trial emulation (score 1)
- **Also caught by:** Hernán citation feed (08-15).
- **INTERESTS.md threads:** Causal inference & pharmacoepi (TTE), EHR phenotyping & OMOP.

**Abstract highlights.** Previous perinatal-TTE work has focused on
point-treatment initiation (e.g., vaccine, antibiotic). Wood et al. extend
the framework to *changes in pregestational treatment regimes* — the
harder pharmacoepi question, because time zero is no longer initiation.
They use T2DM treatment as the worked example, review methods for
identifying pregnancy episodes in routinely collected healthcare data,
introduce candidate time-zeros (pre-conception decision point, first
prenatal visit, positive pregnancy test), and analytic strategies to
minimize immortal-time and selection bias.

**Why it matters here.** The design pattern extends naturally to
CFTR-modulator persistence *through pregnancy*, HRT persistence around
menopause, statin discontinuation on hospitalization, and GLP-1 RA
discontinuation on weight-goal attainment — all of which are
"change-of-existing-regime" TTE questions where the perinatal
literature is furthest ahead. Also worth propagating the immortal-time
alignment recipe to your active pharmacoepi threads.

**Do next:** archive as a design-pattern reference. The right analog to
transfer first is CFTR modulator persistence during pregnancy in the
CFF Patient Registry / AoU-linked pregnancies, which is a live question
in the community.

### 4. Burgess et al. 2026 — What phases of the drug development framework can epidemiological studies emulate? (*American Journal of Epidemiology*)

- **Venue:** *AJE* (2026), advance article, doi:10.1093/aje/kwag194
- **Authors (first 5):** Stephen Burgess, Benjamin Woolf, Emily Bassett, Daniel Robertson, Sofía Villar et al.
- **Feeds:** Hernán citation feed (08-15).
- **INTERESTS.md threads:** Causal inference & pharmacoepi, genetic epi (drug-target MR sub-thread), rare disease (repurposing).

**Snippet.**
> Target trial emulation prompts investigators to frame their analysis
> question in terms of a hypothetical clinical trial. Although this does
> not solve the problem of confounding, the framework can protect against
> other sources of bias. A natural question is this: what kinds of trials
> can be emulated? In a late-phase trial (Phase 3 or 4), the goal is to
> obtain a well-defined causal estimate that closely approximates the
> impact of a proposed intervention. In an early-phase trial (Phase 2 or
> earlier), the [goals differ] …

**Why it matters here.** This is the paper that names the elephant in the
TTE room: which trial *phase* is a TTE actually emulating? Phase 3/4 TTE is
the standard justification, but drug-target MR (Burgess's specialty) is
implicitly a phase-2 emulation, and biomarker-outcome scans are
proof-of-concept phase-1 emulations. Setting the emulation-phase up front
disciplines the "what evidence does this trial actually provide" question
that reviewers keep hammering pharmacoepi TTEs on. Directly relevant to
your drug-target-MR-triangulated-with-observational-TTE rising sub-thread.

**Do next:** cite in the discussion section of any future TTE manuscript
to explicitly state which phase you're emulating. Combine with Hernán's
own recent guidance on causal-question specification.

### 5. Venkatesh & Ritchie 2026 — AI-based multimodal integration of genomics and electronic health records (*Nature Reviews Genetics*)

- **Venue:** *Nature Reviews Genetics* (2026), doi:10.1038/s41576-026-00992-w
- **Authors:** R Venkatesh, M D Ritchie
- **Feeds:** "Foundation models + electronic health records" keyword feed (08-13).
- **INTERESTS.md threads:** EHR foundation models (top), knowledge representation in EHRs, biobanks with EHR linkage (MVP/AoU/UKB genomics-EHR integration), genetic epi.

**Snippet.**
> We focus on methods that enable integration across genomic and clinical
> data modalities at scale, prioritizing recent developments in ML and
> deep learning architectures and foundation-model-based approaches, while
> situating these …

**Why it matters here.** Ritchie is the PMBB / MVP-lineage genomics-plus-EHR
figure, so this is the *canonical* current-state-of-the-field review. It
is the single-most-important cite-in-intro reference for any future
methods paper in your EHR-FM thread. Also likely to update the field's
shared vocabulary — worth reading in full and updating your
`project-glossary` scaffolding to align.

**Do next:** read the full review. Note which architectures they call
canonical, which datasets they anchor benchmarks on, and which gaps they
name; those are the durable citations and the durable open problems.

### 6. Shah et al. 2026 — Lessons from deploying the ChatEHR system at Stanford Medicine (*Nature Medicine*)

- **Venue:** *Nature Medicine* (2026), doi:10.1038/s41591-026-04574-5
- **Authors:** N H Shah, N Sehgal, E A Ashley, M A Pfeffer
- **Feeds:** Nigam Shah new-articles feed (08-14).
- **INTERESTS.md threads:** EHR foundation models (deployment / audit sub-thread), knowledge representation in EHRs (LLM-derived note representations), ML for precision health.

**Snippet.**
> In piloting and deploying a large language model within a large medical
> center, we learned that benchmark-based evaluations are insufficient for
> monitoring and evaluating interactions driven by clinicians, and that
> this requires new methods for …

**Why it matters here.** This is a rare deployment-lessons piece from an
FM-thread-adjacent group at Stanford. The core message — *benchmark-based
evals are insufficient for monitoring clinician-driven LLM interactions* —
lands directly on the FM-audit sub-thread and connects to the pretraining-
contamination-audit thread (scContam, MIA-scFM) you're already tracking.
If you're planning any real-world LLM deployment at Vanderbilt / VUMC, this
is the reference paper for how NOT to overrely on MedQA-style benchmarks.

**Do next:** read alongside the Chatrath et al. arXiv 2608.07796
CliniCARE-Bench paper that also surfaced in the Nigam Shah feed on 08-14 —
CliniCARE-Bench is the *complement* (a longitudinal-EHR reasoning bench),
and reading them together clarifies where benchmark evaluation is
sufficient vs. where interaction-monitoring is required.

---

## METHODS-WATCH (worth cribbing techniques from)

| Paper | Feed / source | One-line take |
| --- | --- | --- |
| **Bandreddi et al. — Tobit vs two-part hurdle for semi-continuous longitudinal data with clonal hematopoiesis application** (arXiv 2608.09725) | `arxiv-digest` 08-11 + clonal-hematopoiesis keyword feed 08-13 | Derives formal equivalence conditions between Tobit and hurdle models for zero-inflated longitudinal outcomes; applied to PLCO CHIP clonal fractions. Fills a methods gap in the CHIP-VEXAS-LOY thread. |
| **Chen et al. — Clustering Informed IPW for Causal Effect Estimation** (arXiv 2608.09839) | `arxiv-digest` 08-11 | Compares standard IPW, cluster-augmented IPW, and global PS with cluster-membership as covariate. Application in n=966 carboplatin-treated breast cancer patients. Cribbing-worthy for any AoU / MVP analysis with strong site or ancestry cluster structure. |
| **Porotsky — Inverse Confounding Analysis (ICA)** (arXiv 2608.11991) | `arxiv-digest` 08-13 | Exact analytical solution for the range of stratification-based RRs compatible with observed frequencies — extends the E-value approach with exact (not worst-case) bounds. Alternative to VanderWeele E-values when frequencies of exposure/confounder/outcome are known. |
| **Kevopoulos et al. — CAN-FLOW: conditional normalizing flows for cardiac anatomy on UKB** (arXiv 2608.09460) | `arxiv-digest` 08-11 | Two-step conditional normalizing-flow generator trained on n=2,208 UKB healthy subjects; beats cVAE across cardiac shape metrics. Template for imaging-conditional generative modeling on biobank data. |
| **Ao et al. — Exome-wide association study of chronic pain in 327,642 UKB participants** (*Genome Medicine* 2026) | Jian Yang related-research feed (08-15) | Largest ExWAS of chronic pain to date; joint common + rare coding-variant framing. Design directly portable to your CF and hereditary-cancer ExWAS work. |
| **Lin et al. — Cross-biobank genetics of GGT in East Asians, cardiometabolic comorbidities, T2D precision risk stratification** (*Cell & Bioscience* 2026) | Lisa Bastarache related-research feed (08-15) | Cross-biobank East-Asian analysis of GGT as biomarker; useful precedent for cross-biobank cardiometabolic PGS work. |
| **Hansen et al. — Anthropometric and cardio-metabolic trait variation and genetic associations in sub-Saharan Africa** (*AJHG* 2026) | Karczewski + Denny citation feeds (08-15) | Sub-Saharan African GWAS on cardiometabolic phenotypes; important for cross-ancestry PGS portability arguments. |
| **Chatrath et al. — CliniCARE-Bench: Clinical Calibrated Audit of Medical Reasoning in EHR** (arXiv 2608.07796) | Nigam Shah feed (08-14) | Longitudinal-EHR reasoning benchmark for LLM agents; asks whether the agent conducts a *defensible investigation* rather than answering from short passages. Direct complement to the Shah *Nat Med* deployment paper above. |
| **Chang et al. — Automated epilepsy and seizure-type phenotyping with transformer-based language models** (*npj Digital Medicine* 2026) | Peter Szolovits + Pascal Brandt related feeds (08-15) | Transformer-LM phenotyping from EHR notes for a complex neuro phenotype. Portable to CF pulmonary-exacerbation and IBD-flare NLP phenotyping. |
| **Team et al. — Scaling Inherently Interpretable Language Models** (arXiv, Goodfire) | Marinka Zitnik / Peter Szolovits / Zhiyong Lu related feeds (multi-hit, 08-14) | Framed as "interpretability need not be a tax on capability." Worth tracking as the interpretability lever for any future clinical-LLM audit. |
| **Foulkes et al. — IPW for auxiliary-variable-dependent measurement error** (arXiv 2608.04918; previously flagged 08-08) | Follow-up citation activity this week | Still on the radar as the EHR-measurement-error IPW methods reference. |
| **Lavery et al. — Pan-Cancer Target Trial Emulation of Exercise and Distant Disease-Free Recurrence** (CEBP 2026) | Hernán citation feed (08-15) | Solid worked-example TTE for a lifestyle exposure across cancer types; contrast with the pharmacoepi TTEs on your reading list. |
| **Launders et al. — Dihydropyridine CCB effects on SMI mental-health outcomes in English EHRs** (*J Psychopharmacol* 2026) | Hernán citation feed (08-15) | TTE distinguishing BBB-penetrant vs. non-penetrant dihydropyridines in CPRD; a nice example of within-drug-class contrast as a repurposing / mechanism probe. |
| **Le Borgne et al. — Impact of concomitant PPIs in advanced/metastatic NSCLC: TTE protocol** (ESMO RWD & Digital Oncology 2026) | Hernán citation feed (08-15) | Protocol paper — worth watching for the analysis. PPI × TKI / ICI is a live pharmacoepi question. |
| **Parasuraman et al. — Genetic prediction of colorectal cancer risk in six major ancestries** (medRxiv 2026) | Chenjie Zeng related-research feed (08-15) | Six-ancestry CRC PRS with an eye to streamlining screening guidelines; adjacent to your GI-cancer PRS interests and cross-ancestry portability. |
| **Wu et al. — Integrative exome sequencing and multi-omics analysis of rare variants in metabolic syndrome** (Functional & Integrative Genomics 2026) | Stephen B Montgomery related feed (08-15) | Rare-variant contribution to a cardiometabolic composite phenotype — a design pattern for composite-risk rare + common analyses. |
| **Linz et al. — Data-driven algorithms to identify Lyme disease cases in EHRs** (*PLOS ONE* 2026) | George Hripcsak related feed (08-15) | Rules + ML EHR phenotyping for an infectious phenotype; parallels PheKB-style phenotype work. |
| **Peng et al. medRxiv — early-onset breast cancer GWAS + PheWAS** (previously flagged 08-08 report) | Lisa Bastarache author feed follow-through | Still worth reading in full — overlaps your early-onset BC lineage. |

---

## SKIP (surfaced, not on-thread)

- **VOICE — vision-omics FM for single-cell expression from H&E** (arXiv 2608.08366; `arxiv-digest` 08-11): outside the clinical-EHR-genomics scope.
- **Charpentier — motor insurance multi-scale causal DAG** (arXiv 2608.09441; `arxiv-digest` 08-11): incidental "motor" keyword hit; non-biomedical.
- **Multiple nursing / cybersecurity / hospitality-industry hits from the `foundation models × EHR` keyword feed 08-13**: incidental keyword overlaps only.
- **`knowledge graph` keyword feed 08-15** (construction-industry LLM + KG paper): incidental.
- **`drug repurposing` keyword feed 08-15** (KRAS-mutant NSCLC in silico screen): pure computational-chemistry pipeline without the EHR / clinical-evidence loop your INTERESTS.md prioritizes.
- **`autoimmune diseases` keyword feed 08-15** (selenium narrative review): nutrition narrative review, off-thread.
- **`variant interpretation` keyword feed 08-15** (small pediatric WES cohort study): off-methods for the ACMG / ClinGen thread.

---

## Housekeeping deltas

- **08-14 → 08-16 arxiv-digest are quiet:** 2 → 1 → 0 previously-surfaced suppressed. This is expected — the pipeline correctly deduplicates against `seen.json`. No pipeline anomaly.
- **Two-feed convergence on Kachhadia et al.** (Zeng self + Denny related) is unusually strong signal. Consider adding a light rule: if a paper appears in ≥2 author feeds *and* one of them is a self-alert, promote it to the top of the HIGH stack automatically.
- **INTERESTS.md last-updated stamp is 2026-07-29.** After reading the Venkatesh & Ritchie NRG review (item 5), consider a light update to the *EHR foundation models* thread to reference it as the new field-defining review — the current thread anchor still leans on 2025-era references.
- **`Foundation models + electronic health records` keyword feed noise floor is high.** Half of the 08-13 batch was nursing / cybersecurity / clinical-education papers. If the recall isn't paying off, consider tightening to `"foundation model" AND ("electronic health records" OR "clinical notes")`.

