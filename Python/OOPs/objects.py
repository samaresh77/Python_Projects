# Object: A physical instance of a class containing actual data.
# Actual thing created from blueprint
class Employee:

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")

employee = Employee(
    "John",
    "Software Engineer",
    60000
)
employee.display_info()