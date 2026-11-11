# Changelog

Each release is archived on Zenodo with its own DOI; the concept DOI
[10.5281/zenodo.23417011](https://doi.org/10.5281/zenodo.23417011) always points to the latest one.

## v1.0.0 (11 November 2026)

First stable version. The file names of the outputs change, hence the new major version.

**Fewer files, clearer names**
- Only the scores keep a date: `data/ofaire_scores_<date>.csv`, one file per snapshot, to follow the
  catalogue over time.
- The other tables describe the latest snapshot only and lose their date: `data/ofaire_questions.csv`
  (it was the same file at every snapshot), `data/question_summary.csv`, `data/guideline_status.csv`
  and `data/actions.csv`. The dated copies of earlier snapshots are removed from the repository; they
  stay in the Git history and in the earlier releases.
- The profiling report also describes the latest snapshot only: notebook 03 removes the report of the
  previous run, so `reports/` holds one file, `eda_<date>.html`.

**Figures from the notebooks**
- Notebooks 03 and 05 save their figures as PDF in `earthportal_sa_audit/figures/` (six figures,
  replaced at each run). The slides read these files, so every figure shown comes from the same data as
  the tables.
- Notebook 03 has a new Figure 4: what the 478 points of O'FAIRe measure on EarthPortal. Notebook 05 has
  two new figures: the Mandatory properties most often empty, and the share of the guideline filled by
  each artefact.

**Other portals**
- The portal is now a setting: `PORTAL_NAME`, `PORTAL_API`, `PORTAL_UI`, `OFAIRE_API`,
  `OFAIRE_PORTAL` and `PORTAL_EXAMPLE` in `.env`, EarthPortal by default. The API key is now
  `PORTAL_APIKEY`; `EARTHPORTAL_APIKEY` still works.
- Notebook 03 reads the reachable maximum and the best artefact from the data instead of writing
  386 and OSO in the code.
- New [`ADAPTING.md`](ADAPTING.md): what to change and check to run the pipeline on another portal.

**Documentation**
- New [`ARCHITECTURE.md`](ARCHITECTURE.md) (how the pipeline is built) and this changelog.
- Report 6 in `docs/`: a proposal for a curation interface built on the JSON audits.
- READMEs updated; `docs/README.md` now lists every report.
- Slides of 13 November 2026 for the OntoPortal Federation & TIB meetings, in `docs/`.

**Results** on the snapshot of 10 November 2026.

## v0.3.0 (29 October 2026)

- Two-part audits: the FAIRness of each ontology (O'FAIRe) and its compliance with the Metadata
  Guidelines (status of the 99 properties: filled, empty or not applicable).
- Every empty property of the guideline becomes an action, with the new priority P5.
- One JSON file per ontology (`audits/json/<ACRONYM>.json`), from which its page is written.
- New table of the status of every property for every ontology; `note` column in the actions.
- Results on the snapshot of 16 October 2026.

## v0.2.0 (29 October 2026)

- New priorities: the Optional properties that cost O'FAIRe points come before the Recommended
  properties that cost nothing.
- Notebook 03: the score figures are split into separate plots; the profiling report and the
  duplicated artefacts are explained.
- Affiliations in `CITATION.cff` written as names.
- Results on the snapshot of 16 October 2026.

## v0.1.0 (16 October 2026)

First archived version: the five notebooks of `earthportal_sa_audit/`, Reports 1 to 5 and the slides
of 9 October 2026 in `docs/`, and `CITATION.cff`.
