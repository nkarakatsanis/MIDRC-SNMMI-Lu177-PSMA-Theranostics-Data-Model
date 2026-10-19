# Treatment decision (`treatment_decision`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

A dated clinician or multidisciplinary decision, including continuation, modification, completion or NLCB, with rationale and evidence.

| Attribute | Value |
| --- | --- |
| Record grain | One decision at a specified time |
| Category | `clinical` |
| Navigation group | Treatment |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/treatment_decision.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/treatment_decision.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_treatment_decision_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `therapy_courses` | [therapy_course](therapy_course.md) | `many_to_one` | Yes | `nmmi_treatment_decision_therapy_courses` | `belongs_to` |
| `therapy_cycles` | [therapy_cycle](therapy_cycle.md) | `many_to_one` | No | `nmmi_treatment_decision_therapy_cycles` | `informed_by` |
| `response_assessments` | [response_assessment](response_assessment.md) | `many_to_many` | No | `nmmi_treatment_decision_response_assessments` | `informed_by` |
| `toxicity_events` | [toxicity_event](toxicity_event.md) | `many_to_many` | No | `nmmi_treatment_decision_toxicity_events` | `informed_by` |
| `clinical_assessments` | [clinical_assessment](clinical_assessment.md) | `many_to_many` | No | `nmmi_treatment_decision_clinical_assessments` | `informed_by` |
| `organ_functions` | [organ_function](organ_function.md) | `many_to_many` | No | `nmmi_treatment_decision_organ_functions` | `informed_by` |
| `dose_summaries` | [dose_summary](dose_summary.md) | `many_to_many` | No | `nmmi_treatment_decision_dose_summaries` | `informed_by` |
| `patient_reported_outcomes` | [patient_reported_outcome](patient_reported_outcome.md) | `many_to_many` | No | `nmmi_treatment_decision_patient_reported_outcomes` | `informed_by` |
| `clinical_events` | [clinical_event](clinical_event.md) | `many_to_many` | No | `nmmi_treatment_decision_clinical_events` | `informed_by` |
| `procedures` | [procedure](procedure.md) | `many_to_many` | No | `nmmi_treatment_decision_procedures` | `informed_by` |
| `treatment_plans` | [treatment_plan](treatment_plan.md) | `many_to_many` | No | `nmmi_treatment_decision_treatment_plans` | `informed_by` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_treatment_decision_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"treatment_decision"</code> |
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
| `decision_type` | Yes | string | Decision made at this assessment; completion and NLCB are separate values. | Allowed values: <code>"start"</code>, <code>"continue"</code>, <code>"hold"</code>, <code>"modify"</code>, <code>"stop"</code>, <code>"complete_planned_course"</code>, <code>"nlcb"</code>, <code>"focal_therapy"</code>, <code>"retreat"</code>, <code>"other"</code> |
| `decision_datetime` | Yes | string | Date/time of decision, distinct from first progression and actual treatment administration. | Format: <code>"date-time"</code> |
| `rationale` | Yes | string | Documented rationale. | — |
| `decision_maker_role` | No | string | Documented decision maker role. | — |
| `benefit_assessment` | No | string | Documented benefit assessment. | — |
| `nlcb_reason` | No | string | Specific reason(s) why ¹⁷⁷Lu-PSMA RPT was ultimately discontinued, representing the No Longer Clinically Benefiting determination. More granular than Reason_For_Discontinuation_Lu177. | — |
| `nlcb_date` | No | string | Date of an explicit NLCB determination, not automatically the date of progression or planned completion. | Format: <code>"date"</code> |
| `continued_beyond_progression` | No | boolean | Indicates whether ¹⁷⁷Lu-PSMA RPT was continued after first documented biochemical or imaging progression, with rationale and subsequent benefit assessment. | — |
| `focal_therapy_for_oligoprogression` | No | boolean | Indicates whether focal therapy was delivered for oligoprogressive disease while systemic ¹⁷⁷Lu-PSMA RPT benefit was considered ongoing. | — |
| `dose_limiting_organ` | No | string | Organ identified in the recorded treatment-modification decision. Not an outcome or a universal tolerance rule. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `therapy_courses` | Yes | array of object | References to therapy_course records. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `therapy_cycles` | No | array of object | References to therapy_cycle records. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `response_assessments` | No | array of object | References to response_assessment records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `toxicity_events` | No | array of object | References to toxicity_event records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `clinical_assessments` | No | array of object | References to clinical_assessment records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `organ_functions` | No | array of object | References to organ_function records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `dose_summaries` | No | array of object | References to dose_summary records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `patient_reported_outcomes` | No | array of object | References to patient_reported_outcome records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `clinical_events` | No | array of object | References to clinical_event records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `procedures` | No | array of object | References to procedure records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `treatment_plans` | No | array of object | References to treatment_plan records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
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

[Read the synthetic treatment_decision records](../../extensions/lu177_psma/v0.3.0/examples/by_node/treatment_decision.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
