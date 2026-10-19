# Reconstruction (`reconstruction`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

One reconstruction or processing execution with software version and input data.

| Attribute | Value |
| --- | --- |
| Record grain | One execution |
| Category | `analysis` |
| Navigation group | Imaging |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/reconstruction.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/reconstruction.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_reconstruction_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `acquisitions` | [acquisition](acquisition.md) | `many_to_one` | Yes | `nmmi_reconstruction_acquisitions` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_reconstruction_provenance_records` | `documented_by` |
| `raw_files` | [supplementary_file](supplementary_file.md) | `many_to_many` | No | `nmmi_reconstruction_raw_files` | `related_to` |
| `output_pt_series_files` | [pt_series_file](pt_series_file.md) | `many_to_many` | No | `nmmi_reconstruction_output_pt_series_files` | `related_to` |
| `output_nm_series_files` | [nm_series_file](nm_series_file.md) | `many_to_many` | No | `nmmi_reconstruction_output_nm_series_files` | `related_to` |
| `output_ct_series_files` | [ct_series_file](ct_series_file.md) | `many_to_many` | No | `nmmi_reconstruction_output_ct_series_files` | `related_to` |
| `output_mr_series_files` | [mr_series_file](mr_series_file.md) | `many_to_many` | No | `nmmi_reconstruction_output_mr_series_files` | `related_to` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"reconstruction"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `algorithm` | No | string | Reconstruction algorithm. | — |
| `software_name` | No | string | Method or version for software name. | — |
| `software_version` | No | string | Method or version for software version. | — |
| `parameter_file_reference` | No | string | Method or version for parameter file reference. | — |
| `attenuation_correction` | No | string | Method or version for attenuation correction. | — |
| `scatter_correction` | No | string | Method or version for scatter correction. | — |
| `decay_correction` | No | string | Method or version for decay correction. | — |
| `normalization_method` | No | string | Method or version for normalization method. | — |
| `iterations` | No | integer | Number of iterations. | Minimum: <code>1</code> |
| `subsets` | No | integer | Number of subsets. | Minimum: <code>1</code> |
| `psf_used` | No | boolean | Whether psf used in reconstruction. | — |
| `tof_used` | No | boolean | Whether tof used in reconstruction. | — |
| `reconstruction_diameter` | No | number | Provisional field for Reconstruction Diameter; operational definition requires review. | — |
| `decay_factor` | No | number | Provisional field for Decay Factor; operational definition requires review. | — |
| `rescale_slope` | No | number | Provisional field for Rescale Slope; operational definition requires review. | — |
| `rescale_intercept` | No | number | Provisional field for Rescale Intercept; operational definition requires review. | — |
| `scatter_fraction_factor` | No | number | Provisional field for Scatter Fraction Factor; operational definition requires review. | — |
| `dead_time_factor` | No | number | Provisional field for Dead Time Factor; operational definition requires review. | — |
| `corrected_image` | No | string | Provisional field for Corrected Image; operational definition requires review. | — |
| `randoms_correction_method` | No | string | Provisional field for Randoms Correction Method; operational definition requires review. | — |
| `filter_type` | No | string | Provisional field for Filter Type; operational definition requires review. | — |
| `applied_corrections` | No | string | Provisional field for Applied Corrections; operational definition requires review. | — |
| `reconstruction_field_of_view` | No | string | Provisional field for Reconstruction Field of View; operational definition requires review. | — |
| `pet_reconstruction_sequence` | No | string | Provisional field for PET Reconstruction Sequence; operational definition requires review. | — |
| `source_section_note_4_reconstruction_parameters` | No | string | Provisional field for 4. Reconstruction Parameters; operational definition requires review. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `acquisitions` | Yes | array of object | Link to acquisition records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `raw_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `output_pt_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `output_nm_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `output_ct_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `output_mr_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic reconstruction records](../../extensions/lu177_psma/v0.3.0/examples/by_node/reconstruction.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
