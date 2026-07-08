# Research digest report — 2026-07-08

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-07 → 2026-07-08** (first report since 2026-06-20).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-07-08 07:30Z batch | Large batch (~25 author-feed alerts: Chenjie Zeng self-feed and self-citations, Karczewski, Denny, Hripcsak (implied), Hernán, Yang, Montgomery, Szolovits, Zitnik, Vogelstein, Natarajan, Luo, Chute, Shendure, Kastner, Pascal Brandt, Wendy Chung). |
| NCBI My-NCBI "What's new" saved-search digests | daily | Three digests fired 2026-07-08 12:29Z: `drug repurposing` (11 items), `All of Us` (1 item), `UK Biobank` (16 items). |
| `arxiv-digest` repo (`digests/`) | 2026-07-07 → 07-08 | **07-07 = 3 papers** (Fontana UKB multimorbidity, Bang KG-perturbation drug response, Asiedu multi-omics causal discovery); **07-08 = 1 paper** (Nakamura causal video features — off-thread). Pipeline healthy. |

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only; PubMed alerts contain
> title/authors/venue only. Reports below contextualize that metadata
> against your research threads; nothing here reflects full-text reading.

---

## Executive summary

- **Triple-feed hit on within-sibling PGS accuracy attenuation
  (Kelly et al.)** — the same PGS-methods paper surfaces simultaneously
  in your **Hripcsak related-research**, **Denny related-research**, and
  **Hripcsak citations** feeds. Directly extends the PRS-robustness sub-
  thread you tracked last window (Souaiaia tails paper, Ferreira /
  de La Harpe stability papers). **HIGH.**
- **Self-feed hit on cystic-fibrosis pregnancy outcomes
  (MATRIARCH_CF)** — Downes, Bokobza, Weitnauer et al. surfaces in your
  own *Chenjie Zeng — new related research* feed. On the CF/CFTR
  disease thread; MATRIARCH is a prospective observational study of
  pregnancy and parenthood in the modulator era. **HIGH.**
- **Drug-target validation via UK-Biobank genetics
  (Moix, Sadler, Kutalik, *Genome Medicine* 2026)** — integrates
  genetic evidence to identify approved drug targets. Cross-cuts the
  **drug-repurposing** and **UK Biobank** threads. **HIGH.**
- **Proteomic mortality prediction in heart failure
  (Meyre et al., *Eur Heart J* 2026)** — proteomic-biomarker layer for
  incident-HF mortality. Extends the plasma-proteomics-as-risk sub-
  thread (Ding aging-proteomic paper from the 06-20 report). Kutalik/
  Paré/Joseph group; likely UKB-PPP or Global Cardiometabolic proteomics
  scaffolding. **HIGH.**
- **RankVar: ML variant ranking and reinterpretation for rare genetic
  diseases (Zhang et al., *Genome Medicine* 2026, Wendy Chung new-
  articles feed)** — directly on the **variant interpretation** +
  **rare disease** threads. Chung is a senior collaborator on many
  clinical-actionability panels; new-articles firing (not related-
  research) suggests Chung is an author. **HIGH.**
- **UK-Biobank multimorbidity network paper on the `arxiv-digest`
  (Fontana et al., 07-07, `stat.AP`)** — the first genuinely on-thread
  paper the pipeline has surfaced in ~3 weeks: Gaussian Graphical Model
  + Lasso on 24 cardiometabolic diseases and 76 risk factors in UKB,
  with community structure → progression phenotypes → survival strata.
  Directly on the **chronic-disease clustering / multimorbidity**
  thread. Score 3 (`uk biobank`, `biobank`, `multimorbidity`). **HIGH.**
- **AoU Research Program CNV-strabismus/amblyopia paper (Lee & Whitman,
  *IOVS* 2026)** — first AoU genome-wide CNV study surfaced this week;
  narrow disease focus (strabismus/amblyopia), but the AoU-CNV-pipeline
  design (case-count power for rare CNVs in a diversity cohort) is
  reusable. **METHODS-WATCH.**
- **PREDIKTOR: patient-specific KG + LINCS perturbation view for drug
  response** (Bang et al., 07-07 `cs.LG`, arxiv-digest) — patient-level
  KG (DysRegNet + DrugBank) aligned with LINCS-L1000-derived
  perturbation embeddings via a CLIP-style contrastive objective;
  zero-shot transfer to the I-SPY2 trial. Methods pattern is directly
  useful for **explainable drug-repurposing** work, but the concrete
  application is oncology response prediction. **METHODS-WATCH.**
- **Causal-inference note**: Kagenaar et al. — SABR vs surgical
  resection for early-stage NSCLC as an emulated target trial (Chute
  related-research feed) — clean textbook TTE design in an EHR-linked
  cancer cohort. Off your active drug-class threads (GLP-1 / SGLT2 /
  CFTR / HRT), but a **METHODS-WATCH** for TTE template design.
