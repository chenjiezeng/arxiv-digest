# Research digest report — 2026-09-24

Triage of research-related email (Google Scholar alert feeds) + the local
`arxiv-digest` repo against the active threads in `INTERESTS.md` (PheWAS /
phecodes, EHR-linked biobanks, EHR phenotyping / OMOP, causal inference &
pharmacoepi, variant interpretation, genetic epi, CF / APOL1 / CHIP-VEXAS
/ LOY / IBD disease threads, EHR foundation models, KGs / ontologies,
drug repurposing, rare disease, ML for precision health, multimorbidity,
knowledge representation in EHRs).

Window: **2026-09-21 12:40Z → 2026-09-24 09:00Z** (~3 days since the last
research-digest report, covering three `arxiv-digest` cron runs — 09-21,
09-22, 09-23 — and two Scholar-alert batches: the 09-22 06:46Z / 21:55Z
wave and the 09-24 03:26Z / 08:35Z wave).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-21.md` → `2026-09-23.md`) | 09-21 → 09-23 daily crons | 3 daily runs. 09-21 dry (empty). 09-22 3 papers, top hit `tteICE` R package for intercurrent-event handling in time-to-event trials (Deng et al., causal-inference keyword, score 1). 09-23 3 papers, all Score-1 foundation-model / chip / motor keyword hits — off-thread on disease scope (RootQuantV2 root-trait ViT, GPS L1 spoofing, WILSON Mayo Clinic pathology FM). Today's (09-24) digest has not yet posted at report time; standard 10:30 UTC cron. |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com arxiv-digest newer_than:7d` returned zero threads. Consistent with prior reports: the pipeline commits its output to this repo rather than emailing PR/cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-24 batch, 03:26Z + 08:35Z) | 09-24 | ~40 feeds fired across two waves. HIGH-item authors: **Stephen B Montgomery new-related** (Lassen, Venkatesh, Baya, Lindgren et al. *Nat Commun* — **deviations from genetic additivity driven by rare variants at biobank scale**; Jetzinger et al. *Nat Commun* long-read RNA-seq replicate joining; **Ma et al. long-read RNA-seq for isoform / splicing outlier detection in rare-disease trios** carried from 09-21 batch; Garofalo et al. **JHEP Reports HCC-risk DNA-repair genes in 293k participants**). **Jian Yang new-related** (Zheng, Shivakumar, Shen, Kim medRxiv — **absorption and co-expression modules show where polygenic and proteomic risk scores diverge in neurodegenerative diseases**; Fonseca, Caggiano et al. bioRxiv — **locus-specific gene-context interactions improve polygenic prediction**; Nam et al. medRxiv **novel T1D PGS in diverse populations**; Park & Chung *Sci Rep* comparative PRS learners in UKB). **George Hripcsak new-related** (Fu, Lu, Ahn et al. *Nat Commun* — **MedError: machine-assisted framework for systematic error analysis in clinical concept extraction**). **George Hripcsak citations-to** (**Chen 2026 dissertation "Genomic Medicine Translation: Evidence Generation for Genomic Risk Assessment, Clinical Implementation, and a New Tool for Variant Interpretation"** — also fires on Bastarache citations-to and `mendelian diseases` keyword; likely Vanderbilt / eMERGE-lineage translational-genomics thesis). **Joshua C. Denny new-related** (Park et al. *Transl Psychiatry* cross-ancestry OCD PRS transferability — carried from prior window). **Chenjie Zeng new-related** (**Kloots et al. *Eur J Cancer* — tumour-first DNA testing as a gateway to germline screening in metastatic prostate cancer**; Tillman et al. *Pediatric Pulmonology* — CFTR-modulator fluid-associated weight gain case series; Turcan et al. medRxiv — conditional polygenic enrichment for causal cell-population identification). **Lisa Bastarache citations-to** (Chen 2026 dissertation, same). **Lisa Bastarache new-related** (Hu et al. *PLoS Genet* shared polygenic risk across cancers). **Konrad Karczewski citations-to** (Brar & Lee *Hepatology Communications* MetALD global burden — off-thread). **Konrad Karczewski new-related** (Hakizimana et al. Rwandan-children autism-trio exome — off-thread). **Tiffany J Callahan new-related** (Setlur et al. arXiv geometric annotations for pLM features — off-thread). **Marinka Zitnik new-related** (Xu et al. arXiv temporal self-distillation dLLMs — off-thread). **Miguel Hernán citations-to** (Lim 2026 dissertation orthogonal statistical learning; small batch). **Bryan Traynor** feeds: rapamycin ALS multivariate survival (De Nardi et al.). Keyword feeds: `"variant interpretation"` (Musliner et al. Eur Neuropsychopharmacol clinical psychiatric genomics in Europe; **Zimmermann & Urrutia Nat Genet 2026 — interpreting human genetic variation at atomic resolution**); `"All of Us research program"` (Rietkerk et al. Eur Neuropsychopharmacol — **postnatal depression polygenic profiles in CONVERGE + AoU**; **Yang, Zhang, Fischman, Cuchel, Susztak et al. AJKD — drug-target MR study of ANGPTL3/4 and target lipases in CKD, using AoU CDR v8 + PMBB**); `"phenome wide association studies"` (Garimella et al. AJKD — carbamylation × coronary-artery calcification PheWAS in CRIC; Sylvanus et al. Eur Neuropsychopharmacol — shared and subtype-specific neuropsychiatric + proteomic architecture of primary headache disorders in >1.6M individuals, PheWAS in Penn Medicine Biobank). |
| Google Scholar alerts (09-22 batch, 06:46Z + 21:55Z) | 09-22 | ~40 feeds. **Miguel Hernán citations-to**: **Hellemans, Chesnaye, Kramer, Fu, Arnol et al. BMJ — survival benefit of deceased-donor kidney transplantation vs. continued dialysis: international TTE across five European countries**; Abedi et al. JAMA Netw Open — single- vs. multiple-dose antibiotic prophylaxis for total hip arthroplasty (TTE). Also Wen *Int J Biostat* doubly robust monotonic survival curves for time-varying treatments; Lu et al. RSV vaccine effectiveness JAMA Netw Open. **"All of Us research program"**: Huang 2026 dissertation on metabolic/neurocognitive determinants of musculoskeletal health in AoU (Registered Tier). **`electronic health records`**: Wang et al. *Risk* Deep learning for ICU-adverse-event prediction from EHRs (methodological review). **Foundation models + EHR**: Mehandiratta & Anubhuti human digital twins state-of-the-art review. **Chenjie Zeng new-related, Joshua C. Denny citations-to, Lisa Bastarache citations-to, Yuan Luo citations-to**: Sanchez et al. *Lancet Gastroenterology & Hepatology* — genetic variants and renal impairment in decompensated cirrhosis: multi-ancestry GWAS (5 feeds fired). |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against the research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced in this short window, clustering into five knots:

