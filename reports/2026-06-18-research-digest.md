# Research digest report — 2026-06-18

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-17 → 2026-06-18** (since the prior 2026-06-17 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-17 → 06-18 | One large batch 06-18 06:59Z (≈23 author-feed alerts: Chenjie Zeng, Bastarache, Karczewski, Denny, Hripcsak, Hernán, Yang, Pritchard, Montgomery, Szolovits, Callahan, Zitnik, Vogelstein, Natarajan, Luo, Chute, Shendure, Kastner). Plus 06-17 06:02Z keyword tail (variant interpretation, KG, FM+EHR) already covered in yesterday's report. |
| `arxiv-digest` repo (`digests/`) | 2026-06-17 → 06-18 | **06-17 = 2 papers, both off-thread (NYC congestion pricing FM; cancer pathology FM eval). 06-18 not yet produced** at report time (workflow runs 10:30 UTC; this report is pre-cron). |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |

> ⚠️ **arxiv-digest pipeline remains essentially dry** — yesterday's
> output (06-17) added 2 papers, both score-1 "foundation model"
> incidental hits (one urban-mobility econometrics paper, one
> cancer-pathology FM evaluation), neither on-thread. As in the four
> prior reports, virtually 100% of the on-thread signal this window
> came from Scholar alerts surfacing journal / medRxiv articles. The
> overdue pipeline fixes (add `cs.LG`, `stat.ME`, medRxiv/bioRxiv;
> fix `mendelian diseases` / `knowledge graph` / `drug repurposing`
> keywords) would have surfaced items #2, #3, #5 below directly.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below
> contextualize that metadata against your research threads; nothing
> here reflects full-text reading.

---

## Executive summary

- **The standout this window is a *self-citation* of your PheTK tool
  inside a mechanistic APOL1 transplant-rejection paper in JCI.**
  Pell et al. (J. Clin. Invest., 2026) characterize APOL1-G1/G2 effects
  on T-cell receptor signaling using transgenic mice and explicitly cite
  *PheWAS analysis on large-scale biobank data with PheTK* — i.e., your
  group's tool. This surfaces in **both** your *Chenjie Zeng new
  citations* feed and the *Joshua Denny new citations* feed (Denny is
  PheWAS-adjacent). It's the cleanest example yet of your APOL1 +
  PheWAS infrastructure work being cited *back into* an APOL1
  mechanism paper at a top venue, and it's directly on the APOL1 +
  transplant-decision-making slice of your INTERESTS file. **Read first.**
- **First on-thread drug-repurposing hit in three weeks.** Schatz,
  Beasley, Melo-Filho, Tropsha et al. (*ACM Transactions on Computing
  for Healthcare* / *Computational Biology*, 2026) — *Using Extraction
  and Evaluation of Explanations for Drug-Repurposing on Knowledge
  Graphs* — surfaces via Tiffany Callahan's related-research feed. This
  is exactly the angle your INTERESTS file specifies: "knowledge-graph
  / GNN approaches with *explainable* hypothesis output (path or
  subgraph rationales rather than opaque link-prediction scores)." The
  Tropsha lab + Callahan/PheKnowLator lineage is the right institutional
  signature. After two consecutive windows of off-thread "drug
  repurposing" keyword noise (benfotiamine MD studies), this is the
  first item that fits the actual research thread.
- **PRS robustness pattern continues, this time *across GWAS releases*.**
  Ferreira et al. (medRxiv, Bastarache related-research) characterize
  PRS *stability* — how individual PRS rankings change as successive
  GWAS releases grow in sample size and ancestry diversity. Pairs with
  last report's de La Harpe paper on intra-individual PRS
  disagreement across *scores* (ASCVD); this one looks at instability
  across *versions* of the same score. Together they're now a clear
  *patient-level PRS robustness audit* sub-thread.
- **Consensus AD GWAS meta-analysis lands in Nature Genetics.**
  T FAM193B consortium (Nature Genetics, 2026) — meta-analysis of
  European-ancestry AD/ADRD GWAS at 128,681 case-or-proxy cases.
  Surfaces in both Joshua Denny and Jian Yang feeds. Off your direct
  disease threads, but a default reference-class GWAS that will be
  cited heavily for the next two years.
- **High-dimensional liver radiomic GWAS** (Tian et al., medRxiv,
  Jian Yang related-research) — DL segmentation + radiomics yields 200
  liver imaging phenotypes, GWAS'd against common metabolic disease.
  This is the *imaging-derived phenotype + GWAS* pattern; highly
  relevant if you're extending AoU PRS work into imaging endpoints (AoU
  is on-boarding clinical imaging for sub-cohorts), and the methods
  pattern itself is transferable.
