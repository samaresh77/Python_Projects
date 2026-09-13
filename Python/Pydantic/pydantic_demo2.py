# BaseModel & Fields
from pydantic import BaseModel

class User(BaseModel):
    name: str # field
    age: int  # field
    email: str = "abc" # field

# User is now a Pydantic model.
#----------
# creating object
user = User(
    name="Rahul",
    age=25,
    # email="rahul@example.com"
)
# By default, a field without a default value is required.

print(user)

#-----------------------------


class User(BaseModel):
    name: str
    age: int
    email: str
    role: str = "user"
    active: bool = True
    skills: list[str]

user = User(
    name="Rahul",
    age=25,
    email="rahul@example.com",
    skills=["Python", "FastAPI", "PostgreSQL"]
)
print(user)

#---------Nested data

class Address(BaseModel):
    city: str
    country: str


class User(BaseModel):
    name: str
    age: int
    address: Address

user = User(
    name="Rahul",
    age=25,
    address={
        "city": "Kolkata",
        "country": "India"
    }
)
print(user.address.city)

#Ex

class Product(BaseModel):
    name: str       
    price: float
    quantity: int
    available: bool = True
    category: str = "general"

product = Product(
    name="Laptop",
    price=75000,
    quantity=5
)
print(product)
print(product.available)
print(product.category)
print(product.model_dump()) #Convert Pydantic model → dictionary
print(product.model_dump_json())  #Convert Pydantic model → JSON