import requests
import json


data = requests.get("http://data.fixer.io/api/latest?access_key=dd1fe6ba8204f8db1ecb6cf55c60976a&format=1")

parsed = json.loads(data.text)
rates = parsed['rates'].items()
date = parsed['date']
print(" \t \t -----------------------------RATES--------------------------------------\n")
print("This are the rates of Euros to different currencies  on date " + str(date) +"\n")
for currency, items in rates:
    print(currency,items)