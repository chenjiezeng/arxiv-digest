# Research digest report — 2026-07-16

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-15 → 2026-07-16** (since the prior 2026-06-20 report;
report cadence lapsed during interval — this catches only the two most
recent Gmail batches plus today's arxiv digest).

## Sources scanned

| Source | Volume in window | Notes |
| --- | --- | --- |
| NCBI PubMed "What's new" saved-search alerts (07-16 12:15Z) | 36 hits across 3 saved searches | `UK Biobank` = 24, `drug repurposing` = 12 (mostly medicinal-chem, low on-thread), `All of Us` = 2 (both on-thread). |
| NCBI PubMed "What's new" saved-search alerts (07-15 12:17Z) | 3 subject digests | Same 3 saved searches; volume not re-triaged individually since the 07-16 digest supersedes. |
| Google Scholar keyword alerts (07-16 03:29Z) | 10 keyword feeds | `UK Biobank`, `All of Us research program`, `Foundation models + EHR`, `variant interpretation OR classification`, `clonal hematopoiesis`, `drug repurposing`, `knowledge graph`, `electronic health records`, `rare diseases`, `autoimmune`. |
| Google Scholar author/related-research alerts (07-14 22:27Z) | 4 author feeds | Joshua C. Denny, Jure Leskovec, Christopher G. Chute, Patrick Ryan. |
| `arxiv-digest` repo (`digests/2026-07-16.md`) | 1 paper (1 previously surfaced, suppressed) | Score 1: Guntoro et al., biosecurity probes on Evo 2 embeddings. Off-thread — biosecurity-adjacent, not EHR/genetic-epi. |
| `arxiv-digest` repo (`digests/2026-07-15.md`) | 1 paper | Off-thread (folk-melody bioinformatics; keyword hit was `motor`). |

> Caveat: Scholar / PubMed alert emails contain title, authors, venue,
> and the first ~2-3 lines of each abstract only. The detailed reports
> below contextualize that metadata against your research threads;
> nothing here reflects full-text reading. Where I have marked a claim
> ("uses target-trial emulation", "uses HPO matching"), it is inferred
> from the title + venue + snippet and should be verified against the
> paper before citing.

---

## Executive summary

- **Standout of the window — Nature paper on Bayesian longitudinal EHR
  + genetic discovery.** Urbut, Ding, Nakao, Koyama, Misra, Jiang,
  Harish, Gaffney, Hornsby, Smoller, Gusev, Natarajan, Parmigiani —
  *A Bayesian framework for longitudinal EHR and genetic discovery*
  (*Nature*, 2026 Jul 15, PMID 42457967, doi:10.1038/s41586-026-10780-5).
  Surfaces in **both** the `All of Us` and `UK Biobank` PubMed feeds.
  Direct hit on your PheWAS/phecode + biobank + EHR foundation-model
  threads: a joint longitudinal-EHR + genetic discovery framework from
  the Natarajan / Gusev / Parmigiani axis, published as full-text
  Nature (not npj / commun-brief). **Read first.**
- **Denny author-feed surfaces Wu / Lee / Abiri / Ionita-Laza phenotype
  imputation paper.** *Domain-aware matrix completion for phenotype
  imputation using electronic health record data with applications in
  genomic research* (*The Annals of Applied Statistics*, 2026). Exactly
  the pattern you care about — EHR-derived phenotype completion as a
  substrate for downstream genetic analysis — from Iuliana Ionita-Laza's
  group. **HIGH.**
- **Two independent target-trial-emulation pharmacoepi papers surface
  in the same PubMed batch.** (1) Xu et al. — *Urate-lowering effects
  of losartan: a meta-analysis of RCTs **and target trial emulation***
  (*Hypertens Res*, 2026, PMID 42458015). (2) Xu, Xu, Guo, Her, Li, Lai,
  Zhang, Tan, Zhan — *Long-Term Cardiovascular Risks of Anticholinergic
  Versus Non-Anticholinergic Antidepressants: A **Target Trial Emulation
  With Negative Control Correction*** (*Pharmacoepidemiol Drug Saf*,
  2026, PMID 42449494). Both on your causal-inference / pharmacoepi
  thread; #2 is especially notable for pairing TTE with negative-control
  outcome/exposure correction — a design pattern worth cribbing. **HIGH
  (both).**
- **Variant-interpretation + phenotype-matching paper from the Thévenon
  group.** Ruzicka, Ravel, Audoux, Boulat, Thévenon — *Integration of
  Machine Learning-Based Pathogenicity Prediction and Phenotype Matching
  Improves Variant Prioritization in Rare Clinical Testing* (2026,
  variant-interpretation keyword feed). Directly on the ACMG / rare-
  disease diagnostics thread and specifically on the pattern of stacking
  ML pathogenicity (REVEL / AlphaMissense / etc.) with HPO-based
  phenotype match — worth reading against your active variant-curation
  work. **HIGH.**
- **Multimorbidity trajectory paper using obesity classification.**
  Ampadu-Yeboah, Carr, Ho, Gill, Sattar, Jani — *Classification and
  Severity Assessment of Obesity in Clinical Risk Prediction of
  Multimorbidity Trajectories* (*Clin Obes*, 2026 Aug, PMID 42457618).
  On the chronic-disease-clustering / multimorbidity-trajectory thread;
  UK Biobank cohort. **HIGH.**
- **Patrick-Ryan-feed surfaces a real Lumacaftor/Ivacaftor pediatric
  long-term safety paper.** Zemanick, McColley, Linnemann et al. — *Long-
  term safety and efficacy of Lumacaftor/Ivacaftor in children 12 months
  of age and older with cystic fibrosis: a 96-week open-label study*
  (*ERJ Open*, 2026). Directly on the CFTR-modulator disease thread —
  extends the modulator-in-infants safety literature. **HIGH.**
- **Everything else in the drug-repurposing PubMed feed is medicinal
  chemistry / structural biology / venom neutralization and off-thread**
  (marimastat for snakebite, snake-venom small-molecule adjuncts,
  isoxazol-thiazolidinones for ERα, PI4K/PIPK reviews, S100A9 as
  MASLD/sarcopenia biomarker, hydroquinidine in a rat colon-cancer
  model, artificial-intelligence-in-radiotherapy review). None of these
  hit your explainable-KG / EHR-based / target-trial-emulation
  repurposing angles. **SKIP.** The one exception with a genuine
  clinical-evidence loop is Li, Cheng, Liu, Zhang, Zhang — *Translational
  prioritization of genetically supported candidate targets and
  pharmacological annotations for chronic lung diseases: a single-cell
  eQTL-guided multi-cohort study* (*J Transl Med*, 2026 Jul 15, PMID
  42458479) — MR-guided druggable-genome scan for chronic lung disease
  with pharmacological annotation. **METHODS-WATCH.**
- **arxiv-digest is thin (1 paper on 2026-07-16; 1 off-thread paper on
  2026-07-15).** The single 07-16 surface — Guntoro et al., *Screening
  of Biosecurity Features in Metagenomic Data with Evo 2 Probes* — is a
  genuine hit on the `foundation model` keyword but off your active
  threads (biosecurity screening, not EHR / phenotype / clinical
  application). **SKIP for research relevance**; noted here only because
  it is the one qualifying arxiv output today.

---

## Detailed reports — HIGH priority

### 1. Urbut et al. — Bayesian framework for longitudinal EHR + genetic discovery (Nature, 2026)

- **Citation.** Urbut SM, Ding Y, Nakao T, Koyama S, Misra A, Jiang X,
  Harish A, Gaffney L, Hornsby WE, Smoller JW, Gusev A, Natarajan P,
  Parmigiani G. *A Bayesian framework for longitudinal EHR and genetic
  discovery.* **Nature.** 2026 Jul 15 (online ahead of print).
  doi:10.1038/s41586-026-10780-5. PMID 42457967.
- **Why it lands on your threads.** Simultaneously served by both the
  `All of Us` and `UK Biobank` NCBI What's-New feeds — a strong signal
  that the paper uses (at least one of) the flagship EHR-linked biobanks
  as its evaluation substrate. The author list spans MGH (Natarajan),
  Harvard/HMS (Smoller, Parmigiani), and DFCI (Gusev): the working axis
  behind several of the recent biobank-scale probabilistic-modeling
  papers. The framing — *Bayesian* + *longitudinal EHR* + *genetic
  discovery* in a single sentence — puts it at the exact intersection of
  three of your active threads (biobanks, EHR phenotyping, genetic
  epidemiology).
- **Why it earns Nature real estate.** Longitudinal EHR + genetic
  discovery has historically been solved by (a) reducing time to a
  binary case/control label and running GWAS, or (b) using time-to-event
  survival GWAS. A *Bayesian longitudinal* framework — if it truly
  exploits the trajectory shape rather than collapsing it — would
  address the persistent under-powered problem of common chronic-disease
  progression genetics (e.g., LDL trajectory vs. LDL-at-baseline; HbA1c
  slope vs. peak HbA1c). This is directly relevant to your interest in
  EHR foundation models: a probabilistic longitudinal generative model
  is one of the natural competitors to CLMBR/MOTOR-style transformer
  encoders for genetic-association endpoints.
- **What to look for on full-text read.**
  1. Which biobank(s) did they benchmark on — AoU only, UKB only, or
     both plus a validation cohort like MGB or MVP?
  2. How do they handle the ascertainment structure of the EHR
     time-series (informative visit spacing, missing-not-at-random labs)?
  3. Is the "discovery" claim novel-locus discovery, or improved effect
     estimation at known loci? The latter is the more defensible use
     case for a longitudinal-Bayes framework.
  4. Comparison to Cox / linear-mixed / GWAS on baseline: does the
     Bayesian longitudinal design actually recover loci that survival
     or baseline-quantile designs miss, or is the gain marginal?
  5. Does the method scale to the ~500k UKB / ~250k AoU cohort sizes,
     or does it require subsampling?
- **Triage bucket.** **HIGH — read first.** Almost certainly worth a
  full-text read this week.

---

### 2. Wu, Lee, Abiri, Ionita-Laza — Domain-aware matrix completion for phenotype imputation (Ann Appl Stat, 2026)

- **Citation.** Wu H, Lee CH, Abiri N, Ionita-Laza I. *Domain-aware
  matrix completion for phenotype imputation using electronic health
  record data with applications in genomic research.* **The Annals of
  Applied Statistics.** 2026 (surfaced in the *Joshua C. Denny related-
  research* Scholar feed — i.e., the Scholar recommender flagged it as
  related to Denny's PheWAS / PheRS body of work).
- **Why it lands on your threads.** This is exactly the shape of your
  EHR-phenotyping + genetic-epi work: use matrix completion (a low-
  rank / factor structure over the phecode × patient matrix) to
  *impute* missing phenotypes, then use the imputed matrix as the
  outcome substrate for downstream genetic analysis. "Domain-aware"
  presumably means the completion is regularized by phenotype semantic
  structure (phecode hierarchy? SNOMED IS-A?) rather than being purely
  data-driven — which is the difference between the Wei/Bastarache
  PheRS work and generic collaborative filtering.
- **Where it fits in your existing PheRS / PheWAS reading.** This sits
  alongside Kirchler / Simon-style probabilistic phenotype models and
  the "surrogate outcome" / "silver-standard label" thread from
  KOMAP-lineage phenotyping. The Annals of Applied Statistics venue
  suggests the paper's contribution is on the *statistical* side
  (identifiability, rate of convergence for the completion under an
  EHR-realistic missingness model) rather than a benchmark leaderboard
  — which makes it more valuable for citation as *method* than for
  head-to-head phenotyping accuracy claims.
- **What to look for on full-text read.**
  1. How is "domain awareness" operationalized — phecode-ancestor
     regularizer, ontology-graph Laplacian, or learned from data?
  2. Downstream evaluation: does the paper actually run a GWAS on the
     imputed phenotype and show gain vs. GWAS on the raw / partially
     observed phenotype? Effect on genomic-control λ / genomic
     inflation?
  3. How is *phenotype ascertainment bias* handled — i.e., patients
     with more visits have more observed phecodes, so completion may
     re-weight them relative to sparse-record patients.
  4. Is the code released, and in what language (R vs. Python) —
     matters for adoption.
- **Triage bucket.** **HIGH.** Direct methods overlap with the
  phenotype-imputation angle of your active phecode work.

---

### 3. Xu Y et al. — Long-term cardiovascular risks of anticholinergic antidepressants: TTE with negative-control correction (Pharmacoepidemiol Drug Saf, 2026)

- **Citation.** Xu Y, Xu H, Guo J, Her QL, Li R, Lai Y, Zhang Y,
  Tan ECK, Zhan S. *Long-Term Cardiovascular Risks of Anticholinergic
  Versus Non-Anticholinergic Antidepressants: A Target Trial Emulation
  With Negative Control Correction.* **Pharmacoepidemiol Drug Saf.**
  2026 Jul; 35(7): e70434. doi:10.1002/pds.70434. PMID 42449494.
- **Why it lands on your threads.** Two design elements from your
  causal-inference reading list stacked in one paper: (i) target-trial
  emulation across two active-comparator drug classes (avoiding the
  new-user-vs-non-user immortal-time trap); (ii) negative-control
  correction — either negative-control outcomes (Prasad-Jena / Schuemie
  style) or negative-control exposures (Lipsitch / Tchetgen-Tchetgen
  style) — to bound residual unmeasured confounding. This pairing is
  the current best-practice template for observational drug-safety CV
  outcomes.
- **What to look for on full-text read.**
  1. Which negative-control approach — outcomes, exposures, or both?
     What's the actual set of NC outcomes chosen (usually falls back to
     a Schuemie-style list of ~30 "should be null" endpoints)?
  2. What's the *active comparator* pair — SSRI vs. TCA is the obvious
     one (TCAs being high-anticholinergic, SSRIs low), but the design
     detail matters (e.g., are TCAs vs. SNRIs the contrast?).
  3. Is there an ancestry / demographic subgroup analysis, and does
     the CV-risk gradient hold across age strata (matters for the
     Beers-list justification the paper likely alludes to)?
  4. What's the ratio of the point estimate to the calibrated (post
     NC-correction) estimate? Large shrinkage would suggest genuine
     residual confounding rather than a robust effect.
