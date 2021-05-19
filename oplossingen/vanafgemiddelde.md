## Vanaf gemiddelde

```python
def invoerArray():
    array = []
    for teller in range(5):
        array.append(int(input("Getal: ")))
    return array

def gemiddeldeVanArray(array):
    som = 0
    aantal = 0
    for element in array:
        som += element
        aantal += 1
    return som / aantal

def bovenMinimum(array, getal):
    for element in array:
        if element >= getal:
            print(element)

getallen = invoerArray()
gemiddelde = gemiddeldeVanArray(getallen)
bovenMinimum(getallen, gemiddelde)
```

[Terug naar opdracht](/taken/vanafgemiddelde.html)
[Terug naar cursus](/26_listsenfuncties.html)