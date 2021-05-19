## Schrikkeljaar

```python
jaar = int(input("Jaar: "))
if jaar % 4 == 0:
    if jaar % 100 == 0:
        if jaar % 400 == 0:
            print("Schrikkeljaar")
        else:
            print("Geen schrikkeljaar")
    else:
        print("Schrikkeljaar")
else:
    print("Geen schrikkeljaar")
```

[Terug naar opdracht](/taken/schrikkeljaar.html)
[Terug naar cursus](/15_nesten.html)