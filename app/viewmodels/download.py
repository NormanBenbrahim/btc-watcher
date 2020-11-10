from datetime import date
from typing import Optional, List
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

class PriceInput(BaseModel):
    start: date
    end: date
    incomes: List[Item]
    expenses: List[Item]


class PriceOutput(PriceInput):
    id: str

class PriceOutput(PriceInput):
    id: str