num = int(input("Anna kokonaisluku: "))

for i in range(2, num):
    if num % i == 0:
        print("Ei ole alkuluku")
        break
    if i == num - 1:
        print("On alkuluku")
