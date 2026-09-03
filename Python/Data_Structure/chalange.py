# 1
users = [
    {
        "name": "John",
        "age": 25,
        "role": "admin"
    },
    {
        "name": "Alice",
        "age": 17,
        "role": "employee"
    },
    {
        "name": "Bob",
        "age": 30,
        "role": "manager"
    }
]

for user in users:
    if user["age"] >= 18:
        print(user["name"])

# 2
find_user = input("Enter name to find: ")

found = False

for user in users:
    if find_user == user["name"]:
        print("User found")
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")
        print(f"Role: {user['role']}")

        found = True
        break

if not found:
    print("User not found")


# 3
users = []

while True:

    print(
        "\n1. Add User\n"
        "2. View Users\n"
        "3. Search User\n"
        "4. Exit"
    )

    option = int(input("Choose option from 1 to 4: "))

    if option == 1:

        name = input("Enter name to add: ")
        age = int(input("Enter age: "))

        user = {
            "name": name,
            "age": age
        }

        users.append(user)

        print("User added successfully!")

    elif option == 2:

        if len(users) == 0:
            print("No users found")
        else:
            for user in users:
                print(user)

    elif option == 3:

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

    elif option == 4:

        print("Goodbye!")
        break

    else:
        print("Invalid option")