**PGS × context / non-additivity knot (3 items, top of list).**
**Lassen, Venkatesh, Baya, Lindgren et al. *Nature Communications* 2026** —
**"Deviations from genetic additivity driven by rare variants at biobank
scale"**. Direct methodological extension of the Baya *AJHG* 2026
misaligned-individuals framing that the previous report tracked;
Baya is second-author here, and this paper appears to be the biobank-scale
formal test paper behind the same lab's PGS-residual / non-additivity
lineage. **Fonseca, Caggiano, Costantino, Dominguez et al. bioRxiv 2026** —
**"Locus-specific gene-context interactions improve polygenic prediction"**
(Jian Yang new-related feed). Explicit deployment of GxE / gene-context
interactions at the locus level to lift PGS accuracy; direct hit for the
`GxE and PGS × exposure / environment interactions` sub-thread that
`INTERESTS.md` calls out around Nagpal & Gibson *Nature Genetics* 2026.
**Zheng, Shivakumar, Shen, Kim medRxiv 2026** — **"Absorption and
Co-expression Modules Show Where Polygenic and Proteomic Risk Scores
Diverge in Neurodegenerative Diseases"**. Directly on-thread for the
`Multi-omics-augmented PRS` sub-thread — quantifies where PGS and
proteomic RS diverge as an information-content question, using
co-expression modules as the diagnostic instrument. Together the three
papers extend the "tails-and-residuals" taxonomy of PGS from the 09-21
report (Baya *AJHG*, Souaiaia *Nature*, Vazquez *Genetics*, Ward *medRxiv*)
with a **non-additivity + GxE + multi-omics** trio.

