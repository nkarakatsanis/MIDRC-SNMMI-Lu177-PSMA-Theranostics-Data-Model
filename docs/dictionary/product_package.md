# Product Package (`product_package`)

Release **0.4.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

One versioned package specification for a medicinal product, not a physical vial.

| Attribute | Value |
| --- | --- |
| Record grain | One versioned package specification for a medicinal product, not a physical vial. |
| Category | `clinical` |
| Navigation group | Radiopharmaceutical product |
| MIDRC relationship | `new_extension` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.4.0/schemas/product_package.json) · [YAML schema](../../extensions/lu177_psma/v0.4.0/integration/yaml/product_package.yaml) · [Submission template](../../extensions/lu177_psma/v0.4.0/templates/submission_product_package_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `nmmi_product_package_projects` | `member_of` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_product_package_provenance_records` | `documented_by` |
| `medicinal_products` | [medicinal_product](medicinal_product.md) | `many_to_one` | Yes | `nmmi_product_package_medicinal_products` | `package_of` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"product_package"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `package_name` | Yes | string | Human-readable package presentation label. | Minimum length: <code>1</code> |
| `container_type` | Yes | string | Immediate container type, such as vial or syringe. | Minimum length: <code>1</code> |
| `container_material` | No | string | Material of the immediate container. | Minimum length: <code>1</code> |
| `closure_system` | No | string | Closure specification. | Minimum length: <code>1</code> |
| `shielding_configuration` | No | string | Shielding specification and reference; not evidence that a specific unit was handled correctly. | Minimum length: <code>1</code> |
| `nominal_fill_volume_ml` | No | number | Nominal volume per immediate container in mL; actual fill is recorded on the unit. | Minimum: <code>0</code> |
| `headspace_description` | No | string | Nominal headspace composition or specification. | Minimum length: <code>1</code> |
| `secondary_packaging` | No | string | Outer packaging specification. | Minimum length: <code>1</code> |
| `base_quantity` | No | number | Number or amount to which the package specification refers. | Minimum: <code>0</code> |
| `base_unit` | No | string | Unit for base_quantity, separate from activity and concentration units. | Minimum length: <code>1</code> |
| `storage_temperature_min_c` | No | number | Lower labeled storage temperature in degrees Celsius. | — |
| `storage_temperature_max_c` | No | number | Upper labeled storage temperature in degrees Celsius. | — |
| `storage_conditions` | No | string | Versioned storage conditions, including at-rest and in-transit distinctions when supplied. | Minimum length: <code>1</code> |
| `light_protection` | No | string | Protection from light required by the source specification. | Minimum length: <code>1</code> |
| `transport_classification` | No | string | Transport class and governing source/version; not an inferred legal classification. | Minimum length: <code>1</code> |
| `radiation_safety_label` | No | string | Label specification or referenced instruction. | Minimum length: <code>1</code> |
| `expiry_reference_basis` | No | string | Time origin used for labeled shelf life, such as calibration or end of synthesis. | Minimum length: <code>1</code> |
| `shelf_life_hours` | No | number | Specified shelf life in hours under the stated conditions; not a universal product constant. | Minimum: <code>0</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | array of object | Link to project records by code or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"code"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `medicinal_products` | Yes | array of object | Link to medicinal_product records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic product_package records](../../extensions/lu177_psma/v0.4.0/examples/by_node/product_package.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
