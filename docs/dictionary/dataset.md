# Dataset (`dataset`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

A set of metadata and associated data file objects originating from single a research study, clinical trial or patient cohort.

| Attribute | Value |
| --- | --- |
| Record grain | One collection |
| Category | `administrative` |
| Navigation group | Governance |
| MIDRC relationship | `preserved_and_extended` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/dataset.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/dataset.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_dataset_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `datasets` | `performed_for` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `acknowledgement` | No | string | Publication acknowledgement(s) for the published dataset. | — |
| `data_citation` | No | string | The citation for the published dataset. | — |
| `data_contributor` | No | string | The name of the organization or individual that the contributed dataset belongs to. | — |
| `data_description` | Yes | string | A brief, free-text description of the data files and associated metadata provided for this dataset. | — |
| `data_url_doi` | No | string | A URL or DOI for the source of the dataset or the contributing organization's website. | — |
| `disease_type` | No | string | The primary type of disease studied in this dataset, if applicable. | — |
| `full_name` | No | string | The full name or title of the dataset or publication. | — |
| `license` | No | string | The license under which the dataset has been published. | — |
| `longitudinal` | No | boolean | Indicates whether the dataset has longitudinal or time-series data. | — |
| `primary_site` | No | string | The primary body site studied in this dataset. | — |
| `publication_citation` | No | string | The major or main publication(s) associated with the data itself or with the publication that published the dataset. | — |
| `research_description` | No | string | If the dataset is related to a research study, provide a brief, free-text description or abstract of the study being performed, for example, the hypothesis being tested and a very brief description of the materials, methods and results. | — |
| `research_design` | No | string | A summary of the goals of the research or a general description of the research's relationship to a clinical application. | — |
| `research_objective` | No | string | The general objective of the research; what the researchers hope to discover or determine. | — |
| `research_setup` | No | string | A high level description of the setup used to achieve the research objectives. | — |
| `submitter_id` | Yes | string | A human-readable identifier for the study's record in the database. It can be used in place of the UUID for identifying or recalling a record. | — |
| `type` | Yes | string (enumerated) | The name of the node in the database to be used in queries. In this case "dataset". | Allowed values: <code>"dataset"</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | one or more of: array of object; object | The code of the project that this dataset belongs to, i.e., a link to the parent node. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic dataset records](../../extensions/lu177_psma/v0.3.0/examples/by_node/dataset.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
