# A list stores multiple values in one variable.
users = ["John", "Alice", "Bob"]
print(users[0])
print(users[-1])
print(len(users))

# Lists are mutable.
# Mutable means:
# We can change the data.
users = ["John", "Alice", "Bob"]
users[1] = "David"
print(users)

# append() add item at the end
users.append("Sam")
print(users)

# insert() Adds an item at a specific position.
users.insert(1, "Tobi")
print(users)

# remove()
users.remove("John")
print(users)

# pop() Remove by index.
users.pop(1)
print(users)

# user exists or not
users = ["John", "Alice", "Bob"]

if "Alice" in users:
    print("User exists")

# List unpacking
name1, name2, name3 = users
print(name1)
print(name2)
print(name3)