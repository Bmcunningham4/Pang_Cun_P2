
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

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
full_alphabet = string.ascii_letters

digits = string.digits
punctuation = string.punctuation

#todo: When I comeback turn this into a class then make next 2!
# Password generator 1: Generates password of length n
def password_1(length):
    password = ""
    for i in range(length):
        password += random.choice(full_alphabet + digits + punctuation)
    return password

bens_pw = password_1(10)
print(bens_pw)

# Password generator 2: Chose total length, how many capitals, numbers and punctuation characters you want
def password_2(length, capitals, numbers, punct): # Note on this for every number total length greater than (cap+num+punct) will assing a non-capital letter!
    password = []
    new_length = length - capitals - numbers - punct
    if new_length < 0:
        return f"Your password lenth must be longer than {length}"
    for i in range(new_length):
        password.append(random.choice(lower_alphabet))
    for i in range(capitals):
        password.append(random.choice(upper_alphabet))
    for i in range(numbers):
        password.append(random.choice(digits))
    for i in range(punct):
        password.append(random.choice(punctuation))
    
    random.shuffle(password) #? This is a clutch addition
    new_password = "".join(password)
    return new_password

bens_2 = password_2(6,1,1,1)
print(bens_2)
