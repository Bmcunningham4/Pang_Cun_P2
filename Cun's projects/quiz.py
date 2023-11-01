import random
import sys

#! Need to get better with this shite...
file_path = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects/quiz_qna.py" 
sys.path.append(file_path)


from quiz_qna import (
    question_1,
    question_2,
    question_3,
    question_4,
    question_5, 
    question_6,
    question_7
)


list_of_questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7]
random.shuffle(list_of_questions) 


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


def main():
    print("You have chosen to play the NBA themed quiz!")
    display_questions()
    

if __name__ == "__main__":
    main()
else:
    print() 