- **One useful target-trial-emulation tutorial.** Hatano et al.
  (*International Orthopaedics*, 2026) is a discipline-specific TTE
  practical guide using THA vs hemi-arthroplasty for hip fracture as
  the worked example. METHODS-WATCH — not on a disease thread, but a
  clean concise TTE walkthrough useful as a citation when training new
  collaborators in pharmacoepi.
- **Carry-forward duplicate:** Bastarache feed re-surfaces the Zhao
  *targeted reflex RNA-seq* paper (npj Genomic Medicine), which was
  already covered as a 06-13 item and referenced in yesterday's report
  alongside the Mighton ACMG-VUS statement. No new content.
- **No new on-thread items for the rest of the disease threads:**
  no new CF/CFTR, no new CHIP/VEXAS, no new IBD, no new
  multimorbidity-trajectory work, no new EHR foundation-model paper,
  no new ACMG statement, no new All of Us or UK Biobank paper. The
  large 06-16 Scholar batch covered yesterday's report — today's batch
  is thinner.

Counts: **5 HIGH**, **6 METHODS-WATCH**, rest SKIP. Today's window is
notably lighter than the 06-13→06-17 catch-up window — expected, since
this is a 24-hour slice rather than a 5-day one.

---

## HIGH priority — detailed reports

### 1. APOL1-risk alleles modulate T-cell receptor signaling to promote allograft rejection
- **Authors / venue:** J. Pell, E.M. Tanvir, Z. Sun, I. Chernova, A. Reghuvaran et al. — *The Journal of Clinical Investigation*, 2026. URL: `jci.org/articles/view/193173`.
- **Surfaced by:** *Chenjie Zeng — 1 new citation to articles by* (i.e., **cites your work** — specifically *PheWAS analysis on large-scale biobank data with PheTK*) **+** *Joshua C. Denny — 2 new citations* (same paper, same citation hook). Double-feed saturation, one feed of which is your own group.
- **Thread:** APOL1 disease thread (kidney + **transplant decision-making**, ancestry considerations) **+** PheWAS / phecode infrastructure (your own tooling cited) **+** variant interpretation (G1/G2 functional characterization).
- **What it is:** Mechanistic study of how APOL1 G1 and G2 risk alleles modulate T-cell receptor signaling and promote kidney allograft rejection. Uses transgenic mice with *physiologic* expression of wild type (G0), G1-APOL1, or G2-APOL1 — i.e., not over-expression artifacts. Reports that both G1 and G2 carriers show greater CD8+ T-cell activation with expansion of a central-memory subset (snippet cuts there). The implicit clinical framing is that APOL1 high-risk donor (or recipient?) status is not just a tubular-cell intrinsic mechanism for kidney disease but also has a *cell-extrinsic immune* contribution that bears on transplant matching and immunosuppression intensity.
- **Why it matters to you:** Four converging hits.
  (a) **The paper cites your PheTK paper directly** — this is the rare case of seeing your large-scale-biobank infrastructure work make it into the citation list of a *mechanistic* immunology paper in a top-tier translational journal. That's a useful credentialing signal for any subsequent PheWAS-tool grant or methods writeup.
  (b) APOL1 is explicit in your INTERESTS file under "kidney disease risk, **transplant decision-making**, ancestry considerations." This paper directly attacks the transplant-decision question with a mechanistic basis — bridging the *population-genetics* APOL1 story (your PheWAS-side work) to the *immunology* APOL1 story for the first time at this venue tier.
  (c) Surfacing in both your own citation feed *and* the Denny feed (Denny was the eMERGE PI behind the original PheWAS infrastructure) — the same paper landing in two PheWAS-tool author feeds is a strong field signal.
  (d) Pairs naturally with last week's pediatric APOL1 / BIG Initiative paper (Zahr et al., Ped Nephrology) — together they sketch a *full life-course* APOL1 thread: pediatric onset (Zahr) → adult CKD progression (your existing work) → transplant rejection mechanism (Pell, here).
