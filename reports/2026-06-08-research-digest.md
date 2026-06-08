# Research digest — 2026-06-08

Compiled from (a) Google Scholar alert emails in the last 7 days and
(b) the local arXiv-digest files at `digests/2026-06-06.md` and
`digests/2026-06-07.md`. Triaged against the active threads in
`INTERESTS.md` (last updated 2026-04-30).

## Email landscape (7-day window)

Inbox state for `cezeng21@gmail.com`:

- **Author-following alerts** (~25 threads, all from
  `scholaralerts-noreply@google.com` dated 2026-06-07): Christopher G.
  Chute, Marinka Zitnik, George Hripcsak, Patrick Ryan, Jian Yang,
  Konrad Karczewski, Joshua C. Denny, Lisa Bastarache, Daniel Kastner,
  Stephen B. Montgomery, Tiffany J. Callahan, Pascal Brandt, Jay
  Shendure, Peter Szolovits, James Zou, Miguel Hernán, Jure Leskovec,
  Vivek Natarajan, Peter Visscher, Quoc V. Le, Bert Vogelstein, Yuan
  Luo, plus a self-citation alert for "Chenjie Zeng".
- **Keyword alerts** (2026-06-06 → 2026-06-08): `"All of Us research
  program"` (2 batches), `"UK Biobank"` (2 batches), `"electronic
  health records"`, `"Foundation models" + EHR`, `"drug repurposing"`,
  `"knowledge graph"`, `"variant interpretation" / "variant
  classification"`, `"autoimmune disorders"`, `"rare diseases"`,
  `"mendelian diseases"`, `APOL1`, `"Undiagnosed Diseases Network"`.
- **arXiv-digest from GitHub** (committed to this repo): `2026-06-06.md`
  surfaces **2 papers** at min-score 1; `2026-06-07.md` is empty (one
  paper from the previous day suppressed as already seen). No emails
  from the GitHub Action — the digest is a markdown file checked into
  `digests/`.
- **Off-topic noise** ignored: LinkedIn, Substack, etc.

Below: detailed reports on the 12 studies that map cleanly onto active
threads, in roughly descending priority.

---

## 1. HIGH — Agentic Authoring of OMOP Concept Sets from Natural Language

**Authors:** H. Chen, X. He, H. Dai, Y. Huang, M. Liu, J. Bian
**Venue:** medRxiv 2026 (preprint, 2026.06.02)
**Surfaced via:** Christopher G. Chute author alert
**Threads served:** EHR phenotyping & OMOP; ML for precision health

**Summary.** Free-text → OMOP concept set authoring is the choke point
for scalable computable phenotyping in OHDSI-style observational
research. Existing tools (ATLAS, CONCEPTOR) require expert
interaction; the authors propose an LLM-agentic pipeline that takes a
natural-language phenotype description and returns a curated OMOP
concept set with provenance.

**Why it's HIGH for you.** Directly overlaps the OMOP-based phenotyping
thread and the LLM-assisted phecode/HPO assignment angle. Pair it with
the existing concept-set scaffolding for All of Us / OMOP-CDM work —
this could meaningfully reduce the human-curation burden when
producing phenotypes for biobank PheWAS-style scans.

**To read for.** (i) Does the agent expose a vocabulary-aware critic
that can catch the false-positive "child concept" inclusions that
defeat naive LLM concept-set drafts? (ii) Evaluation set — are they
benchmarking against a manually curated reference, and what's the
recall/precision per phenotype family (chronic vs. rare)?

**Link.** medRxiv 10.64898/2026.06.02.26354704

---

## 2. HIGH — Bridging Ancestry Gaps in Genomic Risk Prediction with Tabular Foundation Models

**Authors:** A. Das, Y. Cui
**Venue:** bioRxiv 2026 (preprint, 2026.05.29)
**Surfaced via:** Konrad Karczewski author alert
**Threads served:** Genetic epidemiology (PRS portability); ML for
precision health; biobanks

**Summary.** Standard PRS underperform in non-European ancestries
because of sample-size imbalance and non-stationarity of effect sizes.
The authors adapt **tabular foundation models** (a la TabPFN-lineage)
to genotype matrices and show that cross-ancestry transfer is
materially improved over PRS and standard ML baselines.

**Why it's HIGH for you.** This sits at the intersection of the
trans-ancestry PRS thread and the EHR-foundation-model thread —
specifically the "ancestry-stratified risk in EHR-linked cohorts"
sub-question. If the architecture genuinely transfers across UKB →
AoU / MVP genotype panels, it's directly useful for the composite
risk-model stacking (PRS + rare pathogenic variants) work.

