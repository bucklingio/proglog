def ingredientenTonen():
    print("INGREDIËNTEN:")
    print("250 gram zelfrijzende bloem")
    print("3 eieren")
    print("50 cl melk")
    print("een zakje vanillesuiker")


def bereidingTonen():
    print("BEREIDING:")
    print("Zeef de bloem met de vanillesuiker.")
    print("Voeg de eieren en de melk toe.")
    print("Bak de pannenkoeken in een pan met boter.")


keuze = int(input("1=ingrediënten, 2=bereiding, 0=stop: "))
while keuze != 0:
    if keuze == 1:
        ingredientenTonen()
    elif keuze == 2:
        bereidingTonen()
    else:
        print("Verkeerde keuze.")
    keuze = int(input("1=ingrediënten, 2=bereiding, 0=stop: "))
