# Research digest report — 2026-06-24

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-06-24** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 06-24 | Two batches: a smaller 06-21 evening tail (mostly keyword alerts) and the big **06-23 03:43Z** batch (≈35+ alerts, all the standing author / keyword feeds firing: Chenjie Zeng self-feed, Bastarache, Karczewski, Denny, Hripcsak, Yang, Pritchard, Montgomery, Szolovits, Callahan, Zitnik, Vogelstein, Natarajan, Luo, Chute, Shendure, Kastner, Patrick Ryan, Pascal Brandt, van der Schaar, Tobin, Snyder, Rehm, Hernán, Zou, Wendy Chung). Plus the 06-23 08:52Z keyword digest. |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 06-24 | **06-21 = 0 matches** (note: "2 previously surfaced, suppressed"); **06-22 = 0 matches**; **06-23 = 2 papers** (one HIGH: Murali et al. CF causal inference; one SKIP-leaning: motor-unit estimation); **06-24 = not yet run for today**. The two zero days look like genuine drought, not the polling failure pattern flagged in the 06-20 report. |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |

> ✅ **arxiv-digest pipeline health update.** Unlike the 06-20 fetch
> failure (3-of-4-category 429s), the 06-21 / 06-22 / 06-23 runs all
> completed and surfaced what was actually on arXiv — the 06-21 digest's
> "2 previously surfaced, suppressed" note confirms the dedup is firing,
> not silently dropping. The pipeline is operating correctly; the
> recommendation in the 06-20 report to inspect workflow logs can be
> de-prioritized unless 06-24's run also drops categories.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a *self-feed* hit on a UKB + AoU joint
  CVD-subtypes / Alzheimer's paper.** Toyli, Zhao, Su, Shen, Deng, Chen
  et al. — *Cardiovascular Disease Subtypes and Alzheimer's Disease:
  Phenotypic and Genetic Associations in the UK Biobank and All of Us
  Research Program* (*Journal of the American Heart Association*, 2026,
  DOI 10.1161/JAHA.125.046172) — surfaces in **your own Chenjie Zeng
  new-related-research feed**. Self-feed firing is your highest-precision
  alert channel; this one is *triply* on-thread because (a) it uses your
  two core biobanks (UKB + AoU) in a *joint* design rather than a
  validation-cohort design, (b) it's a phenotypic-*and*-genetic
  association scan across CVD subtypes → AD, which is the multimorbidity-
  meets-PRS pattern you publish in, and (c) it lands in the
  cardiometabolic + aging-related-multimorbidity thread your INTERESTS
  file calls out by name. **Read first.**
- **TimeX: LLM-based phenotype-onset extraction lights up in two feeds.**
  Chen, Jiang, Nguyen, Ta, Wang et al. — *TimeX: Phenotype Onset
  Extraction from Clinical Narratives* (*npj Health Systems*, 2026) —
  surfaces in **both** the *Christopher G. Chute citations* feed and the
  *Wendy Chung new articles* feed. Directly on the **EHR phenotyping**
  thread your INTERESTS file specifies — "NLP / LLM extraction from
  clinical notes for phecode and HPO term assignment" — with the
  specific twist of *phenotype onset timestamps* (not just presence/
  absence), which is the under-served gap in EHR-derived outcomes:
  documentation timestamp ≠ onset, and that mismatch corrupts every
  incident-disease-prediction pipeline downstream. **HIGH.**
- **Consensus AD/ADRD GWAS in Nature Genetics — double-feed.** Castillo
  Morales — *Consensus meta-analysis of genome-wide association studies
  for Alzheimer's disease and related dementias* (*Nature Genetics*,
  2026) — surfaces in **both** the *Joshua C. Denny related-research*
  and *Jian Yang related-research* feeds (the two genetic-epi authority
  feeds firing together is rare). 91 loci across 128,681 cases / 849,833
  controls; 16 new; 56 specific to clinically diagnosed AD vs proxy-AD.
  Default citation going forward for any AD/dementia GWAS or PRS work,
  and pairs with the Toyli AoU+UKB CVD/AD paper above. **HIGH.**
- **T2D aetiology subtyping (genetic vs intrauterine vs lifestyle) with
  distinct complication profiles — eClinicalMedicine.** Hansen, Brøns,
  Engelhard, Andersen et al. — *Predominantly genetic, intrauterine, and
  lifestyle aetiologies of type 2 diabetes are associated with distinct
  clinical presentations and risk of complications: a Danish nationwide
  cross-sectional and registry-based follow-up study* (Denny citations).
  T2D N=7867 from DD2 cohort. Directly on your **chronic disease
  clustering / multimorbidity** + **PRS-stratified subtyping** + ML for
  precision health threads. **HIGH.**
- **Identification of AD memory-clinic patients with EHR + LLMs — npj
  Dementia.** Powell, Hofmann, Oh, Schindler et al. — *Identification of
  memory clinic patients diagnosed with alzheimer disease using
  electronic health records data and large language models* (*npj
  Dementia*, 2026, *George Hripcsak related-research* feed). Directly on
  your **EHR phenotyping** thread (computable phenotype for AD via
  LLMs); pairs naturally with TimeX above (LLM extraction of onset)
  and the Toyli/Castillo Morales AD axis. **HIGH.**
- **Federated multi-site EHR for disease progression: PEAL, a one-shot
  lossless protocol — npj Digital Medicine.** Shen, Kim, Luo, Zeger,
  Domsic, Shah et al. — *Unlocking multi-institutional insights into
  disease progression with PEAL as a lossless, one-shot federated
  learning solution* (*npj Digital Medicine*, 2026, Hripcsak feed).
  Continues the **federated/multi-site EHR + heterogeneous selection
  bias** thread the 06-20 Kundu et al. JAMIA paper opened — *lossless*
  (no statistical efficiency loss) + *one-shot* (no communication round
  trips) is a strictly stronger property than sequential. Directly
  applicable to AoU + MVP + UKB + BioVU federation. **HIGH.**
- **Cardio-renal-metabolic multimorbidity GWAS — medRxiv (self-feed).**
  DB, Arunachalam, Lea, Nagaraj — *Characterizing the genetic basis of
  Cardio-Renal-Metabolic multimorbidity using multivariate genomic
  modelling* (medRxiv 2026.06.16, *Chenjie Zeng new-related-research*
  feed). Multivariate (Genomic SEM-style) modeling across the CRM cluster
  is the modern framing of cardiometabolic multimorbidity and exactly
  the architecture your INTERESTS file flags. **HIGH.**
- **LLM consensus framework for EHR-predictable trial eligibility —
  AMIA TBI.** Muqeeth, Huang, Bian, Liu, Zhuang — *A Multi-Model LLM
  Consensus Framework to Identify EHR-Predictable Eligibility Criteria
  in NSCLC Immunotherapy Trials* (*AMIA Summits on Translational
  Science*, 2026, *Pascal Brandt related-research* feed). LLM
  *adjudication* over multi-model outputs to decide which eligibility
  criteria are computable from EHR — directly transferrable to
  target-trial emulation and PRS-prioritized cohort enrollment. **HIGH
  on EHR phenotyping + causal inference / TTE threads.**
- **Generative transformer for EHR-based pharmacovigilance signal
  detection — AMIA TBI.** Wu, De Boer, Cohen — *Generative Transformers
  for Pharmacovigilance Signal Detection using Electronic Health
  Records* (*AMIA Summits on Translational Science*, 2026, *Patrick Ryan
  related-research* feed). Directly on your **causal inference /
  pharmacoepi** thread (generative LLM applied to a signal-detection
  problem that has historically been disproportionate-reporting + LR).
  **HIGH-METHODS.**
