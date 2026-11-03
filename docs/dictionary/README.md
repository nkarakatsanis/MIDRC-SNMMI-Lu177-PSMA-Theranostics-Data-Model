# Human-readable data dictionary — 0.4.0

**90 node types · 3,212 node/property entries · 412 relationships.** Shared properties are counted once per node, not as distinct clinical concepts.

[Architecture and use cases](../DATA_MODEL.md) · [Domain index](../DOMAINS.md) · [Repository guide](../REPOSITORY_GUIDE.md)

Each page follows the MIDRC dictionary structure: node identity and category, record grain, links and back-references, multiplicity and required link groups, then property definitions, types, allowed values and constraints. The source JSON schemas remain authoritative.

The dictionary describes the complete 0.4.0 proposal under `extensions/lu177_psma/v0.4.0/`. The inherited `gdcdictionary/` source is a separate preserved baseline. This documentation does not indicate a deployed MIDRC release or completed clinical/terminology review.

| Node | Group | MIDRC relationship | Properties | Links |
| --- | --- | --- | ---: | ---: |
| [absorbed_dose](absorbed_dose.md) | Quantification | `new_theranostics_node` | 27 | 4 |
| [acquisition](acquisition.md) | Imaging | `new_theranostics_node` | 92 | 9 |
| [administration](administration.md) | Treatment | `new_theranostics_node` | 41 | 8 |
| [anatomic_target](anatomic_target.md) | Quantification | `new_theranostics_node` | 18 | 2 |
| [annotation](annotation.md) | Imaging | `preserved_and_extended` | 61 | 22 |
| [annotation_file](annotation_file.md) | Imaging | `preserved_and_extended` | 50 | 15 |
| [biological_target](biological_target.md) | Radiopharmaceutical reference | `new_extension` | 20 | 2 |
| [biomarker_assessment](biomarker_assessment.md) | Clinical | `new_theranostics_node` | 46 | 4 |
| [case](case.md) | Subject | `preserved_and_extended` | 53 | 3 |
| [clinical_assessment](clinical_assessment.md) | Clinical | `new_theranostics_node` | 113 | 3 |
| [clinical_event](clinical_event.md) | Outcomes | `new_theranostics_node` | 30 | 5 |
| [computational_model](computational_model.md) | Digital twin research | `new_extension` | 29 | 3 |
| [condition](condition.md) | Clinical | `preserved_and_extended` | 57 | 3 |
| [core_metadata_collection](core_metadata_collection.md) | Governance | `preserved` | 23 | 1 |
| [cr_series_file](cr_series_file.md) | Imaging | `preserved` | 37 | 2 |
| [ct_series_file](ct_series_file.md) | Imaging | `preserved_and_extended` | 67 | 3 |
| [data_release](data_release.md) | Governance | `preserved` | 10 | 1 |
| [dataset](dataset.md) | Governance | `preserved_and_extended` | 29 | 1 |
| [decay_emission](decay_emission.md) | Radiopharmaceutical reference | `new_extension` | 26 | 4 |
| [dicom_annotation_file](dicom_annotation_file.md) | Imaging | `preserved_and_extended` | 41 | 3 |
| [disease_burden](disease_burden.md) | Quantification | `new_theranostics_node` | 32 | 5 |
| [dispense_event](dispense_event.md) | Radiopharmaceutical supply | `new_extension` | 22 | 5 |
| [dose_summary](dose_summary.md) | Quantification | `new_theranostics_node` | 23 | 4 |
| [dosimetry](dosimetry.md) | Quantification | `new_theranostics_node` | 45 | 12 |
| [dx_series_file](dx_series_file.md) | Imaging | `preserved` | 37 | 2 |
| [eligibility_assessment](eligibility_assessment.md) | Clinical | `new_theranostics_node` | 33 | 10 |
| [external_identifier](external_identifier.md) | Semantics and governance | `new_extension` | 33 | 10 |
| [imaging_study](imaging_study.md) | Imaging | `preserved_and_extended` | 42 | 6 |
| [laboratory_panel](laboratory_panel.md) | Clinical | `new_theranostics_node` | 27 | 4 |
| [material_lot](material_lot.md) | Radiopharmaceutical manufacture | `new_extension` | 23 | 4 |
| [measurement](measurement.md) | Clinical | `preserved_and_extended` | 55 | 8 |
| [medical_history](medical_history.md) | Clinical | `new_theranostics_node` | 41 | 2 |
| [medication](medication.md) | Clinical | `preserved_and_extended` | 49 | 2 |
| [medicinal_product](medicinal_product.md) | Radiopharmaceutical product | `new_extension` | 28 | 3 |
| [mg_series_file](mg_series_file.md) | Imaging | `preserved` | 40 | 2 |
| [model_parameter](model_parameter.md) | Digital twin research | `new_extension` | 27 | 5 |
| [model_prediction](model_prediction.md) | Digital twin research | `new_extension` | 26 | 4 |
| [model_release](model_release.md) | Governance | `new_theranostics_node` | 17 | 1 |
| [model_run](model_run.md) | Digital twin research | `new_extension` | 31 | 11 |
| [molecular_entity](molecular_entity.md) | Radiopharmaceutical reference | `new_extension` | 27 | 2 |
| [mr_series_file](mr_series_file.md) | Imaging | `preserved_and_extended` | 80 | 3 |
| [nm_series_file](nm_series_file.md) | Imaging | `preserved_and_extended` | 64 | 3 |
| [observation](observation.md) | Clinical | `preserved_and_extended` | 27 | 3 |
| [organ_function](organ_function.md) | Clinical | `new_theranostics_node` | 25 | 5 |
| [package_component](package_component.md) | Radiopharmaceutical product | `new_extension` | 18 | 4 |
| [patient_reported_outcome](patient_reported_outcome.md) | Outcomes | `new_theranostics_node` | 44 | 4 |
| [preparation_event](preparation_event.md) | Radiopharmaceutical manufacture | `new_extension` | 30 | 5 |
| [procedure](procedure.md) | Clinical | `preserved_and_extended` | 37 | 5 |
| [product_ingredient](product_ingredient.md) | Radiopharmaceutical product | `new_extension` | 22 | 4 |
| [product_package](product_package.md) | Radiopharmaceutical product | `new_extension` | 34 | 3 |
| [program](program.md) | Governance | `preserved` | 4 | 0 |
| [project](project.md) | Governance | `preserved` | 32 | 1 |
| [provenance](provenance.md) | Governance | `new_theranostics_node` | 31 | 1 |
| [pt_series_file](pt_series_file.md) | Imaging | `preserved_and_extended` | 64 | 3 |
| [radiology_report](radiology_report.md) | Clinical | `preserved` | 58 | 4 |
| [radionuclide](radionuclide.md) | Radiopharmaceutical reference | `new_extension` | 26 | 2 |
| [radiopharmaceutical](radiopharmaceutical.md) | Radiopharmaceutical reference | `new_theranostics_node` | 37 | 9 |
| [radiopharmaceutical_batch](radiopharmaceutical_batch.md) | Radiopharmaceutical manufacture | `new_theranostics_node` | 28 | 4 |
| [radiopharmaceutical_order](radiopharmaceutical_order.md) | Radiopharmaceutical supply | `new_extension` | 28 | 7 |
| [radiopharmaceutical_test](radiopharmaceutical_test.md) | Radiopharmaceutical evidence | `new_extension` | 54 | 7 |
| [radiopharmaceutical_unit](radiopharmaceutical_unit.md) | Radiopharmaceutical supply | `new_extension` | 28 | 5 |
| [reconstruction](reconstruction.md) | Imaging | `new_theranostics_node` | 45 | 7 |
| [reference_evidence](reference_evidence.md) | Research evidence | `new_extension` | 41 | 5 |
| [registration](registration.md) | Imaging | `new_theranostics_node` | 25 | 9 |
| [regulatory_authorization](regulatory_authorization.md) | Radiopharmaceutical product | `new_extension` | 32 | 4 |
| [response_assessment](response_assessment.md) | Outcomes | `new_theranostics_node` | 132 | 21 |
| [rf_series_file](rf_series_file.md) | Imaging | `preserved` | 37 | 2 |
| [root](root.md) | Governance | `preserved` | 3 | 0 |
| [scanner](scanner.md) | Imaging | `new_theranostics_node` | 23 | 3 |
| [scanner_qa](scanner_qa.md) | Imaging | `new_theranostics_node` | 24 | 2 |
| [semantic_mapping](semantic_mapping.md) | Governance | `new_theranostics_node` | 25 | 1 |
| [site](site.md) | Governance | `new_theranostics_node` | 15 | 1 |
| [specimen](specimen.md) | Clinical | `new_theranostics_node` | 18 | 2 |
| [study](study.md) | Longitudinal context | `new_theranostics_node` | 18 | 1 |
| [supplementary_file](supplementary_file.md) | Governance | `preserved_and_extended` | 34 | 4 |
| [supply_offer](supply_offer.md) | Radiopharmaceutical supply | `new_extension` | 28 | 3 |
| [survival_outcome](survival_outcome.md) | Outcomes | `new_theranostics_node` | 36 | 5 |
| [theranostic_pair](theranostic_pair.md) | Radiopharmaceutical reference | `new_extension` | 21 | 5 |
| [therapy_course](therapy_course.md) | Longitudinal context | `new_theranostics_node` | 25 | 3 |
| [therapy_cycle](therapy_cycle.md) | Longitudinal context | `new_theranostics_node` | 21 | 2 |
| [time_activity_curve](time_activity_curve.md) | Quantification | `new_theranostics_node` | 23 | 4 |
| [timepoint](timepoint.md) | Longitudinal context | `new_theranostics_node` | 25 | 4 |
| [toxicity_event](toxicity_event.md) | Outcomes | `new_theranostics_node` | 35 | 6 |
| [toxicity_summary](toxicity_summary.md) | Outcomes | `new_theranostics_node` | 26 | 3 |
| [treatment_decision](treatment_decision.md) | Treatment | `new_theranostics_node` | 40 | 12 |
| [treatment_plan](treatment_plan.md) | Treatment | `new_theranostics_node` | 31 | 10 |
| [treatment_transition](treatment_transition.md) | Longitudinal context | `new_theranostics_node` | 32 | 5 |
| [us_series_file](us_series_file.md) | Imaging | `preserved` | 32 | 2 |
| [visit](visit.md) | Longitudinal context | `preserved_and_extended` | 27 | 2 |
| [xa_series_file](xa_series_file.md) | Imaging | `preserved` | 39 | 2 |

Regenerate with `python scripts/build_dictionary_docs.py`; use `--check` to verify that the pages match the schemas.
