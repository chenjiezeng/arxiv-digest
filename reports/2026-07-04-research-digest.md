# Research digest report — 2026-07-04

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-27 → 2026-07-04** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-07-01 → 07-04 | Two large 07-04 batches (00:10Z author-feeds + 10:27Z keyword-feeds): CPAgents PheWAS, MIXPRS Nature Genetics, rare-variant PRS medRxiv (Karczewski feed), CH↔Alzheimer review (CHIP kw), All of Us endometriosis clustering, Bastarache-cited CFTR pancreatitis organoids, Ellinor CAD PRS clinical utility, ACMG repeat-expansion NGS statement, Bastarache-cited SSc phenotyping (LPC vs PheRS vs ICD), and more. Lighter 07-01/02/03 tail. |
| `arxiv-digest` repo (`digests/`) | 2026-06-27 → 07-04 | Very light week: **07-01 = 7 papers** (UKB proteomics GGM = HIGH; 3 causal-inference stat.ME papers = METHODS-WATCH; IBD spatial-ST workflow = low). **06-30 = 4 papers** (GWAS+HWE unified test, DNA LMs, H&E-RNA alignment, insurance embeddings). **06-25/26/27/28/29 = 0-2 each**, mostly incidental keyword hits. **07-02/03/04 mostly empty** — see pipeline note below. |
| NCBI My NCBI "drug repurposing" PubMed | 07-02 07:15Z | 15 items; oncology-heavy, one KG+LLM therapeutic-prioritization preprint (Wei et al., PMC-42389242) is directly on-thread. |

> ⚠️ **arxiv-digest pipeline note:** the last several days show near-zero
> results even in categories that produced content earlier in the month.
> **07-02 = 1 paper (Airbnb), 07-03 = 1 paper (3D plant phenotyping),
> 07-04 = 0**. Suppression counters (`previously surfaced, suppressed`)
> are non-zero, so `seen.json` is working — but base counts look
> genuinely thin. Possibly a real seasonal dip (July 4 US holiday
> weekend, fewer submissions), possibly a partial fetch failure that
> isn't logged. Worth a quick sanity check of a 3-day lookback run
> against the arXiv API before dismissing as noise.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

**HIGH-priority hits this cycle (12):**

1. **CPAgents** — agentic composite-phenotype generation for cardiac
   PheWAS in UK Biobank imaging (arXiv 2606.28179).
2. **mCNV PheWAS in 422,170 UKB individuals** — first large-scale
   phenome-wide association scan of multi-allelic CNVs (medRxiv).
3. **MIXPRS** (Nature Genetics, Yang lab) — multi-population,
   multi-method PRS integration from summary statistics.
4. **Rare-variant risk scores complement common-variant PRS** (medRxiv,
   Ge/Karczewski adjacent) — WGS-based composite risk scoring, exactly
   the "stacking PRS with rare pathogenic variants" bullet in
   `INTERESTS.md`.
5. **STELLAR** (medRxiv, Lin lab) — ensemble learning to fuse
   rare-variant burden with common-variant PRS.
6. **CAD PRS utility in low-risk primary prevention** (Bertot,
   Melloni, Pirruccello, Ellinor et al., Am J Cardiol) — PRS
   reclassifies clinically low-risk individuals into elevated ASCVD
   risk.
7. **Prior-informed conditional GGMs on UKB cardiometabolic
   proteomics** (Mapelli et al., 2606.31805) — n=49,129 UKB
   participants, 366 proteins; recovers T2D network perturbations and
   34 network-central candidate biomarkers.
8. **All of Us endometriosis/adenomyosis symptom clusters** (Goroshchuk
   et al., Human Reproduction) — Controlled Tier v8; combines biobank
   + symptom clustering + quality-of-life.
9. **CFTR-modulator responses in chronic-pancreatitis organoids**
   (Osorio-Vasquez et al., Cell Stem Cell) — 37 PDOs across
   idiopathic/hereditary/alcohol CP; extends CFTR-modulator biology
   beyond CF.
10. **CHIP in Alzheimer's brain** (Zhao, King, Wong, Trends Mol Med) —
    review of protective vs pathogenic CHIP effects in AD via
    mutant-myeloid brain infiltration.
11. **DNMT3A CHIP → autoimmunity** (Sun et al., MR study) — CHIP
    causal-inference link to 14 AIDs; intersects the CHIP and IBD
    threads.
