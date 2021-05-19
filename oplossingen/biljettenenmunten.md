## Biljetten en munten

```python
biljettenEnMunten = [500, 200, 100, 50, 20, 10, 5, 2, 1]

bedrag = int(input("Bedrag: "))

for waarde in biljettenEnMunten:
    aantal = bedrag // waarde
    if aantal != 0:
        print(waarde, ":", aantal)
        bedrag = bedrag % waarde
```

[Terug naar opdracht](/taken/biljettenenmunten.html)
[Terug naar cursus](/25_toevoegen.html)