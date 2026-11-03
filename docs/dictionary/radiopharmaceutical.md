# Radiopharmaceutical (`radiopharmaceutical`)

Release **0.4.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Radiopharmaceutical product identity independent of a particular batch or administration.

| Attribute | Value |
| --- | --- |
| Record grain | One reference agent in the v0.4 profile. Existing product-like records remain readable; migrate them explicitly rather than silently reinterpreting their identifiers. |
| Category | `clinical` |
| Navigation group | Radiopharmaceutical reference |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.4.0/schemas/radiopharmaceutical.json) · [YAML schema](../../extensions/lu177_psma/v0.4.0/integration/yaml/radiopharmaceutical.yaml) · [Submission template](../../extensions/lu177_psma/v0.4.0/templates/submission_radiopharmaceutical_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `nmmi_radiopharmaceutical_projects` | `member_of` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_provenance_records` | `documented_by` |
| `radionuclide_records` | [radionuclide](radionuclide.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_radionuclide_records` | `has_identity` |
| `molecular_entities` | [molecular_entity](molecular_entity.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_molecular_entities` | `has_component` |
| `biological_targets` | [biological_target](biological_target.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_biological_targets` | `has_identity` |
| `chelators` | [molecular_entity](molecular_entity.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_chelators` | `has_component` |
| `linkers` | [molecular_entity](molecular_entity.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_linkers` | `has_component` |
| `targeting_vectors` | [molecular_entity](molecular_entity.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_targeting_vectors` | `has_component` |
| `precursors` | [molecular_entity](molecular_entity.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_precursors` | `has_component` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"radiopharmaceutical"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `name` | Yes | string | Radiopharmaceutical product name. | — |
| `radionuclide` | No | string | Radionuclide label such as Lu-177. | — |
| `molecular_target` | No | string | Target such as PSMA. | — |
| `product_code` | No | string | Product identifier, including NDC when applicable. | — |
| `code_system` | No | string | Product coding system. | — |
| `production_type` | No | string | Production route or product category. | — |
| `non_active_ingredients` | No | string | Description of inactive ingredients. | — |
| `physical_half_life_seconds` | No | number | Physical radionuclide half-life with reference source. | Minimum: <code>0</code> |
| `identity_scope` | No | string (enumerated) | Identity level of this record. New v0.4 reference-agent records are distinct from legacy product-like records; migration must preserve old identifiers. | Allowed values: <code>"reference_agent"</code>, <code>"legacy_product"</code> |
| `agent_class` | No | string | Functional class of the reference agent; product, lot and administration are separate identities in the v0.4 profile. | Minimum length: <code>1</code> |
| `intended_use` | No | array of string | Intended diagnostic, therapeutic or investigational uses, supported by versioned evidence. | Unique items: <code>true</code> |
| `valency` | No | integer | Number of targeting motifs per construct. | Minimum: <code>0</code> |
| `multimerization_state` | No | string | Monomeric or multimeric structural specification. | Minimum length: <code>1</code> |
| `albumin_binding_moiety` | No | boolean | Presence of a structurally specified albumin-binding moiety; not a measured plasma binding fraction. | — |
| `conjugation_site` | No | string | Site of conjugation in the specified molecular construct. | Minimum length: <code>1</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | array of object | Link to project records by code or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"code"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `radionuclide_records` | No | array of object | Link to radionuclide records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `molecular_entities` | No | array of object | Link to molecular_entity records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `biological_targets` | No | array of object | Link to biological_target records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `chelators` | No | array of object | Link to molecular_entity records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `linkers` | No | array of object | Link to molecular_entity records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `targeting_vectors` | No | array of object | Link to molecular_entity records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `precursors` | No | array of object | Link to molecular_entity records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic radiopharmaceutical records](../../extensions/lu177_psma/v0.4.0/examples/by_node/radiopharmaceutical.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