12. **ACMG Points-to-Consider on repeat-expansion detection from NGS**
    (Guha et al., Genetics in Medicine) — directly relevant to variant
    interpretation + rare-disease diagnosis.

**METHODS-WATCH (6):**

- Residual-on-residual regression as observational-CI alternative to
  AIPW/TMLE under weak positivity (Naimi et al.).
- Unified HWE+association test for GWAS (Böhringer & Holzmann).
- LLM+biomedical-KG therapeutic prioritization (Wei et al., PMC).
- Long-read + Mendelian-logic phased-variant interpretation for
  inherited retinal disease (Mustafi et al., IOVS).
- Unsupervised (LPC) vs rule-based (PheRS) vs ICD counts for systemic
  sclerosis EHR phenotyping (Luo, Weng, Bernstein et al.).
- RareDxR1 / RarePathAI — two rare-disease reasoning systems (agentic
  LLM and real-world-data predictive analytics respectively).

**SKIP:** Pig heritability, plant 3D phenotyping, Airbnb causal ML,
generic AI-in-drug-discovery reviews, insurance-pricing LLM
embeddings, non-thread oncology drug-repositioning.

---

## Detailed writeups — HIGH bucket

### 1. CPAgents: Agentic Composite Phenotype Generation for Cardiac Disease Association
- **Authors:** Z Li, W Zhao, K Yu, W Zhang, PM Matthews, W Bai, et al.
- **Venue:** arXiv 2606.28179 (2026)
- **Thread hits:** PheWAS / phecodes, EHR-linked biobanks (UKB
  imaging), ML for precision health.
- **What's new:** Current PheWAS relies on pre-defined single-variable
  phenotypes or expert-crafted features. CPAgents proposes an
  **iterative, multi-agent LLM framework** that composes richer
  phenotypes from cardiac imaging + associated variables, aiming to
  capture non-linear effects and cross-phenotype interactions before
  running association tests.
- **Why it matters to you:** Directly on your PheWAS/biobank axis.
  Cited in a Bastarache-tracked feed too, so it's crossing PheWAS
  citation networks. Worth reading in full for whether the composite
  phenotypes are (a) usefully **portable** across biobanks vs.
  UKB-specific, and (b) whether the agent uses phecodes as anchors or
  invents its own outcome definitions — the latter would complicate
  reproducibility.

### 2. Phenome-wide association of multiallelic CNVs in 422,170 UKB individuals
- **Authors:** M Eisenberg, R Packer, N Shrine, G Demidov, H Pack, et
  al.
- **Venue:** medRxiv (2026-06-04 posting, 2026-06-03 date).
- **Thread hits:** PheWAS, UKB, genetic epidemiology, variant
  interpretation.
- **What's new:** First large-scale PheWAS of **multi-allelic** CNVs
  (mCNVs) at UKB scale. These variants are hard to characterize
  genome-wide and often not tagged by flanking SNVs, so they've been
  underrepresented in prior CNV-PheWAS. The paper claims **novel
  disease loci** at multi-allelic sites.
- **Why it matters to you:** Extends the phenome-wide catalog into a
  variant class that ACMG/ClinGen frameworks handle poorly. If any
  of the reported loci fall in genes your VCEP or CFTR/APOL1/CHIP
  threads care about, worth cross-referencing.

### 3. MIXPRS: multi-population and multi-method PRS from summary statistics
- **Authors:** L Xu, Y Dong, X Zeng, Z Bian, G Zhou, L Guan, H Zhao.
- **Venue:** Nature Genetics (2026).
- **Thread hits:** Genetic epi (PRS, cross-ancestry portability).
- **What's new:** Ensemble that integrates multiple existing
  multi-population PRS methods using **only summary statistics**,
  yielding better performance in underrepresented ancestries than any
  single constituent method.
- **Why it matters to you:** Cross-ancestry portability is a listed
  active thread. Because it's summary-statistics-only, MIXPRS is
  usable in AoU / BioVU / MVP without individual-level exchange —
  which is exactly the constraint you tend to work under.

### 4. Rare-variant risk scores complement common-variant PRS
- **Authors:** M Qin, B Wu, L Yang, W Cheng, J Feng, J Yu, T Ge, et
  al.
