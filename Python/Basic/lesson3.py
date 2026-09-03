# for in
names = ["John", "Alice", "Bob"]
for name in names:
    print(name)

# range
for number in range(5):
    print(number)

for number in range(0, 11, 2):
    print(number)


# while
number = 1

while number <= 5:
    print(number)
    number += 1


# Enumerate
users = ["John", "Alice", "Bob"]

for index, user in enumerate(users):
    print(index, user)