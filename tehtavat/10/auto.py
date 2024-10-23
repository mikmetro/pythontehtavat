from random import randint

class Auto:
    def __init__(self, rekisteri: str, huippunopeus: int) -> None:
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = self.kuljettumatka = 0

    def kiihdytä(self, muutos: int) -> None:
        self.nopeus = max(min(self.huippunopeus, self.nopeus + muutos), 0)

    def kulje(self, tunnit: float) -> None:
        self.kuljettumatka += self.nopeus * tunnit

class Kilpailu:
    def __init__(self, nimi: str, pituus: int, autot: list[Auto]) -> None:
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.loppu = False

    def tunti_kuluu(self) -> None:
        for i in self.autot:
            i.kiihdytä(randint(-10, 15))
            i.kulje(1)
            if i.kuljettumatka >= self.pituus:
                self.loppu = True

    def tulosta_tilanne(self) -> None:
        self.autot.sort(key=lambda x: x.kuljettumatka, reverse=True)
        for (x,i) in enumerate(self.autot):
            print(f"{"#"+str(x+1):<3} {i.rekisteri:<7} {i.kuljettumatka}km")
        print("\n")

    def kilpailu_ohi(self) -> bool:
        return self.loppu

if __name__ == "__main__":
    autot: list[Auto] = []
    for i in range(1,11):
        autot.append(Auto(f"ABC-{i}", randint(100, 200)))
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    i = 0
    while not kilpailu.loppu:
        kilpailu.tunti_kuluu()
        i += 1
        if i % 10 == 0:
            kilpailu.tulosta_tilanne()

    print("\n- Lopulliset tulokset -")
    kilpailu.tulosta_tilanne()
