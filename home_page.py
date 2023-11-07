
#! Goat
from Cuns_projects import password_generator, ATM, currency_converter, quiz         
from Pangs_projects import calculator, madLib, numGuess

def print_home_menu():
    print("""
-------------------------------------------------------------          
Please select the number of which app you would like to use!
    - (1) Password Generator
    - (2) ATM
    - (3) NBA themed quizgame
    - (4) Currency Coverter
    - (5) Madlib
    - (6) Calculator
    - (7) Number Guessing Game
-------------------------------------------------------------        
    Or if you do not wish to use this App Oasis, press (0)
    """)
    return ""

def get_integer_input1(prompt):
    while True:
        user_input = input(prompt)
        try:
            integer_input = int(user_input)
            return integer_input
        except ValueError:
            print(f"Invalid input. Please enter a valid integer.")
            print()


def main_main():
    print("Welcome to Pand & Cun's App Oasis !! :)")

    while True:
        print_home_menu()
        print()                      
        user_input = get_integer_input1("Enter the app number here: ")
        print()

        if user_input == 0:
            print()
            print("Thank you for using our App Oasis, We hope you enjoyed !!")
            break

        elif user_input == 1:
            password_generator.main()

        elif user_input == 2:
            ATM.main()

        elif user_input == 3:
            quiz.main()

        elif user_input == 4:
            currency_converter.main()

        elif user_input == 5:
            madLib.main()

        elif user_input == 6:
            calculator.main()

        elif user_input == 7:
            numGuess.main()

        else:
            print(f"Sorry {user_input} is not a valid choice. Please try again!")


if __name__ == "__main__":
    main_main()
else: 
    ""