**Causal inference / pharmacoepi (2 items).**
**Hellemans, Chesnaye, Kramer, Fu, Arnol et al. *BMJ* 2026** — international
**target trial emulation** of deceased-donor kidney transplantation vs.
continued dialysis across five European country registries, stratified by
patient characteristics (age, diabetes, CVD), donor quality (SCD/ECD), and
donor retrieval (DBD/DCD). Hernán-lineage TTE flagship of the 09-22
citations-to batch; pair with Turchin *BMJ* 2026 SGLT-2 vs. GLP-1 renal
TTE from the prior report as the same-registry-family "read TTEs in
pairs" cluster. **Yang, Zhang, Fischman, Cuchel, Susztak et al. *American
Journal of Kidney Diseases* 2026** — **Drug-target Mendelian randomisation
study of ANGPTL3, ANGPTL4, and their target lipases in CKD**, using **All
of Us Controlled Tier CDR v8 + PMBB** individual-level data. Direct match
for the `Drug-target Mendelian randomisation triangulated with
observational cohort estimates` sub-thread (Saxby et al. metformin × AAA
lineage) — this is the AoU-scale instantiation for a specific
drug-target-lipid-CKD triangulation.

**EHR foundation-model & knowledge-representation audit (2 items).**
**Fu, Lu, Ahn, Chen, Yin, Wen, Yue et al. *Nature Communications* 2026** —
**MedError: a machine-assisted framework for systematic error analysis in
clinical concept extraction** (Hripcsak new-related feed). Directly serves
`Knowledge representation in EHRs → Fidelity, portability, and audit of
representations` and pairs with the Fu et al. *npj Health Systems* 2026
multi-site geriatric-care benchmark from the prior report — same
first-author lineage, the pair now covers *both* systematic-error
attribution *and* multi-site benchmarking, which is the full audit stack
for clinical-NLP-extracted representations. **Chen 2026 (Vanderbilt-lineage
dissertation, published on the Vanderbilt Electronic Theses and
Dissertations server)** — *Genomic Medicine Translation: Evidence
Generation for Genomic Risk Assessment, Clinical Implementation, and a New
Tool for Variant Interpretation*. Fires on three separate Scholar feeds
(Bastarache citations-to, Hripcsak citations-to, `mendelian diseases`
keyword) which is a strong salience signal. Consolidates PGS + rare
variant + implementation science + variant-interpretation tooling under
one framework; likely a citation-frame source for the genomic-medicine
translation-pathway thread.

**Variant interpretation flagship (1 item).**
**Zimmermann & Urrutia *Nature Genetics* 2026** — **"Interpreting human
genetic variation at atomic resolution"**. Perspective / synthesis piece
that reframes ACMG-AMP variant interpretation with mechanistic
(atomic-resolution) evidence layers. Directly on-thread for `Variant
interpretation → ACMG-AMP variant classification` and pairs with the
Boßelmann & May *Hum Mol Genet* 2026 mutation-rate-transfer paper from
the prior report as complementary "add a new evidence layer to variant
interpretation" moves.

**PheWAS / biobank-linked application (4 items).**
**Rietkerk, Lancaster, Singh, Lapato, Barr et al. *European
Neuropsychopharmacology* 2026** (WCPG-abstract format) — **dissecting the
shared and distinct polygenic profiles of postnatal depression and
reproductive-related traits in the CONVERGE study + All of Us Research
Program**. Explicit AoU replication — direct hit for `Biobanks with EHR
linkage → All of Us`. **Sylvanus, Davis, Khan, Gunawan, Shi et al. *European
Neuropsychopharmacology* 2026** — **"Shared and Subtype-Specific
Neuropsychiatric and Proteomic Architecture of Primary Headache
Disorders in Greater than 1.6 Million Individuals"** — uses LD-score
regression for genetic correlations + PheWAS in Penn Medicine Biobank +
multi-omic integration. On-thread for `PheWAS / phecode infrastructure`
and `Multi-omics-augmented PRS`. **Kloots, Kets, Schuurs-Hoeijmakers,
Kroeze et al. *European Journal of Cancer* 2026** — **"Tumour-first DNA
testing as a gateway to germline screening in patients with metastatic
prostate cancer"** (Chenjie Zeng new-related feed). On-thread for the
`Genetic epidemiology → hereditary cancer` overlap and directly relevant
to the account owner's own prior work on germline predisposition in
prostate cancer. **Tillman, Lazutina, Robinson, Colwell et al. *Pediatric
Pulmonology* 2026** — **case series of sustained fluid-associated weight
gain following CFTR modulator therapy** (Chenjie Zeng new-related feed).
Small-N adverse-event signal in the CFTR-modulator pharmacoepi lineage;
pairs with the Merino et al. *Annals ATS* 2026 mental-health
pharmacovigilance paper from the prior report as complementary
"modulator-era chronic adverse event surveillance" moves.

