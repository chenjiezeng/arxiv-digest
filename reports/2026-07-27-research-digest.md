# Research digest report — 2026-07-27

Triage of research-related email + the GitHub `arxiv-digest` against the
active threads in `INTERESTS.md` (PheWAS/phecodes, EHR-linked biobanks,
EHR phenotyping/OMOP, causal inference & pharmacoepi, variant
interpretation, genetic epi, CF/APOL1/CHIP-VEXAS/IBD disease threads,
EHR foundation models, KGs/ontologies, drug repurposing, rare disease,
ML for precision health, multimorbidity).

Window: **2026-07-23 12:00Z → 2026-07-27 03:00Z** (roughly the 3½ days
since the last committed report at
`reports/2026-07-23-research-digest.md`). Covers a full Friday +
weekend + early Monday of Scholar / NCBI / bioRxiv/medRxiv alert
traffic and four `arxiv-digest` cron runs (07-24 through 07-27, three
of them near-empty).

## Sources scanned

| Source | Window | Notes |
| --- | --- | --- |
| Google Scholar alerts (author-feeds) | 07-24 09:02Z, 07-26 05:17Z | Two major author-feed batches. 07-24 fires **Karczewski, Ryan, Hernán, Denny, Bastarache, Pritchard, Xu, Chute, Hripcsak, Pascal Brandt, Zitnik, Callahan, Yang, Kastner, Luo, Szolovits, Natarajan, Baker, Shendure**. 07-26 fires the same cluster plus **Chenjie Zeng (self), Wendy Chung, Muin Khoury, Evan Eichler, Liwei Wang**. Highest-signal single hit: the *Silver labels for EHR computable phenotyping* preprint surfacing in **three separate feeds** (Ryan + Brandt + Hripcsak). |
| Google Scholar alerts (keyword feeds) | 07-25 03:27Z, 07-26 11:32Z | Two keyword-feed batches. Keywords fired: `electronic health records`, `APOL1`, `variant interpretation OR variant classification`, `UK Biobank`, `phenome wide association studies`, `knowledge graph`, `All of Us research program`, `Foundation models and "electronic health records"`, `drug repurposing`, `mendelian diseases`, `autoimmune disorders / diseases`, `rare diseases`, `"Guidance for estimating penetrance of monogenic ..."` (self-citation feed). |
| NCBI "My NCBI What's New" (AoU, UK Biobank, drug repurposing) | 07-26 12:42Z | Three NCBI batches — AoU, UKB, and drug-repurposing. |
| bioRxiv / medRxiv Subject Collection Alerts | 07-27 00:01Z, 00:05Z | Aggregate feeds — individual papers surfaced upstream via Scholar / NCBI. Not a separate net. |
| `arxiv-digest` repo (`digests/`) | 2026-07-24 → 07-26 | **3 daily files scanned; 1 non-empty.** 07-24 = 1 paper (single-cell FM contamination audit). 07-25 = 0 papers ("no matches in lookback window"). 07-26 = 0 papers. Continuing thin catches — see suggestions section. |

> Caveat: Scholar / NCBI emails contain title, authors, venue, and the
> first ~2–3 lines of each abstract only. The reports below contextualize
> that metadata against your research threads; nothing here reflects
> full-text reading. `arxiv-digest` entries include the full abstract
> because the pipeline captures it.

> ⚠️ **`arxiv-digest` cron output remained thin this window** — one
> non-empty day out of three, and the non-empty day surfaced a
> single-keyword score-1 paper. As noted in the 06-13, 07-16, 07-18,
> 07-21, 07-22, and 07-23 reports, 80%+ of on-thread signal continues to
> arrive via Scholar / NCBI / journal alerts outside arXiv q-bio /
> stat.AP. Recommendation repeated: add `cs.LG`, `stat.ME`, and a
> medRxiv/bioRxiv feed.

---

## Executive summary

- **Silver-labels-for-computable-phenotyping is the strongest single
  signal this window — triple-feed saturation.** S. Wang, M.T.
  Slaughter, J.C. Nelson, B.D. Williamson, *Using binary silver labels
  in electronic health records-based computable phenotyping algorithms*
  (arXiv 2607.18431, 2026). Surfaced simultaneously in **three
  independent author feeds** (Patrick Ryan + Pascal Brandt + George
  Hripcsak) — the strongest saturation signal of the window.
  Semi-supervised phenotyping with binary "silver" labels is exactly
  the AoU / OHDSI-style computable-phenotype problem where the
  gold-label bottleneck (chart review) is the practical blocker.
  **HIGH — read first.**
- **PRS × drug-response — Nongoal statin response.** L. Liou, J.
  García-González, H.M. Wu, S. Namba, F. Vaura et al., *Polygenic
  Prediction of Nongoal Response to Statin Therapy* (*Circulation:
  Genomic and Precision Medicine*, 2026; Bastarache related-research
  feed 07-24). Direct PRS-for-drug-response study — sits at the
  intersection of your PRS thread and your pharmacoepi thread, and
  extends the Fritsche ICI-thyroiditis PRS-for-drug-toxicity pattern
  from the 06-13 report to a lipid drug class. **HIGH.**
