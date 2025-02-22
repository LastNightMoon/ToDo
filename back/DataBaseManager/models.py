from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pydantic import BaseModel
from datetime import date
    
Base = declarative_base()
    
class Users(Base):
    __tablename__ = 'Users' 
    id: int = Column(Integer, primary_key=True)
    login: str = Column(String)
    password: str = Column(String)
    
class Groups(Base):
    __tablename__ = 'Groups'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    user_id: int = Column(Integer)


class Tasks(Base):
    __tablename__ = 'Tasks'
    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer)
    name: str = Column(String)
    group_id: int = Column(Integer) 
    create_date: date = Column(Date)
    closed: bool = Column(Boolean)
    closed_date: date = Column(Date)
    