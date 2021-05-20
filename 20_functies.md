Functies
========

Elk programma dat je tot nu toe maakte is één reeks instructies.\
Echte programma's kunnen groot worden. Ze bevatten soms duizenden
opdrachten.\
Het is dan niet meer haalbaar deze opdrachten in één geheel te plaatsen.

-   Het wordt moeilijk om de grote ljinen te begrijpen van wat je
    programma doet.

-   Het wordt moeilijk om in team te werken. In een team willen
    verschillende programmeurs verschillende onderdelen van het
    programma maken.

-   Je begint stukken code te herhalen. Dit heeft nadelen: als deze code
    fouten bevat, moet je de code op meerdere plaatsen corrigeren. Als
    je deze code op een andere manier kan verbeteren (bijvoorbeeld
    sneller doen werken), dan moet je deze aanpassing op *meerdere*
    plaatsen doen.

De oplossing: je programma opsplitsen in kleinere delen. Men noemt die
delen subroutines.\
Voorbeeld: een webshop.

-   De gebruiker voegt producten toe aan zijn winkelmandje. Je plaatst
    de code die je daarvoor nodig hebt in een subroutine met de naam\
    `productenToevoegenAanWinkelmandje()`. We zetten ronde haakjes op
    het einde van de functienaam. Dit doen we ook in de code. Hiermee
    onderscheiden we een functie van een variabele.

-   De gebruiker bekijkt zijn winkelmandje. Je plaatst de code die je
    daarvoor nodig hebt in een subroutine `winkelMandjeTonen()`.

-   De gebruiker betaalt. Je plaatst de code die je daarvoor nodig hebt
    in een subroutine `betalen()`.

Je programma voert de code in een subroutine niet automatisch uit.\
Je programma voert de code enkel uit als jij de subroutine oproept.\
Jij beslist op welke plaats in je programma je een subroutine oproept.\
Je kan een subroutine ook *meerdere keren* oproepen.\
In Python (en veel andere talen) noemen we deze subroutines *functies*.\
Voorbeeld: een programma toont hoe je pannenkoeken bakt.\
Als je nadenkt kom je tot de conclusie dat het programma twee kleinere
delen bevat:

-   Ingrediënten tonen.\
    Je plaatst de code die dit doet in een functie
    `ingredientenTonen()`.

-   Bereiding tonen.\
    Je plaatst de code die dit doet in een functie `bereidingTonen()`.

Je maakt de functies `ingredientenTonen()` en `bereidingTonen()`.\
Je maakt een nieuw bestand _pannenkoeken.py_. Je maakt de
functie `bereidingTonen()`:

```python
def ingredientenTonen():
    print("INGREDIËNTEN:")
    print("250 gram zelfrijzende bloem")
    print("3 eieren")
    print("50 cl melk")
    print("een zakje vanillesuiker")


def bereidingTonen():
    print("BEREIDING:")
    print("Zeef de bloem met de vanillesuiker.")
    print("Voeg de eieren en de melk toe.")
    print("Bak de pannenkoeken in een pan met boter.")
```

Je begint het schrijven van een functie met `def`. Daarmee *definieer*
je de functie.\
Een functienaam eindig je met ronde haakjes.\
Als je nu het programma uitvoert gebeurt er niets. Je programma voert de
code van een functie niet automatisch uit.\
Python voert functies enkel uit als jij ze oproept. Je voegt daarvoor
volgende regels toe:
```python
    ...
    print("Voeg de eieren en de melk toe.")

ingredientenTonen()
bereidingTonen()
```
Hou rekening met de volgorde: definieer eerst je functie voor je ze
uitvoert.\
Je programma ziet er nu zo uit (je ziet duidelijk da het programma twee
onderdelen bevat):

```python
def ingredientenTonen():
    print("INGREDIËNTEN:")
    print("250 gram zelfrijzende bloem")
    print("3 eieren")
    print("50 cl melk")
    print("een zakje vanillesuiker")


def bereidingTonen():
    print("BEREIDING:")
    print("Zeef de bloem met de vanillesuiker.")
    print("Voeg de eieren en de melk toe.")
    print("Bak de pannenkoeken in een pan met boter.")


ingredientenTonen()
bereidingTonen()
```

Je bewaart en voert het programma uit.\
Je programma roept eerst de functie `ingredientenTonen()` op en voert de
code van die functie uit.\
Je programma roept daarna de functie `bereidingTonen()` op en voert de
code van die functie uit.\
Het hoofdprogramma bevat nu enkel twee regels: de oproepen van de
functies.\
Het hoofdprogramma kan ook uitgebreider zijn.\
Je wijzigt het hoofdprogramma zodat de gebruiker kan kiezen om de
ingrediënten te zien of de bereiding te zien.
```python
    ...
    print("Voeg de eieren en de melk toe.")

keuze = int(input("1=ingrediënten, 2=bereiding, 0=stop: "))
while keuze != 0:
    if keuze == 1:
        ingredientenTonen()
    elif keuze == 2:
        bereidingTonen()
    else:
        print("Verkeerde keuze.")
    keuze = int(input("1=ingrediënten, 2=bereiding, 0=stop: "))
```
Je bewaart en voert uit.

![image](images/hardhat.png) [België](/taken/belgie.html).

Je kan in een functie alle instructies gebruiken die je al kent.\
Je maakt een voorbeeld. De gebruiker tikt in het hoofdprogramma een
getal.\
Je roept een functie op met de naam `evenOneven()`.\
Je toont in die functie `Even` als het getal even is. Anders toon je
`Oneven` .\
Je maakt een nieuw bestand _evenoneven.py_. Je schrijft
volgend programma:

```python
def evenOneven():
    if getal % 2 == 0:
        print("Even")
    else:
        print("Oneven")


getal = int(input("Getal: "))
evenOneven()
```

Je bewaart en voert uit.\
Je kan in een functie een andere functie oproepen.\
Je maakt een voorbeeld. Je roept in het hoofdprogramma de functie
`ajuinSoep()` op.\
Je roept in de functie `ajuinSoep()` een functie `ingredienten()` op.\
Je roept daarna in de functie `ajuinSoep()` een functie `bereiding()`
op.\
Je maakt een nieuw bestand _ajuinsoep.py_:

```python
def ingredienten():
    print("INGREDIËNTEN:")
    print("6 uien")
    print("1 klontje boter")
    print("peper")
    print("zout")


def bereiding():
    print("BEREIDING:")
    print("Snij de uien.")
    print("Bak de uien met de boter.")


def ajuinSoep():
    print("AJUINSOEP")
    print("----------")
    ingredienten()
    bereiding()

ajuinSoep()
```

Je bewaart en voert uit.

![image](images/hardhat.png) [Geluk](/taken/geluk.html).

<a class="btn" href="./19_elif.html">&#9194; Elif</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./21_parameter.html">Parameter &#9193;</a>