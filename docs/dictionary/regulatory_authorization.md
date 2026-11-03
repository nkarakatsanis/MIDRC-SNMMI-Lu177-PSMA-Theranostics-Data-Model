# Regulatory Authorization (`regulatory_authorization`)

Release **0.4.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

One product-specific regulatory application or authorization state in one jurisdiction at a stated date.

| Attribute | Value |
| --- | --- |
| Record grain | One product-specific regulatory application or authorization state in one jurisdiction at a stated date. |
| Category | `clinical` |
| Navigation group | Radiopharmaceutical product |
| MIDRC relationship | `new_extension` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.4.0/schemas/regulatory_authorization.json) · [YAML schema](../../extensions/lu177_psma/v0.4.0/integration/yaml/regulatory_authorization.yaml) · [Submission template](../../extensions/lu177_psma/v0.4.0/templates/submission_regulatory_authorization_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `nmmi_regulatory_authorization_projects` | `member_of` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_regulatory_authorization_provenance_records` | `documented_by` |
| `medicinal_products` | [medicinal_product](medicinal_product.md) | `many_to_one` | Yes | `nmmi_regulatory_authorization_medicinal_products` | `authorizes` |
| `reference_products` | [medicinal_product](medicinal_product.md) | `many_to_many` | No | `nmmi_regulatory_authorization_reference_products` | `references` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"regulatory_authorization"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `application_identifier` | No | string | NDA, ANDA, IND, marketing-authorization or other identifier; preserve leading zeros and identifier scheme. | Minimum length: <code>1</code> |
| `application_type` | Yes | string | Application type under the named authority; do not infer approval from an NDC or application number. | Minimum length: <code>1</code> |
| `regulatory_pathway` | No | string | Legal pathway with authority and source citation; section references require regulatory review. | Minimum length: <code>1</code> |
| `authority` | Yes | string | Regulatory authority responsible for the application or authorization. | Minimum length: <code>1</code> |
| `jurisdiction` | Yes | string | Jurisdiction to which this state applies. | Minimum length: <code>1</code> |
| `authorization_holder` | No | string | Marketing authorization holder, distinct from manufacturer, supplier and labeler. | Minimum length: <code>1</code> |
| `status` | Yes | string | Source-reported regulatory state, not inferred from availability or marketing codes. | Minimum length: <code>1</code> |
| `status_date` | Yes | string | Date to which the recorded regulatory status applies. | Format: <code>"date"</code>; Minimum length: <code>1</code> |
| `approval_date` | No | string | Actual approval date when supported by the source. | Format: <code>"date"</code>; Minimum length: <code>1</code> |
| `approved_indication` | No | string | Source wording or reviewed representation of the indication for this authorization and label version. | Minimum length: <code>1</code> |
| `label_version` | No | string | Approved or investigational label/protocol version associated with the assertion. | Minimum length: <code>1</code> |
| `reference_application_identifier` | No | string | Identifier of the reference application with its scheme/authority in the source. | Minimum length: <code>1</code> |
| `reference_relationship` | No | string | Relationship to a reference product, such as RLD or comparator; equivalence is an evidence assertion, not automatic identity. | Minimum length: <code>1</code> |
| `submission_strategy` | No | string | Administrative filing context such as a grouped supplement, if relevant. | Minimum length: <code>1</code> |
| `source_citation` | Yes | string | Authoritative source and locator supporting the regulatory assertion. | Minimum length: <code>1</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | array of object | Link to project records by code or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"code"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `medicinal_products` | Yes | array of object | Link to medicinal_product records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `reference_products` | No | array of object | Link to medicinal_product records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic regulatory_authorization records](../../extensions/lu177_psma/v0.4.0/examples/by_node/regulatory_authorization.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
