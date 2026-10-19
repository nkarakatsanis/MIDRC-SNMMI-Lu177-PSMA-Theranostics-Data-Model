# Annotation (`annotation`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Information describing characteristics of imaging studies, series and instances (e.g., segmentations, bounding boxes, feature labels) and inferences based on those characteristics (e.g., predicted diagnoses). Annotations may be recorded in the course of clinical care or retrospectively for purposes of research (e.g., imaging annotations from PACS or retrospective labeling tools). Please refer to https://midrc.org/annotations to learn more about a particular batch of annotations.

| Attribute | Value |
| --- | --- |
| Record grain | One annotation/contour execution; its files remain separate artifacts |
| Category | `annotation` |
| Navigation group | Imaging |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/annotation.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/annotation.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_annotation_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `datasets` | [dataset](dataset.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `cases` | [case](case.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `imaging_studies` | [imaging_study](imaging_study.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `cr_series_files` | [cr_series_file](cr_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `ct_series_files` | [ct_series_file](ct_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `dx_series_files` | [dx_series_file](dx_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `mg_series_files` | [mg_series_file](mg_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `mr_series_files` | [mr_series_file](mr_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `nm_series_files` | [nm_series_file](nm_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `pt_series_files` | [pt_series_file](pt_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `rf_series_files` | [rf_series_file](rf_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `us_series_files` | [us_series_file](us_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `xa_series_files` | [xa_series_file](xa_series_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `annotation_files` | [annotation_file](annotation_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `dicom_annotation_files` | [dicom_annotation_file](dicom_annotation_file.md) | `many_to_one` | No; group 1 | `annotations` | `related_to` |
| `anatomic_targets` | [anatomic_target](anatomic_target.md) | `many_to_one` | No | `nmmi_annotation_anatomic_targets` | `related_to` |
| `registrations` | [registration](registration.md) | `many_to_many` | No | `nmmi_annotation_registrations` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_annotation_provenance_records` | `related_to` |
| `anatomic_reference_pt_series_files` | [pt_series_file](pt_series_file.md) | `many_to_one` | No | `nmmi_annotation_anatomic_reference_pt_series_files` | `related_to` |
| `anatomic_reference_nm_series_files` | [nm_series_file](nm_series_file.md) | `many_to_one` | No | `nmmi_annotation_anatomic_reference_nm_series_files` | `related_to` |
| `anatomic_reference_ct_series_files` | [ct_series_file](ct_series_file.md) | `many_to_one` | No | `nmmi_annotation_anatomic_reference_ct_series_files` | `related_to` |
| `anatomic_reference_mr_series_files` | [mr_series_file](mr_series_file.md) | `many_to_one` | No | `nmmi_annotation_anatomic_reference_mr_series_files` | `related_to` |

Group 1: **at least one populated member** among `datasets`, `cases`, `imaging_studies`, `cr_series_files`, `ct_series_files`, `dx_series_files`, `mg_series_files`, `mr_series_files`, `nm_series_files`, `pt_series_files`, `rf_series_files`, `us_series_files`, `xa_series_files`, `annotation_files`, `dicom_annotation_files`.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `airspace_disease_grading` | No | string (enumerated) | Values are extracted from the annotation file midrc_mdai_chestxr. Accepted values are "mild" opacities (1-2 lung zones), "moderate" opacities (3-4 lung zones), and "severe" opacities (&gt;4 lung zones). | Allowed values: <code>"mild"</code>, <code>"moderate"</code>, <code>"severe"</code> |
| `annotation_long_name` | No | string | The long name of the annotation provides more information about the specific annotation. | — |
| `annotation_method` | No | string (enumerated) | Defines the method by which the annotation was created. Clinically_derived - Based on information produced in the process of the subject's medical care; Retrospective_expert - Based on information produced retrospective to the subject's care by annotators with relevant special clinical expertise; Retrospective_general - Based on information produced retrospective to the subject's care by annotators without relevant special clinical expertise; Retrospective_auto - Based on information produced retrospective to the subject's care using automated means. | Allowed values: <code>"Clinically_derived"</code>, <code>"Retrospective_expert"</code>, <code>"Retrospective_general"</code>, <code>"Retrospective_auto"</code> |
| `annotation_name` | No | string (enumerated) | The name of the annotation. These names are unique and assigned by MIDRC. Annotation names reference a document posted on the MIDRC website describing the annotation, methods and values expected. All MIDRC created annotations start with "midrc_". | Allowed values: <code>"midrc_bpr_landmarks"</code>, <code>"midrc_bpr_regions"</code>, <code>"midrc_lung_segs"</code>, <code>"midrc_lung_measures"</code>, <code>"midrc_mdai_chestxr"</code>, <code>"midrc_mRALE_Mastermind_Challenge"</code>, <code>"SIFT"</code>, <code>"NMMI_PSMA_SEGMENTATION"</code>, <code>"NMMI_PSMA_DOSE_MAP"</code>; Source term: MIDRC; Annotation Name |
| `annotator_id` | No | string | Coded value to represent a particular annotator in a group. These need only be unique per annotation. | — |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `class_covid19_pneumonia` | No | string (enumerated) | Values are extracted from the annotation file midrc_mdai_chestxr; Accepted values include "typical" appearance, which is multifocal bilateral, peripheral opacities, or opacities with rounded morphology, lower lung-predominant distribution; "indeterminate" appearance, which is absence of typical findings and unilateral, central or upper lung predominant distribution of airspace disease; "atypical" appearance, which is pneumothorax or pleural effusion, pulmonary edema, lobar consolidation, solitary lung nodule, or mass diffuse tiny nodules cavity; "negative" for pneumonia, which is no lung opacities. | Allowed values: <code>"atypical"</code>, <code>"indeterminate"</code>, <code>"negative"</code>, <code>"typical"</code> |
| `instance_uids` | No | array of string | Used to denote that this annotation applies only to specific images (image instances) in a series. If absent, an annotation that references an imaging series node applies to the entire imaging series. | — |
| `midrc_mRALE_score` | No | integer | Values are extracted from the annotation file mRALE_Mastermind_Challenge. The Radiographic Assessment of Lung Edema (RALE) score is provided as a reference standard assessment of disease severity on chest radiograph. A normal chest radiograph receives a score of 0, while a chest radiograph with complete consolidation of both lungs receives the maximum score of 24. | Minimum: <code>0</code>; Maximum: <code>24</code> |
| `sift_image_quality_index` | No | string (enumerated) | A score of image quality based on the SIFT annotation software. | Allowed values: <code>"A"</code>, <code>"B"</code>, <code>"C"</code>, <code>"D"</code>, <code>"Not Reported"</code> |
| `software_version` | No | string | (0018, 1020) Software Version(s). The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0018, 1020); Software Version(s) |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `segmentation_identifier` | No | string | Contour identifier for this particular target, image and method. | — |
| `segmentation_method` | No | string | Segmentation method. | — |
| `software_name` | No | string | Segmentation software name. | — |
| `parameters` | No | string | Segmentation parameters. | — |
| `frame_of_reference_uid` | No | string | Segmentation frame of reference uid. | — |
| `roi_image_uid` | No | string | Unique identifier of the image on which the ROI was defined and measured. | — |
| `roi_segmentation_imaging_modality` | No | string | The imaging modality used for contouring the ROI. | — |
| `roi_segmentation_method_absolute_threshold_value` | No | string | Provisional field for ROI_Segmentation_Method_Absolute_Threshold_Value; operational definition requires review. | — |
| `segmentation_method_description` | No | string | A description of the segmentation method, particularly for those that fit in the "Other" category. | — |
| `roi_segmentation_method_ratio_reference_region` | No | string | Provisional field for ROI_Segmentation_Method_Ratio_Reference_Region; operational definition requires review. | — |
| `roi_segmentation_method_ratio_threshold_value` | No | string | Provisional field for ROI_Segmentation_Method_Ratio_Threshold_Value; operational definition requires review. | — |
| `roi_segmentation_method_relative_threshold_value` | No | string | Provisional field for ROI_Segmentation_Method_Relative_Threshold_Value; operational definition requires review. | — |
| `roi_segmentation_modality_coregistration_method` | No | string | The method used to coregister the imaging modalities used during ROI segmentation. | — |
| `roi_segmentation_modality_coregistration_method_name` | No | string | A free-text description of the method used to coregister the imaging modalities used during ROI segmentation. | — |
| `annotation_profile` | No | string | Theranostics annotation profile. | Allowed values: <code>"segmentation"</code>, <code>"other"</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `annotation_files` | No | one or more of: array of object; object | The submitter_id or id of the annotation_file this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `cases` | No | one or more of: array of object; object | The submitter_id or id of the case this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `cr_series_files` | No | one or more of: array of object; object | The submitter_id or id of the CR imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `ct_series_files` | No | one or more of: array of object; object | The submitter_id or id of the CT imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `datasets` | No | one or more of: array of object; object | The submitter_id or id of the case this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `dicom_annotation_files` | No | one or more of: array of object; object | The submitter_id or id of the dicom_annotation_file this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `dx_series_files` | No | one or more of: array of object; object | The submitter_id or id of the DX imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `imaging_studies` | No | one or more of: array of object; object | The submitter_id or id of the imaging_study this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `mg_series_files` | No | one or more of: array of object; object | The submitter_id or id of the MG imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `mr_series_files` | No | one or more of: array of object; object | The submitter_id or id of the MR imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `nm_series_files` | No | one or more of: array of object; object | The submitter_id or id of the NM imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `pt_series_files` | No | one or more of: array of object; object | The submitter_id or id of the PT imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `rf_series_files` | No | one or more of: array of object; object | The submitter_id or id of the RF imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `us_series_files` | No | one or more of: array of object; object | The submitter_id or id of the US imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `xa_series_files` | No | one or more of: array of object; object | The submitter_id or id of the XA imaging series this annotation relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `anatomic_targets` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `registrations` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `provenance_records` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `anatomic_reference_pt_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `anatomic_reference_nm_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `anatomic_reference_ct_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `anatomic_reference_mr_series_files` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic annotation records](../../extensions/lu177_psma/v0.3.0/examples/by_node/annotation.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
