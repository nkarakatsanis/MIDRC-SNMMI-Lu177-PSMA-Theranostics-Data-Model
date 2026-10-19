# Repository guide — release 0.3.1

**tentative authors list**

Nicolas A Karakatsanis, Atlas Haddadi Avval, Julia Brosch-Lenz, Irene Buvat, Abhinav Jha, Mario Jreige, Quanzheng Li, Neeta Pandit-Taskar, Babak Saboury, Jazmin Schwartz, Tahir I Yusufaly, Tyler J Bradshaw

## Source layout

| Path | Role |
| --- | --- |
| `gdcdictionary/`, `pyproject.toml` and original license files | Imported MIDRC source, retained at parent `bee947238381704486ccd12beeb8f4689fb22843`. |
| `extensions/lu177_psma/v0.3.0/` | Complete v0.3.0 theranostics working model, dictionary, templates, graphs and examples. |
| `docs/DATA_MODEL.md`, `docs/DOMAINS.md`, `docs/NODE_CATALOG.md` | Human-readable GitHub documentation. |
| `docs/dictionary/` | Generated field-by-field reference for all 67 nodes, including required links and alternative groups. |
| `docs/upstream/README.before-lu177-psma-v0.3.0.md` | Previous README preserved exactly. |
| `VERSION` and `release.json` | Repository release identity: **0.3.1**; underlying model revision remains **0.3.0-proposal**. |
| `releases/0.3.1.md` and `releases/0.3.0.md` | Current patch notes and corrected initial-release notes. |
| `scripts/build_release_assets.py` | Builds downloadable artifacts from committed files. |
| `scripts/build_dictionary_docs.py` | Rebuilds the field-level reference; `--check` detects documentation drift. |

## Baseline compatibility

The repository's imported source and the deployed compiled dictionary have different revisions. The proposal is based on deployed dictionary `1.4.3-2-g7505333`, commit `7505333d56c87a289463a814131e38d0f2be6674`. Its snapshot, hash and additive patch are in the versioned model folder.

The imported source includes a custom `pt_series_file.mr_images` boolean. It remains intact in `gdcdictionary/schemas/pt_series_file.yaml`. A receiving Gen3 implementation must reconcile that field and other source differences before applying this proposal to the source tree. This upload does not claim source-level interchangeability between these different baselines.

## Release automation

The release workflow is scoped to this repository's `cdis` branch. A committed change to `VERSION`, or a manual run, validates the model, verifies package checksums, builds the model archive and publishes the matching version as a GitHub development release. The title is exactly the numeric `VERSION`; the tag uses a `v` prefix. Existing tags and release assets are never overwritten by the workflow. This documentation patch also updates the v0.3.0 release description from its corrected notes file; it does not move that tag or replace its downloads.

The initial release title is **0.3.0**, using **v0.3.0**. Inherited MIDRC tags have since been removed from this repository. The current documentation-only patch is release **0.3.1**, using **v0.3.1**. It packages the unchanged v0.3.0 model and keeps the standalone Word and HTML filenames at v0.3.0 so their document identity remains accurate. The internal `0.3.0-proposal` working-artifact label is retained to distinguish review status from repository release identity.

The inherited build-and-deploy job is restricted to its original MIDRC source repositories. It is not used to deploy this personal model repository. The new workflow publishes release files only; it does not migrate a database or update MIDRC services.

## Development and integration

Use the root README's local validation command. Review the node delta, seven proposed enum additions, source crosswalks and open review register with the receiving Gen3 developers. Reconcile the target baseline, compile the receiving dictionary, validate synthetic submissions and then evaluate real-data mappings. NucLex, LOINC and RadLex bindings require independent semantic review.

Keep release notes and version identifiers explicit. A later adoption into the active MIDRC dictionary is a separate integration change; changes to ontology definitions do not automatically change patient record relationships.
