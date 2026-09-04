# 1 write() is for writing text:
with open("notes.txt", "w") as file:
    file.write("Python File Handling\nI am learning Python.\nI will become a Python developer.")
print("file created")

# 2 read
with open("notes.txt", "r") as file:
    # for line in file:
    #     print(line.strip())
    print(file.read())

# 3 append
with open("notes.txt", "a") as file:
    file.write("\nI am learning FastAPI next.")
    print("test added")

# 4 json
import json

users = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 22}
]
# dump() -> takes a Python data structure and converts it into JSON.
with open("users.json", 'w') as file:
    json.dump(users, file, indent=4) 

with open("users.json", "r") as file:
    users = json.load(file)

print(users)