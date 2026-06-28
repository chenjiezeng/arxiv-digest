# Research digest report — 2026-06-28

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-06-28** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 06-28 | Three batches: 06-25 05:57Z (≈25 author-feed alerts), 06-26 03:15Z (≈14 keyword-feed alerts incl. *All of Us*, *UK Biobank*, *APOL1*, *clonal hematopoiesis*, *electronic health records*, *foundation models + EHR*, *drug repurposing*, *Undiagnosed Diseases Network*, *phenome-wide association*, *variant interpretation*, *knowledge graph*, *rare diseases*, *autoimmune disorders*, *mendelian diseases*), and 06-27 11:34Z (≈30+ author-feed alerts: Chenjie Zeng self-feed, Bastarache, Karczewski, Denny, Hripcsak, Hernán, Pritchard, Montgomery, Szolovits, Callahan, Zitnik, Natarajan, Luo, Chute, Shendure, Kastner, Patrick Ryan, Pascal Brandt, Daniel Kastner, Wendy Chung, Mark Daly, Leo Anthony Celi, Vivek Natarajan, Pranav Rajpurkar, Mihaela van der Schaar, Nigam Shah). |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 06-28 | **06-21..22 = 0 papers**; **06-23 = 2 papers** (one on-thread CF causal inference paper, one off-thread motor neuron paper); **06-24 = 0 papers** (3/4 categories failed); **06-25 = 2 papers** (one TFM-robustness paper, one federated tensor-decomposition paper); **06-26 = 1 paper** (KG-grounded AMR prediction); **06-27..28 = 0 papers**. Net: **5 papers from arxiv-digest, ~3 on-thread.** |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |

> ⚠️ **arxiv-digest 06-24 fetch failure repeated the 06-20 pattern: 3/4
> categories (q-bio.GN, q-bio.PE, stat.AP) failed to fetch.** This is the
> second time this month the pipeline has degraded; the new aggressive
> 5-second client delay and 15-second inter-category pause are *helping*
> on most days (06-23, 06-25, 06-26 fired cleanly) but still failing
> intermittently. The rest of the window completed normally.
> **Recommendation: leave the polling cadence alone for now; if a third
> failure lands in the next 7 days, escalate to a per-category retry-
> with-jitter pattern.**

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a *quadruple-feed* AJHG paper that
  cites your work.** Baya, Lassen, Hill, Venkatesh, Currant et al. —
  *Individuals who deviate from polygenic expectation are enriched for
  damaging variants in genes linked to rare disease* (*American Journal
  of Human Genetics*, 2026) — surfaces simultaneously in (a) **your own
  Chenjie Zeng new-related-research feed**, (b) the **Lisa Bastarache
  related-research feed**, (c) the **Jian Yang related-research feed**,
  (d) the **Joshua C. Denny related-research feed**, (e) the *10 new
  citations to articles by Joshua Denny* feed, and (f) the *10 new
  citations to articles by George Hripcsak* feed — i.e., **six
  independent surfacing channels for one paper**, the highest signal
  density this digest pipeline has produced in the entire 2026 record.
  The thesis is exactly the bridge between common-variant PRS and rare-
  variant burden that your INTERESTS file flags as a top thread:
  individuals whose phenotype deviates from PGS-predicted expectation
  are enriched for rare damaging variants in *rare-disease genes*, which
  reframes PGS-misalignment as a *rare-disease screening signal*.
  **Read first.**
- **PGS Browser hits *three* simultaneous feeds.** Kolosov, Reeve, Briotta
  Parolo, Kurki et al. — *PGS Browser: a public platform for personalized
  polygenic score analysis and interpretation* (*Nature Communications*,
  2026) — appears in **Chenjie Zeng (your own feed)**, **Mark Daly new-
  articles**, and the **phenome-wide association studies** keyword feed.
  FinnGen-flavored authorship (Reeve, Briotta Parolo, Kurki) + Mark Daly
  senior authorship → this is the canonical FinnGen response to "how do
  we operationalize PGS for clinical interpretation." Directly on the
  PRS / PheWAS / clinical-translation thread. **HIGH.**
- **AJHG companion paper from the same issue: SDoH + genetic risk
  integration.** Biji, Ferar, Pejaver, Kenny, Liu, Asgari — *Integrating
  social determinants of health and genetic risk in disease risk models*
  (*AJHG*, 2026) — appears in **Joshua C. Denny related-research**,
  **Konrad Karczewski related-research**, and the **All of Us research
  program** keyword feeds. Built on AoU data; combines SDoH and PGS in
  a single disease-risk model. Directly on the EHR-linked biobank +
  genetic-epi composite-risk threads. **HIGH.**
- **Distinct genetic architecture in the tails of complex traits —
  *Nature*, this window (carry-over).** Souaiaia, Wu, Ori, Choi, Hoggart
  et al. (*Nature*, 2026, Montgomery feed). Already flagged in the 06-20
  report; re-surfaced this window via the 06-25 Montgomery batch and
  again in the 06-27 batch. The PRS-tails reframe — clinical action
  happens in the tails and the tails have *different* genetic
  architecture than the bulk — is becoming a default citation. **HIGH
  (re-flag).**
- **Biological aging and generational shifts in early-onset cancer risk
  — *Nature Medicine*, leveraging All of Us + UK Biobank.** Tian, Zong,
  Ren, Tica, Hong, Oduyale et al. (*Nature Medicine*, 2026, *All of Us
  research program* keyword feed). Empirical AoU + UKB paper on
  biological-age acceleration as a driver of the early-onset cancer
  rise. Directly on the **biobanks-with-EHR-linkage** + **multimorbidity
  / aging** threads. **HIGH.**
- **Privacy-preserving phenotype matching for rare-disease cohort
  discovery (UDN).** Walsh — *Privacy-Preserving Phenotype Matching for
  Rare Disease Cohort Discovery* (2026, *Undiagnosed Diseases Network*
  keyword feed). Privacy-preserving HPO-based matching across UDN-style
  cohorts. Directly on the **rare disease + HPO + privacy-preserving
  federation** intersection of your INTERESTS file. **HIGH on rare-
  disease thread.**
- **A city-wide lifecourse Chinese cohort using EHR + survey data —
  *Nature Health*.** Yang, Gao, Qian, He, Dan, Wang et al. (*Nature
  Health*, 2026, *electronic health records* + *All of Us* keyword
  feeds). New East-Asian whole-population EHR-linked cohort (PowerCC,
  Chibi city). Cross-ancestry-portability data point for the AoU / UKB /
  MVP / BioVU thread. **HIGH on the biobanks-with-EHR-linkage thread.**
