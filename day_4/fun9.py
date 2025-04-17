# funkcja lambda
# skrocona forma funkcji
# domyslnie return

def odejmij(a, b):
    return a - b


print(odejmij(7, 90))  # -83

odejmij2 = lambda a, b: a - b
print(odejmij2(3, 4))

# przerobic na lambde
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie
lista = [1, 2, 3, 4, 24, 50, 100, 500]
l = []
for i in lista:
    l.append(i * 2)
print(l)

print([i * 2 for i in lista])


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))

print(l2)  # [2, 4, 6, 8, 48, 100, 200, 1000]

# funkcje wyzszego rzędu

# map() - bierze kolejne elementy i wykonuje na nich funkcje
print(f"Zastosowanie funkcji map() {list(map(zmien, lista))}")
#  Zastosowanie funkcji map() [2, 4, 6, 8, 48, 100, 200, 1000]

# lambda jako funkcja anonimowa - uzycie w miejscu deklaracji
print(f"Zastosowanie funkcji map() {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie funkcji map() {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie funkcji map() {list(map(lambda x: x * 8, lista))}")
print(f"Zastosowanie funkcji map() {list(map(lambda x: x * 5, lista))}")
# Zastosowanie funkcji map() [2, 4, 6, 8, 48, 100, 200, 1000]
# Zastosowanie funkcji map() [2, 4, 6, 8, 48, 100, 200, 1000]
# Zastosowanie funkcji map() [4, 8, 12, 16, 96, 200, 400, 2000]
# Zastosowanie funkcji map() [8, 16, 24, 32, 192, 400, 800, 4000]
# Zastosowanie funkcji map() [5, 10, 15, 20, 120, 250, 500, 2500]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)

# filter()
print(f"Zastosowanie filter() {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter() [1, 2]
print(f"Zastosowanie filter() {list(filter(lambda x: x > 3, lista))}")  # Zastosowanie filter() [4, 24, 50, 100, 500]
print(f"Zastosowanie filter() {list(filter(lambda x: x > 100, lista))}")  # Zastosowanie filter() [500]
print(
    f"Zastosowanie filter() {list(filter(lambda x: x > 20 and x < 200, lista))}")  # Zastosowanie filter() [24, 50, 100]
print(f"Zastosowanie filter() {list(filter(lambda x: 20 < x < 200, lista))}")  # Zastosowanie filter() [24, 50, 100]
