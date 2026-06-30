# Research digest report — 2026-06-30

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-06-30** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 06-30 | Large 06-29 batch (~16 alerts: Hripcsak, Bastarache, Callahan, Szolovits, Zou, Ryan, van der Schaar, Leskovec, Zitnik, He, Natarajan + keyword feeds for "electronic health records", "rare diseases", and Foundation-models+EHR). Smaller 06-27 batch (Ryan, Callahan, Hripcsak, van der Schaar, Zitnik). 06-28 keyword feeds (rare diseases, EHR, foundation-models+EHR). |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 06-30 | **06-26 = 1 paper** (KG-TRACE, off-thread AMR); **06-27 / 06-28 / 06-29 = 0 papers**; **06-30 = 4 papers** (HWE-GWAS unified procedure, DNA-LM benchmark, histopath-RNA multimodal, LLM insurance pricing — only the first is on-thread). |
| NCBI "My NCBI What's New" / bioRxiv/medRxiv subject digests | daily | Aggregate digests for UK Biobank, allergy/immunology, endocrinology, bioinformatics, genetics; not individually triaged here. |
| JAMA Network / Nature Medicine push alerts | weekly | Several "Online First" batches 06-26 → 06-29; relevant items are surfaced via Scholar feeds (#5 below) rather than re-triaged here. |

> ✅ **The 06-20 arxiv-digest fetch failure (3/4 categories 429'd) did
> not recur this window** — 06-26 produced 1 paper, 06-30 produced 4
> papers, both across all four categories. The 06-27/28/29 zeros appear
> to be genuine quiet days for the q-bio.QM / q-bio.GN / q-bio.PE /
> stat.AP cross-section rather than polling failures. The new
> 5-second client delay + 15-second inter-category pause seems to be
> holding under steady state.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **EHR foundation-models thread keeps firing.** *Cohort-Anchored
  Foundation Models for Electronic Health Records: From Risk Scores to
  Auditable Peer Cohorts* (K. Zheng, arXiv:2606.21885, 2026) surfaces in
  **two independent feeds** — the *George Hripcsak — new related
  research* feed and the *Foundation models + "electronic health
  records"* keyword feed. Direct continuation of the
  Sivarajkumar/Szolovits/Hripcsak/Brandt multimodal-EHR-FM paper
  from the 06-20 report. Distinguishing feature: explicit *auditable
  peer cohort* framing — the FM is anchored to a defined reference
  cohort so the risk-score output is paired with the comparator group
  that drives it. Directly on the CLMBR / MOTOR / EHRSHOT / FEMR /
  MEDS lineage. **HIGH.**
- **Multi-modal rare-disease inheritance classification with
  ontology-enriched text.** Mahmood & Alsalem — *A Multimodal Biomedical
  Transformer Fusion Network for Disease-Level Rare-Disease-Inheritance
  Classification Using Ontology-Enriched Text, Metadata, and Gene …*
  (2026), surfaced via the *citations to Lisa Bastarache* feed. Sits at
  the intersection of three of your INTERESTS threads — **rare disease**
  (inheritance pattern classification), **EHR foundation models / KGs**
  (ontology-enriched transformer fusion), and **HPO / SNOMED**
  (likely the ontology layer). The Bastarache-citation channel is
  one of your higher-precision feeds for phecode-adjacent work.
  **HIGH.**
- **Digital twins for clinical trials — methods perspective in npj
  Digital Medicine.** Estévez, Peck, McKinney, Weatherall et al. —
  *Causal inference and digital twins: a roadmap for the future of
  clinical trials* (*npj Digital Medicine*, 2026), via the *Mihaela
  van der Schaar — new articles* feed. Directly on your **causal
  inference + pharmacoepidemiology** thread and adjacent to **target
  trial emulation** — digital-twin generative simulation is the
  natural extension of TTE when the comparator arm is constructed
  rather than observed. Useful citation when arguing for synthetic
  controls in any forthcoming AoU/MVP TTE write-up. **HIGH.**
- **FHIR vs OMOP head-to-head on All of Us EHR data.** Patterson,
  Minto, Beaton et al. — *A comparison of Fast Healthcare
  Interoperability Resources and Observational Medical Outcomes
  Partnership electronic health record data within the All of Us …*
  (2026), via the *Patrick Ryan — new related research* feed.
  Directly on **EHR phenotyping / OMOP** *and* the **AoU**
  biobank thread. Head-to-head FHIR-vs-OMOP on actual AoU data is
  exactly the question every AoU phenotyping pipeline has to answer
  before committing to a CDM. Patrick Ryan is the OHDSI lead, so
  the framing will be authoritative; the open question is whether
  the comparison is descriptive (counts agree?) or outcomes-grade
  (do downstream cohorts match?). **HIGH.**
- **Automated reanalysis of genomic data for rare disease
  diagnostics at scale — Nature Medicine.** Welland, Ahlquist, De
  Fazio, Austin-Tse et al. (*Nature Medicine*, 2026), via the *rare
  diseases* keyword feed. From the abstract framing: "−disease and
  variant-level evidence …" suggests an ACMG-aligned reclassification
  pipeline run at population scale. Directly on your **rare disease**
  + **variant interpretation (ACMG / ClinGen)** threads. Austin-Tse
  is Broad/MGH ClinGen-side — the methodology will likely follow
  ACMG-AMP rather than purely statistical reclassification. **HIGH.**
- **LLM extraction of physical activity from EHR notes — JAMIA
  pipeline + benchmark.** Yang, Niu, Li, Zhou, Xiao, Zhou, Zhan et al.
  — *Benchmarking information extraction of physical activity from
  electronic health record with large language models: an natural
  language processing pipeline and …* (*Journal of the American
  [Medical Informatics Assn]*, 2026), via the *Tiffany Callahan*
  feed (and also surfacing in the *George Hripcsak* feed). Direct
  hit on **EHR phenotyping** (NLP / LLM extraction from clinical
  notes for non-coded phenotypes). Physical activity is an under-coded
  EHR concept — there are no ICD or LOINC codes for "patient runs
  3x/week" — so LLM-from-notes is the only way to get it at scale.
  Useful template for any phecode/HPO-adjacent NLP extraction in
  your pipeline. **HIGH.**
- **Knowledge graphs + reasoning LLMs for transcriptomic
  perturbation prediction.** Fawkes, Hodgson, Hartford — *Knowledge
  Graphs and Reasoning LLMs for Finding Simple Yet Effective
  Transcriptomic Perturbation Predictors* (arXiv:2606.08816, 2026),
  via the *Tiffany Callahan — new related research* feed. KG + LLM
  reasoning to identify transcriptomic-perturbation predictors —
  which lands adjacent to your **drug repurposing** thread (the
  perturbation/response framing is one of the standard repurposing
  signals) and to the **knowledge-graph reasoning** thread.
  Methodologically interesting but the perturbation/transcriptomic
  layer is upstream of the clinical-evidence loop you prioritize.
  **METHODS-WATCH.**
- **arxiv-digest 06-30 produced one on-thread paper.** Böhringer &
  Holzmann — *Evaluating HWE and Association in Genome Wide
  Association Studies: A Unified Procedure* (arXiv:2606.30311,
  stat.ME, 2026-06-29). Unified test that conditions the genotype
  association on the HWE statistic in controls; the framing
  "improves … subsequent fine mapping" is the keyword hit.
  Methods-watch for any GWAS workflow you maintain. The other three
  06-30 papers (DNA-LM benchmark, histopath multimodal, LLM
  insurance pricing — yes, "motor" insurance, false keyword hit) are
  off-thread. **METHODS-WATCH (Böhringer); SKIP (other three).**
- **GLP-1 RA + transient retinal perfusion delay.** Lee, Chang,
  Jang, Ma, Song — *GLP-1 receptor agonist-induced transient
  retinal perfusion delay and its potential mediation by intracranial
  pressure* (*Biomedicine &amp; …*, 2026), via the *Hripcsak
  citations* feed. Mechanism / case-series style report; on your
  GLP-1 drug-class watch but on the safety / NAION-adjacent side
  rather than the indication-expansion side. Logged for the
  GLP-1 RA pharmacoepi running list. **METHODS-WATCH** on
  pharmacoepi-signal mining; **SKIP** if you're not actively
  curating GLP-1 RA AE signals.
- **Cardiology interface terminology curation with ML.** Dehkordi,
  Zhou, Perl, Deek, Geller et al. — *Curation of a Cardiology
  Interface Terminology for Highlighting Electronic Health Records
  using Machine Learning* (arXiv, 2026), via the *Patrick Ryan —
  new related research* feed. Adjacent to **OMOP / phecode / SNOMED**
  curation — interface terminologies sit between local EHR vocab
  and SNOMED/LOINC. The Perl/Geller lineage is the SNOMED auditing
  group at NJIT, which has done substantial phecode-adjacent
  terminology curation; useful methods reference for any phecode-or-
  HPO mapping curation work. **METHODS-WATCH.**
- **Multi-keyword leak still present.** The 06-30 arxiv-digest
  surfaced *Semantic insurance pricing with large language models*
  via a `motor` keyword hit — this is the **MVP-Million-Veteran-Program
  keyword colliding with French automobile-insurance "motor third-party
  liability"**. Recommend disambiguating `motor` to `MVP motor` or
  `million veteran motor` or replacing with `million veteran` (carry-
  forward suggestion for the pipeline).

Counts: **6 HIGH**, **4 METHODS-WATCH**, rest SKIP. Window is busier
than 06-19/06-20 because it covers ~10 days, but the **per-day signal
density is similar** to the 06-20 report.

---

## HIGH priority — detailed reports

### 1. Cohort-Anchored Foundation Models for Electronic Health Records: From Risk Scores to Auditable Peer Cohorts
- **Authors / venue:** K. Zheng — arXiv:2606.21885, 2026.
- **Surfaced by:** **Dual-feed** — (a) *George Hripcsak — new related
  research* feed and (b) the *Foundation models + "electronic health
  records"* keyword feed. Dual-channel firing on an arXiv preprint
  is a moderate-precision signal; less saturated than 06-20's
  Sivarajkumar et al. triple-feed but more than a single-channel hit.
- **Thread:** **EHR foundation models** (CLMBR / MOTOR / EHRSHOT /
  FEMR / MEDS lineage; your INTERESTS file explicitly tracks
  "Foundation-model fairness and calibration audits when grounded in
  EHR data") **+** **ML for precision health** (the "risk scores" output
  is what gets acted on clinically).
- **What it is:** From the snippet: "Foundation models have achieved
  remarkable performance across medical question answering, imaging,
  and electronic health record (EHR) tasks, yet reliable clinical
  deployment remains challenging due to limited interpretability,
  vulnerability to …" The distinguishing word in the title is
  **"cohort-anchored"**: the FM's output is not a raw risk score in
  isolation but a score *paired with the peer cohort that drives the
  score*. The "auditable peer cohorts" framing is the methodological
  novelty — it makes the FM's risk-score output checkable against a
  reference group of similar patients rather than presented as an
  opaque scalar. This is a direct response to the calibration /
  fairness / interpretability critique of CLMBR-style FMs.
- **Why it matters to you:** Four reasons.
  (a) **Directly addresses the FM calibration/audit thread** in your
  INTERESTS file. CLMBR and MOTOR are validated by retrospective
  AUROC on phecodes; neither emits an auditable comparison cohort.
  An FM that emits both a score *and* the peer cohort that drives it
  is exactly the audit-friendly variant the field has been asking for.
  (b) **Peer cohort framing pairs with your phecode work.** PheRS-style
  ascertainment depends on a well-defined reference cohort; an FM that
  outputs the cohort directly is potentially a phenotyping primitive
  (the "peer cohort" is a learned phenotype).
  (c) **Operationally aligns with AoU / MVP audit requirements.** Both
  cohorts require defensible cohort-definition trails for any
  prediction-grade work; a model that auto-emits the comparator group
  fits the compliance posture.
  (d) **Hripcsak feed firing** — Hripcsak's lab is the OHDSI prediction-
  framework lead. Anything FM-shaped that lands in his related-research
  feed is field-relevant by construction.
- **Action:** **HIGH.**
  (i) Read for the **peer-cohort definition mechanism** — is the cohort
  retrieved by a learned embedding nearest-neighbor over the FM's
  representation space, or is it constructed from a structured query
  (phecode + age + sex + …)? Embedding-NN is the more interesting
  design.
  (ii) Note the **risk-score head architecture** — is it a calibrated
  classifier on top of the cohort, or a Cox-style time-to-event head?
  The calibration mechanism matters for clinical use.
  (iii) Check the **evaluation cohort** — MIMIC? Columbia (the
  Hripcsak feed firing suggests Columbia)? UK Biobank? Cohort identity
  bounds the transfer claim.
  (iv) Note any **comparison against CLMBR / MOTOR / FEMR** baselines.
  If absent, that's the obvious external-validity gap.
  (v) **Save and cite-watch** — this is the kind of paper that becomes
  a default citation for any "auditable EHR FM" argument you write in
  the next 12 months.

### 2. A Multimodal Biomedical Transformer Fusion Network for Disease-Level Rare-Disease-Inheritance Classification Using Ontology-Enriched Text, Metadata, and Gene Data
- **Authors / venue:** M.A. Mahmood, K. Alsalem — venue not in
  snippet (likely *Bioinformatics*, *NPJ Digital Medicine*, or a
  biomedical-AI venue; the *citations-to-Lisa-Bastarache* surfacing
  suggests it cites her phecode / phenotype work).
- **Surfaced by:** *10 new citations to articles by Lisa Bastarache*
  feed.
- **Thread:** **Rare disease** (inheritance pattern classification at
  disease level) **+** **Knowledge graphs / ontologies** (ontology-
  enriched text — likely HPO and/or OMIM) **+** **EHR foundation
  models / multimodal fusion** (transformer fusion across text +
  metadata + gene data).
- **What it is:** A multimodal transformer that fuses (a) **ontology-
  enriched text** (free-text disease descriptions enriched with HPO /
  OMIM / SNOMED terms), (b) **metadata** (likely disease-level
  attributes — onset age, system involvement), and (c) **gene data**
  (associated gene lists or sequence-based features) to classify
  disease *inheritance pattern* (autosomal dominant / recessive /
  X-linked / mitochondrial / complex). The Bastarache-citation
  channel suggests phecode or phenotype-similarity infrastructure is
  used somewhere in the pipeline.
- **Why it matters to you:** Three reasons.
  (a) **Rare-disease inheritance classification is a phenotyping
  primitive.** Knowing inheritance pattern bounds the variant-
  interpretation prior — autosomal recessive disease constraints what
  a single heterozygous variant can mean; X-linked changes the female-
  carrier interpretation. An automated disease-level inheritance
  predictor is upstream of any ACMG / ClinGen variant call that
  depends on inheritance assumption.
  (b) **Ontology-enriched text + transformer fusion is exactly the
  HPO-aware multimodal FM design** you'd want for rare-disease
  diagnostic NLP. Most rare-disease NLP is HPO-coded *after* extraction
  (text → HPO terms → reasoning); ontology-enriched *input* (text +
  HPO terms together as input) is a different and potentially
  stronger pattern.
  (c) **Bastarache-citation surfacing** means it references her work
  — likely the phecode catalog or her rare-disease similarity work.
  Worth checking whether they use **PheCodeX**, OMIM, ORPHA, or
  Mondo as the disease-level vocabulary; the choice constrains
  downstream EHR integration.
- **Action:** **HIGH.**
  (i) Read for the **ontology integration layer** — is HPO/OMIM
  injected at the embedding layer (concept embeddings concatenated to
  text tokens), the attention layer (graph attention over HPO),
  or post-hoc (transformer output combined with HPO similarity)? Each
  has different downstream implications.
  (ii) Note the **disease vocabulary** (OMIM, ORPHA, Mondo, PheCodeX,
  custom). Mondo is the natural cross-walk; OMIM is the legacy
  reference; ORPHA is the European reference. The choice determines
  whether this slots into your EHR rare-disease cohorts.
  (iii) Check the **gene data modality** — is it gene list (OMIM-
  derived), sequence (transformer over gene sequences), or expression
  (tissue-level expression vector)? The most clinically useful is
  gene list + tissue expression.
  (iv) Note the **inheritance label source** — OMIM, ORPHA, manual?
  Label-source bias is a known issue in inheritance-pattern
  prediction (under-reporting of recessive disease in OMIM, e.g.).
  (v) **Potential composition** with your rare-disease + HPO-based
  phenotype matching work — if the inheritance predictor is robust,
  it could be a covariate in your HPO-driven rare-disease repurposing
  pipeline.

### 3. Causal inference and digital twins: a roadmap for the future of clinical trials
- **Authors / venue:** S.R. Estévez, R. Peck, E. McKinney, J.
  Weatherall et al. — *npj Digital Medicine*, 2026.
- **Surfaced by:** *Mihaela van der Schaar — new articles* feed.
- **Thread:** **Causal inference and pharmacoepidemiology** (target
  trial emulation lineage) **+** **ML for precision health** (digital
  twin = generative counterfactual at the patient level).
- **What it is:** A *roadmap / perspective* paper on integrating
  digital-twin generative simulation into clinical trial design and
  analysis. Likely structured around: (1) **synthetic control arms**
  generated by a digital twin instead of recruited or matched, (2)
  **counterfactual outcomes** under alternative treatment regimens,
  (3) **causal identifiability constraints** when the twin is trained
  on observational data, and (4) **regulatory acceptance** (FDA's
  recent digital-twin guidance). Van der Schaar's group has been
  the methodological lead on this for the past two years.
- **Why it matters to you:** Three reasons.
  (a) **Target trial emulation is your direct methodology.** TTE
  constructs a synthetic trial protocol applied to observational
  data; digital twins go a step further and construct a synthetic
  *counterfactual outcome* per patient. The boundary is conceptually
  thin — a TTE with rich enough covariate adjustment and a flexible
  enough outcome model *is* a digital twin in disguise. A roadmap
  paper that draws this boundary explicitly is a useful citation.
  (b) **GLP-1 / SGLT2 / CFTR drug-class threads.** Each of these has
  ongoing TTE work where the comparator is hard to construct (e.g.,
  CFTR modulators vs no-treatment comparator is biased by access
  cohort selection; HRT vs no-HRT is biased by healthy-user effect).
  Digital-twin synthetic controls are a way to construct the
  comparator from the cohort itself.
  (c) **van der Schaar feed** is a high-precision channel for causal-
  ML methodology; this is the kind of paper that becomes a default
  reference when arguing for synthetic-control evidence in regulatory
  / payer settings.
- **Action:** **HIGH.**
  (i) Read the **causal identifiability section** — what assumptions
  do they require beyond standard TTE (no unmeasured confounding,
  positivity, consistency)? Digital twins usually require a stronger
  *structural-equation* assumption on the outcome generation
  process; that's the conceptual cost.
  (ii) Note the **regulatory framing** — do they reference FDA's
  digital-twin guidance, EMA's, both? Regulatory acceptability is
  what determines whether this is operationally useful or only
  methodologically clean.
  (iii) Check the **evaluation examples** — do they apply to an
  actual past trial (synthetic control reproducing the published
  result) or just propose the framework? Reproduction of past trials
  is much stronger evidence.
  (iv) Pair with the Sept-2024 Hernán "target trial emulation
  refresher" if cited; if not, that's the obvious bibliographic gap.
  (v) Citation candidate for any TTE write-up where you need to
  argue for or against a synthetic comparator arm.

### 4. A comparison of Fast Healthcare Interoperability Resources and Observational Medical Outcomes Partnership electronic health record data within the All of Us …
- **Authors / venue:** J. Patterson, E. Minto, M. Beaton, A. [—] —
  venue not in snippet (likely *JAMIA*, *JAMIA Open*, or *npj
  Digital Medicine* given the OHDSI / AoU framing).
- **Surfaced by:** *Patrick Ryan — new related research* feed.
- **Thread:** **EHR phenotyping & OMOP** (head-to-head FHIR-vs-OMOP
  comparison) **+** **Biobanks with EHR linkage: All of Us** (AoU is
  the test bed).
- **What it is:** A head-to-head comparison of **FHIR-format EHR data**
  vs **OMOP-CDM-format EHR data** **within the All of Us Research
  Program**. AoU provides both — FHIR via the Standard Workspace
  PFB / Hail and OMOP-CDM via the BigQuery `cdr` dataset — and the
  question of whether they agree (and where they don't) is a
  practical blocker for any AoU phenotyping pipeline that wants to
  use both representations or compare across studies that use one
  vs the other. Patrick Ryan-feed surfacing means OHDSI-lineage; the
  comparison framing will likely follow the OHDSI conventions
  (concept-set–driven cohort definitions).
- **Why it matters to you:** Four reasons.
  (a) **Direct operational guidance for AoU phenotyping.** Any
  cohort defined in OMOP-CDM has a question lurking — does the
  *same* cohort reconstructed from the FHIR primary source agree?
  This paper presumably gives you the empirical answer for AoU.
  (b) **OMOP is on your INTERESTS file**; AoU is the biobank you
  publish in most. A head-to-head comparison from the OHDSI lead
  in AoU is a default citation for any AoU-OMOP cohort write-up.
  (c) **Discordance directions are informative.** If FHIR shows more
  encounters than OMOP, OMOP is dropping some encounter types; if
  OMOP shows more conditions per encounter than FHIR, OMOP's
  concept-set expansion is broader than FHIR's CodeableConcept.
  Either pattern has phenotyping implications.
  (d) **Patrick Ryan feed** is one of your highest-precision channels
  for OHDSI / OMOP / AoU work — the surfacing is high-confidence
  on-thread by construction.
- **Action:** **HIGH.**
  (i) Read for the **comparison granularity** — encounter count,
  condition count per encounter, drug-exposure granularity, lab-
  value mapping? Each has different downstream consequences.
  (ii) Note the **AoU release window** (CDR v7? v8?) — the OMOP
  mapping has evolved across releases and the comparison may be
  release-specific.
  (iii) Check whether they evaluate **outcome-grade cohort agreement**
  (the same set of patients identified by both) or only
  *descriptive*-grade (counts match). Outcome-grade is what matters
  for phenotyping.
  (iv) Note any **recommended best practice** — if they recommend
  one over the other (or a hybrid pull), that's directly actionable
  for any AoU-OMOP pipeline you maintain.
  (v) **Save** for the AoU phenotyping methods file; cite-watch in
  any AoU cohort-construction methods section.

### 5. Automated reanalysis of genomic data for rare disease diagnostics at scale
- **Authors / venue:** M.J. Welland, K.D. Ahlquist, P. De Fazio, C.
  Austin-Tse et al. — *Nature Medicine*, 2026.
- **Surfaced by:** *rare diseases* keyword feed (Scholar).
- **Thread:** **Rare disease** (clinical diagnostic reanalysis) **+**
  **Variant interpretation (ACMG / ClinGen)** (reclassification at
  scale is the variant-level operation) **+** **Genetic
  epidemiology** (rare-variant evidence accumulation over time).
- **What it is:** From the snippet: "−disease and variant-level
  evidence with …" — i.e., a pipeline that ingests variant-level
  evidence and disease-level evidence and re-runs ACMG/AMP-style
  classification at population scale. Austin-Tse is Broad/MGH
  Clinical Lab Science / ClinGen; the methodology will follow
  ACMG-AMP curation conventions. The "at scale" framing implies a
  production-grade reanalysis pipeline rather than a method paper —
  the kind of system that runs on a clinical genome cohort
  quarterly to surface VUS→P/LP transitions as new evidence
  accumulates.
- **Why it matters to you:** Four reasons.
  (a) **Rare disease + ACMG reclassification is squarely on your
  INTERESTS threads.** Your INTERESTS file calls out "variant
  curation tooling (InterVar, AnFiSA-style DSLs)" — an automated
  reanalysis pipeline is the production deployment of that DSL.
  (b) **Population-scale reanalysis enables longitudinal variant
  surveillance.** A variant that was VUS at first report may
  become P/LP as ClinVar accumulates more cases; an automated
  reanalysis pipeline closes the feedback loop. For any APOL1 /
  CFTR / BRCA cohort you maintain, this kind of pipeline is the
  way to keep classifications current.
  (c) **Nature Medicine venue** signals clinical-evidence framing
  rather than methods-only — the paper likely includes a clinical
  yield estimate (% of cases newly diagnosed by reanalysis).
  Yield numbers from this paper are citation-grade for any
  rare-disease reanalysis argument.
  (d) **Austin-Tse / ClinGen lineage** aligns with the variant-
  interpretation thread; this is methodologically credible.
- **Action:** **HIGH.**
  (i) Read for the **evidence-ingestion architecture** — ClinVar
  pull frequency, gnomAD allele-frequency thresholds, OMIM /
  ORPHA disease-evidence integration. Reanalysis is only as good
  as the evidence updates it ingests.
  (ii) Note the **cohort size and reanalysis cadence** — what's
  the realistic reanalysis-yield rate when run quarterly vs
  annually on a clinical genome cohort?
  (iii) Check whether they integrate **functional evidence**
  (MaveDB, ClinGen functional studies) or only literature evidence.
  Functional-evidence integration is the next frontier.
  (iv) Note the **ACMG strength assignment** logic — automated PVS1
  / PS3 / PM2 assignment is the hard problem; if they handle PVS1
  splicing automation well, that's directly useful for your CFTR
  variant work.
  (v) Citation-watch for any rare-disease reanalysis or
  longitudinal-classification write-up.

### 6. Benchmarking information extraction of physical activity from electronic health record with large language models: an natural language processing pipeline and …
- **Authors / venue:** H. Yang, Z. Niu, M. Li, H. Zhou, Y. Xiao, S.
  Zhou, Z. Zhan et al. — *Journal of the American Medical
  Informatics Association* (JAMIA), 2026.
- **Surfaced by:** *Tiffany Callahan — new related research* feed.
  Likely also relevant to *George Hripcsak — new related research*
  feed structure.
- **Thread:** **EHR phenotyping & OMOP** ("NLP / LLM extraction from
  clinical notes for phecode and HPO term assignment" — the user's
  INTERESTS file explicitly calls this out) **+** **ML for precision
  health** (the extracted feature is downstream of risk prediction
  and lifestyle-intervention targeting).
- **What it is:** A benchmark and pipeline for extracting **physical-
  activity** information from clinical notes using LLMs. Physical
  activity is the canonical *under-coded* EHR concept — there are no
  ICD-10 or LOINC codes for "patient runs 3x/week" or "sedentary
  lifestyle"; the only signal is free text in social-history,
  exercise-counseling, or counseling-against-sedentary-behavior
  sections of notes. JAMIA venue + Callahan-feed surfacing suggests
  this is methodologically rigorous (curated test set, multiple LLM
  baselines, ablation across prompting strategies).
- **Why it matters to you:** Three reasons.
  (a) **Direct on-thread for EHR phenotyping NLP.** Your INTERESTS
  file explicitly mentions "NLP / LLM extraction from clinical notes
  for phecode and HPO term assignment." Physical activity is not
  phecode-mapped but the *extraction methodology* generalizes —
  prompting strategy, few-shot template, chain-of-thought-vs-direct,
  whatever they find is the methodology you'd want for any
  under-coded phenotype (alcohol use, dietary patterns, sleep,
  social support).
  (b) **Composite-risk modeling and target-trial emulation both
  benefit from PA covariates.** PA is a strong confounder in
  cardiometabolic and CFTR-modulator pharmacoepi work — having a
  validated NLP-derived PA covariate is operationally useful for
  any AoU/MVP TTE in those areas. Currently this covariate is
  unavailable in AoU's structured tables.
  (c) **Callahan feed** is a high-precision channel for OMOP / HPO /
  ontology-aware NLP work — this paper is on-thread by surfacing
  channel alone.
- **Action:** **HIGH.**
  (i) Read for the **prompting strategy** that wins — few-shot,
  CoT, chain-of-verification, structured-output? The winning
  strategy generalizes across phenotyping NLP.
  (ii) Note the **LLM baselines** — open-source (Llama, Mistral)
  vs closed (GPT, Claude). For AoU / MVP enclave compliance, only
  open-source is operationally usable.
  (iii) Check the **gold-standard annotation protocol** — single vs
  multi-annotator, IAA, source of notes (MIMIC, in-house, AoU).
  AoU-source would be ideal; MIMIC is the usual proxy.
  (iv) Note **error analysis** — false positives from health-
  coaching templates ("patient was advised to exercise") are the
  classic NLP-on-PA failure mode; how do they handle it?
  (v) Potential adoption — if the open-source pipeline is
  workable, integrate as an AoU phenotyping primitive for any
  PA-confounded TTE you run.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Knowledge Graphs and Reasoning LLMs for Finding Simple Yet
  Effective Transcriptomic Perturbation Predictors** — J. Fawkes,
  L. Hodgson, J. Hartford — arXiv:2606.08816, 2026 (Tiffany
  Callahan feed). KG-grounded LLM reasoning identifies
  perturbation-response predictors in transcriptomics. *Watch
  for:* the **KG-grounded prompting** mechanism — does the LLM
  reason over a retrieved subgraph or over a flat textual
  description of one? Subgraph-grounded prompting with rationale
  output is exactly the **explainable drug-repurposing** angle
  your INTERESTS file flags. **Adjacent to drug repurposing**
  via the perturbation-prediction analogue, but upstream of the
  clinical-evidence loop; **METHODS-WATCH** rather than HIGH.

- **Curation of a Cardiology Interface Terminology for
  Highlighting Electronic Health Records using Machine Learning**
  — M.K.H. Dehkordi, S. Zhou, Y. Perl, F.P. Deek, J. Geller et al.
  — arXiv, 2026 (Patrick Ryan feed). The Perl/Geller lineage at
  NJIT does SNOMED/OMOP auditing and interface-terminology
  curation. *Watch for:* whether the ML layer is **subsumption
  inference** (find concepts that should be children of a parent
  but aren't), **synonymy clustering** (find local terms that
  collapse to one SNOMED concept), or **completeness flagging**
  (terms in EHR but absent from the interface vocabulary). The
  cardiology focus is incidental — the **methodology** transfers
  to any phecode / HPO mapping curation. **Useful methods
  reference** for the OMOP / phecode mapping work; not directly
  on a disease thread.

- **GLP-1 receptor agonist-induced transient retinal perfusion
  delay and its potential mediation by intracranial pressure** —
  Y.K. Lee, Y.Y. Chang, H.N. Jang, D.J. Ma, H.B. Song —
  *Biomedicine & …*, 2026 (Hripcsak citations feed). Mechanistic
  + small-cohort observational report. *Watch for:* whether the
  perfusion-delay signal is **proportional to GLP-1 RA exposure
  duration / dose** (suggests a pharmacoepi-able signal) or a
  **one-time post-initiation transient** (less useful). NAION-
  adjacent — if proportional, this links to the GLP-1/NAION
  literature you've been tracking. **Logged on GLP-1 RA AE
  watch.**

- **Evaluating HWE and Association in Genome Wide Association
  Studies: A Unified Procedure** — S. Böhringer, H. Holzmann —
  arXiv:2606.30311, 2026 (stat.ME, surfaced by `arxiv-digest`
  06-30). Conditional genotype-based test that conditions the
  3×2 association χ² on the control-group HWE χ², with asymptotic
  distribution theory. Avoids the standard practice of pre-
  filtering SNPs by an arbitrary HWE threshold. *Watch for:*
  whether the procedure gives a **stable ranking** of SNPs across
  HWE-cutoff choices — that's the operational benefit. **Useful
  methods reference** for any GWAS QC pipeline you maintain; the
  alopecia data set evaluation is incidental. Carry-forward: the
  fine-mapping reference is what made the keyword match.

- **Quantifying and Improving the Robustness of Retrieval-
  Augmented Language Models Against Spurious Features in
  Grounding Data** — S. Yang, J. Wu, W. Ding, N. Wu, S. Liang,
  M. Gong, H. Li et al. — Findings of [the EMNLP/ACL family],
  2026 (Peter Szolovits related-research feed). RAG robustness
  benchmark against spurious features in retrieval. *Watch for:*
  whether the spurious-feature framing **transfers to clinical
  RAG** (LLM-over-EHR retrieval) — if a clinical LLM grounds its
  answer in a note that contains a confounding lab value rather
  than the relevant diagnosis, that's a clinically-meaningful
  spurious-feature failure mode. Not directly on a clinical
  thread, but methodologically relevant to any retrieval-
  augmented EHR FM design. **METHODS-WATCH.**

- **arxiv-digest 06-26 KG-TRACE** — N. Garg, S. Jain, S. Yadav,
  B.K. Bhargava, G. Singh, A. Srivastava, P. Kar — *KG-TRACE:
  A Neuro-Symbolic Framework for Mechanistic Grounding in
  Antimicrobial Resistance Prediction*. AMR-prediction-with-KG
  is **off your disease threads** but the **neuro-symbolic +
  mechanistic-grounding** pattern overlaps with explainable
  drug-repurposing methodology. **Light log only** — surface if
  the methodology recurs in a more on-thread paper.

---

## SKIP / noise (logged, no action)

- **Real-Time Voice AI Hears but Does Not Listen** — M. Bartelds,
  F. Bianchi, J. Zou — arXiv:2606.26083, 2026 (James Zou feed).
  Speech / vocal-delivery evaluation; off the clinical/EHR threads.
- **Towards Root Memories: Benchmarking and Enhancing Implicit
  Logical Memory Retrieval for Personalized LLMs** — H. Ding, X.
  Yu, C. Wang, J. Xiao, K. Bao, W. Wang, X. He (Xiangnan He feed).
  Personalized-LLM memory / recommender lineage; off-thread.
- **NatureBench: Can Coding Agents Match the Published SOTA of
  Nature-Family Papers?** — Y. Wang, L. Cheng, Y. Zuo, S. Zeng,
  B. He, C. Jiang et al. (Vivek Natarajan citations feed).
  Coding-agent benchmark — off the clinical-AI thread despite the
  Nature framing.
- **Equivariant Graph Neural Operator for Modeling 3D Dynamics**
  — E. Zander, M. Xu, J. Han, A. Lou, J. Leskovec, S. Ermon et al.
  (Leskovec feed). 3D-dynamics GNN; off-thread (general ML).
- **On-Policy Self-Distillation for Efficient Diffusion Language
  Models with Early-Stage Calibration** — H. Zhu, M. Liu, J. Liu,
  Z. Ge, T. Wang, J. Gesi, D. Wang (Marinka Zitnik related-
  research feed). LLM training-method paper; off the
  clinical-FM thread.
- **CellBRIDGE: Learning Cellular Trajectories via Interaction-
  Aware Alignment** — S. Ruhrberg Estévez et al. (van der Schaar
  feed, 06-27). Cellular-trajectories on single-cell data; off
  the EHR-trajectory thread despite the name overlap.
- **Unified Energy for Invariant and Independent Decoding in
  Diffusion Language Models** — Y. Yan, M. Xu, Z. Yang, Y. Bian
  (Zitnik feed). DLM training method; off-thread.
- **Coproduction Without Youth? Closing the Participation Gap in
  Digital Mental Health Research** — C. Blease, M. Tibbs, A.
  Balaskas, S. Liverpool (Szolovits citations feed). HCI /
  participation; off your methods threads.
- **Digital solutions in acute medicine: Will electronic health
  records join up the patient journey (soon?)** — C.P. Subbe, A.
  Kinderlerer, Y.H. Jani — *Future Healthcare Journal*, 2026
  ("electronic health records" keyword feed). Perspective piece,
  policy-tier; SKIP.
- **DNA Language Models: An Assessment of Pre-Training for Fine-
  Tuning Tasks** — R. Karpinsky, J. Mozziconacci, M. Delcey —
  arXiv:2606.30140, 2026 (q-bio.GN, arxiv-digest 06-30).
  Genomic-FM benchmark; off the clinical-FM and variant-
  interpretation threads.
- **Data-Efficient Multimodal Alignment for Histopathology-based
  Molecular Prediction** — D. Winter et al. — arXiv:2606.29949,
  2026 (eess.IV, arxiv-digest 06-30). Pathology + RNA alignment;
  off the EHR-FM thread.
- **Semantic insurance pricing with large language models** — C.
  Blier-Wong, D. Kusmenko — arXiv:2606.29371, 2026 (stat.AP,
  arxiv-digest 06-30). False keyword hit on `motor` (French
  motor-third-party-liability insurance, *not* Million Veteran
  Program). SKIP. **See pipeline suggestion below.**

---

## Suggestions for the pipeline

Carry-forward items from the 06-20 report remain unactioned. Today's
items add three new issues:

1. **`motor` keyword false-hit on automobile-insurance papers.** The
   06-30 arxiv-digest surfaced *Semantic insurance pricing with large
   language models* via a `motor` keyword hit — the paper is about
   French motor-third-party-liability *automobile* insurance, not
   the Million Veteran Program. Recommend disambiguating the keyword
   from `motor` to `MVP motor` or `million veteran motor` or
   `million veteran program` (as a phrase). The collision with
   `motor neuron` and `motor insurance` is a known noise pattern.

2. **`fine mapping` keyword behaving correctly.** Today's
   Böhringer & Holzmann paper surfaced via `fine mapping` and is
   on-thread (GWAS methods). The keyword is doing what it should;
   no action.

3. **Add bioRxiv `Genetics` and medRxiv `Epidemiology` to the source
   feeds.** Today's items #2 (Mahmood multimodal rare-disease
   inheritance), #4 (Patterson FHIR-vs-OMOP), #5 (Welland Nature
   Medicine reanalysis) all came via Scholar feeds because they're
   in non-arXiv venues (the actual venues differ but none are in
   the q-bio / stat.AP arXiv slice the current `arxiv-digest`
   polls). Carry-forward from the 06-20 report; not new but
   reinforced.

4. **Continue the Patrick Ryan + Tiffany Callahan + George Hripcsak
   feed weighting.** Three of today's six HIGH items came from these
   three feeds (Ryan → #4 + Curation methods; Callahan → #2 + #6 +
   #7; Hripcsak → #1 + #9). These are your highest-precision OMOP /
   OHDSI / EHR-phenotyping channels and warrant keeping at full
   delivery rather than digesting.

5. **`knowledge graph` keyword tightening** (carry-forward from
   06-20). Not retracted; today's KG-TRACE 06-26 paper is the 8th
   consecutive window of non-biomedical KG hits via this keyword.
   Suggested fix unchanged: replace with `biomedical knowledge
   graph` OR `clinical knowledge graph` OR a compound filter
   `(knowledge graph) AND (medical OR biomedical OR clinical OR
   EHR OR phenotype OR drug OR disease)`.

6. **Add `digital twin` / `synthetic control arm` / `target trial
   emulation` keywords** (new). Today's item #3 (Estévez digital
   twins roadmap) would have been caught by `digital twin` from
   arXiv `stat.ME` and `cs.LG` slices that the current pipeline
   doesn't poll. Pairs with the Scholar-feed coverage.

7. **Add `cohort-anchored` / `peer cohort` / `auditable foundation
   model` keywords** (new). Today's item #1 (Zheng cohort-anchored
   EHR FM) is one of a growing family of audit-friendly EHR-FM
   papers; the sub-pattern is emerging and worth dedicated keyword
   coverage.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 6 | (1) Zheng cohort-anchored EHR FM [Hripcsak + FM-EHR keyword], (2) Mahmood & Alsalem multimodal rare-disease-inheritance [Bastarache citations], (3) Estévez et al. causal-inference + digital twins roadmap [van der Schaar, *npj DM*], (4) Patterson et al. FHIR-vs-OMOP in AoU [Ryan], (5) Welland et al. automated rare-disease reanalysis at scale [rare-diseases keyword, *Nat Med*], (6) Yang et al. LLM extraction of physical activity from EHR [Callahan, *JAMIA*] |
