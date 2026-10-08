"""
The goal of this script is to keep, in one place, the settings shared by the notebooks of this
folder. It reads the API key from the single .env file at the root of the repository, chooses the
date of the snapshot to work on, and defines where each notebook reads and saves its files.
The notebooks import it with:  from config import *
"""
import datetime as dt
import os
from pathlib import Path

from dotenv import load_dotenv

# __file__ holds the path of config.py itself, .resolve() turns it into an absolute path, and .parent moves up one level to the folder that contains it.
FOLDER = Path(__file__).resolve().parent          # => earthportal_sa_audit/
# REPO goes up one more level, to the root of SA_Management
REPO = FOLDER.parent                              # => SA_Management/
# The "/" operator on a Path joins path parts, so REPO / ".env" is <repo>/.env
load_dotenv(REPO / ".env")

# Web services
API_URL = "https://data.earthportal.eu"
OFAIRE_URL = "https://services.earthportal.eu/ofaire/"
# os.getenv(name, "") returns the value, or an empty string if the variable is missing
APIKEY = os.getenv("EARTHPORTAL_APIKEY", "")

# Snapshot date: today by default, or the date written as RUN_DATE in .env
RUN_DATE = os.getenv("RUN_DATE") or dt.date.today().isoformat()

# Inputs
CHEATSHEET = REPO / "docs" / "emmanuel_dataTerra_Report1-MOD-Cheatsheet.tex"
OFAIRE_PROPERTIES = FOLDER / "reference" / "ofaire_properties.config.json"
KNOWN_ISSUES = FOLDER / "reference" / "ofaire_known_issues.csv"
CODE_VS_CONFIG = FOLDER / "reference" / "ofaire_code_vs_config.csv"
MANUAL_LINKS = FOLDER / "reference" / "manual_links.csv"

# Outputs
RAW = FOLDER / "data" / "raw" / RUN_DATE          # untouched API answers (not committed)
DATA = FOLDER / "data"                            # tables built from them
REPORTS = FOLDER / "reports"
MAPPING = FOLDER / "mapping"
AUDITS = FOLDER / "audits"
# "parents=True" creates any missing parent folders (data/, then raw/, then the date) while "exist_ok=True" means "no error if the folder is already there"
for folder in (RAW, DATA, REPORTS, MAPPING, AUDITS):
    folder.mkdir(parents=True, exist_ok=True)


def kind_of(ontology):
    """
    This function sorts each catalogue entry into the three groups we use in every count 
    (for example 70 artefacts + 16 views (a view of another artefact) + 5 metadata-only (no content uploaded)).
    """
    if ontology.get("viewOf"):
        return "view"
    if ontology.get("summaryOnly"):
        return "metadata-only"
    return "artefact"
