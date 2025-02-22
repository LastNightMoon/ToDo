import uvicorn
from fastapi import FastAPI
from utils.variable_environment import VarEnv
from DataBaseManager.models import Users, Groups, Tasks
import sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from DataBaseManager import db

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)