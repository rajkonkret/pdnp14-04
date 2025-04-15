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

# nadpisanie elemntu w liście
lista[3] = "Roman"
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Roman', 'Maciek', 'Anna']

# dopisanie do listy na wskazanym indeksie
lista.insert(1, "Wojtek")
print(lista)
# ['Radek', 'Wojtek', 'Tomek', 'Zenek', 'Roman', 'Maciek', 'Anna']

lista.insert(15, 'Tadeusz')
print(lista)
# ['Radek', 'Wojtek', 'Tomek', 'Zenek', 'Roman', 'Maciek', 'Anna', 'Tadeusz']

# sprawdzenie indeksu dla elemntu
print(lista.index("Tadeusz"))
lista.append("Roman")
print(lista)
print(lista.index("Roman"))  # index numer 4

numer_anna = lista.index("Anna")
print(numer_anna)  # index 6

# usunięcie elemntu z listy po indeksie
lista.remove("Anna")
print(lista)

# usunięcie po indeksie
lista.pop(5)
print(lista)
# ['Radek', 'Wojtek', 'Tomek', 'Zenek', 'Roman', 'Tadeusz', 'Roman']
print(lista.pop(5))  # Tadeusz, zwraca usunięty element
print(lista)
# ['Radek', 'Wojtek', 'Tomek', 'Zenek', 'Roman', 'Roman']
print(lista.pop(-2))  # Roman
print(lista.pop())  # Roman  usunie ostatni element


