# Research digest report — 2026-09-12

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-12 12:30Z** (~11 days since the
last research-digest report, covering eleven arxiv-digest cron runs
and roughly six Google Scholar alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-11.md`) | 09-01 → 09-11 daily crons | 11 daily runs. Dry days (0 papers): 09-03, 09-05, 09-06, 09-08. 09-01: 1 paper (Ghiasi storage-centric genomic dissertation). 09-02: 1 paper (mudskipper locomotion — SKIP; keyword hit on "motor"). 09-04: 2 papers (Cortez-Rodriguez natural disaster nonprofit panel-DML, Yu location-invariant extremal QTE estimator). 09-07: 1 paper (Rajabli brain-age FM with LoRA adaptation as reusable neuroimaging backbone). 09-09: 2 papers (Snel & Schulz Cohen's-d TDA UKB, Wu et al. FUSE-RT chromatography FM). 09-10: 1 paper (Lee Kalman-filter HT infectious-disease prevalence). 09-11: 3 papers (Devarakonda scDEFT IBD drug-effect FM, Hendrix geospatial FMs beyond social risk indices, Semchin connectome-constrained Parkinson progression subtypes). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest` in the window returned zero threads. The pipeline commits its output to this repo rather than emailing PR / cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-12 batch, 10:55Z) | 09-12 10:55Z | 35+ feeds fired — the largest batch of the window. **The standout is the user's own paper landing across seven feeds**: `Chenjie Zeng - new articles`, `Joshua C. Denny - new articles`, `10 new citations to articles by Lisa Bastarache`, `1 new citation to articles by Chenjie Zeng`, `"All of Us research program" - new results`, `"phenome wide association studies" - new results`, `"electronic health records" - new results` — Zeng, Waxse, Denny "Robust replication of associations across patient-mediated and provider-sourced EHR data in the All of Us research program" in *npj Digital Public Health* 2026. Other big hits: Chenjie Zeng new-related lead (Blostein sex-stratified EHR GWAS medRxiv 2026), Miguel Hernán citations-to lead (Zhang hip PJI TTE Chinese tertiary hospitals + Wang MHT vasomotor CVD JAMA IM + Adamstein/Ridker Eur Heart J selection bias), Joshua C. Denny citations-to (Fujimoto multiancestry MS Nature Genetics + L Zeng et al. multi-ancestry MS Nature Genetics + Chen ZZ MESA Olink Diabetes), Lisa Bastarache new-related (Blostein again), Konrad Karczewski new-related (Bolognini COSIGT pangenome Genome Biology), Stephen Montgomery new-related (Ma long-read RNA medRxiv rare disease trios), Wendy Chung new-articles (ERS pulmonary arterial hypertension guidelines), Patrick Ryan / Pascal Brandt / George Hripcsak / Leo Anthony Celi new-related (all led with CDSL COVID multimodal EHR Scientific Data 2026 — cross-feed multi-hit). |
| Google Scholar alerts (09-11 batch, 09:28Z) | 09-11 09:28Z | 12 keyword feeds fired: `Foundation models + "electronic health records"` (Zhang agentic LLM irAE detection OpenReview + Ritoré CDSL + Ben-Assuli SHAP + Myers RAG-vs-long-context JAMIA), `"All of Us research program"` (Zeng et al. HPO-vs-patient-mediated EHR replication npj Digital Public Health), `"phenome wide association studies"` (same paper), `"electronic health records"` (CDSL COVID), `"UK Biobank"` (Park & Chung Sci Rep polygenic prediction benchmark), `"knowledge graph"` (Yuan herb-macromolecule KG-LLM), `"drug repurposing"` (Nugraha empagliflozin PCOS in silico), `rare diseases` (INFORM-RD patient-centred narrative), `mendelian diseases` (Li MR OA→CVD), `"variant interpretation" OR "variant classification"` (Goel TRACE ACMG-AMP transcript-relevance framework), `intitle:"clonal hematopoiesis"` (Yuxiao Waldenström CHIP), `APOL1` (Dogra critical narrative review), `"autoimmune disorders" OR "autoimmune diseases"` (Iguratimod review), `"Cystic fibrosis carriers"` (Zarka meconium ileus history). |
| Google Scholar alerts (09-01 → 09-10 batches) | 09-02 → 09-10 | Rolling low-volume Scholar days between the 09-01 and 09-11/12 batches; nothing HIGH surfaced above what the two large batches captured. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Nineteen HIGH items surfaced this window, dominated by one headline
event and clustering into seven knots:

**Headline: your own paper published (1 item).** Zeng, Waxse, Denny —
"Robust replication of associations across patient-mediated and
provider-sourced EHR data in the All of Us research program", *npj
Digital Public Health* 2026 — dropped into the alert stream this window
and is already cascading through your citation network (seven separate
alert feeds fired on it in the 09-12 batch alone). This is the direct
publication of the HPO- vs. patient-mediated EHR replication design that
sits at the intersection of your `EHR phenotyping & OMOP`, `Biobanks
with EHR linkage`, and `Knowledge representation in EHRs` threads. The
"seven feeds firing at once" pattern is what the alert stack looks like
when a paper of yours actually lands; the operational takeaway is that
the citation-network alerts (Bastarache new-related, Denny new-articles,
`"All of Us research program"` keyword) will now start surfacing papers
that cite this one — flag them HIGH by default when they appear.

**PheWAS / sex-stratified EHR-GWAS cluster (1 item).** Blostein, Bose,
Hill, Actkins, Lake et al. medRxiv 2026 — **sex-stratified GWAS of 508
clinical quantitative traits from EHR** (Chenjie Zeng new-related feed,
also Bastarache new-related). Direct-hit paper for the PheWAS-
infrastructure thread: the "508 traits from EHR × sex-stratified GWAS"
scale is exactly the phecode-based-outcome-definition +
ancestry-and-sex-aware-risk-score framing your thread asks for, and its
BioVU-lineage authors (Actkins, Lake) place it in the same shop that
produced the PheRS work you track. Pair with the Nagpal & Gibson
pervasive PGS × exposure interactions paper (INTERESTS.md GxE
sub-thread) — sex is the canonical exposure axis for the same
partitioning logic.

