# Research digest report — 2026-09-22

Triage of research-related email (Google Scholar alert feeds + NCBI PubMed
saved-search alerts + bioRxiv subject alerts + JAMA Online First) and the
local `arxiv-digest` repo against the active threads in `INTERESTS.md`
(PheWAS / phecodes, EHR-linked biobanks, EHR phenotyping / OMOP, causal
inference & pharmacoepi, variant interpretation, genetic epi, CF / APOL1 /
CHIP-VEXAS / LOY / IBD disease threads, EHR foundation models, KGs /
ontologies, drug repurposing, rare disease, ML for precision health,
multimorbidity, knowledge representation in EHRs).

Window: **2026-09-21 12:40Z → 2026-09-22 12:40Z** (~24 hours since the
`2026-09-21-research-digest.md` report; covers one `arxiv-digest` cron run
(dry) plus the 09-22 06:46Z Google Scholar alert wave — ~40 feeds fired in
one batch — the 09-21 14:10Z NCBI PubMed alerts for the "drug repurposing"
and "All of Us" saved searches, one bioRxiv Subject Collection alert
(09-22 00:01Z), and three JAMA Online First emails on 09-21).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-21.md`) | 09-21 cron | Dry — 0 papers surfaced in the 30 h lookback. Also dry in the 09-19 → 09-20 runs already logged in the previous report. No new digest file for 09-22 yet (the cron runs at 10:30 UTC and its output has not committed to the repo working tree at the time of this scan). |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com arxiv-digest newer_than:2d` returned zero threads. Consistent with the last three reports: the pipeline commits its output to this repo rather than emailing PR/cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-22 batch, 06:46Z) | 09-22 | ~40 feeds fired in one wave. HIGH-item leaders: **Miguel Hernán citations-to** — Hellemans et al. *BMJ* 2026 **international TTE of deceased donor kidney transplant vs. continued dialysis**; Liang et al. *Diabetologia* 2026 systematic review of **menopause hormone therapy × type-2 diabetes**; Wen *Int J Biostat* 2026 **doubly-robust monotonic survival curves** under time-varying treatments; Chi et al. *Genes & Diseases* 2026 **trustworthy AI review** (target-trial framework citation). **Joshua C. Denny new-related** — Sanchez et al. **Lancet Gastroenterology & Hepatology 2026** *"Genetic variants and the risk of renal impairment in decompensated cirrhosis: a multi-ancestry GWAS"* (also fires under Zeng, Bastarache, Yuan Luo, Jian Yang feeds); Bal et al. *Nature Cardiovascular Research* 2026 **multiancestry PRS improves HCM stratification**; Chen et al. *Nature* 2026 **cell-type-specific eQTLs underlie genetic architecture of complex traits**; Perée et al. *Nat Commun* 2026 **cis-eQTL analysis on 27 blood and 43 gut cell populations matches 140 IBD risk loci and identifies entrectinib as a repurposing candidate**. **Stephen B Montgomery new-related** — Zhang, Zhou, Li, Ryckman, Ray, Scifres et al. **PRS-CARV** (Research Square 2026) *"A summary statistics framework for integrating annotation-informed rare variants to improve polygenic risk prediction"*. **George Hripcsak new-related** — Bakr et al. *J Biomedical Informatics* 2026 **MEDAL: sequential adapter learning for privacy-preserving multicenter clinical language models**. **Emily Alsentzer new articles** — Sivaraman et al. arXiv 2609.19318 *"I Know Where to Look, But Does the LLM? Charting the Gaps Between Clinical Expert Needs and Unstructured Data Abstraction Tools"*. **Tiffany J Callahan new-related** — Vichentijevikj, Mishev & Misheva **GeneResolver** (Research Square 2026): a *traceable hybrid multi-agent pipeline for etiology-aware gene prioritization* in rare disease. **Zhiyong Lu new articles** — Lefkowitz, Eisenberg, Huang, Mudunuri et al. (Research Square 2026) **machine-readable database for genotype-phenotype analyses in rare diseases, using FKTN-related congenital muscular dystrophies as a prototype**. **Bryan Traynor citations-to** — Kingsmore & Delatycki *Annual Review of Medicine* 2026 **Genomic Screening for Infants and Reproductive Adults**; Um, Adelman & Pollina *Annual Review of Pathology* 2026 **Fault Lines in the Genome: somatic DNA mutations in aging and neurodegeneration** (somatic-mosaicism thread). **Michael Snyder new articles** — Lautman et al. *IEEE JBHI* 2026 **interpretable workflow for cohort phenotyping using longitudinal wearable data**. **Leo Anthony Celi new articles** — Le Guellec, Bentegeac, Boyer, Celi et al. *J Epidemiology & Population Health* 2026 **"The dead science theory"** (meta-epidemiology). **Chenjie Zeng new-related** — Sanchez et al. cirrhosis renal GWAS (same paper as above); **Doumat, Iyer & Jain** *Current Opinion in Pulmonary Medicine* 2026 review of medical issues and pulmonary outcomes in CF and bronchiectasis; Shi, Swanson, Diemer, Gerlovin et al. medRxiv 2026 **selection bias in MR studies with adjustment for medication use**. **Neil M Davies new articles** — Nolan, Davies, Harron, Islam & Cook *BMJ Medicine* 2026 editorial *"Promoting access and trust: cohort and data profiles in BMJ Medicine"*. **Pascal Brandt new-related** — Seth et al. Computational and Structural Biotechnology **FHIR data mapping quality assessment scoping review + expert-informed requirements for future pre-mapping frameworks**. Remaining ~20 feeds low-signal or off-thread; enumerated in the SKIP section. |
| NCBI PubMed saved-search alerts (09-21 14:10Z) | 09-19 → 09-21 | Two saved-searches fired. **"drug repurposing"** returned 2 new items: Greenberg et al. *Nature Communications* 2026 **drug screen + machine learning predict neuroprotective agents in a preclinical human model of childhood dementia** (PMID 42764280); Zhou et al. *Drug Development Research* 2026 review of **statins as repurposed anticancer agents**. **"All of Us"** returned 2 new items: Peng et al. *Alzheimer's & Dementia* 2026 **genetic evidence suggests a protective role of immunoglobulin M in Alzheimer's disease** (PMID 42764449); Pederson, Buto, Zimmerman, Velez, Sims, Murchland, Wang, Glymour, Spartano, Weuve, Gilsanz, Chi, Whitmer & Brennan *Alzheimer's & Dementia* 2026 **clinical modifiers of the association between type 1 diabetes and dementia incidence** (PMID 42764447). |
| bioRxiv Subject Collection alert (09-22 00:01Z) | 09-22 | Weekly digest across Bioinformatics / Genetics / Genomics / Immunology / Pathology. No new items previously unseen in other channels; the Bioinformatics section headline (MaSkel-like ML classification of expression states) is off-thread and no follow-up is warranted this window. |
| JAMA Online First (09-21 18:35Z, 18:49Z, 20:06Z) | 09-21 | Three JAMA Online First TOC emails. Headline items — review on cancer vaccine development, kidney transplant access after Medicare Advantage expansion, physician politicization editorial — are off the tracked research threads; no HIGH-item pull-through. |

> Caveat: Scholar and PubMed emails contain only title, authors, venue,
> and the first ~2–3 lines of each abstract. The reports below
> contextualize that metadata against the research threads; nothing here
> reflects full-text reading. `arxiv-digest` entries include the full
> abstract because the pipeline captures it — but this window contained
> no new `arxiv-digest` hits. Author lists are truncated as they appear
> in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fifteen HIGH items surfaced this window, dominated by a single Scholar
wave on 09-22 06:46Z. They cluster into six knots:

**Multi-ancestry GWAS / cross-cutting genomic-epi headline (1 item).**
**Sanchez et al. *Lancet Gastroenterology & Hepatology* 2026** —
*"Genetic variants and the risk of renal impairment in decompensated
cirrhosis: a multi-ancestry genome-wide association study."* Fired
across the Denny, Bastarache, Chenjie Zeng, Yuan Luo and Jian Yang
feeds in the same batch — a rare five-feed simultaneous hit and the
signal-to-noise leader of the window. Directly serves `Genetic
epidemiology → GWAS + cross/trans-ancestry portability` and pairs
with the Central-Asian PGS-validation gap (Abdullaev *Genes* 2026,
last report) as another data point on how much non-EUR ancestry
representation shifts the genetic architecture recovered from GWAS.

**Composite-risk / PGS thread (3 items).** **Zhang, Zhou, Li, Ryckman,
Ray, Scifres et al. PRS-CARV** (Research Square 2026) — a summary
statistics framework that **integrates annotation-informed rare
variants** with common-variant PGS. This is a direct instrument for the
`Genetic epidemiology → Composite risk models stacking PRS with rare
pathogenic variants` sub-thread and pairs with Baya *AJHG* 2026
"misaligned individuals" (PGS residuals) and Souaiaia *Nature* PGS-tails
in the taxonomy `INTERESTS.md` maintains. **Bal et al. *Nature
Cardiovascular Research* 2026** — a **multiancestry PRS improves
stratification in HCM** among sarcomere P/LP-negative cases (two-thirds
of HCM has no P/LP variant explained). Classic composite-risk framing:
Mendelian variant + polygenic-tail contribution across ancestries. **Wang
et al. Human Reproduction Open 2026** — a context-specific PES
(polygenic embryo screening) evaluation in best-prognosis PGT cycles.
Methodologically important as PES continues to run ahead of its
population evidence base; the "context-specific stratification vs
best-prognosis pool" framing is the right frame for how to critique it
and pairs with the PGS-portability thread.

**Causal inference / pharmacoepi TTE cluster (4 items).** **Hellemans et
al. *BMJ* 2026** (Hernán feed) — international **target trial emulation
of deceased donor kidney transplantation vs. continued dialysis** using
the European Renal Association Registry across five countries/regions,
stratified by age, diabetes, cardiovascular disease, standard vs.
expanded-criteria donor, DBD vs. DCD. On-thread for `Causal inference
and pharmacoepidemiology → target trial emulation` and a clean example
of the "multi-registry TTE" pattern that will need to be replicated
across AoU / MVP for US comparators. **Liang et al. *Diabetologia* 2026**
(Hernán feed) — **systematic review + meta-analysis of menopause hormone
therapy on type-2 diabetes** risk and prognosis. Directly serves the
`hormone replacement therapy` drug-class sub-thread and pairs with the
persistence / discontinuation sub-thread already tracked. **Shi,
Swanson, Diemer, Gerlovin et al. medRxiv 2026** (Zeng feed) — *"Selection
bias in Mendelian randomization studies with adjustment for medication
use"*: extends the Shi/Diemer/Swanson AJE 2026 MR-interpretation piece
already in the last report and is the direct methodological complement
to the `Genetic epidemiology → Drug-target MR triangulated with
observational cohort estimates` sub-thread — LDL-C example, where MR
estimates are complicated by widespread statin use. **Wen *Int J
Biostat* 2026** (Hernán feed) — **doubly-robust monotonic survival
curves for time-varying treatments** in observational studies. A
technical g-methods paper (repairs monotonicity of DR longitudinal
g-formula) that serves the `causal inference` methods watch and pairs
with recent DR-longitudinal work; useful if any of the ongoing TTE
projects switch to DR estimators for cumulative-incidence outcomes.

**EHR + LLM / AI-for-EHR cluster (3 items).** **Sivaraman, Turnham,
Bonano, Aresh et al. arXiv 2609.19318** (Emily Alsentzer feed) —
*"I Know Where to Look, But Does the LLM? Charting the Gaps Between
Clinical Expert Needs and Unstructured Data Abstraction Tools."*
Direct qualitative-plus-benchmark study of where LLM-based information
extraction from clinical notes falls short of what expert cancer
abstractors actually need — an on-brand fit for the
`representation-and-downstream-use → NLP-derived representations
from clinical notes` sub-thread and a needed corrective to the
LLM-extract-and-ship literature. **Bakr et al. *J Biomedical
Informatics* 2026** (Hripcsak feed) — **MEDAL: sequential adapter
learning for privacy-preserving multicenter clinical language models.**
Federated / adapter-based fine-tuning of clinical LMs across sites.
Serves both `Federated / privacy-preserving EHR causal analytics`
(architecture pattern) and `EHR foundation models` (multicenter
fine-tuning without pooling notes). **Lautman, Chang, Rangan, Hittle,
Uwakwe et al. *IEEE JBHI* 2026** (Snyder feed) — *"An interpretable
workflow for cohort phenotyping using longitudinal wearable data."*
Wearable-derived phenotyping with explicit interpretability — the
right template for the wearable → phecode / phenotype pipeline that
Luo et al. *PLOS Medicine* 2026 (last report) opened.

**Rare disease / variant interpretation (3 items).** **Vichentijevikj,
Mishev & Misheva — GeneResolver** (Research Square 2026, Callahan feed)
— *"a traceable hybrid multi-agent pipeline for etiology-aware gene
prioritization"* that reasons over HPO phenotypes, variant patterns,
inheritance, and heterogeneous biological evidence — with a
**traceable** rationale, not opaque link-prediction scores. Direct
match for the `Rare disease → auditable HPO-driven diagnostic
benchmarks with separable metrics for ranking vs. evidence coverage`
sub-thread; joins the Ghasemnejad et al. ReAct+RAG paper (last report)
as the second on-thread agentic rare-disease diagnostic paper this
month. **Lefkowitz, Eisenberg, Huang, Mudunuri et al.** (Research
Square 2026, Zhiyong Lu feed) — a **machine-readable database for
genotype-phenotype analyses in rare diseases, prototyped on FKTN-related
congenital muscular dystrophies** (α-dystroglycanopathies). Fits the
`variant interpretation` × `rare disease` × `knowledge representation`
intersection: how to make gene-level phenotypic data computable for
downstream reanalysis at scale. **Kingsmore & Delatycki *Annual Review
of Medicine* 2026** (Traynor citations-to feed) — *"Genomic Screening
for Infants and Reproductive Adults."* The definitive Annual-Review
framing piece for population-scale genomic screening — the exact
"population-screening vs. clinical-ascertainment" framing the PheWAS
thread's penetrance sub-thread cares about, now written up as an
authoritative review for the audience beyond human genetics.

**Drug repurposing / IBD-thread crossover (1 item).** **Perée et al.
*Nature Communications* 2026** (Denny feed) — cell-type-specific
cis-eQTL analysis in 27 sorted blood cell populations + 43 intestinal
cell populations, matching **140 IBD risk loci** and nominating
**entrectinib as a repurposing candidate**. On both the `IBD` disease
sub-thread and the `Drug repurposing → knowledge-graph / eQTL-based
repurposing with explainable rationale` sub-thread — a rare
double-hit.

Two additional items are METHODS-WATCH rather than HIGH:
**Chen et al. *Nature* 2026** — cell-type-specific eQTLs underlie the
genetic architecture of complex traits (Denny feed); a
genetic-architecture foundational paper. **Chi et al. *Genes &
Diseases* 2026** — disease-agnostic trustworthy-AI review (Hripcsak
feed); reference paper.

Three items outside the main knots are on-thread but supplementary:
**Doumat, Iyer & Jain *Curr Opin Pulm Med* 2026** — CF/bronchiectasis
medical-outcomes review (CF thread); **Um, Adelman & Pollina *Annual
Review of Pathology* 2026** — somatic mutations in aging + neurodegen
(somatic-mosaicism thread); **Le Guellec, Celi et al. *J Epid Popul
Health* 2026** — *"The dead science theory"* meta-epidemiology piece
(reproducibility / clinical-AI framing).