- **Triage bucket.** **HIGH — read as a design template**, whether or
  not the specific antidepressant question is on your active disease
  threads.

---

### 4. Xu X et al. — Urate-lowering effects of losartan: RCT meta-analysis + target-trial emulation (Hypertens Res, 2026)

- **Citation.** Xu X, Naeem A, Emmett A, Siedlinski M, Chinoy H,
  Guzik TJ, Kontopantelis E, Tomaszewski M. *Urate-lowering effects of
  losartan: a meta-analysis of randomised controlled trials and target
  trial emulation.* **Hypertens Res.** 2026 Jul 15 (online ahead of
  print). doi:10.1038/s41440-026-02719-0. PMID 42458015.
- **Why it lands on your threads.** Sits on the causal-inference /
  pharmacoepi thread with a specific design worth studying: the paper
  runs *both* an RCT meta-analysis *and* a target-trial emulation on
  the same clinical question. Whether or not urate-lowering itself is
  on your disease list, the *paired* RCT-meta + TTE design is the gold
  standard for showing that your observational TTE recovers the RCT
  answer — which is the calibration argument every observational
  methods paper needs.
- **Note on cohort.** Tomaszewski / Kontopantelis are Manchester —
  the emulation is presumably UK Biobank + CPRD, which is directly
  relevant to your biobanks thread.
