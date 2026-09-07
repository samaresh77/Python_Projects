# What is map()?
# map() applies a function to every item in an iterable.
# map(function, iterable)

numbers = [1, 2, 3, 4, 5]
doubled = list(
    map(lambda number: number * 2, numbers)
)
print(doubled)

# map() with a normal function
def square(number):
    return number * number

numbers = [1, 2, 3, 4, 5]

squares = list(map(square, numbers))

print(squares)

# map() with strings
names = ["rahul", "priya", "amit"]
upper_names = list(
    map(lambda name: name.upper(), names)
)

print(upper_names)

#Extract names
users = [
    {"id": 1, "name": "Rahul", "age": 25},
    {"id": 2, "name": "Priya", "age": 30},
    {"id": 3, "name": "Amit", "age": 22}
]
names = list(
    map(lambda user: user["name"], users)
)
print(names)

# multiple lists
prices = [100, 200, 300]
quantities = [2, 3, 4]

total = list(
    map(lambda price, quantity: price * quantity, prices, quantities)
)
print(total)