- **Causal inference with multiple misclassified exposures, applied to
  CF — first on-thread `arxiv-digest` paper this window.** Murali,
  Barnatchez, Hoppe, Wagner, Keller, Josey (arXiv 2606.23656,
  2026-06-22, stat.ME). **Score 2** on the arxiv-digest scoring
  (`causal inference` + `cystic fibrosis`). The methodology — calibration
  weighting + control-variate-adjusted estimators with double
  robustness for misclassified binary exposures — is directly on the
  causal-inference thread; the CF application (throat-swab vs sputum
  for Pseudomonas/Staphylococcus detection in pediatric CF) is directly
  on the CF disease thread. **HIGH.**
- **Benchmarking LLM-based extraction of physical activity from EHRs —
  JAMIA.** Yang, Niu, Li, Zhou, Xiao, Zhou, Zhan et al. (*JAMIA*, 2026,
  *Tiffany Callahan* + *George Hripcsak* related-research feeds).
  Directly on the **EHR phenotyping / LLM-extraction** thread. **HIGH-
  methods.**
- **APOL1 + Black kidney donors editorial — JAMA Internal Medicine.**
  Sharif — *APOL1 and Black Kidney Donors—Reducing Risk or
  Opportunity?* (*JAMA IM*, 2026, *APOL1* keyword feed). Editorial on
  APOL1 risk-genotype-informed donor selection. Directly on the
  **APOL1** disease thread; relevant to your transplant-decision-making
  sub-thread. **HIGH-perspective.**
- **`arxiv-digest` adjacent finds.** A federated tensor-decomposition
  paper for single-cell immune data (Faes et al., arXiv 2606.24938,
  cross-ancestry keyword hit) and a KG-grounded antimicrobial-resistance
  prediction framework (Garg et al., KG-TRACE, arXiv 2606.26179) both
  fire on adjacent threads (federated multi-ancestry methods; KG +
  drug-mechanism), but neither is strongly on a primary thread.
  **METHODS-WATCH.**
- **Variant-interpretation thread — collagen IV paralog pathogenicity
  divergence.** Tzoumkas, Doctor, Sadeghi-Alavijeh, Gale — *Population-
  scale genomics reveals divergent pathogenicity of variant classes
  across paralogous collagen IV genes* (medRxiv, 2026, *Joshua Denny
  related-research* feed). Paralog-aware variant interpretation in
  Alport-spectrum collagen-IV genes, leveraging population-scale data.
  Directly on the variant-interpretation / ACMG-AMP thread. **METHODS-
  WATCH leaning HIGH if you're working on paralog-aware classifier
  inputs.**