- **What to look for on full-text read.**
  1. What's the RCT vs. TTE point-estimate agreement — do they land
     within each other's CIs, or is there systematic disagreement in
     magnitude that requires discussion?
  2. What confounders were adjusted for in the emulation that the
     RCT does not require — and how were they measured?
  3. Is the paper's real contribution the *urate* finding (i.e., a
     substantive claim about losartan's urate mechanism) or the
     *methods calibration* (i.e., "here is how you validate a TTE
     against an RCT")? Which one they emphasize will tell you whether
     to cite it in a substantive-claim context or a methods context.
- **Triage bucket.** **HIGH (methods)**.

---

### 5. Ruzicka, Ravel, Audoux, Boulat, Thévenon — ML pathogenicity + phenotype-matching for variant prioritization (2026)

- **Citation.** Ruzicka J, Ravel JM, Audoux J, Boulat A, Thévenon J.
  *Integration of Machine Learning-Based Pathogenicity Prediction and
  Phenotype Matching Improves Variant Prioritization in Rare Clinical
  Testing.* 2026 (surfaced in the `variant interpretation OR variant
  classification` keyword feed; venue not resolvable from the alert
  snippet).
- **Why it lands on your threads.** Directly on the variant-
  interpretation + rare-disease thread. The core design — combining an
  ML pathogenicity score (REVEL / AlphaMissense / PrimateAI-3D lineage)
  with HPO-based phenotype match to re-rank candidate variants for a
  patient — is the exact pipeline pattern used by Exomiser /
  LIRICAL / AMELIE / Phen2Gene, so the interest is in *what* they
  add and *how much* the phenotype-matching adds over ML alone.
- **What to look for on full-text read.**
  1. Which ML pathogenicity models are in the ensemble — and are they
     independently scored or blended?
  2. Which HPO-matching algorithm — resnik/lin semantic similarity,
     graph-embedding based (Phen2Gene / PhenoApt), or LLM-mediated?
  3. What's the evaluation cohort — real solved-case series, or a
     simulated benchmark like the ClinVar-injected-into-UDN dataset?
     Real diagnostic-yield uplift is the only claim that matters
     clinically.
  4. How does it compare head-to-head to Exomiser / LIRICAL on the
     same held-out cases? If they don't report this, treat the yield
     claim with caution.
- **Triage bucket.** **HIGH.**

---

### 6. Ampadu-Yeboah et al. — Obesity classification for multimorbidity trajectory prediction (Clin Obes, 2026)

- **Citation.** Ampadu-Yeboah A, Carr A, Ho F, Gill J, Sattar N,
  Jani BD. *Classification and Severity Assessment of Obesity in
  Clinical Risk Prediction of Multimorbidity Trajectories.*
  **Clin Obes.** 2026 Aug; 16(4): e70097. doi:10.1111/cob.70097.
  PMID 42457618.
- **Why it lands on your threads.** Multimorbidity-trajectory paper
  from the Glasgow (Sattar / Jani / Ho / Gill) cardiometabolic-
  epidemiology axis — surfaced in the `UK Biobank` PubMed feed, so
  presumably UK Biobank cohort. The framing — *severity of obesity* as
  a stratifier for multimorbidity trajectory — is exactly the pattern
  you flagged in the multimorbidity thread (chronic-disease clustering
  applied to cardiometabolic disease).
- **What to look for on full-text read.**
  1. What's the trajectory-modeling method — LCA, LCGA/GBTM,
     sequence-clustering, or something newer (e.g., latent-topic
     model on phecode sequences)?
  2. How is obesity graded — BMI class only, or BMI + waist + a
     metabolic-syndrome composite?
  3. Are the identified trajectory clusters *stable* under
     sensitivity re-clustering, or do they collapse when the number
     of allowed classes is perturbed?
- **Triage bucket.** **HIGH** on multimorbidity thread.

---

### 7. Zemanick et al. — Lumacaftor/Ivacaftor long-term pediatric safety (ERJ Open, 2026)

- **Citation.** Zemanick ET, McColley SA, Linnemann RW et al. *Long-
  term safety and efficacy of Lumacaftor/Ivacaftor in children 12
  months of age and older with cystic fibrosis: a 96-week open-label
  study.* **ERJ Open Res.** 2026 (surfaced in the Patrick Ryan Scholar
  feed).
- **Why it lands on your threads.** Directly on the CFTR modulator
  pharmacoepi thread — this is a **prospective open-label** study, not
  an EHR-based real-world design, so it's a modulator-outcomes anchor
  paper, not a methods paper. Still important for the modulator-in-
  infants safety narrative: the CFTR-modulator eligibility question is
  slowly being pushed to younger ages, and Lumacaftor/Ivacaftor
  specifically is now the older/dropped modulator (Trikafta being
  standard-of-care) — so the 96-week safety readout is a *legacy*
  regimen readout rather than a Trikafta expansion. Useful context for
  where the Trikafta-in-infants literature is going next.
- **What to look for on full-text read.**
  1. What's the retention / dropout rate at 96 weeks and what were
     the primary AE-driven discontinuations?
  2. Growth / weight-for-age trajectories in the treated infants —
     this is the perennial concern of pediatric CFTR-modulator use.
  3. Whether the paper reports enough natural-history context that
     you could use it as a comparator for a Trikafta-in-infants
     real-world analysis.
- **Triage bucket.** **HIGH (disease-thread).**

---

## Detailed reports — METHODS-WATCH

### 8. Li R et al. — MR + single-cell eQTL druggable-genome scan for chronic lung disease (J Transl Med, 2026)

- **Citation.** Li R, Cheng J, Liu Y, Zhang X, Zhang Z. *Translational
  prioritization of genetically supported candidate targets and
  pharmacological annotations for chronic lung diseases: a single-cell
  eQTL-guided multi-cohort study.* **J Transl Med.** 2026 Jul 15
  (online ahead of print). doi:10.1186/s12967-026-08625-w.
  PMID 42458479. Surfaced in *both* the `UK Biobank` and `drug
  repurposing` PubMed feeds.
- **Why it's METHODS-WATCH rather than HIGH.** The single-cell-eQTL-
  guided druggable-genome-scan design is the current template for
  "genetics-guided drug repurposing" (following the OpenTargets +
  Priority-Index lineage). It's on-thread for your drug-repurposing
  interest — but this specific instance is applied to chronic lung
  disease, which is not on your active disease list. The value is
  the *pipeline* (which cell-type eQTL panel, how they filtered
  druggable-genome, how pharmacological annotation was joined), not
  the specific candidate list.
- **What to look for.**
  1. Which single-cell eQTL panel — OneK1K, Randolph et al., or a
     new lung-specific one?
  2. Are the candidate targets ranked by MR effect size, cell-type
     specificity, or a compound score?
  3. Is the pharmacological annotation from ChEMBL / DrugBank / DGIdb,
     and does the paper actually name specific repurposing candidates
     with clinical-development-stage annotation?
- **Triage bucket.** **METHODS-WATCH.**

---

### 9. Guntoro et al. — Evo 2 embedding probes for biosecurity (arXiv 2607.14070)

- **Citation.** Guntoro J, Dack A, Danno D, Jančovičová M, Jurinović K,
  Smilansky V. *Screening of Biosecurity Features in Metagenomic Data
  with Evo 2 Probes.* **arXiv:2607.14070v1.** 2026 Jul 15. Primary
  category q-bio.GN. From the AIxBio Hackathon 2026 (BlueDot Impact /
  Apart Research / Cambridge Biosecurity Hub).
- **Why it's SKIP-for-research but noted here.** Only qualifying paper
  in today's arxiv digest and the only new hit on the `foundation
  model` keyword — hence its appearance here. Genuine research
  contribution (probing frozen Evo 2 layer-26 activations for AMR /
  virulence signal, showing ROC-AUC 0.888–0.977 for AMR detection with
  linear + attention probes) — but the *application* (metagenomic
  biosecurity surveillance) does not intersect your EHR / phecode /
  biobank / clinical-decision threads.
- **Triage bucket.** **SKIP.** (Noted only for completeness.)

---

## Also-noted (SKIP or SKIM only)

From the `UK Biobank` PubMed feed, the following are single-endpoint
UKB epidemiology papers with no direct methods overlap on your active
threads — worth a glance only if a specific disease intersects your
active work:

- Wan et al. — colorectal cancer after polyp removal, UKB cohort
  (PMID 42460415). *Skim if actively working on CRC.*
- Zhang, Zhang, Qiu, Hu — disease-predominant loci across AD / PD /
  DLB, UKB conditional GWAS + colocalization (PMID 42460153).
  *Genetic-epi methods paper; relevant if working on
  neurodegenerative pleiotropy.*
- Zeng J et al. — childhood underweight + adult obesity → MASLD /
  cirrhosis, 375,125-adult cohort (PMID 42458890). *Life-course
  epidemiology, not on-thread.*
- Jiang, Jing, Han, Ye, Zhao — sex-specific genetic effects across
  733 UKB traits (PMID 42458269). *Genetic-epi methods; sex-
  stratified phewas-scale scan.*
- Buonocore et al. — epilepsy risk after adult-onset hydrocephalus,
  UKB (PMID 42458109). *Off-thread.*
- Rask-Andersen et al. — age-related adiposity + cardiometabolic
  disease risk, UKB (PMID 42457939). *Off-thread.*
- Wang Y et al. — instant vs. filtered coffee + biological aging, UKB
  (PMID 42457711). *Off-thread; low-prior on causal validity.*
- Hilliard et al. — loneliness / social isolation and health, UKB
  (Nat Commun, PMID 42457663). *Off-thread.*
- Yin et al. — physical activity and depression in axSpA
  (PMID 42457341). *Cross-sectional, off-thread.*
- Kearns et al. — epidural analgesia in labour and neonatal /
  childhood outcomes, BMJ (PMID 42457242). *Off-thread.*
- Chang et al. — mental health / biological aging / lifestyle
  mediating SDoH → dementia (PMID 42456853). *Off-thread.*
- Yan, Lin, Wu — CKD-stratified plasma proteomic signatures of
  sarcopenia, UKB (PMID 42456803). *Off-thread; proteomics-first
  design.*
- Tang & Storey — generalized test of genotype–phenotype causality in
  population-sampled nuclear families, PLoS Genet (PMID 42455868).
  *Methods paper on family-based causal inference; interesting if
  extending FBAT-lineage work.*
- Xiao et al. — cardiovascular-kidney-metabolic-syndrome staging and
  cancer risk, proteomic/metabolomic mediators (PMID 42455107).
  *Off-thread.*
- Chaput et al. — sleep duration + health, self-reported vs. device
  (PMID 42454954). *Off-thread.*
- Yang L et al. — CX3CL1 / UMOD and AKI risk, MR + clinical
  validation (PMID 42454155). *Off-thread.*
- Huang et al. — accelerometer MVPA + cancer risk, UKB
  (PMID 42450828). *Off-thread.*
- Breton et al. — sex-stratified genetics of late-adulthood brain
  volumes (PMID 42449465). *Off-thread.*

From the `drug repurposing` PubMed feed — all off-thread except for
the Li et al. paper covered above:

- Guo et al. — S100A9 as PAD/sarcopenia biomarker (PMID 42460156).
- Kim W et al. — PKLR / JNK inhibition for MASLD/MASH
  (PMID 42460009). *Preclinical med-chem.*
- Shi et al. — AI in cancer radiotherapy/immunotherapy review
  (PMID 42459675). *Review, off-thread.*
- Coonen et al. — vascular tissue repurposing for organ-bath
  standardization (PMID 42457096). *Off-thread bench-methods.*
- Chen H — marimastat for snakebite (PMID 42456951). *Off-thread.*
- Colarusso et al. — isoxazol-thiazolidinones for ERα in breast
  cancer (PMID 42456473). *Med-chem repositioning.*
- Du S — PI4K/PIPK families in breast cancer review
  (PMID 42455373). *Review.*
- Reghu et al. — small-molecule adjuncts to antivenom therapy
  (PMID 42450267). *Off-thread.*
- Keskin et al. — hydroquinidine in DMH rat colon cancer model
  (PMID 42449947). *Preclinical, off-thread.*

From other Scholar keyword feeds (07-16 03:29Z) — no on-thread hits
beyond the ones surfaced above:

- `All of Us research program` — one paper (Mbaocha, food/housing
  insecurity + depression in Black immigrants, 2026 dissertation).
  *Off-thread; not a methods paper.*
- `Foundation models + electronic health records` — one paper
  (Debnath & De, "AI in Human Health: A Comprehensive Review", Acta
  Sci Med Sci). *General review, not a foundation-model methods
  paper.*
- `electronic health records` — Prosper, blockchain for EHR in cloud
  healthcare, 2026. *Off-thread infrastructure paper.*
- `knowledge graph` — Dhawan et al., Ayurveda-Net causal KG for
  herbal actions. *Off-thread; not biomedical KG in the sense
  you care about.*
- `rare diseases` — Nenkova et al., rare-disease policy in Bulgaria /
  Romania / Greece. *Off-thread (policy, not diagnostics).*
- `clonal hematopoiesis` (intitle:) — Yigitbasi et al., CH in newly
  diagnosed multiple myeloma → neutropenia / supportive-care burden /
  survival. *Directly on the CHIP disease thread but small single-
  center cohort — SKIM only.*
- `autoimmune` — Sturm et al., caesarean birth + twin-discordant
  outcomes. *Off-thread.*
- `drug repurposing` (Scholar) — Sun et al., drug-repurposing
  nanotheranostic for resistant bacterial pneumonia. *Off-thread
  (nanomedicine, not clinical evidence-based repurposing).*

From author-feed alerts (07-14 22:27Z):

- **Joshua C. Denny** — surfaced the Wu / Lee / Abiri / Ionita-Laza
  matrix-completion paper (covered above as HIGH #2).
- **Jure Leskovec** — Huang, Zhang, Wang, Qu, Lu, Li et al.,
  *Autonomous biomedical research with an artificial intelligence
  agent*, **Science** 2026. *Off your active threads (LLM-agent
  research automation), but worth a look given the venue and the
  Leskovec authorship — potential methods relevance for downstream
  EHR-agent work.* **SKIM.**
- **Christopher G. Chute** — Truong & Ritchie, "Eras of bioinformatics
  technologies from CLI to AI chatbots" (Brief Bioinform).
  *Historical / perspective piece, off-thread.*
- **Patrick Ryan** — Zemanick et al., Lumacaftor/Ivacaftor pediatric
  (covered above as HIGH #7).

---

## Pipeline / infrastructure notes

- `arxiv-digest` output is unusually thin this window (1 relevant
  paper 07-16 with 1 previously-surfaced suppressed; 1 paper 07-15).
  This is consistent with mid-July arXiv submission seasonality
  rather than a pipeline failure (unlike the 2026-06-20 fetch-failure
  incident) — the digest header explicitly reports "1 relevant (1
  previously surfaced, suppressed)" rather than a fetch error. No
  action needed on the pipeline.
- Consider whether the `foundation model` keyword should be tightened
  to `foundation model` NEAR/10 (`ehr` OR `clinical` OR `patient`)
  to filter out biosecurity / metagenomic / vision applications that
  do not intersect the EHR-FM thread. Today's Guntoro et al. paper
  is the second time in recent memory that a genomic-foundation-model
  paper cleared the filter without being on-thread for your EHR-FM
  work.
- The two `target trial emulation` hits in a single PubMed batch
  (Xu X et al. losartan; Xu Y et al. antidepressants) suggest the
  TTE literature is now consistently productive at this cadence.
  Worth considering whether to add `target trial emulation` as a
  first-class thread section in INTERESTS.md (currently folded into
  the causal-inference thread).

---

*Report generated automatically from Gmail alert emails + `arxiv-
digest` output. No full-text article reads were performed; all
detailed reports above are inferred from title / venue / authors /
snippet metadata and should be verified against the paper before
citation.*
