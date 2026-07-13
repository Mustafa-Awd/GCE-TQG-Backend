import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR.parent / "data" / "ICT.json"

with open(FILE_PATH, "r" , encoding="utf-8") as file:
    syllabus = json.load(file)