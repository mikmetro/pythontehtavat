from math import pi

def pizza_hinta(halkasija, hinta):
    r = halkasija / 2
    area = pi * (r ** 2)
    return hinta / area

p1 = float(input("Pizza 1 halkasija: "))
p1h = float(input("Pizza 1 hinta: "))

p2 = float(input("Pizza 2 halkasija: "))
p2h = float(input("Pizza 2 hinta: "))

p1r = pizza_hinta(p1, p1h)
p2r = pizza_hinta(p2, p2h)

if(p1r < p2r):
    print(f"Pizza 1 on parempi vastine rahalle: {p1r:.4f}€/cm² < {p2r:.4f}€/cm²")
elif(p1r > p2r):
    print(f"Pizza 2 on parempi vastine rahalle: {p2r:.4f}€/cm² < {p1r:.4f}€/cm²")
else:
    print(f"Molemmat ovat saman hintaisia: {p2r:.4f}€/cm²")
