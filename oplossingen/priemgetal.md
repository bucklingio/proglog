## Priemgetal

```python
getal = int(input("Getal: "))
isPriemgetal = True
if getal < 1:
    print("Geen priemgetal.")
else:
    if getal < 4:
        print("Priemgetal.")
    else:
        helft = getal / 2
        deler = 2
        while deler <= helft and getal % deler != 0:
            deler += 1
        if deler > helft:
            print("Priemgetal.")
        else: 
            print("Geen priemgetal.")
```

[Terug naar opdracht](/taken/priemgetal.html)
[Terug naar cursus](/17_nognesten.html)