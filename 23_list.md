List
=====

Elke variabele die je tot nu toe maakte bevat één waarde.

-   De variabele `voornaam` bevat één tekst (bv. `Mia`).

-   De variabele `temperatuur` bevat één getal (bv. 7).

Een list is een variabele die *meerdere* waarden bevat.\
Programmeurs spreken over de *elementen* in een list als ze de waarden
in een list bedoelen.\
Lists worden in andere talen ook *arrays* genoemd.\
Je maakt als voorbeeld een variabele met de naam `voornamen`.\
De variabele bevat drie elementen: `Ann`, `Jos` en `Mia`.

Elk element heeft een volgnummer. De nummering begint vanaf **0**.\
Dit is wennen: je nummert als mens vanaf **1**!\
Je ziet hier de list, met boven elk element het volgnummer van
dat element:
<table border="1">
<tr>
    <th>0</th>
    <th>1</th>
    <th>2</th>
</tr>
<tr>
    <td>Ann</td>
    <td>Jos</td>
    <td>Mia</td>
</tr>
</table>

Programmeurs spreken over de *index* van een element als ze het
volgnummer bedoelen.\
Voorbeelden van variabelen die een list zijn:

-   `voetbalploeg` bevat 11 elementen. Elk element bevat de naam van een
    speler.

-   `provincies` bevat 10 elementen. Elk element bevat de naam van een
    provincie.

-   `maandelijkseNeerslag` bevat 12 elementen. Elk element bevat de
    hoeveelheid neerslag die in een maand gevallen is.

Je leert in de volgende hoofdstukken praktische toepassingen van lists.

Voorbeeld
---------

Je maakt een programma dat

1.  een list variabele `voornamen` maakt met 3 elementen: `Ann`, `Jos`
    en `Mia`.

2.  het element met index 0 op het scherm toont.

Je maakt een nieuw bestand _voornamen.py_:

```python
voornamen = ["Ann", "Jos", "Mia"]
print(voornamen[0])
```

Je bewaart en voert uit.\
Je beschrijft een list in Python met vierkante haakjes \[ \]. Je
scheidt de verschillende elementen met een komma.\
Je selecteert een element uit een list met de naam van de list,
gevolgd door de index van het element tussen vierkante haakjes.

Je wijzigt het programma. Je vraagt een volgnummer aan de gebruiker:

```python
voornamen = ["Ann", "Jos", "Mia"]
index = int(input("Volgnummer: "))
if index >= 0 and index <= 2:
    print(voornamen[index])
```

Je bewaart en voert uit.

Element wijzigen
----------------

Je maakt een nieuw bestand _werknemers.py_.\
Je maakt een list met de namen van de werknemers van een firma.

```python
werknemers = ["Joe Jackson", "Donald Duck", "Martha Muffin"]
```

Donald Duck gaat met pensioen. Een nieuwe werknemer wordt aangeworven:
Olga Obama.\
Je voegt een regel toe om het tweede element van de list te vervangen.
Dit element heeft als index 1.

```python
werknemers = ["Joe Jackson", "Donald Duck", "Martha Muffin"]
werknemers[1] = "Olga Obama"
```

Je toont daarna dit element op het scherm. Je programma ziet er als
volgt uit:

```python
werknemers = ["Joe Jackson", "Donald Duck", "Martha Muffin"]
werknemers[1] = "Olga Obama"
print(werknemers[1])
```

Je bewaart en voert uit.\
Je kan het nummer van de werknemer die met pensioen gaat vragen aan de
gebruiker.\
Je kan ook de naam van de nieuwe werknemer vragen aan de gebruiker.\
Je wijzigt daartoe het programma:

```python
werknemers = ["Joe Jackson", "Donald Duck", "Martha Muffin"]
index = int(input("Volgnummer van de werknemer die met pensioen gaat: "))
while index < 0 or index > 2:
    index = int(input("Verkeerd volgnummer, probeer opnieuw: "))
nieuweWerknemer = input("Nieuwe werknemer: ")
werknemers[index] = nieuweWerknemer
print(werknemers[index])
```

![image](images/hardhat.png) [Geluksgetallen](/taken/geluksgetallen.html).\
![image](images/hardhat.png) [Random list](/taken/randomlist.html).

<a class="btn" href="./22_functiesmetreturn.html">&#9194; Functies met return</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./24_forin.html">For in &#9193;</a>
