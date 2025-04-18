import requests

# pip install reuests
url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"

response = requests.get(url)
print(response)  # <Response [200]>
# 200 - ok
# 3xx - przekierowania
# 4xx - 404 - bład url, 400 Bad request - bład parametru
# 5xx błedy serwera 500 internal server error

print(response.text)  # odczytanie jsona
data = response.json()  # dostaniemy słownik
print(type(data))  # <class 'dict'>
# print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '076/A/NBP/2025', 'effectiveDate': '2025-04-18', 'mid': 3.7661}]}
print(data.keys())  # dict_keys(['table', 'currency', 'code', 'rates'])
print(data['rates'])
print(data.get('rates'))
# [{'no': '076/A/NBP/2025', 'effectiveDate': '2025-04-18', 'mid': 3.7661}]
print(data['rates'][0])  # pierwszy element z listy
# {'no': '076/A/NBP/2025', 'effectiveDate': '2025-04-18', 'mid': 3.7661}
print(data['rates'][0]['mid'])  # 3.7661
