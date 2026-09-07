numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers)

# List comprehension: Python gives us a shorter and very common way to write list
# [expression for item in iterable]
numbers = [number for number in range(1, 6)]
print(numbers)

squares = [number * number for number in range(1, 6)]
print(squares)

names = ["rahul", "priya", "amit"]
upper_names = [name.upper() for name in names]
print(upper_names)

print("-------Exercise--------")

# Ex - 1 
numbers = [number for number in range(1, 21)]
print(numbers)

# Ex - 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [
    num
    for num in numbers
    if num % 2 == 0
]

print(even_list)

# Ex - 3
numbers = [1, 2, 3, 4, 5]
squares = [
    num * num
    for num in numbers
]
print(squares)

#Ex - 4
users = [
    {"name": "Rahul", "age": 25},
    {"name": "Priya", "age": 17},
    {"name": "Amit", "age": 30},
    {"name": "John", "age": 16}
]
# result = [
#     expression
#     for item in iterable
#     if condition
# ]
result = [
    user["name"].upper()
    for user in users
    if user["age"] >= 18
]
print(result)