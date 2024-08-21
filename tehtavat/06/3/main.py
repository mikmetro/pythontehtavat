def gallons_to_liters(l):
    return l * 3.785

while 1:
    m = float(input("Montako gallonaa? "))
    if m < 0:
        break
    print(f"{m}l = {gallons_to_liters(m):.4f}gl")
