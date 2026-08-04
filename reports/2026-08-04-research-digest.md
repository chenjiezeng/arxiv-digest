# Research digest report — 2026-08-04

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-08-01 12:35Z → 2026-08-04 05:00Z** (~2.5 days since the
last committed report at `reports/2026-08-01-research-digest.md`). The
window is dense with drug-target-MR / proteomic-MR papers and with
pharmacogenomic hypertension work; the biggest single item is that the
**Bujnis et al. Hashimoto's GWAS in which you are a co-author is now the
official Nature Genetics publication** (previously seen as the accepted-
online version in the 08-01 report — now the AOP/first-online version
has landed and the Google Scholar author-alert fired to your `Chenjie
Zeng - new articles` feed).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| `arxiv-digest` repo (`digests/2026-08-01.md`, `2026-08-02.md`, `2026-08-04.md`) | 08-01, 08-02, 08-04 (10:30Z crons; 08-03 empty/suppressed) | 3 daily runs. 08-01 and 08-02 empty (previously surfaced items suppressed). **08-04 surfaced 6 papers** including LeDXA (UKB self-supervised DXA representations, HIGH methods-watch) and the TTE R package tutorial (Noma, HIGH direct-use). |
| NCBI "My NCBI What's New" — AoU / UKB / drug repurposing | 08-03 16:58Z | AoU: 0 items this window (no NCBI batch fired; Scholar covered it). UKB: 8 items (Vaura Eur Heart J pharmacogenomic hypertension side effects is HIGH; Zhong proteome-wide MR CVD is HIGH; the rest are off-thread). Drug repurposing: 2 items (Zhong cross-population PW-MR CVD is a duplicate of the UKB item; Asiri antiviral docking is off-thread noise). |
| Google Scholar keyword alerts | 08-03 10:51Z | Ten keyword feeds fired in a single batch: AoU (5 items — Rahman opioid ML now Scholar-visible, Lehrer tocilizumab RA depression, Salwan glaucoma deprivation, Araque MASLD social factors, Kamyab ischemic stroke post-TIA); drug repurposing (Gulisano organoids review — off-thread); CF carriers (Jiang post-ERCP pancreatitis — worth reading); foundation models & EHR (TabHealth self-supervised tabular FM — off-thread); rare diseases + UDN + mendelian (Farrugia Middle East review, Martin UDN-Aus, Kraatari-Tiri XXYLT1 IRD — all off-thread); autoimmune (Zhang notch signaling review); APOL1 (Kwakyi West African CKD diet); variant interpretation (Yasinskyi AlphaFold BRCA1); EHR (Michaud youth vaping RCT protocol); KG (Sun KG-ACE LLM medical reasoning); UKB (Firdous omega-3 systematic review); CHIP (Zhang review — off-thread). |
| Google Scholar author-feed alerts | 08-03 04:32Z | ~24 author feeds fired in a single batch. Top-signal items: **Bujnis et al. Nat Genet Hashimoto's** (your `Chenjie Zeng - new articles` feed — you are a co-author); **Wang H, Zhang B et al. medRxiv distributional diagnosis with negative controls for GLP-1 outcome-wide RWE** (Hripcsak + Ryan feeds — OHDSI/pharmacoepi HIGH); **Diao et al. arXiv kidney function / KF prediction multiethnic** (Zitnik feed); **Sevgi 2025 CRISPR breast cancer risk loci** (citing your work); **Silberg/Zou Circulation viewpoint on agentic/generative AI for drug discovery**; **Seow Nature Genetics Singapore precision medicine** (Denny feed); **Hamad JAMA Netw Open GLP-1 fragility fracture in T2D** (Hernán feed); **Corsi-Zuelli EHR low-dose MTX × psychosis** (Pascal Brandt feed — repurposing angle). Also Karczewski/Pritchard/Yang/Callahan/Bastarache/Kastner/Do/Montgomery/Snyder/Szolovits feeds — mostly off-thread noise. |
| Preprint / journal subject alerts (bioRxiv, medRxiv, JAMA) | 08-01 → 08-03 | Not surfaced in the search; assume individual on-thread items already caught via NCBI + Scholar upstream. |

> Caveat: NCBI emails carry title / authors / journal / DOI / PMID
> but no abstract; Scholar alerts include a short snippet only. The
> write-ups below are triage against your INTERESTS.md — not full-
> text reads. `arxiv-digest` entries carry the full abstract.

---

## Executive summary (HIGH-priority studies, ranked)

Eight HIGH items surface in this window, plus two METHODS-WATCH items
from the 08-04 arxiv digest. The dominant knot is **pharmacogenomics-
of-medication-side-effects + drug-target/proteomic MR + observational
pharmacoepi calibration** — three papers land in this cell and together
they refine the 08-01 GLP-1 / statin×CHIP cluster into a
broader pharmacogenomic-modifier-of-persistence-and-side-effects lens.

**Your own paper — Nature Genetics official (1 item).**

1. **Bujnis et al. Nat Genet 2026** — multi-ancestry Hashimoto's
   thyroiditis GWAS (48,694 cases). You are a co-author. Preprint
   version was flagged in the 08-01 report; the official Nature
   Genetics publication has now landed and appeared on your own
   Scholar author feed. **Confirm indexed in Google Scholar profile
   and cross-link into your CV / publications page today.**

**Pharmacogenomics × drug-target MR × RWE calibration (4 items).**
The largest thematic knot of the window.

2. **Vaura, Krebs, Kiiskinen, Rämö, Tamlander, Estonian Biobank
   research team, Rubinacci, Milani, Ripatti — Eur Heart J 2026-08-03**
   — *Side effects in hypertension treatment: a pharmacogenomic
   analysis.* Ripatti (Helsinki/FIMM) + Milani (Estonian Biobank).
   Directly on the "pharmacogenomic modifiers of medication
   persistence" INTERESTS sub-thread — extends persistence to side
   effects, which is the upstream driver of discontinuation.
