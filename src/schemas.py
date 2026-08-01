from pydantic import BaseModel, Field
from datetime import date


class ExpenseCreate(BaseModel):
    title: str
    amount: float = Field(gt=0)
    category: str
    date: date


class Expense(ExpenseCreate):
    id: int