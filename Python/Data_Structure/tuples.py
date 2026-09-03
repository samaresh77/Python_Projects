# A tuple also stores multiple values.
user = ("John", "Admin", 25)

# But there is one important difference:
# Tuples are immutable.
# That means you cannot change their items.

user = ("John", "Admin", 25)
# user[0] = "Alice" # error not modify
print(user)

# Tuples are useful when data should not change.
supported_roles = (
    "admin",
    "manager",
    "employee"
)
print(supported_roles[0])

# Tuple Unpacking
user = ("John", "admin", 25)

name, role, age = user

print(name)
print(role)
print(age)