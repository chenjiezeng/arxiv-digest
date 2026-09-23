# Research digest report — 2026-09-23

Triage of research-related email (Google Scholar alert feeds) + the local
`arxiv-digest` repo against the active threads in `INTERESTS.md` (PheWAS /
phecodes, EHR-linked biobanks, EHR phenotyping / OMOP, causal inference &
pharmacoepi, variant interpretation, genetic epi, CF / APOL1 / CHIP-VEXAS
/ LOY / IBD disease threads, EHR foundation models, KGs / ontologies,
drug repurposing, rare disease, ML for precision health, multimorbidity,
knowledge representation in EHRs).

Window: **2026-09-21 12:40Z → 2026-09-23 12:40Z** (~2 days since the last
research-digest report, covering one `arxiv-digest` cron run and one full
Scholar day plus one keyword-feed evening wave).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-22.md`) | 09-22 daily cron | 3 papers, all score 1: PACE (frozen tabular foundation-model column encoder as an upstream feature-screening primitive — foundation-model keyword only, generic ML), `tteICE` R package implementing the five ICH E9 (R1) strategies for treatment-effect estimation with intercurrent events in two-arm trials (methods-watch for causal inference), and Charpentier & Barry benchmark-relative pooling–profiling scale for motor-insurance tariffs (SKIP; the "motor" keyword hit is on insurance, not sensorimotor). No 09-23 file — the cron fires at 10:30 UTC and today's run has not yet committed at the time of this report. |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com arxiv-digest newer_than:3d` and `chenjiezeng/arxiv-digest newer_than:7d` returned zero threads. Consistent with prior reports: the pipeline commits its output to this repo rather than emailing PR/cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-22 batch, 06:46Z — author feeds) | 09-22 | ~30 author feeds fired. HIGH-item authors: Miguel Hernán citations-to (Hellemans et al. **BMJ 2026 international target-trial-emulation of deceased-donor kidney transplantation vs continued dialysis** across five European registries; Lu et al. JAMA Network Open **RSV vaccine effectiveness in US older adults, 2023-24**; Wen International Journal of Biostatistics **monotonicity-preserving doubly-robust g-computation** for time-varying treatments; Chi et al. Genes & Diseases **Trustworthy AI for disease pathogenesis and precision medicine** disease-agnostic framework), Konrad Karczewski new-related (**Boßelmann & May *Human Molecular Genetics* 2026 — mutation-rate estimates and somatic variants from cancer improve variant interpretation in epilepsy**; Uffelmann & Visscher bioRxiv **liability-scale variance explained for polygenic scores**; Génin et al. **POPGEN local-ancestry reference panel for metropolitan France**), Karczewski citations-to (Muzammal et al. Med Data Min genomic-variant-analysis / structure-prediction tools review), Joshua C. Denny new-related (**Bal et al. *Nature Cardiovascular Research* 2026 — multi-ancestry PGS improves stratification in HCM patients**, PGS-on-Mendelian composite risk; **Perée et al. *Nature Communications* 2026 — 27-blood + 43-intestinal cell-type-specific eQTLs match 140 IBD risk loci and prioritise entrectinib for repurposing**; Bakr et al. J Biomedical Informatics **MEDAL sequential adapter learning for privacy-preserving multicenter clinical LLMs** — also on the Hripcsak feed; Hu et al. Hypertension **antihypertensive drug-target MR for MAFLD/NAFLD repurposing**; Zheng et al. medRxiv **PGS vs proteomic risk score divergence in neurodegeneration** absorption/co-expression modules), Denny citations-to (Sanchez et al. Lancet cirrhosis GWAS — see cross-feed hit below; Duarte-García et al. *Arthritis & Rheumatology* **TTE of azathioprine/belimumab/methotrexate/MPAA in non-renal SLE from Optum**), Lisa Bastarache new-related (**Goel *European Journal of Human Genetics* 2026 — "Penetrance, effect and causal attribution: which number should be reported for recurrent CNVs?"** editorial; **Shi/Swanson/Diemer/Gerlovin medRxiv 2026 — selection bias in MR studies with adjustment for medication use (LDL-C example)**; Shen et al. Research Square **integrated PRS composite and ensemble learning for precision medicine (PGx tie-in)**), Bastarache citations-to (Jasper et al. Frontiers in Immunology **FOLR2 gene-based PheWAS across 3 classes of variation** — eMERGE lineage), Chenjie Zeng new-related (Sanchez et al. Lancet cirrhosis GWAS; Doumat et al. Current Opinion in Pulmonary Medicine **medical issues and pulmonary outcomes in CF and bronchiectasis** overview; Shi et al. MR selection bias medRxiv), Stephen B Montgomery new-related (**Zhang et al. medRxiv — PRS-CARV summary-statistics framework integrating annotation-informed rare variants to improve PGS prediction**; Lekka et al. npj Genomic Medicine **Cas9-directed long-read sequencing to resolve the CES1 PGx locus**; Henry et al. Epilepsia **biallelic RNU2-2 developmental and epileptic encephalopathy** rare-disease phenotypic characterization; Sanchez cirrhosis GWAS), Tiffany J Callahan new-related (**Vichentijevikj et al. — *GeneResolver* traceable hybrid multi-agent pipeline for etiology-aware gene prioritization** in rare disease), Zhiyong Lu new articles (**Lefkowitz/Eisenberg/Huang/Mudunuri et al. — Machine-readable database for genotype-phenotype analyses in rare diseases using FKTN-related congenital muscular dystrophies as a prototype**), Zhiyong Lu new-related (Ho et al. arXiv "Language Models Can Control Their Own Attention" — infra), Emily Alsentzer new articles (**Sivaraman/Turnham/Bonano/Aresh et al. arXiv 2609.19318 — "I Know Where to Look, But Does the LLM?" Charting gaps between clinical expert needs and unstructured-data-abstraction tools**), Marinka Zitnik new-related (KV-cache / long-context LM infra items — LOW), Michael Snyder new articles (**Lautman/Chang/Rangan/Hittle/Uwakwe et al. IEEE JBHI — interpretable workflow for cohort phenotyping using longitudinal wearable data**), George Hripcsak new-related (MEDAL, as above), Hripcsak citations-to (Chi et al. Trustworthy AI framework; Spiero et al. **pretrained LMs for cohort selection from EHR notes and downstream effect on prognostic-model performance**; Riess et al. **DZHK Feasibility Explorer for cardiovascular cohort discovery across multi-study data**), Kai Wang new-related (Park et al. BMC Medical Genomics **SETD5-related disorders HPO-based clinical/genotypic characterization**), Patrick Ryan new-related (Tartof et al. **bivalent RSVpreF effectiveness across three RSV seasons**), Peter Szolovits new-related (long-context LM infra — LOW), Yuan Luo citations-to (Sanchez cirrhosis GWAS), Jian Yang / Neil M Davies / David Baker / Bryan Traynor / Pascal Brandt / Leo Anthony Celi — mostly off-thread or previously covered items. Sanchez et al. Lancet cirrhosis GWAS surfaced across at least seven feeds (Denny/Bastarache/Zeng/Yang/Montgomery/Yuan Luo/Denny-citations); treated as one HIGH item below. |
| Google Scholar alerts (09-22 batch, 21:55Z — keyword feeds) | 09-22 | ~11 keyword feeds fired. HIGH-item hits: `Foundation models AND "electronic health records"` (**Mehandiratta & Anubhuti *Intelligent Hospital* 2026 — "Human Digital Twins for Precision Healthcare: A State-of-the-Art Review of AI, Multiscale Biology, and Clinical Decision Intelligence"** — direct hit for the `EHR foundation models → Digital twins from EHR data` sub-thread; also Wang et al. **RMHP methodological review of deep learning for early adverse-event prediction in ICU from EHRs**; Yuan et al. IJCAI-preprint **hypergraph learning across patient visits for EHR-based diagnosis prediction** — knowledge-representation angle), `"variant interpretation" OR "variant classification"` (**J Chen 2026 UNC dissertation — "Genomic Medicine Translation: Evidence Generation for Genomic Risk Assessment, Clinical Implementation, and a New Tool for Variant Interpretation"** — eMERGE-IV monogenic+polygenic CHD analyses + new noncoding-variant tool), `mendelian diseases` (same Chen dissertation), `"All of Us research program"` (**C Huang 2026 UCLA dissertation — "Metabolic, Neurocognitive, and Demographic Determinants of Musculoskeletal Health: Evidence from Large-Scale Real-World Data"** cross-cohort AoU + Medicare + TriNetX diabetes-osteoporosis + related analyses; SC Kim thesis on **geocoding-pipeline benchmarking in the AoU program**; AC Dunkwu 2026 dissertation on **combined rare-and-common-variant PRS for prostate cancer**), `"knowledge graph"` (all off-thread — enterprise KG, ML-resource KG, cybersecurity KG, construction KG; SKIP), `"drug repurposing"` (structure-based VAV2-targeting for foam-cell suppression in atherosclerosis, CNS AI drug design chapters — mostly METHODS, no EHR-based angle), `rare diseases` (patient-family experience after complex treatment for rare disease; mitochondrial-disease-as-model-for-rare-disease-services BMJ Innovations perspective; Chen dissertation cross-hit), `"UK Biobank"` (active commuting × biological-aging UKB analysis — LOW), `intitle:"clonal hematopoiesis"` (**F Luca 2026 dissertation — "Immune Perturbation and Mutant Clone Fitness During Clonal Hematopoiesis of Indeterminate Potential"**), `"autoimmune disorders"` (TNF-α inhibitor spectrum review; tertiary lymphoid structures in autoimmune disease and cancer — mostly review/mechanistic, no EHR angle). |
| Google Scholar alerts (09-21 evening batch, 02:03Z) | 09-21 | Already inside the previous report's window (which cut at 12:40Z 09-21 and drew from an 07:55Z 09-21 batch); this later 09-21 evening batch surfaced items that were largely folded into that report's "Variant interpretation" and "All of Us research program" keyword-feed rows (e.g., Boßelmann & May which now also re-surfaces on the 09-22 Karczewski-related feed — see below). No new HIGH items after cross-checking against the 09-21 report. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against the research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets. The Sanchez et al. cirrhosis GWAS appears
> in seven different author feeds simultaneously (Denny, Bastarache,
> Zeng, Yang, Montgomery, Yuan Luo, Denny-citations) — a single paper,
> not seven; listed once below.

