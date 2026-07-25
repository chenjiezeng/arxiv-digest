# Research digest report — 2026-07-25

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-23 12:00Z → 2026-07-25 12:00Z** (roughly the ~48 hours
since the last committed report at `reports/2026-07-23-research-digest.md`).
This is a two-day catch-up: the Scholar author-feed cluster fires on a
~48h cycle so the 07-24 09:02Z batch is the main author-alert dump; the
NCBI incremental batches from 07-23 11:53Z / 07-24 12:33Z fill in the
PubMed follow-ups; and the 07-25 03:27Z keyword-alert cluster is the
morning-of-07-25 keyword sweep.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author-feed cluster) | 2026-07-24 09:02Z | Fifteen author-feeds fired together — Denny (related + citations), Bastarache (related + citations), Karczewski (related + citations), Hripcsak (related + citations), Szolovits (related + citations), Zitnik (related), Callahan (related), Yang (related + citations), Baker (articles), Pritchard (citations), Ryan (related), Hernán (citations), Luo (citations), Natarajan (citations), Kastner (citations), Montgomery (related + citations), Xu (articles), Brandt (related), Zeng (related + **1 direct citation**). Three heavy on-thread hits — Bastarache-lab statin-response PGS + Duffy-null neutropenia correction; Layer-lab **GenoSiS** biobank genotype-similarity search; Ryan feed's SGLT2i-vs-GLP1 target-trial emulation. |
| NCBI "My NCBI What's New" ("UK Biobank", "drug repurposing") | 2026-07-24 12:33Z | Two NCBI batches — UKB (13 items) with two on-thread hits (Ye plasma proteomics for T2D liver outcomes; the residual is mostly UKB dietary-index / accelerometer / omics observational studies). Drug-repurposing batch was ~10 items dominated by traditional-medicine / oncology in-silico repurposing — no on-thread rare-disease or biobank-signal hits. |
| Google Scholar alerts (keyword feeds) | 2026-07-25 03:27Z | ~15 keyword feeds — `electronic health records`, `knowledge graph`, `Foundation models + electronic health records`, `APOL1`, `rare diseases`, `phenome wide association studies`, `All of Us research program`, `variant interpretation`, `drug repurposing`, `autoimmune disorders`, `intitle:"clonal hematopoiesis"`, `mendelian diseases`, `UK Biobank`. Two direct on-thread HIGHs — Hopper *Annual Review of Medicine* on APOL1 precision therapy, and Valle *The Oncologist* on CH interference in cfDNA liquid biopsy in a large VA veteran cohort. Two 07-23 items re-surface (Żebrowska Circadian Imbalance PheWAS, Johnson AoU disparities) — already covered in the 07-23 report; noted for reference and not re-detailed. |
| `arxiv-digest` repo (`digests/2026-07-24.md`, `digests/2026-07-25.md`) | 2026-07-24 → 2026-07-25 (10:30Z cron) | **07-24:** 1 paper surfaced (3 previously-seen suppressed); Ali *scContam* audit of pretraining contamination in single-cell foundation model benchmarks — score 1, `foundation model` hit. **07-25:** 0 papers surfaced (1 previously-seen suppressed) — the tightest cron output of the week. |
| bioRxiv / medRxiv Subject Collection Alerts | 07-23 → 07-25 daily | Aggregate feeds — individual papers surfaced upstream via Scholar / NCBI. Not a separate net. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it.

---

## Executive summary

- **DePinho *Nature Aging* review of TERT cites your telomere-length /
  cancer work — direct new citation to Chenjie Zeng.** DePinho, *Positioning
  TERT at the apex of aging* (*Nature Aging* 2026; s43587-026-01179-y;
  cites *Association between telomere length and risk of cancer and
  non-neoplastic diseases*). This is a first-author citation surfaced in
  the Zeng-cited-by feed — a Nature Aging perspective in the aging
  hallmarks program citing your telomere-length paper. **HIGH — track for
  reference-list check.**
- **GenoSiS — biobank-scale genotype similarity search for dynamic
  patient-matched cohort creation (Genome Research).** Schneider,
  Chowdhury, Tepper, Khan et al., *Biobank-scale genotype similarity
  search and dynamic patient-matched cohort creation with GenoSiS*
  (*Genome Research* 2026; Zeng related-research feed). Layer-lab-style
  infrastructure paper — SVS-based scalable vector search over genotype
  embeddings for on-the-fly cohort matching. Directly on the
  biobank-infrastructure sub-thread and pairs with the BioVU / AoU
  penetrance-and-shared-haplotype tools tracked in the DRIVE v3 entry
  from the 07-23 report. **HIGH.**
- **Bastarache-lab polygenic prediction of *non-goal* statin response —
  *Circulation: Genomic and Precision Medicine*.** Liou, García-González,
  Wu, Namba, Vaura et al., *Polygenic Prediction of Nongoal Response to
  Statin Therapy* (*Circ Genom Precis Med* 2026; Zeng related-research
  feed + Bastarache related-research feed). Uses PGS to identify
  individuals unlikely to reach guideline LDL-C targets on statin therapy
  — a treatment-effect-heterogeneity framing directly on the ML-for-
  precision-health thread and cleanly pairs with the DAPA-HF HTE paper
  from the 07-21 arxiv-digest. **HIGH.**
