# Smart Expense Tracker API

A RESTful Expense Tracker API built with **FastAPI** to manage personal expenses. The API supports creating, retrieving, filtering, summarizing, and deleting expenses using JSON file storage.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses (overall and by category)
- Delete an expense
- Interactive Swagger/OpenAPI documentation
- Automated unit tests using Pytest

## Tech Stack

- Python 3
- FastAPI
- Pydantic
- Pytest
- JSON File Storage

## Project Structure

```
smart-expense-tracker-api/
│── README.md
│── AI_NOTES.md
│── requirements.txt
│── pytest.ini
│── expenses.json
│
├── src/
│   ├── main.py
│   ├── schemas.py
│   ├── storage.py
│   ├── utils.py
│   └── __init__.py
│
└── tests/
    ├── __init__.py
    └── test_api.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Pramodh8088/smart-expense-tracker-api.git
cd smart-expense-tracker-api
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## API Documentation

Interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```

## Run the Tests

```bash
pytest
```

## Sample Data

The project includes sample expense records in `expenses.json` to make testing easier. You can edit or clear the file if you want to start with an empty dataset.

## Author

**Pramodh HS**