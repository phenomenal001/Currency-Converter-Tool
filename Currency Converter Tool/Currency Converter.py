import requests
import pycountry

API_KEY = 'fca_live_QiRD4yaE7K1aJQIAfVLojfu8J2KPxSXPYkDxxTzc'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD","CAD","EUR","AUD","CNY","INR"]

# CURRENCIES = list(map(lambda x: x.alpha_3, pycountry.currencies))


# CURRENCIES_LIST = []
# list_data = (list(pycountry.currencies))
# for a in list_data:
#     CURRENCIES_LIST.append(a.alpha_3)

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except:
        print("Invalid Currency")
        return None

while True:
    base = input(f"Enter the base currency from the given list {CURRENCIES} OR (Q for Quit):").upper()   

    if base == "Q":
        print("Thank you")
        break
    elif base not in CURRENCIES:
        pass

    data = convert_currency(base)

    if not data:
        continue

    for tricker, value in data.items():
        print(f"{tricker}:{value}")