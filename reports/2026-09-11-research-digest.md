# Research digest report — 2026-09-11

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-09-01 12:40Z → 2026-09-11 12:40Z** (~10 days since the
last research-digest report, covering ten daily `arxiv-digest` cron runs
and roughly a half-dozen Google Scholar alert batches, including the
09-09, 09-10, and 09-11 batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-09-01.md` → `2026-09-10.md`) | 09-01 → 09-10 daily crons | 10 daily runs. Dry days (0 papers): 09-03, 09-05, 09-06, 09-08. 09-01: 1 paper (Mansouri Ghiasi storage-centric metagenomics — off-topic, SKIP). 09-02: 1 paper (Ramesh et al. mudskipper locomotion — SKIP). 09-04: 2 papers (Cortez-Rodriguez disasters × nonprofits — SKIP; Yu et al. location-invariant extremal QTE with IPW — METHODS-WATCH). 09-07: 1 paper (Rajabli & Collins brain-age→Alzheimer FM with LoRA — METHODS-WATCH). 09-09: 2 papers (**Snel & Schulz UKB Cohen's-d attribution — HIGH**; Wu et al. HPLC RT FM — SKIP). 09-10: 1 paper (Lee et al. Kalman-smoothed HT infectious-disease prevalence — METHODS-WATCH). |
| No `arxiv-digest` email hits from GitHub | — | Search of `subject:"arxiv-digest"` and GitHub notification variants in the window returned zero threads. The pipeline continues to commit its output to this repo rather than emailing PR / cron notifications; the on-disk digests *are* the arxiv-digest feed. |
| Google Scholar alerts (09-11 batch, ~03:09Z + ~09:28Z) | 09-11 03:09Z, 09:28Z | ~30 feeds fired across two waves. Highlights (see per-paper detail below): **Chenjie Zeng — own paper published**, Zeng/Waxse/Denny *npj Digital Public Health* 2026 landed simultaneously on the `"All of Us research program"` and `"phenome wide association studies"` keyword feeds; **Walker et al. medRxiv** — AoU + Pharmlines polygenic + familial contributions to antidepressant continuation / switching / discontinuation / augmentation (Denny + Karczewski + Bastarache + Jian Yang author feeds all landed on it); **Ellershaw et al. arXiv 2608.16273** — Foresight-England national-scale generative EHR-FM (Hripcsak author feed); **Zhang et al. *Genomics, Proteomics & Bioinformatics* 2026** — Bayesian colocalization benchmarking for MR-identified targets (Jian Yang author feed); Roberts et al. *IJPRAS* 2026 — polygenic pharmacotherapy evidence map (Denny author feed); Liu et al. *Genome Research* 2026 — biobank-scale G×E modulator learning (Denny author feed); Barbosa Araujo et al. *bioRxiv* 2026 — PRS pipeline from curation to reporting (Denny author feed); Dogra et al. — APOL1 kidney disease narrative review (APOL1 keyword feed); Park & Chung *Scientific Reports* — statistical-learning comparison for polygenic prediction in UKB (`"UK Biobank"` keyword feed); Renauer et al. *medRxiv* — germline CENPBP1 predisposes to glioblastoma (Karczewski + Denny citations-to feeds); Yang et al. *medRxiv* — Who seeks care, and what gets measured? EHR visit/observation processes (Hripcsak author feed). |
| Google Scholar alerts (09-10 batch, 13:52Z) | 09-10 13:52Z | 2 NCBI PubMed feeds fired (`UK Biobank`, `All of Us`) with a rolling >20-paper backlog each (day-of-week batch cadence). Signal preview only — nothing net-new above what Scholar caught. |
| Google Scholar alerts (09-09 batch, 22:32Z + 16:04Z) | 09-09 16:04Z, 22:32Z | Multiple hits. Highlights: **Ju et al. — UDCA and Parkinson's-disease risk emulated target trial in UK EHR** (`Foundation models + "electronic health records"` keyword feed AND `"electronic health records"` keyword feed); **Wu et al. *EBioMedicine* 2026 — Discovering repurposable drugs for AD/dementias via TTE in decentralised RWD** (Yong Chen author feed AND Patrick Ryan citations-to feed); **Muayad et al.** — Cumulative Atopic Disease Burden and Keratoconus in All of Us (`"All of Us research program"` feed); **Fu et al. *Nature Communications* 2026** — Cost-efficient long-read trio-barcoded adaptive sequencing improves rare disease diagnosis (Stephen Montgomery feed); **Aguilar-Ordoñez et al. *Nature Communications* 2026** — WGS of 1,427 Mexican individuals from oriGen (Denny citations-to feed); Fujimoto et al. *Nature Genetics* 2026 — multiancestry GWAS + multiomics of multiple sclerosis (with AoU replication); Rämö et al. *JACC* 2026 — genetically mediated LDL and VTE risk in AoU; Berry et al. *JACC* 2026 — monogenic ALB variants and severe hypercholesterolemia in AoU; Nagalamadaka et al. *J Affect Disord* — psychiatric conditions and central serous chorioretinopathy in AoU; Long et al. *J Hum Immunity* — HLA-B8/HLA-DQ2.5 celiac ancestry-dependent risk in AoU; Zhou et al. *STAR Protocols* — protocol for local-ancestry + cross-ancestry PRS in admixed populations; Chen et al. *JAMA Netw Open* — oral anticoagulants in AF + advanced CKD; Reizine et al. — antifungal duration and 90-day mortality in candidemia (multicenter TTE, France). |
| Google Scholar alerts (09-02 → 09-08 batches) | 09-02 → 09-08 | Lower-volume days in this window between the 09-01 batch (captured in the previous report) and the 09-09 push. Most surfaced items were absorbed by the 09-09 / 09-11 batches, which is why they are cited from those later batches below. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fourteen HIGH items surfaced this window, clustered into six knots:

**Your own paper is out (0). Zeng, Waxse & Denny (npj Digital Public
Health 2026)** — the AoU patient-mediated vs. provider-sourced EHR
replication paper landed on Scholar keyword feeds this morning, and is
now indexed under *"All of Us research program"* and *"phenome wide
association studies"*. This is your own work reaching general Scholar
visibility; you'll want to boost it wherever you syndicate.

**Pharmacogenomic-modifier-of-medication-persistence cluster (1 item).**
**Walker et al. medRxiv 2026.08.14.26360458** — polygenic and familial
contributions to antidepressant continuation, switching, discontinuation
and augmentation in **All of Us + Pharmlines** cohorts. This is a
direct, on-brand hit for the *pharmacogenomic modifier of medication
persistence* sub-thread you added to INTERESTS.md in July, and it uses
AoU as one of the two anchor cohorts — near-perfect fit. Four separate
author feeds (Denny, Karczewski, Bastarache, Jian Yang) surfaced it on
09-11, which is unusual co-signal for one preprint.

**Pharmacoepi target-trial-emulation cluster (3 items).** **Wu et al.
*EBioMedicine* 2026** — TTE-based drug repurposing for AD / related
dementias in decentralised RWD, hits both your causal-inference / TTE
thread AND the drug-repurposing thread (with an explicit
observational-real-world-data anchor). **Ju et al.** — UDCA →
Parkinson's disease risk, emulated target trial in UK EHR, direct hit
for the pharmacoepi/TTE thread and adjacent to the drug repurposing
thread. **Reizine et al.** — antifungal treatment duration → 90-day
mortality in critically ill candidemia, multicenter TTE in France; TTE
methodology exemplar for infectious-disease context (surfaced via a
Hernán citations-to feed).

**EHR foundation-model + representation cluster (2 items).**
**Ellershaw et al. arXiv 2608.16273 — Foresight-England**, the first
national-scale generative EHR-FM (pilot strictly COVID-19-scoped),
evaluating direct + indirect pandemic effects — already flagged in the
09-01 report from the Pascal Brandt feed but re-surfaced via Hripcsak
this week and now published on arXiv. **Yang et al. medRxiv
2026.08.12.26360236** — "Who seeks care, and what gets measured?" —
distinguishes visit vs. observation processes in multi-center EHR,
directly serving your `Knowledge representation in EHRs` sub-thread on
structural and temporal representation of the patient timeline (event
sequencing, representation choices that leak or preserve label
information at prediction time). Adjacent methodology paper: Snel &
Schulz arXiv 2609.07729 — training-data attribution for Cohen's d in
normative age biomarkers in UKB, on your `Digital twins from EHR data`
+ `ML for precision health` intersection.

**Genetic-epi + drug-target-MR cluster (2 items).** **Zhang et al.
*Genomics, Proteomics & Bioinformatics* 2026** — benchmarking Bayesian
colocalization methods for validating MR-identified targets. On-brand
for the *drug-target Mendelian randomisation triangulated with
observational cohort estimates* sub-thread. **Liu et al. *Genome
Research* 2026** — biobank-scale method for learning modulators of G→E
interactions; on-brand for the *GxE and PGS × exposure interactions*
sub-thread you flagged around Nagpal & Gibson 2026.

**Cross-ancestry PGS + Latin-American genomics cluster (3 items).**
**Park & Chung *Scientific Reports*** — comparative evaluation of
statistical learning methods for polygenic prediction in UKB. **Aguilar-
Ordoñez et al. *Nature Communications* 2026** — WGS of 1,427 Mexican
individuals from the oriGen cohort, an under-represented-ancestry
reference-population paper directly relevant to cross-ancestry PGS
portability. **Zhou et al. *STAR Protocols*** — protocol for leveraging
local ancestry and cross-ancestry genetic architecture to improve
polygenic prediction in admixed populations.

**Rare disease + variant interpretation cluster (2 items).** **Fu et al.
*Nature Communications* 2026** — cost-efficient long-read
trio-barcoded adaptive sequencing improves rare disease diagnosis;
mid-scale rare-disease sequencing methodology aligned with your
*data-driven reanalysis of unsolved cases* sub-thread. **Goel *Human
Mutation* 2026 — TRACE** — framework for integrating transcript
relevance into ACMG/AMP variant interpretation; direct hit for the
variant-interpretation thread on splicing / RNA evidence for VUS
resolution.

**Also-surfaced adjacent HIGHs (1 item).** **Dogra et al. — APOL1
kidney disease critical narrative review** — reviews molecular
mechanisms, clinical heterogeneity, and emerging therapeutic landscape.
On-brand for the APOL1 disease sub-thread; useful for the therapeutic
landscape framing rather than for novel results.

---

## Per-paper HIGH-priority reports

### 0. Zeng, Waxse & Denny (2026) — *npj Digital Public Health*

**Full title:** Robust replication of associations across
patient-mediated and provider-sourced EHR data in the *All of Us*
research program.

**Authors:** C Zeng, BJ Waxse, JC Denny.

**Venue:** *npj Digital Public Health* 2026 — Nature portfolio, open
access. Landed on Scholar keyword feeds for both `"All of Us research
program"` and `"phenome wide association studies"` on 09-11 09:28Z,
which is when it hit general Scholar visibility.

**Snippet from Scholar (all that came through the alert):** *"The All of
Us Research Program is assembling a nationwide cohort with electronic
health record (EHR) resources through two [pathways] … We thank all
participants of the All of Us Research Program for their generous
contributions to advancing health …"*

**Why HIGH:** it's your own paper. Trivially on-brand for the
`Biobanks with EHR linkage: All of Us …` and `Knowledge representation
in EHRs and applications` threads (the concept-normalization and
representation-fidelity sub-threads specifically — patient-mediated vs.
provider-sourced is exactly the representation-choice-and-portability
question you framed in INTERESTS.md).

**Action for this window:** consider announcing on the outlets you
syndicate through (lab site, Twitter/BlueSky, LinkedIn, mailing lists).
Now is when Scholar-user replies will land.

---

### 1. Walker et al. (2026) — medRxiv

**Full title:** Polygenic and familial contributions to antidepressant
continuation, switching, discontinuation and augmentation in the *All
of Us* and Pharmlines cohorts.

**Authors:** A Walker, X Wang, J Bos, T Lin, F Klont, I Nolte, [et al.].

**Venue:** medRxiv 2026.08.14.26360458 (posted 2026-08-24). Landed on
four author feeds simultaneously on 09-11 03:09Z — Denny, Karczewski,
Bastarache, Jian Yang.

**Snippet from Scholar:** *"Predicting antidepressant response remains a
major challenge, and it is unclear whether reported polygenic
associations reflect drug-specific non-response or a broader propensity
for treatment modification. We analysed participants with at least [one
antidepressant prescription] …"*

**Why HIGH:** direct, on-brand hit for the
*pharmacogenomic-modifier-of-medication-persistence* sub-thread you
added to INTERESTS.md under `Causal inference and pharmacoepidemiology`
in July, plus the *EHR-linked biobank: AoU* thread. The dependent
variables (continuation / switching / discontinuation / augmentation) are
exactly the persistence-side outcomes flagged in Cohen et al.
*Pharmaceuticals* 2026 as the template. The dual-cohort AoU + Pharmlines
design lets them separate polygenic score signal from familial
(family-history) confounding — which is the exact identification
question you flagged for the Psy-PGx UKB lineage.

**Portability to your existing threads:** the "propensity for treatment
modification" framing is directly portable to CFTR-modulator
persistence, statin discontinuation, HRT persistence, and GLP-1 RA
persistence (all named sub-threads). This paper is a template for how
to structure those analyses.

**Read priority:** open the medRxiv full text; the abstract cutoff in
the Scholar snippet ends before the sample-size and effect-size numbers.

---

### 2. Wu et al. (2026) — *EBioMedicine*

**Full title:** Discovering repurposable drugs for Alzheimer's disease
and related dementias: target trial emulation using decentralised
real-world data.

**Authors:** Q Wu, L Li, Y Lei, T Zhou, H Tang, B Zhang, Y Lu, [et al.].

**Venue:** *EBioMedicine* 2026, published-online (Yong Chen author
feed + Patrick Ryan citations-to feed on 09-09 16:04Z).

**Snippet from Scholar:** *"Background: Alzheimer's disease and related
dementias (ADRD) affect nearly 6.9 million Americans, with the number
expected to triple by 2050, while disease-modifying therapies remain
unavailable. Drug repurposing, which identifies new [indications] …"*

**Why HIGH:** two threads intersect. **Drug repurposing** — this is the
`causal-inference framings of off-label use (target-trial emulation of
repurposing candidates)` sub-thread you flagged as high-priority.
**Causal inference and pharmacoepidemiology** — TTE + real-world data at
scale ("decentralised real-world data" is the design pattern paralleling
Ju et al. below, and adjacent to Jang et al. 2607.17958's
federated-EHR-causal-analytics template).

**Read priority:** the *EBioMedicine* full text should specify (i) the
data network (decentralised implies distributed / cross-site), (ii) the
candidate list and screening logic, and (iii) whether they build a
sensitivity-analysis / negative-control layer. Any of those, plus the
top candidates, is what you'll want to cite alongside your CFTR-modulator
and GLP-1 pharmacoepi work.

---

### 3. Ju et al. (2026) — UCL preprint

**Full title:** Ursodeoxycholic acid and Parkinson's disease risk: an
emulated target trial in UK electronic health records.

**Authors:** C Ju, A Schrag, C Carroll, X Xiong, J Carpenter, [et al.].

**Venue:** UCL Discovery preprint (2026), running title *UDCA and
Parkinson's disease*. Landed on two keyword feeds on 09-09 22:32Z:
`Foundation models + "electronic health records"` and
`"electronic health records"`.

**Snippet from Scholar:** *"In this study, we used routinely collected
electronic health records to compare the risk … hepatobiliary disease,
may not be fully captured in routine electronic health records. This is
… neuroprotective effects in in-vitro models of Parkinson's disease …"*

**Why HIGH:** direct hit for the pharmacoepi/TTE thread and adjacent to
the drug-repurposing thread. UDCA neuroprotection in Parkinson's is a
long-standing repurposing hypothesis with mixed RCT evidence; a
well-executed UK-EHR TTE (with a hepatobiliary-indication active
comparator, if they used one) is exactly the design pattern your thread
is looking for.

**Read priority:** open the UCL Discovery PDF. Check (i) index-date
specification, (ii) hepatobiliary-disease as an indication confounder
handling, (iii) any grace-period / lookback for prevalent PD, and (iv)
whether they use negative-control outcomes to calibrate residual
confounding.

---

### 4. Reizine et al. (2026) — Hernán citations-to feed

**Full title:** Association of antifungal treatment duration with 90-day
mortality in critically ill adults with candidemia: a multicenter target
trial emulation in France.

**Venue:** (venue not shown in the truncated Scholar snippet; landed on
the Miguel Hernán citations-to feed on 09-11 03:09Z).

**Why HIGH:** methods-exemplar TTE with a treatment-duration exposure
(vs. treatment-vs-no-treatment), which is a harder specification —
useful reference for how to structure CFTR-modulator or GLP-1 duration
TTEs. Multicenter French design also relevant to your cross-site
representation sub-thread.

**Read priority:** MEDIUM — read for methodology only unless the
infectious-disease application is directly on-scope for a project.

---

### 5. Ellershaw et al. (2026) — arXiv 2608.16273 — Foresight-England

**Full title:** Foresight-England: Development of a National-Scale
Generative AI Model of Electronic Health Records for Medical Event
Prediction across the COVID-19 Pandemic.

**Authors:** S Ellershaw, C Tomlinson, Z Kraljevic, S Denaxas, [et al.].

**Venue:** arXiv preprint 2608.16273. Re-surfaced this window via the
George Hripcsak author feed (09-11 03:09Z). Already noted in the 09-01
report from the Pascal Brandt feed — flagging again because it's the
canonical reference for the *national-scale generative EHR-FM*
sub-thread.

**Abstract lead:** *"Foresight-England (Foresight-E) is the first
national-scale generative foundation model of electronic health records
(EHRs), developed as a research pilot strictly for COVID-19 research. We
evaluated its ability to model the direct and indirect effects of [the
pandemic] …"*

**Why HIGH:** field-defining reference for `EHR foundation models` at
national scale, and the paired reference for the FHIR/USCDI
representation-standards sub-thread of `Knowledge representation in
EHRs` (Lemieux 2026 was the framing paper you cited; Foresight-E is the
first FM implementation at that scale).

**Read priority:** if you didn't open the arXiv HTML yet after the 09-01
Brandt-feed surfacing, do it now — it's likely to be the citation-
handle paper for anyone comparing national-scale EHR FMs.

---

### 6. Yang et al. (2026) — medRxiv

**Full title:** Who seeks care, and what gets measured? Understanding
the distinct mechanisms behind visit and observation processes in
multi-center electronic health records.

**Authors:** CH Yang, M Salvatore, H Lu, Z Zhu, P Tennant, X Shi, [et al.].

**Venue:** medRxiv 2026.08.12.26360236, posted 2026-08-14. Landed on the
Hripcsak author feed on 09-11.

**Snippet from Scholar:** *"Electronic health record (EHR)-linked
cohorts support association, prediction, and causal studies using
longitudinally measured markers of health. However, a lab biomarker
measurement is recorded only when a patient first has a medical
[encounter] …"*

**Why HIGH:** direct hit for the *structural and temporal representation
of the patient timeline* sub-thread of `Knowledge representation in
EHRs and applications`. Separating the visit process (why a patient is
in the system) from the observation process (what gets measured
conditional on the visit) is exactly the identification issue that
biases both prediction models and observational causal analyses. The
multi-center framing is also on the *cross-site representation drift*
sub-thread.

**Read priority:** HIGH for methods borrowing to any EHR-based analysis
using labs or vitals; the framework is portable across cohorts (UKB, AoU,
BioVU, MIMIC).

---

### 7. Zhang et al. (2026) — *Genomics, Proteomics & Bioinformatics*

**Full title:** Benchmarking Bayesian Colocalization Methods in
Validating Mendelian Randomization-identified Targets.

**Authors:** W Zhang, S Yoshiji, R Sladek, J Dupuis, T Lu.

**Venue:** *Genomics, Proteomics & Bioinformatics* 2026, advance article.
Landed on the Jian Yang author feed on 09-11.

**Snippet from Scholar:** *"Mendelian randomization (MR) is an important
tool for identifying potential biomarkers and drug targets.
Colocalization analysis is crucial for validating MR findings and
guarding against confounding due to linkage disequilibrium. We aim to
[compare] …"*

**Why HIGH:** direct hit for the *drug-target Mendelian randomisation
triangulated with observational cohort estimates* sub-thread (Saxby et
al. metformin × AAA; MR-ALasso lineage). Colocalization is the standard
LD-confounding safeguard, and a benchmarking paper across methods (coloc,
SuSiE-coloc, HyPrColoc, PWCoCo, etc.) is a citation-handle paper.

**Read priority:** MEDIUM-HIGH; read enough to know which method they
recommend and under what SNP-density / power regime.

---

### 8. Liu et al. (2026) — *Genome Research*

**Full title:** A biobank-scale method for learning modulators of [G→E
interactions] (title truncated in the Scholar entry).

**Authors:** Z Liu, A Ramteke, A Anand.

**Venue:** *Genome Research* 2026, early-online 2026-08-17.

**Snippet from Scholar:** *"Gene–environment (G→E) interactions —
wherein the magnitude and sometimes the direction of a variant's effect
depends on environmental context — are increasingly recognized as
important contributors to the genetic architecture of complex traits …"*

**Why HIGH:** direct hit for the *GxE and PGS × exposure / environment
interactions* sub-thread you flagged under `Genetic epidemiology` (with
Nagpal & Gibson *Nature Genetics* 2026 as the reference). Biobank-scale
methodology is the piece of the puzzle you specifically flagged (not
another single-locus interaction paper).

**Read priority:** open for method + benchmarks. If they use UKB / AoU
as biobanks, worth reading for cross-cohort transfer of the modulator
identification.

---

### 9. Park & Chung (2026) — *Scientific Reports*

**Full title:** Comparative evaluation of statistical learning methods
for polygenic prediction in UK Biobank.

**Authors:** S Park, W Chung.

**Venue:** *Scientific Reports* 2026 (Nature portfolio). Landed on the
`"UK Biobank"` keyword feed on 09-11.

**Snippet from Scholar:** *"We further validated our findings using UK
Biobank …"* (abstract truncated).

**Why HIGH:** on-brand for the `Genetic epidemiology` thread and the
*multi-omics-augmented PRS* sub-thread as a baseline-methods reference.
Benchmarking papers like this are useful for choosing the PRS pipeline
in AoU or MVP work where you're aiming for cross-ancestry portability.

**Read priority:** MEDIUM; skim tables and pick out which methods
outperform (Lassosum / PRS-CS / LDpred2 / SBayesR / PRScsx / DBSLMM /
GNN-based methods) at what heritability × sample-size regime.

---

### 10. Aguilar-Ordoñez et al. (2026) — *Nature Communications*

**Full title:** Whole genome sequencing of 1,427 Mexican individuals
from the oriGen cohort.

**Authors:** I Aguilar-Ordoñez, E Guzman-Cerezo, [et al.].

**Venue:** *Nature Communications* 2026. Landed on the Denny
citations-to feed on 09-09.

**Snippet from Scholar:** *"Latin American populations remain
underrepresented in [genomic studies] …"*

**Why HIGH:** directly serves the cross-ancestry portability agenda in
your `Genetic epidemiology` thread. A well-sized Mexican reference
resource is directly usable for downstream fine-mapping and PGS
portability work, and complements the UKB-heavy default.

**Read priority:** MEDIUM; scan for (i) rare-variant discovery rate vs.
gnomAD, (ii) PGS residual-imputation performance, and (iii) admixture
structure (Amerindian, European, African).

---

### 11. Zhou et al. (2026) — *STAR Protocols*

**Full title:** Protocol for leveraging local ancestry and cross-ancestry
genetic architecture to improve polygenic prediction in admixed
populations.

**Authors:** G Zhou, I Yolou, Y Xie, H Zhao.

**Venue:** *STAR Protocols* 2026. Landed on the Denny author feed on
09-09.

**Why HIGH:** protocol paper for admixed-population PGS. Directly on-
brand for cross-ancestry portability, and specifically for the local-
ancestry deconvolution approach (relevant to AoU African-American and
Hispanic subgroups where global-ancestry PRS underperforms).

**Read priority:** HIGH-if-in-scope; open only when you're about to
apply admixed-cohort PGS.

---

### 12. Fu et al. (2026) — *Nature Communications*

**Full title:** Cost-efficient long-read trio-barcoded adaptive
sequencing improves rare disease diagnosis.

**Authors:** Y Fu, AC English, LF Paulin, SN Jhangiani, N Gogate, [et
al.].

**Venue:** *Nature Communications* 2026. Landed on the Stephen
Montgomery citations-to feed on 09-09.

**Snippet from Scholar:** *"Rare diseases often [require targeted
sequencing at scale] …"*