Three PubMed-alert HIGH items round out the picture:
**Greenberg et al. *Nat Commun* 2026** — **drug screen + ML for
neuroprotection in childhood dementia** (drug-repurposing thread);
**Peng et al. *Alzheimer's & Dementia* 2026** — **genetic evidence for
protective role of IgM in AD** (All of Us biobank thread); **Pederson
et al. *Alzheimer's & Dementia* 2026** — **clinical modifiers of the
type-1-diabetes → dementia association** (All of Us biobank +
multimorbidity threads).

---

## Detailed reports per HIGH-priority study

Each block below expands the title / snippet-level metadata from the
alert into a compact structured writeup with thread mapping, why it
matters, and open questions. Reports are grouped by knot, not by feed;
where a paper appears under multiple feeds the feed list is inlined.

### 1. Sanchez et al. — Multi-ancestry GWAS of renal impairment in decompensated cirrhosis

- **Citation.** L.O. Sanchez, J. Clària, C. Galvanin, F. Aguilar, R. Layese et al. *"Genetic variants and the risk of renal impairment in decompensated cirrhosis: a multi-ancestry genome-wide association study."* **Lancet Gastroenterology & Hepatology** 2026 (advance article).
- **Alert channels.** Denny new-related, Chenjie Zeng new-related, Lisa Bastarache new-related, Yuan Luo citations-to, Jian Yang new-related — same paper fires under five feeds simultaneously (the strongest same-batch signal-to-noise concordance of the window).
- **Snippet (verbatim).** "Renal impairment is a major complication of decompensated cirrhosis and a key driver of mortality. Despite its clinical significance, the genetic architecture of susceptibility to renal impairment in this context remains largely unexplored."
- **Thread mapping.** `Genetic epidemiology → GWAS + cross/trans-ancestry portability`; secondary `Biobanks with EHR linkage` (assuming the design leans on registry / biobank-level phenotype capture).
- **Why HIGH.** Cross-ancestry GWAS in a specific clinical-decompensation phenotype (renal impairment in decompensated cirrhosis) rather than at the disease-cause level, which is the flavor of "endophenotype under clinical condition" that pairs well with the PheWAS penetrance-under-clinical-ascertainment framing. Cirrhosis + AKI/HRS is also a natural target for pharmacoepi work on nephrotoxic drug avoidance and TTE of terlipressin, which is why the paper hits so many feeds at once.
- **Open questions.** (i) What cohorts contributed to the multi-ancestry design (European Renal Association? national biobanks? liver-transplant registries?)? (ii) Was the outcome AKI vs. hepatorenal syndrome vs. eGFR-drift, and how were competing risks handled? (iii) Do the top loci overlap the CKD-generic loci (UMOD, SHROOM3, APOL1) or are they cirrhosis-specific? APOL1 in particular would connect to the tracked disease thread. (iv) Was there a within-decompensation vs. all-cirrhosis contrast to separate susceptibility from decompensation-triggered susceptibility? These will decide whether the paper is a "read now" or "cite the finding, wait for methods" for downstream work.
- **Follow-up.** Full-text read at first opportunity; check whether an eLife / medRxiv preprint exists that predates the Lancet Gastro version so the methods table can be inspected without a paywall.

### 2. Zhang, Zhou, Li, Ryckman, Ray, Scifres et al. — PRS-CARV

- **Citation.** Y. Zhang, G. Zhou, M. Li, K.K. Ryckman, M. Ray, C. Scifres et al. *"PRS-CARV: A summary statistics framework for integrating annotation-informed rare variants to improve polygenic risk prediction."* Research Square 2026 preprint.
- **Alert channels.** Stephen B Montgomery new-related.
- **Snippet.** "Polygenic risk scores (PRS) primarily rely on common variants because rare variant effects are difficult to estimate without large sequencing cohorts. We developed PRS-CARV, a summary statistics framework that integrates annotation-informed rare …"
- **Thread mapping.** `Genetic epidemiology → Composite risk models stacking PRS with rare pathogenic variants`; secondary `PGS residuals / polygenic-deviation designs`, `Multi-omics-augmented PRS` framing.
- **Why HIGH.** PRS-CARV is the summary-statistics-only, annotation-informed rare-variant + PGS composite framework the composite-risk sub-thread has been waiting for. Most published composite scores require individual-level data (which is why they run in UKB / AoU / MVP and stop there); a summary-statistics-only framework generalizes composite risk to any GWAS+RVAS study with published summstats. If the calibration and portability claims hold this is the paper to cite as the successor to Souaiaia PGS-tails and Baya PGS-residuals frameworks for stacking rare pathogenic variants onto common-variant polygenic score.
- **Open questions.** (i) Which annotation source does CARV consume — MPC, CADD, PrimateAI, in silico splicing? (ii) Does the summary-statistics framework handle the effect-inflation from small allele-count RV strata, or does it defer to per-gene burden statistics? (iii) Portability claim: is it demonstrated across ancestries (UKB → AoU?) or is that left for a companion paper? (iv) Is code released — R / Python / snakemake — and how does the compute footprint compare to LDpred2-auto extensions?
- **Follow-up.** Preprint read at first opportunity; cross-reference against the Ward et al. medRxiv "rare extreme PRS strongly indicate AD risk" paper from the last report — they're perpendicular framings of the same idea (rare variant in the tail of PRS vs. PRS-with-rare-variant-lift) and should be discussed together in the CFTR + APOL1 + BRCA composite-risk write-up when that thread advances.

### 3. Bal et al. — Multiancestry PRS improves stratification in HCM

- **Citation.** H.S. Bal, A. Pampana, A. Nayak, M. Gaonkar, S. Patel et al. *"A multiancestry polygenic risk score improves stratification in patients with hypertrophic cardiomyopathy."* **Nature Cardiovascular Research** 2026.
- **Alert channels.** Joshua C. Denny new-related.
- **Snippet.** "Hypertrophic cardiomyopathy (HCM) has traditionally been considered a Mendelian disease driven by pathogenic or likely pathogenic variants in sarcomere-encoding genes (SARC-HCM-P/LP). However, these variants explain only one-third of cases …"
- **Thread mapping.** `Genetic epidemiology → Composite risk models`; secondary `Specific disease threads` (cardiovascular / cardiomyopathy — adjacent to the CFTR pharmacoepi thread as a "Mendelian disease with polygenic modifier" template).
- **Why HIGH.** Directly on the composite-risk framing: two-thirds of HCM cases have no P/LP sarcomere variant, so a well-calibrated multiancestry PRS becomes both a Mendelian-negative case discovery instrument and a modifier of penetrance for P/LP-positive cases. The Mendelian + PGS "two-hit" template is directly portable to CFTR (modifier PGS on CFTR heterozygotes), APOL1 (polygenic modifier of high-risk-genotype penetrance), BRCA (already extensively studied), and TTR / ATTR (V142I penetrance under polygenic background).
- **Open questions.** (i) Which ancestries were represented, and does the PRS retain calibration when transported to AoU African ancestry cohorts? (ii) Was the PGS trained on HCM cases or on quantitative-trait proxies (LV wall thickness, ECG-derived hypertrophy)? (iii) Was the stratification metric a net reclassification improvement over the Mendelian-only baseline, or a Harrell's-C incremental? (iv) How does the paper handle the P/LP-positive-vs-negative interaction — additive PGS + Mendelian, or interaction-term PGS × Mendelian?
- **Follow-up.** Read at first opportunity; use as an anchor citation when framing the HCM/CFTR/APOL1 "Mendelian-plus-modifier" composite-risk pattern in future writing.

### 4. Hellemans et al. — International target trial emulation of deceased donor kidney transplantation vs. continued dialysis

