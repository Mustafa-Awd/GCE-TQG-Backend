import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def loadTopics(filename="ICT"):
    FILE_PATH = BASE_DIR.parent / "data" / f"{filename}.json"
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        syllabus = json.load(file)
    topics = list(syllabus.keys())

    return topics