# Research digest report — 2026-07-30

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-23 13:00Z → 2026-07-30 12:35Z** (~7 days since the
last committed report at `reports/2026-07-23-research-digest.md`,
which closed with morning-of-07-23 alerts). This is a **multi-day
catch-up** — expect a longer HIGH list than the daily follow-on
reports.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-07-24.md` → `2026-07-30.md`) | 07-24 → 07-30 (10:30Z crons) | 7 daily runs. 5 non-empty (24, 27, 28, 29, 30); 25 and 26 empty. 8 papers surfaced total (2 previously-seen suppressed). Two are HIGH (oci-agent 07-27; GraphRareBench 07-29); two METHODS-WATCH (Parikh/Volfovsky optimal-RCT-estimators 07-28; Neubrander/Volfovsky confounder-trap text-causal 07-30); rest score-1 off-thread. |
| Google Scholar alerts (author-feed cluster) | 07-26 → 07-29 | Multi-day cluster spanning Denny (related + citations), Bastarache (related), Karczewski (citations + related), Zitnik (related), Ryan (related), Hripcsak (citations), Hernán (citations), Szolovits (citations + related), Zhiyong Lu (new articles), Chenjie Zeng (self-citations + related), plus off-thread author feeds (Ma, Yang, Snyder, Ren, Chung, Kastner, Langenberg, Pritchard, Montgomery, Callahan, Brandt). |
| Google Scholar alerts (keyword feeds) | 07-26 15:32Z batch | 12 keyword feeds fired together — `phenome wide association studies`, `UK Biobank`, `All of Us research program`, `drug repurposing`, `electronic health records`, `variant interpretation`, `knowledge graph`, `foundation models & EHR`, `mendelian diseases`, `rare diseases`, `APOL1`, `autoimmune diseases`, plus penetrance-paper citations feed. |
| NCBI "My NCBI What's New" — AoU / UKB / drug repurposing | 07-23, 07-24, 07-25, 07-26, 07-27, 07-28, 07-29 | Six daily batches per topic. AoU volumes small (2–9/day); UKB heavier (10–26/day); drug repurposing largest (10–13/day). On-thread hits sparse — the highest-value AoU hit is Hwang et al. GLP-1 real-world weight loss (07-29). |
| bioRxiv / medRxiv Subject Collection Alerts | daily | Aggregate feeds — individual papers surfaced upstream via Scholar / NCBI. Not a separate net. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it.

---

## Executive summary (HIGH-priority studies, ranked)

Fifteen HIGH items surfaced this week, clustering into four dense knots:

**GLP-1 pharmacoepidemiology (3 items).** Tang et al. BMJ (Hernán & Ryan
feeds) — first target-trial-emulation of hair loss under GLP-1 RAs in
T2D. Eze et al. (Hripcsak feed) — systematic review of cancer outcomes
+ biological mechanisms under GLP-1 RAs. Hwang et al. Drug Des Devel
Ther (AoU NCBI) — first head-to-head real-world weight-loss comparison
across GLP-1 RAs in **All of Us**. Together these cover safety-signal
mining (hair loss), oncology safety (cancer), and comparative
effectiveness (weight loss) — the three highest-value angles for the
GLP-1 pharmacoepi thread.

**Rare-disease / phenotype-driven diagnosis (4 items).** GraphRareBench
arXiv (07-29) — HPO-query benchmark with graph-defined hard confounders
+ evidence-audited agent evaluation. Song et al. JMIR — LLM initial-
visit specialty triage in rare diseases. Ekici et al. — Mendelian
kidney disease diagnostic yield in a real clinical cohort. García et al.
Archives of Medical Research — variant curation & classification
standards review with a rare-disease focus. These lock onto the rare-
disease + HPO diagnosis + variant-interpretation intersection.

**EHR-phenotyping infrastructure + methods (3 items).** Wang et al.
arXiv (Ryan feed) — binary silver labels in EHR-based computable-
phenotyping algorithms. Lemieux et al. JAMIA Open — national EHR
interoperability for research (surfaced in the 07-23 report; upgraded
here after full-text availability confirmed). Corsi-Zuelli et al. —
low-dose methotrexate against incident psychosis in an EHR cohort (an
EHR-based drug-repurposing signal).

**Causal inference & PheWAS methods (5 items).** Chou et al. arXiv
(07-27) — oci-agent human-in-the-loop causal-inference workflow
(propensity trimming, sensitivity, HTE, DR learning). Żebrowska et al.
eBioMedicine — Circadian Imbalance Index GWAS + PheWAS + MR (the
multi-cohort triangulation template your PheWAS thread tracks). Feng
et al. Mol Psychiatry — cross-ancestry pleiotropic imaging-PGS +
depression risk stratification. Nguyen et al. bioRxiv — PrimeKG-Plus
literature-derived multimodal precision-medicine KG expansion (drug-
repurposing thread). Liu et al. Neurotherapeutics — deep-learning +
WGS drug-repurposing across 92 CNS conditions. Also Jin et al. Nature
Protocols — LLMs-for-medical-research tutorial (methods reference,
from the Zhiyong Lu feed).

Two adjacent studies flagged as METHODS-WATCH sit in the same causal
lane: Parikh/Volfovsky (Amazon/Meta/Anthropic bench; RCT estimator
selection) and Neubrander/Volfovsky (text-treatment "confounder trap"
via masking). Neither is directly on-thread but both are worth
tracking as design references.

---

## HIGH — full write-ups

### 1. Tang, Zhang, Lu, Zhang, Liu, Lu et al., *Risk of hair loss associated with glucagon-like peptide-1 receptor agonists in adults with type 2 diabetes: target trial emulation* — **BMJ 2026**

**Feeds:** Miguel Hernán "10 new citations to articles by …" (07-27
14:34Z); Patrick Ryan "new related research" (07-27 14:34Z). The double
citation-feed hit is the tell — this is being read as canonical
methods work on the target-trial-emulation side.

**Why HIGH.** Two of your active threads collide here:
1. **Drug-class thread (GLP-1 RAs)** — hair-loss reports have been
   accumulating on the informal / FAERS side since 2024, but the
   confounding structure (weight loss → telogen effluvium; T2D itself
   → alopecia risk) has kept the pharmacoepi literature cautious. A
   TTE done properly on a large database is the right design.
2. **Causal inference / pharmacoepi (target trial emulation)** — TTE
   applied to a *safety* signal (rather than the usual effectiveness
   question) is worth reading for the estimand construction: what does
   "would have started GLP-1 RA today" look like for a hair-loss
   outcome window, and how did they handle informative discontinuation?

**Actionable question for your GLP-1 thread.** BMJ tier + TTE framing
should establish the reference design. Note whether the paper uses
active comparator (e.g., DPP-4i or SGLT2i) — active-comparator TTE for
GLP-1 safety is where Hernán's group has been steering the field.

**Feed-metadata caveats.** Only title + venue + first ~2 lines
available; author list & sample size not extracted from the alert
snippet. Full-text pull recommended before any comparison to your own
AoU GLP-1 work.

---

### 2. Eze, Ntakirutimana, SD… et al., *Cancer outcomes and biological mechanisms among patients with type 2 diabetes mellitus using glucagon-like peptide-1 receptor agonists: a systematic review and …* — **2026**

**Feed:** George Hripcsak "10 new citations to articles by George
Hripcsak" (07-27 14:34Z).

**Why HIGH.** Sits at the intersection of two active threads:
- **GLP-1 drug-class pharmacoepi** — the cancer-safety-signal
  question (thyroid, pancreatic, and now solid tumors) is unsettled;
  a 2026 systematic review is a good synthesis checkpoint.
- **Chenjie's own cancer-epi background** — solid-tumor risk under
  GLP-1 RAs is one of the two GLP-1-adjacent questions worth
  triangulating if you spin up an AoU comparative-effectiveness /
  safety analysis (the other being weight-loss magnitude, see #3).

**Actionable question.** Read for the *inclusion criteria* and whether
they separate observational-vs-RCT evidence — the RCT signal (LEADER,
SUSTAIN-6) and observational signal have historically disagreed on
the pancreatic-cancer question. If the review triangulates them
properly, cite it as reference on your GLP-1 slide deck.

---

### 3. Hwang, Lee, Kim, *Real-World Comparative Weight Loss of GLP-1 Receptor Agonists in the All of Us Research Program: A Retrospective Cohort Study* — **Drug Des Devel Ther 2026;20:604247**

**Feed:** NCBI PubMed "What's new for 'All of Us' in PubMed" (07-29
15:07Z; PMID 42518911). Free PMC full text available.

**Why HIGH.** This is exactly the study your infrastructure is set up
for. First head-to-head real-world weight-loss comparison across GLP-1
RAs on the **All of Us cohort** — the platform you already have
tooling for (`aou-workbench-2`, `waxse` skills, PheTK / dsub pipelines
via the `tam` skill). Directly serves the GLP-1 drug-class thread and
the AoU-native pharmacoepi arm.

**Read priority: FIRST.** Read the methods for:
- Which GLP-1 RAs were compared (semaglutide vs. tirzepatide vs.
  liraglutide vs. dulaglutide — the head-to-head structure is what
  the RCT literature notably lacks outside of SURMOUNT / STEP).
- Weight ascertainment approach (EHR-recorded weights are irregular
  in AoU; how did they handle the missing-visit pattern?).
- Adjustment for BMI at index, baseline HbA1c, prior anti-obesity
  medication use.
- Whether they used any of the AoU-native EHR-code phenotypes you
  might want to reuse.
- Sample size — real-world head-to-head across GLP-1 RAs in AoU is
  power-limited by tirzepatide's late arrival (2022 approval), so the
  sample-size disclosure will tell you what's currently feasible.

**Actionable follow-on.** This is a direct template if you're planning
an AoU-based GLP-1 outcome study (weight, HbA1c, cancer, cardiovascular
events, or renal). At minimum, cite as prior work.

---

### 4. Żebrowska, Wielscher, Zhang et al., *Genetic architecture of a Circadian Imbalance Index: genome-wide association, phenome-wide association, and Mendelian randomisation analyses* — **eBioMedicine 2026**

**Feed:** Google Scholar "Lisa Bastarache — new related research"
(07-26 05:17Z). Was flagged in the 07-23 report from the NCBI AoU
batch; this Bastarache-related-research alert is the second surfacing
and confirms the venue.

**Why HIGH.** The full GWAS → PheWAS → MR triangulation on a single
constructed composite phenotype ("Circadian Imbalance Index") — this
is the exact three-legged design that anchors your PheWAS-infrastructure
thread. Read for:
- **How the composite is constructed** (which sleep / activity /
  chronotype variables enter; how are they weighted; is it PCA,
  factor score, or a clinically-grounded index?). Composite-phenotype
  construction is a live methodological question — the alternative to
  composites is multi-trait GWAS + follow-up, and each has different
  power / interpretation tradeoffs.
- **PheWAS in what platform** (UKB + which biobank on the MR leg?
  the eBioMedicine venue suggests a multi-cohort UK-anchored design).
- **MR design** — one-sample, two-sample, multivariable MR? The
  exposure-outcome direction they run tells you the intended causal
  claim.

**Actionable follow-on.** File as a design reference for any composite-
phenotype PheWAS/MR pipeline you might want to build on AoU or BioVU.
Denny + Bastarache both surface it in the past week, which is a
consensus signal.

---

### 5. Feng, Guo, Huang, Jia, Hu, Yang, *Cross-ancestry pleiotropic analysis of imaging-derived phenotypes enhances risk stratification of depression* — **Molecular Psychiatry 2026**

**Feed:** Google Scholar "Joshua C. Denny — new related research"
(07-27 14:34Z).

**Why HIGH.** Two threads served:
- **Genetic epi (cross-ancestry PRS)** — imaging-derived-phenotype
  (IDP) PGS applied cross-ancestry is where the neuroimaging genetics
  field is trying to move; the portability question there is the same
  one you track on the PRS side.
- **ML for precision health (individualized risk prediction)** —
  the *risk stratification enhancement* framing (rather than average-
  effect estimation) is the higher-priority version of PRS work for
  clinical translation.

**Actionable follow-on.** Read for:
- **Pleiotropic method** (are they using MTAG, PLEIO, or a bespoke
  cross-trait PGS combination?)
- **Which IDPs** enter the PGS composite (structural MRI volumes,
  DTI, resting-state fMRI features?)
- **Ancestry coverage** — which non-European cohorts, and does the
  cross-ancestry gain persist or degrade under the standard
  Bhattacharya / Ge cross-ancestry portability caveats?

**Where it links to your work.** If you're planning any cross-ancestry
PRS + EHR-phenotype work on AoU, this is a template for the
"structured predictor + downstream stratification" framing.

---

### 6. Wang, Slaughter, Nelson, Williamson, *Using binary silver labels in electronic health records-based computable phenotyping algorithms* — **arXiv:2607.18431 (2026-07-24)**

**Feed:** Google Scholar "Patrick Ryan — new related research" (07-26
05:17Z).

**Why HIGH.** Computable phenotyping is a core thread. "Silver
labels" (algorithmically-derived proxy labels used when true labels
are scarce) is a very live topic — the PheValuator lineage and the
KOMAP lineage both traffic in silver-label constructs. A formalization
of how to *use* binary silver labels (as opposed to how to *estimate*
them, which is what PheValuator does) is exactly the kind of
methods-infrastructure paper that changes downstream downstream
phenotyping practice.

**Actionable follow-on.** Read for:
- **Which estimator family** (do they extend PheValuator's
  PPV/sensitivity framing, or come at it from a
  measurement-error / label-noise angle like Menon / Lauritzen?)
- **Guarantees under label-shift** (silver labels drift when the
  underlying algorithm is updated — do they address this?)
- **Whether they handle time-varying labels** (repeated
  measurements, not just cross-sectional case/control).

**Where it links to your work.** If you're building any EHR-based
computable phenotype for AoU or BioVU, this paper is the current
methods baseline to cite. Also serves the `ehr-phenotyping-os` skill
as a candidate addition.

---

### 7. Nguyen, Nguyen-Phuong, Nguyen et al., *PrimeKG-Plus: a literature-derived expansion of a multimodal precision medicine knowledge graph* — **bioRxiv 2026**

**Feed:** Google Scholar "Marinka Zitnik — new related research"
(07-26 05:17Z).

**Why HIGH.** Directly on the drug-repurposing thread. PrimeKG
(Zitnik lab) is the current reference multimodal precision-medicine
KG; a literature-derived expansion (adding edges + entities extracted
from PubMed text) is the natural next iteration and pushes it toward
the *explainable-hypothesis-output* angle the interests file
prioritizes (paths / subgraph rationales rather than opaque link
prediction).

**Actionable follow-on.** Read for:
- **Extraction pipeline** (rule-based, LLM-based, or hybrid;
  precision/recall of edge extraction, and whether they hold out a
  gold-standard set).
- **New coverage** — which entities / relations are added over the
  base PrimeKG? Is HPO or clinical-note-derived phenotypes
  represented, since that connects to your rare-disease HPO
  phenotyping angle?
- **Downstream evaluation** — repurposing predictions on a held-out
  set? Comparison to PrimeKG-base?

**Where it links to your work.** File as a design reference for
KG-based drug-repurposing work with an EHR-evidence loop (which is
the version of drug-repurposing you're explicitly interested in per
INTERESTS.md).

---

### 8. Corsi-Zuelli, Taquet, Deakin, R…, *Potential preventive role of low-dose methotrexate against incident recorded psychosis: a retrospective cohort study based on electronic health records* — **2026**

**Feed:** Google Scholar `"electronic health records"` keyword feed
(07-26 11:32Z).

**Why HIGH.** Two threads:
- **EHR-based drug repurposing** — this is exactly the "EHR-based
  repurposing signals mined from real-world prescribing and outcomes"
  angle called out in INTERESTS.md, applied to a *neurology/psychiatry*
  question via an *immunosuppressive* medication.
- **Causal inference / pharmacoepi** — Taquet is a well-known
  TriNetX-based EHR-repurposing analyst (Oxford/OpenSAFELY-adjacent);
  his methods are usually solid and interpretable.

**Actionable follow-on.** Read for:
- **Data source** (TriNetX or a national EHR network?)
- **Active comparator + new-user design** — MTX for RA is the natural
  comparator group; did they use it, or a non-user comparator? A non-
  user comparator is a weakness that would put it in the METHODS-
  WATCH bucket instead.
- **How they defined "incident recorded psychosis"** — this is
  exactly the phecode-based outcome definition question you care
  about, and the answer determines how credible the safety signal is.

**Where it links to your work.** Reference example for EHR-based
drug-repurposing pipelines that hit the causal-inference bar. Could
serve as a template for a comparable Chenjie-lineage question (an
underused drug × an EHR-derived outcome, with an active comparator
and TTE framing).

---

### 9. Song, Xu, Xiao, Bi, Zhang, Zheng, Li…, *Initial-Visit Specialty Triage in Rare Diseases Using Large Language Models: Retrospective Benchmarking Study* — **Journal of Medical Internet Research 2026**

**Feed:** Google Scholar `rare diseases` keyword feed (07-26 11:32Z).

**Why HIGH.** Rare-disease diagnosis is an active thread, and LLM-
based specialty triage from initial-visit information is the version
of the rare-disease diagnostic-odyssey problem that has direct
clinical translation potential. Complements the GraphRareBench arXiv
paper (#13 below) which benchmarks HPO-driven diagnosis specifically.

**Actionable follow-on.** Read for:
- **Ground-truth construction** — how did they define the "correct"
  specialty for each rare-disease case?
- **LLM comparison** — which models, and are they zero-shot,
  fine-tuned, or RAG-augmented on rare-disease-specific corpora?
- **Comparison to clinician triage** — the meaningful comparison is
  not just LLM-vs-random but LLM-vs-generalist-clinician.

**Where it links to your work.** Reference for the rare-disease-LLM
methods thread. Also useful context for the `wglab` / Phen2Gene /
Phenolyzer skill space you already reference.

---

### 10. Ekici, Knaup, Schaeffer, Schneider et al., *Diagnosing Mendelian Kidney Disease: Hidden Niches in the (Kidney) Genome* — **American Journal of Kidney Diseases 2026** (feed reports venue as "*Journal of Kidney Diseases*")

**Feed:** Google Scholar `mendelian diseases` keyword feed (07-26
11:32Z).

**Why HIGH.** Serves two threads:
- **Rare disease diagnosis** — Mendelian kidney disease diagnostic
  yield in real clinical cohorts is the same class of question as
  your APOL1 thread.
- **APOL1** — the paper is unlikely to be an APOL1-focused study
  (APOL1 kidney risk is polygenic + moderate-penetrance, not
  Mendelian), but Mendelian-kidney-disease diagnostic yield is
  context for interpreting APOL1's contribution to end-stage kidney
  disease in the general population.

**Actionable follow-on.** Read for:
- **Gene panel** used and diagnostic yield.
- **Clinical presentation vs. genotype** — what's the correlation
  structure; how many patients had a "hidden" (i.e., unrecognized)
  monogenic diagnosis?
- **Whether they discuss the phenocopy / oligogenic / modifier
  question**, which is where APOL1 sits.

**Where it links to your work.** Reference for the APOL1 vs.
Mendelian-kidney-disease dichotomy in your active APOL1 thread.

---

### 11. Liu, Qu, Mentch, Chang, Kim, Qiu, Ostberg, Nguyen, Glessner, Hakonarson, *Drug repurposing opportunities across 92 CNS-related conditions using deep learning and whole-genome sequencing* — **Neurotherapeutics 2026;23(5):e00976** (PMID 42520674)

**Feed:** NCBI PubMed "What's new for 'drug repurposing' in PubMed"
(07-29 15:07Z).

**Why HIGH.** Directly on the drug-repurposing thread, and combines
two of the sub-angles INTERESTS.md flags as high-priority:
- **KG-adjacent** — 92 conditions across a shared genetic-signal
  substrate is essentially a matrix-completion / KG-embedding
  framing.
- **Genomic-anchored** — using WGS to define the disease-side of the
  drug-target-disease matrix reduces the reliance on curated
  disease-gene edges, which are known to be biased toward
  well-studied disease areas.

**Actionable follow-on.** Read for:
- **Which DL model** — GNN over a disease-gene-drug graph? A
  matrix-factorization variant? A masked-language-model over
  variant-drug sequences?
- **Cohort** — is this CAG (Children's Hospital of Philadelphia), which
  Hakonarson leads, or an aggregated multi-cohort WGS set? CAG
  ancestry composition is worth knowing since CNS-drug repurposing
  candidates should ideally validate across ancestry.
- **Repurposing evaluation** — are they using a hold-out drug-disease
  edge set (standard evaluation) or an EHR / prescription-based
  validation loop (the higher-priority evidence-loop angle from
  INTERESTS.md)?

**Where it links to your work.** File as design reference for
DL+genomics drug-repurposing. Compare to PrimeKG-Plus (#7) for
KG-vs-embedding-first design tradeoffs.

---

### 12. Chou, Alexandre, Olds, Zhang, Kallus, *A Human-Augmenting Agentic Workflow for Observational Causal Inference* — **arXiv:2607.22443v1 (2026-07-24; digest 07-27)**

**arxiv-digest hit:** score 2 (propensity score + causal inference
keyword hits). Kallus (Cornell + Netflix) is a well-known causal-ML
name.

**Why HIGH.** Directly on the causal-inference thread. `oci-agent` is
an open-source Python package implementing a human-in-the-loop LLM
workflow around observational causal inference: covariate balance
checking, propensity score trimming, sensitivity analysis, doubly
robust learning of the ATE for a binary treatment, plus (added since
initial release) heterogeneous treatment effect estimation and multiple
continuous treatments via partially linear models.

Two reasons this is HIGH rather than METHODS-WATCH:
1. **The "human-augmenting" framing is the right one.** Fully-
   autonomous LLM-driven causal-inference agents have been called out
   (correctly) as dangerous — assumption elicitation, DAG scrutiny,
   and identifiability judgments are inherently a human job. A design
   that *automates the bookkeeping and preserves human oversight for
   the assumption layer* is aligned with the `causal-inference-os`
   philosophy in your skill library.
2. **Netflix has been running this at scale** (>100 analyses/month
   since June 2026), which is a real-world validation signal you
   don't often get for academic causal-inference tooling.

**Actionable follow-on.** Read for:
- **Sensitivity analysis** approach (E-value, bounds-based, or
  bespoke).
- **HTE support** — is it causal-forest style, meta-learner style,
  or DR-Learner style? This maps directly to which sub-thread of your
  ML-for-precision-health work it lands under.
- **Integration surface** — package Python, or does it require
  Netflix-internal infrastructure? Public GitHub repo, per the arxiv
  abstract.

**Where it links to your work.** Candidate addition to the
`causal-inference-os` skill's tool inventory. Also of interest as a
pattern for automating the "run the balance table, print the trimming
plot, log the sensitivity" boilerplate that eats time in every AoU
target-trial-emulation project.

---

### 13. Guo, Yang, Xu, Zheng, Sun, Li, *GraphRareBench: An Auditable Graph-Evidence Benchmark for Phenotype-Driven Rare-Disease Diagnosis* — **arXiv:2607.24878v1 (2026-07-27; digest 07-29)**

**arxiv-digest hit:** score 1 (`hpo` keyword). Code + data at
`https://github.com/GUI0609/GraphRareBench`.

