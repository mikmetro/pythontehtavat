lentoasemat = {}

def help():
    print("1) Rekisteröi uusi lentoasema")
    print("2) Hae lentoaseman tiedot")
    print("3) Lopeta")

help()

while 1:
    cmd = input("")
    if cmd == "1":
        icao = input("Syötä ICAO koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema lisätty")
    elif cmd == "2":
        icao = input("Syötä ICAO koodi: ")
        if icao in lentoasemat:
            print(f"Lentoaseman {icao} tiedot:")
            print("Nimi:", lentoasemat[icao])
        else:
            print(f"{icao} ICAO koodia ei löytynyt")
    elif cmd == "3":
        print("Kiitos käynnistä")
        break
    else:
        print("Virheellinen syöte")
