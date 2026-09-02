# Even/Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Age category
age = int(input("Enter a number: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

# username and password checking
correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter Password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")

# corporate access
# roles = ["admin", "manager", "employee"]
role = input("Enter your role: ").lower()
if role in ["admin", "manager"]:
    print("Full access")
elif role == "employee":
    print("Limited access")
else:
    print("Access denied")
