## Willekeurige volgorde

```python
import random

getallen = []
for teller in range(5):
    getallen.append(0)

for getal in range(5):
    index = random.randint(0, 4)
    while getallen[index] != 0:
        index = random.randint(0, 4)
    getallen[index] = getal + 1

for element in getallen:
    print(element)
```

[Terug naar opdracht](/taken/willekeurigevolgorde.html)
[Terug naar cursus](/25_toevoegen.html)