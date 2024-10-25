kuhanpituus = float(input("Kerro kuhan pituus (cm): "))

if kuhanpituus < 37:
    print(f"Laske kuha takaisin järveen, pituus oli {
          37 - kuhanpituus}cm alle sallitun rajan.")
else:
    print("OK")
