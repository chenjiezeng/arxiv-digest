# Research digest report — 2026-07-28

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-23 12:00Z → 2026-07-28 12:00Z** (five days since the
last committed report at `reports/2026-07-23-research-digest.md`). Longer
window than the typical daily follow-on because several weekend days
had light signal — batching them into a single Monday report avoids
five near-empty files.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author-feed cluster) | 2026-07-24 09:02Z, 2026-07-26 05:17Z, 2026-07-27 14:34Z | Three batches. 07-27 was the largest (Denny, Bastarache, Karczewski, Hripcsak, Ryan, Szolovits, Callahan, Zitnik, Yang author feeds all fired). On-thread highlights: **Wang binary-silver-labels EHR phenotyping paper** (surfaces 3× — Ryan/Brandt/Hripcsak related), **Tang GLP-1 hair-loss target-trial-emulation** (surfaces via Hernán + Ryan), Feng cross-ancestry depression imaging PGS, PrimeKG-Plus KG expansion, DPCGS GWAS→scRNA-seq framework. |
| Google Scholar alerts (keyword feeds) | 2026-07-25 03:27Z, 2026-07-26 11:32Z | Two batches. On-thread hit: **Corsi-Zuelli methotrexate-vs-psychosis EHR cohort** (electronic health records feed). Off-thread: Wang UKB dietary metabolic syndrome, García rare-disease variant-curation review, Pärna eating-disorder GWAS, fibromyalgia drug-repurposing review. |
| NCBI "My NCBI What's New" ("All of Us", "UK Biobank", "drug repurposing") | 07-23 → 07-27 daily | 15 emails total. Most days had 1–4 hits per feed, low on-thread density. Notable: Barua AoU accelerometer + inflammatory arthritis (07-26), Hausman-Kedem sapropterin repurposing for ACTA2 rare disease (07-27), Chong metformin ulcerative colitis systematic review (07-27). |
| `arxiv-digest` repo (`digests/2026-07-24.md` → `digests/2026-07-28.md`) | 07-24 → 07-28 (10:30Z cron) | 5 papers surfaced across 5 days (07-25 and 07-26 empty). On-thread hits: **Chou `oci-agent` Netflix causal-inference agentic workflow** (07-27, score 2), **Parikh `Towards Optimal Estimators for RCTs`** (07-28, score 1; Jordan/Foster/Volfovsky author panel), Ali scContam single-cell FM contamination audit (07-24). |
| bioRxiv / medRxiv Subject Collection Alerts | 07-23 → 07-28 daily | Aggregate feeds — individual papers surfaced upstream via Scholar / NCBI. Not a separate net. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it.

---

## Executive summary

- **Silver-labels for computable phenotyping — arXiv preprint hits three
  Scholar author feeds at once.** Wang, Slaughter, Nelson, Williamson,
  *Using binary silver labels in electronic health records-based
  computable phenotyping algorithms* (arXiv 2607.18431, 2026;
  surfaces via Ryan, Brandt, and Hripcsak Scholar related-research
  feeds on 2026-07-26). Gold-labelled cases are expensive; this paper
  formalizes how imperfect ("silver") labels — e.g. rule-based
  proxies, code-only definitions, or LLM extractions — can be
  combined statistically to train computable phenotypes without a
  large chart-reviewed gold set. Triple-feed hit across three
  Ryan/OHDSI/Karolinska-adjacent name feeds signals a paper the
  computable-phenotype community is likely to converge on. **HIGH —
  read first for the EHR phenotyping / OMOP thread.**
- **GLP-1 receptor agonists and hair loss — TTE in BMJ.** Tang,
  Zhang, Lu, Zhang, Liu, Lu et al., *Risk of hair loss associated
  with glucagon-like peptide-1 receptor agonists in adults with type
  2 diabetes: target trial emulation* (BMJ 2026; Hernán citation feed
  **and** Ryan related feed on 2026-07-27). Explicit target-trial
  emulation methodology applied to a novel safety signal for the
  GLP-1 drug class you're actively tracking. **HIGH — direct
  causal + pharmacoepi + GLP-1 triple-thread hit.**
- **Netflix `oci-agent` — human-in-the-loop agentic workflow for
  observational causal inference.** Chou, Alexandre, Olds, Zhang,
  Kallus, *A Human-Augmenting Agentic Workflow for Observational
  Causal Inference* (arXiv 2607.22443, submitted 2026-07-24;
  `arxiv-digest` 2026-07-27, score 2 — propensity score + causal
  inference). Open-source Python package that automates covariate
  balance checking, propensity trimming, sensitivity analysis while
  keeping humans in the loop for framing and diagnostics. Running
  >100 analyses/month at Netflix since June 2026. Directly on the
  causal-inference + ML-for-precision-health threads. **HIGH.**
- **Cross-ancestry pleiotropic analysis of imaging phenotypes for
  depression risk stratification — Molecular Psychiatry.** Feng,
  Guo, Huang, Jia, Hu, Yang, *Cross-ancestry pleiotropic analysis of
  imaging-derived phenotypes enhances risk stratification of
  depression* (Molecular Psychiatry 2026; Denny related-research feed
  on 2026-07-27). Cross-ancestry pleiotropy on imaging-derived
  phenotypes for depression risk. On the cross-/trans-ancestry
  portability sub-thread and the imaging-genomics sub-thread. **HIGH.**
