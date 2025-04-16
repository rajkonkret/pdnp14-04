# pętle - możliwośc wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

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
