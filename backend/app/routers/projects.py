from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.crud.projects import create_project, get_all_projects, get_project_by_id, update_project, delete_project
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectRead
from typing import List

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectRead, status_code=201)
def create(
    data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_project(db, data, user_id=current_user.id)

@router.get("/", response_model=List[ProjectRead])
def list_all(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_all_projects(db, skip=skip, limit=limit)

@router.get("/{project_id}", response_model=ProjectRead)
def get_one(
    project_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    project = get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=ProjectRead)
def update(
    project_id: int,
    data: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    project = get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return update_project(db, project, data)

@router.delete("/{project_id}", status_code=204)
def delete(
    project_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    project = get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    delete_project(db, project)