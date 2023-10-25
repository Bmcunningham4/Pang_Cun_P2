user_decision = input("Would you like to keep using the password generator? (y/n) ")
        new_decision = user_decision.lower()
        if new_decision == "y":
            pass
        elif new_decision == "n":
            break
        else:
            print("That is not a valid choice select y for yes or n for no!")