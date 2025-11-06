from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    model_config = {
    "from_attributes": True
}


class Token(BaseModel):
    access_token: str
    token_type: str
