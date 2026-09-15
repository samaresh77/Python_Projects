#Pydantic + FastAPI Validation

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=18, le=100)

@app.post("/users")
def create_user(user: User):

    return {
        "message": "User created successfully",
        "user": user
    }
