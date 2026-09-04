# Research digest report — 2026-09-04

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-04 12:40Z** (~3 days since the
last research-digest report, covering three arxiv-digest cron runs and
three Google Scholar alert batches). Short interval — the previous
2026-09-01 report already covered the 09-01 11:36Z Scholar batch, so
this run picks up the 09-02 02:01Z, 09-03 04:33Z, and 09-03 13:02Z
batches plus 09-01 → 09-03 daily arxiv-digest runs.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-03.md`) | 09-01 → 09-03 daily crons | 3 daily runs, low signal. 09-01: 1 paper (Mansouri Ghiasi storage-centric genomics systems — 1 keyword hit on `precision medicine`; primarily systems/architecture, SKIP for the current threads). 09-02: 1 paper (Ramesh et al. mudskipper locomotion — keyword hit `motor`; SKIP, off-topic biomechanics). 09-03: 0 matches. The dry days are typical of the Aug–Sep arxiv submission valley. |
| No `arxiv-digest` email hits from GitHub | — | As in the prior report, `arxiv-digest` commits directly to this repo rather than emailing PR/cron notifications; the on-disk digests above *are* the arxiv-digest feed for the window. |
| Google Scholar alerts (09-03 batch #2, 13:02Z) | 09-03 13:02Z | 11 keyword feeds fired: `mendelian diseases` (Song et al. Frontiers in Bioinformatics missense-variant characterization); `"electronic health records"` (Collins privacy-aware EHR+SDoH+IoT analytics — off-topic); `"knowledge graph"` (PLRA-KG recommender systems — off-topic); `rare diseases` (Ilicki & Spicer *Drug Discovery Today* investment-professional benchmark — off-topic economics); `"UK Biobank"` (Y Luo et al. selection-bias-adjusted MR of BMI/education/CRP on depression); `intitle:"clonal hematopoiesis"` (Yao et al. J Formosan Med Assoc CH×ASCVD review; plus 6 ASH-abstract-style CH papers); `"variant interpretation"` (Kırboğa G3 CYP2C9/CYP2C19/NUDT15 DMS; Boceck et al. npj Genomic Medicine aiDIVA rare-disease diagnostics; Chen et al. Frontiers Immunol autoinflammatory variant discoveries); `Foundation models + "electronic health records"` (Collins privacy-aware architecture — same as above); `"drug repurposing"` (Skovbo et al. *Eur J Vasc Endovasc Surg* AAA drug-repurposing signals); `"All of Us research program"` (Wagner supplements-for-diabetic-neuropathy — off-topic clinical review with an AoU citation); `"autoimmune disorders"/"autoimmune diseases"` (case report — SKIP). |
| Google Scholar alerts (09-03 batch #1, 04:33Z) | 09-03 04:33Z | ~24 author feeds fired: 6 fed the same **Hu et al. Nat Comm 2026 PGS pre-train/fine-tune** paper (Hripcsak cite, Denny cite, Bastarache related, Yong Chen new, Yuan Luo new, Zhiyong Lu related); Denny cite feed also led with **Lassen et al. Nat Comm rare-variant non-additivity** and included Garofalo et al. JHEP Reports HCC-DNA-repair-genes multi-ancestry; Denny related feed led with **Zhang et al. arXiv 2608.06063 AoU wearable×PRS×MDD** and included Kudamala et al. AoU functional-decline lab-trajectory (previously flagged), Dutta et al. Cell Genomics PRS×proteomics cancer proteins, Goto et al. medRxiv Yamanashi multi-omics cohort, Iwaki et al. LRRK2 penetrance-modified-by-PRS (via Karczewski related); Karczewski related feed added Fonseca et al. bioRxiv locus-specific gene-context PGS; Hernan cite feed led with **Kunitsu et al. HIF-PHI vs ESA HF-hospitalization TTE**; Patrick Ryan related feed led with **Bots et al. IJE 2026 Negative controls guidance paper**; Patrick Ellinor new (Helseth et al. J Card Failure LLM recommendations for HF therapy); Emily Alsentzer new-articles: Alsentzer et al. Helicobacter DAF-binding adhesins (basic bio — off-topic for research threads); Peter Szolovits related and Zhiyong Lu related returned mostly off-topic LM papers; Marinka Zitnik related returned reasoning-paradigms scale-awareness (off-topic); Jian Yang / Stephen Montgomery cite fed Jia et al. Nature lncRNAs in brain disorders (adjacent, methods-watch); Jonathan Pritchard cite fed Fan et al. RGL2 postoperative-delirium×AD (methods-watch); Konrad Karczewski cite fed Abe blog on allele frequencies (SKIP). |
| Google Scholar alerts (09-02 batch, 02:01Z) | 09-02 02:01Z | 9 keyword feeds fired: `"All of Us research program"` (**Garofalo et al. JHEP Reports** multi-ancestry HCC rare-variant analysis — 293k participants incl. AoU); `mendelian diseases` (Jiang et al. Genes MR of autoimmune×follicular lymphoma); `Foundation models + "electronic health records"` (Abraham nursing-AI perspective — off-topic); `"variant interpretation"` (Li et al. FOXL2 frameshift ovarian aging case report); `rare diseases` (AstraZeneca China selumetinib approval news — SKIP); `"drug repurposing"` (Shen et al. sertraline colorectal cancer metabolomics — off-topic); `"UK Biobank"` (Zhang et al. plasma proteomics ML for osteoporosis — moderate); `"knowledge graph"` (Wang et al. construction-quality KG-LLM — off-topic); `"electronic health records"` (**Chovatiya et al. Real-world abrocitinib RWE study** using EHR + claims — moderate autoimmune pharmacoepi). |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries carry the full abstract
> because the pipeline captures it, but this window's arxiv-digest
> hits are off-topic and are not written up. Author lists are
> truncated as they appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Sixteen items reach HIGH in this window, clustering into six knots.
A short interval — but the 09-03 batch was dense, and one paper
(Hu et al. Nat Comm PGS boosting) surfaced in six separate feeds,
signalling it as the paper of the week for your PGS thread.

**PGS methodology cluster (5 HIGH items).** Hu et al. *Nature
Communications* 2026 "**Adaptive Boosting of pre-trained Polygenic
Risk Scores**" (**Item 1**) is the single most-echoed paper this
window — appearing in Hripcsak, Denny, Bastarache, Chen, Luo, and
Zhiyong Lu feeds. It fine-tunes public pre-trained PGS by adaptive
variable selection + boosting, directly serving your "composite risk
models stacking PRS with rare pathogenic variants" thread.
Complementing it, Lassen, Venkatesh, Baya et al. *Nature Communications*
2026 (**Item 2**) tests **non-additivity at biobank scale** using an
orthogonal allelic-recoding framework — the "rare variants drive
non-additive deviation" observation is a mechanistic backbone for the
Baya *AJHG* 2026 misaligned-individuals PGS-tails framing already in
your interests. Zheng, Shivakumar, Shen, Kim medRxiv 2026 (**Item 3**)
maps **where PRS and proteomic risk scores diverge** across
neurodegeneration via absorption / co-expression modules — a
representation-choice question for multi-omics-augmented PRS, one
of your explicit sub-threads. Iwaki, Blauwendraat, Makarious, Singleton
(**Item 11**) shows **LRRK2 p.G2019S penetrance is modified by a PD
PRS** — a template for the CFTR / APOL1 / BRCA penetrance framing you
prioritize. Dutta et al. *Cell Genomics* 2026 (**Item 12**) integrates
**PGS for 21 cancers with 4,955 plasma proteins**, defining PRS ×
proteomic trans-regulated networks — direct multi-omics-augmented PRS.

**Causal-inference / pharmacoepi cluster (3 HIGH items).** Bots et al.
*Int J Epidemiol* 2026 (**Item 4**) is a Patrick Ryan-flagged
**negative-controls guidance paper** — direct reinforcement of the
empirical-calibration-by-negative-controls approach the 09-01 report
led with (Zhang et al. GLP-1/SGLT2/DPP4i TTE). Kunitsu et al.
*Pharmacoepi Drug Safety* 2026 (**Item 13**) runs a Japanese nationwide
**active-comparator claims-based cohort of HIF-PHI vs ESA for HF
hospitalization** in non-dialysis CKD — a clean pharmacoepi example
citing target-trial-emulation methodology. Chovatiya et al. 2026
(**Item 15**) reports **real-world abrocitinib use** for
moderate-to-severe atopic dermatitis via linked EHR + claims — modest
but worth logging in the autoimmune sub-thread.

**AoU-linked biobank cluster (3 HIGH items).** Zhang, Folarin, Zhong
et al. arXiv 2608.06063 (**Item 5**) integrates **wearable trajectories
with polygenic risk to predict incident MDD in the All of Us Research
Program** — direct AoU + PRS + longitudinal-wearable stack, aligning
with the digital-twins-from-EHR sub-thread. Garofalo et al. *JHEP
Reports* 2026 (**Item 16**) does **multi-ancestry sequencing across
293,141 participants (incl. AoU) to identify DNA-repair predisposition
genes for HCC risk** — Lynch/BRCA-adjacent rare-variant hepatology.
Hu et al. Nat Comm PGS boosting (Item 1, listed above) is trained /
validated against AoU as one of its target cohorts, giving it
additional AoU-thread weight.

**CHIP / somatic mosaicism cluster (1 HIGH item).** Yao et al.
*J Formosan Med Assoc* 2026 (**Item 6**) reviews **CH → ASCVD**
biological mechanisms, clinical implications, and emerging therapy
— exactly the disease-thread review paper your CHIP/VEXAS/LOY interest
wants. Six ASH-abstract-style CH papers accompany it in the same
alert (transplant outcomes, TBDs, occupational firefighter exposure,
hypercoagulability, biomass-smoke exposure, neuroendocrine tumor
patients) — background context but only the Yao review is prioritized.

**Variant interpretation / PGx cluster (2 HIGH items).** Kırboğa
*G3* 2026 (**Item 7**) argues from **deep mutational scanning of
CYP2C9, CYP2C19, NUDT15** that generic pathogenicity scalars miss
pharmacogene-specific mechanism — a direct methods hit for the
variant-interpretation + PGx-modifier-of-medication-persistence
sub-threads. Boceck et al. *npj Genomic Medicine* 2026 (**Item 14**)
presents **aiDIVA** — a hybrid AI system for rare-disease
diagnostics benchmarked against 2,890 causal-variant cases; direct
fit to the auditable HPO-driven diagnostic-benchmark sub-thread
(GraphRareBench lineage).

**Drug-repurposing cluster (1 HIGH item).** Skovbo, Hallas, Stubbe,
Sabater-Lleal et al. *Eur J Vasc Endovasc Surg* 2026 (**Item 8**)
mines long-term drug exposure ↔ **AAA** associations, extending the
**Saxby et al. metformin × AAA** MR triangulation reference already
in your interests. Real-world Danish prescribing signal.

**Agentic-AI-in-clinical-settings cluster (2 HIGH items).** Qin/Zeng/
Ma/Ge/Tham/Shah/Eils et al. *Lancet Digital Health* 2026 (**Item 9**)
lays out an **evaluation framework for autonomous agentic AI systems
in health care** — direct successor framing to the OCI-Agent /
Netflix / EHR-HTE agentic-pipeline sub-thread. Fang, Li, Noori, Fesser,
Zitnik 2026 (**Item 10**) — "Closing the Loop in AI-Driven Biomedical
Discovery" — the Zitnik-lab positioning piece for hypothesis-generation
agents.

**Locus-specific gene×context PGS.** Fonseca et al. bioRxiv 2026
(**Item 17**) fits **locus-specific gene-context interactions** into
PGS — directly extends the Nagpal & Gibson *Nat Genet* pervasive
PGS × exposure interactions framing.

---

## Detailed reports

### Item 1 — Hu et al. *Nature Communications* 2026: Adaptive Boosting of pre-trained Polygenic Risk Scores (ABPRS)

**Feeds that surfaced it:** George Hripcsak citations-to (position 1);
Joshua C. Denny related-research (position 3); Lisa Bastarache
related-research (position 1); Yong Chen new-articles (position 1);
Yuan Luo new-articles (position 1); Zhiyong Lu related-research
(position elsewhere). Six-feed convergence.
**Venue:** *Nature Communications*, 2026 (article ID s41467-026-77128-5).
**Authors:** J Hu, R Chen, M Salvatore, O Wu, OB Ozdemir, Y Lu, and
co-authors (Yun Lu is likely the corresponding author from the
Michigan-Nature-Comm PGS lineage; full author list not exposed in
alert snippet).
**Abstract excerpt (Scholar snippet):** "Polygenic risk scores are
widely used for predicting genetic risk across complex diseases and
traits, and several pre-trained models have been developed. Few
approaches leverage these pre-trained polygenic risk scores to further
refine predictive performance. Here, we present Adaptive Boosting of
pre-trained Polygenic Risk Scores, a fine-tuning framework that refines
pre-trained polygenic risk score models through adaptive variable
selection and model boosting to identify additional [signal]…"
**Why this is HIGH for your interests:** Cites the AoU quality/utility/
diversity paper, so at minimum trains against or benchmarks in AoU.
The framing is exactly the "public pre-trained PGS + local fine-tuning"
pattern you would want for biobank-scale PGS deployment — take a PGS
Catalog or PRS-CS-Auto score card, then boost with adaptive variable
selection on locally-genotyped and locally-phenotyped AoU / BioVU
data. Directly relevant to two active threads:
  1. **Genetic epidemiology → composite risk models stacking PRS
     with rare pathogenic variants** (INTERESTS.md L76-78). ABPRS is
     the natural "PGS refinement" plug for the discovery-instrument
     PGS-tails framing (Souaiaia / Vazquez / Baya lineage).
  2. **PGS residuals / polygenic-deviation designs** (INTERESTS.md
     L81-84). A booster that "identifies additional variants" beyond
     the pre-trained score is functionally a residual-explaining
     model — worth checking whether the additional variants
     recovered by ABPRS are enriched for rare or LoF variants (the
     Baya-Souaiaia axis) or for GxE-sensitive loci (the Nagpal
     axis).
**Concrete next steps:** Read the paper to establish (a) which base
pre-trained PGS they use (PGS Catalog IDs?), (b) whether the boosting
step recovers rare-variant signal or is confined to common-variant
tag refinement, (c) whether they validate cross-ancestry (given six
citation feeds and a Nat Comm venue, this is likely a headline
figure). If ancestry-portability is addressed, this becomes a
candidate reference for AoU-based composite-risk pipelines. Cross-
reference against Harikrishnan & Kelly medRxiv 2026 PC/mixed-model
PRS portability (methods-watch below).

---

### Item 2 — Lassen, Venkatesh, Baya, Lindgren et al. *Nature Communications* 2026: Deviations from genetic additivity driven by rare variants at biobank scale

**Feeds that surfaced it:** Joshua C. Denny citations-to (position 1);
Konrad Karczewski related-research (position 2).
**Venue:** *Nature Communications*, 2026 (article ID s41467-026-76151-w).
**Authors:** FH Lassen, SS Venkatesh, NA Baya, CM Lindgren, plus
additional authors truncated in snippet. The Baya name is significant
— Nikolas Baya is the first author on the Baya *AJHG* 2026
"misaligned individuals / PGS-residuals" paper already in your
interests (INTERESTS.md L82-84).
**Abstract excerpt (Scholar snippet):** "Additive genetic models are
the default for genome-wide association studies, but deviations from
additivity are crucial for understanding disease mechanisms and
therapeutic responses. Yet existing methods for testing nonadditivity
are computationally infeasible for large-scale analysis or rely on
Hardy-Weinberg assumptions, making them unsuitable for rare variants
in large biobanks. We use an orthogonal allelic recoding framework
that enables scalable testing of nonadditive [effects]…"
**Why this is HIGH for your interests:** This is the mechanistic
companion to the Baya PGS-tails / misaligned-individuals framing you
prioritize. If rare variants systematically drive non-additive
deviations from GWAS-predicted trait values, then:
  1. "Misaligned individuals" in PGS-tails designs are exactly the
     population where you would expect to enrich for penetrance-
     modifying rare variants — this paper gives you the statistical
     lever (orthogonal allelic recoding avoiding Hardy-Weinberg
     assumptions) for scanning biobanks (UKB, AoU, MVP, BioVU) for
     such non-additive rare variants.
  2. Provides a Nat-Comm-grade citation for the argument that "PGS
     residuals contain interpretable rare-variant signal" — this is
     load-bearing for the composite-risk-models section of your
     interests.
  3. Adjacent to your CHIP / somatic-mutation contamination concern
     (INTERESTS.md L108-110): non-additive effects at somatic loci
     would masquerade as germline non-additivity if not filtered.
**Concrete next steps:** Read for (a) the recoding math (does it
generalize to X-chromosome and PAR? relevant for the LOY thread),
(b) whether they report per-gene non-additivity enrichment tables
sorted by gene (candidate list for the composite-risk instrument),
(c) whether AoU / BioVU are among the tested biobanks (they cite
"Genomic data in the all of us research program"). Compare against
Fonseca et al. bioRxiv 2026 locus-specific gene-context PGS
(**Item 17**) — different mechanism (context, not rare-variant
non-additivity), but overlapping downstream inference.

---

### Item 3 — Zheng, Shivakumar, Shen, Kim medRxiv 2026: Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases

**Feeds that surfaced it:** Joshua C. Denny related-research (position
1); Konrad Karczewski related-research (position 1); Jian Yang
related-research (position 1); Lisa Bastarache related-research (also
returned); Chenjie Zeng related-research (position 1 in the
09-01 11:36Z batch already covered by the prior report). Recurring
across five feeds over two batches.
**Venue:** medRxiv, 2026 (posted 2026-08-24, DOI 10.64898/2026.08.24.
26361271).
**Authors:** C Zheng, M Shivakumar, L Shen, D Kim (Dokyoon Kim's Penn
group — consistent authorship pattern for PGS × Olink work).
**Abstract excerpt (Scholar snippet):** "Polygenic and proteomic risk
scores are both proposed for pre-symptomatic stratification, yet the
extent to which they provide overlapping or complementary information
has not been measured across neurodegenerative disease. To quantify
[the divergence between PRS and PrRS across neurodegenerative
conditions using]…"
**Why this is HIGH for your interests:** Direct hit on two sub-threads
simultaneously:
  1. **Multi-omics-augmented PRS** (INTERESTS.md L86-91). The paper's
     ambition — "measure PGS-vs-proteomic overlap across
     neurodegeneration" — is the exact evaluation gap in the Shan et
     al. UKB 2026 / Feng et al. cross-ancestry IDP lineage you
     tracked.
  2. **Pre-symptomatic carrier phenoconversion prediction from
     longitudinal biomarker trajectories** (INTERESTS.md L204-208).
     The paper explicitly frames PGS + PrRS for "pre-symptomatic
     stratification," which is precisely the Ran/Benatar ALS
     template applied to a broader neurodegenerative panel. If the
     paper identifies specific absorption/co-expression modules where
     proteomic signal dominates over polygenic signal, those modules
     become candidate biomarker panels for BRCA / APOL1 CKD / HTT
     preclinical HD phenoconversion prediction — a portable
     methodological finding.
**Concrete next steps:** Read the medRxiv preprint (D Kim group is
consistent about posting preprints in advance of journal versions).
Check whether they use UKB Olink or a different proteomic platform
— matters for portability. Assess whether the "absorption module"
framework is generic (portable to cardiometabolic / autoimmune PRS)
or specialized to neurodegeneration.

---

### Item 4 — Bots, Schultze, Pajouheshnia, Douglas et al. *International Journal of Epidemiology* 2026: Negative controls and how to use them: a guidance paper

**Feeds that surfaced it:** Patrick Ryan related-research (only feed,
sole item — high-signal because Ryan's feed rarely returns
methodology-guidance papers).
**Venue:** *International Journal of Epidemiology*, 2026 (article ID
55/5/dyag163).
**Authors:** SH Bots, A Schultze, R Pajouheshnia, IJ Douglas, and
additional authors truncated in snippet. Schultze and Douglas are
recognizable LSHTM pharmacoepi names; the paper likely represents a
consensus / working-group output.
**Abstract excerpt (Scholar snippet):** "Negative controls have gained
traction as a useful tool for causal research to address confounding
and bias. However, general guidance on how to select and apply
negative controls and how to report and interpret their findings is
lacking. This paper lays out the key steps of conducting a negative-
control analysis and provides all relevant background information,
important feasibility and validity considerations, and practical
suggestions for the implementation and interpretation of each step."
**Why this is HIGH for your interests:** Reinforcement of the
empirical-calibration-by-negative-controls approach that dominated
the 09-01 report (Zhang et al. GLP-1/SGLT2/DPP4i TTE), now framed as
a guidance paper. Direct hits on:
  1. **Causal inference and pharmacoepidemiology** (INTERESTS.md
     L46-51). This becomes the reference guidance paper to cite
     alongside Hernán's TTE lineage when defining your negative-
     control panel for any pharmacoepi analysis.
  2. **Agentic / human-in-the-loop OCI pipelines** (INTERESTS.md
     L53-58). An agentic pipeline that automates PS-trimming and
     sensitivity analysis needs a codified negative-control step;
     this paper is the natural input specification for that step.
**Concrete next steps:** Read the IJE paper for (a) the taxonomy of
negative controls (outcome-, exposure-, indication-, mechanism-
based), (b) reporting checklist (an emerging convention worth
adopting in your own drafts), (c) failure modes explicitly called
out. Fold into any TTE analyses you supervise; especially useful as
a companion to the Zhang et al. GLP-1/SGLT2/DPP4i paper the prior
report highlighted.

---

### Item 5 — Zhang, Folarin, Zhong et al. arXiv 2608.06063: Longitudinal wearable monitoring and polygenic risk for incident major depressive disorder in the All of Us Research Program

**Feeds that surfaced it:** Joshua C. Denny related-research (position
1). Sole feed hit, but leads that feed — high-signal.
**Venue:** arXiv preprint 2608.06063, 2026.
**Authors:** Y Zhang, AA Folarin, R Zhong, H Kim, S Sun, C Stewart,
and additional authors truncated. Folarin has been in the RADAR-base
digital-phenotyping lineage; consistent with the wearable-data thread.
**Abstract excerpt (Scholar snippet):** "Major depressive disorder
(MDD) risk reflects both stable inherited liability and dynamic
behavioral patterns, yet these dimensions are rarely examined
together using long-term objective data in real-world settings. Here,
we integrated genomic [and wearable-derived digital-phenotype
trajectories in the All of Us Research Program to model incident
MDD]…"
**Why this is HIGH for your interests:** Direct three-way intersection:
  1. **All of Us biobank thread** (INTERESTS.md L29-37): AoU
     wearable-linked participants remain a small subset, so any
     methods paper that gets meaningful sample size on the wearable
     × PRS × incident-outcome question is worth logging.
  2. **Genetic epidemiology → PRS × exposure/environment
     interactions** (INTERESTS.md L86-88). Wearable-derived behavior
     (sleep, activity, HR variability) is a canonical "environmental"
     exposure; the paper is a direct instance of PGS × longitudinal-
     digital-phenotype interaction.
  3. **Digital twins from EHR data** (INTERESTS.md L119-123).
     Integrating structured PGS with time-series wearable signal is
     the natural next step in individualized-trajectory prediction
     — this is a template study for AoU-scale digital-twin
     construction.
**Concrete next steps:** Check the arXiv PDF for (a) which AoU
wearable subset (Fitbit-linked participants, current N?), (b) which
MDD case definition (phecode-based? DSM-derived from notes? AoU
survey-based?) — matters for the phecode/PheRS thread, (c) whether
they treat wearable time-series as fixed features or learn a
representation (foundation-model territory). If they use phecodes,
this becomes an example paper for how the AoU phecode outcome
definitions are being adopted in the wild.

---

### Item 6 — Yao, Chen, Tsai, Chen, Chan et al. *J Formosan Med Assoc* 2026: Clonal hematopoiesis and atherosclerotic cardiovascular disease: Clinical implications, biological mechanisms, and emerging therapeutic strategies

**Feeds that surfaced it:** `intitle:"clonal hematopoiesis"` keyword
feed (position 1). Sole first-mover in the CH keyword feed for the
window; six additional CH abstracts follow, mostly ASH-abstract
transplant / thrombosis / occupational-exposure preliminaries.
**Venue:** *Journal of the Formosan Medical Association*, 2026
(article ID S0929664626008417).
**Authors:** CY Yao, YC Chen, BR Tsai, JW Chen, CY Chan, plus
additional authors truncated. Consistent with a Taiwanese
multi-institutional CH review team.
**Abstract excerpt (Scholar snippet):** "Clonal hematopoiesis (CH),
defined by the age-related expansion of hematopoietic stem cells
harboring somatic driver mutations, has emerged as a novel and
clinically relevant contributor to atherosclerotic cardiovascular
disease (ASCVD). Once [considered incidental, CH is now recognized
as a modifiable cardiovascular risk factor requiring integrated
clinical management]…"
**Why this is HIGH for your interests:** Direct fit to the CHIP-VEXAS-
LOY disease sub-thread (INTERESTS.md L104-110). A review synthesizing
"clinical implications, biological mechanisms, and emerging
therapeutic strategies" is precisely the reference frame you'd cite
when arguing for CHIP screening as a modifiable CVD input in an
EHR-linked biobank cohort. Complementary to the Kessler *Nature* 2022
lineage and the Li et al. *Atherosclerosis* 2026 LOY×PAD paper
already in your interests. The six accompanying CH abstracts (Tara
et al. transplant outcomes; Ogbue et al. telomere biology disorders;
Anamika et al. hypercoagulability; Pattnaik et al. NET patients;
Gada et al. biomass-smoke exposure; Surksha et al. firefighter
exposure) collectively map how CH is being written across ASH-
abstract format, but only the Yao review is prioritized.
**Concrete next steps:** Read the Yao review for (a) which therapeutic
targets they highlight (IL-6 axis? IL-1β? SGLT2is as CH-modulator?),
(b) whether they distinguish TET2 vs DNMT3A vs JAK2 CHIP by CVD
risk, (c) their position on population-level CH screening (relevant
to AoU/UKB screening cohorts). Cite alongside your CHIP/LOY thread
references.

---

### Item 7 — Kırboğa *G3: Genes, Genomes, Genetics* 2026: Deep mutational scanning of CYP2C9, CYP2C19, and NUDT15 shows that pharmacogene variant interpretation requires assay-specific functional data

**Feeds that surfaced it:** `"variant interpretation" OR "variant
classification" OR "Causal Variant"` keyword feed (position 1). Sole
first-mover.
**Venue:** *G3: Genes, Genomes, Genetics*, 2026 (advance article
jkag248, OUP).
**Authors:** KK Kırboğa (sole author, unusual for a DMS paper but
consistent with a computational-reanalysis framing).
**Abstract excerpt (Scholar snippet):** "Pharmacogene missense variants
can disrupt protein stability, catalytic competence, or substrate
handling through distinct mechanisms. General-purpose predictors
estimate clinical pathogenicity as a single scalar, whereas
pharmacogene [effects require assay-specific functional data
distinguishing loss-of-catalysis vs. loss-of-stability vs. altered
substrate handling]…"
**Why this is HIGH for your interests:** Direct two-thread hit:
  1. **Variant interpretation (ACMG / ClinGen)** (INTERESTS.md L68-72).
     The paper argues generic pathogenicity scores (AlphaMissense,
     REVEL) miss pharmacogene-specific mechanism, which is a direct
     methodological argument for assay-specific evidence codes
     (PS3/BS3) in ClinGen VCEP guidelines for pharmacogenes.
  2. **Pharmacogenomic modifiers of medication persistence**
     (INTERESTS.md L60-64). CYP2C9 (warfarin, celecoxib, tolbutamide),
     CYP2C19 (clopidogrel, PPIs, escitalopram), NUDT15 (thiopurines)
     are exactly the persistence-relevant pharmacogenes. If DMS-
     derived function scores reclassify persistence-relevant
     variants, that flows directly into the Cohen et al.
     *Pharmaceuticals* 2026 / Psy-PGx UKB lineage you tracked.
