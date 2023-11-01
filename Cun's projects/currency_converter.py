import sys
from password_generator import get_integer_input
file_path = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects/currency_data.py"
sys.path.append(file_path)
from currency_data import currency_conversions

countries_list = []
currency_list = []
abrev_list = []
numbers_list = list(range(1,23))
for country in range(1, 23):
    countries_list.append(currency_conversions[country][4])
    currency_list.append(currency_conversions[country][3])
    abrev_list.append(currency_conversions[country][1])

country_currency = list(zip(numbers_list, countries_list, currency_list, abrev_list))
# print(country_currency)
for cuz in country_currency:
    # print(cuz)
    pass
    

def aussie_converter(amount, num): 
    ratio = currency_conversions[num][2]
    abrev2 = currency_conversions[num][1]
    country2 = currency_conversions[num][4]
    country_type = currency_conversions[num][3]

    new_amount = round(amount * ratio, 2)
    print(f"Aussie Dollar conversion to {country2} {country_type}")
    return f"{amount} AUD => {new_amount} {abrev2} "

def convert_to_aussie(amount, num):
    ratio = currency_conversions[num][2]
    abrev2 = currency_conversions[num][1]
    country2 = currency_conversions[num][4]
    country_type = currency_conversions[num][3]

    new_amount = round(amount / ratio, 2)
    print(f"{country2} {country_type} conversion to Aussie Dollar ")
    return f"{amount} {abrev2} => {new_amount} AUD "

def diff_to_diff(amount, num1, num2):
    ratio1 = currency_conversions[num1][2]
    ratio2 = currency_conversions[num2][2]


    abrev1 = currency_conversions[num1][1]
    abrev2 = currency_conversions[num2][1]

    country1 = currency_conversions[num1][4]
    country2 = currency_conversions[num2][4]
    country_type1 = currency_conversions[num1][3]
    country_type2 = currency_conversions[num2][3]

    aussie_amount = amount / ratio1
    new_amount = round(aussie_amount * ratio2, 2)

    print(f"{country1} {country_type1} conversion to {country2} {country_type2}")
    return f"{amount} {abrev1} => {new_amount} {abrev2}"


def print_menu():
    print("""You have chosen to use the currency converter!! 💸💶 #? Probs get rid of that ayy
                    
Please select from one of the following options:
    - Press (1) To convert from Australian dollars to another currency.
    - Press (2) To convert from another currency to Australian dollars.
    - Press (3) To convert between any other 2 currencies.
        
    Or if you would like to exit press (0)
    """)
    return ""

def valid_choice(prompt):
    while True:
        user_cuz = get_integer_input(prompt)
        if user_cuz in range(1, 23):  
            return user_cuz
        else:
            print("Please enter a valid choice from 1 to 22", '\n')

def valid_amount(prompt):
    while True:
        user_money = get_integer_input(prompt)
        if user_money >= 0:
            return user_money
        else:
            print("Invalid input. You must enter a positive number!", '\n')    
            
        

#! Yo pang should, I remove the brackets at the and or keep?
def show_currencies():
    print("""
1)  United States (Dollar)      12) South Korea (Won)
2)  European Union (Euro)       13) Mexico (Peso)
3)  United Kingdon (Pound)      14) Brazil (Real)
4)  Canada (Dollar)             15) Russia (Ruble)
5)  New Zealand (Dollar)        16) South Africa (Rand)
6)  Japan (Yen)                 17) Sweden (Krona)
7)  Switzerland (Franc)         18) Norway (Krone)
8)  China (Yuan)                19) Denmark (Krone)
9)  Hong Kong (Dollar)          20) Poland (Zloty)
10) Singapore (Dollar)          21) Cunland (Cunbucks)
11) India (Rupee)               22) Monopoly Money (Monpoly Dollaz)
          """)

def main():
    print_menu()

    while True:
        print()
        user_input = get_integer_input("Select which currency converter setting you would like to use here: ")

        if user_input == 0:
            break

        elif user_input == 1:
            show_currencies()

            user_currency = valid_choice("Enter the number of the currency you would like to convert to: ")
            user_amount = valid_amount("Enter the amount you would like to convert: ")
            print()

            print(aussie_converter(user_amount, user_currency))
        
        elif user_input == 2:
            show_currencies()

            user_currency = valid_choice("Enter the number of the currency you would like to convert from: ")
            user_amount = valid_amount("Enter the amount you would like to convert: ")
            print()

            print(convert_to_aussie(user_amount, user_currency))
            
        elif user_input == 3:
            show_currencies()

            user_currency1 = valid_choice("Enter the number of the currency you would like to convert from: ")
            user_currency2 = valid_choice("Enter the number of the currency you would like to convert to: ")
            user_amount = valid_amount("Enter the amount you would like to convert: ")
            print()

            print(diff_to_diff(user_amount, user_currency1, user_currency2))

        else:
            print(f"Sorry {user_input} is not a valid choice. Please try again!")


if __name__ == "__main__":
    main()

else:
    print()