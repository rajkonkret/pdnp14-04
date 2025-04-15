# krotka, tupla - niemutowalna lista
# pozwala efektywniej zarzadzac pamięcią
# moze symulowac stałe

tupla_imiona = ("Radek", "Tomek", 'Zenek', "Mateusz")
print(tupla_imiona)
print(type(tupla_imiona))
# ('Radek', 'Tomek', 'Zenek', 'Mateusz')
# <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)
print(type(tupla_liczby))

tupla = 43
print(type(tupla))  # <class 'int'>
tupla1 = (43)
print(type(tupla1))  # <class 'int'>

# tupla jednoelemntowa
tupla2 = 43,
print(type(tupla2))  # <class 'tuple'>

# PEP8 zaleca by w takich przypadkach uzywac nawiasów
tupla3 = (43,)
print(type(tupla3))

# tupla_liczby[3] = 123 # TypeError: 'tuple' object does not support item assignment
del tupla_liczby  # mozna usunąć całą tuplę
# print(tupla_liczby) # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona.index("Radek"))  # numer indexu 0
print(tupla_imiona.count("Radek"))  # występuje jeden raz

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>

a, b = 1, 2
print(a, b)  # 1 2

a, b = tup
print(a, b)  # 1 2

tup2 = 1, 2, 3
# a, b = tup2 # ValueError: too many values to unpack (expected 2)
a, *b = tup2  # * worek na dane
print(a, b)  # 1 [2, 3]

print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Mateusz')
# name1, name2, name3

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)
# Radek Tomek ['Zenek', 'Mateusz']
name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)
# Radek ['Tomek', 'Zenek'] Mateusz
*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)
# ['Radek', 'Tomek'] Zenek Mateusz

# sortowani etupli zwraca liste
print(sorted(tupla_imiona))
# ['Mateusz', 'Radek', 'Tomek', 'Zenek']
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Mateusz')
print(type(tupla_imiona))  # <class 'tuple'>
print(type(sorted(tupla_imiona)))  # <class 'list'>
