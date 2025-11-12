from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class LeadStatus(str, enum.Enum):
    new = "new"
    contacted = "contacted"
    qualified = "qualified"
    disqualified = "disqualified"

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    source = Column(String, nullable=True)
    interest_level = Column(String, nullable=True)
    status = Column(Enum(LeadStatus), default=LeadStatus.new)
    notes = Column(Text, nullable=True)
    assigned_agent_id = Column(Integer, ForeignKey("agents.id", ondelete="SET NULL"))

    assigned_agent = relationship("Agent", back_populates="leads")
    client = relationship("Client", back_populates="lead", uselist=False)


