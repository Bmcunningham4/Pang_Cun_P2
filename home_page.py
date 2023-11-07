import sys

file_path1 = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects"
file_path2 = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Pang's projects"
 
sys.path.append(file_path1)
sys.path.append(file_path2)

from Cuns_projects import password_generator 
from Cuns_projects import ATM                
from Cuns_projects import currency_converter 
from Cuns_projects import quiz
# import calculator
# import madLib
# import numGuess

def print_home_menu():
    print("""Welcome to Pand & Cun's App Oasis !! :)
                    
Please select the number of which app you would like to use!
    - (1) Password Generator
    - (2) ATM
    - (3) NBA themed quizgame
    - (4) Currency Coverter
    - (5) Madlib
    - (6) Calculator
    - (7) Number Guessing Game
        
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
    print_home_menu()

    while True:
        print_home_menu()
        print()                      
        user_input = get_integer_input1("Enter the app number here: ")

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
            # madLib.main()
            pass

        elif user_input == 6:
            # calculator.main()
            pass

        elif user_input == 7:
            # numGuess.main()
            pass


        else:
            print(f"Sorry {user_input} is not a valid choice. Please try again!")


if __name__ == "__main__":
    main_main()
else: 
    print("Why would I import this somewhere else..")


