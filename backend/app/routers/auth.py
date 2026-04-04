from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.core.security import verify_password, create_access_token, hash_password
from app.schemas.token import Token, LoginRequest
from app.schemas.user import UserCreate
from app.crud.users import get_user_by_email
from app.models.users import User


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=Token) 
def login(
    payload: LoginRequest,
    response: Response,
    db: Session = Depends(get_db),
):
    user = get_user_by_email(db, email=payload.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")


    if not verify_password(payload.password, str(user.password)):
        raise HTTPException(status_code=401, detail="Invalid email or password")


    token = create_access_token(
        data={"user_id": user.id, "name": user.name, "role": user.role}
    )
    response.set_cookie(key="access_token", value=token, httponly=True)
    return Token(access_token=token)

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logged out successfully"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(
    data: UserCreate,
    db: Session = Depends(get_db),

):
    user = db.query(User).filter(User.email == data.email).first()

    if user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(data.password)
    new_user = User(
        name=data.name,
        email=data.email,
        password=hashed_password,
        role=data.role,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Created Success"}
    
    