from sqlalchemy import Column , Integer , String ,DateTime
from sqlalchemy.orm import relationship
from db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False , index=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="developer")

    tasks = relationship(argument="Task", back_populates="assignee")
    projects = relationship(argument="Project", back_populates="owner")