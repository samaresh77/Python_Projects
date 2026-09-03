# A docstring describes what a function does.
def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""  # docstring
    return a + b


print(add(10, 20))
print(add.__doc__)

#


def calculate_discount(price: float, discount: float = 10) -> float:
    """
    Calculate the final price after applying a discount.

    Args:
        price: Original product price.
        discount: Discount percentage.

    Returns:
        Final price after discount.
    """
    return price - (price * discount / 100)

# Ex - 1


def greet(name: str = "Guest") -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


print(greet())

# Ex - 2


def calculate_sum(*numbers: int) -> int:
    """Return the sum of all provided numbers."""
    total = 0
    for num in numbers:
        total += num
    return total


print(calculate_sum(10, 20, 30))

# Ex - 3


def create_user(name: str, age: int, role: str = "user") -> dict:
    """Create and return a user dictionary."""
    user = {
        "name": name,
        "age": age,
        "role": role
    }
    return user


print(create_user("sam", 25, "developer"))
