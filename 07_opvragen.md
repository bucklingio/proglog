Opvragen
========

Je opent het bestand _persoon.py_. Het programma is niet
flexibel:

-   De voornaam Mia staat in je programma. Als Piet het programma
    gebruikt en wil dat Mia wordt vervangen door zijn naam, moet hij het
    programma wijzigen. Dit is niet de bedoeling: de gebruiker van je
    programma moet niet kunnen programmeren.

-   Het aantal kinderen staat in je programma. Als Piet het programma
    gebruikt en dat aantal wil vervangen door zijn eigen aantal
    kinderen, moet hij het programma wijzigen.

Om het programma flexibel te maken

-   tik je de voornaam niet in je programma terwijl *jij* het programma
    maakt,

-   maar laat je de *gebruiker* zijn voornaam intikken tijdens de
    uitvoering van het programma. Je onthoudt de getikte tekst in de
    variabele `voornaam`.

Je doet dit als voorbeeld met de voornaam:

1.  je vervangt de regel `voornaam = "Mia"` door volgende regel:
    ```python
    voornaam = input()
    ...
    ```
    De instructie `input()` laat je toe informatie te tikken in het
    terminalscherm. Python bewaart de invoer daarna in de variabele
    `voornaam`.

2.  Wanneer de gebruiker de tekst intikt kan je hem uitleggen wat hij
    moet tikken. Deze uitleg zet je tussen de haakjes van `input()`. Je
    past de regel aan:
    ```python
    voornaam = input("Wat is je voornaam? ")
    ...
    ```
Je bewaart en voert uit. De gebruiker kan nu zijn voornaam intikken. Als
hij de voornaam _Piet_ intikt, zie je dat de variabele
`voornaam` de tekst _Piet_ bevat:
```
Piet
3
True
4
480
```
Je vraagt ook het aantal kinderen aan de gebruiker.

**Opgepast!** Het type van de functie `input()` is **altijd** een
string.

Als je met je invoer wil rekenen, moet je de invoer omzetten naar een
getal.\
Je kan hiervoor de functie `int()` gebruiken voor gehele getallen, en
`float()` voor reële getallen.\
Je probeert dit hier al uit, ook al gaan we met de invoer niet rekenen.

1.  Je vervangt de regel `aantalKinderen = 3` door volgende regel:
```python
...
aantalKinderen = int(input("Hoeveel kinderen heb je?"))
...
```
2.  Je verwijdert de regel `aantalKinderen = 4`.

Je bewaart en voert uit.

![image](images/hardhat.png) Rechthoek: zie takenbundel.\
![image](images/hardhat.png) Cirkel: zie takenbundel.

<a class="btn" href="./06_variabelen.html">&#9194; Variabelen</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./08_getalveranderen.html">Getal veranderen &#9193;</a>