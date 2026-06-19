# Research digest report — 2026-06-19

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-18 (post 06:59Z Scholar batch covered yesterday) →
2026-06-19**. Yesterday's 06-18 report explicitly stopped before the
2026-06-18 13:40Z Scholar keyword batch, the NCBI What's New batches,
the 06-18 arxiv-digest commit, and the 06-19 00:00Z bioRxiv/medRxiv
subject-collection alerts; all of those fall inside today's window.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar keyword alerts (11 distinct keywords) | 2026-06-18 13:40Z | Batch of 11 keyword alerts after the morning author/citation batch. Keywords: phenome-wide association studies, All of Us Research Program, rare diseases, mendelian diseases, UK Biobank, electronic health records, drug repurposing, variant interpretation, autoimmune disorders, foundation models + EHR, knowledge graph. |
| NCBI "My NCBI What's New" PubMed digests | 2026-06-18 12:32Z | UK Biobank (17 items), drug repurposing (11 items), All of Us (2 items). |
| `arxiv-digest` repo (`digests/2026-06-18.md`) | 2026-06-18 10:30Z cron | **3 papers, all off-thread** (see below). |
| bioRxiv subject-collection alert | 2026-06-19 00:01Z | Bioinformatics / Genetics / Genomics / Immunology / Pathology. |
| medRxiv subject-collection alert | 2026-06-19 00:05Z | Epidemiology / Genetic & Genomic Medicine / Health Informatics / Obstetrics / Oncology / Pediatrics. |
| `arxiv-digest` for 2026-06-19 | not yet produced | Cron has not run at report time. |

> ⚠️ **The arxiv-digest pipeline is dry again today.** Yesterday's
> output (06-18) added **3 papers, all off-thread**:
> (i) Schulz & Ritter — *Measurement noise limits the advantage of
> nonlinear over linear models in biomedical prediction* (cs.LG, UK
> Biobank tasks, score 2). Actually a useful general-methods read for
> *anyone doing tabular ML on biobank-scale data*; see METHODS-WATCH
> below.
> (ii) Dyck & Sauzet — *WSPsignal R package for Weibull-shape-parameter
> pharmacovigilance signal detection* (stat.ME, score 1, EHR keyword
> leak via "electronic health records").
> (iii) Seiffarth et al. — *DART microfluidic chip paradigm for live-cell
> imaging* (q-bio.QM, score 1, CHIP-keyword false-positive on
> "microfluidic chip"). Confirms that the `chip` keyword still
> false-positives on hardware as well as the older microelectronic
> false-positives previously flagged.
> Virtually 100% of on-thread signal today again came from
> Scholar/PubMed/medRxiv alerts; items #1, #2, #5, #6, #7 below
> would have surfaced from the pipeline only if the recommended
> medRxiv + cs.LG + JAMA-network feeds were added.

> Caveat: Scholar/PubMed/biorxiv alert emails contain title, authors,
> venue, and the first ~2-3 lines of each abstract only. The reports
> below contextualize that metadata against your research threads;
> nothing here reflects full-text reading.

---

## Executive summary

- **Biggest hit: a Vanderbilt EHR-pediatrics paper from your direct
  collaborator network.** Palmer, Shyr, Morley, Han, Bejan, Walsh,
  Ruderfer (medRxiv, 2026) — *Adverse Childhood Experiences and Growth
  Outcomes in Childhood: A Longitudinal EHR-Based Study*. Bejan, Walsh,
  Ruderfer are VUMC, on your immediate orbit; the framing — ACEs as a
  longitudinal EHR-derived exposure, growth-trajectory as the outcome —
  is squarely on the EHR-phenotyping + multimorbidity-trajectory
  thread. **Read first** if you haven't already (this is your group's
  network).
- **Cleanest pharmacoepi hit of the week: a target-trial-emulation
  paper on semaglutide and adult-onset seizure in *Neurology*.**
  Eun, Bong, Koh, Trousdale, Cho, Jang, Lee (Neurology, 2026; PubMed
  *All of Us* alert) — *Semaglutide and Risk of Adult-Onset Seizure: A
  Target Trial Emulation*. Sits at the explicit intersection of two
  INTERESTS-file threads — *target trial emulation* under causal
  inference & pharmacoepi, plus *GLP-1 RAs* as an active drug-class
  thread. Neurology venue + AoU/PubMed-alert pickup means this is
  likely the new default citation for any GLP-1 + neurological
  off-target outcome write-up.
- **Karczewski/Saxena multi-trait sleep + rare coding variant paper.**
  Zhang, Lu, Kunorozva, Jones, Maher, Valliere, Wood, Weedon, Tubbs,
  **Karczewski**, Ge, Tiemeier, Lane, Saxena, Ollila, Chen (medRxiv,
  2026) — *Rare Coding Variants Reveal Distinct Genetic Architectures
  Across Multidimensional Sleep Phenotypes*. Konrad Karczewski + Richa
  Saxena + Tian Ge + Andrew Wood + Michael Weedon authorship is the
  rare-variant-burden / Karczewski-lab signature. Multi-trait rare
  coding-variant burden is the pattern you've been tracking under
  composite risk + rare-variant association.