---

## Executive summary (HIGH-priority studies, ranked)

Thirteen HIGH items surfaced this window, clustering into six knots:

**Multi-ancestry GWAS in an EHR-relevant clinical outcome (1 item, top of list).**
**Sanchez, Clària, Galvanin, Aguilar, Layese et al. *Lancet Gastroenterology
& Hepatology* 2026** — multi-ancestry GWAS for renal impairment in
decompensated cirrhosis, GWAS for serum creatinine in 3,220 patients.
Sits at the intersection of `Genetic epidemiology → cross/trans-ancestry
portability` and `Biobanks with EHR linkage → EHR-derived clinical
outcomes`. Notable that this single paper triggered seven of the author
feeds this window — the cross-feed frequency is itself a signal that the
paper hits multiple citation neighbourhoods that overlap with `INTERESTS.md`
threads.

**Pharmacoepi / target-trial-emulation cluster (2 items).**
**Hellemans, Chesnaye, Kramer, Fu, Arnol et al. *BMJ* 2026** (Hernán
citations-to feed) — international TTE of deceased-donor kidney
transplantation vs continued dialysis across European Renal Association
Registry data from Catalonia, Denmark, France and two additional
countries/regions, quantifying survival benefit by patient
characteristics (age, diabetes, CVD), donor quality (standard vs
expanded criteria), and donor retrieval type (DBD vs DCD). Directly
serves the `Causal inference & pharmacoepi → TTE` thread; secondarily
touches `APOL1 → kidney disease risk, transplant decision-making`
where donor/recipient stratification interacts with ancestry-modified
transplant risk. **Duarte-García, Sandino-Bermúdez et al. *Arthritis &
Rheumatology* 2026** (Denny citations-to) — TTE of comparative infection-
related hospitalization risk among non-renal SLE patients initiating
azathioprine, belimumab, methotrexate, or mycophenolic-acid analogues
from Optum Labs Data Warehouse claims (2011–2023). Serves the same TTE
thread plus autoimmune drug-safety RWE.

**Composite-risk / PGS methodology cluster (3 items).**
**Bal, Pampana, Nayak, Gaonkar, Patel et al. *Nature Cardiovascular
Research* 2026** (Denny new-related) — multi-ancestry PGS improves
stratification in patients with hypertrophic cardiomyopathy, where
sarcomere-encoding P/LP variants explain only ~1/3 of cases and PGS
adds risk-stratification power. This is the exact composite-risk /
PGS-on-Mendelian design pattern in `INTERESTS.md → Composite risk
models stacking PRS with rare pathogenic variants`, in an EHR-tractable
cardiomyopathy cohort. **Zhang, Zhou, Li, Ryckman, Ray, Scifres et al.
medRxiv 2026 — PRS-CARV** (Montgomery new-related) — summary-statistics
framework integrating annotation-informed rare variants into polygenic-
risk prediction without requiring individual-level sequencing at scale.
Direct hit for the same composite-risk sub-thread and adjacent to the
Baya *AJHG* 2026 "PGS residuals / polygenic-deviation" family already
tracked in `INTERESTS.md`. **Uffelmann & Visscher *bioRxiv* 2026** —
principled conversion from Nagelkerke's R² to liability-scale variance
explained for PGS, adjusted for case-control ascertainment in the test
sample; enables cross-prevalence / cross-ascertainment comparison, a
long-standing pain point in PGS reporting. METHODS-hygiene for
`Genetic epidemiology → PGS`.

**Selection-bias / MR methodology cluster (2 items).**
**Shi, Swanson, Diemer, Gerlovin et al. *medRxiv* 2026** (Bastarache /
Zeng / Denny new-related) — selection bias in Mendelian randomization
studies with adjustment for medication use, worked through the LDL-C ×
lipid-lowering-medication example. Follows the AJE 2026 "Questions
asked and, maybe, answered with MR" (already in the 09-21 report) but
zooms into a concrete cause-of-bias in drug-relevant MR that
`INTERESTS.md → drug-target MR triangulated with observational cohort
estimates` needs to guard against; portable to statin discontinuation
and CFTR-modulator MR designs. **Goel *European Journal of Human
Genetics* 2026** (Bastarache new-related) — editorial "Penetrance,
effect and causal attribution: which number should be reported for
recurrent copy-number variants?" — responds to Goh et al. CNV
counselling and re-frames what "penetrance" means when population-
ascertained CNV carriers are compared to clinically-ascertained ones.
Direct hit for the PheWAS thread's "penetrance under population
screening vs. clinically ascertained cohorts" framing.