- **Citation.** R. Hellemans, N.C. Chesnaye, A. Kramer, E.L. Fu, M. Arnol et al. *"Survival benefit of deceased donor kidney transplantation versus continued dialysis: international target trial emulation."* **BMJ** 2026 (open access, PIIS 394/bmj-2026-100624).
- **Alert channels.** 10 new citations to Miguel Hernán.
- **Snippet.** "Objective To quantify the survival benefit of deceased donor kidney transplantation versus continued dialysis according to patients' characteristics (age, diabetes, cardiovascular disease), donor quality (standard criteria donor or expanded criteria donor) and donor retrieval type (donation after brain death or donation after circulatory death). Design Target trial emulation. Setting European Renal Association Registry data from five countries or regions: Catalonia (Spain), Denmark, France …"
- **Thread mapping.** `Causal inference and pharmacoepidemiology → Target trial emulation`.
- **Why HIGH.** Multi-registry TTE of the transplant-vs-dialysis decision — the classic "point-of-decision" TTE where the counterfactual is well defined but the observational execution has to handle immortal-time on the transplant list, waitlist competing risks, and donor-quality confounding. The five-country pattern is a template for a US analogue in AoU + MVP + UNOS registry data, and pairs with the Turchin et al. BMJ 2026 SGLT-2 vs. GLP-1 renal-outcomes TTE from the last report as another instance of TTE-in-BMJ as a house style.
- **Open questions.** (i) How was the immortal-time-on-waitlist bias handled — sequential trials at each donor-offer event? (ii) Was donor quality (SCD vs. ECD) and retrieval type (DBD vs. DCD) exchanged out of the treatment definition (donor-type-agnostic TTE) or in as effect modifiers? (iii) Cross-country heterogeneity: what is the between-country I² for the primary effect, and what shifts it? (iv) Does the paper's supplementary include an eligibility-flow diagram of the type the Hernán TTE house style typically produces?
- **Follow-up.** Read; use as a reference TTE-in-BMJ paper and check whether the AoU / MVP kidney data would support a US analogue (though absent living-donor cost-of-organ counterfactual data, the US replication may be harder). Pair with the ongoing GLP-1 / SGLT2 renal-outcomes TTE thread.

### 5. Liang et al. — Menopause hormone therapy and type-2 diabetes: systematic review and meta-analyses

