from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InventoryLogBase(BaseModel):
    product_id: int
    change: float
    reason: str



class InventoryLogCreate(InventoryLogBase):
    pass  


class InventoryLogUpdate(BaseModel):
    change: Optional[float] = None
    reason: Optional[str] = None


class InventoryLogOut(InventoryLogBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
