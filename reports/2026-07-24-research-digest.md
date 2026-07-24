# Research digest report — 2026-07-24

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-23 12:00Z → 2026-07-24 12:35Z** (roughly the 24 hours
since the last committed report at `reports/2026-07-23-research-digest.md`,
which closed with the mid-morning-07-23 NCBI batch). A narrow daily
follow-on — expect fewer HIGH items than the 07-23 multi-batch report.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author-feed cluster) | 2026-07-24 09:02Z | Large single-batch fire — twenty-plus author feeds arrived in the same minute. On-thread signal is dominated by four HIGH hits: **Lai/Denny** S4-Multi multi-ancestry PRS protocol (STAR Protocols), **Liou** statin-response PGS (Circ Genom Precis Med, on the Bastarache related feed), **Yen** SGLT2i-vs-GLP-1RA target-trial emulation on Patrick Ryan feed, and **Chattopadhyay** MR instrument-borrowing (arXiv, on Pritchard citations). Plus a Denny-citations paper on tacrolimus / CYP3A5 population PK, and the Boltz *Nature Genetics* blended-WGS-plus-exome method paper on the Karczewski related feed. |
| Google Scholar keyword feeds | (none new in-window) | The daily keyword feeds (`phenome wide association studies`, `UK Biobank`, `All of Us research program`, `drug repurposing`, `variant interpretation`, `foundation models`, `knowledge graph`, `mendelian diseases`, `rare diseases`, `autoimmune diseases`, `electronic health records`, `clonal hematopoiesis`, `APOL1`) fired *before* the window at 2026-07-23 01:59Z and were already covered in the 07-23 report. No new keyword-feed batch arrived today — expected, since those alerts run once every ~24h and the next batch will land tonight. |
| NCBI "My NCBI What's New" (UK Biobank, drug repurposing) | 2026-07-24 12:33Z | Two NCBI batches — UKB (13 items) and drug-repurposing (8 items). UKB batch is dominated by disease-specific proteomics / nutrition papers; two entries on-thread — **Wu & Gao** AI-multimodal 10-year glaucoma prediction (genetics + deep-learning fundus imaging) and **Liu et al.** GWAS of self-harm phenotypes with shared genetic architecture with depression / chronic pain. Drug-repurposing batch is mostly single-drug mechanism reviews; one framework paper — **Qiu et al.** functional-genomics-pharmacotranscriptomics host-directed anti-influenza pipeline — is a methods-watch. |
| `arxiv-digest` repo (`digests/2026-07-24.md`) | 2026-07-24 (10:30Z cron) | Only 1 paper surfaced (3 previously-seen suppressed) — Ali *scContam* pretraining-contamination audit for single-cell foundation model benchmarks. Score-1, single keyword hit (`foundation model`); off the biomedical-phenotype threads but methodologically portable to the EHR-foundation-model calibration audit thread. METHODS-WATCH. |
| bioRxiv / medRxiv Subject Collection Alerts | 07-23 → 07-24 daily | Aggregate feeds — individual papers surface upstream via Scholar / NCBI. Not a separate net. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it.

---

## Executive summary

- **S4-Multi multi-ancestry polygenic-model construction protocol —
  Denny group, STAR Protocols.** Lai, Tyrer, Baierl, Pharoah, Peng,
  *Protocol for constructing multi-ancestry polygenic models using
  S4-Multi* (STAR Protocols 2026; Denny related-research feed).
  A step-by-step method paper for building multi-ancestry PRS with
  S4-Multi — end-to-end from reference genotype prep through GWAS
  summary-statistic formatting to score construction. Directly
  serves the trans-ancestry PRS portability sub-thread and pairs
  with yesterday's Jo/Khor East Asian meta-analysis on the same
  Denny feed. **HIGH — read first (short protocol paper, low
  activation energy).**
- **Polygenic prediction of nongoal statin response — Circulation
  Genomic and Precision Medicine.** Liou, García-González, Wu,
  Namba, Vaura et al., *Polygenic Prediction of Nongoal Response
  to Statin Therapy* (Circ Genom Precis Med 2026; Bastarache
  related-research feed). PGS applied to a *drug-response*
  phenotype (failure to reach LDL goal on statin), not a disease
  phenotype — the pharmacogenomics-adjacent variant of PRS
  application. Directly on the ML-for-precision-health thread
  ("who to treat / when to escalate") and on the composite-risk
  sub-thread inside genetic epi (PGS residualized against a
  clinical treatment target). **HIGH.**