**To read for.** External validation panels (which ancestries, which
diseases, how the AFR/AMR gap closes vs. baseline). Whether the model
is open-weight enough to drop into an AoU Researcher Workbench
environment.

**Link.** bioRxiv 10.64898/2026.05.29.728877

---

## 3. HIGH — TASC: time-aware sequence clustering with uncertainty quantification for EHR trajectories

**Authors:** A. Y. Yan, T. K. M. Cudjoe, C. O. Taylor
**Venue:** BioData Mining 2026
**Surfaced via:** "All of Us research program" keyword alert
**Threads served:** Chronic disease clustering & multimorbidity; EHR
phenotyping; biobanks (AoU)

**Summary.** Trajectory-clustering of EHR sequences with explicit
uncertainty quantification. Demonstrated on 2,052 total knee
replacement patients in **All of Us**, building temporally ordered
visit sequences and clustering them into post-op trajectories.

**Why it's HIGH for you.** Two thread hits — chronic-disease/sequence
clustering AND it's on AoU. The uncertainty-quantification angle is
the differentiator vs. plain LCMM / topic-model trajectory work
(matters when downstream clinicians have to act on cluster
assignment). The TKR case study is a tractable proof of concept that
could be replicated for autoimmune flare or CKM-multimorbidity work.

**To read for.** Calibration of the cluster-membership uncertainty
estimates against held-out outcomes; sensitivity to coding density
heterogeneity across AoU sites.

**Link.** BioData Mining: link.springer.com/article/10.1186/s13040-026-00569-7

---

## 4. HIGH — Machine Learning Algorithms for Predicting Glycemic Control and Weight Loss Outcomes in GLP-1 Receptor Agonist Users

**Authors:** T. M. Abegaz, G. Frietze
**Venue:** Frontiers in Artificial Intelligence 2026
**Surfaced via:** "All of Us research program" keyword alert
**Threads served:** Causal inference & pharmacoepidemiology (GLP-1 RA
sub-thread); biobanks (AoU); ML for precision health (HTE / treatment
response)

**Summary.** Retrospective cohort in AoU of adults initiating GLP-1
RA therapy with paired baseline/follow-up labs and weight. Two
cohorts — glycemic-response and weight-response — modeled
independently with standard ML classifiers.

**Why it's HIGH for you.** Active thread on GLP-1 RA pharmacoepi, and
on AoU. The "who responds" question is one of your stated
HTE-meta-learner / causal-forest interests. Read this critically — if
they're predicting a post-baseline outcome without target-trial
framing, treatment-confounded selection will limit causal
interpretation; but the AoU cohort design and feature set are
re-usable.

**To read for.** Cohort entry definitions (incident vs. prevalent
user), handling of switching/adherence, calibration & decision-curve
analysis (your stated bar), and whether they attempt a causal
contrast or only predictive accuracy.

**Link.** doi.org/10.3389/frai.2026.1861563

---

## 5. HIGH — Polygenic Risk Scores for Prediction of Immune Checkpoint Inhibitor Thyroid Toxicity in Diverse Populations

**Authors:** L. G. Fritsche, L. M. Higgins, M. Schipper, G. Strohbehn et al.
**Venue:** Clinical Cancer Research 2026
**Surfaced via:** Lisa Bastarache + Joshua C. Denny author alerts (two threads, same paper)
**Threads served:** Genetic epidemiology (PRS cross-ancestry);
pharmacoepidemiology; ML for precision health (treatment-related ADR)

**Summary.** Develops and validates a PRS for immune checkpoint
inhibitor–induced thyroid dysfunction across ancestrally diverse
cohorts. Two of your tracked authors flagged it — usually a signal of
strong cross-cutting relevance.

**Why it's HIGH for you.** Three thread hits: PRS portability,
pharmaco-genomics / drug-class outcomes (ICI), and EHR-linked diverse
biobank cohorts. This is the type of "PRS tied to a clinical decision"
paper your triage rubric upgrades over a generic GWAS PRS paper.

**To read for.** Calibration in non-EUR subsets; whether they stack
the PRS with thyroid-autoantibody status or HLA effects; effect-size
attenuation curves across ancestry.

**Link.** Clinical Cancer Research 2026 (via Scholar alert).

---

## 6. HIGH — Monogenic and Polygenic Contributions to Cardiomyopathy and Heart Failure Across Diverse Populations

**Authors:** N. Pereira, J. Tan, O. Dikilitas, M. Figueiral, J. Tan-Arroyo et al.
**Venue:** Research Square preprint rs-9581360, 2026
**Surfaced via:** Konrad Karczewski author alert
**Threads served:** PheWAS / penetrance estimation; genetic
epidemiology (composite PRS + rare-variant); biobanks; ML for
precision health

