## Letter statistiek

```python
letters = []
for index in range(26):
    letters.append(0)

woord = input("Woord: ")

for letter in woord:
    letters[ord(letter) - 97] += 1

for index in range(len(letters)):
    if letters[index] != 0:
        print(chr(index + 97), ":", letters[index])
```
[Terug naar opdracht](/taken/letterstatistiek.html)
[Terug naar cursus](/28_unicode.html)