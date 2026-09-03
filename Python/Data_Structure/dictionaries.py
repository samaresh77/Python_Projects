# Dictionaries are extremely important for backend development.
# A dictionary stores:
# key → value

user = {
    "name": "John",
    "age": 25,
    "role": "admin"
}
# access data
print(user["name"])

# add new data
user["email"] = "john@example.com"
print(user)

# update data
user["age"] = 26
print(user["age"])

# delete data
del user["role"]
# or
user.pop("age")
print(user)

# .get()
print(user.get("age")) # default value None
print(user.get("age", "Age not available"))
# print(user["age"]) #causes an error because "age" does not exist.

# keys
for key in user:
    print(key)

# values
for value in user.values():
    print(value)

for key, value in user.items():
    print(f"{key}: {value}")

# List of Dictionaries
users = [
    {
        "id": 1,
        "name": "John",
        "age": 25,
        "role": "admin"
    },
    {
        "id": 2,
        "name": "Alice",
        "age": 30,
        "role": "manager"
    },
    {
        "id": 3,
        "name": "Bob",
        "age": 22,
        "role": "employee"
    }
]

for user in users:
    print(user["name"])

# Python dictionary:
user = {
    "id": 1,
    "name": "John",
    "role": "admin"
}
# Json
{
    "id": 1,
    "name": "John",
    "role": "admin"
}

# They look almost identical.
# Main difference

# Python:

# True
# False
# None

# JSON:

# true
# false
# null