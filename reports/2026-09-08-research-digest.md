# Research digest report — 2026-09-08

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-08 12:40Z** (~7 days since the
last research-digest report, covering seven arxiv-digest cron runs and
two Google Scholar alert batches — 09-07 16:17Z and 09-08 06:12Z —
plus the daily openRxiv medRxiv/bioRxiv Subject Collection Alerts).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-07.md`) | 09-01 → 09-07 daily crons | 7 daily runs. Dry days (0 papers, digest stub only): 09-03, 09-05, 09-06. 09-01: 1 paper (Ghiasi storage-centric (meta)genomic systems, `precision medicine` hit). 09-02: 1 paper (Ramesh et al. mudskippers on mud, `motor` hit — SKIP, off-topic keyword). 09-04: 2 papers (Cortez-Rodriguez natural-disasters × nonprofits panel-data causal inference; Yu et al. location-invariant extremal QTE for heavy-tailed distributions). 09-07: 1 paper (Rajabli & Collins compact brain-age FM adapted to Alzheimer's downstream tasks via LoRA). |
| No `arxiv-digest` email hits from GitHub | — | Second-time confirmation: `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads. The pipeline commits directly to this repo (nightly cron `daily-arxiv-digest.yml`, 10:30 UTC); the on-disk digests *are* the arxiv-digest feed for this account. |
| Google Scholar alerts (09-08 batch, 06:12Z) | 09-08 06:12Z | 12 keyword feeds fired: `rare diseases` (P2X7 review — SKIP mechanism paper), `Foundation models + "electronic health records"` (NeuroVision-FM self-supervised brain-MRI FM — METHODS-WATCH), `"All of Us research program"` (Sarder et al. SES × maternal mental health in AoU), `"drug repurposing"` (Bührman et al. iPSC governance — SKIP), `"electronic health records"` (**Liu et al. Nature Medicine MoChiAgent** — Mother-Child LLM agent for perinatal outcomes from longitudinal EHR), `"variant interpretation" OR "variant classification"` (Hull et al. RS1 VCEP criteria + variant curation), `"UK Biobank"` (Katz Social Science & Medicine MR of obesity → employment), `APOL1` (van Hougenhouk-Tulleken et al. Clinical Kidney Journal blood pressure × APOL1 in South African chronic haemodialysis), `mendelian diseases` (Huang & Xiao bidirectional MR AD × lichen planus — SKIP), `"autoimmune disorders" OR "autoimmune diseases"` (Michalek et al. Rev Cardiovasc Med aortic aneurysm autoimmune review), `"knowledge graph"` (Liu et al. Scientific Reports temporal KG with global-KG + historical matrix), `intitle:"clonal hematopoiesis"` (Da Silva Faria et al. Blood Advances CH in autoimmune hemolytic anemia). |
| Google Scholar alerts (09-07 batch, 16:17Z) | 09-07 16:17Z | 18 author-related feeds fired. HIGH-triage anchors: **Denny** (`citations-to` led with Hysong et al. AJHG SCT PheWAS/LabWAS meta-analysis across BioVU + Penn Med Biobank + AoU; `new-related` led with Roberts et al. IJPRAS polygenic pharmacotherapy evidence map). **Bastarache** (`new-related` led with GenPhenia DNN rare-disease Human Genomics 2026). **Karczewski** (`new-related` led with Loay et al. AJHG mutation-rate-heterogeneity bias in variant effect predictors; `citations-to` NMD transcriptional-adaptation in yeast — SKIP). **George Hripcsak** (`citations-to` led with Bai et al. Sci Rep relation-aware multimodal KG for DDI prediction). **Patrick Ryan** (`new-related` led with **Syrona** — open-source pairwise-comparison visual analytics for OMOP CDM). **Stephen B Montgomery** (`new-related` led with Ma et al. medRxiv long-read RNA-seq for splicing outlier detection in rare-disease trios). **Tiffany J Callahan** (`new-related` led with Bai et al. J Pharm KG-based screening of synergistic anticancer drug combinations). **Yuan Luo** (`citations-to` led with Lei et al. Am J Nephrol multi-dimensional sleep patterns × CKD complications & mortality in UKB). **Chenjie Zeng** (`new-related` led with Erhabor et al. Archives Med Sci AoU e-cigarette repeated cross-sectional 2017–2023). **Marinka Zitnik + Peter Szolovits + Zhiyong Lu** feeds all led with Ho et al. arXiv 2026 Language Models Can Control Their Own Attention (off-topic for these threads, but represents a shared cross-lab-attention observation across the ML feeds). **Kai Wang** (`new-related` m6A ACS Chem Biol — off-topic). **Neil M Davies** (single letter response, `citations-to` — SKIP). **Alexander (Sasha) Gusev + Goncalo Abecasis + Jian Yang + Daniel Kastner + Vivek Natarajan** — no HIGH-priority hits above what the specific keyword feeds captured. |
| openRxiv Subject Collection Alerts (09-08 batch, 00:01Z bioRxiv + 00:05Z medRxiv) | 09-08 00:01–00:05Z | Daily openRxiv digests for the subscribed collections (medRxiv: Epidemiology / Genetic and Genomic Medicine / Oncology Epidemiology / Maternal Fetal Medicine; bioRxiv: Bioinformatics / Genetics / Genomics / Immunology). These emails carry titles-only lists; the substantive discoveries this window arrived through the Scholar feeds above (Ma et al. long-read RNA-seq medRxiv shows on both Montgomery citations-to AND the medRxiv Genetic and Genomic Medicine collection). |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Nine HIGH items surfaced this window, clustering into five knots:

**PheWAS × biobank × EHR-linkage cluster (2 items).** Hysong et al.
*AJHG* 2026 (Denny citations-to feed) — the direct-hit paper of the
week: **sickle cell trait (SCT) PheWAS + LabWAS meta-analysis across
BioVU + Penn Med Biobank + All of Us**, 4,813 SCT among 58,830 African-
ancestry participants (~60% female). Three-biobank African-ancestry
PheWAS at exactly the scale your `PheWAS / phecode infrastructure` and
`Biobanks with EHR linkage` threads target. Brownstein et al. *Journal
of Medical Genetics* 2026 (cross-fired on Denny citations-to,
Karczewski new-related) — **whole-exome sequencing + EMR-linked biobank
data to identify candidate deafness genes**, integrating gnomAD-style
constraint (Karczewski overlap) with EHR phenotypes for a category
where up to half of inherited cases remain unsolved; a textbook
`EHR-linked biobank analysis is a core theme` paper for the rare-
Mendelian × common-biobank interface.

**Variant interpretation & VEP-audit cluster (2 items).** Loay et al.
*AJHG* 2026 (Karczewski new-related) — **mutation rate heterogeneity
biases variant effect prediction and reveals genuine mutational
robustness**, showing that conservation-based VEPs implicitly assume
uniform mutation rates and that correcting for context-specific
mutation rate changes the interpretation of "constraint" across sites.
Directly serves `Variant interpretation (ACMG / ClinGen)` and the
LOFTEE / pLoF-burden methods subthread. Hull et al. *Human Genetics*
2026 (variant-classification keyword feed) — **RS1-specific ACMG/AMP
variant classification criteria with pilot variant curation**, the
gene-based-therapy driver for X-linked retinoschisis. A canonical
ClinGen-VCEP guideline paper for your variant-curation-tooling
subthread.

**EHR foundation-model & LLM-agent cluster (2 items).** Liu et al.
*Nature Medicine* 2026 (`electronic health records` keyword feed) —
**MoChiAgent**, an LLM-based clinical assistant that orchestrates
multiple sub-agents to jointly predict maternal and infant outcomes
from *longitudinal linked mother-child EHR*. This is a full-journal
Nature Medicine LLM-agent EHR-FM paper; the linked mother-child design
is a scaling axis your `Digital twins from EHR data` subthread
prioritizes. Sarder et al. 2026 (AoU keyword feed) — **socioeconomic
status × maternal mental health in All of Us**, the AoU cohort's own
maternal-outcome descriptive companion for the MoChiAgent framing.

**Rare-disease diagnostic-benchmarking cluster (2 items).** Brunello et
al. *Human Genomics* 2026 (Bastarache new-related) — **GenPhenia**, a
deep-neural-network method addressing complex genotype–phenotype
relationships (pleiotropy, locus heterogeneity) in rare-disease
diagnosis. Slots directly into the Guo et al. GraphRareBench /
Phenolyzer / Phen2Gene / PhenoSV / LIRICAL / Exomiser / PhenoGPT2
benchmarking family your `Auditable HPO-driven diagnostic benchmarks`
subthread tracks. Ma et al. *medRxiv* 2026 (Montgomery new-related) —
**long-read RNA-seq improves isoform and splicing outlier detection in
whole blood from rare-disease trios**, the exact "splicing / RNA
evidence for VUS resolution" subthread in your Variant Interpretation
thread, with long-read + trio design as the discovery lever.

**Pharmacoepi / pharmacogenomics / KG cluster (1 item).** Roberts et
al. *International Journal of Pharmaceutical Research and Allied
Sciences* 2026 (Denny new-related) — **polygenic pharmacotherapy
beyond single-gene rules: an evidence map of scores, interactions,
ancestry transferability, and clinical utility**. Positioning review
for exactly your `Pharmacogenomic modifiers of medication persistence`
subthread — PGx expanded from CYP2D6-style single-gene rules to
score-based, GxE-modulated, ancestry-portable rules.

