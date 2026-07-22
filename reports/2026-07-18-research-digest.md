# Research digest report — 2026-07-18

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-07-18** (since the prior 2026-06-20 report;
28-day gap. The bulk of triage below focuses on the most recent
2026-07-16 → 07-18 batches, where email coverage is complete; earlier
windows are noted only where a citation of your own work or a top-tier
paper falls in them.).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-07-16 → 07-18 | Three large batches: 07-16 15:53Z (~14 alerts — Hernán, Luo/Naderian PRS, Szolovits, Bastarache citations, Denny, Kastner, Karczewski, Chenjie Zeng related, Fei Wang, Zitnik, Montgomery). 07-17 17:51Z (~15 keyword alerts — UK Biobank, AoU, drug repurposing, EHR FMs, rare diseases, APECED, UDN, phenotype-risk-scores, CF carriers, mendelian, APOL1, KG, autoimmune, variant interpretation). 07-18 02:44Z (~30 author-feed alerts — **1 new citation to Chenjie Zeng**, Bastarache, Denny, Hripcsak, Ryan, Karczewski, Kastner, Chute, Vogelstein, Natarajan, Yang, Pritchard, Montgomery, Szolovits, Zitnik, Callahan, Hernán, Shendure, Kohane, Ellinor, Wendy Chung, Neale, Nigam Shah). |
| `arxiv-digest` repo (`digests/`) | 2026-07-14 → 07-18 | **5 daily files;** 07-14/15 empty (or nearly so); 07-16 = 1 paper (Evo 2 biosecurity probes, off-thread FM hit); 07-17 = 1 paper (scVision cell FM, off-thread FM hit); 07-18 = 0 papers. |
| NCBI "My NCBI What's New" (AoU, UK Biobank) | daily | Aggregate PubMed digests. 07-17 batch: 14 UK Biobank + 3 AoU items. |
| bioRxiv / medRxiv subject alerts | daily | Aggregate; not individually triaged. |

> ⚠️ **`arxiv-digest` remains essentially dry** — 2 papers across 5 days,
> both single-keyword `foundation model` hits that are off-thread
> (biosecurity metagenomics; single-cell vision FM). As in the last six
> reports, 100% of on-thread signal came from Scholar / PubMed. The
> pipeline recommendation stands: **add `cs.LG`, `stat.ME`, and a
> medRxiv/bioRxiv feed**; without them all HIGH-priority hits below
> would remain invisible to the `arxiv-digest` pipeline.

> Caveat: Scholar alert emails contain title, authors, venue, and a
> two-line snippet — no full abstract. Triage below reads the snippet +
> venue signal + surfacing pattern (which feeds fire, how many); it does
> not include full-text reading. Papers marked HIGH warrant a full-text
> follow-up.

---

## Triage summary — this window

### Top-of-pile (READ FIRST, in order)

1. **[SELF-CITATION] Zemanick, Graeber, Castellani, Cutting et al. —
   *The role of sweat chloride in determining CFTR protein restoration
   in people with cystic fibrosis* (*Lancet Respiratory Medicine*,
   2026).** Quadruple-feed saturation: (a) **`1 new citation to
   articles by Chenjie Zeng`** (your citations feed lit up — the
   strongest possible surfacing pattern this pipeline produces), (b)
   **`Chenjie Zeng — new related research`**, (c) **`10 new citations
   to articles by Joshua C. Denny`**, (d) **`"Cystic fibrosis carriers"
   — new results`** keyword feed. Also cited in the CF-carriers thread
   (which reflects your Vanderbilt-era CF/CFTR work). **A top-tier
   journal (Lancet Respir Med) citing your work is the single
   highest-priority item this window.** See detailed report §1.
2. **Wu, Lee, Abiri, Ionita-Laza — *Domain-aware matrix completion for
   phenotype imputation using electronic health record data with
   applications in genomic research* (*Annals of Applied Statistics*,
   2026).** Surfaced by *Lisa Bastarache — new related research*.
   Directly on the **PheWAS/phecode + EHR phenotyping** threads —
   phenotype imputation over sparse EHR-phecode matrices is the
   methodological gap that has held back rare-phecode PheWAS since
   phecodes were introduced. Ionita-Laza's group is one of the two or
   three doing rigorous latent-variable statistical genomics; landing
   in AoAS (methods journal) means this is a reference-class methods
   contribution. See §2.
