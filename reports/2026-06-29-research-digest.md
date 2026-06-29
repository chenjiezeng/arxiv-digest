# Research digest report — 2026-06-29

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window covered: roughly **2026-06-16 → 2026-06-29** (the most recent two
weeks of Google Scholar alerts plus the corresponding `digests/` files
from this repo). Two prior report dates (2026-06-18, 2026-06-20) already
covered the earlier slice, so the new content below leans on the
**2026-06-23 → 2026-06-29** Scholar+arXiv window and only revisits earlier
items when they are unusually on-thread.

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Gmail Google Scholar alerts (author + keyword) | 2026-06-16 → 06-29 | ~200 alert threads. Heaviest single-day batches on 06-27 (author-feeds: Chenjie Zeng self-feed, Bastarache, Montgomery, Pritchard, Szolovits, Zitnik, Chute, Bastarache citations, Callahan, Patrick Ryan, Pascal Brandt, Mihaela van der Schaar, Leo Celi, Daniel Kastner, Yuan Luo) and 06-28 (keyword feeds: rare diseases, electronic health records, AoU, PheWAS, drug repurposing, KG, UK Biobank, variant interp, APOL1, clonal hematopoiesis, autoimmune, mendelian, penetrance citations, foundation models + EHR). |
| Gmail arXiv subject-class mailings (q-bio, stat, cs) | 2026-06-23 → 06-29 | Routed to a separate `rabble@arxiv.org` inbox; aggregate digests, not individually triaged. The `arxiv-digest` repo already filters these against the keyword list. |
| `arxiv-digest` repo `digests/` files | 2026-06-16 → 06-28 | 13 daily digests; **the heaviest filtered days** were 06-23 (CF causal-inference paper), 06-19 (PGS/Beacon), 06-18 (UK Biobank measurement-error analysis), 06-17 (foundation-model multimodal cancer), 06-16 (Zitnik biological FM paper). 06-13/-14/-15/-20/-21/-22/-24/-27/-28 were empty or near-empty days. |
| Other newsletters (alphaXiv, marktechpost, rohanpaul, Sebastian Raschka, AI-Made-Simple) | 06-26 → 06-29 | Not research-relevant to active threads — excluded from per-study reports. |

> Caveat: Google Scholar alert emails contain title, authors, venue, and
> the first ~2–3 lines of each abstract only. The per-study writeups
> below contextualize that metadata against your research threads; they
> do not reflect full-text reading. arXiv-digest entries already include
> the full abstract from arXiv, so the deep blocks below for those
> papers are abstract-grounded.

---

## Executive summary

- **One paper this window directly cites your self-feed and is the
  single highest-priority item: Baya et al., *Individuals who deviate
  from polygenic expectation are enriched for damaging variants in genes
  linked to rare disease* (AJHG, 2026).** Surfaces in (a) your own
  Chenjie Zeng "new related research" feed AND (b) the Lisa Bastarache
  "new related research" feed on 06-27 — a double-feed convergence on a
  paper that *fuses two of your active threads*: composite risk models
  stacking PRS with rare pathogenic variants (Genetic epidemiology) AND
  the rare-disease/Mendelian penetrance work (PheWAS/phecode
  infrastructure). This is the most important paper of the window.
  See report #1 below.

- **A second top-tier item: Welland et al. (Broad), *Automated
  reanalysis of genomic data for rare disease diagnostics at scale*
  (Nature Medicine, 2026).** Tool name **Talos**; validated on 1,089
  rare-disease individuals and then deployed for iterative reanalysis on
  an unselected cohort. Hits the **Variant interpretation (ACMG /
  ClinGen)** + **Rare disease** threads squarely; specifically the
  "automated reanalysis" question that VCEPs keep hand-waving about.
  See report #2.

- **Direct citation to your penetrance work appeared in the
  06-28 batch.** "Guidance for estimating penetrance of monogenic …" —
  new citations alert flagged Gorevic et al., *Challenging traditional
  classifications: Gene penetrance in genetically transitional disease*
  (Genes & Diseases, 2026). The same paper surfaces independently in
  the "mendelian diseases" keyword feed. Worth at least skimming the
  citing context for whether their critique of fixed penetrance
  categories is compatible with your population-screening framing.
  See report #3.

