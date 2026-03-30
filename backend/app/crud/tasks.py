from sqlalchemy.orm import Session
from app.models import Task
from app.schemas.task import TaskCreate, TaskUpdate
from typing import Optional

def create_task(db: Session, data: TaskCreate) -> Task:
    task = Task(
        title=data.title,
        description=data.description,
        status=data.status,
        project_id=data.project_id,
        assigned_to=data.assigned_to,
        due_date=data.due_date
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(db: Session, task_id: int) -> Task:
    return db.query(Task).filter(Task.id == task_id).first()

def get_all_tasks(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    project_id: Optional[int] = None,  
    status: Optional[str] = None,       
    assigned_to: Optional[int] = None   
):
    query = db.query(Task)

    # apply filters only if they were provided
    if project_id is not None:
        query = query.filter(Task.project_id == project_id)
    if status is not None:
        query = query.filter(Task.status == status)
    if assigned_to is not None:
        query = query.filter(Task.assigned_to == assigned_to)

    return query.offset(skip).limit(limit).all()

def update_task(db: Session, task: Task, data: TaskUpdate) -> Task:
    # only update fields that were actually sent
    if data.title is not None:
        task.title = data.title
    if data.description is not None:
        task.description = data.description
    if data.status is not None:
        task.status = data.status
    if data.assigned_to is not None:
        task.assigned_to = data.assigned_to
    if data.due_date is not None:
        task.due_date = data.due_date
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
