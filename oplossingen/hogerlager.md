## Hoger Lager

```python
import random

teRadenGetal = random.randint(1, 10)
raadGetal = int(input("Raad het getal tussen 1 en 10: "))
aantalBeurten = 1
while raadGetal != teRadenGetal:
    aantalBeurten += 1
    if raadGetal > teRadenGetal:
        print("Lager.")
    else:
        print("Hoger.")
    raadGetal = int(input("Raad het getal tussen 1 en 10: "))
print("Proficiat.")
print("Geraden in", aantalBeurten, "beurten.")
```

[Terug naar opdracht](/taken/hogerlager.html)
[Terug naar cursus](/17_nognesten.html)