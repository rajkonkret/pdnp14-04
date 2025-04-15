# słownik - para klucz wartość
# {'user': 'Radek'}
# odpowiednik json
# klucze nie mogą się powtarzac

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(type(dictionary_1))  # <class 'dict'>
print(dictionary_1)  # {}

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 67
print(dictionary)  # {'imie': 'Radek', 'wiek': 67}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 67])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 67)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 67}

# wypisanie wartości
print(dictionary['imie'])  # Tomek
# print(dictionary['Imie']) # KeyError: 'Imie'

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

dictionary.update({'data': "31-12-2025"})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 67, 'data': '31-12-2025'}

dict_small = {"x": 2}
print(dict_small)  # {'x': 2}
dict_small.update([("y", 3), ("z", 8)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 8}

# input() - pozwala wprowadzic dane do komputera np.: z klawiatury
# tekst = input("Podaj imię")
# print(tekst)
# Podaj imięRadek
# Radek

# napisac aplikację kalkulator
# pobrac liczby
# wyswietlic wynik działania (+)
# a = int(input("podaj pierwszą liczbę")) # str
# b = input("podaj drugą liczbę")
# print(a + float(b))

# napisac aplikacje pol_ang
pol_ang = {"kot": "cat", "pies": "dog", "dach": "roof"}
print(f'znam takie słowa: {pol_ang.keys()}')
odp = input("Podaj słowko do przetłumaczenia")
# print(pol_ang[odp.strip().lower()])
print(pol_ang.get(odp.strip().lower(), "Nie mo"))

name1 = "GROSS"
name2 = "groẞ"
print(name1.lower() == name2.lower())  # False
print(name1.casefold() == name2.casefold())  # True

print(ord("ẞ"))  # 7838 kod znaku ẞ