---

## HIGH — Detailed reports

### 1. Lassen, Venkatesh, Baya, Lindgren et al. — Deviations from genetic additivity driven by rare variants at biobank scale
- **Venue:** *Nature Communications* 2026, article 76151.
- **Threads served:** `Genetic epidemiology → PGS residuals / polygenic-deviation designs`; `Composite risk models stacking PRS with rare pathogenic variants`; `Variant interpretation`.
- **Why it matters:** Additive genetic models are the default in GWAS, but deviations from additivity carry mechanism-of-action and therapeutic-response information that standard PGS lose. This paper introduces a biobank-scale non-additivity test and identifies **rare-variant-driven** deviations as the dominant source of the signal. Directly extends the Baya *AJHG* 2026 misaligned-individuals framing (Baya is second author here, same lab lineage) with a formal test. Read paired with the **Fonseca et al. bioRxiv 2026 locus-specific gene-context interactions** paper (item 3) — Lassen quantifies the *rare-variant* source of non-additivity; Fonseca quantifies the *gene-context* source. Together they say "the additive PGS is missing two identifiable, complementary axes of information."
- **Read-order priority:** Read first. This is the Nature Communications flagship of the window and the direct methodological reference for the `Tails-and-residuals` taxonomy.

### 2. Hellemans, Chesnaye, Kramer, Fu, Arnol et al. — Survival benefit of deceased-donor kidney transplantation versus continued dialysis: international target trial emulation
- **Venue:** *BMJ* 2026, article bmj-2026-100624 (Hernán citations-to feed).
- **Threads served:** `Causal inference and pharmacoepidemiology → target trial emulation`; `EHR-linked biobanks / registries` (European Renal Association Registry from Catalonia, Denmark, France, and two other countries or regions).
- **Why it matters:** International multi-country registry-based TTE of a **hard clinical decision** (transplant vs. continued dialysis) stratified by patient characteristics (age, diabetes, CVD), donor quality (standard-criteria vs. expanded-criteria donor), and donor retrieval type (donation after brain death vs. donation after circulatory death). The stratified-by-donor-quality axis is the useful piece — it is the effect-modifier structure that pushes TTE beyond a single average treatment effect into an actionable per-patient risk-benefit calculation. Pair with the previous report's **Turchin *BMJ* 2026 SGLT-2 vs. GLP-1 renal TTE** as the "read TTEs in pairs" cluster: both stratify by a baseline modifier (albuminuria there, donor quality here) rather than treating it as a subgroup analysis.
- **Read-order priority:** Read second, right after Turchin. The pair is the current benchmark for European-registry-TTE reporting conventions.

### 3. Fonseca, Caggiano, Costantino, Dominguez et al. — Locus-specific gene-context interactions improve polygenic prediction
- **Venue:** bioRxiv 2026-08-28 (Jian Yang new-related feed).
- **Threads served:** `Genetic epidemiology → GxE and PGS × exposure / environment interactions`; `Composite risk models`.
- **Why it matters:** Current PGS assume simple additive models that ignore context-specific genetic effects. This paper adds **locus-specific gene-context interactions** to the PGS objective and shows an accuracy lift. Direct fit under the Nagpal & Gibson *Nature Genetics* 2026 pervasive-PGS×exposure sub-thread. **Pair explicitly with Lassen et al. (item 1)**: Lassen says rare variants drive one class of non-additivity; Fonseca says locus-specific GxE drives another. Together they define two orthogonal PGS-augmentation levers.
- **Read-order priority:** Read paired with Lassen.

