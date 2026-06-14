# Research digest report — 2026-06-13

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-06-02 → 2026-06-13** (since the prior 2026-06-01 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-06 → 06-13 | Five batches: 06-06 12:24Z, 06-07 16:07Z, 06-08 07:03Z, 06-09 10:59Z, 06-11 00:14Z, 06-11 19:32Z, 06-12 10:41Z, 06-13 03:56Z. |
| `arxiv-digest` repo (`digests/`) | 2026-06-02 → 06-13 | **12 daily files; 5 non-empty.** 06-02/03/07/08/13 empty (06-03 logged 3/4 q-bio fetch failures again); 06-06 = 2 papers; 06-09 = 3 papers; 06-10 = 2 papers; 06-11 = 4 papers; 06-12 = 1 paper. |
| NCBI "My NCBI What's New" (AoU, UK Biobank) | daily | Aggregate PubMed digests; not individually triaged here. |
| bioRxiv / medRxiv subject alerts | daily | Aggregate collection digests; not individually triaged here. |

> ⚠️ **`arxiv-digest` is back online** for most of the window — the
> upstream q-bio fetch issue that suppressed the prior report (and again
> on 06-03) has partially recovered: 06-06 onward we're getting consistent
> daily catches. Net signal is still thin (12 papers across 12 days, mostly
> single-keyword score-1 hits) and 80%+ of genuinely on-thread material
> continues to come from Scholar alerts / journals outside arXiv. The
> recommendation from the last two reports stands: add `cs.LG`, `stat.ME`,
> and a medRxiv/bioRxiv feed.

> Caveat: Scholar alert emails contain title, authors, venue, and the first
> ~2-3 lines of each abstract only. The reports below contextualize that
> metadata against your research threads; nothing here reflects full-text
> reading.

---

## Executive summary

- **Penetrance-in-population-screening is the strongest single signal
  this window.** A new Human Molecular Genetics paper (Ramchand et al.)
  characterizes *limited* penetrance of dominantly-inherited AIRE variants
  in a population-based cohort — and it lands in your *self-citation*
  feed for the "Guidance for estimating penetrance of monogenic …"
  paper. Penetrance gap between population vs ascertained cohorts is the
  exact pattern your PheWAS/PheRS thread is built around.
- **Variant carrier × drug-class × EHR outcomes is a recurring shape.**
  Marston et al. (Nature Medicine, Ellinor alert) report SGLT2i effects
  on incident heart failure *stratified by cardiomyopathy-associated
  variant carrier status* — a clean monogenic-carrier × drug-class
  interaction in an EHR-linked setting. Squarely on your PRS-stacked-with-
  rare-pathogenic-variant composite-risk thread, and on the SGLT2i drug
  class.
- **CHIP & APOL1 disease threads both have new high-tier items.** CHIP
  evolution during cancer treatment (Arabzadeh, JCI) extends the
  treatment-associated CHIP literature you've been tracking; APOL1-risk
  alleles modulating allograft rejection via TCR signaling (Pell, JCI)
  feeds directly into the APOL1 transplant decision-making thread.
- **LLM-assisted phenotyping / variant curation is becoming a small
  cluster.** Five separate items: MARRVEL-MCP (agentic Mendelian
  diagnosis, AJHG), Agentic Authoring of OMOP Concept Sets (Chen et al.,
  medRxiv, Bian/Chute lineage), MedADL (frailty/functional status
  extraction), Genosolver (rare disease NLP), VarLitBench/VarLitAgent
  (LLM evidence curation for ACMG). Together these suggest the
  LLM-assisted phenotype/variant-curation tooling is hitting a critical
  mass — worth a horizontal scan rather than just paper-by-paper.
- **EHR foundation models**: two items in the CLMBR/MOTOR/FEMR lineage —
  Clinical-MoE (MoE foundation models for EHR) and *From Foundation
  Models to Foundation Specialists* (distillation from large EHR
  models).
- **Cross-ancestry portability**: Das & Cui (Karczewski feed) propose
  *tabular foundation models* as an ancestry-gap-bridging mechanism for
  PRS — methodological novelty for your trans-ancestry PRS portability
  thread.
- **Drug repurposing**: thin this window. The AI-in-drug-repurposing
  review (Cielecka-Piontek/Souto) and the ceRNA-network/AUD piece
  (Kavousipour et al.) are both off-thread (neither has the EHR or
  KG-with-explainability angle you flagged). No HIGH-priority
  repurposing items.
- **arxiv-digest contributions**: BartCure (Bayesian causal ML for cure
  models, stat.ME 06-11) on treatment-effect heterogeneity in survival,
  and Shen et al. on external controls for treatment switching in
  oncology RCTs (stat.ME 06-06) — both methods-grade picks on the causal
  ML thread.

Counts: **17 HIGH**, **6 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. Limited penetrance of dominantly inherited AIRE variants in a population-based cohort
- **Authors / venue:** S.N. Ramchand, J.M. Leech, L.N. Sharp, G. Bonfield et al. — *Human Molecular Genetics*, 2026.
- **Surfaced by:** Google Scholar "*Guidance for estimating penetrance of monogenic …*" **new citations** alert (06-13) — i.e., this paper cites work directly adjacent to / by you on penetrance estimation methodology.
- **Thread:** PheWAS/PheRS → **penetrance estimation under population-
  screening conditions** (vs clinically ascertained cohorts).
- **What it is:** Population-based estimation of penetrance for
  *dominantly inherited* AIRE variants (canonical APS-1 / autoimmune
  polyendocrine syndrome type 1 gene). The snippet emphasizes
  "pathogenic variants in the [AIRE gene] … limited penetrance" — i.e.,
  the population-cohort effect size is meaningfully lower than the
  classical clinical-cohort estimate.
- **Why it matters to you:** This is *exactly* the
  population-vs-clinical penetrance gap your INTERESTS file calls out.
  AIRE is also a useful test case because dominant inheritance with
  variable penetrance is the regime where PheRS-style composite
  phenotype scoring helps most — the surfaced phenotypes diverge from
  the textbook APS-1 picture and a phenotype-summary score can detect
  partial penetrance that ICD codes alone miss. Worth reading as a
  template for how to write up *any* monogenic variant where the
  biobank-derived penetrance estimate is lower than the clinical
  estimate.
- **Action:** **HIGH** — read for (i) the population denominator and
  ascertainment, (ii) effect size relative to APS-1 clinical case
  series, and (iii) whether the authors use phecode summaries or
  endpoint-by-endpoint risk ratios.

### 2. Effects of SGLT2 inhibition on incident heart failure in carriers of cardiomyopathy-associated genetic variants
- **Authors / venue:** N.A. Marston, S. Kany, G.E.M. Melloni, S.J. Jurgens et al. — *Nature Medicine*, 2026.
- **Surfaced by:** Patrick T. Ellinor "new articles" alert (06-12).
- **Thread:** Causal inference / pharmacoepi (**SGLT2i** drug-class)
  **+** composite-risk modeling (PRS stacked with rare pathogenic
  variants) **+** EHR-linked biobank outcomes.
- **What it is:** Stratified effect of SGLT2i on incident heart failure
  in carriers of cardiomyopathy-associated rare/monogenic variants. The
  snippet is truncated but the framing is a *monogenic-carrier × drug
  × outcome* interaction in a biobank cohort.
- **Why it matters to you:** Multi-thread hit. (a) SGLT2i is on your
  active drug-class list. (b) The carrier-stratified design is the
  prototype shape for the kind of pharmacogenomic-pharmacoepi work that
  feeds composite-risk modeling — variant evidence modifying drug
  benefit/harm. (c) Ellinor's group typically uses UKB/MGB; the cohort
  and outcome ascertainment will be directly transferable. *Nature
  Medicine* tier — likely to drive citations.
- **Action:** **HIGH** — read for (i) the variant ascertainment
  (curated cardiomyopathy panel or ClinGen?), (ii) confounding-by-
  indication handling (active comparator vs no-comparator?), (iii)
  whether interaction is on multiplicative or additive scale and
  whether a TTE framing is used.

### 3. Evolution of clonal hematopoiesis during cancer treatment and its impact on outcomes
- **Authors / venue:** M. Arabzadeh, Y.H. Tang, C. Colin-Leitzinger, S. Marzban et al. — *Journal of Clinical Investigation*, 2026.
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert (06-13).
- **Thread:** Clonal hematopoiesis (CHIP) disease thread.
- **What it is:** Longitudinal CHIP dynamics under cancer therapy and
  the downstream outcome consequences. Snippet positions CHIP as
  *evolving* during treatment (presumably enrichment of specific
  driver mutations under selection from cytotoxic / targeted therapy)
  and ties that to outcomes.
- **Why it matters to you:** Pairs with the JCI-tier *t-CHIP* / therapy-
  associated literature you've been tracking. Distinct from the
  Bick stroke paper and the post-HCT meta-analysis (last report's #4)
  because the unit of analysis is *clone evolution under treatment
  pressure*, not cross-sectional CHIP carrier status. Useful for any
  composite-risk model where CHIP status is dynamic rather than a
  baseline binary.
- **Action:** **HIGH** — read for the longitudinal sampling design and
  the driver-mutation level breakdown (DNMT3A vs TET2 vs splice/PPM1D
  expansions under chemotherapy).

### 4. APOL1-risk alleles modulate T-cell receptor signaling to promote allograft rejection
- **Authors / venue:** J. Pell, E.M. Tanvir, Z. Sun, I. Chernova, A. Reghuvaran et al. — *Journal of Clinical Investigation*, 2026.
- **Surfaced by:** "APOL1" keyword alert (06-13).
- **Thread:** APOL1 (kidney disease / transplant decision-making /
  ancestry).
- **What it is:** Mechanistic study showing G1/G2 APOL1 risk alleles
  modulate T-cell receptor signaling and thereby promote allograft
  rejection. Bridges *genetic risk* and *clinical transplant outcome*
  via an immune mechanism rather than the more familiar
  podocyte-injury / focal-segmental-glomerulosclerosis route.
- **Why it matters to you:** Your INTERESTS file lists APOL1 as
  "kidney disease risk, **transplant decision-making**, ancestry
  considerations." This paper is a mechanistic underpinning for a
  *recipient-side* APOL1 transplant-decision question that complements
  the existing donor-side literature (kidneys from G1/G2 donors). A
  causal mechanism (TCR signaling) also strengthens any
  observational-design argument you'd make in a transplant-outcomes
  paper.
- **Action:** **HIGH** — read for the *in vivo* model, the human
  validation cohort (if any), and whether the authors discuss
  recipient-side APOL1 genotyping policy implications.

### 5. Update on APOL1 and chronic kidney diseases in children
- **Authors / venue:** J.D. Varner, T.O. Ilori, R.A. Gbadegesin — *Pediatric Nephrology*, 2026.
- **Surfaced by:** "APOL1" keyword alert (06-08).
- **Thread:** APOL1 disease thread (pediatric extension).
- **What it is:** Review piece updating APOL1 / CKD in pediatric
  populations, with explicit mention of "kidney transplant outcomes and
  pregnancy" in the snippet.
- **Why it matters to you:** Two-line pediatric coverage of an
  area where most prior literature is adult. The
  transplant-outcomes-and-pregnancy axis intersects your transplant-
  decision thread.
- **Action:** **HIGH** — skim as a citation source for the pediatric
  APOL1 picture; useful background for any cross-age APOL1 work.

### 6. Polygenic risk scores for prediction of immune checkpoint inhibitor thyroid toxicity in diverse populations
- **Authors / venue:** L.G. Fritsche, L.M. Higgins, M. Schipper, G. Strohbehn et al. — *Clinical Cancer Research*, 2026.
- **Surfaced by:** **Two** alerts — Joshua C. Denny + Lisa Bastarache *new related research* (06-09 / 06-11).
- **Thread:** Genetic epidemiology (PRS) **+** pharmacoepi (drug-toxicity
  prediction) **+** cross-ancestry portability.
- **What it is:** PRS for ICI-induced thyroid toxicity — i.e., uses
  germline polygenic risk for autoimmune thyroid disease to predict who
  develops thyroiditis on PD-(L)1 blockade — evaluated *across
  ancestries*. The Fritsche lab pattern is exactly the
  PRS-for-drug-adverse-event one you've been tracking.
- **Why it matters to you:** Hits three of your threads at once: PRS
  construction, cross-ancestry validation, and pharmacoepidemiology of a
  drug class. ICI thyroiditis is also a clean Mendelian-adjacent
  pharmacogenomic outcome (autoimmunity unmasked by checkpoint
  blockade) — similar in shape to your interest in monogenic carriers
  developing endpoints under environmental triggers. Two-alert
  saturation (Denny + Bastarache) signals strong group-level relevance.
- **Action:** **HIGH** — read for the cross-ancestry calibration
  curves, decision-curve analysis (if any), and the autoimmune-thyroid
  GWAS used as the source PRS.

### 7. Bridging Ancestry Gaps in Genomic Risk Prediction with Tabular Foundation Models
- **Authors / venue:** A. Das, Y. Cui — *bioRxiv*, 2026.
- **Surfaced by:** Konrad Karczewski *new related research* alert (06-07).
- **Thread:** Genetic epidemiology (cross-ancestry PRS portability) **+**
  EHR/tabular foundation models.
- **What it is:** Applies tabular foundation models (TabPFN-style) to
  the cross-ancestry PRS portability problem. Snippet flags
  "models deployed for genomic prediction of diseases perform unevenly
  [across ancestries]" — i.e., the classic PRS-portability gap — and
  proposes a tabular-FM solution.
- **Why it matters to you:** Tabular FMs are a recent methods wave
  (TabPFN, TabuLa-8B). Pulling that thread into PRS portability is on
  the cutting edge of your trans-ancestry composite-risk thread. Worth
  reading whether the FM is used as a *transfer prior* (fine-tune on a
  small target-ancestry cohort) or as a meta-learner that pools across
  ancestries.
- **Action:** **HIGH** — read for the tabular FM choice, the held-out
  ancestry benchmark, and whether the gain comes from the FM
  pretraining vs from architectural choices (PRS-augmented features).

### 8. MARRVEL-MCP: An agentic interface for Mendelian disease discovery via tool-augmented context engineering
- **Authors / venue:** Z. Everton, J. Botas, S.Y. Kim, L. Yao, Z. Liu, H.H. Jeong — *American Journal of Human Genetics*, 2026.
- **Surfaced by:** Lisa Bastarache *new related research* alert (06-11).
- **Thread:** Rare disease (HPO-based diagnosis) **+** LLM-assisted
  phenotyping **+** variant interpretation.
- **What it is:** MARRVEL-MCP — an *MCP-style agentic interface* on top
  of the MARRVEL Mendelian-disease knowledge base. Tool-augmented LLM
  reasoning over phenotype / variant / gene evidence.
- **Why it matters to you:** Sits at the intersection of two active
  threads. (a) Rare-disease diagnosis with HPO grounding. (b) Your
  LLM-assisted phenotyping & OMOP thread, with the agentic-MCP wrinkle.
  AJHG audience suggests it's targeted at clinical-genetics adoption
  rather than pure ML-tooling. Pairs with #15 below (G. AI) as the
  *clinical-deployment-grade* end of the LLM-rare-disease tooling
  cluster.
- **Action:** **HIGH** — read for the tool inventory (which MARRVEL
  endpoints are exposed) and the prompt / orchestration pattern; useful
  template for any agentic rare-disease pipeline you might build.

### 9. Targeted reflex RNA sequencing for enhanced variant classification on exome and genome sequencing improves patient outcomes
- **Authors / venue:** X. Zhao, R. Rigobello, M. Driver, S. Lau, M.L. Chong et al. — *npj Genomic Medicine*, 2026.
- **Surfaced by:** Konrad Karczewski + Lisa Bastarache *new related
  research* alerts (06-09, 06-11, 06-12 — **3 author alerts**).
- **Thread:** Variant interpretation (ACMG/ClinGen, **splicing/RNA
  evidence for VUS resolution**).
- **What it is:** Reflex RNA-seq triggered by ambiguous WES/WGS calls
  (specifically targeting predicted splice variants and pseudo-exons)
  to upgrade or downgrade VUSs. Demonstrates downstream effect on
  patient outcomes — i.e., diagnostic / management uplift.
- **Why it matters to you:** This is *the* canonical
  splicing-RNA-evidence-for-VUS-resolution paper for the window — your
  INTERESTS file calls out "splicing/RNA evidence for VUS resolution"
  explicitly under variant interpretation. Triple-alert saturation
  (Karczewski + Bastarache, twice) is a strong signal it'll be the
  go-to citation for RNA evidence in VCEP guidance updates over the
  next year.
- **Action:** **HIGH** — read for the reflex *trigger criteria* (which
  ACMG codes / which in silico flags), the assay (targeted
  short-read vs. long-read RNA), and the per-patient outcome metric.

### 10. Clinical-MoE: Mixture-of-Experts Foundation Models for Electronic Health Records
- **Authors / venue:** M. Chen, Z. Wang, Y. Li, X. Li, T. Zhang, H. Liu, J. Xu et al. — 2026.
- **Surfaced by:** "Foundation models and 'electronic health records'" keyword alert (06-13).
- **Thread:** EHR foundation models (CLMBR/MOTOR/FEMR/MEDS lineage).
- **What it is:** Mixture-of-experts architecture for EHR foundation
  models. MoE on EHR is a natural step now that token-level FMs (CLMBR,
  MOTOR) have stabilized — different experts can specialize on
  modality streams (codes vs labs vs meds vs notes) or on
  patient-population strata. Snippet truncates after the framing.
- **Why it matters to you:** Slot directly into your CLMBR/MOTOR/FEMR
  thread. MoE-on-EHR is also a plausible answer to the
  patient-heterogeneity problem that's been flagged in the
  patient-aware sampling work (ICML 2026 workshop in the prior report).
- **Action:** **HIGH** — read for routing strategy (per-token vs
  per-visit vs per-patient), the expert specialization that emerges
  empirically, and the downstream-task evaluation suite.

### 11. From Foundation Models to Foundation Specialists: Distilling Clinical Knowledge from Large EHR Models
- **Authors / venue:** J. Liu, X. Zhao, Y. Wang, X. Li, Y. Xu, H. Wang, Z. Chen et al. — 2026.
- **Surfaced by:** "Foundation models and 'electronic health records'" keyword alert (06-11).
- **Thread:** EHR foundation models — *adaptation / distillation*.
- **What it is:** Distills knowledge from large EHR FMs into smaller
  task-specific "specialists" — i.e., the
  pretrain-once-distill-many pattern (already standard in language)
  applied to EHR.
- **Why it matters to you:** Most groups don't have the compute to
  pretrain a CLMBR/MOTOR from scratch but can absolutely run a
  distillation step. Practically useful for getting on-thread EHR FM
  capability into AoU / UKB pipelines without reinventing pretraining.
  Pairs with #10 (Clinical-MoE) as the two ends of the EHR FM stack
  this window.
- **Action:** **HIGH** — read for the distillation recipe (logit
  distillation? feature distillation?) and which downstream tasks
  retain vs lose performance under compression.

### 12. MedADL: High-Throughput Information Extraction of Functional Status from Electronic Health Records to Advance Frailty Assessment in Older Adults
- **Authors / venue:** S. Fu, Z. Yue, J.T. Nguyen, H. Liu, J. Ahn, V. Ramirez et al. — 2026.
- **Surfaced by:** "electronic health records" keyword alert (06-13).
- **Thread:** EHR phenotyping (computable phenotype for functional
  status / frailty, **clinical-notes NLP**) **+** multimorbidity (frailty
  is the cross-system summary phenotype).
- **What it is:** High-throughput information extraction (likely
  LLM-assisted) of *functional status* (ADLs/IADLs) from EHR clinical
  notes for frailty assessment in older adults.
- **Why it matters to you:** Functional status / frailty is one of the
  highest-value note-derived phenotypes precisely because it is
  *systematically under-coded* in ICD/CPT — exactly the kind of
  phenotype where LLM extraction beats rules-based by a wide margin.
  Directly serves your computable-phenotype / LLM-assisted phenotyping
  interest. Frailty is also the canonical multimorbidity summary
  endpoint.
- **Action:** **HIGH** — read for the LLM extraction prompt /
  fine-tuning recipe and the validation against gold-standard ADL
  rating scales; useful template for your own AoU note-extraction
  work.

### 13. Agentic Authoring of OMOP Concept Sets from Natural Language
- **Authors / venue:** H. Chen, X. He, H. Dai, Y. Huang, M. Liu, J. Bian — *medRxiv*, 2026.
- **Surfaced by:** Christopher G. Chute *new related research* alert (06-07).
- **Thread:** EHR phenotyping & **OMOP** (computable-phenotype
  construction).
- **What it is:** Agentic LLM pipeline that takes a *natural-language
  phenotype description* and emits an OMOP CDM concept set ready for
  OHDSI cohort definition. Direct response to one of the longest-
  standing OHDSI workflow pain points.
- **Why it matters to you:** OMOP concept-set authoring is one of the
  manual steps that gates fast iteration on OHDSI/AoU phenotype
  studies. An agentic NL→concept-set tool is squarely on your
  EHR-phenotyping & LLM-assisted-phenotyping interests. Bian group is
  prolific in this area; expect this to evolve into a
  community-adopted tool.
- **Action:** **HIGH** — read for the tool's evaluation harness (how
  is concept-set quality measured?), and whether they evaluate on
  ATLAS-curated reference concept sets.

### 14. GWAS of extended prescription analgesic use identifies genetic loci in chronic pain
- **Authors / venue:** C.E. Harlow, E. Uzochukwu, H.A. Fernando, C.E. Mordaunt et al. — *Nature Communications*, 2026.
- **Surfaced by:** Jian Yang *new related research* alert (06-12).
- **Thread:** Genetic epidemiology (GWAS, **drug-utilization-derived
  phenotyping**) **+** pharmacoepidemiology.
- **What it is:** GWAS where the *phenotype* is extended prescription
  analgesic use — i.e., medication-record-derived chronic pain
  endpoint. Identifies new genetic loci tied to pain.
- **Why it matters to you:** Drug-utilization-as-phenotype is a
  recurring shape in EHR-linked biobank work, and your INTERESTS file
  highlights "methods that exploit the depth of EHR follow-up
  (medications, labs, imaging codes) for genetic studies" specifically.
  Worth reading whether they handle confounding-by-indication (e.g.,
  cancer pain vs musculoskeletal pain) in the phenotype definition.
- **Action:** **HIGH** — read for the drug-record phenotype operational
  definition (which ATC classes, what duration threshold), and the
  comparison to non-medication-defined pain phenotypes.

### 15. G. AI: an AI-driven platform for phenotype standardization, variant interpretation and structured clinical reporting in rare disease genomic diagnosis
- **Authors / venue:** Z. Wang, X. Chen, L. Tang, X. Wu, A. Huang, H. … — 2026.
- **Surfaced by:** "rare diseases" keyword alert (06-09).
- **Thread:** Rare disease (HPO-based phenotyping) **+** variant
  interpretation (ACMG) **+** LLM-assisted clinical reporting.
- **What it is:** End-to-end platform for rare-disease diagnostic
  workflow — phenotype standardization (likely HPO normalization),
  variant interpretation (ACMG-style classification), and structured
  reporting. Aimed at clinical-grade deployment rather than research
  prototype.
- **Why it matters to you:** Pairs with #8 (MARRVEL-MCP) as the
  *integration-platform* and *agentic-tool-augmented-LLM* ends of the
  rare-disease pipeline. Worth knowing how the two compare on the
  phenotype-standardization step (HPO normalization is the lever that
  most often blocks downstream variant prioritization).
- **Action:** **HIGH** — read for the platform's HPO-normalization
  approach and whether the variant-interpretation module produces
  ACMG-compliant evidence-code output.

### 16. An integrated proteogenomic investigation of the human liver uncovers molecular drivers of steatotic liver disease
- **Authors / venue:** É. Gobeil, J. Bourgault, M. Enault, V. Côté, P.L. Mitchell et al. — *medRxiv*, 2026.
- **Surfaced by:** Jonathan K. Pritchard *10 new citations* alert (06-12).
- **Thread:** Genetic epidemiology (proteome-MR / multi-omics
  triangulation) **+** drug-target prioritization **+** liver disease
  (MASLD).
- **What it is:** Integrated proteogenomic study of the human liver
  identifying molecular drivers of MASLD. Continues the proteome-MR
  triangulation template you saw four times in the prior two windows
  (now five).
- **Why it matters to you:** Two angles. (a) Method: continues the
  proteome-MR pattern — fifth instance in three windows reinforces
  that this template is the dominant target-discovery shape across
  organ systems. (b) Disease: MASLD pairs with the GLP-1 → liver
  outcomes paper (Chung et al., AJG) flagged as HIGH in the last
  report. Together they form a *MASLD biology + GLP-1 pharmacoepi*
  pair that is naturally co-cited in a discussion section.
- **Action:** **HIGH (methods + disease)** — skim the triangulation
  pipeline (likely GWAS + pQTL MR + colocalization in liver tissue)
  and harvest any new MASLD drug targets surfaced.

### 17. Biological and mechanistic pathways of cardiometabolic multiple long-term conditions
- **Authors / venue:** L.L. Lim, A. Jenkins, D. Prabhakaran, S. Sookoian et al. — *The Lancet*, 2026.
- **Surfaced by:** Joshua C. Denny *10 new citations* alert (06-12).
- **Thread:** Chronic disease clustering / multimorbidity (**cardiometabolic
  MLTC**).
- **What it is:** *Lancet* mechanistic review of biological pathways
  underlying cardiometabolic multiple long-term conditions (MLTC) —
  i.e., a mechanistic counterpart to the EHR-pattern-mining
  multimorbidity literature.
- **Why it matters to you:** Cardiometabolic MLTC is explicitly called
  out in your multimorbidity thread. Mechanism-side framing pairs well
  with the deterministic-overlapping-multimorbidity AoU paper
  (Rahemi & Omidi) from the last report — together they bracket the
  multimorbidity work between *clinical mechanism* (this paper) and
  *operational phenotype definition*. Lancet-tier, so will be a
  default citation in any multimorbidity write-up for the next ~2
  years.
- **Action:** **HIGH** — read as a citation anchor; pull the pathway
  taxonomy and check whether the proposed mechanistic clusters map onto
  the EHR-defined trajectories your prior work surfaces.

### 18. Bayesian Causal Machine Learning for Cure Models (BartCure)
- **Authors / venue:** A.R. Linero, F.J. Rubio, P. Basak — *arXiv stat.ME*, 2026 (digest 06-11).
- **Surfaced by:** `arxiv-digest` 2026-06-11, keyword hit *treatment effect heterogeneity*.
- **Thread:** Causal inference (modern causal ML, **HTE**) **+** ML for
  precision health (survival under cure structures).
- **What it is:** BartCure — Bayesian causal ML for *cure models*
  (survival models with a cured subpopulation). Decomposes the causal
  effect on RMST into stochastic cure and stochastic latency
  components, with HTE detection via Bayesian shrinkage. Applied to
  CALGB 40101 (breast cancer adjuvant chemo).
- **Why it matters to you:** Sits cleanly at the intersection of your
  causal-ML thread (HTE, debiased ML) and your ML-for-precision-health
  thread (survival, treatment-effect-heterogeneity for clinical
  decisions). The cure-model framing is also clinically meaningful:
  many oncology and rare-disease outcomes have a cured subpopulation
  that standard Cox HTE models conflate with delayed failure. Bayesian
  shrinkage makes the HTE-direction call more conservative — your
  INTERESTS file specifically calls out "calibration" and "decision-
  curve analysis" for ML-precision-health work, both natural next
  steps for this approach.
- **Action:** **HIGH (methods)** — read for the principal-strata
  formulation and the simulation behavior on direction-of-HTE
  detection.

### 19. Leveraging External Controls for Treatment Switching in Randomized Controlled Trials: A Weighted Causal Inference Framework for Overall Survival
- **Authors / venue:** A.A. Shen, C. Fu, R. Lin — *arXiv stat.ME*, 2026 (digest 06-06).
- **Surfaced by:** `arxiv-digest` 2026-06-06, keyword hit *causal inference*.
- **Thread:** Causal inference / pharmacoepi (synthetic / external
  controls, **treatment switching**).
- **What it is:** Framework combining synthetic-control + balancing-
  weight methods to handle *treatment switching* (when control-arm
  patients cross over to the experimental arm or to a third therapy
  mid-trial). Uses multiple imputation with time-varying weights;
  illustrated on two phase III oncology trials.
- **Why it matters to you:** Treatment switching is exactly the kind
  of structural problem that broke your last *crossover-adjusted Cox*
  efforts in target-trial-emulation work. Pairs with the
  TTE-and-external-controls work in pharmacoepi (RCT + RWE hybrid
  designs are now standard). The synthetic-control component is also
  on your modern-causal-ML thread.
- **Action:** **HIGH (methods)** — read for the risk-set-selection rule
  for external controls (this is the part that breaks identifiability
  if done casually) and the simulation comparison against rank-
  preserving structural failure-time (RPSFT).

### 20. VarLitBench and VarLitAgent for Benchmarking and Automating LLM-Assisted Functional Evidence Curation in Genomic Variant Interpretation
- **Authors / venue:** A. Saadat, J. Fellay — *2026 Workshop on Generative and Agentic [AI for Health?]*, 2026.
- **Surfaced by:** "variant interpretation" keyword alert (06-13).
- **Thread:** Variant interpretation (ACMG/ClinGen, **functional
  evidence curation**) **+** LLM-assisted phenotyping.
- **What it is:** A benchmark (VarLitBench) and agent (VarLitAgent)
  for LLM-driven *functional evidence curation* — i.e., automating the
  literature-mining step that supports ACMG PS3/BS3 evidence codes.
- **Why it matters to you:** PS3/BS3 is one of the most expensive
  manual evidence steps in ClinGen VCEP curation; an LLM agent that
  can at least pre-screen the functional literature would be a
  practical accelerator. Pairs with #9 (reflex RNA-seq) as the
  *programmatic evidence collection* side of variant interpretation
  to complement the *assay-driven evidence collection* side.
- **Action:** **HIGH** — read for the benchmark composition (which
  variants, which ACMG codes evaluated) and the agent's
  performance vs. expert-curated baseline. Useful template if you
  consider building a ClinGen-specific variant-curation copilot.

### 21. When can whole-genome SNP heritability be reliably estimated from summary statistics?
- **Authors / venue:** B.K. Pham, S. Davenport, D. Azriel, A. Schwartzman — *bioRxiv*, 2026.
- **Surfaced by:** Jian Yang *new related research* alert (06-07, 06-11).
- **Thread:** Genetic epidemiology (**LDSC limits**, summary-stat
  heritability).
- **What it is:** Theoretical / empirical characterization of when
  LDSC-style heritability estimation from summary statistics is
  reliable — likely identifies the regimes (LD reference choice,
  trait polygenicity, sample size, MAF/LD weighting) where LDSC
  estimates diverge from REML.
- **Why it matters to you:** LDSC is the workhorse for any cross-trait
  / cross-ancestry heritability comparison you do; a principled
  characterization of when it fails is methodologically important.
  Two-alert surfacing in the Yang feed strengthens the signal.
- **Action:** **HIGH (methods)** — read for the failure modes
  identified (likely high-polygenicity + low-LD-reference-match
  scenarios) and any practical diagnostic the authors propose.

### 22. Genosolver: Rare Disease Diagnosis through Holistic Integration of Unstructured Clinical Narratives Using Large Language and Reasoning Models
- **Authors / venue:** T. Islam, M. Danner, Z. Ziad, M. Begemann, D. Beijer et al. — 2026.
- **Surfaced by:** Christopher G. Chute *7 new citations* alert (06-11).
- **Thread:** Rare disease (**clinical NLP for ultra-rare disease**) **+**
  LLM reasoning models.
- **What it is:** Genosolver — LLM + reasoning-model integration over
  *unstructured clinical narratives* for rare-disease diagnosis.
  Reasoning-model framing (likely o1-style chain-of-thought or a
  similar test-time-compute approach) suggests they're targeting the
  hard differential-diagnosis cases that fail HPO-based prior tools.
- **Why it matters to you:** Your INTERESTS file calls out
  "ultra-rare clinical NLP" specifically. Reasoning models are a
  natural fit for the *iterative-hypothesis* shape of rare-disease
  workups. Pairs with #8 (MARRVEL-MCP) and #15 (G. AI) as the third
  axis (note-narrative vs structured phenotype) of the rare-disease
  LLM tooling cluster.
- **Action:** **HIGH** — read for the reasoning-model choice and
  whether the evaluation set is a real undiagnosed-disease cohort
  (UDN-style) or a synthetic benchmark.

### 23. Trans-ethnic estimation and implications of genetic impact on continuous glycemic profiles
- **Authors / venue:** E.Y.W. Yu, H.Y. Ren, X. Liang, Y. Xi, M. Shuai, Z. Miao, F. Xu et al. — *Cell Discovery*, 2026.
- **Surfaced by:** Jian Yang *10 new citations* alert (06-07).
- **Thread:** Genetic epidemiology (**trans-ancestry**, biomarker-as-
  exposure / continuous-glycemic-trait GWAS).
- **What it is:** Trans-ethnic GWAS + downstream estimation on
  continuous glycemic profiles (likely CGM-derived metrics rather than
  HbA1c alone, given "continuous"). Identifies genetic architecture
  and cross-ancestry portability of glycemic phenotypes.
- **Why it matters to you:** Pairs naturally with the G6PD rs1050828
  paper from the last report (#13 in 2026-06-01 report) — both deal
  with *variant-biomarker confounding* in glycemic phenotyping.
  Cross-ancestry continuous-biomarker GWAS is also methodologically
  upstream of any cross-ancestry diabetes PRS you'd build in AoU.
- **Action:** **HIGH** — read for the cross-ancestry effect-size
  comparison and any methods detail on continuous-glycemic phenotype
  harmonization.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **OmniBioTwin: A System-of-Twinned-Systems Framework for Health Digital
  Twins** — Z. Wang, Y. Huang, J. Bian — *arXiv q-bio.QM*, 2026 (digest
  06-11). Multiscale digital-twin framework, instantiated with a
  GLP-1/Alzheimer's case study. The GLP-1 angle is a keyword incident
  rather than a real pharmacoepi study, but the *system-of-systems*
  abstraction is an interesting reference architecture if you ever
  consider multiscale modeling integrated with EHR cohorts. *Watch
  for:* the layer decomposition and the cross-scale coupling operators.
- **Predicting Hospitalization from a Whole-Person Health Score with
  Incomplete EHR Data (ALI)** — G.E. Weavil, J. Rigdon, S.C.
  Lotspeich — *arXiv stat.AP*, 2026 (digest 06-10). Allostatic-load
  index (ALI) as a whole-person health predictor with missing-data
  patterns handled by pattern-submodel approach. *Watch for:* the
  pattern-submodel handling of structural EHR missingness — small
  but methodologically clean.
- **A causal discovery framework for digital phenotyping** — A.
  Ibrahim — *Scientific Reports*, 2026 (Hripcsak feed, 06-07).
  Causal-discovery applied to behavioral / digital-phenotyping data.
  Off-thread (digital phenotyping is not your area), but causal-
  discovery + EHR is broadly relevant to multimorbidity-trajectory
  work. *Watch for:* whether the discovery algorithm is constraint-
  based (PC) or score-based (NOTEARS-style).
- **Federated SPARQL querying for genomic variant functional
  annotation** — A. Bodrug-Schepers, R. Bourcier, R. Redon, A. Gaignard
  — *arXiv q-bio.QM*, 2026 (digest 06-06). Federated SPARQL across
  biomedical KGs (UniProtKB) for variant annotation in the cerebral-
  aneurysm ICAN project. Off-thread disease but the
  federated-KG-without-data-duplication pattern is worth knowing for
  any KG / variant-evidence pipeline. *Watch for:* how local clinical
  data is kept on-site while public KGs are queried.
- **The bottleneck was never data or algorithms: building a learning
  utility for AI-enabled learning health systems** — J. Bian, M.
  Afshar, C.M. Scifres et al. — *npj Health Systems*, 2026 (Nigam Shah
  + Chute citation feeds). Position piece on learning-health-system
  infrastructure. *Watch for:* the operational pattern they propose
  (utility model vs. one-off project model) — useful framing for
  any institutional learning-health-system work.
- **Polygenic architecture of psychopathology via SVD of 8 psychiatric
  GWAS** — F. Facal, A.M. Pérez-Gutiérrez et al. (Denny feed, 06-11).
  Multivariate SVD on psychiatric GWAS summary statistics. *Watch
  for:* the SVD framing as an alternative to genomic SEM / multivariate
  LDSC — useful methodological reference if you do multi-trait GWAS
  factorization on autoimmune / cardiometabolic disease clusters.

---

## SKIP / noise (logged, no action)

- **Bayesian Inference Framework for Genomically-Anchored Personalized
  Physiological Interpretation** (Dey & Biswas, arXiv 06-12, score 3
  on `causal inference`/`mendelian randomization`/`gwas`). Despite
  high score, this is an architectural proposal piece on personalized
  AI from genomic priors, written in essay-style; not a
  PheWAS/PheRS/causal-epi methods paper. SKIP — the high score is a
  keyword-coincidence rather than topical relevance.
- **Correlation Is Not Enough: Embedding Human Metadata for Individual
  Causal Discovery** (Biswas et al., arXiv 06-09). Same author cluster,
  Large Behavioural Model framing — not on the clinical/EHR thread.
  SKIP.
- **m6A-FORM** (arXiv 06-11) — RNA methylation FM, off the
  clinical/EHR thread. SKIP.
- **Continuous biome representations from Earth observation** (arXiv
  06-11) — non-biomedical. SKIP.
- **scTransformer** (arXiv 06-09) — single-cell methods; off-thread.
- **Spine MRI multi-agent report generation** (arXiv 06-09) — radiology
  FM, off-thread.
- **Flexible Flows for Biological Sequence Design** (arXiv 06-10) —
  generative model for biological sequences; off the clinical/EHR
  thread.
- **AoU "Racial Differences in Psychosocial Outcomes Among Prostate
  Cancer Survivors"** (Wang et al., Cureus, 06-09) — clinical-question
  AoU paper, not on a tracked thread (psychosocial outcomes, not
  pharmacoepi or genetic epi). Borderline SKIP.
- **AoU "Women's experience with gender-based discrimination, social
  support, and health outcomes"** (Oswald et al., 06-11) — clinical
  question, off-thread.
- **AoU "Healthcare Acceptability and Delayed Care Among Older People
  Living with HIV in AoU"** (Lane et al., AIDS and Behavior, 06-13) —
  HIV care-access study; off-thread.
- **"mendelian diseases" keyword alert** continued to surface MR
  papers (Ma et al. on Zuo Gui Wan; Yu et al. on asthma/dental
  caries; Yang et al. on autoimmune × ITP; Li et al. on
  antihypertensives) — all MR, not Mendelian disease. Pattern persists;
  see *Suggestions for the pipeline* below.
- **"knowledge graph" keyword alert** continued to surface
  non-biomedical KG papers (manufacturing, education, construction
  project risks). 4th consecutive window.
- **"drug repurposing" keyword alert** — Cielecka-Piontek/Souto review
  (AI in drug repurposing) is a broad survey not on the
  KG/GNN-explainability angle; Kavousipour et al. on
  redox-ceRNA-network in AUD is target-only without a clinical-evidence
  loop. Both SKIP per INTERESTS filtering.
- **APS-1 sibling alerts** to AIRE penetrance paper (#1 above) are
  consolidated into that report; not double-counted.

---

## Suggestions for the pipeline

Carrying forward and refining from the last two reports:

1. **`arxiv-digest` mostly back, but still under-covers the journal
   stream.** 06-06 onward is producing daily catches, but only ~1/day
   and most are single-keyword score-1 hits. The 80%+ of genuinely
   on-thread papers continue to come from journals (Nature Med, JCI,
   AJHG, Clin Cancer Res, Nat Comms, HMG, Lancet) outside arXiv
   q-bio/stat. **Recommendation (3rd report running):** add `cs.LG`,
   `stat.ME`, and a medRxiv/bioRxiv source. medRxiv alone would catch
   #16 (Gobeil proteogenomic MASLD), #13 (Chen agentic OMOP), and
   #21 (Pham LDSC failure modes) from this window.
2. **`mendelian diseases` keyword still leaks MR papers** — 4
   instances in 8 days. Either replace with `OMIM` / `MIM` IDs, or
   exclude `-randomization`.
3. **`knowledge graph` keyword: same as before**, 4 consecutive
   windows of non-biomedical hits. Recommend `biomedical knowledge
   graph` OR `clinical knowledge graph` OR `(knowledge graph)
   (medical OR biomedical OR clinical OR EHR OR phenotype)`.
4. **Add `proteome-wide` / `colocalization`** — fifth proteome-MR
   triangulation paper in three reports (Gobeil et al. this window).
5. **Add `OMOP` as a standalone keyword** — agentic OMOP
   concept-set authoring (#13 this report) and the prior OHDSI-data-
   quality work would surface more reliably with a dedicated keyword
   than relying on EHR keyword recall.
6. **Add `reflex RNA` or `RNA evidence`** as a keyword for the
   splicing-VUS-resolution angle (#9 this report is the second instance
   of this shape).
7. **Consider an `agentic` + `LLM` co-occurrence keyword for the
   clinical / variant / phenotype space** — five distinct
   LLM-assisted-phenotyping / agentic items this window (MARRVEL-MCP,
   Agentic Authoring OMOP, MedADL, Genosolver, VarLitAgent). This
   cluster is clearly a sub-thread on its own.
8. **Self-citation hits** (Yang/Schaffer/Tran/Zeng/Park AoU prostate
   abstract last report; Hassan et al. doublet vs triplet prostate
   cancer this report, Chenjie Zeng feed) — keeping as-is unless they
   get noisier, since they double as a citation-audit signal.
