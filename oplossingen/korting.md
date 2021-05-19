## Korting

```python
aantalKorting = 0
leeftijdBezoeker = int(input("Leeftijd bezoeker: "))
while leeftijdBezoeker != 0:
    if leeftijdBezoeker < 7 or leeftijdBezoeker > 80:
        aantalKorting += 1
    leeftijdBezoeker = int(input("Leeftijd bezoeker: "))
print("Aantal bezoekers met korting: ", aantalKorting)
```

[Terug naar opdracht](/taken/korting.html)
[Terug naar cursus](/17_nognesten.html)