**Why HIGH.** Rare-disease HPO-driven diagnosis is a core thread and
the benchmark's structural choices are exactly right for what has
been missing from the field:
- **2,365 ontology-derived cases + 18,093 target-confounder pairs** —
  the confounder-pair design (each target disease paired with
  graph-defined "hard confounders" that share HPO evidence) is the
  right way to measure discrimination, not just rank.
- **Full-pool retrieval, hard-confounder discrimination, evidence
  access** are treated as three separate axes of model behavior —
  matches the pattern you'd want if you were going to compare
  Phen2Gene, Phenolyzer, and modern LLM-based phenotype-driven
  diagnostic agents on the same footing.
- **Provenance-preserving** — source-linked evidence records, so
  agent evaluation can distinguish "correct answer, wrong evidence"
  from "correct answer, right evidence" (the target-evidence
  coverage delta of 0.561 between the two agents they benchmark
  makes exactly this point).
- Reports MRR **0.640–0.740** for supervised rankers, **0.746 / 0.718**
  for two LLM agents; but note that **22.1–43.7% of Hit@10 successes
  still ranked at least one graph-defined hard confounder above the
  target** — a diagnostic-audit metric that no prior benchmark surfaces.

**Actionable follow-on.** Even without reading the full paper, the
benchmark itself is worth cloning (small enough at 2,365 cases) and
running any HPO-based tool through it before deployment. Add to the
`wglab` / rare-disease skill's evaluation-references section.

