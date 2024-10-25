from random import randint

vastaus = randint(1,10)
while 1:
    arvaus = int(input("Arvauksesi: "))
    if arvaus > vastaus:
        print("Liian suuri arvaus")
    elif arvaus < vastaus:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break