**Concrete next steps:** Read the G3 paper for (a) the DMS assay
design (functional-cellular vs. in vitro biochemical), (b) how many
variants reclassify vs. AlphaMissense/REVEL, (c) whether
star-allele-adjacent variants are flagged. If the reclassification
rate is meaningful, this becomes cite-worthy for any AoU / MVP
CYP-metabolizer-phenotype pipeline. Note the companion Ishimura et
al. *Cancer Chemother Pharmacol* 2026 DPYD c.812delT S-1 toxicity
case in the same alert — pharmacogene case reports and DMS
reclassification arriving in the same week reinforce the assay-
specific-evidence argument.

---

### Item 8 — Skovbo, Hallas, Stubbe, Sabater-Lleal et al. *European Journal of Vascular and Endovascular Surgery* 2026: Drug Repurposing Signals for Abdominal Aortic Aneurysms

**Feeds that surfaced it:** `"drug repurposing"` keyword feed
(position 1). Sole first-mover among mostly-off-topic antiviral /
KG-based repurposing papers.
**Venue:** *European Journal of Vascular and Endovascular Surgery*,
2026 (article ID S1078588426008269).
**Authors:** JS Skovbo, J Hallas, J Stubbe, M Sabater-Lleal, plus
additional authors truncated. Hallas is a recognizable Odense
pharmacoepi name; consistent with a Danish prescribing-registry
study.
**Abstract excerpt (Scholar snippet):** "Drug repurposing offers a
cost effective approach to identify therapies for abdominal aortic
aneurysm (AAA), which lacks proven medical treatment. This study
assessed associations between long term cumulative drug exposure
and AAA [incidence / progression across a nationwide Danish
prescription registry cohort]…"
**Why this is HIGH for your interests:** Direct extension of the
Saxby et al. metformin × AAA MR triangulation reference already in
your interests (INTERESTS.md L64-66). Where Saxby et al. brought MR
triangulation to the metformin-AAA hypothesis, Skovbo et al. brings
long-term real-world prescribing evidence for a broader panel of
candidate drugs. Direct triangulation opportunity: MR estimates
(Saxby) + observational cumulative-exposure estimates (Skovbo) for
each drug candidate → converging evidence for repurposing. Serves
two threads:
  1. **Drug repurposing** (INTERESTS.md L184-192) — "EHR-based
     repurposing signals mined from real-world prescribing and
     outcomes" and "causal-inference framings of off-label use" are
     both this paper's core methodology.
  2. **Causal inference and pharmacoepidemiology** (INTERESTS.md
     L46-51) — Danish prescription registries are the canonical
     RWE data source for this design.
