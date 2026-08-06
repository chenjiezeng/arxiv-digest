# Research digest report — 2026-08-02

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-30 12:35Z → 2026-08-02 12:30Z** (~3 days since
`reports/2026-07-30-research-digest.md`, which closed with the
morning-of-07-30 arxiv-digest run). Short catch-up — expect a tighter
HIGH list than the 07-30 multi-day report.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-07-31.md` → `2026-08-02.md`) | 07-31 → 08-02 (10:30Z crons) | 3 daily runs. 1 non-empty (07-31 with 1 paper — Ran/Shen/Guan DR-FRL); 08-01 and 08-02 empty with previously-surfaced suppressions. Score-1 hit on `causal inference`. |
| Google Scholar alerts (keyword feeds) | 07-31 → 08-01 21:30Z batch | 11 keyword feeds fired together on 08-01 (`drug repurposing`, `knowledge graph`, `APOL1`, `electronic health records`, `rare diseases`, `intitle:"clonal hematopoiesis"`, `variant interpretation`/`variant classification`, `phenome wide association studies`, `mendelian diseases`, `UK Biobank`, `foundation models + electronic health records`). Author-feed cluster did NOT fire this window — last one was 07-27, covered in the prior report. |
| Google Scholar alerts (author feeds) | — | None fired in-window. Watch for the next batch. |
| NCBI "My NCBI What's New" — AoU / UKB / drug repurposing | 07-30, 07-31, 08-01 | Three daily batches per topic (9 emails total). AoU volumes still small (3–6/day); UKB heavy (9–19/day); drug repurposing steady (7–10/day). Densest AoU signal is the 07-30 batch which surfaced two Denny-lineage AoU papers (Ahn et al. HLA trans-ancestry; Bujnis et al. Hashimoto's GWAS). |
| bioRxiv / medRxiv Subject Collection Alerts | daily (07-31, 08-01, 08-02) | Aggregate feeds; individual on-thread items pulled out below. The 08-01 medRxiv batch had a dense on-thread cluster (ClinGen glaucoma VCEP, interpretable omnigenic NN, uromodulin monogenic×polygenic, early-onset breast cancer GWAS+PheWAS). |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated to first
> 3–5 as they appear in the alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced this window, clustering into five knots that
are each dense enough to be their own story:

**All of Us / cross-ancestry PheWAS-infrastructure cluster (5 items).**
Zhang et al. *Nat Commun* — transcript-aware rare-variant AoU
cardiopulmonary scan (AoU native, gene-collapsing methods). Ahn/House/
Motsinger-Reif with Denny — trans-ancestry HLA architecture across
390k AoU participants, EHR-linked. Bujnis et al. (Denny + Kanai +
Fritsche) — multi-ancestry Hashimoto's thyroiditis GWAS in *Nat
Genet*. Gu et al. AoU OUD GWAS + DL functional annotation (cross-
ancestry). Kore et al. — local-ancestry-informed rare-variant burden
methodology for admixed populations (this is the methods-generalizable
piece that reweights the four AoU-empirical papers). Rodriguez et al.
PMBB Geno-Pheno Toolkit adds cross-biobank PheWAS infrastructure to
the same lane.

**EHR foundation-model pretraining wave (3 items, all from same lab
lineage).** Placidi/Liu et al. paired arXiv preprints — patient-aware
sampling for EHR FM pretraining + autoregressive multimodal (ECG +
codes) EHR FMs. Chen et al. *arXiv* — "medical world models" review
that is the field-defining framing reference for digital-twin work on
EHR data (adjacent to the Zhang/Ideker/Oermann *Cell* 2026 paper you
already track in the digital-twins-from-EHR sub-thread). Upmeier zu
Belzen et al. medRxiv add an "interpretable omnigenic neural network"
at the genome scale — different modality, same architecture-first
framing.

**Rare-disease diagnostic-odyssey commentary (1 item; big).** Wright,
Phillips, Wynn, Meade, Baple et al. *Nat Med* — "Reducing the
diagnostic odyssey in rare disease: why screening is not the only
answer." This is a Nature Medicine commentary from the Wright/Baple
group (DDD study lineage) that reframes newborn/preconception screening
against clinical WGS as complementary rather than substitute. Exactly
the framing paper your rare-disease thread wants when scoping
Uria-Regojo–style reanalysis cohorts.

**Causal-inference methodology (2 items).** Ran/Shen/Guan arXiv
DR-FRL — doubly robust functional representation learning for
longitudinal causal inference with irregular clinical histories.
Directly answers the "sequence learners minimize prediction loss, not
efficient influence function" gap in EHR-based TTE work. Carter et al.
medRxiv — statin drug-target MR × clonal hematopoiesis (HMG-CoA
reductase genetically predicted inhibition vs. observed statin use):
the drug-target-MR-triangulated-with-observational-cohort design your
INTERESTS.md pharmacoepi thread explicitly prioritizes, applied to
your CHIP thread.

**Variant-interpretation infrastructure (1 item).** Nagy et al.
*GeroScience* — "Beyond the linear genome: how reference bias
threatens preventive medicine and geroscience." Links directly to your
pangenome/HPRC v2 watch (07-30 report) and the reference-minor allele
concern for automated ACMG/AMP pipelines. This is the interpretive-
layer paper the HPRC2 preprint invited.

METHODS-WATCH bench includes Idogawa Varporter (ClinGen TP53 automated
classification), Tompson ClinGen Glaucoma VCEP for myocilin, Wang et
al. GLP-1/GIP drug-target MR triangulation in *Metabolism*, and
Abegaz/Frietze AoU GLP-1 ML — the last close enough to your GLP-1
thread that a full read is warranted.

---

## HIGH — full write-ups

### 1. Zhang, Hong, Wang, Jurgens, Liu et al., *Transcript-aware rare genetic variant association analyses of cardiopulmonary traits in participants from the All of Us Research Program* — **Nature Communications 2026** (s41467-026-75569-6)

**Feed:** Google Scholar `"All of Us research program"` keyword feed
(08-01 21:30Z; position 0 of 10).

**Why HIGH.** Three of your active threads collide here:
1. **EHR-linked biobanks (AoU)** — an AoU-native rare-variant scan
   published in *Nat Commun* is a canonical example of the pattern
   your infrastructure is built for.
2. **Genetic epi (rare variant methods, transcript-aware collapsing)** —
   transcript-aware burden testing is the current state of the art
   over gene-level collapsing (properly handles alternative transcripts
   and dominant-negative isoform-specific effects).
3. **ML-for-precision-health / cardiopulmonary phenotyping** — the
   phenotype ascertainment side is exactly the EHR-derived-outcome
   discipline the thread rewards.

**Actionable question.** Read the methods for:
- **Which transcript-aware model** (VEP + LOFTEE + transcript-set
  aggregation? MANE Select vs. all-transcript aggregation? How do they
  handle non-canonical transcripts with tissue-specific expression?).
- **Ancestry composition** — the AoU sample allows meaningful non-EUR
  representation; whether they stratify or pool matters for the
  cross-ancestry portability claim.
- **Phecode / cardiopulmonary phenotype definitions** — what OMOP /
  phecode lift are they using for the outcome side, since your AoU
  work will want to reuse or extend it.
- **Sample size + power** — AoU-native rare-variant scans have been
  power-limited until v9; whether this paper is on v8 or v9 tells you
  what's currently feasible for follow-on work.

**Where it links to your work.** Direct template for any AoU-native
rare-variant analysis you spin up. Also candidate for the
`verily-workbench-aou` / `aou-workbench-2` skill's example list of
AoU-native association-testing work in the recent literature.

---

### 2. Ahn, House, Burkholder, Tran, Breeyear, Justice, Durney… Denny, Motsinger-Reif, *Shared trans-ancestry architecture of HLA-mediated disease risk in the All of Us Research Program* — **Research Square 2026** (PMC13405435)

**Feeds:** Google Scholar `"All of Us research program"` keyword feed
(08-01 21:30Z, position 1); NCBI PubMed "What's new for 'All of Us'"
07-30 batch (as second-most-recent hit).

**Why HIGH.** Denny is a co-author. Three threads served:
- **EHR-linked biobanks (AoU)** — 390,823 AoU participants across six
  ancestry groups, 262,915 with linked EHR. This is the biggest AoU
  HLA scan on record, and the EHR linkage is what elevates it from a
  standard trans-ancestry GWAS.
- **Genetic epi (cross-ancestry portability)** — HLA is the
  archetypal locus where cross-ancestry portability is worst; a shared
  trans-ancestry architecture finding (if it holds) is a notable
  counterexample and worth reading for the methodological approach
  (graph-based HLA typing from WGS is called out in the abstract).
- **Autoimmune / IBD adjacency** — HLA-mediated disease risk includes
  IBD, celiac, T1D, RA, SLE. Even if IBD isn't the focus, the
  disease-set they scan will overlap.

**Actionable question.** Read the methods for:
- **Graph-based HLA typing pipeline** — pangenome-adjacent (which
  connects to Nagy et al. #11 below and the HPRC v2 preprint in your
  cross-report continuity notes). Which caller, and what's the
  concordance vs. IMGT/HLA imputation baselines?
- **How EHR was used** — as outcome definition (case ascertainment
  via phecodes) or covariate?
- **Trans-ancestry meta-analysis approach** — fixed vs. random
  effects; how they handled ancestry-specific HLA allele frequency
  differences.

**Where it links to your work.** Denny co-authorship makes this
directly relevant to your PheWAS/phecode infrastructure thread and
the biobank-scale-cross-ancestry thread. Also a candidate reference
for the `zeng-publications` skill's cross-ancestry AoU section.

---

### 3. Bujnis, Sterenborg, Li, Åsvold, Brčić, Boraska Perica, Babbar, Denny, Fritsche, Kanai et al., *Multi-ancestry GWAS provides insights into Hashimoto's thyroiditis* — **Nature Genetics 2026**

**Feed:** NCBI PubMed "What's new for 'All of Us'" 07-30 batch (07-30
15:20Z).

**Why HIGH.** Denny + Kanai (BBJ/Broad) + Fritsche (MGI) is the
canonical multi-biobank multi-ancestry GWAS author lineup, and a
*Nat Genet* multi-ancestry Hashimoto's GWAS is a design-reference
paper for the same architecture applied to any autoimmune outcome
you might pursue. Two threads served:
- **Genetic epi (multi-ancestry GWAS)** — the reference implementation
  of a Denny-lineage cross-biobank meta-analysis in 2026.
- **Autoimmune / IBD-adjacent disease** — Hashimoto's is autoimmune
  thyroiditis, shares HLA architecture with the broader autoimmune
  spectrum you track.

**Actionable question.** Read for:
- **Cohort composition** — which biobanks contribute (AoU + BBJ + MGI
  + UKB is the standard modern set; whether MVP is in tells you the
  ceiling on non-EUR representation).
- **Cross-ancestry meta-analysis strategy** — MR-MEGA, MRMEGA-2, or
  bespoke; whether they use ancestry-common vs. ancestry-specific
  effects.
- **Downstream analyses** — do they do fine-mapping, TWAS, or drug-
  target MR follow-on? Autoimmune GWAS loci that are drug-target-
  actionable are of specific interest (JAK inhibitors, IL-2 pathway).

**Where it links to your work.** Design reference for any multi-
biobank GWAS you might pursue for CFTR carrier phenotypes, APOL1
carrier phenotypes, or the hereditary cancer variant PheWAS you have
underway. Cite as prior art on the multi-ancestry meta-analysis
architecture side.

---

### 4. Gu, Petrovitch, Hall, Lambert, Kember, Nahid, Ma, Sprague, McDonough, Johnson, *GWAS and DL functional annotation of Opioid Use Disorder across three ancestries in All of Us* — **medRxiv 2026**

**Feed:** NCBI PubMed "What's new for 'All of Us'" 07-30 batch (07-30
15:20Z).

**Why HIGH.** Continues the AoU multi-ancestry GWAS lineage the
07-23 report flagged (Gu et al. AoU OUD GWAS was already in that
report; this looks to be the same team's DL-functional-annotation
follow-on, which is worth re-surfacing). Serves:
- **AoU / cross-ancestry GWAS** — three ancestries, actively-added
  functional annotation via DL.
- **Genetic epi (functional annotation via DL)** — a step beyond
  standard VEP / RegulomeDB; DL functional priors on GWAS hits is
  the current frontier.

**Actionable question.** Read for:
- **Which DL functional-annotation model** — DeepSEA, Enformer,
  ChromBPNet, or a bespoke one? The choice determines how portable
  the annotations are.
- **Fine-mapping integration** — do the DL priors go into a Bayesian
  fine-mapping framework (FLAMES, PolyFun) or are they used only for
  post-hoc annotation?
- **Cross-ancestry portability** of the fine-mapped signals — this
  is the specific gap this design is meant to address.

**Where it links to your work.** OUD is not a tracked disease
thread but the *methodology* is directly portable to your
cardiometabolic-outcome AoU work. Also a template for the "AoU
GWAS + DL functional annotation" pattern that will show up more
often as v9 lands.

---

### 5. Kore, Tan, Lu, Manuel-Friedman, Hu, Chatterjee, Zhou, Dhindsa, Atkinson, *Local ancestry-informed rare variant burden testing improves gene discovery in admixed populations* — **medRxiv 2026**

**Feed:** NCBI PubMed "What's new for 'All of Us'" 07-30 batch (07-30
15:20Z).

**Why HIGH.** Directly on the genetic-epi cross-ancestry portability
sub-thread, and it's the methodological piece that generalizes across
items #1–#4 above. Two threads served:
- **Genetic epi (rare-variant methods in admixed cohorts)** — local
  ancestry-informed burden testing is the frontier for AoU-style
  cohorts where individuals have ancestry-heterogeneous chromosomes.
  Atkinson (Broad) and Dhindsa (Regeneron) are both central authors on
  this class of methods.
- **PheWAS infrastructure** — any downstream PheWAS in AoU that uses
  rare-variant gene burden as the exposure benefits from this.

**Actionable question.** Read for:
- **Local ancestry inference tool used** — RFMix, GNOMIX, FLARE?
  This determines the local-ancestry call quality baseline.
- **Burden test formulation** — do they extend SKAT/SAIGE-GENE+/
  STAAR to accept local-ancestry-stratified allele frequencies, or
  do they build a new estimator?
- **Empirical demonstration** — which cohort, which disease, and
  how much gene-discovery uplift over ancestry-agnostic testing?

**Where it links to your work.** Direct methods candidate for any
AoU rare-variant PheWAS. Consider adding to the `tam` (PheTK) or
`broad-genomics` skill's rare-variant methods section.

---

### 6. Rodriguez, Guare, Caruth, Cardone, Carson, Cherlin, Mohammed, Gupta, Kumar, Keat, Verma SS, Verma A, *PMBB Geno-Pheno Toolkit: scalable reproducible pipelines for cross-biobank association analyses* — **bioRxiv 2026**

**Feed:** NCBI PubMed "What's new for 'All of Us'" 08-01 batch (08-01
17:14Z).

**Why HIGH.** Anurag Verma's group (Penn Medicine Biobank) is a
central node in the PheWAS-infrastructure community. A "cross-biobank
association analyses" toolkit is the pattern your PheWAS-infrastructure
thread has been waiting for — the reproducibility side of the
multi-biobank meta-analysis story that #3 (Bujnis) is the empirical
side of. Serves:
- **PheWAS / phecode infrastructure** — direct.
- **EHR-linked biobanks** — cross-biobank explicitly.
- **Knowledge representation in EHRs** — reproducible pipelines force
  the concept-mapping and phenotype-definition standardization your
  new "knowledge representation" thread cares about.

**Actionable question.** Read for:
- **What "scalable reproducible" means** in practice — Nextflow?
  Snakemake? WDL/Cromwell? This determines whether it's portable
  to AoU / dsub-based workflows.
- **Which biobanks it currently supports** — PMBB is the anchor; UKB,
  AoU, MVP, BioVU support is what would make this reusable for you.
- **PheWAS support** — do they wrap PheTK, PheWAS.R, or a bespoke
  layer?
- **Standardized phenotype library** — do they include a shipped
  phecode / phecodeX phenotype set, or do you bring your own?

**Where it links to your work.** Candidate addition to the `ohdsi`
skill's HADES / OMOP infrastructure section, and the `tam` skill's
PheTK companion. If the phenotype library is portable, could serve as
a shared substrate across AoU/UKB/MVP analyses you spin up.

---

### 7. Wright, Phillips, Wynn, Meade, Baple et al., *Reducing the diagnostic odyssey in rare disease: why screening is not the only answer* — **Nature Medicine 2026**

**Feed:** Google Scholar `rare diseases` keyword feed (08-01 21:30Z).

**Why HIGH.** Caroline Wright + Emma Baple are the DDD (Deciphering
Developmental Disorders) lineage — DDD is the reference-standard
paediatric rare-disease exome/genome-sequencing cohort. A *Nat Med*
commentary from this group on the diagnostic-odyssey framing is
canonical for the rare-disease thread. Serves:
- **Rare disease diagnosis** — direct, at the framing-paper level.
- **Data-driven reanalysis of unsolved cases** — this commentary is
  likely to explicitly compare newborn/preconception screening with
  reanalysis of already-sequenced clinical cases, which is the
  Uria-Regojo–style question in your active INTERESTS.md sub-thread.

**Actionable question.** Read for:
- **Screening vs. diagnostic testing framing** — does it advocate a
  particular ratio, or leave it agnostic? The relevant tradeoff is
  cost per solved case (screening at scale) vs. cost per solved case
  (deep phenotyping + reanalysis).
- **HPO-driven diagnosis positioning** — where does the commentary
  place HPO-driven phenotype-first diagnostic pipelines
  (Exomiser/LIRICAL/Phen2Gene) in the "not just screening" framing?
- **Newborn genomic screening** — likely to intersect the current
  GUARDIAN-NY / BabySeq2 debate. Which side does the commentary
  land on?

**Where it links to your work.** Framing reference for any rare-
disease diagnostic-yield analysis. Consider adding to the `wglab`
skill's rare-disease diagnostic-tool references, and the
`ehr-phenotyping-os` skill's phenotype-validation section (since the
"reanalysis" angle is essentially EHR-based rare-disease phenotype
curation at scale).

---

### 8. Placidi, Liu, Han, Rei, Faisal (and companion Liu, Placidi, Han, Balston, Rei, Faisal), *Pretraining EHR Foundation Models with Patient-Aware Sampling* — **arXiv:2607.22114 (2026-07-27)** + *Autoregressive EHR Foundation Models with Multimodal Inputs* — **arXiv:2607.22264 (2026-07-28)**

**Feed:** Google Scholar `foundation models + electronic health
records` keyword feed (08-01 21:30Z).

**Why HIGH.** Paired preprints from the same Imperial College / A.
Aldo Faisal group tackling the two live gaps in EHR-FM pretraining:
- Patient-aware sampling (fixing the standard-transformer assumption
  that documents / sequences are i.i.d. when they're actually
  patient-grouped) — direct sequel work to the CLMBR/MOTOR/EHRSHOT
  lineage's implicit patient batching.
- Autoregressive multimodal EHR FM adding waveform (ECG) alongside
  codes — one of the two big frontiers in EHR-FM (the other being
  imaging).

Both are directly on the EHR-foundation-models thread, and the
pairing means they're a compact reading unit — one methods paper and
one modality-extension paper — that establishes a design pattern.

**Actionable question.** Read for:
- **Patient-aware sampling formalism** — is it patient-level
  clustering + within-patient shuffling, or something more principled
  like a hierarchical loss? Sample efficiency claims should show
  scaling curves.
- **Multimodal fusion architecture** — early fusion (unified token
  stream) vs. late fusion (separate encoders); which does the
  autoregressive-multimodal paper adopt?
- **Benchmark choice** — do they use EHRSHOT or a new benchmark? If
  the latter, the contamination-audit concern (07-30 METHODS-WATCH
  note re: Ali scContam) becomes salient.
- **Comparison to CLMBR / MOTOR / MEDS-baseline** — necessary for
  positioning.

**Where it links to your work.** Direct candidate for the
`ehr-foundation-models` skill inventory. Also worth pulling into the
`callahantiff` skill's KG-adjacent references since Faisal's group
has been active on the EHR-representation-learning side.

---

### 9. Chen, Cong, Jin, Fan, Zhou, Ai, Gong et al., *Medical world models in healthcare: foundations, applications, and challenges* — **arXiv:2607.25242 (2026-07-29)**

**Feed:** Google Scholar `foundation models + electronic health
records` keyword feed (08-01 21:30Z).

**Why HIGH.** "World models" — the term of art from RL/robotics for
learned dynamics models of an environment — landing in the healthcare
FM literature is the field-defining framing shift the digital-twins-
from-EHR sub-thread has been anticipating. The Zhang/Ideker/Oermann
*Cell* 2026 paper you already track (Cell Digital Twins in Healthcare
and Medicine consortium) is the biology/systems side; this arXiv
review is the ML-architecture side of the same conversation. Two
threads:
- **EHR foundation models (digital twins from EHR)** — direct.
- **ML for precision health (individualized trajectory prediction)** —
  world models are precisely the substrate for individualized
  trajectory prediction under counterfactual interventions.

**Actionable question.** Read for:
- **Definition of "world model" for medicine** — is it a
  next-observation predictor, a counterfactual-outcome predictor, or
  a mechanistic simulator? Each has different validation regimes.
- **Coverage of EHR + non-EHR modalities** — do they include
  imaging, wearables, omics, or is it EHR-focused? EHR-focused
  coverage is what maps most directly to your thread.
- **Evaluation / validation framing** — a world model that has never
  been validated against counterfactual data is just an autoregressive
  model with a fancier name. Do they discuss the causal-inference
  overlay?

**Where it links to your work.** Reference framing paper for the
digital-twins-from-EHR sub-thread. Add to the `ehr-foundation-models`
skill alongside the Zhang/Ideker Cell paper as the two anchor
citations.

---

### 10. Upmeier zu Belzen, Arnoldt, Hollmann, Herrmann, Nguyen, Eckhoff, Kohleick, Abou Ghaloun, Schmidt, Hegselmann, Theis, Buergel, Steinfeldt, Wild, Eils, *An interpretable omnigenic neural network architecture for the human genome* — **medRxiv 2026** (submitted 08-01, v2 of a 07-31 v1)

**Feed:** medRxiv Subject Collection Alert 08-01; also medRxiv 07-31
alert (v1).

**Why HIGH.** Theis (Helmholtz / TUM) + Eils (BIH) is a computational
genomics powerhouse pairing, and an "interpretable omnigenic" NN at
the human genome scale is precisely the sort of architecture-first
work that reframes what "polygenic" means computationally. Two
threads:
- **EHR foundation models (architecture side)** — this is a genome-
  scale FM in the same conceptual space as CLMBR/MOTOR, on a
  different substrate (genotypes rather than clinical events).
- **Genetic epi (omnigenic / polygenic architecture)** — the omnigenic
  model of Boyle/Li/Pritchard is now getting NN implementations; a
  human-genome-scale interpretable one is a milestone.

**Actionable question.** Read for:
- **What "interpretable" means** — attention-map style, feature-
  attribution style (SHAP/integrated gradients), or something built
  into the architecture (concept bottleneck, sparse regression head)?
- **Training data** — UKB genotypes + phenotypes? Which trait set?
  Cross-ancestry?
- **Comparison to standard PRS** — the meaningful comparison is not
  just against SNP-level GWAS but against modern PRS (PRS-CS, PRSice)
  and against transformer-based genotype models.

**Where it links to your work.** Add to the `broad-genomics` skill's
population-genetics section as a design reference for
NN-based-polygenic-modeling. Also relevant to the `waxse` /
`ehr-phenotyping-os` skills as a substrate on which downstream EHR
phenotype prediction could be built.

---

### 11. Nagy, Munkácsy, Murmu, Longo, López et al., *Beyond the linear genome: how reference bias threatens preventive medicine and geroscience* — **GeroScience 2026**

**Feed:** Google Scholar `"variant interpretation" OR "variant
classification …"` keyword feed (08-01 21:30Z).

