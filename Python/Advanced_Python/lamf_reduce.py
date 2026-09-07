# map() → transform every item
# filter() → select matching items
# reduce() → combine items into one result
# reduce() repeatedly combines values until only one value remains.

from functools import reduce

numbers = [10, 20, 30, 40, 50]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)

# multiplication
numbers = [2, 3, 4, 5]

result = reduce(
    lambda a, b: a * b,
    numbers
)

print(result)

# maximum value
numbers = [10, 45, 23, 89, 12, 67]
max_value =reduce(
    lambda a, b: max(a, b), numbers
)
print(max_value)

prices = [100, 200, 300, 400]
total = reduce(lambda a, b: a + b, prices)
print(total)

# reduce() with an initial value
numbers = [1, 2, 3]

total = reduce(
    lambda a, b: a + b,
    numbers,
    10
)

print(total)
