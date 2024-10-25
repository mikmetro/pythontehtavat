from random import randint

def noppa():
    return randint(1,6)

tulos = noppa()
while tulos < 6:
    print(tulos)
    tulos = noppa()
print(tulos)
