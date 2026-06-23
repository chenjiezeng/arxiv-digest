# Research digest report — 2026-06-23

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML
for precision health, multimorbidity).

Window: **2026-06-02 → 2026-06-23** (since the prior 2026-06-01 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-02 → 06-23 | Multiple author + keyword batches; latest batches landed 06-23 03:43 UTC (Chute citations, Hripcsak related) and 06-23 08:52 UTC (`"clonal hematopoiesis"`, `"drug repurposing"` keyword feeds). |
| `arxiv-digest` repo (`digests/`) | 2026-06-02 → 06-23 | **Pipeline silent.** 06-02 = 0 relevant; 06-03 = 0 relevant with 3/4 categories failing (q-bio.QM, q-bio.GN, q-bio.PE); **no digest files after 2026-06-03** (last 20 days). |
| bioRxiv / medRxiv subject alerts | daily | Aggregate collection digests, not individually triaged. |

> ⚠️ **The `arxiv-digest` GitHub pipeline has produced no output for 20
> days.** Last committed digest is `2026-06-03.md`. The 06-03 run reported
> "3/4 categories failed to fetch (q-bio.QM, q-bio.GN, q-bio.PE)" — the
> same q-bio fetch failure flagged in the 06-01 report has persisted *and*
> the cron appears to have stopped emitting entirely after 06-03. Two
> things to check before the next cycle:
>   1. Why the nightly Action stopped producing commits after 06-03 (auth
>      expiry? workflow disabled? schedule changed?). Inspect run history
>      in Actions tab → *Daily arXiv digest*.
>   2. The persistent q-bio 429 / category-fetch failure — the politeness
>      retry loop in `scripts/arxiv_digest.py` is not enough; consider
>      lengthening the inter-category sleep or splitting q-bio into a
>      separate workflow with its own concurrency lane.
>
> Net effect on this report: no high-priority arXiv preprints from the
> repo for this window — only the *previously-surfaced* 05-27/05-28 batch
> (already covered in the 06-01 report). Below I include just the brief
> back-references for completeness.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. URLs in the bracketed `[scholar→ ...]` links resolve
> through Google's redirector.

---

## Executive summary

- **EHR phenotyping is the dominant cluster this window.** Five concrete
  items: TimeX (phenotype onset extraction from notes), an Alzheimer-from-
  EHR LLM identification paper, an OMOP transformation of a nationwide
  community-care DB, Beesley & Mukherjee's MGI selection-bias /
  phenotype-misclassification case studies, and Wu et al.'s generative-
  transformer pharmacovigilance signal-detection paper. TimeX and the
  Beesley/Mukherjee work are the two highest-priority — TimeX because
  onset timestamps are exactly the EHR-derived outcome problem you keep
  hitting in CFTR and CHIP work; Beesley/Mukherjee because their
  bias-reduction framework is directly importable to MGI-style biobank
  analyses.
- **EHR foundation models**: two AMIA Summits 2026 papers from the same
  group (Zhu, Zhou, Liang, Scherer, Xu …) on synthetic-EHR release and
  adapting tabular FMs to EHR — both relevant to your CLMBR / MOTOR /
  EHRSHOT lineage thread.
- **CHIP**: one new paper this window — Hesselager et al. in *Blood
  Cancer Journal* on CHIP in high-grade B-cell lymphomas, with single-
  cell multiomics. Augments the cancer-outcomes side of your CHIP thread.
- **Drug repurposing keyword feed**: 9 hits this window, mostly off-
  thread (chemistry/docking-only or single-pathogen). Two are worth
  noting: El-Tanani et al.'s pharmacogenomic exposure–target–context
  eligibility framework (a clinical-evidence framing, which fits your
  HIGH criterion); and Kang's MDD druggable-genome paper using
  direction-aware TWAS + colocalization for repurposing (a
  *clinical-evidence-loop* GWAS-to-repurposing pipeline, which is
  squarely your high-interest angle).
- **UK Biobank**: two new items — a UKB lifestyle × genetic-risk paper
  on arrhythmia (Yang et al., *BMC CV Disorders*), and a UKB
  psychological-distress × urogenital-disorders longitudinal paper (Liu
  et al., *Scientific Reports*). The arrhythmia paper is the more
  methodologically interesting (composite-risk PRS + lifestyle).
- **Causal / pharmacoepi**: a *Two-Sample MR* paper on COPD → lung
  cancer via blood-metabolite mediation (Cao et al.); fits your
  biomarker-as-exposure / MR scan thread.
- **Knowledge graphs**: one item — a herbal-drug network-pharmacology +
  KG paper on diabetes/obesity (Sil et al.); methodology is interesting
  but the herbal-pharmacology angle keeps this METHODS-WATCH rather than
  HIGH.
- **Variant interpretation**: CATVariant (Ngo et al., *Nucleic Acids
  Research*) — a web server integrating sequence/structure/population/
  clinical evidence for variant interpretation. Worth a look against
  your existing InterVar / VEP / LOFTEE stack.
- **Population cohort / pharmacoepi**: Gardner et al. in *AJOG* — 2.5M
  California births, hyperemesis-gravidarum → adverse-pregnancy
  outcomes. Off-thread disease-wise, but a clean large-cohort design.
- **Methods exemplar (METHODS-WATCH)**: PEAL (Shen, Kim, Luo, Zeger …)
  in *npj Digital Medicine* — lossless one-shot federated learning for
  multi-institutional EHR disease-progression analysis. Lossless +
  one-shot is the unusual claim worth verifying.
- **GitHub `arxiv-digest`**: no new signal this window beyond what the
  06-01 report already covered (BIRDNet KG paper, win-measure missing-
  data IPW/AIPW, semiparametric functional DiD). Pipeline is down — see
  warning box above.

---

## HIGH — directly serves an active research thread

### 1. TimeX: Phenotype Onset Extraction from Clinical Narratives
**Authors:** F Chen, S Jiang, QM Nguyen, CN Ta, K Wang …
**Venue:** *npj Health Systems*, 2026
**Source:** Scholar alert — Christopher Chute citations (06-23 03:43 UTC).
**Snippet:** "Disease phenotype onset is critical for timely and accurate
diagnosis and clinical decision-making, yet it remains poorly
characterized in the literature. Estimating phenotype onset using EHR
data holds promise but remains challenging. Researchers often resort to
EHR documentation timestamps as proxies for phenotype onset, which can
be inaccurate. Conventional NLP approaches suffer from limited
scalability and …"
**Why HIGH (threads matched: EHR phenotyping & OMOP; rare disease):**
Phenotype-onset estimation from notes — rather than first-mention
timestamps — is exactly the problem that bites CFTR modulator
eligibility analyses (when did pulmonary deterioration begin?) and CHIP
incidence work (when did the cytopenia start, vs. when it was coded?).
The framing as a scalable LLM-replacement for hand-built NLP fits the
"LLM-assisted phecode/HPO assignment" angle in `INTERESTS.md`. Recommend
reading full text before next CFTR-EHR analysis — onset definition is
typically the most leveraged decision in those study designs.

### 2. Case studies in bias reduction and inference for EHR data with selection bias and phenotype misclassification (MGI)
**Authors:** LJ Beesley, B Mukherjee
**Venue:** main paper + supplement, U. Michigan deepblue repo; surfaced
via supplement PDF.
**Source:** Scholar alert — George Hripcsak "new related research" (06-23 03:43 UTC).
**Snippet:** "In the main paper, we provide an overview of The Michigan
Genomics Initiative (MGI) dataset and provide detailed analyses. Here,
we include some additional information …"
**Why HIGH (threads: EHR phenotyping & OMOP; Biobanks with EHR linkage;
PheWAS / phecode infrastructure):** Beesley/Mukherjee have been the
methodological anchor for ascertainment-bias correction in MGI-style
recruited biobanks. A new case-studies paper from them is *directly*
importable to AoU/MVP/BioVU work where the same selection-bias +
phenotype-misclassification compound applies. This pairs naturally with
the PheRS / penetrance estimation problem flagged in INTERESTS.md
(population-screening vs. clinically-ascertained cohorts is exactly the
selection-bias structural problem). Pull the main paper, not just the
supplement.

### 3. OMOP common data model transformation: leveraging a nationwide community-based health care database to support AI/ML research
**Authors:** TP Haderlein, C Der-Martirosian, WP Bensken …
**Venue:** *JAMIA* (advance article, doi 10.1093/jamia/ocag087), 2026.
**Source:** Scholar alert — Hripcsak related-research feed.
**Why HIGH (threads: EHR phenotyping & OMOP):** Another nationwide
community-care OMOP build joins the AoU/MVP/BioVU pool — useful
reference for justifying CDM choices and for cross-CDM portability of
phecode-based outcome definitions. No abstract snippet available in the
alert; pull the JAMIA PDF for population characteristics and concept-
mapping fidelity numbers.

### 4. Identification of memory clinic patients diagnosed with Alzheimer disease using EHR data and large language models
**Authors:** WJB Powell, A Hofmann, IY Oh, SE Schindler …
**Venue:** *npj Dementia*, 2026.
**Source:** Scholar alert — Hripcsak related-research feed.
**Snippet:** "Alzheimer disease (AD) is a neurodegenerative disorder
marked by gradual decline in memory and thinking. New treatments for
early symptomatic AD have increased the need for early and accurate AD
diagnosis. This study aimed to identify which …"
**Why HIGH (threads: EHR phenotyping & OMOP; ML for precision health):**
LLM-based phenotyping for AD ties to a clinical decision (eligibility
for the new anti-amyloid agents), which moves this *out of* the generic-
benchmark SKIP bucket and into the HIGH bucket per the INTERESTS.md
rubric. A useful comparator for the LLM-vs-rules-based phenotype
extraction work you've been tracking.

### 5. Generative Transformers for Pharmacovigilance Signal Detection using Electronic Health Records
**Authors:** YF Wu, I De Boer, T Cohen
**Venue:** *AMIA Summits on Translational Science Proceedings*, 2026.
**Source:** Scholar alert — Hripcsak related-research feed.
**Why HIGH (threads: EHR phenotyping; Causal inference & pharmacoepi):**
Generative-transformer pharmacovigilance from EHR is squarely on your
pharmacoepi / GLP-1 / SGLT2i / Trikafta thread — particularly worth
contrasting with the established self-controlled case-series and
sequence-symmetry approaches you use. No abstract in the alert; pull
the AMIA proceedings PDF.

### 6. Foundation Model–Guided Synthetic EHR Release: Performance Enhancement with Privacy Preservation
**Authors:** R Zhu, X Zhou, I Liang, SW Scherer, K Xu …
**Venue:** *AMIA Summits on Translational Science Proceedings*, 2026.
**Source:** Scholar alert — Hripcsak related-research feed.
**Why HIGH (threads: EHR foundation models):** Synthetic-EHR release
gated by a foundation model speaks directly to the CLMBR / MOTOR
lineage. Worth assessing whether the privacy-utility tradeoff measured
here is comparable to what EHRSHOT-style downstream tasks tolerate.

### 7. Large Models for Small Tables: Adapting Tabular Foundation Models to EHR Data
**Authors:** R Zhu, X Zhou, I Liang, SW Scherer, K Xu … (same group)
**Venue:** *AMIA Summits on Translational Science Proceedings*, 2026.
**Source:** Scholar alert — Hripcsak related-research feed.
**Why HIGH (threads: EHR foundation models; ML for precision health):**
Adapting tabular FMs (TabPFN / TabFM style) to small EHR tables is the
under-served setting between full sequence FMs (MOTOR) and standard
GBMs. Pair-read with #6 above for an integrated take on the group's
2026 AMIA contribution.

### 8. Clonal hematopoiesis of indeterminate potential in high grade B-cell lymphomas: clinicobiological associations and further insight with single-cell multiomics analysis
**Authors:** C Hesselager, P Hollander, E Pettersson, G Enblad …
**Venue:** *Blood Cancer Journal*, 2026.
**Source:** Scholar alert — `intitle:"clonal hematopoiesis"` keyword feed (06-23 08:52 UTC).
**Snippet:** "Clonal hematopoiesis of indeterminate potential (CHIP) is
an age-associated condition linked to enhanced inflammation,
cardiovascular disease (CVD) and an inferior outcome in solid
malignancies. CHIP is defined as the presence of …"
**Why HIGH (threads: Clonal hematopoiesis (CHIP) and VEXAS):** Extends
the CHIP-and-cancer-outcomes literature into high-grade B-cell
lymphoma, with a single-cell multiomics layer. Complements the CHIP-
HCT meta-analysis flagged in the 06-01 report. Probably the single
most-on-thread paper this window for your CHIP work.

### 9. CATVariant: a web server for integrated protein variant interpretation across sequence, structure, population, and clinical evidence
**Authors:** K Ngo, H Amini, I Vorobyov, CE Clancy
**Venue:** *Nucleic Acids Research*, 2026.
**Source:** Scholar alert (snippet-only metadata in the digest).
**Why HIGH (threads: Variant interpretation (ACMG / ClinGen)):** Another
entry in the integrated VUS-interpretation tooling space (InterVar /
VarSome / Franklin / AnFiSA lineage). Worth a tooling-comparison note
for the ClinGen-VCEP guidance work — does CATVariant ingest splicing /
RNA evidence and ClinGen-VCEP-specific criteria, or is it a
sequence+population+structure only stack?

### 10. Pharmacogenomic Stratification for Oncology Drug Repurposing: An Exposure Target Context Eligibility Framework
**Authors:** M El-Tanani, AF Wali, SA Rabbani, Y El-Tanani …
**Venue:** *Pharmaceuticals* (MDPI), 2026.
**Source:** Scholar alert — `"drug repurposing"` keyword feed.
**Why HIGH (threads: Drug repurposing):** Framing repurposing through
*pharmacogenomic exposure–target–context eligibility* is a clinical-
evidence-loop approach (rather than target-only or chemistry-only) —
which is the angle INTERESTS.md flags as HIGH. The "eligibility
framework" framing also fits naturally with the target-trial-emulation
side of your causal-inference thread (eligible-population definition
mirrors a TTE protocol).

### 11. Colocalization Reprioritizes the Major Depressive Disorder Druggable Genome: Demotion of the Top TWAS Signal (DRD2) and Nomination of SLC12A5/FURIN/DCC by Direction-Aware, Confirmation-Gated …
**Authors:** B Kang
**Venue:** preprint (Research Square), 2026.
**Source:** Scholar alert — `"drug repurposing"` keyword feed.
**Snippet:** "…direction-aware drug repurposing, and summary-based
colocalization … This study integrated gene-mapping, brain transcriptome
imputation, and drug-repurposing … First, we performed systematic
direction-aware …"
**Why HIGH (threads: Drug repurposing; Genetic epidemiology):** TWAS +
colocalization + *direction-aware* repurposing — i.e., the repurposing
signal is gated by whether the perturbation direction matches the
disease-protective allele direction. This is exactly the kind of
explainable-rationale repurposing pipeline (path-rationale, not opaque
score) flagged as HIGH in INTERESTS.md. Single-author preprint though;
sanity-check the colocalization implementation.

### 12. Cross-sectional and prospective associations between multidimensional psychological distress and urogenital disorders: findings from the UK biobank
**Authors:** H Liu, L Liu, Z Zhao, X Liu, Y Cao
**Venue:** *Scientific Reports*, 2026.
**Source:** Scholar alert — biobank-feed.
**Why HIGH (threads: Biobanks with EHR linkage — UK Biobank):** A
straight UKB exposure-outcome paper; medium-priority because clinical-
question rather than methods, but on-cohort.

### 13. Impact of a comprehensive healthy lifestyle and genetic risk on arrhythmia: insights from the UK biobank study
**Authors:** Q Yang, X Lu, Y Lu, X Jiang, T Wang, C Guo
**Venue:** *BMC Cardiovascular Disorders*, 2026.
**Source:** Scholar alert — biobank-feed.
**Why HIGH (threads: Biobanks with EHR linkage; Genetic epidemiology;
ML for precision health):** PRS × lifestyle interaction in UKB
arrhythmia — a composite-risk-modelling design that fits your
PRS + rare-pathogenic-variant stacking thread. The methodology
(probably PRS quartiles × WHO lifestyle index) is conventional; useful
as a reference for how lifestyle-modifier strata are typically reported
on UKB arrhythmia outcomes.

### 14. Chronic Obstructive Pulmonary Disease Influence on Lung Cancer Risk Through Blood Metabolite Mediation: A Two-Sample Mendelian Randomisation and …
**Authors:** YN Cao, L Wang, HS Fan, ZJ Zhang
**Venue:** *International Journal of Chronic …*, 2026.
**Source:** Scholar alert — biobank-feed.
**Why HIGH (threads: Genetic epidemiology — Phenome-wide MR, biomarker-
as-exposure scans):** Two-sample MR with blood-metabolite mediation —
directly relevant to the biomarker-as-exposure scan thread. The
mediation-MR design is the methodologically interesting bit; check
whether they handle horizontal pleiotropy in the mediator-outcome leg
properly.

---

## METHODS-WATCH — off-thread disease, exemplary methods

### 15. PEAL: a lossless, one-shot federated learning solution for multi-institutional disease progression
**Authors:** Y Shen, JS Kim, C Luo, SL Zeger, RT Domsic, AA Shah …
**Venue:** *npj Digital Medicine*, 2026.
**Source:** Scholar alert — Hripcsak related-research feed.
**Snippet:** "Multisite analysis of EHR data presents unique
opportunities for studying disease progression in real-world settings.
However, privacy concerns, communication costs, and site-level
heterogeneity pose significant …"
**Why METHODS-WATCH:** *Lossless* + *one-shot* federated learning is a
strong pair of claims — if it holds, it would simplify N3C-style multi-
site analyses considerably. Worth verifying that "lossless" means
parameter-identical to pooled training (vs. asymptotically equivalent).

### 16. Leadership, Informatics Expertise, and Resources: Determinants of Institutional Data Sharing in the National Clinical Cohort Collaborative (N3C)
**Authors:** CM Rose, WS Bush, MF Beno, SM Williams, JL Haines …
**Venue:** *AMIA Summits*, 2026.
**Source:** Scholar alert — Chute citation feed.
**Why METHODS-WATCH:** Socio-technical analysis of why some
institutions contribute to N3C and others don't — relevant context for
designing any future multi-site analysis governance, even outside N3C.

### 17. Translation readiness of model-based synthetic tabular data in healthcare: a systematic review and governance audit
**Authors:** S Castagno, A Subramanian, IE Epanomeritakis …
**Venue:** *JAMIA*, 2026.
**Source:** Scholar alert — Chute citation feed.
**Snippet:** "Objectives: To evaluate the clinical applications and
translation readiness of model-based synthetic tabular data in
healthcare, and identify gaps in governance reporting …"
**Why METHODS-WATCH:** Pairs with item #6 (foundation-model–guided
synthetic-EHR release) — this is the governance/audit side of the same
question. Useful citation for any synthetic-data justification you
write.

