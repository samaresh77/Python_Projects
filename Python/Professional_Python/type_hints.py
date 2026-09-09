def get_user(user_id: int) -> dict:
    ...

# user_id → int
# return  → dict

def add(a: int, b: int) -> int:
    return a + b

# Python doesn't automatically reject this just because we wrote int.
print(add("10", "20")) # 1020

# Type Hints for Lists
names: list[str] = [
    "Rahul",
    "Priya",
    "Amit"
]
def get_names() -> list[str]:
    return ["Rahul", "Priya", "Amit"]

# Dictionary Type Hints
user: dict[str, int | str] = {
    "name": "Rahul",
    "age": 25
}
users: list[dict[str, int | str]]

# Tuple Type Hints
user: tuple[str, int] = ("Rahul", 25)

# Set Type Hints
numbers: set[int] = {1, 2, 3, 4}

# None as a Return Type
# This function doesn't return a meaningful value.
def print_user(name: str) -> None:
    print(name)

# | — Multiple Possible Types
# value can be an int OR a str.
def process(value: int | str):
    ...

process(100)
process("100")

# Return Types Can Also Have Multiple Types
def get_user(user_id: int) -> dict | None:
    ...

# Ex - 1
from typing import Dict, List

name: str = "Alice"
age: int = 30
salary: float = 50000.0
is_active: bool = True
skills: List[str] = ["Python", "SQL", "Data Analysis"]
scores: Dict[str, int] = {"math": 95, "science": 88}

#Ex - 2
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

#Ex - 3
def get_even_numbers(numbers: list[int]) -> list[int]:
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

#Ex - 4
users = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Priya"},
    {"id": 3, "name": "Amit"}
]
def find_user(user_id: int) -> dict[str, int | str] | None:
    for user in users:
        if user["id"] == user_id:
            return user

    return None

#Ex - 5
def process_value(value: int | str) -> int | str:
    return value