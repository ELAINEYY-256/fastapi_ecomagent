from sqlalchemy.orm import Session
from app.database import SessionLocal
from fastapi import HTTPException
from app.models.lead import Lead, LeadStatus


class LeadService:

    @staticmethod
    def create_lead(data):
        db: Session = SessionLocal()
        try:
            lead = Lead(
                name=data.name,
                contact_info=data.contact_info,
                source=data.source,
                interest_level=data.interest_level,
                notes=data.notes,
                assigned_agent_id=data.assigned_agent_id
            )
            db.add(lead)
            db.commit()
            db.refresh(lead)
            return lead
        finally:
            db.close()

    @staticmethod
    def get_all_leads():
        db = SessionLocal()
        try:
            return db.query(Lead).all()
        finally:
            db.close()

    @staticmethod
    def qualify_lead(lead_id: int):
        db = SessionLocal()
        try:
            lead = db.query(Lead).filter(Lead.id == lead_id).first()
            if not lead:
                raise HTTPException(status_code=404, detail="Lead not found")

            lead.status = LeadStatus.qualified
            db.commit()
            db.refresh(lead)
            return lead
        finally:
            db.close()
