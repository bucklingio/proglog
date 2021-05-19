## Temperaturen

```python
somTemperaturen = float(0)
aantalTemperaturen = 0
temperatuur = float(input("Temperatuur: "))
hoogsteTemperatuur = temperatuur
laagsteTemperatuur = temperatuur
while temperatuur != 777:
    if temperatuur > hoogsteTemperatuur:
        hoogsteTemperatuur = temperatuur
    if temperatuur < laagsteTemperatuur:
        laagsteTemperatuur = temperatuur
    somTemperaturen += temperatuur
    aantalTemperaturen += 1
    temperatuur = float(input("Temperatuur: "))
if aantalTemperaturen != 0:
    gemiddeldeTemperatuur = somTemperaturen / aantalTemperaturen
    print("Hoogste temperatuur: ", hoogsteTemperatuur)
    print("Laagste temperatuur: ", laagsteTemperatuur)
    print("Gemiddelde temperatuur: ", round(gemiddeldeTemperatuur, 2))
```

[Terug naar opdracht](/taken/temperaturen.html)
[Terug naar cursus](/17_nognesten.html)