users = []

def add_user():
    name = input("Enter name to add: ")
    age = int(input("Enter age: "))
    user = {
        'name': name,
        'age': age
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