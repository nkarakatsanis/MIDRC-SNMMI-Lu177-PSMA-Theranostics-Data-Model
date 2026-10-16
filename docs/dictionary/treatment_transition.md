# Treatment transition (`treatment_transition`)

Release **0.3.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

A post-course therapy transition, retreatment, or a dated assessment that no subsequent therapy has yet occurred.

| Attribute | Value |
| --- | --- |
| Record grain | One transition or follow-up status assessment |
| Category | `clinical` |
| Navigation group | Longitudinal context |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/treatment_transition.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/treatment_transition.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_treatment_transition_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `prior_courses` | [therapy_course](therapy_course.md) | `many_to_one` | Yes | `nmmi_treatment_transition_prior_courses` | `follows` |
| `subsequent_courses` | [therapy_course](therapy_course.md) | `many_to_many` | No | `nmmi_treatment_transition_subsequent_courses` | `initiates` |
| `medications` | [medication](medication.md) | `many_to_many` | No | `nmmi_treatment_transition_medications` | `documents` |
| `treatment_decisions` | [treatment_decision](treatment_decision.md) | `many_to_many` | No | `nmmi_treatment_transition_treatment_decisions` | `motivated_by` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_treatment_transition_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"treatment_transition"</code> |
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
| `transition_type` | Yes | string | Kind of subsequent treatment or dated follow-up status. | Allowed values: <code>"subsequent_systemic_therapy"</code>, <code>"psma_rpt_retreatment"</code>, <code>"no_subsequent_therapy_observed"</code>, <code>"other"</code> |
| `transition_status` | Yes | string | Whether a transition is planned, occurred, or not yet observed. | Allowed values: <code>"planned"</code>, <code>"occurred"</code>, <code>"not_yet_observed"</code>, <code>"unknown"</code> |
| `post_lu177_therapy_received` | No | boolean | Indicates whether the patient received any subsequent anticancer therapy after completion or discontinuation of ¹⁷⁷Lu-PSMA RPT. Per PCWG3, all subsequent therapies must be recorded until death as they affect OS interpretation. | — |
| `retreatment_performed` | No | boolean | Dated status of retreatment performed. | — |
| `agent_name` | No | string | Name of the anticancer agent(s) administered after ¹⁷⁷Lu-PSMA RPT, recorded in order of administration. | — |
| `reason` | No | string | Reason for initiating subsequent anticancer therapy after ¹⁷⁷Lu-PSMA. | — |
| `start_date` | No | string | Date on which the first subsequent anticancer therapy was initiated after ¹⁷⁷Lu-PSMA RPT. | Format: <code>"date"</code> |
| `last_prior_administration_date` | No | string | Transition last prior administration date. | Format: <code>"date"</code> |
| `last_followup_date` | No | string | Transition last followup date. | Format: <code>"date"</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `prior_courses` | Yes | array of object | References to therapy_course records. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `subsequent_courses` | No | array of object | References to therapy_course records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `medications` | No | array of object | References to medication records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `treatment_decisions` | No | array of object | References to treatment_decision records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | References to provenance records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic treatment_transition records](../../extensions/lu177_psma/v0.3.0/examples/by_node/treatment_transition.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
