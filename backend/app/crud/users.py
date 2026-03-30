from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db: Session, data: UserCreate) -> User:

    hashed = hash_password(data.password)
    user = User(
        name=data.name,
        email=data.email,
        password=hashed,
        role=data.role
    )
    db.add(user)     
    db.commit()     
    db.refresh(user)  
    return user

def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 10):

    return db.query(User).offset(skip).limit(limit).all()