def grootste(getal1, getal2):
    if getal1 > getal2:
        grootste = getal1
    else:
        grootste = getal2
    return grootste


print(grootste(3, 4))

grootsteGetal = grootste(float(input("Getal 1: ")), float(input("Getal 2: ")))
print("Het kwadraat van het grootste getal is ", grootsteGetal**2)
