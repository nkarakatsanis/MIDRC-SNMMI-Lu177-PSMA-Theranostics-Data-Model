# Lu177 PSMA model version 0 3

**tentative authors list**

Nicolas A Karakatsanis, Atlas Haddadi Avval, Julia Brosch-Lenz, Irene Buvat, Abhinav Jha, Mario Jreige, Quanzheng Li, Neeta Pandit-Taskar, Babak Saboury, Jazmin Schwartz, Tahir I Yusufaly, Tyler J Bradshaw

Version 0.3.0-proposal, 16 October 2026. This package proposes an additive theranostics extension to the deployed MIDRC dictionary. The architecture document and offline HTML explain the model and the patient journey. Technical acceptance by MIDRC and terminology-owner approval remain separate steps.

## Start here

- `NMMI_Model_Explorer.html`: graph, node tables, source crosswalk, patient journey, use cases, outcome framework, integration audit and the conceptual layers.
- `NMMI_Lu177_PSMA_Architecture_and_Status.docx`: human-readable architecture and integration description.
- `integration/MIDRC_Integration_Guide.md`: precise changes and developer handoff.
- `gen3_dictionary.json`: compiled merged proposal with the 29 baseline nodes plus 38 proposed nodes.
- `schemas/`, `templates/`, `tables/`, `graph/`: synchronized schema, portal-style JSON templates, CSV property tables and graph exports.
- `integration/midrc_additive_patch.json`: RFC 6902 add operations against the pinned baseline, with a tested round trip.
- `examples/full_patient_journey.json`: 122 entirely invented linked records across 55 used node types; 29 independent baseline regression fixtures are separate.
- `source_field_catalog.json` and `mappings/`: 921 original field occurrences, including 94 revised outcome entries and 65 paper-table occurrences.
- `validation/`: executed local checks and 65 review items, including historical findings and new integration decisions.

## What changed

Eleven earlier custom node types are retired in favor of MIDRC nodes. PET uses `pt_series_file`; planar and SPECT use `nm_series_file`; CT uses `ct_series_file`. Laboratory, ROI and anthropometric values use `measurement`; lifestyle values use `observation`. Contours use `annotation`, with existing annotation-file nodes for artifacts. Raw and other supporting files use `supplementary_file`. Version 0.2 legacy outcome aliases are mapped to their revised canonical destinations.

All 824 baseline property definitions are preserved except seven explicit enum appends. Existing required fields, enums, types and relationship groups are not narrowed or replaced. 17 MIDRC nodes receive optional additions and 12 remain unchanged. Additional source-only labels are clearly distinguished from canonical definitions. Semantic deduplication still requires context-specific expert review; the package does not declare the external ontology complete.

## Templates and validation

`*` prefixes mark required fields in the supplied portal format. They are removed before submission. Nulls are editing placeholders; remove unfilled optionals and fill required values. Required link groups still need a member even when every individual link is unstarred. File URLs belong to file indexing; the live PT/NM schemas do not define a node property named `urls`.

Run `python scripts/validate_model.py` from a Python environment with `jsonschema` installed. The report includes JSON Schema and Gen3 metaschema validation, baseline preservation, 29 regression fixtures, 122 patient-journey records, source coverage, and 27 intentionally invalid cases. Gen3 compilation, deployment, ingestion and real clinical data have not been tested. Synthetic file sizes, hashes and names are placeholders, not verified files.

MIDRC source attribution and Apache 2.0 license are under `sources/`. Historical mapping files under `sources/v0_2_*` are reference history; current mappings are under `mappings/`. The tentative authors list does not imply author approval of this proposal. Technical adoption remains subject to the receiving team’s review.