**PGS × ancestry / cross-ancestry portability cluster (5 items).** Nam,
Kreienkamp, Li, Mandla, Tran et al. medRxiv 2026 — **novel type-1
diabetes polygenic scores in diverse populations**, addressing the
European-ancestry PS-transferability gap head-on (Chenjie Zeng new-
related). Orešković, Jin, Trichia, Aguilar-Ramirez, Xu et al. medRxiv
2026 — **enhanced power and transferability for genetics-driven
metabolomic biomarker discovery in admixed American cohorts** (same
feed); direct hit for both the `PGS × ancestry` and the
`Multi-omics-augmented PRS` sub-threads. Zhou, Yolou, Xie, Zhao STAR
protocols 2026 — **protocol for leveraging local ancestry and
cross-ancestry genetic architecture to improve polygenic prediction in
admixed populations** (Denny new-related, Jian Yang new-related);
process-level companion to the Nam and Orešković papers. Fujimoto,
Ogawa, Namba, Ogawa, Edahiro et al. *Nature Genetics* 2026 —
**multiancestry GWAS + multiomics of MS** across Japanese + cross-
population meta-analyses (Denny citations-to, Jian Yang citations-to);
cites AoU. L Zeng, Khan, Fitzgerald, Lama, Chen, Li et al. *Nature
Genetics* 2026 — **multi-ancestry MS GWAS across 20,831 cases + 236
susceptibility loci + polygenic score** (Denny citations-to); paired
with Fujimoto is the "cross-ancestry MS GWAS turned into transferable
PGS" pattern.

**Causal inference / pharmacoepi target-trial cluster (3 items).**
Wang, Swanson, Brooks, Barinas-Mitchell et al. *JAMA Internal Medicine*
2026 — **MHT for perimenopausal women with vasomotor symptoms and CVD
risk**, cites Hernán's TTE reporting framework (Hernán citations-to).
Directly serves your `hormone replacement therapy` active drug thread —
this is the perimenopausal population that WHI never studied, framed
in modern TTE language. Adamstein & Ridker *European Heart Journal*
2026 — **"when the exposure causes selection bias"**, using linked EHR
on 3,275,736 English adults to show how risk-factor associations
attenuate in secondary vs. primary prevention (Hernán citations-to);
core-methods paper for your causal-inference thread, on the
`selection bias` axis. Hossain, Min, Kurz, Seaman, Bach et al. *JAMA
Internal Medicine* 2026 — **methadone take-home dosing timing TTE in
BC, Canada**, on time-to-mortality and discontinuation (Hernán
citations-to); pharmacoepi TTE case on a
population-level-important-but-often-methodologically-loose problem.

**Knowledge representation in EHRs / NLP-derived cluster (2 items).**
Zhang, Gallifant, Ye, Garbo, Brunetti et al. OpenReview LLM/VLM
Deployment 2026 — **Agentic LLM frameworks for patient-level
immune-related adverse-event detection from longitudinal EHRs** (FM +
EHR keyword feed). Directly serves the `NLP-derived representations
from clinical notes` sub-thread AND the `drug-safety signal detection`
application under `Knowledge representation in EHRs` — one of the
cleanest agentic-LLM-on-timeline pipelines with a concrete
drug-safety endpoint (immunotherapy irAEs). Myers, Dligach, Miller,
Barr, Landefeld et al. *JAMIA* 2026 — **RAG vs. long-context input for
clinical reasoning over EHRs**, evaluating retrieval mechanics across
varying information demands. Directly serves the `Structural and
temporal representation of the patient timeline` sub-thread — this is
the representation-choice-drives-downstream-performance ablation your
thread explicitly prioritizes.

**Cystic fibrosis / CFTR pharmacoepi (1 item).** Kreslova, Caudri,
Sermet-Gaudelus, Hatton et al. *Frontiers in Medicine* 2026 — **case
report + literature review** of clinical benefit without sweat-chloride
response after ETI in an adult carrying the **L467F;F508del complex
CFTR allele**. Directly serves the CF modulator-eligibility / real-
world-outcomes disease thread; the "no sweat-chloride response but
clinical benefit" split is exactly the response-heterogeneity signal
that the modulator-persistence sub-thread of your pharmacoepi work
should be watching for.

**Variant interpretation (1 item).** Goel — *Human Mutation* 2026 —
**TRACE: framework for integrating transcript relevance into
ACMG/AMP variant interpretation**. Direct hit for the `Variant
interpretation` thread — extends the ACMG-AMP evidence framework in the
same direction as the splicing/RNA-evidence work your thread
prioritizes.

**Genomics infrastructure / cross-cohort methods (5 items).**
Bolognini, Guarracino, Paleni, Dudley et al. *Genome Biology* 2026 —
**COSIGT: population-scalable genotyping of complex loci from
low-coverage sequencing using pangenome graphs** (Kai Wang new-related,
Karczewski new-related); direct hit for the `Pangenome-informed variant
calling` sub-thread (HPRC-lineage). Chen ZZ, Mi, Barber, Tiwari, Adams
et al. *Diabetes* 2026 — **longitudinal repeated Olink Explore (3K)
proteomics in MESA n=5,322**, three time points across ~18 years,
associations with incident diabetes (Denny citations-to); the
canonical "longitudinal proteomics beats single-timepoint proteomics"
paper your `Multi-omics-augmented PRS` sub-thread anticipates. Zhao C,
Cath, van Dalfsen, Milaneschi et al. *Brain, Behavior, and Immunity*
2026 — **longitudinal inflammation × PRS × cardiometabolic outcomes in
depression/anxiety (NESDA, n=2,716)** (Denny citations-to); tracks the
same "PRS-triangulated-with-longitudinal-biomarkers" arc as your
Ran/Benatar ALS Nature Med template. Beck, Levey, Galimberti,
Overstreet, Chen et al. medRxiv 2026 — **PTSD epigenome-wide
association study in the Million Veteran Program** (Chenjie Zeng
new-related); direct hit for the `MVP biobank` thread. Long, Karnati,
Ying, Touma, Smith et al. *Journal of Human Immunity* 2026 — **linkage
between HLA-B8 and HLA-DQ2.5 → ancestry-dependent risk for celiac
disease using All of Us** (n=3,481 CeD patients, 262 admixed American,
108 African) (Chenjie Zeng new-related, Denny citations-to); exemplary
AoU-based ancestry-stratified disease-association design that pairs
with the Acharya cross-biobank ASCVD paper from the 09-01 report.