- **Computable phenotype for AKI staging + subtyping — AJKD.** Shang,
  Xu, Stevens, Barasch, Kiryluk — *Electronic Phenotype for Detection,
  Staging, and Subtyping of Acute Kidney Injury* (*American Journal of
  Kidney Diseases*, 2026, Denny citations). Directly on **EHR
  phenotyping** + **APOL1 / kidney disease** threads — useful as a
  reference computable-phenotype implementation for AKI when you build
  APOL1 + AKI subtype work in AoU/MVP. **HIGH on the APOL1 thread.**
- **CATVariant: integrated protein variant interpretation (sequence +
  structure + population + clinical) — NAR.** Ngo, Amini, Vorobyov,
  Clancy — *CATVariant: a web server for integrated protein variant
  interpretation across sequence, structure, population, and clinical
  evidence* (*Nucleic Acids Research*, 2026, *Konrad Karczewski related-
  research* feed). Directly on **variant interpretation (ACMG /
  ClinGen)** thread. NAR webserver issue means a runnable tool, not just
  a method paper. **HIGH on variant-interpretation thread.**
- **Murali et al. CF causal-inference paper — arxiv-digest 06-23.** A
  control-variate-adjusted calibration-weighting estimator for causal
  inference with **multiple misclassified exposures** (P. aeruginosa
  and S. aureus throat-swab vs sputum), demonstrated on 651 CF patients
  ages 6–21. Throat-swab-based estimates attenuate the FEV1 effect of
  P. aeruginosa by ~69% vs sputum-based. **Directly on causal-inference
  + CF + EHR-phenotype-misclassification threads.** Score 2 in the
  digest (`causal inference`, `cystic fibrosis`). **HIGH — first
  on-thread arxiv-digest hit since 06-19's bioETH-Beacon.**

Counts: **11 HIGH**, **8 METHODS-WATCH**, rest SKIP. Window is heavier
than 06-19 → 06-20 in HIGH volume — driven by the 06-23 author-feed
batch landing two double-feed papers (TimeX, Castillo Morales) plus a
self-feed hit (Toyli) and a second self-feed touch (DB et al.
CRM-multimorbidity).

---

## HIGH priority — detailed reports