**Why HIGH.** This is the interpretive-layer paper the HPRC v2
preprint (in your 07-30 cross-report continuity notes) invited.
Reference-bias-in-preventive-medicine ties directly to two of your
threads:
- **Variant interpretation (ACMG / ClinGen)** — automated ACMG
  pipelines (InterVar, TAPES, VarSome) rely on reference-genome
  coordinates; reference-minor alleles create systematic
  misclassification, and preventive-genetics use cases (BRCA, LDLR,
  APOE) are where this hurts most.
- **Genetic epi (pangenome-informed variant calling)** — direct
  companion to the HPRC v2 update as the "why this matters clinically"
  paper.

**Actionable question.** Read for:
- **Quantitative estimates** of how much variant misclassification is
  attributable to reference bias (published clinical-actionable panel
  vs. GRCh38 reference-minor allele rate).
- **Recommendations for automated pipelines** — do they propose a
  concrete workflow change (pangenome-aware calling, or a post-hoc
  reference-minor allele flag)?
- **Geroscience angle** — likely to focus on age-related traits (APOE
  for AD, TERT for aging, CDKN2A for MI). Any overlap with your
  cardiovascular / cancer thread should be noted.

**Where it links to your work.** Reference candidate for the `wglab`
skill's variant-interpretation section, and a direct companion to the
HPRC v2 update in the `broad-genomics` skill. Cite together when
raising the pangenome-portability question.

