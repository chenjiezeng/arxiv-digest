# Research digest report — 2026-08-28

Triage of research-related email + the local `arxiv-digest` repo against
the active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked
biobanks, EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/LOY/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity, knowledge representation in
EHRs).

Window: **2026-08-17 12:40Z → 2026-08-28 12:35Z** (~11 days since the
last research-digest report, covering ten daily arxiv-digest cron runs
and multiple Google Scholar / NCBI / bioRxiv / medRxiv alert batches).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Local `arxiv-digest` repo (`digests/2026-08-17.md` → `2026-08-27.md`) | 08-17 → 08-27 daily crons | 10 daily runs. 08-18: 4 papers (Bayesian epidemic alignment / RSV, causal mediation for zero-inflated longitudinal / retail, N-of-1 primer, regression-not-to-the-mean HTE). 08-20: 3 papers (Monroe MFM, Peru mayoral DML, urban rail DML — all off). 08-21, 08-22, 08-23, 08-24: 0 relevant. 08-25: 1 paper (causal inference in extremes — climate/finance). 08-26: 1 paper (RIBOSPAN long-context RNA FM). 08-27: 1 paper (frozen hematology FM audit under acquisition shift). |
| No `arxiv-digest` email hits from GitHub | — | Same as 08-17 report: the pipeline commits its output to this local repo rather than emailing PR / cron notifications. Digest files under `digests/` are the primary artifact. |
| Google Scholar alerts (keyword feeds, 08-27 batch, 11:44Z) | 08-27 11:44Z | 12+ keyword feeds fired simultaneously: `"variant interpretation" OR "variant classification" OR "Causal Variant"`, `"UK Biobank"`, `"knowledge graph"`, `"All of Us research program"`, `intitle:"clonal hematopoiesis"`, `"drug repurposing"`, `"autoimmune disorders" OR "autoimmune diseases"`, `Foundation models + "electronic health records"`, `"electronic health records"`, `"Undiagnosed Diseases Network"`, `mendelian diseases`, `rare diseases`. |
| Google Scholar alerts (author + citation feeds, 08-27 batch, 06:59Z) | 08-27 06:59Z | 15+ author / citation feeds fired: Chenjie Zeng (new-related, self-feed hit), Lisa Bastarache (citations-to), Joshua C Denny (citations-to), Jian Yang (new-related + citations-to), Konrad Karczewski (citations-to), Peter Szolovits (new-related), Marinka Zitnik (new-related), Zhiyong Lu (new-related), Tiffany J Callahan (new-related), George Hripcsak (new-articles), Stephen B Montgomery (new-related + citations-to), Yuan Luo (citations-to), Daniel Kastner (citations-to), Vivek Natarajan (citations-to), Jonathan K Pritchard (citations-to). |
| Google Scholar alerts (mid-window: 08-24 13:41Z, 08-25 23:33Z) | 08-24 → 08-25 | Interim author-feed batches: Pascal Brandt (new-related, Danish EHR-epidemiology paper), Peter Szolovits, George Hripcsak, Marinka Zitnik, Zhiyong Lu. |
| NCBI My-NCBI What's-New (08-27 12:34Z) | 08-26 05:36Z → 08-27 05:35Z | `"UK Biobank"` returned **23 items**; `"All of Us"` returned **4 items**. Highest-signal UKB items: PULSE (Wu et al. Nat Comput Sci, Digital Twins Consortium), Kayaalp et al. missense variant effects (Nat Genet), Squires et al. HRT × dementia responsive subgroups (Alzheimers Dement), Huang et al. autoimmune → MACE proteomic mediators (Proteomes), Reed et al. exceptional parental longevity (JAMA Netw Open). |
| bioRxiv Subject Collection Alert (08-28 00:01Z) | 26–27 Aug postings | Bioinformatics / Genetics / Genomics / Immunology / Pathology. Mostly protein-structure / cell-atlas / methods content; on-thread items scarce (Akey et al. "Principled Framework for Using Correlated Traits to Improve Risk Prediction" was the closest fit to PRS-with-correlated-traits work). |
| medRxiv Subject Collection Alert (08-28 00:05Z) | 27 Aug postings | Epidemiology / Genetic and Genomic Medicine / Health Informatics / Nephrology / OB-Gyn / Oncology / Pediatrics. Highest-signal: Tipping et al. new-onset T2DM × obesity-related cancer risk (UKB matched cohort); Zheng et al. polygenic + proteomic risk score divergence in neurodegenerative disease; Nadig et al. + Karczewski coding-mutation contribution to autism; Aceves-Ewing et al. UDN KMO biallelic variants → congenital NAD deficiency; Tan et al. reproductive genetic screening with perinatal treatability. |

> Caveat: Scholar / NCBI PubMed / rxiv emails contain title, authors,
> venue, and only the first ~2–3 lines of each abstract. The reports
> below contextualize that metadata against the active research threads;
> nothing here reflects full-text reading. `arxiv-digest` entries
> include the full abstract because the pipeline captures it.
> Author lists are truncated as they appear in alert snippets.

---

## Executive summary (HIGH-priority studies, ranked)

Twelve HIGH items surfaced this window, clustering into six knots:

**Digital twins from EHR — the field-defining framing paper landed
(1 item).** Wu et al. *Nature Computational Science* 2026-08-26 —
**PULSE: Longitudinal alignments and syntheses of multimodal clinical
data for personalized medicine**, authored under the *International
Consortium of Digital Twins in Healthcare and Medicine* banner (Zhang,
Loupy, Oermann, Gladyshev, and colleagues). This is the
methodology-companion to the *Cell* 2026 field-defining framing paper
you added to the `EHR foundation models → Digital twins from EHR data`
rising sub-thread (INTERESTS.md line ~120). Same consortium, same
lineage — read this together with the *Cell* paper as the "framing +
first implementation" bundle for the digital-twins-from-EHR canon.

**Variant interpretation — a Nat Genet functional-evidence integration
paper (1 item).** Kayaalp et al. *Nat Genet* 2026-08-26 — **Prediction
of human missense variant effects from functional evidence** (Casanova
group; PMID 42649388). Direct anchor for the ACMG / ClinGen thread —
functional-evidence integration is exactly the PS3 / BS3 evidence pole
that ACMG variant curation guidelines pivot on. Sits alongside the
Mitev framework paper (08-17 report) as the two anchor references for
the variant-interpretation subthread this month.