- **Optimal estimator selection for RCTs — Jordan/Foster/Volfovsky
  author panel.** Parikh, Levin-Konigsberg, Tripuraneni, Madeka,
  Jordan, Foster, Perrault-Joncas, Volfovsky, *Towards Optimal
  Estimators for Randomized Control Trials* (arXiv 2607.23254,
  submitted 2026-07-25; `arxiv-digest` 2026-07-28, score 1 — causal
  inference). Sample-splitting framework for choosing between
  weighted-least-squares, difference-in-means, and covariate-adjusted
  estimators based on analytical objective (inference vs. decision
  regret). Runs on Amazon SCOT trials + Strengthening Democracy
  Challenge (25 interventions). On the causal-inference /
  double-ML sub-thread; useful as an estimator-selection reference
  when a family of RCTs is being analyzed. **HIGH.**
- **Low-dose methotrexate against incident psychosis — retrospective
  EHR cohort.** Corsi-Zuelli, Taquet, Deakin et al., *Potential
  preventive role of low-dose methotrexate against incident recorded
  psychosis: a retrospective cohort study based on electronic health
  records* (Scholar "electronic health records" feed on 2026-07-26).
  Taquet on the author list places this in the TriNetX / OxCGRT
  EHR-drug-repurposing lineage. Pairs the drug-repurposing thread
  with the EHR-phenotyping thread — psychosis as an
  EHR-recorded outcome, methotrexate as an anti-inflammatory
  repurposing candidate. **HIGH.**
- **PrimeKG-Plus — literature-derived expansion of a multimodal
  precision-medicine knowledge graph.** Nguyen, Nguyen-Phuong,
  Nguyen et al., *PrimeKG-Plus: a literature-derived expansion of a
  multimodal precision medicine knowledge graph* (bioRxiv 2026;
  Zitnik related-research feed **and** Callahan related-research
  feed on 2026-07-26). Zitnik-lab-adjacent PrimeKG has been the
  reference multimodal precision-medicine KG for drug repurposing
  and rare-disease work; a literature-derived expansion extends its
  coverage. **HIGH for the knowledge-graph + drug-repurposing
  threads.**
- **DPCGS — computational framework linking GWAS to single-cell
  transcriptomics.** Liu, Shen, Li, Zhu, Yang, Wu, Xuan et al.,
  *DPCGS: a computational framework for linking GWAS to single-cell
  transcriptomics in complex traits and diseases* (bioRxiv 2026;
  Yang related-research feed on 2026-07-26). GWAS-to-cell-type
  attribution — parallels the sc-DRS / MAGMA / scGWAS reference
  class. Relevant for TWAS-adjacent and cell-type-of-action
  questions. **HIGH.**
- **Eze GLP-1 RA cancer outcomes systematic review.** Eze, Ntakirutimana,
  et al., *Cancer outcomes and biological mechanisms among patients
  with type 2 diabetes mellitus using glucagon-like peptide-1
  receptor agonists: a systematic review and meta-analysis*
  (Hripcsak citations feed on 2026-07-27). Pairs with the Tang
  BMJ TTE hair-loss paper above — same drug class, complementary
  outcome sweep. Signal that GLP-1-outcome pharmacoepi is a hot
  topic across multiple review venues right now. **HIGH.**
- **Sapropterin (Kuvan) repurposed for ACTA2 rare-disease.**
  Hausman-Kedem, Bielopolski, Krishnan et al., *Re-Purposing
  Sapropterin (Kuvan) for ACTA2-Related Multisystemic Smooth Muscle
  Dysfunction Syndrome: A Translational Mechanistic and
  First-In-Human Therapeutic Report* (Ann Clin Transl Neurol
  2026-07-26; NCBI drug-repurposing feed on 2026-07-27). Combined
  mechanistic + first-in-human report for a repurposed indication
  of a PKU drug in an ultra-rare vascular disease. On the
  drug-repurposing + rare-disease intersection. **MEDIUM-HIGH.**

Everything else in this window is either off-thread (esophageal cancer
smoking burden, kidney stone × physical activity in AoU, McConnell's
sign case report, prostate PSMA imaging registry, Chinese herbal
repurposing for multiple myeloma, dietary index → gastric cancer),
methods-watch-only (see tail), or previously covered (Wu UKB
metabolic-syndrome exome-wide scan, Żebrowska circadian imbalance
GWAS-PheWAS-MR, Johnson AoU disparities cross-sectional — all
appeared in the 07-23 report).

---

## Detailed reports

### 1. Using binary silver labels in electronic health records-based computable phenotyping algorithms

**Authors.** S Wang, MT Slaughter, JC Nelson, BD Williamson.
**Venue.** arXiv preprint arXiv:2607.18431, 2026.
**Signal source.** Google Scholar author-feed for **Patrick Ryan** —
new related research (2026-07-26 05:17Z); also fires **Pascal
Brandt** related-research feed and **George Hripcsak**
related-research feed the same day. Triple-feed hit across three
OHDSI-adjacent name feeds.
**Bucket.** HIGH.
**Threads served.** EHR phenotyping & OMOP (computable-phenotype
methodology); ML for precision health (weak-supervision-adjacent
statistical methods); PheWAS / phecode infrastructure (silver-label
strategies are directly applicable to phecode definition).

**What the paper does (from title + snippet).** Gold-labeled cases
(from expert chart review) are the standard reference for computable
EHR phenotypes but expensive to produce at scale. This paper
formalizes how *binary silver labels* — imperfect but cheap
labels such as rule-based ICD-code definitions, prescription-history
proxies, or LLM extractions — can be combined statistically to
train computable phenotypes without a large chart-reviewed gold
set. The Williamson / Slaughter authorship anchors this in the
Kaiser Permanente Washington biostatistics / Karolinska-adjacent
KPWHRI methods stack — same lineage as recent PheValuator and
KOMAP work in your reference class.