**EHR foundation-model & clinical-NLP cluster (3 items).**
**Mehandiratta & Anubhuti *Intelligent Hospital* 2026** — state-of-the-art
review of *Human Digital Twins for Precision Healthcare* (AI + multiscale
biology + clinical decision intelligence), explicitly integrating
foundation-model architectures with EHR-linked longitudinal data
(Ayushman Bharat digital identity + EHR is cited as an example of a
national interoperable substrate). Companion framing to the
Zhang/Ideker/Oermann *Cell* 2026 Digital-Twins consortium reference and
the Noori/Fesser/Zitnik *Cell* 2026 "World models for biomedicine" paper
already tracked in `INTERESTS.md → EHR foundation models → digital-twins
from EHR data`. **Bakr, Garcia-Agundez, Atkison, Rudrapatna et al.
*Journal of Biomedical Informatics* 2026 — MEDAL** (Hripcsak / Denny
new-related) — sequential adapter learning for privacy-preserving
multicenter clinical language models on clinical notes across sites.
Directly serves both `Federated / privacy-preserving EHR causal
analytics` (the Jang et al. 2607.17958 design pattern in `INTERESTS.md`)
and `EHR foundation models → cross-site adaptation`. **Sivaraman,
Turnham, Bonano, Aresh et al. arXiv 2609.19318** (Alsentzer new
articles) — "I Know Where to Look, But Does the LLM?" — charts gaps
between clinical-expert needs and unstructured-data-abstraction tools
for cancer registries. Direct hit for `EHR phenotyping & OMOP → NLP /
LLM extraction from clinical notes for phecode / HPO term assignment`
and for `Knowledge representation in EHRs → NLP-derived representations
from clinical notes`.

**Rare-disease / variant-interpretation / drug-repurposing cluster (4 items).**
**Boßelmann & May *Human Molecular Genetics* 2026** (Karczewski new-related;
also on the 09-21 keyword-feed) — mutation-rate estimates and somatic
variants from cancer improve variant interpretation in epilepsy;
directly serves `Variant interpretation (ACMG/ClinGen)` and the
Ji et al. *Biology* 2026 "somatic contamination of germline scans" QC
layer already tracked. **Vichentijevikj, Mishev & Misheva 2026 —
*GeneResolver*** (Callahan new-related) — traceable hybrid multi-agent
pipeline for etiology-aware gene prioritization in rare-disease
diagnosis, integrating clinical phenotypes, genomic variants,
inheritance patterns and heterogeneous biological evidence with
explicit reasoning traces. Serves `Rare disease → auditable HPO-driven
diagnostic benchmarks` (GraphRareBench / Phen2Gene / LIRICAL /
PhenoGPT2 lineage) *and* `Knowledge graphs & ontologies` — the
"traceable" framing is exactly the audit-log discipline
`INTERESTS.md` wants propagated across HPO-driven benchmarking.
**Lefkowitz, Eisenberg, Huang, Mudunuri et al. 2026** (Zhiyong Lu new
articles) — machine-readable database for genotype-phenotype analyses
in rare diseases using FKTN-related congenital muscular dystrophies as
a prototype for α-dystroglycanopathy ultra-rare disease. Serves
`Rare disease → deep phenotyping for rare-disease diagnosis (HPO-based)`
and `Knowledge representation in EHRs → concept normalization`.
**Perée, Petrov, Tokunaga, Kvasz, Farnir et al. *Nature Communications*
2026** (Denny new-related) — cell-type-specific cis-eQTL analysis in
27 sorted blood populations + 43 intestinal cell types matched to
140 IBD risk loci, prioritising **entrectinib** (ROS1/NTRK inhibitor)
as a repurposing candidate. Direct hit for `Drug repurposing → EHR-
based repurposing signals` combined with `Specific disease threads →
IBD`; also lands as a KG-adjacent explainable-mechanism paper because
it grounds the repurposing hypothesis in cell-type-resolved eQTL
evidence, not opaque link-prediction scores.

---

## Detailed reports

Below, each HIGH item gets a short structured report against `INTERESTS.md`.
Non-HIGH items are listed as METHODS-WATCH or SKIP at the end.

---

### 1. Sanchez, Clària, Galvanin, Aguilar, Layese et al. — *The Lancet Gastroenterology & Hepatology* 2026

**Title.** Genetic variants and the risk of renal impairment in decompensated cirrhosis: a multi-ancestry genome-wide association study.

**Venue / date.** *Lancet Gastroenterology & Hepatology*, 2026 (early
online per Scholar snippet; PIIS2468-1253(26)00217-7).

**Design / cohort.** Multi-ancestry GWAS for **serum creatinine
levels in 3,220 patients with decompensated cirrhosis**. The GWAS
design is stated for creatinine (a continuous kidney-function
biomarker) rather than binary AKI/HRS status, which is methodologically
appropriate given how noisy binary renal-impairment definitions are in
end-stage-liver-disease populations.

**Cross-feed frequency.** Landed on **seven** feeds simultaneously
(Denny, Bastarache, Zeng, Yang, Montgomery, Yuan Luo, Denny-citations-
to). This is a strong "many-neighbourhood" signal for a paper that
sits between hepatology, nephrology and multi-ancestry biobank
methodology.

**Fit against `INTERESTS.md`.**
- `Genetic epidemiology → cross / trans-ancestry portability` —
  primary fit. A multi-ancestry GWAS in a comparatively small
  (n≈3.2k) but phenotypically-deep cohort is where trans-ancestry
  fine-mapping methodology gets tested against sample-size limits.
- `Biobanks with EHR linkage → phenotype validation against
  EHR-derived outcomes` — secondary fit, if the exposure biomarker
  (serum creatinine) is drawn from routine EHR laboratory data;
  worth confirming from full text.
- `Applications to prioritize → drug-safety signal detection` —
  weak tertiary fit; renal-impairment susceptibility loci in
  cirrhosis have obvious implications for nephrotoxic-drug avoidance
  (aminoglycosides, contrast, non-selective beta-blockers) in this
  population.

**What to read for.**
1. How they defined the analysis phenotype (single-value serum
   creatinine, longitudinal trajectory, or eGFR-derived).
2. Whether they used a multi-ancestry meta-analysis method or a
   trans-ancestry fine-mapping approach (MR-MEGA, SuSiEx, PESCA).
3. Whether any signal overlaps known kidney-disease loci (UMOD,
   SHROOM3, APOL1) or hepatology-specific loci (PNPLA3, TM6SF2)
   — the intersection is where the causal story lives.
4. Trans-ancestry PGS transportability — 3,220 samples split by
   ancestry is small for per-ancestry PGS, so if they attempted
   it, it's a stress-test of current methods rather than a
   definitive answer.

