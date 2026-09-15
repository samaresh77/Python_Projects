#Response Models

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=18, le=100)
    password: str = Field(min_length=6)

class UserResponse(BaseModel):
    name: str
    age: int


@app.post("/users", response_model=UserResponse) #response_model -> Accept UserCreate as the request, but make sure the response follows UserResponse.
def create_user(user: UserCreate):
    return user

    #          REQUEST
    #             ↓
    #     UserCreate schema
    #     name / age / password
    #             ↓
    #       create_user()
    #             ↓
    #    UserResponse schema
    #        name / age
    #             ↓
    #         RESPONSE


# UserCreate
#     ↓
# What client is ALLOWED to send

# UserResponse
#     ↓
# What client is ALLOWED to receive