3. **Naderian, Smith, Dikilitas, Hamed et al. — *Additive value of
   polygenic risk and family history for coronary heart disease risk
   stratification in two diverse US cohorts* (*American Journal of
   Human Genetics*, 2026).** Surfaced by *"All of Us research
   program"* keyword feed. Cites both the initial AoU surveys paper
   (Mapes et al.) and the AoU genomic-data paper (Nature 2024) — so
   confirms AoU as one of the two cohorts. PRS + family-history +
   diverse-ancestry + AoU is the exact intersection of your PRS
   thread and your AoU/UKB/MVP thread. See §3.
4. **Hamed, Naderian, Bangash, Hernandez et al. — *Implementing a
   Multi-Ancestry Polygenic Risk Score for Coronary Heart Disease in
   a Diverse Cohort* (*Genetics in Medicine*, 2026).** Same author
   nucleus as item #3 (Naderian, Hamed); surfaced by *5 new citations
   to articles by Yuan Luo*. Multi-ancestry PRS **implementation** —
   not derivation, not evaluation, but the clinical deployment step —
   in Genetics in Medicine (the eMERGE house journal). See §4.
5. **Wen, Brauer, Choi, Comulada et al. — *Associations between
   discrimination and mental healthcare utilization among racial and
   ethnic minority cancer survivors in the All of Us Research
   Program*.** Surfaced by *Chenjie Zeng — new related research* feed.
   AoU + cancer survivors + disparities is the intersection of your
   cancer-genetic-epi thread and your AoU-EHR-linked-biobank thread.
   See §5.
6. **Chen, Tong, Lu, Duan, Luo, Suchard et al. — *PDA (Privacy-
   Preserving Distributed Algorithms) in action: ten principles for
   high-quality multi-site clinical evidence generation* (*Journal of
   the American Medical Informatics Association*, 2026).** **Double-
   feed saturation** — surfaced by both *Patrick Ryan — new articles*
   AND *George Hripcsak — new articles* (both new-articles feeds, not
   just related-research). This is a **JAMIA principles paper** from
   the OHDSI-Penn-UCSD-Duke federated-EHR axis; ten-principles papers
   are the reference-class artifact for how OHDSI wants people to
   design multi-site studies going forward. See §6.
7. **Nagpal, Gibson — *Pervasive interactions between exposures and
   polygenic risk can inform more effective clinical and behavioral
   interventions* (*Nature Genetics*, 2026).** Surfaced by *10 new
   citations to articles by Yuan Luo*. G×E interactions with PRS —
   directly on your PRS + causal-inference intersection; Nature
   Genetics venue means it's default-cite for the topic. See §7.
8. **Hermanson, Hudson, Plate — *Public Cohort Analysis Identifies
   Thyroglobulin Variants as Hypothyroidism Risk Factors* (*Journal of
   Biological Chemistry*, 2026).** From the NCBI "All of Us" PubMed
   digest — this is a **rare-variant AoU discovery paper** (TG gene,
   hypothyroidism). Even without full text, the venue + AoU +
   Mendelian-endocrine-disease combination lands on your rare-disease
   + AoU-genomics threads. See §8.

### Also on-thread (MEDIUM — log, revisit if a project touches them)

- **Sajal, Song, Brown, Machiela, Kraft et al. — *Integrative analysis
  prioritizes proteins associated with renal cell carcinoma and its
  risk factors* (*JNCI Cancer Spectrum*, 2026)** — surfaced by *APOL1*
  keyword feed. NCI/DCEG author list (Machiela, Kraft, P.J. Brown
  co-authorship). Renal-cell-carcinoma + proteomic + APOL1 lands on
  the tangent between your APOL1/kidney thread and your cancer
  genetic-epi thread — worth a quick read to see if APOL1 is
  substantively featured or just a control locus.
- **Shelley, Shi, Bastarache, Chung, Mosley — *Correction to
  "Polygenic Variation Underlying Neutrophil Counts Modifies the
  Penetrance of Duffy-Null Neutropenia"*** — Bastarache new-articles
  feed. **Correction**, not new work; the original paper is a canonical
  PheWAS-penetrance-of-monogenic reference for your penetrance
  sub-thread. Log the correction; don't re-triage the paper.
- **Liu, Liu, Ge, Zhang, Bai, Li et al. — *Associations of
  accelerometer-derived daily step counts with future health risks: A
  phenome-wide association study among over 60,000 UK adults*
  (*International Journal of ...*, 2026)** — surfaced by both *UK
  Biobank* and *All of Us* keyword feeds (references AoU's earlier
  step-count analysis). Accelerometer-derived PheWAS is a nice
  cross-modal instance of the PheWAS pattern (exposure = wearable
  signal rather than gene) — file under "PheWAS with non-genetic
  exposures".
