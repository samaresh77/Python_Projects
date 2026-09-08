# Generators & yield
# A generator produces values one at a time, instead of creating all values in memory at once.
# A generator uses yield instead of return:

def get_numbers():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

numbers = get_numbers()
# print(numbers) # print object type 
print(next(numbers)) # print one by one
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

#
def get_numbers():
    yield 10
    yield 20
    yield 30

for number in get_numbers():
    print(number)

# numbers = list(range(1, 1_000_001))
# print(numbers)

def generate_numbers():
    for number in range(1, 1_000_001):
        yield number

print(next(get_numbers()))

# Generator expression
squares = (x * x for x in range(10))

# return vs yield
# The function ends at the first return.
def example():
    return 10
    return 20

# The function can pause and resume.
def example():
    yield 10
    yield 20

# Ex 
def generate_numbers():
    for number in range(1, 6):
        yield number

for number in generate_numbers():
    print(number)

# Ex
squares = (x * x for x in range(1, 6))

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

# Ex
def generate_users(users):
    for user in users:
        yield user

users = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Priya"},
    {"id": 3, "name": "Amit"},
]

for user in generate_users(users):
    print(user)

# Ex
def test_generator():
    print("Step 1")
    yield 10

    print("Step 2")
    yield 20

generator = test_generator()

print("Generator created")

print(next(generator))
print(next(generator))
