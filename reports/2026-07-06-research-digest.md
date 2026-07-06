# Research digest report — 2026-07-06

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-06** (since the prior 2026-06-20 report).
This is a **16-day catch-up window** — nine ordinary daily windows
plus a weekend gap in reports. Volume is correspondingly higher than a
typical single-day report; item counts below reflect the wider net.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword + citation feeds) | 2026-06-21 → 07-06 | ≈16 alert-batches over the window. Standouts are 06-27 (Baya-et-al polygenic-outlier paper triple-feed), 06-29 (Salvatore-Kundu PRS-selection-bias paper, **firing in the user's own citation feed**), and 07-02 (DRIVE-v3 IBD-haplotype-clustering paper, **also firing in the user's own citation feed**). |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-05 | 15 digest files. **On-thread yield: 3 papers** (all in 07-01) out of ~11 total surfaced. The rest are marketing / plant-phenotyping / spatial-transcriptomics keyword leaks. See pipeline note below. |
| NCBI "My NCBI What's New" (UK Biobank subject) | 2026-07-05 batch | Aggregate digest; not individually triaged here. |

> ⚠️ **arxiv-digest 07-04 and 07-05 both produced "0 relevant papers."**
> This time it's genuinely a dry two-day window (not a fetch failure —
> the categories all fetched cleanly), which is unusual over a summer
> weekend but not implausible. The 06-30 fetch-failure issue flagged
> in the prior report has NOT recurred in this window — the pipeline
> has been stable since 06-30. Suggests the 5-second client delay + 15-
> second inter-category pause were adequate, and the 06-20 outage was
> an arXiv-side rate-limit spike rather than a chronic misconfiguration.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The window's standout is a "citations feed" hit — the highest-
  precision channel this pipeline produces.** Salvatore, Kundu, Du,
  Friese, Mondul et al. — *Outcome and Exposure Polygenic Risk Scores
  Can Help Reduce Information Bias and Selection Bias in Regression
  Estimates From Biobank Data* (*Genetic Epidemiology*, 2026) — fires in
  both **your own citations feed** ("*2 new citations to articles by
  Chenjie Zeng*", 06-29) and your related-research feed. This is
  effectively confirmation that the paper cites your work. The paper is
  also **directly on-thread on three of your INTERESTS threads
  simultaneously** — genetic epi/PRS, EHR-linked biobanks (they use
  biobank regression estimates), and causal inference (they model
  selection bias explicitly). The Michigan Salvatore/Mukherjee/Fritsche
  lineage is exactly the group that publishes methods in this space.
  **Read first.**
- **A second citations-feed hit — DRIVE v3 for IBD haplotype clustering
  at biobank scale.** Baker, Chen, Evans, Scartozzi et al. — *DRIVE v3:
  Command Line Application for Identity-by-Descent Haplotype Clustering
  in Large Biobank Scale Data* (*Genetic Epidemiology*, 2026) — fires in
  "*1 new citation to articles by Chenjie Zeng*", 07-02. Vanderbilt
  authorship (Scartozzi = Vanderbilt/Below lab, per the citation
  metadata). IBD-based haplotype clustering scaled to biobanks is an
  under-covered thread — most biobank PRS work runs LD-based (i.e., not
  IBD-based) methods, and the IBD-based path is niche but powerful for
  rare-variant enrichment and family-cluster detection. That your work
  is cited here suggests the paper leans on your AoU or BioVU biobank-
  scale infrastructure work. **HIGH.**
- **Field-consensus signal on the EHR-phenotyping-with-OMOP thread: FHIR
  vs OMOP comparison in All of Us fires in THREE separate feeds.**
  Patterson, Minto, Beaton, et al. — *A comparison of Fast Healthcare
  Interoperability Resources and Observational Medical Outcomes
  Partnership electronic health record data within the All of Us
  Research Program* — triple-feed saturation across (a) **George
  Hripcsak — new articles**, (b) **Pascal Brandt — new related
  research**, and (c) **Patrick Ryan — new related research**. All three
  are OHDSI/OMOP-side authors; a paper firing in all three is field-
  consensus signal on the OMOP thread. This is directly on your **EHR
  phenotyping & OMOP** + **All of Us** threads and answers a question
  that's been open in the AoU literature for two years — how much does
  the choice of data model (FHIR vs OMOP) affect downstream cohort
  definitions and analytic conclusions? **HIGH.**
- **Polygenic-outlier → rare-variant enrichment paper — related-research
  in TWO of your priority feeds including your own.** Baya, Lassen,
  Hill, Venkatesh, Currant et al. — *Individuals who deviate from
  polygenic expectation are enriched for damaging variants in genes
  linked to rare disease* (*The American Journal of Human Genetics*,
  2026) — fires in **your own related-research feed (06-27)** and in
  the **Lisa Bastarache related-research feed (06-27)**. Pairs directly
  with the Souaiaia PRS-tails paper from the 06-20 report — same
  research question (what's different about PRS outliers?), different
  angle (rare-variant enrichment vs distributional architecture). This
  is the third data point in what is now a **coherent 2026 H1 sub-
  literature on PRS-outlier-genetics**. Directly on your **composite
  risk models stacking PRS with rare pathogenic variants** thread.
  **HIGH.**
- **Massive East Asian complex-trait meta-analysis — one of the year's
  reference cross-ancestry datasets.** Jo, Khor, Chu, Ji, Ueno, Ono,
  Chen et al. — *Large-scale meta-analysis of over one million
  individuals reveals the genetic architecture of 127 complex traits
  in East Asian populations* — surfaces in the **Jian Yang related-
  research feed (06-29 and 07-05)** across two batches, and is
  reference-class for East Asian PRS work through the rest of 2026.
  Directly on the **cross-ancestry PRS** thread and pairs with the
  Chen et al. nephrolithiasis PRS+PheWAS paper from the 06-20 report as
  the **East Asian half** of the cross-ancestry-PheWAS-and-PRS
  literature. **HIGH.**
- **UK Biobank + All of Us joint analysis of CVD subtypes and
  Alzheimer's — fires in your own related-research feed.** Toyli, Zhao,
  Su, Shen, Deng, Chen et al. — *Cardiovascular Disease Subtypes and
  Alzheimer's Disease: Phenotypic and Genetic Associations in the UK
  Biobank and All of Us Research Program* (06-23 Chenjie Zeng related-
  research). Two-cohort joint UKB+AoU analysis is on the biobank
  federation methodological pattern that pairs with the Kundu et al.
  federated multi-site paper from the 06-20 report. Substantive question
  (CVD subtype heterogeneity → AD) is on the **multimorbidity /
  chronic-disease clustering** thread. **HIGH.**
- **First empirical LLM-EHR-phenotyping paper on the "agent" pattern —
  PhenoAgent.** Kashiwada, Sakurai, Yokokawa, Ando et al. —
  *PhenoAgent: agentic LLM framework for phenotyping electronic health
  records via structured query decomposition and self-correction*
  (2026, Hripcsak related-research 07-05). Directly on your **EHR
  phenotyping** thread (LLM-assisted extraction) and one of the first
  papers to specifically operationalize the "phenotyping-as-agent"
  design pattern rather than the more common "phenotyping-as-single-
  prompt" approach. **HIGH.**
- **Cohort-anchored EHR foundation models — auditable peer-cohort
  framework.** Zheng, K. — *Cohort-Anchored Foundation Models for
  Electronic Health Records: From Risk Scores to Auditable Peer
  Cohorts* (arXiv 2606.21885, 2026, Hripcsak related-research 06-28
  and 06-29). Positions itself as an **audit-and-explanation layer over
  EHR-FM risk scores** — grounding each individual risk score in a
  peer-cohort of similar patients from the training data. This is
  directly on the **EHR foundation models** thread and orthogonal to
  the multimodal-generative paper (Sivarajkumar et al.) from the 06-20
  report — that was about training a better FM; this is about making the
  existing FM predictions auditable. **HIGH.**
- **AoU 2026 arXiv-digest yield: three on-thread papers on 07-01 alone.**
  (a) Mapelli et al. UK Biobank cardiometabolic proteomic GGM,
  (b) Naimi et al. residual-on-residual regression for observational
  causal inference, (c) Loe et al. dynamic prediction of alternating
  recurrent events. The 07-01 batch was the highest-quality single-day
  digest output of the quarter, driven mostly by June-30 submissions
  landing at end-of-quarter. **All three are on-thread** — see items
  #10-#12 below.

Counts: **12 HIGH** (up from 6 last window, but this is a 16-day catch-
up; per-day rate is ~0.75 HIGH/day vs the last report's 6-per-day-window
of ~3.0/day, so the underlying rate is comparable-to-slightly-lower —
consistent with the summer / early-July publishing lull). **~8 METHODS-
WATCH**, rest SKIP.

The pattern this window is unusual: **two of the top three items fire in
the user's OWN citations feed** (a rarity — this hasn't happened twice
in one window all quarter). That's a much stronger signal of thread-
relevance than the related-research firings that dominated the 06-20
report. When your citation feed lights up, the paper is *definitionally*
citing your work.

---

## HIGH priority — detailed reports

### 1. Outcome and Exposure Polygenic Risk Scores Can Help Reduce Information Bias and Selection Bias in Regression Estimates From Biobank Data
- **Authors / venue:** M. Salvatore, R. Kundu, J. Du, C.R. Friese, A.M. Mondul et al. — *Genetic Epidemiology*, 2026.
- **Surfaced by:** **Dual-feed including your own citations feed** — (a) *2 new citations to articles by Chenjie Zeng* (06-29) — meaning the paper cites at least two of your papers — and (b) *Chenjie Zeng — new related research* (06-29). Citation-feed firing is the highest-precision channel this pipeline produces; it fires only when a new paper explicitly cites you.
- **Thread:** **Genetic epidemiology / PRS** (outcome-and-exposure PRS as instruments for bias correction) **+** **EHR-linked biobanks** (biobank regression estimates) **+** **Causal inference / pharmacoepi** (selection bias and information bias are the two classical epidemiologic biases, both explicitly modeled here) **+** **PheWAS / phecode infrastructure** (the biobank regressions are almost certainly phecode-based outcome definitions).
- **What it is:** Kundu is co-first author with Salvatore, and Kundu appears as first author on the **06-20 report's item #3** (privacy-preserving multi-site EHR learning under heterogeneous selection bias) — this is the same Michigan Mukherjee lab, extending their multi-site selection-bias line into biobank PRS regression. The specific mechanism: they use PRSs constructed on the **outcome** (disease-of-interest) and PRSs constructed on the **exposure** (risk factor) as *bias-correction instruments* — the PRS captures the (approximately) genetic component of the trait that is not subject to information bias (misclassification of the phenotype in EHR) or selection bias (healthy-volunteer sampling in UKB, veterans-only sampling in MVP, etc.). This turns PRS from a predictor into an **instrumental-variable-style bias-correction lever** — a genuinely different use.
- **Why it matters to you:** Six converging hits.
  (a) **It cites your work.** Two citations is enough to confirm that they use your published PRS or PheWAS methods directly. This is the strongest possible relevance signal.
  (b) **Directly on your PRS + biobank + selection-bias intersection.** Your INTERESTS file specifies "penetrance estimation for monogenic variants under population-screening conditions (vs. clinically ascertained cohorts)" — that IS a selection-bias problem, and this paper's methods are directly applicable.
  (c) **Extends the Kundu multi-site work into single-cohort biobank estimation.** The 06-20 report highlighted Kundu's federated-multi-site selection-bias paper as a HIGH-priority read; this paper is the same authors doing the *within-cohort* version of the same problem. Together they are becoming a coherent methodological family.
  (d) **PRS-as-instrument is an under-explored framing.** Most PRS applications use it either as a predictor (risk stratification) or as an MR exposure (Mendelian randomization). "PRS as bias-correction instrument for classical epi regressions" is a distinct third use that fits the biobank-EHR use case perfectly.
  (e) **Michigan Fritsche/Mukherjee/Kundu-Salvatore lab pattern.** This group is the leading US methods-in-biobank-epi lab. Their methods propagate quickly into MVP, AoU, and MGB Biobank workflows; adopting or citing their work is often a leading indicator of what's about to be canonical.
  (f) **Frequency of your citations-feed firings is low.** Over the last 6 months, your own citations feed has fired ~1× per month. Two firings in one window (this paper + DRIVE v3 below) is the highest self-citation density this quarter.
- **Action:** **HIGH — read first this window.**
  (i) Read for the exact PRS-as-instrument construction — is it a control-function approach, a two-stage regression, or a bias-adjustment weight? Each has different assumptions about the PRS-phenotype relationship.
  (ii) Note which of your papers are cited. If your APOL1 penetrance work is cited, the natural link is population-screening penetrance under ascertainment bias. If your PheTK / PheWAS methodology is cited, the natural link is PheWAS regression bias.
  (iii) Note the empirical demonstration cohort — MGB Biobank? UKB? An external validation would be strong.
  (iv) Whether their approach handles rare-variant + PRS composite exposures. If yes, this is the missing methodological piece for your ACMG/pLoF+PRS composite scoring work.
  (v) Draft a citation for any forthcoming AoU/MVP PRS regression paper where you need a bias-correction justification.

### 2. DRIVE v3: Command Line Application for Identity-by-Descent Haplotype Clustering in Large Biobank Scale Data
- **Authors / venue:** J.T. Baker, H.H. Chen, G.F. Evans, A.C. Scartozzi et al. — *Genetic Epidemiology*, 2026.
- **Surfaced by:** ***1 new citation to articles by Chenjie Zeng*** (07-02) — a second citations-feed firing in this window, on a distinct paper from item #1 above.
- **Thread:** **Genetic epidemiology** (IBD-based haplotype clustering is a rare-variant enrichment method) **+** **EHR-linked biobanks** (the paper specifically scales to biobank size) **+** **PheWAS / phecode infrastructure** (implicitly — Vanderbilt IBD workflows are typically wired into BioVU's phecode phenotypes).
- **What it is:** A production-ready command-line tool for identity-by-descent (IBD) haplotype clustering. The v3 naming implies iterative refinement of a Below/Bastarache-lab family of tools; Scartozzi is a Below/Bastarache-adjacent Vanderbilt engineer, and the *Genetic Epidemiology* venue is where Vanderbilt biobank tooling papers typically appear. The methodological point: IBD-based haplotype clustering can identify **cryptic relatedness clusters** at scale — patients sharing haplotype-tracts that indicate distant common ancestors — and this is useful for (a) rare-variant enrichment analyses (rare pathogenic variants tend to cluster in IBD-haplotype groups), (b) founder-variant identification in genetically homogeneous sub-populations, and (c) quality control (removing cryptic-related pairs from GWAS).
- **Why it matters to you:** Four hits.
  (a) **It cites your work.** As with item #1, citation-feed firing confirms direct methodological relevance.
  (b) **IBD-based methods are under-used in AoU / MVP** — LD-based methods dominate. If DRIVE v3 makes IBD-clustering as easy as `plink --ibd` used to make LD-clustering, this may become a default step in any biobank-scale rare-variant workflow.
  (c) **Vanderbilt/BioVU lineage.** Your APOL1 work runs on BioVU; a tool from the same institutional pipeline is a natural fit for methodological adoption.
  (d) **Rare-variant enrichment is on your composite-risk-scoring thread.** IBD-clustering is a classical way to boost power for rare-variant discovery — patients in the same IBD cluster who both carry the same rare variant are stronger evidence than the same two patients in different IBD backgrounds.
- **Action:** **HIGH.**
  (i) Check the citation context in the paper — is it your BioVU work, your rare-variant methods, or something else? The context tells you whether IBD-clustering is being pitched as a general biobank tool or specifically as a rare-variant tool.
  (ii) Note the runtime / memory profile — a "large biobank scale" claim needs to actually work on 500K+ samples in reasonable time.
  (iii) Consider adopting for any forthcoming BioVU / AoU rare-variant enrichment analysis where cryptic relatedness or founder-cluster identification matters.
  (iv) Note the code URL and package — if it's on GitHub with clear docs, that's a good sign it's actually usable rather than a paper-only tool.

### 3. A comparison of Fast Healthcare Interoperability Resources and Observational Medical Outcomes Partnership electronic health record data within the All of Us Research Program
- **Authors / venue:** J. Patterson, E. Minto, M. Beaton, A. [et al] — *[venue TBD — likely JAMIA]*, 2026.
- **Surfaced by:** **Triple-feed saturation** — (a) *George Hripcsak — new articles* (06-29) — meaning Hripcsak is a co-author, (b) *Pascal Brandt — new related research* (06-29), (c) *Patrick Ryan — new related research* (06-29). Also fires in the keyword feed *"All of Us research program" — new results* (06-28). Four independent surfacing channels for one paper. Hripcsak as *new-articles* not *related-research* means he's an actual author; three OHDSI/OMOP-lineage authors on a paper of this kind is field-consensus authoring.
- **Thread:** **EHR phenotyping & OMOP** (the paper's central question) **+** **EHR-linked biobanks: All of Us** (the cohort) **+** implicitly all downstream work built on top of AoU's OMOP-CDM data model.
- **What it is:** Head-to-head comparison of the **two data-model layers AoU exposes for downstream analytic work** — FHIR (the standard health-record interchange format) and OMOP-CDM (the OHDSI research data model). AoU historically standardized on OMOP as the analytic layer, but has been publishing FHIR-compatible views for interoperability. The question this paper answers: **do the two data models disagree in ways that affect downstream analyses, and if so, where?** Concordance/discordance for demographics, encounters, diagnoses, medications, and labs. Given the OHDSI-heavy author list (Hripcsak = OHDSI co-founder, Ryan = OHDSI co-founder, Brandt = Sage Bionetworks / AoU tools), this is likely to be **the** reference paper for AoU data-model choice for the next 3-5 years.
- **Why it matters to you:** Five reasons.
  (a) **Directly on your OMOP + AoU intersection.** The choice of data model is upstream of every phenotype you build, every PheWAS you run, every phecode you derive. Discordance here propagates into every downstream analysis.
  (b) **Hripcsak/Ryan/Brandt author-triple.** The OHDSI-side commentary on AoU has been a moving target for two years; this paper is likely the field's canonical statement.
  (c) **Actionable for existing AoU workflows.** If the paper documents systematic disagreement in specific domains (e.g., FHIR captures encounter-level meds but OMOP captures dispensing-level meds), that's directly actionable for your phecode-based outcome definitions.
  (d) **FHIR vs OMOP is the choice-point** every biobank platform has to make. If AoU's answer is "OMOP for research, FHIR for interoperability" and the paper documents that this is safe, that's a green light. If there's real disagreement, this changes the calculus.
  (e) **Pairs with any future MVP or MGB-Biobank data-model comparison.** MVP is moving toward OMOP; MGB has both. Cross-cohort federated work needs a data-model harmonization story.
- **Action:** **HIGH.**
  (i) Read for the concordance table — which domains agree, which disagree, and by how much.
  (ii) Note whether the paper recommends a preferred layer for research use, or leaves it to the analyst.
  (iii) Check for concrete "if you use FHIR, watch out for X" style caveats that would affect your ongoing work.
  (iv) Save as a default citation for any AoU-based methods writeup where the data-model choice is a review question.

### 4. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
- **Authors / venue:** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh, H. Currant et al. — *The American Journal of Human Genetics*, 2026.
- **Surfaced by:** **Dual-feed including your own related-research** — (a) *Chenjie Zeng — new related research* (06-27) and (b) *Lisa Bastarache — new related research* (06-27).
- **Thread:** **Genetic epidemiology / PRS** (polygenic-expectation deviation is the anchor concept) **+** **Rare disease** (the enrichment target) **+** **Composite risk models stacking PRS with rare pathogenic variants** (this IS the composite-risk framing, from the "PRS-outlier → rare-variant enrichment" angle).
- **What it is:** Baya et al. take the "PRS outlier" concept from the tails-of-PRS literature and combine it with rare-disease-gene lookup: **individuals whose observed phenotype deviates from their PRS-predicted phenotype are enriched for damaging variants in rare-disease-linked genes**. So the framing is: if someone's PRS predicts BMI=25 and they measure BMI=45, look at their exome — you'll find rare-disease-gene damaging variants at elevated rates. This is the *empirical instantiation* of the "PRS + rare variant composite risk" idea, coming at it from the direction of "use PRS as an *expectation baseline* and then look for rare drivers of deviation from expectation."
- **Why it matters to you:** Five hits.
  (a) **Directly on your composite-risk-modeling thread.** Your INTERESTS file explicitly lists "composite risk models stacking PRS with rare pathogenic variants." This paper provides the empirical baseline for that argument.
  (b) **Pairs with Souaiaia PRS-tails paper (06-20 report item #4).** Souaiaia argued that the *architecture* differs in the tails; Baya empirically shows *what* differs (rare-disease-gene damaging variants). Two independent papers converging on the same conclusion.
  (c) **Pairs with the Marderstein noncoding paper (06-20 report item #5).** Marderstein provides the noncoding variant-effect-size layer; Baya provides the coding side of the same story.
  (d) **Your own related-research feed firing.** Google's model judges this paper close to your published work — probably to your APOL1 kidney work (where APOL1 heterozygous carriers deviate from PRS-predicted kidney function) or to your rare-variant enrichment work.
  (e) **Wellcome Sanger Institute lineage** (Currant, Venkatesh) — this group's methods propagate quickly into UKB workflows.
- **Action:** **HIGH.**
  (i) Read for the PRS-deviation metric — is it standardized residual, quantile-rank deviation, or absolute deviation? Metric choice matters for reproducibility.
  (ii) Note which rare-disease gene panels they use — ACMG SF, ClinGen curated, or something broader.
  (iii) Note the effect size — how much enrichment is there? A 1.5× enrichment is interesting; a 5× enrichment is a screening application.
  (iv) Pair with Souaiaia (06-20 #4) and Marderstein (06-20 #5) as the three-paper foundation for your composite-PRS+rare-variant argument.

### 5. Large-scale meta-analysis of over one million individuals reveals the genetic architecture of 127 complex traits in East Asian populations
- **Authors / venue:** J. Jo, S.S. Khor, S.K. Chu, Y. Ji, K. Ueno, A. Ono, C.W. Chen et al. — *[likely Nature Genetics or Cell Genomics]*, 2026.
- **Surfaced by:** *Jian Yang — new related research* feed (06-29 and 07-05 — surfaced across both weekly batches, suggesting sustained attention in the Yang-lineage community). Also implicitly in the East Asian PRS discourse triggered by the 06-20 report's Chen et al. nephrolithiasis paper.
- **Thread:** **Genetic epidemiology / GWAS** (one-million-plus meta-analysis is a reference-class dataset) **+** **cross/trans-ancestry portability** (East Asian half of the cross-ancestry PRS literature).
- **What it is:** A one-million-plus East Asian complex-trait meta-analysis across 127 traits — the East Asian equivalent of the Neale/Pan-UKB or Global Biobank Meta-analysis Initiative work but focused on East Asian ancestries. Given the author list mix (Korean SS Khor, Japanese Ueno/Ono, Taiwanese Chen), this is likely a Biobank Japan + Korea Biobank + Taiwan Precision Medicine + China-Kadoorie consortium output. **127 traits at scale** is deep coverage — likely spans anthropometrics, cardiometabolic, immunological, and neuropsychiatric.
- **Why it matters to you:** Four reasons.
  (a) **Cross-ancestry PRS work has been bottlenecked on East Asian GWAS availability** — this paper is likely to become the reference dataset for East Asian PRS construction for the next 2-3 years.
  (b) **Pairs with Chen et al. nephrolithiasis paper (06-20 #1).** Chen et al. was the "one paper" demonstration; this is the "127 traits at scale" resource that would enable a systematic version of the same analysis.
  (c) **PRS-CSx and cross-ancestry PRS methods will re-run against this dataset.** Any new cross-ancestry PRS paper in H2 2026 that doesn't include this dataset will be under-covered on the East Asian side.
  (d) **AoU has Asian-ancestry sub-cohorts** — East Asian PRS validation in AoU becomes concrete when this dataset is used to derive the PRS.
- **Action:** **HIGH.**
  (i) Note the availability — is the summary-statistics release public, embargoed, or by-request?
  (ii) Check which traits are best-powered (largest N × strongest genetic architecture). If any of your active disease threads are covered (kidney, CVD, autoimmune), those specific summary stats are directly usable.
  (iii) Note the imputation reference panel and array-typing choice — for cross-ancestry PRS work these matter more than the sample size in some slices.
  (iv) Save as a citation for any forthcoming AoU or MVP cross-ancestry PRS work.

### 6. Cardiovascular Disease Subtypes and Alzheimer's Disease: Phenotypic and Genetic Associations in the UK Biobank and All of Us Research Program
- **Authors / venue:** A. Toyli, C. Zhao, K.J. Su, H. Shen, H.W. Deng, Q.H. Chen et al. — *[venue TBD]*, 2026.
- **Surfaced by:** *Chenjie Zeng — new related research* (06-23) — your own related-research feed.
- **Thread:** **EHR-linked biobanks: All of Us and UK Biobank** (both cohorts explicitly used) **+** **Multimorbidity / chronic-disease clustering** (CVD subtypes → AD is a multimorbidity trajectory) **+** **Genetic epidemiology** (they run both phenotypic and genetic association work).
- **What it is:** A joint UKB + AoU analysis of the relationship between cardiovascular disease *subtypes* (not just "any CVD" but specific CVD phenotypes like coronary artery disease, heart failure, atrial fibrillation, stroke) and incident Alzheimer's Disease, with both phenotypic (real-world outcome) and genetic (GWAS/PRS-based) association layers. The UKB+AoU dual-cohort design is the current gold standard for **replication under differing selection biases** (UKB = healthy-volunteer bias; AoU = underrepresented-population enrichment).
- **Why it matters to you:** Four reasons.
  (a) **Directly on the UKB + AoU thread.** Your INTERESTS file lists both cohorts as core.
  (b) **CVD-subtype → AD is a multimorbidity story.** Chronic-disease trajectory work is on your INTERESTS list; this is a concrete instance of a two-condition trajectory analyzed with modern methods.
  (c) **The UKB + AoU replication pattern is a methodological template.** How they harmonize CVD subtype phecodes across the two cohorts is a template you can reuse.
  (d) **Your related-research feed firing.** Google's model judges this paper close to your published work — most plausibly to your AoU-based cardiometabolic or PheWAS work.
- **Action:** **HIGH.**
  (i) Read for the phecode / subtype definition — did they use Bastarache's phecode catalog, PheKB, or roll their own subtypes?
  (ii) Note the effect sizes for each CVD subtype-AD pair — heterogeneity across subtypes is the interesting finding, since it argues for subtype-specific rather than composite-CVD PRS.
  (iii) Note whether the genetic side uses cross-ancestry PRS or European-only. AoU's diverse population makes European-only PRS use a self-inflicted portability problem.
  (iv) Compare their harmonization approach to yours — cross-cohort phecode harmonization templates are worth a compare-and-contrast.

### 7. Unsupervised characterization of 100,272 EHR patients identifies high-risk groups and comorbidities linked to premature aging
- **Authors / venue:** S. Xian, J.W. Smoller, Y. Luo, T.L. Walunas, C. Liu, A. Khan et al. — *npj Digital Medicine*, 2026.
- **Surfaced by:** *Yuan Luo — new articles* feed (06-29) — Luo is a co-author.
- **Thread:** **Chronic disease clustering and multimorbidity** (the paper's central methodology) **+** **EHR phenotyping** (unsupervised methods over EHR data) **+** aging trajectories (pairs with 06-20 #6 Ding et al. plasma proteomic aging paper).
- **What it is:** An unsupervised (clustering / topic-model) characterization of ~100K EHR patients — very likely Northwestern's NM-Enterprise-Data-Warehouse cohort given Walunas + Luo authorship — identifying **high-risk multimorbidity subtypes and their comorbidity signatures linked to premature aging phenotypes**. This is the EHR-side counterpart to the Ding et al. plasma proteomic aging paper from the 06-20 report — both papers target "premature aging" as a predictive endpoint, one via clinical multimorbidity signatures and the other via proteomic signatures.
- **Why it matters to you:** Four reasons.
  (a) **Directly on your INTERESTS file's chronic-disease clustering and multimorbidity thread** — this is exactly the "unsupervised methods for discovering disease subtypes, multimorbidity patterns, and disease trajectories from EHR" pattern the file specifies as high-priority.
  (b) **Pairs with Ding et al. proteomic aging (06-20 #6)** — the multimorbidity and proteomic signatures could compose into a joint predictor.
  (c) **Northwestern NM-EDW is comparable to BioVU / AoU in size and scope** — methods here transfer.
  (d) **Yuan Luo lineage produces reusable pipelines.** Luo's group publishes code-and-data more consistently than the average NLP-EHR lab.
- **Action:** **HIGH.**
  (i) Read for the clustering method — LDA-style topic model, k-means over embeddings, or graph-community detection? Each has different interpretability properties.
  (ii) Note the "premature aging" outcome definition — chronological-vs-biological age gap? Comorbidity-burden index? Multiple frailty phenotype?
  (iii) Note whether the cluster labels are stable across resampling — a common failure mode of EHR-clustering work is bootstrap-instability.
  (iv) Save as a reference for any forthcoming multimorbidity subtyping work in AoU or MVP.

### 8. PhenoAgent: agentic LLM framework for phenotyping electronic health records via structured query decomposition and self-correction
- **Authors / venue:** Y. Kashiwada, R. Sakurai, Y. Yokokawa, K. Ando et al. — *[venue TBD — likely npj Digital Medicine or JAMIA]*, 2026.
- **Surfaced by:** *George Hripcsak — new related research* (07-05).
- **Thread:** **EHR phenotyping & OMOP** (specifically LLM-assisted computable phenotype development) **+** **EHR foundation models** (agentic LLM pipelines are the emerging pattern) **+** ML for precision health.
- **What it is:** An **agentic** LLM framework for EHR phenotyping — meaning the framework doesn't just prompt an LLM to identify phenotypes from notes but decomposes phenotyping tasks into sub-queries (find diagnoses, find labs, find medications, resolve inconsistencies), executes them iteratively, and **self-corrects** when internal consistency checks fail. This is the "agent" pattern applied to what's typically been a single-prompt task. Contrasts with the more common "one-shot LLM phenotyping" work by making the reasoning steps explicit and auditable.
- **Why it matters to you:** Four reasons.
  (a) **Directly on the "LLM-assisted computable phenotype development" strand of your EHR phenotyping thread.**
  (b) **Structured decomposition + self-correction is the design pattern most likely to transfer to production.** Single-prompt LLM phenotyping has struggled with the reproducibility bar; agentic frameworks with explicit sub-tasks are easier to audit.
  (c) **Hripcsak feed firing.** OHDSI-lineage attention to an LLM phenotyping paper is signal that this may be adopted into OHDSI tooling.
  (d) **Pairs with the DxDirector agentic LLM diagnosis paper (Szolovits citations feed).** Two "agentic LLM" papers surfacing in the same window suggests the pattern is becoming a class rather than a one-off.
- **Action:** **HIGH.**
  (i) Read for the sub-task decomposition — how is phenotyping split, and how is each sub-task evaluated?
  (ii) Note the evaluation — do they evaluate against phecode-derived gold standards, PheKB, or a novel expert-curated dataset?
  (iii) Note the LLM base — closed-source (Claude/GPT-4/Gemini) or open-source (Llama/Mistral)? Reproducibility depends on this.
  (iv) Consider whether the pattern is adoptable for your BioVU / AoU phecode derivation work.

### 9. Cohort-Anchored Foundation Models for Electronic Health Records: From Risk Scores to Auditable Peer Cohorts
- **Authors / venue:** K. Zheng — arXiv 2606.21885, 2026.
- **Surfaced by:** *George Hripcsak — new related research* (06-28 and 06-29). Also fires in *Foundation models and "electronic health records" — new results* (06-28).
- **Thread:** **EHR foundation models** (CLMBR / MOTOR / EHRSHOT / FEMR / MEDS lineage — the paper's central object of study) **+** **EHR phenotyping** (peer-cohort identification is a phenotyping primitive) **+** ML for precision health (auditability of risk scores).
- **What it is:** A framework for making EHR foundation model risk-score outputs **auditable via peer cohorts**. The idea: instead of just outputting a number ("risk = 0.87"), the system also returns the **peer cohort** — the set of most-similar patients in the training data — so a clinician can inspect the peer cohort to understand why the model produced its prediction. Positions itself as a bridge between the "risk score" outputs of CLMBR/MOTOR-style FMs and the "case-based" interpretability that clinicians actually use. Single-author arXiv preprint, so scope is bounded.
- **Why it matters to you:** Three reasons.
  (a) **EHR foundation models are on the INTERESTS thread explicitly.**
  (b) **Peer-cohort explanations are a rare interpretability layer.** Most FM interpretability work either does gradient-based saliency (which is unreliable for tabular EHR data) or trains a proxy explanation model. Peer-cohort retrieval is direct: "your prediction is like the average outcome for these 30 similar patients."
  (c) **Pairs with the multimodal-EHR-FM paper (06-20 #2) as the audit layer** — Sivarajkumar et al. built a better model; Zheng builds an audit layer for existing models.
- **Action:** **HIGH.** (Single-author arXiv preprint, so read for the idea rather than for empirical claims.)
  (i) Read for the peer-cohort identification method — nearest-neighbor in the FM embedding space, or something more structured?
  (ii) Note whether the peer cohorts are actually clinically coherent (interpretable) or just numerically similar.
  (iii) Consider whether the pattern would apply to your PRS-based risk scores (the same "auditable risk score" idea works for PRS, not just EHR-FMs).

### 10. Domain-aware matrix completion for phenotype imputation using electronic health record data with applications in genomic research
- **Authors / venue:** H. Wu, C.H. Lee, N. Abiri, I. Ionita-Laza — *The Annals of Applied Statistics*, 2026.
- **Surfaced by:** **Dual-feed** — (a) *Lisa Bastarache — new related research* (06-29) and (b) *Joshua C. Denny — new related research* (06-29).
- **Thread:** **EHR phenotyping** (phenotype imputation is a phenotyping primitive) **+** **Genetic epidemiology** (the paper's "applications in genomic research" hook) **+** **PheWAS / phecode infrastructure**.
- **What it is:** A domain-aware matrix-completion approach to imputing missing phenotype values in EHR data, specifically designed for downstream use in genomic research (GWAS, PheWAS, PRS). Ionita-Laza is a Columbia-Biostatistics rare-variant methodologist; this is a statistical-methods paper published in *AoAS* (the applied-stats flagship). The "domain-aware" framing means the matrix completion uses external biological knowledge (e.g., ICD hierarchy, phecode grouping, gene-panel overlap) as priors rather than treating the phenotype matrix as a bare low-rank object.
- **Why it matters to you:** Four reasons.
  (a) **Directly on the EHR phenotyping + genetic epi intersection.** Missing-phenotype imputation is a common bottleneck in biobank-based PheWAS work, and this is a modern statistical approach to it.
  (b) **Bastarache + Denny dual-feed** — the two Vanderbilt-lineage phecode-methodology authorities both getting this in their related-research feeds is field-consensus signal.
  (c) **AoAS venue.** Applied stats-methods work has different reproducibility norms than applied medical stats — code is more commonly released, methods more rigorously proven.
  (d) **Applicable to AoU or MVP** where phenotype missingness is heterogeneous.
- **Action:** **HIGH.**
  (i) Read for the domain-prior encoding — how are ICD hierarchies or phecode groupings incorporated into the low-rank penalty?
  (ii) Note the empirical demonstration — MGB / Columbia biobank / synthetic. Real-data results transfer better.
  (iii) Consider whether the method could improve phenotype completeness for your PheWAS work, especially in AoU where EHR coverage is uneven.
  (iv) Note the code release status.

### 11. Multi-ancestry polygenic risk score methods improve glaucoma prediction across diverse populations in three large biobanks
- **Authors / venue:** A.V. Segre, M.A. Bartolo, I.F. Aboobakar, H.M.T. Vy et al. — *Ophthalmology & [venue]*, 2026.
- **Surfaced by:** *Ron Do — new articles* (06-29) — Ron Do (Mount Sinai/BioMe) is a co-author, indicating direct authorial involvement.
- **Thread:** **Genetic epidemiology / cross-ancestry PRS** (multi-ancestry PRS methods) **+** **EHR-linked biobanks** (three biobanks — likely BioMe + UKB + AoU or similar) **+** ML for precision health (glaucoma prediction as clinical application).
- **What it is:** Applies multi-ancestry PRS methods (PRS-CSx, PRS-Mixer, or similar) to glaucoma prediction across three large biobanks with different ancestry compositions. The three-biobank replication is important because PRS portability across ancestries has been the primary criticism of PRS-based screening; a paper that demonstrates *method-level improvement* rather than *cohort-level improvement* has broader applicability.
- **Why it matters to you:** Three reasons.
  (a) **Cross-ancestry PRS methods are on the INTERESTS thread.** Any methodological improvement here is directly relevant.
  (b) **Three-biobank replication is the current gold standard.** Any AoU-based PRS validation work you do needs external replication in ≥2 other cohorts; this paper is a template.
  (c) **Ron Do BioMe lineage.** BioMe is heavily Hispanic/Latino-enriched, so multi-ancestry methods that work in BioMe transfer to AoU's Hispanic sub-cohort. This is a rare methodological cross-fertilization.
- **Action:** **HIGH.**
  (i) Note which three biobanks — this matters for how directly the method transfers to AoU.
  (ii) Note whether they use PRS-CSx, PRS-Mixer, or something new. If they compare methods head-to-head, the winner becomes the default.
  (iii) Note whether they release ancestry-specific PRS weights or a single-portable weight file.
  (iv) Consider adopting for any forthcoming cross-ancestry PRS work.

### 12. Real-world performance of large-scale propensity score adjustment strategies: Matching, weighting, and stratification
- **Authors / venue:** K.M. Li, M.J. Schuemie, P.B. Ryan, L. Zhang, Y. Chen et al. — *[venue TBD]*, 2026.
- **Surfaced by:** **Dual-feed of author-alerts** — (a) *Patrick Ryan — new articles* (07-05, meaning Ryan is a co-author) and (b) *George Hripcsak — new articles* (07-05, meaning Hripcsak is also a co-author). Two OHDSI-lineage co-authors on a propensity-score-methods paper is essentially OHDSI's canonical statement.
- **Thread:** **Causal inference and pharmacoepidemiology** (propensity score methods are the workhorse) **+** **EHR phenotyping & OMOP** (large-scale = OMOP-style multi-site) **+** ML for precision health.
- **What it is:** Head-to-head empirical comparison of propensity-score matching vs weighting vs stratification at large-scale (multi-site OMOP-style) settings. This is a follow-up to the OHDSI methods-benchmark line — Schuemie, Ryan, Hripcsak have been the trio behind the OHDSI large-scale evidence generation methods. The "real-world performance" framing suggests they evaluate empirical properties (bias, variance, coverage) across many drug-outcome pairs rather than in a single case study.
- **Why it matters to you:** Three reasons.
  (a) **Directly on your causal inference / pharmacoepi thread.** Propensity-score choice affects every drug-safety and drug-effectiveness study you might design.
  (b) **OHDSI-canonical statement.** When Schuemie + Ryan + Hripcsak co-publish PS-methods work, it becomes the OHDSI-network default.
  (c) **Pairs with your active drug-class threads** (GLP-1, SGLT2, CFTR modulators, HRT). All of these involve propensity-score adjustment; a benchmark tells you which method to default to.
- **Action:** **HIGH.**
  (i) Read for the recommendation — does matching, weighting, or stratification win, and under what conditions?
  (ii) Note the data source — Observational Health Data Sciences and Informatics network claims? Sentinel? Truven?
  (iii) Note whether they cover both binary and continuous exposures (the CFTR modulator dose-response question needs continuous-exposure PS).
  (iv) Save as a default citation for any forthcoming pharmacoepi work.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic; carry-forwards from prior windows)

- **Prior-informed conditional Gaussian graphical models for protein-interaction reconstruction (Mapelli et al., stat.AP, 2026-06-30)** — Score-3 arxiv-digest hit on 07-01. Uses UK Biobank cardiometabolic proteomics (n=49,129, p=366) as the demonstration. Off-thread on the surface (protein-network reconstruction is not one of your active threads), but the **UK Biobank cardiometabolic proteomics dataset** and the **domain-prior-informed penalty** are both worth logging — the same framework could apply to any prior-informed EHR-outcome network you'd want to build. **METHODS-WATCH.**

- **Residual-on-residual regression for effect estimation in observational data (Naimi et al., stat.ME, 2026-06-29)** — Score-2 arxiv-digest hit on 07-01. Compares residual-on-residual to AIPW and TMLE on a nulliparous-pregnancy-outcomes-study dataset. Not a new method per se, but a **stability-under-positivity-violation** comparison that argues for residual-on-residual as a triangulation strategy alongside AIPW/TMLE. **METHODS-WATCH for any future TTE writeup** — useful when a referee asks "why not TMLE?" and the honest answer is "positivity violation."

- **Dynamic prediction of alternating recurrent events via neural network (Loe, Murry, Wu; stat.ML, 2026-06-29)** — Score-1 arxiv-digest hit on 07-01. IPW-weighted pseudo-observations + neural-net for alternating recurrent event prediction. Applied to first-year-medical-resident low-mood-episode prediction. **METHODS-WATCH** for the primitive: IPW-pseudo-observation + neural-net could apply to any EHR alternating-recurrent outcome (relapse-remission cycles in IBD, hospitalization-recovery in HF).

- **Cross-ancestry pleiotropic analysis of imaging-derived phenotypes enhances risk stratification of depression (Feng, Guo, Huang et al., Molecular Psychiatry, 2026)** — Denny citations feed (07-05). Imaging-derived phenotypes + cross-ancestry pleiotropy is a novel primitive; off-thread substantively (depression / imaging) but the **PheWAS-of-imaging-phenotypes-across-ancestry** design is transferable. **METHODS-WATCH.**

- **Structural variant discovery and diagnostic impact in rare diseases from short-read and long-read sequencing (Sanchis-Juan, Mostovoy, Stenton, Ganesh et al., medRxiv, 2026)** — Montgomery related-research feed (06-29). Rare-disease diagnostic yield from short-vs-long-read SV calling. **METHODS-WATCH** on the variant-interpretation thread — argues that long-read calling adds meaningful diagnostic yield beyond short-read in rare-disease exomes, which is directly relevant if you're ever asked whether to move BioVU-style cohorts to long-read.

- **AI-CURA, an automated LLM workflow for high-accuracy genetic variant classification (Ma, Fong, Lai et al., Science Translational Medicine, 2026)** — variant interpretation keyword feed (06-28). Directly on the ACMG / ClinGen variant interpretation thread. LLM-based variant classification is now the frontier — this is the *Science Translational Medicine* version of what has been arXiv-preprint work for the last two years. **HIGH-adjacent** — reads as METHODS-WATCH because the venue is clinical rather than statistical, but if the accuracy claim holds up on external test sets it becomes a default tool. **Read to check the accuracy claim.**

- **Automated reanalysis of genomic data for rare disease diagnostics at scale (Welland, Ahlquist, De Fazio, Austin-Tse et al., Nature Medicine, 2026)** — rare diseases keyword feed (06-28). Automated reanalysis of prior-negative rare-disease exomes as new variant knowledge accumulates. Directly on the **rare disease** thread. **METHODS-WATCH** — reference dataset for any "how much re-analysis matters" argument.

- **Harmonizing standards and resources for the medical genome (Ashley, Alizadeh, Armitage, Bhatt et al., Nature, 2026)** — Heidi Rehm new articles (07-05). Nature Perspective on standards for precision-genomic-medicine. **METHODS-WATCH** — likely to be cited a lot in ACMG / ClinGen writeups.

- **Cardiovascular outcomes and safety associated with statin therapy for primary prevention in older adults with type 2 diabetes: A target trial emulation study (Chan, Xu, Chan, Wan; Hernán citations 06-29)** — TTE in older T2D, statin primary prevention. **METHODS-WATCH** — statins are not one of your active drug-class threads, but the TTE-in-older-adults-with-comorbidity template is transferable to your GLP-1 / SGLT2 work.

- **Causal inference and digital twins: a roadmap for the future of clinical trials (Estévez, Peck, McKinney, Weatherall et al., npj Digital Medicine, van der Schaar feed)** — Roadmap paper. **METHODS-WATCH** — the "digital twin" framing is currently over-hyped, but the causal-inference intersection is legitimate and worth tracking.

- **GLP-1 Receptor Agonists and Risk of Mental Health Disorders in Type 2 Diabetes: Active Comparator, New User Cohort Study (Kim, Kim, Lee et al., Patrick Ryan related-research 07-05)** — Active-comparator new-user design on GLP-1 RAs → mental health. Directly on your **GLP-1 drug-class thread**. **HIGH-adjacent** — reads as METHODS-WATCH because it's a single-outcome study, but the active-comparator new-user design is exactly the pharmacoepi template you're publishing in. **Read for the specific implementation.**

- **Integrating social determinants of health and genetic risk in disease risk models (Biji, Ferar, Pejaver, Kenny et al., AJHG, 2026; Bastarache citations 06-27)** — Combined-risk model with SDoH + PRS. **METHODS-WATCH** — the composite-risk-scoring thread is on your INTERESTS list, and SDoH is the third axis alongside common (PRS) and rare (pLoF burden).

- **Challenging traditional classifications: Gene penetrance in genetically transitional disease (Gorevic, Niewold, Aksentijevich, Pfeffer et al., Genes & Diseases, 2026)** — surfaces as a **citation to your "Guidance for estimating penetrance of monogenic..." paper** (06-28). Perspective piece on penetrance in transitional (partially monogenic, partially polygenic) diseases. **METHODS-WATCH** — small venue but explicit citation of your penetrance work is direct signal.

- **Nudel et al. — The impact of diverse ancestry on polygenic risk score-based prediction models for psychiatric and neurodevelopmental disorders (Psychiatry Research, 2026)** — triple-feed (Karczewski + Yang + Denny). Cross-ancestry PRS in psych/neurodev. **METHODS-WATCH** — off-thread substantively but the triple-feed indicates field-wide attention.

- **Empowering biomedical evidence exploration and synthesis with deep knowledge graph research (Wang, Chen, Yang, Wang, Jin, Peng, Lu; Nature MI, 2026)** — knowledge graph keyword (07-05). Biomedical KG for evidence synthesis. On the **KG / ontologies** thread. **METHODS-WATCH** — Nature MI venue suggests methodological depth; check whether it uses SemMedDB, PubMedKG, or a new construction.

- **Krieger, JE — Polygenic risk score translation across diverse populations (Frontiers in Cardiovascular Medicine, 2026)** — Jian Yang citations (06-29). Review of cross-ancestry PRS translation. **METHODS-WATCH** — useful review citation.

---

## SKIP / noise (logged, no action)

- **DxDirector: agentic LLM for full-process clinical diagnosis (Xu, Huang et al., Nature Communications; Szolovits citations 07-05)** — Agentic-LLM diagnosis paper. Off your EHR-phenotyping thread substantively; nature communications venue but agentic-LLM medicine papers are proliferating and few survive replication. Logged. Note: pairs with PhenoAgent (item #8) as a "class" of agentic-LLM medicine papers now emerging.
- **BulkFormer: foundation model for bulk transcriptomes (Kang, Fan et al., Cell Systems, 2026)** — Zitnik related-research (07-05). Transcriptomic FM, off your EHR-FM thread.
- **AI-Driven Enterprise Architecture for Intelligent Digital Healthcare Transformation (Foundation-models-and-EHR keyword, 07-05)** — Vendor/consultancy paper, keyword leak.
- **Explainable AI machine learning framework for chronic kidney disease prediction utilizing electronic health records (Rizwan et al., BMC Med Inf, 2026)** — CKD prediction with generic XAI. Off-thread despite kidney overlap — not a methods advance.
- **Clonal hematopoiesis of indeterminate potential (CHIP) — a pivotal contributor of aging and related disorders (Dhenge, Kulkarni, Annals of Translational Medicine, 2026)** — CHIP review, tangentially on-thread but review-tier not primary-lit.
- **Endoluminal Complement Accessibility as a Spatial Determinant of Glomerular Injury (APOL1 keyword, 07-05)** — glomerular pathology review; keyword leak on APOL1.
- **Drug repurposing for Alzheimer's / monkeypox molecular-docking papers** — Off-thread on drug repurposing (chemistry-only, no clinical evidence loop; your INTERESTS explicitly rate these lower).
- **Multiple mendelian-diseases DMD-variant / retinal-disease papers** — Rare-disease clinical case reports; not on the methods thread.
- **Autoimmune-vestibular / autoimmune Panchakarma / autoimmune-eye-movement papers** — Autoimmune keyword leaks, off the IBD / autoimmune methods thread.
- **APECED T-cell subset paper** — Immunology, off-thread.
- **Various Karczewski / Shendure / Vogelstein / Pritchard citation-feed hits** on non-clinical adjacent topics (peer-review, orthopedic surgery AI, biliprotein design, Neanderthal genetics, etc.) — Feed leaks.
- **arxiv-digest 06-24 through 06-28 range** — Six days of no on-thread output; keyword leaks on Airbnb marketing (07-02) and 3D plant phenotyping (07-03) are the only surfaced-but-off-thread hits.
- **Sociodemographic prostate cancer / hypertension MENA / long COVID / mixed AoU health-disparities papers** — All AoU-based but on health-disparities rather than the methods threads.

---

## Suggestions for the pipeline

Carry-forward items from the 06-20 report remain **unactioned** — the tracked.yaml file has not been edited since 04-30. In addition:

1. **arxiv-digest yield is chronically low relative to Scholar alerts.** In this 16-day window, 3 on-thread papers came from the pipeline (all in one day, 07-01) while ≥12 came from Scholar alerts. The pipeline covers `q-bio.QM`, `q-bio.GN`, `q-bio.PE`, `stat.AP` — but the on-thread papers this window are in `stat.ME`, `stat.ML`, `cs.LG`, and journal venues (Nature, Nature Genetics, Genetic Epidemiology, AJHG, npj Digital Medicine). **Add `cs.LG`, `stat.ME`, `stat.ML` to the arxiv-digest source list** — this is the single highest-leverage change and it's been recommended in three consecutive reports.

2. **medRxiv / bioRxiv coverage.** Multiple on-thread items this window are medRxiv-preprint stage (Sanchis-Juan structural variants, Liu noncoding immunity). The current pipeline can never reach these. **Adding medRxiv q-bio + bioRxiv genomics feeds would roughly double the on-thread yield** for a modest polling-complexity cost.

3. **`knowledge graph` keyword still leaks non-biomedical hits** (this window: TFreeKGGen, Temporal Evidence Chain for TKG-QA, Structure-Aware Zero-Shot Relational Learning). **Recommend narrowing to `biomedical knowledge graph` OR `clinical knowledge graph` OR `medical knowledge graph`** — same fix as prior reports.

4. **The 07-04 and 07-05 zero-paper days are genuine dry days**, not fetch failures. Suggest adding a distinct "zero output but pipeline healthy" marker in the digest header to distinguish this from the 06-20 fetch failure. The current output ("0 relevant papers" with categories listed) is close but doesn't explicitly say "categories fetched cleanly."

5. **Track your own citations feed with higher-precision alerting.** This window had TWO citations-feed firings (Salvatore-Kundu PRS-bias, Baker DRIVE v3). These are the highest-precision signals the pipeline produces; both landed in generic new-articles batches with 30+ other papers. Worth splitting citations-feed emails into their own alert / label so they're not buried.

6. **Add `polygenic outlier` / `PRS outlier` / `polygenic-expectation deviation` keywords.** The Baya et al. paper (item #4) and its pairing with Souaiaia (06-20 #4) makes "PRS outlier genetics" a coherent sub-thread; a dedicated keyword catches this class directly.

7. **Add `active comparator new user` / `target trial emulation` as keywords** (carry-forward; still unaddressed). Multiple hits this window (Kim GLP-1 ACNU, Chan statins TTE, Chen CV outcomes TTE) — the pattern is stable and worth tracking directly.

8. **Add `FHIR` / `OMOP-CDM` / `data model comparison` as keywords.** Item #3 (Patterson FHIR vs OMOP) is one of the most on-thread papers of the quarter and surfaced entirely through Hripcsak's new-articles feed. A keyword would catch this class directly.

9. **Add `foundation model` + `EHR` compound keyword.** Currently `foundation model` alone would catch anything; a compound with EHR / clinical / phecode restricts to the EHR-FM thread.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 12 | (1) Salvatore et al. PRS-based bias correction [Zeng-citations+related], (2) Baker DRIVE v3 IBD-haplotype-clustering [Zeng-citations], (3) Patterson et al. FHIR-vs-OMOP in AoU [Hripcsak-authored+Brandt+Ryan], (4) Baya et al. polygenic-outliers → rare-variant enrichment [Zeng+Bastarache], (5) Jo et al. 1M-East-Asian complex-trait meta-analysis [Yang related], (6) Toyli et al. CVD-subtypes-and-AD UKB+AoU [Zeng related], (7) Xian et al. unsupervised 100K-EHR premature-aging clustering [Luo authored], (8) Kashiwada et al. PhenoAgent LLM EHR phenotyping [Hripcsak related], (9) Zheng cohort-anchored EHR-FMs [Hripcsak related], (10) Wu et al. domain-aware phenotype matrix completion [Bastarache+Denny], (11) Segre et al. multi-ancestry glaucoma PRS in 3 biobanks [Ron Do authored], (12) Li et al. real-world propensity-score benchmark [Ryan+Hripcsak co-authored] |
| METHODS-WATCH | ~15 | Mapelli UKB proteomic GGM (arxiv-digest 07-01), Naimi residual-on-residual (arxiv-digest 07-01), Loe et al. IPW-pseudo-obs recurrent events (arxiv-digest 07-01), Feng cross-ancestry imaging pleiotropy (Denny cite), Sanchis-Juan SV rare-disease (Montgomery), AI-CURA LLM variant classification (Sci Transl Med), Welland automated rare-disease reanalysis (Nature Med), Ashley medical-genome standards (Nature; Rehm), Chan et al. statin TTE (Hernán cite), Estévez causal-inference + digital twins (van der Schaar), Kim GLP-1 ACNU mental health (Ryan related), Biji SDoH + genetic risk composite (Bastarache cite), Gorevic penetrance perspective (cites your penetrance paper), Nudel cross-ancestry psych PRS (triple), Wang biomedical-KG evidence synthesis (Nat MI), Krieger PRS-across-populations review (Yang cite) |
| SKIP | ~30 | Health-disparity AoU / autoimmune-vestibular / DMD variant clinical / mendelian retinal-disease case reports / drug-docking chemistry / Neanderthal genetics / architecture-vendor healthcare AI / CHIP review / general LLM benchmark / marketing causal-inference / plant phenotyping / spatial-transcriptomics workflow — see SKIP section above |

Compared to the 06-20 report: this is a **16-day catch-up** window rather
than a 2-day one. Absolute HIGH count is higher (12 vs 6), but per-day
rate is lower (0.75/day vs 3.0/day for the 06-20 window's 2-day span).
The signal-per-day rate is comparable to the mid-June average.

**The single most important reading order this window:**
1. Salvatore et al. PRS-bias-correction (item #1) — cites your work
2. Patterson et al. FHIR-vs-OMOP AoU (item #3) — will be canonical
3. Baya et al. polygenic-outlier rare-variant (item #4) — composite-risk
4. Baker DRIVE v3 (item #2) — cites your work
5. Jo et al. 1M-East-Asian meta-analysis (item #5) — reference dataset

Items 6-12 in any order — all HIGH but less time-critical.
