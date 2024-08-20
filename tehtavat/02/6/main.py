from random import randint

kolmen = ""
neljan = ""
for i in range(0, 3):
    kolmen += str(randint(0, 9))
    neljan += str(randint(1, 6))

neljan += str(randint(1, 6))

print("Kolmenumeroinen koodi:", kolmen)
print("Neljänumeroinen koodi:", neljan)
