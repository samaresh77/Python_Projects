# Enum = Enumeration.
# It lets you define a fixed collection of named values.

from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    MANAGER = "manager"

role = UserRole.ADMIN

print(role)
print(role.value)
print(role.name)

#
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    MANAGER = "manager"

class User:
    def __init__(self, name: str, role: UserRole):
        self.name = name
        self.role = role

user1 = User("Rahul", UserRole.ADMIN)
user2 = User("Priya", UserRole.USER)

print(user1.role)
print(user1.role.value)