# Research digest report — 2026-09-02

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-02 12:40Z** (~24 hours since the
2026-09-01 report; covers one arxiv-digest cron run, one full Google
Scholar alert batch (09-02 02:01Z), the tail of the previous batch
(09-01 11:36Z — the citation- and author-feed items not already
detailed in the prior report), the 09-01/09-02 medRxiv + bioRxiv
collection alerts, three NCBI PubMed alert emails, the JAMA
Vol 336(9) issue release, and the ML4H seminar digest).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md`) | 09-01 cron | 1 paper. Ghiasi *Storage-Centric System Designs for Fast, Efficient, and Low-Cost Genomic and Metagenomic Analyses* (cs.AR, keyword hit "precision medicine", score 1) — off-thread hardware/systems dissertation; **SKIP**. No 09-02 arxiv-digest run has fired yet as of 12:40Z. |
| No `arxiv-digest` email hits from GitHub | — | Confirmed again: `from:notifications@github.com` × arxiv-digest returns zero threads in the window. The pipeline commits its output to this repo; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-02 batch, 02:01Z) | 09-02 02:01Z | Ten keyword feeds fired: `"All of Us research program"` (Garofalo et al. JHEP Reports multi-ancestry HCC + Hu et al. Nature Comms adaptive-boosting PRS fine-tune); `mendelian diseases` (Jiang et al. Genes autoimmune × follicular lymphoma MR-multiomics); `Foundation models + "electronic health records"` (Abraham nursing-perspective AI-in-PHC review — SKIP); `"variant interpretation" OR "variant classification"` (Li et al. paternal-then-maternal FOXL2 BPES-I three-gen — narrow); `rare diseases` (AstraZeneca Koselugo China approval news — SKIP); `"drug repurposing"` (Shen et al. sertraline anti-CRC metabolomics — off-thread mechanistic); `"UK Biobank"` (Zhang et al. FASEB J proteomics-ML osteoporosis, Strawbridge et al. PRS-SCZ × 1,459 proteins in 44,661 UKB, Hong et al. passive smoking × obesity × MACE multi-cohort, Lim UKB organ-dysfunction × depression, Chen et al. TyG × T2D microvascular UKB, plus Hu et al. adaptive-boosting PRS again, Mertens et al. Communications Medicine MRI body-comp pooled UKB + NAKO, Preanto et al. ECG ML review); `"knowledge graph"` (Wang et al. construction-domain KG-LLM — SKIP); `"autoimmune disorders" or "autoimmune diseases"` (Stone environmental risk factors book chapter — SKIP); `"electronic health records"` (Chovatiya et al. abrocitinib RWE atopic dermatitis — MED). |
| Google Scholar alerts (09-01 batch, 11:36Z) | 09-01 11:36Z | Overlaps with the prior report's cutoff. HIGH items not detailed there: **Zheng et al. medRxiv PGS × proteomic-RS divergence in neurodegeneration** (surfaced under Chenjie Zeng, Jian Yang, Konrad Karczewski, and Joshua C. Denny related-research feeds); **Lassen et al. Nat Commun deviations-from-additivity driven by rare variants at biobank scale** (same Chenjie Zeng feed, and Konrad Karczewski / Lisa Bastarache related feeds); **Fang, Li, Noori, Fesser, Zitnik** "Closing the Loop in AI-Driven Biomedical Discovery" (Marinka Zitnik author feed); **Qin, Zeng, Ma, Ge, Tham, Shah, Eils** "Autonomous agentic AI systems in health care: friend or foe?" (Lancet Digital Health 2026 — Nigam Shah author feed); **Gan et al.** knowledge-graph-guided multiple sclerosis identification and therapeutic-trend analysis, two-health-system RWE (Hripcsak related feed); **Zhao et al. arXiv** "Rare Diseases, Common Dilemmas: LLMs Prioritize Equal Resource Distribution over Patient Benefit" (Isaac Kohane author feed); **Chen et al. MOCR-DB** multi-omics causal-inference resource DB (Konrad Karczewski citations-to). |
| medRxiv Collection alert (09-02 00:05Z) | 09-01 postings | Endocrinology, Epidemiology, Genetic & Genomic Medicine, Health Informatics, Ob/Gyn, Oncology. HIGH: **Weyrich et al.** age-related CHIP × mosaic sex-chromosome loss × systemic proteomics × disease vulnerabilities (CHIP+LOY sub-thread direct hit); **Liu, Mizani, Zhao, Wood, Inouye, Price, Jiang, CVD-COVID-UK/COVID-IMPACT** COVID-19 hospitalisation + common-disease risk from comorbid diagnoses in **13 million individuals** (multimorbidity + PGS/PRS + national EHR); **Witham et al.** multiple long-term conditions → unscheduled care pathways (multimorbidity trajectories); **Song, Ni, Liu, Li, Malin, Yin** CPT/HCPCS code recommendation from clinical notes, comparative AI methods (knowledge representation in EHRs); **Bingham & Arussy** cost-aware active feature acquisition for differential diagnosis under realistic clinical availability constraints (ML-for-precision-health, decision-tied); **Shi et al. PCGS** pediatric cancer biomarker/risk-group ID via explainable GNN + Shapley (KG-GNN + rare disease); **Kohler et al.** global adoption of openEHR clinical data repositories vendor + community survey (interoperability standards); **Li et al.** LLM-assisted evidence audit of late-stage cancer incidence as a screening-trial endpoint (LLM-audit template). MED/NOTE: **Efthymiou et al.** RUBCN autophagy-overdrive neurodevelopmental disorder with age-dependent neurodegeneration (rare-disease case-series, HPO relevance). |
| bioRxiv Collection alert (09-02 00:02Z) | 09-01 postings | Bioinformatics, Genetics, Genomics, Immunology. HIGH: **Kaniewski et al.** "Every Cure Knowledge Graph: A Unified Biomedical KG for Drug Repurposing" (bioRxiv, DOI 2026.08.26.747253 — direct hit for drug-repurposing KG thread, Melissa Haendel + Alexander Tropsha + David Fajgenbaum authorship); **Wiel et al. MetaDome 2027** aggregated missense-variant evidence across homologous human protein domains (variant interpretation / ClinGen VUS thread); **Yu et al.** LLMs for accessible reporting of bioinformatics analyses in interdisciplinary contexts (NLP-derived representations, methods-watch). MED: **Refaee et al.** microsecond MD of SOD1 variants × divergent ALS clinical outcomes (rare-disease variant-interpretation adjacent). |
| NCBI PubMed alerts (09-01 12:54Z, 09-02 12:35Z) | rolling | `UK Biobank` × 2, `All of Us` × 1, `drug repurposing` × 2 saved-search push. Content not opened per email (each is a large digest); worth an inbox scan when planning next TTE/PGS study. |
| JAMA Vol 336 No 9 New Issue (09-01 18:36Z) | 09-01 online-first | HIGH: **Oosterom-Eijmael, Hulst, Monteiro de Oliveira et al.** — *Dapagliflozin and Acute Kidney Injury Following Cardiac Surgery: A Randomized Clinical Trial* (SGLT2i pharmacoepi + perioperative-AKI thread direct hit); accompanying editorial **Winkelmayer & Chertow** *Dapagliflozin to Reduce the Risk of Perioperative AKI in Elective Cardiac Surgery*. MED: Ng et al. SOLARIS phase III high-dose vitamin D3 in metastatic CRC (Alliance A021703); Clarençon et al. DISCOUNT trial thrombectomy in medium/distal-vessel stroke; Zaidat et al. one-year outcomes of TESLA endovascular treatment for large AIS. |
| ML4H seminar (09-01 23:10Z) | 09-01 | Endometriosis diagnostic-delay early-detection case study — **rare-disease + pre-symptomatic phenoconversion adjacent**, on the same axis as the Ran/Benatar ALS-phenoconversion prediction reference in your INTERESTS.md. |
| bioRxiv/medRxiv 09-01 00:0xZ (pre-cutoff) | 08-31 postings | Included in the prior report's window; not re-triaged here. |
| Newsletters, industry alerts, and off-thread noise | 09-01 → 09-02 | Filtered: `unwindai@mail.beehiiv.com`, `swyx+ainews@substack.com`, `semianalysis@substack.com`, `marktechpost-newsletter@mail.beehiiv.com`, `stateai@substack.com`, `artificialintelligencemadesimple@substack.com`, `news@alphasignal.ai`, `prem.mohanty@elicit.com`, `swyx@substack.com`, plain arXiv daily class mailings. All AI-industry / model-launch content; **no research-thread hits**. |

> Caveat: Scholar and PubMed emails give title + authors + venue + the
> first 2–3 lines of each abstract. Reports below contextualize that
> against the tracked threads; nothing reflects full-text reading. The
> arxiv-digest local run captures full abstracts, and the 09-01 entry
> that surfaced is included verbatim from the on-disk file.

---

## Executive summary (HIGH-priority studies, ranked)

Roughly fifteen HIGH items surfaced this window, clustering into six
knots:

**Pharmacoepi / RCT of an SGLT2 inhibitor (1 item).** Oosterom-Eijmael
et al. — the JAMA 09-01 issue's headline **dapagliflozin RCT for
prevention of AKI after cardiac surgery**, with an accompanying
Winkelmayer/Chertow editorial. A rare RCT-quality read into the SGLT2i
mechanism side of your `Causal inference and pharmacoepidemiology`
drug-thread panel, useful as the head-to-head anchor when you write up
the RWE-TTE side.

**PGS × multi-omics + PGS × rare-variant cluster (3 items).** Zheng,
Shivakumar, Shen, Kim medRxiv — **polygenic and proteomic risk scores
diverge in neurodegeneration**, quantified via absorption and
co-expression modules; a direct-hit for the `Multi-omics-augmented PRS`
sub-thread (Shan/Feng-family) and complements the Kopal et al.
brain-imaging × mental health × cardiometabolic MiXeR paper you already
track. Lassen, Venkatesh, Baya, Lindgren et al. *Nat Commun* —
**deviations from additivity driven by rare variants at biobank
scale**; the Baya-lineage paper you specifically flagged for `PGS
residuals / polygenic-deviation designs` (the "misaligned individuals"
framing) with a rare-variant read-out. Hu, Chen, Salvatore, Wu, Ozdemir,
Lu et al. *Nat Commun* — **pre-train + fine-tune adaptive boosting of
pre-trained PRS**, fine-tuned on UK Biobank and externally validated
across **All of Us + eMERGE + Penn Medicine Biobank**. Three-biobank
external validation is exactly the design pattern your
`Biobanks with EHR linkage` thread wants propagated.

**Biobanks & genetic epi (1 item on top of the above).** Garofalo,
Chotiprasidhi, Johnson et al. *JHEP Reports* — **multi-ancestry
sequencing analysis in 293,141 participants** identifying predisposition
DNA-repair genes for HCC risk, drawing on All of Us + MVP data. Cleanly
on the `Rare-variant / cross-ancestry / biobank` axis you already track;
complements the Acharya et al. three-biobank ASCVD-heritability paper
from the prior window.

**CHIP / LOY / somatic mosaicism (1 item).** Weyrich, Ware,
Steixner-Kumar, Windschmitt, Sarakpi, Abplanalp, Dimmeler, Speer, Zeiher
medRxiv — **age-related CHIP and mosaic sex-chromosome loss define
distinct systemic proteomic programs and disease vulnerabilities**.
Direct-hit for the `CHIP, VEXAS, LOY` sub-thread you flagged, with the
extra angle of proteomic-signature-of-mosaicism — a shared spine with
the Weinstock proteomic-CHIP work and the Loh/Kessler LOY lineage. This
is the one to open first from the CHIP/LOY watch.

**Knowledge graphs + drug repurposing + EHR RWE (2 items).** Kaniewski,
Carter, Rhodes, Lim, Li, Vergine, Matentzoglu, Schaper, Reilly, Sundar,
Vijnck, Sharp, Alfonso, Ford, Stepanenko, Hempstead, Brokmeier, Bizon,
Tropsha, Haendel, Fajgenbaum, Lancashire bioRxiv — **Every Cure
Knowledge Graph, a unified biomedical KG for drug repurposing**;
Haendel + Tropsha + Fajgenbaum authorship signals ontology-grounded,
mechanism-explainable design (Every Cure's Castleman-lineage). Gan, Zhu,
Tang, Sweet, Morris, Han et al. — **KG-guided multiple-sclerosis
identification and therapeutic-trend analysis, RWE from two large
healthcare systems** (Hripcsak citation feed). Together these pair the
KG-substrate and the KG-applied-to-EHR-RWE halves of your
`Drug repurposing` and `Knowledge graphs & ontologies` threads.

**Agentic AI in health / biomedical discovery (2 items).** Qin, Zeng,
Ma, Ge, Tham, Shah, Eils *Lancet Digital Health* — **autonomous
agentic AI systems in health care: friend or foe?**; a positioning
piece for the agentic sub-thread you added under
`Causal inference and pharmacoepi`. Fang, Li, Noori, Fesser, Zitnik —
**Closing the Loop in AI-Driven Biomedical Discovery** (a
hypothesis-generation → experiment-loop position paper). Both align
with the `Agentic / human-in-the-loop observational-causal-inference
pipelines` sub-thread.

**EHR-driven multimorbidity + national-scale prediction (2 items).**
Liu, Mizani, Zhao, Wood, Inouye, Price, Jiang, CVD-COVID-UK/
COVID-IMPACT medRxiv — **COVID-19 hospitalisation + common-disease
risk from comorbid diagnoses in 13 million individuals** (national EHR
+ comorbidity phenotype vectors). Direct-hit for
`Chronic disease clustering and multimorbidity` at national scale, and
a natural sibling for the Ellershaw et al. Foresight-England national
EHR-FM paper from the prior window. Witham et al. medRxiv — **people
living with multiple long-term conditions have different pathways of
unscheduled care in hospital**; a Sayer-lineage multimorbidity-pathway
paper, methods-watch for phenotype-sequence trajectory modeling.

**Variant interpretation + knowledge representation (2 items).** Wiel,
Ferraro, Yu, Zhen, Nachun, Mendez, Reuter, Cui, Bonner, Carter,
Marwaha, van de Vorst, Emami, Kravets, Neu, van Ham, Kleefstra, Ashley,
Bernstein, Montgomery, Gilissen, Wheeler bioRxiv — **MetaDome 2027**,
comprehensively updated aggregation of missense-variant evidence
across homologous protein domains (Ashley/Bernstein/Gilissen/Wheeler
authorship, direct hit for `Variant interpretation (ACMG / ClinGen)`).
Song, Ni, Liu, Li, Malin, Yin medRxiv — **CPT/HCPCS code
recommendation from clinical notes: a comparative evaluation of AI
methods** (Malin/Yin lineage, direct hit for
`Knowledge representation in EHRs → NLP-derived representations from
clinical notes`).

---

## Detailed reports — HIGH-priority studies

Papers below are the ones I would open next; each note gives (a) the
core method or claim, (b) why it maps to a research thread, and (c)
what to compare it against in the existing literature you track.

### 1. Oosterom-Eijmael, Hulst, Monteiro de Oliveira et al. — *Dapagliflozin and Acute Kidney Injury Following Cardiac Surgery: A Randomized Clinical Trial*
**Venue:** *JAMA*, 2026 Sep 1; Vol 336 No 9 (issue online 09-01).
**Companion:** Editorial by Winkelmayer & Chertow, *Dapagliflozin to
Reduce the Risk of Perioperative AKI in Elective Cardiac Surgery*.
**Surfaced via:** JAMA new-issue email (09-01 18:36Z).
**Threads:** Causal inference & pharmacoepi (SGLT2 sub-thread); ML for
precision health (perioperative decision-tied); indirectly variant
interpretation via SGLT2 target biology.

**What it is.** A randomized clinical trial in elective cardiac-surgery
patients evaluating dapagliflozin (SGLT2 inhibitor) for prevention of
postoperative AKI. This is the RCT side of the perioperative
SGLT2i-AKI question that your target-trial-emulation reading has been
tracking on the observational side.

**Why it matters for your work.** Three angles: (a) it is a **hard
anchor RCT** for the SGLT2i sub-thread — pair it with the Zhang et al.
*Diabetes, Obesity & Metabolism* 2026 empirically-calibrated GLP-1/
SGLT2/DPP4 TTE from the prior report to see how the calibrated
observational estimate matches the RCT effect. (b) It updates the
mechanism story: SGLT2i beyond glycemic effect, into a perioperative-
outcome question that is exactly the kind of "who to treat, when to
escalate" decision your `Machine learning for precision health` thread
prioritizes. (c) The Winkelmayer/Chertow editorial gives a
network/AKI-epidemiology framing that is portable to your CFTR-modulator
persistence and GLP-1 persistence writing.

**Contrast against:** Zhang et al. *Diabetes, Obesity & Metabolism*
2026 (calibrated head-to-head GLP-1/SGLT2/DPP4 TTE, prior window);
Suchard et al. LEGEND-HTN; DAPA-CKD / EMPA-KIDNEY (chronic-CKD SGLT2i
RCTs, non-perioperative); OHDSI SGLT2i × diuretic negative-control-
calibrated safety papers.

---

### 2. Zheng, Shivakumar, Shen, Kim — *Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases*
**Venue:** medRxiv, 2026 (DOI 2026.08.24.26361271).
**Surfaced via:** Google Scholar alerts (09-01 11:36Z) — under the
Chenjie Zeng, Jian Yang, Konrad Karczewski, and Joshua C. Denny
related-research feeds simultaneously (a four-feed hit is a strong
recall signal that this paper is on the same axis as your prior work).
**Threads:** Genetic epidemiology → Multi-omics-augmented PRS
(Nightingale NMR / Olink proteomics / metabolomics stacked with PGS);
also PGS residuals / polygenic-deviation designs (indirectly, via the
"divergence" framing).

**What it is (from abstract).** Polygenic and proteomic risk scores are
both proposed for pre-symptomatic stratification. The paper quantifies
the extent to which they provide overlapping vs complementary
information across neurodegenerative disease, using **absorption
analysis and co-expression modules** to localize where the two RS types
diverge (i.e., which biological modules the proteomic score captures
that the polygenic score misses, and vice versa).

**Why it matters for your work.** This is the paper your
`Multi-omics-augmented PRS` sub-thread was waiting for: an explicit
divergence framework rather than a black-box stacked-score. The module-
level decomposition is the same *interpretable* angle you already track
for the Shan UKB 2026 lipid/cardiometabolic multi-omics PRS and the
Feng et al. cross-ancestry IDP pleiotropy paper. It is also a natural
methodological substrate for your composite-risk PGS-tails / residuals
work (Baya, Souaiaia, Vazquez lineage) — the co-expression modules give
a candidate axis on which "misaligned individuals" (high PRS, low
proteomic RS, or vice versa) could be enriched for rare pathogenic
variants.

**Contrast against:** Baya *AJHG* 2026 misaligned individuals /
PGS-residuals; Souaiaia *Nature* PGS tails; Shan UKB 2026 multi-omics
PRS; Kopal et al. MiXeR brain imaging × mental health × cardiometabolic;
Zhu et al. AoU partitioned BP-PRS (prior window). Also worth checking
whether the modules overlap with the Weyrich et al. CHIP/LOY proteomic
programs (Report #5 below).

---

### 3. Lassen, Venkatesh, Baya, Lindgren, et al. — *Deviations from genetic additivity driven by rare variants at biobank scale*
**Venue:** *Nature Communications*, 2026 (DOI 10.1038/s41467-026-76151-w).
**Surfaced via:** Google Scholar alerts (09-01 11:36Z) — Chenjie Zeng,
Konrad Karczewski, Lisa Bastarache related-research feeds.
**Threads:** Genetic epidemiology → PGS residuals /
polygenic-deviation designs (the Baya "misaligned individuals" framing
you already prioritize); Variant interpretation (ACMG / ClinGen — rare
variants); PheWAS / phecode infrastructure (penetrance under population
screening).

**What it is (from abstract).** Additive genetic models are the default
for GWAS. This paper introduces a scalable framework for **testing
nonadditivity driven by rare variants at biobank scale**, tackling the
statistical bottleneck that existing methods can't handle. The
Baya-Lindgren-Venkatesh authorship signals a direct extension of the
Baya *AJHG* 2026 "misaligned individuals" paper you flagged as a
discovery lever.

**Why it matters for your work.** This is the methods paper your
`PGS residuals / polygenic-deviation designs` sub-thread expected next.
It formalizes the discovery lever your INTERESTS.md called out:
detecting rare variants by their deviations from the additive
polygenic-expected effect. Also directly on the
`penetrance estimation for monogenic variants under population-
screening conditions vs clinically ascertained cohorts` axis of your
PheWAS-infrastructure thread — non-additive rare-variant effects are
exactly where penetrance disagreements arise.

**Contrast against:** Baya *AJHG* 2026 misaligned individuals; Souaiaia
*Nature* PGS-tails; Vazquez *Genetics* low-risk-group designs; Ji et
al. *Biology* 2026 somatic-mutation-contamination QC (which sits
upstream as a rare-variant scan cleanup step).

---

### 4. Hu, Chen, Salvatore, Wu, Ozdemir, Lu et al. — *A pre-train and fine-tune framework for adaptive boosting of pre-trained polygenic risk scores*
**Venue:** *Nature Communications*, 2026 (DOI 10.1038/s41467-026-77128-5).
**Surfaced via:** Google Scholar alerts (09-02 02:01Z) — under both
`"All of Us research program"` and `"UK Biobank"` keyword feeds (a
two-feed hit).
**Threads:** Genetic epidemiology (PGS methodology, cross-ancestry
portability); Biobanks with EHR linkage (multi-biobank external
validation).

**What it is (from abstract).** A **pre-train + fine-tune framework**
that adaptively boosts pre-trained polygenic risk scores. Fine-tuned on
UK Biobank data, then externally validated for both binary diseases and
continuous traits across **three independent datasets — All of Us +
eMERGE + Penn Medicine Biobank**.

**Why it matters for your work.** Two hits at once. On methods, this is
the transfer-learning-for-PRS story your `PGS / polygenic scores` and
`cross / trans-ancestry portability` sub-threads want to see: adapt a
frozen upstream PGS to a downstream cohort instead of building from
scratch. On study-design, the multi-biobank external-validation setup
(AoU + eMERGE + PMBB) is exactly the "propagate the design template"
axis your `Biobanks with EHR linkage` thread prioritizes; pair it with
the Acharya et al. Geisinger MyCode + UKB + AoU cross-biobank ASCVD
paper from the prior window.

**Contrast against:** Ge, Chen et al. PRS-CS lineage; Weissbrod
PolyPred; eMERGE PRS-transferability work; the Kurniansyah et al.
*Nat Genet* multiancestry AD-PRS from the prior window.

---

### 5. Weyrich, Ware, Steixner-Kumar, Windschmitt, Sarakpi, Abplanalp, Dimmeler, Speer, Zeiher — *Age-related clonal hematopoiesis and mosaic sex chromosome loss define distinct systemic proteomic programs and disease vulnerabilities*
**Venue:** medRxiv, 2026 (DOI 2026.08.29.26361722).
**Surfaced via:** medRxiv Collection alert (09-02 00:05Z, Genetic and
Genomic Medicine collection).
**Threads:** Clonal hematopoiesis (CHIP), VEXAS, and mosaic Loss of Y
(LOY) — the CHIP + LOY sub-thread you flagged with the Loh 2018 /
Kessler 2022 / Li et al. *Atherosclerosis* 2026 LOY × PAD lineage;
Multi-omics-augmented PRS (proteomic side).

**What it is (from abstract signal).** Analyzes **CHIP and mosaic
sex-chromosome loss (mLOY / mLOX)** as two age-related somatic-
mosaicism axes and characterizes their **distinct systemic proteomic
programs** and associated disease vulnerabilities. Zeiher / Dimmeler
authorship signals a cardiovascular-outcome framing.

**Why it matters for your work.** Direct-hit for the CHIP + LOY
sub-thread. Two extra angles: (a) it puts CHIP and LOY on the **same
proteomic axis**, which is a joint-analysis substrate you haven't seen
in your tracked LOY papers to date; (b) it is the natural companion to
the Zheng et al. neurodegeneration polygenic-vs-proteomic RS divergence
paper (Report #2) — both are "what does proteomics add to a
genetic-risk read?" but on complementary substrates (germline PGS ↔
neurodegeneration for Zheng; somatic mosaicism ↔ CV disease for
Weyrich).

**Contrast against:** Loh *Nature* 2018 (LOY, germline lineage);
Kessler *Nature* 2022 (LOY, biobank-scale); Li et al. *Atherosclerosis*
2026 LOY × PAD; Ji et al. *Biology* 2026 QC layer for somatic-vs-
germline contamination in rare-variant scans; Weinstock CHIP-proteomic
lineage.

---

### 6. Kaniewski, Carter, Rhodes, Lim, Li, Vergine, Matentzoglu, Schaper, Reilly, Sundar, Vijnck, Sharp, Alfonso, Ford, Stepanenko, Hempstead, Brokmeier, Bizon, Tropsha, Haendel, Fajgenbaum, Lancashire — *Every Cure Knowledge Graph: A Unified Biomedical Knowledge Graph for Drug Repurposing*
**Venue:** bioRxiv, 2026 (DOI 2026.08.26.747253).
**Surfaced via:** bioRxiv Collection alert (09-02 00:02Z,
Bioinformatics collection).
**Threads:** Drug repurposing (KG / GNN approaches with explainable
hypothesis output); Knowledge graphs & ontologies (biomedical KG for
clinical reasoning).

**What it is (from author signal).** A **unified biomedical knowledge
graph for drug repurposing**, developed by Every Cure — the David
Fajgenbaum-led nonprofit that has been publishing the AI + rare-
disease-repurposing playbook off Fajgenbaum's Castleman-disease
sirolimus experience. Melissa Haendel + Alexander Tropsha +
Matentzoglu (Semantic-KG / Monarch lineage) + Bizon (ROBOKOP lineage)
authorship signals a Monarch-Initiative-lineage, ontology-grounded,
mechanism-explainable graph substrate rather than an opaque
link-prediction model.

**Why it matters for your work.** Direct-hit for the exact intersection
of your `Drug repurposing` and `Knowledge graphs & ontologies` threads.
Your interests explicitly prioritize "knowledge-graph / GNN approaches
with *explainable* hypothesis output (path or subgraph rationales rather
than opaque link-prediction scores)"; the Every Cure KG's Monarch-
grounded design is that. Also on-thread for `Rare disease` — Every
Cure's flagship use case is rare-disease repurposing where
HPO-based phenotype matching connects to candidate compounds.

**Contrast against:** ROBOKOP (Bizon); Monarch Initiative
knowledge-graph; PrimeKG (Zitnik lab, Chandak et al. 2023); HetioNet
(Himmelstein et al. 2017); RTX-KG2 (multiomics KG). Also pair with the
next paper below (KG-guided MS therapeutic-trend analysis) as the
"applied to RWE" downstream.

---

### 7. Gan, Zhu, Tang, Sweet, Morris, Han et al. — *Knowledge graph-guided multiple sclerosis identification and therapeutic trend analysis: Real-world evidence from two large healthcare systems*
**Venue:** journal not fully surfaced in alert snippet; RWE study across
two large healthcare systems, 2026.
**Surfaced via:** Google Scholar alerts (09-01 11:36Z, George Hripcsak
related-research feed).
**Threads:** Knowledge graphs & ontologies (KG for clinical reasoning);
Drug repurposing (KG-based EHR RWE); EHR phenotyping (KG-guided
cohort/phenotype ID).

**What it is (from snippet).** Uses a **knowledge graph to guide
identification of multiple-sclerosis patients** in two large healthcare
systems and then to analyze **real-world therapeutic trends** in that
cohort. Combines KG-based patient-graph construction with EHR-derived
prescribing/outcome data.

**Why it matters for your work.** This is the KG-*applied-to-EHR-RWE*
half that pairs naturally with Every Cure (above) — KG as the substrate
and KG as the EHR-integration layer. Direct-hit for your `Knowledge
representation in EHRs → Patient-level and cohort-level knowledge
graphs from EHR` sub-thread, and for the `Drug repurposing → EHR-based
repurposing signals mined from real-world prescribing and outcomes`
angle. Multi-site (two healthcare systems) is on the design axis your
`Fidelity, portability, and audit of representations` sub-thread wants
propagated.

**Contrast against:** Every Cure KG (Report #6); ROBOKOP; NP-KG
(Callahan); FedV-KGQA (prior window, cross-site KG QA); N3C /
CohortDiagnostics (OHDSI-side); Ilves et al. CohortContrast (Estonian
OMOP, prior window).

---

### 8. Fang, Li, Noori, Fesser, Zitnik — *Closing the Loop in AI-Driven Biomedical Discovery*
**Venue:** 2026 (preprint / short paper — venue not yet resolved from
alert snippet).
**Surfaced via:** Google Scholar alerts (09-01 11:36Z, Marinka Zitnik
new-articles feed).
**Threads:** Causal inference and pharmacoepidemiology → Agentic /
human-in-the-loop observational-causal-inference pipelines (the rising
sub-thread you added).

**What it is (from snippet).** AI scientists generate hypotheses,
propose experiments, and analyze datasets; several have been deployed
in silico. This paper argues for **closing the loop** — making the
hypothesis → experiment → analysis → refinement cycle end-to-end rather
than one-shot.

**Why it matters for your work.** Zitnik's framing of the biomedical-
discovery loop is a natural companion to the agentic-observational-
causal-inference sub-thread you added (Chou/Kallus `oci-agent`,
Netflix, and the Li et al. EHR-derived HTE for trial-design pipeline).
The bench-side loop-closing story is the sibling of the RWE-side
agentic-TTE story: they share the "human in the loop for assumption /
interpretation, automation for the mechanical steps" spine.

**Contrast against:** Qin et al. *Lancet Digital Health* (Report #9);
Chou/Kallus `oci-agent`; the Li et al. arXiv 2607.16934 EHR-HTE-for-
trial-design; James Zou "Structured Scaling of AI Discovery Across
Diverse Scientific Domains" (surfaced same 09-01 batch as a companion).

---

### 9. Qin, Zeng, Ma, Ge, Tham, Shah, Eils — *Autonomous agentic artificial intelligence systems in health care: friend or foe?*
**Venue:** *The Lancet Digital Health*, 2026.
**Surfaced via:** Google Scholar alerts (09-01 11:36Z, Nigam Shah
new-articles feed).
**Threads:** Causal inference and pharmacoepi (agentic sub-thread);
Machine learning for precision health (decision-tied evaluation, safety
framing); Knowledge representation in EHRs (deployment-side).

**What it is (from snippet).** A **positioning piece from Shah + Eils
+ Tham** on autonomous agentic AI systems in health care, with an
explicit friend-or-foe frame around pre-deployment evaluation, ongoing
monitoring, and accountability. From the "before deployment, ..." lead
sentence, this is the deploy-side accountability paper for agentic
systems in clinical care.

**Why it matters for your work.** Complements the Fang/Zitnik piece
above: Fang/Zitnik on the biomedical-discovery-loop side, Qin/Shah on
the health-care-deployment side. Together they bracket the agentic
sub-thread you added under `Causal inference and pharmacoepi` and the
`Machine learning for precision health` thread's "generic benchmark
papers are SKIP; decision-tied papers are HIGH" bar — this one clears
the bar because it is explicitly deployment-tied.

**Contrast against:** Fang et al. Closing-the-Loop (Report #8); Chou/
Kallus `oci-agent`; Nigam Shah / Ethan Goh prior evaluation-framework
work; the Ellershaw et al. Foresight-England national-scale EHR-FM
paper (prior window) as the FM-side deploy substrate.

---

### 10. Garofalo, Chotiprasidhi, Johnson et al. — *Multi-ancestry sequencing analysis in 293,141 participants identifies predisposition DNA repair genes associated with HCC risk*
**Venue:** *JHEP Reports*, 2026.
**Surfaced via:** Google Scholar alerts (09-02 02:01Z, `"All of Us
research program"` keyword feed).
**Threads:** Biobanks with EHR linkage (AoU + MVP joint analysis);
Rare-variant / cross-ancestry genetic epi; Variant interpretation
(ACMG / ClinGen — DNA-repair gene predisposition).