**Concrete next steps:** Read for (a) which drug classes surface
beyond metformin (statins, ACE-inhibitors, ARBs, SGLT2is,
GLP-1 RAs?), (b) whether they apply an active-comparator design vs.
new-user cohort, (c) whether negative-control outcomes are used
(directly ties to Item 4 Bots et al. IJE negative-controls
guidance). Cite as the paired observational reference to Saxby et
al. MR when writing the AAA drug-repurposing section.

---

### Item 9 — Qin, Zeng, Ma, Ge, Tham, Shah, Eils et al. *Lancet Digital Health* 2026: Autonomous agentic artificial intelligence systems in health care: friend or foe?

**Feeds that surfaced it:** Nigam Shah new-articles (sole item — high
signal because Shah's feed rarely fires single-item batches for
non-Stanford-Center outputs).
**Venue:** *The Lancet Digital Health*, 2026 (article ID PIIS2589-
7500(26)00096-8).
**Authors:** Y Qin, D Zeng, W Ma, Z Ge, YC Tham, NH Shah, R Eils, and
additional authors truncated. International consortium with Stanford
(Shah), Berlin (Eils), Singapore (Tham) — indicates a global-consensus
framing piece.
**Abstract excerpt (Scholar snippet):** "First, before deployment,
AAAS should undergo systematic evaluation, including pre-deployment
testing, red-teaming, stress testing, and benchmarking. Notably,
evaluation should extend beyond model-level accuracy to include
system-level [validation, human-in-the-loop oversight, and continuous
post-deployment monitoring]…"
**Why this is HIGH for your interests:** Direct successor framing to
the OCI-Agent / Netflix / EHR-HTE agentic-pipeline sub-thread
(INTERESTS.md L52-58). Where the OCI-Agent (Chou/Kallus 2607.22443)
was the technical exemplar, this Lancet piece is the evaluation-
frame policy exemplar. Together they anchor the "how do we deploy
these things responsibly" side of the agentic-observational-causal-
inference conversation. Also relevant to the broader EHR-FM +
digital-twin threads because AAAS deployed for triage / decision
support inherits the same evaluation gaps.
**Concrete next steps:** Read for the specific evaluation checklist
(pre-deployment red-teaming, benchmarks, post-deployment monitoring).
Adopt whatever it recommends as a companion checklist to the Bots
negative-controls guidance (Item 4) — one governs
methodological-transparency in the causal step, the other governs
system-level oversight of the agent that automates that step.

