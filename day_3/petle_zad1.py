# pętle - możliwośc wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # 0 do 4
    print(i)

for i in range(5):
    pass  # nic nie rob

for _ in range(5):  # niema zmienna
    print("Test podłoga")
    print(_)

for i in range(10):
    print(i * 2)
    print(i + 2)

# przerobic lotto na wylosowanie 6 liczb. uzyc pętli
lista_kule = list(range(1, 50))
lista_wyn = []

for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wyn.append(wyn)

print(lista_wyn)  # [14, 11, 23, 4, 19, 6]