- **Correction to Shelley/Bastarache Duffy-null neutropenia
  penetrance-modifier paper — *Am J Hematology*.** Shelley, Shi,
  Bastarache, Chung, Mosley, *Correction to "Polygenic Variation
  Underlying Neutrophil Counts Modifies the Penetrance of Duffy-Null
  Neutropenia"* (*Am J Hematol* 2026; Zeng related-research feed). A
  formal correction to a BioVU polygenic-modifier-of-monogenic-penetrance
  paper — the pattern-of-work you track for CFTR / APOL1 penetrance
  design. **HIGH — pull the correction to check whether the corrected
  effect estimates change the modifier-of-penetrance headline.**
- **APOL1-mediated kidney disease precision-therapy review — *Annual
  Review of Medicine*.** Hopper, Wang, Olabisi, *APOL1-Mediated Kidney
  Disease and the Emerging Era of Precision Therapy* (*Annu Rev Med*
  2026-07-25; APOL1 keyword feed). Comprehensive review of the emerging
  APOL1-inhibitor / antisense-oligonucleotide / STAT-pathway
  therapeutic landscape — directly on the APOL1 disease thread and
  useful as a reference for the pharmacoepi / kidney-transplant sub-
  angle. **HIGH (reference utility).**
- **Clonal hematopoiesis interferes with cfDNA liquid biopsy in a large
  US Veterans cohort — *The Oncologist*.** Valle, Scobie, Rowe,
  Pritchard et al., *Interference of Clonal Hematopoiesis in cfDNA
  Liquid Biopsy Testing & Identification of Actionable Alterations in
  Large Diverse Cohort of US Veterans* (*The Oncologist* 2026-07-25;
  `intitle:"clonal hematopoiesis"` feed). CH-artifact filtering for
  cfDNA-based mCRPC actionable-alteration calling in the VA Precision
  Oncology / MVP-linked cohort — sits at the intersection of your CHIP/
  VEXAS thread, hereditary cancer thread, and the veterans-biobank
  (MVP) sub-thread. **HIGH.**
- **Ryan-feed target-trial emulation: SGLT2i vs GLP-1 RA for psoriatic
  arthritis in T2D.** Yen, Wang, Hwu, Chen, Hsu et al., *Comparative
  Risk of Psoriatic Arthritis in Type 2 Diabetes: An Emulated Target
  Trial of SGLT2 Inhibitors vs. GLP-1 Receptor Agonists* (*Drug Des
  Devel Ther* 2026; Ryan related-research feed). Directly on the
  active drug-class threads (GLP-1 RAs + SGLT2is) and provides an
  extra-cardiovascular-outcome benchmark for the emerging comparative-
  effectiveness literature. **HIGH.**
- **Denny-feed multi-ancestry PGS construction protocol — S4-Multi
  (STAR Protocols).** Lai, Tyrer, Baierl, Pharoah, Peng, *Protocol for
  constructing multi-ancestry polygenic models using S4-Multi* (*STAR
  Protoc* 2026; Denny related-research feed). Reference-utility PGS
  construction pipeline paper — directly on the trans-ancestry
  portability sub-thread of genetic epi, and cleanly pairs with the
  Jo et al. East-Asian meta-analysis of 127 traits from the 07-23
  report. **HIGH (reference utility).**
- **Karczewski-feed *Nature Genetics* infrastructure: blended
  genome+exome sequencing.** Boltz, Chu, DeFelice, Liao, Sealock et al.,
  *A blended genome and exome sequencing method captures genetic
  variation in an unbiased and cost-effective manner* (*Nature Genetics*
  2026; Karczewski related-research feed). New cost-optimized sequencing
  design that could reshape biobank sequencing economics — a piece of
  biobank-infrastructure worth tracking for AoU srWGS / lrWGS design
  decisions. **HIGH (infrastructure).**
- **Germline cancer risk alleles drive MDS *throughout adulthood* —
  *Leukemia*.** Walker, Koppayi, Carlelycke, Haribabu et al., *Germline
  cancer risk alleles drive myelodysplastic neoplasms throughout
  adulthood* (*Leukemia* 2026; Zeng related-research feed). Extends the
  known role of pathogenic/likely-pathogenic germline variants in
  pediatric MDS to adult MDS — directly on the hereditary-cancer × EHR
  thread and the CH/MDS lineage. **HIGH.**
- **UKB proteomics enhances liver-event prediction in
  prediabetes/T2D — *Diabetes, Obesity and Metabolism*.** Ye, Zhang,
  Ding et al., *Large-Scale Plasma Proteomics Enhances Prediction of
  Liver-Related Events Among Individuals With Prediabetes and Type 2
  Diabetes: A Prospective Cohort Study in the UK Biobank* (*Diabetes
  Obes Metab* 2026-07-23; NCBI UKB feed). UKB Olink-based proteomic risk
  stratification for MASLD/cirrhosis outcomes in the dysglycemia cohort
  — cardiometabolic multimorbidity thread. **MEDIUM-HIGH.**

Everything else in this window is either off-thread (UKB
dietary-index / accelerometer / obesity-omics observational studies,
oncology in-silico drug-repurposing, single-cell benchmarking without
EHR grounding), or a methods-watch entry summarized below. The 07-24
`arxiv-digest` paper (Ali scContam) is METHODS-WATCH only, and 07-25
was empty.