**Why HIGH:** direct hit for the `Rare disease` thread, and adjacent to
the *data-driven reanalysis of unsolved cases at 10k+ cohort scale*
sub-thread (Uria-Regojo et al. medRxiv 2026 was the mid-scale reference
you had; this is a sequencing-methodology angle on the same
undiagnosed-rare-disease problem).

**Read priority:** MEDIUM-HIGH; read for (i) trio-barcode multiplexing
economics and (ii) whether they benchmark diagnostic yield against
standard short-read WGS.

---

### 13. Goel (2026) — *Human Mutation*

**Full title:** TRACE: A Framework for Integrating Transcript Relevance
Into ACMG/AMP Variant Interpretation.

**Author:** H Goel.

**Venue:** *Human Mutation* 2026. Landed on the
`"variant interpretation" OR "variant classification"` keyword feed on
09-11.

**Snippet from Scholar:** *"Background: Accurate clinical variant
interpretation depends on the [transcript context] …"*

**Why HIGH:** direct hit for the `Variant interpretation (ACMG /
ClinGen)` thread, specifically the *splicing / RNA evidence for VUS
resolution* sub-thread. TRACE-style transcript-relevance integration is
exactly what the ClinGen VCEP guidance is moving toward but often lacks
tooling for.

**Read priority:** MEDIUM; open if you're doing any VUS-classification
work, otherwise citation-file only.

