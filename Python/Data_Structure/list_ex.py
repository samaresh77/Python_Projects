# 1
users = ["John", "Alice", "Bob"]

users.append("David")
users.remove("Alice")
users[1] = "Robert"
print(users)
print(len(users))

# 2
users = ["alice", "bob", "robert"]
users = [u.capitalize() for u in users]
print(users)
users = ["mary jane", "bob", "robert"]
users = [u.title() for u in users]
print(users)

users = ["John", "Alice", "Bob", "David"]

user = input("Enter name to find: ").strip().lower()

users = [name.lower() for name in users]

if user in users:
    print("User found")
else:
    print("User not found")

# 3
skills = [
    "Python",
    "FastAPI",
    "Python",
    "PostgreSQL",
    "FastAPI"
]
updated_skills = set(skills)
print(updated_skills)

# 4
user = {
    "name": "John",
    "age": 25,
    "role": "developer"
}
user["email"] = "john@example.com"
user["age"] = 26
print(user["name"])

for key,value in user.items():
    print(key, value)