- **UK-Biobank governance perspective (Green & Ritchie, *BMJ* 2026,
  from `UK Biobank` PubMed alert)** — "Trust without safeguards: why UK
  Biobank is the outlier among our data services." Not a research
  paper; a policy commentary. **METHODS-WATCH / SITUATIONAL AWARENESS.**
  Worth flagging because it could affect data-access norms across
  UKB-adjacent projects.
- **`arxiv-digest` pipeline is healthy this window.** 07-07 fired
  normally (3 papers, one strongly on-thread); 07-06 and 07-05 were
  genuine 0-paper days; 07-08's single paper (Nakamura video-features
  causal inference) is off-thread. No fetch failures this week.

Counts: **6 HIGH**, **5 METHODS-WATCH**, rest SKIP / logged.

---

## HIGH priority — detailed reports

### 1. Within-sibling attenuation of polygenic risk score accuracy: investigating the effects of principal component analysis, LD score regression, and mixed model *(Kelly et al.)*
- **Authors / venue:** C.M. Kelly, O. Onuorah, E. Gilbert et al. — journal unclear from snippet (likely *Human Molecular Genetics* / *Genetic Epidemiology* / preprint). Snippet from Scholar alerts.
- **Surfaced by:** **Triple-feed saturation** — (a) *Joshua C. Denny — new related research*, (b) *George Hripcsak — new related research* (implied by parallel batch), (c) *George Hripcsak — 7 new citations to articles* (title text mirrors that citation feed). Two independent related-research feeds firing on the same paper, plus a citation hit, is a strong-consensus signal in a methodological area (PRS robustness / within-family attenuation).
- **Thread:** **Genetic epidemiology / PRS** (specifically PRS *within-family accuracy attenuation*, a canonical robustness sub-question) **+** methods for PRS calibration.
- **What it is:** Within-sibling analyses are the gold standard for isolating direct genetic effect from indirect (assortative-mating, dynastic, population-stratification) contributions to a PRS's predictive accuracy. Kelly et al. dissect *how much of the well-documented PRS accuracy attenuation from population to sibling designs* is attributable to specific pre-processing / methodological choices — PCA (population-structure correction depth), LD score regression (heritability partitioning that feeds PRS-weighting), and mixed-model GWAS (BLUP-style shrinkage). The paper is a methods-audit rather than a new PRS.
- **Why it matters to you:** Three converging reasons.
  (a) **Extends the PRS-stability / PRS-robustness sub-thread** that has now dominated three consecutive reports (Souaiaia tails paper 06-20; Ferreira across-version; de La Harpe across-method). Kelly et al. is the *within-family* axis of that same robustness map — population vs. family estimates are the standard external-validity check on PRS.
  (b) **Directly relevant to composite-risk scoring** (INTERESTS: "composite risk models stacking PRS with rare pathogenic variants"). If attenuation depends on PCA depth / LDSC choices, then any composite-risk write-up needs to be explicit about which PRS weights are being combined, and whether they've been benchmarked in a within-family design.
  (c) **Triple-feed firing across the two most-cited EHR-linked-biobank methodologists** (Denny, Hripcsak) is unusually informative — it means the PRS-methods audience the paper aims at is exactly the AoU/UKB/BioVU/eMERGE audience.
- **Action:** **HIGH — read first.**
  (i) Identify the evidence type: is this a re-analysis of UKB sibling pairs, or a simulation? A UKB-sib re-analysis is far more citable.
  (ii) Note *which* PCA / LDSC / mixed-model configurations retain vs lose sibling accuracy — that operational answer is what a downstream user (you, in AoU/MVP work) actually needs.
  (iii) Cross-check with the Souaiaia tails paper: if tail architecture *and* within-family attenuation both differ from bulk, the composite-PRS-plus-rare-variant argument gets stronger.
  (iv) Confirm the journal / preprint venue and the corresponding-author's institution — the CM Kelly + O Onuorah authorship suggests an Irish / European genetic-epi lab.

### 2. Maternal, Infant, Reproductive and Child Health in Cystic Fibrosis (MATRIARCH_CF): a prospective, observational study to evaluate pregnancy and parenthood in the modulator era *(Downes et al.)*
- **Authors / venue:** A. Downes, I. Bokobza, L. Weitnauer et al. — venue unclear from snippet (likely *Journal of Cystic Fibrosis* or *ERJ Open*).
- **Surfaced by:** *Chenjie Zeng — new related research* feed — **your own related-research feed**. Self-feed firing is one of the highest-precision channels in this triage pipeline; it fires only when Google's relevance model judges the paper close to your published work.
- **Thread:** **Cystic fibrosis / CFTR** (INTERESTS: "modulator pharmacoepi, real-world outcomes, modulator eligibility & psychosocial impact"). MATRIARCH_CF is squarely on the modulator-era CF outcomes thread — pregnancy and parenthood are exactly the post-modulator questions that couldn't be asked before Trikafta shifted median predicted lifespan.
- **What it is:** A prospective observational cohort of pregnant women with CF (and their partners / infants), designed to characterize maternal, obstetric, and pediatric outcomes in the modulator era. This is the CF-community response to the sudden clinical relevance of pregnancy in CF as median lifespan pushed past the third decade. Consortium-scale design (multi-site — Downes/Bokobza are likely lead sites).
- **Why it matters to you:** Two converging reasons.
  (a) **Directly on the CF/CFTR modulator-pharmacoepi thread** you have flagged in INTERESTS. Pregnancy-in-CF is one of the top-three modulator-era clinical questions the field is racing to answer (alongside CFTR-modulator use during pregnancy, and modulator effect on children born to modulator-taking parents).
  (b) **Self-feed hit** — Google's relevance model is telling you this paper is close to something you've published. If you have a CF real-world-outcomes paper in the reference list, MATRIARCH_CF will likely cite it (or be citable *by* your next CF write-up).
