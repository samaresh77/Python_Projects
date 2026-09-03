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

option = 0

while option != 4:
    print(
            f"Choose your options below:\n"
            f"1: Check Balance\n"
            f"2: Deposite\n"
            f"3: Withdraw\n"
            f"4: Exit"
        )
    option = int(input("Enter a number: "))
    if option < 1 or option > 4:
        print("Choose the correct option from 1 to 4 \n")
    elif option == 1:
        print(f"Your balance is {balance}\n")
    elif option == 2:
        add_balance = int(input("Enter amount to deposite: "))
        if add_balance <= 0:
            print("Deposite amount must be greater than 0\n")
        else:
            balance += add_balance
            print(f"Your Current balance is {balance}\n")
    elif option == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= 0:
            print("Withdraw Amount must be greater than 0\n")
        elif withdraw > balance:
            print("Insuficient fund\n")
        else:
            balance -= withdraw
            print(
                    f"Withdrawl Successful!"
                    f"Remaining balance {balance}\n"
                )
    