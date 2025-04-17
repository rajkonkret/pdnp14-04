a = 10  # globalne
b = 10


def dodaj():
    a = 7  # lokalne zmienne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a # użyj globalne a
    a = 9
    b = 89
    print(a + b)


print(f"Wartość a z góry {a=} (globalne)")  # Wartość a z góry a=10 (globalne)
dodaj()  # 15
print(f"Wartość a z góry {a=} (globalne)")  # Wartość a z góry a=10 (globalne)
dodaj2()  # 20 globalne
print(f"Wartość a z góry {a=} (globalne)")  # Wartość a z góry a=10 (globalne)
dodaj3()  # 98
print(f"Wartość a z góry {a=} (globalne)")  # Wartość a z góry a=9 (globalne)
dodaj2()
print(f"Wartość a z góry {a=} (globalne)")  # Wartość a z góry a=9 (globalne)
