# Root (`root`)

Release **0.3.1** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)



| Attribute | Value |
| --- | --- |
| Record grain | One MIDRC root record |
| Category | `internal` |
| Navigation group | Governance |
| MIDRC relationship | `preserved` |
| Submittable | <code>false</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/root.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/root.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_root_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

No outgoing links are declared.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `schema_version` | No | string | No description supplied in the schema. | — |
| `type` | Yes | string | No description supplied in the schema. | — |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"root"</code> |

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
