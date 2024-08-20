leiviskat = float((input("Anna leiviskät: ")))
naula = float((input("Anna naulat: ")))
luoti = float((input("Anna luodit: ")))

naula += leiviskat * 20
luoti += naula * 32

paino = luoti * 13.3

kg = int(paino // 1000)
g = paino % 1000

print("Massa nykymittojen mukaan: ")
print(f"{kg} kilogrammaa ja {g:.2f} grammaa.")
