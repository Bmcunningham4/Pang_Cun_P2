
# Password generator ideas: 
"""
#! Have the password specifications for each function above, eg. random 10 letter passwords
- Function to chose parameters eg. how many numbers, how many letters etc..
- Nested function to generate multiple passwords
- Give a password and add things to it so it meats certain requirements eg. # of special characters..
"""

import string
import random


lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
alphabet = string.ascii_letters

digits = string.digits
punctuation = string.punctuation


# Description... (undecided)
def make_simple_password(x):
    password = ""
