from datetime import date
from typing import Optional, List
from pydantic import BaseModel

class Months(BaseModel):
    """
    Schema for number of months
    """
    name: str
    months: int