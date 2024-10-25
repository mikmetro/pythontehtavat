from random import randint

m = int(input("Montako tahkoa nopassa? "))

def noppa(max):
    return randint(1,max)

tulos = noppa(m)
while tulos < m:
    print(tulos)
    tulos = noppa(m)
print(tulos)
