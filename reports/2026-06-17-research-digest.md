# Research digest report — 2026-06-17

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-13 → 2026-06-17** (since the prior 2026-06-13 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-13 → 06-17 | Three batches: 06-15 03:27Z (APOL1, Gharavi), 06-16 07:23Z (large multi-author batch — Bastarache, Karczewski, Denny, Hripcsak, Chute, Kastner, Rehm, Pritchard, Yang, Karczewski, Brandt, Shah, Szolovits, Celi, Patrick Ryan, etc.), 06-17 06:02Z (keyword batch — UK Biobank, AoU, drug repurposing, EHR, variant interpretation, KG, mendelian, rare diseases, FM+EHR). |
| `arxiv-digest` repo (`digests/`) | 2026-06-13 → 06-17 | **5 daily files; 1 non-empty.** 06-13/14/15/17 empty; 06-16 = 2 papers (Fesser/Zitnik on post-training of biological reasoning models; hyreg2 latent-class R package). |
| NCBI "My NCBI What's New" (AoU, UK Biobank) | daily | Aggregate PubMed digests; not individually triaged here. |
| bioRxiv / medRxiv subject alerts | daily | Aggregate collection digests; not individually triaged here. |

> ⚠️ **`arxiv-digest` is essentially dry this window** — 4 of 5 days
> empty, only 06-16 produced anything (2 papers), and one of those is
> a single-keyword latent-class hit on an R package rather than a
> substantive methods paper. Virtually 100% of the on-thread signal
> this window came from Scholar alerts surfacing medRxiv / journal
> articles. Pipeline recommendation from the previous three reports
> stands: **add `cs.LG`, `stat.ME`, and a medRxiv/bioRxiv feed** —
> without those, items #1, #3, #4, #10, #11, #12 below (all the
> highest-priority hits) would never have been surfaced.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below
> contextualize that metadata against your research threads; nothing
> here reflects full-text reading.

---

## Executive summary

- **Penetrance from biobanks (newborn-screening framing) is the
  strongest single signal this window.** Gold et al. (medRxiv,
  Bastarache + Karczewski feeds) estimate *long-term penetrance* of
  P/LP variants in the genomic-newborn-screening (gNBS) gene panel
  using adult biobanks as a proxy for "what would gNBS catch over a
  lifetime?" — this is exactly the population-vs-clinical penetrance
  shape your INTERESTS file is built around, and continues the
  Ramchand AIRE / Marston SGLT2i × cardiomyopathy-carrier pattern from
  the previous two reports. **Three weeks running we have a top-tier
  penetrance-in-population-screening paper at the head of the report.**
- **All of Us as an equitable-PRS engine.** Kang et al. (Statistics in
  Biosciences) is a tutorial-style end-to-end AoU PRS workflow with
  RA as the case study — and it cites work from your group, so it
  surfaces both in the Bastarache citations feed and in your own
  *Chenjie Zeng new citation* feed. Practical AoU operational pattern
  that's worth lifting wholesale into any AoU PRS pipeline you build.
- **EHR phenotyping × LLMs continues to consolidate.** Molina et al.
  (Annals of Emergency Medicine) is a head-to-head comparison of a
  *computable structured phenotype* vs an LLM for opioid-use-disorder
  identification on EHR data — surfaced *twice* (Hripcsak +
  Pascal Brandt feeds), the strongest two-alert saturation pattern
  this window. The LLM-vs-rules comparison on a stigmatized,
  under-coded condition is exactly the format that should anchor your
  computable-phenotype write-ups.
