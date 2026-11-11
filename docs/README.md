# docs

This folder holds the reports and slides of my internship at Data Terra (CNRS), from 1 September to
31 October 2026. Each `.tex` file is compiled to the PDF of the same name under `build/`.

| Document | What it is about | PDF |
|---|---|---|
| Report 1: MOD cheatsheet | A quick reference table (cheatsheet) of the OntoPortal Metadata Guidelines: the 99 properties, with their usage (Mandatory, Recommended, Optional), their FAIR principle and their MOD property. **Notebook 04 reads this `.tex` file**: please do not rename it. | [PDF](build/emmanuel_dataTerra_Report1-MOD-Cheatsheet.pdf) |
| Report 2: O'FAIRe questions | The 61 questions of O'FAIRe in a human-readable table, written from `questions.config.json`: their points and the properties each one reads. | [PDF](build/emmanuel_dataTerra_Report2-OFAIRe-Questions.pdf) |
| Report 3: O'FAIRe properties | The 123 properties of O'FAIRe in a human-readable table, written from `properties.config.json`. | [PDF](build/emmanuel_dataTerra_Report3-OFAIRe-Properties.pdf) |
| Report 4: O'FAIRe Java implementation | How the Java code of O'FAIRe computes each question, and where it works differently from the configuration files. | [PDF](build/emmanuel_dataTerra_Report4-OFAIRe-Java-Implementation.pdf) |
| Report 5: cheatsheet vs EarthPortal | Two observations on the guidelines and the EarthPortal schema: some properties are stored under another name, and some fields expected by the portal are not in the guidelines. | [PDF](build/emmanuel_dataTerra_Report5-Cheatsheet-vs-EarthPortal.pdf) |
| Report 6: curation interface | A proposal for a user interface for the curation of EarthPortal, built on the JSON audits (design, not code). | [PDF](build/emmanuel_dataTerra_Report6-Curation-Interface.pdf) |
| Slides, 9 October 2026 | *Monitoring and improving the FAIRness of EarthPortal semantic artefacts*: first results, presented at the Data Terra team meeting. | [PDF](build/emmanuel_dataTerra_Slides_2026-10-09.pdf) |
| Slides, 13 November 2026 | *From the Metadata Guidelines to curation actions*: the pipeline and the results of 10 November 2026, presented to the OntoPortal Federation (Editorial Board and coordination group). | [PDF](build/emmanuel_dataTerra_Slides_2026-11-13_EditorialBoard.pdf) |

The slides are also archived on Zenodo, one version per presentation:
[10.5281/zenodo.23391527](https://doi.org/10.5281/zenodo.23391527). The slides of the TIB and Data
Terra meeting of 13 November 2026 are only there, as their own version
([10.5281/zenodo.24132003](https://doi.org/10.5281/zenodo.24132003)).

## Figures

- `Figures/`: the figures of the reports and of the slides of 9 October, and the logos of CNRS,
  Data Terra and SISSA.
- `Figures/slides_2026-11-13/`: for the slides of 13 November, the screenshots of the audits taken
  from the snapshot of 10 November 2026, the logos, the Earth picture and the QR codes.
- The charts of the slides of 13 November are not copied here: they are read from
  `../earthportal_sa_audit/figures/`, where notebooks 03 and 05 save them, so that each chart comes
  from the same data as the tables.

## How to compile

I use **TeX Live** with **LaTeX Workshop** in **VS Code**, which avoids the timeouts of Overleaf.
The file `.latexmkrc` compiles with pdfLaTeX and sends every output to `build/`; only the PDFs are
committed. Always compile from this folder, so that every path is found:

```bash
cd docs
latexmk emmanuel_dataTerra_Report5-Cheatsheet-vs-EarthPortal.tex
```

`latexmk` with no file name compiles Report 1. What each document needs (all part of TeX Live):

- the reports: `dataterra-report.sty` and `DataTerra_internship.bib`, which are in this folder;
- the slides of 9 October: the Beamer theme `metropolis`;
- the slides of 13 November: the packages `lato` (the font; without it, pdfLaTeX uses Helvetica) and
  `qrcode`, and the figures of `../earthportal_sa_audit/figures/`.