### 18. AI Strategies for Advancing Global Bioinformatics Infrastructure and Ecosystems
**Authors:** MD Ritchie
**Venue:** 2026 (book / review).
**Source:** Scholar alert — Chute citation feed.
**Why METHODS-WATCH:** Marylyn Ritchie's overview of where
bioinformatics infrastructure is heading with conversational-LLM
interfaces. Useful background framing rather than a paper to cite.

### 19. The Open Syndrome Definition as a Machine-Readable Standard for Public Health
**Authors:** APG Ferreira, A Anžel, I Marcilio, H Hughes, AJ Elliot …
**Venue:** *Journal of Medical Internet Research*, 2026.
**Source:** Scholar alert — Chute citation feed.
**Why METHODS-WATCH (touches: EHR phenotyping; KGs/ontologies):**
Machine-readable case-definition standard for public-health syndromes;
the citations to HPO suggest interoperation with the phenotype-ontology
ecosystem you track.

### 20. Completeness of Common Data Elements for Breast Cancer Clinical Trials in Observational Databases
**Authors:** A Anand, Y Fang, C Weng, K Natarajan
**Venue:** *AMIA Summits*, 2026.
**Source:** Scholar alert — Hripcsak related-research feed.
**Why METHODS-WATCH:** CDE coverage assessment in observational DBs —
directly methodologically relevant if you ever need to do trial-arm
emulation in EHR data (which you do, for the drug-class threads).

