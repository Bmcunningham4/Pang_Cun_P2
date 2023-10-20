#Key features/ required components:
"""
? Essential:
- Connected to live currencies
- Can pick which currency you want to convert and the amount
- Need a function to fetch specific currencies
- And then a diff function to do the maths conversion!...\

? Optional:
- If I can't figure out how to connect to API, then use monopoly money and cun bucks as examples as well as some real googled ones...

? Apaz best to fetch live rates from one of these API's..
- Open Exchange Rates
- Fixer.io
- CurrencyLayer
- ExchangeRatesAPI.io
"""
# from forex_python.converter import CurrencyRates #? This would be ideal from Github but can't figure out 
"""Didn't work in the end and not worth getting a free trial anywhere..
api_key = "9341f1a55ff4fa63421f6a94951ef547"
api_url = "https://fixer.io/dashboard"
import requests
"""

#! Need to get better with this shite...
import sys
file_path = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects/currency_data.py" # raw string bby to account for space and '
sys.path.append(file_path)
from currency_data import currency_conversions

#? All this crap is so I can print for the menu (Even tho could've just used dict.. )
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

#? Now getting into it..

def aussie_converter(amount, num): # (Num of what new currency you want)
    ratio = currency_conversions[num][2]
    abrev2 = currency_conversions[num][1]
    country2 = currency_conversions[num][4]
    country_type = currency_conversions[num][3]

    new_amount = round(amount * ratio, 2)
    print(f"Aussie Dollar conversion to {country2} {country_type}")
    return f"{amount} AUD => {new_amount} {abrev2} "

#! Instead of copy and pasting this code I could have a conditional statement that choses whether to convert to or from!!
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

# Test station #! Just need to add in error handling!!
hey = diff_to_diff(50, 3, 21)
print(hey)
print()

hi5 = convert_to_aussie(100, 3)
print(hi5)
print()


hi = aussie_converter(100, 3)
print(hi)
hi4= aussie_converter(100000, 21)
print(hi4)



