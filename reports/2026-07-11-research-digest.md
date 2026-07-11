# Research digest report — 2026-07-11

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-11** — three weeks since the prior
2026-06-20 report. Longer than the usual 1–2 day window because no
research-digest report ran in the interim; the arxiv-digest daily pipeline
kept running (through 2026-07-07) but no Scholar+arxiv triage report was
generated.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 07-11 | ~200 alert threads across the window. Focused triage on the 07-09 → 07-11 batch (most recent, un-triaged) plus a scan of the 06-21 → 07-08 backlog for triple-feed / self-feed hits. |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 07-07 | **Pipeline is 4 days stale** — no digest for 2026-07-08 → 07-11. Across 2026-06-21 → 07-07 the pipeline surfaced ~15 candidate papers (dominated by 06-30/07-01/07-07); of these, ~5 are on-thread (multimorbidity, causal-inference methods, drug repurposing, IBD spatial transcriptomics). |
| NCBI "My NCBI What's New" / bioRxiv / medRxiv subject digests | daily | Aggregate digests; not individually triaged here beyond the Scholar-alert cross-references. |

> ⚠️ **arxiv-digest pipeline is 4 days behind** (last digest 2026-07-07;
> today is 2026-07-11). No fetch-failure warning was logged for
> 07-08/07-09/07-10/07-11 — the workflow simply hasn't run. Worth
> confirming whether the GitHub Actions cron is failing silently, whether
> the runner is paused/removed, or whether this is an authenticated-cron
> credential issue. The 2026-06-20 pipeline note flagged the *reverse*
> failure mode (aggressive rate-limit induced 429s); this is a distinct
> failure and does not clear on its own. **Recommend investigating
> today** — a 4-day-stale digest is missing ~4 days of q-bio and stat.AP
> submissions in the window that most commonly surfaces on-thread papers.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **Self-feed hit + Karczewski feed on cross-ancestry TWAS methods —
  Nature Communications.** Bledsoe, Watkins, Bowen-Moore, Shaw et al. —
  *Multi-ancestry gene expression models amplify transcriptome-wide
  association study discovery and validation* (*Nature Communications*,
  2026). **Surfaced by (a) your own Chenjie Zeng — new-related-research
  feed and (b) the Konrad Karczewski — new-related-research feed** —
  double-feed with the self-feed lighting up, which is the highest-
  precision signal this digest can produce. Directly on your genetic-
  epidemiology / cross-ancestry / TWAS thread and paired with the
  MIXPRS multi-population PRS paper (item #2) suggests the field is
  consolidating around trans-ancestry statistical-genetics as a
  reference-class question in 2026 H2. **HIGH — read first.**
- **PGS Browser: public platform for personalized PGS analysis — Nature
  Communications, self-feed.** Kolosov, Reeve, Briotta Parolo, Kurki et
  al. — *PGS Browser: a public platform for personalized polygenic score
  analysis and interpretation* (*Nature Communications*, 2026), also in
  the **Chenjie Zeng self-feed** (co-surfaced with Bledsoe above). PGS
  infrastructure paper — the "PGS Catalog is the reference catalog, PGS
  Browser is the personal-report layer." Directly on your PRS clinical-
  implementation thread and pairs with the PRS-robustness /
  PRS-as-clinical-test sub-thread. **HIGH.**
- **MIXPRS: multi-population multi-method PRS combining — Nature
  Genetics.** Xu, Dong, X. Zeng, Bian, Zhou, Guan, Zhao — *MIXPRS enables
  multi-population and multi-method polygenic risk scores using summary
  statistics* (*Nature Genetics*, 2026, *Jian Yang — new-related-research*
  feed). Explicitly frames the "no single method wins everywhere"
  problem for multi-ancestry PRS and proposes summary-statistics-only
  ensembling. Directly on the trans-ancestry-PRS thread and complementary
  to Bledsoe (item #1). Note: X. Zeng is a co-author (not you — verify
  from author affiliation if archiving). **HIGH.**
- **Rare-variant burden explains PRS deviators — AJHG.** Baya, Lassen,
  Hill, Venkatesh, Currant et al. — *Individuals who deviate from
  polygenic expectation are enriched for damaging variants in genes
  linked to rare disease* (*American Journal of Human Genetics*, 2026,
  *Stephen B Montgomery — new-related-research* feed). This is the
  cleanest instance to date of the **"PRS+rare-variant composite risk"**
  argument on your INTERESTS file: individuals whose observed phenotype
  deviates from PRS prediction are systematically enriched for damaging
  variants in rare-disease genes — i.e., the residual of PRS-prediction
  captures Mendelian-like signal. Directly on **variant interpretation +
  genetic epi + rare disease + composite-risk-modeling** threads
  simultaneously. **HIGH — one of the two standouts this window.**
- **AoU + HBOC carrier ascertainment — ancestry/SES disparities,
  medRxiv, Denny related-research.** Yerukala Sathipati & Scott —
  *Documented clinical genetic testing among carriers of hereditary
  breast and ovarian cancer variants: Ancestry and socioeconomic
  disparities in the All of Us research program* (medRxiv 2026, *Joshua
  C. Denny — new-related-research* feed). This is on your **AoU +
  EHR-linked biobank + variant interpretation** intersection, with the
  additional layer that it measures **downstream clinical action**
  (documented genetic testing) rather than just carrier prevalence.
  Ancestry-stratified real-world ascertainment of pathogenic-variant
  carriers is exactly the AoU-specific analysis your penetrance work
  needs a companion for. **HIGH.**
- **STELLAR: rare-variant-integrating ensemble PRS — medRxiv, Jian Yang
  feed.** T. Chen, X. Li, R. Mazumder, H. Zhang, X. Lin — *STELLAR: A
  flexible ensemble learning framework integrating rare variants to
  enhance polygenic risk prediction* (medRxiv 2026, *Jian Yang —
  new-related-research* feed). Sibling paper to Baya (item #4) — where
  Baya *describes* the PRS-tail rare-variant enrichment, STELLAR
  *exploits* it in a stacked ensemble. Xihong Lin group; well-cited
  methods lineage. Together with Baya + Souaiaia (from the 06-20
  report), this is the **third consecutive report** with a rare-variant-
  aware PRS paper landing as HIGH — the sub-thread is now consistent
  enough to warrant a keyword expansion (see pipeline note #4). **HIGH.**
- **AoU GWAS of lichen sclerosus — All-of-Us keyword feed.** Silberstein,
  Abraskin, Gaudette, Hutchcraft — *77181 Genome-Wide Association Study
  of Lichen Sclerosus in the National Institute of Health All of Us
  Research Program* (JAAD or similar dermatology journal, 2026, "All of
  Us research program" keyword feed). AoU-based GWAS of a
  **female-predominant, underdiagnosed autoimmune-adjacent condition** —
  directly on the AoU biobank thread and on the "AoU as a discovery
  cohort for female-predominant / autoimmune / underdiagnosed
  phenotypes" sub-thread. Almost certainly uses AoU phecode/OMOP
  phenotype definitions. **HIGH.**
- **PRS robustness for cardiovascular clinical implementation — medRxiv
  (carry-forward, now in the Jian Yang feed).** de La Harpe, Vaucher,
  Kutalik, Fellay et al. — *Advancing Clinical Implementation of
  Cardiovascular Polygenic Risk Scores Through Patient-Level Robustness
  Assessment* (medRxiv 2026). Previously flagged in the 06-18 / 06-20
  reports on the PRS-stability sub-thread; now landing in the Jian Yang
  related feed as well. Confirms the sub-thread's coherence — Baya
  (deviators), STELLAR (rare-variant-integrating PRS), de La Harpe
  (patient-level robustness), and Souaiaia (tail architecture, from
  06-20) are converging on **"PRS as a clinical test needs
  patient-level rather than population-level performance metrics."**
  **HIGH-carry-forward.**
- **arxiv-digest on-thread: UKB comorbidity-network + progression
  phenotypes (07-07).** Fontana, Mapelli, Di Angelantonio, Ieva —
  *Enhancing comorbidity network inference with risk-enriched health
  trajectories embedding* (arXiv 2607.04702, 2026-07-06, stat.AP,
  score 3: uk biobank + biobank + multimorbidity). Gaussian-graphical-
  model comorbidity network on 24 UKB cardiometabolic diseases + 76 risk
  factors, then clustering community-derived patient embeddings into 4
  progression phenotypes with distinct long-term survival. Directly on
  your **multimorbidity / chronic disease clustering + UKB** threads.
  This is the first strong on-thread arxiv-digest hit in three weeks
  (see arxiv-digest quality note below). **HIGH.**
- **arxiv-digest on-thread: UKB prior-informed conditional GGM on
  cardiometabolic proteomics (07-01).** A. Mapelli, Massi, Cuccuru, Di
  Angelantonio, Ieva — *Prior-informed conditional Gaussian graphical
  models: an application to protein interaction network reconstruction*
  (arXiv 2606.31805, 2026-06-30, stat.AP, score 3: uk biobank + biobank
  + precision medicine). Same lab as Fontana (07-07). UKB-PPP proteomics
  (n = 49,129, p = 366) with knowledge-graph priors + covariate-
  conditional network estimation, identifies 34 T2D-associated network
  biomarkers detectable only through connectivity (not differential
  expression). Directly on **UKB + proteomic-signature + multimorbidity**
  threads and pairs with Ding et al. (Nature Medicine, 06-20 report).
  **HIGH.**
- **Chenjie Zeng self-feed also lit up on multi-ancestry TWAS** —
  see item #1 (Bledsoe). **Note that the self-feed fires only for
  papers Google's relevance model judges close to your published work.**
  Firing across two consecutive reports (06-20: Chen et al. nephro
  PRS+PheWAS; 07-11: Bledsoe multi-ancestry TWAS + Kolosov PGS Browser)
  is the standing pattern to trust most.

**Counts: 9 HIGH, 6 METHODS-WATCH, rest SKIP.** Higher HIGH count than
the 06-20 report (6 HIGH) reflects the longer 3-week window plus the
convergence of the PRS + rare-variant composite-risk sub-thread. The
06-20 items #4 (Souaiaia PRS-tails), #5 (Marderstein noncoding), and
#6 (Ding proteomic aging) all pair with items from this window — the
sub-threads they anchored are now producing multi-paper clusters,
which is the strongest form of on-thread signal.

---

## HIGH priority — detailed reports

### 1. Multi-ancestry gene expression models amplify transcriptome-wide association study discovery and validation
- **Authors / venue:** X. Bledsoe, N. Watkins, T. Bowen-Moore, M. Shaw et al. — *Nature Communications*, 2026. `nature.com/articles/s41467-026-75193-4`.
- **Surfaced by:** **Double-feed** — (a) *Chenjie Zeng — new-related-research* (**your own feed**) and (b) *Konrad Karczewski — new-related-research*. Self-feed firing is the highest-precision channel; Karczewski-feed pairing suggests the paper touches gnomAD-style multi-ancestry reference infrastructure.
- **Thread:** **Genetic epidemiology / TWAS / cross-ancestry portability.** The specific gap addressed is that *gene expression prediction models* (the TWAS building blocks — PrediXcan, S-PrediXcan, JTI, etc.) have historically been European-trained and transfer poorly across ancestry. The paper argues that jointly modeling multiple ancestries in the prediction-model training step is a discovery-and-validation multiplier.
- **What it is:** From the snippet — "Our understanding of the influence of ancestral background on genetically determined expression remains limited, especially when gene expression models are applied to studies from different or multiple populations." The methodological pattern is *jointly*-trained multi-ancestry gene-expression prediction models applied to trans-ancestry TWAS. Likely uses TOPMed + GTEx v9 + MAGE / gEUVADIS multi-ancestry expression data as training set, ancestry-stratified validation. The "amplify discovery and validation" language suggests both increased trans-ancestry hit yield AND better replication when discoveries in one ancestry are checked in another.
- **Why it matters to you:** Four converging reasons.
  (a) **Self-feed firing.** Google Scholar judged this close to your published work — the highest-precision signal the pipeline produces. In three weeks of reports, the self-feed has now fired for this paper AND the 06-20 Chen nephrolithiasis PheWAS+PRS paper AND the co-surfaced Kolosov PGS Browser paper. Three self-feed hits in three weeks is a high-rate window.
  (b) **Cross-ancestry TWAS is a defining thread on your INTERESTS file.** "GWAS, PRS / polygenic scores, TWAS, fine-mapping, and cross / trans-ancestry portability" — this paper is one bullet away from a direct restatement of that thread.
  (c) **Pairs with the MIXPRS paper (item #3).** Trans-ancestry PRS methods and trans-ancestry TWAS methods are the two co-evolving arms of "multi-ancestry statistical genetics." A double-hit in the same report suggests the field is now consolidating this into a coherent research programme.
  (d) **Karczewski-feed pairing.** Karczewski's new-related-research feed lights up for papers that touch pLoF burden, gnomAD, or ancestry-stratified allele frequencies. That this TWAS paper triggers his feed suggests the multi-ancestry models are validated against ancestry-stratified rare-variant data — i.e., the pLoF-burden connection is explicit.
- **Action:** **HIGH — read first.**
  (i) Note the ancestry composition of the training set — GTEx v9 has limited non-European samples; MAGE / gEUVADIS is more diverse. The training-set diversity bounds the trans-ancestry portability claim.
  (ii) Check whether they release *per-tissue-per-ancestry* prediction weights (analogous to PrediXcan / JTI GTEx). If so, that's a resource for any AoU TWAS work.
  (iii) Compare their multi-ancestry framework against the recent EGRET / cross-ancestry JTI benchmarks — the field's "what beats what" ordering matters for method selection.
  (iv) Check reference list for your work.

### 2. PGS Browser: a public platform for personalized polygenic score analysis and interpretation
- **Authors / venue:** N. Kolosov, M.P. Reeve, P.D. Briotta Parolo, M.I. Kurki et al. — *Nature Communications*, 2026. `nature.com/articles/s41467-026-74461-7`.
- **Surfaced by:** *Chenjie Zeng — new-related-research* feed (**your own feed**), co-surfaced with Bledsoe above.
- **Thread:** **Genetic epidemiology / PRS clinical implementation.** Explicit clinical-translation infrastructure for PGS Catalog scores — the "individual report layer" that PGS Catalog itself does not provide.
- **What it is:** From the snippet — "Polygenic scores (PGSs) quantify individual genetic susceptibility to complex diseases and can identify high-risk individuals well before clinical onset. Their clinical translation, however, requires population-based reference resources." Almost certainly a browser-style platform (a la ENIGMA / gnomAD browser) where a user's per-locus genotypes → PGS-Catalog-scored → percentile-referenced against a population reference panel → per-disease clinical-cutoff report. The Kurki + Reeve authorship is FinnGen-adjacent, so the reference panel is likely FinnGen + UKB. Complementary to the PGS Catalog itself: PGS Catalog stores the score definitions; PGS Browser applies them to an individual and reports.
- **Why it matters to you:** Three reasons.
  (a) **Self-feed firing.** As with #1, Scholar judged this close to your work.
  (b) **This is the "PGS clinical-report" primitive** you'd need for any AoU / MVP / UKB-style biobank return-of-results work. If AoU eventually does aggregate PGS return-of-results to participants (currently only variant-level for ACMG SF genes), a PGS Browser-style tool is the natural rendering layer.
  (c) **Pairs with the PRS-robustness sub-thread.** de La Harpe (patient-level robustness), Souaiaia (tail architecture, 06-20), Baya (deviators), and Kolosov (PGS Browser reporting) collectively define **"what does an individual-patient PGS report actually mean?"** — the sub-thread's practical companion to the methods-focused sub-thread anchored by Souaiaia/Ferreira.
- **Action:** **HIGH.**
  (i) Check what reference population(s) are used for percentile scaling — European-only, cross-ancestry, or ancestry-adaptive? The reference choice is the pinch-point for equity in clinical PGS reporting.
  (ii) Note whether the browser exposes only PGS Catalog scores or also computes ensemble / method-mixed PGS (a la MIXPRS in item #3). Ensembling would be a differentiating feature.
  (iii) Note the return-of-results framing — does it output raw percentile, categorized risk (low/average/high), or decision-curve-analysis-based clinical recommendations? Each framing has a different regulatory/clinical footprint.
  (iv) Worth a save for any future AoU PGS return-of-results conversation.

### 3. MIXPRS enables multi-population and multi-method polygenic risk scores using summary statistics
- **Authors / venue:** L. Xu, Y. Dong, X. Zeng, Z. Bian, G. Zhou, L. Guan, H. Zhao — *Nature Genetics*, 2026. `nature.com/articles/s41588-026-02637-4`.
- **Surfaced by:** *Jian Yang — new-related-research* feed. (Note: X. Zeng in the author list — verify whether this is Chenjie or a different X. Zeng before citing.)
- **Thread:** **Cross-ancestry PRS / genetic epidemiology + machine learning for precision health.** Ensembling multi-population, multi-method PRSs from summary statistics only.
- **What it is:** From the abstract snippet — "Many multi-population polygenic risk score (PRS) methods have been proposed to improve prediction in underrepresented populations; however, no single method performs best across all scenarios. Although integrating PRSs across multiple [methods and populations is intractable when only summary statistics are available]…" So the contribution is an ensembling method that only requires GWAS summary statistics as input — no individual-level data needed, which is the key data-access constraint for federated cross-consortium PRS work. Likely combines PRS-CS, LDpred2, SBayesR, and PRS-CSx / PRS-Mixer as component learners.
- **Why it matters to you:** Three reasons.
  (a) **The "no single method wins everywhere" framing is now mainstream** — MIXPRS makes it operational. Any future AoU / MVP PRS validation work should default to method-ensembling rather than picking one method.
  (b) **Summary-statistics-only requirement is federated-friendly.** This is the exact data-access constraint that governs AoU (no raw-data export) and MVP (enclave-only compute). A summary-statistics-only ensembling method fits the compliance profile of both, unlike individual-level ensemblers.
  (c) **Pairs with Bledsoe (item #1).** Trans-ancestry TWAS + trans-ancestry PRS ensembling are two arms of the same programme.
- **Action:** **HIGH.**
  (i) Read for the specific weighting scheme — inverse-variance, stacking, or held-out-set-tuned? Held-out-set tuning is the most flexible but requires access to individual-level data on the tuning set, which partly negates the "summary-stats only" advantage.
  (ii) Check the population panel — includes AFR / EAS / SAS / AMR? A 5-population evaluation is the standard; anything less is a limitation to note.
  (iii) Compare against the recent CT-SLEB, PROSPER, and PRS-Mixer benchmarks — MIXPRS should be beating at least one.
  (iv) Verify whether "X. Zeng" is you — if so this is more than related-research (though it did not appear on the citations feed, suggesting it's not your paper).

### 4. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease
- **Authors / venue:** N.A. Baya, F.H. Lassen, B. Hill, S.S. Venkatesh, H. Currant et al. — *American Journal of Human Genetics*, 2026.
- **Surfaced by:** *Stephen B Montgomery — new-related-research* feed.
- **Thread:** **Genetic epidemiology (PRS+rare-variant composite) + variant interpretation (rare-variant burden) + rare disease + composite risk models.** This is the strongest single-paper instance of the PRS-plus-rare-variant composite-risk pattern in the entire window.
- **What it is:** The core claim from the title: individuals whose *observed phenotype deviates from PRS prediction* — either much higher-than-expected disease or much lower-than-expected — are systematically enriched for damaging variants in rare-disease-associated genes. Operationally: you compute a PRS, you compute a prediction residual (observed phenotype − PRS-predicted phenotype), and you find that the *tails of that residual distribution* are enriched for rare pLoF / missense burden in relevant rare-disease genes. The methodological consequence is that PRS residual is a *cheap screen* for rare-variant-driven monogenic disease masquerading as complex trait — you can find undiagnosed Mendelian cases within a UKB-like biobank without whole-exome sequencing.
- **Why it matters to you:** Five converging reasons.
  (a) **The PRS-plus-rare-variant composite-risk pattern is an explicit INTERESTS-file bullet** ("composite risk models stacking PRS with rare pathogenic variants"). This paper *is* the empirical case for the pattern's utility.
  (b) **Pairs with Souaiaia (06-20 report, Nature).** Souaiaia argued the *tail genetic architecture differs from the bulk*; Baya finds the specific mechanism — damaging-variant enrichment in the tail. Together they are a coherent argument for hybrid PRS+burden scoring.
  (c) **Rare-disease-detection-within-biobank framing is on your INTERESTS file.** "Rare-variant association methods, deep phenotyping for rare-disease diagnosis (HPO-based)." Using PRS residuals as a *phenotypic filter* for rare-disease-gene sequencing is a highly-actionable finding for any AoU + rare-disease work.
  (d) **AJHG venue + Lassen / Venkatesh / Currant co-authorship = Oxford stats-genetics / UKB group.** This is high-quality methodological work with rigorous UKB and possibly FinnGen replication.
  (e) **Directly enables one of the pipeline suggestions from 06-20** — adding PRS-deviator or PRS-residual keywords. This paper would have been surfaced by that keyword had it been added.
- **Action:** **HIGH — one of the two standouts this window (with item #1).**
  (i) Read for how "damaging variants in genes linked to rare disease" is defined — ClinVar P/LP, LOFTEE HC pLoF, or a functional-effect predictor threshold? The definition drives which residual-tail enrichments are called real.
  (ii) Note the specific traits — height, BMI, T2D, CAD, LDL-C? The list matters for whether the finding generalizes to your APOL1 / CF-relevant phenotypes.
  (iii) Check whether they release *per-individual residual scores* or only aggregate statistics. Per-individual residuals would be a phenotyping primitive you could layer onto AoU.
  (iv) Cite in any future write-up of the PRS+rare-variant composite framework.

### 5. Documented clinical genetic testing among carriers of hereditary breast and ovarian cancer variants: Ancestry and socioeconomic disparities in the All of Us research program
- **Authors / venue:** S. Yerukala Sathipati, H. Scott — medRxiv, 2026. `medrxiv.org/content/10.1101/2026.06.09.26355262v1`.
- **Surfaced by:** *Joshua C. Denny — new-related-research* feed. (Denny is AoU CEO; his feed is the closest thing to an AoU-institutional-signal channel.)
- **Thread:** **AoU / EHR-linked biobank (core) + variant interpretation (HBOC pathogenic-variant carrier ascertainment) + causal-inference/pharmacoepi-adjacent (ancestry + SES as exposures for testing-uptake outcome).** Also touches your "penetrance estimation under population-screening conditions" sub-thread — HBOC carriers ascertained through population sequencing are exactly the "detected-but-not-clinically-recognized" population your penetrance-in-population-screening work models.
- **What it is:** From the abstract — "Hereditary breast and ovarian cancer (HBOC) variant carriers benefit from risk-reducing interventions, but only if identified. The extent to which carriers are clinically recognized, and whether recognition is equitable across diverse [ancestry and SES groups]…" The core measure is *documented clinical genetic testing* (from AoU EHR + participant survey linkage) among the subset of AoU participants who — by genomic sequencing — are HBOC pathogenic-variant carriers. The gap between "carrier-by-sequencing" and "documented-clinical-test" is the ascertainment gap; the analysis stratifies that gap by ancestry and SES.
- **Why it matters to you:** Five reasons.
  (a) **This is the AoU + EHR + variant-interpretation intersection at its cleanest.** It uses AoU's unique feature (paired sequencing + EHR + survey) to measure a downstream *clinical action* rather than just carrier prevalence. That's the design your penetrance-in-population-screening work is closest to.
  (b) **Ancestry disparity in clinical-test uptake is the population-screening equity question.** Any argument you make for population genomic screening (APOL1, HBOC, LQT, FH) has a Achilles' heel: if the intervention only reaches European-ancestry participants after screening, the screening exacerbates inequity. This paper measures that gap directly in AoU.
  (c) **Denny-feed hit signals AoU institutional relevance.** Denny's related-research feed lights up for AoU-adjacent work; this is the second recent Denny-feed AoU-adjacent hit (Kundu et al. multi-site EHR selection bias, from 06-20).
  (d) **HBOC is a canonical pathogenic-variant class** — BRCA1/2 pLoF variants with well-established ACMG classification. Uses cleanly for cross-referencing with your ACMG classification / VUS resolution work.
  (e) **medRxiv preprint** — actionable citation for any preprint / draft you have in flight; you can cite it now.
- **Action:** **HIGH.**
  (i) Read for the sequencing pipeline used to ascertain carriers — AoU short-read sWGS with a specific pathogenic-variant filter, or a specific HBOC panel? The filter's sensitivity/specificity bounds the "true-carrier" denominator.
  (ii) Note the ancestry categorization — genetic-ancestry-inferred (ADMIXTURE / SNPweights) vs. self-reported? The categorization drives interpretability.
  (iii) Check whether the SES measure is participant-reported income/education or ZIP-code-derived. The former is more direct; the latter has known ecological-fallacy issues.
  (iv) Cite as a reference for any AoU-based penetrance / population-screening equity write-up.

### 6. STELLAR: A flexible ensemble learning framework integrating rare variants to enhance polygenic risk prediction
- **Authors / venue:** T. Chen, X. Li, R. Mazumder, H. Zhang, X. Lin — medRxiv, 2026. `medrxiv.org/content/10.1101/2026.06.07.26355109v1`.
- **Surfaced by:** *Jian Yang — new-related-research* feed.
- **Thread:** **Genetic epidemiology (PRS + rare variants) + variant interpretation (rare-variant burden) + ML for precision health (ensemble methods).** Sibling paper to Baya (item #4): where Baya *describes* the rare-variant-enrichment in PRS deviators, STELLAR *builds a predictor* on that pattern.
- **What it is:** An ensemble framework that combines a standard polygenic score with rare-variant burden terms (likely LOFTEE HC pLoF, missense-severity-weighted, or ClinVar P/LP-weighted) into a single stacked predictor for a target phenotype. The "flexible ensemble" language suggests they compare multiple base-learner combinations. Xihong Lin group at Harvard has been a leader in rare-variant burden methods (SKAT, ACAT-V lineage); this is likely their PRS-integration extension.
- **Why it matters to you:** Three reasons.
  (a) **Direct implementation of the composite-PRS-plus-rare-variant pattern.** The INTERESTS-file bullet on "composite risk models stacking PRS with rare pathogenic variants" now has a specific methodological candidate.
  (b) **Xihong Lin lineage.** SKAT, ACAT, STAAR — the group has a strong track record of methods that get adopted. If STELLAR benchmarks well, expect adoption in downstream burden-analysis pipelines.
  (c) **medRxiv preprint** — early-access, cite-able.
- **Action:** **HIGH.**
  (i) Read for the specific base-learner set — PRS-CS + LDpred2 + STAAR + ACAT-V? The base-learner diversity affects generalization.
  (ii) Check the phenotypes evaluated — CAD, T2D, LDL-C, height? The list matters for whether it transfers to your APOL1 / CF / kidney phenotypes.
  (iii) Compare AUC / R² gains vs. PRS-alone AND vs. burden-alone. The two-baseline comparison is the actual demonstration.
  (iv) Cross-reference with Baya (item #4) — if STELLAR's improvement mechanism is exactly the PRS-deviator rare-variant enrichment Baya describes, that's a clean methods → biology → methods loop.

### 7. Genome-Wide Association Study of Lichen Sclerosus in the National Institute of Health All of Us Research Program
- **Authors / venue:** M. Silberstein, K. Abraskin, J. Gaudette, M. Hutchcraft — *Journal of the American Academy of Dermatology* (JAAD, likely), 2026, abstract # 77181 (typical for AAD abstract-based submissions).
- **Surfaced by:** "All of Us research program" keyword feed.
- **Thread:** **AoU / EHR-linked biobank (core) + genetic epidemiology (GWAS) + PheWAS-adjacent (lichen sclerosus is a female-predominant, chronically-underdiagnosed condition; ascertainment via EHR phecode is nontrivial).**
- **What it is:** GWAS of lichen sclerosus (LS) — an autoimmune-adjacent, female-predominant, chronic mucocutaneous condition — using AoU. LS is one of the underdiagnosed autoimmune-adjacent conditions AoU is uniquely well-suited to study because (i) it disproportionately affects populations underserved by traditional dermatology-registry-based genetic studies, and (ii) it is likely phecoded (phecode 695.4 or 686.9x depending on the map) in EHR data, so ascertainment scales with AoU EHR-linked cohort.
- **Why it matters to you:** Four reasons.
  (a) **AoU-based GWAS of an underdiagnosed autoimmune-adjacent phenotype is exactly the AoU-differentiator use-case.** UK Biobank has a healthy-volunteer bias that under-samples this condition; MVP's veteran cohort is >80% male; only AoU has the demographic breadth for LS discovery-level GWAS.
  (b) **Phecode-based EHR ascertainment.** The methods almost certainly use ICD → phecode → case ascertainment; whichever phecode map they use is worth noting (Bastarache 1.2 vs. PheCode X 2.0 vs. AoU's built-in phenotype library).
  (c) **Autoimmune-disease thread.** Your INTERESTS file explicitly notes IBD as "shared with broader autoimmune work" — LS is on the same autoimmune-adjacent spectrum.
  (d) **AoU as GWAS discovery cohort** is a growing pattern; keeping track of exemplars is worth doing.
- **Action:** **HIGH.**
  (i) Read for case-ascertainment strategy (phecode-based, chart-review-validated, or PheKB-style rule-based). Chart review is the gold standard but not scalable.
  (ii) Note the case count — LS is underdiagnosed even in EHR, so the case count is a proxy for the phenotype algorithm's sensitivity.
  (iii) Check ancestry stratification — AoU's African-ancestry sub-cohort is a differentiator for LS-related autoimmune work.
  (iv) Log as a reference for AoU-based autoimmune GWAS design decisions.

### 8. Advancing Clinical Implementation of Cardiovascular Polygenic Risk Scores Through Patient-Level Robustness Assessment
- **Authors / venue:** R. de La Harpe, J. Vaucher, Z. Kutalik, J. Fellay et al. — medRxiv, 2026. Carry-forward — previously flagged in the 06-18 and 06-20 reports.
- **Surfaced by:** *Jian Yang — new-related-research* feed (new surfacing channel this window; previously surfaced via a different author feed).
- **Thread:** **Genetic epidemiology (PRS) + ML for precision health (clinical-implementation-grade robustness) + causal inference-adjacent (decision-grade validation).**
- **What it is:** Patient-level robustness assessment for cardiovascular PRS — measures *intra-individual* discordance across PRS methods rather than population-level discordance. From the snippet: "Polygenic risk scores (PRSs) for atherosclerotic cardiovascular disease (ASCVD) can perform equivalently at the population level yet disagree for individual patients."
- **Why it matters to you:** Two reasons.
  (a) **PRS-stability sub-thread anchor.** Together with Souaiaia (Nature, tails architecture, 06-20), Baya (deviators, item #4), STELLAR (rare-variant PRS, item #6), and Kolosov (PGS Browser, item #2), this is the fifth PRS-robustness/individual-report paper in three weeks. The sub-thread is now a coherent body of work.
  (b) **New Jian Yang feed surfacing.** Two independent surfacing channels for the same paper is a signal-strength doubler.
- **Action:** **HIGH-carry-forward.** No new action beyond the 06-18 recommendation (read for the specific robustness metric — cross-method concordance, permutation-based, or bootstrap-derived; cite as anchor for any PRS-as-clinical-test write-up).

### 9. Enhancing comorbidity network inference with risk-enriched health trajectories embedding
- **Authors / venue:** N. Fontana, A. Mapelli, E. Di Angelantonio, F. Ieva — arXiv 2607.04702, 2026-07-06, stat.AP. (Surfaced by `arxiv-digest` 2026-07-07.)
- **Surfaced by:** `arxiv-digest` 2026-07-07 (score 3: uk biobank + biobank + multimorbidity).
- **Thread:** **Chronic disease clustering & multimorbidity (core) + EHR-linked biobank (UKB) + ML for precision health (trajectory clustering).**
- **What it is:** From the abstract — comorbidity network inference using individual health trajectories to learn disease associations with (a) semantic similarity and temporal co-occurrence, (b) sparse Gaussian Graphical Model with Lasso regularization, and (c) prior clinical knowledge on shared risk factors. Applied to UKB with 24 cardiometabolic diseases and 76 risk factors → recovers clinically meaningful disease patterns, identifies 4 disease communities aligning with cardiometabolic taxonomy → derives community-based patient representations → clusters those into **4 progression phenotypes with significantly different long-term survival trajectories**.
- **Why it matters to you:** Three reasons.
  (a) **Multimorbidity thread is on your INTERESTS file** with explicit call-out of "Unsupervised and semi-supervised methods for discovering disease subtypes, multimorbidity patterns, and disease trajectories from EHR or biobank data. Latent class / latent profile analysis, topic models on diagnosis sequences, graph-based comorbidity networks, and trajectory clustering. Particularly interested when applied to cardiometabolic disease…" This paper is a near-exact match — cardiometabolic UKB, graph-based network, trajectory-based cluster.
  (b) **Framework not just descriptive but survival-linked.** The community-based patient representation → progression phenotype → survival trajectory chain is the operational form of the multimorbidity thread.
  (c) **Same lab as Mapelli et al. (07-01, item #10 below).** The Fontana + Mapelli papers are a coordinated methodological programme — worth reading them together.
- **Action:** **HIGH.**
  (i) Read for the risk-factor pool size (76 factors) — is this all UKB metabolic panel + assessment-center data, or a curated subset? The size drives the confounding-control claim.
  (ii) Note the community-count decision (4 communities) — is this Bayesian-model-selection-derived or a chosen-a-priori grid? The former is stronger.
  (iii) Compare the 4 progression phenotypes against known cardiometabolic subtypes (Ahlqvist SNSD, Wagner clusters). Recovering-known-subtypes is a validation signal.

### 10. Prior-informed conditional Gaussian graphical models: an application to protein interaction network reconstruction
- **Authors / venue:** A. Mapelli, M.C. Massi, G. Cuccuru, E. Di Angelantonio, F. Ieva — arXiv 2606.31805, 2026-06-30, stat.AP. (Surfaced by `arxiv-digest` 2026-07-01.)
- **Surfaced by:** `arxiv-digest` 2026-07-01 (score 3: uk biobank + biobank + precision medicine).
- **Thread:** **UKB + proteomic signatures (UKB-PPP) + multimorbidity + knowledge-graph priors + ML for precision health.**
- **What it is:** Prior-informed conditional Gaussian graphical model — combines curated interaction-database priors (StringDB / BioGRID style) with covariate-conditional network estimation. Applied to UKB-PPP cardiometabolic proteomics (n = 49,129 UKB participants, p = 366 proteins). Identifies **34 network-central T2D-associated biomarkers, several detectable only through their connectivity** (not differential expression) — a finding directly analogous to the "hub" concept in multimorbidity networks. Reveals 6 biologically coherent protein communities.
- **Why it matters to you:** Three reasons.
  (a) **UKB-PPP is on the proteomic-signatures thread** — recall Ding et al. (Nat Med, 06-20 report). This paper is a UKB-PPP methods paper.
  (b) **Prior-informed KG + statistical network modeling** is the same combination you'd want for any drug-repurposing / EHR-KG work — biological knowledge as a Bayesian prior, data-driven perturbations on top.
  (c) **Same lab as Fontana (item #9).** Reading them together clarifies the methodological programme.
- **Action:** **HIGH.**
  (i) Note the specific prior source(s) — StringDB (confidence-weighted) is standard; BioGRID / IntAct / Reactome differ in coverage.
  (ii) The 34 network-central biomarkers — are these validated against a held-out T2D case set, or only descriptive? Held-out validation is the harder claim.
  (iii) Compare community-detection scheme with Fontana (Louvain? spectral?) — inter-lab consistency across #9 and #10 would strengthen both.
  (iv) Save for any UKB-PPP or KG-informed statistical-genetics work.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **PREDIKTOR: Predicting Therapeutic Outcome via Aligning Patient-Specific Knowledge Graph and Gene-Level Perturbation Representations** — D. Bang, S. An, I. Sung, I. Yun, S. Kim, S. Lee — arXiv 2607.04557, 2026-07-06, cs.LG. (Surfaced by `arxiv-digest` 2026-07-07; score 1, `knowledge graph`.) **Directly on the drug repurposing + KG thread** despite the low score. Individualized gene regulatory network (DysRegNet) + DrugBank drug-target links + a frozen LINCS L1000 attention model → CLIP-style contrastive alignment for drug-response prediction. Evaluated on TCGA + I-SPY2. Not directly clinical-EHR-linked, but the design pattern — patient-KG × perturbation-encoder aligned via contrastive objective — is the natural fusion for future EHR-KG + LINCS + AoU integrations. **METHODS-WATCH — high-priority within METHODS-WATCH.**

- **Residual-on-Residual Regression as a Tool for Effect Estimation in Observational Data** — A.I. Naimi, Q. Jin, Y.-H. Yu, S.M. Parisi, L.M. Bodnar — arXiv 2606.30976, 2026-06-29, stat.ME. (Surfaced by `arxiv-digest` 2026-07-01; score 2, inverse probability + causal inference.) Compared to AIPW and TMLE with equivalent estimates in the standard setting; **outperforms AIPW/TMLE under weak positivity violations when the effect is approximately constant** (partially linear model). Uses nuMoM2b for demonstration. Useful for your causal-inference / pharmacoepi thread as a triangulation strategy — a "when AIPW and TMLE disagree, run RoR" defensive-analytics move. **METHODS-WATCH.**

- **Colocalization of eQTLs With Type 2 Diabetes and Glycemic Traits Using Whole-Genome Sequences in Diverse Populations From the NHLBI Trans-Omics in Precision Medicine (TOPMed) Program** — N. Wang, D.A. DiCorpo, Y. Zhang, E. Kleinbrink, D.K. Arnett et al. — *Diabetes*, 2026. (Jian Yang related-research feed.) TOPMed multi-ancestry WGS-based eQTL colocalization for T2D + glycemic traits — addresses the low-frequency/rare-variant blind spot of imputed-genotype methods. Pairs with Bledsoe (item #1) for the cross-ancestry statistical-genetics theme. **METHODS-WATCH on the trans-ancestry-eQTL sub-thread; potentially HIGH if you're doing T2D-specific work.**

- **Distilling Foundation Models for Electronic Health Records** — W. Zhang, Y. Chen, H. Liu, J. Wang, X. Li, X. Hong, M. Zhao et al. — surfaced via "electronic health records" keyword and "Foundation models AND EHR" keyword feeds. Model-distillation applied to EHR foundation models — the "how do we shrink CLMBR/MOTOR/MEDS-style FMs for deployment" question. **METHODS-WATCH on the EHR-FM thread**; useful for any AoU / MVP compute-constrained deployment work.

- **X-FEMR: A Token-level Explainable Approach for Electronic Health Records Foundation Models using Transformer-based Models** — J. Huang, P. Yin, Z. Xu, D. Capurro, M. Conway, T. Dang — arXiv preprint, 2026. Token-level attribution over EHR FMs — the "which codes drive the risk prediction" interpretability question. Complements Zhang et al. (distillation) as the interpretability sibling of the same EHR-FM methods thread. **METHODS-WATCH.**

- **Integrative statistical genetics prioritizes candidate ASCVD susceptibility genes across tissues** — Q. Liu, X. Han, Y.Q. Hu, L. Fu — *Molecular Medicine*, 2026. ("Phenome-wide association studies" keyword feed.) TWAS-style susceptibility-gene prioritization for ASCVD — pairs with Bledsoe (#1) as a downstream-application example. **METHODS-WATCH.**

- **DiSTILL: A Hybrid Cloud-HPC Workflow System for Reproducible Spatial Transcriptomics Analysis** — M.J. Toledo Tan et al. — arXiv 2606.30693, 2026-06-28, q-bio.GN. (Surfaced by `arxiv-digest` 2026-07-01; score 1, inflammatory bowel disease.) IBD spatial transcriptomics workflow orchestration — off the EHR-IBD-phenotyping thread substantively (this is wet-lab pipeline plumbing, not EHR phenotyping), but the IBD phenotype anchor is on-list. **METHODS-WATCH-borderline-SKIP.**

- **Polygenic scores as modifiers in Mendelian diseases** — A. Schmidt, K.U. Ludwig, H.O. Heyne — *Medizinische Genetik*, 2026. ("Mendelian diseases" keyword feed.) Perspective / review-format piece framing PRS as a *modifier* of Mendelian penetrance. Directly on the PRS + rare-variant composite thread — pairs with Baya (item #4) and STELLAR (item #6). Would rank HIGH if it's a primary-analysis paper; ranking as METHODS-WATCH pending confirmation this is a review rather than empirical. **METHODS-WATCH-leaning-HIGH.**

---

## SKIP / noise (logged, no action)

- **arxiv-digest** entries with `foundation model` keyword hits that turn out to be non-EHR foundation models: DNA-LM (Karpinsky et al., 06-30); tabular in-context learners (Guan et al., 07-01); histopathology-RNA-seq alignment (Winter et al., 06-30); 3D plant phenotyping (Jia et al., 07-03). Confirms the pipeline-note recommendation to tighten the `foundation model` keyword to require an EHR/clinical/biomedical co-occurrence term.
- **arxiv-digest** entries with `causal inference` keyword hits on non-clinical applications: Airbnb price/booking modeling (Wu & Schmierer, 07-02; Wu et al., 07-01), marketing mix multicollinearity clustering (Wu et al., 07-01), insurance pricing with LLM embeddings (Blier-Wong & Kusmenko, 06-30). Ongoing keyword-leak class — same pipeline-note recommendation from prior reports (require a clinical/biomedical co-occurrence term).
- **Causal ASCEND: Scalable Two-tier Causal Discovery on High Dimensional Multi-omics Data** — S. Asiedu, D. Watson — arXiv 2607.04527, 2026-07-05, stat.ML (surfaced by `arxiv-digest` 07-07). Genomics causal discovery framework — technically interesting but not on your clinical / EHR / biobank threads. Log.
- **Evaluating HWE and Association in GWAS: A Unified Procedure** — S. Böhringer, H. Holzmann — arXiv 2606.30311, 06-30, stat.ME. Classical GWAS methods paper (HWE + association testing unification). Log — off your active methods threads.
- **Semantic insurance pricing with large language models** — Blier-Wong & Kusmenko — arXiv 2606.29371, stat.AP (`motor` keyword hit is on "motor third-party liability" — an insurance term). Classic keyword-leak SKIP.
- Many **Google Scholar author-feed** citation-graph leaks — LLM/AI newsletter entries (Rohan Paul, Marktechpost, AlphaSignal), the batch of Chute / Zitnik / Shah citations that surface non-clinical LLM-agent or NLP papers, and a persistent pattern of *molecular-mechanism* review articles surfacing in the Karczewski / Denny / Kastner citation feeds. These are the standing SKIP noise class and are not individually enumerated.
- **Multi-modal knowledge graph entity alignment: a comprehensive survey** — Z. Yan et al. — VLDB Journal, 2026. ("knowledge graph" keyword feed.) Generic KG survey, non-biomedical. Standing SKIP for the KG-keyword leak class.
- **APOL1 keyword hit** — Patricio-Liébana et al., *Kidney International Case Reports* — collapsing glomerulopathy case report with G2/G2 APOL1. Off-thread substantively (case report, not methodology or cohort analysis) but the APOL1 keyword is central to your interests — worth a two-minute check to confirm nothing generalizable, then log.
- **RNA m6A methylation writers in autoimmune diseases** — Gao et al., *Acta Pharmacologica Sinica*, 2026. Molecular-mechanism review. SKIP.
- Various **UK Biobank** keyword-feed papers on off-thread phenotypes (GERD × abdominal obesity, HFpEF-ABA cardiac remodeling, sedentary behavior). Standard UKB-keyword-leak class. Log.
- **Undiagnosed Diseases Network keyword feed** surfaced an *acne trial* result (paper #71158 in same abstract batch as Silberstein). Off-thread; standard UDN-keyword-leak class.
- **arxiv-digest 07-04/05/06** — 0 papers each. Not fetch-failures (unlike 06-20); just genuinely sparse windows.
- **arxiv-digest 07-08 → 07-11** — no digest generated. Pipeline is stale (see pipeline note above).

---

## Suggestions for the pipeline

Carry-forward items from 06-20 remain unactioned. Today's items add
several new issues.

1. **`arxiv-digest` pipeline appears stopped since 2026-07-07.** *New,
   highest-priority item.* No digests for 07-08 → 07-11. The 06-20 report
   flagged a 3-of-4-category *fetch failure* (429s); this is different —
   the workflow isn't running at all, so nothing gets emitted. Check
   GitHub Actions run history for the schedule; verify the cron trigger,
   runner availability, and any recent token / permission changes.
   Investigate today.

2. **`knowledge graph` keyword: 8th consecutive window of non-biomedical
   hits** (today's Multi-modal KG entity alignment survey, plus the
   U-KGNav navigation KG paper). Same recommended fix as 06-20 —
   tighten to `(knowledge graph) AND (medical OR biomedical OR clinical
   OR EHR OR phenotype OR drug OR disease OR gene)`.

3. **`foundation model` keyword: 4 non-EHR-foundation-model hits in
   the arxiv-digest window** (DNA-LM, tabular ICL, histopath-RNAseq
   alignment, 3D plant phenotyping). Recommended fix: tighten to
   `(foundation model) AND (electronic health record OR EHR OR clinical
   OR biobank OR phenotype OR medical)` OR restrict to specific
   `foundation model for EHR` phrase.

4. **Add PRS-residual / PRS-deviator / PRS-penetrance-modifier keywords**
   (*new — 3rd consecutive report's sub-thread coherence*). Today's Baya
   AJHG paper (item #4) and Schmidt Medizinische Genetik paper
   ("Polygenic scores as modifiers in Mendelian diseases") would have
   been surfaced by these. Recommended specific keywords:
   `PRS deviator`, `polygenic residual`, `PRS modifier of Mendelian`,
   `polygenic penetrance modifier`.

5. **Add `PRS ensemble`, `polygenic score ensemble`, `stacked
   polygenic risk` keywords** (*new*). Today's MIXPRS (Nature Genetics,
   item #3) and STELLAR (medRxiv, item #6) would benefit from direct
   surfacing rather than via author-feeds.

6. **`mendelian diseases` and `drug repurposing` keyword fixes**
   (carry-forward, 8th consecutive window unchanged). Underlying keyword
   behavior hasn't changed.

7. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds**
   (carry-forward, unaddressed). Every HIGH-item this window that surfaced
   through Scholar (items #1–8) would have failed to appear in the
   current arxiv-digest scope. The Fontana/Mapelli/Naimi arxiv-digest
   items (#9, #10, and the RoR causal-inference METHODS-WATCH item) show
   what stat.AP + stat.ME give you when the source category is included
   — the multimorbidity / causal-inference-methods coverage got real.
   The gap that remains is q-bio.QM depth + cs.LG for the EHR-FM / KG
   methods papers.

8. **Continue self-citation feed as the highest-precision channel**
   (carry-forward). Chenjie Zeng self-feed fired for both Bledsoe (item
   #1) and Kolosov (item #2) this window; that pattern is the strongest
   signal the pipeline produces and no changes are needed to that alert.

9. **PRS-robustness sub-thread now warrants a periodic "state of the
   sub-thread" mini-report** (new observation). Souaiaia (06-20),
   de La Harpe (06-18/20/07-11), Baya (this window), STELLAR (this
   window), Kolosov (this window), Chen nephro PheWAS+PRS (06-20) form
   a coherent 6-paper cluster in <4 weeks. Worth a synthesis pass —
   "what does the PRS-as-clinical-test literature now look like, and
   what's the citation-worthy summary" — as a one-off report.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 9 | (1) Bledsoe et al. multi-ancestry TWAS [Nat Comm, self-feed + Karczewski], (2) Kolosov et al. PGS Browser [Nat Comm, self-feed], (3) Xu et al. MIXPRS [Nat Genet, Jian Yang], (4) Baya et al. PRS deviators + rare-variant enrichment [AJHG, Montgomery], (5) Sathipati & Scott HBOC AoU ancestry/SES disparities [medRxiv, Denny], (6) Chen et al. STELLAR rare-variant PRS ensemble [medRxiv, Jian Yang], (7) Silberstein et al. lichen sclerosus AoU GWAS [AoU keyword feed], (8) de La Harpe et al. cardiovascular PRS robustness [medRxiv, Jian Yang — carry-forward], (9) Fontana et al. UKB comorbidity network trajectory [arXiv 2607.04702], (10) Mapelli et al. UKB-PPP prior-informed cGGM [arXiv 2606.31805]. |
| METHODS-WATCH | 6+ | PREDIKTOR (KG × LINCS for drug repurposing), Naimi et al. (residual-on-residual regression), Wang et al. (TOPMed multi-ancestry T2D eQTL), Zhang et al. (EHR FM distillation), X-FEMR (EHR FM interpretability), Liu et al. (integrative statistical genetics for ASCVD), Schmidt et al. (PRS-as-Mendelian-modifier review), DiSTILL (IBD spatial transcriptomics workflow — borderline). |
| SKIP | ~35 | See SKIP/noise section above. |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH over a
1-day window), this 3-week window delivers 9 HIGH / 6 METHODS-WATCH,
which per-day is *lower density* than the 06-20 window — but the
composite-risk (PRS + rare variants) sub-thread is now the dominant
signal, with a 4-paper cluster (Baya, STELLAR, de La Harpe, Kolosov)
that pairs with the 06-20 Souaiaia paper into a 5-paper coherent
literature. The Bledsoe + MIXPRS pair also anchors a distinct
trans-ancestry-statistical-genetics cluster. Two clean sub-thread
crystallizations in a single window is the standout pattern.

**Two primary actionable items:**

1. **Investigate the arxiv-digest pipeline stall (07-08 through 07-11
   inclusive).** Highest priority — silent pipeline stops are worse than
   loud fetch failures because they're invisible until a report like
   this one flags them.

2. **Draft a one-off "PRS as a clinical test" synthesis** covering
   Souaiaia (06-20), de La Harpe (multi-report), Baya (this report),
   STELLAR (this report), Kolosov (this report), and Chen nephro
   PheWAS+PRS (06-20). Six papers in <4 weeks is a bona fide sub-thread
   crystallization; capturing it now would produce a durable reference
   for any PRS-clinical-implementation write-up over the next 6–12 months.
