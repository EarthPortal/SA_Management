# Management and Curation of EarthPortal Resources

Hello, and welcome to this project about the management and curation of the resources hosted in
[EarthPortal](https://earthportal.eu). The work was carried out within [Data Terra](https://www.data-terra.org/)
(CNRS) during an internship from 1 September to 31 October 2026, supervised by Christelle Pierkot.

Each subfolder of this repository is dedicated to a specific activity and has its own README with
more details:

- **`docs/`**: the reports and slides written during the internship, such as the quick reference
  table (cheatsheet) of the OntoPortal Metadata Guidelines, which the pipeline reads.
- **`earthportal_sa_audit/`**: the pipeline. Five notebooks build a state of the art of the semantic
  artefacts hosted in EarthPortal at the date of a snapshot (O'FAIRe scores, comparison with the
  Metadata Guidelines), and write one audit per artefact, as a page and as a JSON file. The notebooks
  also save the figures used in the slides (`earthportal_sa_audit/figures/`), so each figure comes
  from the committed data.

To learn more about a subfolder, please open its README first. Three short files at the root
complete them:

- [`ARCHITECTURE.md`](ARCHITECTURE.md): how the pipeline is built, and which file each step reads and writes;
- [`ADAPTING.md`](ADAPTING.md): what to change and check to run the pipeline on another OntoPortal portal;
- [`CHANGELOG.md`](CHANGELOG.md): what changed in each release.

## Reproducibility

### 1. Prerequisites

![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04.3%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12.3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-2.43.0-F05032?style=for-the-badge&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-1.109.3-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

Our development environment runs smoothly on:

- [Ubuntu](https://ubuntu.com/) 24.04.3 LTS *(required: or any modern Linux system)*
- [Python](https://www.python.org/) 3.12.3 *(required: 3.12 or later; check with `python3 --version`)*
- [Git](https://git-scm.com/) 2.43.0 *(required: check with `git --version`)*
- [Visual Studio Code](https://code.visualstudio.com/) 1.109.3 *(optional: use any editor you like!)*

You also need an **API key of the portal** you audit (EarthPortal by default): create an account on
[earthportal.eu](https://earthportal.eu), then copy the key shown on your account page. Only notebook 01
(data collection) uses it.

### 2. First-time setup

![pip](https://img.shields.io/badge/pip-Package%20Manager-3775A9?style=flat-square&logo=pypi&logoColor=white)
![venv](https://img.shields.io/badge/venv-Virtual%20Environment-3776AB?style=flat-square&logo=python&logoColor=white)

1. Clone the repository and move into it:

```bash
   git clone https://github.com/EarthPortal/SA_Management.git
   cd SA_Management
```

2. Create and activate a virtual environment:

```bash
   python3 -m venv .venv
   source .venv/bin/activate
```

3. Install the Python dependencies:

```bash
   pip install -r requirements.txt
```

4. Register the virtual environment as a Jupyter kernel:

```bash
   python3 -m ipykernel install --user --name data-terra-venv --display-name "Data Terra (.venv)"
```

   > **Why?** The notebooks expect a kernel named `data-terra-venv`. JupyterLab and
   > `jupyter nbconvert` need this name (they are not in `requirements.txt`: install them with
   > `pip install jupyterlab`). In VS Code, you can also choose `.venv` directly when you select the
   > kernel (*Python Environments* > `.venv`).

5. Create your `.env` file from the template, then write your API key after `PORTAL_APIKEY=`:

```bash
   cp .env.example .env
   nano .env        # or open it in VS Code
```

   > **Note:** `.env` holds your personal API key. It is listed in `.gitignore`: never commit it
   > and never share it. Besides the key, `.env` can hold `RUN_DATE` (the snapshot to work on) and,
   > for another portal, the variables described in [`ADAPTING.md`](ADAPTING.md).

### 3. Updating an existing copy

If you already set up the project and only want the latest changes (for example, a new folder
you did not have before):

1. Move to the project directory:

```bash
   cd SA_Management
```

2. Pull the latest changes:

```bash
   git pull
```

3. Activate your virtual environment:

```bash
   source .venv/bin/activate
```

4. Install any new dependencies:

```bash
   pip install -r requirements.txt
```

5. Compare `.env.example` with your `.env`, and add any new variable it lists.

Then open the README of the new folder to learn how to use it.

## How to cite

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23417011.svg)](https://doi.org/10.5281/zenodo.23417011)

If you use these notebooks or reports, please cite them with the DOI above. It always points to
the latest release on Zenodo; each release also has its own DOI, listed on the Zenodo page. You can
also click **Cite this repository** on the GitHub page.

The slides have their own record on Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23391527.svg)](https://doi.org/10.5281/zenodo.23391527).
Each presentation is a version of this record, with its own DOI: to refer to one talk, please cite
the DOI of its version.

## License

[MIT](LICENSE).
