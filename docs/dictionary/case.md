# Case (`case`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

The collection of all data related to a specific patient or case in the context of a specific dataset or experiment.

| Attribute | Value |
| --- | --- |
| Record grain | One person per project |
| Category | `administrative` |
| Navigation group | Subject |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/case.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/case.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_case_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `datasets` | [dataset](dataset.md) | `many_to_many` | Yes | `cases` | `member_of` |
| `sites` | [site](site.md) | `many_to_one` | No | `nmmi_case_sites` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_case_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `age_at_index` | No | number | The study participant's age, in years, at the index event. The index event is determined by the data submitter and used as an anchor date for all temporal variables. Note that an age of 0 indicates a participant who is younger than 1 year old. For participants with ages greater than 89 years, please use the property 'age_at_index_gt89'. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | Minimum: <code>0</code>; Maximum: <code>89</code>; Source term: NCIt; C181702; Age in Years at Index Date |
| `age_at_index_gt89` | No | string (enumerated) | Indicates whether the subject's age at the time of the study was greater than 89 years. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | Allowed values: <code>"Yes"</code>, <code>"No"</code> |
| `case_ids` | No | array of string | A list of one or more case submitter_ids associated with this data. | — |
| `country_of_residence` | No | string | The country where the subject resides. | Source term: SNOMED; 416647007; Country of residence |
| `covid19_positive` | No | string (enumerated) | An indicator of whether the patient has ever had a positive COVID-19 test or been diagnosed with one of the following ICD-10 COVID-19 conditions: COVID-19 (U07. 1), Influenza due to unidentified influenza virus with other manifestations (J11.8), Post COVID-19 condition (U09.9), Myalgic encephalomyelitis/chronic fatigue syndrome (G93.32), or Sequelae of other specified infectious and parasitic diseases (B94.8). For more information about a patient's specific COVID-19 diagnosis, details can be found under Condition. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Indeterminate"</code>, <code>"Not Reported"</code>; Source term: NCIt; C171614; Positive History of COVID-19 |
| `days_to_death` | No | integer | The number of days from the index date to the date of death. | — |
| `days_to_last_follow_up` | No | integer | The number of days from the index date to the date of last follow-up. | — |
| `ethnicity` | No | string (enumerated) | A social group characterized by a distinctive social and cultural tradition that is maintained from generation to generation. Members share a common history and origin and a sense of identification with the group. They have similar and distinctive features in their lifestyle habits and shared experiences. They often have a common genetic heritage which may be reflected in their experience of health and disease. | Allowed values: <code>"Hispanic or Latino"</code>, <code>"Not Hispanic or Latino"</code>, <code>"Not Reported"</code>; Source term: NCIt; C16564; Ethnic Group; 24.07e |
| `gen3_linked_subjects_available` | No | boolean | Indicates whether there is data available for the subject in other data resources. | — |
| `icu_indicator` | No | boolean | Indicates whether the subject has been admitted to the ICU. | Source term: NCIt; C171454; Intensive Care Unit Stay |
| `index_event` | No | string (enumerated) | The event used as the anchor or start date for all temporal data elements. This acts as day 0 on a timeline of events relating to the patient. This property is included to ensure personal privacy protection in accordance with the HIPAA Safe Harbor Method. More information can be found here https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html. | Allowed values: <code>"COVID-19 Test"</code>, <code>"Long COVID Diagnosis"</code>, <code>"Study Enrollment"</code>, <code>"First Imaging Study"</code> |
| `indoor_biomass_smoke_exposure` | No | string (enumerated) | An indicator confirming exposure to indoor biomass smoke (wood, charcoal). | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `linked_external_data` | No | array of string | A list of all external data resources that are confirmed to have data for the case. | — |
| `long_covid_diagnosis` | No | string (enumerated) | An indicator of whether the patient has ever been diagnosed with one of the following ICD-10 long COVID-19 conditions: U09.9 (Post COVID-19 condition, unspecified), G93.32 (Myalgic encephalomyelitis/chronic fatigue syndrome), and B94.8 (Sequelae of other specified infectious and parasitic diseases). 'Positive' means the patient was diagnosed with a long COVID condition, while 'Not Reported' means the patient has never been diagnosed with a long COVID condition. | Allowed values: <code>"Positive"</code>, <code>"Not Reported"</code>; Source term: NCIt; C179263; Post-Acute Sequelae of COVID-19 |
| `mortality_status` | No | string (enumerated) | Status of participant/subject as alive or dead. | Allowed values: <code>"Alive"</code>, <code>"Deceased"</code>, <code>"Not Reported"</code> |
| `number_of_pack_years` | No | number | If participant is a former or current cigarette smoker, documents the number of pack-years of smoking [(average number smoked daily)/20] x (number of years smoked) = pack-years]. | — |
| `occupational_exposure` | No | string (enumerated) | An indicator confirming occupational risk exposure. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `occupational_exposure_type` | No | string | A description of the type of occupational exposure. | — |
| `patient_category` | No | string (enumerated) | A category describing whether the patient was an inpatient (residing in the hospital where they were being treated), an outpatient (visiting a healthcare facility for diagnosis or treatment but admitted for an overnight stay), or a patient visiting the Intensive Care Unit (ICU). | Allowed values: <code>"Inpatient"</code>, <code>"Outpatient"</code>, <code>"ICU"</code>, <code>"Not Reported"</code> |
| `pulmonary_fibrosis_family_history` | No | string (enumerated) | An indicator confirming a family history of pulmonary fibrosis. | Allowed values: <code>"Yes"</code>, <code>"No"</code>, <code>"Not Reported"</code> |
| `race` | No | string (enumerated) | A geographic ancestral origin category that is assigned to a population group based mainly on physical characteristics that are thought to be distinct and inherent. | Allowed values: <code>"American Indian or Alaska Native"</code>, <code>"Asian"</code>, <code>"Black or African American"</code>, <code>"Native Hawaiian or other Pacific Islander"</code>, <code>"Other"</code>, <code>"White"</code>, <code>"Not Reported"</code>; Source term: NCIt; C17049; Race; 24.07e |
| `race_ethnicity` | No | array of string (enumerated) | Race and/or ethnicity minimum required category as defined in the Revisions to OMB's Statistical Policy Directive No. 15 - Standards for Maintaining, Collecting, and Presenting Federal Data on Race and Ethnicity. Only 7 race minimum categories are enumerated, as determined by SPD 15; this question is presented as 'select all that apply', so single individuals may select multiple categories. There may be additional detailed categories provided in the property 'race_ethnicity_detail'; detailed categories must be subcategories of one of these minimum categories. In the case where race is 'Other', there may be additional information in the property 'race_ethnicity_write_in'. | Each item: (Allowed values: <code>"Other"</code>, <code>"Not Reported"</code>, <code>"American Indian or Alaska Native"</code>, <code>"Asian"</code>, <code>"Black or African American"</code>, <code>"Hispanic or Latino"</code>, <code>"Middle Eastern or North African"</code>, <code>"Native Hawaiian or Pacific Islander"</code>, <code>"White"</code>) |
| `race_ethnicity_detail` | No | array of string (enumerated) | Race and/or ethnicity detailed category as defined in the Revisions to OMB's Statistical Policy Directive No. 15 - Standards for Maintaining, Collecting, and Presenting Federal Data on Race and Ethnicity; this question is presented as 'select all that apply', so single individuals may select multiple categories. Only 6 to 9 detailed race categories are enumerated, as determined by SPD 15; in the case where the detailed category is 'Another group', there may be additional information provided in the property 'race_ethnicity_write_in'. | Each item: (Allowed values: <code>"Another group"</code>, <code>"Not Reported"</code>, <code>"Navajo Nation"</code>, <code>"Blackfeet Tribe of the Blackfeet Indian Reservation of Montana"</code>, <code>"Native Village of Barrow Inupiat Traditional Government"</code>, <code>"Nome Eskimo Community"</code>, <code>"Aztec"</code>, <code>"Maya"</code>, <code>"Chinese"</code>, <code>"Asian Indian"</code>, <code>"Filipino"</code>, <code>"Japanese"</code>, <code>"Korean"</code>, <code>"Vietnamese"</code>, <code>"Pakistani"</code>, <code>"Hmong"</code>, <code>"Afghan"</code>, <code>"African American"</code>, <code>"Jamaican"</code>, <code>"Haitian"</code>, <code>"Nigerian"</code>, <code>"Ethiopian"</code>, <code>"Somali"</code>, <code>"Trinidadian and Tobagonian"</code>, <code>"Ghanaian"</code>, <code>"Congolese"</code>, <code>"Mexican"</code>, <code>"Puerto Rican"</code>, <code>"Cuban"</code>, <code>"Salvadoran"</code>, <code>"Dominican"</code>, <code>"Guatemalan"</code>, <code>"Colombian"</code>, <code>"Honduran"</code>, <code>"Spaniard"</code>, <code>"Lebanese"</code>, <code>"Iranian"</code>, <code>"Egyptian"</code>, <code>"Syrian"</code>, <code>"Iraqi"</code>, <code>"Israeli"</code>, <code>"Moroccan"</code>, <code>"Yemeni"</code>, <code>"Kurdish"</code>, <code>"Native Hawaiian"</code>, <code>"Samoan"</code>, <code>"Chamorro"</code>, <code>"Tongan"</code>, <code>"Fijian"</code>, <code>"Marshallese"</code>, <code>"Chuukese"</code>, <code>"Palauan"</code>, <code>"Tahitian"</code>, <code>"English"</code>, <code>"German"</code>, <code>"Irish"</code>, <code>"Italian"</code>, <code>"Polish"</code>, <code>"Scottish"</code>, <code>"French"</code>, <code>"Swedish"</code>, <code>"Norwegian"</code>) |
| `race_ethnicity_write_in` | No | string | Free-text details related to race and/or ethnicity as defined in the Revisions to OMB's Statistical Policy Directive No. 15 - Standards for Maintaining, Collecting, and Presenting Federal Data on Race and Ethnicity. This property is only used if there is additional race information that does not match any of the minimum or detailed race categories. | — |
| `sex` | No | string (enumerated) | The biologic character or quality that distinguishes male and female from one another as expressed by analysis of the person's gonadal, morphologic (internal and external), chromosomal, and hormonal characteristics. | Allowed values: <code>"Female"</code>, <code>"Male"</code>, <code>"Not Reported"</code>; Source term: NCIt; C28421; Sex |
| `site_id` | No | string | A de-identified code used to classify a case as part of a specific data submission. | Source term: NCIt; C83081; Study Site Identifier |
| `smoking_history` | No | string (enumerated) | Qualitative categorization of the participant's/subject's smoking history. | Allowed values: <code>"Never"</code>, <code>"Former"</code>, <code>"Current"</code>, <code>"Not Reported"</code> |
| `submitter_id` | Yes | string | A human-readable, unique identifier for a record in the metadata database. It can be used in place of the UUID for identifying or recalling a record (e.g., in data queries or uploads/exports). | — |
| `token_record_id` | No | string | An ID used to link a de-identified case in MIDRC to the same case in an external data resource. | — |
| `treatment_info` | No | boolean | Indicates whether detailed treatment information is available for the subject. | Source term: LOINC; 55753-8; Treatment information |
| `type` | Yes | string | The node_id of the node in the data model; the name of the node used in queries and API requests (e.g., "aligned_reads_file" for the "Aligned Reads File" node). | — |
| `ventilator_indicator` | No | boolean | Indicates whether the subject has been on a ventilator. | Source term: SNOMED; 250870006; Ventilator finding |
| `zip` | No | string | The three-digit United States zip code of residence for any population greater than 20,000. For zip codes where the three digit number represents a population less than 20,000 "000" will be provided. | — |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `deidentification_method` | No | string | Documented de-identification approach and profile version. | — |
| `consent_scope` | No | string | Permitted data-use scope; actual enforcement remains with commons authorization. | — |
| `sex_assigned_at_birth` | No | string | Source sex assigned at birth, kept separate from gender identity. | — |
| `gender_identity` | No | string | Self-reported gender identity if collected. | — |
| `age_at_treatment` | No | integer | Patient's age in years at the time they began radiopharmaceutical therapy. | — |
| `geographic_region` | No | string | General geographic region of patient residence (e.g., state, country, or de-identified region for multi-center studies). | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `datasets` | Yes | one or more of: array of object; object | The submitter_id or id of the dataset this case belongs to, i.e., a link to a record in the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>) / 2. object] |
| `sites` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
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

[Read the synthetic case records](../../extensions/lu177_psma/v0.3.0/examples/by_node/case.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
