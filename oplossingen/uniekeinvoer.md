## Unieke invoer

```python
def isNietUniek(array, invoer):
    for element in array:
        if element == invoer:
            return True
    return False

getallen = []
for teller in range (5):
    invoer = int(input("Getal: "))
    while isNietUniek(getallen, invoer):
        print("Getal reeds ingetikt, probeer opnieuw.")
        invoer = int(input("Getal: "))
    getallen.append(invoer)

for getal in getallen:
    print(getal)
```

[Terug naar opdracht](/taken/uniekeinvoer.html)
[Terug naar cursus](/26_listsenfuncties.html)