---

### 12. Carter, Gozdecka, Wen, Quirós, Lockhart, Dudek, Bond, Richenberg, Larsson, Bromage, …, Vassiliou, Burgess, Kar, *Statin Use and Genetically Predicted HMG-CoA Reductase Inhibition in Relation to Clonal Hematopoiesis* — **medRxiv 2026**

**Feed:** NCBI PubMed "What's new for 'UK Biobank'" 07-30 batch (07-30
15:20Z).

**Why HIGH.** Vassiliou (CHIP lineage, Sanger) + Burgess (MR
methodology, Cambridge) + Kar (drug-target MR) is exactly the author
combination the INTERESTS.md `drug-target Mendelian randomisation
triangulated with observational cohort estimates` sub-thread points
at. And the outcome — clonal hematopoiesis — sits at the CHIP/VEXAS/
LOY somatic-mosaicism thread. Two threads intersect:
- **Causal inference / pharmacoepi (drug-target MR + observational
  cohort triangulation)** — this is the exact design pattern the
  active sub-thread flags.
- **CHIP / somatic mosaicism** — statin-CHIP association has been
  reported in observational cohorts before (2023 Bick et al.
  MESA/JHS/BioMe); the MR triangulation is the missing piece.

**Actionable question.** Read for:
- **Direction of effect** — do genetically-predicted HMG-CoA
  reductase inhibition and observed statin use both associate with
  CHIP in the same direction, or does the MR reverse the observational
  signal (which would suggest confounding by indication)?
