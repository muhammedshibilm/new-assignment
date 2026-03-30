from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app import crud, models
from app.schemas.user import UserCreate, UserRead
from typing import List



router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=201)
def register_user(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    # check email already exists
    existing = crud.users.get_user_by_email(db, email=data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.users.create_user(db, data)

@router.get("/", response_model=List[UserRead])
def list_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # must be logged in
):
    return crud.users.get_all_users(db, skip=skip, limit=limit)