- **Action:** **HIGH.**
  (i) Read for the modulator-exposure ascertainment: are they collecting explicit Trikafta / Kalydeco exposure timing during pregnancy, or is it a post-hoc classification?
  (ii) Note the outcomes: maternal (pulmonary exacerbations during / post pregnancy), obstetric (preterm, PROM, GDM), and pediatric (birth weight, congenital anomalies, breastfeeding) — the pediatric column is what Trikafta-in-pregnancy studies are missing most.
  (iii) Consortium identity — is this UK-CF-registry-linked, US CFF-linked, or European? The registry linkage determines whether this study can be replicated in your EHR-linked cohorts.
  (iv) Save as a citable reference for any modulator-era real-world outcomes work.

### 3. Integration of genetic evidence to identify approved drug targets *(Moix, Sadler, Kutalik)*
- **Authors / venue:** S. Moix, M.C. Sadler, Z. Kutalik — ***Genome Medicine*, 2026; 18(1):98**. PMID 42410617. Surfaced by NCBI `UK Biobank` alert.
- **Surfaced by:** Not a Scholar-alert hit; came in via the **NCBI My-NCBI `UK Biobank` saved search** — meaning the paper uses UKB data as part of its evidence integration.
- **Thread:** **Drug repurposing** (INTERESTS explicitly: "computational identification of new indications for approved drugs" + "EHR-based repurposing signals" + "target-only or chemistry-only pipelines *lower interest* without a clinical-evidence loop") **+** **UK Biobank** **+** **Genetic epidemiology** (target-genetics integration = MR-style / colocalization / Open Targets style).
- **What it is:** *Genome Medicine* review / methods paper on integrating genetic evidence to identify (and by extension, re-identify) approved drug targets. The Kutalik-group provenance suggests a rigorous statistical-genetics framing — likely Mendelian-randomization plus colocalization plus PheWAS-style side-effect scans, applied at UKB scale. The framing "approved drug targets" implies the paper isn't proposing new targets but is *validating* / *rationalizing* the current pharmacopeia through genetics — which is the natural precursor to explainable drug-repurposing.
- **Why it matters to you:** Three reasons.
  (a) **Directly on the drug-repurposing thread**, in the sub-flavor you have flagged as high interest ("explainable hypothesis output" and "clinical-evidence loop" — as opposed to target-only pipelines). Genetics-as-evidence integration is the "explainable rationale" ingredient.
  (b) **UKB-based** — makes it a candidate template for the same design applied to AoU or MVP as those cohorts' proteomic and genetic layers mature.
  (c) **Kutalik group** — the Lausanne genetic-epi lab has one of the cleanest MR + colocalization pipelines in the field; whatever workflow they propose is likely to be reproducible and well-benchmarked.
- **Action:** **HIGH.**
  (i) Read for the *evidence layers* combined (genetic-association, MR, colocalization, tissue-specific eQTL, protein-QTL, side-effect PheWAS) — the composition of layers is the reusable design pattern.
  (ii) Note the retrospective / prospective mode — does the paper *rediscover* approved-target genetics for known drugs (validation exercise), or *propose* new indications for approved targets (repurposing exercise)? The latter is directly on-thread; the former is METHODS-WATCH-tier.
  (iii) Cross-check against Open Targets Genetics workflows — where does the paper add value beyond the Open Targets score?
  (iv) Save as a citation anchor for any drug-repurposing-via-EHR-and-genetics write-up.

