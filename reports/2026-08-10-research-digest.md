# Research digest report — 2026-08-10

Triage of research-related email + the GitHub `arxiv-digest` repo against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS-LOY/IBD disease
threads, EHR foundation models, KGs/ontologies, drug repurposing, rare
disease, ML for precision health, multimorbidity, knowledge
representation in EHRs).

Window: **2026-08-08 12:36Z → 2026-08-10 07:30Z** (~2 days since the
2026-08-08 research-digest report, covering two arxiv-digest cron runs,
one NCBI PubMed What's-New batch on 08-09, one Google Scholar keyword
batch on 08-09, and one Google Scholar author batch on 08-10).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-08.md`, `2026-08-10.md`) | 08-08, 08-10 (10:30Z crons) | Both essentially empty: 08-08 surfaced 0 new (8 previously surfaced, suppressed by `seen.json`); 08-10 no matches in the lookback window. 08-09 file absent (weekend cron gap). Quiet upstream weekend at arXiv. |
| NCBI My-NCBI What's-New (08-09 batch) | 08-08 09:15Z → 08-09 07:25Z | Three saved searches fired: "All of Us" (2 hits, 1 on-thread: Hysong et al. AoU SDoH prediction — same paper is the top of Chenjie's own citation feed today), "UK Biobank" (13 hits, 4 on-thread), "drug repurposing" (9 hits, mostly off-thread reviews). |
| Google Scholar keyword feeds (08-09 batch, 08:53Z) | 08-08 → 08-09 | 12 keyword feeds fired: `Cystic fibrosis carriers` (HIGH — CFTR × lifestyle × bronchiectasis), `UK Biobank` (HIGH — UMOD × loop diuretic PGx), `variant interpretation` (MUGO combinatorial optimization), `Foundation models + electronic health records` (Jiang et al. review), `clonal hematopoiesis` (radiopharm therapy → CHIP), `Guidance for estimating penetrance of monogenic ...` (BSGM incidental findings guidance), plus lower-signal `knowledge graph`, `autoimmune diseases`, `rare diseases`, `electronic health records`, `mendelian diseases`, `drug repurposing`, `All of Us research program`. |
| Google Scholar author feeds (08-10 batch, 06:32Z) | 08-09 → 08-10 | 20+ author feeds fired. Densest signal from Bastarache (Olayinka et al. AD PGS × rare variant discovery), Chenjie Zeng (self-citation feed: Hysong AoU SDoH + Xu et al. multi-ancestry PWAS 640k), and George Hripcsak (Onoja et al. multimorbidity trajectory ML). Sub-batch from 08-09 01:11Z: Miguel Hernán (Tirzepatide × ASCVD BMJ), Emily Alsentzer (Aali et al. medical text validation LMs). |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries would include the full
> abstract but this window's runs surfaced no new papers. Author lists
> are truncated to first 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Ten HIGH items surfaced this two-day window, clustering into four knots:

**PGS-as-discovery-instrument cluster (2 items, tightly linked to prior
week's Khan UMOD).** Olayinka et al. *Alzheimer's & Dementia* — AD PGS
stratifies the Alzheimer's Disease Sequencing Project (ADSP) sample to
enrich for novel rare-variant discovery. This is precisely the
*PGS-residuals / PGS-tails as a discovery lever* framing in your
INTERESTS.md — same discovery instrument, in AD instead of last week's
UMOD kidney example. Second, Kreutz et al. *Clin Pharmacol Ther* —
**UMOD** genotype × **loop diuretic** clinical outcomes in a UKB HF
cohort. This is the *pharmacogenomic modifier of medication response*
sub-thread applied to the exact locus Khan et al. medRxiv (last report)
just showed is a monogenic × age × PGS penetrance case study. The
UMOD locus went from "intermediate-penetrance CKD variant with PGS
modification" (Khan) → "cardiovascular drug-response modifier"
(Kreutz) in one week. Bookmark for an UMOD-locus-across-phenotypes
mini-review.

**Multi-ancestry proteomics-as-instrument cluster (1 item, big).** Xu Y
et al. medRxiv 2026 — a proteome-wide association study of 2,594
proteins × cardiovascular diseases in **640,000 multi-ancestry
participants**. Genetically imputed proteomics with a cross-ancestry
protein-QTL framework. Directly serves your multi-omics-augmented PRS
sub-thread and the drug-target MR sub-thread (proteomics + genetics is
the drug-target-MR substrate). Cross-ancestry portability at this N
is a first — read carefully for the imputation-model architecture
(likely a re-worked TWAS/PWAS pipeline with UKB + AoU + probably MVP
proteomics).

**Somatic mosaicism cluster (2 items).** Zeng Z et al. *JACC Advances* —
Mosaic Loss of Y × peripheral arterial and aortic diseases in UKB.
Direct extension of the *LOY as male-specific CHIP analogue* rising
sub-thread (Li et al. *Atherosclerosis* 2026 lineage, Loh *Nature*
2018, Kessler *Nature* 2022). PAD/aortic outcomes match the CHIP
cardiovascular-outcome playbook. Read alongside Liu Q et al. *Clin
Med (Lond)* — CHIP risk factors review — for a paired myeloid/male
somatic mosaicism update.

**CF / CFTR modifier cluster (1 item).** Mikaeeli, Zheng, Li,
Nakanishi et al. *ERJ Open Research* 2026 — CFTR **p.Phe508del**
heterozygote × smoking × alcohol × **bronchiectasis** risk.
Heterozygote-carrier phenotypes are the "how much does one CFTR
variant matter in the general population" question your CF/CFTR
thread has been circling. Design likely UKB (given the Nakanishi
authorship — this is the Greenwood / Nakanishi CF-carrier
epidemiology lineage). Portable framing: penetrance modification of a
monogenic-disease *heterozygote* by exposure, mirroring the
Khan/Olayinka *penetrance modification by PGS* framing above.

**EHR foundation model / phenotyping infrastructure cluster (4
items).** Jiang Y et al. preprints 2026 — "Translating EHR Foundation
Models into Clinical Decision Support" — the translational-pipeline
review you've been waiting for (data resources → model → real-world
deployment). Zhu Y et al. **KDD 2026** — OneEHR "reproducible and AI
agent-ready longitudinal EHR analysis toolkit" — a benchmarking
substrate that competes with MEDS / EHRSHOT. Onoja A et al.
*JAMIA* 2026 — explainable temporal ML of **multimorbidity
trajectories after acute MI** with mechanistic-phenotype overlay: hits
both the multimorbidity-clustering thread and the "ML tied to a
clinical decision" filter. Hysong M R et al. *Communications
Health* 2026 — practical considerations for **SDoH-based disease
prediction in AoU** (PRIMED Consortium; also pinged Chenjie's own
citation feed, worth checking whether Zeng's AoU phenomics paper is
cited).

Plus a genetic-epi methods item: Sun S D et al. **KDD 2026** — MUGO
differentiable combinatorial optimization for causal variant discovery
in the **non-coding genome** (variant-interpretation thread), and a
GWAS-methods item: Qi X et al. *Genetic Epidemiology* — robust
inference with GhostKnockoffs under sample relatedness (background
methods bookmark).

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
by source, then bucket.

### arxiv-digest surfacings (2026-08-08 → 2026-08-10)

No new HIGH / METHODS-WATCH papers this window. 08-08.md reports 0
relevant (8 previously surfaced, suppressed by `seen.json`); 08-10.md
reports 0 matches in the lookback window; 08-09.md was not generated
(the weekend cron sequence has known gaps). Nothing from the
upstream `q-bio.QM / q-bio.GN / q-bio.PE / stat.AP` daily arXiv
mailings crossed the `--min-score 1` net over this weekend. Watch
next Monday's crons for the arXiv Monday-morning backlog dump.

### NCBI My-NCBI What's-New — 08-09 batch

#### HIGH — Zeng Z, Li Y, Li Z, Liu H, Chen B, Wang H, Meng Q, Chen R, Jin L, Yu C, Wang X, Chen J, Li X, Zheng Z. *Mosaic Loss of Y Chromosome and Risks of Peripheral Arterial and Aortic Diseases.* JACC Adv. 2026 Aug 8;5(9):103113. PMID 42570429.

Population-scale LOY × cardiovascular outcomes, extending the
male-specific CHIP analogue thread from myeloid CHIP × cardiovascular
death (Kessler *Nature* 2022) into peripheral arterial + aortic
disease. This is a natural pairing with Li et al. *Atherosclerosis*
2026 (LOY × PAD, already tagged in INTERESTS.md as the seed for the
LOY rising sub-thread) and directly serves the *CHIP / VEXAS / LOY —
somatic mosaicism generally* disease thread. Read for the LOY
detection method (mLRR-Y vs. Loh 2018 mosaic-caller), the
LOY-cell-fraction cutoff, and whether they stratify by smoking (the
canonical LOY confounder). Note: shared surname with Chenjie is
coincidence, not a self-citation ping.

#### HIGH — Liu Q, Yang F, Adami HO, Zhao Y, Wästerlid T, Fang F, Liu Q. *Risk factors of clonal hematopoiesis of indeterminate potential.* Clin Med (Lond). 2026 Aug 8:100635. PMID 42570703.

Risk-factor review for CHIP acquisition (Karolinska group; Fang
lineage). Pairs with the LOY paper above to give a complete
somatic-mosaicism update this week. Read for the ambient-exposure
angle (chemotherapy, radiation, smoking, aging) and whether they
propose CHIP screening thresholds worth adopting in AoU / UKB WGS
scans.

#### HIGH — Qi X, Belloy ME, Gu J, Liu X, Tang H, He Z. *Robust Inference With GhostKnockoffs in Genome-Wide Association Studies With Sample Relatedness.* Genet Epidemiol. 2026 Sep;50(6):e70051. PMID 42569895.

Extends the Ghostknockoffs FDR-controlled association framework to
handle sample relatedness — critical for AoU (extensive family
clusters), MVP, and any founder-population biobank (FinnGen,
Estonian, Sardinia). This is a *methods* item worth tracking for any
future large-cohort GWAS you run — the GhostKnockoffs family (He/Tang
lineage) is emerging as the FDR alternative to LD-clumping + genomic
inflation control.

#### HIGH — Hysong MR, Manning AK, Green MD, Konigsberg IR, Vargas LB, Sharma J, Lange L, Shuey MM, Glover LM, Wojcik GL, Lee S, Raffield LM, Cromer SJ; Polygenic Risk Methods Development (PRIMED) Consortium. *Practical considerations for social determinant-based disease prediction in the All of Us research program.* Commun Health. 2026;1(1):17. PMID 42568450.

PRIMED consortium output. This is the same paper that appears at the
top of Chenjie's own Scholar citation feed today (see below), which
suggests it cites Zeng's AoU phenomic-profile lineage — worth checking
citation graph before deciding whether to read in full. Substantively:
practical guidance on incorporating SDoH into AoU disease prediction
models, likely including calibration-across-subgroups discussion.
Adjacent to your *Machine Learning for Precision Health* thread with a
fairness / calibration angle and to the AoU biobank thread. Note the
Wojcik / Lange / Raffield authorship — this is the same PRIMED cluster
producing the ancestry-aware PGS work.

#### MEDIUM — Trillo-Muyo S, Ermund A, Dolan B, Akyürek LM, Magnusson JM, Hansson GC. *A SNP altering the MUC5AC mucin structure is increased in idiopathic pulmonary fibrosis together with the MUC5B SNP.* Respir Res. 2026 Jul 28;27(1):304. PMID 42571015.

Complements the canonical MUC5B rs35705950 IPF finding with a MUC5AC
structural variant. Adjacent to the CF/CFTR thread as another mucin-
locus × chronic lung disease example. Read only if the CFTR mucin-
biology thread is being reactivated for a manuscript.

#### MEDIUM — Chu S, Casanova F, Bala R, Howes OD, Osimo E, de Marvao A, Ardissino M, O'Regan DP, McIntosh A, Strawbridge RJ, Pillinger T, Tyrrell J. *Effects of Schizophrenia, Bipolar Disorder, and Depression on Cardiopulmonary and Abdominal Organ Structure.* Biol Psychiatry Glob Open Sci. 2026 Jun 29;6(5):100783. PMID 42569312.

Imaging × psychiatric-disorder cohort; UKB-lineage. Adjacent to the
psychiatric-cardiometabolic multimorbidity thread. Read only if the
imaging × biobank × mental-health thread is active.

#### MEDIUM — Wu HY, Hou JH, Huang LY, Tan L, Xu W. *APOE Genotypes Modulate the Relationship of Hypertension With Alzheimer's Disease.* Biol Psychiatry Glob Open Sci. 2026 Jun 22;6(5):100773. PMID 42569203.

APOE × hypertension × AD three-way interaction, mechanistic angle.
Adjacent to the AD PGS × rare variant discovery paper (Olayinka
below), and to the *rare-variant penetrance modified by polygenic /
environmental background* rising sub-thread. Read after Olayinka if
extending an AD-thread report.

#### SKIP — Li J, Hutton GJ, Aparasu RR. *Discontinuation of disease-modifying therapies in older adults with multiple sclerosis.* Mult Scler Relat Disord. 2026 Sep;113:107378. PMID 42435649.

Off-thread (MS-specific pharmacoepi; no genomics or transferable
method).

#### SKIP — Cen L, Tang C, Lin B, Song X, Zhang X, Liu P, Xu C, Yu C. *Hepatocyte VDR protects against cirrhosis-associated bone loss via repression of the FN1/Integrin αv signaling.* J Adv Res. 2026 Aug 8. PMID 42570690.

Off-thread (basic biology, no EHR/biobank/genetic-epi hook).

#### SKIP — Stürmer P et al. *Frailty before disease onset: risk of mortality and chronic conditions in disease-free middle-aged adults.* Geroscience. 2026 Aug 8. PMID 42570190.

Off-thread (frailty epidemiology).

#### SKIP — Pelicioni PHS et al. *Real-world gait changes preceding Parkinson's disease diagnosis in a population-scale UK biobank cohort.* J Neural Transm. 2026 Aug 8. PMID 42570098.

Off-thread (gait / PD).

#### SKIP — Kholeif S et al. *Health profiles and lifestyles of those with cardiomyopathy vs. age-matched controls: a UK Biobank analysis.* Br J Cardiol. 2026 May 5;33(2):022. PMID 42568885.

Off-thread (descriptive lifestyle epi).

#### SKIP — Chen J et al. *Association between Circulating Ketone Bodies and Primary Open-Angle Glaucoma and Related Ocular Parameters.* Ophthalmol Sci. 2026 Jul 6;6(9):101313. PMID 42568854.

Off-thread (ocular).

#### SKIP — Guo J et al. *Independent and combined associations of diabetes and thyroid disorders with risks of incident dementia.* Front Endocrinol. 2026 Jul 24;17:1874555. PMID 42568451.

Off-thread (associational epi; no genomics / method transfer).

#### SKIP — Wei C et al. *Frequency of adding salt to foods, metabolic signature, and the risk of extracoronary atherosclerotic vascular disease progression.* Front Nutr. 2026 Jul 24;13:1870553. PMID 42568408.

Off-thread (nutrition epi).

#### SKIP — 8 further "drug repurposing" search hits (cardiovascular-cancer proteostasis review, EBV × MS pharmacologic hypothesis generation, mGlu5 patent review, hypertension bacterial-target bioinformatics, Alzheimer's anti-neuroinflammatory review, in-silico AMR drug pipelines, TreeScan pharmacovigilance scoping review, mitophagy-astrocyte AD multi-omics, anti-inflammatory microbiome-gut-brain repurposing).

Reviews and single-disease bioinformatics; none intersect the
explainable-KG / EHR-signal / TTE-of-off-label criteria the
drug-repurposing thread prioritizes.

### Scholar keyword feeds — 08-09 batch

#### HIGH — Mikaeeli S, Zheng TM, Li PZ, Nakanishi T, Soulé A, et al. *Lifestyle exposures and bronchiectasis risk in CFTR p.Phe508del carriers.* ERJ Open Research 2026 (Cystic fibrosis carriers keyword feed).

CFTR heterozygote × smoking + alcohol × bronchiectasis. Directly hits
the CF / CFTR disease thread and specifically the *heterozygote-
phenotype epidemiology* sub-question. Nakanishi authorship places
this in the Nakanishi / Greenwood CF-carrier UKB lineage. The
gene-environment framing means it also serves the *G × E and PGS × exposure*
rising sub-thread by analogy. Read carefully: whether the "carrier
effect" is dose-dependent with smoking pack-years, whether it
survives adjustment for polygenic burden, and whether the sample
supports quintile-level HR estimates (typical UKB carrier N for
Phe508del is ~4-5k). Portable to APOL1 heterozygote × exposure and
BRCA1/2 heterozygote × lifestyle-modifier framings.

#### HIGH — Kreutz R, Gebert P, Luo J, Tassopoulou P, Bolbrinker J, et al. *UMOD Genotype and Clinical Outcomes in Heart Failure Patients Treated with Loop Diuretics: A UK Biobank Pharmacogenetic Cohort Study.* Clin Pharmacol Ther. 2026 (UK Biobank keyword feed).

UMOD common variant × loop-diuretic clinical outcomes in UKB HF
initiators, intention-to-treat, 12-mo follow-up, confounder-adjusted
Cox. This is the *pharmacogenomic modifier of medication response*
rising sub-thread in the exact "portable to CFTR modulator / statin
discontinuation / HRT persistence / GLP-1 RA persistence" framing
INTERESTS.md wants. The **more important observation**: UMOD is the
same locus Khan A et al. medRxiv (in last week's 2026-08-08 report)
showed as a rare-variant intermediate-penetrance × age × PGS modifier
for tubular kidney injury. Two independent UMOD stories in one week:
(1) rare-variant kidney-injury penetrance × PGS (Khan), (2)
common-variant × loop-diuretic-response in HF (Kreutz). The
UMOD-locus-across-phenotypes-and-designs mini-review writes itself.

#### HIGH — Sun SD, Liu J, Xu P, Hu Y, Zhang MJ, Zhang J. *MUGO: Differentiable Combinatorial Optimization for Causal Variant Discovery in the Non-coding Genome.* KDD V.2 2026 (variant interpretation keyword feed).

Differentiable combinatorial optimization applied to *causal
non-coding variant discovery*. The non-coding-genome variant-
interpretation gap (functional annotation + fine-mapping + causal
inference) is where the INTERESTS.md variant-interpretation thread
has been thinnest. This is a KDD-tier ML paper — read for the
differentiable-relaxation architecture (likely Gumbel-softmax or
straight-through) and whether it produces per-variant causal scores
that plug into a downstream ACMG-style workflow. Compare to FunSeq2
(Gerstein lab) and CADD-family scores as the incumbent non-coding
variant interpretation stack.

#### HIGH — Jiang Y, Dai R, Zhang Z, Gao S, Chen Y, Du Y, Liu J, et al. *Translating Electronic Health Record Foundation Models into Clinical Decision Support.* preprints.org 2026 (Foundation models + EHR keyword feed).

Translational-pipeline review of EHR FMs: data resources → model
architecture → real-world clinical deployment. This is the *how do
CLMBR / MOTOR / EHRSHOT / MEDS actually reach a patient* framing
INTERESTS.md has been asking for. Read the deployment / calibration /
site-shift sections carefully — the sub-question is which
representation-choice bottleneck (temporal encoding vs. concept
vocabulary alignment) matters most for CDS. Sits alongside the *digital
twins from EHR* rising sub-thread (Zhang/Ideker/Oermann *Cell* 2026).

#### METHODS-WATCH — Zhu Y, Wang Z, Gu L, Sui D, Wang Y, Harrison E, Fu T, et al. *OneEHR: Reproducible and AI Agent-Ready Longitudinal EHR Analysis Toolkit.* KDD 2026 (Foundation models + EHR keyword feed).

KDD tool paper for a longitudinal-EHR analysis benchmark toolkit
explicitly designed for AI-agent consumption. Adjacent to MEDS,
EHRSHOT, FEMR. Bookmark for the toolkit ergonomics review — the
question is whether it's actually reproducible-and-agent-ready (worth
running against your own AoU / MIMIC workflows) or just KDD-friendly
packaging.

#### METHODS-WATCH — Ellard S, Hanson H, Cassidy EJ, Thomson K, Durkie M, et al. *The British Society for Genetic Medicine guidance on managing incidental findings identified during rare disease genomic testing.* J Med Genet. 2026 (Guidance for estimating penetrance of monogenic ... citation feed).

BSGM guidance on secondary findings during rare-disease testing.
Reference-format piece with variant-return, patient-recontact, and
penetrance-estimation implications. Adjacent to the ACMG SF list, the
*Guidance for estimating penetrance* citation feed it fired on
(Wright et al. lineage). Read for any deviations from ACMG SF policy
that would matter for cross-cohort variant return in AoU / UKB.

#### METHODS-WATCH — Schwengber WK, Sanders J, Pinteric A, Armitage L, et al. *Hematologic Consequences of Radiopharmaceutical Therapy: From Clonal Hematopoiesis to Therapy-Related Myeloid Neoplasms.* J Nucl Med 2026 (clonal hematopoiesis intitle feed).

Radiopharmaceutical therapy → CHIP → t-MDS lineage. Peaks with the
177Lu-PSMA-617 phase-3 trial results simultaneously landing (see
Chenjie self-citation feed below): prostate cancer patients on
radioligand therapy are a growing at-risk population for
therapy-related CHIP. Read as the *iatrogenic CHIP exposure* case
study; relevant if the CHIP thread turns toward drug-induced somatic
mosaicism.

#### MEDIUM — Wang J, Yang J, Guo R. *Stepwise Diagnostic Evaluation of Chinese Large Language Models: Comparative Study of Common and Rare Diseases.* J Med Internet Res 2026 (rare diseases keyword feed).

LLM benchmark for stepwise diagnosis with rare-vs-common comparison.
Adjacent to the *Auditable HPO-driven diagnostic benchmarks* rising
sub-thread (GraphRareBench, Phen2Gene, PhenoGPT2 lineage). Read only
if extending the HPO-diagnostic benchmarking piece into cross-lingual
LLM territory.

#### MEDIUM — Aditi, Blackwell T, Fang X, Sharma S, Mendoza M, et al. *Long-term risk of dementia following encephalitis: a large-scale retrospective cohort study of electronic health records.* J Neurology 2026 (electronic health records keyword feed).

Long-term-outcome cohort with EHR ascertainment. Adjacent to the
selective-testing / auxiliary-variable-dependent-sampling problem
(Foulkes et al. from last report). Read for the encephalitis-cohort
definition and censoring approach if the neurologic-multimorbidity
sub-thread becomes active.

#### MEDIUM — Dong Z, Wang Y, Wang S, Lu J, Wang S, Xu M, et al. *Lp(a) and Risk of Subsequent Stanford Type A Aortic Dissection in Patients With Acute Coronary Syndrome: A Multicenter Case-Control Study With Mendelian Randomization.* mendelian diseases 2026 (mendelian keyword feed).

Multi-cohort Lp(a) × aortic dissection MR — adjacent to the
drug-target MR sub-thread (Lp(a)-lowering agents in trial). Bookmark
for the aortic-dissection subthread if returning to aortic outcomes.

#### LOW — Chinese guidelines on autoimmune bullous diseases autoantibodies.

Practice-guideline piece; not on-thread.

#### LOW — Nisar A et al. Letter-to-editor comment on Chen et al. UKB METS-IR × SIRI × renal cell carcinoma paper.

Correspondence piece; no primary evidence.

#### LOW — Yang L et al. *Shared Systemic Metabolic Signature Across the Neurological Disease Spectrum: 274,241 UK Biobank Nightingale NMR analysis.*

UKB NMR × neurological outcomes summary-level analysis. Adjacent to
the *multi-omics-augmented PRS* thread. Read only if extending
Nightingale-NMR × PRS work.

#### LOW — Liu H et al. UKB *Life Course Adiposity and Risk of Incident Osteoporosis*, Liu X et al. *Smoking behavior and frailty CVD joint impact* UKB, You Q et al. *Healthy Lifestyle × CKD-metabolic mortality* UKB+NHANES, You Y et al. *Finasteride/tamsulosin × T2D* China+UKB, Niu T et al. *Wearable PA × mortality diabetes+HTN* UKB+NHANES, Ma X et al. *SDOH × bone-joint progression* UKB, van den Berg et al. *Cardio-oncology biomarkers UKB thesis chapter*.

Descriptive-epidemiology UKB cohort papers. Off-thread individually;
mentioned only to note the UKB-descriptive-epi background rate this
week.

#### LOW — Xu Q, Hong L, Shen M. *Coalition-based Knowledge Graph Learning for Actual Controller Disclosure.* IEEE TKDE 2026 (knowledge graph feed).

Off-domain (financial disclosure); not on-thread.

#### LOW — Wang A et al. *Deconstructing Combination Therapies and Drug Repurposing for Cutaneous Leishmaniasis.* J Asian Med Sci 2026 (drug repurposing feed).

Single-indication component network MA; not on-thread.

### Scholar author feeds — 08-10 batch

#### HIGH — Olayinka O, Farrell JJ, Zhu C, Khurshid Z, Martin ER, et al. *Stratification by a polygenic risk score of common variation aids in Alzheimer's disease rare variant discovery.* Alzheimer's & Dementia 2026 (Lisa Bastarache related-research feed).

**PGS-stratified rare-variant discovery** in the Alzheimer's Disease
Sequencing Project (ADSP), European-ancestry participants. This is a
canonical instance of the *PGS-residuals / PGS-tails as a discovery
lever* framing INTERESTS.md now explicitly tracks. Design: use AD PGS
to enrich the cohort for rare-variant discovery — the same design
principle Baya *AJHG* 2026 "misaligned individuals" articulated in
generic form. Read alongside Khan et al. UMOD medRxiv (2026-08-08
report) and Peng et al. early-onset breast cancer medRxiv (also
2026-08-08 report) as a three-paper triangulation of *PGS as a
discovery instrument, not just a prediction instrument*. Together
they justify a mini-review argument: PGS-residual / PGS-tail /
PGS-stratification-based rare-variant discovery is the field's next
methodological pivot.

#### HIGH — Xu Y, Loesch D, Taylor HJ, Keating MF, Ritchie SC, et al. *A proteome-wide association study of cardiovascular diseases in 640,000 participants of multiple ancestries.* medRxiv 2026 (Chenjie Zeng related-research feed).

Genetically imputed proteomics for **2,594 proteins** applied to CVD
outcomes across **640,000 multi-ancestry** participants. This is a
proteomics-PWAS with the scale to actually resolve cross-ancestry
protein-QTL portability — a first at this N. Directly serves the
*multi-omics-augmented PRS*, *drug-target Mendelian randomisation*,
and *cross-ancestry portability* sub-threads simultaneously. Read
carefully for: the reference protein-QTL panels (deCODE 35k SomaScan?
UKB PPP Olink? Both stitched?), how the imputation models handle
ancestry-shifted eQTL/pQTL architecture, and whether the top
hits track known drug targets (PCSK9, LPA, IL-6R). The
"drug-target MR" sub-thread should adopt whatever protein-QTL
weights they publish.

#### HIGH — Onoja A, Elomaa K, Whetton AD, Geifman N. *Explainable temporal machine learning of multimorbidity trajectories after acute myocardial infarction: complementing clinical risk scores with mechanistic phenotypes.* JAMIA 2026 (Chenjie Zeng + George Hripcsak + 7 new citations to Bastarache feeds — pinged three separate feeds).

Explainable temporal ML for multimorbidity trajectories after AMI,
with mechanistic-phenotype overlay to complement clinical risk scores.
Hits multiple threads simultaneously: (1) *Chronic disease clustering
and multimorbidity* — trajectory clustering post-AMI; (2)
*ML for precision health* — decision-aligned (post-AMI risk
stratification is a real clinical decision); (3) *EHR foundation
models* — likely tokenized-EHR-style representation. The *mechanistic
phenotype* overlay is the interesting move — pairing ML trajectory
clusters with mechanistic biomarker signatures to give clusters
biological interpretability. Portable to post-CFTR-modulator
trajectory clustering, post-GLP-1 RA initiation trajectory clustering,
post-HRT trajectory clustering.

#### HIGH — Shen C, Dupuis J, Zhang Q. *Multi-ancestry colocalization approaches.* PLoS Genetics 2026 (Chenjie Zeng related-research feed).

Multi-ancestry colocalization methods. Cross-ancestry portability of
colocalization signal is the standard failure mode for fine-mapping
(local LD structure varies by ancestry, so coloc PP4 flips by
population). This paper is the methods update your genetic-epi thread
needs for any TWAS or proteomic-MR that touches non-EUR populations.
Read alongside Xu Y multi-ancestry PWAS above (same feed, same
issue, coupled solutions).

#### HIGH — Liao CC, Hu WC, Yang SF, Li JM. *Genome-wide cross-trait analysis reveals immunogenetic pleiotropy between autoimmune diseases and myocardial infarction and prioritizes therapeutic targets.* Atherosclerosis 2026 (Chenjie Zeng related-research feed).

Cross-trait GWAS between autoimmune diseases and MI, with
therapeutic-target prioritization. Directly serves the *cross-trait
shared genetic architecture and multi-trait triangulation* rising
sub-thread (MiXeR / conditional-FDR family; Kopal et al. brain-imaging
× mental health × cardiometabolic lineage). Read for the shared-target
list — this is drug-target-MR-adjacent evidence.

#### HIGH — Krüger N, Schneeweiss S, Wang SV. *Tirzepatide and the risk of atherosclerotic cardiovascular events: population-based cohort study.* BMJ 2026 (10 new citations to Miguel Hernán feed).

Tirzepatide × ASCVD population-based cohort — the exact question that
tirzepatide's real-world ASCVD story hangs on (SURMOUNT-MMO reported
positive but is trial-scale; observational at population scale
matters for translation). Sits inside the *GLP-1 RA* drug-class watch
and the pharmacoepi thread. Read for the target-trial-emulation
scaffolding (Schneeweiss / Wang typically use it) and the
active-comparator choice (semaglutide? empagliflozin? none?).

#### MEDIUM — Aali A, Bikia V, Varma M, Chiou N, Ostmeier S, et al. *Toward expert-level medical text validation with language models.* npj Digital Medicine 2026 (Emily Alsentzer new-articles feed).

Language-model validation on medical text. Adjacent to the NLP-derived
representations from clinical notes sub-thread. Read only if extending
the clinical-note LLM extraction work.

#### MEDIUM — Nashnoush E, D'Couto H, Fine B et al. *Deep Learning Estimation of FEV1/FVC and Obstructive Lung Disease Classification From Chest Radiographs.* (Leo Anthony Celi new-articles).

CXR-based FEV1/FVC estimation. Adjacent to the CF/CFTR-modulator
outcome-measurement sub-thread if CXR-derived ppFEV1 becomes a viable
proxy in EHR cohorts where spirometry is missing.

#### MEDIUM — Elkoshi Z. *The central role of IL-6 in the differential effects of GLP-1 receptor agonists and metformin across multiple health conditions.* Front Immunol 2026 (Hripcsak 10 new citations).

Review-format IL-6 mechanism piece for GLP-1 RA vs metformin
differential effects. Bookmark for the GLP-1 pharmacoepi thread's
mechanism section.

#### MEDIUM — Rajueni K, Koskimaki F, Salo V, Pasanen A, Sliz E, et al. *Multi-biobank genome-wide association study of dermatochalasis implicates genes involved in skin biology and morphology.* medRxiv 2026 (Chenjie Zeng + Denny + Bastarache related-research feeds).

Multi-biobank GWAS meta-analysis of dermatochalasis (n=13,200 cases).
The multi-biobank design is the methods interest here (FinnGen +
UKB + Estonian? — check on full-text). Off-thread as a disease unless
extending to skin-lax / photoaging phenotypes.

#### MEDIUM — He Z, Chu B, Yang J, Gu J, Chen Z, Liu L, Morrison T, et al. *CIT-Lasso: a scalable approach beyond guilty by association for identifying causal variants from genome-wide summary statistics.* Genome 2026 (Jian Yang related-research feed).

Summary-statistic fine-mapping / causal-variant identification method
(He/Tang lineage, same group as GhostKnockoffs paper above). Read
alongside GhostKnockoffs and the multi-ancestry colocalization paper
for a "current-state-of-fine-mapping" mini-update.

#### MEDIUM — Armstrong ND, Srinivasasainagendra V, Patki A, Pilla L, et al. *Evaluation of functional annotation-informed and ancestry-specific polygenic risk scores for ischemic stroke.* Frontiers in Bioinformatics 2026 (Lisa Bastarache related-research feed).

Functional-annotation-informed + ancestry-specific PRS for ischemic
stroke. Serves the *ancestry-aware PGS / cross-trans-ancestry
portability* sub-thread. Read for the specific PRS construction
method (LDpred2-func? PRS-CSx-func? new?) and downstream calibration
across African / East Asian / European ancestry.

#### MEDIUM — Tu H, Ju C, McGurnaghan SJ, Blackbourn LAK, et al. *Absence of Interaction Between 5α-Reductase Inhibitors and Glucocorticoids on Incidence of Myocardial Infarction in People With Type 2 Diabetes.* Diabetes, Obesity and Metabolism 2026 (Chenjie Zeng related-research feed).

Interaction analysis on MI incidence with 5α-reductase × glucocorticoid.
Adjacent to the pharmacoepi thread; niche question.

#### METHODS-WATCH — Cheng W, Ma M, Shen S, Hupalowska A, Rood JE, et al. *Towards Human-Led, Agent-Driven Autonomous Laboratories for the Life Sciences.* 2026 (Jian Ma new-articles feed).

LLM-agent-driven autonomous wet-lab vision paper. Off-thread for
clinical work; bookmarkable as background for the agentic-pipeline
future-of-research thread.

#### METHODS-WATCH — Boßelmann CM, Ortiz S, Dahl R, Liao VWY, et al. *Accurate prediction of gain-and loss-of-function missense variants in GABAA receptors.* EBioMedicine 2026 (Kai Wang 10 new citations).

Missense GoF/LoF prediction for GABA_A receptors. Adjacent to
variant-interpretation thread — but disease-specific enough that read
depends on whether epileptic-encephalopathy is on your active list.

#### METHODS-WATCH — Kern DM, Bohn J, Gilbert JP, Knoll C, Ryan PB. *REWARD—an open-source framework for identifying the unknown benefits of existing medications to inform drug discovery, development, and repurposing.* (Patrick Ryan new-articles feed).

Open-source EHR-based drug-repurposing signal-detection framework.
Directly serves the *EHR-based repurposing signals mined from
real-world prescribing and outcomes* sub-thread. Read for the
signal-generation logic and whether it composes with OHDSI standard
tooling.

#### METHODS-WATCH — Liang C, Chilson EL, Wu J, Kelly SP, Liu Q. *Can We Compare Adverse Event's Attributable Risk Using a Self-Controlled Case Series Design for Vaccine Safety? A Guillain-Barré Syndrome Use Case.* (Patrick Ryan related-research feed).

SCCS design method question with GBS-vaccine use case. Bookmark for
the pharmacoepi methods list.

#### METHODS-WATCH — Villa A, Eadie AL, Synnott D, Romanò R, Piffoux M, et al. *AI-based augmentation of oncology clinical trials.* Nature Reviews Clinical Oncology 2026 (Hernán 10 new citations feed).

AI × oncology trial enrichment / synthetic-control-arm review. Adjacent
to the target-trial-emulation and ML-for-decision-making threads;
also to the synthetic-EHR/synthetic-control-arm sub-thread. Bookmark.

#### LOW / SKIP — Off-thread items in the 08-10 batch:

- Ong AQC et al. *AI in cardiovascular care meta-analysis of RCTs* — SR/MA level, off-primary-thread.
- Kim Y et al. *Capable language models can outgrow benefits of collaboration.* Nat Mach Intell — LLM-agent behavior, off-clinical-thread.
- Yang F et al. *Microglial dysfunction bridging synaptic pruning + neuroinflammation* — off-thread basic neuro.
- Peet CJ et al. *TBK1 mutation × familial recurrent myopericarditis* — case-report-tier.
- Xu Z et al. *Discriminative LMs as Retrievers.* arXiv (Zitnik feed) — ML retrieval, off-thread.
- Lee N et al. *Compositional Representation of Crystalline Materials.* KDD (Zitnik feed) — materials, off-thread.
- Yan L et al. *Melatonin GWAS × hypertension MR* — niche.
- Zhu Q et al. *Wnt gene family in donkey* — off-species.
- Zang M et al. *CD8 T-cell immunotherapy response in gastric cancer* — single-cell oncology.
- Zhu X et al. *Combinatorial CRISPRi screening in synthetic biology* — off-clinical.
- Grentzinger V et al. *Long Read Sequencing of Filaggrin* — off-thread (dermatology).
- Zuppelli T et al. *Long-Read RNA Seq × radiotherapy microglia* — off-thread.
- Peroni E et al. *Down syndrome leukemogenesis spatial multi-omics* — off-thread.
- Mohamed NA et al. *T2D × pancreatic lineage stem cell* — off-thread.
- Li Y et al. *scCotag prior-informed co-optimal transport for scRNA multi-omics* — off-thread (single-cell method).
- Yang Z et al. *IP rights + legal liability AI pediatric diagnosis* — off-thread (policy).
- Yunqiu G et al. *AI × NK cell niches immuno-oncology.* Front Immunol — off-thread.
- Gu Y et al. *EviRAG evidence-guided RAG medical VLM.* ACL 2026 — LLM tooling, off-primary-thread.

---

## Cross-cutting observations

1. **UMOD as a "portable penetrance-modification archetype."** Two
   independent UMOD-locus stories landed in successive weeks —
   Khan medRxiv (rare-variant × age × PGS penetrance for tubular
   kidney injury) and Kreutz Clin Pharmacol Ther (common-variant ×
   loop-diuretic HF outcome). Combined with the last report's PGS-tails
   framing, this gives a locus-specific case study for the
   "monogenic × common × drug-response" penetrance-modification
   template. Worth writing up as a short methods-focused perspective
   piece on how a single locus can be read three ways.

2. **PGS-as-discovery-instrument is congealing into a real methods
   pattern.** Olayinka AD (this window) + Khan UMOD (last window) +
   Peng early-onset BC (last window) + Baya *AJHG* 2026 (framing
   reference in INTERESTS.md) now form a coherent
   *stratify-by-PGS-to-discover-rare-variants* methodology across
   three diseases and two designs (PRS-stratified sequencing burden;
   PRS-residual missense enrichment). This is well past the point of
   being a "one paper does this" claim.

3. **Multi-ancestry portability crescendo.** Xu Y et al. multi-ancestry
   PWAS 640k + Shen Dupuis Zhang multi-ancestry colocalization + Armstrong
   ancestry-specific ischemic-stroke PRS all landed in the same
   Chenjie related-research batch. Read together they suggest the
   cross-ancestry-portability sub-thread has become a first-class
   topic rather than a sub-topic of PRS methods.

4. **Somatic mosaicism twin update.** Zeng Z JACC Adv (LOY × PAD /
   aortic) + Liu Q Clin Med (Lond) CHIP risk factors +
   Bravo-Perez et al. lymphoid CHIP (last window) — three
   somatic-mosaicism pieces in two weeks. The male-specific LOY vs
   myeloid vs lymphoid CHIP triangulation could support a full-thread
   update if the disease-specific outcome data (cardiovascular,
   hematologic, neoplastic) is aligned.

## What's NOT in the report

- **`arxiv-digest` repo** — quiet weekend at arXiv, both cron runs
  empty.
- **bioRxiv / medRxiv subject-collection alerts** — none surfaced this
  window; on-thread medRxiv items (Xu Y PWAS, Rajueni dermatochalasis,
  Peng early-onset BC from prior report) came through Scholar
  author/keyword feeds rather than subject-collection subscriptions.
- **Substack / newsletters** — none crossed the on-thread threshold
  this window.
- **arxiv.org daily category mailings** — the three cs / q-bio /
  stat.AP daily mailings from no-reply@arxiv.org on 08-10 are the
  upstream source for the local `arxiv-digest` pipeline; nothing
  crossed the digest's `--min-score 1` threshold.
- **NCBI "All of Us" What's New (08-08 batch)** — separate email,
  covers the same Hysong et al. paper already surfaced via the 08-09
  NCBI batch and the 08-10 Chenjie related-research feed. No
  additional papers.

## Next steps to consider

1. **UMOD locus mini-review.** With Khan (rare × age × PGS →
   tubular injury) and Kreutz (common × loop diuretic → HF outcome)
   landing one week apart, and Denny/Bastarache/Hripcsak lineage on
   both, a 2-page methods-perspective piece on
   *reading-a-single-locus-through-three-designs* is well-positioned.
2. **PGS-as-discovery-instrument perspective piece.** Olayinka AD +
   Khan UMOD + Peng early-onset BC now anchor a
   *stratify-by-PGS-to-discover-rare-variants* argument that has both
   methods weight (Baya, Souaiaia, Vazquez precedents) and multi-
   disease empirical support.
3. **Read Xu Y multi-ancestry PWAS full text first** — 640k
   participants is a first-of-its-kind scale for cross-ancestry
   proteomics-genetics, and the imputation-model architecture will
   shape the drug-target MR sub-thread going forward.
4. **APOL1 triad (from 2026-08-08 report) still open** — Gaheer /
   Chen / Kim & Lee still deserves a short thread-update writeup;
   nothing displaced them this window.
5. **Follow-up on Onoja et al. JAMIA** — Multimorbidity-trajectory ML
   with *mechanistic phenotype overlay* is the exact
   ML-for-precision-health-with-biological-interpretability template
   INTERESTS.md wants. Read for portability to post-modulator CF
   trajectories or post-GLP-1 RA cardiometabolic trajectories.

_Report generated 2026-08-10 by scheduled routine; sources: Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-10 → next scheduled run._
