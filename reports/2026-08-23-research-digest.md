# Research digest report — 2026-08-23

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease
threads, EHR foundation models, KGs/ontologies, drug repurposing, rare
disease, ML for precision health, multimorbidity, knowledge
representation in EHRs).

Window: **2026-08-17 12:40Z → 2026-08-23 11:35Z** (~6 days since the
last research-digest report, covering five arxiv-digest cron runs plus
four Google Scholar alert batches on 08-19, 08-20/21, 08-22, and 08-23,
and NCBI My-NCBI "what's new" batches on 08-17, 08-18, 08-19, 08-20,
08-21, and 08-22).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-18.md` → `2026-08-23.md`) | 08-18 → 08-23 daily crons | 5 daily runs (08-19 skipped). 08-18: 4 papers (largest batch — Bayesian epidemic alignment for seasonal ID interventions; causal mediation for zero-inflated longitudinal data w/ non-compliance; N-of-1 digital-health primer; regression-not-to-the-mean w/ heterogeneous TE). 08-20: 3 new + 1 suppressed (Monroe molecular FM; Peru mayoral-experience panel-DML; urban rail transit panel-DML — all off-thread but methods-note-worthy). 08-21: 0 (3 suppressed). 08-22: 0 (1 suppressed). 08-23: 0. |
| Google Scholar alerts — keyword feeds (08-19, 08-21, 08-22, 08-23 batches) | 08-19 21:10Z → 08-23 11:35Z | ~9 keyword feeds fire each batch (`electronic health records`, `Foundation models + electronic health records`, `UK Biobank`, `All of Us research program`, `variant interpretation`/`variant classification`, `knowledge graph`, `drug repurposing`, `rare diseases`, `mendelian diseases`, `autoimmune disorders/diseases`, `intitle:"clonal hematopoiesis"`). Densest single-item signal was the Ellershaw et al. Foresight-England EHR-FM paper (dual hit on `electronic health records` + `Foundation models + electronic health records`). |
| Google Scholar alerts — author / citation feeds (08-20, 08-22, 08-23 batches) | 08-20 21:23Z → 08-23 05:19Z | 30+ author / citation feeds across the batches: Chenjie Zeng (self, ×2), Lisa Bastarache (×3: new-articles + new-related + citations-to), Joshua C. Denny (×3), Konrad Karczewski (×3), Kai Wang (×3), Jian Yang (×3), George Hripcsak (×3), Stephen B Montgomery (×2), Peter Szolovits (×2), Pascal Brandt (×2), Patrick Ryan (×2), Tiffany J Callahan (×2), Marinka Zitnik, Zhiyong Lu (×2), Vivek Natarajan, Yuan Luo, Daniel Kastner, Jonathan K Pritchard, Miguel Hernán, Nigam Shah, Bing Ren, Neil M Davies, Leo Anthony Celi, Russ B Altman, Xingyi Guo, Yu Akagi. |
| NCBI My-NCBI "what's new" batches (08-17 → 08-22, daily at ~13Z) | 08-17 → 08-22 daily | Six daily runs each firing three saved searches (`All of Us`, `UK Biobank`, `drug repurposing`) against PubMed. Deltas were small (<10 hits per batch on 08-19 and 08-22, essentially quiet on 08-17). Overlap with Scholar's `All of Us` and `UK Biobank` keyword feeds is high; the incremental value is PubMed-indexed items missed by Scholar. |
| medRxiv / bioRxiv Subject Collection Alerts (08-23) | 08-23 00:01Z + 00:05Z | Two batches (bioRxiv: Bioinformatics/Genetics/Genomics/Pathology; medRxiv: Epidemiology/Genetic and Genomic Medicine/Nephrology/Obstetrics). Metadata-only summaries; items overlapping with Scholar are folded into the Scholar reports below. |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:action@github.com` and `arxiv-digest` returned zero threads. As in the 08-17 report: the local repo commits are the digest artifact; there is no email notification channel. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fourteen HIGH items surfaced this window, clustering into five knots:

**EHR foundation models cluster (2 items — top-of-window signal).**
Ellershaw et al. arXiv 2608.16273 — **Foresight-England**: a
243M-parameter generative foundation model trained *de novo* on
longitudinal EHRs from **54.9 million patients**, entirely within the
NHS England Secure Data Environment, for medical-event prediction
across the COVID-19 pandemic. This is the largest-scale EHR-FM
disclosure of the summer and the clearest published EHR-FM
counterpart to CLMBR / MOTOR / MEDS, distinguished by (a) the
population-registry scale, (b) native training inside a national
Secure Data Environment (a compliance template for AoU / MVP work),
and (c) the explicit pre-/post-COVID temporal split as a
distribution-shift stress test. Fires the **`EHR foundation models`**
thread (INTERESTS.md line ~114) and is a direct comparator for the
CLMBR / MOTOR / EHRSHOT lineage. Palacios et al. arXiv 2608.17051 —
**institution-specific LLM prompting recovers PHI that de-identification
systems and their gold standards both miss**. Complementary
adversarial angle to the FM buildout: if the training corpus's own
de-id gold standard leaks PHI under institution-specific prompts, then
CLMBR / MEDS-style benchmark contamination audits (INTERESTS.md line
~121, scContam / MIA-scFM rising sub-thread) need to include a
prompt-mediated-PHI-leakage layer, not just membership inference.

**AoU / biobank cluster (5 items).** Kullo, Horowitz, Bastarache,
Berkman et al. **Recommendations for return of secondary genomic
findings in observational cohort studies** (in press; Bastarache
new-articles + Hripcsak citations-to dual hit) — workshop-derived
consensus recommendations grounded in MyCode, AoU, and NIDDK cohort
programs. This is the reference framing document for **the operational
side of monogenic risk in AoU / BioVU** (INTERESTS.md line ~24:
penetrance estimation for monogenic variants under population-screening
conditions vs. clinically ascertained cohorts) and belongs in the
citation pack whenever the CFTR / APOL1 threads touch returnable-findings
policy. Zhou, Yolou, Xie, Zhao *STAR Protocols* 2026 — **protocol for
leveraging local ancestry and cross-ancestry genetic architecture to
improve polygenic prediction in admixed populations from AoU**.
Triple-feed hit (Zeng new-related + Denny new-related + Jian Yang
new-related) means it's genuinely on the ancestry-aware-PGS-in-AoU
methods spine. Directly serves the **PGS-tails / ancestry-portability**
sub-thread (INTERESTS.md line ~74). Cheng, Butler-Laporte, Nakanishi,
Lu *Genetics in Medicine* 2026 — **simple clinical score to prioritize
detection of severe alpha-1 antitrypsin deficiency (PiZZ) in AoU**.
Exactly the "clinical-features-first, then genotype-confirm" workflow
that the **penetrance-under-screening thread** wants — the phenotype
side of the same problem the Kullo et al. recommendations paper
addresses on the ethical / return-of-results side. Pairs with any
CFTR / APOL1 penetrance work as a template. Kosgolla, Smith
*Addiction* 2026 — **joint associations of recovery capital and
polygenic risk with EHR-observed remission and relapse in substance
use disorder: longitudinal AoU evidence**. Directly serves the
**PGS × exposure / environment interactions** rising sub-thread
(recovery capital is the environmental modifier, PGS the genetic
substrate) on an EHR-linked longitudinal outcome (remission /
relapse). Portable template for future GLP-1-RA persistence,
HRT persistence, CFTR-modulator persistence × PGS work. Yee, Oakes,
Santacroce, Feldman et al. *Seminars in Arthritis* 2026 — **e-cigarette
use and risk of incident rheumatoid arthritis and systemic lupus
erythematosus in AoU**. Autoimmune-onset ascertainment from EHR-linked
exposures in AoU; adjacent to the multimorbidity / autoimmune thread.
Worth reading for the exposure-ascertainment approach (vape-use survey
signal → phecode-anchored incident autoimmune outcome).