**Bucket.** HIGH — multi-ancestry GWAS × EHR-relevant clinical
outcome; also METHODS-WATCH for its trans-ancestry methodology
choices.

---

### 2. Hellemans, Chesnaye, Kramer, Fu, Arnol et al. — *BMJ* 2026

**Title.** Survival benefit of deceased donor kidney transplantation
versus continued dialysis: international target trial emulation.

**Venue / date.** *BMJ*, 2026 (bmj-2026-100624).

**Design / cohort.** **International target trial emulation** using
European Renal Association Registry data from **five countries or
regions** (Catalonia, Denmark, France, plus two additional). Effect
modification examined by (a) patient characteristics — age, diabetes,
cardiovascular disease; (b) donor quality — standard-criteria vs
expanded-criteria donor; and (c) donor retrieval type — donation
after brain death (DBD) vs donation after circulatory death (DCD).

**Fit against `INTERESTS.md`.**
- `Causal inference & pharmacoepi → target trial emulation` —
  primary fit. Multi-country registry TTE with explicit
  effect-modification stratification is what the Hernán-lineage
  TTE framework does best.
- `APOL1 → kidney disease risk, transplant decision-making` —
  secondary fit. Transplant-vs-dialysis TTEs are the operational
  substrate where APOL1 donor / recipient genotyping matters
  most. Worth checking whether donor-recipient ancestry
  interacts with expanded-criteria-donor benefit — the paper
  is unlikely to look at APOL1 directly (European registry data
  don't have genotypes), but the design template is portable.
- `Biobanks with EHR linkage → multi-country registry linkage` —
  tertiary fit; European registry infrastructure is a different
  substrate from AoU / UKB / MVP / BioVU but the design
  discipline is the same.

**What to read for.**
1. Their concrete TTE specification — how they handled the
   time-varying eligibility problem (patients enter the
   waitlist then may or may not receive an offer), and
   whether they used per-protocol vs intention-to-treat
   analogues.
2. Effect modification by expanded-criteria donor and DCD —
   these are the operational levers that expand donor supply
   at some cost; TTE effect estimates directly inform
   allocation policy.
3. Whether they used g-methods / clone-and-censor or
   propensity-based approaches for the sequential-treatment
   assignment.
4. Comparison against the Wolfe et al. 1999 NEJM landmark and
   subsequent updates — do the 2026 magnitudes still hold in
   the modern era of expanded-criteria donors and DCD?

**Bucket.** HIGH — direct hit for TTE thread + transplant-decision
thread that overlaps APOL1.

---

### 3. Bal, Pampana, Nayak, Gaonkar, Patel et al. — *Nature Cardiovascular Research* 2026

**Title.** A multiancestry polygenic risk score improves stratification
in patients with hypertrophic cardiomyopathy.

**Venue / date.** *Nature Cardiovascular Research*, 2026
(s44161-026-00866-8).

**Design / cohort.** Multi-ancestry PGS applied in HCM patients where
sarcomere-encoding pathogenic/likely-pathogenic variants (SARC-HCM-P/LP)
explain only ~1/3 of cases. The framing question: does PGS add
independent stratification value over the traditional Mendelian
classification?

**Fit against `INTERESTS.md`.**
- `Genetic epidemiology → composite risk models stacking PRS with
  rare pathogenic variants` — direct fit, right in the wheelhouse of
  the composite-risk sub-thread. HCM is the canonical Mendelian-plus-
  polygenic disease where the composite-risk story matters clinically
  (ICD implantation, screening cadence for family members).
- `Variant interpretation (ACMG / ClinGen)` — secondary fit; a PGS
  layer changes what a "sarcomere VUS" means when the same patient
  also carries a top-decile HCM PGS.
- `Genetic epidemiology → cross / trans-ancestry portability` —
  the "multiancestry" claim is exactly where recent HCM-PGS work
  has been thin; this is a stress-test.

**What to read for.**
1. Effect size of PGS *within* SARC-P/LP carriers vs *outside* —
   this decides whether PGS re-classifies or merely stratifies.
2. Discrimination and calibration by ancestry; multi-ancestry
   PGS validation is where most claimed advances shrink under
   external validation.
3. Whether the PGS was constructed on non-HCM traits
   (LV wall thickness, LV mass) or on HCM-status GWAS, and
   the sample size behind the underlying GWAS.
4. Downstream clinical implication — do they propose a
   composite-risk score suitable for clinical decision curves,
   or is this an association paper only?

**Bucket.** HIGH — Composite-risk thread, in a Mendelian-plus-
polygenic disease.

---

### 4. Zhang, Zhou, Li, Ryckman, Ray, Scifres et al. — *medRxiv* 2026 — PRS-CARV

**Title.** PRS-CARV: A summary statistics framework for integrating
annotation-informed rare variants to improve polygenic risk prediction.

**Venue / date.** *medRxiv* preprint 2026 (rs-10671954 preprint route).

**Design / method.** PRS-CARV is a **summary-statistics framework**
integrating **annotation-informed rare variants** into PRS
construction, targeting the long-standing limitation that rare-variant
effects are difficult to estimate stably without individual-level
sequencing data.

**Fit against `INTERESTS.md`.**
- `Genetic epidemiology → composite risk models stacking PRS with
  rare pathogenic variants` — direct fit, complementary to the
  Bal et al. HCM paper above but on the *method* side rather than
  the *disease-cohort* side.
- `Genetic epidemiology → PGS residuals / polygenic-deviation
  designs` — adjacent; a well-built rare-variant-augmented PRS
  changes what the "residual" looks like, so the Baya-Souaiaia-
  Vazquez tails-and-residuals taxonomy has to be re-evaluated on
  augmented scores rather than common-variant PRS.

**What to read for.**
1. Whether the framework is truly summary-statistics-only or if
   it needs individual-level rare-variant data for the annotation
   layer; the former is a much bigger deal for downstream users.
2. Annotation strategy — LOFTEE / MPC / gnomAD constraint /
   AlphaMissense — and how they weight annotations without
   over-fitting.
3. Benchmarks against SBayesRC-family and PRS-CS-family methods
   on the same cohorts.
4. Portability across ancestries — annotation-based methods can
   inherit or mitigate ancestry bias depending on the annotation
   set.

**Bucket.** HIGH-METHODS — infrastructure for the composite-risk
thread.

---

### 5. Uffelmann & Visscher — *bioRxiv* 2026

**Title.** From Nagelkerke's R² to Liability-Scale Variance Explained
for Polygenic Scores.

**Venue / date.** *bioRxiv* preprint (2026.09.12.751172), posted
2026-09-17.

**Design / method.** Methodological paper deriving a principled
conversion from Nagelkerke's R² (the widely-mis-used case-control
pseudo-R² for disease-status PGS) to **liability-scale variance
explained**, adjusted for case-control ascertainment in the test
sample.

**Fit against `INTERESTS.md`.**
- `Genetic epidemiology → PGS` — METHODS-hygiene fit. Enables
  cross-prevalence / cross-ascertainment comparison of PGS
  performance, a long-running pain point when PGS studies
  quote incomparable Nagelkerke values.

**What to read for.**
1. Whether the correction is closed-form or requires simulation.
2. How large the correction is at typical case-fractions
   (case:control 1:1 vs 1:10 vs 1:100) — that's how big the
   published-vs-comparable gap is in existing PGS papers.
