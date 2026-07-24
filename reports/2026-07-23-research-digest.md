# Research digest report — 2026-07-23

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-22 19:30Z → 2026-07-23 12:00Z** (roughly the 16 hours
since the last committed report at `reports/2026-07-22-research-digest.md`,
which closed with morning-of-07-22 alerts). This is a *narrow* daily
follow-on, not a multi-day catch-up — expect fewer HIGH items than
yesterday.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author-feed cluster) | 2026-07-22 19:31Z | Six author-feeds fired together — Denny (related + citations), Bastarache (related), Karczewski (citations), Chute (citations), Pritchard (citations), Shendure (related), Luo (citations). Two Denny hits dominate the on-thread signal (Baya AJHG polygenic-deviation + Gu AoU OUD GWAS). |
| Google Scholar alerts (keyword feeds) | 2026-07-23 01:59Z | Five keyword feeds — `phenome wide association studies`, `UK Biobank`, `All of Us research program`, `drug repurposing`, `variant interpretation`. Streit Nature Genetics BPD GWAS + BPD-PheWAS is the double-feed hit (surfaces in both PheWAS and UKB feeds); one high-signal MR pharmacoepi hit (Saxby metformin AAA). |
| NCBI "My NCBI What's New" ("All of Us", "UK Biobank") | 2026-07-23 05:09Z, 11:53Z | Two NCBI batches — AoU (9 items) with three on-thread hits (Lemieux JAMIA Open EHR interoperability, Żebrowska circadian GWAS+PheWAS+MR, Johnson AoU genomic healthcare disparities), UKB (26 items) with two additional on-thread hits (Wu integrative UKB rare-variant metabolic syndrome, Wang RFC1-CANVAS + PRS). |
| `arxiv-digest` repo (`digests/2026-07-23.md`) | 2026-07-23 (10:30Z cron) | 2 papers surfaced, 3 previously-seen suppressed; both new papers are score-1 (single keyword hit). Neither is strongly on-thread — a bioKG annotation-prioritization framework and a genomic-language-model TF-binding interpretability paper. Both bucketed as METHODS-WATCH. |
| bioRxiv / medRxiv Subject Collection Alerts | 07-22 → 07-23 daily | Aggregate feeds — individual papers surfaced upstream via Scholar / NCBI. Not a separate net. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it.

---

## Executive summary

- **Polygenic deviation as a rare-disease discovery lever — AJHG.**
  Baya, Lassen, Hill, Venkatesh, Currant et al., *Individuals who deviate
  from polygenic expectation are enriched for damaging variants in
  genes linked to rare disease* (Am J Hum Genet 2026; Denny
  related-research feed). Formalizes "misaligned" individuals (phenotype
  observed − phenotype predicted from PGS) as an enrichment strategy
  for pathogenic rare variants — a natural inversion of the standard
  PRS-tail approach and directly parallel to the Souaiaia et al.
  *Nature* PRS-tails paper cited in the 06-20 report and the Vazquez
  *Genetics* low-risk-groups paper flagged in the 07-22 report. **HIGH
  — read first.**
- **First multi-ancestry AoU GWAS of opioid use disorder with a
  deep-learning functional annotation layer.** Gu, Petrovitch, Hall,
  Lambert, Kember et al., *Genome-Wide Association Studies and
  Deep-Learning Functional Annotation of Opioid Use Disorder across
  Three Ancestries in the All of Us Research Program* (medRxiv 2026-07-15;
  Denny related-research feed). Extends OUD genetic architecture beyond
  European samples in AoU — a template for the class of AoU-native,
  multi-ancestry, EHR-derived phenotype GWAS your PheWAS threads should
  be tracking. **HIGH.**
- **The Nature Genetics BPD GWAS + biobank PheWAS follow-up — double-feed
  hit.** Streit, Awasthi, Hall, Braun, Niarchou et al., *Genome-wide
  association analyses of borderline personality disorder identify 11
  loci and highlight shared risk with mental and somatic disorders*
  (Nature Genetics 2026; PheWAS keyword feed **and** UK Biobank keyword
  feed). 11 novel loci; BPD-PGS PheWAS in **Vanderbilt BioVU + UK
  Biobank** shows shared risk with COPD and other somatic conditions.
  Niarchou on the author list places this squarely in the BioVU
  phecode-PheWAS lineage. Serves both the PheWAS thread and the
  genetic-epi thread. **HIGH.**
- **DRIVE v3 — Bastarache-lab IBD haplotype clustering at biobank
  scale.** Baker, Chen, Evans, Scartozzi et al., *DRIVE v3: Command
  Line Application for Identity-by-Descent Haplotype Clustering in
  Large Biobank Scale Data* (Genetic Epidemiology 2026; Bastarache
  related-research feed). Multi-individual IBD + phenotypic-enrichment
  tool for shared-haplotype discovery — a piece of biobank-scale
  genetic-epi infrastructure directly aligned with the BioVU
  penetrance-and-shared-haplotype work your infrastructure thread
  tracks. **HIGH.**
