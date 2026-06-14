# Research digest report — 2026-06-04

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP/IBD disease threads, EHR
foundation models, KGs/ontologies, drug repurposing, rare disease, ML for
precision health, multimorbidity).

Window: **2026-06-02 → 2026-06-04** (since the prior 2026-06-01 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-02 → 06-04 | Two batches today: 06-03 19:07 UTC (author + citation alerts) and 06-04 08:37 UTC (keyword alerts). |
| `arxiv-digest` repo (`digests/`) | 2026-06-02 → 06-03 | **Empty.** 06-02 = 0 relevant; 06-03 = 0 relevant with 3/4 categories failing to fetch (q-bio.QM, q-bio.GN, q-bio.PE). Pipeline remains silent. |
| bioRxiv / medRxiv subject alerts | daily | Aggregate collection digests, not individually triaged. |
| Raw arXiv daily mailings (`no-reply@arxiv.org`) | daily | Unfiltered cs/q-bio/stat to a list address; not triaged here. |

> ⚠️ The `arxiv-digest` GitHub pipeline produced **zero signal** this window
> for the third consecutive cycle. q-bio fetches are intermittently
> 429-ing; the 2026-06-03 run logged "3/4 categories failed to fetch."
> Recommendation (repeated from the 2026-06-01 report): inspect the arXiv
> client backoff in `scripts/arxiv_digest.py` or extend lookback to 168 h
> for a manual catch-up run.

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **UK Biobank dominates the keyword feed this cycle** (≥9 distinct UKB
  papers in a single Scholar alert). The standout is a cardiovascular-
  liver-metabolic *multimorbidity* paper (He et al., *Cardiovascular
  Diabetology*) — squarely on your multimorbidity thread. A UKB
  pharmacogenetic loop-diuretics study (UMOD genotype × heart failure
  outcomes) is also live methodology for your pharmacoepi thread.
- **All of Us**: thinner this cycle than the 2026-06-01 window, but two
  notable hits — a *npj Digital Medicine* paper on generative semantic
  auditing of EHRs using AoU v7 controlled tier, and an NYU Langone
  precision-medicine registry paper that benchmarks against AoU/UKB
  design.
- **Pharmacoepidemiology / GLP-1 + SGLT2**: a clinical-practice review on
  SGLT2is + GLP-1 RAs in T2D + CKD surfaced via the **Patrick Ryan**
  author feed (Handelsman et al.). Not a methods paper, but useful
  reference background for the drug-class thread.
- **CHIP**: one mechanistic paper — Weyrich et al. on independent dose-
  dependent contributions of CHIP and mosaic loss of Y (mLoY) to incident
  heart failure (*Eur J Heart Failure*). Pairs with the 2026-06-01 mtDNA
  *Nature* paper on age-related somatic mosaicism.
- **Drug repurposing**: a *Nature Reviews Cancer* review on **mutation-
  centric kinase drug repurposing for rare cancers** (Chan, Subbiah,
  Gujral). High-quality reference for the drug-repurposing thread —
  variant-level pharmacological mapping is exactly the
  "explainable-rationale" framing you flagged as priority.
- **PheWAS**: a Taiwanese early-onset ischemic stroke GWAS+PheWAS
  (Wang et al., *Neurology*) using the TPMI PheWeb across 695 ICD-based
  phenotypes. A trans-ancestry example of the PheWAS scan you do; useful
  comparator for cross-ancestry portability work.
- **Mendelian Randomization**: an IL-6R × Lp(a) interaction MR paper
  (Kheirkhah et al., *JACC: Basic to Translational*) via the **Joshua
  Denny** author feed — interesting because it does *interaction* MR, not
  marginal MR.

Counts (this window): **6 HIGH**, **3 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. Mutation-centric kinase drug repurposing for rare cancers
- **Authors / venue:** M. Chan, H. Ma, V. Subbiah, T.S. Gujral — *Nature
  Reviews Cancer*, 2026.
- **Surfaced by:** `"drug repurposing"` keyword alert (06-04).
- **Thread:** Drug repurposing (high-priority sub-thread:
  explainable-rationale, variant-level pharmacology).
- **What it is:** A Nature Reviews piece proposing systematic, variant-
  level pharmacological mapping of oncogenic kinase variants as the
  organizing principle for rare-cancer drug repurposing. Argues that many
  rare-cancer oncogenic variants lack matched therapies despite a large
  arsenal of approved kinase inhibitors, and that variant-level
  drug-activity tables can close the gap.
- **Why it matters to you:** Maps directly onto your *high-priority*
  drug-repurposing angle — "explainable hypothesis output, path or
  subgraph rationales rather than opaque link-prediction scores." A
  variant→drug mapping is exactly the kind of rationale you favor over
  black-box link prediction. Also adjacent to your rare-disease thread
  (here rare *cancer*, but the framing transfers to rare-variant
  disease).
- **Action:** **HIGH** — read in full. Particularly: how do they handle
  *evidence tiers* (Subbiah is the Tier-evidence person from OncoKB-
  adjacent work)? Does the framework propose any HPO-style phenotype-
  matching for rare-cancer indications? Both questions feed your
  rare-disease + KG/repurposing intersection.

### 2. Associations of the atherogenic index of plasma and its modified indices with the incidence and progression of cardiovascular-liver-metabolic multimorbidity: a prospective cohort study from UK Biobank
- **Authors / venue:** Q. He, M. Sun, J. Yao, Y. Wang, Y. Shen —
  *Cardiovascular Diabetology*, 2026.
- **Surfaced by:** `"UK Biobank"` keyword alert (06-04).
- **Thread:** Chronic disease clustering and multimorbidity (cardio-
  metabolic) **+** EHR-linked biobanks (UKB).
- **What it is:** UKB prospective cohort study linking the atherogenic
  index of plasma (AIP) and its modified variants to incident and
  *progressive* cardiovascular-liver-metabolic (CLM) multimorbidity. The
  multimorbidity outcome — joint CV + hepatic + metabolic states — is
  exactly the kind of cardiometabolic cluster your multimorbidity thread
  is interested in.
- **Why it matters to you:** Three reasons. (i) It uses a UKB
  *trajectory/progression* outcome, not just incident events, which is
  closer to the disease-trajectory clustering you want. (ii) AIP and its
  variants are simple lipid-derived biomarkers — useful as comparators or
  features in any composite risk model. (iii) The CLM construct is a
  ready-made multimorbidity outcome definition you can borrow.
- **Action:** **HIGH** — read for the CLM phenotype operationalization
  (which ICD/phecode codes? what's the temporal anchor for "progression"?)
  and for the modeling approach (sequential / multi-state hazard or just
  baseline-AIP → incident-CLM Cox?).

### 3. Independent and dose-dependent contributions of clonal hematopoiesis and mosaic loss of Y to incident heart failure
- **Authors / venue:** M. Weyrich, A. Ware, J. Windschmitt, T. Sarakpi et
  al. — *European Journal of Heart Failure*, 2026.
- **Surfaced by:** `intitle:"clonal hematopoiesis"` keyword alert (06-04).
- **Thread:** Clonal hematopoiesis (CHIP) disease thread **+** somatic
  mosaicism (mLoY).
- **What it is:** Co-analysis of CHIP variant allele fraction (VAF) and
  mosaic loss of chromosome Y (mLoY) as *independent* and *dose-dependent*
  predictors of incident heart failure. The "dose-dependent" framing
  implies they treat both CHIP-VAF and mLoY-cell-fraction as continuous
  exposures rather than binary, which is methodologically cleaner.
- **Why it matters to you:** Directly extends the CHIP→CV-outcome
  literature into HF (not just stroke or all-cause CV mortality), and
  treats mLoY as a parallel somatic-mosaicism exposure rather than a
  nuisance. This is the same modeling pattern that would apply to
  composite somatic-mosaicism risk scores combining CHIP + mLoY + mLoX +
  mtDNA mosaicism. Complements the 2026-06-01 *Nature* mtDNA paper.
- **Action:** **HIGH** — read for the joint modeling (mutually adjusted
  Cox? competing-risks?) and for whether they report an additive vs.
  multiplicative interaction between CHIP-VAF and mLoY.

### 4. Identification of novel genetic risk variants associated with early-onset ischemic stroke in Taiwan
- **Authors / venue:** Y.C. Wang, K.M. Liu, Y.L. Gan, N.F. Chi, L.S. Lu,
  C.Y. Chou et al. — *Neurology*, 2026.
- **Surfaced by:** `"phenome wide association studies"` keyword alert
  (06-04).
- **Thread:** PheWAS / phecode infrastructure **+** Genetic epidemiology
  (trans-ancestry portability).
- **What it is:** Early-onset ischemic stroke GWAS in Taiwan, with
  PheWAS follow-up using the **TPMI PheWeb** across 695 ICD-based disease
  phenotypes plus 24 quantitative traits. A clean GWAS → PheWAS pipeline
  on a non-European cohort.
- **Why it matters to you:** Two angles. (i) **Trans-ancestry portability**:
  the TPMI PheWeb is an East Asian PheWAS resource — a useful comparator
  for any UKB/AoU PheWAS scan you've done, especially for ischemic-stroke
  PRS portability. (ii) **ICD→phecode-style phenotyping** at PheWAS scale
  in a non-MVP/AoU/UKB cohort — i.e., the same phecode-style infrastructure
  exported to TPMI. Worth knowing as a third major PheWeb-style resource
  alongside MVP and UKB.
- **Action:** **HIGH** — skim for the TPMI PheWeb's ICD→phecode mapping
  conventions (do they reuse the Denny / Bastarache phecode map, or have
  Taiwan-specific extensions?). If TPMI maps to standard phecodes, it's a
  high-value cross-ancestry replication target for your PheRS work.

### 5. A generative approach for semantic auditing of electronic health records
- **Authors / venue:** I. Girshovitz, A. Ambus, M. Shahar, R.
  Gilad-Bachrach — *npj Digital Medicine*, 2026.
- **Surfaced by:** `"All of Us research program"` keyword alert (06-04).
- **Thread:** EHR phenotyping & OMOP **+** EHR-linked biobanks (AoU) **+**
  EHR foundation models (generative).
- **What it is:** A generative-model approach to **semantic auditing** of
  EHR data — using AoU v7 controlled-tier as the test bed. The framing is
  not phenotype validation but rather *semantic* consistency checking
  (e.g., does this combination of codes/measurements/medications make
  clinical sense?). The snippet calls AoU "a large-scale US biobank,"
  confirming the cohort.
- **Why it matters to you:** Sits at the intersection of three threads —
  AoU as the cohort, EHR-phenotyping data quality (different from Kahn-
  framework structural DQ; this is *semantic* / clinical-plausibility DQ),
  and the EHR-foundation-model lineage (generative). Could pair with the
  Spotnitz IBD data-quality paper from the prior report.
- **Action:** **HIGH** — read for the generative architecture (LLM?
  autoencoder?) and whether the audit produces patient-level outlier
  scores that you could use as a phenotype-confidence filter in your own
  AoU phecode work.

### 6. Defining the roles of SGLT2 inhibitors and GLP-1 receptor agonists in the management of chronic kidney disease in adults with type 2 diabetes with or without [cardiovascular disease]
- **Authors / venue:** Y. Handelsman, A.Y.Y. Cheng, G.P. Fadini et al. —
  clinical-practice / consensus review, 2026.
- **Surfaced by:** **Patrick Ryan "new related research"** author alert
  (06-03).
- **Thread:** Causal inference & pharmacoepidemiology (GLP-1 RA + SGLT2i
  drug classes).
- **What it is:** A clinical-practice review/consensus on SGLT2i and
  GLP-1 RA in T2D + CKD, with and without comorbid CVD. Not a methods
  paper; a reference synthesis.
- **Why it matters to you:** It's a review, not a primary study, so the
  weight is lower than primary pharmacoepi RWE — but it lands in *Patrick
  Ryan*'s feed, which means OHDSI-side researchers are tracking it, and
  it codifies the clinical-decision frame against which any
  target-trial-emulation of these two drug classes is going to be judged.
  Useful background for any AoU/UKB TTE you do on SGLT2 or GLP-1.
- **Action:** **HIGH (skim only)** — bookmark as reference; not a
  read-front-to-back. Pull the recommendation-level statements for the
  CKD + T2D ± CVD strata and use as the comparator-arm specification when
  designing a TTE.

---

## METHODS-WATCH (off-thread disease, exemplary method)

### M1. Mendelian Randomization reveals Interleukin-6 Receptor – Lipoprotein(a) interplay with independent cardiovascular risk reductions
- **Authors / venue:** A. Kheirkhah, S. Di Maio, S. Coassin, S.
  Schönherr et al. — *JACC: Basic to Translational Science*, 2026.
- **Surfaced by:** **Joshua C. Denny "new related research"** alert
  (06-03).
- **Why method-watch:** This is *interaction* MR — IL-6R × Lp(a) — not
  the standard marginal-effect MR most pharmacoepi MR papers do. If you
  want to extend your phenome-wide MR / biomarker-as-exposure scans into
  interaction terms (e.g., does drug A's predicted MR effect depend on
  background level of biomarker B?), this is the template paper.

### M2. Impact of UMOD genotype on clinical outcomes among patients with heart failure initiating loop diuretics: a UK Biobank pharmacogenetic cohort study
- **Authors / venue:** R. Kreutz, P. Gebert, J. Luo, P. Tassopoulou, J.
  Bolbrinker et al. — *Journal of Hypertension*, 2026.
- **Why method-watch:** Pharmacogenetic *new-user* cohort design in UKB
  linked to primary care + hospital + vital status records — a clean
  template for genotype-stratified drug-outcome studies that don't
  involve any of your tracked drug classes but use exactly the data
  layers (UKB linked primary care + HES + ONS) you'd use for a Trikafta
  or HRT analysis if you moved them to UKB.

### M3. Distinct genetic architecture in the tails of complex traits *(carryover from 2026-06-01)*
- Still showing citation echoes this cycle (10-new-citations alerts for
  Denny, Pritchard, Karczewski). Flagging only that the saturation
  signal persists — if you haven't read it yet, it remains the highest-
  impact paper of the prior cycle.

---

## arxiv-digest GitHub repo — status

| Date | Relevant | Notes |
| --- | --- | --- |
| 2026-06-02 | 0 | Clean fetch, no matches |
| 2026-06-03 | 0 | **3/4 categories failed to fetch** (q-bio.QM, q-bio.GN, q-bio.PE) — only stat.AP succeeded |

The repo has now produced three consecutive empty digests (05-31, 06-02,
06-03), and two of those three had explicit fetch failures. The pipeline
is not surfacing q-bio submissions reliably. Possible causes worth a
diagnostic run:

1. **arXiv rate limiting**: scripts use 5 s client delay + 2 retries;
   when q-bio 429s on the first try, the immediate retry probably also
   429s. Consider exponential backoff (e.g., 10 s → 30 s → 90 s) instead
   of fixed 5 s.
2. **Lookback exhaustion**: with 30 h lookback and weekend gaps, real
   q-bio submission volume is sometimes legitimately low. Try a manual
   168 h backfill via the Actions tab to confirm whether the issue is
   *fetch failure* or *legitimate zero matches*.
3. **Keyword drift**: less likely on a 3-day window, but worth checking
   that `config/tracked.yaml` still matches the active threads — the
   drug-repurposing thread added 2026-04-30 may need additional keywords
   (e.g., "kinase repurposing", "variant-level pharmacology") to catch
   review-format pieces like the Chan/Subbiah/Gujral paper above.

---

## Lower-priority signals (logged, not detailed)

- **UKB cardiometabolic comorbid signal cluster** — five additional UKB
  papers in the keyword feed on dietary antioxidant index × IBS, EASO
  obesity framework morbidity stratification, metabolic-syndrome ×
  depression × proteomics × neuroimaging, chronic-pain × AF risk, and a
  CYP2A6 → COPD/lung-cancer mediated MR. All UKB-based; most are
  exposure-driven epidemiology rather than methods. Skim if any overlap
  with your specific disease threads.
- **Foundation models for EHR + omics** — Sood, "Multi-Modal Foundation
  Models for Integrating Immune Gene Variation, Transcriptomics, and
  Clinical Phenotypes in Precision Medicine" (*Bioinformatics Insights
  and Analytics*). Venue is unfamiliar; treat as low signal until full
  text reviewed.
- **Knowledge graphs (off-domain)** — diffusion-model-based rule
  generation for KG reasoning (Cheng et al., arXiv). Not biomedical;
  lower interest per `INTERESTS.md`.
- **Chenjie Zeng new-related-research feed** — taxane-induced peripheral
  neuropathy in Black women with breast cancer (Ballinger, ECOG-ACRIN).
  Coauthor-network hit; lower priority for the active threads here.
- **Lisa Bastarache new-related-research** — plant photosynthetic
  genomic-prediction paper. Off-domain noise from the author alert; skip.
- **Konrad Karczewski new-related-research** — UKB knee-pain GWAS in
  ~440k participants. Standard UKB GWAS; not a tracked outcome.
- **Jonathan Pritchard new citations** — single-cell PLXND1 MASLD
  analysis (Ma et al., *Metabolites*). Off-thread.

---

## Action checklist

1. **Read in full:** items #1 (NRC drug-repurposing review), #2 (UKB CLM
   multimorbidity), #3 (Weyrich CHIP + mLoY → HF), #5 (npj DM semantic
   auditing).
2. **Skim:** #4 (Taiwan stroke PheWAS) and #6 (SGLT2/GLP-1 review).
3. **Investigate pipeline:** run a manual 168 h `arxiv-digest` backfill
   and check whether q-bio fetch failures are persistent or transient.
4. **Optional config tweak:** consider adding kinase- and
   variant-level-pharmacology terms to `config/tracked.yaml` to catch
   reviews like #1 if the pipeline were healthy.
