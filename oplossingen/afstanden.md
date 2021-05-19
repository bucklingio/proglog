## Afstanden

```python
afstand = float(input("Afstand in centimeters: "))
print("1. Naar meters")
print("2. Naar inches")
print("3. Naar feet")
keuze = int(input("Keuze: "))
if keuze == 1:
    meters = afstand / 100
    print("Afstand in meters:", round(meters, 2))
elif keuze == 2:
    inches = afstand * 0.39
    print("Afstand in inches:", round(inches, 2))
elif keuze == 3:
    feet = afstand * 0.0328084
    print("Afstand in feet:", round(feet, 2))
else:
    print("Verkeerde keuze.")
```

[Terug naar opdracht](/taken/afstanden.html)
[Terug naar cursus](/19_elif.html)