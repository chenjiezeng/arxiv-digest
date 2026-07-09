# Research digest report — 2026-07-09

Triage of research-related email + the local `arxiv-digest` output
against the active threads in `INTERESTS.md` (PheWAS/phecodes,
EHR-linked biobanks, EHR phenotyping/OMOP, causal inference &
pharmacoepi, variant interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/
IBD disease threads, EHR foundation models, KGs/ontologies, drug
repurposing, rare disease, ML for precision health, multimorbidity).

Window: **2026-07-01 → 2026-07-09** (since the prior 2026-06-20 report;
no report was cut for the intervening days, so this covers a longer
window than usual).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-07-01 → 07-09 | Two large batches (07-06 22:10Z Jian-Yang-centric author feed; 07-08 07:31Z multi-author batch spanning Chute, Denny, Hripcsak, Bastarache, Karczewski, Zeng, Callahan, Ryan, Brandt, Chung, Kastner, Montgomery, Pritchard, Szolovits, Zitnik, Gusev, Vogelstein, Luo, Chute, Yang, Hernán, Natarajan). 07-09 00:40Z keyword feeds (foundation-models+EHR, UK Biobank, EHR, KG, rare disease, drug repurposing, AoU, variant interpretation). |
| `arxiv-digest` local repo (`digests/`) | 2026-07-01 → 07-08 | 10 daily digests generated. On-thread hits: **07-01 (7 papers, 3 previously suppressed), 07-02 (1), 07-03 (1), 07-04–07-06 (dry), 07-07 (3), 07-08 (1)**. The 06-30 digest also surfaced 4 papers just before this window opened. |
| GitHub `arxiv-digest` email notifications | 07-01 → 07-09 | **None** in this window. The digest is generated in-repo (daily commits) rather than pushed by email — no PR/issue/action notifications arrived. |

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. arXiv digest entries include
> the full abstract. The reports below are triaged against your INTERESTS.md
> threads; nothing here reflects full-text reading.

---

## Executive summary

- **Cross-ancestry PRS methodology hit a Nature Genetics landmark.** Xu,
  Dong, Zeng, Bian, Zhou, Guan, Zhao — *MIXPRS enables multi-population
  and multi-method polygenic risk scores using summary statistics*
  (**Nature Genetics**, 2026). Summary-stats-only integration across
  ancestries + across PRS methods, addressing the "no single method
  wins" problem that has plagued trans-ancestry PRS. Directly on your
  **Genetic epidemiology → cross/trans-ancestry portability** thread.
  **HIGH — read first.** *(Jian Yang related-research feed, 07-06.)*
- **Triple-feed on within-sibling PRS attenuation methods.** Kelly,
  Onuorah, Gilbert — *Within-sibling attenuation of polygenic risk
  score accuracy: investigating the effects of principal component
  analysis, LD score regression, and mixed model association in the UK
  Biobank* (**Human Genetics**, 2026). Surfaces simultaneously in the
  **Joshua Denny**, **George Hripcsak**, and **Lisa Bastarache**
  related-research feeds. Directly interrogates the PC/LDSC/LMM
  confounder-adjustment toolkit that underpins essentially every PRS
  paper you cite — the sibling design gives a clean estimate of what
  each of those adjustments actually strips out (and what leaks). **HIGH.**
  *(Denny 07-08; Hripcsak/Bastarache 07-08 same batch.)*
- **VUMC EHR-based growth-chart framework for genetic disorders in your
  own related-research feed.** Shyr, Tinker, Brown, Wright, Peterson et
  al. — *An EHR-based framework for modeling growth curves and
  constructing growth centile charts for genetic disorders*
  (**npj Genomic Medicine**, 2026). VUMC group (Wright, Peterson). Sits
  exactly at the **EHR phenotyping** × **Rare disease** intersection —
  building disorder-specific growth reference curves from routinely
  collected EHR heights/weights so patients with rare disorders can be
  benchmarked to a same-condition, not general-population, centile.
  **HIGH.** *(Chenjie Zeng related-research feed, 07-08.)*