- **UK Biobank exome-wide rare-variant scan for metabolic syndrome at
  n = 367,188 (78,300 cases).** Wu, Sang, Xu, Zhan, Yuan, Ge, Yu et al.,
  *Integrative exome sequencing and multi-omics analysis elucidates
  the regulatory role of rare variants in metabolic syndrome*
  (Functional & Integrative Genomics 2026; NCBI UKB feed). Single-variant
  + gene-based rare-variant burden framing on the UKB WES. Bears on
  the pLoF-burden methods thread and gives a cardiometabolic template
  worth cribbing for CFTR / APOL1 / BRCA carrier PheWAS design. **HIGH.**
- **Circadian Imbalance Index: GWAS + PheWAS + MR triple in EBioMedicine
  — sole 07-23 hit in the AoU NCBI feed.** Żebrowska, Wielscher, Zhang,
  Saksvik-Lehouillier, DiMilia, Burns, Redline et al., *Genetic
  architecture of a Circadian Imbalance Index: genome-wide association,
  phenome-wide association, and Mendelian randomisation analyses*
  (EBioMedicine 2026-07-21; PMID 42481375; surfaces in **both** AoU and
  UKB feeds). Composite-trait GWAS → PheWAS → MR pipeline — the
  three-way framing your PheWAS + MR method thread has been pattern-
  matching. **HIGH.**
- **Multi-modal rare-disease functional landscape on 11,000 patients.**
  Uria-Regojo, Fernández-Caballero et al., *Dissecting the functional
  landscape of rare diseases through genomic variation in a
  heterogeneous cohort of 11,000 patients* (medRxiv 2026-06-10; Chute
  citation feed). Aggregated real-world clinical genomic data + HPO
  for data-driven reanalysis — directly on the rare-disease thread and
  the HPO / ontology thread. **HIGH.**
- **UK Biobank + East Asian cross-ancestry meta-analysis of 127 complex
  traits, n > 1M.** Jo, Khor, Chu, Ji, Ueno, Ono, Chen et al.,
  *Large-scale meta-analysis of over one million individuals reveals
  the genetic architecture of 127 complex traits in East Asian
  populations* (bioRxiv 2026-06-23; Denny related-research feed).
  Directly on the trans-ancestry portability sub-thread — pairs with
  the Kore et al. local-ancestry rare-variant burden paper from the
  07-22 report. **HIGH.**
- **RFC1-CANVAS + polygenic-modifier framing on GEL + UKB + Australian
  ataxia cohorts.** Wang, Fearnley, Davies, Snell, Lee et al., *DNA
  Repair Pathway Variants Are Enriched in Individuals with Biallelic
  AAGGG CANVAS and RFC1-Related Disease* (Movement Disorders 2026-07-22;
  NCBI UKB feed). Repeat-expansion carrier cohort × polygenic-score
  analysis — cleanly parallel to the composite-risk (PRS + rare
  pathogenic variant) framing you use for hereditary cancer and CFTR
  penetrance in AoU. **HIGH.**
- **JAMIA Open — national EHR interoperability for research.** Lemieux,
  Pfaff, Moffitt, Nakashima, Duncan, Galvez, Giannini, McMurry, Walden,
  Haendel, *From clinics to discoveries: harnessing national EHR
  interoperability for research* (JAMIA Open 2026-07-22; NCBI AoU
  feed). Reference-utility paper for the EHR-phenotyping / OMOP thread
  — Haendel on the author list places it in the N3C / OHDSI lineage.
  **HIGH (reference utility).**
- **Metformin & abdominal aortic aneurysm — MR + observational combined,
  drug-target MR.** Saxby, Stoma, Dudbridge, Samani, Bown, Nelson,
  *Evidence of a Protective Effect of Metformin on Abdominal Aortic
  Aneurysm Risk: Insights From an Observational Study and Mendelian
  Randomisation Analysis Using Putative Metformin Targets* (Ann Hum
  Genet 2026-07-23; NCBI UKB feed). Classic drug-target MR pattern
  applied to a repurposing candidate for AAA — clean template for the
  drug-repurposing sub-thread and pairs with the MR-ALasso methods
  paper from the 07-22 report. **HIGH.**
- **AoU cross-sectional genomic disparities cycle.** Johnson, Hite,
  Richmond, Lisi, Ainsworth, *Healthcare experiences and the cycle
  of genomic healthcare disparities: A cross-sectional study utilizing
  the 'All of Us' research program* (J Community Genet 2026-07-22;
  NCBI AoU feed). Pairs conceptually with the Sun et al. "target study
  within a target trial" disparities-estimand paper from the 07-22
  report; provides empirical AoU baseline data on healthcare-experience
  disparities. **MEDIUM-HIGH.**

Everything else in this window is either off-thread (breast-cancer
imaging discordance, Bombus subspecies population genomics, single-cell
integration methods, various UKB dietary-index → outcome papers), or
a methods-watch entry summarized below. The two `arxiv-digest`
papers today are both METHODS-WATCH-only (bioKG annotation
prioritization + genomic-language-model TF interpretability) — see
the tail section.

---

## Detailed reports

### 1. Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease

**Authors.** NA Baya, FH Lassen, B Hill, SS Venkatesh, H Currant et al.
**Venue.** *The American Journal of Human Genetics*, 2026 (Cell
Press S0002-9297(26)00200-4).
**Signal source.** Google Scholar author-feed for Joshua C. Denny —
new related research (07-22 19:31Z; top-of-feed hit).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (PRS + rare-variant
composite); variant interpretation (indirectly — enriches for
"actionable" damaging variants); rare disease.

