# Research digest report — 2026-08-20

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-20 12:37Z** (~3 days since the
last research-digest report, covering four arxiv-digest cron runs, one
Google Scholar keyword-alert batch on 08-19, one Scholar author/citation
batch on 08-19, and four consecutive medRxiv/bioRxiv collection-alert
batches on 08-17, 08-18, 08-19, and 08-20).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-17.md` → `2026-08-20.md`) | 08-17 → 08-20 daily crons | Four cron files. **08-16 and 08-17: 0 relevant papers** (dry — expected, weekend). **08-18: 4 papers** (all stat.ME/stat.AP causal-inference — Bayesian epidemic-clock alignment, zero-inflated causal mediation with non-compliance, digital-health N-of-1 primer, regression-not-to-the-mean with negative-weighting in HTE). **08-19: no file** (cron did not produce output, or dry). **08-20: 3 papers, 1 previously surfaced and suppressed** — Monroe molecular FM (drug-discovery), Peruvian mayor DML (municipal budget execution), urban rail DML (metro reliability). Of the 7 non-suppressed papers this window, four are on-target for the **causal-inference / pharmacoepi** thread; three are off-domain SKIPs. |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` / `chenjiezeng` / `arxiv` returned zero threads in the last 14 days. The `arxiv-digest` pipeline commits its output to the local repo rather than emailing PR / cron notifications, so the on-disk `digests/` tree remains the primary artifact — same as last window. |
| Google Scholar keyword alerts (08-19 batch, 21:10Z) | 08-19 21:10Z | 10 keyword feeds fired: `All of Us research program`, `UK Biobank`, `electronic health records`, `Foundation models` + EHR, `drug repurposing`, `autoimmune diseases`, `rare diseases`, `mendelian diseases`, `variant interpretation` / `variant classification`, `knowledge graph`. Densest signal from the AoU keyword feed (Kosgolla & Smith PRS-and-recovery paper + Kullo/Bastarache secondary-findings recommendations). |
| Google Scholar author + citation alerts (08-19 batch, 14:14Z) | 08-19 14:14Z | 20+ author / new-related / citations-to feeds fired: Chenjie Zeng (self), Lisa Bastarache (citations-to), Joshua C. Denny (citations-to), Miguel Hernán (citations-to), Kai Wang (×2), Konrad Karczewski (×2), George Hripcsak (×2), Peter Szolovits (×2), Jonathan K. Pritchard (citations-to), Jian Yang (×2), Stephen B. Montgomery (×2), Yuan Luo (citations-to), Zhiyong Lu, Marinka Zitnik, Tiffany J. Callahan, Vivek Natarajan (citations-to), Patrick Ryan, Daniel Kastner (citations-to), Wendy Chung (new articles). Densest cluster: causal-inference / pharmacoepi (Hernán CCW review) + federated LLMs in medicine (Hripcsak feed) + rare-variant biobank sequencing (Denny citations-to Fenland WES). |
| Google Scholar keyword alerts (08-18 batch, 12:01Z) | 08-18 12:01Z | 5 keyword feeds fired: `UK Biobank`, `electronic health records`, `Foundation models` + EHR, `autoimmune diseases`, `knowledge graph`. All items medium-to-low relevance (KG non-biomedical, UKB observational cohort, generic agentic-medicine review). |
| medRxiv/bioRxiv collection alerts (08-17 → 08-20 daily) | 08-17 00:05Z → 08-20 00:05Z | Four consecutive daily digests each. medRxiv collections monitored: Epidemiology, Genetic & Genomic Medicine, Health Informatics, Obstetrics & Gynecology, Oncology, Pediatrics, Endocrinology, Nephrology. bioRxiv collections: Bioinformatics, Genetics, Genomics, Immunology, Pathology. Densest on-target signal from **medRxiv Health Informatics (08-19)** — stigmatizing-language LLM audit by Yang et al., federated LLMs, ML-EHR VTE prediction — and **medRxiv Genetic & Genomic Medicine (08-19)** — Fenland WES-adjacent PRS-portability paper, low-pass-seq PGx phenotype inference. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. medRxiv/bioRxiv collection alerts
> give title + author list only (no abstract). The reports below
> contextualize that metadata against your research threads; nothing
> here reflects full-text reading. `arxiv-digest` entries include the
> full abstract because the pipeline captures it. Author lists are
> truncated as they appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Eleven HIGH items surfaced this window, clustering into five knots:

**Biobank × EHR × polygenic-risk cluster (2 items).** Kosgolla & Smith
*Addiction* 2026 (AoU keyword feed) — **PRS × recovery capital predicting
EHR-observed remission and relapse in substance-use disorder in All of
Us**. This is the exact "PGS-in-EHR-linked-biobank as an outcome
modulator, using EHR-derived phenotype endpoints" pattern that lives at
the intersection of the **Biobanks with EHR linkage** and **Genetic
epidemiology** threads — and one of the first pieces to bring PRS into
addiction-medicine longitudinal outcomes at AoU scale. Kullo, Horowitz,
Bastarache, Berkman et al. 2026 (AoU keyword feed, Genomes2People
preprint, in press) — **Recommendations for return of secondary genomic
findings in observational cohort studies**, spanning Geisinger MyCode,
AoU, and NIH-funded workshop consensus. This is the reference
governance-and-return-of-results scaffold that every biobank-scale
monogenic-penetrance analysis on your watchlist eventually has to answer
to; Bastarache authorship is a strong signal to read in full.

