yritykset = 0
while 1:
    user = input("Käyttäjätunnus: ")
    passw = input("Salasana: ")
    if user == "python" and passw == "rules":
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        if(yritykset == 5):
            print("Pääsy evätty")
            break
        else:
            print("Väärät tunnukset. Yritä uudelleen")
