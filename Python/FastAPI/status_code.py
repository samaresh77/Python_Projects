# HTTP Status Codes

# | Code  | Meaning          | Typical API usage             |
# | ----- | ---------------- | ----------------------------- |
# | `200` | OK               | Successful GET                |
# | `201` | Created          | Successful POST               |
# | `204` | No Content       | Successful DELETE             |
# | `400` | Bad Request      | Invalid request               |
# | `401` | Unauthorized     | Not authenticated             |
# | `403` | Forbidden        | Authenticated but not allowed |
# | `404` | Not Found        | Resource doesn't exist        |
# | `409` | Conflict         | Duplicate resource            |
# | `422` | Validation Error | Pydantic/FastAPI validation   |
# | `500` | Server Error     | Unexpected backend error      |

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=18, le=100)
    password: str = Field(min_length=6)

class UserUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=18, le=100)

class UserResponse(BaseModel):
    name: str
    age: int


users = []

#Create
@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate):  
    
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "age": user.age
    }

    users.append(new_user)

    return new_user

#Read all
@app.get("/users", response_model=list[UserResponse])
def get_users():
    return users

#read one data
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):      

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

#update
@app.put(
    "/users/{user_id}",
    response_model=UserResponse
)
def update_user(user_id: int, user_data: UserUpdate):

    for user in users:

        if user["id"] == user_id:

            user["name"] = user_data.name
            user["age"] = user_data.age

            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

#delete
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            users.remove(user)

            return {
                "message": "User deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )