# Research digest report — 2026-07-07

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-07** (since the prior 2026-06-20 report;
this covers 17 days of alerts and 15 daily `arxiv-digest` runs).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 06-21 → 07-07 | Two large batches this triage: **07-06 22:10Z** (≈25 author/citation feeds fired simultaneously — Chenjie Zeng self-feed, Bastarache, Karczewski, Denny, Hripcsak, Yang, Pritchard, Montgomery, Szolovits, Callahan, Zitnik, Vogelstein, Luo, Chute, Patrick Ryan, James Zou); **07-07 11:12Z** (keyword feeds — knowledge graph, rare diseases, foundation-models + EHR, All of Us). |
| `arxiv-digest` repo (`digests/`) | 06-22 → 07-06 | **07-02 = 1 paper** (Airbnb pricing causal-inference — off-thread), **07-03 = 1 paper** (3D plant phenotyping 3D-FM — off-thread), **07-04 / 07-05 / 07-06 = 0 papers each.** Six consecutive days of empty/leaked output — see pipeline note below. |
| Journal ToCs (JAMA new-issue emails) | 07-07 | JAMA July 2026 issue notification; not individually triaged (nothing on tracked pharmacoepi drug classes surfaced by keyword this window). |

> ⚠️ **`arxiv-digest` produced zero on-thread output across 15 daily
> runs in this window.** Two runs surfaced a single off-thread paper via
> a single-keyword leak (`causal inference` → Airbnb pricing;
> `foundation model` → 3D plant reconstruction). Every on-thread signal
> below came through Scholar alerts. The pipeline's `--min-score 2`
> default suppressed nothing on-thread here — the arXiv q-bio.QM /
> q-bio.GN / q-bio.PE / stat.AP feeds simply had no papers matching
> two-or-more of the tracked keywords in the lookback window. This is
> the **6-consecutive-day-empty pattern** flagged in every recent
> report; the fix (add `cs.LG`, `stat.ME`, `q-bio.OT`, and
> medRxiv/bioRxiv subject feeds) remains unaddressed. All 13 HIGH
> papers below appeared in journal venues (Nature Genetics, JAHA, npj
> Genomic Medicine, Nature Machine Intelligence, ERJ, AJHG) or on
> medRxiv/bioRxiv — none reachable by the current pipeline.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. Reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **A methods-paper landmark hits your PRS thread: MIXPRS (Nature
  Genetics).** Xu, Dong, X. Zeng, Bian, Zhou, Guan, Zhao et al. —
  *MIXPRS enables multi-population and multi-method polygenic risk
  scores using summary statistics* (**Nature Genetics**, 2026, *Jian
  Yang related-research* feed). The framing —"Many multi-population PRS
  methods have been proposed to improve prediction in underrepresented
  populations; however, no single method performs best across all
  scenarios. Although integrating PRSs across multiple [methods] …" —
  is directly on your **cross/trans-ancestry PRS portability** thread
  and the **PRS+method-stability** sub-thread that emerged from the
  06-18 and 06-20 reports (Ferreira across-version, de La Harpe
  across-method, Souaiaia across-distribution-region). MIXPRS makes
  those tension points *actionable*: rather than picking one method,
  ensemble across them under a summary-statistics-only constraint.
  **HIGH — likely the default 2026 H2 citation for multi-population
  ensemble PRS.**
- **Two more triple-signal PRS-methodology papers land the same day
  (both medRxiv, both cross-cited across Yang + Denny feeds).**
  (a) Mas Montserrat, Barrabes, Bustamante et al. — *Non-Parametric
  Ancestry Adjustment for Polygenic Scores* (medRxiv 2026.06.07). PC-
  free / non-parametric correction of the ancestry shift in PRS
  distributions — an alternative to the PC-regression standard.
  (b) Chen, X. Li, Mazumder, H. Zhang, X. Lin — *STELLAR: A flexible
  ensemble learning framework integrating rare variants to enhance
  polygenic risk prediction* (medRxiv 2026.06.07). Composite scoring
  that stacks **rare-variant burden with PRS** — the exact
  "PRS+rare-variant composite risk" thread called out in your
  INTERESTS file. The Bustamante and X. Lin (Harvard) authorships
  place both papers in the reference class. **HIGH — read paired with
  MIXPRS.**
- **A GLP-1 RA target trial emulation with an autoimmune-disease
  twist (JAHA).** Dai, Y.A. Lee, Natalie, W. Jackson, A. Pham, J.
  Levine et al. — *Glucagon-Like Peptide-1 Receptor Agonists and
  Cardiovascular Events in Adults With Obesity and Autoimmune
  Disease: A Target Trial Emulation* (*Journal of the American Heart
  Association*, 2026, *Patrick Ryan related-research* feed). Hits
  **three** of your active threads in one paper — target trial
  emulation, GLP-1 RA drug-class thread, and the autoimmune-disease
  adjunct (IBD sub-thread). Standard TTE-in-EHR template applied to
  a specialized sub-population (autoimmune + obesity) where the
  MACE/VTE risk baseline is elevated relative to general obesity
  cohorts. **HIGH — read for the template, log for the drug-class
  effect estimate.**
- **First on-thread AoU HBOC-screening-disparities paper in the
  triage.** Yerukala Sathipati & Scott — *Documented clinical genetic
  testing among carriers of hereditary breast and ovarian cancer
  variants: Ancestry and socioeconomic disparities in the All of Us
  research program* (medRxiv 2026.06.09, *Joshua Denny related-
  research* feed). A biobank-scale question of how many HBOC carriers
  in AoU were **actually flagged clinically** — and how that varies by
  ancestry / SES. Directly on **AoU-EHR-linked biobank + variant
  interpretation + population-screening penetrance** thread. **HIGH.**
- **Nature Machine Intelligence: DeepEvidence, a multi-agent deep-
  research agent for biomedical evidence synthesis.** Z. Wang, Z. Chen,
  Z. Yang, X. Wang, Q. Jin, Y. Peng, Z. Lu et al. — *Empowering
  biomedical evidence exploration and synthesis with deep knowledge
  graph research* (**Nature Machine Intelligence**, 2026, *Christopher
  Chute citations* feed). Multi-agent LLM system doing breadth-first +
  depth-first traversal over biomedical KGs for evidence synthesis;
  cites the Human Phenotype Ontology (Chute lineage). Directly on
  **biomedical KG + LLM-agent + drug-repurposing/rare-disease
  reasoning** threads. NIH-Zong Lu group authorship (BEST Fellow
  lineage). **HIGH — 2026 H2 default citation for LLM-agent-over-
  biomedical-KG.**
- **Real-world Ivacaftor developmental gains (lung + height) — ERJ.**
  Guimbellot, Baker, Chalamalla, N.R. Rose et al. — *Unlocking growth
  potential: Ivacaftor therapy and developmental gains in lung and
  height in a cohort study of children and young adults with cystic
  fibrosis* (**European Respiratory Journal**, 2026, *Patrick Ryan
  related-research* feed). Directly on your **CFTR modulator + real-
  world outcomes** sub-thread. Guimbellot is the CF real-world-
  outcomes reference author. **HIGH.**
