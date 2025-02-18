from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pydantic import BaseModel
from utils.variable_environment import VarEnv
from DataBaseManager.models import Users, Groups, Tasks

class DataBaseManager():
    def __init__(self, db_url=f'postgresql+psycopg2://{VarEnv.DBUSER}:{VarEnv.DBPASSWORD}@{VarEnv.DBHOST}/{VarEnv.DBNAME}'):
        """
        Инициализация подключения к БД:
        - db_url: строка подключения (например, 'sqlite:///mydatabase.db')
        """
        self.engine = create_engine(db_url, echo=True)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def execute_commit(self, command):
        with self.engine.connect() as session:
            session.execute(command)
            session.commit()
            session.close()
        
    def select(self, command, types='all'):
        with self.engine.connect() as session:
            if (types == 'all'):
                data = session.execute(command).fetchall()
            else:
                data = session.execute(command).fetchone()
            session.close()
            return data

db = DataBaseManager()

