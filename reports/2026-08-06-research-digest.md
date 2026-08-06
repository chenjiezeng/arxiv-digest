# Research digest report — 2026-08-06

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-08-02 12:30Z → 2026-08-06 12:40Z** (~4 days since
`reports/2026-08-02-research-digest.md`). Short catch-up; expect a lean
HIGH list. Author-feed batch fired on 08-04 (10 feeds simultaneously),
which is the densest cluster in the window.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-04.md` → `2026-08-06.md`) | 08-04 → 08-06 (~04:50Z crons) | 3 daily runs, all non-empty. Papers: 6 (08-04) + 5 (08-05, 4 previously surfaced suppressed) + 3 (08-06, 7 previously surfaced suppressed). Highest-scoring hit: **Ciardulli et al. functional propensity score (UKB BMI × T2D)** at score 4 in the 08-05 run. |
| Google Scholar alerts (keyword feeds) | 08-03, 08-05 batches | Two full ~11-feed batches this window. 08-03 (10:51Z) and 08-05 (05:27Z) fired all keyword feeds together (`APOL1`, `all-of-us-research-program`, `clonal hematopoiesis`, `drug repurposing`, `electronic health records`, `foundation models + EHR`, `knowledge graph`, `mendelian diseases`, `rare diseases`, `UK Biobank`, `variant interpretation/classification`, plus `autoimmune`). |
| Google Scholar alerts (author feeds) | 08-04 21:30Z batch | Dense batch: Denny (author + related), Kanai (author), Bastarache (related), Karczewski (related), Gusev (author), Hripcsak (related), Kai Wang (related), Konrad Karczewski (citations), Lu (author), Motsinger-Reif via "citations to Chenjie Zeng". |
| NCBI "My NCBI What's New" — AoU / UKB / drug repurposing | 08-02, 08-03, 08-04, 08-05, 08-06 | Five daily batches per topic (15 emails total in-window). AoU volumes small (1–3/day, ordinary); UKB batches moderate (2–4/day this window); drug repurposing steady. Densest hits: 08-06 AoU (SCOPE OUD tool) and 08-06 UKB (four CVD/HF association pieces). |
| bioRxiv / medRxiv Subject Collection Alerts | daily (08-02 → 08-06) | Aggregate feeds; the 08-05 medRxiv batch and the 08-06 bioRxiv batch showed the most on-thread items (frailty index integrity + polygenic-index UK validation). Same caveat as before: metadata-only. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated to first
> 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Eight HIGH items surfaced this window. They cluster into four knots:

**Composite-risk + Denny-lineage AoU (2 items).** Motsinger-Reif / Lloyd /
Akhtari / House / Patel / … / Denny — *Polyexposure, Polysocial, and
Polygenic Scores for Common, Complex Disease Classification* (Res Sq
2026). NEW paper this window from the Denny + Motsinger-Reif + Chirag
Patel (Harvard, exposome) lineage that formalizes the polyexposure ×
polysocial × polygenic tri-score for disease classification. This is
the composite-risk-model paper your INTERESTS.md `Composite risk models
stacking PRS with rare pathogenic variants` sub-thread has been
signaling — this one stacks the *exposome/socialome* rather than rare
variants but is the same conceptual move. Motsinger-Reif / Ahn / House
… Denny AoU HLA trans-ancestry (07-30 report #2) also re-surfaced this
window via the "2 new citations to Chenjie Zeng" feed as a continuity
signal — no new content, still relevant.

**Multi-ancestry / cross-context GWAS (2 items).** Bujnis et al.
*Nature Genetics* multi-ancestry Hashimoto's thyroiditis GWAS — the
formal *Nat Genet* publication (previously surfaced as pre-print in
08-02 report #3, now published). Liu, Zheng, Gu et al. *Nat Genet*
GWAS of 111 gestational phenotypes in up to 121,579 Chinese
participants — Kanai co-authored; **first-in-class large East Asian
biobank gestational-phenotype scan** with explicit "context-specific
genetic effects" framing (i.e., pregnancy-context × constitutional
genetics interaction). Together these two Kanai-associated *Nat Genet*
papers this window are the multi-ancestry-cross-context-GWAS pattern
your INTERESTS.md thread prioritizes.

**Causal-inference infrastructure for EHR / biobank (3 items).**
Ciardulli / Fontana / Vantini / Ieva — *functional propensity score
weighting* (arXiv 2608.03200, score 4 in the pipeline) with UKB BMI
trajectory → T2D + HbA1c application. This is the highest-scoring
arxiv-digest hit of the window and directly on the
functional-covariate / longitudinal-EHR gap in TTE design. Foulkes /
Thaweethai / Scharfstein / Huang / Reeder — *IPW for auxiliary
variable dependent sampling* (arXiv 2608.04918) motivated by RECOVER
Adult and Pediatric Long-COVID cohorts. Selective-testing-based
two-phase designs are ubiquitous in EHR — this is the methods paper
that formalizes handling them. Noma — *Target Trial Emulation with R
Package TTE* (arXiv 2608.01625) — a tutorial + methodological guide
with SGLT2i-vs-DPP-4i and ARB-vs-CCB worked examples. Direct
infrastructure paper for the pharmacoepi thread; the R package matters
for turnkey TTE.

**Drug-target MR × oncology (1 item).** Bate, Dong, Liu, Seviiri,
Brown, Atkins et al. (Gusev group) — *Immune checkpoint inhibition MR
for cancer repurposing*. Drug-target MR triangulated for an oncology
repurposing question is exactly the design pattern your INTERESTS.md
`Drug-target Mendelian randomisation triangulated with observational
cohort estimates` sub-thread names — this one extends the pattern
(previously flagged for statin × CHIP in 08-02 #12 and metformin × AAA
in 07-23) to ICI × cancer.

**Bonus: LLM-benchmark infrastructure at scale.** Zhiyong Lu group's
Wang et al. *npj Digital Medicine* — *Benchmarking and developing LLMs
using one million clinical trials*. A million-trial-derived benchmark
for clinical LLMs is a substrate that will show up in downstream
evaluation of any clinical-LLM you consider adopting.

METHODS-WATCH bench includes Sasson/LeCun/Segal DXA self-supervised
(UKB validation, LeCun as senior author), Krol et al. correlated
frailty for family rare-variant survival, Xu/Tchetgen Tchetgen proximal
trial reconciliation, Zhao et al. proximal confounders covariate
selection, Emfietzoglou et al. statin × AMD TTE (Hernán citation
network), Zhang X CHIP CVD gene-specific mechanisms review, plus the
depressive-phenotyping and UKB-DXA-body-composition items.

---

## HIGH — full write-ups

### 1. Motsinger-Reif, Lloyd, Akhtari, House, Patel, House, … Denny, *Polyexposure, Polysocial, and Polygenic Scores for Common, Complex Disease Classification and the Creation of a Clinical Exposure Assessment* — **Research Square 2026** (rs-10284839)

**Feed:** Google Scholar author feed for Joshua C. Denny — "new
articles" batch (08-04 19:46Z).

**Why HIGH.** New paper this window in the Denny + Motsinger-Reif +
Chirag Patel (Harvard exposome) axis. Three threads converge here:
1. **Genetic epi — composite risk models** — your INTERESTS.md
   `Composite risk models stacking PRS with rare pathogenic variants`
   sub-thread explicitly asks for architectures that fuse polygenic
   with orthogonal risk axes. This paper formalizes a *tri-score*
   (polygenic × polysocial × polyexposure) design that generalizes the
   PRS-tails-and-residuals taxonomy your thread already tracks
   (Baya AJHG, Souaiaia Nature, Vazquez Genetics). This is the
   exposome-and-social-determinants generalization of the same idea.
2. **EHR phenotyping / knowledge representation in EHRs** — the
   "Clinical Exposure Assessment" side is essentially an
   EHR-derived-exposome representation-choice paper. Fits directly in
   the new `Knowledge representation in EHRs and applications`
   sub-thread on concept normalization + representation-choice-drives-
   downstream-performance.
3. **PheWAS / phecode infrastructure** — the disease-classification
   framing at "common, complex disease" scale is a PheWAS-adjacent
   design (phecodes as outcomes, tri-score as exposure).

**Actionable question.** Read the methods for:
- **Where the polysocial score comes from** — self-reported survey?
  EHR-derived social-determinants (SDOH) codes? Area-level ADI /
  deprivation? Each choice has different portability.
- **What "polyexposure" means operationally** — chemical/environmental
  exposures from an air-quality overlay (Patel's line of work),
  medication-exposure PRS (rare), or lifestyle-derived score?
- **The classifier architecture** — is this a linear tri-score sum, a
  learned interaction model, or a stacked classifier? Interaction
  terms are the crux — if PGS × exposure interactions are pervasive
  (per Nagpal & Gibson *Nat Genet* 2026, in your `Genetic epi`
  sub-thread), a linear-sum tri-score is misspecified.
- **AoU as the base cohort** — likely, given the Motsinger-Reif +
  Denny lineage and the polysocial angle. Confirm.
- **Validation cohort** — does it validate cross-biobank (UKB / MVP /
  BioVU)? Portability of a polysocial score across health systems is
  where this design either wins or breaks.

**Where it links to your work.** Direct reference for the
composite-risk / PGS-tails-and-residuals thread and the
knowledge-representation-in-EHRs thread. Candidate addition to the
`zeng-publications` skill and to the `ehr-phenotyping-os` skill as an
exemplar of exposome × EHR × genetics stacking. Also a natural
citation for any PheWAS-monogenic paper you spin up when framing
"PGS is one of several risk axes."

---

### 2. Bujnis, Sterenborg, Li, Åsvold, Brčić, Boraska Perica, Babbar, Denny, Fritsche, Kanai et al., *Multi-ancestry genome-wide association analyses provide insights into the genetic basis of Hashimoto's thyroiditis* — **Nature Genetics 2026** (s41588-026-02704-w)

**Feed:** Google Scholar author feed for Masahiro Kanai — "new
articles" (08-04 19:46Z). Previously surfaced as the pre-print form in
08-02 report #3 via NCBI 07-30 batch; **now formally published in
*Nat Genet***.

**Why HIGH.** Formal *Nat Genet* publication of the paper flagged as
HIGH in 08-02. Confirmed abstract: 48,694 Hashimoto's cases in
multi-ancestry meta-analysis. All the design-reference reasons from
the 08-02 write-up hold — Denny + Kanai + Fritsche is the canonical
Denny-lineage multi-biobank multi-ancestry GWAS lineup. Two threads
served:
- **Genetic epi (multi-ancestry GWAS)** — direct reference-
  implementation.
- **Autoimmune / IBD-adjacent** — Hashimoto's is autoimmune
  thyroiditis; shares HLA architecture with the broader autoimmune
  spectrum you track. Notably, this pairs with the Motsinger-Reif /
  Ahn / House HLA trans-ancestry AoU paper (08-02 report #2) as
  companion work on the HLA-mediated autoimmunity landscape.

**Actionable question.** Read the *Nat Genet* version for:
- **Exact cohort composition** — the abstract's "precise …" is cut
  off in the snippet; the paper likely uses a case definition audit
  (which biobanks contribute cases, phecode 244.4 vs. narrower).
- **Cross-ancestry loci vs. ancestry-specific** — the abstract's
  "context-specific" framing (also in the companion Liu et al. paper,
  #3 below) suggests they call out effect-size heterogeneity by
  ancestry at specific loci.
- **Drug-target follow-on** — autoimmune GWAS hits are the
  drug-target-actionable end of GWAS; check for MR / drug-target
  callouts (JAK, IL-2, IL-17).

**Where it links to your work.** Same as 08-02 write-up — design
reference for any Denny-lineage cross-biobank GWAS you might spin up
(hereditary cancer PheWAS, CFTR carrier phenotypes, APOL1 carrier
phenotypes). Update to the "reference implementation" citation now
that the *Nat Genet* version is out.

---

### 3. Liu, Zheng, Gu, Yang, Zhen, Wei, Liu et al., *Genome-wide association analyses of gestational phenotypes identify context-specific genetic effects* — **Nature Genetics 2026** (s41588-026-02677-w)

**Feed:** Google Scholar author feed for Masahiro Kanai — "new
articles" (08-04 19:46Z, paired with the Bujnis paper above).

**Why HIGH.** Two *Nat Genet* papers in the same Kanai author-feed
batch is unusual, and this one is on a distinct axis: 111 gestational
phenotypes in up to 121,579 Chinese biobank participants. Three
threads:
- **Biobanks with EHR linkage (multi-ancestry, non-EUR biobank
  emphasis)** — this is an East Asian biobank scan at the *Nat
  Genet* level, of the same design lineage as UKB / AoU-based scans
  but on an under-represented ancestry. Multi-ancestry portability
  arguments benefit from EAS-specific priors.
- **Genetic epi (context-specific / GxE)** — the abstract's
  "context-specific genetic effects" is precisely the
  `GxE and PGS × exposure / environment interactions` sub-thread's
  vocabulary. Pregnancy is a distinctive physiological context;
  gestational-phenotype × constitutional-genetic interactions could
  reframe hereditary-cancer or hypertension PGS studies.
- **PheWAS / phecode infrastructure (adjacent, but different scale)** —
  111 phenotypes is PheWAS-adjacent but at pregnancy-specific
  resolution rather than the full phecode tree.

**Actionable question.** Read for:
- **Which Chinese biobank** — China Kadoorie? CMEC? Some newer
  hospital-network-linked cohort? Determines what data-access lift is
  possible if you'd ever want to replicate.
- **Which 111 phenotypes** — obstetric outcomes (preeclampsia,
  gestational diabetes, preterm birth), pregnancy-specific labs
  (HbA1c-in-pregnancy), or maternal late-life outcomes tied back to
  pregnancy events?
- **"Context-specific" mechanism** — is it that some loci have
  pregnancy-specific effects (only appear in the maternal-during-
  pregnancy state) or that pregnancy modifies effect sizes at loci
  also active outside pregnancy? Very different biology.
- **Cross-ancestry follow-on** — do they compare to UKB / FinnGen /
  BioBank Japan for the same phenotypes where possible?

**Where it links to your work.** Design reference for any
context-specific-GxE genetic-epi scan (immediate parallels: cancer
treatment × germline, statin exposure × CHIP genotype, HRT × BC
susceptibility loci). Add to `broad-genomics` skill's cross-ancestry
GWAS section, and reference in any hereditary-cancer × context work
you plan.

---

### 4. Ciardulli, Fontana, Vantini, Ieva, *Generalized propensity score weighting for functional causal inference framework* — **arXiv:2608.03200v1 (2026-08-04; digest 08-05)**

**arxiv-digest hit:** score 4 (`uk biobank`, `biobank`, `propensity
score`, `causal inference`) — the highest-scoring hit of the window.

**Why HIGH.** Directly on two threads:
- **Causal inference / pharmacoepi (functional exposure)** — extends
  propensity-score weighting from scalar to *functional* exposures
  (trajectories rather than point exposures). The formulation
  (dual/unconstrained smooth optimization) is a computational win at
  UKB scale, not just a theoretical extension.
- **UKB / biobank cohorts** — the applied example is UKB BMI
  trajectories → T2D risk and subsequent HbA1c trajectories. Two
  time-varying phenotypes both treated functionally, with
  covariate-balance diagnostics adapted to the functional setting.

The paper reports both a covariate-balance improvement and a
computational scalability claim over the sequential-line-search
predecessor — a paper that publishes both a statistical improvement
and a scale-up story is high-signal for methods you'd actually reach
for.

**Actionable question.** Read the methods for:
- **The functional weight formulation** — is it a truncation-in-
  functional-space (like a spline-basis PS) or does it stay
  non-parametric? Determines when the smoothness assumption bites.
- **The trajectory censoring / missingness treatment** — UKB BMI
  trajectories are sparse (visits 5–10 years apart); how do they
  handle irregular observation grids?
- **Balance diagnostics** — for a functional exposure "balance" is
  distribution-of-trajectories × covariates; what's the metric?
- **Comparison to the scalar-BMI baseline** (Wainberg 2019 cited) —
  what's the effect-size or standard-error uplift for using the full
  trajectory vs. a single baseline BMI?
- **Portability to a phecode outcome** — the T2D outcome uses a
  scalar time-to-event; can the same framework take a functional
  outcome (HbA1c trajectory) as the endpoint, and if so how do they
  parameterize the target-trial estimand?

**Where it links to your work.** Direct methods candidate for any
AoU / UKB TTE where the exposure is a trajectory (BMI, HbA1c, SBP,
eGFR) rather than a treatment-at-baseline. Add to the
`causal-inference-os` skill's estimator inventory alongside DR-FRL
(from 08-02 report Bonus HIGH). DR-FRL + this paper together cover
"functional exposure" (this one) and "functional history"
(DR-FRL) — you probably want both as tools.

---

### 5. Foulkes, Thaweethai, Scharfstein, Huang, Reeder, *Inverse probability weighting for auxiliary variable dependent sampling in observational studies of Long COVID* — **arXiv:2608.04918v1 (2026-08-05; digest 08-06)**

**arxiv-digest hit:** score 1 (`inverse probability`).

**Why HIGH.** The scoring is low (single keyword hit) but the
substance is directly on-thread: this is *the* methods paper for
two-phase / auxiliary-variable-dependent sampling in observational
EHR studies, motivated by RECOVER (Researching COVID to Enhance
Recovery), which is a paradigmatic AoU-adjacent longitudinal EHR
cohort. Three threads:
- **Causal inference / EHR phenotyping** — the paper explicitly
  frames this as "ubiquitous in electronic health record data." Any
  AoU / UKB / MVP substudy that samples selectively based on
  intermediate variables (e.g., who gets a follow-up lab drawn, who
  gets a genomic subassay, who gets a Fitbit sub-cohort) is exactly
  this design. Ignoring the sampling mechanism is the standard
  pitfall.
- **Pharmacoepi / TTE** — target-trial-emulation studies with
  differential-sampling on treatment or outcome ascertainment share
  the same bias structure. This is a portable IPW correction.
- **Long-COVID as adjacent disease context** — RECOVER Adult and
  Pediatric are the reference cohorts; Scharfstein (JHU) is a
  co-author, which flags this as a Rubin-lineage sensitivity-
  analysis-forward paper.

**Actionable question.** Read the paper for:
- **The IPW formulation** — is it a single-stage IPW or a two-stage
  IPW-of-IPW? RECOVER's design has multiple selection stages
  (enrollment, sub-study, biosample) so this matters.
- **Weight-truncation / stabilization** — the trickiest part of
  IPW in the two-phase setting.
- **Sensitivity analyses** — Scharfstein-lineage papers usually
  include a bias sensitivity to unmeasured selection; check for a
  Rosenbaum-style Γ or a tipping-point sensitivity.
- **Software** — did they release an R package? Comparable to Long,
  Wang, Robins two-phase estimator libraries?

**Where it links to your work.** Direct methods reference for any
AoU sub-cohort analysis where the sub-cohort is selected on an
auxiliary variable (Proteomics sub-cohort, Fitbit sub-cohort,
NLP-annotated notes sub-cohort). Add to the
`causal-inference-os` skill's sampling-bias section, and to the
`waxse` skill's AoU-sampling-design references.

---

### 6. Bate, Dong, Liu, Seviiri, Brown, Atkins et al. (Sasha Gusev group), *Investigating the repurposing potential of immune checkpoint inhibition for cancer treatment using Mendelian randomisation* — **preprint 2026**

**Feed:** Google Scholar author feed for Alexander (Sasha) Gusev —
"new articles" (08-04 19:46Z).

**Why HIGH.** Three threads:
- **Drug repurposing (with the clinical-evidence loop your thread
  cares about)** — ICI repurposing across cancer types using genetic
  instruments rather than empirical trial evidence. This is a
  drug-target-MR generalization of drug-repurposing, keeping the
  clinical-actionability angle your INTERESTS.md drug-repurposing
  sub-thread prioritizes.
- **Causal inference / pharmacoepi (drug-target MR triangulation)** —
  same design pattern as the Carter et al. statin × CHIP paper
  (08-02 report #12) and the Saxby et al. metformin × AAA paper
  (07-23 report). This one extends the pattern to oncology.
- **Cancer genetic epi (adjacent to your hereditary-cancer
  background)** — Southey / Gusev-adjacent oncology genetics team;
  the specific cancer types tested will bracket what's cross-
  relevant.

**Actionable question.** Read for:
- **Which PD-1 / PD-L1 / CTLA-4 loci** — the instruments are the
  crux; specifically, cis-eQTL for PDCD1 / CD274 / CTLA4 or SNPs at
  the coding gene? cis-pQTL if a proteomic MR?
- **Which cancer outcomes** — pan-cancer, or a specific set (lung,
  melanoma, RCC where ICIs are frontline)? The prior belief per
  cancer is very different.
- **Comparison to observed-effect literature** — for melanoma and
  NSCLC there's decade of trial data; does the MR estimate line up
  in direction and rough magnitude, or is there a specific cancer
  where MR predicts benefit that trials haven't tested?
- **Reverse causation** — genetic instruments for ICI targets can
  be affected by cancer-state selection; check for
  reverse-causation / Steiger filtering.

**Where it links to your work.** Direct template for the
"drug-target-MR + observational-cohort triangulation" pattern applied
to a cancer-repurposing question. Adjacent to your hereditary-cancer
work — worth reading with a specific eye toward what the ICI-MR
framework would say about hereditary-cancer-carrier populations
(where ICI eligibility differs by mismatch-repair status). Add as a
reference in the `zeng-publications` skill's cancer section and the
`wglab` skill's variant-actionability section.

---

### 7. Noma, *Target Trial Emulation with the R Package TTE: A Tutorial and Methodological Guide* — **arXiv:2608.01625v1 (2026-08-03; digest 08-04)**

**arxiv-digest hit:** score 2 (`target trial emulation`, `inverse
probability`).

**Why HIGH.** Directly on the causal inference / pharmacoepi thread.
Practical infrastructure: a self-contained TTE tutorial for R with
two fully-synthetic worked examples that are exactly the drug-class
comparisons your thread tracks:
1. **SGLT2 inhibitors vs. DPP-4 inhibitors** initiation with
   all-cause death as endpoint — directly on the SGLT2i sub-thread.
2. **Sequentially-nested ARB vs. CCB** trials with heart-failure
   hospitalization and competing death — the sequential-trial
   framing is the correct one for TTE with time-updated
   eligibility.

The paper covers protocol → identification assumptions →
person-period data structures → stabilized-weights → truncation →
balance diagnostics → weighted pooled survival → standardization →
competing risks → cluster bootstrap. That's the full TTE checklist,
walked through in R.

**Actionable question.** Read for:
- **Comparison to the `TrialEmulation` R package** (Danaei / Hernán
  lineage) — how does this new `TTE` package differ? Is it faster,
  more feature-complete, or does it have a different scope (e.g.,
  competing-risks-first)?
- **Cluster bootstrap at original-individual level** — this is the
  right variance estimator for TTE with person-period expansion,
  but often skipped; worth verifying implementation.
- **AoU / UKB compatibility** — does the person-period data structure
  work with AoU's OMOP-CDM extraction, or does it require a bespoke
  reshape step?

**Where it links to your work.** Direct candidate for any TTE you
spin up (CFTR modulator × outcome, HRT × outcome, GLP-1 RA ×
persistence). Add the `TTE` package to the `causal-inference-os`
skill's software inventory alongside `TrialEmulation`. Consider
running the tutorial's SGLT2i example as a warm-up if you plan any
similar TTE.

---

### 8. Wang, Lin, Jin, Gao, Pradeepkumar, Jiang, *Benchmarking and developing large language models using one million clinical trials* — **npj Digital Medicine 2026** (Zhiyong Lu group)

**Feed:** Google Scholar author feed for Zhiyong Lu — "new articles"
(08-04 19:46Z).

**Why HIGH.** Zhiyong Lu (NLM / NCBI BioNLP) is a central node in
biomedical NLP infrastructure. A million-trial LLM benchmark is a
substrate-scale contribution — it's the eval set future biomedical
LLM claims will be judged against. Two threads:
- **EHR foundation models / clinical LLM benchmarks** — this is the
  clinical-trial-domain analogue of MedQA / MedMCQA / PubMedQA. If
  it's structured well, it becomes a portable eval for any clinical
  LLM you might consider (including LLM-based phecode extraction
  from notes, or LLM-based trial-matching pipelines like TrialGPT
  from the same group).
- **Drug repurposing (clinical-evidence loop)** — clinical-trial-
  derived benchmarks are the closest thing to grounded-evidence eval
  for drug-repurposing agents. Relevant to the drug-repurposing
  thread's `KG / GNN with explainable hypothesis output` sub-thread
  as an evaluation substrate.

**Actionable question.** Read for:
- **Task taxonomy** — what tasks does the benchmark cover? Trial
  eligibility parsing, outcome extraction, adverse-event extraction,
  treatment-arm mapping to OMOP concepts?
- **Data provenance** — are the trials from ClinicalTrials.gov
  registry entries, from published protocols, or from
  full-text-of-published-results?
- **Baselines** — do they benchmark GPT-4 / Claude / Llama / MedPaLM
  / Gemini across the tasks? The relative ordering matters for
  which model to reach for on which sub-task.
- **Comparison to TrialGPT** — same group, likely; check
  positioning.

**Where it links to your work.** Add to the `ncbi-nlp` skill's
benchmark section as the current-frontier clinical-LLM eval. Also a
candidate reference for the `ehr-foundation-models` skill's
benchmarking section, complementary to EHRSHOT (which is
patient-level rather than trial-level). Consider using as a
pre-adoption filter for any clinical LLM you plan to route through
LLM-based EHR phenotyping.

---

## METHODS-WATCH (worth crib-noting, not required reads)

- **Sasson, Levine, Shilo, Kohn, Lutsker, Godneva, Gabet, Krongauz,
  Weinberger, LeCun, Balestriero, Segal, *Self-supervised DXA
  representations encode multi-system disease risk, biological aging
  and heritability* — arXiv:2608.02208 (2026-08-03; digest 08-04)**.
  LeCun + Balestriero + Eran Segal is a heavyweight ML + biobank
  pairing. Trained on 11,540 unlabeled scans, evaluated on 47,400 UKB
  scans. Prognostic imaging FM on a modality (DXA) that's routinely
  captured but under-used. On-thread for EHR-adjacent multimodal FMs.
  METHODS-WATCH rather than HIGH because DXA is off the specific
  disease threads you track, but the design pattern (self-supervised
  imaging + UKB validation + heritability recovery + biological-age
  gap) is worth having in the mental library.
- **Krol, Rondeau, Choi, Briollais, *Correlated frailty model for
  analysis of genetic association in family studies* —
  arXiv:2608.02127 (2026-08-03; digest 08-04)**. Family-based
  common-and-rare variant testing with time-to-event outcomes, using
  a residual-familial × IBD-based frailty. Directly relevant to any
  family-based hereditary-cancer study (BRCA / MMR carrier families).
  METHODS-WATCH because family-based designs aren't the current
  active thread but they'll come up.
- **Xu, Tchetgen Tchetgen, Schisterman, Blackwell, Caniglia,
  *Regression-Based Proximal Reconciliation of Conflicting Trials with
  Unmeasured Effect Modifiers* — arXiv:2608.04202 (2026-08-04; digest
  08-06)**. Tchetgen Tchetgen (Penn) — proximal-causal-inference
  methodology extended to reconciling conflicting RCTs (Meis vs.
  PROLONG on 17-OHPC for preterm-birth prevention). Portable to any
  question "why do two AoU / UKB studies disagree" — proxies for
  unmeasured effect modifiers is the right frame. Useful cross-link
  for the Rodriguez et al. PMBB Toolkit paper (08-02 #6): if
  cross-biobank meta-analysis disagrees, this is a formal way to
  ask why.
- **Zhao, Wang, Han, Ma, Sun, *Rethinking Covariate Selection for
  Causal Effect Inference: The Primacy of Proximal Confounders* —
  ACM Trans KDD 2026** (Hripcsak-related feed, 08-04). Proximal
  causal inference literature is having a moment (see Xu et al.
  above). A KDD-adjacent take on proximal confounder selection is a
  useful pairing to the biostat versions. METHODS-WATCH — not
  substantively different from what the biostat literature already
  covers, but the CS-KDD framing may be more portable to
  ML-heavy pipelines.
- **Emfietzoglou, Keenan, Baroutis et al., *Sustained High-Intensity
  Lipophilic Statin Use and Risk of Age-Related Macular Degeneration:
  A Target Trial Emulation* — Ophthalmology Retina 2026** (Hernán
  citation network, 08-04). Direct TTE application paper in
  Hernán-adjacent style. AMD isn't on-thread, but this is a
  reference example of how the TTE design translates to a
  medication-class × distal-outcome question, adjacent to your
  statin-CHIP interest.
- **Zhang X, Zhang H, Fu, Feng, Wang, *Clonal Hematopoiesis of
  Indeterminate Potential in Cardiovascular Disease: Gene-Specific
  Mechanisms and Therapeutic Implications* — International Journal of
  … 2026** (`clonal hematopoiesis` feed, 08-03). Review paper of
  CHIP-driver-specific CVD mechanisms. Gene-specific mechanistic
  review is a useful counterpoint to the Carter et al. statin × CHIP
  MR paper (08-02 #12) — this review should motivate which CHIP-gene
  strata Carter et al. or your follow-ups should analyze.
- **Ao, Kolifarhood, Parisien, Bortsov, Grant, *Exome-wide association
  study of chronic pain in 327,642 UK Biobank participants* — Genome
  Medicine 2026** (Jian Yang / Stephen Montgomery related feeds,
  08-04, resurfaced from 07-31 flag). Very large UKB exome-wide scan
  from the Grant / Bortsov (Duke) group. Off-disease-thread but
  useful for anyone reading UKB rare-variant methods.
- **Cavanaugh, Wong, Smith, Bivas-Benita, Akiva, El-Hay, Orkaby,
  Yanover, Olivieri-Mui, *Evaluating Frailty Index Integrity: Insights
  from an International Network Study* — J Gerontol A Biol Sci Med
  Sci 2026** (NCBI AoU 08-05). Multi-network frailty-index audit;
  Yanover (IBM Research / KI Research) is a co-author, and this fits
  the multimorbidity / EHR-derived-composite-score audit angle. Read
  if scoping any AoU-based frailty analysis.
- **Butler, Fioretti, Anker, Khan, Marti, Pandey, Petersson, Linge,
  *Body Composition in Heart Failure: MRI and DXA Assessment in the
  UK Biobank Study* — JACC Heart Failure 2026** (NCBI UKB 08-06).
  Pandey (UTSW HF) + Anker (Charité HF); this is a UKB
  multimodal-imaging cardiometabolic association paper. Relevant to
  the LeDXA DXA-FM paper (above METHODS-WATCH #1) as a downstream
  clinical-question-side companion — DXA readouts in an HF cohort.
- **Dearman, Vrticka, Moore, Kumari et al., *Evaluating the
  performance of polygenic indices of neuropsychiatric conditions
  and brain endophenotypes in four UK population samples* — medRxiv
  2026** (Bastarache related feed, 08-04). PGS-evaluation paper
  across four UK samples. Off-disease-thread but a reference example
  of PGS-portability audits.
- **Hernandez, Mawass, Matheson, Masel, *Rare variants drive high
  variance in human ancestral fitness at mutation-selection-drift
  balance* — bioRxiv 2026** (Karczewski related feed, 08-04).
  Population-genetics theory paper on rare-variant fitness variance.
  Adjacent to your rare-variant thread as a "why we should care about
  rare-variant burden variance" theoretical grounding.
- **Corsi-Zuelli, Taquet, Deakin, R… *Potential preventive role of
  low-dose methotrexate against incident recorded psychosis: a
  retrospective cohort study based on electronic health records* —
  2026** (Pascal Brandt related feed, 08-03). EHR-based
  drug-repurposing signal in psychiatry. Off-disease-thread but the
  design (EHR-based off-label-use signal detection for psychiatry) is
  a template for the drug-repurposing sub-thread.
- **Ma, Chen, Shan, Du, Song, *Neural-symbolic temporal knowledge
  graph reasoning with multi-granularity modeling and compatibility
  constraints* — ESWA 2026** (KG feed, 08-05). Temporal KG reasoning
  paper. Adjacent to the `Knowledge graphs & ontologies` and
  `Knowledge representation in EHRs` threads; the temporal-KG angle
  is under-served in biomedical KG work.

---

## SKIPPED (present but off-thread)

Compressed list — noted for provenance so nothing is silently dropped:

- Mehdipour et al. — SCOPE OUD predisposition tool (AoU 08-06 NCBI).
  Opioid-use-disorder-predisposition classifier; off active disease
  thread but methodologically PheWAS-like — noted.
- CorePath (Yin et al. arXiv 2608.03079) — breast-CNB pathology FM
  (08-05 digest). Off-thread modality (pathology) despite the
  hereditary-cancer keyword adjacency.
- Chauhan, Ghadimi, Liu — causal forest for travel mode choice
  (08-06 digest). Off-domain (transportation).
- Sharipov, Mukhtarov, Molybog — Autoregressive Transformer for
  Single-Cell Generation (08-05 digest). Off-thread (single-cell
  generation, not on the EHR/biobank axis).
- Xiong, Hu, Zheng et al. — Contrastive single-cell pretraining
  (08-04 digest). Off-thread.
- Yu, Wu, Hood et al. — Bayesian joint modeling of SWAN
  symptomatology and falls (08-04 digest). SWAN is a great cohort
  but off-disease-thread here.
- Joshi B. — Formula 1 dirty-air causal analysis (08-06 digest).
  Off-domain but nice methods demo.
- Hut, Masoero — AI agents simulating A/B tests (08-04 digest).
  Adjacent to `agentic causal-inference pipelines` sub-thread but
  not on EHR / biobank; noted.
- Maung, Zheng — Group testing + IPW with CDC influenza data (08-05
  digest). On-thread by causal-inference keyword but for a
  group-testing surveillance design not typical of AoU/UKB.
- Wang J et al. — Systematic multi-level analyses of arthritis-
  neurodegeneration axis (UKB NCBI 08-06). Off-thread by disease.
- Zhang MJ et al. — CV health × pulmonary hypertension proteomic
  mediation (UKB NCBI 08-06). Off-thread disease.
- You Q et al. — Healthy lifestyle × CV-kidney-metabolic syndrome
  mortality (UKB NCBI 08-06). Off active disease thread.
- Chen J et al. — Bruceine A × alcoholic liver disease phytomedicine
  (AoU NCBI 08-05). Off-thread / animal model.
- Chen Q, Chen M, Guo J et al. — CRP-TyG index × cardio-renal-metabolic
  multimorbidity (UKB Scholar 08-05). Adjacent to multimorbidity
  thread but a biomarker-index paper rather than a clustering paper.
- Guo J, Qiao Y, Li H — IBD × ankylosing spondylitis MR / meta
  (Medicine 2026, `mendelian diseases` feed 08-05). IBD-adjacent
  but limited new signal.
- Multiple Google Scholar hits on educational EHR simulation
  (Huerne et al. 08-05), molecular autopsy in unexplained sudden
  death (Singh et al. 08-05), and unrelated review pieces from the
  same batch — all noted; none on active threads.
- Multiple drug-repurposing feed hits on nanoformulated
  triclabendazole × neurocysticercosis (de Souza et al. 08-05) and
  organoid drug-repurposing validation (Gulisano 08-03). Both
  off-thread by disease / methodology axis.
- APOL1 feed (08-05): "CB March" HTML page — collaboration listing,
  not a paper.
- Wang, Jiang, Yuan et al. — GLP-1 vs GIP MR × phenomic analyses
  (Metabolism 2026) — already noted in 08-02 report METHODS-WATCH,
  no update.
- Multiple ATVB conference abstracts on CHIP-mechanism vascular
  biology — off active EHR/PheWAS thread.

---

## Cross-report continuity notes

- **Motsinger-Reif / Ahn / House HLA trans-ancestry AoU paper**
  (08-02 report #2) — resurfaced this window via "2 new citations to
  articles by Chenjie Zeng" (08-04 19:46Z). Continues to accrue
  citations; no new content.
- **Bujnis et al. multi-ancestry Hashimoto's GWAS** — 08-02 report
  #3 flagged the pre-print; this window (item #2) has the formal
  *Nat Genet* publication.
- **Ran/Shen/Guan DR-FRL** (08-02 Bonus HIGH) — no re-surface, but
  Ciardulli et al. functional-PS (this report #4) is a natural
  compositional companion: DR-FRL handles functional histories,
  Ciardulli handles functional exposures. Both worth having in
  the toolkit.
- **Carter et al. statin × CHIP MR** (08-02 report #12) — no
  re-surface, but the Bate et al. ICI-repurposing MR (this report
  #6) is the same drug-target-MR-triangulated design pattern
  extended to a different disease context. Consider reading
  together.
- **Nagy et al. GeroScience reference-bias paper + HPRC v2**
  (08-02 report #11 + continuity) — no re-surface this window.
- **Rodriguez et al. PMBB Geno-Pheno Toolkit** (08-02 report #6) —
  no re-surface, but the Xu et al. proximal-trial-reconciliation
  paper (METHODS-WATCH this report) is a natural companion for
  cross-biobank-disagreement diagnostics.
- **Chou et al. `oci-agent`** (07-30 report HIGH #12) — still no
  re-surface. Continue watching.
- **Baya et al. AJHG polygenic-deviation** — still on the reading
  queue since the 07-23 report. The Motsinger-Reif / Denny
  tri-score paper (this report #1) is an orthogonal composite-risk
  design worth reading in the same session as Baya.
- **Wright et al. Nat Med rare-disease commentary** (08-02 report
  #7) — no re-surface this window.

---

## Suggested next actions

1. **Read Motsinger-Reif / Denny tri-score paper first** (item #1).
   New this window, from the Denny lineage, and directly on your
   composite-risk sub-thread. It also connects the composite-risk
   thread to the new `Knowledge representation in EHRs`
   sub-thread — a two-for-one read.
2. **Read Liu et al. gestational-phenotypes *Nat Genet*** (item #3).
   New this window, first-of-scale East Asian biobank gestational
   scan, with GxE / context-specific framing.
3. **Read Ciardulli et al. functional PS + Foulkes et al. IPW-two-
   phase together** (items #4 and #5). Both are causal-inference
   methods papers you'll want on the shelf for AoU / UKB TTE work;
   they complement DR-FRL (08-02 Bonus HIGH).
4. **Skim Bate et al. ICI-repurposing MR** (item #6). Same
   drug-target-MR triangulation design as the Carter statin-CHIP paper
   you already have queued — read them as a pair to establish the
   template.
5. **Bookmark Noma TTE-R-package tutorial** (item #7). Direct
   infrastructure candidate for your pharmacoepi work — decide
   whether to adopt `TTE` vs. `TrialEmulation` for the next TTE.
6. **Bookmark the Wang et al. 1M-clinical-trials LLM benchmark**
   (item #8) and Zhiyong Lu group's TrialGPT lineage as your
   evaluation substrate for any clinical LLM you consider adopting.
7. **Note the Bujnis *Nat Genet* publication** (item #2) — update
   citations if you're already citing the pre-print.
8. **Consider triangulating Xu et al. proximal reconciliation**
   (METHODS-WATCH) if you spin up a cross-biobank meta that shows
   disagreement — it's the right formal framework for asking
   whether an unmeasured effect modifier reconciles the disagreement.
