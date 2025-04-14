# kolekcje - przechowuja wiele elementów, różnych typów na raz

# lista -  przechowuja wiele elementów, różnych typów na raz
# zachowuje kolejnosc przy dodawaniu danych

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Emilia")
lista.append("Maciek")
lista.append("Anna")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Emilia', 'Maciek', 'Anna']
#     0         1       2         3         4        5
#     -6        -5      -4        -3        -2       -1
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Maciek

# print(lista[10]) # IndexError: list index out of range

# ['Radek', 'Tomek', 'Zenek', 'Emilia', 'Maciek', 'Anna']
#     0         1       2         3         4        5
#     -6        -5      -4        -3        -2       -1
print(len(lista))  # długosć listy
print(lista[len(lista) - 1])  # Anna
print(lista[-1])  # Anna
print(lista[-2])  # Maciek
print(lista[-3])  # Emilia

# slicowanie - fragment listy
print(lista[0:3])  # 012, ['Radek', 'Tomek', 'Zenek']
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Emilia', 'Maciek', 'Anna']
print(lista[2:5])  # ['Zenek', 'Emilia', 'Maciek']

print(lista[2:15])  # ['Zenek', 'Emilia', 'Maciek', 'Anna']
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Emilia', 'Maciek', 'Anna']
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']
print(lista[10:234])  # []

# ['Radek', 'Tomek', 'Zenek', 'Emilia', 'Maciek', 'Anna']
#     0         1       2         3         4        5
#     -6        -5      -4        -3        -2       -1
print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # [0:4] |# ['Radek', 'Tomek', 'Zenek', 'Emilia']

lista_15 = list(range(15))  #
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # [start:stop:krok] [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(lista[::2])  # ['Radek', 'Zenek', 'Maciek']

print(lista[::-1])
# wyświetla odwróconą listę
# ['Anna', 'Maciek', 'Emilia', 'Zenek', 'Tomek', 'Radek']
