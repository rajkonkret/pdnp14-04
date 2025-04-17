# funkcja wewnętrzna, zagnieżdzona
# w dekoratorach
def fun1():
    print('To jest fun1')

    def fun2():
        print("To jest fun2")

    # fun2() # zwraca wynik
    return fun2  # zwraca adres funkcji, referencję


xfun = fun1()  # To jest fun1
print(xfun)  # <function fun1.<locals>.fun2 at 0x000001F864275BC0>
print(type(xfun))  # <class 'function'>
xfun()  # uruchamiamy funkcje zawarta w zmiennej, czyli fun2
xfun()
xfun()
xfun()
xfun()
