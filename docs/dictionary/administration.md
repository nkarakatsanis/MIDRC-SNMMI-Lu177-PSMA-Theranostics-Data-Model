# Administration (`administration`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

An actual diagnostic or therapeutic radiopharmaceutical administration, with measured activity, reference time and residual correction.

| Attribute | Value |
| --- | --- |
| Record grain | One actual administration event |
| Category | `clinical` |
| Navigation group | Treatment |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/administration.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/administration.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_administration_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `cases` | [case](case.md) | `many_to_one` | Yes | `nmmi_administration_cases` | `related_to` |
| `radiopharmaceuticals` | [radiopharmaceutical](radiopharmaceutical.md) | `many_to_one` | Yes | `nmmi_administration_radiopharmaceuticals` | `related_to` |
| `radiopharmaceutical_batches` | [radiopharmaceutical_batch](radiopharmaceutical_batch.md) | `many_to_one` | No | `nmmi_administration_radiopharmaceutical_batches` | `related_to` |
| `therapy_cycles` | [therapy_cycle](therapy_cycle.md) | `many_to_one` | No | `nmmi_administration_therapy_cycles` | `related_to` |
| `visits` | [visit](visit.md) | `many_to_one` | No | `nmmi_administration_visits` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_administration_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"administration"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `administration_purpose` | Yes | string | Purpose distinguishes treatment administration from tracer injection. | Allowed values: <code>"therapy"</code>, <code>"diagnostic"</code>, <code>"other"</code> |
| `administration_datetime` | No | string | Administration start datetime with timezone; apply common shift within patient if de-identified. | Format: <code>"date-time"</code> |
| `administered_activity_mbq` | Yes | number | Net measured activity delivered, decay-referenced to activity_reference_datetime. | Minimum: <code>0</code> |
| `activity_reference_datetime` | Yes | string | Datetime to which net delivered activity is decay corrected. | Format: <code>"date-time"</code> |
| `pre_injection_activity_mbq` | No | number | Pre-injection activity at its recorded measurement time. | Minimum: <code>0</code> |
| `residual_activity_mbq` | No | number | Residual activity at its recorded measurement time. | Minimum: <code>0</code> |
| `pre_measurement_datetime` | No | string | Measurement datetime; do not subtract activities measured at different reference times without decay correction. | Format: <code>"date-time"</code> |
| `residual_measurement_datetime` | No | string | Measurement datetime; do not subtract activities measured at different reference times without decay correction. | Format: <code>"date-time"</code> |
| `residual_correction_method` | No | string | How residual and delivery losses were handled. | — |
| `route` | No | string | Administration route. | — |
| `activity_meter_identifier` | No | string | Activity meter identifier; calibration provenance must be traceable. | — |
| `activity_measurement_container` | No | string | Vial or syringe material and geometry used for activity measurement. | — |
| `administration_date` | No | string | Date the specific Lu-177 PSMA therapy cycle was administered. | Format: <code>"date"</code> |
| `dicom_start_time` | No | string | Provisional field for Radiopharmaceutical Start Time; operational definition requires review. | — |
| `dicom_stop_time` | No | string | Provisional field for Radiopharmaceutical Stop Time; operational definition requires review. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | Yes | array of object | Link to case records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `radiopharmaceuticals` | Yes | array of object | Link to radiopharmaceutical records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `radiopharmaceutical_batches` | No | array of object | Link to radiopharmaceutical_batch records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `therapy_cycles` | No | array of object | Link to therapy_cycle records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `visits` | No | array of object | Link to visit records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic administration records](../../extensions/lu177_psma/v0.3.0/examples/by_node/administration.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
