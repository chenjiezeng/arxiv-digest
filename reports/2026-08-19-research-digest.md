# Research digest report — 2026-08-19

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-19 12:40Z** (~48 hours since the
last research-digest report, covering two arxiv-digest cron runs, one
large Google Scholar alert batch on 08-18, and two NCBI PubMed saved-
search batches on 08-18 and 08-19).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-18.md`, `2026-08-19.md`) | 08-18 → 08-19 daily crons | 08-18 surfaced **4 papers** (Bayesian epidemic-alignment g-computation for RSV; zero-inflated causal mediation w/ non-compliance; digital-health N-of-1 primer; "regression not to the mean" negative-weighting warning). 08-19 cron had not yet fired at the time of this report (scheduled 10:30 UTC; retrieval at ~12:40 UTC found no `digests/2026-08-19.md`). |
| No `arxiv-digest` email hits from GitHub | — | `arxiv-digest` continues to commit digests directly to the repo rather than emailing; the on-disk `digests/` tree *is* the feed. |
| Google Scholar alerts (author + citation feeds, 08-18 02:27Z batch) | 08-18 02:27Z | ~40+ author / citation feeds fired: Chenjie Zeng (self), Joshua C Denny (×2: new-related + citations-to), Kai Wang (×2), Konrad Karczewski (×2), Peter Szolovits (×2), Marinka Zitnik, Zhiyong Lu, Tiffany J Callahan, Stephen B Montgomery (×2), Yuan Luo (citations-to), Daniel Kastner (citations-to), George Hripcsak (×2), Miguel Hernán (citations-to), Vivek Natarajan (citations-to), Jian Yang (×2), Neil M Davies, Leo Anthony Celi, Gary S Collins, Wendy Chung, David Baker, George H Chen, Lisa Bastarache (×2), Jonathan K Pritchard (citations-to), Pascal Brandt, Fei Wang. Densest hits in the Karczewski citations-to and Denny citations-to clusters (both pull the same PUSL1 mitochondrial-tRNA paper and Panthera pangenomic splice-haplotype tool). |
| Google Scholar alerts (keyword feeds, 08-18 12:01Z batch) | 08-18 12:01Z | 10 keyword feeds fired: `UK Biobank`, `knowledge graph`, `electronic health records`, `Foundation models + electronic health records`, `autoimmune disorders/diseases`, `drug repurposing`, `All of Us research program`, `mendelian diseases`, `variant interpretation` / `variant classification`, `phenome wide association studies`, `rare diseases`. |
| NCBI PubMed saved-search alerts (08-18 12:49Z + 08-19 12:35Z) | 08-18 → 08-19 | Three saved searches fired both days: `All of Us`, `UK Biobank`, `drug repurposing`. 08-19 batch surfaced a **GEI-modulator biobank-scale method** (Liu et al. *Genome Res*), a multi-omics CAD PRS review (Su et al. *Ageing Res Rev*), and three AoU papers (early-onset CRC risk factors, glaucoma wearables, SOGI-measure validation). |

> Caveat: Scholar and PubMed emails contain title, authors, venue, and
> only the first ~2–3 lines of each abstract (Scholar) or citation-only
> metadata (PubMed). The reports below contextualize that metadata
> against your research threads; nothing here reflects full-text reading.
> `arxiv-digest` entries include the full abstract because the pipeline
> captures it. Author lists are truncated as they appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced this window. They cluster into five knots.

**Biobank-scale GxE and multi-omics-augmented PRS cluster (3 items).**
Liu Z, Ramteke, Anand, Gorla, Jeong, Sankararaman *Genome Res* 2026 —
a **biobank-scale method for learning modulators of gene–environment
interaction from multiple environmental exposures** simultaneously. This
is the direct-hit methods paper for the **PGS × exposure/environment
interactions** rising sub-thread you added to INTERESTS.md (Nagpal &
Gibson *Nat Genet* 2026 lineage), and specifically the "multiple
exposures at once" gap that most existing PGS × E work leaves open.
Su Q, Li, Hu, Huang, Mo, Huang, Pan *Ageing Res Rev* 2026 —
**multi-omics integration for coronary artery disease risk prediction**;
review-and-synthesis that maps onto the **multi-omics-augmented PRS**
sub-thread (Nightingale NMR / Olink / metabolomics stacked with PGS —
Shan UKB 2026 lineage). Perry J, Murzynowski, Kerrison, Day, Luan et al.
2026 (preprint on Research Square) — **rare genetic variation
underlying metabolic traits in the Fenland cohort**, framed against
UKB and AoU WES benchmarks. This lands on the **composite risk models
stacking PRS with rare pathogenic variants** thread and is directly
comparable to your prior read of the Baya *AJHG* 2026 misaligned-
individuals framing.

**Knowledge-representation-in-EHR cluster (2 items).** Yan Z, Huang,
Wang F, Su C IEEE ICDH 2026 — **Knowledge Graph–Guided Domain
Generalization for Computational Phenotyping: A Tutorial** (Fei Wang
group). This is a *direct hit* for the new `Knowledge representation
in EHRs and applications` thread — specifically the sub-topic on
**patient-level and cohort-level knowledge graphs from EHR** — with
the added angle that KG structure is used to **generalize computable
phenotypes across sites** (BioVU / AoU / MIMIC / UKB drift). Celi LA,
Dunn J, Wang F, Feng M *ACM Trans Intelligent Systems* 2026 (also
under the Fei Wang feed) — **Beyond Benchmarks: Toward Reliable,
Equitable, and Epistemically Honest AI for Digital Health**. Reads
as a companion piece to your existing scContam / MIA-scFM contamination-
audit interest, but on the digital-health-benchmark side; direct
scaffolding for the **EHR foundation models fairness and calibration
audits** sub-thread.

**LLM-assisted / expert-guided causal-inference cluster (2 items).**
The arxiv-digest surfaced two 08-16-submitted stat.ME / stat.AP
papers whose framing is squarely inside the "agentic / human-in-the-
loop observational-causal-inference pipelines" rising sub-thread:
Moriña *stat.ME* 2608.16537 — **Bayesian epidemic alignment for
causal evaluation of seasonal infectious-disease interventions**,
formalizing epidemic-clock alignment as a *model component* (not a
preprocessing step) so timing uncertainty propagates into every
causal contrast. Bhandari S, Kar, Daniels, Karmakar *stat.ME*
2608.15775 — **causal mediation analysis for zero-inflated longitudinal
data with treatment non-compliance and multiple mediators**, using
Bayesian enriched Dirichlet-process mixtures + a scalable
G-computation algorithm. Both extend the g-computation toolkit
in ways portable to CFTR-modulator persistence / GLP-1 RA persistence
mediation analyses.

**PheWAS × drug repurposing cluster (2 items).** Chen Y, Huang, Ou,
Qi, Jiang, Zhang, Cai *Int. J* 2026 — **Identifying Antidiabetic Drugs
for Lung Cancer Treatment Through Genetic Epidemiology, Multiomics
Integration, and Functional Validation** (surfaced by the `phenome wide
association studies` keyword feed). This is exactly the **EHR-based
drug-repurposing signals mined from real-world prescribing and outcomes**
sub-thread — with a PheWAS anchor and functional (A549 in vitro)
validation loop. Directly comparable in framing to Cui-Yao et al. on
GLP-1 RAs × cancer signals. Zhao Q, Ling, Alamin, Shu, Hong, Wang J
*IEEE Trans Comput Biol Bioinform* 2026 (PubMed 42611652) — **A
Knowledge Graph-Driven Multimodal Framework for Drug-Disease
Association Prediction**. Fits the **knowledge-graph / GNN approaches
with explainable hypothesis output** angle in the drug-repurposing
thread; multimodal (structure + text + KG) is the new direction.

**Chronic-disease-clustering + CFTR pharmacoepi cluster (3 items).**
Musah YM 2026 (thesis; surfaced via Denny citations-to) — **Modeling
Heterogeneous Trajectories of Chronic Kidney Disease Progression with
Finite Mixture Models Using the All of Us Dataset**. Direct-hit
combination of the **chronic disease clustering and multimorbidity**
thread and the **All of Us** thread — longitudinal-eGFR trajectory
clustering with AoU as the substrate. Yetişgin H, Bilgiç, Kürtül
Çakar, Akca Dinç et al. *Eur J Pediatr* 2026 (Chenjie Zeng self-alert
feed) — **Mental health, sleep, and quality of life following CFTR
modulator therapy: a longitudinal study of children with cystic
fibrosis and caregivers**. Direct-hit for the **CF / CFTR modulator
psychosocial-impact** sub-thread — outcome-side complement to the
CFTR-modulator eligibility papers you tracked earlier. Hanley MN,
Purvis, Limb, Saya, Bickerstaffe et al. *Eur J Hum Genet* 2026
(Chenjie Zeng self-alert) — **co-design and preliminary evaluation
of a comprehensive breast-cancer risk report incorporating polygenic
risk information**. Direct implementation-side companion to the
**PGS composite-risk / PGS-tails** thread — the "how do you actually
communicate a PRS-inclusive risk score to a real patient" question
that most of the tails/residuals literature ducks.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
by source, then by bucket.

### arxiv-digest surfacings (2026-08-18 → 2026-08-19)

#### METHODS-WATCH — Moriña D. *Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions.* arXiv 2608.16537v1 (stat.ME, 2026-08-17). Score 1 (keyword: g-computation).

Formalizes **epidemic-clock alignment as a model component** (not a
preprocessing step) in a Bayesian causal count model with
season-specific affine transformations that map calendar time to a
latent epidemic clock. Intervention effects are estimated on the clock,
not on calendar week. Uses negative-binomial observation, hierarchical
area/season/area-season effects, a shrunk Fourier epidemic curve, and
a continuous programme-intensity exposure. **Posterior g-computation**
yields prevented cases, prevented fractions, peak attenuation, and
epidemic displacement, under both a controlled and a dynamic contrast
(the latter propagating disease history within each arm). Two-tier
simulations under stable timing, epidemic-clock variation, intensity-
dependent ascertainment, and area-level confounding. Illustrated on
open Catalan primary-care surveillance + RSV immunisation data. Not
directly on-thread for any single INTERESTS.md line, but a **methods-
watch pickup for any seasonal-outcome pharmacoepi TTE** where calendar-
alignment quietly conflates epidemic phase with intervention effect
— which describes essentially every influenza-season, RSV-season, or
respiratory-virus pharmacoepi analysis on the AoU / UKB watchlist.

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. *Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.* arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1 (keyword: g-computation).

Bayesian causal-mediation framework built on **enriched Dirichlet-
process mixture models** with a **scalable G-computation algorithm**
for zero-inflated longitudinal outcomes and mediators, in the presence
of treatment non-compliance and multiple mediators. Application is
digital marketing (email campaign / free-shipping vs price-discount),
not biomedical — but the *methods pattern* is directly portable:
substitute "email-opening" with "medication-initiation compliance",
"purchase" with "MPR / persistence", and "value-added incentive" with
"drug class assignment", and this is exactly the multi-mediator,
zero-inflated, non-compliance-prone setup that CFTR-modulator
persistence, statin discontinuation, HRT persistence, and GLP-1 RA
persistence analyses face. The G-computation formulation makes it
readable against the egg-computation paper from the 2026-08-17 report.

#### METHODS-WATCH — Daza EJ. *A Primer on Digital Health N-of-1 Studies and Single-Case Designs.* arXiv 2608.15526v1 (stat.AP, 2026-08-16). Score 1 (keyword: precision medicine).

Chapter-length **primer on N-of-1 designs and single-case ("multitudinal")
approaches for digital health**. Reframes precision medicine as
"characterize the individual's own recurring patterns first, then decide
if a subgroup label is even needed", explicitly against the group-
average-guides-individual paradigm. Ends with a section on "esametry"
— the statistics of the digitized multitudes within each person.
Directly relevant to the **ML for precision health** thread's
individualized-risk-prediction and treatment-effect-heterogeneity
sub-topics, and to the wearable-data threads (the 2026-08-07 arxiv
Zhang et al. AoU Fitbit-PRS-MDD paper is the population-level
counterpart to Daza's individual-level framing). Not a methods paper
per se, but a reference-quality framing document.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. *Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.* arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1 (keyword: heterogeneous treatment effects).

**Constant-treatment-effect models under staggered treatment and
treatment-effect heterogeneity can produce estimates with the wrong
sign** — a weighted average with negative weights across durations.
Extends the linear-regression version of this critique (de
Chaisemartin & D'Haultfœuille et al.) to **logistic regression**,
using a drug-induced-homicide × overdose-deaths natural experiment.
For linear link: constant-effect RR 0.977 (CI 0.866–1.101) vs
average RR 0.728 (0.507–0.979) across durations. Logistic link:
constant 1.064 vs average 0.739. Direct methods-watch flag for
**every TTE with staggered start-of-follow-up on the AoU / UKB
watchlist** where the analyst reports a single hazard ratio: the
negative-weighting pathology may be masking real heterogeneous
effects. Pairs with Wood et al. arXiv 2608.11108 from the 08-17
report (pregnancy TTE time-zero) as the analytic-model twin to that
paper's design-side warning.

*(No papers on 2026-08-14 through 2026-08-17 — six consecutive dry
crons — and 2026-08-19 had not yet fired at the time of this report.)*

### Google Scholar author / citation feeds (2026-08-18)

#### HIGH — Yan Z, Huang Z, Wang F, Su C. *Knowledge Graph–Guided Domain Generalization for Computational Phenotyping: A Tutorial.* IEEE 14th International Conference on Healthcare Informatics 2026. Surfaced via Fei Wang author feed.

Tutorial-length paper from the Fei Wang / Cornell group on **using
biomedical knowledge graphs to make computable phenotypes generalize
across sites**. Frames computational phenotyping as needing to
integrate heterogeneous data (EHRs, registries, imaging, multi-omics)
across deeply phenotyped research cohorts, and uses KG structure as
the *domain-generalization scaffold* that lets a phenotype trained
on site A survive on site B. This is a **direct-hit paper** for the
`Knowledge representation in EHRs and applications` thread you added
last month — specifically the "patient-level and cohort-level
knowledge graphs from EHR" and the "fidelity, portability, and audit
of representations" sub-topics. Read alongside the Lemieux *JAMIA
Open* 2026-07 FHIR-representation-consequences paper you flagged as
the reference framing paper for that thread; the two together form
the theoretical spine for a representation-ablation-vs-site-drift
research plan.

#### HIGH — Celi LA, Dunn J, Wang F, Feng M. *Beyond Benchmarks: Toward Reliable, Equitable, and Epistemically Honest AI for Digital Health.* ACM Transactions on Intelligent Systems and Technology 2026. Surfaced via Fei Wang author feed.

Reference-quality position paper (Celi–Dunn–Wang–Feng, a heavy roster)
naming the **fundamental tension in digital-health AI**: development
data and validation metrics bear little resemblance to deployment
conditions. Reads as the digital-health-benchmark-audit companion to
the scContam / MIA-scFM contamination-audit lineage you flagged for
CLMBR / MOTOR / MEDS benchmarking. Direct scaffolding for the
**EHR foundation models fairness and calibration audits** sub-thread
and for the "epistemically honest" framing you can borrow when writing
about any of the CLMBR / MOTOR benchmark results. Since Celi and
Wang co-author, this and the Yan-et-al. tutorial above should be
read as a matched pair.

#### HIGH — Musah YM. *Modeling Heterogeneous Trajectories of Chronic Kidney Disease Progression with Finite Mixture Models Using the All of Us Dataset.* South Dakota State University 2026 (thesis). Surfaced via Joshua C. Denny citations-to feed.

Thesis / dissertation applying **finite-mixture-model trajectory
clustering to longitudinal eGFR data from the All of Us Research
Program** to characterize heterogeneous CKD progression and identify
factors associated with faster-vs-slower decliners. Direct-hit
combination of two INTERESTS.md threads: **chronic disease clustering
and multimorbidity** (trajectory clustering method) and the
**All of Us biobank cohort** (data substrate). Even at thesis-level
maturity this is worth noting because AoU's longitudinal EHR depth
is finally deep enough to support this class of analysis — the
population-level answer to APOL1-conferred CKD-progression risk
stratification (a disease thread you already track) may want a
trajectory-cluster prior before jumping to Cox proportional hazards.

#### HIGH — Hanley MN, Purvis R, Limb S, Saya S, Bickerstaffe A et al. *The co-design, development, and preliminary evaluation of a comprehensive breast cancer risk report incorporating polygenic risk information.* European Journal of Human Genetics 2026. Surfaced via Chenjie Zeng self-alert feed.

**Implementation-side counterpart** to the PGS tails-and-residuals
literature you track. Where Souaiaia *Nature* and Baya *AJHG* frame
PGS as a *discovery instrument*, this paper is about how you
actually communicate a PRS-inclusive comprehensive risk score to a
patient — co-design with consumers, iterative user testing,
preliminary evaluation. Bridges the **PGS composite-risk / PGS-tails**
thread to the return-of-results / clinical-implementation side that
your ClinGen / variant-interpretation thread also cares about. Worth
a citation slot in any AoU / UKB breast-cancer PRS paper that
gestures at clinical utility.

#### HIGH — Yetişgin H, Bilgiç I, Kürtül Çakar M, Akca Dinç G et al. *Mental health, sleep, and quality of life following CFTR modulator therapy: a longitudinal study of children with cystic fibrosis and caregivers.* European Journal of Pediatrics 2026. Surfaced via Chenjie Zeng self-alert feed.

Longitudinal pediatric CF study evaluating **CFTR modulator effects
on sleep and mental health in children and caregivers** — an outcome-
side complement to the CFTR-modulator eligibility & psychosocial-
impact sub-thread on your list. The dyadic (patient + caregiver)
design is what makes it stand out: modulator effects on caregiver
mental health are essentially unstudied in the AoU pediatric-adjacent
literature, and are the kind of "modulator eligibility & psychosocial
impact" question CF adults ask in the clinic constantly. If you're
prototyping an AoU CFTR-modulator-persistence analysis, this is a
sensitivity-analysis anchor — modulator discontinuation may correlate
with caregiver-mental-health signals that are visible in AoU's
survey battery even without a linked pediatric cohort.

#### HIGH — Perry J, Murzynowski J, Kerrison N, Day F, Luan J et al. *Exploring Rare Genetic Variation Underlying Metabolic Traits in the Fenland Cohort.* Research Square 2026 preprint. Surfaced via `All of Us research program` keyword feed.

WES-based **rare-variant × metabolic-trait analysis in the Fenland
cohort**, explicitly framed against UKB and AoU as reference biobanks.
Direct-hit for the **composite risk models stacking PRS with rare
pathogenic variants** thread and for the **biobanks with EHR linkage:
AoU / UKB / MVP / BioVU** thread. Fenland is smaller than AoU or UKB
but has extremely deep metabolic phenotyping (MRI, DEXA, CGM,
metabolomics) — read this alongside Abner et al. *Nature* 2026 (from
the 08-17 report; diurnal-glucose GWAS on UKB CGM-like data) and
Baya *AJHG* 2026 misaligned-individuals framing to triangulate a
"deep metabolic phenotyping + rare-variant burden + PGS residuals"
research plan.

#### MEDIUM — Cher WY, Agarwal T, Sun P, Ow JR, Tabaglio T et al. *Panthera: a deep learning pan-genomic splice haplotypes identification tool.* Scientific Reports 2026. Surfaced via Karczewski + Denny citations-to feeds (cites gnomAD constraint).

Open-source tool (GitHub-released) for **high-throughput pangenomic
analysis of splice haplotypes** — the argument is that current
spliceogenic-variant annotators (SpliceAI, Pangolin, etc.) work on
single DNA variants against a single reference genome, and that
considering *splice haplotypes* under pangenomic reference improves
accuracy of spliceogenic-variant calls. Directly relevant to the
**variant interpretation (ACMG / ClinGen)** thread's splicing / RNA
evidence for VUS resolution sub-topic, and to the **pangenome-informed
variant calling** sub-thread you added under genetic epi. Worth
benchmarking against SpliceAI on your CFTR VUS shortlist before
downstream investment.

#### MEDIUM — Rebelo-Guiomar P, Kra-Oz N, Powell C, Jouret G et al. *The pseudouridine synthase PUSL1 modifies U39 of mitochondrial tRNAs and is linked to human neurological phenotypes.* Nucleic Acids Research 2026. Surfaced via Karczewski + Denny citations-to feeds (cites gnomAD).

Mechanistic paper — PUSL1 modifies mitochondrial tRNAs, and PUSL1
variants are linked to neurological phenotypes in humans. On-thread
for the **rare disease** sub-thread (mitochondrial disorders as a
neurodevelopmental / neurological rare-disease space); the gnomAD
constraint citation is the population-frequency-anchor for their
variant-pathogenicity argument. Second-tier interest given the narrow
gene focus, but a nice example of how a small clinical series can be
strengthened by the population-constraint / mutation-tolerance
framework you already work in.

#### MEDIUM — Oshi M, Kawashima K, Sugimori M, Yamada A, Shah Z et al. *Somatic BRCA alterations in breast cancer are associated with distinct biological and clinical patterns according to germline BRCA status.* ESMO open 2026. Surfaced via Chenjie Zeng self-alert feed.

Empirical study of **somatic BRCA alterations in breast cancer,
stratified by germline BRCA status**. Establishes that germline vs
somatic BRCA hits carry different biological / clinical fingerprints —
which matters both for **variant interpretation** (ACMG / ClinGen
splitting somatic vs germline evidence) and for the **breast-cancer
PGS composite-risk framing** (where germline BRCA + PGS + somatic
BRCA is arguably the correct three-way stratification, not the
usual germline-only stratification). If you're building a case
for a "somatic-mutation contamination of germline rare-variant scans"
QC layer (which was one of the CHIP / VEXAS / LOY sub-thread bullets),
this paper is on the tumor-suppressor side of that same argument.

#### MEDIUM — Baiju N, Waaseth M, Sætrom P, Sandanger TM et al. *Associations of whole blood gene expression with menopausal status and hormone therapy use in the NOWAC postgenome cohort.* Scientific Reports 2026. Surfaced via Chenjie Zeng self-alert feed.

Whole-blood transcriptomics × **menopausal status × HT use** in
NOWAC (Norwegian Women and Cancer) postgenome cohort. Direct-hit
for the **HRT persistence** sub-thread (which sits under the
pharmacoepi drug-class thread with GLP-1 RAs and CFTR modulators);
the transcriptomic-signature angle gives you an intermediate
biomarker for whether an HRT-persistence analysis in AoU / UKB has
biological plausibility for a downstream effect. Second-tier for
being cross-sectional and single-cohort, but a useful reference
when framing why HT persistence is an outcome worth measuring.

#### MEDIUM — Nyberg F, Lundmark P, Blomberg A, Dekkers K et al. *Genome-wide association study of image-based emphysema scoring in the Swedish CArdioPulmonary bioImage Study (SCAPIS) suggests two new risk loci in smokers.* Respiratory Research 2026. Surfaced via Joshua C. Denny new-related feed.

CT-emphysema GWAS in SCAPIS with two novel loci in smokers. Not
directly on-thread but a good exemplar of the **imaging-derived-
phenotype GWAS** pattern (image-quantified continuous trait, not an
ICD/phecode outcome) that the AoU CT-and-MRI cohort will eventually
enable at scale. Worth remembering as a template when the AoU
imaging modality expansion catches up to UKB.

#### MEDIUM — Park P, Choi Y, Park S, Han J, Kim J, Ryu B, Shin D et al. *Development and Open-Source Release of a Multi-Cancer Module for Structuring Pathology Reports.* Research Square 2026 preprint. Surfaced via Denny citations-to feed (cites MedEx).

**Scalable NLP framework for structuring multi-cancer pathology reports**
with external validation and an open-source release. Fits the
**NLP-derived representations from clinical notes** sub-topic under
your `Knowledge representation in EHRs and applications` thread —
pathology reports are one of the harder note types to structure at
scale and are the raw material for tumor-registry-quality outcomes
in an EHR-linked cohort. If AoU or BioVU wants tumor-stage-and-grade
as first-class variables, this class of tool is the on-ramp.

#### METHODS-WATCH — Chen Y, Huang X, Ou J, Qi F, Jiang P, Zhang T, Cai S. *Identifying Antidiabetic Drugs for Lung Cancer Treatment Through Genetic Epidemiology, Multiomics Integration, and Functional Validation.* International Journal (venue unclear from snippet) 2026. Surfaced via `phenome wide association studies` keyword feed.

Combines **genetic epidemiology, multi-omics integration, PheWAS,
functional enrichment, PPI-network mapping, somatic mutation
profiling, and A549 in vitro validation** to identify antidiabetic
drugs repurposable for lung cancer. Direct-hit for the **drug
repurposing** thread's EHR-based-signals-with-a-clinical-evidence-loop
angle; the PheWAS anchor is the specific hook that pulled it into
your feed. Framing is closer to Mendelian-randomization-triangulated
observational-cohort drug-target estimation (Saxby metformin × AAA
lineage you already track) than to pure ML-KG link prediction —
worth reading for the *methods pattern*, even if the specific
antidiabetic-drug × lung-cancer signal is hypothesis-generating.

#### METHODS-WATCH — Bentley AR, Soremekun O, Adeyemo AA. *Genomics and Cardiometabolic Diseases in Africa.* Genomics in Africa (book chapter) 2026. Surfaced via `All of Us research program` keyword feed.

Book-chapter review of **cardiometabolic genomics in African-ancestry
populations**, framed against H3Africa, All of Us, and TOPMed as
representation-gap remediation initiatives. Not a primary research
paper but a reference-quality contextualization for any AoU African-
ancestry analysis you write; also useful backup for the ancestry-
stratified-risk-in-EHR-linked-cohorts angle under the biobank thread.

### NCBI PubMed saved-search alerts (2026-08-18 → 2026-08-19)

#### HIGH — Liu Z, Ramteke A, Anand A, Gorla A, Jeong M, Sankararaman S. *A biobank-scale method for learning modulators of gene-environment interaction underlying human complex traits from multiple environmental exposures.* Genome Research 2026 (PMID 42613154, published 2026-08-18).

**Methods paper for biobank-scale GEI discovery across multiple
environmental exposures simultaneously.** The "multiple exposures at
once" framing is the key differentiator vs the standard one-exposure-
at-a-time GEI tests. This is the direct-hit methods paper for the
**PGS × exposure / environment interactions** rising sub-thread
(Nagpal & Gibson *Nat Genet* 2026 lineage), and pairs with the
Abner et al. *Nature* 2026 diurnal-glucose paper from the 08-17
report as the analytic-method twin to that paper's chronotype × PGS
substrate. Directly runnable on UK Biobank; portable to AoU once
enough environmental exposure variables reach the WGS-linked cohort.

#### HIGH — Su Q, Li QY, Hu CK, Huang Y, Mo LR, Huang WZ, Pan DG. *Precision Medicine Breakthrough: Multi-Omics Integration Elevates CAD Risk Prediction.* Ageing Research Reviews 2026 (PMID 42612709, published 2026-08-18). Review.

Review of **multi-omics integration for CAD risk prediction** —
review-and-synthesis of the multi-omics-augmented-PRS literature
that maps onto the **Nightingale NMR / Olink proteomics / metabolomics
stacked with PGS** sub-thread. Second-tier for being a review rather
than a primary methods paper, but a good citation anchor for the
"multi-omics stacking meaningfully beats PGS-alone for CAD" claim
that the sub-thread turns on.

#### HIGH — Nigam A, Onongaya C, Meshram P, Frebault J, Gaertner W, Ikramuddin S, Harmon JV Jr, Goffredo P. *Traditional Risk Factors Are Not Associated with the Rise of Early-Onset Colorectal Cancer: An All of Us Study.* Diseases of the Colon and Rectum 2026 (PMID 42610385, published 2026-08-18).

**All of Us case-control study** of early-onset CRC finding
traditional risk factors do NOT explain the observed rise. Directly
relevant to the **biobanks with EHR linkage: All of Us** thread and
to the **chronic disease clustering and multimorbidity** thread
(cancer as a young-onset outcome with a shifting risk-factor
profile). Worth reading as a substantive AoU EHR-phenotyping
example — traditional-risk-factor "no association" findings in AoU
often reveal ascertainment issues at least as often as they reveal
true epidemiology, so this needs a careful methods read; but if the
finding holds, the young-onset-CRC etiology gap opens up rare-variant
+ environmental + microbiome sub-questions that AoU is uniquely
positioned to answer.

#### HIGH — Zhao Q, Ling Q, Alamin MH, Shu P, Hong Y, Wang J. *A Knowledge Graph-Driven Multimodal Framework for Drug-Disease Association Prediction.* IEEE Transactions on Computational Biology and Bioinformatics 2026 (PMID 42611652, published 2026-08-18).

**KG-driven multimodal drug-disease-association prediction** —
directly on-thread for the **drug repurposing** interest, specifically
the "knowledge-graph / GNN approaches with explainable hypothesis
output" angle. Multimodal (structure + text + KG) is the new
direction beyond pure KG link prediction. Would want to look at
whether the path-based explanations are usable clinically, or whether
they are the usual "top-N most-important edges" hand-wave — the latter
is what most KG-explainer papers deliver, and it's not enough for a
clinical-evidence-loop drug-repurposing pipeline.

#### MEDIUM — Bernstein I, Jafry S, Singh K, Wang SY. *Assessing physical activity and sleep patterns in glaucoma using wearable devices.* British Journal of Ophthalmology 2026 (PMID 42613167, published 2026-08-18).

**AoU wearable-device analysis** of physical activity and sleep in
glaucoma — a substantive AoU analysis on the wearables front, though
outside your primary disease threads. Fits the **All of Us +
wearables** substrate pattern that the Zhang et al. 2026-08-07
arxiv Fitbit-PRS-MDD paper also uses; the two together validate
that the Fitbit substrate in AoU is now mature enough for outcome-
specific studies at scale. Worth remembering for the substrate-scale
argument even if the glaucoma target isn't on the tracked disease
list.

#### SKIP — Gaughan SJ, Tien PC, Obedin-Maliver J, Ceja A, Tran NK, Kaplan RL et al. *Validation of an Extended Sexual Orientation and Gender Identity Measure in a Racially and Ethnically Diverse Cohort of People Living with or at Risk for HIV Infection.* AIDS Behav 2026 (PMID 42611398).

Measure-validation study in an HIV-adjacent cohort; not on-thread.

#### SKIP — the seven remaining `drug repurposing` PubMed hits (Trojan mast cells / colon-cancer aptamer / Penfluridol × mycobacteria / antibacterial immunotherapy / OA synovium / JAK2 STAT3 SOCS3 × colon / thiazolidinones × ERα breast cancer)

All wet-lab or chemistry-only drug-target / drug-delivery pipelines
without an EHR-based clinical-evidence loop. Per INTERESTS.md, these
are lower-priority for the drug-repurposing thread — noted only for
completeness.

### Scholar author feeds (2026-08-18): remaining METHODS-WATCH / MEDIUM items

The 08-18 02:27Z Scholar batch fired 40+ author / citation alerts.
Beyond the HIGH items broken out above, the following bear a brief
mention against your active threads:

- **METHODS-WATCH** — Farajidizaji M, Raina V. *Task Competence Is Not
  Instruction Following: Evaluating Instruction-Conflicting Behavior in
  Small Language Models.* arXiv 2607.19608 (Szolovits new-related).
  General LLM-evaluation methods work, portable to the LLM-as-clinical-
  reasoner space you touch via the egg-computation / oci-agent thread.

- **METHODS-WATCH** — Bann D, Wang M, Davies NM, Wright L, O'Connor et al.
  *Science or Advocacy? The Global Rise of Policy Claims and Calls to
  Action in Population Health Research (1990-2024).* Am J Public Health
  2026 (Neil M Davies new articles). Meta-scientific audit of causal-
  language creep in population health; a useful mirror for your own
  "associations stay associations" writing discipline.

- **METHODS-WATCH** — Allery F, Pineda-... et al. *Mitigating health
  inequities with machine learning: a nationwide cohort study
  developing and evaluating ethnicity-specific cardiovascular risk
  prediction models across …* (Gary S Collins new articles). External-
  validation-across-ancestries paper on ML CV risk prediction — on-
  thread for the ML-for-precision-health "external validation across
  sites or ancestries" sub-topic.

- **METHODS-WATCH** — Pocobelli G, Hyun N, Shaw PA, Bakoyannis L et al.
  *Empirical application of missing data methods to address
  confounding in health insurance claims-based analyses using
  electronic health records available on a subset* (Patrick Ryan new-
  related). Directly relevant to the OMOP / EHR phenotyping thread —
  missing-data-in-claims-plus-EHR is the recurring headache for AoU
  and MVP analyses that need both claims and encounter records.

- **METHODS-WATCH** — Yamamoto R, Tohyama T, Han A, Pedersen N et al.
  *Impact of an ROX index-guided intubation strategy on mortality in
  patients receiving high-flow nasal cannula: a target trial emulation*
  (Leo Anthony Celi new articles). Textbook TTE in an ICU cohort —
  clinical-focus paper but the TTE-with-decision-support-trigger
  design is what makes it worth a bookmark.

- **METHODS-WATCH** — Ao X, Kolifarhood G, Parisien M, Bortsov A,
  Grant AV et al. *Exome-wide association study reveals common and
  rare coding variants shaping chronic pain in 327642 UK biobank
  participants.* Genome Medicine 2026 (Jian Yang new-related).
  UKB WES × chronic-pain exome-wide; on-thread for the composite-
  risk / rare-variant thread. Chronic pain is outside your tracked
  diseases but the *design* is what to remember.

- **MEDIUM** — Guo X, Hu J, Tian H, Yan C, Liu Q, Zhou T, Liu C et al.
  *Trans-ancestry meta-analysis of genome-wide association study
  identifies eight novel genetic loci in type 1 diabetes: A multi-
  population study.* Diabetic Medicine 2026 (Denny new-related).
  T1D trans-ancestry GWAS with 8 novel loci; on-thread for the
  genetic-epi + PGS-portability sub-topics but not a direct hit for
  your active disease threads.

- **MEDIUM** — Heigh V, Zhang X, Abdelmagid MG, Ongie L, Lasho TL et
  al. *Fetal Hemoglobin in Bone Marrow Failure Syndromes: Comparative
  Utility Versus PNH Clones and Telomere Length.* Blood Red Cells &
  Iron 2026 (Chenjie Zeng self-alert). Bone-marrow-failure-syndrome
  differential-diagnosis biomarker paper — adjacent to your own IBMFS
  interest but outside the tracked disease threads.

- **MEDIUM** — Rare-disease citation-to hits linked to gnomAD constraint
  (DLG4-related synaptopathy Cureus 2026, UBTF-related neurodegeneration
  JMG 2026): both use `A genomic mutational constraint map using
  variation in 76,156 …` as a variant-pathogenicity anchor — routine
  usage, worth noting only as substrate-scale evidence that the
  constraint-map framework is now baseline for clinical rare-disease
  variant curation.

- **SKIP** — the citation-echo papers in cell / molecular biology
  (spatial-vista, m6A prediction, RNA editing, nuclear speckle
  chromatin niches, magnetic hydrogels for bone diseases, PFAS ×
  lipids, etc.). Not on-thread.

---

## Thread coverage table

Cross-checking this window's HIGH-priority items against `INTERESTS.md`
active threads:

| Thread | Items surfaced | Notes |
| --- | --- | --- |
| PheWAS / phecode infrastructure | 1 | Chen et al. antidiabetic × lung cancer (PheWAS-anchored drug-repurposing) |
| Biobanks with EHR linkage (AoU / UKB / MVP / BioVU) | 4 | Musah AoU-CKD trajectories; Perry Fenland WES vs UKB/AoU; Nigam AoU early-onset CRC; Bernstein AoU wearables × glaucoma |
| EHR phenotyping & OMOP | 1 | Yan et al. KG-guided computational-phenotype domain generalization |
| Causal inference & pharmacoepi | 2 | Moriña Bayesian epidemic-clock g-computation; Bhandari zero-inflated causal mediation w/ non-compliance |
| Variant interpretation (ACMG / ClinGen) | 2 | Cher Panthera pangenomic splice haplotypes; Oshi somatic vs germline BRCA |
| Genetic epidemiology | 3 | Liu et al. biobank-scale GEI-modulator method; Su et al. multi-omics CAD PRS; Perry Fenland rare variants |
| CF / CFTR modulators | 1 | Yetişgin et al. modulator × mental health / sleep / QoL pediatric |
| APOL1 | 0 | — |
| CHIP / VEXAS / LOY | 0 | Oshi somatic-vs-germline BRCA framing partially on-thread |
| IBD | 0 | — |
| EHR foundation models | 1 | Celi et al. Beyond Benchmarks digital-health AI audit |
| Knowledge representation in EHRs | 2 | Yan KG-guided phenotyping; Park pathology-report NLP structuring |
| Knowledge graphs & ontologies | 2 | Yan KG-guided phenotyping; Zhao KG-multimodal drug-disease prediction |
| Drug repurposing | 2 | Chen antidiabetic × lung cancer; Zhao KG-multimodal drug-disease |
| Rare disease | 1 | Rebelo-Guiomar PUSL1 mitochondrial neurological phenotypes |
| ML for precision health | 3 | Daza N-of-1 primer; Kung regression-not-to-mean; Allery ethnicity-specific CV risk |
| Chronic disease clustering & multimorbidity | 1 | Musah AoU-CKD-trajectory finite-mixture-model clustering |
| PGS composite-risk (tails-and-residuals rising sub-thread) | 2 | Hanley PRS-inclusive breast-cancer risk report; Liu GEI-modulator |

Weakest coverage this window: **APOL1**, **CHIP/VEXAS/LOY**, and **IBD**
disease threads were entirely dry, and the **agentic causal-inference**
sub-thread saw no direct hits (the arxiv-digest g-computation-tagged
papers were on the design/method side, not the LLM-agent side; no new
`oci-agent`-family follow-ups). Consider a manual arxiv scan under
`cs.LG × causal inference × agent` if the sub-thread stays dry for
another two weeks.

---

## Reading queue (priority order)

1. Liu Z et al. *Genome Res* 2026 biobank-scale GEI-modulator method — PMID 42613154.
2. Yan Z, Huang Z, Wang F, Su C IEEE ICDH 2026 KG-guided phenotyping tutorial.
3. Musah YM 2026 AoU-CKD finite-mixture-model trajectories (thesis).
4. Hanley MN et al. *Eur J Hum Genet* 2026 co-designed breast-cancer PRS-inclusive risk report.
5. Celi LA, Dunn J, Wang F, Feng M *ACM TIST* 2026 Beyond Benchmarks digital-health AI.
6. Perry J et al. Fenland WES rare-variant metabolic-trait analysis (Research Square).
7. Yetişgin H et al. *Eur J Pediatr* 2026 CFTR modulator × mental health / sleep pediatric.
8. Cher WY et al. *Sci Rep* 2026 Panthera pangenomic splice-haplotype tool.
9. Moriña D arXiv 2608.16537 Bayesian epidemic-clock g-computation.
10. Chen Y et al. antidiabetic × lung cancer PheWAS + multiomics drug-repurposing paper.

Items 1, 2, 3, 5 are the ones that most directly extend rising
sub-threads in INTERESTS.md; items 4 and 6 sit inside established
threads but at rare pivot points (implementation-side PRS, deep-
metabolic-phenotyping + rare-variant); item 7 is the CF outcome
paper that connects most cleanly to your existing CFTR-modulator
persistence prototype.
