from pydantic import BaseModel
from typing import Optional
from enum import Enum


class LeadStatus(str, Enum):
    new = "new"
    contacted = "contacted"
    qualified = "qualified"
    disqualified = "disqualified"


class LeadCreate(BaseModel):
    name: str
    contact_info: str
    source: Optional[str] = None
    interest_level: Optional[str] = None
    notes: Optional[str] = None
    assigned_agent_id: Optional[int] = None


class LeadOut(BaseModel):
    id: int
    name: str
    contact_info: str
    source: Optional[str]
    interest_level: Optional[str]
    status: LeadStatus
    notes: Optional[str]
    assigned_agent_id: Optional[int]

    model_config = {
        "from_attributes": True
    }
