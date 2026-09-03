# *args
def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total
print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30))
print(calculate_sum(1, 2, 3, 4, 5))

# find largest
def find_max(*numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest
print(find_max(10, 50, 20, 80, 30))
print(find_max(-10, -5, -20))