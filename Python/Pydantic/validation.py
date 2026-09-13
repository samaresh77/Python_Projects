# What is validation?
# Validation means:
# Checking whether incoming data follows the rules your application expects.

from pydantic import BaseModel, ValidationError


class Product(BaseModel):
    name: str
    price: float
    quantity: int

#valid
product = Product(
    name="Laptop",
    price=75000,
    quantity=5
)
#invalid
# product = Product(
#     name="Laptop",
#     price="abc",
#     quantity=5
# )
print(product)

# Catching ValidationError
class Product(BaseModel):
    name: str
    price: float
    quantity: int


try:
    product = Product(
        name="Laptop",
        price="hello",
        quantity=5
    )

    print(product)

except ValidationError as error:
    print("Validation failed!")
    print(error)

#Ex
print("---------------------------------------------------------")

from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    name: str
    age: int
    salary: float
    active: bool = True

#valid check
employee = Employee(
    name="Samaresh",
    age=25,
    salary=50000
)

print(employee)

#invalid check
try:
    Employee(
        name="Samaresh",
        age="hello",
        salary=50000
    )

except ValidationError as error:
    print("Validation failed!")
    print(error.errors())

#Missing check
try:
    Employee(
        name="Samaresh",
        age=25
    )

except ValidationError as error:
    print("Validation failed!")
    print(error.errors())