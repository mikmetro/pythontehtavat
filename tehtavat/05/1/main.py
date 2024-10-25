from random import randint

arpaluvut = int(input("Arpalukujen summa: "))
summa = 0

for i in range(arpaluvut):
    summa += randint(1,6)

print(summa)
