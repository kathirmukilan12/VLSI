numbers = input("Enter numbers separated by spaces: ")

numbers = numbers.split()

values = []

for number in numbers:
    values.append(float(number))

minimum = values[0]
maximum = values[0]
total = 0

for number in values:
    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

    total = total + number

average = total / len(values)

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {average}")