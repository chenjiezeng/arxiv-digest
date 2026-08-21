# Research digest report — 2026-08-21

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-21 12:40Z** (~4 days since the
last research-digest report, covering four arxiv-digest cron runs and
three Google Scholar alert batches on 08-18, 08-19, 08-20, and 08-21).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-17.md` → `2026-08-21.md`) | 08-17 → 08-21 daily crons | 4 daily runs. 08-17, 08-21: 0 relevant papers (dry). 08-18: 4 papers (Bayesian epidemic-clock g-computation, zero-inflated causal mediation with non-compliance, digital-health N-of-1 primer, regression-not-to-the-mean under staggered treatment). 08-20: 3 papers (Monroe MFM foundation model, Peru mayoral experience with panel DML, urban rail reliability DML). |
| No `arxiv-digest` email hits from GitHub | — | Same as prior report: `arxiv-digest` commits the digest to the local repo as its artifact rather than emailing PR/cron notifications. The on-disk `digests/` directory *is* the arxiv-digest feed. `notifications@github.com` × `arxiv-digest` returned zero hits in the searched window. |
| Google Scholar alerts (keyword feeds, 08-21 batch, 01:39Z) | 08-21 01:39Z | 10 keyword feeds fired: `variant interpretation`/`variant classification`, `rare diseases`, `electronic health records`, `Foundation models + electronic health records`, `drug repurposing`, `knowledge graph`, `All of Us research program`, `UK Biobank`, `mendelian diseases`, `intitle:clonal hematopoiesis`, `autoimmune diseases`. |
| Google Scholar alerts (08-19 batches, 14:14Z + 21:10Z) | 08-19 14:14Z–21:10Z | 20+ author/citation feeds fired (Karczewski x2, Wendy Chung, Daniel Kastner cites, Chenjie Zeng self, Kai Wang new-related + cites, Jian Yang cites + new-related, Hripcsak new-related + cites, Denny cites, Pritchard cites, Szolovits cites + new-related, Yuan Luo cites, Callahan new-related, Patrick Ryan new-related, Vivek Natarajan cites, Montgomery new-related + cites, Zitnik new-related, Zhiyong Lu new-related, Bastarache cites, **Miguel Hernán cites**) plus 8 keyword feeds. Densest signal from the rare-disease, AoU, and CHIP feeds; the Hernán feed carried a citation to a systematic review of the clone-censor-weight approach. |
| Google Scholar alerts (08-20 batch, 21:23Z) | 08-20 21:23Z | 12+ author/citation feeds fired (Szolovits new-related + cites, Denny new-related, Zitnik new-related, Kai Wang cites, Nigam Shah new-articles, Bastarache cites, Patrick Ryan new-related, Karczewski cites, Jian Yang new-related, Montgomery cites + new-related). Nigam Shah's *NEJM AI* Safety-Risks-in-Medical-AI classification piece is the standout. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fifteen HIGH items surfaced this window, clustering into five knots:

**EHR foundation-models cluster (2 items, one landmark).** Ellershaw,
Tomlinson, Kraljevic, Denaxas et al. arXiv 2608.16273 — **Foresight-England:
a national-scale generative EHR model trained on 54.9 million de-identified
records** (essentially the entire population of England) for medical-event
prediction across the COVID-19 pandemic. This is the *biggest single EHR-FM
substrate the field has seen* and directly extends the CogStack / Foresight
lineage (Kraljevic KCL / Denaxas UCL) to whole-population scale. Direct hit
on the **EHR foundation models** thread and the **Digital twins from EHR
data** rising sub-thread — trajectory-prediction on this cohort is
approximately the operational template for a population-scale digital twin.
Read alongside the CLMBR / MOTOR / EHRSHOT / MEDS lineage as the
comparability question ("what does a country-scale FM buy over a
health-system-scale FM"). Li et al. *npj* 2026 (Hripcsak new-related feed) —
**parameter-efficient federated LLM framework for privacy-preserving,
multi-institutional adaptation in medicine**. Directly serves the
**federated / privacy-preserving EHR causal analytics** rising sub-thread
(Jang et al. arXiv 2607.17958 lineage): a parameter-efficient recipe
lowers the compute floor for network studies across BioVU/AoU/UKB/MVP.

**AoU + PGS cluster (2 items).** Kosgolla & Smith *Addiction* 2026 (AoU
keyword feed) — **joint associations of recovery capital and polygenic
risk with EHR-observed remission and relapse in substance use disorder**,
using the AoU cohort with a longitudinal EHR-derived phenotype. This is
a textbook **PGS × environment interaction** applied to an AoU
EHR-derived outcome — matches the Nagpal & Gibson *Nature Genetics* 2026
scaffold on the *disease side* (rather than the drug-effect side handled
by Reho pharmacoexposomics from the last report). Kullo, Horowitz,
Bastarache, Berkman et al. 2026 (AoU feed) — **workshop-consensus
recommendations for return of secondary genomic findings in
observational cohort studies** (Geisinger MyCode, AoU, NIDDK). Bastarache
co-authorship makes this canonical for the PheRS/PheWAS community; it
serves both the **ACMG / ClinGen variant curation** thread and the
**AoU / UKB / MVP / BioVU** biobank-linkage thread. Should sit alongside
existing return-of-results policy anchors in the CFTR / BRCA / secondary
findings work.

**Somatic mosaicism cluster (1 item, direct-thread).** Meyre, Ahn, Ehlert,
Dederichs et al. *Circulation* 2026 (`intitle:clonal hematopoiesis` feed)
— **CHIP is associated with silent brain lesions and cognitive decline in
patients with atrial fibrillation**, using a **custom TWIST 94-gene CHIP
panel** covering 323 kb of exonic targets. Direct hit on the **CHIP /
VEXAS / LOY somatic-mosaicism** thread (INTERESTS.md line ~103) and on
the *CHIP-vascular-outcomes* Loh 2018 / Kessler 2022 / Bick 2020 lineage
— the outcome is not incident CV death but **silent brain infarcts** on
imaging plus **cognitive decline trajectories**, which is a novel outcome
axis for the CHIP-atherosclerosis mechanism. Pairs with Li et al.
*Atherosclerosis* 2026 LOY×PAD (from prior INTERESTS updates) as the
"CHIP/LOY meets vascular imaging" pair. The TWIST panel design is worth
harvesting as a template for AoU / UKB WGS-derived CHIP-VAF re-analyses.

**LLM-assisted rare-disease diagnosis cluster (5 items, unusually
concentrated).** Schächter, Pechmann, Kirschner, Hasenauer et al. arXiv
2608.16507 — **LLMs as synthetic clinical experts to inform longitudinal
rare-disease modeling**, reducing expert-disagreement across
disease-type boundaries. Direct hit on the **Auditable HPO-driven
diagnostic benchmarks** sub-thread (INTERESTS.md line ~195). Jiang, Fu,
Kim, Li, Peng, Teng, Mi, Wu arXiv 2608.14683 — **One Score, Two Decisions:
Selective Prediction on the Rare-Disease Tail** — eight small
open-weight LLMs achieve at most 4.6% Recall@1 on prevalence-stratified
records, forcing an *abstain-vs-endorse* gate. This is the exact
GraphRareBench extension (the "Hit@10 hides ranking-of-confounders"
observation you flagged for propagation) with a *calibration-and-selective-
prediction* lens layered on. Nguyen & Shyr arXiv 2608.16831 — **Policy
Iteration with Human Feedback (PIHF)** — post-training RL for in-context
learning, moving frontier-executor Recall@1 on 1,243 public rare-disease
benchmark cases **from 26.5% → 59.3%** with transfer to open-weight
executors. Zhong et al. arXiv (IJCAI 2026) — **RareDASH: a dynamic
multi-agent system for holistic rare-disease care** across the *full
life-cycle* (diagnostic + medication + follow-up), rather than an
isolated task. Batson, Lombardo, Leeflang, Taylor-Phillips et al. *J Clin
Epi* 2026 — **methodology for test-accuracy study designs for rare and
ultra-rare conditions**, applied to newborn blood-spot screening. This is
the **evaluation-methodology anchor** the rare-disease LLM-diagnosis
work-cluster lacks; every one of Schächter / Jiang / Nguyen / Zhong needs
a design like this to make PPV / sensitivity / prevalence-adjusted
claims defensible.

**Genetic-epi + biobank cluster (3 items).** Ao, Kolifarhood, Parisien,
Bortsov, Grant et al. *Genome Medicine* 2026 (Jian Yang + Montgomery
dual-feed hit) — **exome-wide association study for chronic pain in
327,642 UK Biobank participants**, common + rare coding variants.
Directly serves the **GWAS / genetic epi** thread and the **rare-variant
+ composite-risk** sub-thread (pain is a chronic phenotype where PheWAS
outcome-definition choices are highly consequential). Chen C 2026
(*J Med Genet*, UKB feed) — **actionable genotypes beyond the coding
sequence and their association with lifespan in the UK Biobank**. Directly
serves the **ACMG / ClinGen** thread (INTERESTS.md line ~66) and the
**AoU / UKB / MVP / BioVU** biobank-linkage thread; the noncoding
extension is exactly the axis on which InterVar / VarSome deployments
degrade. TOPMed Consortium *Science* 2026 (UKB feed) — **cross-cohort
eQTL/sQTL colocalization for 10,611 UK Biobank GWAS signals** across 164
traits, with 7,096 colocalizations that involve *secondary* e/sQTLs.
This is the reference resource for the **PGS + expression / splicing
integration** work in cardiometabolic and psychiatric traits — direct
predecessor of multi-omics-augmented PRS in the rising composite-risk
framing.

**Pharmacoepi methods (1 item, direct-thread).** Manzanilla, Brunetta,
Peyre-Pradat, Michiels et al. *J Clin Epi* 2026 (Miguel Hernán citations
feed) — **systematic methodological review of the clone-censor-weight
(CCW) approach for avoiding immortal-time bias in target-trial
emulation**. This is the *authoritative review* to cite when the
CFTR-modulator, GLP-1 RA, HRT, or pregnancy pharmacoepi projects invoke
CCW; complements the Wood et al. perinatal-TTE paper from the 08-17
report (both address subtly-different ITB sources).

**ML for precision health (1 item, framing-paper level).** Sheng, Song,
Shah, Wu, Car, Wong *NEJM AI* 2026 (Nigam Shah new-articles feed) —
**A Classification of Safety Risks in Medical AI**. Reference framing
paper for any ML-for-precision-health work that touches deployment
safety. Read before writing about clinical-agent evaluation; likely
becomes a citable taxonomy alongside the FDA / MHRA / FUTURE-AI
guidance stack.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-17 → 2026-08-21)

#### METHODS-WATCH — Moriña D. *Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions.* arXiv 2608.16537v1 (stat.ME, 2026-08-17). Score 1.

Bayesian causal count model that treats each season's calendar-to-
epidemic-clock mapping as a *model component* (season-specific affine
transformations), so intervention effects are estimated on the aligned
epidemic clock and *timing uncertainty propagates into every causal
contrast*. Uses a negative-binomial observation distribution,
hierarchical area / season / area-season effects, a shrunk Fourier
epidemic curve, and a continuous program-intensity exposure; posterior
g-computation delivers prevented cases, prevented fractions, peak
attenuation, and epidemic displacement under both controlled and
dynamic contrasts. Applied to Catalan primary-care surveillance and RSV
immunization data. **Bookmark for the seasonal-outcomes edge cases**
(influenza vaccination effectiveness in AoU / UKB, RSV immunization
effectiveness studies in MVP): the "align on latent epidemic clock, not
calendar week" idea is portable to any seasonal outcome where phase
shift between years is a confounder to intervention timing. Off the
current watchlist but a strong template.

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. *Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.* arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1.

Bayesian causal mediation framework based on enriched Dirichlet-process
mixture models with a scalable G-computation algorithm, designed for the
*jointly hard* case of (i) treatment non-compliance, (ii) multiple
longitudinal mediators, and (iii) zero-inflated mediators and outcomes.
Applied to a large digital-marketing-campaign dataset (value-added
incentives vs. traditional discounts), but the modeling recipe is
identical to what a **medication-adherence-mediated pharmacoepi
analysis** needs: patient non-compliance with GLP-1 RA / CFTR
modulator / SSRI initiation, multiple longitudinal mediators (MPR, dose,
concomitant meds), zero-inflated outcomes (event counts). Directly
complementary to Bandreddi et al. (Tobit-vs-hurdle for zero-inflated
CHIP-VAF, 08-17 report) on the zero-inflation modeling axis, and to the
CCW / Wood-perinatal-TTE anchors on the compliance axis. **Adopt this
DPM+G-comp recipe as a candidate architecture** for any pharmacoepi
analysis that has all three complications at once.

#### METHODS-WATCH — Daza EJ. *A Primer on Digital Health N-of-1 Studies and Single-Case Designs.* arXiv 2608.15526v1 (stat.AP, 2026-08-16). Score 1.

Chapter-length primer on **n-of-1 studies, single-case designs, and
"multitudinal" approaches** for digital-health data — characterizing a
single person's *own* recurring health patterns rather than nesting them
in the best subgroup. Coins "esametry" (statistics of the digitized
multitudes within a person). Relevant to the **Machine learning for
precision health** thread and to the **Digital twins from EHR data**
rising sub-thread (INTERESTS.md line ~117) — an individualized digital
twin is arguably a formal n-of-1 model. Also the correct methodological
frame for **CGM-based diurnal glucose studies** (Abner et al. *Nature*
2026, prior report), for **wearable-based ABCD digital-phenotype GWAS**
work (Gerstein-lab lineage), and for the CFTR-modulator-eligibility
individualized-response question. Read as background for any wearable /
CGM / accelerometer analysis on UKB or AoU.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. *Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.* arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1.

Shows that a constant-treatment-effect model in a **staggered treatment
with heterogeneous durations** setting can produce a weighted average
with *negative weights* over duration-specific effects — so the estimated
constant effect can be smaller in magnitude, or even the *opposite sign*,
of nearly all duration-specific HTE estimates. Demonstrated on
drug-induced-homicide prosecutions × overdose deaths; extends the
econometrics literature by showing the pathology arises in **logistic
regression** too (not just linear). **Directly relevant to any
pharmacoepi HTE analysis with staggered adoption**: SGLT2i introduction
across health systems, CFTR-modulator uptake across CF centers, HRT-
formulation shifts across menopause clinics. If you're running a causal
forest or a meta-learner on staggered-adoption cohorts, the ATE the CF
gives you may misrepresent the sign of the CATE at every duration.
Should be cross-cited whenever the HTE section relies on a
constant-effect baseline for context.

#### METHODS-WATCH — Banaszewski B, Fitzgibbon AW. *Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference.* arXiv 2608.18982v1 (cs.LG, 2026-08-19). Score 1.

Molecular foundation model pre-trained on 81M PM6-quantum-chemistry
molecules with three notable methodological choices: (1) improved graph
representation of stereochemistry, (2) conformer denoising + embedding
decorrelation losses, (3) TabPFN prior-data-fitted model as the
downstream in-context predictor. Also releases MiniMol_PFN and
CheMeleon_PFN — the *TabPFN downstream adapter is drop-in-portable* to
prior MFMs and boosts them too. Off your active clinical-EHR threads,
but worth a bookmark for the **drug repurposing** thread whenever
QSAR / ADMET / activity-cliff prediction gates a repurposing candidate;
the "small-cohort in-context prediction on MFM embeddings" recipe is
directly applicable to the pharmacogenomic-modifier work as well
(cyp2d6 substrate prediction at small N).

#### SKIP — Machacuay C, Lincovil J, Rojas H. *Mayoral Experience or Municipal Capacity? Negative-Outcome Evidence on Municipal Budget Execution in Peru.* arXiv 2608.18354v1 (stat.AP, 2026-08-18). Score 1.

Peruvian district municipalities × mayoral experience × budget
execution, with panel DML and a **negative-outcome control**
(first-difference alignment shows changes in experience do *not* predict
predetermined GDP — a clean falsification design). Off-topic biomedically,
but the **negative-outcome-control-on-first-differences** trick is a
transferable design idea for pharmacoepi self-control studies. Filed for
methods reference only.

#### SKIP — Yao Y, Zhang N, Graham DJ. *Quantifying the Causal Operational Determinants of Service Reliability in Urban Rail Transit: Evidence from Panel Double/Debiased Machine Learning.* arXiv 2608.17901v1 (stat.AP, 2026-08-18). Score 1.

Urban rail reliability × 90+ candidate variables using panel DML.
Off-topic; ships as an applied DML example.

### Scholar alerts — 08-21 keyword feeds (05:39Z UTC-normalized)

#### HIGH — Ellershaw S, Tomlinson C, Kraljevic Z, Denaxas S, et al. *Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic.* arXiv 2608.16273 2026 (dual hit: `electronic health records` + `Foundation models + electronic health records` feeds).

**Foresight-England scales the CogStack / Foresight EHR-FM lineage
(Kraljevic KCL, Denaxas UCL) to essentially the entire population of
England — 54.9M de-identified individuals — for medical-event prediction
across the COVID-19 pandemic.** This is the single largest EHR-FM
substrate in the field to date and the direct national-scale extension
to the CLMBR / MOTOR / EHRSHOT / MEDS body of work. Direct hit on the
**EHR foundation models** thread (INTERESTS.md line ~110) and on the
**Digital twins from EHR data** rising sub-thread (line ~117). Read
full-text for: (1) the tokenization / event schema (SNOMED? UK codes?),
(2) the pandemic-period covariate-shift audit (Foresight-England
explicitly frames a *cross-pandemic* prediction task, which is a good
distribution-shift stress test), (3) whether they released trained
weights or an inference API for external replication, (4) *fairness /
sub-population calibration* (they claim representativeness across all
backgrounds — verify by ancestry, socioeconomic decile, region), (5)
whether it beats CLMBR / MOTOR head-to-head on a benchmark task and by
how much. This should become the *reference comparison model* for any
future EHR-FM work discussing scaling, and pairs with a national-scale
digital-twins essay next to the Zhang / Ideker / Oermann *Cell* 2026
framing paper.

#### HIGH — Kosgolla JV, Smith DC. *Joint associations of recovery capital and polygenic risk with electronic health record observed remission and relapse in substance use disorder: Longitudinal evidence from the All of Us research program.* Addiction 2026 (`All of Us research program` feed).

**PGS × recovery capital (a psychosocial-exposure construct) with an
EHR-observed longitudinal remission/relapse outcome in AoU.** Direct hit
on **Biobanks with EHR linkage: All of Us** and on the **PGS × exposure
/ environment interactions** rising sub-thread (INTERESTS.md line ~76;
the Nagpal & Gibson *Nature Genetics* lineage but on the *disease-course*
side rather than the disease-risk side). Read for: (1) the SUD phecode
definition (which SUD phecodes; incident vs. prevalent), (2) the
recovery-capital operationalization (structured survey vs. NLP-derived),
(3) the longitudinal-remission-relapse outcome-modeling choice (survival
vs. multi-state; recurrent-event Andersen-Gill or Prentice-Williams-
Peterson), (4) whether they tested for genotype × recovery-capital
statistical interaction on the additive scale (the correct scale for
public-health-relevant PGS-modifier claims), (5) whether the results
replicate across ancestry strata. Naturally pairs with the Abner *Nature*
diurnal-glucose paper (prior report) as the AoU × PGS × environment
dual anchor.

#### HIGH — Kullo IJ, Horowitz CR, Bastarache L, Berkman B, et al. *Recommendations for return of secondary genomic findings in observational cohort studies.* 2026 (`All of Us research program` feed, PDF pre-print).

**Consensus workshop-derived recommendations covering Geisinger MyCode,
AoU, NIDDK-hosted cohorts.** Bastarache co-author is what elevates this
to HIGH for our threads — she is core to the PheRS / PheWAS-in-return-of-
results community. Direct hit on the **ACMG / ClinGen variant curation**
thread (INTERESTS.md line ~66) and on **AoU / UKB / MVP / BioVU**.
Read for: (1) the recommendation matrix (which secondary-finding
categories go back to participants under which conditions), (2) how they
handle the AoU-specific return-of-results workflow (which was still
under-specified at last review), (3) whether they cite PheRS as a
*prioritization instrument* for which secondary findings to prioritize
(the natural role for PheRS in a return-of-results pipeline), (4) IRB /
informed-consent language recommendations. Cite whenever writing about
CFTR / BRCA / hereditary-cancer return-of-results workflows or when the
methods section needs a policy anchor.

#### HIGH — Meyre PB, Ahn HJ, Ehlert CA, Dederichs TS, et al. *Association of Clonal Hematopoiesis With Silent Brain Lesions and Cognitive Decline in Patients With Atrial Fibrillation.* Circulation 2026 (`intitle:"clonal hematopoiesis"` feed).

**CHIP × silent brain infarcts on imaging × cognitive-decline
trajectory in an atrial-fibrillation cohort**, using a **custom TWIST
targeted panel covering 94 CHIP + hematologic-cancer genes (323 kb of
exonic sequence)**. Direct-thread hit on **CHIP / VEXAS / LOY somatic
mosaicism** (INTERESTS.md line ~103). Novel-outcome extension of the
CHIP-vascular-outcomes literature (Jaiswal / Bick / Kessler lineage):
moves the outcome from *incident CVD/mortality* to *silent
cerebrovascular disease + cognitive decline*, which is where the AF
population is unusually informative (AF is itself associated with
silent embolic infarcts, so CHIP-amplifies-thrombogenic-inflammation is
mechanistically plausible). Read for: (1) the exact 94-gene panel design
(gene list and coverage depth — worth harvesting as a template for AoU /
UKB WGS-derived CHIP-VAF re-analyses), (2) which CHIP driver mutations
individually drive the signal (TET2? DNMT3A? ASXL1?), (3) whether they
adjusted for AF-specific anticoagulation choices, (4) VAF-threshold
sensitivity (0.02 vs. 0.10 cut). Pairs with Li et al. LOY×PAD
*Atherosclerosis* 2026 (from prior INTERESTS updates) as the
"CHIP/LOY-meets-vascular-imaging" pair.

#### HIGH — Schächter C, Pechmann A, Kirschner J, Hasenauer J, et al. *Large language models as synthetic clinical experts to inform longitudinal rare-disease modeling.* arXiv 2608.16507 2026 (`rare diseases` feed).

**LLMs as *synthetic clinical experts* for longitudinal rare-disease
modeling**, with an explicit reduction-in-expert-disagreement axis
(across disease-type boundaries). Direct hit on **Rare disease** and on
the **Auditable HPO-driven diagnostic benchmarks** rising sub-thread
(INTERESTS.md line ~195). The "LLM as synthetic expert" framing is the
same architecture as egg-computation (Vossler et al., prior report) but
applied to disease-course modeling rather than QI intervention timing
— a portable pattern. Read for: (1) how they measure "clinical
faithfulness" of LLM-derived expert opinions against a ground-truth
subset, (2) whether the disease-type-boundary reduction generalizes
across rare-disease families (e.g., SMA vs. metabolic vs. HLH), (3)
whether the LLM output is uncertainty-calibrated (an LLM expert that
under-reports uncertainty is *worse* than a human expert), (4) how it
interoperates with HPO-based prior work. Read alongside Nguyen & Shyr
PIHF and Jiang et al. selective-prediction (both below) as a
three-paper *"rare-disease LLM operating point"* snapshot.

#### HIGH — Jiang Z, Fu Z, Kim Y, Li Z, Peng X, Teng F, Mi J, Wu H. *One Score, Two Decisions: Selective Prediction on the Rare-Disease Tail.* arXiv 2608.14683 2026 (`rare diseases` feed).

**Selective prediction on rare-disease diagnostic ranking**: eight small
open-weight LLMs achieve *at most 4.6% Recall@1* on
prevalence-stratified patient records, so the correct operating point is
an *abstain-vs-endorse gate* rather than a Recall@k number. This is the
direct extension of the GraphRareBench "22–44% Hit@10 hides
ranking-of-confounders" observation (07-29 report) with a *calibration
and selective-prediction* lens on top. Read for: (1) the exact
calibration method (temperature scaling? conformal?), (2) whether the
abstain gate improves clinical utility net of the recall loss (utility
decomposition matters), (3) which prevalence stratum the abstain-gate
helps most in (natural expectation: helps most on the ultra-rare tail),
(4) how the *frontier* proprietary LLMs perform under the same protocol.
Cite alongside Nguyen & Shyr PIHF (below) as "the two rare-disease LLM
papers of the summer that finally treat calibration seriously."

#### HIGH — Nguyen MH, Shyr C. *Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning.* arXiv 2608.16831 2026 (`rare diseases` feed).

**Policy Iteration with Human Feedback (PIHF)** lifts Recall@1 on 1,243
public rare-disease benchmark cases **from 26.5% → 59.3%** on a frontier
proprietary executor with transfer to open-weight executors. This is a
+33-absolute-point jump on the same benchmark, which is unusually large
for a training-time-free method (PIHF is in-context RL). Directly serves
the **Rare disease** thread and the **Auditable HPO-driven diagnostic
benchmarks** sub-thread. The "convert scarce expert reasoning into
in-context updates" framing rhymes with Vossler et al. egg-computation
(prior report) — expert reasoning is scarce, LLMs are cheap, close the
loop with policy-iteration-style feedback. Read for: (1) the benchmark
identity — is it the same as GraphRareBench, PhenoGPT2's benchmark, or
distinct? (2) how the frontier→open-weight transfer works when the open
executor has different context handling, (3) the feedback-signal
composition (does it need clinician annotations or can it be
LLM-synthesized). Naturally reads alongside Schächter and Jiang above
as a three-paper cluster.

#### HIGH — Zhong J, Yu J, Li Y, Qin M, Zou L, Wang Y, Zhang Y, et al. *RareDASH: A Dynamic Multi-Agent System for Holistic Rare Disease Care.* IJCAI 2026 preprint (`rare diseases` feed).

**Dynamic multi-agent LLM system spanning the *full life-cycle* of
rare-disease care** — diagnostic + medication recommendation +
follow-up — rather than an isolated task. Direct hit on the **Rare
disease** thread and (crucially) on the **agentic / human-in-the-loop
pipelines** rising sub-thread that has been extending into rare-disease
turf. The "full life-cycle" scope is what elevates this over one-task
LLM diagnosis papers. Read for: (1) the agent-composition scheme
(specialized-agent taxonomy — HPO-mapper, differential-generator,
literature-retriever, dose-recommender, follow-up-scheduler), (2) how
they orchestrate the agents (message-passing? deterministic pipeline?
LLM-router?), (3) the benchmark used and whether it evaluates the
*chain* rather than just each agent independently, (4) whether the
patient-centric framing they claim maps to a real EHR workflow. Highest
utility as a reference architecture for a **rare-disease clinical
copilot** proof-of-concept.

#### HIGH — Batson S, Lombardo S, Leeflang M, Taylor-Phillips S, et al. *Evaluating Test Accuracy Study Designs for Rare and Ultra-rare Conditions: Application to Newborn Blood Spot Screening.* Journal of Clinical Epidemiology 2026 (`rare diseases` feed).

**Methodology-review paper on test-accuracy study designs for rare and
ultra-rare conditions**, with newborn-blood-spot screening as the
running application. This is the *evaluation-methodology anchor* the
four rare-disease LLM-diagnosis papers above collectively lack: without
a defensible prevalence-adjusted design, none of Schächter / Jiang /
Nguyen / Zhong can make PPV / sensitivity / NPV claims that transfer to
a clinical deployment. Read for: (1) the design-choice matrix
(prospective cohort vs. registry-based vs. two-gate vs. multi-gate),
(2) how to handle prevalence when it's *~10^-4 or lower*, (3) whether
they explicitly discuss designs that combine an LLM diagnostic system
with a downstream confirmatory test. Cite whenever the rare-disease
LLM-diagnosis thread graduates from a benchmark to a deployment
evaluation.

#### HIGH — Halper-Stromberg E, Narayan S, Laufer V, Limson M, et al. *Clinical Variant Interpretation with the Integrative Genomics Viewer (IGV) for Molecular Pathologists.* Journal of Visualized Experiments 2026 (`variant interpretation` / `variant classification` feed).

**Standard-of-practice paper for using IGV in molecular-pathology
variant interpretation.** Direct hit on the **ACMG / ClinGen variant
curation** thread. IGV is the *de facto* visualization layer for read-
level evidence in ACMG-AMP calls (BS3 functional evidence, PS3 CNV
support, sanity-checking a suspected FP). Read as a training-material
anchor if the CF / BRCA / cardiomyopathy panel-interpretation workflow
needs a citable process paper. Bookmark alongside Mitev variant-
classification-platform framework (prior report) as the "how to
operationalize a variant-interpretation program" pair.

#### MEDIUM — Chen C. *Supplementary Appendix: Actionable genotypes beyond the coding sequence and their association with lifespan in the UK Biobank.* J Med Genet 2026 supplement (`UK Biobank` feed).

**Actionable-genotype (ACMG SF list) analysis extended beyond the
coding sequence, with cause-specific lifespan as outcome, in UKB.**
Direct thread hit on **ACMG** + **UKB**. This is the supplementary-
appendix listing; the primary paper (Chen 2026 J Med Genet) is the
citation to track. Read for: (1) the noncoding actionable-variant
definition (splice? regulatory? UTR? intronic?), (2) how they combined
noncoding + coding actionable into a single carrier definition, (3)
lifespan-reduction magnitude, (4) whether the analysis adjusted for
selection of long-lived participants (UKB healthy-volunteer bias). If
the effect sizes are non-trivial, this feeds directly into the
composite-risk PGS + rare-pathogenic thread (INTERESTS.md line ~76).

#### MEDIUM — Ao X, Kolifarhood G, Parisien M, Bortsov A, Grant AV, et al. *Exome-wide association study reveals common and rare coding variants shaping chronic pain in 327,642 UK biobank participants.* Genome Medicine 2026 (dual hit: Jian Yang + Stephen Montgomery new-related feeds).

**ExWAS on chronic pain in n=327,642 UKB participants**, common + rare
coding variants. Adjacent to **GWAS / genetic epi** and to the
composite-risk sub-thread. Chronic pain is a phecode where
outcome-definition choices are unusually consequential (self-report vs.
opioid Rx vs. ICD-based). Read for: (1) chronic-pain phenotype
definition, (2) whether rare-variant burden tests (SKAT-O / STAAR) were
applied and what genes surfaced, (3) whether they built a PGS and
tested its portability. Downgrade to LOW if it's a plain common-variant
GWAS with a rare-variant appendix.

#### MEDIUM — TOPMed Consortium (Consortium 32 authors). *Cross-cohort analysis of expression and splicing quantitative trait loci in TOPMed.* Science 2026 (`UK Biobank` feed).

**Cross-cohort eQTL / sQTL fine-mapping in TOPMed with 164 UKB
GWAS traits × 10,611 GWAS signals colocalized with e/sQTLs (7,096
involving *secondary* e/sQTLs)**. Reference-resource paper for the
multi-omics-augmented PRS thread (composite-risk rising sub-thread,
INTERESTS.md ~76). The **secondary-e/sQTL** finding is notable — it
suggests substantial GWAS signal is buried in secondary regulatory
variants that a naive fine-mapping pass would miss. Read for: (1)
tissue-mapping (which tissues drove the colocalizations), (2) ancestry
composition of the TOPMed reference (portability question), (3) whether
they deposited a public colocalization catalog that can be layered onto
future GWAS. Downgrade to LOW if you're not actively building or using
PGS this quarter.

#### HIGH — Li A, Chen Y, Long W, Yin Y, Hu Y, Kim H, Zhou W, et al. *Toward federated large language models in medicine: a parameter-efficient framework for privacy-preserving, multi-institutional adaptation.* npj [Digital Medicine or npj Health Systems] 2026 (George Hripcsak new-related feed).

**Parameter-efficient federated LLM framework for privacy-preserving,
multi-institutional adaptation** — LoRA-style adapters at each site with
a federated aggregation step. Direct hit on the **federated /
privacy-preserving EHR causal analytics** rising sub-thread (INTERESTS.md
line ~54). Parameter-efficient federation lowers the compute floor
enough that a BioVU × AoU × MVP × MIMIC federated adaptation experiment
becomes tractable without sharing raw records. Read for: (1) the
communication-round budget, (2) the privacy formalization (differential
privacy? secure aggregation?), (3) heterogeneity handling across sites
with different EHR representations, (4) whether they validate on a
clinical task (phecode prediction? mortality? readmission?) versus an
NLP benchmark. Slot next to Jang et al. arXiv 2607.17958 as the second
federated-EHR anchor of the quarter.

#### HIGH — Sheng B, Song J, Shah NH, Wu J, Car J, Wong TY. *A Classification of Safety Risks in Medical AI.* NEJM AI 2026 (Nigam Shah new-articles feed).

**Taxonomy of safety risks in medical AI**, in NEJM AI, from a
first-tier authorship group (Nigam Shah, Tien Wong, Josip Car). Reads
as a *foundational framing* paper for ML-for-precision-health work.
Direct hit on **Machine learning for precision health** and on any
clinical-agent evaluation writing. Read for: (1) the risk-category
taxonomy (data / model / deployment / oversight), (2) whether it maps
onto FDA / MHRA / FUTURE-AI guidance, (3) whether it explicitly covers
LLM-agent risks (contamination, hallucination, adversarial-prompt), (4)
whether they recommend a per-risk mitigation matrix. Cite as the risk
framing whenever the RareDASH / PIHF / clinical-agent work above is
proposed for deployment.

#### METHODS-WATCH — Manzanilla A, Brunetta C, Peyre-Pradat F, Michiels S, et al. *Use of clone-censor-weight to avoid immortal-time bias: a systematic methodological review.* Journal of Clinical Epidemiology 2026 (Miguel Hernán citations feed).

**Systematic methodological review of the CCW approach for immortal-
time bias in target-trial emulation.** Direct hit on **Causal inference
and pharmacoepidemiology**. This is the CCW review to cite in every
future TTE that invokes clone-censor-weight — CFTR modulator, GLP-1 RA,
HRT, SGLT2i, statin. Complements the Wood et al. perinatal-TTE paper
(prior report; both address subtly-different sources of immortal-time
bias — CCW is a *misclassification* fix while Wood is a *time-zero-
selection* fix). Should replace older CCW citations in the pharmacoepi
methods paragraph.

#### MEDIUM — Perry J, Murzynowski J, Kerrison N, Day F, Luan J, et al. *Exploring Rare Genetic Variation Underlying Metabolic Traits in the Fenland Cohort.* 2026 preprint (Denny citations feed).

**Rare-variant metabolic-trait analysis in the Fenland cohort via
WES.** Adjacent to the **rare-variant + composite-risk** thread. Fenland
is a mid-scale cohort; the results are worth tracking as a
non-UKB/AoU/MVP comparator on WES metabolic phenotypes. Read only if
extending the composite-risk framing to metabolic traits, or if the
paper cites Denny lineage for a phecode-based metabolic outcome
definition.

#### MEDIUM — Zou L, Whitley O, Tseng HW, Simopoulos C, Chang D, et al. *scEPS integrates genetic and single-cell disease atlas data to provide granular mechanistic insights into complex human diseases.* medRxiv 2026 (Jian Yang citations feed).

**scEPS integrates genetic + single-cell disease-atlas data** for
mechanistic dissection of complex-disease loci. Adjacent to the
**GWAS / functional-interpretation** thread. Bookmark as a candidate
tool if the single-cell / GWAS integration angle becomes active in the
CHIP / LOY / CF work.

#### LOW — Nigam A, Onongaya C, Meshram P, Frebault J, et al. *Traditional Risk Factors Are Not Associated with the Rise of Early-Onset Colorectal Cancer: An All of Us Study.* Diseases of the Colon & Rectum 2026 (`All of Us research program` feed).

**AoU-based early-onset CRC association study.** Off primary methods
threads (no genomic / phenotyping-methods hook), but the *negative
result* on traditional risk factors is scientifically notable — worth a
line in a future EOCRC discussion. Not a HIGH item because the paper
doesn't advance methods you're actively building.

#### LOW — Zhang Q, Xu J, Deng S, Li X, Li Z, Xing S, Wang S, et al. *Association between puberty timing and overall survival in male cancer patients: a prospective cohort analysis from the UK Biobank.* BMC Cancer 2026 (`UK Biobank` feed).

Standard UKB observational analysis of pubertal-timing × cancer
survival in men (n=22,902). Off your methods threads; noted for
completeness.

#### LOW — Wang Y, Miao X, Withers M, MCS et al. *Insights into the relationship between menopausal timing and risk of cardiovascular disease: a systematic review and meta-analysis of Mendelian randomization…* 2026 (`mendelian diseases` feed).

MR meta-analysis on menopausal-timing × CVD. Peripherally relevant to
HRT-pharmacoepi (menopause is the natural conditioning variable), but
this is a meta-analysis rather than a primary methods contribution.
Bookmark for HRT discussion citations.

#### LOW — Schachter et al. companion papers (see cluster above); IgG4 review (autoimmune keyword feed); anti-aging drug repurposing (VG et al. Genetics & Molecular Research); maritime KG routing.

Off primary methods threads. Filed for completeness.

### Scholar alerts — 08-19 author/citation feeds

#### METHODS-WATCH — see above: Manzanilla et al. CCW review (already reported as HIGH under the Hernán feed).

#### MEDIUM — Xue S, Hu C, Li L, Einspieler H, Kiss A, Podesser BK, et al. *Longitudinal [18F]FDG PET/MR Assessment of Arterial Inflammation in Patients With Prostate Cancer Undergoing Androgen Deprivation Therapy.* 2026 (Chenjie Zeng self-related feed).

Self-related-feed hit downstream of Zeng's prostate-cancer
epidemiology lineage; ADT-cardiovascular-toxicity imaging paper. Not on
the active methods watch — bookmark only if the ADT-CV subthread
reactivates.

#### LOW — Duz MB, Lasa-Aranzasti A, Cazurro-Gutiérrez A, et al. *Clinical characterization and genotype–phenotype correlations in Chilton-Okur-Chung syndrome.* BMC Medical Genomics 2026 (Wendy Chung new-articles feed).

Rare-syndrome genotype-phenotype paper. Adjacent to rare disease thread
but very small-cohort clinical case series. Filed.

#### LOW — Abner E et al. *Genetic variants affect diurnal glucose levels throughout the day.* Nature 2026 (Konrad Karczewski new-related feed).

**Already reported as HIGH in the 08-17 report** (diurnal-glucose GWAS
via functional-time phenotype). Same paper re-firing on the Karczewski
new-related feed on 08-19. Duplicate — no new content, but a signal
that the paper is being widely cited across Karczewski's related-work
network. No further action.

#### LOW — Ao X et al. *Exome-wide association study reveals common and rare coding variants shaping chronic pain in 327642 UK biobank participants.* Genome Medicine 2026 (Stephen B Montgomery new-related feed).

**Already reported as MEDIUM under 08-21 UKB feed** — same paper firing
on Montgomery's new-related feed on 08-19. No further action.

### Scholar alerts — 08-20 author/citation feeds

#### HIGH — Sheng B, Song J, Shah NH, Wu J, Car J, Wong TY. *A Classification of Safety Risks in Medical AI.* NEJM AI 2026 (Nigam Shah new-articles feed).

**Same as HIGH under 08-21 keyword feed above — the Nigam Shah
new-articles feed carried it a day early.** Consolidate; no further
action beyond that HIGH entry.

#### MEDIUM — Higgins DM, Blackden C, Brown M, Diaz C, Duffy L, et al. *The Gabriella Miller Kids First Data Resource for genomic research in pediatric cancer and congenital anomalies.* The American Journal of Human Genetics 2026 (Kai Wang citations feed).

**Resource paper for the Gabriella Miller Kids First (GMKF) data
resource** — pediatric cancer + congenital anomalies genomic cohort.
Adjacent to the rare-disease-cohort thread; GMKF is one of the reference
pediatric-genomic resources alongside PCGC and dbGaP. Bookmark for any
pediatric-rare-disease work.

#### MEDIUM — Gonzalez-Barbuzano S, Suarez-Pajes E, et al. *Genomic and integrative based progression biomarker discovery in adult sepsis: toward clinical stratification and precision medicine.* Annals of Intensive Care 2026 (Lisa Bastarache citations feed).

Sepsis genomic biomarker discovery paper (Bastarache lineage citation
because of PheWAS methods). Off the immediate CF / CHIP / pharmacoepi
watchlist.

#### LOW — Gillani SA, Baig MSA. *Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice.* arXiv 2026 (Szolovits citations feed).

LLM algorithmic-audit paper; off primary threads.

#### LOW — Dhanda S, Morris DE, Morton K, Elmet M, et al. *Enhanced passive safety surveillance (EPSS) of a seasonal intranasal influenza vaccine (Fluenz Tetra) in children in England.* 2026 (Patrick Ryan new-related feed).

Vaccine passive-safety-surveillance paper. Adjacent to pharmacoepi
thread but off the drug-class watchlist.

#### LOW — Abdellatif D, Obeid M, Aqeilan RI. *Modeling and targeting haploinsufficiency in SHINE syndrome.* bioRxiv 2026 (Karczewski citations feed).

Ultra-rare syndrome mechanism paper. Off primary threads.

#### LOW — Mora P, Aroda VR, Asong M, et al. *Efficacy and safety of once-daily oral zenagamtide, a novel unimolecular GLP-1 and amylin receptor agonist, in adults with type 2 diabetes.* 2026 (Patrick Ryan new-related feed).

**Zenagamtide RCT (dual GLP-1 + amylin agonist).** Off methods threads
but *directly on the GLP-1 pharmacoepi drug-class watchlist* — worth a
flag for the GLP-1-generation-2 watch (co-agonists / tri-agonists / oral
formulations). Not a HIGH because it's a phase-2/3 RCT rather than a
real-world evidence study, but the drug-class relevance means it should
be watched for a subsequent AoU / MVP real-world-outcomes follow-up.

#### LOW — Trotta G, Austin-Zimmerman I, Spinazzola E, Sideli L, et al. *Integrating biological pathway polygenic scores and trauma in psychosis: findings from the EU-GEI study.* Translational Psychiatry 2026 (Jian Yang new-related feed).

Pathway-PGS × trauma × psychosis in EU-GEI. Adjacent to the PGS ×
environment thread but off-cohort. Bookmark for reference if extending
into pathway-PGS work.

#### LOW — LLM RL / diffusion-LM papers (Farajidizaji & Raina; Dang et al.; Lu et al. — Szolovits and Zitnik feeds).

Generic small-LM / diffusion-LM RL papers. Off the clinical-agent
thread.

#### LOW — Kids First (already reported MEDIUM); scEPS medRxiv (already MEDIUM); other citation echoes.

Filed as noted above.

---

## What's NOT in the report

- **GitHub `arxiv-digest` cron / PR notifications** — none surfaced in
  Gmail search (`from:notifications@github.com` × `arxiv-digest`); the
  local repo commits and the on-disk `digests/` directory serve as the
  digest artifact.
- **NCBI My-NCBI What's-New batches** (AoU / UKB / drug repurposing) —
  none fired in the searched window.
- **bioRxiv / medRxiv Subject Collection Alerts** — 08-21 00:01Z bioRxiv
  and 00:05Z medRxiv collection alerts fired but on-thread content
  crossing HIGH threshold surfaced via the Scholar alerts already.
- **arxiv.org daily category mailings** (`no-reply@arxiv.org`) — the raw
  upstream feed that supplies the `arxiv-digest` pipeline; papers
  surfaced via the digest are covered in the arxiv-digest section above.
- **Substack / newsletters** — Michael Burry Trading Post firing on
  08-21 was noise; no biomedical newsletters crossed the on-thread
  threshold.

## Next steps to consider

1. **Read Ellershaw et al. Foresight-England arXiv 2608.16273 full
   text.** Highest-signal single item this window and the largest EHR-FM
   substrate published to date. Pairs naturally with the CLMBR / MOTOR /
   EHRSHOT / MEDS lineage for a national-scale-EHR-FM commentary. Check
   whether trained weights or inference API are available for external
   replication.
2. **Read Kosgolla & Smith AoU PGS × recovery-capital paper** for the
   PGS × environment × EHR-observed longitudinal outcome pattern; this
   is the natural template to lift for the CFTR-modulator × environment
   or GLP-1 RA × environment analyses.
3. **Cite Kullo, Horowitz, Bastarache, Berkman return-of-secondary-
   findings recommendations** as the policy anchor in any BRCA / CFTR /
   secondary-findings return-of-results methods paragraph. Read for the
   AoU-specific workflow specification, which was under-specified in
   prior anchors.
4. **Adopt the Meyre et al. TWIST 94-gene CHIP panel design** as a
   template for AoU / UKB WGS-derived CHIP-VAF re-analyses. Extract the
   gene list and coverage-depth targets. Pairs with Bandreddi et al.
   Tobit-vs-hurdle modeling choice (prior report) for a complete
   "panel + longitudinal-model" CHIP protocol.
5. **Read the five rare-disease-LLM papers together as one cluster**
   (Schächter synthetic-clinical-experts + Jiang selective-prediction +
   Nguyen PIHF + Zhong RareDASH + Batson test-accuracy-designs).
   Collectively they define the operating-point-and-evaluation frontier
   for LLM-based rare-disease diagnosis this quarter. Draft a one-page
   comparison table (backbone LLM, benchmark, Recall@k, abstain
   mechanism, deployment evaluation) — natural input for the
   PhenoGPT2 / GraphRareBench comparison shortlist.
6. **Cite Manzanilla et al. CCW systematic review** in the pharmacoepi
   methods paragraph, replacing older CCW references. Pair with Wood et
   al. perinatal-TTE (prior report) as the two 2026 canonical citations
   for CCW and perinatal-TTE respectively.
7. **Cite Sheng, Shah et al. NEJM AI safety-risks taxonomy** as the
   framing paper for any clinical-agent deployment discussion (RareDASH,
   PIHF, egg-computation, oci-agent).
8. **Bookmark Li et al. federated-LLM parameter-efficient framework** as
   the second federated-EHR-analytics anchor alongside Jang et al.
   arXiv 2607.17958. Watch for a real-EHR clinical-task validation
   follow-up.
9. **Track the zenagamtide (dual GLP-1 + amylin) RCT** for a subsequent
   AoU / MVP real-world-outcomes follow-up; the GLP-1-generation-2 watch
   should now include co-agonists explicitly.

_Report generated 2026-08-21 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-21 → next scheduled run._