**What it is (from snippet).** **Multi-ancestry sequencing analysis in
293,141 participants**, drawing on **All of Us Controlled Tier v8** +
**Million Veteran Program** (MVP), identifying predisposition DNA-repair
genes associated with HCC (hepatocellular carcinoma) risk.

**Why it matters for your work.** Two hits at once. (a) Study-design
template: AoU CTv8 + MVP joint rare-variant analysis at biobank scale is
exactly the design pattern your `Biobanks with EHR linkage` thread
wants propagated. (b) On DNA-repair predisposition for a solid tumor,
this is a natural addition to your ACMG / ClinGen VCEP / pLoF-burden
watch — expect an accompanying gene-list with penetrance estimates that
you can compare to the ClinVar predisposition-cancer VCEP curations.

**Contrast against:** Acharya et al. *Journal of Human Genetics* 2026
three-biobank ASCVD (prior window, similar design template on a
different disease); Kessler-lineage MVP rare-variant work; UK Biobank
WES pLoF-burden HCC papers.

---

### 11. Liu, Mizani, Zhao, Wood, Inouye, Price, Jiang & CVD-COVID-UK/COVID-IMPACT Consortium — *Predicting COVID-19 hospitalisation and common disease risk from comorbid diagnoses in 13 million individuals*
**Venue:** medRxiv, 2026 (DOI 2026.08.27.26361302).
**Surfaced via:** medRxiv Collection alert (09-02 00:05Z, Health
Informatics collection).
**Threads:** Chronic disease clustering and multimorbidity (national-
scale); EHR foundation models (comorbidity representation); PGS /
common-disease risk (Alkes Price + Michael Inouye authorship).