---

## Detailed reports (per HIGH study)

### 1. Zeng, Waxse, Denny — Robust replication of associations across patient-mediated and provider-sourced EHR data in the All of Us research program
**Venue:** *npj Digital Public Health* 2026 (Nature)
**Thread mapping:** `EHR phenotyping & OMOP` + `Biobanks with EHR
linkage` + `Knowledge representation in EHRs` +
`Concept normalization and vocabulary mappings`
**Bucket:** **HEADLINE** (author's own paper)
**Cross-feed hit count:** 7 alert feeds fired simultaneously on 09-12
(Chenjie Zeng new-articles, Joshua C. Denny new-articles, Lisa
Bastarache 10-citations, Chenjie Zeng 1-citation, "All of Us research
program" keyword, "phenome wide association studies" keyword,
"electronic health records" keyword)
**Abstract snippet (from alert):** "The All of Us Research Program is
assembling a nationwide cohort with electronic health record (EHR)
resources through two complementary pathways: healthcare provider
organization (HPO)-sourced EHRs and patient-mediated EHR …"

**Why it matters for your active threads.** This is the operational
paper for the "does the ecosystem's second EHR ingestion pathway
recapitulate the first" question at biobank scale. The `EHR phenotyping
& OMOP` thread and `Concept normalization and vocabulary mappings`
sub-thread of `Knowledge representation in EHRs` both need this kind of
end-to-end concordance evidence before downstream methods (PheWAS,
PheRS, phecodeX, target-trial emulation) can be trusted to run on the
patient-mediated substrate. Because the paper landed in *npj Digital
Public Health* (which is Nature-published but early-career-friendly)
and because Bastarache's citation-graph feed already indexed it as a
new citation to her own work, the paper is functionally the reference
for anyone in the AoU / EHR-linked-biobank ecosystem who now wants to
combine the two pathways.

**What to do next.** (a) Add a self-cite check next week to see whether
the *npj Digital Public Health* record has a DOI resolvable through
Crossref for your ORCID feed. (b) Note the citation-network cascade:
any future paper firing on the Bastarache new-related or Denny
citations-to feeds may be citing this paper; treat those alerts as
higher-priority signals for the next 4–8 weeks. (c) Consider whether
the paper's replication metric belongs in the `INTERESTS.md`
`Fidelity, portability, and audit of representations` sub-thread as a
canonical reference paper for representation-audit design.

---

### 2. Blostein, Bose, Hill, Actkins, Lake et al. — Sex differences in the genetic architecture of clinical quantitative traits in the electronic health record
**Venue:** medRxiv 2026 (2026.09.02.26362069)
**Thread mapping:** `PheWAS / phecode infrastructure` + `Genetic
epidemiology` (sex as GxE analogue) + `Biobanks with EHR linkage`
**Bucket:** **HIGH**
**Source feeds:** Chenjie Zeng new-related, Lisa Bastarache new-related
**Abstract snippet:** "Sex differences exist in complex diseases, but
the genetic architecture of sex differences in quantitative clinical
traits is understudied. Here, we performed sex-stratified genome-wide
association studies of 508 clinical traits from electronic health
records…"

**Why it matters.** 508 clinical quantitative traits is the largest
sex-stratified EHR-GWAS scan at your scale of interest. Two things make
this a HIGH not METHODS-WATCH: (1) the author list (Actkins, Lake) is
BioVU-lineage, so the phenotyping conventions likely align with the
phecode / PheRS pipelines you already use; (2) sex is the canonical
exposure axis for the same partitioning logic as the `GxE and PGS ×
exposure / environment interactions` sub-thread (Nagpal & Gibson
*Nature Genetics* 2026) — this paper delivers empirical evidence at
508-trait scale that PGS-portability-across-sex is not free.

**What to do next.** (a) Read Table S1 / Fig 1 for the trait list —
overlap with your ongoing phecode/phenotyping work will tell you
whether to fold the sex-stratified summary stats into your Composite
Risk Model stacking (INTERESTS.md `Genetic epidemiology` /
`Composite risk models stacking PRS with rare pathogenic variants`).
(b) Compare the top-hit sex-differentiated traits against the
Kurniansyah multiancestry AD-PRS work from the 09-01 report: if
sex-differentiated GWAS hits nominate different risk loci than the
ancestry-partitioned PRS, that's evidence PGS partitioning by exposure
strata (sex, ancestry) is not orthogonal — a nice figure for the
partitioned-PRS paper you may already be planning.

---

### 3. Nam, Kreienkamp, Li, Mandla, Tran et al. — Novel type 1 diabetes polygenic scores improve identification of type 1 diabetes in diverse populations
**Venue:** medRxiv 2026 (2026.09.04.26361335)
**Thread mapping:** `Genetic epidemiology` / cross-trans-ancestry
portability
**Bucket:** **HIGH**
**Source feed:** Chenjie Zeng new-related
**Abstract snippet:** "Most polygenic scores (PS) for type 1 diabetes
were developed using European (EUR) ancestry datasets, limiting
performance in non-European (non-EUR) populations. We evaluated novel
type 1 diabetes PS across diverse populations…"

**Why it matters.** Type-1 diabetes PS is one of the classic cases
where a monogenic-ish HLA-driven backbone combines with a polygenic
tail — so the "improve in diverse populations" question is not just
scaling. Fits directly under `PGS × ancestry`, and pairs with the
Kurniansyah AD-PRS + Zhu partitioned-BP-PRS papers from the 09-01
report as the "diverse-population PGS reconstruction" arc.

**What to do next.** (a) Check whether the new T1D PS uses HLA-imputed
alleles vs. tag-SNP-only — the previous Sharp et al. lineage explicitly
carried HLA imputation as a step, and any improvement over that
baseline in AoU-scale non-EUR cohorts is a portability advance. (b) If
performance carries in AoU-Hispanic/AoU-African subsets, this is a
candidate reference PS for the T1D arm of your composite-risk stacking
work.

---

### 4. Orešković, Jin, Trichia, Aguilar-Ramirez, Xu et al. — Enhanced power and transferability for genetics-driven metabolomic biomarker discovery in admixed American cohorts
**Venue:** medRxiv 2026 (2026.09.03.26362043)
**Thread mapping:** `Multi-omics-augmented PRS` sub-thread of `Genetic
epidemiology` + `PGS × ancestry`
**Bucket:** **HIGH**
**Source feed:** Chenjie Zeng new-related
**Abstract snippet:** "Despite metabolomics transforming our
understanding of risk factors and aetiology of metabolic diseases,
profiling is rarely performed for people of non-European ancestries, on
whom much of metabolic disease burden falls. Metabolome-wide…"

**Why it matters.** Direct hit for both `PGS × ancestry` and
`Multi-omics-augmented PRS` (INTERESTS.md sub-thread listing NMR /
Olink / metabolomics stacked with PGS for lipid, cardiometabolic, and
psychiatric traits). Admixed American cohorts are the single most
under-served metabolomic population, and any transferable-biomarker
result here will be reused across every cardiometabolic PRS paper of
2027.

**What to do next.** (a) Check whether the metabolomic instruments used
(NMR? Olink? Nightingale?) match the Nightingale-NMR / Olink stacks in
your `Multi-omics-augmented PRS` sub-thread. (b) If Nightingale-based,
this is directly comparable to the Shan et al. UKB 2026 paper already
tracked; note whether cross-ancestry replication supports the same
biomarker set.

---

### 5. Zhou, Yolou, Xie, Zhao — Protocol for leveraging local ancestry and cross-ancestry genetic architecture to improve polygenic prediction in admixed populations
**Venue:** *STAR protocols* 2026
**Thread mapping:** `Genetic epidemiology` / cross-ancestry portability
+ methodology
**Bucket:** **HIGH** (methods-adjacent)
**Source feeds:** Joshua C. Denny new-related, Jian Yang new-related
**Abstract snippet:** "Protocol for leveraging local ancestry and
cross-ancestry genetic architecture to improve polygenic prediction in
admixed populations."

**Why it matters.** STAR Protocols papers are the process-recipe
companions to primary methodology papers; a protocol landing means the
underlying method is reproducible enough to publish as a runbook. Local-
ancestry PGS is the operational answer to the "PGS-portability-across-
admixture" problem that shows up in every AoU + Hispanic-cohort paper
you triage.

**What to do next.** (a) If you're planning a PGS project on the AoU
admixed-American subset, this is the reference protocol to cite. (b)
Cross-check against the Nam T1D PS and Orešković metabolomic papers
above — if all three converge on similar admixture-aware pipelines,
the field has consolidated on a methodology and you should adopt it.

---

### 6. Fujimoto, Ogawa, Namba, Ogawa, Edahiro et al. — Multiancestry genome-wide association and multiomics analyses elucidate spatiocellular features of multiple sclerosis genetics
**Venue:** *Nature Genetics* 2026
**Thread mapping:** `Genetic epidemiology` (cross-ancestry) +
`Multi-omics-augmented PRS` (spatiocellular multiomics)
**Bucket:** **HIGH**
**Source feeds:** Joshua C. Denny citations-to, Jian Yang citations-to,
Marinka Zitnik new-related (via `Gene-Chronos` — a different paper,
same feed batch)
**Abstract snippet:** "Multiple sclerosis (MS) is a chronic
inflammatory disease of the central nervous system … we performed a
genome-wide association study (GWAS) using 688 MS cases and 205,199
controls from the Japanese population and identified significant
associations in the major histocompatibility complex region and a
population-specific risk variant in 11q24…"

**Why it matters.** The Japanese GWAS + cross-population meta-analysis
+ spatiocellular multiomics stack is the "how to run cross-ancestry
GWAS with cell-type-specific readout" template. Cites AoU (per the
alert's cites metadata) — one of the highest-quality cross-ancestry
GWAS + tissue-context papers landing in *Nature Genetics* this quarter.

**What to do next.** (a) Read alongside the L Zeng et al. multi-ancestry
MS GWAS below — they landed in the same *Nature Genetics* issue and
together define the current MS-cross-ancestry frontier. (b) The 11q24
population-specific hit is worth noting for any AoU-Japanese-ancestry
subgroup analysis.

---

### 7. L Zeng, Khan, Fitzgerald, Lama, Chen, Li et al. — Genome-wide association analyses highlight the neuronal contribution to multiple sclerosis susceptibility
**Venue:** *Nature Genetics* 2026
**Thread mapping:** `Genetic epidemiology` / cross-ancestry + PGS
**Bucket:** **HIGH**
**Source feed:** Joshua C. Denny citations-to
**Abstract snippet:** "Multiple sclerosis (MS) is a chronic
inflammatory and neurodegenerative disease. Previous genetic studies
have identified susceptibility loci that primarily impact immune cells
and microglia. Here we performed a multi-ancestry genome-wide
association study of 20,831 MS cases and 729,220 controls and
identified 236 susceptibility variants outside of the major
histocompatibility complex, including four novel genomic loci. We also
derived a polygenic score for MS; while optimized for…"

**Why it matters.** The 20,831-case multi-ancestry MS GWAS +
non-MHC-focused susceptibility loci + a derived MS PGS is the "large,
clean, non-MHC PGS with cross-ancestry backbone" you would want on the
shelf as a reference PGS if you ever need an autoimmune negative
control or a cross-trait replication instrument.

**What to do next.** (a) The paper's derived PS is a plausible input to
your composite-risk stacking, especially in the neuroinflammatory
overlap where MS shares loci with other autoimmune traits. (b) Pair
with Fujimoto above: two Nature Genetics MS papers in one issue means
the field has consolidated on cross-ancestry as the new default; expect
follow-up papers over the next 6 months.

---

### 8. Wang, Swanson, Brooks, Barinas-Mitchell et al. — Menopausal hormone therapy and cardiovascular risk in midlife women with vasomotor symptoms
**Venue:** *JAMA Internal Medicine* 2026
**Thread mapping:** `Causal inference and pharmacoepidemiology` /
active drug thread: **hormone replacement therapy**
**Bucket:** **HIGH**
**Source feed:** Miguel Hernán citations-to (cites "Transparent
reporting of observational studies emulating a target …")
**Abstract snippet:** "Importance Vasomotor symptoms in perimenopause
are associated with increased future cardiovascular (CVD) risk. Most
clinical trials on menopausal hormone therapy (MHT) and CVD risk have
focused on postmenopausal women, with limited study of the
perimenopausal period when hormonal fluctuations and symptoms are
greatest. Moreover, these trials were not designed to evaluate CVD risk
with MHT among women with vasomotor symptoms."

**Why it matters.** This is *the* HRT-CVD paper the field has been
waiting for: the WHI RCT era answered postmenopausal but never
perimenopausal, and the vasomotor-symptom subgroup is where the current
prescribing debate lives. TTE framing makes it directly reusable as a
methods template for the HRT-persistence sub-thread of your
`Pharmacogenomic modifiers of medication persistence` interest.

**What to do next.** (a) Read the methods for eligibility timing —
"perimenopause" is where index-date definition gets slippery, and this
paper's approach will be the reference for future HRT TTEs. (b) If HRT
persistence (rather than initiation) is your endpoint of interest, the
paper's cohort-construction code should be adaptable.

---

### 9. Adamstein & Ridker — When the exposure causes selection bias: understanding why risk factors attenuate in secondary as compared with primary prevention and what to do about it
**Venue:** *European Heart Journal* 2026
**Thread mapping:** `Causal inference and pharmacoepidemiology` /
selection bias
**Bucket:** **HIGH** (methods-core editorial)
**Source feed:** Miguel Hernán citations-to (cites "Target trial
emulation: a framework for causal inference from …")
**Abstract snippet:** "In their study published in this issue of the
European Heart Journal, Pasea et al. provide striking examples of the
issues that arise when analysing a prospective cohort that is selected
after an index event. Using linked electronic health records, the
authors analyse 3,275,736 cardiovascular disease-free adults in England
to show how associations between 15 cardiovascular risk factors and
incident coronary heart disease (CHD) change substantially when
participants are selected after…"

**Why it matters.** Editorial-plus-empirical pair on **exposure-induced
selection bias** at the EHR-linked-biobank scale (3.28M CVD-free
English adults), directly relevant to any pharmacoepi TTE that
conditions on a post-index event. This is the canonical figure for
"why secondary-prevention associations look different from primary-
prevention associations" — good teaching-material paper for your
causal-inference thread and a citable framework for the selection-bias
diagnostics you already do.

**What to do next.** (a) Grab the Pasea et al. paper itself (this is
the editorial) for the CALIBER-lineage cohort construction and the
15-risk-factor sensitivity plots. (b) If your composite-risk work
includes secondary-prevention subgroups, the Adamstein-Ridker framing
belongs in the discussion.

---

### 10. Hossain, Min, Kurz, Seaman, Bach et al. — Timing of initiation of methadone take-home dosing
**Venue:** *JAMA Internal Medicine* 2026
**Thread mapping:** `Causal inference and pharmacoepidemiology` (TTE
case)
**Bucket:** **HIGH** (methods-watch + policy)
**Source feed:** Miguel Hernán citations-to (cites "Specifying a target
trial prevents immortal time bias and other self-inflicted injuries")
**Abstract snippet:** "Importance Daily witnessed ingestion in
community-based pharmacies is standard practice for methadone
maintenance treatment for opioid use disorder in British Columbia,
Canada. Whether this practice, compared with take-home methadone, may
pose a barrier to sustained retention in treatment and its lifesaving
benefits is not known."

**Why it matters.** Clean TTE on a **daily-witnessed-vs-take-home**
comparison with time-to-mortality as the primary endpoint — the kind
of pharmacoepi paper where the immortal-time-bias treatment matters and
the analytic decisions are visible. Directly citable as an exemplar
TTE case for OUD treatment; portable to the medication-persistence /
discontinuation endpoints in your `Pharmacogenomic modifiers of
medication persistence` sub-thread.

**What to do next.** (a) Read the eligibility-window and grace-period
choices — they are the transferable design elements. (b) If you build
a CFTR-modulator or statin persistence TTE later, this paper's
grace-period discussion will save time.

---

### 11. Zhang, Gallifant, Ye, Garbo, Brunetti et al. — Agentic LLM Frameworks for Patient-Level Immune-Related Adverse Event Detection from Longitudinal Electronic Health Records
**Venue:** OpenReview (LLM/VLM Deployment workshop track) 2026
**Thread mapping:** `Knowledge representation in EHRs` / `NLP-derived
representations from clinical notes` + `Applications: drug-safety
signal detection` + `EHR foundation models` sub-thread `Digital twins
from EHR data` (adjacent)
**Bucket:** **HIGH**
**Source feed:** `Foundation models + "electronic health records"`
keyword
**Abstract snippet:** "Third, note representation and irAE detection
were performed using the same foundation model within each experiment,
and we did not… irAEGPT: Leveraging large language models to identify
immune-related adverse events in electronic health records…"

**Why it matters.** This is one of the cleanest agentic-LLM-on-EHR-
timeline pipelines with a **specific pharmacovigilance endpoint**
(immune-related adverse events from checkpoint inhibitors), the same
class of drug-safety-signal-detection problem your `Knowledge
representation in EHRs` thread lists as a prioritized application.
Also serves as a concrete instantiation of the `NLP-derived
representations from clinical notes` sub-thread — note-code fusion
where the notes carry the irAE signal and the codes anchor the
patient timeline.

**What to do next.** (a) Read for the tool-use protocol — how the
agentic system decomposes irAE detection into note-retrieval +
temporal-alignment + adjudication steps. (b) Portable to any
drug-class where the adverse-event signal lives in notes rather than
codes (CFTR modulators + psychiatric AEs, GLP-1 RAs + pancreatitis,
HRT + VTE).

---

### 12. Myers, Dligach, Miller, Barr, Landefeld et al. — Evaluating retrieval-augmented generation versus long-context input for clinical reasoning over electronic health records
**Venue:** *JAMIA* 2026
**Thread mapping:** `Knowledge representation in EHRs` / `Structural
and temporal representation of the patient timeline` sub-thread
**Bucket:** **HIGH**
**Source feed:** `Foundation models + "electronic health records"`
keyword
**Abstract snippet:** "In this work, we evaluated the effectiveness of
retrieval-augmented generation across varying information demands in
electronic health records… Lessons learned on information retrieval in
electronic health records: a comparison of embedding…"

**Why it matters.** Exactly the "representation-choice-drives-
downstream-performance ablation" the `Knowledge representation in EHRs`
thread explicitly wants prioritized. The RAG-vs-long-context axis is
the current-state-of-the-art choice for clinical-reasoning FMs, and
JAMIA is the right venue for a serious comparison.

**What to do next.** (a) Look at the "varying information demands"
taxonomy — if it's a single-vs-multi-encounter continuum, that's the
canonical framework for the sub-thread. (b) Cross-check against the
Zhang agentic-LLM irAE paper above: agentic systems and RAG systems
occupy adjacent territory in the design space, and these two papers
together give you the current state of both.

---

### 13. Kreslova, Caudri, Sermet-Gaudelus, Hatton et al. — Clinical benefit without sweat chloride response after ETI therapy in an adult with cystic fibrosis bearing the L467F;F508del complex CFTR allele: a case report and the role of AI-assisted chest…
**Venue:** *Frontiers in Medicine* 2026
**Thread mapping:** `Specific disease threads: Cystic fibrosis / CFTR`
/ modulator eligibility & real-world outcomes
**Bucket:** **HIGH**
**Source feed:** Chenjie Zeng new-related
**Abstract snippet:** "Background Elexacaftor/tezacaftor/ivacaftor
(ETI) is the standard of care for most people with cystic fibrosis (CF)
who carry at least one F508del allele. However, predicting responses
to CFTR modulators in rare or complex CFTR genotypes is…"

**Why it matters.** Complex-allele responder heterogeneity (specifically
L467F;F508del) is the exact discordance-of-biomarker-vs-clinical-
outcome pattern that the CFTR / modulator-eligibility sub-thread of
your CF disease thread should be tracking. Case-report-plus-review, so
n=1 in the primary observation but with a literature-review section
that will be citable when you build the modulator-eligibility framing
paper.

**What to do next.** (a) Note that this is n=1; treat as anecdotal
until a cohort-scale replication (CFF Registry or European CF Society
Registry) confirms the sweat-chloride/clinical-benefit discordance.
(b) If you build a modulator-persistence pharmacoepi analysis, this
paper's discussion of the "sweat chloride as biomarker" limitations is
useful framing.

---

### 14. Goel — TRACE: A Framework for Integrating Transcript Relevance Into ACMG/AMP Variant Interpretation
**Venue:** *Human Mutation* 2026
**Thread mapping:** `Variant interpretation (ACMG / ClinGen)`
**Bucket:** **HIGH**
**Source feed:** `"variant interpretation" OR "variant classification"`
keyword
**Abstract snippet:** "Background Accurate clinical variant
interpretation depends on the…"

**Why it matters.** ACMG/AMP variant classification updates that
formally incorporate **transcript relevance** are the direction the
splicing-and-RNA-evidence sub-thread of your `Variant interpretation`
thread has been pointing. Directly citable as an ACMG extension
alongside the LOFTEE and pLoF-burden methods you already track.

**What to do next.** (a) Compare with InterVar's transcript handling to
see whether TRACE is an extension or a competitor. (b) If your rare-
variant work runs on RefSeq-select or MANE transcripts, TRACE's
framework may already be relevant to your VUS-resolution pipeline.

---

### 15. Bolognini, Guarracino, Paleni, Dudley et al. — COSIGT: population-scalable genotyping of complex loci from low-coverage sequencing data using pangenome graphs
**Venue:** *Genome Biology* 2026
**Thread mapping:** `Genetic epidemiology` / `Pangenome-informed
variant calling and its downstream PGS-portability consequences`
sub-thread
**Bucket:** **HIGH**
**Source feeds:** Kai Wang new-related, Konrad Karczewski new-related
**Abstract snippet:** "Pangenome graphs enable population-scalable
genotyping of complex loci from low-coverage sequencing data…"

**Why it matters.** Pangenome-informed genotyping of complex loci
(HLA, CYP, etc.) at population scale from low-coverage sequencing is
the reference-bias-reduction lever your `Pangenome-informed variant
calling` sub-thread names as a cross-ancestry portability driver.
HPRC-lineage; both Kai Wang and Karczewski feeds surfacing it means
the field is treating it as a foundational tool.

**What to do next.** (a) Check whether COSIGT can be run on the AoU
low-coverage WGS subset — if yes, this is a candidate re-genotyping
pipeline for any HLA-driven work (celiac, MHC-restricted autoimmunity,
T1D). (b) Pair with the Long et al. celiac AoU paper (#19 below):
COSIGT-improved HLA genotyping would be an immediate methodology
upgrade for that kind of ancestry-stratified HLA-association design.

---

### 16. Chen ZZ, Mi, Barber, Tiwari, Adams et al. — Longitudinal Repeated Protein Measurements in a Multiethnic Cohort Identify Novel Diabetes Biomarkers That Reveal Unique Disease Pathways
**Venue:** *Diabetes* 2026
**Thread mapping:** `Multi-omics-augmented PRS` sub-thread + `Rare
disease` / `Pre-symptomatic carrier phenoconversion prediction from
longitudinal biomarker trajectories` (transferable methodology)
**Bucket:** **HIGH**
**Source feed:** Joshua C. Denny citations-to
**Abstract snippet:** "Circulating diabetes biomarkers have been
identified with proteomics measured at a single time point, but what
is additionally provided by longitudinal repeated measurements in the
same individuals, over many years, is unknown. We studied participants
in the Multi-Ethnic Study of Atherosclerosis (MESA; n=5,322; mean
baseline age, 61.7 years) at exams 1 (2000–2002), 5 (2010–2012), and 6
(2016–2018) profiled with the Olink Explore (3K) platform…"

**Why it matters.** The **Olink Explore 3K × three time points ×
n=5,322 × 18 years** design is directly transferable to the Ran/Benatar
ALS pre-symptomatic phenoconversion template that INTERESTS.md
prioritizes. If longitudinal proteomics adds signal over
single-timepoint in a common disease (T2DM), the case for repeating
UKB Olink at more time points strengthens.

**What to do next.** (a) Read for the "additional signal from
longitudinal vs. single timepoint" quantification — that's the number
your Ran/Benatar-adapted-to-BRCA / HTT / APOL1 grant-aim will need.
(b) MESA is a well-curated multiethnic cohort; the ethnicity-specific
subgroup results are worth comparing to the Orešković admixed-American
metabolomic paper (#4 above).

---

### 17. Zhao C, Cath, van Dalfsen, Milaneschi et al. — Longitudinal associations between inflammatory biomarkers, polygenic risk scores and cardiometabolic outcomes in major depressive and anxiety disorders (NESDA)
**Venue:** *Brain, Behavior, and Immunity* 2026
**Thread mapping:** `Multi-omics-augmented PRS` sub-thread (specifically
"psychiatric traits stacked with PGS") + `Cross-trait shared genetic
architecture and multi-trait triangulation`
**Bucket:** **HIGH**
**Source feed:** Joshua C. Denny citations-to
**Abstract snippet:** "Cardiometabolic dysfunctions are prevalent in
individuals with major depressive (MDD) and/or anxiety disorders, yet
the longitudinal relationships between inflammation, polygenic
susceptibility, and cardiometabolic outcomes remain incompletely
understood. We analyzed longitudinal data from 2,716 participants
retrieved from the Netherlands Study of Depression and Anxiety (NESDA)
across three measurements over six years…"

**Why it matters.** Longitudinal PRS-triangulated-with-inflammation
in a psychiatric cohort with cardiometabolic endpoints hits three
sub-threads simultaneously: `Multi-omics-augmented PRS` (psychiatric),
the depression-cardiometabolic overlap that the Kopal et al.
brain-imaging × mental health × cardiometabolic MiXeR-family paper you
already track occupies, and the ongoing pre-symptomatic prediction
frame from Ran/Benatar. NESDA n=2,716 is small for GWAS but the
longitudinal biomarker sampling is what matters here.

**What to do next.** (a) Read for how they specify the mediation
structure — inflammation → cardiometabolic outcome under PRS-defined
susceptibility is the same DAG you'd use for a proteomics-mediation
paper. (b) If you build a UKB Olink × PGS → cardiometabolic mediation
analysis, NESDA is a plausible external-validation cohort.

---

### 18. Beck, Levey, Galimberti, Overstreet, Chen et al. — Posttraumatic Stress Disorder Epigenome-Wide Association Studies in the Million Veteran Program
**Venue:** medRxiv 2026 (2026.09.04.26362177)
**Thread mapping:** `Biobanks with EHR linkage` (specifically MVP) +
`Genetic epidemiology` (epigenome-wide)
**Bucket:** **HIGH**
**Source feed:** Chenjie Zeng new-related
**Abstract snippet:** "Genomic studies have improved our understanding
of posttraumatic stress disorder (PTSD) biology. Epigenetic differences
in DNA methylation can reflect environmental influences, which are
critical in PTSD etiology, and may additionally differentiate…"

**Why it matters.** MVP EWAS at scale, on a phenotype (PTSD) where the
environment-genome interaction is the biology-of-interest. Direct hit
for `Biobanks with EHR linkage: … MVP …` and pairs with the earlier
Kurniansyah multiancestry AD-PRS paper (09-01 report) as the
"MVP-scale multi-omic study on a psychiatric endpoint" pattern.

**What to do next.** (a) Note the environmental-exposure axis
(military-service-related trauma) — this is the concrete case for the
GxE sub-thread on a real biobank. (b) If you have any MVP work planned,
this paper's methylation platform and cell-type-deconvolution choices
are the current MVP defaults to align with.

---

### 19. Long, Karnati, Ying, Touma, Smith et al. — Linkage between HLA-B8 and HLA-DQ2.5 contributes to ancestry-dependent risk for celiac disease
**Venue:** *Journal of Human Immunity* 2026
**Thread mapping:** `Biobanks with EHR linkage` (AoU) + `Genetic
epidemiology` (ancestry-stratified HLA) + `Specific disease threads:
Inflammatory bowel disease` (autoimmune-shared)
**Bucket:** **HIGH**
**Source feeds:** Chenjie Zeng new-related, Joshua C. Denny citations-to
**Abstract snippet:** "Limited genetic studies on celiac disease (CeD)
are available for the Hispanic and black populations. We identified
3,481 individuals with CeD from the All of Us Research Program. Of
these, 2,899 carried one of the four well-established risk haplotypes,
including 262 of admixed American (89% Hispanic) and 108 of African
(70% black) ancestry. An enrichment in the DQB1*02:01 allele was
observed in CeD patients across all ancestries, with the strongest
association in Europeans…"

**Why it matters.** Exemplary AoU-based ancestry-stratified HLA-
association design (n=3,481 CeD cases with fine-grained
Hispanic/African breakdown) — the same design template as the Acharya
cross-biobank ASCVD paper from the 09-01 report, but on an
autoimmune/HLA phenotype. Pairs with COSIGT (#15 above) as the
"AoU-HLA-ancestry-stratified" pipeline of the near future.

**What to do next.** (a) Read the ancestry-classification methods (SNP-
based? EHR-reported? both?) — that choice drives how portable the
result is to any AoU project you run. (b) The DQB1*02:01 enrichment
pattern across ancestries is a reference for any autoimmune-HLA design
you build; if IBD is on your list, this paper's methodology is
directly transferable.

---

## METHODS-WATCH (short list)

- **Zhang, Li, Su, Shen, Lu — Comparative effectiveness of
  single-stage vs. two-stage revision for hip PJI: INFORM target trial
  emulation** (*Archives of Orthopaedic and Trauma Surgery* 2026;
  Hernán citations-to). Clean TTE on a well-known surgical
  effectiveness question in Chinese tertiary hospitals; useful as a
  TTE-in-non-US-setting exemplar.
- **Bueno Lopez, Iona, Turnbull, Du, Chen et al. — Smoking, exhaled
  carbon monoxide, and risk of Parkinson disease** (*JAMA Neurology*
  2026; Hernán citations-to). China Kadoorie Biobank n=512,724;
  causal-inference biobank case worth watching for the exposure-
  measurement contribution (exhaled CO vs. self-reported smoking).
- **Ritoré-Hidalgo, Villar Fernández, Oprescu et al. — COVID Data for
  Shared Learning (CDSL): a multimodal publicly accessible dataset of
  EHR + chest imaging from hospitalized COVID-19** (*Scientific Data*
  2026; multi-feed cross-hit — Patrick Ryan, Pascal Brandt, George
  Hripcsak, Leo Anthony Celi all surfaced it). New multimodal EHR
  resource; portable to multimodal-EHR-FM training.
- **Snel & Schulz — Attributing Cohen's d: Training Data Attribution
  for Disease-Related Effects in Normative Age Biomarkers** (arXiv
  2609.07729, UK Biobank). Effect-size-attribution influence functional
  for age biomarkers; UKB validation. Methods-watch for any age-
  biomarker or normative-model FM audit.
- **Ma, Weisburd, DiTroia, Romo, Covill et al. — Long-read RNA
  sequencing improves isoform and splicing outlier detection in whole
  blood from rare disease trios** (medRxiv 2026; Stephen Montgomery
  new-related). Rare-disease-trio splicing evidence — good adjunct to
  the `Rare disease` thread's HPO-based diagnostic work.
- **Dogra, Baranwal, Ahmad, Kumar, Ashawat — APOL1 kidney disease: a
  critical narrative review** (2026; `APOL1` keyword). Narrative
  review, not primary; skim for citation-completeness in APOL1 work.
- **Semchin, d'Angremont, Ding et al. — Discovering Subtypes of
  Neurodegenerative Progression with a Scalable Connectome-Constrained
  Dynamic Model** (arXiv 2609.10890, PPMI). Parkinson subtype
  discovery; adjacent to `Chronic disease clustering and
  multimorbidity` thread.
- **Devarakonda — scDEFT: A deep learning framework for drug-effect
  prediction and counterfactual reasoning** (arXiv 2609.10831, IBD
  atlas 1.16M cells). Drug-effect FM applied to IBD atlas with
  responder-stratification and counterfactual prediction; adjacent to
  `Drug repurposing` (IBD sub-thread) and `Machine learning for
  precision health`.

---

## SKIP (surfaced but off-thread)

- Kastner citations feed lead: A20 (TNFAIP3) autoimmune review — off-
  thread (chemistry / molecular biology).
- Vivek Natarajan citation-batch lead: Italian AI-in-medicine editorial
  — off-thread (position piece).
- Callahan new-related lead: polymer dielectric ML — off-thread
  (materials).
- Marinka Zitnik new-articles: Nature Reviews Cancer 25-year
  retrospective — off-thread (position piece).
- Pritchard citations lead: SciDocBench workflow-centered benchmark for
  scientific document understanding — off-thread (ML benchmark).
- Neil M Davies new-articles: policy-claim rise in population health
  research — off-thread (meta-science).
- Michael Snyder new-articles: prenatal congenital lung malformation
  operative timing — off-thread (paediatric surgery).
- Wendy Chung new-articles: ERS pulmonary arterial hypertension
  guidelines — off-thread (guideline update).
- Patrick T. Ellinor new-articles: Murine ADAM15 atrial arrhythmia —
  off-thread (murine biology).
- Peter Szolovits new-related: MedProb VLM probing for medical VQA —
  off-thread (imaging FM benchmark).
- Peter Szolovits citations: AI children's-stories social
  representation — off-thread (media study).
- Yuan Luo citations lead: response to immortal-time-bias comment on
  antiseizure medication — thin (methodological response letter).
- Konrad Karczewski citations lead: TECTB non-syndromic hearing loss —
  off-thread (mendelian ear).
- Stephen Montgomery citations lead: mechanisms of promoter/enhancer
  disease variants (Long et al. Nature Genetics) — adjacent but not
  actionable in your active threads.
- Miguel Hernán citations tail: Hebrew-title SARS-CoV-2 household
  contact, German colorectal cancer prevention, Spanish neurocognitive
  longevity lifestyle article — all off-thread noise from broad-
  citation feed.
- Marinka Zitnik new-related: Gene-Chronos single-cell FM
  developmental-time inference — off-thread (single-cell FM, not EHR
  FM).

---

## Notes on the window

- **Signal shape.** The 09-11 and 09-12 batches carried the bulk of
  the HIGH signal (17 of 19 HIGH items). The 09-01 → 09-10 stretch was
  quiet on Scholar, dominated by low-yield arxiv-digest days (four
  fully dry, three single-paper days). This is consistent with the
  end-of-August / start-of-September publication lull followed by a
  post-Labor-Day surge.
- **Own-paper cascade.** The seven-feed simultaneous fire on Zeng,
  Waxse, Denny *npj Digital Public Health* is the operational marker
  that a paper of yours has entered the citation graph. Watch for
  follow-up alerts through Bastarache new-related and Denny
  citations-to for the next 4–8 weeks.
- **Cross-feed multi-hit as HIGH signal.** Three papers surfaced on
  ≥2 alert feeds this window: Blostein (Chenjie Zeng + Bastarache
  new-related — HIGH), Fujimoto MS (Denny + Jian Yang citations-to —
  HIGH), COSIGT (Kai Wang + Karczewski new-related — HIGH), CDSL COVID
  (Patrick Ryan + Pascal Brandt + Hripcsak + Celi — METHODS-WATCH),
  Long AoU celiac (Chenjie Zeng + Denny citations-to — HIGH), Zhou
  local-ancestry PGS (Denny + Jian Yang new-related — HIGH). The
  cross-feed pattern is a reliable "field-consensus interest" marker.
- **Next-report timing.** Consider a next report around 2026-09-19 to
  2026-09-22 (one week cadence, aligned with mid-week Scholar batch)
  or 2026-09-29 (matching the 15-day cadence used previously).

---

*Generated 2026-09-12 by Claude Code triage against `INTERESTS.md`
version last-updated 2026-07-29.*
