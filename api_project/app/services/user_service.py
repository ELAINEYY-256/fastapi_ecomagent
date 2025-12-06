from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.database import SessionLocal
from app.models.user import User
from app.models.company import Company
from app.utils.security import hash_password, verify_password, create_access_token


class UserService:
    
    @staticmethod
    def get_company_by_name (name: str):
        db: Session = SessionLocal()
        return db.query(Company).filter(Company.name == name).first()
    
    @staticmethod
    def create_company(company: Company):
        try:
            db: Session = SessionLocal()
            db.add(company)
            db.commit()
            db.refresh(company)
            return company
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
        finally:
            db.close()
    
    @staticmethod
    def get_user_by_email(email: str):
        db: Session = SessionLocal()
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_id(user_id: int):
        db: Session = SessionLocal()
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_users_by_company_id(company_id: int):
        db: Session = SessionLocal()
        return db.query(User).filter(User.company_id == company_id).all()
    
    @staticmethod
    def get_users_by_branch_id(branch_id: int):
        db: Session = SessionLocal()
        return db.query(User).filter(User.branch_id == branch_id).all()
    
    
    @staticmethod
    def create_user(user: User):
        db: Session = SessionLocal()
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
        finally:
            db.close()

    @staticmethod
    def login_user(email: str, password: str):
        db: Session = SessionLocal()

        try:
            user = db.query(User).filter(User.email == email).first()

            if not user or not verify_password(password, user.password_hash):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid email or password"
                )
            
            token_payload = {
                "sub": user.email,
                "user_id": user.id,
                "company_id": user.company_id,
                "role": user.role,
            }

            token = create_access_token(token_payload)
            return {"access_token": token, "token_type": "bearer"}

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

        finally:
            db.close()



          