---

### 14. Snel & Schulz (2026) — arXiv 2609.07729

**Full title:** Attributing Cohen's d: Training Data Attribution for
Disease-Related Effects in Normative Age Biomarkers.

**Authors:** J Snel, M-A Schulz.

**Venue:** arXiv preprint 2609.07729v1, primary category cs.LG.
Surfaced by the local `arxiv-digest` run on 09-09 with score = 2 on the
`uk biobank`, `biobank` keywords.

**Abstract lead (from arxiv-digest):** *"Normative age models are
trained to predict chronological age in a nominally healthy cohort.
Applied to patients, they deviate, and the gap between predicted and
chronological age is read as disease risk. Here, we attribute the
disease-related effect size of the age gap directly to individual
training samples, rather than using a prediction-level loss as the
attribution target. For Cohen's d, the resulting closed-form influence
functional, validated against leave-one-out retraining, ranks training
samples by their effect on held-out case-control separation. Across four
diseases and two biomarker modalities in UK Biobank, removing the 10%
most influential training samples raises held-out disease-related effect
size in every seed. It more than doubles the metabolomic-age effect for
type-2 diabetes and raises the brain-age effect for multiple sclerosis
by roughly a third. Random removal leaves effect size flat even at 50%
removal, confirming the gain comes from which samples are removed, not
how many. Flagged subjects carry subclinical cardiometabolic burden that
diagnosis-based exclusion misses, on markers the model never sees. For
type-2 diabetes, where the method gains most, the marker recovered is
HbA1c, the standard measure of blood sugar control. We release
pyinfluence, our influence-function package, for reproducibility and
reuse."*

