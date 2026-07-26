# Research digest report — 2026-07-26

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-23 12:00Z → 2026-07-26 12:00Z** (roughly the 72 hours
since the last committed report at `reports/2026-07-23-research-digest.md`).
This is a **3-day catch-up** — mostly weekend-adjacent volume, but two
double- / triple-feed hits demand attention. Items already covered in the
07-23 report and re-surfaced in the 07-24 and 07-26 alerts (Streit BPD
GWAS, Baya AJHG PGS-deviation, DRIVE v3, Żebrowska Circadian, Wu UKB
MetS, Lemieux JAMIA Open, Johnson AoU disparities, Jo East Asian meta)
are **not** re-detailed here — see the 07-23 report.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts — author cluster (07-24) | 2026-07-24 09:02Z | Ten author feeds fired — Denny, Bastarache, Karczewski, Ryan, Zeng, Zitnik, Callahan, Szolovits, Yang, Montgomery. Five on-thread hits (Yen SGLT2i-vs-GLP1RA target trial, Boltz Nat Genet BGE sequencing, Liou statin nongoal-response PGS, Lai S4-Multi PGS protocol, Baker DRIVE v3 — already covered). |
| Google Scholar alerts — author cluster (07-26) | 2026-07-26 05:17Z | Eleven author feeds fired — Ryan, Brandt, Hripcsak, Denny, Bastarache, Zeng, Karczewski, Zitnik, Callahan, Szolovits, Yang, Montgomery. Two multi-feed hits dominate: Wang binary silver labels EHR phenotyping (**triple-feed**: Ryan + Brandt + Hripcsak), Nguyen PrimeKG-Plus (**double-feed**: Zitnik + Callahan). |
| Google Scholar alerts — keyword feed ("All of Us research program") | 2026-07-25 03:27Z, 2026-07-26 11:32Z | Two AoU keyword pings — 07-25 = Johnson AoU disparities (already covered), 07-26 = Lemieux JAMIA Open EHR interoperability (already covered). No fresh AoU signal. |
| `arxiv-digest` repo (`digests/2026-07-24.md`, `-25.md`, `-26.md`) | 2026-07-24 / -25 / -26 (10:30Z cron) | **1 relevant paper across 3 days** — Ali scContam single-cell FM contamination audit (07-24, keyword `foundation model`, score 1). Both 07-25 and 07-26 empty. Suppression working — three previously-surfaced papers filtered out. |
| NCBI "My NCBI What's New" ("All of Us", "UK Biobank") | window | Not fired in this window (last NCBI batch was 07-23 11:53Z, covered in previous report). |
| bioRxiv / medRxiv Subject Collection Alerts | 07-24 → 07-26 daily | Aggregate feeds — individual papers surfaced upstream via Scholar. Not a separate net. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it.

---

## Executive summary

- **Weakly-supervised EHR phenotyping with binary silver labels — arXiv preprint.**
  Wang, Slaughter, Nelson, Williamson, *Using binary silver labels in
  electronic health records-based computable phenotyping algorithms*
  (arXiv 2607.18431). **Triple-feed** hit — Patrick Ryan, Pascal
  Brandt, and George Hripcsak all surface it in the same batch, which
  places it firmly in the OHDSI / EHR-phenotyping mainstream. Directly
  on the "computable phenotype development" sub-thread and adjacent
  to the PheValuator / KOMAP / silver-label lineage. **HIGH — read first.**
- **PrimeKG-Plus: literature-derived expansion of a multimodal precision-medicine
  KG — bioRxiv.** Nguyen, Nguyen-Phuong, Nguyen et al., *PrimeKG-Plus:
  a literature-derived expansion of a multimodal precision medicine
  knowledge graph* (bioRxiv 2026.07.14.738415). **Double-feed** hit
  (Marinka Zitnik + Tiffany Callahan). Refreshes all 20 original
  PrimeKG resources and adds literature-derived edges. Directly on
  the KG / ontology thread and the drug-repurposing thread (PrimeKG
  is the reference KG for TxGNN-style drug repurposing). **HIGH.**
- **Target-trial emulation of SGLT2i vs. GLP-1 RA for psoriatic
  arthritis in T2D.** Yen, Wang, Hwu, Chen, Hsu et al., *Comparative
  Risk of Psoriatic Arthritis in Type 2 Diabetes: An Emulated Target
  Trial of SGLT2 Inhibitors vs. GLP-1 Receptor Agonists* (Drug Design,
  Development & Therapy 2026; Ryan feed). Direct head-to-head TTE of
  the two drug classes on the pharmacoepi thread, with a novel outcome
  (PsA). **HIGH.**
- **Blended Genome Exome (BGE) sequencing in Nature Genetics — Broad
  Institute infrastructure paper.** Boltz, Chu, DeFelice, Liao,
  Sealock et al., *A blended genome and exome sequencing method
  captures genetic variation in an unbiased and cost-effective manner*
  (Nature Genetics 2026; Karczewski feed). 1–4× low-pass WGS + 30–40×
  deep WES in a single sequencing run — direct implications for
  next-gen AoU / biobank-scale sequencing. **HIGH (infrastructure).**
- **Polygenic prediction of statin nongoal-response — Circulation:
  Genomic and Precision Medicine.** Liou, García-González, Wu, Namba,
  Vaura et al., *Polygenic Prediction of Nongoal Response to Statin
  Therapy* (Circulation: Genomic and Precision Medicine 2026;
  Bastarache feed). LDL-C-response PGS to identify individuals unlikely
  to reach guideline-concordant targets — a clinical-utility PRS
  application squarely on your ML-for-precision-health and
  pharmacogenomics threads. **HIGH.**