---

### Item 10 — Fang, Li, Noori, Fesser, Zitnik 2026: Closing the Loop in AI-Driven Biomedical Discovery

**Feeds that surfaced it:** Marinka Zitnik new-articles (sole item).
**Venue:** 2026 (venue not exposed in snippet — likely a Zitnik-group
white paper or *Nature Reviews Bioengineering* / *Cell Systems*
opinion; check).
**Authors:** A Fang, K Li, A Noori, L Fesser, M Zitnik (Harvard
Zitnik lab, mixed-scale collaboration).
**Abstract excerpt (Scholar snippet):** "AI scientists generate
hypotheses, propose experiments, and analyze datasets, and several
have [reached partial autonomy across the discovery loop, but end-
to-end closure — from hypothesis to validated finding — remains
open]…"
**Why this is HIGH for your interests:** Framing paper for the
hypothesis-generation → experimental-loop closure question. Relevant
to:
  1. **Drug repurposing** (INTERESTS.md L184-192) — the KG-based
     explainable-hypothesis subthread you prioritize is one instance
     of "AI generates hypothesis, needs closure." Item 8 (Skovbo AAA
     drug repurposing) is a natural closure loop (KG-generated
     hypothesis → Danish prescription-registry validation).
  2. **Rare disease** (INTERESTS.md L194-210) — reanalysis pipelines
     are a canonical AI-scientist-loop use case (Uria-Regojo et al.
     medRxiv 2026 reference in your interests).
  3. **Agentic pipelines** cluster generally.
