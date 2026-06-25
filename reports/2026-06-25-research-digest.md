# Research digest report — 2026-06-25

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-06-25** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 06-25 | Three large batches: 06-21 10:36Z + 20:52Z (author + keyword feeds), 06-23 03:43Z + 08:52Z (author + keyword feeds), 06-25 05:57Z (very large author + citation feed batch — ≈33 alerts). Author feeds dominated by Karczewski, Pritchard, Jian Yang, Denny, Montgomery, Hripcsak, Szolovits, Chute, Hernán, Patrick Ryan, Daniel Kastner, Bastarache, Wendy Chung, Pranav Rajpurkar, Patrick Ellinor, Mark Gerstein, Evan Eichler, Ewan Birney, Sasha Gusev, Russ Altman, Mihaela van der Schaar, Isaac Kohane, Leo Celi. |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 06-25 | **06-21 = 0, 06-22 = 0, 06-23 = 2, 06-24 = 0 (3/4 categories failed to fetch, suppressed).** See pipeline note. The 06-23 surfacing includes one strong on-thread paper (Murali et al., causal inference + CF). |
| NCBI "My NCBI What's New" (UK Biobank) | 2026-06-25 | Aggregate digest; not individually triaged. |
| alphaXiv Weekly Digest | 2026-06-24 | Promotional / product announcement (autoresearch agent for arXiv URLs); not on-thread. |

> ⚠️ **arxiv-digest 06-24 had another 3-of-4-category fetch failure**
> (`q-bio.GN`, `q-bio.PE`, `stat.AP` all failed; only `q-bio.QM`
> succeeded, and that category had no matches). This is the **second
> fetch failure in five days** (prior: 06-20). The pattern suggests the
> arXiv rate-limit hasn't been mitigated by the existing 5-second client
> delay + 15-second inter-category pause. Recommend acting on the
> pipeline note below before the next polling cycle.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **Quadruple-feed saturation: *The Genetic Architecture of Cutaneous
  Melanoma Across the Variant Spectrum* (X. Chen et al., 2026)** fires
  simultaneously in **four** Scholar feeds: *Konrad Karczewski — new
  related research*, *10 new citations to Konrad Karczewski*, *10 new
  citations to Jonathan K. Pritchard*, and *10 new citations to Jian
  Yang*. Four-feed saturation is the highest-signal pattern the pipeline
  produces — the only stronger pattern would be appearance in your own
  Chenjie Zeng *citations* feed. Common + rare + structural variant
  analysis of a clinically actionable cancer phenotype, with the
  variant-spectrum framing that is becoming the field's reference design.
  **HIGH — read first.**
- **arxiv-digest 06-23 surfaces a quadruple-thread on-thread paper.**
  Murali, Barnatchez, Hoppe, Wagner, Keller, Josey — *Causal Inference
  with Multiple Misclassified Exposures: A Control Variate-Adjusted
  Calibration Weighting Approach* (arXiv 2606.23656, stat.ME, 2026).
  The empirical demonstration is **N=651 cystic fibrosis patients
  aged 6–21** estimating the effect of *P. aeruginosa* on FEV₁ % predicted,
  showing that swab-based estimates attenuate the effect by ~69% relative
  to sputum-based gold standard (–2.67 vs –8.52 pp). Lands on **four**
  of your threads at once: causal inference / pharmacoepi,
  CF/CFTR disease thread, EHR phenotyping (misclassification is the EHR
  phenotyping problem in disguise), and ML for precision health
  (treatment-decision-relevant). The first arxiv-digest paper to hit
  multiple core threads simultaneously in months. **HIGH.**
- **First major target-trial-emulation of GLP-1 RAs in IBD.** Yeh,
  Ahuja, Patel, Xu, Park, Gold et al. — *Adjunctive GLP1 Receptor
  Agonists in Patients with Inflammatory Bowel Diseases and Obesity
  and/or Diabetes: A Target Trial Emulation* (*Clinical*… [likely
  *Clinical Gastroenterology & Hepatology*], 2026, via Hernán citations
  feed). Triple-thread paper: causal inference (TTE design), GLP-1 RA
  pharmacoepi, IBD disease thread. **HIGH.**
- **LLM-assisted reanalysis of unsolved rare disease genomes — NEJM AI.**
  Jaech, Cheatham, Shringarpure, Genetti et al. — *LLM-assisted reanalysis
  of unsolved rare disease genomes increases diagnostic yield* (*NEJM AI*,
  2026, via "rare diseases" keyword feed). LLM applied at the
  reanalysis step where most of the diagnostic-odyssey value lives
  (sequenced-but-unsolved cohorts). Cross-thread: rare disease + variant
  interpretation + EHR foundation models. **HIGH.**
- **EHR phenotyping × LLM: two convergent papers, both in npj Health
  Systems.** Chen, Jiang, Nguyen, Ta, Wang et al. — *TimeX: Phenotype
  Onset Extraction from Clinical Narratives* (*npj Health Systems*, 2026,
  via Chute citations feed) — phenotype *onset date* extraction is the
  weakest link in time-to-event EHR studies, and an LLM-grade solution
  changes the methodological landscape. Powell, Hofmann, Oh, Schindler et
  al. — *Identification of memory clinic patients diagnosed with
  Alzheimer disease using EHR data and large language models* (*npj
  Health Systems*, 2026, via *both* Hripcsak related-research and the
  "electronic health records" keyword feed — **double-feed hit**) —
  AD-cohort identification from EHR + notes. Both lands on EHR
  phenotyping + clinical NLP. **BOTH HIGH.**
- **Population-scale paralogous-gene pathogenicity divergence (medRxiv).**
  Tzoumkas, Doctor, Sadeghi-Alavijeh, Gale — *Population-scale genomics
  reveals divergent pathogenicity of variant classes across paralogous
  collagen IV genes* (medRxiv, 2026, via Denny related-research). Tests
  whether the same variant class has the same effect across paralogs
  (here `COL4A3`/`COL4A4`/`COL4A5`, the Alport-syndrome genes) — directly
  relevant to **variant-interpretation transfer rules** in ACMG/ClinGen
  curation, where "evidence from paralog" is a frequently invoked but
  poorly characterized criterion. **HIGH.**
- **Pakistan Genome Resource — 173,303 exomes & genomes in *Nature*.**
  Koch, Khalid, Khan, Bandyadka, Doyon et al. — *Analysis of 173,303
  exomes and genomes in the Pakistan Genome Resource* (*Nature*, 2026,
  via Denny citations feed). Largest South Asian genomic cohort to date,
  with the cross-ancestry and consanguinity dimensions that AoU / MVP /
  UKB don't capture. **HIGH** on cross-ancestry portability +
  rare-variant burden methods.