- **Action:** **HIGH — read first.**
  (i) Identify which of your published methods or analyses they cite (likely PheTK, possibly your AoU APOL1 paper as well — check the reference list).
  (ii) Note which APOL1 variant model they use (transgenic mice physiologic expression vs human iPSC-derived T cells); this informs how transferable the immune-axis result is to your population-level analyses.
  (iii) The clinical actionability question — does the paper recommend a change to *donor selection* on APOL1 status? If so, this becomes a citation when arguing for or against APOL1 donor screening in any transplant-decision write-up you do.
  (iv) Worth a brief note back to whichever co-authors maintain PheTK — citation tracking for tool funding.

### 2. Using Extraction and Evaluation of Explanations for Drug-Repurposing on Knowledge Graphs
- **Authors / venue:** K. Schatz, J.M. Beasley, C. Melo-Filho, A. Tropsha et al. — *ACM Transactions on Computing for Healthcare* (or *Computational Biology*), 2026. URL: `dl.acm.org/doi/pdf/10.1145/3820155`.
- **Surfaced by:** *Tiffany J. Callahan — new related research* alert.
- **Thread:** Drug repurposing (**explainable KG / GNN approach**) **+** knowledge graphs & ontologies (biomedical KG) **+** ML for precision health.
- **What it is:** Methodology for *extracting and evaluating explanations* for drug-repurposing predictions made by knowledge-graph models. From the abstract framing: "Knowledge-graph (KG) databases represent information about real-world entities (via nodes) and relationships between them (via edges) in the form of semantic networks. We consider the problem of reliably inferring novel relationships between [drug and disease nodes]..." — i.e., link-prediction on a biomedical KG, with the contribution being the *explanation* layer (subgraph rationale / metapath extraction / counterfactual evidence) and a *quality evaluation* framework for those explanations.
  Authorship is the Tropsha (UNC chemoinformatics / OpenPredict / SemMedDB-KG lineage) + Beasley / Melo-Filho group, which has been the steady contributor to explainable KG-based repurposing since the Drug Repurposing Hub days.
- **Why it matters to you:** Three reasons.
  (a) **This is the first drug-repurposing hit in three windows that fits your INTERESTS-file specification verbatim.** That section explicitly calls out "knowledge-graph / GNN approaches with *explainable* hypothesis output (path or subgraph rationales rather than opaque link-prediction scores)." Schatz et al. attack the explanation-extraction problem head-on, which is the gap between the "PrimeKG / Hetionet says drug X for disease Y" surface-level paper and a paper that you'd actually cite when arguing that a KG-derived repurposing hypothesis is *clinically* worth testing.
  (b) The Callahan-feed surfacing is high-signal: Tiffany Callahan maintains PheKnowLator, one of the most-used biomedical KG-construction tools, and her related-research alerts have been the most reliable filter for KG-grounded biomedical work. This isn't a random keyword leak.
  (c) Methodologically transferable: the "explanation evaluation framework" piece is reusable for *any* GNN/KG you might build downstream — e.g., for the rare-disease HPO-based repurposing pattern you mentioned in INTERESTS.
- **Action:** **HIGH.**
  (i) Read for the explanation type — are these *metapath-based* (which fits HPO-to-drug reasoning naturally) or *subgraph-based* (better for unknown-mechanism hypothesis generation)?
  (ii) The *evaluation framework* is the main practical asset — what's the gold standard they use (DrugBank known indications, ClinicalTrials.gov, biomedical literature)? Their evaluation harness is what you'd lift wholesale.
  (iii) Check whether they test against EHR-derived signals (real-world prescribing) — your INTERESTS specifies "EHR-based repurposing signals mined from real-world prescribing." If they don't, that's the obvious extension point.
  (iv) Update the `INTERESTS.md` cross-references; this becomes the new default cite when arguing for explainable KG repurposing.

