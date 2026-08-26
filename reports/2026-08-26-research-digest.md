# Research digest report — 2026-08-26

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-26 13:00Z** (~9 days since the
last research-digest report, covering nine arxiv-digest cron runs and
the 08-25 late-evening Google Scholar author-feed batch plus the 08-26
morning keyword batch).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-17.md` → `2026-08-26.md`) | 08-17 → 08-26 daily crons | 9 daily runs (08-19 missing — no digest file committed for that date). 08-17, 08-21, 08-22, 08-23, 08-24: 0 relevant papers (dry runs, with 3 / 1 / 1 / 0 / 0 papers respectively suppressed as previously surfaced). 08-18: 4 papers (Bayesian epidemic alignment g-computation, zero-inflated causal mediation, N-of-1 primer, regression-not-to-mean overdose HTE). 08-20: 3 papers (Monroe MFM, Peruvian-mayor double ML, urban-rail DML — all off-thread biomedical). 08-25: 1 paper (causal effects in extremes, off-domain). 08-26: 1 paper (RIBOSPAN RNA foundation model, off-EHR). |
| No `arxiv-digest` email hits from GitHub | — | Confirmed with `from:notifications@github.com` search; the local repo commits are the artifact. |
| Google Scholar alerts (author + citation feeds, 08-25 23:33Z batch) | 08-25 23:33Z | ~30 author/citation feeds fired simultaneously: Chenjie Zeng (self), Lisa Bastarache (×2), Joshua C. Denny (×2 — new-related + 10 citations-to), Kai Wang (×2), Konrad Karczewski (×2 — new-related + 10 citations-to), Peter Szolovits (×2), Marinka Zitnik, Zhiyong Lu, Tiffany J. Callahan, Jian Yang (×2), Stephen B. Montgomery (×2), Daniel Kastner, George Hripcsak (×2), Pascal Brandt, Yuan Luo, Jonathan K. Pritchard, Miguel Hernán, Vivek Natarajan, Hongyu Zhao, Hua Xu, Patrick Ryan. |
| Google Scholar alerts (keyword feeds, 08-26 08:21Z batch) | 08-26 08:21Z | 9 keyword feeds fired: `UK Biobank`, `All of Us research program`, `knowledge graph`, `electronic health records`, `Foundation models + electronic health records`, `drug repurposing`, `rare diseases`, `mendelian diseases`, `variant interpretation` / `variant classification`. |
| NCBI My-NCBI PubMed "What's New" (sender `efback@ncbi.nlm.nih.gov`) | 08-19 → 08-26 daily | 3 saved searches — `All of Us`, `UK Biobank`, `drug repurposing`. 08-26 `All of Us` batch: 4 articles. 08-26 `UK Biobank` batch: 17 articles. The full 08-26 AoU and UKB batches were retrieved and are triaged below; earlier daily NCBI batches only had headlines retained. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. NCBI PubMed alerts carry title + authors + citation
> only. `arxiv-digest` entries include the full abstract because the
> pipeline captures it. Author lists are truncated as they appear in
> alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fifteen HIGH items surfaced this window, clustering into six knots:

**All of Us direct-methods cluster (3 items).** Zhang J, Hong SH, Wang
X, Jurgens SJ, Liu CT, Dupuis J, Ellinor PT, O'Connor GT, Mei Q, Choi
SH — *Transcript-aware rare genetic variant association analyses of
cardiopulmonary traits in the All of Us Research Program.* Nat Commun
2026;17:9038. **Direct-hit AoU rare-variant paper** from the Ellinor
group; transcript-aware collapsing (vs. gene-level) is the exact
`PheWAS / phecode infrastructure` × `Biobanks with EHR linkage` ×
`Genetic epidemiology` cross-thread reference paper this window
produces. Sharp RR, Hysong M, Mealer RG, Raffield LM, Glover L, Love MI
— *Considering social risk alongside genetic risk for bipolar disorder
in the All of Us Research Program.* HGG Adv 2026:100665. Direct hit on
the **PGS × exposure / environment interactions** rising sub-thread
(Nagpal & Gibson lineage) applied to bipolar disorder in AoU — social
risk as the E in G×E is the phenotype-diverging move worth reading in
full. Chen Y, McMurry A, Gottlieb D, Jones JR, Strober BJ et al.
— *Sharing Aggregated Patient Counts in Place of Line-Level EHR Data:
Analytic Fidelity and the Limits of Count Suppression for Privacy.*
medRxiv 2026 (Hripcsak new-related feed). **Directly relevant to the
AoU Data & Statistics Dissemination Policy** (count suppression) that
constrains every AoU analysis you and your team produce; the
Interoperability / representational-consequences sub-thread (Lemieux
lineage) under `Knowledge representation in EHRs` gets its
count-suppression audit paper.

**Cystic fibrosis / CFTR direct-thread cluster (2 items).** Wyatt MKL,
Raraigh KS, Faino AV, McGarry ME — *Variants of Varying Clinical
Consequence (VVCCs) in children with CRMS/CFSPID.* J Cystic Fibrosis
2026 (Zeng self-feed). Direct hit on the **CFTR variant-interpretation**
subarm — the CRMS/CFSPID inconclusive-newborn-screen population is
exactly where VVCC (formerly VCC) evidence gets weighed against ACMG /
ClinGen CFTR-VCEP criteria. Menditto VG et al. — *Prenatal CFTR
modulator therapy and fetal meconium ileus in CF: systematic review +
IPD meta-analysis.* J Cystic Fibrosis 2026 (Zeng self-feed). Perfectly
overlaps two active sub-threads: **CFTR modulator pharmacoepi** and the
**early-pregnancy time-zero-selection problem** from Wood et al.
(08-17 report). Prenatal Trikafta / ivacaftor exposure with fetal
outcome is exactly the target-trial-emulation-in-pregnancy design the
Wood paper is scaffolding.

**Causal-inference + pharmacoepi target-trial-emulation cluster
(3 items).** Launders N, Richards-Belle A, Wu SM, Man KKC et al. —
*Impact of adjunctive dihydropyridine CCBs on mental health outcomes
in severe mental illness: target trial emulation in English EHR.* J
Psychopharmacol 2026 (Pascal Brandt new-related feed). Direct hit on
**EHR-based drug-repurposing signals** (CCBs → mental-health outcomes
is a classic repurposing hypothesis) *and* on the causal-inference
target-trial-emulation methods thread. Lai JH, Avanceña ALV, Cata JP,
Barner JC et al. — *Initiation of Gabapentin with Opioids and Risk of
Respiratory / Cardiovascular / Opioid-Related Adverse Events Following
Surgery for Breast Cancer.* Clin Pharmacol Ther 2026 (Miguel Hernán
citations-to feed). TTE-in-US-claims for a common perioperative
drug-drug combination; template for the CFTR-modulator ×
concomitant-medication safety questions on your watchlist. Chehrazi M,
Seaman S, Cornelius V, Modi N — *PROTECT-Preterm: emulating target
trials of dynamic probiotic strategies for NEC / late-onset sepsis in
very preterm infants.* BMJ Paediatr Open 2026 (Hernán citations-to
feed). **Dynamic-treatment-regime TTE** with a real-world neonatal
cohort — worth reading purely as a template for dynamic-regime
emulation in EHR contexts (CFTR-modulator dose changes, statin
titration, insulin escalation are analogous dynamic regimes).

**Genetic-epi / PGS-portability cluster (3 items).** Yapp TAJ, Krishnan
M, Liu S, Manna SL, Cheng H et al. — *Variant Harmonization Critically
Determines Polygenic Score Transferability for Lipid Traits in Samoan
Populations.* Hum Genet Genomics Adv 2026 (Karczewski new-related
feed). Anchors the **cross-ancestry PGS portability** subthread with
the underappreciated point that upstream variant harmonization (allele
strand, INDEL representation, multi-allelic normalization) drives more
of the portability gap than the score itself for underrepresented
populations. Zhou G, Yolou I, Xie Y, Zhao H — *Protocol for leveraging
local ancestry and cross-ancestry genetic architecture to improve
polygenic prediction in admixed populations.* STAR Protocols 2026
(Hongyu Zhao new-articles feed). STAR Protocols is a step-by-step
methods venue — this is directly usable as the local-ancestry-aware
PGS recipe for any AoU-admixed analysis you're building. Guo X, Hu J,
Tian H, Yan C, Liu Q et al. — *Trans-ancestry meta-analysis of GWAS
identifies eight novel genetic loci in type 1 diabetes.* Diabetic
Medicine 2026 (Karczewski new-related feed). Novel T1D loci from a
trans-ancestry sweep; feeds both the **GWAS / genetic epi** thread and
future T1D-PGS × exposure analyses.

**Variant interpretation / rare-disease infrastructure cluster
(2 items).** Ma J, Weisburd B, DiTroia S, Romo L, Covill LE et al. —
*Long-read RNA sequencing improves isoform and splicing outlier
detection in whole blood from rare disease trios.* medRxiv 2026
(Karczewski + Montgomery new-related feeds, dual hit). Directly serves
the **splicing / RNA evidence for VUS resolution** subarm of
`Variant interpretation (ACMG / ClinGen)`; whole-blood LR-RNA-seq is
exactly the modality that gets a splice-altering VUS reclassified from
VUS to Likely-Pathogenic under PS3-splicing evidence. Radivojac P
— *Resolving variants of uncertain significance at scale with
calibrated computational and experimental evidence.* Book of Abstracts,
6th Belgrade Bioinformatics Conf 2026 (`mendelian diseases` keyword
feed). Framing talk by Radivojac (co-author of MutPred / calibrated
in-silico prediction lineage) on scaling VUS resolution with
*calibrated* prediction + experimental readouts — the calibration
angle bridges the **variant interpretation** thread to the
**ML for precision health** calibration sub-thread.

**LLM + KG + clinical-agent bridging cluster (2 items).** Keloth VK,
Ren Y, Bhattarai K, Xu H — *Evolution of LLMs for Clinical Information
Extraction: A Comparative Study of GPT and Llama Models.* IEEE ICHI
2026 (Hua Xu new-articles feed). Direct hit on the
**NLP / LLM extraction from clinical notes for phecode / HPO
assignment** subarm of `EHR phenotyping & OMOP`; Xu's group at Yale is
central to the clinical NLP benchmark canon so the GPT-vs-Llama
comparison anchors the model-choice question for future computable-
phenotype work. Mumtaz U, Noor A, Ahmed A — *Grounding Healthcare LLMs
in a Causal Knowledge Graph: Framework, Metrics, and a Cardiovascular
Pilot.* arXiv 2608.15382 2026 (Zhiyong Lu new-related feed). Three-way
bridge across **`Knowledge graphs & ontologies`** ×
**`Causal inference and pharmacoepidemiology`** ×
**LLM-clinical-agent** — the exact "LLM-does-mechanical, human-owns-
assumptions" division of labor that egg-computation (08-17 report) also
lives on. Read alongside Vossler et al. (egg-computation) and
Chou/Kallus (`oci-agent`) as the third leg of the causal-KG LLM stool.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-17 → 2026-08-26)

#### METHODS-WATCH — Moriña D. *Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions.* arXiv 2608.16537v1 (stat.ME, 2026-08-17). Score 1.

Bayesian causal count model in which season-specific affine transformations
map calendar time to a latent epidemic clock, with intervention effects
estimated on that clock rather than on the calendar week. The alignment is
a model component (not a preprocessing step), so timing uncertainty
propagates into every causal contrast. Uses negative-binomial observation,
hierarchical area / season / area-season effects, shrunk Fourier epidemic
curve, and posterior g-computation to yield prevented cases, prevented
fractions, peak attenuation, and epidemic displacement. Illustrated on
Catalan primary-care RSV immunisation data. **Bookmark for the
`Causal inference and pharmacoepidemiology` thread** — seasonally
recurrent respiratory infections in CF (Pseudomonas exacerbations,
RSV / influenza vaccine effect) are exactly the setting where calendar-
week-aligned ITS analyses over-report or under-report intervention
impact depending on which season the intervention landed in.

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. *Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.* arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1.

Bayesian causal mediation framework based on enriched Dirichlet process
mixture models + scalable G-computation for zero-inflated longitudinal
outcomes with treatment non-compliance and multiple longitudinal
mediators. Applied to a large US-retailer promotional-email campaign to
compare value-added incentives (free shipping) vs. price discounts.
Off your primary biomedical thread (retail marketing example), but the
**zero-inflated-longitudinal + non-compliance + multi-mediator**
machinery is directly portable to (a) longitudinal CHIP / LOY clonal-
fraction analyses (zero-inflated, longitudinal, with medication and
somatic-mutation mediators), and (b) medication-adherence-mediated
effect decomposition (statin, GLP-1 RA, CFTR-modulator persistence as
mediators of hard clinical outcomes). Bookmark alongside Bandreddi et
al. Tobit-vs-hurdle (08-17 report) for the zero-inflated-longitudinal
methods shortlist.

#### METHODS-WATCH — Daza EJ. *A Primer on Digital Health N-of-1 Studies and Single-Case Designs.* arXiv 2608.15526v1 (stat.AP, 2026-08-16). Score 1.

Book-chapter-style primer on **n-of-1 designs, single-case designs, and
digital-health "multitudinal" approaches** that characterize a single
person's recurring health patterns rather than borrowing subgroup
averages. Coins "esametry" for the statistics of within-person digital
signals. Directly serves the **`Machine learning for precision health`**
thread's individualized-decision framing, and the **digital-twins-from-
EHR** rising sub-thread (INTERESTS.md line ~117). Read if extending
into individualized-trajectory-prediction work with continuous
wearable / CGM / smartphone-EMA streams on top of AoU / UKB imaging or
proteomic layers.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. *Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.* arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1.

Illustrates that in longitudinal settings with **staggered treatment and
heterogeneous treatment effects**, the constant-treatment-effect
estimator can be a weighted average (with negative weights) of
heterogeneous effects across treatment durations — so the constant
estimate and per-duration heterogeneous estimates disagree. Shown for
linear *and* logistic link with drug-induced-homicide prosecutions →
overdose deaths in the US. **Reference paper for anyone running
staggered-adoption TTE with logistic outcomes in EHR** — the analog
here is any policy-adoption or drug-launch analysis where sites /
regions turn treatment on at different times (CFTR-modulator
availability across CF care centers is a canonical example). Slot
alongside the Callaway-Sant'Anna / de Chaisemartin-D'Haultfœuille
staggered-DiD lineage.

#### SKIP — Banaszewski B, Fitzgibbon AW. *Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference.* arXiv 2608.18982v1 (cs.LG, 2026-08-19). Score 1.

1.61B-parameter molecular FM with PM6 pretraining and TabPFN-based
in-context prediction; strong on Polaris and activity-cliff benchmarks.
Off your active EHR / phenotyping / pharmacoepi threads; note only in
case the drug-repurposing chemistry-only pipelines re-enter your
attention.

#### SKIP — Machacuay C, Lincovil J, Rojas H. *Mayoral Experience or Municipal Capacity? Negative-Outcome Evidence on Municipal Budget Execution in Peru.* arXiv 2608.18354v1 (stat.AP, 2026-08-18). Score 1.

Panel double ML on Peruvian district municipalities. Off-thread; the
negative-outcome-control identification move is pedagogically clean
but the Reho et al. Pharmacoexposomics + Chen et al. count-suppression
audits are higher-signal reads for the same time budget.

#### SKIP — Yao Y, Zhang N, Graham DJ. *Quantifying the Causal Operational Determinants of Service Reliability in Urban Rail Transit: Evidence from Panel Double/Debiased Machine Learning.* arXiv 2608.17901v1 (stat.AP, 2026-08-18). Score 1.

Panel DML on 46 international metro operators. Off-thread transit
economics; nothing to import.

#### METHODS-WATCH — Leimenstoll L, Schienle M. *Identification and Inference for Causal Effects in Extremes under General Conditions.* arXiv 2608.22957v1 (stat.ME, 2026-08-24). Score 1.

Causal Tail Coefficient (CTC) extended to allow heterogeneous tail
indices and heavy-tailed confounders in a linear structural causal
model with regularly-varying innovations. Shows how differences in
tail behavior can identify causal structure; derives asymptotic
inference and tests for causal direction / heavy-tailed confounding.
Illustrated on climate and financial extremes. Off your primary
biomedical thread but the **"extreme-event as a distinct causal
estimand"** framing is worth bookmarking for any biomedical extreme-
value work (e.g., extreme HbA1c excursions, sepsis-onset physiology,
rare adverse-event tails).

#### SKIP — Wang Z, Tang B, Zhang F, Han S, Liu P. *RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling.* arXiv 2608.22849v1 (cs.LG, 2026-08-24). Score 1.

1.61B-parameter RNA FM with 10,240-nt native context; SOTA on
frozen-representation RNA type classification and mRNA generation.
Off your EHR / clinical thread. Note only if a future project touches
transcript-level rare-variant scoring where the model backbone matters.

### NCBI PubMed My-NCBI alerts — 'All of Us' saved search (08-26 batch, 4 articles)

#### HIGH — Zhang J, Hong SH, Wang X, Jurgens SJ, Liu CT, Dupuis J, Ellinor PT, O'Connor GT, Mei Q, Choi SH. *Transcript-aware rare genetic variant association analyses of cardiopulmonary traits in participants from the All of Us Research Program.* Nat Commun 2026;17:9038. PMID 42642362.

**Direct-hit AoU rare-variant paper** from a cardiopulmonary-genetics
team with Ellinor senior authorship. Transcript-aware collapsing (vs.
gene-level) is the specific methodological move worth reading in full:
which transcript is "canonical" changes the burden-test result more
than pipeline authors usually admit, and AoU short-read WGS is the
right substrate to demonstrate that. Cross-thread hit on
**`PheWAS / phecode infrastructure`** (cardiopulmonary traits ≈
respiratory + circulatory phecodes), **`Biobanks with EHR linkage`**
(direct AoU methods), and **`Genetic epidemiology`** (rare-variant
burden). Read for: (1) the exact transcript-selection rules
(APPRIS / MANE Select / GENCODE basic), (2) whether they report
transcript-choice sensitivity as a supplementary figure, (3) whether
they release the transcript-aware collapsing code as an AoU-workbench-
compatible package, (4) how they handle the AoU short-read WGS
callset's known false-negative rates in structural regions.

#### HIGH — Sharp RR, Hysong M, Mealer RG, Raffield LM, Glover L, Love MI. *Considering social risk alongside genetic risk for bipolar disorder in the All of Us Research Program.* HGG Adv 2026:100665. PMID 42642929.

Direct hit on the **PGS × exposure / environment interactions** rising
sub-thread (Nagpal & Gibson lineage) — with **social** risk as the E.
AoU's social-determinants survey layer is exactly the substrate this
kind of composite-risk-with-environment work needs. Notable authorship:
Raffield (NHLBI TOPMed genetics), Love (RNA/statistics). Read for:
(1) which SDoH variables enter as E (income, education, area
deprivation, discrimination), (2) how they handle the PGS × SDoH
non-independence (ancestry stratification is a confounder for both),
(3) whether they estimate GxE beyond a linear interaction term
(RERI / additive-scale interaction preferred for public-health-
translatable claims), (4) any decomposition of GxE by ancestry group
(within-ancestry GxE is more interpretable than trans-ancestry). This
paper should slot alongside Nagpal & Gibson (Nat Genet 2026, PGS ×
exposure pervasiveness) as citable references for the composite-risk
framing of INTERESTS.md.

#### MEDIUM — Chaochao P, Yunyun G, Meimei X, Hong L, Guoxuan N. *Associations between sense of agency and psychotic symptoms in patients with schizophrenia: A network analysis.* Acta Psychol (Amst) 2026;270:107703. PMID 42641581.

Not an AoU paper — likely a false-positive PubMed hit on the phrase
"all of us" in the abstract text. Off-thread; skip.

#### MEDIUM — Halder R, Warshel A. *On the origin of the ionic strength control of the motility of kinesin-14.* PNAS 2026;123(35):e2618972123. PMID 42640789.

Not an AoU paper; molecular-motor biophysics. False-positive PubMed
hit. Off-thread; skip.

### NCBI PubMed My-NCBI alerts — 'UK Biobank' saved search (08-26 batch, 17 articles)

#### MEDIUM — Charoenngam N, Huerta-Chagoya A, Hsu S, Vora M, Mercader JM, Udler MS, Mannstadt M. *Genotype-First Characterization of Familial Hypocalciuric Hypercalcemia Type 1: Prevalence, Serum Calcium and Clinical Associations.* J Bone Miner Res 2026;zjag129. PMID 42640938.

**Genotype-first characterization of a Mendelian trait in UKB**
(FHH type 1, CASR) with Udler / Mercader (MGH T2D genetics) among the
authors. Same methodological family as the penetrance-under-
population-screening work on INTERESTS.md line ~24 (PheWAS / phecode
sub-thread). Read if extending into monogenic-calcium-metabolism
penetrance work; otherwise a template paper for future genotype-first
studies. Bumps to HIGH if you re-activate the CASR / calcium-sensing-
receptor sub-thread.

#### METHODS-WATCH — Koh HB, Kim HJ, Heo SJ, Park CH, Kim HW, Joo YS, Chang TI, Park JT, Yoo TH, Kang SW, Han SH. *Plasma Levels of Growth Differentiation Factor 15 and Adverse Kidney Outcomes: Proteomics-Based Mediation Analysis and Mendelian Randomization.* Clin J Am Soc Nephrol 2026. PMID 42640732.

**Proteomics-based mediation analysis + MR on UKB Olink data**,
GDF-15 → adverse kidney outcomes. Directly serves the
**Multi-omics-augmented PRS** rising sub-thread (INTERESTS.md line
~78) — Olink NMR / proteomics-mediated MR on cardiometabolic traits
is exactly this design. Compare with Shan et al. UKB 2026 (multi-
omics-augmented PRS) already on the reading list. Read for:
(1) whether they include APOL1 stratification given kidney outcomes,
(2) the MR instrument (cis-pQTL preferred), (3) their handling of
Olink batch effects across the UKB expansion.

#### METHODS-WATCH — Maldonado-Garcia C, Salih AM, Neubauer S, Petersen SE, Raisi-Estabragh Z. *Distinct relationships of compartment-specific fat distribution profiles with cardiovascular ageing and future cardiovascular events.* Heart 2026. PMID 42642077.

**UKB CMR + fat-compartment segmentation** for CV outcomes. Peterson /
Neubauer lineage (canonical UKB CMR authors). Adjacent to the
imaging-FM subthread already flagged in 08-17 report (CAN-FLOW paper).
Read for cross-reference if extending imaging-FM work on cardiac data.

#### METHODS-WATCH — Luo J, Wang Y, Tan Z, Bai G, Sun L, Liu Y, Li R, Ke J, Zhang J. *Integrated Assessment of Abdominal Adiposity and Muscle Strength for Atherosclerotic Cardiovascular Disease Risk in UK Biobank: A Comprehensive Analysis From Population Cohort to Multi-Omics Molecular Exploration.* Diabetes Obes Metab 2026. PMID 42642342.

Multi-omics × body-composition analysis in UKB. Standard template but
useful precedent for combining Olink / metabolomics / imaging in a
single risk model — worth a look if the multi-omics-augmented-PRS
sub-thread stays active.

#### METHODS-WATCH — Sun A, Liu H, Yang X, Guo H, Zeng R, Deng Y, Liu Z. *Hemodynamic phenotypes defined by arterial stiffness index and pulse pressure with risk of diabetic microvascular complications in type 2 diabetes.* Front Endocrinol 2026;17:1917833. PMID 42643233.

UKB hemodynamic phenotyping. Off primary methods thread; useful only
if extending T2D microvascular-complication phecode work.

#### MEDIUM — Chen L, Hsieh H, Cheng N, Xu Y. *Genome-Wide Association Summary Statistics-Based Genetic Mapping of Brain Functional and Structural Networks in Type 2 Diabetes Mellitus and Its Complications.* Brain Res Bull 2026;112098. PMID 42641768.

UKB brain-imaging GWAS in T2D. Adjacent to the multi-omics-augmented-PRS
thread but skewed toward imaging genetics; read only if extending into
brain-imaging × cardiometabolic architecture per Kopal et al.
(cross-trait triangulation, INTERESTS.md line ~91).

#### LOW — Huang Y, Li K, Yangybrbi Y, Xu Y, Gu W, Lin M, Shi W, Li J, Yang Y, Wang H. *Cardiovascular-Kidney-Metabolic Syndrome in neurological and psychiatric disorders: a large multi-national cohort study.* Brain Behav Immun 2026;106974. PMID 42641671.

Multi-national CKM-syndrome × neuropsychiatric outcome cohort study.
Descriptive; off methods thread. Note only for the CKM-syndrome
phenotype definition if it becomes relevant.

#### LOW — He X, Liang J, Ouyang Y et al. *Association between the planetary health diet and sleep disorders: results from the UK Biobank.* Psychiatry Res 2026;365:117415. PMID 42641305.

Dietary-pattern × sleep-disorder observational analysis. Off methods
thread.

#### LOW — Li J, Chen J, Qiu W, Han D, Wang K, Gao W, Chen A. *Association of hemoglobin glycation index with the risk of chronic lung disease in individuals with CKM stages 0-3: evidence from two large prospective cohorts in Europe and East Asia.* Diabetes Res Clin Pract 2026;113523. PMID 42641803.

Hemoglobin glycation index × chronic lung disease. Off methods thread;
noted only for the CKM-staged design.

#### LOW — Zhang X, Yan W, Fan X, Zhang P, Gao Y, Wang Y, Shen H, Cai C, Zeng S, Zhu J. *Proteomic health archetypes identified in disease-free adults enable risk assessment for diverse chronic diseases.* Genome Med 2026;18(1):128. PMID 42304423.

Latent-class / archetype clustering of UKB Olink proteomes for cross-
disease risk. Adjacent to the **Chronic disease clustering and
multimorbidity** thread but on proteomic space rather than diagnosis
space — worth reading if extending multimorbidity work into biomarker-
defined subtypes.

#### LOW — Zhai Z, Lv Y, Li P, Zhang Y, Li L, Wang P, Suo X, Ding J, Ye F, Bo Y, Wang L, Wang Y. *Physical frailty and the risk of peripheral vertigo: evidence from the UK Biobank cohort.* Front Neurol 2026;17:1910905. PMID 42643260.

Frailty × vertigo association study; descriptive. Off-thread.

#### LOW — Zhu X, Xia H, Sun T, Wang X. *Weekend Warrior Physical Activity, Sedentary Behavior, and Incident Disability in Middle-Aged and Older Adults.* Geriatr Gerontol Int 2026. PMID 42642715.

Activity-pattern × disability study. Off-thread.

#### LOW — Qiao X, Yu D, Guo L, Pan Q. *The impact of new obesity definitions on prevalence and health outcomes.* Diabetes Res Clin Pract 2026;113522. PMID 42641806.

Definitional-comparison paper. Off methods thread.

#### LOW — Yang W, Chen Z, Zhang Y, Peng C, Chen B. *Flavonoid-rich dietary patterns and incident hospital-recorded Parkinson's disease: a prospective UK Biobank study.* Front Nutr 2026;13:1893517. PMID 42638917.

Diet × PD observational. Off-thread.

#### LOW — Liu L, Chen K, Liu D, Chen J, Yang S, Yao S, Li Z, Yang J, Chen N. *Association between long-term ambient air pollution and incident inflammatory bowel disease across levels of adherence to a plant-based diet.* Front Nutr 2026;13:1893740. PMID 42638808.

Air-pollution × diet × IBD interaction. Tangential hit on the
**IBD disease thread** — worth a skim only if extending environmental-
exposure × PGS × IBD work.

#### LOW — Fu X, Li X, Ma X, Wu N, Ni W, Li H. *A lifestyle-driven inflammatory load index and its circulating metabolomic signature identify susceptibility to hospital-recorded acute respiratory infections.* Front Endocrinol 2026;17:1878728. PMID 42638794.

Lifestyle-inflammatory index + metabolomics. Off methods thread.

#### LOW — Kong S, Xu S, Wu S, Kou C, Bai W. *Relationship between mobile phone use and multidimensional frailty: evidence from UK Biobank.* Front Public Health 2026;14:1868178. PMID 42638665.

Digital-behavior × frailty. Off-thread.

### Google Scholar author-feed alerts (08-25 23:33Z batch)

#### HIGH — Chen Y, McMurry A, Gottlieb D, Jones JR, Strober BJ et al. *Sharing Aggregated Patient Counts in Place of Line-Level EHR Data: Analytic Fidelity and the Limits of Count Suppression for Privacy.* medRxiv 2026 (George Hripcsak new-related feed).

**Directly relevant to AoU workbench operations** — count suppression
under the AoU Data & Statistics Dissemination Policy is the exact
regime this paper is auditing. Cross-cuts three INTERESTS.md sub-
topics: (a) **Interoperability standards and their representational
consequences** (Lemieux et al. JAMIA Open lineage, INTERESTS.md line
~159), (b) the **`Federated / privacy-preserving EHR causal
analytics`** rising sub-thread under `Causal inference and
pharmacoepidemiology`, and (c) practical operational relevance to the
count-suppression constraint you and Bennett Waxse encode in AoU
Verily Workbench cohorts. Read full-text for: (1) which analytic
tasks tolerate cube-aggregation with threshold suppression vs. break
under it (regressions with continuous covariates? Cox with time-
varying strata? PheWAS-scale scans?), (2) whether they benchmark the
AoU Data & Statistics Dissemination Policy specifically (threshold
= 20) or use their own thresholds, (3) their suggested remediation
patterns (differential privacy + synthetic-data alternatives).
**Cite this paper any time you have to defend a count-suppressed AoU
analysis in a methods review** or explain the fidelity loss to a
collaborator.

#### HIGH — Yapp TAJ, Krishnan M, Liu S, Manna SL, Cheng H et al. *Variant Harmonization Critically Determines Polygenic Score Transferability for Lipid Traits in Samoan Populations.* Human Genetics and Genomics Advances 2026 (Konrad Karczewski new-related feed).

Pinpoints **variant harmonization** (strand ambiguity, INDEL
representation, multi-allelic normalization, effect-allele alignment)
as an underappreciated driver of PGS non-portability in
underrepresented populations. Fits the **cross / trans-ancestry
portability** thread (INTERESTS.md line ~74) with a rare Pacific-
Islander focus — Samoan populations are one of the least-represented
ancestry groups in reference PGS training. Read for: (1) which
harmonization step (strand vs. INDEL vs. multi-allelic vs. effect-
allele) contributes most of the transferability gap, (2) whether they
release a portable harmonization QC pipeline, (3) whether the analysis
extrapolates to other Pacific / Indigenous populations. Portable
lesson: any AoU-multi-ancestry PGS work should audit the same
harmonization steps before attributing residual gaps to genetic-
architecture differences.

#### HIGH — Guo X, Hu J, Tian H, Yan C, Liu Q et al. *Trans-ancestry meta-analysis of genome-wide association study identifies eight novel genetic loci in type 1 diabetes.* Diabetic Medicine 2026 (Konrad Karczewski new-related feed).

Novel T1D loci from a trans-ancestry GWAS. Adds targets to the
**GWAS / genetic epi** thread and, given the T1D × early-onset-
autoimmune-disease context, is worth bookmarking for any future
T1D-PGS × exposure work in AoU (T1D is under-represented on the
type-2-heavy pharmacoepi drug lists).

#### HIGH — Ma J, Weisburd B, DiTroia S, Romo L, Covill LE et al. *Long-read RNA sequencing improves isoform and splicing outlier detection in whole blood from rare disease trios.* medRxiv 2026 (Konrad Karczewski + Stephen Montgomery new-related feeds, dual hit).

**Whole-blood long-read RNA-seq for rare-disease trios** — directly
serves the **splicing / RNA evidence for VUS resolution** subarm of
`Variant interpretation (ACMG / ClinGen)` (INTERESTS.md line ~66).
LR-RNA-seq resolves isoform switches and cryptic splice events that
short-read RNA-seq only imperfectly detects, so PS3-splicing evidence
under ACMG becomes tractable at population scale. Dual authorship
signal (Karczewski's gnomAD lineage + Montgomery's RNA-QTL lineage)
means this will become a canonical reference for splicing evidence
in variant-classification work. Read for: (1) the sequencing platform
(PacBio Sequel IIe vs. ONT), (2) the analytic pipeline
(FLAIR / TALON / IsoQuant), (3) sensitivity for splice-altering
intronic variants vs. exonic missense, (4) whether the trio design
recovers de novo splice events that pedigree-uninformed callers miss.

#### HIGH — Zhou G, Yolou I, Xie Y, Zhao H. *Protocol for leveraging local ancestry and cross-ancestry genetic architecture to improve polygenic prediction in admixed populations.* STAR Protocols 2026 (Hongyu Zhao new-articles feed).

STAR Protocols is a step-by-step methods venue — this is the practical
recipe for **local-ancestry-aware PGS in admixed populations**,
directly usable for AoU (where admixed African-American / Hispanic /
Native-American strata make single-ancestry PGS transferability
brittle). Complements Yapp et al. (Karczewski feed, above) — Yapp is
the harmonization audit, Zhou/Zhao is the local-ancestry-aware scoring
recipe. **Download and read side-by-side** as the two portable steps
for the ancestry-aware-PGS pipeline the AoU thread has been waiting
for.

#### HIGH — Launders N, Richards-Belle A, Wu SM, Man KKC et al. *Impact of adjunctive dihydropyridine CCBs on mental health outcomes in severe mental illness: target trial emulation in English EHR.* J Psychopharmacology 2026 (Pascal Brandt new-related feed).

**TTE in English EHR** for a repurposing hypothesis (dihydropyridine
CCBs, e.g., amlodipine, for mental-health outcomes in SMI). Cross-hit
on **`Causal inference and pharmacoepidemiology`** (TTE methods) and
**`Drug repurposing`** (EHR-based repurposing signals sub-thread —
INTERESTS.md line ~178). Man senior authorship is a signal
(pharmacoepi TTE track record). Read for: (1) exposure ascertainment
(dispensing records vs. prescription events), (2) whether they
implement an active-comparator (thiazide? ACE-I?) to control for
confounding-by-indication (hypertensive treatment on top of an
antipsychotic-metabolic-syndrome-associated substrate), (3) primary
outcome definition (relapse via readmission vs. specific psychiatric
phecode), (4) whether they use a negative-outcome control to detect
residual confounding.

#### HIGH — Lai JH, Avanceña ALV, Cata JP, Barner JC et al. *Initiation of Gabapentin with Opioids and Risk of Respiratory / Cardiovascular / Opioid-Related Adverse Events Following Surgery for Breast Cancer.* Clin Pharmacol Ther 2026 (Miguel Hernán citations-to feed).

**US-claims TTE for perioperative gabapentin + opioid co-initiation.**
The FDA-warning-relevant setting (gabapentin + opioid respiratory-
depression) makes this a template for CFTR-modulator × concomitant-
medication safety work (statin + Trikafta, ivacaftor + fluoroquinolone,
etc. — small-cohort settings where TTE with claims is the only
feasible route). Read for: (1) new-user, active-comparator definition
(opioid-alone as comparator), (2) how they handle the perioperative
time-zero (surgery date), (3) sensitivity analyses for competing risks
(cancer-related mortality).

#### HIGH — Chehrazi M, Seaman S, Cornelius V, Modi N. *PROTECT-Preterm: emulating target trials of dynamic probiotic strategies for NEC / late-onset sepsis in very preterm infants.* BMJ Paediatr Open 2026 (Miguel Hernán citations-to feed).

**Dynamic-treatment-regime TTE** — probiotic strategy is a dynamic
regime (start / stop / switch by clinical trigger), and very-preterm
neonatal cohorts are exactly the setting where a randomized trial is
ethically hard. Reference paper for anyone building a dynamic-regime
TTE in EHR contexts: CFTR-modulator dose adjustments, statin titration,
insulin escalation, HRT-formulation switching all follow the same
dynamic-regime pattern. Read for: (1) how they define the regimes
(if-then rules over clinical states), (2) g-computation vs. cloning-
weighting-censoring, (3) sensitivity analyses for compliance-with-
regime, (4) whether they release the simulation code.

#### HIGH — Wyatt MKL, Raraigh KS, Faino AV, McGarry ME. *Variants of Varying Clinical Consequence (VVCCs) in children with CRMS / CFSPID.* J Cystic Fibrosis 2026 (Chenjie Zeng self-feed).

**Direct-hit CFTR variant-interpretation paper.** CRMS (CFTR-Related
Metabolic Syndrome, US) / CFSPID (CF Screen-Positive Inconclusive
Diagnosis, international) is the inconclusive-newborn-screen
population where VVCC-classified variants (formerly VCC) dominate.
Raraigh is a canonical CFTR-VCEP author. Cross-hit on the
**variant-interpretation (ACMG / ClinGen)** thread and the
**CF / CFTR** disease thread. Read for: (1) how VVCC classification
correlates with progression to CF phenotype in a longitudinal cohort,
(2) whether they benchmark VVCC vs. CFTR2-database-based
classification, (3) implications for prenatal / newborn counseling
(where the VVCC label itself creates ambiguity), (4) any signal about
which specific VVCC variants (e.g., R117H-7T, 5T-TG12) drive most of
the CRMS / CFSPID caseload.

#### HIGH — Menditto VG et al. *Prenatal CFTR modulator therapy and fetal meconium ileus in CF: systematic review + IPD meta-analysis.* J Cystic Fibrosis 2026 (Chenjie Zeng self-feed).

**Direct-hit CFTR-modulator × prenatal-exposure paper.** IPD meta-
analysis of published prenatal ivacaftor / Trikafta cases with fetal
meconium ileus as outcome — the flagship "does maternal modulator
therapy rescue in-utero CF pathology?" question. Cross-hits three
INTERESTS.md areas: **CF / CFTR pharmacoepi**, the
**early-pregnancy time-zero-selection problem** from Wood et al.
(08-17 report), and the **PGS × exposure / environment interactions**
framing (in-utero pharmacological exposure as the E). Read for:
(1) how they handle the immortal-time bias inherent to case-report
ascertainment (fetuses ascertained because they didn't die), (2) the
denominator problem (published cases are a biased sample), (3) any
subgroup analysis by CFTR genotype (F508del/F508del vs. gating
mutations vs. VVCCs), (4) whether they address the LR-RNA-seq splicing
evidence layer for the modulator-response-predicting variants.

#### HIGH — Xie Q, Zhang J, Wang Y, Huang J, Lin F, Weng RL et al. *CiteSure: retrieval-augmented large language models for faithful biomedical citation recommendation.* JAMIA 2026 (Tiffany J. Callahan new-related feed).

RAG framework against LLM biomedical citation hallucination.
Complement to the LLM-clinical-agent thread and directly relevant to
**verified-citation workflows** for grant / manuscript drafting where
LLM hallucinated citations remain a real risk. Read for: (1) the
retrieval index (PubMed? Semantic Scholar? both?), (2) attribution
provenance (does it return the citation with sentence-level source
anchors?), (3) whether the eval measures true citation validity
(does the paper exist? was it correctly cited?). This is a workflow-
tool paper more than a research paper, but if it works well it removes
a real blocker for LLM-drafted methods sections.

#### HIGH — Mumtaz U, Noor A, Ahmed A. *Grounding Healthcare LLMs in a Causal Knowledge Graph: Framework, Metrics, and a Cardiovascular Pilot.* arXiv 2608.15382 2026 (Zhiyong Lu new-related feed) — companion Research-Square framework version also cited.

**Three-way bridge across `Knowledge graphs & ontologies` ×
`Causal inference and pharmacoepidemiology` × LLM-clinical-agent.**
The exact "LLM does mechanical, human owns identification assumptions"
division of labor that Vossler et al. egg-computation (08-17 report)
lives on, but with a KG-grounded reasoning layer instead of Gantt-
chart-based DAG proposal. Read alongside egg-computation and
Chou/Kallus `oci-agent` as the third leg of the causal-KG-LLM stool.
Read for: (1) what causal semantics the KG encodes (Pearl-style
DAG? SWIG?), (2) evaluation metrics (whether they distinguish
retrieval-correctness from causal-reasoning-correctness), (3) the
cardiovascular pilot's specific query set (HTE questions? confounding-
identification questions? both?), (4) whether the framework is
biomedical-domain-agnostic or requires cardiovascular-specific
priors.

#### HIGH — Keloth VK, Ren Y, Bhattarai K, Xu H. *Evolution of LLMs for Clinical Information Extraction: A Comparative Study of GPT and Llama Models.* 2026 IEEE 14th ICHI (Hua Xu new-articles feed).

**Yale-Xu-group GPT-vs-Llama clinical-IE benchmark.** Direct hit on
the **NLP / LLM extraction from clinical notes for phecode / HPO
assignment** subarm of `EHR phenotyping & OMOP` (INTERESTS.md line
~150). Xu's group has been central to clinical-IE benchmarks
(cTAKES, CLAMP, Sheikhalishahi review), so the GPT-vs-Llama comparison
becomes the model-choice anchor for the next generation of computable-
phenotype work. Read for: (1) which clinical-IE tasks (NER? relation
extraction? assertion classification?), (2) which GPT / Llama sizes
and versions, (3) prompt-engineering vs. fine-tuning conditions,
(4) whether open-Llama beats closed-GPT on any task (portability +
reproducibility signal for on-prem clinical NLP).

#### METHODS-WATCH — Radivojac P. *Resolving variants of uncertain significance at scale with calibrated computational and experimental evidence.* Book of Abstracts, 6th Belgrade Bioinformatics Conf 2026 (`mendelian diseases` keyword feed).

Framing talk by Radivojac (MutPred / calibrated in-silico prediction
lineage). Abstract-only, but the **"calibrated evidence"** move —
integrating in-silico scores with experimental readouts under a
Bayesian calibration umbrella — is the framework worth citing for
VUS-resolution work. Read the full talk / paper if extending into the
ACMG-thread calibration subarm; slot alongside PhenoSV / AlphaMissense
calibration audits.

#### METHODS-WATCH — Kespechara K, Mingkhwan A. *Multi-source Knowledge Graph RAG for LLM-Based Medical Diagnosis.* Int'l Conf on AI in Healthcare 2026 (Zhiyong Lu new-related feed).

Multi-source KG + RAG for medical diagnosis LLMs. Bookmark for cross-
comparison with Mumtaz et al. above; useful only if extending
diagnostic-agent work in the LLM-clinical-agent thread.

#### METHODS-WATCH — Mumtaz U, Noor A, Ahmed A. *Framework for Grounding Healthcare LLMs in a Causal Knowledge Graph: A Cardiovascular Example.* Research Square 2026 (Zhiyong Lu new-related feed).

Companion / longer version of the arXiv paper above. Read whichever
has the more detailed evaluation section.

#### METHODS-WATCH — Denos M, Bhatta L, Medici M, Teumer A, Brumpton B et al. *Investigating the effects of maternal thyroid hormones on offspring cardiometabolic risk factors in adulthood: an intergenerational Mendelian randomization study.* Eur J Endocrinology 2026 (Joshua C. Denny new-related feed) — conference abstract.

**Intergenerational MR** for maternal thyroid → offspring
cardiometabolic outcome. Adjacent to the **drug-target MR** rising
sub-thread (INTERESTS.md line ~64); the intergenerational design is a
newer wrinkle worth watching. Read for the design template if
extending into maternal-exposure × offspring-outcome MR work.

#### METHODS-WATCH — Choi KH, Lee SH, Kim SM, Hong D, Lee SY, Lee JM et al. *SGLT2 inhibitor on infarct size and LV remodeling by CMR in patients with AMI.* Cardiovascular Interventions (JACC) 2026 (Patrick Ryan new-related feed).

RCT / prospective CMR study of SGLT2i on infarct / LV outcomes.
Directly relevant to the **SGLT2i pharmacoepi** drug-class watchlist
(INTERESTS.md line ~48); the CMR-outcome design is a template for
cardiac-imaging-endpoint TTE studies. Read as a comparator when
writing the SGLT2i pharmacoepi section of any AoU / UKB analysis.

#### METHODS-WATCH — Ahmad WA, Sagy YW, Arbel R, Battat E, Dicker D et al. *Comparative risks of dementia and Parkinson's disease with GLP-1 RAs versus other oral glucose-lowering medications in obese patients with T2D: a large real-world cohort.* Eur J Internal Medicine 2026 (Patrick Ryan new-related feed).

**GLP-1 RA vs. other OGLM active-comparator new-user design** for
neurological outcomes. Direct hit on the **GLP-1 RA pharmacoepi**
drug-class watchlist and on the emerging GLP-1-and-brain-outcome
literature. Read for: (1) exposure definition (any GLP-1 RA vs.
semaglutide-specific vs. tirzepatide-included), (2) comparator choice
(SU vs. DPP-4i vs. broad OGLM), (3) whether they use active-comparator
new-user design with propensity trimming, (4) how they handle the
weight-loss mediator (weight-loss-mediated vs. direct pharmacologic
effect on cognition).

#### METHODS-WATCH — Gao Z, Sun Y, Wang H, Jiang R, Liu Q. *RegFM: interpretable context-aware foundation model for human transcriptional regulation.* bioRxiv 2026 (Marinka Zitnik new-related feed).

Transcriptional-regulation FM. Off primary EHR-FM thread but useful
as an example of **interpretable / context-aware FM** architecture
(a critique-of-black-box angle that reads well against the CLMBR /
MOTOR canon).

#### METHODS-WATCH — Lyu T, Zhuang X, Ding K, Cao X, Liang L, Zhao W et al. *Knowledge Graph-Enhanced Long-CoT for Complex Biomolecular Reasoning.* KDD 2026 (Marinka Zitnik new-related feed).

KG-enhanced long-chain-of-thought reasoning for biomolecular
questions. Adjacent to Mumtaz et al. above but on the biomolecular
(vs. clinical-causal) side. Bookmark for the KG-CoT stack.

#### METHODS-WATCH — Li J, King Z, Sano A. *Digital Phenotyping for At-Risk Identification in Opioid Use Disorder.* IEEE-EMBS BSN 2026 (Pascal Brandt new-related feed).

Digital-phenotyping-from-smartphone-sensor for OUD risk. Adjacent to
the **`Machine learning for precision health`** thread; useful only
if extending into passive-sensing digital-phenotyping work.

#### METHODS-WATCH — Ahmed S. *Incorporating automated phenotyping strategies to identify genes, pathways and cells involved in age-related hearing loss.* Thesis, 2026 (Denny / Hripcsak citations-to feeds, dual hit).

PhD thesis on automated phenotyping applied to age-related hearing
loss with an AoU chapter. Downgrade to LOW unless auditing the AoU
methods section for reference; more of a citation-count signal than
a primary read.

#### MEDIUM — Hu C, Yang G, Xiong H, Xie Y, Yuan Z, Liu J, Wang P et al. *From Germline Variants to Tumor Outcome: GWAS-Based Functional Genomics Prioritizes Colorectal Cancer Susceptibility Genes and Links SMAD9 to Prognosis.* Human Mutation 2026 (Karczewski + Chenjie Zeng + Bastarache + Jian Yang new-related feeds — QUADRUPLE hit).

**Quadruple-feed hit** = strong network signal (cross-cited across
multiple canonical genetic-epi authors). Germline PGS × CRC tumor
outcome, prioritizes SMAD9. Downstream of Chenjie Zeng's CRC lineage.
Read only if reactivating the CRC epidemiology arm; otherwise flag
as a network-density event and move on.

#### MEDIUM — Huangfu Y, Sørensen TIA, Beltrán-Sánchez H, Guo H et al. *Temporal association between body weight and type 2 diabetes at the population level.* Communications Medicine 2026 (Bastarache + Denny citations-to feeds, dual hit).

Population-level temporal weight × T2D. Standard descriptive analysis;
cited from a Bastarache PheWAS pleiotropy paper. Off primary methods
thread.

#### MEDIUM — ter Kuile AR, Mitchell BL, Lee SH et al. *Genome-wide genetic overlap between fear-based disorders and generalised anxiety disorder.* Molecular Psychiatry 2026 (Bastarache + Denny citations-to feeds, dual hit).

Genetic-overlap analysis; cites SAIGE. Off active thread; note as a
downstream SAIGE-use example.

#### MEDIUM — Groot A, Karimian K, Rechsteiner A, Greider CW. *Nanopore sequencing measures chromosome end-specific telomere lengths in human cells.* bioRxiv 2026 (Chenjie Zeng self-feed).

Nanopore telomere-length assay. Adjacent to somatic-mosaicism thread
(telomere shortening is a somatic-aging-marker), but the assay-
development focus is off your methods thread.

#### MEDIUM — Vaaramo M, Kari JT, Korpelainen R, Palviainen T et al. *The Effect of Cardiorespiratory and Muscular Fitness on Healthcare Costs Among Adults: A Triangulation Study.* Med Sci Sports Exerc 2026 (Karczewski citations-to feed).

Triangulation study (observational + MR) for fitness × healthcare
costs. Off primary thread.

#### LOW — Erkan MO, Ercan Emreol H, Dara Kar HD, Sag E, Liu C et al. *A rare RBCK1 mutation–associated infantile-onset Takayasu arteritis-like large-vessel vasculitis: expanding ubiquitination defects.* Rheumatology 2026 (Daniel Kastner citations-to feed).

Rare-disease case series; off active thread. Note only for the
Kastner autoinflammatory lineage.

#### LOW — Park H, Le Bert N, Bertoletti A, Tolwinski N, Gruber J et al. *Sex-specific trajectories of nonlinear immune aging at single-cell level.* Nature Communications 2026 (Stephen B. Montgomery citations-to feed).

Basic-immunology aging paper. Off active thread; note for cross-
reference if extending sex-differential immune-aging work.

#### LOW — Dziubek A, Grimson A. *The Identification and Impact of 3′ UTR Regulatory Variants on Phenotype and Disease.* Annual Review of Genetics 2026 (Denny citations-to feed).

Review of 3′-UTR variant impact; cites gnomAD constraint map.
Reference-only.

#### LOW — Feigin VL et al. *The World Stroke Organization–Lancet Neurology Commission: Pragmatic Solutions to Reduce the Global Burden of Stroke.* Lancet Neurology 2026 (Bastarache citations-to feed).

Global-health policy commission. Off active methods thread; note only
if the stroke-genetics thread is reactivated.

#### LOW — Matsuo K. *Mendelian Randomization Revisited: From Instrument Validity to Epidemiologic Validity.* Journal of Epidemiology 2026 editorial (Denny new-related feed).

Editorial on MR-instrument validity vs. epidemiologic validity. Read
if writing an MR-methods commentary; otherwise skip.

#### LOW — Sinnassamy S, Massiani Beaudoin O, Lombard B et al. *Interactions of LINE-1 ORF1p with proteins and chromatin suggest a role in neuronal physiology.* Life Science Alliance 2026 (Kai Wang citations-to feed).

LINE-1 basic biology. Off active thread.

#### LOW — Zhu X, Zhai C, Li C, Liu R, Mou H, Zhu Y, Luo W et al. *Multi-layered molecular regulation of complex traits in an advanced intercross line.* bioRxiv 2026 (Karczewski + Denny new-related feeds).

Intercross-line eQTL analysis; off human-EHR thread.

#### LOW — Öğütlü H, Dursun O, Esin İ, Erdem H, Tatar A. *Investigation of The Relationship Between ADHD and Mitochondrial DNA Copy Number: One-Year Follow-Up Study.* [Journal TBD] 2026 (Karczewski new-related feed).

ADHD × mtDNA-CN observational. Off thread.

#### LOW — Multiple book-chapter items ("AI in Biomedical Imaging", "AI-Enhanced Drug Discovery and Development", "Revolutionizing Genomics with AI", "Emerging Technologies at the Intersection of AI and Biotechnology", "Transformative AI in Healthcare", "Unlocking Proteomics and Metabolomics Through AI") — mostly from a single 2026 Wiley/Elsevier volume (`fcQEEgAAQBAJ`) that keeps hitting keyword feeds. Not primary science; keyword-feed noise.

### Google Scholar keyword-feed alerts (08-26 08:21Z batch) — additional beyond above

#### METHODS-WATCH — Mining BD. *GraphRAG-ADR: a knowledge graph–enhanced approach for extracting Adverse Drug Reactions (ADRs) from patient narratives.* 2026 (`knowledge graph` keyword feed).

Neo4j-backed KG-RAG for ADR extraction from patient narratives (95,322
nodes, 209,560 edges). Adjacent to the **drug-safety signal detection**
subarm of `Knowledge representation in EHRs and applications`; read
if extending patient-narrative-based drug-safety work.

#### LOW — Fang J, Wang Z, Shao J, Fan J, Luo Q. *Advances in multimodal data integration for drug efficacy prediction: Methodological evolution and clinical translation.* Drug Discoveries & Therapeutics 2026 (`drug repurposing` keyword feed).

Review of multimodal integration for drug efficacy prediction.
Reference-only.

#### LOW — Solomon BI, Munoz AM, Borruso A, Sinaii N, Farhat N et al. *Aspiration and silent aspiration in Niemann-Pick disease type C1: longitudinal findings from the NIH natural history study.* Orphanet J Rare Diseases 2026 (`rare diseases` keyword feed).

NPC1 natural-history observational. Off active thread; noted only for
the NIH natural-history study design template.

#### LOW — Belančić A, Gkrinia EMM, Lam YW, Vitezić D. *Therapeutic Advances in Spinal Muscular Atrophy: A Review of Clinical, Safety, and Economic Considerations.* Frontiers in Pharmacology 2026 (`rare diseases` keyword feed).

SMA therapeutic review. Off active thread.

#### LOW — Renaudineau Y, Hawkes J, Mizgalska K, Natoli V et al. *The private truncating TLR7 p.Glu834* variant associates with juvenile-onset SLE and pathological cytokine expression in vitro.* Annals of the Rheumatic Diseases 2026 (`mendelian diseases` keyword feed).

Private-variant → juvenile-onset SLE. Off active thread; noted as a
functional-validation-of-a-VUS example that could be cited for the
ACMG-thread functional-evidence subarm.

#### LOW — Abujamous L. *Exploring the Breast Cancer Germline and Somatic Mutations Landscape in Qatar.* 2026 dissertation (`variant interpretation` keyword feed).

Regional dissertation on BC germline / somatic landscape. Off active
thread.

---

## What's NOT in the report

- **GitHub `arxiv-digest` cron / PR notifications** — none surfaced in
  Gmail search; the local repo commits and the on-disk `digests/`
  directory serve as the digest artifact.
- **bioRxiv / medRxiv subject-collection alerts** — none surfaced;
  scholar author feeds carried what preprint content there was
  (Ma et al. LR-RNA-seq medRxiv; Chen et al. count-suppression
  medRxiv; Groot et al. nanopore-telomere bioRxiv; Zhu et al. multi-
  layered-eQTL bioRxiv).
- **Nature / Science / Cell direct alerts** — none in window; scholar
  author feeds carried the Nat Commun (Zhang / Ellinor AoU rare-variant
  paper) and Nat Comms (Park et al. sex-immune-aging) hits.
- **arxiv.org daily category mailings** (`no-reply@arxiv.org`) — the
  raw upstream feed that supplies the `arxiv-digest` pipeline; papers
  surfaced via the digest are covered in the arxiv-digest section
  above.
- **NCBI My-NCBI PubMed batches earlier than 08-26** — daily thread
  headlines were retained but individual article lists were not
  re-fetched. If a specific 08-19 / 08-20 / 08-21 / 08-22 / 08-23 /
  08-25 batch matters, request a targeted re-fetch.
- **Substack / newsletters** — none crossed the on-thread threshold
  this window.

## Next steps to consider

1. **Read Zhang / Ellinor AoU rare-variant Nat Commun paper (PMID
   42642362) full-text.** Highest-signal single AoU-methods item this
   window. Extract the transcript-selection rules and the release
   status of the transcript-aware collapsing code so it can be applied
   to CFTR / kidney-phecode / hematology-phecode AoU rare-variant
   analyses on your watchlist.
2. **Read Chen et al. count-suppression medRxiv (Hripcsak feed) and
   bundle with Lemieux et al. JAMIA Open FHIR/USCDI framing paper**
   into a citable methods paragraph for AoU-analytic-fidelity
   discussion in future manuscripts. This is the paper to cite whenever
   a reviewer asks why an AoU analysis reports aggregated
   suppressed counts.
3. **Adopt Zhou / Zhao STAR Protocols local-ancestry-aware PGS recipe
   as the default for AoU-admixed PGS analyses**, and pair with Yapp
   et al. variant-harmonization audit as the two-step ancestry-aware-PGS
   pipeline.
4. **Read Wyatt (CRMS/CFSPID VVCC) and Menditto (prenatal CFTR-modulator
   IPD meta-analysis) back-to-back** as CFTR-thread updates. The
   Menditto IPD meta-analysis is the pregnancy-CFTR-modulator paper the
   Wood et al. TTE tutorial (08-17 report) has been waiting for as an
   applied companion.
5. **Read Launders et al. English-EHR TTE for CCB × mental-health in
   SMI** as a case study for the EHR-based drug-repurposing signals
   subarm — decide whether to write it up as a triangulated methods
   note alongside the Mumtaz KG-LLM paper and egg-computation.
6. **Add Ma et al. LR-RNA-seq rare-disease-trio paper to the variant-
   interpretation reading list** as the canonical splicing-evidence
   modality reference for ACMG PS3-splicing evidence at population
   scale.
7. **Bookmark Keloth / Xu GPT-vs-Llama clinical-IE comparison** for
   the next round of computable-phenotyping model-choice decisions
   (particularly if evaluating open-Llama for on-prem clinical NLP).
8. **Cite Mumtaz et al. causal-KG-grounded-LLM arXiv paper (2608.15382)
   alongside Vossler egg-computation (arXiv 2608.10339) and Chou/Kallus
   oci-agent (arXiv 2607.22443)** as the emerging triad of LLM-assisted
   causal-inference approaches in healthcare.
9. **Bandreddi et al. Tobit-vs-hurdle (08-17 report) + Bhandari et al.
   zero-inflated-longitudinal causal-mediation (08-18 arxiv-digest)**
   now form the zero-inflated-longitudinal methods shortlist for
   CHIP / LOY VAF-trajectory work.

_Report generated 2026-08-26 by scheduled routine; sources Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-26 → next scheduled run._
