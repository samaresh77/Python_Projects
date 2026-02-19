from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List

app = FastAPI()

# In-memory database
users = []
user_id_counter = 1


# -----------------------
# Models
# -----------------------

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., gt=0)


class User(UserCreate):
    id: int


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2)
    email: EmailStr | None = None
    age: int | None = Field(default=None, gt=0)


# -----------------------
# Routes
# -----------------------

@app.get("/")
def home():
    return {"message": "User API running 🚀"}


# ✅ CREATE USER (Prevent duplicate email)
@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    global user_id_counter

    # Check duplicate email
    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    new_user = user.dict()
    new_user["id"] = user_id_counter

    users.append(new_user)
    user_id_counter += 1

    return new_user


# ✅ GET ALL USERS (Return count)
@app.get("/users")
def get_users():
    return {
        "total_users": len(users),
        "data": users
    }


# ✅ GET SINGLE USER
@app.get("/users/{user_id}", response_model=User)
def get_single_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


# ✅ UPDATE USER
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_data: UserUpdate):

    for user in users:
        if user["id"] == user_id:

            # Prevent duplicate email (if updating email)
            if updated_data.email:
                for existing_user in users:
                    if (
                        existing_user["email"] == updated_data.email
                        and existing_user["id"] != user_id
                    ):
                        raise HTTPException(
                            status_code=400,
                            detail="Email already exists"
                        )

            # Update only provided fields
            update_dict = updated_data.dict(exclude_unset=True)

            for key, value in update_dict.items():
                user[key] = value

            return user

    raise HTTPException(status_code=404, detail="User not found")


# ✅ DELETE USER
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"message": "User deleted successfully"}

    raise HTTPException(status_code=404, detail="User not found")