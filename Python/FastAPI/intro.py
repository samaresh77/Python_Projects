# What is FastAPI?
# FastAPI is a Python web framework for building APIs.

from fastapi import FastAPI  #Imports the FastAPI class.

app = FastAPI()  #This creates your FastAPI application.


@app.get("/hello")  #Create GET endpoint

def hello():        #This function handles the request.
    return {        #response -> FastAPI converts the Python dictionary into JSON.
        "message": "Hello World"
    }

# Express                    FastAPI
# ────────────────────────────────────
# app.get()                  @app.get()
# req                        function parameters
# res.json()                 return {}
# express()                  FastAPI()
# Node.js                    Python

# FastAPI has several useful features built into the framework.
# 1. Type hints
# 2. Automatic validation With Pydantic
# 3. Automatic API documentation (/docs)
# 4. High performance(async, await)

# FastAPI Architecture
            #      Client
            #        │
            #        │ HTTP Request
            #        ▼
            #  ┌───────────┐
            #  │  FastAPI  │
            #  └─────┬─────┘
            #        │
            #        ▼
            #  Router/Endpoint
            #        │
            #        ▼
            #  Pydantic Validation
            #        │
            #        ▼
            #   Business Logic
            #        │
            #        ▼
            #    Database
            #        │
            #        ▼
            #  Response JSON
            #        │
            #        ▼
            #      Client

# HTTP Methods
# | Method | Purpose               |
# | ------ | --------------------- |
# | GET    | Read data             |
# | POST   | Create data           |
# | PUT    | Replace/update data   |
# | PATCH  | Partially update data |
# | DELETE | Delete data           |

# What is an Endpoint?
# GET /users (together called endpoint)
# GET
#  ↓
# HTTP method

# /users
#  ↓
# Path

@app.get("/")
def home():
    return {"message": "Hello World"}

#this part uses decorators
# when client call get or hit api then fastapi call home()

# The Big Picture

# Python
#   │
#   ├── Functions
#   ├── Type hints
#   ├── Exceptions
#   ├── OOP
#   ├── Modules
#   └── Decorators
#           │
#           ▼
#       Pydantic
#           │
#           ├── Validation
#           ├── Nested models
#           ├── Serialization
#           └── Settings
#                   │
#                   ▼
#                FastAPI
#                   │
#                   ├── HTTP
#                   ├── Routes
#                   ├── Requests
#                   ├── Responses
#                   └── APIs
#                          │
#                          ▼
#                      PostgreSQL