**What the paper does (from title + snippet).** Formalizes the
concept of *misaligned* individuals — people whose observed
phenotype deviates substantially from the value predicted by their
PGS — and shows that the misaligned tail is **enriched for damaging
variants in genes linked to rare disease**. In other words: PGS
residuals are a discovery lever for pathogenic rare variants, not
just noise.

**Why it matters for your work.**
1. **Direct inversion of the standard PRS-tail design.** Instead of
   asking "who's in the top decile of PGS," this asks "who's
   further from their PGS-predicted phenotype than we'd expect?"
   — a natural approach for surfacing carriers of large-effect
   rare variants that the PGS misses by construction. Directly on
   the composite-risk (PRS + rare pathogenic variant) sub-thread
   inside genetic epi.
2. **Bridges the two "risk-tail" lineages you've been tracking.**
   Pairs cleanly with (a) the Souaiaia et al. *Nature* PRS-tails
   paper (06-20 report — top of the PGS distribution), (b) the
   Vazquez et al. *Genetics* low-risk-groups paper (07-22 report —
   bottom of the risk distribution), and now Baya (perpendicular
   to the PGS axis — deviation from prediction). Together the
   three papers give a full "tails-and-residuals" taxonomy of PGS
   as a discovery instrument.
3. **AoU / UKB applicability.** The design is portable to any
   biobank where PGS + rare-variant calls + phenotype are
   available — i.e. AoU, UKB, MVP, BioVU. A natural adjacent
   analysis would be to look at misaligned individuals in the
   ClinGen-actionable-gene subset (BRCA1/2, LDLR, KCNQ1, etc.)
   and quantify how much of the misalignment is explained by
   documented pathogenic variants.

**Follow-ups.** Pull the paper; check (a) which phenotypes were
tested, (b) the discovery cohort (UKB / FinnGen / AoU?), (c) whether
the enrichment holds for genes on the ACMG SF3.2 list specifically,
(d) their definition of "damaging" (LOFTEE HC pLoF? AlphaMissense
threshold? ClinVar P/LP?). Author panel (Currant, Venkatesh, Lassen)
overlaps with the Oxford / Christoffersen / Lindgren
UKB-exome-sequencing consortium — cross-check for possible companion
papers.

---

### 2. Genome-Wide Association Studies and Deep-Learning Functional Annotation of Opioid Use Disorder across Three Ancestries in the All of Us Research Program

**Authors.** S Gu, D Petrovitch, OT Hall, JW Lambert, RL Kember et al.
**Venue.** medRxiv, 2026-07-15 (2026.07.15.26358096).
**Signal source.** Google Scholar author-feed for Joshua C. Denny —
new related research (07-22 19:31Z; second hit in the batch).
**Bucket.** HIGH.
**Threads served.** Biobanks with EHR linkage (AoU); genetic
epidemiology (multi-ancestry GWAS); EHR phenotyping (OUD from EHR).

**What the paper does (from title + snippet).** Three-ancestry
GWAS of opioid use disorder in the All of Us Research Program —
explicitly framing the study as filling the European-population
bias gap in existing OUD genetic architecture — plus a
deep-learning functional annotation layer on the discovered loci.
Kember on the author list is the key link to the MVP OUD-GWAS
lineage.

**Why it matters for your work.**
1. **Template for AoU-native multi-ancestry GWAS on EHR-derived
   phenotypes.** OUD phecode / ICD extraction is nontrivial in AoU
   (chronic pain codes, opioid dependence codes, prescription
   histories), and the fact that the paper made it through says the
   phenotype-definition strategy is now stabilizing. Worth reading
   the methods section closely as a reference for any AoU-native
   phenotype-based GWAS.
2. **Deep-learning functional annotation is the interesting
   secondary layer.** If they used AlphaMissense / Enformer /
   Basenji-style deep-learning annotations to prioritize
   noncoding hits, that's a portable pipeline for other AoU
   phenotypes in your threads — CFTR carrier phenotypes,
   APOL1-carrier kidney phenotypes, hereditary cancer syndromes.
3. **Kember connection.** Overlaps with the MVP OUD-GWAS
   consortium — the AoU work here will likely become a
   discovery + replication partner for MVP, making this a good
   entry point into the multi-biobank OUD-GWAS reference class.

**Follow-ups.** Pull the PDF; check (a) OUD phenotype definition
(phecode 304.0? single-ICD? prescription-history-augmented?), (b)
ancestry inference method (PC-based? admixture-aware?), (c) which
deep-learning model was used for the functional annotation, (d)
overlap with MVP OUD GWAS loci.

---

### 3. Genome-wide association analyses of borderline personality disorder identify 11 loci and highlight shared risk with mental and somatic disorders

**Authors.** F Streit, S Awasthi, ASM Hall, A Braun, M Niarchou et al.
**Venue.** *Nature Genetics*, 2026 (s41588-026-02654-3).
**Signal source.** Google Scholar keyword feeds — surfaces in
**both** the "phenome wide association studies" feed and the "UK
Biobank" feed (07-23 01:59Z, top of both).
**Bucket.** HIGH.
**Threads served.** PheWAS/PheRS (BPD-PGS PheWAS in BioVU + UKB);
genetic epidemiology (largest BPD GWAS meta-analysis to date);
biobanks with EHR linkage.

