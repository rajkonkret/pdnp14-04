tekst = 'Witaj Świecie'

print(tekst)
print(type(tekst))

# teksty są niemutowalne
tekst.upper()
# 3    """ Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE
upper_case = tekst.upper()
print(upper_case)  # WITAJ ŚWIECIE

print(tekst.capitalize())  # Witaj świecie
print(tekst.lower())  # witaj świecie

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encoded_s = tekst.encode("utf-8")
print(encoded_s)  # b'Witaj \xc5\x9awiecie'
# \xc5\x9a
print(type(encoded_s))  # <class 'bytes'>, dane bajtowe
print(encoded_s.decode('utf-8'))  # Witaj Świecie

# Witaj Świecie
# 0123456789... indeksy od 0

print(tekst[4])  # indeks 4, pozycja 5

print(tekst.count("i"))  # 3 elementy
print(tekst.count("j", 0, 4))  # 0 elementow, 0123, z prawej strony zbior otwarty

imie = "Radek"
print(imie)

print("Imie", imie)  # Imie Radek

starszy = "Witaj %s!"  # %s - wklej str
print(starszy % imie)  # Witaj Radek!

tekst_format = f"Mam na imię {imie} i lubie pythona."
print(tekst_format)
# f - string
tekst_format = f"\tMam na imię {imie}\n i lubie pythona.\b"
print(tekst_format)
# \t - tabulator
# \n nowa lina
# \b - backspace
# "	  Mam na imię Radek
#  i lubie pythona"

print("Witaj {}! ".format(imie))  # Witaj Radek!

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy
#

""" Komentarz
    wielolinijkowy"""
