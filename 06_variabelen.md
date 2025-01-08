Variabelen
==========

Een variabele is een plaats in het interne geheugen van je computer
(RAM). Je bewaart gegevens in een variabele: een string, een getal of
een logische waarde.\
Voorbeeld: je maakt een variabele. Je bewaart er je voornaam in. Je kan
verder in je programma de informatie uit de variabele lezen, en er iets
mee doen: op het scherm tonen, of gebruiken in een berekening ...\
Je maakt zoveel variabelen als je denkt nodig te hebben. Je geeft elke
variabele een unieke naam. Je onderscheidt zo de variabelen van elkaar.\
Jij kiest zelf de naam voor elke variabele. De naam mag in de meeste
programmeertalen geen spaties bevatten en niet met een cijfer beginnen.
Je kiest een naam die duidelijk aangeeft waarvoor je de variabele
gebruikt.\
Dit maakt je programma leesbaar en makkelijker te begrijpen.

-   Je maakt een variabele `aantalKinderen`.\
    Je bewaart in deze variabele hoeveel kinderen je hebt.

-   Je maakt nog een variabele met de naam `zakgeld`.\
    Je bewaart in deze variabele hoeveel zakgeld elk kind krijgt.

Moderne programmeurs gebruiken een afspraak voor de schrijfwijze van
variabelen. Deze afspraak heet camelcase. Je tikt daarbij de naam van
een variabele in kleine letters.\
Als de naam bestaat uit meerdere woorden, begin je elk nieuw woord met
een hoofdletter. Je gebruikt geen spaties.\
Voorbeelden: `aantalKinderen`, `grootsteWedde`,
`kortingVoorGroteGezinnen`.

Opmerking
---------

Python heeft verschillende sleutelwoorden met een speciale betekenis. Deze woorden zijn gereserveerd voor de taal.\
Je mag deze woorden niet gebruiken als naam van een variabele.\
Je ken al een paar woorden: `print`, `True`, en `False`. Je mag geen variabele met de naam `print`, `True` of `False` maken. 

Voorbeeld
---------

Je maakt een voorbeeld:

-   Je maakt een variabele met de naam `voornaam`. De inhoud is de
    string `Mia`.

-   Je maakt een variabele met de naam `aantalKinderen`. De inhoud is
    het getal `3`.

-   Je maakt een variabele met de naam `gehuwd`. De inhoud is de waarde
    `True`.

-   Je toont daarna de inhoud van de variabelen.

Je maakt het programma.

1.  Je maakt een nieuw bestaand aan met de naam
    _persoon.py_.

2.  Je maakt een variabele aan met de naam `voornaam` en de waarde
    `"Mia"`. Je schrijft dit op volgende manier in Python.
```python
voornaam = "Mia"
```
3.  Je maakt een variabele aan met de naam `aantalKinderen` en de waarde
    `3`.

4.  Je maakt een variabele aan met de naam `gehuwd` en de waarde `True`.
```python
...
aantalKinderen = 3
gehuwd = True
```
5.  Je toont nu de waarde van de variabele `voornaam` in het
    uitvoerscherm.
```python
...
print(voornaam)
```
6.  Je toont ook de waarden van de variabelen `aantalKinderen` en
    `gehuwd`.
```python
...
print(aantalKinderen)
print(gehuwd)
```
7.  Je bewaart en voert uit.

Je ziet volgende uitvoer in het terminalvenster:
```python
Mia
3
true
```
Je programma ziet er nu zo uit:
```python
voornaam = "Mia"
aantalKinderen = 3
gehuwd = True
print(voornaam)
print(aantalKinderen)
print(gehuwd)
```

![image](images/hardhat.png) [Film](/taken/film.html).

Wijzigen
--------

Je kan de waarde van een variabele wijzigen (\"variabel\"). Je kan in de
loop van je programma een andere waarde in je variabele plaatsen.\
Voorbeeld: Mia krijgt nog een kind: het aantal kinderen wijzigt van 3
naar 4.\
Je opent het programma _persoon.py_. Je voegt onderaan
volgende regel toe:
```python
...
aantalKinderen = 4
print(aantalKinderen)
```

Je bewaart en voert uit. Je ziet volgende uitvoer in het
terminalvenster:
```
Mia
3
True
4
```

Gebruik in een berekening
-------------------------

Je kan de inhoud van een variabele gebruiken in een berekening.\
Voorbeeld: Mia krijgt €120 kindergeld per kind. Je berekent het totale
kindergeld als volgt: lees de inhoud van de variabele `aantalKinderen`
(4) en vermenigvuldig dit met 120.\
Je kan het resultaat van de berekening:

-   rechtstreeks tonen op het scherm

-   of bewaren in een nieuwe variabele, bijvoorbeeld `totaalKindergeld`.

Je kiest hier voor het rechtstreeks tonen. Voeg volgende regel toe aan
je programma:
```
...
print(aantalKinderen * 120)
```
Je bewaart en voert uit. Je ziet nu volgende uitvoer onderaan in het
terminalvenster:
```
480
```

![image](images/hardhat.png) [Lotto](/taken/lotto.html).

<a class="btn" href="./05_meerderebewerkingen.html">&#9194; Meerdere bewerkingen</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./07_opvragen.html">Opvragen &#9193;</a>