**LLM / EHR-foundation-model cluster (3 items).** Yang, Gu, Hathaway,
Wyss, Marengo, Gibbons, Lyndon, Wu, Chen, Liu, Wang, Celi, Bates, Lin,
Zhou, Yang *medRxiv* 2026-08-19 (Health Informatics) — **"Large Language
Models Generate Stigmatizing Language During Reasoning Over Real-World
Clinical Data"**. This is the fairness/audit study your EHR-FM thread
has been missing at this scale — LLM-generated stigmatizing text as an
auditable failure mode on top of real EHRs, not synthetic prompts.
Pairs with the pretraining-contamination sub-thread (scContam / MIA-scFM)
you added to INTERESTS.md as the "audit-EHR-FMs-not-just-benchmark-them"
axis. Li, Chen, Long, Yin, Hu, Kim, Zhou et al. *npj Digital Medicine*
2026 (Hripcsak new-related feed) — **"Toward federated large language
models in medicine: a parameter-efficient framework for
privacy-preserving, multi-institutional adaptation"**. This directly
serves your **federated / privacy-preserving EHR causal analytics**
rising sub-thread; parameter-efficient adaptation (LoRA-style) is the
missing ingredient for FL over sites with heterogeneous compute.
Wiest et al. *medRxiv* 2026-08-18 (Health Informatics) —
**"Retrieval-Augmented LLMs for Clinically Aligned Adverse Event Coding
in AML Clinical Trials"** (Kather group). Trial-side AE coding is a
clean testbed for RAG-anchored LLM-assisted phenotyping; the "clinically
aligned" claim is the audit hook.

**Causal-inference / pharmacoepi cluster (3 items).** Manzanilla,
Brunetta, Peyre-Pradat, Michiels et al. *Journal of Clinical
Epidemiology* 2026 (Hernán citations-to feed) — **"Use of
clone-censor-weight to avoid immortal-time bias: a systematic
methodological review"**. This is the reference paper for CCW-in-TTE
adoption you should cite in every pregnancy / GLP-1 RA / CFTR-modulator
TTE going forward; complements the Wood et al. arXiv 2608.11108
early-pregnancy time-zero paper from the 08-17 report. Rowan & Dreyer
*medRxiv* 2026-08-18 (Epidemiology) — **"Beyond Signal Detection:
Sequential Target Trial Emulations to Confirm Previously Detected
Adverse Drug Event Signals for Atorvastatin in Older Medicare
Beneficiaries"**. Signal-detection → TTE-confirmation is exactly the
two-stage pharmacovigilance framing you've been prototyping for
CFTR-modulator persistence and statin discontinuation; running example
here (statin AE in Medicare) is portable. Power, Sanderson, Gkatzionis,
Richardson, Tilling, Davey Smith, Hemani *medRxiv* 2026-08-18
(Epidemiology, v3) — **"Triangulating evidence to evaluate selection
bias in lifecourse Mendelian randomization studies: a practical
framework illustrated by early-life adiposity and breast cancer"**.
Bristol MRC-IEU triangulation-of-methods framework applied to lifecourse
MR — the Hemani lineage sensitivity-analysis template. Directly relevant
to the **drug-target MR triangulated with observational cohort
estimates** rising sub-thread (Saxby et al. metformin × AAA;
MR-ALasso).

**Genetic-epi / rare-variant / PRS-portability cluster (2 items).**
Perry, Murzynowski, Kerrison, Day, Luan et al. Research Square 2026
(Denny citations-to feed) — **"Exploring Rare Genetic Variation
Underlying Metabolic Traits in the Fenland Cohort"**. WES in 11,458
deeply metabolically phenotyped individuals; explicitly positions itself
as the *deep-phenotyping-follow-up* complement to biobank-scale
sequencing (UKB / AoU) where genotype-targeted metabolic assays are
feasible. Cites the AoU genomic-data paper. This is the pattern —
biobank discovery → intermediate-cohort deep-phenotyping validation —
that your **Genetic epidemiology** thread has been building around.
Harikrishnan & Kelly *medRxiv* 2026-08-19 (Genetic & Genomic Medicine)
— **"Evaluating the Impact of Principal Component and Mixed Model
Approaches on Polygenic Risk Score Portability to Diverse Ancestries in
the UK Biobank"**. Head-to-head PC vs. mixed-model PRS calibration
across ancestries — exactly the methodological ablation the
**pangenome-informed variant calling → PGS-portability** sub-thread
needs on the *statistical-model* side (as opposed to the
*reference-panel* side).

**Somatic-mosaicism / long-read / cross-trait cluster (1 item).**
Jensen, Le Guen, Talozzi, Yang, Gorzynski, Pena-Tauber, Stewart,
Ferasse, Nachun, Arriaga, Lee, Pulgrossi, Park, Zhang, Wagner, Mormino,
Poston, Henderson, He, Wyss-Coray, Montgomery, Ashley, Greicius
*medRxiv* 2025-10-10 → v4 posted 2026-08-18 (Genetic & Genomic
Medicine) — **"Long-read genome sequencing and multi-omics in aging and
neurodegeneration"** (Stephen B. Montgomery, Euan Ashley, Michael
Greicius, Tony Wyss-Coray). Long-read WGS + multi-omics in an aging
cohort; the natural sequencing-modality upgrade for CHIP / VEXAS / LOY
detection (long-read handles structural variants and repeat expansions
that short-read misses), and a clean template for the aging-cohort
neurodegeneration side of the **somatic mosaicism** thread. Version 4
suggests substantial revision since the original post; worth checking
what changed.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
by source, then by bucket.

### arxiv-digest surfacings (2026-08-17 → 2026-08-20)

#### METHODS-WATCH — Moriña D. *Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions.* arXiv 2608.16537v1 (stat.ME, 2026-08-17). Score 1.

