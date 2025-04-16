# pętle - możliwośc wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(5):  # 0 do 4
    print(i)

for i in range(5):
    pass  # nic nie rob

for _ in range(5):  # niema zmienna
    print("Test podłoga")
    print(_)

for i in range(10):
    print(i * 2)
    print(i + 2)

# przerobic lotto na wylosowanie 6 liczb. uzyc pętli
lista_kule = list(range(1, 50))
lista_wyn = []

for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wyn.append(wyn)

print(lista_wyn)  # [14, 11, 23, 4, 19, 6]

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:
    if c > 4:
        print("Większe od 4")
    else:
        print("Mniejsze, równe 4")
# Mniejsze, równe 4
# Mniejsze, równe 4
# Mniejsze, równe 4
# Większe od 4
# Większe od 4

for i in range(0, 10, 2):  # start, stop, krok, krok co 2
    print(i)
# 0
# 2
# 4
# 6
# 8
for i in range(-10, 0):
    print(i)

for i in range(10, 0, -1):  # krok ujemny
    print(i)

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)  # gdy warunek spełniony
    print('Przy kazdym przejsciu pętli')
# Przy kazdym przejsciu pętli
# 3
# Przy kazdym przejsciu pętli
# Przy kazdym przejsciu pętli
# Przy kazdym przejsciu pętli
# Przy kazdym przejsciu pętli

imiona = ["Radek", 'Tomek', "Zenek", "Ania"]
print(imiona)
print(type(imiona))
# ['Radek', 'Tomek', 'Zenek', 'Ania']
# <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek
for i in range(len(imiona)):
    print(i, imiona[i])
    # 0 Radek
    # 1 Tomek
    # 2 Zenek
    # 3 Ania

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - numeruje kolekcje i zwraca jej element i numer
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ["Radek", 'Tomek', "Zenek", "Ania", "Roman"]
wiek = [44, 55, 32, 27]

# Radek 44, różna długosc list
# for p in imiona:
#     print(p, wiek[imiona.index(p)]) # IndexError: list index out of range

# zip() - łączenie kolekcji w jedną
for i in zip(imiona, wiek):
    print(i)

for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Ania', 27))
(0, ('Radek', 44))

for a, b in enumerate(zip(imiona, wiek)):
    print(a, b)
# 0 ('Radek', 44)
# 1 ('Tomek', 55)
# 2 ('Zenek', 32)
# 3 ('Ania', 27)
# c,d = ('Radek', 44)
for a, (b, c) in enumerate(zip(imiona, wiek)):
    print(a, b, c)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Ania 27

zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x000002227FF0C2C0>

for i in zipped:
    print(i)
    # ('Radek', 44)
    # ('Tomek', 55)
    # ('Zenek', 32)
    # ('Ania', 27)
    # ('Roman', None)
# iterator działa raz
print(10 * "-")
for i, w in zipped:
    print(i, w)

print(10 * "-")
zipped = zip_longest(imiona, wiek, fillvalue=None)
zipped_list = list(zipped)
for i, w in zipped_list:
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27
# Roman None
