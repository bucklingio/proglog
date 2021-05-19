## List totaal

```python
import random

som = 0
randomArray = []
randomArray.append(random.randint(1, 10))
randomArray.append(random.randint(11, 20))
randomArray.append(random.randint(21, 30))

for element in randomArray:
    print(element)
    som += element

print(som)
```

[Terug naar opdracht](/taken/listtotaal.html)
[Terug naar cursus](/24_forin.html)