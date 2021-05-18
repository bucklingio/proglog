String
======

Aantal tekens
-------------

De instructie `len()` geeft je het aantal tekens in een string.\
Je geeft een string mee als parameter. Je krijgt het aantal tekens als
return waarde.\
Je maakt volgend programma om dit te proberen:
_lengtestring.py_:

```python
voornaam = input("Voornaam: ")
aantalTekens = len(voornaam)
print("Aantal tekens in je voornaam: ", aantalTekens)
```

Je kan `len()` ook gebruiken om de lengte van lists te returnen.

Eén teken
---------

Elk teken in een string heeft een index, net zoals bij lists.\
De index van het eerste teken is 0.\
Je breidt het programma uit. Je toont één per één de tekens in de
voornaam:
```python
...
print("Aantal tekens in je voornaam: ", aantalTekens)
for i in range(aantalTekens):
    print(voornaam[i])
```
Je bewaart en voert uit.

![image](images/hardhat.png) [Aantal spaties](/taken/aantalspaties.html).\
![image](images/hardhat.png) [Palindroom](/taken/palindroom.html).\
![image](images/hardhat.png) [Aantal woorden](/taken/aantalwoorden.html).\
![image](images/hardhat.png) [Saus](/taken/saus.html).

<a class="btn" href="./26_listsenfuncties.html">&#9194; Lists en functies</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./28_unicode.html">Unicode &#9193;</a>