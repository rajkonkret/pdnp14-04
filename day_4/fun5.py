# stworzyc funkcje kantor
# ma miec dwie funkcje wewnętrne eur, usd
# w zaleznosci od parametru ma zwracac jedną z tych funkcji
# przelicz walute (uzyj funkcji)

def kantor(waluta):
    def usd(kwota):
        print(f"Wymieniam dolary: {3.77 * kwota}")

    def eur(kwota):
        print(f"Wymieniam euro: {4.28 * kwota}")

    if waluta == "usd":
        return usd
    else:
        return eur


kantor_eur = kantor("eur")
kantor_eur(1000)
kantor_eur(13000)
# Wymieniam euro: 4280.0
# Wymieniam euro: 55640.0

kantor_usd = kantor("usd")
kantor_usd(1000)