---

### 14. García, García, Olivera, Pedroza et al., *Variant Curation and Classification in Rare Disease Genomics: Standards and Emerging Tools for Single-Nucleotide Variant Analysis* — **Archives of Medical Research 2026**

**Feeds:** Google Scholar "10 new citations to articles by Konrad
Karczewski" (07-27 14:34Z); `"variant interpretation" OR "variant
classification …"` keyword feed (07-26 11:32Z); *"Guidance for
estimating penetrance of monogenic …"* citations feed (07-26 11:32Z).
Triple-feed hit — the paper is being read broadly.

**Why HIGH.** Variant interpretation is an active thread. A 2026
review that covers ACMG/AMP standards + emerging tools + rare-disease
focus is exactly the current reference the field lacks — most
comparable reviews are 2020–2023 vintage and predate the AlphaMissense
/ REVEL2 / SpliceAI-v2 wave.

**Actionable follow-on.** Read for:
- **Tool coverage** — do they cover InterVar, CancerVar,
  AutoPVS1, TAPES, VarSome, and the newer AI-first tools
  (AlphaMissense, ESM-family for missense pathogenicity)?
- **RNA / splicing evidence** — INTERESTS.md explicitly flags this
  as a live area; a review that treats splicing evidence rigorously
  (as opposed to naming SpliceAI and moving on) is useful.
