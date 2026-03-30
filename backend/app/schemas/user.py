from pydantic import BaseModel, EmailStr
from typing import Literal

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: Literal["admin", "developer"] = "developer"

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    model_config = {
        "from_attributes": True
    }