- **S4-Multi protocol paper — STAR Protocols.** Lai, Tyrer, Baierl,
  Pharoah, Peng, *Protocol for constructing multi-ancestry polygenic
  models using S4-Multi* (STAR Protocols 2026; Denny feed). Reproducible
  step-by-step recipe for multi-ancestry PGS construction from the
  Pharoah / Peng ovarian-cancer group. Directly serves the
  trans-ancestry PGS portability thread. **HIGH (protocol utility).**
- **`arxiv-digest` — scContam single-cell FM contamination audit
  (only new paper in 3 days).** Sarwan Ali, *Auditing pretraining
  contamination in single-cell foundation model benchmarks* (arXiv
  2607.20572, 07-21 submission; keyword `foundation model`, score 1).
  scFM benchmark contamination detection — MinHash fingerprints +
  membership-inference. Off-thread from EHR FMs but methodologically
  parallel. **METHODS-WATCH.**
- **PrimeKG-Plus paired with Asada citation-aware pre-training gives
  two literature-derived KG angles this week.** Asada, Tsujimura,
  Ishigaki, Egami, Fukuda, *Citation-Aware Continual Pre-Training for
  Biomedical Language Models* (BioNLP 2026; Szolovits feed). Citation
  links as continual-pretraining signal for biomedical LMs. Not
  directly clinical, but a natural companion to PrimeKG-Plus if you
  end up thinking about literature-KG augmentation. **METHODS-WATCH.**
- **DPCGS — GWAS ↔ single-cell transcriptomics linker on bioRxiv.**
  Liu, Shen, Li, Zhu, Yang, Wu, Xuan et al., *DPCGS: a computational
  framework for linking GWAS to single-cell transcriptomics in
  complex traits and diseases* (bioRxiv 2026.07.14; Jian Yang feed).
  Framework for mapping GWAS signal onto cell-type-resolved expression
  — related to sc-DRS / MAGMA-scDRS lineage. Off the primary EHR
  thread but adjacent to genetic-epi + TWAS. **METHODS-WATCH.**
- **SHARE — human-AI co-learning for EHR phenotyping (medRxiv).**
  Yang, Zhang, Love, Animashaun, Zhong et al., *A framework for
  human-artificial intelligence co-learning for disease activity
  labeling using electronic health records* (medRxiv
  2026.07.16.26358271; Ryan feed). Synergistic Human-Agent REasoning
  system for scalable outcome phenotyping — directly on the
  LLM-assisted phenotyping thread. **METHODS-WATCH-HIGH.**
- **OMOP-standardized cancer temporal-trend protocol — BMJ Open.**
  López-Sánchez, Palomar-Cros, Giuliodori et al., *Temporal trends
  in epidemiology and patient characteristics of 36 cancers: a
  protocol for a multinational population-based cohort study using
  OMOP-standardised databases* (BMJ Open 2026; Ryan feed). OMOP-CDM
  reference protocol paper — Prieto-Alhambra Oxford consortium
  lineage. Directly on the OMOP thread and adjacent to your cancer
  epidemiology background. **HIGH (reference utility).**
- **Synthetic-EHR simulation for causal-inference method assessment
  (vaccine efficacy) — medRxiv.** Velasco Pardo, Daines, Katikireddi,
  Ritchie et al., *Simulation of synthetic health records for
  assessment of causal inference methods for vaccine efficacy*
  (medRxiv 2026.07.17.26358308; Ryan feed). Synthetic-EHR simulation
  benchmarking causal methods — a design pattern for validating your
  own TTE / IPTW workflows. **METHODS-WATCH.**

Everything else in this window is either off-thread (chemical /
diffusion / vision-language / animal-genomics feeds from broad
authors, IVF PGT methods, Fabry iPSC lines, goat population genomics,
prostate-cancer imaging registries) or a routine methods-watch
summarized in the tail section. The AoU keyword feed produced only
already-covered items.

---

## Detailed reports

### 1. Using binary silver labels in electronic health records-based computable phenotyping algorithms

**Authors.** S Wang, MT Slaughter, JC Nelson, BD Williamson.
**Venue.** arXiv preprint arXiv:2607.18431, 2026.
**Signal source.** Google Scholar author-feeds — **triple-feed** hit:
Patrick Ryan (top of 07-26 05:17Z batch), Pascal Brandt (top of
07-26 batch), George Hripcsak (top of 07-26 batch). All three feeds
place it at position 0.
**Bucket.** HIGH.
**Threads served.** EHR phenotyping & OMOP; ML for precision health
(weakly supervised outcome labeling); adjacent to PheValuator /
KOMAP tooling in the OHDSI stack.

**What the paper does (from title + snippet).** Formalizes weakly
supervised phenotyping in the setting where gold-standard chart-review
labels are unavailable at scale. The paper's contribution is
methodological: how to combine diagnosis-code-derived binary silver
labels with a downstream learner while accounting for the
label-noise process, so that the resulting phenotype algorithm has
calibrated performance despite training on imperfect labels.

**Why it matters for your work.**
1. **Triple-feed signal is the loudest possible.** Three OHDSI-adjacent
   author feeds (Ryan, Brandt, Hripcsak) surfacing the same
   preprint on the same day is the strongest possible indicator
   that this is going to become a reference paper in the
   computable-phenotype literature. Read it before it gets cited
   in your next AoU manuscript.
