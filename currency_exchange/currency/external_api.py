import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"


def get_exchange_rates():
    response = requests.get(API_URL)
    return response.json()


def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()
    if from_currency not in rates['rates'] or to_currency not in rates['rates']:
        raise ValueError("Invalid currency code")

    converted_amount = amount * (rates['rates'][to_currency] / rates['rates'][from_currency])
    return converted_amount