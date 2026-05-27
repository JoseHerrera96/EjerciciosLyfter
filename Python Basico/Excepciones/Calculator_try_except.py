def add(a, b):
    print("This is the add function.")
    try:
        a = float(a)
        b = float(b)
        result = a + b
        print(f"{a} + {b} = {result}")

        return result
    
    except TypeError as e:
        print(f"An error occurred while converting inputs to float: {e}")
        return a
    

def subtract(a, b):
    print("This is the subtract function.")
    try:
        a = float(a)
        b = float(b)
        result = a - b
        print(f"{a} - {b} = {result}")

        return result
    
    except TypeError as e:
        print(f"An error occurred while converting inputs to float: {e}")
        return a

def multiply(a, b):
    print("This is the multiply function.")
    try:
        a = float(a)
        b = float(b)
        result = a * b
        print(f"{a} * {b} = {result}")

        return result
    
    except TypeError as e:
        print(f"An error occurred while converting inputs to float: {e}")
        return a

def divide(a, b):
    print("This is the divide function.")
    try:
        a = float(a)
        b = float(b)
        result = a / b
        print(f"{a} / {b} = {result}")

        return result
    
    except TypeError as e:
        print(f"An error occurred: {e}")
        return a
    except ZeroDivisionError as e:
        print(f"Division by zero is not allowed. Details: {e}")
        return a

def main_menu(current_value):
    
    print(" ")
    print(f"Current value: {current_value}")

    print(" ")
    print("1. Addition (+)" \
    "\n2. Subtraction (-)" \
    "\n3. Multiplication (*)" \
    "\n4. Division (/)" \
    "\n5. Clear")
    print(" ")

    user_operation = input("Select an operation: ")

    return user_operation

def calculator():

    print(" ")
    print("\nWelcome to the calculator!")

    starter_value = input("\nEnter the initial value: ")
    current_value = starter_value
    previous_value = starter_value

    while True:

        user_operation = main_menu(current_value)
        print(" ")

        try:
            if not user_operation in ['1', '2', '3', '4', '5']:
                raise ValueError("Invalid input. Please choose a valid operation.")
            
            if user_operation in ['1', '2', '3', '4']:
                num = input("Enter second operand: ")
                print(" ")

            if user_operation == '1':
                result = add(current_value, num)
            elif user_operation == '2':
                result = subtract(current_value, num)
            elif user_operation == '3':
                result = multiply(current_value, num)
            elif user_operation == '4':
                result = divide(current_value, num)
            elif user_operation == '5':
                result = 0.0
                print("Calculator cleared. Current value reset to 0.")
            
            previous_value = current_value
            current_value = result

            print(" ")
            decision = input("Do you want to continue? (1.yes / 2.no): ")

            if not decision in ['1', '2']:
                print(" ")
                raise ValueError("Invalid input. Please choose a valid option.")
        
            if decision == '2':
                print(" ")
                print("Thank you for using the calculator. Goodbye!")
                print(" ")
                break

        except ValueError as e:
            print(f"Invalid operation. Details: {e}")       
        except TypeError as e:
            current_value = previous_value
            print(f"Invalid input. Please enter a number. Details: {e}")

if __name__ == "__main__":
    try:
        calculator()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")