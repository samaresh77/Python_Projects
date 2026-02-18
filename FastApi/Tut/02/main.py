from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello/{name}")
def greeting(name: str):
    return {"Welcome!": name}


@app.get("/multiply")
def multiply(num1: int = 10, num2: int = 10):
    return {"Multiplication": num1 * num2}


# 👇 Create model for request body
class LoginRequest(BaseModel):
    name: str
    email: str


@app.post("/login")
def create_login(data: LoginRequest):
    return {
        "name": data.name,
        "email": data.email
    }