# stworzyc funkcje obliczjacą średnia
def liczby(name=None, *cyfry):
    print(cyfry)
    try:
        count = len(cyfry)
        suma = 0
        for c in cyfry:
            suma += c

        avg = suma / count

    except Exception as e:
        print("Błąd:", e)
    else:  # gdy nie ma błedu
        print(f"Srednia dla ucznia {name} wynosi: {avg}")
    finally:  # zawsze
        print("Nastepne obliczenie")


liczby()
liczby(1, 2, 3)
liczby("Radeki", 1, 2, 3)
liczby("Radeki", 1, 2, 3, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8)
