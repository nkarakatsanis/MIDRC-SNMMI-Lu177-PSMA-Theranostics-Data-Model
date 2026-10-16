# Lu177-PSMA release history

# 0.3.0

Initial theranostics development release of the **SNMMI-MIDRC Lu177-PSMA theranostics data model**, a proposed expansion of the baseline MIDRC Gen3 model and dictionary.

- 67 node types and 293 relationships: 29 retained MIDRC baseline nodes plus 38 proposed theranostics nodes.
- Reuse of MIDRC PET/PT, NM, CT, MR, measurement, observation and annotation structures, with optional additions to 17 baseline nodes and seven proposed enum additions.
- JSON/YAML schemas, portal-style JSON templates, graph/table views, baseline snapshots, additive patch and migration/source mappings.
- Revised outcome-assessment fields, nine patient-journey stages, five use cases and 122 invented linked example records.
- Human-readable architecture, node catalog, domain index and 67 field-level dictionary pages following the MIDRC documentation structure, covering 2,519 node/property entries.
- Author-supplied v0.3.0 Word and HTML files preserved exactly.

**Version identity:** release **0.3.0**, tag **v0.3.0**. The existing MIDRC tag `0.3.0` is preserved. Packaged working-artifact revision `0.3.0-proposal` describes its development status.

**Validation:** local schema, baseline, template, evidence-link and negative-case checks pass. Live Gen3 build/ingestion, clinical completeness and final ontology/terminology alignment remain pending. This release does not deploy a MIDRC service or prescribe a treatment regimen.

The imported `gdcdictionary/` source is preserved, including its custom PET/MR `mr_images` property. Reconcile the imported source revision with the pinned deployed baseline before integration.

**tentative authors list**

Nicolas A Karakatsanis, Atlas Haddadi Avval, Julia Brosch-Lenz, Irene Buvat, Abhinav Jha, Mario Jreige, Quanzheng Li, Neeta Pandit-Taskar, Babak Saboury, Jazmin Schwartz, Tahir I Yusufaly, Tyler J Bradshaw
