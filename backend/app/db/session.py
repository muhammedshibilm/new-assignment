import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")


#Engine Creation
engine = create_engine(DATABASE_URL ,echo=True) 


#Session Creation
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

#Base Class Creation
class Base(DeclarativeBase):
    pass