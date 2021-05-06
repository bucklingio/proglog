def tekenLijn(teken, aantal):
    lijn = ""
    for i in range(1, aantal + 1):
        lijn += teken
    print(lijn)


tekenLijn("=", 5)
tekenLijn("-", 10)
