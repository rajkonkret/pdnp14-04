# funkcja - wykonanie fragmentu kodu wielokrotnie
# funkcja musi byc najpierw zadeklarowana
# w miejscu deklaracji funkcja nie uruchamia się
# zeby uruchomic funkcję nalezy ja wywołac

a = 8
b = 6


# funkcje nezwracające wyniku
def dodaj():  # funkcja bez argumentów
    print(a + b)


def dodaj2(a, b):  # argumenty a i b obowiązkowe
    print(a + b)  # lokalne argumnty w zakresie tej funkcji


# funkcvja ma argument o wartości domyslnej c=0
# to pozwala zasymulowac przeciążanie funkcji liczbą argumentów
def odejmij(a, b, c=0):
    print(a - b - c)


# argumenty pozycyjne
# użycie/uruchomienie funkcji
dodaj()  # 14
# dodaj2()  TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(67, 89)  # 156
odejmij(1, 2, 3)  # -4
odejmij(1, 2)  # -1

# argumenty po nazwie
odejmij(c=9, b=9, a=78)
odejmij(b=9, a=87)  # 78

# argumenty mieszane
odejmij(1, b=9)
dodaj2(1, b=10)

# najpierw pozycyjne, następnie po nazwie
# odejmij(b=8, 1, 2) # SyntaxError: positional argument follows keyword argument

print(dodaj())
print(dodaj2(56, 78) + dodaj())