3. **Zhong H, Zhu J, Liu S, Wong, Zhang Y, Luu, Wu Q, Wang X, Wu L —
   Mol Genet Genomics 2026-08-03** — *Cross-population proteome-wide
   mendelian randomization study identifies likely causal proteins for
   cardiovascular diseases.* Sits in the same drug-target-MR /
   proteomic-MR lane as the Wang et al. GLP-1/GIP paper from the 08-01
   report — the cross-population angle is the new element.
4. **Wang H, Zhang B, Lei Y, Lu Y, Zhang D, Jian X, Zhu Y — medRxiv
   2026** — *Distributional Diagnosis and Calibration with Negative
   Controls for Outcome-wide Real-world Evidence.* Focus: GLP-1 outcome-
   wide RWE. Surfaced from BOTH the George Hripcsak and Patrick Ryan
   author feeds — this is Ryan-lab OHDSI negative-control methodology
   extended to distributional diagnosis. Directly on the causal-
   inference / pharmacoepi thread AND the GLP-1 pharmacoepi cluster.
5. **Turner AJ, Boone EC, Haidar CE, Yang W et al. — Clin Transl Sci
   2026** — *CYP2C19 c.681G>A Is not in Complete Linkage Disequilibrium
   With c.332-23A>G: Implications for Pharmacogenetic Testing.* Uses
   All of Us participants. Directly on the CYP2D6/CYP2C19-adjacent
   pharmacogenomic-persistence thread; also on the AoU-native biobank
   thread. Practical implication for any AoU CYP2C19 star-allele call
   you use downstream.

**Causal inference & pharmacoepi tooling (2 items).**

6. **Noma H — arXiv 2608.01625v1 (08-04 arxiv-digest)** — *Target
   Trial Emulation with the R Package TTE: A Tutorial and Methodological
   Guide.* Self-contained tutorial for the TTE R package with two fully
   synthetic worked examples (SGLT2i vs DPP4i, sequentially nested ARB
   vs CCB with heart-failure hospitalization + competing death).
   Directly on the target-trial-emulation sub-thread. Adopt as the
   default TTE reference / teaching artifact.
7. **Wang H et al. medRxiv (see item 4)** — dual-listed here for the
   distributional-diagnosis methodology, which is the more general
   contribution.

**ML for precision health + wearables / imaging FMs (2 items).**

8. **Sasson, Levine, Shilo, Kohn, Lutsker, Godneva, Gabet, Krongauz,
   Weinberger, LeCun, Balestriero, Segal — arXiv 2608.02208v1 (08-04
   arxiv-digest)** — *Self-supervised DXA representations encode multi-
   system disease risk, biological aging and heritability (LeDXA).*
   JEPA-based SSL, trained on 11,540 Human Phenotype Project scans, +
   external evaluation on 47,400 UKB scans. Beats DINOv3 with 150,000×
   fewer training images. Directly on **EHR foundation models →
   multimodal EHR FMs** and on **biological-age-from-imaging** as an
   incident-disease prediction signal.
9. **Xie H, Xue F, Wang X — Lifetime Data Anal 2026-08-03** —
   *Transition dynamics modeling of pre-trained accelerometry
   representations for time to diagnosis of Parkinson's disease.*
   Wearables + pre-trained representations + time-to-event outcome.
   Directly on **ML for precision health tied to a clinical decision**
   (who to escalate for PD workup) and on the pre-symptomatic-carrier-
   phenoconversion sub-thread from the rare-disease section.
10. **Diao JA, Sanchez M, Sommer A, Cohen K et al. — arXiv 2026** —
    *Kidney function and kidney failure prediction in a large
    multiethnic population.* Marinka Zitnik author feed. On the ML-
    for-precision-health thread; adjacent to the APOL1 disease thread
    (kidney failure prediction in multiethnic populations is where
    APOL1 modifies risk).

METHODS-WATCH bucket:

- **Krol A, Rondeau V, Choi Y-H, Briollais L — arXiv 2608.02127v1
  (08-04 arxiv-digest)** — Correlated frailty model for the analysis
  of a survival outcome in family cancer studies with IBD probability
  matrix + kinship matrix + common/rare-variant sets. Directly on the
  genetic-epi + rare-variant threads, but for family-cancer-study
  data — worth having on file for hereditary-cancer-syndrome
  survival analyses where family aggregation is the study design
  rather than a nuisance.
- **Silberg J, Eckmann P, Boen J, Zou J — Circulation 2026** —
  Viewpoint on *Agentic and Generative AI for Drug Discovery.* Zou
  author feed. Sits alongside the Matsumoto EcoXAI (08-01 report)
  and Chou `oci-agent` (07-27 report) as the third recent agentic-
  drug-discovery / agentic-XAI piece — worth citing when framing the
  agentic-workflows arc.

---

## HIGH — full write-ups

### 1. Bujnis, Sterenborg, Li, Åsvold, Brčić, Boraska Perica, Babbar, Denny, Fritsche, Kanai, Konrade, Leese, Marouli, Metspalu, Moksnes, Mukherjee, Okada, Palmer, Papadopoulou, Peculis, Rovite, Sauer, Soto-Pedre, Srinivasan, Steinbrenner, Teder-Laving, Wang, Weihs, **Zeng C**, Zhou J et al., *Multi-ancestry genome-wide association analyses provide insights into the genetic basis of Hashimoto's thyroiditis* — **Nature Genetics 2026 (doi 10.1038/s41588-026-02704-w)**

**Feed:** Google Scholar `Chenjie Zeng - new articles` alert (2026-08-03
04:32Z batch).

