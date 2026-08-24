# Research digest report — 2026-08-24

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS-LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-24 12:00Z** (~7 days since the
last research-digest report, covering seven scheduled arxiv-digest cron
runs — six commits landed, one date missing — and five Google Scholar
alert batches on 08-17, 08-18, 08-19, 08-20, and 08-22–08-23).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-18.md` → `2026-08-24.md`) | 08-18 → 08-24 daily crons | 6 daily runs landed. 08-18: 4 papers (Bayesian epidemic alignment g-computation; Bayesian causal mediation for zero-inflated longitudinal; N-of-1 primer for digital health; regression-not-to-mean overdose DIH). 08-20: 3 papers (Monroe molecular FM; Peru municipal DML; urban rail transit DML). 08-21, 08-22, 08-23, 08-24: 0 papers (with 3, 1, 0, 0 previously-surfaced suppressions respectively — the pipeline is deduplicating correctly against `seen.json`). **08-19: NO digest file exists** — the bot commit stream skips from `Daily digest 2026-08-18` to `Daily digest 2026-08-20`. Confirmed via `git log`: the cron did not run (or ran and errored) on 2026-08-19. Nothing else looks anomalous about the pipeline. Worth a one-line check of the GitHub Actions run log for `2026-08-19` if you want confirmation of the failure mode. |
| No `arxiv-digest` email hits from GitHub | — | Search of `from:notifications@github.com` × `arxiv-digest`, `chenjiezeng`, and `arxiv` returned zero threads in the window (this repeats the finding from the 08-17 report). The `arxiv-digest` pipeline commits its output to the local repo (`arxiv-digest-bot@users.noreply.github.com`) rather than emailing PR / cron notifications. Digest files under `digests/` remain the primary artifact; the on-disk repo *is* the arxiv-digest feed. |
| Google Scholar alerts (keyword feeds, 08-17, 08-18, 08-19, 08-20, 08-21, 08-22, 08-23 batches) | 08-17 → 08-23 | 10-12 keyword feeds fire per batch: `variant interpretation` / `variant classification`, `autoimmune disorders/diseases`, `electronic health records`, `UK Biobank`, `knowledge graph`, `drug repurposing`, `rare diseases`, `All of Us research program`, `mendelian diseases`, `Foundation models + electronic health records`, `phenome wide association studies` (fired once, 08-18), `clonal hematopoiesis` (fired once, 08-21). |
| Google Scholar alerts (author + citation feeds, 08-18, 08-20, 08-23 batches) | 08-18 → 08-23 | 20+ author/citation feeds fire per batch: Chenjie Zeng (self), Lisa Bastarache (×2), Joshua C. Denny (×2), Kai Wang (×2), Konrad Karczewski (×2), Peter Szolovits (×2), Jian Yang (×2), Stephen B Montgomery (×2), George Hripcsak (×3: new-articles + new-related + citations-to), Daniel Kastner (×2), Marinka Zitnik, Zhiyong Lu (×2), Tiffany J Callahan, Vivek Natarajan (citations-to), Yuan Luo (citations-to), Miguel Hernán (citations-to), Neil M Davies (new articles), Patrick Ryan (new-related), Pascal Brandt (new-related), Jonathan K Pritchard (citations-to), Bing Ren (new-articles), Xingyi Guo (new-articles), Fei Wang (new-articles), Nigam Shah (new-articles), Leo Anthony Celi (new-articles), Russ B Altman (new-articles), Wendy Chung (new-articles), George H Chen (new-articles). |
| NCBI My-NCBI What's-New alerts | 08-17 → 08-23 | Daily fires for `UK Biobank`, `All of Us`, `drug repurposing` PubMed saved searches. Snippets contain no titles (envelopes only); trigger-open only if the corresponding Scholar-keyword feed didn't already surface the paper. |

> Caveat: Scholar emails contain title, authors, venue, and only the
> first ~2–3 lines of each abstract. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it. Author lists are truncated as they
> appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Fourteen HIGH items surfaced this window, clustering into five knots:

**Return-of-secondary-genomic-findings + population screening (2 items).**
Kullo IJ, Horowitz CR, Bastarache L, Berkman B et al. *Recommendations
for return of secondary genomic findings in observational cohort
studies* (dual feed: Lisa Bastarache new-articles + George Hripcsak
citations-to) — the eMERGE / All-of-Us / BioVU lineage authoring a
consensus framework for how observational cohorts return incidental /
secondary findings. This is a **direct-hit paper** for INTERESTS.md's
core PheWAS / penetrance-under-population-screening thread: any
recontact / return-of-results policy an ancestry-stratified PGS study
of AoU or BioVU needs a citable framework, and Kullo/Horowitz/
Bastarache is now that citation. Cheng Y, Butler-Laporte G, Nakanishi
T, Lu T. *Development of a simple clinical score to prioritize
detection of severe alpha-1 antitrypsin deficiency with PiZZ genotype*
(All of Us keyword feed, Genetics in Medicine 2026) — a **penetrance-
in-population-screening** paper for a monogenic disorder (AATD/PiZZ),
in the AoU cohort, that develops a clinical prioritization score. This
is the **exact template** for the CFTR / APOL1 penetrance work
INTERESTS.md tracks — a phecode-and-labs prioritization score
downstream of a monogenic variant call. Together with Kullo et al.
these two papers form a coherent "how to score and how to return"
pair for the population-screening thread.

**Foresight / national-scale EHR generative FM (1 item, but hit on
four feeds).** Ellershaw S, Tomlinson C, Kraljevic Z et al.
*Foresight-England: Development of a National-Scale Generative AI
Model of Electronic Health Records for Medical Event Prediction
across the COVID-19 Pandemic* (arXiv; hit by George Hripcsak
new-related, Patrick Ryan new-related, `electronic health records`
keyword, and `Foundation models + electronic health records`
keyword — quadruple feed hit). Direct hit on **EHR foundation
models** and on **Digital-twins-from-EHR** rising sub-thread
(INTERESTS.md line ~117), and interesting for the **fidelity /
portability / audit-of-representations** sub-topic under `Knowledge
representation in EHRs` (line ~168) because it's trained
at national scale. The quadruple-feed hit is the strongest signal
this window: this is the paper to read.

**Genetic-epi × biobank cluster (5 items).** Corfield EC, Shadrin AA,
Frei O, Rahman Z et al. *Family genetic designs in MoBa provide
insights into health and functioning* — Nature 2026 (dual feed:
Karczewski + Neil Davies). Nature-tier trio-design paper; slots into
the **cross-trait shared genetic architecture and multi-trait
triangulation** sub-thread and the MR-adjacent family-design
literature. Holley G, Eggertsson HP, Kristmundsdottir S, Beyter D
et al. *An Icelandic pangenome reference* — Nature 2026 (Denny
citations-to feed). Direct hit on the **pangenome-informed variant
calling and PGS-portability** rising sub-thread (INTERESTS.md
line ~90). Ao X, Kolifarhood G, Parisien M, Bortsov A, Grant AV
et al. *Exome-wide association study reveals common and rare coding
variants shaping chronic pain in 327,642 UK Biobank participants*
— Genome[Res/Med] 2026 (dual feed: Stephen B Montgomery + Jian
Yang). UKB ExWAS at n=328k for a highly-multimorbid trait; direct
hit on the **`Biobanks with EHR linkage: UKB`** and **`Genetic
epidemiology / GWAS / ExWAS`** threads. Zhou G, Yolou I, Xie Y,
Zhao H. *Protocol for leveraging local ancestry and cross-ancestry
genetic architecture to improve polygenic prediction in admixed
populations* — STAR Protocols 2026 (Denny + Jian Yang + Chenjie
Zeng self-related feeds, **triple** hit — the strongest self-feed
signal of the window). This is a portable protocol for cross-ancestry
PGS portability; the triple-feed hit signals it is *especially*
relevant to your own line of work. Suger AH, Harrison TA, Zhang J,
Wu MC, Darst BF et al. *The pleiotropic landscape of rare variant
associations with multiple cancers in large biobanks* — Human
Genetics and Genomics 2026 (Karczewski citations-to). Direct hit
on the **composite risk models stacking PRS with rare pathogenic
variants** sub-thread and on the **rare-variant / pleiotropic /
biobank ExWAS** line.

**Pharmacoepi × EHR-based drug-repurposing TTE (2 items).** Launders
N, Richards-Belle A et al. *Impact of adjunctive dihydropyridine
calcium channel blockers on mental health outcomes in people with
severe mental illness: A target trial emulation in English EHR*
(Pascal Brandt new-related feed). CCB × mental-health as an
observational-drug-repurposing TTE — direct hit on the intersection
of **pharmacoepi TTE** and **drug repurposing (EHR-signal, causal-
inference framing)** threads. Schubert KM, Ferreira-Atuesta C,
Soma A, Zelano J et al. *Safety of Antiseizure Medications During
Direct Oral Anticoagulant Therapy in Epilepsy* — JAMA Neurology
2026 (Hernán citations-to). Drug-drug-interaction pharmacoepi in
a high-stakes clinical setting; TTE-adjacent.

**Computable phenotyping + LLM-agent-in-clinical-workflow (2 items).**
Yan Z, Huang Z, Wang F, Su C. *Knowledge Graph–Guided Domain
Generalization for Computational Phenotyping: A Tutorial* — IEEE 14th
2026 (Fei Wang new-articles feed). Direct hit on the **Knowledge
representation in EHRs and applications** thread — specifically the
`Fidelity, portability, and audit of representations` sub-topic
(INTERESTS.md line ~168), because domain-generalization from a KG
scaffold is precisely the mechanism you want if you're going to
run one phecode extractor across BioVU / AoU / MIMIC / UKB.
Schächter C, Pechmann A, Kirschner J, Hasenauer J. *Large language
models as synthetic clinical experts to inform longitudinal
rare-disease modeling* — arXiv 2026 (rare diseases keyword feed).
Direct hit on the **Rare disease** thread and adjacent to the
**Auditable HPO-driven diagnostic benchmarks** rising sub-thread
(GraphRareBench lineage): LLMs standing in as synthetic experts
opens both a scaling avenue and a validity risk that maps back to
the GraphRareBench "ranking-vs-evidence" argument.

**CHIP / AoU-native pharmacoepidemiology bonus (2 items).** Meyre PB,
Ahn HJ, Ehlert CA, Dederichs TS et al. *Association of Clonal
Hematopoiesis With Silent Brain Lesions and Cognitive Decline in
Patients With Atrial Fibrillation* — Circulation 2026 (`clonal
hematopoiesis` intitle keyword feed). Direct hit on the **CHIP /
VEXAS / LOY somatic-mosaicism** disease thread — CH × CV /
neurocognitive outcomes in the AF population; complements the
Bandreddi Tobit-vs-hurdle methods paper from the 08-17 report.
Kosgolla JV, Smith DC. *[PGS × EHR-observed] remission and relapse
in substance use disorder: Longitudinal evidence from the All of
Us research program* — Addiction 2026 (All of Us keyword feed).
PGS-informed longitudinal outcomes in AoU — a **native-to-AoU
PheRS / phecode-outcome study design**, and one of the first to
land in the AoU-published-literature since the last report.

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
within source, then by bucket.

### arxiv-digest surfacings (2026-08-18 → 2026-08-24)

#### METHODS-WATCH — Moriña D. *Bayesian epidemic alignment for causal evaluation of seasonal infectious-disease interventions.* arXiv 2608.16537v1 (stat.ME, 2026-08-17). Score 1.

Bayesian causal count model where season-specific affine transforms
map calendar time to a latent **epidemic clock**; intervention effects
are estimated on the clock rather than the calendar, so uncertainty
about epidemic timing propagates into every causal contrast. Posterior
**g-computation** yields prevented cases, prevented fractions, peak
attenuation, and epidemic displacement under both a controlled and a
dynamic contrast. Applied to Catalan primary-care RSV immunisation data.
The clock-alignment idea is a portable **time-warping trick for any
seasonal-exposure TTE** — think influenza-antiviral pharmacoepi, RSV
monoclonal-antibody rollout in pediatrics, or seasonal-allergy step-up
therapy analyses in AoU / OPTUM. Bookmark alongside the **g-methods**
lineage in `INTERESTS.md` (line ~46).

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. *Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.* arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1.

Bayesian causal mediation with enriched **Dirichlet process mixture
models** and a scalable **G-computation** estimator, developed for a
setting with (i) longitudinal exposure with **non-compliance**
(email-opening in the running example), (ii) **multiple longitudinal
mediators**, and (iii) **zero-inflated** mediators + zero-inflated
outcomes. The running example is a marketing campaign, but the pattern
— non-compliant longitudinal treatment × zero-inflated mediators →
zero-inflated clinical outcomes — is precisely the shape of a
**medication-adherence pharmacoepi analysis on EHR labs data** (MPR
non-compliance → zero-inflated adherence-day counts → zero-inflated
lab-abnormality outcomes). Portable to the **CFTR-modulator adherence
→ pulmonary-exacerbation-rate** and **GLP-1 RA adherence → HbA1c-
lowering trajectory** questions on the pharmacoepi watchlist. The
zero-inflated-mediator formalism also connects to the Bandreddi
Tobit-vs-hurdle result from the 08-17 report — the two together are
the "how to model zero-inflated longitudinal clinical data" toolkit
of the summer.

#### METHODS-WATCH — Daza EJ. *A Primer on Digital Health N-of-1 Studies and Single-Case Designs.* arXiv 2608.15526v1 (stat.AP, 2026-08-16). Score 1.

Textbook-chapter primer on **N-of-1 and single-case designs** for
digital health, with a forward-looking pitch for "esametry" (statistics
of digitized-multitudes-within-a-person). Not a methods contribution
per se, but a citable reference for any **precision-medicine / digital-
twin** methods piece that wants to distinguish subgroup-refinement
personalization (traditional precision medicine) from within-person
serial-experiment personalization (Daza's framing). Slots into the
**Machine learning for precision health** thread (line ~119) and the
**Digital-twins-from-EHR** rising sub-thread (line ~117) as the
canonical "why not just personalize per-patient" reference.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. *Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.* arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1.

Extends the recent econometrics result that a constant-treatment-effect
estimator can be a weighted average with **negative weights** across
treatment durations when effects are heterogeneous across durations, to
the **logistic-regression** case. Illustrated with drug-induced-homicide
prosecutions × overdose deaths: the constant-effect estimate has a
different sign than nearly all heterogeneous-duration effects. Bookmark
for **longitudinal pharmacoepi analyses with staggered treatment
initiation** — CFTR-modulator eligibility waves, GLP-1 RA post-approval
cascades, HRT initiation cascades — where a naive constant-effect
regression can flip sign relative to the duration-stratified TTE. Direct
methods complement to the negative-weighting caveats in Callaway–Sant'Anna
DID lineage.

#### SKIP — Banaszewski B, Fitzgibbon AW. *Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference.* arXiv 2608.18982v1 (cs.LG, 2026-08-19). Score 1.

Molecular foundation model pretrained on 81M molecules with a TabPFN-based
downstream predictor. Score-1 keyword hit on `foundation model`; nothing
biomedical / EHR / clinical. Off-thread.

#### SKIP — Machacuay C, Lincovil J, Rojas H. *Mayoral Experience or Municipal Capacity? Negative-Outcome Evidence on Municipal Budget Execution in Peru.* arXiv 2608.18354v1 (stat.AP, 2026-08-18). Score 1.

Peruvian municipal-panel DML paper; the negative-outcome-control design
is pedagogically clean and portable to biomedical causal-inference
teaching, but the paper itself is off-thread.

#### SKIP — Yao Y, Zhang N, Graham DJ. *Quantifying the Causal Operational Determinants of Service Reliability in Urban Rail Transit: Evidence from Panel Double/Debiased Machine Learning.* arXiv 2608.17901v1 (stat.AP, 2026-08-18). Score 1.

Urban-rail-reliability DML paper. Off-thread.

### Scholar alerts — 08-17 → 08-23 batches

#### HIGH — Kullo IJ, Horowitz CR, Bastarache L, Berkman B, et al. *Recommendations for return of secondary genomic findings in observational cohort studies.* [Journal TBD] 2026 (Lisa Bastarache new-articles feed + George Hripcsak citations-to feed, dual hit).

Consensus-framework paper on **return of secondary genomic findings
(ROSF)** in observational cohort studies from the eMERGE / All of Us /
BioVU lineage (Kullo → Horowitz → Bastarache → Berkman is the exact
author-order signal for the eMERGE ROSF working group). Directly serves
INTERESTS.md's core question of **penetrance under population-screening
conditions** because ROSF policy is what turns a biobank scan into a
recontact / population-screening study — the paper is upstream of any
CFTR / APOL1 / HBOC penetrance-and-return-of-results design in AoU or
BioVU. Read full-text for: (1) which variant classes they recommend
returning (P/LP only, or also VUS-with-strong-family-history), (2) how
they handle re-classification over time (ClinVar 3-star updates), (3)
recontact protocols and consent-model constraints in observational
biobanks, (4) whether they specifically comment on ancestry-stratified
recontact considerations. This should become a **standing citation** in
the introduction of any penetrance-in-population-screening paper you
draft from AoU / BioVU going forward.

#### HIGH — Cheng Y, Butler-Laporte G, Nakanishi T, Lu T. *Development of a simple clinical score to prioritize detection of severe alpha-1 antitrypsin deficiency with PiZZ genotype.* Genetics in Medicine 2026 (`All of Us research program` keyword feed).

**Penetrance-in-population-screening for a monogenic variant**, exactly
the template `INTERESTS.md`'s PheWAS-infrastructure thread calls out
(line ~26). Alpha-1 antitrypsin deficiency (AATD) with PiZZ genotype is
a canonical monogenic variant with well-documented ascertainment bias
(clinically-ascertained cohorts vastly overestimate penetrance vs.
population screening). Butler-Laporte co-authorship signals the AoU-
downstream population-screening ExWAS lineage. The **simple clinical
score to prioritize detection** framing means this paper: (1) uses
phecode-and-labs-derived features from AoU EHR, (2) selects a clinically
usable subset (age, smoking, FEV1, LFTs — read full-text to confirm), (3)
validates against a WES-defined PiZZ ground truth. This is the **exact
design pattern** to copy for CFTR (F508del homozygotes), APOL1 (G1/G2
compound heterozygotes), TTR (V142I amyloidosis), and BRCA1/2 in AoU or
BioVU. Read full-text for: (i) the score's PPV / sensitivity in the
held-out AoU subset, (ii) how they define the "severe AATD" outcome
(phecodes, chart review, both), (iii) whether they compare score-driven
prioritization to broad WES-based screening on a cost-per-case-detected
axis. Highly directly relevant — this is your **template**.

#### HIGH — Ellershaw S, Tomlinson C, Kraljevic Z et al. *Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic.* arXiv 2026 (George Hripcsak new-related + Patrick Ryan new-related + `electronic health records` keyword + `Foundation models + electronic health records` keyword — QUADRUPLE FEED HIT).

**National-scale generative EHR foundation model** (England NHS-scale)
built for medical-event prediction across the COVID-19 pandemic
disruption. Quadruple-feed hit — the loudest single-paper signal in
the window. Direct hit on **EHR foundation models** (line ~112),
**Digital-twins-from-EHR** rising sub-thread (line ~117), and the
`Interoperability standards and their representational consequences`
sub-topic under `Knowledge representation in EHRs` (line ~163). Read
for: (1) which national data source (NHS Digital vs. OpenSAFELY vs.
CPRD Aurum) and how much of England is covered, (2) how they handle
the **COVID-19 distribution shift** (masked pretraining pre-shift,
finetuning post-shift, or joint), (3) the tokenization / event-schema
choice (MEDS / FEMR / OMOP-CDM native / custom), (4) evaluation
tasks — is medical-event prediction canonical next-event-in-timeline
(CLMBR-style), phecode-onset prediction, or clinical-outcome
regression, (5) whether they publish weights or only inference API,
(6) how the model performs *across* NHS trusts (portability audit
against site shift, `Fidelity, portability, and audit of
representations` sub-topic). This paper deserves a full-text read;
it's the current best candidate to sit alongside the Zhang / Ideker
/ Oermann *Cell* 2026 digital-twins framing reference as the
implementation reference.

#### HIGH — Zhou G, Yolou I, Xie Y, Zhao H. *Protocol for leveraging local ancestry and cross-ancestry genetic architecture to improve polygenic prediction in admixed populations.* STAR Protocols 2026 (Joshua C. Denny new-related + Jian Yang new-related + Chenjie Zeng new-related feeds, TRIPLE hit — the strongest self-feed signal of the window).

**Portable protocol paper for local-ancestry-informed cross-ancestry
PGS** in admixed populations. Triple feed hit (Denny + Jian Yang + Zeng
self-related) is a strong signal this is *especially* relevant to your
own line of work. Directly serves the **`cross / trans-ancestry
portability`** sub-thread of Genetic epidemiology (INTERESTS.md line
~63) and the multi-ancestry framing of the PheRS thread (line ~24).
Read full-text for: (1) the exact reference LA-inference tools they
recommend (RFMix vs. FLARE vs. GNOMIX), (2) which cross-ancestry PGS
methods they benchmark (PRS-CSx, XPASS, BridgePRS, PROSPER), (3)
their validation cohort (AoU is the obvious substrate given the
Denny + Zeng co-authorship signal; UKB African/S. Asian is the
alternative), (4) how they handle **admixture-strat calibration** at
the tails (whether the protocol changes the tail-risk quantile
allocation vs. naive PRS). A STAR Protocols paper is by design a
runnable pipeline — worth cloning the accompanying code repo and
seeing if it drops onto AoU AllxAll straightforwardly.

#### HIGH — Corfield EC, Shadrin AA, Frei O, Rahman Z et al. *Family genetic designs in MoBa provide insights into health and functioning.* Nature 2026 (Konrad Karczewski new-related + Neil M Davies new-articles, dual hit).

Nature-tier **family-genetic-design** paper in the MoBa cohort. Dual
feed hit (Karczewski + Neil Davies) is a strong methods-signal:
Karczewski for the gnomAD/rare-variant lineage authorship weight,
Davies for the MR / within-family instrument-selection lineage. Family
designs (trio, sib-pair) are the **field-standard control for
dynastic effects** in polygenic prediction, and this paper is likely
to become the current-best reference on how much of a common GWAS
signal is "confounded by parents" vs. transmitted causal genotype.
Direct hit on the **PGS / cross-ancestry portability** sub-thread
(dynastic effects are a portability confounder) and on the
**PGS × exposure / environment interactions** framing (dynastic
= environmental transmission from parental genotype). Read for:
(1) the specific traits where dynastic effects were largest (likely
educational-attainment-adjacent), (2) the numerical shrinkage of
"unadjusted PGS effect" vs. "within-family PGS effect" for
cardiometabolic outcomes, (3) whether they compare within-family
effects to their AoU / UKB / MVP equivalents (portability across
biobank vs. birth-cohort designs).

#### HIGH — Holley G, Eggertsson HP, Kristmundsdottir S, Beyter D et al. *An Icelandic pangenome reference.* Nature 2026 (Joshua C. Denny citations-to feed).

**Icelandic pangenome reference** paper (deCODE authorship signature).
Direct hit on the **pangenome-informed variant calling and its
downstream PGS-portability consequences** rising sub-thread
(INTERESTS.md line ~90; HPRC v2 lineage). Read for: (1) how much
reference-bias reduction is achieved for European-ancestry variant
calls (Iceland is deep-EUR — the counterfactual is that pangenome
gains for EUR are small vs. AFR / EAS ancestries), (2) whether they
publish a re-called cohort (this becomes the substrate for downstream
PGS-portability re-benchmarks), (3) the CHM13-vs-GRCh38-vs-pangenome
comparison for medically-actionable variants. Companion citation:
the Denny citations-to feed also hit at the same batch, meaning this
paper cites Denny's PheWAS lineage — worth chasing which paper it
cites and why (probably an example of an Icelandic-cohort PheWAS
downstream of the pangenome recall).

#### HIGH — Ao X, Kolifarhood G, Parisien M, Bortsov A, Grant AV et al. *Exome-wide association study reveals common and rare coding variants shaping chronic pain in 327,642 UK Biobank participants.* Genome[Med/Res] 2026 (Stephen B Montgomery new-related + Jian Yang new-related, dual hit).

**UKB ExWAS at n=328k for chronic pain** — a highly-multimorbid trait
with a well-known EHR-phenotyping bias (chronic-pain phecodes vary
2–3× in prevalence across health systems). Dual-feed hit (Montgomery
+ Jian Yang) signals functional-genomics / stats-genetics interest.
Directly serves the **`Biobanks with EHR linkage: UKB`** thread and
the **`GWAS / rare-variant / burden-test`** methods thread. Read for:
(1) whether they use UKB's chronic-pain-questionnaire self-report or
an EHR-derived phecode as the outcome (this is the entire
identifiability of the paper), (2) the rare-coding-variant burden
signal — are there any Mendelian-pain-syndrome genes (SCN9A, SCN10A,
SCN11A) that survive at exome-wide significance? (3) cross-ancestry
replication in the UKB non-EUR subsets. Bookmark as a comparator for
any AoU-native ExWAS you plan.

#### HIGH — Suger AH, Harrison TA, Zhang J, Wu MC, Darst BF et al. *The pleiotropic landscape of rare variant associations with multiple cancers in large biobanks.* Human Genetics and Genomics 2026 (Konrad Karczewski citations-to feed).

**Rare-variant × multi-cancer pleiotropy scan in biobanks.** Direct
hit on the **`composite risk models stacking PRS with rare pathogenic
variants`** sub-thread (INTERESTS.md line ~74) and the **`Cross-trait
shared genetic architecture and multi-trait triangulation`** sub-thread
(line ~94). Multi-cancer pleiotropy of rare-variant burden is the
line of work that maps HBOC-lineage burden signals onto non-canonical
cancers — a direct extension of the CHEK2 / ATM / BRCA cross-cancer
patterns your prostate-cancer / breast-cancer background will
recognize immediately. Read for: (1) which cancers are jointly
analyzed (breast + prostate + colorectal is the eMERGE-standard
minimum), (2) the burden-test choice (SKAT-O vs. STAAR vs. Firth-
adjusted logistic), (3) whether the pleiotropy signal is driven by
a handful of hub genes (TP53, ATM, CHEK2) or is more distributed.
Companion citation to the Chenjie Zeng / hereditary-cancer lineage.

#### HIGH — Yan Z, Huang Z, Wang F, Su C. *Knowledge Graph–Guided Domain Generalization for Computational Phenotyping: A Tutorial.* IEEE 14th [Conf-name-truncated-in-snippet] 2026 (Fei Wang new-articles feed).

**Tutorial on KG-guided domain generalization for computational
phenotyping.** Direct hit on the **`Knowledge representation in EHRs
and applications`** thread — specifically the `Fidelity, portability,
and audit of representations` sub-topic (line ~168), because
domain-generalization-from-a-KG is the mechanism you want if one
phecode extractor is going to run consistently across BioVU / AoU /
MIMIC / UKB. Fei Wang is a recognized voice on computational
phenotyping + KG at Weill Cornell. Read for: (1) the specific KG
scaffolds they benchmark (UMLS vs. SNOMED-CT vs. HPO vs. OMOP-CDM
concept graph), (2) which domain-generalization method they pair
it with (invariant risk minimization, group-DRO, correlation
alignment), (3) whether the tutorial ships with an implementation
that drops onto MIMIC-IV or eICU-CRD. If it does, it's a natural
addition to the KG-representation section of any future EHR-FM
methods essay you write.

#### HIGH — Kosgolla JV, Smith DC. *[Longitudinal PGS × EHR-observed] remission and relapse in substance use disorder: Longitudinal evidence from the All of Us research program.* Addiction 2026 (`All of Us research program` keyword feed).

**Native-to-AoU PGS × EHR longitudinal outcomes study for substance
use disorder.** Direct hit on the **PheWAS / PheRS methodology
applied to biobank cohorts** thread. PGS + EHR-observed remission /
relapse in SUD is a rare longitudinal use of AoU (most AoU studies
are cross-sectional). Read for: (1) how they defined remission
(clean-tox-screen-window vs. absence-of-SUD-phecodes vs. medication-
discontinuation), (2) which PGS they used (opioid-use disorder,
alcohol-use disorder, cannabis-use disorder — each has a recent
distinct GWAS), (3) ancestry-stratified results (SUD PGS is
notoriously ancestry-non-portable), (4) whether AoU's Fitbit /
wearable / SDoH modules are used as time-varying confounders. This
paper is a **design-pattern reference** for any AoU-native
PheRS-longitudinal-outcomes study.

#### HIGH — Meyre PB, Ahn HJ, Ehlert CA, Dederichs TS et al. *Association of Clonal Hematopoiesis With Silent Brain Lesions and Cognitive Decline in Patients With Atrial Fibrillation.* Circulation 2026 (`clonal hematopoiesis` intitle keyword feed).

**CH × AF × silent brain lesions × cognitive decline** in a clinical
cardiology setting. Direct hit on the **CHIP / VEXAS / LOY somatic-
mosaicism** disease thread (INTERESTS.md line ~103). Bandreddi
(08-17 report) is the current-best modeling paper for zero-inflated
longitudinal VAF; Meyre et al. is now the current-best clinical
demonstration of a CH × non-hematologic outcome. Read for: (1)
which CH driver genes carry the neurocognitive signal (DNMT3A vs.
TET2 vs. ASXL1 vs. JAK2 — DNMT3A has the largest cognitive-signal
prior across UKB / MVP), (2) the CH detection assay (targeted panel
vs. WGS-derived) and its VAF threshold, (3) whether they adjust for
CHIP-related medication use (aspirin, DOAC, statin), (4) mediation
by silent-brain-lesion burden vs. direct effect. Bookmark for the
CHIP-in-AoU-WGS analysis on the watchlist.

#### HIGH — Launders N, Richards-Belle A et al. *Impact of adjunctive dihydropyridine calcium channel blockers on mental health outcomes in people with severe mental illness: A target trial emulation in English EHR.* [Journal TBD] 2026 (Pascal Brandt new-related feed).

**Drug-repurposing TTE on CCBs × mental health outcomes** in English
EHR. Direct hit on the intersection of **pharmacoepi TTE** (line ~46)
and **drug repurposing** (**Causal-inference framings of off-label
use** sub-thread, line ~140) threads. CCBs as neuroprotective /
mood-stabilizing agents have a long-standing pharmacology hypothesis
and a real observational signal in claims data; the TTE framing lifts
this from "association study" to "candidate repurposing indication".
Read for: (1) which CCB indication was the eligibility criterion
(hypertension vs. angina), (2) the mental-health outcome definition
(phecode-derived vs. SMI-specific composite), (3) time-zero handling
(new-user active-comparator against another antihypertensive, vs.
untreated), (4) which sensitivity analyses (E-value or Rosenbaum
bounds — the Porotsky Inverse-Confounding-Analysis method from the
08-17 report would give a more informative landscape).

#### HIGH — Schächter C, Pechmann A, Kirschner J, Hasenauer J. *Large language models as synthetic clinical experts to inform longitudinal rare-disease modeling.* arXiv 2026 (`rare diseases` keyword feed).

**LLMs as synthetic clinical experts to inform longitudinal
rare-disease modeling.** Direct hit on the **Rare disease** thread
and adjacent to the **Auditable HPO-driven diagnostic benchmarks**
rising sub-thread (INTERESTS.md line ~189 — GraphRareBench lineage).
LLMs standing in as synthetic experts is both an appealing scaling
avenue (rare-disease centers have very few real experts per disease)
and a validity risk (LLMs hallucinate rare-disease phenotypes at
elevated rate). Read for: (1) which rare disease (Pechmann is a SMA
clinician — likely SMA), (2) whether the LLM outputs are used as
priors, as pseudo-labels, or as synthetic-cohort augmentation, (3)
what ground-truth expert consensus they compare against (expert-panel
Delphi is the gold standard), (4) whether they audit for HPO-term
consistency vs. free-text drift. Pairs with the Uria-Regojo et al.
data-driven-reanalysis paper (08-17 report) as the two current-best
rare-disease-computational papers on the watch.

#### HIGH — Schubert KM, Ferreira-Atuesta C, Soma A, Zelano J et al. *Safety of Antiseizure Medications During Direct Oral Anticoagulant Therapy in Epilepsy.* JAMA Neurology 2026 (Miguel Hernán citations-to feed).

**Drug-drug-interaction pharmacoepi** in a high-stakes clinical
setting. Hernán citations-to means this paper likely cites Hernán's
TTE canon; the DDI framing (antiseizure meds × DOACs) makes it a
**target-trial-emulation-of-a-pharmacovigilance-question** — one of
the paradigms your active pharmacoepi thread lists. Read for: (1)
the specific antiseizure-meds studied (enzyme-inducing carbamazepine
/ phenytoin vs. non-inducing levetiracetam / lacosamide is the
central pharmacology contrast), (2) the outcome (stroke / bleeding /
composite MACE), (3) TTE mechanics (new-user active-comparator vs.
prevalent-user cohort). Direct comparator for any future AoU-native
DDI pharmacoepi analysis.

#### METHODS-WATCH — Wang D, Kossinna P, Ardila K, Kumarapeli S et al. *IBAS: Interaction-bridged association studies discovering novel genes underlying complex traits.* PLOS Computational Biology 2026 (Joshua C. Denny new-related feed).

**Interaction-bridged association-study method** for discovering genes
under complex traits, from the Denny-adjacent lineage. Slots into the
**GxE and PGS × exposure / environment interactions** rising sub-
thread (line ~85; Nagpal & Gibson lineage). Read for: (1) whether the
"bridge" is a molecular-QTL, an environmental exposure, or a network-
based interaction, (2) benchmarks vs. GxEMM / MTAG / iSAFE, (3) which
traits they validated on. If it turns out to be a QTL-bridged method,
compare against the Ciardulli et al. functional-propensity-score
lineage from the 08-08 report.

#### METHODS-WATCH — Pham K, Madakkatel I, Mulugeta A, Lumsden A, Hill C et al. *Data-Driven Discovery of Candidate Predictors of Future Rheumatoid Arthritis Diagnosis in the UK Biobank.* Seminars in Arthritis and Rheumatism 2026 (`UK Biobank` keyword feed).

**Data-driven prediction of incident RA in UKB.** Slots into the
**Chronic disease clustering and multimorbidity** thread (line ~127)
and the autoimmune-disease sub-thread. Read for: (1) which
data-driven method they use (LASSO / gradient-boosting / SHAP-based
feature selection), (2) whether the discovered predictors are novel
vs. rediscovering canonical RA-anticipator markers (anti-CCP,
inflammation, family history), (3) how far in advance the predictors
carry signal (5-year-anticipatory is the clinically-actionable
threshold), (4) calibration / decision-curve analysis. Compare with
the CG Walsh treatment-resistant-depression transportability paper
from the 08-23 batch (both are "predict incidence from EHR /
biobank data" designs).

#### METHODS-WATCH — Nigam A, Onongaya C, Meshram P, Frebault J et al. *Traditional Risk Factors Are Not Associated with the Rise of Early-Onset Colorectal Cancer: An All of Us Study.* Diseases of the Colon & Rectum 2026 (`All of Us research program` keyword feed).

**Native-to-AoU early-onset colorectal-cancer risk-factor scan.**
Adjacent to the AoU-native design pattern of the Kosgolla SUD paper
above; the null finding on traditional risk factors is scientifically
interesting for the EOCRC etiology field but off your immediate
methods threads. Bookmark if the CRC / MSI-adjacent thread reactivates
(hereditary CRC / Lynch syndrome overlaps with the ACMG / ClinGen
thread).

#### METHODS-WATCH — Yee J, Oakes EG, Santacroce L, Feldman CH et al. *Electronic Cigarette Use and Risk of Incident Rheumatoid Arthritis and Systemic Lupus Erythematosus in the All of Us Research Program.* Seminars in Arthritis and Rheumatism 2026 (`All of Us research program` keyword feed).

**AoU-native e-cigarette × RA/SLE observational-epidemiology study.**
Standard-format exposure–outcome cohort analysis, but AoU-native and
autoimmune-thread-adjacent. Read for the exposure-ascertainment
approach (AoU survey vs. EHR-encoded tobacco use) — the
survey-vs-EHR discordance in AoU tobacco data is a known limitation
that has methodological implications for any AoU-native exposure
analysis.

#### METHODS-WATCH — Ellershaw S — see the Foresight-England HIGH entry above (four-way feed hit).

Not duplicated; see the HIGH entry.

#### METHODS-WATCH — Halper-Stromberg E, Narayan S, Laufer V, Limson M et al. *Clinical Variant Interpretation with the Integrative Genomics Viewer (IGV) for Molecular Pathologists.* Journal of Visualized Experiments 2026 (`variant interpretation` / `variant classification` keyword feed).

**IGV-based clinical variant-interpretation walk-through** for
molecular pathologists. Slots into the **ACMG / ClinGen** thread
as a practical-tooling reference (useful when writing didactic /
training content). Not methods-original but a citable
walk-through of an IGV-in-the-loop workflow.

#### METHODS-WATCH — Le NN, Padmanabhan S. *Cardiometabolic pathways linking genetically proxied educational attainment to cardiovascular disease: a Mendelian randomisation, mediation and colocalisation study.* medRxiv 2026 (Lisa Bastarache new-related feed).

**MR + mediation + colocalization** for educational-attainment →
cardiometabolic-pathways → CVD. Adjacent to the **drug-target MR**
sub-thread (line ~64) in that it uses the MR-mediation triangle,
but the exposure (educational attainment as a genetic instrument)
is closer to the dynastic-effects / MoBa paper above than to
canonical drug-target MR. Read only if extending into the
social-genomics / dynastic-effects thread.

#### METHODS-WATCH — Termorshuizen JD, Davies HL, Lee SH, Dennis JK et al. *Genomic meta-analyses of binge-eating behavior and anorexia nervosa yield insights into the unique and shared biology of eating disorder phenotypes.* [Journal TBD] 2026 (Jian Yang citations-to feed).

**Cross-trait GWAS meta-analysis** for eating-disorder phenotypes.
Slots into the **cross-trait shared genetic architecture** sub-thread
(line ~94; Kopal et al. lineage). Read if the psychiatric / behavioral-
phenotypes thread reactivates; otherwise low-signal for the current
active methods work.

#### METHODS-WATCH — Yamamoto R, Tohyama T, Han A, Pedersen N et al. *Impact of an ROX index-guided intubation strategy on mortality in patients receiving high-flow nasal cannula: a target trial emulation.* Journal of [Critical Care?] 2026 (Leo Anthony Celi new-articles feed).

**Critical-care TTE on ROX-index-guided intubation.** Off primary
methods thread but a good pharmacoepi-TTE-adjacent design comparator
(ICU decision rules as time-varying interventions is a specific class
of TTE with immortal-time and lead-time subtleties). Read for
methodological transferability, not for the clinical result.

#### METHODS-WATCH — Allery F, Pineda-[Truncated] et al. *Mitigating health inequities with machine learning: a nationwide cohort study developing and evaluating ethnicity-specific cardiovascular risk prediction models across [English NHS].* [Journal TBD] 2026 (Gary S. Collins new-articles feed).

**Ethnicity-specific CV-risk-prediction models at national NHS scale.**
Slots into the **`Fidelity, portability, and audit of representations`**
sub-topic under KR-in-EHRs and the **Machine learning for precision
health** thread. Read for calibration-across-ethnicity results, which
are the direct comparator for any AoU-native ancestry-stratified
prediction work. Companion to the Walsh treatment-resistant-depression
transportability paper.

#### METHODS-WATCH — Farajidizaji M, Raina V. *Task Competence Is Not Instruction Following: Evaluating Instruction-Conflicting Behavior in Small Language Models.* arXiv 2607.19608 2026 (Peter Szolovits new-related feed).

**LLM behavioral eval** for small language models — task-competence
vs. instruction-following. Adjacent to the **clinical-LLM-agent**
sub-thread (evaluating whether a clinical LLM will follow a system
prompt over its trained priors is a safety-relevant question), but
the paper itself is generic LLM eval, not clinical. Bookmark for
the clinical-agent-safety framing.

#### METHODS-WATCH — Ito H, Seki T, Takiguchi T, Akagi Y, Kubota K, Miyake K et al. *Cost-effectiveness analysis of early antihypertensive treatment for hypertension detected at health screening.* Hypertension Research 2026 (Yu Akagi feed).

**Health-screening cost-effectiveness analysis** for early
antihypertensive treatment. Slots into the population-screening-and-
decision thread; adjacent to the AATD PiZZ Cheng et al. paper above
in that both are "how do we act on a screening result." Read only
if extending into cost-effectiveness / decision-analytic modeling.

#### MEDIUM — Piera-Jiménez J, Cano I, Carot-Sans G, Cresswell K et al. *Recommendations for a national electronic health record in Spain: a Delphi study.* The Lancet Digital Health 2026 (`Foundation models + electronic health records` keyword feed).

**Delphi consensus on a national EHR for Spain.** Adjacent to the
`Interoperability standards and their representational consequences`
sub-topic. Read only if the interoperability-standards / HL7-FHIR
policy thread reactivates.

#### MEDIUM — Nyberg F, Lundmark P, Blomberg A, Dekkers K et al. *Genome-wide association study of image-based emphysema scoring in the Swedish CArdioPulmonary bioImage Study (SCAPIS) suggests two new risk loci.* [Journal TBD] 2026 (Joshua C. Denny new-related feed).

**Image-derived emphysema-score GWAS** in SCAPIS. Adjacent to the
UKB CMR / DXA imaging-derived-phenotype GWAS lineage but for a
smaller cohort. Read for the imaging-phenotype-GWAS methods contrast
against the CAN-FLOW paper from the 08-17 report; otherwise low-signal.

#### MEDIUM — Cheng Z, Bai R, Diao Y. *Integrative Transcriptomics and Mendelian Randomization Identify RGS1 as a Causal Immune Regulator in Alzheimer's Disease.* Current Issues in Molecular Biology 2026 (`mendelian diseases` keyword feed, appears in 08-17 batch).

Standard MR-plus-transcriptomics AD-target-discovery template.
Already flagged in the 08-17 report (LOW-tier there); repeated in
the 08-17 keyword batch of this window; unchanged.

#### MEDIUM — Wang F, Al-Lawati A, Bektas I et al. *Unified Multi-Dimensional Benchmark for Complex Graph Reasoning in Large Language Models.* arXiv 2026 (Marinka Zitnik new-related feed).

Generic LLM-graph-reasoning benchmark. Same-title paper appeared in
the 08-17 batch (LOW there); repeated. Off clinical-agent thread.

#### MEDIUM — Gonzalez-Barbuzano S, Suarez-Pajes E et al. *Genomic and integrative based progression biomarker discovery in adult sepsis: toward clinical stratification and precision medicine.* Annals of Intensive Care 2026 (dual: 1 new citation to articles by Lisa Bastarache + 10 new citations to articles by Jian Yang).

Sepsis-biomarker integrative-genomics paper. Adjacent to critical-care
precision-medicine but off primary methods thread. Read only if the
sepsis / critical-care sub-thread reactivates.

#### MEDIUM — Meng Y, Shen M, Guo SY et al. *Whole-exome sequencing reveals the genetic landscape and polygenic susceptibility in 1241 patients with clinically suspected hemophagocytic lymphohistiocytosis.* [Journal TBD] 2026 (repeated from 08-16 batch; Bastarache new-related).

Already flagged MEDIUM in the 08-17 report; unchanged.

#### MEDIUM — Chen Y, Huang X, Ou J, Qi F, Jiang P, Zhang T, Cai S. *Identifying Antidiabetic Drugs for Lung Cancer Treatment Through Genetic Epidemiology, Multiomics Integration, and Functional Validation.* [Journal TBD] 2026 (`phenome wide association studies` keyword feed, 08-18 batch — the *phenome wide association studies* keyword fired for one paper this window).

**Drug-repurposing scan** for antidiabetic drugs × lung cancer, via
genetic epi + multiomics. Adjacent to the drug-repurposing thread but
methodology is standard MR-plus-omics. Bookmark for the diabetes-drug
× cancer sub-line if the metformin × AAA (Saxby) lineage reactivates.

#### MEDIUM — Tao C, Li W, Jiang Y, Fan S, Zhou X, Xu H, Liu J et al. *SRSF2 mutations contribute to bone marrow immune microenvironment alterations.* Cell Death & Disease 2026 (6 new citations to articles by Daniel Kastner feed).

**SRSF2 (splicing-factor) mutations × bone-marrow immune
microenvironment.** SRSF2 is a canonical CH driver gene and a
myelodysplasia driver; the paper is at the mechanism side of the
CHIP / clonal-hematopoiesis thread. Adjacent to Meyre et al. above
but at the molecular-mechanism level rather than the
clinical-outcome level. Read if extending into CH-driver-gene-
specific mechanism work; otherwise low-signal.

#### LOW — Pribus SJ, Altman RB, Nayar G. *Interpreting Protein Language Models: high attention sites predict functional regions.* bioRxiv 2026 (Russ B Altman new-articles feed).

Protein-LM interpretability paper. Off clinical thread.

#### LOW — Pagan V, Rankin SA, Edwards NA, Thorner K, Xie S et al. *SMAD6 is required for normal foregut development in humans and frogs.* Development 2026 (Wendy Chung new-articles feed).

Developmental-genetics paper. Off clinical / EHR thread.

#### LOW — Shen X, Huang CYH, Elmer J, Chen GH. *Learning Under Treatment-Induced Label Indeterminacy with Expert Annotations of Counterfactual Outcomes: A Case Study in Neurological Prognostication.* arXiv 2026 (George H. Chen new-articles feed).

Counterfactual-label ML for neuroprognostication. Adjacent to causal-
ML but off your active applied-pharmacoepi threads.

#### LOW — Bann D, Wang M, Davies NM, Wright L, O'Connor et al. *Science or Advocacy? The Global Rise of Policy Claims and Calls to Action in Population Health Research (1990-2024).* American Journal of [Epidemiology?] 2026 (Neil M Davies new-articles feed).

Meta-scientific review of policy-claims prevalence in pop-health
papers. Not methods; off-thread.

#### LOW — [Multiple LLM-benchmark / small-LM / diffusion-LM / non-biomedical KG papers surfacing in the Zhiyong Lu, Marinka Zitnik, Tiffany J Callahan, Zhiyong Lu new-related feeds]

Generic LLM benchmark / architecture papers, non-biomedical.
Off-thread.

#### LOW — Saka N, Vijaya KS, Mohan CC, Kadiyam N, RB [+]. *Conceptual comorbidity networks in autoimmune thyroid disease: A PRISMA-guided review of clinical patterns, immunological links, and emerging disease clusters.* [Journal TBD] 2026 (autoimmune keyword feed).

PRISMA review of autoimmune thyroid comorbidity. Off primary methods.

#### LOW — Kim JM, Cho J, Song J, Jung M, Lee S, Kim SY, Lee JS et al. *Seeing the Unseen: Photography for Deep phenotyping in Undiagnosed Rare Diseases.* Rare 2026 (rare diseases keyword feed).

Rare-disease photography deep-phenotyping. Adjacent to the rare-
disease thread but a specialized modality; off current methods focus.

#### LOW — Douglas CMW, Kleinhout-Vliek T, Hagendijk R et al. *Social pharmaceutical innovation (SPIN): A sensitizing concept for challenges in rare diseases.* Journal of Pharmaceutical Science and Practice 2026 (rare diseases keyword feed, 08-17 batch).

Repeat from the 08-17 report (LOW). Unchanged.

#### LOW — Selviyanti E, Subriadi AP, Haryanti T. *Integrating Technology, Human, and Knowledge Dimensions in EHR Implementation: A Systematic Literature Review of Socio-Technical [Framing].* 2026 (Foundation-models-plus-EHR keyword feed, 08-17 batch).

Repeat from the 08-17 report (LOW). Unchanged.

#### LOW — Marquez G, Crowhurst K, Sinemus H, Karakis N et al. *All of Us Consortium Training Summary Report.* 2026 (All of Us keyword feed, 08-17 batch).

Repeat from the 08-17 report (LOW). Program-training report.

#### LOW — de Andrés-Galiana EJ, Fernandez-Martinez JL [+]. *Identifying candidate therapeutic targets in amyotrophic lateral sclerosis through a transcriptome-wide machine-learning consensus approach for drug repurposing.* [Journal TBD] 2026 (drug repurposing keyword feed, 08-17 batch).

Repeat from the 08-17 report (METHODS-WATCH there). Unchanged.

---

## What's NOT in the report

- **GitHub `arxiv-digest` cron / PR notifications** — none surfaced in
  Gmail search; the local repo commits and the on-disk `digests/`
  directory serve as the digest artifact. Consistent with the 08-17
  report.
- **Missing `digests/2026-08-19.md`** — the arxiv-digest-bot commit
  stream skips 08-19 (commits: 08-18, then 08-20). This is a **pipeline
  gap flag**, not a data-signal absence. Recommend one manual check of
  the GitHub Actions run log for 2026-08-19 to confirm the failure mode.
- **NCBI My-NCBI What's-New batches** (AoU / UKB / drug repurposing) —
  present in the inbox but envelopes only (no titles in snippets).
  Where the corresponding Scholar-keyword feed surfaced the same paper,
  it appears above; the NCBI-only batches added no unique surfacings.
- **bioRxiv / medRxiv Subject Collection Alerts** — none surfaced;
  Scholar author feeds (Le NN medRxiv MR-mediation; SN Payrovnaziri
  npj Digital Medicine neonatal labs) carried what preprint content
  there was.
- **arxiv.org daily category mailings** (`no-reply@arxiv.org`) — the
  raw upstream feed that supplies the `arxiv-digest` pipeline; papers
  surfaced via the digest are covered in the arxiv-digest section
  above.

## Next steps to consider

1. **Investigate the missing `digests/2026-08-19.md`.** One-line
   check: pull up the GitHub Actions run log for 2026-08-19 to see
   whether the cron failed, was skipped, or ran successfully but
   deduplicated to zero (in which case the pipeline should have
   emitted a "0 relevant papers" file anyway). If a genuine cron
   miss, consider a defensive `on: schedule` retry step.
2. **Read Ellershaw et al. Foresight-England full text.** Loudest
   single-paper signal of the window (quadruple-feed hit). Anchor
   paper for the EHR-FM + digital-twins-from-EHR + national-scale-
   representation triangle. Deserves a top-of-queue read alongside
   the Zhang / Ideker / Oermann *Cell* 2026 digital-twins framing
   reference.
3. **Read Kullo, Horowitz, Bastarache, Berkman et al. ROSF-in-
   observational-cohorts full text.** Should become a **standing
   citation** for any penetrance-in-population-screening paper you
   draft from AoU / BioVU going forward. Slots directly into the
   introduction of the CFTR / APOL1 penetrance write-ups on the
   watchlist.
4. **Read Cheng et al. AATD PiZZ prioritization score** as the
   design template for a CFTR / APOL1 penetrance-in-AoU paper. The
   "simple clinical score to prioritize detection" framing is a
   directly-clonable design pattern.
5. **Clone Zhou et al. STAR Protocols cross-ancestry PGS pipeline**
   and see if it drops onto AoU AllxAll. Triple-feed hit (Denny +
   Jian Yang + Zeng self-related) suggests it's especially
   directly-relevant to your active work.
6. **Bookmark Yan et al. KG-guided domain generalization tutorial**
   for the KG-representation section of any EHR-FM methods essay.
   If it ships with an implementation that drops onto MIMIC-IV,
   run a small ablation of "with KG scaffold vs. without" on your
   preferred benchmark cohort.
7. **Compare Launders et al. CCB × mental-health TTE** to the AoU
   pharmacoepi CCB use-case; the TTE mechanics (new-user active-
   comparator against another antihypertensive) are directly
   transferable to any AoU-native repurposing TTE.
8. **Adopt Kung et al. regression-not-to-mean caveat** as a required
   sensitivity note for any longitudinal-pharmacoepi analysis with
   staggered treatment initiation on the watchlist (CFTR-modulator
   eligibility waves, GLP-1 RA post-approval cascades, HRT initiation
   cascades) — a naive constant-effect regression can flip sign
   relative to the duration-stratified TTE.
9. **Add Meyre et al. CH × AF × cognitive decline (Circulation)** to
   the CHIP-clinical-outcomes reading list alongside Bandreddi et al.
   Tobit-vs-hurdle (08-17 report). Meyre gives the clinical-outcome
   signal; Bandreddi gives the modeling choice.
10. **Extend the Corfield MoBa family-design result to the AoU / UKB
    cross-ancestry PGS work** — Nature-tier family-design shrinkage
    of PGS effects is directly informative for whether an AoU
    ancestry-stratified PGS reflects "true genetic transmission" vs.
    "shared parental environment," a distinction that matters for
    the CFTR-modulator / APOL1 / hereditary-cancer penetrance
    designs on the watchlist.

_Report generated 2026-08-24 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo. No emails were
modified. Next report should cover 08-24 → next scheduled run._
