## Palindroom

```python
def isPalindroom(woord):
    for i in range(len(woord)//2):
        if woord[i] != woord[len(woord) - 1 - i]:
            return False
        else:
            return True

woord = input("Woord: ")
if isPalindroom(woord):
    print("Palindroom.")
else:
    print("Geen palindroom.")
```

[Terug naar opdracht](/taken/palindroom.html)
[Terug naar cursus](/27_string.html)