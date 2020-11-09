from datetime import date
from typing import List, Dict
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    coin: str


class PriceInput(BaseModel):
    start: date
    end: date
    price: List[Item]
    market_cap: List[Item]


class PriceOutput(PriceInput):
    id: str