#type
name = "Samaresh"
age = 25
salary = 50000.50
is_developer = True
job = None

print(type(name))
print(type(age))
print(type(salary))
print(type(is_developer))
print(type(job))

# f-Strings
name = "Samaresh"
age = 25

print(f"My name is {name} and I am {age}")

#input taken -> input() always returns a string.
name = input("Enter your name: ")

print(name)

age = input("Enter your age: ")

print(type(age))

age2 = int(input("Enter your age: "))
print(type(age2))