wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float
print(temp)
print(type(temp))  # <class 'float'>

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # float 0.023209876543209877
print(rok // wiek)  # czesc całkowita z dzielenia
print(rok % wiek)  # modulo - reszta z dzielenia
print(5 % 2)  # wynik 2 r 1 5 % 2 = 1

print(wiek ** rok)
# len() długosc
print(len(str(wiek ** rok)))  # 3386
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds
# thelimit(4300digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + 4 / (2 + 4) / 2)  # -160.66666666666666

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal - pozwala ominać bład zaokrąglenia

print(f"sprawdzenie zmiennej {temp} {wiek}")  # sprawdzenie zmiennej 36.6 47
print(f"""
{temp}
    {wiek}""")
# "36.6
#     47"

# typ logiczny
# prawda fałsz
# True False
# 1 0

czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))  # <class 'bool'>

print(int(czy_znasz_pythona))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("RaDEK"))  # True
print(bool("0"))  # True

print(bool(""))  # False
print(bool(None))  # False, odpowiednik null, stan nieokreslony, nie wiem

# and - i
print(True and False)  # False
print(False and False)  # False
print(False and True)  # False
print(True and True)  # True

# or - lub
print(True or False)  # True
print(False or False)  # False
print(False or True)  # True
print(True or True)  # True

# not - negacja
print(not True)  # False
print(not False)  # True

a = 8
b = 6

print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 8 >= 6 = True
print(f"Porównanie {a >=b = }")  # Porównanie a >=b = True
print(f"Porównanie {a} <= {b} = {a <= b}")  # Porównanie 8 <= 6 = False
# == porównannie
print(f"Porównanie {a} == {b} = {a == b}")  # Porównanie 8 == 6 = False
# != - rózne
print(f"Porównanie {a} != {b} = {a != b}")  # Porównanie 8 != 6 = True
