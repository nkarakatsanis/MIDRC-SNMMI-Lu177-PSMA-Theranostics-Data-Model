# Survival Outcome (`survival_outcome`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Time-to-event result with explicit origin, event definition, event indicator and censoring date.

| Attribute | Value |
| --- | --- |
| Record grain | One endpoint definition per case and course |
| Category | `clinical` |
| Navigation group | Outcomes |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/survival_outcome.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/survival_outcome.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_survival_outcome_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `therapy_courses` | [therapy_course](therapy_course.md) | `many_to_one` | Yes | `nmmi_survival_outcome_therapy_courses` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_survival_outcome_provenance_records` | `documented_by` |
| `response_assessments` | [response_assessment](response_assessment.md) | `many_to_many` | No | `nmmi_survival_outcome_response_assessments` | `event_supported_by` |
| `clinical_events` | [clinical_event](clinical_event.md) | `many_to_many` | No | `nmmi_survival_outcome_clinical_events` | `event_supported_by` |
| `treatment_transitions` | [treatment_transition](treatment_transition.md) | `many_to_many` | No | `nmmi_survival_outcome_treatment_transitions` | `event_supported_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"survival_outcome"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `endpoint_name` | Yes | string | Endpoint endpoint name. | — |
| `endpoint_definition` | Yes | string | Endpoint endpoint definition. | — |
| `time_origin_definition` | Yes | string | Endpoint time origin definition. | — |
| `event_definition` | Yes | string | Endpoint event definition. | — |
| `censoring_reason` | No | string | Endpoint censoring reason. | — |
| `origin_date` | No | string | Date used for endpoint origin date. | Format: <code>"date"</code> |
| `event_date` | No | string | Date used for endpoint event date. | Format: <code>"date"</code> |
| `censor_date` | No | string | Date used for endpoint censor date. | Format: <code>"date"</code> |
| `event_observed` | Yes | boolean | True for qualifying event, false for censored follow-up. | — |
| `duration_days` | No | number | Calculated follow-up duration from defined origin to event or censor date. | Minimum: <code>0</code> |
| `months_conversion` | No | string | Rule converting days to months for reported month-based results. | — |
| `date_of_death` | No | string | Patient's date of death, if applicable. | Format: <code>"date"</code> |
| `efs` | No | number | Time from Lu-177 PSMA therapy start absent of any adverse events | — |
| `last_followup_date` | No | string | Date of the patient's last contact or information update. | Format: <code>"date"</code> |
| `os_months` | No | number | Time from Lu-177 PSMA therapy start to death from any cause, in months. | — |
| `pfs_months` | No | number | Time from Lu-177 PSMA therapy start to progression or death, in months. | — |
| `rpfs_months` | No | number | Time from Lu-177 PSMA therapy start to radiographic progression or death, in months. | — |
| `duration_months` | No | number | Reported endpoint duration in months, with explicit conversion convention and event/censor data. | Minimum: <code>0</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `therapy_courses` | Yes | array of object | Link to therapy_course records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `response_assessments` | No | array of object | References to response_assessment records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `clinical_events` | No | array of object | References to clinical_event records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `treatment_transitions` | No | array of object | References to treatment_transition records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic survival_outcome records](../../extensions/lu177_psma/v0.3.0/examples/by_node/survival_outcome.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
