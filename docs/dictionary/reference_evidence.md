# Reference Evidence (`reference_evidence`)

Release **0.4.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

One citable evidence context, population or experimental dataset; not an individual patient observation.

| Attribute | Value |
| --- | --- |
| Record grain | One citable evidence context, population or experimental dataset; not an individual patient observation. |
| Category | `administrative` |
| Navigation group | Research evidence |
| MIDRC relationship | `new_extension` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.4.0/schemas/reference_evidence.json) · [YAML schema](../../extensions/lu177_psma/v0.4.0/integration/yaml/reference_evidence.yaml) · [Submission template](../../extensions/lu177_psma/v0.4.0/templates/submission_reference_evidence_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `nmmi_reference_evidence_projects` | `member_of` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_reference_evidence_provenance_records` | `documented_by` |
| `radiopharmaceuticals` | [radiopharmaceutical](radiopharmaceutical.md) | `many_to_many` | No | `nmmi_reference_evidence_radiopharmaceuticals` | `describes` |
| `medicinal_products` | [medicinal_product](medicinal_product.md) | `many_to_many` | No | `nmmi_reference_evidence_medicinal_products` | `describes_product` |
| `biological_targets` | [biological_target](biological_target.md) | `many_to_many` | No | `nmmi_reference_evidence_biological_targets` | `describes_target` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"reference_evidence"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `title` | Yes | string | Title or descriptive name of the evidence item. | Minimum length: <code>1</code> |
| `evidence_kind` | Yes | string (enumerated) | Kind of evidence source. | Allowed values: <code>"publication"</code>, <code>"trial"</code>, <code>"regulatory_label"</code>, <code>"experimental_dataset"</code>, <code>"technical_report"</code>, <code>"other"</code> |
| `setting` | Yes | string (enumerated) | Experimental or reference setting; never silently pool species or settings. | Allowed values: <code>"human_clinical"</code>, <code>"preclinical"</code>, <code>"in_vitro"</code>, <code>"computational"</code>, <code>"reference"</code> |
| `source_citation` | Yes | string | Citation or source location; exact identifiers can also be assigned through external_identifier. | Minimum length: <code>1</code> |
| `source_version` | No | string | Document, label, dataset or registry version. | Minimum length: <code>1</code> |
| `source_locator` | No | string | Page, section, table, figure or record locator supporting the assertion. | Minimum length: <code>1</code> |
| `evidence_date` | No | string | Date of the evidence version or observation period as defined by the source. | Format: <code>"date"</code>; Minimum length: <code>1</code> |
| `species` | No | string | Organism represented in the evidence; required for biological experimental results. | Minimum length: <code>1</code> |
| `population_description` | No | string | Population, cell system, species strain or cohort context. | Minimum length: <code>1</code> |
| `disease_context` | No | string | Disease and subtype described in the source; not an anatomical target. | Minimum length: <code>1</code> |
| `treatment_setting` | No | string | Treatment line, prior therapy and other setting constraints. | Minimum length: <code>1</code> |
| `study_design` | No | string | Source-described study design. | Minimum length: <code>1</code> |
| `trial_phase` | No | string | Source-described trial phase; not a permanent agent property. | Minimum length: <code>1</code> |
| `sponsor` | No | string | Study sponsor as reported. | Minimum length: <code>1</code> |
| `comparator` | No | string | Comparator or reference condition. | Minimum length: <code>1</code> |
| `sample_size` | No | integer | Number of experimental units or subjects, interpreted with sample_unit. | Minimum: <code>0</code> |
| `sample_unit` | No | string | Unit counted by sample_size, such as participants, specimens or animals. | Minimum length: <code>1</code> |
| `inclusion_criteria` | No | string | Population inclusion and exclusion summary. | Minimum length: <code>1</code> |
| `biomarker_selection_criteria` | No | string | Biomarker selection rule and source version. | Minimum length: <code>1</code> |
| `primary_endpoint` | No | string | Prespecified primary endpoint and its definition reference. | Minimum length: <code>1</code> |
| `secondary_endpoints` | No | array of string | Secondary endpoints and their definition references. | Unique items: <code>true</code> |
| `generalizability_limits` | No | string | Known limitations on applying the evidence to another context. | Minimum length: <code>1</code> |
| `evidence_level` | No | string | Assessment under a named evidence-grading rubric supplied in provenance. | Minimum length: <code>1</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | array of object | Link to project records by code or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"code"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `radiopharmaceuticals` | No | array of object | Link to radiopharmaceutical records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `medicinal_products` | No | array of object | Link to medicinal_product records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `biological_targets` | No | array of object | Link to biological_target records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic reference_evidence records](../../extensions/lu177_psma/v0.4.0/examples/by_node/reference_evidence.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