3. Practical software delivery — does it come as a small R /
   Python package, or is it just a paper.

**Bucket.** METHODS-WATCH-HIGH — cite and use for any future
PGS-benchmarking table.

---

### 6. Shi, Swanson, Diemer, Gerlovin et al. — *medRxiv* 2026

**Title.** Selection bias in Mendelian randomization studies with
adjustment for medication use.

**Venue / date.** *medRxiv* preprint (2026.09.16.26363225).

**Design / method.** MR-methodology paper working through the
concrete case of **LDL-cholesterol MR under widespread lipid-
lowering medication use**. Shows how naive adjustment for
medication use in the exposure model induces selection bias.

**Fit against `INTERESTS.md`.**
- `Causal inference & pharmacoepi → drug-target Mendelian
  randomisation triangulated with observational cohort
  estimates` — direct fit. The Saxby et al. metformin × AAA
  design and the MR-ALasso lineage all depend on the exposure
  MR estimate being unbiased under real-world medication
  patterns; this paper describes exactly where that
  assumption fails.
- `Pharmacogenomic modifiers of medication persistence` —
  secondary fit. If medication use is itself a mediator or
  collider under PGx-modified persistence, MR-with-adjustment
  designs get subtly worse for those patients.
- Portable directly to **CFTR-modulator persistence MR**,
  **statin discontinuation MR** and **HRT persistence MR** —
  all three are on the CF / hormone / PGx sub-threads.

**What to read for.**
1. Their DAG for the selection-bias mechanism — this is what
   travels to statin / HRT / CFTR-modulator MR.
2. The proposed remediation (if any) — e.g., censoring at
   medication start, negative-control-outcomes, or a
   sensitivity-analysis DAG.
3. Whether they empirically re-estimate LDL-C MR effects with
   vs without correction, and how big the shift is.

**Bucket.** HIGH-METHODS — critical reading for any drug-target MR
in `INTERESTS.md`.

---

### 7. Goel — *European Journal of Human Genetics* 2026 (editorial)

**Title.** Penetrance, effect and causal attribution: which number
should be reported for recurrent copy-number variants?

**Venue / date.** *European Journal of Human Genetics* editorial
(s41431-026-02236-1), responding to Goh et al.

**Design / content.** Editorial re-framing what "penetrance" means
for recurrent CNVs — arguing that the naïve population-carrier
proportion (Pr(phenotype | carrier)) is not the right number
when clinical vs population ascertainment differ, and separating
penetrance from effect size and causal attribution.

**Fit against `INTERESTS.md`.**
- `PheWAS / phecode infrastructure → penetrance estimation for
  monogenic variants under population-screening conditions (vs.
  clinically ascertained cohorts)` — direct fit. This editorial
  is the CNV analogue of the exact SNV-penetrance framing
  question that already anchors the PheWAS thread. The
  Wells et al. medRxiv AoU CNV paper from the 09-21 report
  window ("pleiotropic and distributed neuropsychiatric effects
  of neurodevelopmental CNVs") is now sitting in the same
  penetrance-framing conversation.
- `Variant interpretation (ACMG / ClinGen)` — secondary fit;
  ACMG PVS1 / PS3 / PP4 CNV-scoring rules implicitly assume a
  penetrance definition, and this editorial forces that
  definition to be explicit.

**What to read for.**
1. Which of the three numbers (penetrance vs effect vs causal
   attribution) they recommend for clinical counselling — and
   whether that recommendation matches how ClinGen VCEPs
   currently phrase CNV risk in variant-summary reports.
2. Whether they propose a naming convention (e.g., population-
   penetrance vs clinical-penetrance vs attributable-fraction)
   that could be lifted into PheWAS penetrance reporting.

**Bucket.** HIGH — framing paper for the PheWAS penetrance sub-
thread; pairs with Wells et al. AoU CNV paper.

---

### 8. Duarte-García, Sandino-Bermúdez et al. — *Arthritis & Rheumatology* 2026

**Title.** Comparative Safety of Common Immunosuppressant Therapies
in Systemic Lupus Erythematosus: A Target Trial Emulation Study.

**Venue / date.** *Arthritis & Rheumatology* (art.70343), 2026.

**Design / cohort.** TTE emulating comparative infection-related
hospitalization risk in non-renal SLE patients initiating
**azathioprine, belimumab, methotrexate, or mycophenolic-acid
analogues (MPAA)**, from the Optum Labs Data Warehouse claims
March 2011 – September 2023. Excluded prior lupus nephritis and
solid-organ transplant patients.

**Fit against `INTERESTS.md`.**
- `Causal inference & pharmacoepi → target trial emulation` —
  direct fit; standard TTE with active comparators on Optum
  claims data.
- `Specific disease threads → Inflammatory bowel disease
  (autoimmune umbrella)` — adjacent. IBD and SLE share
  immunosuppressant therapy classes (MTX, MPAA, biologics),
  so the design template is portable.

**What to read for.**
1. Concrete active-comparator matching and its balance
   diagnostics.
2. Whether they used a clone-censor-weight approach for
   time-varying treatment or a per-protocol approximation.
3. Whether belimumab (biologic) vs traditional DMARDs
   comparisons hold up after adjustment for indication and
   severity.

**Bucket.** HIGH — TTE cluster + drug-safety thread.

---

### 9. Mehandiratta & Anubhuti — *Intelligent Hospital* 2026

**Title.** Human Digital Twins for Precision Healthcare: A
State-of-the-Art Review of Artificial Intelligence, Multiscale
Biology, and Clinical Decision Intelligence.

**Venue / date.** *Intelligent Hospital*, 2026 (Elsevier;
S305083712600069X).

**Design / content.** State-of-the-art review of human digital
twins integrating AI, multiscale biology, and clinical decision
intelligence, with explicit foundation-model architecture
discussion and EHR-linked longitudinal-data substrates
(Ayushman Bharat Health Account, ABHA, is cited as an example
of a national interoperable digital identity + longitudinal EHR
platform).

**Fit against `INTERESTS.md`.**
- `EHR foundation models → Digital twins from EHR data` —
  direct fit. Companion framing reference to the
  Zhang/Ideker/Oermann *Cell* 2026 International Consortium of
  Digital Twins in Healthcare and Medicine framing paper and
  the Noori/Fesser/Zitnik *Cell* 2026 "World models for
  biomedicine" paper — already tracked in `INTERESTS.md`.
- `Knowledge representation in EHRs → Interoperability
  standards and their representational consequences` —
  adjacent fit; the ABHA example is a non-US national-scale
  interoperability substrate.

**What to read for.**
1. The review's taxonomy of "digital twin" architectures —
  whether they distinguish patient-specific dynamic-simulation
  twins from cohort-level statistical twins from
  foundation-model-derived synthetic-patient twins.
2. Which foundation-model families they cite for the EHR-
  substrate side — CLMBR, MOTOR, MEDS, FEMR, or generic LLMs
  fine-tuned on notes.
3. Whether they surface any evaluation framework that would
  support a fair digital-twin benchmark; the field is currently
  fragmented on evaluation.

**Bucket.** HIGH — Digital-twins sub-thread anchor paper for
this window.

---

### 10. Bakr, Garcia-Agundez, Atkison, Rudrapatna et al. — *J Biomedical Informatics* 2026 — MEDAL

**Title.** MEDAL: Sequential adapter learning for privacy-preserving
multicenter clinical language models.

**Venue / date.** *Journal of Biomedical Informatics*, 2026
(S1532046426001255).

**Design / method.** **MEDAL** = sequential adapter learning to
fine-tune clinical LLMs across multiple sites while preserving
privacy, targeted at multicenter clinical-note reasoning where
data-sharing constraints prevent a central-training approach.

**Fit against `INTERESTS.md`.**
- `Federated / privacy-preserving EHR causal analytics
  (Jang et al. arXiv 2607.17958 design pattern)` — direct fit
  for the cross-site-adaptation angle.
- `EHR foundation models → cross-site adaptation` —
  direct fit.
- `Knowledge representation in EHRs → NLP-derived
  representations from clinical notes → note-code fusion` —
  adjacent fit; adapter-based fine-tuning of clinical LLMs is
  the standard scaffolding for downstream note-code phenotyping.

**What to read for.**
1. Whether the adapters are LoRA-style / prefix-tuning /
   IA³, and whether the sequential order across sites
   matters for downstream performance (catastrophic-
   forgetting question).
2. Which multicenter note corpora they use (MIMIC-IV,
   eICU-CRD, i2b2, N3C, or a private multi-site consortium),
   and whether cross-site transfer is measured or only
   in-domain.
3. Whether they measure downstream *phenotyping* accuracy
   (concept extraction, HPO term assignment, negation) or
   only note-level classification.

**Bucket.** HIGH — Federated-EHR + EHR-FM cluster.

---

### 11. Sivaraman, Turnham, Bonano, Aresh et al. — arXiv 2609.19318

**Title.** "I Know Where to Look," But Does the LLM? Charting the
Gaps Between Clinical Expert Needs and Unstructured Data
Abstraction Tools.

**Venue / date.** arXiv preprint 2609.19318, 2026.

**Design / method.** Clinical data-abstraction — the process of
distilling structured information from patient records — is
positioned as a critical bottleneck for cancer-registry-style
research. Paper charts gaps between what clinical experts *need*
from unstructured-data-abstraction tools and what current
LLM-based information-extraction (IE) systems actually provide.

**Fit against `INTERESTS.md`.**
- `EHR phenotyping & OMOP → NLP / LLM extraction from clinical
  notes for phecode and HPO term assignment` — direct fit.
- `Knowledge representation in EHRs → NLP-derived
  representations from clinical notes` — direct fit; sits
  under "Note-code fusion (notes-augmented phecodes,
  LLM-extracted problems supplementing structured codes)."