- **CHIP ascertainment** — UKB WES-based CHIP calling; what caller
  and VAF threshold?
- **Which HMG-CoAR SNPs** — the standard rs17238484 / rs12916 pair,
  or a broader instrument? The multi-instrument analysis is where
  drug-target MR gets tricky.
- **Cross-CHIP-gene stratification** — DNMT3A vs. TET2 vs. ASXL1 —
  the biology differs by CHIP driver and the statin-CHIP association
  may not be uniform.

**Where it links to your work.** Direct template for the "drug-target
MR + observational-cohort statin/HMG-CoAR" pattern that could be
extended to metformin/AAA (Saxby et al. in the 07-23 report) or
GLP-1/cardiovascular. Also worth adding as a reference for the CHIP
thread — the Kessler et al. *Nature* 2022 lineage.

---

## Bonus HIGH — pure arxiv-digest hit

### Ran, Shen, Guan, *Doubly Robust Functional Representation Learning for Longitudinal Causal Inference with Irregular Histories* — **arXiv:2607.28567v1 (2026-07-30; digest 07-31)**

**arxiv-digest hit:** score 1 (`causal inference`).

**Why HIGH.** Directly on the causal-inference thread and it fills a
specific methodological gap you care about: standard doubly-robust
estimators need scalar summaries of history, but EHR / ICU / VitalDB
data is inherently irregular functional (laboratory point clouds,
vital-sign streams). DR-FRL is a cross-fitted workflow that turns
irregular histories into estimand-targeted state representations,
with EIF-targeted validation, calibration, overlap, tail, and
ablation diagnostics. Two features make it HIGH rather than
METHODS-WATCH:
1. **The "if the representation preserves EIF-relevant nuisance
   information, representation error enters the same second-order
   product remainder as ordinary nuisance error" theorem** is the
   right formulation — it tells you when representation learning is
   *safe* for downstream causal inference, not just when it might
   work.