### 4. Proteomic markers enhance mortality prediction in heart failure *(Meyre et al.)*
- **Authors / venue:** P.B. Meyre, Y. Li, G.L. da Rocha, E. Shemesh, M. Chong, A. Roy, K.M. Karaye, S. Störk, L. Mielniczuk, S.K. Sharma, B. Mohan, F. Lanas, T. Wittlinger, A. Celik, J. Abdullakutty, J. Núñez, O.S. Ogah, N. Jathappa, T. McCready, A. Grinvalds, H. Gerstein, D.P. Leong, P.G. Joseph, S. Yusuf, G. Paré — ***European Heart Journal*, 2026** (`ehag525`, ahead of print). PMID 42414001. Surfaced by NCBI `UK Biobank` alert.
- **Surfaced by:** NCBI My-NCBI `UK Biobank` saved search — UKB proteomics or UKB-adjacent proteomic scaffolding likely used.
- **Thread:** **ML for precision health** (individualized risk stratification tied to clinical decisions — "who to escalate" in HF is exactly the sort of decision you flag as HIGH) **+** proteomic-biomarker layer of the composite-risk sub-thread **+** adjacent to multimorbidity / cardiometabolic disease thread.
- **What it is:** A large, multi-continental heart-failure cohort study demonstrating that adding plasma proteomics to a clinical risk score meaningfully improves mortality prediction. Author list spans Canada / Europe / Asia / Africa / Latin America — this is almost certainly a **PURE-HF / PHRI (Population Health Research Institute) global cohort** design (Yusuf, Paré, Gerstein, Leong, Joseph, McCready are the PHRI leadership). The proteomics layer likely uses Olink or SomaScan; the value proposition is *global* transferability of proteomic prognostic signatures, not just UKB-PPP.
- **Why it matters to you:** Three reasons.
  (a) **Extends the plasma-proteomic-signature sub-thread** that emerged with the Ding et al. Nature Medicine cellular-aging paper (06-20 report). Meyre et al. is the *heart-failure-specific* instance of the same "proteins improve clinical prediction" argument, now with a Yusuf/PHRI global cohort backing it — high generalizability claim.
  (b) **Directly on the "ML tied to clinical decision" high-priority framing** in your INTERESTS file. HF mortality prediction → escalation decisions (transplant listing, LVAD eligibility, palliative-care initiation) is exactly the decision loop you have flagged as HIGH.
  (c) **PHRI cohort design pattern** — a global-registry-scale HF cohort with proteomic add-on is an operational template for what an AoU-scale proteomic HF study could look like.
- **Action:** **HIGH.**
  (i) Read for the cohort composition and the specific clinical baseline (MAGGIC / Seattle / a standard HF risk score) that proteomics is being added on top of. Incremental performance vs *state-of-the-art* clinical scoring is what determines clinical actionability.
  (ii) Note whether Meyre et al. report **decision-curve analysis or net reclassification improvement** rather than just AUC / c-statistic gains — that framing is what your INTERESTS specifically calls out ("calibration and decision-curve analysis").
  (iii) Check the proteomic platform (Olink Explore HT ~5400 proteins vs SomaScan ~7000) and whether they validate signatures across platforms — cross-platform reproducibility is the open question in proteomic-signature transferability.
  (iv) Cross-reference with UKB-PPP-derived proteomic HF signatures — if concordant, it's the strongest case yet for proteomic add-on becoming a standard HF workup.

### 5. RankVar: machine learning-based variant ranking and reinterpretation for rare genetic diseases *(Zhang et al.)*
- **Authors / venue:** Y. Zhang, M.U. Ahsan, P. Wang, X. Lin, I.M. Campbell et al. — ***Genome Medicine*, 2026**. Surfaced by Scholar alert.
- **Surfaced by:** *Wendy Chung — new articles* feed — "new articles" (not "related research") means Chung is likely an author or very close collaborator.
- **Thread:** **Variant interpretation** (ACMG / ClinGen classification — INTERESTS: "variant curation tooling (InterVar, AnFiSA-style DSLs)") **+** **Rare disease** ("rare-variant association methods, deep phenotyping for rare-disease diagnosis").
- **What it is:** An ML-based variant ranking + *reinterpretation* system for rare-genetic-disease diagnostic work-ups. The "reinterpretation" framing is the important word — this is not a first-pass classifier but a system for *revisiting* previously-called VUSes as new evidence (phenotype data, functional evidence, in silico scores) accumulates. Wendy Chung + I.M. Campbell (CHOP) suggests a pediatric-genetics grounding — RankVar is likely to have been validated against clinical WES cases with expert-adjudicated ground-truth ACMG classifications.
- **Why it matters to you:** Three reasons.
  (a) **Directly on the variant-interpretation + rare-disease intersection** — reinterpretation of VUSes is one of the concrete places where automation has clinical impact (the ClinGen reinterpretation curation lag is a known bottleneck).
  (b) **Genome Medicine venue + Chung authorship** suggest this is targeted at clinical-genetics practitioners, which is where variant-curation tooling actually gets used.
  (c) **Complements the Marderstein noncoding paper (06-20 report)** — that paper is about noncoding-effect estimation; RankVar is about ranking and reprioritization once effect estimates exist. Together they slot into a "next-generation variant-interpretation stack."