**What the paper does (from abstract snippet).** Largest GWAS
meta-analysis of borderline personality disorder to date;
identifies 11 loci. **Phenome-wide analyses in Vanderbilt University
Medical Center Biobank (BioVU) and UK Biobank** using BPD-PGS
confirm associations with expected psychiatric phenotypes and also
identify associations with somatic conditions including obstructive
pulmonary disease. Niarchou on the author list is the BioVU /
Denny-lab connection.

**Why it matters for your work.**
1. **Direct BioVU + UKB PheWAS follow-up on a novel PGS.** This is
   the exact study design your PheWAS-of-a-major-locus /
   PheWAS-of-a-PGS reference-pattern thread has been pattern-matching
   — GWAS discovery + BioVU + UKB PheWAS follow-up, all in one
   *Nature Genetics* paper. Directly serves the "PheWAS
   infrastructure" thread.
2. **Shared risk with somatic comorbidities is a live topic.** The
   BPD ↔ COPD association (probably smoking-mediated) parallels the
   pattern of psychiatric-PGS → somatic-outcome findings that keep
   appearing (schizophrenia ↔ cardiometabolic, depression ↔
   cardiovascular). Cross-check whether they estimate a
   smoking-mediated indirect effect, which would tie back to your
   causal-mediation thread.
3. **Multimorbidity connection.** The "psychiatric-PGS predicts
   somatic-disease phecodes" pattern is a natural entry into the
   multimorbidity / disease-clustering thread — psychiatric PGS
   could be tested as a driver of latent-class assignments in
   cardiometabolic clustering work.

**Follow-ups.** Check (a) BPD phecode definition in BioVU (is it
phecode 301.21 or a bespoke code set?), (b) whether they release
BPD summary stats for external PheWAS, (c) UKB BPD phenotype
definition (which UKB field?), (d) the exact list of somatic
phecodes reaching significance in the BPD-PGS PheWAS.

---

### 4. DRIVE v3: Command Line Application for Identity-by-Descent Haplotype Clustering in Large Biobank Scale Data

**Authors.** JT Baker, HH Chen, GF Evans, AC Scartozzi et al.
**Venue.** *Genetic Epidemiology*, 2026 (gepi.70048).
**Signal source.** Google Scholar author-feed for Lisa Bastarache —
new related research (07-22 19:31Z; sole hit in the batch).
**Bucket.** HIGH.
**Threads served.** Biobanks with EHR linkage (BioVU
infrastructure); PheWAS/phecode infrastructure (multi-individual
IBD + phenotypic enrichment); genetic epidemiology.

**What the paper does (from snippet).** Command-line tool for
identity-by-descent (IBD) haplotype clustering at biobank scale,
with an integrated phenotypic-enrichment testing framework — i.e.
"find shared haplotypes carried by phenotype-enriched clusters."
Explicit gap-filling framing: existing IBD tools don't couple to
phenotype-enrichment testing. The author list (Baker, Chen, Evans,
Scartozzi) is squarely in the Bastarache Vanderbilt / BioVU orbit.

**Why it matters for your work.**
1. **Direct biobank-scale infrastructure piece.** DRIVE was one of
   the tools your infrastructure thread was already tracking; v3
   makes it CLI-ready for large biobanks — worth flagging as usable
   for AoU (where WGS is available for ~245k people) once the
   compute-cost profile is known.
2. **Bastarache-lab lineage places this in your PheWAS
   infrastructure toolchain.** Pairs with PheWAS (Denny-Bastarache),
   PheCodes / phecodeX (Bastarache), and now DRIVE (Bastarache-adjacent
   for IBD-driven phenotype discovery) — the same lab's tools
   composed together give an end-to-end "shared-haplotype → phecode
   enrichment" pipeline.
3. **Portable to hereditary-cancer founder-variant discovery.** IBD
   clustering on rare pathogenic-variant carriers is exactly how
   founder haplotypes get discovered — natural applicability to
   BRCA / MSH2 / APC founder work in AoU, since AoU's diverse
   cohort will have multiple founder populations underrepresented
   in gnomAD.

**Follow-ups.** Pull the paper; check (a) compute profile / memory
footprint at biobank scale, (b) input format (VCF? PLINK? BGEN?),
(c) whether the phenotypic-enrichment test uses phecodes
directly, (d) GitHub link and reproducibility.

---

### 5. Integrative exome sequencing and multi-omics analysis elucidates the regulatory role of rare variants in metabolic syndrome

**Authors.** CX Wu, J Sang, Q Xu, Y Zhan, SJ Yuan, YY Ge, XJ Yu et al.
**Venue.** *Functional & Integrative Genomics*, 2026 (PubMed
42472903).
**Signal source.** Google Scholar keyword feed — `UK Biobank` —
new results (07-23 01:59Z).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (rare-variant EWAS at
biobank scale); variant interpretation (regulatory rare variants);
UKB biobank thread.

