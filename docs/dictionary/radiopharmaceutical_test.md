# Radiopharmaceutical Test (`radiopharmaceutical_test`)

Release **0.4.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

One nonpatient QC, biological-reference or computational-evaluation result with an explicit subject and method.

| Attribute | Value |
| --- | --- |
| Record grain | One nonpatient QC, biological-reference or computational-evaluation result with an explicit subject and method. |
| Category | `clinical` |
| Navigation group | Radiopharmaceutical evidence |
| MIDRC relationship | `new_extension` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.4.0/schemas/radiopharmaceutical_test.json) · [YAML schema](../../extensions/lu177_psma/v0.4.0/integration/yaml/radiopharmaceutical_test.yaml) · [Submission template](../../extensions/lu177_psma/v0.4.0/templates/submission_radiopharmaceutical_test_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `projects` | [project](project.md) | `many_to_one` | Yes | `nmmi_radiopharmaceutical_test_projects` | `member_of` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_radiopharmaceutical_test_provenance_records` | `documented_by` |
| `radiopharmaceutical_batches` | [radiopharmaceutical_batch](radiopharmaceutical_batch.md) | `many_to_one` | No | `nmmi_radiopharmaceutical_test_radiopharmaceutical_batches` | `assesses` |
| `material_lots` | [material_lot](material_lot.md) | `many_to_one` | No | `nmmi_radiopharmaceutical_test_material_lots` | `assesses` |
| `radiopharmaceutical_units` | [radiopharmaceutical_unit](radiopharmaceutical_unit.md) | `many_to_one` | No | `nmmi_radiopharmaceutical_test_radiopharmaceutical_units` | `assesses` |
| `reference_evidence` | [reference_evidence](reference_evidence.md) | `many_to_one` | No | `nmmi_radiopharmaceutical_test_reference_evidence` | `assesses` |
| `computational_models` | [computational_model](computational_model.md) | `many_to_one` | No | `nmmi_radiopharmaceutical_test_computational_models` | `assesses` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"radiopharmaceutical_test"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `test_context` | Yes | string (enumerated) | Nonpatient context. Individual patient laboratory and ROI results remain MIDRC measurement records. | Allowed values: <code>"batch_qc"</code>, <code>"material_qc"</code>, <code>"unit_qc"</code>, <code>"reference_result"</code>, <code>"model_evaluation"</code> |
| `quantity_name` | Yes | string | Quantity or finding assessed, such as radiochemical purity, binding affinity or cohort median PFS. | Minimum length: <code>1</code> |
| `quantity_code` | No | string | Reviewed identifier for the test quantity, if available. | Minimum length: <code>1</code> |
| `quantity_code_system` | No | string | Code system for quantity_code. | Minimum length: <code>1</code> |
| `quantity_code_version` | No | string | Release of the coding system. | Minimum length: <code>1</code> |
| `method_name` | Yes | string | Assay, calculation or assessment method. | Minimum length: <code>1</code> |
| `method_version` | No | string | Assay/SOP/software version. | Minimum length: <code>1</code> |
| `result_status` | Yes | string (enumerated) | Result availability; pending is not negative or failed. | Allowed values: <code>"final"</code>, <code>"preliminary"</code>, <code>"pending"</code>, <code>"not_performed"</code>, <code>"invalid"</code> |
| `result_text` | No | string | Qualitative result or narrative interpretation; no inherited MIDRC patient-result enum is broadened. | Minimum length: <code>1</code> |
| `unit` | No | string | Unit of numerical result, preferably reviewed UCUM; fraction and percent must be distinguished. | Minimum length: <code>1</code> |
| `result_operator` | No | string (enumerated) | Relation between result and reported numerical bound. | Allowed values: <code>"eq"</code>, <code>"lt"</code>, <code>"le"</code>, <code>"gt"</code>, <code>"ge"</code>, <code>"approx"</code> |
| `statistic` | No | string | Statistic such as mean, median, fraction or standard deviation; cohort summaries require a population context. | Minimum length: <code>1</code> |
| `assay_datetime` | No | string | When the assay was performed, with UTC offset. | Format: <code>"date-time"</code>; Minimum length: <code>1</code> |
| `activity_reference_datetime` | No | string | Timestamp to which any activity-dependent quantity was decay-referenced. | Format: <code>"date-time"</code>; Minimum length: <code>1</code> |
| `analyte_basis` | No | string | Chemical species and denominator, such as total compound mass or total compound molar amount. | Minimum length: <code>1</code> |
| `anatomic_context` | No | string | Organ, tissue, lesion class, source region or reference region in the evidence; not a patient lesion identifier. | Minimum length: <code>1</code> |
| `matrix` | No | string | Assay matrix such as serum, plasma, solvent or cell system. | Minimum length: <code>1</code> |
| `time_after_administration_hours` | No | number | Elapsed time in the referenced experimental context; not the date of a patient event. | — |
| `temperature_c` | No | number | Assay temperature in degrees Celsius. | — |
| `ph` | No | number | Assay pH, with measurement method in the evidence. | — |
| `uncertainty_value` | No | number | Uncertainty magnitude for the numerical result. | Minimum: <code>0</code> |
| `uncertainty_unit` | No | string | Unit or explicit dimensionless designation for uncertainty_value. | Minimum length: <code>1</code> |
| `uncertainty_kind` | No | string | Uncertainty statistic and confidence level where applicable. | Minimum length: <code>1</code> |
| `specification_version` | No | string | Version of the acceptance specification used for a QC judgment. | Minimum length: <code>1</code> |
| `acceptance_lower` | No | number | Lower numerical acceptance limit, in unit, when appropriate. | — |
| `acceptance_upper` | No | number | Upper numerical acceptance limit, in unit, when appropriate. | — |
| `acceptance_decision` | No | string (enumerated) | Recorded evaluation against the named specification; not a clinical release authorization. | Allowed values: <code>"pass"</code>, <code>"fail"</code>, <code>"not_evaluated"</code> |
| `decay_correction_basis` | No | string | Decay correction method, nuclide and time reference for yield, activity or purity results. | Minimum length: <code>1</code> |
| `reference_radiation` | No | string | Reference radiation and endpoint required to interpret RBE or other relative radiobiological quantities. | Minimum length: <code>1</code> |
| `rubric_name` | No | string | Named assessment rubric required for readiness, evidence or quality scores. | Minimum length: <code>1</code> |
| `rubric_version` | No | string | Version of the scoring rubric. | Minimum length: <code>1</code> |
| `test_result_number` | No | number | The result a test represented by a number. | — |
| `test_result_percent` | No | number | The result a test represented by a percent. | — |
| `test_result_ratio` | No | number | The result a test represented by a ratio. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `projects` | Yes | array of object | Link to project records by code or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"code"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `radiopharmaceutical_batches` | No | array of object | Link to radiopharmaceutical_batch records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `material_lots` | No | array of object | Link to material_lot records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `radiopharmaceutical_units` | No | array of object | Link to radiopharmaceutical_unit records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `reference_evidence` | No | array of object | Link to reference_evidence records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `computational_models` | No | array of object | Link to computational_model records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic radiopharmaceutical_test records](../../extensions/lu177_psma/v0.4.0/examples/by_node/radiopharmaceutical_test.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
