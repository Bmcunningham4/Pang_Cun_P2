# Key features/ ideas that my glashcard quiz game must have...
#! Overall could add diff quizzes to play, but this isn't flashcards it's just a quiz game which is ok...
"""
? Need
- User interface 
- scoring system
- randomization so it's not boring in same order every time..
- end of game summary
? optional
- timer (probs not)
- question answer storage (probs only needed if I was making it a big thing..)
- ability to make flashcards instead of just being quizzed but probs too complicated..
- Ability to chose what quiz game you want to play eg. have diff ones!..

? Note:
- I think it would be easier if I had the answers just in variables downn the page but its better dictionary practice if I have them stored in dicts..
"""

import random
import sys

#! Need to get better with this shite...
file_path = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects/quiz_qna.py" # raw string bby to account for space and '
sys.path.append(file_path)

# Ohhhhhh The reason you do this is because then you don't have to use the file name each time..
from quiz_qna import (
    question_1,
    question_2,
    question_3,
    question_4,
    question_5, 
    question_6,
    question_7
)

print("Welcome to my lit NBA themed Quiz... Yew")

list_of_questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7]
random.shuffle(list_of_questions) # You don't assign this to a variable just do it in place...


def display_questions():
    q_number = 0
    num_correct = 0 

    for question in list_of_questions:
        q_number += 1
        print()
        print(f"Question {q_number}:")
        print(question["question"])
        options = question["options"]

        num = 0
        for option in options:
            letter = ["A", "B", "C"]
            print(letter[num], option)
            num += 1

        print()
        user_answer = input("Enter: A, B or C: ").upper()
        correct_ans = question["correct_answer"]

        while user_answer not in ["A", "B", "C"]:
            print(f"{user_answer} is not a valid input, please chose again..")
            user_answer = input("Enter: A, B or C: ").upper()

        if user_answer == question["correct_answer"]:
            num_correct += 1
            print("Correct!")
        else:
            print(f"Incorrect!! Option {correct_ans} was the correct answer")

    print()
    print("RESULTS")
    print(f"You scored {num_correct} / 7!!")      
    percent = round(num_correct * 100 / 7, 2)
    print(f"That is {percent}% correct! Woooo")

display_questions()

# print(question_1["correct_answer"])


