# Research digest report — 2026-09-15

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-15 12:40Z** (~14 days since the
last research-digest report, covering fourteen arxiv-digest cron runs
and roughly a dozen Google Scholar / medRxiv / bioRxiv alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-02.md` → `2026-09-12.md`) | 09-02 → 09-12 daily crons | 12 daily runs. Dry days (0 papers): 09-03, 09-05, 09-06, 09-08, 09-12 (weekend/thin submission days). 09-02: 1 paper (mudskipper motor program, off-topic). 09-04: 2 papers (Cortez-Rodriguez causal inference on natural-disaster×nonprofit outcomes; Yu et al. location-invariant extremal QTE via IPW). 09-07: 1 paper (Rajabli & Collins brain-age CNN as reusable Alzheimer's FM). 09-09: 2 papers (Snel & Schulz influence-function attribution of Cohen's d in UKB; Wu et al. FUSE-RT Sim2Real chromatography FM). 09-10: 1 paper (Lee et al. Kalman-filtered Horvitz–Thompson IPW prevalence). 09-11: 3 papers (Devarakonda scDEFT single-cell drug-effect prediction on 1.16M-cell IBD atlas; Hendrix et al. geospatial FMs beyond social risk indices; Semchin et al. connectome-constrained Parkinson's subtypes). |
| No `arxiv-digest` email hits from GitHub | — | As with the prior window, `from:noreply@github.com arxiv-digest` returned zero threads — the pipeline commits its output to this repo rather than emailing PR/cron notifications; the on-disk digests *are* the arxiv-digest feed. `seen.json` (last modified 09-15 12:36Z) confirms the 09-15 cron ran but produced no new emailable output because scoring/dedup left nothing new. |
| Google Scholar alerts (09-14 morning batch, 08:24Z) | 09-14 08:24Z | 12 author-feeds fired: George Hripcsak (Ellershaw Foresight-England national-scale EHR FM; Momenzadeh causal-ML ICU discharge; Kitsos/STRIDE LM-assisted sepsis labels; Xiong KOMAP-Online JASA multimodal phenotyping; Lyu rubric-guided LLM OUD phenotyping; Dymshyts OHDSI PL LLM evaluation; Srinivasan diabetes-type AYA algorithm; Trujeque JMIR nonprescribed-fentanyl NLP), Isaac Kohane (Xiong et al. KOMAP-Online JASA), Konrad Karczewski (Zheng et al. medRxiv absorption/coexpression modules for PGS + proteomic RS in neurodegeneration; Heilbron dissertation on causal-gene identification in GWAS loci), Claudia Langenberg (Carrasco-Zanini et al. *Sci Transl Med* proteomics for undiagnosed rare disease after WGS), Peter Visscher (Wang et al. *Nature* 2026 within-family effect of ancestry on complex traits in a Mexican population), Wendy Chung (Ottman et al. APOE-disclosure RCT in NYC Latinos), Zhiyong Lu (attention-control LM, off-topic), Tiffany J Callahan (updated COVID-19 vaccines + autoimmune-rheumatic outcomes cohort), Marinka Zitnik (protein-ligand GNN, off-topic), Peter Szolovits (medical VLM counterfactual preference optimization, off-topic), Patrick Ryan (Bouwman EU orphan-medicine RWE 2000-2025), Joshua Denny (Fetchko sex differences in oral diseases EHR — off-topic). |
| Google Scholar alerts (09-14 afternoon batch, 14:22Z, keyword feeds) | 09-14 14:22Z | 11 keyword-feeds fired: `Foundation models + "electronic health records"` (Liang et al. *BMJ* CVD risk prediction across HIC/LMIC diabetes; Kim & Gha-hyun *J Psychosomatic Res* subtype-directional depression↔GI EHR cohort; Schulte-Althoff et al. *npj Health Systems* explainable SHAP-space fall risk profiling; Seker et al. *Int J* mood-instability NLP transdiagnostic cannabis predictor in 13,025 adolescents; Islam et al. *JMIR Formative* HSV-1↔dementia high-dim PS analysis), `"electronic health records"`, `"UK Biobank"` (Zhang et al. *BMC MIF* interpretable MCI classifier in CAD+HTN externally validated; Shi et al. *Respir Res* proteomic signatures preceding bronchiectasis; Wu et al. *Front Public Health* multidimensional health-vulnerability transitions and CVD; Yan et al. ANGPTL3 mortality; Chen et al. residential green/blue-space × genetic-susceptibility COPD), `APOL1` (Swiatecka-Urban et al. *Transplantation* two-genome donor+recipient PRS for allograft longevity, explicitly citing CKD-PRS × APOL1 additivity), `"knowledge graph"` (mostly off-topic; Liang MMKGR survey and Qu et al. *JMIR MI* temporal-KG-RL for chronic gastritis diagnosis+treatment prediction are the on-topic ones), `"variant interpretation" OR "variant classification"` (Xu et al. *Int J Neuroscience* MR-prioritized CD40 in MG), `"drug repurposing"` (Agranat & D'Acquarica *Future Med Chem* editorial), `"All of Us research program"` (Diaby et al. AoU poly-tobacco disparities), `mendelian diseases` (Liang et al. *PLOS Med* protein-mediated drug-target MR for CKD in T2D), `rare diseases` (mostly off-topic; EU health-law review; Roschyk lncRNA-ASD). |
| medRxiv Subject Collection Alert (09-15 00:05Z) | 09-15 00:05Z | Genetic and Genomic Medicine, Epidemiology, Health Informatics, Allergy/Immunology digests — subject-collection stream (title metadata only). |
| bioRxiv Subject Collection Alert (09-15 00:01Z) | 09-15 00:01Z | Bioinformatics, Genetics, Genomics, Immunology, Pathology digests. |
| arXiv daily Subj-class mailing (09-15 05:00–05:03Z) | 09-15 05:00Z | Full q-bio + stat daily arXiv mailings; supersets of what `arxiv-digest` will surface on the 09-15 run. |
| PubMed `My NCBI` (09-14 14:03Z) | 09-14 14:03Z | Two feeds fired: `drug repurposing` and `UK Biobank`. Titles overlap with the Scholar keyword feeds; nothing new that isn't already listed above. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Thirteen HIGH items and four METHODS-WATCH items surfaced this window,
clustering into seven knots:

**EHR foundation-model / phenotyping cluster (5 items).**
Ellershaw et al. arXiv 2608.16273 (**Foresight-England**), the first
national-scale generative EHR-FM, resurfaced via Hripcsak's citations-to
feed after landing initially in the prior window; the same 09-14 Hripcsak
batch dropped **Xiong et al.** *JASA* 2026 — the KOMAP-family
knowledge-driven online multimodal automated phenotyping system that
directly serves your `EHR phenotyping & OMOP` and
`Knowledge representation in EHRs` threads. **Lyu et al.** arXiv
2609.05682 — a rubric-guided LLM for opioid-use-disorder computable
phenotyping — is the on-brand *auditable* LLM-phenotyping paper.
**Dymshyts et al.** OHDSI 2025 poster — LLM evaluation of the OHDSI
Phenotype Library concept sets — is the OHDSI-native counterpart. And
**Kitsos et al.** medRxiv 2026 STRIDE — LM-assisted label refinement
for sepsis detection across seven sites — reads directly on your
`NLP-derived representations from clinical notes` sub-thread and the
Wu-et-al. ACT auditable-CT-phenotyping pattern from the prior window.

**Causal inference / pharmacoepi cluster (3 items).**
**Momenzadeh et al.** *Sci Rep* 2026 — a causal-ML framework for ICU
discharge decision support from EHRs — is a direct-hit for your
`Causal inference and pharmacoepi` thread with an explicit HTE + decision
framing. **Liang et al.** *PLOS Medicine* 2026 (Mendelian-diseases feed)
— protein-mediated drug-target MR for CKD in T2D — is a canonical
example of the drug-target-MR-triangulated-with-observational sub-thread
you explicitly prioritized (Saxby metformin×AAA lineage). **Yu et al.**
arXiv 2609.04018 — a location-invariant extremal QTE estimator under
IPW — is a methods anchor for extreme-quantile TTE where population
QTEs are otherwise not translation-invariant.

**Biobanks + genetic epi cluster (3 items).**
**Wang et al.** *Nature* 2026 (Peter Visscher feed) — within-family
effects of genetic ancestry on complex traits in a Mexican population —
is a textbook direct-hit for `Genetic epidemiology` and for the
cross-ancestry-portability sub-thread; within-family designs get past the
population-stratification confounding that PGS-portability audits keep
tripping on. **Swiatecka-Urban et al.** *Transplantation* 2026 (APOL1
keyword feed) — **two-genome donor+recipient PRS** for kidney-allograft
longevity, explicitly stratifying on APOL1 high-risk status — is a
direct hit for the APOL1 disease thread. **Snel & Schulz** arXiv
2609.07729 — influence-function attribution of case-control effect
size (Cohen's d) to individual training samples in UK Biobank — is
the biobank-native methods paper.

**Rare-disease diagnostics (2 items).**
**Carrasco-Zanini et al.** *Science Translational Medicine* 2026
(Langenberg + Karczewski feeds) — plasma proteomics for undiagnosed
rare-disease patients after genome sequencing (n=424) — is the
proteomics-augments-WGS-diagnostics paper the rare-disease thread has
been waiting for; pairs directly with the Ran/Benatar 2026 ALS carrier
phenoconversion template you already track. **Zheng et al.** medRxiv
2026 (Karczewski feed) — absorption/coexpression modules that show
where polygenic and proteomic risk scores **diverge** in
neurodegenerative disease — is the complementary PGS-vs-proteomic-RS
audit that pairs with the "PGS residuals / polygenic-deviation"
sub-thread and with Ottman et al.'s Latino APOE-disclosure RCT (Wendy
Chung feed).

**Knowledge representation / KG-in-EHR (1 item).**
**Qu et al.** *JMIR Medical Informatics* 2026 — reinforcement-learning
temporal knowledge-graph reasoning (CG-TKG) for chronic-gastritis
diagnosis-and-treatment prediction — is the on-topic KG paper from the
otherwise heavily off-topic 09-14 `"knowledge graph"` feed.

**RWE / pharmacoepi in orphan drugs (1 item).**
**Bouwman et al.** *Ther Innov Regul Sci* 2026 (Patrick Ryan feed) —
contribution of real-world evidence to orphan-medicine approvals in the
EU, 2000-2025 — is on-brand for `Rare disease` × `Causal inference and
pharmacoepi` and complements your `Drug repurposing` thread's
clinical-evidence-loop requirement.

**IBD / patient-stratification with counterfactual reasoning (1 item).**
**Devarakonda** arXiv 2609.10831 (**scDEFT**) — a drug-effect single-cell
transducer applied to a 1.16M-cell inflammatory-bowel-disease atlas
with pre-treatment responder stratification (AUROC 0.70 vs. chance
baseline) — is the exact intersection of your `IBD` disease thread with
the `Chronic disease clustering and multimorbidity` and
`ML for precision health` threads.

---

## Detailed reports by thread

### 1. EHR foundation models × Knowledge representation × Phenotyping (5 items)

#### 1a. Ellershaw et al. arXiv 2608.16273 — **Foresight-England: national-scale generative EHR-FM (Hripcsak citations-to feed, 09-14 08:24Z)**
> Authors: S. Ellershaw, C. Tomlinson, Z. Kraljevic, S. Denaxas, et al.

Foresight-England (Foresight-E) is described as the *first
national-scale generative foundation model of EHRs*, developed as a
research pilot strictly for COVID-19 research. The paper evaluates
Foresight-E's ability to model **direct and indirect effects** of the
pandemic on medical event trajectories.

**Why it matters for you.**
- Direct hit for `EHR foundation models` → *Digital twins from EHR
  data* sub-thread. National-scale + generative + COVID-scoped is
  exactly the template the Zhang / Ideker / Oermann *Cell* 2026
  digital-twin consortium paper primes.
- Sits in the same territory as the Foresight lineage (Kraljevic
  et al.) that you've already flagged; this is the England-wide scale-up.
- Interlocks with your `Interoperability standards and their
  representational consequences` sub-thread — England's national
  primary+secondary care linkage (via NHS Digital) is a natural probe
  for what phenotypes are *computable at national scale*.
- Triage: **HIGH**. Read after the *Cell* consortium paper and before
  the Lemieux *JAMIA Open* framing paper you already track — this is
  the national-scale exemplar for both.

#### 1b. Xiong, Sweet, Hong, Bonzel, Panickan et al. *JASA* 2026 — Bending the Learning Curve for EHR Research via Knowledge-Driven Online Multimodal Automated Phenotyping System (KOMAP-family) (Kohane new-articles + Hripcsak citations-to)
> Authors: X. Xiong, S. M. Sweet, C. Hong, C. L. Bonzel, V. A. Panickan et al. — *Journal of the American Statistical Association*, 2026.

Snippet: "EHRs hold great promise for translational research but remain
difficult to use at scale because diagnostic codes are noisy,
disease-relevant features are hard to identify, high-quality labels are
limited and patient-level data … [is scarce]." The paper appears to
extend the KOMAP-online line — an online, multimodal, knowledge-driven
automated phenotyping system that uses embedded knowledge (concept
embeddings + KG signals) as a discovery lever rather than requiring
labeled training data at every site.

**Why it matters for you.**
- Direct hit for `EHR phenotyping & OMOP` and for the
  `Concept normalization and vocabulary mappings` sub-thread of
  `Knowledge representation in EHRs`.
- KOMAP is on your existing lineage list (grouped with cui2vec /
  Med-BERT / SapBERT / MedTok). Getting into *JASA* is the
  statistical-legitimacy stamp for the "knowledge-driven, label-scarce"
  claim — worth reading for the identifiability/consistency guarantees
  their statistical framing gives (Weijing Tang / Tianxi Cai / Peter
  Kramlinger co-author neighborhood makes this reasonable).
- Portable to your `Fidelity, portability, and audit of representations`
  sub-thread: online updating claims are exactly the kind of
  representation-drift-across-sites question the Xiong et al. framework
  should be able to formalize.
- Triage: **HIGH**. Read alongside CohortContrast (Ilves et al., prior
  window) and PheValuator; expect Xiong et al. to give the theoretical
  side of what CohortContrast gave empirically.

#### 1c. Lyu, Pardo, Peng, Chen, Zhang, Lu et al. arXiv 2609.05682 — A Rubric-Guided Large Language Model Solution for Opioid Use Disorder Computable Phenotyping (Hripcsak citations-to feed)
> Authors: M. Lyu, P. Pardo, C. Peng, Z. Chen, M. Zhang, J. L. Lu et al. — arXiv preprint, 2026.

Snippet: "OUD remains a public health crisis in the US, yet it is
difficult to identify from EHRs because missing diagnosis codes and
supporting evidence are buried in clinical narratives. Accurate OUD
[phenotyping requires reading notes …]." The design is a **rubric-guided
LLM** — the LLM is constrained by a scored rubric rather than free-form
prompting — for computable phenotyping.

**Why it matters for you.**
- Direct hit for `EHR phenotyping & OMOP` → *LLM-assisted phenotyping*
  and for `NLP-derived representations from clinical notes` under
  `Knowledge representation in EHRs`.
- The "rubric-guided" formulation is on-brand with your emphasis on
  **auditable** LLM phenotyping — a rubric is a specification a chart
  reviewer can adjudicate against, unlike a free-form LLM verdict.
- Pairs naturally with your Wu et al. arXiv 2608.25948 auditable-CT
  phenotyping paper from the prior window (imaging FM audit) and with
  the Xue et al. medRxiv 2026 psychiatric-concept encoder-LM paper —
  the pattern of encoder-based + rubric-constrained systems regaining
  ground on decoder-based frontier LLMs when auditability is required.
- Trans-substrate corollary: OUD is a phenotype where structured coding
  massively under-captures cases (ICD codes trail actual encounters
  documented in notes) — the *positive-predictive-value under
  clinical-narrative augmentation* problem your INTERESTS.md flagged
  under NLP-derived representations.
- Triage: **HIGH**. Read after Xiong et al. above; expect Lyu to be the
  applied instantiation of the abstract KOMAP-family claim.

#### 1d. Dymshyts, Swerdel, Shoaibi (OHDSI 2025 symposium poster) — Evaluating the OHDSI Phenotype Library concept sets using Large Language Models
> Authors: D. Dymshyts, J. Swerdel, A. Shoaibi.

Snippet: "The OHDSI community has developed a publicly accessible,
version-controlled Phenotype Library (OHDSI PL) to guide real-world
evidence towards the FAIR principles …" The paper evaluates whether
LLMs can be used to *audit* the concept sets that back OHDSI phenotype
definitions.

**Why it matters for you.**
- Direct hit for `EHR phenotyping & OMOP` and for the
  `Concept normalization and vocabulary mappings` +
  `Fidelity, portability, and audit of representations` sub-threads.
- OHDSI PL is the FAIR-compliant, version-controlled reference set for
  network studies; running an LLM audit on it — rather than asking an
  LLM to *build* phenotypes — is the inverted, safer direction. The
  question "does this concept set match its stated definition?" is
  auditable in a way "define this phenotype" is not.
- Pairs with your Ilves et al. CohortContrast paper from prior window
  and with the Xiong et al. JASA paper above — together, three
  complementary vectors on OMOP concept-set fidelity.
- Triage: **HIGH** for your `Knowledge representation in EHRs` thread.
  Poster-only means low methodological depth, but the direction is
  right and the OHDSI community will build on it.

#### 1e. Kitsos Kalyvianakis, Pérez de Amézaga, Lee et al. medRxiv 2026 — STRIDE: Language model-assisted label refinement for accurate sepsis detection from EHRs
> Authors: I. Kitsos Kalyvianakis, C. Pérez de Amézaga, E. S. Lee et al. — medRxiv 2026.09.08.

Snippet: "Sepsis is a leading cause of hospital mortality, yet timely
recognition is hampered by nonspecific presentations and label noise in
code-based case definitions. We developed STRIDE, a machine-learning
framework for sepsis detection across seven [sites]." STRIDE uses an
LLM to *refine* labels — cleaning up noisy code-based sepsis definitions
so downstream ML predictors are trained against a cleaner ground truth.

**Why it matters for you.**
- Direct hit for `EHR phenotyping & OMOP` and for the
  `NLP-derived representations from clinical notes` sub-thread.
- Sepsis is the canonical case where structured coding
  (Sepsis-3 / DKA / hypotension) chronically under-captures on one axis
  and over-captures on another. LM-assisted label refinement is the
  exact "note-code fusion" pattern your INTERESTS.md flagged.
- Seven-site design goes at the portability question head-on — how
  robust is the LLM-cleaned label across sites?
- Triage: **HIGH**. Read as a peer to Lyu et al. and to the Xue et al.
  psychiatric-concept paper from prior window.

---

### 2. Causal inference & pharmacoepi (3 items)

#### 2a. Momenzadeh, Ghaderzadeh, Oshaghi et al. *Sci Rep* 2026 — A causal machine learning framework for ICU discharge decision support using electronic health records (Hripcsak feed)
Snippet: "Discharging patients from the ICU requires balancing the
risks of premature transfer against the costs and capacity constraints
of prolonged ICU stay. While early discharge may increase the risk of
deterioration and readmission …"

**Why it matters for you.**
- Direct hit for `Causal inference and pharmacoepi` (though not a drug
  question — a discharge-timing question — the design is identical:
  action effect on an outcome under confounding) and for
  `ML for precision health` (HTE + decision).
- INTERESTS.md is explicit: ML papers are HIGH when they're tied to a
  clinical decision. ICU discharge is a decision every ICU makes every
  day, so this is on the "clinical decision" side rather than the
  "leaderboard benchmark" side.
- Read for the *estimand specification* — extubation + step-down is
  a compound decision; sloppy causal-ML pipelines conflate the two.
- Triage: **HIGH**. Watch for the propensity/g-computation specifics.

#### 2b. Liang, Zheng, Tan, Sasako, Ilboudo et al. *PLOS Medicine* 2026 — Protein mediators of chronic kidney disease in Type 2 diabetes: A Mendelian randomization study (mendelian-diseases keyword feed)
Snippet: "… this study infers protein mediators of chronic kidney
disease in Type 2 diabetes using MR."

**Why it matters for you.**
- Direct hit for `Genetic epidemiology` → phenome-wide MR / biomarker-
  as-exposure sub-thread, and for `Causal inference and pharmacoepi` →
  drug-target MR sub-thread you explicitly prioritized (Saxby et al.
  metformin×AAA lineage; MR-ALasso lineage).
- CKD-in-T2D is right at the confluence of your APOL1 (kidney), GLP-1/
  SGLT2 pharmacoepi, and metabolic-disease multi-thread interests.
  Protein mediators are the intermediate phenotypes drug-target MR
  needs to *identify tractable targets*.
- Portable to CFTR modulator ancillary-outcome work if the same MR
  scaffolding is applied to lung-function proteins.
- Triage: **HIGH**. Read for the MR instrument selection — the failure
  mode of proteomic MR is horizontal pleiotropy through the same
  pathway.

#### 2c. Yu, Huang, Liu, Tang, Wang, Zhang, Zhao arXiv 2609.04018 — A location-invariant estimator of extremal quantile treatment effects for heavy-tailed distributions (arxiv-digest 2026-09-04, propensity-score keyword hit)
Full abstract inline in the arxiv-digest. Contribution: adapts the
location-invariant Fraga EVI estimator to the causal setting using IPW,
then replaces the extrapolation formula with a difference-based scheme
so the location parameter cancels when quantile differences are taken.
Result: a QTE estimator invariant under a common location shift of the
potential outcome distributions.

**Why it matters for you.**
- Methods paper for `Causal inference and pharmacoepi`. Applications:
  extreme-quantile TTE where the tail is the object of interest —
  extreme hospitalization costs, extreme LOS, extreme drug-exposure
  windows, extreme lab values (creatinine spikes in APOL1 kidney work,
  extreme HbA1c on GLP-1 discontinuation).
- The prior estimators break under location shifts even though the
  population QTE doesn't — a subtle but real bug when you're subtracting
  quantiles across cohorts / calendar time.
- Triage: **METHODS-WATCH**, borderline HIGH. Not the estimator you
  reach for first (most TTE work lives well inside the data range),
  but the one you reach for when quantile shifts under exposure
  intersect with heavy-tailed outcomes.

---

### 3. Biobanks with EHR linkage + Genetic epi (3 items)

#### 3a. Wang, Berumen, Vergara-Lope, Baca et al. *Nature* 2026 — Within-family effect of ancestry on complex traits in a Mexican population (Peter Visscher new-articles feed)
Snippet: "Human populations differ in disease prevalence and phenotypes
[due to genetics, environment, and their interaction]. [Within-family
effects] …"

**Why it matters for you.**
- Direct hit for `Genetic epidemiology` → *Cross-trait shared genetic
  architecture and multi-trait triangulation* and *PGS × ancestry*
  sub-threads.
- Within-family designs remove population-stratification and shared-
  environment confounding — a much cleaner probe for "does ancestry
  affect this trait, or does the environment correlated with ancestry?"
  Landing this in Mexican mestizo populations, which have among the
  most well-characterized recent admixture, is the ideal proof-of-
  concept.
- Directly relevant to your APOL1 kidney thread — the "APOL1
  genotype-phenotype association vs. correlated environment" question
  is exactly what within-family designs adjudicate. The methodological
  template ports directly.
- Triage: **HIGH**. *Nature* venue + Visscher lab + within-family
  Mexican design makes this a template you'll cite.

#### 3b. Swiatecka-Urban, Mitash, Koeppel, Turner *Transplantation* 2026 — Two Genomes, one Outcome: Stratifying Donor and Recipient Polygenic Risk Score to Improve Kidney Allograft Longevity (APOL1 keyword feed)
Snippet: "Cross-ancestry work shows that a CKD-PRS combines
**additively** with APOL1 status. … Analogous interactions almost
certainly govern other outcomes: a donor APOL1 high-risk … kidney
disease burden, integration of APOL1 and other [PRS signals for
allograft longevity]."

**Why it matters for you.**
- Direct hit for the APOL1 disease thread (kidney transplant
  decision-making, ancestry considerations) AND for the
  `Composite risk models stacking PRS with rare pathogenic variants`
  sub-thread — APOL1 is the archetypal rare-pathogenic-variant×PRS
  layer, and the two-genome design (donor genome + recipient genome
  both contributing to allograft outcome) is a beautiful extension of
  composite risk into transplantation.
- CKD-PRS × APOL1 additivity is exactly the interaction structure your
  `PGS × exposure / environment` sub-thread wants documented.
- Directly informs transplant policy — the question "should donor APOL1
  status influence organ allocation" is live, and a two-genome PRS
  formalization is what a policy committee would rely on.
- Triage: **HIGH**. This is your APOL1 thread's landing zone this
  window.

#### 3c. Snel & Schulz arXiv 2609.07729 — Attributing Cohen's d: Training Data Attribution for Disease-Related Effects in Normative Age Biomarkers (arxiv-digest 2026-09-09; uk-biobank + biobank keyword hits, score 2)
Full abstract in the arxiv-digest. Contribution: **influence functional
for Cohen's d** — attributes case-control effect size (rather than
prediction loss) to individual training samples. Validated against
leave-one-out retraining. In UK Biobank across four diseases × two
biomarker modalities: removing the top 10% most-influential training
samples **more than doubles** the metabolomic-age effect for type-2
diabetes and raises the brain-age effect for MS by ~1/3. Random
removal is flat. Flagged subjects have subclinical cardiometabolic
burden that diagnosis-based exclusion misses — for T2D, the recovered
marker is HbA1c (blood sugar control). Ships `pyinfluence`.

**Why it matters for you.**
- Direct hit for `Biobanks with EHR linkage` + `ML for precision
  health` + `Genetic epidemiology` (normative-age model → deviation
  as disease risk → biomarker-as-exposure logic).
- The really interesting finding is that the influence-function ranking
  identifies **subclinical disease burden** that diagnosis-based
  exclusion misses. That's the deeper pattern your INTERESTS.md
  flagged: healthy-cohort definitions leak disease signal into
  "normal", and the resulting normative model under-detects disease
  deviation. The influence-functional makes this quantitative and
  correctable.
- `pyinfluence` is directly portable to any UKB / AoU / BioVU normative
  age model — brain age, metabolomic age, retinal age, cardiac age.
- Triage: **HIGH**. Read for the influence-functional derivation and
  the leave-one-out validation; the metabolomic-age × T2D + brain-age
  × MS ablations tell you where the method delivers most.

---

### 4. Rare disease diagnostics & PGS-vs-proteomic complementarity (2 items)

#### 4a. Carrasco-Zanini, Andrade, Pietzner et al. *Science Translational Medicine* 2026 — Proteomics identify disease-associated variants in patients with rare diseases undiagnosed after genome sequencing (Langenberg + Karczewski feeds)
Snippet: "Despite the introduction of genome sequencing (GS) for rare
disease diagnostics, a genetic cause is not identified in most
patients. Here, we explored the potential of proteomics to improve the
diagnostic yield in 424 patients with rare diseases …"

**Why it matters for you.**
- Direct hit for `Rare disease` → data-driven reanalysis of unsolved
  cases sub-thread (Uria-Regojo et al. medRxiv 2026 already in your
  INTERESTS.md). This paper is the *proteomic-augmented* reanalysis
  variant, complementary to the RNA / splicing / long-read reanalysis
  strands.
- Ties in with your Ran/Benatar 2026 ALS *Nature Medicine*
  pre-symptomatic-carrier-phenoconversion template: same UKB Olink /
  AoU proteomics infrastructure, but pointed at *diagnosed-negative*
  rather than *at-risk* patients.
- 424 patients is a mid-scale cohort — small enough to be a
  proof-of-concept, large enough that positive hits generalize.
- Directly ports to your BRCA / APOL1 / HTT / hereditary-cancer-
  syndromes carrier list — the same proteomic assay that resolves a
  VUS in an undiagnosed rare-disease patient can prioritize among VUS
  in a hereditary-cancer panel.
- Triage: **HIGH**. Read for the proteomic-signal → variant-prioritization
  scoring: does the pipeline give you *ranked* candidates, and how does
  it handle the pleiotropic-protein failure mode?

#### 4b. Zheng, Shivakumar, Shen, Kim medRxiv 2026 — Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases (Karczewski citations-to feed)
Snippet: "PGS and proteomic risk scores are both proposed for
pre-symptomatic stratification, yet the extent to which they provide
overlapping or complementary information has not been measured across
neurodegenerative disease. To quantify [this] we build absorption and
co-expression modules …"

**Why it matters for you.**
- Direct hit for the `Multi-omics-augmented PRS` sub-thread of
  `Genetic epidemiology` (Nightingale NMR / Olink proteomics stacked
  with PGS) — and specifically for the question your INTERESTS.md
  framed as the "PGS residuals / polygenic-deviation" family: where
  do proteomic RS *diverge* from PGS, and does that divergence carry
  actionable disease-risk signal?
- Neurodegeneration is the ideal test bed: APOE dominates the PGS but
  the proteomic layer (NfL, GFAP, pTau) captures near-symptom-onset
  biology that the PGS can't see. Absorption vs. co-expression module
  framing is the *right* representation choice for asking "does the
  proteomic RS add over the PGS or absorb it?"
- Pairs with the Snel & Schulz 2609.07729 metabolomic-age paper above —
  same "biomarker-derived deviation" logic, different attribution
  method.
- Triage: **HIGH**. Read before the Carrasco-Zanini paper above (same
  proteomic infrastructure, complementary question).

---

### 5. Knowledge graphs & ontologies for clinical reasoning (1 item)

#### 5a. Qu, Sun, Wang, Liu, Yao, Li, Song et al. *JMIR Medical Informatics* 2026 — Reinforcement Learning-Based Temporal Knowledge Graph Reasoning for Predicting Chronic Gastritis Diagnosis and Treatment (knowledge-graph keyword feed)
Snippet: "Temporal KGs extend the static KG framework by introducing
the temporal dimension. … We constructed a chronic gastritis temporal
knowledge graph (CG-TKG) based on real-world [EHR data]."

**Why it matters for you.**
- Direct hit for `Knowledge graphs & ontologies` and for the
  `Patient-level and cohort-level knowledge graphs from EHR`
  sub-thread of `Knowledge representation in EHRs`.
- Temporal KGs on EHR-derived patient timelines are exactly the
  representation your INTERESTS.md flagged for cohort discovery, drug
  safety, and treatment-response prediction. RL over a temporal KG is
  a specific instantiation of "graph reasoning for clinical
  decisions" — which chronic-gastritis paths (diet / H. pylori
  eradication / PPI escalation) lead to which outcomes?
- Chronic gastritis is off-topic disease-wise (not on your CF / APOL1
  / CHIP-VEXAS-LOY / IBD list) but the *method* is transferable to
  IBD directly.
- Triage: **METHODS-WATCH**. Read the RL formulation on the temporal
  KG; skim the gastritis-specific clinical claims.

---

### 6. RWE for orphan drugs (1 item)

#### 6a. Bouwman, Almeida, Jonker, Leufkens *Ther Innov Regul Sci* 2026 — Contribution of Real-World Evidence for the Orphan Medicines Approvals in the European Union Between 2000 and 2025 (Patrick Ryan citations-to feed)
Snippet: 25-year retrospective on RWE use in EU orphan-medicine
approvals.

**Why it matters for you.**
- Cross-cuts `Rare disease` × `Causal inference and pharmacoepi` ×
  `Drug repurposing`. The regulatory-acceptance question — *what kinds
  of RWE do EMA orphan approvals actually rely on?* — is the missing
  piece in most computational-repurposing pipelines that claim
  clinical translatability without engaging with the regulatory
  evidence gate.
- 25-year window catches the entire orphan-drug era from the 2000 EU
  orphan-medicine regulation forward — long enough to show trends
  (natural-history controls → external comparators → target-trial
  emulation).
- Directly informs your CFTR modulator (Trikafta / ivacaftor)
  pharmacoepi thread, where the modulators were approved on small
  trials with meaningful RWE input.
- Triage: **HIGH**. Read for the RWE-modality classification and how
  it evolves over the 25 years — useful ammunition for framing your
  own drug-repurposing / TTE work as regulator-legible.

---

### 7. IBD × single-cell drug-effect prediction (1 item)

#### 7a. Devarakonda arXiv 2609.10831 — **scDEFT**: single-cell Drug EFfect Transducer (arxiv-digest 2026-09-11; inflammatory-bowel-disease + patient-stratification keyword hits, score 2)
Full abstract inline in the arxiv-digest. Contribution: scDEFT treats a
drug as a **conditioning operator** on single-cell representations,
enabling *prediction* and *explanation*. Feature-wise linear modulation
produces drug-conditioned cell latents (learned per-cell then frozen);
two heads aggregate over shared transcriptional neighborhoods to
predict drug-induced state change and responder status; a backward
stage ranks latent dimensions by responder-separation strength and maps
them to genes under a cell-composition control. Applied to a
**harmonized IBD atlas of 1.16M cells** across three cohorts and two
drug classes: predicts state change at 45% of baseline-to-reproducibility-
ceiling headroom, stratifies responders before treatment at AUROC 0.70
where standard predictors remain at chance.

**Why it matters for you.**
- Direct hit for `Inflammatory bowel disease` (from your Specific
  disease threads) and for `ML for precision health` (patient
  stratification before treatment — a live clinical decision, not
  a leaderboard benchmark).
- Interlocks with `Chronic disease clustering and multimorbidity`
  (harmonized atlas across cohorts is exactly the multi-cohort
  clustering scaffolding). The counterfactual-prediction claim
  (predicting drug×cohort effects for unseen combinations) is the
  right way to phrase "personalized drug response" — as
  intervention, not just correlation.
- AUROC 0.70 for pre-treatment responder stratification is
  clinically meaningful for IBD, where biologics-non-response rates
  approach 30-40% and current biomarkers do very little.
- Triage: **HIGH**. Read the FiLM drug-conditioning construction and
  the responder-backward-attribution stage.

---

## METHODS-WATCH items

- **Rajabli & Collins** arXiv 2609.05400 — A generalizable feature
  extractor for Alzheimer's-related brain MRI tasks. Compact brain-age
  3D CNN adapted via LoRA (~1% extra params) to six downstream tasks;
  transfers ADNI→OASIS-3 without retraining. Relevant to the
  `Digital twins from EHR data` sub-thread as a *foundation-model-as-
  reusable-backbone* proof-of-concept — the pattern (small pretrained
  model + LoRA + task) will port to EHR-FM adapter work. Triage:
  METHODS-WATCH.

- **Wu et al.** arXiv 2609.07531 — FUSE-RT chromatography FM with
  Sim2Real transfer. Multitask foundation model + Sim2Real transfer
  learning across 179 chromatographic methods; simulation-data-scale
  power law. Off-topic disease-wise but the *Sim2Real + FM adapter +
  power-law scaling* pattern is directly portable to synthetic-EHR
  pretraining for EHR-FMs where real longitudinal EHR data is scarce.
  Triage: METHODS-WATCH.

- **Lee, Rempala, Schnell** arXiv 2609.09325 — Kalman filtering of
  Horvitz–Thompson IPW estimates for infectious-disease prevalence.
  Extends the standard random-walk state-space to a joint local-linear
  trend so precision borrows from past estimates; provides
  filter (real-time) and smoother (retrospective) options; handles
  missing-testing days. Directly portable to `Causal inference and
  pharmacoepi` for any calendar-time inverse-probability-weighted
  running-cohort estimator where daily estimates are noisy (e.g.,
  running SGLT2i-initiator TTEs by calendar week). Triage:
  METHODS-WATCH.

- **Semchin, d'Angremont, Ding, Antar, Lorenzi, Arfanakis, van der
  Werf, Thompson, Gutman** arXiv 2609.10890 — Connectome-constrained
  dynamic model for Parkinson's-disease subtypes with subject-specific
  disease time. Recovers four progression subtypes on PPMI, validated
  cross-sectionally, benchmarked against SuStaIn. Off-topic disease
  (PD not on your list) but the *disease-progression subtyping under
  connectome / graph constraint* framework is directly portable to
  IBD, autoimmune, and aging-multimorbidity trajectory clustering.
  Triage: METHODS-WATCH.

---

## SKIP-worthy items (surfaced but low signal)

Brief notes on items that surfaced but don't warrant deep reading:

- **Cortez-Rodriguez** arXiv 2609.04136 (natural disasters × nonprofit
  outcomes, causal inference keyword hit) — no evidence of causal
  effect; off-topic domain (nonprofit-sector economics) even though
  the causal-inference methods are well-executed. SKIP.
- **Mansouri Ghiasi** arXiv 2608.31004 (storage-centric systems for
  genomic analyses, precision-medicine keyword hit) — CS.AR
  systems-engineering dissertation; only "precision medicine" adjacent
  as motivation text. SKIP.
- **Ramesh, Sadalgekar, Tan, Li** arXiv 2609.00564 (mudskippers +
  motor keyword hit) — biomechanics; incidental keyword collision.
  SKIP.
- **Hendrix, Zhang, Heitzig, Bazemore, Rehkopf** arXiv 2609.11689
  (geospatial FMs beyond social risk indices, foundation-model
  keyword hit) — geospatial-FM audit vs. ADI/SDI/SVI on CDC PLACES
  outcomes. Interesting but not on your active threads (no EHR /
  biobank / phenotyping / KG / rare-disease overlap). SKIP with a
  bookmark for later if you get into place-based confounders in AoU /
  MVP work.
- **Xu, Li, Nan** *Int J Neurosci* (CD40 in MG via MR, variant-
  interpretation keyword feed) — small applied MR study; off-thread
  disease. SKIP.
- **Liang, Ma, Wang, Yan, Ma** *Eng Appl AI* (multimodal KG reasoning
  survey) — general-domain survey; skim only if you need a citation
  handle for the survey. SKIP for direct research relevance.
- **Ottman, Wetmore, Leu, Uhlmann** *[venue TBD]* 2026 (APOE-
  disclosure RCT in Latinos, Wendy Chung feed) — psychological
  impacts of APOE genotype disclosure; niche disclosure-ethics work,
  not on your APOE-thread. SKIP unless you're branching into
  genotype-disclosure ethics.
- **Trujeque, Simonetti, Ortiz, Ingraham** *JMIR* 2026 (NLP for
  nonprescribed fentanyl in EHRs, Hripcsak feed) — solid applied NLP
  paper on a substance-use phenotype; off-thread disease. SKIP unless
  the Lyu et al. OUD paper above surfaces methods overlap.
- **Islam, Foraker, Hossain, Arnold** *JMIR Formative* 2026 (HSV-1 →
  dementia longitudinal PS analysis) — high-dimensional propensity
  score (17k covariates) is on-thread methodologically, but the
  HSV→dementia hypothesis is off your active-thread list. SKIP unless
  the causal-forest methods section is worth cribbing.
- **Diaby, Feizy, Zhang et al.** *Addictive Behaviors* 2026 (AoU
  poly-tobacco disparities) — AoU cohort work but the substance-use
  angle is not on your active threads. SKIP unless the AoU cohort
  construction section is worth reading.
- **Schulte-Althoff, Krappen, Bießmann, Jäger** *npj Health Systems*
  2026 (SHAP fall-risk profiling from EHRs) — solid applied inpatient
  fall-risk work; SHAP-space at group level is on-thread
  methodologically for `Fidelity, portability, and audit of
  representations`. Skim only.
- Various other UK Biobank Scholar hits — bronchiectasis proteomics,
  ANGPTL3 mortality, MCI classifier in CAD+HTN, residential green/
  blue space × COPD, allostatic load proteomic signature — all UKB
  applied cohort studies, none on your active disease threads. SKIP.
- Various "knowledge graph" keyword-feed hits — elevator fault
  diagnosis, financial fraud, cultural-heritage KGs — off-topic.
  SKIP.

---

## Cross-window carry-over notes

- The **Zhang et al. GLP-1 / SGLT2 / DPP4 empirically-calibrated TTE**
  paper flagged in the 2026-09-01 report is now cited in downstream
  work — expect it to be a reference anchor for the target-trial
  emulation cluster this window. No new companion paper surfaced
  this window; keep watching Hripcsak citations-to.
- **CohortContrast (Ilves et al.)** from the prior window pairs
  naturally with Xiong et al. JASA (this window) and Dymshyts et al.
  OHDSI PL (this window) — three complementary vectors on OMOP
  concept-set fidelity in one 4-week span, an unusually dense
  moment for that sub-thread.
- **Kurniansyah et al. multiancestry AD-PRS** (*Nat Genet* 2026,
  prior window) and Zheng et al. absorption/coexpression modules
  (this window) both feed the multi-omics-augmented PRS in
  neurodegeneration cluster — read them together with the
  Ran/Benatar ALS carrier-phenoconversion template you already track.
- The **Karczewski feed's Heilbron dissertation** (causal-gene
  identification in GWAS loci) surfaced this window but isn't strong
  enough on its own to flag HIGH — dissertations from strong labs
  are worth a skim for the framing, not for the method. Note for
  next window's watch list.

---

## Actions / follow-through suggestions

1. Prioritize reading order (top three): Wang et al. *Nature* Mexican
   within-family ancestry → Xiong et al. JASA KOMAP-online →
   Carrasco-Zanini et al. STM rare-disease proteomics.
2. The 09-14 Hripcsak feed alone delivered **eight** on-thread papers
   in one alert — worth confirming that citations-to feed is still
   configured for that author and set up as an aggressive alert
   (author feeds compress dense clusters like this into a single
   email that's easy to miss on a busy morning).
3. Consider adding **"absorption module" OR "coexpression module"**
   as a new keyword under `config/tracked.yaml` — the Zheng et al.
   framing looks like it will propagate.
4. Consider dropping the **"knowledge graph"** raw keyword feed —
   after several weeks it's mostly off-topic (elevator fault
   diagnosis, financial fraud, CMC process development, cultural
   heritage). Replace with a narrower feed like
   **"knowledge graph" AND ("electronic health records" OR "EHR"
   OR "phenotyping" OR "OMOP" OR "clinical")**.
5. Two orthogonal-methods papers are ripe for combined citation:
   Snel & Schulz influence-function Cohen's d (this window) + the
   Wu et al. auditable-CT-phenotyping (prior window) → a coherent
   "influence-function-based audit of biobank case-control models"
   frame you could carry into your own work.
