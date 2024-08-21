from math import floor

vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kk = int(input("Anna kuukausi: "))

print(vuodenajat[floor((kk - 3) / 3)])
