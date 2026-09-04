def is_even(n):
    return n % 2 == 0


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


while True:
    print("\n===== MENU =====")
    print("1. Check even/odd")
    print("2. Calculate factorial")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        number = int(input("Enter a number: "))

        if is_even(number):
            print("Even")
        else:
            print("Odd")

    elif choice == "2":
        number = int(input("Enter a number: "))
        print(f"Factorial: {factorial(number)}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")