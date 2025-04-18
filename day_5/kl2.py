class Human:
    """
    Klasa opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """

        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1= Human() 3 TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Anna", 37, 170)
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 37
# k
cz1.wypisz_wiek()
cz1.wypisz_wzrost()
cz1.powitanie()
# Mam 37 lat
# Mam 170 cm wzrostu
# Nazywam się Anna

cz2 = Human("Radek", 45, 190, "m")

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłem w drogę
# Ruszyłem w drogę
