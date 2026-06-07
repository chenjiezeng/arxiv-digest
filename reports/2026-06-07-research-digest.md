# Research digest report — 2026-06-07

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-06-02 → 2026-06-07** (since the prior 2026-06-01 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-06 06:51 + 12:24 UTC | Two batches: citation/author alerts (06:51 UTC) and keyword alerts (12:24 UTC). |
| NCBI PubMed "What's new" alerts | 2026-06-05 → 06-06 | Three searches: "UK Biobank" (9 items), "All of Us" (1), "drug repurposing" (9). |
| `arxiv-digest` repo (`digests/`) | 2026-06-02 → 06-07 | 06-02, 06-03, 06-07 empty; 05-31 & 06-03 logged 3/4 q-bio category fetch failures (issue persists). 06-06 returned 2 papers — both included below. |
| bioRxiv / medRxiv subject alerts | daily | Aggregate collection digests, not individually triaged. |

> ⚠️ The `arxiv-digest` GitHub pipeline produced **2 papers in 6 days**
> (both on 06-06). 06-02, 06-03, and 06-07 were empty; 06-03 again logged
> "3/4 categories failed to fetch" (q-bio.QM, q-bio.GN, q-bio.PE) — same
> failure mode flagged the past two reports. The q-bio fetch is now
> chronically broken; ranking against a pipeline this thin is misleading.
> See pipeline suggestions at the end.

> Caveat: Scholar alert emails contain title, authors, venue, and the first
> ~2–3 lines of each abstract only. PubMed alerts return title/authors/
> citation, no abstract. The reports below contextualize that metadata
> against your research threads; nothing here reflects full-text reading.

---

## Executive summary

- **The standout paper of the window is PiMInfer** (Wang et al., medRxiv,
  via the Lisa Bastarache citation alert): a *phenotype-to-mechanism*
  framework that runs phenome-wide comorbidity → biomedical KG →
  molecular-mechanism nominations → therapeutic discovery. This sits at
  the intersection of **three** of your active threads — PheWAS/PheRS,
  biomedical knowledge graphs, and drug repurposing with explainable
  rationale — and it cites Bastarache's phecodeX paper. Highest single
  read of the window.
- **AoU TKR-trajectory clustering with uncertainty (TASC)** — Yan,
  Cudjoe, Taylor, *BioData Mining* — uses 2,052 AoU primary total-knee-
  replacement patients to build time-aware sequence clusters with
  uncertainty quantification. Direct hit on your multimorbidity /
  disease-trajectory thread, anchored in AoU.
- **PSA + PRS prostate cancer (Lu et al., medRxiv)** — UK Biobank,
  GRS269 + PSA composite scoring. Adjacent to your own AoU prostate-
  cancer / HT-ADT line of work, and on-thread for composite risk
  (PRS-stacked-with-clinical) reasoning.
- **GLP-1 ML in AoU (Abegaz & Frietze, *Frontiers in AI*)** — ML
  prediction of glycemic-control and weight-loss outcomes in AoU GLP-1
  initiators. Pharmacoepi/AoU/ML for precision health triple-hit, though
  framing is predictive rather than causal.
- **Selection-bias upper bound (Liu, Wang, Altman, arXiv 2606.00563)** —
  practical bound on selection-bias effects in medical prediction
  models; cites the AoU program paper. Methods piece directly relevant
  to your external-validation-across-sites/ancestries interest.
- **arxiv-digest 06-06 — 2 papers**: Shen, Fu, Lin (causal inference for
  treatment switching in oncology RCTs with synthetic-control + balancing
  weights) and Bodrug-Schepers et al. (federated SPARQL for variant
  annotation; biomedical KG). Both genuinely on-thread.
- **Rare-disease ASO therapy at the ultra-rare end** — Crooke, Glass,
  Gleeson, Mignon, Chung et al. (*Nucleic Acids Research*), the n-Lorem
  experience for "nano-rare" (<30 patients worldwide) variants.

Counts: **9 HIGH**, **6 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. A phenotype-to-mechanism framework links phenome-wide comorbidity architecture to molecular mechanisms and therapeutic discovery in complex diseases (PiMInfer)
- **Authors / venue:** W.T. Wang, M. Zhou, J. Tong, M.J. Lin, A. Ke, M. Wei, Z. Xu, et al. — *medRxiv*, 2026 (preprint, link: medrxiv.org/content/10.64898/2026.05.13.26353128).
- **Surfaced by:** Lisa Bastarache "4 new citations" alert (cites the phecodeX paper).
- **Thread:** **PheWAS / PheRS infrastructure** **+** **Knowledge graphs & ontologies** **+** **Drug repurposing** **+** chronic-disease multimorbidity.
- **What it is:** PiMInfer is a phenotype-to-mechanism inference framework. Snippet describes the pipeline as: deep phenotypic characterization from real-world clinical data → biomedical KG traversal → mechanistic nominations for clinically heterogeneous complex diseases → therapeutic-target suggestions. Cites Bastarache's *phecodeX* paper, so the phenotype side is almost certainly phecode-anchored.
- **Why it matters to you:** This is arguably the highest-leverage paper of the window for your interests. It chains together three of your active threads in one framework:
  1. **PheWAS/PheRS** — phenome-wide comorbidity architecture is the input modality;
  2. **Biomedical KGs** — knowledge graph is the reasoning substrate, which directly addresses your INTERESTS preference for "knowledge-graph / GNN approaches with *explainable* hypothesis output (path or subgraph rationales rather than opaque link-prediction scores)";
  3. **Drug repurposing** — explicit therapeutic-discovery output, with phenome-wide comorbidity as the clinical-evidence loop (exactly the angle your INTERESTS flag as high-priority vs. "target-only or chemistry-only pipelines without a clinical-evidence loop").
- The Bastarache citation suggests phecode/phecodeX is the phenotype backbone — i.e., this is the closest paper yet to the project shape "PheRS + biomedical KG → repurposing hypothesis." Read carefully for the KG schema (which ontologies — HPO? MONDO? UMLS?), the path-extraction method (random walks? GNN attention?), and how mechanistic "support" is scored.
- **Action:** **HIGH — read first this week.** Likely the most directly on-thread paper since the G6PD PheRS paper (2026-06-01 report #13). Probable cite for your own PheRS-stacked-with-KG-repurposing work; also worth checking authorship for collaborators.

### 2. TASC: a time-aware sequence clustering framework with uncertainty quantification for electronic health record trajectories
- **Authors / venue:** A.Y. Yan, T.K.M. Cudjoe, C.O. Taylor — *BioData Mining*, 2026.
- **Surfaced by:** "All of Us research program" keyword alert (top result, marked most relevant).
- **Thread:** **Chronic disease clustering / multimorbidity** **+** **EHR phenotyping** **+** **All of Us biobank** **+** ML for precision health.
- **What it is:** Time-aware sequence clustering for EHR trajectories with explicit uncertainty quantification. Proof-of-concept on 2,052 AoU patients undergoing primary total knee replacement (TKR), using both EHR codes and survey data to construct temporally-ordered patient trajectories.
- **Why it matters to you:** Three things stand out:
  1. **Time-aware sequence clustering** is exactly the methodological shape your INTERESTS flag under multimorbidity ("trajectory clustering ... topic models on diagnosis sequences"). Most EHR trajectory work is either time-agnostic (LDA-on-codes) or time-binned but uncertainty-free; TASC's uncertainty quantification is a methodological upgrade.
  2. **AoU is the cohort vehicle** — directly portable to your AoU work, and the use of both EHR + survey data mirrors AoU's dual data streams.
  3. **TKR is a procedure-anchored phenotype**, similar to the surgical-anchored cohorts you build for HT/ADT and CFTR work. The trajectory-extraction protocol may be transferable to your prostate-cancer/HT trajectory work.
- The TKR clinical question (n=2,052) is small but the *method* is the deliverable. Read for: how time-awareness is encoded (continuous-time RNN? Hawkes process? attention-based?), how uncertainty is propagated to cluster assignments (deep-ensembles? Dirichlet processes?), and whether the cluster labels remain stable under re-sampling — the most common failure mode in this literature.
- **Action:** **HIGH — read for the trajectory-extraction protocol and uncertainty propagation.** Strongest AoU-anchored multimorbidity methods paper of the window.

### 3. Improved prostate cancer prediction by combining Prostate-Specific Antigen (PSA) test results with Genetic Risk Scores (GRS/PRS)
- **Authors / venue:** J. Lu, G. Chen, S.W.D. Merriel, M.N. Weedon, A. Murray et al. — *medRxiv*, 2026 (preprint).
- **Surfaced by:** Joshua C. Denny "10 new citations" alert (cites the AoU program paper).
- **Thread:** **Genetic epidemiology** (PRS) **+** **EHR-linked biobanks** (UK Biobank) **+** **composite risk modeling**, adjacent to your own prostate-cancer/AoU work.
- **What it is:** GRS269 (269-variant prostate-cancer PRS) derived and applied to UK Biobank participants. The paper evaluates whether GRS269 improves prostate-cancer prediction *on top of* PSA — a clinically standard biomarker with well-known high false-positive rate (~80%).
- **Why it matters to you:** Composite risk (PRS + biomarker + clinical) is one of your stated genetic-epi interests, and prostate-cancer specifically overlaps with the AoU prostate-HT abstract you co-authored (last report's #3). Key question this paper should answer: does adding PRS to PSA improve net reclassification *at clinically actionable thresholds*, or only at the population level? The 80% false-positive PSA framing is well-trodden — what's new here is the GRS269 calibration vs. earlier 100–200-variant PRSes. Also worth comparing to AoU prostate PRS performance in non-European ancestries, given UKB is overwhelmingly EUR.
- Caveat: medRxiv preprint, so the score may shift on peer review. Also a stand-alone PSA+PRS composite (without MRI / mpMRI inclusion) is increasingly considered out-of-date in screening literature; check whether they benchmark vs. PCPT/PBCG calculators.
- **Action:** **HIGH** — read for the calibration / decision-curve analysis and for cross-validation strategy. Useful background for any AoU/MVP prostate-cancer composite-risk drafting.

### 4. Machine Learning Algorithms for Predicting Glycemic Control and Weight Loss Outcomes in GLP-1 Receptor Agonist Users
- **Authors / venue:** T.M. Abegaz, G. Frietze — *Frontiers in Artificial Intelligence*, 2026.
- **Surfaced by:** "All of Us research program" keyword alert.
- **Thread:** **Pharmacoepidemiology (GLP-1 drug-class)** **+** **All of Us biobank** **+** **ML for precision health** (treatment-effect heterogeneity).
- **What it is:** Retrospective cohort study in AoU GLP-1 RA initiators with baseline + follow-up measurements; two cohorts (glycemic and weight) for ML prediction of treatment response.
- **Why it matters to you:** Directly extends the GLP-1/AoU line from last week's #1 (Chung et al., AJG, liver outcomes). Where Chung et al. was a hard-clinical-outcome paper (incident liver events), this one is treatment-effect *prediction* — closer to your INTERESTS phrasing "individualized risk prediction, treatment-effect heterogeneity." Important methodological flag: this is *predictive*, not *causal* — the lack of an active comparator (e.g. DPP-4i or SU initiators) and lack of treatment-effect estimands (CATE, T-learner, etc.) means it shouldn't be over-interpreted as "what would happen if we randomized." Useful if you're building a GLP-1 HTE pipeline; risky if you're citing it as evidence of effect.
- **Action:** **HIGH** — read for the AoU cohort construction (initiator definition, washout, censoring) and the feature set; flag the predictive-vs-causal framing in any citation.

### 5. A Practical Upper Bound on Selection Bias Effects in Medical Prediction Models
- **Authors / venue:** K. Liu, M. Wang, R.B. Altman — arXiv:2606.00563, 2026.
- **Surfaced by:** Joshua C. Denny "10 new citations" alert (cites the AoU program paper).
- **Thread:** **ML for precision health** (calibration, external validation) **+** **EHR-linked biobanks** **+** causal inference (selection bias).
- **What it is:** Practical (computable, deployment-time) upper bound on the effect of selection bias on model generalizability when models trained on biased data are deployed in a broader target population. Altman group at Stanford; likely a bound based on density-ratio or covariate-shift quantification rather than worst-case.
- **Why it matters to you:** Selection bias is the recurring methodological worry across AoU (volunteer cohort, overrepresentation of certain groups), UKB (healthy-volunteer bias), and any EHR-derived cohort. A *computable upper bound* is more useful than the usual narrative caveat — gives a number you can put on the limitations section of a clinical prediction model. Pairs naturally with the prior report's #14 Lancet Digital Health fairness scoping review.
- **Action:** **HIGH (methods)** — read for the bound construction (is it KL-based? Wasserstein? worst-case over a class?) and whether they validate it empirically on AoU/UKB.

### 6. arxiv-digest 06-06: Leveraging External Controls for Treatment Switching in Randomized Controlled Trials — A Weighted Causal Inference Framework for Overall Survival
- **Authors / venue:** A.A. Shen, C. Fu, R. Lin — arXiv:2606.06441v1, primary category stat.ME. (2026-06-04 submission).
- **Surfaced by:** `arxiv-digest` 2026-06-06 (keyword: "causal inference"). One of only two papers the pipeline returned all week.
- **Thread:** **Causal inference and pharmacoepidemiology** (treatment switching, weighting, synthetic controls).
- **What it is:** Oncology-RCT framework combining synthetic-control methods with observational-causal balancing weights to handle treatment switching (i.e., crossover from control to experimental arm at progression — which violates RCT randomization for overall survival). Uses multiple imputation + time-varying weights and proposes risk-set selection strategies for external-control imputation.
- **Why it matters to you:** Treatment switching is a recurring pharmacoepi problem (cancer trials, GLP-1 add-ons after baseline therapy, CFTR modulator initiation in already-symptomatic patients). The combination of *external controls* + *time-varying weights* is methodologically modern and translates beyond oncology — the same logic applies to any TTE emulation where untreated comparators are scarce. Two demonstrated applications on phase III oncology trials.
- **Action:** **HIGH** — read for the time-varying-weight construction and risk-set selection. Direct add to your causal-inference reference shelf.

### 7. arxiv-digest 06-06: Federated SPARQL querying for genomic variant functional annotation
- **Authors / venue:** A. Bodrug-Schepers, R. Bourcier, R. Redon, A. Gaignard — arXiv:2606.05918v1, primary category q-bio.QM. (2026-06-04 submission).
- **Surfaced by:** `arxiv-digest` 2026-06-06 (keyword: "knowledge graph"). The other half of the week's only two pipeline hits.
- **Thread:** **Knowledge graphs & ontologies** (biomedical) **+** **Variant interpretation** (functional annotation) **+** FAIR / privacy-preserving infrastructure.
- **What it is:** Variant annotation via federated SPARQL queries — clinico-genomic data modeled as a KG using biomedical ontologies, annotation performed by federated querying of remote KGs (UniProtKB) rather than duplicating public databases on-site. Use-case is the ICAN cerebral berry aneurysm research program.
- **Why it matters to you:** This is the *infrastructure* side of variant interpretation — instead of locally caching gnomAD/ClinVar/UniProt, the proposal is to query them in place. Two interesting angles:
  1. **FAIR + sensitive-data alignment** — the inverse of the usual variant-annotation pipeline. Useful if you're advising on All-of-Us-style cohorts where the genomic data has to stay on-platform.
  2. **Biomedical KG with explicit ontology layer** — pairs with PiMInfer (#1) for a "KG-first" stack for variant interpretation + phenotype-to-mechanism. Two same-week arXiv papers both pointing in the same biomedical-KG direction is mild evidence the q-bio.QM tier is moving that way.
- **Action:** **HIGH (infrastructure)** — read for the federation pattern; lower priority than #1 unless you're actively spec'ing an annotation pipeline.

### 8. Dynamical proteomic signatures for depression across preclinical stages in 52,121 individuals from a prospective cohort study
- **Authors / venue:** J. Hui, W. Wei, P. Chuyu, B. Zhao, Y. Gou, D. He, J. Feng, S. Cheng, X. Yang, B. Cheng, F. Zhang — *World J Biol Psychiatry*, 2026. PMID 42246212. (UK Biobank, n=52,121.)
- **Surfaced by:** PubMed "UK Biobank" alert (06-06).
- **Thread:** **Genetic epidemiology** (proteome-wide screening; pairs with proteome-MR pattern) **+** **EHR-linked biobanks** (UKB).
- **What it is:** UK Biobank proteomic-Olink cohort study (n=52,121) deriving "dynamical" proteomic signatures for depression across preclinical stages — i.e., longitudinal proteomic shifts in the years before clinical depression diagnosis.
- **Why it matters to you:** The UKB Olink proteome is now the dominant substrate for proteome-MR and proteome-PheWAS work (3+ papers in the prior two reports). This one is *longitudinal proteomics* in the preclinical window — a less-explored modality than the cross-sectional proteome-MR template, and methodologically interesting if you're considering trajectory-based proteomic biomarkers for any of your tracked diseases (CHIP cardiometabolic outcomes; CFTR/CF baseline-to-modulator trajectories).
- **Action:** **HIGH (methods)** — skim for the longitudinal-proteomic analysis design and stage definition; primary clinical readout (depression) is off-thread but the trajectory-proteomic template is portable.

### 9. Addressing the needs of nano-rare patients: the n-Lorem experience
- **Authors / venue:** S.T. Crooke, S. Glass, J.G. Gleeson, L. Mignon, **Wendy Chung** et al. — *Nucleic Acids Research*, 2026.
- **Surfaced by:** Wendy Chung "new articles" alert.
- **Thread:** **Rare disease** (ultra-rare end of the spectrum) **+** variant interpretation **+** therapeutic infrastructure (ASOs).
- **What it is:** A report on the n-Lorem Foundation's experience treating "nano-rare" patients — pathogenic variants with known worldwide prevalence <30 patients — with custom antisense oligonucleotides (ASOs). Wendy Chung's involvement signals the clinical-genetics provenance.
- **Why it matters to you:** The nano-rare tail is the limiting case of your rare-disease thread: patient n=1 to n=30 makes population-screening, GWAS, and PheWAS infrastructure unusable, but HPO-based phenotype matching and individual-variant interpretation become primary. The n-Lorem framework is a case study in *how* you operationalize delivery (variant identification → ASO design → IRB / FDA path → outcomes tracking) — useful background even if you're not directly designing ASOs. The paper is the closest the window comes to the "rare-variant + HPO-based phenotype matching" angle in your INTERESTS file under rare-disease repurposing.
- **Action:** **HIGH** — read for the operational framework (eligibility, variant classification standards, outcomes capture) more than the molecular biology. Worth citing in any rare-disease drug-development methods context.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Integrative analyses elucidate transcriptional regulatory functions of risk alleles for metabolic liver disease** — B. Zhu, N. He, Y. Xiao, B. Chen, C. Li, R. Mandla, Y. Liu et al. — *Nature Genetics*, 2026. (Lisa Bastarache + Joshua C. Denny citation alerts × 2.) MASLD GWAS loci × chromatin accessibility × MPRA. *Watch for:* the MPRA-based functional validation pipeline; pairs naturally with the GLP-1/MASLD pharmacoepi line.
- **Genome-wide association study of coronary flow reserve assessed by cardiac perfusion PET suggests a role for NF-κB pathway** — R. Venkatesh, T. Cherlin, N. Wayne, R. Kumar, L. Guare et al. — *Nature Cardiovascular Research*, 2026. (J.C. Denny citation alert.) Penn-led GWAS of an *imaging-derived phenotype*. *Watch for:* the CFR phenotype operationalization from cardiac PET — useful template if you're tracking imaging-anchored phenotypes in AoU/UKB.
- **A Practical Upper Bound on Selection Bias Effects in Medical Prediction Models** (Liu, Wang, Altman) — already in HIGH as #5; cross-listed here for any reader scanning methods first.
- **Towards Multidisciplinary Summarization of Hospital Stays: Efficient Sentence-Level Clinical Provenance Categorization** — B. Karacan, V. Bhargava, B. Di Eugenio, N. Parde et al. — arXiv:2606.02487, 2026. (J.C. Denny citation alert — cites a clinical-note section-header paper.) Sentence-level *provenance* (which clinical role authored which sentence) for downstream multidisciplinary summarization in the NICU. *Watch for:* the provenance classifier — relevant if you're doing LLM-assisted phenotyping from notes and need to weight or filter by author role (a known confound in computable-phenotype QC).
- **Epidemiological and bioinformatics analyses of air pollution and genetic susceptibility in aortic stenosis risk** — Y. Ma, Q. Jiang, J. Zhang, Y. Yang, Y. Tian, J. Yang — *Nature Communications*, 2026 (UK Biobank). PMID 42248854. *Watch for:* the G×E interaction design between air-pollution exposure (likely PM2.5) and AS PRS — methods transferable to any G×E in your cardiometabolic threads.
- **Shared pathophysiology and therapeutic repurposing in Alzheimer's disease and type 2 diabetes: a critical review of convergent mechanisms and clinical challenges** — W. Fu, R. Lu, D. Wang, Z. Sang — *Bioorg Chem*, 2026 (review). PMID 42247872. *Watch for:* the convergent-mechanism framing for repurposing between two chronic conditions — useful background for any GLP-1 / SGLT2i → neurodegeneration repurposing argument (an active area in real-world-evidence pharmacoepi).

---

## SKIP / noise (logged, no action)

- **arxiv-digest pipeline:** 06-02 / 06-03 / 06-07 = 0 papers; 06-03 again logged "3/4 categories failed to fetch." This is the **third consecutive week** the q-bio fetcher has shown the same intermittent failure. Pipeline is effectively reduced to stat.AP signal only on bad days.
- **PubMed "drug repurposing"** alert: of 9 items, 0 were on-thread (all small-molecule structure-based virtual-screening single-target oncology / antiviral papers — no KG/GNN, no EHR-based repurposing, no causal framing). The PubMed "drug repurposing" feed is a high-noise channel; the Scholar feed is doing better.
- **PubMed "UK Biobank"** alert (9 items): retained the 1 proteomic-depression paper (Hui et al., HIGH #8) and the 1 G×E air-pollution paper (Ma et al., METHODS-WATCH). The other 7 were single-question UKB papers (water hardness → CKD; allergic disease → osteoporosis; physical-activity attenuation of mortality in T2D; musculoskeletal → Parkinson's; retinal morphology → depression/anxiety; ACADM β-oxidation in AS/AAA; circadian preference → cancer-depression comorbidity). Each is a clean UKB observational paper but doesn't overlap with active disease threads or showcase a method you don't already have.
- **PubMed "All of Us"** alert: 1 item (Husseinali et al., androgenetic alopecia & cardiometabolic comorbidities) — off-thread.
- **Maurin et al., *Nature Communications*, "Epigenetic landscapes in human pancreatic islets…"** — high-quality islet methylome paper (Denny citation alert), but pure functional epigenomics; not on your threads.
- **Iyer et al., PNAS, MYBPC1-linked Myotrem myopathy** — single-gene rare disease structural biology; off-thread.
- **Osaghale et al., *Gene Reports*, Replication-guided functional genomic prioritization in AD** — FinnGen-based AD GWAS prioritization; low-tier venue; off-thread.
- **Gliantseva et al., *Bulletin of Experimental Biology…*, uterine-fibroid GWAS loci × obesity** — single small candidate-SNP study; methodologically thin.
- **Nguyen et al., *World Allergy Org J*, ML for CBZ/ALLO SCAR prediction in Vietnamese** — pharmacogenomic ADR prediction; off-thread unless you're tracking HLA-based ADR work specifically.
- **Several "drug repurposing" Scholar items** — FusionTarget (fusion-protein virtual screening), Mou et al. structure-based to LLM review, Awasthi DLBCL repurposing, Tan pancreatic-cancer HK2-virtual-screen, MAGC-DTI cross-attention DTI prediction, Wang LYPD6B single-cell breast-cancer repurposing, Zhou et al. *Adv Sci* TNBC repurposing. All are target-anchored / structure-anchored / single-cell-anchored — none with the EHR or KG-with-explainability angle your INTERESTS flag as high-priority for repurposing.
- **"Knowledge graph"** Scholar item: again non-biomedical (news-recommendation KG). Same recurring noise as the prior 3 weeks.
- **"Variant interpretation"** Scholar item: hearing-loss Brazilian patient cohort — single-population clinical reporting, not the broader ACMG/ClinGen-methodology shape your INTERESTS flag.
- **"Foundation models + EHR"** Scholar item: Olorunnisola et al. *sociotechnical sensemaking in anesthesiology* — qualitative case study, not a foundation-model paper.
- **Citation-only churn** in Karczewski (admixture-tracts paper), Montgomery (proteomic signatures for retinal degeneration in T2D), Kastner (systemic sclerosis ethnicity phenotyping), Szolovits (self-harm-detection LLMs in mental health), Shendure (multi-omic transformers for GRN inference), Luo (knowledge-graph news recommendations), van der Schaar (critically-damped momentum optimization), Zou (SQUEEZE EVOLVE), Bastarache extra cites (ICI cardiac toxicity Japanese registry, ICI MMM-overlap FAERS).

---

## Suggestions for the pipeline

Carrying forward from prior reports, with one new item:

1. **Q-bio fetch is now chronically broken.** Three consecutive weeks of "3/4 categories failed to fetch" warnings on at least one day. Recommend: (a) check arXiv API status logs for the fetch window (likely rate-limit collision), (b) add an exponential-backoff retry loop with jitter rather than the current 2-retry hard cutoff, and (c) consider sequencing categories with a 30-second gap instead of parallel fan-out. The 5-second client delay in `arxiv_digest.py` is below what arXiv considers polite under load.
2. **Expand source set.** Same recommendation as the prior two reports: most genuinely on-thread papers this window were in journals + medRxiv (PiMInfer, Lu PSA+PRS, Hui proteomics depression, Zhu MASLD *Nat Genet*). Adding a medRxiv / bioRxiv subject-category fetcher with the same keyword scorer would have caught 6 of the 9 HIGH items above. Also worth adding `cs.LG` and `stat.ME` (the latter would have caught the Shen treatment-switching paper without it being a categorical mismatch).
3. **Tighten `apol1` keyword** (carried over): word-boundary anchoring `\bapol1\b` to suppress APOE false positives. Still relevant.
4. **`knowledge graph` keyword** (carried over): require biomedical co-occurrence (`biomedical knowledge graph`, `clinical knowledge graph`, `disease knowledge graph`) — fourth consecutive week of news / manufacturing KG noise.
5. **Add `proteome-wide` / `colocalization`** (carried over): proteome-MR / proteome-PheWAS shape continues to recur (Hui depression UKB this week, plus the 3-cluster prior window).
6. **NEW: PubMed `drug repurposing` feed is noisy** at the structure-based / single-target oncology end. Either (a) require a co-occurrence term (`electronic health records`, `phenome`, `knowledge graph`, `causal`, `target trial`) on top, or (b) demote PubMed `drug repurposing` to METHODS-WATCH by default and rely on Scholar for the high-quality KG / EHR-based hits.
7. **NEW: PubMed `All of Us` query is too narrow** — only returned 1 PubMed hit this window vs. 8+ via Scholar. Worth widening to `"All of Us"[ti] OR "All of Us research program"[abstract]` instead of the current bare `"All of Us"` literal.
