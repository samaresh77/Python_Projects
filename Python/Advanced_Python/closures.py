# What is a closure?
# A closure happens when:
# An outer function creates a variable.
# An inner function uses that variable.
# The outer function finishes.
# The inner function remembers the variable.

def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner

function = outer()
function()

#
def create_counter():
    count = 0

    def counter():
        nonlocal count # without nonlocal keyword python teact count as local so give error
        count += 1
        return count

    return counter

counter = create_counter()

print(counter())
print(counter())
print(counter())

# Closure vs decorator
def logger(function):

    def wrapper(*args, **kwargs):
        print("Calling function")
        return function(*args, **kwargs)

    return wrapper

#
def create_multiplier(multiplier):

    def multiply(number):
        return number * multiplier

    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))