# @property : With @property, you control what happens when someone reads or changes the value.
# The outside code interacts with salary, but the class controls how salary is accessed internally.

class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.__salary = new_salary

employee1 = Employee("Rahul", 25, 50000)
try:
    employee2 = Employee("Priya", 30, -10000)
except ValueError as error:
    print("Error:", error)

print(employee1.salary)

employee1.salary = 60000

print(employee1.salary)