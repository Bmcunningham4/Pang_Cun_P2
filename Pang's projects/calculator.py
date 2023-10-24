#Calculator script that takes user input (2 numbers) and performs the selected algorithm

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


#! while loop to operate user input
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print ("Enter 'subtract' for subtraction")
    print ("Enter 'multiiply' for multiplication")
    print ("Enter 'divide' for division")
    print ("Enter 'exit' to exit the program")

    user_input = input(": ")

#! Establishing number variables, exit code and if statements to decide what arithmetic to use
    if user_input == "exit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ", division(num1, num2))

    else:
        print("Invalid input")


    