- **Blended genome + exome sequencing (Nat Genet).** T.A. Boltz, B.B.
  Chu, M. DeFelice, C. Liao, J.M. Sealock et al., *A blended genome
  and exome sequencing method captures genetic variation in an
  unbiased and cost-effective manner* (*Nature Genetics*, 2026;
  Karczewski related-research feed 07-24). Cost-effective WGS+WES
  hybrid — potentially a new default sequencing strategy for
  biobank-scale rare-variant work; Sealock on the author list points
  to a Vanderbilt / BioVU connection. **HIGH.**
- **Two clean pharmacoepi TTEs in the same window.** (a) E.J. Cannon,
  W. Wang, F.L. Norby, R.F. Walker et al., *Semaglutide vs. liraglutide
  and incidence of diabetes and cardiovascular disease: A target trial
  emulation using real-world data* (*Br J Clin Pharmacol*, 2026;
  Hernán feed 07-24) — GLP-1 head-to-head. (b) F.S. Yen, S.I. Wang,
  C.M. Hwu, K.Y. Chen, C.C. Hsu et al., *Comparative Risk of Psoriatic
  Arthritis in Type 2 Diabetes: An Emulated Target Trial of SGLT2
  Inhibitors vs. GLP-1 Receptor Agonists* (*Drug Design, Development
  and Therapy*, 2026; Patrick Ryan feed 07-24) — active-comparator
  SGLT2i vs GLP-1 RA TTE. Both drug classes are on your active
  pharmacoepi list; the second is an unusual off-target autoimmune
  outcome. **HIGH ×2.**
- **APOL1 precision therapy — Annual Review of Medicine.** T. Hopper,
  B. Wang, O.A. Olabisi, *APOL1-Mediated Kidney Disease and the
  Emerging Era of Precision Therapy* (*Annu Rev Med*, 2026; APOL1
  keyword feed 07-25). Reference-tier review from Olabisi (Duke,
  leading APOL1 clinical-genetics group) — will be the default APOL1
  precision-therapy citation for the next several years. Pairs with
  the JCI Pell et al. paper (recipient-side APOL1 in transplant
  rejection) from the 06-13 report. **HIGH.**
- **Low-dose methotrexate against incident psychosis in an EHR
  retrospective cohort.** F. Corsi-Zuelli, M. Taquet, B. Deakin, R.
  [Upthegrove?] et al., *Potential preventive role of low-dose
  methotrexate against incident recorded psychosis: a retrospective
  cohort study based on electronic health records* (2026; EHR keyword
  feed 07-26). Taquet (Oxford EHR pharmacoepi) on the author list —
  precisely the shape of an EHR-derived drug-repurposing signal your
  drug-repurposing thread was reoriented toward in April 2026. **HIGH.**
- **PrimeKG-Plus — literature-derived expansion of a multimodal
  precision-medicine KG.** T.T.D. Nguyen, T. Nguyen-Phuong, Q.H.
  Nguyen et al., *PrimeKG-Plus: a literature-derived expansion of a
  multimodal precision medicine knowledge graph* (*bioRxiv*, 2026;
  Marinka Zitnik + Tiffany Callahan feeds 07-26 — double-feed).
  Extension of the PrimeKG multimodal precision-medicine KG (Zitnik
  lab) with literature-derived facts — squarely on your KG /
  drug-repurposing intersection thread. **HIGH.**
- **MR methods — Instrument borrowing from auxiliary outcome traits.**
  A. Chattopadhyay, N. Chatterjee, *Improving Mendelian Randomization
  Analysis by Instrument Borrowing from Auxiliary Outcome Traits*
  (arXiv 2607.16086; Pritchard citation feed 07-24). Chatterjee at
  Johns Hopkins is one of the leading MR / statistical-genetics
  methodologists. Pairs with the MR-ALasso paper (Qasim et al., stat.ME
  07-22, previously reported) as the second MR-methods paper in two
  weeks that changes instrument-selection defaults. **HIGH (methods).**
