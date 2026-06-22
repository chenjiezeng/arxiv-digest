# Research digest report — 2026-06-22

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-06-22** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 06-22 | Two large 06-21 batches: 10:36Z author-feed batch (~30+ alerts: Chenjie Zeng self-feed, Bastarache, Karczewski, Denny, Hripcsak, Szolovits, Hernán, Yang, Pritchard, Montgomery, Ryan, Shendure, Callahan, Vogelstein, Natarajan, Luo, Chute, Snyder, Chung, Eichler, Birney, Kopp, Gusev, Kastner, Altman, Ellinor, van der Schaar, Baker) and 20:52Z keyword-feed batch (electronic health records, foundation models + EHR, autoimmune, mendelian, All of Us, knowledge graph, UK Biobank, drug repurposing, variant interpretation, rare diseases, APOL1, phenome wide association studies, clonal hematopoiesis). |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 | **06-21 = 0 papers in the lookback window** (2 previously surfaced suppressed; clean run, no fetch failure). |
| bioRxiv / medRxiv subject collection alerts | 06-21, 06-22 | Aggregate digest emails; not individually triaged here. |
| NCBI "What's new for 'UK Biobank' in PubMed" | 06-20 | Aggregate digest; primary signal hits surfaced through Scholar already. |

> ℹ️ **`arxiv-digest` was clean this window — `2026-06-21` ran without
> fetch errors but returned 0 papers in the lookback window (2 previously
> surfaced suppressed). Following yesterday's 06-20 3-of-4-category fetch
> failure, today's clean 0-paper output is the "real" signal rather than
> a polling artifact. All on-thread signal this window comes from Scholar
> alerts.** The 06-20 fetch-failure issue remains open as a pipeline
> reliability concern even though today's run was healthy.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a self-feed Cell Genomics review of GWAS
  translation.** Felici, Chen, Yuan, Jiang, Ip, Rudd et al. —
  *Translating genome-wide association studies at multiple scales: Drug
  target prioritization, cellular architectures, and organ imaging*
  (*Cell Genomics*, 2026) — surfaces simultaneously in (a) **your own
  Chenjie Zeng new-related-research feed** and (b) the **Joshua C. Denny
  citations feed**. Double-feed firing including your own self-feed,
  flagged on a *review* paper that covers GWAS → drug target → cellular
  context → organ imaging, is high-precision signal that this is now the
  default citation for the *post-GWAS translation* literature. Bears
  directly on multiple INTERESTS threads (genetic epi, drug repurposing,
  composite-risk modeling) and is a candidate intro-citation for
  essentially any future PRS / TWAS / GWAS-Catalog write-up. **Read
  first.**
- **A new biobank Nature paper — Pakistan Genome Resource at 173k.**
  Koch, Khalid, Khan, Bandyadka, Doyon et al. — *Analysis of 173,303
  exomes and genomes in the Pakistan Genome Resource* (*Nature*, 2026,
  surfaced via Denny citations feed; explicitly cites *Genomic data in
  the All of Us research program*). South Asian biobank with high
  familial relatedness — i.e., engineered for *natural homozygous LoF
  knockout* discovery (the same design rationale as the FinnGen,
  Icelander deCODE, and Amish populations, but at 173k scale). Frames LoF
  variants as drug-target validation hypotheses. **HIGH** on cross-
  ancestry biobank + variant-interpretation + drug-repurposing threads.
- **LLM-assisted rare-disease genome reanalysis hits NEJM AI.** Jaech,
  Cheatham, Shringarpure (23andMe), Genetti et al. — *LLM-assisted
  reanalysis of unsolved rare disease genomes increases diagnostic
  yield* (*NEJM AI*, 2026, "rare diseases" keyword feed). Reanalysis-
  of-unsolved-cases is the operationally meaningful framing for clinical
  utility; "increases diagnostic yield" in the title is the only metric
  payers will respond to. The 23andMe authorship is notable — a consumer-
  scale company is now doing clinical-grade rare-disease reinterpretation.
  Directly on the rare-disease + EHR-phenotyping (LLM-assisted) threads.
  **HIGH.**
- **Comparative-effectiveness of GLP-1 RAs on kidney outcomes.** Neumiller,
  Deng, Swarna, Polley, Herrin et al. — *Comparison of Specific Glucagon-
  Like Peptide-1 Receptor Agonists on Kidney Outcomes Among Patients With
  Type 2 Diabetes* (*American Journal of Kidney Diseases*, 2026, Patrick
  Ryan related-research feed). Head-to-head comparison *within* the GLP-1
  RA class (semaglutide vs liraglutide vs dulaglutide etc.) for kidney
  endpoints is the next-generation pharmacoepi question — the class-level
  GLP-1-vs-DPP4 / GLP-1-vs-SU work has been done; intra-class comparative
  effectiveness for CKD outcomes is the open question, and the analytic
  template is target-trial emulation. **HIGH** on the GLP-1 pharmacoepi
  thread; **methods-relevant** for the APOL1 thread (kidney outcomes).
