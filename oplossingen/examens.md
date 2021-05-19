## Examens

```python
wiskunde = int(input("Geef de punten voor wiskunde: "))
boekhouden = int(input("Geef de punten voor boekhouden: "))
informatica = int(input("Geef de punten voor informatica: "))

if wiskunde >= 6 and boekhouden + informatica >= 12:
    print("De student is geslaagd.")
else:
    print("De student is niet geslaagd.")
    if wiskunde < 6:
        print("De student is niet geslaagd voor wiskunde.")
    if boekhouden + informatica < 12:  
        print("De student is niet geslaagd voor boekhouden en informatica.")
```

[Terug naar opdracht](/taken/examens.html)
[Terug naar cursus](/15_nesten.html)