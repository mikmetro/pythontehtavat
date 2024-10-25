class Hissi:
    def __init__(self, alin: int, ylin: int) -> None:
        self.kerros = self.alin = alin
        self.ylin = ylin


    def siirry_kerrokseen(self, kerros: int):
        while self.kerros != kerros:
            if self.kerros > kerros:
                self.kerros_alas()
            elif self.kerros < kerros:
                self.kerros_ylös()

    def kerros_alas(self):
        self.kerros = max(self.alin, self.kerros - 1)

    def kerros_ylös(self):
        self.kerros = min(self.ylin, self.kerros + 1)

class Talo:
    def __init__(self, alin: int, ylin: int, hissit: int) -> None:
        self.hissit = [Hissi(alin, ylin) for i in range(hissit)]

    def aja_hissiä(self, hissi: int, kerros: int) -> None:
       self.hissit[hissi].siirry_kerrokseen(kerros)

    def palohälytys(self) -> None:
        for i in self.hissit:
            i.siirry_kerrokseen(0)


if __name__ == "__main__":
    talo = Talo(0, 15, 3)
    print(talo.hissit[1].__dict__)
    talo.aja_hissiä(1, 12)
    print(talo.hissit[1].__dict__)
    talo.palohälytys()
    print(talo.hissit[1].__dict__)