- **AoU-based genomic healthcare disparities cross-section, and
  S4-Multi multi-ancestry PRS protocol.** M.D. Johnson et al.,
  *Healthcare experiences and the cycle of genomic healthcare
  disparities: A cross-sectional study utilizing the 'All of Us'
  research program* (surfaced again 07-26 in Denny related-research +
  AoU keyword feeds — confirming last week's Denny-feed hit); and
  P.H. Lai, J.P. Tyrer et al., *Protocol for constructing multi-ancestry
  polygenic models using S4-Multi* (*STAR Protocols*, 2026; Denny
  related-research feed 07-24). The Johnson paper is a re-confirmation
  from last window; S4-Multi is a fresh multi-ancestry PRS protocol
  usable in AoU. **HIGH (Lai/S4-Multi); MEDIUM-HIGH re-confirmation
  (Johnson).**
- **`arxiv-digest` contribution — scFM benchmark contamination
  audit.** Sarwan Ali, *Auditing pretraining contamination in
  single-cell foundation model benchmarks* (arXiv 2607.20572,
  q-bio.GN; digest 07-24, second contamination-audit paper in as many
  days from the same author). Off your clinical/EHR thread, but the
  MinHash-fingerprint + loss-based membership-inference-attack framework
  is directly portable to EHR-FM contamination auditing (CLMBR /
  MOTOR / FEMR / MEDS pretraining on datasets that overlap the
  downstream evaluation cohorts). **METHODS-WATCH — worth reading if
  you audit an EHR-FM.**

Everything else in the window is either off-thread (Bombus population
genomics, protein nanoparticle design, single-cell integration
methods, dietary-index → outcome UKB papers), a routine methods-only
reference, or a duplicate of an item already reported. See the tail
sections.

Counts: **9 HIGH**, **6 METHODS-WATCH**, rest SKIP.

---

## HIGH priority — detailed reports

### 1. Using binary silver labels in electronic health records-based computable phenotyping algorithms

**Authors.** S. Wang, M.T. Slaughter, J.C. Nelson, B.D. Williamson.
**Venue.** arXiv 2607.18431, 2026.
**Signal source.** **Triple-feed saturation** — Google Scholar author
feeds for Patrick Ryan (OHDSI, Janssen R&D), Pascal Brandt (BioVU /
Vanderbilt informatics), and George Hripcsak (Columbia OHDSI /
biomedical informatics) all surface this paper in the 07-26 05:17Z
alert batch.
**Bucket.** HIGH.
**Threads served.** EHR phenotyping & OMOP (computable phenotype
development); ML for precision health (semi-supervised phenotype
labelling); PheWAS/PheRS (any phecode-adjacent phenotype problem).

**What the paper does (from snippet).** "Gold-standard" chart-review
labels for computable-phenotype algorithm development are expensive
and slow to acquire. The paper studies the use of *binary silver
labels* — high-throughput, imperfect proxy labels derived from EHR
rules or single algorithms — as a substitute or complement to
gold-standard labels for training and evaluating computable
phenotyping algorithms. Positioned as a methodological contribution
to the semi-supervised / weakly-supervised phenotyping literature.

**Why it matters for your work.**
1. **The gold-label bottleneck is the current binding constraint on
   AoU / OHDSI phenotyping.** Every serious phecode / phenotype
   algorithm eventually runs into the "we need chart-reviewed cases
   to validate" wall. Silver-label methodology directly attacks that
   bottleneck.
2. **Triple-feed saturation is a strong signal.** The paper hit
   Ryan (Janssen OHDSI), Brandt (Vanderbilt BioVU), and Hripcsak
   (Columbia OHDSI) simultaneously — three of the highest-authority
   EHR-phenotyping author feeds. That kind of co-fire almost always
   indicates a paper that will be widely cited within the
   OHDSI / N3C / AoU ecosystem within a year.
3. **Directly composable with your existing pipelines.** Anywhere
   you're building an AoU phenotype algorithm and using an
   existing PheKB / PheValuator / KOMAP silver-standard label as
   the ground truth, this paper likely provides better statistical
   guarantees on the resulting algorithm's operating characteristics.
   Pairs with the PheValuator / KOMAP work you already track in the
   `ehr-phenotyping-os` skill.

**Follow-ups.** Pull the paper; check (a) the silver-label
noise-model assumptions (do they require class-conditional or
instance-conditional noise models?), (b) whether they benchmark
against PheValuator / KOMAP directly, (c) what phenotype(s) they
evaluate on, (d) any released R / Python package. The Nelson /
Williamson at Kaiser Permanente / Fred Hutch axis is worth
noting — they've historically written the most careful phenotyping
methods papers in this space.

---

### 2. Polygenic Prediction of Nongoal Response to Statin Therapy

**Authors.** L. Liou, J. García-González, H.M. Wu, S. Namba, F.
Vaura et al.
**Venue.** *Circulation: Genomic and Precision Medicine*, 2026.
**Signal source.** Google Scholar author feed for Lisa Bastarache —
new related research (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (PRS); causal inference /
pharmacoepi (statin drug class); machine learning for precision
health (drug-response prediction).

**What the paper does (from snippet).** Uses polygenic risk scores
to predict *nongoal response* to statin therapy — i.e., patients
who fail to reach LDL-C treatment targets on standard statin doses.
"Nongoal response" is a clinically meaningful pharmacogenomic
endpoint (as opposed to raw LDL-C reduction), because it maps
directly to a clinical decision (intensify statin, add ezetimibe,
add PCSK9i).

**Why it matters for your work.**
1. **Extends the PRS-for-drug-response pattern to statins.** Fritsche
   et al. (2026, *Clin Cancer Res*; flagged HIGH in the 06-13 report)
   did the same for ICI-induced thyroiditis. Together they establish
   the PRS-for-drug-response design as reproducible across drug
   classes and endpoints.
2. **Clinically actionable framing.** Your INTERESTS file specifically
   calls out ML/PRS papers that are "tied to a clinical decision (who
   to treat, who to screen, when to escalate)" as HIGH. Nongoal statin
   response is exactly such a decision — the endpoint answers "which
   patient should be escalated to a PCSK9 inhibitor?"
3. **Cross-ancestry and Namba on the author list.** Namba's presence
   suggests Biobank Japan involvement — a natural cross-ancestry
   check. Vaura (Finland, PGS / cardiovascular genetics) similarly
   suggests FinnGen involvement.

**Follow-ups.** Pull the paper; check (a) the "nongoal" operational
definition (LDL-C threshold, follow-up window, adherence
adjustment), (b) which cohorts contributed (FinnGen? Biobank
Japan? UKB?), (c) calibration and decision-curve analysis for
clinical utility, (d) discussion of statin-adherence confounding
in the phenotype.

---

### 3. A blended genome and exome sequencing method captures genetic variation in an unbiased and cost-effective manner

**Authors.** T.A. Boltz, B.B. Chu, M. DeFelice, C. Liao, J.M. Sealock
et al.
**Venue.** *Nature Genetics*, 2026.
**Signal source.** Google Scholar author feed for Konrad Karczewski —
new related research (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Genetic epidemiology (biobank-scale sequencing
infrastructure); variant interpretation (unbiased variant capture);
biobanks with EHR linkage (sequencing strategy for AoU / UKB / MVP /
BioVU).

**What the paper does (from snippet).** Introduces a method that
*blends* WGS and WES sequencing on the same samples in an unbiased,
cost-effective way — capturing the full variant spectrum of WGS
(structural variants, noncoding regulatory variants) while
maintaining the coverage-per-dollar advantage of WES for coding
regions. Sealock on the author list is the Vanderbilt genomic
medicine group (part of the BioVU / eMERGE-VUMC axis) — suggests
this is intended for real biobank deployment.

**Why it matters for your work.**
1. **May reshape biobank sequencing defaults.** The current
   sequencing-strategy debate (WES vs WGS vs blended array + WGS
   imputation) is one of the highest-cost decisions in biobank
   design. A rigorous "blended" strategy in *Nature Genetics* is
   the kind of paper that shifts the reference class for the next
   round of AoU / MVP / eMERGE-IV expansion decisions.
2. **Broad Institute + Vanderbilt author panel places this in the
   AoU / BioVU orbit.** Broad + Vanderbilt is the same axis that
   sequenced the AoU srWGS cohort — practical relevance to any
   future AoU expansion.
3. **Structural-variant capture is the interesting extra.** Your
   variant-interpretation thread cares about splicing / RNA
   evidence, LOFTEE-flagged pLoF, and SV interpretation. A method
   that recovers SVs at WES-like cost is directly on-thread.

**Follow-ups.** Pull the paper; check (a) cost per sample vs pure
WGS and pure WES, (b) SV recall benchmarked against a WGS-only
reference (e.g., 1000 Genomes long-read), (c) exon coverage depth
achieved, (d) whether the paper releases pipeline code / reference
files.

---

### 4. Semaglutide vs. liraglutide and incidence of diabetes and cardiovascular disease: A target trial emulation using real-world data

**Authors.** E.J. Cannon, W. Wang, F.L. Norby, R.F. Walker et al.
**Venue.** *British Journal of Clinical Pharmacology*, 2026.
**Signal source.** Google Scholar citation feed for Miguel Hernán —
10 new citations (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Causal inference (target trial emulation);
pharmacoepidemiology (GLP-1 RA head-to-head); biobanks with EHR
linkage (real-world data pipeline).

**What the paper does (from title).** Head-to-head target trial
emulation of semaglutide vs. liraglutide (two GLP-1 receptor
agonists) on incident diabetes and cardiovascular disease using
real-world observational EHR data. Cites Hernán — likely uses the
Hernán target-trial-emulation framework directly.

**Why it matters for your work.**
1. **GLP-1 RAs are on your active pharmacoepi drug-class list.**
   Your INTERESTS file flags GLP-1 RAs alongside SGLT2is, CFTR
   modulators, and HRT. This is a clean within-class head-to-head
   TTE — exactly the shape of drug-comparative-effectiveness
   analysis you'd run in AoU.
2. **Cites Hernán → uses Hernán TTE framework.** The paper appears
   in Hernán's *citations to* feed — likely uses the "target trial"
   protocol-emulation approach explicitly. Useful reference for the
   TTE-specification part of any AoU pharmacoepi manuscript.
3. **Extends the GLP-1 literature beyond glycemic outcomes.** Most
   GLP-1 CV literature is aggregate class-effect analysis (e.g.,
   meta-analysis of CVOTs). Semaglutide-vs-liraglutide within-class
   comparisons are much less common and more clinically actionable.

**Follow-ups.** Pull the paper; check (a) the TTE protocol
specification (index date, grace period, treatment strategies), (b)
the data source (Optum? MarketScan? EHR consortium?), (c) whether
they handle differential adherence / persistence between semaglutide
(weekly) and liraglutide (daily) — the dosing frequency is a known
confounder in this comparison, (d) subgroup analyses by BMI / A1c
strata (natural HTE subgroups given the semaglutide weight-loss
advantage).

---

### 5. Comparative Risk of Psoriatic Arthritis in Type 2 Diabetes: An Emulated Target Trial of SGLT2 Inhibitors vs. GLP-1 Receptor Agonists

**Authors.** F.S. Yen, S.I. Wang, C.M. Hwu, K.Y. Chen, C.C. Hsu et
al.
**Venue.** *Drug Design, Development and Therapy*, 2026.
**Signal source.** Google Scholar author feed for Patrick Ryan —
new related research (07-24 09:02Z).
**Bucket.** HIGH.
**Threads served.** Causal inference (target trial emulation);
pharmacoepidemiology (SGLT2i + GLP-1 RA head-to-head, active
comparator); autoimmune disease (psoriatic arthritis outcome —
adjacent to the IBD sub-thread).

**What the paper does (from title).** Active-comparator target trial
emulation of SGLT2 inhibitors vs. GLP-1 receptor agonists on
incident *psoriatic arthritis* in T2D patients. Unusual because the
outcome is autoimmune / inflammatory rather than cardiometabolic —
tests whether these drugs have differential anti-inflammatory
off-target effects.

**Why it matters for your work.**
1. **Both drug classes are on your active list.** SGLT2i and GLP-1
   RA are both on your INTERESTS pharmacoepi thread. A head-to-head
   comparison is directly relevant to any prescribing-preference
   modelling.
2. **Off-target autoimmune outcome is unusual and interesting.**
   Both drug classes have hypothesized anti-inflammatory mechanisms
   (SGLT2i via reduced cardiac inflammation, GLP-1 RA via
   GLP-1R-mediated pathways in immune cells). A rigorous
   head-to-head autoimmune outcome is a clean test of that
   hypothesis in RWD.
3. **Design template for AoU-style analyses.** Active-comparator +
   T2D restriction + TTE emulation is the current gold standard
   for pharmacoepi in claims data — worth reading the exposure /
   outcome definitions for AoU portability.

**Follow-ups.** Pull the paper; check (a) the data source (Taiwan
NHIRD is Yen's usual dataset — good scale but limited SNOMED),
(b) how psoriatic arthritis was defined (ICD-9/10 codes + rheum
visit? Dermatology + rheum joint definition?), (c) confounding-by-
indication handling given SGLT2i vs GLP-1 RA prescribing patterns,
(d) whether they subgroup by baseline BMI or A1c.

---

### 6. APOL1-Mediated Kidney Disease and the Emerging Era of Precision Therapy

**Authors.** T. Hopper, B. Wang, O.A. Olabisi.
**Venue.** *Annual Review of Medicine*, 2026.
**Signal source.** Google Scholar keyword feed — `APOL1` — new
results (07-25 03:27Z).
**Bucket.** HIGH.
**Threads served.** APOL1 (all of it — kidney disease risk,
precision therapy, transplant considerations, ancestry).

**What the paper does (from snippet).** Annual-Review-of-Medicine
review by Olabisi (Duke, one of the leading APOL1 clinical-genetics
groups) framing APOL1 as a canonical precision-therapy target. The
snippet emphasizes "APOL1 is an ideal target for precision" — likely
frames the APOL1 clinical-trial landscape (VX-147 / inaxaplin,
etc.), the risk-genotype-based screening question, and the
implications for kidney transplant decisions.

**Why it matters for your work.**
1. **Reference-tier review.** *Annual Review of Medicine* pieces
   are default first-citations for the next 3–5 years. This will
   be the go-to APOL1 precision-therapy citation for any manuscript
   or grant you write in the space through 2029-ish.
2. **Complements the recent JCI Pell et al. paper.** Pell et al.
   (JCI 2026, flagged HIGH in the 06-13 report) established the
   recipient-side APOL1 mechanism (T-cell-receptor signalling
   modulation → allograft rejection). Hopper/Wang/Olabisi will
   likely frame the *therapeutic* implications of both donor- and
   recipient-side APOL1 status. Together they give a
   mechanism + therapy framing pair.
3. **Practical for AoU work.** AoU has ~20% African-ancestry
   participants and APOL1 risk-allele frequencies at expected
   levels. Any APOL1 analysis in AoU should cite Olabisi's review
   for the clinical context.

**Follow-ups.** Pull the paper; check (a) the current state of
APOL1-targeted therapeutics (inaxaplin phase 3 status), (b) the
recommendation on transplant-decision APOL1 genotyping, (c) any
discussion of population-screening penetrance (vs the
clinically-ascertained penetrance in the AIRE penetrance paper
flagged 06-13), (d) tabulated genotype-phenotype risk estimates.

---

### 7. Potential preventive role of low-dose methotrexate against incident recorded psychosis: a retrospective cohort study based on electronic health records

**Authors.** F. Corsi-Zuelli, M. Taquet, B. Deakin, R. [author
truncated in snippet — likely R. Upthegrove] et al.
**Venue.** [truncated in snippet; publication venue not visible —
likely *Molecular Psychiatry* or *JAMA Psychiatry* given the
author panel].
**Signal source.** Google Scholar keyword feed — `electronic health
records` — new results (07-26 11:32Z).
**Bucket.** HIGH.
**Threads served.** Causal inference / pharmacoepi (drug-repurposing
signal from RWD); drug repurposing (EHR-based repurposing);
EHR phenotyping (psychosis onset definition).

**What the paper does (from title).** Retrospective cohort study
in EHR data testing whether low-dose methotrexate exposure
(prescribed for autoimmune or inflammatory indications) is
associated with lower incidence of *recorded psychosis* onset.
The design is the standard EHR-based drug-repurposing signal
detection template — take a drug prescribed for indication A,
look for reduced incidence of unrelated condition B in exposed
vs unexposed. Taquet (Oxford) is one of the leading practitioners
of this exact design.

**Why it matters for your work.**
1. **Exactly the drug-repurposing angle you flagged in April
   2026.** Your INTERESTS drug-repurposing section explicitly
   calls out "EHR-based repurposing signals mined from real-world
   prescribing and outcomes." This paper is the canonical
   instance of that shape for the window.
2. **Taquet on the author list.** Taquet's prior EHR-repurposing
   work (SSRI × COVID, various anti-inflammatories × psychiatric
   outcomes) is the reference class here — his methodology has
   been used by multiple groups. Solid pedigree.
3. **Pairs with the inflammation-psychosis biological literature.**
   Low-grade neuroinflammation as a driver of first-episode
   psychosis is an active area; an anti-inflammatory repurposing
   signal (methotrexate → psychosis prevention) is a well-motivated
   hypothesis test rather than a fishing expedition.

**Follow-ups.** Pull the paper; check (a) the data source
(TriNetX? OpenSAFELY? Oxford NHS?), (b) the confounding-by-
indication handling (methotrexate users have autoimmune disease
which is itself psychosis-risk-modifying), (c) whether they use
active comparator (e.g., methotrexate vs sulfasalazine or
biologic DMARDs), (d) subgroup analysis by autoimmune indication
(RA vs psoriasis vs Crohn's).

---

### 8. PrimeKG-Plus: a literature-derived expansion of a multimodal precision medicine knowledge graph

**Authors.** T.T.D. Nguyen, T. Nguyen-Phuong, Q.H. Nguyen et al.
**Venue.** *bioRxiv*, 2026.
**Signal source.** **Double-feed** — Google Scholar author feeds
for Marinka Zitnik and Tiffany J. Callahan — both new related
research (07-26 05:17Z).
**Bucket.** HIGH.
**Threads served.** Knowledge graphs & ontologies (biomedical KG
construction); drug repurposing (KG-based repurposing pipelines
with mechanistic rationale).

**What the paper does (from snippet).** Extends **PrimeKG** (the
Marinka Zitnik / Payal Chandak multimodal precision-medicine KG
covering 10 major biomedical databases) with literature-derived
relations extracted from PubMed / other publication sources.
Snippet emphasizes "Biomedical knowledge evolves rapidly, yet [KGs
lag]" — direct response to the KG-staleness problem.

**Why it matters for your work.**
1. **Directly on your drug-repurposing & KG threads.** Your
   drug-repurposing INTERESTS entry specifically flags KG / GNN
   approaches with *explainable* mechanistic rationale as
   high-priority. PrimeKG is the canonical biomedical KG for that
   family of work; expanding it with literature-mined facts is a
   direct capability upgrade.
2. **Double-feed (Zitnik + Callahan) is a strong signal.** Zitnik
   is the PrimeKG author; Callahan is the OMOP2OBO / SPOKE
   biomedical-KG author. Both feeds firing simultaneously on the
   same paper indicates community endorsement across the
   biomedical-KG author cluster.
3. **Practical utility for HPO-based rare-disease work.** PrimeKG
   includes HPO / MONDO / drug-target relations; a literature-
   expanded version should improve any HPO-driven candidate
   drug identification for rare disease (see also the Uria-Regojo
   11k rare-disease cohort paper in the 07-23 report).

**Follow-ups.** Pull the paper; check (a) the literature-extraction
pipeline (which NER? which relation extractor? PubTator 3.0?
LitCovid-style?), (b) whether the expansion is directional
(patient-KB) or bidirectional (KB-patient), (c) the size
delta from PrimeKG v1, (d) whether they benchmark on a
drug-repurposing downstream task.

---

### 9. Improving Mendelian Randomization Analysis by Instrument Borrowing from Auxiliary Outcome Traits

**Authors.** A. Chattopadhyay, N. Chatterjee.
**Venue.** arXiv 2607.16086, 2026 (likely a *Biostatistics* or
*Am J Hum Genet* submission).
**Signal source.** Google Scholar citation feed for Jonathan K.
Pritchard — 10 new citations (07-24 09:02Z).
**Bucket.** HIGH (methods).
**Threads served.** Causal inference (MR methods); genetic
epidemiology (instrument selection); drug target MR (via
instrument-strength improvements).

**What the paper does (from title).** Novel MR estimator that
*borrows instruments from auxiliary outcome traits* to strengthen
inference on the primary outcome. The Chatterjee group (Johns
Hopkins) is known for statistical-genetics methods work
(GenoPred, PROSPER, etc.) — this fits the same pattern of
"borrow-strength-across-related-traits" methodology.

**Why it matters for your work.**
1. **MR methods are having a moment.** MR-ALasso (Qasim et al.,
   stat.ME, 07-22 report), MR-ALasso-B, Saxby metformin drug-
   target MR (07-23 report), and now this Chatterjee paper — four
   MR-methods / drug-target-MR papers in three weeks. MR estimator
   defaults are shifting; worth tracking the frontier.
2. **Direct implication for drug-target MR.** If instruments are
   scarce for a drug target (e.g., low-N proxy exposure like
   circulating drug-target protein), borrowing instruments from
   auxiliary traits could rescue analyses that would otherwise
   be weak-instrument-limited. Directly on your drug-target-MR
   sub-thread.
3. **Chatterjee lineage means high methodological rigor.**
   Chatterjee's methods papers historically come with detailed
   simulations and R packages; expect this one to be usable off
   the shelf.

**Follow-ups.** Pull the paper; check (a) the theoretical
guarantees (consistency conditions on auxiliary trait selection),
(b) simulation performance vs standard MR estimators, (c) the
"how similar must the auxiliary trait be" question — is there
a formal criterion or an empirical rule of thumb?, (d) R /
Python implementation.

---

## METHODS-WATCH (exemplary methods, off-thread topic)

### `arxiv-digest` 2026-07-24 — Auditing pretraining contamination in single-cell foundation model benchmarks
**Authors.** Sarwan Ali (q-bio.GN).
**Signal.** `arxiv-digest` 07-24, keyword `foundation model`, score 1.
**Take.** MinHash-based gene-set fingerprint + loss-based
membership-inference attack (MIA-scFM) framework for auditing
whether scFM benchmarks are contaminated by their pretraining
corpora. Applied to four scIB benchmarks × three scFMs
(Geneformer, scGPT, UCE); finds PBMC 3k and CELLxGENE human
pancreatic islet atlas are 77-80% contaminated by Genecorpus-30M.
Introduces a controlled re-pretraining experiment showing that
MIA-scFM AUROC scales monotonically with capacity-to-data ratio.
**Why it's worth methods-watching:** the audit framework —
fingerprinting + membership inference + controlled overfitting
experiment — is directly portable to EHR-foundation-model
benchmarks. CLMBR / MOTOR / FEMR / MEDS models pretrain on
subsets of the *same* institutional EHRs that supply their
downstream evaluation cohorts. This is the second Sarwan Ali
paper in the digest (07-23 also had a Sarwan Ali dictionary-
learning interpretability paper on genomic foundation models) —
worth watching the author's output. **METHODS-WATCH.**

### Semaglutide/liraglutide TTE methods
See HIGH #4 above. The Hernán-framework TTE specification is the
methodological interest even outside the specific GLP-1 question.

### S4-Multi multi-ancestry PRS protocol (STAR Protocols, 2026)
**Authors.** P.H. Lai, J.P. Tyrer, J. Baierl, P.D.P. Pharoah, P.C.
Peng.
**Signal.** Google Scholar author feed for Joshua C. Denny — new
related research (07-24 09:02Z).
**Take.** STAR-Protocols piece on constructing multi-ancestry
polygenic models using S4-Multi. Cross-ancestry PRS is on your
active list; STAR-Protocols papers are step-by-step recipes usable
for direct implementation. Not novel science but useful reference
utility — cite whenever building multi-ancestry PRS in AoU.
**METHODS-WATCH (reference utility).**

### Instrument borrowing MR (Chatterjee) — see HIGH #9

### Robust foundation model for healthcare (Z. Wu, 2025 thesis / Peter Szolovits feed 07-24)
**Take.** MIT thesis-tier robustness work on healthcare foundation
models — likely covers adversarial robustness and distributional
shift, which are the two known weaknesses of CLMBR / MOTOR-style
FMs. Not clinically on-thread but a natural reference for any
EHR-FM benchmarking paper. **METHODS-WATCH.**

### AI-assisted differential diagnosis safety-framework (Ma, Giuffrè, Wright, McCann et al., arXiv, 2026; Hua Xu feed 07-24)
**Take.** Hypothetico-deductive safety framework for AI-DDx
systems. The clinical-safety framing is what makes this
methods-watch — most LLM-DDx papers focus on accuracy metrics
without a safety-focused evaluation. Off your primary threads
but useful reference if you build any clinical LLM tooling.
**METHODS-WATCH.**

---

## Duplicates / re-confirmations (already reported)

Several items in this window are re-confirmations of previously
reported papers via additional author feeds — logged for
completeness, not double-counted in HIGH totals:

- **Baya et al. — Polygenic-deviation → rare-disease damaging
  variants — AJHG.** Now confirmed via a second feed (Lisa Bastarache
  related-research 07-26; originally reported 07-23 as HIGH #1 via
  Denny feed). Still HIGH; no new content.
- **Wu et al. — Integrative UKB WES × multi-omics for metabolic
  syndrome — Functional & Integrative Genomics.** Now confirmed via
  two additional feeds (Karczewski + Montgomery related-research
  07-26; originally 07-23 report HIGH #5 via UKB keyword feed).
- **Jo et al. — East Asian 1M+ cross-ancestry meta-analysis —
  bioRxiv.** Re-surfaced in Jian Yang related-research feed 07-24
  (originally 07-23 report HIGH #8 via Denny feed).
- **Johnson et al. — AoU healthcare-experiences disparities — J
  Community Genet.** Re-surfaced in Denny related-research + AoU
  keyword feeds 07-26 (originally 07-23 report HIGH #12 via AoU
  NCBI feed).
- **Żebrowska et al. — Circadian Imbalance Index GWAS/PheWAS/MR —
  EBioMedicine.** Re-surfaced in Chenjie Zeng self-alert +
  Bastarache related-research feeds 07-26 (originally 07-23 report
  HIGH #6 via AoU + UKB NCBI feeds). Self-alert hit for the
  Circadian-Imbalance / PheWAS-MR pipeline overlap with the
  penetrance methodology paper is a small but meaningful citation
  signal.
- **Lemieux et al. — National EHR interoperability for research —
  JAMIA Open.** Re-surfaced in AoU keyword feed 07-26 (originally
  07-23 report HIGH #10 via AoU NCBI feed).
- **Ekici et al. — Diagnosing Mendelian Kidney Disease** (mendelian
  diseases keyword feed 07-26). Kidney-genetics review; adjacent to
  the APOL1 thread but on hereditary kidney disease broadly. Skim
  as a citation source for the Mendelian-kidney-disease context
  in any APOL1 manuscript.

---

## SKIP / noise (logged, no action)

- **"knowledge graph" keyword** continues to surface non-biomedical
  KG papers (educational recommender systems, financial dynamic
  KGs — the latter is the 07-14 arxiv-digest catch, correctly
  scored 1). **5 consecutive windows** of non-biomedical KG hits
  from the keyword. Recommendation restated: narrow to `biomedical
  knowledge graph` OR add exclusions for education / finance /
  manufacturing.
- **"mendelian diseases" keyword** continues to leak MR
  papers (Zhang et al. lipid-ALS MR, 07-23). 5th consecutive
  window. Recommendation: replace with `OMIM` / `MIM` IDs or add
  `-randomization` exclusion.
- **"drug repurposing" keyword** — mostly review pieces
  (fibromyalgia, diabetes mellitus computational repurposing,
  KRAS network analysis) and one genuine EHR-based signal
  (Corsi-Zuelli methotrexate → psychosis — captured HIGH above).
  The two computational-drug-repurposing reviews are off the
  KG-explainability / EHR-signal angle you flagged; skip.
- **Multiple UK Biobank dietary-index / lifestyle / anthropometric
  → outcome papers** — routine UKB epi, no thread crossover
  (metabolic-syndrome × gastric cancer, physical activity ×
  MASLD, etc.).
- **Bombus / animal phylogeography / de novo protein nanoparticle
  design / cf-DNA fragmentomics** — off-thread from Shendure /
  Baker / Vogelstein feeds.
- **Pediatric type-1 diabetes seasonality, various
  immunology / autoimmune keyword hits** — off-thread.
- **AoU + APHA meeting abstract on CHD risk classification in
  Black and Hispanic/Latina women (Rodriguez et al., APHA 2026;
  AoU keyword feed 07-23)** — clinical-descriptive AoU work; off
  your active pharmacoepi / genetic-epi threads. SKIP.
- **Impact of clonal hematopoiesis in MM CAR-T outcomes (Carlson
  et al., 07-23 CHIP feed)** — CHIP in CAR-T therapy, oncology-
  clinical rather than the CHIP × cardiovascular / therapy-associated
  clone dynamics you've been tracking. Borderline; logged as
  SKIP for this window but worth mentioning if you write anything
  on CHIP in cellular therapy contexts.
- **CYP3A5 tacrolimus PK models** (multiple citation feeds
  07-24) — narrow pharmacogenetics topic, off the current active
  threads.
- **Various citation-audit / self-citation hits** (Chenjie Zeng
  self-alerts on the Circadian Imbalance paper and Van der Velden
  PSMA imaging in metastatic prostate cancer, DePinho on TERT in
  Nature Aging) — kept as-is per prior report; useful as a
  citation-audit signal.

---

## Suggestions for the pipeline

Repeating and refining suggestions from prior reports:

1. **`arxiv-digest` cron output stayed thin (1/3 non-empty days).**
   Third consecutive window with < 2 papers/day; only one score-1
   paper this window. The `cs.LG` + `stat.ME` + medRxiv/bioRxiv
   addition remains the highest-value change for recall.
2. **`knowledge graph` keyword — narrow it now.** 5 consecutive
   windows of majority non-biomedical hits (education, finance,
   manufacturing). Recommend `biomedical knowledge graph` OR
   `clinical knowledge graph` OR `(knowledge graph) (medical OR
   biomedical OR clinical OR EHR OR phenotype)` as previously
   suggested.
3. **`mendelian diseases` — replace or scope.** 5 consecutive
   windows leaking MR papers. Replace with `OMIM` / `MIM` IDs
   or add `-randomization` exclusion.
4. **Consider a `target trial emulation` keyword.** This window
   had two clean TTE papers (Cannon semaglutide/liraglutide,
   Yen SGLT2i/GLP-1 RA psoriatic arthritis) that surfaced via
   author feeds only. A dedicated `target trial emulation` OR
   `emulated target trial` keyword would improve recall on this
   pattern.
5. **Consider a `polygenic prediction of drug response` OR
   `PRS × treatment response` composite keyword.** Fritsche
   (06-13 report) + Liou (this report) suggest this is a
   coherent sub-thread worth its own recall filter.
6. **Add `EHR foundation model` variants.** The `Foundation
   models and "electronic health records"` current keyword is
   producing mixed signal (hepatology + generative AI review
   this window; useful last window). Consider a stricter
   composite `(CLMBR OR MOTOR OR FEMR OR MEDS) OR ("EHR
   foundation" OR "clinical foundation model")`.
7. **Consider watching for `silver labels` or `weak supervision`
   in EHR context.** The Wang et al. arXiv preprint (HIGH #1
   this window) suggests a growing methods sub-cluster on
   weakly-supervised phenotyping.

---

*Prepared 2026-07-27; next report expected once new signal
accumulates (typically 1–2 days). Full arxiv-digest for today is
scheduled via the 10:30 UTC cron; recent digests at
`digests/2026-07-2[4-6].md` are largely empty (see arxiv-digest
staleness note above).*
