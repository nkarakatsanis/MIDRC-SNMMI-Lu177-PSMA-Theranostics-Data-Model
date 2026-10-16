# Data Release (`data_release`)

Release **0.3.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Internal node to store different data releases.

| Attribute | Value |
| --- | --- |
| Record grain | One MIDRC data release record |
| Category | `internal` |
| Navigation group | Governance |
| MIDRC relationship | `preserved` |
| Submittable | <code>false</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/data_release.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/data_release.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_data_release_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `roots` | [root](root.md) | `many_to_one` | Yes | `data_releases` | `describes` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `major_version` | Yes | integer | The number identifying the major version. | — |
| `minor_version` | Yes | integer | The number identifying the minor version. | — |
| `name` | Yes | string | String representing release name. | — |
| `release_date` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `released` | No | boolean | Indicates if it is the current release. | Default: <code>false</code> |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"data_release"</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `roots` | No | one or more of: array of object; object | No description supplied in the schema. | One or more alternatives: [1. array of object: Each item: (Minimum items: <code>1</code>; Maximum items: <code>1</code>) / 2. object] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
