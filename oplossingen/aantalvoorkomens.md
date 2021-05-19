## Aantal voorkomens

```python
import random

getallen = []
aantalKeer = 0

for teller in range(7):
    getallen.append(random.randint(1, 5))

for element in getallen:
    print(element)

getal = int(input("Getal: "))

for element in getallen:
    if element == getal:
        aantalKeer += 1

print(aantalKeer)
```

[Terug naar opdracht](/taken/aantalvoorkomens.html)
[Terug naar cursus](/25_toevoegen.html)