Also on the METHODS-WATCH ledger this window, six items worth
cribbing rather than reading front-to-back:

- **Bai et al. *Scientific Reports* 2026** (Hripcsak citations-to) —
  relation-aware multimodal KG learning for drug-drug interaction
  prediction. On-topic for `Knowledge graphs & ontologies` and for
  the `Drug repurposing` KG/GNN-with-explainable-hypothesis-output
  subthread.
- **Bai et al. *J Pharm Anal* 2026** (Callahan new-related) — KG-based
  screening for synergistic anticancer drug combinations, same
  KG+GNN pattern applied to combinatorial oncology repurposing.
- **Pajusalu et al. *BMC Med Informatics* 2026 — Syrona** (Ryan new-
  related) — open-source visual analytics tool for pairwise comparison
  of health datasets in OMOP CDM. Direct pairing to the CohortContrast
  workflow your previous digest flagged (2026-09-01 report).
- **Krantz et al. *JAMA Network Open* 2026** (Denny citations-to) —
  HLA-A*32:01 and lamotrigine-induced DRESS. HLA pharmacogenetic
  screening panel extension; pairs with your existing MH/RYR1
  interest from the 2026-09-01 report.
- **Zhang et al. *Genomics Proteomics & Bioinformatics* 2026** (Denny
  new-related) — benchmarking Bayesian colocalization methods in
  validating MR-identified targets. Direct-lift methods paper for
  your **drug-target MR triangulated with observational cohort
  estimates** subthread.
- **Liu, Ramteke & Anand *Genome Research* 2026** (Denny new-related)
  — biobank-scale method for learning modulators of genetic effects
  (G→E interactions). On-topic for `GxE and PGS × exposure /
  environment interactions` (Nagpal & Gibson lineage).

Plus one arxiv-digest METHODS-WATCH:

- **Rajabli & Collins arXiv 2609.05400v1** (09-07 digest) — compact
  brain-age supervised pretrained 3D CNN adapted via LoRA (~1%
  parameters) to Alzheimer's downstream tasks; strong template for
  **model-reuse under strict data constraints**, cross-cohort
  transfer without retraining (ADNI → OASIS-3 unchanged), and
  logit-fusion with age + cognitive score for MCI progression. On-
  topic for `EHR foundation models` (as an imaging FM audit
  companion) and for `Machine learning for precision health` (with
  a real clinical-decision hook: MCI stable-vs-progressing).

---

## Detailed reports on studies relevant to research interests

### HIGH-1 — Hysong et al. *American Journal of Human Genetics* 2026: Phenome- and laboratory-wide meta-analyses of sickle cell trait reveal multi-system disease associations

- **Cite:** MR Hysong, MM Shuey, TW Miller-Fleming, K Keat, … *AJHG* 2026. Link (cell.com): https://www.cell.com/ajhg/fulltext/S0002-9297(26)00311-3
- **Signal path:** Joshua C. Denny citations-to feed (09-07 16:17Z),
  cross-fired on Konrad Karczewski new-related, Lisa Bastarache
  citations-to.
- **INTERESTS.md threads served:** `PheWAS / phecode infrastructure`
  (primary); `Biobanks with EHR linkage: All of Us, UK Biobank, MVP,
  BioVU` (co-primary); `Genetic epidemiology` (ancestry-stratified,
  cross-ancestry PheWAS).
- **What it does.** Three-biobank meta-analysis of phenome-wide and
  clinical laboratory-wide associations of sickle cell trait (SCT,
  heterozygous HBB *S* carriers) in **58,830 African-ancestry
  participants (~60% female)**, of whom **4,813 carry SCT**. Cohorts
  are Vanderbilt's BioVU, Penn Medicine Biobank, and *All of Us* — the
  exact three you flag in `Biobanks with EHR linkage` and one of only
  a handful of studies in this window to run *all three* together.
- **Why it's HIGH.** (i) SCT has historically been under-studied
  because it doesn't cause disease as a Mendelian carrier state, and
  penetrance estimates for its adverse-outcome associations *outside*
  clinically-ascertained cohorts are exactly what your penetrance-
  under-population-screening framing wants. (ii) Adding LabWAS on top
  of PheWAS is the "depth of EHR follow-up" methods lever your thread
  calls out — the phenotype endpoint moves off ICD-derived phecodes
  and onto quantitative lab-value distributions, which is a much
  denser signal in an EHR-linked biobank. (iii) The African-ancestry
  focus is the ancestry-stratified analogue of most PheWAS work,
  addressing a well-known coverage gap in AoU / BioVU / Penn Med
  studies where non-European ancestries are historically under-
  powered.
