# Medical History (`medical_history`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Family history and historical summaries with source provenance.

| Attribute | Value |
| --- | --- |
| Record grain | One history assessment |
| Category | `clinical` |
| Navigation group | Clinical |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/medical_history.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/medical_history.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_medical_history_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `cases` | [case](case.md) | `many_to_one` | Yes | `nmmi_medical_history_cases` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_medical_history_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"medical_history"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `comorbidity_cardiovascular_disease` | No | string | Presence of clinically significant cardiovascular disease (e.g., CAD, CHF, Stroke). | — |
| `comorbidity_chronic_kidney_disease` | No | string | Presence of Chronic Kidney Disease (CKD) not including primary renal effects of cancer/therapy, specify stage if known. | — |
| `comorbidity_diabetes_mellitus` | No | string | Presence of Diabetes Mellitus as a comorbidity. | — |
| `comorbidity_hypertension` | No | string | Presence of Hypertension as a comorbidity. | — |
| `significant_comorbidities_list` | No | array of string | List of significant co-existing medical conditions at baseline (e.g., Diabetes Mellitus, Hypertension, Cardiovascular Disease, Chronic Kidney Disease, COPD). Can be free text or coded. | — |
| `family_history_other_cancer` | No | string | Indicates if there is a family history of other significant cancers (e.g., breast, ovarian, pancreatic, colorectal). | — |
| `family_history_other_cancer_details` | No | string | Specify type of cancer and relative for other family cancer history. | — |
| `family_history_prostateca` | No | string | Indicates if there is a family history of prostate cancer in first or second-degree relatives. | — |
| `family_history_prostateca_relatives` | No | array of string | Specify relatives with prostate cancer (e.g., Father, Brother, Son). | — |
| `family_history_prostate_cancer` | No | string | Parent, sibling, | — |
| `family_history_prostate_cancer_age` | No | string | Age of onset | — |
| `family_history_breast_cancer` | No | string | Provisional field for breast cancer; operational definition requires review. | — |
| `family_history_colorectal_cancer` | No | string | Provisional field for colorectal cancer; operational definition requires review. | — |
| `family_history_ovarian_cancer` | No | string | Provisional field for ovarian cancer; operational definition requires review. | — |
| `family_history_melanoma` | No | string | Provisional field for melanoma; operational definition requires review. | — |
| `family_history_pancreatic_cancer` | No | string | Provisional field for pancreatic cancer; operational definition requires review. | — |
| `history_prostate_cancer` | No | string | Provisional field for prostate cancer; operational definition requires review. | — |
| `history_bph` | No | string | Benign Prostate Hyperplasia | — |
| `history_prostatitis` | No | string | Provisional field for prostatitis; operational definition requires review. | — |
| `history_diabetes` | No | string | Provisional field for diabetes; operational definition requires review. | — |
| `history_coronary_disease` | No | string | Provisional field for coronary disease; operational definition requires review. | — |
| `history_hypertension` | No | string | Provisional field for hypertension; operational definition requires review. | — |
| `history_heart_failure` | No | string | Provisional field for heart failure; operational definition requires review. | — |
| `history_kidney_stones` | No | string | Provisional field for kidney stones; operational definition requires review. | — |
| `history_bladder_stones` | No | string | Provisional field for bladder stones; operational definition requires review. | — |
| `history_uti` | No | string | History of any prior Urinary Tract Infection | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | Yes | array of object | Link to case records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic medical_history records](../../extensions/lu177_psma/v0.3.0/examples/by_node/medical_history.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
