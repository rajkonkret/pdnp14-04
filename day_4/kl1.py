# klasy - element programowania  obiektowego
# klasa - szablon, opis, przepis
# cechy - zmienne
# metody - funkcje w klasie
# obiekt - instancja klasy
# klasa musibyc zadeklarowana przed uzyciem
# tworzenie obiektu uruchamia metode __init__
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakacja

# PascalCase
class Human:
    """
    Klasa Human w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} ")


cz1 = Human()
print(cz1)

print(Human.__doc__)  # Klasa Human w Pythonie
print(print.__doc__)
# cd.\day_4\
# pydoc -b
# pydoc -w kl1
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# None
# k
cz1.wiek = 45
cz1.imie = "Anna"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 45
# k
cz1.powitanie()
cz1.wypisz_wiek()