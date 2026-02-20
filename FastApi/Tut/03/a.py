from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary storage (in memory)
registered_user_name = None


class UserRegistration(BaseModel):
    name: str
    email: str
    password: str


@app.post("/register")
def register_user(user: UserRegistration):
    global registered_user_name
    registered_user_name = user.name
    
    return {
        "message": f"{user.name} registered successfully"
    }


@app.get("/welcome")
def welcome_user():
    if registered_user_name:
        return {"message": f"Welcome {registered_user_name} 🎉"}
    return {"message": "No user registered yet"}