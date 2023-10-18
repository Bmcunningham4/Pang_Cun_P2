# Make a start on a lit atm from scratch don't be a hack and find an old one this should be easy money!

#* Needs to have functionality to do:  + extras!
"""
- Ability to view balance
- Deposit
- Withdraw
- View history? (only of instances until you exit loop)
? If I want to make more complicated, could inherit another class with extra features like:
- ability to exchange
- Make a new account/ transfer between accounts?

#* ahahah I'll make a pang account and a cun account with passwords and diff amounts..
"""
import time

#! Pang's password is 1234
#! Cun's password is 3333

class ATM:
    max_attempts = 3
    cun_balance = 5000000
    pang_balance = -50

    def __init__(self): #* Is this garbage really needed here..
        self.incorrect_attempts = 0 
        self.whos_account = None #* This shit seems to save the day for some reason..

    # Got very carried away with this one yikes..
    def check_pin(self):
        for i in range(3):
            pin = float(input("Please enter you 4 digit pin fam: "))
            if pin == 1234 or pin == 3333:
                break
            else:
                self.incorrect_attempts += 1
                print("That pin is incorrect please try again...")  

        if pin == 1234:
            print("Welcome to your account Mr. Pang")
            self.whos_account = "Pang's account"   

        elif pin == 3333:
            print("Welcome to your account King")
            self.whos_account = "King's account"

        if self.incorrect_attempts == self.max_attempts:
            print()
            print("Incorrect password too many times!! This ATM will now self destruct in 5 seconds..")
            for i in range(5, 0, -1):
                print(i)
                time.sleep(1)
            print("BOOOOOOM 🧨🎉")
        return ""
        
    #! This is slightly complicated need to have checked pin but don't want to call it again.. :(
    def view_balance(self):
        self.check_pin() 

        if self.whos_account == "Pang's account":
            print(f"The balance of Pang's account is ${self.pang_balance}")
        elif self.whos_account == "King's account":
            print(f"The balance of the King's account is ${self.cun_balance}")

        return ""

#? Testing station...
bens_test = ATM()
print(bens_test.view_balance())