- **First explicit FM-on-EHR paper of the week.** Sivarajkumar, Zhang,
  Ji, Bilalpur, Wu, Li et al. (npj Health Systems, 2026) — *A
  multimodal generative model for structured and unstructured
  electronic health records*. Surfaces in **two** of your keyword
  feeds (the *"electronic health records"* feed and the *"Foundation
  models + EHR"* feed). Generative model on structured + unstructured
  jointly is on the multimodal-EHR-FM axis that's been thin in your
  recent feeds.
- **EHR FM ICD-code modeling paper from the modern CLMBR/MOTOR
  lineage.** Thukral, Kang, Singh, Hiremath, Hänsel et al. (arXiv,
  2026) — *Hierarchical Modeling of ICD Codes in EHR Foundation
  Models*. Directly on the CLMBR/MOTOR/MEDS lineage in your INTERESTS
  file. Hierarchical ICD modeling is the natural next step after
  MEDS-style flat tokenization; pair with Steinberg / Shah / Pfohl
  prior work.
- **AlphaGenome-as-VUS-resolver paper, with a clinical case lock.**
  Eger, López, Gómez Navarro, Peña-Tauber, Cochran, Hiatt, Gelvez,
  García-García, Lobo, Greicius, Matallana, Acosta-Uribe, Kosik
  (medRxiv, 2026) — *AlphaGenome identifies a deep intronic variant in
  a family with PLA2G6-associated neurodegeneration: Closing the
  diagnostic gap in rare genetic diseases*. Squarely on the
  *splicing/RNA evidence for VUS resolution* arm of variant
  interpretation, plus the rare-disease and AI-for-diagnosis arms.
  Greicius/Kosik lineage adds Stanford-style clinical neurogenetics
  credibility.
- **Sleeper hit: an Ohno-Machado multi-site privacy-preserving
  EHR-selection-bias paper, JAMIA.** Kundu, Salvatore, Patel,
  Ohno-Machado et al. (JAMIA, 2026) — *Privacy-enhancing sequential
  learning under heterogeneous selection bias in multi-site electronic
  health records data*. Surfaces in the EHR + foundation-models-EHR
  feeds; pairs with the Mitchell AoU-reweighting paper below for an
  evolving *selection-bias-across-biobanks* sub-thread.
- **Methods-grade AoU paper from Emory.** Mitchell (Emory, 2026, web)
  — *Comparative Evaluation of Reweighting Methods to Address
  Selection Bias in the All of Us Research Program*. Solo-author
  paper hosted on Yang group page at Emory; first dedicated
  reweighting-method comparison in AoU.
- **Rare-disease-sized cohorts in Lancet Digital Health.** Janowczyk,
  Merkler, Michielin, Madabhushi (Lancet Digital Health, 2026) —
  *Precision medicine's inevitable trajectory toward rare-disease-sized
  cohorts: implications for machine learning and deep learning*.
  Madabhushi's pathology-informatics group; argues precision-medicine
  ML increasingly faces rare-disease sample sizes and adapts methods
  accordingly. Tracks your rare-disease + ML-for-precision-health
  threads.
- **Imaging-derived phenotype GWAS lands in *Med*.** Liu, Guo, Yan,
  Yu, Hu, Deng, Yan, Li, Cai, Deng, Wang, Yu (Med, 2026) — *Atlas of
  human brain imaging-derived phenotypes and disease risk*. Continues
  the *imaging-derived phenotype + GWAS* sub-thread you flagged
  yesterday with Tian et al. liver radiomics. Brain MRI-derived
  phenotypes catalogued + disease-risk mapped at *Med* venue.
- **PheWAS infrastructure paper, methods-grade.** Chen & Liao (Comput
  Biol Chem, 2026) — *Detecting disease comorbidity based on SNP
  association on PheWAS scale*. Methods-watch; phenome-wide
  comorbidity detection from shared SNP signals — relevant to your
  PheWAS / phecode infrastructure work, though small lab.
- **Useful pipeline-side measurement-noise paper from the arxiv-digest.**
  Schulz & Ritter (cs.LG, 2026, arxiv-digest 06-18) —
  *Measurement noise limits the advantage of nonlinear models over
  linear models in biomedical prediction*. The one arxiv-digest item
  this window worth reading; argues that whenever linear ≈ flexible
  on UK Biobank tabular tasks, the *binding* limit is measurement
  reliability, not the model. Directly useful for any time you compare
  PRS, EHR-feature, or omics-feature predictors and have to defend the
  linearity baseline.
- **Carry-forward duplicates from yesterday's batch:** the Pell et al.
  *APOL1 + TCR + transplant rejection* paper (JCI) does NOT re-surface
  today; it was the dominant HIGH item yesterday. The Schatz et al.
  *KG-explanation-extraction for drug repurposing* paper (ACM TCH) also
  doesn't re-surface today. No carry-forward duplicates this window.
- **No new on-thread items for:** CF/CFTR (the bioRxiv 2-paper CFTR
  cluster from Pion, Miller, Raraigh, Cutting is mechanistic
  /functional, not on the CFTR-modulator-pharmacoepi arm of your
  CF thread — logged METHODS-WATCH), no new CHIP/VEXAS, no new IBD,
  no new ACMG/ClinGen statement, no new MVP/BioVU, no new direct
  PRS-stability paper.

Counts: **9 HIGH**, **8 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. Adverse Childhood Experiences and Growth Outcomes in Childhood: A Longitudinal EHR-Based Study
- **Authors / venue:** S. Palmer, C. Shyr, T.J. Morley, J. Shelley, L. Han, J.H. Simmons, C. Bejan, C. Walsh, D.M. Ruderfer — *medRxiv*, 2026 (preprint 2026.06.15.26355527).
- **Surfaced by:** medRxiv *Pediatrics* subject-collection alert (2026-06-19 00:05Z).
- **Thread:** EHR phenotyping & OMOP (longitudinal EHR-derived exposure + outcome) **+** ML for precision health (clinical decision-grade pediatric growth trajectories) **+** multimorbidity/trajectory adjacent.
- **Why it matters specifically to you:** **Co-authors are your immediate
  VUMC orbit.** Cosmin Bejan, Colin Walsh, Doug Ruderfer are
  Vanderbilt — directly on your network. The phenotyping pattern —
  ACEs as a *computable phenotype from longitudinal EHR* with growth
  outcomes mapped over follow-up — fits the computable-phenotype +
  EHR-phenotyping arm of your interests file exactly. Pediatric growth
  trajectory outcomes are also adjacent to the trajectory-clustering
  / latent-trajectory arm under multimorbidity.
- **What it is (abstract framing, limited to alert snippet):**
  Longitudinal EHR-based study linking ACEs to growth outcomes in
  childhood. Likely uses Vanderbilt SD/eMERGE-style cohort or BioVU
  pediatric arm.
- **Action:** **HIGH — read first.**
  (i) Confirm the EHR source (BioVU/SD vs national EHR network) and the
  ACE-phenotyping algorithm (rule-based vs NLP-extracted, ICD vs
  free-text).
  (ii) Note the growth-trajectory modeling approach (latent-class
  growth, mixed-effects, spline-based) — directly transferable to any
  pediatric trajectory clustering you'd do in AoU.
  (iii) Likely useful as a co-author / interest-network ping; this is
  your group's footprint.

### 2. Semaglutide and Risk of Adult-Onset Seizure: A Target Trial Emulation
- **Authors / venue:** Y. Eun, S. Bong, H.Y. Koh, R.K. Trousdale, Y.M. Cho, Y. Jang, S.T. Lee — *Neurology*, 2026 (published online 2026-06-17, print 2026-07-14; PMID 42308439).
- **Surfaced by:** NCBI PubMed "All of Us" What's-New alert (2026-06-18 12:32Z).
- **Thread:** Causal inference & pharmacoepi (**target trial emulation** — explicit) **+** GLP-1 RA drug-class thread (also explicit) **+** ML for precision health (deciding when to deploy a GLP-1 in a patient with seizure history).
- **What it is:** Target trial emulation comparing semaglutide initiation to a non-GLP-1 comparator for the outcome of adult-onset seizure incidence. The combination of (a) **TTE** as the explicit design, (b) **GLP-1 RA** as the exposure of interest, (c) **neurological off-target outcome** as the question, and (d) publication in *Neurology* makes this the dominant default citation going forward for any *GLP-1-and-neurological-outcome* question — a corner of the GLP-1 literature that has been growing fast but with mixed-quality designs.
- **Why it matters to you:** Hits two of your INTERESTS-file threads at their explicit named intersection:
  (a) "Target trial emulation, propensity score / IPW, g-methods, and modern causal ML... Active drug-class threads: GLP-1 RAs, SGLT2is..." — this paper is *the* GLP-1 TTE paper of the week. After last week's Hatano et al. orthopaedics-TTE tutorial, this is a substantive TTE *on the drug-class you're actually tracking*, not a methods walkthrough.
  (b) *Neurology* venue means this becomes the citation for any future analyses you do involving GLP-1 + CNS outcomes (seizure being one of the harder-to-confound classes of CNS endpoints since it's an acute event rather than a chronic-disease label).
  (c) If they used AoU as the data source, that's a triple intersection (TTE + GLP-1 + AoU); the PubMed "All of Us" alert pickup is suggestive but not confirmed — verify in the abstract.
- **Action:** **HIGH — read first (along with #1).**
  (i) Confirm the data source — AoU? VA MVP? Korean NHIS (Korean PI list)? This determines portability.
  (ii) Note the TTE protocol details: eligibility criteria, treatment-strategy specification, sustained vs initiator analyses, comparator choice (active vs none).
  (iii) Capture the effect size and confidence-interval width — Neurology will have demanded a tight design.
  (iv) Add to your active GLP-1 / TTE working bibliography.

### 3. Rare Coding Variants Reveal Distinct Genetic Architectures Across Multidimensional Sleep Phenotypes
- **Authors / venue:** Y. Zhang, W. Lu, L. Kunorozva, S.E. Jones, M. Maher, J. Valliere, A.R. Wood, M.N. Weedon, J.D. Tubbs, **K. Karczewski**, T. Ge, H. Tiemeier, J. Lane, R. Saxena, H.M. Ollila, C.-Y. Chen — *medRxiv*, 2026 (preprint 2026.06.16.26355625).
- **Surfaced by:** medRxiv *Genetic and Genomic Medicine* subject-collection alert (2026-06-19 00:05Z).
- **Thread:** Genetic epidemiology (rare coding-variant burden, multi-trait) **+** variant interpretation (LOFTEE / pLoF burden, implicit) **+** ML for precision health / composite-risk-model adjacent.
- **What it is:** Multi-trait rare coding-variant burden analysis across multiple sleep phenotypes. Author lineage is the Karczewski (gnomAD / LOFTEE / pLoF) + Saxena (sleep genetics) + Andrew Wood / Michael Weedon (Exeter UK Biobank rare-variant burden specialists) + Tian Ge (PRS portability) signature — i.e., the cleanest possible authorship signal for a rare-variant burden paper.
- **Why it matters to you:**
  (a) **Karczewski-network** — Konrad Karczewski is on your Scholar author-feed list specifically because his lab outputs the LOFTEE / gnomAD / pLoF tooling you use. A rare-variant paper with his name on it is automatic on-thread.
  (b) **Composite risk** — INTERESTS file calls out "Composite risk models stacking PRS with rare pathogenic variants." A multi-trait rare-variant decomposition across sleep phenotypes is the rare-variant half of that composite, and the multi-phenotype framing (which trait does the rare variant matter for?) is directly the question composite-risk modeling asks.
  (c) **Sleep multi-phenotype** — sleep is a tracked-condition under your aging / multimorbidity thread (sleep regularity already appeared yesterday in the Chen Sleep paper, today's UK Biobank batch). Pairs naturally.
- **Action:** **HIGH.**
  (i) Read for the burden-test framework (SAIGE-GENE+? STAAR? regenie?) and the gene-set definition (pLoF + missense pathogenic, LOFTEE-filtered, etc.).
  (ii) Note which sleep phenotypes diverge in rare-variant architecture from common-variant GWAS — this is the *informative* part for future composite-risk thinking.
  (iii) Check if any gene comes up across multiple sleep phenotypes — those are the pleiotropic-rare-variant candidates worth tracking for transferability to other multimorbidity-cluster work.

### 4. A multimodal generative model for structured and unstructured electronic health records
- **Authors / venue:** S. Sivarajkumar, H. Zhang, Y. Ji, M. Bilalpur, X. Wu, C. Li et al. — *npj Health Systems*, 2026 (URL: nature.com/articles/s44401-026-00095-y).
- **Surfaced by:** Scholar keyword feeds — **two feeds simultaneously**: *"electronic health records"* and *"Foundation models + EHR"* (2026-06-18 13:40Z). Double-feed pickup.
- **Thread:** EHR foundation models (multimodal — structured + unstructured) **+** EHR phenotyping & OMOP.
- **What it is:** A multimodal generative model ("GDP" per their own abstract) for jointly handling structured EHR (demographics, vitals, labs, codes) plus unstructured clinical notes. From the snippet: "GDP's architecture could, in theory, be extended with additional encoders for these modalities (and some recent works do explore multimodal foundation models, including imaging), but we did not incorporate or test those" — i.e., structured + notes is in, imaging is acknowledged but out of scope.
- **Why it matters to you:** This is one of the cleaner instances of the *generative* multimodal EHR FM pattern your INTERESTS file calls out — MEDS / EHRSHOT / CLMBR / MOTOR are mostly *predictive* tokenization-based; this is generative + structured + notes. The npj Health Systems venue is new (npj-family but explicitly health-systems-flavored) and likely to host more of these; worth knowing the title for any future EHR FM literature scan. Surfacing in *both* the EHR keyword feed and the explicit FM+EHR feed means the keyword pipeline is at least catching it twice — which is helpful when you re-read these reports.
- **Action:** **HIGH.**
  (i) Read for the joint encoder/decoder design — are the structured codes tokenized in MEDS style or as a separate stream? How are notes encoded (BERT-family? Llama-family? frozen vs co-trained)?
  (ii) Note the downstream tasks they evaluate on — if these include phenotype prediction or computable-phenotype generation, the paper is directly useful for your phenotyping work.
  (iii) Check the dataset — MIMIC? UPMC? eICU? AoU? — and whether structured/notes alignment was forced through encounter-id joins or learned.

### 5. Hierarchical Modeling of ICD Codes in EHR Foundation Models
- **Authors / venue:** M. Thukral, D.G. Kang, R.P. Singh, S.K. Hiremath, K. Hänsel et al. — *arXiv preprint* arXiv:2606.15447, 2026.
- **Surfaced by:** Scholar keyword feed *"Foundation models + EHR"* (2026-06-18 13:40Z).
- **Thread:** EHR foundation models (CLMBR / MOTOR / EHRSHOT / MEDS lineage) **+** EHR phenotyping & OMOP.
- **What it is:** Architecture paper exploiting the hierarchy of ICD codes (chapter → subchapter → category → subcategory) inside a Transformer-based EHR foundation model. From the abstract snippet: "Many of these methods were developed in the pre-foundation-model era and are trained end-to-end... a head within modern Transformer-based EHR foundation models" — i.e., they propose a hierarchical-ICD-aware head/representation on top of standard MEDS/MOTOR-style backbones.
- **Why it matters to you:** Hits the *CLMBR, MOTOR, EHRSHOT, MedTok, FEMR, MEDS lineage* call-out in your INTERESTS file directly. ICD-code hierarchy exploitation is a known gap in flat-tokenization EHR FMs — most of those tokenize each ICD code as its own token, losing the natural phecode-like hierarchy. The phecode community has long argued for hierarchical phenotyping; this paper is the FM-side analogue. Likely citable in any future write-up where you want to argue for phecode-grouped or hierarchical phenotype tokenization.
- **Action:** **HIGH (methods-watch leaning).**
  (i) Read for the hierarchy-injection mechanism — pretraining loss modification? Architectural prior (e.g., tree-position embeddings)? Hierarchical softmax?
  (ii) Compare empirically against MOTOR / CLMBR baselines on whatever downstream tasks they use.
  (iii) Note whether they generalize to OMOP-CDM codes or just ICD — important for portability to AoU/MVP/BioVU.

### 6. AlphaGenome identifies a deep intronic variant in a family with PLA2G6-associated neurodegeneration: Closing the diagnostic gap in rare genetic diseases
- **Authors / venue:** S.J. Eger, G. López, L.F. Gómez Navarro, A. Peña-Tauber, J.N. Cochran, S.M. Hiatt, N. Gelvez, M. García-García, S. Lobo, M.D. Greicius, D.L. Matallana, J. Acosta-Uribe, K.S. Kosik — *medRxiv*, 2026 (preprint 2026.06.10.26355004).
- **Surfaced by:** medRxiv *Genetic and Genomic Medicine* subject-collection alert (2026-06-19 00:05Z).
- **Thread:** Variant interpretation (ACMG / ClinGen, **splicing / RNA evidence for VUS resolution** — explicit) **+** rare disease (**deep phenotyping for rare-disease diagnosis** — explicit) **+** ML for precision health.
- **What it is:** A clinical-case-grounded application of AlphaGenome (DeepMind's whole-genome regulatory/splicing predictor, released late 2025) to identify a deep intronic variant in PLA2G6 — a known neurodegeneration gene — that closes a long-standing diagnostic odyssey for a family. Combines (a) AlphaGenome predictions, (b) Stanford-Greicius clinical neurogenetics, (c) Kosik (neurodegeneration), (d) Colombian rare-disease cohort (Acosta-Uribe / Matallana, U. de los Andes / U. del Rosario). This is the exact *AI-VUS-resolution* archetype your INTERESTS file lists as high-priority.
- **Why it matters to you:** Three reasons.
  (a) **Splicing / deep-intronic / VUS resolution** is the most clinically-impactful slice of variant interpretation right now — most ACMG/ClinGen frameworks struggle with non-coding variants, and a clinical-deployment paper that shows AlphaGenome closing a real case is exactly the citation you'd want when arguing for AlphaGenome / SpliceAI / Pangolin-style tools in a population-screening VUS workflow.
  (b) PLA2G6 is in the *rare pathogenic variant* category — neurodegeneration with brain iron accumulation. Composite-risk-model arguments where rare pathogenic variants drive penetrance estimation under population screening (your INTERESTS file thread) need exemplar variants like this one.
  (c) The undiagnosed-family → diagnosis pipeline is the cleanest write-up structure for *AI-assisted clinical variant interpretation*; valuable as a template.
- **Action:** **HIGH.**
  (i) Read for the AlphaGenome score thresholds they used and whether they did orthogonal RNA-seq / minigene validation (likely; closing a diagnostic gap formally requires functional confirmation, not just predictor confidence).
  (ii) Note how they reconcile AlphaGenome predictions with existing splice predictors (SpliceAI, Pangolin) — does AlphaGenome win on this specific variant, and what's the prediction-magnitude differential?
  (iii) Track for the next-generation ACMG/ClinGen VCEP statement on integrating AI splicing tools — this paper will be cited as evidence.

### 7. Privacy-enhancing sequential learning under heterogeneous selection bias in multi-site electronic health records data
- **Authors / venue:** R. Kundu, M. Salvatore, K.K. Patel, **L. Ohno-Machado** et al. — *Journal of the American Medical Informatics Association*, 2026 (URL: academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocag083/8708528).
- **Surfaced by:** Scholar keyword feeds *"electronic health records"*, *"Foundation models + EHR"*, *"All of Us research program"* (2026-06-18 13:40Z) — **triple-feed pickup**.
- **Thread:** EHR phenotyping & OMOP (**multi-site EHR, heterogeneous selection** — explicit) **+** Biobanks with EHR linkage (AoU mentioned in abstract as a contrast cohort) **+** causal inference & pharmacoepi (selection-bias methodology).
- **What it is:** Methods paper for estimating disease-risk parameters across multi-site EHR data where each site has its own selection mechanism, without sharing individual-level data. From the abstract: "Recruitment strategies vary widely, from the disease-enriched surgical cohorts of the Michigan Genomics Initiative (MGI), to the demographically representative national cohort of the NIH All of Us Research Program (AOU). These differing [selection mechanisms]..." — i.e., the explicit framing is "MGI vs AoU" as the canonical disease-enriched-vs-representative biobank contrast, with their method bridging the two without raw-data sharing.
- **Why it matters to you:** Two angles.
  (a) **Selection-bias-across-biobanks is becoming its own sub-thread.** This paper + the Mitchell AoU-reweighting paper (item #8) + the persistent population-genetics-portability literature are converging on a coherent question: *when do you trust a biobank-derived risk parameter for population-level deployment?* This Kundu paper is the federated-statistical-methods angle. Ohno-Machado authorship is the gold-standard signature for this corner of biomedical informatics.
  (b) Practically actionable: any future write-up where you fit a risk model in BioVU and want to claim AoU generalizability (or vice-versa) needs to either harmonize the selection mechanism or apply a reweighting/sequential-learning method. This paper is the methodology you'd cite.
- **Action:** **HIGH.**
  (i) Read for the specific selection mechanisms modeled (deterministic enrichment? volunteer self-selection? clinic-of-recruitment effects?) and the sufficient-statistics they communicate between sites.
  (ii) Check if they validate on AoU + MGI + a third biobank (BioVU? UKB?) — the trinity would be the most convincing.
  (iii) Bookmark for the next AoU-related selection-bias question.

### 8. Comparative Evaluation of Reweighting Methods to Address Selection Bias in the All of Us Research Program
- **Authors / venue:** E. Mitchell — Emory CS preprint, 2026 (URL: cs.emory.edu/~jyang71/files/aou-reweighting.pdf, hosted by Jian Yang at Emory).
- **Surfaced by:** Scholar keyword feed *"All of Us research program"* (2026-06-18 13:40Z).
- **Thread:** Biobanks with EHR linkage: **All of Us** (explicit) **+** causal inference & pharmacoepi (selection-bias correction) **+** ML for precision health.
- **What it is:** Solo-author technical preprint comparing reweighting methods (IPW family, calibration-weighting, raking, propensity-score weighting, machine-learning-based weighting) for correcting selection bias in AoU. Hosted on Jian Yang's Emory CS page, which suggests this is a Yang-supervised student work — the Yang group at Emory has been working on AoU statistical foundations for a couple years.
- **Why it matters to you:** Direct fit to the *biobank selection bias* sub-thread surfacing this week (paired with Kundu et al., item #7). AoU is on your INTERESTS-file high-priority list, and the reweighting-method comparison is the practical question every AoU analyst hits: "I have a non-representative volunteer cohort — which of the seven plausible reweighting methods do I use?" A side-by-side comparison answers that with empirical guidance.
- **Action:** **HIGH (methods-watch leaning).**
  (i) Read for the comparison metric — bias reduction in known-truth simulations? Closeness to ACS / NHANES marginals after weighting? Out-of-sample replication?
  (ii) Track whether it ends up in JAMIA or Stat Med or a med-info venue (current PDF is a preprint manuscript).
  (iii) Cross-reference against the Kundu et al. method (item #7) — Kundu is multi-site federated, this is single-site AoU; complementary not overlapping.

### 9. Precision medicine's inevitable trajectory toward rare-disease-sized cohorts: implications for machine learning and deep learning
- **Authors / venue:** A. Janowczyk, D. Merkler, O. Michielin, A. **Madabhushi** — *The Lancet Digital Health*, 2026 (URL: sciencedirect.com/science/article/pii/S2589750026000233).
- **Surfaced by:** Scholar keyword feed *rare diseases* (2026-06-18 13:40Z).
- **Thread:** Rare disease (**explicit** — title) **+** ML for precision health (**explicit** — title) **+** ML methods for small cohorts.
- **What it is:** Perspective/review in *Lancet Digital Health* arguing that as precision medicine subdivides populations into ever-more-specific patient strata, the effective per-stratum sample size collapses toward rare-disease territory — and that ML/DL methods need to adapt accordingly. From the abstract: "tailoring treatments to highly specific patient subgroups, the rise of rare-disease-sized cohorts (RDSCs) presents a formidable challenge... infrastructure and associated algorithmic approaches, drawing lessons from rare disease research."
- **Why it matters to you:** This is a *framing* paper that articulates a concept your INTERESTS file already implicitly tracks — rare-disease methods (HPO-based deep phenotyping, ultra-rare clinical NLP, rare-variant association methods) generalize to precision-medicine sub-populations broadly. Madabhushi's authorship gives it ML-pathology credibility; *Lancet Digital Health* venue gives it visibility. Likely to become a cited framing paper in any rare-disease + ML grant or paper for the next 18 months.
- **Action:** **HIGH (read for framing, not methods).**
  (i) Note the specific recommendations they make for "RDSC algorithms" — likely federated learning, transfer learning, foundation-model finetuning, Bayesian priors, simulation-based-inference.
  (ii) Capture the framing language ("RDSC", "rare-disease-sized cohorts") in case it becomes the standard term.
  (iii) Add to citation list for any precision-health-on-rare-conditions write-up.

---

## METHODS-WATCH (exemplary methods, off-thread or methods-only)

- **Measurement noise limits the advantage of nonlinear models over linear models in biomedical prediction** — M.-A. Schulz, K. Ritter — *arXiv* 2606.18420 (cs.LG), 2026; surfaced via `arxiv-digest 2026-06-18.md`. Argues with an exact excess-risk identity that a degree-*k* interaction is attenuated by the *k*-th power of feature reliability while the linear part is attenuated only once — so at typical biomedical measurement reliabilities, the nonlinear advantage vanishes even when the underlying biology is strongly nonlinear. Empirically validated on 140 UK Biobank tasks. *Watch for:* the operational implication for *any* PRS vs ML comparison you do — if a tree ensemble ties logistic regression, the binding constraint may be measurement noise (genotyping error, phecode misclassification, lab-measurement noise) rather than model capacity. This is the cleanest theoretical justification for *not* over-celebrating LR ≈ XGBoost ties on EHR tabular tasks.

- **Atlas of human brain imaging-derived phenotypes and disease risk** — Q. Liu, J. Guo, J. Yan, S. Yu, Y. Hu, Y. Deng, B. Yan, P. Li, J. Cai, Z. Deng, Z. Wang, J. Yu — *Med*, 2026 (PMID 42309062, PubMed UK Biobank alert). Continues the imaging-derived phenotype + GWAS sub-thread from yesterday's Tian et al. liver radiomics paper. *Watch for:* the comprehensiveness of brain IDP catalog and whether they ship summary statistics for downstream PRS construction.

- **Detecting disease comorbidity based on SNP association on PheWAS scale** — L. Chen, L. Liao — *Comput Biol Chem*, 2026 (PMID 42308866, PubMed UK Biobank alert). PheWAS-scale comorbidity detection from shared SNP signals — methodologically adjacent to phecode comorbidity networks. *Watch for:* the comorbidity-graph construction method (does it use phecodes? raw ICD? cluster the SNP-shared phenotype pairs?) — useful as a comparator for any phecode-comorbidity network work.

- **RetiMap: Automated Retinal Vascular Measures Link Microvascular Structure to Metabolic Health and Predict Cardiovascular Risk** — Y. Talmor-Barkan, M. Shapira, S. Shilo, M. Gorodetski, D. Azouri, Y. Aviv, Y. Reisner, A. Godneva, A. Weinberger, A. Skaat, A. Loewenstein, E. Berkowitz, R. Kornowski, **E. Segal**, H. Rossman — *JACC Basic Transl Sci*, 2026 (PMID 42308589, PubMed UK Biobank alert). Eran Segal group — automated retinal vascular trait extraction → metabolic phenotype → CV risk. *Watch for:* the segmentation pipeline and whether they connect retinal-vascular IDPs to GWAS / PRS workflows (i.e., is this an imaging-derived-phenotype paper or a pure prediction paper?). Pairs with item under imaging-phenotype sub-thread.

- **Translating genome-wide association studies at multiple scales: Drug target prioritization, cellular architectures, and organ imaging** — B. Felici, S. Chen, M. Yuan, X. Jiang, S. Ip, J.H.F. Rudd, M. **Inouye** — *Cell Genomics*, 2026 (PMID 42309052, PubMed drug-repurposing alert). Review/perspective from the Inouye group integrating GWAS → drug-target prioritization, cellular architecture, and organ imaging — i.e., the *three downstream translation axes* for GWAS. *Watch for:* their proposed prioritization framework — if it formalizes a pipeline (GWAS → cell-type → tissue → drug target → repurposing candidate) you may want to cite this in any drug-repurposing-from-GWAS argument.

- **Hard to Halt: Automation Bias in Agent-Driven Sequencing Prior Authorization Workflows** — M. Nie, W. Chung, J. Waxler, M. Lee, **C. Weng**, R. Lewis, P. Ahimaz, **K. Wang**, C. Liu — *medRxiv*, 2026 (preprint 2026.06.16.26355782, medRxiv Health Informatics alert). LLM-agent automation bias in clinical sequencing prior-auth workflow — Chunhua Weng + Kai Wang authorship (Columbia clinical informatics + clinical genomics). *Watch for:* the specific failure modes of agent-driven clinical decision automation — useful when arguing for human-in-the-loop in any LLM-assisted clinical genomics workflow you build.

- **CFTR function in nasal airway cells from symptomatic and asymptomatic CF heterozygotes** + **Clinical and primary cell evidence reveals complex CFTR function-phenotype relationships** — two paired papers from the Cutting/Raraigh lab — *bioRxiv*, 2026 (bioRxiv Genetics alert). Functional characterization of CFTR variants in heterozygote nasal airway cells, with implications for CF carrier phenotypes. Off the pharmacoepi side of your CF thread but on the *variant interpretation + functional validation* side. *Watch for:* whether they establish a function-phenotype map useful for VUS resolution in CFTR carriers — directly relevant to the population-screening / carrier-penetrance question.

- **Glaucoma in UK Biobank: A Comparison of Diagnostic- Versus Treatment-based Definitions** — W. Sun et al. — *Ophthalmology*, 2026 (PMID 42309491). Phenotype-definition comparison study in UK Biobank — exactly the *computable-phenotype validation* genre. *Watch for:* the agreement / discordance between Dx-code and Rx-based phenotype definitions; this is the canonical pattern your phecode + EHR-phenotyping thread benchmarks against.

---

## SKIP / noise (logged, no action)

- **`arxiv-digest 2026-06-18`** (3 papers): Schulz/Ritter promoted to METHODS-WATCH above; Dyck/Sauzet *WSPsignal R package* — score-1 keyword leak on "electronic health records", actually a pharmacovigilance signal-detection package, not on-thread; Seiffarth et al. *DART microfluidic chip* — score-1 false-positive on `chip` keyword (microfluidic chip, no relation to clonal hematopoiesis).
- **Scholar *phenome wide association studies* feed**: Wu et al. *pediatric obesity Taiwan GWAS+PheWAS* (J Formosan Med Assoc) — off-thread disease; Chen et al. *nephrolithiasis genome-phenome PRS* (Kidney Dis) — off-thread.
- **Scholar *All of Us research program* feed beyond Mitchell item**: Gadelmawla et al. *heavy-metal CV/metabolic ML review* (Cardiovasc Toxicol) — keyword brush by AoU; Kim et al. *East/SE Asian American queer-identities content analysis* (psycnet) — keyword leak; Herzig et al. *assortative mating + vertical cultural transmission on genetic associations* (Theor Pop Biol) — relevant population-genetics methods but not AoU; Amarasena et al. *migraine care India/Sri Lanka* — clinical, off-thread; Reyneker *onychauxia toenails* — clinical, off-thread.
- **Scholar *rare diseases* feed beyond Janowczyk item**: Mansoob et al. *RaraSwed Swedish national RD registry* (BMC Glob Public Health) — registry paper; Ramos et al. *Brazil RD epidemiology* — Brazilian referral-center descriptive; Baynam et al. *RD preparedness* — policy perspective; Nguyen et al. *LiteOdyssey AI agent for RD diagnosis* (arXiv) — adjacent, light methods novelty; Wang et al. *MedLatentDx multi-agent communication for cross-hospital RD diagnosis* — adjacent, multi-agent novelty; Lace et al. *RD research barriers in underrepresented European countries* (Eur J Public Health) — policy; Fernández-Vilas et al. *social phenomenon of RD logical-modal analysis* (Front Sociol) — humanities; Sinha *bioanalytical CRO services for RD drug development* — industry; Alary et al. *quality of life in rare liver disease* (Health Expect) — qualitative.
- **Scholar *mendelian diseases* feed**: Xiang et al. *Methotrexate causal relationship with COPD via MR + network toxicology* — Mendelian Randomization, not Mendelian disease; the keyword still leaks MR papers (**7th consecutive window** — see pipeline suggestions).
- **Scholar *UK Biobank* feed beyond Liu (METHODS-WATCH)**: Qu et al. *deficit accumulation frailty → incident CKD UKB+CHARLS* (Int Urol Nephrol); Kelly et al. *socioeconomic differences in cardiometabolic risk factors* (BMJ Public Health); Huang et al. *insulin resistance surrogate indexes + psoriasis* (Research Square); Lu et al. *stair climbing + valvular heart disease* (Front Cardiovasc Med); Zabad *PRS biobank-scale algorithms thesis* (McGill); Chen et al. *sleep regularity + ocular aging* (Sleep); Xue et al. *atherogenic index of plasma + CMM cardiovascular-kidney-metabolic* (Cardiovasc Diabetol); Fu et al. *physical activity + sleep + depression* (BMC Public Health); Shen et al. *TyG index + biological aging + CVD risk* (Cardiovasc Diabetol) — all UKB cohort epidemiology, mostly cardiometabolic, not on-thread specifically.
- **Scholar *electronic health records* feed beyond Sivarajkumar + Kundu (HIGH)**: Zhang et al. *predicting lab test ordering in ED with structured+unstructured EHR ML* (JMIR Med Inform); Lit et al. *DPARD Dutch national diabetes registry* (Diabetes Epi Glob Health); Curammeng et al. *EHR usage + nurse eye fatigue*; Baljevic et al. *light-chain amyloidosis + ATTR diagnostic workup using US EHR*; Ikonen *EHR usability + patient safety physician survey*; Wong et al. *primary care + public health integration*; Pranasari/Aditama *technology in elderly chronic disease QoL*; Cummins/Liu *environmental + social determinants for pneumonia readmission ML* (Digital Health).
- **Scholar *drug repurposing* feed beyond Schatz (yesterday) carry-over**: Chen et al. *DRQuantum quantum walks on multi-layered heterogeneous network* (Sci Rep) — quantum-walk method on KG; conceptually adjacent to explainable-KG-repurposing thread, but lacks the explanation-extraction angle. Logged as adjacent but not HIGH (compare to Schatz et al. yesterday which was on the explanation thread). Other items in feed: Irshad et al. *cloud computing for drug repurposing leveraging academic idle resources* — infrastructure; Abdelsayed *computational pipelines for disease-specific drug repurposing* — generic review; Rodage *repurposing antimalarial Lumefantrine for TNBC* — chemistry-only; Sabale/Patil *AI in drug discovery review* — generic; Ainslie *AI in pharmaceutical research* — generic; Arora et al. *PanDTP-12 drug-tolerant persister gene program* — cancer pharmacogenomics; Praveen *protein-ligand interactions for anti-TB drug discovery* — chemistry; Gong *pentose phosphate metabolism + astrocyte AD AI-driven drug repurposing* — AI + drug-repurposing in AD but not on the clinical-evidence-loop thread; Vanjale et al. *AI-enhanced network pharmacology* — generic. The DRQuantum paper deserves a 30-second skim if interested in quantum-walk methods on biomedical KGs, but is not on the *explainable KG repurposing* thread your INTERESTS file specifies.
- **Scholar *variant interpretation* feed beyond Eger (HIGH) + Grech & Pace**: Li et al. *hemostatic profiles + hypertensive disorders of pregnancy multi-omics MR* — MR not variant interpretation; Franssen/Kaiser *MKRN3 missense mutations in central precocious puberty* (Curr Opin Pediatr) — single-gene clinical review; Verma et al. *genetic biomarkers in sudden cardiac events* — review.
- **Scholar *autoimmune disorders* feed**: Shravya et al. *divergent autoimmune genetic landscapes in diabetic vs non-diabetic individuals* (BMC Genomic Data) — Indian-population PRS in autoimmune; Alkhatib et al. *HCQ-associated cardiomyopathy case-based review* — case report; Lahouty et al. *exosomes in celiac disease* — mechanistic; Libera et al. *premature hair graying* — clinical; Guo/Huang *immune reset via BMT* — review.
- **Scholar *knowledge graph* feed**: Lee/Kuo *LLM+GNN for KG-based recommender* — e-commerce; Zhao et al. *KnowPath KGQA* — generic KGQA; Arman et al. *dynamic KG forecasting scientific knowledge evolution* — generic; Liu et al. *robust multi-modal KGC via modality experts* — generic; Alselwi et al. *KG-enhanced memory-augmented retrieval for long context* — generic; Khani et al. *model graph inductive learning KGC* — generic; **Jin et al. *CME-KGDTI: integrating clustered mutations into KG embedding for drug-target interaction prediction* (BioData Mining)** — drug-target interaction prediction on a biomedical KG with clustered mutations as a layer; adjacent to your drug-repurposing-on-KG thread but skews toward drug discovery rather than repurposing. Worth a 30-second look. Shan/Luo *recipe-controlled decoder audit for KGC* — generic; Cazzaro et al. *grounded text-to-Cypher* — generic; Li et al. *ETC-KG hybrid KG construction* — application.
- **PubMed *UK Biobank* feed beyond items already covered**: 17 items, the majority cardiometabolic + biobank-cohort observational; the imaging-derived-phenotype atlas (Liu et al., *Med*) is METHODS-WATCH above; Chen/Liao PheWAS comorbidity is METHODS-WATCH; the rest are mostly traditional UKB cohort epidemiology not on a tracked disease thread.
- **PubMed *drug repurposing* feed beyond Eun semaglutide-TTE (HIGH item #2)**: Lueangaramkul et al. *FDA-approved drugs vs feline infectious peritonitis 3CLpro* — veterinary; Li/Gao/Liu *GLP-1 RAs in neurological disorders review* (Drug Des Devel Ther) — review framing, adjacent to GLP-1 thread but review-only; Xie et al. *DTANet+ drug-target affinity* — chemistry; Felici et al. *GWAS-to-drug-targets* is METHODS-WATCH above; Wang et al. *druggable-genome MR for atherosclerotic CAD* — MR pharmacology; Okunade et al. *N-acetylcysteine RCT in early-onset preeclampsia* — clinical trial; Tyagi et al. *metformin neuroprotection mechanistic review* — mechanism; Famta et al. *statins for HNSCC repurposing systematic review*; Sharata et al. *PCOS comprehensive review*; Mouawia et al. *ivermectin + SARS-CoV-2 asymptomatic RCT* — old retro-active.
- **PubMed *All of Us* feed beyond Eun (HIGH item #2)**: Attia et al. *head & neck manifestations in sarcoidosis AoU case-control* — clinical descriptive; logged.
- **medRxiv subject-collection items beyond highlighted ones**: a batch of off-thread items across Epidemiology / OBGYN / Oncology / Pediatrics; the on-thread items are #1 (Palmer ACEs), #3 (Zhang sleep rare variants), and #6 (Eger PLA2G6) above. Other notables logged but not HIGH: Cao et al. *maternal/fetal HLA heterozygosity in preeclampsia multi-ancestry pregnancy cohort* (medRxiv Genetic & Genomic Medicine) — pregnancy genetics; Shah et al. *MOSAIC methylation classifier for acute leukemia* — cancer epigenetics methods; AL Yazeedi et al. *structural variation landscape in MENA from long-read nanopore* — ancestry SV catalog; Levy et al. *pretrained LLMs for suicide risk prediction from VA clinical notes* — VA NLP, adjacent to MVP veterans thread but clinical-NLP focused.
- **bioRxiv subject-collection items**: large batch of mostly off-thread bioinformatics methods (Hi-C, single-cell, vaccine design, structural bio). The two CFTR-function papers from Cutting/Raraigh logged METHODS-WATCH above. Liu et al. *cross-platform nanopore benchmarking with methylation-associated substitution errors* (bioRxiv Bioinformatics) — possibly relevant to LR-SV interpretation but off the human-population-genetics thread.

---

## Suggestions for the pipeline

Prior recommendations stand. None of today's 9 HIGH items were
surfaced by `arxiv-digest`; all came from Scholar / PubMed /
bioRxiv-medRxiv subject feeds. Reiterated with one new addition:

1. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds** (7th
   report). Items #1, #3, #5, #6, #7 today (Palmer ACEs, Zhang sleep
   rare variants, Thukral hierarchical-ICD EHR FM, Eger AlphaGenome
   PLA2G6, Kundu multi-site EHR selection bias) are all medRxiv /
   arXiv / JAMIA-style sources outside the current q-bio / stat.AP
   feed set.
2. **`mendelian diseases` keyword: 7th consecutive window of MR leakage.**
   Today's hit was Xiang et al. methotrexate-COPD MR. Recommendation
   unchanged: replace with `OMIM` / `MIM:` IDs or exclude
   `-randomization`.
3. **`knowledge graph` keyword: 7th consecutive window of non-biomedical
   leakage.** Recommendation unchanged.
4. **`drug repurposing` keyword: still target-only.** Today's actually-on-
   thread repurposing item was the GLP-1 TTE paper (Eun, item #2), surfaced
   by PubMed *All of Us* feed, not by the `drug repurposing` keyword scan.
5. **`chip` keyword: false-positives now extend to hardware.** Today's
   `arxiv-digest 06-18` surfaced a *microfluidic chip* paper (Seiffarth
   et al.) — a *different* class of false positive than the earlier
   `chipset` / `microelectronic chip` false positives. Recommend
   tightening to `clonal hematopoiesis` / `CHIP variants` / `DNMT3A
   TET2 ASXL1` literal hits rather than the 4-letter `chip` word.
6. **(NEW) `EHR foundation model` / `EHR FM` as an explicit phrase keyword.**
   Item #5 today (Thukral hierarchical ICD codes in EHR foundation
   models) is the exact pattern your INTERESTS file calls out (CLMBR /
   MOTOR / EHRSHOT / MEDS lineage), but a generic `electronic health
   records` scan brings it up in a pile of EHR-usability and
   pharmacovigilance papers. A dedicated phrase keyword would isolate
   the FM-on-EHR lineage cleanly.
7. **(NEW) `target trial emulation` as a phrase keyword.** Item #2 today
   (Eun semaglutide-seizure TTE) was the *Neurology* TTE of the week
   and surfaced only via the `All of Us` PubMed feed. A dedicated
   `target trial emulation` keyword on the arxiv-digest side would
   directly hit the most clinically-actionable corner of your
   causal-inference thread, and would also have hit yesterday's Hatano
   orthopaedics-TTE paper.
8. **(NEW) `AlphaGenome` as a keyword.** Item #6 today (Eger PLA2G6
   AlphaGenome paper) is the first explicit AlphaGenome-clinical-
   deployment paper to land in the post-release era. AlphaGenome + the
   class of related splicing-AI tools (SpliceAI, Pangolin, Pangolin2)
   are now a tracked sub-class under variant interpretation; a
   dedicated keyword catches them directly.
9. **Track when your own group / direct collaborators publish.** Item #1
   today (Palmer + Bejan + Walsh + Ruderfer ACEs paper) is a VUMC
   paper from your collaborator network. The PheTK-self-citation feed
   from yesterday and this Palmer paper both argue for keeping the
   self/collaborator-author Scholar feeds active — they're the single
   highest-precision signal you have.
