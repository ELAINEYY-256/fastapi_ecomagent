from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException, status


class UserService:

    @staticmethod
    def register_user(name: str, email: str, password: str, role: str):
        db: Session = SessionLocal()
        try:
            existing_user = db.query(User).filter(User.email == email).first()
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email already exists."
                )

            hashed_pw = hash_password(password)
            user = User(
                name=name,
                email=email,
                password_hash=hashed_pw,
                role=role
            )

            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        
        

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

        finally:
            db.close()
