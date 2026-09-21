# Research digest report — 2026-09-21

Triage of research-related email (Google Scholar alert feeds) + the local
`arxiv-digest` repo against the active threads in `INTERESTS.md` (PheWAS /
phecodes, EHR-linked biobanks, EHR phenotyping / OMOP, causal inference &
pharmacoepi, variant interpretation, genetic epi, CF / APOL1 / CHIP-VEXAS
/ LOY / IBD disease threads, EHR foundation models, KGs / ontologies,
drug repurposing, rare disease, ML for precision health, multimorbidity,
knowledge representation in EHRs).

Window: **2026-09-01 12:40Z → 2026-09-21 12:40Z** (~20 days since the last
research-digest report, covering twenty `arxiv-digest` cron runs and roughly
a dozen Google Scholar alert batches, headlined by the 09-14, 09-15, 09-17,
09-18–19 and 09-20–21 daily pushes).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-20.md`) | 09-01 → 09-20 daily crons | 20 daily runs. Dry days (0 papers): 09-03, 09-05–06, 09-08, 09-12, 09-13–15, 09-19–20. Active days: 09-01 (Mansouri Ghiasi storage-centric metagenomics dissertation), 09-02 (mudskipper locomotion — SKIP), 09-04 (natural disasters × nonprofit sector panel DML; Yu et al. location-invariant extremal QTE with IPW), 09-07 (Rajabli & Collins Alzheimer's MRI foundation feature extractor, LoRA), 09-09 (Snel & Schulz Cohen's-d attribution in UK Biobank normative age biomarkers; Wu et al. FUSE-RT HPLC retention-time FM), 09-10 (Lee/Rempala/Schnell Kalman filter for HT prevalence — METHODS-WATCH), 09-11 (Devarakonda **scDEFT** counterfactual drug-effect on 1.16M-cell harmonized IBD atlas; Hendrix et al. **geospatial FMs** capturing health-relevant dimensions of place beyond social-risk indices; Semchin et al. connectome-constrained Parkinson's subtypes), 09-16 (Wang et al. multiscale NTM-in-CF mucus mechanics; Zhang et al. scKITE knowledge-enhanced scFM), 09-17 (Fujita & Hattori **Information Set Emulation**: causal certificates for AI-derived EHR features, score 3), 09-18 (Ghasemnejad et al. **ReAct + RAG LLM agents for HPO-severity classification** using ACMG/ACOG criteria, 93.55% accuracy on 10,211 HPO terms; Csillag Finger & Possebom semiparametric contamination-bias with multi-valued treatments). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com arxiv-digest newer_than:22d` returned zero threads. Consistent with the last two reports: the pipeline commits its output to this repo rather than emailing PR/cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-21 batch, 07:55Z + 09-21 02:03Z) | 09-21 | 40+ feeds fired across two waves. HIGH-item authors: Miguel Hernán (Turchin BMJ 2026 **SGLT-2 / GLP-1 renal outcomes TTE**; NEJM colonoscopy interval RCT), George Hripcsak (Bakken JAMIA memorial for Clem McDonald with FHIR-interoperability framing; Zitnik et al. Cell **World models for biomedicine**; Sorka et al. JAMIA **DiagnosticXchange** clinical-AI evaluation framework; Basu JAMIA **institutional data commons federated DUC-aware architecture**), Lisa Bastarache citations-to (Johnson et al. JACC Case Reports **PheRS-triggered e-visit pathway for TTR V142I**; Luo et al. PLOS Medicine **accelerometer-derived real-world sleep stages × PheWAS UK Biobank**), Lisa Bastarache new-related (Zhang et al. medRxiv **TorchGWAS2** cost-effective phenome- and genome-wide association testing in related samples; Bai et al. Orphanet JRD **RYR1 VUS → pathogenic** malignant-hyperthermia reclassification; Ward et al. medRxiv **rare extreme PRS strongly indicate AD risk**), Chenjie Zeng new-related (Lawandos & Sodhi *Pediatric Research* early CFTR modulation in preschool CF; Aliukonyte et al. ERJ Open Res bronchial segmental heterogeneity of ETI response; Selvadurai et al. iScience anti-inflammatory + phosphorylation effects of ETI; Merino et al. Annals ATS mental health safety profile of CFTR modulators from French pharmacovigilance + VigiBase), Konrad Karczewski citations-to (Sun et al. Nat Commun **cervical spinal cord GWAS in 80k UKB**; Lopez-Balastegui et al. Diabetologia **GPCRVP score for GLP1R variant impact prediction**; Sun et al. Nat Commun **genome-wide skin pQTL mapping**), Joshua C Denny citations-to (Sun et al. Nat Commun skin pQTL, same paper), Joshua C Denny new-related (**Huang et al. medRxiv All of Us nicotine-use phenotypic + genetic characterization**; Kramer et al. medRxiv PTSD rare CNVs in WGS biobank; Celik Research Square AoU preoperative PRO-PH × AKI), Tiffany J Callahan new-related (Boceck et al. **npj Genomic Medicine aiDIVA hybrid AI for rare-disease diagnostics**; Thompson et al. bioRxiv **HeartVar LLM-assisted variant classification** for CVD cohorts), Yuan Luo citations-to (**Pollet & McDermott arXiv 2609.18134 rethinking methodological progress in health AI** — 12 algorithms re-implemented on MIMIC-IV), Peter Szolovits citations-to (Fu et al. npj Health Systems **multi-site benchmarking of geriatric-care construct extraction from EHRs**), Stephen B Montgomery new-related (Ma et al. medRxiv **long-read RNA-seq improves isoform + splicing outlier detection** in rare disease trios), Konrad Karczewski new-related (Kramer et al. medRxiv PTSD rare CNVs), Mark Gerstein new articles (Gerstein et al. **AI Scientists for Building Virtual-Cell Models**), Marinka Zitnik new articles (Noori/Fishman/Fang/Fesser/Zitnik *Cell* **World models for biomedicine** — field-defining reference), Vivek Natarajan citations-to (same World Models paper). Keyword feeds: "variant interpretation" (Boßelmann & May Hum Mol Genet somatic-mutation rates from cancer improve interpretation in epilepsy), "electronic health records" (**Wu et al. BMJ H&CI leveraging time-series EHRs with LLMs for CKD diagnosis in primary care**). |
| Google Scholar alerts (09-19 batch, 22:22Z) | 09-19 | Chenjie Zeng's **own poster** landed via multiple feeds: **C. Zeng, K. Raraigh, G. Cutting, J. Denny et al. — "Longitudinal disease burden and drug safety profiles of CFTR modulator therapy in cystic fibrosis: a real-world analysis from the NIH All of Us Research Program"** (Journal of Cystic Fibrosis, NACFC 2026 poster 646). Sibling CF/PGx hit in same feed: **Roye et al. J Cystic Fibrosis Poster 449 — assessment of altered CFTR modulator metabolism from prescribed concurrent medication + pharmacogenetic variation** (CYP3A4/5 modifiers). Also: Netten et al. medRxiv Lifelines accelerometry-derived PA/SB × health outcomes; Bihler et al. J Cystic Fibrosis in vitro responsiveness of **417 CFTR variants** to VNZ/TEZ/IVA; Park et al. Transl Psychiatry cross-ancestry OCD PRS transferability; **Wells et al. medRxiv All of Us pleiotropic + distributed neuropsychiatric effects of neurodevelopmental CNVs**; Ihara et al. active vs. non-active comparators × PPI mortality signal during ICI therapy (Ryan feed). |
| Google Scholar alerts (09-18 batch, 16:43Z + 23:18Z) | 09-18 | **Tsuo et al. Nature Genetics 2026** — *"All of Us diversity and scale yield context-dependent improvements in polygenic prediction"* (245,388 WGS). Also: Galderisi et al. JCEM continuous glucose monitoring before/after ETI in youths with CF; Abdullaev et al. Genes Uzbek cardiometabolic effect-allele frequencies (Central-Asian PGS-validation gap); Cook Psychoneuroendocrinology AoU intersectional-inflammation. |
| Google Scholar alerts (09-17 batch, 05:47Z) | 09-17 | **O'Malley et al. J Cystic Fibrosis — CFTR modulation alters pancreatic cancer cell growth: implications for cancer risk in CF** (Chenjie Zeng new-related feed, on-thread). Also: Stenger et al. Neuromuscular Disorders chronological patterns of pathogenic-variant distributions across muscular-dystrophy genes; Uwineza et al. Journal of Community Genetics genetic-services access in Rwanda; Ning et al. JNCI TTE adjuvant chemo after neoadjuvant FOLFIRINOX / gem-nab-paclitaxel in resected pancreatic cancer. |
| Google Scholar alerts (09-15 batch, 17:30Z) | 09-15 | Shi/Diemer/Swanson AJE **"Questions asked and, maybe, answered with Mendelian randomization"** — the Hernán-lineage MR interpretation paper. |
| Google Scholar alerts (09-14 batch, 08:24Z) | 09-14 | **Liu & Wang J Clin Epi 2026 — "Artificial Intelligence and Target Trial Emulation: Toward Scalable and Credible Real-World Evidence"** (Hernán citations-to; positioning review directly serving the agentic-TTE sub-thread). Also: Sarıoğlu J Clin Sleep Med Letter re: timing of GLP-1RA exposure in real-world CV analyses; Xie/Choi/Al-Aly eClinicalMedicine 2025–26 flu vaccine effectiveness in US veterans (TTE lineage). |
| Google Scholar alerts (09-01 → 09-13 rolling batches) | 09-01 → 09-13 | Rolling low-to-medium volume days between the 09-01 report and the 09-14 push. Notable single-hit items: Cystic Fibrosis Journal NACFC-abstract-supplement papers (rolling appearances across Chenjie Zeng feeds), assorted GLP-1 / SGLT2 pharmacoepi cardiometabolic papers via keyword feeds, and infrequent MR / MR-lineage citing-articles via the Hernán feed. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against the research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets. Where the poster's author line begins
> "C. Zeng, K. Raraigh, G. Cutting, J. Denny…" that is the account
> owner's own conference poster, not an alert about an unrelated author
> — attribution noted below.

