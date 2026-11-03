# Repository guide for 0.4.0

**tentative authors list**

Nicolas A Karakatsanis, Atlas Haddadi Avval, Julia Brosch-Lenz, Irene Buvat, Abhinav Jha, Mario Jreige, Quanzheng Li, Neeta Pandit-Taskar, Babak Saboury, Jazmin Schwartz, Nouran Zaid, Tahir I Yusufaly, Tyler J Bradshaw

The current model lives under `extensions/lu177_psma/v0.4.0/`. The previous `v0.3.0/` directory is preserved for comparison and regression checks. The inherited `gdcdictionary/` and its Python packaging remain unchanged and are not the merged proposal.

Lu177-PSMA theranostics data model release 0.4.0 extends the deployed MIDRC Gen3 dictionary version `1.4.3-2-g7505333`, commit `7505333d56c87a289463a814131e38d0f2be6674`, retrieved on 16 October 2026. The baseline snapshot and its SHA-256 checksum are preserved in this release.

The imported source parent is `bee947238381704486ccd12beeb8f4689fb22843`, a different revision. Its custom PT `mr_images` field and other differences need receiving-team reconciliation before integration.

## Current artifacts

- `schemas`, `integration/yaml`, `templates`, `tables` and `graph` are representations of the same 90-node dictionary.
- `review` contains the two radiopharmaceutical workbooks; `publication` contains the manuscript draft, supplement and submission notes.
- `mappings/radiopharmaceutical_source_crosswalk.json` and the revision log trace the new inputs. Source hashes and field extracts are under `sources/radiopharmaceutical_inputs`.
- `integration/v030_to_v040_additive_patch.json` upgrades the prior merged proposal. The baseline patch still starts from the exact deployed MIDRC snapshot.
- `scripts/validate_model.py` validates structure, profile rules, fixtures and both patches. Root `scripts/build_dictionary_docs.py --check` detects documentation drift.
- `scripts/v040/` records the schema and source-crosswalk generation procedure. Artifact authoring also requires the source Word drafts and the supported spreadsheet renderer; generated artifacts are distributed for direct review.

## Publication workflow

The GitHub Actions release workflow runs on the authorized `cdis` branch when VERSION changes. It validates the model and documentation, verifies checksums, builds downloads and publishes a development release. The title is `0.4.0` and the tag is `v0.4.0`. Existing tags are never moved. This workflow publishes files only; it does not deploy MIDRC, migrate a database or submit a manuscript to a journal.

Model, baseline dictionary, terminology/ontology, clinical criteria and dataset versions remain independent. A receiving deployment still needs a Gen3 build, ingestion/export round trip, vocabulary review and clinical/radiopharmacy review.
