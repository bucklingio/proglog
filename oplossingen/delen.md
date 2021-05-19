## Delen

```python
getal1 = float(input("Getal 1: "))
getal2 = float(input("Getal 2: "))
if getal1 > getal2:
    grootste = getal1
    kleinste = getal2
else:
    grootste = getal2
    kleinste = getal1
if kleinste == 0:
    print("Delen door 0 is onmogelijk.")
else:
    print(round(grootste / kleinste, 2))
```

[Terug naar opdracht](/taken/delen.html)
[Terug naar cursus](/13_meerdereif.html)