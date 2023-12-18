import requests

response = requests.get(
    "https://v6.exchangerate-api.com/v6/be775458e910695e6c8e31d8/latest/USD"
)

if response.ok == True:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]
    print("base: " + base)
    print("date: " + date)
    # print(rates)
# Nie działa trzeba się zarejestrować i otrzymać API Key

for key in rates:
    print(key + ": ", rates[key])