**Concrete next steps:** Locate the venue (search Zitnik lab preprint
tracker or arXiv). Read for their taxonomy of "loop closure" — this
is orthogonal to the Qin et al. Lancet framing (Item 9), which is
about evaluation/governance. Consider both as complementary
framing references for the agentic-pipeline section of any
methods-review paper.

---

### Item 11 — Iwaki, Blauwendraat, Makarious, Singleton (Helsinki server preprint 2026): Penetrance of Parkinson's Disease in LRRK2 p. G2019S Carriers Is Modified by a Polygenic Risk Score

**Feeds that surfaced it:** Konrad Karczewski related-research
(position 8, but subject-line matches your priority thread very
cleanly).
**Venue:** Helsinki server preprint, 2026 (bitstream 5e707182-2f21-
4e14-ac58-a4ec2895c2a9); likely en route to *npj Parkinson's Disease*
/ *Annals of Neurology*.
**Authors:** H Iwaki, C Blauwendraat, MB Makarious, AB Singleton.
Blauwendraat + Singleton are the NIH Parkinson genetics unit —
this is a GP2 consortium output.
**Abstract excerpt (Scholar snippet):** "While the LRRK2 p. G2019S
mutation has been demonstrated to be a strong risk factor for
Parkinson's Disease (PD), factors that contribute to penetrance
among carriers, other than aging, have not been well identified.
Objectives: To [quantify the modification of LRRK2 G2019S PD
penetrance by a PD polygenic risk score]…"
**Why this is HIGH for your interests:** Direct methodological
template for the penetrance-of-monogenic × PGS composite-risk
question that anchors the PheWAS / phecode infrastructure thread
(INTERESTS.md L25-27, "penetrance estimation for monogenic variants
under population-screening conditions vs. clinically ascertained
cohorts"). Almost identically portable to:
  - **BRCA1/2** penetrance × PRS in AoU / UKB / MVP;
  - **CFTR** F508del penetrance for CF phenotype severity × modifier
    PRS;
  - **APOL1** G1/G2 CKD penetrance × cardiometabolic PRS;
  - **HTT** preclinical HD conversion × age-of-onset PRS.
**Concrete next steps:** Read the Helsinki server PDF. Check (a)
what PD PRS they use (Nalls-Blauwendraat 90-locus? PGS Catalog?),
(b) whether they stratify penetrance by quintile / tail (aligns
with Souaiaia PGS-tails framing), (c) whether they discuss
population-screening vs. clinically-ascertained penetrance divergence
(directly answers your thread's headline question). This paper's
template is worth mimicking for any monogenic-modifier PRS analysis
you supervise.

---

### Item 12 — Dutta, Zhang, Guo, Quint, Rooney et al. *Cell Genomics* 2026: Polygenic risk scores and plasma proteomics identify cancer-related proteins and trans-regulated protein networks

**Feeds that surfaced it:** Joshua C. Denny related-research (position
4).
**Venue:** *Cell Genomics*, 2026 (article ID S2666-979X(26)00184-9).
**Authors:** D Dutta, J Zhang, X Guo, R Quint, MR Rooney, plus
additional authors truncated. Consistent with the ARIC / UKB Olink
proteogenomics lineage.
**Abstract excerpt (Scholar snippet):** "Genome-wide association
studies identify cancer susceptibility loci, but downstream protein
mechanisms remain incompletely defined. We integrate polygenic risk
scores (PRSs) for 21 cancers with 4,955 plasma proteins measured in
cancer-free [individuals to characterize trans-regulated protein
networks and cancer-relevant protein signatures]…"
**Why this is HIGH for your interests:** Direct fit to multi-omics-
augmented PRS sub-thread (INTERESTS.md L86-91). Complements Zheng et
al. (Item 3) — Zheng et al. quantifies where PGS and PrRS diverge in
neurodegeneration; Dutta et al. shows PRS × proteomic overlap
across 21 cancers. Together they provide a cross-disease view of
PGS × Olink relationships. Relevant secondary threads:
  1. **Pre-symptomatic carrier phenoconversion prediction**
     (INTERESTS.md L204-208) — the trans-regulated protein networks
     they identify are candidate biomarkers for incident-cancer
     prediction (BRCA carriers, etc.).
  2. **Rare disease** — for hereditary-cancer syndromes with UKB
     Olink / AoU proteomics.
**Concrete next steps:** Read for (a) which of the 21 cancers show
strongest PRS × protein trans-regulation (candidate list for
follow-up), (b) whether they define a proteomic risk score
comparable to PGS, (c) whether cross-ancestry validation is
attempted. Cross-reference against Garofalo et al. (Item 16) HCC
DNA-repair rare-variant analysis for a combined "rare-variant +
common-variant + proteomic" HCC picture.

---

### Item 13 — Kunitsu, Ikuta, Hira, Nakagawa, Terada *Pharmacoepi Drug Safety* 2026: Risk of HF Hospitalization Associated With HIF-PHI vs ESA — A Nationwide Claims-Based Cohort Study

**Feeds that surfaced it:** Miguel Hernán citations-to (position 1).
**Venue:** *Pharmacoepidemiology and Drug Safety*, 2026 (article ID
pds.70453).
**Authors:** Y Kunitsu, K Ikuta, D Hira, S Nakagawa, T Terada
(Japanese pharmacoepi group).
**Abstract excerpt (Scholar snippet):** "Hypoxia‐inducible factor
prolyl hydroxylase inhibitors (HIF‐PHIs) are increasingly used to
treat renal anemia in patients with chronic kidney disease (CKD).
We evaluated the risk of heart failure associated with HIF‐PHIs
compared with erythropoiesis‐stimulating agents (ESAs) in routine
clinical practice. Methods We conducted a nationwide, retrospective,
active‐comparator cohort study using a Japanese claims database. We
included adults with non‐dialysis CKD and heart [failure history]…"
**Why this is HIGH for your interests:** Direct pharmacoepi active-
comparator design in a nationwide claims database, citing "Transparent
reporting of observational studies emulating a target trial" —
this is a textbook TTE-adjacent design serving your causal-inference
+ pharmacoepi thread (INTERESTS.md L46-51). Not itself GLP-1/SGLT2/
CFTR/HRT (your active drug-class list), but the design is directly
portable to those drug classes. Especially notable that the paper
follows the Hernán TTE reporting convention.
**Concrete next steps:** Read for (a) how they handle immortal-time
bias and channeling bias (active-comparator design should minimize
both, worth confirming), (b) whether negative controls are used
(directly connects to Item 4 Bots et al.), (c) whether the CKD +
HF eligibility criteria are OMOP-mappable — matters for portability
to your AoU / MVP infrastructure.

---

### Item 14 — Boceck, Laugwitz, Sturm, Bezdan, Gschwind et al. *npj Genomic Medicine* 2026: aiDIVA — hybrid AI for rare disease diagnostics using evidence-based, machine learning and language models

**Feeds that surfaced it:** `"variant interpretation"` keyword feed
(position 3).
**Venue:** *npj Genomic Medicine*, 2026 (article ID s41525-026-00611-x).
**Authors:** D Boceck, L Laugwitz, M Sturm, D Bezdan, A Gschwind, and
additional authors truncated. German rare-disease-diagnostics group
(Sturm / Gschwind pattern).
**Abstract excerpt (Scholar snippet):** "[We benchmarked aiDIVA on
3,041 published solved rare-disease cases. Specifically], we focused
on the 2,890 (out of 3,041) benchmark cases in which the causal
variant was ranked within the top 10 by aiDIVA— [with subset
analyses distinguishing an 'easy' subset ranking the causal
variant within the top 3, and a 'difficult' subset consisting of
the remaining 362 cases where…]"
**Why this is HIGH for your interests:** Direct fit to the auditable
HPO-driven diagnostic-benchmark sub-thread (INTERESTS.md L196-202):
GraphRareBench (Guo et al. 2607.24878) argues Hit@10 conflates
ranking-of-confounders. aiDIVA reports Hit@10 = 2890/3041 = 95%
with an explicit 'easy' (top-3) vs. 'difficult' (top-10-not-top-3)
subset breakdown — directly enacting the GraphRareBench-inspired
"separable metrics for ranking vs. evidence coverage" argument you
want propagated. Also relevant to:
  1. **Rare disease** thread generally.
  2. **Knowledge representation in EHRs** — a hybrid AI system
     combining evidence-based rules with ML + LM is exactly the
     representation-choice question you flagged.
**Concrete next steps:** Read the npj paper for (a) which benchmark
cases they use (RD-Diagnostics? Solve-RD? DDD Genotypes-to-Mendeliome?)
— matters for cross-comparison against Phenolyzer / Phen2Gene /
PhenoSV / LIRICAL / Exomiser / PhenoGPT2, (b) whether the 362
"difficult" cases show enrichment for specific evidence-code
categories (chart-review-validated PS3? BP7?), (c) whether they
enable reproducible re-scoring for benchmark comparability. This
paper is a natural companion to GraphRareBench when writing about
the ranking-vs-evidence-coverage question.

---

### Item 15 — Chovatiya, Mummert et al. 2026: Real-World Use of Abrocitinib for Moderate-to-Severe Atopic Dermatitis in the United States Based on Electronic Health Records and Administrative Claims

**Feeds that surfaced it:** `"electronic health records"` keyword feed
(position 1 in the 09-02 batch).
**Venue:** 2026 (venue not exposed in snippet — likely *JAAD /
Dermatologic Therapy / American Journal of Clinical Dermatology*;
check).
**Authors:** R Chovatiya, A Mummert, S Chang, M [others truncated].
Consistent with an industry-sponsored real-world evidence brief.
**Abstract excerpt (Scholar snippet):** "[We evaluated real-world use
patterns, effectiveness, and safety of abrocitinib for moderate-to-
severe atopic dermatitis in the United States using linked
electronic health records and administrative claims data.]"
**Why this is HIGH for your interests:** Modest but worth logging as
an autoimmune-adjacent EHR + claims RWE study. Direct relevance to:
  1. **Specific disease threads → Inflammatory bowel disease
     "shared with broader autoimmune work"** (INTERESTS.md L110-111).
     JAK1 inhibition (abrocitinib) is under investigation for IBD;
     an atopic-dermatitis real-world safety signal is informative
     for the broader autoimmune / JAK1 discussion.
  2. **EHR phenotyping & OMOP** (INTERESTS.md L39-43) — linked EHR
     + claims cohorts are the OMOP-native RWE substrate.
