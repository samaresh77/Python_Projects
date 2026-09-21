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

@app.get("/users/search")
def search_users(limit: int = 10):
    return {
        "limit": limit
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }

@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User created",
        "user": user
    }

@app.get("/tickets")
def get_tickets():
    return {
        "tickets": [
            {
                "id": 1,
                "title": "Login problem",
                "status": "open"
            },
            {
                "id": 2,
                "title": "Payment issue",
                "status": "resolved"
            }
        ]
    }

@app.get("/tickets/search")
def search_tickets(limit: int = 10):
    return {
        "limit": limit
    }

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    return {
        "ticket_id": ticket_id
    }
