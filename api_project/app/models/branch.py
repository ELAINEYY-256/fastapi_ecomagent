from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    
    name = Column(String, nullable=False)
    country = Column(String, nullable=True)
    state = Column(String, nullable=True)
    region = Column(String, nullable=True)
    physical_address = Column(String, nullable=True)
    is_head_branch = Column(Boolean, default=False)

    company = relationship("Company", back_populates="branches")
  


