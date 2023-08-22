# Define the arithmetic functions
def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")

def mul(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")

def div(a, b):
    if b != 0:  # Check for division by zero
        answer = a / b
        print(f"{a} / {b} = {answer}")
    else:
        print("Division by zero is not allowed.")

# Take user input for values
val1 = int(input("Input the first value: "))
val2 = int(input("Input the second value: "))

# Main loop for user interaction
while True:
    # Display available operations
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter the number of the operation you want to perform: ")
    
    if choice == "1":
        add(val1, val2)
    elif choice == "2":
        sub(val1, val2)
    elif choice == "3":
        mul(val1, val2)
    elif choice == "4":
        div(val1, val2)
    elif choice == "5":
        print("Exiting the program.")
        break  # Exit the loop and end the program
    else:
        print("Invalid input. Please enter a valid operation number.")