- **ClinGen VCEP alignment** — do they map their recommendations to
  gene-specific VCEP guidelines?

**Where it links to your work.** Reference candidate for the
`wglab` skill's ANNOVAR / InterVar / CancerVar section.

---

### 15. Jin, Wan, Leaman, Tian, Wang, Yang… *Tutorial: guidance on the use of large language models for medical research* — **Nature Protocols 2026**

**Feed:** Google Scholar "Zhiyong Lu — new articles" (07-27 14:34Z).

**Why HIGH.** Nature Protocols tutorial from Zhiyong Lu's group is a
canonical reference — Lu leads the NLM BioNLP group (the `ncbi-nlp`
skill inventory), and Leaman (BioNLP research, GNorm2 / AIONER
lineage) as co-author signals that the tutorial will be grounded in
what actually works in biomedical text, not generic LLM advice.
Frontier-model-era (GPT-5 mentioned in the snippet) plus Nature
Protocols format means it will define citable methodology for
LLM-augmented medical-research workflows for the next 12–24 months.

**Actionable follow-on.** Read whole. Any AoU / BioVU project that
uses an LLM for note extraction, phenotype curation, or literature
retrieval will want to cite this rather than a preprint. Consider
adding a compressed extract into the `claude-api` or `ncbi-nlp`
skill.

