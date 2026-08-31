# Research digest — 2026-08-31

**Sources triaged**
- Gmail: Google Scholar keyword alerts and citation alerts landing 2026-08-31 (last 24h; ~30 threads reviewed against `INTERESTS.md`).
- Repo: `digests/2026-08-25.md` through `digests/2026-08-28.md` (arXiv q-bio.QM / q-bio.GN / q-bio.PE / stat.AP).
- GitHub email digest for `chenjiezeng/arxiv-digest`: no notification threads in the last 14d; the arXiv content lives in the repo itself, so it is what this report draws from.

**Buckets** (from `INTERESTS.md` triage rubric): **HIGH** = directly serves an active thread; **METHODS-WATCH** = off-topic disease but transferable methods; **SKIP** = incidental keyword hit.

---

## Executive summary

Twelve items cleared the triage bar this cycle. The strongest signals are in three threads:

1. **Causal inference / pharmacoepi**: two Hernán-cited pieces (a JAMA Network Open SGLT-2i-after-AKI target-trial emulation and an AJE 21-year fish-intake TTE) plus an arXiv methods paper on per-protocol estimation in sequential TTE. All portable to CFTR-modulator persistence and GLP-1 RA discontinuation designs.
2. **EHR-linked biobank cohorts**: an AoU structural-variant amblyopia paper (Whitman & Lee) and the NetMoint UK Biobank multimodal-dementia-trajectory paper are the two most substantive biobank items; both are worth reading in full.
3. **Chronic-disease multimorbidity / phecode infrastructure**: Kerr et al. 523k-person Danish-registry psychiatric comorbidity network (cites phecode mapping) is the highest-signal multimorbidity item since May; complements the earlier `2026-07-29` digest work on trajectory clustering.

One self-citation update from Google Scholar: 2 new citations to Chenjie Zeng articles — noted, not covered in study reports below.

---

## HIGH-priority studies

### 1. Multimodal risk trajectories reveal heterogeneous paths to dementia (NetMoint) — Lee et al., arXiv 2608.26210, 2026-08-26

**Thread**: EHR-linked biobanks (UK Biobank) · ML for precision health · Chronic-disease clustering (dementia subtyping).

**Design**. 104,120 UK Biobank participants dementia-free at baseline. NetMoint is a multimodal framework fusing plasma proteomics, structural MRI, and cerebral haemodynamics to predict individualised 1/5/10/20-year risk of Alzheimer's, vascular, and frontotemporal dementia. External validation: ADNI-to-UKB harmonisation to 138 shared features.

**Key results**. Mean AUC 0.937 (AD), 0.930 (VD), 0.932 (FTD). Determinants shifted with horizon — structural brain vulnerability at short horizons, circulating molecular signatures at long horizons, with subtype-specific profiles. Multi-horizon trajectory clustering identified a 0.7% persistently very-high-risk AD subgroup (predicted 20-y risk 53.5%) and an 8.3% increasing-very-high-risk FTD trajectory (67.2%). Distinct molecular signatures: lower TGFB1 in the AD group, higher NDRG1 in the FTD group. Independent ADNI→UKB AUC 0.741 at 20 years after feature harmonisation.

**Why it matters here**. Direct match to two threads simultaneously: multimodal-augmented risk in UK Biobank (multi-omics-augmented PRS analogue on the proteomics side) and trajectory-resolved multimorbidity clustering. The subtype-specific proteomic biomarkers (TGFB1, NDRG1) are testable against BioVU / AoU proteomics substrates.

**Caveats to check on full read**. AUC 0.93+ across three horizons and three subtypes in a single held-in cohort merits calibration + decision-curve inspection; the ADNI→UKB validation drops to 0.741 which is more consistent with what an independent cohort should produce. Partially-observed multimodal fusion needs a missingness-mechanism audit.

**Link**: http://arxiv.org/abs/2608.26210v1

---

### 2. DINIRS: Digital Twin for Individualized Treatment Effects of Non-Invasive Respiratory Support — Islam, Mosier, Subbian, arXiv 2608.26915, 2026-08-27

**Thread**: EHR foundation models (digital-twins-from-EHR sub-thread) · Causal inference (HTE) · ML for precision health.

**Design**. Trained on 23 baseline variables from the first 24 ICU hours in 5,336 MIMIC-IV acute-respiratory-failure patients. Transformer encoder with a survival-attention gate decomposes 28-day ventilator-free days into survival probability × conditional ventilation duration; cross-fitted doubly-robust learner estimates ITEs. External validation in 2,540 eICU-CRD patients.

**Key results**. Mean benefit +2.07 ventilator-free days per patient. Predicted NIRS benefit higher in patients with less organ dysfunction (88.4% vs 49.0%). External validation reproduced the pattern *without retraining*. The benefit stems from shorter ventilation among survivors, not from reduced mortality — mechanism attributed to avoiding intubation-associated complications.

**Why it matters here**. Clean example of the digital-twins-from-EHR framing (`INTERESTS.md` §EHR foundation models) applied to a real ICU decision. The censoring-aware DR-learner design is the piece to crib — directly portable to CFTR-modulator escalation timing, HRT initiation, and GLP-1 RA persistence questions.

