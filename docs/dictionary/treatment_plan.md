# Treatment Plan (`treatment_plan`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Versioned physician-approved treatment intent or adaptation, with evidence links and planned activity.

| Attribute | Value |
| --- | --- |
| Record grain | One plan version |
| Category | `clinical` |
| Navigation group | Treatment |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/treatment_plan.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/treatment_plan.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_treatment_plan_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `therapy_courses` | [therapy_course](therapy_course.md) | `many_to_one` | Yes | `nmmi_treatment_plan_therapy_courses` | `related_to` |
| `therapy_cycles` | [therapy_cycle](therapy_cycle.md) | `many_to_one` | No | `nmmi_treatment_plan_therapy_cycles` | `related_to` |
| `response_assessments` | [response_assessment](response_assessment.md) | `many_to_many` | No | `nmmi_treatment_plan_response_assessments` | `informed_by` |
| `toxicity_events` | [toxicity_event](toxicity_event.md) | `many_to_many` | No | `nmmi_treatment_plan_toxicity_events` | `informed_by` |
| `organ_functions` | [organ_function](organ_function.md) | `many_to_many` | No | `nmmi_treatment_plan_organ_functions` | `informed_by` |
| `dose_summaries` | [dose_summary](dose_summary.md) | `many_to_many` | No | `nmmi_treatment_plan_dose_summaries` | `informed_by` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_treatment_plan_provenance_records` | `documented_by` |
| `eligibility_assessments` | [eligibility_assessment](eligibility_assessment.md) | `many_to_many` | No | `nmmi_treatment_plan_eligibility_assessments` | `informed_by` |
| `laboratory_measurements` | [measurement](measurement.md) | `many_to_many` | No | `nmmi_treatment_plan_laboratory_measurements` | `related_to` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"treatment_plan"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `planned_activity_gbq` | No | number | Planned therapeutic activity for the referenced cycle, distinct from measured delivered activity. | Minimum: <code>0</code> |
| `plan_version` | Yes | string | Version of treatment intent or adaptation. | — |
| `approval_status` | Yes | string | Human review state of this plan. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"clinician_approved"</code>, <code>"superseded"</code> |
| `rationale` | No | string | Clinical rationale for plan or modification. | — |
| `planned_interval_days` | No | number | Planned interval between administrations in days. | Minimum: <code>0</code> |
| `plan_datetime` | No | string | Date/time this plan version was recorded. | Format: <code>"date-time"</code> |
| `planning_reference_dose_gy` | No | number | Reference dose used in this plan, if any; not a model-imposed or universal PSMA-RPT tolerance limit. | Minimum: <code>0</code> |
| `planning_reference_source` | No | string | Source, context and applicability of a planning reference level. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `therapy_courses` | Yes | array of object | Link to therapy_course records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `therapy_cycles` | No | array of object | Link to therapy_cycle records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `response_assessments` | No | array of object | Link to response_assessment records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `toxicity_events` | No | array of object | Link to toxicity_event records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `organ_functions` | No | array of object | Link to organ_function records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `dose_summaries` | No | array of object | Link to dose_summary records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `eligibility_assessments` | No | array of object | References to eligibility_assessment records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `laboratory_measurements` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic treatment_plan records](../../extensions/lu177_psma/v0.3.0/examples/by_node/treatment_plan.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