- **Cross-ancestry proteome-wide association (medRxiv, Karczewski
  citations).** Krueger, Fischer, Rizwan, Kumar et al. — *Multi-
  ancestry modeling improves fine-mapping resolution, protein
  prediction, and discovery for proteome-wide association studies*
  (medRxiv 2026.06.29, *Konrad Karczewski citations* feed). Cross-
  ancestry PWAS methodology — cis+trans-pQTL modeling in ancestrally
  diverse populations to improve protein prediction outside European
  cohorts. On **cross-ancestry portability + composite-PRS-plus-omics**
  thread. **HIGH.**
- **Rare-variant burden in tails of polygenic distributions (AJHG,
  Montgomery feed).** Baya, Lassen, B. Hill, Venkatesh, Currant et al.
  — *Individuals who deviate from polygenic expectation are enriched
  for damaging variants in genes linked to rare disease* (**American
  Journal of Human Genetics**, 2026, *Stephen Montgomery related-
  research* feed). Follow-on to Souaiaia et al. (Nature) from the 06-20
  report: extreme deviation from expected polygenic score is
  **enriched for damaging rare variants**. Empirical validation of the
  composite-risk (PRS + rare-variant burden) case. **HIGH — pair with
  Souaiaia (06-20) and STELLAR (above).**
- **Your own self-feed fires on a CGRP-mAb migraine safety TTE.** Gül,
  Ong, Trudeau, N. Thompson, H. Yuan et al. — *Cerebrovascular risk
  with calcitonin gene-related peptide monoclonal antibodies versus
  onabotulinumtoxinA in patients with migraine: A real-world …*
  (*Chenjie Zeng — new related research* self-feed). Self-feed hit,
  which is one tier below the citation feed but still high-precision
  triage signal. Not on a tracked drug-class thread, but the design
  pattern (real-world head-to-head comparison with a lower-risk active
  comparator to reduce confounding-by-indication) is the same TTE
  template you publish in. **HIGH-self-feed, METHODS-WATCH for the
  drug class.**
- **Self-supervised EHR foundation model targeting downstream clinical
  discriminability.** E. Carter, O. Bennett, N. Sullivan, S. Lowe et
  al. — *Self-Supervised Learning for Future Clinical Discriminability
  in Electronic Health Records* (foundation-models + EHR keyword feed,
  07-07). Directly on the **CLMBR / MOTOR / MEDS lineage** — the
  paper's title framing ("future clinical discriminability") suggests
  a pretraining objective explicitly tuned for downstream *prediction*
  rather than generic language-model perplexity, which is the gap
  between CLMBR-style and the newer MOTOR-style objectives. **HIGH on
  EHR-FM thread.**
- **Targeted reflex RNA sequencing for VUS on exome/genome — npj
  Genomic Medicine.** X. Zhao, Rigobello, Driver, S. Lau, M.L. Chong
  et al. — *Targeted reflex RNA sequencing for enhanced variant
  classification on exome and genome sequencing improves patient
  outcomes* (**npj Genomic Medicine**, 2026, *Konrad Karczewski
  related-research* feed). Reflex RNA-seq to resolve DNA-level
  splicing/expression VUS at the point of clinical reporting — exactly
  on the **ACMG/ClinGen splicing / RNA evidence** sub-thread called
  out in your INTERESTS. Karczewski feed → likely uses LOFTEE-style
  pLoF baselines. **HIGH.**
- **KG for cardiovascular drug safety / pharmacovigilance — scoping
  review.** Jafarpour, Rad, Esmaeili, Bitaraf — *Knowledge Graph for
  Cardiovascular Drug Safety and Pharmacovigilance: A Scoping Review*
  (2026, *Christopher Chute citations* feed). PRISMA-ScR scoping over
  KG-in-pharmacovigilance methods for cardiovascular ADRs. Directly on
  the **biomedical KG + drug repurposing / pharmacovigilance** axis.
  Useful landscape citation. **HIGH on KG-pharmacoepi thread.**
- **Ancestry-diverse T2D eQTL colocalization in TOPMed WGS.** N. Wang,
  DiCorpo, Y. Zhang, Kleinbrink, Arnett et al. — *Colocalization of
  eQTLs With Type 2 Diabetes and Glycemic Traits Using Whole-Genome
  Sequences in Diverse Populations From the NHLBI Trans-Omics in
  Precision Medicine (TOPMed) Program* (**Diabetes**, 2026, *Patrick
  Ryan related-research* feed via Yang). Ancestry-diverse WGS-based
  eQTL / T2D colocalization — cross-ancestry variant-to-mechanism
  work. **HIGH on trans-ancestry + variant interpretation** if T2D
  is a background phenotype for the AoU work; else **METHODS-WATCH**.

Counts: **13 HIGH**, **5 METHODS-WATCH**, rest SKIP. Compared to the
06-20 report (6 HIGH), the higher HIGH count reflects the wider 17-day
window (vs. one-day). The recurring pattern remains: **all on-thread
signal comes from Scholar alerts; `arxiv-digest` produced zero on-
thread papers over 15 daily runs.**

---

## HIGH priority — detailed reports

### 1. MIXPRS enables multi-population and multi-method polygenic risk scores using summary statistics
- **Authors / venue:** L. Xu, Y. Dong, X. Zeng, Z. Bian, G. Zhou, L. Guan, H. Zhao — **Nature Genetics**, 2026. URL: nature.com/articles/s41588-026-02637-4.
- **Surfaced by:** *Jian Yang — new related research* feed. Note the H. Zhao (Yale) and Y. Dong / L. Xu authorship — this is the Yale statistical-genetics group's ensemble-PRS entry, sitting alongside PRS-CSx, MUSSEL, and PRS-Mixer as the multi-population reference methods.
- **Thread:** **Genetic epidemiology / PRS** (multi-population + multi-method ensemble) **+** cross/trans-ancestry portability.
- **What it is:** From the framing: "Many multi-population polygenic risk score (PRS) methods have been proposed to improve prediction in underrepresented populations; however, no single method performs best across all scenarios. Although integrating PRSs across multiple [methods] …". The gap MIXPRS closes is method-selection instability: PRS-CSx wins on some ancestry/trait combinations, MUSSEL on others, and a practitioner has no principled way to pick before genotype-lookup. MIXPRS treats method-selection as an ensemble problem solvable **from summary statistics alone** — no individual-level tuning cohort required. Nature Genetics-tier means the empirical evaluation is broad (multiple traits × multiple ancestries × multiple methods).
- **Why it matters to you:** Four converging hits.
  (a) **The exact PRS-stability sub-thread that emerged from the last three reports.** Ferreira et al. (across-version), de La Harpe et al. (across-method), Souaiaia et al. (across-distribution-region). MIXPRS makes the *across-method* leg actionable — you don't pick one, you ensemble.
  (b) **The summary-statistics-only constraint matches the AoU / UKB / MVP data-access model.** Individual-level tuning-cohort access requires enclave compute and per-cohort DUAs; summary-stats ensembling can be done outside the enclave once genotype-level scores are computed inside.
  (c) **Multi-population by design.** Your INTERESTS file explicitly lists cross/trans-ancestry portability. MIXPRS is designed *for* the underrepresented-population regime rather than benchmarked *on* it as an afterthought.
  (d) **Nature Genetics venue = default citation.** For any downstream PRS write-up in 2026 H2, this is the ensembling baseline you'll need to cite (and probably compare against).
