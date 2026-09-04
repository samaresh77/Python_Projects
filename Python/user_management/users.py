users = []


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
    print("User added!")


def view_users():
    if not users:
        print("No users found")
    else:
        for user in users:
            print(f"Name: {user['name']}, Age: {user['age']}")


def search_user():
    name = input("Enter name to search: ")

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    found = False

    for user in users:
        if user["name"].lower() == name.lower():
            print("User found")
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")

            found = True
            break

    if not found:
        print("User not found")