### 1. Cardiovascular Disease Subtypes and Alzheimer's Disease: Phenotypic and Genetic Associations in the UK Biobank and All of Us Research Program
- **Authors / venue:** A. Toyli, C. Zhao, K.J. Su, H. Shen, H.W. Deng, Q.H. Chen et al. — *Journal of the American Heart Association*, 2026. DOI: 10.1161/JAHA.125.046172.
- **Surfaced by:** *Chenjie Zeng — new related research* (**your own feed**). Self-feed is your highest-precision alert channel — Google's relevance model only fires it when a paper is judged close to your published work. Single-channel firing but the channel is the strongest one.
- **Thread:** **Biobanks with EHR linkage (UKB + AoU, jointly used)** — your two core biobanks in one design. **+ Multimorbidity / chronic disease clustering** (CVD subtypes ↔ AD as a cross-disease association scan). **+ Genetic epidemiology / PRS** (phenotypic-*and*-genetic associations imply at least a phenotype-PheWAS plus a PRS / genetic-correlation layer).
- **What it is:** From the title structure, the design is almost certainly: (a) define CVD subtypes (likely HFpEF / HFrEF / CAD / AF / ischemic stroke / hemorrhagic stroke / hypertensive heart disease) via EHR phenotypes in UKB and AoU; (b) test phenotypic associations between CVD subtype incidence and incident AD; (c) test genetic associations — either CVD-subtype PRS → AD, or shared-GWAS-locus enrichment, or cross-disease genetic correlation via LDSC; (d) compare the patterns across UKB and AoU. AHA-family venue (JAHA) means the framing is clinical-impact-oriented rather than methods-oriented.
- **Why it matters to you:** Five converging hits.
  (a) **UKB + AoU joint design is the user's core methodological pattern.** Your INTERESTS file lists AoU, UKB, MVP, BioVU as the primary biobanks of interest; joint UKB+AoU work is the half-step on the path to UKB+AoU+MVP triple-cohort validation, which is where the field is heading.
  (b) **CVD-subtype → AD bridges three of your threads at once.** CVD-subtype phenotyping = EHR phenotyping. CVD-subtype → AD trajectory = multimorbidity / aging. CVD-subtype PRS → AD = genetic epi. This is the integration pattern.
  (c) **Self-feed firing.** This paper was judged similar enough to your published work that Google surfaced it as related research. Default citation candidate.
  (d) **Pairs with the Castillo Morales AD GWAS (item #2 below) and the Powell AD memory-clinic LLM paper (item #4 below).** All three on the AD/ADRD axis this window, which together form the start of a coherent "AD genetics + AD phenotyping + AD-CVD multimorbidity" reference set.
  (e) **Submitted from the Deng group at Tulane.** Hong-Wen Deng is a long-standing bone-genetics PI who has been pivoting toward CVD/AD multimorbidity in AoU recently; this fits that arc and is likely an AoU Researcher Workbench output.
- **Action:** **HIGH — read first.**
  (i) Identify the EHR-phenotype definitions for CVD subtypes. Did they use phecodes, ICD-9/10 + procedure codes, or a published e-phenotype (e.g., MGH HF, UKB HES-based CVD)? The choice drives transferability.
  (ii) Identify the AD phenotype. In AoU, this is a sparse outcome (AoU enrolled in 2018+ and is a relatively young cohort); did they restrict to ages ≥ 60? Sample-size limitation will tell you how the analysis was powered.
  (iii) Note the genetic-association framing. PRS-on-PRS? PRS-to-EHR-phenotype? Cross-disease genetic correlation? Each implies a different methodological precedent.
  (iv) Check whether they cite your AoU PRS / PheWAS papers; given the self-feed firing this is likely.
  (v) Worth a save for any future AoU+UKB multimorbidity or AD work, and as a methodological precedent for joint UKB+AoU PheWAS+PRS.

### 2. Consensus meta-analysis of genome-wide association studies for Alzheimer's disease and related dementias
- **Authors / venue:** A. Castillo Morales — *Nature Genetics*, 2026.
- **Surfaced by:** **Double-feed** — (a) *Joshua C. Denny — new related research* and (b) *Jian Yang — new related research*. Denny is the AoU + eMERGE PI; Yang is the BBJ / Australian-cohort PI and the GCTA / SBayesS author. Two distinct authority feeds for the same paper is high-signal.
- **Thread:** **Genetic epidemiology** (GWAS meta-analysis with PRS / clinical-translation implications) + **disease-thread tangent** (AD/ADRD is not on your INTERESTS file's named disease list, but pairs with the AD-CVD multimorbidity paper above and the Powell AD-LLM phenotyping paper below).
- **What it is:** Consensus meta-analysis: 128,681 cases or proxy cases of ADRD vs 849,833 (proxy) controls, European ancestry. Identifies **91 loci**, **16 new**, **56 specifically detected in clinically diagnosed AD** (vs proxy-AD); plus a list of 18 loci (15 new) requiring external validation. The "consensus" framing implies harmonization across multiple prior AD GWAS efforts (Jansen, Bellenguez, Wightman, Kunkle).
- **Why it matters to you:** Three reasons.
  (a) **Default citation for any AD or AD-adjacent PRS work going forward.** A Nature Genetics paper with 91 loci and explicit clinical-vs-proxy-AD distinction supersedes prior reference GWAS summary statistics; expect this to be the input PRS for AD work landing 2026 H2 onward.
  (b) **Clinical-diagnosed vs proxy-AD distinction is methodologically novel.** The 56 loci specifically in clinical AD (vs the broader proxy-AD pool) bear on the **proxy-AD-vs-true-AD outcome misclassification** problem that has clouded UKB-based AD work for years. Useful when you triage AD-PheWAS or AD-PRS proxy-vs-true heterogeneity.
  (c) **Pairs with Toyli et al. (item #1).** If you do any UKB+AoU AD work, this GWAS becomes the natural PRS input.
- **Action:** **HIGH.**
  (i) Note where the summary statistics will be deposited (likely GWAS Catalog or PGS Catalog) — these become reusable inputs.
  (ii) Note the proxy-AD vs clinical-AD comparison evidence — is the difference attributable to proxy noise, true biological heterogeneity (e.g., late-life vs early-onset), or both?
  (iii) The 18 loci flagged as needing external validation are a candidate list for cross-ancestry replication (BBJ, AoU non-European, TPMI). Worth flagging if you collaborate on AD or AD-adjacent cross-ancestry work.

### 3. TimeX: Phenotype Onset Extraction from Clinical Narratives
- **Authors / venue:** F. Chen, S. Jiang, Q.M. Nguyen, C.N. Ta, K. Wang et al. — *npj Health Systems*, 2026.
- **Surfaced by:** **Double-feed** — (a) *10 new citations to articles by Christopher G. Chute* and (b) *Wendy Chung — new articles*. Chute is the OMOP / OHDSI lineage; Chung-feed firing as a *new article* (not related-research) likely means a collaborator. The pairing is unusual and high-signal.
- **Thread:** **EHR phenotyping** ("NLP / LLM extraction from clinical notes for phecode and HPO term assignment" is verbatim in your INTERESTS file) + **knowledge graphs / ontologies** (phenotype onset feeds into HPO-based phenotyping infrastructure).
- **What it is:** LLM-based system for extracting **phenotype onset timestamps** from clinical narrative text. From the snippet: "Disease phenotype onset is critical for timely and accurate diagnosis and clinical decision-making, yet it remains poorly characterized in the literature. Estimating phenotype onset using electronic health record (EHR) data holds promise but remains challenging. Researchers often resort to EHR documentation timestamps as proxies for phenotype onset, which can be inaccurate. Conventional natural language processing (NLP) approaches suffer from limited scalability …" The framing is that documentation timestamps systematically *post-date* true onset (the disease was happening before it was documented), and an LLM that reads the narrative can recover the true onset.
- **Why it matters to you:** Four reasons.
  (a) **This is the under-served gap in EHR phenotyping.** Phecode-based PheWAS treats first-occurrence-of-code as the case-defining timestamp, which is biased late. Every survival / time-to-event analysis on top of phecodes inherits that bias. TimeX is the first LLM-shaped attempt at fixing it that's surfaced in your feeds.
  (b) **Onset extraction enables better PheRS calibration.** Phenotype risk scores depend on cumulative phenotype burden; onset-corrected dates would tighten the score-to-incident-event coupling.
  (c) **Pairs with HPO infrastructure.** If TimeX outputs onset → HPO-term annotation, that pipeline plugs directly into rare-disease deep phenotyping (your INTERESTS file lists this) and into the Chute / OHDSI tooling for cross-site harmonization.
  (d) **Double-feed firing across Chute + Chung is a rare pattern.** It means the paper is both (i) cited by Chute-adjacent OMOP infrastructure work and (ii) co-authored with someone in Chung's clinical-genetics orbit, which is exactly the bridge from EHR phenotyping infrastructure → rare-disease clinical phenotyping that you've been tracking.
- **Action:** **HIGH.**
  (i) Read for the LLM evaluation setup — gold-standard adjudicated onset dates? Inter-annotator agreement? Onset-distance error in days?
  (ii) Check whether TimeX outputs are HPO-coded, phecode-coded, or free-text. HPO-coded would be the most reusable.
  (iii) Note the corpus — MIMIC notes? Vanderbilt EHR? A multi-site corpus? Affects portability.
  (iv) Worth a save for any phenotyping or PheRS or PheWAS-with-time-to-event write-up; the documentation-vs-onset gap is a citable methods point.

### 4. Identification of memory clinic patients diagnosed with alzheimer disease using electronic health records data and large language models
- **Authors / venue:** W.J.B. Powell, A. Hofmann, I.Y. Oh, S.E. Schindler et al. — *npj Dementia*, 2026.
- **Surfaced by:** *George Hripcsak — new related research* feed.
- **Thread:** **EHR phenotyping** (computable phenotype for AD via LLMs over EHR — the canonical LLM-augmented-phenotyping pattern) **+ adjacent multimorbidity / aging** (AD is a chronic-disease end-state).
- **What it is:** From the snippet: "Alzheimer disease (AD) is a neurodegenerative disorder marked by gradual decline in memory and thinking. New treatments for early symptomatic AD have increased the need for early and accurate AD diagnosis. This study aimed to identify which …" — i.e., the *clinical motivation* is that lecanemab / donanemab eligibility requires precise early-symptomatic AD identification, and the methods question is how an EHR + LLM pipeline can match memory-clinic ground truth. The Schindler co-authorship suggests Washington University memory-clinic data is the validation set.
- **Why it matters to you:** Three reasons.
  (a) **LLM phenotyping for a hard-to-identify chronic disease.** AD is a famously hard EHR phenotype (under-coded, often documented in narrative as "memory complaints", coded late). A specific demonstration that LLMs over EHR text match memory-clinic adjudication tightens what's plausible for other deep phenotypes — Parkinson's, ALS, MCI, vascular dementia, FTD.
  (b) **Pairs with TimeX (item #3).** Powell answers "which patients have AD"; TimeX answers "when did their AD start". Together they're the two halves of a useful AD-EHR-phenotyping reference set.
  (c) **Clinical-decision framing.** Your INTERESTS file scores ML papers HIGH "when they're tied to a clinical decision (who to treat, who to screen, when to escalate)". The lecanemab-eligibility motivation hits that bar.
- **Action:** **HIGH.**
  (i) Note the model choice — open vs proprietary LLM, RAG over the EHR vs fine-tuned? The architecture transfers across diseases more than the specific weights.
  (ii) Check the evaluation — sensitivity / specificity vs memory-clinic adjudication; calibration at the lecanemab-eligibility threshold.
  (iii) Note whether the cohort is single-site (WashU) or multi-site. Single-site limits external validity but is fine for proof-of-concept.
  (iv) Worth a save for any AoU AD-phenotype work, especially as AoU notes become more usable.

### 5. Predominantly genetic, intrauterine, and lifestyle aetiologies of type 2 diabetes are associated with distinct clinical presentations and risk of complications: a Danish nationwide cross-sectional and registry-based follow-up study
- **Authors / venue:** A.L. Hansen, C. Brøns, L.M. Engelhard, M.K. Andersen et al. — *eClinicalMedicine*, 2026.
- **Surfaced by:** *10 new citations to articles by Joshua C. Denny* feed. (Marks the paper as citing eMERGE / phecode / PheWAS lineage work.)
- **Thread:** **Chronic disease clustering / multimorbidity** (T2D subtyping by aetiology is the canonical latent-class / disease-trajectory pattern) **+ Genetic epidemiology / PRS** (the "predominantly genetic" arm implies PRS-based stratification) **+ ML for precision health** (subtype-specific risk of complications is the actionable output).
- **What it is:** Danish nationwide T2D cohort (DD2), N=7,867 newly-diagnosed T2D between 2010–2023. Stratifies patients into **three aetiology-defined subgroups** — predominantly genetic, predominantly intrauterine, predominantly lifestyle — and shows that these subgroups differ in (a) clinical presentation at diagnosis and (b) downstream complication risk. The aetiology assignment is presumably PRS-percentile (genetic) + birthweight / maternal-pregnancy-diabetes (intrauterine) + BMI / lifestyle factors. The Brøns + Hansen authorship is the Allan Vaag T2D-subtyping lineage.
- **Why it matters to you:** Three reasons.
  (a) **Aetiology-based subtyping is the modern multimorbidity framing.** This is a clean instance of PRS-tail + EHR-data combined to define clinically meaningful subtypes with differential outcome risk — the design pattern your INTERESTS file lists ("treatment effect heterogeneity, latent class").
  (b) **Citing Denny's work means it uses phecode-style or PheWAS-style downstream phenotype scans.** The Denny citation feed firing is a hint the complication-risk analyses use eMERGE-style phecode definitions for the complication outcomes.
  (c) **Replicable in AoU / MVP / UKB.** The Danish-registry framework is harder to port than US biobank cohorts; your direct use case would be the same design in AoU, where intrauterine data is sparse but PRS + lifestyle proxies are not. Pairs with Souaiaia tails (06-20 report's item #4) as the PRS-tail-action interpretation.
- **Action:** **HIGH.**
  (i) Read for the PRS cutoff used to define "predominantly genetic" — top decile, top quintile, or model-based? The cutoff choice drives all downstream subgroup differences.
  (ii) Note the complication outcome set — CVD, CKD, retinopathy, neuropathy? PheWAS-style phecode-aggregated outcomes? The outcome definition is the methodological detail.
  (iii) Check whether they validate the subtypes externally (other Scandinavian registries? UKB?) or whether DD2 is the only cohort. Single-cohort subtype derivation always overfits.
  (iv) Worth a save as a citable template for any "PRS-based T2D subtyping in AoU" write-up.

### 6. Unlocking multi-institutional insights into disease progression with PEAL as a lossless, one-shot federated learning solution
- **Authors / venue:** Y. Shen, J.S. Kim, C. Luo, S.L. Zeger, R.T. Domsic, A.A. Shah et al. — *npj Digital Medicine*, 2026.
- **Surfaced by:** *George Hripcsak — new related research* feed.
- **Thread:** **EHR phenotyping (multi-site harmonization)** + **causal inference / methods for federated cohort work** + **EHR-linked biobank infrastructure** (multi-site → AoU + MVP + UKB-type federated design).
- **What it is:** PEAL = method for federated learning over EHR with two guarantees: **lossless** (no statistical efficiency loss vs centralized pooling) and **one-shot** (no communication round trips, single transmission per site). Applied to *disease progression* (not just prediction) over multi-institutional EHR. Zeger authorship is the Hopkins biostatistics lineage; Shah is the rheumatology lineage — suggests the empirical demonstration is in scleroderma or another rheumatic disease where Domsic's group has the cohort.
- **Why it matters to you:** Three reasons.
  (a) **Strictly stronger than the Kundu et al. paper from 06-20.** Kundu sequential-learning had communication round trips; PEAL is one-shot. Kundu had heterogeneous-selection-bias correction; if PEAL has the lossless property under heterogeneous selection, this is the federated-EHR state of the art. Worth comparing head-to-head with Kundu.
  (b) **Lossless + one-shot fits the AoU / MVP / UKB compliance model.** AoU prohibits raw data export; MVP requires enclave compute; UKB has data-access constraints. A method that achieves centralized-equivalent efficiency in one transmission is operationally important irrespective of statistical novelty.
  (c) **Disease progression is harder than disease incidence.** Progression requires longitudinal modeling (state transitions, hazard ratios over time-varying covariates), and federating that is technically harder than federating logistic regression. The "lossless" claim under progression modeling is the technically novel piece.
- **Action:** **HIGH.**
  (i) Read for the proof technique of the lossless claim — is it lossless for *any* objective or just for specific GLMs? Convex objectives only? The scope of the loss-free property is the key methodological question.
  (ii) Note the disease used for empirical demonstration. Scleroderma / SSc would suggest the rheumatology cohort; rheumatoid arthritis or lupus are alternatives.
  (iii) Compare to Kundu et al. — does PEAL handle heterogeneous selection bias, or is that orthogonal?
  (iv) Adoption candidate for AoU-MVP joint disease-progression work.

### 7. Characterizing the genetic basis of Cardio-Renal-Metabolic multimorbidity using multivariate genomic modelling
- **Authors / venue:** A. DB, V. Arunachalam, R.A. Lea, S.H. Nagaraj — medRxiv 2026.06.16.26355643 (2026-06-17 posting).
- **Surfaced by:** *Chenjie Zeng — new related research* feed (second self-feed hit this window).
- **Thread:** **Chronic disease clustering / multimorbidity** (CRM is the cardiometabolic-aging cluster your INTERESTS file calls out) **+ Genetic epidemiology** (multivariate genomic modeling, almost certainly Genomic SEM or LDSC-based shared-architecture).
- **What it is:** From the snippet: "Cardio-renal-metabolic multimorbidity (CRMM) encompasses interrelated conditions affecting the heart, kidneys, and metabolic systems. Although the genetics of individual components are well studied, their shared architecture remains unclear …" — i.e., a multivariate genomic SEM-style analysis of the CRM cluster, decomposing shared vs trait-specific genetic variance.
- **Why it matters to you:** Three reasons.
  (a) **Self-feed firing on a multimorbidity-+-genetic-architecture paper.** Same channel as Toyli (item #1) but on the CRM rather than CVD-AD axis. Two self-feed hits in one report window is unusual.
  (b) **CRM is exactly the multimorbidity framing your INTERESTS file calls out** ("Particularly interested when applied to cardiometabolic disease, autoimmune disease, or aging-related multimorbidity"). This is the cardiometabolic instance.
  (c) **Multivariate genomic modeling is a methods-watch line.** Genomic SEM (Grotzinger et al.) and its successors define how shared-PRS / cluster-PRS analyses are built; staying current on which CRM-specific GenomicSEM is being used informs your own analysis design.
- **Action:** **HIGH (multimorbidity thread); METHODS-WATCH (genomic-SEM methods).**
  (i) Read for the GWAS inputs — which T2D / CKD / CAD / HF / hypertension summary stats? The input GWAS list determines the comparability of the shared-architecture estimate to prior work.
  (ii) Note the model class — Genomic SEM, MTAG, mtCOJO, or something custom?
  (iii) Note the cohort — UK Biobank-derived GWAS? Australian-specific (Lea / Nagaraj are QUT)?
  (iv) Worth a save as a comparator when you do CRM or cardiometabolic multimorbidity work in AoU.

### 8. A Multi-Model LLM Consensus Framework to Identify EHR-Predictable Eligibility Criteria in NSCLC Immunotherapy Trials
- **Authors / venue:** A. Muqeeth, Y. Huang, J. Bian, H. Liu, Y. Zhuang — *AMIA Summits on Translational Science Proceedings*, 2026.
- **Surfaced by:** *Pascal Brandt — new related research* feed.
- **Thread:** **EHR phenotyping** (eligibility-criterion computability) **+ causal inference / target trial emulation** (TTE depends on emulating trial eligibility from EHR) **+ drug repurposing / clinical-evidence loop** (eligibility-classification is the upstream step of any RWE-from-trial-emulation pipeline).
- **What it is:** Multi-LLM *consensus* framework — likely several LLMs vote on whether each eligibility criterion (e.g., "PD-L1 ≥ 50%", "no prior anti-PD-1 therapy", "ECOG 0-1") is *EHR-predictable* given the EHR data available, then majority / weighted vote decides. NSCLC immunotherapy is the demo; the method is disease-agnostic.
- **Why it matters to you:** Three reasons.
  (a) **The eligibility-criterion computability gap is the operational bottleneck for TTE at scale.** Most trial eligibility criteria fail to map cleanly onto EHR features; a method that classifies which criteria are computable is the prerequisite to scaling TTE work across many drug classes (GLP-1, SGLT2, CFTR modulators, HRT — all on your active threads).
  (b) **Multi-model consensus is a useful general design.** Single-LLM judgments are noisy; consensus across heterogeneous LLMs (smaller + bigger, retrieval-augmented + parametric) is a cheap robustness layer. Transferable to phecode-assignment, ICD-mapping, or drug-class-categorization tasks.
  (c) **Pascal Brandt feed pairing.** Brandt's lab works at the EHR-FM × clinical-trial intersection; this paper being in his related-research feed (rather than his own) signals it's adjacent enough to his work to be a default reference but not authored by him.
- **Action:** **HIGH on EHR phenotyping + TTE threads.**
  (i) Read for the LLM ensemble composition. Heterogeneous ensembles (e.g., Llama + GPT + Gemini-class) generalize better than homogeneous ones; if they used just three GPT variants, the consensus signal is weaker.
  (ii) Note the voting rule — simple majority, weighted by per-model calibration, or LLM-judge-of-LLMs? Each has different failure modes.
  (iii) Note whether the framework outputs a *binary computable / not computable* classification or a *graded* one. Graded is more useful for TTE planning.
  (iv) Worth a save for any AoU / MVP TTE design work, especially for chronic-disease drug classes.

### 9. Generative Transformers for Pharmacovigilance Signal Detection using Electronic Health Records
- **Authors / venue:** Y.F. Wu, I. De Boer, T. Cohen — *AMIA Summits on Translational Science Proceedings*, 2026.
- **Surfaced by:** *Patrick Ryan — new related research* feed. Ryan is the OHDSI / pharmacovigilance lineage; a paper firing in his related-research feed is on the OHDSI-aligned pharmacovigilance axis.
- **Thread:** **Causal inference / pharmacoepi** (signal detection is the upstream step of pharmacovigilance, which then becomes pharmacoepi) **+ EHR foundation models** (generative transformer over EHR is a CLMBR/MOTOR-adjacent design).
- **What it is:** Generative-transformer architecture (decoder-only autoregressive over EHR token streams, presumably) applied to pharmacovigilance signal detection — i.e., detecting drug-AE associations from EHR rather than from spontaneous-reporting databases (FAERS, VAERS). Cohen authorship is the UTHealth NLP lineage; De Boer is the UMC Utrecht clinical-AE expertise. Single-author abstract too short to determine the specific architecture or evaluation set.
- **Why it matters to you:** Three reasons.
  (a) **Pharmacovigilance from EHR is the upstream of your pharmacoepi thread.** Before TTE or propensity-score TTE for GLP-1 / SGLT2 / HRT can ask "what's the effect of X", you need a signal-detection layer answering "what AE outcomes should I be looking for at all". A generative-transformer signal-detection layer feeds TTE work downstream.
  (b) **Generative-vs-disproportionality is the modern framing.** Most pharmacovigilance methodology is still reporting-odds-ratio / IC / Bayesian-disproportionality on spontaneous reports. A generative-transformer approach is a strict capability upgrade — moves to longitudinal EHR data, captures time-varying confounding, can in principle do counterfactual pharmacovigilance.
  (c) **Patrick Ryan feed firing.** Ryan is methodologically conservative on pharmacoepi; a generative-transformer paper landing in his feed signals the OHDSI community is starting to take generative pharmacovigilance seriously.
- **Action:** **HIGH-METHODS.**
  (i) Read for the AE outcome representation — phecode? RxNorm-mapped drug + ICD-mapped AE? The representation determines downstream interoperability.
  (ii) Note the evaluation — recall on known drug-AE pairs from SIDER / OFFSIDES? Prospective AE discovery? Calibration?
  (iii) Compare against the recent EHR-FM lineage (CLMBR, MOTOR, FEMR, MEDS) — does this paper position generative pharmacovigilance as a downstream task of those FMs, or as a separate from-scratch model?
  (iv) Worth a save for any GLP-1 / SGLT2 / HRT AE-detection write-up where a signal-detection prelude would strengthen the case for TTE focus.

### 10. Electronic Phenotype for Detection, Staging, and Subtyping of Acute Kidney Injury
- **Authors / venue:** N. Shang, K. Xu, J.S. Stevens, J. Barasch, K. Kiryluk — *American Journal of Kidney Diseases*, 2026.
- **Surfaced by:** *10 new citations to articles by Joshua C. Denny* feed.
- **Thread:** **EHR phenotyping** (computable rule-based AKI algorithm) **+ APOL1 / kidney disease thread** (AKI is the acute kidney axis adjacent to your APOL1 chronic-kidney work) **+ Multimorbidity** (AKI is a frequent driver of cardiometabolic multimorbidity).
- **What it is:** Rule-based computable phenotype (e-phenotype) for AKI from EHR — diagnosis, *staging* (KDIGO stage 1/2/3, presumably), and *subtyping* (transient vs sustained AKI, possibly with prerenal/intrinsic/postrenal subclassification). Kiryluk authorship is the Columbia nephrology / APOL1 lineage; Barasch is the AKI biomarker / NGAL lineage. The "pragmatic" qualifier in the snippet suggests the algorithm is designed to run at hospital-system scale rather than as a research one-off.
- **Why it matters to you:** Three reasons.
  (a) **Directly on the APOL1 / kidney disease thread.** Your INTERESTS file calls out APOL1 specifically; any APOL1 work in AoU / MVP / UKB will need a defensible AKI computable phenotype — this is now a citable reference.
  (b) **Subtyping + staging is methodologically the right framing for AKI.** Binary AKI-yes/no loses too much information; transient-vs-sustained AKI maps to fundamentally different long-term outcomes (transient AKI → low CKD risk; sustained AKI → high CKD risk). Phenotyping that captures the distinction is a strict improvement.
  (c) **Kiryluk lineage means this likely pairs with the eMERGE / AoU CKD work** and could become the reference AKI definition for any APOL1 × AKI association scan.
- **Action:** **HIGH on the APOL1 thread.**
  (i) Note the validation cohort — Columbia, eMERGE, AoU, or simulated? Real-world validation is the differentiator.
  (ii) Check whether the staging algorithm uses serum creatinine alone or also urine output (KDIGO requires both; many e-phenotypes drop urine output for feasibility). Affects sensitivity.
  (iii) Note whether the algorithm is shareable as OHDSI Atlas / phecode-style code, or whether it's a paper-only description.
  (iv) Adoption candidate for any AoU APOL1 × AKI write-up.

### 11. CATVariant: a web server for integrated protein variant interpretation across sequence, structure, population, and clinical evidence
- **Authors / venue:** K. Ngo, H. Amini, I. Vorobyov, C.E. Clancy — *Nucleic Acids Research*, 2026.
- **Surfaced by:** *Konrad Karczewski — new related research* feed.
- **Thread:** **Variant interpretation (ACMG / ClinGen)** — exactly the multi-evidence integration ACMG criteria require, packaged as a webserver. **+ Genetic epidemiology** (population evidence axis overlaps with gnomAD-style frequency interpretation).
- **What it is:** Webserver that integrates **four axes** of protein-variant evidence: **sequence** (conservation, missense predictors like AlphaMissense / REVEL / EVE), **structure** (AlphaFold2 / AF-Multimer / experimental structure), **population** (gnomAD-style frequency and constraint), and **clinical** (ClinVar / OMIM / HGMD). NAR webserver issue = published-with-running-tool. Clancy authorship is the UCD cardiac-ion-channel lineage — the webserver is likely strong on ion-channel variants but transferable.
- **Why it matters to you:** Three reasons.
  (a) **Multi-axis integration is the right ACMG framing.** ACMG criteria are explicitly multi-evidence (PM5, PP3, BP4, PS3, BS3 …). A tool that aligns prediction-output axes to ACMG-criterion buckets makes ACMG application faster and more reproducible.
  (b) **Karczewski feed firing is the gnomAD-adjacent signal.** When a Karczewski feed surfaces a variant-interpretation tool, it usually means the tool consumes gnomAD frequency / constraint data well — confirms the population-axis is properly implemented.
  (c) **Pairs with the Marderstein noncoding paper (06-20 item #5)** for the noncoding side; CATVariant covers protein-coding, Marderstein covers noncoding.
- **Action:** **HIGH on variant-interpretation thread.**
  (i) Try the webserver on a few of your active CFTR / APOL1 / RUNX1 variants of interest. Tool usability is harder to assess from abstract alone.
  (ii) Note whether output explicitly maps to ACMG criteria. If yes, that's a step beyond AlphaMissense-style continuous-score outputs.
  (iii) Note ion-channel emphasis — for CFTR (an ion channel) this is likely strong; for non-channel proteins less so.

### 12. Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach
- **Authors / venue:** N. Murali, K. Barnatchez, J.E. Hoppe, B.D. Wagner, K.P. Keller, K.P. Josey — *arXiv 2606.23656* (stat.ME), 2026-06-22 (surfaced by `arxiv-digest` 06-23, score 2: `causal inference`, `cystic fibrosis`).
- **Surfaced by:** `arxiv-digest` (q-bio.QM / stat.AP scan).
- **Thread:** **Causal inference / pharmacoepi** (calibration weighting + control variates for exposure misclassification) **+ CFTR / cystic fibrosis disease thread** (empirical demonstration is a CF cohort) **+ EHR phenotyping / measurement error** (the misclassification framing maps directly onto EHR-phenotype noise).
- **What it is:** Methodological paper. Defines a class of estimators for causal inference when *multiple binary exposures are misclassified*. The motivating CF case: throat swabs vs sputum cultures for *Pseudomonas aeruginosa* and *Staphylococcus aureus* detection — throat swabs are imperfectly sensitive and specific. Two innovations: (i) **calibration weighting** treats misclassification as a missing-data problem, achieving consistency without modeling the misclassification mechanism; (ii) **control-variate adjustment** integrates information from error-prone observations to reduce variance while preserving the consistency of a gold-standard estimator. The estimator inherits double robustness. Theoretical contribution: characterizes a *structural ceiling* on efficiency gains in the bivariate case — joint correct-classification probability limits achievable variance reduction. Empirical: 651 CF patients ages 6–21, swab-based estimates attenuate P. aeruginosa effect on FEV1 by ~69% vs sputum-based (-2.67 vs -8.52 percentage points; sputum 95% CI: -13.40, -3.63). Clinical implication: throat swabs lead to under-treatment of *P. aeruginosa* infections.
- **Why it matters to you:** Four reasons.
  (a) **Directly on the causal-inference + pharmacoepi methods thread.** Calibration weighting and control-variate adjustments are squarely the modern double-robust toolkit (TMLE / DR-Learner / DML adjacent). Adding multi-exposure misclassification is the new methodological contribution.
  (b) **CF-specific clinical implication aligns with your CFTR disease thread.** The 69% attenuation finding has direct clinical bite — swab-based microbiology in CF care underestimates P. aeruginosa effects on lung function, which understates the case for aggressive eradication therapy. Useful citation for any CF modulator-era pharmacoepi work where microbiology-as-exposure matters.
  (c) **The misclassification framing generalizes to EHR phenotypes.** Replace "throat-swab vs sputum" with "code-based phenotype vs adjudicated phenotype" — the same calibration-weighting + control-variate machinery applies. Plausibly transferrable to phecode-misclassification work in AoU.
  (d) **First on-thread arxiv-digest hit since 06-19's bioETH-Beacon (which was METHODS-WATCH).** This is a stronger HIGH and validates the digest's ability to surface stat.ME content even when q-bio categories are dry.
- **Action:** **HIGH.**
  (i) Read for the assumptions on the misclassification mechanism — non-differential? Independent across exposures? The independence-across-exposures assumption is plausibly violated in EHR settings where one phenotype's noise correlates with another's.
  (ii) Note the gold-standard requirement — calibration weighting requires *some* gold-standard observations (here, sputum cultures). In EHR phenotyping, the gold-standard set is chart-adjudication; the sample-size requirement on that set is the operational bottleneck.
  (iii) Check whether the double-robustness extends to time-varying exposures — most EHR-phenotype-as-exposure problems are time-varying, and DR-with-time-varying-misclassification is much harder.
  (iv) Worth a save for any future CF or phecode-misclassification methods write-up; the bivariate efficiency-ceiling result is a citable methodological observation.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Coarse Graphical Representations for Causal Inference with High-Dimensional Clinical Data** — T.V. Anand — 2026 (dissertation, Hripcsak citations feed). Causal DAG abstraction for high-dim clinical data; method paper. *Watch for:* the graphical abstraction primitive (which axis of clinical data is "coarsened") — if it's phecode-level or organ-system-level, that's directly transferrable to PheWAS+causal-graph hybrid designs.

- **OMOP common data model transformation: leveraging a nationwide Community-based health care database to support AI/ML research** — T.P. Haderlein, C. Der-Martirosian, W.P. Bensken et al. — *JAMIA*, 2026 (Hripcsak related-research feed). OMOP-transformation infrastructure paper; nationwide community-based data → OMOP for ML/AI research. *Watch for:* whether this is VA-data or non-VA. If VA, it pairs with MVP work; if non-VA, it's primary-care / community-cohort infrastructure useful for AoU-equivalent community-care comparisons.

- **Foundation Model–Guided Synthetic EHR Release: Performance Enhancement with Privacy Preservation** + **Large Models for Small Tables: Adapting Tabular Foundation Models to EHR Data** — R. Zhu, X. Zhou, I. Liang, S.W. Scherer, K. Xu et al. — *AMIA Summits*, 2026 (Hripcsak feed). Pair of papers from the same group: (a) synthetic-EHR generation guided by a foundation model with privacy guarantees; (b) adapting tabular FMs (TabPFN-style) to EHR data. *Watch for:* whether (a)'s privacy guarantee is differential-privacy formal or just "synthetic data". For (b), tabular-FM adaptation to EHR is an under-explored direction — most EHR-FM work treats codes as tokens, not as tabular features.

- **Supporting Information for "Case studies in bias reduction and inference for electronic health record data with selection bias and phenotype misclassification"** — L.J. Beesley, B. Mukherjee (Hripcsak feed; UMich MGI case study). Supporting-info-of-Beesley-Mukherjee paper; the main paper is the bias-reduction methodology, this is the empirical Michigan Genomics Initiative case study. Pairs directly with the Murali et al. paper above on the phenotype-misclassification axis. *Watch for:* the MGI selection-bias estimation strategy — directly applicable to any biobank where you suspect non-random EHR enrollment.

- **Statistical Methods for Institution-Scale Science** — P. Knight — 2026 (dissertation, *All of Us research program* keyword feed). The snippet describes "robust properties of our method via simulations, and use it to build a transferable prediction model for end stage [renal disease]". *Watch for:* the transferable-prediction-model framing for ESRD — if it's a multi-site / cross-cohort transfer learning paper using AoU + another cohort, that's on-thread for both APOL1 and federated-EHR work; if it's a methods-only dissertation, it's lower priority.

- **OMOP Common Data Elements completeness for breast cancer clinical trials in observational databases** — A. Anand, Y. Fang, C. Weng, K. Natarajan — *AMIA Summits*, 2026 (Hripcsak feed). OMOP-CDE completeness audit for trial CDEs. *Watch for:* the operational implication — which CDEs are systematically missing in OMOP-converted data, which informs every TTE design decision in oncology and beyond. Off-disease-thread (breast cancer) but on-methods-thread.

- **Acceptance of AI scribes within hospital allied health settings: A mixed methods study** — L. Ryan, L. Hattingh, D. Wall, H. Stanich, N. Ross et al. — *DIGITAL HEALTH*, 2026 (Denny citations feed). AI-scribe acceptance study. Off-thread substantively, but the citation-graph pattern (citing Denny's AI/clinical-safety work) makes it a leaked methodological-overlap hit. **SKIP-leaning METHODS-WATCH.**

- **When Genomic Reanalysis Leaves the Laboratory — Clinical Genetics in the Age of Consumer AI** — S.G. Finlayson, H.L. Rehm — *NEJM AI*, 2026 (*Heidi Rehm new articles* feed). Perspective piece on consumer-AI reinterpretation of genomic data. *Watch for:* the framing — if it discusses consumer-LLM-based reinterpretation of VUS, that's directly on the variant-interpretation + LLM-augmented-phenotyping intersection. Rehm + Finlayson coauthorship signals a substantive perspective rather than an opinion piece.

---

## SKIP / noise (logged, no action)

- **Australian Adaptation of Resources to Communicate Hereditary Cancer Risk With Family Members** (Zeng self-feed, position 2) — communications-research adaptation paper. Self-feed false positive.
- **Outcomes of a Canadian real-world cohort of metastatic castration-sensitive prostate cancer patients stratified by early PSA nadir** (Zeng self-feed, position 1) — real-world prostate-cancer outcomes. Off the cardiometabolic / AD / multimorbidity threads despite the RWE framing. Self-feed leak.
- **Functional analysis of germline RUNX1 variants identified in individuals with suspected familial platelet disorder** (Zeng self-feed) — RUNX1 / familial platelet disorder / CHIP-adjacent. Light **CHIP-thread interest** but the specific paper is variant-functional-analysis, not population epi; lower than HIGH.
- **Sex-stratified polygenic risk scores for coronary artery disease incidence: Insights from a 20-year cohort study** (Zeng self-feed) — sex-stratified CAD-PRS in a Middle East cohort (Tehran Lipid). On the cross-ancestry PRS axis but small-cohort and methods-light. Worth glancing only if writing a cross-ancestry PRS review.
- **ORIGIN-1 trial: organoid-guided N-of-1 trial for CFTR modulator response in rare non-F508del CF** (Zeng self-feed) — CF trial protocol. **CFTR / CF interest** but is a trial protocol, not data; reserve for when results land.
- **Associations of testosterone, SHBG, and related hormones with cancer risks in men** (Zeng self-feed, IPD meta-analysis in Lancet Healthy Longevity) — off-thread (cancer / endocrinology). Self-feed leak.
- **Conformational cycling of the Wntless transporter drives trafficking and secretion of Wnt morphogens** (Tiffany Callahan related-research feed) — Wnt-pathway molecular biology. Off the KG-construction thread (which is what Callahan's feed normally surfaces); molecular-biology leak.
- **Severe Antenatal Presentation of a Novel Dnase2 Mutation in a Preterm Omani Neonate** (Kastner related-research) — rare interferonopathy case report. Off-thread for population epi.
- **An optimised lipid nanoparticle platform enables efficient CRISPR/Cas9 genome editing in hard-to-transfect cells** (Shendure related-research) — LNP CRISPR delivery. Off-thread.
- **Cross-sectional and prospective associations between multidimensional psychological distress and urogenital disorders: findings from the UK Biobank** (UK Biobank keyword) — psychological-distress × urogenital epi. Off the genetic / phenotyping / pharmacoepi axes.
- **Stem cell-derived extracellular vesicles for rare diseases** (rare diseases keyword) — therapeutic mechanism paper. Off the rare-disease *diagnostic/phenotyping* axis your INTERESTS file calls out.
- **Hypoxic CA9 variant as a potential prognostic marker in gastric and breast cancers** (Denny citations) — Mizo-population cancer-pathway variant analysis. Off-thread.
- **Frontier of Multi-Modal Fusion: A Systematic Review of Knowledge Graph-Guided Generative Augmentation** (knowledge graph keyword) — 8th consecutive window of non-biomedical KG hits. See pipeline note below.
- **Believing Women with Autoimmune Diseases: Correcting Testimonial Injustice in Healthcare** (autoimmune keyword) — humanities perspective. Off-thread.
- **Pharmacogenomic Stratification for Oncology Drug Repurposing: An Exposure Target Context Eligibility Framework** (drug repurposing keyword) — oncology PGx framework; off the EHR-evidence-loop drug-repurposing pattern your INTERESTS file emphasizes.
- **Mendelian Randomisation paper on COPD and lung cancer via blood metabolites** (mendelian diseases keyword) — this is the chronic "mendelian diseases" keyword leak to MR (carry-forward, 8th consecutive window).
- **Cardiovascular Genetic Epidemiology in the Genome-Wide Era: From Association Discovery to Mechanistic Dissection and Clinical Translation** (Jian Yang citations) — narrative review; useful as a citation when writing review-tier material on CVD genetic epi, but no novel data.
- **Clonal hematopoiesis of indeterminate potential in high grade B-cell lymphomas** (CHIP keyword) — molecular CHIP × lymphoma association paper. On the CHIP thread tangentially but is single-cell-multiomics mechanistic, not population epi. Light read at most.
- **AI-Driven Biostatistics in Healthcare** (Foundation models + EHR keyword, 06-21 batch) — survey / framing chapter. Skip.
- **OTULIN / autoinflammatory / Wendy-Chung-feed RNase-deficiency etc.** (multiple SKIP-tier autoinflammatory and rare-Mendelian alerts in Wendy Chung / Daniel Kastner / Shendure feeds) — molecular / case-report tier; off-thread for population work.
- **MetaboNet-Bench: A Multi-modal Benchmark for Glucose Forecasting in Type 1 Diabetes** (Michael Snyder new articles) — T1D forecasting benchmark. Off-thread (T2D is on your threads via the chronic-disease clustering line; T1D is not).
- **Adverse events HPV vaccine post-marketing surveillance China** (Patrick Ryan related-research) — non-OHDSI / non-TTE pharmacovigilance. Off-thread methodologically.
- **Multiple LLM-evaluation / LLM-safety papers in Szolovits / Luo / Natarajan / Zou / Zitnik feeds** (e.g., Sethi et al. critical-care board questions; Azamfirei "correct enough"; Castagno synthetic-tabular-data systematic review; Maheswaran "Foundry" host-owned trust; Yan "Unified Energy for Invariant and Independent Decoding") — broad LLM-safety / LLM-architecture papers without clinical-decision hook. SKIP.
- **OTULIN catalytic-uncoupling Nature Immunology paper** — carry-forward from 06-20 SKIP list; surfaced again in citation feeds this window. Confirmed SKIP.
- **Patient-Reported Experiences With Viewing and Understanding Test Results in Patient Portals** (Hripcsak feed) — patient-portal communications. Off-thread.
- **Heidi Rehm SARS-CoV-2 mRNA vaccine in kidney transplant recipients** (Chute related-research) — COVID vaccine immunogenicity in transplant. Off-thread.
- **Pyoderma gangrenosum / autoinflammatory mechanism papers** (Kastner related-research carry-forward) — off-thread.

---

## Suggestions for the pipeline

Carry-forward issues from prior reports stand; today's items add three
new observations:

1. **Pipeline health check.** The 06-21 → 06-23 runs all completed; the
   06-20 fetch failure does **not** appear to be recurring. The 5-second
   client delay + 15-second inter-category pause look adequate. **De-
   prioritize** the "doubling the inter-category pause" suggestion from
   06-20 unless 06-24 also drops categories. (Worth checking: is the
   "previously surfaced, suppressed" message in the 06-21 digest doing
   the right thing? — i.e., dedup on arXiv ID, not on title.)

2. **`knowledge graph` keyword: 8th consecutive window of non-biomedical
   hits** (today: Ebadinezhad & Adeshina KG-guided generative
   augmentation survey). Specific fix from 06-20 still stands: change to
   `biomedical knowledge graph` OR `clinical knowledge graph` OR a
   compound filter `(knowledge graph) AND (medical OR biomedical OR
   clinical OR EHR OR phenotype OR drug OR disease)`.

3. **`mendelian diseases` keyword: 8th consecutive window of MR-paper
   leaks** (today: Cao et al. COPD + lung cancer two-sample MR).
   Specific fix: rename the keyword from `mendelian diseases` to
   `mendelian disease` OR `mendelian disorder` to avoid the
   `mendelian randomi[s/z]ation` leak, or use the compound
   `mendelian (disease OR disorder) NOT randomization`. Carry-forward.

4. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds**
   (carry-forward, unaddressed). Today's items #1 (Toyli JAHA), #2
   (Castillo Morales Nature Genetics), #3 (Chen TimeX npj Health
   Systems), #4 (Powell npj Dementia), #5 (Hansen eClinicalMedicine),
   #6 (Shen npj Digital Medicine), #7 (DB CRMM medRxiv), #10 (Shang
   AJKD), #11 (Ngo NAR) are all journal venues unreachable by the
   current arXiv-only digest. Item #7 in particular is a *medRxiv preprint*
   surfacing only via Scholar — adding medRxiv polling would directly
   close this gap.

5. **Add `OMOP`, `phecode`, `target trial emulation` keyword check —
   confirm not silently misfiring.** Items #5 (Hansen), #8 (Muqeeth),
   #10 (Shang) all touch on phecode / OMOP / TTE concepts but did not
   surface via the arxiv-digest keyword pipeline (only via Scholar
   author feeds). Worth a one-time confirmation that the keyword
   matching is firing on these venues' arXiv preprints when they exist
   (some AMIA-Summits papers are also on arXiv).

6. **Add `LLM` AND (`EHR` OR `clinical notes` OR `phenotype`) keyword
   compound.** Items #3 (TimeX), #4 (Powell AD), #8 (Muqeeth) are all
   LLM × EHR papers — a coherent sub-pattern. Adding the compound
   keyword catches these directly without having to go through Scholar
   author feeds.

7. **Add `federated learning` AND (`EHR` OR `biobank`) compound.** Item
   #6 (Shen PEAL) and 06-20's Kundu sequential paper are both federated
   EHR — second consecutive window of federated-EHR signal. Worth a
   dedicated keyword.

8. **Add `multimorbidity` AND (`cardio-renal-metabolic` OR `cardiometabolic`
   OR `aging`) compound.** Items #1 (Toyli), #5 (Hansen), #7 (DB) all
   touch multimorbidity from different angles — a coherent
   cardiometabolic-multimorbidity sub-thread that warrants direct
   keyword coverage. Three hits in one window.

9. **Continue tracking your own self-citation + new-related-research
   feeds as the single highest-precision channels.** This window's two
   self-feed HIGHs (items #1 Toyli and #7 DB CRM-multimorbidity) confirm
   the channel quality. The 06-20 report's note on this — "keep both
   alerts as-is" — continues to hold.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 12 | (1) Toyli et al. UKB+AoU CVD/AD [Zeng self-feed], (2) Castillo Morales AD/ADRD GWAS [Denny+Yang, Nat Genet], (3) Chen et al. TimeX phenotype onset [Chute+Chung, npj Health Sys], (4) Powell et al. AD memory clinic + LLM [Hripcsak, npj Dementia], (5) Hansen et al. T2D aetiology subtypes + complications [Denny, eClinicalMed], (6) Shen et al. PEAL lossless federated EHR [Hripcsak, npj Digital Med], (7) DB et al. CRMM multimorbidity GWAS [Zeng self-feed, medRxiv], (8) Muqeeth et al. multi-LLM consensus for EHR-predictable trial eligibility [Brandt, AMIA], (9) Wu et al. generative-transformer pharmacovigilance EHR [Ryan, AMIA], (10) Shang et al. AKI electronic phenotype + staging + subtyping [Denny, AJKD], (11) Ngo et al. CATVariant integrated protein variant interp [Karczewski, NAR], (12) Murali et al. CF causal inference with misclassified exposures [arxiv-digest 06-23] |
| METHODS-WATCH | 8 | Anand TV causal graphical, Haderlein OMOP nationwide, Zhu et al. FM-guided synthetic EHR + tabular-FM-to-EHR pair, Beesley & Mukherjee MGI selection-bias case study supporting info, Knight ESRD-transferable-prediction dissertation, Anand et al. OMOP-CDE completeness for trial CDEs, Finlayson & Rehm NEJM-AI genomic reanalysis perspective |
| SKIP | ~30 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH), this window
delivers **twice the HIGH count** (12 vs 6) — driven by (a) a
disproportionately large 06-23 Scholar batch (35+ alerts in one
delivery), (b) two self-feed hits in the same window (rare), (c) two
double-feed hits (TimeX, Castillo Morales), and (d) a recovered arxiv-
digest pipeline producing one HIGH (Murali CF) after three windows of
sparse output. The recurring pattern from prior reports holds: Scholar
alerts deliver nearly all on-thread signal; the `arxiv-digest` pipeline
contributes one HIGH per ~4 days of running. The most actionable
pipeline change this report is **adding medRxiv polling** (item #7
Cardio-Renal-Metabolic multimorbidity GWAS reached you only via the
Zeng self-feed; medRxiv-source polling would have surfaced it directly).