**HRT pharmacoepi with heterogeneous-effect subgroup discovery
(1 item).** Squires et al. *Alzheimer's & Dementia* 2026 —
**Hormone-replacement therapy and dementia risk among postmenopausal
women: identifying responsive subgroups in the UK Biobank** (PMID
42644405). Direct hit on both the **HRT pharmacoepi thread** (the
persistent CFTR-modulator / HRT / GLP-1 RA discontinuation watchlist in
INTERESTS.md line ~50) and the **HTE sub-thread of ML for precision
health**. Portable to CFTR modulators and GLP-1 RA "responsive
subgroup" designs; also a natural pair with the Nagpal & Gibson PGS ×
exposure lineage.

**Proteomic-mediation and multi-omics-augmented PRS cluster
(3 items).** Huang et al. *Proteomes* 2026 — **Proteomic mediators
linking autoimmune diseases to major adverse cardiovascular events
(UK Biobank)** (PMID 42647374). Zheng et al. medRxiv 2026 — **Absorption
and co-expression modules show where polygenic and proteomic risk
scores diverge in neurodegenerative diseases**. Vitali et al.
*Alzheimer's & Dementia: Translational Research & Clinical
Interventions* 2026 — **Sex- and APOE-specific transcriptomic drug
repurposing for AD** (drug-repurposing feed). Together these anchor the
**multi-omics-augmented PRS** sub-thread (INTERESTS.md line ~85) — the
Huang paper shows proteomics-as-mediator between autoimmune exposure
and CV outcome, the Zheng paper diagnoses *where* proteomic and
polygenic scores diverge (proteomic captures late-life "absorption"
that PGS cannot), and the Vitali paper does a stratified transcriptomic
repurposing that generalizes the sex × APOE × drug lens to other
PGS × context designs.

**CHIP × cardiovascular sub-cluster (3 items).** Han et al.
ResearchSquare 2026 — **Genetic βAR signaling modifies CH-associated
mortality in patients with atherosclerotic CVD** (uses ~550k UK Biobank
WES + AoU initial WGS release for CH ascertainment). Streck et al.
*JVS-Vascular Science* 2026 — **TET2-mutant CH × peripheral bypass
graft occlusion** (multicenter retrospective cohort pilot). Tang et al.
*Cell Investigation* 2026 — **CH as a context-dependent modifier of
organ-specific disease** (review synthesizing organ-specific CH
mechanism and translational boundary). All three fire the
**CHIP / VEXAS / LOY / somatic mosaicism** thread (INTERESTS.md line
~103); Han et al. is the most operationally useful because it stakes
out the exact **UKB WES + AoU WGS CHIP-ascertainment protocol** that
current AoU CHIP work needs to align with. Streck et al. is the
mechanistic vascular hit; Tang et al. is the review to cite when
framing CH-as-modifier-of-organ-specific-disease.

**Genetic epi — cross-ancestry T1D GWAS + drug-target MR (2 items).**
Guo et al. *Diabetic Medicine* 2026 — **Trans-ancestry meta-analysis of
GWAS identifies eight novel genetic loci in type 1 diabetes: a
multi-population study** (fires Chenjie Zeng self-related feed). Direct
addition to the **cross / trans-ancestry portability** sub-thread
(INTERESTS.md line ~72) and to the biobank-with-EHR-linkage thread
because T1D outcomes in AoU / MVP become newly discoverable. Lee et al.
*Biomedicines* 2026 — **Genetic assessment of oesophageal safety of
GLP-1 and GIP receptor perturbation: a drug-target Mendelian
randomisation study** — direct on the **drug-target MR** rising
sub-thread and the **GLP-1 RA pharmacoepi watchlist** at the same time
(oesophageal safety is one of the standing GLP-1 RA safety questions).

**Rare disease + PGS clinical implementation (2 items).** Aceves-Ewing
et al. medRxiv 2026 — **Biallelic variants in KMO cause a novel form of
congenital NAD deficiency** — Undiagnosed Diseases Network case-family
authorship anchor, and a direct fire on the **rare-disease → HPO →
disease-map** thread. Hanley et al. *European Journal of Human Genetics*
2026 (from Chenjie Zeng self-related feed) — **The co-design,
development, and preliminary evaluation of a comprehensive breast
cancer risk report incorporating polygenic risk information**. Direct
on the **PGS clinical-implementation** wing — this is the "how do
patients read a PGS report" companion to any PGS-tails / composite-risk
methods paper.

Two additional **METHODS-WATCH** items round out the window: Sharma &
Tapadiya arXiv 2608.25148 (frozen-hematology-FM audit under acquisition
shift — the *pretraining-contamination-audit* rising sub-thread; the
paper explicitly identifies DinoBloom's pretraining exposure overlap
with a downstream benchmark) and Bhandari et al. arXiv 2608.15775
(Bayesian causal mediation for zero-inflated longitudinal data — the
methods framework transports to CH VAF trajectory analysis).

---

## Detailed reports

Each entry: bucket (HIGH / METHODS-WATCH / MEDIUM / SKIP), citation,
one-paragraph analytic summary tied to `INTERESTS.md` threads. Sorted
by bucket, then source.

### HIGH — surfaced this window

#### HIGH — Wu W, Li G, Wang K, Xu H, Xiao H, Hu C, Liu S, Tang C, Liu F, Zou Z, Li B, Li J, Zhang CL, Wong H, Chong I, Lu W, Sun Z, Yin Y, Loupy A, Oermann E, Al Dajani SA, Zhu H, Gootenberg J, Abudayyeh OO, Gladyshev VN, Rasko JEJ, Zhang K; *International Consortium of Digital Twins in Healthcare and Medicine.* **Longitudinal alignments and syntheses of multimodal clinical data for personalized medicine with the PULSE framework.** *Nature Computational Science* 2026 Aug 26. doi:10.1038/s43588-026-01026-5 (PMID 42649447; `UK Biobank` PubMed feed).

**Direct hit on the *Digital twins from EHR data* rising sub-thread**
in `EHR foundation models` (INTERESTS.md line ~120). Same consortium
name (International Consortium of Digital Twins in Healthcare and
Medicine) that the *Cell* 2026 field-defining framing paper is
organized under. The named authorship signals a *methods-first
implementation* companion to the *Cell* framing piece — Zhang / Oermann
/ Gladyshev / Loupy / Abudayyeh are the same coalition that put the
digital-twins-in-healthcare white paper together. Read for: (1)
whether PULSE is a shared *alignment* backbone (so multiple sites can
line up their EHR timelines into a common longitudinal frame) or a
site-local *synthesis* system; (2) what modalities it accepts (codes,
labs, notes, imaging, wearables, -omics) and how it handles missingness
across the joins; (3) benchmarks — MEDS / EHRSHOT / MIMIC-IV or an
in-house consortium cohort; (4) whether it publishes a portability
audit under site shift (BioVU vs. AoU vs. UKB vs. MIMIC), which is the
audit lever the `Fidelity, portability, and audit of representations`
sub-topic (INTERESTS.md line ~171) wants propagated. Whatever the
answers, **cite this alongside the *Cell* Digital-Twins framing paper
as the two-paper anchor bundle** for any digital-twin-from-EHR methods
essay this year; the sub-thread now has both a manifesto and a
reference implementation.