**Rare-variant / composite-risk cluster (3 items).** Ao, Kolifarhood,
Parisien, Bortsov, Grant et al. *Genome Medicine* 2026 (Montgomery +
Jian Yang dual hit) — **exome-wide association study of chronic pain
in 327,642 UK Biobank participants**, jointly reporting common and
rare coding variants. Direct hit on the **composite-risk / rare + common
integration** sub-thread (INTERESTS.md line ~76). Read for how they
handle the exome-scale multiple-testing burden, whether they cite the
Baya "PGS residuals" framing, and whether the phenotype definition is
robust to the notorious chronic-pain outcome heterogeneity. Suger,
Harrison, Zhang, Wu, Darst et al. *Human Genetics and Genomics
Advances* 2026 (Karczewski citations-to feed) — **the pleiotropic
landscape of rare variant associations with multiple cancers in large
biobanks**. Exactly the design your composite-risk / pleiotropy thread
wants: rare-variant burden × multiple cancer outcomes, biobank-scale.
Belongs on the reading list alongside Backman *Nature* 2021 (UKB
exome pheWAS) and any AoU rare-variant PheWAS output that emerges.
Peng, Jackson, Alpen, Ye, Southey, Li *medRxiv* 2026 (Zeng self-cite
feed) — **genetic susceptibility and causes for early-onset breast
cancer from genome-wide and phenome-wide analyses**. On-topic
self-relevant (early-onset breast cancer is squarely inside Zeng's
published cancer-epi lineage). Read full-text for: (1) the phecode /
outcome definition of "early-onset", (2) whether the phenome-wide
component uses UKB, MoBa, or a Southey-network cohort, (3) whether
common + rare variant components are integrated in a composite-risk
frame or reported separately.

**Pharmacoepi / EHR-model-portability cluster (2 items).** Launders,
Richards-Belle et al. 2026 (Pascal Brandt new-related feed) — **impact
of adjunctive dihydropyridine calcium-channel blockers on mental-health
outcomes in people with severe mental illness: a target-trial emulation
in English EHR**. Direct hit on the **causal inference &
pharmacoepi** thread with a repurposing / off-label angle
(CCBs → psychiatric outcomes). Reference paper for the drug-class
watchlist's argument that TTE-on-EHR can reach non-obvious
repurposing candidates. Walsh, Ripperger, McCoy, Castro, Hu et al.
*npj Digital Medicine* 2026 (Pascal Brandt new-related feed) —
**evaluating transportability failures of EHR-based risk models for
treatment-resistant depression**. This is the empirical companion to
the **`Fidelity, portability, and audit of representations`**
sub-topic (INTERESTS.md line ~168). Direct hit on the "does the risk
model still work at a different site?" question that all AoU / BioVU /
MIMIC-based prediction models need to answer. Should sit alongside
Roine et al. HF-diagnosis-heterogeneity (08-17 report) as the two
portability-audit anchors of the last two windows.

**CHIP / somatic mosaicism + variant-interpretation cluster (2 items).**
Meyre, Ahn, Ehlert, Dederichs et al. *Circulation* 2026 — **association
of clonal hematopoiesis with silent brain lesions and cognitive decline
in patients with atrial fibrillation**, custom TWIST-based CHIP
ascertainment. Direct hit on the **CHIP / VEXAS / LOY somatic-mosaicism**
thread (INTERESTS.md line ~103) with a *neurocognitive-outcomes* twist
that extends the cardiovascular-outcomes lineage; useful reference for
future AoU / UKB WGS-based CHIP × cognition analyses. Pairs with the
08-17 Bandreddi Tobit-vs-hurdle modeling paper as the *phenotype* +
*model-family* pair for a CHIP-outcomes methods essay. Yang, Zou, Pu,
Li, Hu, Wang, Liu et al. *bioRxiv* 2026 (Karczewski new-related feed)
— **context-dependent variant interpretation from Mendelian disease to
genetic predisposition: a proof-of-concept using LPL**. Direct hit on
the **ACMG / ClinGen variant curation** thread — same *"gene has two
disease modes"* problem that CFTR, TTR, and RET all have. LPL is a
particularly clean example because the Mendelian phenotype
(chylomicronemia) and the population-genetic phenotype (dyslipidemia
risk) share the same gene but need entirely different curation
frameworks. Read for the proposed context-annotation extension to
ACMG/AMP.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / LOW / SKIP),
citation, one-paragraph analytic summary tied to `INTERESTS.md`
threads. Sorted within source, then by bucket.

### arxiv-digest surfacings (2026-08-18 → 2026-08-23)

#### METHODS-WATCH — Moriña D. *Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions.* arXiv 2608.16537v1 (stat.ME, 2026-08-17). Score 1.

Bayesian causal count model that makes epidemic alignment a *model
component* (season-specific affine maps from calendar time to a latent
epidemic clock) rather than a preprocessing step, so uncertainty about
epidemic timing propagates into every causal contrast. Negative-binomial
observation model, hierarchical area/season effects, shrunk Fourier
epidemic curve, continuous programme-intensity exposure; posterior
g-computation yields prevented cases, prevented fractions, peak
attenuation, epidemic displacement. Applied to Catalan primary-care
surveillance + RSV immunisation. **Bookmark for any future respiratory-
pathogen intervention TTE on EHR-linked biobank data** — the
epidemic-clock alignment idea is portable to flu / COVID / RSV
vaccination pharmacoepi in AoU / MVP where the seasonal timing itself
is a nuisance parameter.

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. *Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.* arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1.