- **Target-trial emulation of SGLT2i vs GLP-1RA in T2D for
  psoriatic arthritis risk — Patrick Ryan related feed.**
  Yen, Wang, Hwu, Chen, Hsu et al., *Comparative Risk of
  Psoriatic Arthritis in Type 2 Diabetes: An Emulated Target
  Trial of SGLT2 Inhibitors vs. GLP-1 Receptor Agonists* (Drug
  Design, Development and Therapy 2026; Ryan related-research
  feed). Head-to-head active-comparator target-trial emulation
  between two of your tracked drug classes (SGLT2i, GLP-1 RA),
  with a novel autoimmune-outcome twist. Serves the causal-
  inference / pharmacoepi thread and the drug-class comparative-
  effectiveness sub-thread. **HIGH.**
- **MR instrument-borrowing across related outcomes — arXiv,
  Chattopadhyay & Chatterjee.** Chattopadhyay & Chatterjee,
  *Improving Mendelian Randomization Analysis by Instrument
  Borrowing from Auxiliary Outcome Traits* (arXiv:2607.16086,
  2026; Pritchard citations feed). Cross-outcome instrument
  borrowing under valid-IV overlap assumptions — a method
  variant to add to the MR toolkit alongside MR-ALasso (07-22
  report). Directly serves the causal-inference thread; pairs
  with the metformin-AAA drug-target MR paper on the 07-23
  report as a plausible near-term application. **HIGH
  (methods).**
- **Blended WGS + exome sequencing at production scale —
  *Nature Genetics*, Boltz/Karczewski.** Boltz, Chu, DeFelice,
  Liao, Sealock et al., *A blended genome and exome sequencing
  method captures genetic variation in an unbiased and cost-
  effective manner* (Nature Genetics 2026; Karczewski
  related-research feed). Blended-WGS/exome capture as a
  cost-efficient alternative to WGS-only or exome-only at
  biobank scale — direct infrastructure paper for any AoU /
  UKB / MVP variant-calling thread, and for the pLoF-burden
  and rare-variant work in the genetic-epi thread. **HIGH
  (infrastructure).**
- **Tacrolimus population-PK + CYP3A5 pharmacogenomics review —
  Clinical Pharmacokinetics, top of Denny citations feed.**
  Randolph, Jubas, Gong, Venkataramanan et al., *A Review of
  Population Pharmacokinetic Models and Dosing Algorithms
  Assessing the Influence of CYP3A5 Genotype and Other Clinical
  Covariates on Tacrolimus Pharmacokinetics* (Clin Pharmacokinet
  2026; Denny citations feed — cites the 76,156-genomes
  constraint map). A reference-utility review for the
  pharmacogenomics-in-EHR sub-thread. Cites Karczewski's
  gnomAD constraint map as a source for allele-frequency
  weighting in dosing algorithms — an interesting cross-over
  between the constraint-metrics and pharmacogenomics
  literatures. **MEDIUM-HIGH (reference utility).**
- **AI-multimodal 10-year incident-glaucoma prediction on UKB —
  Ophthalmology Science.** Wu & Gao, *Artificial Intelligence-
  Driven Multimodal Prediction of 10-Year Incident Glaucoma
  Integrating Genetic and Deep Learning-Derived Imaging Features*
  (Ophthalmol Sci 2026 Aug; PMID 42495699; NCBI UKB feed).
  Composite genetics + fundus-imaging deep-learning risk model
  for a 10-year incident outcome — the multimodal-EHR-FM template
  applied to a clean UKB phenotype. Serves the ML-for-precision-
  health thread and the EHR-FM-multimodal sub-thread.
  **MEDIUM-HIGH.**
- **Self-harm GWAS + genetic overlap with depression / chronic
  pain — Biol Psychiatry Global Open Sci.** Liu, Ye, Huang, Zhu,
  Wang et al., *Unraveling the Genetic Basis of Self-Harm
  Phenotypes: New Perspectives on Its Links to Depression and
  Chronic Pain* (Biol Psychiatry Glob Open Sci 2026 Sep; PMID
  42494825; NCBI UKB feed). GWAS + shared-architecture analysis
  of self-harm phenotypes using UKB — parallel design to the
  Streit BPD GWAS + PheWAS paper on the 07-23 report.
  **MEDIUM.**
- **METHODS-WATCH — scContam: pretraining-contamination audits
  for single-cell foundation-model benchmarks.** Ali, *Auditing
  pretraining contamination in single-cell foundation model
  benchmarks* (arXiv 2607.20572, 2026-07-21; `arxiv-digest`).
  MinHash fingerprint + loss-based membership-inference-attack
  audit framework, applied to Geneformer / scGPT / UCE against
  scIB benchmarks. Not on the biomedical-phenotype threads, but
  the audit *pattern* — quantify pretraining-corpus leakage
  before reporting zero-shot benchmark numbers — is directly
  transferrable to any EHR-FM calibration audit (CLMBR / MOTOR
  / EHRSHOT). **METHODS-WATCH.**