#### HIGH — Kayaalp B, Çil K, Conil C, Cobat A, Kars ME, Itan Y, Casanova JL, Özçelik T. **Prediction of human missense variant effects from functional evidence.** *Nature Genetics* 2026 Aug 26. doi:10.1038/s41588-026-02727-3 (PMID 42649388; `UK Biobank` PubMed feed).

**Direct anchor for the ACMG / ClinGen thread** (INTERESTS.md line
~66). The title compresses two of the three canonical evidence pillars
in the ACMG-AMP framework (functional-evidence PS3 / BS3) with
missense-variant effect prediction, which is where the field is
consolidating (AlphaMissense, ESM1v, PopEVE lineage). Casanova group as
senior lineage signals an inborn-error-of-immunity / IUIS phenotype
grounding rather than a pure computational-benchmark paper. Read for:
(1) the source of functional evidence (deep mutational scans, MAVEs,
saturation-mutagenesis screens, protein-abundance assays) and how they
combine multiple assays; (2) whether they benchmark against
AlphaMissense / EVE / PrimateAI-3D on ClinVar 2-star+; (3) whether they
propose a *quantitative* PS3-strength calibration (functional-evidence
strength as a graded rather than binary variable, in the ClinGen SVI
"quantitative approaches to functional evidence" tradition); (4) their
UKB use-case (why the PubMed alert fires on `UK Biobank` — likely a
population-scale carrier-frequency validation cohort). Pair with the
Mitev variant-classification-platform framework paper (08-17 report)
as the two anchor references — Mitev covers the *platform-evaluation*
layer, Kayaalp covers the *evidence-integration* layer.

#### HIGH — Squires S, Saleh RN, Pilling LC, Atkins JL, Ranson JM, Tai XY, Vauzour D, Llewellyn DJ, Minihane AM. **Hormone replacement therapy and dementia risk among postmenopausal women: Identifying responsive subgroups in the UK Biobank.** *Alzheimer's & Dementia* 2026 Aug;22(8):e71679. doi:10.1002/alz.71679 (PMID 42644405; `UK Biobank` PubMed feed).

**Direct hit on both the HRT pharmacoepi watchlist** (INTERESTS.md
line ~50 — the HRT initiation / persistence sub-thread) **and the
HTE / responsive-subgroup wing of ML for precision health**
(INTERESTS.md line ~208). The "responsive subgroups" phrasing signals
either a causal-forest / meta-learner heterogeneous-treatment-effect
design or a stratified subgroup analysis with pre-specified effect
modifiers (APOE ε4, age at initiation, formulation, route). Read for:
(1) the estimand (ATE vs. subgroup-specific CATE vs. best-arm-assignment
policy); (2) which effect-modifiers were pre-specified vs. discovered
(APOE, WHI-style formulation/route, time-since-menopause window); (3)
whether they handle prevalent-user bias (HRT initiation is confounded
by menopausal-symptom severity and healthy-user selection); (4) how
they define dementia incidence (all-cause vs. AD-specific), which
matters for the timing-of-onset subgroup story. This paper is a
template for the exact analysis structure I'd want portable to:
CFTR-modulator responder subgroups in AoU/UKB, GLP-1 RA
discontinuation-responsive subgroups, and statin discontinuation
outcomes. Pair with Reho et al. Pharmacoexposomics (08-17 report,
Hripcsak feed) as the framing + methods pair for stratified pharmacoepi.

#### HIGH — Huang J, Liu C, Sperling LS, Quyyumi AA, Sun YV. **Proteomic mediators linking autoimmune diseases to major adverse cardiovascular events: Insights from the UK Biobank.** *Proteomes* 2026 Jul 24;14(3):38. doi:10.3390/proteomes14030038 (PMID 42647374; `UK Biobank` PubMed feed).

**Direct hit on the autoimmune-disease thread** (INTERESTS.md line
~111 — IBD listed explicitly, "shared with broader autoimmune work")
**and the multi-omics-augmented PRS sub-thread** (INTERESTS.md line
~85). Proteomic *mediation* is the specific design shape I want
propagated — a causal-inference mediation structure with Olink
proteomics as the intermediate layer between autoimmune exposure and
MACE endpoint. Read for: (1) which autoimmune diseases were the
exposures (RA / SLE / IBD / psoriasis / MS); (2) how they handled
temporal ordering (autoimmune diagnosis must precede baseline
proteomics measurement); (3) which mediation estimator (VanderWeele
natural direct/indirect, g-formula) and how they handled multiple
mediators; (4) the top mediating proteins and whether they overlap with
known atherosclerosis pQTL colocalization results. This is the direct
CV-outcome complement to the Aging Cell 2026 sleep-proteomic + aging
paper (Liu et al. PMID 42649471). Sun YV is a Emory PheWAS /
biomarker-mediation lineage; expect a methodologically careful paper.

#### HIGH — Han Y, Chen B, Gao Y, Zhang X, Wang S, Dai H, Xu W, et al. **Genetic βAR signaling modifies clonal hematopoiesis-associated mortality in patients with atherosclerotic cardiovascular disease.** ResearchSquare preprint rs-10583290, 2026 (fires `All of Us research program` + `intitle:"clonal hematopoiesis"` keyword feeds).

**Direct hit on the CHIP / VEXAS / LOY somatic-mosaicism thread**
(INTERESTS.md line ~103). Explicitly ascertains CHIP in **~550,000 UK
Biobank WES + All of Us initial WGS release cohort** — the exact
biobank-scale CHIP-ascertainment protocol I need to align current AoU
CHIP work with. β-adrenergic-receptor genotype × CHIP interaction on
mortality is a nice "signaling-modifier-of-CHIP-effect" design that
sits alongside the Kessler *Nature* 2022 lineage on CHIP mortality
predictors. Read for: (1) the exact CHIP-calling protocol on AoU WGS
(mutect2 tumor-only, PLINK-based VAF filtering, driver-gene panel
choice — this is the protocol you need aligned with the Machiela / Loh
canon); (2) whether they used the *Li et al. Atherosclerosis 2026*
(LOY × PAD) design as a template; (3) whether AoU + UKB estimates
replicate — a portability check; (4) whether the βAR modifier
generalizes across CHIP driver genes (DNMT3A / TET2 / ASXL1) or is
gene-specific. Read alongside Streck et al. (below) as the
TET2-specific vascular-CHIP hit.

