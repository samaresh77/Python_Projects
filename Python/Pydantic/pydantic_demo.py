# Pydantic
# This is the bridge between Python and FastAPI.

# What problem does Pydantic solve?
# Pydantic uses the type definitions to validate and parse the data.

from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


user = User(
    name="Rahul",
    age=25,
    email="rahul@example.com"
)

print("User:")
print(user)

print("\nName:")
print(user.name)

print("\nDictionary:")
print(user.model_dump())

print("\nJSON:")
print(user.model_dump_json())