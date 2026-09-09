# Research digest report — 2026-09-09

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS-LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-09-04 → 2026-09-09 12:35Z** (primary scanning window;
the last committed report was `reports/2026-07-30-research-digest.md`,
so anything between then and 2026-09-04 has been superseded by newer
alerts and is out of scope for this run).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-09.md`) | 09-01 → 09-09 (10:30Z crons) | 9 daily runs. 5 non-empty (01, 02, 04, 07); 03, 05, 06, 08, 09 empty. 5 papers surfaced total. 1 METHODS-WATCH (Rajabli/Collins brain-age foundation model, 09-07); Cortez-Rodriguez + Yu extremal QTE (09-04) sit at the methods-lane edge; Ghiasi storage-centric genomics (09-01) and Ramesh mudskipper locomotion (09-02) are off-thread SKIP. |
| Google Scholar alerts (author-feed cluster) | 09-06 → 09-08 | Denny (related + citations), Bastarache (related + citations), Callahan (related + citations), Zeng (related), Montgomery (related + citations), Zitnik (related), Yang (related + citations), Luo (citations), Karczewski (related + citations), Hripcsak (citations + related), Wang (related), Pritchard (citations), Abecasis (new articles), Neil Davies (new articles), Gusev (new articles), Brandt (related). |
| Google Scholar alerts (keyword feeds) | 09-08 06:12Z batch | Ten keyword feeds fired together — `electronic health records`, `UK Biobank`, `All of Us research program`, `variant interpretation / classification / causal variant`, `foundation models & EHR`, `knowledge graph`, `drug repurposing`, `APOL1`, `clonal hematopoiesis`, `autoimmune diseases / disorders`, `mendelian diseases`, `rare diseases`. |
| bioRxiv / medRxiv Subject Collection Alerts | daily 09-07, 09-08, 09-09 | Aggregate feeds — individual on-thread papers surfaced upstream via Scholar. |
| arXiv q-bio daily 60-1 (Sep 9 05:56Z) | 09-09 | Bulk category listing; nothing survives against `config/tracked.yaml` beyond what the digest cron already caught. |

> Caveat: Scholar / arXiv keyword emails contain title, authors, venue,
> and the first ~2–3 lines of each abstract only. The reports below
> contextualize that metadata against your research threads; nothing
> here reflects full-text reading. `arxiv-digest` entries include the
> full abstract because the pipeline captures it.

---

## Executive summary (HIGH-priority studies, ranked)

Ten HIGH items surfaced this window, clustering into five knots:

**EHR foundation models + LLM agents (1 item, high signal).** Liu et al.
*Nature Medicine* — **MoChiAgent**, an LLM-orchestrated Mother-Child
clinical assistant that predicts maternal and infant outcomes directly
from longitudinal EHR. This is exactly the "agentic prediction from
raw longitudinal EHR" pattern the digital-twin-from-EHR sub-thread has
been tracking; Nature Medicine venue moves it from methods-curiosity
to a reference paper for the thread.

**Composite risk models + PGS-tails / rare-variant × PGS (3 items).**
Bal et al. *Nature Cardiovascular Research* — multi-ancestry PRS
improves risk stratification in patients with hypertrophic cardio-
myopathy where SARC-P/LP variants explain only ~⅓ of cases (the
canonical "rare pathogenic × PRS" composite-risk design). DePaolo et al.
*European Heart Journal* — gene variants + PRS for thoracic aortic
disease (parallel HTAAD-P/LP × PGS story). Dutta et al. *Cell Genomics*
— PRS × plasma proteomics across 21 cancers, identifying trans-regulated
protein networks (the multi-omics-augmented-PRS sub-thread).

**PheWAS / biobank infrastructure (2 items).** Hysong et al. *AJHG* —
three-biobank meta-analysis (BioVU + Penn Medicine Biobank + All of Us,
n=58,830 African-ancestry participants) of sickle-cell trait via
PheWAS + LabWAS. This is a canonical example of your "PheWAS +
phecodes + African-ancestry stratification + EHR-linked biobank"
intersection and worth reading before writing methods for anything
similar. Brownstein et al. *J Med Genet* — WES + EHR-linked biobank
analysis identifying candidate deafness genes.

**Rare disease / HPO diagnosis (1 item).** Brunello et al. *Human
Genomics* — GenPhenia deep neural networks for HPO-driven rare-disease
diagnosis. Extends the Phenolyzer / Phen2Gene / LIRICAL / Exomiser
benchmarking family; the GraphRareBench separable-metrics argument
should be propagated here.

**Drug repurposing + variant interpretation (3 items).** Perée et al.
*Nature Communications* — cis-eQTL analysis across 27 sorted blood
cell populations + 43 intestinal cell types identifies genes matching
140 IBD risk loci and nominates entrectinib as a repurposing candidate
(cell-type-eQTL → repurposing, IBD thread + KG-informed drug repurposing).
Bai et al. *J Pharm Analysis* — knowledge-graph screening for
synergistic anticancer drug combinations (explainable-KG drug
repurposing angle). Hull et al. *Human Genetics* — ClinGen RS1-specific
ACMG/AMP variant classification criteria for X-linked retinoschisis
(gene-specific VCEP framework, directly on the ACMG/ClinGen thread).

**GxE / PGS × environment (1 item).** Liu, Ramteke, Anand *Genome
Research* — biobank-scale method for learning G→E interaction
modulators from complex-trait data. Sits alongside Nagpal & Gibson
*Nature Genetics* 2026 as the second big-cohort G×E entry this quarter.

Two additional CHIP/APOL1 disease-thread entries fell between HIGH and
watchlist — Da Silva Faria *Blood Advances* on CHIP in autoimmune
hemolytic anemia (CHIP + autoimmune crossover, worth flagging) and
van Hougenhouk-Tulleken *Clinical Kidney Journal* on BP + APOL1 in a
South African dialysis population (in-population APOL1 phenotyping).

---

## HIGH — full write-ups

### 1. Liu, Zheng, Kang, Xu, Chen, Li et al., *Prediction of maternal and infant outcomes from longitudinal electronic health records with a Mother-Child AI agent* — **Nature Medicine 2026**

**Feed:** `"electronic health records"` keyword alert (09-08 06:12Z).
Top position, marked IMPORTANT.

**Why HIGH.** The paper claims MoChiAgent, an LLM-based clinical
assistant that orchestrates multiple sub-models to predict a range of
maternal and infant outcomes from longitudinal EHR, moves beyond the
"pick one endpoint, engineer features, train one model" pattern into
agent-orchestrated multi-endpoint prediction. That touches three of
your threads at once:

- **EHR foundation models** — a Nature Medicine paper on longitudinal
  EHR prediction via an LLM agent lands squarely in the CLMBR / MOTOR
  / MEDS lane, with the twist that the top-level model is an LLM
  agent rather than a monolithic transformer over medical codes.
- **Knowledge representation in EHRs and applications** —
  representation choice for pregnancy trajectories (irregular time,
  admissions as containers, medication-exposure windows) is exactly
  what this section of `INTERESTS.md` calls out.
- **Digital twins from EHR data** — the endgame the Zhang / Ideker /
  Oermann *Cell* framing paper articulates. A Mother-Child agent that
  predicts trajectories from raw longitudinal EHR is a step toward
  that individualized-trajectory endgame; whether it holds up as a
  digital-twin foundation vs. a well-engineered ensemble is the read.

**What to check on full-text read.**
1. Sub-model architecture — is the "agent" an LLM router over
   classical prediction heads (light-touch orchestration) or does it
   generate predictions autoregressively?
2. External validation — one-site, multi-site, cross-country?
3. Calibration and decision-curve analysis for actionable endpoints,
   not just AUC.
4. Any pretraining-contamination audit (scContam-style) — outcomes
   like maternal mortality get discussed in text; a naive LLM could
   memorize them.
5. Whether the "endpoints" are code-driven phenotypes or chart-review
   validated. Nature Medicine reviewers should have pushed on this
   but sometimes accept coded outcomes.

**Not-yet-visible.** The abstract preview gives outcomes and design
framing but not sample size, cohorts, or the endpoint list.

**Priority action.** Read full text within the week. Cite in the EHR
foundation models notes as the LLM-agent counterpoint to
CLMBR/MOTOR/MEDS lineage.

---

### 2. Bal, Pampana, Nayak, Gaonkar, Patel et al., *A multiancestry polygenic risk score improves stratification in patients with hypertrophic cardiomyopathy* — **Nature Cardiovascular Research 2026**

**Feed:** Joshua C. Denny "new related research" (09-06 06:02Z),
marked IMPORTANT. Top position.

**Why HIGH.** Composite risk models (rare pathogenic × PRS) are an
active sub-thread in `INTERESTS.md` under Genetic epidemiology. HCM
is the canonical case: SARC-HCM-P/LP variants explain only about a
third of cases, leaving the remaining two-thirds as either
oligogenic, polygenic, or environmental. This paper uses a multi-
ancestry PRS to stratify risk within a clinically-diagnosed HCM
cohort — exactly the composite framing you want the digest to
prioritize.

Two features of this study that make it worth full-text reading:
1. **Multi-ancestry construction** rather than an EUR-derived score
   ported over. That's the direction the field is moving; whether
   the multi-ancestry construction actually improves discrimination
   in each ancestry group vs. an EUR-only score is the question.
2. **In-patient stratification** rather than population-screening.
   The clinical question is *among diagnosed HCM patients*, does the
   PRS predict severity, complications, or SCD risk? This is a much
   harder discrimination task than case/control.

**What to check on full-text read.**
1. Was the PRS constructed within the HCM cohort or on all-comers?
   The Baya *AJHG* 2026 "misaligned individuals" framing warns that
   in-cohort PRS constructions collide with ascertainment.
2. Absolute risk stratification (top 5%, top 10%) rather than only
   AUC / HR — for the composite-risk framing to matter clinically,
   the top-tail effect size must be actionable.
3. Ancestry-specific calibration curves in each subgroup, not just
   pooled discrimination.

**Priority action.** Extract the composite-risk-of-monogenic-disease
methods for reuse: how they defined the P/LP subgroup, how they
handled ancestry stratification, and how the PRS was ported. This is
a direct template for hereditary-cancer and hereditary-kidney studies.

---

### 3. Hysong, Shuey, Miller-Fleming, Keat et al., *Phenome- and laboratory-wide meta-analyses of sickle cell trait reveal multi-system disease associations* — **American Journal of Human Genetics 2026**

**Feed:** Bastarache "10 new citations" (09-07 16:17Z, top). Also
surfaced in Denny citations feed same batch — the double citation-feed
hit indicates the paper is being read as canonical
PheWAS-in-African-ancestry-biobanks methodology.

**Why HIGH.** Direct hit on the PheWAS / phecode infrastructure thread
and the biobanks-with-EHR-linkage thread simultaneously. Three
features:

- **Three-biobank meta-analysis** (BioVU + Penn Medicine Biobank +
  All of Us). This is exactly the multi-biobank template your PheWAS
  thread anchors on.
- **58,830 African-ancestry participants, of whom 4,813 have SCT.**
  Sample size makes previously borderline SCT-associated conditions
  detectable. Ancestry-stratified analysis by design.
- **PheWAS + LabWAS together.** LabWAS (clinical-lab-wide association)
  complements phecode PheWAS by picking up sub-clinical signals that
  never make it to a coded diagnosis. This is the pattern the
  Żebrowska et al. *eBioMedicine* Circadian Imbalance Index study
  used (surfaced in the 2026-07-30 report) and is worth propagating
  wherever you're studying carriers of a common variant.

**What to check on full-text read.**
1. Phecode vs. phecodeX — which map did they use? Given the AJHG
   venue and the BioVU authorship, phecodeX is likely.
2. LabWAS methodology — median vs. any-observed threshold, how they
   collapsed multiple measurements per person.
3. Novel vs. replicated associations — SCT is well-studied enough
   that most of the "significant hits" will be already-known; the
   value is in effect-size refinement and new sub-clinical signals.
4. Site-heterogeneity — how much of the between-biobank
   heterogeneity is genuine phenotype heterogeneity vs. coding
   practice differences? This is the site-shift question your
   Knowledge-representation thread flags.

**Priority action.** This is a template paper. Read carefully and cite
in methods when writing anything that combines PheWAS + LabWAS across
three biobanks, or anything doing African-ancestry-stratified analysis
of a common variant.

---

### 4. Perée, Petrov, Tokunaga, Kvasz, Farnir et al., *Cell-type specific analyses in blood and gut identify cis-eQTL matching 140 IBD risk loci and entrectinib as repurposing candidate* — **Nature Communications 2026**

**Feed:** Stephen B Montgomery "new related research" (09-06 06:02Z),
marked IMPORTANT.

**Why HIGH.** Two active threads collide here:

- **Drug repurposing** — the paper explicitly nominates
  **entrectinib** (an approved ROS1/NTRK/ALK inhibitor for solid
  tumors) as a repurposing candidate for IBD. This is the
  cell-type-specific-eQTL → repurposing pattern rather than
  KG-only or chemistry-only nomination — which is exactly the
  angle your Drug-repurposing section calls "high-priority."
- **Inflammatory bowel disease** — one of the specific disease
  threads. 140 risk loci refined at cell-type resolution across
  blood and gut is a substantial expansion.

**What to check on full-text read.**
1. How they colocalized eQTL with GWAS signal — coloc, LocusFocus,
   OpenTargets, or in-house?
2. Which cell types drove the entrectinib nomination — the
   drug-repurposing hypothesis is only as strong as the cell-type
   attribution.
3. Any human real-world-evidence signal already in play (entrectinib
   users have small n in solid tumors, but any concurrent IBD
   phenotype data in the tumor cohorts would strengthen the case).
4. Whether the framework generalizes to other GWAS-rich, cell-type-
   heterogeneous diseases — psoriasis, RA, ankylosing spondylitis.

**Priority action.** Read full text within the week. This is a
concrete example of what your Drug-repurposing thread asks for:
KG- or eQTL-informed hypothesis with a specific clinical-evidence
loop. Also relevant for a possible AoU / MVP EHR-based follow-up
looking for entrectinib exposure × IBD outcomes.

---

### 5. Brunello, Colangelo, Rius, Erra, Lugones et al., *GenPhenia: using deep neural networks to accelerate rare-disease diagnosis* — **Human Genomics 2026**

**Feed:** Lisa Bastarache "new related research" (09-07 16:17Z, top).

**Why HIGH.** Direct hit on the rare-disease HPO-driven diagnostic
benchmarking sub-thread. Extends the Phenolyzer / Phen2Gene / LIRICAL
/ Exomiser / PhenoGPT2 family with a new DNN backbone.

**What to check on full-text read.**
1. **Separable metrics for ranking vs. evidence coverage.** The
   GraphRareBench observation (Hit@10 hides ranking-of-confounders)
   is exactly the QC argument you want propagated here. Does GenPhenia
   report Hit@1 / Hit@5 / Hit@10 alongside a coverage / recall
   metric at each rank cutoff, or only aggregate accuracy?
2. **Confounder handling.** How well does it discriminate the
   correct gene from other genes in the same phenotype
   cluster (Bardet-Biedl vs. Alström, Marfan vs. Loeys-Dietz)?
3. **HPO version drift.** Which HPO release was used for training?
   Rare-disease benchmarks are notoriously fragile to HPO version.
4. **Comparison baselines.** Is it compared to LIRICAL / Exomiser
   on the same held-out cases, or on a favorable curated set?
5. **Explainability.** DNNs on HPO terms tend to be opaque; whether
   the paper offers phenotype-level saliency or gene-level rationale
   determines whether it's clinically usable.

**Priority action.** Skim full text; extract the benchmarking design
if it's rigorous. If it lacks separable ranking-vs-coverage metrics,
add to the METHODS-WATCH counter-examples that the GraphRareBench
critique is meant to correct.

---

### 6. Hull, Mero, Hankey, Lee, Sullivan et al., *Development of RS1-specific ACMG/AMP variant classification criteria with pilot variant curation* — **Human Genetics 2026**

**Feed:** `"variant interpretation" OR "variant classification"`
keyword alert (09-08 06:12Z, top).

**Why HIGH.** Direct hit on the ACMG / ClinGen VCEP variant-
interpretation thread. RS1 (X-linked retinoschisis) is a small VCEP,
but the *pattern* — gene-specific ACMG/AMP criterion specification +
pilot curation to validate — is exactly the template you want to
track for the CFTR, APOL1, and hereditary-cancer VCEPs.

Key framing: the paper motivates the work by pointing at *gene therapy
eligibility* — the RS1 VCEP is driven by need to classify variants for
enrollment in gene therapy trials. This is a live application area for
the ACMG framework, and worth flagging as the direction the field is
going for other therapeutic-eligibility-driven VCEPs.

**What to check on full-text read.**
1. Which ACMG criteria did they specify or restrict (PS3, PP3, PVS1,
   BP1, BP4, BS3)?
2. What functional-evidence weighting did they use? RS1 has good
   biochemistry; whether the VCEP adopted a strong PS3 or a moderate
   PS3_moderate is the tell.
3. What percentage of previously ambiguous VUS resolved on pilot
   curation? This is the field's benchmark for "did the specification
   actually help."

**Priority action.** Save as reference for any CFTR / hereditary-
cancer VCEP methods writing. The RS1 template is directly reusable
for other gene-therapy-driven variant classification efforts.

---

### 7. Liu, Ramteke, Anand, *A biobank-scale method for learning modulators of G→E interactions* — **Genome Research 2026 (early release)**

**Feed:** Denny "new related research" (09-07 16:17Z).

**Why HIGH.** Direct hit on the GxE / PGS × exposure / environment
interactions sub-thread. Complements Nagpal & Gibson *Nature Genetics*
2026 as the second G×E method-paper this quarter. The framing —
learning environmental modulators of G→E interactions from biobank-
scale complex-trait data — is exactly the "GxE reframes PGS
portability" angle you flagged.

**What to check on full-text read.**
1. How they defined "environment" — self-reported exposures,
   biomarkers, area-level SES, or all three?
2. Multiple-testing burden for the modulator scan and how they
   handled it (BH FDR vs. G×E-specific hierarchical procedure).
3. Simulation study showing power vs. false-positive rate under
   realistic G×E effect sizes — the field has been burned by
   G×E "hits" that don't replicate.
4. Any UKB → AoU / MVP portability check? A method that only works
   in UKB is a UKB tool, not a G×E method.

**Priority action.** Read alongside Nagpal & Gibson. Together they
should give you a clear read on where G×E methods stand at biobank
scale in mid-2026.

---

### 8. Bai, Wu, Yang, Wu, Xia, Zhang, Bo, He, *Knowledge graph-based screening for synergistic anticancer drug combinations* — **Journal of Pharmaceutical Analysis 2026**

**Feed:** Tiffany J Callahan "new related research" (09-07 16:17Z).

**Why HIGH.** Drug repurposing sub-thread — specifically the
"explainable KG output" angle. Combination therapies for cancer are
combinatorially explosive; a KG-based screen that outputs *rationale
subgraphs* (rather than opaque link-prediction scores) is what your
thread flags as high-priority.

**What to check on full-text read.**
1. Is the KG output actually explainable (path or subgraph rationale
   per predicted combination), or is it a scored ranking?
2. Real-world / clinical-evidence loop — do they validate any of the
   top predictions against DrugCombDB, SYNERGxDB, or actual clinical
   trial data?
3. Which node types are in the KG — proteins only, or proteins +
   pathways + diseases + phenotypes?
4. What's the base rate for known synergistic pairs in the eval set?
   The bar for a "novel discovery" is meaningful only against a
   sensible base rate.

**Priority action.** Compare against RACER (Lou et al., in the Callahan
Sep 6 feed) — both are agent / KG approaches to drug-related reasoning.
Together they anchor the "explainable-KG drug repurposing" corner of
the thread.

---

### 9. Brownstein, Kamal, Zoabi, Gesin, Knoller et al., *Exome sequencing and large-scale analysis of electronic medical record-linked biobank data identify candidate deafness genes* — **Journal of Medical Genetics 2026**

**Feed:** Denny "new related research" (09-07 16:17Z).

**Why HIGH.** Biobanks + EHR linkage thread. WES + EHR-derived
phenotypes for a specifically Mendelian condition (hearing loss)
where up to half of inherited cases remain gene-unresolved. This
is a rare-variant-discovery-with-EHR-outcomes design — the pattern
your `INTERESTS.md` calls out for penetrance estimation under
population-screening vs. clinically-ascertained conditions.

**What to check on full-text read.**
1. Which biobank(s) — the abstract preview does not name them.
2. How was hearing loss defined from EHR — audiology-lab values,
   ICD-based coding, or notes-derived? Hearing loss is
   under-coded in EHR outside of specialty settings.
3. Novel gene claims must clear a high bar. Any functional evidence
   for the candidate genes, or purely statistical association?
4. Ancestry composition of the biobank — hearing loss genetics has
   strong ancestry-specific components (e.g., GJB2 dominant in some
   populations, absent in others).

**Priority action.** Skim for methodology. If the biobank is one you
work with (BioVU / AoU / UKB / MVP), read in full and cite for the
"WES + EHR phenotypes → Mendelian gene discovery" pattern.

---

### 10. Dutta, Zhang, Guo, Quint, Rooney et al., *Polygenic risk scores and plasma proteomics identify cancer-related proteins and trans-regulated protein networks* — **Cell Genomics 2026**

**Feed:** Denny "new related research" (09-06 06:02Z).

**Why HIGH.** Multi-omics-augmented PRS sub-thread. Integrates PRSs
for 21 cancers with 4,955 plasma proteins in cancer-free individuals
— a proteomics-PGS scan for trans-regulated protein networks.

**What to check on full-text read.**
1. Which cohort — UKB Olink, ARIC SomaScan, or another? Assay choice
   materially affects which proteins are in-scope.
2. Trans- vs. cis- regulated protein networks are much harder to
   interpret; the value of the paper depends on whether the "network"
   claims are supported by enrichment tests or just co-occurrence.
3. Any drug-target inference (druggable trans-regulators
   identified from the PRS-protein scans)? The natural bridge to
   drug repurposing.
4. Cross-cancer versus cancer-specific signals — is the shared
   network structure biologically informative, or dominated by
   pan-cancer inflammation / clotting proteins?

**Priority action.** Read alongside Feng et al. cross-ancestry
IDP pleiotropy (in your 07-30 write-up) and Shan et al. UKB
multi-omics-PRS — this trio anchors the multi-omics-augmented-PRS
picture for late 2026.

---

## Watchlist: CHIP / APOL1 disease-thread hits

Two items fall between HIGH and skip — thread-relevant but each on its
own not yet a call-to-action paper.

### Da Silva Faria, Moisan, Lecluze, Pincez, *Clonal Hematopoiesis in Autoimmune Hemolytic Anemia* — **Blood Advances 2026**

**Feed:** `intitle:"clonal hematopoiesis"` keyword alert (09-08 06:12Z).

CHIP × autoimmune disease crossover — pairs with the growing CHIP-
autoimmunity literature (Blood ITP paper cited in the abstract as
methodological precedent). AIHA is small-n by nature; the interest is
in whether CHIP is *enriched* in AIHA vs. matched controls, and
whether specific CHIP driver mutations (DNMT3A vs. TET2 vs. ASXL1)
show differential association. Read after Sep 09 open-access release
if it's not already open.

### van Hougenhouk-Tulleken, Rheeder et al., *Blood pressure and APOL1 risk variants in a South African chronic haemodialysis population of African ancestry* — **Clinical Kidney Journal 2026**

**Feed:** `APOL1` keyword alert (09-08 06:12Z).

APOL1 thread. The value here is that it's an *in-population* study
(South African African-ancestry haemodialysis cohort) — the phenotype
description of hemodynamics under APOL1 dosage in an African-ancestry
end-stage-renal-disease population is exactly the missing piece
between the US biobank APOL1 literature and the West/South African
populations where the risk allele is far more common. Skim the effect
sizes and sample size; likely useful as a reference paper rather than
methods.

---

## METHODS-WATCH

Papers not directly on any active disease thread, but methods worth
cribbing for future work.

### Zhang, Yoshiji, Sladek, Dupuis, Lu, *Benchmarking Bayesian Colocalization Methods in Validating Mendelian Randomization-identified Targets* — **Genomics, Proteomics & Bioinformatics 2026**

Feed: Denny "new related research" (09-07). Direct methods reference
for the drug-target Mendelian-randomization triangulated with
observational cohort estimates sub-thread. When you write MR
triangulation methods, this is the paper to cite for coloc-method
selection (coloc vs. eCAVIAR vs. hyprcoloc vs. SuSiE-coloc).

### Qi, Belloy, Gu, Liu, Tang, He, *Robust Inference With Ghostknockoffs in Genome-Wide Association Studies With Sample Relatedness* — **Genetic Epidemiology 2026**

Feed: Denny "new related research" (09-07). Knockoff-based GWAS
inference under family / cryptic relatedness. Reference for any
biobank GWAS where the relatedness structure is non-negligible (AoU
in particular).

### Barbosa Araujo, Fiuza, Ferraz, Kroll et al., *From Data Curation to Risk Reporting: A Pipeline for Polygenic Risk Scores* — **bioRxiv 2026**

Feed: Denny "new related research" (09-07). End-to-end PRS pipeline
paper — QC, ancestry stratification, calibration, reporting. Worth
reading for the reporting section specifically; PRS reporting
standards are still maturing.

### Roberts, Thompson, Anderson, Smith, *Polygenic Pharmacotherapy beyond Single-Gene Rules: An Evidence Map of Scores, Interactions, Ancestry Transferability, and Clinical Utility* — **International Journal of Pharmaceutical Research 2026**

Feed: Denny "new related research" (09-07). Evidence-map review of
PGS × drug response. Overlaps with the pharmacogenomic-modifier-of-
medication-persistence sub-thread. Venue (IJPR) is lower-tier, so
weight the review as a *review* rather than a primary reference —
useful as a scoping map, not as a foundation citation.

### Zhang, Zhou, Li, Ryckman, Ray, Scifres et al., *PRS-CARV: A summary statistics framework for integrating annotation-informed rare variants to improve polygenic risk prediction* — **Research Square 2026**

Feed: Denny "new related research" (09-06). Summary-statistics framework
that integrates rare-variant annotation into PRS construction —
directly speaks to the composite-risk / PGS-tails framing. Read
before writing anything that combines PRS with rare pathogenic
variants at scale.

### Rajabli & Collins, *A Generalizable Feature Extractor for Alzheimer's-Related Brain MRI Tasks* — **arXiv 2609.05400 (surfaced by digest 09-07)**

Foundation-model transfer-learning paper. Off primary thread
(imaging-only, no EHR), but the LoRA-adapter + frozen backbone
architecture is a portable pattern worth noting — the same "small
adapters over a frozen supervised backbone" recipe should also work
for CLMBR / MOTOR fine-tuning to site-specific tasks.

### Cortez-Rodriguez, *Natural Disasters and the Nonprofit Sector* — **arXiv 2609.04136 (surfaced by digest 09-04)**

Off-thread substantively (nonprofits, not health) but the panel-
causal-inference methodology (contradicting prior positive
associations with a properly-controlled panel design) is worth
noting as a null-effect worked example — the sort of "prior
associations were confounded" story your pharmacoepi thread pays
attention to as a design counter-example.

### Yu, Huang, Liu, Tang, Wang, Zhang, Zhao, *A location-invariant estimator of extremal quantile treatment effects for heavy-tailed distributions* — **arXiv 2609.04018 (surfaced by digest 09-04)**

Extremal QTE estimator with IPW-adjusted causal EVI. Niche but
directly on the heavy-tailed outcome / propensity-score interaction
that comes up in cost / length-of-stay analyses. Save as reference
for heavy-tailed causal-inference work.

---

## SKIP-noted (surfaced but off-thread)

- Ghiasi, *Storage-Centric System Designs for Enabling Fast,
  Efficient, and Low-Cost Genomic and Metagenomic Analyses* — arXiv
  digest 09-01. Hardware/storage-systems dissertation; genomic-adjacent
  but not on any research thread here.
- Ramesh et al., *Mudskippers use tail thrusting to help crutching to
  move on mud of various wetness* — arXiv digest 09-02. Biomechanics;
  keyword hit on "motor" is incidental.
- Ong, Qin, Soon, Chua, Yilmaz et al., *Beyond Metabolic Syndrome:
  Expanded Cardiometabolic Phenotyping Reveals Distinct Sleep and
  Physical Activity Profiles from Wearable Monitoring* — Zeng "new
  related research" (09-06). Wearable phenotyping paper; touches the
  multimorbidity thread lightly but is not EHR-based or biobank-linked.
  Track as low-priority read.
- Krantz et al. JAMA Netw Open — HLA-A*32:01 and lamotrigine DRESS.
  Pharmacogenomic HLA thread-adjacent but not on any active thread
  here; noteworthy for HLA-PGx clinicians.
- Wei et al. Briefings in Bioinformatics — X chromosome QTL WAS
  methods. Off-thread methods.
- Chen et al. Frontiers in Bioinformatics — Taiwan lipid PRS.
  Population-specific PRS with limited transfer to your active
  cohorts.

---

## Reading queue (rank order for the week)

1. **Liu et al. Nature Medicine — MoChiAgent** (EHR + LLM agent)
2. **Bal et al. Nat Cardiovasc Res — HCM multiancestry PRS**
3. **Hysong et al. AJHG — SCT tri-biobank PheWAS + LabWAS**
4. **Perée et al. Nat Commun — cell-type eQTL IBD + entrectinib**
5. **Liu, Ramteke, Anand Genome Res — biobank G×E modulators**
6. **Hull et al. Hum Genet — RS1 ACMG VCEP** (skim, save as template)
7. **Bai et al. J Pharm Analysis — KG anticancer drug combos**
8. **Brunello et al. Hum Genomics — GenPhenia DNN rare-disease dx**
9. **Dutta et al. Cell Genomics — 21-cancer PRS × plasma proteomics**
10. **Brownstein et al. J Med Genet — WES + EHR deafness genes**

Watchlist and METHODS-WATCH entries can wait until the HIGH queue
clears.