### 3. Characterising the Stability of Polygenic Risk Scores: implications for risk stratification
- **Authors / venue:** A. Ferreira, P.A. Lind, H. Moody, I.B. Hickie, C.M. Olsen et al. — *medRxiv*, 2026 (preprint 2026.05.17.26353273).
- **Surfaced by:** *Jian Yang — new related research* alert (Yang's group has been central to PRS portability methodology).
- **Thread:** Genetic epidemiology (**PRS robustness** sub-thread) **+** ML for precision health (decision-grade scoring) **+** clinical translation.
- **What it is:** Empirical characterization of **PRS stability across successive GWAS releases**. Abstract framing: "Polygenic risk scores (PRS) improve progressively as genome-wide association studies (GWAS) increase in sample size and ancestral diversity, yet the effect of successive GWAS releases on individual PRS rankings remains poorly [characterized]." I.e., the question is — if I genotype a patient, run their PRS using GWAS release vN, then re-run on release vN+1 a year later, does that patient's rank in the population shift, and by how much? This is the *temporal / versioning* axis of PRS robustness.
- **Why it matters to you:** Pairs directly with last report's #11 (de La Harpe et al., ASCVD PRS patient-level robustness across *different scoring methods*). Together they sketch a coherent *PRS-as-a-clinical-test robustness* sub-thread:
  - **de La Harpe**: across-method discordance (PRS-CS vs LDpred2 vs PT, all built on the same GWAS) → which score to trust today.
  - **Ferreira**: within-method instability (the same score updated as the upstream GWAS grows) → when to *re-deliver* a PRS to a patient and what the threshold for changing their clinical category is.
  This is operationally important for any PRS-deployment write-up — "we report a PRS today, but how often do we re-issue?" is the exact question regulators will ask, and the literature so far has been thin. Ferreira's surfacing in the Yang feed (PRS-portability-native author) means it's likely the field's go-to citation for that sub-question.
- **Action:** **HIGH.**
  (i) Read for the discordance metric they use (Δ percentile rank? % crossing the 95th-percentile threshold? rank-correlation across versions?).
  (ii) The temporal axis — do they use real successive GWAS releases (e.g., PGC SCZ wave 1 → 2 → 3) or simulate increased N from the same base GWAS? Real-release is more informative.
  (iii) Whether the instability is uniform across ancestries — if non-European individuals get more rank-shuffled with each release, that's a fairness story.
  (iv) Add to the carry-forward "PRS robustness audit" mini-bibliography (with de La Harpe).

### 4. Consensus meta-analysis of genome-wide association studies for Alzheimer's disease and related dementias
- **Authors / venue:** T FAM193B consortium — *Nature Genetics*, 2026. URL: `nature.com/articles/s41588-026-02583-1`.
- **Surfaced by:** *Jian Yang — new related research* alert (also reachable via Karczewski / Denny if you scan further down those feeds).
- **Thread:** Genetic epidemiology (GWAS reference) **+** AD as a tracked condition under multimorbidity / aging.
- **What it is:** A *consensus* meta-analysis of European-ancestry GWAS for Alzheimer's disease and related dementias (ADRD), pooling 128,681 cases or proxy cases plus controls. The "consensus" framing implies a deliberate effort to reconcile prior overlapping AD meta-analyses (Wightman, Bellenguez, Schwartzentruber) whose case sets and proxy-case definitions partly overlap and whose published loci have not fully replicated. Nature Genetics venue + consortium authorship signals this becomes the *de facto* reference AD GWAS for the next 2 years.
- **Why it matters to you:** Two angles.
  (a) Default-citation utility — any analysis you do touching AD risk (multimorbidity, MR exposures, cross-disease PRS portfolios, AoU dementia phenotyping) will need to cite a single AD GWAS, and from this point on it's almost certainly this one. Worth knowing the case definition (clinical AD vs ADRD vs proxy by parental history) so you know what your PRS is *actually* predicting.
  (b) Methodological — the *consensus* framing means they reconciled conflicting case definitions across prior meta-analyses; their reconciliation approach is itself a template for any future cross-cohort phecode-vs-clinical phenotype reconciliation, which is on your computable-phenotype thread tangentially.
- **Action:** **HIGH (as reference utility, not as a methods read).**
  (i) Capture: total cases, total proxy cases, case definition (any clinically diagnosed AD vs all ADRD), ancestry breakdown.
  (ii) Note the GWAS summary statistics availability — for PRS construction, you need to know if both clinical-AD-only and AD+proxy stats are released separately.
  (iii) Single-paragraph mental note for later, not a deep read.

### 5. Genetic architecture of high-dimensional liver radiomic phenotypes and their role in common metabolic diseases
- **Authors / venue:** H. Tian, M. Kamineni, B. Truong, V.K. Raghu, J.S. Dron et al. — *medRxiv*, 2026 (preprint 2026.05.19.26353617).
- **Surfaced by:** *Jian Yang — new related research* alert.
- **Thread:** Genetic epidemiology (**imaging-derived endpoints** / GWAS) **+** ML for precision health (DL-derived phenotype) **+** EHR/biobank infrastructure (likely UKB imaging substudy) **+** adjacent to MASLD / cardiometabolic disease.
- **What it is:** Deep-learning–based liver segmentation + radiomics extraction produces 200 well-defined quantitative liver-image phenotypes from biobank-scale abdominal imaging (almost certainly UKB MRI substudy, n ~40K). GWAS each, then map to common metabolic diseases (NAFLD/MASLD, T2D, ASCVD-relevant lipids). This is the *radiomics-as-quantitative-phenotype* pattern: instead of GWAS'ing the binary "MASLD vs not," you GWAS *200 individual imaging descriptors* and let the genetic architecture decompose mechanism.
- **Why it matters to you:** Three reasons.
  (a) Methodologically transferable to AoU — AoU is on-boarding imaging for sub-cohorts; a "200 DL-derived imaging phenotypes per organ" template scales cleanly. If you have any AoU imaging work in mind for the next 12 months, this is the methods scaffolding.
  (b) On the *imaging-derived phenotype* axis that has been underrepresented in your INTERESTS file — worth a note to consider adding "imaging-derived phenotypes / radiomic GWAS" as an explicit thread.
  (c) The Dron / Truong / Raghu authorship lineage is the Khera / Natarajan PRS-and-imaging-cardiometabolic group at MGH/Broad — high citation-quality group, paper will travel.
- **Action:** **HIGH (methods-watch leaning).**
  (i) Read for the segmentation backbone (TotalSegmentator? a custom 3D U-Net?) and the radiomics feature set (pyradiomics' default 110-feature panel vs custom).
  (ii) The GWAS-per-phenotype scale — do they correct for the 200 phenotypes via Bonferroni, FDR, or a hierarchical model? That decision matters for any radiomic-GWAS work you do.
  (iii) Note which liver features map to MASLD risk loci (PNPLA3, TM6SF2, etc.) and which surface novel genetic architecture — the novel-locus list is the actionable bit.
  (iv) Potentially propose "imaging phenotypes + GWAS" as a new INTERESTS subsection if you do AoU imaging work this year.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **GWAS of extended prescription analgesic use identifies genetic loci in chronic pain** — C.E. Harlow, E. Uzochukwu, H.A. Fernando, C.E. Mordaunt et al. — *Nature Communications*, 2026 (Jian Yang related-research). Chronic-pain GWAS defined via *prescription-analgesic exposure*, not via ICD pain codes. *Watch for:* the prescription-derived phenotype definition (which drug list, what duration cutoff, how they handle co-prescription for non-pain indications). This is a clean instance of the **prescription-as-phenotype** EHR-phenotyping pattern, transferable to any opioid / GLP-1 / SGLT2 phenotype you might build in AoU/UKB.

- **Functionally informed annotation influences pathway-specific polygenic risk and disease inference in Alzheimer's disease** — K. Bazemore, T. Iqbal, A.B. Kuzma, S.F.A. Grant et al. — *medRxiv*, 2026 (preprint 2026.05.25.26353905, Jian Yang related-research). Pathway-PRS where SNV-to-gene mapping is *functionally* informed rather than position-based. *Watch for:* the functional-annotation source (cS2G? OpenTargets? eQTL fine-mapping?) and whether the gain in pathway-PRS portability matters more than the gain in pathway-PRS variance explained. Transferable to any pathway-specific PRS work, including the rare-pathogenic-variant + PRS composite-risk patterns on your interests.

- **Improved prostate cancer prediction by combining PSA test results with Genetic Risk Scores (PRS)** — J. Lu, G. Chen, S.W.D. Merriel, M.N. Weedon, A. Murray et al. — *medRxiv*, 2026 (preprint 2026.05.14.26353195, Jian Yang related-research). Biomarker + PRS integration template; PSA is the canonical false-positive-prone screening biomarker. *Watch for:* whether they use net-reclassification / decision-curve framing (the right decision-grade metric) or just Δ AUC. Generalizes to any biomarker + PRS combination — CA-125+PRS, GFAP+PRS, troponin+PRS.

- **Improving the design of observational studies in orthopaedics: a practical guide to target trial emulation** — M. Hatano, Y. Kimura, H. Yasunaga, S. Tanaka — *International Orthopaedics*, 2026 (Miguel Hernán citation feed). Discipline-specific TTE walkthrough using THA vs hemi-arthroplasty as the worked example. *Watch for:* the "translating a causal question into a target trial protocol" section — useful as a teaching reference when training non-pharmacoepi collaborators on the TTE framework you already use.

- **CMSV: Long-Read-Based Structural Variation Detection Through a CNN-Mamba Model** — S. Cheng, H. Ma — *Genes*, 2026 (Stephen Montgomery related-research). DL-based SV detection from long-read sequencing using a CNN+Mamba hybrid. *Watch for:* whether the Mamba state-space backbone gives meaningful gains over the Transformer-based SV-callers (SVision, NanoVar, deepvariant SV mode) — long-read SV detection accuracy matters for your variant-interpretation thread, even though this paper is on the discovery side rather than classification.

- **Food substitution modelling approaches: a methodological study** — T. Roosdorp, M. Fridén, D.B. Ibsen, F. Rosqvist — *Current Developments in Nutrition*, 2026 (Hernán citation feed). Methodological comparison of nutritional substitution-effect models showing that some modeling choices give *estimates opposite to the true simulated effect*. *Watch for:* the standard-multivariate-regression vs leave-one-out vs g-method comparison — these failure modes generalize to *any* "what if we replace X with Y" causal question in EHR data (medication switching, treatment substitution).

---

## SKIP / noise (logged, no action)

- **Bastarache re-surface of Zhao et al. *Targeted reflex RNA-seq* (npj Genomic Medicine)** — already covered in the 06-13 report and referenced in yesterday's 06-17 report alongside Mighton ACMG-VUS. Duplicate.
- **APOL1 / TCR rejection paper also surfaces in Joshua Denny feed** — same paper as item #1; not a separate item.
- **Targeted reflex RNA-seq Bastarache feed also surfaces *cardiovascular risk factors in non-classical Fabry disease*** (Veldman et al., Orphanet J Rare Dis) — lysosomal-storage rare disease + CV risk modifier; adjacent to your rare-disease thread but not central. Logged.
- **Vivek Natarajan citations** — LLMs for scientometric mapping of scientific controversy (Susnjak et al., Scientometrics). Off-thread; not on the Med-Gemini-deployment debate.
- **Bert Vogelstein citations** — ctDNA detection in NSCLC via mutant-DNA enrichment (Labrousse et al., Scientific Reports). Cancer ctDNA, off your threads.
- **Peter Szolovits / Jian Yang misc** — *Medical Vision-Language Models for Robust Disease Diagnosis* (Algumaei et al., CVPR-adjacent); *Non-coding RNA networks regulating NLRP3 inflammasome* (Raajasekar, GMR); *Post-translational modifications in psychiatric disorders* (Hu et al., J Transl Med); *SoK: A taxonomy of LLM threats* (Stylianou et al., Computer Science Review) — all off the EHR-FM / clinical-deployment axis or general LLM-security.
- **Jonathan Pritchard / Marinka Zitnik citations** — *Charting the computational landscape of single-cell genetic perturbation* (Zhang et al.); *SimSD: Simple Speculative Decoding in Diffusion LMs* (Cui et al.) — perturbation single-cell and ML-systems work, off the clinical / EHR-FM thread.
- **George Hripcsak / Christopher Chute citations** — *How Do I Want to Live with Type 1 Diabetes?* (Barth et al., CHI-style HCI); *AI for Physical, Cognitive, and Developmental Challenges* (Wang & Begg, AI in Social Work); HCI/social-work books citing his computable-phenotype work. Off-thread.
- **Daniel Kastner citations** — *Non-coding RNA networks regulating NLRP3 inflammasome in neurodegenerative and CV diseases* (Raajasekar, GMR). Mechanistic NLRP3, off your VEXAS/CHIP empirical thread.
- **Jay Shendure / Konrad Karczewski related research** — *Parallel reporter assay for zebrafish* (Ligunas & Materna, Dev Biol). Cis-regulatory module assay, off the human-population-genetics thread.
- **Yuan Luo citations** — *Role of ChatGPT in higher education* (Abdelrahman et al.). Off-thread.
- **JAMA Cardiology editor invitation** — ESC 2026 submission promo email; not research content. Logged.
- **Joshua Denny related-research** — *Consensus AD GWAS* covered as #4 above; the second item in that feed (the Hu et al. *Post-translational modifications in psychiatric disorders* review) is off-thread.
- **arxiv-digest 06-17** — both papers off-thread: *NYC congestion pricing* (urban-mobility econometrics using TS foundation models, score 1, keyword leak), *FM representations for multimodal cancer analysis* (pathology FM evaluation, score 1, keyword leak). Neither lands on the CLMBR/MOTOR/EHRSHOT axis.

---

## Suggestions for the pipeline

All four prior reports' recommendations remain unactioned. None of
today's HIGH items were surfaced by `arxiv-digest`; all five came from
Scholar alerts. Reiterated here for visibility:

1. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds.** Items
   #3, #4, #5 today (Ferreira PRS stability, AD GWAS consensus meta, Tian
   liver radiomic GWAS) are all medRxiv / *Nature Genetics* — none
   reachable from the current q-bio / stat.AP feed set. Item #2 (Schatz
   KG-repurposing explanations) is ACM venue and wouldn't surface there
   either, but would surface from cs.LG.
