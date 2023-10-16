
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
alphabet = string.ascii_letters

digits = string.digits
punctuation = string.punctuation


# Password generator 1: Generates password of length n
def make_simple_password(length):
    password = ""

