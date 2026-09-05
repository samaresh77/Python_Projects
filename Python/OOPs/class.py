# Object-Oriented Programming (OOP) in Python is a programming paradigm that organizes code using classes and objects. 
# Class: A logical blueprint or template used to create objects.
# Object: A physical instance of a class containing actual data.

# Blueprint
class User:    #User is the class.
    pass


user1 = User() # user1 is object
user2 = User() # user2 is object

# __init__ Method: The constructor method that runs automatically when you create a new object to initialize its data.

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# self refers to the current object.
class User:
    
    def __init__(self, name, age):
        # Instance Attributes (self.name, self.age)
        self.name = name
        self.age = age

    # When a function belongs to a class, we call it a method.
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    def is_adult(self):
        return self.age >= 18

user1 = User("John", 25)
user2 = User("Alice", 30)
print(user1.name, user1.age)
print(user2.name, user2.age)
user1.introduce()
print(user1.is_adult())