**What it is (from author + collection signal).** **National-scale (13
million individuals) prediction of COVID-19 hospitalisation and common-
disease risk** from a comorbidity-diagnosis representation of each
patient's EHR. Uses the CVD-COVID-UK/COVID-IMPACT Consortium data
(NHS-linked, HDR UK). Price + Inouye authorship signals a PRS-aware
comorbidity-graph representation.

**Why it matters for your work.** This is the multimorbidity-at-scale
paper that pairs directly with the Ellershaw et al. Foresight-England
national-scale EHR-FM paper from the prior window: same national NHS
data substrate, complementary framing (Foresight = generative FM;
this paper = comorbidity-representation predictive model). On the
`Chronic disease clustering and multimorbidity` thread, the 13-million
scale is the ceiling for the field at present, and worth citing as a
scale anchor. Also relevant to your `Knowledge representation in EHRs
→ Concept-level, structural, and temporal representation` axis:
comorbid-diagnosis vectors are one representation choice among several
(vs. event sequences, vs. graph embeddings), and this paper's scale
lets it speak to which choice pays off downstream.

**Contrast against:** Ellershaw et al. Foresight-England (prior window);
Burkhart et al. federated GEMs (prior window); MOTOR / CLMBR / MEDS
lineage; N3C consortium papers.

