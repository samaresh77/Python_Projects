# ATM Machine

current_balance = int(input("Enter your current amount: "))
Withdrawal_amount = int(input("Enter your withdrawal amount: "))

if current_balance < 1:
    print("Withdrawal amount must be greater than 0")
elif current_balance < Withdrawal_amount:
    print("Withdrawal amount cannot be greater than current balance")
else:
    print(f"Current balance: {current_balance}\nWithdrawal amount: {Withdrawal_amount}\nWithdrawal successful\nRemaining balance: {current_balance-Withdrawal_amount}")