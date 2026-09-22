from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.db import Base, engine, get_db
from database.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    name: str
    email: str

@app.get("/")
def home():
    return {
        "message": "Welcome to HelpDesk API"
    }

@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return users

@app.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

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
