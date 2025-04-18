from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pyrhonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        # super() - klasa wyzsza
        # obowiązkowo musimy wywołac konstruktor super()

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko k ok ok oko ko")


class Orzel(Ptak):
    """
    Klasa Orzeł dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("kier kir kier")


# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
# or1.wydaj_odglos()
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
or2 = Orzel("Bielik", 50)
or2.latam()
kur2.wydaj_odglos()
or2.wydaj_odglos()
# Ko k ok ok oko ko
# kier kir kier