- **Venue:** medRxiv (2026-06-21 date, 2026-06-29 posting).
- **Thread hits:** Genetic epi (composite risk models stacking PRS
  with rare pathogenic variants), variant interpretation.
- **What's new:** Uses WGS to build **rare-variant risk scores (RVRS)**
  and shows they add to common-variant PRS for disease risk
  prediction and top-tail stratification.
- **Why it matters to you:** Bull's-eye for the "composite risk models
  stacking PRS with rare pathogenic variants" bullet in
  `INTERESTS.md`. Reproducing / adapting their scoring in BioVU or
  AoU (once WGS coverage is broad enough) is a plausible near-term
  project.

### 5. STELLAR: ensemble learning for rare-variant + PRS
- **Authors:** T Chen, X Li, R Mazumder, H Zhang, X Lin.
- **Venue:** medRxiv (2026-06-07 posting).
- **Thread hits:** Same as #4.
- **What's new:** A flexible ensemble framework specifically designed
  to integrate rare-variant signals into polygenic prediction. Two
  independent teams (STELLAR from the Lin lab, Qin et al. above)
  converging on rare+common composite scoring within the same
  fortnight is a signal that this subfield is heating up.
- **Why it matters to you:** Read alongside #4 and compare the
  ensemble architecture (STELLAR) vs. the direct-RVRS approach — the
  design choices probably matter more for high-heritability + rare-
  variant-enriched diseases (BRCA1/2, LDLR, monogenic-cardio) than for
  diffusely polygenic traits.

### 6. Utility of a CAD PRS in a low-risk primary prevention cohort
- **Authors:** JH Bertot, GEM Melloni, J Pirruccello, FK Kamanu et
  al. (Ellinor group).
- **Venue:** American Journal of Cardiology (2026).
- **Thread hits:** ML for precision health (PRS tied to a clinical
  decision — who to escalate to primary prevention), genetic epi.
- **What's new:** Longitudinal cohort study asking whether CAD PRS
  identifies clinically low-risk individuals with elevated ASCVD risk
  (i.e., reclassification into treat/screen). The specific angle you
  care about: how the reclassification behaves at the guideline
  cutoff, not just AUROC.
- **Why it matters to you:** This is exactly the type of PRS-utility
  paper that fits the "PRS tied to a clinical decision" HIGH criterion
  vs. the SKIP "leaderboard" default. Ellinor group typically means
  the ancestry-stratification and calibration will be reported
  transparently.

### 7. Prior-informed conditional GGMs — UKB cardiometabolic proteomics
- **Authors:** A Mapelli, MC Massi, G Cuccuru, E Di Angelantonio, F
  Ieva.
- **Venue:** arXiv 2606.31805 / stat.AP (2026).
- **Thread hits:** UKB (proteomics arm), ML for precision health,
  multimorbidity (cardiometabolic).
- **What's new:** GGM that (i) incorporates curated PPI-database
  priors via a **structured weighted penalty** and (ii) conditions on
  covariates so the network can vary by individual context. Applied
  to n=49,129 UKB participants, 366 proteins → recovers **T2D-
  associated network perturbations**, identifies **34 network-central
  candidate biomarkers** (several detectable only via network
  connectivity, not marginal DE), and finds 6 biologically coherent
  protein communities.
- **Why it matters to you:** Methodologically clean template for
  network-level biomarker discovery in EHR-linked biobank proteomics.
  Their emphasis on "detectable only through connectivity, not
  differential expression" is exactly the argument for network
  approaches over differential-abundance-first pipelines.

### 8. Endometriosis / adenomyosis symptom clusters in All of Us
- **Authors:** O Goroshchuk, N Pérez-Gómez, F Carmona, HS Taylor et
  al.
- **Venue:** Human Reproduction (2026).
- **Thread hits:** All of Us cohort work, chronic disease clustering
  and multimorbidity, EHR phenotyping.
- **What's new:** Large cross-sectional AoU (Controlled Tier v8)
  analysis characterizing symptom clusters in endometriosis /
  adenomyosis and QoL impact.
- **Why it matters to you:** Illustrative recent example of what
  people are getting out of AoU v8 that includes survey QoL data
  alongside EHR. If you're planning any AoU-based project, worth
  scanning for how they handle case identification (SNOMED /
  survey-self-report / phecode) and multiple-testing across
  symptom domains.

