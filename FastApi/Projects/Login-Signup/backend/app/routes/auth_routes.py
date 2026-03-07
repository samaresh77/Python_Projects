from fastapi import APIRouter, HTTPException
from database import users_collection
from schemas.user_schema import UserSignup
from utils.auth_utils import hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: UserSignup):

    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)

    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }

    users_collection.insert_one(new_user)

    return {"message": "User created successfully"}