# Research digest report — 2026-08-22

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-22 12:35Z** (~5 days since the
last research-digest report, covering six arxiv-digest cron runs and
three Google Scholar alert batches on 08-20, 08-21, and 08-22).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-17.md` → `2026-08-22.md`) | 08-17 → 08-22 daily crons | Six daily runs. 08-17, 08-21, 08-22: 0 relevant papers (dry). 08-18: 4 papers (Bayesian epidemic-alignment g-computation; zero-inflated causal mediation w/ non-compliance; n-of-1 digital-health primer; regression-not-to-the-mean w/ constant-treatment-effect misspecification in longitudinal designs). 08-19: no digest file (arxiv weekend / holiday gap — nothing to review). 08-20: 3 papers (Monroe molecular FM; Peruvian mayor-experience DML; urban-rail-transit DML). Two of the three 08-20 items are stat.AP DML-in-non-biomedical-domains and score-1; kept for the reviewer stack but not on active threads. |
| No `arxiv-digest` email hits from GitHub | — | Same as prior window: search of `from:notifications@github.com` / `from:action@github.com` × `arxiv-digest`, `chenjiezeng`, and `arxiv` returned zero threads in the last 30 days. The `arxiv-digest` pipeline commits its output to the local repo (this branch) rather than emailing notifications. Digest files under `digests/` are the primary artifact; the on-disk repo *is* the arxiv-digest feed. |
| Google Scholar alerts (keyword feeds, 08-22 batch, 06:01Z) | 08-22 06:01Z | 10 keyword feeds fired: `All of Us research program`, `Foundation models + electronic health records`, `rare diseases`, `phenome wide association studies`, `UK Biobank`, `knowledge graph`, `autoimmune diseases`, `mendelian diseases`, `electronic health records`, `variant interpretation`/`variant classification`, `drug repurposing`, `APOL1`, plus one citation trail (`Personalized lab test models to quantify disease...`). |
| Google Scholar alerts (author + citation feeds, 08-22 batch, 00:53Z) | 08-22 00:53Z | 20+ author / citation feeds fired: Chenjie Zeng (×2: self-cite + related), Kai Wang (×2: new-related + citations-to), Lisa Bastarache (×2: new-related + citations-to), Joshua C Denny (×2: new-related + citations-to), Konrad Karczewski (×2), Peter Szolovits (×2), Zhiyong Lu, Tiffany J Callahan, Jian Yang (×2), Stephen B Montgomery (citations-to), Marinka Zitnik (×2), Vivek Natarajan (citations-to), Daniel Kastner (citations-to), Jonathan K Pritchard (citations-to), Yuan Luo (citations-to), Pascal Brandt (new-related), George Hripcsak (×2: new-related + citations-to), Patrick Ryan (new-related), James Zou (new articles), Jure Leskovec (new articles). |
| Google Scholar alerts (08-20/08-21 keyword feeds, 21:23Z + 01:39Z) | 08-20 21:23Z – 08-21 01:39Z | Second author-feed sweep firing Szolovits, Zitnik + one keyword sweep (`All of Us research program`, `electronic health records`, `knowledge graph`, `rare diseases`, `Foundation models + electronic health records`) that surfaced the Foresight-England paper (dual-fed with Hripcsak + Ryan new-related). |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Thirteen HIGH items surfaced this window, clustering into five knots:

**EHR foundation-model cluster (2 items — anchor of the window).**
Ellershaw et al. arXiv 2608.16273 — **Foresight-England**, a
243-million-parameter generative FM trained *de novo* on longitudinal
EHRs from **54.9 million NHS England patients** entirely within the
NHS SDE, with evaluation across the COVID-19 pandemic period.
Triple-fed (`Foundation models + electronic health records` keyword,
George Hripcsak new-related, Patrick Ryan new-related) — the signal
strength alone flags this as the field-defining paper of the week for
your **EHR foundation models** thread (`INTERESTS.md` line ~114).
Reference substrate for the *digital-twins-from-EHR* rising sub-thread.
Burkhart, Solo, Lee, Charles, Liao et al. arXiv 2608.02939 —
**Federated generative event models (GEMs)** across 122,251 tokenized
EHR trajectories; directly addresses the *cross-site transfer
degradation* problem that motivates the **Fidelity, portability, and
audit of representations** sub-topic (`INTERESTS.md` line ~168). Read
the two back-to-back: Foresight-England is the national-scale
*monolith*, Burkhart et al. is the *federated alternative*, and the
CLMBR / MOTOR / MEDS lineage will start branching along that axis.

**Rare-variant + biobank pleiotropy cluster (3 items).** Suger,
Harrison, Zhang, Wu, Darst et al. HGG Advances 2026 — **pleiotropic
landscape of rare variant associations with multiple cancers across
large biobanks**, using AoU Controlled Tier Dataset 8. This is the
biobank-scale pleiotropy paper your **Genetic epidemiology** +
**Biobanks with EHR linkage** threads (INTERESTS.md lines ~72 and ~28)
have been waiting for; also feeds the *composite risk / PGS-tails*
framing for cancer. Zhou, Yolou, Xie, Zhao STAR Protocols 2026 —
**protocol for local-ancestry + cross-ancestry PGS in AoU admixed
individuals**. Direct methods drop for the *cross / trans-ancestry
portability* line under Genetic epi, and the *ancestry-aware risk
scores* piece of PheWAS / phecode infrastructure. Bsc, Rawaa Eltayib,
Olsen et al. AJT 2026 — **polygenic prediction of actinic keratosis
identifying transplant recipients at risk of extreme lesion burden**,
using QSkin / STAR / UKB / AoU as a four-cohort stack. This is a
concrete "PGS-tails-under-a-modifiable-immunosuppression-exposure"
design that pairs with the PGS × environment sub-thread (Nagpal &
Gibson lineage) and the "PGS tied to a clinical decision" bar in the
**ML for precision health** thread.

**Variant-interpretation + Mendelian↔predisposition cluster (2 items).**
Yang, Zou, Pu, Li, Hu, Wang, Liu et al. bioRxiv 2026 —
**context-dependent variant interpretation from Mendelian disease to
genetic predisposition: a proof-of-concept using LPL** (Karczewski
new-related feed). LPL is the perfect testbed: severe biallelic LOF →
familial chylomicronemia; heterozygous / hypomorphic → hypertriglyceridemia
predisposition; and pathogenicity for *type-2-diabetes-risk-modifier*
alleles differs by the biological context (dietary, metabolic,
polygenic background). Direct hit on the **ACMG / ClinGen variant
interpretation** thread and complements the Mitev framework paper from
the 08-17 report. Friedman & Pollak *Kidney International* 2026 —
review of **new mechanistic ideas in APOL1 kidney disease**. Anchor
review for the APOL1 disease sub-thread (INTERESTS.md line ~102);
signals that AMKD mechanism is moving beyond the "risk-genotype ⇒
kidney injury" narrative toward multi-hit and modifier-aware
frameworks — the exact substrate the PGS × environment work needs
to layer onto for APOL1.

**All of Us clinical-research cluster (2 items — Zeng-thread-adjacent).**
Nigam, Onongaya, Meshram, Frebault et al. *Diseases of the Colon &
Rectum* 2026 — **traditional risk factors are NOT associated with the
rise of early-onset colorectal cancer in All of Us**. Sits directly at
the intersection of Zeng's CRC epidemiology lineage and the **Biobanks
with EHR linkage** thread. Null-result paper on the "what's driving
EOCRC" question is signal, not noise; complements the ancestry /
microbiome / exposome hypotheses being explored elsewhere. Yee, Oakes,
Santacroce, Feldman et al. *Seminars in Arthritis and Rheumatism* 2026
— **electronic cigarette use and risk of incident RA and SLE in AoU**.
Standard EHR + questionnaire pharmacoepi in AoU; useful reference for
methods choices (case ascertainment via phecode? chart? self-report?)
whenever you write up an AoU autoimmune-outcome pharmacoepi paper.

**Rare-disease LLM / HPO-diagnosis cluster (3 items).** Schächter,
Pechmann, Kirschner, Hasenauer et al. arXiv 2608.16507 — **LLMs as
synthetic clinical experts to inform longitudinal rare-disease
modeling**, framed around SMA and boundary-crossing between disease
types. Highly relevant to the *pre-symptomatic phenoconversion
prediction from longitudinal biomarker trajectories* rising sub-thread
(INTERESTS.md line ~201; Ran / Benatar ALS template). Nguyen & Shyr
arXiv 2608.16831 — **Policy Iteration with Human Feedback (PIHF)**
lifts Recall@1 from 26.5% → 59.3% across 1,243 public rare-disease
benchmark cases (frontier proprietary executor), transferable across
proprietary and open-weight LLMs. Direct methods drop for the
**auditable HPO-driven diagnostic benchmarks with separable metrics
for ranking vs. evidence coverage** sub-thread (INTERESTS.md line ~197;
GraphRareBench lineage). Jiang, Fu, Kim, Li, Peng, Teng, Mi, Wu arXiv
2608.14683 — **selective prediction on the rare-disease tail** (should
the diagnostic system endorse its top-1 prediction or defer?) with a
canonical result that eight small open-weight LLMs achieve at most 4.6%
Recall@1 on the tail. Complements PIHF as a *calibration / abstention*
axis; together the two form a proper "confidence-and-coverage" story
for rare-disease LLM diagnostics.

**Imaging-driven PheWAS + Fitbit-derived phenotypes (2 items).** Jang,
Lytchakov, Duda, Borthakur et al. Research Square 2026 —
**AI-driven CT segmentation for osteoporosis detection, with PheWAS
linkage across multiple large health-system biobanks** (fired the
`phenome wide association studies` keyword feed). Direct hit on the
PheWAS + imaging-derived-phenotype intersection, and on the *phenotype
validation against EHR-derived outcomes* piece of the **Biobanks with
EHR linkage** thread. Note the L1-vertebra measurement style — this
becomes a *quantitative imaging endophenotype* PheWAS, which fits the
functional-time / imaging-FM thread as well. Corponi, Reami, Ossola,
Fanelli, Jauhar et al. medRxiv 2026 — **Fitbit-derived rest-activity
phenotypes ("damped physical activity" and "unstable sleep") in
inter-episode mood disorders** (Denny feed). The persistence-during-
euthymia framing is precisely what a *pre-symptomatic phenoconversion*
paper looks like for psychiatry; also the *AoU / UKB wearable-signals
as PheWAS-style phenotypes* substrate.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-17 → 2026-08-22)

#### METHODS-WATCH — Moriña D. *Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions.* arXiv 2608.16537v1 (stat.ME, 2026-08-17). Score 1.

Interrupted-time-series and pre–post designs align epidemics by
calendar week, which conflates a shift in epidemic *phase* with a
change in disease *burden* whenever epidemic onset / speed / peak
timing varies. Introduces a Bayesian causal count model in which
season-specific affine transformations map calendar time to a latent
**epidemic clock**, and intervention effects are estimated on that
clock (alignment is a model component, not preprocessing — uncertainty
propagates into every causal contrast). Negative-binomial observation,
hierarchical area / season effects, shrunk Fourier epidemic curve,
continuous programme-intensity exposure; **posterior g-computation**
yields prevented cases, prevented fractions, peak attenuation, and
epidemic displacement under controlled and dynamic contrasts.
Illustrated on Catalan primary-care RSV surveillance and RSV
immunisation data. Methods-watch for the **causal inference &
pharmacoepi** thread whenever the exposure timing is itself a
random-timing variable (immunisation campaigns, HRT-formulation
launches, CFTR-modulator approval waves, GLP-1 RA supply shortages).
Bookmark for pandemic/seasonal-effect-modeling comparisons; complements
the egg-computation Gantt-DAG approach from the 08-17 report where the
LLM handles the trajectory-mapping step.

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. *Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.* arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1.

Motivated by a longitudinal promotional-email campaign — irrelevant
substrate — but the methods engine is directly transferable: a
**Bayesian causal mediation framework using enriched Dirichlet process
mixture models** with a scalable **g-computation** algorithm, handling
non-compliance, multiple longitudinal mediators, and zero-inflated
mediators / outcomes. The zero-inflated-longitudinal component is
precisely the shape of **CHIP / VEXAS / LOY VAF trajectories** and of
**medication-persistence-with-below-detection-dose data**; the
non-compliance handling is directly analogous to prescription-fill-vs-
initiation mismatch in pharmacoepi. Should sit next to the
Bandreddi Tobit-vs-hurdle paper from the 08-17 report as a
complementary methods bundle for zero-inflated longitudinal outcomes
in EHR / biobank pharmacoepi.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. *Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.* arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1.

Shows that in longitudinal settings with staggered treatment and
heterogeneous treatment effects, a **constant-treatment-effect model
can return a weighted average with negative weights** of the true
duration-heterogeneous effects — producing an estimated constant
effect that is smaller in magnitude or of *opposite sign* to almost
every one of the underlying heterogeneous effects. Demonstrated on
drug-induced-homicide prosecutions × unintentional overdose deaths;
critically, the paper shows the negative-weight issue arises in
**logistic** regression too, not just linear models (constant RR =
1.064 vs. duration-heterogeneous RRs 0.539–1.008; constant linear
RR 0.977 vs. duration-heterogeneous RRs 0.507–0.979). This is the
paper to cite whenever a **CFTR-modulator persistence**, **GLP-1 RA
discontinuation**, or **HRT initiation** analysis reports a "small
overall effect" from a constant-treatment-effect Cox / logistic model
in a longitudinal EHR cohort — it may be a negative-weighting artifact
masking real duration-heterogeneous effects. Portable to essentially
every longitudinal pharmacoepi analysis on the watchlist.

#### SKIP — Daza EJ. *A Primer on Digital Health N-of-1 Studies and Single-Case Designs.* arXiv 2608.15526v1 (stat.AP, 2026-08-16). Score 1.

Digital-health n-of-1 / single-case-design primer. Adjacent to the
**Machine learning for precision health** thread's individualized-
prediction line, but at review / primer altitude rather than the
tied-to-a-clinical-decision bar you want to prioritize. Bookmark if
writing a *digital-twins-from-EHR + individualized-trajectory
prediction* essay; otherwise LOW-priority.

#### SKIP — Banaszewski B, Fitzgibbon AW. *Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference.* arXiv 2608.18982v1 (cs.LG, 2026-08-19). Score 1.

Molecular foundation model pretrained on 81M molecules from PM6
quantum-chemistry data with a TabPFN-style in-context downstream
predictor; beats prior MFMs on Polaris + activity-cliff benchmarks.
Chemistry-first FM — off your EHR / clinical-agent threads. Only
tangentially relevant if the **drug repurposing** line pivots into
molecular-fingerprint-based candidate generation, which it hasn't.

#### SKIP — Machacuay C, Lincovil J, Rojas H. *Mayoral Experience or Municipal Capacity? Negative-Outcome Evidence on Municipal Budget Execution in Peru.* arXiv 2608.18354v1 (stat.AP, 2026-08-18). Score 1.

Peruvian municipal-governance panel-DML application with a nice
**negative-outcome control** design (pre-mayor GDP as the negative
control for within-municipality vs. cross-sectional identification).
Off-topic substrate, but the negative-outcome-control pattern is a
clean template if you're evaluating a pharmacoepi TTE where a
pre-exposure clinical marker can serve as a negative-outcome anchor
against unmeasured confounding — bookmark the DAG pattern, skip the
paper.

#### SKIP — Yao Y, Zhang N, Graham DJ. *Quantifying the Causal Operational Determinants of Service Reliability in Urban Rail Transit: Evidence from Panel Double/Debiased Machine Learning.* arXiv 2608.17901v1 (stat.AP, 2026-08-18). Score 1.

Panel DML on 46 international metro operators. Off-topic. The
panel-fixed-effects × DML pattern is standard; the paper is a clean
example if you're teaching DML on longitudinal non-medical data, but
adds nothing to the biomedical thread.

### Scholar alerts — 08-22 keyword + author / citation batches

#### HIGH — Ellershaw S, Tomlinson C, Kraljevic Z, Denaxas S, et al. *Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic.* arXiv 2608.16273 2026 (`Foundation models + electronic health records` keyword feed; George Hripcsak new-related; Patrick Ryan new-related; triple-fed).

**243-million-parameter generative FM trained *de novo* on longitudinal
EHRs from 54.9 million NHS England patients, entirely within the NHS
England Secure Data Environment.** The triple-fed signature (keyword +
Hripcsak + Ryan) marks this as the field-defining paper of the window
for your **EHR foundation models** thread (INTERESTS.md line ~114) and
the *digital-twins-from-EHR* rising sub-thread. Reference candidate
that the CLMBR / MOTOR / EHRSHOT / MEDS / FEMR lineage will
increasingly be measured against; also the substrate model for testing
whether pandemic-era distributional shift breaks EHR-FM calibration.
Read full-text for: (1) the tokenization scheme (event vs. sub-event
vocabulary — how do they handle SNOMED / dm+d / HES codes together?),
(2) whether the SDE-native training pattern is architecturally
different from public-cloud EHR-FM training, (3) their pandemic-window
evaluation strategy (does calibration collapse for the March–June 2020
window? do they report time-stratified metrics?), (4) whether they
release model weights / a benchmark harness for the NHS SDE
(governance-permitting) — that determines whether this becomes a
*shared* reference model or a *published-but-not-usable* one. Should
be paired with the Burkhart et al. federated-GEMs paper (below) as the
two anchor readings for the current EHR-FM debate: national monolith
vs. federated GEMs.

#### HIGH — Burkhart MC, Solo L, Lee I, Charles SK, Liao Z, et al. *Federated generative event models for tokenized electronic health records.* arXiv 2608.02939 2026 (Pascal Brandt new-related feed).

**Federated training of tokenized generative event models (GEMs)
across 122,251 EHR trajectories.** Snippet cites the standard concern
— "EHR foundation models are limited by institutionally siloed data
and substantial performance degradation under cross-site transfer" —
and evaluates federated training as the mitigation. Direct hit on the
**Fidelity, portability, and audit of representations** sub-topic
(INTERESTS.md line ~168) and the **Federated / privacy-preserving EHR
causal analytics** rising sub-thread under causal inference (line ~57).
The GEM tokenization angle also intersects with MEDS / EHRSHOT / FEMR
lineage — check whether their event schema is MEDS-compatible.
Read full-text for: (1) how they measure "site transfer degradation"
before / after (which held-out sites? which downstream tasks?),
(2) whether GEMs preserve *causal-structure-informative* patterns or
only marginal event distributions, (3) whether federated training
improves calibration in addition to mean performance, (4) governance /
privacy scaffolding (differential privacy budget? secure aggregation?).
Pair-read with Foresight-England: the two together frame the EHR-FM
"scale in one place vs. federate across many places" tradeoff you'll
want to write into any future methods commentary.

#### HIGH — Yang Q, Zou WB, Pu N, Li Y, Hu Y, Wang YC, Liu X, et al. *Context-dependent variant interpretation from Mendelian disease to genetic predisposition: a proof-of-concept using LPL.* bioRxiv 2026 (Konrad Karczewski new-related feed).

**Reframing variant interpretation for the regime where population
sequencing meets precision medicine** — where the same variant carries
different clinical consequences under different biological contexts
(genetic background, dietary exposure, metabolic state). LPL is the
canonical testbed: biallelic LOF → familial chylomicronemia (a rare
Mendelian disease); heterozygous / hypomorphic → hypertriglyceridemia
predisposition (a common polygenic-tail phenotype); some coding
variants act as *metabolic-modifier* alleles. Direct hit on the
**ACMG / ClinGen variant interpretation** thread (INTERESTS.md line
~66) and complements the Mitev variant-classification-platform
framework paper from the 08-17 report. Also feeds the **PGS × exposure
/ environment interactions** rising sub-thread — LPL is a natural
substrate for "polygenic-triglyceride-PRS × rare-hypomorphic-LPL ×
dietary-fat-exposure" composite-risk models. Read for: (1) their
proposed classification framework (is it an extension of ACMG or a
parallel schema?), (2) whether they operationalize "biological
context" as a set of *quantitative* modifiers (PGS, expression, diet)
or as clinical categories, (3) whether the framework is generalizable
beyond LPL to CFTR (modifier-aware CF), APOL1 (with hypertension/HIV
modifier), and cancer-risk genes with modifier-dependent penetrance.

#### HIGH — Friedman DJ, Pollak MR. *New ideas about mechanism in APOL1 kidney disease.* Kidney International 2026 (`APOL1` keyword feed).

**Anchor mechanistic review for APOL1-mediated kidney disease (AMKD).**
Signals that field is moving beyond the *risk-genotype ⇒ podocyte
injury* narrative toward multi-hit and modifier-aware frameworks.
Direct hit on the APOL1 disease sub-thread (INTERESTS.md line ~102).
Read full-text for: (1) which non-genetic modifiers are foregrounded
(HIV nephropathy, sickle cell, COVID-19, interferon-mediated
inflammation), (2) whether the paper discusses *penetrance under
population-screening conditions* — which directly serves the PheWAS
sub-thread's penetrance-estimation piece (INTERESTS.md line ~25),
(3) any commentary on **APOL1-targeted therapeutics** (inaxaplin /
VX-147 lineage) as they intersect with pharmacoepi, (4) whether the
review cites the AoU / UKB APOL1-carrier phenotyping literature.
Should be the cited framing reference next time the APOL1 sub-thread
generates a computable-phenotype or penetrance manuscript.

#### HIGH — Nigam A, Onongaya C, Meshram P, Frebault J, et al. *Traditional Risk Factors Are Not Associated with the Rise of Early-Onset Colorectal Cancer: An All of Us Study.* Diseases of the Colon & Rectum 2026 (`All of Us research program` keyword feed).

**Null result on the "which traditional risk factors explain rising
EOCRC?" question in AoU.** Sits at the intersection of Zeng's CRC
epidemiology lineage and the **Biobanks with EHR linkage** thread.
Null-result papers on the driver-of-EOCRC question are informative
signal, not noise — they push the hypothesis space toward
non-traditional exposures (microbiome, exposome, adolescent-onset
obesity, ultra-processed diet) and toward *interaction* patterns that
scalar risk-factor regressions miss. Read for: (1) which risk-factors
they tested and how they were ascertained (self-report questionnaire?
EHR-derived phecodes? survey time-since-exposure?), (2) sample size
of the EOCRC-vs-average-onset comparison and its power, (3) whether
they did any ancestry-stratified or SES-stratified analysis (EOCRC
disparities pattern is real), (4) analytical model — Cox with adjusted
hazards, or something more flexible? This is a good candidate for
the *phenotype-validation-anchor* audit under the **EHR phenotyping /
OMOP** thread if the EOCRC case definition is chart-review-validated.

#### HIGH — Suger AH, Harrison TA, Zhang J, Wu MC, Darst BF, et al. *The pleiotropic landscape of rare variant associations with multiple cancers in large biobanks.* Human Genetics and Genomics Advances 2026 (`All of Us research program` keyword feed).

**Rare-variant × pleiotropy × pan-cancer × biobank scale** — the
paper anchors two INTERESTS.md threads at once (Genetic epidemiology
line ~72; Biobanks with EHR linkage line ~28) using AoU Controlled
Tier Dataset 8. Rare-variant burden across multiple cancers is exactly
the composite-risk substrate you'd want stacked with a PGS-tails
framing. Read full-text for: (1) which cancers were tested and which
rare-variant sets (LOFTEE-filtered pLoFs? mis-Z-scored missense?
ClinVar P/LP?), (2) whether pleiotropy is defined as *shared genes*
across cancers or *shared variants* — different biological
implications, (3) whether they externally validate in UKB / MVP /
FinnGen (essential for the biobank thread), (4) whether the paper
addresses **penetrance estimation under population-screening
conditions** for monogenic-cancer genes (BRCA1/2, MSH2/MLH1, TP53) —
this is the direct link to your PheWAS penetrance sub-thread. Track
whether the Darst et al. authorship signals continuity with the
prostate-cancer-genetics lineage you follow.

#### HIGH — Zhou G, Yolou I, Xie Y, Zhao H. *Protocol for leveraging local ancestry and cross-ancestry genetic architecture to improve polygenic prediction in admixed populations.* STAR Protocols 2026 (`All of Us research program` keyword feed).

**Explicit protocol drop for local-ancestry-aware PGS construction on
AoU admixed individuals.** Direct methods paper for the *cross /
trans-ancestry portability* line under **Genetic epi** (INTERESTS.md
line ~74) and the *ancestry-aware risk scores* piece of the PheWAS
infrastructure thread. Because STAR Protocols publishes step-by-step
computational recipes, this is the paper to *actually run* if you're
constructing PGS in AoU admixed African-ancestry / Hispanic-ancestry
cohorts. Read for: (1) which local-ancestry inference tool they use
(RFMix, Gnomix, FLARE?), (2) how they handle the cross-ancestry
architecture stack (which reference GWAS panels, GBMI vs. PGP vs.
GWAS Catalog?), (3) whether the pipeline is compatible with the
AoU Researcher Workbench's compute constraints (single-VM vs. Dataproc /
Hail) — this determines usability, (4) whether they explicitly
benchmark against PRS-CSx, PROSPER, or ancestry-blind PRS-CS as
baselines.

#### HIGH — Bsc AP, Rawaa Eltayib MD, Olsen CM, et al. *Polygenic prediction of actinic keratosis identifies transplant recipients at risk of extreme lesion burden.* American Journal of Transplantation 2026 (`All of Us research program` keyword feed).

**PGS applied to the tail of a modifiable-exposure-driven phenotype
(actinic keratosis under chronic immunosuppression), across four
cohorts (QSkin, STAR SOTRs, UKB, AoU).** Snippet frames PGS
identification of *extreme-burden* transplant recipients — this is a
concrete instantiation of the **PGS-tails-under-a-modifiable-
environment** framing (Souaiaia + Nagpal & Gibson lineage) and of the
"PGS tied to a clinical decision" bar under **ML for precision health**
(who to screen more aggressively for skin-cancer surveillance).
Read for: (1) whether they use ancestry-matched PGS or a single
Euro-derived PGS across cohorts (portability caveat), (2) whether
"extreme lesion burden" is a phecode-defined outcome or a chart-review
count, (3) whether they benchmark PGS gain over standard clinical
scoring (Fitzpatrick + years-since-transplant + immunosuppression
regimen), (4) actionability — do they specify a screening interval
change? Cite when writing the "PGS-in-a-decision" position piece.

#### HIGH — Schächter C, Pechmann A, Kirschner J, Hasenauer J, et al. *Large language models as synthetic clinical experts to inform longitudinal rare-disease modeling.* arXiv 2608.16507 2026 (`rare diseases` keyword feed).

**LLMs as synthetic clinical experts to fill the sparse-data gap in
longitudinal rare-disease modeling.** Snippet describes "disease-type
boundary crossing" (a patient trajectory switches from one disease
subtype to another) and "reduced disagreement" — this reads as a
*probabilistic trajectory classification* problem where LLM priors
substitute for missing expert labeling at scale. Direct fit for the
**Pre-symptomatic phenoconversion prediction from longitudinal
biomarker trajectories** rising sub-thread (INTERESTS.md line ~201;
Ran / Benatar ALS template). Read for: (1) which rare disease is the
substrate (SMA is likely given Pechmann / Kirschner authorship —
Freiburg SMA registry), (2) how they validate "clinical faithfulness"
of LLM-generated synthetic expert judgments (chart review? expert
inter-rater?), (3) whether the LLM is used at label-generation time
or as an inference-time posterior, (4) portability to
BRCA-carrier-to-cancer, APOL1-carrier-to-CKD, HD-carrier-to-symptom-onset
trajectory modeling.

#### HIGH — Nguyen MH, Shyr C. *Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning.* arXiv 2608.16831 2026 (`rare diseases` keyword feed).

**Policy Iteration with Human Feedback (PIHF) lifts Recall@1 from
26.5% to 59.3% across 1,243 public rare-disease benchmark cases**,
frontier proprietary executor, transferable across proprietary and
open-weight executors. Direct methods drop for the **auditable
HPO-driven diagnostic benchmarks with separable metrics for ranking
vs. evidence coverage** rising sub-thread (INTERESTS.md line ~197;
GraphRareBench lineage). The magnitude of the improvement (2.24×
Recall@1) is unusual for HPO-diagnosis benchmarks — this should be
audited quickly: (1) is the 1,243-case benchmark public and
non-overlapping with LLM training data, (2) does the improvement hold
under GraphRareBench's ranking-of-confounders decomposition (or does
the LLM learn to rank *common* confounders more accurately without
improving on the *true* diagnosis rank), (3) how much of the gain is
executor-choice vs. PIHF-post-training, (4) is the human-feedback loop
scalable to real rare-disease diagnostic deployment (label cost per
case). Should be shortlisted for a methods commentary on HPO-diagnosis
LLM benchmarking alongside Phenolyzer / Phen2Gene / PhenoSV /
PhenoGPT2 / GraphRareBench.

#### HIGH — Jiang Z, Fu Z, Kim Y, Li Z, Peng X, Teng F, Mi J, Wu H. *One Score, Two Decisions: Selective Prediction on the Rare-Disease Tail.* arXiv 2608.14683 2026 (`rare diseases` keyword feed).

**Selective prediction on the rare-disease tail — should the
diagnostic system endorse its first prediction or defer?** Canonical
result: eight small open-weight LLMs achieve **at most 4.6%
Recall@1** on the tail-stratified patient-record subset. Direct hit
on the *ranking vs. evidence coverage* concern in the HPO-diagnosis
sub-thread — the Recall@1 = 4.6% number is a *floor* on how bad
the deferral-free LLM diagnostic pipeline can look at the tail,
and complements PIHF (above) as the *calibration / abstention* axis.
Read for: (1) how they define the "tail" (prevalence cutoff, HPO-term
sparsity), (2) whether their abstention mechanism uses log-probability
calibration or an auxiliary model, (3) whether the deferral behavior
transfers to frontier proprietary LLMs, (4) implications for
LIRICAL / Exomiser / PhenoGPT2 evaluation — does the deferral pattern
match?

#### HIGH — Jang AMH, Lytchakov AJ, Duda JT, Borthakur A, et al. *Advancing Osteoporosis Detection Through AI-Driven CT Segmentation: Insights from Multiple Large Health System Biobanks.* Research Square 2026 (`phenome wide association studies` keyword feed).

**AI-driven CT segmentation of L1 vertebra → osteoporosis phenotype,
with PheWAS linkage across multiple large health-system biobanks.**
Direct hit on the intersection of **PheWAS / phecode infrastructure**
(imaging-derived-phenotype PheWAS) and **Biobanks with EHR linkage**
(phenotype validation against EHR-derived outcomes). The style
(quantitative imaging endophenotype → PheWAS scan) mirrors what UKB
DXA-FM work (LeDXA, 08-08 report) and CAN-FLOW cardiac (08-17 report)
have been building toward. Snippet mentions LBD (low bone density)
linked in PheWAS to "osteoporosis, respiratory failure, sepsis,
coagulation defects, and cardiovascular disease" plus a null GWAS —
suggests either sample-size limits or that quantitative L1 attenuation
captures late-life-multimorbidity confounding rather than an
osteoporosis-specific genetic axis. Read for: (1) which health-system
biobanks (Penn, MGB, Vanderbilt, MSHS…), (2) chart-review-anchored
PPV for the osteoporosis phenotype, (3) whether the PheWAS applies
phecode-based exclusion ranges properly for BMD-adjacent phenotypes,
(4) whether they follow up the multimorbidity signals with an
appropriate DAG / mediation analysis.

#### HIGH — Corponi F, Reami M, Ossola P, Fanelli G, Jauhar S, et al. *Damped Physical Activity and Unstable Sleep: Fitbit-Derived Rest-Activity Phenotypes in Inter-episode Mood Disorders.* medRxiv 2026 (Joshua C. Denny new-related feed).

**Fitbit-derived rest-activity phenotypes persisting during euthymia
in mood disorders.** The framing is directly *pre-symptomatic phenotype
persistence* — the same shape as the pre-symptomatic-phenoconversion
sub-thread (INTERESTS.md line ~201) applied to psychiatry rather than
neurology (ALS). Snippet notes prior evidence draws largely from small
short actigraphy studies; this paper appears to scale that up.
Complements the AoU / UKB *wearable-signals-as-PheWAS-phenotypes*
substrate (INTERESTS.md line ~29 wearable-follow-up bit). Read full-text
for: (1) cohort provenance (which biobank / clinical cohort provides
the Fitbit data), (2) whether the phenotype is scored per-participant
or per-episode-adjacent time-window, (3) whether the "damped physical
activity" measure translates back to accelerometer-derived UKB
phenotypes (portability), (4) whether authors propose a *deployment*
use — e.g., patient-level early-warning for recurrence — which would
push the paper into the **ML for precision health** thread's
tied-to-a-clinical-decision bar.

### Scholar alerts — supporting METHODS-WATCH items (08-22 batch)

#### METHODS-WATCH — Noma H, Goto A, Sugimoto T, Sunada H, Oda F, et al. *Real-world effectiveness of SGLT2 inhibitors in adults aged 75 years or older: a target trial emulation.* Age and Ageing 2026 (Miguel Hernán citations-to feed).

**SGLT2i vs. DPP-4i TTE in Japanese ≥75yo, ITT analysis.** Fires the
Hernán citations-to feed because it cites the TTE reporting-standards
paper. Adds real-world elderly-subgroup evidence for the **SGLT2i
pharmacoepi** sub-thread (INTERESTS.md line ~47) that maps directly
onto the AoU / MVP older-adult subgroups you've been prototyping.
Read for: (1) DPP-4i comparator justification (active comparator ≥
non-user, but is DPP-4i clinically neutral or a substitute-good?),
(2) frailty-adjustment strategy at ≥75yo, (3) whether they report
kidney / heart-failure outcomes separately by baseline eGFR — the
elderly-specific ESKD / hyperkalemia signal is what would change
prescribing.

#### METHODS-WATCH — Chen S, Liang Y, Luo S, Zheng J, Yoshiji S, Power GM, et al. *Elucidating the proteomic pathways linking childhood body mass index with type 2 diabetes: a Mendelian randomization and recall-by-genotype study.* International Journal of Epidemiology 2026 (Joshua C. Denny new-related feed).

**MR + recall-by-genotype design linking childhood BMI → proteomic
pathways → T2D across ethnic groups.** Adds to the **drug-target
MR** rising sub-thread (INTERESTS.md line ~64) with a *proteomics-as-
mediator* extension. Complements the Qasim et al. adaptive-penalization
two-sample MR method from the 08-17 report as the *application-side*
partner. Read for: (1) which proteomic panel (Olink, SomaScan),
(2) how they handle the two-step MR selection of instruments —
horizontal-pleiotropy is severe with proteomics, (3) which ethnic
groups (given the *Yoshiji et al.* lineage this may include East-Asian
UKB or Biobank Japan), (4) recall-by-genotype design specifics — does
it triangulate the MR estimate with a directly-genotyped subgroup?

#### METHODS-WATCH — Barbosa Araujo PV, Fiuza TS, Ferraz RS, Kroll JE, et al. *From Data Curation to Risk Reporting: A Pipeline for Polygenic Risk Scores.* bioRxiv 2026 (Joshua C. Denny new-related feed).

**End-to-end PRS construction pipeline — curation, statistical
methods, reporting.** Adjacent to the **PGS / composite-risk** thread;
usefulness depends on whether it's opinionated (single recommended
method) or agnostic (menu of methods). Read only if actively
constructing PRS in AoU / UKB and you need a checklist paper; likely
overlaps with the STAR Protocols admixed-ancestry PGS paper (above)
and with existing PGS Catalog conventions.

#### METHODS-WATCH — Zhong J, Yu J, Li Y, Qin M, Zou L, Wang Y, Zhang Y, et al. *RareDASH: A Dynamic Multi-Agent System for Holistic Rare Disease Care.* IJCAI preprints 2026 (`rare diseases` keyword feed).

**LLM multi-agent system for holistic rare-disease care** across
diagnosis / medication recommendation / life-cycle management.
Adjacent to the **rare disease** thread and to the LLM-agent line
under the causal-inference thread (agentic pipelines). Read only for
the *architecture recipe* (how they compose agents, evaluation cost)
— the "holistic care" framing is broad enough that the substantive
diagnostic contribution may be thin.

#### METHODS-WATCH — Zheng Z, He M, Yu X, Chen L, Li J, Zhang J, Luo R. *Telomere-to-telomere CHM13 reference reveals missing truth variants and improves deep learning-based variant calling in long-read sequencing data.* Quantitative Biology 2026 (Konrad Karczewski new-related feed).

**T2T-CHM13 as the reference substrate for deep-learning variant
calling in long-read data.** Adjacent to the **Pangenome-informed
variant calling and its downstream PGS-portability consequences**
rising sub-thread (INTERESTS.md line ~89; HPRC v2 lineage). Read if
extending into long-read variant-calling pipelines for AoU / UKB
long-read subcohorts; downgrade to LOW if this is yet-another
DeepVariant-on-CHM13 benchmarking paper.

#### METHODS-WATCH — Ishimura H, Suehiro A, Hira D, Hishinuma E, Kato M, et al. *A rare variant in DPYD c.812delT causes severe adverse events of S-1 in a patient with tongue cancer.* Cancer Chemotherapy and Pharmacology 2026 (Konrad Karczewski new-related feed).

**Case report of a DPYD rare variant → fluoropyrimidine severe
adverse event.** Concrete instantiation of the
*Pharmacogenomic-modifiers-of-medication-persistence / adverse-events*
line (INTERESTS.md line ~59; Psy-PGx / CYP2D6 lineage) in oncology.
Read only if extending into DPYD-directed prescribing or into
PGx-informed medication-persistence work; case reports are low-signal
on their own but useful for the *rare-variant-with-large-effect →
clinical action* narrative.

### Scholar alerts — lower-priority items (batched)

#### MEDIUM — Yee J, Oakes EG, Santacroce L, Feldman CH, et al. *Electronic Cigarette Use and Risk of Incident Rheumatoid Arthritis and Systemic Lupus Erythematosus in the All of Us Research Program.* Seminars in Arthritis and Rheumatism 2026 (`All of Us research program` keyword feed).

Standard AoU EHR + self-report pharmacoepi study. On-thread only for
the **Biobanks with EHR linkage** methods audit — read for how they
handle e-cigarette exposure ascertainment (self-report vs. clinical
documentation), incidence definition (phecode vs. chart), and
confounding by combustible-tobacco co-exposure. Otherwise a
clinical-question paper unlikely to change methods.

#### MEDIUM — Andrews SJ. *What my mother's APOE result taught me about dementia risk.* npj Dementia 2026 (George Hripcsak citations-to feed).

Perspective piece on personal APOE-result interpretation and dementia
risk communication. Adjacent to the **penetrance under
population-screening conditions** framing in PheWAS but at commentary
altitude. Read if drafting a penetrance-and-risk-communication
essay for the APOL1 or BRCA panels.

#### MEDIUM — Meng Y (via Bastarache new-related feed, 08-22). *Patient-reported symptoms, fatigue, functional impairment and quality of life in RYR1-related malignant hyperthermia and exertional rhabdomyolysis.* [Journal 2026].

n=? RYR1 disease deep phenotyping. Adjacent to **rare disease** but
niche; read only if extending into RYR1 / muscle-channelopathy
phenotyping.

#### METHODS-WATCH — Beitzen-Heineke A, Siskin M, Muller M, Bhatt A, et al. *Divergent effects of GnRH agonist and GnRH antagonist treatment on platelet activity and transcriptome.* Cardio Oncology 2026 (Chenjie Zeng new-related feed).

Prostate-cancer androgen-deprivation-therapy platelet effects. Fires
the Zeng-related feed because it's downstream of the prostate CRPC /
mHSPC lineage (Saad et al. from 08-17 report). Read only if the
CardioOnc side of prostate-cancer pharmacoepi is reactivated.

#### LOW — Poursafa P, Jylhävä J. *Aging in the air we breathe: mechanisms and consequences of air pollution exposure for biological aging.* Ageing Research Reviews 2026 (Chenjie Zeng self-cite feed, dual with Stephen B Montgomery citations-to feed).

Review of air-pollution × biological aging, citing Zeng-lineage work.
Off methods thread.

#### LOW — Ostherr K, Engebretsen E, Woods A. *Ambient scribes as narrative technologies.* The Lancet 2026 (Peter Szolovits citations-to feed).

Perspective on ambient AI scribes as narrative technology. Off methods
thread; culture-of-medicine framing.

#### LOW — Kulkarni A, Desai D, Monteiro J. *Case report: compound heterozygous PTH1R variant(s) in a patient with inactivating PTH/PTHrP signalling disorder type 1 (iPPSD1).* JPEM 2026 (`All of Us research program` keyword feed).

Rare-disease case report; AoU cited only as a variant-frequency
lookup. Off primary threads.

#### LOW — Zhang C, Wang R, Zheng H, Zhang H, Liu Y, Wei X, et al. *Physiological World Models for Human State Transitions.* arXiv 2608.15309 2026 (`All of Us research program` keyword feed).

Wearable / physiological world-models framing paper citing AoU as
substrate. Read only if the *digital-twins-from-EHR* commentary
extends to *digital-twins-from-wearables*.

#### LOW — Nahshon C, Fahoum L, Hadar D, Cohen H, et al. *Hormonal contraceptives and cancer risk in women with a BRCA1 or BRCA2 pathogenic variant.* Breast Cancer 2026 (Miguel Hernán citations-to feed).

BRCA-carrier × hormonal-contraceptive cancer-risk cohort. Adjacent to
the Zeng breast-cancer lineage; read only if extending into
BRCA-modifier pharmacoepi.

#### LOW — Ding J, Lu Y, Zhang Q, Zeng Z, Xu W, Fishman N, He Y et al. *The Virtual Embryo Challenge: Generative Modeling of Embryogenesis Across Space, Scale and Time.* arXiv preprint 2026 (Marinka Zitnik + James Zou new-articles feeds, dual hit).

Foundation-model challenge for embryogenesis. Off clinical / EHR
thread.

#### LOW — Ellershaw et al. (already reported above, HIGH). Duplicate-fed via three feeds — no additional bucket needed.

#### LOW — Zheng X, Sedlazeck FJ. *IsoAtlas: Visual interpretation of known and novel transcript isoforms using population-scale long-read evidence.* bioRxiv 2026 (Kai Wang new-related feed).

Isoform-atlas resource; useful reference for RNA-based variant-effect
interpretation, but off the immediate ACMG-classification thread.

#### LOW — Peres MA, Liu P, Tay JRH. *Data Resource Profile: The National Dental Centre Singapore Oral Disease Registry (NDCS-ODR).* International Journal of Epidemiology 2026 (Miguel Hernán citations-to feed).

Data-resource-profile paper. Off-thread.

#### LOW — Wheeler AM, Baker JF, Barton JL, Danila MI, et al. *Extending Service Beyond Active Duty: Generalizability of Rheumatoid Arthritis Research Conducted Among US Veterans.* Arthritis Care & Research 2026 (Hernán citations-to feed).

Veterans / RA generalizability commentary. Off primary methods
threads unless extending into MVP-based RA pharmacoepi.

#### LOW — Tankovic K, Claudepierre P, Vo TT, Le TTK, Iggui S, et al. *Risk of Cancer according to Duration of Targeted Therapy Exposure in Spondyloarthritis.* Arthritis & Rheumatology 2026 (Hernán citations-to feed).

French-nationwide cohort on targeted-therapy duration × cancer risk
in SpA. Off primary thread.

#### LOW — Multiple spine-surgery + AoU descriptive papers (Maity, Haikal, Wang, Yakdan et al., all Spine Journal 2026, `All of Us research program` keyword feed).

Proceduralist-observational analyses using AoU as substrate.
Off methods thread; noise-level for the alert feed.

#### LOW — RelArena / TabPFN-Rel / SKILLER / SearchPatientSpace / etc. (Leskovec / Zitnik / Szolovits generic-LLM-benchmark papers).

Non-clinical LLM / relational-learning benchmarks. Off active
clinical-agent thread.

---

## What's NOT in the report

- **GitHub `arxiv-digest` cron / PR notifications** — none surfaced in
  Gmail search; the local repo commits and the on-disk `digests/`
  directory serve as the digest artifact.
- **NCBI My-NCBI What's-New batches** (AoU / UKB / drug repurposing) —
  none fired in the searched window.
- **bioRxiv / medRxiv Subject Collection Alerts** — none surfaced;
  scholar author feeds carried what medRxiv content there was (e.g.,
  the Corponi et al. Fitbit-mood paper).
- **arxiv.org daily category mailings** (`no-reply@arxiv.org`) — the
  raw upstream feed that supplies the `arxiv-digest` pipeline; papers
  surfaced via the digest are covered in the arxiv-digest section
  above.
- **Substack / newsletters** — noted (Latent Space) but no biomedical
  content in this window crossed the on-thread threshold.
- **08-19 digest file** — no `digests/2026-08-19.md` exists in the
  repo; the arxiv-digest cron produces per-day files only when arXiv
  posts new submissions in-window, so a missing date reflects an
  arXiv-side dry day, not a pipeline gap.

## Next steps to consider

1. **Read Ellershaw et al. Foresight-England (arXiv 2608.16273) full
   text.** Highest-signal single item for the **EHR foundation models**
   thread this window and likely the citable framing paper of the
   quarter. Pair with Burkhart et al. federated GEMs (arXiv 2608.02939)
   as the national-monolith-vs-federated axis.
2. **Bundle Yang et al. LPL context-dependent variant interpretation +
   Friedman & Pollak APOL1 mechanism review** into a "*variant
   interpretation for the Mendelian-to-common-disease boundary*"
   reading pair — LPL and APOL1 are the two cleanest testbeds for the
   biological-context reframing.
3. **Shortlist Suger et al. rare-variant × pan-cancer × AoU pleiotropy
   as the citable AoU-rare-variant biobank paper** for the next
   composite-risk / PGS-tails commentary.
4. **Adopt Zhou et al. STAR Protocols local-ancestry PGS pipeline** as
   the current *actionable* recipe for AoU admixed-cohort PGS
   construction — this is the paper to run, not just cite.
5. **Read PIHF (Nguyen & Shyr) + selective-prediction (Jiang et al.)
   back-to-back** as the *calibration-and-abstention* pair for
   HPO-diagnosis LLM benchmarking; audit whether PIHF's 2.24× Recall@1
   gain holds under a GraphRareBench-style ranking-of-confounders
   decomposition.
6. **Cite Kung et al. regression-not-to-the-mean** whenever a
   longitudinal pharmacoepi analysis (CFTR-modulator persistence, HRT
   discontinuation, GLP-1 RA persistence) reports a "small overall
   effect" from a constant-treatment-effect Cox / logistic model —
   the negative-weighting artifact is the likely explanation and
   duration-heterogeneous effects should be reported instead.
7. **Read Nigam et al. EOCRC + AoU** as an anchor for the EOCRC null-
   result literature; write it into the next CRC-thread notebook if
   the case-definition is chart-validated.
8. **Track Jang et al. imaging-PheWAS osteoporosis** — this is the
   template for future *quantitative-imaging-endophenotype → PheWAS*
   scans, and worth pairing with CAN-FLOW (08-17 report) and LeDXA
   (08-08 report) into a *biobank imaging FM → PheWAS* essay.

_Report generated 2026-08-22 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-22 → next scheduled run._
