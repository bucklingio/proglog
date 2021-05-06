opbrengst = 0
gestort = float(input("Gestortbedrag(0 om te stoppen): "))
while gestort != 0:
    opbrengst += gestort
    print(opbrengst)
    gestort = float(input("Gestort bedrag (0 om te stoppen): "))