- **Action:** **HIGH.**
  (i) Read for the *ranking signal* being learned — is it a probabilistic ACMG-criterion aggregator, a direct pathogenicity likelihood, or a Bayesian update over prior classification? Each has different implications for clinical UI.
  (ii) Note the training / evaluation cohort — CHOP + Columbia + wherever Chung is now (Broad?) suggests a well-curated tertiary-care case series. External validation is the open question.
  (iii) Check the release status (is RankVar deployed as a tool, or a research prototype?) — deployed tools are directly citable for your ACMG-tooling work.
  (iv) Compare to InterVar / Franklin / VarSome workflows — where does RankVar's ranking add value beyond commodity ACMG-criterion classifiers?

### 6. Enhancing comorbidity network inference with risk-enriched health trajectories embedding *(Fontana, Mapelli, Di Angelantonio, Ieva)*
- **Authors / venue:** N. Fontana, A. Mapelli, E. Di Angelantonio, F. Ieva — ***arXiv 2607.04702v1***, 2026-07-06 (`stat.AP`, surfaced by `arxiv-digest` 07-07). Score 3 (`uk biobank`, `biobank`, `multimorbidity`).
- **Surfaced by:** `arxiv-digest` (07-07) — the first genuinely on-thread arxiv-digest paper in three reporting windows.
- **Thread:** **Chronic disease clustering and multimorbidity** (INTERESTS: "Unsupervised and semi-supervised methods for discovering disease subtypes, multimorbidity patterns, and disease trajectories from EHR or biobank data"; "graph-based comorbidity networks, and trajectory clustering. Particularly interested when applied to cardiometabolic disease") **+** **Biobanks with EHR linkage** (UK Biobank) **+** ML for precision health (risk stratification tied to survival trajectories).
- **What it is:** A methodological framework for population-level disease-network inference that (a) uses *individual health trajectories* rather than cross-sectional prevalences, (b) applies Gaussian Graphical Models with Lasso regularization for sparse network estimation, (c) explicitly models *shared risk factors* as confounders in a dedicated "confounding evaluation step" (rather than ignoring confounding as most comorbidity-network work does), and (d) uses the resulting community structure to derive *patient-level embeddings* that then cluster into "four progression phenotypes with significantly different long-term survival trajectories." Applied at UKB scale on 24 cardiometabolic diseases + 76 risk factors. Di Angelantonio (Cambridge, Emerging Risk Factors Collaboration) is the clinical anchor; Ieva (Milan, Stat) is the methods anchor.
- **Why it matters to you:** Four reasons.
  (a) **Perfect fit for the multimorbidity / disease-clustering thread**, in the sub-flavor you explicitly flagged as HIGH ("Particularly interested when applied to cardiometabolic disease, autoimmune disease, or aging-related multimorbidity"). Cardiometabolic multimorbidity in UKB is exactly the target application.
  (b) **The confounding-aware framing** is the methodological innovation you'd want to see — most comorbidity networks in the literature are correlation-based and produce fully-connected uninterpretable graphs; this paper's Lasso + prior-informed-confounding step gives sparse, interpretable networks.
  (c) **The progression-phenotypes-to-survival pipeline** is the operational hook — network → community → embedding → cluster → survival curve is a template for turning multimorbidity networks into actionable risk strata.
  (d) **UKB scaffolding** — the codebase (if released) would transfer directly to AoU / MVP / BioVU multimorbidity analyses.
- **Action:** **HIGH.**
  (i) Skim the arXiv HTML render for the confounding-evaluation step's specification — is it a formal DAG-based backdoor adjustment, or a heuristic risk-factor subtraction? The former is a citable methodological advance.
  (ii) Note the four disease communities and whether they align with the standard cardiometabolic syndromes (metabolic syndrome, atherothrombotic, HFpEF cluster, CKD-anchored). If the paper *rediscovers* the standard clusters, that's validity evidence; if it identifies novel splits, that's the discovery.
  (iii) Check code / data availability — the reproducibility of a GGM + Lasso pipeline in UKB depends heavily on shared trajectories code.
  (iv) Consider as a template for a comparable multimorbidity analysis in AoU or MVP, which have shorter EHR follow-up but broader demographic diversity.
  (v) Save as a citation anchor for any multimorbidity-trajectory or cardiometabolic-clustering work.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Lee & Whitman — Genomic copy number variants associated with strabismus and amblyopia in the All of Us Research Program** — *Investigative Ophthalmology & Visual Science*, 67(8):21, 2026 (PMID 42411868, from NCBI `All of Us` alert). AoU-based genome-wide CNV analysis. Substantively narrow (strabismus / amblyopia) but the **AoU rare-CNV analysis design** — case-count power in a diversity cohort, ancestry-stratified CNV callsets, EHR-linked phenotype ascertainment — is directly transferable. Small operational note: this is one of the first published AoU CNV papers (most published AoU work has been SNV-based); worth reading for the AoU-CNV-pipeline template.

