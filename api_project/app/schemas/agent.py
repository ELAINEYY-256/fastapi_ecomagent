from pydantic import BaseModel
from typing import Optional


class AgentBase(BaseModel):
    contact_info: str
    region: Optional[str] = None
    performance_score: Optional[float] = 0.0


class AgentCreate(AgentBase):
    user_id: int


class AgentUpdate(BaseModel):
    contact_info: Optional[str] = None
    region: Optional[str] = None
    performance_score: Optional[float] = None


class AgentOut(AgentBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
