current_balance = int(input("Enter your current balance: "))
withdrawal_amount = int(input("Enter your withdrawal amount: "))

if withdrawal_amount <= 0:
    print("Withdrawal amount must be greater than 0")

elif withdrawal_amount > current_balance:
    print("Withdrawal amount cannot be greater than current balance")

else:
    remaining_balance = current_balance - withdrawal_amount

    print(
        f"Withdrawal successful\n"
        f"Remaining balance: {remaining_balance}"
    )