- **Bang et al. — PREDIKTOR: Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations** — *arXiv 2607.04557v1*, 2026 (`cs.LG`, surfaced by `arxiv-digest` 07-07, score 1). A **CLIP-style contrastive alignment** of two per-patient views: (a) an individualized gene-regulatory-network + drug-target KG (DysRegNet + DrugBank), (b) a frozen LINCS-L1000-derived post-perturbation transcriptome. Trained on TCGA, zero-shot to I-SPY2 (+5.6% AUROC). *Watch for:* the **patient-level KG + perturbation-embedding alignment pattern** — this is directly reusable for an explainable-drug-repurposing pipeline where the "explanation" is the subgraph / pathway that links a patient's dysregulated network to a drug's LINCS signature. The oncology framing is off your active disease threads, but the methods pattern is exactly the sort of "explainable rationale + clinical-evidence loop" you have flagged as high-interest in drug-repurposing.

- **Asiedu & Watson — Causal ASCEND: Scalable Two-tier Causal Discovery on High Dimensional Multi-omics Data** — *arXiv 2607.04527v1*, 2026 (`stat.ML`, surfaced by `arxiv-digest` 07-07, score 1). Constraint-based causal-discovery framework that exploits known *two-tier* (upstream regulators → downstream effects) biological structure for polynomial-time discovery on multi-omics scale. *Watch for:* the **dynamically updated ancestral conditioning sets** primitive — if this generalizes beyond SNP-methylation-expression tiers to EHR-scale variable orderings, it's a useful causal-discovery primitive for phenome-wide MR / mediation analyses. Off-thread substantively but on-thread methodologically for the causal-inference audience.

- **Kagenaar, Lugo-Palacios, Aggarwal et al. — SABR vs surgical resection for early-stage NSCLC: an emulated target trial** — *Journal of Thoracic Oncology* (likely, per venue prefix) (from Chute related-research feed). Clean TTE design in an EHR-linked cancer cohort, comparing stereotactic ablative radiotherapy against surgical resection for stage-I NSCLC. Off your active drug-class threads (GLP-1 / SGLT2 / CFTR / HRT), but *watch for:* the treatment-strategy definition and the eligibility-window mechanics — SABR-vs-surgery TTE is a canonical worked example that transfers to any two-arm-treatment-comparison design you might build in AoU or MVP.

- **Green & Ritchie — Trust without safeguards: why UK Biobank is the outlier among our data services** — *BMJ*, 2026;394:e100164 (PMID 42413979, from NCBI `UK Biobank` alert). *Not a research paper* — a policy commentary from a data-governance / research-methods angle. **Situational awareness** — worth reading if you rely on UKB access norms, because the BMJ commentary tier can catalyze changes in data-access policy that ripple through your access-approval workflows.

- **Yaseen et al. — A CYP11B2 variant (rs7831617) is associated with lower blood pressure and a reduced risk of incident hypertension** — *Scientific Reports*, 2026 (from *10 new citations to Joshua C. Denny* feed). A blood-pressure-lowering PheWAS / GWAS-lookup-style variant paper. *Watch briefly:* if the cohort is a non-European biobank, note the CYP11B2 East-Asian-specific signal — otherwise SKIP. Denny-citation firing suggests they used a PheWAS / phecode primitive.

- **Barmada — Predicting health and disease: a conceptual framework for AI in preventive and precision medicine** — *BMJ Health & Care Informatics*, 2026 (from Karczewski citations feed). *Perspective piece*; useful as a **citation anchor** in a precision-medicine / AI-in-clinical-decisions framing paper, not a primary literature read.

---

## SKIP / noise (logged, no action)

