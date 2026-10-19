# Radiology Report (`radiology_report`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

A detailed report that describes the results of an imaging test. A radiology report can include narrative information about the type of imaging test that was done, how it was done, and any labels representing the results of the test.

| Attribute | Value |
| --- | --- |
| Record grain | One MIDRC radiology report record |
| Category | `data_file` |
| Navigation group | Clinical |
| MIDRC relationship | `preserved` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/radiology_report.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/radiology_report.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_radiology_report_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `core_metadata_collections` | [core_metadata_collection](core_metadata_collection.md) | `many_to_one` | No; group 1 | `radiology_reports` | `data_from` |
| `datasets` | [dataset](dataset.md) | `many_to_one` | No; group 1 | `radiology_reports` | `related_to` |
| `cases` | [case](case.md) | `many_to_one` | No; group 1 | `radiology_reports` | `related_to` |
| `imaging_studies` | [imaging_study](imaging_study.md) | `many_to_many` | No; group 1 | `radiology_reports` | `related_to` |

Group 1: **at least one populated member** among `core_metadata_collections`, `datasets`, `cases`, `imaging_studies`.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `airway_involvement` | No | string (enumerated) | An indicator confirming whether airway involvement was discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `airway_involvement_type` | No | array of string (enumerated) | A description noting the specific type of airway involvement discovered during imaging. | Each item: (Allowed values: <code>"Bronchial Stenosis"</code>, <code>"Bronchofistula"</code>, <code>"Other"</code>, <code>"Not Reported"</code>) |
| `body_part_examined` | No | array of string | (0018, 0015) Body Part Examined. | — |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `cavities` | No | string (enumerated) | An indicator confirming whether cavities were discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `cavities_count` | No | integer | The number of cavities discovered during imaging. | — |
| `cavities_largest_size` | No | number | A measure in size of the largest cavity discovered during imaging. | — |
| `cavities_wall_thickness` | No | number | A measure of wall thickness of the cavities discovered during imaging. | — |
| `ct_protocol` | No | array of string (enumerated) | A description of the protocol used for a computed tomography (CT) scan. | Each item: (Allowed values: <code>"High Resolution CT (HRCT)"</code>, <code>"Routine Non-Contrast"</code>, <code>"Routine CT Chest with Contrast"</code>, <code>"CT Pulmonary Angiogram (PE Protocol)"</code>, <code>"Slice thickness"</code>, <code>"Expiration"</code>, <code>"Inspiration"</code>) |
| `cysts_bullae` | No | string (enumerated) | An indicator confirming whether cysts or bullae were discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `data_category` | Yes | string (enumerated) | Broad categorization of the contents of the data file. | Allowed values: <code>"Radiology Report"</code> |
| `data_format` | Yes | string (enumerated) | Format of the data files. | Allowed values: <code>"CSV"</code>, <code>"DICOM"</code>, <code>"JSON"</code>, <code>"PDF"</code>, <code>"RTF"</code>, <code>"TSV"</code>, <code>"TXT"</code>, <code>"XML"</code> |
| `data_type` | Yes | string (enumerated) | Specific content type of the data file. | Allowed values: <code>"Radiology Report"</code> |
| `distribution_axial` | No | string (enumerated) | A description noting the distribution of fibrosis across the different zones relative to the center of the lung. | Allowed values: <code>"Peripheral"</code>, <code>"Central"</code>, <code>"Diffuse"</code>, <code>"Not reported"</code> |
| `distribution_zone` | No | string (enumerated) | A description noting the distribution of fibrosis across the different zones within the lungs. | Allowed values: <code>"Upper"</code>, <code>"Mid"</code>, <code>"Lower"</code>, <code>"Not Reported"</code> |
| `fibrocalcific_scarring` | No | string (enumerated) | An indicator confirming whether fibrocalcific scaring was discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `fibrosis_pattern` | No | string (enumerated) | A description of the pattern of fibrosis related scaring, determined by imaging. | Allowed values: <code>"Usual Interstitial Pneumonia (UIP)"</code>, <code>"Probable UIP"</code>, <code>"Indeterminate"</code>, <code>"Alternative Diagnosis"</code>, <code>"Not reported"</code> |
| `fibrosis_segments` | No | array of string (enumerated) | A description of the specific anatomic location of the fibrosis. | Each item: (Allowed values: <code>"Upper"</code>, <code>"Middle"</code>, <code>"Lower"</code>) |
| `file_name` | Yes | string | The name (or part of a name) of a file (of any type). | — |
| `file_size` | Yes | integer | The size of the data file (object) in bytes. | — |
| `ground_glass_opacities` | No | string (enumerated) | An indicator confirming whether ground-glass opacities (GGOs) were discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `ground_glass_opacities_focality` | No | string (enumerated) | A description noting whether confirmed ground-glass opacities (GGOs) were localized (focal) or spread across multiple locations (diffuse). | Allowed values: <code>"Focal"</code>, <code>"Diffuse"</code> |
| `honeycombing` | No | string (enumerated) | An indicator confirming whether honeycomb fibrosis was discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `honeycombing_focality` | No | string (enumerated) | A description noting whether confirmed honeycomb fibrosis was localized (focal) or spread across multiple locations (diffuse). | Allowed values: <code>"Focal"</code>, <code>"Diffuse"</code> |
| `image_quality` | No | string (enumerated) | A description noting the quality of the image(s) used for the radiology report. | Allowed values: <code>"Optimal"</code>, <code>"Suboptimal"</code>, <code>"Non-diagnostic"</code> |
| `laterality` | No | string (enumerated) | Laterality type relative to the anatomic site of the body examined or affected. | Allowed values: <code>"Unilaterall"</code>, <code>"Bilateral"</code>, <code>"Not reported"</code> |
| `lymphadenopathy_consolidation` | No | string (enumerated) | An indicator confirming whether lymphadenopathy or consolidation were discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `md5sum` | Yes | string | The 128-bit hash value expressed as a 32 digit hexadecimal number used as a file's digital fingerprint. | Pattern: <code>"^[a-f0-9]{32}$"</code> |
| `modality` | No | string | (0008, 0060) Modality | — |
| `object_id` | No | string | The GUID of the object in the index service. | — |
| `paracicatricial_emphysema` | No | string (enumerated) | An indicator confirming whether paracicatricial emphysema was discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `parenchymal_bands` | No | string (enumerated) | An indicator confirming whether parenchymal bands were discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `pleural_involvement` | No | string (enumerated) | An indication of whether the pleura impacted by the fibrosis, based on imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `pleural_involvement_phase` | No | array of string (enumerated) | A description noting the phase of pleural involvement. | Each item: (Allowed values: <code>"Effusion"</code>, <code>"Thickening"</code>, <code>"Calcification"</code>) |
| `pulmonary_hypertension_signs` | No | array of string (enumerated) | A description noting the specific signs of pulmonary hypertension discovered during imaging. | Each item: (Allowed values: <code>"Pulmonary Artery Dilatation"</code>, <code>"Right Ventricle Enlargement"</code>) |
| `pulmonary_hypertension_signs_indicator` | No | string (enumerated) | An indicator confirming whether imaging showed signs of pulmonary hypertension. | Allowed values: <code>"Effusion"</code>, <code>"Thickening"</code>, <code>"Calcification"</code> |
| `report_generation_method` | No | string (enumerated) | A categorical description of the way the report was generated, either through clinical care (Clinical) or through computational means (Synethic). | Allowed values: <code>"Clinical"</code>, <code>"Synthetic"</code> |
| `report_modification_method` | No | string (enumerated) | A categorical description of the type of modification performed on the report, either by redaction of sensitive information (Redacted) or by obscuring it through replacement with random or shifted values (Synthetic replacement). | Allowed values: <code>"Redacted"</code>, <code>"Synthetic replacement"</code> |
| `reticular_opacities` | No | string (enumerated) | An indicator confirming whether reticular opacities were discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `reticular_opacities_focality` | No | string (enumerated) | A description noting whether confirmed reticular opacities were localized (focal) or spread across multiple locations (diffuse). | Allowed values: <code>"Focal"</code>, <code>"Diffuse"</code> |
| `study_description` | No | string | (0008, 1030) Study Description. | — |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `symmetry` | No | string (enumerated) | A description noting how the fibrotic changes are distributed throughout the organ or tissue. | Allowed values: <code>"Symmetrical"</code>, <code>"Asymmetrical"</code>, <code>"Not reported"</code> |
| `traction_bronchiectasis` | No | string (enumerated) | A indicator confirming whether traction bronchiectasis was discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `traction_bronchiectasis_focality` | No | string (enumerated) | A description noting whether confirmed traction bronchiectasis was localized (focal) or spread across multiple locations (diffuse). | Allowed values: <code>"Focal"</code>, <code>"Diffuse"</code> |
| `tuberculoma_calcified_ghon_focus` | No | string (enumerated) | An indicator confirming whether a tuberculoma calcified ghon focus was discovered during imaging. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | No | one or more of: array of object; object | The submitter_id or id of the case this report relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `core_metadata_collections` | No | one or more of: array of object; object | The submitter_id or id of the core_metadata_collection to which the report belongs, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `datasets` | No | one or more of: array of object; object | The submitter_id or id of the case this report relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `imaging_studies` | No | one or more of: array of object; object | The submitter_id or id of the imaging_study this report relates to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |

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
