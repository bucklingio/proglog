## Naar kleine letters

```python
zin = input("Tik een zin: ")
nieuweZin = ""

for teken in zin:
    tekengetal = ord(teken)
    if tekengetal >= 65 and tekengetal <= 90:
         kleineLetter = chr(tekengetal + 32)
         nieuweZin += kleineLetter
    else:
        nieuweZin += teken
        
print(nieuweZin)
```

[Terug naar opdracht](/taken/naarkleineletters.html)
[Terug naar cursus](/28_unicode.html)