2. **Direct complement to PheValuator.** PheValuator (Swerdel et al.,
   OHDSI) evaluates existing rule-based phenotypes using
   silver-label probabilistic gold standards; this paper is the
   *training-time* analogue — build a model directly from silver
   labels. The two together give an end-to-end pipeline: build with
   silver labels → validate with silver labels → deploy. Natural
   fit for AoU-native phenotype development where gold-standard
   chart review is essentially impossible at scale.
3. **Bears on the LLM-assisted phenotyping thread.** LLM-extracted
   phenotype labels are silver by construction (they're
   noisy proxies for the underlying chart-review truth). The
   framework here should be portable to LLM-generated silver labels
   as a next step — a natural bridge into the SHARE / co-learning
   pattern (see report #10).

**Follow-ups.** Pull the arXiv PDF (2607.18431); check (a) which
label-noise process is assumed (constant per class? conditional on
patient features? conditional on covariates?), (b) whether the
authors give theoretical performance guarantees (e.g., risk-consistent
estimation) or only empirical evaluation, (c) which OMOP CDM benchmark
phenotypes were used for validation, (d) whether the codebase is
public (GitHub link).

---

### 2. PrimeKG-Plus: a literature-derived expansion of a multimodal precision medicine knowledge graph

**Authors.** TTD Nguyen, T Nguyen-Phuong, QH Nguyen et al.
**Venue.** bioRxiv, 2026 (2026.07.14.738415).
**Signal source.** Google Scholar author-feeds — **double-feed** hit:
Marinka Zitnik (top of 07-26 batch), Tiffany J Callahan (top of
07-26 batch). Both feeds place it at position 0.
**Bucket.** HIGH.
**Threads served.** Knowledge graphs & ontologies; drug repurposing
(PrimeKG is the reference KG for TxGNN and other drug-repurposing
GNN pipelines); rare disease.

**What the paper does (from snippet).** Extends PrimeKG (Chandak,
Huang, Zitnik, *Scientific Data* 2023) by (a) updating **all 20
original data resources** to their latest releases, and (b) adding
a literature-derived layer of edges — i.e. moving beyond curated
ontology-alignment edges to relations mined from the biomedical
literature. The precision-medicine KG becomes a moving target
that tracks the primary literature rather than remaining static.

**Why it matters for your work.**
1. **PrimeKG is the reference KG for drug repurposing with LLM /
   GNN pipelines.** The Zitnik lab's TxGNN paper builds on PrimeKG
   for zero-shot drug repurposing; extending PrimeKG matters
   whenever you touch drug-repurposing workflows in your reference
   class. The literature-derived expansion is exactly the kind of
   "explainable KG output" your drug-repurposing thread flags as
   high-priority.
2. **Callahan co-signal is meaningful.** Tiffany Callahan (PheKnowLator,
   OMOP2OBO) working on the same paper class as Zitnik implies
   this is the drug-repurposing / KG-for-clinical-reasoning
   convergence point. Callahan's PheKnowLator has been used for
   drug-repurposing hypothesis generation; expect follow-ups that
   plug PheKnowLator-style ontology edges into PrimeKG-Plus.
3. **Rare-disease angle.** PrimeKG includes rare-disease
   phenotypes and drug-disease-gene triples; the update should
   improve rare-disease drug-repurposing coverage — a natural fit
   for the HPO-based rare-disease reanalysis thread from the
   07-23 report (Uria-Regojo et al.).

**Follow-ups.** Pull the bioRxiv PDF; check (a) which 20 data
resources were updated and to which release dates, (b) how the
literature-derived edges were mined (co-occurrence? relation
extraction with a specific model?), (c) whether the release
provides scored edges (confidence per relation) or only binary
inclusion, (d) whether TxGNN-style benchmarks show improved
zero-shot indication prediction on the updated KG.

---

### 3. Comparative Risk of Psoriatic Arthritis in Type 2 Diabetes: An Emulated Target Trial of SGLT2 Inhibitors vs. GLP-1 Receptor Agonists

**Authors.** FS Yen, SI Wang, CM Hwu, KY Chen, CC Hsu et al.
**Venue.** *Drug Design, Development and Therapy*, 2026 (DDDT.S614222).
**Signal source.** Google Scholar author-feed — Patrick Ryan
(07-24 09:02Z; position 0).
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi (target trial
emulation); drug repurposing (both drug classes have expanding
indications); active drug threads for SGLT2is **and** GLP-1 RAs
(both explicitly named in `INTERESTS.md`).

**What the paper does (from title + snippet).** Head-to-head TTE
comparing SGLT2 inhibitors vs. GLP-1 receptor agonists on incident
psoriatic arthritis (PsA) risk in T2D patients. The paper explicitly
frames T2D + PsA comorbidity as high-burden (absenteeism, reduced
productivity, CV events), and TTE is used to estimate the causal
effect of the drug-class choice on PsA incidence.

**Why it matters for your work.**
1. **Head-to-head of the two drug classes you explicitly
   track.** `INTERESTS.md` lists SGLT2is and GLP-1 RAs as the two
   active drug threads inside pharmacoepi. A published head-to-head
   TTE on an unusual outcome (PsA — inflammatory / autoimmune, not
   the usual MACE endpoint) expands the effective outcome space
   for your future TTEs of the same drug pair.
2. **Autoimmune / inflammatory outcome is the interesting
   angle.** Most SGLT2i-vs-GLP1RA TTEs have focused on CV, renal,
   or metabolic outcomes; an inflammatory-arthritis outcome
   crosses into the IBD-adjacent autoimmune space you also track
   in `INTERESTS.md`. Worth pattern-matching against the
   GLP-1-RA-and-IBD-flares literature to see if a shared
   inflammatory-suppression mechanism story emerges.
3. **Template for AoU replication.** The design is straightforward
   (new-user cohort, active comparator, propensity score, censoring
   on discontinuation) and directly transplantable to AoU with
   phecode-derived PsA (phecode 696.4) as outcome — AoU's linked
   prescription data + phecode extraction makes this feasible.

**Follow-ups.** Pull the paper; check (a) data source (Taiwan NHI?
US claims?), (b) PsA outcome definition (ICD-9-CM 696.0 / ICD-10
L40.5, incident vs. prevalent), (c) treatment strategies (initiation
alone or as-treated), (d) sensitivity analyses for confounding by
indication (both drug classes have overlapping T2D indications but
non-overlapping obesity indications).

---

### 4. A blended genome and exome sequencing method captures genetic variation in an unbiased and cost-effective manner

**Authors.** TA Boltz, BB Chu, M DeFelice, C Liao, JM Sealock et al.
**Venue.** *Nature Genetics*, 2026 (s41588-026-02669-w).
**Signal source.** Google Scholar author-feed — Konrad Karczewski
(07-24 09:02Z; position 0).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology infrastructure; variant
interpretation (pLoF burden analyses depend on the sequencing
substrate); biobanks with EHR linkage (sequencing choice is a
first-order design decision).

**What the paper does (from abstract snippet).** Introduces the
**Blended Genome Exome (BGE)** method — a DNA library approach that
generates **1–4× low-pass whole-genome + 30–40× deep whole-exome
data in a single sequencing run**. Sealock on the author list is
Broad-adjacent, DeFelice / Liao are Broad Sequencing Platform. The
motivation is clear: cost-effective substrate for biobank-scale
studies that need both exome-quality coding variant calls AND
genome-wide imputation-quality common-variant tags.

**Why it matters for your work.**
1. **Substrate for the next generation of biobank sequencing.** AoU
   has ~245k WGS today; the cost per sample of full WGS is still
   ~$400–500. BGE at low-pass 1–4× is dramatically cheaper (~$100
   range), and if 1–4× WGS + 30–40× WES gives comparable
   imputation-quality genome-wide tags to full 30× WGS, it becomes
   the default choice for the *next* million-sample biobank round.
   Watch for AoU / MVP / UKB adoption announcements.
2. **Direct implications for pLoF-burden methods.** Your variant
   interpretation thread includes LOFTEE / pLoF burden methods; the
   30–40× WES arm of BGE is exactly the substrate those methods
   need. If BGE gives you clean pLoF calls + genome-wide common-
   variant tags in one library prep, downstream PRS+rare-variant
   composite models (see 07-23 report #1 — Baya AJHG) become a
   single-library workflow.
3. **Cost angle matters for AoU cohort expansion planning.** AoU's
   long-term plan targets 1M+ WGS; BGE could bend the cost curve
   enough to accelerate that timeline. Worth reading the cost /
   yield analysis in the paper before any AoU-scale sequencing-cost
   estimate.

**Follow-ups.** Pull the paper; check (a) imputation-quality
comparison against full 30× WGS on common variants (INFO
distributions), (b) rare-variant recall on the WES arm vs. standard
30× WES benchmarks, (c) structural-variant detection performance
(1–4× is thin for SVs), (d) whether BGE-produced libraries are
compatible with existing Broad WES + AoU imputation pipelines.

---

### 5. Polygenic Prediction of Nongoal Response to Statin Therapy

**Authors.** L Liou, J García-González, HM Wu, S Namba, F Vaura et al.
**Venue.** *Circulation: Genomic and Precision Medicine*, 2026
(CIRCGEN.125.005666).
**Signal source.** Google Scholar author-feed — Lisa Bastarache
(07-24 09:02Z; position 0).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (PGS for clinical
outcomes); ML for precision health (clinical-decision-tied ML);
pharmacogenomics-adjacent; causal inference / pharmacoepi (identifying
who benefits from statin therapy).

**What the paper does (from snippet).** Uses PGS to identify T2D /
CV patients unlikely to achieve **guideline-concordant LDL-C
lowering** on statin therapy — i.e. a "predicted statin
non-responders" score. The framing is inverted from the usual "PGS
predicts LDL-C" or "PGS predicts CV events" designs: instead, PGS
predicts *pharmacotherapy nongoal response*, which is directly
actionable at the clinical decision point.

**Why it matters for your work.**
1. **Clinical-decision-tied PGS is the exact HIGH-priority ML
   pattern from `INTERESTS.md`.** The interests file explicitly
   distinguishes "ML tied to a clinical decision" (HIGH) from
   "generic benchmark / leaderboard papers" (SKIP). A PGS whose
   output feeds directly into "escalate statin dose vs. switch to
   ezetimibe vs. add PCSK9" is exactly the decision-tied pattern.
2. **Namba co-author = BioBank Japan / trans-ancestry PGS
   context.** Shinichi Namba (Yamamoto lab, Osaka) working on
   statin-response PGS implies this is likely a multi-ancestry
   analysis — worth checking the ancestry composition and whether
   the PGS transfers across ancestries.
3. **Natural entry to a pharmacogenomics PheRS.** LDL-C-response
   PGS + phecode-derived cardiometabolic outcomes in AoU could
   become a PheRS-style multi-outcome scan: "how does a
   statin-nonresponder PGS map across the full phecode space?"
   Direct fit for your PheWAS/PheRS infrastructure thread.

**Follow-ups.** Pull the paper; check (a) which cohorts (UKB? MGB
Biobank? BioBank Japan? All-of-Us?) were used for discovery vs.
validation, (b) which outcome (LDL-C at 1y? binary goal-attainment?
percent LDL-C reduction?), (c) how the PGS was constructed (LDpred2?
PRS-CS-x for trans-ancestry?), (d) whether they estimate net
reclassification vs. standard clinical predictors (age, sex,
baseline LDL-C).

---

### 6. Protocol for constructing multi-ancestry polygenic models using S4-Multi

**Authors.** PH Lai, JP Tyrer, J Baierl, PDP Pharoah, PC Peng.
**Venue.** *STAR Protocols*, 2026 (S2666-1667(26)00334-5).
**Signal source.** Google Scholar author-feed — Joshua C. Denny
(07-24 09:02Z; sole hit in the batch).
**Bucket.** HIGH (protocol utility).
**Threads served.** Genetic epidemiology (cross- / trans-ancestry
PGS); biobanks with EHR linkage (PGS in AoU / MVP requires
multi-ancestry methods).

**What the paper does (from snippet).** Reproducible step-by-step
STAR-Protocols paper for constructing multi-ancestry PGS with
**S4-Multi**. Covers reference-genotype preparation, GWAS
summary-statistic formatting, and end-to-end PGS generation.
Pharoah + Peng are the ovarian-cancer genetics group at
Cambridge / Cedars-Sinai — this is likely a spinout from their
multi-ancestry ovarian-cancer PGS work.

**Why it matters for your work.**
1. **Reproducible multi-ancestry PGS recipe.** STAR Protocols is
   the "recipe" journal — the paper is a de facto tutorial.
   Directly useful whenever you need to build PGS for AoU's
   ~50% non-European participants. Pairs with your existing
   PRS-CSx / PRS-CS / LDpred2-auto toolchain.
2. **Denny-feed placement suggests biobank / AoU relevance.**
   Denny's author feed is heavily biased toward AoU / biobank
   application papers; this surfacing implies S4-Multi is being
   thought of as an AoU-appropriate multi-ancestry PGS method.
   Worth cross-checking against the last AoU PGS methods survey.
3. **Ovarian-cancer origin — natural bridge to hereditary-cancer
   work.** Pharoah's ovarian-cancer PGS + BRCA1/2 carrier
   penetrance work is the natural test case; S4-Multi could
   plausibly be re-run for breast-cancer PGS × BRCA1/2 carrier
   modifier analyses in AoU — direct fit with your published
   BRCA / hereditary-cancer research.

**Follow-ups.** Pull the protocol; check (a) input formats
required (PLINK? BGEN? VCF?), (b) reference-panel dependencies
(1000G? UKB? AoU?), (c) compute / memory profile, (d) whether
the protocol releases pre-computed weights for common cancer
phenotypes.

---

### 7. A framework for human-artificial intelligence co-learning for disease activity labeling using electronic health records

**Authors.** Z Yang, Y Zhang, Z Love, A Animashaun, K Zhong et al.
**Venue.** medRxiv, 2026-07-16 (2026.07.16.26358271).
**Signal source.** Google Scholar author-feed — Patrick Ryan (07-26
05:17Z; position 5).
**Bucket.** METHODS-WATCH-HIGH.
**Threads served.** EHR phenotyping (LLM-assisted phenotype
development); ML for precision health; adjacent to EHR foundation
models.

**What the paper does (from snippet).** Introduces **SHARE
(Synergistic Human-Agent REasoning system)** — a framework for
human-AI interaction where the AI proposes phenotype labels and a
human expert corrects them iteratively, with the correction signal
feeding back into the model. The framing is "scalable phenotyping
of complex outcomes accurately, robustly and…" — i.e. explicitly
targeted at outcome definitions that are complex enough to require
LLM assistance but where fully automated labeling is not trusted.

**Why it matters for your work.**
1. **Complements the Wang binary-silver-labels paper (report #1).**
   Where Wang gives a *statistical* framework for learning from
   noisy silver labels, SHARE gives a *human-in-the-loop* framework
   for progressively refining them. Together they cover the two
   ends of the "how do we get high-quality phenotype labels at
   scale" problem.
2. **Directly relevant to your Trikafta / CFTR-modulator eligibility
   phenotype work.** CFTR-modulator eligibility depends on complex
   composite outcomes (rescue-medication use, pulmonary exacerbation
   frequency, spirometry-derived FEV1 trajectory) — a natural
   candidate for human-AI co-labeling rather than pure rule-based
   or pure LLM extraction.

**Follow-ups.** Pull the paper; check (a) which LLM backbone was
used (GPT-4 / Claude / open-weights?), (b) how the human-correction
feedback loop was implemented (fine-tuning? active learning? RLHF-
style?), (c) which disease-activity outcomes were validated, (d)
whether the paper reports a labeling-throughput comparison against
pure-manual chart review.

---

### 8. Temporal trends in epidemiology and patient characteristics of 36 cancers: a protocol for a multinational population-based cohort study using OMOP-standardised databases (CANcer_20 protocol)

**Authors.** I López-Sánchez, A Palomar-Cros, A Giuliodori et al.
**Venue.** *BMJ Open*, 2026 (bmjopen 16:e119069).
**Signal source.** Google Scholar author-feed — Patrick Ryan (07-26
05:17Z; position 7).
**Bucket.** HIGH (reference utility).
**Threads served.** EHR phenotyping & OMOP; cancer epidemiology
(natural bridge to Chenjie's cancer-epi background); pharmacoepi
(multinational OMOP infrastructure).

**What the paper does (from snippet).** Multinational OMOP-CDM
cohort-study protocol characterizing incidence, prevalence, and
patient characteristics across 36 cancers. Explicitly frames OMOP-CDM
as a complement to registry data for cancer surveillance.

**Why it matters for your work.**
1. **Reference protocol for OMOP-based cancer epi.** BMJ Open's
   protocol format is designed to be cited by later analytic papers
   — this is the "how would we do multi-country cancer epi in OMOP"
   canonical reference. Directly useful whenever your cancer-epi
   background intersects with the OMOP thread.
2. **Multinational OMOP is Prieto-Alhambra / Oxford lineage.** The
   Barcelona / IDIAP-JGol author list places this in the
   Prieto-Alhambra Oxford OMOP-cancer research pipeline. Worth
   reading the data-sources appendix for the reference network of
   OMOP-CDM cancer databases outside AoU.
3. **36 cancers is a broad net.** Includes the common cancers your
   own publications cover (breast, colorectal) plus rarer ones — a
   convenient reference for "which OMOP databases carry which
   cancer phenotypes at usable N."

**Follow-ups.** Pull the paper; check (a) which OMOP databases
participate (CPRD? IMASIS? SIDIAP?), (b) cancer phenotype
definitions (SNOMED concept sets), (c) whether AoU is in the
participating network, (d) planned analytic outputs and expected
completion dates.

---

### 9. Simulation of synthetic health records for assessment of causal inference methods for vaccine efficacy

**Authors.** V Velasco Pardo, L Daines, SV Katikireddi, L Ritchie et al.
**Venue.** medRxiv, 2026-07-17 (2026.07.17.26358308).
**Signal source.** Google Scholar author-feed — Patrick Ryan (07-26
05:17Z; position 3).
**Bucket.** METHODS-WATCH.
**Threads served.** Causal inference / pharmacoepi (synthetic-EHR
benchmarking of causal methods); EHR phenotyping (synthetic-EHR
generation is a phenotype-simulation task).

**What the paper does (from snippet).** Simulates synthetic EHRs
under known causal structure to benchmark causal-inference methods
(likely IPW, g-methods, TMLE) for vaccine effectiveness estimation.
Motivated by the COVID-era near-real-time vaccine effectiveness
work where standard observational methods gave conflicting answers.

**Why it matters for your work.**
1. **Synthetic-EHR benchmarks are the "true-answer" test bed for
   causal-ML methods.** Anytime you propose a new TTE / IPW /
   causal-forest workflow on AoU, you need a benchmark where you
   know the true causal effect. Synthetic-EHR generation with
   known ground truth is that benchmark.
2. **Katikireddi coauthorship = strong causal-epi provenance.**
   Srinivasa Vittal Katikireddi (Glasgow) is a heavyweight in
   causal-epi methods for COVID; this places the paper in a
   credible methodological lineage.

**Follow-ups.** Pull the paper; check (a) which simulation
framework (Synthea? bespoke?), (b) which causal methods were
benchmarked, (c) whether the code is publicly available, (d)
whether the framework supports non-vaccine exposures (would extend
to drug-effect TTEs).

---

### 10. `arxiv-digest` 2026-07-24 — Auditing pretraining contamination in single-cell foundation model benchmarks (scContam)

**Authors.** Sarwan Ali (q-bio.GN).
**Signal.** `arxiv-digest` today (only new paper across the 3-day
window; keyword `foundation model`, score 1). arXiv 2607.20572v1,
submitted 2026-07-21.
**Bucket.** METHODS-WATCH.

**Take.** Contamination audit for **single-cell foundation models
(scFMs)** — Geneformer, scGPT, UCE. Introduces `scContam`, a per-cell
audit combining MinHash-based gene-set fingerprints against the
explicit pretraining corpus with a loss-based membership inference
attack (MIA-scFM). Findings: PBMC 3k and CELLxGENE pancreatic islet
atlas — two of the most-cited scIB benchmark datasets — have
extensive pretraining overlap ($80.4\%$ and $77.0\%$ of cells with
fingerprint $p < 0.05$ against Genecorpus-30M), while post-cutoff
datasets AIDA v2 and Tahoe-100M show 0% overlap. A controlled
re-pretraining experiment shows MIA-scFM AUROC scales monotonically
with the model's capacity-to-data ratio ($0.494 → 0.690 → 0.881$
across properly-regularized, mildly-overfit, and aggressively-overfit
regimes), indicating that production scFMs *don't* instance-memorize
individual cells but distributional contamination is real and must
be audited separately. Donor-matched within-cell-type analysis shows
contaminated cells embed measurably tighter than clean cells
(permutation $p = 0.030, 0.014, < 0.002$).

**Why it matters for your work.** Off the primary EHR / clinical
thread but a direct methodological template for auditing **EHR
foundation models** (CLMBR / MOTOR / MEDS / EHRSHOT) for
distributional contamination — the same benchmark-leakage concern
applies at least as strongly to EHR-FMs. Portable design: run
gene-set fingerprints ↔ EHR concept-set fingerprints; run
loss-based MIA on held-out patient trajectories; check whether
benchmark-vs-clean patients cluster tighter in embedding space.
The composition-matched negative control from the same author's
prior work (already flagged 07-23) is the sibling protocol.
**METHODS-WATCH** — port this to your CLMBR / MOTOR audit toolkit.

---

### 11. DPCGS: a computational framework for linking GWAS to single-cell transcriptomics in complex traits and diseases

**Authors.** C Liu, B Shen, J Li, R Zhu, P Yang, B Wu, Y Xuan et al.
**Venue.** bioRxiv, 2026-07-14 (surfaced 07-26; 2026.07.14.738331).
**Signal source.** Google Scholar author-feed — Jian Yang (07-26
05:17Z; position 0).
**Bucket.** METHODS-WATCH.
**Threads served.** Genetic epidemiology (GWAS + single-cell
integration); TWAS-adjacent (cell-type-specific expression links).

**What the paper does (from snippet).** Framework for connecting
GWAS signal to cell-type-specific expression in single-cell
transcriptomics data — the "which cell type carries the GWAS
signal" question. Sits in the sc-DRS / MAGMA-scDRS / SCDRS family
but with a computational-framework framing rather than a
disease-specific application.

**Why it matters for your work.** Off the primary EHR / clinical
thread but methodologically parallel to TWAS-in-tissue work that
comes up in the hereditary-cancer background. Worth reading only
if you're planning a single-cell-informed re-analysis of an
existing GWAS in your reference class (BRCA-region signals,
CFTR-modifier signals, APOL1-tissue signals). **METHODS-WATCH.**

---

### 12. Citation-Aware Continual Pre-Training for Biomedical Language Models

**Authors.** M Asada, T Tsujimura, T Ishigaki, S Egami, K Fukuda et al.
**Venue.** *BioNLP 2026* (ACL Anthology 2026.bionlp-1.32).
**Signal source.** Google Scholar author-feed — Peter Szolovits
(07-26 05:17Z; position 0).
**Bucket.** METHODS-WATCH.
**Threads served.** Knowledge graphs & ontologies (citation graphs
as structured knowledge); adjacent to EHR foundation models
(continual pre-training is portable to EHR LMs).

**What the paper does (from snippet).** Continual-pretraining
recipe for biomedical LMs that explicitly uses **citation links** —
i.e. the structured knowledge encoded by paper-to-paper citation
edges — as part of the training signal. Standard LM pretraining
throws this signal away.

**Why it matters for your work.** Natural companion to PrimeKG-Plus
(report #2): citation edges are the same class of literature-derived
structured knowledge that PrimeKG-Plus is now incorporating. If you
end up thinking about literature-KG-augmented drug-repurposing
pipelines, this paper is the LM-side complement. Off the primary
clinical thread but on the KG thread. **METHODS-WATCH.**

---

## METHODS-WATCH (short entries)

### Sex-specific SGLT2i genital infection risk factors — Therapeutic Advances
**Authors.** A Kajiwara-Morita, S Kugimoto, K Oniki, A Yoshida et al.
(Therapeutic Advances in Drug Safety 2026; Ryan feed, 07-26).
**Take.** SGLT2i pharmacovigilance for genital infections in T2D —
retrospective cohort + JADER (Japan) disproportionality analysis.
On the SGLT2i drug thread but the outcome (genital infection) is
routine pharmacovigilance rather than novel pharmacoepi.
**METHODS-WATCH.**

### Challenges implementing ADA guidelines in EHRs — JAMIA Open
**Authors.** I Demarie, ME Bowen, S Agarwal, C Mai, K Marble et al.
(JAMIA Open 2026; Ryan feed, 07-26).
**Take.** Implementation-science paper on translating ADA Standards
of Care into EHR-executable form. Ryan-feed placement implies OMOP
relevance. On the EHR-implementation thread but not on your primary
research threads. **METHODS-WATCH.**

### Oral semaglutide CV benefits + BMI/HbA1c mediators — J Clin Endocrinol Metab
**Authors.** SE Inzucchi, R Abdul Ghani, J Deanfield, S Emerson et al.
(J Clin Endocrinol Metab 2026; Ryan feed, 07-26).
**Take.** SOUL trial secondary analysis — whether baseline / change
in HbA1c or BMI modifies the 14% MACE reduction from oral
semaglutide. On the GLP-1 RA drug thread and adjacent to your
causal-mediation interests, but this is a trial secondary analysis,
not real-world evidence. **METHODS-WATCH.**

### GenoSiS — biobank-scale genotype similarity search — Genome Research
**Authors.** K Schneider, M Chowdhury, M Tepper, JB Khan et al.
(Genome Research 2026; Bastarache feed, 07-24).
**Take.** Vector-search-based cohort creation from genotype
embeddings — Intel SVS library for fast retrieval. Directly useful
if you need to construct patient-matched control cohorts from AoU
WGS at speed. **METHODS-WATCH** — worth bookmarking as an
infrastructure primitive.

### Wang whole-genome long-read variant detection review — Genome Research
**Authors.** K Wang, CJ Aex, H Lee (Genome Research 2026; Karczewski
feed, 07-24).
**Take.** Long-read WGS variant-calling landscape. Adjacent to
variant-interpretation thread; useful reference when long-read
data become available at biobank scale (AoU long-read subset is
in progress). **METHODS-WATCH.**

### EHR audit-log language modeling — medRxiv
**Authors.** S Kim, SS Lou, A Cobb, S Jha, TG Kannampallil (medRxiv
2026.06.24; Szolovits feed, 07-26).
**Take.** Applies LM sequence modeling to EHR audit-log data
(clinician-EHR interaction patterns). Novel data type — audit logs
capture *how* clinicians use the EHR, not just what data they see.
Portable to burnout / workload / clinical-decision-support
research. **METHODS-WATCH.**

### Multi-ancestry colocalization approaches — PLoS Genetics
**Authors.** C Shen, J Dupuis, Q Zhang (PLoS Genetics 2026; Yang
feed, 07-26). **Take.** Cross-ancestry colocalization for
fine-mapping — natural complement to the S4-Multi PGS protocol
(report #6). **METHODS-WATCH.**

### Adaptive-penalized bootstrap-smoothed two-sample MR — arXiv
**Authors.** M Qasim, K Wang, IS Bhatt (arXiv 2607.18503; Yang
feed, 07-26). **Take.** Follow-up MR methods paper from the same
author cluster as the MR-ALasso paper flagged in 07-22.
Complements the drug-target-MR (Saxby, 07-23 report) design
pattern. **METHODS-WATCH.**

### Ancestry-calibrated PTSD PGS × neighborhood interaction — medRxiv
**Authors.** EK Webb, A Jajoo, V Balakundi, MSE Sendi et al.
(medRxiv 2026.07.17.26358149; Yang feed, 07-26). **Take.**
PGS-x-environment interaction with ancestry calibration — an
example of the PRS-portability + G×E design pattern. On the
genetic-epi thread but off the primary clinical threads.
**METHODS-WATCH.**

### Chambers HIV-vaccine uptake, Ontario cohort — AIDS and Behavior
**Authors.** C Chambers, T Bekele, R Grewal, C Kovacs et al. (AIDS
and Behavior 2026; Ryan feed, 07-26). **Take.** Vaccine-uptake
descriptive epi in a linked cohort. Off-thread; noted only to
document that the Ryan feed carries substantial vaccine / infection
pharmacoepi that isn't on your active thread list.
**SKIP / METHODS-WATCH.**

### Zheng multi-ancestry multi-trait psychiatric × Alzheimer — Translational Psychiatry
**Authors.** X Zheng, H Feng, L Ren, Y Zhang (Transl Psychiatry
2026; Yang feed, 07-26). **Take.** Multi-trait GWAS shared-genetics
scan across MPDs + AD. On the genetic-epi thread but a
disease-crossover analysis rather than a methods paper.
**METHODS-WATCH.**

### Dai crystalloid TTE — iScience
**Authors.** Q Dai, Y Hao, J Shen, X Ren, C Jin (iScience 2026;
Ryan feed, 07-24). **Take.** Balanced crystalloid vs. saline TTE
in MIMIC — the interesting methodological point is that
"satisfying standard TTE diagnostics is not sufficient" — exposure-
definition sensitivity reveals hidden confounding. Direct
methods-warning for anyone (including you) building TTEs on ICU or
critical-care data. **METHODS-WATCH-HIGH.**

---

## Off-thread / SKIP (representative entries — not exhaustive)

- Zitnik / Szolovits / Callahan / Yang **diffusion-language-model
  and CLM feeds** — Karnysheva chemical LM probing, dOPSD diffusion
  LM, Van Puyvelde radiology diffusion, Yoo flow-map LM,
  Chaturvedi hybrid block diffusion, Gurnee verbalizable
  representations, Ramanaik adversarial VLM spectral analysis,
  Zhang SLoRA, Zaghouani Arabic LLM safety. All routine LLM /
  arch feeds triggered by the broad "language model" interest of
  the followed authors; none on your clinical / EHR threads.
- **Animal-genomics feeds** — Masuko goat diversity, Zhang pig
  eQTL, Boehnke Finnish METSIM amino-acid GWAS (edge case — on-thread
  for metabolomics but off primary), Wu functionally-informed
  fine-mapping in livestock. Triggered by shared UKB / gnomAD
  reference infrastructure.
- **IVF / PGT** — Gumusoglu-Acar preimplantation cfDNA (Karczewski
  feed). Off-thread.
- **Fabry iPSC line** — Borisch et al. (Stem Cell Research;
  Bastarache feed). Off-thread; noted because Bastarache-feed
  Fabry papers occasionally cross into penetrance / rare-disease
  work.
- **Merkle hESC whole-genome analysis** — off-thread reference
  paper from an older Karczewski citation.
- **Tischkowitz MR of menopause / menarche in BRCA1/2 carriers**
  (Karczewski feed). Directly overlaps Chenjie's breast-cancer
  background but off the current active thread list (which is
  methods-heavy rather than clinical-oncology). Noted for possible
  future reactivation of a BRCA-modifier thread.
- **van der Velden CAPRI-3 PSMA imaging** (Chenjie Zeng feed,
  07-24). Prostate-cancer real-world imaging registry — clinical
  oncology, off methods threads.
- **Gu Fabry patient-derived iPSC**, **Gupta editorial on
  penetrance-of-monogenic-disorders** (Bastarache feed, 07-24) —
  short editorial referencing MyCode / Geisinger; on-thread topic
  but not primary literature.

---

## Housekeeping — arxiv-digest health

- `digests/2026-07-24.md` — 1 paper (scContam), 3 previously seen
  suppressed. Working as designed.
- `digests/2026-07-25.md` — 0 papers, 1 suppressed. Empty is fine
  for a quiet weekend.
- `digests/2026-07-26.md` — 0 papers, 0 suppressed. Empty.

Three consecutive daily digests with 0–1 papers is expected for
weekend / mid-summer arXiv volume in these categories, not evidence
of pipeline breakage. The tracked keywords in `config/tracked.yaml`
continue to have wide recall — the low count reflects a genuinely
quiet arXiv window in q-bio.QM / GN / PE / stat.AP for topics on
your interests list.

---

*Prepared 2026-07-26; next report expected once new signal
accumulates (typically 1–2 days). Full arxiv-digest for today is at
`digests/2026-07-26.md` (0 papers). Previous report at
`reports/2026-07-23-research-digest.md`.*
