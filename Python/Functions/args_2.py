# *args
# which allows an arbitrary number of positional arguments.

# **kwargs
# which allows an arbitrary number of keyword arguments.
# So **kwargs collects keyword arguments into a dictionary.

def create_user(**details):
    print(details)

create_user(
    name="John",
    age=25,
    role="developer"
)

# *args vs **kwargs
# *args
#    ↓
# multiple positional arguments
#    ↓
# tuple
# vs
# **kwargs
#    ↓
# multiple keyword arguments
#    ↓
# dictionary

def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(
    10,
    20,
    30,
    name="John",
    age=25
)

# ex - 1
def print_user(**user):
    print(user)

print_user(
    name="John",
    age=25,
    role="developer"
)

# ex - 2
def show_data(*args, **kwargs):
    print(args)
    print(kwargs)

show_data(
    10,
    20,
    30,
    name="John",
    age=25
)