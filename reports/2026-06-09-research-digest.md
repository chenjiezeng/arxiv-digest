# Research digest report — 2026-06-09

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-06-02 → 2026-06-09** (since the prior 2026-06-01 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-02 → 06-09 | Daily batches across `cezeng21@gmail.com`. Heaviest signal in the 06-09 author-alert batch (~30 author alerts) and the 06-09 keyword batch (~12 keyword alerts). |
| `arxiv-digest` repo (`digests/`) | 2026-06-02 → 06-08 | **Near-silent.** 06-02, 06-03, 06-07, 06-08 = 0 relevant; 06-06 = 2 (causal-inference + federated SPARQL). 06-03 again logged 3/4 q-bio fetch failures. Pipeline degradation has now persisted across three consecutive reports. |
| PubMed `efback@ncbi.nlm.nih.gov` MyNCBI saves | daily | `UK Biobank` and `drug repurposing` daily saved searches. High-volume, not individually triaged here — used to validate that journal-level signal isn't missed. |
| bioRxiv / medRxiv subject alerts | daily | Aggregate collection digests, not individually triaged. |

> ⚠️ The `arxiv-digest` GitHub pipeline is still degraded. **Three consecutive
> windows** with mostly empty digests + repeated q-bio category fetch failures.
> Continue to recommend fix to upstream-fetch retry-loop and expansion of
> source categories (see pipeline suggestions, prior report §1).

> Caveat: Scholar / PubMed alert emails contain title, authors, venue, and
> the first ~2-3 lines of each abstract. The reports below contextualize that
> metadata against the active research threads; nothing here reflects
> full-text reading. Where an alert is a duplicate of an earlier surfacing,
> noted inline.

---

## Executive summary

- **PheWAS-on-CNV blockbuster.** A *Nature*-class paper — *"Phenome-wide
  association of multiallelic copy number variation in 422,170 UK Biobank
  individuals reveals novel genetic loci associated with disease"*
  (Eisenberg, Packer, Shrine, Demidov et al.) — saturated the inbox,
  appearing in **four separate author alerts** (Karczewski, Bastarache,
  Denny, Jian Yang). Direct hit on your PheWAS / UK Biobank / genetic-epi
  thread; multiallelic CNV PheWAS is methodologically novel and almost
  certainly worth citing in your next PheRS / penetrance write-up.
- **CFTR review surfaced via your own author feed.** *"Cystic Fibrosis
  Transmembrane Conductance Regulator (CFTR) Dysfunction in Human Diseases:
  Molecular Mechanisms and Pathophysiological Implications"* (Rahman &
  Daira, *Cells*, 2026) appeared in your **Chenjie Zeng "new related
  research"** feed. Mechanism review, not pharmacoepi — useful as a
  background citation in your CFTR-modulator real-world-outcomes work.
- **GLP-1 in T1D — Lancet.** Lim, Pasternak, Eliasson, Pazzagli, Ueda —
  *The Lancet*, 2026 (surfaced via Patrick Ryan alert). Nationwide
  Swedish register study of GLP-1 RA + SGLT2i in **type 1 diabetes** (not
  T2D). On the GLP-1 pharmacoepi thread; off-label use in T1D is exactly
  the "real-world prescribing of GLP-1s beyond label" question that
  motivates several causal-inference framings.
- **CHIP cluster (4 papers).** Co-occurring CHIP + leukemia risk
  (*Nature Communications*, Barnao/Hubbard/Chan/Zhou), CHIP + mLoY ×
  heart failure dose-dependence (*European Journal of Heart Failure*,
  Weyrich/Ware/Windschmitt), CHIP + sepsis in ASPREE (*Leukemia*, Singh/
  Eisen/Byars/Leichter/Lacaze), and CHIP impact on ICI efficacy and AEs
  (Fujita et al.). Continues the strong post-2026-05 CHIP-outcome
  literature run — the dose-dependence paper is the most directly useful
  for composite-risk modeling.
- **APOL1 update in pediatric CKD.** Varner, Ilori, Gbadegesin —
  *Pediatric Nephrology*, 2026. Pediatric APOL1 + transplant outcomes,
  which extends the adult APOL1 transplant-decision literature you've
  been tracking. Surfaced through both the dedicated `APOL1` keyword
  alert and a Yuan Luo citation alert.