Everything else in the window is off-thread — the Jo/Khor 127-trait
East Asian meta-analysis has already been reported on 07-23 (surfaces
today on the Jian Yang related feed too; suppressed here), a
Saint-Antoine Orchid-CAD-GRS whitepaper (PRS-validation-only, no new
methodology), the DePinho *Nature Aging* TERT commentary on the Zeng
citations feed (aging biology, off the phenotyping threads), and a
long tail of UKB nutrition-and-proteomics observational papers
without a genetic angle. See the "Not covered here" section at the
bottom for the full list.

---

## Detailed reports

### 1. Protocol for constructing multi-ancestry polygenic models using S4-Multi

**Authors.** PH Lai, JP Tyrer, J Baierl, PDP Pharoah, PC Peng.
**Venue.** *STAR Protocols*, 2026 (Cell Press S2666-1667(26)00334-5).
**Signal source.** Google Scholar author-feed for Joshua C. Denny —
new related research (07-24 09:02Z, top of the Denny related-feed
batch).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (multi-ancestry PRS
construction); PheWAS/PheRS infrastructure (calibration and
ancestry-aware risk scores); biobanks with EHR linkage (AoU / UKB
downstream deployment).

**What the paper does (from title + snippet).** A stepwise STAR
Protocols paper — reference genotype prep → GWAS summary-stat
formatting → S4-Multi model fit → PRS generation. S4-Multi is a
summary-statistic-only, LD-shrinkage-based, multi-ancestry PGS
construction method from the Peng / Pharoah group; the point of
the paper is not to introduce a new method but to give an
implementable, reproducible protocol.

**Why it matters for your work.**
1. **Low-friction reference for AoU multi-ancestry PRS
   construction.** AoU's headline advantage over UKB is ancestry
   diversity, so any AoU-native PRS work should default to
   multi-ancestry construction rather than European-only + late
   ancestry adjustment. S4-Multi is one of the two or three
   published methods that ships with usable open-source code; a
   STAR Protocols write-up means the on-ramp is now a
   copy-and-run recipe.
2. **Pairs with the East Asian 127-trait meta-analysis (07-23
   report).** Any downstream AoU / UKB PRS PheWAS on a trait
   covered by the Jo/Khor meta-analysis can now be built with
   both European and East Asian summary statistics as inputs —
   the S4-Multi protocol tells you how.
3. **Compare against PRS-CSx and PROSPER.** S4-Multi belongs to
   the same class of ancestry-aware summary-statistic-only PGS
   methods as PRS-CSx (Ge et al.) and PROSPER (Zhang et al.).
   Worth reading the paper's cross-method comparison (if any)
   to know which method your next AoU multi-ancestry PRS work
   should default to.

**Follow-ups.** Pull the protocol; note (a) reference genotype
requirements (1000G? HGDP+1KG?), (b) required minimum EAS/AFR
GWAS sample size for the multi-ancestry mode to help, (c) whether
the code supports plink2 pgen inputs (relevant for AoU), (d)
any published head-to-head comparison against PRS-CSx / PROSPER
on AoU-comparable ancestry mixtures.

---

### 2. Polygenic Prediction of Nongoal Response to Statin Therapy

