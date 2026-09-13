# Research digest — 2026-09-13

Coverage window: 2026-08-30 → 2026-09-12
Sources: `digests/2026-09-09.md` → `digests/2026-09-12.md`; Gmail Scholar
alerts (past 14 d) — arxiv.org daily class mailings; no
`arxiv-digest`-branded GitHub notification traffic in Gmail (this repo is
not wired to email; digests land as commits, not as GitHub email).

Triage buckets follow `INTERESTS.md`: **HIGH** = active thread; **METHODS-WATCH** =
off-topic disease but portable methods; **SKIP** = incidental hit (not
detailed here).

---

## Executive summary

- **Self-tracker fired**: Zeng, Waxse, Denny — "Robust replication of
  associations across patient-mediated and provider-sourced EHR data in
  the All of Us research program" is now indexed at *npj Digital Public
  Health* 2026 and already picked up 1 citation. Not further summarized
  here (it's your own work), but worth confirming the OA link points at
  the version you want cited.
- **Highest-signal new studies this window** are in three threads:
  1. **CHIP** — a JAMA Cardiology CV-outcomes-trial design piece (Chiu
     et al.) plus a CH-Predict pre-sequencing prediction model (Batchi-
     Bouyou et al., editorialized by Gillis & West) that together
     sharpen the "who to enroll and when to sequence" question your CHIP
     thread has been waiting for.
  2. **Rare disease** — Carrasco-Zanini et al. (*Sci Transl Med*) push
     proteomics as a diagnostic adjunct in genome-negative rare-disease
     cases (n = 424), and an Australian economic evaluation (Gonzalez et
     al., *Genetics in Medicine*) now prices the same idea.
  3. **Target trial emulation / HRT** — Wang et al. (*JAMA Internal
     Medicine*) directly serve the HRT sub-thread by estimating the CV
     effect of menopausal hormone therapy in perimenopausal women with
     vasomotor symptoms via TTE.
- **Cohort-scale event**: *Our Future Health* released its first
  phenomic-profile paper on 1.9 M UK participants (Straub et al.,
  *Nature Medicine*). This is a UKB-scale sibling cohort that your
  biobank thread should now track alongside UKB / AoU / MVP / BioVU.
- **Direct AoU citation**: Long et al. used All of Us to genotype 3,481
  celiac cases and refine HLA-B8 / HLA-DQ2.5 linkage in Hispanic and
  Black participants — a clean example of AoU + ancestry-stratified
  fine-mapping that sits next to your own AoU replication work.
- **arxiv-digest yield this week is thin**: 3 relevant papers on
  2026-09-11, 1 on 2026-09-10, 2 on 2026-09-09, 0 on 2026-09-12 (all in
  digests/). Deep summaries did not fire (nothing hit --deep-score ≥ 4).
  Only scDEFT (IBD single-cell drug-response prediction) and the
  Cohen's-d attribution paper for UKB normative-age models are
  thread-relevant; the rest are METHODS-WATCH.

---

## HIGH — studies directly serving an active thread

### 1. Chiu et al. — Designing Cardiovascular Outcomes Trials in CHIP
- **Venue**: JAMA Cardiology, 2026.
- **Thread**: CHIP / VEXAS / LOY — somatic mosaicism.
- **What's new**: Framework paper on how to design CV-outcomes trials
  that enroll on CHIP status, drawing on hematology-clinic
  longitudinal cohorts as a recruitment substrate. Positions CHIP as an
  actionable enrichment marker for CV trials rather than a passive risk
  variable.
- **Why it matters here**: Bridges the "CHIP as CV risk factor" evidence
  base (Loh 2018, Kessler 2022 lineage) into trial-design guidance. If
  the male-specific LOY analogue eventually needs its own CV trial
  scaffolding (Li et al. 2026 *Atherosclerosis* LOY × PAD is the
  motivating signal), this paper is the template.
- **Action**: Cross-reference against the Jäger et al. 2026
  *Atherosclerosis* CAD-mortality piece below — together they set the
  effect-size prior a CHIP CV-outcomes trial would need to power on.

### 2. Gillis & West editorial on CH-Predict — Finding CHIP before sequencing
- **Venue**: Blood Advances, 2026 (editorial on Batchi-Bouyou et al.).
- **Thread**: CHIP / somatic mosaicism (screening layer).
- **What's new**: CH-Predict is a routine-clinical-data model that
  flags individuals likely to harbor gene-specific CHIP, letting labs
  triage who to sequence. Editorial argues this is the missing "pre-
  test probability" layer for CHIP screening.
- **Why it matters here**: Directly relevant to how EHR-linked biobanks
  (AoU, UKB, MVP, BioVU) could pre-enrich for CHIP without paying for
  universal sequencing — same argument you'd make for penetrance
  estimation of monogenic variants.
- **Action**: Read the primary Batchi-Bouyou paper (this alert is the
  editorial); assess whether the model uses phecode-based features that
  would port to BioVU/AoU without retraining.

### 3. Yang et al. — CHIP in solid-tumor precision oncology
- **Venue**: J Translational Medicine, 2026 (12967-026-08963-9).
- **Thread**: CHIP + variant-origin QC (crosses into Ji et al. 2026
  *Biology* germline-vs-somatic contamination watch).
- **What's new**: Intended-use framework for distinguishing
  hematopoietic-derived variants from tumor variants in solid-tumor
  sequencing, host-biomarker evaluation, and defining intervention
  boundaries.
- **Why it matters here**: Serves the somatic-mutation-contamination-
  of-germline-rare-variant-scans QC sub-thread. Even if you're not
  running tumor sequencing, the variant-origin assessment machinery is
  what you'd want in a germline pipeline that runs against a
  CHIP-enriched biobank.
- **Action**: Extract the intended-use table; compare against the
  contamination QC layer proposed by Ji et al.

### 4. Jäger et al. — CHIP × long-term mortality across the CAD spectrum
- **Venue**: Atherosclerosis, 2026 (conference abstract, S0021-9150(26)00279-0).
- **Thread**: CHIP + CV outcomes.
- **What's new**: Direct within-study CAD+ vs CAD- comparison of CHIP-
  associated mortality, which the literature has been triangulating
  across cohorts rather than measuring head-to-head.
- **Why it matters here**: A within-cohort CAD+/CAD- contrast is the
  cleanest effect-size read for powering the trial design in item #1.
- **Caveat**: Conference abstract — no full text, no methods depth yet.
  Watch for the full paper.

### 5. Sanvido et al. — TET2 inactivation → Notch-1 in macrophages (CHIP mechanism)
- **Venue**: Atherosclerosis, 2026 (conference abstract).
- **Thread**: CHIP mechanism.
- **What's new**: TFMB-(S)-2-HG TET2 inhibition in RAW 264.7 cells,
  Notch signaling & proinflammatory cytokine readouts.
- **Why it matters here**: METHODS-WATCH more than HIGH; it's basic
  mechanism, not an EHR-genomic study. Included here because it names a
  specific druggable node (Notch-1) downstream of the TET2-mutant CHIP
  clone, which sharpens the target-trial thinking in item #1.

### 6. Carrasco-Zanini et al. — Proteomics for genome-negative rare disease
- **Venue**: Science Translational Medicine, 2026 (aeb1331).
- **Thread**: Rare disease + multi-omics-augmented PRS lineage.
- **What's new**: In 424 patients with rare diseases undiagnosed after
  genome sequencing, proteomic profiling identified disease-associated
  variants and candidate gene-disease links. First systematic proteomic
  diagnostic-yield estimate on a genome-negative rare-disease cohort.
- **Why it matters here**: Directly supports the pre-symptomatic
  phenoconversion / proteomic-trajectory sub-thread (Ran/Benatar ALS
  template). The framing "proteins as functional evidence for VUS
  resolution" also cross-connects to your ACMG/ClinGen variant-
  interpretation thread.
- **Action**: Note whether the assay platform is UKB-Olink-comparable
  (it very likely is); if so, the same variant → protein evidence loop
  is reproducible in AoU/UKB.

### 7. Gonzalez et al. — Economic evaluation of functional genomic testing in undiagnosed rare disease
- **Venue**: Genetics in Medicine, 2026 (S109836002601035X).
- **Thread**: Rare disease diagnostics (health-economics layer).
- **What's new**: Estimates 100-500 undiagnosed Australians per year
  would benefit from proteomics testing after uninformative
  exome/genome. Puts a per-QALY price on the workflow in item #6.
- **Why it matters here**: If you cite Carrasco-Zanini for the
  diagnostic yield, cite Gonzalez for the cost-effectiveness case
  needed to argue for reimbursement or biobank inclusion.

### 8. Hendry, Zhou, Jiang — FDA plausible-mechanism guidance across rare disease
- **Venue**: Nature Genetics, 2026 (41588-026-02750-4).
- **Thread**: Rare disease + variant interpretation.
- **What's new**: Commentary arguing the FDA's plausible-mechanism
  guidance is broadly applicable across rare disease if functional
  criteria are met, while defending that the rare/ultra-rare split
  still carries regulatory meaning.
- **Why it matters here**: Regulatory framing feeds directly into ACMG-
  AMP PS3/BS3 functional-evidence weighting; this is the FDA-side
  companion to the ClinGen-side rules you already track.

### 9. Hwang et al. — Effective strategies from the Undiagnosed Diseases Network
- **Venue**: Genetics in Medicine, 2026 (S1098360026010361).
- **Thread**: Rare disease diagnosis (workflow methodology).
- **What's new**: Structured audit of what actually gets UDN cases to a
  diagnosis — the operational counterpart to the reanalysis-at-scale
  papers (Uria-Regojo et al. 2026 medRxiv) already in the thread.
- **Why it matters here**: Bridges single-center reanalysis workflows
  and biobank-scale rare-disease reanalysis; the UDN's diagnostic
  strategies are the ground truth against which biobank-scale HPO-
  driven diagnostic benchmarks (GraphRareBench, PhenoSV, Exomiser,
  PhenoGPT2) should be validated.

### 10. Straub et al. — Our Future Health phenomic profiles (n = 1.9 M)
- **Venue**: Nature Medicine, 2026 (41591-026-04602-4).
- **Thread**: Biobanks with EHR linkage.
- **What's new**: First phenomic-profile paper from Our Future Health,
  a UK cohort at 1.9 M participants with linked phenotypic and genomic
  data. Explicitly frames itself as fit for rare-disease phenotyping,
  risk stratification, multimodal analyses, and recruitment.
- **Why it matters here**: UKB, AoU, MVP, BioVU now have a
  fourth-scale UK sibling worth adding to the tracked-cohorts list.
  Especially interesting for PRS-portability replication (UK-based but
  designed for recruitment, so trial-adjacent) and for rare-disease
  phenoconversion studies.
- **Action**: Add OFH to the biobanks list in INTERESTS.md.

### 11. Long et al. — HLA-B8 × DQ2.5 linkage for celiac in AoU (Hispanic and Black)
- **Venue**: Journal of Human Immunity, 2026 (rupress.org, 2/6/e20260050).
- **Thread**: Biobanks with EHR linkage (AoU); ancestry-aware fine-
  mapping.
- **What's new**: 3,481 celiac cases from All of Us, of which 2,899
  carry established risk alleles; refines HLA-B8 / HLA-DQ2.5 linkage
  contribution in Hispanic and Black participants specifically.
- **Why it matters here**: Direct example of AoU-based ancestry-aware
  fine-mapping of a well-known HLA locus — same design pattern as your
  All of Us replication work. Cite as an exemplar of "AoU as an
  ancestry-diverse replication substrate."

### 12. Wang et al. — MHT × CV risk in midlife women with vasomotor symptoms (TTE)
- **Venue**: JAMA Internal Medicine, 2026 (2853611).
- **Thread**: Causal inference / pharmacoepi — HRT sub-thread.
- **What's new**: Target-trial-emulated estimate of MHT's CV effect in
  perimenopausal women with vasomotor symptoms — the population most
  MHT-CV trials excluded. Cites Hernán TTE framework.
- **Why it matters here**: HRT persistence and CV outcomes are an
  explicit active drug-class thread; this study fills the perimenopausal
  gap that WHI-derived evidence has always struggled with.
- **Action**: Read the estimand section carefully — perimenopausal
  treatment initiation raises non-trivial immortal-time-bias and
  eligibility-alignment issues (see Kobayashi et al. below on the same
  motif in a different setting).

### 13. Blostein et al. — Sex differences in genetic architecture of EHR quantitative traits
- **Venue**: medRxiv, 2026 (2026.09.02.26362069).
- **Thread**: EHR phenotyping / OMOP + genetic epidemiology.
- **What's new**: Sex-stratified GWAS on 508 EHR-derived quantitative
  clinical traits (labs, vitals). Population-scale evidence that
  quantitative-trait genetic architecture differs by sex at levels
  clinically actionable summary statistics haven't yet accounted for.
- **Why it matters here**: Direct evidence that PheWAS/PheRS calibration
  and PRS transferability need to be re-audited under sex
  stratification. Portable to any BioVU/AoU PheWAS you'd run on lab
  traits.
- **Action**: If any of the 508 traits overlap with a PheWAS you have
  running, pull the sex-stratified summary stats for benchmarking.

### 14. Nam et al. — Novel T1D polygenic scores in diverse populations
- **Venue**: medRxiv, 2026 (2026.09.04.26361335).
- **Thread**: Genetic epidemiology — cross-ancestry PRS portability.
- **What's new**: Non-EUR-derived T1D polygenic scores evaluated across
  diverse populations. Prior EUR-only T1D PS have poor non-EUR
  performance; this work advances the "portable T1D PS" case.
- **Why it matters here**: Directly serves the cross-ancestry PGS
  portability sub-thread and the AoU-based composite-risk framing.
  T1D is a plausible next target for the tails-and-residuals PGS
  taxonomy (Baya, Souaiaia, Vazquez lineage).

### 15. Beck et al. — PTSD EWAS in the Million Veteran Program
- **Venue**: medRxiv, 2026 (2026.09.04.26362177).
- **Thread**: Biobanks (MVP) + epigenetics (adjacent to genetic
  epidemiology thread).
- **What's new**: MVP-scale DNA-methylation EWAS on PTSD. First
  large-scale MVP epigenetics readout on a psych phenotype.
- **Why it matters here**: The MVP infrastructure — not the PTSD result
  per se — is the signal. This is the "MVP can now do EWAS on psych
  phenotypes at scale" milestone; portable to hormonal-therapy
  persistence, GLP-1 RA persistence, and other MVP-based causal
  questions in the pharmacoepi thread.

### 16. Kreslova et al. — ETI response in L467F;F508del complex CFTR allele
- **Venue**: Frontiers in Medicine, 2026 (fmed.2026.1930172).
- **Thread**: Cystic fibrosis / CFTR modulator eligibility.
- **What's new**: Case report + review on clinical benefit from
  elexacaftor/tezacaftor/ivacaftor without sweat-chloride response, in
  the L467F;F508del complex allele. Sweat-chloride-vs-clinical-benefit
  decoupling is the exact eligibility-decision motif your CF thread
  cares about.
- **Why it matters here**: Direct evidence that eligibility rules keyed
  to sweat-chloride response would miss real responders — germane to
  modulator-eligibility policy work.
- **Caveat**: n=1 case + narrative review. Cite for framing, not for
  effect estimates.

### 17. Snel & Schulz — Attributing Cohen's d in UKB normative age biomarkers
- **Venue**: arXiv 2609.07729v1 (2026-09-07 submission).
- **Source**: Local digest 2026-09-09.
- **Thread**: Genetic epidemiology (biomarker-as-exposure adjacent) +
  ML for precision health.
- **What's new**: Closed-form influence functional attributes a
  disease-related effect size (Cohen's d) to individual training
  samples in normative age-prediction models on UK Biobank. Removing
  the top-10% most influential samples raises held-out case-control
  effect sizes across four diseases and two biomarker modalities.
  Recovers HbA1c as the marker driving T2D age-gap improvement.
- **Why it matters here**: Directly relevant to any UKB or AoU
  normative-age model you'd audit — this is the "which subjects are
  actually driving my biomarker effect" tool. Portable to PheRS
  calibration audits and PRS-tails framing (Baya-style perpendicular to
  Souaiaia).
- **Action**: `pyinfluence` is released; worth wiring into the PheRS
  calibration audit tooling.

### 18. Devarakonda — scDEFT: single-cell drug-effect transducer (IBD)
- **Venue**: arXiv 2609.10831v1 (2026-09-09 submission).
- **Source**: Local digest 2026-09-11.
- **Thread**: Specific diseases (IBD) + patient stratification (ML for
  precision health).
- **What's new**: Trains a drug-conditioning transducer on a harmonized
  IBD single-cell atlas (1.16 M cells, 3 cohorts, 2 drug classes).
  Predicts drug-induced state change at 45% of a reproducibility ceiling
  and stratifies responders pre-treatment at AUROC 0.70, where standard
  predictors are at chance. Also nominates targets via back-mapping
  latent dimensions to genes.
- **Why it matters here**: IBD is on the tracked-disease list, and the
  pre-treatment responder-stratification claim is the exact clinical
  decision your ML-for-precision-health rubric grades as HIGH. The
  target-nomination back-mapping also connects to the drug-repurposing
  thread's explainability requirement.
- **Caveat**: 0.70 AUROC for responder pre-stratification is a
  plausible-but-not-huge lift over standard predictors. Watch for
  external validation before treating as translation-ready.

---

## METHODS-WATCH — portable methods, off-thread diseases

Detailed only enough to spot the reusable idea:

- **Zhang et al. — INFORM TTE for hip PJI revision (Archives of
  Orthopaedic and Trauma Surgery, 2026)**: Textbook TARGET-reported TTE
  using EHR data from three Chinese tertiary hospitals. Reusable
  template for a target-trial write-up that isn't UK/US, if you ever
  need to cite non-Western EHR-TTE precedent.
- **Kobayashi et al. — Immortal time bias in prophylactic ASM after
  ICH (Neurocritical Care, 2026)**: Letter walking through the
  immortal-time-bias critique of a specific ASM study; reusable as a
  reviewer template.
- **Adamstein & Ridker — Exposure-caused selection bias in secondary vs
  primary prevention (European Heart Journal, 2026)**: Editorial
  reframing why risk factors attenuate in secondary prevention as a
  selection-bias problem. Directly citable as motivation for TTE in the
  secondary-prevention setting.
- **Hanada & Kojima — InMASS (Biometrical Journal, 2026)**: Estimator
  for target-population ATE using only aggregate meta-analysis evidence.
  METHODS-WATCH: portable to combining published trial estimates with
  your own EHR-derived cohort estimate.
- **Lee et al. — Kalman smoothing on HT prevalence estimators
  (arXiv 2609.09325v1, digest 2026-09-10)**: Not on-thread, but the
  "IPW estimate as a noisy state-space observation" formulation is a
  clean pattern reusable for any noisy weighted estimator in
  time-varying settings.
- **Hendrix et al. — Geospatial foundation models for social risk
  (arXiv 2609.11689v1, digest 2026-09-11)**: Foundation-model output as
  a residual-variance predictor on top of ADI/SDI. METHODS-WATCH for
  EHR-adjacent SDoH modeling.
- **Semchin et al. — Connectome-constrained Parkinson progression
  subtypes (arXiv 2609.10890v1, digest 2026-09-11)**: Sub-thread hit is
  "motor subtypes" keyword, but the disease-time + subtype joint
  estimation is a reusable trajectory-clustering pattern for your
  multimorbidity thread. Not high enough on its own.
- **Orešković et al. — Metabolomic biomarker discovery in admixed
  Americans (medRxiv, 2026)**: Method for boosting metabolome-wide
  discovery power in non-European ancestries. Portable to your
  multi-omics-augmented PRS sub-thread if any AoU metabolomics work
  needs cross-ancestry framing.
- **Nourbakhsh et al. — MedProb: probing VLMs for medical QA
  (arXiv 2609.04336)**: Peter Szolovits alert. Off-thread but methods-
  worthy for probing internal representations of biomedical VLMs.
- **Ma et al. — Long-read RNA-seq for splicing outliers in rare-disease
  trios (medRxiv, 2026)**: Stephen Montgomery alert. Off-thread for
  splicing evidence in ACMG/AMP variant curation is a plausible re-use
  path (PS3/BS3 evidence sourcing) — file under variant-interpretation
  future reference rather than acting now.

---

## SKIP — surfaced but incidental

Listed for completeness; no detailed reports.

- Devarakonda scDEFT counter-hits on other alerts (deduplicated).
- Chiu et al. echo in multiple alerts (same paper).
- FUSE-RT chromatography retention-time prediction (arXiv 2609.07531v1,
  digest 2026-09-09) — foundation model on chromatography; no thread
  overlap.
- Non-biomedical KG papers surfaced under the "knowledge graph" alert.
- General SDoH / geospatial economics papers not tied to an EHR-
  linked cohort.
- Non-EHR AoU papers on unrelated dental topics.

---

## Suggested next actions

1. Read the CH-Predict primary paper (Batchi-Bouyou et al., *Blood
   Advances* 2026) that the Gillis & West editorial covers, and decide
   whether to port its feature set to BioVU/AoU.
2. Add **Our Future Health** to the tracked-biobanks paragraph in
   `INTERESTS.md`; also decide whether to add it to `config/tracked.yaml`
   as a keyword.
3. Confirm the version of your own Zeng-Waxse-Denny 2026 paper indexed
   at *npj Digital Public Health* matches what you want cited; the
   1-citation alert is the first downstream user.
4. Wire `pyinfluence` (Snel & Schulz) into a PheRS-calibration audit as
   a proof-of-concept — the influence-attribution logic is directly
   portable.
5. Watch for the full Jäger et al. *Atherosclerosis* 2026 paper (only
   conference abstract available now); it's the within-cohort CAD+/CAD-
   CHIP-mortality contrast the CV-trial-design piece needs.