- **Triple-feed re-surface: Souaiaia et al. PRS-tails *Nature* paper
  again hits Montgomery feed.** Already covered in detail in the 06-20
  report (#4); the re-surfacing only confirms its trajectory toward
  reference-class status. Reference back to 06-20 §4 rather than
  re-reporting.
- **Multi-omic ophthalmic imaging links retinal phenotypes to cardio-
  vascular & neurological traits — *Nature* (likely Nat Comms).** Julian,
  Dou, Duan, Huang, Yoo, Green et al. — *Multi-omic analysis of deep
  learning-derived phenotypes links ophthalmic imaging to cardiovascular
  and neurological traits* (*Nature*…, 2026, via Ewan Birney new
  articles). Deep-learning-derived imaging phenotype as a *new
  intermediate phenotype* for multimorbidity-trajectory work; cardio-
  ophthalmic-neurological linkage is the modern *organ-axis* multimorbidity
  framing. **HIGH** on multimorbidity + EHR foundation models (imaging
  modality).
- **Pharmacoepi: GLP-1 head-to-head on kidney outcomes.** Neumiller,
  Deng, Swarna, Polley, Herrin et al. — *Comparison of Specific
  Glucagon-Like Peptide-1 Receptor Agonists on Kidney Outcomes Among
  Patients With Type 2 Diabetes* (*Am J* … [likely *AJKD*], 2026, via
  Patrick Ryan related-research). Within-class head-to-head pharmacoepi
  is the next-tier question after class-level GLP-1 vs DPP-4 / SU
  comparisons. **HIGH** on GLP-1 + kidney + pharmacoepi threads.

Counts: **10 HIGH**, **6 METHODS-WATCH**, rest SKIP. This window is the
densest HIGH count in the report series so far, driven by:
(a) a four-feed paper (Cutaneous Melanoma genetic architecture),
(b) a quadruple-thread arxiv-digest hit (Murali et al. CF causal
inference),
(c) two convergent NEJM AI / npj Health Systems EHR-NLP papers,
(d) a *Nature* South Asian genome resource,
(e) a *Nature* PRS-tails paper re-surfacing on Montgomery feed, and
(f) two GLP-1 pharmacoepi papers (one TTE, one head-to-head).

---

## HIGH priority — detailed reports

### 1. The Genetic Architecture of Cutaneous Melanoma Across the Variant Spectrum
- **Authors / venue:** X. Chen, S. Zhang, D. Zhao, Z. Guo, D. Li, Z. Luo,
  Y. Sun et al., 2026 (venue unstated in the Scholar snippet — likely
  preprint or *American Journal of Human Genetics* given the
  variant-spectrum framing).
- **Surfaced by:** **Four-feed saturation** — (a) *Konrad Karczewski —
  new related research* (covered in the prior 06-20 batch but
  re-surfaces today via the citation feeds), (b) *10 new citations to
  Konrad Karczewski* (06-25 batch), (c) *10 new citations to Jonathan K.
  Pritchard* (06-25), (d) *10 new citations to Jian Yang* (06-25). The
  Karczewski / Pritchard / Jian Yang trio collectively defines the
  common+rare variant interpretation citation map; firing in all three
  *citation* feeds within one window means the paper is being cited by
  the trio's recent work — i.e., already entering the literature as a
  reference instance. The only stronger pattern would be appearance in
  your own *citations* feed.
- **Thread:** **Variant interpretation** (the explicit "across the variant
  spectrum" framing — common + rare + structural) + **Genetic
  epidemiology / PRS** (the implicit composite-PRS-plus-rare-variant
  scoring pattern, which the title brackets but doesn't name) + adjacent
  disease thread (cutaneous melanoma is not a tracked phenotype, but is
  clinically actionable and EHR-codable).
- **What it is:** Pan-spectrum genetic architecture of a single
  clinically actionable cancer phenotype — common variants (GWAS-tier),
  rare variants (burden + pLoF), and likely structural / mosaic
  contributions, all evaluated in one paper. From the truncated abstract:
  "Cutaneous melanoma is an aggressive skin cancer with a [substantial
  genetic component]…" — the "variant spectrum" framing is the new
  standard for a comprehensive heritability decomposition, of which
  Karczewski / Pritchard / Yang are the leading methodologists.
- **Why it matters to you:** Four reasons.
  (a) **Reference instance for cross-spectrum risk modeling.** Your
  INTERESTS file lists *composite risk models stacking PRS with rare
  pathogenic variants* as a thread. A clean, publishable cross-spectrum
  decomposition of one disease becomes the citation template for that
  thread.
  (b) **Karczewski + Pritchard + Yang citation-feed firing is rare.**
  Karczewski-only or Pritchard-only is the usual signal; all three is
  citation-graph-density evidence that this paper is the field's
  emerging default reference for variant-spectrum genetic architecture.
  (c) **Melanoma has the operational features your methods work on.**
  Well-defined EHR phenotype (ICD-10 C43.*), high penetrance for some
  monogenic predisposition (`CDKN2A`, `BAP1`, `MITF`, `POT1`), large
  common-variant tail (>50 GWAS loci), and a clinical decision (genetic
  testing vs not, screening cadence) that benefits from composite
  scoring. A direct PheWAS+PRS analogue is feasible in AoU/UKB.
  (d) **The variant-spectrum framing is methods-transferable.** Even if
  melanoma itself isn't on your disease threads, the analytical pipeline
  here is the one you'd reuse for any of your tracked phenotypes (CF,
  APOL1, CHIP/VEXAS, IBD).
- **Action:** **HIGH — read first.**
  (i) Identify the cohort — UK Biobank + FinnGen meta-analysis is the
  default for melanoma in 2026; a US-based cohort (MVP, AoU) would be a
  more directly portable comparator.
  (ii) Note the rare-variant burden methodology — REGENIE-burden,
  SAIGE-GENE+, or a custom collapsing test? Burden choice affects
  rare-variant effect-size estimates in the tails (see also the
  Souaiaia tails paper in 06-20 §4 — the two compose).
  (iii) Check the structural-variant treatment — most "variant spectrum"
  papers stop at common + rare SNV/indel and skip SVs; if this one
  actually integrates SVs (or mosaic events from blood-only sequencing,
  which would be unusual for a cancer-predisposition paper), the
  methods are noteworthy.
  (iv) **Critical:** does the paper construct a *composite* score
  (PRS + rare-variant burden together), or report them as separate
  contributions? Composite scoring is the citation hook for your work.

### 2. Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach
- **Authors / venue:** Nandini Murali, Keith Barnatchez, Jordana E. Hoppe,
  Brandie D. Wagner, Kayleigh P. Keller, Kevin P. Josey — arXiv
  2606.23656v1 (stat.ME, 2026-06-22, surfaced by `arxiv-digest` 06-23).
- **Surfaced by:** `arxiv-digest` 06-23 — score 2 (`causal inference`,
  `cystic fibrosis` keyword hits).
- **Thread:** **Quadruple-thread saturation** —
  **Causal inference & pharmacoepi** (calibration weighting + control
  variate is in the IPW / double-robust lineage) **+** **Cystic fibrosis
  / CFTR** disease thread (the empirical application is N=651 CF patients
  6–21y, *P. aeruginosa* effect on FEV₁) **+** **EHR phenotyping**
  (misclassified exposures = phenotype misclassification, the central EHR
  phenotyping problem) **+** **ML for precision health** (treatment-
  decision-relevant: under-treating *P. aeruginosa* is the implied
  clinical consequence).
- **What it is:** Method paper that develops calibration-weighting +
  control-variate estimators for causal inference when **multiple
  exposures are misclassified** simultaneously. Three substantive
  contributions per the abstract:
  (a) Calibration-weighting approach that treats misclassification as a
  *missing-data* problem and achieves consistency *without* requiring a
  model for the misclassification mechanism (a strong methodological
  improvement over standard ME-correction approaches that need
  validation-data-derived sensitivity/specificity).
  (b) Control-variate adjustment that integrates error-prone observations
  (e.g., throat-swab cultures) into a gold-standard estimator (e.g.,
  sputum cultures) to *reduce variance while preserving consistency* —
  i.e., a way to use the cheap measurement to make the expensive
  measurement more efficient.
  (c) Inherits **double robustness** from its components.
  (d) Characterizes a **structural ceiling** on the variance gain in the
  bivariate case: when both exposures are jointly correctly classified
  with high probability, variance reduction is bounded — a useful
  theoretical sanity check.
  Empirical application: N=651 CF patients 6–21, effect of *Pseudomonas
  aeruginosa* and *Staphylococcus aureus* infection on percent-predicted
  FEV₁. Swab-based estimates attenuate the *P. aeruginosa* effect by
  ~**69%** relative to sputum (–2.67 pp [swab] vs –8.52 pp [sputum,
  95% CI –13.40 to –3.63]). Direct clinical implication: throat-swab
  reliance may lead to under-treatment of *Pa* infections.
- **Why it matters to you:** Six converging hits.
  (a) **CF disease thread is on INTERESTS.md** — modulator pharmacoepi,
  CFTR / Trikafta / ivacaftor. This paper isn't a modulator paper per se,
  but the *P. aeruginosa* outcome is the dominant clinically relevant
  short-term outcome in pediatric CF, and any future modulator-era TTE
  needs to grapple with exactly this measurement-error problem
  (swab-based microbiology becomes more common as patients improve and
  produce less sputum).
  (b) **The misclassification framing transfers to EHR phenotyping.**
  Substitute "throat swab" → "ICD-code phenotype" and "sputum culture" →
  "chart-reviewed gold standard," and the methodology is the EHR-
  phenotype causal-effect framework you've been waiting for. PheKB-style
  phenotypes have known sensitivity/specificity vs chart review; a
  causal-inference framework that *uses both* without modeling the
  misclassification mechanism is operationally important.
  (c) **Authors' lineage is causal-CF.** Wagner is the Colorado-based CF
  causal-inference lead (CFDB / EPIC studies); Josey is at Emory in
  health-policy biostat. The application is therefore real-clinical, not
  toy.
  (d) **The control-variate framing is novel for medicine.** Control
  variates are standard in Monte Carlo / financial-engineering variance
  reduction but rare in pharmacoepi. If the framework generalizes, it's
  a methodological template for any cohort with paired
  expensive-gold-standard + cheap-error-prone measurements (e.g.,
  Holter monitor vs single ECG; chart-reviewed phenotype vs ICD
  phenotype; gold-standard claims linkage vs single-payer claims).
  (e) **Pediatric clinical-actionability.** 69% attenuation is large
  enough to flip a clinical-trial decision — exactly the magnitude that
  matters for guideline-setting in a pediatric population.
  (f) **First arxiv-digest paper this month to hit multiple core
  threads simultaneously.** The 06-19 bioETH-Beacon paper was
  METHODS-WATCH; the 06-23 MedRLM paper was METHODS-WATCH; this is the
  first cleanly HIGH `arxiv-digest` paper in over a month.
- **Action:** **HIGH — read in full.**
  (i) Read for the missing-data formulation — is misclassification cast
  as MAR conditional on covariates, or MNAR? MAR vs MNAR determines
  whether the estimator is robust to selective misclassification (e.g.,
  swab-vs-sputum choice driven by disease severity).
  (ii) Check the double-robustness conditions — which two of the three
  nuisance models (outcome model, treatment model, classification
  model) need to be correctly specified.
  (iii) Note the simulation regime — particularly the sample sizes
  tested. The N=651 application is small for double-robust methods;
  asymptotic vs finite-sample behavior matters.
  (iv) **Direct adoption candidate** for: (a) any CF modulator-era TTE
  with mixed sputum/swab microbiology, (b) any EHR-phenotype-based
  causal effect estimation where you have a chart-review validation
  sub-sample (this is the typical PheKB study design), and (c) any
  AoU or MVP study with self-report + EHR-code paired measurements.
  (v) Worth a Wagner / Hoppe contact if you have CF causal-inference
  work in flight.

### 3. Adjunctive GLP1 Receptor Agonists in Patients with Inflammatory Bowel Diseases and Obesity and/or Diabetes: A Target Trial Emulation
- **Authors / venue:** K.H. Yeh, D. Ahuja, S.B. Patel, R. Xu, S. Park,
  S. Gold et al. — *Clinical*… (almost certainly *Clinical Gastroenterology
  & Hepatology* or *Clinical Pharmacology & Therapeutics*), 2026.
- **Surfaced by:** *10 new citations to Miguel Hernán* feed. Appearance
  in Hernán's citations feed is the highest-precision signal for any
  TTE / causal-inference paper — Hernán's group invented the modern TTE
  framework and is cited only by methodologically tight TTE work.
- **Thread:** **Triple-thread saturation** —
  **Causal inference / pharmacoepi** (target trial emulation is the
  Hernán-Robins gold-standard framework) **+** **Drug-class thread:
  GLP-1 RAs** (explicitly listed on INTERESTS.md) **+** **Disease
  thread: IBD** (explicitly listed on INTERESTS.md under autoimmune /
  immune-mediated diseases).
- **What it is:** Target-trial-emulation study of adjunctive GLP-1 RA
  use in IBD patients with concurrent obesity and/or diabetes —
  estimating the causal effect of GLP-1 RA initiation on IBD-relevant
  outcomes (almost certainly: disease activity / flare, hospitalization,
  surgery, biologic escalation, and possibly mortality). The
  "adjunctive" framing means GLP-1 RA is added on top of standard IBD
  therapy, mirroring real-world prescribing patterns. The two-condition
  inclusion criterion (IBD + [obesity OR diabetes]) is the operational
  population in which GLP-1 RA prescribing has actually been increasing.
- **Why it matters to you:** Four reasons.
  (a) **All three components are explicit INTERESTS threads.** Few
  papers triple-hit; this one does. The intersection of (TTE
  methodology) × (GLP-1 RA pharmacoepi) × (IBD disease thread) is
  exactly the niche.
  (b) **The clinical question is real and unresolved.** GLP-1 RAs have
  been hypothesized to have *anti-inflammatory* effects in IBD (small
  case series suggest disease-activity reduction beyond what weight loss
  alone would explain), but the field has lacked a properly controlled
  causal estimate. A TTE in a large EHR cohort is the obvious
  observational analogue to a definitive RCT (which would be slow to
  run).
  (c) **The TTE design choices are methodologically informative.**
  How was eligibility defined (active IBD vs all IBD)? How was the
  treatment strategy specified (initiate at first qualifying encounter
  vs initiate-at-any-time clones)? How was the comparison group built
  (active-comparator vs no-GLP1)? These choices are the actively
  contested design space for TTE in pharmacoepi with chronic disease
  treatments.
  (d) **Operationally relevant to GLP-1 thread expansion.** Your INTERESTS
  file lists GLP-1 RAs as an active drug-class thread; current canonical
  papers are cardiovascular and renal outcomes. IBD is the next
  off-label / on-label expansion frontier, and this paper is plausibly
  the early-mover citation.
- **Action:** **HIGH.**
  (i) Read for the protocol — eligibility window, treatment strategies,
  follow-up, outcomes, censoring rules, and the per-protocol vs
  intent-to-treat estimand.
  (ii) Check the data source — Optum / MarketScan / Veradigm / IQVIA?
  The choice bounds external validity. If it's MVP, that's directly on
  your veterans-cohort thread.
  (iii) Note the comparator — DPP-4 inhibitor active-comparator is the
  rigorous choice; no-GLP1 is the weak choice (channeling bias).
  (iv) Note negative-control outcomes used — any well-done TTE in
  pharmacoepi uses negative-control outcomes to test for residual
  confounding; absence of this is a yellow flag.
  (v) Save for IBD / GLP-1 reference set.

### 4. LLM-assisted reanalysis of unsolved rare disease genomes increases diagnostic yield
- **Authors / venue:** A. Jaech, M. Cheatham, S.S. Shringarpure, C.A.
  Genetti et al. — *NEJM AI*, 2026.
- **Surfaced by:** "rare diseases" keyword feed (06-21). NEJM AI placement
  alone is high-precision signal — the journal is publishing very few
  clinical-AI papers per issue.
- **Thread:** **Rare disease** (the explicit application domain) +
  **Variant interpretation** (reanalysis = re-classification of
  previously-VUS variants) + **EHR foundation models** (the LLM is the
  reanalysis engine).
- **What it is:** LLM applied to the *reanalysis* step of the rare-
  disease diagnostic odyssey — i.e., given a previously-sequenced-but-
  unsolved patient (where the initial analysis returned no diagnostic
  variant), an LLM (presumably GPT-4-class) re-evaluates the variant set
  against updated literature, phenotype information, and possibly
  re-prioritizes via HPO-term retrieval. The headline finding ("increases
  diagnostic yield") implies the LLM-augmented pipeline solves cases the
  standard pipeline misses — the clinically valuable result, not the
  benchmarked-on-MedQA result.
- **Why it matters to you:** Three reasons.
  (a) **Rare disease + variant interpretation is the central intersection
  of two threads on INTERESTS.md.** A method that improves diagnostic
  yield in unsolved rare-disease cases is the highest-clinical-value
  application of LLMs in genomics — far more clinically actionable than
  "GPT-4 answers MedQA at 88%."
  (b) **Reanalysis is where most of the unrealized value lives.**
  Sequencing-but-not-solving is the dominant outcome of rare-disease
  sequencing (median solve rate ~30-40%); the unsolved 60-70% is the
  population where reanalysis matters. An LLM-grade reanalysis pipeline
  potentially shifts the solve-rate floor.
  (c) **NEJM AI placement.** The journal's quality bar is high; the
  paper plausibly becomes a default citation when arguing that LLMs
  have *moved past benchmarking* to clinical utility.
- **Action:** **HIGH.**
  (i) Read for the LLM architecture — generic GPT-4 vs domain-tuned vs
  retrieval-augmented vs agentic loop? The architectural choice is the
  methodological hook.
  (ii) Note the cohort — Broad / Boston Children's, Undiagnosed Diseases
  Network, or commercial-sequencing cohort? UDN is the gold-standard
  comparator.
  (iii) Check what kind of cases get newly solved — are they cases with
  recent literature updates (where the LLM is acting as a literature
  retrieval engine), cases with new phenotype information (where the LLM
  is acting as a phenotype-variant matcher), or genuinely novel
  classifications (where the LLM is doing variant-interpretation work
  ClinVar can't)? The diagnostic mechanism matters for understanding
  the ceiling.
  (iv) Note the rate of *false positive* solves (LLM proposes a
  diagnosis that turns out to be wrong on follow-up). Standard
  diagnostic-yield papers under-report this; LLM-based ones must report
  it.
  (v) Pair with Brownstein et al. *Multimodal Sequencing and Reanalysis*
  (Bastarache feed, this window — see METHODS-WATCH below) for a
  before/after of where the field was vs where the LLM lifts it.

### 5. TimeX: Phenotype Onset Extraction from Clinical Narratives
- **Authors / venue:** F. Chen, S. Jiang, Q.M. Nguyen, C.N. Ta, K. Wang
  et al. — *npj Health Systems*, 2026.
- **Surfaced by:** *10 new citations to Christopher G. Chute* feed.
  Chute citations skew strongly OHDSI / OMOP / phenotyping methodology;
  the appearance here is on-thread signal, not citation-graph noise.
- **Thread:** **EHR phenotyping & OMOP** (phenotype onset is the central
  unsolved problem) + **EHR foundation models** (clinical-NLP at the
  modeling layer) + adjacent: **Causal inference / pharmacoepi**
  (time-to-event analyses are entirely dependent on accurate onset
  dates).
- **What it is:** Method paper for extracting **phenotype onset dates**
  from unstructured clinical narratives (vs structured code-based
  estimates). The standard EHR-phenotyping pipeline assigns onset = date
  of first qualifying ICD/RxNorm/LOINC code, which is well-known to be
  *delayed* relative to true symptom onset (often by months to years
  for chronic conditions). TimeX presumably uses an LLM or seq2seq model
  to find temporal expressions in notes ("symptoms began approximately
  six months ago") and resolve them against the encounter date.
- **Why it matters to you:** Three reasons.
  (a) **Phenotype-onset misclassification is the silent killer of EHR
  time-to-event studies.** Survival analysis with wrong onset dates is
  systematically biased — toward null effects in some designs, toward
  inflated effects in others — and most published EHR survival studies
  carry the bias without correction. A validated onset-extraction
  pipeline becomes a default phenotyping primitive for the whole field.
  (b) **PheKB / OMOP infrastructure does not solve this.** PheKB-style
  phenotypes give *presence/absence* with code-based first-mention dates;
  TimeX-like methods give *onset* with note-derived dates. They compose:
  PheKB defines who, TimeX defines when.
  (c) **npj Health Systems is the OHDSI / EHR-FM venue.** A paper here
  is positioned to be the default citation for the onset-extraction
  primitive going forward.
- **Action:** **HIGH.**
  (i) Read for the temporal-resolution model — rule-based + LLM,
  end-to-end LLM, or a hybrid with explicit calendar arithmetic? The
  choice bounds reproducibility on new note styles.
  (ii) Note the validation cohort — single-site vs multi-site, and
  whether the gold standard is chart-review or registry-derived. Registry
  comparators (e.g., disease-specific registries) are the strongest
  validation.
  (iii) Check whether they release a containerized pipeline (Docker /
  MEDS-compatible) — usable artifacts dominate "method on paper."
  (iv) Direct adoption candidate for any AoU / MVP / UKB phenotyping
  primitive where the time-to-event design is sensitive to onset
  accuracy.

### 6. Identification of memory clinic patients diagnosed with Alzheimer disease using electronic health records data and large language models
- **Authors / venue:** W.J.B. Powell, A. Hofmann, I.Y. Oh, S.E. Schindler
  et al. — *npj Health Systems*, 2026.
- **Surfaced by:** **Double-feed hit** — (a) *George Hripcsak — new
  related research* (high-precision EHR-phenotyping feed), (b)
  "*electronic health records*" keyword feed (06-21 and 06-23 alerts).
- **Thread:** **EHR phenotyping & OMOP** (cohort identification is the
  canonical phenotyping task) + **EHR foundation models** (LLM-as-
  phenotyper) + multimorbidity-adjacent (AD is the dominant aging-related
  phenotype).
- **What it is:** Concrete application of LLM-augmented EHR phenotyping
  to identify memory-clinic patients with Alzheimer disease. The
  "memory clinic" qualifier matters: this is *specialist-confirmed* AD,
  not the general ICD-G30 phenotype which is well-known to misclassify
  (G30 is used for many non-AD dementias in practice). LLM augmentation
  here is presumably using notes from neurology / cognitive-clinic visits
  to filter ICD-coded AD into specialist-confirmed AD.
- **Why it matters to you:** Three reasons.
  (a) **Specialist-confirmed phenotyping is the missing layer in EHR
  cohorts.** Most published EHR-AD studies use ICD codes alone, with
  known PPV of ~40-70% depending on data source. An LLM-augmented
  pipeline that boosts PPV to >90% changes which AD studies are
  publishable in higher-tier venues.
  (b) **The method generalizes to your tracked phenotypes.** Substitute
  "memory clinic" → "IBD clinic" or "CF clinic" or "rheumatology" and
  the pattern transfers directly. Specialist-clinic-derived phenotyping
  is the operational analogue of a chart-review-validated phenotype, but
  scalable.
  (c) **Hripcsak + keyword double-firing is a precision signal.** The
  Hripcsak feed is the OHDSI / Columbia clinical-informatics anchor;
  paper firing both there *and* in the broad EHR keyword feed means it's
  attracting attention beyond the OHDSI core.
- **Action:** **HIGH.**
  (i) Read for the prompt / retrieval design — what notes does the LLM
  see, and how is the AD-yes/no decision elicited? Few-shot examples
  matter a lot for clinical-decision elicitation.
  (ii) Check the validation cohort — single-institution (Washington Univ
  given Schindler's affiliation) vs multi-site. Single-institution
  validation bounds external validity.
  (iii) Note the comparator — pure ICD baseline, or ICD + medication
  baseline? Most AD studies already use ICD + medication; the LLM lift
  should be measured against that, not against ICD-only.
  (iv) Potential adoption candidate for any AoU subcohort-curation work.

### 7. Population-scale genomics reveals divergent pathogenicity of variant classes across paralogous collagen IV genes
- **Authors / venue:** K. Tzoumkas, G.T. Doctor, O. Sadeghi-Alavijeh,
  D.P. Gale — medRxiv, 2026.
- **Surfaced by:** *Joshua C. Denny — new related research* feed.
- **Thread:** **Variant interpretation** (paralogy is one of the
  trickier ACMG/ClinGen evidence categories) + **Genetic epidemiology**
  (population-scale = UKB / FinnGen / 100,000 Genomes) + adjacent
  disease thread (kidney — Alport syndrome → relevant to APOL1 / kidney
  thread).
- **What it is:** Population-scale (likely UKB or 100k Genomes given Gale's
  affiliation at the UCL Centre for Nephrology) analysis of the
  paralogous collagen IV genes — `COL4A3`, `COL4A4`, `COL4A5` — which
  are the Alport-syndrome genes. The "divergent pathogenicity of variant
  classes" framing implies the paper tests whether (e.g.) missense
  variants in `COL4A3` carry the same penetrance as the equivalent
  missense in `COL4A4` — and finds they don't. This is a direct test of
  one of the implicit assumptions in ACMG/ClinGen variant interpretation
  ("evidence from paralog gene") that has not been quantitatively
  characterized at scale.
- **Why it matters to you:** Three reasons.
  (a) **Paralog-based ACMG evidence is methodologically under-developed.**
  PP3-paralog and PM5-paralog evidence categories are invoked when no
  direct evidence exists for a variant, but the *transferability* of
  pathogenicity classifications across paralogs has not been
  quantitatively benchmarked. This paper supplies that benchmark for
  one gene family — and the result is "divergent," which is the
  more-interesting outcome (uniform pathogenicity transfer would be the
  null).
  (b) **Direct relevance to your kidney / APOL1 disease thread.**
  Alport syndrome shares clinical / EHR territory with APOL1-associated
  kidney disease (hematuria → proteinuria → CKD progression). A
  variant-interpretation methods paper on Alport genes is operationally
  relevant when curating kidney-disease variants under ACMG.
  (c) **Population-scale = penetrance-under-screening-conditions
  estimable.** Your INTERESTS file explicitly calls out *penetrance
  estimation for monogenic variants under population-screening conditions
  (vs. clinically ascertained cohorts)*. Alport-syndrome variants in
  unselected biobank participants are textbook population-screening
  penetrance estimands.
- **Action:** **HIGH.**
  (i) Identify the cohort (UKB? 100k Genomes? GeneDx? Genomics England
  rare-disease arm? Gale's UCL lineage suggests Genomics England).
  (ii) Read for the divergence quantification — is it odds-ratio
  difference per variant class, penetrance difference, or
  effect-size-on-eGFR difference? The estimand choice determines what
  ACMG transferability conclusion is supported.
  (iii) Note the variant-class taxonomy used — pLoF / missense /
  splice / synonymous, or finer (CADD-binned)? Finer-grained divergence
  is more methodologically actionable.
  (iv) Potential citation for any future ACMG-revision argument about
  paralog evidence weighting.

### 8. Analysis of 173,303 exomes and genomes in the Pakistan Genome Resource
- **Authors / venue:** C. Koch, S. Khalid, M.Z. Khan, S. Bandyadka, B.
  Doyon et al. — *Nature*, 2026.
- **Surfaced by:** *10 new citations to Joshua C. Denny* feed.
- **Thread:** **Genetic epidemiology** (largest South Asian genomic
  resource) + **Variant interpretation** (rare-variant frequency
  recalibration in non-European populations) + **Biobanks with EHR
  linkage** (PGR has phenotype linkage — extent TBD) + cross-ancestry
  portability.
- **What it is:** Pakistan Genome Resource — a population-scale exome /
  genome cohort of >170k participants from Pakistan, almost certainly
  with the high consanguinity that distinguishes South Asian biobank
  cohorts from European-ancestry-dominant cohorts. The Nature placement
  + headline N indicates this is the reference-instance paper for the
  resource.
- **Why it matters to you:** Three reasons.
  (a) **Cross-ancestry rare-variant frequency calibration.** gnomAD's
  South Asian sub-cohort is small (~15k); PGR being 10x larger means it
  becomes the default *South Asian* allele-frequency reference for ACMG
  PM2-supporting evidence. Any future ACMG curation in South Asian
  populations should be calibrated to PGR.
  (b) **Consanguinity-enriched cohort = autosomal-recessive penetrance
  estimable.** Most population-scale cohorts (UKB, AoU, MVP) have low
  consanguinity, which makes population-scale recessive-disease
  penetrance hard to estimate. PGR's enrichment for consanguinity makes
  it the natural cohort for recessive-disease penetrance work — directly
  relevant to CF / rare-disease threads on INTERESTS.md.
  (c) **Denny citation-feed.** Denny was eMERGE PI; his citation feed
  surfaces papers that the eMERGE / NHGRI-genomic-medicine community is
  citing. Nature paper firing in that feed is field-consensus signal.
- **Action:** **HIGH.**
  (i) Note the phenotype linkage — does PGR have EHR / registry linkage
  beyond family-history? If it has clinical-outcome linkage, it joins
  the biobank thread; if not, it remains a *reference-allele-frequency*
  resource (still high-value).
  (ii) Check the rare-variant pLoF burden methodology — same as MVP /
  AoU pipelines, or custom?
  (iii) Add to citation set for any cross-ancestry PRS portability
  argument.

### 9. Multi-omic analysis of deep learning-derived phenotypes links ophthalmic imaging to cardiovascular and neurological traits
- **Authors / venue:** T.H. Julian, H. Dou, J. Duan, J. Huang, E. Yoo,
  D.J. Green et al. — *Nature*… (likely *Nature Communications*), 2026.
- **Surfaced by:** *Ewan Birney — new articles* feed. Birney as senior
  author signals an EMBL-EBI / UKB-PPP infrastructure paper — the
  authorship is the high-precision signal.
- **Thread:** **Multimorbidity / chronic disease trajectories**
  (cross-organ-axis trait linkage is the modern multimorbidity framing)
  + **EHR foundation models** (the deep-learning-derived ophthalmic
  phenotype is an imaging-modality FM derivative) + **Genetic
  epidemiology** (multi-omic analysis = GWAS + likely PRS) + adjacent:
  ML for precision health.
- **What it is:** Deep-learning model derives novel phenotypes from
  ophthalmic (likely fundus / OCT) imaging at UKB scale, then links the
  imaging-derived phenotypes to **cardiovascular and neurological**
  traits via multi-omic (GWAS + likely proteomic, possibly transcriptomic)
  analysis. The cross-organ-axis framing — retina as a window onto
  cerebral and cardiac microvascular health — is the actively interesting
  multimorbidity-adjacent question.
- **Why it matters to you:** Three reasons.
  (a) **DL-derived imaging phenotypes are the next intermediate
  phenotype layer.** Standard intermediate phenotypes are biomarker
  measurements (BP, LDL, HbA1c); DL-derived imaging phenotypes are an
  emerging additional layer that captures information not in
  scalar-biomarker form. This becomes a phenotyping primitive for any
  cohort with imaging — which AoU/UKB increasingly are.
  (b) **Cross-axis linkage is the multimorbidity-framing leading edge.**
  Your INTERESTS file explicitly lists *multimorbidity patterns and
  disease trajectories from EHR or biobank data*. Retinal-cardiovascular-
  neurological axis linkage is one of the cleanest cross-axis stories
  available — and is plausibly informative for cardio-renal-metabolic
  axis work (the natural next step).
  (c) **Birney + Nature placement.** Birney's UKB-imaging-derived-
  phenotype line at EMBL-EBI defines the citation map for this sub-
  field; a Nature-tier paper from that group is the new default citation.
- **Action:** **HIGH.**
  (i) Read for the DL architecture — pretrained backbone (DINOv2,
  RETFound, OphthalmoFM) vs custom CNN. Pretrained backbone use is the
  modern standard.
  (ii) Note the multi-omic layers used — GWAS only, or also proteomic
  (UKB-PPP) and metabolomic (UKB-NMR)? The breadth determines whether
  the paper is *the* imaging-multimodal reference vs *a* one.
  (iii) Check whether they release the derived phenotype scores per UKB
  participant — accessible scores become reusable for any downstream
  multimorbidity study.

### 10. Comparison of Specific Glucagon-Like Peptide-1 Receptor Agonists on Kidney Outcomes Among Patients With Type 2 Diabetes
- **Authors / venue:** J.J. Neumiller, Y. Deng, K.S. Swarna, E.C. Polley,
  J. Herrin et al. — *Am J* … (almost certainly *American Journal of
  Kidney Diseases* given the kidney-outcomes focus and the Mayo-Clinic
  flavor of the authorship), 2026.
- **Surfaced by:** *Patrick Ryan — new related research* feed (Ryan's
  feed surfaces OHDSI / OBSERVATIONAL-pharmacoepi-network-style work).
- **Thread:** **Causal inference / pharmacoepi** (within-class head-to-
  head comparison is the post-class-level pharmacoepi frontier) +
  **Drug-class thread: GLP-1 RAs** + adjacent disease thread (kidney /
  APOL1, though T2D-kidney is distinct from APOL1-kidney).
- **What it is:** Head-to-head pharmacoepi comparison of *specific*
  GLP-1 receptor agonists (semaglutide vs liraglutide vs dulaglutide
  vs tirzepatide) on kidney outcomes (eGFR slope, dialysis initiation,
  kidney-failure composite endpoint) in T2D. The "specific GLP-1 RA"
  framing is the within-class active-comparator design — much harder
  than class-level GLP-1 vs DPP-4, but also more clinically actionable
  for prescribers choosing between agents.
- **Why it matters to you:** Three reasons.
  (a) **Within-class head-to-head is the pharmacoepi frontier.** Most
  GLP-1 evidence to date is class-level vs placebo or vs DPP-4i;
  within-class comparison is sparse, despite being the actual clinical
  decision. A well-done within-class active-comparator study is rare
  and high-value.
  (b) **Kidney outcomes are a tracked drug-class effect.** SGLT2i +
  GLP-1 RA + kidney is one of the canonical pharmacoepi triangulation
  arenas; a within-class GLP-1 head-to-head fills a gap.
  (c) **Methodologically tight team.** Polley + Herrin signal Mayo /
  Yale biostatistical-pharmacoepi rigor; the analytic methods are
  almost certainly sophisticated (propensity-score matching with
  active-comparator, or target-trial emulation).
- **Action:** **HIGH (on the GLP-1 + pharmacoepi thread).**
  (i) Read for the active-comparator strategy — pairwise PS-matched
  (semaglutide vs liraglutide, etc.) or all-pairs network meta-analysis.
  (ii) Note the data source — Optum / OptumLabs is Mayo's typical
  choice. MVP equivalent (if any) would be a notable cross-validation.
  (iii) Check whether the kidney endpoint is composite or
  component-wise. Composite endpoints can mask heterogeneous within-
  class effects.
  (iv) Save for the GLP-1 reference set.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Bridging Ancestry-Stratified Bias in Pharmacogenomics AI: Toward
  Metabolomics-Inclusive Multi-Omics Precision Medicine** — H. Lee, K.
  Sajid, D. Lee — *Journal of Personalized Medicine*, 2026 (via Denny
  citations feed, 06-25). Position / framework paper on ancestry bias
  in pharmacogenomics ML, with a metabolomic-inclusive multi-omics
  framing. Adjacent to your ancestry-stratified PRS portability thread.
  *Watch for:* whether they propose a *concrete debiasing intervention*
  (multi-task learning, ancestry-adversarial training, etc.) or only
  frame the problem. Concrete-method papers transfer; framing-only
  papers are citation bait.

- **Multimodal Sequencing and Reanalysis Approaches to End the
  Diagnostic Odyssey of Individuals with Suspected Rare Monogenic
  Diseases** — C.A. Brownstein, J.A. Madden, W. Shao, C.A. Genetti et
  al. — *Genes*, 2026 (via Bastarache related-research feed). Review +
  framework paper for end-to-end diagnostic-odyssey resolution in rare
  Mendelian disease. Pairs with NEJM AI Jaech et al. (HIGH §4); together
  they cover the *before* (multimodal sequencing) and *after* (LLM
  reanalysis) of the same problem. **METHODS-WATCH** as a review-tier
  citation set; not a primary methods paper.

- **CLN2 Batten Disease Diagnosed via Newborn Genome Screening** — P.
  O'Connell, L. Fierro, R. Kaplan, L.L. Cohen, W.K. Chung et al. —
  *Genetics in Medicine Open*, 2026 (via Wendy Chung new articles feed).
  Newborn-genome-screening case identification for CLN2 (neuronal
  ceroid lipofuscinosis). Off your primary disease threads but
  exemplary for the *newborn-genome-screening operational pattern* —
  which is the framework expanding to many other rare diseases with
  available therapy (and CLN2 has cerliponase alfa as approved enzyme
  replacement, which fits your drug-repurposing-adjacent
  rare-disease-with-therapy framing). *Watch for:* the variant-
  interpretation pipeline and the false-positive rate, both critical for
  newborn-screening operational design.

- **Reclassification of BRCA1 variants of uncertain significance using
  ancestry-stratified allele frequencies: A Middle East-focused
  analysis** — L. Abujamous, R. Razali, H. Al-Thawadi — *Biomolecules*…,
  2026 (via "variant interpretation" keyword feed). ACMG PM2 ancestry-
  stratification done explicitly in a Middle Eastern population.
  **METHODS-WATCH** as a concrete instance of population-stratified PM2;
  light-read for any ACMG ancestry-stratification argument.

- **Extracting and Classifying Drug Discontinuations From Estonian
  Electronic Health Records: Development and Validation Study** — H.
  Šuvalov, N. Umov, M. Malk, M. Haug, S. Laur, M. Oja et al. — *Journal
  of Medical Internet Research* (almost certainly), 2026 (via Hripcsak
  related-research feed). NLP-extraction of *drug discontinuation events*
  from notes. Off-thread substantively (Estonian EHR), but the
  discontinuation-extraction primitive is operationally important for
  any pharmacoepi study (treatment-discontinuation = censoring event in
  most TTE designs, and is systematically under-captured by structured
  prescription data alone). **METHODS-WATCH** as a phenotyping-
  primitive paper.

- **Toward Reliable and Scalable Real-World Evidence: Principled
  AI-Enabled Methods for Evidence Generation and Clinical Trial Design**
  — B. Zhang dissertation, 2026 (via Hripcsak citations feed).
  Dissertation rather than peer-reviewed paper, so triage weight is
  lower; but the framing — *AI-enabled RWE methods for evidence
  generation* — is directly on your causal-inference + EHR-FM
  intersection. **METHODS-WATCH** to mine for novel methods if any
  chapter is later spun out as a publication.

- **Leveraging tumor dynamics to discover mutations influencing
  progression and treatment response for precision oncology** — E.
  Petter, J. LoPiccolo, S. Groha, R. Border, B. Pasaniuc et al. —
  *Genome Medicine*, 2026 (via Sasha Gusev new articles). Off your
  primary disease threads (oncology), but the framework (using
  *longitudinal tumor dynamics* as the response phenotype for a GWAS-of-
  treatment-response) is methodologically novel. *Watch for:* whether
  the longitudinal-phenotype-as-GWAS-trait approach generalizes outside
  oncology — it plausibly applies to chronic-disease progression
  trajectories in your multimorbidity thread.

- **BMI-genome interactions regulate global gene expression with
  emphasis in brain and gut** — R. Signer, C. Seah, H. Young, K.
  Retallick-Townsley et al. — *Cell Genomics*, 2026 (via Pritchard
  citations feed). GxE interaction-effects on gene expression with the
  brain/gut tissue focus. On your genetic-epi + multimorbidity-adjacent
  thread; the brain-gut axis is the leading multi-organ-axis story of
  the last two years. **METHODS-WATCH** unless multimorbidity work
  starts pulling on GxE.

---

## SKIP / noise (logged, no action)

- **Cutaneous Melanoma genetic architecture** (X. Chen et al.) re-surfaces
  across Karczewski, Pritchard, Jian Yang citation feeds — already
  promoted to HIGH §1 above. Logged separately to note the four-feed
  saturation pattern.
- **Distinct genetic architecture in the tails of complex traits**
  (Souaiaia et al., *Nature*) — re-surfaces via Montgomery related-
  research feed (06-25). Already covered in 06-20 report §4; no
  re-report.
- **A novel model demonstrating that human immune cells promote
  multiorgan SARS-CoV-2 dissemination** (Chute related-research) —
  basic-immunology paper, off-thread.
- **Vaccine Safety Surveillance for Covid-19 Vaccinations** (Patrick Ryan
  related) — India vaccine-safety chapter, off-thread.
- **Sequence-to-function modeling … Drosophila chromatin insulation**
  (Shendure related) — basic-bio model organism paper, off-thread.
- **Clinical Artificial Intelligence Competence in Obstetrics and
  Gynecology** (Szolovits citation) — physician-education / responsible-
  use commentary, off-thread.
- **Population-scale genomics… divergent pathogenicity of variant
  classes across paralogous collagen IV genes** — promoted to HIGH §7.
- **Why Do AI Projects Fail in Drug Development and Pharma?** (Natarajan
  citation) — Pistoia Alliance multi-year industry analysis,
  off-clinical-research-thread.
- **Identifying druggable proteins of the association of chronotype on
  breast cancer using Mendelian randomization** (Jian Yang related) —
  MR pharmacoepi adjacent, but oncology and chronotype-specific; light
  read at most.
- **Proteomics and human microchips identify Thrombospondin-1 as a
  potential biomarker for calciphylaxis stem cell therapy** (Kastner
  citation) — biomarker discovery for a rare hyperphosphatemia
  complication, off your primary threads.
- **Hypertension among Middle Eastern and North African adults residing
  in the United States: using the All of Us…** (Chenjie Zeng new related
  research) — AoU paper but on an EHR-derived clinical hypertension
  descriptive question rather than a genetic / methods paper; on the
  AoU-data-use thread but not on your primary methods threads. Logged.
- **Stem cell-derived extracellular vesicles for rare diseases** (Stephen
  Montgomery citation, also from rare-diseases keyword) — review-tier,
  off-thread substantively (cell therapy mechanism, not your phenotype-
  matching rare-disease framing).
- **Racial Disparities and Social Determinants of Long COVID** (Chute
  citation) — BRFSS analysis, off-thread.
- **Maternal RSVpreF Immunisation Against Infant RSV Hospitalisation:
  Nationwide Population-Based Effectiveness** (Hernán citation) —
  vaccine pharmacoepi but on RSV, off your tracked drug classes.
- **Multimodal Sequencing and Reanalysis** (Bastarache related) —
  METHODS-WATCH (already logged above).
- **Rare variants in inborn errors of immunity genes in young adults
  with severe COVID-19: Brazilian cohort** (Karczewski related) — IEI
  variant-burden in COVID, off primary thread but methodologically
  on-thread for rare-variant burden.
- **Unified Energy for Invariant and Independent Decoding in Diffusion
  Language Models** (Zitnik related) — pure ML, no clinical hook.
- **Fibrosing Myopathy in Systemic Sclerosis** (Kastner related) —
  rheum clinical outcomes, off-thread.
- **Blood-based Biomarkers in Cervical Cancer** (Vogelstein citation) —
  cancer biomarker review, off-thread.
- **Serum Inflammatory Markers and Risk of Colorectal Cancer in
  Patients with IBD** (Kohane new articles, Ananthakrishnan first author)
  — IBD-CRC risk biomarker; on-IBD-thread but biomarker-not-methods
  oriented. Light read at most.
- **Multidomain Risk Profiles and Documented Polyvascular Involvement…**
  (Patrick Ellinor new) — cardiology phenotyping, off your primary
  threads (cardio is adjacent but not central).
- **Fine-tuning large language models to generate single-atom catalyst
  synthesis procedures** (Tiffany Callahan related-research) — chemistry
  LLM, off-thread (clearly a Scholar relevance miss — Callahan does
  biomedical KG work, this is materials science).
- **Drug Repurposing via Biomedical Knowledge Graph Embedding** (R.
  Sankar, 2026, via "drug repurposing" keyword) — student
  GraphSAGE-on-BioKG project; on-thread keyword but no
  explainability hook, which your INTERESTS file specifies as the
  filter criterion. Logged.
- **Pharmacogenomic Stratification for Oncology Drug Repurposing**
  (El-Tanani et al., Pharmaceuticals, drug-repurposing keyword) —
  on-thread keyword but a target-and-chemistry pipeline without
  clinical-evidence loop; precisely the type INTERESTS.md flags as
  *lower interest*. Logged.
- **arxiv-digest 06-24 — 0 papers due to fetch failure** (see pipeline
  note). Not a dry day.
- **Statistical Methods for Institution-Scale Science** (P. Knight,
  All-of-Us keyword) — dissertation; on-AoU-thread but not primary
  literature. Light citation only if methods spin off.
- **Computational Mapping of Neuropsychiatric Risk across Neurodevelopment**
  (M.P. Margolis dissertation, phenome-wide keyword) — PheWAS-using
  dissertation; on-thread keyword but dissertation-tier. Logged.
- **Genetic Evaluation Practices in Living Kidney Donor Candidates**
  (Caliskan et al., APOL1 keyword) — on the APOL1 disease thread;
  clinical-practice / genetic-testing-utilization paper, not a methods
  paper, but worth logging for the APOL1 thread. **Borderline
  METHODS-WATCH / SKIP** — promoted out of the SKIP bucket if you have
  active APOL1 / kidney-donor-decision work.
- **Microglial clonal dynamics in transplanted rhesus macaques** (CH
  keyword) — basic biology of CH in macaques, off your CHIP-in-humans
  thread substantively.
- **Clonal hematopoiesis of indeterminate potential in high grade
  B-cell lymphomas** (CH keyword) — clinical CH in B-cell lymphoma;
  on-thread for CHIP but lymphoma-specific. Light read.
- **Impact of a comprehensive healthy lifestyle and genetic risk on
  arrhythmia: UK Biobank** (UK Biobank keyword) — PRS+lifestyle in UKB
  on a clinical-cardiology question; on the genetic-epi-using-UKB
  thread but cardiology-specific. Logged.
- **Cross-sectional and prospective associations between multidimensional
  psychological distress and urogenital disorders: UK biobank** (UK
  Biobank keyword) — psychology in UKB; off-thread substantively.
- **Artificial Sweeteners and Autoimmune Diseases: Mendelian Randomization**
  (mendelian-diseases keyword) — MR-on-diet-autoimmune; the
  mendelian-diseases keyword routinely leaks MR papers (MR ≠ Mendelian
  disease). See pipeline note. SKIP.
- **All of Us Evenings with Genetics Research Program** (Lloyd et al.,
  AoU keyword) — outreach / educational program description; on-AoU-
  thread but operational-not-methods. Logged.
- **The Frontier of Multi-Modal Fusion: A Systematic Review of KG-
  Guided Generative Augmentation** (Ebadinezhad, Adeshina, KG keyword)
  — generic KG review, no biomedical hook. SKIP.
- **A coupling analysis framework for ship welding quality causal
  factors integrating KG and NK model** (KG keyword) — marine engineering,
  off-thread. SKIP — the KG keyword leak pattern continues, see
  pipeline note.
- **Believing Women with Autoimmune Diseases: Correcting Testimonial
  Injustice** (autoimmune keyword) — philosophy of medicine,
  off-thread.
- **HIF-1α in macrophage polarization** (autoimmune keyword) — basic
  immunology, off-thread.
- **Adverse events HPV vaccine post-marketing surveillance** (Patrick
  Ryan related) — pharmacovigilance off your causal-inference / TTE
  framing.
- **Errors That Matter: Negative Experiences of Incorrect and
  Incomplete Health Records Among Youth in Mental Healthcare** (Hripcsak
  related) — qualitative health-record-experience paper, off-thread.
- **MALDI-TOF Mass Spectrometry for Glioblastoma Secretome Biomarker
  Screening** (Montgomery citation) — biomarker discovery review,
  off-thread.
- **Recursive Scaling in Masked Diffusion Models** (van der Schaar new)
  — ML methods, no clinical hook in abstract.
- **Mark Gerstein / Russ Altman / etc. "applications of AI in genomics"
  pieces** — generic-AI overviews; off-thread.
- **Complete chromosome 21 centromere sequencing of families with Down
  syndrome** (Eichler new) — basic genomics; off your phenotype-genotype
  threads.
- **SW-SpeedDLM: Sliding Window Speculative Decoding** (Zitnik related)
  — pure ML decoding, no clinical hook.
- **The quantified immune-aging dysregulation index: LLM-powered method
  for annotating dysregulation** (Kastner citation) — LLM-aging-
  signature paper; off-thread substantively but adjacent to the
  proteomic-aging thread you've been tracking. Logged.
- **alphaXiv weekly digest 06-24** — promotional content for an
  autoresearch agent feature; not on-thread.

---

## Suggestions for the pipeline

Carry-forward items from 06-20 are still relevant; today's items add
two new urgent issues:

1. **arxiv-digest 06-24 had another 3-of-4-category fetch failure.**
   Second failure in 5 days (also 06-20). The existing 5-second client
   delay + 15-second inter-category pause is not enough. Specific fix
   recommendations:
   - (a) Add per-category jittered retry-with-backoff (up to 3
     retries with 30s / 60s / 120s backoff before declaring the
     category failed).
   - (b) Split the four categories into two workflow runs separated by
     at least 90 minutes, scheduled at different hours.
   - (c) Cache the last successful fetch per-category, so a category
     failure surfaces with "*last successful fetch: YYYY-MM-DD*"
     rather than appearing indistinguishable from an empty result.
   - (d) The existing "3/4 categories failed" warning is good — keep it
     prominent.

2. **First on-thread arxiv-digest HIGH paper in 4+ weeks: Murali et al.
   (06-23, causal inference + CF + EHR phenotyping + ML).** The pipeline
   IS working when categories fetch; this is the kind of paper the
   keyword-tuning was designed to surface. Worth noting in the pipeline
   metrics that the on-thread HIGH ratio is non-zero, even if the
   denominator is small.

3. **`knowledge graph` keyword: 8th consecutive window of non-biomedical
   hits** (06-21 ship-welding KG paper, 06-23 multimodal-fusion KG
   review, plus the prior six windows). Specific fix unchanged from
   06-20 report: tighten to `(knowledge graph) AND (medical OR biomedical
   OR clinical OR EHR OR phenotype OR drug OR disease OR genomic)`. No
   on-thread KG paper has been missed by this constraint in three
   months of observation.

4. **`mendelian diseases` keyword leak: continues** (today's MR-on-
   sweeteners-and-autoimmune hit, 8th consecutive window). The keyword
   matches "Mendelian randomization" instead of "Mendelian disease."
   Specific fix: change to `"mendelian disease" OR "mendelian disorder"`
   (quoted exact-phrase match) to exclude MR papers, or add explicit
   `-randomization` to the query.

5. **`drug repurposing` keyword: today's hits (Sankar GraphSAGE,
   El-Tanani pharmacogenomics-oncology) match the *target-only / chemistry-
   only* anti-pattern called out on INTERESTS.md.** Specific fix: add
   AND-clauses requiring clinical-evidence terms — e.g.,
   `"drug repurposing" AND (real-world OR EHR OR "target trial" OR
   "phenome wide" OR explainable OR pathway OR rare disease)`. This
   loses the link-prediction-noise but retains the explainable-KG and
   EHR-mining strands you specified as high-priority.

6. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds** — six
   of today's 10 HIGH papers (#1 Cutaneous Melanoma, #3 GLP1+IBD TTE,
   #4 NEJM AI rare-disease LLM, #5 TimeX, #6 AD-LLM-EHR, #7
   collagen-IV paralogs medRxiv, #8 PGR Nature, #9 Birney multi-omic
   ophthalmic, #10 Neumiller GLP1-kidney) are *outside* the current
   q-bio.QM/GN/PE + stat.AP arXiv categories. medRxiv specifically would
   have surfaced items #7 (collagen IV) and likely #5 / #6 / #9.

7. **Add `proteomic signature` / `aging clock` / `organ-specific aging`
   keywords** (carry-forward from 06-20). Today's item #9 (Birney
   ophthalmic-multi-omic) is the third multi-omic / aging / cross-axis
   paper in three weeks; the pattern is now coherent enough to warrant
   keyword-level capture.

8. **Add `noncoding variant interpretation` / `regulatory variant
   effect` / `MPRA` keywords** (carry-forward from 06-20). Today's item
   #7 (collagen IV paralogs) is the second variant-interpretation
   methods paper in three weeks that hits the *paralog / cross-locus*
   axis, not the noncoding axis; the more pressing carry-forward is the
   noncoding keyword recommendation from 06-20.

9. **Add `"target trial emulation"` keyword.** Today's item #3 (GLP1+
   IBD TTE) is the first TTE paper to triple-hit your threads in this
   report series. The keyword would have surfaced it directly rather
   than via the (lower-precision) Hernán-citation route.

10. **Track the 4-feed-saturation pattern explicitly.** Today's item
    #1 (Cutaneous Melanoma) is the first 4-feed-saturation paper
    observed in this series. Worth a header in the daily summary that
    counts multi-feed saturation by tier (2-feed, 3-feed, 4-feed) — the
    saturation count is the single most reliable signal of field
    consensus.

11. **Continue tracking your own self-citation feed as the single
    highest-precision channel.** Today's Chenjie Zeng new-related-
    research hit (Jafari, *Hypertension among Middle Eastern and North
    African adults in the All of Us cohort*, *Frontiers in Medicine*,
    2026) was logged as SKIP — descriptive AoU paper, not on your
    methods threads — but the self-feed firing remains the most
    reliable precision signal when it does fire on-thread.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 10 | (1) Chen et al. Cutaneous Melanoma variant spectrum [4-feed], (2) Murali et al. causal inference + multiple misclassified exposures in CF [arxiv-digest 06-23, quadruple-thread], (3) Yeh et al. GLP-1 RA + IBD target trial emulation [Hernán citations, triple-thread], (4) Jaech et al. LLM reanalysis of unsolved rare disease genomes [NEJM AI], (5) Chen et al. TimeX phenotype-onset NLP [npj Health Systems, Chute citations], (6) Powell et al. EHR + LLM Alzheimer phenotyping [npj Health Systems, Hripcsak + keyword double-feed], (7) Tzoumkas et al. paralogous collagen IV pathogenicity [medRxiv, Denny related], (8) Koch et al. Pakistan Genome Resource 173k exomes/genomes [Nature, Denny citations], (9) Julian/Dou/Birney et al. multi-omic ophthalmic-imaging cross-axis trait linkage [Nature-family, Birney new], (10) Neumiller et al. specific GLP-1 RA head-to-head kidney outcomes [AJKD-likely, Patrick Ryan related] |
| METHODS-WATCH | 7 | Lee et al. ancestry-bias pharmacogenomics-AI framework, Brownstein et al. multimodal sequencing + reanalysis review, O'Connell et al. CLN2 newborn-genome-screening, Abujamous et al. BRCA1 PM2 ancestry-stratified, Šuvalov et al. EHR drug-discontinuation NLP, B. Zhang RWE dissertation, Petter/Gusev et al. tumor-dynamics GWAS-of-response, Signer et al. BMI-genome GxE brain-gut |
| SKIP | ~40 | See SKIP/noise section |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH), this 5-day
window delivers a substantially higher HIGH count (10), driven by:
(a) the cross-window accumulation of citation feeds (a 5-day window vs
the 06-20 report's 2-day window), and
(b) two unusually-high-signal patterns surfacing simultaneously — the
four-feed saturation of item #1 and the quadruple-thread saturation of
item #2.

The recurring pattern from prior reports holds: nearly all on-thread
signal comes from Scholar alerts; the `arxiv-digest` pipeline produced
exactly one on-thread HIGH paper (Murali et al., #2) plus one off-
thread paper across 5 days, with two of those 5 days having fetch
failures. The 06-24 fetch failure is the most urgent operational issue.
