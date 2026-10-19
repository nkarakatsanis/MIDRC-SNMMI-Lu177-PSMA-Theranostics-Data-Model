# MIDRC integration guide

**tentative authors list**

Nicolas A Karakatsanis, Atlas Haddadi Avval, Julia Brosch-Lenz, Irene Buvat, Abhinav Jha, Mario Jreige, Quanzheng Li, Neeta Pandit-Taskar, Babak Saboury, Jazmin Schwartz, Tahir I Yusufaly, Tyler J Bradshaw

Version 0.3.0-proposal. This handoff is a proposed additive dictionary extension, not an approved MIDRC release or a demonstrated drop-in deployment.

## Baseline and change boundary

The source is `https://data.midrc.org/api/v0/submission/_dictionary/_all`, retrieved 16 October 2026. Its version is `1.4.3-2-g7505333` and commit is `7505333d56c87a289463a814131e38d0f2be6674`. The exact bytes and SHA-256 are retained in `sources/` and `release_manifest.json`. The five user-supplied JSON templates are retained unchanged, with per-file audits in `uploaded_template_audit.json`.

The merged dictionary preserves all 29 baseline nodes, their existing required lists, system properties, definitions, link multiplicities, labels, backrefs and subgroup rules. Existing metadata and terminology annotations are untouched. The extension adds optional fields/links to 17 of those nodes and adds 38 new record types. Existing data are not required to populate theranostics additions. The 29 schema regression fixtures remain accepted by both baseline and merged schemas.

`midrc_additive_patch.json` contains only add operations. Its application to the exact baseline reproduces `gen3_dictionary.json`. Seven additions extend existing enums: RTDOSE on dicom_annotation_file.modality and two provisional annotation_name values on annotation, annotation_file and dicom_annotation_file. These names identify proposed annotation workflows, not NucLex concepts. They require receiving-team approval. The copied `_settings` records baseline provenance; the receiving build must generate its own release commit and version.

## Reuse decisions

| Earlier node or field | Version 0.3 home | Integration rule |
|---|---|---|
| imaging_series + image_file | pt_series_file, nm_series_file, ct_series_file, mr_series_file | Merge metadata by source linkage and modality; preserve distinct file objects, even when they share a SeriesInstanceUID. |
| PET vs planar/SPECT | PT vs NM file nodes | NM subtype is an added field. Do not submit PET modality under nm_series_file. |
| laboratory_result, roi_measurement, anthropometric_assessment | measurement | Use test_result_number once; add units, coded identity, source labels and collection/contour links. |
| lifestyle_assessment | observation | One dated observation. Baseline case smoking summaries and later observations must not overwrite each other. |
| segmentation | annotation | Keep persistent anatomic_target separate from each contour execution. Retain MIDRC annotation_method enum. |
| segmentation_file | dicom_annotation_file or annotation_file | DICOM SEG/RTSTRUCT vs supported non-DICOM mask artifact. |
| dose_map_file | dicom_annotation_file or supplementary_file | RTDOSE requires the proposed enum addition. Keep other-format artifacts on supplementary_file. |
| raw_imaging_file and clinical_document_file | supplementary_file | Indexed file metadata only. Use radiology_report for a structured radiology report when applicable. |
| PSA baseline/nadir values in response | referenced measurement | Role-specific links identify baseline and nadir; do not store a second numeric copy in response_assessment. |

Existing MIDRC measurement.test_name, measurement.test_method and procedure.procedure_name enums retain their original allowed values. Added coded/source identity fields support theranostics values outside those enums. Do not coerce PSA into a COVID test-name value or silently replace a restricted enum with an unrestricted string. Reference MIDRC definitions for shared geometry fields: PT slice_thickness and CT/MR pixel_spacing remain arrays of numbers. A source value with uncertain modality or tag context is retained explicitly as a source value pending adjudication.

## Relationship and record rules

Links point from a submitted record to a parent/evidence record. Backrefs permit reverse traversal. Shared baseline links are unchanged. New backrefs have explicit `nmmi_` prefixes to avoid collisions. The model graph is acyclic; acquisition and processing runs reference image artifacts. Image files do not acquire back-links to processing runs that would introduce type cycles. The standalone graph and table outputs come from the same schemas.

PT/NM file nodes retain a required, nonexclusive link subgroup: at least one of core_metadata_collections or imaging_studies. The theranostics profile requires imaging_studies for patient-linked imaging. Both links may be present. A profile is a collection-specific requirement and does not silently strengthen the baseline schema for all MIDRC users. Annotation and measurement subgroup rules are similarly preserved. The validator checks group semantics and actual link multiplicity separately from JSON Schema.

Program/project/root administration is environment-specific. Programs and projects do not acquire invented submitter_id fields. Project references use code or UUID and program references use UUID as in the baseline. A case can belong to multiple datasets. An encounter is not a therapy cycle. Actual injections have one authoritative administration record; copied DICOM radiopharmaceutical text remains source-header metadata. Course start and MIDRC case.index_event are distinct anchors.

## Files supplied for implementation

All 67 schemas have portal-style JSON templates. Expanded copies of the five attached templates are named `submission_*_template_expanded.json` in this folder. The full expanded schemas are under `schemas/`. `yaml/` contains self-contained YAML equivalents for review; receiving developers may refactor them into shared definitions/terms according to repository conventions.

Remove `*` required-field markers before submitting a payload. Replace required nulls, drop unfilled optional values, and populate at least one member of every required subgroup. `scripts/prepare_record.py` performs marker and blank cleanup only; it does not populate missing values or bypass validation. Clean examples under `examples/by_node/` illustrate completed payload shapes.

The attached PT/NM templates included `urls`; the deployed node schemas do not. Expanded node templates follow the deployed definitions and omit urls. `indexd_file_manifest_template.json` illustrates a separate handoff for file registration. Confirm the actual receiving upload process and GUID assignment; a node object_id must resolve to the intended registered bytes. Do not use the synthetic hashes as upload metadata.

## Review and staging sequence

1. Confirm the receiving dictionary commit. Rebase/review each additive change if it differs from the pinned baseline.
2. Review node grains, enum additions, annotation names and the remaining overlap candidates. Approve collection-specific profiles and vocabulary governance.
3. Integrate the schemas into the receiving repository’s definitions/terms layout, generate its dictionary and data-model classes, and run that repository’s required tests.
4. Provision administrative project resources and run schema/migration checks in a staging environment. Existing MIDRC regression data must remain accepted.
5. Register test file objects through the actual upload/Indexd workflow. Submit records in dependency order and verify portal graph/table views, queries, backrefs and exports.
6. Exercise corrected/revised records, cross-patient linkage rejection, modality routing, missingness, dates and file access. Preserve model and terminology release provenance.
7. Review representative de-identified cases with the clinical and ontology teams before a release decision. Production rollout and any institutional arrangements require their own authorization.

## Validation boundary

Local tests pass for 67 Draft 4 schemas and the deployed Gen3 metaschema, baseline-preserving constraints, exact patch reproduction, 921 traced source entries, 67 templates, 122 invented patient records and 27 negative cases. The second-cycle dose example explicitly declares partial evidence, whereas the first-cycle lesion-dose example traces acquisitions and contours. The checks do not run a full clinical criteria engine or establish correct extraction from real DICOM/EHR data. A real Gen3 build, service ingestion, file indexing and authorization remain unverified here.

## Sources

- Gen3 dictionary and model: https://gen3.org/resources/user/dictionary/
- MIDRC portal: https://data.midrc.org/DD
- MIDRC repository and schema conventions: https://github.com/uc-cdis/midrc_dictionary
- The original attached templates and prior model sources remain unchanged under sources.