---

## METHODS-WATCH (worth crib-noting, not required reads)

- **Parikh, Levin-Konigsberg, Tripuraneni, Madeka, Jordan, Foster,
  Perrault-Joncas, Volfovsky, *Towards Optimal Estimators for Randomized
  Control Trials* — arXiv:2607.23254v1 (2026-07-25; digest 07-28).**
  Framework for estimator selection *within families of RCTs* using
  sample-splitting; demonstrated on Amazon Supply Chain Optimization
  trials + Strengthening Democracy Challenge (25 interventions). Finds
  weighted least squares best for *inference* goals; difference-in-means
  best for *decision* goals. Not on-thread (industry RCTs, not
  observational clinical), but the "your best estimator depends on your
  loss" framing is portable to your pharmacoepi TTE work.
- **Neubrander, Tierney, Volfovsky, *The Confounder Trap:
  Treatment-Encoding Representations in Causal Inference with Text* —
  arXiv:2607.26309v1 (2026-07-28; digest 07-30).** Formalizes
  representation-induced overlap failure when the *treatment itself* is
  encoded in the text used to build the confounder adjustment
  representation. Deletion masking (bag-of-words / topic models) and
  replacement masking (LLM contexts) as remedies. Relevant for any
  clinical-text-based causal inference (e.g., MDR / opioid indication
  extraction from notes) — a class of problem you may encounter under
  the OMOP / notes side of the phenotyping thread.
