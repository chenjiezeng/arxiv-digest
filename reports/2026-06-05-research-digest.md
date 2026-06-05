# Research digest report — 2026-06-05

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-06-02 → 2026-06-05** (since the prior 2026-06-01 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-03 → 06-05 | Three batches: 06-03 19:07 UTC (author + keyword), 06-04 08:37 UTC (keyword), 06-05 01:15 UTC + 05:56 UTC (author + keyword). |
| `arxiv-digest` repo (`digests/`) | 2026-06-02 → 06-03 | **Still empty.** 06-02 = 0; 06-03 = 0 with 3/4 categories failing to fetch (q-bio.QM, q-bio.GN, q-bio.PE). Pipeline remains silent. |
| GitHub `arxiv-digest` email notifications | window | None received this window (workflow run notifications not arriving in Gmail). |
| PubMed `What's new` (NCBI) — UK Biobank | 2026-06-04 | Aggregate collection digest; not individually triaged. |
| Raw arXiv daily mailings (`no-reply@arxiv.org`) | daily | Unfiltered cs/q-bio/stat list; not triaged here. |

> ⚠️ **Pipeline status (third consecutive report).** `arxiv-digest` produced
> **zero** relevant items on both 06-02 and 06-03, and 06-03 again logged
> "3/4 categories failed to fetch" — the same q-bio fetch failure noted in
> the 05-29 and 06-01 reports. This has now been the dominant failure
> mode for **6+ days running**. Worth opening an issue in the repo to
> investigate (a) the upstream arXiv API call (5xx? rate-limiting? changed
> endpoint?), (b) whether the fetcher retries, and (c) whether `cs.LG` /
> `stat.ME` / medRxiv / bioRxiv ingest should be added so the pipeline
> isn't fully dependent on q-bio uptime. Every actionable item in this
> report came from Scholar, not from `arxiv-digest`.

> Caveat: Scholar alert emails contain title, authors, venue, and the first
> ~2-3 lines of each abstract only. The reports below contextualize that
> metadata against your research threads; nothing here reflects full-text
> reading.

---

## Executive summary

- **Cystic fibrosis is the dominant cluster this window.** Five distinct
  CFTR/CF papers surfaced, all from the Chenjie Zeng "new related research"
  alert + Patrick Ryan alert. Most notable: a *J Cystic Fibrosis* paper on
  **discontinuation of GLP-1 RA therapy in pwCF** (Singh et al.) — sits
  squarely at the intersection of two of your tracked threads (CF/CFTR
  pharmacoepi **+** GLP-1 RA drug class) and is the single most directly
  on-thread paper of the window.
- **Variant interpretation / penetrance** got a notable signal — an *Obstet
  Gynecol Survey* commentary on a paper titled "Residual Allelic Activity
  Likely Underlies the Low Rates of Disease Expression for Predicted
  Loss-of-Function Variants in Population-Scale Biobanks" — directly on
  your pLoF + biobank-penetrance thread.
- **All of Us** continues to be the dominant biobank cluster (8+ AoU hits
  in the 06-05 keyword feed alone). A *Nature Genetics* MASLD
  transcriptional regulation paper benchmarks a new PRS against existing
  models in AoU; a methods preprint (Liu/Wang/Altman, Stanford) gives a
  *practical upper bound on selection bias* for medical prediction with AoU
  + MIMIC-IV worked examples.
- **CHIP** continues to compound (Weyrich et al., *Eur J Heart Fail*):
  independent + dose-dependent contributions of CHIP and mosaic Loss of Y
  to incident heart failure. Adds heart failure to the CHIP→stroke (Bick,
  05-29 report) and CHIP→post-HCT-CV (Thulluri, 06-01 report) cluster.
- **EHR phenotyping / data quality** has a high-tier hit: *npj Digital
  Medicine* paper from Gilad-Bachrach's group on a generative semantic
  auditor for EHRs (Girshovitz et al.). Plus a medRxiv preprint on LLM-based
  ADE extraction from notes (Plasek et al., Mass General Brigham).
- **Drug repurposing**: a *Nature Reviews Cancer* perspective on
  mutation-centric kinase drug repurposing for rare cancers (Chan et al.,
  Subbiah/Gujral group) and a multi-relational KG repurposing + side-effect
  prediction paper (Sharmin & Mahmud).
- **Genetic epi**: a *Circulation* genome-first FH paper across African vs
  European ancestry (Winters et al.) — directly on the
  monogenic-penetrance-by-ancestry thread.
- **EHR foundation models**: an arXiv ChatHealthAI paper (Wang et al.,
  2606.02802) aligning EHR representations with LLMs for grounded clinical
  reasoning. Plus a lower-tier multimodal FM review (Sood).

Counts (this window): **16 HIGH**, **5 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. Changes in metabolic and pulmonary outcomes after discontinuation of glucagon-like-peptide-1 receptor agonist therapy in people with cystic fibrosis
- **Authors / venue:** A. Singh, A. Horvit, J. Abramowitz, M. Abreu, K. Kaput et al. — *Journal of Cystic Fibrosis*, 2026 ([S1569-1993(26)00107-4](https://www.sciencedirect.com/science/article/pii/S1569199326001153)).
- **Surfaced by:** Patrick Ryan "new related research" alert (06-05).
- **Thread:** Pharmacoepidemiology (GLP-1 drug class) **+** Cystic fibrosis / CFTR (modulator pharmacoepi). **Hits two tracked threads simultaneously.**
- **What it is:** Real-world study of *discontinuation* of GLP-1 RAs in
  people with CF — GLP-1 RAs are increasingly prescribed off-label in
  pwCF for weight management or CFRD (CF-related diabetes), and this paper
  evaluates metabolic and pulmonary outcomes after stopping therapy. Snippet
  emphasizes off-label use, weight management, and CFRD framing.
- **Why it matters to you:** This is the single highest-relevance paper of
  the window. GLP-1 RA pharmacoepi is one of your active drug-class threads,
  and CF-specific modulator/medication pharmacoepi is another — papers
  hitting *both* are rare and worth reading in full. Methodologically
  interesting because discontinuation studies require careful handling of
  time-varying exposure + immortal-time bias (typical Cox-with-time-varying-
  covariate or TTE w/ a "treatment-cessation" target). In CF this is also
  doubly confounded by CFTR-modulator co-exposure (Trikafta era) — pwCF on
  modulators gain weight, which interacts with the GLP-1 indication. Look
  for whether they stratify by modulator status.
- **Action:** **HIGH (read first)** — read for (i) the discontinuation
  exposure definition (gap days? prescription run-out?), (ii) modulator-
  era stratification, (iii) pulmonary outcome ascertainment (ppFEV1 vs
  exacerbation events), and (iv) the comparator (continuers vs never-users).

### 2. Ensuring equity in reproductive carrier screening of CFTR with increasing population diversity
- **Authors / venue:** M.J. Gruzin, J. Knezovich, S. Poll, N. Schonrock et al. — *Journal of Cystic Fibrosis*, 2026 ([S1569-1993(26)00107-4 fulltext](https://www.cysticfibrosisjournal.com/article/S1569-1993(26)00107-4/fulltext)).
- **Surfaced by:** **Chenjie Zeng** "new related research" alert (06-05) — i.e., adjacent to your own work.
- **Thread:** CF/CFTR disease **+** variant interpretation (ACMG / ancestry-aware
  classification) **+** cross-ancestry portability.
- **What it is:** CFTR carrier-screening equity audit — the standard
  Ashkenazi/European-ancestry-derived CFTR panels miss variants common in
  other ancestries, and this paper evaluates how to expand screening
  panels with increasing population diversity.
- **Why it matters to you:** CFTR variant interpretation across ancestries
  is a recurring tension in CF screening — gnomAD-derived population
  frequencies drive ACMG PM2/BS1 evidence, and panels designed in European-
  ancestry cohorts under-detect carriers in African, Asian, and Hispanic/
  Latino populations. Sits directly at the intersection of your CF thread
  and your variant-interpretation thread; relevant for any of your
  population-screening / penetrance work that touches CFTR. Pairs naturally
  with the Norton commentary (#11 below) on pLoF penetrance in biobanks.
- **Action:** **HIGH** — read for the carrier-frequency methodology by
  ancestry and the recommended panel-design changes; cite when justifying
  ancestry-stratified CFTR analyses.

### 3. A Genome-First Study of Familial Hypercholesterolemia Comparing African and European Ancestry Individuals
- **Authors / venue:** A.H. Winters, M.A. Kelly, M.G. Syed, T. Bergquist, A.S.F. Berry et al. — *Circulation*, 2026 ([10.1161/CIRCULATIONAHA.126.080694](https://www.ahajournals.org/doi/pdf/10.1161/CIRCULATIONAHA.126.080694)).
- **Surfaced by:** Chenjie Zeng "new related research" alert (06-05).
- **Thread:** Variant interpretation **+** PheWAS/penetrance **+** genetic
  epidemiology (genome-first / monogenic-in-population) **+** ancestry-aware risk.
- **What it is:** Genome-first study of FH in African vs European ancestry
  individuals. FH research has historically focused on European-ancestry
  cohorts; this paper compares the burden, penetrance, and presentation of
  pathogenic FH variants (LDLR, APOB, PCSK9) across ancestries — i.e., a
  *genome-first* design that ascertains carriers from genotype and looks
  forward to phenotype, rather than the more common clinical-ascertainment
  direction.
- **Why it matters to you:** This is *exactly* the template you use for
  CFTR/APOL1 monogenic-penetrance-in-biobank work: genome-first
  ascertainment, ancestry-stratified comparison, PheRS-adjacent phenotype
  scoring. Publication in *Circulation* signals it's the new reference
  paper for cross-ancestry monogenic-penetrance design. Bergquist is the
  Geisinger genomics-screening lead — likely uses MyCode / DiscovEHR or
  AoU+MVP+UKB pool.
- **Action:** **HIGH** — read for (i) carrier-ascertainment pipeline, (ii)
  ancestry-stratified penetrance estimates and CIs, (iii) the LDL-C /
  ASCVD outcome operationalization, and (iv) whether they incorporate PRS
  background. Template-relevant for your APOL1 and CFTR work.

### 4. Comparison of Long Term Effects of Treatment of Different CFTR Modulators in People With Cystic Fibrosis
- **Authors / venue:** P. Famulska, B. Więckowska, B. Narożna, E. Sapiejka et al. — *Pediatric Pulmonology*, 2026 ([ppul.71681](https://onlinelibrary.wiley.com/doi/abs/10.1002/ppul.71681)).
- **Surfaced by:** Chenjie Zeng "new related research" alert (06-05).
- **Thread:** Cystic fibrosis / CFTR (modulator pharmacoepi — Trikafta / ivacaftor / lumacaftor).
- **What it is:** Long-term comparative effectiveness of different CFTR
  modulators (ivacaftor / lumacaftor-ivacaftor / tezacaftor-ivacaftor /
  elexacaftor-tezacaftor-ivacaftor) in pwCF — likely covers ppFEV1, BMI,
  exacerbation rate, and quality-of-life endpoints over multi-year follow-
  up. Pediatric Pulmonology suggests pediatric/young-adult cohort emphasis.
- **Why it matters to you:** Direct hit on your CFTR-modulator pharmacoepi
  sub-thread. Comparative effectiveness across modulator regimens (rather
  than vs. no-modulator) is exactly the kind of head-to-head design that
  the modulator literature is still light on, especially in real-world
  (vs. trial) populations.
- **Action:** **HIGH** — read for the modulator-comparison design (head-
  to-head vs. sequential cohorts), follow-up window, and switching-bias
  handling.

### 5. Efficacy and safety of the cystic fibrosis transmembrane conductance regulator inhibitor GLPG2737 for autosomal dominant polycystic kidney disease: phase 2a MANGROVE study
- **Authors / venue:** R.T. Gansevoort, M. Hueso, A. Pisani, D. Van den Bergh et al. — *Nephrology Dialysis Transplantation*, 2026 ([gfag093](https://academic.oup.com/ndt/advance-article-pdf/doi/10.1093/ndt/gfag093/68411102/gfag093.pdf)).
- **Surfaced by:** Chenjie Zeng "new related research" alert (06-05).
- **Thread:** Drug repurposing (CFTR drug → kidney disease) **+** CF/CFTR.
- **What it is:** Phase 2a trial of GLPG2737 — a *CFTR inhibitor*
  (mirror-image use case to the CF modulator/potentiator/corrector class)
  — in autosomal dominant polycystic kidney disease (ADPKD). Mechanism:
  CFTR drives fluid secretion into renal cysts, and inhibiting CFTR may
  slow cyst growth.
- **Why it matters to you:** A clean *repurposing* / cross-disease use of
  the CFTR drug platform — CFTR modulators target CF; CFTR inhibitors
  target ADPKD. This is the kind of mechanism-driven repurposing your
  drug-repurposing thread is interested in, anchored in a clinical-evidence
  trial rather than an in-silico KG prediction. Useful as a *positive*
  case study if you're benchmarking explainable KG repurposing
  predictions against established mechanism-based candidates.
- **Action:** **HIGH (repurposing case study)** — skim the mechanism
  framing and the phase-2a endpoints (eGFR slope? total kidney volume?);
  use as a reference for "repurposing with mechanistic rationale" in any
  KG / GNN repurposing evaluation work.

### 6. Independent and Dose-Dependent Contributions of Clonal Hematopoiesis and Mosaic Loss of Y to Incident Heart Failure
- **Authors / venue:** M. Weyrich, A. Ware, J. Windschmitt, T. Sarakpi et al. — *European Journal of Heart Failure*, 2026 ([xuag187](https://academic.oup.com/eurjhf/advance-article-pdf/doi/10.1093/ejhf/xuag187/68439318/xuag187.pdf)).
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert (06-04).
- **Thread:** Clonal hematopoiesis (CHIP) disease thread **+** somatic mosaicism
  (mLOY adjacent).
- **What it is:** Joint analysis of CHIP **and** mosaic Loss of Y (mLOY)
  effects on *incident* heart failure, framed as independent + dose-
  dependent contributions. The snippet emphasizes "age-related acquired
  somatic mutations in hematopoietic stem cells … independent risk factors
  for … cardiovascular diseases."
- **Why it matters to you:** Extends the CHIP→CV literature into heart
  failure specifically (after the 05-29 Bick stroke paper and the 06-01
  Thulluri post-HCT CV paper). What makes *this* paper interesting:
  treating CHIP and mLOY as **co-modeled** somatic exposures with
  *dose-dependent* (VAF-graded) effects. That co-modeling structure is
  directly relevant to your composite-risk thread — you've been thinking
  about how to stack CHIP with PRS, and the CHIP+mLOY case is the
  smaller-scale prototype for "stack-of-somatic-events" risk.
- **Action:** **HIGH** — read for the VAF cut-points, the joint-vs-
  independent effect parameterization, and whether they incorporate gene-
  specific CHIP (DNMT3A vs TET2 vs ASXL1) effects.

### 7. A generative approach for semantic auditing of electronic health records
- **Authors / venue:** I. Girshovitz, A. Ambus, M. Shahar, R. Gilad-Bachrach — *npj Digital Medicine*, 2026 ([s41746-026-02809-w](https://www.nature.com/articles/s41746-026-02809-w_reference.pdf)).
- **Surfaced by:** George Hripcsak "new related research" alert (06-05).
- **Thread:** EHR phenotyping (data quality, LLM-assisted) **+** EHR foundation models (generative).
- **What it is:** Generative-model approach to *semantic* (not syntactic)
  auditing of EHR data — i.e., flagging clinical implausibilities that
  pass schema-level validation but are inconsistent with medical knowledge
  (e.g., pregnancy code on a male patient, dose 100× the typical for a
  drug, lab value incompatible with the recorded sex/age). Snippet
  emphasizes "Current quality assessments are limited: they either focus
  on syntax or rely on labor[-intensive review]."
- **Why it matters to you:** This is the natural complement to the Kwon
  et al. "reasoning-intensive consistency verification" paper from the
  06-01 report (#11 in that report). Together, they form a methodological
  pair: Girshovitz/Gilad-Bachrach use *generative models* to flag implausi-
  bilities at the semantic layer; Kwon et al. use *LLM reasoning* to flag
  note-vs-structured discordance. Both feed into your AoU / OMOP data-
  quality + computable-phenotype workflow. *npj Digital Medicine* is the
  higher-tier venue.
- **Action:** **HIGH** — read for the generative-audit formulation, the
  inconsistency taxonomy, and how the audit signal would integrate into a
  computable-phenotype QC pipeline. Pair with Kwon et al.

### 8. Relationship Extraction for Adverse Drug Events in Clinical Notes Using Large Language Models
- **Authors / venue:** J.M. Plasek, Y. Li, M.G. Amato, D. Foer, D.L. Seger et al. — *medRxiv*, 2026 ([10.64898/2026.05.28.26354362](https://www.medrxiv.org/content/10.64898/2026.05.28.26354362.full.pdf)).
- **Surfaced by:** George Hripcsak "new related research" alert (06-05).
- **Thread:** EHR phenotyping (LLM-assisted, NLP from notes) **+** pharmacoepidemiology (ADE ascertainment).
- **What it is:** Generative-LLM-based relation extraction for adverse
  drug events (ADEs) from free-text clinical notes — a phenotype-from-
  notes task where the structured codes systematically under-capture ADEs
  and LLMs may be able to fill the gap.
- **Why it matters to you:** Your pharmacoepi work (GLP-1, SGLT2,
  modulators, HRT) increasingly depends on accurate adverse-event
  ascertainment, and structured codes capture only a fraction of the
  signal that's in notes. An LLM relation-extractor for ADE
  (drug → adverse-event) tuples is directly slot-in-able to the AoU
  pipeline. Mass General Brigham authorship (Plasek, Bates lab adjacent)
  is a quality signal.
- **Action:** **HIGH** — read for the relation schema (drug-event-temporal
  vs drug-event), the LLM prompt/fine-tune choice, and reported precision/
  recall against a clinician-adjudicated reference set.

### 9. Exploring Disparities in Post-Fracture Osteoporosis Pharmacotherapy Initiation: A Retrospective Cohort Study Utilizing the All of Us Research Database
- **Authors / venue:** R. Shabbir, S. Lareef, Z. Kang, B. Layton, R. Hoy et al. — *Osteology*, 2026 ([10.3390/osteology6020010](https://www.mdpi.com/2673-4036/6/2/10)).
- **Surfaced by:** "All of Us research program" keyword alert (06-05).
- **Thread:** EHR-linked biobanks (AoU) **+** pharmacoepidemiology (treatment
  initiation disparities).
- **What it is:** AoU retrospective cohort estimating the rate of
  osteoporosis pharmacotherapy initiation after a fragility fracture, and
  the demographic disparities therein.
- **Why it matters to you:** AoU treatment-initiation studies are a useful
  reference shape for any of your real-world prescribing analyses
  (GLP-1/SGLT2/HRT). The osteoporosis-after-fracture treatment-initiation
  gap is a well-known pharmacoepi finding in registry data, and replicating
  it in AoU validates AoU's medication-data coverage. Lower-tier journal,
  but useful as a methods reference for AoU exposure operationalization.
- **Action:** **HIGH (AoU methods reference)** — skim for AoU medication
  data operationalization (RxNorm / drug-era queries) and the
  fracture-index-date logic (ICD-10 vs imaging vs procedure codes).

### 10. A Practical Upper Bound on Selection Bias Effects in Medical Prediction Models
- **Authors / venue:** K. Liu, M. Wang, R.B. Altman — *arXiv:2606.00563*, 2026 ([arxiv.org/abs/2606.00563](https://arxiv.org/pdf/2606.00563)).
- **Surfaced by:** "All of Us research program" keyword alert (06-05).
- **Thread:** ML for precision health (selection bias / external validation)
  **+** EHR-linked biobanks (AoU + MIMIC-IV worked examples).
- **What it is:** Methods paper that derives a *practical upper bound* on
  selection-bias-induced performance gaps in medical prediction models,
  with experiments on synthetic data, semi-synthetic data derived from
  AoU, and real-world selection bias in MIMIC-IV.
- **Why it matters to you:** Selection bias in AoU is a recurring concern
  (AoU is participant-enrolled, with known representation skews) and a
  *quantitative upper bound* on the bias contribution to prediction
  performance is exactly the kind of methods tool you'd want when
  externally validating a precision-health model across AoU vs UKB vs
  MVP. Altman lab quality signal (Stanford). Note: arXiv preprint, so the
  bound formulation may still evolve.
- **Action:** **HIGH (methods-watch → potentially methods-cite)** — read
  for the bound derivation and the AoU semi-synthetic worked example.
  Pair with Van Calster / Collins fairness-calibration work flagged in the
  06-01 METHODS-WATCH bucket.

### 11. Comment on "Residual Allelic Activity Likely Underlies the Low Rates of Disease Expression for Predicted Loss-of-Function Variants in Population-Scale Biobanks"
- **Authors / venue:** M.E. Norton — *Obstetrical & Gynecological Survey*, 2026 (commentary).
- **Surfaced by:** "All of Us research program" keyword alert (06-05).
- **Thread:** Variant interpretation (pLoF, LOFTEE) **+** PheWAS / penetrance
  in population biobanks **+** rare disease.
- **What it is:** Commentary on a primary paper arguing that *residual
  allelic activity* (i.e., the pLoF allele isn't actually null — leaky
  splicing, downstream initiation, etc.) explains the low penetrance of
  pLoF variants observed in biobanks. Norton is a reproductive-genetics
  expert; the commentary is in an Ob/Gyn survey journal.
- **Why it matters to you:** **This is squarely on your population-
  screening penetrance thread.** The "low penetrance of pLoFs in biobanks"
  observation is the central tension in clinically-ascertained-vs-
  population-screening penetrance estimation (the gap your monogenic-
  penetrance work tries to characterize). If the *mechanism* is residual
  allelic activity rather than ascertainment / age-of-onset / modifiers,
  then the implications for population screening are different: you'd
  expect penetrance to correlate with *quantitative* residual function
  rather than binary pLoF status. Worth tracking down the original primary
  paper that this commentary discusses.
- **Action:** **HIGH** — locate and read the *primary* paper this is
  commenting on (likely a recent *AJHG* / *Nature Genetics* paper). Then
  read the commentary for the clinical-screening implications.

### 12. Statistical Methods for Genetic Analysis of Survival Traits
- **Authors / venue:** D.H. Kim — dissertation, 2026 ([escholarship qt93q2p5ts](https://escholarship.org/content/qt93q2p5ts/qt93q2p5ts.pdf)).
- **Surfaced by:** "All of Us research program" keyword alert (06-05).
- **Thread:** Genetic epidemiology (GWAS for time-to-event outcomes in biobanks).
- **What it is:** PhD dissertation on statistical methods for GWAS of
  survival traits (disease onset, time-to-event) in biobank-scale data.
  Likely covers SPACox-style score tests, frailty models, and Cox-based
  burden tests.
- **Why it matters to you:** Most biobank GWAS still use logistic-on-
  prevalent-disease; survival-trait GWAS is the natural extension when you
  have EHR-derived disease onset times (AoU, UKB), and it's especially
  relevant to your CHIP-incident-CV and CFTR-modulator-time-to-event
  analyses. Dissertation-level depth typically gives more methodological
  detail than the journal versions of the same work.
- **Action:** **HIGH (methods reference)** — skim the chapter-level
  table of contents; identify which chapters cover (i) score-test
  approximations under censoring, (ii) frailty / random-effects in
  biobanks, and (iii) any worked examples on AoU.

### 13. Integrative analyses elucidate transcriptional regulatory functions of risk alleles for metabolic liver disease
- **Authors / venue:** B. Zhu, N. He, Y. Xiao, B. Chen, C. Li, R. Mandla, Y. Liu et al. — *Nature Genetics*, 2026 ([s41588-026-02617-8](https://www.nature.com/articles/s41588-026-02617-8)).
- **Surfaced by:** "All of Us research program" keyword alert (06-05).
- **Thread:** Genetic epidemiology (functional GWAS / MPRA / PRS) **+** EHR-
  linked biobanks (AoU benchmark) **+** MASLD (pharmacoepi-adjacent).
- **What it is:** Functional/MPRA-anchored fine-mapping of MASLD GWAS risk
  alleles, with construction of a *DAV PRS* (likely "deeply-annotated
  variant" PRS) benchmarked against existing MASLD PRS models in AoU.
  Snippet notes the new PRS "performed similarly to PRS9, its predictive
  power was modestly lower than [the prior].
- **Why it matters to you:** MASLD is your active pharmacoepi outcome
  (anchored to the GLP-1 RA + MASLD AJG paper from the 06-01 report). A
  *Nature Genetics* MPRA-prioritized MASLD PRS benchmarked in AoU is the
  natural genetic-epi partner to your MASLD pharmacoepi work — if you're
  doing GLP-1-RA + MASLD outcomes in AoU, having a contemporaneous MASLD
  PRS in the same cohort lets you (i) stratify pharmacoepi effects by
  genetic risk and (ii) test for PRS × treatment interaction. The honest
  reporting that the new PRS underperformed PRS9 is a useful signal of
  methodological maturity in the field.
- **Action:** **HIGH** — read for the AoU PRS benchmark (which prior PRSs,
  which performance metric, which ancestries) and consider citing in any
  AoU MASLD work.

### 14. Improving Genetic Risk Prediction of CAD in Chinese by Multi-ancestry and Multi-trait GWAS Integration
- **Authors / venue:** H. Wang, J. Lin, X. Hao, W. Tang, K. Wang, M. Jiang, D. Wu et al. — *Genomics, Proteomics & Bioinformatics*, 2026.
- **Surfaced by:** Jian Yang "new related research" alert (06-05).
- **Thread:** Genetic epidemiology (cross-ancestry PRS, multi-trait
  integration) **+** ML for precision health (clinical decision use of PRS).
- **What it is:** Multi-ancestry + multi-trait GWAS integration for
  improving CAD genetic risk prediction in Chinese (East Asian) ancestry.
  Multi-trait usually pools related CV traits (lipids, blood pressure) to
  boost CAD PRS power; multi-ancestry handles the trans-ethnic portability
  problem.
- **Why it matters to you:** Cross-ancestry PRS portability is on your
  tracked-list. Wang and the GPB venue suggest this is a methods-as-much-as-
  results paper, useful for any work where you're applying PRS across
  ancestries in AoU's diverse cohort.
- **Action:** **HIGH** — read for the multi-trait integration recipe
  (BOLT? MTAG? PRS-CSx?) and the East-Asian validation. Useful template
  for cross-ancestry PRS work in AoU.

### 15. Multi-Relational Knowledge Graph for Drug Repurposing and Side-Effect Burden Prediction Using Gene–Drug–Disease Associations
- **Authors / venue:** A. Sharmin, B.U. Mahmud — *BioChem*, 2026.
- **Surfaced by:** "drug repurposing" keyword alert (06-05).
- **Thread:** Drug repurposing (KG / GNN angle) **+** pharmacoepidemiology (side-effect burden).
- **What it is:** Multi-relational KG (gene–drug–disease edges) for
  repurposing predictions, with explicit side-effect burden modeling as a
  joint output. The side-effect head is the differentiator vs the typical
  link-prediction-only repurposing pipeline.
- **Why it matters to you:** Side-effect-aware repurposing is the
  *clinical-evidence-loop* version of KG repurposing that your INTERESTS
  file specifically calls out (vs. opaque link-prediction). However, the
  venue (*BioChem*) is unfamiliar, and you'd want to see whether the
  side-effect predictions are validated against FAERS / SIDER or just
  in-graph. Lower-tier venue caveat applies.
- **Action:** **HIGH (cautious)** — skim for the side-effect prediction
  validation source (FAERS? SIDER? OFFSIDES?) and whether the rationales
  are path-explainable. Demote to METHODS-WATCH if side-effect validation
  is purely in-graph.

### 16. Mutation-centric kinase drug repurposing for rare cancers
- **Authors / venue:** M. Chan, H. Ma, V. Subbiah, T.S. Gujral — *Nature Reviews Cancer*, 2026.
- **Surfaced by:** "drug repurposing" keyword alert (06-04).
- **Thread:** Drug repurposing **+** rare disease **+** variant interpretation (mutation-centric).
- **What it is:** *Nature Reviews Cancer* perspective on **mutation-
  centric** drug repurposing for rare cancers — i.e., using the specific
  oncogenic variant (rather than the disease label) as the repurposing
  target. Subbiah's group is a leader in tumor-agnostic / mutation-targeted
  oncology.
- **Why it matters to you:** Hits *two* tracked threads — drug repurposing
  *and* rare disease — and the framing (mutation as repurposing target) is
  conceptually close to your HPO-based rare-disease repurposing angle, but
  with variants rather than phenotypes as the index. Nature Reviews venue
  signals it's worth reading as a field-level orientation piece.
- **Action:** **HIGH (read as orientation)** — read the framework and
  the case studies; useful when writing intros for any of your rare-
  disease or repurposing manuscripts.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Mendelian Randomization Reveals Interleukin-6 Receptor-Lipoprotein(a)
  Interplay With Independent Cardiovascular Risk Reductions** — A.
  Kheirkhah, S. Di Maio, S. Coassin, S. Schönherr et al. — *JACC: Basic to
  Translational Science*, 2026. (Joshua C. Denny "new related research"
  alert, 06-03.) Two-exposure MR (IL-6R + Lp(a)) for CV risk. *Watch for:*
  the joint-MR / multivariable-MR setup — useful template for any of your
  drug-target-MR or proteome-MR work.
- **Time zero alignment in target trial emulation of VMAT2 inhibitors
  versus anticholinergics for tardive dyskinesia** — Y. Matsuda, Y.
  Suzuki — *Psychiatry and Clinical Neurosciences*. (Miguel Hernán
  "10 new citations" alert, 06-05.) Time-zero alignment is a textbook TTE
  issue and citing-Hernán signals it's the methods-grade discussion of
  the same issue you face in your GLP-1 / SGLT2 / modulator TTE work.
  *Watch for:* the specific time-zero strategy and any
  immortal-time-bias quantification.
- **Integrative multi-omics Mendelian randomization reveals key lipid
  metabolism genes as therapeutic targets for diabetic nephropathy
  pathogenesis** — S. Liu, Y. Xia, L. Ding et al. (Jian Yang citations
  alert, 06-05.) Another instance of the proteome-MR-for-drug-target-
  prioritization shape you've been seeing every window (now 5+ in the
  last three reports). Reinforces the prior suggestion to add
  `proteome-wide` / `colocalization` / `drug target` to `tracked.yaml`.
- **ChatHealthAI: Aligning EHR Representations with LLMs for Grounded
  Clinical Reasoning** — B.H. Wang, B. Peng, R. Wang, J. Bai, Z. Song, Y.
  Li — *arXiv:2606.02802*, 2026. (Foundation models + EHR keyword alert,
  06-05.) Alignment of an EHR-representation model with an LLM for
  grounded clinical reasoning. *Watch for:* the alignment recipe (cross-
  attention? contrastive? token-fusion?) — sits in the CLMBR/MOTOR/FEMR
  EHR-FM lineage you track. Demoted from HIGH because it's an arXiv
  preprint with little institutional signal in the snippet.
- **GWAS Identifies Novel Genetic Variants Associated with Knee Pain in UK
  Biobank (n = 439,743)** — Y. Tao, Q. Pan, T. Cai, L. Yang, M. Haque, T.
  Dottorini et al. — *Phenomics*, 2026. (Konrad Karczewski alert,
  06-03.) Big-N UKB GWAS on a chronic-pain phenotype. *Watch for:* the
  knee-pain phenotype definition (self-report vs ICD-10 vs prescription)
  — useful template for any of your phecode-defined chronic-condition GWAS.

---

## NOTABLE: contextual / borderline items

- **Colorectal cancer risk in cystic fibrosis: Systematic review and
  quantitative synthesis** — S. Sunkara, C. Dasari — *JCO* 2026 (ASCO
  abstract e15639). Chenjie Zeng alert. CF disease thread + cancer
  surveillance — relevant if you're looking at CF longevity-related
  cancer outcomes. ASCO abstract caveat (no full paper yet).
- **Defining the Roles of SGLT2 Inhibitors and GLP-1 Receptor Agonists in
  the Management of CKD in Adults with T2D With or Without [comorbidity]**
  — Y. Handelsman, A.Y.Y. Cheng, G.P. Fadini et al. (Patrick Ryan alert,
  06-03.) Guideline / consensus piece. Useful as a citation in any
  GLP-1/SGLT2 + kidney work, but not a primary research paper.
- **Anti-inflammatory effects of GLP1-RA drugs** — L. Quintana, N. Tabaza,
  B. Kurt, F. Kahles — *JCEM*, 2026. (Christopher G. Chute citations
  alert.) Mechanism review; light on epi data but useful for biological
  rationale in your GLP-1 pharmacoepi intros.
- **Predicting risk of mental health deterioration using multimodal data
  from the UK Biobank** — S. Yang, X. Lv, B. Huang, S. Lin, H. Zhao —
  *Journal of Advanced Research*. (PheWAS keyword, 06-05.) UKB multimodal
  + PRS-based risk prediction. Borderline HIGH if you're moving into UKB
  multimodal precision-health prediction; otherwise METHODS-WATCH.
- **Associations between dietary micronutrient intake and serum urate
  concentrations are dependent on SLC2A9 polymorphism rs12498742: A UK
  Biobank cohort study** — P.R. Johnson et al. (UK Biobank keyword alert,
  06-05.) Classic G×E in UKB. Borderline; useful as a G×E template but
  the outcome (urate) isn't tracked.
- **Cardiovascular-liver-metabolic multimorbidity prospective UK Biobank
  cohort** — Q. He et al. (UK Biobank keyword alert, 06-04.) UKB
  multimorbidity. On-thread but the snippet emphasizes plasma biomarker
  indices rather than the multimorbidity-structure methods that interest
  you most.

---

## SKIP / noise (logged, no action)

- **`arxiv-digest` repo, 06-02 & 06-03:** zero relevant; 06-03 again
  logged 3/4 category fetch failures. No actionable papers from the
  pipeline this window (same as the previous two reports).
- **Citation churn:** Marinka Zitnik, Peter Szolovits, James Zou, Bert
  Vogelstein, Jay Shendure, Daniel Kastner, Mihaela van der Schaar,
  Vivek Natarajan — citations and "new related research" alerts continue
  to surface generic LLM / cross-lingual / CRISPR / single-cell papers
  that don't overlap with active threads. SKIP.
- **"Federated Learning in Multimodal Healthcare Diagnostics"** (Nemane
  et al.) — Pascal Brandt alert. Generic federated-ML review in a
  low-tier venue. SKIP.
- **"Federated Multimodal Learning for Predicting HIV Care Retention and
  Viral Suppression"** (Jones, Brivastava, Howard) — AoU keyword. AoU
  *citation*, not an AoU primary study; venue is unfamiliar. SKIP.
- **"Multi-Modal Foundation Models for Integrating Immune Gene Variation,
  Transcriptomics, and Clinical Phenotypes in Precision Medicine"** (A.
  Sood, *Bioinformatics Insights and Analytics*) — EHR FM keyword.
  Single-author review in low-tier venue. SKIP.
- **"Wearable-based Activity Phenotyping Across Congenital Heart Disease
  Severity"** (G. Sazo, dissertation) — AoU keyword. Wearables + CHD;
  off-thread. SKIP.
- **"Revisiting the modifiable areal unit problem in the era of exposome-
  wide association studies"** (Lewis et al.) — AoU keyword. Geospatial
  exposome methods; off-thread unless you're moving into spatial-
  epidemiology. SKIP.
- **"Stabilizing Recurrent Dynamics for Test-Time Scalable Latent
  Reasoning in Looped Language Models"** (Yang et al., arXiv) — Zitnik
  alert. Generic LLM-architecture paper. SKIP.
- **"Construction and application of a multimodal knowledge graph for
  machining deformation uncertainty analysis"** — non-biomedical KG; same
  noise pattern as the prior 3 weeks (keyword still needs biomedical
  co-occurrence — recommendation persists from the 06-01 report).
- **Plant / non-clinical papers**: "Highly Polygenic Control of
  Photosynthetic Responses to Nighttime Temperature" — Bastarache and
  Jian Yang alerts. Plant genetics — keyword leakage. SKIP.
- **"Falls and the global burden of hip fractures in elderly: an
  integrated analysis of mendelian randomization and the global burden of
  disease study"** — Mendelian-diseases keyword still catching MR papers
  (same fix recommendation as 06-01: add `-randomization`).
- **"Materials by machines: A review on intuition and knowledge-driven
  learning"** — Pritchard citations. Materials-science review;
  off-thread. SKIP.
- **"Integrating ontology and knowledge graphs for intelligent assessment
  and feedback in E-learning systems"** — Tiffany Callahan alert. KG in
  *e-learning*, not biomedical. SKIP.
- **Self-citation noise:** "Impact of patient-reported taxane-induced
  peripheral neuropathy on dose reductions … in Black women with breast
  cancer" (Ballinger et al.) — Chenjie Zeng alert, 06-03. This is the
  same self-citation feed pattern called out in the 06-01 report; logging
  without action.

---

## Suggestions for the pipeline (carrying forward + adding)

Most of these are repeats; the persistence is the signal.

1. **`arxiv-digest` pipeline is now silent for 6+ days.** This is the
   third consecutive report flagging the same q-bio fetch failures and
   zero-result digests. Time to open an issue in the repo and either
   patch the fetcher's retry logic or migrate to a broader source list
   (cs.LG + stat.ME + medRxiv + bioRxiv as the prior reports recommended).
2. **Add `proteome-wide` / `colocalization` / `drug target` keywords.**
   Five+ proteome-MR / multi-omics-MR-for-drug-target papers in the last
   three reports; clearly a recurring valuable shape.
3. **Add a `pLoF` / `loss-of-function` keyword.** The Norton commentary
   (#11 above) is the *third* high-relevance pLoF/penetrance item in
   recent reports and your current keyword set probably picks them up
   only via author alerts.
4. **Tighten `mendelian diseases` keyword.** Still catching MR papers
   (third report flagging this) — add `-randomization`.
5. **`knowledge graph` keyword remains noisy** (4th consecutive report) —
   require biomedical co-occurrence (`biomedical knowledge graph` /
   `clinical knowledge graph`).
6. **`apol1` word-boundary anchoring** — recurring `APOE` false-positive
   pattern. (Same fix as 06-01.)
7. **Self-citations:** Chenjie Zeng author-feed continues to surface your
   own work (Ballinger et al. this window, Yang et al. ASCO last week).
   Add `-author:zeng` if it gets noisy or keep as citation-tracking.
8. **CFTR / drug-repurposing intersection:** The GLPG2737 ADPKD paper
   (#5) is exactly the kind of cross-disease CFTR use you'd want to
   surface reliably. Consider adding `CFTR inhibitor` as a separate term
   from `CFTR modulator` so repurposing-direction items don't get lost
   in the modulator pharmacoepi noise.
