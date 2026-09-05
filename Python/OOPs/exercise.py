# 1
class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

    def change_course(self, new_course):
        self.course = new_course

    def is_adult(self):
        return self.age >= 18

    
student1 = Student(
    "Rahul",
    21,
    "Computer Science"
)
student2 = Student(
    "Priya",
    17,
    "BCA"
)

student1.display_info()
student1.change_course("Data Science")
student1.display_info()
student2.display_info()
print(student1.is_adult())

# Class Attributes vs Instance Attributes

class Student:

    university = "ABC University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"University: {self.university}")

student1 = Student(
    "Rahul",
    21
)
student2 = Student(
    "Priya",
    17
)

student1.display_info()
student2.display_info()
print(Student.university)

# Instance attribute → belongs to one object.
# Class attribute → belongs to the class and can be shared by objects.

student1.university = "XYZ University"

print(student1.university)
print(student2.university)
print(Student.university)