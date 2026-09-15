# Package → fastapi
# Class → FastAPI

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return{
        "message": "Welcome to my FastAPI application"
    }

@app.get('/about')
def hello_about():
    return{
        "application": "User Management API",
        "version": "1.0.0",
        "developer": "Your Name"
    }

@app.get('/health')
def hello_health():
    return{
        "status": "healthy"
    }

users = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 21
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 22
    },
    {
        "id": 3,
        "name": "Amit",
        "age": 25
    }
]

@app.get('/users')
def get_users():
    return users

@app.get("/users/count")
def get_user_count():
    return {
        "count": len(users)
    }
