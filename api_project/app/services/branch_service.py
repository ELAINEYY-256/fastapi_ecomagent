from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database import SessionLocal
from app.models.branch import Branch
from app.models.company import Company

class BranchService:

    @staticmethod
    def create_branch(data):
        db: Session = SessionLocal()
        try:
            company = db.query(Company).filter(Company.id == data.company_id).first()
            if not company:
                raise HTTPException(404, "Company not found")

            branch = Branch(
                company_id=data.company_id,
                name=data.name,
                location=data.location,
                is_head_branch=data.is_head_branch,
                country=data.country,
                state=data.state,
                region=data.region,
                physical_address=data.physical_address
            )
            db.add(branch)
            db.commit()
            db.refresh(branch)
            return branch

        finally:
            db.close()

    @staticmethod
    def list_branches():
        db = SessionLocal()
        try:
            return db.query(Branch).all()
        finally:
            db.close()

    @staticmethod
    def get_branch(branch_id: int):
        db = SessionLocal()
        try:
            branch = db.query(Branch).filter(Branch.id == branch_id).first()
            if not branch:
                raise HTTPException(404, "Branch not found")
            return branch
        finally:
            db.close()

    @staticmethod
    def update_branch(branch_id: int, updates):
        db = SessionLocal()
        try:
            branch = db.query(Branch).filter(Branch.id == branch_id).first()
            if not branch:
                raise HTTPException(404, "Branch not found")

            for key, value in updates.model_dump(exclude_unset=True).items():
                setattr(branch, key, value)

            db.commit()
            db.refresh(branch)
            return branch
        finally:
            db.close()

    @staticmethod
    def delete_branch(branch_id: int):
        db = SessionLocal()
        try:
            branch = db.query(Branch).filter(Branch.id == branch_id).first()
            if not branch:
                raise HTTPException(404, "Branch not found")

            db.delete(branch)
            db.commit()
            return {"detail": "Branch deleted"}

        finally:
            db.close()
