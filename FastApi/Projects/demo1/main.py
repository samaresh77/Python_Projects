from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List

app = FastAPI()

# In-memory database
users = []
user_id_counter = 1


# Request Model
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., gt=0)


# Response Model
class User(UserCreate):
    id: int


@app.get("/")
def home():
    return {"message": "User API running 🚀"}


@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    global user_id_counter

    new_user = user.dict()
    new_user["id"] = user_id_counter
    users.append(new_user)

    user_id_counter += 1
    return new_user


@app.get("/users", response_model=List[User])
def get_users():
    return users


@app.get("/users/{user_id}", response_model=User)
def get_single_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"message": "User deleted successfully"}

    raise HTTPException(status_code=404, detail="User not found")