# Running the pipeline on another OntoPortal portal

The pipeline was built and tested on EarthPortal only. Other portals of the OntoPortal Federation
(AgroPortal, BioPortal, EcoPortal, ...) share the same software and the same Metadata Guidelines, so
most of it should work as it is. This page lists what to change, and what to check, before you
trust the results. It is short on purpose: please tell us what you had to change, so that we can
add it here.

## 1. Change: the portal settings in `.env`

Write these lines in your `.env` (see `.env.example`). Without them, the pipeline audits EarthPortal.

| Variable | What it is | EarthPortal value |
|---|---|---|
| `PORTAL_APIKEY` | your API key on that portal (your account page) | |
| `PORTAL_NAME` | the name shown in the audits | `EarthPortal` |
| `PORTAL_API` | the REST API | `https://data.earthportal.eu` |
| `PORTAL_UI` | the web site, for the links in the audits | `https://earthportal.eu` |
| `OFAIRE_API` | the O'FAIRe service | `https://services.earthportal.eu/ofaire/` |
| `OFAIRE_PORTAL` | the name of the portal for O'FAIRe (parameter `portal=`) | `earthportal` |
| `PORTAL_EXAMPLE` | one acronym of the portal, shown as an example in notebook 01 | `OSO` |

Then run the five notebooks in order, as described in the [README of the folder](earthportal_sa_audit/README.md).
If your portal's O'FAIRe service is at another address, or does not accept the `portal=` value you
give, notebook 01 stops with an HTTP error: ask the portal team which address and name to use.

## 2. Check: what notebook 01 needs from the API

Notebook 01 calls these paths, with the API key in the header:

- `/ontologies?include=all&also_include_views=true` (the catalogue, views included);
- `/ontology_metadata` and `/submission_metadata` (the metadata schema of the portal);
- `/ontologies/<ACRONYM>/latest_submission?display=all` (one call per entry).

They exist in the OntoPortal software, but a portal may run another version. If one answers with an
error, notebook 01 says which path failed.

## 3. Check: the files in `earthportal_sa_audit/reference/`

| File | Why it may differ on your portal | How to check |
|---|---|---|
| `ofaire_known_issues.csv` | **R1.3Q2** is marked *unreachable*: O'FAIRe gives its 20 points only to groups whose name contains OBO-FOUNDRY, WHEAT, CROP or INRAE, and EarthPortal has none. Your portal may have one. | Notebook 02 prints the groups of your portal and the groups R1.3Q2 would reward. If one matches, remove the R1.3Q2 row. |
| `manual_links.csv` | Six properties of the cheatsheet are linked by hand to the field that stores them on EarthPortal. | Notebook 04 lists, for every property, the portal field it found. Check the six rows against the schema of your portal (`data/raw/<date>/metadata_schema.json`). |
| `ofaire_properties.config.json`, `ofaire_code_vs_config.csv` | They come from the O'FAIRe code (commit `24def6b`). They change only if your portal runs another version of O'FAIRe. | Ask the portal team which version of O'FAIRe it runs. |

## 4. Check: the numbers that depend on the portal

- **The reachable maximum** (386 points on EarthPortal) is computed by notebook 02 from the questions
  your artefacts can score on. It changes if you change `ofaire_known_issues.csv`, so read it in the
  output of notebook 02; do not reuse 386.
- **F4Q2** (registration in other repositories) and **F4Q1** read the list of repositories and
  libraries written in the O'FAIRe code (`catalogs.config.json`). If your portal is not in that list,
  a registration there earns nothing.
- **Who fixes it.** The split between *author*, *curator* and *portal* is in notebook 04 (sets
  `PORTAL` and `CURATOR`, function `who_fixes`). It is a proposal for EarthPortal; validate it with
  your portal team.

## 5. Re-read the text

The Markdown cells of the notebooks comment the EarthPortal results (for example "OSO is first").
The code recomputes every number, but the comments do not change: re-read them, or ignore them, for
your portal. The guideline itself (the cheatsheet in `docs/`) is the same for every portal of the
Federation.
