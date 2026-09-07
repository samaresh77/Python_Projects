# Lambda Functions
# lambda arguments: expression

#1
square = lambda number: number * number
print(square(10))

#2
is_even = lambda number: number % 2 == 0
print(is_even(10))
print(is_even(7))

#3
maximum = lambda a, b: max(a, b)
print(maximum(10, 20))

#sorted
users = [
    {"name": "Rahul", "age": 25},
    {"name": "Priya", "age": 30},
    {"name": "Amit", "age": 22}
]

sorted_users = sorted(
    users,
    key=lambda user: user["age"]
)
print(sorted_users)

# string len
names = [
    "Rahul",
    "Alexander",
    "Bob",
    "Chris"
]
sorted_names = sorted(
    names,
    key=lambda name: len(name)
)
print(sorted_names)