Two 07-25 keyword-feed items are **re-surfaces of 07-23 hits already
detailed in the previous report** and are not re-detailed here:
- Żebrowska et al. *Genetic architecture of a Circadian Imbalance
  Index: GWAS + PheWAS + MR* (EBioMedicine) — surfaced again on the
  07-25 `phenome wide association studies` feed. See 07-23 report,
  executive-summary bullet #5.
- Johnson et al. *Healthcare experiences and the cycle of genomic
  healthcare disparities in AoU* (J Community Genet) — surfaced again
  on the 07-25 `All of Us research program` feed. See 07-23 report,
  executive-summary bullet #10.

---

## Detailed reports

### 1. Positioning TERT at the apex of aging — cites your telomere/cancer work

**Authors.** RA DePinho.
**Venue.** *Nature Aging*, 2026 (s43587-026-01179-y).
**Signal source.** Google Scholar author-feed — **1 new citation to
articles by Chenjie Zeng** (07-24 09:02Z). The cited article is
*Association between telomere length and risk of cancer and
non-neoplastic diseases* (Zeng et al., first-author telomere-length ×
cancer paper).
**Bucket.** HIGH — direct citation to first-authored work.
**Threads served.** Chenjie's own publication citation graph;
adjacent to genetic-epi thread via the telomere-length lineage.

**What the paper does (from title + snippet).** *Nature Aging*
perspective by Ronald DePinho positioning telomerase reverse
transcriptase (TERT) as an upstream regulator coordinating multiple
hallmarks of aging in preclinical models — mitochondrial health,
epigenetic regulation, inflammation, stem-cell function — beyond its
canonical telomere-maintenance role. Reviews translational strategies
to modulate TERT, including restoration of physiological-range TERT
expression in mice and human cell models.

**Why it matters for your work.**
1. **Direct citation to your first-author telomere-length paper.**
   The `zeng-publications` skill catalogues the *Association between
   telomere length and risk of cancer and non-neoplastic diseases*
   paper as a core early-career output in the telomere / cancer
   epidemiology lineage. Being cited in a Nature-portfolio review by
   DePinho is a solid citation to know about — worth pulling to see
   which claim the review anchors on your work.
2. **Anchors the telomere → aging → cancer narrative that your work
   sits in.** Useful as a reference for future manuscript
   introductions on telomere-length epidemiology, and for grant
   Background sections that need a Nature-family review anchor for
   the TERT-as-aging-hallmark framing.
3. **Adjacent to the aging-hallmarks work.** DePinho's TERT review
   is a plausible companion citation for any current work bridging
   genetic epidemiology of aging biomarkers and cancer risk.

**Follow-ups.** Pull the DePinho review (Nature Aging paywall — use
institutional access). Check (a) which specific claim your paper is
cited to support, (b) whether the citation is in the aging / cancer
risk section or the mitochondrial-health section, (c) whether the
review positions telomere-length as a modifiable-aging biomarker
(implications for your PheWAS threads on aging).

---

### 2. Biobank-scale genotype similarity search and dynamic patient-matched cohort creation with GenoSiS

