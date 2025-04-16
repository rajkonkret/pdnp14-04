from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2025-04-16
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-04-16 13:00:22.605871

print(time.year)  # 2025
print(today.day)  # 16

# tomorrow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2025-04-17

formated_data = datetime.now().strftime("%d/%m/%Y")
print(formated_data)  # 16/04/2025

# 13:07
formated_time = datetime.now().strftime("%H:%M")
print(formated_time)
print(formated_time.removeprefix("0"))
print(type(formated_time))  # <class 'str'>

object_datetime = datetime.now().strptime("16/04/2025", "%d/%m/%Y")
print(object_datetime)  # 2025-04-16 00:00:00
print(type(object_datetime))  # <class 'datetime.datetime'>

print("-------------------")
products = [
    {"sku": 1, "exp_date": today, "price": 200},
    {"sku": 2, "exp_date": today, "price": 100},
    {"sku": 3, "exp_date": tomorrow, "price": 250.00},
    {"sku": 4, "exp_date": today, "price": 75.99},
    {"sku": 5, "exp_date": today, "price": 199},
]

for product in products:
    # print(product)  # {'sku': 5, 'exp_date': datetime.date(2025, 4, 16), 'price': 199}
    # print(product['exp_date'])
    if product['exp_date'] != today:  # != różne
        continue
    product['price'] *= 0.8  # p = p * 0.8
    print('Zmiana ceny')
    print(f"""
Price for sku {product['sku']}
is now {product['price']}""")
# -------------------
# Zmiana ceny
#
# Price for sku 1
# is now 160.0
# Zmiana ceny
#
# Price for sku 2
# is now 80.0
# Zmiana ceny
#
# Price for sku 4
# is now 60.792
# Zmiana ceny
#
# Price for sku 5
# is now 159.20000000000002