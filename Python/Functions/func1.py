# A function is a reusable block of code that performs a specific task.
def greet():
    print("Hello, Python!")


greet()

# function with parameter


def greet(name):  # name is parameter
    print(f"Hello, {name}!")


greet("John")  # John is argument
greet("Alice")
greet("David")

# return: Give the result back to whoever called me.


def add(a, b):
    return a+b


print(add(10, 20))

# multiple parameter


def user_info(name, age, role):
    print("Name:", name)
    print("Age:", age)
    print("Role:", role)


user_info("John", 25, "Developer")

# Even or Odd


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


result = check_even_odd(11)
print(result)

# Valid user or not


def is_valid_user(name, age):
    if name == "":
        return "name must not be empty"
    elif age < 18:
        return "age must be >= 18"
    else:
        return "Valid user"


result = is_valid_user("John", 18)
print(result)

# default parameter


def greet(name="Guest"):
    return name


print(greet())
print(greet("sam"))


def calculate_discount(price, discount=10):
    return price - (price * (discount/100))


print(calculate_discount(1000))
print(calculate_discount(1000, 20))


def create_user(name, age, role="user"):
    user = {
        "Name": name,
        "Age": age,
        "Role": role
    }
    return user


print(create_user("John", 25))
print(
    create_user(
        name="Alice",
        age=30,
        role="admin"
    )
)