### 4. Zheng, Shivakumar, Shen, Kim — Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases
- **Venue:** medRxiv 2026-08-24 (Jian Yang new-related feed).
- **Threads served:** `Genetic epidemiology → Multi-omics-augmented PRS`; `Machine learning for precision health`.
- **Why it matters:** Polygenic and proteomic risk scores are both proposed for pre-symptomatic stratification, but the extent of information overlap versus complementarity has not been quantified across neurodegenerative disease. This paper measures the divergence directly using **co-expression modules** as the diagnostic. Direct application for the `pre-symptomatic carrier phenoconversion prediction from longitudinal biomarker trajectories` sub-thread `INTERESTS.md` prioritizes (Ran / Benatar ALS lineage). Positions as the multi-omics-augmented-PRS answer to "which score to run first, and when the two disagree, what does that mean?"
- **Read-order priority:** Read for portability — the "where do the two scores diverge" framing is directly reusable for BRCA / APOL1 / HTT preclinical carrier stratification.

### 5. Fu, Lu, Ahn, Chen, Yin, Wen, Yue et al. — MedError: A machine-assisted framework for systematic error analysis in clinical concept extraction
- **Venue:** *Nature Communications* 2026, article 77067 (Hripcsak new-related feed).
- **Threads served:** `Knowledge representation in EHRs → Fidelity, portability, and audit of representations`; `EHR foundation models → Pretraining-contamination audits`; `EHR phenotyping & OMOP → NLP-derived representations`.
- **Why it matters:** No standardized framework has existed for systematic error analysis of clinical-NLP concept-extraction models. MedError provides one. Directly serves the "audits of learned representations against clinical ground truth" call-out in `INTERESTS.md`. **Pair with the Fu et al. *npj Health Systems* 2026 multi-site benchmarking framework from the prior report** — same first-author lineage; the pair now covers error attribution *and* multi-site portability, which together are the full audit stack for clinical-NLP-extracted representations. Read as *the* Fu-lineage 2026 diptych for representation audit.

### 6. Chen — Genomic Medicine Translation: Evidence Generation for Genomic Risk Assessment, Clinical Implementation, and a New Tool for Variant Interpretation
- **Venue:** 2026 dissertation (fires on Bastarache citations-to, Hripcsak citations-to, and `mendelian diseases` keyword feeds).
- **Threads served:** `Variant interpretation → ACMG-AMP variant classification`; `Genetic epidemiology → PRS deployment`; `Knowledge representation in EHRs → Applications to prioritize`.
- **Why it matters:** A dissertation that connects PGS + rare-variant risk + implementation + a new variant-interpretation tool. The fact that it fires on both the Bastarache and Hripcsak citations-to feeds *and* the `mendelian diseases` keyword suggests a broad citation footprint, plausibly a Vanderbilt / eMERGE-lineage translational-genomics thesis. Value: uses `common diseases along with monogenic conditions` framing (snippet), which is the composite-risk framing `INTERESTS.md` calls out. Worth reading the abstract and Chapter 1 for the citation-frame paragraph.
- **Read-order priority:** Read the abstract first and skim the variant-interpretation-tool chapter if the abstract lands.

### 7. Zimmermann & Urrutia — Interpreting human genetic variation at atomic resolution
- **Venue:** *Nature Genetics* 2026 (`"variant interpretation"` keyword feed).
- **Threads served:** `Variant interpretation → ACMG-AMP variant classification`.
- **Why it matters:** Perspective / synthesis piece reframing variant interpretation with **mechanistic depth (atomic resolution)** as an added evidence layer. From the snippet, it appears to argue that current variant-interpretation frameworks are missing mechanistic-structure evidence and lays out a roadmap. Pair with **Boßelmann & May *Hum Mol Genet* 2026 mutation-rate transfer** (prior report) as complementary "extend variant interpretation with a new evidence layer" moves — mutation-rate on one side, atomic-resolution mechanism on the other. Directly relevant to the `Variant interpretation` thread.