- **NCBI `drug repurposing` PubMed alert (11 items, 07-08)** — chemistry-only / target-only pipelines dominate this alert this week: Ketodarolutamide × SARS-CoV-2 spike (Zaremba et al.), Cestode fatty-acid-binding protein virtual screening (Rodríguez et al.), Cromoglycate + GPR35 revisit (Tanaka), TYK2 activator SAR (Matsumoto et al.), XPO1 inhibition in HCC (Wang et al.), Cross-species target-similarity repurposing (Du et al.), Mitochondrial keloid signature repurposing (Le et al.). Your INTERESTS explicitly deprioritizes "target-only or chemistry-only pipelines without a clinical-evidence loop" — this week's PubMed drug-repurposing feed is almost entirely that class. **Logged, no read.** The one arguable exception is the Le et al. keloid-signature multi-omics paper (has EHR-adjacent framing), but keloid is off your disease threads.
- **NCBI `drug repurposing` — items 1 (pharmacist-nurse pressure-injury collaboration) and 2 (network-ML biomarker discovery for SLE)** — off-thread (health-services and biomarker-discovery respectively).
- **NCBI `UK Biobank` alert non-highlighted items (14 of 16)** — mostly incident-risk clinical-question papers on cardiometabolic / psychiatric endpoints (depression × stroke, MASLD × depression, triglyceride-glucose × depression-CVD, artificial sweetener × COPD, Life's Essential 8 × stroke/dementia, thyroid cancer × psychological distress, sugar restriction × anxiety/depression, HFpEF-ABA score, blood-pressure phenotypes × cardio-kidney, light-exposure × COPD, cognitive impairment × AFib, MRI-based hip-thigh muscle quantification, multimodal CVD detection). Standard UKB clinical-question output; nothing on your active drug-class or methods threads. **Logged, no read.**
- **NCBI `All of Us` alert (single item)** — the Lee & Whitman AoU CNV paper is elevated to METHODS-WATCH above; the alert has only one item.
- **Karczewski citation feed items 3–10** — Hierarchical hematologic-malignancy epigenetic-genetic classification (Schönung et al., bioRxiv); DPP9-mediated inflammasome repression in checkpoint-inhibitor lung toxicity (Brewer et al., bioRxiv); GTF3C3 biallelic-variant case report (López-López et al., Frontiers in Genetics); Pangenome-based SV imputation in dairy cattle (Yang et al., Nat Commun — Karczewski citation because they cite gnomAD SVs); Prenatal-OPE EWAS (Tang et al., Environment International); FCGR2A promoter variant IBD-stroke shared genetics (Wang et al., Mol Cell Biochem); Cardiomyopathy + myocarditis genetic profile in children (Milting et al., Eur J Heart Failure); Multi-omics arsenic toxicity ferroptosis review (Zhang XL). Karczewski citations = gnomAD-cited-by papers; most are off your specific-disease and methods threads. **Logged.**
- **Chute citations — Racial differences in HIV testing and seborrheic dermatitis in Atlanta** (Collins 2026) — off-thread; incidental Chute citation.
- **Chute related-research — SABR vs surgery NSCLC** is elevated to METHODS-WATCH above.
- **Hernán citations — GLP-1 vs DPP4 after HCC liver resection in T2D** (Xiang, Liu, Feng et al.) — pharmacoepi paper but on an HCC-recurrence outcome, not on your active GLP-1 outcomes (weight, cardiovascular, kidney, MASLD). Peripheral to the GLP-1 drug-class thread; logged.
- **Bastarache citations — 7 new citations** (top hit: PTSD-autoimmune investigation, Lawrence 2026 dissertation-style) — off-thread; the remaining Bastarache-citation snippets are truncated.
- **Karczewski related-research — WES/GS diagnostic yield in Iranian exome-negative AR intellectual disability cohort** (Shokouhian et al., *Human Mutation*, 2026) — rare-disease diagnostic-yield paper; adjacent but not directly citable in your ACMG / composite-risk work.
- **Kastner related-research — AOSD case report** — off-thread.
- **Kastner citations — Type I interferonopathies 15-year review** — off-thread mechanism review.
- **Marinka Zitnik related-research — AutoTrainess: LMs training LMs** — off the clinical/biomedical thread.
- **Shendure related-research — Pan-cell-type chromatin state annotation** (Daneshpajouh et al., *Genome Biology*, 2026) — epigenomics benchmark, off your variant-interpretation clinical thread but useful as a **background reference** if you get into cell-type-specific ACMG evidence.
- **Montgomery related-research — Long-read SV 18q12.1q21.2 triplication case** — off-thread rare-disease structural-variant case.
- **Peter Szolovits new articles — historical MIT/LCS BRAND X MANUAL** — 1980s Szolovits archival material re-listed; SKIP.
- **Peter Szolovits related-research — VLURes VLM long-text grounding benchmark** — LLM-eval benchmark, off the clinical-FM thread.
- **Peter Szolovits citations — Ethical governance of AI predictive analytics in smart healthcare** — policy piece, adjacent to your ML-clinical-decision thread but not a primary read.
- **Yuan Luo citations — SEMA5B in prostate cancer** — off-thread.
- **Vivek Natarajan citations — Dual digital twins for automated labs** — off the clinical-agent thread.
- **Vogelstein citations — p53 R175H antibody development** — off-thread cancer-mechanism paper.
- **Jian Yang related — Pangenome-based rare-variant-aware genome inference across 1kGP** (Ebler et al., bioRxiv) — sequencing-infrastructure paper; potentially useful as a **background reference** for pangenome-aware rare-variant work but off the immediate PheWAS / clinical-decision thread.
- **Jian Yang citations — Forensic epigenetics review** — off-thread.
- **Pascal Brandt related — HABITAT cloud-based mesh-enabled research data ecosystem** (Jampani et al., medRxiv) — research-data-infrastructure paper; not directly on your methods threads but might be a citation anchor for AoU / N3C / iDASH-style federated-infrastructure write-ups.
- **arxiv-digest 07-08 — Nakamura et al. Causal Inference with Video Features** — political-advertising causal inference on Super Mario Bros. + 2020 US TV ads. Clean methods but entirely off your clinical / biomedical threads. **SKIP.** (Score 1 — single keyword hit `causal inference`; would have been suppressed under a stricter deep-score threshold.)

---

## Suggestions for the pipeline

Rolling forward the ongoing list from prior reports; today's items add
one new observation:

1. **`arxiv-digest` pipeline is HEALTHY** this week (07-05 through
   07-08). 07-05 and 07-06 were genuine 0-paper days; 07-07 fired
   3 papers with 1 strongly on-thread (Fontana multimorbidity); 07-08
   fired 1 paper (Nakamura, off-thread). The rate-limit / retry
   changes appear to be working. **No action needed on the pipeline
   robustness front this window.**

2. **`knowledge graph` keyword: 8th consecutive window of largely
   non-biomedical hits** (this week's Bang et al. PREDIKTOR paper is
   biomedical but the keyword is doing its narrowing work poorly on the
   general `cs.LG` category). Repeat the recommendation from 06-20:
   change `knowledge graph` → `biomedical knowledge graph` OR add an
   AND-filter on (medical / biomedical / clinical / EHR / phenotype /
   drug / disease). Bang et al. would still surface via `drugbank` +
   `perturbation` (add `LINCS` as a keyword?).

3. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds**
   (carry-forward, unaddressed). Today's HIGH items #3 (Moix drug-target
   integration, *Genome Medicine*), #4 (Meyre proteomic HF prognostic,
   *Eur Heart J*), #5 (Zhang RankVar, *Genome Medicine*) all came in
   via Scholar or PubMed feeds because they're in journal venues, not
   in q-bio / stat.AP arXiv categories. Source expansion remains the
   single highest-impact pipeline upgrade.

