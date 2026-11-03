# Lu177-PSMA changelog

## 0.4.0

2 November 2026 · Development proposal for technical and scientific review.

Lu177-PSMA theranostics data model release 0.4.0 extends the deployed MIDRC Gen3 dictionary version `1.4.3-2-g7505333`, commit `7505333d56c87a289463a814131e38d0f2be6674`, retrieved on 16 October 2026. The baseline snapshot and its SHA-256 checksum are preserved in this release.

Baseline SHA-256: `578e57dc45f719b07f1ac31482fed9129675c133aaafc3004dc346e5e4928e21`.

### Additive model changes

- Add 23 nodes separating reference agent/substance/target identity, product and packaging, manufacturing, physical units, supply, prescription, dispensing, reference evidence and computational research.
- Add optional fields or links to six earlier nodes: `radiopharmaceutical`, `radiopharmaceutical_batch`, `administration`, `provenance`, `toxicity_event` and `treatment_plan`.
- Retain all 29 MIDRC baseline nodes and all earlier clinical outcome structures. The seven enum appends were already proposed in v0.3.0; this release introduces no additional baseline enum changes.
- Distinguish molar and specific activity, physical decay and biological metabolism, reference/cohort evidence and human observations, and predicted and measured quantities.
- Add an explicit v0.3-to-v0.4 additive patch and context validation. Legacy fields remain readable; curating the new normalized profiles requires an explicit, provenance-preserving migration.

### Review materials

The model now contains 90 nodes, 412 declared links and 3,212 node–property entries. The 1,371 source occurrences include 450 radiopharmaceutical entries: 102 from Nouran's initial model, 325 from the blueprint and 23 IDRP passages. Eighteen revision themes and source-by-source crosswalks identify proposed changes and reasons.

The release includes revised model and rationale workbooks, an offline HTML explorer with 12 graph views, the architecture/status document, a scientific manuscript draft, supplementary information and submission notes. Nouran Zaid is added after Jazmin Schwartz and before Tahir I Yusufaly in the tentative authors list.

### Validation and limits

Local validation accepts all 153 connected example records, all 122 prior records and 29 baseline fixtures. All 49 predefined invalid cases are rejected. Both additive patches reproduce the merged dictionary; JSON/YAML and generated documentation agree. The examples are synthetic and no prediction algorithm was executed.

This release does not establish production Gen3 deployment, clinical validity, regulatory compliance, ontology-owner approval or institutional adoption. It does not submit the manuscript to a journal. NucLex alignment and context-specific terminology review remain pending.

### Version identity

Repository/document release: **0.4.0**; Git tag: **v0.4.0**; schema revision: **0.4.0-proposal**; model directory: `extensions/lu177_psma/v0.4.0/`. The old `v0.3.0/` directory, earlier tags and release assets remain unchanged. This is an additive minor release, following documentation-only releases 0.3.1 and 0.3.2.

**tentative authors list**

Nicolas A Karakatsanis, Atlas Haddadi Avval, Julia Brosch-Lenz, Irene Buvat, Abhinav Jha, Mario Jreige, Quanzheng Li, Neeta Pandit-Taskar, Babak Saboury, Jazmin Schwartz, Nouran Zaid, Tahir I Yusufaly, Tyler J Bradshaw

## 0.3.2 — 2026-10-19

Documentation-only follow-up updating the attached Word and HTML files.

- Add the precise MIDRC baseline statement and corrected release/tag history to both artifacts.
- Use documentation release 0.3.2 in the Word cover/footer, HTML header and download filenames; retain schema revision 0.3.0-proposal.
- Retain the existing repository document paths and refresh document provenance, validation records and checksums.
- Preserve model schemas, templates, graph data, examples, source snapshots and all earlier release tags/assets.

Lu177-PSMA theranostics data model release 0.3.0 extends the deployed MIDRC Gen3 dictionary version `1.4.3-2-g7505333`, commit `7505333d56c87a289463a814131e38d0f2be6674`, retrieved on 16 October 2026. The baseline snapshot and its SHA-256 checksum are preserved in this release.

## 0.3.1 — 2026-10-19

Documentation-only patch of the 0.3.0 development release.

- Add the exact deployed MIDRC baseline version, commit, retrieval date and snapshot provenance to the changelog and release notes.
- Correct outdated statements that an inherited MIDRC `0.3.0` tag is still present. The initial theranostics tag remains `v0.3.0`; this patch uses `v0.3.1`.
- Correct the published v0.3.0 release description without moving its tag or replacing its original assets.
- Refresh the repository guide, release metadata and downloadable ZIP. Keep the standalone Word and HTML filenames at v0.3.0 because those artifacts are unchanged.
- Preserve every file under `extensions/lu177_psma/v0.3.0/` and `gdcdictionary/` byte-for-byte, including schemas, definitions, examples and baseline snapshots. No data migration is introduced.

Lu177-PSMA theranostics data model release 0.3.0 extends the deployed MIDRC Gen3 dictionary version `1.4.3-2-g7505333`, commit `7505333d56c87a289463a814131e38d0f2be6674`, retrieved on 16 October 2026. The baseline snapshot and its SHA-256 checksum are preserved in this release.

## 0.3.0 — 2026-10-16

Lu177-PSMA theranostics data model release 0.3.0 extends the deployed MIDRC Gen3 dictionary version `1.4.3-2-g7505333`, commit `7505333d56c87a289463a814131e38d0f2be6674`, retrieved on 16 October 2026. The baseline snapshot and its SHA-256 checksum are preserved in this release.

Initial theranostics development release of the **SNMMI-MIDRC Lu177-PSMA theranostics data model**, a proposed expansion of the baseline MIDRC Gen3 model and dictionary.

- 67 node types and 293 relationships: 29 retained MIDRC baseline nodes plus 38 proposed theranostics nodes.
- Reuse of MIDRC PET/PT, NM, CT, MR, measurement, observation and annotation structures, with optional additions to 17 baseline nodes and seven proposed enum additions.
- JSON/YAML schemas, portal-style JSON templates, graph/table views, baseline snapshots, additive patch and migration/source mappings.
- Revised outcome-assessment fields, nine patient-journey stages, five use cases and 122 invented linked example records.
- Human-readable architecture, node catalog, domain index and 67 field-level dictionary pages following the MIDRC documentation structure, covering 2,519 node/property entries.
- Author-supplied v0.3.0 Word and HTML files preserved exactly.

**Version identity:** release **0.3.0**, tag **v0.3.0**. The theranostics tag is `v0.3.0`; inherited MIDRC tags have since been removed from this repository. Packaged working-artifact revision `0.3.0-proposal` describes its development status.

**Validation:** local schema, baseline, template, evidence-link and negative-case checks pass. Live Gen3 build/ingestion, clinical completeness and final ontology/terminology alignment remain pending. This release does not deploy a MIDRC service or prescribe a treatment regimen.

The imported `gdcdictionary/` source is preserved, including its custom PET/MR `mr_images` property. Reconcile the imported source revision with the pinned deployed baseline before integration.

**tentative authors list**

Nicolas A Karakatsanis, Atlas Haddadi Avval, Julia Brosch-Lenz, Irene Buvat, Abhinav Jha, Mario Jreige, Quanzheng Li, Neeta Pandit-Taskar, Babak Saboury, Jazmin Schwartz, Tahir I Yusufaly, Tyler J Bradshaw
