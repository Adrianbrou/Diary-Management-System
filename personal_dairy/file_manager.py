import json
import os

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
DIARY_FILE = os.path.join(DATA_DIR, "diary_entries.json")


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)


def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
