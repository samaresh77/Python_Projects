import json


def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


users = load_users()


def add_user():
    name = input("Enter name to add: ")

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    try:
        age = int(input("Enter age: "))
    except ValueError:
        raise ValueError("Age must be a number.")

    if age <= 0:
        raise ValueError("Age must be greater than 0.")

    user = {
        "name": name,
        "age": age
    }

    users.append(user)

    save_users(users)

    print("User added successfully.")


def view_users():
    if not users:
        print("No users found.")
        return

    for user in users:
        print(f"Name: {user['name']}, Age: {user['age']}")


def search_user():
    name = input("Enter name to search: ")

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    for user in users:
        if user["name"].lower() == name.lower():
            print("User found")
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")
            return

    print("User not found.")