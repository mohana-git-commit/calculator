def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    print("Welcome to the intermediate calculator!")

    while True:
        
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        while True:
            choice = input("Enter choice (1/2/3/4): ")

            if choice in ['1', '2', '3', '4']:
                break
            else:
                print("Invalid input! Please choose a valid operation.")

        if choice == '1':
            print(f"The result of {num1} + {num2} is {add(num1, num2)}\n")
        elif choice == '2':
            print(f"The result of {num1} - {num2} is {subtract(num1, num2)}\n")
        elif choice == '3':
            print(f"The result of {num1} * {num2} is {multiply(num1, num2)}\n")
        elif choice == '4':
            print(f"The result of {num1} / {num2} is {divide(num1, num2)}\n")

        another_calculation = input("Do you want to perform another calculation? (y/n): ")
        if another_calculation.lower() != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
