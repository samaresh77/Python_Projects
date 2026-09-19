from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: str


@app.get("/")
def home():
    return {
        "message": "Welcome to HelpDesk API"
    }


@app.get("/users")
def get_users():
    return {
        "users": [
            {
                "id": 1,
                "name": "Rahul"
            },
            {
                "id": 2,
                "name": "Amit"
            }
        ]
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


@app.get("/users/search")
def search_users(limit: int = 10):
    return {
        "limit": limit
    }


@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User created",
        "user": user
    }