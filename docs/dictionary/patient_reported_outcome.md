# Patient Reported Outcome (`patient_reported_outcome`)

Release **0.3.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Patient-reported pain, quality of life or functional assessment with instrument and scoring context.

| Attribute | Value |
| --- | --- |
| Record grain | One instrument and assessment time |
| Category | `clinical` |
| Navigation group | Outcomes |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/patient_reported_outcome.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/patient_reported_outcome.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_patient_reported_outcome_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `therapy_courses` | [therapy_course](therapy_course.md) | `many_to_one` | Yes | `nmmi_patient_reported_outcome_therapy_courses` | `related_to` |
| `timepoints` | [timepoint](timepoint.md) | `many_to_one` | No | `nmmi_patient_reported_outcome_timepoints` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_patient_reported_outcome_provenance_records` | `documented_by` |
| `analgesic_medications` | [medication](medication.md) | `many_to_many` | No | `nmmi_patient_reported_outcome_analgesic_medications` | `contextualized_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"patient_reported_outcome"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `assessment_datetime` | No | string | ISO 8601 assessment datetime; use approved date shifting consistently within the case. | Format: <code>"date-time"</code> |
| `days_from_course_start` | No | number | Signed elapsed days from the linked therapy course start. | — |
| `time_basis` | No | string | Interpretation of stored dates and elapsed times. | Allowed values: <code>"actual"</code>, <code>"shifted"</code>, <code>"relative_only"</code>, <code>"unknown"</code> |
| `time_window_start_day` | No | number | Beginning of assessment window relative to course start, in days. | — |
| `time_window_end_day` | No | number | End of assessment window relative to course start, in days. | — |
| `instrument_name` | No | string | Patient-reported outcome instrument name. | — |
| `instrument_version` | No | string | Patient-reported outcome instrument version. | — |
| `score_domain` | No | string | Patient-reported outcome score domain. | — |
| `scoring_method` | No | string | Patient-reported outcome scoring method. | — |
| `score` | No | number | Numeric score, with range specified by instrument. | — |
| `qol_assessment_date` | No | string | Date the Quality of Life questionnaire was completed. | Format: <code>"date"</code> |
| `qol_instrument_used` | No | string | Name of the Quality of Life questionnaire used (e.g., EORTC QLQ-C30, FACT-P). | — |
| `qol_score` | No | number or string | Overall or specific domain score from the QoL assessment. | — |
| `pro_ctcae_collected` | No | boolean | Indicates whether patient-reported adverse events were collected using the NCI Patient-Reported Outcomes version of the Common Terminology Criteria for Adverse Events (PRO-CTCAE), as recommended by PCWG3 for both early- and late-phase trials. | — |
| `quality_of_life` | No | string | Provisional field for Quality of LIfe; operational definition requires review. | — |
| `assessment_role` | No | string | Patient-reported assessment role. | — |
| `instrument_language` | No | string | Patient-reported instrument language. | — |
| `respondent` | No | string | Patient-reported respondent. | — |
| `recall_period` | No | string | Patient-reported recall period. | — |
| `item_code` | No | string | Patient-reported item code. | — |
| `item_attribute` | No | string | Patient-reported item attribute. | — |
| `score_unit` | No | string | Patient-reported score unit. | — |
| `response_value` | No | string | Original instrument/item response category, retaining PRO-CTCAE frequency, severity or interference as applicable. | — |
| `baseline_averaging_days` | No | integer | Number of days contributing to a baseline average. | Minimum: <code>1</code> |
| `opioid_use` | No | boolean | Indicates whether the patient is using opioid analgesics at the time of follow-up pain assessment. | — |
| `opioid_daily_ome_mg` | No | number | Recorded daily oral morphine equivalent dose when a documented conversion method is available. | Minimum: <code>0</code> |
| `opioid_conversion_method` | No | string | Conversion source/version or explanation of direct equivalence; not calculated by this model. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `therapy_courses` | Yes | array of object | Link to therapy_course records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `timepoints` | No | array of object | Link to timepoint records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `analgesic_medications` | No | array of object | References to medication records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic patient_reported_outcome records](../../extensions/lu177_psma/v0.3.0/examples/by_node/patient_reported_outcome.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
