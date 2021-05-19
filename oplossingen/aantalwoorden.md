## Aantal woorden

```python
zin = input("Geef een zin: ")
aantalWoorden = 0
vorigTeken = " "
for index in range(len(zin)-1):
    if zin[index] != " " and vorigTeken == " ":
        aantalWoorden += 1
    vorigTeken = zin[index]
    
print(aantalWoorden)
```
[Terug naar opdracht](/taken/aantalwoorden.html)
[Terug naar cursus](/27_string.html)