class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizując
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # pole prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Jade z szybkosćią {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


car1 = Car("Multipla", 2025)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.__predkosc) # AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
car1.licznik()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()
# Jade z szybkosćią 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Jade z szybkosćią 0 km/h