---

## Executive summary (HIGH-priority studies, ranked)

Twenty-plus HIGH items surfaced this window, clustering into seven knots:

**Own-work knot (1 item, top of list).** *C. Zeng, K. Raraigh, G. Cutting,
J. Denny et al.* **"Longitudinal disease burden and drug safety profiles
of CFTR modulator therapy in cystic fibrosis: a real-world analysis from
the NIH All of Us Research Program"** — NACFC 2026 poster (JCF supplement,
poster 646). Directly serves the CF/CFTR and AoU biobank threads
simultaneously. This surfaced through both the "Chenjie Zeng — new
articles" feed (self-track) and cross-cited in the Joshua C. Denny
new-articles feed; nothing to review here beyond confirming the citation
is picked up correctly downstream.

**PGS × ancestry / All of Us biobank knot (2 items).** **Tsuo et al.
*Nature Genetics* 2026** — *"All of Us diversity and scale yield
context-dependent improvements in polygenic prediction"* using **245,388
WGS**; the definitive AoU-scale PRS-portability paper of the window,
directly serving `Biobanks with EHR linkage` and `Genetic epidemiology →
PGS × ancestry`. **Wells et al. *medRxiv* 2026** — pleiotropic and
distributed neuropsychiatric effects of neurodevelopmental CNVs in **AoU**;
the population-ascertained cohort version of severity-enriched clinical
ND-CNV studies, exact match for the PheWAS-thread's "penetrance under
population screening vs. clinically ascertained" framing.

**Pharmacoepi target-trial-emulation cluster (3 items).** **Turchin et
al. *BMJ* 2026** (Hernán feed) — head-to-head **SGLT-2 inhibitor vs.
GLP-1 receptor agonist renal-outcomes TTE in T2D with and without
albuminuria**; direct hit for the GLP-1 / SGLT2 drug thread. **Liu &
Wang *J Clin Epi* 2026** — positioning review on **AI + Target Trial
Emulation** as a scalable-RWE program; the reference-frame paper that
sits under the Chou/Kallus `oci-agent` and Netflix-production framing in
`INTERESTS.md`. **Shi, Diemer & Swanson *AJE* 2026** — *"Questions asked
and, maybe, answered with Mendelian randomization"*; the Hernán-lineage
interpretation piece that pairs with **drug-target MR** sub-thread and
usefully sharpens what MR estimands actually deliver (versus what they
are asked to deliver in the drug-target-MR literature).

