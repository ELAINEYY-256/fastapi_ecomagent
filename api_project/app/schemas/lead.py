from pydantic import BaseModel
from typing import Optional
from enum import Enum


class LeadStatus(str, Enum):
    new = "new"
    contacted = "contacted"
    qualified = "qualified"
    disqualified = "disqualified"


class LeadBase(BaseModel):
    name: str
    contact_info: str
    source: Optional[str] = None
    interest_level: Optional[str] = None
    status: Optional[LeadStatus] = LeadStatus.new
    notes: Optional[str] = None
    assigned_agent_id: Optional[int] = None



class LeadCreate(LeadBase):
    pass 


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    contact_info: Optional[str] = None
    source: Optional[str] = None
    interest_level: Optional[str] = None
    status: Optional[LeadStatus] = None
    notes: Optional[str] = None
    assigned_agent_id: Optional[int] = None


class LeadOut(LeadBase):
    id: int

    class Config:
        from_attributes = True
