# earthportal_sa_audit

State of the art of the semantic artefacts hosted in [EarthPortal](https://earthportal.eu): their
O'FAIRe scores, how their metadata compare with the Metadata Guidelines, and one audit per artefact.

The setup (virtual environment, `requirements.txt`, `.env` with your API key) is described in the
[README at the root of the repository](../README.md). This folder needs nothing more.

## How to run it

Open the notebooks in VS Code, choose the kernel **Data Terra (.venv)**, and run them in order. Each
notebook reads only the files written by the ones before it.

| Notebook | What it does | What it saves |
|---|---|---|
| `01_collect_data.ipynb` | Downloads the catalogue, the portal's metadata schema, the latest submission of every ontology and its O'FAIRe assessment | `data/raw/<date>/` |
| `02_ofaire_scores.ipynb` | Builds one table: one row per ontology, its overall scores and its points on each of the 61 O'FAIRe questions | `data/ofaire_scores_<date>.csv`, `data/ofaire_questions_<date>.csv` |
| `03_eda.ipynb` | Explores the scores of the artefacts: where the catalogue loses points, profiling report, plots | `reports/eda_<date>.html`, `data/question_summary_<date>.csv` |
| `04_guideline_vs_ofaire.ipynb` | Turns the cheatsheet of the Metadata Guidelines into a machine-readable table, finds where EarthPortal stores each attribute, and links each O'FAIRe question to the attributes it reads | `mapping/guideline_profile.csv` (and `.json`), `mapping/ofaire_vs_guideline.csv` |
| `05_audits.ipynb` | Writes one audit per ontology: its scores, the questions where it loses points, its empty attributes and who can fill them in | `audits/<ACRONYM>.md`, `audits/index.md`, `data/actions_<date>.csv` |

Only notebook 01 needs the network and the API key. To work again on an older snapshot, write its
date in `.env` (for example `RUN_DATE=2026-09-28`) and run notebooks 02 to 05.

`config.py` is a small script shared by the notebooks: it reads `.env` and defines where each file
goes. The `reference/` folder holds four short tables used by the notebooks:

- `ofaire_properties.config.json`: the fields O'FAIRe reads, from the O'FAIRe source code
  ([agroportal/fairness](https://github.com/agroportal/fairness), commit `24def6b`);
- `ofaire_known_issues.csv`: two O'FAIRe questions that behave in a special way, with the evidence;
- `ofaire_code_vs_config.csv`: the few places where the O'FAIRe code reads other properties than its
  configuration declares, with the evidence (same commit);
- `manual_links.csv`: the six cheatsheet attributes whose portal field cannot be found automatically,
  each with its reason.

The cheatsheet itself is read from [`docs/`](../docs).

## How to read the results

- **Reachable score.** O'FAIRe counts 478 points, but no EarthPortal artefact can earn 92 of them:
  ten questions are not implemented in O'FAIRe (70 points), R1.3Q2 only rewards AgroPortal groups or
  the OBO library (20 points), and the five questions of I1 add up to 42 points while O'FAIRe counts
  44 for I1 (2 points). The reachable score divides the points by the remaining **386**; it is the
  score that curation can move.
- **Inside the reachable maximum**, three rules of O'FAIRe still keep some points away: I2Q7 cannot
  give more than 3.75 of its 5 points, I1Q1 gives its 18 points only to OWL (15 to SKOS), and the last
  2 points of R1.2Q2 ask for *Was invalidated by*, which only makes sense for a retired artefact (the
  audits do not suggest it for the others).
- **Empty attribute.** A value that is null, `""`, `[]` or `{}`. An agent or a contact with nothing
  but its identifier counts as empty too.
- **Priority of an action.** 1 = Mandatory; 2 = Recommended and costing O'FAIRe points;
  3 = Recommended only; 4 = Optional but costing O'FAIRe points.
- **Share of the points lost.** When a question loses points and reads several empty attributes, the
  lost points are divided equally among them. It is a way to rank the actions, not a promise of
  points, because O'FAIRe has its own rule for each question: for example, I1Q5 needs *Has format* and
  *Is format of* together, one attribute is enough for I2Q6, and F1Q2 gives its 11 points only to a
  valid DOI.
- **Who fixes it.** *author* (in the file or the submission form), *curator* (the EarthPortal team: administrators, curation), or *portal* (values it generates
  itself). This split is a proposal, to be validated ...

## First results (snapshot of 28 September 2026)

- 91 public entries: 70 artefacts, 16 views, 5 records without content.
- Artefacts: O'FAIRe score median 53.5 / 100; reachable score median about 67 %, from 49.5 % to
  93.9 % (OSO is first).
- The catalogue loses most points on F1Q2 (external identifier or DOI: 66 of 70 artefacts score 0),
  F4Q2 (registration in other repositories), R1.3Q1 (projects or endorsements) and F1Q4 (version IRI).
- Of the 99 attributes of the cheatsheet, 26 are stored by EarthPortal under another property name.
- Mandatory attributes most often empty: Modification date (28 artefacts), Location (26),
  Creator (24), Categories (20), License (16).

## Note

- `data/raw/` is not committed: the raw API answers contain contact e-mail addresses, and some
  records expose other portals' API keys in their pull URL.