Bayesian causal-mediation framework built on **enriched Dirichlet
process mixture models** with a **scalable G-computation** estimator,
designed for zero-inflated longitudinal mediators / outcomes plus
non-compliance and multiple mediators. Motivating application is a
marketing-email study, but every listed complication — non-compliance
(patients who don't take the drug), longitudinal zero-inflated
mediators (biomarkers with detection floors), multi-mediator paths — is
a *direct match* for EHR pharmacoepi mediation analyses. Pair with the
Bandreddi Tobit-vs-hurdle result (08-17 report) as complementary tools
for the zero-inflated-longitudinal biomarker family; useful for CFTR-
modulator persistence × sputum-culture mediation, GLP-1 RA × HbA1c
mediation, HRT × lipid-panel mediation.

#### METHODS-WATCH — Daza EJ. *A Primer on Digital Health N-of-1 Studies and Single-Case Designs.* arXiv 2608.15526v1 (stat.AP, 2026-08-16). Score 1.

Review chapter on **n-of-1 studies, single-case designs, and other
"multitudinal" digital-health approaches**. Coins/promotes "esametry"
(statistics of the digitized multitudes within one person) as a
frame. Off your active methods threads (all group-level PheWAS /
biobank work), but worth a **future re-visit if any AoU / UKB
digital-health / Fitbit sub-cohort work turns into a single-participant
trajectory analysis** — the framework it maps out (per-person recurring
patterns first, subgrouping second) is the natural methodological
substrate for that turn.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. *Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.* arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1.

Constant-treatment-effect models in **longitudinal settings with
staggered treatment and heterogeneous treatment effects** can produce
weighted averages with **negative weights** across treatment-duration
buckets, so the constant-effect estimate can be smaller in magnitude
or opposite in sign to essentially every duration-specific estimate.
Illustrated with drug-induced-homicide prosecutions → overdose deaths;
shows the negative-weight issue **also arises in logistic regression**,
not just linear. **Directly relevant to any staggered pharmacoepi TTE
where a single scalar "average treatment effect" is being reported
across a wide follow-up window** — CFTR modulator initiation
(pediatric vs. adult), HRT initiation timing (perimenopause vs. late-
menopause), SGLT2i initiation vs. baseline CKD stage. Reference paper
whenever a reviewer asks "why does your constant-effect estimate
conflict with your subgroup / duration estimates?"

#### METHODS-WATCH — Banaszewski B, Fitzgibbon AW. *Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference.* arXiv 2608.18982v1 (cs.LG, 2026-08-19). Score 1.

Molecular foundation model with **prior-data-fitted-network
(TabPFN)-based in-context downstream prediction**, trained on 81M
molecules from PM6 quantum-chemistry data. Beats existing MFMs on
Polaris + activity-cliff benchmarks and delivers PFN-based MiniMol /
CheMeleon variants. Off your **clinical-EHR** and **PheWAS** threads,
but the **PFN-as-downstream-head recipe** is portable to *any*
foundation-model + tabular-clinical-downstream stack (e.g., CLMBR
embeddings + PFN head for an AoU disease-onset outcome). Bookmark as
an architectural pattern.

#### SKIP — Machacuay C, Lincovil J, Rojas H. *Mayoral Experience or Municipal Capacity? Negative-Outcome Evidence on Municipal Budget Execution in Peru.* arXiv 2608.18354v1 (stat.AP, 2026-08-18). Score 1.

Off-topic (Peruvian municipal-governance panel DML). The
**negative-outcome-control × first-differences panel design** is
pedagogically clean and portable — if any future EHR pharmacoepi paper
needs a negative-control-outcome sanity check on a panel design, this
is the reference implementation to cite. Otherwise SKIP.

#### SKIP — Yao Y, Zhang N, Graham DJ. *Quantifying the Causal Operational Determinants of Service Reliability in Urban Rail Transit: Evidence from Panel Double/Debiased Machine Learning.* arXiv 2608.17901v1 (stat.AP, 2026-08-18). Score 1.

Off-topic (metro-reliability DML on 46 operators × 30 years). Same
comment as above: the panel-DML recipe is portable, the application is
not.

### Scholar alerts — keyword feeds (08-19 → 08-23 batches)

#### HIGH — Ellershaw S, Tomlinson C, Kraljevic Z, Denaxas S, et al. *Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic.* arXiv 2608.16273 2026 (`electronic health records` + `Foundation models + electronic health records` + Patrick Ryan new-related feeds, triple hit).

**Foresight-E is a 243M-parameter generative foundation model trained
de novo on longitudinal EHRs from 54.9 million patients, entirely
within the NHS England Secure Data Environment**, framed as a research
resource for medical-event prediction spanning the COVID-19 pandemic.
Direct hit on `EHR foundation models` (INTERESTS.md line ~114) — this
is the summer's largest-scale EHR-FM disclosure and the clearest
population-registry counterpart to CLMBR / MOTOR / MEDS. Read
full-text for: (1) tokenization scheme and how it compares to MEDS
event schemas, (2) how the pre-/post-COVID temporal split is used as
a distribution-shift stress test (this is a **built-in
pretraining-contamination audit substrate** — pandemic-era events
that could not have been seen at pretraining time serve as a natural
held-out generation task), (3) how prediction is validated (is there
a chart-review or PheValuator-style anchor for the predicted events?),
(4) whether they release any embeddings / adapters / benchmarks
outside the NHS SDE. Also read for the *national Secure Data
Environment* pattern as a compliance template for AoU / MVP EHR-FM
work — the on-premises-training constraint is the same.

#### HIGH — Palacios D, Neeley MB, Otto AA, Dhamodharan S, et al. *Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss.* arXiv 2608.17051 2026 (`Foundation models + electronic health records` keyword feed).

Complementary adversarial angle to Foresight-E: **institution-specific
LLM prompts recover PHI that existing de-identification systems
*and their gold standards* both miss**. If the training corpus's own
de-id gold standard leaks PHI under prompt manipulation, then CLMBR /
MEDS / Foresight-E-style benchmark contamination audits (INTERESTS.md
line ~121 rising sub-thread on scContam / MIA-scFM membership-
inference) need to include a **prompt-mediated-PHI-leakage layer**,
not just membership inference. Read for: (1) the specific institution
signals the prompts exploit, (2) whether their recovery rate scales
with FM parameter count, (3) mitigation recommendations that could
retrofit into existing NHS-SDE / AoU-Workbench de-id pipelines.

#### HIGH — Cheng Y, Butler-Laporte G, Nakanishi T, Lu T. *Development of a simple clinical score to prioritize detection of severe alpha-1 antitrypsin deficiency with PiZZ genotype.* Genetics in Medicine 2026 (`All of Us research program` keyword feed).

**Clinical-features-first score to prioritize genotype testing for
severe A1AT deficiency (PiZZ)** in AoU. This is exactly the
"phenotype-first, then genotype-confirm" workflow the
**penetrance-under-screening** thread (INTERESTS.md line ~24) wants
to see — pair it with the Kullo, Bastarache et al. return-of-results
recommendations paper for the ethical bookend, and with any future
CFTR / APOL1 penetrance-in-AoU work as a template. Read for: (1) the
score's features (spirometry, liver enzymes, family history — how
much EHR-only signal is needed?), (2) sensitivity/specificity at the
recommended cutpoint, (3) transportability to UKB / MVP (implicit in
AoU-derived scores).

