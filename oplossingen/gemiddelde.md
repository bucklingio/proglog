## Gemiddelde

```python
som = 0
aantal = 0
getal = float(input("Getal: "))
while getal != 0:
    som += getal
    aantal += 1
    getal = float(input("Getal: "))
if aantal != 0:
    gemiddelde = som / aantal
    print("Gemiddelde: ", round(gemiddelde, 2))
```

[Terug naar opdracht](/taken/gemiddelde.html)
[Terug naar cursus](/16_while.html)