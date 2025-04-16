# python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.strip().casefold():
    case "python":
        lista.append("znam pythona")
    case "java":
        lista.append("znam jave")
    case _:  # else
        print("inny")
# Podaj znany Ci język programowaniapython
# ['znam pythona']

print(lista)