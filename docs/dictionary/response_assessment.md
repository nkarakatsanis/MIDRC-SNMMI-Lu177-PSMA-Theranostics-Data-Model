# Response Assessment (`response_assessment`)

Release **0.3.2** · [Dictionary index](README.md) · [Node catalog](../NODE_CATALOG.md)

Criteria-specific biochemical, imaging or clinical response assessment with baseline and follow-up evidence.

| Attribute | Value |
| --- | --- |
| Record grain | One criteria set and assessment time |
| Category | `clinical` |
| Navigation group | Outcomes |
| MIDRC relationship | `new_theranostics_node` |
| Submittable | <code>true</code> |
| Additional properties permitted | <code>false</code> |
| Unique keys | <code>[["id"], ["project_id", "submitter_id"]]</code> |

[JSON schema](../../extensions/lu177_psma/v0.3.0/schemas/response_assessment.json) · [YAML schema](../../extensions/lu177_psma/v0.3.0/integration/yaml/response_assessment.yaml) · [Submission template](../../extensions/lu177_psma/v0.3.0/templates/submission_response_assessment_template.json)

## Relationships

Links point from this node to referenced records. Multiplicity is the schema’s child-to-parent relationship; a back-reference names traversal in the reverse direction. Requirements below combine the link declaration and the node required-property list.

| Link property | Target | Multiplicity | Required | Back-reference | Label |
| --- | --- | --- | --- | --- | --- |
| `therapy_courses` | [therapy_course](therapy_course.md) | `many_to_one` | Yes | `nmmi_response_assessment_therapy_courses` | `related_to` |
| `baseline_imaging_studies` | [imaging_study](imaging_study.md) | `many_to_many` | No | `nmmi_response_assessment_baseline_imaging_studies` | `supported_by` |
| `followup_imaging_studies` | [imaging_study](imaging_study.md) | `many_to_many` | No | `nmmi_response_assessment_followup_imaging_studies` | `supported_by` |
| `dose_summaries` | [dose_summary](dose_summary.md) | `many_to_many` | No | `nmmi_response_assessment_dose_summaries` | `supported_by` |
| `timepoints` | [timepoint](timepoint.md) | `many_to_one` | No | `nmmi_response_assessment_timepoints` | `related_to` |
| `provenance_records` | [provenance](provenance.md) | `many_to_many` | No | `nmmi_response_assessment_provenance_records` | `documented_by` |
| `baseline_burdens` | [disease_burden](disease_burden.md) | `many_to_one` | No | `nmmi_response_assessment_baseline_burdens` | `supported_by` |
| `followup_burdens` | [disease_burden](disease_burden.md) | `many_to_one` | No | `nmmi_response_assessment_followup_burdens` | `supported_by` |
| `anatomic_targets` | [anatomic_target](anatomic_target.md) | `many_to_many` | No | `nmmi_response_assessment_anatomic_targets` | `supported_by` |
| `absorbed_doses` | [absorbed_dose](absorbed_dose.md) | `many_to_many` | No | `nmmi_response_assessment_absorbed_doses` | `supported_by` |
| `baseline_pros` | [patient_reported_outcome](patient_reported_outcome.md) | `many_to_many` | No | `nmmi_response_assessment_baseline_pros` | `supported_by` |
| `followup_pros` | [patient_reported_outcome](patient_reported_outcome.md) | `many_to_many` | No | `nmmi_response_assessment_followup_pros` | `supported_by` |
| `confirmation_pros` | [patient_reported_outcome](patient_reported_outcome.md) | `many_to_many` | No | `nmmi_response_assessment_confirmation_pros` | `supported_by` |
| `clinical_assessments` | [clinical_assessment](clinical_assessment.md) | `many_to_many` | No | `nmmi_response_assessment_clinical_assessments` | `supported_by` |
| `biomarker_assessments` | [biomarker_assessment](biomarker_assessment.md) | `many_to_many` | No | `nmmi_response_assessment_biomarker_assessments` | `supported_by` |
| `clinical_events` | [clinical_event](clinical_event.md) | `many_to_many` | No | `nmmi_response_assessment_clinical_events` | `supported_by` |
| `laboratory_measurements` | [measurement](measurement.md) | `many_to_many` | No | `nmmi_response_assessment_laboratory_measurements` | `related_to` |
| `roi_measurements` | [measurement](measurement.md) | `many_to_many` | No | `nmmi_response_assessment_roi_measurements` | `related_to` |
| `baseline_psa_results` | [measurement](measurement.md) | `many_to_one` | No | `nmmi_response_assessment_baseline_psa_results` | `related_to` |
| `nadir_psa_results` | [measurement](measurement.md) | `many_to_one` | No | `nmmi_response_assessment_nadir_psa_results` | `related_to` |
| `confirmatory_psa_results` | [measurement](measurement.md) | `many_to_one` | No | `nmmi_response_assessment_confirmatory_psa_results` | `related_to` |

