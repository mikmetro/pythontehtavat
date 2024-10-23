class Auto:
    def __init__(self, rekisteri: str, huippunopeus: int) -> None:
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = self.kuljettumatka = 0

    def kiihdytä(self, muutos: int) -> None:
        self.nopeus = max(min(self.huippunopeus, self.nopeus + muutos), 0)

    def kulje(self, tunnit: float) -> None:
        self.kuljettumatka += self.nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self, rekisteri: str, huippunopeus: int, akkukapasiteetti: float) -> None:
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri: str, huippunopeus: int, bensatankki: float) -> None:
        super().__init__(rekisteri, huippunopeus)
        self.bensatankki = bensatankki


if __name__ == "__main__":
    sauto = Sähköauto("ABC-15", 180, 52.5)
    pauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sauto.kiihdytä(20)
    pauto.kiihdytä(35)

    sauto.kulje(3)
    pauto.kulje(3)

    print(f"{sauto.kuljettumatka}km")
    print(f"{pauto.kuljettumatka}km")
