# What is an iterator?
# An iterator is an object that gives you values one at a time.

numbers = [10, 20, 30]

iterator = iter(numbers)

print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Iterable vs Iterator

# Iterable
# An object that you can loop over.
# Examples:
# list # A list is an iterable.
# tuple
# string
# set
# dictionary

# Iterator
# An object that produces values one at a time using next().
# iterator = iter(numbers)
