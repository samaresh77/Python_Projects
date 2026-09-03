#for
for n in range(1,11):
    print(n)

# steps
for i in range(2,21,2):
    print(i)

# or
for i in range(2,21):
    if i % 2 == 0:
        print(i)

# sum of numbers
total = 0
for i in range(1,101):
    total += i
print(total)

#user found or not
curr_user = input("Enter a name: ").strip()
users = [
    "John",
    "Alice",
    "Bob",
    "David"
]
if curr_user in users:
    print("User found")
else:
    print("User not found")