## Properties

“Required” reflects the node’s `required` list. Alternative-link groups above can impose an additional requirement. System-managed properties are identified separately. Units are preserved in the supplied definitions; no units or code bindings are inferred. An optional field does not automatically permit a null value.

The JSON schema is authoritative, including nested object constraints. The tables expose every top-level property and its declared values, constraints and source terminology. Inherited terminology metadata is reproduced as supplied; inclusion is not a new mapping approval.

### Data and identification properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `type` | Yes | string (enumerated) | No description supplied in the schema. | Allowed values: <code>"response_assessment"</code> |
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
| `criteria_name` | Yes | string | Response criteria name. | — |
| `criteria_version` | No | string | Response criteria version. | — |
| `assessment_scope` | No | string | Response assessment scope. | — |
| `baseline_definition` | No | string | Response baseline definition. | — |
| `result_category` | No | string | Response result category. | — |
| `baseline_date` | No | string | Baseline assessment date. | Format: <code>"date"</code> |
| `confirmation_date` | No | string | Confirmation assessment date, if required by criteria. | Format: <code>"date"</code> |
| `clinical_progression_date` | No | string | Date when clinical progression (e.g., worsening symptoms, need for new therapy) was documented. | Format: <code>"date"</code> |
| `date_of_best_psa_response` | No | string | Date when the best PSA response was documented. | Format: <code>"date"</code> |
| `date_of_radiographic_progression` | No | string | Date when radiographic progression was first documented. | Format: <code>"date"</code> |
| `date_of_radiographic_response_assessment` | No | string | Date when the overall radiographic response was assessed. | Format: <code>"date"</code> |
| `radiographic_response_assessment` | No | string | Response (image-based) | — |
| `imaging_response_assessment_criteria` | No | string | Provisional field for Imaging_Response_Assessment_Criteria; operational definition requires review. | — |
| `psa_baseline_definition` | No | string | Specifies the timepoint convention used to define the baseline PSA value. Required to ensure reproducibility of PCWG3-based PSA response and progression calculations across institutions. | — |
| `psa_baseline_date` | No | string | Date on which the baseline PSA sample was collected, as defined by PSA_Baseline_Definition. | Format: <code>"date"</code> |
| `psa_response_category` | No | string | Categorical PSA response based on predefined criteria (e.g., PCWG3: &gt;=50% decline). | — |
| `psa_progression_confirmation` | No | string | PSA Progression (Yes/No) confirmed &gt; 3 weeks later | — |
| `radiographic_response_criteria` | No | string | Criteria used for assessing radiographic response. | — |
| `radiographic_response_overall` | No | string | Overall radiographic response assessment. | — |
| `psa_nadir_date` | No | string | Date on which the PSA nadir was recorded. | Format: <code>"date"</code> |
| `psa_response_50_confirmed` | No | boolean | Indicates whether a confirmed ≥50% decline in PSA from baseline was achieved at any point during therapy. Confirmation requires a second value at least 3 weeks later. Per PCWG3. | — |
| `psa_response_50_date` | No | string | Date on which the ≥50% PSA decline from baseline was first documented (not the confirmation date). | Format: <code>"date"</code> |
| `psa_best_response_percent` | No | number | Minimum signed 100 × (PSA at assessment − baseline PSA) / baseline PSA over the declared window when best response means greatest decline. Negative is decline. Specify selection rule; omit if baseline is zero. | — |
| `psa_early_rise_pre12w` | No | boolean | Whether an early PSA rise was observed; this does not classify it as flare or exclude true progression. | — |
| `psa_progression_pcwg3_documented` | No | boolean | Indicates whether PSA progression per PCWG3 criteria has been documented: ≥25% increase AND ≥2 ng/mL above nadir (after prior decline), or ≥25% AND ≥2 ng/mL above baseline (no prior decline beyond 12 weeks), confirmed ≥3 weeks later. | — |
| `psa_progression_pcwg3_date` | No | string | Date of first PSA value meeting PCWG3 progression criteria (not the confirmation date). Per PCWG3, this date does not necessarily indicate clinical need to discontinue therapy. | Format: <code>"date"</code> |
| `psa_progression_pcwg3_confirmed_date` | No | string | Date of the confirmatory PSA value (≥3 weeks after PSA_Progression_PCWG3_Date) establishing definitive PCWG3 PSA progression. | Format: <code>"date"</code> |
| `psa_progression_criteria_used` | No | string | Specifies the PSA progression criteria applied, to enable harmonization across datasets with different conventions. | — |
| `imaging_response_criteria_used` | No | string | Specifies the imaging response/progression criteria applied for this patient or study. | — |
| `imaging_overall_response` | No | string | Overall radiographic response assessment across all sites at best response timepoint. | — |
| `imaging_overall_response_date` | No | string | Date on which the overall radiographic response assessment was performed. | Format: <code>"date"</code> |
| `imaging_progression_type` | No | string | Characterizes the nature of radiographic progression per PCWG3, distinguishing growth of pre-existing lesions from development of new lesions, as these carry distinct prognostic and biological implications. | — |
| `imaging_progression_site` | No | array of string | Anatomical site(s) at which radiographic progression was first documented, recorded separately per site per PCWG3. | — |
| `imaging_progression_date` | No | string | Date of first documented radiographic progression at any site (earliest site-specific progression date). | Format: <code>"date"</code> |
| `soft_tissue_response_recist` | No | string | Best overall response in measurable soft tissue disease (nodal and/or visceral) per RECIST 1.1, recorded separately from bone disease per PCWG3. | — |
| `nodal_progression_pcwg3` | No | boolean | Indicates whether nodal progression per PCWG3 criteria has been documented. Previously normal nodes (&lt;1.0 cm) must have grown ≥5 mm in short axis AND be ≥1.0 cm in short axis. For existing pathologic nodes (≥1.5 cm), progression defined per RECIST 1.1. | — |
| `nodal_progression_date` | No | string | Date on which nodal progression per PCWG3 criteria was first documented. | Format: <code>"date"</code> |
| `nodal_progression_location` | No | string | Location of progressive nodal disease, recorded separately per PCWG3 as locoregional versus metastatic. | — |
| `visceral_progression_pcwg3` | No | boolean | Indicates whether visceral progression per PCWG3/RECIST 1.1 criteria has been documented. Measurable visceral lesions ≥1.0 cm in longest dimension. Recorded separately by organ site. | — |
| `visceral_progression_date` | No | string | Date on which visceral progression was first documented. | Format: <code>"date"</code> |
| `visceral_progression_site` | No | array of string | Organ site(s) of visceral progression, recorded separately per PCWG3. | — |
| `bone_progression_pcwg3` | No | boolean | Indicates whether bone progression per PCWG3 2+2 rule has been documented: ≥2 new lesions on first post-treatment scan, confirmed by ≥2 additional new lesions on the next scan. Date of progression = date of first post-treatment scan showing initial 2 new lesions. | — |
| `bone_progression_date` | No | string | Date of the first post-treatment scan on which ≥2 new bone lesions were initially documented per PCWG3 2+2 rule. This is the recorded date of progression even if confirmation occurs on a subsequent scan. | Format: <code>"date"</code> |
| `bone_progression_confirmed_date` | No | string | Date of the confirmatory scan on which ≥2 additional new bone lesions were documented, fulfilling the PCWG3 2+2 rule. | Format: <code>"date"</code> |
| `bone_scan_flare` | No | boolean | Indicates whether a bone scan flare was identified on the first post-treatment scan (new lesions on first follow-up scan not confirmed on subsequent scan) per PCWG3. Flare should not be recorded as progression. | — |
| `bone_progression_criteria_used` | No | string | Specifies the bone progression criteria applied. In ¹⁷⁷Lu-PSMA studies, PSMA-PET/CT or post-therapy SPECT/CT may serve as primary bone imaging modality rather than conventional 99mTc bone scintigraphy. | — |
| `mixed_response` | No | boolean | Indicates whether a mixed response was observed: simultaneous favorable change in one site and unfavorable change in another. Per PCWG3, the disease should be assessed as a whole rather than on the basis of index lesions alone. | — |
| `mixed_response_sites` | No | string | Description of sites showing divergent responses in cases of mixed response, specifying which site(s) responded and which progressed. | — |
| `overall_treatment_response_category` | No | string | Composite overall response integrating PSA response, radiographic response, and clinical status. Captures patients with discordant PSA/imaging responses, which are common in ¹⁷⁷Lu-PSMA RPT. | — |
| `psa_imaging_concordance` | No | string | Indicates concordance or discordance between PSA progression and radiographic progression at time of treatment discontinuation. Discordance (e.g., PSA rise with stable imaging) is clinically relevant in ¹⁷⁷Lu-PSMA RPT. | — |
| `recip_response` | No | string | Original response label from the source (CMR/PMR/SMD/PMD/NE); pair with criteria_name/version and canonical recip_category. Do not treat SUV change alone as RECIP response. | — |
| `recip_response_date` | No | string | Date of the PSMA-PET scan used for RECIP 1.0 response assessment. | Format: <code>"date"</code> |
| `psma_pet_response_date` | No | string | Date of response under the explicitly named PET criteria. Uptake change alone does not establish RECIP response. | Format: <code>"date"</code> |
| `psma_pet_progression_date` | No | string | Date of PET progression under the named criteria. RECIP-PD requires both the specified whole-body volume increase and new lesions; do not apply an OR rule. | Format: <code>"date"</code> |
| `psma_expression_change_percent` | No | number | Percentage change in a prespecified PSMA PET uptake metric (for example SUVmax or SUVmean) for a defined lesion or lesion summary. Metric, lesion-selection rule, acquisition, and reconstruction method must be recorded. | — |
| `new_psma_avid_lesions_posttreatment` | No | integer | Number of new PSMA-avid lesions identified on post-treatment PSMA-PET scan compared to baseline, regardless of anatomical site. | Minimum: <code>0</code> |
| `alp_response_normalization` | No | string | Normalization to the institution-specific reference range, with applicability and laboratory evidence. | Allowed values: <code>"yes"</code>, <code>"no"</code>, <code>"not_applicable"</code> |
| `alp_response_date` | No | string | Date on which ALP normalization was first documented. | Format: <code>"date"</code> |
| `alp_best_response_percent` | No | number | Minimum signed 100 × (ALP at assessment − baseline ALP) / baseline ALP over the declared window when best response means greatest decline. Negative is decline. Specify selection rule; omit if baseline is zero. | — |
| `ldh_response_normalization` | No | string | Normalization to the institution-specific reference range, with applicability and laboratory evidence. | Allowed values: <code>"yes"</code>, <code>"no"</code>, <code>"not_applicable"</code> |
| `ldh_best_response_percent` | No | number | Minimum signed 100 × (LDH at assessment − baseline LDH) / baseline LDH over the declared window when best response means greatest decline. Negative is decline. Specify selection rule; omit if baseline is zero. | — |
| `hemoglobin_nadir_value` | No | number | Lowest hemoglobin value recorded during ¹⁷⁷Lu-PSMA RPT. Associated with hematologic toxicity and independently prognostic for OS in mCRPC. | Minimum: <code>0</code> |
| `hemoglobin_nadir_date` | No | string | Date on which the hemoglobin nadir was recorded. | Format: <code>"date"</code> |
| `ctc_conversion_favorable` | No | string | Recorded assay-specific CTC conversion with baseline/follow-up evidence; not assessed is distinct from no. | Allowed values: <code>"yes"</code>, <code>"no"</code>, <code>"not_assessed"</code> |
| `testosterone_response` | No | string | Serum testosterone level at end of treatment or last follow-up, relative to castrate threshold (≤50 ng/dL). Relevant for assessing adequacy of castration during therapy. | — |
| `fdg_pet_positivity` | No | string | Provisional field for FDG PET positivity; operational definition requires review. | — |
| `invovled_organ_systems` | No | string | Provisional field for invovled organ systems; operational definition requires review. | — |
| `mri_pirads` | No | string | Provisional field for MRI; PIRADS; operational definition requires review. | — |
| `bone_scan` | No | string | Provisional field for BOne scan; operational definition requires review. | — |
| `oligometastasis` | No | string | Provisional field for Oligometastasis; operational definition requires review. | — |
| `widespread_metastasis` | No | string | Provisional field for widespread metastasis; operational definition requires review. | — |
| `superscan` | No | string | very extensive diseases with specific appearance on bone scan | — |
| `criteria_reference` | No | string | Assessment criteria reference. | — |
| `criteria_release` | No | string | Assessment criteria release. | — |
| `criteria_rule_text` | No | string | Assessment criteria rule text. | — |
| `criteria_rule_status` | No | string | Assessment criteria rule status. | — |
| `new_lesion_compartment` | No | string | Assessment new lesion compartment. | — |
| `psa_rise_retrospective_interpretation` | No | string | Assessment psa rise retrospective interpretation. | — |
| `composite_algorithm_name` | No | string | Assessment composite algorithm name. | — |
| `composite_algorithm_version` | No | string | Assessment composite algorithm version. | — |
| `psa_best_response_selection_rule` | No | string | Assessment psa best response selection rule. | — |
| `confirmation_status` | No | string | Confirmation status under the selected criteria. | Allowed values: <code>"not_required"</code>, <code>"pending"</code>, <code>"confirmed"</code>, <code>"not_confirmed"</code>, <code>"not_assessable"</code> |
| `psma_pet_pcwg4_progression_documented` | No | boolean | Recorded result under a specified PCWG4 release, compartment and confirmation rule; no automatic fixed new-lesion threshold is encoded. | — |
| `imaging_progression_modality` | No | string | Actual modality used for progression assessment; criteria are recorded separately. | — |
| `recip_category` | No | string | Canonical RECIP response category. Source CMR/PMR/SMD/PMD labels are retained separately and require explicit mapping. | Allowed values: <code>"RECIP-CR"</code>, <code>"RECIP-PR"</code>, <code>"RECIP-SD"</code>, <code>"RECIP-PD"</code>, <code>"NE"</code> |
| `ptlv_change_percent` | No | number | 100 × (follow-up whole-body volume − baseline volume) / baseline volume; undefined when baseline is zero. | — |
| `psa_followup_value` | No | number | PSA value at the current assessment; authoritative result is linked. | Minimum: <code>0</code> |
| `psa_change_percent` | No | number | 100 × (follow-up PSA − baseline PSA) / baseline PSA; undefined when baseline is zero. | — |
| `psa_subsequent_decline_documented` | No | boolean | Subsequent decline after an early rise, supported by later PSA measurements. | — |
| `retrospective_interpretation_date` | No | string | Date retrospective interpretation was recorded, avoiding future-information leakage into earlier assessments. | Format: <code>"date"</code> |
| `sse_occurred` | No | boolean | Whether an SSE occurred by the stated follow-up cutoff; actual events are linked separately. | — |
| `pain_response` | No | string | Criteria-specific pain response, including explicit not-evaluable status. | Allowed values: <code>"yes"</code>, <code>"no"</code>, <code>"not_evaluable"</code> |
| `pain_response_date` | No | string | Date on which the pain response criterion was first met. | Format: <code>"date"</code> |