- **Ali, *Auditing pretraining contamination in single-cell foundation
  model benchmarks* — arXiv:2607.20572v1 (2026-07-21; digest 07-24).**
  Not on-thread (scFMs, not EHR FMs), but the pretraining-contamination
  audit design (MinHash fingerprint + MIA + donor-matched embedding
  tightness test) is directly portable to EHR FM benchmark audits —
  a live concern for CLMBR / MOTOR / EHRSHOT evaluation. File under
  the EHR-foundation-models thread as a methods reference for
  benchmark hygiene.
- **Curtis, *Sequence effects on mutation rates investigated in
  whole-genome sequenced UK Biobank participants* — G3 2026 (PMID
  42522578).** Not on any active thread, but a UKB-WGS mutation-rate
  analysis is a piece of the genetic-epi infrastructure worth being
  aware of.
- **Sawada, Yuyama Otani, Iwata, Shibata, Okuda, Nishide, Uchiyama,
  Yamanishi, *DATTs: A Database of Disease-Associated Therapeutic Targets
  With Required Actions for Treatment* — Mol Inform 2026 (PMID 42521341).**
  Adjacent to drug-repurposing infrastructure; not on-thread by itself
  but useful as a KG / database companion to PrimeKG.
- **Arrarte et al., *Premature menopause is associated with the
  development of high blood pressure: a UK Biobank cohort study* —
  Menopause 2026 (PMID 42517361).** Marginal HRT thread connection
  (via the menopause axis).

---

## SKIPPED (present but off-thread)

Compressed list — noted for provenance so nothing is silently dropped:

