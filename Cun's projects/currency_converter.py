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

import sys

#! Need to get better with this shite...
file_path = r"/Users/bencunningham/Documents/GitHub/Pang_Cun_P2/Cun's projects/quiz_qna.py" # raw string bby to account for space and '
sys.path.append(file_path)

# Ohhhhhh The reason you do this is because then you don't have to use the file name each time..
from quiz_qna import (
    question_1,
    question_2,
    question_3,
    question_4,
    question_5, 
    question_6,
    question_7
)



