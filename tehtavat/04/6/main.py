from random import uniform

osumat = 0
yritykset = int(input("Kuinka monta pistettä? "))

i = 0
while i < yritykset:
    piste = (uniform(-1,1), uniform(-1,1))
    if piste[0] ** 2 + piste[1] ** 2 < 1:
       osumat += 1
    i += 1

print("Piin likiarvo:", (4 * osumat )/ yritykset)
