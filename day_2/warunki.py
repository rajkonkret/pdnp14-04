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