2. **VitalDB negative-result honesty** — the paper reports that for
   ICU-disposition, scalar lab summaries already carry most of the
   endpoint-relevant information, so DR-FRL doesn't help. A paper that
   publishes its own negative finding is high-signal.

**Actionable question.** Read for:
- **Nuisance-head architectures** — outcome, treatment, censoring
  functions; what NN class?
- **Overlap diagnostic** — how do they define "overlap for functional
  representations"; is it a marginal density-ratio check or a
  representation-space distance test?
- **Sample efficiency** — the "when does DR-FRL help" question is
  really "how big does the effective sample need to be relative to
  the representation complexity."

**Where it links to your work.** Direct methods reference for any
AoU TTE with irregular EHR follow-up (labs, medication reconciliation
events). Compare to Chou et al. `oci-agent` (07-30 report #12) — DR-FRL
is a *statistical* methods paper; `oci-agent` is a *workflow*
paper. They compose: DR-FRL is a valid estimator that `oci-agent`-
style pipelines could adopt as one of their DR-Learner options.

---

## METHODS-WATCH (worth crib-noting, not required reads)

- **Idogawa, Takada, Mariya, Ishikawa, Iyama et al., *Varporter: a
  software platform for comprehensive genomic profiling in cancer* —
  Human Genome Variation 2026** (from `"variant interpretation"` feed).
  Automated ClinGen TP53 variant interpretation platform — a rare
  example of "the exact right VCEP is baked into the tool." File as a
  reference implementation for gene-specific automated variant
  classification. Relevant to your BRCA / hereditary-cancer work.
- **Tompson, Graham, Hadler, Pasutto, Whisenhunt, Chakrabarti, Young,
  Craig, Hewitt, Siggs, Hulleman, Mackey, Burdon, Dubowsky, Souzeau,
  *ClinGen Glaucoma VCEP recommendations enhance classification of
  myocilin variants* — medRxiv 2026** (from medRxiv 08-01). The
  companion paper to Idogawa — this one is the VCEP-development-side
  paper for glaucoma (myocilin). Reference for the ClinGen VCEP
  workflow when you next scope a similar gene-specific curation
  effort for one of the CFTR / APOL1 / BRCA panels.
- **Wang, Jiang, Yuan, Sun, Zhao, Zhou, Liang, Li, Song et al.,
  Mantzoros, *Complementary body weight and cardiometabolic benefits
  of higher GLP-1 and lower GIP: genetic evidence from phenomic
  analyses* — Metabolism 2026** (from NCBI UKB 07-31). Drug-target
  MR + phenomic scan for the *combination* of GLP-1 and GIP effects
  (relevant to tirzepatide, which is dual agonist). Companion to Wang
  et al. Metabolism 2026 lineage. On-thread for GLP-1 pharmacoepi,
  but MR rather than TTE — hence METHODS-WATCH not HIGH.
- **Abegaz, Frietze, *ML algorithms for predicting glycemic control
  and weight-loss outcomes in GLP-1 RA users* — Frontiers in
  Artificial Intelligence 2026** (from NCBI AoU 07-30). AoU-based ML
  for individual GLP-1 response prediction. Directly serves the ML-
  for-precision-health thread + GLP-1 sub-thread, but the "which model"
  matters for whether it clears the "tied-to-a-clinical-decision" bar
  — full read recommended.
- **Lu, Chen, Treggiari, Blessing, Zhuo, Weng et al., *Toward
  Automated Detection of Documentation Inconsistencies in Electronic
  Health Records* — arXiv:2607.22954 2026** (from `"electronic health
  records"` and `foundation-models + EHR` feeds — double hit).
  Weng (Columbia) group; LLM-based EHR-documentation-QA. Relevant to
  the EHR-phenotyping thread as a note-side data-quality layer.
- **Khan, Gresch, Olinger, Mariniello, Shang, Perez-Gomez, Dinsmore,
  Mabillard, Mirshahi, Chang, Devuyst, Kiryluk, *Uromodulin T62P
  variant causes kidney tubular stress and injury modulated by age
  and polygenic risk* — medRxiv 2026** (from medRxiv 08-01). Kiryluk
  (Columbia, kidney genetics) + Devuyst — a monogenic × polygenic
  interaction paper on a specific uromodulin variant. This is the
  micro-scale version of your PGS-residuals / polygenic-deviation
  thread applied to a single monogenic locus, in kidney. Reference
  for the general "monogenic penetrance modulated by polygenic
  background" question that also comes up in APOL1.
- **Peng, Jackson, Alpen, Ye, Southey, Li, *Genetic susceptibility
  and causes for early-onset breast cancer: genome-wide and
  phenome-wide analyses* — medRxiv 2026** (from medRxiv 08-01).
  GWAS + PheWAS combined design for early-onset breast cancer;
  Southey (MCCS) group. Relevant to your cancer-epi background,
  METHODS-WATCH rather than HIGH because it's not directly on the
  active hereditary-cancer thread but the combined design is worth
  cribbing.
- **AL-Sakkaf, *Agentic-TimesFM-AKI: Dual LLM-Time Series Framework
  for Predicting Drug-Induced AKI with Privacy-Preserving Synthetic
  Data* — medRxiv 2026** (from medRxiv 08-01). Combines the
  federated / privacy-preserving sub-thread with an agentic LLM
  overlay and a time-series FM (TimesFM). Long on framing, TBD on
  method quality — worth a skim to see whether the synthetic-data
  approach is DP-guaranteed or just informal.
- **Mustra Rakic, Vorobiev, Pullinger, Malloy et al., *Abstract
  Thu035: Additive Association of Apolipoprotein L1 Risk Genotype
  With Circulating Apolipoprotein L1 Protein Levels in African
  American Adults* — ATVB 2026** (from `APOL1` feed). Conference
  abstract — genotype-protein correlation in AA adults. Small
  incremental datum on the APOL1 protein-level side; watch for the
  full paper.
- **Hsu, Liu, Hardaway, Wang, Yalcinkaya et al., *Ninjurin-1
  Deficiency Drives Atherosclerosis Progression in Clonal
  Hematopoiesis* — ATVB 2026 Abstract Thu057** and **Liu, Liu, Tuo,
  Tang, *TET2-Deficient CH Promotes AAA via Macrophage Pyroptosis* —
  ATVB 2026 Abstract Thu013** (from `clonal hematopoiesis` feed).
  Two ATVB conference abstracts on CHIP × cardiovascular disease.
  Mechanistic angle rather than the EHR-outcome angle your CHIP
  thread specifically calls out; note for adjacent context.
- **Ao, Kolifarhood, Parisien, Bortsov, Grant, *Exome-wide
  association study of chronic pain in 327,642 UK Biobank
  participants* — Genome Medicine 2026** (from NCBI UKB 08-01). Very
  large exome-wide chronic-pain scan; relevant to the UKB-rare-variant
  side of your infrastructure thread even though pain is off-disease.
- **Kiiskinen, Richland, Wang, Lu, Narasimhan, Hastie, Tibshirani,
  Rivas, *CuGen: GPU-accelerated framework for large-scale
  genomics* — medRxiv 2026** (from NCBI UKB 07-30). Rivas + Hastie/
  Tibshirani (Stanford stats) — GPU-genomics infrastructure paper.
  Not on any active disease thread but of interest as a
  computation-scaling reference for the AoU / UKB / MVP workflows
  where genotype × phenotype matrix multiplications are the
  bottleneck.
- **Goel, Chan, Grace, Thomson, Kim, Desvigne-Nickens, Kolm,
  DiMarco, Desai, Kwong, Ho, Weintraub, Kramer, Neubauer, Watkins,
  *Genotype-Phenotype Correlations Identify Phenotypic Differences
  in Sarcomere Mutation-Positive HCM (NHLBI HCM Registry)* —
  medRxiv 2026** (from medRxiv 07-31). Monogenic penetrance in HCM;
  Watkins lineage. Reference for the "clinically ascertained vs.
  biobank-ascertained penetrance" question your PheWAS-monogenic
  thread cares about (Baya AJHG 2026, still on the reading queue
  from the 07-23 report).

---

## SKIPPED (present but off-thread)

Compressed list — noted for provenance so nothing is silently dropped:

- Al-Oudah et al. — Drug repurposing + autoimmune 2020–2025 systematic
  review (drug-repurposing feed). Non-empirical review, off the
  EHR-evidence-loop angle.
- Liu Y et al. — Drug repurposing across 92 CNS conditions with DL +
  WGS (Neurotherapeutics 2026). Already covered in the 07-30 report
  as HIGH #11 — re-surfaced in this window's drug-repurposing feed.
- Chen X et al. RareLens (arXiv 2607.23290) — end-to-end rare-disease
  LLM. On-thread by keyword; skimmed and de-elevated to
  METHODS-WATCH-adjacent since GraphRareBench (07-30 #13) is the
  currently-recommended benchmark to run any such tool through.
- Bahramimehr et al. — Chitinase-3-like protein-1 in pancolitis
  (drug-repurposing feed). Mechanism/target paper; IBD-adjacent but
  off the EHR / target-trial angle.
- Sun H et al. — KG for health-assessment-scale linking (KG feed).
  Biomedical KG-adjacent; low-signal.
- Ibrahim A et al. — OCT biomarker for Alport / COL4 (variant-
  interpretation feed). Imaging biomarker; not variant-classification
  work despite the keyword hit.
- Gu X et al. — CETP inhibition MR for intracranial aneurysm
  (variant-interpretation feed, mis-flagged). Drug-target MR but on a
  drug class not tracked.
- De Paoli F — AI framework for rare-disease genetic diagnosis (PhD
  thesis, Italian). Off-thread by format (dissertation, not
  peer-reviewed article).
- Sardar R — vgen23.com blog on genomic infrastructure gap. Industry
  commentary, not primary research.
- Nguyen H, Huang Y — Bullous pemphigoid × autoimmune diseases
  EHR+MR (Mendelian-diseases feed). Off-thread disease.
- Multiple UKB feed hits on cardiometabolic sub-topics (Zhang M
  APOE ε4 × modifiers, Liu C AF in Black participants, Huang J
  autoimmune × AF, Wang G sleep × osteoarthritis, Broad SR cancer
  susceptibility × lung cancer, Zhang X wearable × PAD, Zhang Y
  fiber × NAFLD, Wu Z eGDR × MASLD, Tan M EASO obesity, Li L HRT
  × BPPV, Goyal A CAD PRS × recurrent CV events, Arrarte V
  menopause × BP, Liu X immune-metabolic × sepsis, Sniderman A HDL
  × apoB × ASCVD, Qiya Z HHV6 × dementia, Chen Q cannabis × brain
  pleiotropy, Luo Z metabolic syndrome × CRC, Abula A CV aging
  multimodal, Gu Z water hardness × diabetic retinopathy) — noted;
  all off active disease threads or too routine to elevate.
- Multiple bioRxiv Genomics collection hits on cattle intolerance
  scores, plant genomes, single-cell atlases — off-thread.
- Fan Q et al. AoU menstrual disorders × ibuprofen / OC. Off-thread
  by disease.
- Rahman H et al. AoU opioid overdose ML — off-thread disease though
  serves the ML-for-precision-health rubric weakly.
- Lloyd SM et al. AoU Evenings with Genetics community program — AoU
  program-descriptive, not a research paper.
- Wei et al. — genetic correlation brain × externalizing behavior
  (UKB LDSC). Off-thread disease.
- Zhang R et al. — flavonoids × psoriasis GxE (UKB). Off-thread
  disease.
- Xia D et al. — Lp(a) × aortic disease (UKB). Off-thread.
- Shi Z et al. — Unified prostate cancer PRS (UKB). Adjacent to your
  cancer background but not on active thread.
- Diambra L et al. — MASLD proteomic endotypes (UKB, Gut). Adjacent
  to multimorbidity/clustering thread but off active disease.
- Zheng J et al. — In-utero sugar restriction × dementia
  (Neurology). Interesting life-course design, off active thread.
- Kondaparthy SC, Macha SC — AI in clinical practice (Springer
  conf). Off-thread review.
- Multiple ATVB abstracts on non-CHIP mechanistic vascular biology —
  off-thread.

---

## Cross-report continuity notes

- **HPRC v2 pangenome preprint** (Lucas, Hebbar, Liao et al.) — surfaced
  again this window on 08-01 in the NCBI AoU batch. Now paired with the
  Nagy et al. GeroScience "reference bias" paper (#11) as the
  clinical-implications side; read together.
- **Denny lineage AoU work** continues to accelerate — two Denny-
  co-authored AoU papers surfaced this window (Ahn/House HLA
  trans-ancestry #2; Bujnis Hashimoto's #3). The 07-27 Scholar author
  feed covered the previous window; another author-feed batch is
  expected in the next 7 days.
- **Chou et al. `oci-agent`** (07-30 report HIGH #12) — no new activity
  yet in this window's alerts, but Ran/Shen/Guan DR-FRL (Bonus HIGH
  above) is a compositional companion — DR-FRL is a valid estimator
  `oci-agent` could adopt.
- **Baya et al. AJHG polygenic-deviation** paper — still on the reading
  queue since the 07-23 report. Not re-surfaced.
- **Streit et al. Nature Genetics BPD GWAS + BPD-PheWAS** — no
  re-surface this window.
- **DRIVE v3** (Bastarache lab, 07-23 report) — no re-surface.
- **Gu et al. AoU multi-ancestry OUD GWAS** (07-23 report) — the
  companion DL-functional-annotation paper #4 above is the follow-on
  work; the earlier GWAS should now be read alongside it.

---

## Suggested next actions

1. **Read Zhang et al. Nat Commun (AoU transcript-aware rare-variant
   cardiopulmonary) first.** Peer-reviewed *Nat Commun* + directly
   on the AoU + rare-variant infrastructure your work depends on.
2. **Read Wright et al. Nat Med rare-disease commentary next.** Fast
   read (commentary), high-signal framing update for the rare-disease
   thread.
3. **Skim the Placidi/Liu paired EHR-FM arXivs together** — they're
   short, from the same group, and define a pretraining-design
   pattern worth being aware of.
4. **Read Carter et al. medRxiv statin-CHIP MR** — direct template
   for the drug-target-MR × observational-cohort triangulation your
   INTERESTS.md pharmacoepi thread explicitly asks for.
5. **Read Nagy et al. GeroScience reference-bias paper together with
   the HPRC v2 preprint.** They're the clinical-implications and
   infrastructure sides of the same story; read as one.
6. **Read Ran/Shen/Guan DR-FRL arXiv** — short paper, direct methods
   candidate for any AoU TTE with irregular follow-up. Consider
   adding to the `causal-inference-os` skill's estimator inventory
   alongside `oci-agent`.
7. **Skim Rodriguez et al. PMBB Geno-Pheno Toolkit** — if it supports
   AoU / UKB / MVP as first-class citizens, it might replace or
   augment homegrown PheTK-wrapper scripts.
8. **Note the Bujnis Nat Genet + Ahn/House Res Sq multi-ancestry
   design pattern** — both use the same Denny + Kanai + Fritsche +
   MGI-style multi-biobank meta-analysis architecture; establish this
   as your reference design for any multi-biobank GWAS you spin up.
