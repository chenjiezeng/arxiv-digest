# Research digest report — 2026-09-06

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-06 12:40Z** (~5 days since the
last research-digest report, covering five arxiv-digest cron runs and
four Google Scholar alert batches plus medRxiv collection alerts and
JAMA Network updates).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-05.md`) | 09-01 → 09-05 daily crons | 5 daily runs. Dry days (0 papers): 09-03, 09-05. 09-01: 1 paper (Ghiasi storage-centric metagenomic dissertation, off-topic). 09-02: 1 paper (Ramesh mudskippers locomotion, keyword-hit noise). 09-04: 2 papers (Cortez-Rodriguez natural-disasters × nonprofits panel-DML, Yu et al. location-invariant extremal QTE for heavy-tailed distributions — METHODS-WATCH for causal-inference extreme-value theory). Window was quiet locally; volume was in Scholar alerts. |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads (pipeline commits to repo, not email). |
| Google Scholar alerts (09-06 batch, 06:02Z) | 09-06 06:02Z | ~30 feeds fired. Anchor items include DePaolo et al. *Eur Heart J* thoracic aortic disease PRS + gene variants (Bastarache feed), Bal et al. *Nat Cardiovascular Res* multiancestry HCM PRS (Denny feed), Perée et al. *Nat Commun* IBD eQTL + entrectinib repurposing (Denny, Montgomery, Pritchard feeds), Todorovic *PRO integration into OMOP* (Hripcsak feed), Jiang et al. EHR-FM → CDS (Hripcsak feed), Chin et al. *J Hum Immunity* temporal windowing for immunodeficiency phenotyping (Bastarache feed), Priya et al. *MASLD subtyping via EHR-linked genomic cohorts* (Bastarache 2-citation feed), Jing et al. *Trends in Genetics* large-scale human cohorts review (Yang feed), Dutta et al. *Cell Genomics* PRS + plasma proteomics for cancer, Zhang PRS-CARV (rare-variant-augmented PRS), Zhou et al. STAR Protocols admixed-population PRS on AoU. |
| Google Scholar alerts (09-04 batches, 16:08Z + 21:26Z) | 09-04 16:08Z / 21:26Z | ~40 feeds across the two batches. Anchors: Zhou et al. *Nat Mental Health* long-term cardiorenal trajectories after antihypertensive initiation in ADHD (706k Dutch cohort; Hripcsak feed), Alasfar et al. *Transplantation* APOL1 donor high-risk + collapsing FSGS (APOL1 keyword feed), Galderisi et al. CGM in CF youths before/after ETI (Ryan feed), Park et al. *Transl Psychiatry* cross-ancestry PRS transferability for OCD, DeVito & Gymrek *Nat Commun* nonlinear/interaction GxE for complex-trait prediction (Yang & Karczewski feeds), Chin et al. temporal-windowing sinusitis → immunodeficiency EHR classifier (Bastarache feed), Xi et al. AACAP EHR-based suicide-attempt prediction in Black youth (Brandt feed), Priya et al. MASLD subtyping (Bastarache 2-cite). |
| Google Scholar alerts (09-03 batches, 04:33Z + 13:02Z) | 09-03 | ~15 feeds. Anchors: Zhang et al. arXiv AoU wearable + PRS for incident MDD (Denny feed), Rajueni et al. medRxiv multi-biobank GWAS of dermatochalasis (Yang feed), Goto et al. Yamanashi Multi-omics Cohort (YMoC) study design (Zeng feed), Guo et al. *Genome Biol* germline SV calling benchmark (Montgomery feed). |
| Google Scholar alerts (09-01 batch, 11:36Z) | 09-01 11:36Z | ~10 feeds. Anchors: Zheng et al. medRxiv "Absorption and Co-expression Modules" — where polygenic and proteomic risk scores diverge in neurodegenerative diseases (fires under Zeng, Yang, Karczewski, and Denny — high concordance signal), Meng et al. bioRxiv sheep multi-tissue epigenomic atlas (off-topic), Tamandeh et al. *Genome* PPI network architecture of polygenic traits. |
| medRxiv Collection Alerts (09-01 → 09-06) | 5 daily alerts | Standing subscriptions to Allergy/Immunology, Endocrinology, Epidemiology, Genetic and Genomic Medicine, Health Informatics, Obstetrics/Gynecology, Pediatrics. Highlights: Yap et al. *Adjusting for medication use in GWAS and its impact on MR analyses: SBP in UK Biobank*; Pandey & Narasimhan *Field-of-view confounding in self-supervised cardiac-imaging genetic discovery*; Deslandes et al. *MR bridging diet and disease*; Das et al. *NLM manual vs. transformer study-design indexing*. |
| JAMA Network updates (09-01 → 09-04) | 9 messages | New Issue Sept 2026 (dapagliflozin AKI-post-cardiac-surgery, nicotine e-cig for smoking cessation, high-dose vitamin D3 in colorectal cancer), pragmatic trials, RSV/flu/COVID vaccine evidence for new respiratory season. Mostly clinical-trials / preventive-health content that adjacently touches pharmacoepi (dapagliflozin trial as an SGLT2i pharmacoepi anchor). |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. arXiv-digest entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced this window, clustering into six knots:

**PRS + rare variants / composite-risk cluster (5 items).** This window
was unusually rich in the tails-and-residuals / composite-risk framing
that `INTERESTS.md` prioritizes. DePaolo et al. *Eur Heart J* 2026 —
combined PRS × HTAAD-gene rare-variant analysis of thoracic aortic
disease prognosis, the canonical composite-risk design applied to
aortopathy. Bal et al. *Nat Cardiovascular Research* 2026 — multiancestry
PRS improves stratification in HCM patients whose SARC-P/LP variants
"explain only one-third of cases," a textbook direct-hit for "monogenic
disease modified by polygenic background." Zhang et al. **PRS-CARV**
(Research Square) — summary-statistics framework integrating
annotation-informed *rare* variants into PRS, portable to any cohort with
GWAS summary stats + functional annotations. Dutta et al. *Cell Genomics*
2026 — PRS for 21 cancers × 4,955 plasma proteins in cancer-free
individuals; trans-regulated protein networks as a PRS-mechanism decoder.
Wang et al. medRxiv 2026 — genomic + proteomic risk scores in diverse
populations, the ProRS + PRS integration paper feeding the multi-omics
PRS sub-thread.

**Pharmacoepi / target-trial-emulation cluster (3 items).** Zhou et al.
*Nat Mental Health* 2026 — 706,414 new users of antihypertensives in
Dutch register data, long-term cardiorenal trajectory comparison
stratified by ADHD; direct-hit new-user active-comparator design that
generalizes to any "prevalent condition × drug initiation" HTE question.
Kadesjö et al. *Lancet Diabetes* 2026 — SGLT2 ketoacidosis nested
case-control in Scandinavian cohorts, direct-hit for the SGLT2 drug
thread. Galderisi et al. 2026 — CGM tracking metabolic changes in CF
youths pre/post elexacaftor/tezacaftor/ivacaftor (Trikafta), direct-hit
for the CFTR-modulator disease thread, particularly the
modulator-persistence and metabolic-side-effects angles.

**Cross-ancestry / GxE genetic-epi cluster (2 items).** DeVito & Gymrek
*Nat Commun* 2026 — nonlinear and interaction effects of spatiotemporal
and nongenetic factors improve complex-trait prediction; directly serves
the "GxE and PGS × exposure interactions" sub-thread. Zhou et al. *STAR
Protocols* 2026 — protocol for leveraging local ancestry + cross-ancestry
genetic architecture to improve polygenic prediction in admixed
populations, using **All of Us** as the exemplar — direct-hit AoU +
cross-ancestry-PRS methods paper.

**IBD drug-repurposing (1 item).** Perée et al. *Nat Commun* 2026 —
cis-eQTL analysis in 27 sorted blood cell populations + 43 intestinal
cell types matches 140 IBD risk loci and nominates **entrectinib** as a
repurposing candidate. Serves the IBD disease thread AND the drug-
repurposing thread (KG/eQTL-driven with explainable mechanistic
rationale), which is exactly the "explainable hypothesis output" angle
`INTERESTS.md` prioritizes over opaque link-prediction pipelines.

**APOL1 disease thread (1 item).** Alasfar et al. *Transplantation* 2026
— Two-case series of donor APOL1 high-risk genotypes and early graft
failure with second-hit de novo collapsing FSGS. Direct-hit for the
APOL1 kidney-disease / transplant-decision thread; small-n case format
means METHODS-WATCH weight but direct-topic HIGH priority.

**EHR phenotyping / OMOP / representation cluster (5 items).** Chin et
al. *J Hum Immunity* 2026 — temporal windowing of recurrent sinusitis
episodes improves EHR-based immunodeficiency classification; direct-hit
for the temporal-representation sub-thread of `Knowledge representation
in EHRs`. Priya et al. 2026 — MASLD subtyping using EHR-linked genomic
cohorts revealing diverse etiologies and progression; direct-hit for
`Chronic disease clustering and multimorbidity` × `EHR phenotyping &
OMOP`. Todorovic *Integrating real-world PROs into OMOP CDM* — extends
the OMOP representation universe to PRO instruments, direct methods paper
for OMOP work. Jiang et al. 2026 — *Translating EHR-FMs into Clinical
Decision Support* — again fires this window (was flagged 09-01 batch
too), reinforcing the CDS-integration angle for CLMBR/MOTOR-lineage
foundation models. Jing et al. *Trends in Genetics* 2026 — narrative
review of large-scale human population cohorts, likely covers UKB / AoU
/ MVP / BioVU / national biobanks; positioning reference for the
biobanks thread.

---

## Detailed reports (HIGH items)

### 1. Zhou et al. — Long-term cardiorenal trajectories after antihypertensive initiation in ADHD vs. non-ADHD adults (Nature Mental Health 2026)

- **Authors:** Y Zhou, D Postmus, S Li, A van Lammeren et al.
- **Venue:** *Nature Mental Health* 2026 (doi: s44220-026-00718-1)
- **Source:** Google Scholar citations-to-Hripcsak feed (09-04 batch),
  cites Hripcsak's "Comprehensive comparative effectiveness and safety
  of first-line …" antihypertensive OHDSI paper.
- **Cohort:** Nationwide Dutch register data; 706,414 new users of
  antihypertensive medications (52.2% female, 18–90y), no prior CVD /
  CKD.
- **Design:** New-user active-comparator retrospective cohort study;
  the ADHD-status × antihypertensive-class interaction on cardiorenal
  trajectories over long-term follow-up.
- **Threads served:** Causal inference and pharmacoepidemiology
  (target-trial-emulation adjacent); ML for precision health
  (HTE by prevalent-condition modifier); Chronic disease clustering
  and multimorbidity (cardiorenal trajectories); PheWAS-adjacent
  outcome definitions.
- **Why it matters:** The design pattern is directly portable to your
  CFTR-modulator-persistence, statin-discontinuation, HRT-persistence,
  and GLP-1-RA-persistence questions — the "prevalent psychiatric or
  metabolic condition as an effect modifier of an initiated
  cardiovascular drug" scaffold with a 700k-person register substrate.
  The Hripcsak-lineage cite chain (OHDSI cohort methods → this paper)
  makes it a methods-transferable HIGH.
- **Bucket:** HIGH.

### 2. DePaolo et al. — Thoracic aortic disease: prognostic role of gene variants and polygenic risk scores (European Heart Journal 2026)

- **Authors:** J DePaolo, DT Smelser, D Guo, S Abramowitz, G Sisti et al.
- **Venue:** *European Heart Journal* 2026, advance article
  (ehag518/8778441).
- **Source:** Bastarache "new related research" feed (09-06 batch).
- **Design:** Combined evaluation of eleven HTAAD (heritable thoracic
  aortic aneurysm and dissection) genes with strong/definitive evidence
  plus a PRS, benchmarking their joint prognostic performance for
  incident/prevalent TAAD.
- **Threads served:** PheWAS / phecode infrastructure (penetrance
  estimation for monogenic variants under population-screening
  conditions); Genetic epidemiology (composite risk models stacking PRS
  with rare pathogenic variants); Variant interpretation (HTAAD ClinGen
  gene curation).
- **Why it matters:** Textbook direct-hit for "monogenic + polygenic
  jointly for a phenotype where classical Mendelian genes explain only
  a fraction." The paper's structure lets you cross-reference with your
  Bal-HCM (item 3) and Lichtenberger-MH (from the last digest) sisters
  for the "aortopathy / cardiomyopathy / pharmacogenetic phenotype"
  triptych of composite-risk designs.
- **Bucket:** HIGH.

### 3. Bal et al. — Multiancestry PRS improves stratification in HCM (Nature Cardiovascular Research 2026)

- **Authors:** HS Bal, A Pampana, A Nayak, M Gaonkar, S Patel et al.
- **Venue:** *Nature Cardiovascular Research* 2026 (s44161-026-00866-8).
- **Source:** Denny "new related research" feed (09-06).
- **Design/framing:** SARC-HCM-P/LP variants explain only ~1/3 of HCM
  cases; the paper builds a **multiancestry** PRS and shows it improves
  patient stratification beyond sarcomere-variant status.
- **Threads served:** Genetic epidemiology (cross-ancestry PRS
  portability; composite risk); PheWAS / penetrance (monogenic
  background modified by polygenic burden); Specific disease threads
  (cardiomyopathy adjacent to your CFTR/APOL1 monogenic-modulated-by-
  polygenic framings).
- **Why it matters:** Direct-hit for "portable, ancestry-inclusive PRS
  layered onto a Mendelian phenotype." Read alongside DePaolo TAAD for
  the two-disease composite-risk methods baseline the field is
  converging on.
- **Bucket:** HIGH.

### 4. Zhang et al. — PRS-CARV: summary-statistics framework integrating annotation-informed rare variants (Research Square 2026)

- **Authors:** Y Zhang, G Zhou, M Li, KK Ryckman, M Ray, C Scifres et al.
- **Venue:** Research Square preprint (rs-10671954).
- **Source:** Denny + Montgomery + Bastarache feeds (09-06).
- **Design:** Summary-statistics-based framework that fuses common-
  variant PRS with functional annotation-weighted rare-variant burden
  estimates, avoiding the requirement for a large sequencing training
  cohort.
- **Threads served:** Genetic epidemiology (composite risk models
  stacking PRS with rare pathogenic variants); PheWAS / phecode
  infrastructure (penetrance signal from rare-variant tails);
  Variant interpretation (annotation choices — LOFTEE / CADD /
  AlphaMissense — as PRS building blocks).
- **Why it matters:** Methods answer to "how do you PRS-boost a rare-
  variant signal without an in-house sequencing cohort?" Directly
  transferable to any of your CFTR / APOL1 / MH-RYR1 phenotype scaffolds
  where common-variant PRS exists but rare-variant sequencing depth is
  cohort-limited.
- **Bucket:** HIGH.

### 5. Dutta et al. — PRS × plasma proteomics identify cancer-related proteins and trans-regulated protein networks (Cell Genomics 2026)

- **Authors:** D Dutta, J Zhang, X Guo, R Quint, MR Rooney et al.
- **Venue:** *Cell Genomics* 2026 (S2666-979X(26)00184-9).
- **Design:** Integrates PRSs for 21 cancers with 4,955 plasma proteins
  measured in cancer-free individuals to identify cancer-related
  proteins and trans-regulated protein networks.
- **Threads served:** Genetic epidemiology (multi-omics-augmented PRS,
  Nightingale / Olink stacked with PGS); Rare disease / cancer
  syndromes (BRCA / Lynch adjacency); Pre-symptomatic carrier
  phenoconversion (proteomics trajectories in cancer-free carriers
  align with the Ran/Benatar template for ALS/BRCA).
- **Why it matters:** A large multi-cancer PRS × proteomics reference
  frame directly matching your "multi-omics-augmented PRS" sub-thread
  and providing candidate trans-regulated protein hubs to prioritize
  for CFTR / cardiometabolic / neurodegenerative reuse.
- **Bucket:** HIGH.

### 6. Wang et al. — Integrating genomic + proteomic data for complex-trait prediction in diverse populations (medRxiv 2026)

- **Authors:** W Wang, J Williams, MG Gillman, LM Raffield et al.
- **Venue:** medRxiv 2026.08.10.26360136.
- **Design:** Compares/combines PRS with proteomic risk scores (ProRS)
  for complex traits; explicit attention to diverse ancestry.
- **Threads served:** Genetic epidemiology (multi-omics-augmented PRS;
  cross-ancestry portability).
- **Why it matters:** Sister paper to Dutta et al. (item 5) that
  focuses on the *prediction*-side gain from adding proteomics to PRS
  in **diverse** populations — squarely on the AoU/UKB-Olink /
  Nightingale-NMR framing your INTERESTS section calls out.
- **Bucket:** HIGH.

### 7. Zhou et al. — Protocol for local-ancestry + cross-ancestry PRS in admixed populations, using All of Us (STAR Protocols 2026)

- **Authors:** G Zhou, I Yolou, Y Xie, H Zhao
- **Venue:** *STAR Protocols* 2026 (S2666-1667(26)00425-9).
- **Design:** Step-by-step protocol for building a polygenic-prediction
  model using admixed AoU participants; leverages **local ancestry**
  alongside cross-ancestry genetic architecture.
- **Threads served:** Biobanks with EHR linkage (AoU); Genetic
  epidemiology (cross-ancestry portability; local-ancestry-aware PRS);
  Pangenome-informed variant calling & downstream PGS portability
  (indirect: local ancestry is a reference-bias corrective).
- **Why it matters:** Direct-hit AoU + local-ancestry PRS **methods
  protocol** — reproducible substrate for any PRS-in-admixed-cohort
  analysis you would run in AoU.
- **Bucket:** HIGH.

### 8. DeVito & Gymrek — Nonlinear and interaction effects of spatiotemporal and nongenetic factors improve complex-trait prediction (Nature Communications 2026)

- **Authors:** R DeVito, M Gymrek
- **Venue:** *Nat Commun* 2026.
- **Design:** Models nonlinear and interaction effects between
  spatiotemporal / nongenetic covariates and genetic predictors for
  complex-trait prediction.
- **Threads served:** Genetic epidemiology (GxE and PGS × exposure
  interactions — the Nagpal & Gibson 2026 lineage); ML for precision
  health (HTE by environment).
- **Why it matters:** Direct-hit for the GxE + PGS × environment
  sub-thread called out in INTERESTS. Read with Nagpal & Gibson *Nat
  Genet* 2026 as the pair of "PGS × exposure interactions reshape
  portability" anchor papers.
- **Bucket:** HIGH.

### 9. Perée et al. — cis-eQTL in blood/gut identifies 140 IBD risk-locus matches and nominates entrectinib as repurposing candidate (Nature Communications 2026)

- **Authors:** H Perée, VA Petrov, Y Tokunaga, A Kvasz, F Farnir et al.
- **Venue:** *Nat Commun* 2026 (s41467-026-76672-4).
- **Design:** cis-eQTL analysis in 27 sorted blood cell populations
  and 43 intestinal cell types; overlaps with GWAS-identified IBD risk
  variants to prioritize genes whose expression is co-modulated by risk
  variants **and** the disease process — the operational definition of
  a preferred drug target. Nominates **entrectinib** (a TRK/ROS1
  inhibitor already approved for NTRK-fusion cancers) as a repurposing
  candidate.
- **Threads served:** Drug repurposing (KG/eQTL approach with
  *explainable* subgraph rationale — the exact angle INTERESTS
  prioritizes over opaque link-prediction pipelines); Specific disease
  threads (IBD); Genetic epidemiology (colocalization / eQTL
  fine-mapping).
- **Why it matters:** This is the drug-repurposing paper of the window.
  Explainable, cell-type-resolved, and disease-thread-aligned. If you
  want to prototype a repurposing signal for a cystic-fibrosis or APOL1
  target using the same cell-type-resolved eQTL scaffold, this is the
  methods template.
- **Bucket:** HIGH.

### 10. Alasfar et al. — Donor APOL1 high-risk genotypes and early graft failure (Transplantation 2026)

- **Authors:** S Alasfar, M Alanzi, E Cho, S Sridhara, H Me Me, L Fu et al.
- **Venue:** *Transplantation* 2026, abstract P4.810.
- **Design:** Two-case series of de novo collapsing FSGS after
  transplantation from donors with APOL1 high-risk genotypes,
  implicating a "second hit" activation of APOL1 nephrotoxicity.
- **Threads served:** Specific disease threads (APOL1 kidney disease
  and transplant decision-making); Rare disease (collapsing FSGS as
  an ultra-rare presentation); Ancestry considerations (APOL1
  ancestry-specific risk).
- **Why it matters:** Direct-hit for the APOL1 transplant thread
  called out in INTERESTS. Small-n case format is METHODS-WATCH-only,
  but the on-topic disease weight makes it HIGH for signal.
- **Bucket:** HIGH.

### 11. Kadesjö et al. — SGLT2 ketoacidosis in routine T2D clinical practice: Scandinavian cohort + nested case-control (Lancet Diabetes 2026)

- **Authors:** E Kadesjö, J Söderling, A Hviid, V Wintzell et al.
- **Venue:** *The Lancet Diabetes & Endocrinology* 2026.
- **Design:** Scandinavian cohort with nested case-control examining
  ketoacidosis risk under real-world SGLT2i use in T2D.
- **Threads served:** Causal inference and pharmacoepidemiology (SGLT2i
  drug thread; real-world evidence with attention to confounding);
  PheWAS / phecode-based outcome definitions.
- **Why it matters:** Direct-hit for the SGLT2 pharmacoepi drug thread.
  Register-based Nordic cohort with nested case-control is a
  reproducible-scaffold TTE-adjacent design; the ketoacidosis outcome
  complements your existing empirically-calibrated Hripcsak-lineage
  cardiovascular-outcome anchors.
- **Bucket:** HIGH.

### 12. Galderisi et al. — CGM tracking metabolic changes in CF youths before/after elexacaftor-tezacaftor-ivacaftor (2026)

- **Authors:** A Galderisi, H Marchiori, L Weiss, A ... et al.
- **Venue:** 2026 (CF endocrinology venue via Patrick Ryan feed).
- **Design:** Continuous glucose monitoring cohort of youths with CF
  before and after ETI ("Trikafta") initiation; documents metabolic
  changes.
- **Threads served:** Specific disease threads (Cystic fibrosis /
  CFTR modulator real-world outcomes); Causal inference and
  pharmacoepidemiology (before/after modulator initiation is a
  pre/post CFTR-modulator design close to the pharmacoepi sub-thread
  you already prioritize).
- **Why it matters:** Direct-hit for the CFTR-modulator real-world-
  outcomes disease thread; the CGM readout adds a wearable-signal
  layer to modulator-response phenotyping that complements the
  Ong et al. wearable-cardiometabolic paper (see METHODS-WATCH below)
  and the metabolic-side-effect concern for durable ETI persistence.
- **Bucket:** HIGH.

### 13. Chin et al. — Temporal windowing of recurrent sinusitis improves EHR-based immunodeficiency classification (Journal of Human Immunity 2026)

- **Authors:** AT Chin, R Mester, V Tozzo, AV Stephens et al.
- **Venue:** *Journal of Human Immunity* 2026.
- **Design:** Rule-based EHR phenotyping study that shows temporal
  windowing of sinopulmonary-infection episodes materially improves
  immunodeficiency classification over episode counts alone.
- **Threads served:** EHR phenotyping & OMOP (computable phenotype
  development with temporal windowing); Knowledge representation in
  EHRs (structural and temporal representation of the patient
  timeline — event sequencing choices, medication-exposure windows,
  temporal representation choices that leak or preserve label
  information at prediction time).
- **Why it matters:** Direct-hit for the temporal-representation
  sub-thread called out in INTERESTS. The "recurrent-episode temporal-
  windowing" heuristic is portable to any recurrent phenotype (recurrent
  UTI, recurrent MDD episodes, recurrent CF pulmonary exacerbations)
  where episode timing carries diagnostic signal that episode counts
  destroy.
- **Bucket:** HIGH.

### 14. Priya et al. — Subtyping MASLD using EHR-linked genomic cohorts reveals diverse etiologies and progression (2026)

- **Authors:** TS Priya, H Yan, KJ Wangensteen
- **Venue:** 2026 (via Bastarache 2-citation feed).
- **Design:** Chronic-disease subtyping using **EHR-linked genomic
  cohorts** — combines longitudinal EHR trajectories with genomic
  stratifiers to reveal heterogeneous etiologies and progression of
  metabolic-dysfunction-associated steatotic liver disease (MASLD).
- **Threads served:** Chronic disease clustering and multimorbidity
  (unsupervised subtyping); EHR phenotyping & OMOP; Biobanks with EHR
  linkage; Genetic epidemiology.
- **Why it matters:** Direct-hit for the multimorbidity /
  disease-trajectory-clustering thread applied to cardiometabolic
  disease with a genomic layer. The MASLD subtyping structure is a
  template you could import for CFTR-modulator responders vs.
  non-responders or APOL1-heterozygote-carrier CKD trajectories.
- **Bucket:** HIGH.

### 15. Todorovic — Integrating real-world Patient-Reported Outcomes into the OMOP common data model (2026)

- **Authors:** M Todorovic
- **Venue:** 2026 (via Hripcsak citations-to feed).
- **Design:** Methods/framework paper for encoding PRO instruments as
  OMOP-CDM entities so they can be used alongside conditions, drug
  exposures, and measurements in value-based-care evaluation.
- **Threads served:** EHR phenotyping & OMOP (extending OMOP's
  representational reach); Knowledge representation in EHRs (concept
  normalization for a modality — PROs — historically outside the OMOP
  core).
- **Why it matters:** Direct-hit for `Concept normalization and
  vocabulary mappings` sub-thread. If your target-trial-emulation and
  drug-persistence studies need PRO endpoints (fatigue for CF, kidney-
  disease-specific QoL for APOL1), an OMOP-native PRO representation is
  the missing piece.
- **Bucket:** HIGH (methodology).

### 16. Jiang et al. — Translating EHR Foundation Models into Clinical Decision Support (2026)

- **Authors:** Y Jiang, R Dai, Z Zhang, S Gao, Y Chen, Y Du, J Liu et al.
- **Venue:** 2026 (via Hripcsak "new related research" feed; note this
  paper *also* fired on 08-28, was flagged in the 09-01 digest as one
  of the Brandt EHR-FM cluster of four — this is a repeat surface).
- **Design:** Positioning paper on operationalizing EHR-FMs (CLMBR /
  MOTOR / MEDS / EHRSHOT lineage) into CDS; explicit focus on
  sparsity-handling in routinely collected clinical data.
- **Threads served:** EHR foundation models; Knowledge representation
  in EHRs (Applications to prioritize — care-gap identification,
  treatment-response prediction, adverse-event surveillance).
- **Why it matters:** Repeat surfacing across two consecutive digest
  windows suggests the CDS-integration angle is a rising sub-thread
  worth watching; already tracked in the 09-01 report — treat this
  citation as a reinforcement signal rather than a new item.
- **Bucket:** HIGH (already tracked; brief mention here).

### 17. Jing et al. — Trends in large-scale human population cohorts (Trends in Genetics 2026)

- **Authors:** X Jing, Z Yan, S Zhang, Y Zhao
- **Venue:** *Trends in Genetics* 2026.
- **Design:** Narrative review of foundational-infrastructure
  large-scale human population cohorts; integrates whole-genome
  sequencing with longitudinal EHRs across national biobanks.
- **Threads served:** Biobanks with EHR linkage (positioning
  reference).
- **Why it matters:** Useful citation anchor for a methods paper or
  grant intro that positions AoU / UKB / MVP / BioVU in the global
  biobank landscape. Skimming worth 20 minutes for the "biobank field
  map as of mid-2026" it likely provides.
- **Bucket:** HIGH-review.

---

## METHODS-WATCH items (brief)

- **Yap et al. medRxiv 2026** — *Adjusting for medication use in GWAS
  and its impact on MR analyses: SBP in UK Biobank.* Methods paper on
  a chronic source of bias in cardiometabolic MR (BP-lowering
  medication under-adjustment). Cite when writing methods for any
  drug-target-MR of an antihypertensive class.
- **Zhang et al. arXiv 2026** — *Longitudinal wearable monitoring +
  polygenic risk for incident MDD in All of Us.* Wearable + PRS +
  AoU + longitudinal — reads on-topic for the biobank/EHR-linked
  thread but the incident-MDD outcome is peripheral to your active
  disease threads. Worth citing as an AoU-wearable-linkage exemplar.
- **Yu et al. arXiv 2609.04018v1** — *Location-invariant estimator of
  extremal quantile treatment effects for heavy-tailed distributions.*
  Extends causal-inference into extreme-value quantiles; niche but
  potentially useful for rare-adverse-outcome pharmacoepi where the
  tail is where the harm lives.
- **Ong et al. 2026** — *Beyond Metabolic Syndrome: Expanded
  Cardiometabolic Phenotyping via Wearables.* Wearable-derived
  cardiometabolic phenotypes; complements the Galderisi CF-CGM paper
  (item 12) and the AoU-wearable-MDD Zhang paper above for the
  "wearable-signal phenotyping" bench.
- **Guo et al. Genome Biology 2026** — Benchmarking short-read germline
  SV calling; ensemble-of-tools wins, graph-genome alignment has small
  incremental impact. Cite for any SV-in-PGS or SV-in-rare-disease
  methods discussion.
- **Rajueni et al. medRxiv 2026** — Multi-biobank GWAS of
  dermatochalasis; useful cross-biobank meta-analysis exemplar.
- **Zheng et al. medRxiv 2026** — *Absorption and Co-expression Modules
  Show Where Polygenic and Proteomic Risk Scores Diverge in
  Neurodegenerative Diseases.* Fires across four author feeds
  (Zeng, Yang, Karczewski, Denny) — a strong concordance signal for
  the multi-omics-PRS sub-thread; already carried over from the 09-01
  batch but worth an eyeballed skim.
- **Pandey & Narasimhan medRxiv 2026** — *Field-of-view confounding
  in self-supervised cardiac-imaging genetic discovery.* Nice
  representation-audit paper for imaging-derived phenotypes; the
  "learned representation can leak site/scanner information into
  discovery" story is a portable QC template.
- **Saha et al. BMC Health Services 2026** — *Classifying and
  measuring stigmatizing / positive language at scale in EHRs.*
  NLP-on-clinical-notes methods; adjacent to the note-augmented
  phecode sub-thread.
- **Park et al. Translational Psychiatry 2026** — *Cross-ancestry and
  cross-disorder transferability of PRS for OCD.* Fires across
  Karczewski, Bastarache, Denny, Zeng feeds; solid cross-ancestry-PRS
  case study in a psychiatric phenotype.
- **Wang et al. medRxiv 2026** — *Whole-exome sequencing in OCD and
  chronic tic disorders identifies 36 large-effect risk genes.*
  Rare-variant discovery, off-thread disease but exemplary large-effect
  gene-discovery methodology.
- **Sherman et al. Human Genetics 2026** — *Underrepresented Voices in
  a Colorado Biobank.* Qualitative biobank-recruitment paper; cite
  for AoU / diverse-cohort inclusion framing.
- **Heudel & Blay ESMO 2026** — *Primary care physician documentation
  in oncology EHRs: prognostic marker or immortal-time bias?* Bias-
  identification piece for EHR-based oncology observational studies;
  useful as a teaching example.
- **Xi et al. AACAP 2026** — *Predicting Suicide Attempts via EHR in
  Black youth.* On-topic for the EHR-based-prediction bench in a
  minoritized-cohort context.
- **Cortez-Rodriguez arXiv 2609.04136v1** — *Natural Disasters and the
  Nonprofit Sector* (panel-DML causal design). Off-topic subject but
  methods-portable — panel DML in a policy-analytics setting.

---

## SKIP (noted for completeness)

- Ghiasi *Storage-Centric Genomic/Metagenomic Analyses* — systems /
  hardware, off-topic.
- Ramesh et al. mudskippers locomotion — keyword-hit noise (`motor`).
- Meng et al. sheep multi-tissue epigenomic atlas — non-human genomics.
- Various off-topic large-model / RL / audio-language / polymer /
  Drosophila / Staphylococcus α-toxin / spatial-omics papers that
  fired on the author feeds without matching an active thread.
- JAMA Network / JAMA Network Open general-issue TOC updates without
  a direct match to an active thread (dapagliflozin-AKI-post-cardiac-
  surgery, nicotine-e-cig, vitamin D3 CRC — noted for adjacent
  awareness).

---

## Notes on the arxiv-digest local runs this window

Five daily cron runs produced only four papers total (09-01 / 09-02 /
09-04), two of them keyword-hit noise (Ghiasi storage, Ramesh
mudskippers) and two on the boundary of causal-inference methods
(Cortez-Rodriguez natural-disasters × nonprofits panel-DML; Yu et al.
location-invariant extremal QTE). The arxiv-digest side of the feed
was quiet — Scholar alerts carried this window. No `arxiv-digest`
GitHub-notification email hits (the pipeline commits its output to the
local repo rather than emailing PR / cron notifications; the on-disk
digests *are* the arxiv-digest feed).

## Update note

Next research-digest report scheduled to be triggered by the next run
of this scheduled task. If any INTERESTS threads want re-weighting (e.g.,
elevate `Wearable + AoU + longitudinal` from METHODS-WATCH to a named
sub-thread — the AoU Zhang wearable-MDD paper and the Ong wearable-
cardiometabolic paper both fired this window), edit `INTERESTS.md` and
the next report will reflect the change.
