# Version 0.4.0 artifact sources

These scripts build the proposed dictionary and documentation from the preserved v0.3.0 model and the source extracts under `extensions/lu177_psma/v0.4.0/sources/`. Python requires PyYAML, python-docx and jsonschema. Workbook authoring uses the supported `@oai/artifact-tool` package; graph rendering uses `@viz-js/viz` and `sharp`; the optional HTML interaction check uses `jsdom`.

Run from the repository root in this order:

1. `python scripts/v040/build_module.py`
2. `python scripts/v040/build_crosswalk.py`
3. `python scripts/v040/build_examples.py`
4. `python scripts/v040/build_views.py`
5. `python extensions/lu177_psma/v0.4.0/scripts/validate_model.py`
6. `node scripts/v040/render_graphs.mjs`
7. `python scripts/v040/build_html.py`
8. `node scripts/v040/build_workbooks.mjs`
9. `python scripts/v040/update_documents.py`
10. `python scripts/v040/package_documentation.py`
11. `python scripts/build_dictionary_docs.py`

The workbook and document scripts use `dist_work/` by default. Set `LU177_ARTIFACT_OUTPUT` consistently to use another directory. `LU177_DOCUMENT_SOURCES` can select another explicit manuscript input directory; otherwise the preserved author-supplied inputs are used. The document update preserves the existing manuscript structure and clinical references.

After a rebuild, render and inspect the Word files and every worksheet, rerun the validator and `python scripts/build_dictionary_docs.py --check`, and run `node scripts/v040/check_html.cjs` if jsdom is installed. DOM emulation does not establish browser or Gen3 deployment compatibility. Refresh the model's SHA256SUMS.txt only after final review. Then `python scripts/build_release_assets.py --output dist` creates a reproducible release ZIP and standalone assets. Existing release tags and downloads must not be overwritten.

The committed audit files describe checks actually performed for this release. Rebuilding documentation invalidates its previous visual-review evidence; record new evidence before publication.