### Relationship properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `therapy_courses` | Yes | array of object | Link to therapy_course records by submitter_id or UUID. | Minimum items: <code>1</code>; Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `baseline_imaging_studies` | No | array of object | Link to imaging_study records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `followup_imaging_studies` | No | array of object | Link to imaging_study records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `dose_summaries` | No | array of object | Link to dose_summary records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `timepoints` | No | array of object | Link to timepoint records by submitter_id or UUID. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `provenance_records` | No | array of object | Link to provenance records by submitter_id or UUID. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `baseline_burdens` | No | array of object | References to disease_burden records. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `followup_burdens` | No | array of object | References to disease_burden records. | Maximum items: <code>1</code>; Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `anatomic_targets` | No | array of object | References to anatomic_target records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `absorbed_doses` | No | array of object | References to absorbed_dose records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `baseline_pros` | No | array of object | References to patient_reported_outcome records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `followup_pros` | No | array of object | References to patient_reported_outcome records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `confirmation_pros` | No | array of object | References to patient_reported_outcome records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `clinical_assessments` | No | array of object | References to clinical_assessment records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `biomarker_assessments` | No | array of object | References to biomarker_assessment records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `clinical_events` | No | array of object | References to clinical_event records. | Unique items: <code>true</code>; Each item: (Exactly one alternative: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>]) |
| `laboratory_measurements` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `roi_measurements` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `baseline_psa_results` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `nadir_psa_results` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |
| `confirmatory_psa_results` | No | one or more of: object; array of object | No description supplied in the schema. | One or more alternatives: [1. object: One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>] / 2. array of object: Minimum items: <code>1</code>; Maximum items: <code>1</code>; Each item: (One or more alternatives: [1. Not explicitly typed; see schema constraints: required keys: <code>"submitter_id"</code> / 2. Not explicitly typed; see schema constraints: required keys: <code>"id"</code>])] |