**Why HIGH:** direct-hit intersection of *Digital twins from EHR data*
(brain-age / metabolomic-age as digital-twin-adjacent biomarkers under
your `EHR foundation models` thread), UKB as biobank, AND
representation-fidelity concerns (the "flagged subjects with subclinical
cardiometabolic burden that diagnosis-based exclusion misses" finding
is exactly the training-data-contamination issue you flagged in
INTERESTS.md's *pretraining-contamination audits for foundation-model
benchmarks* sub-thread — Ali arXiv 2607.20572 scContam / MIA-scFM).

**Read priority:** HIGH; open the arXiv PDF. `pyinfluence` is a portable
tool that could be applied to your CLMBR / MOTOR / MEDS benchmark
contamination auditing.

---

## METHODS-WATCH secondary reports

The following were surfaced this window but are off-primary-topic or
methodology-only; keep in citation file rather than deep-read.

### Rajabli & Collins (2026) — arXiv 2609.05400

Alzheimer's brain-MRI feature extractor: freezes a 7.18M-weight 3D CNN
brain-age model, adapts to each task with LoRA (~1% additional
parameters), holds AUC 0.964 on ADNI dementia and 0.871 unchanged on
OASIS-3. **METHODS-WATCH for the brain-age-as-FM adjacency** with Snel &
Schulz above; not on your primary Alzheimer thread but a good example of
compact-supervised-model → foundation-model repurposing that could
transfer to your EHR-FM pretraining-audits work.

