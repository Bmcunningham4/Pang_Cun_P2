#Calculator script that takes user input (2 numbers) and performs the selected algorithm
import sys
file_path = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects/password_generator.py"
sys.path.append(file_path)
from r"Cun's Projects" import password_generator 




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
def main():
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

    
