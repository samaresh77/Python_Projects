# 1. What is encapsulation?
# Encapsulation means keeping data and the methods that operate on that data together inside a class, 
# while controlling how that data is accessed or modified.
# Keeping data and behavior together inside an object.

# Protected convention: '_' means "This is intended for internal/protected use."
# Python doesn't strictly prevent it.
# The underscore is mainly a convention telling developers:

class Employee:

    def __init__(self, name, salary):
        self.name = name
        # Protected convention: _
        self._salary = salary

employee = Employee("Sam", 50000)
print(employee._salary) # 50000

class Employee:

    def __init__(self, name, salary):
        self.name = name
        # Private attributes: __
        self.__salary = salary

employee = Employee("Sam", 50000)
print(employee.__salary) #AttributeError

