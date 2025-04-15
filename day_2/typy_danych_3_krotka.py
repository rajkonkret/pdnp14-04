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
