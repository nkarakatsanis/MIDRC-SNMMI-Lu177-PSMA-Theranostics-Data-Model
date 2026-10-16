# Supplementary File (`supplementary_file`)

Release **0.3.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Supplementary files associated with a study.

| Attribute | Value |
| --- | --- |
| Record grain | One MIDRC supplementary file record |
| Category | `data_file` |
| Navigation group | Governance |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/supplementary_file.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/supplementary_file.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_supplementary_file_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `core_metadata_collections` | [core_metadata_collection](core_metadata_collection.md) | `many_to_one` | No; group 1 | `supplementary_files` | `data_from` |
| `datasets` | [dataset](dataset.md) | `many_to_one` | No; group 1 | `supplementary_files` | `refers_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_supplementary_file_provenance_records` | `related_to` |
| `cases` | [case](case.md) | `many_to_one` | No | `nmmi_supplementary_file_cases` | `related_to` |

Group 1: **at least one populated member** among `core_metadata_collections`, `datasets`.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `data_category` | Yes | string | The text term describing the broad category that the supplementary file falls into. | — |
| `data_format` | Yes | string | The text term describing the file format of the supplementary file, for example, PDF, XLSX, JPEG, PNG, TSV, etc. | — |
| `data_type` | Yes | string | The type of supplementary file, for example, figures, tables, clinical data, notes, publications, summary statistics, etc. | — |
| `file_description` | No | string | Free text to expand upon details for this file | — |
| `file_name` | Yes | string | The name (or part of a name) of a file (of any type). | — |
| `file_size` | Yes | integer | The size of the data file (object) in bytes. | — |
| `md5sum` | Yes | string | The 128-bit hash value expressed as a 32 digit hexadecimal number used as a file's digital fingerprint. | Pattern: <code>"^[a-f0-9]{32}$"</code> |
| `object_id` | No | string | The GUID of the object in the index service. | — |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `sha256` | No | string | SHA-256 checksum of the immutable artifact. | Pattern: <code>"^[a-fA-F0-9]{64}$"</code> |
| `format_version` | No | string | Format or standard release, including PETSIRD version where relevant. | — |
| `deidentification_profile` | No | string | Profile used to de-identify file contents and metadata. | — |
| `raw_data_type` | No | string | PET list-mode, SPECT projection, planar projection, sinogram or other raw acquisition. | — |
| `petsird_version` | No | string | PETSIRD release for PET list-mode data, if used; do not assume applicability to all modalities. | — |
| `theranostics_file_role` | No | string | Role of this existing MIDRC file object in the theranostics workflow. | Allowed values: <code>"raw_acquisition"</code>, <code>"segmentation"</code>, <code>"dose_map"</code>, <code>"clinical_document"</code>, <code>"processing_parameters"</code>, <code>"other"</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `core_metadata_collections` | No | one or more of: array of object; object | The submitter_id or id of the core_metadata_collection to which the supplementary file belongs, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `datasets` | No | one or more of: array of object; object | The submitter_id or id of the dataset to which the supplementary file belongs, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `provenance_records` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `cases` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `error_type` | No | string (enumerated) | Type of error for the data file object. | Allowed values: <code>"file_size"</code>, <code>"file_format"</code>, <code>"md5sum"</code> |
| `file_state` | No | string (enumerated) | The current state of the data file object. | Allowed values: <code>"registered"</code>, <code>"uploading"</code>, <code>"uploaded"</code>, <code>"validating"</code>, <code>"validated"</code>, <code>"submitted"</code>, <code>"processing"</code>, <code>"processed"</code>, <code>"released"</code>, <code>"error"</code>; Default: <code>"registered"</code> |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic supplementary_file records](../../extensions/lu177_psma/v0.3.0/examples/by_node/supplementary_file.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
