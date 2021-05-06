import random

getallen = [[0 for x in range(3)] for y in range(2)]

getallen[1][2] = 7
print(getallen[1][2])

for rijIndex in range(2):
    for kolomIndex in range(3):
        getallen[rijIndex][kolomIndex] = random.randint(1, 10)

for rij in getallen:
    rijString = ""
    for element in rij:
        rijString += str(element)
        rijString += " "
    print(rijString)
