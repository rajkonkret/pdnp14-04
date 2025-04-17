# funkcje zwracaję wynik
# kończy sie słówkiem return

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(dodaj(5, 6))
print(dodaj(6, 89))

print(odejmij(1, 2, 3))
print(odejmij(1, 2))
print(odejmij())

print(oblicz_vat(1000))
print(oblicz_vat(1000, 15))
print(oblicz_vat(vat=15, kwota=1000))  # 1150.0

zm = oblicz_vat(1000)
if zm == 1230:
    print("Ok")

print(dodaj(5, 6) + dodaj(4, 5)) # 20
