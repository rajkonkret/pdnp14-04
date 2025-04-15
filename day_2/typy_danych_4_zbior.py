# zbiór (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbiór
zb2 = set()
print(type(zb2))  # <class 'set'>
print(zb2)  # set()

# dodanie elemntów do zzbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop()
print(zbior.pop())  # usunie pierwszy element, 33

zmienna = zbior.pop()
print("Usnięto", zmienna)  # Usnięto 66

zbior_copy = zbior.copy()
print(zbior_copy)
print(zbior)
print(id(zbior))
print(id(zbior_copy))
# {18, 22, 24, 777, 11, 44}
# {777, 11, 44, 18, 22, 24}
# 1934325637280
# 1934325632800

# operacje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# część wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {24, 777, 22}
print(zbior.difference(zbior_2))  # {24, 777, 22}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łaczy zbiory
zbior.update(zbior_2)
print(zbior)  # zbior zostaje zmieniony !!!
# {777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62)

lista = list(zbior)
print(lista)  # [777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62]

# sprawdzenie czy dany element istnieje w kolekcji
print(667 in zbior)  # True
print(777 in lista)  # True
print(777 in krotka)  # True
