# 1. What is a decorator?
# A decorator is a function that adds or changes behavior of another function without-
# modifying the original function's code.

# First understand functions as objects
# In Python, functions can be assigned to variables.
def say_hello():
    print("Hello!")

# greeting = say_hello()  #calling the function.
greeting = say_hello     # There are no parentheses.Store a reference to this function.

greeting()

# A function can receive another function
# Python functions can also be passed as arguments.
def say_hello():
    print("Hello!")


def execute_function(function):
    function()


execute_function(say_hello)

# decorator
def my_decorator(function):

    def wrapper():
        print("Before function")

        function()

        print("After function")

    return wrapper

# def say_hello():
#     print("Hello! Mid")
# say_hello = my_decorator(say_hello)
#instead of upper 3 lines put below 3 lines
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Ex
def logger(function):

    def wrapper():
        print("Function started")

        function()

        print("Function finished")

    return wrapper

@logger
def get_users():
    print("Getting users...")

get_users()

# Decorators with arguments
def greet(name):
    print(f"Hello {name}")

def decorator(function):

    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

    return wrapper

greet("Sam")

# Ex
def decorator(function):

    def wrapper(*args, **kwargs):
        print("Before")
        function(*args, **kwargs)
        print("After")

    return wrapper

@decorator
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

