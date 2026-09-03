def add(a, b):
    return a + b

# Python doesn't know what type a and b are supposed to be.
# We can give Python/readers that information:
# Type Hints
def add(a: int, b: int) -> int:
    return a + b

# Meaning:

# a      → int
# b      → int
# return → int

# Type Hints
def greet(name: str) -> str:
    return f"Hello, {name}"
def is_adult(age: int) -> bool:
    return age >= 18

# Ex 1
name = "John"
def greet():
    print(name)

def another_function():
    message = "Hello"
    print(message)

# Ex - 2
def is_adult(age: int) -> bool:
    return age >= 18
print(is_adult(18))

# Ex - 3
def create_user(name: str, age: int, role: str = "user") -> dict:
    user = {
        "name": name,
        "age": age,
        "role": role
    }
    return user

print(create_user("abc", 23, "admin"))