**Why it matters for your work.**
1. **Bridges the PheValuator lineage.** PheValuator (Swerdel et al.)
   already estimates PPV / sensitivity from probabilistic gold
   labels; silver-label estimation is the natural upstream question
   — how to *build* better silver labels (rules, LLM extractions,
   claims-based proxies) and combine them statistically. Directly
   on the EHR phenotyping thread and reference for any AoU / MVP /
   BioVU phenotype where chart review is impractical.
2. **Portable to phecode-based outcome definitions.** PheWAS work
   depends on phecode definitions that are effectively silver-labels
   (aggregations of ICD codes) — this paper's silver-label
   combination machinery is a natural fit for improving phecode-based
   outcome ascertainment when multiple imperfect definitions exist
   (e.g. Denny 2010 phecodes + phecodeX + custom rule set).
3. **Complements the LLM-extraction-as-silver-label direction.**
   Recent work has proposed using LLM extractions from clinical
   notes as silver labels for downstream training — this paper
   supplies the statistical scaffolding for combining an LLM
   silver-label with rule-based silver-labels responsibly.

**Follow-ups.** Pull the arXiv PDF (2607.18431); check (a) the
statistical framework — is this a HMM / latent-class / MPLE style
combination, or a weak-supervision (Snorkel-style) label model?
(b) empirical results — which real-world phenotype was used to
demo? (c) whether they release code, and (d) whether it's tested
under label-conditional-independence violations (the standard
weak-supervision failure mode).

---

### 2. Risk of hair loss associated with glucagon-like peptide-1 receptor agonists in adults with type 2 diabetes: target trial emulation

**Authors.** H Tang, B Zhang, Y Lu, D Zhang, R Liu, Y Lu et al.
**Venue.** *BMJ*, 2026.
**Signal source.** Google Scholar author-feed for **Miguel Hernán**
— new citations (2026-07-27 14:34Z); also fires **Patrick Ryan**
related-research feed the same day. Double-feed hit across the two
canonical target-trial-emulation / pharmacoepi feeds.
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi (explicit
target-trial emulation for a new drug-safety signal); GLP-1
drug-class thread; biobanks with EHR linkage (TTE implementation
typically uses a linked EHR + claims cohort).

**What the paper does (from title).** Textbook target-trial
emulation applied to the GLP-1 receptor agonist drug class,
testing whether GLP-1 RA exposure is associated with incident
hair loss in adults with type 2 diabetes. The choice of *BMJ* as
venue (rather than a specialty pharmacoepi journal) plus the
Hernán-adjacent methodology suggests a rigorously designed
new-user active-comparator TTE — likely GLP-1 RA vs. DPP-4i
or vs. SGLT2i, with cloning-and-splitting on the "start-of-drug"
grace period.

**Why it matters for your work.**
1. **Direct GLP-1 pharmacoepi hit.** GLP-1 RAs are on your active
   drug-class list. Adverse-effect TTEs for GLP-1s (previously:
   pancreatitis, thyroid cancer, gastroparesis) are the
   pharmacoepi frontier for this class — hair loss adds a
   dermatologic signal that's likely to attract further
   TTE replication attempts. Read the design section closely.
2. **Companion to the Saxby metformin-AAA TTE from the 07-23
   report.** Both papers are TTEs applied to specific drug-class
   safety / efficacy signals. Two clean applications of the same
   design pattern in the same week suggests the TTE literature is
   consolidating around a stable methodological template. Cite
   Tang and Saxby together whenever proposing a similar TTE for
   CFTR modulator, SGLT2i, or hereditary-cancer-population
   drug-exposure questions.
3. **BMJ placement matters.** BMJ TTEs typically have high
   scrutiny of the "no-loss-to-immortal-time-bias" grace-period
   design and the active-comparator choice — a TTE published in
   BMJ is a good methodological reference to hand a trainee.

**Follow-ups.** Pull the BMJ paper; check (a) the exact active
comparator (DPP-4i? SGLT2i?), (b) the cohort source (Optum? MarketScan?
UKB?), (c) hair-loss outcome definition (ICD-derived alopecia codes?
prescription-history-derived?), (d) grace-period handling, (e)
negative-control outcomes for residual confounding.

---

### 3. A Human-Augmenting Agentic Workflow for Observational Causal Inference