Bayesian causal count model in which season-specific affine transforms
map calendar time onto a latent "epidemic clock" — intervention effects
are then estimated on that clock rather than on calendar week, so
season-to-season phase shifts don't confound treatment contrasts. Uses
negative-binomial observation model, hierarchical area/season/area-season
effects, a shrunk Fourier epidemic curve, and continuous
programme-intensity exposure. Posterior g-computation gives prevented
cases, prevented fractions, peak attenuation, and epidemic displacement
under both controlled and dynamic contrasts. Illustrated on Catalan
primary-care RSV immunisation data. Off-domain for your active disease
threads, but the **epidemic-clock alignment as a model component (rather
than preprocessing)** is a general design principle worth cribbing —
directly analogous to the **time-since-onset clock vs. calendar clock**
issue that pregnancy pharmacoepi hits (Wood et al. arXiv 2608.11108) and
that CHIP / VEXAS / LOY natural-history analyses will hit whenever the
"clock" is disease-onset rather than calendar time.

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. *Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.* arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1.

Bayesian causal-mediation framework built on enriched Dirichlet process
mixture models, estimated via a scalable G-computation algorithm.
Motivating example is a US retailer's promotional-email A/B trial —
value-added incentives (free shipping) vs. price discounts — with
non-compliance (email opens), multiple longitudinal mediators, and
zero-inflated mediators + zero-inflated purchase outcomes. Analyses that
ignore email-opening behaviour substantially attenuate estimated
effects. The infrastructure is the interesting bit for you: **zero-
inflated longitudinal mediators + non-compliance + G-computation** is
the exact statistical situation that arises in EHR pharmacoepi when
adherence is measured via prescription fills (many zeros: months with
no fills), the mediator is a lab or biomarker with irregular
measurement (zero-inflated by missingness), and the outcome is a count
of clinical events. Directly portable to CFTR-modulator persistence-
mediating-lung-function analyses.

#### MEDIUM — Daza EJ. *A Primer on Digital Health N-of-1 Studies and Single-Case Designs.* arXiv 2608.15526v1 (stat.AP, 2026-08-16). Score 1.

Chapter-length primer on n-of-1 studies and single-case designs for
digital-health applications, positioning them as "characterizing a
single person's own recurring health patterns first" rather than
subgroup-identification. Coins "esametry" (statistics of the digitized
multitudes within each of us). Off-topic for your active disease
threads but conceptually useful as the individual-level counterpart to
your **PheRS / precision-medicine** and **individualized risk
prediction / heterogeneous-treatment-effect** work — n-of-1 is the
degenerate case where the subgroup size is one. If a reviewer ever
asks "why aren't you doing this individually", this is the primer to
cite.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. *Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.* arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1.

Applies the Chaisemartin-D'Haultfoeuille / Goodman-Bacon
**negative-weighting-in-two-way-FE-with-staggered-treatment** critique
outside of linear regression, showing the same issue arises in logistic
regression models. Running example: drug-induced homicide (DIH)
prosecutions reported by media as a "treatment" on unintentional
drug-overdose deaths, US 2016-onward. Estimated constant-treatment risk
ratio (0.977 linear, 1.064 logistic) differs in sign or magnitude from
the average HTE-implied risk ratio (0.728 range 0.507–0.979 linear;
0.739 range 0.538–1.008 logistic). Direct methodological addition to
your **heterogeneous treatment effects** thread: constant-treatment-
effect estimators in logistic regression are not safe when treatment
timing is staggered — matters for staggered-adoption pharmacoepi (GLP-1
RA uptake, CFTR-modulator eligibility waves, HRT prescribing eras).

#### SKIP — Banaszewski B, Fitzgibbon AW. *Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference.* arXiv 2608.18982v1 (cs.LG, 2026-08-19). Score 1.

Molecular foundation model pretrained on 81M PM6-quantum-chemistry
molecules, using stereochemistry-aware graph encoding, conformer
denoising, embedding decorrelation, multi-task learning, and TabPFN
prior-data-fitted downstream head. Matches or exceeds SOTA on Polaris
benchmarks and improves activity-cliff prediction. Off-topic — this is
a chemistry MFM for drug-discovery scaffolding, not clinical or
EHR-linked. Adjacent to your **drug repurposing** thread only in the
sense that MFM-derived molecular representations could feed a
KG-explainable repurposing pipeline downstream, but the paper itself
doesn't touch that loop.

#### SKIP — Machacuay C, Lincovil J, Rojas H. *Mayoral Experience or Municipal Capacity? Negative-Outcome Evidence on Municipal Budget Execution in Peru.* arXiv 2608.18354v1 (stat.AP, 2026-08-18). Score 1.

Panel double-machine-learning + negative-outcome-control identification
strategy for the effect of mayoral human capital on budget execution,
using 1,642 Peruvian district municipalities 2015–2022. Off-topic. The
**negative-outcome-control-aligned-with-within-municipality-design**
identification pattern is worth flagging as a general causal-inference
tactic — the analogue in EHR pharmacoepi would be checking that
pre-treatment "negative control outcomes" (falsification endpoints
unaffected by the drug) don't predict treatment assignment within
person — but the methods here don't add to the standard falsification
literature.

#### SKIP — Yao Y, Zhang N, Graham DJ. *Quantifying the Causal Operational Determinants of Service Reliability in Urban Rail Transit: Evidence from Panel Double/Debiased Machine Learning.* arXiv 2608.17901v1 (stat.AP, 2026-08-18). Score 1.

Panel DML applied to 46 metro operators × CoMET benchmarking database
1994–2024. Off-topic. Interesting only as another datapoint that
panel-DML is now the default in applied stat.AP causal-inference
work — same trajectory that your **causal ML** thread has been
tracking.

---

### Google Scholar keyword alerts (08-18, 08-19 batches)

#### HIGH — Kosgolla JV, Smith DC. *Joint associations of recovery capital and polygenic risk with electronic health record observed remission and relapse in substance use disorder: Longitudinal evidence from the All of Us research program.* Addiction (Abingdon, England) 2026. AoU keyword feed, 08-19 21:10Z.