- `Applications to prioritize → representation-ablation studies
  that show which representation choice drives downstream
  performance vs. the model architecture` — this is a
  needs-analysis paper rather than an ablation, but it
  informs which ablations matter.

**What to read for.**
1. Their taxonomy of clinical-expert needs — this becomes a
   design spec for phecodeX / HPO extraction pipelines.
2. Which specific gaps they identify — coverage vs precision
   vs traceability vs latency — because each gap suggests a
   different downstream method direction.
3. Whether they demo any prototype tool or the paper is
   primarily an audit / user-study.

**Bucket.** HIGH — Clinical-NLP + knowledge-representation cluster.

---

### 12. Boßelmann & May — *Human Molecular Genetics* 2026

**Title.** Mutation rate estimates and somatic variants from
cancer improve variant interpretation in epilepsy.

**Venue / date.** *Human Molecular Genetics* 2026 (ddag095).
Surfaced on the 09-21 keyword feed and re-surfaced on the 09-22
Karczewski-related feed — consistent hit.

**Design / method.** Uses **cancer-derived somatic mutation-rate
estimates** to inform germline variant interpretation in epilepsy
genes, where many variants alter function in ways that are hard
to predict from sequence alone. Serves as a "priors from a very
large somatic dataset" input to ACMG-style rules.

**Fit against `INTERESTS.md`.**
- `Variant interpretation (ACMG / ClinGen)` — direct fit;
  builds a new evidence layer (PS3-adjacent or a new PVS-
  companion category, depending on framing).
- `CHIP / VEXAS / LOY / somatic mosaicism` — indirect;
  the epilepsy paper flips the direction (somatic → germline
  interpretation) relative to the Ji et al. QC-layer paper
  (somatic contamination *biases* germline scans). Together
  they define both sides of the somatic-germline evidence flow.

**What to read for.**
1. How they estimate the epilepsy-gene-specific mutation
   rate — GENIE, TCGA, ICGC or a bespoke cohort.
2. Whether their rate estimates outperform gnomAD constraint
   for the same purpose (Z-score, o/e).
3. Whether they release a scored table or a scoring API
   that downstream ClinGen VCEPs can adopt.

**Bucket.** HIGH — Variant-interpretation thread.

---

### 13. Vichentijevikj, Mishev & Misheva — 2026 — GeneResolver

**Title.** GeneResolver: A Traceable Hybrid Multi-Agent Pipeline
for Etiology-Aware Gene Prioritization.

**Venue / date.** 2026 (Research Square rs-10915520).

**Design / method.** Rare-disease diagnosis positioned as an
integration problem across clinical phenotypes, genomic variants,
inheritance patterns and heterogeneous biological evidence.
GeneResolver is a **traceable hybrid multi-agent pipeline** that
challenges the single-etiology assumption baked into most
gene-prioritization tools.

**Fit against `INTERESTS.md`.**
- `Rare disease → auditable HPO-driven diagnostic benchmarks
  with separable metrics for ranking vs evidence coverage`
  — direct fit. Companion tool to GraphRareBench / Phen2Gene
  / LIRICAL / Exomiser / PhenoGPT2 lineage, with an
  auditability angle that maps to the
  "22-44% Hit@10 hides ranking-of-confounders" observation
  already in `INTERESTS.md`.
- `Knowledge graphs & ontologies → HPO, SNOMED, biomedical
  KG construction for clinical reasoning` — direct fit; a
  multi-agent pipeline that integrates heterogeneous biological
  evidence is doing KG-style aggregation, whether or not the
  authors call it a KG.
- `EHR foundation models` — tangential; multi-agent LLM
  pipelines share infrastructure with EHR-FM inference stacks.

**What to read for.**
1. Their auditability substrate — do they emit per-step
   evidence citations, or is "traceable" a looser claim?
2. Benchmarking against Phen2Gene / LIRICAL /
   Exomiser / PhenoGPT2 on the same public HPO-driven
   benchmark sets — otherwise the traceability advantage
   is not comparable.
3. Whether they explicitly handle the "multiple etiology
   in one patient" case (dual diagnosis, blended phenotype),
   which is exactly the case single-etiology tools fail on.

**Bucket.** HIGH — Rare-disease diagnostic benchmarks +
KG-adjacent + agentic pipeline.

---

### 14. Lefkowitz, Eisenberg, Huang, Mudunuri et al. — 2026

**Title.** Machine-Readable Database for Genotype-Phenotype
Analyses in Rare Diseases Using FKTN-related Congenital Muscular
Dystrophies as a Prototype.

**Venue / date.** 2026 (Research Square rs-10856264), Zhiyong Lu
new-articles feed.