**Authors.** L Liou, J García-González, HM Wu, S Namba, F Vaura et al.
**Venue.** *Circulation: Genomic and Precision Medicine*, 2026.
**Signal source.** Google Scholar author-feed for Lisa Bastarache —
new related research (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Machine learning for precision health (who
to treat / when to escalate); genetic epidemiology (PGS applied
to a drug-response phenotype); causal inference & pharmacoepi
(indirectly — PGS as a stratifier for treatment effect
heterogeneity).

**What the paper does (from title + snippet).** PGS-based
prediction of "nongoal" response to statin therapy — i.e.
patients who fail to reach their LDL treatment goal on
statins despite adherence. Not a disease-onset PRS, but a
treatment-response PRS. Namba on the author list is the
FinnGen / BBJ connection; García-González is Ge lab / Broad.

**Why it matters for your work.**
1. **Extends PRS beyond disease onset into drug response.** The
   overwhelming majority of PRS work targets disease incidence;
   PGS-of-drug-response is a much thinner literature. Direct
   fit for the pharmacogenomics adjacency of the genetic-epi
   thread and for the "when to escalate" arm of the
   ML-for-precision-health thread.
2. **Complements the drug-target MR literature.** Drug-target
   MR (e.g. the Saxby metformin-AAA paper from the 07-23
   report) asks "does target-modulating variation predict
   outcome?"; treatment-response PGS asks "given actual
   pharmacological modulation, does polygenic background
   predict on-therapy outcome?" The two together triangulate
   the causal chain from target → drug → outcome.
3. **Cardiometabolic template portable to other drug classes.**
   The same design applied to SGLT2i responders (glycemic
   goal), GLP-1 RA responders (weight goal), or CFTR modulator
   responders (sweat-chloride / FEV1 goal) would slot directly
   into your active drug-class threads. A near-term follow-on
   in AoU or UKB is realistic given the EHR-linked lab-value
   depth.

**Follow-ups.** Pull the paper; check (a) the cohort (UKB?
FinnGen? BBJ? multi-biobank meta?), (b) how "nongoal" is
operationalized (single LDL measurement post-initiation?
trajectory-based?), (c) whether the PGS was constructed from
LDL-lowering GWAS or from a CAD outcome GWAS, (d) whether
the paper reports any downstream clinical utility (NRI,
decision curves) beyond AUC.

---

### 3. Comparative Risk of Psoriatic Arthritis in Type 2 Diabetes: An Emulated Target Trial of SGLT2 Inhibitors vs. GLP-1 Receptor Agonists

**Authors.** FS Yen, SI Wang, CM Hwu, KY Chen, CC Hsu et al.
**Venue.** *Drug Design, Development and Therapy*, 2026.
**Signal source.** Google Scholar author-feed for Patrick Ryan —
new related research (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Causal inference and pharmacoepidemiology
(target-trial emulation, active-comparator design); drug-class
sub-threads (SGLT2is and GLP-1 RAs, both explicitly tracked);
chronic disease clustering and multimorbidity (T2D → autoimmune
comorbidity).

**What the paper does (from title + snippet).** Emulated target
trial in a T2D cohort comparing SGLT2 inhibitors to GLP-1 RAs
head-to-head for incident psoriatic arthritis. Active-comparator
new-user design — the modern pharmacoepi standard for avoiding
prevalent-user bias and unmeasured-confounding contrasts against
"no treatment."

**Why it matters for your work.**
1. **Two of your tracked drug classes go head-to-head.** Most
   SGLT2i vs GLP-1 RA target-trial emulations focus on
   cardiorenal outcomes (MACE, heart failure hospitalization,
   eGFR decline). Extending to an autoimmune-mediated outcome
   (psoriatic arthritis) is unusual — the mechanism story is
   presumably GLP-1 RA immunomodulation vs SGLT2i inflammation-
   pathway effects. Worth reading the discussion for the
   proposed mechanism.
3. **Template for other active-comparator autoimmune outcomes.**
   The same design could be applied in AoU / MVP for other
   T2D-adjacent autoimmune outcomes — IBD (tracked disease),
   psoriasis, RA — with the same drug classes. A one-off
   pattern here becomes a scan across autoimmune endpoints in
   your AoU work.
2. **Ryan feed context.** Patrick Ryan is OHDSI / Janssen; the
   related-research feed picks up target-trial emulations
   across the OMOP-based comparative-effectiveness literature.
   Worth checking whether the study uses OMOP-CDM-native code
   (Strategus / CohortMethod) — that would make it directly
   reproducible in your OHDSI toolkit.

**Follow-ups.** Pull the paper; check (a) cohort (TriNetX?
national Taiwanese claims? US claims?), (b) index-date
definition and washout, (c) how psoriatic arthritis is
ascertained (single ICD-10 M07.x? multi-code algorithm?
dermatology / rheumatology visit anchor?), (d) whether the
authors report negative-control-outcome calibration, (e)
whether the code is OMOP-CDM-native and portable.

---

### 4. Improving Mendelian Randomization Analysis by Instrument Borrowing from Auxiliary Outcome Traits

**Authors.** A Chattopadhyay, N Chatterjee.
**Venue.** arXiv preprint arXiv:2607.16086, 2026.
**Signal source.** Google Scholar citations feed for Jonathan K.
Pritchard — top of the batch (07-24 09:02Z).
**Bucket.** HIGH (methods).
**Threads served.** Causal inference and pharmacoepidemiology
(MR methods); genetic epidemiology (instrument selection).

**What the paper does (from abstract snippet).** MR under invalid
instruments — the standard pathology of MR — is addressed by
*borrowing* instruments across closely related outcome traits.
Hypothesis: valid instruments for outcome Y1 are largely also
valid for related outcome Y2, so aggregating instrument sets
across a family of related outcomes yields more robust causal
effect estimation and better invalid-IV detection than
single-outcome analysis alone. Chatterjee (Johns Hopkins) is a
long-standing name in the MR-with-summary-stats methods
literature.

**Why it matters for your work.**
1. **A third method for the MR toolbox.** Together with
   MR-ALasso / MR-ALasso-B (Qasim et al., 07-22 report) and
   the classic pleiotropy-robust estimators (MR-Egger,
   MR-PRESSO, weighted median), instrument-borrowing gives a
   third methodological angle for stress-testing any
   candidate MR result. Different failure modes, different
   assumption sets.
2. **Natural application to drug-target MR panels.**
   Drug-target MR (e.g. Saxby metformin-AAA on the 07-23
   report) often has weak-instrument problems because the
   variant set is restricted to cis-eQTL / cis-pQTL of the
   drug target. Instrument borrowing across related outcomes
   (e.g., all cardiovascular endpoints for a lipid-lowering
   target) may be a way to recover power without leaving the
   drug-target scope.
3. **Cross-cohort MR with heterogeneous outcome definitions.**
   The AoU vs UKB vs FinnGen phenotype-definition heterogeneity
   problem (same latent construct, different EHR-derived
   proxies) is another natural fit — auxiliary outcomes here
   would be the same disease under different phecode/ICD
   definitions.

**Follow-ups.** Pull the PDF; check (a) the theoretical
identifying assumption on "related" outcomes (are they assuming
shared genetic architecture, shared IVs, or something weaker?),
(b) sensitivity to outcome mis-selection (what if Y2 is *not*
in fact instrument-sharing with Y1?), (c) simulation study
setup and any real-data application, (d) whether the R
implementation is on GitHub yet.

---

### 5. A blended genome and exome sequencing method captures genetic variation in an unbiased and cost-effective manner

**Authors.** TA Boltz, BB Chu, M DeFelice, C Liao, JM Sealock et al.
**Venue.** *Nature Genetics*, 2026.
**Signal source.** Google Scholar author-feed for Konrad
Karczewski — new related research (07-24 09:02Z).
**Bucket.** HIGH (infrastructure).
**Threads served.** Genetic epidemiology (rare-variant burden and
composite risk); biobanks with EHR linkage (production-scale
variant-calling economics for AoU / UKB / MVP); variant
interpretation (LOFTEE / pLoF burden with high-confidence
coding variant calls).

**What the paper does (from title + snippet).** A blended
whole-genome + whole-exome capture-and-sequence protocol that
recovers the coding-region depth of a proper WES with the
noncoding coverage of a low-pass WGS at meaningfully lower
per-sample cost than doing both separately or running high-depth
WGS. Sealock is Vanderbilt / BioVU-adjacent; the Broad names
(Boltz, DeFelice, Liao) put this firmly in the Broad genomic
platform lineage.

**Why it matters for your work.**
1. **Production-scale genomics economics.** Any AoU / MVP /
   BioVU-scale genotyping decision is dominated by cost per
   sample. A capture protocol that keeps WGS-comparable
   noncoding fidelity at reduced spend is directly relevant to
   how the next round of biobank genotyping gets done — and
   therefore to what your downstream PheWAS / PRS / burden
   analyses will look like in 2027+.
2. **Coding-region depth matters for pLoF burden.** LOFTEE
   HC pLoF calls, AlphaMissense pathogenic-classifier calls,
   and ClinVar P/LP concordance all depend on sufficient
   coding-region depth. A blended protocol that preserves
   WES-grade coding coverage keeps the pLoF-burden thread
   viable on cost-constrained biobanks.
3. **Karczewski feed placement.** Boltz being on the
   Karczewski related-research feed suggests methodological
   overlap with the gnomAD variant-calling / QC lineage —
   worth checking whether the blended-protocol variant calls
   were benchmarked against gnomAD-style QC metrics (VQSR,
   allele balance, strand bias).

**Follow-ups.** Pull the paper; check (a) cost-per-sample
comparison against 30× WGS and 100× WES, (b) coding-region
sensitivity/specificity vs 100× WES ground truth, (c)
noncoding coverage vs 30× WGS at common-variant, rare-variant,
and CNV levels, (d) whether the pipeline is available (WDL /
Snakemake) and portable to non-Broad cloud stacks.

---

### 6. A Review of Population Pharmacokinetic Models and Dosing Algorithms Assessing the Influence of CYP3A5 Genotype and Other Clinical Covariates on Tacrolimus Pharmacokinetics

**Authors.** RM Randolph, S Jubas, L Gong, R Venkataramanan et al.
**Venue.** *Clinical Pharmacokinetics*, 2026.
**Signal source.** Google Scholar citations feed for Joshua C.
Denny — top of the batch, cites the 76,156-genome constraint
map (07-24 09:02Z).
**Bucket.** MEDIUM-HIGH (reference utility).
**Threads served.** Genetic epidemiology (pharmacogenomics as a
clinical translation of common-variant effect estimates);
machine learning for precision health (individualized dosing).

**What the paper does (from title + snippet).** Systematic
review of published population-PK models and dosing algorithms
for tacrolimus (a narrow-therapeutic-index immunosuppressant
used in transplant) that incorporate CYP3A5 genotype alongside
other clinical covariates. Reference-utility rather than
primary methods — the value is in the compiled list of models
+ covariate structures.

**Why it matters for your work.**
1. **Reference for the pharmacogenomics-in-EHR adjacency.**
   Any AoU / MVP / BioVU work that projects pharmacogenomic
   dosing recommendations into the EHR needs to know which
   dosing algorithms are validated for which drugs at which
   genotypes. Tacrolimus is one of the CPIC "level A"
   drug-gene pairs and a common reference case.
2. **Constraint-map citation is the interesting cross-over.**
   The paper cites Karczewski et al.'s 76,156-genome
   constraint map — presumably as a source for allele-frequency
   weighting in dose-prediction covariate structures. Novel to
   see the constraint-metrics literature bleed into
   pharmacogenomics dosing; worth reading how they use it.
3. **Model-comparison template.** The compiled list of
   population-PK models across transplant settings gives a
   template for any similar review of PK models by drug class
   (warfarin/CYP2C9-VKORC1, clopidogrel/CYP2C19, etc.) — useful
   for grant framing on pharmacogenomics-in-EHR.

**Follow-ups.** Pull the paper; note (a) which dosing algorithms
they classify as clinical-ready vs experimental, (b) the
covariate list beyond CYP3A5 (age, weight, hematocrit, comed?),
(c) how the constraint-map citation is used, (d) whether the
paper flags any AoU / UKB / MVP dataset as a candidate for
external validation of the compiled models.

---

### 7. Artificial Intelligence-Driven Multimodal Prediction of 10-Year Incident Glaucoma Integrating Genetic and Deep Learning-Derived Imaging Features

**Authors.** F Wu, XR Gao.
**Venue.** *Ophthalmology Science* 2026 Aug 6(8):101292 (PMID
42495699).
**Signal source.** NCBI "What's new for UK Biobank" batch
(07-24 12:33Z, item 1).
**Bucket.** MEDIUM-HIGH.
**Threads served.** Machine learning for precision health
(individualized risk prediction, 10-year incident outcome);
EHR foundation models (multimodal — genomics + imaging);
biobanks with EHR linkage (UKB).

**What the paper does (from title + snippet).** Multimodal AI
risk model that fuses (a) a genetic component (presumably a
glaucoma PRS, potentially plus rare-variant burden) and (b) a
deep-learning-derived embedding from UKB fundus photographs to
predict 10-year incident glaucoma. Single-outcome, long-horizon,
UKB-based — the design template of choice for the multimodal
EHR-FM sub-thread.

**Why it matters for your work.**
1. **Cleanly matches the multimodal EHR-FM design template.**
   Fundus imaging + genetics is the same architectural pattern
   as EHRSHOT (codes + notes) or MedTok (multimodal tokens),
   just with a different modality mix. The paper is directly
   on the "multimodal EHR FMs" sub-thread in your interests.
2. **A well-defined 10-year incident-glaucoma outcome is a
   clean benchmark.** Glaucoma has a validated UKB phecode/ICD
   ascertainment and a defensible 10-year time horizon.
   Portable to AoU (fundus imaging arm is smaller than UKB but
   growing) as an external-validation cohort.
3. **Genetics + imaging together vs alone is the interesting
   ablation.** The clinical-utility bar for a fusion model is
   that it beats the best single-modality model. Worth reading
   the ablation carefully — this is the same question you'd ask
   of any AoU multimodal risk stack.

**Follow-ups.** Pull the paper; check (a) PRS construction
(what glaucoma GWAS? multi-ancestry?), (b) imaging model
architecture and pretraining corpus, (c) fusion strategy
(late-stack vs cross-attention), (d) calibration and
decision-curve analysis at clinically-meaningful risk
thresholds, (e) external validation (AoU? EPIC-Norfolk?).

---

### 8. Unraveling the Genetic Basis of Self-Harm Phenotypes: New Perspectives on Its Links to Depression and Chronic Pain

**Authors.** W Liu, Y Ye, Z Huang, J Zhu, S Wang et al.
**Venue.** *Biological Psychiatry Global Open Science* 2026 Sep
6(5):100770 (PMID 42494825).
**Signal source.** NCBI "What's new for UK Biobank" batch
(07-24 12:33Z, item 2).
**Bucket.** MEDIUM.
**Threads served.** Genetic epidemiology (GWAS + shared
architecture); biobanks with EHR linkage (UKB); chronic
disease clustering and multimorbidity (self-harm × depression
× chronic pain).

**What the paper does (from title + snippet).** UKB-based GWAS
of self-harm phenotypes + shared genetic architecture analysis
against depression and chronic pain — the same design template
as the 07-23-report Streit BPD GWAS + PheWAS paper, applied to
a different psychiatric-adjacent phenotype.

**Why it matters for your work.**
1. **Same "GWAS + shared architecture across a phenotype triad"
   design template.** With the Streit BPD paper (07-23) also
   using this pattern, it's clearly a stable design template
   for the current wave of psychiatric UKB GWAS. Worth
   internalizing as the reference class for future
   psychiatric-outcome PheWAS in AoU/UKB.
2. **Chronic-pain × mental-health multimorbidity fits the
   multimorbidity thread.** Genetic overlap between self-harm,
   depression, and chronic pain speaks directly to the
   cardiometabolic / autoimmune / aging multimorbidity work in
   the multimorbidity thread — the psychiatric-pain axis is a
   third domain worth pattern-matching.
3. **Less directly on-thread than #1–#7.** No PheWAS follow-up,
   no biobank beyond UKB, no obvious causal-inference framing —
   hence MEDIUM rather than HIGH.

**Follow-ups.** Pull the paper only if reading it complements
the Streit BPD paper — the design comparison is the main
value. Check (a) UKB self-harm ascertainment (ICD? Field
20554?), (b) LDSC / genetic-correlation methods, (c) whether
any Mendelian-randomization step is included between the three
phenotypes.

---

## Methods-watch (single-abstract flag)

### 9. Auditing pretraining contamination in single-cell foundation model benchmarks

**Author.** Sarwan Ali.
**Venue.** arXiv:2607.20572, 2026-07-21 (`digests/2026-07-24.md`).
**Bucket.** METHODS-WATCH.
**Threads served (indirectly).** EHR foundation models
(pretraining-audit pattern portable to CLMBR / MOTOR /
EHRSHOT).

**What the paper does (from the arxiv-digest abstract).**
Introduces **scContam**, a per-cell audit framework combining
a MinHash-based gene-set fingerprint against the explicit
pretraining corpus with a loss-based membership-inference-attack
(MIA-scFM) test. Applied to four scIB benchmarks × three
single-cell foundation models (Geneformer, scGPT, UCE). Finding:
two of the most-cited benchmarks (PBMC 3k, CELLxGENE human
pancreatic islet atlas) have 80.4% and 77.0% of cells with
fingerprint p < 0.05 against Genecorpus-30M — extensive
pretraining-overlap evidence. Post-cutoff datasets (AIDA v2,
Tahoe-100M) show zero overlap evidence. A controlled
re-pretraining experiment establishes that MIA-scFM AUROC
scales monotonically with capacity-to-data ratio (0.494 →
0.690 → 0.881 across properly-regularized, mildly-overfit, and
aggressively-overfit regimes), showing that production scFMs
resist instance-level memorization but *distributional*
contamination must still be audited separately. A donor-matched,
within-cell-type analysis across three architectures shows
contaminated cells embed measurably more tightly than
donor-matched clean cells.

**Why it matters (indirectly).**
1. **The audit pattern is what's portable.** The specific
   MinHash-fingerprint + MIA-scFM instrumentation is
   single-cell-specific, but the *conceptual* audit — "before
   you report a zero-shot benchmark number for a foundation
   model, quantify what fraction of the benchmark was in the
   pretraining corpus" — is exactly the calibration critique
   the EHR-FM literature (CLMBR, MOTOR, EHRSHOT, MedTok)
   should be receiving. The scContam framing (fingerprint +
   MIA + within-condition control) is a directly cribbable
   protocol structure.
2. **Instance vs distributional contamination is a useful
   distinction.** Production-scale FMs (billions of params +
   trillions of tokens) generally resist instance-level
   memorization, so a null MIA doesn't clear the model —
   distributional contamination (i.e., the pretraining and
   benchmark corpora sample the same underlying
   distribution) is the more insidious mode. Worth borrowing
   this framing when evaluating any EHR-FM benchmark result.
3. **Score-1 keyword hit; would not have surfaced in a
   `--min-score 2` run.** The digest pipeline defaults to
   `--min-score 1` for exactly this reason — a single
   `foundation model` hit surfaced a paper whose *pattern*
   is on-thread even though the *domain* (single-cell) is
   not. Confirms the current wide-net pipeline threshold is
   the right choice.

**Follow-ups.** Optional — read only if planning an EHR-FM
benchmark critique or evaluating a specific CLMBR / MOTOR
result where pretraining-corpus overlap with the eval set
is plausible.

---

## Not covered here (skimmed and skipped)

- **Jo, Khor, Chu, Ji, Ueno et al.**, *Large-scale meta-analysis
  of over one million individuals reveals the genetic
  architecture of 127 complex traits in East Asian populations*
  (bioRxiv, surfaces today on the Jian Yang related feed).
  **Already reported on 07-23** — no new information; suppressed
  here.
- **M Saint-Antoine, N Slotnick**, *Whitepaper: Validating
  Orchid's Coronary Artery Disease Genetic Risk Score* (Jian
  Yang citations feed). Company (Orchid) whitepaper validating
  a consumer-facing CAD-PRS product. PRS-validation-only, no
  new methodology; commercial framing. SKIP.
- **RA DePinho**, *Positioning TERT at the apex of aging*
  (Nature Aging; Chenjie Zeng citations feed). Commentary /
  perspective on telomerase biology as an aging-regulator
  hub. Off the phenotyping / EHR / genetic-epi threads.
  SKIP.
- **KJM van der Velden et al.**, *Real-world use of PSMA
  imaging in metastatic castration-sensitive prostate cancer:
  Findings from the CAPRI-3 registry* (Zeng related-research
  feed). PSMA-imaging registry data — clinical prostate
  oncology, not the genetic / EHR-phenotyping threads.
  SKIP.
- **UKB NCBI batch remainder** (11 of 13 items) — proteomics-
  and-nutrition observational papers with no genetic angle
  (liver-related events proteomics in prediabetes, cataract +
  physical-activity, pituitary neuroendocrine tumor +
  metabolic syndrome, dietary antioxidant index + dementia,
  gastric cancer + metabolic syndrome, AF-stroke proteomics
  panel, Alzheimer's precuneus amyloid, ALS platelet factor 4
  mechanism, sugar rationing + depression natural experiment,
  ocular-disease + dietary-nutrient longitudinal analysis,
  SLE 5-protein diagnostic panel). No PheWAS / PRS / EHR-
  phenotyping angle. SKIP.
- **Drug-repurposing NCBI batch remainder** (7 of 8 items) —
  drug-specific mechanistic reviews without the KG / EHR /
  causal-inference angle you track (NUPR1 in breast cancer,
  posaconazole phase-0 glioblastoma, insecticide discovery,
  SARS-CoV-2 corticogenesis, 5-FU in *P. aeruginosa* biofilms,
  fibromyalgia review, trifluoperazine against arboviruses).
  Only the Qiu et al. functional-genomics-pharmacotranscriptomics
  anti-influenza framework is a methods-watch — but purely
  computational without an EHR / causal-inference component,
  so not surfaced above. SKIP.
- **Peter Szolovits / Marinka Zitnik / Tiffany Callahan /
  George Hripcsak / Yuan Luo / Stephen Montgomery / David
  Baker / Miguel Hernán / Vivek Natarajan / Hua Xu / Pascal
  Brandt related-research feeds** — all fired today with the
  usual noise mix (pathology VLMs, chemical language models,
  fuzzy KG quantification, EHR-usability studies, single-cell
  eQTL in pigs, de novo protein design, general causal-
  inference primers, agentic AI workbenches, differential
  diagnosis frameworks, FHIR-CDSS). Nothing on-thread beyond
  what's already captured in items 1–9.
- **Substack / newsletter noise** (AI News, AlphaSignal,
  Medium daily digest, Rohan Paul newsletter) — general AI
  news, not research. SKIP.

---

## Housekeeping

- Latest `arxiv-digest`: `digests/2026-07-24.md` — 1 paper
  surfaced (Ali scContam, score 1). Suppressed as previously
  seen: 3 papers (per the digest header). The `seen.json` cache
  is doing its job.
- Prior report: `reports/2026-07-23-research-digest.md` — 8
  detailed entries (Baya PRS-deviation → damaging variants,
  Gu OUD-GWAS in AoU, Streit BPD GWAS+PheWAS, DRIVE v3
  Bastarache-lab IBD haplotype tool, Wu UKB rare-variant
  metabolic syndrome, Żebrowska Circadian Imbalance Index
  GWAS+PheWAS+MR, Uria-Regojo rare-disease 11k-patient
  functional landscape, Lemieux JAMIA Open national-EHR
  interop, Saxby metformin-AAA MR).
- Nothing overlapped between the 07-23 and 07-24 reports
  besides the Jo/Khor East Asian meta-analysis (surfaces today
  on Jian Yang, was reported yesterday on Denny). No further
  action.
- Next expected fires: the daily Scholar keyword-feed cluster
  should arrive tonight around 02:00Z (2026-07-25 UTC) —
  that's the batch that carries the PheWAS / UKB / AoU /
  drug-repurposing / variant-interpretation feeds and usually
  has the highest on-thread signal. Watch for it.
