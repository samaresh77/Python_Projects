from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Hello Samaresh 🚀"}

#Path Parameters
@app.get("/users/{user_id}")
def get_users(user_id: int):
    return { "user_id": user_id }

#Query Parameters
@app.get("/search")
def search_user(name: str, age: int=18):
    return {"name": name, "age": age}

#Post request
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }