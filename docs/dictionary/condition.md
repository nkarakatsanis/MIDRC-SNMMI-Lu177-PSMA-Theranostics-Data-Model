# Condition (`condition`)

Release **0.3.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Information pertaining to relevant medical condition(s) of a case's subject (e.g., medical diagnoses, diseases, disorders, symptoms, injuries, illnesses, comorbidities) recorded in the process of clinical care (e.g., data extracted from the electronic medical record).

| Attribute | Value |
| --- | --- |
| Record grain | One condition or disease-status assessment |
| Category | `medical_history` |
| Navigation group | Clinical |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/condition.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/condition.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_condition_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `cases` | [case](case.md) | `many_to_one` | Yes | `conditions` | `related_to` |
| `timepoints` | [timepoint](timepoint.md) | `many_to_one` | No | `nmmi_condition_timepoints` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_condition_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `condition_code` | No | string | The code for a specific condition, assigned by the code system. | Source term: NCIt; C93536; Condition Code |
| `condition_code_system` | No | string | The system that assigned the code for a specific condition. | Source term: NCIt; C70895; Code System |
| `condition_name` | No | string | The name of the condition the patient has experienced. | Source term: NCIt; C207483; Condition Name |
| `days_to_condition_end` | No | integer | The number of days from the index date to the date the subject no longer experienced the condition. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | — |
| `days_to_condition_start` | No | integer | The number of days from the index date to the date the subject was diagnosed with or began experiencing the condition. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | — |
| `days_to_symptom_onset` | No | integer | The number of days from the index date to the date the symptoms began. | — |
| `fibrosis_confirmation` | No | string (enumerated) | An indicator confirming whether the patient received a diagnosis of fibrosis. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `fibrosis_lung_involvement_grading` | No | string (enumerated) | A visual measure of the involvement of fibrosis in the lungs. | Allowed values: <code>"Mild (≤25%)"</code>, <code>"Moderate (26–50%)"</code>, <code>"Severe (&gt;50%)"</code>, <code>"Not reported"</code> |
| `fibrosis_volume_loss_grading` | No | string (enumerated) | A visual measure of the volume loss or shrinkage of the lungs due to fibrosis. | Allowed values: <code>"Mild"</code>, <code>"Moderate"</code>, <code>"Severe"</code>, <code>"Not reported"</code> |
| `history_of_connective_tissue_disease` | No | string (enumerated) | An indicator confirming a history of connective tissue disease. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `history_of_connective_tissue_disease_type` | No | string (enumerated) | A description of the type of connective tissue disease. | Allowed values: <code>"Rheumatoid Arthritis"</code>, <code>"Systemic Lupus Erythematosus"</code>, <code>"Scleroderma"</code>, <code>"Unknown"</code> |
| `history_of_hiv` | No | string (enumerated) | An indicator confirming a history of human immunodeficiency virus (HIV). | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `history_of_hiv_treatment` | No | array of string (enumerated) | A description of the type of HIV treatment received. | Each item: (Allowed values: <code>"On current anti-viral treatment"</code>, <code>"Past Treatment"</code>, <code>"Not Reported"</code>) |
| `history_of_interstitial_lung_disease` | No | string (enumerated) | An indicator confirming a history of interstitial lung disease. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `history_of_lung_cancer` | No | string (enumerated) | An indicator confirming a history of lung cancer. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `history_of_other_disease` | No | string (enumerated) | A description of the confirmed history of other diseases not previously listed. | Allowed values: <code>"Hypertension"</code>, <code>"Hypersensitivity Pneumonitis"</code>, <code>"Sarcoidosis"</code>, <code>"None"</code>, <code>"Other"</code>, <code>"Unknown"</code> |
| `history_of_tuberculosis` | No | string (enumerated) | The indicator related to medical history of the condition tuberculosis (TB). | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `history_of_tuberculosis_treatment` | No | array of string (enumerated) | A description of the type of tuberculosis treatment received. | Each item: (Allowed values: <code>"On current treatment"</code>, <code>"Past treatment"</code>, <code>"Not Reported"</code>) |
| `presenting_symptoms` | No | string (enumerated) | A description noting the presenting symptoms at the onset of the condition. | Allowed values: <code>"Dyspnea"</code>, <code>"Chronic Cough"</code>, <code>"Difficulty in Breathing"</code>, <code>"Chest pain"</code>, <code>"Incidental finding"</code>, <code>"Other"</code> |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `assessment_datetime` | No | string | ISO 8601 assessment datetime; use approved date shifting consistently within the case. | Format: <code>"date-time"</code> |
| `days_from_course_start` | No | number | Signed elapsed days from the linked therapy course start. | — |
| `time_basis` | No | string | Interpretation of stored dates and elapsed times. | Allowed values: <code>"actual"</code>, <code>"shifted"</code>, <code>"relative_only"</code>, <code>"unknown"</code> |
| `time_window_start_day` | No | number | Beginning of assessment window relative to course start, in days. | — |
| `time_window_end_day` | No | number | End of assessment window relative to course start, in days. | — |
| `ajcc_m_stage_initialdx` | No | string | Metastasis stage (M) based on AJCC staging system version 9 at the time of initial prostate cancer diagnosis. | — |
| `ajcc_n_stage_initialdx` | No | string | Nodal stage (N) based on AJCC staging system version 9at the time of initial prostate cancer diagnosis. | — |
| `ajcc_stage_group_initialdx` | No | string | Overall AJCC stage group at the time of initial prostate cancer diagnosis. Specify AJCC version used. | — |
| `ajcc_t_stage_initialdx` | No | string | Tumor stage (T) based on AJCC staging system version 9at the time of initial prostate cancer diagnosis. | — |
| `castration_resistance_date` | No | string | Date when the patient's prostate cancer was deemed castration-resistant. | Format: <code>"date"</code> |
| `disease_sensitivity_status` | No | string | Patient's disease status regarding hormone sensitivity at the time of assessment. | — |
| `disease_status_assessment_date` | No | string | Date when the hormone sensitivity status was determined or assessed. | Format: <code>"date"</code> |
| `gleason_grade_group_primary` | No | integer | ISUP Gleason Grade Group from primary prostate cancer diagnosis. | — |
| `gleason_score_primary` | No | string | Gleason score from primary prostate cancer diagnosis. | — |
| `histology_subtype` | No | string | Specific histological subtype or features, particularly noting adenocarcinoma vs. neuroendocrine differentiation or aggressive variants. | — |
| `initial_diagnosis_date_prostateca` | No | string | Date when prostate cancer was first diagnosed. | Format: <code>"date"</code> |
| `lvi_status` | No | string | Presence or absence of lymph-vascular invasion identified in pathology report (typically from primary tumor). | — |
| `metastasis_sites_baseline` | No | array of string | Location(s) of metastatic disease at baseline prior to PSMA theranostics. | — |
| `msi_status` | No | string | Microsatellite instability status (e.g., MSI-High, MSI-Low, MSS-Stable), if tested. | — |
| `baseline_clinical_data_hormone_sensitive_prostate_ca` | No | string | Provisional field for Baseline clinical data; Hormone sensitive prostate ca; operational definition requires review. | — |
| `castrate_resistant_prostate_ca` | No | string | Provisional field for Castrate resistant prostate Ca; operational definition requires review. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | Yes | one or more of: array of object; object | The submitter_id or id of the case this condition describes, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
| `timepoints` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
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

[Read the synthetic condition records](../../extensions/lu177_psma/v0.3.0/examples/by_node/condition.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