### Yu et al. (2026) — arXiv 2609.04018

Location-invariant estimator of extremal quantile treatment effects for
heavy-tailed distributions, using IPW. **METHODS-WATCH for the causal-ML
tail-behavior sub-thread**; adjacent to the Leimenstoll causal effects
in extremes paper you flagged in the 08-25 arxiv-digest run.

### Lee et al. (2026) — arXiv 2609.09325

Kalman filtering and smoothing for improving precision in Horvitz–
Thompson estimation of infectious disease prevalence, with delete-a-
group jackknife for observation variances and a joint local-linear-trend
state-space model. **METHODS-WATCH for surveillance / IPW +
state-space** methodology; not on your active disease threads.

### Roberts et al. (2026) — *IJPRAS*

*Polygenic Pharmacotherapy beyond Single-Gene Rules: An Evidence Map of
Scores, Interactions, Ancestry Transferability, and Clinical Utility.*
Landed on the Denny author feed on 09-11. Framing / review paper — no
new empirical results, but the ancestry-transferability + PGS + clinical
utility bundling maps directly to your INTERESTS.md structure. **Read as
citation file only.**

### Barbosa Araujo et al. (2026) — bioRxiv

*From Data Curation to Risk Reporting: A Pipeline for Polygenic Risk
Scores.* Standardized-pipeline paper (data curation → risk reporting).
**METHODS-WATCH** for the operational side of a PRS deployment.

