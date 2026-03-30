from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Literal["pending", "in_progress", "completed"] = "pending"
    project_id: int
    assigned_to: Optional[int] = None
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["pending", "in_progress", "completed"]] = None
    assigned_to: Optional[int] = None
    due_date: Optional[datetime] = None

class TaskRead(TaskBase):
    id: int

    model_config = {
        "from_attributes": True
    }