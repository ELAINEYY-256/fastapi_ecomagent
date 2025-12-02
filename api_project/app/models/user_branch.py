from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UserBranch(Base):
    __tablename__ = "user_branches"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    branch_id = Column(Integer, ForeignKey("branches.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="branches")
    branch = relationship("Branch", back_populates="users")