### 8. Yang, Zhang, Fischman, Cuchel, Susztak et al. — The Role of Angiopoietin-Like Proteins 3 and 4 and Their Target Lipases in CKD: A Drug-Target Mendelian Randomization Study
- **Venue:** *American Journal of Kidney Diseases* 2026, article S0272-6386(26)01121-2 (`"All of Us research program"` keyword feed).
- **Threads served:** `Genetic epidemiology → drug-target Mendelian randomisation`; `Biobanks with EHR linkage → All of Us + Penn Medicine Biobank`; `Causal inference and pharmacoepidemiology`.
- **Why it matters:** Individual-level analysis using **AoU Controlled Tier CDR v8 + PMBB** to run **drug-target MR** on ANGPTL3 / ANGPTL4 and their target lipases as CKD-modifier candidates. Direct hit for the `Drug-target Mendelian randomisation triangulated with observational cohort estimates` sub-thread `INTERESTS.md` calls out around Saxby et al. metformin × AAA. Also serves the AoU biobank use thread. This is the AoU-scale template a similar CFTR / GLP-1R / SGLT2 drug-target-MR + AoU observational triangulation could follow.
- **Read-order priority:** Read as a methods-lift for future CFTR / drug-target-MR × AoU work.

### 9. Rietkerk, Lancaster, Singh, Lapato, Barr et al. — Dissecting the shared and distinct polygenic profiles of postnatal depression and reproductive-related traits in the CONVERGE study of major depression and the All of Us Research Program
- **Venue:** *European Neuropsychopharmacology* 2026 (WCPG abstract; `"All of Us research program"` keyword feed).
- **Threads served:** `Biobanks with EHR linkage → All of Us`; `Genetic epidemiology → PRS deployment, cross-cohort replication`.
- **Why it matters:** Cross-cohort replication of postnatal-depression polygenic profiles across CONVERGE and AoU. Explicit AoU deployment — direct fit under `Biobanks with EHR linkage → All of Us`. WCPG abstract format so the paper is short; the useful piece is the cross-cohort design as a template for cross-biobank PGS replication (CONVERGE + AoU is a Chinese-ancestry + diverse-ancestry pair that is nontrivially informative for cross-ancestry portability, even at abstract level).

### 10. Sylvanus, Davis, Khan, Gunawan, Shi et al. — Shared and Subtype-Specific Neuropsychiatric and Proteomic Architecture of Primary Headache Disorders in Greater than 1.6 Million Individuals
- **Venue:** *European Neuropsychopharmacology* 2026, WCPG abstract 85 (`"phenome wide association studies"` keyword feed).
- **Threads served:** `PheWAS / phecode infrastructure`; `Genetic epidemiology → Multi-omics-augmented PRS`; `Biobanks with EHR linkage → Penn Medicine Biobank`.
- **Why it matters:** Uses **LD-score regression for genetic correlations, PheWAS in Penn Medicine Biobank for clinical pleiotropy, and multi-omic integration** on a >1.6M-individual cohort for primary-headache-disorder subtyping. Direct match for the `PheWAS / phecode infrastructure` thread and for the `Chronic disease clustering and multimorbidity` thread's cardiometabolic + neuropsychiatric sub-focus. WCPG abstract, so read as a signal of a follow-on manuscript.

### 11. Kloots, Kets, Schuurs-Hoeijmakers, Kroeze et al. — Tumour-first DNA testing as a gateway to germline screening in patients with metastatic prostate cancer
- **Venue:** *European Journal of Cancer* 2026 (Chenjie Zeng new-related feed).
- **Threads served:** `Genetic epidemiology → hereditary cancer / germline predisposition genes`.
- **Why it matters:** Integrated tumour + germline testing is recommended for all metastatic prostate cancer patients, but real-world implementation varies widely. This paper evaluates a **tumour-first workflow** as a stratifier for germline testing. Directly relevant to the account owner's own prior work on germline predisposition variants in prostate cancer and to the `hereditary-cancer × germline-testing implementation` angle. Read as a real-world-implementation reference (workflow design, not discovery).