### 21. Computational investigation of single herbal drugs for diabetes and obesity using knowledge graph and network pharmacology
**Authors:** P Sil, R Tiwari, V Garisetti, SP Baskaran …
**Venue:** *Computational Biology and …*, 2026.
**Source:** Scholar alert.
**Why METHODS-WATCH (touches: Knowledge graphs; Drug repurposing):**
The KG + network-pharmacology methodology is interesting but the
herbal-pharmacology angle and absence of a clinical-evidence loop keep
this OFF your HIGH bucket per the INTERESTS.md rubric.

### 22. BMI-genome interactions regulate global gene expression with emphasis in brain and gut
**Authors:** R Signer, C Seah, H Young, K Retallick-Townsley …
**Venue:** *Cell Genomics*, 2026.
**Source:** Scholar alert.
**Why METHODS-WATCH (touches: Genetic epidemiology — GWAS / eQTL):**
GWAS × BMI × tissue-specific expression interaction — methodologically
similar to GxE eQTL scans. Brain-and-gut tissue specificity is the
hook; relevant if you ever pursue an IBD-and-metabolic-trait
crosstalk analysis.

### 23. Hyperemesis gravidarum and adverse pregnancy outcomes: a population-based cohort study of 2.5 million births in California
**Authors:** RM Gardner, JA Mayo, VD Winn, GM Shaw, JF Simard
**Venue:** *American Journal of Obstetrics & Gynecology*, 2026.
**Source:** Scholar alert.
**Why METHODS-WATCH (touches: Causal inference & pharmacoepi; Chronic-
disease clustering):** Off-thread disease, but a 2.5M-birth population
cohort with explicit causal framing is a useful design exemplar for
large-cohort sibling analyses.