**What the paper does (from snippet).** Exome-wide association
study in **367,188 UKB individuals** (78,300 metabolic-syndrome
cases + 288,888 controls). Single-variant analysis + gene-based
burden + integration with multi-omics data to characterize the
regulatory role of rare variants.

**Why it matters for your work.**
1. **Scale + design template.** ~370k UKB WES + single-variant +
   burden + multi-omics integration is the current reference
   design for rare-variant metabolic-trait discovery. Cleanly
   portable to CFTR-carrier cardiometabolic phenotypes, APOL1-carrier
   metabolic phenotypes, and hereditary-cancer-carrier metabolic
   comorbidities in AoU.
2. **Pairs with the LDL rare-variant work.** UKB WES burden testing
   on metabolic syndrome will overlap with lipid gene sets already
   in your reference class (APOB, PCSK9, LDLR) — worth checking
   the top burden-significant genes.
3. **Regulatory-variant framing is the interesting angle.** If the
   multi-omics integration recovers regulatory pLoF (5'UTR or
   promoter loss-of-function), that's a natural link to the
   LOFTEE / 5'UTR pLoF literature (Whiffin et al.) already in
   your variant-interpretation thread.

**Follow-ups.** Pull the paper; check (a) MetS phenotype
definition (ATP-III? IDF? phecode-derived?), (b) burden-test
method (SAIGE-GENE+? REGENIE burden?), (c) which multi-omics
layers were integrated (eQTL / pQTL / methylation?), (d) top
gene-burden hits.

---

### 6. Genetic architecture of a Circadian Imbalance Index: genome-wide association, phenome-wide association, and Mendelian randomisation analyses

**Authors.** M Żebrowska, M Wielscher, J Zhang, I Saksvik-Lehouillier,
L DiMilia, A Burns, J Valliere, L Vincenzi, S Redline, O Okereke, R
Saxena, R Richmond, MK Rutter, ES Schernhammer.
**Venue.** *EBioMedicine*, 2026-07-21 (in press; 106380). PMID
**42481375**.
**Signal source.** NCBI "What's new for 'All of Us' in PubMed"
(07-23 11:53Z) **and** NCBI "What's new for 'UK Biobank' in PubMed"
(07-23 11:53Z) — double-feed AoU + UKB.
**Bucket.** HIGH.
**Threads served.** PheWAS/PheRS (three-part GWAS → PheWAS → MR
pipeline); causal inference (MR arm); biobanks with EHR linkage
(AoU + UKB); multimorbidity (Circadian Imbalance as a
composite phenotype).

**What the paper does (from title).** Constructs a Circadian
Imbalance Index composite phenotype and runs the full
GWAS → PheWAS → MR triple — GWAS identifies the genetic
architecture, PheWAS characterizes downstream phenotype associations
across the phecode space, and MR tests directional causality
against candidate outcomes. Saxena on the author list (MGH /
Redline sleep-genetics group) plus Richmond (MR methods, Bristol)
place this squarely in the sleep-and-circadian genetic-epi
consortium.

**Why it matters for your work.**
1. **Reference implementation of the GWAS → PheWAS → MR pipeline.**
   This is exactly the composite-methodology framing your PheWAS
   + MR thread has been pattern-matching. The Circadian Imbalance
   Index is a composite-trait exemplar you can cite whenever
   proposing a similar pipeline for CFTR-modulator response, APOL1
   kidney phenotypes, or hereditary-cancer-related phenotypes.
2. **Composite-index construction methodology is portable.** How
   they defined "Circadian Imbalance Index" — inputs, weights,
   normalization — is a recipe for building composite phenotypes
   from EHR-derived signals (sleep codes + shift-work codes +
   ICD sleep disorders + medications) in AoU.
3. **AoU + UKB dual-feed suggests direct AoU replication.** The
   fact that NCBI's AoU search caught this paper implies the
   paper explicitly uses / references AoU data (either as
   discovery or replication) — worth reading the abstract for
   the exact biobank composition.

**Follow-ups.** Pull the paper; check (a) exact composition of the
Circadian Imbalance Index, (b) which biobanks were used for
GWAS vs. PheWAS vs. MR arms, (c) top phecode hits in the PheWAS,
(d) MR outcomes tested and which passed.

---

### 7. Dissecting the functional landscape of rare diseases through genomic variation in a heterogeneous cohort of 11,000 patients

**Authors.** G Uria-Regojo, L Fernández-Caballero et al.
**Venue.** medRxiv, 2026-06-10 (10.64898/2026.06.10.26355349).
**Signal source.** Google Scholar author-feed for Christopher G.
Chute — new citations (07-22 19:31Z; top of feed). Also surfaces
in Pritchard-related feed as a secondary hit.
**Bucket.** HIGH.
**Threads served.** Rare disease; HPO / ontology thread; variant
interpretation (data-driven reanalysis).

**What the paper does (from snippet).** Aggregates real-world
clinical genomic data on **11,000 rare-disease patients** and
develops a data-driven methodology for exploring disease
mechanisms + improving reanalysis of unsolved cases. Cites the
HPO consortium papers — squarely in the HPO-driven rare-disease
diagnosis lineage.

