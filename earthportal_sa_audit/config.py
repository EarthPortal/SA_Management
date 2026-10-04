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

FOLDER = Path(__file__).resolve().parent          # earthportal_sa_audit/
REPO = FOLDER.parent                              # root of the repository
load_dotenv(REPO / ".env")

# Web services
API_URL = "https://data.earthportal.eu"
OFAIRE_URL = "https://services.earthportal.eu/ofaire/"
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
for folder in (RAW, DATA, REPORTS, MAPPING, AUDITS):
    folder.mkdir(parents=True, exist_ok=True)


def kind_of(ontology):
    """artefact, view (a view of another artefact) or metadata-only (no content uploaded)."""
    if ontology.get("viewOf"):
        return "view"
    if ontology.get("summaryOnly"):
        return "metadata-only"
    return "artefact"