---

### 12. Witham, Evison, Bellass, Cooper, Gallier, Pretorius, Sapey, Suklan, Sayer — *People living with multiple long-term conditions have different pathways of unscheduled care in hospital: findings from an analysis of routinely-collected clinical data*
**Venue:** medRxiv, 2026 (DOI 2026.08.28.26361696).
**Surfaced via:** medRxiv Collection alert (09-02 00:05Z, Health
Informatics collection).
**Threads:** Chronic disease clustering and multimorbidity (Sayer-
lineage MLTC work); EHR phenotyping (routine-clinical-data pathways).

**What it is.** Uses routinely-collected hospital clinical data to
characterize how patients with **multiple long-term conditions (MLTC)**
follow **different pathways of unscheduled care**. Sayer-lineage
multimorbidity paper.

**Why it matters for your work.** Direct on-thread for `Chronic
disease clustering and multimorbidity → disease trajectories from EHR`.
Methods-watch value: how the paper defines a "pathway" from routinely-
collected data is portable to your CFTR-modulator persistence /
statin-discontinuation / HRT-persistence work under `Pharmacogenomic
modifiers of medication persistence`.

**Contrast against:** Cassell / Barnett MLTC trajectory work; Kudamala
et al. arXiv 2608.21589 AoU functional-decline prediction (prior
window); NetMoint UKB dementia trajectory paper (prior window).

