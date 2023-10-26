class ATM:
    max_attempts = 3
    cun_balance = 5000000
    pang_balance = -50
    atm_function = 1

    @classmethod #! Cheeky little class refresher for me wooooo
    def get_pang_balance(cls):
        cls.pang_balance = 11
        return cls.pang_balance

# Access pang_balance through a class method
pang_balance = ATM.get_pang_balance()

print(f"Pang's Balance: {pang_balance}")
