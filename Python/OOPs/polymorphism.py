# Polymorphism means the same interface/method can produce different behavior depending on the object.

class Employee:

    def __init__(self, name, age, emp_id):
        self.name = name
        self.age = age
        self.emp_id = emp_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Emp_id: {self.emp_id}")

class Developer(Employee):

    def __init__(self, name, age, emp_id, programming_language):
        super().__init__(name, age, emp_id)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    # Method Overriding
    def display_role(self):
        print("I am a developer")

class Manager(Employee):

    def __init__(self, name, age, emp_id, team_size):
        super().__init__(name, age, emp_id)
        self.team_size = team_size

    def manager_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")

    # Method Overriding
    def display_role(self):
        print("I am a manager")

class Designer(Employee):

    def __init__(self, name, age, emp_id):
        super().__init__(name, age, emp_id)

    def display_role(self):
        print("I am a designer")

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
designer1 = Designer(
    "Amit",
    28,
    "EMP103"
)

# developer1.display_info()
# manager1.manager_info()

employees = [developer1, manager1, designer1]

for employee in employees:
    employee.display_role()