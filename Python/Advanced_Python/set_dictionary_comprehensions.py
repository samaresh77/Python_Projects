# Set Comprehensions
# {expression for item in iterable}
numbers = {number for number in range(1, 6)}
print(numbers)

numbers = [1, 2, 2, 3, 3, 4, 5, 5]
# unique_numbers = {number for number in numbers}
# or
unique_numbers = set(numbers)
print(unique_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}
print(even_numbers)

# Dictionary Comprehension
# {key: value for item in iterable}

numbers = [1, 2, 3, 4, 5]
squares = {
    number: number * number
    for number in numbers
}
print(squares)

users = {
    "rahul": 25,
    "priya": 30,
    "amit": 22
}
upper_users = {
    name.upper(): age
    for name, age in users.items()
}
print(upper_users)

print("------exercise------")

#Ex - 1
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
even_numbers = {
    num
    for num in numbers
    if num % 2 == 0
}
print(even_numbers)

#Ex - 2
numbers = [1, 2, 3, 4, 5]
squares = {
    num * num
    for num in numbers
}
print(squares)

#Ex - 3
numbers = [1, 2, 3, 4, 5]
dictionary = {
    val: val * val
    for val in numbers
}
print(dictionary)

#Ex - 4
users = {
    "Rahul": 25,
    "Priya": 17,
    "Amit": 30,
    "John": 16
}
dictionary = {
    name: age 
    for name, age in users.items()
    if age >= 18
}
print(dictionary)

#Ex - 5
users = [
    {"id": 1, "name": "Rahul", "active": True},
    {"id": 2, "name": "Priya", "active": False},
    {"id": 3, "name": "Amit", "active": True},
    {"id": 4, "name": "John", "active": False}
]
dictionary = {
    user["id"]: user["name"].upper()
    for user in users
    if user["active"]
}
print(dictionary)