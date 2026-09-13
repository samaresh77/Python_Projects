from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    subjects: list[str]


student = Student(
    name="Rahul",
    age=21,
    subjects=["Python", "FastAPI", "PostgreSQL"]
)

print(student)
print(student.subjects)

#
class Product(BaseModel):
    name: str
    prices: list[float]
    quantities: list[int]


product = Product(
    name="Laptop",
    prices=[50000, 55000, 60000],
    quantities=[1, 2, 3]
)

print(product)

#
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int


class Company(BaseModel):
    name: str
    employees: list[Employee]

company = Company(
    name="Tech Solutions",
    employees=[
        {
            "name": "Rahul",
            "age": 25
        },
        {
            "name": "Priya",
            "age": 23
        }
    ]
)

print(company)
print(company.employees[0].name)
print(company.employees[1].age)

# dict

class Student(BaseModel):
    name: str
    marks: dict[str, int]

student = Student(
    name="Rahul",
    marks={
        "python": 90,
        "fastapi": 85,
        "database": 88
    }
)

print(student)

#
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    skills: list[str]


class Company(BaseModel):
    name: str
    employees: list[Employee]
    departments: dict[str, int]

company = Company(
    name="Tech Solutions",
    employees=[
        {
            "name": "Rahul",
            "age": 25,
            "skills": ["Python", "FastAPI"]
        },
        {
            "name": "Priya",
            "age": 23,
            "skills": ["React", "Next.js"]
        }
    ],
    departments={
        "Engineering": 20,
        "HR": 5,
        "Finance": 4
    }
)