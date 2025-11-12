from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    agent_id = Column(Integer, ForeignKey("agents.id", ondelete="SET NULL"))
    lead_id = Column(Integer, ForeignKey("leads.id", ondelete="SET NULL"))

    agent = relationship("Agent", back_populates="clients")
    lead = relationship("Lead", back_populates="client")
    orders = relationship("Order", back_populates="client")


