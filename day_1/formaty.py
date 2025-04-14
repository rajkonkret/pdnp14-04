import sys

user = "Tomek"  # str
wiek = 30  # int
wersja = 3.900001
print(type(wersja))  # <class 'float'>, zmmiennoprzecinkowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
liczba = 890765432123456  # int

print("Witaj %s masz teraz %d lat." % (user, wiek))  # Witaj Tomek masz teraz 30 lat.
# %s string
# %d digit
# print("Witaj %d masz teraz %s lat." % (user, wiek))  #TypeError: %d format: a real number is required, not str

print("witaj %(user)s. jak się czujesz %(user)s" % {"user": user})
# witaj Tomek. jak się czujesz Tomek

print("witaj {}, masz teraz {} lat.".format(user, wiek))
# witaj Tomek, masz teraz 30 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 30 lat.

print("Uzywamy wersji python %i" % 3)  # Uzywamy wersji python 3
print("Uzywamy wersji python %f" % 3)  # Uzywamy wersji python 3.000000
print("Uzywamy wersji python %.1f" % 3.9)  # Uzywamy wersji python 3.9
print("Uzywamy wersji python %.2f" % 3.9)  # Uzywamy wersji python 3.90
print("Uzywamy wersji python %.0f" % 3.9)  # Uzywamy wersji python 4
print("Uzywamy wersji python %.f" % 3.9)  # Uzywamy wersji python 4

print(f"Uzywamy wersji python {wersja}")  # Uzywamy wersji python 3.900001
print(f"Uzywamy wersji python {wersja:.2f}")  # Uzywamy wersji python 3.90
print(f"Uzywamy wersji python {wersja:.1f}")  # Uzywamy wersji python 3.9
print(f"Uzywamy wersji python {wersja:.0f}")  # Uzywamy wersji python 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<15}")  # "Tomek          "
print(f"{user:^25}")  # "          Tomek          "

print(liczba)  # 890765432123456
print(f"Nasza duzą liczba {liczba:,}")  # Nasza duzą liczba 890,765,432,123,456
print(f"Nasza duzą liczba {liczba:_}")  # Nasza duzą liczba 890_765_432_123_456
print(f"Nasza duzą liczba {liczba:_}".replace("_", " "))  # Nasza duzą liczba 890 765 432 123 456
print(f"Nasza duzą liczba {liczba:_}".replace("_", "."))  # Nasza duzą liczba 890.765.432.123.456

dane = 5000000000000
dane = 50_000_000_000
print(type(dane))  # <class 'int'>
print(dane)  # 50000000000
