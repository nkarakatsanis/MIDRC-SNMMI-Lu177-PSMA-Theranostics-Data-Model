# Preparation Event (`preparation_event`)

Release **0.4.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

One actual production, compounding, reconstitution or dilution event with specified inputs and output batch.

| Attribute | Value |
| --- | --- |
| Record grain | One actual production, compounding, reconstitution or dilution event with specified inputs and output batch. |
| Category | `clinical` |
| Navigation group | Radiopharmaceutical manufacture |
| MIDRC relationship | `new_extension` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.4.0/schemas/preparation_event.json) · [YAML schema](../../extensions/lu177_psma/v0.4.0/integration/yaml/preparation_event.yaml) · [Submission template](../../extensions/lu177_psma/v0.4.0/templates/submission_preparation_event_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `nmmi_preparation_event_projects` | `member_of` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_preparation_event_provenance_records` | `documented_by` |
| `input_material_lots` | [material_lot](material_lot.md) | `many_to_many` | No | `nmmi_preparation_event_input_material_lots` | `uses_input` |
| `input_batches` | [radiopharmaceutical_batch](radiopharmaceutical_batch.md) | `many_to_many` | No | `nmmi_preparation_event_input_batches` | `uses_input` |
| `output_batches` | [radiopharmaceutical_batch](radiopharmaceutical_batch.md) | `many_to_one` | Yes | `nmmi_preparation_event_output_batches` | `produces` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"preparation_event"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `event_kind` | Yes | string (enumerated) | Executed preparation activity; dispensing and administration have separate records. | Allowed values: <code>"production"</code>, <code>"compounding"</code>, <code>"reconstitution"</code>, <code>"dilution"</code>, <code>"other"</code> |
| `recipe_name` | Yes | string | Executed recipe or SOP name. | Minimum length: <code>1</code> |
| `recipe_version` | Yes | string | Version of the executed recipe or SOP. | Minimum length: <code>1</code> |
| `started_datetime` | No | string | Start timestamp with UTC offset. | Format: <code>"date-time"</code>; Minimum length: <code>1</code> |
| `completed_datetime` | Yes | string | Completion timestamp with UTC offset, including end-of-synthesis when applicable. | Format: <code>"date-time"</code>; Minimum length: <code>1</code> |
| `site_name` | No | string | Manufacturing or preparation site identity without patient identifiers. | Minimum length: <code>1</code> |
| `gmp_status` | No | string | Source-reported GMP status with governing evidence in provenance; not an inferred certification. | Minimum length: <code>1</code> |
| `execution_mode` | No | string (enumerated) | Mode of execution. | Allowed values: <code>"automated"</code>, <code>"manual"</code>, <code>"hybrid"</code>, <code>"unknown"</code> |
| `instrument_name` | No | string | Synthesis module or preparation instrument. | Minimum length: <code>1</code> |
| `reaction_conditions` | No | string | Executed temperature, time, pH and other conditions with units or an SOP reference. | Minimum length: <code>1</code> |
| `purification_method` | No | string | Executed purification method and version. | Minimum length: <code>1</code> |
| `deviation_description` | No | string | Recorded deviation and its disposition; no deviation is inferred from missing data. | Minimum length: <code>1</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | array of object | Link to project records by code or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"code"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `input_material_lots` | No | array of object | Link to material_lot records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `input_batches` | No | array of object | Link to radiopharmaceutical_batch records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `output_batches` | Yes | array of object | Link to radiopharmaceutical_batch records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic preparation_event records](../../extensions/lu177_psma/v0.4.0/examples/by_node/preparation_event.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
