# Research digest report — 2026-06-16

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/VEXAS/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-06-13 → 2026-06-16** (since the prior 2026-06-13 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-15 → 06-16 | Two batches: 06-15 00:34Z and 03:27Z (~7 threads), and the large 06-16 07:23Z batch (~38 threads). The 06-16 batch was sweeping — most tracked author feeds (Bastarache, Karczewski, Denny, Hripcsak, Yang, Chute, Pritchard, Kastner, Montgomery, Rehm, Zitnik, Shah, Szolovits, Luo, Brandt, Natarajan, Gharavi, Hernán, Vogelstein, Shendure, Zhao, Celi, Ryan) fired on the same delivery wave. |
| `arxiv-digest` repo (`digests/`) | 2026-06-13 → 06-16 | **3 daily files; 0 non-empty.** 06-13 = 0 (2 previously surfaced, suppressed); 06-14 = 0 (1 previously surfaced, suppressed); 06-15 = 0. Net signal from the arXiv pipeline this window: **zero new papers**. |
| NCBI "My NCBI What's New" (AoU, UK Biobank, drug repurposing) | 06-12, 06-13 | Aggregate PubMed digests; pre-window edge case, not individually triaged here. |
| Direct journal/preprint alerts (Nature, Cell, Lancet, etc.) | none in window | The 4-day Gmail search returned no items from these senders independent of Scholar — the journals are reaching you via Scholar's author/keyword feeds rather than direct subscription. |

> ⚠️ **`arxiv-digest` was completely silent for the window** — three days, three zero-paper digests. 06-13 and 06-14 each had previously-surfaced items suppressed by `seen.json` dedup, so the fetch pipeline is technically alive; q-bio/stat.AP simply produced nothing scoring ≥2 on the current keyword set in a 30 h window. The pattern from the prior two reports (Scholar alerts carrying 80%+ of on-thread signal, arXiv supplying methods-grade picks at single-digit/week rate) is intensifying — this window is **100% Scholar-sourced**. The cs.LG/stat.ME/medRxiv expansion recommended in the prior three reports is now overdue.

> Caveat: Scholar alert emails contain title, authors, venue, and the first ~2-3 lines of each abstract only. The reports below contextualize that metadata against your research threads; nothing here reflects full-text reading.

---

## Executive summary

- **Penetrance-in-population-screening hits the strongest signal again.** Gold et al. (medRxiv, surfaced by Karczewski + Bastarache feeds) tackle long-term penetrance of *genomic-newborn-screening-prioritized* P/LP variants using adult biobanks — the **exact** population-vs-clinical penetrance gap your INTERESTS file foregrounds. This is the second consecutive window with a top-tier penetrance paper landing in your self-adjacent feed (Ramchand AIRE last window, Gold gNBS panel this window).
- **A self-citation event you should know about.** Kang et al.'s "Harness All of Us for Equitable Disease Risk Prediction" tutorial (Statistics in Biosciences) cites your **"Comparison of phenomic profiles in the All of Us Research…"** paper — it appears in both the Lisa Bastarache citation feed and your own *Chenjie Zeng — 1 new citation* feed. AoU + PRS + rheumatoid arthritis + equity tutorial = direct hit on three threads.
- **EHR phenotyping × LLM benchmarking has its first head-to-head.** Molina et al. (Annals of Emergency Medicine) is *Computable Structured Phenotype vs LLM* for opioid use disorder identification, with expert physician review as gold standard. Surfaced **twice** (Hripcsak + Pascal Brandt feeds). This is the kind of comparative-evaluation paper that anchors a methods section when you justify rules-vs-LLM choices in AoU phenotype work.
- **Two new ACMG "Points to Consider" statements landed in the same wave.** Mighton et al. on VUS reporting (Rehm feed) and Guha et al. on repeat expansion detection by NGS (Montgomery feed). Both are formal community guidance — they become default citations for the next 2–3 years on variant interpretation methods.
- **IBD × proteomic PRS surfaces a tractable mechanism-stratified phenotype.** Turchin et al. (medRxiv, Denny feed) build a *proteomic* polygenic score targeting IL-18-driven IBD — i.e., an etiologic-subtype PRS rather than a generic IBD risk score. Pairs with Hukerikar et al. (Science Advances, also Denny feed) on the immunoproteome × multimorbidity MR study — together they form a *proteome → subtype → multimorbidity* triangulation.
- **APOL1 disease thread continues.** Zahr et al. (Pediatric Nephrology, APOL1 keyword feed) report from the Biorepository and Integrative Genomics Initiative on APOL1 in pediatric CKD — pairs with the Varner et al. APOL1 pediatric review and the Pell APOL1/TCR transplant-rejection paper from last window.
- **VEXAS gets an MDS-specific review.** Patel et al. (Blood Advances, Kastner feed) on myelodysplastic syndromes in VEXAS — direct hit on the VEXAS/clonal-hematoinflammatory thread.
- **EHR foundation-model lineage adds two items.** Johnson et al. (npj Digital Medicine, Zitnik feed) on clinical-code embeddings for knowledge-grounded AI in medicine, and Huang et al. (Brandt + Hripcsak feeds) on robust spectral embedding with knowledge transfer for EHR.
- **Drug repurposing**: still thin. No on-thread items this window. The pattern (KG/GNN-explainability angle absent; EHR-mining repurposing absent) persists across 3 windows.
- **`arxiv-digest` contributions**: none. Zero papers across 3 days.

Counts: **13 HIGH**, **5 METHODS-WATCH**, rest SKIP/off-thread.

---

## HIGH priority — detailed reports

### 1. Long-term Penetrance of Disease Variants in Genes Prioritized for Genomic Newborn Screening: Evidence from Adult Biobanks
- **Authors / venue:** N.B. Gold, H. Zouk, J. Yeo, S. Lipsitz, S. Koyama et al. — *medRxiv*, 2026 (posted 06-10).
- **Surfaced by:** Konrad Karczewski + Lisa Bastarache *new related research* alerts (06-16) — **two-author saturation**.
- **Thread:** PheWAS/PheRS → **penetrance estimation under population-screening conditions** (vs clinically ascertained cohorts) + biobanks (AoU/UKB-tier) + newborn-screening policy.
- **What it is:** Long-term penetrance estimation for P/LP variants in **genes prioritized for genomic newborn screening (gNBS)** using adult biobanks. Framed around the policy question of gNBS positive predictive value (PPV) — i.e., if you screen a newborn and call them at risk for one of these conditions, how often does adult disease actually materialize over the lifetime? Snippet flags PPV uncertainty as the central question; biobank denominators are the population baseline against which clinical-cohort penetrance can be discounted.
- **Why it matters to you:** This is the **most directly on-thread paper of the window**. Your INTERESTS file specifically calls out "penetrance estimation for monogenic variants under population-screening conditions (vs. clinically ascertained cohorts)" — gNBS is precisely the population-screening operationalization. Two-feed saturation (Karczewski + Bastarache, the two most relevant author feeds for penetrance work) plus medRxiv venue suggests this will become the standard citation for *anyone* arguing about gNBS positive predictive value. Second consecutive window with a top-tier penetrance paper (Ramchand AIRE last window, Gold gNBS this window) — momentum in this area is building.
- **Action:** **HIGH** — read for (i) the gene panel composition (which gNBS-priority panel — RUSP/BabySeq/NSIGHT — and how many genes), (ii) the biobank denominator (UKB / AoU / MGB — likely MGB Biobank given Zouk affiliation), (iii) penetrance estimator (cumulative incidence to age X, or hazard-based), (iv) ICD/phecode mapping for the affected-status definition (this is where biobank-based penetrance most often goes wrong), and (v) the variant-curation level (ClinVar 2-star+ only, or includes likely-pathogenic). Citation-worthy for any of your gNBS- or population-penetrance-adjacent writing for the next ~2 years.

### 2. Harness All of Us for Equitable Disease Risk Prediction: A Tutorial with Case Study on Genetic Prediction Score for Rheumatoid Arthritis
- **Authors / venue:** Z. Kang, Y. Feng, C. Chen, Y. Hou, H. Yang et al. — *Statistics in Biosciences*, 2026.
- **Surfaced by:** Lisa Bastarache *new citations* (06-16) **AND** Chenjie Zeng *new citation* (06-16) — **this paper cites your "Comparison of phenomic profiles in the All of Us Research…" work**.
- **Thread:** Biobanks with EHR linkage (**AoU**) + genetic epidemiology (PRS) + chronic disease/IBD-autoimmune thread (RA) + cross-ancestry equity.
- **What it is:** End-to-end *tutorial* with a worked case study: build a rheumatoid-arthritis genetic prediction score on All of Us, with the AoU-specific data curation, cohort definition, and reproducibility plumbing made explicit. Snippet: "design of All [of Us studies] … workflow for streamlining data curation and analysis." Framed for *equitable* prediction, i.e., explicit attention to underrepresented populations.
- **Why it matters to you:** Triple-thread + self-citation. (a) AoU + PRS is squarely on your active EHR-linked biobank thread. (b) RA is on the autoimmune side of your IBD/autoimmune thread. (c) Equity framing aligns with cross-ancestry portability. (d) **Self-citation** — they cite your phenomic-profile-comparison AoU work, so it's worth knowing how they reference and extend it. Tutorial-format papers also tend to get heavy adoption in early-career and clinical-fellow groups, so this becomes a *teaching* citation for AoU + PRS in the same way the AoU clinical workflow papers became.
- **Action:** **HIGH** — read for (i) how they cite your phenomic-profile paper (context of the citation, exact framing), (ii) the PRS construction recipe (PRS-CS / LDpred2 / clumping+thresholding) and cross-ancestry handling, (iii) the AoU RA phenotype definition (ICD vs phecode vs lab/medication composite), (iv) the equity metric they actually evaluate (calibration in subgroups? AUC by genetic ancestry?). Worth tracking citation count over the next year.

### 3. Computable Structured Phenotype Versus Large Language Model Identification of Opioid Use Disorder Using Electronic Health Record Data
- **Authors / venue:** M.F. Molina, C. Fenton, K.T. LeSaint, S.D. Pimentel et al. — *Annals of Emergency Medicine*, 2026.
- **Surfaced by:** George Hripcsak + Pascal Brandt *new related research* alerts (06-16) — **two feeds**.
- **Thread:** EHR phenotyping (**computable phenotype vs LLM head-to-head**) + clinical NLP + LLM-assisted phenotyping evaluation.
- **What it is:** Direct comparison of a rule-based computable phenotype vs an LLM for identifying opioid use disorder in ED EHRs, with **expert physician review as the reference standard**. Reads as a methods-evaluation paper rather than a deployment claim — i.e., it's structured to inform the "should we use rules or LLMs for this phenotype?" decision.
- **Why it matters to you:** Your INTERESTS file calls out the LLM-vs-rules-based phenotyping comparison explicitly. The current literature mostly has *LLMs winning* on note-derived phenotypes and *rules winning* on structured-only phenotypes — this paper's ED-OUD setting is a mixed structured + free-text case, so the answer is genuinely informative. Two-feed surfacing (Hripcsak's OMOP world + Brandt's EHR-phenotyping world) is a strong signal it's the right paper for that question. Important precedent for methods sections in any of your own LLM-vs-rules AoU/MGB phenotype papers.
- **Action:** **HIGH** — read for (i) the gold-standard physician adjudication protocol (single vs adjudicated, blinded?), (ii) the rule-based phenotype's exact composition (DSM-5-style code list vs OMOP ATLAS reference set), (iii) the LLM choice and prompt/zero-vs-few-shot regime, (iv) the operating characteristic (sensitivity at high PPV, calibration on subgroups), and (v) whether they report cost/time/governance considerations — these usually decide the deployment question more than F1.

### 4. Points to consider for the reporting of variants of uncertain significance in germline genetic and genomic testing: A statement of the American College of Medical Genetics and Genomics (ACMG)
- **Authors / venue:** C. Mighton, A. Abu-El-Haija, V. Aggarwal, Y.M.N. Akkari et al. — *Genetics in Medicine*, 2026.
- **Surfaced by:** Heidi Rehm *new articles* alert (06-16).
- **Thread:** Variant interpretation (ACMG/ClinGen) — **VUS reporting practice**.
- **What it is:** ACMG official "Points to Consider" statement on **how to report VUSs** in clinical germline testing. Snippet: educational resource for clinical laboratory geneticists. This is community guidance, not a research paper — but it constrains the operating environment for everything you do with VUS data.
- **Why it matters to you:** ACMG Points-to-Consider statements become de facto standard for clinical labs within ~12 months. Anything you do that touches VUS reclassification (RNA evidence, functional evidence curation à la VarLitAgent last window) needs to align with what labs are *now allowed and expected* to report. Especially relevant if you're working with biobank-derived variant call sets where the VUS fraction dominates the actionable lookups.
- **Action:** **HIGH** — read for (i) the reporting-thresholds change (is "report VUS as VUS" still default, or are there new tiers like "VUS-warm" vs "VUS-cold"?), (ii) updated language for the clinical report (often a hidden source of EHR phenotype noise), (iii) downstream re-curation triggers (when a lab is now expected to *re-report* a VUS that becomes likely-pathogenic), and (iv) interaction with the prior 2025 SVI updates from ClinGen.

### 5. Detection of repeat expansion variants using next generation sequencing: A points to consider statement of the American College of Medical Genetics and Genomics (ACMG)
- **Authors / venue:** S. Guha, I.S. Rajan-Babu, A. Kesari et al. — ACMG statement, 2026.
- **Surfaced by:** Stephen B. Montgomery *new related research* alert (06-16).
- **Thread:** Variant interpretation (ACMG) — **repeat expansion detection** (specialized case).
- **What it is:** ACMG Points-to-Consider on detecting tandem/repeat expansion variants from short-read NGS (and likely long-read where relevant). Repeat expansions (HD, FXS, C9orf72 ALS/FTD, the SCAs, FAME loci) are notoriously under-detected by standard NGS pipelines.
- **Why it matters to you:** Repeat expansions are the *blind spot* in biobank-wide variant calling — neither standard short-read pipelines nor most rare-variant burden tests catch them, which means they are systematically missing from your PheWAS / penetrance estimation work. This statement defines what the field considers acceptable detection, and therefore which biobanks (UKB long-read pilots, AoU WGS, MVP) you can credibly use for repeat-expansion phenotype work.
- **Action:** **HIGH** — skim for the recommended tools (ExpansionHunter, STRipy, GangSTR variants), the per-locus genotyping-vs-screening dichotomy, and limits-of-detection language. Useful citation for any rare-disease or rare-variant penetrance paper that needs to bound which mutation types are in scope.

### 6. A proteomic polygenic score to identify IL-18 driven inflammatory bowel disease
- **Authors / venue:** M.C. Turchin, N. Raghupathy, C.L. Carty, M. Morris et al. — *medRxiv*, 2026 (posted 05-21, surfaced 06-16).
- **Surfaced by:** Joshua C. Denny *new related research* alert (06-16).
- **Thread:** Inflammatory bowel disease + genetic epidemiology (**proteomic PRS**) + drug-target stratification.
- **What it is:** Proteomic polygenic score targeting **IL-18 as a driver of an IBD etiologic subtype**. Snippet: "IL-18 … causally implicated in IBD risk and may represent a unique mechanism … to identify individuals predisposed to increased levels of IL-18, we implemented a polygenic [score on the IL-18 protein level]." This is essentially a *pQTL-based protein-PRS* used to stratify IBD into a mechanism-defined subtype rather than to predict overall risk.
- **Why it matters to you:** Two angles. (a) **Methods:** proteomic-PRS (pPRS) is the natural next step after standard PRS for personalized targeting of an immunotherapy — and your INTERESTS file explicitly calls out "biomarker-as-exposure scans" and "composite risk models stacking PRS with rare pathogenic variants." A protein-level PRS is exactly the missing intermediate layer in those composite models. (b) **Disease:** IBD is on your active autoimmune thread, and IL-18 modulators are a real drug development target (e.g., anti-IL-18BP). A patient-stratifier for IL-18-driven disease is directly the kind of pharmacogenomic personalization your causal-ML thread is built around.
- **Action:** **HIGH** — read for (i) the source IL-18 pQTL data (Olink vs SomaScan, UKB-PPP vs deCODE), (ii) the PRS construction (clumping+thresholding on the IL-18 pQTL, or LDpred-style?), (iii) the IBD outcome stratification — do high-pPRS individuals respond differentially to TNFi vs IL-18-axis drugs in any retrospective comparison?, (iv) external validation cohort if any (MGB, AoU, FinnGen).

### 7. The immunoproteome and multimorbidity: A Mendelian randomization study
- **Authors / venue:** N. Hukerikar, A.D. Hingorani, S. Chopade, A.J. Cupido et al. — *Science Advances*, 2026.
- **Surfaced by:** Joshua C. Denny *new related research* alert (06-16).
- **Thread:** Multimorbidity + genetic epidemiology (**multi-protein MR**) + drug-target prioritization.
- **What it is:** Mendelian randomization scan of immune proteins against multiple disease endpoints to identify **shared mechanisms across multimorbidity clusters**. Snippet: "eight large plasma proteome GWAS … shared mechanisms and therapeutic opportunities." Sits between the immunoproteome-MR work and your multimorbidity-clustering thread.
- **Why it matters to you:** Pairs naturally with #6 (Turchin proteomic IL-18 PRS) as the **same week, same proteome, two layers** — Turchin uses protein-PRS for *patient* stratification within one disease; Hukerikar uses MR to *map* immune proteins across diseases. Together they bracket the immunoproteome-to-clinical-action axis. Your multimorbidity thread (cardiometabolic MLTC last window, this immunoproteome paper this window) is now consistently surfacing top-tier items.
- **Action:** **HIGH** — read for (i) the protein → disease MR atlas (8 plasma proteome GWAS sources), (ii) any colocalization vs causal-MR distinction, (iii) the *cross-disease* shared mechanism findings (IL-6R, TNFR2 — the usual suspects, or surprises?), and (iv) overlap with the drug-target side (existing licensed biologics whose mechanism is reaffirmed).

### 8. APOL1 and chronic kidney disease in pediatrics: a study from the Biorepository and Integrative Genomics Initiative
- **Authors / venue:** R.S. Zahr, L. Chinthala, A. Mohammed, C.P. Kovesdy et al. — *Pediatric Nephrology*, 2026.
- **Surfaced by:** "APOL1" keyword alert (06-15).
- **Thread:** APOL1 disease thread (pediatric / EHR-linked biorepository).
- **What it is:** Pediatric APOL1 + CKD study using the Biorepository and Integrative Genomics (BIG) Initiative at UTHSC/St. Jude — an EHR-linked pediatric biorepository. Snippet is brief, but the framing (Pediatric Nephrology + biorepository) implies cross-sectional risk-allele × eGFR / proteinuria / CKD-stage analysis.
- **Why it matters to you:** Third APOL1 paper in three weeks (Pell mechanism, Varner review, now Zahr pediatric cohort). Your APOL1 thread is consistently fed — and pediatric APOL1 risk is methodologically interesting because the population-attributable burden is much lower than in adults, so the *penetrance estimation* problem (your other thread!) plus *ancestry-aware risk* (your equity work) compound.
- **Action:** **HIGH** — read for (i) the BIG biorepository pediatric denominator (sample size, age distribution, fraction with APOL1 high-risk genotype), (ii) the outcome definition (CKD by KDIGO, eGFR trajectory, proteinuria), (iii) the comparison to adult-cohort effect sizes (the *natural-history* signal — when does APOL1 risk start manifesting?). Useful complement to the adult AoU/MGB APOL1 work.

### 9. Myelodysplastic Syndromes in VEXAS
- **Authors / venue:** B.A. Patel, K.R. Calvo, K.K. Reichard, M.M. Patnaik — *Blood Advances*, 2026.
- **Surfaced by:** Daniel Kastner *new citations* (06-16).
- **Thread:** VEXAS / clonal hematoinflammatory disorders (CHIP-adjacent).
- **What it is:** Focused review/study on the MDS subset of VEXAS syndrome. Snippet: "VEXAS syndrome is a clonal hemato-inflammatory disorder impacting older, predominantly male [patients]…" — i.e., the MDS overlap is the *somatic UBA1* clone meeting the *clonal-cytopenia-of-undetermined-significance* spectrum.
- **Why it matters to you:** VEXAS is explicitly listed in your INTERESTS file alongside CHIP. The MDS overlap is the most clinically actionable subset because it's the one where allogeneic HSCT is on the table, and it sits exactly at the intersection of your CHIP and VEXAS threads. Kastner's group is the natural source for VEXAS papers; expect this to anchor the MDS-VEXAS field for ~2 years.
- **Action:** **HIGH** — read for (i) the IPSS-M vs UBA1-clone risk stratification, (ii) any EHR / claims-derived natural history (rare but possible from NIH cohorts), (iii) treatment-response data (azacitidine vs ruxolitinib vs HSCT). Useful for any composite-risk modeling that includes both germline rare variants and somatic CHIP/VEXAS clones.

### 10. Embeddings of clinical codes enable knowledge-grounded AI in medicine
- **Authors / venue:** R. Johnson, U. Gottlieb, G. Shaham, L. Eisen, J. Waxman et al. — *npj Digital Medicine*, 2026.
- **Surfaced by:** Marinka Zitnik *new articles* (06-15).
- **Thread:** EHR foundation models + knowledge graphs/ontologies (clinical-code embeddings).
- **What it is:** Pretrained embeddings of clinical codes (ICD, SNOMED, RxNorm, etc.) explicitly designed to support **knowledge-grounded** downstream AI. Snippet: "Standardization of electronic health records [is] [a precondition for…]" — i.e., they treat the code-embedding space as the substrate for LLM grounding.
- **Why it matters to you:** Fills the gap between two of your active threads — *EHR foundation models* (CLMBR/MOTOR/FEMR) and *knowledge graphs / ontologies* (SNOMED, HPO). Code embeddings are the obvious shared layer: CLMBR/MOTOR-style models use code-token embeddings internally; KG-grounded LLMs need embeddings that respect ontology semantics. Zitnik group publishing here means it'll be a serious technical entry, not a positional paper.
- **Action:** **HIGH** — read for (i) the embedding training objective (Cui2vec-style co-occurrence, SapBERT-style ontology-aware, or graph-neural?), (ii) the LLM-grounding evaluation (which downstream tasks, MedQA-style benchmarks vs phenotype-extraction utility), and (iii) whether the embeddings are released — practical reuse depends on this.

### 11. Enhancing Spectral Embedding through Robust and Flexible Knowledge Transfer in Electronic Health Records
- **Authors / venue:** F. Huang, Z. Xia, R. Ma, T. Cai — *arXiv preprint*, 2026 (arXiv:2606.11570).
- **Surfaced by:** Pascal Brandt + George Hripcsak *new related research* (06-15) — **two feeds**.
- **Thread:** EHR phenotyping (embedding methods, knowledge-transfer across sites).
- **What it is:** Spectral-embedding method for EHRs that incorporates knowledge transfer — i.e., the spectral decomposition leverages prior structure (likely from ontologies or pretrained embeddings) for robustness on smaller cohorts. Cai group has been productive in this corner of EHR-stat methods.
- **Why it matters to you:** Spectral / PMI-based EHR embeddings are the *classical* baseline against which the more recent token-level FMs (CLMBR/MOTOR) get measured. A flexible-knowledge-transfer version is methodologically useful for small-cohort phenotyping where pretraining isn't feasible, which is most disease-specific cohorts you'd build inside AoU. Two-feed surfacing in the OMOP-adjacent author set is a meaningful signal.
- **Action:** **HIGH (methods)** — read for (i) the knowledge source (ontology Laplacian? pretrained embedding warm-start?), (ii) the robustness claim (sample-size, noise, missingness), and (iii) the comparator (does it beat CLMBR/MOTOR on small-cohort tasks, or only beat plain spectral?).

### 12. The anti-inflammatory efficacy of melanocortin drugs is influenced by genetic variation at MC1R
- **Authors / venue:** N. Khodeneva, C.S.A. Davan-Wetton, T.E.N. Jonassen et al. — *Scientific Reports*, 2026.
- **Surfaced by:** Konrad Karczewski + Joshua C. Denny *new citations* (06-16) — **two feeds**.
- **Thread:** Pharmacogenomics + drug-class pharmacoepi (anti-inflammatory) + genetic epi.
- **What it is:** MC1R genetic variation modifying the efficacy of melanocortin-class anti-inflammatory drugs. Reads as a mechanism-and-pharmacogenomics piece, not (yet) a clinical RWE study. MC1R is a strong pharmacogenomic locus because the loss-of-function alleles (red-hair-associated R alleles) are at appreciable population frequency.
- **Why it matters to you:** Drug-class × variant-carrier interaction is the recurring shape in your pharmacoepi thread (Marston SGLT2i × cardiomyopathy variants last window, Fritsche PRS × ICI thyroiditis last window, this window's pPRS-IBD #6). MC1R + melanocortins is a clean pharmacogenomic dyad with both *population-scale* variants (R alleles ~10% in European ancestry) and *therapeutic relevance* (acthar, melanocortin agonists). Two-feed surfacing (Karczewski + Denny) signals genetic-epi relevance, not just niche pharmacology.
- **Action:** **HIGH** — skim for the experimental model (likely cellular / preclinical), the specific MC1R variants studied, and any human-cohort validation. Useful citation for pharmacogenomic introduction sections.

### 13. Association and risk prediction of 19 complex diseases with polygenic scores and socioeconomic status
- **Authors / venue:** F.A. Hagenbeek, A. Richmond, M. Tamlander, K. Detrois et al. — *Communications Medicine*, 2026.
- **Surfaced by:** Lisa Bastarache *new related research* (06-16).
- **Thread:** Genetic epidemiology (PRS) + multimorbidity + chronic disease clustering + equity.
- **What it is:** Joint PRS × SES association across 19 complex diseases. Snippet: "how these factors jointly relate to multiple diseases is not fully understood … independent and combined associations." Sounds like a phenome-wide × biobank-scale PRS+SES interaction scan rather than a single-disease prediction paper.
- **Why it matters to you:** Directly on the *composite-risk-model* part of your INTERESTS file. PRS × SES is a recurring framing in equity-aware risk prediction; doing it across 19 diseases gives a multimorbidity-flavored picture too. Pairs with Kang et al. (#2) as the same week's PRS-equity package — Kang does the AoU + RA tutorial framing, Hagenbeek does the multi-disease atlas framing.
- **Action:** **HIGH** — read for (i) cohort (likely FinnGen or pooled European biobanks, given author list), (ii) PRS source for the 19 diseases (PGS Catalog stock or re-derived?), (iii) the *interaction* analysis (additive vs multiplicative — important for clinical decision-curve interpretation), and (iv) any decomposition into chronic disease clusters.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **General-purpose LLMs outperform specialized clinical AI tools on medical benchmarks** — K. Vishwanath, A. Alyakin, M. Ghosh, A. Hage, S.N. Neifert et al. — *Nature Medicine*, 2026 (Natarajan citation feed, 06-16). Head-to-head benchmark of general-purpose LLMs (presumably frontier-tier) vs specialized clinical models. Important context for any methods section where you justify model choice. *Watch for:* the benchmark set composition and whether they handle the deployment-vs-benchmark distinction (i.e., does the specialized model's calibration in deployment recover the gap?).
- **When can whole-genome SNP heritability be reliably estimated from summary statistics?** — B.K. Pham, S. Davenport, D. Azriel, A. Schwartzman — *bioRxiv*, 2026 (Jian Yang feed, **3rd consecutive window surfacing**). Already covered in the prior report; mention here because the third surfacing across feeds indicates it's the methods reference of the spring. *Watch for:* the failure-mode taxonomy and any diagnostic the authors propose.
- **Polygenic risk scores associate with asthma phenotypes and proteomic analyses implicate IL1R1 in two family-based studies** — S. Lee, M. Moll, K. Mendez, N. Prince, J. Lasky-Su et al. — *medRxiv*, 2026 (Bastarache feed). Same-week sibling to Turchin #6: another proteomic-aware PRS, this time on asthma with IL1R1 implicated. *Watch for:* the family-based design (TDT-style or sibship-based — this is the part that controls for population stratification more rigorously than population-based PRS work).
- **Advancing Clinical Implementation of Cardiovascular Polygenic Risk Scores Through Patient-Level Robustness Assessment** — R. de La Harpe, J. Vaucher, Z. Kutalik, J. Fellay et al. — *medRxiv*, 2026 (Bastarache feed). Patient-level *intra-individual* PRS variability — i.e., the same patient gets different risk estimates from different equally-good PRSs. *Watch for:* the calibration / disagreement metric they use (this is the actionable methods piece for any PRS deployment work). Pairs with the Fellay group's VarLitAgent from last window.
- **A Large Language Model for Extracting Post-marketing Adverse Drug Events from Clinical Notes in the Electronic Health Record** — D. Ludwig, M. Wang, J. Buchanan, T. Trinh — *Drug Safety*, 2026 (Hripcsak feed). LLM-extraction of ADEs from clinical notes for pharmacovigilance. Off your active disease threads but exemplary methods if your pharmacoepi work ever needs note-derived ADE signals. *Watch for:* the precision/recall on serious-vs-non-serious ADE distinction, and the model choice (open-weight vs API).

---

## SKIP / noise (logged, no action)

- **Repeat-surfacing items**: Gold gNBS penetrance paper (#1) appears in both Karczewski and Bastarache feeds — consolidated in the report above, not double-counted. Vishwanath general-purpose LLM paper appears in Natarajan and likely other tech-medicine feeds — consolidated under METHODS-WATCH.
- **"APOL1" keyword feed**: Zahr et al. (#8) is the on-thread item; the other items in this feed cluster were genuinely on-thread and folded into the APOL1 thread above.
- **Tabular/general-purpose ML papers**: Liu et al. *Benchmarking AI Agents for Scientific Challenges Across Scales* surfaced in three feeds (Pritchard, Zitnik, Zou). Generic AI-agents benchmark, no biomedical phenotype/EHR/variant angle. SKIP.
- **Off-thread Mendelian-randomization items**: Tschiderer (sex-specific lipid MR), Pehkonen (childhood adiposity → labor markets), Pell-MR on stroke proteomics, etc. All MR-only without the rare-variant/penetrance/pharmacoepi angle. SKIP.
- **Brain-imaging / fMRI items**: Ebneabbasi *Genetic basis of dynamic brain states* (surfaced in multiple feeds via medRxiv). Off your thread. SKIP.
- **Single-cell + LLM agent benchmarks**: Liu *Benchmarking AI Agents*, M*: Modular Serving System for Multimodal Models (Leskovec feed), SimSD diffusion LM (Zitnik), Detecting Functional Memorization in Code LMs (Zitnik), Risk Under Pressure adversarial robustness (Szolovits) — all generic ML, not clinical/EHR/variant. SKIP.
- **Drug repurposing keyword feed**: nothing on the KG/GNN-explainability or EHR-mining angle this window. (NCBI digests from 06-12/13 are pre-window.) SKIP.
- **Educational / policy / patient-portal items**: Yamada *Rare Diseases education review* (Chute + Montgomery feeds), Richwine *Patient portal test result understanding* (Hripcsak feed), Uttley *UK Institutional Guidance for AI in Research* (Szolovits feed), Kohane *Guideline Machines* (Kohane self-citation). All adjacent but off the research-methods threads. SKIP.
- **AoU clinical-question papers**: none surfaced this window (vs the 3 in last window's AoU set). Net: zero.

---

## Suggestions for the pipeline

Carrying forward (4th consecutive report) and adding:

1. **`arxiv-digest` is silent this window — three days of zero papers.** The pipeline is alive (dedup correctly suppressed previously-seen items), but q-bio/stat.AP isn't producing anything scoring ≥2 on the current keywords in the 30 h window. The 100%-Scholar-sourced state of this report means the keyword-set + category-set on arxiv-digest is now under-serving your actual research surface. The recommendations from the last three reports stand and are increasingly urgent:
   - **Add `cs.LG`, `stat.ME`.** This window's Hukerikar immunoproteome MR, Hagenbeek PRS+SES, Huang spectral-embedding-with-knowledge-transfer would all have hit stat.ME or cs.LG.
   - **Add a medRxiv source.** Gold gNBS penetrance, Turchin pPRS-IBD, Hagenbeek 19 diseases, de La Harpe CVD PRS robustness, Pham LDSC failure modes — **all five** medRxiv preprints this report. medRxiv coverage would have caught the entire HIGH-priority list except the journal-published items (Mighton, Guha, Molina, Patel, Johnson, Kang, Khodeneva).
2. **Add `OMOP` as a keyword** — Kang et al. (#2) is implicitly OMOP-adjacent via AoU; the agentic OMOP concept-set authoring from last window was missed by current keywords.
3. **Add `proteomic PRS` or `protein polygenic`** — Turchin #6 and Lee (METHODS-WATCH) this window are the second and third proteomic-PRS papers in two reports.
4. **Add `points to consider`** as a keyword — ACMG / ClinGen Points-to-Consider statements (Mighton, Guha this report) are high-value low-volume, easy to surface by literal phrase.
5. **`mendelian diseases` keyword** still leaks Mendelian-randomization papers (Tschiderer, Pehkonen, Hukerikar etc. this window). Replacement to `OMIM` / `MIM` or addition of `-randomization` recommended for the 4th time.
6. **Self-citation hits**: Kang et al. citing your "Comparison of phenomic profiles in the All of Us" paper is this window's signal. Useful audit data.
7. **Author feeds firing all at once on 06-16** — most of your tracked author Scholar feeds (24+ feeds) delivered in the same wave at 07:23Z. This is Scholar's behavior, not yours, but it means the *triage burden compresses to one morning per week* — worth knowing when planning when to read this report.