**Caveats**. MIMIC-IV → eICU is a light shift (both US ICU); portability to non-ICU EHR remains untested. "No retraining needed" claims are worth verifying against a calibration slope.

**Link**: http://arxiv.org/abs/2608.26915v1

---

### 3. Can You Trust Frozen Hematology Foundation Models under Acquisition Shift? — Sharma & Tapadiya, arXiv 2608.25148, 2026-08-25

**Thread**: EHR foundation models (pretraining-contamination-audit sub-thread) · Knowledge representation in EHRs (fidelity/portability audit).

**Design**. Audit of 15 frozen encoders (hematology, pathology, general vision) across four public single-cell WBC domains. Two axes: accuracy robustness and calibration. Explicit pretraining-exposure audit that identifies MLL23 as DinoBloom's internal cohort.

**Key results**. In-domain linear-probe macro-F1 saturated at 0.98-0.997, but cross-dataset F1 drops 34-72% with rank reordering — DinoBloom-L falls from 1st to 10th of 15 on the most-shifted target. Calibration collapses in parallel: source-trained probes go from ECE 0.004 in-domain to ECE 0.35 off-domain; temperature scaling transfers poorly. Label-free adaptation and marginal-entropy model-selection appear safe under balanced eval but fail under realistic class-prior shift. Class-Balanced Re-standardization (CBR) partially recovers.

