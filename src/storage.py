import json
from pathlib import Path

FILE_PATH = Path("expenses.json")


def load_expenses():
    if not FILE_PATH.exists():
        return []

    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4, default=str)