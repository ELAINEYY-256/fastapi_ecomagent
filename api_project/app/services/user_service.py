from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password, verify_password, create_access_token


class UserService:

    @staticmethod
    def register_user(name: str, email: str, password: str, role: str):
        db: Session = SessionLocal()

        try:
            # Check if user exists
            if db.query(User).filter(User.email == email).first():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email already exists."
                )

            user = User(
                name=name,
                email=email,
                password_hash=hash_password(password),
                role=role
            )

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

            token = create_access_token({"sub": user.email})
            return {"access_token": token, "token_type": "bearer"}

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

        finally:
            db.close()
