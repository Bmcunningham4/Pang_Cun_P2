import time

class ATM:
    max_attempts = 3
    cun_balance = 5000000
    pang_balance = -50

    def __init__(self):
        self.incorrect_attempts = 0 
        self.whos_account = None

    def check_pin(self):
        for i in range(3):
            pin = float(input("Please enter your 4-digit pin: "))
            if pin == 1234 or pin == 3333:
                break
            else:
                self.incorrect_attempts += 1
                print("That pin is incorrect. Please try again...")  

        if pin == 1234:
            print("Welcome to your account Mr. Pang")
            self.whos_account = "Pang's account"   

        elif pin == 3333:
            print("Welcome to your account King")
            self.whos_account = "King's account"

        if self.incorrect_attempts == self.max_attempts:
            print()
            print("Incorrect password too many times!! This ATM will now self-destruct in 5 seconds..")
            for i in range(5, 0, -1):
                print(i)
                time.sleep(1)
            print("BOOOOOOM 🧨🎉")

    def view_balance(self):
        self.check_pin() 
        account_balance = 0 # If you don't include this, causes error after 3 wrong attempts

        if self.whos_account == "Pang's account":
            print(f"The balance of Pang's account is ${self.pang_balance}")
            account_balance = self.pang_balance
        elif self.whos_account == "King's account":
            print(f"The balance of the King's account is ${self.cun_balance}")
            account_balance = self.cun_balance

        return account_balance 

# Testing station...
bens_test = ATM()
print(bens_test.view_balance())
