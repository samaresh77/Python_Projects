# Serialization & Deserialization
# What is Serialization?
# Think of:
# Python Object
#      ↓
# Dictionary / JSON

# Converting a Pydantic model into data that can be sent/stored/transmitted is serialization.

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
# convert the object called user to dictionary
data = user.model_dump() # pydantic V2 -> user.model_dump() ,  V3 -> user.dict()
print(data)
print(type(data))

# Pydantic Model
#       ↓
# model_dump()
#       ↓
# Python Dictionary

json_data = user.model_dump_json()

print(json_data)
print(type(json_data))

# Deserialization
#dict
data = {
    "name": "Priya",
    "age": 23,
    "email": "priya@example.com"
}
# convert it into a Pydantic model
user = User.model_validate(data)

print(user)
print(type(user))

# Dictionary
#     ↓
# model_validate()
#     ↓
# Pydantic Model

# JSON → Pydantic Model
json_data = """
{
    "name": "Samaresh",
    "age": 25,
    "email": "samaresh@example.com"
}
"""
user = User.model_validate_json(json_data)
print(user)

#              SERIALIZATION
# Pydantic Model ─────────────→ Dictionary
#        │                       model_dump()
#        │
#        └─────────────────────→ JSON
#                                 model_dump_json()


#              DESERIALIZATION
# Dictionary ──────────────────→ Pydantic Model
#                                 model_validate()

# JSON ────────────────────────→ Pydantic Model
#                                 model_validate_json()