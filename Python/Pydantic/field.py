# What is Field()?

# | Constraint    | Meaning                     |
# | ------------- | --------------------------- |
# | `gt`          | greater than                |
# | `ge`          | greater than or equal       |
# | `lt`          | less than                   |
# | `le`          | less than or equal          |
# | `min_length`  | minimum string length       |
# | `max_length`  | maximum string length       |
# | `multiple_of` | must be a multiple of       |
# | `pattern`     | string must match a pattern |

from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(ge=18, le=100)
    username: str = Field(
        min_length=3,
        max_length=20
    )

user = User(
    name="Rahul",
    age=18,
    username="sam"
)

print(user)

#
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=100
    )

    price: float = Field(
        gt=0
    )

    quantity: int = Field(
        ge=0
    )

    available: bool = True

    category: str = "general"

product = Product(
    name="Laptop",
    price=75000,
    quantity=5
)

print(product)

# Nested models

from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    country: str


class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address


user = User(
    name="Rahul",
    age=25,
    email="rahul@example.com",
    address={
        "city": "Kolkata",
        "state": "West Bengal",
        "country": "India"
    }
)

print(user)

print(user.name)
print(user.address.city)
print(user.address.state)
print(user.address.country)