---

### 13. Wiel, Ferraro, Yu, Zhen, Nachun, Mendez, Reuter, Cui, Bonner, Carter, Marwaha, van de Vorst, Emami, Kravets, Neu, van Ham, Kleefstra, Ashley, Bernstein, Montgomery, Gilissen, Wheeler — *MetaDome 2027: a comprehensively updated resource for aggregating missense variant evidence across homologous human protein domains*
**Venue:** bioRxiv, 2026 (DOI 2026.08.26.747388).
**Surfaced via:** bioRxiv Collection alert (09-02 00:02Z, Bioinformatics
collection).
**Threads:** Variant interpretation (ACMG / ClinGen); Rare disease
(missense-variant-driven Mendelian).

**What it is.** A comprehensively **updated release of MetaDome**
(named "MetaDome 2027" in the title), aggregating missense-variant
evidence across homologous human protein domains. Wheeler / Bernstein /
Ashley (Stanford Undiagnosed Diseases lineage), Montgomery, and
Gilissen (Nijmegen rare-disease lineage) authorship signals a
production-grade rare-disease-diagnosis resource.

**Why it matters for your work.** Direct-hit for `Variant interpretation
(ACMG / ClinGen)`: the tooling side (aggregating homologous-domain
evidence for missense) is the ClinGen-style *paralog / domain* evidence
class (PP3-adjacent), and MetaDome 2027 with a fresh evidence-base is
the reference tool for that. Also on-thread for `Rare disease` — the
Stanford UDN + Nijmegen author list is the target user base.

