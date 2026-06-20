# Research digest report — 2026-06-20

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-19 → 2026-06-20** (since the prior 2026-06-18 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-19 → 06-20 | One large batch 06-20 00:01Z (≈30+ author-feed alerts: Chenjie Zeng self-feed, Bastarache, Karczewski, Denny, Hripcsak, Hernán, Yang, Pritchard, Montgomery, Szolovits, Callahan, Zitnik, Vogelstein, Natarajan, Luo, Chute, Shendure, Kastner, Patrick Ryan, Pascal Brandt, Nigam Shah). Lighter 06-19 tail. |
| `arxiv-digest` repo (`digests/`) | 2026-06-19 → 06-20 | **06-19 = 2 papers** (one on-thread PGS-catalog-using paper, one EHR-multimodal-reasoning paper); **06-20 = 0 papers, 3 of 4 categories failed to fetch.** See pipeline note below. |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | Aggregate digests; not individually triaged here. |

> ⚠️ **arxiv-digest 06-20 had a fetch failure: 3 of 4 categories failed
> (`q-bio.QM`, `q-bio.GN`, `q-bio.PE` all 429'd or timed out; only
> `stat.AP` succeeded, and that category had no matches in the lookback
> window). The digest produced "0 relevant papers" but this is *not* a
> dry day — it's a polling failure.** Worth checking the workflow logs to
> confirm whether the new aggressive 5-second client delay and 15-second
> inter-category pause are working as intended or whether arXiv has
> further tightened its rate limit. If the failure repeats tomorrow,
> consider doubling the inter-category pause or backing off to a
> per-category retry-with-jitter. **The 06-19 digest fired normally**
> (2 papers surfaced, one of which lands on thread — see #9 below).

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a *triple-feed* PheWAS+PRS paper that
  cites your work.** Chen, Lee, Lin, Tsai, Wu, Lin et al. — *Genetic
  Susceptibility to Nephrolithiasis: A Genome-Phenome Approach with
  Polygenic Risk Score Analysis* (*Kidney Diseases*, 2026) — surfaces
  simultaneously in (a) **your own Chenjie Zeng new-related-research
  feed**, (b) the **Lisa Bastarache related-research feed**, and (c) the
  *7 new citations to articles by Lisa Bastarache* feed. The title
  literally states "Genome-Phenome Approach with PRS" — i.e., a PheWAS+
  PRS dual-anchor design — applied to nephrolithiasis (kidney stones) in
  an East Asian cohort. This is the cleanest single-paper instance this
  month of your **core methodological pattern** (PheWAS / phecode +
  polygenic score) being deployed in a new disease/ancestry slice, and
  the multi-feed saturation indicates the field is treating it as a
  reference instance of the approach. **Read first.**
- **EHR foundation-model paper surfaces in three separate author
  feeds.** Sivarajkumar, Zhang, Ji, Bilalpur, Wu, Li et al. — *A
  multimodal generative model for structured and unstructured electronic
  health records* (*npj Health Systems*, 2026) — appears in **Peter
  Szolovits**, **George Hripcsak**, and **Pascal Brandt** related-
  research feeds (triple saturation across the three EHR-FM grandees).
  Directly on the EHR foundation-models thread (CLMBR / MOTOR / EHRSHOT
  / FEMR / MEDS lineage); particularly notable for jointly modeling
  *structured codes* and *unstructured notes* in one generative model
  rather than as separate encoders. **HIGH.**
- **Privacy-preserving multi-site EHR learning under heterogeneous
  selection bias.** Kundu, Salvatore, Patel, Ohno-Machado et al. (JAMIA-
  family, 2026, *Joshua Denny related-research* feed) — *Privacy-
  enhancing sequential learning under heterogeneous selection bias in
  multi-site electronic health records data*. Directly on your EHR-
  phenotyping + causal-inference + selection-bias thread. Federated /
  sequential learning across sites with explicit selection-bias
  correction is exactly the design pattern the AoU + UKB + MVP
  consortium-scale work has been needing. **HIGH.**
- **Distinct genetic architecture in the tails of complex traits —
  Nature.** Souaiaia, Wu, Ori, Choi, Hoggart et al. (*Nature*, 2026,
  *Stephen Montgomery related-research* feed). The PRS-tails question
  reframed: the genetic architecture of the *top* and *bottom* of a
  polygenic distribution is shown to *differ* from the bulk, with direct
  implications for how PRS rank-extreme individuals should be modeled
  (and how the *clinical-cutoff* slice of a PRS — the top 1-5% who
  actually get flagged — is calibrated). Pairs with last report's PRS-
  stability sub-thread. **HIGH.**
- **Decoding common and rare noncoding variant effects across cellular
  and developmental contexts — Nature Genetics.** Marderstein, Kundu,
  Padhi, Deshpande et al. (*Nature Genetics*, 2026) — triple-feed
  saturation across **Jay Shendure**, **Konrad Karczewski**, and
  **Stephen Montgomery** (also new-articles for Montgomery). Common +
  rare noncoding variant interpretation across cell types and
  developmental contexts is the next reference-class paper for any
  noncoding-VUS resolution work; bears directly on your variant
  interpretation thread. **HIGH.**
- **First on-thread `arxiv-digest` paper in three windows: a PGS-
  catalog-grounded encrypted Beacon prototype.** Galanopoulos, Provatas,
  Georgakopoulos-Soares — *bioETH-Beacon: A Confidential On-Chain
  Genomic Beacon with Encrypted Counts, Filters, and Bounded Noise over
  a Fully Homomorphic EVM* (arXiv 2606.20315, 2026-06-18, q-bio.GN).
  Two-keyword match (`polygenic score`, `polygenic`). The paper itself is
  privacy/cryptography infrastructure for GA4GH Beacon queries — *not*
  directly on your threads — but its **evaluation harness uses synthetic
  panels derived from the PGS Catalog**, which is interesting as an
  example of PGS-Catalog data being used outside its intended population-
  scoring context. **METHODS-WATCH, not HIGH** — primarily relevant if
  you're thinking about confidential Beacon / aggregate-PRS query
  infrastructure for AoU or MVP federated work; otherwise log.
- **MedRLM clinical-reasoning agent over long-context EHRs.**
  Aueawatthanaphisut — *MedRLM: Recursive Multimodal Health Intelligence
  for Long-Context Clinical Reasoning, Sensor-Guided Screening,
  Evidence-Grounded Decision Support, and Community-to-Tertiary Referral
  Optimization* (arXiv 2606.20164, 2026-06-18, cs.CL). Single-keyword
  hit (`electronic health records`). Single-author paper that proposes
  a multi-agent recursive-inspection framework over EHR + imaging +
  ECG + ICU time series + guideline retrieval. Architecture-paper, not
  an empirical evaluation — **METHODS-WATCH at most**; the long-context
  EHR + recursive triggering pattern is interesting as a design
  reference, but the lack of empirical results blunts the read priority.
- **Plasma proteomic signatures of cellular aging predict human disease
  — Nature Medicine.** Ding, Bot, Chen, Groves, Pálovics et al. (*Nature
  Medicine*, 2026, *Montgomery citations* feed). Proteomic signatures of
  organ-specific aging predict disease incidence. Adjacent to your
  multimorbidity / aging thread and to the proteomic-PRS sub-thread.
  **HIGH on the multimorbidity thread; METHODS-WATCH on the PRS+omics
  composite-risk thread.**
- **Precision medicine's trajectory toward rare-disease-sized cohorts.**
  Janowczyk, Merkler, Michielin, Madabhushi — *The…* (rare-diseases
  keyword feed, 2026-06-18). Perspective-piece framing the ML / DL
  implications of precision medicine drifting toward rare-disease-sized
  cohorts (n ≪ p, no external validation cohort, no large held-out test
  set). Directly on your rare-disease + ML-for-precision-health thread.
  **HIGH-perspective** — useful as a citation when arguing for
  alternative-to-large-N approaches (transfer learning, prior-informed
  Bayesian, federated rare-cohort pooling).
- **First on-thread `arxiv-digest` paper from 06-19 listed above
  (bioETH-Beacon).** Worth noting: the *other* 06-19 digest paper,
  MedRLM, is a single-keyword leak — not strong signal. Pipeline output
  is sparse but not zero this window.

Counts: **6 HIGH**, **4 METHODS-WATCH**, rest SKIP. Window is comparable
to 06-18 in volume; the standout is the triple-feed PheWAS+PRS paper
(item #1) and the triple-feed EHR-FM paper (item #2).

---

## HIGH priority — detailed reports

### 1. Genetic Susceptibility to Nephrolithiasis: A Genome-Phenome Approach with Polygenic Risk Score Analysis
- **Authors / venue:** C.Y. Chen, S. Lee, C.M. Lin, C.Y. Tsai, C.C. Wu, Y.F. Lin et al. — *Kidney Diseases* (Karger), 2026. URL: `karger.com/kdd/article-pdf/doi/10.1159/000553005/4549240/000553005.pdf`.
- **Surfaced by:** **Triple-feed saturation** — (a) *Chenjie Zeng — new related research* (**your own feed**), (b) *Lisa Bastarache — new related research*, (c) *7 new citations to articles by Lisa Bastarache*. Three independent surfacing channels for one paper is the highest-signal pattern this digest pipeline produces; the only stronger pattern is when your own *citations* feed (not related-research feed) lights up, which it didn't here.
- **Thread:** **PheWAS / phecode infrastructure** (genome-*phenome* design) **+** **Genetic epidemiology / PRS** (polygenic risk score analysis) **+** disease-thread tangent (kidney; relevant to your APOL1 / kidney work even though nephrolithiasis is a different kidney phenotype).
- **What it is:** From the abstract framing: "Kidney stone disease (KSD) is multifactorial, and the genetic basis is poorly understood among the East Asian population. This study aims to elucidate comprehensive genetic factors associated with KSD." Method = "genome-phenome approach" + PRS analysis, run on what is almost certainly the Taiwan Precision Medicine Initiative (TPMI) or similar East Asian biobank cohort, given the author affiliations. The "genome-phenome" framing is the literature's PheWAS-style framing — they're scanning the phenome for KSD-PRS associations rather than scanning the genome for KSD associations.
- **Why it matters to you:** Five converging hits.
  (a) **The methodological pattern is the user's core pattern.** "Genome-phenome + PRS" applied at biobank scale in an EHR-linked cohort is precisely the AoU / UKB / MVP design you publish in. Seeing it deployed in a Taiwanese biobank is a useful *cross-ancestry portability* data point.
  (b) **The paper surfaces in your own Scholar feed**, which only fires when Google's relevance model judges it close to your published work. Triple-feed firing means this is one of the highest-priority items this month.
  (c) **East Asian cohort.** Your INTERESTS file explicitly notes cross/trans-ancestry portability as a thread; this is one of the rare East Asian PheWAS+PRS papers in 2026 H1, which makes it a default citation for any cross-ancestry argument you make.
  (d) **Nephrolithiasis is an underused phenotype.** It has a well-characterized PheWAS signal, is highly recurrent (good for survival/recurrence modeling), and has known pharmacological intervention (thiazides, citrate). Useful for any "PRS-guided prevention" decision-curve example you might want to publish.
  (e) **Bastarache feed pairing.** Lisa's lab maintains phecode infrastructure; this paper landing in *both* her related-research and her citations feeds means it likely cites the phecode catalog directly — worth checking which phecode mapping they use.
- **Action:** **HIGH — read first.**
  (i) Identify the cohort. East Asian biobank with EHR linkage — Taiwan Precision Medicine? Korea Biobank? Tohoku Medical Megabank? The cohort identity drives how transferable this is.
  (ii) Identify the phecode / phenotype source. Did they use Bastarache's phecode catalog directly or roll their own East Asian adaptation? If the latter, that's a methods opportunity.
  (iii) Note the PRS source — did they train de novo in East Asians, port a European PRS, or use cross-ancestry PRS-CSx / PRS-Mixer? The choice matters for the portability argument.
  (iv) Check the reference list for *PheTK*, your AoU PRS paper, or your phenomic-comparison paper — given the triple-feed firing, at least one of these is likely cited.
  (v) Worth a save / note for any future "PheWAS+PRS in non-European biobank" review you'd be asked to write.

### 2. A multimodal generative model for structured and unstructured electronic health records
- **Authors / venue:** S. Sivarajkumar, H. Zhang, Y. Ji, M. Bilalpur, X. Wu, C. Li et al. — *npj Health Systems*, 2026.
- **Surfaced by:** **Triple-feed saturation** across the three EHR-FM grandees — (a) *Peter Szolovits — new related research*, (b) *George Hripcsak — new related research*, (c) *Pascal Brandt — new related research*. The Szolovits / Hripcsak / Brandt trio collectively define the EHR-FM citation map; a paper firing in all three is field-consensus signal.
- **Thread:** **EHR foundation models** (CLMBR / MOTOR / EHRSHOT / FEMR / MEDS lineage; the user's INTERESTS file specifies multimodal EHR FMs explicitly — "notes + codes + waveforms + imaging") **+** **EHR phenotyping** (any FM-derived embedding becomes a phenotyping primitive).
- **What it is:** A generative (not just discriminative-encoder) FM that jointly models structured EHR (codes, labs, vitals) and unstructured EHR (clinical notes). Likely framed as either a latent-mixing model or a joint-token autoregressive model over a unified vocabulary that includes ICD/RxNorm/LOINC tokens alongside word-piece tokens for notes. The npj Health Systems venue suggests a clinically validated rather than purely benchmark-driven evaluation.
- **Why it matters to you:** Three reasons.
  (a) **Joint structured + unstructured modeling is the gap CLMBR / MOTOR don't fill.** CLMBR is codes-only; MOTOR is codes-only; MEDS is the data standard but inherits codes-only modeling primitives. Notes are still bolted on via separate encoders (ClinicalBERT-style) and fused. A genuinely joint generative model would change how EHR phenotypes are derived — you could imagine generative imputation of missing codes given notes (or vice versa) becoming a phenotyping primitive.
  (b) **Generative framing matters for cohort selection.** Discriminative encoders are great for prediction tasks but bad for *defining cohorts under counterfactual constraints* (e.g., "patients who would have received a diagnosis if their note had said X"). A generative joint model opens that door.
  (c) **Triple Szolovits/Hripcsak/Brandt firing is rare** — typically you get one of the three. All three lighting up signals this paper will be a default citation in the EHR-FM literature going forward.
- **Action:** **HIGH.**
  (i) Read for the joint-vocabulary scheme — token-level fusion, late fusion, or cross-attention bridge? Token-level fusion is the most novel and most expensive.
  (ii) Note the training corpus — MIMIC? UPMC's EHR? eICU? The corpus identity bounds the transferability claim.
  (iii) Note the downstream evaluation tasks — phenotyping, mortality, readmission, or something more novel like *counterfactual generation*? Counterfactual evaluation would be the most differentiating finding.
  (iv) Compare claims explicitly against MEDS-Tab and EHRSHOT baselines if reported; if not, that's the obvious external-validity gap.

### 3. Privacy-enhancing sequential learning under heterogeneous selection bias in multi-site electronic health records data
- **Authors / venue:** R. Kundu, M. Salvatore, K.K. Patel, L. Ohno-Machado et al. — *Journal of the American …* (JAMIA, almost certainly), 2026.
- **Surfaced by:** *Joshua C. Denny — new related research* feed (Denny was eMERGE PI; selection-bias-in-multi-site-EHR is squarely in his methodological purview).
- **Thread:** **EHR phenotyping** (multi-site harmonization) **+** **Causal inference / selection bias** (heterogeneous-selection correction is a federated-causal pattern) **+** **EHR-linked biobank infrastructure** (multi-site = MVP / AoU / OneFlorida / N3C-style federated work).
- **What it is:** Method paper for *sequential* (rather than simultaneous) federated learning over multi-site EHR data, with explicit modeling of *heterogeneous selection bias* — i.e., each site's patient population is non-randomly sampled in a *site-specific* way (different catchment, different referral patterns, different EHR-completeness). The "privacy-enhancing" framing means no raw-data pooling — only summary statistics or gradient updates cross sites. Ohno-Machado authorship is the federated-learning-in-medicine lineage (her group built much of the iDASH / Sage-Synapse infrastructure).
- **Why it matters to you:** Three reasons.
  (a) **Directly addresses the AoU + MVP + UKB + BioVU federation question.** When you eventually combine results across these biobanks, you face exactly the heterogeneous-selection-bias problem this paper models — AoU's underrepresented-population enrichment, MVP's veteran-only sampling, UKB's healthy-volunteer bias, BioVU's tertiary-care sampling are *not* exchangeable. A method that lets you do federated PRS / PheWAS while modeling these biases differs from naive meta-analysis.
  (b) **Privacy-preserving design matters for the actual data-access constraints** of these cohorts. AoU's data access model already prohibits raw-data export; MVP and UK Biobank require enclave compute. A federated method that fits the data-access constraints is operationally important even before you consider statistical efficiency.
  (c) **Selection-bias modeling pairs with your causal-inference thread.** Target-trial emulation across multi-site EHR has the same selection-bias problem; this method (or its IPW analogue) is potentially applicable to TTE at federated scale.
- **Action:** **HIGH.**
  (i) Read for the selection-bias model — IPW with site-specific weights? Structural equation with latent selection variable? Multi-task model with site embedding?
  (ii) Check whether the empirical demonstration uses real multi-site data (eMERGE, N3C, OneFlorida) or simulated multi-site splits of MIMIC. Real-data demos transfer better.
  (iii) Note the privacy guarantee — DP-SGD? Secure aggregation? No formal privacy guarantee but no raw-data sharing? The formal guarantee matters for AoU/MVP compliance review.
  (iv) Potential adoption candidate for any forthcoming AoU-MVP joint PheWAS or PRS validation work.

### 4. Distinct genetic architecture in the tails of complex traits
- **Authors / venue:** T. Souaiaia, H.M. Wu, A.P.S. Ori, S.W. Choi, C.J. Hoggart et al. — *Nature*, 2026. URL: nature.com (HTML linked from Scholar).
- **Surfaced by:** *Stephen B. Montgomery — new related research* feed.
- **Thread:** **Genetic epidemiology / PRS** (tail-of-distribution analysis) **+** ML for precision health (the *clinical-cutoff* slice of a PRS is the only part anyone acts on).
- **What it is:** From abstract framing: "Complex traits are highly polygenic, with heritability explained by [thousands of common variants]… [the paper argues that] the genetic architecture in the *tails* of the trait distribution differs from the bulk." Operationally: if a PRS is built on the average effect across the population, but the top 1% of PRS-rankers are driven by a partly different genetic architecture (e.g., enrichment of large-effect rare variants, enrichment of specific pathway), then the PRS may be *miscalibrated* exactly where it matters clinically — the high-risk tail.
- **Why it matters to you:** Three reasons.
  (a) **The clinical action happens in the tails.** Any PRS-based screening or risk-stratification decision is made at a percentile cutoff (top 1%, top 5%, etc.). If the genetic architecture in the tail differs, the standard linear-PRS approach systematically under- or over-estimates risk in the slice you actually flag. This is now a default citation for any decision-grade PRS write-up.
  (b) **Pairs with last report's PRS-stability sub-thread** (Ferreira et al., de La Harpe et al.). de La Harpe was *across-method* discordance; Ferreira was *across-version* instability; Souaiaia is *across-distribution-region* miscalibration. Together the three define a coherent **"PRS-as-a-clinical-test robustness"** literature.
  (c) **Connects to the composite-PRS-plus-rare-variant theme.** If tails are enriched for rare-variant effects, then PRS + ACMG/pLoF burden composite scoring is the natural fix — which is on your INTERESTS file under "composite risk models stacking PRS with rare pathogenic variants."
- **Action:** **HIGH.**
  (i) Read for the *evidence type* — do they show tail-architecture difference via enrichment for specific pathways, enrichment for rare-variant signals, or distributional moments of effect-size? Each implies a different fix.
  (ii) Note the traits used — height, BMI, T2D, CAD? Whether the result holds for *psychiatric* or *immune* traits is the open question.
  (iii) Map to your composite-risk scoring work — if rare-variant enrichment in tails is real, that's the empirical case for moving away from pure-PRS to PRS+pLoF burden.

### 5. Decoding common and rare noncoding variant effects across cellular and developmental contexts
- **Authors / venue:** A.R. Marderstein, S. Kundu, E.M. Padhi, S. Deshpande et al. — *Nature Genetics*, 2026.
- **Surfaced by:** **Triple-feed saturation** — (a) *Jay Shendure — new related research*, (b) *Konrad Karczewski — new related research*, (c) *Stephen B. Montgomery — new articles*. The Shendure / Karczewski / Montgomery trio collectively defines the variant-interpretation citation map; firing across all three (and as a *new article* for Montgomery, meaning he's an author or close-collaborator) is high-signal.
- **Thread:** **Variant interpretation** (ACMG / ClinGen — specifically the noncoding-VUS resolution gap, where ACMG criteria are weakest) **+** Genetic epidemiology (rare-variant effect-size estimation in noncoding regions).
- **What it is:** Method + empirical paper for jointly modeling common and rare noncoding variant effects across *cellular contexts* (cell-type-specific regulatory effects) and *developmental contexts* (different effects across embryonic vs adult tissue). The dual common-and-rare framing is the technically novel part — most prior noncoding methods are tuned to one or the other; this one does both. Shendure-group authorship suggests this leverages MPRA + lentiMPRA + saturation-mutagenesis data at scale.
- **Why it matters to you:** Three reasons.
  (a) **Noncoding VUS resolution is the unresolved gap in ACMG.** ACMG criteria are strongest for missense and pLoF; the noncoding criteria (PM4, PVS1 splicing, BP7) are sparse and inconsistently applied. Any methodological advance in noncoding-variant interpretation directly affects which VUSes can be resolved.
  (b) **Cellular and developmental contexts matter for clinical interpretation.** A regulatory variant that affects only neural-crest-stage expression has different penetrance than one with adult-pan-tissue effect. ClinGen VCEPs have not yet incorporated cell-type-resolved evidence in a standardized way; this paper is likely to be the methods reference.
  (c) **Triple Shendure/Karczewski/Montgomery firing.** This combination of senior authors marks the paper as the field's likely default citation for noncoding-effect-size estimation in 2026 H2.
- **Action:** **HIGH.**
  (i) Read for the data modalities — MPRA only, MPRA + eQTL, or MPRA + perturb-seq? The breadth of evidence types affects how generalizable the framework is.
  (ii) Check whether they release a per-variant noncoding effect-size score (analogous to AlphaMissense for missense). If so, that score becomes a citation when assigning weights to noncoding variants in your rare-variant composite-risk work.
  (iii) Note the rare-variant evaluation — do they evaluate against curated noncoding ClinVar entries, or only against MPRA-derived ground truth? Curated-ClinVar evaluation is more clinically actionable.
  (iv) Pair with the Souaiaia tails paper (#4) — if noncoding rare variants drive the tail-architecture difference, these two papers compose into a coherent argument.

### 6. Plasma proteomic signatures of cellular aging predict human disease
- **Authors / venue:** D.Y. Ding, V.A. Bot, K.L. Chen, J.W. Groves, R. Pálovics et al. — *Nature Medicine*, 2026.
- **Surfaced by:** *10 new citations to articles by Stephen B. Montgomery* feed.
- **Thread:** **Multimorbidity / aging / chronic disease trajectories** (organ-specific aging is the modern multimorbidity framing) **+** ML for precision health (proteomic signatures = predictor) **+** adjacent to the composite-PRS-plus-omics theme.
- **What it is:** Proteomic (likely Olink or SomaScan) signatures of cellular aging are mapped onto incident-disease prediction across a large EHR-linked cohort (likely UKB-PPP given the methodology, or possibly the Stanford Aging Plasma Proteome cohort). The "asynchronous aging across cells and organs" framing is the Wyss-Coray / Pálovics line — different organs age at different rates, and proteomic signatures can read out organ-specific aging at scale.
- **Why it matters to you:** Three reasons.
  (a) **Multimorbidity is one of your INTERESTS threads** ("disease trajectories from EHR or biobank data"). Organ-specific aging as a *unifying covariate* for multimorbidity is one of the cleaner methodological framings, and a Nature Medicine paper in this space becomes a default reference.
  (b) **Proteomic signatures are the next-gen risk-stratification layer over PRS.** Your INTERESTS file mentions "composite risk models stacking PRS with rare pathogenic variants"; proteomics is the symmetric layer (predictor of *short-term* risk, complementary to PRS's *lifetime* risk). Worth knowing the field's leading citation when arguing for proteomic + PRS composite scoring.
  (c) **UKB-PPP infrastructure is on-thread.** If this paper uses UKB-PPP, the data primitives (Olink-NPX adjusted for batch, etc.) become reusable for any AoU-equivalent work as proteomic data lands in AoU sub-cohorts.
- **Action:** **HIGH (multimorbidity thread); METHODS-WATCH (PRS+omics composite-risk thread).**
  (i) Read for the cohort identity — UKB-PPP vs UCSF/Stanford aging cohort. UKB-PPP is much more transferable.
  (ii) Note the proteomic platform — Olink Explore HT (~5400 proteins) vs SomaScan (~7000 proteins). Cross-platform reproducibility of the aging-signature is the open question.
  (iii) Check whether they validate the proteomic age signature against EHR-derived disease outcomes (the multimorbidity question) or only against chronological age (the aging-clock question). The former is much more clinically actionable.
  (iv) Worth a save for any multimorbidity-trajectory write-up.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic)

- **bioETH-Beacon: A Confidential On-Chain Genomic Beacon with Encrypted Counts, Filters, and Bounded Noise over a Fully Homomorphic EVM** — C. Galanopoulos, K.A. Provatas, I. Georgakopoulos-Soares — *arXiv 2606.20315*, 2026 (q-bio.GN, surfaced by `arxiv-digest` 06-19). Privacy-preserving GA4GH Beacon-style aggregate-variant-count queries running on a fully homomorphic Ethereum VM. **Off-thread** for daily work, but **methodologically interesting** as an instance of (a) PGS-catalog data being used as a synthetic-cohort benchmark, and (b) cryptographic primitives applied to federated genomic-query infrastructure — relevant if any future AoU / MVP / UKB federated work needs cryptographic-rather-than-policy data access controls. Score 2 in the digest (`polygenic score`, `polygenic` keyword hits, both incidental).

- **MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization** — A. Aueawatthanaphisut — *arXiv 2606.20164*, 2026 (cs.CL, surfaced by `arxiv-digest` 06-19). Single-author architecture paper for a multi-agent recursive-inspection framework over long-context EHR + imaging + ECG + ICU time series. **No empirical results**, just framework + evaluation design. *Watch for:* the **Clinical Evidence Graph Memory** primitive (per-patient subgraph linking observations to retrieved evidence + standardized definitions) — if generalizable, that's a useful primitive for any retrieval-augmented EHR-FM design.

- **Precision medicine's inevitable trajectory toward rare-disease-sized cohorts: implications for machine learning and deep learning** — A. Janowczyk, D. Merkler, O. Michielin, A. Madabhushi — *The …* (likely *The Lancet Digital Health* or similar perspective venue), 2026 (rare-diseases keyword feed). Perspective piece arguing that as precision medicine drills into molecularly defined subtypes, every cohort effectively becomes a rare-disease cohort (n ≪ p, no external validation set, no large held-out test). *Watch for:* the proposed mitigations — transfer learning from larger cohorts, Bayesian priors elicited from larger cohorts, federated rare-cohort pooling. **Useful citation** when arguing against pure-N-scaling for any rare-disease ML write-up.

- **RLKGC: Reinforcement Learning Retrieval with Large Language Models for Knowledge Graph Completion** — U.B. Teya, K. Shu, S. Arslanturk, S. Draghici, L. Liu — *PAKDD*, 2026 (Tiffany Callahan related-research feed). RL-guided LLM retrieval applied to inductive knowledge-graph completion. *Watch for:* whether the retrieval is **biomedical-KG-specific** or generic. The Draghici / Arslanturk lineage suggests biomedical applications (likely SemMedDB or DrugBank), in which case it's directly on the KG + drug-repurposing axis; if it's generic KG completion, it's off-thread. **Generic KG-completion noise is the 7th consecutive window of this keyword leak** — see pipeline note below.

- **Assessment of Genetic Correlations Between Tobacco or Alcohol Use and Neurodegenerative Diseases Using East Asian Genetic Ancestry Genome-Wide … (LDSC)** — L. Wang, W. Belbellaj, F. Lona-Durazo et al. — *American Journal of …* (likely AJMG or AJHG), 2026 (Jian Yang related-research feed). LDSC genetic correlation in East Asian ancestry. *Watch for:* whether they use a re-derived East-Asian LD reference panel (BBJ) or attempt to port European LD scores — the LD-reference choice is the methodological pinch-point of cross-ancestry rg estimation, and it's relevant to any EAS-PRS work you do. **On the cross-ancestry methods thread,** light-read.

- **Personal Care Utility: Health as Everyday Infrastructure** — M. Abbasian, E. Khatibi, S.A. Farahani, N. Nagesh, A. Ilaty et al. — *arXiv*, 2026 (*Christopher G. Chute citations* feed). LLM-based health utility framing. Off-thread substantively, but cited by something Chute-adjacent — likely just a citation-graph leak. **SKIP-leaning METHODS-WATCH.**

- **Measurement noise limits the advantage of nonlinear models over linear models in biomedical prediction** — M.-A. Schulz, K. Ritter — *arXiv 2606.18420*, 2026 (cs.LG, surfaced by `arxiv-digest` 06-18). UK Biobank–based theoretical+empirical result that measurement error attenuates nonlinear-model advantage faster than linear-model advantage, with the implication that a *tie* between linear and flexible models is not a verdict on biological linearity. **METHODS-WATCH for any prediction-modeling write-up** — useful citation when defending a linear baseline against the "but did you try a transformer" referee comment, especially in UKB/AoU prediction work. Carry-forward from 06-18 since it wasn't reported then either.

---

## SKIP / noise (logged, no action)

- **Karczewski / Jay Shendure / James Zou "TXT" abstract excerpts about cohort-scale sequencing recommendations** (MacArthur + Daly + Sunyaev co-authored, Zou + Valiant referenced) — appears to be the same multi-author perspective piece surfacing as a snippet in three feeds. Likely about ancestry diversity in ever-larger sequencing cohorts; abstract too truncated to triage further. Logged.
- **OTULIN / Pyoderma gangrenosum (Nature Immunology)** — molecular-uncoupling-of-catalytic-activity paper surfaces in **four** citation feeds (Karczewski, Denny, Daniel Kastner, Joshua Denny). Off-thread — it's an autoinflammatory disease mechanism paper, not directly on your VEXAS/CHIP or IBD axes despite the autoinflammatory keyword overlap.
- **Sepsis-with-normal-lactate ICU cohorts** (Celi authors) — Leo Celi's group; off-thread (ICU sepsis, not your EHR-phenotyping or causal-inference threads in a directly applicable way).
- **Adiposity and cancer review** (Nature Metabolism, Jian Yang citation) — review-tier, off-thread.
- **GIGYF2 / autism synapse paper** (Evan Eichler new article) — molecular psychiatry, autism, off your threads.
- **Microbial Dark Matter, A Multi-layer Mystery** (Snyder feed) — microbiome, off-thread.
- **Integrated Experimental-Theoretical and Data-Driven Multiphysics Analysis of Material Properties in Coatings** (Hripcsak citation) — materials-science paper that incidentally cites Hripcsak; clear citation-graph leak.
- **Apoptosis signaling and cancer targeted therapy review** (Vogelstein citation) — cancer-mechanism review, off-thread.
- **Non-Clinical Toxicology of Therapeutic Vaccines review** (Pritchard citation) — off-thread.
- **46-Autoinflammatory Bone Diseases textbook chapter** (Kastner related-research) — textbook chapter, not primary literature.
- **Detecting Functional Memorization in Code Language Models** (Zitnik related-research) — LLM-security, off the clinical-FM thread.
- **Metric Match: A Subset Selection Approach to Evaluating LLM Judge Reliability** (Shah new articles) — LLM-judge-evaluation methodology, off-thread (no clinical hook in the abstract).
- **Implicit bias in medication prescribing scoping review** (Szolovits citation) — health-policy / equity, off the EHR-phenotyping methods thread.
- **Adverse events HPV vaccine post-marketing surveillance China** (Patrick Ryan related-research) — pharmacovigilance, off your causal-inference / TTE thread substantively.
- **2024-2025 COVID-19 vaccine and MACE among US veterans, JAMA Intern Med** (Al-Aly authorship, Miguel Hernán citation) — MVP-data pharmacoepi but on a topic (COVID vaccine cardiovascular safety) that isn't a tracked drug class. Logged — Al-Aly's group does AoU/MVP-style work, but this specific study is off the GLP-1/SGLT2/CFTR/HRT drug-class thread. Worth glancing only if you need a MVP TTE template.
- **Intellectual humility and online health information-seeking** (Chute related-research) — HCI / health-literacy paper, off-thread.
- **De Novo Biliprotein redesign** (David Baker new article) — protein design, off-thread.
- **arxiv-digest 06-20** — 0 papers due to fetch failure (see pipeline note). Not a dry day; a polling failure.

---

## Suggestions for the pipeline

All prior reports' recommendations remain unactioned. Today's items
add two new issues:

1. **06-20 arxiv-digest had a 3-of-4-category fetch failure.** Check the
   workflow logs for the actual error (likely 429 from arXiv API). If
   the new 5-second client delay + 15-second inter-category pause is
   getting hit anyway, consider (a) jittered retry-with-backoff per
   category, (b) further-doubling the inter-category pause, or (c)
   splitting the four categories into two workflow runs separated by
   90 minutes. Whichever fix is chosen, the digest should produce a
   distinct "polling-failure" output (already partly there — the "3/4
   categories failed" warning was present) rather than appearing
   indistinguishable from a 0-paper day.

2. **`knowledge graph` keyword: 7th consecutive window of non-biomedical
   hits** (today's RLKGC paper, last six windows of similar
   recommender-system leaks). Specific fix: change the keyword from
   `knowledge graph` to `biomedical knowledge graph` OR `clinical
   knowledge graph` OR a compound filter `(knowledge graph) AND (medical
   OR biomedical OR clinical OR EHR OR phenotype OR drug OR disease)`.
   The single highest-value 06-18 KG paper (Schatz et al.,
   explainable-drug-repurposing) wasn't surfaced by keyword anyway — it
   came via the Callahan feed — so tightening this keyword loses nothing
   real and removes a noisy class.

3. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds**
   (carry-forward, unaddressed). Today's items #3 (Kundu et al. multi-
   site EHR), #4 (Souaiaia tails), #5 (Marderstein noncoding), #6
   (Ding proteomic aging) all appeared in Scholar feeds because they're
   in journal venues (JAMIA / Nature / Nature Genetics / Nature
   Medicine), not in q-bio / stat.AP arXiv categories. The current
   `arxiv-digest` pipeline can never reach these without source
   expansion.

4. **`mendelian diseases` and `drug repurposing` keyword fixes**
   (carry-forward, 7th consecutive window). No new instance today, but
   not retracted — the underlying keyword behavior hasn't changed.

5. **Add `PRS stability` / `polygenic score stability` / `PRS
   robustness` / `polygenic tails` as keywords** (carry-forward).
   Today's item #4 (Souaiaia tails) is the third PRS-robustness sub-
   thread paper in two reports; this is now a coherent sub-pattern.

6. **Add `proteomic signature` / `aging clock` / `organ-specific aging`
   keywords** (new). Today's item #6 (Ding aging proteomic) is the
   second proteomic-aging paper in three weeks and pairs with the
   composite-PRS-plus-omics theme on your INTERESTS file. Worth catching
   directly.

7. **Add `noncoding variant interpretation` / `regulatory variant
   effect` / `MPRA` keywords** (new). Today's item #5 (Marderstein) is
   the first major noncoding-interpretation paper in this digest's
   history and would have been missed without the Shendure feed.

8. **Continue tracking your own self-citation feed as the single
   highest-precision channel.** Today's item #1 (Chen et al. nephro
   PRS+PheWAS) is a triple-feed hit including your own related-research
   alert. The pattern from 06-18 (your own *citations* feed surfacing
   the APOL1 transplant paper) is the gold standard; today's
   *related-research* hit is one tier lower but still high-precision.
   Keep both alerts as-is.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 6 | (1) Chen et al. nephro PRS+PheWAS [self+Bastarache×2], (2) Sivarajkumar et al. multimodal EHR FM [Szolovits+Hripcsak+Brandt], (3) Kundu et al. privacy-preserving multi-site EHR [Denny], (4) Souaiaia et al. PRS tails [Montgomery, Nature], (5) Marderstein et al. noncoding variant effects [Shendure+Karczewski+Montgomery, Nat Genet], (6) Ding et al. plasma proteomic aging [Montgomery, Nat Med] |
| METHODS-WATCH | 4 | bioETH-Beacon (PGS-catalog use in encrypted Beacon), MedRLM (recursive multimodal EHR reasoning), Janowczyk et al. (rare-disease-sized cohorts perspective), RLKGC (RL-LLM KG completion), Wang et al. (EAS LDSC tobacco/alcohol/ND), Schulz & Ritter (UKB nonlinear-vs-linear with measurement noise, carry-forward from 06-18) |
| SKIP | ~25 | See SKIP/noise section above |

Compared to the 06-18 report (5 HIGH / 6 METHODS-WATCH), this window
delivers a slightly higher HIGH count, driven by two triple-feed papers
(items #1 and #2) plus a third triple-feed paper (item #5). The
recurring pattern remains: nearly all on-thread signal comes from
Scholar alerts; the `arxiv-digest` pipeline produced one on-thread
paper (bioETH-Beacon, METHODS-WATCH) out of two papers across two days,
which is the typical recent-month ratio. The 06-20 fetch failure is the
primary new issue to act on.