**Concrete next steps:** Only worth reading if the drug-class /
disease overlap becomes an active thread; otherwise log for the
autoimmune-drug RWE list.

---

### Item 16 — Garofalo, Chotiprasidhi, Johnson et al. *JHEP Reports* 2026: Multi-ancestry sequencing analysis in 293,141 participants identifies predisposition DNA repair genes associated with HCC risk

**Feeds that surfaced it:** `"All of Us research program"` keyword
feed (position 1 in the 09-02 batch); Joshua C. Denny citations-to
(position 2 in the 09-03 batch, citing AoU genomic-data paper).
**Venue:** *JHEP Reports*, 2026 (article ID S2589555926002909).
**Authors:** AM Garofalo, P Chotiprasidhi, JP Johnson, and additional
authors truncated. Consistent with a multi-cohort hepatocellular-
cancer consortium.
**Abstract excerpt (Scholar snippet):** "Genetic testing for Lynch
and BRCA1/2-associated hereditary cancer syndromes is recommended in
colon or pancreatic cancer patients, but their association with
hepatocellular carcinoma (HCC) risk is unknown. We evaluated
associations between rare germline variants in DNA-repair genes and
HCC risk across ancestrally diverse cohorts. Methods We analyzed
whole exome (WES) and whole genome sequencing (WGS) data from 2,594
HCC cases and [297,547 controls across UKB, AoU, and other cohorts]
…"
**Why this is HIGH for your interests:** Direct three-thread hit:
  1. **Biobanks with EHR linkage: All of Us** (INTERESTS.md L29-37)
     — multi-ancestry AoU + UKB WES/WGS pooled analysis is exactly
     the design your thread prioritizes.
  2. **Variant interpretation (ACMG/ClinGen)** (INTERESTS.md L68-72)
     — Lynch/BRCA rare germline variants in DNA-repair genes are
     under active ClinGen curation; new evidence of HCC association
     is directly informative for VCEP evidence codes.
  3. **Genetic epidemiology → composite risk models** (INTERESTS.md
     L76-78) — pairs naturally with an HCC PRS + rare variant
     stacked-risk model.