- **CFTR modulator thread is active in *your own* related-research feed
  again.** Two papers on the same day: (1) Downes et al. — *MATRIARCH_CF*,
  a prospective observational study of pregnancy and parenthood on CFTR
  modulators in females with CF (**BMJ Open Respiratory Research**, 2026),
  and (2) AlMunefi et al. — systematic review of ETI (Elexacaftor/
  Tezacaftor/Ivacaftor) impact on airway and systemic inflammation
  (**Annals ATS**, 2026). Directly on your **CF/CFTR** disease thread
  and specifically on the **modulator pharmacoepi / real-world outcomes**
  angle (pregnancy — a subgroup excluded from the modulator RCTs; and
  systemic-inflammation biomarker response — the mechanistic middle
  layer between modulator and clinical outcomes). **HIGH (both).**
- **Target-trial emulation lands in the Chute feed.** Kagenaar,
  Lugo-Palacios, Aggarwal et al. — *Stereotactic ablative radiotherapy
  (SABR) versus surgical resection for early-stage NSCLC: an Emulated
  Target Trial* (**Journal of Clinical Oncology**, 2026). Clean example
  of target-trial emulation for a treatment choice where the RCT hasn't
  and probably won't happen at scale (SABR-vs-surgery in operable
  early-stage lung cancer). Directly on the **causal inference /
  pharmacoepi (target-trial emulation)** thread; the *design* is the
  reason to read, even though the disease is off your core threads.
  **HIGH (methods).**
- **Variant-ranking ML tool for rare disease in Wendy Chung's own-
  articles feed.** Zhang, Ahsan, Wang, Lin, Campbell et al. — *RankVar:
  machine learning-based variant ranking and reinterpretation for rare
  genetic diseases* (**Genome Medicine**, 2026). Directly on your
  **Variant interpretation (ACMG/ClinGen)** thread — RankVar reinterprets
  DNA variants using phenotype + prior biological knowledge, i.e., the
  same integration pattern InterVar and the AnFiSA-style DSLs were
  building toward. **HIGH.**
- **EHR foundation-model distillation — new keyword hit.** Zhang, Chen,
  Liu, Wang, Li, Hong, Zhao et al. — *Distilling Foundation Models for
  Electronic Health Records* (2026 preprint). Distillation of EHR FMs
  into deployable smaller models — an obvious follow-on to the
  CLMBR/MOTOR/FEMR wave that has been dominating your EHR-FM thread.
  **HIGH.** *("Foundation models + electronic health records" keyword
  alert, 07-09.)*

---

## HIGH — detailed reports

### 1. MIXPRS: multi-population, multi-method PRS from summary statistics
- **Authors:** L. Xu, Y. Dong, X. Zeng, Z. Bian, G. Zhou, L. Guan, H. Zhao
- **Venue:** *Nature Genetics*, 2026
- **Source:** Jian Yang related-research alert, 2026-07-06
- **Link:** https://www.nature.com/articles/s41588-026-02637-4
- **Threads:** Genetic epidemiology → PRS / cross-ancestry portability;
  ML for precision health (individualized risk).
- **What it is (from the abstract):** A framework that integrates
  multiple PRS methods across multiple ancestry populations using only
  GWAS summary statistics — no individual-level tuning cohort required.
  Motivating problem: no single trans-ancestry PRS method (PRS-CSx,
  PROSPER, BridgePRS, etc.) is uniformly best; ensembles win on average
  but usually need an individual-level tuning set for weight learning.
  MIXPRS learns the weights from summary stats.
- **Why it matters for your work:** Two direct hooks.
  1. Your PheWAS/phecode + PRS work needs *portable* PRS as its
     ancestry-aware layer; MIXPRS is a plug-in improvement over the
     PRS-CSx-only baseline that most VUMC-style PheWAS+PRS analyses
     currently deploy.
  2. In BioVU / AoU / MVP where an individual-level tuning set is
     political-cost-per-use (each pull triggers a review), summary-only
     ensembles let you build the PRS on public GWAS + AoU or BioVU held-
     out validation only, without an intermediate individual-level tuning
     step.
- **Follow-up actions:**
  1. Skim the "no individual-level tuning" claim — how sensitive is
     performance to the summary-stat LD reference used?
  2. Compare stated benchmarks against the Chen-Bastarache-Bass-Wu-Lin
     nephrolithiasis paper (from the previous window) — does MIXPRS
     over-perform PRS-CSx in the same East-Asian slice?
  3. Check code availability — Nature Genetics tools are typically
     GitHub-released; verify it runs on AoU-style workspace.

### 2. Within-sibling attenuation of PRS accuracy: PCA vs LDSC vs LMM
- **Authors:** C.M. Kelly, O. Onuorah, E. Gilbert
- **Venue:** *Human Genetics*, 2026
- **Source:** J. Denny + G. Hripcsak + L. Bastarache related-research
  alerts (triple-feed saturation), 2026-07-08
