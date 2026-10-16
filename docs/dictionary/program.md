# Program (`program`)

Release **0.3.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

A broad framework of goals to be achieved. (NCIt C52647)

| Attribute | Value |
| --- | --- |
| Record grain | One initiative |
| Category | `administrative` |
| Navigation group | Governance |
| MIDRC relationship | `preserved` |
| Submittable | <code>false</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["name"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/program.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/program.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_program_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

No outgoing links are declared.

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `dbgap_accession_number` | Yes | string | The dbgap accession number provided for the program. | — |
| `name` | Yes | string | Full name/title of the program. | — |
| `type` | No | string | No description supplied in the schema. | — |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |

## Synthetic examples

[Read the synthetic program records](../../extensions/lu177_psma/v0.3.0/examples/by_node/program.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