**Why it matters here**. Direct methodological analogue for the CLMBR/MOTOR/MEDS benchmark-contamination audit thread. The "in-domain saturated, cross-dataset collapse" pattern is exactly the failure mode I want the EHR-FM digital-twins evaluations to be audited for. The exposure-vs-scanner-shift confound (DinoBloom's only held-out set is the source domain) is a portable QC argument for any FM benchmark.

**Caveats**. WBC-imaging domain, not tabular EHR; the CBR fix and calibration behavior may not transfer directly, but the audit protocol is what to copy.

**Link**: http://arxiv.org/abs/2608.25148v1

---

### 4. Sustained fish intake and 21-year Alzheimer's disease risk: a target trial emulation — Zhao et al., *American Journal of Epidemiology*, 2026

**Thread**: Causal inference / pharmacoepi (target trial emulation methodology). Cites Hernán TTE framework.

**Design**. Observational data on 2,012 cognitively healthy Framingham Heart Study Offspring adults. Emulated a target trial of seven isocaloric fish-intake strategies to estimate 21-year AD risk. Modelled repeated diet measures; adjusted for pre-baseline diet, baseline covariates, and time-varying confounding.

**Why it matters here**. High-methodological-density TTE with **repeated-measures exposure** and a long horizon (21 y) — exactly the design pattern I want to copy for CFTR-modulator persistence and HRT initiation timing, where exposure is neither point-in-time nor static. Repeated-measures exposure with time-varying confounding is where sequential TTE (see #8 below) also enters.

**Read alongside**: Hernán TTE framework paper (already cited), and the Chou SGLT-2i paper (#5).

---

### 5. Early Sodium-Glucose Cotransporter-2 Inhibitor Use After Acute Kidney Injury in Type 2 Diabetes — Chou, Chen, Jiang, Lin, Wu, *JAMA Network Open*, 2026

**Thread**: Causal inference / pharmacoepi (SGLT-2i drug-class watch, target-trial emulation).

**Design**. Cohort study comparing SGLT-2i prescription within 30 days vs 31-90 days after discharge among adults with T2D recovering from dialysis-requiring AKI (AKI-D). Design cites TTE framework.

**Why it matters here**. On the tracked SGLT-2i drug class, and squarely on the treatment-timing question ("when to escalate") that `INTERESTS.md` §Machine learning for precision health flags as high-priority. The AKI-D subgroup is a real clinical decision — clinicians hesitate to reinitiate SGLT-2i after AKI-D, but the trial evidence is thin.

**Follow-up to check**. What propensity model / IPTW spec they used; whether they present decision-curve analysis; how they handle immortal-time between hospital discharge and prescription.

---

### 6. Estimating networks of psychiatric comorbidity over two decades among 523,644 individuals using nationwide Danish registry data — Kerr, Benros, Wandall, Fried, Karstoft, 2026 (Research Square preprint)

**Thread**: Chronic-disease clustering and multimorbidity · PheWAS / phecode infrastructure (paper cites the Wu et al. ICD→phecode mapping).

**Design**. Danish national register, 523,644 adults receiving a first psychiatric diagnosis at age 18+. Cross-sectional and longitudinal comorbidity among 25 diagnoses (300 pairs). Regularised networks based on conditional logistic regression.

**Why it matters here**. Biggest population-scale psychiatric multimorbidity network I've seen surface this year. Direct analogue to the trajectory-network / phecode-comorbidity work in the July 29 report; portable to a BioVU or AoU replication using phecodeX psychiatric bins. Sex-difference analysis is called out and matches an open sub-question.

**Read alongside**: Chronic-disease-clustering block in earlier reports (`2026-07-29-research-digest.md`).

---

### 7. Epilepsy and Subsequent Dementia in Adults with Down Syndrome: A Propensity Score–Matched Cohort Study Using Federated Electronic Health Records — da Silva, Tudella, Lee, Santos et al., *Seizure*, 2026

**Thread**: EHR phenotyping & OMOP · Causal inference (federated observational) · Rare disease (Down syndrome / early-onset AD).

**Design**. Federated EHR network, PS-matched cohort of DS adults with vs without recorded epilepsy diagnosis. Outcome: incident dementia (predominantly early-onset AD in DS).

**Why it matters here**. Matches two active sub-threads at once: **federated / privacy-preserving EHR causal analytics** (`INTERESTS.md` §Causal inference sub-thread on Jang et al. 2607.17958 design pattern) and pre-symptomatic phenoconversion in a monogenic-risk population (DS trisomy → APP dosage → early-onset AD). The federated-EHR framing is what to read for methods.

**Caveats**. Recorded-diagnosis exposure is subject to under-ascertainment in DS (seizures may be attributed to behavioural symptoms); worth checking their sensitivity analysis.

---

### 8. From Cumulative Weights to Marginal Density Ratios: Per-Protocol Estimation in Sequential Target Trial Emulation — Ke, Cui, Dai, Emir, Cabrera, Alemayehu, arXiv 2608.20976, 2026

**Thread**: Causal inference / pharmacoepi (methods).

**One-line takeaway**. Marginal-density-ratio approach to sequential TTE per-protocol estimation, replacing cumulative IPCW weights that are unstable under sustained adherence + long follow-up. Directly applicable to CFTR-modulator persistence over 5+ years (where cumulative weights explode).

---

## METHODS-WATCH

### 9. Genomic structural variant associated with amblyopia in the All of Us research program — Whitman & Lee, *J AAPOS*, 2026

**Thread**: EHR-linked biobanks (AoU). Amblyopia is off my disease list, but AoU-SV methodology is worth the skim. 564 SVs examined; keep for the SV-calling pipeline and the AoU phenotype-linkage design.

### 10. Association of serum uric acid, gout with incident sepsis: a large population-based prospective cohort study from UK Biobank — Han et al., 2026

**Thread**: UK Biobank observational. Standard biomarker-exposure design; skim for the sepsis phenotype definition (interested in how sepsis was ascertained in UKB HES linkage).

### 11. Genetic overlap between eGFR and cardiovascular disease identifies potential targets for cardiorenal syndrome — Li, Chen, Xiong, Yuan, *Renal Failure*, 2026

**Thread**: Genetic epidemiology (cross-trait / MiXeR + conjFDR). 478 shared loci between eGFR and CVD via MiXeR + conjFDR — methods-watch for the multi-trait triangulation sub-thread. Skip disease-story; keep the MiXeR pipeline pointer.

### 12. Concordance Between Claims-Based and Electronic Health Record–Based Comorbidity Measures — Onukwugha et al., *JCO Clinical Cancer Informatics*, 2026

**Thread**: Knowledge representation in EHRs (concept-normalisation / claims-EHR crosswalks). NCI-CI computed from claims vs EHR on a linked source. Directly serves the "representation-ablation studies" sub-topic; short read to keep for the OMOP-vocabulary discussion.

---

## SKIP but noted (single-line each)

- **RIBOSPAN** (long-context RNA FM, 1.6B params, 10240-nt context) — RNA modelling, not EHR.
- **Monroe** (molecular FM on PM6, 81M molecules) — chemistry-first, no clinical loop; would only re-enter if paired with EHR-repurposing evidence.
- **GITIII-scale** (spatial-transcriptomics TME FM) — off-thread; interpretable-LR-decomposition mechanism only if it connects to drug-target evidence.
- **Panel DML for urban rail reliability** (Yao, Zhang, Graham) — DML methods-watch; not clinical.
- **CTC identification in extremes** (Leimenstoll & Schienle) — heavy-tailed causal inference; off-thread but worth remembering if any extreme-value bioinformatics application surfaces.
- **Rare variation in autism (Satterstrom et al., medRxiv)** — high-quality rare-variant cross-trait paper; off tracked disease list, keep for the pleiotropy methodology only.
- **Machine Learning / LLM / Multimodal AI for Diagnosing Pediatric Rare Diseases: Scoping Review** (Zhao et al., JMIR 2026) — scoping review; useful for the rare-disease LLM-diagnosis benchmark thread but not a primary source.

---

## Alerts noted, not covered

- 2 new citations to Chenjie Zeng articles (Google Scholar) — cite-tracking, filed.
- 10-new-citation alerts to Bastarache, Denny, Karczewski, Kastner, Hripcsak, Hernán, Luo, Zitnik, Montgomery, Wang, Natarajan, Szolovits — cite-tracking; the study-level items surfaced from those alerts that met the triage bar are included above (Kerr et al., Chou et al., Zhao et al., Li et al., psoriasis GWAS).

---

_Generated 2026-08-31 as a scheduled arxiv-digest research summary. Source list, buckets, and the triage rubric follow `INTERESTS.md` (last updated 2026-07-29)._