- Ma et al. — LncRNA RP11-708J19.2 in colorectal cancer via SIRT7 /
  H3K18ac (European Journal of Histochemistry). Cites Chenjie's
  colorectal cancer work. Informational only.
- Van der Velden et al. — PSMA imaging in mCSPC (CAPRI-3 registry,
  European Journal of Nuclear Medicine). Cites Chenjie's prostate
  cancer work. Off-thread.
- HPRC2 pangenome preprint (Lucas, Hebbar, Liao et al., bioRxiv). Recurs
  across Yang, Montgomery, Karczewski, Denny citation feeds — genomics
  infrastructure, not on your active threads but broadly relevant
  reference genome update.
- Layeghifard, Díaz-Gay, Bergstrom et al. — Prior therapy defines
  mutation profiles in childhood cancer at relapse (Nature). Off-thread.
- Magaziner, Collins, Miller et al. — Cell-autonomous inflammation
  in VEXAS is mediated by cGAS-STING (Kastner citations feed).
  VEXAS is a tracked disease thread but this is basic-science
  mechanism, not the somatic-mosaicism / EHR-linked outcomes angle
  the thread specifically calls out. File for adjacent context but
  not required reading.
- Castellana, Chiappetta — AI/LLMs as decision-support tools in
  hospital compounding pharmacy (Bastarache citations feed). Off-thread.
- Kasimala, Kumar — PromptOps for LLM applications (Luo citations
  feed). Off-thread.
- Ghaderi et al. — Data reanalysis in AI era (PLoS Biology; Natarajan
  citations feed). Off-thread.
- Oh, Kim, Park, Kim — Model-and-task-aware test-time scaling for
  medical LLMs/VLMs (Szolovits related feed). Off-thread (evaluation
  methods for medical VLMs, not clinical-decision-tied ML).
- Zhu et al. — LLMs for Q&A generation from EHRs (Szolovits citations
  feed). Off-thread (educational Q&A, not phenotype extraction).
- Wang, Li, Liao — Anchoring virtual cells on gene programs (Pritchard
  citations feed). Off-thread.
- Zhang, Bao, Zeng et al. — Single-cell eQTL mapping in pigs (Montgomery
  related feed). Off-thread.
- Ren, Liu, Yin, Liu — Single-cell long-read transcriptomics review
  (Yang citations feed). Off-thread.
- Meyer, Frey, Brei et al. — LLM-KG-Bench-Framework 3 (Callahan related
  feed). Semantic Web / non-biomedical KG focus; INTERESTS.md
  down-weights this.
- Mishra, Diwan — Explainable multimodal systems in EHRs and predictive
  analytics (Brandt related feed). Book chapter; not primary research.
- Zhang, Kuang, Zhang, Horrillo, Chen et al. — 3D chromatin sensitivity
  to heart disease TF (Bing Ren feed). Off-thread.
- Pini, Shuffrey, O'Reilly Sparks et al. — PROGRESS in Autism at
  Columbia (Wendy Chung feed). Off-thread.
- Kendiukhov — Systematic evaluation of single-cell FM interpretability
  (Zitnik related feed). Off-thread (not EHR FMs).
- Peng, Wang, Song et al. — AI / generative models in hepatology (foundation
  models + EHR feed). Off-thread review.
- Joodi, Nawwar, Rasheed et al. — Fibromyalgia integrating pathophysiology
  with drug repurposing (drug repurposing feed). Off-thread review.
- Pärna, Sedman, Kariis, Vainik, Mõttus — Genetic architecture of eating
  disorder risk (PheWAS feed). Off-thread by disease.
- Elkaimbillah et al. — Educational recommender systems / KG (knowledge
  graph feed). Off-thread by domain.
- Wang, Li, Li, Yuan, Zhang — Metabolic syndrome + gastric cancer risk in
  UKB (UK Biobank feed). Off-thread by disease.
- Hendricks, Bochukova, Marenne et al. — Rare-variant analysis of obesity
  genes (Langenberg feed). 2017 back-catalog re-surface; not new work.
- Lau, Chekmeneva, Pinto, O'Halloran — Metabolomic clock of aging
  (Montgomery citations feed). Off-thread.
- Nyiransabimana — Nursing prevention/management of delirium in ICU
  (Luo citations feed). Off-thread.
- Gleason, Kidu, Babu, Hasselfeld, Wolff — Preclinical eval of AI in
  patient portal message management (Szolovits citations feed).
  Off-thread.
- Zhou, Wu, Liu, Tian, Castanon, Bartlett et al. — Human body single-cell
  atlas of 3D genome + DNA methylation (Michael Snyder feed). Off-thread.
- Song, Zheng, Yang et al. — Repurposing old drugs for tumor immune
  microenvironment (drug repurposing feed). Review; off the
  EHR-evidence-loop angle.
- Gupta, Singh, Shetty et al. — Repurposing masitinib as FOXM1 inhibitor
  in breast/oral cancer (drug repurposing feed). Off-thread (preclinical
  chemistry-only pipeline; INTERESTS.md explicitly deprioritizes this
  angle).
- Badawi, El-Sayed, Fawzy — Immunometabolic reprogramming in MS review
  (drug repurposing feed). Off-thread.
