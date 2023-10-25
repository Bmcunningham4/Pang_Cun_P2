
#! Password Generator: To fix list:
"""
- Add user interface
"""

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
            print(f"{stringy} is not a valid string, must contain only letters!. eg mango..")  
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

#! All working beautifully..    (all working ✅)
test1 = PasswordGenerator()
print(test1.password_1(12))
print(test1.password_2(1, 3, 3, 3))
print(test1.password_3("mango")) 
print(test1.password_4(3, 8))
