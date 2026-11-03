# External Identifier (`external_identifier`)

Release **0.4.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

One reviewed external identifier assignment to one explicitly typed entity; schema-level ontology mappings remain semantic_mapping records.

| Attribute | Value |
| --- | --- |
| Record grain | One reviewed external identifier assignment to one explicitly typed entity; schema-level ontology mappings remain semantic_mapping records. |
| Category | `administrative` |
| Navigation group | Semantics and governance |
| MIDRC relationship | `new_extension` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.4.0/schemas/external_identifier.json) · [YAML schema](../../extensions/lu177_psma/v0.4.0/integration/yaml/external_identifier.yaml) · [Submission template](../../extensions/lu177_psma/v0.4.0/templates/submission_external_identifier_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `nmmi_external_identifier_projects` | `member_of` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_external_identifier_provenance_records` | `documented_by` |
| `radiopharmaceuticals` | [radiopharmaceutical](radiopharmaceutical.md) | `many_to_one` | No; group 1 | `nmmi_external_identifier_radiopharmaceuticals` | `identifies` |
| `radionuclides` | [radionuclide](radionuclide.md) | `many_to_one` | No; group 1 | `nmmi_external_identifier_radionuclides` | `identifies` |
| `molecular_entities` | [molecular_entity](molecular_entity.md) | `many_to_one` | No; group 1 | `nmmi_external_identifier_molecular_entities` | `identifies` |
| `biological_targets` | [biological_target](biological_target.md) | `many_to_one` | No; group 1 | `nmmi_external_identifier_biological_targets` | `identifies` |
| `medicinal_products` | [medicinal_product](medicinal_product.md) | `many_to_one` | No; group 1 | `nmmi_external_identifier_medicinal_products` | `identifies` |
| `product_packages` | [product_package](product_package.md) | `many_to_one` | No; group 1 | `nmmi_external_identifier_product_packages` | `identifies` |
| `regulatory_authorizations` | [regulatory_authorization](regulatory_authorization.md) | `many_to_one` | No; group 1 | `nmmi_external_identifier_regulatory_authorizations` | `identifies` |
| `reference_evidence` | [reference_evidence](reference_evidence.md) | `many_to_one` | No; group 1 | `nmmi_external_identifier_reference_evidence` | `identifies` |

Group 1: **exactly one populated member** among `radiopharmaceuticals`, `radionuclides`, `molecular_entities`, `biological_targets`, `medicinal_products`, `product_packages`, `regulatory_authorizations`, `reference_evidence`.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"external_identifier"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `identifier` | Yes | string | Exact external code as a string, preserving leading zeros, hyphens and case where significant. | Minimum length: <code>1</code> |
| `identifier_system` | Yes | string | Identifier authority or scheme, such as RxNorm, UNII, CAS, NDC, MPID, PhPID, PubChem, DOI or PMID. | Minimum length: <code>1</code> |
| `identifier_system_version` | No | string | Release or version of the identifier system. | Minimum length: <code>1</code> |
| `identifier_level` | Yes | string | Semantic level, such as RxNorm IN/PIN/SCD/SBD, NDC product/package, substance, medicinal product or publication. | Minimum length: <code>1</code> |
| `preferred_label` | No | string | Label from the identifier authority at the stated version. | Minimum length: <code>1</code> |
| `jurisdiction` | No | string | Jurisdiction where relevant to the identifier assignment. | Minimum length: <code>1</code> |
| `issuer` | No | string | Issuing authority where not inherent in identifier_system. | Minimum length: <code>1</code> |
| `mapping_relation` | Yes | string (enumerated) | Reviewed relationship between the linked entity and external concept; candidate is not validated equivalence. | Allowed values: <code>"exact"</code>, <code>"narrower"</code>, <code>"broader"</code>, <code>"related"</code>, <code>"candidate"</code> |
| `review_status` | Yes | string (enumerated) | Review state of this assignment. | Allowed values: <code>"unreviewed"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"rejected"</code> |
| `source_citation` | Yes | string | Source supporting the identifier assignment and its semantic level. | Minimum length: <code>1</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | array of object | Link to project records by code or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"code"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `radiopharmaceuticals` | No | array of object | Link to radiopharmaceutical records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `radionuclides` | No | array of object | Link to radionuclide records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `molecular_entities` | No | array of object | Link to molecular_entity records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `biological_targets` | No | array of object | Link to biological_target records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `medicinal_products` | No | array of object | Link to medicinal_product records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `product_packages` | No | array of object | Link to product_package records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `regulatory_authorizations` | No | array of object | Link to regulatory_authorization records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `reference_evidence` | No | array of object | Link to reference_evidence records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic external_identifier records](../../extensions/lu177_psma/v0.4.0/examples/by_node/external_identifier.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