### Renauer et al. (2026) — medRxiv

*Germline Variants in Centromere Binding Protein 126 Predispose to
Glioblastoma.* Surfaced via Karczewski + Denny citations-to feeds. On-
brand for cancer-genetics rare-variant thread but adjacent to your core
disease threads. Read only if glioblastoma is directly on-scope.

### Fujimoto et al. (2026) — *Nature Genetics*

*Multiancestry genome-wide association and multi-omics analyses
elucidate spatiocellular features of multiple sclerosis genetics.* AoU
replication is used. **METHODS-WATCH for cross-ancestry multi-omics
integration**; not on your core disease threads but strong example.

### Muayad et al. (2026) — *American …* [ophthalmology]

*Cumulative Atopic Disease Burden and Keratoconus: Cross-Sectional and
Longitudinal Associations in the All of Us Research Program.* AoU
cohort application to an off-topic disease pair. Cite as example of AoU-
based longitudinal cohort analysis — not on your primary disease
threads.

### Long et al. (2026) — *J Human Immunity*

*Linkage between HLA-B8 and HLA-DQ2.5 contributes to ancestry-dependent
risk for celiac disease.* AoU celiac cohort, ancestry-stratified — a
methods exemplar for HLA-haplotype ancestry-dependent risk (analogous to
the APOL1 kidney disease framing).

