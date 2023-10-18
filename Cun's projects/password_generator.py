
# Password generator ideas: 
"""
#! Have the password specifications for each function above, eg. random 10 letter passwords
? Maybe have a password generator class and then diff generation functions, so you pick which one you want to use..

? Diff function ideas: (4 should be plenty!)
- Random combo for n length
- Random generation where you chose the total length and how many numbers and characters you want in it?
- Give a password and it converts it a certain format to at least include 1 upper character and 1 punct symbol:
    eg. input mango output: Mango6
- Generate a list of n passwords to pick from

"""

import string
import random

class PasswordGenerator:

    #Need these as attributes within class
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
    def password_2(self, length, capitals, numbers, punct): # Note on this for every number total length greater than (cap+num+punct) will assing a non-capital letter!
        password = []
        new_length = length - capitals - numbers - punct
        if new_length < 0:
            return f"Your password lenth must be longer than {length}, for these parameters!"
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
        string_test = all(char in self.full_alphabet for char in stringy) #? Making sure valid string to begin with..
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
            print(f"{stringy} is not a valid string, must contain only letters!. eg mango..")  
        return new_pass

    # Password gen 4: Generates n passwords of lenght m
    def password_4(self, how_many, length):
        passwords = []
        for i in range(how_many): 
            password = self.password_1(length)
            passwords.append(password)
        return passwords #? Ideally I'd rather these passwords be iterated like on list with here are your n passwords of lenth m: (but this will have to do..)

#? Testing station...    (all working ✅)
test1 = PasswordGenerator()
print(test1.password_1(8))
print(test1.password_2(10, 3, 3, 3))
print(test1.password_3("mango")) #? This method is classic lol
print(test1.password_3("mangosfordays"))
print(test1.password_4(4, 8))