Longitudinal AoU analysis combining a **recovery-capital construct** and
**polygenic risk score** as joint predictors of substance-use-disorder
remission and relapse, with the endpoint defined from *EHR-observed*
events (rather than survey self-report). Directly fits three of your
threads at once: **Biobanks with EHR linkage** (AoU-derived
longitudinal endpoints); **Genetic epidemiology** (PRS-as-modulator
design); **EHR phenotyping** (EHR-derived remission/relapse phenotype
in SUD, historically hard because SUD is under-coded and mis-coded).
The Addiction venue and the "EHR-observed" phrasing in the title
suggests they had to make explicit methodological choices about how to
call a remission event from codes — worth reading in full for the
phenotype-definition section alone. A rare AoU paper that pairs PRS
with EHR-outcome phenotyping in behavioural health.

#### HIGH — Kullo IJ, Horowitz CR, Bastarache L, Berkman B, et al. *Recommendations for return of secondary genomic findings in observational cohort studies.* Genomes2People preprint (in press), 2026. AoU keyword feed, 08-19 21:10Z.

Consensus-workshop recommendations for return-of-secondary-findings
across observational cohorts including Geisinger MyCode, AoU, and
NIDDK-funded studies. Bastarache authorship + Kullo (Mayo, ClinGen)
first authorship makes this the reference governance-and-ethics
document for any biobank-scale monogenic-penetrance analysis that has
to decide whether/how to return actionable findings. Directly relevant
to your **variant interpretation (ACMG / ClinGen)** thread and to the
**penetrance estimation for monogenic variants under population-
screening conditions** sub-thread of PheWAS/PheRS infrastructure. Read
in full when you next revise the CFTR / APOL1 / hereditary-cancer
penetrance manuscripts — the return-of-results discussion will need
to cite this.

#### METHODS-WATCH — Ginzberg SP, Weller JHD, Skefos CM, Perrier ND. *Genetic endocrine tumors focusing on the thyroid.* Best Practice & Research Clinical … 2026. AoU keyword feed, 08-19 21:10Z.

Review that cites the AoU + UKB RET-pathogenic-variant prevalence
estimate (1 in ~245k AoU + 469k UKB) as landmark. Adjacent to your
**biobank-based penetrance** work — the population-based-prevalence
number they cite came out of the exact analysis you and colleagues do.
Not a primary read but worth noting as external citation of the
methodological framing.

#### HIGH — Higgins DM, Blackden C, Brown M, Diaz C, Duffy L et al. *The Gabriella Miller Kids First Data Resource for genomic research in pediatric cancer and congenital anomalies.* American Journal of Human Genetics 2026. AoU keyword feed, 08-19 21:10Z.

Resource paper describing Kids First (pediatric cancer + congenital
anomaly WGS + clinical data). Not directly on any active thread but
worth knowing about as an **EHR-linked pediatric-cohort biobank
complement** — the pediatric-cohort space is thin in your current
watchlist and Kids First is the field-standard resource.

#### MEDIUM — Ghosh S, Panda SK, Pattanaik SR. *A Critical Review on Generative Artificial Intelligence in Healthcare: Innovations, Applications and Challenges.* Frontiers in Engineering, Science, 2027. `Foundation models + electronic health records` feed, 08-19 21:10Z.

Generic generative-AI-in-healthcare review; the "2027" journal issue is
telling. SKIP as primary read but flag as one of many generic reviews
crowding the FM-in-medicine feed.

#### MEDIUM — Olival J, Pijuan J, Caelles-Gramunt N et al. *Multi-Omics Integration in Clinical Practice for the Identification of Genetic Variants in Rare Diseases.* Archives of Medical Research 2026. `rare diseases` feed, 08-19 21:10Z.

Review of multi-omics integration for rare-disease variant
identification. Adjacent to your **rare disease** thread but the field
has ~5 reviews per month of this shape now — skip unless it names a
specific method or tool that isn't already in your rare-disease
review-of-methods stack.

#### MEDIUM — López-Bueno R, Andersen LL, Polo-López A et al. *Longitudinal changes of cardiorespiratory fitness are associated with cardiovascular disease and mortality: evidence from the UK Biobank.* European Journal of ... 2026. `UK Biobank` feed, 08-19 21:10Z.

Standard UKB observational cardiorespiratory-fitness → CVD-and-mortality
association study. Not on your active disease threads; MEDIUM only as an
example of the "UKB observational-cohort" content that dominates the UKB
keyword feed.

#### SKIP — Singh S, Pandey SK, Sohal JS. *Rewiring Pharmacology: Drug Repurposing as a Precision Tool in Oncology - A Systematic Review.* Current Cancer Drug Targets 2026. `drug repurposing` feed, 08-19 21:10Z.

Oncology drug-repurposing review without a clinical-evidence loop or
KG-explainable output. Off the high-priority angles for your **drug
repurposing** thread.

#### SKIP — Saka N, Vijaya KS, Mohan CC, Kadiyam N, Bhandari RB. *Conceptual comorbidity networks in autoimmune thyroid disease: A PRISMA-guided review of clinical patterns, immunological links, and emerging disease clusters.* 2026. `autoimmune diseases` feed, 08-19 21:10Z.

Autoimmune-thyroid-comorbidity review; adjacent to **chronic disease
clustering** only as a conceptual review of clusters, not a data-
driven multimorbidity paper.

#### SKIP — Yaseen H, Shah AAH, Nadeem M, Shakeel H. *Genetic neglect and health inequity: the overlooked burden of Alport syndrome in Pakistan.* Journal of Community Genetics 2026. `variant interpretation` feed, 08-19 21:10Z.

Regional-disparities commentary on Alport syndrome. Off active threads.

#### SKIP — Li S, Chen X, Cen H, Chen H, Lu Y. *Insomnia Increases Susceptibility to Sciatica: Evidence from Mendelian Randomization and Integrative Genetic Analyses.* Journal of Pain Research 2026. `mendelian diseases` feed, 08-19 21:10Z.

