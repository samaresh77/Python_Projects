from users import add_user, view_users, search_user


def main():
    while True:
        print(
            "\n1. Add User\n"
            "2. View Users\n"
            "3. Search User\n"
            "4. Exit"
        )

        try:
            option = int(input("Choose option from 1 to 4: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            try:
                add_user()
            except ValueError as error:
                print("Error:", error)

        elif option == 2:
            view_users()

        elif option == 3:
            try:
                search_user()
            except ValueError as error:
                print("Error:", error)

        elif option == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()