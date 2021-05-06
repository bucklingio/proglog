temperatuur = float(input("Temperatuur: "))
if temperatuur <= 0:
    if temperatuur < -40:
        print("Blijf thuis.")
    else:
        print("Doe een dikke jas aan.")
