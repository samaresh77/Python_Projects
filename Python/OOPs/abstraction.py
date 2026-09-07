# What is Abstraction?
# Abstraction means exposing what an object should do while hiding how it does it.

# Python provides the abc module for creating abstract classes.
# from abc import ABC, abstractmethod

# There are two important things here:

# ABC
# Means:
# This class is an Abstract Base Class.

# @abstractmethod
# Means:
# Child classes must provide an implementation of this method.

from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):

    def calculate_salary(self):
        return 60000

class Manager(Employee):

    def calculate_salary(self):
        return 100000

developer = Developer()
manager = Manager()

print(developer.calculate_salary())
print(manager.calculate_salary())
print("---------------------")

# Abstraction + Polymorphism
from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):

    def calculate_salary(self):
        return 60000


class Manager(Employee):

    def calculate_salary(self):
        return 100000


class Designer(Employee):

    def calculate_salary(self):
        return 50000

employees = [
    Developer(),
    Manager(),
    Designer()
]

for employee in employees:
    print(employee.calculate_salary())

print("------------------")

# Exercise

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):

    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def calculate_salary(self):
        return 60000

class Manager(Employee):

    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def calculate_salary(self):
        return 100000

class Designer(Employee):

    def __init__(self, name, employee_id, design_tool):
        super().__init__(name, employee_id)
        self.design_tool = design_tool

    def calculate_salary(self):
        return 50000

developer = Developer("Rahul", "emp101", "python")
manager = Manager("Tom", "emp102", 10)
designer = Designer("Alise", "emp103", "Canva")

employees = [
    developer,
    manager,
    designer
]
for employee in employees:
    print(f"Name: {employee.name}")
    print(f"Employee ID: {employee.employee_id}")
    print(f"Salary: {employee.calculate_salary()}")
    print()