**Design / method.** Constructs a **machine-readable rare-disease
genotype-phenotype database** using **FKTN-related congenital
muscular dystrophies** (an α-dystroglycanopathy family) as a
prototype. Explicit focus on ultra-rare disorders with
population-dependent prevalence.

**Fit against `INTERESTS.md`.**
- `Rare disease → deep phenotyping for rare-disease diagnosis
  (HPO-based)` — direct fit.
- `Rare disease → data-driven reanalysis of unsolved cases at
  10k+ cohort scale (Uria-Regojo et al. medRxiv 2026 as the
  mid-scale reference)` — adjacent fit; machine-readable
  genotype-phenotype substrates are what makes cohort-scale
  reanalysis feasible.
- `Knowledge representation in EHRs → concept normalization
  and vocabulary mappings` — adjacent fit; a genotype-
  phenotype database implicitly commits to a vocabulary
  (HPO for phenotype, HGVS for genotype, MONDO for
  disorder).

**What to read for.**
1. Whether the "machine-readable" schema is aligned with
   GA4GH Phenopackets or is a custom schema.
2. How they handle allelic heterogeneity within a single
   rare-disease gene family.
3. Whether the substrate is genuinely release-quality
   (versioned, DOI-attached) or a proof-of-concept for a
   future release.

**Bucket.** HIGH — Rare-disease + knowledge-representation cluster.

---

### 15. Perée, Petrov, Tokunaga, Kvasz, Farnir et al. — *Nature Communications* 2026

**Title.** Cell-type specific analyses in blood and gut identify
cis-eQTL matching 140 IBD risk loci and entrectinib as repurposing
candidate.

**Venue / date.** *Nature Communications* 2026 (s41467-026-76672-4).

**Design / method.** Cell-type-resolved cis-eQTL analysis across
**27 sorted blood cell populations + 43 intestinal cell types**,
intersected against **140 IBD GWAS risk loci**, prioritizing
**entrectinib** (a ROS1 / NTRK inhibitor originally approved for
NTRK-fusion cancers) as a **repurposing candidate for IBD**.

**Fit against `INTERESTS.md`.**
- `Drug repurposing → knowledge-graph / GNN approaches with
  *explainable* hypothesis output (path or subgraph rationales
  rather than opaque link-prediction scores)` — strong fit
  despite not being a KG paper: the cell-type-eQTL → GWAS-locus
  → drug-target chain *is* the explainable-path rationale.
- `Specific disease threads → Inflammatory bowel disease` —
  direct disease-thread fit.
- `Drug repurposing → EHR-based repurposing signals mined from
  real-world prescribing and outcomes` — adjacent; the
  entrectinib prediction is exactly the kind of hypothesis
  that becomes testable via TrialGPT-style trial matching or
  EHR-based off-label-use analysis.

**What to read for.**
1. How many of the 140 IBD loci resolved to a single
   candidate causal gene through cell-type-specific eQTL —
   the fraction is the field-comparison number.
2. Whether entrectinib was the single top-ranked candidate
   or one of several, and what the second-tier candidates
   are (those often become the more interesting story).
3. Any negative-control drug they screened against to
   calibrate false positives.

**Bucket.** HIGH — IBD + drug-repurposing + explainable-mechanism
cluster.

---

## METHODS-WATCH (worth noting, not full report)

- **Wen — *International Journal of Biostatistics* 2026**
  "Doubly robust estimation of monotonic survival curves for
  time-varying treatments in observational studies" (Hernán
  citations feed). METHODS-WATCH for TTE longitudinal
  g-computation.
- **Chi, Liu, Yan, Wang, Luo, Su, Jiang et al. — *Genes &
  Diseases* 2026** "Trustworthy AI for disease pathogenesis and
  precision medicine: a disease-agnostic framework from data to
  deployment" (Hernán / Hripcsak citations). METHODS-WATCH for
  ML-for-precision-health scaffolding.
- **Wang, Yan, Chen, Tan, Chen, Lu, Duan et al. — *RMHP*
  2026** — methodological review of deep learning for early
  adverse-event prediction in ICU using EHRs. METHODS-WATCH for
  `Applications to prioritize → adverse-event surveillance`.
- **Wolf, Grapp, Hartmann, Friederich et al. — *European Heart
  Journal — Digital Health* 2026** — systematic review of AI in
  the inpatient heart-failure care pathway. METHODS-WATCH for
  care-pathway integration of prediction models.
- **Chen 2026 UNC dissertation** "Genomic Medicine Translation:
  Evidence Generation for Genomic Risk Assessment, Clinical
  Implementation, and a New Tool for Variant Interpretation"
  (surfaced on the Mendelian-diseases / variant-interpretation /
  rare-diseases keyword feeds simultaneously). Contains
  eMERGE-IV monogenic-plus-polygenic CHD analyses and a new
  noncoding-variant interpretation tool. METHODS-WATCH — worth
  a scan when it appears in published form.
- **Huang 2026 UCLA dissertation** "Metabolic, Neurocognitive,
  and Demographic Determinants of Musculoskeletal Health:
  Evidence from Large-Scale Real-World Data" (All-of-Us +
  Medicare + TriNetX). METHODS-WATCH for
  cross-cohort methodology; substantive content
  (musculoskeletal / osteoporosis) is off-thread.
- **Kim 2026 dissertation** "Geocoding Pipeline Development and
  Data Quality Assessment for Enhancing Precision Medicine
  Research" (AoU pipeline benchmarking). METHODS-WATCH — geocoding
  pipelines are downstream infrastructure for social-determinants-
  of-health work in AoU.
- **Dunkwu 2026 dissertation** "Characterizing the Combined Role
  of Rare and Common Variants for Prostate Cancer Risk". Adjacent
  to composite-risk thread but disease-specific (prostate cancer
  is not a tracked disease).
- **Genin, Herzig, Le Folgoc, Marenne, Blanché et al. — 2026**
  POPGEN reference panel of local ancestry for metropolitan
  France (Karczewski new-related). METHODS-WATCH for
  cross-ancestry portability infrastructure.
- **Sun, Ng, Toh, Lim, Wang, Welton et al. — *medRxiv* 2026** —
  East-Asian Parkinson's disease WGS identifying novel
  susceptibility loci and functional regulatory variation
  (Karczewski new-related). METHODS-WATCH for cross-ancestry
  GWAS; disease off-thread.
- **Wang, Zeng, Chen, Hu, Hu, Xie, Du et al. — *Human
  Reproduction Open* 2026** — context-specific evaluation of
  polygenic embryo screening (PES) in best-prognosis PGT cycles
  (Denny new-related). METHODS-WATCH; PES is a high-stakes but
  ethically fraught PGS application — track if the field's
  reporting standards firm up.
- **Zheng, Shivakumar, Shen, Kim — *medRxiv* 2026** —
  "Absorption and Co-expression Modules Show Where Polygenic and
  Proteomic Risk Scores Diverge in Neurodegenerative Diseases"
  (Denny new-related). METHODS-WATCH for multi-omics-augmented
  PRS in `INTERESTS.md`.
- **Chen, Wang, Krockenberger, Tyebally, Berg et al. —
  *Nature* 2026** — "Cell-type-specific eQTLs underlie the
  genetic architecture of complex traits" (Denny new-related).
  METHODS-WATCH for eQTL infrastructure; complements Perée et
  al. above.
