# 1. What is an Exception?
# An exception is an error that occurs while a Python program is running.

# | Exception           | Example                                 |
# | ------------------- | --------------------------------------- |
# | `ValueError`        | `"abc"` converted to `int`              |
# | `TypeError`         | incompatible types                      |
# | `ZeroDivisionError` | dividing by zero                        |
# | `KeyError`          | dictionary key doesn't exist            |
# | `IndexError`        | list index doesn't exist                |
# | `FileNotFoundError` | file doesn't exist                      |
# | `NameError`         | variable doesn't exist                  |
# | `AttributeError`    | object doesn't have requested attribute |


# handle error
# 1
try:
    age = int(input("Enter age: "))
    print(f"Your age is {age}")

except ValueError:
    print("Invalid age. Please enter a number.")

# 2
try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Number cannot be zero.")

# 3 else: block executes only when no exception occurs.
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)

# 4  finally:  executes regardless of whether an exception occurs.
try:
    number = int(input("Enter number: "))
    print(number)

except ValueError:
    print("Invalid number.")

finally:
    print("Program finished.")

# 5 
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Number:", number)

finally:
    print("Done.")

# 6 
try:
    number = int("abc")

except ValueError as error:
    print("Error:", error)

# 7 raise
age = 15

if age < 18:
    raise ValueError("Age must be 18 or older.")

# user validation
def create_user(name, age):

    if not name:
        raise ValueError("Name cannot be empty.")

    if age < 18:
        raise ValueError("User must be at least 18.")

    return {
        "name": name,
        "age": age
    }

try:
    user = create_user("John", 25)
    print(user)

except ValueError as error:
    print("Error:", error)

