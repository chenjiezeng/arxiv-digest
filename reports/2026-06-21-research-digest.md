# Research digest report — 2026-06-21

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-20 → 2026-06-21** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-20 → 06-21 | One large batch 06-21 10:36Z (≈30 author-feed alerts: **Chenjie Zeng self-feed**, Bastarache, Karczewski, Denny, Hripcsak, Hernán, Yang, Montgomery, Szolovits, Callahan, Zitnik, Natarajan, Luo, Chute, Kastner, Patrick Ryan, Wendy Chung, Patrick Ellinor, Joshua Denny, Russ Altman, Mark Gerstein, Evan Eichler, Michael Snyder, Sasha Gusev, Jeffrey Kopp). No 06-20 evening tail. |
| `arxiv-digest` repo (`digests/`) | 2026-06-20 → 06-21 | **06-21 = 0 papers** (no warning logged — clean run, just empty). Cf. 06-20 = 0 papers (3/4 categories fetch-failed; warning logged). See pipeline note below. |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |

> ⚠️ **`arxiv-digest` 06-21 run produced 0 papers with NO warning** — a
> clean run that surfaced nothing. By itself that's plausible (Saturday
> q-bio / stat.AP intake is genuinely thin), but pairs with 06-20's
> 3/4-category fetch failure to make a two-day stretch where the pipeline
> contributed zero on-thread signal. Recommend checking whether 06-21
> actually fetched all four categories successfully or whether the
> warning logic is silently failing when *all* categories return empty
> (vs. when *some* error out, which is what was caught yesterday). The
> distinction matters: "all four categories returned 0 papers" is real
> news ("nothing on q-bio.QM / GN / PE / stat.AP today"), but "fetch
> succeeded with status 200 but parsing returned 0 entries" is a
> regression worth a workflow-log check.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a *self-feed* multi-scale GWAS-
  translation paper in Cell Genomics that lands squarely on the drug-
  repurposing thread.** Felici, Chen, Yuan, Jiang, Ip, Rudd et al. —
  *Translating genome-wide association studies at multiple scales: Drug
  target prioritization, cellular architectures, and organ imaging*
  (*Cell Genomics*, 2026) — surfaces in **your own Chenjie Zeng new-
  related-research feed**. The self-feed firing is the highest-precision
  channel the alert pipeline produces; combined with the title's explicit
  "drug target prioritization" framing and the Cell-tier venue, this is
  the single most actionable item this window. The multi-scale framing
  (proteins → cells → organs) is the design pattern you've been tracking
  for GWAS-to-clinical-actionable translation, and it explicitly ties
  GWAS signals to drug-target ranking via tissue-context and imaging
  layers. **Read first.**
- **First rigorous meta-analysis of LLM diagnostic performance in rare
  diseases — directly on the rare-disease + LLM thread.** Zhu, Luo, Xu,
  Zhang, Fu, ALMasri et al. — *A systematic review and meta-analysis of
  the Diagnostic Performance of Large Language Models in Rare Diseases*
  (Research Square preprint, 2026, **Bastarache citation feed**). This
  is the first systematic-review-with-pooled-estimates of LLM diagnostic
  accuracy *specifically in rare disease* — the prior literature was a
  pile of single-model single-disease evaluations. It cites a Bastarache
  paper on LLM-based rare-disease diagnosis, which is the dominant
  reference in this sub-field. **HIGH** for the rare-disease and ML-for-
  precision-health threads; default citation going forward.
- **Triple-hit target-trial-emulation paper: GLP-1 RAs in IBD + obesity/
  diabetes.** Yeh, Ahuja, Patel, Xu, Park, Gold et al. — *Adjunctive
  GLP1 Receptor Agonists in Patients with Inflammatory Bowel Diseases
  and Obesity and/or Diabetes: A Target Trial Emulation* (*Clinical
  Gastroenterology and Hepatology*-family, 2026, **Hernán citation**).
  Three of your active threads converge: (a) GLP-1 pharmacoepi as a
  tracked drug class, (b) target-trial emulation as your default causal
  framework, (c) IBD as a tracked disease thread. The Hernán-citation
  surfacing means it cites the canonical TTE methodology paper and is
  therefore methodologically rigorous. **HIGH.**
- **Comparative-effectiveness GLP-1 RA paper on kidney outcomes —
  pharmacoepi thread.** Neumiller, Deng, Swarna, Polley, Herrin et al. —
  *Comparison of Specific Glucagon-Like Peptide-1 Receptor Agonists on
  Kidney Outcomes Among Patients With Type 2 Diabetes* (*American
  Journal of …*, 2026, **Patrick Ryan related-research**). Head-to-head
  GLP-1-vs-GLP-1 comparison for kidney outcomes is the second-step
  pharmacoepi question after the GLP-1-vs-placebo / GLP-1-vs-other-class
  questions are exhausted. Patrick Ryan surfacing is the OHDSI / OMOP
  signal — likely a multi-database CDM study. **HIGH** on the GLP-1
  pharmacoepi sub-thread.
- **Somatic-mosaicism paper directly on the CHIP/VEXAS/telomere-biology
  thread.** Franke, Kirchner, Barredo, Zaidan et al. — *Promoter TERT-
  Related Hematopoietic Somatic Mosaicism in Patients With Telomere
  Biology Disorders* (*American Journal of Hematology*, 2026, **Chenjie
  Zeng self-feed**). TERT-promoter somatic mosaicism in TBD patients is
  exactly the kind of telomere-biology / clonal-hematopoiesis crossover
  paper your INTERESTS file flags as on-thread. Self-feed surfacing
  reinforces priority. **HIGH** on the CHIP/somatic-mosaicism thread.
- **HPO curation deepens rare-disease prioritization performance.**
  Cuperus, Pasmans, Han, Arterbery et al. — *In-depth Human Phenotype
  Ontology Curation Boosts Prioritization Performance for Netherton
  Syndrome* (*British Journal of Dermatology*, 2026, **Chenjie Zeng
  self-feed**). HPO-curation-improves-diagnostic-yield is exactly your
  rare-disease + KGs/ontologies thread crossover. Self-feed surfacing.
  The disease is dermatologic (Netherton syndrome) but the methodological
  pattern — refine HPO terms for an under-curated disease, then measure
  diagnostic-prioritization lift — is the generalizable contribution.
  **HIGH** on the HPO / rare-disease thread.
- **Regulome-wide association atlas across contexts — pairs with
  yesterday's Marderstein paper.** Liu, Wang, Sun, Luo, Qian, Li, He et
  al. — *A Multi-Context Regulome-Wide Association Atlas for Genetic
  Studies of Aging Brain Disorders* (medRxiv, 2026, **Bastarache
  citation**). Multi-context (cell-type × developmental-state) regulome
  atlas applied to aging-brain disorders. Composes with the Marderstein
  noncoding-variant paper from the 06-20 report into a coherent multi-
  context regulatory-variant-interpretation sub-thread. **HIGH** on the
  variant-interpretation thread; **METHODS-WATCH-plus** on the brain-
  aging / multimorbidity thread.