**Authors.** W Chou, A Alexandre, L Olds, Y Zhang, N Kallus.
**Venue.** arXiv preprint 2607.22443, submitted 2026-07-24
(primary category stat.CO).
**Signal source.** `arxiv-digest` 2026-07-27 — keyword hits
"propensity score" + "causal inference", score 2.
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi (workflow
automation for OCI); ML for precision health (agentic AI for
methods-heavy tasks); knowledge graphs / ontologies (indirectly —
the workflow's "codified analyst" is a form of process ontology).

**What the paper does (from abstract).** Introduces `oci-agent`,
an open-source Python package implementing a human-in-the-loop
agentic workflow for observational causal inference. Automates
laborious tasks — covariate balance checking, propensity score
trimming, sensitivity analysis — so that humans focus on the
harder cognitive work of question framing and assumption
scrutiny. Initially open-sourced June 2026 with doubly-robust ATE
estimation; has since added heterogeneous-treatment-effect
estimation and multiple-continuous-treatment support via
partially linear models. Netflix uses it for >100 analyses/month.

**Why it matters for your work.**
1. **First "agentic OCI" package with real production usage.**
   The distinction from most causal-inference agent papers is
   the *deployed* claim — 100+ analyses/month at Netflix since
   June is production-scale evidence that this framework works,
   not just a demo. Directly relevant if you plan any
   agent-assisted causal-inference workflow for AoU or biobank
   pharmacoepi work.
2. **The task decomposition itself is worth reading.** Which OCI
   tasks did they judge automatable (balance-checking, trimming,
   sensitivity) versus reserved for humans (framing, assumption
   evaluation, diagnostics)? That decomposition is a portable
   design pattern for any "which analyst tasks should an LLM own"
   question in EHR pharmacoepi.
3. **Kallus authorship.** Nathan Kallus is one of the current
   authorities on causal ML (double / debiased ML, DR learners) —
   worth checking the DR-learner + causal-forest implementation
   choices against the current tmle/ate ecosystem. His
   involvement elevates this above a typical
   Netflix-industry-agent paper.

**Follow-ups.** Pull the arXiv PDF; check (a) which
sensitivity-analysis methods are automated (Rosenbaum bounds?
E-value? Manski bounds?), (b) how the human-in-the-loop UX is
structured (checkpoint prompts? Assumption-approval gates?),
(c) whether the internal Netflix case studies are described in
enough detail to adapt to a healthcare context, (d) the
open-source GitHub link and license, (e) whether the codebase
has any biobank-EHR-friendly adapters or is A/B-test-first.

---

### 4. Cross-ancestry pleiotropic analysis of imaging-derived phenotypes enhances risk stratification of depression

**Authors.** Y Feng, X Guo, P Huang, N Jia, S Hu, S Yang.
**Venue.** *Molecular Psychiatry*, 2026.
**Signal source.** Google Scholar author-feed for **Joshua C.
Denny** — new related research (2026-07-27 14:34Z).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (cross-/trans-ancestry
portability); biobanks with EHR linkage (UKB imaging-derived
phenotypes); PheWAS/PheRS (depression PGS + IDP-PGS composite
risk).

**What the paper does (from title).** Cross-ancestry pleiotropic
analysis leveraging imaging-derived phenotypes (IDPs — likely
UKB brain-MRI IDPs) to improve polygenic risk stratification
for depression. The setup is: (a) discover pleiotropic
loci shared between IDPs and depression across ancestries,
(b) use the pleiotropy-informed instrument to build an
improved depression risk score, (c) show that the improved
risk score enhances stratification vs. a single-ancestry
single-trait PGS baseline.

**Why it matters for your work.**
1. **Cross-ancestry + IDP + pleiotropy triangle.** This is the
   natural next-generation refinement of PGS design — instead
   of one summary-stat source, one ancestry, one trait, use
   the pleiotropic-shared signal across ancestries and
   correlated traits to boost portability and stratification
   power. Directly on the trans-ancestry-portability
   sub-thread and pairs with the Jo et al. East Asian
   127-trait meta-analysis paper from the 07-23 report.
2. **UKB imaging is the frontier for biobank pleiotropy work.**
   The UKB imaging cohort (~100k+ MRIs) supplies the IDPs
   that make pleiotropic PGS design possible. This paper
   likely serves as a template for imaging-PGS-enhanced
   stratification for other neuropsychiatric traits (bipolar,
   schizophrenia, ADHD, Alzheimer's), which is a natural
   extension direction.
3. **Depression is a good AoU-replication target.** AoU has
   depression phecodes and (increasingly) imaging data at
   the AoU Imaging Study level — a natural downstream
   analysis would be to replicate the enhanced depression
   PGS in AoU with EHR-derived depression phecodes as
   outcome.

**Follow-ups.** Pull the paper; check (a) which IDPs (grey matter?
white matter tract? functional connectivity?), (b) which ancestry
strata were used for discovery vs. validation, (c) improvement
in AUC / calibration over single-ancestry baseline, (d) whether
they release the enhanced PGS weights.

---

### 5. Towards Optimal Estimators for Randomized Control Trials

**Authors.** H Parikh, G Levin-Konigsberg, N Tripuraneni, D Madeka,
MI Jordan, D Foster, D Perrault-Joncas, A Volfovsky.
**Venue.** arXiv preprint 2607.23254, submitted 2026-07-25
(primary category stat.AP).
**Signal source.** `arxiv-digest` 2026-07-28 — keyword hit
"causal inference", score 1.
**Bucket.** HIGH (methods-heavy).
**Threads served.** Causal inference (RCT estimator selection);
ML for precision health (estimator selection under
heterogeneous / heavy-tailed outcomes).

**What the paper does (from abstract).** Standard
difference-in-means is unbiased but often imprecise, and no
single covariate-adjustment method dominates across datasets.
Instead of picking "the best estimator for this RCT" (which
risks convenient selection), the paper proposes a
sample-splitting framework that estimates the *distribution*
of evaluation metrics (MSE, regret) across a *family* of RCTs
and thereby identifies the optimal estimator for a specific
analytical goal. Applied to Amazon SCOT (Supply Chain
Optimization Technology) trials and the Strengthening
Democracy Challenge (25 interventions). Result: weighted
least squares best for inference goals, difference-in-means
best for decision-regret minimization.

**Why it matters for your work.**
1. **Estimator-selection framework is portable to biobank
   RCTs.** AoU-embedded pragmatic trials, UKB-linked trials,
   and healthcare-system RCTs are typically analyzed with a
   single-default estimator; this framework justifies a
   principled choice across estimator families and could be
   cited in an SAP where estimator choice is otherwise
   arbitrary.
2. **Sample-splitting to estimate MSE distribution is the
   novel move.** The clever bit is treating an
   "estimator-family calibration" problem as itself an
   estimation problem, which requires many RCTs — natural
   fit for a healthcare RCT program that runs dozens of
   trials of similar design (e.g. behavioral-nudge trials
   in MyChart, adherence-nudge trials in pharmacy).
3. **Author panel is heavyweight.** Michael Jordan + Dean
   Foster + Alexander Volfovsky is an unusual concentration
   of causal-inference and statistics-theory authority —
   worth reading even if the immediate application seems
   distant.

**Follow-ups.** Pull the arXiv PDF; check (a) whether the
framework assumes access to trial-level metadata or just
outcome data, (b) how many RCTs are needed to stabilize the
estimator-selection procedure, (c) whether it handles
non-compliance or trial heterogeneity, (d) whether they
release code.

---

### 6. Potential preventive role of low-dose methotrexate against incident recorded psychosis: a retrospective cohort study based on electronic health records

**Authors.** F Corsi-Zuelli, M Taquet, B Deakin, R et al.
**Venue.** journal not fully captured in snippet (likely a
British psychiatric-epi outlet — Taquet is at Oxford
Psychiatry, Deakin is at Manchester).
**Signal source.** Google Scholar keyword feed "electronic
health records" — new results (2026-07-26 11:32Z).
**Bucket.** HIGH.
**Threads served.** EHR phenotyping (psychosis as an
EHR-recorded outcome); causal inference / pharmacoepi (drug
exposure → psychiatric outcome design); drug repurposing
(methotrexate as an anti-inflammatory repurposing candidate).

**What the paper does (from title + snippet).** Retrospective
cohort study using EHR data (likely TriNetX or a UK EHR
extract) testing whether low-dose methotrexate exposure — as
prescribed for rheumatologic indications — reduces incident
psychosis risk. Taquet on the author list is the key link to
the TriNetX / OxCGRT EHR-drug-repurposing lineage that
previously produced high-profile analyses on COVID-19
sequelae, hormonal contraception + psychiatric outcomes, and
GLP-1 + suicidality.

**Why it matters for your work.**
1. **Methotrexate is a strong anti-inflammatory drug-repurposing
   candidate.** Chronic low-dose methotrexate is the workhorse
   DMARD for rheumatoid arthritis and has been proposed for
   cardiovascular disease (CIRT trial), psoriasis-comorbidities,
   and now psychosis prevention (rationale: inflammation-based
   psychiatric-disorder hypothesis). Directly on the
   drug-repurposing thread and the pharmacoepi thread.
2. **Taquet-lineage methodology.** Taquet's EHR-repurposing
   papers have a distinctive design template (large TriNetX
   cohort, propensity-matched active-comparator design,
   subgroup-heavy Kaplan-Meier reporting). Worth reading for
   the design choices even if the specific finding is not on
   your CFTR / APOL1 / hereditary-cancer priority set.
3. **Psychiatric-outcome definitions from EHR are notoriously
   tricky.** How they defined "incident recorded psychosis"
   (F20-F29? First-hospitalization? Antipsychotic
   prescription?) is a methodologically portable question for
   any psychiatric-outcome EHR analysis in AoU.

**Follow-ups.** Pull the paper (search by title in Scholar);
check (a) EHR source (TriNetX? OpenSAFELY? UK primary-care?),
(b) active comparator (biologic DMARD? another
csDMARD? untreated inflammatory-arthritis controls?), (c)
psychosis outcome definition, (d) sensitivity analyses for
protopathic bias and immortal time.

---

### 7. PrimeKG-Plus: a literature-derived expansion of a multimodal precision medicine knowledge graph

**Authors.** TTD Nguyen, T Nguyen-Phuong, QH Nguyen et al.
**Venue.** bioRxiv, 2026.
**Signal source.** Google Scholar author-feeds for **Marinka
Zitnik** — new related research (2026-07-26 05:17Z) — **and**
**Tiffany J Callahan** — new related research (2026-07-26
05:17Z). Double-feed hit across the two canonical
KG-for-biomedicine name feeds.
**Bucket.** HIGH.
**Threads served.** Knowledge graphs & ontologies; drug
repurposing (PrimeKG is the reference multimodal KG for
drug-repurposing GNN methods); rare disease (PrimeKG covers
Orphanet phenotypes and Mendelian gene panels).

**What the paper does (from title + snippet).** Extends the
PrimeKG multimodal precision-medicine knowledge graph
(Chandak et al., Nat Sci Data 2023 — Zitnik lab) with a
*literature-derived* expansion — presumably automated
extraction of new entities and relations from PubMed via LLM
or PubMedBERT-style pipelines. Directly addresses the
"biomedical knowledge evolves rapidly, static KGs stale
quickly" problem.

**Why it matters for your work.**
1. **PrimeKG is the current reference KG for drug repurposing
   with GNNs.** Any paper extending PrimeKG is an
   infrastructure-tier read for the drug-repurposing thread.
   Directly parallels TxGNN (Huang et al., Nat Med 2024, Zitnik
   lab) which used PrimeKG for zero-shot drug-disease
   prediction.
2. **Literature-derived expansion methodology is portable.**
   The pipeline they use (LLM extraction? PubMedBERT + RE
   heads? Manual curation?) is a portable design pattern for
   maintaining an HPO-based rare-disease KG or an
   OMOP-concept-extended clinical KG.
3. **Callahan-cofire signals dual utility.** Tiffany Callahan
   is one of the leading voices on biomedical-KG
   infrastructure (PheKnowLator, OpenBioLink), so a paper
   surfacing on both her related-research feed and Zitnik's is
   likely to be picked up by both the KG-methods and
   clinical-KG-application communities.

**Follow-ups.** Pull the bioRxiv preprint; check (a) the
literature-extraction pipeline architecture, (b) node and
edge type additions vs. PrimeKG baseline, (c) whether they
benchmark on drug-disease link prediction against PrimeKG,
(d) whether they release the expanded KG or just the
extraction code.

---

### 8. DPCGS: a computational framework for linking GWAS to single-cell transcriptomics in complex traits and diseases

**Authors.** C Liu, B Shen, J Li, R Zhu, P Yang, B Wu, Y Xuan et al.
**Venue.** bioRxiv, 2026.
**Signal source.** Google Scholar author-feed for **Jian Yang**
— new related research (2026-07-26 05:17Z).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (TWAS-adjacent
GWAS-to-cell-type attribution); precision medicine
(cell-type-of-action inference for complex traits).

**What the paper does (from title).** Computational framework
for attributing GWAS signal to specific cell types via
integration with single-cell RNA-seq expression data. The
reference class here is sc-DRS (Zhang et al., Nat Genet 2022,
Price lab), scGWAS, MAGMA-derived per-cell-type enrichment,
and the more recent sc-linker / PAGWAS-style methods. Yang
lab authorship (Westlake / Queensland) places this in the
GCTA / SBayesRC / SBayesS methods lineage.

**Why it matters for your work.**
1. **Cell-type-of-action attribution is a persistent gap
   in trans-ancestry PRS work.** Understanding *which*
   cell type mediates a GWAS locus's effect is important
   for both mechanistic interpretation and for improving
   PRS transferability by re-weighting on tissue-relevant
   loci.
2. **Yang lab methods lineage.** Yang's group produced
   GCTA / SBayesRC / SBayesR — reference tools your PRS
   work already builds on. A new framework from this
   group is worth benchmarking against sc-DRS before
   adopting.
3. **Portable to CFTR / APOL1 / hereditary-cancer
   cell-type-of-action.** Cell-type attribution for
   monogenic-modifier PGS (e.g. which cell types drive the
   modifier signal for CFTR-lung-function or APOL1-kidney
   penetrance PGS) is a natural application.

**Follow-ups.** Pull the bioRxiv preprint; check (a) benchmark
against sc-DRS, (b) whether it accepts SBayesRC-derived
posterior effect sizes as input, (c) which single-cell atlases
are supported (Tabula Sapiens? CELLxGENE?), (d) code
availability.

---

### 9. Cancer outcomes and biological mechanisms among patients with type 2 diabetes mellitus using glucagon-like peptide-1 receptor agonists: a systematic review and meta-analysis

**Authors.** ED Eze, L Ntakirutimana, SD et al.
**Venue.** systematic review; journal not fully captured in
snippet.
**Signal source.** Google Scholar author-feed for **George
Hripcsak** — new citations (2026-07-27 14:34Z).
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi (GLP-1
outcomes); drug repurposing (GLP-1 for oncology outcomes);
ML for precision health (indirect — treatment-heterogeneity
signal in GLP-1 cancer-outcome studies).

**What the paper does (from title).** Systematic review and
meta-analysis of cancer outcomes and biological mechanisms
in T2DM patients using GLP-1 receptor agonists — synthesizes
the observational and pharmacoepi literature on GLP-1
exposure → cancer risk / cancer outcome. Pairs conceptually
with the Tang et al. hair-loss TTE above (both are
GLP-1-outcome-focused papers).

**Why it matters for your work.**
1. **Reference-class synthesis for the GLP-1 pharmacoepi
   thread.** Two GLP-1-outcome papers landing in the same
   week (Tang BMJ TTE + Eze SR/MA) is a signal to update
   the internal reference class for GLP-1-outcome
   pharmacoepi.
2. **Cancer-outcome direction is important given
   hereditary-cancer-carrier populations.** BRCA1/2, Lynch,
   and other hereditary-cancer-carrier populations may
   have baseline elevated cancer risk that interacts with
   drug-class exposure — a GLP-1 cancer-outcome SR is a
   useful background reference before designing an
   HCS-carrier × GLP-1 pharmacoepi analysis.

**Follow-ups.** Pull the SR; check (a) included studies and
overlap with prior GLP-1 SR/MAs, (b) which cancer sites are
covered (breast? pancreatic? thyroid? all-site?), (c) whether
mechanistic sections cite specific pathway hypotheses.

---

### 10. Re-Purposing Sapropterin (Kuvan) for ACTA2-Related Multisystemic Smooth Muscle Dysfunction Syndrome: A Translational Mechanistic and First-In-Human Therapeutic Report

**Authors.** M Hausman-Kedem, N Bielopolski, V Krishnan, S Wald-
Altman, SI Shrian, O Bar-Yosef, L Kapusta, C Shamber, PL
Musolino, M Weil.
**Venue.** *Annals of Clinical and Translational Neurology*,
2026-07-26 (10.1002/acn3.70493).
**Signal source.** NCBI "What's new for 'drug repurposing' in
PubMed" (2026-07-27 13:21Z; PMID 42503698).
**Bucket.** MEDIUM-HIGH.
**Threads served.** Drug repurposing (rare-disease
angle); rare disease (ACTA2-related smooth muscle dysfunction
is ultra-rare vascular syndrome).

**What the paper does (from title).** Translational
mechanistic report + first-in-human therapeutic report for
sapropterin (BH4 — the drug approved for phenylketonuria)
repurposed for ACTA2-related multisystemic smooth muscle
dysfunction syndrome — an ultra-rare monogenic vascular
disease affecting cerebral and coronary vasculature.

**Why it matters for your work.**
1. **Rare-disease drug repurposing is exactly the
   HPO-phenotype-matched candidate-drug direction your
   drug-repurposing thread flags as high-priority.** The
   ACTA2-sapropterin pairing has a plausible mechanistic
   rationale (BH4 as eNOS cofactor in a smooth-muscle
   dysfunction context).
2. **First-in-human data is rare for
   ultra-rare-disease repurposing.** Most rare-disease
   repurposing papers are pipeline-level (KG signal,
   mechanistic-model prediction). A first-in-human
   therapeutic report is the endpoint of the pipeline —
   worth reading as a template for what the drug-repurposing
   thread eventually converts into.

**Follow-ups.** Pull the paper; check (a) the mechanistic
rationale (BH4 / eNOS / NO signaling in ACTA2-mutant smooth
muscle), (b) the first-in-human protocol (N? outcomes?
adverse events?), (c) whether they cite a KG or
mechanistic-model prediction that identified sapropterin.

---

## METHODS-WATCH (short entries)

### `arxiv-digest` 2026-07-24 — Auditing pretraining contamination in single-cell foundation model benchmarks
**Authors.** Sarwan Ali (q-bio.GN).
**Signal.** `arxiv-digest` 2026-07-24, keyword `foundation model`,
score 1.
**Take.** Introduces `scContam` — MinHash-based gene-set
fingerprinting + membership inference attack (MIA-scFM) to
audit whether zero-shot benchmark performance for single-cell
foundation models (Geneformer, scGPT, UCE) reflects
pretraining exposure. Finds 80.4% (PBMC 3k) and 77.0%
(CELLxGENE pancreatic islet atlas) of benchmark cells have
pretraining-overlap evidence, vs. 0% for post-cutoff datasets
(AIDA v2, Tahoe-100M). The controlled re-pretraining
experiment (MIA AUROC 0.494 → 0.881 as overfitting worsens)
is clean. **METHODS-WATCH** — the audit framework is directly
portable to EHR foundation models (CLMBR, MOTOR, MEDS,
EHRSHOT) where MIMIC-III / eICU / N3C overlap between
pretraining corpora and benchmark tasks is a live concern.

### `arxiv-digest` 2026-07-28 — SCTA: An Agentic Framework for Stable and Interpretable Target Gene Discovery from Single-Cell RNA Sequencing
**Authors.** S Chen, C Zhu, Y Zhang, Y Li, Q Xie, H Wang (cs.LG).
**Signal.** `arxiv-digest` 2026-07-28, keyword `precision
medicine`, score 1.
**Take.** Decomposes single-cell target-gene discovery into
specialized agents aligned with key pipeline decision points
(preprocessing, cell-population selection, DE analysis,
biological interpretation). Ablation on hereditary chronic
pancreatitis. Off-thread for single-cell target discovery
specifically but the "decision-centric agent decomposition"
template is portable to any multi-step biomedical analysis
pipeline — e.g. PheWAS, TWAS, or drug-repurposing pipelines.
**METHODS-WATCH.**

### `arxiv-digest` 2026-07-28 — TCellAlign: Cross-study T-cell Populations Alignment with Nomenclature-Guided Multi-Agent Workflow
**Authors.** P Xie, R Zhou, Z Ou, J Zhang, X Zhou, X Sun, J Lu,
W Ma (q-bio.QM).
**Signal.** `arxiv-digest` 2026-07-28, keyword `foundation
model`, score 1.
**Take.** Multi-agent framework for aligning T-cell population
labels across studies using literature retrieval + information
extraction + Cell Ontology + evidence adjudication. Off-thread
for T-cell nomenclature per se, but the
literature-retrieval + evidence-grounded-adjudication design
pattern is portable to HPO term standardization across
studies. **METHODS-WATCH.**

### Feng et al. UKB / CANCEL — likely dietary + cardiometabolic (07-27 UKB NCBI)
**Authors.** C Zeng, H Lyu, L Lou, X Lu, M Lei (*Food Sci Nutr*
2026-07-26). **Take.** Composite Dietary Antioxidant Index →
asthma-COPD overlap in UKB. Namesake collision with Chenjie
Zeng — worth flagging that this Zeng is unrelated (Chinese
dietary-epi group). Off-thread but a routine reference for
UKB dietary-index → composite-respiratory-outcome designs.
**METHODS-WATCH.**

### Chong et al. — Metformin ulcerative colitis systematic review (07-27 drug repurposing NCBI)
**Authors.** J Chong, H Ding, J Ma, C Gong, J Xu, J Pan (*Naunyn
Schmiedebergs Arch Pharmacol* 2026-07-27). **Take.** Preclinical
+ limited clinical evidence for metformin in ulcerative
colitis. Pairs with the Saxby metformin-AAA MR paper from the
07-23 report as further evidence that metformin repurposing is
being systematically explored across indications. **METHODS-WATCH.**

### Barua et al. — Accelerometry activity/sleep patterns in AoU for inflammatory arthritis (07-26 AoU NCBI)
**Authors.** S Barua, A Kulkarni, D Upadhyay, S Hariharan, I
Ashman, K Chen, A Tsirigos, JU Scher, RH Haberman (*ACR Open
Rheumatol* 2026). **Take.** AoU accelerometry Fitbit data + EHR
outcomes for inflammatory arthritis prediction. Off-thread for
inflammatory arthritis specifically, but a useful
methods-only reference for AoU wearable + EHR outcome
prediction designs — directly applicable to CFTR / APOL1 /
CHIP wearable-signal work in AoU. **METHODS-WATCH.**

### Tao et al. — Operation-Mechanism Alignment for Clinical Reasoning over EHR (BioNLP 2026)
**Authors.** G Tao, S Wang, Y Xue, A Tanwar, Y Ji, K Sun, M Mok
et al. **Signal.** Hripcsak Scholar related-research feed
(2026-07-27). **Take.** Framework for aligning LLM operations
with the underlying clinical-reasoning mechanism when
answering questions over EHR. BioNLP 2026 workshop-tier but
methodologically on-thread for EHR-LLM interpretability.
**METHODS-WATCH.**

### García et al. — Rare disease variant curation and classification review
**Authors.** JB García, M García, LE Olivera, CIR Pedroza et al.
(*Archives of Medical Research* 2026). **Signal.** Karczewski
Scholar citations feed (2026-07-27) + "variant interpretation"
keyword feed (2026-07-26). **Take.** Review of ACMG/AMP
variant-curation tools and emerging methods for single-
nucleotide variant analysis in rare-disease genomics. Not novel
but a useful survey-class reference for the ACMG/ClinGen
thread. **METHODS-WATCH.**

### Xia et al. — Functional analysis and classification of six RYR1 variants in Japanese malignant hyperthermia
**Authors.** G Xia, S Otsuki, K Mukaida, M Xu, K Kido, A Sumii et
al. (*British Journal of Anaesthesia* 2026). **Signal.**
Bastarache Scholar related-research feed (2026-07-27). **Take.**
Functional characterization of six RYR1 variants in a Japanese
MH cohort, with ACMG/AMP classification. Off-thread specifically
for MH but a compact example of variant-functional-evidence-plus-
ACMG-classification design applicable to any actionable-gene
VUS resolution project. **METHODS-WATCH.**

### HPRC2 pangenome (three Scholar feeds simultaneously)
**Authors.** JK Lucas, P Hebbar, WW Liao, JF Macias-Velasco et al.
(bioRxiv 2026). **Signal.** Denny, Yang, Montgomery citation feeds
(2026-07-27; three-way simultaneous hit). **Take.** Second
release of the Human Pangenome Reference Consortium pangenome
with near-complete coverage of common genetic variation.
Infrastructure-tier update; not novel methodology but the
reference genome your downstream work implicitly depends on is
shifting from a linear-plus-alt-contigs paradigm to a graph
pangenome — worth noting when planning any WGS-based analysis
that expects a stable reference over the next 2–3 years.
**METHODS-WATCH (infrastructure).**

---

## Off-thread / SKIP (representative entries — not exhaustive)

- Wong et al. — Long-term physical activity patterns and kidney
  stone risk (Fitbit + AoU cohort survival analysis, J Endourol
  2026-07-26; NCBI AoU 07-27) — pure activity-outcome epi in AoU,
  off-thread.
- Fernandes et al. — McConnell's Sign in RV Infarct case report —
  off-thread (case report, incidental AoU keyword match).
- Wang et al. — MetS + component burden × gastric cancer risk in
  UKB (Cancer Research Communications 2026-07-26; NCBI UKB feed
  07-26) — routine UKB × cancer risk paper.
- He et al. — Microbiota-modulating dietary strategies for
  gallstone prevention in 2 UKB-adjacent cohorts (Turk J
  Gastroenterol 2026-07-26; NCBI UKB 07-27) — dietary epi.
- Zeng et al. — Composite Dietary Antioxidant Index and
  asthma-COPD overlap in UKB (Food Sci Nutr 2026-07-26; NCBI UKB
  07-27) — dietary epi (note namesake, unrelated author).
- Ye et al. — Chinese esophageal cancer smoking-attributable
  burden 1990–2021 (Zhonghua Yu Fang Yi Xue 2026-07-06; NCBI UKB
  07-27) — Chinese disease-burden analysis.
- Wei et al. — Low-data-burden vascular-behavioral profile for
  cognitive decline (Am J Prev Med 2026-07-26; NCBI UKB 07-27) —
  aging cognitive-decline prediction, off-thread.
- Li et al. — Repurposing Camellia sinensis Roots and Ginkgo
  biloba Leaves for Multiple Myeloma (Chem Biodivers 2026-07;
  NCBI drug-repurposing 07-27) — traditional-herbal repurposing.
- Babu et al. — Transcriptomic profiling of amygdala in autism
  (Autism Res 2026-07-26; NCBI drug-repurposing 07-27) —
  incidental keyword match, off-thread.
- van der Velden et al. — PSMA imaging in metastatic
  castration-sensitive prostate cancer (Eur J Nucl Med 2026;
  Chenjie Zeng Scholar related feed 07-27) — imaging-oncology,
  off-thread.
- Ma et al. — LncRNA RP11-708J19.2 in colorectal cancer
  progression (Eur J Histochem 2026; Chenjie Zeng Scholar
  citations 07-27) — cancer molecular biology, off-thread.
- Multiple animal-genomics feeds (pig scRNA eQTL, various
  chromatin structure atlases) triggered on shared reference
  infrastructure.

---

*Prepared 2026-07-28; next report expected once new signal
accumulates (typically 1–2 days). Full arxiv-digest for today is at
`digests/2026-07-28.md` (3 papers: TCellAlign, SCTA target
discovery, Parikh RCT estimators).*
