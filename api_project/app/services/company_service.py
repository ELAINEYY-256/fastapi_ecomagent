from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.database import SessionLocal
from app.models.company import Company

class CompanyService:

    @staticmethod
    def create_company(name: str):
        db: Session = SessionLocal()
        try:
            existing = db.query(Company).filter(Company.name == name).first()
            if existing:
                raise HTTPException(400, "Company already exists")

            company = Company(name=name)
            db.add(company)
            db.commit()
            db.refresh(company)
            return company

        finally:
            db.close()

    @staticmethod
    def list_companies():
        db = SessionLocal()
        try:
            return db.query(Company).all()
        finally:
            db.close()

    @staticmethod
    def get_company(company_id: int):
        db = SessionLocal()
        try:
            company = db.query(Company).filter(Company.id == company_id).first()
            if not company:
                raise HTTPException(404, "Company not found")
            return company
        finally:
            db.close()

    @staticmethod
    def update_company(company_id: int, name: str | None):
        db = SessionLocal()
        try:
            company = db.query(Company).filter(Company.id == company_id).first()
            if not company:
                raise HTTPException(404, "Company not found")

            if name:
                company.name = name

            db.commit()
            db.refresh(company)
            return company

        finally:
            db.close()

    @staticmethod
    def delete_company(company_id: int):
        db = SessionLocal()
        try:
            company = db.query(Company).filter(Company.id == company_id).first()
            if not company:
                raise HTTPException(404, "Company not found")

            db.delete(company)
            db.commit()
            return {"detail": "Company deleted"}

        finally:
            db.close()
