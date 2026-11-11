# earthportal_sa_audit

State of the art of the semantic artefacts hosted in [EarthPortal](https://earthportal.eu): their
O'FAIRe scores, how their metadata compare with the Metadata Guidelines, and one audit per artefact,
with two parts (FAIRness and compliance with the guideline).

The setup (virtual environment, `requirements.txt`, `.env` with your API key) is described in the
[README at the root of the repository](../README.md). This folder needs nothing more.

## How to run it

Open the notebooks in VS Code, choose the kernel **Data Terra (.venv)** (step 4 of the
[root README](../README.md)), and run them in order. Each notebook reads only the files written by the
ones before it.

| Notebook | What it does | What it saves |
|---|---|---|
| `01_collect_data.ipynb` | Downloads the catalogue, the portal's metadata schema, the latest submission of every ontology and its O'FAIRe assessment | `data/raw/<date>/` |
| `02_ofaire_scores.ipynb` | Builds one table: one row per ontology, its overall scores and its points on each of the 61 O'FAIRe questions | `data/ofaire_scores_<date>.csv`, `data/ofaire_questions.csv` |
| `03_eda.ipynb` | Explores the scores of the artefacts: where the catalogue loses points, profiling report, plots, duplicated artefacts | `data/question_summary.csv`, `reports/eda_<date>.html`, four figures in `figures/` |
| `04_guideline_vs_ofaire.ipynb` | Turns the cheatsheet of the Metadata Guidelines into a machine-readable table, finds where the portal stores each attribute, and links each O'FAIRe question to the attributes it reads | `mapping/guideline_profile.csv` (and `.json`), `mapping/ofaire_vs_guideline.csv` |
| `05_audits.ipynb` | Writes one audit per ontology in two parts: its FAIRness (O'FAIRe scores, questions where it loses points) and its compliance with the guideline (status of the 99 properties), with the suggested actions and who can take them | `audits/json/<ACRONYM>.json` (the data), `audits/<ACRONYM>.md` (the page), `audits/index.md`, `data/guideline_status.csv`, `data/actions.csv`, two figures in `figures/` |

**Figures.** Notebooks 03 and 05 save their figures as PDF in `figures/`. The slides in `docs/` use these
files as they are, so every figure shown in a presentation comes from the same data as the tables.

Only notebook 01 needs the network and the API key. To work again on an older snapshot, write its
date in `.env` (for example `RUN_DATE=2026-10-16`) and run notebooks 02 to 05.

**Which files keep a date?** The raw data (`data/raw/<date>/`, not committed) and the scores
(`data/ofaire_scores_<date>.csv`, small, one file per snapshot, to follow the catalogue over time).
Every other output describes the **latest snapshot only** and is replaced at each run: the tables, the
audits, the figures, and the profiling report (`reports/eda_<date>.html`: notebook 03 removes the report
of the previous run, so the folder always holds one report, whose name gives its date). The snapshot
date of the audits is written in `audits/index.md`, at the top of each audit page and in the key
`snapshot` of each JSON file. Older versions stay in the Git history and in
the Zenodo archive of each release. `data/ofaire_questions.csv` does not depend on the snapshot at
all: it is the same table of the 61 questions every time.

To run the notebooks without opening them, for example on a server:

```bash
cd earthportal_sa_audit
for nb in 0[1-5]_*.ipynb; do
  jupyter nbconvert --to notebook --execute --inplace "$nb"
done
```

This needs `jupyter nbconvert` (`pip install jupyterlab` installs it; it is not in `requirements.txt`)
and the registered kernel `data-terra-venv` (step 4 of the [root README](../README.md)), or add
`--ExecutePreprocessor.kernel_name=python3` with the virtual environment activated.

`config.py` is a small script shared by the notebooks: it reads `.env` and defines the portal
addresses and where each file goes. It works for EarthPortal by default; for another OntoPortal
portal, see [`ADAPTING.md`](../ADAPTING.md). The `reference/` folder holds four short tables used by the notebooks:

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
- **Status of a property.** *filled*, *empty* or *not applicable*. Empty means a value that is null,
  `""`, `[]` or `{}`; an agent or a contact with nothing but its identifier counts as empty too. *This
  ontology is a view of* applies only to views, and *Was invalidated by* only to retired ontologies.
  Filled means present: whether the value is correct is not checked.
- **Priority of an action.** Every empty property of the guideline is an action. 1 = Mandatory;
  2 = Recommended and costing O'FAIRe points; 3 = Optional and costing O'FAIRe points; 4 = Recommended
  only; 5 = Optional only. After the Mandatory properties, what costs points comes first.
- **Share of the points lost.** When a question loses points and reads several empty attributes, the
  lost points are divided equally among them. It is a way to rank the actions, not a promise of
  points, because O'FAIRe has its own rule for each question: for example, I1Q5 needs *Has format* and
  *Is format of* together, one attribute is enough for I2Q6, and F1Q2 gives its full 11 points only to
  a DOI that the DOI service knows (any other valid URL gives 6).
- **Who fixes it.** *author* (in the file or the submission form), *curator* (the portal team: administrators, curation), or *portal* (values it generates
  itself). This split is a proposal, to be validated ...

## Latest results (snapshot of 10 November 2026)

- 92 public entries: 68 artefacts, 19 views, 5 records without content.
- Artefacts: O'FAIRe score median 54 / 100; reachable score median about 67 %, from 49.5 % to
  94.4 % (OSO is first).
- The catalogue loses most points on F1Q2 (external identifier or DOI: 65 of 68 artefacts score 0),
  F4Q2 (registration in other repositories), R1.3Q1 (projects or endorsements: 50 artefacts score 0)
  and F1Q4 (version IRI).
- Of the 99 attributes of the cheatsheet, 72 are found under the same name, 21 through a mapping and
  6 by hand (`reference/manual_links.csv`); 26 are stored by EarthPortal under another property name.
- Mandatory attributes most often empty: Modification date (27 artefacts), Location (24),
  Creator (23), Categories (20), License (15).

The results of earlier snapshots (28 September, 2, 6, 8 and 16 October 2026) are in the Git history
and in the earlier releases on Zenodo.

## The JSON audits

`audits/json/<ACRONYM>.json` holds everything the page `audits/<ACRONYM>.md` says, and the page is
written from it. It is meant for programs, for example a curation interface. Its keys: `acronym`,
`name`, `kind`, `snapshot`, `portal_page`; `fairness` (scores, rank, `points_lost`); `guideline`
(`summary` by usage, and the 99 `properties` with their status); `actions` (priority, who fixes it,
property, where the portal stores it, O'FAIRe questions, share of points, note). It holds no value of
the metadata, so no name or e-mail address of a person.

## Note

- `data/raw/` is not committed: the raw API answers contain contact e-mail addresses, and some
  records expose other portals' API keys in their pull URL.
