## Vijf getallen

```python
getal = int(input("Getal: "))
laagste = getal
hoogste = getal
for teller in range(1,5):
    getal = int(input("Getal: "))
    if getal < laagste:
        laagste = getal
    if getal > hoogste:
        hoogste  = getal
print("Laagste getal:", laagste)
print("Hoogste getal:", hoogste)
```

[Terug naar opdracht](/taken/vijfgetallen.html)
[Terug naar cursus](/18_for.html)