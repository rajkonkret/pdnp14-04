import sys

print()  # wypisz/wydrukuj
# ctrl alt l - formatowanie kodu wg zasad PEP8

print("Nazywam się Radek")
print('Nazywam sie Radek')
print('Nazywam sie Radek')
print('Nazywam sie Radek')
print('Nazywam sie Radek')
print('Nazywam sie Radek')
print('Nazywam sie Radek')
print('Nazywam sie Radek')
print('Nazywam sie Radek')
# ctrl d - powiela linie

# print("Nazywam się Radek')
#   File "C:\Users\CSComarch\PycharmProjects\pdnp14-04\day_1\pierwszy.py", line 15
#     print("Nazywam się Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 15)
# ctrl / - komentarz wielu linijek
# Process finished with exit code 1 błąd
print("Dalej")
# Nazywam sie Radek
# Dalej
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, dane tekstowe

print("39")
print(39)
print(type("39"))
print(type(39))  # <class 'int'>, liczby całkowite
# print("39" + 39) # TypeError: can only concatenate str (not "int") to str
print("39" + "39")  # konkatenacja, łaczenie stringów
print(39 + 39)

print(int("39") + 39)  # rzutowanie na int, zamiana, 78
print("39" + str(39))  # rzutowanie na tekst, str(), 3939

print("168" * 35)
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(168 * 35)  # 5880

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - pudełko na dane
# snake_case - nazwy zmiennych, plikow itp
# nazwa zmiennej powinna podpowiadac co zawiera zmienna
# kebab-case
# PascalCase
# camelCase

# typowanie dynamiczne
name = "radek"
print(name)  # radek
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))  # <class 'int'>

# podpowiedzi typów
name: str = "Radek"
print(type(name))  # <class 'str'>
name = 90
print(name)
# pip install mypy

age = 90
print(age)
print(type(age))