**Contrast against:** MetaDome (original Wiel 2019); AlphaMissense
2023; ClinGen VCEP guidelines; REVEL / ESM1b missense predictors;
LOFTEE / gnomAD-constraint (for the pLoF side).

---

### 14. Song, Ni, Liu, Li, Malin, Yin — *CPT/HCPCS Code Recommendation from Clinical Notes: A Comparative Evaluation of AI Methods*
**Venue:** medRxiv, 2026 (DOI 2026.08.29.26361731).
**Surfaced via:** medRxiv Collection alert (09-02 00:05Z, Health
Informatics collection).
**Threads:** Knowledge representation in EHRs → NLP-derived
representations from clinical notes AND Concept normalization and
vocabulary mappings; EHR phenotyping & OMOP (adjacent).

**What it is (from title).** A **comparative evaluation of AI methods
for recommending CPT/HCPCS procedure codes** from clinical notes.
Malin/Yin lineage (Vanderbilt informatics).

**Why it matters for your work.** Direct hit for
`NLP-derived representations from clinical notes → LLM /
transformer-based concept extraction, HPO / SNOMED term assignment`.
CPT/HCPCS is the procedure-code axis of your Concept normalization
sub-thread (ICD / phecode / RxNorm / SNOMED / LOINC being the
diagnosis / medication / concept / lab axes). Comparative-methods
evaluation is the useful framing — encoder-based LMs vs. frontier LLMs
for structured-code assignment, same auditing pattern as the Xue et al.
psychiatric-concept extraction paper (prior window) and the Wu et al.
ACT phenotyping paper (prior window).