- **Method notes to crib.** Meta-analysis mechanics across
  three US biobanks with heterogeneous phecode coverage; joint
  PheWAS + LabWAS design, which is directly portable to your
  Trikafta/CFTR-modulator, APOL1 kidney, and LOY-CHIP subthreads
  wherever the outcome of interest is dominated by a lab value rather
  than an ICD code.
- **Follow-up.** Read full paper (BioVU/Penn/AoU harmonization,
  African-ancestry PheWAS as an ancestry-stratified template), and
  triangulate against Acharya et al. *J Human Genet* 2026 (three-
  biobank ASCVD heritability, MyCode + UKB + AoU) flagged in the
  2026-09-01 report for a matched cross-biobank ancestry design.

### HIGH-2 — Brownstein et al. *Journal of Medical Genetics* 2026: Exome sequencing and large-scale analysis of electronic medical record-linked biobank data identify candidate deafness genes

- **Cite:** Z Brownstein, L Kamal, Y Zoabi, K Gesin, H Knoller, … *J
  Med Genet* 2026-09-02. Link: https://jmg.bmj.com/content/early/2026/09/02/jmg-2026-111784
- **Signal path:** Joshua C. Denny citations-to (09-07), also on
  Konrad Karczewski new-related — cites gnomAD constraint map. Cross-
  fired signal means both a PheWAS-lineage feed *and* a constraint-
  method feed picked it up.
- **INTERESTS.md threads served:** `Biobanks with EHR linkage`
  (primary); `Rare disease` (primary — inherited hearing loss); `EHR
  phenotyping & OMOP` (secondary — EMR-derived hearing-loss
  phenotypes as gene-discovery outcome); `Variant interpretation
  (ACMG / ClinGen)` (secondary — LOFTEE/pLoF within an EHR-linked
  cohort).
- **What it does.** Uses WES paired with EMR-linked biobank data to
  identify candidate genes for hearing loss, exploiting the biobank +
  EMR pairing to expand the spectrum beyond the ~half of inherited
  hearing-loss cases that remain genetically unresolved with standard
  panels. The value proposition is exactly the one your thread
  articulates: EHR breadth + genomic sequencing depth as a rare-
  variant discovery instrument.
- **Why it's HIGH.** The paper is the "EHR-linked biobank rescue" of a
  Mendelian-disease category (hearing loss) where clinical genetic
  testing routinely stalls. It sits at the intersection of three of
  your active threads — biobanks + rare disease + variant curation —
  and cites *A genomic mutational constraint map using variation in
  76,156 …* (gnomAD family). Read it against the Uria-Regojo et al.
  medRxiv 2026 mid-scale reanalysis paper your `Data-driven reanalysis
  of unsolved cases at 10k+ cohort scale` subthread flagged.
- **Method notes to crib.** The workflow (EHR-derived phenotype
  ascertainment → variant filtering by gnomAD constraint → burden /
  aggregation in EHR-linked biobank → clinical review of surviving
  candidates) is the template you want mirrored on other rare-disease
  categories (e.g., BRCA carriers with incident cancer, APOL1
  carriers with CKD conversion, HTT preclinical HD).

### HIGH-3 — Loay et al. *American Journal of Human Genetics* 2026: Mutation rate heterogeneity biases variant effect prediction and reveals genuine mutational robustness

- **Cite:** H Loay, P Kar, E Koch, V Seplyarskiy, D Weghorn. *AJHG*
  2026. Link: https://www.cell.com/ajhg/abstract/S0002-9297(26)00312-5
- **Signal path:** Karczewski new-related feed (09-07 16:17Z).
- **INTERESTS.md threads served:** `Variant interpretation (ACMG /
  ClinGen)` (primary — VEP audit); `Genetic epidemiology` (secondary
  — constraint / heritability under nonuniform mutation-rate
  landscape).
- **What it does.** Systematically shows that variant effect
  predictors (VEPs) built on sequence conservation implicitly treat
  conservation as evidence of functional constraint, but that
  variation in *mutation rate* across the genome produces conservation
  patterns that look like constraint even where no fitness selection
  is acting. Correcting for context-specific mutation-rate
  heterogeneity strips out the bias and separates *genuine*
  mutational robustness from apparent constraint.
- **Why it's HIGH.** This is a foundational audit of the entire class
  of VEPs — AlphaMissense, EVE, ESM1v, PrimateAI — that you and every
  ACMG-AMP variant curator lean on for `PP3/BP4` computational
  evidence. If the correction changes conservation-based priors at a
  non-trivial fraction of sites, PP3/BP4 calls at those sites may
  need re-weighting. It directly parallels the audit logic of the
  scContam / MIA-scFM pretraining-contamination papers in your `EHR
  foundation models` thread — same "the benchmark isn't measuring
  what we thought" pattern.
