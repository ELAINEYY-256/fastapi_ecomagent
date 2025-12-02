from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.company import Company
from app.models.branch import Branch
from app.models.user import User
from app.database import SessionLocal
from app.utils.security import hash_password, create_access_token


class OnboardingService:

    @staticmethod
    def signup_company(data):
        db: Session = SessionLocal()

        try:
            existing_company = db.query(Company).filter(Company.name == data.company_name).first()
            if existing_company:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Company already exists"
                )

            company = Company(name=data.company_name)
            db.add(company)
            db.commit()
            db.refresh(company)

            head_branch = Branch(
                name=f"{company.name} Head Office",
                company_id=company.id,
                country=None,
                state=None,
                region=None,
                physical_address=None,
                is_head_branch=True
            )

            db.add(head_branch)
            db.commit()
            db.refresh(head_branch)

        
            hashed_pw = hash_password(data.password)

            user = User(
                first_name=data.first_name,
                last_name=data.last_name,
                email=data.email,
                password_hash=hashed_pw,
                company_id=company.id,
                branch_id=head_branch.id,
                role="superuser",
                is_superuser=True
            )

            db.add(user)
            db.commit()
            db.refresh(user)

        
            token = create_access_token({
                "sub": user.email,
                "user_id": user.id,
                "company_id": company.id,
                "role": user.role
            })

            return {
                "company_id": company.id,
                "user_id": user.id,
                "email": user.email,
                "role": user.role,
                "token": token
            }

        finally:
            db.close()