### 9. CFTR-modulator responses in chronic-pancreatitis organoids
- **Authors:** V Osorio-Vasquez, J Zhu, JC Lumibao, K Lande et al.
- **Venue:** Cell Stem Cell (2026).
- **Thread hits:** Cystic fibrosis / CFTR (pharmacoepi + modulator
  eligibility bullet extended into CFTR-related disease).
- **What's new:** 37 patient-derived organoids across idiopathic,
  hereditary, and alcohol-related CP. Retains inflammation-associated
  transcriptomic and proteomic features. Tests CFTR-modulator response
  in this new indication.
- **Why it matters to you:** Directly relevant to the CFTR-modulator
  thread — expands the eligibility question from "CF patients with X
  genotype" to "CFTR-heterozygous / CFTR-related disease patients" and
  provides a preclinical justification for real-world modulator
  outcomes studies in chronic pancreatitis. Cited citations include
  "Beyond Carrier Status: CFTR Heterozygosity as an Overlooked …" —
  the CFTR-heterozygote clinical spectrum is having a moment.

### 10. Clonal hematopoiesis in Alzheimer's brain
- **Authors:** H Zhao, KY King, ST Wong.
- **Venue:** Trends in Molecular Medicine (2026).
- **Thread hits:** CHIP / VEXAS (CHIP-hematologic-outcomes bullet
  extended to CNS).
- **What's new:** Review of the emerging biology of CH-mutant myeloid
  cells entering / expanding in the AD brain — framing them as
  **context-dependent** (inflammatory in some settings, reparative in
  others). Not primary data, but a useful current-state snapshot.
- **Why it matters to you:** Would slot into any CHIP+EHR-outcomes
  proposal as a mechanistic-plausibility citation for a CH↔dementia
  outcomes lookup in BioVU or MVP.

### 11. DNMT3A CHIP → autoimmunity — MR study
- **Authors:** L Sun, S Zhang, M Feng, Y Wang, Y Jin, J Xue, X Ni et
  al.
- **Venue:** Combinatorial Chemistry & High Throughput Screening
  (via PubMed 42381332).
- **Thread hits:** CHIP + inflammatory-bowel-disease / autoimmune
  overlap.
- **What's new:** Two-sample MR linking genetic liability to
  DNMT3A-driven CHIP with 14 autoimmune diseases, mediated by
  specific immune-cell populations.
- **Why it matters to you:** Directly hits the "CHIP and VEXAS →
  hematologic outcomes" thread's autoimmune-spillover corner, and
  helps triangulate whether prior EHR observational associations
  between CHIP and autoimmune incidence carry through causal-scale
  scrutiny. Journal choice is modest — don't over-weight, but worth
  a look for the instrument selection.

### 12. ACMG Points-to-Consider — repeat-expansion detection from NGS
- **Authors:** S Guha, IS Rajan-Babu, A Kesari, S Garg, NC Rose et
  al.
- **Venue:** Genetics in Medicine (2026).
- **Thread hits:** Variant interpretation (ACMG/ClinGen), rare
  disease.
- **What's new:** Formal ACMG "points to consider" statement on
  detecting repeat-expansion variants from short-read and long-read
  NGS. Sets expectations for laboratory workflows and
  interpretation.
- **Why it matters to you:** Anchors any rare-disease repeat-
  expansion work on defensible ACMG footing, and worth flagging to
  any collaborators running InterVar/AnFiSA-style pipelines.

---

## Detailed writeups — METHODS-WATCH bucket

### M1. Residual-on-Residual Regression for observational effect estimation
- Naimi et al. (stat.ME, 2606.30976). Presents a **stable
  alternative to AIPW/TMLE** for partial-linear-model settings, and
  in simulation is **better under weak positivity violations** when
  the true effect is approximately constant. Concordant with AIPW /
  TMLE on the nuMoM2b vegetable-intake↔preeclampsia example.
- **Why watch:** Useful triangulation tool for pharmacoepi work
  where positivity is thin (e.g., CFTR-modulator or SGLT2i
  eligibility subgroups).

### M2. Unified HWE-and-association test for GWAS
- Böhringer & Holzmann (stat.ME, 2606.30311). Conditions the Pearson
  χ² on the HWE-χ² in controls, removes the arbitrary HWE cutoff,
  improves ranking and downstream fine-mapping efficiency.
- **Why watch:** Small QC-layer improvement that's basically free to
  adopt in a GWAS pipeline; worth flagging to anyone maintaining an
  in-house GWAS QC playbook.

