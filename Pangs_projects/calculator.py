# Calculator script that takes user input (2 numbers) and performs the selected algorithm

#* from Cuns_projects.password_generator import get_integer_input --- This should be bloody working but isn't

#!Functions for arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x,y):
    if y==0:
        return "Error: Cannot divide by zero"
    return x / y

def get_integer_input2(prompt):
    while True:
        user_input = input(prompt)
        try:
            integer_input = int(user_input)
            return integer_input
        except ValueError:
            print(f"Invalid input. Please enter a valid integer.")
            print()

#! while loop to operate user input
def main():
    print("You have chosen to use the calculator!")
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print ("Enter 'subtract' for subtraction")
        print ("Enter 'multiiply' for multiplication")
        print ("Enter 'divide' for division")
        print ("Enter 'exit' to exit the program")

        user_input = input(": ")
        print()

    #! Establishing number variables, exit code and if statements to decide what arithmetic to use
        if user_input == "exit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = get_integer_input2("Enter the first number: ")
            num2 = get_integer_input2("Enter the second number: ")

            if user_input == "add":
                print("Result: ", add(num1, num2), '\n')
            elif user_input == "subtract":
                print("Result: ", subtract(num1, num2), '\n')
            elif user_input == "multiply":
                print("Result: ", multiply(num1, num2), '\n')
            elif user_input == "divide":
                print("Result: ", division(num1, num2), '\n')

        else:
            print("Invalid input", '\n')

if __name__ == "__main__":
    main()

    
