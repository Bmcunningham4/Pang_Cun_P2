
#! Example currency converter!! so I can understand how it works..

import requests

# Define your API key and the API URL
api_key = 'YOUR_API_KEY'  # Replace with your actual API key
api_url = 'https://api.apilayer.com/exchangerates_data/latest'

# Function to fetch exchange rates
def get_exchange_rates(base_currency='USD'):
    params = {'base': base_currency, 'apikey': api_key}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        print('Failed to fetch exchange rates.')
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)
    if rates:
        if to_currency in rates:
            converted_amount = amount * rates[to_currency]
            return converted_amount
        else:
            print(f"Conversion from {from_currency} to {to_currency} is not supported.")
    return None

# Main program
if __name__ == '__main__':
    from_currency = 'USD'
    to_currency = 'EUR'
    amount = 100

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

