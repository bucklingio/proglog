Vergelijken
===========

Je moet in veel programma's waarden vergelijken. Bijvoorbeeld: je
programmeert een spelletje.\
Je vergelijkt dan de score van de speler met de hoogste score van de
vorige spelers.\
Als de score van de speler *groter* is dan de hoogste score
(vergelijking), wijzig je de hoogste score naar de score van die
speler.\
Je leert hier hoe je eenvoudige vergelijkingen doet in je programma.

Getallen
--------

Je maakt een getal dat controleert of 5 groter is dan 3.

1.  Je maakt een nieuw bestand _vergelijken.py_.

2.  Je voegt volgende regel toe:

        print(5 > 3)

    Je kan op verschillende manieren vergelijken:

    -   `==` : Zijn twee getallen gelijk?

    -   `!=` : Zijn ze verschillend?

    -   `<` : Is het eerste *kleiner dan* het tweede?

    -   `<=` : Is het eerste *kleiner of gelijk aan* het tweede?

    -   `>` : Is het eerste *groter dan* het tweede?

    -   `>=` : Is het eerste *groter of gelijk aan* het tweede?

Let op de dubbele `==`. Je gebruikt de enkele `=` in Python om een
waarde te geven aan een variabele.\
Je gebruikt de dubbele `==` om twee waarden te vergelijken.\
Je bewaart en voert uit. Je krijgt volgende uitvoer te zien:

        True

Dit betekent: het is waar (True) dat 5 groter is dan 3. Je kan ook
variabelen vergelijken.\
Voorbeeld: Je vraagt je eigen lengte. Je vraagt de lengte van je
buurman. Je vergelijkt beide lengtes.\
Vervang de regel in je programma door volgende regels:

    mijnLengte = float(input("Wat is jouw lengte?"))
    lengteBuurman = float(input("Wat is de lengte van je buurman?"))
    print(mijnLengte > lengteBuurman)

Je bewaart en voert uit.\
[Let op:]{.ul} Als je de instructie `float()` niet gebruikt, gaat Python
de getallen alfabetisch vergelijken: 11 is dan bijvoorbeeld kleiner dan
2, omdat 1 voor 2 komt.

Strings
-------

Je kan ook strings vergelijken.\
Een string is 'groter' dan een tweede string als de string alfabetisch
*na* de tweede string komt.\
De string _Benny_ is bijvoorbeeld 'groter' dan de string
_Agnetha_.\
Een string is 'kleiner' dan een tweede string als de string alfabetisch
*voor* de tweede string komt.\
De string _appel_ is bijvoorbeeld 'kleiner' dan de string
_peer_.\
Je voegt volgende regel toe aan je programma:

    ...
    (*\textcolor{gray}{print(mijnLengte > lengteBuurman)}*)
    print("limonade" < "bier")

Je bewaart en voert uit. De tweede uitvoer is `False`.\
Het is onwaar (False) dat de string _limonade_ alfabetisch
voor de string _bier_ komt.

![image](images/hardhat.png) Vergelijken: zie takenbundel.

<a class="btn" href="./09_concateneren.html">&#9194; Concateneren</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./11_if.html">If &#9193;</a>