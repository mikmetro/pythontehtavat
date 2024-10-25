vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0 and vuosi % 100 == 0:
    print(f"{vuosi} ON karkausvuosi")
elif vuosi % 4 == 0 and vuosi % 100 != 0:
    print(f"{vuosi} ON karkausvuosi")
else:
    print(f"{vuosi} EI ole karkausvuosi")