### M3. LLMs meet biomedical KGs for mechanistically-grounded therapeutic prioritization
- Wei, Day, Wang, Alewine, Tyler, Slika, Saraf, Tai, Chan, Leaman, Lu
  (arXiv 2604.19815, PubMed PMC-42389242, NIH-Lu group).
- **Why watch:** The "**explainable hypothesis output (path or
  subgraph rationales rather than opaque link-prediction scores)**"
  bullet in your drug-repurposing thread reads like it was written
  for this paper. Worth full-text reading and comparing rationale
  quality to KG-only baselines (RotatE etc.).

### M4. Phased-variant framework with long-read + Mendelian logic — IRD
- Mustafi, Nakamichi, Rahimi, Darrah, Rooks et al. (IOVS, 2026).
- **Why watch:** Direct hit for the "splicing / RNA evidence for VUS
  resolution" and long-read-based ACMG evidence adjudication
  sub-theme. If replicable in other Mendelian domains (cardiomyopathies,
  hereditary cancer), it's a candidate to pull into the VCEP
  workflow.

### M5. LPC vs. PheRS vs. ICD-count comparison in systemic sclerosis
- Luo, Zhang, Agarwal, Weng, Bernstein (Semin Arthritis Rheum, 2026;
  Bastarache-cited feed).
- **Why watch:** Head-to-head EHR phenotyping benchmark of an
  unsupervised approach (LPC) vs. rule-based PheRS vs. plain ICD
  counts, with mortality-prediction as the downstream task. Because
  it cites Bastarache's original PheRS work, the setup should be
  familiar. Useful reference for any PheRS-methodology paper you're
  writing.

### M6. Rare-disease reasoning systems — RareDxR1 and RarePathAI
- RareDxR1 (Jiang et al., arXiv 2607.00147) — agentic LLM for
  open-domain rare-disease diagnosis from unstructured clinical
  notes, and their sibling paper Elmofty & Leser (BioNLP 2026)
  quantifies **when retrieval actually helps** vs. hurts LLM
  rare-disease diagnosis (versus DeepRare-style agentic baselines).
- RarePathAI (Russo et al., Research Square) — predictive analytics
  in real-world data, citing Bastarache's rare/common vocab linking
  work.
- **Why watch:** Two independent systems tackling the same problem
  space (rare disease + LLM + real-world / notes data). Elmofty &
  Leser's ontology-coverage angle is the more methodologically
  interesting of the three because it treats the ontology as the
  independent variable.

---

## Cross-cutting observations

- **The rare + common composite-PRS wave is real.** Two independent
  medRxiv preprints (Qin et al. and Chen/Lin STELLAR) within days of
  each other, and MIXPRS as the cross-ancestry ensemble. Worth
  writing a two-paragraph internal note comparing the three
  formulations before external groups do.
- **CFTR beyond CF is picking up steam.** Cell Stem Cell chronic-
  pancreatitis-organoid paper + the "CFTR heterozygosity as
  overlooked" citation trail suggest the CFTR-modulator thread is
  broadening. The BioVU / AoU real-world evidence for modulator use
  in CFTR-heterozygotes with pancreatitis phenotypes is a very
  gettable retrospective study.
- **Drug repurposing evidence-stack diverging.** The KG-based branch
  (Wei et al.) and the LLM-embedding-only branch (Kondadadi &
  Ortega, "Beyond Knowledge Graphs") are actively contesting whether
  KGs are necessary. Consistent with your INTERESTS preference for
  the explainable-KG branch and lower interest in text-only
  pipelines.

## Not covered (deferred)

- 30+ author-feed Scholar alerts (Denny, Hripcsak, Chute, Callahan,
  Zitnik, Szolovits, Karczewski-adjacent, Ellinor, Van der Schaar,
  Montgomery, Pritchard, Yang etc.) — the top hits from each were
  merged into the buckets above; the rest were incidental
  cross-citations to off-thread work.
- Daily arXiv subject-class mailings (cs, q-bio, stat) to
  `rabble@arxiv.org` — mailing-list-level, not individually triaged.
- Coffee↔liver-proteomics UKB paper — clinical epi, off your active
  methods threads.
- Plant 3D phenotyping, Airbnb causal ML, insurance-embedding LLM
  papers from the arxiv-digest — SKIP.