**Summary.** Cardiomyopathy gene pathogenic variant carriers
typically come from clinically ascertained cohorts; population
prevalence and age-specific penetrance are poorly characterized. The
authors estimate population-level penetrance for cardiomyopathy genes
**and** test whether polygenic background modifies risk in carriers,
across diverse ancestries.

**Why it's HIGH for you.** This is essentially the canonical use case
described in your PheWAS / penetrance section ("penetrance estimation
for monogenic variants under population-screening conditions vs.
clinically ascertained cohorts"), applied to cardiomyopathy with the
composite PRS-on-top-of-monogenic design you've called out as a
target.

**To read for.** Which biobanks were combined; the
"population-screening vs. clinical-ascertainment" correction strategy;
whether age-specific penetrance curves stratify by ancestry; the
sample sizes for AFR/AMR carriers (usually the bottleneck).

**Link.** researchsquare.com/article/rs-9581360

---

## 7. HIGH — Influence of Combination Therapy with SGLT2 Inhibitors and GLP-1 RAs on Blood Pressure (Japanese Type 2 Diabetes)

**Authors:** T. Matsushita, Y. Wada, M. Saburi, K. Kobayashi et al.
**Venue:** (Scholar alert; venue truncated)
**Surfaced via:** Patrick Ryan author alert
**Threads served:** Causal inference & pharmacoepidemiology (SGLT2i +
GLP-1 dual-class)

**Summary.** Real-world cohort study quantifying BP effects of dual
SGLT2i + GLP-1 RA therapy vs. monotherapy or other regimens in
Japanese T2DM patients.

**Why it's HIGH for you.** Directly addresses the dual drug-class
thread (SGLT2i + GLP-1). Patrick Ryan flagging it suggests OHDSI-style
methods context. Most "combination therapy" papers are descriptive —
worth checking whether they emulated a target trial or relied on
adjusted regression.

**To read for.** Population transportability — Japanese T2DM cohort
effect sizes may not transfer to US AoU; check the active-comparator
new-user design, and whether they handled prescribing-channelling bias.

---

## 8. HIGH — Update on APOL1 and Chronic Kidney Diseases in Children

**Authors:** J. D. Varner, T. O. Ilori, R. A. Gbadegesin
**Venue:** Pediatric Nephrology 2026
**Surfaced via:** `APOL1` keyword alert
**Threads served:** APOL1 (specific disease thread); rare disease;
genetic epidemiology

**Summary.** Narrative update on APOL1-associated kidney disease in
pediatrics, including transplant outcomes and pregnancy effects.

**Why it's HIGH for you.** APOL1 is a named thread. Even though this
is a review, the pediatric and transplant-decision angles are exactly
the "transplant decision-making, ancestry considerations" sub-bullet
in your INTERESTS.md.

**To read for.** Any new penetrance estimates by APOL1 genotype
combination (G1/G2 homozygous vs. compound); the transplant-donor
screening recommendations; pregnancy outcome data is usually thin —
note any cohort it cites.

---

## 9. HIGH — A Causal Discovery Framework for Digital Phenotyping

**Authors:** A. Ibrahim
**Venue:** Scientific Reports 2026
**Surfaced via:** George Hripcsak author alert
**Threads served:** Causal inference; EHR phenotyping; ML for
precision health

**Summary.** Applies causal discovery (structure learning over the
DAG of behavioral signals) to digital-phenotyping streams from
phones/wearables.

**Why it's METHODS-WATCH / borderline HIGH.** Causal discovery
methodology you could lift into an EHR-trajectory setting — your
chronic disease clustering / multimorbidity thread benefits from
moving past association toward causal structure. Digital phenotyping
data is a different modality than typical EHR codes, so primary
disease relevance is moderate.

**To read for.** Identifiability assumptions, sample size needed for
stable structure recovery, and whether the framework handles latent
confounders (key for any port to EHR/biobank).

---

## 10. HIGH — Leveraging External Controls for Treatment Switching in RCTs: A Weighted Causal Inference Framework

**Authors:** A. A. Shen, C. Fu, R. Lin
**Venue:** arXiv 2606.06441 (stat.ME)
**Surfaced via:** local arXiv-digest `digests/2026-06-06.md` (score 1, keyword: "causal inference")
**Threads served:** Causal inference & pharmacoepidemiology

**Summary.** Treatment switching in oncology RCTs breaks the
randomization guarantee. The authors propose synthetic-control +
balancing-weight estimators with multiple imputation and time-varying
weights, plus criteria for selecting the external-control risk set.
Demonstrated on two Phase III oncology trials.

**Why it's HIGH for you.** Maps onto the target-trial-emulation and
weighting-method threads. Useful machinery if you're augmenting an
AoU/MVP observational arm onto an existing RCT — relevant for any
real-world-evidence project where switching contaminates the ITT
contrast.

**To read for.** How the external-control selection criteria avoid
amplifying unmeasured confounding; comparison vs. RPSFT and IPCW
baselines; whether the variance estimator accounts for both
imputation and weight uncertainty.

**Link.** arxiv.org/abs/2606.06441

---

## 11. METHODS-WATCH — Retrieval-Augmented Foundation Model Enhances Risk Prediction Using EHRs

**Authors:** S. Shurrab, M. Al-Omari, D. El Samad, F. E. Shamout
**Venue:** Workshop on Multi-modal Foundation Models (likely MIDL/NeurIPS 2026 workshop)
**Surfaced via:** `Foundation models + "electronic health records"` keyword alert
**Threads served:** EHR foundation models (CLMBR / MOTOR / EHRSHOT
lineage); ML for precision health

**Summary.** RAG-augmented EHR foundation model — instead of relying
solely on parametric memory, the model retrieves similar past
trajectories at inference time and conditions risk prediction on
them.

**Why it's METHODS-WATCH.** Direct hit on the FM thread. Worth
checking whether they evaluate on EHRSHOT, MEDS, or proprietary; how
they handle the retrieval-index ancestry/site composition (a known
fairness failure mode for retrieval-augmented clinical models).

---

## 12. METHODS-WATCH — Early vs. Delayed Primary Local Therapy and Survival in De Novo Metastatic Prostate Cancer: Target Trial Emulation

**Authors:** A. A. Hassan, A. Y. Aboelsaad, A. M. A. Gawad et al.
**Venue:** World Journal of Urology 2026
**Surfaced via:** Miguel Hernán author alert
**Threads served:** Causal inference & pharmacoepidemiology (target
trial emulation)

**Summary.** A classic target-trial-emulation applied to a treatment
timing question (early vs. delayed local therapy) in metastatic
prostate cancer.

**Why it's METHODS-WATCH.** Disease is off your active list, but it's
a clean exemplar of the target-trial design you cite as a methods
goal — particularly the protocol-specification step and the handling
of intercurrent therapies. Use as a methods reference if you draft an
AoU/MVP target-trial protocol for a tracked drug class.

---

## Suppressed / lower-priority hits (logged, not detailed)

- **Toward Precision Electrochemical Sensing of CFTR Function in CF
  Models** (Miglione et al., Anal Chem 2026; Chenjie Zeng author
  alert) — CFTR thread but a biosensor / functional-assay paper, not
  pharmacoepi or modulator outcomes. SKIP unless you want it for
  background.
- **Trans-ethnic estimation of genetic impact on continuous glycemic
  profiles** (Yu et al., Cell Discovery 2026) — cross-ancestry GWAS
  on glycemic traits; relevant to the GLP-1 / metabolic thread but
  not directly drug-class. METHODS-WATCH.
- **Federated SPARQL querying for genomic variant functional
  annotation** (Bodrug-Schepers et al., arXiv 2606.05918) — knowledge
  graph thread, but the focus is FAIR-data plumbing for variant
  annotation of cerebral aneurysm cohorts, not biomedical KG
  construction for clinical reasoning. SKIP.
- **Polygenic Score for Prostate Cancer Aggressiveness** (Xu et al.,
  medRxiv) — adjacent to your PRS-decision-utility interests but
  prostate cancer is not a tracked disease. METHODS-WATCH.
- **Registry Forge: SMART-on-FHIR registries** (Boyce et al., medRxiv)
  — adjacent infra paper. SKIP.

---

## Suggested next actions

1. Read items **1, 2, 3, 6** first — each hits ≥2 active threads with
   direct methodological transferability to your AoU / biobank work.
2. Item **5** (ICI thyroid PRS) for the cross-ancestry PRS-with-
   clinical-decision use case; could anchor a parallel template for
   tracked drug classes.
3. Items **10, 12** are pure methods reads — useful templates if you
   draft a target-trial / external-control protocol for SGLT2i +
   GLP-1 combination work.
4. The local arXiv-digest signal was thin this window (0–2 papers
   per day). Consider lowering `--min-score` for a backfill run, or
   broadening keywords in `config/tracked.yaml` if you want more
   recall in the q-bio.QM / stat.AP feeds.