#### HIGH — Streck E, Harloff M, Freuer D, Dintner S, Dedegkikas D, et al. **TET2-mutant clonal hematopoiesis is associated with peripheral bypass graft occlusion: a multicenter retrospective cohort pilot study.** *JVS-Vascular Science* 2026 (`intitle:"clonal hematopoiesis"` keyword feed).

**Direct hit on the CHIP thread, vascular sub-arm**. Multicenter
retrospective cohort with TET2-driver specificity. Pilot study — read
for effect size and n, but the *design* is highly portable: bypass
graft patency is a hard, well-adjudicated vascular endpoint on which
CHIP effect is *expected* (inflammation-driven neointimal hyperplasia)
but not previously well-quantified. Should sit alongside Li et al.
*Atherosclerosis* 2026 (LOY × PAD) and Han et al. (above) as the three
vascular-CHIP / vascular-somatic-mosaicism data points in the
2026 catch.

#### HIGH — Tang B, Kuai Y, Ye Z, Zhao X, Fan C, Huang M, Luo Y, et al. **Clonal hematopoiesis as a context-dependent modifier of organ-specific disease: Evidence, mechanisms, and translational boundaries.** *Cell Investigation* 2026 (`intitle:"clonal hematopoiesis"` keyword feed).

**CHIP-as-context-dependent-modifier review paper**. Reviews rather
than primary data, but the framing — CH as an organ-specific *modifier*
rather than a systemic risk factor — is exactly the analytical framing
INTERESTS.md line ~103 wants propagated. Directly cite this when
writing about CHIP-modifier-of-organ-outcome for CVD, CKD, liver
disease, or CNS. Read for: (1) which organs they treat as "modified"
(kidney, liver, brain, vasculature), (2) whether they handle the
DNMT3A vs. TET2 vs. ASXL1 gene-specificity of the modifier claims;
(3) how they treat translational boundaries (mouse ↔ human,
mechanism ↔ clinical outcome).

#### HIGH — Guo X, Hu J, Tian H, Yan C, Liu Q, Zhou T, Liu C, et al. **Trans-ancestry meta-analysis of genome-wide association study identifies eight novel genetic loci in type 1 diabetes: A multi-population study.** *Diabetic Medicine* 2026 (fires **Chenjie Zeng self-related feed**).

**Cross / trans-ancestry T1D GWAS with 8 novel loci**. Fires the
self-related feed, which is a signal that the discovery is likely to
touch cohorts / methods that align with recent T1D work in Zeng's
lineage. Direct on the **cross / trans-ancestry portability**
sub-thread of `Genetic epidemiology` (INTERESTS.md line ~72) and,
because T1D is a biobank-EHR outcome that MVP / AoU / UKB all define
via phecodes, the loci become newly discoverable in downstream PRS ×
outcome work. Read for: (1) contributing cohort composition (which
non-European ancestries carried the new-locus signal); (2) whether any
of the 8 loci are already ClinVar / OMIM known for T1D syndromic forms
(HLA-region vs. non-HLA); (3) whether they build a **trans-ancestry
PRS** for T1D and audit its portability, which is the sub-thread
question. Slot this alongside any AoU T1D phecode analysis for
pre-registration purposes.

#### HIGH — Hanley MN, Purvis R, Limb S, Saya S, Bickerstaffe A, et al. **The co-design, development, and preliminary evaluation of a comprehensive breast cancer risk report incorporating polygenic risk information.** *European Journal of Human Genetics* 2026 (fires **Chenjie Zeng self-related feed**).

**PGS clinical-implementation companion piece**. Co-design method
paper for a comprehensive breast-cancer risk report. This is the
"how patients read a PGS report" complement to any methodology work on
PGS tails / composite risk. Direct on the *precision-medicine clinical
decision* end of `ML for precision health` (INTERESTS.md line ~215):
this is exactly the "clinical decision (who to screen, when to
escalate)" hook the thread prioritizes. Read for: (1) co-design
methodology (who was in the room — clinicians, patients, genetic
counselors, at-risk women); (2) how they present PGS + traditional
risk factors + rare-variant status jointly (the composite-risk framing
INTERESTS.md line ~74 wants); (3) preliminary usability metrics (recall
of numeric risk, calibration of subjective vs. objective risk, decision
regret). Should sit in the reading pile whenever writing about the
translation of a composite risk model into a patient-facing artifact.

#### HIGH — Lee H, Min YW, Oh YE, Kim TS, Min BH, Lee JH, et al. **Genetic assessment of oesophageal safety of GLP-1 and GIP receptor perturbation: A drug-target Mendelian randomisation study.** *Biomedicines* 2026;14(9):1887 (`"variant interpretation" OR "variant classification" OR "Causal Variant"` keyword feed, colocalization content).