**Contrast against:** ClaimGuard; Xue et al. medRxiv 2026 psychiatric
concept extraction (prior window); Wu et al. arXiv 2608.25948 ACT
auditable CT phenotyping (prior window); RadBERT / SapBERT.

---

### 15. Zhang, Zhang, Cheng, Gong, Kou, Jiang — *Explainable Plasma Proteomics-Based Machine Learning for Osteoporosis Diagnosis, Prognosis, and Protein Biomarker Discovery in the UK Biobank*
**Venue:** *The FASEB Journal*, 2026 (DOI 10.1096/fj.202600647R).
**Surfaced via:** Google Scholar alerts (09-02 02:01Z, `"UK Biobank"`
keyword feed).
**Threads:** Genetic epidemiology → Multi-omics-augmented PRS
(proteomics side); Biobanks with EHR linkage (UKB Olink); Machine
learning for precision health (decision-tied: osteoporosis fracture
risk).

**What it is (from snippet).** Uses **UK Biobank plasma proteomic and
clinical data** to develop **SPX-OP**, an explainable ML pipeline for
osteoporosis diagnosis, prognosis, and protein-biomarker discovery. OP
outcomes ascertained from UK Biobank first-occurrence records.

**Why it matters for your work.** On the multi-omics-augmented PRS
axis, this is the third UKB Olink paper in a short window (with Zheng
et al. on neurodegeneration and Weyrich et al. on CHIP/LOY). All three
argue for the *complementary* rather than *substitutive* role of
proteomics vs. genetics in outcome prediction. The "explainable" (SHAP-
family) framing keeps it on the right side of your `ML papers are HIGH
when tied to a clinical decision; generic-benchmark papers SKIP` bar.