- **Substantive Nature paper from the Montgomery feed: Souaiaia, Wu,
  Ori, Choi, Hoggart et al., *Distinct genetic architecture in the
  tails of complex traits* (Nature, 2026).** Heritability is not the
  same in tail vs. center of trait distributions — tails are enriched
  for rare/large-effect variants. This is methodologically important
  for **any extreme-quantile PRS work** and feeds the composite-risk
  thread directly. See report #4.

- **AI-CURA (Science Translational Medicine, 2026) — LLM workflow for
  ACMG-AMP variant classification with explicit accuracy claims.**
  Surfaced in the variant-interpretation keyword feed (06-28). High
  priority for the ACMG/ClinGen thread and the LLM-assisted
  phenotyping/curation overlap. See report #5.

- **In the arxiv-digest repo, the standout filtered paper this window
  is Murali et al., *Causal Inference with Multiple Misclassified
  Exposures: A Control Variate-Adjusted Calibration Weighting Approach*
  (stat.ME, 2026-06-22; in digest 06-23, score=2 on `causal inference`
  + `cystic fibrosis`).** Methods paper that *uses a 651-patient CF
  cohort* as the worked example, comparing throat-swab vs. sputum P.
  aeruginosa exposure measurement and showing 69% attenuation of the
  FEV1 causal effect under misclassification. This lands on **two**
  active threads (causal inference & pharmacoepi; CF/CFTR). See
  report #6.

- **Two PORTER/cafm/Talos-style EHR foundation model papers landed
  this window** — Zheng (cafm — Cohort-Anchored FM, arXiv 2606.21885)
  and Guo et al. (PORTER — Language-grounded portable structured EHR
  FM, arXiv 2606.24102). Both lined up under the "Foundation models +
  EHR" keyword feed. See reports #7 and #8.

- **Two notable PRS infrastructure papers:** Kolosov et al. *PGS
  Browser: a public platform for personalized polygenic score analysis
  and interpretation* (Nat Comms, 2026) and Tarhini et al. *Predicting
  immune-related thyroiditis using polygenic risk scores in patients
  with advanced melanoma* (J ImmunoTherapy Cancer, 2026), both from the
  Chenjie Zeng author feed. See reports #9 and #10.

- **One AoU + OMOP convergence paper:** Patterson, Minto, Beaton et al.,
  *FHIR–OMOP data within the All of Us Research Program*. Hits AoU
  biobank thread + EHR phenotyping/OMOP thread. See report #11.

- **One on-thread CHIP paper from the keyword feed**, but it's a
  hypothesis review (Caradonna et al., *Clonal Hematopoiesis and Gut
  Microbiota–Derived TMAO as Candidate Amplifiers of Cardiovascular
  Inflammation*) — METHODS-WATCH at best, not actionable. Briefly
  noted at the end.

- **APOL1 keyword feed surfaced only one item** (Bankole et al.,
  type 2 diabetes / Nigeria), low priority. Briefly noted at the end.

- **Drug repurposing keyword feed surfaced only one item**
  (Basirpour et al., SGLT2is/dexrazoxane/doxorubicin cardiotoxicity
  review) — METHODS-WATCH at best, briefly noted.

- **A 06-23 arxiv-digest CF paper** (Murali et al., already mentioned)
  is the cleanest "HIGH" arxiv-digest hit of the window. Other digest
  papers in 06-16 → 06-19 (Zitnik biological FM, FM-on-pathology, UK
  Biobank measurement noise, bioETH-Beacon PGS-catalog query) are
  methodologically interesting but tangential. Brief notes at the end.

---

## Per-study detailed reports

### 1. HIGH — Baya, Lassen, Hill, Venkatesh, Currant et al. — *Individuals who deviate from polygenic expectation are enriched for damaging variants in genes linked to rare disease* (AJHG, 2026)

**Source:** Google Scholar — *Chenjie Zeng — new related research* (06-27)
**Cross-feed:** Lisa Bastarache — new related research (06-27)
**Venue:** American Journal of Human Genetics, 2026
**Link:** https://www.cell.com/ajhg/fulltext/S0002-9297(26)00200-4

