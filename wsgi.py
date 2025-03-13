import sys
import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR))

os.environ["FLASK_APP"] = "app"

from app import app as application