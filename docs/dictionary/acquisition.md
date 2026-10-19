# Acquisition (`acquisition`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Acquisition settings and timing for one series or frame group.

| Attribute | Value |
| --- | --- |
| Record grain | One acquisition settings block |
| Category | `clinical` |
| Navigation group | Imaging |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/acquisition.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/acquisition.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_acquisition_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `scanners` | [scanner](scanner.md) | `many_to_one` | Yes | `nmmi_acquisition_scanners` | `related_to` |
| `scanner_qas` | [scanner_qa](scanner_qa.md) | `many_to_many` | No | `nmmi_acquisition_scanner_qas` | `qualified_by` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_acquisition_provenance_records` | `documented_by` |
| `imaging_studies` | [imaging_study](imaging_study.md) | `many_to_one` | Yes | `nmmi_acquisition_imaging_studies` | `related_to` |
| `pt_series_files` | [pt_series_file](pt_series_file.md) | `many_to_one` | No | `nmmi_acquisition_pt_series_files` | `related_to` |
| `nm_series_files` | [nm_series_file](nm_series_file.md) | `many_to_one` | No | `nmmi_acquisition_nm_series_files` | `related_to` |
| `ct_series_files` | [ct_series_file](ct_series_file.md) | `many_to_one` | No | `nmmi_acquisition_ct_series_files` | `related_to` |
| `mr_series_files` | [mr_series_file](mr_series_file.md) | `many_to_one` | No | `nmmi_acquisition_mr_series_files` | `related_to` |
| `raw_files` | [supplementary_file](supplementary_file.md) | `many_to_many` | No | `nmmi_acquisition_raw_files` | `related_to` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"acquisition"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `protocol_name` | No | string | Acquisition protocol name. | — |
| `duration_seconds` | No | number | Acquisition duration. | Minimum: <code>0</code> |
| `energy_window_names` | No | array of string | Ordered energy-window labels. | — |
| `energy_window_lower_kev` | No | array of number | Ordered energy-window limits in keV. | Each item: (Minimum: <code>0</code>) |
| `energy_window_upper_kev` | No | array of number | Ordered energy-window limits in keV. | Each item: (Minimum: <code>0</code>) |
| `number_of_energy_windows` | No | integer | Number of windows; equals length of all window arrays. | Minimum: <code>1</code> |
| `number_of_bed_positions` | No | integer | Number of bed positions. | Minimum: <code>1</code> |
| `number_of_spect_acquisition_projections` | No | integer | The total number of projections acquired during the SPECT acquisition. | — |
| `imaging_spect_detector_type` | No | string | The scintillating material used by the gamma camera to detect photons. | — |
| `imaging_spect_image_comments` | No | string | A free-text field allowing any relevant comments or annotations about the acquisition; can contain information about acquisition and reconstruction settings. | — |
| `spiral_pitch_factor` | No | number | Provisional field for Spiral Pitch Factor; operational definition requires review. | — |
| `mas_exposure` | No | number | Provisional field for mAs (exposure); operational definition requires review. | — |
| `kvp` | No | integer | Provisional field for kVp; operational definition requires review. | — |
| `exposure_time` | No | integer | Provisional field for Exposure Time; operational definition requires review. | — |
| `ma_x_ray_tube_current` | No | number | Provisional field for mA (X-ray tube current); operational definition requires review. | — |
| `revolution_time` | No | number | Provisional field for Revolution Time; operational definition requires review. | — |
| `scan_options` | No | string | Provisional field for Scan Options; operational definition requires review. | — |
| `frame_reference_time` | No | integer | Provisional field for Frame Reference Time; operational definition requires review. | — |
| `frame_duration` | No | integer | Provisional field for Frame Duration; operational definition requires review. | — |
| `radiopharmaceutical_substabce` | No | string | Provisional field for Radiopharmaceutical Substabce; operational definition requires review. | — |
| `radionuclide_code_meaning` | No | string | Provisional field for Radionuclide Code Meaning; operational definition requires review. | — |
| `frame_start_time` | No | number | Provisional field for Frame Start Time; operational definition requires review. | — |
| `actual_frame_duration` | No | integer | Provisional field for Actual Frame Duration; operational definition requires review. | — |
| `sensitivity_factor` | No | number | Provisional field for Sensitivity Factor; operational definition requires review. | — |
| `sliceprogressiondirection` | No | string | Provisional field for SliceProgressionDirection; operational definition requires review. | — |
| `image_index` | No | string | Provisional field for Image Index; operational definition requires review. | — |
| `counts_source_attribute` | No | string | Provisional field for Counts Source Attribute; operational definition requires review. | — |
| `radiopharmaceutical_info_seq` | No | string | Provisional field for Radiopharmaceutical Info Seq; operational definition requires review. | — |
| `energy_window_seq` | No | string | Provisional field for Energy Window Seq; operational definition requires review. | — |
| `collimator_name` | No | string | Provisional field for Collimator Name; operational definition requires review. | — |
| `collimator_type` | No | string | Provisional field for Collimator Type; operational definition requires review. | — |
| `angular_step` | No | number | Provisional field for Angular Step; operational definition requires review. | — |
| `rotation_direction` | No | string | Provisional field for Rotation Direction; operational definition requires review. | — |
| `acquisition_start_condition` | No | string | Provisional field for Acquisition Start Condition; operational definition requires review. | — |
| `acquisition_end_condition` | No | string | Provisional field for Acquisition End Condition; operational definition requires review. | — |
| `cardiac_cycle_position` | No | number | Provisional field for Cardiac Cycle Position; operational definition requires review. | — |
| `rotation_information_sequence` | No | string | Provisional field for Rotation Information Sequence; operational definition requires review. | — |
| `tomo_angle_range` | No | number | Provisional field for Tomo Angle Range; operational definition requires review. | — |
| `energy_window_information_sequence` | No | string | Provisional field for Energy Window Information Sequence; operational definition requires review. | — |
| `number_of_frames_in_rotation` | No | string | Provisional field for Number of Frames in Rotation; operational definition requires review. | — |
| `start_angle` | No | string | Provisional field for Start Angle; operational definition requires review. | — |
| `type_of_detector_motion` | No | string | Provisional field for Type of Detector Motion; operational definition requires review. | — |
| `acuisition_date_time` | No | string | Provisional field for Acuisition date/time??; operational definition requires review. | — |
| `frame_time_continuous_bed` | No | string | Provisional field for Frame time continuous bed; operational definition requires review. | — |
| `bed_speed` | No | string | Provisional field for bed speed?; operational definition requires review. | — |
| `table_motion` | No | string | Provisional field for table motion; operational definition requires review. | — |
| `x_ray_tube_current` | No | number | X-Ray Tube Current in mA. | — |
| `exposure` | No | number | The exposure expressed in mAs, for example calculated from Exposure Time and X-Ray Tube Current. | — |
| `ctdivol` | No | number | Computed Tomography Dose Index (CTDIvol), in mGy according to IEC 60601-2-44, Ed.2.1 (Clause 29.1.103.4), The Volume CTDIvol. It describes the average dose for this image for the selected CT conditions of operation. | — |
| `ctdi_phantom_type_code_sequence` | No | string | Provisional field for CTDI Phantom Type Code Sequence; operational definition requires review. | — |
| `type_of_sequence` | No | string | Provisional field for TYPE OF SEQUENCE; operational definition requires review. | — |
| `contrast_enhanced` | No | string | Provisional field for CONTRAST-ENHANCED; operational definition requires review. | — |
| `high_bit` | No | string | Provisional field for High Bit; operational definition requires review. | — |
| `acquisition_number` | No | string | Provisional field for Acquisition Number; operational definition requires review. | — |
| `acquisition_termination_condition` | No | string | Provisional field for Acquisition Termination Condition; operational definition requires review. | — |
| `detector_motion_details_sequence` | No | string | Provisional field for Detector Motion Details Sequence; operational definition requires review. | — |
| `pet_frame_acquisition_sequence` | No | string | Provisional field for PET Frame Acquisition Sequence; operational definition requires review. | — |
| `pet_position_sequence` | No | string | Provisional field for PET Position Sequence; operational definition requires review. | — |
| `collimator_grid_name` | No | string | Provisional field for Collimator/Grid Name; operational definition requires review. | — |
| `gantry_detector_slew` | No | string | Provisional field for Gantry/Detector Slew; operational definition requires review. | — |
| `counts_source` | No | string | Primary Source of Counts | — |
| `acquisition_time` | No | string | Time of scan acquisition | — |
| `table_speed` | No | string | Table motion speed | — |
| `table_traverse` | No | string | Total distance moved | — |
| `table_motion_direction` | No | string | Head-first/Feet-first | — |
| `number_of_time_slices` | No | string | Maximum number of Time Slices existing in Series | — |
| `acquisition_type_source_value` | No | string | Original acquisition-type label when its modality or DICOM attribute context has not been adjudicated. Confirmed CT Acquisition Type uses MIDRC ct_series_file.acquisition_type. | — |
| `source_section_note_2_image_characteristics` | No | string | Provisional field for 2. Image Characteristics; operational definition requires review. | — |
| `source_section_note_3_acquisition_parameters` | No | string | Provisional field for 3. Acquisition Parameters; operational definition requires review. | — |
| `source_section_note_5_other_important_fields` | No | string | Provisional field for 5. Other Important Fields; operational definition requires review. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `scanners` | Yes | array of object | Link to scanner records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `scanner_qas` | No | array of object | Link to scanner_qa records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `imaging_studies` | Yes | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `pt_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `nm_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `ct_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `mr_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `raw_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic acquisition records](../../extensions/lu177_psma/v0.3.0/examples/by_node/acquisition.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