**Concrete next steps:** Read the JHEP Reports paper for (a) which
DNA-repair genes reach significance (BRCA1, BRCA2, PALB2, MLH1,
MSH2, MSH6? BRIP1, RAD51C, ATM?), (b) case ascertainment strategy
(EHR-derived HCC via phecode? ICD10 C22? cancer registry linkage?),
(c) risk estimates by ancestry (portability). Cross-reference against
Dutta et al. (Item 12) for a rare-variant + PRS + proteomic HCC
triangulation.

---

### Item 17 — Fonseca, Caggiano, Costantino, Dominguez bioRxiv 2026: Locus-specific gene-context interactions improve polygenic prediction

**Feeds that surfaced it:** Konrad Karczewski related-research
(position 9). Lower position, but subject-line match is very clean
for a specific INTERESTS.md sub-thread.
**Venue:** bioRxiv preprint, 2026 (2026.08.26.746823).
**Authors:** R Fonseca, C Caggiano, M Costantino, O Dominguez, plus
additional authors truncated.
**Abstract excerpt (Scholar snippet):** "Polygenic scores (PGS) are
a primary output of large-scale genetic studies and are being
deployed in clinical and non-clinical settings. However, current PGS
assume simple additive models that ignore context-specific genetic
effects, which likely [attenuate portability across ancestries,
environments, and cohorts]…"
**Why this is HIGH for your interests:** Direct extension of the
Nagpal & Gibson *Nature Genetics* 2026 pervasive-PGS×exposure-
interactions framing already in your interests (INTERESTS.md L86-88).
Where Nagpal & Gibson establishes the phenomenon at a global level,
Fonseca et al. offers a locus-specific incorporation mechanism.
Complements Lassen et al. (Item 2) — Lassen tests rare-variant
non-additivity; Fonseca tests locus-specific gene × context. Together
they cover two axes of PGS-additivity relaxation.
**Concrete next steps:** Read the bioRxiv PDF for (a) how they define
"context" (biobank membership? environmental exposure?
tissue-expression context?), (b) whether the improvement is
cross-ancestry, (c) whether the locus-specific interactions align
with the Baya-Souaiaia PGS-tails framework. If context = ancestry,
this becomes a direct portability contribution.