- **Hu, Byrne, Bidel, Xiao, Zhao, Dehghan et al. — *Hypertension*
  2026** — drug-target MR for antihypertensive-drug repurposing
  in MAFLD (Denny citations + Bastarache citations). Adjacent to
  drug-target-MR sub-thread; disease off-thread.
- **Spiero, Damen, Hooft, Moons et al. — 2026** — Pretrained
  LMs for cohort selection from EHRs and downstream effect on
  prognostic-model performance (Hripcsak citations). Adjacent
  to `Knowledge representation in EHRs → representation
  choices that leak or preserve label information at
  prediction time`.
- **Lautman, Chang, Rangan, Hittle, Uwakwe et al. — *IEEE
  JBHI* 2026** — Interpretable workflow for cohort phenotyping
  using longitudinal wearable data (Michael Snyder new
  articles). Adjacent to `Chronic disease clustering and
  multimorbidity` where wearable-derived phenotypes stack with
  EHR-derived ones.
- **Park, Kwak, Kim, Kim, Hwang, Ryu et al. — *BMC Medical
  Genomics* 2026** — SETD5-related disorders HPO-based
  clinical / genotypic characterization (Kai Wang new-related).
  Adjacent to rare-disease HPO thread; specific-gene study.
- **Henry, Pekkola Pacheco, Duba, Burstedt et al. — *Epilepsia*
  2026** — biallelic RNU2-2 developmental / epileptic
  encephalopathy characterization (Montgomery new-related).
  Adjacent to rare-disease WGS-solved-case reporting.
- **Lekka, Ambrodji, Nater, Ballah, Amstutz et al. — *npj
  Genomic Medicine* 2026** — Cas9-directed long-read
  sequencing for the CES1 PGx locus (Montgomery new-related).
  Adjacent to `Pharmacogenomic modifiers of medication
  persistence` where CES1 metabolizes clopidogrel, methylphenidate
  and others.

## SKIP (recorded so they are not re-surfaced)

- Local `arxiv-digest` 09-22: PACE (tabular FM upstream primitive
  — generic), tteICE R package (methods-adjacent but not
  drug/EHR-linked), Charpentier & Barry pooling / profiling
  (insurance, "motor" keyword misfire — SKIP).
- All `"knowledge graph"` 09-22 keyword-feed hits — enterprise
  KG, ML-resource KG, cybersecurity KG, construction KG, cultural-
  landscape KG. Consistent with the `INTERESTS.md` note that
  interest in non-biomedical KG infrastructure is LOW.
- `"UK Biobank"` active-commuting × biological-aging (Wang et al.
  J Transp Health). LOW — physical-activity epi rather than the
  UKB-with-genomics angle.
- `"drug repurposing"` structure-based VAV2 / atherosclerosis
  virtual-screening (Bansal & Srivastava). Purely chemistry
  pipeline without a clinical-evidence loop, which
  `INTERESTS.md` explicitly de-prioritizes.
- Marinka Zitnik / Peter Szolovits / Zhiyong Lu new-related items
  on LLM long-context / KV-cache / attention infrastructure
  (Ho et al. arXiv, Xie et al. HeadWiseKV, Cao et al. stream
  stability, Shao et al. multilingual unlearning). LM-infra,
  not clinical.
- Kastner citations (autoinflammatory case reports, NLRP-family
  reviews). Off-thread this window unless we re-open an
  autoinflammatory sub-thread.
- Neil M Davies, Bryan Traynor, David Baker, Leo Anthony Celi,
  Pascal Brandt items — no new HIGH-thread hits this window.

---

## Cross-reference to `INTERESTS.md` sub-threads

| Sub-thread | HIGH items this window |
| --- | --- |
| PheWAS / phecode infrastructure — penetrance under population vs clinical ascertainment | Goel EJHG editorial (#7) |
| Biobanks with EHR linkage | Sanchez Lancet cirrhosis GWAS (#1); Hellemans BMJ TTE (#2) |
| EHR phenotyping & OMOP — LLM extraction | Sivaraman arXiv (#11) |
| Causal inference & pharmacoepi — TTE | Hellemans BMJ (#2); Duarte-García SLE TTE (#8) |
| Causal inference & pharmacoepi — drug-target MR | Shi/Swanson/Diemer selection bias medRxiv (#6) |
| Variant interpretation (ACMG / ClinGen) | Boßelmann & May HMG (#12); Goel EJHG (#7) |
| Genetic epidemiology — composite risk PGS × rare | Bal HCM Nat Cardiovasc Res (#3); Zhang PRS-CARV (#4) |
| Genetic epidemiology — PGS methodology | Uffelmann & Visscher bioRxiv (#5) |
| Genetic epidemiology — cross / trans-ancestry portability | Sanchez Lancet cirrhosis GWAS (#1); Bal HCM (#3) |
| EHR foundation models — Digital twins | Mehandiratta Intelligent Hospital review (#9) |
| EHR foundation models — federated / cross-site | Bakr MEDAL (#10) |
| Knowledge representation in EHRs | Sivaraman arXiv (#11); Bakr MEDAL (#10); Lefkowitz FKTN db (#14) |
| Knowledge graphs & ontologies | Vichentijevikj GeneResolver (#13) |
| Drug repurposing | Perée IBD Nat Commun eQTL entrectinib (#15) |
| Rare disease — auditable HPO benchmarks | Vichentijevikj GeneResolver (#13) |
| Rare disease — deep phenotyping | Lefkowitz FKTN db (#14) |
| Specific disease — IBD | Perée Nat Commun (#15) |
| Specific disease — APOL1 / kidney / transplant | Hellemans BMJ (#2, adjacent) |
| ML for precision health | Chi Genes & Diseases (METHODS-WATCH) |

---

## Notes / caveats / follow-ups

- The 09-22 batch drove ~40 individual author-feed emails and
  ~11 keyword-feed emails; this report reads the highest-
  frequency-across-feeds items in full and samples the rest.
  The single Sanchez et al. cirrhosis paper appeared in seven
  author feeds — a strong "many-neighborhood" signal that this
  paper's citation network sits across hepatology-nephrology-
  biobank-genetics topics simultaneously.
- Two paper appear on both an author-feed AND a keyword-feed:
  Boßelmann & May (Karczewski + variant-interpretation keyword)
  and the J. Chen 2026 UNC dissertation (Mendelian-diseases +
  variant-interpretation + rare-diseases keyword feeds).
- No new arxiv-digest GitHub notifications in the window — the
  daily-cron pipeline commits its output to this repo rather
  than emailing, as noted in the prior report. The 2026-09-23
  daily digest file will be produced by the 10:30 UTC cron
  today; anything caught there will land in the next report
  window.
- Two dissertations (Chen UNC, Huang UCLA) surfaced this window;
  usually promoted to HIGH only once they appear as peer-
  reviewed papers, but noted under METHODS-WATCH to keep the
  scent.
- The Sanchez cirrhosis GWAS + Hellemans transplant TTE +
  Perée IBD eQTL papers together form a
  nephrology-hepatology-gastroenterology mini-cluster; worth
  noting if these three intersect any active analysis project
  (e.g., APOL1 × cirrhosis-related renal failure would put all
  three in the same design conversation).