- **Wang, Lee, Le, Turhan, Hu, Garcia et al. — *A dish-to-biobank
  framework links β-cell nutrient-stress programs to genetic and
  dietary risk for Type 2 Diabetes* (*bioRxiv*, 2026)** — surfaced by
  *Konrad Karczewski — new related research*. Cellular-model-to-
  biobank translation. Off your core threads (T2D + β-cell), but the
  "cellular model informs biobank association" framework is a
  design-pattern worth logging.
- **Yang, Zhao, Zhao, Yang — *Deciphering cell type-specific causal
  genetic effects on brain imaging-derived phenotypes and disorders
  with single-cell Mendelian randomization* (*PLOS ...*, 2026)** —
  surfaced by *Jian Yang — new related research*. Single-cell MR for
  imaging phenotypes is off-thread but adjacent to the causal-
  inference thread; log as a methods reference.
- **Hayeck, Sottolano, Blair, Xenakis et al. — *Likelihood-based
  calibration improves the clinical utility of JAG1 functional data
  for variant classification* (*American Journal of Human Genetics*,
  2026)** — surfaced by the *variant interpretation OR variant
  classification* keyword feed. JAG1 (Alagille) is a well-known
  ClinGen VCEP target; likelihood-based functional-data calibration
  is directly on your variant-interpretation thread. **MEDIUM-HIGH**
  if you touch functional-evidence calibration for ClinGen; MEDIUM
  otherwise.
- **Lewis, D'Angelo, Zhong — *Strengths and Limitations of All of Us
  Data Use for Public Health Research* (*Am J Public Health*, 2026)**
  — from the NCBI AoU digest. Brief editorial (e1–e3), no abstract.
  Worth a 5-minute skim as a citation-for-limitations for future AoU
  papers.
- **Sadowski, Tarver, Burnette et al. — *Advancing data-driven health
  research from the All of Us data training and engagement program*
  (*Journal of the Medical Library Association*, 2026)** — AoU
  training program overview. **LOG only** — not research; useful
  citation for AoU-program-description sections.

### `arxiv-digest` this window (both off-thread)

- **2026-07-17: scVision (Yesiloglu, Mostafa, Zou, Alizadeh, Wu, Xing,
  Adeli, Islam)** — Vision FM for single-cell biology via optimal-
  transport gene layout ("cells as images"). Interesting method but
  single-cell FM is off your threads. Not clinical, not phenotyping.
  **SKIP** (unless a single-cell tangent enters an active project).
- **2026-07-16: Guntoro et al., *Screening of Biosecurity Features in
  Metagenomic Data with Evo 2 Probes*** — Evo 2 linear probes for AMR
  detection in metagenomes. Off-thread (biosecurity metagenomics).
  **SKIP.**

