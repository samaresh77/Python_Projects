# What does | None mean?

from pydantic import BaseModel


class User(BaseModel):
    name: str
    phone: str | None  #phone can contain a string or None.

user = User(
    name="Rahul",
    phone=None
)
print(user)

#
class User(BaseModel):
    name: str
    phone: str | None = None # give default value as None

user = User(
    name="Rahul"
)
print(user)

#EX

class Customer(BaseModel):
    name: str
    email: str
    phone: str | None = None
    city: str = "Kolkata"
    active: bool = True

customer1 = Customer(
    name = "Sam",
    email = "sam@example.com",
)
print(customer1)
customer2 = Customer(
    name = "Sam",
    email = "sam@example.com",
    phone= "9803848",
    city= "Kol"
)
print(customer2)
customer3 = Customer(
    name = "Sam",
    email = "sam@example.com",
    phone = None,
    city = "Delhi",
    active = False
)
print(customer3)