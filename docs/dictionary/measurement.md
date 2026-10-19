# Measurement (`measurement`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

A structured value (numerical or categorical) obtained through systematic examination of a person or sample.

| Attribute | Value |
| --- | --- |
| Record grain | One measured value with context; lab, ROI and anthropometric profiles |
| Category | `medical_history` |
| Navigation group | Clinical |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/measurement.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/measurement.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_measurement_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `conditions` | [condition](condition.md) | `many_to_one` | No; group 1 | `measurements` | `related_to` |
| `procedures` | [procedure](procedure.md) | `many_to_one` | No; group 1 | `measurements` | `related_to` |
| `cases` | [case](case.md) | `many_to_one` | No; group 1 | `measurements` | `related_to` |
| `laboratory_panels` | [laboratory_panel](laboratory_panel.md) | `many_to_one` | No | `nmmi_measurement_laboratory_panels` | `related_to` |
| `annotations` | [annotation](annotation.md) | `many_to_many` | No | `nmmi_measurement_annotations` | `related_to` |
| `anatomic_targets` | [anatomic_target](anatomic_target.md) | `many_to_one` | No | `nmmi_measurement_anatomic_targets` | `related_to` |
| `timepoints` | [timepoint](timepoint.md) | `many_to_many` | No | `nmmi_measurement_timepoints` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_measurement_provenance_records` | `related_to` |

Group 1: **at least one populated member** among `conditions`, `procedures`, `cases`.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `home_oxygen_use` | No | string (enumerated) | An indicator confirming whether home oxygen is used. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `oxygenation_measurement_environment` | No | string (enumerated) | The environment in which the oxygenation test was performed. | Allowed values: <code>"Room air"</code>, <code>"Supplmental Oxygen"</code>, <code>"Not Reported"</code> |
| `pulmonary_function_test` | No | string (enumerated) | An indicator confirming whether a pulmonary function test was performed. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `six_minute_walk_test` | No | string (enumerated) | An indicator confirming whether the patient completed the 6 Minute Walk Test (6MWT). | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `test_days_from_index` | No | integer | A number of days beginning with the index date and ending with the date of the test. | — |
| `test_method` | No | string (enumerated) | The test method used to confirm a condition or produce a measurement. | Allowed values: <code>"RT-PCR"</code>, <code>"Rapid antigen test"</code>, <code>"Not Reported"</code>; Source term: NCIt; C82535; Test Method |
| `test_name` | No | string (enumerated) | The name of the test for which this measurement was the result. | Allowed values: <code>"COVID-19"</code>, <code>"FVC (L)"</code>, <code>"FEV1 (L)"</code>, <code>"6-Minute Walk Test Distance"</code>, <code>"6-Minute Walk Test Exertional Drop in O2 (%)"</code>, <code>"Oxygenation (SpO2)"</code>, <code>"Home Oxygen Quantity"</code>; Source term: NCIt; C82541; Test Name |
| `test_result_number` | No | number | The result a test represented by a number. | — |
| `test_result_percent` | No | number | The result a test represented by a percent. | — |
| `test_result_ratio` | No | number | The result a test represented by a ratio. | — |
| `test_result_text` | No | string (enumerated) | The measured result of the test described using a list of enumerations. | Allowed values: <code>"Indeterminate"</code>, <code>"Negative"</code>, <code>"Positive"</code>, <code>"Not Reported"</code>; Source term: NCIt; C77140; Clinical Test Result |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `test_name_source_value` | No | string | Name of the measured laboratory analyte. Source field catalog and external dictionary define analyte-specific semantics. | — |
| `test_method_source_value` | No | string (enumerated) | The test method used to confirm a condition or produce a measurement. | Allowed values: <code>"RT-PCR"</code>, <code>"Rapid antigen test"</code>, <code>"Not Reported"</code>; Source term: NCIt; C82535; Test Method |
| `test_result_source_value` | No | string (enumerated) | The measured result of the test described using a list of enumerations. | Allowed values: <code>"Indeterminate"</code>, <code>"Negative"</code>, <code>"Positive"</code>, <code>"Not Reported"</code>; Source term: NCIt; C77140; Clinical Test Result |
| `unit` | No | string | Unit of the numeric test result. Use UCUM when validated. | — |
| `unit_source_value` | No | string | Original unit before harmonization. | — |
| `test_code` | No | string | Approved external analyte code such as LOINC, if mapped. | — |
| `test_code_system` | No | string | Code system for test_code. | — |
| `test_code_version` | No | string | Vocabulary release. | — |
| `result_status` | No | string | Status such as final, preliminary or corrected. | — |
| `specimen_type` | No | string | Specimen type when no specimen record is available. | — |
| `result_operator` | No | string | Comparator such as &lt;, &lt;=, =, &gt;= or &gt;. | — |
| `derived_formula` | No | string | Formula for eGFR or creatinine clearance, when applicable. | — |
| `reference_range_low` | No | number | Reference limit in the same unit as the reported test result. | — |
| `reference_range_high` | No | number | Reference limit in the same unit as the reported test result. | — |
| `source_element_id` | No | string | Field identifier from source_field_catalog.json; identifies source analyte definition. | — |
| `measurement_date` | No | string | Date the ROI measurement was performed. | Format: <code>"date"</code> |
| `measurement_profile` | No | string | Theranostics collection profile for an atomic measurement. | Allowed values: <code>"laboratory"</code>, <code>"roi"</code>, <code>"anthropometric"</code>, <code>"biomarker"</code>, <code>"other"</code> |
| `measurement_datetime` | No | string | Time of specimen collection or measurement; retain actual/shifted/relative-only basis. | Format: <code>"date-time"</code> |
| `days_from_course_start` | No | number | Elapsed days from the explicitly linked therapy-course start; distinct from MIDRC index-event time. | — |
| `time_basis` | No | string | Interpretation of stored dates and elapsed times. | Allowed values: <code>"actual"</code>, <code>"shifted"</code>, <code>"relative_only"</code>, <code>"unknown"</code> |
| `time_window_start_day` | No | number | Beginning of assessment window relative to course start, in days. | — |
| `time_window_end_day` | No | number | End of assessment window relative to course start, in days. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | No | one or more of: array of object; object | The submitter_id or id of the case(s) this measurement describes, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `conditions` | No | one or more of: array of object; object | The submitter_id or id of the condition this measurement describes, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `procedures` | No | one or more of: array of object; object | The submitter_id or id of the procedure this measurement describes, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `laboratory_panels` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `annotations` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `anatomic_targets` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `timepoints` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `provenance_records` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic measurement records](../../extensions/lu177_psma/v0.3.0/examples/by_node/measurement.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
