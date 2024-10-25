class Julkaisu:
    def __init__(self, nimi: str) -> None:
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi: str, kirjoittaja: str, sivumäärä: int) -> None:
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self) -> None:
        print(self.nimi, self.kirjoittaja, self.sivumäärä)

class Lehti(Julkaisu):
    def __init__(self, nimi: str, päätoimittaja: str) -> None:
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self) -> None:
        print(self.nimi, self.päätoimittaja)

if __name__ == "__main__":
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    lehti.tulosta_tiedot()
    kirja.tulosta_tiedot()
