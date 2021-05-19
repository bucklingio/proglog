## Random list

```python
import random

randomArray = []
randomArray.append(random.randint(1, 10))
randomArray.append(random.randint(11, 20))
randomArray.append(random.randint(21, 30))

index = random.randint(0, 2)
print(index)
print(randomArray[index])

randomArray[index] = random.randint(101, 200)

print(randomArray[index])
```

[Terug naar opdracht](/taken/randomlist.html)
[Terug naar cursus](/23_list.html)