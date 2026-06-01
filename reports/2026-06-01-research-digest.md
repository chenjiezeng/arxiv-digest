# Research digest report — 2026-06-01

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-05-30 → 2026-06-01** (since the prior 2026-05-29 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-05-30 → 06-01 | Two batches: 05-31 22:24 UTC (author + citation alerts) and 06-01 07:24 UTC (keyword alerts). |
| `arxiv-digest` repo (`digests/`) | 2026-05-29 → 05-31 | **Empty.** 05-30 = 0 relevant; 05-31 = 0 relevant with 3/4 categories failing to fetch (q-bio.QM, q-bio.GN, q-bio.PE). Pipeline is currently silent. |
| bioRxiv / medRxiv subject alerts | daily | Aggregate collection digests, not individually triaged. |
| Raw arXiv daily mailings (`no-reply@arxiv.org`) | daily | Unfiltered cs/q-bio/stat to a list address; not triaged here. |

> ⚠️ The `arxiv-digest` GitHub pipeline produced **no signal** this window. The
> 2026-05-31 run logged "3/4 categories failed to fetch" — q-bio fetches
> intermittently failed. Suggest a re-run or upstream-fetch retry-loop fix
> before the next cycle. (Same recommendation as the prior report — issue
> persists.)

> Caveat: Scholar alert emails contain title, authors, venue, and the first
> ~2-3 lines of each abstract only. The reports below contextualize that
> metadata against your research threads; nothing here reflects full-text
> reading.

---

## Executive summary

- **All of Us is the dominant cluster this window.** Eight distinct AoU
  papers surfaced — including (notably) a paper with **you as a coauthor**
  in the "All of Us research program" keyword feed (#3 below, Yang/Schaffer/
  Tran/Zeng/Park on hormone therapy + metabolic markers in prostate cancer).
  This is the ASCO 2026 abstract round, so several are conference abstracts
  rather than full papers — flagged inline.
- **Pharmacoepi / GLP-1**: a high-quality AoU GLP-1 RA → liver-outcomes
  paper in MASLD/T2D landed in your *Chenjie Zeng* "new related research"
  alert (AJG, full paper). Squarely on your GLP-1 drug-class thread.
- **CHIP / somatic mosaicism**: two high-tier items — a meta-analysis on
  CHIP and CV outcomes after hematopoietic-cell transplantation, and a
  *Nature* paper (Karczewski/Neale/Wei Zhou alerts × 3) on the *mechanism*
  of age-related mtDNA mutation accumulation in blood. The mtDNA paper is a
  natural complement to CHIP biology.
- **Genetic epi**: *Nature* paper on "distinct genetic architecture in the
  tails of complex traits" (Souaiaia et al.) surfaced in **six** different
  author alerts (Denny, Montgomery, Pritchard, Jian Yang × 2, Wei Zhou) —
  unusual saturation, signals strong relevance to PRS/rare-variant
  composite-risk work.
- **EHR phenotyping**: three concrete items — leakage-safe multimorbidity
  phenotypes in AoU (Rahemi & Omidi), reasoning-intensive EHR consistency
  verification (Kwon et al.), and EHR-vs-self-report discordance (Mojtahedi
  et al.). All three touch data quality, your AoU IBD-data-quality thread,
  and computable-phenotype rigor.
- **Drug repurposing**: a prototype-augmented graph-representation paper
  for brain-disorder gene identification with explicit repurposing framing
  — fits your KG/GNN-with-explainability preference.
- **EHR foundation models**: ICML 2026 workshop paper on patient-aware
  sampling for EHR FM pretraining (Placidi et al.) — directly relevant to
  the CLMBR/MOTOR/FEMR lineage.

Counts: **14 HIGH**, **5 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. GLP-1 receptor agonist use and liver-related outcomes in MASLD and type 2 diabetes in the All of Us Research Program
- **Authors / venue:** R.T. Chung et al. — *American Journal of Gastroenterology*, 2026.
- **Surfaced by:** **Chenjie Zeng "new related research"** alert (i.e., adjacent to your own work).
- **Thread:** Pharmacoepidemiology (GLP-1 drug-class) **+** EHR-linked biobanks (All of Us).
- **What it is:** AoU-based observational study of GLP-1 RA exposure and
  liver-related outcomes in adults with MASLD (metabolic dysfunction-
  associated steatotic liver disease) and type 2 diabetes. Published in
  *AJG*, so full paper, not a conference abstract.
- **Why it matters to you:** Hits the intersection of three active threads
  — GLP-1 RA pharmacoepi, AoU as the cohort vehicle, and confounding-by-
  indication management in real-world drug-outcome studies. The fact that
  it appears in *your* author-related feed signals it shares either
  methodological or citation lineage with your published work. Likely uses
  some form of new-user / active-comparator design; worth reading for
  exposure-window and incident-MASLD outcome operationalization in AoU.
- **Action:** **HIGH** — read in full for the AoU exposure/outcome
  definitions and the design (TTE? new-user cohort? Cox vs IPW?).

### 2. Assessing data quality of inflammatory bowel disease patients in the All of Us research program
- **Authors / venue:** M. Spotnitz, A.S. Faye, J. Giannini, T.R. Litwin, Y. Ostchega, et al. — *JAMIA Open*, 2026.
- **Surfaced by:** "All of Us research program" keyword alert (06-01).
- **Thread:** IBD disease thread **+** EHR-linked biobanks (AoU) **+** EHR phenotyping (data quality).
- **What it is:** Data-quality audit of AoU's IBD patient sub-cohort —
  evaluates how well AoU's EHR + biospecimen + genomic streams can be
  trusted for IBD-focused research. Snippet emphasizes the multi-stream
  nature (EHRs, biospecimens, genomics).
- **Why it matters to you:** Directly serves the IBD thread *and* feeds
  your AoU phenotyping work. A formal data-quality assessment for a tracked
  disease is exactly the kind of paper to cite when you're justifying AoU
  cohort construction in your own IBD/autoimmune work. Authors (Spotnitz,
  Faye) are Columbia OHDSI / OMOP-CDM adjacent — likely uses OHDSI Data
  Quality Dashboard or Achilles-style checks.
- **Action:** **HIGH** — read for the DQ framework used (Achilles? Kahn-
  framework dimensions?) and IBD-specific phenotype validation.

### 3. Metabolic and inflammatory marker elevations and associations with hormone therapy usage in prostate cancer patients of the All of Us Research Program cohort
- **Authors / venue:** Y.J. Yang, K.R. Schaffer, T.C. Tran, **C. Zeng**, B.H. Park et al. — ASCO 2026 (JCO suppl. abstract 5031).
- **Surfaced by:** "All of Us research program" keyword alert (06-01).
- **Thread:** This is **your own paper** appearing in your AoU keyword feed.
- **What it is:** AoU analysis of prostate-cancer patients comparing those
  on hormone therapy (HT/ADT) vs not, with respect to metabolic and
  inflammatory markers. ASCO 2026 abstract.
- **Why it matters to you:** Flagging because it's *yours* — useful for
  your own records / citation tracking. Also useful to know that AoU
  keyword feeds will surface your own work; consider adding an `author:Zeng`
  exclusion if you want to avoid self-hits, or keep them as a citation
  audit signal.
- **Action:** No new action; logging that the keyword pipeline correctly
  caught your ASCO abstract. (Aside: this is a HT/ADT pharmacoepi paper in
  AoU — overlaps with your HRT thread infrastructure even though the
  clinical question is different.)

### 4. Clonal hematopoiesis and cardiovascular outcomes after hematopoietic cell transplantation: A systematic review and meta-analysis
- **Authors / venue:** L. Thulluri, A. Bowen, K. Quasem, M. Carrasquel-Alvarez et al. — *Journal of Hematology …*, 2026.
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert (06-01).
- **Thread:** Clonal hematopoiesis (CHIP) disease thread.
- **What it is:** Systematic review + meta-analysis of CHIP and CV
  outcomes specifically in the post-HCT setting. A narrower clinical
  subpopulation than the Bick 800k-individual stroke paper from last week,
  but addresses a specific high-risk transplant context where donor or
  recipient CHIP matters.
- **Why it matters to you:** Extends the CHIP→CV-outcome literature into
  the HCT context. Useful for your composite-risk modeling — donor-derived
  CHIP is an under-studied somatic source of recipient cardiovascular risk.
  Complements last week's Bick stroke paper (#4 in the 2026-05-29 report)
  and the *Nature Communications* co-occurring-CHIP-mCA paper.
- **Action:** **HIGH** — read for effect sizes in the HCT-specific setting
  and overlap with the broader Bick et al. estimates.

### 5. Mechanism of age-related accumulation of mtDNA mutations in human blood
- **Authors / venue:** R. Gupta, T.J. Durham, G. Chau, M. Kanai, M.M. Uddin et al. — *Nature*, 2026.
- **Surfaced by:** Konrad Karczewski + Benjamin Neale + Wei Zhou author alerts (×3 — strong saturation signal).
- **Thread:** CHIP / somatic mosaicism (adjacent — mtDNA rather than nuclear CHIP variants).
- **What it is:** Nature paper on the mechanism by which mutant mtDNA
  accumulates in blood with age — somatic mosaicism in the mitochondrial
  genome rather than the nuclear genome.
- **Why it matters to you:** Your CHIP thread is anchored on *nuclear*
  somatic events (DNMT3A, TET2, ASXL1, etc.), but mtDNA somatic mosaicism is
  a parallel age-related phenomenon with potential clinical readouts in
  hematology and oncology. The Broad-anchored author roster (Karczewski/
  Neale/Wei Zhou) signals high-quality population-genomics methodology.
  Worth reading as background for "biobank-scale somatic-mosaicism
  measurement at the mtDNA layer" — a methodological cousin of CHIP
  detection.
- **Action:** **HIGH** — read for the detection methodology (sequencing
  depth / heteroplasmy thresholds) and any biobank cohort used.

### 6. Distinct genetic architecture in the tails of complex traits
- **Authors / venue:** T. Souaiaia, H.M. Wu, A.P.S. Ori, S.W. Choi, C.J. Hoggart et al. — *Nature*, 2026.
- **Surfaced by:** **6 separate author alerts** — Joshua C. Denny, Stephen B. Montgomery, Jonathan K. Pritchard, Jian Yang (×2: "new related" + "10 new citations"), Wei Zhou. Unusually high saturation.
- **Thread:** Genetic epidemiology (GWAS, PRS, tail/extreme phenotypes,
  rare-variant + common-variant architecture).
- **What it is:** Nature paper investigating how genetic architecture
  (common-variant polygenicity vs. rare large-effect variants) varies along
  the *trait continuum* — i.e., whether the tails of complex traits are
  enriched for rare large-effect variants relative to the bulk distribution.
  Snippet: "Complex traits are highly polygenic, with heritability explained
  by many hundreds of common variants of small effect together with rare
  variants of large effect. Yet how this genetic architecture varies along
  the trait continuum has been underexplored…"
- **Why it matters to you:** This is *directly* on your composite-risk
  modeling thread (PRS stacked with rare pathogenic variants) and your
  penetrance-in-population-screening thread. If common-vs-rare architecture
  differs at the extremes, that has direct implications for how you weight
  PRS vs monogenic variant evidence in penetrance estimation — extremes of
  phenotype distributions are exactly where monogenic carriers concentrate.
  6-author-alert saturation suggests this will be a high-citation paper
  going into your active drafts.
- **Action:** **HIGH** — read carefully; likely the single most directly
  relevant paper of the window for your PheRS/PRS-composite work.

### 7. Pretraining EHR Foundation Models with Patient-Aware Sampling
- **Authors / venue:** J.C. Placidi, Y. Liu, J. Han, M. Rei, A.A. Faisal — ICML 2026 Workshop on Structured Data for AI.
- **Surfaced by:** "Foundation models and 'electronic health records'" keyword alert (06-01).
- **Thread:** EHR foundation models (CLMBR/MOTOR/FEMR/MEDS lineage).
- **What it is:** Autoregressive EHR foundation-model pretraining with a
  *patient-aware* sampling strategy — i.e., the sampler is aware of
  patient-level structure rather than treating tokens iid. The snippet is
  truncated but the framing is "autoregressive foundation models for
  [EHR/clinical sequences]…"
- **Why it matters to you:** Patient-aware sampling is exactly the kind of
  tokenization/sampling design choice that distinguishes EHR FMs from
  language FMs (visits, irregular time, patient identity). Slots directly
  into your CLMBR/MOTOR/FEMR thread. ICML workshop, so likely shorter and
  early — good for tracking where the field is heading on sampling design.
- **Action:** **HIGH** — read for the sampling formulation and how it
  compares to MOTOR/FEMR positional handling.

### 8. A prototype-augmented graph representation learning framework for identifying brain disorder-associated genes and facilitating drug repurposing
- **Authors / venue:** J. Li, Y. Li, S. Lin, J. Rao, H. Zhao — *PLOS [Computational Biology?]*, 2026.
- **Surfaced by:** "drug repurposing" keyword alert (06-01).
- **Thread:** Drug repurposing (KG/GNN angle, with explainability).
- **What it is:** Graph representation learning with *prototypes* —
  prototype-based attention/aggregation tends to provide more
  interpretable per-prediction rationales than vanilla GNN embeddings —
  applied to brain-disorder-gene identification and downstream repurposing.
- **Why it matters to you:** Your INTERESTS file flags "knowledge-graph /
  GNN approaches with *explainable* hypothesis output (path or subgraph
  rationales rather than opaque link-prediction scores)". Prototype-
  augmented GNNs are one of the cleaner ways to attach an interpretable
  rationale (the prototypes serve as exemplars). Brain disorder is not a
  tracked disease, but the *method* is on-thread.
- **Action:** **HIGH** — read for the prototype mechanism (how prototypes
  are learned, how rationales are extracted), then evaluate whether the
  same architecture is transferable to your rare-disease HPO-based
  repurposing angle.

### 9. A Foundational Exome Resource for Jordan: Dual Ancestry Admixture and Population-Specific Variants to Improve Clinical Variant Interpretation
- **Authors / venue:** T. Froukh — *medRxiv*, 2026.
- **Surfaced by:** Konrad Karczewski "new related research" alert.
- **Thread:** Variant interpretation (ACMG/ClinGen) **+** cross-ancestry portability.
- **What it is:** A foundational exome reference for the Jordanian
  population — characterizes dual-ancestry admixture and identifies
  population-specific variants to improve clinical variant classification.
  Open-access on medRxiv.
- **Why it matters to you:** Variant interpretation in non-European
  ancestries is a recurring gap — population-specific variant frequencies
  drive ACMG PM2/BS1 evidence codes. A region-specific exome reference is
  exactly the kind of resource that improves penetrance estimation in
  population-screening contexts (your monogenic-penetrance interest). Also
  relevant if you're building cross-ancestry composite-risk models.
- **Action:** **HIGH** — skim for the variant-call pipeline and whether
  Jordanian-specific frequencies are deposited in gnomAD or kept local.

### 10. Deterministic Overlapping Multimorbidity Phenotypes for Leakage-Safe EHR Modeling of Incident Cognitive Impairment in All of Us
- **Authors / venue:** Z. Rahemi, M. Omidi — *Journal of Interdisciplinary Research Applied to Medicine*, 2026.
- **Surfaced by:** George Hripcsak "10 new citations" alert (citing OHDSI work).
- **Thread:** Chronic disease clustering / multimorbidity **+** EHR phenotyping **+** AoU.
- **What it is:** Multimorbidity phenotyping framework using *deterministic
  overlapping* phenotypes (rather than mutually-exclusive clusters or
  summary indices like Charlson) with explicit attention to *leakage* (i.e.,
  outcome features inadvertently leaking into the multimorbidity feature
  set when modeling an incident outcome). Applied to incident cognitive
  impairment in AoU, anchored at first SARS-CoV-2-positive test, N = 23,435
  adults ≥50.
- **Why it matters to you:** Direct hit on your multimorbidity thread.
  Three things make it interesting: (i) deterministic + overlapping is a
  middle path between unsupervised cluster labels (unstable) and summary
  indices (oversimplified) — both of which your INTERESTS flags as
  shortcomings; (ii) leakage-safe framing is a methodological rigor point
  often glossed in multimorbidity work; (iii) it's in AoU, so the cohort
  construction is directly portable to your AoU work.
- **Action:** **HIGH** — read for the deterministic overlapping phenotype
  definition (probably rule-based on diagnosis codes) and the leakage-
  prevention protocol.

### 11. Towards Error-Free EHRs: Reasoning-Intensive Consistency Verification Between Clinical Notes and Structured Tables in Electronic Health Records
- **Authors / venue:** Y. Kwon, J. Kim, J. Choi, P. Rabaey, M. Kim, S. Im, J. — 2026.
- **Surfaced by:** George Hripcsak "new related research" alert.
- **Thread:** EHR phenotyping (note-structured consistency, LLM-assisted) **+** EHR data quality.
- **What it is:** Reasoning-intensive (likely LLM-based) consistency
  verification between free-text clinical notes and structured EHR tables
  — i.e., flagging disagreements between what the note says vs. what the
  coded diagnoses/medications/labs say.
- **Why it matters to you:** Note-vs-structured discordance is a major
  source of phenotype noise (and citation #12 below quantifies it from a
  different angle). LLM-based reasoning verifiers are a practical tool for
  computable-phenotype QC at scale. Slot this into your "LLM-assisted
  phenotyping" interest under EHR phenotyping & OMOP.
- **Action:** **HIGH** — read for the verifier prompt design and how
  disagreement is operationalized (does it produce per-record flags or
  population-level rates?).

### 12. Discordance Between Electronic Health Records and Self-Reported Data: Evidence from Traumatic Brain Injury and Colorectal Cancer
- **Authors / venue:** Z. Mojtahedi, A. Bolourian, T.S. Lane, M.R. Lininger — *Healthcare*, 2026.
- **Surfaced by:** Joshua C. Denny "new related research" alert.
- **Thread:** EHR phenotyping (data quality, validation against self-report).
- **What it is:** Empirical study of discordance between EHR-derived and
  self-reported diagnoses, using TBI and colorectal cancer as test cases.
- **Why it matters to you:** Self-report vs EHR discordance is a recurring
  challenge in AoU (which has both streams) and a key consideration for
  computable-phenotype validation. The TBI/CRC pairing gives you both an
  injury-event phenotype (often under-coded) and a cancer phenotype
  (typically registry-confirmed) — useful for triangulating where the gaps
  sit. Pairs naturally with #11 (notes-vs-structured) as a "ground-truth-
  is-fuzzy" methodological pair.
- **Action:** **HIGH** — read for the magnitude and direction of
  discordance per condition; useful as a citation when designing AoU
  phenotype validation.

### 13. Development of polyphenotypic scores to prioritize detection of G6PD rs1050828 heterozygotes in African and African American populations
- **Authors / venue:** T. Lu, D. Stein, W. Zhang, Y. Itan, A.D. Paterson — *Genetics in Medicine*, 2026.
- **Surfaced by:** Chenjie Zeng "new related research" alert.
- **Thread:** PheWAS / PheRS (this is a *poly-phenotypic score* — i.e., PheRS-style construction) **+** variant interpretation **+** ancestry-aware risk.
- **What it is:** Develops *polyphenotypic scores* — i.e., risk scores
  built from multiple phenotypic features (PheRS-style) — to prioritize
  detection of heterozygous carriers of the G6PD missense variant
  rs1050828 (p.Val98Met), which is common in African / African American
  populations and lowers HbA1c independently of glycemia (a classic
  variant–biomarker confounding case affecting diabetes diagnosis).
- **Why it matters to you:** **This is the closest hit of the window to
  your PheWAS/PheRS thread.** It combines (i) PheRS construction, (ii)
  ancestry-stratified application, (iii) variant-driven phenotype
  prioritization in a population where the variant is common — all three
  are on your bullet list. Also flagged as related to your own work by
  Scholar.
- **Action:** **HIGH** — read for the score-construction methodology and
  the population-screening framing. Highest PheRS-specific relevance this
  week.

### 14. Multi-omics triangulation identifies complement factor H as a genetically supported protective factor in IgA nephropathy
- **Authors / venue:** N. Shao, K. Tan, P. Chen, Q. Luo — *Clinical Kidney Journal*, 2026.
- **Surfaced by:** "phenome wide association studies" keyword alert (06-01).
- **Thread:** Genetic epidemiology (MR-style triangulation + multi-omics) **+** drug-target prioritization.
- **What it is:** Multi-omics triangulation (likely GWAS + proteomics MR +
  colocalization) nominating CFH as a genetically supported *protective*
  factor in IgA nephropathy.
- **Why it matters to you:** Same proteome-MR-for-target-prioritization
  template you saw 3× in the prior window (CD58/PARP1, lung function,
  breast cancer cross-ancestry). Continued evidence that this MR+coloc
  pattern is the dominant target-discovery shape across nephrology, lung,
  oncology, and now glomerular disease. Useful if you're considering
  adding `proteome-wide` / `colocalization` to `tracked.yaml` (suggested
  last time).
- **Action:** **HIGH (methods + repurposing)** — skim the triangulation
  pipeline; pair with last week's MR cluster.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Critical appraisal of fairness metrics for AI-based clinical prediction
  models: a scoping review** — J. Matos, B. Van Calster, L.A. Celi, P.
  Dhiman, J.W. Gichoya et al. — *Lancet Digital Health*, 2026. (Celi +
  Gary S. Collins alerts.) Scoping review of fairness metrics in clinical
  prediction. *Watch for:* the metric taxonomy + Van Calster/Collins
  perspective on calibration vs fairness trade-offs (relevant to your
  external-validation-across-ancestries interest).
- **Co-intelligence: a proposal for human–artificial intelligence
  collaboration for large language models in medical research** — A.Y. Ong,
  D.A. Merle, N.H. Shah, Y.C. Tham, T.Y. Wong et al. — *Lancet Digital
  Health*, 2026. (Nigam Shah alert.) Position piece on human-AI co-work in
  medical research. *Watch for:* the proposed workflow patterns — relevant
  if you're integrating LLM-assisted phenotyping into a human-in-the-loop
  curation pipeline.
- **Exploring Genetic Variations Associated with the Immune Response in
  Underrepresented Populations** — A.L. Hernández-Ledesma, E.L. Coss-
  Navarrete et al. — *Annual Review of Biomedical Data Science*, 2026.
  Cites the AoU "data quality, utility, and diversity" paper. *Watch for:*
  cross-ancestry immunogenetics review — useful background for your APOL1
  / IBD / autoimmune-PRS work.
- **Long COVID Persistence and Surveillance Gaps Across 58 US Hospitals**
  — J. Tian, A. Azhir, M. Decaro, N. Chau, J. Hügel, M. Morris et al. —
  *JAMA Network Open*, 2026. (Yuan Luo + Christopher G. Chute alerts ×2.)
  Multi-site EHR surveillance design. *Watch for:* the 58-site cohort
  construction and PASC ascertainment — methods are transferable to other
  multi-site biobank surveillance designs.
- **Recurrence modeling with EHR through NLP and ML techniques** — J.A.
  Fortino, H. Lin, A. Gulati, B. Srinivas, A. Park, S.S. Yom et al. —
  *(oncology venue)*, 2026. (EHR keyword alert.) Recurrence ascertainment
  from notes — relevant to your "exploit EHR depth (notes/labs/meds) for
  outcomes" line, even if oncology recurrence isn't a tracked disease.

---

## NOTABLE: AoU ASCO 2026 abstract roundup

The 2026-06-01 "All of Us research program" keyword alert mostly returned
**ASCO 2026 abstracts**. Most are conference-only and may not have full
papers attached yet — flagging titles for awareness:

- **Genome-wide association study of tyrosine kinase inhibitor–induced
  hepatotoxicity in All of Us** (Jung, Seomun, Han) — TKI pharmacogenomics
  in AoU; HIGH if you're tracking pharmacogenomic-AoU work.
- **Fine-scaled genomic ancestry clusters to reveal population-specific
  cancer enrichments in the All of Us Research Program** (Gupta, Isshiki,
  Ercelen et al.) — fine-scale ancestry vs self-reported race for cancer
  enrichment; HIGH for your trans-ancestry portability thread.
- **Many Genomes, One Disease: Genetic Risk of Hidradenitis Suppurativa
  Across Ancestries** (Williams, Belony, Last) — cross-ancestry HS
  genomics in AoU; medium (HS not tracked, but methods on-thread).
- **Consumer wearables / Fitbit-derived activity & heart rate for
  predicting hospitalization in AoU cancer cohort** (Najjar, Elkhider, et
  al., 3 separate abstracts) — wearables + AoU; SKIP unless you're moving
  into wearables.
- **Economic and Demographic Associations in Hypertension-Related
  Complications Among Florida Participants in AoU** (Benitez, Chanelo, Last)
  — student-research-day poster; SKIP.
- **ADHD and Food Insecurity in AoU** — SKIP.

---

## SKIP / noise (logged, no action)

- **`arxiv-digest` repo, 05-30 & 05-31:** zero relevant; 05-31 logged 3/4
  category fetch failures. No actionable papers from the pipeline this
  window.
- **"APOL1" keyword alert:** caught "Apolipoprotein variations across
  *APOE* genotypes in young and elderly patients with coronary heart
  disease" — false hit (APOE ≠ APOL1). Pattern is `APOE` matching `APOL1`
  via prefix; consider tightening the keyword to `apol1` with word-
  boundary anchoring.
- **"mendelian diseases" keyword alert:** caught a two-sample Mendelian-
  randomization paper on GERD → allergic asthma. MR ≠ Mendelian disease;
  add `-randomization` to the query if you want to exclude MR papers
  there (you have `mendelian randomization` separately under genetic epi
  in tracked.yaml).
- **"knowledge graph" keyword alert:** "Construction and application of a
  multimodal knowledge graph for machining deformation uncertainty
  analysis" — non-biomedical KG (manufacturing). SKIP per INTERESTS. The
  recurring noise from this keyword (3rd week running) reinforces the
  prior suggestion to require biomedical co-occurrence (e.g., `biomedical
  knowledge graph` or `clinical knowledge graph`).
- **"autoimmune disorders/diseases" keyword alert:** "NK cells in
  endocrine autoimmune disorders" review — basic immunology, not on the
  AoU/biobank thread. SKIP.
- **"rare diseases" keyword alert:** "Location matters: topography of
  germline CEBPA variants in familial AML" — single-gene rare-disease
  case discussion; not on the rare-variant-association-methods thread.
  SKIP (borderline).
- **"variant interpretation" keyword alert:** RAC1 variants drive distinct
  disorders (Coppola & Tartaglia, EJHG) — single-gene phenotype-genotype
  discussion; borderline SKIP unless you have a specific RASopathies
  thread.
- **AI in Rare Diseases: Workflow-Integrated Precision Kidney Care**
  (Thongprayoon et al., *Clinics and Practice*) — review piece in a
  lower-tier journal; the AoU/HPO-based-repurposing angle is mentioned
  but not central. Borderline SKIP.
- **ORCA: end-to-end causal-analysis copilot** (Xuan et al., arXiv) — LLM
  copilot for causal analysis, surfaced via Hripcsak citation feed.
  Generic / off-clinical-thread; SKIP.
- **Citation-only churn:** several Vogelstein / Szolovits / Zitnik /
  Natarajan / Shendure alerts continue to return generic
  LLM/cancer/CRISPR citations that don't overlap with active threads.
  SKIP.

---

## Suggestions for the pipeline

Carrying forward and refining from the prior report:

1. **`arxiv-digest` pipeline is silent and partially broken.** 05-31 logged
   3/4 q-bio category fetch failures, and the last 6 days of digests are
   all empty or score-1. Worth investigating: (a) is the upstream arXiv
   API rate-limiting? (b) does the fetcher retry on 5xx? (c) is the
   `--min-score 1` threshold too aggressive given current coverage?
   *And* the same structural point from the prior report stands: most of
   the genuinely on-thread papers are in journals + med/bio-rxiv, outside
   q-bio.QM/GN/PE/stat.AP. Adding `cs.LG`, `stat.ME`, and a medRxiv /
   bioRxiv source would catch ~80% of the items in this report.
2. **Tighten `apol1` matching.** Word-boundary anchoring (`\bapol1\b`)
   would suppress the recurring `APOE` false positives.
3. **Tighten `mendelian diseases` keyword.** Currently catching MR
   papers. Either exclude `-randomization` or merge it into the genetic-
   epi-side `mendelian randomization` keyword.
4. **`knowledge graph` keyword remains noisy** (3rd consecutive week).
   Recommend requiring biomedical co-occurrence.
5. **Add `proteome-wide` / `colocalization`** — 4 proteome-MR papers in
   the last two windows; clearly a recurring high-value shape.
6. **Self-citations:** Yang/Schaffer/Tran/Zeng/Park appeared in the AoU
   keyword feed. Either accept this as a citation-tracking signal or add
   an `-author:zeng` filter if it gets noisy.