**EHR foundation-model & AI-for-EHR cluster (5 items).** **Noori, Fishman,
Fang, Fesser, Zitnik *Cell* 2026** — *"World models for biomedicine"*; the
field-defining framing reference for cross-scale (molecular → cellular →
tissue → clinical) world models simulating interventions. Positions as a
"digital-twins from EHR data" companion to the Zhang/Ideker/Oermann
consortium reference already tracked in `INTERESTS.md`. **Wu et al. *BMJ
Health & Care Informatics* 2026** — leveraging **time-series EHRs with
LLMs for CKD diagnosis in primary care**; on-brand `EHR foundation models
+ EHR phenotyping` intersection paper. **Fu et al. *npj Health Systems*
2026** (Szolovits feed) — a **multi-site benchmarking framework for
scalable extraction of geriatric-care constructs from EHRs**; the
representation-portability audit paper that pairs with the ACT audit and
the scContam / MIA-scFM contamination protocols. **Pollet & McDermott
arXiv 2609.18134** (Yuan Luo feed) — *"Rethinking How We Evaluate
Methodological Progress in Health AI"*; **12 algorithms re-implemented in
a shared evaluation framework on MIMIC-IV** and a second dataset — a
methods-hygiene paper that directly supports the pretraining-contamination
audit sub-thread. **Fujita & Hattori arXiv 2609.17777** (local
`arxiv-digest`, score 3) — *"Information Set Emulation: Causal
Certificates for AI-Derived EHR Features"*; introduces typed lifts and
auditable causal certificates for AI-extracted features under a locked
target trial with cross-fitted AIPW estimation, distinguishing empirical
and population targets. Sits at the exact intersection of `EHR foundation
models` × `causal inference` × `knowledge representation in EHRs`.

**PheRS / phecode infrastructure knot (2 items).** **Johnson, Sarkar,
Kornblau, Baik et al. *JACC Case Reports* 2026** (Bastarache citations-to
feed) — a **PheRS-triggered e-visit pathway to capture TTR V142I in a
heart-failure population**; the ATTRv V142I variant present in ~4% of
African-American individuals with heart failure, exposed by phenotype-risk
scoring and routed through an operational care-pathway trigger. Direct
hit for the `PheWAS / phecode infrastructure` thread and for
`Applications to prioritize → computable phenotyping / PheKB / PheValuator`,
now in a decision-supported clinical form (not just a discovery
instrument). **Zhang et al. medRxiv 2026 — TorchGWAS2** (Bastarache
new-related feed) — cost-effective PheWAS + GWAS on related samples
(linear-mixed-model based, GPU-accelerated); the infrastructure
underpinning for the PheWAS-scaling sub-thread. Pairs directly with the
Bastarache-lineage lift of PheWAS at biobank scale.

**Variant interpretation / rare-disease diagnostic knot (5 items).**
**Ghasemnejad et al. arXiv 2609.19569** (local `arxiv-digest`, score 2)
— *"Large Language Model Agents for Evidence Based Genetic Disease
Severity Classification"*: a **ReAct + RAG agent** applied to **10,211
HPO terms**, using **ACMG-endorsed severity guidelines** + ACOG
quality-of-life criteria, PubMed retrieval, and independent claim
verification. 93.55% phenotype-level accuracy (MCC 0.9237), 82–91% claim
support, 95.2% concordance with Mackenzie's Mission gene list. Direct
hit for the **auditable HPO-driven diagnostic benchmarks** sub-thread
prioritized under `Rare disease` (analogous to GraphRareBench framing) and
for `Variant interpretation → ACMG-AMP`. **Boceck et al. *npj Genomic
Medicine* 2026** (Callahan feed) — **aiDIVA hybrid AI for rare-disease
diagnostics** using evidence-based + ML + LLM signals; on-thread rare-
disease diagnostic tool. **Thompson et al. bioRxiv 2026** — **HeartVar
LLM-assisted variant classification** for CVD cohorts (28 criteria, 22
databases). **Bai et al. *Orphanet JRD* 2026** — reclassification of
RYR1 VUS `c.7108_7109delinsAAGCC (p.Gly2370delinsLysPro)` to pathogenic
for malignant hyperthermia; a case-study exemplar of the ACMG reclassification
loop and a bridge to Lichtenberger's *Anesthesiology* 2026 (previous
window). **Boßelmann & May *Hum Mol Genet* 2026** — **mutation-rate
estimates + somatic variants from cancer improve variant interpretation
in epilepsy**; portable across other Mendelian-disease interpretation
loops.

**CFTR modulator disease-thread knot (5 items).** **O'Malley et al. *J
Cystic Fibrosis* 2026** — CFTR modulation alters pancreatic-cancer-cell
growth and signaling; direct implications for **cancer risk in CF** and
a clean bridge from CFTR pharmacoepi to oncological risk. **Merino et
al. *Annals ATS* 2026** — mental-health safety profile of CFTR modulators
from the French pharmacovigilance database + VigiBase; the safety-signal
paper that pairs with the persistence / discontinuation sub-thread.
**Aliukonyte et al. *ERJ Open Research* 2026** — bronchial-segmental
heterogeneity of responsiveness to ETI in CF (CT ↔ BAL inflammation);
representation of within-patient response heterogeneity. **Selvadurai
et al. *iScience* 2026** — anti-inflammatory + phosphorylation effects
of ETI in young children with CF. **Roye et al. *J Cystic Fibrosis* 2026
Poster 449** — **altered CFTR-modulator metabolism from prescribed
concurrent medication + pharmacogenetic variation (CYP3A4/5)**; this is
the pharmacogenomic-modifier-of-medication-persistence sub-thread's CF
instantiation, exactly the direction `INTERESTS.md` calls out under
`Causal inference and pharmacoepidemiology`.

---

## HIGH — Detailed reports

### 1. C. Zeng, K. Raraigh, G. Cutting, J. Denny et al. — Longitudinal disease burden and drug-safety profiles of CFTR modulator therapy in cystic fibrosis: a real-world analysis from the NIH All of Us Research Program
- **Venue:** *Journal of Cystic Fibrosis* 2026 (NACFC 2026 abstract supplement, poster 646).
- **Threads served:** `Specific disease threads → CF/CFTR`; `Biobanks with EHR linkage → All of Us`; `Causal inference and pharmacoepidemiology` (drug-safety, real-world outcomes); `EHR phenotyping & OMOP` (phecode-based longitudinal burden).
- **Note:** This is the **account owner's own poster**, surfaced through the self-tracking Chenjie Zeng feed and mirrored in the Joshua C. Denny new-articles feed. No triage action needed beyond confirming that the AoU-based longitudinal CFTR modulator work has posted publicly. The paired feed hit on Roye et al. Poster 449 (below) is the direct methodological neighbor.