### 12. Tillman, Lazutina, Robinson, Colwell et al. — Case Series of Sustained Fluid-Associated Weight Gain Following CFTR Modulator Therapy
- **Venue:** *Pediatric Pulmonology* 2026 (PMC13507763; Chenjie Zeng new-related feed).
- **Threads served:** `Specific disease threads → Cystic fibrosis / CFTR`; `Causal inference and pharmacoepidemiology → CFTR modulator pharmacoepi, real-world outcomes`.
- **Why it matters:** Small-N case series but a **new adverse-event signal** (sustained fluid-associated weight gain) in the CFTR-modulator pharmacoepi literature. Pairs with the **Merino et al. *Annals ATS* 2026 mental-health-safety pharmacovigilance paper** from the prior report as complementary "chronic modulator-era adverse-event surveillance" moves. On-thread for the account owner's own AoU CFTR-modulator work (poster 646, NACFC 2026) — fluid retention is a candidate covariate to check in longitudinal AoU EHR-derived weight trajectories under modulator exposure.

---

## METHODS-WATCH

- **Deng, Zhou, Wang, Han — `tteICE` R package, arXiv 2609.23473** (local `arxiv-digest` 2026-09-22, score 1): implements the five ICH E9(R1) strategies for handling intercurrent events in time-to-event outcomes in two-arm trials, with nonparametric and semiparametric-efficient estimators, competing-risks / semi-competing-risks support, Shiny front-end. Off-thread on disease but a direct-hit methods reference for the CFTR-modulator persistence / discontinuation analyses (persistence-discontinuation *is* an intercurrent event under ICH E9(R1)).
- **Turcan, Hou, Lin, Pfenning, Sakaue et al. medRxiv 2026** — "Conditional polygenic enrichment distinguishes causal from tagging disease-critical cell populations in single-cell RNA-seq" (Chenjie Zeng new-related feed). Methodological refinement for integrating GWAS with scRNA-seq to identify *causal* rather than *tagging* cell populations — portable to any GWAS × sc integration attempt.
- **Ma, Weisburd, DiTroia, Romo, Covill et al.** long-read RNA-seq for isoform / splicing outlier detection in rare-disease trios (Montgomery feed, carried from 09-21 batch; also appears again in 09-24 pull) — the rare-disease reanalysis lever.
- **Jetzinger, Paniagua, Cormack, Mestre-Tomás et al. *Nat Commun* 2026** — handling biological replicates in long-read RNA-seq by joining or not joining (Montgomery feed). Methodological hygiene for long-read RNA-seq workflows that touch rare-disease trios.
- **Nam, Kreienkamp, Li, Mandla, Tran et al. medRxiv 2026** — novel T1D polygenic scores improve identification in diverse populations (Jian Yang new-related feed). Cross-ancestry PGS-portability paper for T1D specifically. On-thread for `Genetic epidemiology → PRS, cross-ancestry portability`.
- **Peng, Butler-Laporte, Johnson, Engelman et al. Alzheimer's & Dementia** — genetic evidence for a protective role of immunoglobulin M in Alzheimer's disease, using AoU + UKB (Jian Yang new-related feed). AoU deployment for AD-protective drug-target-MR-adjacent analysis.
- **Zimmermann & Urrutia** already in HIGH — but also serves as a methods-watch reference for how atomic-resolution mechanistic evidence gets folded into ACMG frameworks.
- **Wang, Yan, Chen, Tan, Chen, Lu, Duan et al. *Risk*** 2026 — deep-learning ICU-adverse-event prediction from EHRs: methodological review (Pascal Brandt new-related feed; posted both 09-22 and 09-24). Framing reference for `Machine learning for precision health → prognostic modeling` — off-thread day-to-day but useful as a citation-frame paper for ICU-EHR-FM claims.
- **Mehandiratta & Anubhuti** — Human Digital Twins for Precision Healthcare state-of-the-art review (`Foundation models and "electronic health records"` keyword feed, 09-22). On-thread as a **companion reference to the Zhang / Ideker / Oermann *Cell* 2026 digital-twins consortium paper** in `INTERESTS.md`; useful as a survey citation.
- **Sanchez et al. *Lancet Gastroenterology & Hepatology* 2026** — multi-ancestry GWAS of renal impairment in decompensated cirrhosis. Fired on five feeds (Denny citations-to, Yang citations-to, Bastarache new-related, Chenjie Zeng new-related, Pascal Brandt new-related) — legitimate visibility signal, but disease scope is off-thread day-to-day. Notable as a cirrhosis-genetics multi-ancestry contribution.
- **Musliner, Vassos, Breen *European Neuropsychopharmacology*** 2026 — "Clinical Application of Psychiatric Genomics in Europe — Not Later, Now" (WCPG plenary abstract, `variant interpretation` keyword feed). Not a methods paper — a policy / clinical-genomics deployment position piece. Useful as a citation-frame paragraph for "why psychiatric genomics is being deployed clinically now" in the psychiatric-genomics translation direction.
- **Alfasly et al. arXiv 2609.25123 — WILSON pathology foundation model** (local `arxiv-digest` 2026-09-23, score 1). Mayo Clinic 189k slides across 42 organs + 829 diagnostic entities, using pathology reports as supervision. Off-thread on disease scope but the whole-slide-composite-image trick and 272-to-2155-fold compute reduction relative to slide-level models are methodologically interesting for cross-modal foundation-model design. Also a Mayo-Clinic FM entry, which is a datapoint on the "small-shop-but-high-quality-data FMs" question.

