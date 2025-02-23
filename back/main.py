import uvicorn
from fastapi import FastAPI
from utils.variable_environment import VarEnv
from DataBaseManager.models import Users, Groups, Tasks
from models import UserAuth, UserLogin
import sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from DataBaseManager import db
from fastapi.responses import JSONResponse
from utils.logger import Logger

app = FastAPI()

@app.post("/register", response_class=JSONResponse)
async def registerUser(item: UserAuth):
    if db.select(sqlalchemy.select(Users).where(Users.login==item.login)):
        result = False
        msg = "A user with this login already exists"
    elif not item.login or not item.password:
        result = False
        msg = "Login and password fields cannot be empty"
    else:
        result = True
        msg = "Ok"
        db.execute_commit(sqlalchemy.insert(Users).values(login=item.login, password=item.password))
    return JSONResponse(content={"result": result, "msg": msg}, status_code=200)

@app.post("/login", response_class=JSONResponse)
async def authenticate(item: UserLogin):
    if not item.login or not item.password:
        result = False
        msg = "Login and password fields cannot be empty"
    elif not db.select(sqlalchemy.select(Users).where(Users.login==item.login, Users.password==item.password)):
        result = False
        msg = "The login or password entered is incorrect"
    else:
        result = True
        msg = "Ok"
    return JSONResponse(content={"result": result, "msg": msg}, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)