from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=False)

    owner = relationship(argument="User", back_populates="projects")
    tasks = relationship(argument="Task", back_populates="project", cascade="all, delete")