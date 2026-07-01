# Research digest report — 2026-07-01

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-01** (rolling ~10-day catch-up covering
the digest gap since the last report on 2026-06-20).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-01 | Digests read: 06-23, 06-25, 06-26, 06-30. Days 06-21/22/24/27/28/29 produced only a header (0 relevant papers — genuine dry days per the pipeline). 06-30 was the largest with 4 papers. |
| Google Scholar author alerts | 2026-07-01 06:15Z batch | ~30 alerts across the standing author feeds (Bastarache, Denny, Hripcsak, Hernán, Karczewski, Patrick Ryan, Chute, Szolovits, Kastner, Yang, Pritchard, Montgomery, Zitnik, Shendure, Vogelstein, Natarajan, Celi, Luo, Brandt, Collins). |
| NCBI PubMed "What's new" alerts | 2026-07-01 12:32Z | Three saved searches fired: `UK Biobank` (15 hits), `drug repurposing` (8 hits), `All of Us` (4 hits). |
| alphaXiv weekly digest | 2026-06-24 | Product announcement (autoresearch feature); not paper content — noted for interest, not triaged. |

Caveat: Scholar / PubMed alert bodies contain title + venue + a snippet
only. The reports below are triaged against those snippets plus, where
available, the arxiv-digest full abstract. Nothing here reflects
full-text reading — flag the HIGH items for the reading queue.

---

## Executive summary

**HIGH (5 items — direct match to an active thread; read first)**

