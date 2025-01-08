Elementen toevoegen aan lists
==============================

Je kan in Python makkelijk elementen toevoegen aan een list.\
Lists zijn in Python dynamisch: ze hebben geen vaste lengte.\
Je gebruikt de instructie `append()` om elementen toe te voegen aan een
list.

Voorbeeld: Je maakt een list van 20 willekeurige getallen tussen 1 en
100.\
Python heeft geen ingebouwde instructies voor het genereren van
willekeurige getallen.\
Je gaat hiervoor een aparte module importeren: `random`.\
`import` instructies zet je altijd bovenaan je programma.\
Je gebruikt de instructie `random.randint()` uit de module `random` voor
het genereren van willekeurige gehele getallen.\

Je begint met een lege list `getallen`.\
Je genereert een willekeurig getal, en voegt dit toe aan de list.\
Je herhaalt dit 20 keer via de `for` instructie. Je toont daarna de
getallen op het scherm.\
Je maakt een nieuw bestand _twintigelementen.py_:

```python
import random

getallen = []

for teller in range(20):
    randomGetal = random.randint(1, 100)
    getallen.append(randomGetal)

for getal in getallen:
    print(getal)
```
Je bewaart en voert uit.

Je maakt een tweede voorbeeld. Je maakt een lege list `voornamen`. De
gebruiker tikt 5 namen. Je vult daarmee de elementen van de list.\
Je toont daarna de elementen op het scherm. Je maakt een nieuw bestand
_vijfvoornamen.py_ .

```python
voornamen = []

for i in range(5):
    voornamen.append(input("Voornaam: "))

for voornaam in voornamen:
    print(voornaam)
```
Je bewaart en voert uit.

Je gebruikt de functie `len()` om het aantal elementen van de list op te vragen.\
Je maakt een derde voorbeeld. Je maakt een lege list voornamen. De gebruiker tikt
verschillende namen.\
Je vult daarmee de elementen van de list.\
Je stopt met toevoegen als de voornaam `STOP` gegeven wordt.\
Je toont eerst het aantal elementen op het scherm. Je toont ook alle namen op het scherm.`
Je maakt een nieuw bestand _listvoornamen.py_:

```python
naam = input("Geef voornaam:")
while naam != "STOP":
    voornamen.append(naam)
    naam = input("Geef voornaam:")

print("Aantal voornamen", len(voornamen))
for voornaam in voornamen:
    print(voornaam)
```
Je bewaart en voert uit.

![image](images/hardhat.png) [List wijzigen](/taken/listwijzigen.html)\
![image](images/hardhat.png) [Tafel list](/taken/tafellist.html).\
![image](images/hardhat.png) [Omgekeerd](/taken/omgekeerd.html).\
![image](images/hardhat.png) [Aantal voorkomens](/taken/aantalvoorkomens.html).\
![image](images/hardhat.png) [Willekeurige volgorde](/taken/willekeurigevolgorde.html).\
![image](images/hardhat.png) [Uniek](/taken/uniek.html).\
![image](images/hardhat.png) [Biljetten en munten](/taken/biljettenenmunten.html).

<a class="btn" href="./24_forin.html">&#9194; For in</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./26_listsenfuncties.html">Lists en functies &#9193;</a>
