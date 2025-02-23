import uvicorn
from fastapi import FastAPI, Depends, Request, Response

from back.auntefication import SessionData, get_session_data, create_session_user, backend,cookie
from utils.variable_environment import VarEnv
from DataBaseManager.models import Users, Groups, Tasks
from models import UserAuth, UserLogin
import sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from DataBaseManager import db
from fastapi.responses import JSONResponse
from utils.logger import Logger
from uuid import UUID, uuid4


app = FastAPI()


@app.post("/register", response_class=JSONResponse)
async def registerUser(item: UserAuth, response: Response):
    if db.select(sqlalchemy.select(Users).where(Users.login == item.login)):
        result = False
        msg = "A user with this login already exists"
    elif not item.login or not item.password:
        result = False
        msg = "Login and password fields cannot be empty"
    else:
        result = True
        msg = "Ok"
        db.execute_commit(sqlalchemy.insert(Users).values(login=item.login, password=item.password))
        user = db.select(sqlalchemy.select(Users).where(Users.login == item.login), db.any)
        await create_session_user(response, id=user.id, login=item.login)
    return JSONResponse(content={"result": result, "msg": msg}, status_code=200)


@app.post("/login", response_class=JSONResponse)
async def authenticate(item: UserLogin, response: Response):
    result = True
    if not item.login or not item.password:
        return JSONResponse(content={"result": False, "msg": "Login and password fields cannot be empty"},
                            status_code=200)
    user = db.select(
        sqlalchemy.select(Users).where(sqlalchemy.and_(Users.login == item.login, Users.password == item.password)), db.any_)
    if not user:
        result = False
        msg = "The login or password entered is incorrect"
    else:
        msg = "Ok"
        session = uuid4()
        data = SessionData(id=user.id, login=item.login)
        await backend.create(session, data)
        cookie.attach_to_response(response, session)
        print("dldkdkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        # await create_session_user(response, id=user.id, login=item.login)
    return JSONResponse(content={"result": result, "msg": msg}, status_code=200)


@app.get("/", response_class=JSONResponse)
async def index(session_data: SessionData = Depends(get_session_data)):
    # навешивание этих аргументов уже значит проверку
    return session_data.dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