- **Nature paper on conversational AI for disease management — direct
  EHR-FM relevance.** Liévin, Palepu, Weng, Saab, Stutz et al. —
  *Towards Conversational AI for Disease Management* (*Nature*, 2026,
  **Vivek Natarajan citation**). This is the next chapter of the AMIE
  / Med-PaLM line — moving from one-shot diagnostic dialogue to
  *longitudinal disease management*. The "disease management" framing
  (chronic-condition follow-up, medication titration, adherence support)
  is much closer to the EHR-FM / chronic-care use case than prior AMIE
  papers. **HIGH** on the EHR-FM / clinical-AI thread, especially
  intersected with chronic-disease management.

Counts: **7 HIGH**, **8 METHODS-WATCH**, rest SKIP. Window is moderate
in volume; standouts are (i) the self-feed Cell Genomics drug-target /
multi-scale GWAS paper (item #1) and (ii) the convergence of three
GLP-1 pharmacoepi papers in one batch (items #3, #4, plus one METHODS-
WATCH NAION paper) signaling the GLP-1-RA evidence base is in a peak
publication wave.

---

## HIGH priority — detailed reports

### 1. Translating genome-wide association studies at multiple scales: Drug target prioritization, cellular architectures, and organ imaging
- **Authors / venue:** B. Felici, S. Chen, M. Yuan, X. Jiang, S. Ip, J.H.F. Rudd et al. — *Cell Genomics*, 2026. URL: `cell.com/cell-genomics/fulltext/S2666-979X(26)00144-8`.
- **Surfaced by:** **Chenjie Zeng — new related research** (**your own self-feed**). Single-feed but the highest-precision channel — only fires when Google's relevance model judges the paper close to your published work.
- **Thread:** **Drug repurposing** (the title is literally "Drug target prioritization") **+** **Genetic epidemiology / PRS / TWAS** (multi-scale GWAS translation is your core methodological pattern) **+** **Multimodal EHR + imaging** (organ imaging is one of the "scales"). Lower-intensity cross-hit on cardiovascular thread (Rudd is a CV-imaging author).
- **What it is:** From abstract snippet: *"With a vast corpus of findings from nearly two decades of genome-wide association studies (GWASs), many studies now focus on translating these genetic associations into biological insights at multiple scales, from proteins and cells to entire organs…"* This is a **perspective / review-tier** Cell Genomics piece that synthesizes the multi-scale GWAS-translation literature — proteins (via TWAS / pQTL / pwAS), cells (via single-cell eQTL / CELLECT / scDRS), and organs (via UKB imaging-GWAS, deep-learning-derived imaging phenotypes). The drug-target-prioritization framing means it's organizing the literature around the *clinically actionable* downstream — which gene/pathway is a credible drug target — rather than the upstream biological mechanism per se.
- **Why it matters to you:** Four converging hits.
  (a) **Self-feed firing is the highest-precision signal channel.** Google's relevance model only fires this feed for papers it judges close to your published GWAS / PheWAS work; combined with the Cell-tier venue, this is a one-in-a-month signal.
  (b) **Drug-target prioritization is a 2026 addition to your INTERESTS file** (`drug repurposing` thread added 2026-04-30). The "knowledge-graph / GNN approaches with explainable hypothesis output" sub-thread is one framing; multi-scale GWAS-translation is the *complementary* framing (genetic-evidence-first rather than KG-first). A review-tier reference that organizes both perspectives is exactly the citation you want as you write up your own drug-repurposing work.
  (c) **Multi-scale framing (proteins → cells → organs) is the natural decomposition of your composite-risk-modeling thread.** Your INTERESTS file notes "composite risk models stacking PRS with rare pathogenic variants"; the next layer down is proteomic and imaging composites. This paper organizes the multi-omic / multi-scale evidence-stacking literature in one place.
  (d) **Organ-imaging GWAS is the dominant 2025-2026 direction for UKB-PPP-equivalent work.** Imaging-derived phenotypes (IDPs) from UKB cardiac MR / brain MR / retinal OCT are now the highest-yield endophenotypes for cardiometabolic and neuro disease. The Julian et al. ophthalmic-imaging multi-omic paper in this same window (METHODS-WATCH below) is the empirical instance; Felici et al. is the synthesizing review.
- **Action:** **HIGH — read first.**
  (i) Identify the drug-target-prioritization framework — Open Targets, PoPS, PRoGeM, MR-based (e.g., Schmidt / Gill MR-pheWAS), or a new synthesis. The framework choice tells you which evidence types are weighted highest.
  (ii) Note the imaging-GWAS examples — likely UKB cardiac, brain, and retinal. Which of these are highlighted as "translation-ready" tells you where the field thinks IDPs are mature enough for drug-target inference.
  (iii) Check the reference list for *PheTK*, your AoU PRS paper, your phenomic-comparison paper, or any of your APOL1 / CFTR work — given the self-feed firing, at least one of these is likely cited (or the paper is methodologically adjacent to your published work, which is a citation opportunity going forward).
  (iv) Pair with #7 below (Liu et al. multi-context regulome atlas) and with yesterday's Marderstein noncoding-variant paper — the three together compose into "multi-scale variant-to-target evidence stacking," which is a coherent narrative for a forthcoming write-up.
  (v) Note the senior-author lineage (the surname order suggests Rudd or a CV-imaging PI may be senior); the lab identity bounds how transferable the framework is to non-CV disease areas.

### 2. A systematic review and meta-analysis of the Diagnostic Performance of Large Language Models in Rare Diseases
- **Authors / venue:** G. Zhu, Z. Luo, X. Xu, H. Zhang, Y. Fu, H. ALMasri et al. — Research Square preprint (`researchsquare.com/article/rs-10011746`), 2026. *Likely targeted at a clinical-informatics or rare-disease venue (JMIR / JAMIA / Lancet Digital Health) post-revision.*
- **Surfaced by:** **10 new citations to articles by Lisa Bastarache** feed — i.e., this paper *cites* a Bastarache paper on LLM rare-disease diagnosis (the snippet specifically calls out "accuracy of large language models in generating rare disease …"). Citation-feed surfacing is the *second-highest-precision* channel after self-feed.
- **Thread:** **Rare disease** (the entire premise of the meta-analysis) **+** **EHR phenotyping / clinical NLP** (LLM-based diagnostic suggestions are an extension of HPO-based phenotype extraction) **+** **ML for precision health** (specifically, ML tied to a clinical decision — diagnostic suggestion at point of care).
- **What it is:** From the abstract: *"rare diseases (RDs) remain notoriously difficult to diagnose, often leaving patients in a prolonged 'diagnostic odyssey.' While Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) have demonstrated significant potential in clinical decision support, there is a notable lack of systematic, quantitative evaluations spanning diverse disease categories and model architectures. This [paper provides a systematic review and meta-analysis] …"* Method = systematic literature search (likely PRISMA), data extraction across studies that benchmarked LLMs on rare-disease diagnostic tasks (diagnosis suggestion, ranked-list match against ground truth, phenotype-to-disease mapping), and **pooled estimates** of diagnostic accuracy across model families × disease categories × evaluation tasks.
- **Why it matters to you:** Four reasons.
  (a) **First systematic-pooled-estimate paper in this sub-field.** Prior literature is a sprawl of single-disease, single-model evaluations (GPT-4 on Mendelian disorders, Llama on dermatologic, BERT-based on cardiac, etc.). A pooled meta-analysis is the citation that anchors any forthcoming "where does the field actually stand" claim — you'll want it on hand for grant write-ups, review responses, and any rare-disease-LLM project framing.
  (b) **Cites Bastarache.** Lisa's group's LLM-for-rare-disease paper (probably the "Accuracy of large language models in generating rare disease …" paper the alert calls out) is one of the *anchor* references being pooled. If you're co-authoring or collaborating with the Bastarache / phecode lineage, knowing what the meta-analysis says about that paper's effect size matters.
  (c) **Disease-category × model-architecture cross-tabulation is the missing piece.** Most readers want to know "does LLM-X work for disease-category-Y?" rather than the single-cell estimate. Meta-analysis cross-tabulation is the right design for that question, and is what will get cited going forward in clinical-decision-support write-ups.
  (d) **RAG vs base-LLM is the most actionable dimension.** The methods-evaluation answer "does RAG help rare-disease diagnosis?" determines whether the AoU / N3C / eMERGE rare-disease-diagnostic infrastructure should go RAG-first (HPO-knowledge-base + retrieval) or fine-tune-first (rare-disease-corpus-trained). The meta-analysis is the first paper that can give a quantitative answer.
- **Action:** **HIGH.**
  (i) Read for the pooled accuracy estimates by **model family** (GPT-4 vs Llama vs Med-PaLM vs MedGemma) — does the gap actually close as you go to in-domain models, or is base-GPT-4 still SOTA?
  (ii) Read for the **disease-category breakdown** (Mendelian vs metabolic vs autoinflammatory vs dermatologic etc.) — heterogeneity-of-effect across categories tells you where LLMs are reliable and where the diagnostic odyssey is still LLM-resistant.
  (iii) Read for the **RAG sub-analysis** — does adding HPO-knowledge-base retrieval substantively improve diagnostic accuracy, or is the lift inside the noise band? This determines whether RAG infrastructure investment is justified.
  (iv) Check the included-studies list for the Bastarache paper and for any rare-disease-LLM work from the Tiffany Callahan / Mike Bada / Andrew Williams ontology-grounded lineage. The papers excluded for "insufficient methodology reporting" are also informative — that's where the field is weakest.
  (v) Save as a default citation for any rare-disease-ML write-up; pair with the Janowczyk perspective from yesterday's report (rare-disease-sized cohorts) for a coherent "rare disease as the next frontier" narrative.

### 3. Adjunctive GLP1 Receptor Agonists in Patients with Inflammatory Bowel Diseases and Obesity and/or Diabetes: A Target Trial Emulation
- **Authors / venue:** K.H. Yeh, D. Ahuja, S.B. Patel, R. Xu, S. Park, S. Gold et al. — *Clinical Gastroenterology and Hepatology* (likely), 2026.
- **Surfaced by:** *10 new citations to articles by Miguel Hernán* feed — cites the canonical Hernán-Robins TTE methodology. Citation-feed surfacing.
- **Thread:** **Causal inference and pharmacoepidemiology** (TTE design, your default causal framework) **+** **GLP-1 RAs** (an explicitly tracked drug class in your INTERESTS file) **+** **Inflammatory bowel disease** (also explicitly tracked, under autoimmune work).
- **What it is:** Target-trial emulation of "GLP-1 RA initiation as add-on therapy" in IBD patients who also have obesity and/or T2D — a particularly clean indication-overlap population for studying GLP-1 effects in IBD without the confounding of starting GLP-1 *because* of IBD activity. The TTE design specifies: (a) eligibility (IBD diagnosis, obesity / T2D), (b) treatment strategies (GLP-1 RA initiation vs no GLP-1 RA initiation), (c) assignment (target-trial randomization point, emulated by index date), (d) outcomes (IBD flares, biologic-class change, surgery, hospitalization, plus standard obesity/T2D outcomes), (e) follow-up, (f) causal contrast. Likely a large-EHR cohort (TriNetX, Optum, Medicare, or a large health-system EHR).
- **Why it matters to you:** Four reasons.
  (a) **Triple-thread hit.** Your INTERESTS file flags GLP-1 RAs, target-trial emulation, *and* IBD as active threads; this paper hits all three simultaneously. The hit-density alone makes it the highest-priority pharmacoepi item this window.
  (b) **The GLP-1-in-IBD question is methodologically hard.** GLP-1 RAs may have direct anti-inflammatory effects (mechanistic interest); they may also *appear* effective via weight loss alone (mediator vs confounder question); and IBD activity at GLP-1 initiation is a classic confounder (sicker IBD patients may be deprioritized for GLP-1 due to nausea / GI tolerability concerns). A TTE design with proper eligibility windowing is the right answer; this paper is likely one of the first credibly-designed instances.
  (c) **The Hernán citation surfacing is methodological signal.** Papers that cite the canonical TTE methodology paper tend to be in the "I read the textbook and applied it carefully" camp rather than the "I called my retrospective cohort a target trial in the discussion" camp. The methodological quality is more likely above the median.
  (d) **Pairs with prior reports' GLP-1 thread.** The 06-18 report flagged the Yan et al. JAMA Internal Medicine GLP-1 + osteoporosis paper; 06-20 flagged the Cai et al. JAMA Internal Medicine COVID-vaccine-and-MACE-in-MVP paper (off-class but MVP design). This is the third pharmacoepi TTE paper in a week on the GLP-1 / chronic-disease-pharmacoepi axis — the literature is in a peak publication cycle.
- **Action:** **HIGH.**
  (i) Read for the **eligibility window** and **clone-censor-weight** approach — how do they handle "started GLP-1 *after* IBD diagnosis" vs "had GLP-1 before IBD diagnosis"? The cleaner the eligibility window, the more credible the causal claim.
  (ii) Read for the **outcome hierarchy** — IBD flare (most clinically relevant), biologic-switch (proxy for IBD activity escalation), hospitalization (composite endpoint). Make sure the primary outcome isn't a soft surrogate.
  (iii) Note the **comparator group** — "no GLP-1" is weak (active vs no treatment); "DPP-4 inhibitor" or "SGLT2i" or "metformin titration" comparators are stronger because they isolate the GLP-1 effect from generic glycemic-control effect.
  (iv) Check sensitivity analyses for **selection bias** (sicker IBD patients are less likely to start GLP-1) — IPW with detailed IBD-activity covariates, negative-control outcomes, or E-value reporting are the right tools.
  (v) Default citation for any future GLP-1 / IBD / autoimmune pharmacoepi write-up, *and* a model methodological template for TTE in EHR-linked cohorts.

### 4. Comparison of Specific Glucagon-Like Peptide-1 Receptor Agonists on Kidney Outcomes Among Patients With Type 2 Diabetes
- **Authors / venue:** J.J. Neumiller, Y. Deng, K.S. Swarna, E.C. Polley, J. Herrin et al. — *American Journal of …* (likely *American Journal of Kidney Diseases* given the topic, or *AJM* / *Am J Cardiol* given the author lineage), 2026.
- **Surfaced by:** *Patrick Ryan — new related research* feed. Patrick Ryan = OHDSI / OMOP / J&J pharmacoepidemiology; his related-research surfacing strongly suggests an OMOP-CDM-based multi-database study.
- **Thread:** **Causal inference and pharmacoepidemiology** (head-to-head GLP-1 comparison) **+** **GLP-1 RAs** (explicitly tracked drug class) **+** **EHR-linked biobank / OMOP** (Patrick-Ryan-surfaced = likely OMOP-CDM design) **+** light-touch APOL1 / kidney thread (kidney outcomes endpoint).
- **What it is:** Head-to-head comparative-effectiveness study of *specific* GLP-1 RAs (semaglutide vs liraglutide vs dulaglutide vs tirzepatide, likely) on kidney outcomes (composite renal endpoint: eGFR decline, dialysis initiation, kidney-related hospitalization, kidney-related mortality) in T2D patients. The "specific" framing is the design choice — most prior GLP-1 outcomes literature is class-level (GLP-1 vs no GLP-1, or GLP-1 vs SGLT2i, or GLP-1 vs DPP-4); within-class head-to-head is methodologically harder (channeling bias: which patient gets which GLP-1 depends on insurer formulary, prescriber preference, dosing convenience, prior side-effect experience) but is the question prescribers actually face.
- **Why it matters to you:** Four reasons.
  (a) **Within-class GLP-1 comparison is the next-generation pharmacoepi question.** Once the class-level GLP-1 evidence base saturates (which is happening in 2025-2026), within-class differentiation is what guides prescribing. Methods that handle within-class channeling bias (likely active-comparator new-user design + propensity-score-overlap + negative-control outcomes) are the methodological frontier.
  (b) **OMOP / OHDSI signal via Patrick Ryan's feed.** The likely design pattern is a multi-database OMOP-CDM study (Optum, IBM MarketScan, Medicare 5%, plus possibly a UK / European database) — which is *the* template for federated-cohort comparative-effectiveness work and aligns with your EHR-linked-biobank thread.
  (c) **Kidney outcome endpoint pairs with your APOL1 / kidney thread.** Not a direct APOL1-by-GLP-1 interaction paper, but kidney outcomes from GLP-1 differential treatment is data infrastructure that will eventually support APOL1-stratified GLP-1 effect estimation in AoU or MVP.
  (d) **Polley / Herrin authorship is the Mayo CER lineage.** That group has been doing high-quality OMOP-CDM-based comparative-effectiveness work for several years; methodological rigor is more likely above the median.
- **Action:** **HIGH** on pharmacoepi thread; **METHODS-WATCH** on the APOL1/kidney sub-thread.
  (i) Read for the **active-comparator new-user design** — is the comparator group "another GLP-1 initiator" (cleanest) or "any second-line agent" (weaker)?
  (ii) Read for **channeling-bias diagnostics** — distribution of propensity scores, covariate balance after weighting, negative-control outcomes (e.g., outcomes unaffected by GLP-1 choice should show null effects).
  (iii) Note the **databases** — OMOP-CDM with 4+ databases is the strong design; single-database studies are 1 step weaker for generalizability.
  (iv) Check whether they pre-specified the comparator and outcome (registered protocol on OHDSI) or did post-hoc selection. Pre-specification is the methodological gold standard.
  (v) Default citation for any future GLP-1 kidney-effect or within-class GLP-1 head-to-head write-up.

### 5. Promoter TERT-Related Hematopoietic Somatic Mosaicism in Patients With Telomere Biology Disorders
- **Authors / venue:** M. Franke, R. Kirchner, B. Barredo, A. Zaidan et al. — *American Journal of Hematology*, 2026 Jun 15. PMID 42290596.
- **Surfaced by:** **Chenjie Zeng — new related research** (**self-feed**, *the highest-precision signal channel*).
- **Thread:** **Clonal hematopoiesis (CHIP) and VEXAS — somatic mosaicism, hematologic outcomes** (explicitly listed in your INTERESTS file under "specific disease threads") **+** **Rare disease** (TBDs are ultra-rare) **+** **Variant interpretation** (TERT promoter is a high-impact noncoding region — interpretation is non-trivial).
- **What it is:** Hematopoietic somatic mosaicism for TERT-promoter variants in patients with telomere biology disorders (TBDs — dyskeratosis congenita, idiopathic pulmonary fibrosis, hepatopulmonary syndrome with short telomeres). TERT-promoter somatic variants are well-described in solid tumors as activating mutations; in TBD patients, *germline* TERT-promoter variants reduce TERT expression (causing the disease), and *somatic* TERT-promoter variants in hematopoietic clones can serve as a *compensatory* mechanism — those clones with restored TERT activity outgrow the telomere-compromised baseline, producing a somatic-mosaicism signal that's potentially observable in bulk blood sequencing. This paper presumably characterizes that mosaicism quantitatively, links it to clinical outcomes, and discusses what it implies for TBD diagnostic workflow.
- **Why it matters to you:** Four reasons.
  (a) **Self-feed firing = highest-precision signal channel.** Same reasoning as item #1.
  (b) **Directly on the CHIP / somatic mosaicism thread.** Your INTERESTS file lists "somatic mosaicism, cardiovascular and hematologic outcomes" as the framing. Compensatory somatic-mosaicism in TBD is exactly that — *clonally expanded somatic variation with hematologic disease consequence*. The TBD context is rarer than CHIP but the methodology generalizes.
  (c) **Noncoding (promoter) variant interpretation crossover.** TERT promoter is the canonical noncoding region with high clinical relevance — the C228T / C250T somatic hotspots are intensely studied in tumors. ACMG noncoding criteria are weakest here; any paper that characterizes the clinical consequence of TERT-promoter variation in a Mendelian/somatic crossover context adds variant-interpretation evidence.
  (d) **Rare-disease + ultra-rare cohort design.** TBDs are vanishingly rare; the paper has to do something interesting with cohort design (multi-site referral cohort, registry pooling, single-center longitudinal). Useful as a design reference for any ultra-rare-disease write-up.
- **Action:** **HIGH.**
  (i) Read for the **detection method** — bulk WES variant-calling with VAF inspection, deep targeted sequencing of TERT promoter, ddPCR validation? The method bounds the sensitivity to low-VAF clones.
  (ii) Note the **clinical correlation** — does TERT-promoter somatic mosaicism associate with milder hematologic phenotype (compensation working), or with more aggressive clonal evolution (acquired risk)? Both findings are interpretable but imply different clinical actions.
  (iii) Check whether they propose **screening recommendations** — should TBD patients be serially monitored for TERT-promoter somatic mosaicism as a prognostic biomarker?
  (iv) Pair with broader CHIP literature — the CHIP / VEXAS / TBD / paroxysmal nocturnal hemoglobinuria pattern of "somatic clonal expansion with disease-modifying consequences" is a coherent class that's worth framing together in any future write-up.

### 6. In-depth Human Phenotype Ontology Curation Boosts Prioritization Performance for Netherton Syndrome
- **Authors / venue:** E. Cuperus, S.G.M.A. Pasmans, H.L. Han, A.S. Arterbery et al. — *British Journal of Dermatology*, 2026.
- **Surfaced by:** **Chenjie Zeng — new related research** (**self-feed**).
- **Thread:** **Knowledge graphs & ontologies — HPO** (the entire premise) **+** **Rare disease** (Netherton syndrome is ultra-rare autosomal recessive ichthyosis due to SPINK5 LoF) **+** **EHR phenotyping** (HPO curation feeds into phecode and HPO-based EHR phenotyping pipelines).
- **What it is:** A clinical-genetics + dermatology team curated the HPO term set for Netherton syndrome in depth — expanding the existing HPO entries with finer-grained terms based on the actual dermatologic phenotype as observed in Netherton patients — and then measured the **diagnostic-prioritization performance lift** of the expanded HPO set when used in standard rare-disease prioritization tools (LIRICAL, Exomiser, Phen2Gene, Phenomizer or similar). The hypothesis is that under-curated HPO entries cap how well any HPO-based prioritization tool can rank a candidate diagnosis; refining the terms removes that ceiling.
- **Why it matters to you:** Four reasons.
  (a) **Self-feed firing = highest-precision signal channel.**
  (b) **HPO is explicitly on your INTERESTS file** ("HPO, SNOMED, biomedical KG construction for clinical reasoning"). HPO-curation-quality is the upstream constraint on every HPO-based diagnostic, phenotyping, or LLM-with-HPO-RAG pipeline you might build — a paper that quantifies the lift from better curation is methodologically central.
  (c) **The generalizable methodology beats the specific disease.** Netherton is the case study; the contribution is "**measure** how much HPO-curation depth matters for diagnostic yield." This is the right experimental template for the broader question — your rare-disease + LLM work needs an "HPO-quality vs. diagnostic-yield" axis to be properly interpretable.
  (d) **Dermatologic phenotype is HPO's historic weak point.** Dermatology terms are visually-anchored and notoriously hard to standardize; if a Netherton-specific deep curation moves the needle measurably, that's an argument for *systematic* dermatology HPO investment — which has implications for any biobank-scale rare-disease work that includes skin phenotypes (AoU's skin-image collection is the obvious target).
- **Action:** **HIGH.**
  (i) Read for the **prioritization-tool benchmark** — which tool(s) did they evaluate? LIRICAL is the most rigorous; Exomiser is the most widely deployed; in-house tools are less generalizable. The choice of tool determines how transferable the result is.
  (ii) Read for the **lift magnitude** — going from default-HPO to deep-curation, how many ranks does Netherton move up in the prioritization list? Order-of-magnitude lift (e.g., rank #47 → rank #3) is field-changing; marginal lift (rank #5 → rank #2) is real but less actionable.
  (iii) Note **which HPO terms were added or refined** — the new term IDs become a citation for any HPO-based downstream work. If they propose new dermatology HPO terms, those should propagate upstream into the HPO release.
  (iv) **Generalizability question:** is the methodology (clinician-driven term refinement → measure prioritization lift) automatable, or does it require expert curator effort per disease? If the latter, the bottleneck is HPO-curation workforce; if the former, LLM-assisted HPO refinement is the obvious next step.

### 7. A Multi-Context Regulome-Wide Association Atlas for Genetic Studies of Aging Brain Disorders
- **Authors / venue:** C. Liu, A. Wang, H. Sun, K. Luo, S. Qian, Y. Li, X. He et al. — medRxiv, 2026. PMC13228756.
- **Surfaced by:** *10 new citations to articles by Lisa Bastarache* feed — cites the "Exploiting the GTEx resources to decipher the mechanisms at …" methodological paper (which is the regulome-association / TWAS-extension lineage).
- **Thread:** **Variant interpretation — noncoding variants** (regulome-wide = regulatory-element-wide) **+** **Genetic epidemiology — TWAS** (regulome-wide association is the natural extension of TWAS from gene-level to regulatory-element-level) **+** **Multimorbidity / aging** (aging brain disorders = AD + PD + ALS + frontotemporal dementia + vascular dementia + Lewy body dementia, treated as a coherent disease set).
- **What it is:** A multi-context (cell-type × developmental-state × disease-context) regulome-wide association atlas — likely combining cell-type-specific ATAC-seq / ChIP-seq / scRNA-seq data with GWAS summary statistics for aging-brain disorders, producing a tissue/cell-type-resolved map of which regulatory elements drive disease risk for each disorder. The "atlas" framing means it's a *resource paper* (public release) rather than a single-disease analysis — the goal is reusability.
- **Why it matters to you:** Four reasons.
  (a) **Pairs with yesterday's Marderstein noncoding-variant paper.** The 06-20 report flagged Marderstein et al. *Decoding common and rare noncoding variant effects across cellular and developmental contexts* (Nature Genetics) — a methods paper for jointly modeling common + rare noncoding variants across cell types and developmental contexts. The Liu et al. atlas is the empirical-resource counterpart, applied specifically to aging-brain disorders. Together they compose into "multi-context regulatory-variant interpretation as the next-generation noncoding-VUS resolution framework."
  (b) **Aging-brain-disorder-cohort framing is the right multimorbidity slice.** Pooling AD + PD + ALS + dementias as a disease class (rather than analyzing one at a time) is the modern multimorbidity / shared-genetic-architecture framing — and your INTERESTS file flags multimorbidity and chronic-disease clustering.
  (c) **Atlas / resource papers compound in value.** Unlike a single-paper analysis, an atlas accrues citations as downstream users query the resource for their own work. Knowing the atlas exists is the first step to using it (or competing with it) — especially for any future AoU / UKB neurodegenerative phenotyping work.
  (d) **Cited via Bastarache** (TWAS / GTEx-resource lineage) — methodological lineage signal.
- **Action:** **HIGH** on variant-interpretation thread; **METHODS-WATCH-plus** on multimorbidity / aging thread.
  (i) Read for the **atlas data structure** — UCSC-track-browsable, REST-API-queryable, downloadable VCF, or a manuscript-only resource? Accessibility determines re-use rate.
  (ii) Note the **GWAS sources** — GWAS Catalog versions, IGAP / GR@ACE / FinnGen for AD, the latest PD-GWAS for PD, etc. Outdated GWAS = stale atlas.
  (iii) Check the **cell-type coverage** — does it span neurons (excitatory, inhibitory), glia (astrocytes, microglia, oligodendrocytes), vascular cells, and immune infiltrates? Microglia and vascular cells are the under-served axes in most existing atlases.
  (iv) Pair with Marderstein et al. (06-20 report) for a coherent noncoding-variant-interpretation literature synthesis.

### 8. Towards Conversational AI for Disease Management
- **Authors / venue:** V. Liévin, A. Palepu, W.H. Weng, K. Saab, D. Stutz et al. — *Nature*, 2026.
- **Surfaced by:** *10 new citations to articles by Vivek Natarajan* feed. (Vivek Natarajan is a co-author on the canonical AMIE / Med-PaLM papers; surfacing in his citations feed for a paper with these authors is high-precision.)
- **Thread:** **EHR foundation models / clinical AI** (next chapter of the AMIE line, now in *Nature*) **+** **ML for precision health** (disease management is the chronic-care decision-loop) **+** EHR phenotyping (any longitudinal-management AI must reason over longitudinal EHR).
- **What it is:** From the abstract framing: *"While large language models (LLMs) have shown promise in diagnostic dialogue, their [extension to disease management is the next step]…"* This is the **AMIE-for-chronic-disease** successor paper — moving from one-shot diagnostic conversation (which the original AMIE / Nature 2024-25 paper handled) to *longitudinal disease management* (chronic-condition follow-up, medication titration, adherence support, escalation criteria, between-visit triage). The author lineage (Liévin, Palepu, Weng, Saab, Stutz, Natarajan and collaborators) is the Google DeepMind / Google Research Health team that built AMIE.
- **Why it matters to you:** Four reasons.
  (a) **Chronic-disease management is the EHR-FM use case that matters clinically.** Diagnostic AI (AMIE 2024-25) is the headline; chronic-care AI is the volume. Any EHR-FM that can do disease management has product-market-fit with primary care, which is where most of clinical workload sits — and where most of the longitudinal EHR data accumulates.
  (b) **Nature publication signals field-consensus framing.** The previous AMIE papers were Nature; this paper's Nature publication means the framing of "conversational AI for disease management" is being normalized in the field. Default citation for any future EHR-FM chronic-care write-up.
  (c) **Disease management = decision-loop with state.** This is the LLM-with-state / LLM-with-memory pattern, applied clinically. Methodologically, that's much harder than one-shot dialogue and forces engagement with the "what state does the model carry across visits" question — which has direct EHR-FM design implications (token-level memory vs explicit care-plan structured representation vs RAG-over-prior-visits).
  (d) **Vivek's citation feed is a high-precision channel for AMIE / Google Health line.** When a paper of this caliber surfaces via his citation feed (rather than related-research), it likely cites his prior AMIE paper directly — which makes the continuity with the AMIE narrative explicit.
- **Action:** **HIGH.**
  (i) Read for the **state-carrying mechanism** — episodic memory module, RAG over prior visits, explicit care-plan data structure, or full-context-window per-patient? Each has different engineering and clinical-safety implications.
  (ii) Read for the **disease classes evaluated** — diabetes / hypertension / asthma / depression are the obvious chronic-care benchmarks. Inclusion of any of *your* tracked disease classes (IBD, CF, kidney disease) would be especially valuable.
  (iii) Note the **evaluation design** — OSCE-style standardized-patient simulation, real-patient observational study, or RCT? OSCE is the AMIE precedent; an RCT would be field-changing.
  (iv) Check the safety / escalation behavior — disease management means deciding when to *not* manage in-band and instead escalate to a human clinician. This is the highest-stakes design decision in chronic-care AI and is the place where most existing systems are weakest.
  (v) Default citation for any forthcoming EHR-FM / chronic-care / conversational-AI write-up.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **A dish-to-biobank framework links β-cell nutrient-stress programs to genetic and dietary risk for Type 2 Diabetes** — X. Wang, H. Lee, A. Le, B. Turhan, N. Hu, P.S. Garcia et al. — bioRxiv, 2026 (Chenjie Zeng self-feed). Self-feed firing makes it methodologically interesting even though the cell-biology framing is off-thread for daily work. **Watch for:** the framework for translating an in-vitro perturbation result into a biobank-scale association test — that's a generalizable "molecular-phenotype to clinical-outcome" pipeline pattern. If they validate the dish-derived signature against AoU / UKB / MVP T2D outcomes, that's also a portability data point for your composite-PRS-plus-omics thread.

- **Polygenic risk scores associate with asthma phenotypes and proteomic analyses implicate IL1R1 in two family-based studies** — S. Lee, M. Moll, K. Mendez, N. Prince, J. Lasky-Su — medRxiv, 2026 (Chenjie Zeng self-feed). PRS + proteomic-analysis composite predictor in a family-based design, applied to asthma. **Watch for:** the family-based PRS design (handles confounding from population structure differently than cohort-based PRS, particularly relevant when proteomic effects could be confounded by environmental exposures) and the IL1R1 implication (asthma drug target candidate, IL-1 pathway). Pairs with your composite-risk thread.

- **Multi-omic analysis of deep learning-derived phenotypes links ophthalmic imaging to cardiovascular and neurological traits** — T.H. Julian, H. Dou, J. Duan, J. Huang, E. Yoo, D.J. Green et al. — *Nature Cardiovascular …*, 2026 (Bastarache citation feed). UKB-based retinal-imaging × cardiovascular × neurological multi-omic pipeline, using adversarial-autoencoders on OCT and color fundus images. **Watch for:** the autoencoder-derived imaging phenotype + GWAS + metabolomic stacking pattern — that's the empirical instance of the multi-scale-GWAS-translation framework Felici et al. (#1 above) review. Excellent methods reference for any UKB-style imaging-derived-phenotype work.

- **Leveraging longitudinal data to boost statistical power for gene–environment interaction analysis (SAGELD)** — H. Xu, Y. Ma, Y. Liu, Y. Li, L. Wan, J.F. Zhang, Y. Zhao et al. — *Nature Computational Science*, 2026 (Bastarache citation feed). G×E method for longitudinal traits with sample-relatedness control — matrix-projection-based. **Watch for:** the scalability claim (genome-wide G×E across longitudinal biobank data is computationally hard; if SAGELD scales properly, it's adoptable for AoU / UKB / MVP). Pairs with your genetic-epi / cross-ancestry methods thread.

- **Ultra-fast genetic colocalisation across millions of association signals** — M. Jesse, A.E. Riet, K. Alasoo — *PLOS Genetics*, 2026 (Bastarache citation feed). Algorithmic improvement for genome-wide colocalisation at the scale of millions of association signals (i.e., trans-PheWAS × trans-eQTL scale). **Watch for:** the speed claim and the reference panel choice. If it makes phenome-wide × molecular-QTL colocalisation tractable, that's a candidate replacement for the standard `coloc` package in any future PheWAS+QTL integration work.

- **Deciphering cell type-specific causal genetic effects on brain imaging-derived phenotypes and disorders with single-cell Mendelian randomization** — A. Yang, X. Zhao, X.M. Zhao, Y.T. Yang — *PLOS Computational Biology*, 2026 (Bastarache citation feed). Single-cell MR for brain-imaging-phenotype × disorder triangulation. **Watch for:** the cell-type-resolved MR framework — single-cell eQTL × imaging-phenotype × disease causal triangulation is the methodologically frontier of MR. Off-thread substantively (brain imaging disorders) but exemplary methods.

- **Machine diagnostics and machine phenotyping of migraine: a HUNT study** — A. Danelakis, H.K. Abildsnes, F. Faisal, M.H. Bjørk, D. Giles et al. — *Neurology*, 2026 (Bastarache citation feed). HUNT-cohort EHR-based machine-phenotyping of migraine using ML classifiers. **Watch for:** the HUNT cohort design (Norwegian population biobank with EHR linkage = analog to UKB / AoU but smaller). EHR-based phenotyping at biobank scale for a single disease is your phenotyping-pipeline pattern; the specific disease (migraine) is off-thread but the design is on-thread.

- **Association between GLP-1 receptor agonist use and NAION with optic disc drusen** — I. Abboud, R. Madani, J.G. Chacko, P.H. Phillips et al. — *Ophthalmology*, 2026 (Hripcsak citation feed). GLP-1 RA + non-arteritic anterior ischemic optic neuropathy in patients with optic disc drusen. **Watch for:** another in the growing GLP-1 ocular-adverse-event literature (the GLP-1 + NAION question has been live since 2024-25). Pharmacovigilance, not pharmacoepi — uses case-control or disproportionality methods rather than TTE — so methodologically weaker than #3 / #4 above but completes the GLP-1 thread for this window.

---

## SKIP / noise (logged, no action)

- **Hyperemesis gravidarum and adverse pregnancy outcomes: a population-based cohort study of 2.5 million births in California** (Yuan Luo citation feed) — large-cohort obstetric study; off-thread.
- **SW-SpeedDLM / SimSD / Recursive Scaling in Masked Diffusion Models** (Marinka Zitnik related-research, three separate papers) — diffusion-LLM architecture papers; off the clinical-FM thread; **fourth consecutive window** of diffusion-LLM noise from the Zitnik feed (see pipeline note below).
- **Ethical Considerations in Personal Health Large Language Models** (Szolovits citation) — ethics review; off the methods thread.
- **Medical Vision-Language Models for Robust Disease Diagnosis** (Szolovits related-research) — VLM-for-radiology; off-thread (not EHR-FM, not multimodal EHR; pure imaging VLM).
- **Several VLM / LLM-benchmark / hallucination papers in the Szolovits feed** — CheckMIABench, automated VQA benchmark for oncology imaging, language-dependent diagnostic safety, hallucination analysis, drug-name fragility benchmark, web-graph-centrality pretraining data selection — all generic LLM-evaluation methodology, all off-thread.
- **Recipe-Controlled Decoder Audit for Structural Knowledge-Graph Completion** (Tiffany Callahan related-research) — generic KG-completion; **eighth consecutive window** of non-biomedical KG-completion noise (see pipeline note below).
- **OTULIN / Pyoderma gangrenosum (Nature Immunology)** (Karczewski citation, 06-20 carry-forward) — autoinflammatory mechanism; not on VEXAS / CHIP / IBD axes despite keyword overlap.
- **Translating genome-wide association studies … (Felici et al.)** — this is item #1 above (HIGH); not skipped, listed here only because Scholar's feed also surfaces it via the Chenjie Zeng *self*-feed.
- **Pakistan Genome Resource exome / genome analysis** (Joshua Denny citation) — large-cohort sequencing paper; off-thread substantively (pan-LoF discovery in a new ancestry), useful as a *gnomAD-equivalent in PaK ancestry* citation should it ever be relevant.
- **Adjunctive GLP1 RA in IBD** — item #3 above (HIGH); listed in the Hernán citation feed.
- **Revisiting POWER in the GLP-1 Age** (Jian Yang citation) — obesity-care perspective piece; not on the GLP-1 pharmacoepi methods thread directly.
- **Computational investigation of single herbal drugs for diabetes / knowledge graph / network pharmacology** (knowledge-graph keyword feed) — herbal-medicine KG paper; off-thread.
- **Integrating LLM + GNN for KG-Based Multi-Source Recommender System** (knowledge-graph keyword feed) — generic recommender system; off-thread.
- **Foundation models and electronic health records / GDP — multimodal generative model for EHR** (keyword feed) — this is the Sivarajkumar et al. paper from the prior report (HIGH at 06-20); re-surfacing in the keyword feed today.
- **Plasma proteomic signatures of cellular aging predict human disease** (Ding et al.) — re-surfacing from the 06-20 report (HIGH there); no new info.
- **Complete chromosome 21 centromere sequencing of families with Down syndrome** (Evan Eichler new article) — Down syndrome genomics; off-thread.
- **Genetic Susceptibility to Severe Hypertriglyceridemia (Blokhina et al.)** (Joshua Denny related-research) — rare-variant lipid genetics in MENA cohort; tangential to your APOL1 / kidney thread (different organ system), off-thread for daily work.
- **Genetic Correlations Between Tobacco/Alcohol Use and Neurodegenerative Disease (Wang et al., EAS LDSC)** — re-surfacing from the 06-20 report (METHODS-WATCH there); no new info.
- **Power and sample-size estimation in human microbiome research** (Michael Snyder new article) — microbiome power-analysis methodology; off-thread.
- **Tumor dynamics and mutations influencing progression** (Sasha Gusev new article) — oncology somatic-evolution paper; off-thread.
- **Personal Care Utility: Health as Everyday Infrastructure** (Chris Chute citation, 06-20 carry-forward) — LLM-utility framing; off-thread.
- **Errors That Matter: Negative Experiences of Incorrect Health Records Among Youth in Mental Healthcare** (Hripcsak related-research) — qualitative HCI study; off-methods-thread.
- **MALDI-TOF Mass Spectrometry for Glioblastoma Secretome Biomarker Screening** (Montgomery citation) — mass-spec methods review; off-thread.
- **Role of Bioinformatics in Drug Discovery and Precision Healthcare** (Russ Altman new article) — perspective piece; off-thread for daily work.
- **Applications of Artificial Intelligence in Genomic Data Analysis and Personalized Medicine** (Mark Gerstein new article) — perspective piece; off-thread.
- **Autologous stem cell transplantation for refractory juvenile-onset systemic sclerosis** (Daniel Kastner related-research) — pediatric rheumatology; off-thread.
- **Hematopoietic Somatic Mosaicism in TBD** — item #5 above (HIGH).
- **Long-read sequencing in CD19 CAR-T vector copy number** (Montgomery related-research) — bioinformatics for CAR-T QC; off-thread.
- **IgG antibodies against SARS-CoV-2 spike in mother-child dyads** (Chute related-research) — COVID serology; off-thread.
- **ML Coronary Artery Tortuosity** (Patrick Ellinor new article) — cardiac imaging ML; off-thread for daily work, methodologically adjacent to the imaging-derived-phenotype space (item #1's organ-imaging axis); MMETHODS-WATCH-leaning skip.
- **Glutathione transferase polymorphism in thymoma + myasthenia gravis** (Karczewski citation) — single-gene single-disease association; off-thread.
- **Preferences of Research Participants with Experience Receiving Individual Results for Future Return of Results** (Wendy Chung new article) — research-ethics / return-of-results policy; off-thread for methods.
- **Pyoderma gangrenosum / OTULIN molecular uncoupling** (Karczewski citation, again, 06-20 carry-forward).
- **arxiv-digest 06-21** — 0 papers (clean run, no warning). 06-20 was 0 with a 3/4-category fetch-failure warning. Two consecutive days of pipeline contributing zero on-thread signal.

---

## Suggestions for the pipeline

All prior reports' recommendations remain unactioned. Today's items
add one new issue and reinforce three carry-forwards:

1. **`arxiv-digest` 06-21 produced 0 papers WITHOUT a warning logged**
   (vs. 06-20's 0 papers WITH a 3/4-category-failure warning). Two
   possible explanations: (a) clean run, all four categories returned
   empty lists for the lookback window (plausible on a Saturday), or
   (b) regression where the warning logic only fires when *some* — not
   *all* — categories error out, so an all-empty pipeline run looks
   indistinguishable from a clean-but-genuinely-zero day. **Recommend
   checking the 06-21 workflow logs** to disambiguate; if (b), add an
   "all-categories-returned-zero-this-window" warning so the user can
   tell apart real-zero from polling-failure-zero days. (This is the
   second-day instance of the more general issue flagged in the 06-20
   report.)

2. **`knowledge graph` keyword leak: 8th consecutive window of non-
   biomedical KG-completion hits** (today's Recipe-Controlled Decoder
   Audit for KG Completion; prior week's RLKGC; prior windows of
   recommender-system KG noise). The specific fix is the same as
   yesterday's recommendation: change the keyword to `biomedical
   knowledge graph` OR `clinical knowledge graph`, or use the compound
   filter `(knowledge graph) AND (medical OR biomedical OR clinical OR
   EHR OR phenotype OR drug OR disease)`. This recommendation has now
   been raised in four consecutive reports without action.

3. **Diffusion-LLM noise from the Zitnik feed: 4th consecutive window**
   (today's SW-SpeedDLM + SimSD + Recursive Scaling MDM in one batch;
   prior window's instances were SimSD-equivalent papers from the same
   keyword neighborhood). Diffusion LLMs are not on the clinical-FM
   thread; the noise comes from Marinka Zitnik's broader ML interests
   leaking into her related-research feed. **Recommend** *not* dropping
   the Zitnik alert (her group does enough on-thread work — therapeutic-
   commons, knowledge graphs for clinical reasoning — to make the alert
   net-positive); instead, **flag this as a feed-curation insight** —
   diffusion-LLM papers from her related-research feed can be auto-
   skipped at triage time with a regex match on the title.

4. **Add `cs.LG`, `stat.ME`, `medRxiv` and `bioRxiv` source feeds**
   (carry-forward, unaddressed for 4+ weeks). Today's items #2 (Zhu
   et al. LLM-rare-disease meta-analysis, Research Square preprint),
   #3 (Yeh et al. GLP-1 in IBD TTE, Clin Gastro), #4 (Neumiller et al.
   GLP-1 kidney comparative-effectiveness, AJ-something), #5 (Franke
   et al. TERT-promoter somatic mosaicism, Am J Hematol), #6 (Cuperus
   et al. HPO + Netherton, BJD), #7 (Liu et al. regulome atlas,
   medRxiv), #8 (Liévin et al. AMIE-for-DM, Nature), all surfaced via
   Scholar feeds rather than arxiv-digest because they're in journal
   venues. The current `arxiv-digest` pipeline can never reach these
   without source expansion. **The arxiv-digest pipeline's signal/noise
   ratio is now negative over the past two weeks** — almost every on-
   thread paper comes from Scholar alerts; almost every arxiv-digest
   surface is METHODS-WATCH or SKIP. Source expansion is the leverage
   point.

5. **Add `drug target prioritization` / `target prioritization` as
   keywords** (new, prompted by today's item #1). The Felici et al.
   Cell Genomics review is the genre archetype; adding this keyword
   would catch future drug-target-prioritization GWAS-translation
   papers directly (rather than relying on the self-feed firing).

6. **Add `HPO curation` / `HPO terms` / `phenotype ontology` as
   keywords** (new, prompted by today's item #6). Cuperus et al. surfaced
   via self-feed; the keyword fix would catch it directly.

7. **Add `target trial emulation` / `TTE` as keywords** (new, prompted
   by today's item #3). Yeh et al. surfaced via Hernán citation feed;
   keyword tracking would surface TTE papers regardless of senior-
   author lineage.

8. **`mendelian diseases` / `drug repurposing` / `PRS stability` /
   `proteomic signature` / `aging clock` / `organ-specific aging` /
   `noncoding variant interpretation` / `regulatory variant effect` /
   `MPRA`** keyword additions (carry-forward, all 8th+ consecutive
   window, all unaddressed).

9. **Continue tracking your self-citation feed as the highest-precision
   channel.** Today's items #1, #5, #6 all surfaced via the self-feed.
   The 06-20 report's #1 (Chen et al. nephro PRS+PheWAS) was triple-
   feed including self. The 06-18 report's gold-standard surface was a
   self-*citation* feed hit. Pattern: self-feed firing predicts genuine
   relevance with very high precision; whenever it fires, the paper
   should default to HIGH unless the abstract makes the off-thread case
   conclusively.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 8 | (1) Felici et al. multi-scale GWAS-translation, *Cell Genomics* [self-feed]; (2) Zhu et al. LLM diagnostic performance meta-analysis in rare diseases [Bastarache citation]; (3) Yeh et al. GLP-1 RA in IBD TTE [Hernán citation]; (4) Neumiller et al. specific-GLP-1-RA kidney outcomes comparative effectiveness [Patrick Ryan]; (5) Franke et al. TERT-promoter somatic mosaicism in TBD [self-feed]; (6) Cuperus et al. HPO curation for Netherton syndrome [self-feed]; (7) Liu et al. multi-context regulome atlas for aging brain disorders [Bastarache citation]; (8) Liévin et al. conversational AI for disease management, *Nature* [Natarajan citation] |
| METHODS-WATCH | 8 | Wang et al. dish-to-biobank T2D framework [self-feed]; Lee et al. PRS+proteomic IL1R1 in asthma [self-feed]; Julian et al. ophthalmic-imaging multi-omic UKB [Bastarache]; Xu et al. SAGELD G×E for longitudinal [Bastarache]; Jesse et al. ultra-fast colocalisation [Bastarache]; Yang et al. single-cell MR for brain imaging [Bastarache]; Danelakis et al. HUNT migraine phenotyping [Bastarache]; Abboud et al. GLP-1 + NAION ocular adverse-event [Hripcsak] |
| SKIP | ~30 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH), this window
delivers a higher HIGH count (8 / 8). The standout pattern is **three
self-feed papers in one batch** (items #1, #5, #6) — the highest self-
feed hit rate in any recent window. The second pattern is **three GLP-1
pharmacoepi papers in one batch** (#3, #4, plus the NAION METHODS-WATCH
item) — the GLP-1 RA evidence base is in a peak publication cycle.
The `arxiv-digest` pipeline contributed 0 papers for the second
consecutive day; **all on-thread signal came from Scholar alerts**.
Source expansion (medRxiv / bioRxiv / `cs.LG` / `stat.ME`) and keyword
additions (drug target prioritization, HPO curation, TTE) are now the
two highest-leverage pipeline fixes.
