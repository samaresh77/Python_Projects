class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.__salary = new_salary


employee1 = Employee("Rahul", 25, 50000)

print(employee1.get_salary())

try:
    employee1.set_salary(-5000)
except ValueError as error:
    print("Error:", error)

print(employee1.get_salary())