**Why it matters for your work.**
1. **Reanalysis-of-unsolved-cases framing is directly on-thread.**
   Rare-disease diagnostic reanalysis is one of the highest-value
   translational applications of the ACMG / ClinGen /
   variant-interpretation stack. This paper's 11k-patient cohort
   is at a scale where reanalysis pipelines can be benchmarked
   quantitatively (yield per year, variant-of-uncertain-significance
   → likely-pathogenic conversion rate).
2. **HPO-based framing bridges rare-disease and phenotyping
   threads.** The HPO-driven reanalysis logic parallels the
   Phenolyzer / Phen2Gene / PhenoSV toolchain from Kai Wang's lab
   already in your reference class (see wglab skill). Worth
   reading for methodological details on HPO propagation and
   phenotype-based gene prioritization.
3. **11k is a useful size benchmark.** Bridges the gap between
   single-center reanalysis studies (~100s of patients) and
   biobank-scale approaches (~100k+). Cite whenever proposing a
   reanalysis-yield sample size.

**Follow-ups.** Pull the paper; check (a) cohort provenance
(single national program? Multi-site aggregation?), (b) reanalysis
yield metric, (c) which HPO propagation rules were used, (d)
whether they benchmark against Exomiser / LIRICAL.

---

### 8. Large-scale meta-analysis of over one million individuals reveals the genetic architecture of 127 complex traits in East Asian populations

**Authors.** J Jo, SS Khor, SK Chu, Y Ji, K Ueno, A Ono, CW Chen et al.
**Venue.** bioRxiv, 2026-06-18 (posted 2026-06-23;
2026.06.18.730290).
**Signal source.** Google Scholar author-feed for Joshua C. Denny —
new related research (07-22 19:31Z; third hit in the batch).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (cross- / trans-ancestry
portability); biobanks with EHR linkage (East Asian biobank
consortium meta-analysis).

**What the paper does (from snippet).** Cross-ancestry
GWAS meta-analysis in East Asian populations across **127 complex
traits** with a combined n > 1M — explicitly framed as filling the
EUR-population bias gap in existing GWAS meta-analysis.

**Why it matters for your work.**
1. **Direct trans-ancestry-portability infrastructure.** GWAS
   meta-analysis at n > 1M in a non-EUR population is a scarce
   resource — pairs with the Kore et al. local-ancestry rare
   variant burden paper from the 07-22 report to give an
   ancestry-aware toolkit for downstream PRS portability tests in
   AoU (which has ~20% Asian participants).
2. **127 traits is a broad enough net for downstream MR / PheRS
   work.** If summary stats are released, this is a valuable
   instrument-selection resource for East-Asian-specific MR
   analyses — worth pulling to check the release policy.
3. **AoU / MVP relevance.** AoU's Asian subpopulation is
   underpowered for solo GWAS; using East Asian consortium summary
   stats for PRS transfer / weighted-sum tuning is a natural
   application.

**Follow-ups.** Pull the paper; check (a) constituent biobanks
(Biobank Japan? Taiwan Biobank? Korean Genome Epidemiology Study?),
(b) whether summary stats are publicly released and where, (c)
sample overlap with existing East Asian biobank consortia, (d)
which 127 traits are included.

---

### 9. DNA Repair Pathway Variants Are Enriched in Individuals with Biallelic AAGGG CANVAS and RFC1-Related Disease

**Authors.** X Wang, LG Fearnley, KC Davies, P Snell, S Lee et al.
**Venue.** *Movement Disorders* (Mov Disord Off J Mov Disord Soc),
2026-07-22 (PMID 42473260).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed"
(07-23 11:53Z; item 23).
**Bucket.** HIGH.
**Threads served.** Rare disease (RFC1 CANVAS is a recessive
repeat-expansion disorder); genetic epidemiology (polygenic
modifier of a monogenic disease); variant interpretation
(pathogenic-repeat carriers).

**What the paper does (from snippet).** Biallelic RFC1 AAGGG
carriers profiled in **Genomics England (GEL)**, **UK Biobank**,
and a replication Australian ataxia cohort. Polygenic-score
analysis tests whether DNA-repair-pathway variants are
enriched in biallelic AAGGG carriers with CANVAS-related disease.

**Why it matters for your work.**
1. **Direct rare-variant + PGS composite framing.** This is
   exactly the design pattern your CFTR / APOL1 / hereditary-cancer
   work uses — take a Mendelian-variant carrier cohort, then ask
   whether a *pathway-specific* PGS modifies penetrance /
   phenotype expression. RFC1 CANVAS is an interesting test case
   because it's recessive and DNA-repair-linked.
2. **GEL + UKB + Australian cohort is a reproducible template.**
   GEL for discovery (rare disease-enriched), UKB for
   population-level validation, and an external ataxia cohort for
   replication — a template you can transplant to CFTR-modulator
   response, APOL1 kidney penetrance, or BRCA hereditary-cancer
   penetrance.