2. **`mendelian diseases` keyword still leaks MR papers.** 6th consecutive
   window. Replace with `OMIM` / `MIM:` IDs or exclude `-randomization`.
3. **`knowledge graph` keyword: 6th consecutive window of non-biomedical
   hits.** Today's actually-on-thread KG paper (#2) was surfaced by the
   Callahan feed, not by the keyword scan. Fix overdue. Recommend
   `biomedical knowledge graph` OR `clinical knowledge graph` OR
   `(knowledge graph) AND (medical OR biomedical OR clinical OR EHR OR
   phenotype OR drug OR disease)`.
4. **`drug repurposing` keyword: still target-only.** Today's actually-on-
   thread repurposing paper surfaced via Callahan, not via the keyword.
   Add `(EHR OR real-world OR biobank OR knowledge graph OR target trial
   OR explanation)` to the filter logic, or split the keyword into
   `chemistry-only` (SKIP) vs `clinical-evidence-loop` (HIGH).
5. **Add `proteomic polygenic` / `pQTL polygenic` as a keyword.** Carried
   from last week; not retracted (no new instance today but pattern still
   live).
6. **Add `radiomic GWAS` / `imaging-derived phenotype GWAS` as
   keywords.** Today's #5 (Tian et al.) is the second imaging-GWAS in
   two weeks (the prior was a kidney-volume paper logged but not
   reported). Worth catching directly.
7. **Add `PRS stability` / `polygenic score stability` / `PRS robustness`
   as keywords.** With Ferreira (today) + de La Harpe (last report),
   this is now a coherent sub-pattern.
8. **Track when the user's own group's tools (PheTK, the AoU PRS paper,
   the phenomic-comparison paper) get cited.** Today's #1 is a clean
   instance of a useful citation surfacing in your Chenjie Zeng feed —
   keep the self-citation alert as-is; it's the single highest-precision
   feed you have.
