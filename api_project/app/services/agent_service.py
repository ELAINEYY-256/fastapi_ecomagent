from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.agent import Agent
from app.models.user import User


class AgentService:

    @staticmethod
    def db() -> Session:
        return next(get_db())

    @staticmethod
    def create_agent(data):
        db = AgentService.db()
        try:
            user = db.query(User).filter(User.id == data.user_id).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            if user.role != "agent":
                raise HTTPException(
                    status_code=400,
                    detail="User must have role 'agent' to create an agent profile"
                )

            new_agent = Agent(
                user_id=data.user_id,
                contact_info=data.contact_info,
                region=data.region,
                performance_score=data.performance_score
            )

            db.add(new_agent)
            db.commit()
            db.refresh(new_agent)
            return new_agent

        finally:
            db.close()

    @staticmethod
    def update_agent(agent_id: int, updates):
        db = AgentService.db()
        try:
            agent = db.query(Agent).filter(Agent.id == agent_id).first()
            if not agent:
                raise HTTPException(status_code=404, detail="Agent not found")

            if updates.contact_info is not None:
                agent.contact_info = updates.contact_info
            if updates.region is not None:
                agent.region = updates.region
            if updates.performance_score is not None:
                agent.performance_score = updates.performance_score

            db.commit()
            db.refresh(agent)
            return agent

        finally:
            db.close()

    @staticmethod
    def list_agents():
        db = AgentService.db()
        try:
            return db.query(Agent).all()
        finally:
            db.close()

    @staticmethod
    def get_agent(agent_id: int):
        db = AgentService.db()
        try:
            agent = db.query(Agent).filter(Agent.id == agent_id).first()
            if not agent:
                raise HTTPException(status_code=404, detail="Agent not found")
            return agent
        finally:
            db.close()

    @staticmethod
    def delete_agent(agent_id: int):
        db = AgentService.db()
        try:
            agent = db.query(Agent).filter(Agent.id == agent_id).first()
            if not agent:
                raise HTTPException(status_code=404, detail="Agent not found")

            db.delete(agent)
            db.commit()
            return {"message": "Agent deleted successfully"}

        finally:
            db.close()