- **Method notes to crib.** The correction is a plug-in re-weighting
  step, so it's usable on top of any existing VEP output. Read for
  (a) how large the correction is on canonical clinical genes, (b)
  whether the correction is downloadable as a per-site adjustment
  track, and (c) whether the effect is uniform across the coding
  genome or concentrated in specific mutation-context classes
  (CpG-transitions vs. AT-transversions, etc.).

### HIGH-4 — Hull et al. *Human Genetics* 2026: Development of RS1-specific ACMG/AMP variant classification criteria with pilot variant curation

- **Cite:** S Hull, M Mero, W Hankey, K Lee, LS Sullivan, … *Human
  Genetics* 2026.
- **Signal path:** `"variant interpretation" OR "variant
  classification"` keyword feed (09-08 06:12Z).
- **INTERESTS.md threads served:** `Variant interpretation (ACMG /
  ClinGen)` (primary — gene-specific VCEP criteria); `Rare disease`
  (secondary — X-linked retinoschisis, a rare gene-therapy target).
- **What it does.** Develops RS1-specific ACMG/AMP variant
  classification criteria for X-linked retinoschisis (juvenile-onset
  vision loss). Gene-based therapies are advancing for RS1, so
  variant-level classification (LP / P vs. VUS) is now a clinical
  gating decision for gene therapy eligibility, not just a curation
  record. Includes a pilot variant curation set applying the RS1-
  specific criteria.
- **Why it's HIGH.** The clinical-gating point matters — a VUS that a
  VCEP could reclassify as LP unlocks gene-therapy access. Your
  variant-curation-tooling subthread is exactly this pipeline
  (InterVar, AnFiSA-style DSLs, LOFTEE, pLoF burden), and RS1 gives
  a fresh gene-specific playbook to compare against the CFTR VCEP
  work you already track and against the ClinGen general framework.
- **Follow-up.** Pair with the Krantz et al. JAMA Network Open 2026
  HLA-A*32:01 lamotrigine-DRESS paper (Denny citations-to, same
  09-07 batch) — different mechanism (HLA pharmacogenetic screening
  vs. ACMG VCEP for a coding gene), but the same "convert genetic
  evidence into a clinical gating decision" pipeline.

### HIGH-5 — Liu et al. *Nature Medicine* 2026 — MoChiAgent: Prediction of maternal and infant outcomes from longitudinal electronic health records with a Mother-Child AI agent

- **Cite:** S Liu, W Zheng, J Kang, T Xu, S Chen, G Li, J Li, … *Nature
  Medicine* 2026. Link: https://www.nature.com/articles/s41591-026-04694-y
- **Signal path:** `"electronic health records"` keyword feed (09-08
  06:12Z, marked IMPORTANT).
- **INTERESTS.md threads served:** `EHR foundation models` (primary —
  full-journal LLM-agent EHR paper, exactly the `Digital twins from
  EHR data` framing); `Knowledge representation in EHRs and
  applications` (co-primary — mother-child longitudinal EHR linkage as
  a `Structural and temporal representation of the patient timeline`
  choice); `Machine learning for precision health` (secondary — tied
  to clinical decisions about when to escalate perinatal care).
- **What it does.** Builds MoChiAgent, an LLM-based clinical assistant
  that orchestrates multiple sub-agents to jointly predict maternal
  and infant outcomes from *longitudinal mother-child linked* EHR.
  Current predictive models fragment the outcome (predict
  preeclampsia; predict preterm birth; predict neonatal jaundice;
  predict maternal depression; each as its own model), and often
  depend on costly imaging or lab tests. The MoChiAgent design flips
  that: one orchestrator, many endpoints, EHR-only inputs.
- **Why it's HIGH.** Two structural properties push this from
  METHODS-WATCH into HIGH: (i) the mother-child *linked-EHR* design
  is a distinctive structural representation choice — the patient
  timeline is now a *dyad* timeline, exactly the kind of
  representation-choice-drives-downstream-performance ablation your
  `Knowledge representation in EHRs` thread wants papers on; (ii)
  a *Nature Medicine*-tier LLM-agent EHR-FM paper is a field-defining
  landmark on the timeline from CLMBR/MOTOR/MEDS-FEMR/EHRSHOT and
  Ideker/Oermann-*Cell* 2026 digital-twin framing.