- **IBD × proteomic-PRS** is the second proteome-MR/proteomic-PRS
  paper in two weeks: Turchin et al. (medRxiv, Denny feed) build a
  *proteomic* polygenic score for IL-18 to identify a mechanistically-
  defined IBD subgroup — directly on your IBD disease thread, and
  also a clean instance of the proteome-PRS pattern (next to last
  week's Gobeil MASLD proteogenomic paper).
- **APOL1 and VEXAS disease threads both have new items.** Zahr et al.
  (Pediatric Nephrology) is a pediatric APOL1/CKD cohort study from
  the BIG Initiative — pairs with the Varner pediatric review from
  the last report. Patel et al. (Blood Advances) is a focused review
  of *MDS in VEXAS* — bridges your CHIP/VEXAS thread (somatic
  mosaicism + hematologic outcomes) at the highest-overlap point.
- **Variant-interpretation guidance refreshed twice in one window.**
  Mighton et al. (ACMG VUS-reporting *points to consider* statement,
  Heidi Rehm feed) and Guha et al. (ACMG *repeat-expansion NGS*
  detection statement, Stephen Montgomery feed) both land as
  ACMG/ClinGen guidance updates — high citation-weight reference
  documents for any variant-interpretation work you do.
- **Multimorbidity gets two genetic/proteomic anchors.** Hukerikar
  et al. (Science Advances) is a *Mendelian randomization across the
  immunoproteome × multiple diseases* — shared-mechanism framing for
  multimorbidity that pairs naturally with the Lim et al. Lancet
  cardiometabolic-MLTC mechanistic review from the last report.
  Uosukainen et al. extend PFAPA into a long-term comorbidity case-
  control study (Kastner feed) — autoinflammatory multimorbidity.
- **Two PRS-clinical-implementation items.** Hagenbeek et al.
  (Communications Medicine) on PRS+SES across 19 diseases and de La
  Harpe et al. (medRxiv) on *patient-level* PRS robustness for ASCVD
  — both feed the precision-health translation thread.
- **arxiv-digest contributions are thin but include one notable
  item:** Fesser et al. on post-training of biological reasoning
  models (cs.LG, 06-16, Zitnik group) is a controlled study of
  CPT/SFT/RL trade-offs in *biological* FMs — interesting METHODS-
  WATCH for your EHR-FM lineage even though it's not directly on the
  CLMBR/MOTOR axis. The hyreg2 R package (stat.ME, 06-16) is a clean
  but narrow latent-class implementation — borderline; logged.
- **No strong drug-repurposing items this window** — the
  "drug repurposing" keyword surfaced a benfotiamine
  P2Y14R-antagonist molecular-dynamics study (Wang et al.), which is
  target-only without an EHR/KG-with-explainability angle. SKIP per
  INTERESTS filtering. Drug-repurposing has now been dry for two
  consecutive windows.

Counts: **13 HIGH**, **7 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. Long-term Penetrance of Disease Variants in Genes Prioritized for Genomic Newborn Screening: Evidence from Adult Biobanks
- **Authors / venue:** N.B. Gold, H. Zouk, J. Yeo, S. Lipsitz, S. Koyama et al. — *medRxiv*, 2026.
- **Surfaced by:** Lisa Bastarache *new related research* alert (06-16) **+** Konrad Karczewski *new related research* alert (06-16) — i.e., two independent author-related-research surfaces.
- **Thread:** PheWAS/PheRS → **penetrance estimation under population-
  screening conditions** (vs clinically ascertained cohorts) **+** EHR-
  linked biobanks **+** rare disease / variant interpretation.
- **What it is:** Uses *adult* biobanks (likely UKB / MGB-style) as a
  long-window proxy to estimate penetrance for the gene set
  prioritized for **genomic newborn screening (gNBS)**. Abstract framing:
  "gNBS is a potential public health intervention, but its positive
  predictive value (PPV) remains uncertain. Estimating the prevalence
  and penetrance of pathogenic and likely pathogenic (P/LP) variants
  in [those genes] …" Reuses the standard adult-biobank trick of
  re-estimating penetrance in an unascertained population.
- **Why it matters to you:** Three converging hits.
  (a) Penetrance-in-population-screening is the explicit named
  example in your INTERESTS file under PheWAS/PheRS. (b) The gNBS
  framing makes this a *public-health-decision* PPV calculation, not
  just a methodological exercise — exactly the kind of write-up your
  composite-risk modeling work needs as citation scaffolding when
  arguing for or against deploying a variant-based screen at the
  population level. (c) Two-author-feed surfacing (Bastarache +
  Karczewski) confirms this is on the field's central radar.
- **Action:** **HIGH** — read for (i) the gene panel composition
  (which gNBS lists they use: BabySeq, NBSeq, BeginNGS), (ii) the
  biobank ascertainment and the penetrance estimator (Kaplan-Meier
  to lifetime endpoint vs cross-sectional prevalence), and (iii) how
  they propagate uncertainty into PPV. This will be a default citation
  for any monogenic-variant-screening write-up over the next 12
  months.

### 2. Harness All of Us for Equitable Disease Risk Prediction: A Tutorial with Case Study on Genetic Prediction Score for Rheumatoid Arthritis
- **Authors / venue:** Z. Kang, Y. Feng, C. Chen, Y. Hou, H. Yang et al. — *Statistics in Biosciences*, 2026.
- **Surfaced by:** Lisa Bastarache *new citations* alert (06-16) **+** Chenjie Zeng *new citations* alert (06-16) — i.e., **cites your work**.
- **Thread:** EHR-linked biobanks (**All of Us**) **+** genetic
  epidemiology (PRS) **+** cross-ancestry portability **+** ML for
  precision health (operational tutorial).
- **What it is:** A practical, transparent, reproducible workflow for
  AoU PRS analysis, instantiated on rheumatoid arthritis. Modules
  cover (1) AoU study design, presumably (2) cohort/phenotype
  construction, (3) genotype QC, (4) PRS scoring + portability across
  ancestries, (5) validation. The framing — "enriched recruitment of
  populations underrepresented in biomedical research … rich resource
  for equitable health research … complexity of the AoU platform is
  a common hurdle" — is operational tutorial, not novel methods.
- **Why it matters to you:** Three angles. (a) Self-citation: surfaces
  in your own Chenjie Zeng citations feed, indicating it cites work
  you've authored, likely your phenomic-AoU comparison paper. (b) AoU
  PRS workflow is on three of your active threads at once (AoU, PRS,
  cross-ancestry portability). (c) Tutorial format means it's
  immediately useful as a *template* — drop in a different outcome or
  PRS source and re-run. RA as the case-study disease is on the
  autoimmune cluster, which is adjacent to your IBD thread.
- **Action:** **HIGH** — skim for the *operational* pieces: the AoU
  cohort definition (which concept sets and exclusion criteria they
  use), the PRS construction choice (PRS-CS, LDpred2, or external
  weights), and the cross-ancestry calibration / decision-curve step
  if any. Worth a quick read even just to align your future AoU PRS
  pipelines with what's becoming the community-accepted pattern.

### 3. Computable Structured Phenotype Versus Large Language Model Identification of Opioid Use Disorder Using Electronic Health Record Data
- **Authors / venue:** M.F. Molina, C. Fenton, K.T. LeSaint, S.D. Pimentel et al. — *Annals of Emergency Medicine*, 2026.
- **Surfaced by:** George Hripcsak *new related research* alert
  (06-16) **+** Pascal Brandt *new related research* alert (06-16) —
  the strongest two-alert saturation in this window.
- **Thread:** EHR phenotyping (**computable phenotype vs LLM**) **+**
  causal inference / pharmacoepi (substance-use cohort identification)
  **+** LLM-assisted phenotyping.
- **What it is:** A head-to-head benchmark — *rules-based / structured
  computable phenotype* vs *LLM extraction from clinical text* — for
  identifying patients with opioid use disorder (OUD) in EHR. OUD is
  systematically under-coded (stigma, billing patterns, evolving
  DSM/ICD coding), which is exactly the phenotype shape where LLM
  extraction is expected to beat rules-based by a wide margin. Annals
  of Emergency Medicine venue suggests the comparison is grounded in
  ED encounter data, where OUD ascertainment is operationally
  critical.
- **Why it matters to you:** Hits the computable-phenotype thread at
  its most actionable point — the comparison format ("LLM vs
  structured phenotype on a known under-coded condition") is exactly
  the experimental design you'd want to mirror for any LLM-augmented
  phenotyping work, including the AoU note-extraction direction
  several of last week's reports flagged. Two-feed saturation
  (Hripcsak's group is OHDSI/computable-phenotype-native; Brandt is
  PheKB/EHR-phenotyping) signals it'll be a default citation for the
  LLM-vs-rules debate.
- **Action:** **HIGH** — read for (i) the LLM choice and prompting
  pattern (zero-shot vs fine-tuned vs RAG), (ii) the gold standard
  (chart review? referral to OUD treatment?), and (iii) error
  decomposition — false positives from incidental opioid prescriptions
  vs false negatives from euphemistic chart language. Whichever
  direction the LLM wins, the *failure-mode taxonomy* will be useful.

### 4. A proteomic polygenic score to identify IL-18 driven inflammatory bowel disease
- **Authors / venue:** M.C. Turchin, N. Raghupathy, C.L. Carty, M. Morris et al. — *medRxiv*, 2026.
- **Surfaced by:** Joshua C. Denny *new related research* alert (06-16).
- **Thread:** Genetic epidemiology (**proteomic PRS**) **+**
  inflammatory bowel disease (IBD) disease thread **+** drug-target
  prioritization.
- **What it is:** Builds a *proteomic* polygenic score for IL-18 —
  i.e., a PRS that predicts circulating IL-18 levels rather than IBD
  directly — and uses it to identify a mechanistically-defined IBD
  subgroup ("IL-18-driven IBD"). Abstract framing: "High levels of
  IL-18 have been causally implicated in IBD risk and may represent a
  unique mechanism driving IBD yet to be therapeutically targeted. To
  identify individuals predisposed to increased levels of IL-18, we
  implemented a polygenic [score …]"
- **Why it matters to you:** Two-way hit. (a) IBD is an active
  disease thread. (b) The proteomic-PRS pattern is methodologically
  important: it's a way to stratify a polygenic disease into
  *cytokine-defined subtypes* without having to measure the protein
  in every patient. Pairs naturally with last week's Gobeil
  proteogenomic-MASLD paper as the second proteome-PRS-style item in
  the same trans-window; together they suggest this is a budding
  *PRS-on-pQTLs* sub-pattern worth its own keyword.
- **Action:** **HIGH** — read for (i) the IL-18 pQTL source (UKB-
  PPP, deCODE, or Olink Explore?), (ii) the IBD-stratification
  endpoint (does the IL-18-PRS-high subgroup respond differently to
  IL-23 / TNF blockade?), and (iii) whether they evaluate the score
  in a treatment-effect-heterogeneity framing — that would tie it
  back to your causal-ML thread.

### 5. APOL1 and chronic kidney disease in pediatrics: a study from the Biorepository and Integrative Genomics Initiative
- **Authors / venue:** R.S. Zahr, L. Chinthala, A. Mohammed, C.P. Kovesdy et al. — *Pediatric Nephrology*, 2026.
- **Surfaced by:** "APOL1" keyword alert (06-15).
- **Thread:** APOL1 disease thread (pediatric extension, biobank-
  linked).
- **What it is:** A pediatric APOL1 / CKD cohort study from the
  **BIG Initiative** (Biorepository and Integrative Genomics, at
  UTHSC/Le Bonheur). One of the few APOL1 cohorts purpose-built
  around pediatric ascertainment; complements the Varner pediatric
  review item from the last report by providing a *data-side* anchor
  to that review's clinical synthesis.
- **Why it matters to you:** Your INTERESTS file calls out APOL1 as
  "kidney disease risk, transplant decision-making, ancestry
  considerations" — the pediatric axis (early-onset progression,
  family-history-driven testing) is increasingly relevant to the
  transplant-decision conversation because pediatric APOL1 carriers
  feed the donor pool in adulthood. Two pediatric APOL1 hits in two
  weeks (Varner review last report, this empirical study this
  report) suggests the pediatric line is consolidating into its own
  sub-thread.
- **Action:** **HIGH** — read for the recruitment pattern (referral
  vs general pediatric biobank), the BIG genotyping platform
  (presumably PMRA-based), the CKD ascertainment (eGFR cutoff,
  proteinuria), and any reporting of family-history clustering.

### 6. Myelodysplastic Syndromes in VEXAS
- **Authors / venue:** B.A. Patel, K.R. Calvo, K.K. Reichard,
  M.M. Patnaik — *Blood Advances*, 2026.
- **Surfaced by:** Daniel Kastner *10 new citations* alert (06-16).
- **Thread:** CHIP / VEXAS disease thread (hematologic outcomes
  specifically).
- **What it is:** Review of the *MDS overlap* in VEXAS — i.e., the
  fraction of UBA1-mutated VEXAS patients who develop or co-present
  with myelodysplastic syndrome. VEXAS is now well-characterized as
  a clonal hematoinflammatory disorder of older predominantly male
  patients (per the snippet), and MDS-in-VEXAS is the natural
  bridging condition into the broader hematologic-malignancy
  literature.
- **Why it matters to you:** VEXAS is explicitly named in your
  INTERESTS file under "CHIP and VEXAS: somatic mosaicism,
  cardiovascular and hematologic outcomes." The MDS dimension is
  precisely the *hematologic-outcomes* axis. Lands in the Kastner
  citations feed — Kastner's group did the original VEXAS
  characterization, so anything in that feed is essentially the
  authoritative VEXAS reading list.
- **Action:** **HIGH** — read as the consolidated VEXAS-MDS reference
  for the next 12 months; useful for cross-sectional CHIP/VEXAS
  cohort papers where MDS co-occurrence becomes a confounder or
  effect modifier.

### 7. Points to consider for the reporting of variants of uncertain significance in germline genetic and genomic testing: A statement of the American College of Medical Genetics and Genomics
- **Authors / venue:** C. Mighton, A. Abu-El-Haija, V. … et al. —
  *ACMG points-to-consider statement*, 2026.
- **Surfaced by:** Heidi Rehm *new articles* alert (06-16).
- **Thread:** Variant interpretation (ACMG/ClinGen, **VUS reporting**).
- **What it is:** ACMG official *points to consider* statement on
  how VUSs should be reported in germline genetic and genomic testing.
  Rehm-authored, which essentially makes it the field-defining
  document for the next reporting-policy cycle. Likely covers (a)
  what to include and exclude in the report itself, (b) re-contact
  policy when reclassification occurs, (c) communication of
  uncertainty to patients/clinicians.
- **Why it matters to you:** VUS handling is the operational
  bottleneck for variant-interpretation pipelines — your INTERESTS
  file lists ACMG-AMP variant classification, ClinGen VCEP guidelines,
  and splicing/RNA evidence for VUS resolution explicitly. ACMG-issued
  guidance is the rare *citation that doesn't decay*. Pairs with the
  Zhao et al. reflex RNA-seq paper from the last report — that one
  attacks VUS *resolution*; this one defines the *reporting* policy
  in the gap before resolution.
- **Action:** **HIGH** — read once carefully and keep as a reference;
  the re-contact-on-reclassification position will be the most
  contested element and will change the operational design of any
  VUS-tracking system you build.

### 8. Detection of repeat expansion variants using next generation sequencing: A points to consider statement of the American College of Medical Genetics and Genomics Laboratory Quality Assurance Committee
- **Authors / venue:** S. Guha, I.S. Rajan-Babu, A. Kesari et al. —
  *ACMG points-to-consider statement*, 2026.
- **Surfaced by:** Stephen B. Montgomery *new related research* alert
  (06-16).
- **Thread:** Variant interpretation (ACMG/ClinGen, **NGS-based STR
  detection**) **+** rare disease (repeat-expansion disorders).
- **What it is:** ACMG points-to-consider statement on detecting
  *repeat expansion variants* (STR-based disorders like HD, FXN,
  C9orf72, RFC1) using short-read NGS. STR detection from short-read
  data has been technically thorny (ExpansionHunter, STRetch, Tandem-
  genotypes) — a formal ACMG position normalizes which tools / quality
  thresholds are clinically reportable.
- **Why it matters to you:** Pairs with #7 (Mighton VUS-reporting) as
  the *second* ACMG guidance document this window — and STR detection
  is increasingly relevant to rare-disease diagnostic pipelines you
  might build on top of WGS biobanks. Repeat-expansion disorders are
  the variant class where the standard ACMG/AMP framework has the
  largest gaps; ACMG explicitly addressing them is itself a signal.
- **Action:** **HIGH** — read for the tool inventory ACMG endorses,
  the QC criteria (read depth, repeat motif handling), and any
  guidance on reflex Sanger/Southern confirmation. Useful reference
  for any pipeline that wants to claim ACMG-conformance on STRs.

### 9. The immunoproteome and multimorbidity: A Mendelian randomization study
- **Authors / venue:** N. Hukerikar, A.D. Hingorani, S. Chopade,
  A.J. Cupido et al. — *Science Advances*, 2026.
- **Surfaced by:** Joshua C. Denny *new related research* alert
  (06-16).
- **Thread:** Multimorbidity (**shared-mechanism**) **+** genetic
  epidemiology (proteome-MR triangulation, drug-target
  prioritization).
- **What it is:** Two-sample MR of the *immunoproteome* (eight large
  plasma-proteome GWAS pooled) against multiple diseases, identifying
  immune-protein causal effects that span more than one disease —
  i.e., shared-mechanism immune drivers of multimorbidity. Drug-
  target prioritization framing implicit (Hingorani lab signature).
- **Why it matters to you:** Multimorbidity is an active thread, and
  the *shared-mechanism* line (vs the EHR-trajectory line) is the
  underpopulated half. Pairs with last report's Lim et al. Lancet
  cardiometabolic-MLTC mechanistic review and the Gobeil proteogenomic
  MASLD work: together this is now a coherent *proteome-MR-defines-
  multimorbidity-mechanism* sub-thread. Tier-one venue (Science
  Advances), so likely citation-dense.
- **Action:** **HIGH** — read for (i) the disease set and the
  multi-outcome MR architecture (univariate vs multivariate MVMR), (ii)
  shared targets that show pleiotropic causal effects across
  cardiometabolic + autoimmune clusters (those become drug-repurposing
  candidates by construction), and (iii) whether they handle
  horizontal pleiotropy with MR-Egger / weighted-median / CAUSE.

### 10. Association and risk prediction of 19 complex diseases with polygenic scores and socioeconomic status
- **Authors / venue:** F.A. Hagenbeek, A. Richmond, M. Tamlander,
  K. Detrois et al. — *Communications Medicine*, 2026.
- **Surfaced by:** Lisa Bastarache *new related research* alert
  (06-16).
- **Thread:** Genetic epidemiology (PRS) **+** social-determinants
  integration **+** ML for precision health.
- **What it is:** Joint modeling of *PRS + socioeconomic status* across
  19 complex diseases. Abstract framing: "Differences in disease risk
  are linked to inherited genetic variation and social circumstances,
  but how these factors jointly relate to multiple diseases is not
  fully understood." Likely reports independent and combined
  associations and discrimination uplift from combining PRS with SES.
- **Why it matters to you:** PRS-with-SES jointly is the operational
  shape your composite-risk modeling thread needs — your write-ups
  combining PRS with rare pathogenic variants would also benefit
  from this kind of SES-attribution analysis to forestall a "but it's
  all confounded by SES" reviewer comment. 19-disease scan also makes
  this a default cross-disease PRS+SES reference.
- **Action:** **HIGH** — read for the SES operationalization (Townsend
  Deprivation Index? composite of education + income + occupation?),
  the discrimination-uplift metric (Δ AUC vs Δ net reclassification),
  and whether they vary the analysis by ancestry.

### 11. Advancing Clinical Implementation of Cardiovascular Polygenic Risk Scores Through Patient-Level Robustness Assessment
- **Authors / venue:** R. de La Harpe, J. Vaucher, Z. Kutalik,
  J. Fellay et al. — *medRxiv*, 2026.
- **Surfaced by:** Lisa Bastarache *new related research* alert
  (06-16).
- **Thread:** Genetic epidemiology (PRS) **+** ML for precision
  health (**patient-level robustness / decision-grade PRS
  implementation**) **+** clinical translation.
- **What it is:** Examines whether **PRSes that perform equivalently
  at the population level disagree at the individual patient level**
  for ASCVD — i.e., intra-individual variability across PRS choices.
  Abstract: "Polygenic risk scores (PRSs) for atherosclerotic
  cardiovascular disease (ASCVD) can perform equivalently at the
  population level yet disagree for individual patients."
- **Why it matters to you:** This is the *clinical-implementation
  audit* counterpart to the population-level PRS validation
  literature, and it directly addresses a known weakness of PRS
  deployment: AUC-equivalent scores can give patient-level decisions
  that *swap*. Your ML-for-precision-health thread explicitly calls
  out calibration and decision-curve analysis — this paper is the
  *individual-level-disagreement* extension of that. ASCVD is also
  the prototype disease for PRS clinical translation.
- **Action:** **HIGH** — read for (i) the patient-level disagreement
  metric (rank-correlation? Bland-Altman? % discordant on the
  high-risk threshold?), (ii) what drives discordance (LD reference,
  variant set, weighting scheme), and (iii) the practical
  recommendation: do they advocate ensembling, choosing the most-
  validated score, or reporting an uncertainty band?

### 12. Polygenic risk scores associate with asthma phenotypes and proteomic analyses implicate IL1R1 in two family-based studies
- **Authors / venue:** S. Lee, M. Moll, K. Mendez, N. Prince,
  J. Lasky-Su et al. — *medRxiv*, 2026.
- **Surfaced by:** Lisa Bastarache *new related research* alert
  (06-16).
- **Thread:** Genetic epidemiology (PRS + proteomics) **+** asthma
  phenotyping.
- **What it is:** PRS-based stratification of asthma phenotypes in
  two family-based cohorts, with proteomic analyses implicating
  IL1R1 as a mechanistic driver. Combines the PRS-to-subtype shape
  (similar to #4 Turchin IL-18 / IBD this report) with proteomic
  follow-up.
- **Why it matters to you:** Three threads at once. (a) PRS-to-subtype
  approach — this is the third paper in two windows that uses PRS to
  define a *mechanistically-defined disease subgroup* (Marston SGLT2i
  × cardiomyopathy-variant from last report; Turchin IL-18-IBD this
  report; Lee IL1R1-asthma here). (b) Asthma is adjacent to the
  autoimmune / multimorbidity threads. (c) Family-based design adds
  population-stratification robustness that helps with the
  cross-ancestry portability conversation.
- **Action:** **HIGH** — read for the family-based PRS adjustment
  (within-family vs between-family effects) and how they go from a
  PRS-positive proteomic hit to a *causal* IL1R1 claim (likely
  pQTL-MR / colocalization).

### 13. Long-term comorbidity associated with childhood periodic fever, aphthous stomatitis, pharyngitis, and adenitis (PFAPA) syndrome: a case-control study
- **Authors / venue:** H. Uosukainen, S. Kettunen, T. Ruuska-Loewald
  et al. — 2026 (Kastner-related research feed; venue not in
  snippet — likely Pediatrics / Rheumatology).
- **Surfaced by:** Daniel Kastner *new related research* alert (06-16).
- **Thread:** Multimorbidity (**autoinflammatory long-term
  comorbidity**) **+** rare disease (PFAPA).
- **What it is:** Case-control study of long-term comorbidity in
  patients with PFAPA syndrome (the most common pediatric
  autoinflammatory syndrome). Investigates whether PFAPA in childhood
  predisposes to adult-life comorbidities — a multimorbidity-
  trajectory question framed at the rare-disease end.
- **Why it matters to you:** PFAPA is rare-disease + autoinflammatory
  + multimorbidity-relevant; the case-control design also yields a
  template for any rare-disease longitudinal-comorbidity study you
  might build in AoU / UKB (where the case sample sizes for
  individual rare diseases are small but the follow-up is long). The
  Kastner-feed surfacing is high-signal because his group has been
  consolidating the autoinflammatory-disease comorbidity literature.
- **Action:** **HIGH** — read for the matching strategy (age, sex,
  ascertainment site) and the comorbidity outcome set (do they look
  beyond rheumatologic outcomes into cardiometabolic, mental health,
  etc.?). Useful template if you ever extend your multimorbidity work
  into childhood-onset rare-disease cohorts.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **How Post-Training Shapes Biological Reasoning Models** —
  L. Fesser, H. Zhang, M.M. Li, E. Wang, B. Perozzi, S. Azizi,
  S.M. Kakade, M. Zitnik — *arXiv cs.LG*, 2026 (digest 06-16,
  also Marinka Zitnik articles feed). Controlled study of CPT / SFT
  / RL trade-offs in biology FMs (DNA/RNA/protein backbones, 100+
  models trained). Findings: CPT improves downstream perf by
  aligning models with biological language; SFT increases ID
  performance but OOD declines as models fit training distribution;
  RL applied to strong SFT checkpoints with aligned rewards recovers
  OOD. *Watch for:* the recipe (brief SFT, larger RL allocations,
  asymmetric adaptation across stages) — directly transferable to
  any post-training of an EHR FM in the CLMBR / MOTOR lineage even
  though this paper is on bio-sequence FMs.

- **hyreg2: R package for latent-class estimation on mixed
  continuous + dichotomous data** — S. Elkenkamp, J. Grosser,
  K. Rand — *arXiv stat.ME*, 2026 (digest 06-16). Frequentist
  joint-likelihood latent-class for mixed outcome types (continuous
  + binomial), with EM via flexmix backend; handles heteroskedasticity
  and censored data. Off-thread (clinical / health-economics use case
  is EQ-5D-5L valuation), but a clean implementation for any
  latent-class / disease-subtype-discovery work that mixes lab
  values with binary indicators. *Watch for:* whether the joint
  likelihood scales to k > 4 classes and to the number of binary
  indicators typical of phecode-defined comorbidity profiles.

- **AI safety evaluation in an underrepresented population:
  real-world performance of clinical decision support and frontier
  language models on Medicaid patient [data]** — S. Basu, S. Patel,
  P. Sheth, B. Arevalo et al. — 2026 (Patrick Ryan related-research
  feed). Real-world performance audit of CDS and frontier LLMs on
  Medicaid patient data — i.e., a fairness audit grounded in a
  specific underrepresented payer population. Off your direct
  threads but on the broader CDS/LLM-in-healthcare audit pattern.
  *Watch for:* the evaluation metric set (calibration in
  subpopulations; absolute vs relative risk by payer status).

- **Detecting disease comorbidity based on SNP association on PheWAS
  scale** — L. Chen, L. Liao — *Computational Biology and
  Chemistry*, 2026 (Bastarache-citation feed). ML method for
  comorbidity detection grounded in UKB PheWAS SNP-association data.
  *Watch for:* the dimensionality-reduction choice (the snippet
  flags "high dimensionality of SNP data, a common [issue]") — if
  it's a comorbidity network from SNP-sharing rather than from
  patient-level co-occurrence, that's a genuinely different lens
  worth knowing for your multimorbidity-graph work.

- **Methodological Developments for Advancing Genetic Risk
  Prediction Across Populations** — J.A. Dias — PhD thesis, 2026
  (Bastarache-citation feed). Multi-chapter thesis covering
  multi-ancestry GWAS strategy (pooled vs fixed-effect meta vs
  MR-MEGA), cross-ancestry PRS, and rare-variant handling. *Watch
  for:* the MR-MEGA simulation comparison and any practical decision
  rules for when pooled analysis beats meta-analysis under fixed-
  vs mixed-effects framings.

- **Methodological Advances for Robust and Interpretable
  Gene-Environment Interaction Studies** — M. Sadowski — PhD thesis,
  2025 (Bastarache-citation feed). Methods for SNP-level GxE with
  improved power and interpretation. *Watch for:* any methods that
  scale from SNP-level GxE up to PRS × environment, which is the
  framing you'd actually want for clinically-relevant gene-
  environment work (e.g., PRS × CFTR modulator).

- **Improving Genetic Risk Prediction of CAD in Chinese by
  Multi-ancestry and Multi-trait GWAS Integration** — H. Wang,
  J. Lin, X. Hao, W. Tang, K. Wang, M. Jiang, D. Wu et al. —
  *Genomics, Proteomics & Bioinformatics*, 2026 (Bastarache-
  citation feed). Multi-ancestry + multi-trait integration to
  improve a CAD PRS in Chinese populations. *Watch for:* the
  multi-trait integration step (which auxiliary traits and how they
  weight) and whether the gain is uniform across CAD subtypes — the
  shape generalizes to any underrepresented-ancestry PRS work in
  AoU.

---

## SKIP / noise (logged, no action)

- **"drug repurposing" keyword alert (06-17)** continued to surface
  target-only / chemistry-only items (Wang et al. on benfotiamine as
  a P2Y14R antagonist via molecular dynamics — no EHR / KG /
  clinical-evidence loop). SKIP per INTERESTS filtering. Two
  consecutive windows with no on-thread drug-repurposing items.
- **"mendelian diseases" keyword alert (06-17)** continued to
  surface MR (mendelian randomization) papers (Yang et al. on gut
  microbiota and urolithiasis). 5th consecutive window. Pipeline
  fix is overdue.
- **"All of Us research program" keyword alert (06-17)** —
  cervical-cancer screening among Hispanic women on the
  Arizona-Sonora border (Robles Morales dissertation). Off-thread.
- **"UK Biobank" keyword alert (06-17)** — insomnia / proteomic /
  mortality in depression (Liu et al., BMC Psychiatry). Off-thread
  unless you're tracking proteomic depression endpoints.
- **"electronic health records" keyword alert (06-17)** — EHR
  adoption in Philippine public hospitals (Villarino, IJMI). Health
  policy, not informatics. SKIP.
- **"knowledge graph" keyword alert (06-17)** — LLM-driven KG
  enrichment (Sabitov et al., non-biomedical conf). 5th consecutive
  window of non-biomedical KG hits. Pipeline fix overdue.
- **"Foundation models and 'electronic health records'" keyword
  alert (06-17)** — FHIR-EMR development in Indonesia (Qomaruddin
  & Rakhmawati). Off-thread (FHIR development position piece, not
  EHR FM).
- **"variant interpretation" keyword alert (06-17)** — bidirectional
  alignment fine-tuning for decoder-only LMs (Vinogradov et al.,
  Wave Electronics conference). Keyword-incident only, not on the
  ACMG / ClinGen axis. SKIP.
- **"rare diseases" keyword alert (06-17)** — caregiver coping in
  IMD in India (Kharbanda et al.). Care / psychosocial study, off
  your methods + variant + LLM-tooling threads. SKIP.
- **Bidirectional Alignment FT for Decoder-only LMs** keyword hits —
  fine-tuning methods paper from outside biomedical NLP, surfaces
  only because of keyword leakage. SKIP.
- **Vivek Natarajan citations: General-purpose LLMs outperform
  specialized clinical AI tools on medical benchmarks** (Vishwanath
  et al., Nature Medicine, 06-16) — Med-Gemini-adjacent debate
  about benchmark validity, not on your clinical-deployment EHR
  thread. Logged but not actioned; would be METHODS-WATCH if the
  *evaluation framework* itself is the contribution.
- **Marinka Zitnik citations: Detecting Functional Memorization in
  Code LLMs** (Meeus et al., 06-16) — code memorization; off the
  bio-FM / EHR-FM thread.
- **Citation noise** continued to surface oncology, ARDS, ICI
  myocarditis, and CRISPR / synthetic-bio items via Pritchard,
  Hripcsak, Karczewski, and Vogelstein citation feeds. All logged
  but not on-thread.

---

## Suggestions for the pipeline

Carrying forward the previous three reports' recommendations, all
still applicable. Reiterated here for visibility because none has
been actioned yet and this week's report would have been ~50%
shorter without the journal/medRxiv surfaces that compensate for
arXiv's empty days:

1. **Add `cs.LG`, `stat.ME`, and medRxiv/bioRxiv source feeds to
   `arxiv-digest`.** 4 of 5 days in this window produced zero papers
   on the current q-bio/stat.AP categories. The Fesser/Zitnik post-
   training paper (#1 METHODS-WATCH) only appeared because the
   06-16 digest reached into cs.LG informally; that should be
   first-class. medRxiv alone would have surfaced items #1, #3, #4,
   #11, #12 above.
2. **`mendelian diseases` keyword still leaks MR papers** — 5
   consecutive windows now. Replace with `OMIM` / `MIM:` IDs, or
   exclude `-randomization`. Overdue.
3. **`knowledge graph` keyword: 5th consecutive window of non-
   biomedical hits.** Recommend `biomedical knowledge graph` OR
   `clinical knowledge graph` OR `(knowledge graph) (medical OR
   biomedical OR clinical OR EHR OR phenotype)`.
4. **`drug repurposing` keyword: 2nd consecutive window of
   target-only / chemistry-only hits.** Add `(EHR OR real-world OR
   biobank OR knowledge graph OR target trial)` to the keyword
   logic, or split into two sub-keywords.
5. **Add `proteomic polygenic` / `pQTL polygenic`** as a keyword.
   Two papers in two weeks (Turchin IL-18/IBD; Lee IL1R1/asthma)
   plus last week's Gobeil. This is becoming its own sub-pattern.
6. **Add `points to consider` / `ACMG statement`** as a phrase
   keyword. Two ACMG points-to-consider statements this window (VUS
   reporting + repeat expansions). They are high-citation-value
   reference documents that should surface predictably.
7. **Add `All of Us` as a phrase (not just `AoU`)** — Kang et al.
   item #2 surfaced via the Bastarache citations feed, not directly.
8. **Self-citation hits** — Kang et al. (Statistics in Biosciences)
   surfaced in your own Chenjie Zeng citation feed *and* in the
   Bastarache feed — double-surfacing is a useful priority signal.
   Keep self-citation alerts as-is.
