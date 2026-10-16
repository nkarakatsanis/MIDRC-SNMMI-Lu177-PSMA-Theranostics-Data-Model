# Clinical Assessment (`clinical_assessment`)

Release **0.3.0** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Symptoms, signs, performance status and baseline clinical assessment.

| Attribute | Value |
| --- | --- |
| Record grain | One assessment time |
| Category | `clinical` |
| Navigation group | Clinical |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/clinical_assessment.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/clinical_assessment.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_clinical_assessment_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `cases` | [case](case.md) | `many_to_one` | Yes | `nmmi_clinical_assessment_cases` | `related_to` |
| `timepoints` | [timepoint](timepoint.md) | `many_to_one` | No | `nmmi_clinical_assessment_timepoints` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_clinical_assessment_provenance_records` | `documented_by` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"clinical_assessment"</code> |
| `submitter_id` | Yes | string | Stable submitter-assigned identifier, unique within a project. Do not encode direct patient identifiers. | Minimum length: <code>1</code> |
| `model_version` | No | string | Version of the submitting theranostics extension, independently of the MIDRC baseline version. | — |
| `record_status` | No | string | Record curation state, independent of clinical value. | Allowed values: <code>"draft"</code>, <code>"reviewed"</code>, <code>"approved"</code>, <code>"superseded"</code>, <code>"withdrawn"</code> |
| `source_record_id` | No | string | Identifier of the originating source record; use an approved pseudonym when needed. | — |
| `source_system` | No | string | Source system or data provider. | — |
| `missing_properties` | No | array of string | Names of properties missing from this record; no missing value is encoded as zero. | — |
| `missing_reasons` | No | array of string (enumerated) | Reasons corresponding by index to missing_properties. | Each item: (Allowed values: <code>"unknown"</code>, <code>"not_collected"</code>, <code>"not_applicable"</code>, <code>"not_available"</code>, <code>"withheld"</code>, <code>"pending"</code>) |
| `assessment_datetime` | No | string | ISO 8601 assessment datetime; use approved date shifting consistently within the case. | Format: <code>"date-time"</code> |
| `days_from_course_start` | No | number | Signed elapsed days from the linked therapy course start. | — |
| `time_basis` | No | string | Interpretation of stored dates and elapsed times. | Allowed values: <code>"actual"</code>, <code>"shifted"</code>, <code>"relative_only"</code>, <code>"unknown"</code> |
| `time_window_start_day` | No | number | Beginning of assessment window relative to course start, in days. | — |
| `time_window_end_day` | No | number | End of assessment window relative to course start, in days. | — |
| `hypotension` | No | string | Provisional field for Hypotension; operational definition requires review. | — |
| `hypertension` | No | string | Provisional field for Hypertension; operational definition requires review. | — |
| `hyponatremia` | No | string | Provisional field for Hyponatremia; operational definition requires review. | — |
| `hypernatremia` | No | string | Provisional field for Hypernatremia; operational definition requires review. | — |
| `hypokalemia` | No | string | Provisional field for Hypokalemia; operational definition requires review. | — |
| `hyperkalemia` | No | string | Provisional field for Hyperkalemia; operational definition requires review. | — |
| `hypomagnesia` | No | string | Provisional field for Hypomagnesia; operational definition requires review. | — |
| `pruritis` | No | string | Provisional field for Pruritis; operational definition requires review. | — |
| `urinary_retention` | No | boolean | The presence of oliguria or anuria for the past several hours or suprapubic fullness. | — |
| `urinary_incontinence` | No | boolean | The presence of urge, overflow, stress, or mixed urinary incontinence. | — |
| `fecal_incontinence` | No | boolean | Presence of fecal incontinence. | — |
| `dysuria` | No | boolean | Presence of pain or burning with micturition. | — |
| `impotency` | No | boolean | Presence of erectile dysfunction. | — |
| `bone_pain_spine_pelvis_ribs_femur_joints_back` | No | boolean | Presence of bone pain, e.g., in vertebrae. | — |
| `hypogastric_pain` | No | boolean | Presence of pain or tenderness of the hypogastric area. | — |
| `loss_of_appetite_synomym_anorexia` | No | boolean | Loss of appetite. | — |
| `weight_loss_ctcae_weight_decreased_or_cachexia` | No | boolean | Presence of unintentional weight loss in the past few weeks or months. | — |
| `fatigue` | No | boolean | Presence of fatigue despite getting enough sleep. | — |
| `urinary_urgency` | No | boolean | Presence of urgency to void. | — |
| `hesitancy` | No | boolean | Presence of hesitancy with micturition. | — |
| `hematuria` | No | boolean | Presence of gross hematuria, i.e., blood in urine. | — |
| `hematospermia` | No | boolean | Presence of gross hematospermia, i.e., blood in semen. | — |
| `nocturia` | No | boolean | Having to wake up at least once during nighttime sleep to urinate, disrupting sleep. | — |
| `dribbling` | No | boolean | Post-void involuntary leakage of a few drops of urine after the patient finished urinating. | — |
| `ipss` | No | integer | International Prostate Symptom Score (total score). | — |
| `urinary_frequency` | No | boolean | Presence of a need to urinate more often than usual during waking hours. | — |
| `back_pain` | No | boolean | Presence of pain, tension, or stiffness in the back. | — |
| `arthralgia` | No | boolean | Presence of joint pain (without necessarily implying inflammation). | — |
| `spine_compression` | No | boolean | Presence of diagnosed spinal cord compression or vertebral compression fracture. | — |
| `pelvic_pain` | No | boolean | Presence of pain or discomfort in the lower abdomen or pelvic region. | — |
| `numbness` | No | boolean | Presence of partial or total loss of sensation, typically in extremities. | — |
| `paralysis` | No | boolean | Presence of partial or complete loss of voluntary muscle function in one or more body parts. | — |
| `weakness_limbs_leg` | No | boolean | Presence of reduced strength or inability to move limbs/legs against resistance. | — |
| `neuralgia` | No | boolean | Presence of severe, shooting, or throbbing pain along the distribution of a nerve. | — |
| `erectile_dysfunction` | No | boolean | Presence of inability to achieve or maintain an erection sufficient for satisfactory sexual performance. | — |
| `reduced_libido` | No | boolean | Presence of a noticeable decrease in sexual desire or drive. | — |
| `painful_ejaculation` | No | boolean | Presence of pain or burning sensation during or immediately after ejaculation. | — |
| `infertility` | No | boolean | Diagnosed inability to conceive after 12 months of regular, unprotected intercourse. | — |
| `osteoporosis` | No | boolean | Diagnosed metabolic bone disease characterized by low bone mass (e.g., DEXA T-score ≤ -2.5). | — |
| `metabolic_syndrome` | No | boolean | Diagnosed cluster of conditions (hypertension, hyperglycemia, abnormal cholesterol/triglycerides, excess body fat). | — |
| `baseline_bowel_function_summary` | No | string | Qualitative summary of baseline bowel function (e.g., regular, constipation, diarrhea), if not captured by specific symptom grading. | — |
| `baseline_pain_score_type` | No | string | The standardized scale used to assess baseline pain (e.g., NRS, Brief Pain Inventory - Severity). | — |
| `baseline_pain_severity_score` | No | integer | Patient-reported pain severity score at baseline using a standardized scale (e.g., 0-10 Numerical Rating Scale, BPI item). | — |
| `baseline_urinary_symptoms_severity` | No | integer | Severity of urinary symptoms at baseline, if assessed (e.g., using IPSS score or qualitative description). | — |
| `ecog_status_assessment_date` | No | string | Date when the ECOG performance status was assessed. | Format: <code>"date"</code> |
| `ecog_status_baseline` | No | integer | Eastern Cooperative Oncology Group (ECOG) performance status at baseline prior to PSMA theranostics. | — |
| `ecog_status_value` | No | integer | ECOG performance status assessed at a specific timepoint (baseline, during therapy, follow-up). | — |
| `mibg` | No | string | Provisional field for MIBG; operational definition requires review. | — |
| `integer` | No | string | Provisional field for Integer; operational definition requires review. | — |
| `temperature` | No | string | Provisional field for temperature; operational definition requires review. | — |
| `blood_pressure` | No | string | Provisional field for blood pressure; operational definition requires review. | — |
| `heart_rate` | No | string | Provisional field for heart rate; operational definition requires review. | — |
| `respiratory_rate` | No | string | Provisional field for respiratory rate; operational definition requires review. | — |
| `o2_saturation` | No | string | Provisional field for O2 saturation; operational definition requires review. | — |
| `lap` | No | string | Provisional field for LAP; operational definition requires review. | — |
| `cachexia` | No | string | Provisional field for cachexia; operational definition requires review. | — |
| `pallor` | No | string | Provisional field for pallor; operational definition requires review. | — |
| `paresthesia` | No | string | Provisional field for paresthesia; operational definition requires review. | — |
| `paresis` | No | string | Provisional field for paresis; operational definition requires review. | — |
| `lymphedema` | No | string | Provisional field for lymphedema; operational definition requires review. | — |
| `bone_tenderness` | No | string | Provisional field for bone tenderness; operational definition requires review. | — |
| `overdistented_bladder` | No | string | Provisional field for overdistented bladder; operational definition requires review. | — |
| `abnormal_dre` | No | string | Provisional field for abnormal DRE; operational definition requires review. | — |
| `dre_firmness` | No | string | Provisional field for DRE firmness; operational definition requires review. | — |
| `dre_nodule` | No | string | Provisional field for DRE nodule; operational definition requires review. | — |
| `dre_asymmetry` | No | string | Provisional field for DRE asymmetry; operational definition requires review. | — |
| `loss_of_appetite` | No | string | Provisional field for loss of appetite; operational definition requires review. | — |
| `weight_loss` | No | string | Presence of unintentional weight loss | — |
| `urgency` | No | string | Provisional field for urgency; operational definition requires review. | — |
| `bone_pain` | No | string | Provisional field for bone pain; operational definition requires review. | — |
| `low_back_pain` | No | string | Provisional field for low back pain; operational definition requires review. | — |
| `tracer` | No | string | Provisional field for Tracer; operational definition requires review. | — |
| `pain_at_bony_sites` | No | string | Provisional field for pain at bony sites; operational definition requires review. | — |
| `functional_status_ecog_score` | No | string | Provisional field for functional status (ECOG score); operational definition requires review. | — |
| `diahhrea` | No | string | Provisional field for diahhrea; operational definition requires review. | — |
| `dry_mouth` | No | string | Provisional field for dry mouth; operational definition requires review. | — |
| `bowel_movement_regularity` | No | string | Provisional field for bowel movement regularity; operational definition requires review. | — |
| `appetite` | No | string | Provisional field for appetite; operational definition requires review. | — |
| `nausea` | No | string | Provisional field for nausea; operational definition requires review. | — |
| `swelling_of_feet` | No | string | Provisional field for swelling of feet; operational definition requires review. | — |
| `prior_treatment_chemotherapy_androgen_receptor_antagonists_surgery_etc` | No | string | Provisional field for prior treatment (chemotherapy, androgen receptor antagonists, surgery, etc); operational definition requires review. | — |
| `comorbitities_diabetes_hypertension_other_disease_affecting_kidneys_and_immune_system` | No | string | Provisional field for comorbitities (diabetes, hypertension, other disease affecting kidneys and immune system); operational definition requires review. | — |
| `prostate_cancer_stage` | No | string | Provisional field for prostate cancer stage; operational definition requires review. | — |
| `hormonse_sensitive_disease` | No | string | Provisional field for hormonse sensitive disease; operational definition requires review. | — |
| `mention_fever_as_symptom_temp_is_noted_in_signs` | No | string | Provisional field for Mention fever as symptom - temp is noted in signs; operational definition requires review. | — |
| `assessment_role` | No | string | Role in the clinical pathway: baseline, interim, end of treatment, or follow-up. | — |
| `ecog_score` | No | integer | Recorded ECOG performance status, with assessment date and source. | Minimum: <code>0</code>; Maximum: <code>5</code> |
| `prognostic_model_name` | No | string | Recorded prognostic assessment prognostic model name. No risk prediction is calculated by this schema. | — |
| `prognostic_model_version` | No | string | Recorded prognostic assessment prognostic model version. No risk prediction is calculated by this schema. | — |
| `prognostic_risk_category` | No | string | Recorded prognostic assessment prognostic risk category. No risk prediction is calculated by this schema. | — |
| `prognostic_context` | No | string | Recorded prognostic assessment prognostic context. No risk prediction is calculated by this schema. | — |
| `prognostic_score` | No | number | Score from the named, versioned prognostic method, when recorded. | — |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `cases` | Yes | array of object | Link to case records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `timepoints` | No | array of object | Link to timepoint records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic clinical_assessment records](../../extensions/lu177_psma/v0.3.0/examples/by_node/clinical_assessment.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