Counts: **8 HIGH**, **7 MEDIUM**, 2 arXiv-digest SKIP. Standout is item
#1 (self-citation in Lancet Respir Med) and the AoU-PRS-CHD paper pair
(items #3 + #4 from overlapping author teams).

---

## HIGH priority — detailed reports

### 1. The role of sweat chloride in determining CFTR protein restoration in people with cystic fibrosis
- **Authors / venue:** E.T. Zemanick, S.Y. Graeber, C. Castellani, G.R. Cutting et al. — *Lancet Respiratory Medicine*, 2026.
- **Surfaced by:** **Quadruple-feed saturation** — (a) **`1 new citation to articles by Chenjie Zeng`** (your own **citations** feed — the highest-signal firing pattern this pipeline produces), (b) *Chenjie Zeng — new related research*, (c) *10 new citations to articles by Joshua C. Denny*, (d) *"Cystic fibrosis carriers" — new results* keyword feed. Four independent surfacings for one paper, one of them being your citations feed, is the strongest signal in a month.
- **Thread:** **CF disease-thread** (your Vanderbilt-era CF carrier PheWAS/PheRS work) **+** **PheWAS / phecode infrastructure** (this is a CFTR-genotype-to-clinical-endpoint calibration paper, directly parallel to the CF-PheWAS design you contributed to) **+** **variant interpretation / functional data** (sweat chloride as functional readout for CFTR-modulator response).
- **What it is:** *Lancet Respir Med*-tier consensus/analytic paper on how sweat chloride tracks CFTR protein restoration under modulator therapy (ivacaftor/lumacaftor/tezacaftor/elexacaftor). Zemanick and Castellani are the CF Foundation registry / European CF Society outcome-standardization leadership; Cutting is the Johns Hopkins CFTR-variant reference lab (CFTR2). The paper almost certainly reframes sweat chloride from a diagnostic biomarker into a **quantitative pharmacodynamic marker of CFTR protein rescue** — with implications for genotype-specific dosing and for clinical-trial endpoint definitions in modulator combinations for rare CFTR variants.
- **Why it cites you (best guess):** The Denny/Zeng CF carrier PheWAS lineage established the CFTR heterozygous phenotype spectrum in EHR-linked biobanks — a natural citation for any Lancet Respir Med paper reframing sweat-chloride-as-CFTR-function readout, because the CF-carrier phenotype spectrum contextualizes what "residual CFTR function" looks like clinically. Alternatively, they may cite your work on quantifying CFTR heterozygote-phenotype associations in AoU/BioVU. Either way, **you should confirm which paper of yours is cited and in what context** — this is the sort of citation that changes how you frame the impact section of the next CFTR-related grant/paper.
- **Why it matters to you:** Four reasons.
  (a) **A Lancet Respir Med citation** — top-tier respiratory journal, high impact factor, will drive downstream visibility of the cited paper. Worth a note in your h-index / citation-tracking file and worth flagging to any co-authors.
  (b) **Confirms your CF work is being read by the clinical CF community** (Zemanick, Castellani, Cutting are clinical-CF-registry lineage, not human genetics) — different citation-community than most of your work.
  (c) **The paper may open a collaboration angle.** Cutting's CFTR2 lab is the definitive functional-variant reference; if the paper cites your CF-carrier or CFTR-heterozygote work, the reverse citation direction may become natural for your next paper.
  (d) **Denny-citations feed also fired**, meaning this same paper is likely citing one or more Denny lab CF/CFTR papers — worth noting the co-citation, because Lancet Respir Med papers citing both you and Denny in the same reference list signal a clean "Vanderbilt CF-EHR lineage" grouping in the reviewer's mind.
- **Action:** **HIGH — read within 48 hours.**
  (i) Pull the full text of the *Lancet Respir Med* paper, locate the citation to your work in the reference list, and read the surrounding paragraph in context (this is the highest-value step — takes 15 minutes).
  (ii) Note which of your papers is cited and update your annotated CV / citation-context file if you keep one.
  (iii) Cross-check whether any of the co-authors overlap with the Denny lab — if so, this may already be a friendly citation from a known collaborator rather than a cold citation from a new community. Adjust the outreach question accordingly.
  (iv) If the paper reframes sweat chloride as a quantitative pharmacodynamic marker, note the design pattern for future CFTR-heterozygote work — a *quantitative* per-variant CFTR-function readout is the reciprocal of what your PheWAS work does (quantitative per-variant phenotype readout).
  (v) Consider whether a short LinkedIn / Twitter mention is warranted for visibility (personal call).

### 2. Domain-aware matrix completion for phenotype imputation using electronic health record data with applications in genomic research
- **Authors / venue:** H. Wu, C.H. Lee, N. Abiri, I. Ionita-Laza — *The Annals of Applied Statistics*, 2026.
- **Surfaced by:** *Lisa Bastarache — new related research* feed. Bastarache's related-research feed is the single most reliable signal for on-thread PheWAS/phecode-methods papers this pipeline surfaces.
- **Thread:** **PheWAS / phecode infrastructure** (phenotype imputation is the missing methodological piece for rare-phecode PheWAS) **+** **EHR phenotyping** (matrix completion over patient × phecode matrices is a phenotyping primitive) **+** **statistical methods for EHR-linked biobank analysis** (AoAS venue = methods paper, not an application paper).
- **What it is:** Ionita-Laza (Columbia biostats) is a leading statistical geneticist — her group has authored several reference methods papers on rare-variant analysis and heritability estimation. This paper introduces a **domain-aware matrix-completion approach for imputing missing phenotypes** in the patient × phecode (or patient × diagnosis-code) matrix, with an application to genomic research (almost certainly a downstream PheWAS or PRS-phecode analysis where phecode sparsity limits power). "Domain-aware" implies the completion incorporates *phecode ontology structure* (parent-child phecode relationships), *clinical co-occurrence patterns*, or *demographic priors* — rather than treating the matrix as generic low-rank.
- **Why it matters to you:** Four reasons.
  (a) **Rare-phecode PheWAS is fundamentally power-limited by sparsity.** Any phecode with prevalence < 0.5% in a biobank has too few cases for a well-powered per-phecode PRS or per-phecode variant association. Imputing missing phecodes (or missing structured labels more broadly) would substantially improve power in the long tail of the phecode distribution — which is where your monogenic-variant-penetrance work operates.
  (b) **AoAS is a methods journal.** This will be a reference methods paper cited in future PheWAS methodology reviews. Reading it now means you know the technique before it becomes standard.
  (c) **Bastarache surfacing the paper is signal that phecode/EHR-phenotyping community sees this as adjacent to their work** — likely to be adopted rapidly if the method works.
  (d) **Pairs with existing sub-threads** — this is the same problem PheValuator addresses from the validation side (Swerdel et al.) and that KOMAP addresses from the semi-supervised side (Hong et al.); a rigorous matrix-completion perspective is the third leg of that stool.
- **Action:** **HIGH.**
  (i) Read for the ontology / domain-prior structure — is it phecode hierarchy? SNOMED-CT? A learned embedding? The prior structure is the innovation.
  (ii) Check the "applications in genomic research" section: what phenotype / cohort / genotype / outcome? If it uses AoU or UKB, the empirical demonstration is directly transferable.
  (iii) Note downstream statistical guarantees — most matrix-completion methods lack calibrated uncertainty estimates for downstream inference, which is critical for PheWAS FDR/Bonferroni control. If the paper provides calibrated imputation intervals, that's the key contribution.
  (iv) Consider whether the method is applicable to your rare-monogenic-penetrance work — if you have a monogenic variant with 30 cases across AoU + UKB, could you use this imputation to expand the case set 3-5× before PheWAS?

### 3. Additive value of polygenic risk and family history for coronary heart disease risk stratification in two diverse US cohorts
- **Authors / venue:** M. Naderian, J.L. Smith, O. Dikilitas, M.E. Hamed et al. — *The American Journal of Human Genetics*, 2026.
- **Surfaced by:** *"All of Us research program"* keyword feed (and adjacent Yuan Luo citation feed). The Scholar snippet explicitly cites both the Mapes AoU-surveys paper (Epidemiology, 2019) and the AoU-genomic-data paper (Nature 2024, 627:340–346) — confirming AoU is one of the two "diverse US cohorts".
- **Thread:** **PRS / genetic epi** (additive PRS + non-genetic risk factor) **+** **AoU / diverse-cohort thread** **+** **causal inference / risk stratification** (the "additive value" framing is a *marginal information* question — how much does PRS add over family history?).
- **What it is:** Naderian, Dikilitas, and Hamed are the Mayo Clinic / eMERGE-Mayo axis (Dikilitas is at Mayo; Naderian and Hamed are at Mayo or eMERGE-linked institutions). AJHG venue means this is a rigorous methodological demonstration, not a translational implementation paper. The "two diverse US cohorts" framing is almost certainly AoU + one of {MVP, eMERGE, MyCode, or Mayo Biobank} — likely MVP given the diverse-cohort framing. The paper evaluates whether adding a CHD PRS to family-history-based CHD risk stratification improves discrimination / net reclassification — a decision-grade PRS evaluation.
- **Why it matters to you:** Four reasons.
  (a) **Additive-information framing is the correct decision-grade PRS question.** Not "does PRS predict CHD?" (it does, everyone knows) — but "does PRS add anything on top of family history and standard clinical factors?" This is the framing that any PRS clinical-implementation paper (yours or others') needs to address.
  (b) **AoU + diverse-cohort is your core cohort infrastructure.** Whatever methodological approach they use for PRS-across-ancestry in AoU will be a default reference for your future AoU PRS work.
  (c) **Pairs with item #4 in this report.** Naderian and Hamed appear on both papers; item #3 is the AJHG methods paper, item #4 (Genetics in Medicine) is the clinical-implementation companion. Reading both together gives you the full pipeline from method to implementation.
  (d) **Family-history baseline is understudied.** Most PRS-additivity papers baseline against Framingham risk score or PCE, not family history. Family-history is a *cheap* clinical variable — if PRS beats FH in a diverse cohort, that's a much stronger clinical utility argument than "PRS beats PCE".
- **Action:** **HIGH.**
  (i) Read the discrimination and net-reclassification tables (NRI, IDI, decision-curve analysis). NRI for the high-risk-tail slice is the key number.
  (ii) Note which two cohorts — confirm AoU + MVP hypothesis or update.
  (iii) Check the ancestry-stratified PRS performance — cross-ancestry PRS calibration is a first-order concern for any diverse-cohort PRS paper.
  (iv) Note the PRS source — de novo? Ported? PRS-CSx / PRScs-multi? — because your own PRS work needs to reference this paper's methodology in future submissions.

### 4. Implementing a Multi-Ancestry Polygenic Risk Score for Coronary Heart Disease in a Diverse Cohort
- **Authors / venue:** M. Hamed, M. Naderian, H. Bangash, V. Hernandez et al. — *Genetics in Medicine*, 2026.
- **Surfaced by:** *5 new citations to articles by Yuan Luo* feed.
- **Thread:** **PRS / genetic epi** (multi-ancestry PRS) **+** **AoU / diverse-cohort thread** **+** **implementation science / clinical translation** (the *implementation* framing rather than *derivation* or *evaluation*).
- **What it is:** Companion / follow-on to item #3 (same author nucleus: Naderian, Hamed, and — new here — Bangash and Hernandez). *Genetics in Medicine* is the eMERGE-house / ACMG-adjacent clinical-translation journal. The word "Implementing" in the title is the tell — this is the **operationalization step** for a multi-ancestry CHD PRS: how it enters a clinical workflow, what the return-of-results looks like, what the decision-support integration is, what the ancestry-inference pipeline is at the point of clinical delivery.
- **Why it matters to you:** Three reasons.
  (a) **The AoU / MVP / eMERGE community is moving from PRS *derivation* to PRS *implementation*.** Papers like this are the emerging reference class for how PRS actually gets delivered in a diverse healthcare setting; you will need to cite them in any translational-framing section of future work.
  (b) **Multi-ancestry PRS implementation is a hard operational problem** — ancestry inference at the point-of-care is nontrivial (self-report vs genetic PC-inferred; continuous vs discrete; how to handle admixed individuals). Whatever approach they take will be a reference for any AoU-based clinical-PRS work.
  (c) **Genetics in Medicine venue** signals ACMG-community consumption — the audience of clinical geneticists who make return-of-results decisions.
- **Action:** **HIGH.**
  (i) Read pairing with item #3 as a two-paper block (method + implementation).
  (ii) Note the ancestry-inference pipeline used — discrete-superpopulation? Continuous PC-based? PRS-CSx-multi? — because this pattern will get copied.
  (iii) Check for return-of-results / patient-facing components — most PRS-implementation papers hand-wave this; concrete descriptions are rare and valuable.
  (iv) Note the diverse cohort identity — if AoU, this is potentially adjacent to your work; if UKB or MVP alone, less so.

### 5. Associations between discrimination and mental healthcare utilization among racial and ethnic minority cancer survivors in the All of Us Research Program
- **Authors / venue:** Y.P. Wen, E.R. Brauer, S. Choi, W.S. Comulada et al. — journal not specified in Scholar snippet.
- **Surfaced by:** *Chenjie Zeng — new related research* feed. Your related-research feed fires when Google's model judges paper close to your published work — meaning the paper is close to your cancer-survivorship / cancer-EHR / AoU-cancer methodology.
- **Thread:** **Cancer genetic epi / survivorship** (survivorship-outcomes-in-diverse-cohort) **+** **AoU-EHR-linked-biobank** (AoU as the sole data source) **+** disparities / mental-health-utilization.
- **What it is:** Wen and Comulada are UCLA-based (Comulada is UCLA CHIPTS-adjacent); Brauer is a UCLA School of Nursing psycho-oncology researcher. AoU + cancer survivors + discrimination measures (AoU has a discrimination-experience survey module) + mental-healthcare utilization (SUD, MH visits from EHR). The design is almost certainly cross-sectional survey-linked-to-EHR: discrimination score from AoU survey → mental-healthcare use from EHR → stratified by cancer-survivor status and race/ethnicity.
- **Why it matters to you:** Three reasons.
  (a) **AoU cancer-survivor cohort construction is exactly your methodological territory.** Whatever phecode / cancer-case-definition they use for the AoU cancer-survivor identification is directly comparable to your AoU cancer methodology (and possibly cites it).
  (b) **Discrimination-survey linkage to EHR is the AoU sociotechnical superpower.** Very few cohorts have both social-determinants surveys and EHR follow-up; this is the exact use case AoU was designed for. The paper is a demonstration of how to exploit that.
  (c) **Reviewer angle.** If you're reviewing an AoU-based paper on cancer survivorship in the next 6 months, this will be a natural citation to check against.
- **Action:** **HIGH-MEDIUM.**
  (i) Read specifically the AoU cancer-case-definition (which phecodes / concept IDs / self-report items are the case defintion?) — a comparison point for your work.
  (ii) Note the discrimination-scale source (EDS? PEDQ-CV? AoU-specific instrument?) — the choice is field-relevant.
  (iii) File under "AoU cancer-survivor methodology reference".
  (iv) Not a required-read; log-and-skim rather than deep-read unless a project touches survivorship-outcomes in AoU.

### 6. PDA (Privacy-Preserving Distributed Algorithms) in action: ten principles for high-quality multi-site clinical evidence generation
- **Authors / venue:** Y. Chen, J. Tong, Y. Lu, R. Duan, C. Luo, M.A. Suchard et al. — *Journal of the American Medical Informatics Association* (JAMIA), 2026.
- **Surfaced by:** **Double new-articles-feed saturation** — (a) *Patrick Ryan — new articles*, (b) *George Hripcsak — new articles*. **Both are new-articles feeds** (not related-research feeds), meaning both Ryan and Hripcsak are on the author list. This is a stronger signal than any related-research firing — both principal investigators of the OHDSI / OMOP / Penn-Columbia federated-EHR axis co-authored.
- **Thread:** **EHR phenotyping / OMOP** (federated-EHR is the OHDSI operating context) **+** **causal inference / pharmacoepi** (multi-site evidence generation is the target trial emulation setting) **+** **EHR-linked biobank infrastructure** (multi-site principles apply to AoU + MVP + N3C + PEDSnet + OneFlorida).
- **What it is:** A **JAMIA principles paper** codifying ten principles for privacy-preserving distributed learning over multi-site EHR data. The author list (Chen, Tong, Lu, Duan, Luo, Suchard, plus Ryan and Hripcsak) is the OHDSI-Penn-UCLA-Duke federated-methods axis — same author nucleus that published the PDA method papers 2019–2024. This is the community consensus paper on what "good" distributed-EHR study design looks like: privacy budget, homogeneity vs heterogeneity assumptions, gold-standard subset for local validation, negative-control outcomes, etc.
- **Why it matters to you:** Three reasons.
  (a) **Ten-principles papers become de facto review checklists.** If you review a multi-site EHR paper in the next year, JAMIA reviewers are already going to check it against these ten principles. Reading the paper now means you know the reviewer's checklist before the review.
  (b) **Pairs with your causal-inference / target-trial-emulation thread.** Target trial emulation across sites is a distributed-causal-inference problem; the PDA framework is the operational answer.
  (c) **Directly relevant to AoU + MVP + UKB federated work.** As you contemplate any cross-biobank analysis, these ten principles are the design constraints.
- **Action:** **HIGH.**
  (i) Read the ten principles as a checklist and note which are novel vs. established consensus.
  (ii) Cross-check against the AoU data-access constraints — several principles are almost certainly operationalizations of what AoU already forbids (raw data export).
  (iii) File as a reviewer-checklist reference for any future multi-site EHR review you get.
  (iv) Note the empirical demonstration cohort (N3C? OneFlorida? PEDSnet?) — a real-data demo strengthens the paper's transferability claim.

### 7. Pervasive interactions between exposures and polygenic risk can inform more effective clinical and behavioral interventions
- **Authors / venue:** S. Nagpal, G. Gibson — *Nature Genetics*, 2026.
- **Surfaced by:** *10 new citations to articles by Yuan Luo* feed.
- **Thread:** **PRS / genetic epi** (G×E) **+** **causal inference / intervention** (the paper's framing bridges G×E to intervention design — a causal-inference framing rather than a pure discovery framing) **+** **behavioral / precision-medicine intervention** (which loops back to your risk-stratification and clinical-implementation threads).
- **What it is:** Nagpal + Gibson (Georgia Tech) — Gibson's lab is one of the reference labs for PRS-generalizability and G×E interaction. *Nature Genetics* perspective/analysis paper on how G×E interactions can inform intervention targeting. The framing is decision-theoretic: if PRS × exposure interaction is real and pervasive, then intervention effectiveness varies by PRS stratum, which changes optimal intervention allocation.
- **Why it matters to you:** Three reasons.
  (a) **G×E in PRS is the missing piece for actionable PRS.** PRS alone doesn't tell you what intervention to give; PRS × modifiable-exposure interaction does. Nagpal + Gibson framing this in Nature Genetics with the intervention lens is a *default citation* for any future PRS-implementation paper you write.
  (b) **Pairs with items #3 + #4 in this report.** Items #3 and #4 are CHD-PRS implementation papers; #7 is the theoretical scaffolding for why PRS+exposure interaction matters for implementation.
  (c) **Bridges to your causal-inference thread.** G×E-for-intervention is a heterogeneous-treatment-effect problem — same statistical class as causal-forest / meta-learners for treatment-effect heterogeneity.
- **Action:** **HIGH.**
  (i) Read for the empirical-vs-theoretical balance: how much is proof-of-concept G×E discovery vs how much is intervention-design framework?
  (ii) Note the exposure classes analyzed (behavioral? environmental? both?) — behavioral exposures are the actionable ones.
  (iii) Cite in any future PRS-implementation paper as the theoretical scaffolding for the "why does this matter" section.

### 8. Public Cohort Analysis Identifies Thyroglobulin Variants as Hypothyroidism Risk Factors
- **Authors / venue:** J.N. Hermanson, A.D. Hudson, L. Plate — *Journal of Biological Chemistry*, 2026.
- **Surfaced by:** NCBI "What's new for 'All of Us' in PubMed" digest (07-17 batch).
- **Thread:** **AoU-genomics** (AoU as the public cohort) **+** **rare / low-frequency variant analysis** (TG gene, hypothyroidism) **+** **variant interpretation** (functional characterization angle if from a Plate/Hudson biochemistry lab).
- **What it is:** Plate (Vanderbilt Biochemistry — same institution as your training lineage) leads a biochemistry group focused on proteostasis; the "public cohort analysis" framing implies AoU is used as the discovery cohort to identify TG (thyroglobulin) variants associated with hypothyroidism, likely followed by biochemical / cell-biology characterization of variant effects. This is the two-shot design pattern of **AoU-discovery + wet-lab-functional-follow-up**, which is one of the reference designs the AoU program was created to enable.
- **Why it matters to you:** Four reasons.
  (a) **Design pattern is exactly what AoU is for.** Using AoU as the discovery cohort for rare-disease-gene variants + biochemical follow-up is the design pattern you'll cite in future AoU rare-disease grant/paper framings.
  (b) **Vanderbilt biochem lab using AoU** — Plate is at Vanderbilt, so this is likely on your institutional network. Worth being aware of who else at Vanderbilt uses AoU for rare-disease discovery.
  (c) **Thyroglobulin / hypothyroidism is a common-disease-with-monogenic-tail setting** — same conceptual class as CFTR-mediated CF vs. CFTR-heterozygote phenotype spectrum. The methodology likely echoes what you'd use for a CFTR or BRCA variant-tail analysis.
  (d) **JBC venue** signals biochemistry-community consumption — not the same audience as your PheWAS work, but the AoU-genomics community will cite this as a reference example.
- **Action:** **HIGH-MEDIUM.**
  (i) Read the AoU cohort-construction methodology (which release? which ancestry set? which variant-calling pipeline? WGS or ACAF?). This tells you which AoU-release the discovery is against.
  (ii) Note the variant classification approach — is it ACMG/AMP or purely biochemistry-informed?
  (iii) File under "AoU rare-variant discovery + wet-lab follow-up examples" for future grant framing.
  (iv) Consider a brief note to Plate if you're at Vanderbilt / adjacent — this is exactly the sort of intra-institutional AoU collaboration angle worth being aware of.

---

## Pipeline recommendations (unchanged, stated once)

The recurring pattern from the last seven reports holds: **`arxiv-digest`
misses ~100% of on-thread signal**. Two papers surfaced this window, both
single-keyword `foundation model` incidental hits, both off-thread.

Concrete fixes (deliberately unchanged from prior reports):

1. **Add `cs.LG` and `stat.ME`** to the tracked categories — most
   phenotype-imputation / causal-ML / EHR-FM methods papers are cross-
   listed there and get missed.
2. **Add a medRxiv / bioRxiv feed** — item #7 (Nagpal Gibson) and item
   #4 (Hamed) would have been surfaced pre-publication.
3. **Fix single-word keyword boundaries** for `mendelian`, `knowledge
   graph`, `drug repurposing` — several near-miss hits were caught by
   the Scholar keyword feed only.
4. **Consider PubMed as a source** rather than a parallel channel —
   the NCBI What's-New digests are already producing better on-thread
   signal than `arxiv-digest` and are essentially free to parse.

Items 1–3 have been open across 8 reports; item 4 is new here based on
the observation that the NCBI PubMed What's-New digests captured item #8
(AoU-TG hypothyroidism) which no other source surfaced.

---

_Report generated 2026-07-18._