**Why this is HIGH.** Two of your active threads — **Genetic
epidemiology** (composite risk models stacking PRS with rare pathogenic
variants) and **Rare disease / Variant interpretation** (penetrance
under population screening vs. clinically ascertained cohorts) — meet
exactly in the framing of this paper. The setup is: take the residual
between observed phenotype and PRS-predicted phenotype ("polygenic
deviation"); ask whether individuals in the tails of that residual are
enriched for damaging variants in known disease genes; report the
enrichment ratios. That is *structurally* the same question as monogenic
penetrance under population screening, except using PRS residuals as
the discovery signal instead of a phecode-defined outcome.

**Specific things to check on full read:** (a) which biobank(s) — almost
certainly UK Biobank given the author list (Lassen, Currant), but
confirm; (b) how they defined "damaging" (LOFTEE-HC pLoF vs. missense
constraint?); (c) whether the enrichment direction is symmetric (tails
on both sides enriched) or asymmetric (only the "deviates-toward-disease"
tail) — the latter would be the more biologically clean signal; (d)
whether they make any claim about penetrance estimates derivable from
the deviation framework, vs. just enrichment.

**Action.** Read end-to-end. The mechanism (PRS residual → rare-variant
prioritization) is directly portable to your composite-risk and
penetrance work, and the fact that this surfaces in your own self-feed
means there is a citation/reference linkage worth understanding for
positioning your own next manuscript.

---

### 2. HIGH — Welland, Ahlquist, De Fazio, Austin-Tse et al. — *Automated reanalysis of genomic data for rare disease diagnostics at scale* (Nature Medicine, 2026)

**Source:** Google Scholar — *rare diseases — new results* (06-28)
**Venue:** Nature Medicine, 2026
**Link:** https://www.nature.com/articles/s41591-026-04477-5

**Tool/framework name:** Talos (from the snippet).

**Why this is HIGH.** Hits **Variant interpretation (ACMG/ClinGen)** and
**Rare disease** simultaneously, and lands on the specific pain-point
that VCEPs and the ACMG-AMP guidance have been circling for years:
how do you do iterative reanalysis at population scale when ClinVar,
gnomAD, and gene-disease evidence are updating monthly? The snippet
says they fuse **disease- and variant-level evidence with
inheritance-aware filtering**, validated on **1,089 individuals with
rare disease**, then deployed for **iterative reanalysis in an
unselected cohort**. That last clause — "unselected cohort" — is the
biobank-screening framing, and is the bridge between ascertained
rare-disease diagnostics and population-screening penetrance work.

**Specific things to check on full read:** (a) the size of the
"unselected cohort" (the snippet doesn't say — likely a Broad biobank
contribution, possibly AoU or 100K Genomes); (b) reanalysis yield —
how many additional diagnoses per cycle; (c) the inheritance-aware
filtering rules — whether they handle X-linked, de novo, and
compound-het cleanly; (d) whether Talos generates ClinGen-VCEP-style
structured outputs (so it can feed into curation pipelines) or just
candidate-variant lists.

**Action.** Read end-to-end. Specifically compare Talos's evidence
fusion to **InterVar** and **AnFiSA**-style DSLs (which are in your
INTERESTS as variant-curation tooling). If Talos's framework can serve
as the iterative-reanalysis backbone for a biobank-scale ascertainment
study, that's a meaningful collaboration target.

---

### 3. HIGH (citation context) — Gorevic, Niewold, Aksentijevich, Pfeffer et al. — *Challenging traditional classifications: Gene penetrance in genetically transitional disease* (Genes & Diseases, 2026)

**Source:** Google Scholar — *"Guidance for estimating penetrance of monogenic …" — new citations* (06-28); cross-feed in *mendelian diseases — new results* (06-28)
**Venue:** Genes & Diseases, 2026
**Link (from snippet):** https://www.cell.com/ajhg/... (HTML rendered in scholar alert; the actual venue link wasn't fully resolved in the alert HTML — verify on Scholar)

**Why this is HIGH.** This is a *direct citation* to your penetrance
guidance paper. The framing — "genetically transitional disease" — is
the conceptual middle ground between fully Mendelian and fully complex
disease, and the snippet says they want to *challenge the traditional
classifications*, which usually means arguing that fixed-penetrance
labels don't fit autoinflammatory / autoimmune-overlap conditions
(Niewold and Aksentijevich are both autoimmune-genetics people; Gorevic
is amyloidosis/MEFV). Daniel Kastner's name is conspicuously absent —
worth checking if he's a coauthor in the full version.

**Specific things to check on full read:** (a) does the paper cite your
guidance specifically for the **calibration-aware vs. condition-aware
penetrance estimation** point, or for the **ascertainment-correction**
point — these have different downstream implications; (b) which
specific conditions they use as "transitional" exemplars (likely TRAPS,
FMF, hyper-IgD — autoinflammatory with reduced penetrance and modifier
loci); (c) whether they propose a quantitative reframing or only
critique the binary classification.

**Action.** Skim the citing section first; the rest can wait. If the
citation is in the introduction setting up the problem, that's a
positioning/framing reference and worth thanking on the next round; if
it's in the discussion as a contrast (i.e., "Zeng et al. argue X, but
we show…"), it's an active methodological debate worth engaging in.

---

### 4. HIGH — Souaiaia, Wu, Ori, Choi, Hoggart et al. — *Distinct genetic architecture in the tails of complex traits* (Nature, 2026)

**Source:** Google Scholar — *Stephen B Montgomery — new related research* (06-27)
**Venue:** Nature, 2026

**Why this is HIGH.** Composite-risk and PRS-tail work is in your
**Genetic epidemiology** thread. The claim — that the genetic
architecture of the *tails* of complex traits differs from the bulk
(more rare-variant contribution, larger effect sizes, departure from
infinitesimal-model heritability) — is methodologically important for
**any extreme-quantile PRS work** and for the question of when a
PRS tail justifies follow-up rare-variant sequencing.

**Specific things to check on full read:** (a) which traits they used
as exemplars and at what tail thresholds (top 0.1%? top 1%?); (b)
whether they estimate the rare-variant contribution to tail heritability
explicitly, and via what method (BOLT-REML extension? saddlepoint?);
(c) whether the tail-enrichment story is consistent across ancestries —
this is critical for portability and for the cross-ancestry PRS thread.

**Action.** Read sections on methods and tail-heritability estimation.
This is directly relevant to *both* the composite-risk-model framing
and the case-for-stacking-PRS-with-rare-variants framing. If the
sample size in the tail is large enough that they can do gene-set
enrichment, that's a citable result for the deviation work in #1.

---

### 5. HIGH — Ma, Fong, Lai, Wu, Hue, Ying, Chen et al. — *AI-CURA, an automated LLM workflow for high-accuracy genetic variant classification* (Science Translational Medicine, 2026)

**Source:** Google Scholar — *"variant interpretation" OR "variant classification" OR "Causal Variant" — new results* (06-28)
**Venue:** Science Translational Medicine, 2026
**Link:** https://www.science.org/doi/abs/10.1126/scitranslmed.adz4172

**Why this is HIGH.** The variant-interpretation thread explicitly calls
out InterVar/AnFiSA-style DSLs and LLM-assisted curation. AI-CURA is
the highest-profile LLM-for-ACMG-AMP paper to hit a top-tier translational
venue this year. STM peer review is rigorous enough that the
"high-accuracy" claim in the title has been forced through external
validation. Hong Kong group (the author pattern — Hue, Ying, Chen — is
consistent with HKU/CUHK), which is a different evidence base than
the Broad-centric Talos work in #2; worth comparing head-to-head.

**Specific things to check on full read:** (a) what's the benchmark
truth set — ClinVar consensus 3-star, or curated VCEP outputs, or a
held-out expert panel? Each gives a very different "accuracy" number;
(b) does it call ACMG criteria *individually* (PVS1, PM2, PP3 …) and
then aggregate, or does it directly call Pathogenic/Likely
Pathogenic/VUS/Likely Benign/Benign? The first is the InterVar style and
is more auditable; (c) failure mode breakdown — for VUS resolution
specifically, does it lean PP3-heavy (computational evidence) or does
it generate splicing/RNA-evidence arguments (which is your
splicing-evidence interest)?

**Action.** Read the methods and benchmark sections in full. This is
the kind of paper that you'd cite in any ClinGen-VCEP-tooling proposal,
and it likely defines the new bar for what "automated ACMG" means in
2026.

---

### 6. HIGH — Murali, Barnatchez, Hoppe, Wagner, Keller, Josey — *Causal Inference with Multiple Misclassified Exposures: A Control Variate-Adjusted Calibration Weighting Approach* (stat.ME, 2026-06-22)

**Source:** `arxiv-digest` repo, `digests/2026-06-23.md` (keyword hits: `causal inference`, `cystic fibrosis`; score=2)
**arXiv:** 2606.23656v1

**Why this is HIGH.** This is the single cleanest "two-thread-overlap"
hit in arxiv-digest this window. Methods thread = **Causal inference
and pharmacoepidemiology** (calibration weighting, control variates,
double-robustness). Disease thread = **Cystic fibrosis / CFTR** (the
worked example is a 651-patient CF cohort age 6–21, comparing
throat-swab vs. sputum-culture exposure measurement for *P. aeruginosa*
and *S. aureus*).

**The headline finding.** Swab-based estimates *attenuate the causal
effect of P. aeruginosa on percent-predicted FEV₁ by approximately 69%*
relative to sputum-based estimates (−2.67 vs −8.52 percentage points;
95% CI for sputum −13.40 to −3.63). That is enormous. It implies that
much of the existing CF observational literature on swab-derived
exposures is materially underestimating treatment-deserving effect
sizes. Authors explicitly note the policy implication: "relying on
throat swabs may lead to *under-treatment* of P. aeruginosa
infections."

**Methodological core.** Calibration weighting treats misclassification
as a missing-data problem and is consistent without modeling the
misclassification mechanism — i.e., you don't need to know
sensitivity/specificity, just need a small validation subset. Control
variate adjustment uses error-prone observations to *reduce variance*
of the gold-standard estimator without breaking consistency. The
estimator is **double robust** (inherits the property from its
component estimators). They also derive a structural ceiling on
efficiency gains in the bivariate misclassified-exposure case, which
is a useful negative result.

**Action.** Read in full. Two reasons: (a) the framework is portable
to any EHR-based study where the exposure is a phecode or
medication-derived flag with known imperfect sensitivity/specificity
(this is most of your AoU / MVP / BioVU pharmacoepi work); (b) the CF
substantive finding is directly relevant to the modulator-pharmacoepi
thread — if swab-based exposure attenuates causal effects by ~70% in
CF infections work, the same logic likely applies to swab-based
microbiology in modulator-effectiveness studies.

---

### 7. METHODS-WATCH — K. Zheng — *Cohort-Anchored Foundation Models for Electronic Health Records: From Risk Scores to Auditable Peer Cohorts* (arXiv 2606.21885, 2026)

**Source:** Google Scholar — *Foundation models and "electronic health records" — new results* (06-28)
**arXiv:** 2606.21885

**Why METHODS-WATCH.** EHR foundation-model thread (CLMBR/MOTOR/EHRSHOT/
MedTok/FEMR lineage in your INTERESTS). The pitch is **cafm** — a
Cohort-Anchored FM framework that "elevates" risk scores into
"auditable peer cohorts," with human-in-the-loop refinement that
translates model behaviour into auditable cohort summaries. That last
bit — turning model outputs into *peer cohort* summaries rather than
opaque risk scores — is the same fairness/calibration audit framing
that your INTERESTS list flags.

**Caveat.** Single-author arXiv preprint from a non-headline group; no
peer review yet. The framing is intellectually adjacent to MOTOR /
EHRSHOT but doesn't (from the snippet) appear to fine-tune or compare
against them. Treat as a framing reference, not a methods baseline,
until peer review.

**Action.** Skim sections on the "peer cohort" definition and the
audit mechanism. If the peer-cohort framing turns out to be a clean
calibration-by-subgroup formulation, it's worth citing as a possible
audit tool for any EHR-FM-based downstream prediction.

---

### 8. METHODS-WATCH — Guo, Yan, Vettese, Sung — *PORTER: Language-Grounded Event Representations for Portable Structured EHR Foundation Models* (arXiv 2606.24102, 2026)

**Source:** Google Scholar — *Foundation models and "electronic health records" — new results* (06-28)
**arXiv:** 2606.24102

**Why METHODS-WATCH.** Argues that most EHR FMs encode clinical events
as *discrete tokens* tied to a specific vocabulary (ICD vs SNOMED vs
phecode), which kills portability across institutions. PORTER decouples
the event representation from the vocabulary by grounding events in
language descriptions, with the explicit claim that this makes the FM
**portable** across sites.

**Why it matters.** This is exactly the portability problem your
**EHR phenotyping & OMOP** thread is sensitive to — if the EHR FM is
locked to one site's coding habits, it can't transport to AoU / MVP /
BioVU / VUMC without retraining. PORTER's portability claim, if it
holds up, is a meaningful step.

**Caveat.** Sung group has been credible in pediatric EHR-ML;
this is preprint-only and the benchmarks are likely limited.

**Action.** Skim methods (event encoding + grounding step) and the
portability evaluation section. If they report cross-site transfer
that beats CLMBR/FEMR baselines, this is citable for any FM-portability
discussion.

---

### 9. METHODS-WATCH — Kolosov, Reeve, Briotta Parolo, Kurki et al. — *PGS Browser: a public platform for personalized polygenic score analysis and interpretation* (Nature Communications, 2026)

**Source:** Google Scholar — *Chenjie Zeng — new related research* (06-27)
**Venue:** Nature Communications, 2026

**Why METHODS-WATCH.** PRS/PGS infrastructure paper. The angle they
emphasize — *population-based reference resources* for clinical
translation — is the right framing, and is the same problem your
INTERESTS list calls out under "calibration, ancestry-aware risk
scores." Surfaces in your self-feed so there's probably a citation
linkage.

**Action.** Bookmark the platform. If it provides ancestry-stratified
reference distributions for arbitrary PGS Catalog entries, it could
become the standard substrate for the calibration work. Worth a
~20-minute skim of the methods to see how they handle
ancestry-portability.

---

### 10. METHODS-WATCH — Tarhini, Khaksar, Chen, Lee, Hodi, Li et al. — *Predicting immune-related thyroiditis using polygenic risk scores in patients with advanced melanoma* (J ImmunoTherapy Cancer, 2026)

**Source:** Google Scholar — *Chenjie Zeng — new related research* (06-27)
**Venue:** Journal for ImmunoTherapy of Cancer, 2026

**Why METHODS-WATCH.** Disease scope (melanoma + ICI toxicity) is off
your active threads, but the *design* — using PRS to predict an irAE
in a treatment-defined cohort — is the cleanest example of
"PRS-as-pharmacoepi-instrument" that has hit a clinical journal this
window. Could be a useful citation for any project that uses PRS to
risk-stratify a treatment-receiving subpopulation. Surfaces in your
self-feed, so a methodological citation/positioning linkage exists.

**Action.** Read the abstract and Methods for the PRS construction
(probably leveraging the autoimmune-thyroid GWAS lead variants — your
**autoimmune disease** thread overlap is here). Skip the clinical
discussion unless you're staffing the irAE direction.

---

### 11. HIGH (overlaps two threads) — Patterson, Minto, Beaton et al. — *FHIR–OMOP data within the All of Us Research Program* (06-28 keyword feed)

**Source:** Google Scholar — *"All of Us research program" — new results* (06-28)

**Why HIGH.** Two-thread hit: **Biobanks with EHR linkage: All of Us**
and **EHR phenotyping & OMOP**. The exact question of how AoU's
FHIR-derived clinical data maps onto the OMOP-CDM (which is the data
substrate AoU now exposes for cohort builds) is foundational to *any*
methods paper using AoU EHR data — and the snippet suggests they're
quantifying or characterizing this mapping rather than just using it.

**Specific things to check on full read:** (a) is this a *consistency*
paper (FHIR ⇄ OMOP round-trip) or an *enrichment* paper (FHIR adds
something OMOP doesn't capture, or vice versa)? Either matters; (b)
which OMOP vocab versions and which AoU data release; (c) any worked
phenotype example that shows the mapping difference materially —
e.g., a phecode/condition occurrence count delta.

**Action.** Read carefully if you have any AoU-based study in
flight — this is the kind of paper that gets cited as the
foundational methods reference for AoU + OMOP work.

---

### 12. METHODS-WATCH — Fesser, Zhang, M. Li, Wang, Perozzi, Azizi, Kakade, Zitnik — *How Post-Training Shapes Biological Reasoning Models* (cs.LG, arXiv 2606.16517, 2026)

**Source:** `arxiv-digest` repo, `digests/2026-06-16.md` (keyword hit: `foundation model`; score=1)
**arXiv:** 2606.16517

**Why METHODS-WATCH.** Trains and evaluates 100+ biological reasoning
models under controlled variation across continued pre-training,
supervised fine-tuning, and RL. The finding that **SFT increases
in-domain performance but OOD performance peaks early and declines** is
the kind of empirical generalization-vs-overfit lesson that should
inform any *EHR-FM fine-tuning* you do (your INTERESTS thread).
Although this paper is about biology FMs (DNA/RNA/proteins) rather
than EHR FMs, the post-training-stage analysis is highly portable.

**Action.** Skim the SFT vs RL section. Citable in any
foundation-model fine-tuning discussion.

---

### 13. METHODS-WATCH — Schulz, Ritter — *Measurement noise limits the advantage of nonlinear models over linear models in biomedical prediction* (cs.LG, arXiv 2606.18420, 2026)

**Source:** `arxiv-digest` repo, `digests/2026-06-18.md` (keyword hits: `uk biobank`, `biobank`; score=2)
**arXiv:** 2606.18420

**Why METHODS-WATCH.** The "linear baseline matches deep model on
tabular EHR/biobank data" finding is well known; this paper gives it a
formal measurement-error explanation. The clean part: a degree-k
interaction is attenuated by the k-th power of feature reliability,
while the linear part is attenuated only once. Across **140 UK
Biobank tasks**, the gap between flexible and linear models — where it
exists at all — carries the predicted noise signature. The conclusion
("nonlinearity is hidden, not absent") is a useful framing for any
ML-on-biobank work where the reviewer asks "why didn't you try a
gradient-boosted model?"

**Action.** Save for the next time you write up an EHR-tabular ML
result and need a clean defense of why linear/regularized baselines
are sufficient. The 140-task UKB ablation is the citable evidence.

---

### 14. METHODS-WATCH — Hu, Tripodi, Naidoo, McGough, Chakraborti — *Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis* (cs.LG, arXiv 2606.17115, 2026)

**Source:** `arxiv-digest` repo, `digests/2026-06-17.md` (keyword hit: `foundation model`; score=1)
**arXiv:** 2606.17115

**Why METHODS-WATCH.** Multimodal FM (whole-slide image + transcriptomic
profile) benchmark across 5 FMs, 8 downstream classification tasks,
two real-world commercial oncology cohorts. The findings that **(a)
image and omics representations carry complementary signals**, **(b)
multimodal fusion helps mainly when no single modality dominates**,
and **(c) conformal prediction sets recover the true diagnosis even
when point predictions fail** are all directly portable to EHR-FM
multimodal work in your INTERESTS list (notes + codes + waveforms +
imaging).

**Action.** Skim the conformal-prediction section — useful citation
for any uncertainty-aware EHR-FM discussion.

---

### 15. METHODS-WATCH — Galanopoulos, Provatas, Georgakopoulos-Soares — *bioETH-Beacon: A Confidential On-Chain Genomic Beacon with Encrypted Counts, Filters, and Bounded Noise over a Fully Homomorphic EVM* (q-bio.GN, arXiv 2606.20315, 2026)

**Source:** `arxiv-digest` repo, `digests/2026-06-19.md` (keyword hits: `polygenic score`, `polygenic`; score=2)
**arXiv:** 2606.20315

**Why METHODS-WATCH.** Tangential to active threads, but worth noting:
the synthetic panels they use are derived from the **PGS Catalog**, so
this is technically a "PGS data infrastructure" paper, not a
substantive PRS paper. The privacy framing (GA4GH Beacon + FHE) is
genuinely novel, but unless you're staffing a federated-PRS direction
it can wait.

**Action.** Skip unless you're spinning up privacy-preserving biobank
collaboration.

---

## Briefly noted (low priority / SKIP)

- **Caradonna et al. — *Clonal Hematopoiesis and Gut Microbiota-Derived
  TMAO as Candidate Amplifiers of Cardiovascular Inflammation: The
  CHIDT Hypothesis* (Antioxidants, 2026).** Keyword feed
  `intitle:"clonal hematopoiesis"` (06-28). Hypothesis-generating
  review, not data. SKIP for your CHIP/VEXAS active thread (which is
  data-focused).
- **Bankole et al. — *Expression of APOL1 and NOTCH2 genes in patients
  with type 2 diabetes mellitus attending Babcock University Teaching
  Hospital, Ogun State, Nigeria* (PDF only, 2026).** APOL1 keyword
  feed (06-28). Small single-center observational; SKIP.
- **Basirpour et al. — *Emerging Cardioprotective Strategies Beyond
  Dexrazoxane: SGLT2 Inhibitors, Drug Repurposing, and Mitochondrial
  Approaches in Doxorubicin Cardiotoxicity* (2026).** Drug
  repurposing keyword feed (06-28). Pharmacology review; doesn't have
  the explainable-hypothesis / KG-GNN / EHR-signal angles you flagged
  for the drug-repurposing thread. SKIP.
- **arxiv-digest 06-26: KG-TRACE (neuro-symbolic AMR prediction).**
  KG keyword hit but the disease scope is M. tuberculosis AMR
  prediction, which is outside your active threads. METHODS-WATCH at
  best (the WHO mutation KG + RotatE embeddings + "Biological
  Grounding Ratio" metric is the kind of explainable-KG framing you
  flagged for drug repurposing, but applied to a different problem).
- **arxiv-digest 06-25: Tabular FM robustness on microbiome data
  (Perciballi et al.) and federated tensor decomposition of single-cell
  immune data (Faes et al.).** Both methodologically clean but
  disease/data scope is off-thread. SKIP for triage purposes.
- **arxiv-digest 06-11: m6A-FORM (RNA methylation FM), Bayesian Causal
  Machine Learning for Cure Models (Linero et al.), OmniBioTwin (GLP-1
  digital twin framework).** The BCML cure model paper is interesting
  but not directly actionable (CALGB-40101 breast cancer trial worked
  example). OmniBioTwin hits the `glp-1` keyword but is an
  *architecture-paper* rather than a substantive GLP-1 pharmacoepi
  study; SKIP for the active drug-class thread.
- **arxiv-digest 06-09: Embedding-geometry critique of biomedical LMs
  (Biswas et al.) — score=2 on `foundation model` + `knowledge graph`.**
  Adjacent to your KG thread but the framing is "Large Behavioural
  Model over a graph of a user's life," which doesn't quite map to the
  biomedical-KG-for-clinical-reasoning angle. SKIP for now.

---

## Notes on pipeline health

- **arxiv-digest produced near-empty days on 06-13, 06-14, 06-15,
  06-20, 06-21, 06-22, 06-24, 06-27, 06-28.** Some of these are
  genuinely low-volume weekend days (q-bio.QM / q-bio.GN routinely have
  low Friday-night and Saturday submissions for arXiv listing-day
  purposes), but the cluster of empty days around 06-13/-14/-15 and
  again 06-20/-21/-22 deserves a check — possibly arXiv rate-limiting
  recurrence or a category-fetch failure. Worth grep'ing the GitHub
  Actions log for `429` in those date ranges.
- **The Scholar-alert volume is healthy** — 06-27 and 06-28 each
  delivered 10+ author-feed batches and 10+ keyword-feed batches. Author
  feeds with the most signal this window: Bastarache (4 alerts),
  Montgomery (2 alerts including a Nature paper), Pritchard, Szolovits,
  Patrick Ryan, Chenjie Zeng self-feed.

---

## Suggested next actions

1. **Read in full:** Baya et al. (#1), Welland/Talos (#2), Murali et al. CF causal-inference (#6), AI-CURA (#5).
2. **Skim citing context:** Gorevic et al. (#3) — your penetrance citation context.
3. **Skim methods sections:** Souaiaia et al. (Nature) (#4), PGS Browser (#9), Patterson et al. AoU FHIR/OMOP (#11).
4. **Bookmark for later:** PORTER (#8), cafm (#7), Schulz–Ritter (#13), Hu et al. multimodal FM (#14).
5. **Pipeline health:** check Actions logs for 06-13/-14/-15 and 06-20/-21/-22 to confirm whether the empty days were genuine zero-relevant days or fetch failures.
