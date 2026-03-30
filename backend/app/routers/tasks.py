from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.crud.tasks import create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from app.schemas.task import TaskCreate, TaskUpdate, TaskRead
from typing import List, Optional

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskRead, status_code=201)
def create(
    data: TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_task(db, data)

@router.get("/", response_model=List[TaskRead])
def list_all(
    skip: int = 0,
    limit: int = 10,
    project_id: Optional[int] = None,   # ?project_id=1
    status: Optional[str] = None,        # ?status=pending
    assigned_to: Optional[int] = None,   # ?assigned_to=2
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_all_tasks(db, skip, limit, project_id, status, assigned_to)

@router.get("/{task_id}", response_model=TaskRead)
def get_one(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskRead)
def update(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task(db, task, data)

@router.delete("/{task_id}", status_code=204)
def delete(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(db, task)