### Rämö et al. (2026) — *JACC*

*Genetically Mediated Differences in LDL Cholesterol and Risk of Venous
Thromboembolism.* AoU truncating-variant and AlphaMissense-damaging
analyses. **METHODS-WATCH** for the composite-risk-model +
AlphaMissense-annotation pattern you flagged as *tails-and-residuals*
lever.

### Berry et al. (2026) — *JACC*

*Monogenic ALB Variants as Determinants of Severe Hypercholesterolemia.*
AoU monogenic-variant / severe-phenotype design. **METHODS-WATCH** for
monogenic-modifier-of-quantitative-trait paper design.

### Nagalamadaka et al. (2026) — *J Affective Disorders*

*Psychiatric Conditions Associated with Central Serous Chorioretinopathy
in All of Us.* AoU cross-sectional. Cite as AoU application example
only.

### Chen et al. (2026) — *JAMA Network Open*

*Oral Anticoagulants in Patients With Atrial Fibrillation and Advanced
CKD Not Requiring Dialysis.* Multi-drug pharmacoepi study surfaced via
Hernán citations-to feed. **METHODS-WATCH** for pharmacoepi design in
kidney-population subgroup (adjacent to APOL1 thread).

### Dogra et al. (2026) — narrative review

*APOL1 kidney disease: a critical narrative review of molecular
mechanisms, clinical heterogeneity, and the emerging therapeutic
landscape.* Direct APOL1 thread hit but as a therapeutic-landscape
review; useful for framing the ancestry-dependent risk + emerging
therapeutics narrative.