---

## SKIP — surfaced but off-thread

These hit the alerts but don't intersect any active research thread
worth a write-up:

- **Identification of spiropyrrolidinoxindoles as SARS-CoV-2 main
  protease inhibitor hits from virtual screening** (Chen et al.,
  *Journal of Computer-Aided Drug Design*) — chemistry-only.
- **AI in Scholarly Investigation: Transforming Research and Ethics**
  (Irfan, book chapter) — meta-commentary.
- **Development and evaluation of a structured LLM-based pipeline for
  automated ICHI coding using neurosurgical request forms** (Lee et al.)
  — ICHI is off your phecode/HPO axis; narrow scope.
- **Patient-Reported Experiences With Viewing and Understanding Test
  Results in Patient Portals** (Richwine, Steitz, Everson, *JMIR*) —
  patient-experience survey, not methods.
- **Applications of ML methods in long COVID phenotyping** (Szlenk et
  al., *Annales Academiae Medicae Silesiensis*) — review, not novel
  cohort or methods.
- **Unveiling the psychological impact of visual impairment in young
  and middle-aged adults** (van der Linden et al., *BMC Psychology*)
  — qualitative concept-mapping, off-thread.
- **iPSC-Derived Myogenic Progenitor Cells from People with ME/CFS …**
  (Nguyen, 2026 preprint) — wet-lab transcriptomics.
