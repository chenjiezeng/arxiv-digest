# Research digest report — 2026-09-05

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-05 12:00Z** (~4 days since the last
research-digest report, covering four `arxiv-digest` cron runs and four
Google Scholar alert batches plus daily openRxiv, JAMA Network, and My
NCBI feeds).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-04.md`) | 09-01 → 09-04 daily crons | 4 daily runs, low volume. 09-01: 1 paper (Mansouri Ghiasi storage-centric genomic analysis; SKIP — cs.AR hardware dissertation, only "precision medicine" keyword hit). 09-02: 1 paper (Ramesh et al. mudskipper locomotion; SKIP — "motor" false-positive). 09-03: 0 papers (2 previously surfaced, suppressed). 09-04: 2 papers (Cortez-Rodriguez natural-disaster nonprofit sector panel-data causal inference, off-topic domain but METHODS-WATCH for panel-data causal design; Yu et al. arXiv 2609.04018 location-invariant extremal quantile treatment effect estimator with IPW — METHODS-WATCH for the extreme-tail HTE work Leimenstoll flagged on 08-25). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads. The pipeline commits to the repo directly (no PR / cron-failure emails triggered), so the on-disk digests remain the arxiv-digest feed. |
| Google Scholar alerts (09-04 batch, 21:26Z + 16:08Z) | 09-04 | Double batch, ~30 feeds fired. Keyword feeds: `variant interpretation OR classification`, `rare diseases`, `drug repurposing`, `electronic health records`, `knowledge graph`, `Foundation models + EHR`, `All of Us research program`, `UK Biobank`, `mendelian diseases`, `APOL1`, `intitle:"clonal hematopoiesis"`, `autoimmune`. Author feeds: Bastarache (×2 — new articles + citations-to), Hripcsak (×2), Denny, Hernán, Karczewski (×2), Montgomery (×2), Zitnik, Callahan, Zhiyong Lu, Chenjie Zeng, Peter Szolovits, Yuan Luo, Jian Yang, Patrick Ryan, Kai Wang, Kastner, Pritchard, Capra, Celi. Multiple papers surfaced across ≥3 feeds (Hu et al. NatCom PRS boosting hit 5+; Park et al. Translational Psychiatry OCD-PGS cross-ancestry hit 4+; DeVito & Gymrek NatCom GxE hit ≥3). |
| Google Scholar alerts (09-03 batch, 13:02Z) | 09-03 | ~10 keyword feeds fired: `variant interpretation` (Kırboğa CYP2C9/CYP2C19/NUDT15 DMS), `mendelian diseases`, `electronic health records`, `knowledge graph`, `UK Biobank` (Luo MR selection-bias in BMI/education/CRP → depression), `rare diseases`, `intitle:"clonal hematopoiesis"` (Yao et al. CHIP–ASCVD mechanistic review), `drug repurposing`, `Foundation models + EHR`. |
| Google Scholar alerts (09-02 batch) | 09-02 | Low volume; no unique HIGH surfaces distinct from the 09-01 report or the 09-03/04 batches below. |
| openRxiv (bioRxiv + medRxiv) | 09-01 → 09-05 | 10 daily collection digests (Bioinformatics/Genetics/Genomics/Immunology/Pathology on bioRxiv; Endocrinology/Genetic and Genomic Medicine/Health Informatics on medRxiv). No standout HIGH items distinct from Scholar. |
| JAMA Network (Online First + Network Open) | 09-01 → 09-04 | 9 issues. Non-triage topics (ESC Congress commentary, dementia prevention, phages/UTIs, colorectal cancer trends, Dapagliflozin AKI post-cardiac-surgery, e-cigarettes for smoking cessation, high-dose vitamin D3 CRC). Nothing HIGH matched. |
| My NCBI PubMed alerts | 09-02–04 | 6 alerts (AoU / UKB / drug-repurposing). Full overlap with the Scholar HIGH set below. |
| Direct / collaborator email | — | Zero direct research/manuscript/grant emails from named collaborators in the window. Non-newsletter email was commercial (Perplexity billing, LinkedIn, Meta, Redivis product update, OpenEvidence). |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Nineteen HIGH items surfaced this window, clustering into six knots:

**Pharmacoepi target-trial-emulation cluster (2 items).** Zhang et al.
*Diabetes, Obesity & Metabolism* 2026 (Yong Chen group) — head-to-head
GLP-1 RA vs. SGLT2i vs. DPP4i cardiovascular-outcomes TTE with
**empirical calibration**; direct-hit for the GLP-1 / SGLT2 drug thread
and for your standing emphasis on negative-control distributional
diagnosis in TTE. (The 09-01 report noted a Zhang et al. head-to-head
TTE from the Hripcsak feed; the new alert cycle now attributes it more
clearly to Yong Chen's team, same paper.) Paired with Zhou et al.
*Nature Mental Health* 2026 — 706,414-patient nationwide Dutch-register
new-user cohort of antihypertensive initiation stratified by ADHD
status, with **long-term cardiorenal disease trajectories** as the
outcome. The trajectory-as-outcome framing is a template for HTE-by-
comorbidity work that maps directly onto the GLP-1/SGLT2 persistence
sub-thread you flagged.

**Genetic epi / PRS composite-risk cluster (5 items).** Hu et al.
*Nature Communications* 2026 — **pre-train and fine-tune framework for
adaptive boosting of pre-trained PRS**, surfaced simultaneously on five
author feeds (Denny, Bastarache, Hripcsak, Karczewski, Yong Chen, Yuan
Luo); the pattern imports the CLMBR/MOTOR foundation-model paradigm
into PRS territory and is likely to become a baseline everywhere.
Lassen, Venkatesh, **Baya**, Lindgren et al. *Nature Communications*
2026 — biobank-scale **deviations from genetic additivity driven by
rare variants**, extending the Baya-lineage "misaligned individuals"
polygenic-deviation framing you noted in INTERESTS.md into
rare-variant non-additive territory. DeVito & Gymrek *Nature
Communications* 2026 — **nonlinear GxE + spatiotemporal interactions**
for complex-trait prediction, reinforcing the Nagpal & Gibson
"pervasive PGS × exposure" framing under `Genetic epi (GxE / PGS ×
exposure)`. Park et al. *Translational Psychiatry* 2026 (surfaced on
four author feeds — Karczewski, Chenjie Zeng, Bastarache, Denny) —
**cross-ancestry AND cross-disorder PGS transferability for OCD**;
serves both the portability and cross-trait multi-trait triangulation
sub-threads. Zheng et al. medRxiv 2026 — **absorption + co-expression
modules highlight where PRS and proteomic risk scores diverge in
neurodegeneration**; extends the multi-omics-augmented-PRS sub-thread
with an interpretability angle.

**EHR phenotyping / knowledge-representation cluster (3 items).** Chin,
Mester, Tozzo et al. (Bastarache group), *Journal of Human Immunity*
2026 — **temporal windowing of recurrent sinusitis improves EHR-based
immunodeficiency classification**; a concrete demonstration that
visit-window aggregation changes case definitions, directly
transferable to phecode/PheRS episode-counting for other recurrent
conditions (UTIs, DVTs, otitis media, exacerbations). Fits the
`Structural and temporal representation of the patient timeline`
sub-thread of `Knowledge representation in EHRs`. Wu et al. arXiv 2026
— **auditable CT phenotyping through report-derived radiological
observations**, testing whether medical-image FMs read disease-specific
findings or shortcuts; the imaging-FM analogue of the scContam /
MIA-scFM audits and a fit for both `Fidelity, portability, and audit
of representations` and `NLP-derived representations from clinical
notes`. Du et al. arXiv 2026 (Hripcsak cite) — **explainable
transformer models for clinical prediction on structured EHRs**; a
CLMBR/MOTOR-neighbor with an explicit explainability layer worth
checking for representation-ablation signals.

**Disease-thread hits (3 items).** Alasfar et al. *Transplantation*
2026 abstract P4.810 — **donor APOL1 high-risk genotype with second-hit
De Novo collapsing FSGS in two transplant recipients**; direct-hit
casework for the APOL1 transplant-decision-making sub-thread. Galderisi
et al. 2026 (Ryan cite) — **CGM to track metabolic changes in youths
with CF before and after ETI initiation**; direct pre/post-ETI
real-world outcome with a continuous biomarker for the CFTR-modulator
pharmacoepi thread, and a natural companion to the
pharmacogenomic-modifier-of-persistence sub-thread. Skovbo, Hallas,
Stubbe, **Sabater-Lleal** et al. 2026 — **drug repurposing signals for
abdominal aortic aneurysms** from real-world prescribing; direct
comparator to the Saxby metformin × AAA MR triangulation you noted in
INTERESTS.md, now approached from the observational-cohort end.

**Biobank / population-cohort infrastructure (3 items).** Zhang,
Folarin, Zhong et al. arXiv 2608.06063 — **longitudinal wearable
monitoring + polygenic risk for incident MDD in the All of Us Research
Program**; the AoU-scale wearable-augmented PRS composite you've been
watching (Gerstein-lab ABCD template applied at AoU scale). Zhang et
al. 2026 — **explainable plasma-proteomics ML for osteoporosis in the
UK Biobank**; UKB Olink + explainable ML for a chronic-disease
diagnosis/prognosis endpoint, template for the multi-omics-PRS
composite designs. Jing, Yan, Zhang & Zhao *Trends in Genetics* 2026 —
**timely review of large-scale human population cohorts**; useful
canonical citation for AoU/UKB/MVP/BioVU comparisons.

**Variant interpretation & rare-disease diagnostic tooling (3
items).** Kırboğa 2026 in *G3* — **DMS of CYP2C9, CYP2C19, NUDT15**
demonstrating that pharmacogene variant interpretation requires
assay-specific functional data; directly informs
pharmacogenomic-modifier-of-persistence analyses (CYP2C19-clopidogrel/
PPI, NUDT15-thiopurine, CYP2C9-warfarin/NSAIDs). Boceck, Laugwitz,
Sturm et al. *npj Genomic Medicine* 2026 — **aiDIVA hybrid
evidence-based/ML/LLM rare-disease diagnostic pipeline**, a candidate
to run through the GraphRareBench "ranking-vs-evidence-coverage" audit
lens you added in the 07-29 INTERESTS.md update. Fang, Li, Noori,
Fesser, Zitnik preprint 2026 — **"Closing the Loop in AI-Driven
Biomedical Discovery"**; the drug-repurposing / hypothesis-loop
analogue of the OCI-agent pattern under `Agentic / human-in-the-loop
observational-causal-inference pipelines`.

---

## Detailed reports

### 1. Chin, Mester, Tozzo, Stephens et al. — *Journal of Human Immunity* 2026

**Threads:** PheWAS/phecode infrastructure; EHR phenotyping & OMOP;
Knowledge representation in EHRs (structural/temporal timeline
sub-thread).

**Bucket:** HIGH.

**What it is (from snippet):** "Recurrent sinopulmonary infections are
a hallmark of common variable immunodeficiency (CVID), yet electronic
health records (EHR) struggle to distinguish multiple discrete
infections from a single infection comprising multiple clinic visits…"
Temporal windowing of recurrent sinusitis to improve EHR-based
immunodeficiency classification — a Bastarache-group phenotyping paper.

**Why it matters to your threads:** This is a concrete
methods-on-representation paper: choosing a visit-window aggregation
rule for what counts as "one infection" is exactly the kind of
representation choice you flagged as gap-worthy under `Structural and
temporal representation of the patient timeline`. The lever
generalizes trivially to recurrent-UTI, recurrent-otitis-media,
DVT-vs-recurrent-VTE, and CF-exacerbation phenotypes — all
episode-count-sensitive phecodes where a naive count of visit rows
mislabels chronic patients as multi-episode acute patients. Worth
reading with an eye to porting the windowing rule into your
phers/PheRS pipeline, and to citing when arguing that
representation-choice ablations matter as much as model choice for
biobank phenotyping.

### 2. Zhang, Folarin, Zhong et al. — arXiv 2608.06063 (AoU + wearables + PRS for MDD)

**Threads:** All of Us biobank + EHR linkage; Genetic epi / PRS
(composite / multi-modal); Digital twins from EHR data.

**Bucket:** HIGH.

**What it is (from snippet):** Integration of AoU genomic data
(polygenic score for MDD) with longitudinal wearable behavioral data
to predict incident major depressive disorder. Explicit design goal:
combine "stable inherited liability and dynamic behavioral patterns"
with long-term objective data in a real-world setting.

**Why it matters to your threads:** This is the AoU-scale realization
of the wearable-digital-phenotype × PGS composite you flagged in the
Gerstein-lab ABCD sub-thread. It also fits `Digital twins from EHR
data` because the wearable component supplies the individualized
longitudinal trajectory that pure EHR-FM digital-twins currently miss.
Directly portable to CFTR-modulator persistence (activity trajectories
around ETI initiation), GLP-1 RA weight/activity trajectories, and
statin discontinuation contexts if AoU Fitbit coverage overlaps.

### 3. Lassen, Venkatesh, Baya, Lindgren et al. — *Nature Communications* 2026

**Threads:** Genetic epidemiology (PGS residuals / polygenic-deviation
designs); UK Biobank; Composite risk models stacking PRS with rare
pathogenic variants.

**Bucket:** HIGH.

**What it is (from snippet):** "Additive genetic models are the default
for genome-wide association studies, but deviations from additivity
are crucial for understanding disease mechanisms and therapeutic
responses… We use an orthogonal allelic recoding framework that
enables scalable testing of nonadditive [effects]…" Rare-variant
non-additive scan at biobank scale.

**Why it matters to your threads:** Baya-lineage paper that pairs with
the AJHG 2026 "misaligned individuals" framing you flagged as a
PGS-tails-and-residuals discovery instrument. Where the AJHG paper
uses PGS-residual outliers as a discovery lever, this one attacks the
same "where does the additive model fail?" question directly through
non-additive rare-variant effects. Together the two form a taxonomy of
"how additive-model failure surfaces a discovery signal": one from the
polygenic side, one from the rare-variant side. For your composite
risk work, this justifies including dominance / recessivity terms in
the rare-variant burden layer instead of only additive dosage.

### 4. Fang, Li, Noori, Fesser, Zitnik — Preprint 2026 ("Closing the Loop in AI-Driven Biomedical Discovery")

**Threads:** Causal inference & pharmacoepi (agentic /
human-in-the-loop pipelines); Drug repurposing.

**Bucket:** HIGH.

**What it is (from snippet):** Framing paper on autonomous
hypothesis-experiment-analysis loops in biomedical discovery, with
explicit attention to what breaks when the loop is closed end-to-end
by AI agents. Zitnik-lab authored.

**Why it matters to your threads:** This is the drug-discovery-side
counterpart of the OCI-agent pattern (Chou/Kallus arXiv 2607.22443)
under your `Agentic / human-in-the-loop observational-causal-inference
pipelines` sub-thread. For your KG/GNN drug-repurposing work with
explainable-rationale outputs, this is the field-level framing paper
to cite when arguing that agentic proposal-generation should feed
back through a human-in-the-loop assumption-check gate rather than
straight into wet-lab prioritization.

### 5. Zhang, Zhou, Tang, Lu, Zhang, Chen et al. — *Diabetes, Obesity & Metabolism* 2026 (three-way GLP-1/SGLT2/DPP4 TTE)

**Threads:** Causal inference & pharmacoepi (GLP-1 RAs, SGLT2is, TTE,
negative-control calibration).

**Bucket:** HIGH.

**What it is:** Head-to-head three-way target trial emulation
comparing GLP-1 RAs, SGLT2 inhibitors, and DPP4 inhibitors for
cardiovascular outcomes in type 2 diabetes, with **empirical
calibration by negative controls**.

**Why it matters to your threads:** Direct-hit for the GLP-1 / SGLT2
drug thread. Also serves as a reference exemplar of the Suchard/Ryan
empirical-calibration TTE workflow with negative controls for
distributional diagnosis — reinforced by the Bots et al. IJE 2026
negative-controls guidance paper listed under METHODS-WATCH below.
Same paper was flagged on the Hripcsak feed in the 09-01 report; the
new alert cycle now attributes it more clearly to Yong Chen's team.

### 6. Zhou, Postmus, Li, van Lammeren et al. — *Nature Mental Health* 2026

**Threads:** Causal inference & pharmacoepi; Chronic disease
clustering / multimorbidity (trajectories); ML for precision health.

**Bucket:** HIGH.

**What it is (from snippet):** "…nationwide retrospective cohort study
using Dutch register data, we included 706,414 new users… of
antihypertensive medications without prior cardiovascular disease or
chronic kidney disease…" Long-term cardiorenal disease trajectories
stratified by ADHD comorbidity.

**Why it matters to your threads:** New-user design at 700k scale with
disease-trajectory outcomes is a canonical pattern that transfers
directly onto GLP-1 / SGLT2 persistence and cardiorenal-trajectory
work. The ADHD-stratified HTE angle is the multimorbidity-modifier
framing you flagged under `Chronic disease clustering and
multimorbidity`. Worth reading to see how they defined trajectory
clusters (LCTA / LCMM vs. topic-model / trajectory-KG-embedding
alternatives) and whether the trajectory endpoint absorbs the usual
composite-CV endpoint concerns.

### 7. Galderisi, Marchiori, Weiss et al. — 2026 (CGM tracking metabolic changes in CF youth on ETI)

**Threads:** CFTR modulator pharmacoepi (real-world outcomes); ML for
precision health.

**Bucket:** HIGH.

**What it is:** Continuous glucose monitoring to track metabolic
changes in youths with cystic fibrosis before and after initiation of
elexacaftor / tezacaftor / ivacaftor (ETI, Trikafta).

**Why it matters to your threads:** Direct pre/post-ETI real-world
outcome study with a **continuous biomarker** (CGM-derived glycemic
metrics) rather than a coarse phecode endpoint. This is the kind of
outcome-resolution upgrade you want on the CFTR-modulator side
because CFRD (CF-related diabetes) is a mid-latency ETI outcome
where discrete diagnosis codes lag the underlying biology by
years. Also directly feeds the pharmacogenomic-modifier-of-persistence
sub-thread: CGM-derived glucose trajectories can serve as an early
"metabolic response" phenotype whose modifier discovery is more
tractable than late-phecode CFRD.

### 8. Alasfar, Alanzi, Cho, Sridhara, Me Me, Fu et al. — *Transplantation* 2026 (P4.810)

**Threads:** APOL1 (kidney disease risk, transplant decision-making,
ancestry considerations).

**Bucket:** HIGH.

**What it is:** Two-case series of donor APOL1 high-risk-genotype
kidneys developing de novo collapsing FSGS in recipients, with
second-hit contributions to graft failure.

**Why it matters to your threads:** This is exactly the transplant
decision-making evidence base you're tracking under APOL1. Case series
of this specificity are the empirical raw material for
donor-genotype-informed allocation policy, and for the "APOL1 second
hit" mechanism versus environmental / recipient-side contribution
debate. Worth pulling to compare with the APOL1-LT trial recipient-
genotyping arm.

### 9. Skovbo, Hallas, Stubbe, Sabater-Lleal et al. — 2026 (drug repurposing signals for AAA)

**Threads:** Drug repurposing (EHR-based / real-world prescribing);
Causal inference & pharmacoepi.

**Bucket:** HIGH.

**What it is (from snippet):** "Objective: Drug repurposing offers a
cost-effective approach…" Real-world drug-repurposing scan for
abdominal aortic aneurysms from prescribing and outcomes data.

**Why it matters to your threads:** Direct comparator to the Saxby et
al. metformin × AAA drug-target Mendelian-randomisation triangulation
you flagged under `Drug-target Mendelian randomisation triangulated
with observational cohort estimates`. This provides the
observational-cohort leg of the triangulation. Reading the two side
by side is the exemplar of how MR + real-world prescribing converge
(or diverge) on a repurposing hypothesis — a template you can port to
CFTR-modulator repurposing, GLP-1 RA repurposing beyond diabetes, and
statin repurposing.

### 10. Kırboğa — *G3: Genes, Genomes, Genetics* 2026 (DMS of CYP2C9, CYP2C19, NUDT15)

**Threads:** Variant interpretation (ACMG / ClinGen); Pharmacogenomic
modifiers of medication persistence.

**Bucket:** HIGH.

**What it is:** Deep mutational scanning of CYP2C9, CYP2C19, and NUDT15
showing that pharmacogene variant interpretation requires
**assay-specific functional data**.

**Why it matters to your threads:** This closes a real gap you flagged
under `Pharmacogenomic modifiers of medication persistence`. DMS data
transferable to the CYP2C19-clopidogrel/PPI persistence axis,
NUDT15-thiopurine tolerance, and CYP2C9-warfarin/NSAID interactions.
The "assay-specific" caveat is critical for how you build PGx
metabolizer-phenotype covariates in persistence analyses — using a
mismatched assay's functional annotation can flip
poor-metabolizer classifications for a subset of variants.

### 11. Boceck, Laugwitz, Sturm, Bezdan, Gschwind et al. — *npj Genomic Medicine* 2026 (aiDIVA)

**Threads:** Rare disease (auditable HPO diagnostic benchmarks);
Variant interpretation.

**Bucket:** HIGH.

**What it is:** Hybrid rules + ML + LLM diagnostic pipeline for rare
disease using evidence-based scoring, machine learning, and language
models. Genome-diagnostic tool paper.

**Why it matters to your threads:** aiDIVA is the exact kind of hybrid
pipeline you flagged as a candidate for the GraphRareBench audit lens
(Guo et al. arXiv 2607.24878) — where Hit@10 hides the ranking of
confounders. Worth running through the "ranking vs. evidence-coverage"
audit and comparing against Phenolyzer, Phen2Gene, PhenoSV, LIRICAL,
Exomiser, PhenoGPT2. Also cross-cite when arguing for auditable rare-
disease diagnostic benchmarks.

### 12. DeVito & Gymrek — *Nature Communications* 2026 (nonlinear + GxE for complex traits)

**Threads:** Genetic epi (GxE / PGS × exposure); ML for precision
health.

**Bucket:** HIGH.

**What it is (from snippet):** "Adjusting for [nonlinear and
interaction effects of spatiotemporal and nongenetic factors] improves
prediction for complex traits…" Explicit modeling of nonlinear +
interaction effects between genetic and spatiotemporal/nongenetic
factors.

**Why it matters to your threads:** Directly reinforces the Nagpal &
Gibson "pervasive PGS × exposure interactions" framing under `GxE and
PGS × exposure / environment interactions`. Especially useful as
methodological support when arguing that PGS portability is
inseparable from GxE — an interaction with unmeasured environment is
observationally equivalent to reduced portability across sites /
ancestries with different environmental distributions.

### 13. Hu, Chen, Salvatore, Wu, Ozdemir, Lu et al. — *Nature Communications* 2026 (adaptive boosting of pre-trained PRS)

**Threads:** Genetic epi / PRS; Biobanks with EHR linkage.

**Bucket:** HIGH.

**What it is:** Pre-train and fine-tune framework for adaptive
boosting of pre-trained polygenic risk scores. Surfaced on 5+ author
feeds (Denny, Bastarache, Hripcsak, Karczewski, Yong Chen, Yuan Luo)
in the 09-04 batch alone.

**Why it matters to your threads:** The CLMBR/MOTOR pretrain-then-fine-
tune paradigm imported into PRS territory. Likely to become a
standard baseline for cross-ancestry PRS transfer, and for
site-specific fine-tuning of a UKB-pretrained PRS on
AoU/MVP/BioVU. Worth pulling to see whether the boosting layer
respects the PGS-residuals discovery structure (Baya et al.) or
washes it out — a real risk if the fine-tune step over-corrects
"misaligned individuals" toward the average.

### 14. Park, Kim, Myung, Jung, Kim, Park et al. — *Translational Psychiatry* 2026 (cross-ancestry + cross-disorder PGS for OCD)

**Threads:** Genetic epi (cross-ancestry PGS portability); Cross-trait
shared genetic architecture.

**Bucket:** HIGH.

**What it is:** Cross-ancestry AND cross-disorder transferability of
polygenic risk scores for obsessive-compulsive disorder. Surfaced on
four author feeds this cycle (Karczewski, Chenjie Zeng, Bastarache,
Denny).

**Why it matters to your threads:** Feeds both `cross / trans-ancestry
portability` and `Cross-trait shared genetic architecture and
multi-trait triangulation` in one paper. The fact that it hit four
separate author feeds means it is being read widely across your
community — worth knowing what its cross-disorder anchor set is, so
you can position your own OCD/anxiety cross-trait work relative to
it.

### 15. Zheng, Shivakumar, Shen, Kim — medRxiv 2026 (PRS vs. proteomic risk divergence in neurodegeneration)

**Threads:** Multi-omics-augmented PRS; ML for precision health.

**Bucket:** HIGH.

**What it is:** Absorption and co-expression modules highlight where
polygenic and proteomic risk scores diverge in neurodegenerative
diseases.

**Why it matters to your threads:** Explicit **divergence analysis**
between PRS and proteomic scores is the interpretability half of the
multi-omics-PRS sub-thread — the flip side of Shan et al. UKB 2026
"stacked PRS + Olink" work. Divergence is where the two layers carry
complementary information; convergence is where the proteomic score
is a mediator of PRS. The distinction is directly relevant to whether
PRS + proteomics composite is worth building for any given trait, or
whether one collapses into the other. Portable to psychiatric,
cardiometabolic, and lipid trait composites you are considering.

### 16. Wu, Witschey, Li, Ordonez, Bressem et al. — arXiv 2026 (Auditable CT Phenotyping)

**Threads:** Knowledge representation in EHRs (fidelity / audit;
NLP-derived reps); EHR foundation models.

**Bucket:** HIGH.

**What it is (from snippet):** "Medical image foundation models can
[predict]…" Auditable CT phenotyping through radiological-report-
derived observations; tests whether image FMs use disease-specific
findings or shortcuts.

**Why it matters to your threads:** This is the imaging-FM analogue of
the single-cell scContam / MIA-scFM audit protocols you flagged as
portable templates for CLMBR / MOTOR / MEDS benchmark contamination.
Same "audit" logic, different modality. Directly serves both
`Fidelity, portability, and audit of representations` and
`NLP-derived representations from clinical notes` (because the
"auditable" step uses radiology-report NLP as the audit ground
truth). Reading this alongside Chin et al. (item 1) gives you both
temporal and semantic representation audits in one week.

### 17. Jing, Yan, Zhang, Zhao — *Trends in Genetics* 2026 (biobank cohort review)

**Threads:** Biobanks with EHR linkage (AoU / UKB / MVP / BioVU).

**Bucket:** HIGH.

**What it is (from snippet):** "Additionally, by integrating large-scale
whole-genome sequencing with longitudinal EHRs in a…" A timely review
of large-scale human population cohorts and how they compare.

**Why it matters to your threads:** Useful as a canonical citation for
AoU / UKB / MVP / BioVU comparisons in future methods papers, and as a
map of which sub-cohorts (ancestry, geography, EHR depth, WGS vs.
imputation) support which analysis designs. Worth skimming for its
comparison table.

### 18. Zhang, Zhang, Cheng, Gong, Kou, Jiang — 2026 (UKB Olink ML for osteoporosis)

**Threads:** Multi-omics-augmented PRS; UK Biobank; ML for precision
health.

**Bucket:** HIGH.

**What it is:** Explainable plasma-proteomics ML for osteoporosis
diagnosis, prognosis, and protein biomarker discovery in the UK
Biobank.

**Why it matters to your threads:** UKB Olink + explainable ML for a
chronic-disease diagnosis/prognosis endpoint — a template for the
multi-omics-PRS composite designs you're considering. Osteoporosis is
a natural HRT-modulated endpoint, so cross-cite when writing the HRT
persistence work.

### 19. Du, Adamek, Kryukov, Dormont, Bar-Joseph et al. — arXiv 2026 (explainable transformer on structured EHR)

**Threads:** EHR foundation models; Knowledge representation in EHRs.

**Bucket:** HIGH.

**What it is:** Explainable transformer models for clinical prediction
tasks on structured electronic health records (Hripcsak cite).

**Why it matters to your threads:** A CLMBR/MOTOR-neighbor with an
explicit explainability layer. Worth reading with an eye to
representation-ablation signals (which representation choice drives
performance vs. the model architecture) — the exact question you
flagged as "especially interested in" under `Applications to
prioritize` in the Knowledge representation in EHRs thread.

---

## METHODS-WATCH (compact)

- **Bots SH et al., "Negative controls and how to use them: a
  guidance paper,"** *International Journal of Epidemiology* 2026
  (Ryan cite) — canonical negative-control cookbook. Pair with the
  Zhang et al. GLP-1/SGLT2/DPP4 TTE (HIGH #5) as the methods
  reference.
- **Guo Y et al., "Benchmarking short-read germline SV calling
  highlights advantages of ensembles and small impact of graph genome
  alignment,"** *Genome Biology* 2026 (Montgomery cite) — pangenome-
  portability sub-thread; the null-ish graph-alignment result is a
  useful counter-weight to the "pangenome fixes PGS portability"
  narrative.
- **Long W et al., "GenomeHarness: Harnessing AI Agents for Reliable
  Adaptation of Genome Language Models,"** arXiv:2608.21916 (Zitnik
  cite) — agent-adaptation pattern for genome LMs; conceptually paired
  with HIGH #4 (Zitnik "Closing the Loop") but off the biomedical /
  clinical spine.
- **Zheng Z et al., "Telomere-to-telomere CHM13 reference reveals
  missing truth variants and improves DL-based variant calling in
  long-read data,"** 2026 (Montgomery cite) — reference-bias /
  pangenome cross-ancestry sub-thread.
- **Saha S et al., "An approach to classifying and measuring
  stigmatizing and positive language at scale in EHR,"** *BMC Health
  Services Research* 2026 (Hripcsak cite) — NLP-derived
  representation from clinical notes; audit-adjacent to Wu et al.
  (HIGH #16).
- **Kudamala R et al., "Predicting Early Functional Decline from
  Longitudinal Lab and Vital Sign Trajectories: A Large-Scale Study
  Using the All of Us Research Program,"** arXiv:2608.21589 — AoU
  trajectory-clustering methods, portable to multimorbidity work.
- **Dutta D et al., "Polygenic risk scores and plasma proteomics
  identify cancer-related proteins and trans-regulated protein
  networks,"** *Cell Genomics* 2026 — PRS × proteomics cross-omics
  design across 21 cancers; overlaps with HIGH #15 and HIGH #18 on
  the multi-omics-PRS spine.
- **Rajueni K et al., "Multi-biobank GWAS of dermatochalasis,"**
  medRxiv 2026 (Jian Yang cite) — multi-biobank meta-GWAS design
  pattern.
- **Chovatiya R et al., "Real-World Use of Abrocitinib for
  Moderate-to-Severe Atopic Dermatitis in the US Based on EHR and
  Administrative Claims,"** 2026 — EHR + claims fusion template for
  autoimmune drug uptake.
- **Kunitsu Y et al., "Risk of HF Hospitalization: HIF-PHi vs ESA —
  nationwide new-user cohort,"** 2026 (Hernán cite) — active-
  comparator new-user TTE template.
- **Jia Y et al., "Mapping genetic regulation of gene expression to
  cellular contexts identifies lncRNAs associated with brain
  disorders,"** *Nature* 2026 (Montgomery / Yang cite) — context-aware
  eQTL for brain disorders.
- **Cortez-Rodriguez, "Natural Disasters and the Nonprofit Sector,"**
  arXiv 2609.04136 (from local arxiv-digest 09-04) — off-topic
  domain but panel-data causal-inference design; skim only for the
  panel-data-TTE method framing.
- **Yu X, Huang S, Liu J et al., "Location-invariant estimator of
  extremal QTE for heavy-tailed distributions,"** arXiv 2609.04018
  (from local arxiv-digest 09-04) — extremal QTE with IPW; extends
  the extreme-tail HTE work Leimenstoll flagged on 08-25.

---

## Notes and caveats

- **arxiv-digest email channel remains silent.** No
  `notifications@github.com` × `arxiv-digest` emails in the window,
  matching the prior report — the local `digests/*.md` files are the
  actual feed. The recent
  daily runs (09-01, 09-02, 09-04) each surfaced only 1–2 papers, and
  all of them fell to SKIP or METHODS-WATCH; the HIGH signal this
  window came entirely from Scholar author + keyword feeds.
- **Two of the local arxiv-digest runs were low-signal keyword
  matches** (09-01 storage-centric hardware → `precision medicine`;
  09-02 mudskipper locomotion → `motor`). If these categories keep
  producing false-positives, worth revisiting `config/tracked.yaml`
  to tighten either `motor` (require co-occurrence with `neuron`,
  `movement disorder`, or `Parkinson`) or drop `precision medicine`
  as a solo keyword.
- **Same-paper cross-feed duplication is real signal, not noise.**
  Hu et al. NatCom PRS boosting hit 5+ author feeds in one 09-04
  batch; Park et al. OCD-PGS hit 4+. That kind of concurrent
  detection across independent author networks is itself a strong
  attention prior — flagged in the exec summary above.
- **No direct collaborator email in the window.** All non-newsletter
  senders were commercial. If a manuscript or grant email was
  expected in this window from a named collaborator, it did not
  land in the primary inbox.

_Report generated on 2026-09-05._