- **Method notes to crib.** How many sub-agents, and are they modality-
  specialized (codes / notes / labs / medications) or endpoint-
  specialized (maternal / fetal / infant)? How does the orchestrator
  arbitrate conflicting sub-agent outputs? What's the calibration
  behavior across trimesters (a temporal representation issue)? How
  does it perform on rare adverse endpoints where the base rate
  starves any single-endpoint model? Also worth reading against the
  Ellershaw et al. Foresight-England national-scale generative EHR-
  FM paper from the 2026-09-01 report.

### HIGH-6 — Sarder et al. 2026: Associations of Socioeconomic Status with Maternal Mental Health: Insight from NIH All of Us Research Program

- **Cite:** U Sarder, J Jackson, A Britt, T Gary, A Cao. 2026.
- **Signal path:** `"All of Us research program"` keyword feed (09-08
  06:12Z).
- **INTERESTS.md threads served:** `Biobanks with EHR linkage: All of
  Us, UK Biobank, MVP, BioVU` (primary — AoU descriptive-epi paper on
  maternal mental health); `Chronic disease clustering and
  multimorbidity` (secondary — SES × maternal mental health is a
  social-determinant × chronic-disease design).
- **What it does.** AoU descriptive-epi study characterizing the
  association between socioeconomic status and maternal mental health
  outcomes. Not a methods paper; a cohort-descriptive companion to
  the MoChiAgent framing (HIGH-5 above).