- **EHR ML for cardiac arrest.** Sharma, Brody, Friedman, Magoon et al. —
  *JACC: Advances*, 2026 (Pascal Brandt alert). AI-ECG + EHR fusion for
  out-of-hospital cardiac-arrest prediction. Squarely on the
  ML-for-precision-health thread (prediction tied to a clinical
  decision — who to monitor / escalate).
- **Target-trial emulation in pregnancy hypertension.** Atkinson,
  Lindquist, Tong, Hiscock et al. — labetalol vs nifedipine in pregnancy,
  using **TTE methodology** (Miguel Hernán "10 new citations" alert).
  Clean TTE example in a non-tracked disease — METHODS-WATCH.
- **Wrong-side imaging detection from EHR.** Kneifati-Hayek, Peabody,
  Baillie, Park et al. — *BMJ Open Quality*, 2026 (Hripcsak alert).
  EHR-derived computable phenotype for a *safety event*. METHODS-WATCH
  for the rule design.
- **Rare-disease genomic-diagnosis platform "G. AI".** Wang, Chen, Tang,
  Wu, Huang et al. AI-driven platform combining phenotype standardization
  + variant interpretation + structured clinical reporting. Hits three
  threads (rare disease + variant interpretation + HPO/phenotype
  standardization).

`arxiv-digest` pipeline this window: 2 papers total (causal-inference
external-control framework; federated SPARQL variant annotation KG). The
federated-SPARQL paper is on-thread (KG / variant annotation); the
external-control paper is off-thread but a clean methods read.

Counts: **11 HIGH**, **5 METHODS-WATCH**, rest SKIP. Detailed reports
below for each HIGH item.

---

## HIGH priority — detailed reports

### 1. Phenome-wide association of multiallelic copy number variation in 422,170 UK Biobank individuals reveals novel genetic loci associated with disease
- **Authors / venue:** M. Eisenberg, R. Packer, N. Shrine, G. Demidov, H. [et al.] — preprint/journal pending (likely *Nature*-tier given preprint pattern), 2026.
- **Surfaced by:** **4 separate author alerts** — Konrad Karczewski "new
  related research", Lisa Bastarache "new related research", Joshua C.
  Denny "new related research", Jian Yang "10 new citations". Saturation
  pattern matches the *"Distinct genetic architecture in the tails of
  complex traits"* paper from last window (6 alerts) — i.e., this is
  signal, not noise.
- **Thread:** PheWAS / phecode infrastructure **+** UK Biobank **+**
  genetic epidemiology (structural variation).
- **What it is:** PheWAS of **multiallelic** CNVs (i.e., CNVs that have
  more than two copy-state alleles in the population, as opposed to
  binary deletions/duplications) across the full 422,170-individual UK
  Biobank exome cohort. Identifies novel disease-associated loci where
  the per-copy-state effect is masked when CNVs are collapsed to a
  binary del/dup encoding.
- **Why it matters to you:** Direct hit on PheWAS infrastructure +
  biobank thread. Two technical reasons it's worth a careful read: (i)
  multiallelic CNV encoding is a more powerful test than binary CNV
  burden — useful template if you're considering CNV-aware phecode
  associations in AoU/UKB/BioVU; (ii) the saturation across Karczewski/
  Bastarache/Denny/Yang author alerts means this will rapidly become
  citation-required for any UKB-PheWAS work in 2026. Bastarache
  specifically is the canonical phecode author, so co-citation here is a
  near-certain pairing.
- **Action:** **HIGH** — read for the multiallelic encoding scheme,
  effect-size attenuation under binary collapsing, and any
  ancestry-stratified replication. Cross-check against your in-progress
  PheRS work to see whether multiallelic CNV would add signal beyond
  SNP-based PheRS.

### 2. Cystic Fibrosis Transmembrane Conductance Regulator (CFTR) Dysfunction in Human Diseases: Molecular Mechanisms and Pathophysiological Implications
- **Authors / venue:** M.S. Rahman, M. Daira — *Cells*, 2026.
- **Surfaced by:** **Chenjie Zeng "new related research"** alert (i.e.,
  Scholar links this to your prior CF/CFTR work).
- **Thread:** CF / CFTR disease thread.
- **What it is:** Mechanism-focused review of CFTR dysfunction beyond
  classic CF — explores CFTR involvement in non-CF diseases (likely
  pancreatic, hepatobiliary, and possibly cancer / inflammation
  pathways).
