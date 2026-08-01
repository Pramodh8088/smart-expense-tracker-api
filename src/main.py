from fastapi import FastAPI,Query,HTTPException,status
from src.schemas import Expense, ExpenseCreate
from src.storage import load_expenses, save_expenses



app = FastAPI(
    title="Smart Expense Tracker API",
    description="A REST API to manage personal expenses",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API"
    }


@app.post(
    "/expenses",
    status_code=status.HTTP_201_CREATED,
    tags=["Expenses"]
)
def add_expense(expense: ExpenseCreate):

    expenses = load_expenses()

    new_id = 1

    if expenses:
        new_id = max(exp["id"] for exp in expenses) + 1

    new_expense = {
        "id": new_id,
        **expense.model_dump()
    }

    expenses.append(new_expense)

    save_expenses(expenses)

    return {
        "message": "Expense added successfully",
        "expense": new_expense
    }


@app.get(
    "/expenses",
    tags=["Expenses"]
)
def get_expenses(category: str = Query(default=None)):

    expenses = load_expenses()

    if category:
        expenses = [
            expense for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return {
        "total_expenses": len(expenses),
        "expenses": expenses
    }

@app.get(
    "/expenses/total",
    tags=["Reports"]
)
def get_total_expenses(category: str = Query(default=None)):

    expenses = load_expenses()

    if category:
        expenses = [
            expense for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    total = sum(expense["amount"] for expense in expenses)

    return {
        "category": category if category else "All",
        "total_expense": total
    }

@app.delete(
    "/expenses/{expense_id}",
    tags=["Expenses"]
)
def delete_expense(expense_id: int):

    expenses = load_expenses()

    updated_expenses = [
        expense for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    save_expenses(updated_expenses)

    return {
        "message": "Expense deleted successfully"
    }