### System-managed properties

| Property | Required | Type | Definition | Allowed values and constraints |
| --- | --- | --- | --- | --- |
| `id` | No | string | A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general. | Pattern: <code>"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"</code>; System alias: <code>"node_id"</code>; Source term: NCIt; C54100; Universally Unique Identifier |
| `project_id` | No | string | Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement. | — |
| `state` | No | exactly one of: string (enumerated); string (enumerated) | The current state of the object. | Default: <code>"validated"</code>; Exactly one alternative: [1. string (enumerated): Allowed values: <code>"uploading"</code>, <code>"uploaded"</code>, <code>"md5summing"</code>, <code>"md5summed"</code>, <code>"validating"</code>, <code>"error"</code>, <code>"invalid"</code>, <code>"suppressed"</code>, <code>"redacted"</code>, <code>"live"</code> / 2. string (enumerated): Allowed values: <code>"validated"</code>, <code>"submitted"</code>, <code>"released"</code>] |
| `created_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |
| `updated_datetime` | No | exactly one of: string; null | A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z&#124;(+&#124;-)hh:mm] | Exactly one alternative: [1. string: Format: <code>"date-time"</code> / 2. null] |

## Synthetic examples

[Read the synthetic response_assessment records](../../extensions/lu177_psma/v0.3.0/examples/by_node/response_assessment.json). These are structural demonstrations, not patient data or treatment recommendations.

Generated from the committed node schema by `scripts/build_dictionary_docs.py`. Do not edit this generated page directly.
