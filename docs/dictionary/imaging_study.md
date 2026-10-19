# Imaging Study (`imaging_study`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Information related to an imaging study or exam done for diagnostic or research purposes, including patient clinical or contextual data recorded at the time of the imaging study.

| Attribute | Value |
| --- | --- |
| Record grain | One examination |
| Category | `medical_history` |
| Navigation group | Imaging |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/imaging_study.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/imaging_study.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_imaging_study_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `cases` | [case](case.md) | `many_to_one` | Yes | `imaging_studies` | `related_to` |
| `datasets` | [dataset](dataset.md) | `many_to_many` | Yes | `imaging_studies` | `member_of` |
| `visits` | [visit](visit.md) | `many_to_one` | No | `nmmi_imaging_study_visits` | `related_to` |
| `timepoints` | [timepoint](timepoint.md) | `many_to_one` | No | `nmmi_imaging_study_timepoints` | `related_to` |
| `administrations` | [administration](administration.md) | `many_to_many` | No | `nmmi_imaging_study_administrations` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_imaging_study_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `age_at_imaging` | No | number | The study participant's age, in years, at the time the imaging study was performed. Note that an age of 0 indicates a participant who is younger than 1 year old. For participants with ages greater than 89 years, please use the property 'age_at_index_gt89'. | Minimum: <code>0</code>; Maximum: <code>89</code>; Source term: NCIt; C201610; Age at Imaging |
| `age_at_imaging_gt89` | No | string (enumerated) | Indicates whether the age of the patient in years at the time the imaging study was performed is greater than 89 years. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | Allowed values: <code>"Yes"</code>, <code>"No"</code> |
| `body_part_examined` | No | array of string | (0018, 0015) Body Part Examined. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0018, 0015); Body Part Examined |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `days_from_study_to_neg_covid_test` | No | array of integer | The number of days from the imaging study to the patient's negative COVID-19 test(s). This property takes a list of values, each of which represents a COVID-19 test for the patient. A positive value for this property means that a negative COVID-19 test result was obtained for the patient that many days after the imaging study was performed. A negative value indicates that a negative COVID-19 test result was obtained prior to the date of imaging. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | — |
| `days_from_study_to_pos_covid_test` | No | array of integer | The number of days from the imaging study to the patient's positive COVID-19 test(s). This property takes a list of values, each of which represents a COVID-19 test for the patient. A positive value for this property means that a positive COVID-19 test result was obtained for the patient that many days after the imaging study was performed. A negative value indicates that the positive COVID-19 test result was obtained prior to the date of imaging. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | — |
| `days_to_study` | No | number | The number of days between the case's index date and the date of the imaging study. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | — |
| `image_data_modified` | No | boolean | An indicator of whether any post-clinical modification of image pixel data has been performed on the study. | — |
| `loinc_code` | No | string | The LOINC code assigned based on the study description provided. The Logical Observation Identifiers, Names, and Codes (LOINC) standard is A common language (set of identifiers, names, and codes) for clinical and laboratory observations. | Source term: LOINC; LOINC; LOINC Code |
| `loinc_contrast` | No | string | The LOINC indicator noting whether the image was completed with or without contrast, as associated with the assigned LOINC code. The Logical Observation Identifiers, Names, and Codes (LOINC) standard is A common language (set of identifiers, names, and codes) for clinical and laboratory observations. | Source term: LOINC; LOINC; LOINC Contrast |
| `loinc_long_common_name` | No | string | The LOINC long common name associated with the assigned LOINC code. The Logical Observation Identifiers, Names, and Codes (LOINC) standard is A common language (set of identifiers, names, and codes) for clinical and laboratory observations. | Source term: LOINC; LOINC; LOINC Long Common Name |
| `loinc_method` | No | string | The LOINC method or imaging modality associated with the assigned LOINC code. The Logical Observation Identifiers, Names, and Codes (LOINC) standard is A common language (set of identifiers, names, and codes) for clinical and laboratory observations. | Source term: LOINC; LOINC; LOINC Method |
| `loinc_system` | No | string | The LOINC system or body part examined associated with the assigned LOINC code. The Logical Observation Identifiers, Names, and Codes (LOINC) standard is A common language (set of identifiers, names, and codes) for clinical and laboratory observations. | Source term: LOINC; LOINC; LOINC System |
| `study_description` | No | string | (0008, 1030) Study Description. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0008, 1030); Study Description |
| `study_modality` | No | array of string | The modalities of the imaging study; derived from (0008, 0060) Modality. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0008, 0060); Study Modality |
| `study_uid` | No | string | (0020, 000d) Study Instance UID. The Digital Imaging and Communications in Medicine (DICOM) standard is the international standard to transmit, store, retrieve, print, process, and display medical imaging information. | Source term: DICOM; (0020, 000d); Study Instance UID |
| `study_year` | No | integer | The year when imaging study was performed; year component of Study Date (0008, 0020). | Source term: DICOM; (0008, 0020); Study Date Attribute |
| `study_year_shifted` | No | boolean | Indicates whether the study year has been shifted for de-identification. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | — |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `study_date` | No | string | Date of imaging study. | Format: <code>"date"</code> |
| `imaging_purpose` | No | string | Baseline, eligibility, dosimetry, response or follow-up purpose. | — |
| `is_therapy_baseline` | No | boolean | Is this the baseline exam for PSMA therapy | — |
| `study_time` | No | string | Provisional field for Study Time; operational definition requires review. | — |
| `accession_number_pseudonym` | No | string | Provisional field for Accession Number; operational definition requires review. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | Yes | one or more of: array of object; object | The submitter_id or id of the case observed in this imaging_study, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `datasets` | Yes | one or more of: array of object; object | The submitter_id or id of the dataset this case belongs to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>) / 2. object] |
| `visits` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `timepoints` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `administrations` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `provenance_records` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic imaging_study records](../../extensions/lu177_psma/v0.3.0/examples/by_node/imaging_study.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