- **Action:** **HIGH — read first.**
  (i) Read for the ensembling scheme: convex combination with per-trait weights? Bayesian model averaging with method-effective-sample-size prior? Stacking with a held-out proxy target?
  (ii) Note the empirical evaluation — which trait × ancestry combinations? UKB Non-European sub-cohorts, PAGE, BBJ, TWB, MVP? The evaluation panel bounds the transferability claim.
  (iii) Check whether they release code + summary-statistic pre-processed inputs, and how large the memory / compute footprint is on a per-trait basis.
  (iv) Compare implicit / explicit assumptions against MUSSEL and PRS-CSx — is MIXPRS strictly a super-class, or does it depend on a subset that dominates?
  (v) For your composite-PRS-plus-rare-variant work: MIXPRS gives you the PRS layer; STELLAR (below) gives you the rare-variant layer — the two compose.

### 2. STELLAR: A flexible ensemble learning framework integrating rare variants to enhance polygenic risk prediction
- **Authors / venue:** T. Chen, X. Li, R. Mazumder, H. Zhang, X. Lin — medRxiv 2026.06.07 (Harvard Biostat lineage, Xihong Lin group).
- **Surfaced by:** *Jian Yang — new related research* feed.
- **Thread:** **Genetic epidemiology / PRS** (composite risk with rare variants) **+** **Variant interpretation** (rare-variant burden used as predictor).
- **What it is:** Ensemble framework that combines **common-variant PRS + rare-variant burden scores** into one predictor of disease risk. Framing: "existing statistical methods used for rare variant association testing are not [designed for] prediction." STELLAR's move is to treat rare-variant testing outputs (SKAT / burden test statistics) as *features* in an ensemble alongside a standard PRS. Xihong Lin group work — reference-class for this design pattern.
- **Why it matters to you:** Three reasons.
  (a) **Your INTERESTS file explicitly names "composite risk models stacking PRS with rare pathogenic variants."** STELLAR is a direct methods-paper for that pattern.
  (b) **Pairs with the tails work (Souaiaia 06-20; Baya et al. HIGH #6 below).** If tails of polygenic distributions are enriched for damaging rare variants, then STELLAR-style composite scoring is *how* you actually operationalize the finding rather than just reporting it.
  (c) **Xihong Lin's group is the reference for rare-variant statistical methods.** Any composite-risk write-up you produce will need to either compare against STELLAR or explicitly justify not using it.
- **Action:** **HIGH.**
  (i) Read for the composition rule — linear stacking, gradient boosting over PRS+burden as features, or a Bayesian latent-risk model?
  (ii) Note the rare-variant unit — gene, sliding-window, functional annotation-weighted?
  (iii) Check the empirical panel — UKB WES + WGS? Genes-first analyses on specific diseases? Cardiometabolic focus (which would be on-thread for the AoU work)?
  (iv) Compare against Bomba-style FGR or the composite-risk designs cited in AoU papers.

### 3. Non-Parametric Ancestry Adjustment for Polygenic Scores
- **Authors / venue:** D. Mas Montserrat, M. Barrabes, C.D. Bustamante et al. — medRxiv 2026.06.07.
- **Surfaced by:** **Cross-feed** — both *Jian Yang* AND *Joshua Denny* related-research feeds; Bustamante-authorship signals the Stanford / Galatea-Bio lineage.
- **Thread:** **Genetic epidemiology / PRS** (PC-free ancestry adjustment) **+** cross-ancestry portability.
- **What it is:** From framing: "Modern polygenic risk scores (PRS) exhibit shifts correlated with ancestry, leading to erroneous predictions for non-European individuals when models are trained on predominantly European cohorts." The standard fix is PC-regression against genomic PCs. The paper proposes a **non-parametric** correction, likely quantile / rank-based, that doesn't assume linear PC dependence. Bustamante-group work.
- **Why it matters to you:** Three reasons.
  (a) **PC-regression breaks in admixed and non-Europe-adjacent populations.** AoU has a genuinely admixed cohort, and standard PC-regression under- or over-corrects depending on the trait. A non-parametric alternative is directly usable.
  (b) **Cross-fires in Yang + Denny feeds.** Denny fires on AoU-relevant work; Yang fires on general PRS methodology. Both firing simultaneously means it hits the AoU-PRS intersection.
  (c) **Pairs with MIXPRS.** MIXPRS ensembles across methods but assumes each method's PRS is already ancestry-adjusted. Mas Montserrat gives the ancestry-adjustment step; MIXPRS gives the ensemble. Compose them.
- **Action:** **HIGH.**
  (i) Read for the non-parametric mechanism — CDF-matching by genomic-PC-neighborhood, kernel density estimation, quantile regression forests?
  (ii) Note the evaluation cohort — UKB Africa/South Asia subgroups, PAGE, AoU, or all three?
  (iii) Check whether the adjustment is per-trait or trait-agnostic. Trait-agnostic adjustment is much more deployable in a biobank pipeline.

### 4. Glucagon-Like Peptide-1 Receptor Agonists and Cardiovascular Events in Adults With Obesity and Autoimmune Disease: A Target Trial Emulation
- **Authors / venue:** H. Dai, Y.A. Lee, A. Natalie, W. Jackson, A. Pham, J. Levine et al. — **Journal of the American Heart Association**, 2026. URL: ahajournals.org/doi/pdf/10.1161/JAHA.125.047893.
- **Surfaced by:** *Patrick Ryan — new related research* feed.
- **Thread:** **Causal inference / pharmacoepi** (TTE template) **+** **GLP-1 RA drug-class thread** **+** autoimmune-disease adjunct (IBD sub-thread).
- **What it is:** Target trial emulation of GLP-1 RA vs. non-user in adults with obesity **and** an autoimmune disease (likely RA / psoriasis / IBD / SLE — the exact AID panel is the paper's design choice). Framing: "Obesity and autoimmune diseases (AIDs) are each associated with elevated risk of cardiovascular and thromboembolic events. Glucagon-like peptide-1 receptor agonists (GLP-1RAs) have demonstrated cardiovascular and metabolic …". The TTE motivation is the standard one: RCTs of GLP-1 RA in obesity underrepresent autoimmune-disease patients, so a real-world TTE fills that evidence gap. JAHA venue means the primary outcome is likely MACE composite.
- **Why it matters to you:** Three reasons.
  (a) **Hits three of your threads simultaneously** (TTE + GLP-1 + autoimmune/IBD). The IBD sub-thread has been active in your INTERESTS list; this is the first paper this year that lands there via the pharmacoepi angle.
  (b) **Standard reference-class TTE.** For any future GLP-1 / SGLT2 TTE writing you do (AoU or MVP), this is a template to lift from — inclusion / exclusion, active comparator choice, IPW spec, sensitivity analyses.
  (c) **Patrick Ryan feed firing on a JAHA TTE** is signal that OHDSI-adjacent adopters view this as reference-class; likely uses OMOP CDM under the hood.
- **Action:** **HIGH.**
  (i) Identify the AID panel — RA / IBD / psoriasis / SLE. If IBD is included, note the effect estimate specifically.
  (ii) Note the active comparator — non-GLP-1 obesity drug (naltrexone-bupropion, phentermine-topiramate), SGLT2i, or "no obesity pharmacotherapy"? Choice bounds confounding-by-indication.
  (iii) Check the CDM / data source — is it Merative MarketScan, PharMetrics, or a UK EHR (CPRD)? US-payer vs. UK-NHS drives generalizability.
  (iv) Check outcome definition — MACE composite, MACE+ (with heart failure hospitalization), or TE separately?
  (v) Log as a template for the AoU MVP GLP-1 write-up.

### 5. Documented clinical genetic testing among carriers of hereditary breast and ovarian cancer variants: Ancestry and socioeconomic disparities in the All of Us research program
- **Authors / venue:** S. Yerukala Sathipati, H. Scott — medRxiv 2026.06.09.
- **Surfaced by:** *Joshua C. Denny — new related research* feed. Denny is the AoU CEO / Chief Medical Officer — his related-research feed firing on an AoU disparities paper is high-signal.
- **Thread:** **Biobanks with EHR linkage** (AoU) **+** **Variant interpretation** (HBOC = BRCA1/2/PALB2/ATM/CHEK2/RAD51C/D) **+** rare-disease / cancer genetics disparities.
- **What it is:** Framing: "Importance: Hereditary breast and ovarian cancer (HBOC) variant carriers benefit from risk-reducing interventions, but only if identified. The extent to which carriers are clinically recognized, and whether recognition is equitable across diverse …". Study operationally answers: among AoU participants whose genomic data reveals an HBOC pathogenic variant, **what fraction have any evidence of clinical genetic testing in their EHR** — and how does that fraction vary by ancestry / SES / geography? The answer is the population-screening penetrance-vs-clinical-ascertainment question your INTERESTS file explicitly names.
- **Why it matters to you:** Four reasons.
  (a) **Directly on the penetrance-under-population-screening thread.** Population-based ascertainment of pathogenic variants yields lower observed penetrance than clinically-ascertained cohorts partly because population-based carriers don't receive risk-reducing interventions. This paper *measures the size of the intervention gap* rather than assuming it away.
  (b) **AoU + EHR-linked disparities.** AoU's design intent is to enroll underrepresented populations. This paper is a first-cut audit of whether that design intent translates to *equitable clinical genetic recognition* — the outcome you actually care about for screening policy.
  (c) **Denny feed firing = AoU leadership treats this as reference-class.** Feed hits on Denny's related-research are the strongest signal in your Scholar-alert panel for "does the AoU leadership consider this important."
  (d) **Standard evidence for any downstream advocacy write-up.** If you argue for population-based screening for HBOC (or for CFTR-carrier screening, APOL1 screening, etc.), this paper is the template for the "who is being missed" measurement.
- **Action:** **HIGH.**
  (i) Read for the identification method of "documented clinical genetic testing" — CPT codes, procedure text NLP, or self-report? Each has known false-negative rates.
  (ii) Note the ancestry / SES / geography stratification granularity — census-tract SES linkage or self-report?
  (iii) Check whether they extended to *risk-reducing intervention receipt* (bilateral mastectomy, oophorectomy, tamoxifen), or stopped at genetic testing.
  (iv) Consider as a template for parallel analyses of ATM / CHEK2 / cystic-fibrosis / APOL1 population-based-carrier ascertainment.

### 6. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
- **Authors / venue:** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh, H. Currant et al. — **American Journal of Human Genetics**, 2026.
- **Surfaced by:** *Stephen B. Montgomery — new related research* feed.
- **Thread:** **Genetic epidemiology / PRS** (tails of PRS distribution) **+** **Variant interpretation** (rare-variant enrichment in tail deviants) **+** **Rare disease** (rare-disease-linked gene enrichment).
- **What it is:** The complementary empirical result to Souaiaia et al. (Nature, 06-20 report). If Souaiaia showed "the tails of complex traits have distinct genetic architecture," Baya et al. show "the individuals whose observed phenotype deviates from what the PRS predicts are enriched for damaging variants in rare-disease genes." Operationally: filter the biobank cohort to individuals whose observed trait diverges from PRS prediction (positive or negative residual), then look for over-representation of pLoF / ClinVar-pathogenic / high-CADD variants in Mendelian-disease genes.
- **Why it matters to you:** Three reasons.
  (a) **Direct empirical warrant for composite PRS + rare-variant scoring.** The Souaiaia finding was theoretical (tails have distinct architecture); Baya validates the *actionable* form (residuals identify carriers of damaging variants). This is now the empirical case for STELLAR-style scoring.
  (b) **Bridges polygenic and Mendelian frames.** Your INTERESTS file has both — this paper is the connective tissue between "PRS" and "rare-disease diagnosis" threads.
  (c) **Cheap-to-run diagnostic pattern.** If you have PRS + WES for the same cohort (AoU / UKB), computing residuals and looking for rare-variant enrichment is a nearly free additional analysis on any complex-trait study you're doing.
- **Action:** **HIGH.**
  (i) Read for the residual definition — z-score of observed phenotype minus PRS-predicted, per-decile stratification, or full quantile regression?
  (ii) Note the traits examined — height, BMI, LDL, and blood counts are the standard set; anything with clinical actionability (LDL → statin) is more useful for downstream policy.
  (iii) Check whether the pLoF enrichment is specific to *known* Mendelian-disease genes for that phenotype (LDLR for LDL) or is broadly diffuse.
  (iv) Consider proposing as a validation analysis for your AoU work.

### 7. Empowering biomedical evidence exploration and synthesis with deep knowledge graph research (DeepEvidence)
- **Authors / venue:** Z. Wang, Z. Chen, Z. Yang, X. Wang, Q. Jin, Y. Peng, Z. Lu et al. — **Nature Machine Intelligence**, 2026. URL: nature.com/articles/s42256-026-01266-0.
- **Surfaced by:** *Christopher G. Chute citations* feed (cites HPO). NIH / Zhiyong Lu group authorship.
- **Thread:** **Knowledge graphs & ontologies** (biomedical KG traversal) **+** **Drug repurposing** (explainable KG paths) **+** LLM-agent for clinical reasoning.
- **What it is:** Framing: "DeepEvidence, a deep research agent for evidence exploration and synthesis across heterogeneous biomedical knowledge sources. DeepEvidence advances deep research through coordinated multi-agent collaboration combining breadth-first and depth-first research strategies to search …". Multi-agent LLM system that dispatches sub-agents in parallel over biomedical KGs + literature + structured resources, with an explicit BFS/DFS traversal split so breadth-agent finds candidate hypothesis edges and depth-agent verifies them via citation trails. Cites HPO (Chute lineage) as one of the KGs it consumes.
- **Why it matters to you:** Three reasons.
  (a) **Directly on the drug-repurposing thread's "explainable KG-path hypothesis output" preference** in your INTERESTS file. DeepEvidence outputs *rationales* (BFS-DFS traversal paths) rather than opaque link-prediction scores.
  (b) **HPO integration = rare-disease phenotype-matching hook.** Your INTERESTS file explicitly names HPO-based phenotype matching for rare-disease drug repurposing; this paper is a substrate for that.
  (c) **Nature Machine Intelligence + Zhiyong Lu group** = 2026 H2 default citation for "LLM-agent over biomedical KG."
- **Action:** **HIGH.**
  (i) Read for the KG panel — is it PrimeKG, SPOKE, iBKH, DrugBank, or a custom aggregation? The KG choice bounds the reasoning scope.
  (ii) Note the evaluation task — clinical QA, drug repurposing benchmark (DRKG), or open-ended literature synthesis?
  (iii) Check whether the multi-agent design has any *cost* discipline (call budget, retrieval budget), or if it's unconstrained. Unconstrained agents are hard to reproduce and hard to deploy.
  (iv) Consider as a substrate for your rare-disease drug-repurposing work — the BFS-DFS traversal pattern is directly reusable.

### 8. Unlocking growth potential: Ivacaftor therapy and developmental gains in lung and height in a cohort study of children and young adults with cystic fibrosis
- **Authors / venue:** J.S. Guimbellot, E. Baker, A. Chalamalla, N.R. Rose et al. — **European Respiratory Journal**, 2026.
- **Surfaced by:** *Patrick Ryan — new related research* feed.
- **Thread:** **CFTR / cystic fibrosis** (modulator real-world outcomes) **+** **Pharmacoepi** (long-term effectiveness) **+** **ML for precision health** (individual growth-trajectory prediction).
- **What it is:** Real-world cohort study of Ivacaftor initiators, measuring **linear growth (height) and pulmonary function (FEV1 / FEV1pp)** trajectories in children and young adults. Framing: "Cystic fibrosis (CF) is historically characterized by impaired lung function and stunted growth due to variants in Cystic Fibrosis Transmembrane conductance Regulator (CFTR). CFTR modulators, like ivacaftor, have revolutionized treatment …". Guimbellot is the CF real-world-outcomes reference author, and this is likely a CFF Patient Registry-derived analysis with careful growth-trajectory modeling (spline / mixed-effects).
- **Why it matters to you:** Three reasons.
  (a) **Directly on your CFTR modulator + real-world outcomes sub-thread.** Height gain is a clinically important secondary outcome that TRIKAFTA / ivacaftor RCTs didn't power for; real-world CFFPR data is the natural evidence source.
  (b) **Guimbellot authorship = reference-class.** Any downstream CF-modulator work you cite in a review or write about needs Guimbellot in the reference list.
  (c) **Pediatric focus adds developmental-window angle.** Growth-window sensitivity is the design pattern for early-vs-late modulator-initiation causal work.
- **Action:** **HIGH.**
  (i) Read for the cohort — CFFPR (US), UK CF Registry, EPCFR (European)?
  (ii) Note the Ivacaftor-eligible genotype panel — G551D-only or the broader gating-mutation set?
  (iii) Check the growth modeling — spline / GAMLSS / mixed-effects with random slopes?
  (iv) Compare implicit effect size against the ELX/TEZ/IVA growth findings (which have more coverage in eligible children).

### 9. Multi-ancestry modeling improves fine-mapping resolution, protein prediction, and discovery for proteome-wide association studies
- **Authors / venue:** C.J. Krueger, M. Fischer, T. Rizwan, M.M. Kumar et al. — medRxiv 2026.06.29.
- **Surfaced by:** *Konrad Karczewski citations* feed.
- **Thread:** **Genetic epidemiology / cross-ancestry** (multi-ancestry pQTL) **+** **Genetic epi + omics** (PWAS methodology) **+** composite-PRS-plus-omics.
- **What it is:** Framing: "Proteomic predictive models are predominantly trained on cis-acting variants in European-ancestry cohorts, limiting power and predictive accuracy in ancestrally diverse populations. We performed cis- and trans-protein quantitative trait locus …". Extends the standard European-trained pQTL model to jointly cis + trans + multi-ancestry, then propagates the improved predictor into PWAS discovery / fine-mapping. Companion paper to the plasma proteomic aging line (Ding et al., 06-20 report).
- **Why it matters to you:** Three reasons.
  (a) **Cross-ancestry PWAS is on-thread.** Your INTERESTS file specifies cross/trans-ancestry portability; extending it to *proteomic* predictors is the next step beyond PRS.
  (b) **UKB-PPP infrastructure adjacency.** If this paper uses UKB-PPP with African / South Asian sub-cohorts, the data primitives are directly reusable when comparable Olink data lands in AoU.
  (c) **Composite-PRS-plus-omics thread.** Pairs with Ding et al. (Nature Medicine plasma proteomic aging, 06-20) — Ding was European-cohort proteomic aging; Krueger extends the predictor to non-European.
- **Action:** **HIGH.**
  (i) Read for the training cohort — UKB-PPP, ARIC, JHS, or All of Us Olink pilot?
  (ii) Note the trans-pQTL modeling — MR-JTI-style, causal-cis + horizontal-pleiotropy correction, or plain ridge?
  (iii) Check downstream PWAS traits — cardiometabolic (T2D, CAD, LDL)? Aging phenotypes?

### 10. Self-Supervised Learning for Future Clinical Discriminability in Electronic Health Records
- **Authors / venue:** E. Carter, O. Bennett, N. Sullivan, S. Lowe et al. — foundation-models + EHR keyword feed, 07-07 (unclear venue from snippet; likely arXiv or NeurIPS-workshop-adjacent).
- **Surfaced by:** *Foundation models and "electronic health records"* keyword alert.
- **Thread:** **EHR foundation models** (CLMBR / MOTOR / MEDS lineage) **+** EHR phenotyping (downstream classification quality).
- **What it is:** Framing: "structure of downstream clinical decision making, we seek to …". The abstract snippet suggests a **pretraining objective explicitly targeting downstream clinical discriminability** — i.e., picking the SSL loss so that the resulting representation is maximally separable for clinical prediction tasks. This is the gap between CLMBR's plain masked-modeling and MOTOR's time-to-event contrastive objective; a "future-discriminability" framing points toward event-based losses.
- **Why it matters to you:** Three reasons.
  (a) **EHR-FM thread specifically named in your INTERESTS file** ("CLMBR, MOTOR, EHRSHOT, MedTok, FEMR, MEDS lineage").
  (b) **Objective-choice is where the field is currently disagreeing.** MOTOR moved past CLMBR-style masking; if this paper introduces a *discriminability-aware* SSL objective, it's a design proposal that either aligns with or competes with MOTOR.
  (c) **Downstream evaluation panel matters.** If they benchmark against EHRSHOT or MEDS-Tab, the paper is quickly reproducible; if not, it's harder to trust.
- **Action:** **HIGH.**
  (i) Locate the venue — abstract snippet suggests arXiv or NeurIPS 2026 workshop.
  (ii) Read for the SSL objective — future-event contrastive, InfoNCE with time-decay, or a supervised proxy target?
  (iii) Check baselines — CLMBR, MOTOR, MEDS-Tab required for credibility.
  (iv) Note the training corpus — Stanford (MOTOR heritage), MIMIC, or a hospital-specific corpus?

### 11. Targeted reflex RNA sequencing for enhanced variant classification on exome and genome sequencing improves patient outcomes
- **Authors / venue:** X. Zhao, R. Rigobello, M. Driver, S. Lau, M.L. Chong et al. — **npj Genomic Medicine**, 2026.
- **Surfaced by:** *Konrad Karczewski — new related research* feed.
- **Thread:** **Variant interpretation** (ACMG/ClinGen splicing / RNA evidence for VUS resolution) **+** clinical genomic reporting.
- **What it is:** Clinical service model — when exome/genome sequencing yields a variant of uncertain significance where the *type* of uncertainty is potentially splicing / expression, **reflex to targeted RNA sequencing** on the same sample, and use the RNA-level evidence (PS3 / PVS1 splicing / BP4) to re-classify the VUS. Framing "improves patient outcomes" suggests a downstream diagnostic-yield or actionability metric is measured.
- **Why it matters to you:** Three reasons.
  (a) **Directly on the ACMG splicing / RNA evidence sub-thread** in your INTERESTS file.
  (b) **Operational service-model paper.** Most splicing-evidence work is either computational (SpliceAI-only) or bespoke-research. This paper describes what a **clinical reflex workflow** looks like at scale — the design template for whether a program should adopt it.
  (c) **npj Genomic Medicine + Karczewski feed** = variant-interpretation reference-class.
- **Action:** **HIGH.**
  (i) Read for the reflex trigger criteria — SpliceAI ≥ 0.2? Any near-splice variant? Only exon/intron junction variants?
  (ii) Note the RNA panel — whole-transcriptome, targeted gene-panel, or MiSeq-based amplicon?
  (iii) Check the yield metric — % of VUS moved to LP/P, or % of P moved to LP-with-explicit-splicing-mechanism?

### 12. Knowledge Graph for Cardiovascular Drug Safety and Pharmacovigilance: A Scoping Review
- **Authors / venue:** M. Jafarpour, F.S. Rad, M. Esmaeili, E. Bitaraf — 2026 (scoping review; likely IEEE / Frontiers venue).
- **Surfaced by:** *Christopher Chute citations* feed.
- **Thread:** **Knowledge graphs & ontologies** (KG for PV) **+** **Causal inference / pharmacoepi** (pharmacovigilance) **+** biomedical KG + drug-repurposing tangent.
- **What it is:** PRISMA-ScR scoping review of KG applications for cardiovascular drug safety and pharmacovigilance. Framing lifts the standard scoping-review scope: methodologies, technologies, evidence gaps. Useful landscape citation.
- **Why it matters to you:** Two reasons.
  (a) **Landscape citation for the biomedical KG + pharmacovigilance intersection.** Neither exhaustive nor definitive, but useful as a first-cite when arguing why KG methods deserve attention in PV.
  (b) **Cardiovascular focus overlaps the GLP-1 / SGLT2 CV-outcomes work.** If a KG-based causal-inference angle enters the drug-class TTE thread, this is the review to point at.
- **Action:** **HIGH-secondary** (read the table of surveyed methods, skim the framework analysis).
  (i) Identify which KGs are most-cited — SPOKE, PrimeKG, DrugBank-derived, SemMedDB?
  (ii) Check which prediction / detection tasks dominate — ADR prediction, signal detection, drug-drug interaction?

### 13. Cerebrovascular risk with calcitonin gene-related peptide monoclonal antibodies versus onabotulinumtoxinA in patients with migraine: A real-world …
- **Authors / venue:** S. Gül, B. Ong, S. Trudeau, N. Thompson, H. Yuan et al. — 2026 (venue unclear from snippet).
- **Surfaced by:** *Chenjie Zeng — new related research* self-feed. Self-feed hits are one tier below citation-feed hits but still high-precision.
- **Thread:** **Causal inference / pharmacoepi** (real-world head-to-head TTE-adjacent).
- **What it is:** Real-world comparative safety study of CGRP monoclonal antibodies (erenumab / fremanezumab / galcanezumab / eptinezumab) vs. onabotulinumtoxinA in migraine patients, comparing **cerebrovascular event** rates. Not a tracked drug class in your INTERESTS file, but the design template — active-comparator RWE comparison with a lower-risk comparator to reduce confounding-by-indication — is the same TTE pattern you publish in.
- **Why it matters to you:** Two reasons.
  (a) **Self-feed hit.** Google judges this close enough to your published work to fire your own alert. Highest-precision channel available.
  (b) **Design template.** The "head-to-head active-comparator RWE" pattern is the modern TTE-in-EHR default; this paper is a compact template for adapting to any drug pair.
- **Action:** **HIGH (design-template read).**
  (i) Read for the propensity spec + comparator choice justification (why onabotA specifically?).
  (ii) Note the outcome definition — ICD-based stroke composite, TIA inclusion / exclusion, event-window?
  (iii) Log as a template for a comparable AoU-based analysis of any drug-pair where a lower-risk active comparator exists.

### 14. Colocalization of eQTLs With Type 2 Diabetes and Glycemic Traits Using Whole-Genome Sequences in Diverse Populations From the NHLBI Trans-Omics in Precision Medicine (TOPMed) Program
- **Authors / venue:** N. Wang, D.A. DiCorpo, Y. Zhang, E. Kleinbrink, D.K. Arnett et al. — **Diabetes** (ADA), 2026.
- **Surfaced by:** *Jian Yang — new related research* feed (also relevant to Patrick Ryan feed given T2D-outcomes overlap).
- **Thread:** **Genetic epidemiology / cross-ancestry** (multi-ancestry T2D eQTL) **+** variant interpretation (colocalization = variant-to-mechanism).
- **What it is:** Cross-ancestry eQTL / T2D colocalization analysis in TOPMed WGS, addressing the gap that most eQTL / T2D colocalization work is European-cohort only. Framing "imputed genotyping arrays limit the detection of low-frequency and rare variants" points to a WGS-based advantage — rare / low-frequency variants that arrays miss but WGS catches, and their downstream regulatory effects.
- **Why it matters to you:** Two reasons.
  (a) **Cross-ancestry + WGS + colocalization** — three of your INTERESTS-file threads composed in one paper.
  (b) **TOPMed is a natural comparator to AoU / MVP.** If AoU expands to WGS-level analyses of T2D, TOPMed is the reference comparator; understanding TOPMed's eQTL / T2D colocalization is directly relevant.
- **Action:** **HIGH.**
  (i) Read for the sample composition — TOPMed ancestry breakdown, sample-size per ancestry.
  (ii) Note the colocalization method — coloc, moloc, ecaviar, or a WGS-native version?
  (iii) Check whether any of the reported loci overlap AoU-observed loci from earlier reports.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **The Agentic Garden of Forking Paths** — J. Miao, J.K. Pritchard, J. Zou — *arXiv 2607.01507*, 2026 (dual feeds: **Jonathan Pritchard AND James Zou new-articles**). Analytical-multiverse / researcher-DoF paper — every analysis pipeline choice fans out into a "garden of forking paths," and the paper proposes an **agent-based framework** for surveying that garden systematically. Adjacent to statistical-integrity / robustness work. **METHODS-WATCH** for any biomarker-discovery or PheWAS write-up where analytical DoF is a referee concern. Pritchard+Zou co-firing is high-signal for computational statistical genetics.

- **Temporal Disease Trajectories Derived from EHR Data in Critical Care Patients** — Y. Zhang, A. Torralbo, N. Sebire, S. Denaxas — *Studies in Health Technology and Informatics*, 2026 (Patrick Ryan related-research feed). Denaxas group at UCL. 364,627-patient ICU cohort with trajectory extraction from longitudinal EHR. **METHODS-WATCH** for your multimorbidity / disease-trajectory thread — the design is directly on-pattern (temporal disease-code sequence clustering), the venue (SHTI) is thinner than a top journal but Denaxas group work is reliable.

- **Real-time prediction of rapid weight change in children with cystic fibrosis who have initiated modulator therapy** — A. Garter, E. Gecili, M.M. Hossain, A. Nakamura et al. — *Clinical Nutrition ESPEN*, 2026. ETI (elexacaftor/tezacaftor/ivacaftor) weight-trajectory prediction in pediatric CF. **METHODS-WATCH** for the CF thread (individual-trajectory prediction) — modest venue but relevant to any CF modulator write-up that touches nutritional outcomes.

- **Population pharmacokinetics and pharmacodynamics of canagliflozin in paediatric patients with type 2 diabetes mellitus** — N. Goeyvaerts, P.O. Gisleskog, M. Neyens, J.J.P. Ruixo — *British Journal of Clinical Pharmacology*, 2026 (Patrick Ryan feed). SGLT2i (canagliflozin) PK/PD in pediatric T2D. On the SGLT2 drug-class thread but not on your causal-inference angle — **METHODS-WATCH** if pediatric extrapolation of SGLT2 CV signals becomes a topic.

- **Genomic Dimensionality Bounds Mixed-Model Association Power, Fine-Mapping Resolution, and Genomic Prediction Reliability** — J. Jiang — *bioRxiv*, 2026 (Yang feed). Theoretical result on mixed-model GWAS power as a function of full-GRM dimensionality — the observation that livestock and human GWAS behave differently unified under a single dimensionality framework. **METHODS-WATCH** for any GWAS-methods write-up; livestock-vs-human framing is unusual.

- **Rare variants in genes related to inborn errors of immunity in patients with rheumatoid arthritis and secondary immunodeficiency** — F. Atschekzei, N. Dubrowinskaja, M. Anim, D. Steinemann et al. — *RMD Open*, 2026 (*Lisa Bastarache — new related research* feed). Rare-variant IEI genes in RA + secondary immunodeficiency. Bastarache-feed firing on a rare-variant IEI paper is signal that the phecode-adjacent immune-phenotype work has interest. **METHODS-WATCH.**

- **Computer-Interpretable Domain Knowledge for Drug-Induced Acute Kidney Injury: a Knowledge Graph Approach** — R. Vos, I. Vagliano, C. Boersma, F. van Harmelen — *Scientific Data*, 2026 (*Tiffany Callahan — new related research* feed). Drug-induced AKI KG for computable clinical knowledge. On the biomedical-KG + drug-outcomes intersection. **METHODS-WATCH** — nice reference for domain-KG construction pattern.

- **Transcending Genome-Wide Association Studies to Create Useful Multi-omic Views of Glaucoma** — K. Li, J.H. Kang, A.P. Khawaja, S. Jardines, J. Vergroesen et al. — *Progress in Retinal and Eye Research*, 2026 (Montgomery citations feed). Multi-omic (GWAS + eQTL + proteomic + methylation) view of glaucoma. Off your tracked disease list, but exemplar of "multi-omic view of a complex trait" that's likely to be the reference format going forward. **METHODS-WATCH.**

---

## SKIP / noise (logged, no action)

**Non-biomedical KG papers** (same 8th-consecutive-window `knowledge graph` keyword leak; recommend keyword tightening — see pipeline note):
- *TEOKGC: text embedding optimization for knowledge graph completion* — generic KG completion, not biomedical.
- *ISERA-KGC: Enhancing Knowledge Graph Completion with Interactive Semantic Enhancement* — same.
- *Parent-Seeding Pheromone-Guided Subgraph Extraction for Clinical QA over FHIR KGs* (Chute citations) — clinical-QA over FHIR but not on your methods threads.
- *Verifiable Knowledge Expansion through Retrieval-Grounded Formal Concept Analysis* (arXiv, Chute citations) — cites HPO but is a generic ontology-construction paper.

**PRS-in-psychiatric-outcomes papers** (Yang feed; off your disease threads):
- *Educational Attainment PGS and School Performance in Adolescents With Psychiatric Disorders (iPSYCH2015)* (Fanelli et al.) — off-thread despite the PRS methods.
- *Polygenic overlap and shared genomic loci between anorexia nervosa and cardiometabolic traits* (Lu et al.) — cardiometabolic overlap is on-adjacent but anorexia is off your disease threads.
- *The Distinct Role of Family History and PRS on Lithium Response in Bipolar Disorder* (Ercis et al.) — bipolar disorder off-thread.
- *Testing Cross-Phenotype Effects of Rare Variants in Longitudinal Studies* (Rudra et al. supplementary materials) — supplementary-only, log for later citation but no action.

**Off-thread pharmacoepi papers** (Patrick Ryan feed; not on tracked drug classes):
- *Comparative Effects of SGLT2i and GLP-1 RA on METS-IR and SPISE* (Voziki et al.) — small-N observational study on insulin-resistance surrogates; not tracked outcomes.
- *Can oral GLP-1 receptor agonists ACHIEVE the same as SGLT2 inhibitors?* (Heerspink & Smeijer, Lancet editorial) — editorial-tier.
- *Influence of correlated vaccination behaviors on COVID-19 vaccine effectiveness (VISION)* (Kautz et al.) — off-thread.
- *Adaptive Sequential Multiple Hypotheses Testing for Concomitant Vaccine Safety Surveillance* (Silva et al., Stats in Medicine) — statistical methods for vaccine safety surveillance; off-thread.
- *GLP-1 Drugs May Fight Addiction …* (Al-Aly popular-press-format) — non-primary-literature.

**Journal-issue / non-actionable notifications:**
- JAMA July 2026 New Issue emails (2 copies delivered) — no individual paper triage warranted from ToC-only.
- NCBI My-NCBI daily digests — aggregate, not individually triaged here.

**Foundation-model / LLM-benchmark leaks** (off-clinical):
- *Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation* (Zitnik feed) — discrete-diffusion LM methods, off clinical/EHR thread.
- *Position: The Open Benchmark Paradox …* (Chute citations) — medical LLM eval position piece; interesting but not a research paper.

**Molecular / mechanism-only papers** (Vogelstein, Baker, Chute, Callahan citation leaks):
- *The future of blood-based biomarkers in liver cancer* (Singal et al., Vogelstein citations) — review, off-thread.
- *Mass-standardised antibody / SARS-CoV-2 endotypes* (Chute citations) — off-thread.
- *Association Between FOXE1 Gene Polymorphism and Subclinical Hypothyroidism* (Chute citations) — small-N Egyptian case-control, off-thread.

**Off-thread AoU / biobank leaks:**
- *Determinants of Food Insecurity and Its Association with BMI in Spinal Cord Injury (AoU)* — AoU thread but off your disease/methods threads.
- *Misaligned Expectations: Motivations of Medically Underserved People to Enroll in AoU* (Hripcsak citations) — ethics/enrollment framing, not methods.
- *Biobank innovation consortium for mental, intellectual and neurodevelopmental disorders study: BICMINDS* (Denny feed) — biobank-infrastructure paper; log the existence of BICMINDS but no methods bearing here.
- *Targeted Next-Generation Sequencing for Rare Diseases in Global South (protocol)* — protocol paper.
- *Integrating diversity, equity, and inclusion in generative AI applications for healthcare education* (Szolovits citations) — scoping review, off-methods.
- *arxiv-digest 07-02 Airbnb causal-inference paper* — single-keyword leak.
- *arxiv-digest 07-03 3D plant phenotyping 3DFM paper* — single-keyword leak.

---

## Suggestions for the pipeline

Prior reports' recommendations remain unactioned. Today's items add
one new issue and refresh two carry-forwards:

1. **6-consecutive-day-empty `arxiv-digest` output (07-01 → 07-06,
   excluding two single-keyword-leak days).** No on-thread paper
   surfaced from any of the 15 daily runs in this window. Every HIGH
   paper below was in a journal venue or medRxiv/bioRxiv — none in
   q-bio.QM / q-bio.GN / q-bio.PE / stat.AP. The fix (add `cs.LG`,
   `stat.ME`, `q-bio.OT`, medRxiv, bioRxiv subject feeds) is
   **carry-forward, 8th consecutive report unaddressed**. This is now
   the single highest-leverage change to the pipeline.

2. **`knowledge graph` keyword: 8th consecutive window of non-
   biomedical hits.** Today's non-biomedical leaks: TEOKGC, ISERA-KGC,
   FHIR-QA pheromone-guided subgraph, Verifiable Knowledge Expansion.
   Same fix as last report: change to `biomedical knowledge graph` OR
   `clinical knowledge graph` OR compound filter `(knowledge graph)
   AND (medical OR biomedical OR clinical OR EHR OR phenotype OR drug
   OR disease)`. The single highest-value KG paper this window
   (DeepEvidence) came via Chute-citations feed, not keyword, so
   tightening loses nothing.

3. **Add PRS-stability / composite-risk-scoring keywords.**
   Today's HIGH #2 (STELLAR), #3 (Mas Montserrat ancestry
   adjustment), and #6 (Baya damaging-variant enrichment in tail
   deviants) form a coherent sub-thread that the current keyword list
   catches only via the generic `polygenic` term. Suggested additions:
   `polygenic score stability`, `PRS calibration`, `ancestry
   adjustment`, `composite risk score`, `rare variant burden score`.

