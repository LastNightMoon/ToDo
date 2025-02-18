import uvicorn
from fastapi import FastAPI
from utils.variable_environment import VarEnv
from DataBaseManager.models import Users, Groups, Tasks
import sqlalchemy
from DataBaseManager import db

app = FastAPI()


if __name__ == "__main__":
    db.execute_commit(sqlalchemy.insert(Users).values(login ='Roman', password='1234'))
    uvicorn.run(app, host="0.0.0.0", port=8000)