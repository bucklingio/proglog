## Uniek

```python
import random

getallen = []
aantalKeer = []

for teller in range(5):
    aantalKeer.append(0)

for teller in range(7):
    getallen.append(random.randint(1, 5))

for element in getallen:
    print(element)
    aantalKeer[element - 1] += 1

print("Unieke getallen:")

for teller in range(5):
    if aantalKeer[teller] == 1:
        print(teller + 1)
```

[Terug naar opdracht](/taken/uniek.html)
[Terug naar cursus](/25_toevoegen.html)