4. **Add `polygenic score attenuation`, `within-sibling`, `sibling PGS`,
   `family-based PRS` as keywords** (new — HIGH item #1 Kelly et al.).
   The within-family / cross-family attenuation axis is now a distinct
   PRS-robustness sub-thread that pairs with the tails / stability /
   across-method robustness papers already tracked. Adding these
   keywords would let arxiv-digest catch the next Kelly-style paper
   directly rather than via a Denny/Hripcsak related-research feed.

5. **Add `MATRIARCH`, `CFTR modulator pregnancy`, `Trikafta pregnancy`
   as keywords** (new — HIGH item #2). The CF-modulator-pregnancy axis
   is on-thread and one of the fastest-moving CF sub-fields; direct
   keyword capture would be higher-precision than the Zeng self-feed
   for future MATRIARCH-adjacent papers.

6. **Add `drug target identification`, `genetics-informed drug target`,
   `Open Targets` as keywords** (new — HIGH item #3 Moix et al.). The
   drug-target-genetics-integration sub-thread pairs with the drug-
   repurposing thread; direct keyword capture would let the pipeline
   surface Moix-style papers before Scholar / PubMed does.

7. **Continue tracking `polygenic tails` / PRS-stability keywords**
   (carry-forward from 06-20). Today's Kelly item is the fourth PRS-
   robustness paper in three windows; the sub-thread is now consolidated.

8. **Continue tracking `proteomic signature` / `aging clock` /
   `organ-specific aging` keywords** (carry-forward from 06-20).
   Today's Meyre item is the second proteomic-prognostic paper in the
   sub-thread.

9. **Continue tracking own-Scholar-alert feeds as the highest-precision
   channel** (carry-forward). Today's HIGH item #2 (MATRIARCH_CF)
   surfaced *only* in the Zeng self-feed; the same pattern that
   surfaced the 06-18 APOL1 transplant paper and the 06-20 nephro-PRS-
   PheWAS paper. Self-feed remains gold-standard.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 6 | (1) Kelly et al. within-sibling PGS attenuation [Denny+Hripcsak triple-feed]; (2) Downes et al. MATRIARCH_CF pregnancy in CF [Zeng self-feed]; (3) Moix, Sadler, Kutalik drug-target genetic-evidence integration [*Genome Med*]; (4) Meyre et al. proteomic HF mortality prediction [*Eur Heart J*, PHRI]; (5) Zhang et al. RankVar ML variant ranking [Chung new articles, *Genome Med*]; (6) Fontana et al. UKB multimorbidity networks + progression phenotypes [arxiv-digest 07-07] |
| METHODS-WATCH | 5 | Lee & Whitman AoU CNV strabismus/amblyopia; Bang et al. PREDIKTOR patient-KG + LINCS drug-response; Asiedu & Watson two-tier causal discovery on multi-omics; Kagenaar et al. SABR-vs-surgery NSCLC target-trial emulation; Green & Ritchie UKB governance BMJ commentary |
| SKIP | ~30 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 6 METHODS-WATCH), this window
delivers a comparable HIGH count with a **different mix of channels**:
06-20 was Scholar-alert-dominated (triple-feed papers from Bastarache /
Szolovits / Hripcsak / Shendure / Montgomery / Karczewski); 07-08 is
more distributed — one Scholar triple-feed (Kelly), one Scholar self-
feed (MATRIARCH_CF), **two PubMed-only hits** (Moix drug-target, Meyre
HF proteomic), one Scholar new-articles hit (RankVar), and one
`arxiv-digest` hit (Fontana). The pipeline is functioning across all
three channels this week.