3. **Pairs with the Baya AJHG paper (this report's #1).** Both
   land in the same day; both formalize the interaction between
   rare damaging variants and polygenic-score signal. Together
   they define the current frontier of composite-risk methodology.

**Follow-ups.** Pull the paper; check (a) which DNA-repair-pathway
gene set was used (POLE? MMR? BER?), (b) whether the PGS was
built from CANVAS-specific GWAS or from a general repair-pathway
prior, (c) UKB CANVAS carrier N and their phenotypic profile.

---

### 10. From clinics to discoveries: harnessing national EHR interoperability for research

**Authors.** J Lemieux, ER Pfaff, RA Moffitt, J Nakashima, R Duncan,
E Galvez, JP Giannini, JA McMurry, A Walden, M Haendel.
**Venue.** *JAMIA Open*, 2026-07-22 (2026 Aug issue; 9(4):ooag137).
**Signal source.** NCBI "What's new for 'All of Us' in PubMed"
(07-23 11:53Z; item 2).
**Bucket.** HIGH (reference utility).
**Threads served.** EHR phenotyping & OMOP; biobanks with EHR
linkage (national infrastructure).

**What the paper does (from title + author panel).** Perspective /
methodology paper on how to leverage national EHR interoperability
standards (FHIR, USCDI, C-CDA) for observational research. Author
panel is heavy on N3C / OHDSI figures (Pfaff, Moffitt, Haendel) —
the N3C data-harmonization + OMOP-CDM lineage.

**Why it matters for your work.**
1. **Reference-utility paper for the EHR-phenotyping thread.**
   Whenever you write an AoU manuscript and need a one-line
   citation for "national EHR interoperability enables
   research-grade phenotyping," this becomes the go-to citation.
2. **Haendel on the author list.** Haendel's MONARCH / OBO
   Foundry lineage places this at the ontology-integration
   crossroads — worth reading for how they map FHIR / USCDI
   codes to OMOP concepts, which is a persistent friction point
   in AoU work.
3. **N3C connection.** The N3C is one of the two US-scale EHR
   consortia (with AoU) that generates OMOP-CDM data at
   national scale. A perspective from N3C leadership on
   interoperability is worth reading before designing any
   cross-cohort N3C + AoU study.

**Follow-ups.** Pull the paper; note (a) any specific
recommendations on OMOP concept mapping, (b) discussion of
FHIR-to-OMOP ETL, (c) governance / access-control model
recommendations.

---

### 11. Evidence of a Protective Effect of Metformin on Abdominal Aortic Aneurysm Risk: Insights From an Observational Study and Mendelian Randomisation Analysis Using Putative Metformin Targets

**Authors.** KL Saxby, S Stoma, F Dudbridge, NJ Samani, MJ Bown, CP Nelson.
**Venue.** *Annals of Human Genetics*, 2026-07-23 (ahg.70049).
**Signal source.** NCBI "What's new for 'UK Biobank' in PubMed"
(07-23 11:53Z; item 2).
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi (drug-target
MR); drug repurposing (metformin repositioning for AAA); genetic
epidemiology (Dudbridge on MR methods).

**What the paper does (from title).** Combines observational
(likely UKB EHR-derived) analysis of metformin exposure and
abdominal aortic aneurysm (AAA) incidence with a **drug-target MR
analysis using putative metformin targets** (probably
GDF15 / mTOR / AMPK-pathway instruments). Nelson on the author
list is the Leicester cardiovascular-genomics group, Dudbridge
is the MR methodologist.

**Why it matters for your work.**
1. **Textbook drug-target MR + observational triangulation.**
   The design — observational effect estimate + genetic
   drug-target instrument — is exactly the pattern your
   pharmacoepi + MR sub-threads use. Cite this whenever you
   discuss triangulating observational drug effects against
   MR instruments.
2. **Metformin repositioning is on-thread for drug
   repurposing.** Metformin has been proposed for AAA (via
   AMPK / inflammation modulation), aging (TAME), and cancer
   (many hypothesized indications). This is a rigorous
   test of the AAA hypothesis, and the metformin-repurposing
   literature is the drug-repurposing subthread's most-cited
   drug.
3. **Direct pairing with the MR-ALasso paper from 07-22.**
   The 07-22 report's Qasim/Wang/Bhatt MR-ALasso methods paper
   is the tool; Saxby et al. is a clean application of the
   drug-target-MR-with-triangulation design — the two papers
   together give you method + exemplar for the same design
   pattern.

**Follow-ups.** Pull the paper; check (a) which SNPs were used
as metformin-target instruments, (b) whether the observational
arm used UKB EHR-derived AAA cases (ICD-10 I71), (c) sensitivity
analyses for horizontal pleiotropy, (d) effect-size comparison
against observational estimate.

---

### 12. Healthcare experiences and the cycle of genomic healthcare disparities: A cross-sectional study utilizing the 'All of Us' research program

**Authors.** MD Johnson, A Hite, J Richmond, EC Lisi, HC Ainsworth.
**Venue.** *Journal of Community Genetics*, 2026-07-22 (17(4):88).
**Signal source.** NCBI "What's new for 'All of Us' in PubMed"
(07-23 11:53Z; item 5).
**Bucket.** MEDIUM-HIGH.
**Threads served.** Biobanks with EHR linkage (AoU); disparities /
equity in genomic medicine.

**What the paper does (from title).** Cross-sectional analysis in
AoU of self-reported healthcare experiences and their
relationship to genomic-medicine access / uptake — framed as the
"cycle of genomic healthcare disparities" (distrust → nonparticipation
→ underrepresentation → data gaps → less-generalizable tools →
distrust).

**Why it matters for your work.**
1. **Empirical baseline for AoU disparities work.** Pairs
   conceptually with the Sun et al. "target study within a
   target trial" disparities-estimand paper from the 07-22
   report — Sun gives the identifiability framework, Johnson
   gives the descriptive AoU baseline you'd cite before
   applying the framework.
2. **Uses AoU survey data + EHR data linkage.** AoU has
   extensive social-determinants-of-health survey data — this
   paper is a demonstration that the survey layer is usable for
   equity-focused research, not just genomic analyses. Useful
   template for social-genomics analyses in your reference class.

**Follow-ups.** Pull the paper; check (a) which AoU survey
instruments were used, (b) sample size and demographic
composition, (c) key associations reported.

---

## METHODS-WATCH (short entries)

### `arxiv-digest` 2026-07-23 — Plausibility-Driven Prioritization of Candidate Biomedical Annotations
**Authors.** E Cavalleri, M Alavinezhad, D Malchiodi, M Mesiti (q-bio.QM).
**Signal.** `arxiv-digest` today, keyword `knowledge graph`, score 1.
**Take.** Framework using biomedical knowledge graphs (bioKGs) to
prioritize automatically-generated biological annotations for expert
curation. Trains relation-specific binary classifiers with
community-based negative sampling; introduces plausibility measures
combining classifier confidence + reliability + semantic context.
Reports +5.8% balanced-accuracy improvement across five bioKGs. On
the KG thread but *upstream* of clinical use — this is a curation
tool, not a clinical-reasoning tool. **METHODS-WATCH** in case the
negative-sampling strategy is portable to HPO-based clinical KGs.

### `arxiv-digest` 2026-07-23 — Causal dictionary learning reveals and validates transcription-factor binding features in genomic language models
**Authors.** Sarwan Ali (q-bio.GN).
**Signal.** `arxiv-digest` today, keyword `foundation model`, score 1.
**Take.** Sparse-autoencoder interpretability + *causal* intervention
on genomic foundation models (Nucleotide Transformer, DNABERT-2)
to extract TF-binding features. The interesting methodological
contribution is the composition-matched negative-control protocol
that removes GC / repeat confounding — a standard pitfall in
motif-discovery interpretability that most papers ignore. Not
clinically on-thread but this is a template for how to make
interpretability claims on any biomedical foundation model (including
EHR FMs) more rigorous. **METHODS-WATCH** — the causal-ablation
validation logic is portable to CLMBR / MOTOR / MEDS interpretability
work.

### Non-infectious Uveitis PheWAS-adjacent in AoU
**Authors.** P Marella, V Subramanian, M Habiel (*Am J Ophthalmol*
2026-07-21; NCBI AoU feed).
**Take.** AoU phecode-based analysis linking non-infectious uveitis
to psychiatric comorbidities. Off-thread (specialty ophthalmology),
but a routine methods-only reference for AoU-based phecode-comorbidity
analyses. **METHODS-WATCH.**

### Predictive Value of Lipoprotein(a) and LPA Genetic Risk Score for Incident Sudden Cardiac Death
**Authors.** Y Li, W Hong, Y Li et al. (*Mayo Clin Proc* 2026-07-22;
NCBI UKB feed). **Take.** Standard PRS + biomarker composite
prediction in UKB — off-thread (SCD outcome), but an exemplar of
the PRS-plus-biomarker composite-prediction design pattern.
**METHODS-WATCH.**

### Impact of modifiable risk factors, including diabetes, and diabetes-related complications, on dementia risk in older U.S. adults: mutually adjusted estimates from a population-based cohort
**Authors.** A Wiggers, L Muthukumar, EL Reynolds et al. (*Diabetes
Res Clin Pract* 2026-07-22; NCBI AoU feed). **Take.** Standard
mutually-adjusted-risk-factor design applied to a population-based
US cohort — likely NHANES or AoU-adjacent. Off-thread but a
routine reference for adjustment sets in cardiometabolic-cognitive
analyses. **METHODS-WATCH.**

---

## Off-thread / SKIP (representative entries — not exhaustive)

- Multiple UK Biobank dietary-index → disease-outcome papers
  (vitamin K → ASCVD, dietary inflammatory index → cholelithiasis,
  triglyceride-glucose × obesity → aortic stenosis, remnant
  cholesterol × inflammation → frailty, plasma metabolomics →
  MASLD) — routine UKB nutrition-epi, no thread-crossover.
- Bombus subspecies population genomics, yellowtail kingfish
  phylogeography, snake phylogeography — animal-genomics feeds
  triggered on shared UKB / gnomAD reference infrastructure.
- Single-cell integration, single-cell lineage tree methods,
  Drosophila neuromodulatory neuron transcriptomics — off-thread
  from the Shendure / Pritchard feeds.
- Long-COVID clinical-trial systematic reviews — off-thread.
- Breast-cancer imaging-pathology discordance (Sfarad et al., *Ann
  Surg Oncol*) — direct match to Chenjie's breast-cancer background
  publications but off the *current* active-thread list (which is
  methods-heavy rather than clinical-oncology).

---

*Prepared 2026-07-23; next report expected once new signal
accumulates (typically 1–2 days). Full arxiv-digest for today is at
`digests/2026-07-23.md` (2 papers, both moderate signal).*