1. **Padovani-Claudio, Lewis, Bastarache, He — "Determination and GWAS validation of optimal minimal phecode count for eye disease cohort generation"** *(IOVS 2026)*. Direct methods paper on phecode-count cutoffs from the Bastarache group — core PheWAS / phecode-infrastructure thread.
2. **Aboobakar, Dutton, Pasquale, Kang et al. — "Social vulnerability modifies the relationship between polygenic risk and primary open-angle glaucoma in the All of Us Research Program"** *(IOVS 2026)*. PRS × social-vulnerability interaction in AoU — hits the biobank/PRS + EHR-linked cohort + precision-health threads simultaneously.
3. **Lee & Whitman — "Genome-Wide and Rare Variant Association Studies of Admixed American and African Ancestry Individuals with Amblyopia in the All of Us Research Program"** *(IOVS 2026)*. Ancestry-stratified GWAS + rare-variant analysis in AoU — hits genetic epi + cross-ancestry + biobank threads.
4. **Cai, Toy, Martin, Fan, Westlund, Tran et al. (Patrick Ryan feed) — "Semaglutide and Neovascular Age-Related Macular Degeneration: An OHDSI Network Study"** *(IOVS 2026)*. OHDSI/OMOP network study of a GLP-1 RA safety signal — exact overlap with the causal-inference + pharmacoepi + GLP-1 drug thread and the EHR phenotyping/OMOP thread.
5. **Yang, Xu, Hou, Zhou, Saykin, Cheng — "Deep contrastive learning framework identifies cell-type-specific drug targets in Alzheimer's disease"** *(Alzheimer's Dement 2026)*. Multi-omics + contrastive learning for AD drug repurposing with a mechanistic (cell-type) rationale — matches the "explainable / mechanism-rooted" preference in the drug-repurposing thread.

**METHODS-WATCH (5 items — off-thread topic but methods worth cribbing)**

- **Murali, Barnatchez, Hoppe, Wagner, Keller, Josey — "Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach"** *(arXiv 2606.23656; stat.ME)*. Doubly-robust calibration weighting for misclassified categorical exposures, worked out on a 651-patient CF cohort (throat-swab vs sputum P. aeruginosa). Hits both the causal-inference methods thread and the CF disease thread — arguably HIGH depending on how live your CF-modulator work is.
- **Schulz & Ritter — "Measurement noise limits the advantage of nonlinear models over linear models in biomedical prediction"** *(arXiv 2606.18420; cs.LG)*. UK Biobank benchmark (140 tasks) with an exact excess-risk identity showing why flexible models tie linear ones under typical biomedical measurement reliability. Directly relevant to the ML-for-precision-health thread's calibration/utility framing.
- **Dyck & Sauzet — "Applying the Weibull Shape Parameter test for signal detection in pharmacovigilance using the R package WSPsignal"** *(arXiv 2606.18809; stat.ME)*. Time-to-event hazard-shape signal detection for EHR-based pharmacovigilance — worth a note in the causal-inference / pharmacoepi toolbox.
- **Grant, Patel, Burgess — "Multivariable Mendelian randomization with weak instruments: a comparison of Bayesian and frequentist methods"** *(arXiv 2606.26638)*. MVMR under weak-instrument regimes; directly relevant if you have phenome-wide MR / biomarker-as-exposure scans running.
- **Hejblum et al. — "Probabilistic record linkage of de-identified research datasets with discrepancies using diagnosis codes"** *(Sci Data 2026, via Szolovits feed)*. Diagnosis-code-based deterministic-with-uncertainty linkage — reusable if you're joining AoU / MVP / registry cohorts against local EHR tables.

**Notable but SKIP (4 items — surface as awareness, don't queue)**

- **Karpinsky, Mozziconacci, Delcey — "DNA Language Models: An Assessment of Pre-Training for Fine-Tuning Tasks"** *(arXiv 2606.30140; q-bio.GN)*. DNABERT2-vs-ConvNova pretraining ablation. Foundation-model thread is about *EHR* FMs, not DNA LMs — awareness only.
- **Böhringer & Holzmann — "Evaluating HWE and Association in GWAS: A Unified Procedure"** *(arXiv 2606.30311; stat.ME)*. Conditional χ² procedure folding HWE testing into association. Genetic-epi-adjacent but a niche statistical improvement rather than an active-thread hit.
- **Perciballi et al. — "Are Tabular Foundation Models Robust to Realistic Query Distribution Shifts in Microbiome Data?"** *(arXiv 2606.24995; cs.LG)*. TFM robustness on microbiome — off-thread.
- **Cavinato, Hofmeister, Kutalik — "Evaluating anonymized genome re-identification using polygenic predictions and its implications for data privacy"** *(bioRxiv 2026)*. PGS-based re-identification attack. Interesting for biobank-governance conversations but no direct methods-borrow.

**DIGEST-INFRASTRUCTURE NOTE.** The digest fired every day 06-21 → 07-01
except that 06-21 / 06-22 / 06-27 / 06-28 / 06-29 produced 0 relevant
papers. Given the previous 06-20 fetch-failure incident, these "0-hit"
days are *plausible* on a Saturday-Sunday-plus-holiday cadence, but the
run of five zero-hit days over a 10-day window is unusual. **Recommend a
quick spot-check of the Actions log** for those dates — if all four
categories reported successful fetches but zero score-≥1 papers, the
digest is fine and arXiv was just quiet; if any category shows a 429 or
timeout it's a repeat of the 06-20 rate-limit failure and the polling
delays need another bump.

---

## HIGH — detailed reports

### 1. Padovani-Claudio, Lewis, Bastarache, He — Determination and GWAS validation of optimal minimal phecode count for eye disease cohort generation *(IOVS 2026)*

**Threads hit:** PheWAS / phecode infrastructure (primary); EHR
phenotyping; genetic epi (GWAS validation loop).

**Why it matters.** This is an infrastructure paper from the group that
maintains the phecode system, doing exactly the calibration work called
out in your INTERESTS.md phecode section: *how many phecode occurrences
do you need for a cohort to be well-defined?* GWAS validation of the
cutoff (i.e., does a known genetic association hold at the resulting
case-set) turns a phenotype-definition choice into a testable empirical
question rather than a rules-of-thumb one. Applied to eye disease, but
the methodology transports directly to any other disease you're
phecoding out of BioVU / AoU / MVP.

**What to look for on read.**
- The functional form of "optimal N" — does it recommend a single
  disease-agnostic minimum (e.g., N ≥ 2) or a per-disease optimum
  tuned by prevalence and GWAS power?
- How the GWAS-validation step is specified: replicated hit rate?
  Effect-size concordance with an external GWAS? χ² inflation?
- Whether the paper considers ancestry-stratified case counts (relevant
  to your ancestry-aware-risk-scores angle) or only pooled cohorts.
- Whether they compare against ICD-10-based cohorts as a baseline.

**Downstream use.** If they land on N ≥ 2 as the general recommendation,
this is a citable justification for the "at least twice" phecode
threshold that shows up throughout PheWAS pipelines but is usually
justified with a hand-wave.

**Source.** Google Scholar alert (Lisa Bastarache author feed),
2026-07-01. IOVS 2026, arvojournals.org article 2815661.

---

### 2. Aboobakar, Dutton, Pasquale, Kang et al. — Social vulnerability modifies the relationship between polygenic risk and primary open-angle glaucoma in the All of Us Research Program *(IOVS 2026)*

**Threads hit:** Biobanks with EHR linkage (AoU) + Genetic epi (PRS) +
ML for precision health (heterogeneous risk / who to screen).

**Why it matters.** A PRS × environment interaction study in AoU is
squarely in the biobank + PRS + EHR-linked-cohort intersection you've
flagged. Social-vulnerability-index modification of PRS effects is
exactly the type of *calibration-across-strata* question your
INTERESTS.md calls out for PRS work. Also relevant to the ancestry
angle if the SVI stratification happens to align with the AoU ancestry
composition.

**What to look for on read.**
- Interaction specification: multiplicative on log-OR, or explicit
  ancestry- and SVI-stratified PRS distributions?
- Whether the PRS is re-weighted per ancestry (PRS-CSx, PRS-CS-auto)
  or a single European-training PRS applied across the AoU
  multi-ancestry cohort — the latter would be a limitation worth
  flagging.
- Whether they report an absolute-risk translation (decile risk × SVI
  quartile table) or only relative-risk interactions.

**Downstream use.** Direct precedent if you're building a
composite-risk model that stacks PRS with social determinants in AoU.

**Source.** Google Scholar alert (Joshua C. Denny related research
feed), 2026-07-01. IOVS 2026, arvojournals article 2813500.

---

### 3. Lee & Whitman — Genome-Wide and Rare Variant Association Studies of Admixed American and African Ancestry Individuals with Amblyopia in the All of Us Research Program *(IOVS 2026)*

**Threads hit:** Genetic epi (cross-ancestry GWAS, rare-variant burden)
+ Biobanks with EHR linkage + Rare disease (rare-variant methods).

**Why it matters.** Cross-ancestry rare-variant work in AoU is scarce
outside the AoU flagship papers themselves; this puts the AoU
short-read WGS to use on non-European ancestry cohorts, which is the
tail your INTERESTS.md flags as "portability" work. Even if amblyopia
isn't a tracked disease, the AoU-specific rare-variant methods choices
(collapsing thresholds, ancestry-PC handling, sample-size-vs-power
trade-offs at ~50k WGS) generalize to any AoU-based rare-variant
follow-up you'd do on a tracked outcome.

**What to look for on read.**
- Which collapsing method (SKAT / SKAT-O / burden / STAAR) they use
  and whether they pool or meta-analyze across ancestries.
- How they define ancestry (genetic PCs, self-report, admixture
  fractions) — the "Admixed American" label suggests a
  genetic-ancestry definition rather than the AoU-CDR default.
- Whether they release effect estimates that could be meta-analyzed
  with UKB / MVP rare-variant results.

**Downstream use.** Reference template for AoU rare-variant burden
pipelines on tracked outcomes.

**Source.** Google Scholar alert (Joshua C. Denny related research
feed), 2026-07-01. IOVS 2026, arvojournals article 2815766.

---

### 4. Cai, Toy, Martin, Fan, Westlund, Tran et al. (Patrick Ryan feed) — Semaglutide and Neovascular Age-Related Macular Degeneration: An OHDSI Network Study *(IOVS 2026, dual alert)*

**Threads hit:** Causal inference & pharmacoepi (GLP-1 drug thread,
target trial emulation-adjacent) + EHR phenotyping & OMOP + ML for
precision health (drug safety signal).

**Why it matters.** This is the *exact* intersection of three of your
threads — a GLP-1 RA outcomes study, done in OMOP-CDM, run as an OHDSI
network study across sites. Semaglutide × neovascular AMD is one of a
handful of safety signals under active discussion for GLP-1s, and
network-scale evidence is the cleanest form of it. Also worth reading
purely for the OHDSI network-study *methods* template — the
propensity-score / negative-control-outcome / empirical-calibration
pipeline is what your INTERESTS.md points at for the GLP-1 thread.

**What to look for on read.**
- Sites included in the network (which CDMs?) and how many patients
  per site — network heterogeneity matters more than headline HR.
- Comparator: new-user active-comparator design (vs DPP-4 / SGLT2 /
  metformin?) or new-user vs non-user? The latter is much weaker.
- Whether they report empirical calibration with a negative-control-
  outcome distribution, per OHDSI convention.
- Absolute-risk / NNH translation — headline HRs on a rare outcome
  can inflate perceived risk without an absolute-scale anchor.

**Downstream use.** Template for GLP-1 × [tracked outcome] OHDSI-style
analyses; ammunition for the GLP-1 safety-signal discussion.

**Source.** Google Scholar alerts (Patrick Ryan author feed AND George
Hripcsak author feed, both 2026-07-01) — dual alert confirms it's a
network-study collaboration piece.

---

### 5. Yang, Xu, Hou, Zhou, Saykin, Cheng — Deep contrastive learning framework identifies cell-type-specific drug targets in Alzheimer's disease *(Alzheimers Dement Amst 2026)*

**Threads hit:** Drug repurposing (primary — explainable + mechanistic
angle) + ML for precision health.

**Why it matters.** Your INTERESTS.md drug-repurposing thread
explicitly prefers *explainable* pipelines that emit path or subgraph
rationales, and de-prioritizes chemistry-only pipelines with no
clinical-evidence loop. Cell-type-specific target identification via
contrastive learning is the mechanistic-rationale variant of that
setup: instead of a black-box drug-disease link, the output is
"repurposing candidate X because it modulates target Y in cell type Z
that is dysregulated in AD." That's a stronger claim than a raw
link-prediction score.

**What to look for on read.**
- The contrastive objective: what's the positive/negative pair
  definition, and does it use single-cell perturb-seq / LINCS L1000
  as ground-truth?
- Whether they surface the cell-type × target pair for each candidate
  drug (i.e., is the "explainability" real or a post-hoc rationale?).
- Any EHR / real-world-prescribing validation loop — even
  small-cohort — or is it purely computational?
- Whether AD-specific candidates recover known modulators
  (donepezil / lecanemab / anti-inflammatories) as a sanity check.

**Downstream use.** Reference architecture if you push on the
cell-type-aware angle of the repurposing thread, especially for other
tracked diseases where single-cell atlases exist (CF airway
epithelium, IBD gut mucosa, APOL1 podocytes).

**Source.** NCBI PubMed "drug repurposing" saved-search alert,
2026-07-01. PMID 42382038. Free PMC article.

---

## METHODS-WATCH — condensed

### Murali et al. — Causal Inference with Multiple Misclassified Exposures *(arXiv 2606.23656)*

Doubly-robust calibration + control-variate estimator for causal effect
estimation when exposures are measured with error. Applied to a CF
cohort (n=651, ages 6-21) using throat swabs (imperfect) vs sputum (gold
standard) for P. aeruginosa and S. aureus. Swab-based estimates
attenuated the P. aeruginosa → FEV1 effect by ~69% relative to
sputum-based estimates (−2.67 vs −8.52 percentage points; 95% CI for
sputum: −13.40, −3.63). Two takeaways: (a) the estimator is a
plug-and-play upgrade wherever you have gold-standard vs error-prone
exposure measurements on subcohorts; (b) the CF-specific result is a
real clinical warning — swab-based reasoning may substantially
under-treat.

**Why not HIGH:** Cystic-fibrosis-thread relevance depends on whether
your active work touches microbiology-driven outcomes. If yes, promote
to HIGH.

**Source.** `arxiv-digest` 2026-06-23 (score 2: `causal inference`,
`cystic fibrosis`).

### Schulz & Ritter — Measurement noise limits the advantage of nonlinear models over linear models *(arXiv 2606.18420)*

Exact excess-risk identity showing degree-k interactions get attenuated
by feature reliability^k while linear signal is attenuated once —
across 140 UKB tasks the linear-vs-flexible gap has the predicted noise
signature. Useful ammunition when someone claims "gradient boosting
wins on tabular" without checking measurement reliability.

**Why not HIGH:** Not directly clinical-decision-facing, but a strong
reference for calibration/decision-curve write-ups.

**Source.** `arxiv-digest` 2026-06-18 (score 2: `uk biobank`,
`biobank`).

### Dyck & Sauzet — WSPsignal for pharmacovigilance signal detection *(arXiv 2606.18809)*

R package for Weibull-hazard signal detection over post-marketing EHR
time-to-event data. Frequentist for large samples (~20k obs), Bayesian
for small (~1k). Cite if you need a hazard-shape-based signal detector
in the pharmacoepi toolbox alongside disproportionality methods.

**Source.** `arxiv-digest` 2026-06-18 (score 1: `electronic health
records`).

### Grant, Patel, Burgess — MVMR with weak instruments *(arXiv 2606.26638)*

Bayesian vs frequentist multivariable Mendelian randomization
comparison for the weak-instrument regime. Directly relevant if any
active phenome-wide MR / biomarker-as-exposure scan is on your desk.

**Source.** Google Scholar alert (Joshua C. Denny related research
feed), 2026-07-01.

### Hejblum et al. — Probabilistic record linkage with discrepancies using diagnosis codes *(Scientific Data 2026)*

Approach for linking de-identified research datasets using ICD codes
as the discriminator. Reusable for joining external cohorts against
local EHR without a shared identifier.

**Source.** Google Scholar alert (Peter Szolovits author feed),
2026-07-01. www.nature.com/scientificdata.

---

## SKIP — quick notes (surface, don't queue)

- **DNA LMs pretraining ablation (arXiv 2606.30140).** Off-thread —
  your foundation-model interest is EHR FMs, not DNA LMs.
- **HWE-conditioned GWAS χ² test (arXiv 2606.30311).** Statistically
  clean but a niche procedural improvement.
- **Tabular FM microbiome robustness (arXiv 2606.24995).** Off-thread.
- **Genome re-identification via PRS (bioRxiv 2026 via Denny feed).**
  Awareness-only for biobank-governance conversations.
- **Insurance pricing with LLM embeddings (arXiv 2606.29371).**
  Score-1 false-positive on `motor` (motor third-party liability).
- **DART microfluidic chip paradigm (arXiv 2606.18523).** Score-1
  false-positive on `chip` (microfluidic, not CHIP hematology).
- **openhdemg spinal motor neurons (arXiv 2606.23066).** Score-1
  false-positive on `motor`.
- **bioETH-Beacon (arXiv 2606.20315).** Confidential genomic beacon
  over homomorphic Ethereum; interesting privacy engineering, off-thread.
- **MedRLM recursive multimodal EHR agent (arXiv 2606.20164).**
  Framework-paper without empirical grounding — parked.
- **KG-TRACE neuro-symbolic AMR prediction (arXiv 2606.26179).**
  KG-grounded neural pipeline but for AMR / M. tuberculosis; drift from
  the biomedical-KG-for-clinical-reasoning thread's focus.
- **Multimodal alignment for histopath molecular prediction (arXiv
  2606.29949).** Adjacent (foundation-model alignment) but off-thread.
- **Federated tensor decomposition of single-cell immune data (arXiv
  2606.24938).** Interesting privacy-preserving stats; off the
  EHR-focused threads.

---

## PubMed subject-alert triage (2026-07-01)

**`UK Biobank` (15 hits).** Overwhelmingly downstream clinical-question
uses of UKB (obesity-paradox, plasma metabolites × epilepsy,
alcohol-BMD MR, smoking × CKD interaction, artificial-sweeteners × CKD,
etc.). None methodologically noteworthy at the abstract level. One item
worth a quick scan: **"Association of Smoking, Smoking Cessation, and
Genetic Susceptibility With Chronic Kidney Disease Risk"** (Kidney Med
2026, PMID 42375691) — gene × environment interaction on CKD; overlaps
loosely with the APOL1 kidney-disease-risk thread. Not enough to
promote to HIGH.

**`All of Us` (4 hits).** Two of interest:
- **"Characterizing endometriosis and adenomyosis symptom clusters and
  their impact on quality of life in the All of Us Research Program"**
  (Hum Reprod 2026, PMID 42381368). Symptom clustering in AoU — hits
  the chronic-disease-clustering / multimorbidity thread. Would be a
  quick read to see whether they use latent-class methods you'd import.
- **"Hypertension among Middle Eastern and North African adults... All
  of Us"** (Front Med 2026, PMID 42383063). AoU representation /
  equity work; awareness only.

**`drug repurposing` (8 hits).** One direct match to the
drug-repurposing thread: the AD deep-contrastive paper (**#5 above**,
PMID 42382038). Also of interest but background-level: *"Semaglutide
alleviates osteoarthritis independent of weight loss via GLP-1R-
mediated activation of autophagy through AKT/mTOR inhibition"*
(J Orthop Translat 2026, PMID 42381999) — mechanistic follow-up on the
same GLP-1 repurposing signal the OHDSI Semaglutide × AMD paper (#4)
tests epidemiologically. Reading both back-to-back gives a nice
mechanism → RWE loop.

---

## Housekeeping / open items

- **Verify the 06-20 → 07-01 zero-hit run** via the Actions log
  (`daily-arxiv-digest.yml` runs on 06-21, 06-22, 06-27, 06-28, 06-29
  all produced only a 138-byte header file). If any category shows a
  429, the polling delay needs another bump; if all categories fetched
  cleanly and simply had no keyword hits, this is a genuine quiet
  stretch and no action needed.
- **Consider adding an "OHDSI network study" phrase to
  `config/tracked.yaml`** — the semaglutide-AMD paper (#4) is exactly
  the type of study you care about, and network-study terminology is
  distinctive enough to be a high-precision keyword.
- **Bastarache phecode-count paper (#1)** is a candidate for
  citation-tracking — worth adding to the standing Scholar alert list
  if you rely on that phecode-threshold justification anywhere.