**Authors.** K Schneider, M Chowdhury, M Tepper, JB Khan et al.
**Venue.** *Genome Research*, 2026 (early access, gr.280278.124).
**Signal source.** Google Scholar author-feed for Chenjie Zeng — new
related research (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Biobanks with EHR linkage (AoU / UKB / MVP /
BioVU); EHR phenotyping infrastructure; ML for precision health
(patient-matching for treatment-effect estimation).

**What the paper does (from abstract snippet).** Introduces GenoSiS,
a genotype-embedding + Intel Scalable Vector Search (SVS)
performance-library pipeline that produces positional encodings of
biobank-scale genotypes and returns representative patient-matched
cohorts for any query patient with sub-second latency. Framed as a
tool for dynamic cohort creation at biobank scale.

**Why it matters for your work.**
1. **Directly on the biobank-infrastructure sub-thread.** Pairs with
   the DRIVE v3 IBD-clustering entry from the 07-23 report — DRIVE
   works at the haplotype-similarity layer for shared-ancestry
   discovery, GenoSiS works at the genome-wide embedding layer for
   overall-similarity cohort matching. Together they define two
   complementary sides of the biobank-similarity-search stack that
   your AoU / BioVU work touches.
2. **Enables new PheWAS designs.** On-the-fly genotype-matched
   control-cohort creation could enable ancestry-matched or
   polygenic-background-matched PheWAS designs in AoU without
   pre-specifying matched-pair strata — a natural methodological
   extension of the ancestry-aware calibration threads under PheWAS/
   phecode infrastructure.
3. **Treatment-effect-heterogeneity relevance.** Patient-matched
   cohort creation is the input to any nearest-neighbor style HTE
   estimator (matching-based meta-learners) — potentially useful for
   the ML-for-precision-health thread, where you're tracking causal
   forests / meta-learners for treatment-effect heterogeneity.

**Follow-ups.** Pull the Genome Research paper. Check (a) whether
the code is released and whether it runs against AoU / UKB
genotype formats (BGEN / VCF), (b) latency at n = 250k+ (AoU srWGS
scale), (c) whether the embedding is population-informed
(admixture-aware) or ancestry-agnostic (this determines whether the
tool is safe for cross-ancestry cohort creation), (d) whether they
benchmark cohort-similarity vs traditional PCA-nearest-neighbor
matching.

---

### 3. Polygenic Prediction of Nongoal Response to Statin Therapy

**Authors.** L Liou, J García-González, HM Wu, S Namba, F Vaura et al.
**Venue.** *Circulation: Genomic and Precision Medicine*, 2026
(CIRCGEN.125.005666).
**Signal source.** Google Scholar author-feed for Chenjie Zeng — new
related research (07-24 09:02Z) **and** Bastarache related-research
feed (double-feed hit).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (PGS applied to a
pharmacotherapy phenotype); ML for precision health (individualized
prediction tied to a clinical decision — "escalate statin therapy");
causal inference & pharmacoepi (treatment-response heterogeneity).

**What the paper does (from abstract snippet).** Uses polygenic risk
scores to predict which patients will *fail* to reach LDL-C guideline
targets on statin therapy — reframing PGS from "who's at genetic
risk for CVD" to "who is genetically unlikely to respond to the
standard first-line pharmacotherapy." A treatment-response
heterogeneity framing.

**Why it matters for your work.**
1. **Textbook example of the ML-for-precision-health rubric.** The
   `INTERESTS.md` says ML papers are HIGH when they're "tied to a
   clinical decision (who to treat, who to screen, when to
   escalate)" — this paper is precisely that. The clinical decision
   is whether to escalate from statin monotherapy to combination
   therapy (add ezetimibe / PCSK9 inhibitor); the PGS is the
   escalation-trigger candidate.
2. **Pairs with the DAPA-HF HTE paper from the 07-21 arxiv-digest.**
   Both are HTE-framed drug-response papers on EHR-linked data —
   DAPA-HF used HTE from a Mayo emulated trial, this one uses PGS
   as the heterogeneity axis. Together they define two axes of
   treatment-effect-heterogeneity discovery you're tracking.
3. **Bastarache-lab lineage.** Bastarache-lab author on the paper
   places it in the BioVU / phenotype-based-drug-response lineage
   — a natural bridge between PheWAS-of-a-PGS work and
   pharmacoepi. Extends the pattern from the Baker et al. DRIVE v3
   paper (07-23 report) into the drug-response domain.

**Follow-ups.** Pull the *Circ Genom Precis Med* paper. Check
(a) which PGS was used (CAD PGS? LDL-C PGS? statin-response-
specific PGS from GWAS-of-drug-response?), (b) which cohort (UKB?
MVP? All of Us? BioVU?), (c) whether they estimate net
reclassification improvement over the current escalation criteria
(LDL-C failure + high-risk-status), (d) whether they release code
for the escalation-trigger PGS.

---

### 4. Correction to "Polygenic Variation Underlying Neutrophil Counts Modifies the Penetrance of Duffy-Null Neutropenia"

**Authors.** JP Shelley, M Shi, L Bastarache, CP Chung, JD Mosley.
**Venue.** *American Journal of Hematology*, 2026 (correction,
10.1002/ajh.70420).
**Signal source.** Google Scholar author-feed for Chenjie Zeng — new
related research (07-24 09:02Z).
**Bucket.** HIGH — correction to a paper directly in your
polygenic-modifier-of-monogenic-penetrance reference class.
**Threads served.** PheWAS/PheRS infrastructure (penetrance
estimation under population screening vs. clinically ascertained
cohorts); variant interpretation (modifier PGS as a penetrance
covariate); genetic epidemiology.

**What the paper does (from snippet).** Formal correction notice to
the Shelley et al. paper on **polygenic variation modifying
Duffy-null neutropenia penetrance** in BioVU. The correction is
brief (page-1 style) — likely a numerical / effect-size / figure
correction rather than a retraction.

**Why it matters for your work.**
1. **Direct in the CFTR / APOL1 penetrance framework you use.** The
   Shelley et al. paper is a canonical example of "polygenic
   background modifies monogenic-variant penetrance" in an
   EHR-linked biobank — the exact design template for your
   population-screening-vs-clinically-ascertained penetrance work.
   Any change to effect estimates matters for how strongly the
   modifier claim generalizes.
2. **Duffy-null → CFTR / APOL1 analogy is close.** The Duffy-null
   / neutrophil-count / neutropenia relationship is structurally
   analogous to APOL1 G1/G2 / kidney disease and CFTR / lung
   function — an underlying pathogenic variant whose clinical
   penetrance is modulated by a polygenic background. Corrections
   to the Duffy-null modifier estimates recalibrate what "expected"
   modifier magnitude looks like for these other loci.
3. **Bastarache-lab is a repeated citation source in your work.**
   Two of the three Bastarache items in this two-day window are
   direct-related (this correction + Liou statin-response PGS), so
   this is worth pulling as a bookkeeping matter to keep your
   citation records to Shelley et al. accurate.

**Follow-ups.** Pull the correction; check (a) whether the
correction changes the modifier PGS effect size / significance
threshold or is purely a typographic fix, (b) whether the
BioVU-vs-external-replication comparison in the original is
affected, (c) whether the correction updates any of the supplemental
tables you may have referenced.

---

### 5. APOL1-Mediated Kidney Disease and the Emerging Era of Precision Therapy

**Authors.** T Hopper, B Wang, OA Olabisi.
**Venue.** *Annual Review of Medicine*, 2026 (annurev-med-042325-051210).
**Signal source.** Google Scholar keyword feed for APOL1 (07-25 03:27Z).
**Bucket.** HIGH — reference utility for the APOL1 thread.
**Threads served.** APOL1 disease thread (kidney disease risk,
transplant decision-making, ancestry considerations);
pharmacoepidemiology (emerging APOL1-targeted therapeutics — direct
APOL1 channel modulators, antisense oligonucleotides, STAT-dependent
APOL1 induction).

**What the paper does (from snippet).** Comprehensive review of the
therapeutic landscape emerging around APOL1-mediated kidney disease
— covering direct APOL1 channel modulators (inaxaplin lineage),
STAT-dependent APOL1 induction, and antisense oligonucleotides
targeting APOL1. Frames APOL1 as an ideal target for precision
nephrology.

**Why it matters for your work.**
1. **Core reference update for the APOL1 thread.** *Annual Review
   of Medicine* is the highest-citation-utility venue for a
   consolidated APOL1-precision-therapy summary — better than
   piecemeal-tracking of individual inaxaplin trial updates.
   Belongs in the reference list of any APOL1-focused manuscript
   introduction or grant Background section.
2. **Enables the pharmacoepi angle on APOL1.** With multiple
   therapeutic candidates now moving through late-stage trials, the
   APOL1 thread is transitioning from "genotype → phenotype
   penetrance" to "genotype → phenotype → therapy-eligibility →
   post-therapy outcomes" — the CF-modulator pharmacoepi framework
   you use for Trikafta / ivacaftor is the natural template.
3. **Ancestry considerations tie to your AoU / BioVU work.** APOL1
   G1/G2 risk-allele frequencies are highly ancestry-stratified,
   making AoU (with rich AA representation) the natural discovery
   platform for real-world evidence on APOL1 therapy uptake and
   outcomes.

**Follow-ups.** Pull the review; extract (a) the current landscape
of APOL1-targeted therapies in trials (name, phase, sponsor,
primary endpoint), (b) whether the review takes a position on
population screening vs. targeted screening in high-G1/G2
populations, (c) whether kidney transplant decision-making
guidelines are discussed (donor-side G1/G2 status), (d) any
citations to AoU / BioVU / MVP APOL1 phenotype work you should
cross-reference.

---

### 6. Interference of Clonal Hematopoiesis in cfDNA Liquid Biopsy Testing & Identification of Actionable Alterations in Large Diverse Cohort of US Veterans

**Authors.** LF Valle, M Scobie, K Rowe, CC Pritchard et al.
**Venue.** *The Oncologist*, 2026 (oyag265/8739212).
**Signal source.** Google Scholar keyword feed —
`intitle:"clonal hematopoiesis"` (07-25 03:27Z).
**Bucket.** HIGH.
**Threads served.** Clonal hematopoiesis / VEXAS (CH artifacts in
cfDNA calling); hereditary cancer / precision oncology (prostate
cancer actionable-alteration calling); biobanks with EHR linkage
(US Veterans / MVP-adjacent cohort); ML for precision health
(clinical decision — whether a cfDNA-detected variant is somatic
tumor vs. CH).

**What the paper does (from snippet).** Large-cohort study in US
Veterans with metastatic castration-resistant prostate cancer
(mCRPC) evaluating how clonal hematopoiesis contaminates cfDNA
liquid biopsy panels used to identify actionable alterations (e.g.
BRCA1/2 for PARP inhibitors, DNA-damage-response genes). Provides
CH-filtering strategy validated in a diverse cohort. Pritchard on
the author list places it in the UW / hereditary-cancer /
somatic-vs-germline resolution lineage.

**Why it matters for your work.**
1. **CH-as-nuisance-vs-signal is a core CHIP thread question.**
   Your CHIP/VEXAS thread has been tracking CH as a
   cardiovascular-risk driver; this paper flips the framing — CH
   as an *analytical artifact* that must be filtered before
   downstream somatic-alteration calls are trusted. Both framings
   matter for CH data pipelines.
2. **Hereditary cancer × precision oncology bridge.** Actionable-
   alterations in mCRPC cfDNA include BRCA1/2 pathogenic variants
   that also serve as hereditary-cancer signals — the same variant
   type serves as PARP-inhibitor biomarker AND as familial-cancer
   risk marker. Filtering CH-derived signal correctly is critical
   for both interpretations. Directly on the hereditary cancer
   thread in your `zeng-publications` skill.
3. **Veterans / MVP cohort access is a live thread.** MVP is one
   of the four biobanks the `INTERESTS.md` explicitly names as
   high-priority. Any veterans-cohort mCRPC paper is a template
   for how the VA precision oncology data infrastructure is being
   used — worth reading the methods for cohort-construction
   pointers.

**Follow-ups.** Pull the *Oncologist* paper. Check (a) the
CH-filtering algorithm (VAF-based? paired-blood-cfDNA
subtraction?), (b) the cohort size and ancestry breakdown (Veteran
mCRPC is often ~30% AA), (c) whether the filter changes the
BRCA1/2 germline-signal detection rate, (d) whether the paper
releases code / a callable filter for cfDNA-CH classification.

---

### 7. Comparative Risk of Psoriatic Arthritis in Type 2 Diabetes: An Emulated Target Trial of SGLT2 Inhibitors vs. GLP-1 Receptor Agonists

**Authors.** FS Yen, SI Wang, CM Hwu, KY Chen, CC Hsu et al.
**Venue.** *Drug Design, Development and Therapy*, 2026
(DDDT.S614222).
**Signal source.** Google Scholar author-feed for Patrick Ryan —
new related research (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Causal inference & pharmacoepidemiology
(explicit target-trial emulation between two active drug classes);
active drug-class threads (GLP-1 RAs, SGLT2is); autoimmune (PsA
outcome).

**What the paper does (from snippet).** Emulated target trial in
T2D patients comparing SGLT2i vs GLP-1 RA on incident psoriatic
arthritis. Ryan-feed placement suggests OHDSI / OMOP-CDM
methodology; extra-cardiovascular outcome (PsA) is the interesting
angle since SGLT2i vs GLP-1 RA comparisons in the CV/renal space
are already well-covered.

**Why it matters for your work.**
1. **Directly on the active drug-class threads.** GLP-1 RAs and
   SGLT2is are both explicitly named in `INTERESTS.md` as active
   drug-class threads. Any head-to-head TTE between the two is
   HIGH by default, especially on a non-cardiovascular outcome
   that extends the comparative-effectiveness picture.
2. **PsA is an autoimmune outcome — bridges to the IBD /
   autoimmune sub-thread.** The 07-25 keyword-feed also surfaced
   several autoimmune papers; PsA fits the broader
   inflammatory-arthritis space that's adjacent to your IBD
   thread. Autoimmune drug-response signal in a cardiometabolic
   drug class is precisely the kind of unexpected extra-primary-
   indication effect the pharmacoepi thread is watching for.
3. **Method template.** Yen-lab TTE methodology (Taiwan
   NHI database) is a well-established template for
   claims-based drug-class TTE — cross-check against Ryan-lab
   OHDSI OMOP-CDM TTE conventions for consistency.

**Follow-ups.** Pull the paper; check (a) which claims database
(Taiwan NHIRD? Merative? Optum?), (b) TTE grace-period /
initiator design choices, (c) whether propensity-score overlap
supports the target population, (d) whether the direction of
effect aligns with published biological priors on IL-17 / TNF
pathway modulation by GLP-1 / SGLT2.

---

### 8. Germline cancer risk alleles drive myelodysplastic neoplasms throughout adulthood

**Authors.** TD Walker, AL Koppayi, TE Carlelycke, Y Haribabu et al.
**Venue.** *Leukemia*, 2026 (s41375-026-03052-8).
**Signal source.** Google Scholar author-feed for Chenjie Zeng —
new related research (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Hereditary cancer (germline predisposition
variant × MDS phenotype); genetic epidemiology (germline-somatic
interplay); CHIP/VEXAS/MDS lineage (adult MDS transitions).

**What the paper does (from snippet).** Extends the previously
recognized pediatric role of germline pathogenic / likely
pathogenic (P/LP) variants in MDS-risk genes into adult MDS —
i.e., shows that germline cancer-risk alleles continue to drive
MDS across the full adult lifespan, not just in childhood-onset
disease. Reframes adult MDS as partially germline-driven.

**Why it matters for your work.**
1. **Hereditary cancer × somatic hematologic malignancy bridge.**
   Directly on the hereditary-cancer thread in your `zeng-
   publications` skill — extends germline-variant-driven cancer
   risk into a hematologic-malignancy outcome that's typically
   thought of as a somatic-driver disease. Natural companion to
   the CHIP → MDS transition literature you're tracking.
2. **Design template for AoU / BioVU germline-MDS work.** The
   paper's cohort structure (however it's constructed) provides a
   template for AoU-based hereditary MDS-risk PheWAS designs —
   MDS is codeable in AoU via ICD-10 D46 codes and has meaningful
   incidence at biobank scale.
3. **Bridges to the veterans-cohort CH work in item 6.** Adult
   MDS with germline drivers overlaps with the CH-in-cfDNA
   interpretation problem — a CH-detected DDR / TET2 / DNMT3A
   variant may be either somatic clonal expansion OR the tip of an
   underlying germline predisposition. Frames a two-paper
   composite (Valle + Walker) worth reading together.

**Follow-ups.** Pull the *Leukemia* paper; check (a) which
genes / gene panel was screened, (b) the age distribution of
germline-driven adult MDS (early-adult? late-adult?), (c) whether
they estimate population-level germline attributable fraction, (d)
overlap with the DDX41 / RUNX1 / GATA2 / SAMD9 canonical MDS-
predisposition list.

---

### 9. Protocol for constructing multi-ancestry polygenic models using S4-Multi

**Authors.** PH Lai, JP Tyrer, J Baierl, PDP Pharoah, PC Peng.
**Venue.** *STAR Protocols*, 2026.
**Signal source.** Google Scholar author-feed for Joshua C. Denny
— new related research (07-24 09:02Z).
**Bucket.** HIGH — reference-utility PGS construction protocol.
**Threads served.** Genetic epidemiology (PGS methodology
extended to multi-ancestry); trans-ancestry portability
sub-thread.

**What the paper does (from snippet).** *STAR Protocols* format
step-by-step guide for constructing multi-ancestry polygenic
models using S4-Multi (a summary-statistics-based multi-ancestry
PRS method). Reference-utility protocol paper rather than a new
methods paper.

**Why it matters for your work.**
1. **Fills a gap in the multi-ancestry PGS toolchain.** The
   trans-ancestry PGS space has PRS-CSx, MUSSEL, PROSPER,
   MAGEPRO, and now S4-Multi with a formal protocol writeup —
   worth adding to the reference library for the trans-ancestry
   portability sub-thread.
2. **Pharoah connection.** Pharoah lab is a canonical hereditary-
   cancer PGS lineage (breast, ovarian) — S4-Multi applied to
   BRCA-modifier PGS across ancestries would be a natural
   application in your hereditary-cancer thread.
3. **Pairs with the Jo et al. East-Asian meta-analysis from the
   07-23 report.** Together they define the input-summary-stats
   supply-side and the PGS construction demand-side of the
   trans-ancestry PGS pipeline.

**Follow-ups.** Pull the STAR Protocols paper; check the
computational-resource profile (does it scale to AoU-native
multi-ancestry cohorts?), example datasets provided, and code
release status.

---

### 10. A blended genome and exome sequencing method captures genetic variation in an unbiased and cost-effective manner

**Authors.** TA Boltz, BB Chu, M DeFelice, C Liao, JM Sealock et al.
**Venue.** *Nature Genetics*, 2026.
**Signal source.** Google Scholar author-feed for Konrad Karczewski
— new related research (07-24 09:02Z).
**Bucket.** HIGH — biobank sequencing infrastructure.
**Threads served.** Genetic epidemiology (upstream sequencing-
economics); biobanks with EHR linkage (implications for AoU / MVP
sequencing design).

**What the paper does (from title).** New sequencing design that
blends genome- and exome-sequencing capture / library-preparation
approaches to reduce per-sample cost while retaining unbiased
capture of the coding + non-coding genome. *Nature Genetics*
placement suggests strong performance benchmarks vs. WGS and WES
alone.

**Why it matters for your work.**
1. **Directly affects biobank sequencing economics.** If validated,
   a blended G+E method that costs less than WGS while retaining
   coding-region coverage could reshape sequencing designs for
   BioVU, MVP, and future AoU expansions. Worth tracking as
   infrastructure that will show up downstream in AoU / MVP
   sequencing releases.
2. **Karczewski lab is the gnomAD / LOFTEE / pLoF burden lineage.**
   Any method that changes what variants get called at biobank
   scale directly affects the pLoF-burden downstream analyses you
   track for CFTR / APOL1 / BRCA and other Mendelian genes.
3. **Sealock on the author list is the BioVU / VUMC-genomics
   connection** — signals that a BioVU-adjacent partner is
   contributing to the sequencing-methods development, which
   matters for future BioVU sequencing release plans.

**Follow-ups.** Pull the paper; check (a) per-sample cost vs. WGS,
(b) coverage uniformity across coding and non-coding regions, (c)
whether the method has already been deployed in a specific biobank
release (BioVU, MVP, AoU), (d) how it compares to blended-capture
approaches like Twist Comprehensive Exome + short-insert WGS.

---

### 11. Large-Scale Plasma Proteomics Enhances Prediction of Liver-Related Events Among Individuals With Prediabetes and Type 2 Diabetes: A Prospective Cohort Study in the UK Biobank

**Authors.** C Ye, Z Zhang, Y Ding, Y Yu, S Zhang, J Pan, S Nie et al.
**Venue.** *Diabetes, Obesity and Metabolism*, 2026 (dom.71113).
**Signal source.** NCBI PubMed "UK Biobank" feed (07-24 12:33Z).
**Bucket.** MEDIUM-HIGH.
**Threads served.** Biobanks with EHR linkage (UKB proteomics);
ML for precision health (risk-prediction with proteomic panels);
chronic disease clustering / multimorbidity (cardiometabolic ×
liver outcomes).

**What the paper does (from title).** UKB Olink proteomics-based
risk-stratification for incident liver-related events (MASLD, MASH,
cirrhosis, HCC) in the prediabetes / T2D subset. Presumably tests
whether adding proteomic panels improves prediction over standard
clinical variables (FIB-4, MASLD score).

**Why it matters for your work.**
1. **Cardiometabolic × liver multimorbidity.** Directly on the
   chronic-disease-clustering / multimorbidity thread — the
   cardiometabolic-to-liver progression axis is one of the
   canonical patterns your multimorbidity work tracks.
2. **UKB proteomics is a repeated pattern in your feeds.** Multiple
   UKB proteomics papers surface in the NCBI feeds each week (see
   also the coronary-plaque proteomics paper in the 07-23 UKB
   feed). This one adds the T2D → liver progression outcome —
   filling in the cardiometabolic-multimorbidity template.
3. **Design template for AoU / MVP proteomics work.** Once AoU
   releases proteomic assays at scale, this UKB-based analytical
   template will port directly.

**Follow-ups.** Pull the paper if the cardiometabolic-multimorbidity
thread is active. Check (a) net-reclassification improvement over
FIB-4 / MASLD score, (b) top-ranked proteins in the panel (any
druggable / MR-instrument candidates?), (c) external validation
cohort.

---

## METHODS-WATCH tail

### Auditing pretraining contamination in single-cell foundation model benchmarks (arxiv 2607.20572v1)

**Author.** Sarwan Ali.
**Venue.** arXiv preprint, 2026-07-21 (`q-bio.GN`, `foundation model`
keyword hit).
**Signal source.** `arxiv-digest` repo, `digests/2026-07-24.md` (the
only new paper in the 07-24 digest).
**Bucket.** METHODS-WATCH.

**What the paper does.** Introduces **scContam**, a per-cell audit
framework combining MinHash-based gene-set fingerprints against the
Genecorpus-30M pretraining corpus with a loss-based membership
inference attack (MIA-scFM). Finds that two of the most-cited
single-cell FM benchmarks (PBMC 3k and CELLxGENE pancreatic islet
atlas) contain 77–80% cells with fingerprint evidence of
pretraining overlap; post-cutoff benchmarks (AIDA v2, Tahoe-100M)
show 0%. Controlled re-pretraining shows MIA-scFM AUROC scales
monotonically with capacity-to-data ratio (0.49 → 0.69 → 0.88 across
regularized → mildly-overfit → aggressively-overfit models).
Donor-matched within-cell-type analysis shows contaminated cells
embed measurably more tightly than clean cells.

**Why it's methods-watch (not HIGH).** Not clinical EHR foundation
models — it's single-cell FMs (Geneformer, scGPT, UCE). But the
audit framework is directly transferable to EHR foundation models
(CLMBR, MOTOR, MedTok, EHRSHOT), which is the thread that matters
for your `INTERESTS.md`. The distinction between distributional
contamination (real, hard to fully audit) vs. instance-level
memorization (mostly absent in well-regularized production models)
is exactly the framing that clinical-FM benchmark reporting will
have to adopt.

**Follow-up if the EHR-FM thread gets active.** Cross-check whether
CLMBR / MOTOR / EHRSHOT authors have released their pretraining
corpora cell-hash-equivalents (MedTok tokenizer + code-vocab
fingerprints) that would allow the same audit strategy for
clinical-code sequences.

---

### Exposure definition sensitivity unmasks hidden confounding in crystalloid target trial emulation (iScience)

**Authors.** Q Dai, Y Hao, J Shen, X Ren, C Jin.
**Venue.** *iScience*, 2026 (S2589-0042(26)01959-0).
**Signal source.** Google Scholar author-feed for Patrick Ryan (07-24
09:02Z).
**Bucket.** METHODS-WATCH.

**What the paper does.** Tests whether standard TTE diagnostics
(SMD, balance plots) are sufficient by emulating a balanced-crystalloid
vs. 0.9% saline trial in MIMIC. Finds that exposure-definition
sensitivity (grace period, index-date operationalization) can
unmask hidden confounding that passes standard balance diagnostics.

**Why it's methods-watch (not HIGH).** Doesn't directly serve one of
your named drug-class threads, but the *methodological lesson* is
directly relevant to any TTE work you do — including the SGLT2i vs
GLP-1 RA drug-class threads. Pairs with the Sun disparities-estimand
paper from the 07-22 report as "TTE robustness auxiliary literature."

---

### Functionally informed genome-wide fine-mapping for complex traits (WCGALP proceedings)

**Authors.** Y Wu, Z Zheng, L Thibaut, T Lin, Q Feng, H Cheng et al.
**Venue.** *World Congress on Genetics Applied to Livestock Production
(WCGALP) 2026 proceedings.*
**Signal source.** Google Scholar author-feed for Chenjie Zeng — new
related research (07-24 09:02Z).
**Bucket.** METHODS-WATCH.

**What the paper does (from snippet).** Functionally informed
GWAS fine-mapping, using functional annotations as priors to
resolve causal variants under extensive LD and horizontal
pleiotropy.

**Why it's methods-watch (not HIGH).** Fine-mapping-methods
literature moves quickly and this is a proceedings paper rather
than a journal method release. But the paper is in the right
lineage — SuSiE / PolyFun / FLARE / SBayesRC — to be worth logging
for the trans-ancestry portability + fine-mapping methods threads.
Wait for the journal-version release before deep-reading.

---

## Digest / seen-map state

- `digests/2026-07-24.md` — 1 new paper (Ali scContam), 3 previously
  surfaced suppressed. Only file changed by the 07-24 cron.
- `digests/2026-07-25.md` — 0 new papers (1 previously surfaced
  suppressed). Cleanest cron output of the week.
- `seen.json` last touched 2026-07-25 12:36 — matches the cron.
- Nothing surfaced in the 07-24 or 07-25 digests that overlaps with
  the on-thread hits above; all HIGH items in this report came from
  Scholar / NCBI email feeds, not the arxiv-digest repo.

## Suggested next actions

1. **Pull the DePinho *Nature Aging* review (item 1)** — it directly
   cites your telomere-length paper. Confirm which claim your work is
   cited for.
2. **Read Schneider et al. GenoSiS (item 2)** — this is the strongest
   biobank-infrastructure hit in the window; check whether it runs on
   AoU srWGS.
3. **Pull the Shelley/Bastarache Duffy-null correction (item 4)** — if
   any of your CFTR / APOL1 penetrance-modifier design draws on the
   original paper, note the corrected effect estimates.
4. **Add Hopper *Annu Rev Med* APOL1 review (item 5) to the APOL1
   reference library** — supersedes several piecemeal APOL1-therapy
   updates.
5. **Skim the Valle *Oncologist* paper (item 6)** for the CH-filtering
   algorithm — potentially reusable for other cfDNA / liquid biopsy
   settings.
6. **Note the Liou/Bastarache statin-response PGS (item 3)** as a
   template paper for the ML-for-precision-health thread — pairs with
   the DAPA-HF HTE paper from 07-21.