- **Why it matters to you:** Less directly actionable than a
  pharmacoepi or real-world-outcome paper, but two reasons to keep on
  the read pile: (i) "CFTR dysfunction in non-CF disease" is exactly the
  scientific frame for population-screening / repurposing discussions
  of CFTR modulators outside the CF label, which connects to your
  modulator pharmacoepi thread; (ii) Scholar identifying it as related
  to your published work confirms your CFTR work is being indexed in
  the mechanism-review citation graph, which is useful for tracking
  your citation footprint.
- **Action:** **HIGH (background)** — skim sections on non-CF CFTR
  involvement (chronic pancreatitis, CBAVD, COPD) for any cohort
  evidence; deprioritize the pure biochemistry sections.

### 3. Use of GLP-1 Receptor Agonists and SGLT2 Inhibitors Among Patients with Type 1 Diabetes: A Nationwide Register-Based Cohort Study
- **Authors / venue:** C.E. Lim, B. Pasternak, B. Eliasson, L. Pazzagli,
  P. Ueda — *The Lancet*, 2026.
- **Surfaced by:** Patrick Ryan "new related research" alert.
- **Thread:** Pharmacoepidemiology (GLP-1 RAs **+** SGLT2is, both
  tracked drug classes) **+** causal inference (off-label use,
  register-based real-world evidence).
- **What it is:** Swedish nationwide register study of off-label GLP-1
  RA and SGLT2i use among adults with type 1 diabetes — both classes are
  T2D-approved, but real-world prescribing in T1D is rising. Pasternak/
  Ueda group is well-known for nationwide-register pharmacoepi; *Lancet*
  publication implies a strong outcome-comparison design, almost
  certainly active-comparator + new-user with negative controls.
- **Why it matters to you:** Direct hit on **both** active drug-class
  threads (GLP-1 + SGLT2). Off-label use in T1D is the prototypical
  "real-world prescribing diverges from label" question your INTERESTS
  flags as core to the pharmacoepi thread. Likely a methodologically
  rigorous design you can cite for new-user / active-comparator framing.
- **Action:** **HIGH** — read for the cohort definition (how T1D was
  ascertained — labs vs ICD vs treatment-based), the active comparator
  choice, and outcome adjudication. Useful as a model for any future
  GLP-1-in-AoU work.

### 4. Update on APOL1 and chronic kidney diseases in children
- **Authors / venue:** J.D. Varner, T.O. Ilori, R.A. Gbadegesin —
  *Pediatric Nephrology*, 2026.
- **Surfaced by:** Both the dedicated `APOL1` keyword alert (06-08) and
  the Yuan Luo "10 new citations" alert (06-09) — i.e., the paper is
  being cited in adjacent EHR/biobank work.
- **Thread:** APOL1 disease thread (kidney disease risk, transplant
  decision-making, ancestry considerations).
- **What it is:** Review of APOL1 risk-allele biology and clinical
  implications **in pediatric CKD specifically**, with explicit
  attention to kidney transplant outcomes and pregnancy.
