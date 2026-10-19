# Procedure (`procedure`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Activities or processes ordered by and/or carried out by a healthcare provider on the patient with diagnostic and/or therapeutic purposes.

| Attribute | Value |
| --- | --- |
| Record grain | One intervention or source summary |
| Category | `medical_history` |
| Navigation group | Clinical |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/procedure.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/procedure.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_procedure_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `conditions` | [condition](condition.md) | `many_to_one` | No; group 1 | `procedures` | `related_to` |
| `cases` | [case](case.md) | `many_to_one` | Yes; group 1 | `procedures` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_procedure_provenance_records` | `documented_by` |
| `anatomic_targets` | [anatomic_target](anatomic_target.md) | `many_to_many` | No | `nmmi_procedure_anatomic_targets` | `treats` |
| `therapy_courses` | [therapy_course](therapy_course.md) | `many_to_one` | No | `nmmi_procedure_therapy_courses` | `supported_by` |

Group 1: **at least one populated member** among `conditions`, `cases`.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `breathing_support_type` | No | string | The type of breathing support the patient received. | — |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `days_to_procedure_end` | No | integer | The number of days between the case's index date and the end date of the procedure. | — |
| `days_to_procedure_start` | No | integer | The number of days between the case's index date and the start date of the procedure. | — |
| `history_of_radiation` | No | string (enumerated) | An indicator confirming a history of radiation. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `procedure_name` | No | string (enumerated) | The name of the procedure performed. | Allowed values: <code>"Breathing Support"</code>, <code>"Radiation (Chest)"</code>; Source term: NCIt; C201325; Procedure Name |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `prior_radiotherapy_prostate` | No | boolean | History of radiotherapy to the prostate or pelvis. | — |
| `prior_radiotherapy_metastases` | No | boolean | History of radiotherapy to metastatic sites. | — |
| `prior_radiotherapy_site_list` | No | array of string | List of anatomical sites that received prior radiation therapy. | — |
| `prior_radiotherapy_summary` | No | string | Free text field to summarize key details of prior radiation, such as completion dates, total doses if available, especially if complex. | — |
| `prior_radiotherapy_type` | No | array of string | Type of radiation therapy delivered (e.g., EBRT, IMRT, SBRT, Brachytherapy). May vary by site. | — |
| `prior_surgery` | No | boolean | Specifies if the patient had prior surgery related to prostate cancer. | — |
| `prior_surgery_date` | No | string | Date(s) when prior prostate cancer-related surgery was performed. | — |
| `prior_surgery_type` | No | array of string | Type(s) of prior surgeries performed for prostate cancer. | — |
| `surgical_method` | No | string | Provisional field for surgical method; operational definition requires review. | — |
| `rt_method` | No | string | Provisional field for RT method; operational definition requires review. | — |
| `procedure_date` | No | string | Date of the actual intervention. | Format: <code>"date"</code> |
| `method` | No | string | Intervention method or modality. | — |
| `procedure_name_source_value` | No | string | Source procedure label when absent from the existing MIDRC procedure_name enumeration; use coded identity where available. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | Yes | one or more of: array of object; object | The submitter_id or id of the case to which this procedure is related, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `conditions` | No | one or more of: array of object; object | The submitter_id or id of the condition to which this procedure is related, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `provenance_records` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `anatomic_targets` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `therapy_courses` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic procedure records](../../extensions/lu177_psma/v0.3.0/examples/by_node/procedure.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
