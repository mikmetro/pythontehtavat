print("Mikä on sinun biologinen sukupuolisi?\n1) Mies\n2) Nainen")
sukupuoli = input("Anna numero: ")
if sukupuoli != "1" and sukupuoli != "2":
    print("Virheellinen arvo:", sukupuoli)
    exit()
hemoglob = float(input("Anna hemoglobiini arvosi (g/l): "))

if sukupuoli == "1":
    if hemoglob < 134:
        print("Sinun hemoglobiini arvosi on alhainen")
    elif hemoglob > 195:
        print("Sinun hemoglobiini arvosi on korkea")
    else:
        print("Sinun hemoglobiini arvosi on normaali")
elif sukupuoli == "2":
    if hemoglob < 117:
        print("Sinun hemoglobiini arvosi on alhainen")
    elif hemoglob > 175:
        print("Sinun hemoglobiini arvosi on korkea")
    else:
        print("Sinun hemoglobiini arvosi on normaali")
