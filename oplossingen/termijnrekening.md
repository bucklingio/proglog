## Termijnrekening

```python
beginkapitaal = float(input("Beginkapitaal: "))
looptijd = int(input("Looptijd in jaren: "))
intrestPercentage = float(input("Intrest in procent: "))
for jaar in range (1, looptijd + 1):
    beginkapitaal += beginkapitaal * intrestPercentage / 100
    print("Jaar", jaar, ":", round(beginkapitaal, 2))
```

[Terug naar opdracht](/taken/vijfgetallen.html)
[Terug naar cursus](/18_for.html)