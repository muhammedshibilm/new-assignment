from sqlalchemy import Column, ForeignKey, Integer, String , DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, nullable=False, default="pending")
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    due_date = Column(DateTime)

    project = relationship(argument="Project", back_populates="tasks")
    assignee = relationship(argument="User", back_populates="tasks")