### 2. Tsuo, Shi, Ge, Mandla, Hou, Ding et al. — *All of Us* diversity and scale yield context-dependent improvements in polygenic prediction
- **Venue:** *Nature Genetics* 2026.
- **Threads served:** `Biobanks with EHR linkage → All of Us`; `Genetic epidemiology → PRS, cross-ancestry portability`; `Composite risk models`.
- **Why it matters:** Uses **245,388 whole-genome sequences** (the largest ancestry-diverse WGS-linked EHR cohort at time of publication) to characterize *context-dependent* improvements in polygenic prediction from ancestry diversity — the answer to the *"does AoU scale actually deliver on the portability-lever promise?"* question that has been open since the Martin/PRIMED cross-ancestry portability literature. Immediate pair with **Nagpal & Gibson *Nature Genetics* 2026 pervasive PGS × exposure interactions** (previously tracked) and **Zhu et al. Research Square 2026 partitioned BP-PRS** (previous window). Together they close the "PGS is not one instrument" story with a large-N ancestry-and-context deconvolution.
- **Read-order priority:** Read first — this is a Nature Genetics AoU flagship this window. Confirm whether the paper uses PheWAS / phecode-based downstream case ascertainment (paired with the CohortDiagnostics / CohortContrast lineage from the previous report) or biobank-linked ICD-based codes only.