- **Integrative Transcriptomic Analysis Identifies … Drug Repurposing
  Candidates in Alzheimer's Disease** (Singh, Chaurasia) — transcriptomics-
  only repurposing, no clinical-evidence loop.
- **Drug Repurposing Against Giardia Targeting Lipid Rafts …** (Pence)
  — antiparasitic; off your repurposing-with-EHR angle.
- **Structure-Guided Repurposing of Approved Drugs Targeting KEAP1/NRF2
  Signalling for NAFLD** (Meesala, Battineni) — docking + MD only.
- **Repurposing trifluridine as an anti-Staphylococcus aureus agent …**
  (Sandhu et al., *Scientific Reports*) — anti-infective wet lab.
- **Systems-level Analysis of EMT: Angiogenesis Crosstalk in OSCC**
  (Alassiri et al.) — disease-specific pathway analysis.
- **Possible Therapeutic Approaches to Big Potassium Channelopathies**
  (Čermáková) — review.
- **MMTF-DTI: Drug-target interaction prediction via multimodal feature
  extraction and dynamic fusion** (Zeng et al., *J Biomedical Informatics*)
  — DTI benchmarking, no clinical-evidence loop.
- **EHR retrospective cohort study** (Yang et al., *Advancements in
  Diagnostic Pathology*) — title-only available, can't triage usefully.