## SKIP

- 2026-09-21 empty arxiv-digest (nothing to skip).
- 2026-09-22 arxiv-digest: PACE tabular-FM feature screening (off-thread; not EHR); Charpentier & Barry portfolio demutualization (insurance actuarial, off-thread).
- 2026-09-23 arxiv-digest: RootQuantV2 (root traits, agricultural — off-thread); Ahmad et al. GPS L1 spoofing for autonomous vehicles (off-thread despite `chip` keyword hit).
- Miscellaneous off-thread Scholar hits: gut-skin axis atopic dermatitis / IBD review (Journal of Personalized Medicine); Managing-Fit-at-Work SGM disability sociology; economic-stress birth-sex-ratios Finland (Karczewski feed); Environmental Ethics in Endoscopy (Hernán feed); RSV vaccine effectiveness JAMA Netw Open (Hernán feed, off-thread; MSM covariate paper); Wang et al. active-commuting × biological-aging UKB (Karczewski citations-to, off-thread); Huang 2026 dissertation on musculoskeletal health in AoU (on-thread on cohort but not on outcome family); rapamycin-ALS multivariate survival (Traynor feed, off-thread); Rwandan-ASD trio exome (Karczewski feed, off-thread); Somali AI education (unrelated); "Environmental Ethics in Endoscopy" (unrelated); Zhang & Hu donanemab Alzheimer's meta-analysis (Hernán feed, off-thread meta); Multi-Locus Molecular Diagnoses Taiwanese IEM (variant-interpretation keyword, off-thread disease).

---

## Bookkeeping

- **Report path:** `reports/2026-09-24-research-digest.md`.
- **Local arxiv-digest coverage this window:** `digests/2026-09-21.md` (empty), `digests/2026-09-22.md` (3 papers, all Score 1), `digests/2026-09-23.md` (3 papers, all Score 1). Today's cron has not yet posted at report time.
- **`seen.json` size at report time:** ~178 unique arXiv IDs since the pipeline was seeded (net +3 from 2026-09-21 report's 175). No pruning needed.
- **Next report cadence:** default ~2–3 weeks. The next research-digest report is due 2026-10-08 to -10-15 unless a large batch (Nature Medicine drop, NACFC late-breaker publication, or a set of arXiv papers scoring ≥3) forces an earlier cut. Alternatively, if the Lassen / Fonseca / Zheng PGS-non-additivity trio triggers a follow-up manuscript from any of the tracked labs before then, that publication event is a natural cut trigger.
- **Interest-file drift check:** no `INTERESTS.md` edits are needed based on this window's mix. The sub-threads that fired hardest this window were `PGS residuals / polygenic-deviation designs + GxE + Multi-omics-augmented PRS` (items 1, 3, 4), `Causal inference & pharmacoepi → TTE + drug-target MR` (items 2, 8), `Knowledge representation in EHRs → representation audit` (item 5), `Variant interpretation` (items 6, 7), and CFTR modulator pharmacoepi (item 12). All are currently well-anchored in the interests file. The Lassen + Fonseca + Zheng cluster is a natural expansion of the "tails-and-residuals" PGS taxonomy `INTERESTS.md` already calls out — the current wording covers them without edit.