**Contrast against:** Shan et al. UKB 2026 multi-omics PRS (prior
window); Zheng et al. medRxiv PGS × proteomic RS divergence
(Report #2); Weyrich et al. CHIP/LOY proteomic programs (Report #5);
Sun et al. UKB Olink osteoporosis-related prior work.

---

## Also-noted (worth naming, not opening first)

- **Strawbridge, McQueen, Kendall, Anderson et al.** — Genetic
  predisposition to schizophrenia and circulating proteins in 44,661 UKB
  participants (Research Square, 2026). PRS-SCZ × 1,459 Olink proteins.
  On the same axis as Zheng et al. (Report #2) but for psychiatric
  proteomics.
- **Efthymiou, Tabata, Salimi Dafsari et al.** — Loss of RUBCN causes
  autophagy overdrive in a neurodevelopmental disorder with
  age-dependent neurodegeneration (medRxiv 2026). Ultra-rare Mendelian
  case series with mechanism + HPO-relevant phenotype spectrum;
  methods-watch for rare-disease reanalysis pipelines.
- **Kudamala et al.** arXiv 2608.21589 continues to be named in these
  reports as the AoU aging/multimorbidity longitudinal-labs-and-vitals
  paper worth checking alongside the Kohler et al. openEHR-repository
  survey and the Liu et al. 13M-scale comorbidity paper (Report #11).
- **Zhao, Han, Goel, Dagan, Dagan, Madduri et al.** — *Rare Diseases,
  Common Dilemmas: LLMs Prioritize Equal Resource Distribution over
  Patient Benefit in Decision-Making* (arXiv, Isaac Kohane feed).
  Off-thread for methods but on-thread for the rare-disease-LLM
  benchmarking axis; pair with GraphRareBench (Guo et al. arXiv
  2607.24878, INTERESTS.md reference).
- **Chen et al. MOCR-DB** — Multi-Omics Causal Resource Database
  (Karczewski citation feed); worth naming as a substrate for the
  drug-target-MR triangulation sub-thread (Saxby lineage) but not
  a decision-tied HIGH item on its own.
- **James Zou** — Structured Scaling of AI Discovery Across Diverse
  Scientific Domains (author feed). Companion positioning piece to the
  Fang/Zitnik loop-closing paper (Report #8).
- **JAMA companion RCTs** — Ng et al. SOLARIS high-dose vitamin D3 in
  metastatic CRC (Alliance A021703); Clarençon et al. DISCOUNT
  medium/distal-vessel thrombectomy; Zaidat et al. TESLA one-year
  outcomes. MED for you but not on the tracked drug threads.
- **ML4H seminar** — "Reducing Diagnostic Delay Through Early Disease
  Detection: Endometriosis as a Case Study" (Broad ML4H, 09-01). Same
  axis as the Ran/Benatar ALS-phenoconversion reference in
  INTERESTS.md; worth watching the video if released.

---

## Cross-report continuity notes

The three papers most worth reading against each other, in this order:
1. **Lassen et al.** *Nat Commun* rare-variant deviations from
   additivity — the theoretical / methods substrate.
2. **Zheng et al.** medRxiv PGS × proteomic RS divergence in
   neurodegeneration — the applied-genetic-epi paper that hunts for
   *which biological modules* explain the residual after additivity.
3. **Weyrich et al.** medRxiv CHIP + mLOY proteomic programs — the
   somatic-mosaicism companion showing the same "distinct proteomic
   programs" pattern for age-related somatic-mosaic exposures.

Together they trace one axis you already prioritize in INTERESTS.md:
germline PGS (additive) → germline PGS (rare-variant nonadditive) →
germline + somatic mosaicism, each on a proteomic read-out.

And the pharmacoepi anchor for the SGLT2i sub-thread now has both an
observational calibrated estimate (Zhang et al. *Diabetes, Obesity &
Metabolism*, prior window) and a hard RCT (Oosterom-Eijmael et al.
*JAMA*, this window) for perioperative-AKI. The two together are the
canonical RWE-vs-RCT triangulation setup for the CFTR-modulator and
GLP-1 persistence writing.