4. **Add pharmacoepi + drug-class OMOP-adjacent keywords.**
   `target trial emulation` is already present; add `active
   comparator`, `new user design`, `TTE`, `pharmacovigilance`
   explicitly. Today's HIGH #4 (Dai et al. GLP-1 TTE) was surfaced by
   Patrick Ryan feed, not by keyword.

5. **Add `EHR foundation model` variants.** `foundation model` +
   `electronic health records` combined would raise the precision on
   picking up SSL-for-EHR papers like today's HIGH #10 (Carter et al.
   future-clinical-discriminability).

6. **Continue tracking your own self-citation feed.** Today's HIGH
   #13 (Gül et al. CGRP mAb TTE) is a self-feed hit — same high-
   precision channel that fired on the nephro PRS+PheWAS paper in 06-20.
   Keep both alerts as-is.

7. **Consider adding an `arxiv-digest` "silent-Sunday" alert** — the
   pipeline has now produced 0 or 1 papers on 12 of the last 20 days.
   Rather than continuing to output "0 relevant papers" with no
   pipeline-health signal, an alert at "5 consecutive dry days" would
   flag whether the source-feed expansion (rec. #1 above) needs to be
   prioritized.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 14 | (1) MIXPRS [Yang, Nat Genet], (2) STELLAR ensemble PRS+rare [Yang, medRxiv], (3) Mas Montserrat non-param ancestry adjust [Yang+Denny, medRxiv], (4) Dai et al. GLP-1 TTE in obesity+AID [Ryan, JAHA], (5) Yerukala Sathipati AoU HBOC screening disparities [Denny, medRxiv], (6) Baya et al. rare-variant enrichment in PGS tails [Montgomery, AJHG], (7) DeepEvidence biomedical KG agent [Chute, Nat Mach Intell], (8) Guimbellot Ivacaftor growth [Ryan, ERJ], (9) Krueger et al. multi-ancestry PWAS [Karczewski, medRxiv], (10) Carter et al. self-supervised EHR-FM [foundation-models keyword], (11) Zhao et al. reflex RNA-seq for VUS [Karczewski, npj Genomic Medicine], (12) Jafarpour CV drug-safety KG scoping [Chute], (13) Gül CGRP mAb vs onabotA [self-feed], (14) Wang et al. TOPMed T2D eQTL colocalization [Yang, Diabetes] |
| METHODS-WATCH | 8 | Miao/Pritchard/Zou Agentic Garden of Forking Paths, Zhang et al. ICU disease trajectories, Garter et al. ETI weight prediction in CF children, Goeyvaerts canagliflozin pediatric PK/PD, Jiang genomic dimensionality bounds, Atschekzei RA + IEI rare variants, Vos et al. drug-induced AKI KG, Li et al. glaucoma multi-omic review |
| SKIP | ~25 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 6 METHODS-WATCH over one day),
this 17-day window delivers **14 HIGH / 8 METHODS-WATCH**, dominated
by:

- **A dense PRS-methodology cluster (HIGH #1, #2, #3, #6, #9)** —
  MIXPRS, STELLAR, non-parametric ancestry adjustment, tail-deviation-
  rare-variant enrichment, and multi-ancestry PWAS all land in this
  window and together define a coherent 2026 H2 **"PRS +
  cross-ancestry + rare-variant + calibration"** sub-thread. Read as a
  group.
- **Two strong pharmacoepi TTE/RWE items (HIGH #4 GLP-1 AID, #8
  Ivacaftor growth, #13 CGRP-mAb migraine)** — templates and specific
  effect estimates for your drug-class threads.
- **Three biomedical-KG papers (HIGH #7 DeepEvidence, #12 CV-KG-PV
  scoping)** — DeepEvidence in particular is a landmark for the
  biomedical-KG + LLM-agent + drug-repurposing intersection.
- **AoU-focused HIGH #5** — the HBOC-screening-disparities paper is
  the single most operationally-relevant AoU paper this window.

The `arxiv-digest` pipeline continues to underdeliver — 15 daily runs
in this window produced zero on-thread papers. All value came from
Scholar alerts. The pipeline recommendations at the top of this
section are unchanged from 06-20 and remain the single highest-
leverage change available.
