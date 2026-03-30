from sqlalchemy.orm import Session
from app.models import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

def create_project(db: Session, data: ProjectCreate, user_id: int) -> Project:
    project = Project(
        name=data.name,
        description=data.description,
        created_by=user_id 
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project_by_id(db: Session, project_id: int) -> Project:
    return db.query(Project).filter(Project.id == project_id).first()

def get_all_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Project).offset(skip).limit(limit).all()

def update_project(db: Session, project: Project, data: ProjectUpdate) -> Project:

    if data.name is not None:
        project.name = data.name
    if data.description is not None:
        project.description = data.description
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project: Project):
    db.delete(project)
    db.commit()