
#todo: Changes to add: Exit message?
import time
from password_generator import get_integer_input

#! Pang's password is 1234
#! Cun's password is 3333

class ATM:
    max_attempts = 3
    cun_balance = 5000000
    pang_balance = -50
    atm_function = 0 #? Clutch

    def __init__(self): 
        self.incorrect_attempts = 0 
        self.whos_account = None 

    def check_pin(self):
        pin = None #? Good old pre-assign saving the day..
        for i in range(3):
            try: #? Usually not ideal to have try except blocks within the functions but ah well desperate times..
                pin = int(input("Please enter you 4 digit pin before continuing: "))
            except:
                print("Invalid input, please enter your 4-digit numeric pin.",'\n')
                
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
        return "\n" #? That doesn't change anything for some reason...
    
    def atm_function(self):
        if self.whos_account == "King's account" or self.whos_account == "Pang's account":
            atm_funct = 1
            return atm_funct
        else:
            atm_funct = 0
            return atm_funct
        
    def view_balance(self):
        if self.whos_account == "Pang's account":
            print(f"The balance of Pang's account is ${self.pang_balance}")
        elif self.whos_account == "King's account":
            print(f"The balance of the King's account is ${self.cun_balance}")

        return ""

    def deposit(self, amount):
        if amount >= 0:
            if self.whos_account == "Pang's account":
                self.pang_balance += amount
                return self.pang_balance
            elif self.whos_account == "King's account":
                self.cun_balance += amount
                return self.cun_balance
        else:
            print("You must deposit a positive amount!")

    def withdraw(self, amount): 
        if amount >= 0:
            if self.whos_account == "Pang's account":
                if amount > self.pang_balance:
                    print("Insufficient funds broke boy..")
                else:
                    self.pang_balance -= amount
                    return self.pang_balance #? Do I need to be returning the balances here?
            elif self.whos_account == "King's account":
                if amount > self.cun_balance:
                    print("insufficicient funds broke king..")
                else:
                    self.cun_balance -= amount
                    return self.cun_balance
        else:
            print("You must withdraw a positive amount!")

def print_menu1():
    print("You have chosen to use the ATM!!", '\n')
    return ""

def print_menu2():
    print("""
                    
Please select from one of the following options:
    - Press (1) To view you balance.
    - Press (2) To make a deposit.
    - Press (3) To make a withdrawal.
        
    Or if you would like to exit press (0)
    """)
    return ""


def main():
    print_menu1()
    test = ATM() 
    test.check_pin()

    atm_functioning = test.atm_function() 
    if atm_functioning == 1:
        print_menu2()

        while True:
            print()                      
            user_input = get_integer_input("Select which ATM option you would like to use: ")

            if user_input == 0:
                break

            elif user_input == 1:
                test.view_balance()

            elif user_input == 2:
                deposit_amount = get_integer_input("How much would you like to deposit? ")
                test.deposit(deposit_amount)
                
            elif user_input == 3:
                withdraw_amount = get_integer_input("How much would you like to withdraw? ")
                test.withdraw(withdraw_amount)
                
                
            else:
                print(f"Sorry {user_input} is not a valid choice. Please try again!")
    else:
        pass 


if __name__ == "__main__":
    main()
else:
    print()