Functies met return
===================

Een functie kan een waarde (string, getal, ...) als resultaat teruggeven
aan de code die de functie heeft opgeroepen.\
Je gebruikt hiervoor de instructie `return`.\
Je maakte in de takenbundel de functie `machtsverheffing()`.\
Deze functie berekent de machtsverheffing van een getal en toont het
resultaat.\
Het is de functie zelf die beslist wat er met het resultaat gebeurt: op
het scherm tonen.\
Het hoofdprogramma kan niet beslissen om iets anders te doen met dit
resultaat, zoals dit resultaat in een variabele te bewaren.\
De `return` instructie geeft het resultaat van de functie als een waarde
aan het hoofdprogramma.\
Het hoofdprogramma beslist wat er met dit resultaat gebeurt: op het
scherm tonen, in een variabele onthouden, in een berekening
gebruiken,...\
Op deze manier wordt een functie veel flexibeler.\
Je maakt als voorbeeld een functie met de naam `grootste()`.\
De functie heeft twee parameters, beide zijn getallen.\
De functie geeft als resultaat het grootste van de twee getallen terug.\
Het hoofdprogramma beslist wat er met dit resultaat gebeurt.\
Je maakt een nieuw bestand _grootste.py_:

```python
def grootste(getal1, getal2):
    if getal1 > getal2:
        grootste = getal1
    else:
        grootste = getal2
    return grootste


print(grootste(3, 4))
```

De functie geeft als resultaat de inhoud van de variabele `grootste`
terug.\
Je roept in het hoofdprogramma de functie op, Je toont het resultaat op
het scherm.\
Je voegt volgende regels toe aan je programma:

```python
grootsteGetal = grootste(float(input("Getal 1: ")), float(input("Getal 2: ")))
print("Het kwadraat van het grootste getal is ", grootsteGetal**2)
```

Je gebruikt hier `input` instructies als parameter.\
Je programma vraagt je één voor één de waarde van elke parameter.\
Je programma voert daarna de functie `grootste()` uit met de ingevoerde
waarden.\
Je programma bewaart deze waarde in de variabele `grootsteGetal`.\
Daarna gebruikt je programma deze variabele om het kwadraat te berekenen
en op het scherm te tonen.

![image](images/hardhat.png) Machtsverheffing 2: zie takenbundel.\
![image](images/hardhat.png) Grootste even: zie takenbundel.\
![image](images/hardhat.png) Grootste gemene deler: zie takenbundel.

<a class="btn" href="./21_parameter.html">&#9194; Parameter</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./23_list.html">List &#9193;</a>