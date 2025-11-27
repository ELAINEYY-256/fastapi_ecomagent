from pydantic import BaseModel
from typing import Optional

class BranchBase(BaseModel):
    name: str
    location: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    region: Optional[str] = None
    physical_address: Optional[str] = None
    is_head_branch: Optional[bool] = False

class BranchCreate(BranchBase):
    company_id: int

class BranchUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    is_head_branch: Optional[bool] = None
    country: Optional[str] = None
    state: Optional[str] = None
    region: Optional[str] = None
    physical_address: Optional[str] = None

class BranchOut(BranchBase):
    id: int
    company_id: int

    class Config:
        from_attributes = True