- **Statistical Methods for Institution-Scale Science** (Knight, 2026
  dissertation) — dissertation; method tied to ESRD prediction.
- **Stem cell-derived extracellular vesicles for rare diseases**
  (Han et al., *BioScience Trends*) — translational framework, off
  rare-disease *phenotyping/genetics* thread.
- **AI in interpretation of variants of uncertain significance in
  epilepsy genes** (Capcelea, *MedEspera*) — student-conference abstract.

---

## GitHub `arxiv-digest` back-references

No new commits 2026-06-04 → 2026-06-23 — pipeline appears stalled (see
warning at top). For completeness, the most-recent surfaced items
(already covered in the 06-01 report) were:

- **BIRDNet: Mining and Encoding Boolean Implication KGs as Interpretable
  Deep Neural Networks** — `arXiv:2605.28739` (Dash, single-author) —
  matches KG thread; transcriptomic benchmarks with biology-readable
  first-layer rules.
- **Insurance Pricing Optimization via Off-Policy Evaluation** —
  `arXiv:2605.28327` — propensity-score / IPW methodology, off-domain
  application; METHODS-WATCH only.
- **Benchmarking Ultrasound Foundation Models for Fetal Plane
  Classification** — `arXiv:2605.27796` — ultrasound FM benchmark, off
  any active thread; SKIP.