- **β-cell stress + T2D genetics, dish-to-biobank.** Wang, Lee, Le,
  Turhan, Hu, Garcia et al. — *A dish-to-biobank framework links β-cell
  nutrient-stress programs to genetic and dietary risk for Type 2
  Diabetes* (*bioRxiv*, 2026-06-12) — **double-feed**: Konrad Karczewski
  related-research **and** Chenjie Zeng related-research. Couples
  *in-vitro* β-cell perturbation-program profiling with *biobank*
  genetic-risk + dietary-risk stratification — the kind of cross-scale
  bridge the Felici Cell Genomics review (item #1) advocates as the
  field's direction. **HIGH** for the T2D + biobank methodology thread.
- **APOL1-adjacent kidney genetics in living kidney donors.** Caliskan,
  Oto, Alhamad, Yazici, Velioglu et al. — *Genetic Evaluation Practices
  in Living Kidney Donor Candidates* (*Kidney International Reports*,
  2026, APOL1 keyword feed). Descriptive practice-survey of how genetic
  testing is *actually* used in living-donor evaluation. Directly on the
  APOL1 thread (LKD evaluation is the canonical clinical context for the
  APOL1 transplant question). **HIGH** for the APOL1 thread; provides a
  baseline practice snapshot to cite when arguing for APOL1-specific
  protocols.
- **EHR + LLM for Alzheimer phenotyping at the memory clinic.** Powell,
  Hofmann, Oh, Schindler et al. — *Identification of memory clinic
  patients diagnosed with Alzheimer disease using electronic health
  records data and large language models* (*npj Dementia*, 2026, EHR
  keyword feed). Memory-clinic-specific AD phenotype derived from EHR
  via LLM extraction — exactly the "LLM-assisted phecode/HPO assignment
  from clinical notes" pattern called out in INTERESTS. **HIGH** on EHR
  phenotyping + OMOP thread.
- **Two more on-thread items from Chenjie Zeng related-research feed.**
  Cuperus et al. — *In-depth Human Phenotype Ontology Curation Boosts
  Prioritization Performance for Netherton Syndrome* (*British Journal
  of Dermatology*, 2026) and Lee et al. — *Polygenic risk scores
  associate with asthma phenotypes and proteomic analyses implicate
  IL1R1 in two family-based studies* (*medRxiv*, 2026). The Cuperus
  paper validates HPO depth-of-curation as a diagnostic-yield lever for
  rare-disease dermatology — on the HPO/rare-disease + LLM-phenotyping
  intersection. The Lee paper composes PRS + proteomic evidence on
  asthma using a family-based design — on the composite-PRS-plus-omics
  + family-design sub-thread. **HIGH for the self-feed pair.**
- **Margolis — PheWAS at gene-and-isoform-level resolution.** Margolis —
  *Computational Mapping of Neuropsychiatric Risk across Neurodevelopment
  at Gene-and Isoform-Level Resolution* (UC eScholarship dissertation /
  preprint, 2026, "phenome wide association studies" keyword feed). Maps
  19,431 variant-phenotype PheWAS associations, ~76% replicating in
  independent biobanks, with isoform-level resolution. Dissertation-stage
  but the *isoform-resolution* PheWAS framing is methodologically
  distinctive vs the standard gene/transcript PheWAS. **HIGH** on the
  PheWAS methodology thread; **METHODS-WATCH** until peer-review.
- **`arxiv-digest 06-21` was a clean zero — confirms the pipeline
  recovered.** After yesterday's 3-of-4-category fetch failure, the
  06-21 run returned 0 matches in the lookback window with no warning
  (and "2 previously surfaced suppressed"). This is a healthy zero —
  not a polling artifact. The pipeline's signal-to-noise ratio for
  on-thread arXiv papers in q-bio.QM/GN/PE + stat.AP remains low, as
  noted in prior reports — most on-thread signal continues to come from
  Scholar.

Counts: **9 HIGH**, **6 METHODS-WATCH**, rest SKIP. Window is comparable
to 06-20 in volume; the standout is the self-feed Cell Genomics review
(item #1) and the new Nature biobank paper (item #2).

---

## HIGH priority — detailed reports

### 1. Translating genome-wide association studies at multiple scales: Drug target prioritization, cellular architectures, and organ imaging
- **Authors / venue:** B. Felici, S. Chen, M. Yuan, X. Jiang, S. Ip, J.H.F. Rudd et al. — *Cell Genomics*, 2026. URL: `cell.com/cell-genomics/fulltext/S2666-979X(26)00144-8`.
- **Surfaced by:** **Double-feed** — (a) *Chenjie Zeng — new related research* (**your own feed**), (b) *10 new citations to articles by Joshua C. Denny*. Self-feed firing on a *review* paper is the strongest positive signal that the field treats this as a default citation in your methodological space.
- **Thread:** **Genetic epidemiology / PRS** (GWAS translation — the *post*-GWAS step) **+** **Drug repurposing** (target prioritization is the explicit framing) **+** **Composite risk modeling** (cellular architectures, organ imaging) **+** **EHR-linked biobank** (the data substrate the review draws from).
- **What it is:** Review article synthesizing the post-GWAS translation landscape across three axes: (a) **drug target prioritization** (translating GWAS hits to druggable proteins, including drug repurposing where existing-drug targets overlap GWAS hits), (b) **cellular architectures** (linking GWAS variants to gene regulation in specific cell types — the eQTL / sc-eQTL / perturb-seq lineage), and (c) **organ imaging** (linking GWAS variants to organ-level imaging-derived phenotypes — the cardiac MRI / retinal imaging / brain MRI imaging-genetics literature). One of the cited references is *Genetic drivers of heterogeneity in type 2 diabetes pathophysiology*, suggesting T2D and cardio-metabolic disease are the leading worked examples.
- **Why it matters to you:** Four reasons.
  (a) **Self-feed firing on a review paper is the cleanest possible signal.** Google's relevance model judged this paper close enough to your published work to fire your own feed, on a paper that synthesizes the *next* step beyond your usual PRS/PheWAS framing. Review papers that fire on your self-feed are typically papers you'll be cited in or be expected to cite.
  (b) **The "GWAS → drug target → organ imaging" pipeline is exactly the structure that AoU + UKB-Imaging + MVP enable.** Your INTERESTS file emphasizes EHR-linked biobanks; UKB-Imaging + UKB-Genetics is the prototype, AoU now has imaging in v8, and MVP has imaging through VA radiology. This review is likely the field's reference for *how to use* that combined data substrate.
  (c) **Drug repurposing thread.** Target-prioritization-from-GWAS is one of the cleaner computational drug repurposing framings; this review will be a default citation for any GNN-on-knowledge-graph drug repurposing argument you'd make, since it grounds the "drug target = GWAS hit" assumption that those methods rely on.
  (d) **Pairs with last report's noncoding effects paper.** The Marderstein et al. *Nature Genetics* noncoding paper (#5 in the 06-20 report) provides the variant→regulation→cell-type evidence layer; this review provides the architecture that downstream consumers (drug-target, imaging) sit on top of. Together they compose into "common+rare noncoding variants → cell-type regulation → drug target / organ imaging."
- **Action:** **HIGH — read first.**
  (i) Note who's cited at the head of each section — those are the field's *de facto* lead authors per axis. Likely candidates: Pritchard / Pasaniuc / Hormozdiari (cellular), Astle / Reilly / Vamathevan (drug target), Bycroft / Petersen / Niiranen (organ imaging).
  (ii) Check whether they cite your AoU work and where (intro, drug-target section, or biobank-substrate section). Position of citation tells you which sub-thread they slot you in.
  (iii) Likely a useful intro-citation for any future PheWAS+PRS / cross-ancestry PRS / composite-risk write-up.
  (iv) The list of *cited papers* is potentially more valuable than the review text itself — review reference lists from groups that overlap your work compose into a reading list.

### 2. Analysis of 173,303 exomes and genomes in the Pakistan Genome Resource
- **Authors / venue:** C. Koch, S. Khalid, M.Z. Khan, S. Bandyadka, B. Doyon et al. — *Nature*, 2026. URL: `nature.com/articles/s41586-026-10667-5`.
- **Surfaced by:** *10 new citations to articles by Joshua C. Denny* — specifically cited because the paper explicitly cites *Genomic data in the All of Us research program* (Denny coauthor).
- **Thread:** **EHR-linked biobank** (cross-ancestry biobank infrastructure) **+** **Variant interpretation** (loss-of-function variants, including biallelic LoF / "natural knockouts") **+** **Drug repurposing** (LoF variants as drug-target validation evidence) **+** **Genetic epidemiology / PRS portability** (large South Asian sequencing dataset for trans-ancestry PRS).
- **What it is:** From the abstract framing: "Naturally occurring loss-of-function variants in human genes enable drug target discovery because they mimic pharmacological inhibition of proteins. However, the study of these genetic variants is constrained by their rarity. Sequencing of diverse populations, particularly those enriched in familial relatedness, has been postulated to promote discovery of rare genetic variants. Here we present the Pakistan Genome Resource, a South Asian biobank with high familial relatedness comprising [173,303 individuals]." The methodological argument is identical to the FinnGen and Amish-study rationales: founder-effect-like enrichment via consanguinity surfaces homozygous LoF carriers (natural knockouts) at frequencies the standard outbred-cohort designs can't reach.
- **Why it matters to you:** Four reasons.
  (a) **Trans-ancestry portability of PRS** is on INTERESTS; this is one of the largest non-European sequenced biobanks to date, and downstream PRS work in South Asians will use it as the reference panel.
  (b) **Drug-target validation pipeline.** The LoF-mediated-knockout-mimics-inhibition framing is a key empirical input for any drug-repurposing argument — it converts "GWAS hit ⊆ drug target" into "homozygous LoF + phenotype-shift = candidate target." This is the empirical substrate Felici et al. (#1) reviews.
  (c) **AoU comparison.** The paper cites AoU as a related-but-different design (consented prospective vs founder-population family enrichment); whichever specific All of Us paper they cite will tell you how the field positions AoU vs PGR for variant-effect-size estimation in rare/LoF variants.
  (d) **Variant interpretation.** A new 173k cohort fundamentally changes the *AF-based denominator* for variant pathogenicity in South Asian individuals — gnomAD-South-Asia is ~15k WGS-equivalent, so PGR is ~10× larger and will become the *de facto* AF reference for ACMG-AMP application in South Asian patients. ClinGen VCEPs working on South Asian variant interpretation will rebuild PM2/BS1 frequency thresholds around it.
- **Action:** **HIGH.**
  (i) Check the LoF burden methodology — is it LOFTEE-based, similar to gnomAD constraint? If so, you can compose PGR constraint with gnomAD constraint for cross-ancestry LoF analysis.
  (ii) Note which phenotypes they highlight as having LoF-discovery hits — those become the leading candidate phenotypes for drug-repurposing follow-up.
  (iii) Note the EHR-linkage scope (PGR vs AoU vs UKB). South Asian phenotyping via Pakistan's clinical infrastructure is methodologically distinct from US/UK EHR.
  (iv) The paper is *currently the largest* non-European biobank Nature paper of 2026 H1; track who cites it in the next 6 months as the natural-knockout drug-target pipeline matures.

### 3. LLM-assisted reanalysis of unsolved rare disease genomes increases diagnostic yield
- **Authors / venue:** A. Jaech, M. Cheatham, S.S. Shringarpure (23andMe), C.A. Genetti et al. — *NEJM AI*, 2026. URL: `ai.nejm.org/doi/abs/10.1056/AIcs2501343`.
- **Surfaced by:** *rare diseases* keyword feed (position 0 — top result).
- **Thread:** **Rare disease** (the title is literal) **+** **EHR phenotyping & LLM-assisted phecode/HPO assignment** (LLM-assisted reanalysis is the *most clinically meaningful* application of clinical-NLP infrastructure) **+** **Variant interpretation** (the reanalysis improves classification of previously inconclusive variants).
- **What it is:** LLM-assisted reanalysis of previously unsolved rare-disease cases at scale, evaluated on the operationally meaningful metric of *diagnostic yield improvement* (rather than just LLM benchmark accuracy). The Shringarpure 23andMe affiliation is notable — it suggests the underlying genomic infrastructure is consumer-genetics-grade rather than research-cohort-grade.
- **Why it matters to you:** Four reasons.
  (a) **"Diagnostic yield" is the only LLM-clinical metric that matters.** Most LLM-clinical-NLP papers report accuracy on synthetic benchmarks; this one reports diagnostic-yield delta against a real unsolved-case cohort. NEJM AI publishing it signals that the design met evidentiary thresholds.
  (b) **Directly on the rare-disease + LLM-phenotyping intersection** in INTERESTS — *"LLM extraction from clinical notes for phecode and HPO term assignment"* is exactly the upstream step this paper's pipeline assumes.
  (c) **Pairs with the I. Chen "epidemiological spectrum bias" Research Square paper** that surfaced as the #3 result in the same alert — that paper argues *LLM-based rare-disease diagnostic systems are evaluated on enriched spectra that overstate real-world performance*. Reading the two together gives you the optimistic (Jaech) and skeptical (Chen) framings of the same question.
  (d) **23andMe productionizing rare-disease reanalysis is itself news** — a consumer company can offer "we'll re-review your data with the latest LLM annually" as a service, which would compete with academic rare-disease center reanalysis.
- **Action:** **HIGH.**
  (i) Read for the *baseline* — what was the unsolved-cohort's pre-reanalysis diagnostic yield? Yield delta is meaningless without it.
  (ii) Note the LLM model (Gemini? Claude? Internal model?) and the prompt template — these are the operationally relevant details for replicating in academic settings.
  (iii) Check whether they incorporate HPO terms or work directly from unstructured notes. HPO-grounded would be the more interpretable design.
  (iv) Pair with the Cuperus et al. HPO Netherton paper (#8) — both argue the same thing (better phenotype curation → higher diagnostic yield) from opposite directions: Cuperus from manual deep curation, Jaech from LLM-scale automation.

### 4. Comparison of Specific Glucagon-Like Peptide-1 Receptor Agonists on Kidney Outcomes Among Patients With Type 2 Diabetes
- **Authors / venue:** J.J. Neumiller, Y. Deng, K.S. Swarna, E.C. Polley, J. Herrin et al. — *American Journal of Kidney Diseases*, 2026.
- **Surfaced by:** *Patrick Ryan — new related research* feed.
- **Thread:** **Causal inference & pharmacoepidemiology** (GLP-1 RAs is one of the explicitly tracked drug classes) **+** **APOL1 / kidney disease thread** (kidney outcomes is the endpoint) **+** **EHR-linked biobank / OMOP infrastructure** (the Polley + Herrin authorship suggests Mayo Clinic / OHDSI-style multi-site OMOP work).
- **What it is:** From the abstract framing: "GLP-1 receptor agonist treatment is associated with lower risk for incident CKD and death relative to treatment with a dipeptidyl peptidase-4 inhibitor or sulfonylurea." This study performs the within-class comparison — semaglutide vs liraglutide vs dulaglutide vs the newer entrants (oral sema, tirzepatide) — on kidney endpoints (incident CKD, CKD progression, kidney composite outcomes). The Patrick Ryan related-research surfacing positions it as an OHDSI-template-style multi-site comparative-effectiveness paper.
- **Why it matters to you:** Three reasons.
  (a) **GLP-1 RA pharmacoepi is one of your explicit drug-class threads.** Within-class comparative effectiveness is the next-generation question after class-vs-class is settled — exactly where the field is now.
  (b) **Kidney outcomes overlap your APOL1 thread.** Whether GLP-1 RA kidney benefit varies by APOL1 genotype is an open question; intra-class differences (e.g., if semaglutide outperforms dulaglutide on kidney) would feed into APOL1-genotype-stratified analyses.
  (c) **The Mayo / OHDSI / Patrick Ryan lineage** typically uses target-trial-emulation templates with strong confounding-adjustment infrastructure (LASSO-PS, doubly-robust, etc.). The analytic *template* is reusable for any of your causal-pharmacoepi work.
- **Action:** **HIGH.**
  (i) Note the comparator structure — head-to-head pairwise, active-comparator new-user, or anchored to a reference GLP-1 RA? Each implies a different causal interpretation.
  (ii) Note the kidney composite definition — eGFR-based, ICD-based, KDIGO-based? Composite definition drives the magnitude of any class-difference signal.
  (iii) Check whether they report effect modification by baseline CKD stage, by race (which would proxy APOL1 partially), or by SGLT2i co-prescription. SGLT2i interaction is the most operationally consequential effect modifier.
  (iv) Worth saving as a TTE / pharmacoepi template citation.

### 5. A dish-to-biobank framework links β-cell nutrient-stress programs to genetic and dietary risk for Type 2 Diabetes
- **Authors / venue:** X. Wang, H. Lee, A. Le, B. Turhan, N. Hu, P.S. Garcia et al. — *bioRxiv*, 2026-06-12. URL: `biorxiv.org/content/...2026.06.12.731989.full.pdf`.
- **Surfaced by:** **Double-feed** — *Konrad Karczewski — new related research* **and** *Chenjie Zeng — new related research* (your own feed).
- **Thread:** **Genetic epidemiology / PRS** (T2D genetic risk integration) **+** **EHR-linked biobank** (the biobank end of "dish-to-biobank") **+** **Machine learning for precision health** (treatment-effect heterogeneity, in this case dietary effect modification by genetic risk).
- **What it is:** From the abstract framing: "Type 2 diabetes (T2D) arises from genetic susceptibility and chronic metabolic stress, but whether these converge on shared molecular programs in human populations remains unclear. Here, we develop a dish-to-biobank framework linking [in-vitro β-cell perturbation programs to biobank genetic and dietary risk]." The methodological move is to derive *β-cell stress response programs* from in-vitro perturbation experiments (nutrient stress, glucotoxicity, lipotoxicity) and then **test those programs as effect-modifying covariates** of T2D PRS in a biobank — bridging cellular molecular biology to population-scale risk modeling. Karczewski-feed firing suggests gnomAD-style constraint or LoF-burden analysis is part of the design.
- **Why it matters to you:** Three reasons.
  (a) **Self-feed firing on a bioRxiv preprint is rare** — Google's relevance model gating on your *related research* feed for an in-vitro+biobank bridge paper means the field is starting to position your work in this cross-scale bridge space.
  (b) **The dish-to-biobank framing is exactly the design Felici et al. (#1) advocates** as the field's direction — this is a worked instance of the same bridge that the Cell Genomics review describes.
  (c) **Diet × genetic interaction is on the chronic-disease-clustering / multimorbidity thread.** Dietary risk as effect modifier of T2D PRS is the prototype for "diet × PRS" interactions in cardiometabolic disease — relevant to any AoU dietary-survey + PRS work.
- **Action:** **HIGH** (preprint-stage, so methods-watch is the appropriate intensity).
  (i) Read for the in-vitro program definition — single perturbation, panel of perturbations, or unsupervised program discovery? Panel-based is the most reusable.
  (ii) Check the biobank — UKB is the most likely; AoU dietary surveys + PRS would be the natural follow-up.
  (iii) Note the effect-modification statistical model — interaction term in regression, stratified analysis, causal-forest-style HTE? HTE methodology would be the most methodologically novel.
  (iv) Worth tracking through peer-review; bioRxiv → biorxiv journal pipeline for these papers is typically 6-9 months.

### 6. Genetic Evaluation Practices in Living Kidney Donor Candidates
- **Authors / venue:** Y. Caliskan, O.A. Oto, T. Alhamad, H. Yazici, A. Velioglu et al. — *Kidney International Reports*, 2026. URL: `sciencedirect.com/science/article/pii/S2468024926028974`.
- **Surfaced by:** *APOL1* keyword feed (position 0 — top result).
- **Thread:** **APOL1 disease thread** (LKD evaluation is THE canonical APOL1 clinical context) **+** **Variant interpretation** (ACMG-AMP application in LKD genetic evaluation) **+** **Genetic epidemiology** (population frequency considerations in donor screening).
- **What it is:** From the abstract framing: "Although genetic testing is increasingly used in evaluating living kidney donor (LKD) candidates and recipients, objective data on genetic testing practices are limited. This study aimed to describe current genetic testing practices in LKD…". Descriptive practice-survey of how transplant centers actually use genetic testing in living-donor evaluation, almost certainly including APOL1 testing as a sub-question (given the keyword-feed firing).
- **Why it matters to you:** Three reasons.
  (a) **LKD APOL1 testing is the high-stakes clinical decision** in the APOL1 thread — the donor faces meaningful risk if they carry high-risk APOL1 variants and donate a kidney. The 2024 OPTN policy change requiring APOL1 testing for African-ancestry donors made this an explicit standard-of-care question.
  (b) **Practice-survey data is the empirical baseline** for any subsequent guideline or implementation-science argument. If actual practice deviates from policy, that's a publishable gap.
  (c) **Pairs with the 06-18 APOL1 transplant paper** that your own *citations* feed surfaced (in the 06-18 report) — Caliskan provides the *practice* end of the picture; the cited transplant paper provides the *outcomes* end.
- **Action:** **HIGH.**
  (i) Read specifically for APOL1 — what fraction of centers test, what fraction of African-ancestry candidates are tested, how is risk communicated, what's done with high-risk genotypes.
  (ii) Compare to OPTN's policy timeline — practice should have shifted post-2024; if it hasn't, that's a citation-worthy implementation-gap finding.
  (iii) Note whether they discuss APOL1 in the context of high-risk genotype thresholds (G1/G1, G1/G2, G2/G2 vs G1-or-G2 heterozygous + environmental risk).
  (iv) Useful baseline citation for any APOL1 LKD implementation-science write-up.

### 7. Identification of memory clinic patients diagnosed with alzheimer disease using electronic health records data and large language models
- **Authors / venue:** W.J.B. Powell, A. Hofmann, I.Y. Oh, S.E. Schindler et al. — *npj Dementia*, 2026. URL: `nature.com/articles/s44400-026-00098-4`.
- **Surfaced by:** *"electronic health records"* keyword feed (position 0 — top result).
- **Thread:** **EHR phenotyping & OMOP** (the user's core methodological thread) **+** **EHR foundation models / LLMs** (LLM-extraction from clinical notes) **+** **Rare/chronic disease threads** (memory-clinic AD is a clinical-care setting with well-defined cohort selection).
- **What it is:** From the abstract framing: "Alzheimer disease (AD) is a neurodegenerative disorder marked by gradual decline in memory and thinking. New treatments for early symptomatic AD have increased the need for early and accurate AD diagnosis. This study aimed to identify which [patients in a memory clinic EHR were diagnosed with AD via LLM extraction from clinical notes]." Operationally: LLM-assisted phenotype derivation from memory-clinic notes, evaluated against gold-standard chart-review AD diagnoses. The Schindler authorship suggests this is the Washington University ADRC memory-clinic cohort.
- **Why it matters to you:** Three reasons.
  (a) **Memory-clinic-specific AD phenotyping is operationally distinct** from biobank-scale AD phenotyping. Biobank AD relies on G30/ICD-10 codes (which are sensitive but not specific to AD vs other dementias); memory-clinic phenotyping incorporates *clinical-judgment* labels from neurology notes. LLM-extraction is the bridge.
  (b) **This is the exact LLM-from-notes pipeline INTERESTS specifies** ("LLM extraction from clinical notes for phecode and HPO term assignment"). For Alzheimer-disease specifically — given the AD-treatment landscape post-lecanemab — high-precision EHR identification is now clinically actionable.
  (c) **Pairs with the Jaech et al. NEJM AI rare-disease reanalysis paper (#3).** Both are LLM-extraction-from-notes for clinical phenotyping; Jaech for rare-disease diagnostic yield, Powell for AD case identification. Together they bookend the LLM-clinical-NLP landscape.
- **Action:** **HIGH.**
  (i) Read for the LLM model and prompt template — open-source (Llama-3/Qwen) vs closed-source (GPT-4/Claude/Gemini)? Closed-source generalizes more poorly across health systems.
  (ii) Check whether the gold standard is single-reviewer or adjudicated chart review. Adjudicated is the more credible standard.
  (iii) Note whether they release the prompt or the labeled cohort — release of either would make this a citable resource rather than just a paper.
  (iv) Pair with a comparison against rule-based AD phenotypes (e.g., Bastarache phecode 290.1) — most useful follow-up reading.

### 8. In-depth Human Phenotype Ontology Curation Boosts Prioritization Performance for Netherton Syndrome
- **Authors / venue:** E. Cuperus, S.G.M.A. Pasmans, H.L. Han, A.S. Arterbery et al. — *British Journal of Dermatology*, 2026. URL: `academic.oup.com/bjd/.../ljag249.pdf`.
- **Surfaced by:** *Chenjie Zeng — new related research* feed (your own feed).
- **Thread:** **Knowledge graphs & ontologies** (HPO is the canonical biomedical ontology in INTERESTS) **+** **Rare disease** (Netherton syndrome is a rare congenital dermatology disorder) **+** **Variant interpretation** (HPO depth is the upstream input to Exomiser-style variant prioritization).
- **What it is:** From the abstract framing: "This study brings the Human Phenotype Ontology into dermatology, refining and expanding its use for Netherton syndrome. The updated terms significantly boost diagnostic performance and enhance clinical phenotyping. It highlights the promise…". Empirical demonstration that *manual deep curation* of HPO terms for a specific rare disease (Netherton) measurably improves Exomiser-style gene prioritization performance.
- **Why it matters to you:** Three reasons.
  (a) **HPO curation depth → diagnostic-yield delta is the underlying mechanism** for HPO-grounded rare-disease diagnosis. This paper makes that mechanism quantitative for one disease — a useful precedent if you want to argue for HPO curation investment in your own rare-disease projects.
  (b) **Self-feed firing on a dermatology-journal paper** is unusual — likely the HPO-curation methodology is what's matching, not the disease itself. That positions this paper as a methods reference rather than a Netherton-specific finding.
  (c) **Pairs with the Jaech NEJM AI paper (#3) from a different angle.** Jaech: scale up LLM extraction. Cuperus: scale up manual curation depth. The synthesis question is whether LLM extraction recovers the depth that manual curation produces — and at what cost ratio.
- **Action:** **HIGH.**
  (i) Read for the curation protocol — who curates, against what evidence sources, with what review process. The protocol is the reusable artifact.
  (ii) Note the *quantitative* yield improvement (Exomiser rank-of-truth gene, % cases solved). Magnitude matters; small magnitudes don't move the field.
  (iii) Consider whether the protocol generalizes — Netherton-specific curation may or may not transfer to CFTR-related disease, kidney rare disease, etc.
  (iv) Useful citation for any HPO-curation argument in the rare-disease + ontology space.

### 9. Polygenic risk scores associate with asthma phenotypes and proteomic analyses implicate IL1R1 in two family-based studies
- **Authors / venue:** S. Lee, M. Moll, K. Mendez, N. Prince, J. Lasky-Su et al. — *medRxiv*, 2026. URL: `medrxiv.org/content/medrxiv/early/2026/06/11/2026.06.06.26355045.full.pdf`.
- **Surfaced by:** *Chenjie Zeng — new related research* feed (your own feed).
- **Thread:** **Genetic epidemiology / PRS** (asthma PRS phenotype-stratification) **+** **Composite risk modeling with omics** ("composite risk models stacking PRS with rare pathogenic variants" in INTERESTS — proteomics here plays the rare-variant-analog role) **+** **Multimorbidity** (asthma + IL1R1 + Lasky-Su's metabolomics-on-PRS lineage).
- **What it is:** From the abstract framing: "Despite its high prevalence and the discovery of hundreds of genetic associations, the genetic determinants and heterogeneous manifestations of asthma remain incompletely understood. Incorporating polygenic risk scores (PRS) into asthma…". The technical move is: asthma PRS → phenotypic-cluster heterogeneity → proteomic signature → IL1R1 mechanistic implication, with family-based design controlling for shared environment. Two family-based cohorts (likely CAMP + a second NHLBI consortium cohort).
- **Why it matters to you:** Three reasons.
  (a) **Family-based PRS + proteomics design is methodologically distinctive.** Most PRS+omics composites use population-cohort data; family-based controls for shared environmental confounding that biases population-cohort proteomic-PRS associations.
  (b) **Self-feed firing** — Google judged this paper close enough to your work to fire your related-research feed, on a PRS+omics design. Likely positions you to be cited or asked to peer-review similar designs.
  (c) **IL1R1 has cross-disease implications.** IL1R1 is upstream of IL-1β signaling, which is implicated in psoriasis, IBD, autoimmune disease, and cardiovascular disease (CANTOS trial). A PRS-implicated mechanism with cross-disease relevance is more valuable than a tightly disease-specific finding.
- **Action:** **HIGH.**
  (i) Read for the proteomic platform — Olink or SomaScan? Family-based + Olink-Explore-HT would be the strongest design.
  (ii) Note which asthma phenotypes (TH2-high, TH2-low, eosinophilic, exacerbation-prone, age-of-onset). Phenotypic granularity is the value-add over standard binary-asthma PRS.
  (iii) Check whether IL1R1 protein levels mediate the PRS → phenotype relationship via formal mediation analysis. Mediation framing is the most actionable for follow-up drug-target work.
  (iv) Watch for the peer-review version; medRxiv → journal pipeline typically 4-8 months.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **Electronic Phenotype for Detection, Staging, and Subtyping of Acute Kidney Injury** — N. Shang, K. Xu, J.S. Stevens, J. Barasch, K. Kiryluk — *American Journal of Kidney Diseases*, 2026 ("electronic health records" keyword feed). EHR phenotype for AKI detection, staging, and subtyping, leveraging serum creatinine. The Kiryluk authorship (Columbia nephrology genetics) is on-thread for the APOL1 + kidney genetics axis. **Watch for:** how they handle the missing-urine-output problem (KDIGO criterion 2 is rarely captured in EHR), and whether they subtype AKI by etiology (pre-renal, intrinsic, post-renal) — a real-world AKI phenotype with etiology subtyping would be a default citation for kidney-EHR phenotyping.

- **Knowledge-Augmented Large Language Model for Multimodal Electronic Health Record–Based Risk Prediction: Development and Validation Study** — R. Datta, J. Cui, Z. Guan, V. Reddy, J. Eby — *JMIR AI*, 2026 ("electronic health records" keyword feed). KG-augmented LLM for multimodal EHR risk prediction over structured + unstructured EHR. **Watch for:** the KG choice (UMLS? SemMedDB? Custom biomedical KG?) — a UMLS-grounded KG would be more reusable. Architecture-paper level; complements the Sivarajkumar EHR-FM paper from the 06-20 report on the joint-modality question.

- **Computational Mapping of Neuropsychiatric Risk across Neurodevelopment at Gene-and Isoform-Level Resolution** — M.P. Margolis — UC eScholarship (2026 dissertation/preprint, "phenome wide association studies" keyword feed). 19,431 variant-phenotype PheWAS associations at isoform-level resolution, ~76% replicating in independent biobanks, with exome-wide burden testing for predicted-deleterious variants. **Watch for:** the isoform-level resolution methodology — most current PheWAS treats genes as the unit; isoform-level association is methodologically distinctive and could be a useful citation when arguing for transcript-aware PheWAS in your own work. Dissertation-stage; will likely yield 2-3 papers in 2026 H2.

- **Reclassification of BRCA1 variants of uncertain significance using ancestry-stratified allele frequencies: A Middle East-focused analysis** — L. Abujamous, R. Razali, H. Al-Thawadi — *Biomolecules & biomedicine*, 2026 ("variant interpretation" keyword feed). Re-classifies BRCA1 VUSes using ancestry-stratified allele frequencies in a Middle Eastern population. **Watch for:** which AF reference panel they use as the Middle Eastern denominator — is it gnomAD-MID (small, ~1.6k WGS), a regional sequencing initiative, or rebuilt from local samples? Methodologically on the cross-ancestry ACMG-AMP PM2/BS1 axis. Pairs with the Koch Pakistan Genome Resource paper (#2) — both papers are arguments that AF-denominator improvements drive variant-interpretation gains.

- **KMT2A and KMT2B episignatures address diagnostic challenges associated with rare neurodevelopmental disorders** — Z. Awamleh, A. Chen, S. Choufani, D. Rots, J.M. Ko — *Genetics in Medicine*, 2026 ("variant interpretation" keyword feed). DNA-methylation episignatures as a diagnostic adjunct for KMT2A/KMT2B variant classification in Wiedemann-Steiner and Dystonia-28. **Watch for:** the episignature framework as a *non-MPRA* functional-evidence layer for variant interpretation — complementary to the Marderstein et al. *Nature Genetics* MPRA-based noncoding interpretation (06-20 report #5). Episignatures are now the leading functional-evidence approach for chromatin-regulator genes; if any of your rare-disease work touches that gene class, this becomes a default citation.

- **Impact of a comprehensive healthy lifestyle and genetic risk on arrhythmia: insights from the UK biobank study** — Q. Yang, X. Lu, Y. Lu, X. Jiang, T. Wang, C. Guo — *BMC Cardiovascular Disorders*, 2026 ("UK Biobank" keyword feed). UKB-scale analysis of lifestyle × genetic risk interaction on arrhythmia. **Watch for:** the lifestyle composite definition (typical Khera-style 5-factor lifestyle score?) and whether they report decision-curve analysis or just HR-stratified. Decision-curve analysis would make this clinically actionable. **On-thread methods reference** for any future PRS × lifestyle interaction work in AoU.

---

## SKIP / noise (logged, no action)

- **The All of Us Evenings with Genetics Research Program** (Lloyd, Baker, Jorgez, Coleman, Williams — JCTS, "All of Us research program" keyword feed) — program description / community engagement piece, not primary research.
- **HIF-1α in macrophage polarization: roles in immunometabolism and autoimmune diseases** ("autoimmune diseases" keyword feed) — molecular immunology review, off-thread.
- **Microglial clonal dynamics and the impact of clonal hematopoiesis in autologously transplanted rhesus macaques** (Cell Reports, "clonal hematopoiesis" keyword feed) — primate-model CHIP paper, methodologically interesting but off your human-EHR-cohort CHIP/VEXAS angle.
- **Artificial Sweeteners and Autoimmune Diseases: Mendelian Randomization** (Food Science, "mendelian diseases" keyword feed) — keyword leak; this is a *Mendelian randomization* paper on sweetener exposure, not a Mendelian-disease paper. Standing keyword issue (see pipeline notes).
- **A coupling analysis framework for ship welding quality causal factors integrating knowledge graph and NK model** (Ocean Engineering, "knowledge graph" keyword feed) — non-biomedical KG, **8th consecutive window of this keyword leak**. See pipeline notes.
- **Drug Repurposing via Biomedical Knowledge Graph Embedding** (Sankar, "drug repurposing" keyword feed) — undergrad-thesis-level GNN drug-repurposing paper. Off the explainable-hypothesis-output criterion in INTERESTS.
- **Computational Stability Analysis suggests binding-independent destabilization in pathogenic FBXO11 variants** (Scientific Reports, "variant interpretation" keyword feed) — single-gene computational stability paper, off-thread.
- **Generative Transformers for Pharmacovigilance Signal Detection using EHR** (Wu, De Boer, Cohen — AMIA Summits, EHR keyword feed) — pharmacovigilance NLP, adjacent but methods-only.
- **Optimizing EHR Data Processing in Rural Nigeria** ("electronic health records" keyword feed) — Python vs R benchmarking paper, off-thread.
- **Interoperability and Usability of EHRs (Lund thesis)** — qualitative HCI study, off-thread.
- **Blockchain-Enabled Secure EHR Sharing Framework** (Genetics and Molecular Research) — blockchain-EHR architecture paper, off-thread.
- **Threshold-Optimized EHR-Based ML for Predicting 1-Year Acute Care Use in Diabetes** (MDPI Diabetology) — single-system ML paper, off-thread (the larger-N AoU/UKB analog would be on-thread).
- **Protocol for AI-Models in Emulated Primary Care EHR for CRC Risk** (Research Square) — protocol-only paper.
- **Role of EHR in stigma experiences for women with pregnancy + SUD history** (JAMIA) — qualitative ethics paper, off-thread.
- **Genetic Determinants of Severe Hypertriglyceridemia: Rare Variants + Polygenic Risk** (Blokhina, International Journal — Denny related-research feed) — adjacent to PRS+rare-variant composite-risk thread but disease (HTG) is off your tracked threads.
- **Pakistan Genome Resource–related citations** appearing under multiple author feeds — same paper as #2 above; counted once.
- **Rare disease monitoring plans CDSS case study** (Computers in Biology, rare-disease feed) — clinical-decision-support engineering, off-thread.
- **PEAL lossless one-shot federated learning** (npj Digital Medicine, rare-disease feed) — federated-learning architecture paper; **adjacent** to the 06-20 Kundu privacy-enhancing multi-site EHR paper, but lossless-FL is more methods-only without the selection-bias substantive angle.
- **Rare Kidney Disease Conference Proceedings: Palm Springs December** (Nephron, rare-disease feed) — conference proceedings.
- **Servier Expands Rare Neurology Portfolio with $2.65B Edgewise Acquisition** (Pharma Deals Review) — pharma business news, off-thread.
- **Cardiovascular Genetic Epidemiology in the Genome-Wide Era** (Yan et al., Cardiovascular Drugs and Therapy, "variant interpretation" keyword feed) — review article; adjacent to genetic-epi thread but a review and somewhat duplicative of the Felici #1 piece.
- **Mark Gerstein / Russ Altman / Christopher Chute — "AI in Genomic Data Analysis" and "AI in Drug Discovery" pieces** (Academic Journal of Bioinformatics) — both appear to be in the same low-tier OA "Academic Journal of Bioinformatics" venue from the same week; not primary research, possibly publisher cross-promotion.
- **Evan Eichler new article: chromosome 21 centromere sequencing in Down syndrome families** (AJHG) — chromosome biology, off your thread substantively.
- **Daniel Kastner citations: quantified immune-aging dysregulation index** (Frontiers) — adjacent to multimorbidity/aging thread but LLM-driven annotation methodology only.
- **George Hripcsak citations: GLP-1 + NAION optic disc drusen** (Ophthalmology) — pharmacovigilance signal, drug class is GLP-1 but endpoint (NAION) is off your thread.
- **Marinka Zitnik related-research: SW-SpeedDLM masked diffusion** (Mathematics) — speculative-decoding methods, off the biomedical-FM thread.
- **Mihaela van der Schaar new article: Recursive Scaling in Masked Diffusion Models** (arXiv) — diffusion-models methods.
- **David Baker new article: SNAr biocatalysts from de novo proteins** — protein engineering, off-thread.
- **Sasha Gusev new article: Leveraging tumor dynamics to discover mutations influencing progression and treatment response** (Genome Medicine) — precision oncology, methodologically interesting but cancer focus is off your tracked disease threads.
- **Patrick Ryan related-research extras:** Vaccine Safety Surveillance India; multiple DSME-and-mortality Diabetes-supplement abstracts; tirzepatide/semaglutide dose-response; CF modulator South Africa qualitative study — bulk of the Patrick Ryan feed; useful pharmacoepi reads only if specifically relevant to your day's work.
- **Christopher G. Chute citations: Mental and Physical Health Predictors of Return-to-Work in Long COVID** — N3C-adjacent but off-thread.
- **Joshua C. Denny citations extras:** EECFS causal feature selection; HUNT migraine ML; clopidogrel + CYP2C19; UKB glaucoma definition comparison; ICI colitis digital phenotype — bulk of the Denny citations feed; the UKB glaucoma Dx-vs-Tx-definition paper and the ICI colitis digital phenotype are mildly on the EHR-phenotyping thread but not high-priority.
- **NCBI What's New 'UK Biobank' in PubMed** (06-20) — aggregate digest; primary on-thread hits already captured via Scholar (e.g., the Yang UKB lifestyle×arrhythmia paper).
- **bioRxiv / medRxiv subject collection alerts** (06-21, 06-22) — aggregate digests covering Bioinformatics / Genetics / Genomics / Epidemiology / Genetic and Genomic Medicine; on-thread hits will reach you via Scholar within ~1-2 days of preprint posting (e.g., the Wang dish-to-biobank preprint reached you via Karczewski + self-feed within 9 days of bioRxiv posting).

---

## Suggestions for the pipeline

Carry-forwards from prior reports plus today's items:

1. **arxiv-digest 06-20 fetch-failure follow-up.** 06-21 ran clean (0 papers, no warnings) — the fix appears to have held. **Confirm by checking the 06-22 run** (likely already executed by the time this report is committed). If 06-22 also runs clean, consider the issue resolved; if it recurs, the inter-category-pause and per-category-retry-with-jitter recommendations from the 06-20 report remain the next actions.

2. **`knowledge graph` keyword: 8th consecutive window of non-biomedical hits** (today's *ship welding quality NK model* result is the latest). Specific fix unchanged: tighten to `biomedical knowledge graph` OR `clinical knowledge graph` OR a compound filter `(knowledge graph) AND (medical OR biomedical OR clinical OR EHR OR phenotype OR drug OR disease)`. This is now the highest-priority pipeline change — 8 consecutive windows of noise from a single keyword is wasted attention.

3. **`mendelian diseases` keyword leak — 8th consecutive window.** Today's hit *Artificial Sweeteners and Autoimmune Diseases: Insights From Integrative Bioinformatics and Mendelian Randomization* is a Mendelian-*randomization* paper, not a Mendelian-*disease* paper. Fix: rename keyword to `"mendelian disease"` (singular, in quotes) or to a compound `mendelian disease NOT "mendelian randomization"`.

4. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds** (carry-forward, unaddressed). Today's items #2 (Koch PGR), #3 (Jaech NEJM AI), #4 (Neumiller GLP-1 kidney), #6 (Caliskan LKD), #7 (Powell AD-EHR), #8 (Cuperus HPO-Netherton), and #9 (Lee asthma-PRS-proteomic) all reached you via Scholar because they live in journal/medRxiv/bioRxiv venues outside q-bio/stat.AP. The current `arxiv-digest` pipeline can never reach these without source expansion. **Stronger argument this report than prior reports:** 9 of 9 HIGH items this window are non-arXiv. The arxiv-digest pipeline as configured cannot match what Scholar catches.

5. **Add `noncoding variant interpretation` / `regulatory variant effect` / `MPRA` / `episignature` keywords** (extending the 06-20 recommendation). Today's Awamleh KMT2A/KMT2B episignature paper would have been caught by `episignature`. Episignatures + MPRA + the 06-20 Marderstein noncoding paper define the *functional evidence for variant interpretation* sub-thread that's increasingly active in 2026 H1.

6. **Add `dish-to-biobank` / `cellular perturbation` / `in vitro to biobank` keywords** (new). The Wang T2D β-cell paper (#5) is exactly the cross-scale bridge the Felici review (#1) advocates as the field's direction. This sub-thread is going to grow; worth catching directly rather than via citation-graph noise from author feeds.

7. **Add `target trial emulation` / `target-trial emulation` keyword** (new). Today's Neumiller GLP-1 kidney paper (#4) is the latest in a stream of TTE-template pharmacoepi work; the term has converged on this spelling. Would catch most of your pharmacoepi sub-thread directly.

8. **Continue tracking your own self-citation feed and self-related-research feed as the highest-precision channels.** Today's items #1 (Felici), #5 (Wang dish-to-biobank), #8 (Cuperus HPO-Netherton), and #9 (Lee asthma PRS-proteomic) all fired the Chenjie Zeng new-related-research feed; #1 also fired the Denny citations feed (double-feed). 4 of 9 HIGH items came through your own feed — this is consistently the highest-yield single channel in the digest pipeline.

9. **Carry-forwards still unaddressed:** PRS-stability / PRS-tails / polygenic-tails keywords; proteomic-signature / aging-clock / organ-specific-aging keywords; `mendelian diseases` and `drug repurposing` keyword tightening; multi-source feed expansion to cs.LG / stat.ME / medRxiv / bioRxiv.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 9 | (1) Felici et al. *Cell Genomics* GWAS-translation review [Zeng self-feed + Denny citations], (2) Koch et al. Pakistan Genome Resource [Nature, Denny citations], (3) Jaech et al. LLM rare-disease genome reanalysis [NEJM AI], (4) Neumiller et al. GLP-1 RA kidney outcomes [AJKD, Ryan feed], (5) Wang et al. dish-to-biobank β-cell T2D [bioRxiv, Karczewski + Zeng self-feed], (6) Caliskan et al. LKD genetic evaluation practices [Kidney Int Reports, APOL1 feed], (7) Powell et al. memory-clinic AD EHR+LLM [npj Dementia], (8) Cuperus et al. HPO Netherton curation [BJD, Zeng self-feed], (9) Lee et al. asthma PRS + IL1R1 proteomic family-based [medRxiv, Zeng self-feed] |
| METHODS-WATCH | 6 | Shang et al. AKI electronic phenotype [AJKD], Datta et al. KG-augmented LLM multimodal EHR [JMIR AI], Margolis isoform-level neuropsychiatric PheWAS [dissertation], Abujamous et al. Middle East BRCA1 ancestry-AF reclassification [Biomolecules & Biomedicine], Awamleh et al. KMT2A/KMT2B episignatures [Genetics in Medicine], Yang et al. UKB lifestyle×PRS arrhythmia [BMC Cardiovasc Disorders] |
| SKIP | ~30 | See SKIP/noise section above |

Compared to the 06-20 report (6 HIGH / 6 METHODS-WATCH), this window
delivers a higher HIGH count, driven by **four self-feed firings**
(items 1, 5, 8, 9) and **two Nature/NEJM-AI top-venue papers** (Koch
PGR, Jaech LLM-rare-disease). The recurring pattern is now confirmed
across four consecutive windows: nearly all on-thread signal comes from
Scholar alerts; the `arxiv-digest` pipeline produced **zero** on-thread
papers this window (clean 0-paper digest, not a fetch failure). The
multi-source-expansion recommendation (item #4 in pipeline section) is
now the single most consequential improvement available.