- **Link:** https://link.springer.com/article/10.1007/s00439-026-02852-3
- **Threads:** Genetic epidemiology (PRS methodology, confounding
  control); PheWAS / phecode infrastructure (calibration).
- **What it is:** Uses UK Biobank sibling pairs to quantify how much of
  the *apparent* PRS accuracy in unrelated-individual samples is
  contributed by residual population stratification not stripped by
  standard corrections (PCA on genotype PCs, LD score regression
  intercept adjustment, linear mixed models). The within-sibling design
  makes population structure a within-family constant, so any residual
  accuracy attenuation between the two designs quantifies how much of
  the between-family PRS signal is stratification, not direct genetic
  effect.
- **Why it matters:** Three angles into your active work.
  1. PheWAS with PRS as exposure inherits any residual-stratification
     bias in the PRS itself. If PCA-adjustment leaves substantial
     confounding (as within-sibling tests often reveal), your PheWAS
     effect sizes with PRS are inflated — most in traits where
     ascertainment or geography correlate strongly with the phenotype
     (education, height, some psychiatric traits).
  2. LDSC-intercept and LMM adjustments both make specific
     assumptions about polygenicity + population structure. If Kelly et
     al. show LMM under-corrects in specific ancestry subsets, that
     affects the calibration story for MVP-style multi-ancestry PheWAS.
  3. The sibling design as a *validation harness* is generalizable —
     could be applied to CFTR-modulator target-trial emulation cohorts
     where family relatedness is documented (CFF registry).
- **Follow-up actions:**
  1. Read Fig 1 / Table 1 (accuracy attenuation ratios by trait).
  2. Cross-reference with the Souaiaia et al. *Nature* PRS-tails paper
     flagged in the 06-20 report — Souaiaia argues that the tails
     have different genetic architecture; Kelly argues even the middle
     is stratification-contaminated. Together these change how a
     top-5% clinical-cutoff PRS should be interpreted.

### 3. VUMC EHR-based growth curves for genetic disorders
- **Authors:** C. Shyr, R.J. Tinker, R.F. Brown, A. Wright, J.F. Peterson, et al.
- **Venue:** *npj Genomic Medicine*, 2026
- **Source:** Chenjie Zeng related-research alert, 2026-07-08
- **Threads:** EHR phenotyping & OMOP; Rare disease.
- **What it is:** A generalizable EHR-based framework for building
  condition-specific growth centile charts from routinely captured
  heights/weights, aimed at genetic disorders where the general-
  population CDC/WHO curve is uninformative or misleading (e.g., Prader-
  Willi, Williams, achondroplasia, mucopolysaccharidoses). Uses BioVU-
  style longitudinal EHR growth data.
- **Why it matters:** Sits exactly at the intersection you care about:
  EHR phenotyping tooling that becomes usable for rare disease
  benchmarking. This is a Wright / Peterson (VUMC) group paper, and
  the design pattern — "large EHR → rare disease reference curves via
  a mixed-effects framework" — is transferable to any longitudinal
  biomarker where the general-population reference doesn't apply
  (e.g., NT-proBNP in cardiomyopathy carriers, spirometry in CF,
  glycated-hemoglobin in monogenic diabetes).