MR on insomnia → sciatica. Off active disease threads.

#### SKIP — Yi X, Duan R, Fei Y et al. *A Method for Generating Safety Measures of Hydropower Plant Work Tickets Integrating Knowledge Graph and Large Language Models.* 2026. `knowledge graph` feed, 08-19 21:10Z.

Non-biomedical KG application. Consistent noise on the KG feed.

---

### Google Scholar author + citation alerts (08-19 batch, 14:14Z)

#### HIGH — Perry J, Murzynowski J, Kerrison N, Day F, Luan J et al. *Exploring Rare Genetic Variation Underlying Metabolic Traits in the Fenland Cohort.* Research Square (preprint, `rs-10473668`), 2026. Denny citations-to feed.

WES in 11,458 Fenland participants — a population-based cohort with
**extended metabolic phenotyping** (Nightingale NMR-lipidomics,
proteomics, deep OGTT, extensive lab panel). Positions itself as the
deep-phenotyping-follow-up complement to biobank-scale WES (UKB / AoU)
where genotype-targeted metabolic assays are logistically infeasible.
First large-scale rare-variant association within the Fenland design.
Cites the Bick/Denny **AoU genomic data** resource paper (hence the
Denny alert). Direct fit for your **Genetic epidemiology** thread (rare
variant + metabolic quantitative-trait association) and for the
**Multi-omics-augmented PRS** rising sub-thread (Nightingale/Olink/
metabolomics stacked with PGS). Read in full: the ascertainment and
phenotype-panel design is the interesting bit, not just the discovered
associations.

#### HIGH — Manzanilla A, Brunetta C, Peyre-Pradat F, Michiels S et al. *Use of clone-censor-weight to avoid immortal-time bias: a systematic methodological review.* Journal of Clinical Epidemiology 2026. Hernán citations-to feed.

Systematic review of CCW-in-TTE adoption in published observational
studies. This is the reference paper for **clone-censor-weight as the
default anti-immortal-time tactic in target-trial emulation** —
complements the Wood et al. arXiv 2608.11108 pregnancy-TTE tutorial
from the last window. Every EHR-based TTE you write from here on
(GLP-1 RA, SGLT2i, CFTR-modulator, HRT) should cite one of these two.
Read in full and pull the reporting-checklist section into your TTE
manuscript-drafting boilerplate.

#### HIGH — Li A, Chen Y, Long W, Yin Y, Hu Y, Kim H, Zhou W et al. *Toward federated large language models in medicine: a parameter-efficient framework for privacy-preserving, multi-institutional adaptation.* npj Digital Medicine 2026. Hripcsak new-related feed.

Parameter-efficient (LoRA-style) federated fine-tuning framework for
medical LLMs — the core observation is that full-model FL is
infeasible across sites with heterogeneous compute, but parameter-
efficient adaptation (LoRA / prefix / adapter tuning) is FL-tractable
and preserves privacy. Directly serves your **federated /
privacy-preserving EHR causal analytics** rising sub-thread (Jang et
al. arXiv 2607.17958 lineage) but on the LLM axis rather than the
statistical-estimator axis. Together they cover the two natural FL
substrates: FL-over-estimators (mediation/HTE) and FL-over-model-
adaptation (medical LLMs). npj Digital Medicine venue makes this the
canonical citation. Read in full.

#### METHODS-WATCH — Kabata D. *Using oalasso with psAve.* CRAN package vignette. Hripcsak new-related feed.

R package vignette for outcome-adaptive lasso (Shortreed & Ertefaie
2017) integrated with psAve. Not a paper but a tooling note — the
outcome-adaptive lasso is the right default variable selector for the
propensity-score model in high-dimensional EHR pharmacoepi (selects
confounders + outcome predictors, excludes instruments + noise). Worth
knowing that the R ecosystem has caught up.

#### HIGH — Abner E, Johnson JP, Vujkovic M, Daly M et al. *Genetic variants affect diurnal glucose levels throughout the day.* Nature 2026. Karczewski new-related feed.

**PREVIOUSLY SURFACED** in the 2026-08-17 report — suppress. Recap: UKB
CGM-like data → time-of-day function-valued glucose GWAS; anchors the
**PGS × modifiable-environment (chronotype)** sub-thread.

#### METHODS-WATCH — Chimusa ER. *A Spectrum of the Genomics Landscape of African Diversity.* Genomics in Africa 2026. Karczewski citations-to feed.

Review-chapter on African genomic diversity. Adjacent to
**cross/trans-ancestry portability** in your Genetic epi thread but
review-level, not primary methods.

#### MEDIUM — Duz MB, Lasa-Aranzasti A, Cazurro-Gutiérrez A et al. *Clinical characterization and genotype–phenotype correlations in Chilton-Okur-Chung syndrome.* BMC Medical Genomics 2026. Wendy Chung new-articles feed.

Rare-disease case series for a specific syndrome. MEDIUM for your
**rare disease** thread as a routine genotype-phenotype paper —
useful only if you're actively curating that gene.

#### MEDIUM — Trotta G, Austin-Zimmerman I, Spinazzola E, Sideli L et al. *Integrating biological pathway polygenic scores and trauma in psychosis: findings from the EU-GEI study.* Translational Psychiatry 2026. Jian Yang new-related feed.

Pathway-PGS × environment interaction (trauma) in psychosis — an
instance of your **GxE and PGS × exposure / environment
interactions** rising sub-thread (Nagpal & Gibson lineage), on the
psychiatric-disease side. Not a MUST-READ but a data-point for the
pattern.

#### SKIP — Marziani L, Stenz KT, Zhang H et al. *Exploring the protective potential of remote ischemic conditioning-induced miRNAs in stroke.* Neuroscience 2026. Lisa Bastarache citations-to feed.

Stroke miRNA mechanism; off active threads.