- **Why it matters to you:** Pediatric APOL1 is a relatively
  under-developed extension of the adult APOL1 transplant literature you
  track; pregnancy is also flagged in the snippet ("APOL1 have also been
  implicated in kidney transplant outcomes and pregnancy"). Worth
  reading because: (i) pediatric-onset penetrance is informative for
  the broader penetrance-in-population-screening question; (ii) it sets
  up framing for any future APOL1-PheWAS or PheRS work in AoU's
  pediatric cohorts.
- **Action:** **HIGH** — read for the pediatric penetrance numbers and
  whether the transplant section adds anything beyond the adult
  literature (Freedman, Reeves-Daniel, etc.).

### 5. Co-occurring clonal hematopoiesis exhibits strong selection and high leukemia risk
- **Authors / venue:** K.M. Barnao, A.K. Hubbard, I.C.C. Chan, W. Zhou
  et al. — *Nature Communications*, 2026.
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert
  (2026-05-25; flagging here because it was cross-referenced in the
  06-01 prior report and continues to be cited downstream).
- **Thread:** Clonal hematopoiesis (CHIP) — specifically composite /
  co-occurring CHIP variants.
- **What it is:** Population-scale analysis showing that **co-occurring
  CHIP** variants (i.e., a person carries multiple CHIP mutations) is
  not a chance pattern — there is positive selection for specific
  co-occurrences, and the co-occurring state confers substantially
  elevated leukemia risk.
- **Why it matters to you:** Compositive-CHIP signal is one of the
  cleanest analogues of your composite-risk modeling for monogenic +
  polygenic risk in other diseases. The selection-genetics framing
  (selection coefficients, fitness advantage) is informative if you're
  thinking about CHIP-PRS-as-exposure in PheWAS / MR contexts.
- **Action:** **HIGH** — full read for the selection-genetics framework
  and effect-size estimates; cross-reference with your composite-risk
  pipeline.

### 6. Independent and Dose-Dependent Contributions of Clonal Hematopoiesis and Mosaic Loss of Y to Incident Heart Failure
- **Authors / venue:** M. Weyrich, A. Ware, J. Windschmitt, T. Sarakpi
  et al. — *European Journal of Heart Failure*, 2026.
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert (06-04).
- **Thread:** CHIP **+** mLoY (somatic mosaicism) **+** cardiovascular
  outcomes.
- **What it is:** Cohort study quantifying **independent and
  dose-dependent** contributions of CHIP (typically by VAF stratum)
  and mLoY (typically by mLoY fraction) to incident heart failure.
- **Why it matters to you:** This is **directly** the kind of result
  that informs composite somatic-mosaicism risk modeling: separating
  CHIP-attributable from mLoY-attributable HF risk, with dose-response
  curves rather than dichotomous carrier status. Pairs with #1 in the
  prior report (Bick stroke meta-analysis, 800k individuals) and #4 in
  this report's prior window (CHIP + CV outcomes after HCT). Together,
  these three define the current state of CHIP-CV-outcomes evidence.
- **Action:** **HIGH** — read for the VAF / mLoY-fraction stratum
  definitions and the joint-model specification (additive vs
  interaction).

### 7. Sepsis risk associated with clonal hematopoiesis of indeterminate potential (CHIP): a secondary analysis of the ASPREE trial
- **Authors / venue:** J. Singh, D.P. Eisen, S.G. Byars, A. Leichter,
  P. Lacaze et al. — *Leukemia*, 2026.
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert
  (2026-05-31).
- **Thread:** CHIP **+** infection / sepsis outcomes (a non-CV
  outcome layer for CHIP).
- **What it is:** Secondary analysis of ASPREE (large
  aspirin-in-elderly RCT) examining whether CHIP carriers have elevated
  sepsis incidence on follow-up.
- **Why it matters to you:** Most CHIP-outcome papers anchor on CV or
  hematologic endpoints. Sepsis is a less-explored axis but plausible
  given CHIP's link to inflammation (IL-6, IL-1β). Useful as a
  non-redundant outcome when you build a CHIP-PheWAS / multi-outcome
  composite.
- **Action:** **HIGH** — read for the sepsis-ascertainment definition
  (likely ICD-based in ASPREE) and the magnitude of association vs the
  CHIP→CV effect sizes.

### 8. A real-world data analysis of the impact of clonal hematopoiesis of indeterminate potential on therapeutic efficacy and adverse events of immune checkpoint inhibitors
- **Authors / venue:** T. Fujita, N. Ishibashi, S. Aoyama, Y. [et al.]
  — 2026.
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert
  (06-03).
- **Thread:** CHIP **+** pharmacoepi (off-thread therapy class — ICI —
  but on-thread "CHIP modifies drug response").
- **What it is:** Real-world data analysis of CHIP carrier status as a
  modifier of immune-checkpoint-inhibitor (ICI) efficacy and adverse
  events.
- **Why it matters to you:** CHIP-as-treatment-effect-modifier is a
  thread emerging in 2026 — CHIP affects myeloid biology, which in
  turn affects ICI mechanism. Useful as background if you're thinking
  about heterogeneous treatment effects (HTE) where CHIP is a
  candidate modifier covariate. Off your tracked drug classes
  (GLP-1/SGLT2/CFTR/HRT), but methodologically transferable.
- **Action:** **HIGH (methods)** — read for the HTE / interaction
  analysis design; deprioritize the oncology-specific clinical
  takeaways.

### 9. Artificial Intelligence-Enhanced Electrocardiography and Health Records to Predict Cardiac Arrest
- **Authors / venue:** S. Sharma, J.A. Brody, S.F. Friedman, M.J.
  Magoon et al. — *JACC: Advances*, 2026.
- **Surfaced by:** Pascal Brandt "new related research" alert.
- **Thread:** Machine learning for precision health (prediction tied
  to escalation decision) **+** EHR phenotyping (EHR + waveform
  fusion).
- **What it is:** AI-ECG model fused with structured EHR data to
  predict cardiac arrest. ECG-only AI for arrhythmia / cardiomyopathy
  has matured (Attia/Friedman/Mayo lineage); the EHR-fusion angle is
  newer.
- **Why it matters to you:** Sits directly at the "ML for precision
  health tied to a clinical decision" sweet spot in your INTERESTS
  (who to monitor / escalate). Methodologically also a clean example
  of multimodal EHR FM input (waveform + codes) — relevant to your
  CLMBR/MOTOR thread if waveform tokens are being added.
- **Action:** **HIGH** — read for the multimodal fusion architecture
  (how waveform embeddings are tokenized alongside structured EHR) and
  any calibration / decision-curve analysis.

### 10. G. AI: an AI-driven platform for phenotype standardization, variant interpretation and structured clinical reporting in rare disease genomic diagnosis
- **Authors / venue:** Z. Wang, X. Chen, L. Tang, X. Wu, A. Huang, H.
  [et al.] — 2026.
- **Surfaced by:** "rare diseases" keyword alert (06-09).
- **Thread:** Rare disease **+** variant interpretation (ACMG/ClinGen)
  **+** EHR phenotyping (HPO / phenotype standardization).
- **What it is:** Integrated AI platform combining (i) HPO-based
  phenotype standardization from clinical narratives, (ii)
  variant-interpretation pipeline (likely ACMG-aware), and (iii)
  structured reporting output — i.e., end-to-end rare-disease genomic
  diagnosis.
- **Why it matters to you:** Three of your active threads converge in
  this platform (rare disease, variant interpretation, HPO-based
  phenotyping). Even if the specific tool isn't adopted, the
  architecture choices (LLM vs rule-based phenotype extraction;
  variant-classification rule encoding; report-template
  standardization) are directly transferable to any rare-disease
  diagnostic workflow you build.
- **Action:** **HIGH** — read for the phenotype-extraction NLP module
  and the ACMG rule encoding; cross-reference against InterVar /
  AnFiSA-style approaches.

### 11. Targeted reflex RNA sequencing for enhanced variant classification on exome and genome sequencing improves patient outcomes
- **Authors / venue:** X. Zhao, R. Rigobello, M. Driver, S. Lau, M.L.
  Chong et al. — *npj Genomic Medicine*, 2026.
- **Surfaced by:** "variant interpretation" OR "variant classification"
  keyword alert (06-09).
- **Thread:** Variant interpretation — specifically **splicing / RNA
  evidence for VUS resolution**, which your INTERESTS explicitly
  flags.
- **What it is:** Targeted **reflex** RNA-seq — i.e., RNA-seq triggered
  by a flagged DNA variant (likely a candidate splice variant or VUS)
  rather than run on every sample. Evaluates whether reflex RNA-seq
  changes ACMG classifications and (per snippet) patient outcomes.
- **Why it matters to you:** Direct hit on the "splicing / RNA
  evidence for VUS resolution" bullet under variant interpretation.
  Reflex (rather than universal) RNA-seq is the economically viable
  path for population-screening cohorts, so this is directly relevant
  to penetrance-estimation infrastructure.
- **Action:** **HIGH** — read for the reflex-trigger criteria and the
  reclassification-rate evidence (how many VUS resolved per RNA-seq
  run).

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **A comparison of the safety of oral labetalol versus nifedipine to
  manage hypertension in pregnancy in Australia: a target trial
  emulation** — Atkinson, Lindquist, Tong, Hiscock et al. — 2026.
  Surfaced via **Miguel Hernán "10 new citations"** alert, which is
  about as strong a TTE-quality signal as Scholar provides. Pregnancy
  hypertension is off-thread; the methodology is on-thread for the
  causal-inference / TTE bullet. **Watch for:** the eligibility-window
  definition, treatment-assignment rule, and time-zero anchoring.

- **GWAS of extended prescription analgesic use identifies genetic loci
  in chronic pain** — Harlow, Uzochukwu, Fernando, Mordaunt et al. —
  *Nature Communications*, 2026 (Jian Yang alert). Uses **prescribing
  data as the GWAS phenotype** (rather than self-reported pain), which
  is the same EHR-derived phenotype design you use in pharmacoepi work.
  **Watch for:** the prescription-based phenotype definition (how
  "extended" was operationalized) and whether they ran phecode
  comparisons.

- **Wrong-side imaging orders: automated detection using electronic
  health record data — a retrospective cohort study** — Kneifati-Hayek,
  Peabody, Baillie, Park, Gu et al. — *BMJ Open Quality*, 2026
  (Hripcsak alert). Safety-event computable phenotype with explicit
  EHR rule design. **Watch for:** the rule logic (probably
  laterality-mismatch between order text and prior imaging) — a clean
  template for any laterality-aware phecode work.

- **Theory and practice in biomedical informatics: a framework for
  discovery** — Stead, Aliferis, **Bastarache**, Lorenzi et al. —
  *JAMIA*, 2026. Bastarache co-author is the relevance hook. Framework
  / position piece, not a methods paper, but worth knowing for any
  methods-discussion citation.

- **From Data Stewardship to Model Stewardship: Extending Governance
  Frameworks for AI Era Health Data Use** — Rozenblit, Labkoff, Safran
  — *JMIR*, 2026 (Szolovits citation alert). Governance framing for
  AI-era health data — useful if/when you're writing the
  data-governance section of an AoU/BioVU grant.

---

## arxiv-digest pipeline papers (this window)

**2026-06-06 digest — 2 papers (both score-1):**

1. **Leveraging External Controls for Treatment Switching in Randomized
   Controlled Trials: A Weighted Causal Inference Framework for Overall
   Survival** — Shen, Fu, Lin (stat.ME). External-control + balancing-
   weights framework for treatment-switching adjustment in oncology
   RCTs. **METHODS-WATCH** — the synthetic-control + balancing-weights
   combination is reusable for any TTE-style off-label-use analysis you
   build (though the oncology setting is off-thread).
2. **Federated SPARQL querying for genomic variant functional
   annotation** — Bodrug-Schepers, Bourcier, Redon, Gaignard (q-bio.QM).
   Federated KG-based variant annotation against UniprotKB, avoiding
   public-data duplication. **HIGH (light)** — on-thread (variant
   interpretation + KGs/ontologies), but a workflow paper rather than a
   methods advance. Read if you're building any KG-based variant-
   annotation infrastructure; skip otherwise.

All other dates in the window (06-02, 06-03, 06-07, 06-08) returned
zero relevant papers; 06-03 logged 3/4 q-bio fetch failures (same
upstream issue flagged in the prior two reports).

---

## NOTABLE: AoU / UK Biobank conference-abstract clusters

The 06-09 keyword feeds pulled mostly **ADA Scientific Sessions 2026
abstracts** (Diabetes journal supplement). Same pattern as the AoU
ASCO 2026 cluster from the prior report — flagging titles for
awareness:

- **Health Score and Risk of Mild Cognitive Impairment and Dementia
  among People with Type 2 Diabetes: Findings from the All of Us
  Research Program** (You Lu, D. Li, Y. Yoshida) — AoU + T2D-MCI/
  dementia; medium for multimorbidity / aging-related multimorbidity.
- **1003-OR: The CEBPβ-XOR Axis and Genetic Risk for Metabolic
  Dysfunction-Associated Kidney Disease** (Kars, Ekperikpe, Itan,
  Daehn) — PheWAS-based diabetic-kidney-disease genetic risk; medium
  (specific kidney-disease GWAS).
- **2208-P: Early Detection of Type 1 Diabetes: The T1Detect Pilot
  Screening Program at Wayne Pediatrics** (Buggs-Saxton, Lally,
  Ismaeil) — autoimmunity screening; SKIP (clinical screening pilot,
  not on the methods thread).
- **1422-P: Integrating Lipoprotein (a) with Retinal Imaging
  Biomarkers for Cardiovascular Risk Assessment: UK Biobank Analysis**
  (Thakur, Seo, Nam, Jang, Nusinovici et al.) — UKB CV-risk
  biomarker-integration; medium for the composite-risk thread.

---

## SKIP / noise (logged, no action)

- **`arxiv-digest` repo:** see above — 4 of 7 days in window were
  empty, 1 day had partial fetch failures (06-03), 1 day yielded 2
  score-1 papers (06-06). Pipeline degradation noted for the third
  consecutive report.
- **"knowledge graph" keyword alert:** "PESatNet: Mitigating embedding
  saturation in knowledge graph recommendation via parameter-embedding
  synergistic enhancement" — recommender-systems KG, not biomedical.
  **4th consecutive week** of non-biomedical KG noise from this
  keyword. Pipeline fix (require biomedical co-occurrence) is overdue.
- **"mendelian diseases" keyword alert (06-08, 06-09):** caught two MR
  papers (drug-target MR for antihypertensives × intestinal ischemia;
  MR for asthma/rhinitis × dental caries). Same MR-vs-mendelian-disease
  keyword issue flagged in the prior report — still not fixed.
- **"autoimmune disorders/diseases" keyword:** ADA T1D screening
  abstract (above). Borderline-SKIP.
- **Daniel Kastner / PFAPA review** (Rigante, *Pediatric Research*,
  2026): periodic-fever syndrome conundrum. Off-thread; SKIP.
- **Citation churn (06-09):** Vogelstein (multi-cancer early
  detection FP review), Pritchard (PE3 functional-variant screening),
  Shendure (chromatin insulator biology), Zitnik (speculative
  decoding LLMs), Jian Yang (TLR7 COVID GWAS), Christopher Chute
  (wastewater epi), Leo Celi (education on digital platforms), David
  Sontag (older 2017 Rotmensch knowledge-graph paper), Karczewski
  (TLR7 COVID), Stephen Montgomery (immune biograph + cattle long-read
  RNA-seq), Vivek Natarajan ("Towards World Models in Biomedical
  Research"), James Zou (foundation-model image-segmentation
  adaptation), David Baker (de novo scaffold design dissertation),
  Michael Snyder (power-infrastructure imaging AI), Peter Szolovits
  (vision-language model RL self-improvement), Tiffany Callahan
  (counterfactual-generation w/ KGs over LLMs), Jian Ma (antibody RL
  design), Mihaela van der Schaar (LLM reasoning optimization). All
  routine citation feed; off-thread; SKIP.
- **Yuan Luo citation (Long COVID Persistence across 58 US Hospitals)
  was already flagged in the 2026-06-01 report** as METHODS-WATCH —
  not re-listed.
- **GLP-1 ocular AE meta-analysis (Anatriello et al.,** *Frontiers in
  Endocrinology***) via Hripcsak citation alert:** GLP-1 ocular
  adverse-event meta-analysis. Borderline — on the GLP-1 thread but
  meta-analysis-of-RWE rather than RWE itself. SKIP unless you're
  preparing a GLP-1 AE-spectrum review.
- **"Drug repurposing" — Khan & Jays, DeepPurpose + VEGFR2 in HCC** —
  target-only deep-learning pipeline without clinical-evidence loop;
  explicitly low-interest per INTERESTS. SKIP.
- **"Drug repurposing" — Thamanna & Chellapandi, network pharmacology
  oral-gut-lung axis** — network-pharmacology review without clinical
  evidence loop; SKIP per INTERESTS.

---

## Suggestions for the pipeline

Carrying forward from the prior two reports — these are now recurring
across **three consecutive windows**:

1. **`arxiv-digest` is in a degraded state.** 06-02, 06-03, 06-07, 06-08
   all empty (or empty-with-fetch-warning). Add the upstream-fetch
   retry-loop and broaden source categories (medRxiv / bioRxiv /
   `cs.LG` / `stat.ME` would catch most of the items above).
   *Repeat from prior report.*
2. **Tighten `apol1` matching to `\bapol1\b`** to suppress APOE false
   positives. *Repeat from prior report.*
3. **Tighten or split `mendelian diseases` keyword** (MR papers are
   still leaking through). *Repeat from prior report.*
4. **Require biomedical co-occurrence on `knowledge graph` keyword**
   (4th consecutive week of non-biomedical noise). *Repeat from prior
   report.*
5. **Add `proteome-wide` / `colocalization`** — recurring high-value
   shape. *Repeat from prior report.*
6. **Consider adding `copy number` / `CNV PheWAS`** as a tracked term
   if the Eisenberg UKB CNV-PheWAS paper (#1 above) anchors a new
   sub-thread.
7. **Drop or de-noise the `keyword: chip` short word-boundary rule**
   if `intitle:"clonal hematopoiesis"` is now the canonical CHIP
   source — `chip` standalone occasionally still produces silicon-chip
   false positives (e.g. the 2026-05-22 NVIDIA cooling-channel paper).
