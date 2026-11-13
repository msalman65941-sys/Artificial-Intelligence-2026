import math


def Menu():
    print("Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. x_power_y")
    print("7. Log (base 10)")
    print("8. Natural log (ln)")

    return input("Please select an option (1-8) or type 'quit' to exit: ")

def main():
    while True:
        choice = Menu().lower()

        if choice == 'quit':
            print("Goodbye!")
            break

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The result of addition is: {num1 + num2}")
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The result of subtraction is: {num1 - num2}")
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The result of multiplication is: {num1 * num2}")
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 != 0:
                print(f"The result of division is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            number = int(input("Enter a non-negative integer: "))
            if number >= 0:
                result = 1
                for value in range(1, number + 1):
                    result *= value
                print(f"The result of factorial is: {result}")
            else:
                print("Error: Factorial is only defined for non-negative integers.")
        elif choice == '6':
            x = float(input("Enter x: "))
            y = float(input("Enter y: "))
            print(f"The result of x_power_y is: {x ** y}")
        elif choice == '7':
            number = float(input("Enter a positive number: "))
            if number > 0:
                print(f"The result of log is: {math.log10(number)}")
            else:
                print("Error: Logarithm is only defined for positive numbers.")
        elif choice == '8':
            number = float(input("Enter a positive number: "))
            if number > 0:
                print(f"The result of ln is: {math.log(number)}")
            else:
                print("Error: Natural logarithm is only defined for positive numbers.")
        else:
            print("Invalid option selected. Please try again.")

