from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime


class OrderStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    delivered = "delivered"


class OrderBase(BaseModel):
    client_id: int
    agent_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: int
    total_price: float
    status: Optional[OrderStatus] = OrderStatus.pending


class OrderCreate(OrderBase):
    pass  


class OrderUpdate(BaseModel):
    quantity: Optional[int] = None
    total_price: Optional[float] = None
    status: Optional[OrderStatus] = None


class OrderOut(OrderBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
