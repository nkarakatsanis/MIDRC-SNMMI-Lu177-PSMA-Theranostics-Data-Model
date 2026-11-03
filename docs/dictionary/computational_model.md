# Computational Model (`computational_model`)

Release **0.4.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

One versioned computational model specification, independent of any execution or prediction.

| Attribute | Value |
| --- | --- |
| Record grain | One versioned computational model specification, independent of any execution or prediction. |
| Category | `administrative` |
| Navigation group | Digital twin research |
| MIDRC relationship | `new_extension` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.4.0/schemas/computational_model.json) · [YAML schema](../../extensions/lu177_psma/v0.4.0/integration/yaml/computational_model.yaml) · [Submission template](../../extensions/lu177_psma/v0.4.0/templates/submission_computational_model_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `nmmi_computational_model_projects` | `member_of` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_computational_model_provenance_records` | `documented_by` |
| `reference_evidence` | [reference_evidence](reference_evidence.md) | `many_to_many` | No | `nmmi_computational_model_reference_evidence` | `supported_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"computational_model"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `model_name` | Yes | string | Name of the computational model. | Minimum length: <code>1</code> |
| `model_release` | Yes | string | Exact model/software release; independent of the data-model version. | Minimum length: <code>1</code> |
| `model_kind` | Yes | string (enumerated) | Computational model family; does not assert clinical validation. | Allowed values: <code>"compartmental"</code>, <code>"PBPK"</code>, <code>"voxel_dosimetry"</code>, <code>"tumor_control"</code>, <code>"toxicity"</code>, <code>"AI"</code>, <code>"other"</code> |
| `artifact_uri` | No | string | Location of model code or weights. | Minimum length: <code>1</code> |
| `artifact_sha256` | No | string | SHA-256 digest of the exact code or weight artifact, if available. | Minimum length: <code>1</code> |
| `scope` | Yes | string | Intended subject, population, organ or molecular scope. | Minimum length: <code>1</code> |
| `input_requirements` | Yes | string | Required imaging, clinical, treatment-history and other inputs with units and timing conventions. | Minimum length: <code>1</code> |
| `output_definition` | Yes | string | Predicted quantities and their definitions and units. | Minimum length: <code>1</code> |
| `applicability_limits` | No | string | Disease, population and acquisition settings in which use is justified by evidence. | Minimum length: <code>1</code> |
| `known_failure_modes` | No | string | Known failure modes, including domain shift and missing inputs. | Minimum length: <code>1</code> |
| `identifiability_assessment` | No | string | Parameter identifiability assessment and method. | Minimum length: <code>1</code> |
| `human_oversight` | Yes | string | Required human review and intended research or clinical use constraints. | Minimum length: <code>1</code> |
| `validation_status` | Yes | string (enumerated) | Evidence status; not a certification or universal claim of safety. | Allowed values: <code>"unvalidated"</code>, <code>"internal_evaluation"</code>, <code>"external_evaluation"</code>, <code>"reviewed_for_specified_use"</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | array of object | Link to project records by code or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"code"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `reference_evidence` | No | array of object | Link to reference_evidence records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic computational_model records](../../extensions/lu177_psma/v0.4.0/examples/by_node/computational_model.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