- **Why it's HIGH.** Ordinarily "clinical-question papers using these
  cohorts" are medium in your rubric — but paired with the MoChiAgent
  Nature Medicine paper this week, the two together give you
  *outcome* (MoChiAgent's prediction targets) + *risk factor
  landscape* (SES gradients on maternal mental health) in AoU. Read
  as one item.

### HIGH-7 — Brunello et al. *Human Genomics* 2026 — GenPhenia: using deep neural networks to accelerate rare-disease diagnosis

- **Cite:** FG Brunello, G Colangelo, A Rius, L Erra, AC Lugones, …
  *Human Genomics* 2026.
- **Signal path:** Lisa Bastarache new-related (09-07 16:17Z).
- **INTERESTS.md threads served:** `Rare disease` (primary — HPO-
  based deep-phenotyping diagnostic tools); `Knowledge graphs &
  ontologies` (secondary — HPO ontology as the phenotype substrate).
- **What it does.** GenPhenia is a deep neural network for rare-
  disease diagnosis targeted at the complex genotype-phenotype
  relationships (pleiotropy and locus heterogeneity) that break
  traditional single-gene approaches. Extension / new entrant in the
  Phenolyzer / Phen2Gene / PhenoSV / LIRICAL / Exomiser / PhenoGPT2
  benchmarking family.
- **Why it's HIGH.** Your `Auditable HPO-driven diagnostic benchmarks
  with separable metrics for ranking vs. evidence coverage` subthread
  (GraphRareBench reference-benchmark update, Guo et al. arXiv
  2607.24878) wants every new HPO-driven diagnostic to be
  benchmarked with **separable** ranking-vs-evidence-coverage
  metrics, not just Hit@10. Read GenPhenia specifically for whether
  it reports separable metrics — if it only reports Hit@k / MRR,
  that's exactly the QC argument you want propagated.
- **Method notes to crib.** DNN architecture choice (are phenotypes
  encoded as HPO term embeddings? as term-frequency vectors? as
  ontology-walk embeddings?). Training set size and case-source
  (single-center vs. multi-consortium — matters for the Uria-Regojo-
  scale reanalysis comparison). Whether the paper reports
  performance stratified by locus heterogeneity or pleiotropy tier —
  which is the point of the paper.

### HIGH-8 — Ma et al. *medRxiv* 2026: Long-read RNA sequencing improves isoform and splicing outlier detection in whole blood from rare disease trios

- **Cite:** J Ma, B Weisburd, S DiTroia, L Romo, LE Covill, … medRxiv
  2026.
- **Signal path:** Stephen B Montgomery new-related (09-07 16:17Z,
  marked IMPORTANT). Also present in the medRxiv Genetic and Genomic
  Medicine subject collection alert (09-08 00:05Z).
- **INTERESTS.md threads served:** `Variant interpretation (ACMG /
  ClinGen)` (primary — splicing / RNA evidence for VUS resolution);
  `Rare disease` (co-primary — trio design, splicing-outlier
  discovery); `Genetic epidemiology` (secondary — long-read
  technology impact on variant calling / annotation).
- **What it does.** Applies long-read RNA sequencing to whole blood
  from rare-disease trios to improve detection of isoform-level and
  splicing-outlier events that short-read RNA-seq misses. Blood is
  the accessible-tissue proxy; the trio design (proband + both
  parents) provides the inheritance framing for classifying an
  isoform anomaly as pathogenic.
- **Why it's HIGH.** Your Variant Interpretation thread explicitly
  calls out "splicing / RNA evidence for VUS resolution" as a
  subthread. This paper is the technology-lift version of that
  subthread — long-read RNA-seq lets you *see* the anomalous isoform
  that a short-read run inferred at best statistically. Also directly
  overlaps with the HPRC v2 pangenome-informed calling subthread
  (long-read data as the substrate for pangenome-aware
  interpretation).

### HIGH-9 — Roberts et al. *International Journal of Pharmaceutical Research and Allied Sciences* 2026: Polygenic Pharmacotherapy beyond Single-Gene Rules — An Evidence Map of Scores, Interactions, Ancestry Transferability, and Clinical Utility

- **Cite:** M Roberts, S Thompson, J Anderson, R Smith. *IJPRAS* 2026.
- **Signal path:** Joshua C. Denny new-related (09-07 16:17Z).
- **INTERESTS.md threads served:** `Causal inference and
  pharmacoepidemiology` (primary — `Pharmacogenomic modifiers of
  medication persistence` subthread); `Genetic epidemiology`
  (co-primary — PRS / polygenic scores subthread with pharmacotherapy
  as the outcome).
- **What it does.** Evidence-mapping review of polygenic pharmacotherapy
  — moving pharmacogenomics from CYP2D6-style single-gene rules
  toward score-based, interaction-aware, ancestry-transferable, and
  clinically-actionable frameworks. Explicitly organizes across
  (i) score construction, (ii) drug-drug / drug-gene interactions,
  (iii) cross-ancestry portability, and (iv) clinical utility
  evidence.
- **Why it's HIGH.** Your `Pharmacogenomic modifiers of medication
  persistence` subthread positions PGx as an outcome-modifier of
  real-world discontinuation / MPR for CFTR-modulators, statins, HRT,
  GLP-1 RAs. This review is the positioning paper for that whole
  subthread; use it as the citation-anchor when framing
  discontinuation / MPR analyses.
- **Follow-up.** Pair with Krantz et al. JAMA Network Open 2026 HLA-
  A*32:01 lamotrigine-DRESS (Denny citations-to, same batch), which
  is the *single-gene* PGx endpoint that this review would
  categorize as the baseline for polygenic extension. Together the
  two papers give you the single-gene → polygenic PGx spectrum in one
  batch.

---

## METHODS-WATCH ledger

The seven items below (six Scholar + one arxiv-digest) are worth
cribbing for methodology or as bookkeeping citations, but they aren't
front-to-back reads.

**MW-1. Bai et al. *Scientific Reports* 2026 (Hripcsak citations-to)**
— Relation-aware multimodal KG learning for drug-drug interaction
prediction. Textbook `Knowledge graphs & ontologies` + `Drug
repurposing` KG+GNN pattern; read for the "relation-aware" attention
mechanism and whether the paper delivers path- or subgraph-rationale
explanations (your `explainable hypothesis output` requirement) or
only opaque link-prediction scores. The latter would push this to
SKIP.

**MW-2. Bai et al. *J Pharm Anal* 2026 (Callahan new-related)** —
KG-based screening for synergistic anticancer drug combinations.
Same author cluster (Bai) as MW-1, different disease surface;
combined-therapy repurposing rather than DDI-safety. Same
explainability question applies.

**MW-3. Pajusalu et al. *BMC Med Informatics* 2026 — Syrona (Ryan
new-related)** — Open-source visual analytics for pairwise comparison
of health datasets in OMOP CDM. Direct pairing to CohortContrast
(Ilves et al., flagged in the 2026-09-01 report): both are OMOP-
native cross-site comparison tools. If they cover different comparison
axes (concept coverage vs. temporal drift, e.g.), you get a stackable
audit pipeline; if they overlap, pick one as the tooling reference.

**MW-4. Krantz et al. *JAMA Network Open* 2026 (Denny citations-to)**
— HLA-A*32:01 and lamotrigine-induced drug reaction with eosinophilia
and systemic symptoms (DRESS). Extends the HLA-B*15:02 / HLA-A*31:01
carbamazepine screening panels — a canonical single-gene PGx
endpoint. Pair with HIGH-9 Roberts et al. above for the single-gene →
polygenic PGx spectrum.

**MW-5. Zhang et al. *Genomics, Proteomics & Bioinformatics* 2026
(Denny new-related)** — Benchmarking Bayesian colocalization methods
in validating MR-identified targets. Direct methods lift for your
`Drug-target Mendelian randomisation triangulated with observational
cohort estimates` subthread (Saxby et al. metformin × AAA; MR-ALasso
lineage). Read for method-choice guidance (coloc, coloc-SuSiE,
Predictive-coloc, etc.) when triangulating MR hits against
observational cohorts.

**MW-6. Liu, Ramteke & Anand *Genome Research* 2026 (Denny new-related)**
— A biobank-scale method for learning modulators of genetic effects
(G→E). Nagpal & Gibson pervasive-PGS-×-exposure family. Read for
whether the method scales to All of Us / UK Biobank and whether the
learned modulators are interpretable environmental factors (SES,
diet, smoking) or opaque latent variables.

**MW-7. Rajabli & Collins arXiv 2609.05400v1 (09-07 digest)** —
Compact brain-age-supervised 3D CNN adapted via LoRA (~1%
parameters) to Alzheimer's downstream tasks. Impressive cross-cohort
transfer: adapted for CN-vs-Dementia on ADNI (AUC 0.964) then
applied *unchanged* to OASIS-3 (AUC 0.871). Multi-task reuse:
amyloid positivity from structural MRI (AUC 0.804), MCI progression
with logit + age + cognitive-score fusion (AUC 0.828), ICV-
normalized hippocampal and WMH volumes (R² 0.80, 0.91) using a much
smaller footprint than U-Net baselines. Direct template for
`Machine learning for precision health` — the MCI stable-vs-
progressing endpoint is exactly the clinical-decision hook your
thread rewards. Also a companion audit substrate for the
imaging-FM audit lineage (parallel to Wu et al. ACT auditable CT
phenotyping from your 2026-09-01 report).

---

## SKIP ledger (why the surfaced items did not clear triage)

- **P2X7 Receptor review in Rare Diseases** (rare-diseases keyword,
  09-08) — molecular-mechanism review, not clinical / phenotype work.
- **Ramesh et al. mudskippers on mud** (arxiv-digest 09-02) —
  "motor" keyword hit is a false-positive (biomechanics of amphibious
  locomotion).
- **Cortez-Rodriguez natural-disasters × nonprofits** (arxiv-digest
  09-04, `causal inference` keyword) — panel-data causal-inference
  methods paper is on-shelf for methodology but off-thread for
  biomedical work. Potentially METHODS-WATCH if you ever need to
  cite panel-DiD for a policy-adjacent question.
- **Yu et al. location-invariant extremal QTE** (arxiv-digest 09-04,
  `propensity score` keyword) — pure statistical methods paper on
  extreme-quantile treatment effects for heavy-tailed distributions.
  On-shelf for methodology; off-thread for biomedical direct-use.
- **Ho et al. Language Models Can Control Their Own Attention**
  (Zitnik / Szolovits / Lu new-related, 09-07) — LLM interpretability
  paper; off-topic for your EHR-FM / clinical-NLP threads even
  though it fired multiple author feeds.
- **Xiao et al. m6A ACS Chem Biol** (Kai Wang new-related, 09-07) —
  epitranscriptomics, off-thread.
- **Bührman et al. iPSC governance** (drug-repurposing keyword,
  09-08) — governance / regulatory review, not computational
  repurposing work.
- **Huang & Xiao AD × lichen planus MR** (mendelian-diseases
  keyword, 09-08) — pairwise trait MR of unclear clinical
  relevance; typical "MR-Base pipeline on paired ICD codes" output
  that surfaces regularly and rarely clears triage.
- **Katz obesity × employment MR in UKB** (UK Biobank keyword,
  09-08) — health-economics MR outside the biomedical outcome
  space.
- **Aquino-Jarquin genomic-governance commentary** (Denny citations-to,
  09-07) — policy commentary, not methods.

---

## Anchor updates against `INTERESTS.md`

No changes to the active-thread list this week. The nine HIGH items
cluster inside the existing threads without opening a new lane. The
"long-read RNA-seq for rare-disease VUS resolution" note (HIGH-8, Ma
et al.) is close enough to the existing splicing/RNA-evidence
subthread that it doesn't warrant a new bullet — but if a second
long-read trio paper lands within the next 2-3 windows, promote it
to its own sub-bullet under `Variant interpretation (ACMG / ClinGen)`.
The MoChiAgent paper (HIGH-5) is the strongest signal so far in this
window for the `Digital twins from EHR data` subthread, but as one
paper it doesn't move the anchor either.

---

## Housekeeping

- 3 of the 7 daily arxiv-digest runs this window were dry (09-03,
  09-05, 09-06 — each is a 138-byte "no relevant papers" stub).
  That's consistent with weekend / early-week arxiv posting cadence
  in the tracked categories (`q-bio.QM / q-bio.GN / q-bio.PE /
  stat.AP`). No pipeline-health concern.
- The `noreply@github.com` subscription for arxiv-digest is still
  quiet in Gmail — the cron writes commits directly rather than
  emailing PR notifications, so digest reads should stay on the
  local repo path (`digests/`) rather than the inbox. This mirrors
  the 2026-09-01 report finding; nothing to change.