### Yuxiao et al. (2026)

*Molecular characteristics and clinical implications of clonal
hematopoiesis of indeterminate potential in patients with newly
diagnosed Waldenström [macroglobulinemia].* CHIP thread. Case-series
scale; interesting as an example of CHIP in a specific hematologic
malignancy context.

### Aguilar-Ordoñez et al. duplication note

The 09-09 Denny citations-to feed also surfaced Aguilar-Ordoñez et al.
oriGen (covered above as HIGH #10) — flagging so you don't double-count.

---

## SKIP (surfaced but off-scope)

- `arxiv-digest` 09-01 Mansouri Ghiasi — storage-centric systems for
  genomic analyses. Hardware / systems.
- `arxiv-digest` 09-02 Ramesh et al. — mudskipper locomotion. Off-topic.
- `arxiv-digest` 09-04 Cortez-Rodriguez — Natural Disasters and Nonprofit
  Sector. Off-topic (though uses causal-inference on panel data).
- `arxiv-digest` 09-09 Wu et al. — HPLC retention-time foundation model.
  Off-topic chemistry FM.
- Scholar 09-11 Nugraha et al. — empagliflozin PCOS drug repurposing
  molecular-simulation-only paper (drug-repurposing keyword feed, but
  target-only / chemistry-only which INTERESTS.md explicitly deprioritises).
- Scholar 09-11 Yuan et al. — LLM-driven KG for herb–macromolecule
  interaction prediction (knowledge-graph keyword feed, off-brand — TCM
  herbal not on your active drug threads).
- Scholar 09-09 Yang et al. — eGDR and GI cancer mortality in UK Biobank.
  Off-topic (single-metric single-outcome; not a methods paper).
- Scholar 09-11 Ritoré-Hidalgo et al. — COVID CDSL multimodal dataset
  paper. Dataset-only reference.
- Scholar 09-11 Li et al. — Osteoarthritis eligible-for-joint-replacement
  → cardiovascular disease MR. Off-topic disease pair.
- Scholar 09-11 Zarka *Pediatr Radiol* — meconium ileus history (CF
  carrier alerts feed, but historical / non-empirical).
- Scholar 09-11 Shilpa et al. — Iguratimod in autoimmune disease
  narrative review. Off-topic autoimmune drug review.
- Scholar 09-11 Zhang et al. — Empagliflozin PCOS drug repurposing (as
  above).
- Scholar 09-09 Kalebasty et al. — darolutamide + ADT + docetaxel
  metastatic prostate cancer combination therapy. Off-topic.
- Scholar 09-11 Ho et al. — Language Models Can Control Their Own
  Attention (multiple author feeds hit it as an off-topic ML paper).
- Scholar 09-11 various NLP / LLM-methodology-only citations from author
  feeds — off-scope.

---

## Notes on the arxiv-digest pipeline

- Ten cron runs; four "138-byte empty" days (09-03, 09-05, 09-06, 09-08)
  are the normal weekend-adjacent gaps for `q-bio.QM / q-bio.GN /
  q-bio.PE / stat.AP`, not pipeline failures. All other days produced
  either a short header or a small paper set.
- No pipeline errors visible in the last ten cron runs (no
  429-rate-limit warnings or missing-category caveats surfaced in the
  digest files themselves).
- Recommend adding `metabolomic age`, `brain age`, `training data
  attribution`, and `influence function` as low-weight keywords —
  Snel & Schulz (HIGH #14) surfaced only via `uk biobank` + `biobank`,
  and would have scored higher (and therefore been eligible for the
  deep-summary snippet block) with a keyword hit on
  `metabolomic age` or `training data attribution`.
- Consider adding `target trial emulation` and `emulated target trial`
  to the tracked-keyword list — Ju et al. (HIGH #3) landed only via a
  Scholar author/keyword feed, not via the local arxiv-digest, and it
  would be exactly the kind of paper the local digest should surface.
