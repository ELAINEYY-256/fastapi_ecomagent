from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    contact_info = Column(String, nullable=False)
    region = Column(String, nullable=True)
    performance_score = Column(Float, default=0.0)

    user = relationship("User", backref="agent_profile")
    leads = relationship("Lead", back_populates="assigned_agent")
    clients = relationship("Client", back_populates="agent")
    orders = relationship("Order", back_populates="agent")


