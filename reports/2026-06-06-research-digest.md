# Research digest report — 2026-06-06

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-06-02 → 2026-06-06** (since the prior 2026-06-01 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-06 | Two batches landed 06-06: 06:51 UTC (author + citation alerts, ~35 threads) and 12:24 UTC (keyword alerts, ~13 threads). No alert batches were sent on 06-02 – 06-05 in the inbox. |
| `arxiv-digest` repo (`digests/`) | 2026-06-02 → 06-06 | 06-02: 0 papers. 06-03: 0 papers (3/4 q-bio categories failed to fetch — still broken). 06-06: **2 papers** (first non-empty digest in over a week). |
| bioRxiv / medRxiv subject alerts | daily | Aggregate collection digests, not individually triaged. |
| Raw arXiv daily mailings (`no-reply@arxiv.org`) | daily | Unfiltered cs/q-bio/stat to a list address; not triaged here. |

> The `arxiv-digest` GitHub pipeline broke again 06-03 (same q-bio.QM /
> q-bio.GN / q-bio.PE fetch failures flagged in the prior two reports) but
> recovered by 06-06, surfacing 2 relevant papers. The underlying retry /
> backoff fix is still pending — flag #1 in *Suggestions* carries forward.

> Caveat: Scholar alert emails contain title, authors, venue, and the first
> ~2-3 lines of each abstract only. The reports below contextualize that
> metadata against your research threads; nothing here reflects full-text
> reading.

---

## Executive summary

- **Comorbidity-architecture → mechanism paper saturating two feeds.**
  Wang/Zhou/Tong et al.'s *phenotype-to-mechanism framework* (#1 below)
  appears in both the Lisa Bastarache citation feed *and* the George
  Hripcsak citation feed — strong signal that this paper is in the
  PheWAS-comorbidity-architecture line you actively track. Sits at the
  intersection of PheWAS/PheRS, multimorbidity, and drug repurposing.
- **Pharmacoepi / GLP-1 RA, OHDSI flavor.** Cai et al.'s *Semaglutide
  and neovascular AMD* OHDSI Network Study (#2 below) is a multi-site
  OMOP-CDM analysis of a GLP-1 RA safety signal — directly on the
  GLP-1 pharmacoepi thread *and* methodologically on the OMOP/multi-site
  thread. Surfaced redundantly via Patrick Ryan *new articles* and
  George Hripcsak *new articles*.
- **Cross-ancestry variant interpretation + T2D.** Hodgson et al. (Claudia
  Langenberg) report an *ancestry-enriched HNF4A variant* and a *GP2*
  signal from an exome-wide T2D study (13,674 cases / 41,024 controls) —
  directly serves your variant-interpretation + ancestry-aware risk thread
  with a T2D anchor (#3 below).
- **Causal-inference methods on `arxiv-digest`.** The 06-06 digest
  surfaced Shen/Fu/Lin's *external-control weighted causal inference for
  treatment switching* (#4 below) — synthetic-control + balancing-weights
  hybrid for OS endpoints when patients cross arms. Slots into the
  causal-inference / TTE thread and is directly applicable to RWE designs
  with treatment crossover.
- **MR-for-repurposing template, depression edition.** ter Kuile et al.
  (Lisa Bastarache new-related) extend the proteome-MR-for-target-
  prioritization template to major depression (#5 below) — fourth or
  fifth incarnation of this template across recent windows, reinforcing
  the *Suggestions* note about adding `colocalization` / `proteome-wide`
  to `tracked.yaml`.
- **Rare-disease LLM agent.** Liu et al. (Hongyu Zhao) describe a
  *multi-modal agent for rare disease diagnosis and risk gene
  prioritization* (#6 below) — directly on the rare-disease + HPO-based
  phenotyping + LLM-agent intersection.
- **EHR phenotyping via privacy-preserving local LMs.** Kormilitzin et
  al.'s self-harm-detection paper (#7) appeared in **three separate
  author feeds** (Szolovits, Hripcsak, Brandt) — saturation signal. On
  the EHR-phenotyping-via-LLMs thread; also relevant to your privacy /
  on-prem inference angle.
- **Selection-bias bound for ML medical prediction.** Liu/Wang/Altman's
  *practical upper bound on selection bias effects* (#8) — Joshua C.
  Denny related research alert — directly on the ML-for-precision-health
  thread (calibration / external validity).
- **AoU + EHR trajectory clustering.** Yan/Cudjoe/Taylor's *TASC* (#9) —
  time-aware sequence clustering with uncertainty quantification for EHR
  trajectories, surfaced via the AoU keyword alert. On the multimorbidity
  / disease-trajectory thread.
- **Biomedical KG infrastructure.** Fecho et al.'s *ROBOKOP v1.0* (#10)
  via Tiffany Callahan alert — biomedical KG system release with
  reasoning paths over biomedical entities; aligns with the KGs/ontologies
  thread and the *explainable* drug-repurposing requirement.
- **RWE methods perspective in BMJ.** Hoffmann/Morris/Hernán et al. on
  challenges in routinely collected data for research (#11 — Miguel
  Hernán citation alert) — a methods position piece on RWE design pitfalls;
  goes onto the methods-watch shelf.

Counts: **11 HIGH**, **4 METHODS-WATCH**, rest SKIP. Lower-volume window
than the prior report — only one alert day landed.

---

## HIGH priority — detailed reports

### 1. A phenotype-to-mechanism framework links phenome-wide comorbidity architecture to molecular mechanisms and therapeutic discovery in complex diseases
- **Authors / venue:** W.T. Wang, M. Zhou, J. Tong, M.J. Lin, A. Ke, M. Wei et al. — 2026 (HTML preprint surfaced; venue not in snippet).
- **Surfaced by:** **Lisa Bastarache** "4 new citations" *and* **George Hripcsak** "10 new citations" — dual-feed saturation.
- **Thread:** PheWAS / PheRS (phenome-wide comorbidity architecture) **+** Drug repurposing (therapeutic discovery) **+** Multimorbidity / chronic disease clustering.
- **What it is:** A framework that maps from observed phenome-wide
  *comorbidity architecture* (i.e., the empirical pattern of co-occurring
  diagnoses across complex diseases) to *molecular mechanisms* — and
  then onward to therapeutic-discovery hypotheses (likely repurposing
  candidates). The framing sits between disease-clustering work (which
  stays in the phenotype layer) and drug-repurposing pipelines (which
  start from a molecular target) — it tries to bridge them via the
  comorbidity matrix.
- **Why it matters to you:** Hits three active threads simultaneously.
  The PheWAS-comorbidity-architecture angle is directly on Bastarache's
  intellectual line (which you track because of phecode and PheRS
  methodology), and the *Hripcsak* feed pickup signals OHDSI/OMOP-CDM
  resonance. The therapeutic-discovery output also matches your
  preference for repurposing pipelines that emit *interpretable*
  rationales rooted in clinical co-occurrence rather than pure
  link-prediction scores. The dual-saturation across two distinct
  citation networks is the strongest signal of this window.
- **Action:** **HIGH (top of read pile)** — read carefully for (i) how
  the phenotype-to-mechanism mapping is parameterized (matrix
  factorization? GNN over a phenome-mechanism bipartite graph?), (ii)
  what cohort the phenome-wide comorbidity matrix is built on (UKB? US
  claims? OMOP network?), and (iii) whether the repurposing rationales
  are auditable per candidate. If on-thread, this could be a key citation
  for the next PheRS/composite-risk draft.

### 2. Semaglutide and Neovascular Age-Related Macular Degeneration Among Adults with Type 2 Diabetes: An OHDSI Network Study
- **Authors / venue:** C.X. Cai, B. Toy, B. Martin, R. Fan, E. Westlund, D. Tran et al. — *Ophthalmology*, 2026.
- **Surfaced by:** **Patrick Ryan** "new articles" *and* **George Hripcsak** "new articles" — dual-feed (the OHDSI-leadership pair).
- **Thread:** Causal inference / pharmacoepidemiology (GLP-1 drug-class safety signals) **+** EHR phenotyping / OMOP (multi-site OHDSI Network design) **+** EHR-linked biobanks (network broader than any single biobank).
- **What it is:** Multi-site OHDSI Network Study of semaglutide exposure
  and incident *neovascular AMD* in adults with type 2 diabetes — a
  safety / adverse-event signal on top of the active GLP-1 RA
  pharmacoepi literature. OHDSI Network design implies standardized OMOP
  CDM cohort definitions executed across multiple data partners, with
  combined summary-level estimates.
- **Why it matters to you:** This is the most directly on-thread
  pharmacoepi paper of the window. (i) GLP-1 RAs are an active drug-class
  thread; (ii) the OHDSI Network design is the canonical multi-site OMOP
  pharmacoepi pattern (Ryan/Hripcsak/Schuemie lineage) that your
  causal-inference + OMOP threads both intersect; (iii) the neovascular
  AMD signal is in the news cycle, so this paper will likely be
  high-citation. Strong candidate for a methods read on the cohort
  definition + propensity / weighting strategy, even if neovascular AMD
  is not a tracked outcome.
- **Action:** **HIGH** — read for the OHDSI cohort-definition logic (new-
  user / active-comparator?), the negative-control / heterogeneity
  analyses across sites, and how confounding by indication was handled
  given the T2D severity gradient.

### 3. An ancestry-enriched HNF4A variant and GP2 reveal distinct mechanisms of type 2 diabetes in exome-wide study of 13,674 cases and 41,024 controls
- **Authors / venue:** S. Hodgson, V. Bui, S. Hu, C. Maroteau, M. Bigossi et al. — *medRxiv*, 2026.
- **Surfaced by:** **Claudia Langenberg** "new articles" alert.
- **Thread:** Variant interpretation (ancestry-enriched coding variant; ACMG/ClinGen population-frequency relevance) **+** Genetic epidemiology (exome-wide case-control, large N) **+** Cross-ancestry portability.
- **What it is:** Exome-wide case-control study (n ≈ 13.7k cases / 41k
  controls) for type 2 diabetes that highlights (i) an *ancestry-enriched*
  HNF4A coding variant and (ii) a separate signal at *GP2*, framed as
  pointing to *distinct biological mechanisms* of T2D. HNF4A is a MODY
  gene with a long clinical-genetics track record; "ancestry-enriched"
  implies higher allele frequency in a non-European population subgroup,
  which has direct ACMG PM2/BS1 implications.
- **Why it matters to you:** Directly serves the variant-interpretation
  thread under your ACMG/ClinGen line, where ancestry-enriched coding
  variants at MODY genes are a recurring penetrance-estimation question
  (a single HNF4A variant common in one ancestry but rare elsewhere is
  exactly the kind of variant where biobank-derived penetrance estimates
  diverge from clinical-cohort estimates). Also relevant to your composite-
  risk modeling thread because the GP2 / HNF4A "distinct mechanisms"
  framing implies subgroup-specific genetic architecture — i.e., the same
  question as the *Souaiaia et al. distinct architecture in the tails*
  paper from the prior report, but anchored on a single disease (T2D).
- **Action:** **HIGH** — read for (i) the HNF4A variant's ancestry
  distribution and gnomAD frequencies, (ii) whether penetrance is
  estimated in any biobank-linked subset, and (iii) the GP2 signal's
  effect direction and replication.

### 4. Leveraging External Controls for Treatment Switching in Randomized Controlled Trials: A Weighted Causal Inference Framework for Overall Survival
- **Authors / venue:** A.A. Shen, C. Fu, R. Lin — arXiv 2606.06441 (primary category stat.ME), submitted 2026-06-04.
- **Surfaced by:** `arxiv-digest` repo, 2026-06-06 digest (keyword hit: *causal inference*).
- **Thread:** Causal inference / pharmacoepidemiology (target-trial-emulation-adjacent; treatment switching is a canonical confounding-by-time-varying-treatment problem).
- **What it is:** Methodological framework for estimating overall survival
  treatment effects in RCTs where control-arm patients switch to the
  experimental arm (or other therapies) post-progression. Combines (i)
  synthetic-control methodology (drawing external controls), (ii)
  balancing weights from observational causal inference, and (iii)
  multiple imputation with time-varying weights, plus a discussion of
  risk-set selection for the external-control donor pool. Demonstrated
  on two phase-III oncology trials.
- **Why it matters to you:** Treatment switching is the RCT analog of
  the time-varying-confounding-with-treatment-confounder-feedback problem
  your causal-inference thread already covers (g-methods, IPW). The
  external-control / synthetic-control hybrid is increasingly being
  proposed for hybrid-RCT designs in oncology and rare-disease drug
  approval — directly on your TTE/pharmacoepi line and on your RWE
  methodology line. The risk-set-selection discussion is also relevant
  for cohort design in observational target-trial emulation more
  generally (how to bound the donor pool).
- **Action:** **HIGH (methods)** — read for the risk-set-selection rule
  and the balancing-weight estimator. Also useful as a template for
  *hybrid* designs you may encounter on rare-disease repurposing trials.

### 5. An integrative mendelian randomisation and drug mechanism framework for target prioritisation and therapeutic repurposing in major depression
- **Authors / venue:** A.R. ter Kuile, C. Finan, S. Chopade, M. van Vugt et al. — PDF preprint surfaced, 2026.
- **Surfaced by:** **Lisa Bastarache** "new related research" alert.
- **Thread:** Genetic epidemiology (proteome MR + drug-mechanism overlay) **+** Drug repurposing (target prioritisation).
- **What it is:** Integrative pipeline combining MR (likely proteome-wide
  or transcriptome-wide MR), drug-mechanism annotations, and
  target-prioritisation logic to nominate repurposing candidates for
  major depression. The "drug mechanism framework" piece distinguishes
  this from raw MR-target lists by overlaying mechanism-of-action data.
- **Why it matters to you:** Fourth or fifth incarnation of the
  proteome-MR-for-target-prioritization template across recent windows
  (you flagged it 3× last time across nephrology, lung function, breast
  cancer cross-ancestry, and the new IgA-nephropathy CFH paper). The
  mechanism-overlay step is the new element here — it's the kind of
  *interpretable* glue that turns a target list into an actionable
  repurposing hypothesis, which matches your INTERESTS preference for
  explainable repurposing pipelines.
- **Action:** **HIGH (methods + repurposing)** — read for the
  mechanism-annotation source (DrugBank? ChEMBL?) and how it integrates
  with the MR target list. Also confirms the *Suggestions* note about
  adding `proteome-wide` / `colocalization` as tracked keywords.

### 6. A Versatile Multi-Modal Agent for Rare Disease Diagnosis and Risk Gene Prioritization
- **Authors / venue:** T. Liu, W. Zheng, W. Xuan, R. Yang, B. Yu, K. Huang, N. Liu et al. — preprint surfaced, 2026.
- **Surfaced by:** **Hongyu Zhao** "new articles" alert.
- **Thread:** Rare disease (deep-phenotyping + HPO-based diagnosis) **+** EHR phenotyping (LLM-assisted) **+** ML for precision health (clinical-decision-tied).
- **What it is:** Multi-modal LLM-agent system for two coupled tasks —
  rare-disease diagnosis and risk-gene prioritization. "Multi-modal"
  here typically implies the agent ingests both unstructured clinical
  text (notes / referrals) and structured features (HPO terms, variant
  calls). The snippet flags accurate and timely diagnosis as the
  motivating clinical decision.
- **Why it matters to you:** Three active threads converge: rare-disease
  diagnosis is a tracked area, HPO-based deep phenotyping is an explicit
  sub-bullet, and ML-tied-to-a-clinical-decision (who-to-test, who-to-
  prioritize) is the high-priority shape your INTERESTS calls out
  vs. benchmark-only ML. Hongyu Zhao's group has a strong track record in
  rare-disease genetics methods, so the genetics layer is likely
  non-trivial.
- **Action:** **HIGH** — read for (i) the HPO-to-gene scoring layer
  (Phen2Gene / AMELIE family or a new approach?), (ii) the agentic
  orchestration design, and (iii) any benchmark on UDN-style undiagnosed
  cases. Pair with the n-Lorem nano-rare-patient paper (Wendy Chung
  feed) which is also rare-disease but operational rather than
  algorithmic.

### 7. Detection of Self-Harm in Electronic Mental Health Records Using Privacy-Preserving Local Language Models: Methodological Study
- **Authors / venue:** A. Kormilitzin, D.W. Joyce, A. Tsiachristas, R. Borschmann et al. — *JMIR*, 2026.
- **Surfaced by:** **Peter Szolovits** + **George Hripcsak** + **Pascal Brandt** "new related research" — three-feed saturation.
- **Thread:** EHR phenotyping (NLP/LLM extraction from clinical notes) **+** ML for precision health (clinical decision: self-harm detection) **+** Privacy / on-prem inference considerations.
- **What it is:** Methodological study of *self-harm event detection* in
  electronic mental health records using *local* (i.e., on-premise,
  privacy-preserving) language models rather than cloud APIs. The
  framing is methods-paper: how to operationalize a sensitive-event
  computable phenotype with LMs that never leave the hospital network.
- **Why it matters to you:** Hits the EHR-NLP-for-phenotyping core of
  your EHR-phenotyping & OMOP thread, plus the practical-deployment
  angle of local-inference LMs that you've raised before for
  AoU-equivalent privacy constraints. The 3-feed saturation across two
  distinct intellectual communities (MIT clinical-NLP via Szolovits;
  OHDSI / clinical-informatics via Hripcsak; the Brandt feed) signals
  the paper is being cited as a reference design for sensitive-event
  phenotyping.
- **Action:** **HIGH** — read for (i) the local-LM choice and size
  (BERT-class fine-tune vs. quantized open LM), (ii) precision-recall
  trade-offs at decision thresholds, and (iii) calibration across the
  outcome distribution. Useful as a citation when you discuss
  LLM-assisted phecode assignment under privacy constraints.

### 8. A Practical Upper Bound on Selection Bias Effects in Medical Prediction Models
- **Authors / venue:** K. Liu, M. Wang, R.B. Altman — arXiv 2606.00563, 2026.
- **Surfaced by:** **Joshua C. Denny** "new related research" alert.
- **Thread:** ML for precision health (calibration, external validity) **+** Causal inference (sensitivity analysis for selection bias) **+** EHR phenotyping (selection bias in EHR cohorts).
- **What it is:** Derives a *practical upper bound* on how much selection
  bias can distort estimates from medical prediction models — i.e., a
  sensitivity-analysis-style bound that lets you say "even under
  worst-case selection, the effect is at most X." Altman's group (R.B.
  Altman, Stanford) has been pushing on this kind of bound for several
  years.
- **Why it matters to you:** Selection bias in EHR-derived cohorts is a
  recurring methodological caveat in your work (AoU, BioVU, etc.) — a
  practical upper bound is the kind of tool you can drop into a
  manuscript discussion to quantify the worst case rather than hand-wave.
  Pairs naturally with the Mojtahedi EHR-vs-self-report discordance paper
  from the prior report (which characterizes one source of selection
  bias empirically) — together they give an *empirical magnitude* and a
  *theoretical bound* on the same problem.
- **Action:** **HIGH (methods)** — read for the bound's assumptions
  (typically distribution-shift / propensity-overlap conditions) and
  whether it's data-driven or assumption-driven. Likely a recurring
  citation in your composite-risk and external-validation work.

### 9. TASC: a time-aware sequence clustering framework with uncertainty quantification for electronic health record trajectories
- **Authors / venue:** A.Y. Yan, T.K.M. Cudjoe, C.O. Taylor — *BioData Mining*, 2026.
- **Surfaced by:** "**All of Us research program**" keyword alert.
- **Thread:** Chronic disease clustering / multimorbidity (trajectory clustering) **+** EHR phenotyping (longitudinal sequences) **+** EHR-linked biobanks (AoU as the cohort, per the keyword hit).
- **What it is:** Time-aware sequence-clustering framework for EHR
  trajectories with *uncertainty quantification* attached to each cluster
  assignment. "Time-aware" implies the clustering respects irregular
  spacing between EHR events (not just bag-of-events); UQ on cluster
  assignment is the differentiating feature vs. standard k-means /
  k-prototypes on sequences.
- **Why it matters to you:** Direct hit on the multimorbidity-trajectory
  thread, with the twin features your INTERESTS implicitly prefers:
  irregular-time handling (which CLMBR/MOTOR-style FMs also do) and UQ
  (because cluster-label instability is the dominant criticism of
  trajectory-clustering work). Pairs with last report's *Rahemi & Omidi
  deterministic overlapping phenotypes* paper as a methods contrast —
  one is deterministic-rule-based, the other is probabilistic + UQ.
- **Action:** **HIGH** — read for the time-encoding choice (Hawkes-like?
  positional?), the UQ method (Bayesian non-parametric? bootstrap?), and
  the cluster-stability evaluation. Promising citation for trajectory-
  clustering rigor in AoU work.

### 10. The ROBOKOP v1.0 knowledge graph system for exploring relationships between biomedical entities
- **Authors / venue:** K. Fecho, E. Morris, J.M. Beasley, E.K. Carter, C.H. Chung et al. — *Scientific Reports*, 2026.
- **Surfaced by:** **Tiffany J. Callahan** "new related research" alert.
- **Thread:** Knowledge graphs & ontologies (biomedical KG construction for clinical reasoning) **+** Drug repurposing (KG-based reasoning).
- **What it is:** Formal release / description of *ROBOKOP v1.0* — a
  biomedical knowledge graph system for exploring relationships between
  biomedical entities (genes, drugs, diseases, phenotypes). ROBOKOP has
  been around in the Translator/NCATS ecosystem for a while; this
  appears to be the consolidated v1.0 *Scientific Reports* publication.
- **Why it matters to you:** Directly on the KGs/ontologies thread and
  on your *explainable* drug-repurposing preference — ROBOKOP-style
  systems emit human-readable reasoning paths (subgraph rationales)
  rather than raw embedding scores, which is exactly the rationale shape
  your INTERESTS calls out as on-thread. Callahan's appearance in the
  feed is the relevant author signal (HPO/ontology infrastructure
  intersection).
- **Action:** **HIGH** — skim for the v1.0 schema (which ontologies are
  integrated — HPO, MONDO, ChEBI, etc.?), the reasoning-path output
  format, and any benchmarked repurposing tasks. Useful baseline for
  evaluating any KG-based repurposing pipeline you build or read.

### 11. Using routinely collected data for research purposes: challenges and mitigation strategies
- **Authors / venue:** S. Hoffmann, T. Morris, M. Herrmann, G. Heinze et al. — *BMJ*, 2026.
- **Surfaced by:** **Miguel Hernán** "10 new citations" alert.
- **Thread:** Causal inference / pharmacoepidemiology (RWE/RWD design) **+** EHR phenotyping (data quality + biases in routinely collected data).
- **What it is:** BMJ methods-piece on the challenges of using routinely
  collected (administrative / EHR / registry) data for research, and
  mitigation strategies. The Hernán-citation surfacing implies the paper
  positions itself in the target-trial-emulation / observational-RWE
  intellectual lineage.
- **Why it matters to you:** A general-purpose RWE reference, useful as
  a citation when you justify RWD design choices in AoU/BioVU/MVP work.
  Will probably show up frequently as the canonical "things to watch out
  for" cite for routinely-collected-data studies — worth a read so you
  can use it as a shorthand reference in future drafts.
- **Action:** **HIGH (methods reference)** — read for the mitigation-
  strategy taxonomy (immortal-time bias? confounding by indication?
  outcome-misclassification? missing covariates?). Use as a methods
  citation pool.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Federated SPARQL querying for genomic variant functional annotation** —
  A. Bodrug-Schepers, R. Bourcier, R. Redon, A. Gaignard — arXiv
  2606.05918, 2026-06-04 (q-bio.QM, keyword hit: *knowledge graph*).
  Surfaced via `arxiv-digest` 2026-06-06. *Watch for:* federated KG /
  SPARQL pattern for variant annotation that avoids duplicating public
  databases locally — relevant to your variant-interpretation
  infrastructure if you're considering Translator-style or FAIR-aligned
  query layers. Use case is cerebral berry aneurysms (ICAN project) —
  not a tracked disease, but the federation architecture is portable.
- **Inferring the History of Admixed Populations Using Backwards
  Simulations and Local Ancestry Tracts** — C.Y. Su, A. Mejia-Garcia —
  *Evolutionary Biology*, 2026. (Konrad Karczewski "new related
  research" alert.) *Watch for:* local-ancestry-tract methodology
  improvements — relevant if you're doing local-ancestry-aware analyses
  in admixed AoU subcohorts (e.g., African American + Hispanic / Latino
  subgroups for APOL1 or HbA1c work).
- **A large-scale single cell map of primary and conditional regulatory
  variation in the human brain** — S. Lee, Z. Hamdan, S.S. Huntress, A.
  Yang, M.H. Guo — *medRxiv*, 2026. (Stephen B. Montgomery "new related
  research" alert.) Single-cell eQTL map in brain. *Watch for:* the
  conditional-regulatory-variation methodology — context-dependent eQTL
  detection is a recurring methods area transferable to your TWAS /
  fine-mapping work even though brain isn't a tracked tissue.
- **Critical Appraisal: Prognostic versus Predictive Surrogate Markers
  in Oncology** — A. Pabani, B. Gyawali — *JNCI*, 2026. (Bert Vogelstein
  "10 new citations" alert.) Prognostic-vs-predictive distinction is a
  perennial confusion in biomarker work. *Watch for:* the critical-
  appraisal framing — useful pedagogical reference when reviewing
  biomarker-as-exposure (vs. biomarker-as-effect-modifier) MR papers.

---

## arxiv-digest pipeline output — 2026-06-06

**Status:** 2 papers surfaced after a multi-day silent stretch (06-02 and
06-03 returned zero, with 06-03 logging the same 3/4 q-bio fetch failure
seen earlier).

| # | Title | Score | Categorization |
| --- | --- | --- | --- |
| arxiv-1 | Leveraging External Controls for Treatment Switching in RCTs (Shen, Fu, Lin) | 1 | **HIGH** — covered as item #4 above. |
| arxiv-2 | Federated SPARQL querying for genomic variant functional annotation (Bodrug-Schepers et al.) | 1 | **METHODS-WATCH** — covered in METHODS-WATCH section above. |

Both surfaced at `--min-score 1`. Neither is in a tracked disease, but
both are on the methods-thread. Net signal-to-noise from the pipeline is
positive this digest, the first non-empty output in over a week.

---

## SKIP / noise (logged, no action)

- **"UK Biobank" keyword alert:** Zeng/Lin/Lin/Hu/Fan/Yu "Associations
  between estimated glucose disposal rate and peripheral artery disease:
  evidence from the UK Biobank and NHANES" — UKB-anchored, but PAD/eGDR
  isn't a tracked outcome and the design is association-only without a
  TTE or composite-risk angle. SKIP.
- **"phenome wide association studies" keyword alert:** Ridker IL-6 JACC
  review — not a PheWAS paper, the keyword fires on adjacent text. SKIP
  (same pattern as the prior weeks). Consider tightening to require
  "phecode" or "PheRS" co-occurrence.
- **"mendelian diseases" keyword alert:** Wang et al. "An integrated
  machine learning and mendelian randomization approach identifies
  SERPING1 …" — MR paper, not a Mendelian-disease paper. Same recurring
  false-positive pattern flagged in the prior two reports — the
  `-randomization` exclusion suggestion still stands. SKIP.
- **"drug repurposing" keyword alert:** Kumar et al. *FusionTarget* —
  computational repurposing pipeline against modeled fusion-protein
  structures from genomic breakpoints. Pure structure/chemistry pipeline
  without an EHR or clinical-evidence loop — your INTERESTS explicitly
  flags this as *lower interest*. SKIP.
- **"electronic health records" keyword alert:** Adjei et al. CARE-link
  software-engineering paper for a diabetes EHR — application/software
  paper, no methods novelty. SKIP.
- **"knowledge graph" keyword alert:** Liu et al. *Personalized news
  recommendations based on knowledge graph with relational path guidance*
  — non-biomedical KG (news recommendation). Fourth consecutive week of
  non-biomedical KG noise on this keyword. The biomedical-co-occurrence
  recommendation from the prior report stands.
- **"autoimmune disorders/diseases" keyword alert:** Chiriac et al. on
  external-ear involvement in inflammatory skin disease — clinical
  dermatology review, off-thread. SKIP.
- **"rare diseases" keyword alert:** Sufian *Menopause in rare diseases*
  perspective piece (*Maturitas*) — position paper rather than a methods
  contribution. SKIP.
- **"Undiagnosed Diseases Network" keyword alert:** Chen/Avadhani et al.
  *Frequency of ZFHX3-Mediated Spinocerebellar Ataxia 4 in a US
  Undiagnosed Ataxia Cohort* — single-gene rare-disease prevalence
  study; useful clinical context but not on the rare-variant-method or
  HPO-pipeline angle. SKIP (borderline).
- **"variant interpretation" keyword alert:** Diogo-Cavassana et al.
  *Genetic Landscape of Hearing Loss in Brazilian Patients* — population-
  specific hearing-loss panel; useful as a regional reference but not
  methodologically novel for VUS resolution. Borderline SKIP (could be
  upgraded if you specifically track Brazilian-cohort variant
  frequencies).
- **"All of Us research program" keyword alert (other):** Foundation
  models / sensemaking learning-health-systems case study
  (Olorunnisola/Johnson/Subbian) — sociotechnical anesthesia case study,
  not an FM-methods paper. SKIP.
- **`intitle:"clonal hematopoiesis"` alert:** Krauß et al. *Clonal
  Hematopoiesis does not influence manufacturing of CAR T-Cells* —
  CAR-T manufacturing safety angle. Not on your CHIP-outcome /
  CV-outcome line, but logged for future CHIP-and-cellular-therapy
  context. Borderline SKIP.
- **Chenjie Zeng "new related research" alert:** Tanegashima et al. GWAS
  of radium-223 in mCRPC — pharmacogenomics in a narrow oncology
  setting; not on the pharmacoepi/AoU thread. SKIP.
- **Author-feed citation churn:** Vogelstein / Szolovits / Zitnik /
  Natarajan / Shendure / Pritchard / Rajpurkar / Baker citation feeds
  continued to return generic LLM / structural-biology / oncology
  citations that don't overlap with active threads. SKIP.

---

## Suggestions for the pipeline

Carrying forward from prior reports, plus a 06-06-specific note:

1. **`arxiv-digest` pipeline reliability remains the top item.** 06-03
   logged the same q-bio.QM / q-bio.GN / q-bio.PE fetch failures seen on
   05-31 — third instance of this exact failure mode. 06-06 recovered
   and surfaced two relevant papers, so the recall is not zero, but the
   intermittent failures imply the upstream fetcher needs a proper retry
   loop and back-off. Suggest investigating: (a) is arXiv rate-limiting
   the same IP every few days? (b) does the fetcher distinguish 4xx vs
   5xx? (c) consider an `email_alert_on_partial_fetch` so the
   3-of-4-failed digests don't pass silently.
2. **Tighten `apol1`, `mendelian diseases`, `knowledge graph`, and
   `phenome wide association studies` keyword queries.** All four
   recurred as noise this window. The suggestions from the prior reports
   stand verbatim.
3. **Add `proteome-wide` / `colocalization`** — now the fifth
   incarnation of the MR-for-target-prioritization template across
   recent windows (today's ter Kuile depression paper). This is clearly
   a recurring high-value shape worth surfacing automatically.
4. **Add `OHDSI Network Study` / `OMOP Network` as keyword aliases.**
   Today's Cai et al. semaglutide-AMD paper is one of multiple OHDSI
   network designs in your active reading; capturing this study design
   as a tracked phrase would catch this class earlier.
5. **The author-feed citation churn is structurally noisy.** ~60% of the
   author-citation alerts on 06-06 were generic LLM / structural-biology
   citations unrelated to the tracked thread. Consider a second-stage
   filter on author-citation alerts that requires keyword overlap with
   `tracked.yaml` before promotion — the author signal alone is too
   diffuse without a topical anchor.
6. **Self-citation handling:** the prior-report Yang/Schaffer/Tran/Zeng/
   Park self-citation in the AoU feed did not recur this window (no
   `Chenjie Zeng - new related research` hits on-thread today either,
   beyond the off-thread radium-223 GWAS). Defer the `-author:zeng`
   filter for now.
