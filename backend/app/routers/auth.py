from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.core.security import verify_password, create_access_token
from app.schemas.token import Token
from app.crud.users import get_user_by_email

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),  
    db: Session = Depends(get_db)
):

    user = get_user_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")


    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")


    token = create_access_token(data={"user_id": user.id, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}