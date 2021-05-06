aantalVolwassenen = 0
aantalKinderen = 0
leeftijd = int(input("Leeftijd (0 om te stoppen): "))
while leeftijd != 0:
    if leeftijd >= 18:
        aantalVolwassenen += 1
    else:
        aantalKinderen += 1
    leeftijd = int(input("Leeftijd (0 om te stoppen): "))
print("Aantal volwassenen: " + str(aantalVolwassenen))
print("Aantal kinderen: " + str(aantalKinderen))