#### SKIP — Ayduran S, Kılbaş G, Tığrak SN, Kaleli İ, M. *Phoenixin-14 May Be a Potential Limiting Neuropeptide for Exaggerated Inflammation in Familial Mediterranean Fever and Periodic Fever, Aphthous Stomatitis...* 2026. Daniel Kastner citation feed.

FMF neuropeptide biology; off active threads.

#### SKIP — Mora P, Aroda VR, Asong M et al. *Efficacy and safety of once-daily oral zenagamtide, a novel unimolecular GLP-1 and amylin receptor agonist, in adults with T2D...* 2026. Patrick Ryan new-related feed.

RCT of a new GLP-1/amylin dual agonist; off your causal-inference /
pharmacoepi angle (this is trial evidence, not observational).
MEDIUM only if you're tracking the GLP-1 drug landscape for
downstream real-world persistence work.

#### (Author-feed noise, condensed as one bucket) — SKIP.

Multiple author feeds returned the same off-domain papers (WU Xinyao
et al. *Nanopore-based epigenomic profiling of African swine fever
virus*, appearing under both Kai Wang new-related and Kai Wang
citations-to; the Carey sepsis biomarker paper appearing under both
Peter Szolovits and Yuan Luo citations-to; the AGSI single-cell paper
under Stephen B. Montgomery new-related; the diffusion-language-model
arXiv preprints under Marinka Zitnik and Zhiyong Lu new-related; the
Reducing Pretraining-Generation Mismatch under Marinka Zitnik). None
are on active threads. The Szolovits-adjacent *Model and Task-Aware
Test-Time Scaling Strategies for Large Language and Vision-Language
Models in Medicine* (Oh, Kim, Park, Kim in JMIR) is MEDIUM as a
methods-adjacent LLM-in-medicine paper but doesn't add to the
EHR-foundation-model thread specifically.

---

### medRxiv / bioRxiv collection alerts (08-17 → 08-20 daily digests)

#### HIGH — Yang Y, Gu B, Hathaway DB, Wyss R, Marengo L, Gibbons JB, Lyndon S, Wu J, Chen Q, Liu N, Wang PS, Celi LA, Bates DW, Lin J, Zhou L, Yang J. *Large Language Models Generate Stigmatizing Language During Reasoning Over Real-World Clinical Data.* medRxiv 2026-08-19 (Health Informatics), doi:10.64898/2026.08.12.26360210.

Audit of LLM-generated stigmatizing language during clinical-reasoning
tasks *over real-world EHR data*, not synthetic prompts. Author list
spans Brigham (Bates, Zhou, Lin), Yale (Chen, Yang), Duke (Liu), and
NIMH/Harvard (Wang) — heavy Bates-Zhou cluster. This is the
**fairness-and-calibration audit of EHR foundation models grounded in
EHR data** thread's canonical study, and the "stigmatizing language" as
an auditable failure mode is a portable metric. Pairs conceptually with
the pretraining-contamination sub-thread you added to INTERESTS.md.
Read in full and note whether they published the eval prompts and
adjudication rubric — those are what makes it reproducible across
EHR-FMs (CLMBR / MOTOR / MEDS).

#### HIGH — Rowan CG, Dreyer NA. *Beyond Signal Detection: Sequential Target Trial Emulations to Confirm Previously Detected Adverse Drug Event Signals for Atorvastatin in Older Medicare Beneficiaries.* medRxiv 2026-08-18 (Epidemiology, v3), doi:10.64898/2026.08.12.26360302.

**Signal-detection → TTE-confirmation** as a two-stage pharmacovigilance
framing. Runs sequential TTEs on Medicare claims for previously
detected atorvastatin AE signals — the design pattern is the read-worthy
piece, portable to any Sentinel-lineage or FDA-BEST-lineage AE-signal
follow-up. Directly relevant to your **statin discontinuation as
outcome** (pharmacogenomic-modifier-of-medication-persistence rising
sub-thread) and to the **CFTR-modulator adverse-event**
signal-to-TTE pipeline you've been sketching.

#### HIGH — Power GM, Sanderson E, Gkatzionis A, Richardson TG, Tilling K, Davey Smith G, Hemani G. *Triangulating evidence to evaluate selection bias in lifecourse Mendelian randomization studies: a practical framework illustrated by early-life adiposity and breast cancer.* medRxiv 2025-09-10 → v3 posted 2026-08-18 (Epidemiology), doi:10.1101/2025.09.10.25335479.

Bristol MRC-IEU triangulation-of-methods framework applied to
lifecourse MR — Hemani/Davey Smith lineage. Running example: early-life
adiposity → breast cancer, where selection bias into UKB is a known
issue. Directly relevant to your **drug-target MR triangulated with
observational cohort estimates** rising sub-thread (Saxby et al.
metformin × AAA) — the triangulation logic is the same, just with a
lifecourse-exposure twist rather than a drug-target twist. Read in full
if you're planning any MR of an early-life exposure (adiposity, birth
weight, smoking-in-parents) → adult disease.

#### HIGH — Harikrishnan AS, Kelly CM. *Evaluating the Impact of Principal Component and Mixed Model Approaches on Polygenic Risk Score Portability to Diverse Ancestries in the UK Biobank.* medRxiv 2026-08-19 (Genetic & Genomic Medicine), doi:10.64898/2026.08.17.26360388.

Head-to-head comparison of PC-adjustment vs. mixed-model approaches for
PRS portability across UKB ancestries. Direct methodological ablation
on the **statistical-model** axis of PRS-cross-ancestry-portability, as
opposed to the **reference-panel** axis (pangenome / HPRC). Together
they'd carve up the "which knob matters most for portability" question
in your **cross / trans-ancestry portability** sub-thread.

