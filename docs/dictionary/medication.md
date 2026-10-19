# Medication (`medication`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Information related to medication prescribed, dispensed or administered to the case.

| Attribute | Value |
| --- | --- |
| Record grain | One medication exposure or source summary |
| Category | `medical_history` |
| Navigation group | Clinical |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/medication.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/medication.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_medication_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `cases` | [case](case.md) | `many_to_one` | Yes | `medications` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_medication_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `days_to_medication_end` | No | integer | The number of days from the index date to the date the case stopped a specific medication. | — |
| `days_to_medication_start` | No | integer | The number of days from the index date to the date the case started a specific medication. | — |
| `dose_sequence_number` | No | integer | The sequence number of a specific dose of a medication given in a series of doses. | — |
| `medication_code` | No | string | The code for a specific medication, assigned by the code system. | — |
| `medication_code_system` | No | string | The code for a specific medication, assigned by the code system. | Source term: NCIt; C70895; Code System |
| `medication_manufacturer` | No | string | The name of the company that manufactured the medication. | Source term: NCIt; C156626; Drug Manufacturer |
| `medication_name` | No | string | The name of the specific medication the case was prescribed or administered. | Source term: NCIt; C164322; Drug Name |
| `medication_type` | No | string (enumerated) | A categorization of medication used to describe the type of medication the patient was perscribed or administered. | Allowed values: <code>"ACE inhibitors"</code>, <code>"Bronchodilator"</code>, <code>"Chemotherapy"</code>, <code>"Immunosuppressive medication"</code>, <code>"Immunotherapy"</code>, <code>"Inhaled steroids"</code>, <code>"NSAID"</code>, <code>"Protease inhibitor"</code>, <code>"Supplemental oxygen"</code>, <code>"Systemic steroids"</code>, <code>"Vaccine"</code> |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `prior_androgen_receptor_targeted_agent` | No | boolean | Specifies if the patient received prior ARPI therapy (e.g., Abiraterone, Enzalutamide). | — |
| `prior_arpi_names` | No | array of string | List of ARPIs previously administered. | — |
| `prior_chemo_nontaxane_regimens` | No | string | List or description of non-taxane chemotherapy regimens previously administered. | — |
| `prior_chemotherapy_nontaxane` | No | boolean | Specifies if the patient received prior non-taxane chemotherapy regimens. | — |
| `prior_hormonal_other_regimens` | No | string | List or description of other hormonal therapies previously administered. | — |
| `prior_hormonal_therapy_other` | No | boolean | Specifies if the patient received prior hormonal therapies other than initial ADT or the main ARPIs listed separately (e.g., ketoconazole, estrogens). | — |
| `prior_immunotherapy` | No | boolean | Specifies if the patient received prior immunotherapy (e.g., Sipuleucel-T, Pembrolizumab). | — |
| `prior_immunotherapy_regimens` | No | string | List or description of immunotherapies previously administered. | — |
| `prior_other_systemic_therapies` | No | string | Details of other systemic therapies received for prostate cancer (e.g., Sipuleucel-T, Radium-223). | — |
| `prior_radiopharmaceutical_therapy` | No | boolean | Specifies if the patient received prior radiopharmaceutical therapy other than the current Lu-177 PSMA (e.g., Radium-223, Strontium-89). | — |
| `prior_rpt_agent` | No | array of string | Name of the prior therapeutic radiopharmaceutical agent(s) administered. | — |
| `prior_rpt_completion_date` | No | string | Date the last cycle of prior radiopharmaceutical therapy was administered. | Format: <code>"date"</code> |
| `prior_taxane_chemotherapy` | No | boolean | Specifies if the patient received prior taxane-based chemotherapy (e.g., Docetaxel, Cabazitaxel). | — |
| `prior_taxane_names` | No | array of string | List of taxane chemotherapies previously administered. | — |
| `concurrent_therapies_during_lu177` | No | array of string | Any other cancer therapies administered concurrently with Lu-177 PSMA. | — |
| `hormone_therapy` | No | string | Provisional field for hormone therapy; operational definition requires review. | — |
| `chemotherapy` | No | string | Provisional field for chemotherapy; operational definition requires review. | — |
| `immunotherapy` | No | string | Provisional field for Immunotherapy; operational definition requires review. | — |
| `arpi` | No | string | type of treatment | — |
| `other_medication` | No | string | Provisional field for Other medication; operational definition requires review. | — |
| `morphine` | No | string | Provisional field for Morphine; operational definition requires review. | — |
| `fentanyl` | No | string | Provisional field for Fentanyl; operational definition requires review. | — |
| `pain_medication` | No | string | Provisional field for Pain medication; operational definition requires review. | — |
| `start_date` | No | string | Date of medication start date. | Format: <code>"date"</code> |
| `end_date` | No | string | Date of medication end date. | Format: <code>"date"</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | Yes | one or more of: array of object; object | The submitter_id or id of the case receiving this medication, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |
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

[Read the synthetic medication records](../../extensions/lu177_psma/v0.3.0/examples/by_node/medication.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
