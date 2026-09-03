# number guessing
secret_number = 7
guess = 0

while secret_number != guess:
    guess = int(input("Enter your guess: "))
    if secret_number == guess:
        print("You guessed correctly!")
    else:
        print("Try again")


# find users active and 18 years or older
users = [
    {
        "name": "John",
        "age": 25,
        "active": True
    },
    {
        "name": "Alice",
        "age": 17,
        "active": True
    },
    {
        "name": "Bob",
        "age": 30,
        "active": False
    },
    {
        "name": "David",
        "age": 22,
        "active": True
    }
]

for user in users:
    if user["active"] and user["age"] >= 18:
        print(user["name"])


# Mini ATM
balance = 5000

while True:
    print(
        "\nChoose an option below:"
        "\n1. Check Balance"
        "\n2. Deposit"
        "\n3. Withdraw"
        "\n4. Exit"
    )

    option = int(input("Enter an option: "))

    if option == 1:
        print(f"Your balance is: {balance}")

    elif option == 2:
        deposit_amount = int(input("Enter amount to deposit: "))

        if deposit_amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            balance += deposit_amount
            print(f"Deposit successful! Current balance: {balance}")

    elif option == 3:
        withdrawal_amount = int(input("Enter amount to withdraw: "))

        if withdrawal_amount <= 0:
            print("Withdrawal amount must be greater than 0.")

        elif withdrawal_amount > balance:
            print("Insufficient funds.")

        else:
            balance -= withdrawal_amount
            print(
                f"Withdrawal successful!\n"
                f"Remaining balance: {balance}"
            )

    elif option == 4:
        print("Thank you for using the ATM!")
        break

    else:
        print("Please choose a valid option between 1 and 4.")