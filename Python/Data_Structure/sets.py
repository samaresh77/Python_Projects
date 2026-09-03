# A set stores unique values.
numbers = {1, 2, 3, 4}

# Sets automatically remove duplicates.
numbers = {5, 1, 2, 2, 3, 3, 4, 1}
print(numbers)

# add()
roles = {"admin", "manager"}
roles.add("employee")
print(roles)

# discard()
roles.discard("manager")
print(roles)

# discard() does nothing if it does not exist.
roles.discard("emplyoee")
print(roles)

# remove() can cause an error if the item does not exist.
# roles.remove("manager")
# print(roles)

# Unique Tags
tags = [
    "python",
    "fastapi",
    "python",
    "backend"
]
unique_tags = set(tags)

print(unique_tags)

