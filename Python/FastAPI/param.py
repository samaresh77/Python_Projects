from fastapi import FastAPI

app = FastAPI()


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

# Path parameter

@app.get('/users')
def get_users():
    return users



# Query Parameters
# /users?age=21

@app.get("/users/filter")
def filter_users(age: int):

    result = []

    for user in users:
        if user["age"] == age:
            result.append(user)

    return result

# @app.get("/users/{user_id}")
# def get_user(user_id: int):

#     for user in users:

#         if user["id"] == user_id:
#             return user

#     return {
#         "message": "User not found"
#     }

@app.get("/users/search")
def search_user(name: str):
    result = []
    for user in users:

        if user["name"].lower() == name.lower():
            result.append(user)

    return result