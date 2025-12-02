from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    gender = Column(Enum("male", "female", "other", name="gender_enum"), nullable=True)
    location = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum("superuser", "admin", "agent", name="user_roles"), nullable=False, default="agent")
    is_superuser = Column(Boolean, default=False)

    branches = relationship("UserBranch", back_populates="user")
    company = relationship("Company", back_populates="users")

  



