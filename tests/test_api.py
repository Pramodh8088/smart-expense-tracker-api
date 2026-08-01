from fastapi.testclient import TestClient
from src.main import app
import json

client = TestClient(app)


def setup_function():
    # Reset the JSON file before each test
    with open("expenses.json", "w") as file:
        json.dump([], file)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 450,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    assert response.status_code == 201
    assert response.json()["expense"]["title"] == "Pizza"


def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200


def test_filter_expenses():
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 450,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    response = client.get("/expenses?category=Food")

    assert response.status_code == 200
    assert response.json()["total_expenses"] == 1


def test_total_expenses():
    response = client.get("/expenses/total")
    assert response.status_code == 200


def test_delete_invalid():
    response = client.delete("/expenses/99")
    assert response.status_code == 404

def test_delete_expense():

    client.post(
        "/expenses",
        json={
            "title":"Pizza",
            "amount":450,
            "category":"Food",
            "date":"2026-07-31"
        }
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200

def test_total_by_category():

    client.post(
        "/expenses",
        json={
            "title":"Pizza",
            "amount":450,
            "category":"Food",
            "date":"2026-07-31"
        }
    )

    response = client.get("/expenses/total?category=Food")

    assert response.status_code == 200
    assert response.json()["total_expense"] == 450