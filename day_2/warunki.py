# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykona jednen lub drugi blok programu
# warunek zwraca bool

odp = True
# odp = False
if odp:  # blok programu, który wykona sie gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

if odp:
    print("dane zostały pobrane")

odp = "Radek"
if odp == "Radek":
    print("Nadal Radek")
# Dalsza częśc programu
# dane zostały pobrane
# Nadal Radek

odp = 0
if odp:
    print("Działa")
else:
    print("Zero -> False")
    # Zero -> False

a = "Radek"
if len(a) > 3:
    print(f'Długosc wynosi {len(a)}, więcej niż 3')
# Długosc wynosi 5, więcej niż 3

a = "Radek"
n = len(a)
if n > 3:
    print(f'Długosc wynosi {n}, więcej niż 3')
# Długosc wynosi 5, więcej niż 3

# operator morsa, walrus
if (n := len(a)) > 3:
    print(f'Długosc wynosi {n}, więcej niż 3')

# kolejnośc warunków ma znaczenie
# # pierwszy true, wyjście z drzewka
# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 39999:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki} pln.")
# # podatek 0.2 dla przedziału 10000 do 39999

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f'Rabat wynosi {rabat}')

rabat = 25 if suma_zam > 100 else 0  # operator warunkowy
print(f'Rabat wynosi {rabat}')

# napisac program test z...
#
# punkty = 0
# odp = input("Podaj datę chrztu Polski")  # str
# if odp.strip().casefold() == "966":
#     print("dobrze")
#     punkty += 1  # punkty = punkty + 1
# else:
#     print("Idź sie pouczyć")
#
# print("Zdobyte punkty:", punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
#
# zasymulujemy system zbierania logów
# zmienna bedzie zawierac informacje jaki system
# email, console, inny
# console -> "Stało się coś strasznego"
# email -> "System email"
# jezeli system email to do listy błedow ma dodac opis błedy
# zmienna dodakowa -> error, medium, inny

alert_system = "email"
error_level = "error"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        print("Inny błąd")
else:
    print("Inny system")
# System email
print(lista_b)
