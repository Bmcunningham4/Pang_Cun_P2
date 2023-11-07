#Random Number Guessing Game! Guess a number between 1-100. The computer will say 'Too high!' or 'Too low!' until you guess the correct number. Good luck!!!

import random 

#! Function defining the game where a random number between 1 and 100 is chosen. User attempt counter set at 0
def main():
    secret_num = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Pangsta's awesome number guessing game!!")
    print("I've chosen a number between 1 and 100...can you guess it?", '\n')

    while True:
        try:
            user_guess = int(input("Guess the number: "))
            attempts += 1

            if user_guess < secret_num:
                print("Too Low! Try again", '\n')
            elif user_guess > secret_num:
                print("Too High! Try again", '\n')
            else:
                print(f"Correct! Well done! You guessed the correct number in {attempts} attempts", '\n')
                break
        except ValueError:
            print("Invalid input. Please enter a valid number", '\n')

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        print()
        main()
    else:
        print("Thanks for playing! Come back soon :)", '\n')

if __name__ == "__main__":
    main()
