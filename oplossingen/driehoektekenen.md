## Driehoek tekenen

```python
hoogte = int(input("Hoogte: "))
for hoogteTeller in range(hoogte):
    tekenString = ""
    for lengteTeller in range(hoogteTeller+1):
        tekenString += "*"
    print(tekenString)
```

[Terug naar opdracht](/taken/driehoektekenen.html)
[Terug naar cursus](/18_for.html)