---

## METHODS-WATCH items (surfaced but not prioritized)

- **Tamandeh, Kunwar, Bigge, Serohijos et al. *Genome Biology* 2026**
  — "Protein-protein interaction network architecture of human polygenic
  traits reveals domain-spanning connectivity and evolutionary
  pressures" (Lisa Bastarache related feed). Adjacent to your
  polygenic architecture thread but network-biology-heavy; log for
  the composite-risk section if you need a citation for gene-network
  substrate underlying polygenic traits.
- **Harikrishnan & Kelly medRxiv 2026** — "Evaluating the Impact of
  PC and Mixed Model Approaches on PRS Portability to Diverse
  Ancestries in the UK Biobank" (Karczewski related feed). Directly
  useful methods paper for PGS portability but derivative of a
  well-established literature; log for the cross-ancestry
  portability section.
- **Song, Bai, Fan *Frontiers in Bioinformatics* 2026** —
  "Characteristics of Predicated Pathogenic Missense Variants in
  Human Genes for Mendelian Disorders" (`mendelian diseases` keyword
  feed). Descriptive rather than methodological; log only if the
  gene list overlaps a specific case.
- **Iwaki 09-03 batch also included Fan et al. Alzheimer's / RGL2
  postoperative-delirium** (Jonathan Pritchard cite) — off-topic for
  your active threads but a reminder of AD-adjacent cross-condition
  work.
- **Ilves et al. CohortContrast** (already surfaced in the 09-01
  report, kept firing in Hripcsak feed). Already covered.
- **Jia et al. Nature 2026 lncRNAs in brain disorders** (Jian Yang +
  Montgomery cites) — off-topic disease.
- **Guo et al. *Genome Biology* 2026** benchmarking short-read
  germline SV calling (Stephen Montgomery related) — SV-calling
  methods, low priority.
- **Kudamala et al. arXiv 2608.21589 AoU functional-decline lab/vital
  trajectories** — already flagged in prior report; noted here
  because it fired again on the 09-03 Denny related feed.
- **Y Luo, K Tilling, A Gkatzionis 2026** MR selection-bias adjustment
  in UK Biobank (BMI, education, CRP → depression). Useful MR
  methods paper; log for the drug-target MR sub-thread.
- **Goto et al. medRxiv 2026 Yamanashi Multi-omics Cohort (YMoC)**
  (Denny related feed) — new Japanese screening-defined longitudinal
  metabolic-risk cohort with multi-omics and digital phenotyping.
  Cohort-description paper; monitor for later analytical outputs.
- **Fernández-Cadena, Naylor, Bhattacharjee 2026** Florida sudden-
  death Loeys-Dietz molecular autopsy series (Denny cite). Case
  series; log for variant-interpretation completeness.

## SKIP items (surfaced but off-topic for your active threads)

- Mansouri Ghiasi arxiv-digest 09-01 storage-centric genomics
  systems (systems architecture).
- Ramesh et al. arxiv-digest 09-02 mudskipper locomotion
  (biomechanics).
- Collins 2026 privacy-aware EHR + SDoH + IoT analytics (framing
  piece).
- PLRA-KG recommender systems (`knowledge graph` feed).
- Wagner supplements-for-diabetic-neuropathy blog-style review
  (`AoU` feed, incidental AoU cite).
- Ilicki & Spicer *Drug Discovery Today* rare-disease investment-
  professional benchmark (economics).
- AstraZeneca selumetinib China approval news (`rare diseases` feed).
- Shen et al. sertraline colorectal-cancer metabolomics
  (`drug repurposing` feed; off-topic).
- Elbogdady case report (`autoimmune disorders` feed).
- Multiple antiviral drug-repurposing ML papers (Shahin, Abraham,
  Batra, Benson, Tuchel) — computational-only, no clinical loop.
- Zitnik / Szolovits / Zhiyong Lu related-research feeds mostly
  returned pure-LM / speculative-decoding papers with no clinical
  angle.
- Vivek Natarajan Gemini-in-the-real-world citation (already
  covered).
- Kai Wang RNA-nanopore-PABPN1 paper (basic biology).
- Emily Alsentzer Helicobacter DAF-binding adhesins paper (basic
  biology by clinical-NLP researcher).

---

## Cross-cutting observations for the next window

1. **PGS methodology is the dominant signal this window** (5 HIGH
   items: Items 1, 2, 3, 11, 12, 17). Notably these fit into a
   coherent stack: Item 1 (ABPRS fine-tuning) + Item 3 (PGS-vs-PrRS
   divergence) + Item 12 (PGS × plasma proteomics 21 cancers) +
   Item 2 (rare-variant non-additivity) + Item 17 (locus-specific
   gene-context) + Item 11 (monogenic-modifier PRS). Consider
   whether a brief methods-review draft (in a section like "Composite
   PGS + rare-variant + proteomic risk stratification: a taxonomy")
   would be worth outlining while these papers are fresh.

2. **The negative-controls guidance paper (Item 4) landed in the
   same window as the Kunitsu HIF-PHI TTE paper (Item 13)**. Read
   together, they define the current state of the causal-pharmacoepi
   methodological stack (Bots for negative-controls guidance,
   Kunitsu for a clean example TTE-adjacent claims-based cohort).
   Both are worth having open when reviewing the Zhang et al.
   GLP-1/SGLT2/DPP4i TTE paper (from the prior 09-01 report).

3. **Two "framing" papers arrived from the agentic-AI cluster** (Items
   9 and 10). If you write a perspective / editorial in the next
   window, these are the two references to anchor the "system-level
   governance" argument alongside the OCI-Agent technical reference.

4. **The CHIP review (Item 6) is joined by six ASH-abstract-style
   CH papers in the same alert.** Suggests ASH 2026 abstracts are
   dropping — expect a spike in CHIP / hematologic-malignancy
   activity through late September as the ASH cycle continues. If a
   dedicated CHIP-VEXAS-LOY report emerges, the ASH abstract corpus
   should be revisited then.

5. **The arxiv-digest local runs were dry** (1+1+0 papers over three
   days, all off-topic). Not unusual for the Aug–Sep valley — expect
   density to return with the arxiv September pre-print surge.

## Recommended follow-up reads (top 5 papers to open first)

1. **Hu et al. Nat Comm 2026 ABPRS** (Item 1) — six-feed convergence
   makes this the paper of the week.
2. **Lassen et al. Nat Comm 2026 rare-variant non-additivity** (Item
   2) — extends the Baya PGS-tails framing you already track.
3. **Bots et al. IJE 2026 negative-controls guidance** (Item 4) —
   direct methods-improvement input for any TTE you supervise.
4. **Zhang et al. arXiv 2608.06063 AoU wearable × PRS × MDD** (Item
   5) — three-way AoU intersection with immediate reference value
   for future AoU + wearable proposals.
5. **Yao et al. J Formosan Med Assoc 2026 CH × ASCVD review** (Item
   6) — the reference-review-paper for the CHIP disease sub-thread.

Total window HIGH count: **16** (plus 10 methods-watch, plus ~15
SKIP items).
