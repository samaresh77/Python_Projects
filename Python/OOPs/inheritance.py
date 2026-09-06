# 1. What is inheritance?
# Inheritance means creating a new class from an existing class.
# The existing class is called the parent/base class.
# The new class is called the child/derived class.

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Developer(Employee):
    pass

developer1 = Developer("Rahul", 25)

developer1.display_info()

# super()

class Employee:

    def __init__(self, name, age, employee_id):
        self.name = name
        self.age = age
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")

    # Method Overriding
    def display_role(self):
        print("I am an employee")


class Developer(Employee):

    def __init__(self, name, age, employee_id, programming_language):
        super().__init__(name, age, employee_id)
        self.programming_language = programming_language

    def display_developer_info(self):
        self.display_info()
        print(f"Programming Language: {self.programming_language}")

    # Method Overriding
    def display_role(self):
        print("I am a developer")

class Manager(Employee):

    def __init__(self, name, age, employee_id, team_size):
        super().__init__(name, age, employee_id)
        self.team_size = team_size

    def display_manager_info(self):
        self.display_info()
        print(f"Team Size: {self.team_size}")

    # Method Overriding
    def display_role(self):
        print("I am a manager")


developer1 = Developer(
    "Rahul",
    25,
    "EMP101",
    "Python"
)
manager1 = Manager(
    "Priya",
    32,
    "EMP102",
    8
)

developer1.display_developer_info()
manager1.display_manager_info()

developer1.display_role() # display_role()  ← overrides parent
manager1.display_role() # display_role()  ← overrides parent