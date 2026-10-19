# SNMMI-MIDRC Lu177-PSMA theranostics data model

**Release 0.3.2** · A proposed expansion of the baseline MIDRC Gen3 data model and data dictionary.

This project structures the imaging, clinical, treatment, dosimetry and outcome evidence needed to study personalized Lu177-PSMA therapy. Its graph, table and JSON views describe the same nodes, properties and relationships. Development is led within the SNMMI AI Task Force and Computational Nuclear Ontology Working Groups. The model and its NucLex alignment remain under development; this repository does not assert institutional adoption or a deployed MIDRC extension.

Release **0.3.2** updates the Word architecture document and HTML explorer with the exact MIDRC baseline, corrected tag history and matching documentation version labels. The model schema revision remains **0.3.0-proposal**; node structures, relationships and field definitions are unchanged.

## Start here

| Resource | What it contains |
| --- | --- |
| [Release 0.3.2](https://github.com/nkarakatsanis/MIDRC-SNMMI-Lu177-PSMA-Theranostics-Data-Model/releases/tag/v0.3.2) | Downloadable model archive, standalone HTML and Word documentation. |
| [Human-readable architecture](docs/DATA_MODEL.md) | Domains, patient journey, use cases, MIDRC reuse, OMOP candidates and semantic-layer distinctions. |
| [Field-by-field data dictionary](docs/dictionary/README.md) | Definitions, types, required fields, allowed values and link rules for all 67 nodes and 2,519 node/property entries. |
| [Interactive model explorer](extensions/lu177_psma/v0.3.0/NMMI_Model_Explorer.html) | Graph and table views, element search, mappings, patient journey and use cases. Download the HTML and open it locally. |
| [Architecture document](extensions/lu177_psma/v0.3.0/NMMI_Lu177_PSMA_Architecture_and_Status.docx) | Architecture document revised from the author-supplied file for documentation release 0.3.2. |
| [Node catalog](docs/NODE_CATALOG.md) | All 67 nodes with their role, property count and JSON/YAML/template links. |
| [Domain index](docs/DOMAINS.md) | The 24 domain navigation groups and their reusable node types. |
| [Developer integration guide](extensions/lu177_psma/v0.3.0/integration/MIDRC_Integration_Guide.md) | Additive changes, mappings, validation and implementation review. |
| [Repository guide](docs/REPOSITORY_GUIDE.md) | Source layout, baseline provenance, release/version rules and workflow behavior. |

## Data Dictionary

Following the MIDRC repository convention, a Gen3 data dictionary defines strongly typed nodes, valid node properties and links. The executable schemas therefore carry both the **data model** (record structure and relationships) and **data dictionary** (element definitions and constraints).

The complete v0.3.0 proposal is under `extensions/lu177_psma/v0.3.0/`. Existing imported source remains under `gdcdictionary/`. These are explicitly separate because the imported checkout and the deployed MIDRC dictionary used to build the proposal are different revisions. Adding this release does not replace the active imported schemas or deploy a revised commons.

### Data Dictionary Structure

The proposal contains **67 node types and 293 relationships**: 29 baseline MIDRC nodes, including 17 with optional additions and 12 unchanged, plus 38 proposed theranostics nodes. The dictionary retains the original baseline required fields, datatypes, relationship cardinalities and link-group rules; seven enum additions are separately identified for review.

| Representation | Location |
| --- | --- |
| Merged compiled Gen3 dictionary | [`gen3_dictionary.json`](extensions/lu177_psma/v0.3.0/gen3_dictionary.json) |
| Individual JSON node schemas | [`schemas/`](extensions/lu177_psma/v0.3.0/schemas/) |
| YAML node schemas for integration review | [`integration/yaml/`](extensions/lu177_psma/v0.3.0/integration/yaml/) |
| Portal-style JSON templates | [`templates/`](extensions/lu177_psma/v0.3.0/templates/) |
| Property tables and source crosswalks | [`tables/`](extensions/lu177_psma/v0.3.0/tables/) and [`mappings/`](extensions/lu177_psma/v0.3.0/mappings/) |
| Graph exports and scoped views | [`graph/`](extensions/lu177_psma/v0.3.0/graph/) |
| Additive changes against the pinned baseline | [`midrc_additive_patch.json`](extensions/lu177_psma/v0.3.0/integration/midrc_additive_patch.json) |

Each schema declares its node ID, category, descriptions, properties, required fields and `links`. Links identify the parent `target_type`, reverse `backref`, relationship label, multiplicity and requirement. Gen3 child-to-parent record links and reverse traversal support the connected graph. Graph displays are views of those definitions, rather than a separate clinical ontology.

### Node Properties and Examples

Reuse MIDRC nodes when their meaning and record grain match: `case` for the patient, `visit` for encounter context, `imaging_study` for examinations, `measurement` for quantitative results, `observation` for suitable categorical observations, and `annotation` for segmentation records. PET images use `pt_series_file`; planar and SPECT images use `nm_series_file`; CT and MR use their corresponding series-file nodes.

For a lesion dose, `absorbed_dose` points to an `anatomic_target` and a `dosimetry` calculation. The target points to the patient; the calculation points to the cycle and source acquisitions. Segmentation `annotation` records and method metadata preserve how the estimate was derived. The [lesion-dose use case](docs/DATA_MODEL.md#a-lesion-dose-in-the-connected-model) and [synthetic patient records](extensions/lu177_psma/v0.3.0/examples/full_patient_journey.json) make these links concrete.

For PSA, a `measurement` stores the result, unit, assay identity and timing. A `response_assessment` uses role-specific links such as `baseline_psa_results` and `confirmatory_psa_results`. Those links identify the supporting measurements without copying their values into an outcome row.

`*` prefixes in portal templates mark required fields and must be removed before submission. Null values are editing placeholders. A required alternative link group may require one link even when individual members are not starred. File indexing URLs are handled separately from the node properties. See [template preparation](extensions/lu177_psma/v0.3.0/scripts/prepare_record.py).

### Data model, dictionary, terminology and ontology

| Component | Responsibility | Example |
| --- | --- | --- |
| Data model | Record identity, structure, links and cardinality. | This dose belongs to this lesion and derives from this calculation for this cycle. |
| Data dictionary | Element meaning, datatype, units, allowed values and validation. | `absorbed_dose_gy` is a numeric dose estimate in Gy; its statistic is also recorded. |
| Terminology | Controlled labels and identifiers used consistently in records. | An appropriate reviewed LOINC code identifies a PSA assay. |
| Ontology | Concepts and formal semantic relationships among them. | NucLex/RadLex concepts classify anatomical targets, imaging modalities and dosimetry methods. |

Terminologies can include ontology structure. LOINC, NucLex and RadLex are separately governed semantic resources; they are not interchangeable lists. Their codes and versions can be bound to model properties without replacing links between actual patient records. No NucLex or RadLex identifiers are fabricated in this proposal.

## Dictionary Changes

The original MIDRC change categories are retained for review of future revisions.

### Breaking Changes

Removing or renaming nodes or properties, narrowing datatypes or enums, changing record grain, making an optional field mandatory, or tightening link cardinality can invalidate existing records. Review such changes against actual data and supply an explicit migration. Migration from the earlier custom v0.2 proposal is distinct from compatibility with the MIDRC baseline.

### Entity Relation Additions

This proposal adds 38 theranostics nodes and optional properties/relationships to 17 existing nodes. The [node delta](extensions/lu177_psma/v0.3.0/integration/node_delta.csv) records each decision. New relationships still require Gen3 build and ingestion testing before use in a deployed commons.

### Schema Additions

All 824 baseline property definitions are preserved except seven declared enum appends. Those additions are recorded in [proposed enum additions](extensions/lu177_psma/v0.3.0/integration/proposed_enum_additions.json). Existing MIDRC test-name enums remain intact; assay-specific source labels and coded identity are represented by separate optional properties where needed.

### Cosmetic Corrections

Descriptions and labels can be improved without changing record structure when the meaning is unchanged. A change of measured quantity, unit, concept scope or semantics is not merely cosmetic. Preserve source definitions and mapping provenance during review.

## Testing

From the repository root:

```bash
python -m pip install -r extensions/lu177_psma/v0.3.0/scripts/requirements.txt
python extensions/lu177_psma/v0.3.0/scripts/validate_model.py
python scripts/build_dictionary_docs.py --check
```

Local checks cover 67 schemas and templates, baseline preservation, the additive patch, 921 source occurrences, 122 synthetic linked records, 29 baseline regression fixtures and 27 deliberately invalid cases. The [validation report](extensions/lu177_psma/v0.3.0/validation/validation_report.json) lists the checks and limitations. The synthetic journey illustrates record structure, not a recommended treatment regimen.

The field-level Markdown pages are generated from the same committed schemas. Regenerate them with `python scripts/build_dictionary_docs.py` after schema changes. Build the release downloads with `python scripts/build_release_assets.py --output dist`.

Live Gen3 compilation, database migration, submission API ingestion, portal rendering and real clinical data remain unvalidated. Clinical and terminology-owner review is still required. HTML interaction checks use DOM emulation; the revised Word document is rendered and visually reviewed, with the author's layout retained.

## Versioning

| Item | Identifier |
| --- | --- |
| This repository release | **0.3.2**, recorded in [`VERSION`](VERSION) and [`release.json`](release.json) |
| Current repository Git tag | `v0.3.2` (documentation-only patch) |
| Word and HTML documentation | `0.3.2`; revised baseline and release-history presentation |
| Initial theranostics model tag | `v0.3.0` |
| Packaged working-artifact revision | `0.3.0-proposal`; “proposal” describes its review status |
| Pinned deployed MIDRC dictionary | `1.4.3-2-g7505333`, commit `7505333d56c87a289463a814131e38d0f2be6674` |
| Imported repository parent | `bee947238381704486ccd12beeb8f4689fb22843` |

The initial theranostics model release is tagged `v0.3.0`. Inherited MIDRC tags have since been removed from this repository. Documentation patches are tagged `v0.3.1` and `v0.3.2`; earlier release tags and their original downloads remain unchanged. Future versions should document breaking, additive and cosmetic changes, while model, baseline-dictionary and terminology/ontology versions remain independently identifiable. The original `pyproject.toml` describes the imported baseline Python package, not the new repository release.

## Authorship and attribution

**tentative authors list**

Nicolas A Karakatsanis, Atlas Haddadi Avval, Julia Brosch-Lenz, Irene Buvat, Abhinav Jha, Mario Jreige, Quanzheng Li, Neeta Pandit-Taskar, Babak Saboury, Jazmin Schwartz, Tahir I Yusufaly, Tyler J Bradshaw

The tentative list does not assert individual approval. Existing upstream `LICENSE` and `NOTICE` files are retained. See the extension [attribution notice](extensions/lu177_psma/v0.3.0/NOTICE.md) and the [original imported README](docs/upstream/README.before-lu177-psma-v0.3.0.md). The model remains a technical proposal for the working group and MIDRC developers.

References: [Gen3 dictionary and model](https://gen3.org/resources/user/dictionary/), [MIDRC dictionary](https://data.midrc.org/DD), [MIDRC source](https://github.com/MIDRC/midrc_dictionary).
