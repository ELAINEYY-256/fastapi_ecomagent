from pydantic import BaseModel, EmailStr
from typing import Optional

class CompanySignupRequest(BaseModel):
    company_name: str
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    password: str

class CompanySignupResponse(BaseModel):
    company_id: int
    user_id: int
    email: EmailStr
    role: str
    token: str
