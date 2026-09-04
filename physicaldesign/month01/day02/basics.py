def is_even(n):
    return n % 2 == 0


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


print("Even:", is_even(10))
print("Odd:", is_even(7))
print("Factorial:", factorial(5))