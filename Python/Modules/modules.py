# A module is simply a Python file (.py) that contains code you can reuse from-
# another Python file.

# import calculator

# result1 = calculator.add(10, 20)
# result2 = calculator.subtract(20, 5)

# print(result1)
# print(result2)

from calculator import add, subtract, multiply, divide

print(add(10, 20))
print(subtract(20, 5))
print(multiply(10, 5))
print(divide(10, 2))

from config import APP_NAME, VERSION

print(APP_NAME)
print(VERSION)

from users import get_users, find_user

print(get_users())

user = find_user("John")

if user:
    print("User found")
    print(user)
else:
    print("User not found")