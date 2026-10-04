# Management and Curation of EarthPortal Resources

Hello, and welcome to this project about the management and curation of the resources hosted in
[EarthPortal](https://earthportal.eu). The work is carried out within [Data Terra](https://www.data-terra.org/)
as a six-month internship.

Each subfolder of this repository is dedicated to a specific activity and has its own README with
more details:

- **`docs/`**: short reports written during the internship, such as the quick reference table
  (cheatsheet) for the OntoPortal Metadata Guidelines and the state of the art of EarthPortal.
- **`earthportal_sa_audit/`**: state of the art of the semantic artefacts currently hosted in the
  EarthPortal catalogue (O'FAIRe scores, comparison with the Metadata Guidelines, one audit per
  artefact).
- Other folders are coming soon.

To learn more about a subfolder, please open its README first.

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

You also need an **EarthPortal API key**: create an account on [earthportal.eu](https://earthportal.eu),
then copy the key shown on your account page.

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

4. *(Optional)* Register a Jupyter kernel, if you want to run notebooks:

```bash
   python3 -m ipykernel install --user --name data-terra-venv --display-name "Data Terra (.venv)"
```

5. Create your `.env` file from the template, then write your API key in it:

```bash
   cp .env.example .env
   nano .env        # or open it in VS Code
```

   > **Note:** `.env` holds your personal API key. It is listed in `.gitignore`: never commit it
   > and never share it. Several folders of this repository reads this single file.

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