#### HIGH — Yee J, Oakes EG, Santacroce L, Feldman CH et al. *Electronic Cigarette Use and Risk of Incident Rheumatoid Arthritis and Systemic Lupus Erythematosus in the All of Us Research Program.* Seminars in Arthritis and Rheumatism 2026 (`All of Us research program` keyword feed).

**AoU incident RA / SLE ~ e-cigarette use.** Autoimmune-onset from
EHR-linked exposure signals in AoU; adjacent to the multimorbidity /
autoimmune thread (and the CHIP / VEXAS / LOY somatic-mosaicism
thread's autoimmune borderland). Read for: (1) how they defined
"e-cigarette use" from AoU surveys (ever / current / dual-use with
tobacco), (2) the incident-RA / SLE phecode definitions and whether
they used the ≥2-occurrence rule and exclusion ranges, (3) covariate
adjustment strategy for smoking-e-cigarette confounding. Portable
template for other autoimmune-vaping analyses on AoU.

#### HIGH — Kosgolla JV, Smith DC. *Joint associations of recovery capital and polygenic risk with electronic health record observed remission and relapse in substance use disorder: Longitudinal evidence from the All of Us research program.* Addiction 2026 (`All of Us research program` keyword feed).

**AoU longitudinal SUD remission/relapse as a function of recovery
capital × PGS.** Direct hit on the **PGS × exposure / environment
interactions** rising sub-thread (Nagpal & Gibson lineage, applied to
an EHR-linked longitudinal outcome). Recovery capital is the
environmental modifier; PGS is the genetic substrate; SUD remission
and relapse are EHR-derivable outcomes. Portable template for future
**GLP-1-RA persistence × PGS**, **HRT persistence × PGS**, and
**CFTR-modulator persistence × PGS** work — the same modifier-on-PGS
frame applies. Read for: (1) which SUD phecodes anchor remission
vs. relapse, (2) PGS construction (which discovery GWAS, ancestry
handling), (3) how "recovery capital" is operationalized from AoU
surveys.

#### HIGH — Meyre PB, Ahn HJ, Ehlert CA, Dederichs TS et al. *Association of Clonal Hematopoiesis With Silent Brain Lesions and Cognitive Decline in Patients With Atrial Fibrillation.* Circulation 2026 (`intitle:"clonal hematopoiesis"` keyword feed).

**CHIP × silent-brain-lesion + cognitive-decline** ascertainment in
AFib patients using a custom TWIST-based CHIP panel. Direct hit on
the **CHIP / VEXAS / LOY somatic-mosaicism** thread (INTERESTS.md
line ~103); the *neurocognitive-outcomes* twist extends the
cardiovascular-outcomes lineage (Loh 2018 → Kessler 2022 → Bick 2020
JACC). Read for: (1) CHIP-VAF thresholding and the modeling choice
for VAF distributions (this is where the Bandreddi Tobit-vs-hurdle
result from 08-17 becomes actionable), (2) whether cognitive decline
is standardized against a UDS-like battery vs. registry codes,
(3) the AFib enrichment argument (is the association CHIP → cognition
directly, or CHIP → embolism → cognition?). Belongs in the reading
pack alongside Meyre's earlier CHIP × stroke work.

#### HIGH — Schächter C, Pechmann A, Kirschner J, Hasenauer J et al. *Large language models as synthetic clinical experts to inform longitudinal rare-disease modeling.* arXiv 2026 (`rare diseases` keyword feed).

**LLMs used as synthetic clinical experts to inform longitudinal
rare-disease modeling**, motivated by the small-cohort / low-event-
density problem endemic to rare-disease natural-history work. Fires
the `Rare disease` thread and (adjacent) the rising sub-thread on
**pre-symptomatic phenoconversion prediction from longitudinal
biomarker trajectories** (INTERESTS.md line ~192; Ran / Benatar ALS
template). Read for: (1) how they operationalize "synthetic expert"
(elicited prior, in-context reasoning, prompted trajectory extension?),
(2) how they validate against real longitudinal cohorts (SMA cohort
is a possibility given the Pechmann co-authorship), (3) uncertainty
quantification for LLM-generated priors. If credible, this is a
**portable methods anchor** for the BRCA-incident-cancer,
APOL1-CKD-conversion, and hereditary-cancer-syndrome phenoconversion
sub-threads.

#### METHODS-WATCH — Halper-Stromberg E, Narayan S, Laufer V, Limson M et al. *Clinical Variant Interpretation with the Integrative Genomics Viewer (IGV) for Molecular Pathologists.* Journal of Visualized Experiments 2026 (`variant interpretation` / `variant classification` keyword feed).

JoVE video-methods paper on **using IGV as a clinical-variant-
interpretation adjunct in molecular-pathology workflows**. Pragmatic
craft paper for the ACMG / ClinGen thread — useful if the CF / BRCA /
cardiomyopathy variant-review workflow you're building needs an
explicit read-visualization step. Otherwise LOW.

#### METHODS-WATCH — Peng S, Jackson VE, Alpen K, Ye Z, Southey MC, Li S. *Genetic susceptibility and causes for early-onset breast cancer: insights from genome-wide and phenome-wide analyses.* medRxiv 2026 (Chenjie Zeng new-related feed).

**Genome-wide + phenome-wide analyses of early-onset breast cancer**
noting that >50% of aggressive early-onset cases remain unexplained
after rare pathogenic variants + >200 common variants. Directly
self-relevant (early-onset breast cancer is squarely inside Zeng's
published cancer-epi lineage). Read full-text for: (1) the phecode /
outcome definition of "early-onset" (age cut, first-primary handling),
(2) whether the phenome-wide component uses UKB, MoBa, or a Southey-
network cohort, (3) whether common + rare variant components are
integrated in a composite-risk / PGS-tails frame or reported
separately. Should feed directly into the composite-risk reading list
alongside Baya AJHG 2026 and Souaiaia Nature.

#### METHODS-WATCH — Foresight-E cluster continuation: Collins A, Desai M, Bennett L, Raman P, Lowe S et al. *Searching Patient Space: Language-Guided Cohort Discovery with Clinical Foundation Models.* [venue TBD] 2026 (`Foundation models + electronic health records` keyword feed).

Language-guided cohort-discovery layer on top of clinical FMs; explicit
citation of the "shaky foundations" critique implies a
FM-composition-without-subsumption stance. **Adjacent to Foresight-E**
and to the `EHR foundation models` cohort-discovery-application
sub-thread (INTERESTS.md line ~162). Bookmark as a natural downstream
application for CLMBR / Foresight-E embeddings; read only if the
cohort-discovery use case is active on the reading list.

#### METHODS-WATCH — Zhang H, Shi Y, Zhang S, Jian Z, Liang M, Zhang S et al. *Temporal graph transformer for next visit diagnosis prediction on electronic health records.* Scientific Reports 2026 (`electronic health records` keyword feed) — [already flagged in 08-17 report; re-appears as re-indexed].

Duplicate of a paper already flagged 08-17; comment there stands.

#### METHODS-WATCH — Wang Y, Miao X, Withers M et al. *Insights into the relationship between menopausal timing and risk of cardiovascular disease: a systematic review and meta-analysis of Mendelian randomization…* [venue TBD] 2026 (`mendelian diseases` keyword feed).

**Menopausal-timing → CVD MR meta-analysis.** Adjacent to the HRT
drug-class watchlist and to the **PGS × exposure interactions** thread
if menopausal timing is treated as a genetically-proxied environmental
exposure. Bookmark for HRT-initiation-timing pharmacoepi work; the
menopausal-timing IV is the natural instrument for HRT-initiation
studies where reverse causation is a concern.

#### METHODS-WATCH — Nigam A, Onongaya C, Meshram P, Frebault J et al. *Traditional Risk Factors Are Not Associated with the Rise of Early-Onset Colorectal Cancer: An All of Us Study.* Diseases of the Colon & Rectum 2026 (`All of Us research program` keyword feed).

**AoU-based descriptive analysis of early-onset CRC risk factors.**
Adjacent to the composite-risk cancer thread and the early-onset-
cancer parallel to the Peng et al. breast-cancer paper above. Read
only if the early-onset-cancer thread is actively being built.

#### METHODS-WATCH — Pham K, Madakkatel I, Mulugeta A, Lumsden A, Hill C et al. *Data-Driven Discovery of Candidate Predictors of Future Rheumatoid Arthritis Diagnosis in the UK Biobank.* Seminars in Arthritis and Rheumatism 2026 (`UK Biobank` keyword feed).

**Data-driven UKB predictor discovery for incident RA.** Complements
the Yee AoU e-cigarette → RA/SLE paper above as the *unsupervised
feature-discovery* counterpart to the *targeted-exposure-hypothesis*
design. Read for the ML feature-selection pipeline (LASSO / boosted
trees / SHAP?) and whether they anchor against ACR-criteria-based RA
ascertainment.

#### LOW — Marino M, Jamieson E, Ezekiel-Herrera D et al. *Developing and validating predictive models of electronic health record tool adoption in the pre-implementation stage.* BMC Health Services Research 2026 (Zeng new-related feed).

Implementation-science predictive model for EHR-tool adoption. Off
your methods thread unless implementation-science is being added to
the active thread list.

#### LOW — Kullo IJ, Horowitz CR, Bastarache L, Berkman B et al. *Recommendations for return of secondary genomic findings in observational cohort studies.* (In press, 2026; Lisa Bastarache new-articles + George Hripcsak citations-to dual hit).

**[Already covered as HIGH under the AoU / biobank cluster above.]**
Re-listed here because the same paper fired *both* the Bastarache
new-articles feed and the Hripcsak citations-to feed on 08-20; the
dual-hit is signal of its relevance to your primary author network.

#### LOW — Xingyi Guo new-articles feed: Wu L, Wang J, Cai Q, Cavazos TB, [+]. [Truncated Channing Division / Brigham+Women's + Vanderbilt-affiliated cancer-epi paper] 2026.

Cancer-epidemiology paper from a Zeng-adjacent author network (Xingyi
Guo is a Vanderbilt EHR / cancer-genomics collaborator). Snippet is
too truncated to place cleanly; **worth clicking through the alert
to check** whether it's a breast / prostate / GI cancer TWAS-style
paper that would slot into the Zeng cancer-epi lineage.

### Scholar alerts — author / citation feeds (08-20 → 08-23 batches)

#### HIGH — Kullo IJ, Horowitz CR, Bastarache L, Berkman B et al. *Recommendations for return of secondary genomic findings in observational cohort studies.* [In press] 2026 (Lisa Bastarache new-articles + George Hripcsak citations-to dual hit).

Workshop-derived consensus recommendations from a workshop convened
around **Geisinger MyCode**, **All of Us**, and **NIDDK cohort
programs**. Directly serves the **AoU / BioVU monogenic-penetrance**
subthread (INTERESTS.md line ~24) on the *return-of-results* side.
Read full-text for: (1) exactly which variant categories they recommend
returning (ACMG SF v3.x list vs. an expanded set), (2) how they handle
the population-screening penetrance-vs-clinically-ascertained
penetrance gap (this is the *empirical* piece the recommendations
side has been waiting for), (3) whether they endorse a
PheValuator-style pre-return phenotype-confirmation step. Should sit
alongside the Cheng et al. A1AT AoU paper above as the return-of-
results + phenotype-first bookend, and become a citable framing
paper for any future CFTR / APOL1 / BRCA return-of-results discussion.

#### HIGH — Zhou G, Yolou I, Xie Y, Zhao H. *Protocol for leveraging local ancestry and cross-ancestry genetic architecture to improve polygenic prediction in admixed populations.* STAR Protocols 2026 (Chenjie Zeng new-related + Joshua C. Denny new-related + Jian Yang new-related, triple hit).

Protocol paper for **admixed-population PGS in AoU** using local
ancestry + cross-ancestry genetic architecture. The triple-feed hit
(Zeng self + Denny + Jian Yang) is a strong signal the paper sits on
the ancestry-aware-PGS-in-AoU methods spine. Directly serves the
**PGS ancestry-portability** sub-thread and the **Pangenome-informed
variant calling** / **cross-ancestry PGS-portability** rising
sub-thread (INTERESTS.md line ~86). Read for: (1) which local-ancestry
inference method they recommend (RFMix / Gnomix / a custom pipeline
for the AoU short-read WGS calls), (2) which cross-ancestry
prior-integration method (PRS-CSx / SDPRX / a novel one), (3) whether
they benchmark against Chen 2024 AoU PGS pipeline. Should become the
default reference protocol for any AoU admixed-population PGS work
downstream.

#### HIGH — Walsh CG, Ripperger M, McCoy TH Jr, Castro V, Hu Y et al. *Evaluating transportability failures of electronic health record-based risk models for treatment-resistant depression.* npj Digital Medicine 2026 (Pascal Brandt new-related feed).

**Empirical audit of transportability failures for EHR-based risk
models of treatment-resistant depression.** Direct hit on the
**`Fidelity, portability, and audit of representations`** sub-topic
(INTERESTS.md line ~168). Should sit alongside the Roine et al.
HF-diagnosis-heterogeneity paper from the 08-17 report as the two
portability-audit anchors of the last two windows. Read for: (1) how
they operationalize "transportability failure" (calibration drift?
recalibration-in-the-limit? domain-adaptation-required?), (2) the
site-pair(s) they audit across (BioVU vs. AoU vs. MGH vs. MIMIC?),
(3) whether they identify representation-choice drivers of failure —
this is the ablation study the sub-thread wants (representation
choice vs. model architecture as the driver of portability failure).

#### HIGH — Launders N, Richards-Belle A [+]. *Impact of adjunctive dihydropyridine calcium channel blockers on mental health outcomes in people with severe mental illness: A target trial emulation in English…* 2026 (Pascal Brandt new-related feed).

**Target-trial emulation in English EHR** for **adjunctive
dihydropyridine CCBs → mental-health outcomes in SMI**. Directly
serves the **causal inference & pharmacoepi** thread on a
*repurposing / off-label* CCB → psychiatric-outcomes hypothesis
(CCBs have long-standing candidate-repurposing status for bipolar
disorder). Read for: (1) the exact TTE design (new-user active
comparator? new-user historical comparator?), (2) how they handle
SMI baseline severity confounding (a notorious problem for SMI
pharmacoepi), (3) whether the effect estimate replicates known trial
signals for CCBs in bipolar disorder. Reference paper for the drug-
class watchlist's argument that TTE-on-EHR can reach non-obvious
repurposing candidates.

#### HIGH — Ao X, Kolifarhood G, Parisien M, Bortsov A, Grant AV et al. *Exome-wide association study reveals common and rare coding variants shaping chronic pain in 327642 UK biobank participants.* Genome Medicine 2026 (Stephen B Montgomery new-related + Jian Yang new-related, dual hit).

**Exome-wide association study of chronic pain in 327,642 UKB
participants**, jointly reporting **common and rare coding variants**.
Direct hit on the **composite-risk / rare + common integration**
sub-thread (INTERESTS.md line ~76). Chronic pain is a notoriously
heterogeneous phenotype so the phenotype-definition choice is
critical; the dual-feed hit (Montgomery + Jian Yang) signals the QC
is likely solid. Read for: (1) exome-scale multiple-testing burden
handling, (2) whether they cite the Baya 2026 AJHG "misaligned
individuals" / PGS-residuals framing, (3) which pain phecodes anchor
the discovery (self-report survey items vs. EHR opioid-prescription
signals), (4) whether the discovered rare-variant burden replicates
the AoU exome-WGS releases.

#### HIGH — Suger AH, Harrison TA, Zhang J, Wu MC, Darst BF et al. *The pleiotropic landscape of rare variant associations with multiple cancers in large biobanks.* Human Genetics and Genomics Advances 2026 (Konrad Karczewski citations-to feed).

**Pleiotropic rare-variant × multi-cancer landscape at biobank scale.**
Directly serves the **composite-risk / pleiotropy** thread and (via
the multi-cancer framing) the cross-cancer-shared-architecture
sub-thread. Belongs on the reading list alongside Backman *Nature*
2021 (UKB exome pheWAS) and any AoU rare-variant PheWAS output that
emerges. Read for: (1) which cancers they include (biobank-power-
limited to common tumors, or also rare ones?), (2) whether the
pleiotropic-signal reporting distinguishes primary from secondary
susceptibility genes (the CDKN2A / TP53 / BRCA class of "true
pleiotropy" vs. the incidental co-occurrence class), (3) whether
they audit for the Ji 2026 somatic-contamination confounder
(INTERESTS.md line ~110).

#### HIGH — Corfield EC, Shadrin AA, Frei O, Rahman Z [+]. *Family genetic designs in MoBa provide insights into health and functioning.* Nature 2026 (Konrad Karczewski new-related feed).

**Family-based genetic designs in the Norwegian Mother, Father and
Child Cohort (MoBa)** — a major Nature paper on family GWAS designs
that separate direct genetic effects from parental / assortative
effects. Direct hit on the **GWAS / genetic epi** thread and,
importantly, the **PGS × environment / exposure** thread from the
family-design angle (family designs recover *within-family* PGS
estimates that are robust to gene-environment correlation). Read for:
(1) the specific traits where within-family estimates differ most
from population estimates (portability implications for PGS built
from population GWAS), (2) whether they benchmark against Howe *Nat
Genet* 2022 or Kong *Science* 2018 direct/indirect decomposition
methods, (3) how their design translates to biobank cohorts without
trio structure (AoU, UKB, MVP mostly lack it).

#### HIGH — Yang Q, Zou WB, Pu N, Li Y, Hu Y, Wang YC, Liu X [+]. *Context-dependent variant interpretation from Mendelian disease to genetic predisposition: a proof-of-concept using LPL.* bioRxiv 2026 (Konrad Karczewski new-related feed).

**LPL as a proof-of-concept for context-dependent variant
interpretation** across the Mendelian-disease ↔ genetic-predisposition
boundary. Same "gene has two disease modes" problem CFTR, TTR, and
RET all have; LPL is a particularly clean example because the
Mendelian phenotype (chylomicronemia) and the population-genetic
phenotype (dyslipidemia risk) share the gene but need entirely
different curation frameworks. Direct hit on the **ACMG / ClinGen
variant curation** thread (INTERESTS.md line ~66). Read for the
proposed context-annotation extension to ACMG/AMP and its
extensibility to CFTR (Mendelian CF ↔ variable CBAVD ↔ population
lung-function risk).

#### METHODS-WATCH — Le NN, Padmanabhan S. *Cardiometabolic pathways linking genetically proxied educational attainment to cardiovascular disease: a Mendelian randomisation, mediation and colocalisation…* medRxiv 2026 (Lisa Bastarache new-related feed).

**MR + mediation + colocalisation for educational-attainment → CVD.**
Directly relevant to the **PGS × exposure interactions** thread —
educational attainment as a genetically-proxied exposure with
cardiometabolic mediation. Read if the socioeconomic-exposure MR
sub-thread is actively being built; otherwise LOW.

#### METHODS-WATCH — Chen S, Liang Y, Luo S, Zheng J, Yoshiji S, GM [+]. *Elucidating the proteomic pathways linking childhood body mass index with type 2 diabetes: a Mendelian randomization and recall-by-genotype study.* [venue TBD] 2026 (Jian Yang new-related feed).

**MR + recall-by-genotype for childhood BMI → T2D via proteomics.**
Directly serves the **Multi-omics-augmented PRS** rising sub-thread
(INTERESTS.md line ~82) on the exposure side. The **recall-by-
genotype** design is the specific reason to read this — it's the
gold standard for causal-inference-with-omics-mediators, and any
future GLP-1 / SGLT2 exposure work with proteomics could copy the
design template.

#### METHODS-WATCH — Surana P, Dutta P, Boffetta P, Davuluri R. *PGViS: Personal Genome Variant interpretation Score for lung cancer genomes.* bioRxiv 2026 (Konrad Karczewski new-related feed).

**Personal-genome variant-interpretation score for lung cancer**
integrating coding + inherited risk. Adjacent to the composite-risk
cancer thread; useful comparator for CanRisk / BOADICEA if the
CanRisk analog for lung cancer is being scoped.

#### METHODS-WATCH — Corponi F, Reami M, Ossola P, Fanelli G, Jauhar S [+]. *Damped Physical Activity and Unstable Sleep: Fitbit-Derived Rest-Activity Phenotypes in Inter-episode Mood Disorders.* medRxiv 2026 (Joshua C. Denny new-related feed).

**Fitbit-derived rest-activity phenotypes for inter-episode mood
disorders.** Adjacent to the **Digital twins from EHR data** rising
sub-thread (INTERESTS.md line ~117) on the *wearable-augmented
trajectory* side. Bookmark if the AoU Fitbit sub-cohort is on the
reading list; otherwise LOW.

#### METHODS-WATCH — Higgins DM, Blackden C, Brown M, Diaz C, Duffy L [+]. *The Gabriella Miller Kids First Data Resource for genomic research in pediatric cancer and congenital anomalies.* American Journal of Human Genetics 2026 (Joshua C. Denny + Kai Wang citations-to feeds, dual hit).

Data-resource paper for the **Gabriella Miller Kids First** cohort.
Off your active adult-EHR / adult-biobank threads but bookmark as a
substrate for **pediatric-rare-disease reanalysis** work (INTERESTS.md
line ~197: data-driven reanalysis of unsolved cases at 10k+ cohort
scale — Uria-Regojo et al. is the mid-scale reference).

#### METHODS-WATCH — Kim S, Ji S, Koo B, Jin X, Oh B et al. *Joint Global-Local Representations via Relation-Entity Pair Encoding for Hyper-Relational Knowledge Graphs.* Proceedings of the 32nd ACM SIGKDD 2026 (Tiffany J Callahan new-related feed).

Hyper-relational KG representation-learning paper. Off-thread as a
KG-methodology piece unless a downstream biomedical-KG application is
being written up; the **relation-entity pair encoding** is a
generalization worth citing if a biomedical KG paper needs a hyper-
relational baseline.

#### METHODS-WATCH — Bai C, Wu L, Yang J, Wu Y, Xia Z, Zhang Y, Bo X, He S. *Knowledge graph-based screening for synergistic anticancer drug combinations.* Journal of Pharmaceutical Analysis 2026 (Tiffany J Callahan new-related feed).

**KG-based screening for synergistic anticancer drug combinations.**
Direct hit on the **drug repurposing** thread (INTERESTS.md line ~183
— the *explainable-hypothesis-output KG/GNN sub-thread*). Read for
whether the output is a **path- or subgraph-level rationale** (this
is the design property the thread prioritizes over opaque link-
prediction scores).

#### METHODS-WATCH — Andrews SJ. *What my mother's APOE result taught me about dementia risk.* npj Dementia 2026 (George Hripcsak citations-to feed).

**Reflective essay on the personal side of APOE risk disclosure.**
Off your primary methods thread but a useful lay-facing citation for
the return-of-results discussion paired with the Kullo et al.
recommendations paper above.

#### METHODS-WATCH — Kevopoulos et al. (CAN-FLOW), Bandreddi et al. (Tobit-vs-hurdle), Vossler et al. (egg-computation), Wood et al. (perinatal TTE), Reho et al. (Pharmacoexposomics), Mitev (variant-classification framework), Chang et al. (transformer epilepsy phenotyping), Angell et al. (verified-diagnosis autism), Abner et al. (diurnal glucose GWAS), Pérez-García et al. (HPO-driven literature retrieval).

**Already flagged HIGH in the 08-17 report; all remain on the standing
reading list.** No new commentary in this window.

#### LOW — Guo F, Nayar G, Pribus SJ, Altman RB. *Interpreting Protein Language Models: high attention sites predict functional regions.* bioRxiv 2026 (Russ B Altman new-articles feed).

Protein-LM interpretability; off your active clinical / EHR / PheWAS
threads unless a proteomics-x-clinical outcome analysis is scoped.

#### LOW — Rajesh A, Havas AP, Arnold R, Lande K, Lei X, Li KY et al. *Inhibiting cyclin D1–CDK6 suppresses senescence-associated inflammatory gene expression and age-related functional decline.* Nature Aging 2026 (Bing Ren new-articles feed).

Basic-science aging paper; off clinical thread.

#### LOW — Beitzen-Heineke A, Siskin M, Muller M, Bhatt A [+]. *Divergent effects of GnRH agonist and GnRH antagonist treatment on platelet activity and transcriptome.* Cardio Oncology 2026 (Chenjie Zeng new-related feed).

Cardio-oncology bench + clinical study on GnRH class differences.
Self-relevant to the prostate-cancer subthread (Zeng lineage) but
mechanistic rather than epidemiological; read only if the mHSPC /
CRPC + cardiovascular safety commentary is reactivated.

#### LOW — Yeap BB, Hui J, Robledo KP, Arscott G, Grossmann M [+]. *Effect of Testosterone Treatment on Leucocyte Telomere Length in Men: Results From a Randomised Placebo‐Controlled Trial.* Andrology 2026 (Chenjie Zeng new-related feed).

RCT of testosterone on leucocyte telomere length. Self-relevant only
if the male-hormone-therapy × longevity subthread is added; otherwise
LOW.

#### LOW — Privé BM, Oprea-Lager DE, Muselaers CHJ [+]. *Lutetium-177-PSMA-617 in Oligo-metastatic Hormone-sensitive Prostate Cancer (BULLSEYE): A Trial Update.* European Urology Focus 2026 (Chenjie Zeng new-related feed).

BULLSEYE trial update in oligomets HSPC. Off your active methods
threads; relevant only if the prostate-cancer clinical subthread is
reactivated.

#### LOW — Marino M, Jamieson E, Ezekiel-Herrera D et al. *Developing and validating predictive models of electronic health record tool adoption in the pre-implementation stage.* BMC Health Services Research 2026 (Zeng new-related feed).

Implementation-science; off-thread.

#### LOW — Ginzberg SP, Weller JHD, Skefos CM, Perrier ND. *Genetic endocrine tumors focusing on the thyroid.* Best Practice & Research Clinical Endocrinology & Metabolism 2026 (`All of Us research program` keyword feed).

Endocrine-tumor review that cites the AoU + UKB RET-penetrance
landmark (n = 245,394 AoU + 469,558 UKB, RET PV prevalence 1-in-many).
Good citation for the AoU-monogenic-penetrance-in-population thread if
the RET / MEN2 clinical arm is on the reading list; otherwise LOW.

#### LOW — Various keyword-feed hits: *Diagnostic delay in rare disease Sweden* (Soller); *Genetic research on cardiac channelopathies in African-descent populations* (Taib); *Structure-aware generative KG reasoning* (Jiang); *FOXP3 as therapeutic target in autoimmune diseases* (Bhat); *Puberty timing and survival in male cancer* (Zhang UKB); *IgG4-Autoimmune Disorders* (Asensio-Wandosell); *Cross-sectional/case-control/cohort in Gynecologic Oncology* (Tian/Wei); *Genetic endocrine tumors thyroid* (Ginzberg); *Family genetic designs in MoBa* re-appearing under Neil M Davies (Corfield already covered HIGH); *Retinopathy in Dyskeratosis Congenita* (Jeng-Miller); *STAR-related retinopathy* (Kwok-Yeng); *Multi-Omics Integration in Clinical Practice for Genetic Variants in Rare Diseases* (Olival) 2026; *Rewiring Pharmacology: Drug Repurposing in Oncology* (Singh) 2026 review; *Conceptual comorbidity networks in autoimmune thyroid disease* (Saka).

Standard survey-and-descriptive coverage across the keyword-feed
periphery. None crossed the on-thread threshold beyond LOW.

---

## What's NOT in the report

- **GitHub `arxiv-digest` cron / PR notifications** — none surfaced in
  Gmail search; the local repo commits and the on-disk `digests/`
  directory serve as the digest artifact (same as 08-17 report).
- **arxiv.org daily category mailings** (`no-reply@arxiv.org`) — the
  raw upstream feed that supplies the `arxiv-digest` pipeline; papers
  surfaced via the digest are covered in the arxiv-digest section
  above.
- **Substack / newsletters** — noted but no biomedical content in this
  window crossed the on-thread threshold.
- **NCBI My-NCBI daily deltas** — six daily runs each firing three
  saved searches (`All of Us`, `UK Biobank`, `drug repurposing`); the
  Scholar keyword feeds captured nearly all overlap and the NCBI-only
  deltas were quiet.
- **medRxiv / bioRxiv Subject Collection Alerts** — one bundled pair
  on 08-23; items overlapping with Scholar are folded into the Scholar
  reports above.

## Next steps to consider

1. **Read Ellershaw et al. Foresight-England (arXiv 2608.16273) full
   text.** The single highest-signal item in this window for the
   `EHR foundation models` thread — 243M-parameter FM on 54.9M NHS
   patients, native to the NHS SDE. Should join the CLMBR / MOTOR /
   MEDS / EHRSHOT reading pack and be paired with the Palacios PHI-
   leakage paper as the FM-buildout + adversarial-audit pair.
2. **Cite Kullo, Bastarache, Berkman et al. return-of-results
   recommendations paper** whenever the CFTR / APOL1 / BRCA
   penetrance-in-AoU / BioVU work touches return-of-results policy.
   Pair with the Cheng et al. A1AT AoU clinical-score paper as the
   ethical + clinical-workflow bookend.
3. **Adopt Zhou et al. STAR Protocols admixed-population PGS protocol**
   as the default reference protocol for any AoU admixed-population
   PGS work downstream. Triple-feed hit is a strong signal it sits on
   the field's methodological spine.
4. **Read Walsh et al. transportability failures for treatment-
   resistant depression** as the empirical companion to the Roine
   et al. HF-diagnosis-heterogeneity paper (08-17 report); together
   they anchor the `Fidelity, portability, and audit of
   representations` reading pack.
5. **Bundle Kosgolla et al. SUD + Yee et al. e-cigarette + Cheng et
   al. A1AT** as three AoU longitudinal-outcomes case studies for a
   future AoU-methods essay on **survey-exposure × EHR-outcome
   ascertainment**; each demonstrates a different
   exposure-ascertainment strategy against a different outcome family.
6. **Read Ao et al. UKB chronic-pain exome-wide + Suger et al. rare-
   variant pleiotropy across cancers** back-to-back as the two
   biobank-scale rare-variant + composite-risk reference points from
   this window; both should feed the composite-risk / PGS-tails
   reading list alongside Baya AJHG 2026 and Souaiaia Nature.
7. **Read Yang et al. LPL context-dependent variant interpretation
   bioRxiv** as the closest 2026 analog for the CFTR-context problem
   (Mendelian ↔ population-genetic dual mode) — the proposed context-
   annotation extension is worth stress-testing against CFTR.
8. **Read Corfield et al. MoBa family-designs Nature** as the
   within-family PGS reference paper for the ancestry-portability +
   PGS-environment thread; explicitly compare against Howe *Nat Genet*
   2022 direct/indirect decomposition when extending to AoU / UKB
   (which mostly lack trio structure).
9. **Read Meyre et al. CHIP × silent brain lesions Circulation** as
   the neurocognitive extension of the cardiovascular-outcomes CHIP
   lineage; note the modeling-choice implication (Bandreddi Tobit-vs-
   hurdle from 08-17 remains actionable here).
10. **Read Schächter et al. LLMs-as-synthetic-clinical-experts for
    rare-disease modeling** for portability to BRCA-incident-cancer,
    APOL1-CKD-conversion, and hereditary-cancer-syndrome
    phenoconversion sub-threads.

_Report generated 2026-08-23 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-23 → next scheduled run._
