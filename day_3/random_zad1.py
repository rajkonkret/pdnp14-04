import random

# operacje na liczbach losowych

# "Return random integer in range [a, b], including both end points.
print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # float 0.5886431029920096 od 0 do 0.99999999
print(random.random() * 8)  # 5.949150795937899 od 0 do 7.9999999

lista = [67, 45, 32, 68, 69, 90, 42]
print(random.choice(lista))  # wylosuje element z listy, 32
lista_wyn = []
lista_kule = list(range(1, 50))
# print(lista_kule)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
lista_wyn.append(wyn)
print(lista_wyn)

print(random.choices(lista_kule, k=6))  # [35, 25, 11, 25, 12, 31], z powtórzeniami
print(random.sample(lista_kule, 6))  # [44, 35, 32, 49, 12, 19]
print(random.sample(lista_kule, k=6))  # [27, 9, 25, 4, 20, 13]