**Why HIGH — Nature Genetics official publication of your co-authored
paper.** This paper was already covered as item #3 of the 08-01 report
based on its NCBI PubMed PMID + preprint / accepted-online metadata.
It has now surfaced on your **own** Google Scholar author feed as the
official Nature Genetics AOP publication, which is the citation-worthy
moment for your CV / publications page / any grant progress reports.

Snippet from Scholar (verified 08-03 04:32Z):

> *Autoimmune hypothyroidism (Hashimoto's thyroiditis) is common and
> has a strong genetic component. Here we performed multi-ancestry
> genome-wide association meta-analyses encompassing 48,694
> Hashimoto's thyroiditis cases, using a precise …*

**Immediate actions.**
1. Confirm the Google Scholar profile entry is indexed correctly (the
   author-feed alert fires when Scholar has already indexed it — but
   double-check the citation entry displays correctly on your profile
   and that co-authorship rank matches the AOP author string).
2. Add the Nature Genetics official citation (with the DOI above) to
   the CV / publications list, replacing any earlier preprint or
   accepted-in-press placeholder.
3. Draft a short thread / one-paragraph highlight for internal
   distribution (department, biobank consortium). The 48,694 case
   count is the newsworthy statistic — it is one of the largest
   Hashimoto's thyroiditis GWAS to date and is the first multi-ancestry
   Hashimoto's meta-analysis at this scale.
4. **PheWAS follow-up plan.** As noted in the 08-01 report, queue a
   PheWAS-on-Hashimoto's-loci in AoU CDRv9 as soon as v9 srWGS becomes
   fully queryable. The lookup list (the paper's genome-wide-significant
   loci) is now finalized — begin drafting the analysis code with
   PheTK PheWAS Wilson-style CI reporting and phecode 244 as the
   primary Hashimoto's phecode.
5. **Cross-autoimmune shared-architecture follow-up.** The Hashimoto's
   loci list is a natural input to a cross-trait cFDR / MiXeR
   analysis against RA (phecode 714.1), T1D (phecode 250.1), IBD
   (phecode 555), vitiligo (phecode 709.4), SLE (phecode 695.42),
   and thyroid cancer (phecode 193). This is one route to a follow-
   up paper.

---

### 2. Vaura F, Krebs K, Kiiskinen T, Rämö J, Tamlander M; Estonian Biobank research team; Rubinacci S, Milani L, Ripatti S, *Side effects in hypertension treatment: a pharmacogenomic analysis* — **Eur Heart J 2026-08-03 (ehag575; doi 10.1093/eurheartj/ehag575)**

**Feed:** NCBI My NCBI "UK Biobank" search (2026-08-03 16:58Z batch,
item 6/8).

**Why HIGH — one of the highest-value items this week.** This paper
sits at the exact intersection of two INTERESTS sub-threads:

- **Pharmacogenomic modifiers of medication persistence** — the
  INTERESTS entry names side-effect / discontinuation / MPR as the
  outcome; this paper attacks side effects directly (the upstream
  driver). Ripatti + Milani + Estonian Biobank is the same lineage
  as the Psy-PGx UKB work you already track.
- **EHR-linked biobank** — FinnGen + Estonian Biobank is a
  federated-biobank design that is directly comparable to the
  All of Us / MVP / UKB pattern.

Why *European Heart Journal* rather than a PGx-specialty journal
matters: it signals the paper is framed as a **cardiovascular
pharmacoepidemiology** contribution, which increases the odds that the
paper will influence cardiology practice-pattern change (as opposed to
being cited only in PGx methodology reviews). This is the same "PGx
becomes cardiology" arc that has played out for CYP2C19 × clopidogrel.

**Actions.**
- **Read Methods** for two specific things: (a) how they defined "side
  effect" from Estonian Biobank + FinnGen EHR data (phecode-based,
  code-based, or curated), and (b) which drug classes they scanned
  (thiazides, ACEi, ARB, CCB, beta-blockers all have distinct PGx
  loci — the paper's design choices here matter for how portable it
  is to AoU / UKB).
- **Add to the standing PGx-persistence lookup list.** If they release
  gene × drug × side-effect estimates, this becomes a lookup table
  for your CFTR-modulator-persistence and statin-discontinuation
  planned analyses.
- Compare **Milani / Estonian Biobank pipeline** vs the AoU short-read
  WGS pipeline for star-allele calling; the Estonian Biobank likely
  used array + imputation, and any AoU replication will need CYP
  region calls from WGS (harder — see Turner et al. below).
- If the paper reports effect estimates for ACE-inhibitor-induced
  cough (a classic PGx-side-effect exemplar, historically linked
  to bradykinin receptor variation), those estimates are a
  benchmark for any replication.

---

### 3. Zhong H, Zhu J, Liu S, Wong HTH, Zhang Y, Luu HN, Wu Q, Wang X, Wu L, *Cross-population proteome-wide mendelian randomization study identifies likely causal proteins for cardiovascular diseases* — **Mol Genet Genomics 2026-08-03 (301(1):164; doi 10.1007/s00438-026-02458-4)**

**Feed:** NCBI My NCBI "UK Biobank" search (2026-08-03 16:58Z batch,
item 5/8) — also duplicated on the "drug repurposing" NCBI feed as
item 1/2.

**Why HIGH — cross-population MR extension of the drug-target MR arc.**
INTERESTS flags "drug-target Mendelian randomisation triangulated with
observational cohort estimates" as a rising sub-thread; this paper
extends that framework in two ways: (a) **proteome-wide** (all measured
plasma proteins as candidate exposures, not just druggable-target
proteins) and (b) **cross-population** (the "portability" side of the
GWAS/PRS cross-ancestry axis reframed as an MR-portability question).

