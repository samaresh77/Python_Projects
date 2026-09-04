from users import add_user, view_users, search_user

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
