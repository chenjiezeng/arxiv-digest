# Research digest report — 2026-06-15

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML
for precision health, multimorbidity).

Window: **2026-06-14 → 2026-06-15** (since the prior 2026-06-13 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-14 → 06-15 | Two batches: 06-14 17:04Z (keyword: AoU/UKB), 06-15 00:34Z (author alerts: Denny, Bastarache, Ryan, Hernán, Zitnik, Karczewski, Hripcsak, Szolovits, Chute, Montgomery, Yang, Kastner, Lu, Callahan, Vogelstein, Kohane, Pritchard, Brandt, Shendure, Natarajan, Collins, Luo), 06-15 03:27Z (keyword: APOL1, Gharavi). |
| `arxiv-digest` repo (`digests/`) | 2026-06-14 → 06-15 | 2 daily files; **both empty** (0 papers; 1–2 previously surfaced, suppressed). |
| NCBI / bioRxiv / medRxiv aggregate alerts | daily | Not individually triaged here. |

> ⚠️ **`arxiv-digest` produced zero new matches** on 06-13 and 06-14.
> All HIGH-priority signal this window came from Scholar alerts.
> No GitHub-side notifications for the `arxiv-digest` repo arrived
> (no PR/issue activity in `from:notifications@github.com`).

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below
> contextualize that metadata against your research threads; nothing
> here reflects full-text reading.

---

## Executive summary

- **APOL1 has a banner day.** A *Nature Genetics* News & Views ("Proteomic
  prediction of APOL1-associated kidney disease", Vogan) summarizes a new
  9-protein **APOL1 Proteomic Risk Score (APRS)** that stratifies which
  high-risk-genotype carriers actually progress to kidney failure — the
  exact "penetrance under population screening vs. clinical
  ascertainment" gap that anchors your PheWAS/PheRS thread. A pediatric
  CKD study (Zahr et al., *Pediatric Nephrology*) in the
  Biorepository-and-Integrative-Genomics-Initiative (BIG) characterizes
  pediatric APOL1 HR baseline, CKD risk, and the **p.N264K protective
  variant** — again, ascertainment-controlled penetrance.
- **CHIP × lifestyle in *Nature*.** Gerhardt et al. show that JAK2 /
  TET2 / TP53 / DNMT3A mutant haematopoietic clones respond
  **differentially to sleep and exercise**, partly via inflammation /
  atherosclerosis. Lands in your CHIP/VEXAS thread and cites All of Us
  genomic data — first time we've seen an AoU-cited paper modulating
  CHIP clone expansion by a modifiable behavioral exposure.
- **Y-chromosome PheWAS, n=104,334 Finnish men (FinnGen).** Preussner
  et al. on medRxiv — phenome-wide scan of Y-chromosomal variation in
  complex disease. Methodologically novel (Y is usually dropped from
  GWAS/PheWAS) and squarely on your PheWAS / phecode infrastructure
  thread.
- **MIXPRS in *Nature Genetics*.** Multi-population, multi-method PRS
  from summary statistics — directly relevant to your trans-ancestry
  portability sub-thread (and arrives in your self-citation feed).
- **All of Us, two cardiometabolic uses:** (i) ASCVD treatment gaps in
  AoU (Bene-Alhasan et al., *Atherosclerosis*) — EHR-linked utilization
  description; (ii) AoU + GLP-1 + metformin in hidradenitis suppurativa
  (Shrestha et al., *Diabetes Care*) — drug-class real-world signal in
  AoU, intersecting both your AoU thread and the GLP-1 pharmacoepi
  thread.
- **Two target-trial-emulation papers from the Hernán-citing batch**:
  TKI generation comparison in Ph+ ALL (Zhang et al., TriNetX) and
  semaglutide vs. dulaglutide in UK CPRD T2D (Ulrich et al.) — both
  METHODS-WATCH for the propensity score / TTE pipelines.
- **GWAS of extended prescription analgesic use** (Harlow et al.,
  *Nature Communications*) — uses **prescribing as a phenotype**,
  paralleling pheRS / phecode-style EHR phenotype work and feeding the
  drug-repurposing thread.
- **EHR foundation model / embedding signal** picked up by multiple
  watch authors: Johnson et al. (*npj Digital Medicine*) on knowledge-
  grounded clinical-code embeddings, and Huang/Xia/Ma/Cai (arXiv,
  surfaced by both Brandt and Hripcsak alerts) on **spectral embedding
  with robust knowledge transfer in EHR** — methods-watch for the
  CLMBR/MOTOR/MedTok lineage.
- **`arxiv-digest` was silent** on 06-13 and 06-14 (zero new
  papers). The recommendation from prior reports (add `cs.LG`,
  `stat.ME`, medRxiv) still stands — and is reinforced this week by the
  fact that the Y-chromosome PheWAS and the spectral-EHR-embedding
  paper would have been caught by a medRxiv/cs.LG feed but were not
  caught by your q-bio/stat.AP feed.

---

## HIGH — directly on an active thread

### 1. Proteomic prediction of APOL1-associated kidney disease
**Vogan K.** *Nature Genetics* News & Views, 2026.
Link: https://www.nature.com/articles/s41588-026-02650-7
Threads: **APOL1**, PheWAS/PheRS (penetrance under screening), EHR-
linked biobanks, ML for precision health.

What it is. News & Views summarizing a new APOL1 Proteomic Risk Score
(APRS). High-risk APOL1 genotypes (G1/G2) are strongly associated with
kidney failure in individuals of African ancestry, but only a subset of
HR carriers progress. The summarized study identifies a **nine-protein
signature** that, combined with standard clinical variables, derives an
APRS predicting which HR carriers progress.

Why it matters to you.
- Direct hit on your **penetrance-in-population-screening** sub-thread:
  the central puzzle is which HR APOL1 carriers actually develop
  disease, and proteomic stratification is a complementary axis to PRS
  and EHR-derived modifiers you've been tracking.
- The APRS framing — a small protein panel layered on a monogenic risk
  variant to refine risk — is structurally identical to the
  PRS-stacked-with-rare-pathogenic-variants composite-risk approach
  in your genetic epi thread.
- Pair this with the pediatric APOL1 paper below to triangulate
  ascertainment (adults / proteomics vs. children / clinical CKD risk +
  p.N264K modifier).

How to triage it. Read the primary paper that this N&V points to (find
the s41588-026-02650 sibling). For the BioVU/AoU writing, check
whether APRS is computed in any EHR-linked biobank you have access to
or whether the protein panel can be substituted by Olink / SomaScan
panels in AoU's proteomic sub-cohort.

### 2. APOL1 and chronic kidney disease in pediatrics: BIG initiative
**Zahr RS, Chinthala L, Mohammed A, Kovesdy CP, et al.** *Pediatric
Nephrology*, 2026.
Link: https://link.springer.com/article/10.1007/s00467-026-07385-5
Threads: **APOL1**, rare disease, EHR-linked biobanks, variant
interpretation.

What it is. Baseline characteristics of children in the Biorepository
and Integrative Genomics Initiative (BIG) stratified by APOL1 high-risk
genotype, with three aims: describe pediatric APOL1 HR carriers,
quantify CKD risk by HR genotype, and characterize the **protective
effect of the p.N264K variant** in HR carriers.

Why it matters to you.
- p.N264K is exactly the kind of *modifier-of-a-monogenic-risk-variant*
  signal your APOL1 thread is built around — a clean variant-
  interpretation × population-genetic epi cross.
- Pediatric ascertainment is rare (most APOL1 cohorts are adult
  nephrology), so penetrance trajectory from childhood is novel.

How to triage it. Pull the table of HR-genotype distribution and the
N264K effect size — see if their N264K hazard ratio is consistent with
the adult literature (Hung et al.) and whether they restrict to
biopsied / clinically-ascertained pediatric cases or sample more
broadly. Note for your transplant-decision sub-thread: pediatric
recipients with HR + N264K might be re-classified.

### 3. Mutation-dependent responses to sleep and exercise in clonal haematopoiesis
**Gerhardt T, Jacob W, Gaebel L, Heiser M, Wolfram C, et al.** *Nature*,
2026.
Link: https://www.nature.com/articles/s41586-026-10634-0
Threads: **CHIP/VEXAS**, EHR-linked biobanks (cites AoU), ML for
precision health.

What it is. Across humans and mice, the authors show that CH driver
mutations (Jak2, Tet2, Trp53, Dnmt3a) **respond differentially to
lifestyle exposures** (sleep, exercise) — clones expand or contract,
and the inflammatory/atherosclerotic phenotype of mutant cells shifts.
First demonstration in humans of mutation-stratified lifestyle
modification of CH biology. Two human datasets are reported, one
citing All of Us.

Why it matters to you.
- Directly on your **CHIP / VEXAS** thread, which has been mostly
  CV-outcomes-focused; this expands it to *modifiable* lifestyle
  exposures interacting with CH driver gene.
- Methods-watch: how they handled VAF measurement noise, mutation-
  specific subgroup analyses, and ascertainment of "sleep" / "exercise"
  exposures in AoU — directly transferable to your phenome-wide
  CHIP × phecode work.
- Likely to be cited heavily — worth getting in early.

How to triage it. Skim Figs 1–3 first (mutation-specific effect
heterogeneity). Note the AoU cohort definition for replication; if
they used the AoU CHIP call-set, that's reusable scaffolding.

### 4. Investigating the Y chromosome in complex disease: phenome-wide scan across 104,334 Finnish men
**Preussner A, Leinonen JT, FinnGen, Pirinen M, et al.** *medRxiv*,
2026.
Link: https://www.medrxiv.org/content/10.64898/2026.06.09.26355235
Threads: **PheWAS / phecodes**, genetic epi, EHR-linked biobanks
(FinnGen).

What it is. A phenome-wide Y-chromosome association scan in 104,334
Finnish men in FinnGen. Y is dropped from essentially all standard
GWAS / PheWAS pipelines despite encoding ~2% of the male genome; the
authors lay out a workflow to bring it back in.

Why it matters to you.
- Methodologically central to your PheWAS / phecode infrastructure
  thread: Y-chromosome handling (haplogroup calling, MSY variant
  filtering, dosage construction) is exactly the kind of plumbing
  decision your AoU / UKB / MVP / BioVU work needs to make explicit.
- FinnGen + phecodes is a natural reference for AoU's phecodeX rollout.

How to triage it. Read methods first — what variant call-set they
used, how they treated MSY vs PAR, and whether they used phecodes or
ICD chapters as the phenome. Then scan phenome-wide hits; check
overlap with cardiovascular and prostate cancer (most-replicated Y
associations historically). Tag for **import into your own AoU Y-PheWAS
plan** if you have one queued.

### 5. MIXPRS: multi-population, multi-method polygenic risk scores from summary statistics
**Xu L, Dong Y, Zeng X, Bian Z, Zhou G, Guan L, Zhao H.** *Nature
Genetics*, 2026.
Link: surfaced via "Chenjie Zeng — new related research" 06-13 alert
(thread 19ec25dcdb56447c).
Threads: **genetic epi** (PRS / trans-ancestry portability), ML for
precision health.

What it is. PRS construction framework that combines multiple
populations (cross-ancestry) and multiple methods (likely a mixture /
stacking of LDpred-style, lassosum-style, etc.) from GWAS summary
statistics only. Targets the well-known portability gap.

Why it matters to you.
- Direct hit on your **cross-/trans-ancestry portability** sub-thread
  and the composite-risk-modeling thread.
- *Nature Genetics* venue plus summary-stat-only requirement means
  it'll be a default baseline for the next 6–12 months — worth
  benchmarking against PRS-CSx, MUSSEL, PROSPER on your own AoU /
  UKB / MVP applications.

How to triage it. Pull the code (assume Zhao-lab GitHub) and the
benchmark tables. Confirm whether AFR-EUR or EAS-EUR pairs are the
strongest gain, and whether they handle the typical large effective
sample size imbalance (EUR ≫ AFR). Note the trait list — if BMI / T2D
/ CAD they likely use UKB / BBJ / AoU as benchmarks, which is your
substrate.

### 6. All of Us — Persistent gaps in ASCVD management and risk factor control
**Bene-Alhasan Y, Al Osta S, Issaka Y, Acquah I, et al.**
*Atherosclerosis*, 2026.
Threads: **EHR-linked biobanks (AoU)**, pharmacoepi, ML for precision
health.

What it is. AoU-cohort description of lipid-lowering therapy use,
LDL-C control, and CV risk factor prevalence across CAD / PAD / CAS
patients with established ASCVD. Documents under-treatment / non-
attainment of LDL-C targets.

Why it matters to you.
- Confirms AoU's utility for **real-world prescribing-and-utilization
  description**. Even though this is a clinical-question paper
  (medium priority by your rubric), the operationalization of "ASCVD"
  and the LLT-exposure window are reusable for your causal
  inference / pharmacoepi pipelines.

How to triage it. Check their phenotype definitions (which ICD/SNOMED
maps they used for CAD, PAD, CAS) and the EHR-data-quality filter
they applied. Their LLT exposure scheme is likely transferable.

### 7. AoU + GLP-1 + metformin in hidradenitis suppurativa
**Shrestha R, Nguyen GH, McCoy RG.** *Diabetes Care*, 2026.
Threads: **AoU**, **GLP-1 pharmacoepi**, drug repurposing.

What it is. Real-world AoU analysis of metformin and GLP-1 RA use in
patients with hidradenitis suppurativa (HS). HS has emerging anti-
inflammatory drug-class signal.

Why it matters to you.
- Directly on the **GLP-1 pharmacoepi** thread and crosses your
  drug-repurposing thread (GLP-1 RA for an inflammatory dermatologic
  outcome).
- Methodologically a small-cohort AoU exposure-outcome study; check
  whether they emulated a target trial or used a more descriptive
  design.

How to triage it. Pull Table 1 to see exposure-cohort size for HS
in AoU (likely small, n in the hundreds), and whether sensitivity
analyses use SGLT2i as a negative-control exposure or another
anti-obesity drug. Outcome ascertainment is the key question.

### 8. Semaglutide vs. dulaglutide in UK CPRD T2D
**Ulrich FS, Nielsen MF, Napoli N, et al.** Surfaced via Patrick Ryan
alert, 06-13.
Threads: **GLP-1 pharmacoepi**, target trial emulation.

What it is. Comparative effectiveness and safety of once-weekly
semaglutide vs. dulaglutide in UK primary care (CPRD) among T2D
patients.

Why it matters to you.
- GLP-1 class is on your active list; intra-class comparisons (sema
  vs. dula) are exactly the kind of head-to-head you flagged.
- Patrick-Ryan-alert sourcing means this is likely OHDSI-adjacent.

How to triage it. Look at the propensity score adjustment set and
whether they used a TTE design. Check whether sema's MACE benefit
holds against dula in the active-comparator framing.

### 9. GLP-1 therapy and HF / respiratory failure events in non-diabetic RA + obesity
**Loizidis G, Summer R.** *Clinical Rheumatology*, 2026 (TriNetX).
Threads: **GLP-1 pharmacoepi**, EHR-linked real-world evidence.

What it is. Retrospective TriNetX cohort study of semaglutide /
tirzepatide vs. never-users in non-diabetic RA + obesity adults,
outcomes ICD-coded HF or respiratory failure. Propensity-matched.

Why it matters to you.
- GLP-1 in *non-diabetic* + *autoimmune* population is the cleanest
  test of off-target / repurposing effects — falls into your drug-
  repurposing × GLP-1 intersection.
- TriNetX is OHDSI-adjacent, methodologically familiar.

How to triage it. The methodological worry on a TriNetX 1:1 propensity
match is *immortal-time bias* and *index-date alignment*; check whether
they applied a clone-censor-weight (CCW) or grace period.

### 10. Target Trial Emulation: 2nd- vs 1st-generation TKIs in Ph+ ALL
**Zhang X, Jhou HJ, Chen HY, Xiao N, Chen PH, Lee CH.** *JCO Oncology
Practice*, 2026 (TriNetX).
Threads: **target trial emulation**, pharmacoepi.

What it is. TriNetX-based TTE comparing 1st- vs 2nd-generation TKIs
in newly-diagnosed Ph+ ALL, citing the standard Hernán "explicitly
aiming to emulate" framework. Cites the OHDSI process guide for
inferential studies.

Why it matters to you (METHODS-WATCH).
- Off-topic disease but exemplary TriNetX-TTE plumbing — useful as a
  template for your own EHR-based target trial emulations in CFTR,
  GLP-1, SGLT2i.

### 11. Embeddings of clinical codes enable knowledge-grounded AI in medicine
**Johnson R, Gottlieb U, Shaham G, Eisen L, Waxman J, et al.** *npj
Digital Medicine*, 2026.
Threads: **EHR foundation models**, knowledge graphs / ontologies.

What it is. Standardization-of-EHR-via-embeddings paper from
the Zitnik orbit. Frames clinical code embeddings as the
substrate for knowledge-grounded clinical AI.

Why it matters to you.
- Direct entry in your EHR foundation models thread (CLMBR / MOTOR /
  MedTok / EHRSHOT lineage). MedTok in particular comes from the same
  research neighborhood.

How to triage it. Scan their embedding-space evaluation — do they
align embeddings with HPO / SNOMED ontology structure (your KG
thread)? Or do they rely purely on co-occurrence?

### 12. Enhancing Spectral Embedding through Robust and Flexible Knowledge Transfer in EHR
**Huang F, Xia Z, Ma R, Cai T.** arXiv:2606.11570, 2026.
Threads: **EHR foundation models**, EHR phenotyping.

What it is. Spectral embedding for EHR data with explicit knowledge-
transfer machinery (likely between sites or between code systems).
Surfaced by both Pascal Brandt and George Hripcsak alerts — strong
methods-watch signal.

Why it matters to you.
- METHODS-WATCH for the cross-site EHR transferability problem and
  for OMOP-CDM-style harmonization at the embedding layer.
- Tianxi Cai's group output is consistently relevant to the
  EHR-phenotyping / federated-EHR threads.

How to triage it. Skim methods to see whether the "knowledge transfer"
piece is ontology-based (HPO/SNOMED weights into the spectral kernel)
or empirical (transfer from a source-site embedding). Either way it's
relevant.

### 13. GWAS of extended prescription analgesic use in chronic pain
**Harlow CE, Uzochukwu E, Fernando HA, Mordaunt CE, et al.** *Nature
Communications*, 2026.
Threads: **genetic epi** (GWAS), drug repurposing, EHR phenotyping
(prescribing as phenotype).

What it is. GWAS using **extended prescription analgesic use** as the
phenotype to identify chronic-pain loci. Surfaced via the Jian Yang
alert.

Why it matters to you.
- Direct hit on your *drug-repurposing × EHR-based phenotype* angle:
  prescribing patterns are an EHR-derived proxy phenotype, and
  chronic pain has long been a frustrating GWAS target.
- Methodologically transferable to any "repeated dispensing as a
  phenotype" approach (analogous to your interest in modulator-
  eligibility-by-prescribing-history work in CF).

How to triage it. Check phenotype definition: which DDD / days-supply
threshold, which analgesic classes (opioid / NSAID / both), and
how chronicity was operationalized. Compare to the UKB pain question
GWAS — replication helps anchor whether you trust prescribing-as-
phenotype.

### 14. Polygenic overlap and shared genomic loci: anorexia nervosa × cardiometabolic
**Lu ZA, Ploner A, Birgegård A, Bergen SE.** *Neurobiology of Disease*,
2026.
Threads: **genetic epi** (polygenic overlap, shared loci),
multimorbidity.

What it is. AN × cardiometabolic shared-genetics analysis — extends
the AN-metabolic correlation literature to specific shared loci.

Why it matters to you.
- Cross-trait genetic architecture for cardiometabolic phenotypes
  feeds your multimorbidity-clustering thread.

How to triage it. Pull the shared-loci list and check whether any
overlap with insulin resistance / lipid loci you've been tracking.

### 15. UK Biobank multimorbidity — multimorbidity-based vs clustering definitions
**Silva GC, Fayosse A, et al.** Surfaced via UKB keyword alert,
06-15 03:27Z.
Threads: **multimorbidity / chronic disease clustering**, EHR-linked
biobanks.

What it is. UKB cohort study comparing operational definitions of
multimorbidity (count-based vs cluster-based) and their association
with prevalence, health profiles, and mortality.

Why it matters to you.
- Directly on your **multimorbidity** thread, with particular
  attention to clustering definitions vs count-based — the methodological
  question your thread already flagged.

How to triage it. Pull the definition comparison table — see whether
they used latent class / topic models on phecodes or a simpler
hierarchical clustering. Note the discrimination-of-mortality metric:
if cluster definitions outperform counts only marginally, it weakens
the case for going to clustering in AoU.

---

## METHODS-WATCH

- **Bayesian Causal ML for Cure Models (BartCure)** — Linero, Rubio,
  Basak; arXiv:2606.11405. Causal HTE on RMST decomposed into a
  *stochastic cure* and *stochastic latency* component, applied to
  CALGB 40101 breast cancer trial. Off-thread disease but exactly your
  causal-forest / meta-learner methods-watch slot. Already in the
  06-11 arxiv-digest.
- **OmniBioTwin (multiscale GLP-1 digital twin)** — Wang, Huang, Bian;
  arXiv:2606.11264. Cross-scale GLP-1 signaling twin for AD. Speculative
  / framework paper; flag only because it tags GLP-1.
- **"Is It You or Your Environment?" — Bayesian inference with GWAS
  priors** — Dey, Biswas; arXiv:2606.13556. Frames per-individual
  Bayesian set-points using GWAS-derived priors with explicit MR-vs-
  individual-token-causation discussion; interesting for the
  ancestry-matched prior point but speculative.
- **Causal effect estimation from trans-regulatory single-cell CRISPR
  screens** — Christensen, Markham, Kang, Gabriel; *Cell Genomics*,
  2026. Off-thread (functional genomics, not population) but worth
  noting since it surfaced under both Pritchard and Shendure alerts.
- **Whole-person Health Score (allostatic load) prediction of
  hospitalization from incomplete EHR** — Weavil, Rigdon, Lotspeich;
  arXiv:2606.10093. METHODS-WATCH for missingness-by-design EHR
  pipelines.
- **Guideline Machines** — Kohane, *NEJM AI* 2026. Editorial/
  perspective on LLMs operationalizing clinical guidelines — flag for
  your EHR foundation model thread's clinical-integration sub-question.

---

## SKIP (incidental keyword hits, noted for completeness)

- *Erratum to Loss of GalNAc-T14 / IgA nephropathy* (Gharavi alert).
- *Risk Under Pressure: Compute-Aware Adversarial Robustness* (Szolovits
  related-research) — adversarial ML, off-thread.
- *Long-term isolation / archaic introgression in Near Oceania*
  (Denny alert) — population genetics, off-thread.
- *AI in Oncology overview* (Hernán-cite batch) — review article.
- Author / venue alerts for sleep tES review, Mediterranean diet
  consensus, microbiome One Health GCC, Spanish AS consensus, etc.

---

## State of `arxiv-digest`

- **06-13 + 06-14: empty** (0 new papers, 1–2 suppressed as previously
  surfaced).
- **06-12: 1 paper** — the "Is It You or Your Environment?" Bayesian-
  prior + GWAS framework (score 3).
- **06-11: 4 papers** — m6A-FORM, Continuous biome representations,
  BartCure, OmniBioTwin (all score 1, single keyword hits).
- **06-10: 2 papers** — Flexible Flows for Biological Sequence Design
  (cs.LG; weak hit via `latent class`), Predicting Hospitalization from
  Whole-Person Health Score (stat.AP; clean EHR hit).
- **06-09: 3 papers** — Correlation Is Not Enough / BODHI (cs.AI,
  KG + foundation model; score 2), scTransformer (q-bio.GN, foundation
  model), SpineAgent (cs.CV, foundation model).

> ➤ Recurring recommendation: add `cs.LG`, `stat.ME`, and medRxiv /
> bioRxiv subject feeds. This week alone the Y-PheWAS (medRxiv),
> spectral EHR embedding (cs.LG / stat.ME), and stimulant-use-disorder
> GWAS (medRxiv) would have been caught.

---

## Suggested next actions

1. Pull the **APRS** primary paper (Nature Genetics article whose N&V
   is item #1) and check whether AoU's Olink panel covers the 9
   proteins — that determines whether APRS is replicable in your
   substrate.
2. Pull the **Gerhardt CHIP × lifestyle** *Nature* paper and the AoU
   cohort definition — usable as a replication template for any
   CH × phecode work.
3. Pull the FinnGen **Y-chromosome PheWAS** medRxiv preprint — the
   methods section is the bottleneck for porting Y-PheWAS to AoU.
4. Pull **MIXPRS** code + benchmarks; add to your PRS pipeline
   benchmarking queue.
5. Add `cs.LG`, `stat.ME`, and a medRxiv "Genetic and Genomic Medicine"
   subject feed to `config/tracked.yaml` — three of this week's HIGH
   items came from outside the q-bio scope.