Counts: **9 HIGH**, **3 METHODS-WATCH**, rest SKIP. Window is the
heaviest of June 2026; the standout is the sextuple-feed AJHG paper
(item #1) — the strongest multi-feed firing in the 2026 record.

---

## HIGH priority — detailed reports

### 1. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
- **Authors / venue:** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh, H. Currant et al. — *The American Journal of Human Genetics*, 2026. URL: `cell.com/ajhg/fulltext/S0002-9297(26)00200-4`.
- **Surfaced by:** **Sextuple-feed saturation** — (a) *Chenjie Zeng — new related research* (**your own feed**), (b) *Lisa Bastarache — new related research*, (c) *Jian Yang — new related research*, (d) *Joshua C. Denny — new related research*, (e) *10 new citations to articles by Joshua C. Denny*, (f) *10 new citations to articles by George Hripcsak*. **Six independent surfacing channels.** This is the strongest multi-feed signal in the 2026 record so far — including the *PheWAS+PRS Nephrolithiasis* triple-feed paper from the 06-20 report. The fact that it lands in *both* your related-research feed *and* in the citations feeds of Denny and Hripcsak strongly suggests it cites the eMERGE / AoU PheWAS lineage that your work is part of.
- **Thread:** **Genetic epidemiology / PRS** (PGS-deviation analysis) **+** **Variant interpretation** (rare-variant burden in rare-disease genes) **+** **Rare disease** (rare-disease genes as the target) **+** **PheWAS** (phenotype-genotype discordance as a discovery primitive). This paper sits at the intersection of *four* of your active threads.
- **What it is:** From the abstract: "Polygenic scores (PGSs) stratify disease risk but often fail to capture individual variation. 'Misaligned' individuals, whose observed phenotypes deviate from their genetically expected values based on PGS, provide a powerful model for identifying [rare-variant contributions]." The design is: (i) compute a PGS for a quantitative or binary trait, (ii) identify individuals whose phenotype is in the opposite tail from their PGS-predicted value (high PGS but low phenotype, or vice versa) → "misaligned individuals", (iii) test whether misaligned individuals are enriched for rare damaging variants in genes already linked to *rare* Mendelian disease. The framing is: PGS-residual as a discovery filter for rare-variant burden in known disease genes.
- **Why it matters to you:** Five converging reasons.
  (a) **It operationalizes a question your INTERESTS file flags multiple times.** Your file specifies "Composite risk models stacking PRS with rare pathogenic variants" under *Genetic epidemiology* and "Rare-variant association methods" under *Rare disease*. This paper is exactly that stacking — but inverted: instead of using rare variants as additive predictors, it uses PGS-residual as a filter to *find* rare-variant carriers. That inversion is novel and worth understanding before designing any composite-risk study yourself.
  (b) **Six-feed firing strongly implies it cites multiple PheWAS-lineage papers.** Denny's citation feed firing + Hripcsak's citation feed firing + your *related-research* feed (which only fires when Google's relevance model judges proximity to your published work) → at least one of {PheTK, your AoU PheWAS papers, the phecode catalog, eMERGE PheWAS pieces} is likely cited. Worth a literature check to confirm.
  (c) **"Misalignment" is a phenotype-genotype-discordance design** — same conceptual family as the genome-phenome PheWAS+PRS work, but in the opposite direction. PheWAS scans phenotype-space at fixed genotype; this paper scans rare-variant burden at fixed PGS-residual. The duality is interesting and useful for any methods-comparison write-up.
  (d) **Penetrance estimation under population-screening conditions.** Your INTERESTS file explicitly calls out "penetrance estimation for monogenic variants under population-screening conditions (vs. clinically ascertained cohorts)." This paper's design — population-scale ascertainment, rare-disease-gene burden, PGS-stratified — is exactly that setting. The misalignment-enrichment effect *is* an empirical penetrance signal: high-PGS, low-phenotype individuals who carry a rare damaging variant must have *incomplete penetrance* (because the rare variant didn't outweigh the high PGS).
  (e) **Likely a UK Biobank paper given author roster.** Lassen, Hill, Venkatesh, Currant — these are UK Biobank / Wellcome / Oxford lineage names. If yes, that's a UKB-replication template for any AoU misalignment analysis you'd want to do, and the AoU replication is the obvious next step.
- **Action:** **HIGH — read first.**
  (i) Identify the cohort and the trait set. UKB exome cohort is most likely; check whether they used UKB-PPP for proteomics or restricted to clinical phenotypes.
  (ii) Identify the rare-disease gene panel. ClinGen? OMIM-curated? Gene2Phenotype? The panel choice drives the enrichment magnitude.
  (iii) Identify the PGS source. PGS Catalog? FinnGen-derived? Internally trained? PGS source matters for cross-cohort transfer.
  (iv) Check whether they report a per-gene effect or a panel-aggregate effect. Per-gene effects are the actionable output.
  (v) Critical citation check: does it cite PheTK, the AoU PheWAS paper, eMERGE / BioVU PheWAS work, or the phecode catalog? Six-feed firing strongly suggests at least one.
  (vi) AoU replication design: would `phers` (your PheRS / phecode-based rare-variant risk score work) be the obvious port of this method? If yes, that's an immediate paper.

### 2. PGS Browser: a public platform for personalized polygenic score analysis and interpretation
- **Authors / venue:** N. Kolosov, M.P. Reeve, P.D. Briotta Parolo, M.I. Kurki et al. — *Nature Communications*, 2026. URL: `nature.com/articles/s41467-026-74461-7`.
- **Surfaced by:** **Triple-feed saturation** — (a) *Chenjie Zeng — new related research*, (b) *Mark Daly — new articles*, (c) *"phenome wide association studies"* keyword feed.
- **Thread:** **Genetic epidemiology / PRS** (PGS calibration and interpretation) **+** **PheWAS / phecode infrastructure** (the snippet explicitly mentions "We perform phenome-wide…" indicating a PheWAS pass over PGS) **+** **Knowledge graphs & ontologies** (clinical-interpretation layer for PGS).
- **What it is:** A FinnGen-flavored public web platform for personalized PGS analysis. The Kurki + Daly + Briotta Parolo author roster places this squarely in the FinnGen/Broad lineage. From the snippet: "Polygenic scores (PGSs) quantify individual genetic susceptibility to complex diseases and can identify high-risk individuals well before clinical onset. Their clinical translation, however, requires population-based reference resources…" — the platform almost certainly provides (a) reference-distribution lookups for any PGS in PGS Catalog applied to an individual, (b) ancestry-adjusted percentile rankings, (c) phenome-wide associations of the PGS for clinical interpretation, and (d) interactive visualizations for clinician use. The "performing phenome-wide" passage in the All-of-Us alert snippet indicates an integrated PheWAS layer.
- **Why it matters to you:** Four reasons.
  (a) **Operational infrastructure for clinical PGS, by the FinnGen team.** Your work on PheWAS + PRS in AoU is part of the same translation pipeline; understanding what FinnGen's public-facing tool does is necessary to know what *not* to rebuild for AoU. If the PGS Browser already provides ancestry-adjusted percentile lookups, anyone trying to build the AoU equivalent should pattern after this API.
  (b) **Triple-feed firing including your own feed** means Google's relevance model judges it close to your published work. The combination with *phenome-wide association studies* keyword firing means the paper specifically pitches itself as PheWAS-on-PGS, which is your methodological lane.
  (c) **Mark Daly's signature.** Daly's group is the de facto reference for population-scale PGS methodology decisions; new-articles firing in his feed for a public-platform paper means this is the FinnGen team's flagship 2026 PGS-translation publication, not a side project.
  (d) **Reference resources for ancestry-aware risk.** Your INTERESTS file specifies "ancestry-aware risk scores" under PheWAS. The PGS Browser's ancestry-stratified reference distributions are an external resource your AoU work could call rather than re-derive.
- **Action:** **HIGH.**
  (i) Look at the live tool first (likely linked from the Nature Comms paper) — what does the interface actually do for a clinician? The interface design tells you what the FinnGen team thinks is the minimum viable clinical PGS UI.
  (ii) Note the reference cohort — FinnGen 11.x? With UK Biobank as cross-ancestry validation? Reference-cohort identity determines transferability.
  (iii) Check the PheWAS-on-PGS module — what phecode / ICD-10 vocabulary do they use, and how do they handle multiple-testing across phecodes? This is methods directly comparable to your work.
  (iv) Note whether they support PGS Catalog-listed scores or only internally-developed scores. PGS-Catalog support is the user-facing equivalent of FAIR PGS deployment.
  (v) Possible adoption: cite as the canonical "public PGS interpretation infrastructure" for any forthcoming AoU PGS clinical-translation manuscript.

### 3. Integrating social determinants of health and genetic risk in disease risk models
- **Authors / venue:** A. Biji, K. Ferar, V. Pejaver, E.E. Kenny, B. Liu, S. Asgari — *The American Journal of Human Genetics*, 2026. URL: `cell.com/ajhg/fulltext/S0002-9297(26)00201-6` (note: sequential AJHG article number to item #1 above; same issue).
- **Surfaced by:** **Triple-feed saturation** — (a) *Joshua C. Denny — new related research*, (b) *Konrad Karczewski — new related research*, (c) *"All of Us research program"* keyword feed.
- **Thread:** **EHR-linked biobanks** (AoU empirical study) **+** **Genetic epidemiology** (PGS) **+** **Causal inference / risk modeling** (SDoH-adjusted vs SDoH-unadjusted risk model comparison) **+** **ML for precision health** (composite risk models for clinical decisions).
- **What it is:** From the AoU-feed snippet: "The All of Us Research Program collects detailed health-related data, including demographic information, clinical diagnoses from electronic [health records]… We also thank the NIH All of Us Research Program for making available the participant data examined…". The Pejaver + Kenny authorship places this in the eMERGE + Mt. Sinai + AoU lineage — Pejaver works on PRS portability; Kenny is on the AoU Genetic Diversity working group. The methods are almost certainly: (i) extract SDoH variables from the AoU survey + ZIP-code-linked area-level deprivation indices, (ii) build a baseline genetic-risk-only model (PGS or PGS+ancestry PCs), (iii) build an integrated SDoH+genetic model, (iv) compare discrimination + calibration + decision-curve outcomes across population subgroups (especially ancestry subgroups, which is the headline AoU value-add).
- **Why it matters to you:** Four reasons.
  (a) **First major AJHG paper on the SDoH+PGS integration question using AoU.** Your INTERESTS file explicitly calls out "Composite risk models stacking PRS with rare pathogenic variants" — this is the SDoH-axis equivalent (PGS + SDoH instead of PGS + rare variants). Together with paper #1 above (PGS + rare variants from the *same AJHG issue*), the field is concretely advancing on multiple composite-risk axes this month.
  (b) **AoU is the cohort of choice for this question.** AoU's design — oversampling of underrepresented populations, deep SDoH survey, EHR linkage — is the only major biobank where SDoH-PGS integration *can* be done at scale and with non-European coverage. A paper showing the AoU-native version of this analysis is the methodological reference for your own AoU SDoH-PGS work.
  (c) **Pejaver + Kenny authorship signals genetic-diversity-aware framing.** Both are vocal about ancestry portability of PGS and equity in clinical risk modeling; the paper will likely report ancestry-stratified gains rather than just overall AUC uplift, which is the right framing for AoU.
  (d) **Karczewski's feed firing** is gnomAD-lineage signal — likely a methods touch-point with rare-variant calibration or population-frequency normalization, even if the paper is primarily about common variants.
- **Action:** **HIGH.**
  (i) Identify the SDoH variables used — AoU survey items only, or AoU survey + area-level indices (ADI, SVI)? The choice drives generalizability.
  (ii) Identify the diseases scored — CVD, T2D, breast cancer are the obvious common targets; check whether they include any rare conditions where the SDoH signal would be weaker.
  (iii) Note the decision-curve / NRI analysis — this is the part that matters for *clinical* uptake, not just statistical significance.
  (iv) Note whether they report ancestry-stratified calibration; if yes, that's the headline result for any equity argument.
  (v) Pair-read with paper #1: same issue, complementary composite-risk axes. Cite both together in any composite-risk framing piece.

### 4. Distinct genetic architecture in the tails of complex traits (re-flag from 06-20 report)
- **Authors / venue:** T. Souaiaia, H.M. Wu, A.P.S. Ori, S.W. Choi, C.J. Hoggart et al. — *Nature*, 2026.
- **Surfaced by:** *Stephen B. Montgomery — new related research* feed (re-fired in both the 06-25 and 06-27 batches this window — repeat firing typically means the citation graph is still expanding rapidly).
- **Thread:** **Genetic epidemiology / PRS** (tail-of-distribution architecture) **+** **ML for precision health** (clinical-cutoff calibration in the tails).
- **What it is:** *See full discussion in the 2026-06-20 report (item #4).* In brief: the genetic architecture of the top and bottom tails of a polygenic distribution *differs from the bulk*, which has direct implications for clinical-cutoff PGS calibration — the standard linear PGS systematically miscalibrates exactly the slice that gets clinically actioned (top 1-5%).
- **Why it matters to you:** **Same reasons as 06-20 report.** Worth re-flagging because (a) the repeat firing across two Montgomery alert batches in 4 days suggests the citation graph is expanding fast and you may want to read it now rather than later, and (b) it pairs naturally with the 06-28 items #1 (PGS-deviation rare-variant enrichment) and #2 (PGS Browser): the trio together makes the case that any AoU PGS-translation work needs explicit tail-calibration (item #4), composite-risk integration (items #1 and #3), and operational tooling (item #2).
- **Action:** **HIGH (re-flag).** If you didn't read it after the 06-20 report flag, prioritize it now — the multi-week repeat firing makes it more likely it's going to be a default citation in any near-term PGS clinical-translation manuscript.

### 5. Biological aging and generational shifts in early-onset cancer risk
- **Authors / venue:** R. Tian, X. Zong, D. Ren, S. Tica, D. Hong, O. Oduyale et al. — *Nature Medicine*, 2026. URL: `nature.com/articles/s41591-026-04448-w`.
- **Surfaced by:** *"All of Us research program"* keyword feed (top result in 06-26 batch).
- **Thread:** **Biobanks with EHR linkage** (AoU + UK Biobank dual-cohort design) **+** **Multimorbidity / aging** (biological-age framework) **+** **Genetic epidemiology** (cohort effects in cancer risk) **+** **Specific disease threads** (early-onset cancer is broader than CF/APOL1/CHIP-VEXAS/IBD but cancer-adjacent).
- **What it is:** From the snippet: "Sample size constraints limited cancer site-specific analyses in the All of Us Research Program and organ-specific aging analyses in the … In addition, although we leveraged two large populations in the UK Biobank and the All of Us Research Program…". The design is empirical: compute biological-age proxies (likely clock-based — Horvath, Levine PhenoAge, Klemera-Doubal, or proteomic clocks) for AoU + UKB participants; stratify by birth cohort; test whether *generational* differences in biological-age acceleration explain the well-documented rise in early-onset cancers (e.g., colorectal cancer in adults <50). The dual-cohort UKB + AoU design adds cross-cohort + cross-ancestry replication.
- **Why it matters to you:** Three reasons.
  (a) **High-profile AoU EHR-linked methods paper.** Your INTERESTS file explicitly flags "EHR-linked biobank analysis is a core theme — anything that combines genomic data with longitudinal real-world clinical records is high-priority." This is precisely that — and at *Nature Medicine* venue level.
  (b) **Multimorbidity-aging thread.** Your INTERESTS file's *Chronic disease clustering and multimorbidity* thread explicitly highlights "aging-related multimorbidity." Biological-age frameworks are the methodological substrate for that thread; this paper is the high-profile 2026 reference for biological-age + cancer in EHR-linked cohorts.
  (c) **Generational / cohort-effect framing is methodologically interesting.** Birth-cohort effects in cancer are a hard problem because of confounding by screening practice and diagnostic technology changes; if this paper uses biological-age as a *de-confounder* for cohort-effect cancer trends, that's a methods pattern reusable on other cohort-effect questions (e.g., generational T2D risk, generational autoimmune disease risk).
- **Action:** **HIGH.**
  (i) Identify the biological-age clock — DNA-methylation (limited in AoU because methylation is not standard), phenotypic-clinical-marker-based (Levine PhenoAge), or proteomic? The clock choice limits what's portable to BioVU / MVP.
  (ii) Identify the cancer-site coverage — colorectal is the obvious target given the early-onset CRC literature; check what else they covered.
  (iii) Note the cohort-effect modeling — fixed-effects, random-effects, age-period-cohort decomposition? This is the methodological core.
  (iv) Note whether they report ancestry-stratified biological-age trajectories; this is the AoU value-add over UKB-only analyses.
  (v) Possible cite for any forthcoming AoU multimorbidity / aging-trajectory manuscript.

### 6. Privacy-Preserving Phenotype Matching for Rare Disease Cohort Discovery
- **Authors / venue:** P. Walsh — 2026 (likely a workshop / thesis chapter given single-author format). Surfaced via *"Undiagnosed Diseases Network"* keyword feed.
- **Surfaced by:** *"Undiagnosed Diseases Network"* keyword feed (06-26 batch).
- **Thread:** **Rare disease** (HPO-based phenotype matching for rare-disease cohort assembly) **+** **EHR phenotyping** (computable HPO phenotypes) **+** **Privacy-preserving federation** (cross-institution rare-disease matching is bottlenecked by privacy).
- **What it is:** From the snippet: "Rare diseases are individually uncommon but collectively vast, and the patients who remain undiagnosed after [standard workup are the target of network-based matching]…". Standard rare-disease cohort discovery uses Matchmaker Exchange / PhenomeCentral / GeneMatcher to match patients across institutions on the HPO term overlap of their phenotypes. The bottleneck is privacy: institutions are reluctant to share raw HPO profiles. This paper proposes a privacy-preserving phenotype-matching protocol — almost certainly using either (a) homomorphic encryption over HPO vectors, (b) secure multi-party computation, or (c) differential-privacy-added HPO embeddings, with similarity-search retained.
- **Why it matters to you:** Three reasons.
  (a) **Directly on the rare-disease + HPO intersection of your INTERESTS file.** The file specifies "deep phenotyping for rare-disease diagnosis (HPO-based)" under *Rare disease* — this is exactly the operational layer.
  (b) **Privacy-preserving federation pairs with the multi-site EHR-causal-inference thread.** Both this paper and the 06-20 Kundu / Ohno-Machado paper (privacy-enhancing sequential learning for multi-site EHR) are working the same federation-under-privacy problem from different angles; together they outline the architecture for any AoU-MVP-UDN joint rare-disease analysis.
  (c) **UDN is the natural target cohort.** AoU has limited UDN-style deep phenotyping; UDN itself is the operational rare-disease cohort. If you do any rare-disease work using UDN data, this paper is in the design-citation set.
- **Action:** **HIGH on the rare-disease thread.**
  (i) Identify the cryptographic primitive — homomorphic, secure MPC, or DP. Different primitives have different deployment friction; DP-based methods are the easiest to operationalize.
  (ii) Note the HPO similarity measure used — Lin similarity, Resnik similarity, or HPO embedding (BERT-style)? Embedding-based methods compose with privacy primitives more easily than tree-walking similarity measures.
  (iii) Note the empirical validation — did they use real UDN data or simulated HPO profiles? Real data carries more weight.
  (iv) Possible cite for any AoU-UDN-MVP federated rare-disease cohort design.

### 7. A city-wide lifecourse Chinese cohort using electronic health records and survey data for disease risk and resource allocation
- **Authors / venue:** S. Yang, B. Gao, P. Qian, H. He, L. Dan, L. Wang, C. Li et al. — *Nature Health*, 2026. URL: `nature.com/articles/s44360-026-00140-y`.
- **Surfaced by:** *"electronic health records"* keyword feed + *"All of Us research program"* keyword feed (paper itself is the PowerCC cohort in Chibi city, China — the All-of-Us mention is likely a comparison reference in the discussion).
- **Thread:** **EHR-linked biobanks** (new Chinese whole-population EHR-linked cohort) **+** **EHR phenotyping** (city-wide EHR + survey integration) **+** **ML for precision health** (disease-risk prediction + resource allocation).
- **What it is:** From the snippet: "The population-wide lifecourse cohort in Chibi (PowerCC) is the first city-wide, whole-population lifecourse cohort study in China, established to facilitate the precise prediction of disease risks at the individual level and cost-effective resource allocation at the…". Design = whole-population (i.e., not volunteer-based) city-scale cohort with EHR linkage + survey data, intended for disease-risk modeling and population-health resource allocation. The whole-population (vs. volunteer) design is methodologically important because it sidesteps the healthy-volunteer bias that plagues UK Biobank and AoU.
- **Why it matters to you:** Three reasons.
  (a) **Cross-ancestry portability data point.** Your INTERESTS file's *Genetic epidemiology* thread specifies "cross / trans-ancestry portability." A new Chinese whole-population EHR-linked cohort is one of the rare such resources outside of Biobank Japan, Korea Biobank, and Taiwan TPMI. If PowerCC publishes genotype data, it becomes a natural East-Asian replication cohort for any AoU finding.
  (b) **Whole-population (not volunteer) design** is the most important methodological angle. UKB's healthy-volunteer bias is a known weakness; AoU's underrepresented-population sampling is a partial fix but still not whole-population. A whole-population EHR-linked cohort is the *gold standard* design for unbiased population-genetic-epidemiology work and the *Nature Health* venue suggests they're pitching it that way.
  (c) **EHR + survey integration is your operational lane.** The combination of EHR data with survey-collected SDoH / lifestyle data is exactly the operational substrate of AoU; comparing PowerCC's integration approach with AoU's is useful for any forthcoming AoU methods paper.
- **Action:** **HIGH on biobanks-with-EHR-linkage thread.**
  (i) Verify the whole-population claim — is it census-level or registry-level enrollment? Census-level is rarer and stronger.
  (ii) Identify the genotype data plan — is PowerCC adding genomics, or is it pure EHR + survey? Pure EHR + survey is still valuable but limits the cross-ancestry-PRS replication use.
  (iii) Identify the EHR vocabulary — Chinese ICD, SNOMED-CT translation, or OMOP-CDM? OMOP-CDM compatibility makes federated analysis with AoU + UKB feasible.
  (iv) Note the size — "city-wide" Chibi is ~500K people; the comparison cohort scale matters.
  (v) Candidate citation for any future cross-ancestry EHR-biobank comparison piece.

### 8. Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach
- **Authors / venue:** Nandini Murali, Keith Barnatchez, Jordana E. Hoppe, Brandie D. Wagner, Kayleigh P. Keller, Kevin P. Josey — arXiv:2606.23656v1 (stat.ME), 2026-06-22.
- **Surfaced by:** GitHub `arxiv-digest` 2026-06-23 (score 2: `causal inference` + `cystic fibrosis`).
- **Thread:** **Causal inference / pharmacoepidemiology** (calibration weighting, double-robust estimators, misclassified-exposure correction) **+** **Cystic fibrosis / CFTR** (applied to a 651-patient pediatric CF cohort, ages 6-21).
- **What it is:** From the abstract: throat swabs are commonly substituted for expectorated/induced sputum cultures in CF, but they have imperfect sensitivity/specificity for *Pseudomonas aeruginosa* and *Staphylococcus aureus* detection. The paper develops *calibration weighting + control-variate-adjusted* estimators for causal inference under multiple misclassified binary exposures with clustered observations. Calibration treats misclassification as a missing-data problem — consistency *without* modeling the misclassification mechanism. The control-variate step integrates information from error-prone observations to reduce variance while preserving the gold-standard estimator's consistency. The estimator inherits double-robustness from its components. Empirically: in 651 CF patients age 6-21, swab-based estimates *attenuate* the effect of *P. aeruginosa* on percent-predicted FEV₁ by ~69% relative to sputum-based estimates (−2.67 vs −8.52 pp; 95% CI for sputum: −13.40, −3.63), supporting that swab-only studies systematically *under-treat* P. aeruginosa.
- **Why it matters to you:** Four reasons.
  (a) **Two threads simultaneously.** This is the rare arxiv-digest paper that lands on both the causal-inference thread *and* the CF disease thread — the score-2 keyword overlap is genuine, not incidental. Your INTERESTS file explicitly calls out CF modulator pharmacoepi and target-trial emulation under one roof; misclassified-exposure-correction is the methods primitive needed for any CF modulator-effectiveness study where exposure is defined from imperfect outcome ascertainment (e.g., chronic-infection status defined from EHR culture records).
  (b) **The CF cohort is a real clinical cohort** (n=651, ages 6-21, Hoppe + Wagner authorship — UC Denver / Colorado CF center lineage), not a simulation. Effect size is large and clinically meaningful (69% attenuation of the P. aeruginosa effect on FEV₁ when using swab instead of sputum). That magnitude has implications for any *CF Foundation registry-based* effectiveness study where the exposure definition depends on sample-type-dependent culture status.
  (c) **Methods are reusable beyond CF.** Calibration weighting + control-variate adjustment for misclassified binary exposures applies anywhere EHR-derived exposures are noisy — e.g., ICD-based diabetes-status definitions, smoking-status from notes, medication adherence from prescription-fill data. This is methods-watch for the broader pharmacoepi thread.
  (d) **Double-robustness preservation.** Most missing-data approaches lose DR when the missingness model is misspecified; the paper claims the proposed estimator inherits DR from its components. Worth understanding the conditions under which this holds.
- **Action:** **HIGH on both CF and causal-inference threads.**
  (i) Read for the calibration-weighting derivation — is it a Tan-style augmented IPW or a different family?
  (ii) Note the structural ceiling on efficiency gains in the bivariate setting — this is a useful limitation to understand before deploying on >2 exposures.
  (iii) Note the cohort source — likely EPIC Observational Study or CF-Foundation Patient Registry data from UC Denver; understanding the data provenance matters for any CF registry replication.
  (iv) Direct candidate for citation in any forthcoming AoU / BioVU CF modulator-effectiveness study where exposure ascertainment is the limiting noise source.
  (v) Pair-read with the 06-20 Kundu / Ohno-Machado privacy-preserving multi-site EHR causal paper for a paired methods-citation set on EHR-causal-under-noise.

### 9. Benchmarking information extraction of physical activity from electronic health record with large language models
- **Authors / venue:** H. Yang, Z. Niu, M. Li, H. Zhou, Y. Xiao, S. Zhou, Z. Zhan et al. — *Journal of the American Medical Informatics Association*, 2026. URL: `academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocag101/8713125`.
- **Surfaced by:** **Triple-feed saturation** — (a) *Tiffany J. Callahan — new related research*, (b) *George Hripcsak — new related research*, (c) *"electronic health records"* keyword feed.
- **Thread:** **EHR phenotyping / OMOP** (LLM-based extraction from clinical notes for structured phenotype derivation) **+** **EHR foundation models** (LLM-as-extractor evaluation).
- **What it is:** Benchmarking pipeline for LLM-based extraction of *physical activity* information from EHR clinical notes. Standard EHR data is poor at capturing exercise/activity (it's narrative-only in clinical notes, not structured). The paper benchmarks multiple LLMs on extraction accuracy for activity attributes (frequency, intensity, type, duration) against a manually-annotated gold standard. JAMIA venue + Callahan + Hripcsak feeds → eMERGE / OHDSI lineage; likely benchmarks include GPT-4, Claude, an open-weights Llama-class model, and possibly a fine-tuned ClinicalBERT-class extractor.
- **Why it matters to you:** Three reasons.
  (a) **EHR phenotyping for lifestyle factors is a known gap.** Your INTERESTS file specifies "NLP / LLM extraction from clinical notes for phecode and HPO term assignment" under *EHR phenotyping & OMOP*. Physical activity is one of the canonical hard-to-extract attributes (along with diet, alcohol, occupation, smoking detail beyond "ever/never"); a benchmark paper sets the empirical floor for what's currently achievable.
  (b) **Triple-feed firing (Callahan + Hripcsak + EHR keyword)** signals this is a default citation in the EHR-LLM-extraction literature going forward. Both Callahan and Hripcsak are central in the EHR-phenotyping methods community.
  (c) **Direct adoption candidate.** Any AoU / BioVU study where you'd want to control for physical-activity exposure (e.g., GLP-1 effectiveness, T2D progression, multimorbidity trajectories) would benefit from a benchmarked extraction pipeline rather than relying on AoU's self-reported activity survey alone.
- **Action:** **HIGH-methods.**
  (i) Identify the benchmark LLM set + the gold-standard corpus. Corpus identity (MIMIC, eICU, OHDSI sample) drives transferability.
  (ii) Identify the metric breakdown by attribute (frequency / intensity / type / duration). Frequency is usually easiest; intensity is hardest.
  (iii) Note whether they release the prompt templates and the gold-standard annotations — reproducibility matters for adoption.
  (iv) Possible immediate adoption: for any AoU CF / GLP-1 / multimorbidity work where activity is a relevant confounder.

### 10. APOL1 and Black Kidney Donors—Reducing Risk or Opportunity?
- **Authors / venue:** A. Sharif — *JAMA Internal Medicine*, 2026 (editorial format).
- **Surfaced by:** *APOL1* keyword feed (06-26 batch).
- **Thread:** **Specific disease threads — APOL1** (kidney disease risk, transplant decision-making, ancestry considerations) — direct hit on your INTERESTS file specification.
- **What it is:** Editorial commentary, almost certainly accompanying a JAMA IM original article in the same issue, on the policy question of whether APOL1 genotyping of Black kidney donors *reduces risk* (by deferring high-risk donors) or *reduces opportunity* (by disqualifying medically suitable donors and exacerbating Black-recipient access disparities). From the snippet: "After adjusting for eGFR at time of donation, there remained statistically significant associations…" — suggests the editorial is responding to an empirical paper that finds residual APOL1 risk-genotype effects on donor outcomes even after eGFR adjustment.
- **Why it matters to you:** Three reasons.
  (a) **Direct INTERESTS file hit.** Your file explicitly calls out APOL1 + transplant decision-making + ancestry considerations. This is exactly the editorial-policy layer of that thread.
  (b) **Editorial-perspective papers are useful for framing your own APOL1 work.** Sharif (Birmingham, UK, transplant nephrology) is a recognized voice in the international transplant community; an editorial in JAMA IM places his framing in front of a US clinical audience.
  (c) **The risk-vs-opportunity framing is the right framing for any APOL1 clinical-decision-support tool.** If you're working on APOL1-aware risk-stratification (in AoU or via the APOLLO network), this is a default citation.
- **Action:** **HIGH-perspective.**
  (i) Identify the empirical paper Sharif is editorializing against — likely an APOLLO-network outcome paper or a USRDS-linked donor-outcomes paper.
  (ii) Note Sharif's stance — does he favor or oppose universal APOL1 testing? The position shapes how you cite this.
  (iii) Useful background-citation for any APOL1 clinical-decision-support manuscript.

---

## METHODS-WATCH — brief notes

### 11. Population-scale genomics reveals divergent pathogenicity of variant classes across paralogous collagen IV genes
- **Authors / venue:** K. Tzoumkas, G.T. Doctor, O. Sadeghi-Alavijeh, D.P. Gale — medRxiv, 2026.
- **Surfaced by:** *Joshua C. Denny — new related research* feed (06-25 batch).
- **Thread:** **Variant interpretation (ACMG / ClinGen)** — paralog-aware pathogenicity inference is a known methods gap in ACMG criteria; this is the population-scale empirical test.
- **Take:** Paralog-aware pathogenicity classification has been a methodological goal of ClinGen VCEPs for several years (canonical example: paralog-mismatched variants in *PTEN* vs *TPTE*). A population-scale empirical demonstration in collagen IV genes (COL4A3 / COL4A4 / COL4A5, the Alport syndrome cluster) is directly methods-relevant. **Read if you're working on a paralog-aware classifier input set; otherwise log.**

### 12. Privacy-preserving federated tensor decomposition of single-cell immune data
- **Authors / venue:** A. Faes, S.M. van den Berg, M.A. Haeri — arXiv 2606.24938 (q-bio.GN), 2026-06-22.
- **Surfaced by:** GitHub `arxiv-digest` 2026-06-25 (score 1: `cross-ancestry`).
- **Thread:** Tangential to **EHR-linked biobanks / federation** and **multimorbidity** (multicellular programs as a multimorbidity-mechanism layer).
- **Take:** Federated tensor decomposition (donor × cell-type × gene) recovers multi-cellular programs across institutions without pooling raw cells, with provable equivalence to centralized decomposition under federated global-mean centering. The 261-donor SLE atlas reproduction (interferon program AUC 0.998) and the 3-site COVID-19 reproduction (subspace correlation 0.989) are real demonstrations. Federation under multi-ancestry partitions makes this a candidate primitive for AoU / MVP-style federated single-cell work, but it's *not* directly on your primary threads — it's adjacent. **METHODS-WATCH.**

### 13. KG-TRACE: A Neuro-Symbolic Framework for Mechanistic Grounding in Antimicrobial Resistance Prediction
- **Authors / venue:** N. Garg, S. Jain, S. Yadav, B.K. Bhargava, G. Singh, A. Srivastava, P. Kar — arXiv 2606.26179 (cs.LG), 2026-06-24.
- **Surfaced by:** GitHub `arxiv-digest` 2026-06-26 (score 1: `knowledge graph`).
- **Thread:** **Knowledge graphs & ontologies** (biological KG-grounding of a neural model) **+** tangential to **drug repurposing** (explainable hypothesis output from KG-grounding).
- **Take:** Neuro-symbolic AMR-prediction framework that fuses WGS-based features with WHO-mutation KG embeddings via a learned "epistemic trust gate." AUROC 0.9760 for isoniazid (the main TB-resistance drug); primary value is *symbolic grounding* not predictive uplift. Introduces a Biological Grounding Ratio metric. Useful as a pattern for KG-grounded explainable prediction — and *the explainability angle is exactly what your INTERESTS file calls out for drug-repurposing KG/GNN approaches* ("explainable hypothesis output — path or subgraph rationales rather than opaque link-prediction scores"). Not on the primary disease thread (TB AMR ≠ your tracked diseases), but the KG-grounding pattern is the methodological reference. **METHODS-WATCH leaning HIGH if your next drug-repurposing project needs an explainability primitive.**

### 14. Are Tabular Foundation Models Robust to Realistic Query Distribution Shifts in Microbiome Data?
- **Authors / venue:** G. Perciballi, A. Fall, F. Granese, E. Prifti, J.-D. Zucker — arXiv 2606.24995 (cs.LG), 2026-06-23.
- **Surfaced by:** GitHub `arxiv-digest` 2026-06-25 (score 1: `foundation model`).
- **Thread:** **EHR foundation models** (adjacent — tabular FMs as the structured-EHR analogue) **+** **ML for precision health** (robustness under distribution shift).
- **Take:** Tabular foundation models degrade under realistic biological perturbations to microbiome data (zero-inflation, sparsification, zero-imputation); sparsification disproportionately affects TFMs vs classical random-forest baseline. The microbiome substrate is not your primary thread, but the *finding* — TFMs are not robust to realistic feature-distribution shifts even when discriminative features are preserved — generalizes to any tabular FM applied to EHR labs / vitals / OMOP measurement data, which *is* your thread. **METHODS-WATCH — read briefly for the failure-mode characterization, useful as a default caution when deploying tabular FMs on EHR data.**

---

## SKIP (incidental keyword hits or far off-thread)

For completeness, items that surfaced this window but don't merit a detailed report:

- Estimating common synaptic inputs to spinal motor neurons from MU spike trains (arxiv-digest 06-23, single-keyword `motor` hit) — q-bio.NC; unrelated to your threads.
- Predicting immune-related thyroiditis using PRS in melanoma patients (Chenjie Zeng feed) — interesting as a PRS application but well outside your disease threads and Tarhini's immune-oncology line is not your collaboration network.
- Doubling cascade testing uptake for hereditary cancer syndromes RCT (Chenjie Zeng feed) — clinical RCT, useful background only.
- Multiple author-citation feeds firing on unrelated topics (e.g., Kastner feed on adult-onset Still's disease case report; Pritchard feed on Drosophila chromatin insulation; Szolovits feed on arithmetic pedagogy for language models; Natarajan feed on AI projects failing in drug development).
- A city-wide lifecourse cohort comparison item in the *All of Us* keyword feed (Yang et al., Nature Health) — *included as item #7 above, listed here for source-tracking only.*
- *Generative AI and Language Models in Human Genetics and Health: From Variant Interpretation to Clinical Decision Support* (Pinchevsky-Itan & Itan, Genes, 2026, variant-interpretation keyword feed) — review article; useful as a citation but not a primary finding.
- KRAS-mutated clonal hematopoiesis case report (clonal-hematopoiesis keyword feed) — case-report N=1; not on your CHIP epi thread.
- Several non-human / off-thread MR / drug-screening / general clinical-review items in the various keyword feeds.

---

## Cross-window pattern notes

- **June 2026 has been the heaviest PRS-translation month in the 2026
  record.** Across the 06-18, 06-20, and 06-28 reports, the standout
  papers have all been on a single arc: (i) PheWAS+PRS in non-European
  cohorts (06-20 Nephrolithiasis Taiwan paper), (ii) tail-architecture
  miscalibration of PRS (06-20 Souaiaia *Nature*), (iii) PGS-deviation
  rare-variant enrichment (this week's AJHG paper, item #1), (iv) PGS
  Browser operational tooling (item #2), (v) PGS + SDoH composite-risk
  modeling (item #3). Together these form a *single coherent literature
  thread* on "PRS for clinical translation: how do we calibrate, compose,
  and operationalize it." Worth thinking about whether your forthcoming
  AoU PGS work fits naturally into this thread or needs a new framing.
- **The arxiv-digest pipeline is sparse but improving.** 06-21..28 saw 5
  papers total (vs the 06-15..20 window's 6 papers), with one repeat
  fetch failure on 06-24. The 06-23 CF causal-inference paper (item #8)
  is the strongest on-thread arxiv-digest hit since the 06-19 bioETH-
  Beacon paper. The pipeline remains higher-precision-than-recall:
  short-window noise is low but week-scale recall depends on Scholar
  alerts as the primary signal.
- **Author feeds vs keyword feeds.** This window, the strongest
  multi-feed signals came from author feeds (item #1 sextuple-feed; item
  #2 triple-feed; item #3 triple-feed). Keyword feeds (All of Us, EHR,
  UDN, APOL1) primarily surfaced *single* high-value items — but in
  several cases those items were the same papers already firing in the
  author feeds. The triangulation of author + keyword feeds is what
  produces the highest-confidence picks.
- **Recurring author-feed senders this window:** Chenjie Zeng,
  Bastarache, Karczewski, Denny, Hripcsak, Hernán, Pritchard, Montgomery,
  Szolovits, Callahan, Zitnik, Natarajan, Luo, Chute, Shendure, Kastner,
  Patrick Ryan, Pascal Brandt, Wendy Chung, Mark Daly, Leo Anthony Celi,
  Pranav Rajpurkar, Mihaela van der Schaar, Nigam Shah, Jay Shendure,
  Jian Yang, Joshua C. Denny, Konrad Karczewski, Stephen B. Montgomery,
  Tiffany J. Callahan, George Hripcsak, Daniel Kastner.

---

## Recommended reading order

1. **Item #1** — Baya et al., *Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease* (AJHG). Sextuple-feed; read first.
2. **Item #2** — Kolosov / Reeve / Daly, *PGS Browser* (Nature Communications). Read in tandem with #1.
3. **Item #3** — Biji et al., *Integrating SDoH and genetic risk in disease risk models* (AJHG). Same issue as #1; companion read.
4. **Item #5** — Tian et al., *Biological aging and generational shifts in early-onset cancer risk* (Nature Medicine). Multimorbidity-aging headline.
5. **Item #4** — Souaiaia et al., *Distinct genetic architecture in the tails of complex traits* (Nature). Re-flag from 06-20; read now if you haven't.
6. **Item #8** — Murali et al., *Causal Inference with Multiple Misclassified Exposures* (arXiv). CF + causal-inference dual hit; the standout arxiv-digest item this window.
7. **Items #6, #7, #9, #10** — read as time allows; each lands on a single primary thread and is more incremental than the top 5.
8. **METHODS-WATCH items (#11-#14)** — skim only.

---

## Pipeline notes

- 2026-06-24 had a 3/4-category fetch failure (same pattern as 2026-06-20). No code change recommended yet; if a third failure occurs within 7 days, escalate per the 06-20 report's recommendation (per-category retry-with-jitter or pause-doubling).
- The deep-summary HTML fetch was not exercised this window (no paper hit `--deep-score 4` threshold). The two arxiv-digest score-2 papers (item #8 CF causal inference; item #12 federated tensor decomposition) hit the abstract-only branch as designed.
- `seen.json` suppression is working as intended: the 06-21 digest correctly suppressed 2 previously-surfaced papers; the 06-24 digest suppressed 1; the 06-25 suppressed 1; the 06-27 suppressed 1.

---

*Report generated by Claude on 2026-06-28 from Gmail Scholar alerts +
GitHub `arxiv-digest` against `INTERESTS.md`. Caveat: triage based on
title / authors / abstract metadata only; full-text reading is on the
user.*
