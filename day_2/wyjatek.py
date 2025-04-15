# wyjątek - błędy podczas wykonywania programu

# print(5 / 0)
#  Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp14-04\day_2\wyjatek.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("a" * "23")
    # raise KeyError("Brak klucza")
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except Exception as e:  # pozostałe błedy
    print("Błąd", e)
else:  # gdy nie ma błędu
    print("Wynik", wynik)
finally:  # wykona się zawsze
    print("Koniec dziąłania")
print("Program nadal działa")
# Błąd typu
# Program nadal działa
# Błąd 'Brak klucza'
# Program nadal działa
# Wynik 2.727272727272727
# Konirec dziąłania
# Program nadal działa
