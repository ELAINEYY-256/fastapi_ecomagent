from pydantic import BaseModel
from typing import Optional, List


class ClientBase(BaseModel):
    name: str
    contact_info: str
    agent_id: Optional[int] = None
    lead_id: Optional[int] = None



class ClientCreate(ClientBase):
    pass  


class ClientUpdate(BaseModel):
    name: Optional[str] = None
    contact_info: Optional[str] = None
    agent_id: Optional[int] = None
    lead_id: Optional[int] = None


class ClientOut(ClientBase):
    id: int

    class Config:
        from_attributes = True
