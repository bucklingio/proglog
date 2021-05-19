## Kader tekenen

```python
lengte = int(input("Lengte: "))
breedte = int(input("Breedte: "))
buitenLengteString = ""
for lengteTeller in range(lengte):
    buitenLengteString += "."
print(buitenLengteString)
for breedteTeller in range(1, breedte-1):
    binnenLengteString = "."
    for lengteTeller in range(1, lengte-1):
        binnenLengteString += " "
    binnenLengteString += "."
    print(binnenLengteString)
print(buitenLengteString)
```

[Terug naar opdracht](/taken/kadertekenen.html)

[Terug naar cursus](/18_for.html)