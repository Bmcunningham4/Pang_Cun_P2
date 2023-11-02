
#! Password Generator: To fix list:
# - Exit message ?


import string
import random

class PasswordGenerator:

    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    full_alphabet = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    # Password generator 1: Generates password of length n
    def password_1(self, length):
        password = ""
        for i in range(length):
            password += random.choice(self.full_alphabet + self.digits + self.punctuation)
        return password


    # Password generator 2: Chose total length, how many capitals, numbers and punctuation characters you want
    def password_2(self, length, capitals, numbers, punct): # Note on this for every number total length greater than (cap+num+punct) will assign a non-capital letter!
        password = []
        new_length = length - capitals - numbers - punct
        min_length = capitals + numbers + punct

        if new_length < 0:
            return f"Your password length must be longer than {min_length}, with these parameters! (You selected a length of {length})"
        for i in range(new_length):
            password.append(random.choice(self.lower_alphabet))
        for i in range(capitals):
            password.append(random.choice(self.upper_alphabet))
        for i in range(numbers):
            password.append(random.choice(self.digits))
        for i in range(punct):
            password.append(random.choice(self.punctuation))
        
        random.shuffle(password) #? This is a clutch addition
        new_password = "".join(password)
        return new_password
    
    # Password gen 3: Turns a string into a password that meets these requirements: At least 8 characters, 1 capital & 1 punct symbol
    def password_3(self, stringy):
        string_test = all(char in self.full_alphabet for char in stringy) 
        new_pass = ""

        if string_test == True:
            new_pass = stringy.capitalize()
            if len(new_pass) < 8:
                extra_letters_needed = 8 - len(new_pass)
                for i in range(extra_letters_needed):
                    new_pass += random.choice(self.lower_alphabet)

            new_pass += random.choice(self.digits)
            new_pass += random.choice(self.punctuation)

        else:
            print(f"{stringy} is not a valid string, must contain only letters!. eg mango..")  #? I don't think this ever gets the chance to activate poor fella..
        return new_pass

    # Password gen 4: Generates n passwords of lenght m
    def password_4(self, how_many, length):
        passwords = []
        num_password = 0

        for i in range(how_many): 
            password = self.password_1(length)
            passwords.append(password)
        
        for password in passwords:
            num_password += 1
            print(f"Password option {num_password}: {password}")

        return ""

def print_menu():
    print("""You have chosen to use the password generator!! 👮‍♀️👩‍💻 #? Probs get rid of that ayy
                    
Please select from one of the following options:
    - Press (1) To generate a strong password your choice of length.
    - Press (2) To customise a password with your choice of: length, capitals, numbers and special characters.
    - Press (3) To turn any word into a strong password.
    - Press (4) To generate a list of passwords for you to choose from.
        
    Or if you would like to exit press (0)
    """)
    return ""

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            integer_input = int(user_input)
            return integer_input
        except ValueError:
            print(f"Invalid input. Please enter a valid integer.")
            print()

def main():
    print_menu()
    test1 = PasswordGenerator()

    while True:
        print()                         #? Or just "select here: " ??
        user_input = get_integer_input("Select which password generator mode you would like to use here: ")

        if user_input == 0:
            break
        elif user_input == 1:
            user_length = get_integer_input("What is the length of the password you would like to generate? ")
            print(test1.password_1(user_length))

        
        elif user_input == 2:
            user_length = get_integer_input("What is the length of the password you would like to generate? ")
            user_caps = get_integer_input("How many capital letters would you like? ")
            user_nums = get_integer_input("How many numbers would you like? ")
            user_punct = get_integer_input("How many special symbols would you like? ")
            print(test1.password_2(user_length, user_caps, user_nums, user_punct))
            
        #? this ones diff because I can't use the integer test... have to do a seperate string test
        elif user_input == 3:
            while True:
                user_word = input("What word would you like to turn into a strong password? ")
                if user_word.isalpha():
                    break
                else:
                    print(f"Sorry {user_word} is an invalid input, please try again!")

            print(test1.password_3(user_word))
            

        elif user_input == 4:
            pass
            user_length = get_integer_input("What is the length of the passwords you would like to generate? ")
            user_num = get_integer_input("How many passwords would you like to generate? ")
            print(test1.password_4(user_num, user_length))

        else:
            print(f"Sorry {user_input} is not a valid choice. Please try again!")

        #? This was only causing problems this shite and there's an option to exit anyway...
        """ user_decision = input("Would you like to keep using the password generator? (y/n) ")
        new_decision = user_decision.lower()
        while new_decision != "y" and new_decision != "n":
            print("That is not a valid choice. Select 'y' for yes or 'n' for no.")
            user_decision = input("Would you like to keep using the password generator? (y/n) ")
            new_decision = user_decision.lower()

        if new_decision == "y":
            pass
        elif new_decision == "n":
            pass"""


if __name__ == "__main__":
    main()
else: # Don't need this but ah well
    print()




#? Diff menu option is this better?:
"""
    menu_functions = {
        0: exit,
        1: generate_strong_password,
        2: customize_password,
        3: word_to_password,
        4: generate_password_list
    }
"""


