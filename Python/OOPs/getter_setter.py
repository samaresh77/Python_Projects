class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.__salary = salary


employee1 = Employee("Rahul", -50000)

print(employee1.get_salary())

employee1.set_salary(60000)

print(employee1.get_salary())