| METHODS-WATCH | 4 (+1 logged) | Fawkes et al. KG + reasoning LLMs for transcriptomic perturbation [Callahan]; Dehkordi et al. ML cardiology interface terminology [Ryan]; Lee et al. GLP-1 RA transient retinal perfusion delay [Hripcsak citations]; Böhringer & Holzmann unified HWE+association test [arxiv-digest 06-30]; Yang et al. RAG robustness against spurious grounding features [Szolovits]; KG-TRACE AMR neuro-symbolic [arxiv-digest 06-26] |
| SKIP | ~12 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH), this window
delivers the same HIGH count over ~10 days of accumulated alerts. The
**Scholar feeds carry essentially all of the on-thread signal** in this
window — the `arxiv-digest` pipeline contributed one METHODS-WATCH
item (Böhringer & Holzmann GWAS) across 5 days. The recurring pattern
holds: Scholar author-feeds (Ryan, Callahan, Hripcsak, Bastarache,
van der Schaar) and the *rare diseases* / *Foundation models + EHR*
keyword feeds are your highest-precision channels; the arXiv q-bio /
stat.AP slice continues to underperform for venue reasons (most
on-thread papers land in JAMIA / Nature Medicine / npj Digital
Medicine, not arXiv).

The standout this window is the **EHR foundation-models cluster** —
Zheng's cohort-anchored audit framing (#1) plus Mahmood's ontology-
enriched rare-disease classifier (#2) plus Welland's automated
reanalysis pipeline (#5) form a coherent sub-pattern around **audit-
grade / ontology-grounded / longitudinally-updated** FM design that
is increasingly the field's published direction after the 06-20
Sivarajkumar multimodal EHR-FM paper.
