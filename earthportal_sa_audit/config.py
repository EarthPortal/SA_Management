"""
The goal of this script is to keep, in one place, the settings shared by the notebooks of this
folder. It reads the portal settings and the API key from the single .env file at the root of the
repository, chooses the date of the snapshot to work on, and defines where each notebook reads and
saves its files.
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

# The portal to audit. Every value can be changed in .env; without .env, the pipeline audits EarthPortal.
# To run it on another OntoPortal portal, read ADAPTING.md at the root of the repository.
PORTAL_NAME = os.getenv("PORTAL_NAME") or "EarthPortal"                         # shown in the audits
API_URL = os.getenv("PORTAL_API") or "https://data.earthportal.eu"              # REST API
PORTAL_UI = os.getenv("PORTAL_UI") or "https://earthportal.eu"                  # web pages, for the links in the audits
OFAIRE_URL = os.getenv("OFAIRE_API") or "https://services.earthportal.eu/ofaire/"
OFAIRE_PORTAL = os.getenv("OFAIRE_PORTAL") or "earthportal"                     # the portal's name for O'FAIRe
EXAMPLE = os.getenv("PORTAL_EXAMPLE") or "OSO"                                  # one acronym, shown as an example in notebook 01
# os.getenv(name, "") returns the value, or an empty string if the variable is missing.
# EARTHPORTAL_APIKEY is still accepted, so that older .env files keep working.
APIKEY = os.getenv("PORTAL_APIKEY") or os.getenv("EARTHPORTAL_APIKEY", "")

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
REPORTS = FOLDER / "reports"                      # profiling report of the latest snapshot
FIGURES = FOLDER / "figures"                      # figures of the latest snapshot (used by the slides)
MAPPING = FOLDER / "mapping"
AUDITS = FOLDER / "audits"
# "parents=True" creates any missing parent folders (data/, then raw/, then the date) while "exist_ok=True" means "no error if the folder is already there"
for folder in (RAW, DATA, REPORTS, FIGURES, MAPPING, AUDITS):
    folder.mkdir(parents=True, exist_ok=True)


def kind_of(ontology):
    """
    This function sorts each catalogue entry into the three groups we use in every count
    (for example, on 10 November 2026: 68 artefacts + 19 views (a view of another artefact)
    + 5 metadata-only records (no content uploaded)).
    """
    if ontology.get("viewOf"):
        return "view"
    if ontology.get("summaryOnly"):
        return "metadata-only"
    return "artefact"