- Tang, Zhou, Qi et al. — Dual-granularity ncRNA-drug interactions
  (drug repurposing feed). Off-thread.
- Lin, Liu, Liao et al. — Imipramine reversing sorafenib resistance in
  HCC (drug repurposing feed). Off-thread mechanism paper.
- Choudhari, Sahariah, Jayapal et al. — Quinalphos environmental /
  biological effects (drug repurposing feed, mis-flagged). Off-thread.
- Tirdia, Lakhlan, Kumar et al. — Cross-species therapeutics in
  Plasmodium / Babesia (drug repurposing feed). Off-thread veterinary
  parasitology review.
- Husseinali, Mayo — Cutaneous malignancy in hidradenitis suppurativa,
  AoU case-control (AoU feed). Off-thread.
- Cook, Skibber, Wroe et al. — Health literacy in subarachnoid hemorrhage
  (AoU feed). Off-thread.
- Pein, Niklisch, Horn et al. — VEGFA / EGF polymorphisms in
  cholangiocarcinoma (UKB feed). Off-thread.
- Zhao, An, Cai et al. — Multimodal brain aging + 10 psychiatric
  disorders (UKB feed). Off-thread.
- Zhou, Liu, Zhang et al. — Single-cell eQTL MR for MAN1A2 in
  osteoarthritis (UKB feed). Off-thread.
- Versnjak, Trimarchi, Foryst-Ludwig et al. — Circulating PUFAs in
  AF/atrial cardiomyopathy (UKB feed). Off-thread.
- Chen, Tu, Zhu et al. — Regular hypnotic use and AMD (UKB feed).
  Off-thread.
- Zhang, Yu, Peng et al. — Plasma proteomics for cataract (UKB feed).
  Off-thread.
- Liu, Zhao, Li et al. — HA@Que-Mn nanozymes for postherpetic neuralgia
  (UKB feed, mis-flagged). Off-thread.
- Del Mauro, Li, Yu et al. — Sleep quality + cortical functional
  gradient (UKB feed). Off-thread.
- Zeng, Feng, Cheng et al. — CRP-TyG index for cardiovascular-kidney-
  metabolic syndrome (UKB feed). Off-thread.
- Chang, Lee, Chen et al. — Integrative genomic + transcriptomic analysis
  of hypertension in Taiwanese population (UKB feed). Off-thread.
- Xia, Otsuki, Mukaida et al. — Functional analysis of six RYR1 variants
  in Japanese malignant hyperthermia patients (Bastarache related feed).
  Variant-classification-adjacent but disease-specific; not on active
  threads.
- Lin, Liu, Xu, Shu, Song, Su, Li — L1CAM/ATP1A3/GAP43-positive EVs
  for Parkinson's disease (APOL1 feed, mis-flagged). Off-thread.
- Zhan, Zhu, Li, Wen — Transcription factor EN1 in bladder cancer
  malignancy (drug repurposing feed). Off-thread mechanism paper.
- Eftekhari, Sarmadi, Ghorbanpour Mardomakdeh — Venom peptides targeting
  potassium channels for autoimmune disease (autoimmune feed).
  Off-thread.

---

## Cross-report continuity notes

- The **Streit et al. Nature Genetics BPD GWAS + BPD-PheWAS** paper
  flagged in the 07-23 report continues to surface (indirectly via the
  BioVU-adjacent Bastarache circle); no new information this week.
- The **Baya et al. AJHG polygenic-deviation** paper (07-23 report,
  Denny related-research feed) also has not re-surfaced this week —
  worth reading before the next report to close the loop on the
  PRS-tail-inversion sub-thread.
- The **DRIVE v3** paper (Bastarache lab, 07-23 report) has not
  re-surfaced. Assumed still on the reading queue.
- The **Lemieux et al. JAMIA Open EHR interoperability** paper
  (07-23 report from NCBI AoU batch) re-surfaced this week via the
  Scholar `"All of Us research program"` keyword feed. Elevate its
  read priority.
- The **Gu et al. AoU multi-ancestry OUD GWAS** paper (07-23 report,
  Denny related-research feed) has not re-surfaced. Still on the
  reading queue.

---

## Suggested next actions

1. **Read Hwang et al. (AoU GLP-1 weight loss) first.** Direct
   template for any AoU-native GLP-1 pharmacoepi work you might
   spin up, and the fastest to extract actionable design decisions
   from.
2. **Skim Tang et al. BMJ (hair loss TTE) + Eze et al. (cancer
   outcomes review)** to close the current GLP-1 safety-signal
   picture.
3. **Clone GraphRareBench** (`https://github.com/GUI0609/GraphRareBench`)
   and run any HPO-based diagnostic pipeline through it before
   deployment — the target-vs-confounder audit is worth having
   locally regardless of publication plans.
4. **Add Chou et al. `oci-agent`** to the tool inventory of the
   `causal-inference-os` skill (Python package, GitHub-hosted, active
   at Netflix; matches the skill's philosophy of automating
   bookkeeping while preserving human oversight of assumptions).
5. **Read Jin et al. Nature Protocols** end-to-end — it will be the
   canonical citation for LLM methodology in medical research for
   the next ~year.
