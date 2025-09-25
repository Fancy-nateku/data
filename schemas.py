from pydantic import BaseModel
from typing import Optional
from datetime import date as DateType

#Farmer schemas
class FarmerBase(BaseModel):
    name: str
    email: str

class FarmerCreate(FarmerBase):
    pass

class Farmer(FarmerBase):
    id: int

    model_config = {
        "from_attributes": True
    }

#Expense schemas
class ExpenseBase(BaseModel):
    item: str
    cost: float
    date: DateType
    category: Optional[str] = None
    description: Optional[str] = None

class ExpenseCreate(ExpenseBase):
    farmer_id: int  # link to Farmer

class ExpenseUpdate(BaseModel):
    item: Optional[str] = None
    cost: Optional[float] = None
    date: Optional[DateType] = None
    category: Optional[str] = None
    description: Optional[str] = None

class Expense(ExpenseBase):
    id: int
    farmer_id: int

    model_config = {
"from_attributes": True
    }
