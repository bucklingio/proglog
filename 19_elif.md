Elif
====

`elif` is de afkorting van `else if`. Je kan hiermee de inhoud van een
variabele met verschillende mogelijke waarden vergelijken.\
Als de variabele gelijk is aan één van die waarden, voer je de
bijhorende instructies uit.\
`elif` vergelijkt de variabele dan niet meer met de andere waarden.\
Je begint een `elif` reeks altijd met een `if` instructie.\
Voorbeeld: De gebruiker tikt een landcode. Als de landcode `BE` is, toon
je de tekst `België`.\
Als de landcode `NL` is, toon je de tekst `Nederland`.\
Als de landcode `FR` is, toon je de tekst `Frankrijk`.\
Je maakt een nieuw bestand _landcodes.py_ . Je schrijft
volgende instructies:

```python
landCode = input("Landcode: ")
if landCode == "BE":
    print("België")
elif landCode == "NL":
    print("Nederland")
elif landCode == "FR":
    print("Frankrijk")
```

Als de gebruiker een landcode intikt die verschilt van `BE`, `NL` en
`FR` laat het programma niets zien.\
Je voegt een regel toe, zodat je programma de tekst `Onbekende code`
toont.
```python
    ...
    print("Frankrijk")
else:
    print("Onbekende code.")
```

Je kan binnen een `elif` reeks ook nesten.

![image](images/hardhat.png) [Afstanden](/taken/afstanden.html)\
![image](images/hardhat.png) [Rekenmachine](/taken/rekenmachine.html).

Nieuw in Python 3.10: Structural Pattern Matching (match)
======================================

Als je werkt met Python 3.10 of later, kan je een nieuwe schrijfwijze gebruiken om een variabele met mogelijke waarden te vergelijken.
Het voorbeeld hierboven kan je met deze nieuwe schrijfwijze als volgt schrijven:
```python
landCode = input("Landcode: ")
match landcode:                   // je gebruikt het keyword 'match', gevolgd door de variabele die je wil controleren
    case "BE":                    // je gebruikt het keyword 'case', gevolgd door de waarde die je verwacht
        print("België")
    case "NL":
        print("Nederland")
    case "FR":
        print("Frankrijk")
    case _:                       // in plaats van de 'else', gebruik je nu de 'case _' om iets uit te voeren bij een onbestaande case
        Print("Onbekende code.")
```

Je kan deze schrijfwijze uitproberen op de oefeningen 'afstanden' en 'rekenmachine'.

<a class="btn" href="./18_for.html">&#9194; For</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./20_functies.html">Functies &#9193;</a>
