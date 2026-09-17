# Research digest report — 2026-09-17

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-17 11:30Z** (~16 days since the
last research-digest report, covering sixteen arxiv-digest cron runs
and roughly a dozen Google Scholar alert batches, plus bioRxiv / medRxiv
collection alerts and daily arXiv q-bio / stat class mailings).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-16.md`) | 09-01 → 09-16 daily crons | 16 daily runs. Dry days (0 papers): 09-03, 09-05, 09-06, 09-08, 09-12, 09-13–09-15 (weekend gaps). Non-dry days summarized in the arXiv section below. |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads. The pipeline commits its output directly to this repo rather than emailing PR / cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-17 morning batch, 05:47Z + 10:48Z) | 09-17 05:47Z → 10:48Z | ~20 feeds fired across the two pushes today. Author feeds (05:47Z): **Joshua C. Denny** (Zheng et al. medRxiv PRS-vs-proteomic-RS in neurodegeneration; Walker et al. medRxiv AoU antidepressant persistence PRS; Roberts et al. IJPRAS polygenic pharmacotherapy evidence map; Bal et al. Nat Cardiovasc Res multiancestry-PRS HCM stratification; Zhang et al. Genomics Proteomics & Bioinformatics colocalization benchmarking; Deng et al. Brief Bioinform debiased MR; Chen et al. **Nature 2026** cell-type-specific eQTLs). **Lisa Bastarache** (Walker et al. AoU + Pharmlines antidepressant PRS). **Konrad Karczewski** (Chaldebas et al. medRxiv 5'UTR mechanistic scoring in UKB; Maher et al. J Neurol rare-variant concussion susceptibility; Tawaldemedhen et al. medRxiv multi-trait polygenic HRS dementia-free survival; Soriano et al. Gut MSH3/MLH3 germline tumour-suppressor signature ID4). **Jian Yang** (Walker et al. — same paper triangulated). **Stephen B. Montgomery** (Hu et al. GWAS-based functional genomics colorectal SMAD9). **Zhiyong Lu / Peter Szolovits / Marinka Zitnik** (attention-control LLM paper — off-topic). **Daniel Kastner** (NLRP3 inhibitor in mice — off-topic). **Lisa Bastarache** author-feed also carried the same Walker AoU paper. Keyword feeds (10:48Z): `"All of Us research program"` (**Tsuo et al. Nat Genet 2026** AoU-scale multiancestry PRS; Lee et al. AoU T2D × ADI age-dependence; Eecen et al. Commun Biol GWAS meta-analysis actinic keratosis; Jiang et al. arXiv 2609.12224 AoU + patient surveys OUD; Spence & Patel arXiv 2609.12297 large-biobank human-evolution review), `"UK Biobank"` (Zhou et al. Diabetes Res Clin Pract T2D operational-definition sensitivity; Xie et al. Annals of Neurology ASCVD-Life's-Essential-8 × ALS 0.5M UKB), `"electronic health records"` (Chahar et al. temporal / semantic / guideline-aware care-gap detection), `Foundation models + "electronic health records"` (Xiao et al. arXiv 2609.12277 RL over patient trajectories in EHR FMs; Lu et al. arXiv 2609.14823 MedTRACE tool-augmented multimodal clinical reasoning; Zhu et al. arXiv 2609.15180 uncertainty-estimation correctness in VLM-based clinical prediction), `"drug repurposing"` (Liang et al. MAFLD review; Li et al. BMC Psychiatry diuretics MR for bipolar disorder — colocalization <10%), `intitle:"clonal hematopoiesis"` (**Chien & Garcia-Manero, Cancer 2026** — clinical management of CH review), `APOL1` (**Huang et al. AJP-Renal 2026** IFN-inducible APOL1 podocyte regulation; **Seifu, Bedada, Zeng, Trends in Genetics 2026** "African genomes are not a subset"), `"variant interpretation" OR "variant classification"` (D'Ambrosio et al. Genes SCN4A channelopathies; Silajiding et al. J Assist Reprod Genet Franklin/VarSome/InterVar comparison in reproductive disorders; Dell'Elice et al. Genes hereditary-cancer WES beyond panels), `rare diseases` (Day-Sharman et al. JBI Evid Synth SR/CPG/HTA methods scoping review), `mendelian diseases` (Chen et al. Front Immunol gut microbiota in Mendelian → complex traits; Maccallini pipeline for causal variants in Mendelian ME/CFS), `"knowledge graph"` (largely off-topic — Mazu culture KG). |
| bioRxiv / medRxiv collection alerts | 09-17 00:00–00:06Z | `Bioinformatics / Genetics / Genomics / Immunology / Pathology` bioRxiv feeds and `Endocrinology / Diabetes / Metabolic Disease` medRxiv feed both fired. Content mostly upstream of the same papers surfaced through Scholar. |
| Daily arXiv q-bio / stat mailings | 09-16 03:44Z, 09-17 03:39Z | Standard `q-bio` and `stat.AP` daily class mailings; captured downstream by `arxiv_digest.py` cron and reflected in the `digests/` folder rather than triaged separately. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets. Note: the "2026" dates in these citations are
> preprint / journal dating — this window is real 2026-09-01 → 2026-09-17.

---

## Executive summary (HIGH-priority studies, ranked)

Eighteen HIGH items surfaced this window, clustering into seven knots:

**Biobank-scale polygenic prediction cluster (3 items).** **Tsuo et al.
Nature Genetics 2026** — the field-defining update to your `Biobanks
with EHR linkage` and `Genetic epidemiology` threads: 245,388 whole-genome
sequences from All of Us combined with UK Biobank to build multiancestry
PRSs for 32 traits, with the crucial finding that AoU-only meta-analysis
is not universally optimal — for less-heritable / less-polygenic traits,
adding UKB in meta-analysis *degrades* portability. Direct heir to your
"PGS residuals / tails-and-residuals taxonomy" framing. **Bal et al.
Nat Cardiovasc Res 2026** — multiancestry PRS for hypertrophic
cardiomyopathy that meaningfully improves stratification in patients
already carrying (or not carrying) sarcomere pathogenic variants; a
canonical composite-risk paper (rare pathogenic + polygenic background)
for the `Composite risk models stacking PRS with rare pathogenic
variants` sub-thread. **Zheng, Shivakumar, Shen, Kim medRxiv 2026** —
Absorption / Co-expression Modules paper quantifying where polygenic
and proteomic risk scores diverge in neurodegenerative disease; a
direct-hit paper for your `Multi-omics-augmented PRS` sub-thread with an
explicit "when do proteomics add over PGS" answer keyed to biological
modules.

**Pharmacogenomic-modifier-of-medication-persistence cluster (2 items).**
**Walker et al. medRxiv 2026** (surfaced through *three* independent
author feeds — Denny, Bastarache, Karczewski, Yang) — polygenic and
familial contributions to antidepressant continuation, switching,
discontinuation and augmentation in All of Us + Pharmlines. This is the
paper directly on your `Pharmacogenomic modifiers of medication
persistence` sub-thread (added to INTERESTS.md 2026-07-29): AoU EHR
linkage + medication-persistence outcomes + PRS + family-history
triangulation. Portable to CFTR-modulator persistence, statin
discontinuation, HRT persistence, GLP-1 RA persistence exactly as flagged.
**Roberts et al. IJPRAS 2026** — evidence-map review of polygenic
pharmacotherapy beyond single-gene rules (interactions, ancestry
transferability, clinical utility); companion positioning paper for the
"beyond CYP2D6 metabolizer-phenotype PGx" framing.

**EHR foundation-model cluster (3 items).** **Xiao et al. arXiv
2609.12277** — RL over patient trajectories for clinical reasoning in
EHR FMs (Naumann, Poon, Gao lineage); addresses the diminishing-returns
observation for pretraining scale on fixed clinical datasets by reframing
next-event prediction as trajectory-level clinical reasoning. **Lu et al.
arXiv 2609.14823** — MedTRACE, a tool-augmented multimodal clinical
reasoning agent operating over heterogeneous EHR + imaging + physiological
signals; contains an explicit sub-comparison to the Cardiac Sensing
Foundation Model as a joint ECG / PPG / clinical-report FM. **Zhu et al.
arXiv 2609.15180** — reframes correctness for uncertainty estimation
in VLM-based clinical prediction, arguing that binary-correctness
scoring underestimates calibration failures in few-shot FM evaluation
— a QC pattern portable to CLMBR / MOTOR / MEDS benchmarking.

**EHR phenotyping / OMOP / representation cluster (2 items).** **Zhou
et al. Diabetes Res Clin Pract 2026** — operational definitions of type
2 diabetes influence study population characteristics and outcome
associations, empirical evidence in **501,936 UK Biobank participants**
across **five T2D definition families** distinguishing diagnosed T2D
from HbA1c-defined undiagnosed diabetes with polygenic + clinical
profiling. A direct-hit paper for the `Concept normalization and
vocabulary mappings` sub-thread of `Knowledge representation in EHRs`
and a textbook demonstration of representation-choice-driving-downstream-
performance, applied to the most-studied phenotype in the field. **Jiang
et al. arXiv 2609.12224** — patient-reported survey data (AoU
questionnaires) improve prediction of opioid use disorder beyond
longitudinal EHR alone; a direct-hit paper for the `Applications to
prioritize` sub-thread (drug-safety signal detection / care-gap
identification / adverse-event surveillance) and for the survey-augmented
EHR-representation angle.

**PheWAS / variant-interpretation & rare-variant discovery cluster (2
items).** **Chaldebas et al. medRxiv 2026** (Karczewski feed) —
mechanistic 5'UTR variant scoring using 5ULTRA that expands rare variant
discovery in UK Biobank beyond conservation-based deleteriousness. A
canonical `Variant interpretation (ACMG / ClinGen)` update, especially
for uORF / Kozak-context evidence and for the "PVS1 supporting evidence
from 5'UTR mechanistic classes" pattern in variant curation. **Silajiding
et al. J Assist Reprod Genet 2026** — head-to-head comparison of
Franklin vs. VarSome vs. InterVar performance in variant interpretation
for reproductive disorders; portable QC observation for downstream
InterVar-style DSL tooling.

**APOL1 / kidney disease cluster (2 items).** **Seifu, Bedada, Zeng
Trends in Genetics 2026** — "African genomes are not a subset" — a
perspective piece explicitly built on the APOL1 G1/G2 focal segmental
glomerulosclerosis mechanistic model, extending it into a broader
cross-ancestry variant-frequency-representation framing. Direct hit for
your `APOL1` disease thread and for the `Cross / trans-ancestry
portability` sub-thread of genetic epi. **Huang et al. AJP-Renal 2026**
— differential regulation of basal vs. interferon-induced APOL1 gene
expression in podocytes; the mechanistic wet-lab companion to the
population-scale APOL1 work, identifying transcription factors regulating
APOL1 in the immune-triggered high-expression state that drives
kidney-disease pathogenesis.

**Clonal hematopoiesis clinical-translation (1 item).** **Chien &
Garcia-Manero Cancer 2026** — clinical management of clonal hematopoiesis,
covering CHIP-associated mutations and clinical clonal management; the
practicing-hematologist perspective on the CH / VEXAS / LOY somatic-
mosaicism thread. Reads alongside the Li et al. LOY × PAD paper you
flagged in the 2026-07-29 INTERESTS.md update as the male-specific LOY
analogue of CHIP.

**Chronic-disease clustering + IBD single-cell drug response (2 items,
plus one honorable mention).** **Devarakonda arXiv 2609.10831** —
scDEFT, single-cell drug-effect transducer on a harmonized 1.16M-cell
IBD atlas across 3 cohorts and 2 drug classes; the single-cell
counterpart to the target-trial-emulation / heterogeneous-treatment-
effect thread applied to IBD. Direct hit for your `Inflammatory bowel
disease` and `Machine learning for precision health` threads (baseline
responder stratification AUROC 0.70 where standard predictors are at
chance). **Semchin et al. arXiv 2609.10890** — connectome-constrained
disease progression model recovering four morphologically distinct
Parkinson's subtypes on PPMI, benchmarked against SuStaIn — a direct-hit
paper for the `Chronic disease clustering and multimorbidity` thread
(latent-class / trajectory clustering applied to neurodegeneration).
**Honorable mention:** Wang et al. arXiv 2609.15584v1 multiscale
NTM-in-CF host-pathogen modeling (CF thread — deep-summary block
appended in the arxiv-digest capture on 2026-09-16).

---

## Detailed per-study reports (HIGH-priority items)

### 1. Tsuo et al. — *All of Us diversity and scale yield context-dependent improvements in polygenic prediction* — Nature Genetics 2026

**Threads served.** `Biobanks with EHR linkage: All of Us, UK Biobank,
MVP, BioVU` (core direct-hit) · `Genetic epidemiology` (PRS + cross-
ancestry portability) · `Cross / trans-ancestry portability` sub-thread.

**What's new.** Uses 245,388 whole-genome sequences from All of Us
alongside UK Biobank data to develop multiancestry PRSs for 32 traits
and diseases, and does the *diagnostic* work of asking when adding UKB
to an AoU meta-analysis helps versus hurts. The headline is negative
in an important way: meta-analyzing AoU + UKB is **not universally
optimal**. For less-heritable / less-polygenic traits, adding UKB
degrades multiancestry portability rather than improves it. This is the
paper that turns the assumed "more is better" into a testable trait-
level decision rule.

**Why it's HIGH for you.** Direct implementation of the "AoU + UKB
composite biobank" paradigm your work sits inside. Practical
consequences: (i) it validates the choice of PRS as the discovery
instrument in your composite-risk framing, (ii) it gives a per-trait
prescription for meta-analysis vs. AoU-alone, and (iii) the finding is
mechanistically consistent with your `PGS residuals / polygenic-deviation
designs` sub-thread — for traits where UKB adds noise more than signal,
residual-based designs and low-risk-group tail designs (Souaiaia, Baya,
Vazquez) should have larger operating envelopes than meta-analysis.

**Where it fits in your reading stack.** Read alongside the Kurniansyah
et al. Nat Genet multiancestry AD-PRS paper flagged in the 2026-09-01
digest and the Acharya et al. J Hum Genet three-biobank ASCVD
heritability paper — together they form the current-generation
cross-biobank / cross-ancestry PRS methods triangle you'll want cited
in any future AoU-based composite-risk manuscript.

### 2. Bal et al. — *A multiancestry polygenic risk score improves stratification in patients with hypertrophic cardiomyopathy* — Nature Cardiovascular Research 2026

**Threads served.** `Genetic epidemiology` (PRS) ·
`Composite risk models stacking PRS with rare pathogenic variants`
sub-thread (core direct-hit) · `Variant interpretation (ACMG / ClinGen)`
(sarcomere-P/LP variants).

**What's new.** Historically HCM has been framed as a Mendelian disease
driven by SARC-P/LP variants, but those variants explain only ~one-third
of cases. This paper builds a multiancestry HCM PRS and shows that it
improves stratification *both* in SARC-P/LP carriers and in the
sarcomere-negative HCM cases that dominate the population. The composite
(rare P/LP + polygenic background) is the operational realization of
the "background modifiers of monogenic penetrance" pattern.

**Why it's HIGH for you.** This is the exact composite-risk architecture
your `PheWAS / phecode infrastructure` penetrance-under-population-
screening framing calls for, transplanted onto cardiomyopathy. It's a
direct template for BRCA1/2 composite-risk work in AoU + UKB, for LDLR
FH composite-risk work, and for the CFTR-heterozygote-background-risk
question. Also relevant to the `Cross / trans-ancestry portability`
sub-thread — the "multiancestry" here matters because the SARC-P/LP
prior is itself ancestry-skewed.

### 3. Zheng, Shivakumar, Shen, Kim — *Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases* — medRxiv 2026

**Threads served.** `Genetic epidemiology` · `Multi-omics-augmented PRS`
sub-thread (core direct-hit) · `Pre-symptomatic carrier phenoconversion
prediction from longitudinal biomarker trajectories` sub-thread (rare
disease).

**What's new.** Instead of just adding PRS + PRS-proteomic in a stacked
model and reporting an incremental AUC, this paper decomposes the
divergence *by biological module*, using absorption / co-expression
analysis to say **where** the two risk instruments carry orthogonal
information. That's the interpretability move the field needs.

**Why it's HIGH for you.** Reads as the direct methodological companion
to the Shan et al. UKB 2026 Nightingale NMR + PGS work and to the Feng
et al. cross-ancestry IDP-pleiotropy depression work you've already
flagged. Portable to your BRCA-incident-cancer, HTT preclinical HD,
APOL1 CKD conversion trajectories under the "pre-symptomatic
phenoconversion via proteomics + PGS" template.

### 4. Walker et al. — *Polygenic and familial contributions to antidepressant continuation, switching, discontinuation and augmentation in the All of Us and Pharmlines cohorts* — medRxiv 2026

**Threads served.** `Causal inference and pharmacoepidemiology` /
`Pharmacogenomic modifiers of medication persistence` sub-thread
(core direct-hit) · `Biobanks with EHR linkage` (AoU) · `Genetic
epidemiology` (PRS).

**What's new.** Directly asks whether reported polygenic associations
with antidepressant response reflect **drug-specific non-response** or
a **broader propensity for treatment modification**. Analyzes AoU +
Pharmlines participants with at least one antidepressant prescription
and models continuation vs. switching vs. discontinuation vs.
augmentation as separable outcomes. Uses family-history triangulation
to disentangle drug-specific from generic-treatment-modification
signal.

**Why it's HIGH for you.** This is the paper that operationalizes the
`Pharmacogenomic modifiers of medication persistence` sub-thread you
added on 2026-07-29 (Cohen et al. *Pharmaceuticals* 2026, Psy-PGx UKB
lineage). The design pattern (multi-state persistence outcomes + PRS
+ family history in AoU EHR linkage) transfers cleanly to CFTR-modulator
persistence, statin discontinuation, HRT persistence, and GLP-1 RA
persistence exactly as you flagged. Triangulated across three
independent Scholar author feeds today (Denny, Bastarache, Karczewski,
Yang) which itself signals broad relevance to the group.

### 5. Xiao et al. — *Reinforcement Learning over Patient Trajectories for Clinical Reasoning in EHR Foundation Models* — arXiv 2609.12277

**Threads served.** `EHR foundation models` (core direct-hit) ·
`Structural and temporal representation of the patient timeline`
sub-thread · `Machine learning for precision health` (when tied to
decision-making outcomes).

**What's new.** Argues that diminishing returns from EHR-FM pretraining
on fixed clinical datasets are a consequence of the next-event
prediction objective, and reframes clinical reasoning as an RL fine-
tuning problem over patient trajectories. Explicitly addresses
incompleteness of EHR data as an RL exploration / reward-shaping
problem rather than a data-augmentation problem.

**Why it's HIGH for you.** Direct RL-fine-tuning update to the CLMBR /
MOTOR / EHRSHOT lineage. Ties naturally to the `Digital twins from EHR
data` sub-thread — the trajectory-level RL objective *is* the "digital
twin" objective spelled correctly. The Naumann / Poon / Gao co-authorship
signals Microsoft-lineage rigor.

### 6. Lu et al. — *MedTRACE: Tool-Augmented Multimodal Clinical Reasoning Agents for Evidence-Grounded Decision-Making* — arXiv 2609.14823

**Threads served.** `EHR foundation models` (multimodal FM) · `Knowledge
representation in EHRs and applications` (representation fusion across
codes + notes + waveforms + imaging) · `Machine learning for precision
health`.

**What's new.** Tool-augmented clinical reasoning agent operating
across EHR + medical images + physiological signals with evidence
grounding, benchmarked against a Cardiac Sensing Foundation Model
baseline that jointly models ECG + PPG + clinical reports.

**Why it's HIGH for you.** The multimodal EHR-FM (notes + codes +
waveforms + imaging) angle you called out in INTERESTS.md, with the
added twist that tool-augmentation reintroduces an auditable step
between the FM and the clinical decision — reads as MedTok / TxAgent /
ToolUniverse lineage transposed onto structured EHR.

### 7. Zhu et al. — *Rethinking Correctness for Uncertainty Estimation in Clinical Prediction with Vision-Language Models* — arXiv 2609.15180

**Threads served.** `EHR foundation models` / `Fidelity, portability,
and audit of representations` sub-thread (core direct-hit).

**What's new.** Argues that binary-correctness scoring of VLM clinical-
prediction outputs systematically miscalibrates uncertainty in few-shot
FM evaluation, and proposes a correctness criterion that accounts for
the graded, evidence-dependent structure of clinical decisions.

**Why it's HIGH for you.** Direct portable template for the auditing
argument you've been advancing under the `Fidelity, portability, and
audit of representations` sub-thread — same underlying claim as
scContam / MIA-scFM contamination audits but transposed to the
uncertainty-calibration axis rather than the training-set-contamination
axis. Combining the two gives a fuller CLMBR / MOTOR audit template.

### 8. Zhou et al. — *Operational definitions of type 2 diabetes influence study population characteristics and outcome associations: Empirical evidence from the UK Biobank* — Diabetes Research and Clinical Practice 2026

**Threads served.** `EHR phenotyping & OMOP` (core direct-hit) ·
`Concept normalization and vocabulary mappings` sub-thread of `Knowledge
representation in EHRs` · `Biobanks with EHR linkage`.

**What's new.** Implements five T2D definition families in 501,936 UK
Biobank participants, explicitly distinguishing diagnosed T2D from
HbA1c-defined undiagnosed diabetes, and compares case composition,
diagnosis timing, and polygenic + clinical profiles across definitions.

**Why it's HIGH for you.** The direct-hit `representation-ablation
study that shows *which representation choice* drives downstream
performance` you called for in the KR-in-EHRs section of INTERESTS.md,
applied to the phenotype the entire field uses as a benchmark. Every
paper that uses T2D as a phenotype in AoU / UKB — including several of
your own — is affected by the definition-family choice this paper
quantifies. Portable QC observation to CFTR modulator eligibility
phenotypes, HRT initiation phenotypes, and GLP-1 RA initiation phenotypes.

### 9. Jiang et al. — *Patient-Reported Survey Data Improve Prediction of Opioid Use Disorder* — arXiv 2609.12224

**Threads served.** `Biobanks with EHR linkage` (AoU-specific) ·
`Applications to prioritize` sub-thread of `Knowledge representation in
EHRs` (drug-safety signal detection / adverse-event surveillance) ·
`Machine learning for precision health`.

**What's new.** Explicitly leverages the AoU design choice of combining
longitudinal EHR data with structured participant-reported
questionnaires — arguably the most under-exploited AoU asset — for OUD
prediction. Shows survey items carry incremental predictive signal
beyond EHR structured data, most usefully at the boundary where OUD
diagnosis is under-documented.

**Why it's HIGH for you.** Direct-hit paper for the AoU-specific
representation angle — patient-reported outcomes as an
under-utilized-but-structured modality that complements structured EHR.
The design pattern generalizes to any behaviorally-informed AoU outcome
(depression persistence, adherence, quality-of-life) where EHR-only
prediction plateaus.

### 10. Chaldebas et al. — *Mechanistic 5'UTR Variant Scoring Expands Rare Variant Discovery in the UK Biobank* — medRxiv 2026

**Threads served.** `Variant interpretation (ACMG / ClinGen)` (core
direct-hit) · `Genetic epidemiology` (rare-variant burden) · `Biobanks
with EHR linkage`.

**What's new.** Introduces 5ULTRA, a 5'UTR-focused mechanistic scoring
approach that uses uORFs and Kozak context rather than
nucleotide-conservation alone. Applied to UK Biobank rare-variant burden
scans, it expands the yield of significant rare-variant associations
that conservation-only scorers miss.

**Why it's HIGH for you.** The classic move you've been watching for
under `Variant interpretation` — going beyond conservation-based PVS1
supporting evidence into mechanism-based supporting evidence for a
class of variants (5'UTR) that current ACMG-AMP guidelines handle
inconsistently. Immediately portable to any ClinGen VCEP that curates
genes with 5'UTR-driven expression regulation.

### 11. Silajiding et al. — *Pathogenicity assessment of genetic variants in reproductive disorders* — J Assist Reprod Genet 2026

**Threads served.** `Variant interpretation (ACMG / ClinGen)` (core
direct-hit) · variant-curation-tooling sub-thread (InterVar-style DSLs).

**What's new.** Head-to-head comparison of **Franklin vs. VarSome vs.
InterVar** on a common set of variants in reproductive disorders,
identifying where the three tools converge and diverge.

**Why it's HIGH for you.** Direct QC input for any InterVar-based DSL
work — the discordance patterns between the three tools are exactly the
error-modes an AnFiSA-style DSL would need to encode as guardrails.

### 12. Chen et al. — *Cell-type-specific eQTLs underlie the genetic architecture of complex traits* — Nature 2026

**Threads served.** `Genetic epidemiology` (fine-mapping / eQTL) ·
`Multi-omics-augmented PRS` sub-thread (upstream regulation informing
downstream PRS construction).

**What's new.** Systematic cell-type-specific eQTL map applied to
complex-trait genetic architecture, quantifying how much genetic
signal is captured at cell-type resolution vs. bulk tissue. The takeaway
frame — that regulation of gene expression is the dominant mechanism
for complex-trait effects — is not new, but the cell-type stratification
gives it operational teeth for downstream PRS + colocalization work.

**Why it's HIGH for you.** Upstream substrate for the
proteomics-augmented-PRS + colocalization pipeline that shows up in
the Zheng / Shivakumar / Kim paper above, and for the drug-target MR
triangulation lineage (Saxby et al. metformin × AAA) you called out on
2026-07-29.

### 13. Seifu, Bedada, Zeng — *African genomes are not a subset* — Trends in Genetics 2026

**Threads served.** `APOL1` (core direct-hit) · `Cross / trans-ancestry
portability` sub-thread of genetic epi · `Genetic epidemiology` broadly.

**What's new.** Perspective piece built on the APOL1 G1/G2 focal
segmental glomerulosclerosis mechanistic model — two coding variants
that protect against African trypanosomes but impose a nephropathy
risk when homozygous or compound heterozygous — as the anchor example
for the broader argument that African-ancestry genomes cannot be
modeled as a subset of European-ancestry genomes.

**Why it's HIGH for you.** Direct-hit paper for your `APOL1` disease
thread (the mechanistic reference framing) *and* the cross-ancestry-
portability arguments that recur across your PRS work. The Zeng
authorship is also relevant context if this is in your citation graph.

### 14. Huang et al. — *Differential regulation of basal and interferon-induced APOL1 gene expression in podocytes* — American Journal of Physiology — Renal Physiology 2026

**Threads served.** `APOL1` (core direct-hit, mechanistic) · variant-
interpretation adjacency (understanding cis-regulatory context
informs coding-variant interpretation in APOL1).

**What's new.** Identifies transcription factors required for basal and
interferon-induced APOL1 expression in podocytes, and characterizes the
immune events associated with the high-APOL1-expression state that
drives kidney-disease pathogenesis.

**Why it's HIGH for you.** The mechanistic wet-lab companion to the
Seifu/Bedada/Zeng perspective — together they give you the
"population-scale + mechanistic" pair on APOL1 for this window.
Regulatory context is the missing piece for any APOL1 clinical-decision
framing (which G1/G2 carriers escalate to nephrology, transplant
implications).

### 15. Chien & Garcia-Manero — *Clinical management of clonal hematopoiesis* — Cancer 2026

**Threads served.** `Clonal hematopoiesis (CHIP), VEXAS, and mosaic Loss
of Y (LOY)` disease thread (core direct-hit).

**What's new.** Practicing-hematologist review of clinical management
of CH (particularly CHIP and clonal cytopenia of undetermined
significance), covering the transition from largely-asymptomatic
mutation detection to specific CH-associated mutations and clonal
progression, plus the extra-hematological (cardiovascular, hematologic)
implications.

**Why it's HIGH for you.** The clinical-management-side companion to
the recent LOY × PAD and LOY × cardiovascular literature you flagged.
Complements Loh *Nature* 2018 / Kessler *Nature* 2022 mechanistic
lineage with the "what do we tell patients and their PCPs" perspective
you'll want when translating any of the somatic-mosaicism work into
population-screening framings.

### 16. Devarakonda — *scDEFT: A deep learning framework for drug-effect prediction and counterfactual reasoning* — arXiv 2609.10831v1

**Threads served.** `Inflammatory bowel disease` (core direct-hit) ·
`Machine learning for precision health` (heterogeneous treatment effects
at cell level) · `Drug repurposing` (mechanism-informed target
nomination).

**What's new.** Single-cell Drug Effect Transducer that treats a drug
as a conditioning operator on cell representations, using FiLM to
produce drug-conditioned cell latents, with independent heads for
drug-induced state change and responder status. Backward stage maps
latent dimensions to genes under cell-composition control. Evaluated on
a harmonized IBD atlas of 1.16M cells, 3 cohorts, 2 drug classes:
responder stratification pre-treatment at AUROC 0.70 where standard
predictors are at chance.

**Why it's HIGH for you.** The IBD-specific single-cell counterpart
to the target-trial-emulation + causal-ML pipeline you've been
tracking. The "counterfactual prediction of unseen drug × cohort
effects" framing is directly on your `Causal inference and pharmacoepi`
sub-thread when read as an out-of-distribution HTE method. Also serves
`Drug repurposing` because the same latent-to-gene mapping supports
target and co-target nomination.

### 17. Roberts et al. — *Polygenic Pharmacotherapy beyond Single-Gene Rules: An Evidence Map of Scores, Interactions, Ancestry Transferability, and Clinical Utility* — IJPRAS 2026

**Threads served.** `Causal inference and pharmacoepi` /
`Pharmacogenomic modifiers of medication persistence` sub-thread ·
`Cross / trans-ancestry portability` sub-thread of genetic epi.

**What's new.** Positioning review that maps the transition from
single-gene / compact-panel PGx (CYP2D6, CYP2C19, TPMT) to polygenic
pharmacotherapy where drug response depends on many variants of small
effect. Explicitly organizes the field along four axes: PRS scores +
gene × drug interactions + ancestry transferability + clinical utility.

**Why it's HIGH for you.** The companion positioning paper to Walker
et al. above — Walker gives the empirical data on antidepressant
persistence, Roberts gives the framework map for how to slot such work
into the broader polygenic-pharmacotherapy landscape.

### 18. Semchin et al. — *Discovering Subtypes of Neurodegenerative Progression with a Scalable Connectome-Constrained Dynamic Model* — arXiv 2609.10890v1

**Threads served.** `Chronic disease clustering and multimorbidity`
(core direct-hit) · `Machine learning for precision health` (subtype
discovery tied to clinical motor subtypes / genetic variants).

**What's new.** Connectome-constrained disease progression model that
jointly estimates subject-specific disease time and data-driven subtypes
from longitudinal morphometry. Applied to 85 imaging + clinical
biomarkers from PPMI, recovers four morphologically distinct progression
subtypes that correspond significantly to clinical motor subtypes and
Parkinson's disease genetic variants. Benchmarked against SuStaIn
under a matched protocol; only the proposed method recovers subtypes
correspondent to clinical motor subtypes.

**Why it's HIGH for you.** Direct-hit paper for the trajectory-clustering
angle of your `Chronic disease clustering` thread, and one of the few
recent papers that explicitly connects data-driven subtypes back to
genetic variants — the pattern you'd want to reproduce for AoU / UKB
cardiometabolic multimorbidity trajectories.

---

## METHODS-WATCH (off-thread but exemplary)

- **Hendrix et al. arXiv 2609.11689** — Geospatial FMs explain up to
  54% of the variance in health outcomes left unexplained by ADI / SDI /
  SVI social risk indices across 82,646 US census tracts. Not on-thread
  disease-wise, but the "FM as a residualization instrument for a
  well-established composite index" pattern is directly portable to
  your PGS-residuals / polygenic-deviation framing.
- **Spence & Patel arXiv 2609.12297** — Large-biobank human-evolution
  review. Off your primary threads, but a useful positioning reference
  for framing AoU + UKB as evolutionary-genetics resources.
- **Chen et al. Nature 2026 cell-type-specific eQTLs** (covered above)
  bridges genetic epi with the eQTL / colocalization sub-thread.
- **Lee, Rempala, Schnell arXiv 2609.09325** — Kalman-filter smoothing
  for Horvitz-Thompson inverse-probability-weighted daily prevalence
  estimation under nonrandom testing. Off-thread disease-wise, but the
  IPW-with-time-series-borrowing pattern is worth cribbing for the
  agentic pharmacoepi pipelines you flagged (oci-agent lineage).
- **Snel & Schulz arXiv 2609.07729** — pyinfluence + attributing
  Cohen's d to training samples for normative age biomarkers in UK
  Biobank. The influence-function pattern is a training-data-audit
  companion to the scContam / MIA-scFM contamination audits.

---

## SKIP (surfaced but not thread-relevant)

- Water hardness / mortality UKB cohort study (Guo et al. BMC Public
  Health 2026) — thread-adjacent by biobank source but not on any
  active thread.
- Optimal timing of physical activity for hypertension patients (Li
  et al. UKB 2026) — same category.
- Recorded skin conditions and multidimensional chronic pain (Zhang
  et al. UKB 2026) — same category.
- Remnant cholesterol / CRP / cardiovascular outcome (Chen et al. UKB
  2026) — same category.
- Adverse pregnancy outcomes × cardio-renal-metabolic multimorbidity
  (Liu et al. UKB 2026) — the multimorbidity framing is on-thread but
  the paper's design is not the trajectory-clustering / latent-class
  design your thread prioritizes.
- Deconfounded-Debiased Distributed Estimation (Li et al. Statistica
  Sinica 2026, UKB proteomics application) — off-thread methodologically.
- Zhou-and-Lee AoU T2D × ADI (age-dependence of neighborhood deprivation)
  — thread-adjacent (AoU) but conference-proceedings scale, not the
  methodology-defining paper the thread prioritizes.
- MSH3 / MLH3 germline colorectal cancer tumor-suppressor / ID4
  signature (Soriano et al. Gut 2026, Karczewski feed) — germline-to-
  somatic-signature is on-thread-adjacent for the CHIP / somatic-
  mosaicism lineage but the paper is a cancer-genetics study, not the
  somatic-vs-germline-QC framing.
- Mendelian-randomization studies of individual disease pairs (breast
  cancer, colorectal cancer, bipolar disorder, glioblastoma, ischemic
  stroke × vascular dementia, coronary heart disease × dendritic cells,
  chronic-kidney × peripheral-artery disease) — all methodologically
  in scope but individually below the "direct-hit for an active thread"
  bar. Roberts and Walker above are the two that consolidate the
  PGx-persistence sub-thread.
- Off-topic author-feed noise: LLM attention-control paper (Ho, Ahmad
  et al. arXiv 2026) surfaced simultaneously across Marinka Zitnik /
  Peter Szolovits / Zhiyong Lu feeds; NLRP3 inflammasome inhibitor
  (Kastner feed); Mazu culture KG (knowledge-graph feed);
  Nigerian-hospital EHR governance / role-based access control (EHR
  feed) — all skipped.

---

## Local arxiv-digest highlights (2026-09-01 → 2026-09-16)

Non-dry days from the local `digests/` folder in this window, with the
top HIGH / METHODS-WATCH pick per day:

| Date | Papers | Top pick |
| --- | --- | --- |
| 09-01 | 3 | Prior report used this as its closing day; scope is 09-02→09-17. |
| 09-02 | 2 | Rolling window; see prior report. |
| 09-04 | 2 | Cortez-Rodriguez (Natural Disasters / Nonprofits, panel-data causal — METHODS-WATCH); Yu et al. location-invariant extremal quantile treatment effects (METHODS-WATCH). |
| 09-07 | 2 | Rolling; largely off-thread. |
| 09-09 | 2 | Snel & Schulz pyinfluence + Cohen's d attribution in UKB (METHODS-WATCH). Wu et al. FUSE-RT chromatography FM (off-thread). |
| 09-10 | 1 | Lee/Rempala/Schnell HT + Kalman prevalence estimation (METHODS-WATCH). |
| 09-11 | 3 | **Devarakonda scDEFT IBD (HIGH — item #16 above)**; Hendrix et al. geospatial FMs vs. social risk indices (METHODS-WATCH); Semchin et al. connectome-constrained Parkinson subtypes (HIGH — item #18). |
| 09-16 | 2 | **Wang et al. Multiscale NTM-in-CF host-pathogen (HIGH-adjacent — CF thread)**; Zhang et al. scKITE knowledge-enhanced single-cell FM (adjacent to `EHR foundation models` audit sub-thread by architecture, but scFM not EHR-FM). |

---

## Cross-cutting observations

1. **The Walker et al. antidepressant-persistence paper is triangulated
   by four independent author feeds today.** Denny + Bastarache +
   Karczewski + Yang all landed it as related-research on the same
   morning batch. That's the strongest cross-feed signal in this window
   and reflects the paper's fit to the Vanderbilt / Broad / QIMR
   genetics-of-drug-persistence lineage. If you're planning a
   CFTR-modulator or GLP-1-persistence follow-up, this is the paper
   whose design you'll want to port.

2. **The Tsuo et al. AoU-scale PRS paper is the field-defining Nature
   Genetics landing this window.** Its meta-analysis-degrades-portability
   finding is the more actionable one; it turns "always add more data"
   into a trait-level prescription and should reshape any AoU + UKB PRS
   protocol.

3. **APOL1 got both a mechanistic (Huang podocytes) and a positioning
   (Seifu / Bedada / Zeng "African genomes are not a subset") paper in
   the same 24-hour window** — worth flagging in the APOL1 thread's
   updated reference stack.

4. **EHR foundation models trending toward RL + tool-augmentation.**
   Xiao et al. + Lu et al. + Zhu et al. all landed in a single Foundation-
   models-and-EHR keyword-feed batch — the field's next-step consensus
   is trajectory-level RL fine-tuning and tool-augmented reasoning, not
   more pretraining scale. This confirms the "diminishing-returns from
   scaling" observation you flagged as a rising sub-thread in the
   2026-07-29 INTERESTS.md update.

5. **CH / LOY thread got its clinical-management review.** Chien &
   Garcia-Manero fills the practice-side gap in the CH / VEXAS / LOY
   reading stack alongside Li et al. LOY × PAD (already flagged) and
   the Ji et al. somatic-contamination-of-germline-scans QC paper.

6. **Zero arxiv-digest emails from GitHub in this window.** As previously
   noted, the pipeline commits its output directly to `digests/`; the
   on-disk digests *are* the arxiv-digest feed, and no PR / notification
   emails are expected from it.

---

## Next steps (suggested)

- Read Tsuo et al. Nature Genetics 2026 in full and update
  `INTERESTS.md`'s PRS-portability sub-thread with the trait-family
  prescription (AoU-alone vs. AoU + UKB meta-analysis).
- Read Walker et al. AoU + Pharmlines antidepressant PRS + persistence
  in full; if the design is portable to CFTR-modulator persistence,
  scope a mini-protocol in the CF thread.
- Skim Bal et al. HCM multiancestry PRS for a template to reuse in your
  composite-risk framing work.
- Skim Chaldebas et al. 5ULTRA for the 5'UTR mechanistic-scoring approach
  and note whether it plugs into your ClinGen VCEP / InterVar-DSL
  pipeline.
- File Chien & Garcia-Manero *Cancer* 2026 into the CH / VEXAS / LOY
  reading stack.
- File Seifu / Bedada / Zeng *Trends in Genetics* 2026 into the APOL1
  and cross-ancestry-portability reading stacks.
