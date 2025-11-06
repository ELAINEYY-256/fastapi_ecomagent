from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import hash_password, verify_password, create_access_token

def create_user(db: Session, name: str, email: str, password: str, role: str):
    hashed_pw = hash_password(password)
    user = User(name=name, email=email, password_hash=hashed_pw, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user