**Drug-target MR of GLP-1 and GIP receptor perturbation with
colocalization**. Direct hit on the **drug-target Mendelian
randomisation triangulated with observational cohort estimates**
rising sub-thread (INTERESTS.md line ~64) *and* on the **GLP-1 RA
pharmacoepi watchlist** at the same time. Oesophageal safety is one of
the standing GLP-1 RA safety questions since Barrett's / oesophageal
adenocarcinoma associations were flagged; drug-target MR is the
appropriate "does the mechanism itself cause harm" question separated
from confounded observational associations. Read for: (1) instruments
(GLP-1R and GIPR cis-pQTL / cis-eQTL); (2) outcomes (GERD phecode,
Barrett's oesophagus, oesophageal adenocarcinoma); (3) coloc PP.H4
thresholds and sensitivity to prior; (4) whether they triangulate with
a real-world pharmacoepi target-trial emulation (as the Saxby et al.
metformin × AAA lineage does — INTERESTS.md line ~66). This is the
methods template I want to see applied to CFTR-modulator × pregnancy
safety (currently unanswered) and HRT × cardiovascular safety.

#### HIGH — Aceves-Ewing NM, Li-Villarreal N, Li X, Lalani SR, Rosenfeld JA, Petrosyan V, Milosavljevic A, et al.; *Undiagnosed Diseases Network*; *BCM Center for Precision Medicine Models*. **Biallelic variants in KMO cause a novel form of congenital NAD deficiency.** medRxiv 2026 Aug 27. doi:10.64898/2026.08.24.26360911.

**Rare-variant / rare-disease paper from UDN + BCM Center for
Precision Medicine Models** — direct hit on the `Rare disease` thread
(INTERESTS.md line ~193) and specifically on the *diagnostic reanalysis
of unsolved cases* rising sub-thread (INTERESTS.md line ~205,
Uria-Regojo mid-scale reanalysis reference). The KMO gene sits in the
kynurenine pathway → NAD biosynthesis; biallelic loss-of-function
causing a congenital NAD deficiency phenocopies existing NAD-deficient
syndromes and is exactly the sort of *"expandable phenotype space" via
HPO-similarity* case UDN specializes in. Read for: (1) case-family
size and consanguinity structure; (2) functional confirmation
(fibroblast / iPSC-derived hepatocyte NAD assay, LC-MS metabolomics of
kynurenine intermediates); (3) whether they propose a therapeutic
avenue (dietary niacin supplementation is the obvious first line if
KMO is the missing enzyme); (4) how they connect this to the
already-known *HAAO* / *KYNU* biallelic congenital-NAD-deficiency
lineage. Slot into the UDN reading pile whenever the rare-disease-
diagnosis thread reactivates.

### METHODS-WATCH — surfaced this window

#### METHODS-WATCH — Sharma JK, Tapadiya P. **Can You Trust Frozen Hematology Foundation Models under Acquisition Shift?** arXiv 2608.25148v1 (cs.CV, 2026-08-25).

Audits 15 frozen encoders (hematology / pathology / general-vision
FMs) across 4 public single-cell WBC acquisition domains along
**accuracy robustness and calibration**. Findings: in-domain
linear-probe F1 is saturated (0.98–0.997), but cross-dataset F1 drops
34–72% and rankings re-order — DinoBloom-L, the in-domain best, falls
to 10th of 15 on the most-shifted target (MLL23). Calibration ECE
collapses from 0.004 in-domain to 0.35 off-domain. Introduces
**Class-Balanced Re-standardization (CBR)**, a training-free
pseudo-label-balanced feature normalization that improves all target-
prior scenario means. Critically for the *pretraining-contamination
audit* sub-thread (INTERESTS.md line ~124), **the paper explicitly
identifies MLL23 as DinoBloom's internal cohort**, so the benchmark
cannot isolate exposure from scanner-associated shift — a
pretraining-contamination confounder discovered in the wild. This is
the exact protocol I want propagated to CLMBR / MOTOR / MEDS benchmark
contamination audits: when a foundation-model paper reports a "held-
out" benchmark, verify that the model was not pretrained on it. Read
for: (1) the CBR normalization recipe; (2) their probe-choice
guidance (1-NN retrieval more stable than linear head on average but
neither universally predicts robustness); (3) how they handled
scanner metadata to disentangle acquisition shift from
class-prior shift.

#### METHODS-WATCH — Bhandari S, Kar W, Daniels MJ, Karmakar B. **Causal mediation analysis for zero-inflated longitudinal data in the presence of treatment non-compliance and multiple mediators.** arXiv 2608.15775v1 (stat.ME, 2026-08-16). Score 1.

Bayesian causal mediation framework with **enriched Dirichlet process
mixture models** and a scalable G-computation algorithm for
**zero-inflated multi-mediator longitudinal data with non-compliance**.
Application is off-topic (email marketing), but the methods framework
transports directly to the **CH / LOY VAF trajectory analysis**
under `CHIP / VEXAS / LOY` (INTERESTS.md line ~103): VAF trajectories
are zero-inflated (below-detection-threshold observations) and
longitudinal, and any CH-outcome mediation analysis (e.g. CHIP →
Olink inflammatory-protein panel → CV outcome) has multiple mediators.
Pair with Bandreddi et al. (Tobit-vs-hurdle CHIP, 08-17 report) as the
two zero-inflated-longitudinal reference points for the CH sub-thread.

#### METHODS-WATCH — Kung KC, Martin NK, Lok JJ. **Regression Not-to-the-Mean: An Oddity of Regression, Illustrated with the Risk of Overdose Deaths.** arXiv 2608.15399v1 (stat.AP, 2026-08-15). Score 1.

Shows that constant-treatment-effect models in longitudinal settings
with staggered treatment and **heterogeneous treatment effects across
treatment durations** can produce negative-weight artifacts, and that
the negative-weight issue affects **logistic regression** models
too (not just linear). Empirical illustration on drug-induced-homicide
prosecutions × overdose-deaths. Directly relevant to the
**heterogeneous-treatment-effect wing of ML for precision health**
(INTERESTS.md line ~209) and to any pharmacoepi TTE where the treatment
duration varies (which is essentially all of them — CFTR-modulator,
GLP-1 RA, statin persistence). Bookmark for citing whenever writing
about **staggered-treatment TTE** and reviewer asks why you did or
didn't use a constant-effect specification.

#### METHODS-WATCH — Nadig A, Fu J, Satterstrom FK, Auwerx C, Zhang Z, Torene R, Lu W, Karczewski KJ, The Autism Sequencing Consortium, GeneDx, Buxbaum JD, Kruszka P, Talkowski M, Robinson EB, O'Connor LJ. **Estimating the contribution of coding mutations to autism.** medRxiv 2026 Aug 27. doi:10.64898/2026.08.25.26361328.

**Karczewski-lineage rare-variant paper on autism coding-variant
contribution**. Sits at the intersection of **rare-variant methods**
(INTERESTS.md line ~193) and **PGS-tails / composite-risk designs**
(INTERESTS.md line ~74–84). Read for: (1) the fraction of ASD
liability attributed to *de novo* vs. inherited coding variants;
(2) how they combine population-frequency, functional annotation, and
gene-constraint priors; (3) whether the estimate is calibrated by
ancestry (Karczewski / gnomAD lineage suggests yes); (4) whether they
address the *Baya AJHG 2026 "misaligned individuals" (PGS residual)*
framing you added to INTERESTS.md line ~80 — i.e., does the coding-
variant contribution differ for high-PGS-tail vs. residual-outlier
individuals? Adjacent to but not squarely on the phenotype threads,
so filed as METHODS-WATCH.

#### METHODS-WATCH — Ji S, Li T. **Site-Resolved Plasma-Protein Architecture of Infection Susceptibility: A Cis-pQTL Mendelian Randomization and Colocalization Study.** *Genes* 2026 Jul 29;17(8):887. doi:10.3390/genes17080887 (PMID 42650080; `UK Biobank` PubMed feed).

**cis-pQTL MR + colocalization** for infection susceptibility. Not
central to any active disease thread but the *methods template* is
directly on the **drug-target MR triangulated with observational
cohort estimates** rising sub-thread (INTERESTS.md line ~66) and the
**multi-omics-augmented PRS** thread (INTERESTS.md line ~85). Read for
the exact instrument-selection recipe (cis-only, LD-clumping choices,
Steiger filtering) — the recipe is portable to CFTR-modulator target
MR and to any autoimmune-cytokine drug-target MR work.

#### METHODS-WATCH — Zheng C, Shivakumar M, Shen L, Kim D. **Absorption and Co-expression Modules Show Where Polygenic and Proteomic Risk Scores Diverge in Neurodegenerative Diseases.** medRxiv 2026 Aug 27. doi:10.64898/2026.08.24.26361271.

**Polygenic × proteomic risk-score divergence diagnostic**. Direct on
the **multi-omics-augmented PRS** rising sub-thread (INTERESTS.md
line ~85). The "absorption and co-expression modules" framing is a
weighted-module structure that identifies *which* biological pathways
proteomics captures but PGS misses (or vice versa), which is exactly
the informative divergence needed to argue for stacking PGS with Olink
proteomics rather than picking one. Read for: (1) which neurodegenerative
diseases (AD, PD, ALS, FTD); (2) whether the divergence is in early-vs-
late-life age (proteomics captures acquired risk that early-life PGS
cannot); (3) whether they operationalize a **stacked PGS + proteomic
score** and report calibration improvement; (4) UKB / AoU / mDNA
Alliance cohort provenance.

#### METHODS-WATCH — Vitali F, Raikes AC, Merlini S, Shang Y, et al. **Sex- and APOE-specific transcriptomic drug repurposing identifies four candidate therapeutics for Alzheimer's disease.** *Alzheimer's & Dementia: Translational Research & Clinical Interventions* 2026 (`drug repurposing` keyword feed).

**Sex- and APOE-stratified transcriptomic drug repurposing for AD**.
Directly on the **drug repurposing** thread (INTERESTS.md line ~184).
The *sex × APOE* stratification is what makes this METHODS-WATCH: it's
exactly the "individualized drug-target repurposing" lens that couples
`PGS × exposure` interactions (Nagpal & Gibson lineage, INTERESTS.md
line ~82) with actionable therapeutic hypotheses. Read for: (1)
whether they build a proper **causal-inference framing of off-label
use** (target-trial emulation of the four candidates) or stop at
signature-matching prioritization — INTERESTS.md line ~187 wants the
former; (2) which four candidates and whether any are already in
active EHR-based off-label prescribing (mineable in AoU / MVP); (3)
their integration framework — LINCS / CMap signature vs. differential-
gene-network approach. Compare to de Andrés-Galiana et al. ALS
transcriptome-wide repurposing (08-17 report).

#### METHODS-WATCH — Tan TY, Haas S, Gao X, Li J, Araji S, Liu A, Wimberly C, Gold N, Rentas S, Duyzend M, Walsh KM, Cohen JL. **Expanding reproductive genetic screening through the inclusion of perinatal treatability.** medRxiv 2026 Aug 27. doi:10.64898/2026.08.24.26361139.

**Reproductive-genetic-screening expansion with perinatal-treatability
prioritization**. Sits at the intersection of **ACMG / ClinGen VCEP
variant classification** (INTERESTS.md line ~66) and rare-disease
identification. Perinatal-treatability as a curation criterion is a
nice explicit shift from "carrier screening = severity" to "carrier
screening = actionability" — same shift ACMG has been slowly making on
its secondary-findings list (SF v3 → SF v3.1). Read for: (1) which
gene panel; (2) how they operationalize "perinatal treatability"
(explicit therapy vs. surveillance vs. delivery-planning); (3) whether
they include CFTR / cystic-fibrosis newborn-screening-actionable
variants (INTERESTS.md line ~100 asks for CFTR-modulator eligibility
tracking). Slot into the ACMG-adjacent reading pile.

#### METHODS-WATCH — Tipping O, Wang M, Martin R, Sperrin M, Renehan A. **New-onset type 2 diabetes mellitus and obesity-related cancer risk: a matched cohort study (UK Biobank).** medRxiv 2026 Aug 27. doi:10.64898/2026.08.25.26360729.

**UKB matched cohort of new-onset T2DM → obesity-related cancer**.
Direct on the **pharmacoepi with EHR outcomes** and **biobank +
EHR** threads. Read for the matching design (new-onset T2DM cases vs.
non-diabetic BMI-matched controls) and whether they handle GLP-1 RA /
SGLT2i / metformin exposure as effect modifiers (which is the natural
extension question). This is the *substrate* study — the pharmacoepi
methods extension is a natural follow-up target-trial-emulation for
T2DM medication choice × obesity-related-cancer outcomes.

#### METHODS-WATCH — Marella P, Subramanian V, Habiel M. **Reply to Correspondence for Non-infectious Uveitis is Associated With Increased Psychiatric Comorbidities: An All of Us Research Program Analysis.** *Am J Ophthalmol* 2026 Aug 26 (PMID 42648622; `All of Us` PubMed feed).

Reply-to-correspondence for an **AoU-based phecode analysis** of
non-infectious uveitis × psychiatric comorbidities. Direct on the
**All of Us / EHR-linked biobank** thread (INTERESTS.md line ~28). Read
the reply (and the underlying correspondence + original paper) as an
example of *what reviewers push back on for AoU phecode analyses* —
useful for future methods design. Autoimmune / immune-mediated
inflammatory disease × psychiatric-comorbidity is a real thread in the
`Chronic disease clustering and multimorbidity` slot (INTERESTS.md
line ~220).

### MEDIUM — surfaced this window

#### MEDIUM — Reed ER, Wysocki M, Gal M, Aleksic S, Gao T, Barzilai N, Ye K, Bortnick AE, Andersen SL, Perls T, Sebastiani P, Milman S. **Exceptional Parental Longevity and Onset of Morbidity and Mortality Across Cohorts.** *JAMA Netw Open* 2026 Aug 3;9(8):e2630964 (PMID 42646838).

Longevity-genetics observational study. Familial exceptional longevity
as a proxy for successful-aging genetics. Adjacent to the
*multimorbidity* and *aging-related risk-profile* threads but not
squarely on active methods work. Read only if the aging / multimorbidity
sub-thread is reactivated.

#### MEDIUM — Liu R, Luo J, Zhang Y, Wang F, Xu J, Cao W, Sun S. **Associations Between Accelerometer-Assessed Sleep Patterns, Proteomic Signatures, and Hallmarks of Aging in Adulthood.** *Aging Cell* 2026 Sep;25(9):e70685 (PMID 42649471).

Objective-sleep × proteomics × aging-biomarker triad in UKB. Adjacent
to the multi-omics-augmented PRS thread and the aging thread. Read if
extending the proteomics-as-mediator design (Huang et al. above) to a
non-disease phenotype (biological-age).

#### MEDIUM — Zhong Y, Xia M, Zhao X, et al. **Construction and Validation of Plasma Protein-Based Musculoskeletal Biological Age and Genetic and Environmental Risk Profiles.** *Aging Cell* 2026;25(8):e70636 (PMID 42649044).

Plasma-proteome-derived biological-age construct for musculoskeletal
health, plus genetic and environmental risk profiles. Same
"proteomic-clock" family as prior Aging Cell papers. Read only if the
multi-omics-augmented PRS thread pivots into the biological-age
subarea.

#### MEDIUM — Easton D, Blundell J, MacGregor H. **Shared inheritance reveals landscape of somatic and germline cancer risk in TP53.** 2026 (`variant interpretation` keyword feed).

**Combined germline + somatic TP53 risk landscape**. Direct on the
composite-risk framing (INTERESTS.md line ~74). Interesting claim in
the snippet — "somatic rather than germline risk predominates in
middle-aged healthy adults" — flips the standard TP53 Li-Fraumeni
framing. Medium priority because TP53 sits outside the CF / APOL1 /
CHIP core disease list, but read for the framework if working on
combined-germline-somatic risk in other genes.

#### MEDIUM — Chenchula S, Srinivasamurthy SK, et al. **Pharmacogenetic Predictors of Chemotherapy Treatment-Related Toxicities in Paediatric and Adolescent Acute Lymphoblastic Leukemia: A Systematic Review, Meta-Analysis and Literature-Based Candidate Prioritization.** *Pharmaceuticals* 2026 Aug 1;19(8):1204 (PMID 42653702).

Pharmacogenetic systematic review of paediatric ALL chemotherapy
toxicity. Adjacent to the *pharmacogenomic-modifier-of-medication-
persistence* sub-thread (INTERESTS.md line ~62) — pharmacogenetics is
in scope, though paediatric oncology is off the primary thread.
Bookmark if PGx-modifier-of-persistence work expands into paediatric
chronic-disease cohorts.

#### MEDIUM — Ying Y, Li R, Huang J, Hou J, et al. **Association of cardiovascular-kidney-metabolic syndrome with blinding eye diseases: insights from a UK Biobank cohort analysis.** *Eye (Lond)* 2026 Aug 26 (PMID 42649279).

UKB observational analysis of the AHA-defined CKM syndrome × eye
disease. Adjacent to the multimorbidity thread (INTERESTS.md line
~220) — CKM is a cardiometabolic multimorbidity construct. Read if the
multimorbidity clustering sub-thread reactivates on CKM specifically.

#### MEDIUM — Wang J, Fang H, et al. **Bidirectional Association Between Diabetes and Osteoarthritis: A Population-Based Cohort Study.** *Diabetes Obes Metab* 2026 Aug 26 (PMID 42649112).

Bidirectional T2DM ↔ OA cohort analysis. Off primary thread. Medium
only because bidirectional-outcome designs are useful reference
templates for the multimorbidity thread.

#### MEDIUM — Chang E, Xie K, Zhou DJ, Korzun J, Conrad EC, Roth D, et al. **Automated epilepsy and seizure type phenotyping with transformer-based language models.** *npj Digital Medicine* 2026 (Peter Szolovits new-related feed, already flagged HIGH in the 08-17 report — carried over as a *published-version* update from the earlier snippet; treat as read-when-full-text-available).

Same paper flagged HIGH in the 08-17 report. Downgraded here only
because it was already surfaced; not a new item, just carried over to
confirm the full-text publication.

### LOW — surfaced this window

- **Niu M, Feng Y, Shu K, et al.** *The Role of Integrin Family in
  Atherosclerotic Cardiovascular Disease: A Prospective Cohort Study
  and Mendelian Randomization Analysis.* Biomedicines 2026 (PMID
  42652217). Standard MR + cohort; off primary thread.
- **Yang L, Lin W, Mirsattari SM.** *A Shared Systemic Metabolic
  Signature Across the Neurological Disease Spectrum: A Summary-Level
  Analysis of 274,241 UK Biobank Participants.* Biomedicines 2026
  (PMID 42652156). Summary-level metabolomics × neuro disease. Read
  only if metabolomics-augmented PRS expands into CNS.
- **Wu X, Yang J, Cao W, et al.** *EpiSNPdb: A Comprehensive Database
  of Genetic Epistasis Across Multiple Cancer Types.* Curr Issues Mol
  Biol 2026 (PMID 42651752). Epistasis catalog resource.
- **Kwon RJ, Lim Y.** *Association of Lifestyle Behaviors and Cancer
  Risk in MetALD.* Cancers 2026 (PMID 42649878). MetALD × cancer
  lifestyle-association analysis. Off primary thread.
- **Dai D, Ma M.** *A lightweight machine learning approach for
  predicting breast cancer risk based on routine clinical indicators
  in the Chinese population.* Health Informatics J 2026 (PMID
  42647514). Standard-format risk-prediction paper without a distinctive
  design lever. Off primary methods thread.
- **Rong L, Zhu J, Liu Y, et al.** *Integrative Multi-Omics-Informed
  Analysis Identifies Insulin Therapy-Associated Loci Implicated in
  Osteoarthritis Susceptibility.* Chem Biol Drug Des 2026 (PMID
  42644749). Off primary thread.
- **Naik A, Olier I, et al.** *Multi-horizon machine learning for
  population-level hypertension risk stratification in the UK Biobank.*
  Eur Heart J Digit Health 2026 (PMID 42644167). Standard ML risk
  stratification without a distinctive HTE / calibration angle.
- **Sheng L, He W, Wang F, et al.** *Pro-inflammatory diet in pregnancy
  associated with increased risk of abnormal perinatal outcomes: UK
  Biobank.* Front Public Health 2026 (PMID 42643636). Off methods
  thread.
- **Wang K, Han R, Huang Y, Cai J, Wu X.** *Associations between novel
  triglyceride glucose and adiposity-related indices and risk of MASLD:
  mediating role of biological aging: UK Biobank.* Front Endocrinol
  2026 (PMID 42643580). Off primary thread.
- **Fadaei S, Krebs FS, Zoete V.** *Structure-conditioned self-
  supervised learning of residue interaction constraints in protein
  kinases for variant interpretation.* Bioinformatics 2026. Kinase-
  domain-specific variant-effect prediction; specialized methods
  paper. Off primary CF / APOL1 / CHIP thread but a reference for
  domain-specific variant interpretation methodology.
- **Kumar A, Kumar D, Hivale NS, et al.** *Magnetically Triggered
  Nanocarriers for Targeted Burn Wound Healing: A Drug Repurposing
  Approach.* J Drug Deliv Sci Technol 2026. Off primary thread (drug
  delivery + repurposing for wound healing).
- **Bulk of bioRxiv / medRxiv Aug 27 postings** (protein-topology
  prediction, spatial-DNA sequencing, single-cell CRISPR, Drosophila
  copper response, splice-predictor benchmarking). Individually
  off-thread but the Akey / Bierman / Zhang "Principled Framework for
  Using Correlated Traits to Improve Risk Prediction" is worth a
  30-sec check if PRS-with-correlated-traits work reactivates.

### SKIP — surfaced this window (off-thread)

- **arxiv-digest 08-18 Moriña.** RSV seasonal-intervention Bayesian
  epidemic alignment. Off (infectious-disease timeseries).
- **arxiv-digest 08-18 Daza.** Digital-health N-of-1 primer. Ancillary
  interest only.
- **arxiv-digest 08-18 Bhandari (email marketing).** Statistical
  method is METHODS-WATCH above; application is SKIP.
- **arxiv-digest 08-20 Monroe MFM.** Off (chemistry).
- **arxiv-digest 08-20 Machacuay / Yao (Peru mayoral, urban rail
  DML).** Off (public policy, transit).
- **arxiv-digest 08-25 Leimenstoll.** Off (climate / finance).
- **arxiv-digest 08-26 RIBOSPAN.** Off (RNA foundation model,
  transcriptomics infrastructure).
- **Various generic LLM / RL / graph-benchmark papers** from
  Marinka Zitnik / Zhiyong Lu / Peter Szolovits new-related feeds
  (Dynamic Multi-Byte Prediction, SKILLER small-LM RL, Recursive
  Vision-Language Models, HumanCLAW VLM-through-body). Off clinical
  agent / clinical LLM thread.
- **Kozin Porat / Weinstein UKB ADHD × lifestyle association.** Off
  methods thread.
- **Douglas et al. Social Pharmaceutical Innovation.** Policy /
  sociology-of-science piece; off methods thread.

---

## What's NOT in the report

- **GitHub `arxiv-digest` cron / PR notifications** — still zero
  Gmail hits from `from:notifications@github.com` × `arxiv-digest`,
  `chenjiezeng`, or `arxiv` in the last 30 days. The `arxiv-digest`
  pipeline commits its output to this local repo rather than emailing
  PR / cron notifications; the on-disk `digests/YYYY-MM-DD.md` files
  serve as the artifact.
- **JAMA / Nature Medicine / NEJM Online-First banners.** Received but
  no items crossed the on-thread threshold this window (JAMA "How AI
  Agents Could Help Patients With Heart Failure" is a maternal-fetal
  reflection piece, off-thread; "Online First" batches were the
  standard weekly digest).
- **Substack / newsletters** (AINews, unwindai, alphasignal). Noted
  but no biomedical content in this window crossed the on-thread
  threshold.
- **arxiv.org daily category mailings** (`no-reply@arxiv.org`,
  addressed to `rabble@arxiv.org` — a mailing list). Raw upstream feed
  that supplies the `arxiv-digest` pipeline; papers surfaced via the
  digest are covered in the arxiv-digest section above.

## Next steps to consider

1. **Read the PULSE paper (Wu et al. *Nat Comput Sci* 2026) in full
   alongside the *Cell* 2026 Digital-Twins framing paper.** This is
   the highest-signal single pair of the year for the
   `Digital twins from EHR data` sub-thread; treat as a "manifesto +
   reference implementation" bundle for future methods essays on
   EHR-derived individualized-trajectory prediction. Draft a two-paragraph
   commentary linking PULSE to MEDS / EHRSHOT / FEMR as the
   "consortium-scale successor to single-institution EHR-FM
   benchmarks."
2. **Read Kayaalp et al. *Nat Genet* 2026 in full.** This is the
   functional-evidence-integration anchor for ACMG PS3 / BS3
   calibration. Pair with the Mitev variant-classification-platform
   framework paper (08-17 report) for a consolidated variant-curation
   reading list.
3. **Adopt Squires et al. HRT × dementia responsive-subgroups
   template.** Directly portable to the CFTR-modulator responder-
   subgroup design in AoU / UKB CF cohorts and to any GLP-1 RA / statin
   HTE analysis. Read for the exact estimand / effect-modifier
   pre-specification.
4. **Read Huang et al. UKB autoimmune × MACE proteomic-mediation
   paper.** Directly portable to (a) IBD × CV outcomes, (b) any AoU
   / MVP autoimmune cohort with Olink or SomaScan; and (c) the
   proteomics-as-mediator design pattern that would strengthen future
   pharmacoepi work in the drug-class watchlist.
5. **Align current AoU CHIP work with the Han et al. researchsquare
   protocol.** ~550k UKB WES + AoU initial WGS release CHIP
   ascertainment is the operative protocol; get their preprint methods
   next to any in-progress AoU CHIP-calling pipeline before pushing
   downstream analyses.
6. **Read Lee et al. GLP-1R / GIPR drug-target MR paper.** Direct
   template for CFTR-modulator target-MR × pregnancy safety and HRT
   target-MR × cardiovascular safety design questions. Note the
   coloc PP.H4 thresholds and instrument-selection recipe.
7. **File the Hanley et al. breast-cancer PGS-report co-design paper**
   in the PGS clinical-implementation reading pile. Cite whenever
   arguing for a patient-facing artifact of composite risk output.
8. **File Sharma & Tapadiya (frozen-hematology-FM audit) as a
   *pretraining-contamination protocol* reference.** The
   MLL23-is-DinoBloom's-internal-cohort discovery is a real-world
   caught contamination event and a good citable example for future
   CLMBR / MOTOR / MEDS FM benchmark audits.
9. **Watch the Aceves-Ewing KMO → congenital NAD deficiency preprint
   for peer-reviewed publication.** UDN diagnostic paper with a real
   therapeutic angle (niacin / kynurenine-pathway supplementation);
   likely target for *Genet Med* / *AJHG* / *Am J Med Genet A*.

_Report generated 2026-08-28 by scheduled routine; source Gmail
(cezeng21@gmail.com) + local `arxiv-digest` repo + NCBI My-NCBI +
bioRxiv/medRxiv Subject Collection Alerts. No emails were modified.
Next report should cover 08-28 → next scheduled run._
