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
        print("User not found")
    else:
        for u in users:
            print(u["name"])


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


def main():
    while True:
        # menu
        print(
            "\n1. Add User\n"
            "2. View Users\n"
            "3. Search User\n"
            "4. Exit"
        )
        option = int(input("Choose option from 1 to 4: "))
        if option == 1:
            add_user()

        elif option == 2:
            view_users()

        elif option == 3:
            search_user()

        elif option == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
