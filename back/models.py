from pydantic import BaseModel
from datetime import date

class UserAuth(BaseModel):
    login: str
    password: str

class UserLogin(BaseModel):
    login: str
    password: str
    
class CreateTasks(BaseModel):
    user_id: int
    name: str
    group_id: int
    create_date: date
    closed: bool
    closed_date: date