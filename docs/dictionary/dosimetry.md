# Dosimetry (`dosimetry`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Dosimetry computation with inputs, integration method, mass model, uncertainty and software version.

| Attribute | Value |
| --- | --- |
| Record grain | One calculation run for a cycle or administration |
| Category | `analysis` |
| Navigation group | Quantification |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/dosimetry.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/dosimetry.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_dosimetry_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `therapy_cycles` | [therapy_cycle](therapy_cycle.md) | `many_to_one` | Yes | `nmmi_dosimetry_therapy_cycles` | `related_to` |
| `administrations` | [administration](administration.md) | `many_to_many` | No | `nmmi_dosimetry_administrations` | `related_to` |
| `time_activity_curves` | [time_activity_curve](time_activity_curve.md) | `many_to_many` | No | `nmmi_dosimetry_time_activity_curves` | `derived_from` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_dosimetry_provenance_records` | `documented_by` |
| `acquisitions` | [acquisition](acquisition.md) | `many_to_many` | No | `nmmi_dosimetry_acquisitions` | `derived_from` |
| `pt_series_files` | [pt_series_file](pt_series_file.md) | `many_to_many` | No | `nmmi_dosimetry_pt_series_files` | `related_to` |
| `nm_series_files` | [nm_series_file](nm_series_file.md) | `many_to_many` | No | `nmmi_dosimetry_nm_series_files` | `related_to` |
| `ct_series_files` | [ct_series_file](ct_series_file.md) | `many_to_many` | No | `nmmi_dosimetry_ct_series_files` | `related_to` |
| `mr_series_files` | [mr_series_file](mr_series_file.md) | `many_to_many` | No | `nmmi_dosimetry_mr_series_files` | `related_to` |
| `annotations` | [annotation](annotation.md) | `many_to_many` | No | `nmmi_dosimetry_annotations` | `related_to` |
| `dose_maps` | [dicom_annotation_file](dicom_annotation_file.md) | `many_to_many` | No | `nmmi_dosimetry_dose_maps` | `related_to` |
| `non_dicom_dose_maps` | [supplementary_file](supplementary_file.md) | `many_to_many` | No | `nmmi_dosimetry_non_dicom_dose_maps` | `related_to` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"dosimetry"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `method` | No | string | Dosimetry method. | — |
| `software_name` | No | string | Dosimetry software name. | — |
| `software_version` | No | string | Dosimetry software version. | — |
| `mass_model` | No | string | Dosimetry mass model. | — |
| `model_assumptions` | No | string | Dosimetry model assumptions. | — |
| `uncertainty_method` | No | string | Dosimetry uncertainty method. | — |
| `calculation_datetime` | No | string | Calculation timestamp. | Format: <code>"date-time"</code> |
| `dosimetry_ad_calculation_granularity` | No | integer | Specifies the level of detail for dosimetry computation, such as voxel-based or organ-based. | — |
| `dosimetry_ad_calculation_method` | No | integer | The class of computational method used to calculate absorbed dose to regions of interest. | — |
| `dosimetry_ad_tiac_fitting_method_for_roi` | No | integer | The type of curve fitting that is applied to calculate the time-integrated activity curve for a given ROI. | — |
| `dosimetry_software` | No | string | The software or library used to calculate absorbed dose values for dosimetry. | — |
| `dosimetry_software_version` | No | string | The version of the software or library used to calculate absorbed dose values for dosimetry. | — |
| `dosimetry_imaging_modality` | No | integer | Imaging modality used for dosimetry (e.g., SPECT/CT, scintigraphy). | — |
| `dosimetry_performed` | No | boolean | Indicates if dosimetry calculations were performed for this patient. | — |
| `dosimetry_timepoints` | No | string | Timepoints post-injection when dosimetry imaging was acquired. | — |
| `equivalent_dose` | No | string | Accounts for the different biological effects of various types of radiation. Measured in sieverts (Sv) or rem | — |
| `effective_dose` | No | string | Considers the radiation sensitivity of different tissues and organs, providing an overall risk estimate. Measured in sieverts (Sv). | — |
| `kerma` | No | string | Kinetic energy released in matter per unit mass. Measured in grays (Gy) | — |
| `evidence_completeness` | No | string | Declared completeness of acquisition and contour provenance for this calculation run. | Allowed values: <code>"complete"</code>, <code>"partial"</code>, <code>"unavailable"</code> |
| `missing_evidence_reason` | No | string | Reason acquisition or contour provenance is incomplete; never infer missing evidence from a different cycle. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `therapy_cycles` | Yes | array of object | Link to therapy_cycle records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `administrations` | No | array of object | Link to administration records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `time_activity_curves` | No | array of object | Link to time_activity_curve records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `acquisitions` | No | array of object | References to acquisition records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `pt_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `nm_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `ct_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `mr_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `annotations` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `dose_maps` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `non_dicom_dose_maps` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic dosimetry records](../../extensions/lu177_psma/v0.3.0/examples/by_node/dosimetry.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
