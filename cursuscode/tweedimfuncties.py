import random


def maakArray():
    getallen = [[0 for x in range(5)] for y in range(3)]
    for rijIndex in range(3):
        for kolomIndex in range(5):
            getallen[rijIndex][kolomIndex] = random.randint(1, 10)
    return getallen


def toonArray(eenArray):
    for rij in eenArray:
        rijString = ""
        for element in rij:
            rijString += str(element)
            rijString += " "
        print(rijString)


toonArray(maakArray())