- **Estimation and Inference for Win Measures with Multiple Ordinal
  Endpoints Subject to Missingness** — `arXiv:2605.27085` — IPW/AIPW
  for win measures; ties into your causal-inference thread.
- **Semiparametric Inference for Causal Effects on Functional Outcomes**
  — `arXiv:2605.26964` — functional DiD with EIF + Neyman orthogonality;
  ties into your causal-inference thread.

---

## Recommended next actions

1. **Fix the `arxiv-digest` pipeline.** It has produced no commits for
   20 days and the q-bio fetch failure has persisted across at least
   three reports. Check the Actions tab → *Daily arXiv digest* run
   history; either the cron stopped firing or every run since 06-03 has
   silently failed all categories. This is your primary preprint
   surveillance channel and it is currently dark.
2. **Pull and read** items #1 (TimeX), #2 (Beesley/Mukherjee MGI), and
   #8 (CHIP in B-cell lymphomas) — these are the three most-actionable
   for current threads.
3. **Compare** items #6 + #7 + #17 as a bundle (synthetic-EHR
   foundation models + governance) — they're from overlapping
   conferences and would write up as a single "AMIA 2026 synthetic-
   EHR landscape" note.
4. **Sanity-check** item #11 (Kang TWAS-coloc MDD repurposing) — single-
   author preprint with a strong methodology claim. Direction-aware
   colocalization is the implementation step most likely to be
   subtly wrong.