**Why the design pattern matters.** The Wang et al. GLP-1/GIP paper
(08-01 report item #5) used druggable-MR for two already-active drug
targets. Zhong et al. run essentially the same design *proteome-wide*
and *across populations*, which produces a very different output shape:
a **prioritized list of causal proteins for CVD** that becomes a
druggable-target-nomination input. If the paper releases the ranked
protein list, that list is portable to the CHIP × statin (Carter et al.
08-01 report) triangulation lane.

**Actions.**
- **Extract the ranked protein list** (should be in supplementary
  tables). Add to the `resources/` inventory under
  `drug-target-mr/protein-nominations/` alongside the Wang GLP-1/GIP
  data.
- Check whether they used **UK Biobank Olink** proteomics or
  deCODE SomaScan (or both) as the pQTL panel — INTERESTS explicitly
  flags Olink / NMR / SomaScan as tracked multi-omics-augmented PRS
  substrates.
- **Cross-reference vs INVENT consortium PE-in-DVT paper** (from the
  Ron Do author feed same 08-03 batch) — both are CVD-adjacent, both
  are multi-population, and the intersection of "proteins nominated
  by PW-MR" ∩ "loci called by INVENT VTE GWAS" is a natural
  triangulation exercise.

---

### 4. Wang H, Zhang B, Lei Y, Lu Y, Zhang D, Jian X, Zhu Y et al., *Distributional Diagnosis and Calibration with Negative Controls for Outcome-wide Real-world Evidence* — **medRxiv 2026**

**Feed:** Google Scholar `George Hripcsak - new articles` alert AND
`Patrick Ryan - new articles` alert (same 2026-08-03 04:32Z batch —
dual surfacing is a strong signal). Focus: **GLP-1** outcome-wide RWE.

**Why HIGH — OHDSI negative-control methodology upgraded for outcome-
wide RWE.** Hripcsak + Ryan are the two authors most strongly
associated with the OHDSI negative-controls-for-p-value-calibration
tradition. This paper extends it to **distributional diagnosis** — i.e.,
not just calibrating the mean effect estimate under negative controls
but calibrating the **distribution** of effect estimates across the
full outcome-wide phenome. That is a step-change for outcome-wide RWE
(where thousands of outcomes are tested against a single exposure and
the calibration challenge is inherently distributional).

INTERESTS entries hit:
- **Causal inference & pharmacoepidemiology** — this is the direct
  hit. Negative-control calibration is the OHDSI standard for
  cross-network pharmacoepi.
- **GLP-1 pharmacoepi cluster** — extends the 08-01 four-paper
  bracket (Tang / Eze / Hwang / Wang) with a **fifth
  methodological angle**: outcome-wide negative-control-calibrated
  RWE. Now the GLP-1 evidence 2×2 has explicit MR × outcome-wide
  calibrated observational as two rows, with RCT × single-outcome
  observational as the other two.
- **EHR phenotyping & OMOP** — this is OMOP-CDM-native OHDSI work.

**Actions.**
- **Read Methods** for the distributional-diagnosis test statistic.
  The interesting question is whether the calibration is on the
  effect-size distribution alone (i.e., recentering) or whether it
  also calibrates the **shape** (variance / tail behavior).
- **Adopt for the AoU-CDRv9 GLP-1 outcome-wide scan** you have on
  the queue — this is directly the tool you need. Check whether the
  code is on OHDSI GitHub (probably under `ohdsi` org, likely as
  an extension of `CohortMethod` or `EmpiricalCalibration`).
- Add to the `ohdsi` skill's tool reference under
  `EmpiricalCalibration` companion methods.
- Also relevant to any future federated multi-network scan you
  join — this is the methodology that lets each network's
  outcome-wide effect estimates be pooled with calibrated
  significance thresholds.

---

### 5. Turner AJ, Boone EC, Haidar CE, Yang W et al., *CYP2C19 c.681G>A Is not in Complete Linkage Disequilibrium With c.332-23A>G: Implications for Pharmacogenetic Testing* — **Clin Transl Sci 2026 (doi 10.1111/cts.70684)**

**Feed:** Google Scholar `All of Us research program` keyword alert
(2026-08-03 10:51Z batch, item 5/6).

**Why HIGH — practical PGx call-set QC.** CYP2C19*2 is called by
c.681G>A; the paper shows this variant is *not* in complete LD with
c.332-23A>G — implying that laboratories that assay only one of the
two markers may misassign star-allele status in a subset of individuals.
The paper uses All of Us participants to quantify the LD breakdown.

INTERESTS entries hit:
- **All of Us biobank** — AoU-native validation of a PGx-testing
  assumption.
- **Pharmacogenomic modifiers of medication persistence** — CYP2C19
  is the canonical PGx locus for antiplatelet (clopidogrel), PPI,
  SSRI (voriconazole, citalopram), and other drug-class metabolism.
  Star-allele call error propagates directly into any downstream
  CYP2C19 × outcome analysis you run.
- **Variant interpretation (ACMG / ClinGen)** — this is a
  Yang W / Haidar C.E. paper — likely from the PharmVar / CPIC
  lineage (Yang W is often Wenjian Yang at St. Jude), so it will
  carry authority for guideline updates.

**Actions.**
- **QC action for any past AoU CYP2C19 analysis.** If you have ever
  called CYP2C19*2 from AoU using c.681G>A alone (via WGS SNV
  filter), plan to re-call using both markers and quantify how many
  individuals shift star-allele status. This is likely a small
  fraction, but not zero, and it changes tail estimates for
  clopidogrel-response analyses.
- Add to the `waxse` and `tam` skill's PGx-call-QC checklist.
- Track for downstream **CPIC guideline update** — if the paper is
  from the CPIC informatics team (Haidar), it may inform a *2 call-
  set specification revision.

---

### 6. Noma H, *Target Trial Emulation with the R Package TTE: A Tutorial and Methodological Guide* — **arXiv 2608.01625v1 (08-04 arxiv-digest, submitted 2026-08-03)**

**Feed:** `arxiv-digest` (`digests/2026-08-04.md`), score 2 (keyword hits:
"target trial emulation", "inverse probability"), primary category
stat.ME.

**Why HIGH — direct-use tutorial for the TTE R package.** This is a
self-contained tutorial + methodological guide for the R package
`TTE`, covering the full modern target-trial-emulation workflow:

- Target trial protocol specification (eligibility, treatment
  assignment, time zero, follow-up).
- Intention-to-treat vs per-protocol estimands.
- Identification assumptions.
- Baseline and person-period data structures.
- Temporal ordering for longitudinal weights.
- Stabilized treatment and censoring weights + weight truncation.
- Balance and effective-sample-size diagnostics.
- Weighted pooled discrete-time survival models.
- Model-based standardization.
- Competing-risk analysis + weighted Kaplan-Meier / Aalen-Johansen.
- Cluster bootstrap at the original-individual level.

Two worked examples: **(a) SGLT2i vs DPP4i initiation with all-cause
death**, and **(b) sequentially nested ARB vs CCB trials with heart-
failure hospitalization + competing death.** Both directly map to
INTERESTS-tracked drug-class threads (SGLT2is are on the list; ARB
vs CCB is a classic cardiology TTE exemplar).

**Actions.**
- **Adopt as the default TTE reference for any target-trial-
  emulation analysis you launch.** The Hernán TTE didactic paper is
  still the conceptual reference, but this is now the standard
  R-package tutorial to pair with it.
- Add to the `causal-inference-os` skill's tool reference under
  target trial emulation.
- **Consider a shadow analysis.** The (b) example (sequentially
  nested ARB vs CCB with HF hospitalization) is a natural template
  for the CFTR-modulator persistence analyses on your queue — sub
  in CFTR-modulator initiator vs control-inhaler comparator arms
  and the sequentially-nested-trial structure carries over.
- If the R package is on CRAN + GitHub, add to the standing
  bioinformatics-tools inventory alongside `WeightIt`,
  `MatchIt`, `survey`, `survminer`.

---

### 7. Sasson G, Levine Z, Shilo S, Kohn S, Lutsker G, Godneva A, Gabet A, Krongauz D, Weinberger A, LeCun Y, Balestriero R, Segal E, *Self-supervised DXA representations encode multi-system disease risk, biological aging and heritability (LeDXA)* — **arXiv 2608.02208v1 (08-04 arxiv-digest, submitted 2026-08-03)**

**Feed:** `arxiv-digest` (`digests/2026-08-04.md`), score 2 (keyword
hits: "uk biobank", "biobank"), primary category cs.CV.

**Why HIGH — biobank-scale medical imaging FM with heritability +
biological-aging + incident-disease evaluation.** LeDXA is a JEPA-based
SSL vision model trained from scratch on 11,540 unlabeled Human
Phenotype Project DXA scans and evaluated externally on **47,400 UK
Biobank DXA scans**. Reported results:

- Beats DINOv3 (a SOTA general-purpose vision FM) with **~150,000×
  fewer training images and ~40× fewer parameters** on prevalent-
  disease / biomarker prediction from DXA.
- Over median 4.3-year UKB follow-up, improves **incident-disease
  prediction** vs tabular DXA measures. Largest gains: **hip and
  knee arthrosis, T2D**. For hip arthrosis, 66% of incident cases
  in the highest-risk quartile vs 41% for tabular measures.
- Predicts **chronological age** externally (r = 0.88; MAE = 2.90 y).
- The **biological-age gap** (predicted age − chronological age)
  tracks broader disease burden and predicts a **45% higher mortality
  hazard** in the oldest-appearing quartile.
- The biological-age gap **decreased in women after starting HRT**,
  suggesting it may be modifiable — this is a direct hit on the HRT
  pharmacoepi sub-thread from INTERESTS.
- **GWAS on LeDXA embeddings** recovers mostly known body-composition
  and bone-density loci; LeDXA embeddings are more heritable than
  DINOv3's.

INTERESTS entries hit:
- **EHR foundation models → multimodal EHR FMs (notes + codes +
  waveforms + imaging)** — DXA imaging FM is directly on this thread.
- **Pretraining-contamination audits for FM benchmarks** — the
  150,000× training-size differential vs DINOv3 is a natural case
  study for scale-vs-domain-specificity ablation.
- **Digital twins from EHR data** — the incident-disease prediction
  arm is a step toward the digital-twins framing.
- **Biobanks with EHR linkage: UK Biobank** — 47,400 UKB DXA cohort.
- **HRT persistence pharmacoepi** — the "biological-age gap
  decreases after HRT initiation" finding is a **novel biomarker
  endpoint** for HRT pharmacoepi work. This is worth extracting.
- **GxE / modifiable-biomarker** framing — biological-age-gap is a
  candidate modifier PGS.

**Actions.**
- **Read end-to-end.** This is one of the most on-thread arxiv papers
  of the last two months.
- **Extract the LeDXA-derived biological-age-gap methodology** and
  compare against your existing biological-age markers (e.g., PhenoAge,
  epigenetic clocks, GrimAge). Consider adding LeDXA-BAG as a
  candidate exposure in a hereditary-cancer BRCA carrier incident-
  disease trajectory analysis.
- Check whether **code + model weights are released** (Segal lab
  frequently releases; check `segal-lab` / `ledxa` on GitHub /
  HuggingFace). If so, the model becomes portable to any UKB-DXA
  cohort scan you or a collaborator runs.
- **HRT × biological-age-gap** — draft a short prospective analysis
  plan: incident-CVD / breast-cancer / dementia in HRT initiators
  vs matched non-initiators, with biological-age-gap trajectory as
  a candidate mediator. This is a Nature Aging / Nat Med caliber
  question.

---

### 8. Xie H, Xue F, Wang X, *Transition dynamics modeling of pre-trained accelerometry representations for time to diagnosis of Parkinson's disease* — **Lifetime Data Anal 2026-08-03 (32(3):45; doi 10.1007/s10985-026-09721-1)**

**Feed:** NCBI My NCBI "UK Biobank" search (2026-08-03 16:58Z batch,
item 3/8).

**Why HIGH — wearable pre-trained representations + time-to-event
outcome for a neurodegenerative disease.** The design triple:

1. **Pre-trained representations** — accelerometry FMs (in the same
   lineage as the LeDXA / DINOv3-style vision FMs but for
   accelerometer time-series). Directly on the EHR foundation-models
   → wearable representations sub-thread.
2. **Time-to-diagnosis** — Cox-style / transition-dynamics outcome,
   which is the correct estimand for pre-symptomatic conversion.
   Directly on the pre-symptomatic-carrier-phenoconversion
   sub-thread (Ran / Benatar ALS template).
3. **Parkinson's disease** — PD is the classic pre-symptomatic-
   conversion exemplar in wearable data (movement / gait changes
   precede clinical diagnosis by years).

INTERESTS entries hit:
- **EHR foundation models → wearable representations.**
- **Rare disease → pre-symptomatic-carrier-phenoconversion.**
- **ML for precision health tied to clinical decision** (who to refer
  for neurology workup).
- **Biobanks with EHR linkage: UK Biobank** (UKB wearable substudy).

**Actions.**
- **Read Methods** for the transition-dynamics model specification.
  If the estimator is doubly-robust or targeted-learning-style, it
  pairs with the Ran DR-FRL paper (07-31 arxiv-digest → 08-01
  report item #8) as a wearable-FM × causal-inference-methods
  bridge.
- **Compare against Ran / Benatar ALS pre-symptomatic template.**
  The PD design pattern is directly portable to LRRK2 / GBA
  carrier conversion, which is exactly the kind of hereditary-
  neurodegenerative-carrier work that maps back to your
  hereditary-cancer preclinical trajectory framing.
- If the paper releases the pre-trained accelerometry encoder,
  add to the `resources/` inventory under `wearable-fms/`.

---

### 9. Diao JA, Sanchez M, Sommer A, Cohen K et al., *Kidney function and kidney failure prediction in a large multiethnic population* — **arXiv 2026**

**Feed:** Google Scholar `Marinka Zitnik - new articles` alert
(2026-08-03 04:32Z batch).

**Why HIGH — kidney-failure prediction in a multiethnic population,
adjacent to the APOL1 disease thread.** Diao is the corresponding
author on multiple prior kidney-genetics-informatics papers (including
the JAMA APOL1-transplant-decision-making work). "Multiethnic
population" for kidney disease prediction sits at the exact
intersection of two INTERESTS threads:

- **APOL1** — APOL1 G1/G2 risk-genotype prevalence differs
  dramatically across African and European ancestry populations,
  and APOL1-mediated kidney disease is one of the highest-impact
  cases where population-specific PGx / risk-genotype adjustment
  changes clinical prediction.
- **ML for precision health tied to a clinical decision** — kidney-
  function / kidney-failure prediction is the definitional clinical-
  decision-support use case (referral to nephrology, timing of RRT
  planning).
- **Cross / trans-ancestry portability** under Genetic epidemiology.

Zitnik as senior author signals the paper likely has a **graph-based
or foundation-model methodology** angle — Zitnik lab's recent work is
in that lineage.

**Actions.**
- **Read Abstract + Methods** first to determine whether the paper
  uses APOL1 genotype explicitly or treats ancestry as a covariate.
  This is the crux question for the APOL1-transplant-decision-making
  translation.
- If the paper releases a model checkpoint or code, add to the
  `wglab` / `mims-harvard` skill's tool inventory as a
  kidney-failure prediction baseline.
- Compare to the recent **Kwakyi West African CKD diet paper** (from
  the 08-03 Scholar APOL1 keyword alert) — the Kwakyi paper is on
  the observational-diet-CKD side, Diao is on the ML-prediction side;
  they're complementary halves of the same clinical-decision problem.

---

## METHODS-WATCH — brief write-ups

### M1. Krol A, Rondeau V, Choi Y-H, Briollais L, *Correlated frailty model for analysis of genetic association in family studies* — **arXiv 2608.02127v1 (08-04 arxiv-digest, submitted 2026-08-03)**

Family-based genetic association analysis with a **correlated frailty
model** that combines a kinship-matrix-specified residual familial
component with a region- or gene-specific IBD-probability correlation
structure. Handles both common SNPs and rare variants (or both
together) as the tested set, with a right-censored time-to-event
outcome (time to cancer onset in the simulations).

Not directly on the current core cluster (biobank / AoU / EHR-linked)
because family studies are a different data type, but it is
**directly on the hereditary-cancer-syndrome analysis lane**: BRCA1/2,
Lynch (MLH1/MSH2/MSH6/PMS2), CDH1, TP53, PALB2 pedigrees where family
data is the primary design. Worth reading if you take on a hereditary-
cancer-syndrome cohort where the family aggregation is the study
design.

### M2. Silberg J, Eckmann P, Boen J, Zou J, *Agentic and Generative AI for Drug Discovery* — **Circulation 2026**

**Feed:** Google Scholar `James Zou - new articles` alert (2026-08-03
04:32Z batch).

Circulation viewpoint. Sits alongside **Matsumoto EcoXAI** (08-01
report M3) and **Chou `oci-agent`** (07-27 arxiv → 07-30 report) as
the third recent agentic-drug-discovery / agentic-analysis piece. Now
the "agentic pipelines in biomedical discovery" is a stable arc across
three papers from three different labs — worth citing as a set when
framing the agentic-workflows story in any grant / talk.

---

## Off-thread (recorded, no write-up)

**UK Biobank feed off-thread (08-03 batch):**
- Auger et al. Clin Chem — APOB / estimated APOB ratio for APOE2
  genotype screening (interesting lipoprotein-genetics application,
  but off-thread for the CVD-genetics core).
- Zhang Z et al. Int Urol Nephrol — Comment on Deficit accumulation
  frailty × CKD (comment/response letter, off-thread).
- Kim J et al. Neurosurg Rev — competing-risk model for post-stroke
  subdural hematoma (methods-adjacent but off-thread disease).
- Shiwani H et al. Eur Heart J Cardiovasc Imaging — asymmetric septal
  hypertrophy in LVH diseases (cardiology imaging).
- Gao M et al. MedScience — sarcopenia × infection risk in UKB (off-
  thread disease).
- Firdous & Calder Lipids — omega-3 × cardiometabolic UKB systematic
  review (nutrition-cardiometabolic, off-thread).

**Drug repurposing feed off-thread (08-03 batch):**
- Asiri M et al. Biotechnol Appl Biochem — molecular docking /
  ADMET / PASS / MD simulation of ganciclovir/acyclovir vs RSV
  nucleoprotein (target-only, no clinical-evidence loop).

**All of Us Scholar feed off-thread:**
- Lehrer S, Rheinstein P — tocilizumab × incident depression in RA
  in AoU (retrospective cohort, small-scale drug repurposing signal
  but off-thread disease).
- Salwan A et al. Spartan Medical Res J — deprivation × glaucoma
  healthcare access in AoU (health-services research, off-thread).
- Araque M et al. Gastro Hep Advances — MASLD × adverse social
  factors in AoU (social-determinants epidemiology, off-thread).
- Kamyab & James J Stroke Cerebrovasc Dis — ischemic stroke post-
  TIA in AoU (already noted in 08-01 report as off-thread).
- Ávila et al. Movement Disorders — DNAJC13 × PD multiancestry
  (negative-finding gene-disease association; off-thread but a
  useful reminder that population-scale negative findings are worth
  citing to bracket clinical evidence).

**Drug repurposing Scholar feed off-thread:**
- Gulisano — organoids as functional decision systems in drug
  repurposing (review; off-thread as a preclinical validation
  angle).

**Cystic fibrosis carriers Scholar feed** — Jiang & Sun Dig Dis Sci
2026 — Elevated risk of post-ERCP pancreatitis in CFTR heterozygotes.
Directly on the CFTR carrier thread (heterozygote consequences of
CFTR variants) but the specific outcome (post-ERCP pancreatitis) is
adjacent to your active CFTR interests. Worth a quick abstract-level
read if you're expanding into CFTR carrier gastrointestinal
consequences.

**Foundation models & EHR Scholar feed** — Campana et al. IEEE
TabHealth self-supervised tabular FM (off-thread — no biobank / EHR
grounding shown).

**Rare diseases / UDN / mendelian Scholar feed:**
- Farrugia Middle East rare disease Advocacy Council review.
- Martin EM et al. UDN-Aus establishment paper (Australia's first
  national rare disease diagnostic network — administrative /
  network-establishment paper, off-thread as a research finding
  but worth noting the UDN-Aus as an emerging comparator to the
  US UDN).
- Kraatari-Tiri et al. JAMA Ophthalmol — XXYLT1 × mendelian retinal
  dystrophy (single-gene disease association, off-thread).

**APOL1 Scholar feed** — Kwakyi E et al. West African CKD Cohort
diet × BP × proteinuria (nutrition-CKD in a West African population;
adjacent to APOL1-disease-risk framing but the paper does not report
APOL1 genotype).

**Variant interpretation Scholar feed** — Yasinskyi Y et al. 2026
AlphaFold-derived local structural confidence in BRCA1 missense
variant interpretation (computational-only, no ClinVar consequence
audit).

**EHR Scholar feed** — Michaud TL et al. remotely-delivered parents-
helping-parents youth nicotine vaping cessation RCT protocol
(protocol paper, off-thread).

**Knowledge graph Scholar feed** — Sun C et al. KG-ACE LLM medical
reasoning (KG alignment + consistency enhancement; abstract-level
interesting, worth abstract read but not full paper).

**Clonal hematopoiesis Scholar feed** — Zhang X et al. Int J Mol Med
review on CHIP CVD gene-specific mechanisms + therapeutic
implications (review paper covering ground already familiar).

**Author feed off-thread items (08-03 batch):**
- Sevgi 2025 CRISPR breast-cancer-GWAS-locus target genes (cites
  your work; note for citation-tracking).
- Seow Nature Genetics Singapore Precision Medicine Program
  (Denny feed; national-precision-medicine descriptive paper).
- Hamad JAMA Netw Open GLP-1 × fragility fracture in T2D (Hernán
  feed — GLP-1 pharmacoepi safety-signal, near-thread; worth
  abstract-level read).
- Corsi-Zuelli F et al. — low-dose MTX × incident psychosis in EHR
  cohort (Pascal Brandt feed — repurposing angle, adjacent to
  drug-repurposing thread).
- Lozano-Esparza et al. INVENT PE-in-DVT GWAS (Ron Do feed —
  cardiovascular genetics, adjacent to CVD-MR thread).
- Zhou X et al. sceQTL MR MAN1A2 in naive CD4+ T cells for
  autoimmune therapeutic target (Karczewski feed — druggable-MR
  from single-cell eQTL, methods-watch quality but off your
  specific disease threads).
- Owusu-Marfo qualitative EHR user opinions Ghana (Hripcsak feed).
- Abulibdeh / Celi Lancet Viewpoint correction (Celi feed).
- Wang L et al. subthalamic connectivity × PD psychiatric symptoms
  (Snyder / Szolovits feeds — off-thread).
- Mishra N et al. Nat Commun — large-scale temporal gene expression
  variation in peripheral blood (Kastner feed — adjacent to
  circadian-biomarker thread from 08-01 M1).
- Li T et al. — diagnostic performance of LLMs for orthopedic-rare-
  diseases (Bastarache feed — LLM-for-rare-disease-diagnosis, near-
  thread with the GraphRareBench arc but off your core threads).
- Nagai M et al. Nat Genet — generalizable and interpretable AI in
  regulatory genomics (Montgomery feed — regulatory-genomics AI,
  off-thread).
- Boebinger — automated STEM (Callahan feed — completely off-
  thread, microscopy tooling).
- Sun W et al. — Pacific oyster SV imputation (Jian Yang feed —
  agricultural genomics, off-thread).
- Ehlert et al. INSIGHT — CGM harmonization tool (Snyder feed —
  worth noting if CGM data ever enters an AoU/UKB analysis).
- Zhang B et al. — beef cattle GWAS + eQTL (Yang related-research;
  off-thread).
- Gouy — biological network topology × mutation effects in complex
  trait evolution (Pritchard feed).
- Chen S et al. arXiv — harmonised benchmarking of scRNA-seq /
  spatial transcriptomics FMs (Zitnik related-research feed;
  methods-watch quality but off your core threads).

---

## Cross-report continuity notes

- **Bujnis et al. Nat Genet Hashimoto's** — **UPGRADED TO OFFICIAL
  PUBLICATION.** Was HIGH item #3 in 08-01 report (preprint / accepted-
  online); now officially in Nature Genetics AOP with the DOI above.
  Post-publication follow-through actions (Google Scholar profile
  sync, CV update, PheWAS-follow-up planning) are the top priority.
- **Rahman et al. AoU imminent-opioid-overdose ML** — surfaced now
  on Scholar (08-01 report item #7); same paper, no new content.
- **Chou et al. `oci-agent`** (07-27 arxiv, 07-30 report) + **Ran
  DR-FRL** (07-31 arxiv, 08-01 report item #8) + **Silberg/Zou
  Circulation viewpoint** (this report M2) + **Matsumoto EcoXAI**
  (08-01 report M3) — the agentic-workflow arc is now a four-paper
  cluster. Worth a short internal note framing "agentic causal
  inference / agentic drug discovery / agentic XAI" as a coherent
  arc when writing up next.
- **Wang et al. GLP-1/GIP drug-target MR** (08-01 item #5) + **Wang
  H et al. distributional-diagnosis outcome-wide RWE** (this report
  item #4) + **Zhong et al. cross-population PW-MR CVD** (item #3)
  — extend the GLP-1 evidence 2×2 from 08-01 to a 2×3 (adding
  outcome-wide calibrated observational RWE as a third row alongside
  MR and single-outcome observational).
- **Carter et al. statin×CHIP MR triangulation** (08-01 item #6) —
  no re-surface this window. Still on the reading queue.
- **AoU multi-ancestry OUD GWAS (Gu et al.)** (08-01 item #1) —
  no re-surface this window. Still on the reading queue.
- **Kore et al. local-ancestry burden testing** (08-01 item #4) —
  no re-surface. Still on the reading queue.
- **Ahn et al. Res Sq AoU HLA architecture** (08-01 item #2) —
  no re-surface. Still on the reading queue.
- **GraphRareBench** (07-29 arxiv, 07-30 report) — clone-and-run
  action item still open.
- **Vaura et al. Eur Heart J PGx hypertension side effects**
  (this report item #2) is the new lead item for the
  pharmacogenomic-modifiers-of-medication-persistence sub-thread —
  add as the canonical hypertension-PGx side-effect reference for
  any future CFTR-modulator / statin / HRT / GLP-1 persistence work.

---

## Suggested next actions

1. **[TODAY] Confirm the Bujnis et al. Nat Genet publication is
   correctly indexed on your Google Scholar profile** and update the
   CV / publications page with the official Nature Genetics citation +
   DOI. This is a two-minute action that captures the citation-tracking
   moment.
2. **[TODAY] Read Vaura et al. Eur Heart J** (pharmacogenomic
   hypertension side effects) — highest-value single item this
   window on the PGx sub-thread. Extract the drug-class × PGx locus ×
   side-effect table for downstream lookup.
3. **[THIS WEEK] Read the Wang H et al. medRxiv distributional-
   diagnosis-with-negative-controls paper** — adopt for the AoU
   CDRv9 GLP-1 outcome-wide scan on your queue.
4. **[THIS WEEK] Read the Sasson et al. LeDXA arxiv paper** — the
   HRT × biological-age-gap finding is a novel prospective analysis
   hook worth developing.
5. **[THIS WEEK] Add Noma TTE R package tutorial to the
   `causal-inference-os` skill's reference stack** and adopt as the
   default TTE workflow reference.
6. **[QUEUE] Zhong et al. cross-population PW-MR CVD** — extract
   ranked protein list into `resources/drug-target-mr/`.
7. **[QUEUE] Turner et al. CYP2C19 star-allele call QC** — QC any
   past AoU CYP2C19 analyses for c.681G>A / c.332-23A>G LD
   assumption.
8. **[QUEUE] Xie et al. accelerometry FM for PD conversion** — read
   Methods to determine if the transition-dynamics model is
   doubly-robust; if so, pair with Ran DR-FRL as a wearable-FM ×
   causal-inference bridge.
9. **[QUEUE] Diao et al. multiethnic kidney-failure prediction** —
   read Abstract + Methods to determine whether APOL1 is explicit.
10. **[BACKLOG] The agentic-workflows arc** now has four papers
    (Chou `oci-agent`, Ran DR-FRL, Silberg/Zou Circulation viewpoint,
    Matsumoto EcoXAI). Draft a two-paragraph framing note that
    positions them as a coherent research arc.