- **Citation.** C. Liang, A.J. Dobson, J. Doust, L.W. Ribeiro, G.D. Mishra. *"Menopause hormone therapy and type 2 diabetes risk and prognosis: systematic review and meta-analyses."* **Diabetologia** 2026.
- **Alert channels.** 10 new citations to Miguel Hernán.
- **Snippet.** "Menopause hormone therapy (MHT) may have effects on metabolic conditions. This study was conducted to systematically review the literature, to summarise and quantify the effect of MHT on glucose or insulin levels and on new-onset type 2 diabetes among women without type 2 diabetes and to summarise and quantify the effect of MHT on glucose, insulin, lipid and blood pressure levels among women with type 2 diabetes."
- **Thread mapping.** `Causal inference and pharmacoepidemiology → hormone replacement therapy` drug-class sub-thread; secondary `Pharmacogenomic modifiers of medication persistence` (as a template for HRT persistence pharmacoepi).
- **Why HIGH.** Direct MHT-outcomes systematic review at exactly the level the HRT drug-class sub-thread needs: incidence of T2D + metabolic markers among users vs. non-users, and among T2D-positive users vs. non-users. Pairs with prior work on HRT for CVD/cognitive outcomes.
- **Open questions.** (i) Randomized-trial vs. observational-only pooling, and does the meta-analysis do them separately? (ii) Preparation-specific stratification (oral vs. transdermal, opposed vs. unopposed, CEE vs. estradiol) is where the effect-heterogeneity lives; is it reported at that granularity? (iii) Timing-of-initiation window (< 10 y since menopause vs. > 10 y) — the classic "healthy-user timing" question — is it addressed via meta-regression or subgroup? (iv) Are TTE-emulating observational designs (Miguel Hernán's own WHI reanalysis flavor) included as a distinct evidence tier?
- **Follow-up.** Read at first opportunity; use as anchor citation for the HRT drug-class page in the pharmacoepi thread.

### 6. Shi, Swanson, Diemer, Gerlovin et al. — Selection bias in Mendelian randomization with adjustment for medication use

- **Citation.** J. Shi, S.A. Swanson, E.W. Diemer, H. Gerlovin et al. *"Selection bias in Mendelian randomization studies with adjustment for medication use."* medRxiv 2026.09.16.26363225 preprint.
- **Alert channels.** Chenjie Zeng new-related.
- **Snippet.** "Mendelian randomization (MR) studies often evaluate exposures such as LDL cholesterol (LDL-C). The widespread use of lipid lowering medications complicates the interpretation and the validity of MR estimates. …"
- **Thread mapping.** `Causal inference and pharmacoepidemiology → Mendelian randomization`; secondary `Genetic epidemiology → Drug-target MR triangulated with observational cohort estimates` sub-thread.
- **Why HIGH.** Direct methodological complement to the Shi/Diemer/Swanson *AJE* 2026 MR-interpretation piece already logged. The specific worked example — LDL-C as an MR exposure in a statin-treated population — is the exact bias mechanism that shows up in every drug-target-MR analysis for lipid-lowering therapies (PCSK9, HMGCR, NPC1L1, LPA). If the paper extends beyond LDL-C to BP-lowering (antihypertensives) or glycaemic-control (metformin, GLP-1 RA, SGLT2i), it gives the drug-target-MR sub-thread a "here's how to correctly handle medication adjustment" reference for every future MR analysis in a treated cohort.
- **Open questions.** (i) Does the paper distinguish "conditioning on medication use" (selection bias via collider stratification) from "medication as a mediator" (post-treatment confounding)? (ii) Does the framework handle time-updated medication use (users → non-users → users) or only baseline medication use? (iii) Sensitivity to unmeasured indication for treatment? (iv) Does the paper propose an alternative estimator (rank-preserving, principal-stratification, negative controls) or only characterize the bias?
- **Follow-up.** Read preprint promptly; cite alongside the *AJE* piece as the pair of "how to interpret MR estimates" references for drug-target MR work.

### 7. Wen — Doubly robust estimation of monotonic survival curves for time-varying treatments

- **Citation.** L. Wen. *"Doubly robust estimation of monotonic survival curves for time-varying treatments in observational studies."* **The International Journal of Biostatistics** 2026.
- **Alert channels.** 10 new citations to Miguel Hernán.
- **Snippet.** "Doubly robust estimators of the longitudinal g-computation formula enhance robustness against model misspecification, offering an improvement over the standard inverse probability weighted estimators. However, existing doubly robust estimators for discrete-time survival outcomes do not necessarily guarantee that the estimated survival curves remain monotonic. In this manuscript, we propose a novel estimator of the g-computation formula specifically designed for discrete-time survival …"
- **Thread mapping.** `Causal inference and pharmacoepidemiology → g-methods / g-computation`; METHODS-WATCH.
- **Why HIGH-ish.** Fixes a real practical gap in doubly-robust longitudinal survival estimation — DR estimators can produce non-monotonic survival curves at finite N, which breaks downstream Kaplan-Meier-style presentation and forces post-hoc smoothing. If the estimator is available in a package (LTMLE / gfoRmula) it becomes drop-in for the TTE work that uses cumulative-incidence primary outcomes.
- **Follow-up.** Skim methods and check availability in ltmle / gfoRmula / lmtp; flag to any TTE work with cumulative-incidence outcomes.

### 8. Perée et al. — cis-eQTL analysis in blood/gut identifies 140 IBD risk loci and entrectinib as repurposing candidate

- **Citation.** H. Perée, V.A. Petrov, Y. Tokunaga, A. Kvasz, F. Farnir et al. *"Cell-type specific analyses in blood and gut identify cis-eQTL matching 140 IBD risk loci and entrectinib as repurposing candidate."* **Nature Communications** 2026.
- **Alert channels.** Joshua C. Denny new-related.
- **Snippet.** "Genes whose expression is affected, in a consistent manner, by GWAS-identified risk variants and the disease process, constitute preferred drug targets. We herein combine cis-eQTL analysis in 27 sorted blood cell populations and 43 intestinal cell populations."
- **Thread mapping.** Double-hit: `Specific disease threads → Inflammatory bowel disease` AND `Drug repurposing → EHR-based repurposing signals` / `causal-inference framings of off-label use`.
- **Why HIGH.** IBD is on the tracked disease list (shared with autoimmune work) and the 140-locus match against cell-type-specific cis-eQTLs is exactly the kind of "GWAS + expression convergence" evidence base that gives drug-repurposing hypotheses (like entrectinib for IBD) a mechanistic rationale rather than an opaque link-prediction score. Entrectinib is an approved ROS1/NTRK inhibitor used in NSCLC and NTRK-fusion solid tumors, so this is a genuine repurposing candidate with an existing safety envelope.
- **Open questions.** (i) Was the entrectinib repurposing signal validated in an EHR-based real-world cohort (e.g., serendipitous entrectinib prescription in an IBD patient), or is it a purely computational nomination? (ii) Which cell-type carries the strongest colocalization for the entrectinib-target locus — enterocytes, T cells, macrophages? (iii) Do the 140 IBD loci overlap with the Devarakonda scDEFT counterfactual drug-effect atlas from 09-11? Both papers are working on the same IBD substrate at overlapping cell resolutions and their results should be cross-referenced.
- **Follow-up.** Read; check ClinicalTrials.gov for any entrectinib IBD trial signal; cross-reference against scDEFT and the Zitnik World Models framing.

### 9. Sivaraman et al. — "I Know Where to Look," But Does the LLM?

- **Citation.** V. Sivaraman, R. Turnham, G. Bonano, N. Aresh et al. *"'I Know Where to Look,' But Does the LLM? Charting the Gaps Between Clinical Expert Needs and Unstructured Data Abstraction Tools."* arXiv preprint 2609.19318 (2026).
- **Alert channels.** Emily Alsentzer new articles.
- **Snippet.** "Clinical data abstraction, the process of distilling structured information from patient records, plays a key role in advancing knowledge about diseases such as cancer. Information extraction (IE) with large language models (LLMs) could accelerate this…"
- **Thread mapping.** `Knowledge representation in EHRs and applications → NLP-derived representations from clinical notes`; secondary `EHR foundation models` (evaluation-side), `EHR phenotyping & OMOP → LLM-assisted phenotyping`.
- **Why HIGH.** The "here is where the LLM misses what a human abstractor would catch" contrast is the underexplored side of the LLM-abstraction literature — most published work benchmarks LLMs on already-defined extraction targets, this paper starts from what human abstractors say they need. This is the calibration audit the field needs before deploying LLM abstraction in tumor-registry or PheKB-style production pipelines. Pairs with Fu et al. *npj Health Systems* 2026 (last report) on multi-site benchmarking of geriatric-care construct extraction as a "here is how to audit LLM extraction against clinical ground truth" line.
- **Open questions.** (i) Which LLMs were audited — closed frontier (Claude, GPT), open (Llama, Qwen), medical-fine-tuned (Med-PaLM, MedGemma)? (ii) Was the ground-truth cohort cancer-registry data (SEER-style)? (iii) What abstraction targets specifically failed — nuanced staging, treatment-response evaluation, adverse-event grading? (iv) Is the "expert needs" audit portable to other domains (rheumatology, transplant nephrology, IBD registry) or cancer-specific?
- **Follow-up.** Read arXiv preprint at first opportunity; align with the LLM-assisted-phenotyping work planned for the EHR phenotyping thread.

### 10. Bakr et al. — MEDAL: Sequential adapter learning for privacy-preserving multicenter clinical language models

- **Citation.** A. Bakr, A. Garcia-Agundez, T. Atkison, V.A. Rudrapatna et al. *"MEDAL: Sequential adapter learning for privacy-preserving multicenter clinical language models."* **Journal of Biomedical Informatics** 2026.
- **Alert channels.** George Hripcsak new-related.
- **Snippet.** "Scalable reasoning over clinical notes is a major goal in medical artificial intelligence. Large Language Models (LLMs) are promising for this task, particularly when fine-tuned on multicenter note corpora, but progress has been…"
- **Thread mapping.** `Causal inference and pharmacoepidemiology → Federated / privacy-preserving EHR causal analytics`; secondary `EHR foundation models → CLMBR / MOTOR / MEDS lineage` (federated fine-tuning is a natural cousin to federated EHR FMs).
- **Why HIGH.** Sequential adapter learning (LoRA / prefix-tuning / IA³) is a natural fit for the "each site trains an adapter on local notes, adapters compose without ever pooling raw notes" federated pattern. The `Federated / privacy-preserving EHR causal analytics` sub-thread already tracks the Jang et al. arXiv 2607.17958 design pattern for federated mediation / TTE; MEDAL adds a language-model analogue that could underpin federated LLM-based note phenotyping across N3C / OHDSI-network sites.
- **Open questions.** (i) How does MEDAL handle site-specific adapter drift when the note distributions differ (MIMIC vs. community-hospital notes)? (ii) Does the paper include a membership-inference / MIA-scFM-style contamination audit — a privacy claim without an inference-attack evaluation is not complete? (iii) What are the compute + storage costs vs. LoRA-swap baselines and full-fine-tune baselines? (iv) Is the code released (which framework — PEFT / transformers)?
- **Follow-up.** Read; consider adding a bullet to the federated-EHR sub-thread of `INTERESTS.md`.

### 11. Lautman et al. — Interpretable workflow for cohort phenotyping using longitudinal wearable data

- **Citation.** Z. Lautman, C. Chang, E. Rangan, M. Hittle, C. Uwakwe et al. *"An interpretable workflow for cohort phenotyping using longitudinal wearable data."* **IEEE Journal of Biomedical and Health Informatics** 2026.
- **Alert channels.** Michael Snyder new articles.
- **Snippet.** "Consumer wearable devices non-invasively capture continuous physiological and behavioral signals, positioning them as promising tools for precision medicine applications, in particular disease diagnostics."
- **Thread mapping.** `EHR phenotyping & OMOP → NLP / LLM extraction for phecode and HPO term assignment` (adjacent — same downstream endpoint); secondary `Machine learning for precision health` (wearable-derived phenotype for individualized-risk).
- **Why HIGH.** Wearables → cohort-phenotype is where the sleep-stage × PheWAS lineage (Luo et al. *PLOS Medicine* 2026, last report) needs to land as a general framework rather than one-outcome-at-a-time. The Lautman workflow's *interpretability* emphasis (which is a paper-of-Snyder-lab-style hallmark) is important because wearable-phenotyping in AoU / UKB accelerometry will need to survive external review on the same interpretability grounds that clinical-NLP phenotype pipelines do.
- **Open questions.** (i) Cohort — Snyder-lab Stanford Digital Health Study, UKB accelerometry, or new? (ii) Which diseases were phenotyped and against what ground truth (physician-adjudicated, ICD-derived, chart-review)? (iii) How does the interpretability layer surface — SHAP / attention / rule-list? (iv) Are the phenotyping outputs mappable to phecodes / HPO terms downstream?
- **Follow-up.** Read; add to the growing wearable-phenotyping cluster (Luo et al. sleep-stage PheWAS + Netten et al. Lifelines accelerometry × health-outcome + this one).

### 12. Vichentijevikj, Mishev & Misheva — GeneResolver

- **Citation.** I. Vichentijevikj, K. Mishev, M.S. Misheva. *"GeneResolver: A Traceable Hybrid Multi-Agent Pipeline for Etiology-Aware Gene Prioritization."* Research Square 2026 preprint (rs-10915520).
- **Alert channels.** Tiffany J Callahan new-related.
- **Snippet.** "Rare-disease diagnosis requires the integration of clinical phenotypes, genomic variants, inheritance patterns, and heterogeneous biological evidence. Existing gene-prioritization tools commonly assume that a disorder is caused by a…"
- **Thread mapping.** `Rare disease → Auditable HPO-driven diagnostic benchmarks with separable metrics for ranking vs. evidence coverage`; secondary `Knowledge representation in EHRs and applications → NLP-derived representations from clinical notes` and `Knowledge graphs & ontologies` (HPO reasoning).
- **Why HIGH.** The **traceable** modifier in the title is the key claim — the auditable-benchmark sub-thread has been asking for pipelines that expose per-step evidence rather than a single scalar score, and multi-agent pipelines where each agent can be inspected for its reasoning + citation are the right architecture for that. Together with Ghasemnejad et al. arXiv 2609.19569 (the ReAct+RAG severity classifier from the last report), this is the second on-thread agentic rare-disease diagnostic paper this month.
- **Open questions.** (i) Which multi-agent framework (LangGraph / crewAI / bespoke)? (ii) Which LLM backbone? (iii) Benchmark used (Mackenzie's Mission, GraphRareBench, DDD / 100kGP)? (iv) How does "etiology-aware" show up operationally — separate agents for AD/AR/XL inheritance, separate agents for mechanism (LoF vs. GoF), or a single reasoner? (v) What is the head-to-head vs. Phenolyzer / Phen2Gene / PhenoSV / LIRICAL / Exomiser / PhenoGPT2 baseline stack?
- **Follow-up.** Read preprint at first opportunity; add to the agentic-rare-disease-diagnostic tracking list.

### 13. Lefkowitz, Eisenberg, Huang, Mudunuri et al. — Machine-Readable Database for Genotype-Phenotype Analyses in Rare Diseases

- **Citation.** M.E. Lefkowitz, S.G. Eisenberg, R. Huang, U.S. Mudunuri et al. *"Machine-Readable Database for Genotype-Phenotype Analyses in Rare Diseases Using FKTN-related Congenital Muscular Dystrophies as a Prototype."* Research Square 2026 preprint (rs-10856264).
- **Alert channels.** Zhiyong Lu new articles.
- **Snippet.** "The FKTN-related muscular dystrophies are a subtype of highly heterogeneous, ultra-rare genetic diseases that are part of the α-dystroglycanopathies (αDGs). These disorders present with different prevalences depending on the population and cause…"
- **Thread mapping.** `Rare disease → Data-driven reanalysis of unsolved cases at 10k+ cohort scale` (in spirit — reanalysis needs machine-readable phenotype-genotype); secondary `Variant interpretation` (specifically the α-dystroglycanopathy locus with high VUS burden) and `Knowledge representation in EHRs and applications → Concept normalization and vocabulary mappings`.
- **Why HIGH.** Two things pull it to HIGH: (i) Lu-lab tooling, which places it in an infrastructure tradition (PhenoTagger, PhenoRerank, GeneAgent) that has downstream reach across the biomedical NLP field; (ii) the prototype target — FKTN-related congenital muscular dystrophies — is an ultra-rare, phenotypically heterogeneous, high-VUS locus where machine-readable G-P databases would directly move ACMG-AMP reclassification. If the schema is portable to other ultra-rare loci it becomes a template for the pre-symptomatic phenoconversion prediction sub-thread's raw data layer.
- **Open questions.** (i) What is the schema — OMOP-CDM extension, FHIR Genomics, JSON Schema, GA4GH Phenopackets? (ii) Which upstream data (LOVD? ClinVar? published case reports NLP-mined? DECIPHER)? (iii) Is HPO-based phenotype encoding used, and how are ordinal severity levels encoded? (iv) Is code + schema released, and how does it interoperate with ClinGen VCEP curation workflows?
- **Follow-up.** Read preprint; if the schema is portable, consider tracking as a candidate substrate for the Uria-Regojo 10k-scale reanalysis pattern in the CFTR / RYR1 / α-DG loci.

### 14. Kingsmore & Delatycki — Genomic Screening for Infants and Reproductive Adults

- **Citation.** S.F. Kingsmore, M. Delatycki. *"Genomic Screening for Infants and Reproductive Adults."* **Annual Review of Medicine** 2026.
- **Alert channels.** 7 new citations to Bryan Traynor.
- **Snippet.** "Recent progress in genomic sequencing, bioinformatics, cloud computation, and artificial intelligence is advancing a more mature understanding of the architecture of childhood genetic diseases. This knowledge and these technologies are enabling expanded genomic screening of infant and reproductive adult populations."
- **Thread mapping.** `Genetic epidemiology → Composite risk models` (framing); `PheWAS / phecode infrastructure → penetrance estimation for monogenic variants under population-screening conditions` (directly the framing the PheWAS thread cares about); `Variant interpretation`.
- **Why HIGH.** Annual Review pieces are read broadly outside the immediate genomics community, so citation is worth tracking. More importantly for this account, the population-screening framing — including reproductive-adult carrier screening and NBSeq / BabySeq — is exactly the ascertainment-context contrast the PheWAS penetrance sub-thread is built around (population-screening vs. clinical-ascertainment differences in penetrance / expressivity). Kingsmore's own BabySeq / NBSeq lineage is one of the field's principal population-screening evidence generators.
- **Follow-up.** Read at first opportunity; use as the anchor citation for the "population-screening framing of penetrance" argument in future writing.

### 15. Greenberg et al. — Drug screen + ML predict neuroprotective agents in a preclinical human model of childhood dementia

- **Citation.** Z. Greenberg, E. McDonald, A. Noreña Puerta, M.I. De Silva, C. Christensen, R. Adams, J. Tran, P. Mazzachi, S. Loskarn, S.N. Mubarokah, L. Winner, D. Neavin, M. Maack, K.L. Elvidge, L. Melton, M.R. Hutchinson, K.M. Hemsley, N. Smith, C. Bardy. *"Drug screen and machine learning predict neuroprotective agents in a preclinical human model of childhood dementia."* **Nature Communications** 17(1):9980, 2026. PMID 42764280.
- **Alert channels.** NCBI PubMed saved-search "drug repurposing" (09-21).
- **Thread mapping.** `Drug repurposing → computational identification of new indications for approved drugs`; secondary `Rare disease` (childhood dementia — CLN / NCL / MPS phenotypes are ultra-rare with high phenotype burden).
- **Why HIGH.** Wet-lab drug screen + ML on a preclinical human model of childhood dementia is exactly the "chemistry-plus-clinical-evidence loop" the drug-repurposing thread prioritizes over pure chemistry-only or target-only pipelines. Nat Commun venue signals adequate power / replication. Childhood dementia (CLN3, MPS, NPC1) is a candidate space for CFTR-modulator-analogue small-molecule stabilizer strategies, so downstream method-transfer is plausible.
- **Open questions.** (i) Which preclinical human model (iPSC-derived neurons, cerebral organoids, patient-derived neurons)? (ii) What ML model class — random forest / GNN / VLM on high-content imaging? (iii) Are the predicted neuroprotective agents pharmacologically annotated to any approved-in-adult indications, and if so, any of them adjacent to CFTR modulators, statins, or metformin (the tracked repurposing classes)? (iv) What was the validation strategy — held-out compounds + phenotypic rescue in orthogonal assay?
- **Follow-up.** Read; check whether any of the top hits overlap with the CFTR-modulator-repurposing lineage.

### 16. Peng et al. — Genetic evidence suggests a protective role of immunoglobulin M in Alzheimer's disease (All of Us)

- **Citation.** S. Peng, G. Butler-Laporte, S.C. Johnson, C.D. Engelman, T. Lu. *"Genetic evidence suggests a protective role of immunoglobulin M in Alzheimer's disease."* **Alzheimer's & Dementia** 22(9):e71865, 2026. PMID 42764449.
- **Alert channels.** NCBI PubMed saved-search "All of Us" (09-21).
- **Thread mapping.** `Biobanks with EHR linkage: All of Us, UK Biobank, MVP, BioVU`; secondary `Genetic epidemiology → Mendelian randomization` (implied by "genetic evidence" framing).
- **Why HIGH.** AoU-tagged paper (assuming the PubMed alert triggers on "All of Us" mention in the paper text) on an MR-flavor genetic-causal claim in AD — the exact intersection the biobank + causal-inference threads sit on. IgM as a protective factor is a testable proteomic hypothesis with UKB Olink data as the external validation cohort.
- **Open questions.** (i) Confirm whether AoU is a genetic instrument source or a validation cohort — the alert only surfaces the search term. (ii) Which IgM subclass / MHC-associated variants were the instruments? (iii) Was the analysis two-sample or single-sample MR, and were pleiotropy sensitivity analyses (Egger, weighted-median, MR-PRESSO) reported? (iv) External replication in UKB Olink / AoU proteomics?
- **Follow-up.** Full-text read to confirm AoU role.

### 17. Pederson et al. — Clinical modifiers of the association between type 1 diabetes and dementia incidence (All of Us)

- **Citation.** A.M. Pederson, P. Buto, S.C. Zimmerman, M. Velez, K.D. Sims, A.R. Murchland, J. Wang, M.M. Glymour, N.L. Spartano, J. Weuve, P. Gilsanz, F. Chi, R.A. Whitmer, A.T. Brennan. *"Clinical modifiers of the association between type 1 diabetes and dementia incidence."* **Alzheimer's & Dementia** 22(9):e71799, 2026. PMID 42764447.
- **Alert channels.** NCBI PubMed saved-search "All of Us" (09-21).
- **Thread mapping.** `Biobanks with EHR linkage: All of Us`; secondary `Chronic disease clustering and multimorbidity → cardiometabolic disease trajectory`; also `Machine learning for precision health → treatment-effect heterogeneity` (indirectly — the "clinical modifiers" framing).
- **Why HIGH.** T1D → dementia is a growing observational signal with known heterogeneity by hypoglycemia burden, HbA1c control, and vascular comorbidity. A biobank-based multi-modifier decomposition is exactly the multimorbidity-trajectory framing the thread cares about, and the AoU-taggability is what pulled it into the alert.
- **Open questions.** (i) Which AoU EHR-tables were used for T1D ascertainment (glycemic phenotypes vs. ICD)? (ii) Which modifiers were tested — HbA1c variability, CGM-era vs. pre-CGM, insulin-pump vs. MDI, hypoglycemia frequency, kidney function, cardiovascular events? (iii) Was ascertainment bias for early-vs-late-onset T1D handled (an early-onset T1D cohort has longer diabetes exposure at any dementia-assessment age)? (iv) External validation in UK Biobank / SEARCH for Diabetes in Youth?
- **Follow-up.** Read; use as an example of multimorbidity-trajectory decomposition in AoU for the multimorbidity thread's ongoing curation.

---

## Supplementary reports (on-thread supporting items, briefer)

### Doumat, Iyer & Jain — Medical issues and pulmonary outcomes in CF and bronchiectasis (Curr Opin Pulm Med 2026)

Review-level piece from Ostroff lab lineage (adjacent). CF/bronchiectasis
clinical review — on-thread for the CF disease thread but not a primary
research finding; useful as an update citation on the "medical issues"
side of CF outcomes as the modulator era continues.

### Um, Adelman & Pollina — Fault Lines in the Genome: Somatic DNA Mutations in Aging and Neurodegeneration (Annu Rev Pathol 2026)

Annual-Review piece; on-thread for the somatic-mosaicism sub-thread
(CHIP / VEXAS / LOY) as broader context linking somatic mutations to
aging phenotypes. Also relevant to the QC-layer concern (Ji et al.
*Biology* 2026 already tracked) about somatic-mutation contamination of
germline rare-variant scans.

### Le Guellec, Celi et al. — The Dead Science Theory (J Epid Popul Health 2026)

Short meta-epidemiology piece. Reproducibility-and-open-science framing
paper — useful context for the ongoing pretraining-contamination audit
sub-thread and the Pollet & McDermott arXiv 2609.18134 methods-hygiene
paper from the last report.

### Chi et al. — Trustworthy AI for disease pathogenesis and precision medicine (Genes & Diseases 2026)

METHODS-WATCH review of trustworthy-AI frameworks across multi-omics,
imaging, digital pathology, EHR, and longitudinal RWD. Cites the
target-trial framework for causal inference from observational data —
tie-in to the causal-ML + trustworthy-AI intersection.

### Chen et al. — Cell-type-specific eQTLs underlie the genetic architecture of complex traits (Nature 2026)

METHODS-WATCH foundational paper on how cell-type-specific eQTLs
mediate complex-trait genetics; tie-in to the Perée IBD-repurposing
paper above and to the PGS × cell-type expression sub-thread.

### Seth et al. — FHIR Data Mapping Quality Assessment: Scoping Review + Expert-Informed Requirements (Comp Struct Biotech 2026)

Pascal Brandt-feed. On-thread for `Knowledge representation in EHRs
and applications → Interoperability standards and their representational
consequences` (FHIR data mapping quality is the exact topic Lemieux
et al. *JAMIA Open* 2026-07 tracks as the reference framing paper).
Useful supplementary reference for the FHIR-quality corner of the
knowledge-representation thread.

### Nolan et al. — Promoting access and trust: cohort and data profiles in BMJ Medicine (2026)

Editorial by Nolan, Davies, Harron, Islam, Cook framing how BMJ
Medicine will handle cohort- and data-profile papers going forward.
Not a research paper but useful reference for the biobank-transparency
side of `Biobanks with EHR linkage` and the reproducibility framing
around published cohorts.

### Zhou et al. — Statins as Repurposed Anticancer Agents: Regulated Cell Death, TIME, and Translational Evidence Gap (Drug Dev Res 2026)

NCBI PubMed alert. Review-level paper on the well-worn statin-repurposing
question. On-thread for `Drug repurposing → EHR-based repurposing
signals` and pairs with the ongoing statin-discontinuation sub-thread
under `Pharmacogenomic modifiers of medication persistence`.

---

## METHODS-WATCH & interesting-but-off-thread (from alert wave)

- **Wen — DR monotonic survival curves (Int J Biostat)** — see item 7.
- **Chi et al. — Trustworthy AI review (Genes & Diseases)** — see above.
- **Chen et al. — Cell-type-specific eQTLs (Nature)** — see above.
- **Zheng et al. medRxiv — Absorption and Co-expression Modules show where polygenic and proteomic risk scores diverge in neurodegenerative diseases** (Denny feed) — pairs with the pre-symptomatic phenoconversion / Ran-Benatar ALS trajectory sub-thread; framing on where PGS and proteomic RS should NOT be treated as interchangeable is directly useful.
- **Shi et al. medRxiv — Selection bias in MR with adjustment for medication use** — see item 6 (elevated to HIGH there because it directly serves the drug-target-MR sub-thread; also listed here as a methods-watch anchor for future MR interpretation writing).
- **Lekka et al. npj Genomic Medicine — Resolving the complex CES1 locus with Cas9-directed long-read** — pharmacogenomics infrastructure paper (CES1 metabolizes ester-containing drugs and endogenous lipids). Adjacent to the CFTR-modulator PGx sub-thread if CES1 turns out to modulate ivacaftor/tezacaftor conversion or metabolism.
- **Meyer et al. bioRxiv — Evaluating Aggregated Gene-Level eQTL Scores** — TWAS methodology, tie-in to the composite-risk thread's PRS × TWAS stacking framing.
- **Lee et al. Adv Sci — Cas9-Enriched Nanopore Workflow for Clinical Diagnosis of Repeat Expansion Disorders** — rare-disease diagnostic infrastructure (STR expansion detection).
- **Zhang et al. Bioinformatics — nf-core/pacsomatic** — PacBio HiFi somatic pipeline; bioinformatics-infrastructure watch, primarily relevant if the somatic-mosaicism thread runs long-read follow-ups.
- **Henry et al. Epilepsia — Biallelic RNU2‐2 DEE characterization** — rare-disease phenotype paper (RNU2-2 is a spliceosomal ncRNA on the boundary of "gene of uncertain function" and "highly conserved essential regulator"); on the ncRNA / non-coding rare-variant frontier.
- **Wang et al. Nat Cardiovasc Res — Multiancestry PRS improves HCM stratification** — see item 3.
- **Bakr et al. — MEDAL** — see item 10.

## SKIP (incidental keyword hits, not worth attention this window)

- Linde et al. Lancet Respiratory — Duration of TB preventive treatment (off-thread).
- Abedi et al. JAMA Network Open — Single vs multiple-dose antibiotic prophylaxis for THA (TTE lineage but off-disease).
- Ahuja & Ahuja — Environmental Ethics in Endoscopy (incidental cite).
- Hu & Zhang — Donanemab RCT meta-analysis (off-thread).
- Helle et al. Sci Rep — Economic stress and birth sex ratios in Finland (incidental cite).
- Lu et al. JAMA Network Open — RSV vaccine effectiveness (off-thread).
- Wang et al. Genes — Immune-related MR signals for anxiety, CD40 locus (off-thread specific-disease).
- Jiang, Wang & Xu — MST1/CPNE1 in breast cancer MR (off-thread).
- von Brauchitsch et al. Epilepsia — PRS × phenotype in generalized epilepsy (off-thread disease).
- Kumar et al. medRxiv — m6A methylation across brain regions in AUD (off-thread).
- Wang et al. Osteoarthritis Cartilage — DNAJB12 obesity → KOA MR (off-thread).
- Karamveer et al. Nat Commun — BEAR-GRN single-cell GRN inference benchmark (off-thread infrastructure).
- Gao et al. Comm Biol — Silkworm rare variants (off-species).
- Chen et al. Eur Arch Psychiatry — MDD/ALC single-cell transcription (off-thread).
- Song et al. Sci Adv — Multiomics of regular exercise (off-thread).
- Alavi et al. Genome Biology — dicast structural variant detection (bioinformatics; nice but methods-only).
- Martella et al. Nucleic Acids Research — Large serine recombinase gene insertion (off-thread).
- Boßelmann & May Hum Mol Genet — Mutation rate + cancer-somatic-variants improve epilepsy interpretation (already reported in the 09-21 report as part of the epilepsy interpretation cluster).
- Ho et al. arXiv — Language Models Can Control Their Own Attention (Zitnik feed; ML infrastructure; off-thread).
- Karetnikov, Rahwan & Svetinovic Nat Comp Sci — LLMs as human proxies (Natarajan feed; off-thread).
- Pizzagalli, Porta & Wortel Front Immunol — AI-driven advances in immunology editorial (Kastner feed; off-thread).
- He & Zhao Medicine — Bibliometric of AI × depression (Brandt citations; off-thread).
- Kehaya & Korkmaz Namık Kemal Tıp — Serum LDH in stroke (off-thread).
- Wang et al. Angew Chemie — Metalloenzyme design (Baker feed; off-thread).
- Praestegaard & Paja — Response consistency in consumer-facing LLMs (Bastarache citations; off-thread).
- Muzammal et al. Med Data Min — bioinformatics tools review (Karczewski feed; off-thread).
- Viteri et al. Neurobiol Dis — Cellular senescence in ALS TDP-43 mice (Traynor feed; off-thread).
- Huang et al. Transl Neurodegeneration — PINK1-parkin species dependence (Traynor feed; off-thread).
- Ye et al. J Mol Neurosci — Oxidative stress genes / neurodegen MR (off-thread).
- Liu et al. Medicine — Metabolites / cerebral-volume / ALS 2-step MR (off-thread specific-disease).
- Dinh et al. Front Med — Air pollution / COPD / anemia (Traynor feed; off-thread).
- Gan-Or Brain — GBA1 in PD review (Traynor feed; off-thread specific-disease).
- Czyzewski, Szczodrak & Zielonka — Multi-Agent Medical Board LLM (Szolovits citations; medium — agentic-clinical-AI adjacent but generic).
- Vázquez et al. arXiv — Shroom-visions hallucination detection VLM shared task (Szolovits feed; off-thread).
- Tartof et al. — RSVpreF effectiveness (Ryan feed; off-thread).
- Q. Wang et al. Hum Reprod Open — PES in best-prognosis PGT cycles (elevated to HIGH item 2's supplementary but strictly borderline; kept in HIGH for the PGS-methodology framing).

---

## Cross-cutting notes

**1. One massive same-batch multi-feed hit is a Sanchez-cirrhosis-GWAS signal.** Five feeds firing the same paper (Denny, Zeng, Bastarache, Yuan Luo, Jian Yang) is unusually strong same-batch concordance and consistent with the paper being genuinely central to the multi-ancestry GWAS methods lineage this account tracks.

**2. Composite-risk sub-thread now has three complementary papers.** PRS-CARV (Zhang et al.) for summstats-only rare-variant + PGS integration; Bal et al. for multiancestry PGS lift onto a Mendelian-disease Mendelian-negative subgroup (HCM); Wang et al. Hum Reprod Open for PES context-specificity. Together with the last report's Souaiaia / Baya / Vazquez tails-and-residuals framing, this is enough material for a composite-risk write-up when the thread advances.

**3. Agentic rare-disease diagnostic pipelines are becoming a real cluster.** Ghasemnejad ReAct+RAG severity classifier (last report) and Vichentijevikj GeneResolver (this report) are two on-thread multi-agent HPO-driven diagnostic tools in three weeks. The auditability / traceability emphasis in both papers is the correct direction; watch for the third paper that benchmarks all of these against Phenolyzer / Phen2Gene / PhenoSV / LIRICAL / Exomiser / PhenoGPT2 on the same held-out cohort (GraphRareBench framing).

**4. Federated + adapter-based fine-tuning of clinical LMs (MEDAL) fills a genuine gap.** The federated / privacy-preserving EHR causal analytics sub-thread had the Jang et al. mediation-TTE design pattern; MEDAL now adds a language-model analogue. Together they cover both structured-EHR and note-based federated pipelines.

**5. `arxiv-digest` remained dry for the fifth day in the recent run (09-19, 09-20, 09-21 all dry).** Nothing to explain — is well within normal daily variation for q-bio.QM / q-bio.GN / q-bio.PE / stat.AP submissions in mid-September; the pipeline is operating correctly.

**6. `arxiv-digest` sends no email notifications.** Consistent with the last three reports. On-disk digests remain the arxiv-digest feed of record for this account.

**7. No PR / CI activity to review.** No arxiv-digest-repo PRs open this window; the last two merges (PR #35, PR #36) closed before the previous report.

---

## Suggested next actions for the account owner

1. Read Sanchez et al. *Lancet Gastroenterology & Hepatology* renal-in-cirrhosis multi-ancestry GWAS first (five-feed hit).
2. Read Zhang et al. PRS-CARV preprint; if the summstats-only rare-variant + PGS framework holds, add to the composite-risk anchor citation stack.
3. Read Bal et al. *Nature Cardiovascular Research* HCM multiancestry-PRS paper as the second composite-risk anchor for the Mendelian-plus-modifier template portable to CFTR / APOL1 / BRCA / TTR.
4. Read Hellemans et al. *BMJ* multi-registry TTE for the transplant-vs-dialysis pattern; consider a US-analogue design note in the pharmacoepi thread.
5. Read Shi/Swanson/Diemer/Gerlovin medRxiv preprint on MR + medication-use selection bias; pair with the Shi/Diemer/Swanson AJE piece from the last report as the drug-target-MR "how to interpret" pair.
6. Read Perée et al. *Nat Commun* IBD cis-eQTL + entrectinib paper; cross-reference against scDEFT (last report) and the Zitnik World Models framing.
7. Read Sivaraman et al. arXiv 2609.19318 LLM-abstraction-gap paper; align with the LLM-assisted phenotyping planning under EHR phenotyping.
8. Read Vichentijevikj GeneResolver preprint; add to the agentic-rare-disease-diagnostic tracking list.
9. Read Lefkowitz et al. FKTN machine-readable G-P database preprint; if the schema is portable, consider tracking it as a candidate reanalysis substrate.
10. Read Kingsmore & Delatycki *Annual Review of Medicine* piece for the population-screening framing of penetrance.
11. Verify the AoU role in Peng et al. IgM / AD paper via full text (instrument cohort or replication cohort?).

_End of 2026-09-22 research digest report._
