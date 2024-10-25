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

if __name__ == "__main__":
    autot: list[Auto] = []
    for i in range(1,11):
        autot.append(Auto(f"ABC-{i}", randint(100, 200)))

    run = True
    while run:
        for i in autot:
            i.kiihdytä(randint(-10, 15))
            i.kulje(1)
            if i.kuljettumatka >= 10000:
                run = False
                break

    autot.sort(key=lambda x: x.kuljettumatka, reverse=True)

    for (x,i) in enumerate(autot):
        print(f"{"#"+str(x+1)} {i.rekisteri} {i.kuljettumatka}km")
