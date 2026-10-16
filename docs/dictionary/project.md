# Project (`project`)

Release **0.3.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Any specifically defined piece of work that is undertaken or attempted to meet a single requirement. (NCIt C47885)

| Attribute | Value |
| --- | --- |
| Record grain | One access-controlled project |
| Category | `administrative` |
| Navigation group | Governance |
| MIDRC relationship | `preserved` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["code"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/project.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/project.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_project_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `programs` | [program](program.md) | `many_to_one` | Yes | `projects` | `member_of` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `acknowledgement` | No | string | Publication acknowledgement(s) for the published dataset. | — |
| `availability_mechanism` | No | string | Mechanism by which the project will be made avilable. | — |
| `availability_type` | No | string (enumerated) | Is the project open or restricted? | Allowed values: <code>"Open"</code>, <code>"Restricted"</code> |
| `code` | Yes | string | Unique identifier for the project. | — |
| `complete` | No | string (enumerated) | Description of whether the project submission is complete or still in progress. | Allowed values: <code>"Complete"</code>, <code>"Incomplete"</code> |
| `data_citation` | No | string | The citation for the published dataset. | — |
| `data_contributor` | No | string | The name of the organization or individual that the contributed dataset belongs to. | — |
| `data_description` | No | string | A brief, free-text description of the data files and associated metadata provided for this dataset. | — |
| `data_url_doi` | No | string | A URL or DOI for the source of the dataset or the contributing organization's website. | — |
| `date_collected` | No | string | The date or date range in which the project data was collected. | — |
| `dbgap_accession_number` | Yes | string | The dbgap accession number provided for the project. | — |
| `disease_type` | No | string | The primary type of disease studied in this dataset, if applicable. | — |
| `investigator_affiliation` | No | string | The investigator's affiliation with respect to a research institution. | — |
| `investigator_name` | No | string | Name of the principal investigator for the project. | — |
| `license` | No | string | The license under which the dataset has been published. | — |
| `longitudinal` | No | boolean | Indicates whether the dataset has longitudinal or time-series data. | — |
| `name` | Yes | string | Display name/brief description for the project. | — |
| `primary_site` | No | string | The primary body site studied in this dataset. | — |
| `publication_citation` | No | string | The major or main publication(s) associated with the data itself or with the publication that published the dataset. | — |
| `research_description` | No | string | If the dataset is related to a research study, provide a brief, free-text description or abstract of the study being performed, for example, the hypothesis being tested and a very brief description of the materials, methods and results. | — |
| `research_design` | No | string | A summary of the goals of the research or a general description of the research's relationship to a clinical application. | — |
| `research_objective` | No | string | The general objective of the research; what the researchers hope to discover or determine. | — |
| `research_setup` | No | string | A high level description of the setup used to achieve the research objectives. | — |
| `support_id` | No | string | The ID of the source providing support/grant resources. | — |
| `support_source` | No | string | The name of source providing support/grant resources. | — |
| `type` | No | string | No description supplied in the schema. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `programs` | Yes | one or more of: array of object; object | The program to which the project belongs. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | UUID for the project. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `intended_release_date` | No | string | Tracks a Project's intended release date. | Format: <code>"date-time"</code> |
| `releasable` | No | boolean | A project can only be released by the user when `releasable` is true. | Default: <code>false</code> |
| `released` | No | boolean | To release a project is to tell the GDC to include all submitted entities in the next GDC index. | Default: <code>false</code> |
| `state` | No | string (enumerated) | The possible states a project can be in. All but 'open' are equivalent to some type of locked state. | Allowed values: <code>"open"</code>, <code>"review"</code>, <code>"submitted"</code>, <code>"processing"</code>, <code>"closed"</code>; Default: <code>"open"</code> |

## Synthetic examples

[Read the synthetic project records](../../extensions/lu177_psma/v0.3.0/examples/by_node/project.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