#### HIGH — Jensen TD, Le Guen Y, Talozzi L, Yang S, Gorzynski JE, Pena-Tauber A, Stewart IF, Ferasse A, Nachun D, Arriaga TM, Lee J, Pulgrossi RC, Park J, Zhang J, Wagner AD, Mormino EC, Poston KL, Henderson VW, He Z, Wyss-Coray T, Montgomery SB, Ashley EA, Greicius MD. *Long-read genome sequencing and multi-omics in aging and neurodegeneration.* medRxiv 2025-10-10 → v4 posted 2026-08-18 (Genetic & Genomic Medicine), doi:10.1101/2025.10.10.25337775.

Long-read WGS + multi-omics in an aging + neurodegeneration cohort.
Author list is a Stanford neuro-genomics powerhouse (Montgomery,
Ashley, Wyss-Coray, Greicius). Directly relevant to your **CHIP /
VEXAS / LOY somatic mosaicism** thread as the sequencing-modality
upgrade — long-read handles the structural variants, repeat
expansions, and mosaicism that short-read misses at the low VAFs
somatic-mutation calling requires — and to the **rare disease** thread
(long-read reanalysis of unsolved cases at scale). Version 4 suggests
substantial revision; check the changelog.

#### HIGH — Wiest IC, Dashti N, Schneider MMK, Eckardt JN, Fiebig F, Schweigler D, Buttner S, Middeke JM, Bornhauser M, Rollig C, Kather JN. *Retrieval-Augmented Large Language Models for Clinically Aligned Adverse Event Coding in Acute Myeloid Leukemia Clinical Trials.* medRxiv 2026-08-18 (Health Informatics), doi:10.64898/2026.08.17.26360282.

RAG-anchored LLM for AE coding in AML trials; Kather group (Dresden).
Clinical-alignment claim is the audit hook. Directly relevant to
**NLP / LLM extraction from clinical notes for phecode and HPO term
assignment** (EHR phenotyping thread) and to **applications to
prioritize: adverse-event surveillance** in the knowledge-
representation thread. Read to see how they operationalized "clinically
aligned" — that's the missing metric on most LLM-AE-coding papers.

#### METHODS-WATCH — Hodel F, Thorball CW, Haefliger D, Cerutti L, Cattaneo P, Howald C, Männik K, de La Harpe R, Samer CF, Xenarios I, Fellay J, Girardin FR. *Comparative evaluation of genotyping and low-pass sequencing for pharmacogenetic variant and phenotype inference.* medRxiv 2026-08-19 (Genetic & Genomic Medicine), doi:10.64898/2026.08.18.26360694.

Head-to-head of genotyping vs. low-pass sequencing for PGx variant and
metabolizer-phenotype inference. Directly relevant to the
**pharmacogenomic modifier of medication persistence** rising sub-thread
— the CYP2D6-metabolizer PGx pipeline you're prototyping depends on
which upstream genotyping technology gets used. Skim for the accuracy
comparison and cost per sample.

#### METHODS-WATCH — Uren C, Moller M, Oelofse CR. *In-silico functional prediction of novel tuberculosis pharmacogenetic variants and NAT2 phenotype prediction in African populations.* medRxiv 2026-08-19 (Genetic & Genomic Medicine), doi:10.64898/2026.08.17.26360486.

NAT2 metabolizer-phenotype prediction in African populations. Adjacent
to the **PGx** and **cross-ancestry portability** sub-threads; MEDIUM.

#### MEDIUM — Li Z, Yagis E, Riad A, Windrath-Carr O, Arribas M, Sodiq T, Goldsmith K, Glampson B, Flott K, Haji G, Khan Z, Baker C, Mayer EK. *Machine Learning-Supported Efficient VTE Risk Assessment using Routinely Collected Electronic Health Record Data.* medRxiv 2026-08-19 (Health Informatics), doi:10.64898/2026.08.18.26360687.

EHR-based ML for VTE risk assessment. Standard shape for the
**ML for precision health** thread (ML tied to a clinical decision:
who to give thromboprophylaxis to). Skim if you're actively working on
a VTE prediction pipeline; otherwise MEDIUM.

#### MEDIUM — Vijay A, Govind N, Moorthy A et al. *Explainable Clinician-Supervised Artificial Intelligence as an Implementation Framework for Cardiovascular-Kidney-Metabolic Population Health: Synthetic Data Validation of the CHAPERONE-CKM Framework.* medRxiv 2026-08-19 (Health Informatics), doi:10.64898/2026.08.17.26360643.

CKM population-health AI framework, validated on synthetic data
(reasonable-but-unproven substitute for real EHR). Adjacent to
**chronic disease clustering and multimorbidity** and **ML for
precision health** but the synthetic-data validation limits how much
weight it should carry.

#### MEDIUM — Kacar E, Gomes TDS, O'Donoghue C, Venslovaite G, Hardiman O, McLaughlin RL, Byrne RP. *Genome-wide analyses reveal shared and distinct genetic architecture linking amyotrophic lateral sclerosis, sporadic frontotemporal dementia and cognitive traits.* medRxiv 2026-08-19 (Genetic & Genomic Medicine), doi:10.64898/2026.08.17.26360494.

Cross-trait GWAS ALS × FTD × cognitive traits. Instance of your
**cross-trait shared genetic architecture and multi-trait
triangulation** (MiXeR / conditional-FDR family) sub-thread on the
neurodegeneration side; useful as a data-point.

#### MEDIUM — Ma S, West PK, Trinh A, Yang A, Dolzhenko E, Al Khleifat A, Ali A, Iacoangeli A, Wong T, Akkari PA, Ellis-Ovadia N, Faruq M, Al-Chalabi A, Harms MB, Heiman-Patterson TD, Bedlack R, Stromme M. *Enrichment of Repeat Expansions in FGF14 Associated with Amyotrophic Lateral Sclerosis.* medRxiv 2026-08-18 (Genetic & Genomic Medicine), doi:10.64898/2026.08.16.26351538.