- **Follow-up actions:**
  1. Check whether the framework is released as an R/Python package
     that can be repointed at BioVU / AoU EHR growth data.
  2. Reach out to the VUMC group about co-benchmarking against your
     penetrance-estimation work (both are "condition-conditional EHR
     reference" problems).

### 4. Cystic Fibrosis — MATRIARCH_CF pregnancy cohort on CFTR modulators
- **Authors:** A. Downes, I. Bokobza, L. Weitnauer, R. Scott, R. Dobra, et al.
- **Venue:** *BMJ Open Respiratory Research*, 2026
- **Source:** Chenjie Zeng related-research alert, 2026-07-08
- **Threads:** CF/CFTR modulator pharmacoepi; Causal inference &
  pharmacoepi (real-world evidence for excluded subgroups).
- **What it is:** Study protocol / early results for a prospective
  observational cohort of pregnant and breastfeeding females with CF
  on CFTR modulators. This population was excluded from the modulator
  registration RCTs; MATRIARCH_CF is the primary route to real-world
  safety and efficacy data for pregnancy on Trikafta/ivacaftor/
  lumacaftor.
- **Why it matters:** Direct hit on the CF/CFTR modulator thread of
  interest, specifically the *psychosocial and reproductive-health*
  angle that is under-served by the CFF registry data. Also a template
  for how to build a target-trial-emulation-adjacent design in a
  population where an RCT is ethically hard.
- **Follow-up actions:** Confirm which sites are contributing; check
  overlap with the U.S. CFF pregnancy sub-registry.

### 5. Impact of ETI (Elexacaftor/Tezacaftor/Ivacaftor) on inflammation in CF
- **Authors:** F. AlMunefi, J.P. Dyce, J.Y. Zhao, B.S. Quon
- **Venue:** *Annals of the American Thoracic Society*, 2026
- **Source:** Chenjie Zeng related-research alert, 2026-07-08
- **Threads:** CF/CFTR modulator real-world outcomes.
- **What it is:** Systematic review synthesizing the effect of triple-
  combination modulator therapy on airway and systemic inflammatory
  biomarkers. Relevant because most modulator outcome studies to date
  have focused on ppFEV1, sweat chloride, and exacerbation rate — the
  inflammation biomarker layer is the mechanistic middle ground for
  understanding why some modulator responses lag lung-function
  improvement.
- **Why it matters:** If you're building a phecode-based longitudinal
  outcomes analysis of ETI in BioVU/AoU CF cohorts, systemic-
  inflammation biomarkers (CRP, WBC, ESR) are the highest-value adjunct
  outcome and this review scopes what's already established.
- **Follow-up actions:** Note the studies included that used
  peripheral-blood transcriptomics — those are the cleanest
  mechanistic anchors.

### 6. Target-Trial Emulation — SABR vs surgery for early-stage NSCLC (methods)
- **Authors:** E. Kagenaar, D.G. Lugo-Palacios, A. Aggarwal, et al.
- **Venue:** *Journal of Clinical Oncology*, 2026
- **Source:** Christopher G. Chute related-research alert, 2026-07-08
- **Threads:** Causal inference & pharmacoepi (target-trial emulation).
- **What it is:** Emulated target trial comparing stereotactic ablative
  radiotherapy against surgical resection for operable early-stage
  non-small cell lung cancer. The comparison has been trialed several
  times and has repeatedly under-enrolled (patients don't randomize to
  "cut me open" vs "don't"), so a well-designed emulation is the
  practical evidence base.
- **Why it matters:** Reference implementation of target-trial
  emulation on a *treatment-choice* question with strong selection
  (operable-but-declined-surgery patients differ systematically from
  operable-consented patients). Methods worth cribbing for any target-
  trial design in your pharmacoepi work — particularly the eligibility
  windowing and grace-period handling around treatment initiation.
- **Follow-up actions:** Extract the Supplementary Methods (grace
  period, clone-censor-weight application, positivity diagnostics).

### 7. RankVar — ML variant ranking for rare disease diagnosis
- **Authors:** Y. Zhang, M.U. Ahsan, P. Wang, X. Lin, I.M. Campbell, et al.
- **Venue:** *Genome Medicine*, 2026
- **Source:** Wendy Chung own-articles alert, 2026-07-08
- **Threads:** Variant interpretation (ACMG/ClinGen); Rare disease
  (deep phenotyping / HPO).
- **What it is:** ML-based re-ranking of candidate variants for rare-
  disease diagnosis, combining prior biological knowledge with
  phenotype (HPO term) input to prioritize candidate causal variants
  from whole-genome/exome sequencing. Explicitly framed as
  "reinterpretation" — designed to be re-run as new evidence
  accumulates (a ClinGen-VCEP-adjacent use case).
- **Why it matters:** Central to your Variant interpretation thread.
  RankVar is competing with Exomiser, LIRICAL, AMELIE — worth knowing
  the benchmark-set differences and whether it beats them on the
  hardest cases (VUS reclassification).
- **Follow-up actions:** Confirm on GitHub whether the model is a
  gradient-boosted ranker or a transformer, and what phenotype
  encoding (HPO IDs vs HPO embeddings) it uses.

### 8. Distilling Foundation Models for EHR
- **Authors:** W. Zhang, Y. Chen, H. Liu, J. Wang, X. Li, X. Hong, M. Zhao, et al.
- **Venue:** 2026 preprint (venue not yet confirmed; ResearchGate PDF)
- **Source:** "Foundation models + electronic health records" keyword
  alert, 2026-07-09
- **Threads:** EHR foundation models (CLMBR / MOTOR / EHRSHOT / MedTok
  / FEMR / MEDS lineage).
- **What it is:** Knowledge distillation from a large EHR FM into a
  smaller, deployment-friendly model. The abstract snippet emphasizes
  the general-purpose learner framing that CLMBR-style FMs use.
- **Why it matters:** Deployment cost has been the recurring blocker
  for EHR FMs in production — a distilled MOTOR-scale model that
  matches on a shortlist of clinically valuable tasks (30-day readmit,
  1-year phecode incidence, etc.) is the practical form factor. Also
  interesting for **fairness and calibration audits**: a distilled
  model often loses calibration in tail subpopulations, and how much
  it loses is an under-studied axis for FM-EHR fairness.
- **Follow-up actions:** Full-text read to see (a) which FM they
  distill from (CLMBR/MOTOR/FEMR/a proprietary), (b) which target
  tasks, and (c) whether they measure per-subgroup calibration
  post-distillation.

### 9. UK Biobank multimorbidity — risk-enriched health trajectories (arxiv-digest)
- **Authors:** N. Fontana, A. Mapelli, E. Di Angelantonio, F. Ieva
- **Source:** local `arxiv-digest` 2026-07-07 — arXiv 2607.04702
- **Threads:** Chronic disease clustering / multimorbidity; EHR-linked
  biobanks.
- **What it is:** Constructs comorbidity networks from UK Biobank
  cardiometabolic data (24 diseases, 76 risk factors) using sparse
  Gaussian graphical models with Lasso regularization, informed by a
  confounder-evaluation prior. Recovers four disease communities that
  match established cardiometabolic taxonomy; then does community-
  based patient representations for progression phenotyping — four
  phenotypes with distinct long-term survival curves.
- **Why it matters:** This is the paper on your multimorbidity thread
  for the window. Two things to note: (a) explicit prior on
  confounding (shared risk factors) baked into the network estimation
  step, and (b) two-stage design that separates network inference from
  progression phenotyping.
- **Follow-up actions:** Compare against LDA-on-diagnosis-sequences
  work — does the GGM-based community align with LDA topics?

### 10. Prior-informed conditional GGMs on UK Biobank cardiometabolic proteomics (arxiv-digest)
- **Authors:** A. Mapelli, M.C. Massi, G. Cuccuru, E. Di Angelantonio, F. Ieva
- **Source:** local `arxiv-digest` 2026-07-01 — arXiv 2606.31805
  (n = 49,129 UKB, p = 366 proteins)
- **Threads:** EHR-linked biobanks; Genetic epi (protein biomarkers);
  ML for precision health.
- **What it is:** Same Milan group as #9. Integrates database-derived
  interaction priors (STRING-like curated PPIs) with covariate-
  dependent network modeling on UK Biobank proteomics. Applied to T2D:
  recovers T2D-associated perturbations, identifies 34 network-central
  candidate biomarkers — several detectable only through connectivity,
  not differential expression — and 6 biologically coherent protein
  communities. Code released.
- **Why it matters:** Biomarker discovery via *network centrality*
  rather than differential expression — a good complement to
  differential-abundance style pQTL work. The prior-weighting mechanism
  is worth studying: it lets curated-database evidence guide the
  population-level scaffold while leaving disease-specific edges
  data-driven.
- **Follow-up actions:** Check the GitHub repo
  (github.com/AlessiaMapelli/Prior-informed-conditional-GGMs) —
  compatible with AoU/BioVU proteomics workspaces?

---

## METHODS-WATCH — cite only

- **Naimi, Jin, Yu, Parisi, Bodnar** — *Residual-on-Residual Regression
  as a Tool for Effect Estimation in Observational Data*, stat.ME preprint
  2606.30976 (arxiv-digest 07-01). Under weak positivity violations,
  residual-on-residual regression outperforms AIPW and TMLE when the
  effect is approximately constant (partially linear model). Worth
  keeping as a triangulation tool alongside your AIPW/TMLE pipeline.
- **Asiedu & Watson** — *Causal ASCEND*, stat.ML preprint 2607.04527
  (arxiv-digest 07-07). Two-tiered causal discovery on genome-scale
  omics with polynomial-time scaling — relevant to any SNP-to-transcript
  causal work you do at biobank scale.
- **Krueger, Fischer, Rizwan, Kumar et al.** — *Multi-ancestry
  modeling improves fine-mapping resolution, protein prediction, and
  discovery for proteome-wide association studies*, medRxiv 07-06.
  Multi-ancestry pQTL fine-mapping — the natural pair to the MIXPRS
  paper on the trait side.
- **Mas Montserrat, Barrabes, Bustamante et al.** — *Non-Parametric
  Ancestry Adjustment for Polygenic Scores*, medRxiv 07-06. Non-
  parametric mean-shift correction to make PRS scale-comparable across
  ancestries — a lighter-weight alternative to full multi-ancestry
  training.
- **Chen, Li, Mazumder, Zhang, Lin** — *STELLAR: ensemble learning
  integrating rare variants to enhance PRS*, medRxiv 07-06 (surfaced
  in both Jian Yang and Joshua Denny feeds). PRS + rare-variant burden
  ensemble — same "composite risk models stacking PRS with rare
  pathogenic variants" thread you already track.
- **Kalra, Grilli, Coombes, Armasu, Upjohn et al.** — *Association of
  a Polygenic Risk Score with Diagnosis and Outcomes in Idiopathic
  Pulmonary Fibrosis*, *AJRCCM* 2026 (Denny feed 07-08). Clinically-
  scored PRS in IPF; another instance of PRS-for-a-rare-lung-disease
  that pairs with the CF thread indirectly.
- **Xiang, Liu, Feng et al.** — GLP-1 RAs vs DPP-4is after liver
  resection for hepatocellular carcinoma in T2D patients (Hernán
  citations 07-08). GLP-1 pharmacoepi in a niche indication — worth a
  glance for confounding-by-indication handling.
- **Said, Segre, Wiggs, Aboobakar** — *Large deletion spanning two
  conserved PITX2 enhancer elements is associated with primary open-
  angle glaucoma risk in the All of Us Research Program*, IOVS 2026
  (Denny feed 07-08). Structural-variant discovery on AoU. Interesting
  as a template for enhancer-level SV association at biobank scale.
- **Jampani, McClay, Rana, Mandhadi et al.** — *HABITAT*, medRxiv 07-08
  (Pascal Brandt feed). Cloud-based research data ecosystem at an
  academic medical center — infrastructure adjacent to OMOP, worth
  glancing for BioVU/AoU workflow ideas.
- **Golnari, Prantzalos, Upadhyaya, Buchhalter et al.** — *Developing
  a Specialized Dravet Syndrome Ontology*, medRxiv 07-08 (Callahan
  feed). Rare-disease HPO-adjacent ontology work.
- **Bang, An, Sung, Yun, Kim, Lee** — *PREDIKTOR*, arxiv-digest 07-07.
  Precision-oncology patient-specific KG + gene-perturbation model —
  drug-repurposing-adjacent, worth noting for the KG-hypothesis-
  output angle even though it's chemistry-forward.

---

## SKIP — noted for completeness

- Video-features causal inference (Nakamura et al., arxiv-digest 07-08)
  — off-thread.
- Airbnb / marketplace causal inference papers (Wu, Schmierer et al.,
  arxiv-digest 07-01 and 07-02) — off-thread despite causal-inference
  keyword hit.
- 3D plant phenotyping foundation-model paper (Jia et al., arxiv-digest
  07-03) — off-thread.
- AoU × spinal-cord-injury food-insecurity cross-sectional
  (Li & Yarar-Fisher, 07-07 AoU keyword feed) — off-thread.
- AoU × chimeric-RNA case study (Wang, Elfman, Li, 07-09 AoU keyword
  feed) — off-thread.
- HWE-conditional GWAS test (Böhringer & Holzmann, arxiv-digest 06-30)
  — general-methods, not on active threads.
- DNA Language Models pre-training assessment (Karpinsky et al.,
  arxiv-digest 06-30) — off-thread.
- Multiple hereditary-cancer RNA-analysis and prostate-cancer papers
  (Chenjie Zeng feed 07-08) — off-thread.

---

## Notes for next window

- The `arxiv-digest` pipeline recovered fully after the 06-20 fetch
  failure — 10/10 days between 06-29 and 07-08 produced digests, with
  the expected ~3-days-dry rhythm for the narrow category set.
- The 07-04 through 07-06 dry run is not a pipeline problem — the
  Fourth-of-July arXiv submission slump plus the narrow category
  slate genuinely produces zero on-thread papers on some days.
- No GitHub-notification traffic for `arxiv-digest` this window — the
  daily commits fire but there are no PRs / issues / actions in flight.
