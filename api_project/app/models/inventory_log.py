from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, func
from app.database import Base
from sqlalchemy.orm import relationship

class InventoryLog(Base):
    __tablename__ = "inventory_logs"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    change = Column(Float, nullable=False)
    reason = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())


    product = relationship("Product", back_populates="inventory_logs")  
