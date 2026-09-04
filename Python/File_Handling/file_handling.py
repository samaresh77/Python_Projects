# What is File Handling?

# File handling means using Python to:

# create files
# read files
# write files
# append data
# modify stored data

# ###
# file = open("example.txt", "r")

# with open("example.txt", "r") as file:
#     ...

# 1 write file
with open("message.txt", "w") as file:
    file.write("Hello Python!")

# 2 Read file
file = open("message.txt", "r")

content = file.read()

file.close()

# proffessional

with open("message.txt", "r") as file:
    content = file.read()

print(content)

# 3 append file
with open("message.txt", "a") as file:
    file.write("\nHello Node!\nHello Js!\nHello React!")

# file.read() -> Reads everything.
# file.readline() -> Reads one line.
# file.readlines() -> Reads all lines into a list.

# line by line
with open("message.txt", "r") as file:
    for line in file:
        print(line.strip())

# FileNotFoundError
try:
    with open("abc.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")


# Python → JSON
# Python has a built-in module:
import json

users = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30}
]

with open("users.json", "w") as file:
    json.dump(users, file, indent=4) #indent -> Making JSON Readable

# load use when file already exists otherwise gives FileNotFoundError
with open("users.json", "r") as file:
    users = json.load(file)

print(users)