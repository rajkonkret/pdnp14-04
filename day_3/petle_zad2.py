dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# wyświetli klucze
for i in dictionary:
    print(i)

for i in dictionary.keys():
    print(i)
    # imie
    # nazwisko
    # imie
    # nazwisko

# 3 wyswietla wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# 3 wyświetla pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, v)
# imie Radek
# nazwisko Kowalski

#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
for k, v in dictionary.items():
    print(k, v, sep="=>", end="<===>")
    # 3 imie=>Radek<===>nazwisko=>Kowalski<===>
print("Radek")  # imie=>Radek<===>nazwisko=>Kowalski<===>Radek
print("Tomek")  # Tomek

pol_ang = {"kot": "cat", "pies": "dog", "dach": "roof"}
ang_pol = {}  # pusty słonik

for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}
