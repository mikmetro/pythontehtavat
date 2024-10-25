luvut = []

for i in range(1, 4):
    luvut.append(int(input(f"Kerro luku {i}/3: ")))

print("Lukujen summa:", sum(luvut))
print("Lukujen tulo:", luvut[0]*luvut[1]*luvut[2])
print("Lukujen keskiarvo:", sum(luvut)/len(luvut))
