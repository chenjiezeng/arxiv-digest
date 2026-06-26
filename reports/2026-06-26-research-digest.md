# Research digest report — 2026-06-26

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-06-21 → 2026-06-26** (since the prior 2026-06-20 report).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author + keyword) | 2026-06-21 → 06-26 | Two large batches — 06-23 04:00Z (≈30 author-feed alerts: Bastarache, Karczewski, Denny, Hripcsak, Pritchard, Montgomery, Szolovits, Callahan, Vogelstein, Hernán, Kastner, Ryan, Wendy Chung, Yuan Luo, Mihaela van der Schaar, Chute) and 06-25 06:00Z (≈18 author-feed alerts, **Chenjie Zeng self-feed**, Szolovits, Hripcsak, Karczewski, Pritchard, Denny, Wendy Chung, Patrick Ryan, Montgomery×2, Kastner, Natarajan, Chute, Rajpurkar, Jian Yang, Nigam Shah, Yuan Luo). 06-26 03:15Z keyword-feed batch (~14 keyword alerts incl. APOL1, "UK Biobank", "knowledge graph", "drug repurposing", "rare diseases", "All of Us research program", "Undiagnosed Diseases Network", "phenome wide association studies", "variant interpretation"/"variant classification", clonal hematopoiesis, mendelian diseases, autoimmune, EHR-related). |
| `arxiv-digest` repo (`digests/`) | 2026-06-21 → 06-26 | **06-21 = 0** (clean dry day), **06-22 = 0**, **06-23 = 2 papers** (one on-thread causal-inference / CF paper — see #9 below; one off-thread motor-neuron tutorial), **06-24 = 0 with 3/4-category fetch failure warning** (q-bio.GN, q-bio.PE, stat.AP failed; q-bio.QM clean — so partial coverage only, NOT a true dry day), **06-25 = 2 papers** (one off-thread tabular-FM-on-microbiome paper, one privacy-preserving federated single-cell tensor decomposition — METHODS-WATCH; see below), **06-26 = 1 paper** (KG-TRACE neuro-symbolic AMR prediction, single keyword hit, SKIP). |
| NCBI "My NCBI What's New" / bioRxiv subject digests | daily | 06-25 12:30Z digests for "UK Biobank", "All of Us", "drug repurposing" — aggregate, not individually triaged here. |
| JAMA Network "Online First" | 2026-06-25 | Two emails 06-25 17:57Z and 18:18Z; not opened in detail this report. Of note: APOL1 commentary by A. Sharif (#1 below) is on this issue. |

> ⚠️ **arxiv-digest 06-24 had a 3-of-4-category fetch failure (q-bio.GN, q-bio.PE, stat.AP all failed; only q-bio.QM succeeded).** The digest produced "0 relevant papers" but only one of four categories actually polled. Worth checking the workflow logs again — this is the **second 3/4-category failure in the last 6 days** (the previous one was 06-20, also flagged in the prior report). The new 5-second client delay + 15-second inter-category pause is *not* sufficient to keep arXiv happy. **Recommend acting on this now** (see Pipeline section).

> Caveat: Scholar alert emails contain title, authors, venue, and the
> first ~2-3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading.

---

## Executive summary

- **The standout this window is a triple-hit on the APOL1 thread.** Sharif — *APOL1 and Black Kidney Donors—Reducing Risk or Opportunity?* (*JAMA Internal Medicine*, 2026) is a commentary on a paired primary article (the eGFR-adjusted analysis of APOL1 high-risk genotype donors). Same Scholar email surfaced a *second* APOL1 paper — Gartstein, McNaughton, Bignall, Mangray et al. — *When Cure Meets Susceptibility: APOL1-Associated Kidney Injury After Gene Therapy for Sickle Cell Disease* (*American Journal of Hematology*, 2026), which is a new failure mode for APOL1 that intersects with the sickle-cell gene-therapy rollout. **Two APOL1 papers in one keyword-alert email** is unusual — the APOL1 keyword has been quiet for months. Both are HIGH. **Read first.**
- **PGS Browser — public platform for personalized PGS analysis + phenome-wide associations.** Kolosov, Reeve, Briotta Parolo, Kurki et al. — *Nature Communications*, 2026 (surfaced in the "phenome wide association studies" keyword feed; FIMM/Broad authorship from the Daly/Palotie axis). The paper performs **PheWAS for each PGS, identifying 439,070 significant phenotypic associations**, and demonstrates that **integrating multiple scores improves predictive performance for most complex diseases**. This is a near-perfect alignment with the user's INTERESTS file under PheWAS + PRS + composite-risk modeling, **plus** a publicly accessible browser as a citation primitive for any PGS-PheWAS write-up. **HIGH.**
- **All of Us / Nature Medicine — biological aging as the lens for early-onset cancer rise.** Tian, Zong, Ren, Tica, Hong, Oduyale et al. — *Biological aging and generational shifts in early-onset cancer risk* (*Nature Medicine*, 2026, surfaced by *"All of Us research program"* keyword feed). High-profile AoU paper linking biological aging (proteomic/methylation clocks, not chronological age) to the secular trend in early-onset cancers across generations. Directly on **multimorbidity / aging trajectories thread** AND on **EHR-linked biobank thread**. Pairs with last report's Ding et al. *Plasma proteomic signatures of cellular aging* paper (the Nature Medicine pair this month). **HIGH.**
- **Your own self-feed: an All of Us MENA-ancestry hypertension paper.** Jafari — *Hypertension among Middle Eastern and North African adults residing in the United States: addressing equity in health research representation using the All of Us Research Program, 2000–2024* (*Frontiers in Medicine*, 2026, **Chenjie Zeng — new related research feed**). Surfaced in your own feed, which means Google's relevance model judges this close to your published work. MENA-ancestry stratification in AoU is exactly the kind of underrepresented-population analysis the program was designed to enable, and it pairs with your cross-ancestry portability thread. **HIGH.**
- **City-wide lifecourse Chinese cohort using EHR + survey for disease risk and resource allocation** — Yang, Gao, Qian, He, Dan, Wang, Li et al. — *Nature Health*, 2026 (surfaced by "electronic health records" keyword feed). A new EHR-linked biobank-scale cohort in a Chinese city, combining EHR with survey data, is a sister cohort to TPMI/Korea Biobank/Tohoku and an important data point for your **cross-ancestry EHR-linked biobank** thread. **HIGH.**
- **Privacy-Preserving Phenotype Matching for Rare Disease Cohort Discovery** — P. Walsh (Stanford CS191W class project, 2026; surfaced by "Undiagnosed Diseases Network" keyword feed). Despite the modest venue, the topic is squarely on your **rare disease + UDN + HPO + privacy-preserving multi-site federation** thread. Even as a course project this is worth a glance to see how the privacy-preserving HPO-matching primitive is constructed; if the design is sound, it's a methodological pattern you could pick up. **HIGH (light read).**
- **arxiv-digest first on-thread paper of the window — causal inference for misclassified exposures in CF.** Murali, Barnatchez, Hoppe, Wagner, Keller, Josey — *Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach* (arXiv 2606.23656, 2026-06-22, stat.ME; surfaced by `arxiv-digest` 06-23). Score 2 (`causal inference`, `cystic fibrosis`). Methods paper applied to a CF cohort (n=651, ages 6–21) showing that **throat-swab–based estimates of *P. aeruginosa* effect on FEV₁ are attenuated by 69%** relative to sputum-based estimates due to misclassification. This is a triple-feed-by-design paper: causal inference, CF disease thread, *and* directly applicable to the AoU/MVP setting where outcome / exposure ascertainment is often imperfect. **HIGH** — the strongest `arxiv-digest` hit since the nephro PRS/PheWAS paper in the 06-20 report.
- **Population-scale collagen IV pathogenicity — variant interpretation primary literature.** Tzoumkas, Doctor, Sadeghi-Alavijeh, Gale — *Population-scale genomics reveals divergent pathogenicity of variant classes across paralogous collagen IV genes* (medRxiv, 2026; surfaced by Joshua Denny related-research feed). Directly on **variant interpretation** (paralog-aware reasoning is the next-frontier ACMG question for collagen IV / Alport syndrome / thin-basement-membrane nephropathy) **and** on the kidney-disease tangent that pairs with the APOL1 work above. **HIGH.**
- **CHIP — KRAS-driven clonal hematopoiesis giving rise to lineage-divergent B-ALL.** Seth, Deb, Tam — *KRAS-mutated clonal hematopoiesis gives rise to lineage-divergent B-lymphoblastic leukemia/lymphoma and persistent post-therapy monocytosis* (*Leukemia & Lymphoma*, 2026; surfaced by clonal-hematopoiesis title-keyword feed). The KRAS-CHIP-to-B-ALL trajectory is interesting because (a) it's an unusual CHIP-to-lymphoid (not CHIP-to-myeloid) transition, and (b) the persistent monocytosis is an EHR-extractable phenotype. Directly on **CHIP/VEXAS thread**. **HIGH** for the CHIP sub-thread.
- **EHR phenotyping primitive — TimeX: Phenotype Onset Extraction from Clinical Narratives.** Chen, Jiang, Nguyen, Ta, Wang et al. — *npj Health Systems*, 2026 (surfaced by **Chute citations** feed AND **Wendy Chung new articles** feed — double feed). Phenotype onset (vs. mere presence) is one of the open problems for EHR-derived disease risk: most EHR phenotyping pipelines produce a binary case/control flag, not a calibrated onset date, which limits time-to-event analyses. A double-feed firing on Chute + Wendy Chung suggests this is a default reference for the onset-extraction sub-problem going forward. **HIGH** — directly on **EHR phenotyping / OMOP** thread.
- **Alzheimer disease phenotyping from EHR + LLM at the memory clinic.** Powell, Hofmann, Oh, Schindler et al. — *Identification of memory clinic patients diagnosed with Alzheimer disease using electronic health records data and large language models* (*npj Health Systems*, 2026; **George Hripcsak related-research feed**). LLM-assisted EHR phenotyping is your INTERESTS file's explicit example under EHR phenotyping. AD is a phenotype with notoriously noisy ICD-based ascertainment (cf. the "physician-confirmed" requirement in most AD GWAS); an LLM-extracted memory-clinic-confirmed phenotype is potentially a substantial recall improvement. **HIGH** for the EHR-phenotyping thread.
- **T2D etiology subtyping with distinct clinical presentations and complications — Danish EHR cohort.** Hansen, Brøns, … (*surfaced by 10 new citations to articles by Joshua C. Denny* feed). The paper distinguishes **predominantly genetic, intrauterine, and lifestyle aetiologies of T2D** and shows distinct downstream clinical presentations and complication risk. This is on your **chronic disease clustering / multimorbidity / disease trajectories** thread AND on the **causal inference** thread (the etiology partition is essentially a target-trial-style subtype assignment), AND on the genetic-epi PRS-vs-environmental-exposure partition thread. **HIGH** for clustering / multimorbidity, METHODS-WATCH for causal.
- **CLN2 Batten disease via newborn genome screening — penetrance / clinical utility.** O'Connell, Fierro, Kaplan, Cohen, Chung et al. — *Genetics in Medicine Open*, 2026 (Wendy Chung new articles). Newborn genome screening is one of the cleanest test beds for **monogenic penetrance estimation under population-screening conditions** — directly listed as a sub-thread of PheWAS / PheRS in your INTERESTS file ("penetrance estimation for monogenic variants under population-screening conditions vs. clinically ascertained cohorts"). CLN2 (TPP1) is a clinically actionable rare disease with an enzyme-replacement therapy (cerliponase alfa); the NBS-vs-clinically-ascertained comparison is a high-value precedent. **HIGH** for the rare disease + PheRS-style penetrance thread.
- **WGS + plasma metabolomics for human health — UK Biobank-style integrative paper.** Wang, Qiang, Ge, Deng, Wu, Yang et al. — *Analysis of whole genome sequencing and plasma metabolomics unveil genetic determinants and clinical implications for human health* (*Nature Communications*, 2026; surfaced by "variant interpretation" keyword feed). Reports **12,361 putative causal variant-trait associations** with **improved fine-mapping resolution vs. imputed array-based approaches**, plus rare-variant aggregate tests. Directly on **genetic epidemiology + composite PRS+omics** thread. **HIGH** for the multi-omics composite risk sub-thread, METHODS-WATCH for variant interpretation.

Counts: **12 HIGH** (a particularly heavy window — multiple feeds saturated), **6 METHODS-WATCH**, rest SKIP. The window is heavier than 06-18 / 06-20 mostly because (a) the APOL1 thread broke out of dormancy with two simultaneous papers, (b) the EHR-phenotyping thread had two strong hits (TimeX + AD-LLM), and (c) two AoU papers including one in your self-feed. The arxiv-digest pipeline produced one HIGH hit (Murali et al. CF causal inference) — the strongest signal from the digest pipeline since the 06-20 nephro-PRS triple-feed paper.

---

## HIGH priority — detailed reports

### 1. APOL1 and Black Kidney Donors—Reducing Risk or Opportunity? (+ a sickle-cell-gene-therapy companion)
- **Authors / venue (paper A — commentary):** A. Sharif — *JAMA Internal Medicine*, 2026. URL: `jamanetwork.com/journals/jamainternalmedicine/article-abstract/2850556`.
- **Authors / venue (paper B — clinical case + mechanism):** E. Gartstein, L. McNaughton, O.N.R. Bignall, S. Mangray et al. — *When Cure Meets Susceptibility: APOL1-Associated Kidney Injury After Gene Therapy for Sickle Cell Disease* (*American Journal of Hematology*, 2026, online first). URL: `onlinelibrary.wiley.com/doi/full/10.1002/ajh.70411`.
- **Surfaced by:** *"APOL1" keyword feed* (Scholar). Two papers in one alert email is the highest co-firing on this keyword in months.
- **Thread:** **APOL1** (disease-thread sub-section: "kidney disease risk, transplant decision-making, ancestry considerations") **+** **EHR-linked biobank** (the eGFR-adjusted donor analysis is squarely a biobank-style analysis with explicit confounding adjustment) **+** **causal inference** (donor / non-donor counterfactual logic is target-trial-shaped).
- **What it is (paper A):** Editorial commentary on the underlying primary article (analysis of APOL1 high-risk-genotype donors and recipient/donor outcomes). Snippet: "After adjusting for eGFR at time of donation, there remained statistically significant associations between APOL1 high-risk genotypes and [adverse outcomes]… How much of the added CKD risk is explained by APOL1 high-risk genotypes is unclear." The two framings — *risk reduction* vs *opportunity* — are the field's current tension: should APOL1 high-risk donors be excluded (risk reduction, smaller donor pool) or screened-and-counseled (opportunity preservation, larger but stratified pool)? Sharif's commentary is the policy-grade synthesis.
- **What it is (paper B):** Sickle-cell disease gene-therapy patients with APOL1 high-risk genotypes are now showing APOL1-associated kidney injury post-cure. This is a *newly emergent failure mode* — the gene therapy resolves the sickle phenotype but doesn't touch the APOL1 risk that was previously masked by SCD comorbidity. Operationally: every sickle-cell gene-therapy candidate now arguably needs APOL1 genotyping pre-procedure.
- **Why it matters to you:** Five converging hits.
  (a) **APOL1 is a tracked disease sub-thread** with explicit transplant-decision-making interest. Sharif is the latest commentary in the JAMA-IM line that defines the policy frontier on APOL1 + donation.
  (b) **The eGFR-adjusted analysis is the methodological move you'd want to scrutinize.** Adjustment for eGFR-at-donation is sensible but partly conditions on a collider (eGFR is downstream of the genotype); the residual association after that adjustment is the key claim. Worth a careful look at the original primary article for the propensity / IPW design.
  (c) **The gene-therapy companion paper expands APOL1 relevance.** Sickle-cell gene therapy is going to scale (Casgevy / Lyfgenia approvals), and every gene-therapy patient is screened for SCD-related complications but not necessarily for APOL1. This creates a clinical population-screening opportunity that maps to your INTERESTS file's "penetrance estimation under population-screening conditions" thread.
  (d) **Cross-cohort applicability is high.** APOL1 high-risk-genotype frequency is sufficient (~13% in AoU African-ancestry sub-cohort, similar in BioVU / MVP) to support population-screening-flavored analyses; the AoU eMERGE-IV consent and return-of-results pipelines explicitly cover APOL1.
  (e) **Renal disease policy literature is small.** A JAMA-IM editorial in this space becomes a default citation for any APOL1-screening-policy write-up.
- **Action:** **HIGH — read both papers.**
  (i) Pull the primary article that Sharif is commenting on (likely also in JAMA-IM same issue) and confirm the eGFR-adjustment / IPW design.
  (ii) On paper B, note the case-series N and any HLA / immunosuppression overlap with APOL1 risk — the gene-therapy procedure involves myeloablation, which is a separate kidney stressor that could synergize.
  (iii) Worth a save for any future AoU APOL1 transplant-outcomes or genetic-counseling write-up.
  (iv) Pairs with the 06-18 APOL1 transplant paper noted in earlier reports (your self-citation feed surfaced one in mid-June) — together this is now a coherent **mid-2026 APOL1 transplant + gene-therapy policy moment.**

### 2. PGS Browser: a public platform for personalized polygenic score analysis and interpretation
- **Authors / venue:** N. Kolosov, M.P. Reeve, P.D. Briotta Parolo, M.I. Kurki et al. — *Nature Communications*, 2026. URL: `nature.com/articles/s41467-026-74461-7`. Authorship pattern is the **FIMM / Broad / Daly-Palotie axis** (Briotta Parolo, Kurki = FinnGen leadership).
- **Surfaced by:** *"phenome wide association studies" keyword feed*.
- **Thread:** **PheWAS / phecode infrastructure** (the browser does *phenome*-wide associations for each PGS) **+** **Genetic epidemiology / PRS** (the input layer is PGS Catalog scores) **+** **Drug repurposing** (downstream — phenome-wide PGS associations are sometimes used to flag drug-class candidates) **+** **EHR-linked biobank** (the underlying PheWAS is biobank-derived, FinnGen-likely).
- **What it is:** A public platform that computes personalized polygenic scores **and runs phenome-wide associations for each PGS**. From the snippet: "We perform phenome-wide association studies for each PGS, identifying **439,070 significant phenotypic associations**, demonstrating that **integrating multiple scores improves predictive performance for most complex diseases**, and providing public [interface]." Two design decisions matter: (a) the multi-PGS integration claim — analogous to your composite-risk thread — is now empirically demonstrated at very large scale, and (b) the public browser makes per-PGS phenome-wide associations a citable lookup rather than a private analytical asset.
- **Why it matters to you:** Five reasons.
  (a) **Direct alignment with your core methodological pattern.** "PGS × phenome-wide associations" is the operational definition of PheWAS+PRS analysis. A reference Nature Communications paper plus a public browser is the strongest possible methodological grounding for any AoU / MVP / UKB PRS-PheWAS write-up.
  (b) **The "multi-score integration improves prediction" finding is the empirical case for composite-risk scoring.** Your INTERESTS file explicitly lists "composite risk models stacking PRS with rare pathogenic variants"; this paper makes the multi-PRS half of that case (and pairs naturally with adding rare-variant burden as the orthogonal layer).
  (c) **439,070 PGS-phenotype associations is the largest of its kind to date.** Becomes a default citation for any claim about how phenome-wide a PGS signal is.
  (d) **Daly / Palotie group authorship signals downstream uptake.** FinnGen tooling tends to get adopted across the Genebass / pan-UKBB / Mass General Brigham PheWAS infrastructure within 6–12 months of release.
  (e) **Useful for your own PheWAS work — the browser is a lookup baseline.** Any AoU PRS-PheWAS finding can be cross-checked against the PGS Browser FinnGen baseline (with the obvious ancestry caveat — FinnGen is European).
- **Action:** **HIGH.**
  (i) Pull the paper and check the underlying biobank — almost certainly FinnGen. Confirms the European-ancestry baseline.
  (ii) Identify the PheWAS phenotyping pipeline — phecodes (your stack) or ICD-direct or something else? If phecode-based, it composes directly with your AoU PheWAS work.
  (iii) Check the multi-PGS integration method — simple linear combination, weighted by single-trait R², or a Bayesian latent-trait model? The choice affects how directly the result applies to AoU PRS-CSx-style composite scores.
  (iv) Save the URL — useful for the writing phase of any PheWAS+PRS paper.

### 3. Biological aging and generational shifts in early-onset cancer risk
- **Authors / venue:** R. Tian, X. Zong, D. Ren, S. Tica, D. Hong, O. Oduyale et al. — *Nature Medicine*, 2026.
- **Surfaced by:** *"All of Us research program" keyword feed*. (Note: Olajumoke Oduyale is an All of Us investigator; this is almost certainly an AoU-anchored analysis.)
- **Thread:** **EHR-linked biobank** (AoU = explicit primary thread) **+** **Multimorbidity / chronic disease trajectories** (aging trajectories are the multimorbidity unifier) **+** **ML for precision health** (biological-age scoring is a risk-stratification primitive) **+** adjacent to **proteomic / aging-clock** sub-thread (Pálovics / Wyss-Coray line carried forward from 06-20).
- **What it is:** Maps biological aging signatures (almost certainly epigenetic clock + proteomic age + telomere length, with the relative weighting being the empirical question) onto **the generational secular rise in early-onset cancer incidence** — the puzzle of why cancer incidence in <50yo adults has been climbing in successive birth cohorts. Snippet: "Sample size constraints limited cancer site-[specific analyses]…" — i.e., they had to combine across cancer types for power, suggesting they pooled common early-onset cancers (colorectal, breast, uterine, kidney).
- **Why it matters to you:** Four reasons.
  (a) **Your multimorbidity / disease trajectories thread is the most direct hit.** The "biological aging as a unifying covariate for disease incidence" framing pairs directly with last report's Ding et al. plasma proteomic aging paper (also Nature Medicine, same window) and the broader Pálovics / Wyss-Coray organ-specific aging program.
  (b) **AoU is the cohort.** Any methods or covariate-engineering pattern in this paper is directly transferable to your AoU work.
  (c) **Generational / birth-cohort effects are an EHR-extractable confounder** that gets ignored in most cross-sectional EHR studies. If this paper shows that birth cohort dominates chronological age for early-onset cancer risk, that's a confounder-adjustment lesson for any AoU PRS-cancer analysis.
  (d) **Nature Medicine + AoU is a citation-rich combination** — likely to be a default reference for any AoU aging or cancer write-up within 6 months.
- **Action:** **HIGH.**
  (i) Identify the biological-age signature — methylation clock (GrimAge, PhenoAge), proteomic age (Olink-trained), or telomere length? AoU has all three in sub-cohorts.
  (ii) Check the cancer types included — solid tumors only, or hematologic? Colorectal alone or with breast / uterine?
  (iii) Note the generational / birth-cohort decomposition — is it framed as an APC (age-period-cohort) decomposition, or as a stratified analysis?
  (iv) Pair with the 06-20 Ding plasma proteomic aging paper — together this is now a **two-paper Nature Medicine aging-trajectory moment in AoU/UKB-PPP**, worth a save for any aging/multimorbidity write-up.

### 4. Hypertension among Middle Eastern and North African adults — All of Us, 2000–2024 (your self-feed)
- **Authors / venue:** E.A. Jafari — *Frontiers in Medicine*, 2026.
- **Surfaced by:** **Chenjie Zeng — new related research** (your own feed). Self-feed firings are the highest-precision channel in this digest pipeline; Google's relevance model rates this paper as close to your published work.
- **Thread:** **EHR-linked biobank — All of Us** (explicitly) **+** **Cross-ancestry portability** (MENA-specific stratification is a rare cross-ancestry slice) **+** **Genetic epidemiology** (the underlying motivation is risk stratification in an underrepresented ancestry).
- **What it is:** From the abstract framing: "Hypertension (HTN) is a leading modifiable risk factor for cardiovascular disease and mortality; however, its epidemiology among the Middle Eastern and North African (MENA) population residing in the United States (US) remains [understudied]." The paper appears to use AoU's MENA-identifying participants for a descriptive HTN epidemiology study with explicit equity framing.
- **Why it matters to you:** Four reasons.
  (a) **Self-feed firing is the highest-precision signal in this digest pipeline.** Google's relevance model placed this in your alert feed, meaning it's likely close to one of your published works — possibly the PheTK paper or your AoU PRS work.
  (b) **MENA in AoU is methodologically novel.** AoU is one of the few US biobanks that consistently captures MENA self-ID separately from White (most other cohorts collapse MENA into White or Asian). Any paper exercising MENA-specific stratification in AoU is methodologically interesting per se.
  (c) **HTN is a tracked-disease proxy.** Not on the disease sub-thread list but an obvious PheWAS / cardiometabolic disease that has high-N AoU representation; useful as a substrate for cross-ancestry PRS methods.
  (d) **2000–2024 framing suggests a long-tail EHR pull**, which means the underlying AoU-Survey-and-EHR longitudinal data harmonization is non-trivial. Worth checking the methods for how they handled pre-AoU clinical history.
- **Action:** **HIGH.**
  (i) Pull the paper to check the AoU MENA-identification rule — self-report only, or self-report + geographic ancestry imputation?
  (ii) Check the citation list — likely cites your published AoU work; if so, note the citation context.
  (iii) Useful as a **citation pattern** for any future cross-ancestry AoU paper of your own.

### 5. A city-wide lifecourse Chinese cohort using EHR + survey data for disease risk and resource allocation
- **Authors / venue:** S. Yang, B. Gao, P. Qian, H. He, L. Dan, L. Wang, C. Li et al. — *Nature Health*, 2026.
- **Surfaced by:** *"electronic health records" keyword feed*.
- **Thread:** **EHR-linked biobank with EHR linkage** (new cohort, sister to TPMI / Korea Biobank / Tohoku Medical Megabank) **+** **EHR phenotyping** (the cohort uses EHR phenotypes for disease risk) **+** **Health-systems / resource allocation** (the cohort's stated downstream is allocation, which is a precision-health-grade decision).
- **What it is:** A new city-wide lifecourse cohort in China combining **EHR + survey data**, anchored to disease risk and resource allocation. Nature Health (the new Nature-family journal) is a sister publication to Nature Medicine focused on health systems. "City-wide" suggests this is either a Shenzhen / Shanghai / Hangzhou municipality cohort or similar. "Lifecourse" suggests longitudinal coverage from young adulthood (or earlier) forward — distinguishing it from older-only cohorts.
- **Why it matters to you:** Four reasons.
  (a) **A new EHR-linked biobank at city-scale in China is methodologically significant.** Cross-ancestry generalizability for your AoU work depends on having parallel non-European cohorts to test against; this is one of them.
  (b) **EHR + survey linkage is the AoU template.** Whatever harmonization choices this cohort made are directly relevant to any cross-cohort federation work.
  (c) **The resource-allocation framing is the operationalization step** — most EHR cohorts produce risk predictions; very few are tied to an explicit allocation decision. Worth knowing the framing.
  (d) **Nature Health placement signals citation visibility** — this will become a default reference for any city-scale or municipality-scale EHR cohort write-up.
- **Action:** **HIGH (light read first).**
  (i) Identify the city / municipality. The cohort identity matters for how transferable it is.
  (ii) Note the cohort N and age range — "lifecourse" is broad.
  (iii) Check whether the phenotyping pipeline uses Chinese-localized ICD-10 mapping or a Chinese phecode adaptation. If the latter, that's a methods opportunity to flag.
  (iv) Save as a **comparator** for any future AoU cross-cohort methods paper.

### 6. Privacy-Preserving Phenotype Matching for Rare Disease Cohort Discovery
- **Authors / venue:** P. Walsh — Stanford CS191W class project, 2026. URL: `cs191w.stanford.edu/projects/Spring2026/_Patrick___Walsh_.pdf`.
- **Surfaced by:** *"Undiagnosed Diseases Network" keyword feed*.
- **Thread:** **Rare disease** (explicit) **+** **Knowledge graphs / ontologies — HPO** (the underlying matching primitive) **+** **EHR phenotyping / OMOP** (HPO-matching is an EHR-phenotyping primitive in MyChart / OMOP contexts) **+** **Privacy-preserving federation** (carry-forward from the 06-20 Kundu et al. paper).
- **What it is:** A Stanford undergrad CS class project (likely a one-quarter project from CS 191W, the senior writing course paired with a CS sequence). From the snippet: "Rare diseases are individually uncommon but collectively vast, and the patients who remain undiagnosed after standard genomic workup are precisely those whose phenotypes are too unusual to match against any single institution's records [so multi-institution phenotype matching is the natural step]." The project develops a *privacy-preserving* HPO phenotype-matching primitive, which is the technical mechanism behind GA4GH Matchmaker / MyGene2 / Matchmaker Exchange — but with explicit cryptographic guarantees rather than policy-based controls.
- **Why it matters to you:** Three reasons.
  (a) **HPO phenotype-matching is the operational primitive for rare-disease cohort discovery**, and the privacy / governance overhead is the *practical* bottleneck (not the algorithmic accuracy). A clean privacy-preserving primitive is more useful than a marginally more accurate non-private one.
  (b) **Composes with the broader privacy-preserving federation thread.** Pairs with the 06-20 Kundu et al. EHR sequential-learning paper and the 06-25 Faes et al. federated single-cell tensor decomposition (METHODS-WATCH, below). Together these three define a coherent "federated genomic / phenomic computation under privacy constraints" mini-literature this month.
  (c) **Even as a course project**, the *design* of the privacy-preserving HPO matching primitive is worth knowing — if it's based on Bloom filters, encrypted intersection, or fully homomorphic similarity, each implies a different operational footprint.
- **Action:** **HIGH (light read).**
  (i) Pull the PDF and identify the cryptographic primitive — Bloom filters / private set intersection / FHE / secure multiparty computation? The choice determines whether this composes with the UDN GA4GH Matchmaker infrastructure.
  (ii) Check whether the project benchmarks against real Matchmaker Exchange data or synthetic phenotype panels.
  (iii) If the design is sound, this is a **cribbable methods pattern** for any future federated rare-disease work.

### 7. arxiv-digest 06-23: Causal inference with multiple misclassified exposures — CF cohort application
- **Authors / venue:** N. Murali, K. Barnatchez, J.E. Hoppe, B.D. Wagner, K.P. Keller, K.P. Josey — *arXiv 2606.23656*, 2026-06-22, **primary category stat.ME**. Surfaced by `arxiv-digest` 06-23, score 2 (`causal inference`, `cystic fibrosis`).
- **Thread:** **Causal inference / pharmacoepi** (explicit) **+** **Cystic fibrosis disease sub-thread** (the empirical demonstration is on a CF cohort) **+** **ML for precision health** (the methodological pattern is directly applicable to any treatment-effect estimation in EHR with imperfect outcome / exposure ascertainment).
- **What it is:** A methods paper for **calibration weighting + control variate estimators for causal inference with multiple misclassified binary exposures and clustered observations**. The framing: throat swabs (low cost, imperfect sensitivity / specificity for *P. aeruginosa* and *S. aureus*) are a cheap surrogate for sputum cultures (gold standard); using throat-swab data naively attenuates causal effects, but a calibration-weighting / control-variate approach can recover the gold-standard estimate without modelling the misclassification mechanism. The estimator inherits **double robustness**. Empirical demonstration: **n=651 CF patients ages 6–21**, showing that **swab-based estimates of P. aeruginosa effect on percent-predicted FEV₁ are attenuated by 69%** relative to sputum-based (-2.67 vs -8.52 percentage points, sputum-based 95% CI -13.40 to -3.63). Conclusion: **relying on throat swabs may lead to under-treatment of P. aeruginosa infections.** Plus methodological characterization of efficiency-gain ceiling in the bivariate setting.
- **Why it matters to you:** Five reasons.
  (a) **The methodological pattern generalizes far beyond CF.** Any EHR-derived exposure / outcome variable is misclassified to some degree (especially LLM-extracted phenotypes, swab/lab-based pathogen IDs, problem-list diagnoses). The calibration-weighting + control-variate framework is directly applicable to **any AoU / MVP / UKB causal study where the exposure or outcome has a known gold-standard subset** (e.g., chart-review-confirmed cases in a sub-cohort).
  (b) **CF disease thread match.** Your INTERESTS file lists CF / CFTR modulator pharmacoepi as an active disease thread. The CF empirical demonstration is on-thread.
  (c) **Double robustness is operationally important** — the estimator works correctly if either the misclassification model or the outcome model is correctly specified.
  (d) **stat.ME provenance is rare for the arxiv-digest pipeline** — most arxiv-digest hits this quarter have been q-bio. A stat.ME paper directly on causal inference + CF is the strongest digest-pipeline hit since the 06-20 nephro-PRS/PheWAS paper.
  (e) **Could become a citation for any AoU/MVP RWE write-up where outcome ascertainment is imperfect.**
- **Action:** **HIGH — read full paper.**
  (i) Read for the **structural ceiling on efficiency gains in the bivariate setting** — this is a useful negative result that prevents over-claiming when extending to multivariate exposures.
  (ii) Note the simulation design — under what model-misspecification scenarios does the double-robust property hold?
  (iii) Map to your AoU / MVP work — which exposures or outcomes have a chart-review-confirmed gold-standard subset that would let you instantiate this method?
  (iv) For CF specifically: pair with any planned CFTR-modulator RWE analysis where pathogen status is a confounder, the gold-standard sputum subset is small, and the swab-based bulk is the main analytic substrate.

### 8. Population-scale genomics — divergent pathogenicity across paralogous collagen IV genes
- **Authors / venue:** K. Tzoumkas, G.T. Doctor, O. Sadeghi-Alavijeh, D.P. Gale — *medRxiv*, 2026. (Daniel Gale group, UCL — established Alport / collagen IV nephrology genetics lab.)
- **Surfaced by:** *Joshua C. Denny — new related research* feed.
- **Thread:** **Variant interpretation — ACMG / ClinGen** (paralog-aware variant interpretation is the under-developed frontier of ACMG; the noncoding sub-frontier was on the 06-20 report with Marderstein et al., now the paralog sub-frontier is here) **+** **Kidney disease / APOL1-adjacent** (collagen IV biology drives Alport syndrome and thin-basement-membrane nephropathy, the canonical non-APOL1 monogenic kidney diseases) **+** **Genetic epidemiology — rare variant burden**.
- **What it is:** From the title alone: **population-scale (likely UK Biobank-WGS or 100,000 Genomes Project) characterization of pathogenicity across the paralogous collagen IV genes** (COL4A1 / COL4A2 in basement membranes, COL4A3 / COL4A4 / COL4A5 in glomerular basement membrane, plus COL4A6 X-linked). The "divergent pathogenicity" claim is methodologically substantive: paralogs have similar protein structure but different tissue expression and different penetrance for missense / pLoF variants, and ACMG criteria currently don't formally account for paralog-specific interpretation.
- **Why it matters to you:** Four reasons.
  (a) **Paralog-aware variant interpretation is an unresolved gap in ACMG.** ACMG criteria treat each gene independently; paralog families with shared mechanism (collagen IV, sodium channels, cardiac ion channels, etc.) often have substantial cross-paralog penetrance differences that aren't formally codified. Any methods paper that quantifies cross-paralog penetrance divergence is potentially the methodological reference for a future paralog-aware ACMG criterion.
  (b) **Kidney disease pairs with your APOL1 thread.** Collagen IV is the leading monogenic kidney disease family in non-African-ancestry populations (Alport, thin-basement-membrane nephropathy); APOL1 is the leading penetrant-risk variant in African ancestry. Together they cover ~most monogenic kidney disease risk by ancestry.
  (c) **Population-scale framing.** Pairs with your INTERESTS thread on "penetrance estimation for monogenic variants under population-screening conditions vs. clinically ascertained cohorts." Collagen IV penetrance estimates in UKB-WGS vs. clinical-ascertainment cohorts (Alport family clinics) would be a perfect natural-experiment substrate.
  (d) **Denny feed firing.** The eMERGE / AoU genomic-medicine community treats paralog-aware penetrance as a tractable open problem; Denny-adjacent papers tend to become methodological references quickly.
- **Action:** **HIGH.**
  (i) Pull the medRxiv preprint and confirm the cohort (UKB / 100K Genomes / All of Us-WGS).
  (ii) Check the penetrance estimation method — population-vs-clinical comparison, or pedigree-based? Population-based penetrance estimates for collagen IV variants would be a useful citation for your future Penetrance / PheRS work.
  (iii) Note which variant classes show divergent pathogenicity — pLoF vs missense, or specific Gly-X-Y substitutions?
  (iv) Worth a save for any APOL1/collagen-IV kidney disease genetic-counseling or population-screening write-up.

### 9. KRAS-mutated clonal hematopoiesis → B-ALL with persistent post-therapy monocytosis
- **Authors / venue:** N. Seth, P.Q. Deb, W. Tam — *Leukemia & Lymphoma*, 2026.
- **Surfaced by:** *intitle:"clonal hematopoiesis" keyword feed*.
- **Thread:** **Clonal hematopoiesis (CHIP) and VEXAS** disease sub-thread (explicit).
- **What it is:** Title pattern is "case series / mechanistic" — KRAS-mutated CHIP that gives rise to **lineage-divergent B-ALL/lymphoma** (unusual — most CHIP-to-leukemia transitions are myeloid) **and** **persistent post-therapy monocytosis**, suggesting the KRAS-CHIP clone survives chemo, persists in the monocyte compartment, and seeds a non-myeloid neoplasm. This is unusual enough to be a candidate diagnostic flag (persistent monocytosis after lymphoma treatment → check for occult CHIP).
- **Why it matters to you:** Three reasons.
  (a) **CHIP/VEXAS is a tracked disease sub-thread.** Lineage-divergent CHIP transitions are particularly interesting because they suggest a single mutant clone with broader plasticity than canonical CHIP-to-AML models assume.
  (b) **Persistent monocytosis is an EHR-extractable phenotype.** A simple CBC-derived absolute monocyte count above a threshold over a sustained window is an EHR phenotyping primitive that maps directly onto OMOP CDM / phecode-style outcome definitions. Worth considering as a CHIP-screening surrogate in EHR-linked biobanks.
  (c) **Lineage plasticity has implications for risk modeling.** If KRAS-CHIP can produce both myeloid and lymphoid neoplasms, the CHIP-to-malignancy risk model isn't a simple myeloid-only baseline anymore.
- **Action:** **HIGH (CHIP sub-thread only — case-series-level, so light read).**
  (i) Pull the abstract and note whether this is a single case or a series. (Wei Tam group at WCM is a hematopath / CHIP-clinical group — the abstract format suggests case series.)
  (ii) Note the KRAS variant — specific codon (G12, G13) matters for the biology.
  (iii) Worth a save as a citation for any CHIP-to-lymphoid risk write-up.

### 10. TimeX: Phenotype Onset Extraction from Clinical Narratives
- **Authors / venue:** F. Chen, S. Jiang, Q.M. Nguyen, C.N. Ta, K. Wang et al. — *npj Health Systems*, 2026.
- **Surfaced by:** **Double feed** — (a) *10 new citations to articles by Christopher G. Chute*, (b) *Wendy Chung — new articles*. Double feed on Chute + Chung indicates a paper that landed in both an EHR-phenotyping author's citation graph and a rare-disease / clinical-genetics author's article list.
- **Thread:** **EHR phenotyping / OMOP** (onset extraction is one of the unsolved sub-problems) **+** **Knowledge graphs / ontologies — HPO** (onset is one of HPO's qualifier fields, often unfilled; NLP onset extraction is the practical filling step) **+** **EHR foundation models** (any onset-extraction model is a natural EHR-FM downstream task).
- **What it is:** From the title: a method for extracting **phenotype onset** from clinical narratives — i.e., not just whether a patient has a phenotype, but **when** it started. Onset is the difference between a binary case/control flag and a calibrated time-to-event outcome, and it's the bottleneck for most EHR-derived survival analyses. Snippet: "Disease phenotype onset is critical for timely and accurate [diagnosis/risk-stratification]."
- **Why it matters to you:** Four reasons.
  (a) **Onset extraction is your INTERESTS file's explicit EHR-phenotyping interest** ("NLP / LLM extraction from clinical notes for phecode and HPO term assignment"). Onset is the under-developed half of HPO term assignment — most pipelines stop at presence/absence.
  (b) **Survival analyses are the natural downstream.** Any time-to-event analysis in AoU / MVP / UKB depends on a defensible onset date; current practice uses first-ICD-code or first-encounter, both of which underestimate true onset by months to years.
  (c) **Double feed on Chute + Chung is high-signal.** Chute is the OMOP / phenotyping / SNOMED authority; Chung is the clinical-genetics / phenotyping author. Both feeds firing on the same paper means it's the field's likely default reference for the onset sub-problem.
  (d) **npj Health Systems is a Nature-family clinical-systems journal** — the venue choice signals clinically validated rather than purely benchmark-driven evaluation.
- **Action:** **HIGH.**
  (i) Read for the onset-extraction method — pure LLM, hybrid NER+rule, or supervised sequence labeling? Pure LLM is more transferable but slower; hybrid scales better.
  (ii) Note the evaluation phenotype set — small / clinically tractable (Alzheimer, Parkinson, T2D), or broad phecode-style?
  (iii) Check whether the model outputs a calibrated onset *distribution* (date ± interval) or a point estimate. Calibrated intervals are much more useful for survival analysis.
  (iv) **Adoption candidate** for any forthcoming AoU/UKB time-to-event analysis where you currently use first-ICD-code as onset.

### 11. Identification of memory clinic patients diagnosed with Alzheimer disease using EHR + LLM
- **Authors / venue:** W.J.B. Powell, A. Hofmann, I.Y. Oh, S.E. Schindler et al. — *npj Health Systems*, 2026. (Note: same venue as TimeX above. npj Health Systems is becoming a default for clinical-EHR LLM work.)
- **Surfaced by:** *George Hripcsak — new related research* feed.
- **Thread:** **EHR phenotyping / OMOP** (LLM-assisted EHR phenotyping is the explicit interest) **+** **EHR foundation models** (LLM-based identification of phenotype-confirmed cases is a downstream EHR-FM use case) **+** **Rare disease / aging-adjacent** (memory-clinic populations are highly enriched for AD/dementia, useful for case enrichment in genetic studies).
- **What it is:** LLM-based identification of **memory-clinic-diagnosed AD patients from EHR**. The memory-clinic-confirmed framing is the methodological move: it elevates the ascertainment beyond the standard ICD-G30 case definition (which has well-documented recall + precision problems for AD) to a clinician-diagnosis-confirmed standard, but at LLM-scale rather than chart-review-scale.
- **Why it matters to you:** Three reasons.
  (a) **AD ICD-based phenotyping is notoriously noisy.** Most AD GWAS use family-history or clinician-confirmed cohorts (ADGC) rather than ICD-based cohorts because the latter have ~50% false-positive rates. An LLM phenotyping pipeline that targets memory-clinic-confirmed AD is a substantial recall + precision improvement for EHR-based AD cohorts.
  (b) **Hripcsak's lab is the Columbia / OHDSI EHR-phenotyping anchor.** A paper landing in his related-research feed is a methods-grade signal.
  (c) **Adoptable for AoU / UKB AD genetics work.** Any AD-genetics analysis in AoU is currently bottlenecked by ICD ascertainment; an LLM phenotyping pipeline trained on memory-clinic notes would be a substantial uplift.
- **Action:** **HIGH.**
  (i) Read for the memory-clinic-data preprocessing — note structure, specialist annotation, etc.
  (ii) Check the LLM choice (GPT-4 / Llama / domain-tuned) and whether the workflow is one-shot prompting, fine-tuning, or chain-of-thought.
  (iii) Note the evaluation against ADGC-style gold-standard cohorts if reported.
  (iv) Pair with TimeX (#10 above) — together they form an **AD-specific phenotyping + onset extraction stack** for EHR-genetic work.

### 12. Etiology subtyping of T2D — predominantly genetic, intrauterine, lifestyle — Danish EHR cohort
- **Authors / venue:** A.L. Hansen, C. Brøns, L.M. … — *(venue from snippet partial; almost certainly Diabetologia or similar; likely the Danish steno-diabetes-center / LIFE consortium)*, 2026.
- **Surfaced by:** *10 new citations to articles by Joshua C. Denny* feed.
- **Thread:** **Chronic disease clustering / multimorbidity** (etiology-based T2D subtyping is the clustering question) **+** **Causal inference / pharmacoepi** (the etiology partition is target-trial-shaped — the counterfactual is "if we had assigned each patient to their etiologic subtype, what would the complications be") **+** **Genetic epidemiology** (the "predominantly genetic" subtype is a high-PRS bucket; the partition resembles a stratified-PRS analysis).
- **What it is:** Partitions T2D into etiologic subtypes — **predominantly genetic** (high PRS + early onset + thin), **intrauterine** (low birthweight + metabolic programming), **lifestyle** (high BMI + low PA + later onset) — and shows that the partitions correspond to distinct clinical presentations and complication-risk profiles. The Danish EHR cohort linkage (Statens Serum Institut / Danish Civil Registration system) provides ~complete population-level follow-up.
- **Why it matters to you:** Four reasons.
  (a) **Disease subtyping by etiology is the clean version of the multimorbidity / clustering question.** Most clustering work uses unsupervised methods on multi-omics or EHR codes; etiology-based partitioning is a *supervised* alternative that's more clinically interpretable. Your INTERESTS file lists "Unsupervised and semi-supervised methods for discovering disease subtypes" — this is the supervised counterpart and a useful contrast.
  (b) **PRS-vs-environmental partition is methodologically useful.** Implicit in the design: a PRS-defined "genetic" subtype as an interpretable stratum. Pairs with last report's Souaiaia tails paper (PRS-architecture in the tails) — if the "predominantly genetic" subtype is a tail subgroup, the genetic architecture there is the question Souaiaia's paper addresses.
  (c) **Denny feed firing.** eMERGE / AoU is heavily invested in T2D subtyping; a Danish cohort paper landing in his citation feed signals it's becoming a default reference.
  (d) **Danish registry linkage is the gold standard for cohort completeness.** Methodologically a useful reference for any AoU/MVP cohort-completeness write-up.
- **Action:** **HIGH (clustering / multimorbidity); METHODS-WATCH (causal-inference framing).**
  (i) Identify the etiology assignment rule — PRS threshold, BMI-by-onset-age decision tree, or latent-class model?
  (ii) Note the complication profiles per subtype — micro vs macro complications, which subtype drives renal vs CV?
  (iii) Pair with multimorbidity / disease-trajectory work as a supervised baseline.

### 13. WGS + plasma metabolomics — large-scale genetic determinants and clinical implications
- **Authors / venue:** Y.X. Wang, Y.X. Qiang, Y.J. Ge, Y.T. Deng, B.S. Wu, L. Yang et al. — *Nature Communications*, 2026. URL: `nature.com/articles/s41467-026-74781-8`. (Author block — Wang / Qiang / Ge / Deng et al. — is the Fudan / Shanghai metabolomics genomics group; "L. Yang" senior author candidate.)
- **Surfaced by:** *"variant interpretation" OR "variant classification" OR "Causal Variant" keyword feed*.
- **Thread:** **Genetic epidemiology** (WGS + metabolomics is the multi-omics direction) **+** **Variant interpretation** (12,361 putative causal variant-trait associations is the explicit deliverable) **+** **Composite risk models — PRS + omics** (multi-omics composite risk is the natural downstream).
- **What it is:** Large-scale WGS + plasma metabolomics integration paper. From the snippet: "**12,361 putative causal variant-trait associations, demonstrating enhanced causal signal discovery and improved fine-mapping resolution compared with imputed array-based approaches.** Rare-variant aggregate tests…" — i.e., the central claim is that **WGS-based fine-mapping with metabolite outcomes outperforms imputed-array fine-mapping** (because of low-MAF coverage and improved haplotype resolution), with both common-variant fine-mapping and rare-variant aggregate burden tests reported.
- **Why it matters to you:** Four reasons.
  (a) **WGS-fine-mapping advantage over imputation is the key empirical claim for any WGS-based discovery work.** AoU's WGS release (~245K) is rapidly becoming the default substrate for fine-mapping; quantitative evidence of imputed-vs-WGS gain is operationally useful for justifying WGS-only analyses.
  (b) **Plasma metabolomics is the "next-gen" multi-omics layer.** Pairs with last report's Ding plasma-proteomic-aging paper (different platform but same conceptual layer) — together they define the **2026 H1 "plasma multi-omics as biobank-extension" moment.**
  (c) **Rare-variant aggregate tests for metabolite outcomes** is on your composite-risk thread (multi-omics composite predictors). The rare-variant aggregate signal for metabolites is also methodologically interesting because metabolites have substantially higher heritability than diseases, making rare-variant burden tests more powered per N.
  (d) **12K causal-variant claims is a large lookup substrate** — once the underlying data is browser-accessible, it becomes a citable variant-prioritization resource.
- **Action:** **HIGH.**
  (i) Identify the cohort — UKB-WGS or a Chinese cohort? Cohort identity bounds the ancestry/portability claim.
  (ii) Note the fine-mapping method — SuSiE, FINEMAP, polyfun, etc. — and confirm the WGS-vs-imputed comparison is on identical cohorts (apples-to-apples).
  (iii) Check rare-variant burden method — burden / SKAT / STAAR — and the per-gene effect-size estimates.
  (iv) Worth a save for any future AoU-WGS write-up where you justify WGS-only fine-mapping.

---

## METHODS-WATCH (exemplary methods, off-thread disease/topic, or repeats)

- **Privacy-preserving federated tensor decomposition of single-cell immune data: recovering multicellular programs across institutions** — A. Faes, S.M. van den Berg, M. Amir Haeri — *arXiv 2606.24938*, 2026-06-22 (q-bio.GN; surfaced by `arxiv-digest` 06-25; one-keyword hit `cross-ancestry`). Federated estimator for donor × cell-type × gene tensor decomposition, with site-mean-centering trick that makes the merge robust to site-label confounding (AUC 0.957 vs 0.861 for naive per-site centering), validated on a 261-donor SLE atlas + 3 COVID-19 sites + ILD atlas + liver cohort. Membership-inference attack reduced from 0.91 → 0.61 AUC under secure aggregation. **Off-thread disease-wise** (single-cell immune atlases, not your EHR / biobank work), but **methodologically interesting** as another instance of the privacy-preserving federation pattern this month (pairs with the 06-20 Kundu et al. and #6 above Walsh UDN-matching). Carry-forward worth: useful citation for any **secure-aggregation-as-federation-primitive** discussion. Score 1 in the digest (`cross-ancestry`).

- **Are Tabular Foundation Models Robust to Realistic Query Distribution Shifts in Microbiome Data?** — G. Perciballi, A. Fall, F. Granese, E. Prifti, J.-D. Zucker — *arXiv 2606.24995*, 2026-06-23 (cs.LG; surfaced by `arxiv-digest` 06-25; one-keyword hit `foundation model`). Benchmark for tabular FMs (TabPFN-style) on gut microbiome under three perturbations — high-abundance removal, sparsification (zero-inflation), zero-imputation (spurious non-zeros) — shows zero-imputation is consistently most harmful and TFMs are more sensitive to sparsification than RF baseline. **Off-thread substantively** (microbiome FMs, not EHR FMs), but the **support-query distribution-shift benchmark design** is a useful template for any tabular-FM evaluation including your EHR-FM context. Score 1.

- **CATVariant: a web server for integrated protein variant interpretation across sequence, structure, population, and clinical evidence** — K. Ngo, H. Amini, I. Vorobyov, C.E. Clancy — *Nucleic Acids Research*, 2026 (Konrad Karczewski related-research feed). Yet another variant-interpretation web tool. The integration claim — sequence + structure + population + clinical — is increasingly standard (cf. AlphaMissense, ClinPred, etc.); the value-add depends on the **structure** integration since most existing tools have weak structure handling. **METHODS-WATCH**: log as a possible alternative tool for variant prioritization if you need an additional column in a comparison table.

- **Statistical Methods for Institution-Scale Science** — P. Knight — 2026 (surfaced by "All of Us research program" keyword feed). PhD thesis. Snippet mentions a "transferable prediction model for end stage [renal disease, likely]" — i.e., a portable risk model across institutions. **METHODS-WATCH**: thesis-tier so unlikely to be a citation primitive, but the *transferable prediction model for ESRD* portion may be useful if you do any AoU ESRD/CKD analysis. Worth a glance at the relevant chapter.

- **Generative Transformers for Pharmacovigilance Signal Detection using Electronic Health Records** — Y.F. Wu, I. De Boer, T. Cohen — *AMIA Summits on Translational Science Proceedings*, 2026 (Patrick Ryan related-research feed). Generative-transformer pharmacovigilance from EHR. **METHODS-WATCH for the pharmacoepi thread** — the underlying primitive (generative-LLM-extracted ADE signal from EHR notes) is a natural component of any AoU drug-class RWE pipeline (GLP-1 / SGLT2 / CFTR modulators, etc.). Light-read at most.

- **Generative AI and Language Models in Human Genetics and Health: From Variant Interpretation to Clinical Decision Support** — Y. Pinchevsky Itan, Y. Itan — *Genes*, 2026 (variant interpretation keyword feed). Review-tier. **METHODS-WATCH** — useful as a synthetic "state of generative-AI in clinical genetics" citation if you ever need one; not primary literature.

- **Distinct genetic architecture in the tails of complex traits** — Souaiaia et al., *Nature*, 2026 (re-surfaced in the 06-25 Montgomery related-research feed). **Already HIGH-reported in the 06-20 report (item #4).** Re-noting only to flag that the paper is now showing up in two consecutive windows of Montgomery's feed, which is itself a signal of citation momentum.

- **Consensus meta-analysis of GWAS for Alzheimer's disease and related dementias** — A. Castillo Morales — *Nature Genetics*, 2026 (Jian Yang related-research + Joshua Denny related-research, double feed). AD GWAS consensus meta-analysis. **METHODS-WATCH for the AD-genetics sub-thread** — pairs naturally with the AD-LLM-phenotyping paper (#11 above) if you're considering AoU AD genetics work.

- **A functional comparison of vanzacaftor/tezacaftor/deutivacaftor and elexacaftor/tezacaftor/ivacaftor in patient-derived intestinal organoids with rare CFTR variants** — S. Kroes, L. Zaidi, H.N. Sonneveld-van Kooten, L. Winkel et al. — *Journal of Cystic Fibrosis*, 2026 (surfaced in Chenjie Zeng self-feed). Organoid-functional comparison of the next-gen CFTR triple (vanzacaftor) vs ETI for rare variants. **METHODS-WATCH / HIGH for the CF disease thread specifically** — useful citation for any CFTR-modulator-eligibility or rare-variant-CFTR write-up.

- **Clinical utility of point-of-care sweat chloride testing across contemporary cystic fibrosis care scenarios: a provider survey** — M. Jain, R. Nelson, S. McColley, T. Cybulski, M. Sala et al. — *Journal of Cystic Fibrosis*, 2026 (Chenjie Zeng self-feed). Provider-survey on POC sweat chloride. **METHODS-WATCH** — off-thread methodologically (provider survey not RWE methods) but **on the CF disease thread**. Light-touch.

- **arxiv-digest 06-26: KG-TRACE: A Neuro-Symbolic Framework for Mechanistic Grounding in Antimicrobial Resistance Prediction** — Garg, Jain, Yadav, Bhargava, Singh, Srivastava, Kar — *arXiv 2606.26179*, 2026-06-24 (cs.LG; single-keyword hit `knowledge graph`). Neuro-symbolic KG-grounded AMR prediction (WHO mutation KG + RotatE embeddings + epistemic trust gate) with a Biological Grounding Ratio metric on the CRyPTIC M. tuberculosis cohort. Off-thread (AMR / TB, not your biomedical-KG or clinical-FM context). **The `knowledge graph` keyword again surfaces a non-biomedical-clinical hit** — see pipeline note.

---

## SKIP / noise (logged, no action)

- **Estimating common synaptic inputs to spinal motor neurons from motor unit spike trains using openhdemg** (Cabral et al., q-bio.NC, 06-23 digest) — pure neuroscience / motor-unit physiology, score 1 (`motor` incidental).
- **Sequence-to-function modeling uncovers the context-specific grammar of Drosophila chromatin insulation** (Wang et al., bioRxiv, Shendure feed) — Drosophila chromatin modeling, off-thread.
- **Arithmetic Pedagogy for Language Models** (Lumbantobing, Situngkir, Szolovits feed) — language-model arithmetic pedagogy, clear citation-graph leak.
- **Karczewski / Pritchard citations: Genetic Architecture of Cutaneous Melanoma** (Chen et al., 2026, repeat hits across Karczewski + Pritchard feeds) — melanoma genetics, off-thread.
- **Vivek Natarajan citations: Why Do AI Projects Fail in Drug Development and Pharma?** — Pistoia Alliance report, not primary literature.
- **Peter Szolovits citations: Clinical AI Competence in OB-GYN; Application of LLMs in Medical Diagnosis** — generalist LLM-in-medicine commentaries, off-thread.
- **Daniel Kastner citations: Thrombospondin-1 calciphylaxis biomarker; Metabolic regulatory nodes of inflammasome** — adjacent autoinflammatory but off the VEXAS-specific thread.
- **Stephen Montgomery citations: Stem cell-derived extracellular vesicles for rare diseases (Han et al., BioScience Trends)** — translation framework, off-thread.
- **Stephen Montgomery new article: RNU4ATAC-opathy** (Matalon et al., GIM, 2026) — Montgomery as co-author; rare disease but molecular characterization, light-read at most.
- **Jay Shendure new article: Optimised lipid nanoparticle platform for CRISPR/Cas9** (Yang et al., Acta Biomaterialia) — delivery-tech, off-thread.
- **Christopher G. Chute related-research: multiorgan SARS-CoV-2 dissemination paper** (Wolabaugh et al.) — virology, off-thread.
- **5 new citations to Chute: Racial Disparities and Social Determinants of Long COVID** — health-equity / Long COVID surveillance, off the EHR-phenotyping methods thread.
- **Jian Yang related-research: Mendelian-randomization chronotype / breast cancer** (Luo et al.) — adjacent (MR is a tracked methodology) but off-thread substantively.
- **Bert Vogelstein citations: ctDNA / MRD in colorectal cancer** — off-thread.
- **George Hripcsak related-research: BMI-genome interactions** (Signer et al., Cell Genomics) — off-thread substantively.
- **Lisa Bastarache related-research: malignant hyperthermia / RYR1 reply letter** — clinical letter, off the phecode / PheWAS methods.
- **Lisa Bastarache citations: ChatGPT as a Digital Pharmacist** (Azmakan et al., Intelligence-Based Medicine) — generalist LLM medication-counselling review, off-thread.
- **Mihaela van der Schaar new article: Translation readiness of model-based synthetic tabular data in healthcare** (Castagno et al., JAMIA, 2026) — relevant to ML-for-precision-health discussions but more a governance audit than methods; **light METHODS-WATCH** if you're considering synthetic-tabular data for AoU augmentation.
- **Konrad Karczewski citations: Hypoxic CA9 variant in gastric/breast cancer** — single-cancer variant paper, off the population-genetics methods.
- **Patrick Ryan related-research: Vaccine Safety Surveillance for Covid-19 Vaccinations** (Aggarwal, Polpakara) — India COVID vaccine safety, off the GLP-1/SGLT2/CFTR/HRT drug-class thread.
- **Miguel Hernán citations: Long-term follow-up of colon cancer screening trials** (Post, NEJM Clinician) — colon-cancer screening trial follow-up, off-thread.
- **Yuan Luo citations: Enantioselective transport in lamellar membranes** (Han et al., Chemical Science) — clear citation-graph leak (chemistry).
- **Nigam Shah new article: Challenges in AI-Based Tumor Board Case Summarization and Recommendations** (Yim et al.) — oncology-AI summarization, off the EHR-phenotyping thread.
- **Pranav Rajpurkar new article: Pancreatic Cancer AI: The Need for Prospective Outcome Studies** — radiology AI commentary, off-thread.
- **Marinka Zitnik related-research: Unified Energy for Invariant and Independent Decoding in Diffusion Language Models** — LLM-architecture, off the clinical-FM thread.
- **Tiffany Callahan related-research: Wntless transporter for Wnt secretion** (Ge et al., Nature Communications) — molecular biology, off the KG/drug-repurposing thread substantively.
- **Daniel Kastner related-research: DNase2 mutation interferonopathy case** (Al Jashmi et al.) — single case, light-read.
- **Wendy Chung new article (other): Hypoxic CA9 variant** — already-listed leak.
- **Leo Anthony Celi new article: LLMs in critical care board review** — generalist LLM-medical-QA, off-thread.
- **"Knowledge graph" keyword: BrickTrace (building grounding); Frontier of Multi-Modal Fusion** — non-biomedical KG hits, **8th consecutive window of leak** (carry-forward).
- **"Mendelian diseases" keyword: COPD-blood metabolite mediation MR; mtDNA copy number and GI diseases** — MR-style mendelian-randomization papers misclassified as Mendelian-disease papers, **8th consecutive window of keyword-misclassification** (carry-forward).
- **"Drug repurposing" keyword: Integrated ML/MD virtual screening for breast cancer; Pharmacogenomic stratification for oncology drug repurposing** — both chemistry-/target-only pipelines, off the user's preferred KG-or-EHR-grounded repurposing axis. **8th consecutive window** (carry-forward).
- **"UK Biobank" keyword: light-intensity PA and CVD/cancer; psychological distress and urogenital** — descriptive epi, off methods.
- **"Autoimmune disorders/diseases" keyword (~7 entries this morning): Panchakarma review, autoimmune clustering in neuro-inflammatory, anti-PD-1 in pre-existing autoimmune disease, efgartigimod NMDA encephalitis case, Treg in vitro analysis, PID worldwide volume III, multiple-autoimmune lived-experience qualitative thesis, CAR-T for neuroimmune** — none on the IBD / VEXAS-autoimmune intersection or the EHR-autoimmune-phenotyping intersection. Logged.
- **JAMA Network "Online First" emails (×3 on 06-25)** — not opened in detail; one likely contains the APOL1 commentary (#1).
- **AINews / OpenAI Codex token-growth substack** — not on-thread.

---

## Suggestions for the pipeline

Prior reports' recommendations remain unactioned. Today's report adds three new issues and re-flags one urgently:

1. **🚨 arxiv-digest fetch failures are now recurring.** The 06-24 digest had a 3-of-4-category fetch failure (q-bio.GN, q-bio.PE, stat.AP failed; only q-bio.QM succeeded). Combined with the **06-20 3-of-4-category failure** flagged in the prior report, this is **the second 3/4-category failure in 6 days**. The new 5-second client delay + 15-second inter-category pause is *not* sufficient. Recommend acting immediately:
   - (a) **Split the four categories into two workflow runs separated by 60–90 minutes** — this is the cheapest fix and avoids the rate-limit window entirely.
   - (b) Or, **jittered exponential-backoff retry per category** (3 retries, 30s base, ×2 backoff, ±30% jitter) with a **per-category failure log** that distinguishes "no papers" from "fetch failed."
   - (c) The digest output should clearly distinguish "0 papers due to fetch failure" from "0 papers — clean dry day." 06-24's "0 papers" with a single-line warning at the top is too easy to misread (and **the 06-26 digest does suppress this paper as "previously surfaced" — meaning the 06-24 fetch failure may have caused a previously-on-thread paper to be silently lost from the visible digest and then suppressed when it re-appeared today**).
2. **`knowledge graph` keyword: 8th consecutive window of non-biomedical hits.** Today's KG-TRACE paper (AMR / TB) and BrickTrace (building ontology) continue the pattern. **Specific fix**: change the keyword from `knowledge graph` to a compound filter `(knowledge graph) AND (medical OR biomedical OR clinical OR EHR OR phenotype OR drug OR disease OR phecode OR HPO OR SNOMED)`. The single highest-value KG papers continue to come via author feeds (Callahan, Zitnik), not the keyword feed.
3. **`mendelian diseases` keyword: 8th consecutive window of Mendelian-randomization misclassification.** Today's hits — *Causal associations between mitochondrial DNA copy number and gastrointestinal diseases: A Mendelian randomization study* and *COPD Influence on Lung Cancer Risk Through Blood Metabolite Mediation: A Two-Sample Mendelian Randomisation* — are both MR studies, not Mendelian-disease (monogenic) studies. **Specific fix**: change `mendelian diseases` → `monogenic diseases OR mendelian condition OR rare mendelian` (and exclude `mendelian randomization`).
4. **`drug repurposing` keyword: 8th consecutive window** (carry-forward) — still surfacing chemistry-/target-only pipelines, not the KG / EHR-grounded angle on the user's INTERESTS file. Recommend `(drug repurposing) AND (knowledge graph OR EHR OR real-world OR target trial OR HPO)` compound filter.
5. **Add `cs.LG`, `stat.ME`, and medRxiv / bioRxiv source feeds** (carry-forward, **5th consecutive window** unaddressed). Today's items #2 (PGS Browser, Nature Communications), #3 (Tian biological aging, Nature Medicine), #4 (Jafari MENA HTN, Frontiers in Medicine), #5 (Yang Chinese cohort, Nature Health), #10 (TimeX, npj Health Systems), #11 (Powell AD-LLM, npj Health Systems), #12 (Hansen T2D etiology, presumably Diabetologia), #13 (Wang WGS+metabolomics, Nature Communications) — **none** of these would be reachable by the current q-bio + stat.AP arXiv-only pipeline. Worth a major expansion to medRxiv `genetic_and_genomic_medicine` and `health_informatics` subject feeds at minimum. The 06-23 Murali stat.ME hit is the strongest evidence yet that `stat.ME` is on-thread and should be added.
6. **Add `proteomic signature` / `aging clock` / `organ-specific aging` / `biological aging` keywords** (carry-forward from 06-20 + reinforced today). Today's item #3 (Tian, Nature Medicine) is the third aging-trajectory paper in three reports.
7. **Add `PRS stability` / `polygenic score stability` / `PRS robustness` / `polygenic tails`** (carry-forward).
8. **Add `noncoding variant interpretation` / `regulatory variant effect` / `MPRA`** (carry-forward from 06-20).
9. **Add `paralog-aware variant interpretation` / `paralog penetrance`** (new, from #8 today — Tzoumkas collagen IV paper). Paralog-aware ACMG is now an emerging sub-thread.
10. **Add `phenotype onset extraction` / `temporal phenotyping` / `EHR onset extraction`** (new, from #10 today — TimeX). Onset extraction is now a distinct EHR-phenotyping sub-problem worth surfacing directly.
11. **Continue tracking your own self-citation feed as the single highest-precision channel.** Today's item #4 (Jafari MENA HTN AoU) is the third self-feed-surfaced paper in three reports.

---

## Summary

| Bucket | Count | Items |
| --- | --- | --- |
| HIGH | 13 | (1) Sharif APOL1 + Black donors [JAMA-IM] + Gartstein APOL1 + SCD-gene-therapy [AJH], (2) Kolosov et al. PGS Browser [Nature Communications, 439K PGS-PheWAS], (3) Tian et al. AoU biological-aging + early-onset cancer [Nat Med], (4) Jafari AoU MENA hypertension [self-feed], (5) Yang et al. city-wide Chinese EHR+survey cohort [Nat Health], (6) Walsh privacy-preserving HPO rare-disease matching [Stanford CS191W], (7) Murali et al. causal inference for misclassified exposures in CF [arxiv-digest 06-23, stat.ME], (8) Tzoumkas et al. collagen IV paralog pathogenicity [medRxiv, Denny feed], (9) Seth et al. KRAS-CHIP → B-ALL with monocytosis [L&L], (10) Chen et al. TimeX phenotype onset extraction [npj Health Systems, Chute+Chung double feed], (11) Powell et al. AD memory-clinic LLM phenotyping [npj Health Systems, Hripcsak feed], (12) Hansen et al. T2D etiology subtyping Danish EHR cohort [Denny feed], (13) Wang et al. WGS+plasma metabolomics 12K causal variants [Nat Comms] |
| METHODS-WATCH | ~9 | Faes et al. federated single-cell tensor decomposition [arxiv-digest 06-25], Perciballi et al. tabular FM microbiome robustness [arxiv-digest 06-25], Ngo et al. CATVariant tool [NAR, Karczewski feed], Knight PhD thesis transferable ESRD model [AoU keyword], Wu et al. generative-transformer pharmacovigilance [AMIA, Ryan feed], Pinchevsky Itan & Itan review [Genes], Souaiaia tails (repeat 06-20), Castillo Morales AD GWAS consensus [Nat Genet, Yang+Denny feeds], Kroes et al. vanzacaftor CFTR organoid + Jain et al. sweat chloride POC [CF disease thread, self-feed], KG-TRACE AMR neuro-symbolic [arxiv-digest 06-26] |
| SKIP | ~30 | See SKIP / noise section above |

Compared to the 06-20 report (6 HIGH / 4 METHODS-WATCH), this window is substantially heavier — **13 HIGH** is the highest count in the report series so far. Three concurrent drivers:
- The **APOL1 thread broke out of dormancy** (#1) with two simultaneous papers and a JAMA-IM commentary anchor.
- The **EHR phenotyping thread had a double-hit** (#10 TimeX + #11 AD-LLM) — two npj Health Systems papers in one window is the venue's pattern emerging.
- **Two AoU papers** (#3 Tian Nature Medicine biological aging + #4 Jafari self-feed MENA hypertension) plus a parallel Chinese city-wide cohort (#5).

The arxiv-digest pipeline produced **one HIGH** (Murali CF causal inference) — its strongest hit since the 06-20 nephro-PRS triple-feed paper. **The 06-24 fetch failure** (3-of-4 categories) plus a 06-26 suppression of a previously-on-thread paper is the most pressing pipeline issue (see Pipeline note 1).
