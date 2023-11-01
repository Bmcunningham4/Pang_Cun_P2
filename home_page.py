
#? Welcome to the App Oasis ahahhaahha
# Othe ideas for names.. 
""""
"App Switchboard"
"App Launcher"
"App Plaza"
"App Center"
"App Junction"
"App Navigator"
"App Hub Central"
"App Carousel"
"App Select"
"""

import sys

#? Get all my file paths!
file_path1 = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects"
file_path2 = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Pang's projects"
file_path3 = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects/password_generator.py"
 

#? Upload all filepaths...
sys.path.append(file_path1)
sys.path.append(file_path2)


#? Import all files
import password_generator #? Ohhhh this is only underlined right now because they haven't been used in my code yet!! 
import ATM                #! (Not true because even after use still yellow) ~ something fishy here..
import currency_converter
import quiz


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
    - (8) Weather App
        
    Or if you don't wish to use any of our app's type (I'm worried I'd have too much fun in here)
    """)
    return ""

#! Only doing this because I can't seem to figure out how to import it properly here UGHHHHHH
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
            # madlib.main()
            pass

        elif user_input == 6:
            # calculator.main()
            pass

        elif user_input == 7:
            # numGuess.main()
            pass

        elif user_input == 8:
            # weatherApp.main()
            pass

        else:
            print(f"Sorry {user_input} is not a valid choice. Please try again!")


if __name__ == "__main__":
    main_main()
else: 
    print("Why would I import this somewhere else..")


