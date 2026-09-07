# map()    → transform every item
# filter() → select items that satisfy a condition
# filter(function, iterable)

#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)

#2
users = [
    {"name": "Rahul", "age": 25},
    {"name": "Priya", "age": 17},
    {"name": "Amit", "age": 30},
    {"name": "John", "age": 16}
]
adults = list(
    filter(lambda user: user["age"] >= 18, users)
)
print(adults)

#3
users = [
    {"id": 1, "name": "Rahul", "active": True},
    {"id": 2, "name": "Priya", "active": False},
    {"id": 3, "name": "Amit", "active": True},
    {"id": 4, "name": "John", "active": False}
]
active_users = list(
    filter(lambda user: user["active"], users)
) 
print(active_users)