### 3. Turchin, Petito, Hegermiller, Chelliah et al. — Renal outcomes in people with type 2 diabetes with and without albuminuria treated with SGLT-2 inhibitors and GLP-1 receptor agonists: target trial emulation
- **Venue:** *BMJ* 2026 (Hernán new-articles feed — first author on the Hernán program register).
- **Threads served:** `Causal inference and pharmacoepidemiology → target trial emulation, GLP-1 RAs, SGLT2is`.
- **Why it matters:** Compares risk of renal deterioration under GLP-1 RA vs. SGLT-2i vs. other second-line T2D therapies, stratified by baseline albuminuria — the effect-modifier structure that was largely a subgroup analysis in Zhang et al. 2026 (previous window's Hripcsak-feed empirically-calibrated TTE) is here the primary axis. Read as a direct comparator against Zhang et al.: same drug classes, same outcome family, different framing (albuminuria as effect-modifier vs. negative-control calibration).

### 4. Liu & Wang — Artificial Intelligence and Target Trial Emulation: Toward Scalable and Credible Real-World Evidence
- **Venue:** *Journal of Clinical Epidemiology* 2026 (Hernán citations-to feed).
- **Threads served:** `Causal inference and pharmacoepidemiology → agentic / human-in-the-loop observational-causal-inference pipelines`.
- **Why it matters:** A positioning review reifying the AI-augmented TTE program that the Chou/Kallus `oci-agent` paper (previously tracked) advanced. This is the citation-frame paper — if you want a one-paragraph handoff to a reviewer for why the agentic-TTE sub-thread is a real research program, this is the citation.

### 5. Noori, Fishman, Fang, Fesser, Zitnik — World models for biomedicine
- **Venue:** *Cell* 2026.
- **Threads served:** `EHR foundation models → digital twins from EHR data`; broader modeling of intervention response.
- **Why it matters:** Positions "world models" (in the AI-simulation sense) as the multiscale framing that spans molecular → cellular → tissue → clinical levels and simulates responses under alternative actions. Companion citation for the Zhang/Ideker/Oermann *Cell* 2026 digital-twins-in-healthcare consortium reference already tracked, but from the AI side (simulate-what-if) rather than the healthcare-consortium side. This citation surfaced on **four separate feeds** in the 09-21 batch (Zitnik, Vivek Natarajan, Kai Wang, Hripcsak citations-to), which is a legitimate visibility signal for cross-community traction.

### 6. Wu, Zheng, He, Zuo, Zhang, Li, Luxia — Leveraging time-series EHRs with large language models for chronic kidney disease diagnosis in primary care
- **Venue:** *BMJ Health & Care Informatics* 2026 (keyword-feed hit on `"electronic health records"`).
- **Threads served:** `EHR foundation models`; `EHR phenotyping & OMOP`; `Knowledge representation in EHRs → NLP-derived representations from clinical notes`.
- **Why it matters:** Applied LLM-on-time-series-EHR to CKD diagnosis in a primary-care setting — a clinically-actionable end-point rather than a leaderboard task. Fits the `ML for precision health` HIGH-vs-SKIP filter as a tied-to-clinical-decision paper (who to escalate to nephrology). Read paired with the Fujita/Hattori "Information Set Emulation" arXiv preprint (item 8) — Wu et al. is the applied "we ran an LLM on time-series EHR features and got a good AUC" paper; Fujita is the "here is the causal-certificate architecture that says when those AI-derived features are admissible for causal claims" paper. Reading them in sequence is the productive move.

### 7. Fu, Kwak, Ahn, Lu, Yue, Wang, Liu et al. — A multi-site benchmarking framework for scalable extraction of geriatric-care constructs from EHRs
- **Venue:** *npj Health Systems* 2026 (Szolovits citations-to feed; also cited by Hongfang Liu new-articles feed).
- **Threads served:** `EHR foundation models → Pretraining-contamination audits`; `Knowledge representation in EHRs → Fidelity, portability, and audit of representations`.
- **Why it matters:** A multi-site benchmarking framework, applied to geriatric-care construct extraction, is exactly the representation-drift audit template that `INTERESTS.md` explicitly prioritizes ("representation choices drift across sites (BioVU vs. AoU vs. MIMIC vs. UKB), calibration under site shift, and audits of learned representations against clinical ground truth"). This paper is the geriatric-care instantiation of that audit template.

### 8. Fujita & Hattori — Information Set Emulation: Causal Certificates for AI-Derived EHR Features
- **Venue:** arXiv 2609.17777v1 (local `arxiv-digest` 2026-09-17, keyword hits `electronic health records`, `inverse probability`, `causal inference`, score **3**).
- **Threads served:** `EHR foundation models`; `Knowledge representation in EHRs → Applications to prioritize`; `Causal inference and pharmacoepidemiology → agentic / human-in-the-loop OCI pipelines`.
- **Why it matters:** Introduces a *typed lift* that attaches source evidence, clinical + recording times, decision-time availability, representation version, proposed causal roles, and unresolved ambiguity to AI-extracted EHR features under a locked target trial. Features with unresolved downstream roles are routed to compatible reporting or separate analyses. The "**observational fiber of causal worlds**" framing plus a squared-Chebyshev-radius-equals-residual-MMSE identity gives a target-specific measure of information ambiguity. Cross-fitted AIPW estimation under exchangeability, positivity, and nuisance consistency, with a compression-drift identity separating frame-presence, treatment-assignment, and outcome-observation roles.
- **Read-order priority:** This is a **methods paper of the kind you want to crib**. Even if the empirical experiments here are synthetic Phase-0-notes toy examples, the "causal certificate" abstraction is a legitimate portable primitive that would sit cleanly under the CFTR-modulator AoU work.

### 9. Pollet & McDermott — Rethinking How We Evaluate Methodological Progress in Health AI
- **Venue:** arXiv 2609.18134 (Yuan Luo citations-to feed).
- **Threads served:** `EHR foundation models → Pretraining-contamination audits`; methodological-rigor lens on health-AI benchmarks.
- **Why it matters:** **12 historical + recent algorithms re-implemented within a shared evaluation framework on MIMIC-IV plus a second clinical dataset** — the empirical answer to the "how much of health-AI progress is real vs. framework-choice-driven" question. Pair with the Fu et al. multi-site benchmark and with Sharma et al. (previous window) hematology-FM acquisition-shift audit.

### 10. Ghasemnejad, Argha, Grosser, Wang, Yang, Porntaveetus, Roscioli, Lovell, Aarabi, Alinejad-Rokny — Large Language Model Agents for Evidence-Based Genetic Disease Severity Classification
- **Venue:** arXiv 2609.19569 (local `arxiv-digest` 2026-09-18, keyword hits `acmg`, `human phenotype ontology`, score 2).
- **Threads served:** `Variant interpretation → ACMG-AMP variant classification`; `Rare disease → auditable HPO-driven diagnostic benchmarks`; `Knowledge representation in EHRs → NLP-derived representations`.
- **Why it matters:** Reasoning-and-Acting (ReAct) + Retrieval-Augmented Generation (RAG) agent, applied to classifying **10,211 HPO terms** using **ACMG-endorsed severity guidelines + ACOG quality-of-life criteria**, retrieving PubMed literature, generating interpretable reasoning chains, and independently verifying claims. **93.55% accuracy (MCC 0.9237)**; 82.6–91.4% claim support; gene-level severity aggregated across 8,738 pairs identifying 3,283 autosomal-recessive pairs with severe/profound presentations. External validation: 95.2% concordance with **Mackenzie's Mission** gene list. This is a **direct hit** for the `Rare disease → auditable HPO-driven diagnostic benchmarks with separable metrics for ranking vs. evidence coverage` sub-thread that `INTERESTS.md` calls out around GraphRareBench.

### 11. Boceck, Laugwitz, Sturm, Bezdan, Gschwind et al. — aiDIVA: hybrid AI for rare-disease diagnostics using evidence-based, machine-learning and language models
- **Venue:** *npj Genomic Medicine* 2026 (Tiffany J Callahan new-related feed).
- **Threads served:** `Rare disease`; `Variant interpretation`.
- **Why it matters:** Hybrid pipeline combining rule-based evidence, classical ML, and LLMs for rare-disease variant prioritization + clinical interpretation. On-thread for both `Rare disease diagnosis` and `Variant curation tooling` sub-threads (InterVar-lineage).

### 12. Johnson, Sarkar, Kornblau, Baik et al. — A Phenotype Risk Score–Triggered E-Visit Pathway to Capture TTR V142I in a Heart-Failure Population
- **Venue:** *JACC Case Reports* 2026 (Bastarache citations-to feed).
- **Threads served:** `PheWAS / phecode infrastructure`; `Applications to prioritize → computable phenotyping / PheKB / PheValuator`; `Specific disease threads` (cardiovascular ATTRv).
- **Why it matters:** TTR p.Val142Ile is present in ~4% of African-American individuals and is the most common cause of ATTRv in the United States — but is confirmed by genetic testing in only ~6% of eligible heart-failure patients, contributing to health disparities. This paper wraps a **PheRS trigger** around an **operational e-visit pathway** to close that diagnostic gap. Reading order: the paper is a *Case Reports* venue so it will be short — the value is the **workflow architecture**, not the outcomes. Pair with the earlier Lichtenberger *Anesthesiology* malignant-hyperthermia paper and with the Bai et al. Orphanet JRD RYR1 VUS-reclassification case (item 15 below) — the pattern of "PheRS → suspected variant → operational care-pathway trigger" is generalizable.

### 13. Zhang, Xie, Salehi nasab, Wang, Zhao et al. — TorchGWAS2: Cost-Effective Phenome- and Genome-Wide Association Testing in Related Samples
- **Venue:** medRxiv 2026-09-10 (Bastarache new-related feed).
- **Threads served:** `PheWAS / phecode infrastructure`; `Genetic epidemiology → GWAS scalability`.
- **Why it matters:** GPU-accelerated linear-mixed-model PheWAS + GWAS in related samples — the infrastructure paper for scaling PheWAS at biobank scale where sample relatedness (common in AoU with families, and in Estonian/FinnGen/Icelandic cohorts) has been a scaling bottleneck. Direct fit under the PheWAS-infrastructure thread.

### 14. Ward, Nelson, Katsumata, Fardo et al. — Rare extreme polygenic risk scores strongly indicate Alzheimer's disease risk
- **Venue:** medRxiv 2026-09-08 (Bastarache new-related feed).
- **Threads served:** `Genetic epidemiology → PGS residuals / polygenic-deviation designs, PGS tails`.
- **Why it matters:** Uses **PGS tails** (Souaiaia *Nature* lineage) to identify pre-symptomatic AD-high-risk individuals. Directly serves the "tails-and-residuals taxonomy of PGS as a discovery instrument" that `INTERESTS.md` prioritizes for `PGS residuals / polygenic-deviation designs`. Read paired with **Baya *AJHG* 2026** (previously tracked, misaligned-individuals framing) and **Vazquez *Genetics* 2026** (low-risk-group designs).

### 15. Wells, Zhao, Seshadri, Cavazos et al. — Pleiotropic and distributed neuropsychiatric effects of neurodevelopmental copy-number variants in the All of Us Biobank
- **Venue:** medRxiv 2026-09-13 (Chenjie Zeng new-related feed).
- **Threads served:** `PheWAS / phecode infrastructure → penetrance estimation for monogenic variants under population-screening vs. clinically-ascertained cohorts`; `Biobanks with EHR linkage → AoU`.
- **Why it matters:** ND-CNVs (e.g., 22q11.2, 16p11.2) have well-characterized associations in clinically ascertained cohorts with severe neurodevelopmental phenotypes. This paper asks the population-ascertained version of the same question in AoU — and the answer is the **pleiotropic, distributed effect pattern** rather than a single-syndrome one. This is exactly the "penetrance under population-screening conditions" experiment the PheWAS thread prioritizes, now for ND-CNVs. Pair with Lichtenberger et al. malignant hyperthermia and with Karczewski-lineage rare-variant work.

### 16. Huang, Romero Villela, Luo, Miller et al. — Phenotypic and genetic characterization of different modes of lifetime nicotine use in the All of Us Research Program
- **Venue:** medRxiv 2026-09-11 (Chenjie Zeng new-related feed + Joshua C. Denny new-related feed).
- **Threads served:** `Biobanks with EHR linkage → AoU`; `Genetic epidemiology → GWAS phenotype heterogeneity`.
- **Why it matters:** Extends prior nicotine / smoking GWAS beyond cigarette use to alternative modes (e-cigarettes, cigar, smokeless), which have distinct environmental / genetic architectures. Direct AoU biobank use with EHR-derived exposure phenotypes — exactly the study design under `Biobanks with EHR linkage → phenotype validation against EHR-derived outcomes`.

### 17. Bai, Lei, Luo, Xu — De novo RYR1 variant c.7108_7109delinsAAGCC (p.Gly2370delinsLysPro) causes life-threatening malignant hyperthermia: reclassification from VUS to pathogenic
- **Venue:** *Orphanet Journal of Rare Diseases* 2026 (Bastarache new-related feed).
- **Threads served:** `Variant interpretation → ACMG-AMP variant classification, splicing / RNA evidence for VUS resolution, LOFTEE and pLoF burden methods`; `Rare disease`.
- **Why it matters:** A concrete VUS-to-pathogenic reclassification case with functional + clinical evidence. Bridge citation between the Lichtenberger *Anesthesiology* 2026 malignant-hyperthermia paper (previous window) and the ongoing ACMG-reclassification loop. Companion for the LLM-agent HPO-severity paper (item 10) as the "here is what the classification actually looks like when it is done manually and correctly on a hard case" reference.

### 18. Ma, Weisburd, DiTroia, Romo, Covill et al. — Long-read RNA sequencing improves isoform and splicing outlier detection in whole blood from rare disease trios
- **Venue:** medRxiv 2026 (Stephen B. Montgomery new-related feed).
- **Threads served:** `Rare disease → data-driven reanalysis of unsolved cases`; `Variant interpretation → splicing / RNA evidence for VUS resolution`.
- **Why it matters:** Long-read RNA-seq resolves splicing-outlier detection failures that short-read RNA-seq misses — critical for the rare-disease diagnostic loop where splicing variants often live behind ACMG-uncertain VUS calls. Pair with Uria-Regojo et al. medRxiv 2026 (previously tracked) as the "reanalysis at 10k+ cohort scale" companion.

### 19. Boßelmann & May — Mutation rate estimates and somatic variants from cancer improve variant interpretation in epilepsy
- **Venue:** *Human Molecular Genetics* 2026 (`"variant interpretation" OR "variant classification"` keyword feed).
- **Threads served:** `Variant interpretation → ACMG-AMP variant classification`; `Rare disease`.
- **Why it matters:** Cross-domain transfer of mutation-rate estimates from somatic-cancer variant catalogs into germline epilepsy variant interpretation — the pattern is portable, and portable across the muscle-channelopathy / cardiomyopathy / rare-neurodevelopmental space too. Pair with the Ji et al. *Biology* 2026 QC-layer paper (previously tracked, somatic-mutation contamination of germline rare-variant scans) as the same problem viewed from the confounder-elimination side.

### 20. O'Malley, Keen, Thornell, Campbell, Prouty et al. — CFTR modulation alters pancreatic cancer cell growth and signaling: implications for cancer risk in cystic fibrosis
- **Venue:** *Journal of Cystic Fibrosis* 2026 (Chenjie Zeng new-related feed).
- **Threads served:** `Specific disease threads → Cystic fibrosis / CFTR`; `Causal inference and pharmacoepidemiology → CFTR modulators (Trikafta / ivacaftor)`.
- **Why it matters:** Directly relevant to the account owner's own CFTR-modulator AoU longitudinal-burden work (item 1) — cancer-risk under long-term CFTR modulation is one of the outstanding pharmacoepi questions in the modulator era. In-vitro mechanism paper, but the mechanism-to-real-world pipeline is what makes it a companion to a large-scale AoU pharmacoepi study.

### 21. Roye, Guimbellot, Abouelenein, Chalamalla — Assessment of altered CFTR modulator metabolism from prescribed concurrent medication and pharmacogenetic variation in people with cystic fibrosis
- **Venue:** *Journal of Cystic Fibrosis* 2026 (NACFC Poster 449; Chenjie Zeng new-related feed).
- **Threads served:** `Causal inference and pharmacoepidemiology → pharmacogenomic modifiers of medication persistence`; `Specific disease threads → CF/CFTR`.
- **Why it matters:** This is the CFTR-modulator instantiation of the pharmacogenomic-modifier-of-medication-persistence sub-thread `INTERESTS.md` explicitly calls out — **CYP3A4/5 pharmacogenetic variants + prescribed concurrent CYP3A4/5 modifiers** altering CFTR-modulator metabolism. Portable to statin discontinuation, GLP-1 RA persistence, and HRT persistence via the same CYP pathway.

### 22. Merino, Cohen, Ben Othman, Osmont et al. — Mental-health safety profile of CFTR modulators in pediatrics and adults: insights from the French pharmacovigilance database and from VigiBase
- **Venue:** *Annals of the American Thoracic Society* 2026 (Chenjie Zeng new-related feed).
- **Threads served:** `Causal inference and pharmacoepidemiology → CFTR modulator pharmacoepi, real-world outcomes`; `Specific disease threads → CF/CFTR modulator eligibility & psychosocial impact`.
- **Why it matters:** Mental-health adverse-event signals from CFTR modulators are the pharmacovigilance signal that has been building in the modulator-era CF literature. Pharmacovigilance-database disproportionality analysis (FAERS-cousin methodology on French PV + VigiBase); pairs with the O'Malley pancreatic-cancer mechanism paper (item 20) as the "long-term modulator safety" duo.

### 23. Lawandos & Sodhi — Early CFTR modulation and clinical outcomes in preschool cystic fibrosis
- **Venue:** *Pediatric Research* 2026 (commentary on Presti et al.; Chenjie Zeng new-related feed).
- **Threads served:** `Specific disease threads → CF/CFTR, modulator pharmacoepi, real-world outcomes`.
- **Why it matters:** Commentary on Presti et al.'s multicenter prospective study of lumacaftor/ivacaftor in preschool F508del-homozygous children — the pediatric extension of the modulator real-world literature.

### 24. Aliukonyte, Durfey, Kapnadak, Teresi et al. — Bronchial segmental heterogeneity of responsiveness to modulator therapy in cystic fibrosis: linking structural improvements on CT to inflammation in bronchoalveolar lavage fluid
- **Venue:** *ERJ Open Research* 2026 (Chenjie Zeng new-related feed).
- **Threads served:** `Specific disease threads → CF/CFTR modulator real-world outcomes`; `Machine learning for precision health → treatment-effect heterogeneity`.
- **Why it matters:** Within-patient heterogeneity in ETI response, characterized by segmental CT + BAL. The pattern of "modulator responds but doesn't fully resolve inflammation and structural damage" is the residual-disease question that drives adjunct-therapy pharmacoepi.

### 25. Selvadurai, Han, Keating, Graham et al. — Anti-inflammatory and phosphorylation effects of CFTR modulator triple therapy in cystic fibrosis
- **Venue:** *iScience* 2026 (Chenjie Zeng new-related feed).
- **Threads served:** `Specific disease threads → CF/CFTR modulator real-world outcomes`.
- **Why it matters:** Mechanistic anti-inflammatory + phosphorylation-signaling companion to Aliukonyte's structural / BAL paper. Read the two as a pair: same phenotype (residual inflammation), different modalities (imaging + BAL vs. molecular).

### 26. Galderisi, Marchiori, Weiss, Besançon et al. — Continuous glucose monitoring to track metabolic changes in youths with cystic fibrosis before and after initiation of ETI
- **Venue:** *Journal of Clinical Endocrinology & Metabolism* 2026 (Chenjie Zeng new-related feed).
- **Threads served:** `Specific disease threads → CF/CFTR, cystic-fibrosis-related diabetes (CFRD)`.
- **Why it matters:** Longitudinal CGM before/after ETI in preschool + school-age CF children — CFRD trajectory under early modulator initiation is a live pharmacoepi question given CFTR expression in pancreatic islets and the modulator-era prevalence shifts.

### 27. Snel & Schulz — Attributing Cohen's d: Training Data Attribution for Disease-Related Effects in Normative Age Biomarkers
- **Venue:** arXiv 2609.07729 (local `arxiv-digest` 2026-09-09; keyword hits `uk biobank`, `biobank`, score 2).
- **Threads served:** `Biobanks with EHR linkage → UK Biobank`; `Machine learning for precision health`; `Genetic epidemiology → normative-age biomarker framework`.
- **Why it matters:** Closed-form **influence-functional** attribution of case-control effect size (Cohen's d) to individual training samples in a UKB normative-age model. Removing the top 10% most-influential training samples **more than doubles the metabolomic-age effect for T2DM**, raises brain-age effect for MS by ~⅓, and recovers HbA1c as the operative marker in T2DM. Random-removal ablation confirms the gain is which-samples, not how-many. Ships as `pyinfluence`. Direct application: audit UKB / AoU normative-age model training cohorts for "healthy control" leakage of subclinical cardiometabolic disease.

### 28. Devarakonda — scDEFT: a deep-learning framework for drug-effect prediction and counterfactual reasoning
- **Venue:** arXiv 2609.10831 (local `arxiv-digest` 2026-09-11; keyword hits `inflammatory bowel disease`, `patient stratification`, score 2).
- **Threads served:** `Specific disease threads → Inflammatory bowel disease`; `Machine learning for precision health → treatment-effect heterogeneity, patient stratification`; `Causal inference and pharmacoepidemiology → counterfactual reasoning`.
- **Why it matters:** Single-cell drug-effect predictor treating a drug as a **conditioning operator** on cell representations via FiLM. Applied to a harmonized IBD atlas of **1.16 million cells, three cohorts, two drug classes**. Predicts state change at 45% of the baseline-to-reproducibility-ceiling headroom; stratifies responders pre-treatment at AUROC 0.70 (standard predictors: chance). This is exactly the IBD × treatment-effect-heterogeneity × counterfactual-prediction hit `INTERESTS.md` prioritizes.

### 29. Hendrix, Zhang, Heitzig, Bazemore, Rehkopf — Geospatial Foundation Models Capture Health-Relevant Dimensions of Place Beyond Conventional Social Risk Indices
- **Venue:** arXiv 2609.11689 (local `arxiv-digest` 2026-09-11, keyword hit `foundation model`, score 1).
- **Threads served:** `Machine learning for precision health`; `EHR foundation models` (cross-modal FMs); `Multi-omics-augmented PRS` (contextual analog).
- **Why it matters:** Uses four geospatial FM families on 2022 satellite data across **82,646 census tracts** to predict CDC PLACES 40-chronic-disease + health-behavior outcomes above and beyond ADI/SDI/SVI. Explains up to 54% of the variance left unexplained by conventional social-risk indices, largest gains for annual checkups, arthritis, and high blood pressure. Direct fit for the `Chronic disease clustering and multimorbidity` thread's cardiometabolic sub-focus and for augmenting spatial covariates in TTE-style causal pharmacoepi.

### 30. Bakken — Remembering Clement J. McDonald, MD: advancing healthcare interoperability standards
- **Venue:** *Journal of the American Medical Informatics Association* 2026 (Hripcsak citations-to feed).
- **Threads served:** `Knowledge representation in EHRs → Interoperability standards and their representational consequences`.
- **Why it matters:** Memorial + retrospective in JAMIA. Not a methods paper — but a useful field-shape reference for the FHIR / USCDI / C-CDA lineage citation stack.

### 31. Sun, Han, Gerring, Jackson, Bhalala et al. — Genetic architecture of MRI-derived cervical spinal cord morphology reveals sensory-motor axis and systemic disease associations
- **Venue:** *Nature Communications* 2026 (Konrad Karczewski citations-to feed).
- **Threads served:** `Biobanks with EHR linkage → UK Biobank`; `Genetic epidemiology → GWAS, IDPs`.
- **Why it matters:** Large-scale phenotyping of upper cervical spinal cord structure using brain MRI from **>80,000 UKB participants**, 179 independent GWAS signals. Fits the UKB-imaging × IDP-GWAS lineage that Feng et al. (previously tracked) extended cross-ancestry for depression.

### 32. Lopez-Balastegui, Lian, Gao, Gbahou et al. — The GPCRVP score reliably predicts the impact of GLP1R human variants on receptor function
- **Venue:** *Diabetologia* 2026 (Karczewski citations-to feed).
- **Threads served:** `Variant interpretation → variant classification`; `Causal inference and pharmacoepidemiology → GLP-1 RAs` (drug-target angle); `Genetic epidemiology → drug-target Mendelian randomisation`.
- **Why it matters:** A GPCR-specific variant-effect predictor for GLP1R missense variants — the drug-target-MR-triangulation companion for the entire GLP-1 pharmacoepi literature (item 3). Direct bridge: pharmacoepi TTE tells you the population effect of the drug class; drug-target MR + GPCRVP tells you the mechanistic effect of on-target modulation.

---

## METHODS-WATCH

- **Ilves et al. *Informatics in Medicine Unlocked* 2026 — CohortContrast** (Hripcsak feed, but the paper predates this window; carried forward from the previous report).
- **Sorka et al. JAMIA — DiagnosticXchange** (Hripcsak feed): open-source evaluation framework for clinical-AI diagnostic systems across accuracy, cost, time, invasiveness, physician effort, and safety-behavior dimensions. Off-thread on disease scope but the multi-dimension-scoring template is portable.
- **Basu JAMIA — Institutional data commons** (Hripcsak feed): federated Data-Use-Certification-aware architecture for secure data-use in biomedical data ecosystems. Off-thread day-to-day, but relevant background for the federated-EHR-causal-analytics sub-thread.
- **Ihara et al. — active vs. non-active comparators × PPI mortality signal during ICI therapy** (Patrick Ryan feed): comparator-choice sensitivity analysis in RWE, generalizable pattern.
- **Bihler et al. J Cystic Fibrosis — in vitro responsiveness of 417 CFTR variants to VNZ/TEZ/IVA**: builds the modulator-eligibility catalog for the next-generation triple combination — precondition for any AoU-scale modulator-eligibility pharmacoepi.
- **Wang et al. *q-bio.QM* 2026 — multiscale ABM + PDE model of NTM infection in CF**: mechanistic model, off-thread for pharmacoepi but a useful reference for CF NTM burden framing.
- **Wu, Han, Mito et al. arXiv 2609.07531 — FUSE-RT retention-time FM with Sim2Real transfer** (2026-09-09): off-thread on disease but the Sim2Real transfer pattern is portable to EHR-FM low-data-domain adaptation.
- **Rajabli & Collins arXiv 2609.05400 — Compact brain-age CNN + LoRA as a reusable AD foundation feature extractor** (2026-09-07): a low-parameter foundation-model transfer story that will be useful as a comparator for large-scale EHR-FM claims.
- **Zhang et al. arXiv 2609.14970 — scKITE knowledge-enhanced single-cell FM** (2026-09-16): only 179k pretraining samples (<0.5% of prior scFM training data), outperforms much larger scFMs via cell-annotation + gene-regulatory supervision. Off-thread on disease but methodologically relevant to the pretraining-contamination + data-scaling audit thread — pairs with Ali arXiv 2607.20572 scContam.

## SKIP

- 2026-09-02 mudskipper locomotion; 2026-09-04 natural disasters × nonprofit sector; 2026-09-10 Kalman filter for HT prevalence (COVID-19 focus, not portable); 2026-09-18 semiparametric contamination bias with multi-valued treatments (Csillag Finger & Possebom); scattered off-thread emails (Somali AI education, veterinary AI, quantum-hybrid physics, avian sex chromosomes, cryo-EM NHA1, non-coding scoliosis regulatory variants, HCM molecular landscape, MYLIP × female CVD, pulmonary embolism × DVT case-only GWAS, choroid plexus fetal aneuploidy screening, immune-checkpoint arrhythmias, RMS-MDD Chinese-medicine benchmark, paediatric asthma family-AI qualitative study, responsible stroke AI review).

---

## Bookkeeping

- **Report path:** `reports/2026-09-21-research-digest.md`.
- **Local arxiv-digest coverage:** `digests/2026-09-01.md` → `digests/2026-09-20.md` (nightly cron). 2026-09-21's digest will run on the standard 10:30 UTC cron and post separately.
- **`seen.json` size at report time:** 175 unique arXiv IDs since the pipeline was seeded, spanning 2604.xxxxx → 2609.20473. No pruning needed.
- **Next report cadence:** default is ~2–3 weeks, so the next research-digest report is due 2026-10-05 to -10-12 unless a large batch (Nature Medicine drop, NACFC late-breaker publication, or a new set of arXiv papers scoring ≥3) forces an earlier cut.
- **Interest-file drift check:** no `INTERESTS.md` edits are needed based on this window's mix. The sub-threads that fired hardest were `PheWAS / phecode infrastructure` (items 12, 13, 15), `Causal inference & pharmacoepi` (items 3, 4, 5, 21), `Variant interpretation` (items 10, 11, 17, 19, 32), `CFTR modulator pharmacoepi` (items 1, 20–26), and `EHR foundation models / AI-for-EHR` (items 5, 6, 7, 8, 9) — all currently well-anchored.
