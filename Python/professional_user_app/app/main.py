from app.enums import UserRole
from app.services import (
    add_user,
    delete_user,
    find_user,
    load_users,
)


def main() -> None:
    users = load_users()

    while True:
        print("\n===== User Management System =====")
        print("1. Add user")
        print("2. View users")
        print("3. Search user")
        print("4. Delete user")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Name: ").strip()
                age = int(input("Age: "))

                print("Roles: admin, user, manager")
                role = UserRole(
                    input("Role: ").strip().lower()
                )

                user = add_user(
                    users,
                    name,
                    age,
                    role
                )

                print(
                    f"User created: "
                    f"{user.id} - {user.name}"
                )

            elif choice == "2":
                if not users:
                    print("No users found.")
                    continue

                for user in users:
                    print(
                        f"ID: {user.id} | "
                        f"Name: {user.name} | "
                        f"Age: {user.age} | "
                        f"Role: {user.role.value}"
                    )

            elif choice == "3":
                user_id = int(input("User ID: "))

                user = find_user(users, user_id)

                if user:
                    print(
                        f"ID: {user.id} | "
                        f"Name: {user.name} | "
                        f"Age: {user.age} | "
                        f"Role: {user.role.value}"
                    )
                else:
                    print("User not found.")

            elif choice == "4":
                user_id = int(input("User ID: "))

                if delete_user(users, user_id):
                    print("User deleted successfully.")
                else:
                    print("User not found.")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()