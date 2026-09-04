users = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30}
]

def get_users():
    return users

def find_user(name):
    for user in users:
        if name.lower() == user["name"].lower():
            return user

    return None