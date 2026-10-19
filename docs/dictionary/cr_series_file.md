# CR Series File (`cr_series_file`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

A package of image files and metadata related to a CR imaging series to which one or more computed radiograph (CR) instances belong.

| Attribute | Value |
| --- | --- |
| Record grain | One MIDRC cr series file record |
| Category | `data_file` |
| Navigation group | Imaging |
| MIDRC relationship | `preserved` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/cr_series_file.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/cr_series_file.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_cr_series_file_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `core_metadata_collections` | [core_metadata_collection](core_metadata_collection.md) | `many_to_one` | No; group 1 | `cr_series_files` | `data_from` |
| `imaging_studies` | [imaging_study](imaging_study.md) | `many_to_one` | No; group 1 | `cr_series_files` | `related_to` |

Group 1: **at least one populated member** among `core_metadata_collections`, `imaging_studies`.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `contrast_bolus_agent` | No | array of string | (0018, 0010) Contrast/Bolus Agent. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0018, 0010); Contrast Bolus Agent |
| `data_category` | Yes | string (enumerated) | Broad categorization of the contents of the data file. | Allowed values: <code>"CR"</code> |
| `data_format` | Yes | string (enumerated) | Format of the data files. | Allowed values: <code>"DCM"</code>, <code>"nii.gz"</code> |
| `data_type` | Yes | string (enumerated) | Specific content type of the data file. | Allowed values: <code>"DICOM"</code>, <code>"NIfTI"</code> |
| `detector_type` | No | string (enumerated) | (0018, 7004) Detector Type. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Allowed values: <code>"DIRECT"</code>, <code>"SCINTILLATOR"</code>, <code>"STORAGE"</code>, <code>"FILM"</code>; Source term: DICOM; (0018, 7004); Detector Type |
| `dicom_header_file_guid` | No | string | The GUID of the zip file containing DICOM header files for an imaging series in the MIDRC index service. | — |
| `file_name` | Yes | string | The name (or part of a name) of a file (of any type). | — |
| `file_size` | Yes | integer | The size of the data file (object) in bytes. | — |
| `image_data_modification_method` | No | string (enumerated) | A categorical description of the type of image modification performed on the study series. | Allowed values: <code>"Removal of alphanumeric characters"</code>, <code>"Defacing"</code>, <code>"Skull-stripping"</code> |
| `image_data_modification_name` | No | integer | A MIDRC classification describing specific methods (e.g., software tools, processes) used to modify the study series. More information can be found at midrc.org. | — |
| `image_data_modified` | No | boolean | An indicator of whether any post-clinical modification of image pixel data has been performed on the study series. | — |
| `image_type` | No | array of string | (0008, 0008) Image Type. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0008, 0008); Image Type |
| `imager_pixel_spacing` | No | array of number | (0018, 1164) Imager Pixel Spacing. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0018, 1164); Imager Pixel Spacing |
| `lossy_image_compression` | No | string (enumerated) | (0028, 2110) Lossy Image Compression; Note, if an image is compressed with a lossy algorithm, the Attribute Lossy Image Compression (0028,2110) is set to "01". Subsequently, if the image is decompressed and transferred in uncompressed format, this Attribute value remains "01". The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Allowed values: <code>"00"</code>, <code>"01"</code>; Source term: DICOM; (0028, 2110); Lossy Image Compression |
| `manufacturer` | No | string | (0008, 0070) Manufacturer. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0008, 0070); Manufacturer |
| `manufacturer_model_name` | No | string | (0008, 1090) Manufacturer's Model Name. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0008, 1090); Manufacturer's Model Name |
| `md5sum` | Yes | string | The 128-bit hash value expressed as a 32 digit hexadecimal number used as a file's digital fingerprint. | Pattern: <code>"^[a-f0-9]{32}$"</code> |
| `modality` | No | string | (0008, 0060) Modality. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0008, 0060); Modality |
| `number_of_instances` | No | integer | The number of instances included in this series. | — |
| `object_id` | No | string | The GUID of the object in the index service. | — |
| `pixel_spacing` | No | array of number | (0028, 0030) Pixel Spacing. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0028, 0030); Pixel Spacing |
| `series_description` | No | string | (0008, 103e) Series Description. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0008, 103e); Series Description |
| `series_uid` | No | string | (0020, 000e) Series Instance UID. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0020, 000e); Series Instance UID |
| `spatial_resolution` | No | number | (0018, 1050) Spatial Resolution. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0018, 1050); Spatial Resolution |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `view_position` | No | array of string | (0018, 5101) View Position. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0018, 5101); View Position |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `core_metadata_collections` | No | one or more of: array of object; object | The submitter_id or id of the core_metadata_collection to which the cr_series_file belongs, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `imaging_studies` | No | one or more of: array of object; object | The submitter_id or id of the imaging_study this cr_series_file belongs to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |

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

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