Repeat-expansion association study for ALS. Adjacent to long-read-WGS
thread (repeat expansions are the classic short-read-blindspot); MEDIUM.

#### MEDIUM — Stankevic E, Huang Y, Campillo Pereda I et al. (DBDS Genomic Consortium + Iceland collaborators). *Genomic and proteomic evidence linking dental caries in childhood and adolescence to cardiometabolic diseases.* medRxiv 2026-08-19 (Epidemiology), doi:10.64898/2026.08.17.26360562.

Danish Blood Donor Study + Iceland genomic-consortium multi-omics
analysis linking childhood/adolescent dental caries to adult
cardiometabolic disease. Interesting as a large-scale multi-omics
biobank-lineage study; adjacent to **Multi-omics-augmented PRS** and
**Biobanks with EHR linkage** but the specific phenotype (dental
caries → CVD) is outside your active disease threads.

#### MEDIUM — Kowada A. *Optimal LDCT screening for never-smoking Asian women using integrated polygenic and environmental risk: a microsimulation modelling study.* medRxiv 2026-08-18 (Oncology), doi:10.64898/2026.08.18.26360665.

PRS + environmental risk integrated into a lung-cancer screening
microsimulation for never-smoking Asian women — one of the cleaner
recent applications of **PGS-informed screening-threshold
optimization**. Adjacent to your **ML for precision health** thread on
the screening-decision side.

#### METHODS-WATCH — Merlo J, Bashir NZ, Rodriguez-Lopez M, Khalaf K, Öberg J, Perez-Vicente R. *Describing health inequalities without distortion: Simple-Means MAIHDA vs Random-Effects MAIHDA.* medRxiv 2026-08-18 (Epidemiology), doi:10.64898/2026.08.17.26360592.

Head-to-head of two MAIHDA (multilevel analysis of individual
heterogeneity and discriminatory accuracy) variants for intersectional-
inequality description. Adjacent to your **heterogeneous treatment
effects** thread on the descriptive-inequality side rather than the
treatment-effect-modification side; useful methods reference.

#### METHODS-WATCH — Mäkelä E, Kari JT, Van Genechten S, Bottas R, Sillanpää E, Joensuu L. *Causal Effects of Physical Activity and Sedentary Behavior on Healthcare Costs.* medRxiv 2026-08-19 (Epidemiology), doi:10.64898/2026.08.18.26360577.

Causal analysis of physical activity → healthcare costs; adjacent to
**target trial emulation** methods but off active disease/exposure
threads.

#### MEDIUM — Sehgal NKR, Tronieri JS, Rader B, Ungar L, Guntuku SC. *Self-Reported Side Effects Among Reddit Users Taking Nonapproved Retatrutide.* medRxiv 2026-08-18 (Health Informatics), doi:10.64898/2026.05.28.26352819.

Social-media pharmacovigilance for a non-approved GLP-1/GIP/glucagon
triple agonist (retatrutide). Adjacent to your **GLP-1 RA persistence
/ adverse-event** watchlist; MEDIUM as an unconventional data source.

#### MEDIUM — Savatt JM, Nixon MP, Berry ASF, Johns A, Walsh LK, Martin CL, Ledbetter DH, Challman TD, Myers SM. *Elevated Rates of Gastrointestinal Dysfunction in Children with Neurodevelopmental Disabilities: Not Just an Autism Issue.* medRxiv 2026-08-19 (Pediatrics), doi:10.64898/2026.08.17.26360370.

Geisinger MyCode-adjacent (Ledbetter, Martin, Myers) pediatric
neurodevelopmental-disability × GI comorbidity study. Adjacent to
**chronic disease clustering and multimorbidity** on the pediatric side;
MEDIUM.

#### SKIP (bioRxiv 08-20, condensed) — Nothing on the bioRxiv Bioinformatics / Genetics / Genomics / Immunology / Pathology digest for 08-20 lands on an active thread. The closest miss is the *Automating the Construction of Contextualized Biomedical Knowledge Graphs for Scientific Inference* (Zheng, Liu, Zeng et al.) — a KG-construction methods paper, on-topic for the **Knowledge graphs & ontologies** thread but weak on the biomedical-reasoning-quality side; skim if you want the pipeline. Also worth noting the *Single-cell foundation models benefit from cross-modal training: adding proteomics data beats parameter scaling* (Burq, Stepec, Kim, Cimermancic) — off the EHR-FM axis but a clean data-point for the "modality beats scale" argument at the pretraining-strategy level.

#### SKIP (medRxiv 08-17, condensed) — 08-17 medRxiv Epidemiology digest surfaced *A Mendelian randomization-based drug repurposing* study whose abstract wasn't captured in the alert snippet — flag to inspect the medRxiv 08-17 collection page directly if you want to trace it (candidate for the **drug repurposing** thread if the design does clinical-evidence-loop closure).

---

## Coverage-gap notes

- **PheWAS / phecode infrastructure**: 0 direct hits this window. Not
  concerning at 3 days but worth flagging if next window is also dry —
  the phecode-methods literature has been slow this quarter.
- **CFTR / Trikafta**: 0 direct hits.
- **APOL1**: 0 direct hits.
- **CHIP / VEXAS / LOY**: 1 adjacent hit (Jensen et al. long-read WGS
  in aging cohort — modality upgrade).
- **IBD**: 0 direct hits.
- **EHR foundation models — pretraining contamination**: no new
  contamination-audit papers surfaced; the Yang et al. stigmatizing-
  language audit is a fairness-side complement but not a
  contamination-side one.
- **Digital twins from EHR data**: 0 hits.

If the next 3–7 days stay dry on these, consider a manual arXiv
`stat.ME` + `cs.LG` scan for "population-level digital twin" and a
manual medRxiv scan for "CFTR modulator" and "APOL1" as a coverage
patch.
