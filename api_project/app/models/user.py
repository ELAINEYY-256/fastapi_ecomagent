from sqlalchemy import Column, Integer, String, Enum
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    gender = Column(Enum("male", "female", "other", name="gender_enum"), nullable=True)
    location = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum("admin", "agent", name="user_roles"), nullable=False, default="agent")

