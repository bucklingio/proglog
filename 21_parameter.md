Parameter
=========

Je opent het bestand _evenoneven.py_.\
De functie is niet flexibel: ze kan enkel van de variabele `getal`
zeggen of het even of oneven is.\
Je voegt in het hoofdprogramma volgende regel toe:
```python
...
getal = int(input("Getal: "))
tweedeGetal = int(input("Tweede getal: "))
(*\textcolor{gray}{evenOneven()}*)
```
Je kan de functie niet oproepen om te zeggen of dit tweede getal even of
oneven is.\
De oplossing: aan de functie een parameter toevoegen.\
Een parameter is een waarde (string, getal, ...) die je meegeeft bij de
oproep van de functie.\
Je kan bij elke oproep een *andere* waarde meegeven als parameter.\
Je kan in de functie de waarde lezen en er berekeningen mee doen.\
Je voegt een parameter toe aan de functie `evenOneven()`:
```python
def evenOneven(eenGetal):
    if eenGetal % 2 == 0:
        print("Even")
        ...
```
Telkens je de functie oproept moet je een waarde meegeven voor de
parameter `eenGetal`. Je wijzigt het hoofdprogramma:
```python
...
tweedeGetal = int(input("Tweede getal: "))
evenOneven(getal)    
evenOneven(tweedeGetal)
```
Je vermeldt bij de eerste oproep de variabele `getal` als parameter.\
Je programma roept de functie op.\
Je programma vult de parameter `eenGetal` met de waarde in de variabele
`getal`.\
Als de variabele `getal` 10 bevat, bevat de parameter `eenGetal` ook de
waarde 10.\
De code in de functie toont de tekst `Even`.\
Bij de tweede oproep vermeld je de variabele `tweedeGetal`.\
Bij het uitvoeren bevat de parameter `eenGetal` de waarde van de
variabele `tweedeGetal`.\
Je kan, naast variabelen, ook waarden als parameter gebruiken. Je voegt
volgende regel toe aan je programma:
```python
...
evenOneven(tweedeGetal)
evenOneven(3)
```
Je bewaart en test het programma.

Meerdere parameters
-------------------

Een functie kan *meerdere* parameters hebben. Het *type* van de
parameters kan verschillen.\
Voorbeeld: Je maakt een procedure die een lijn tekent.\
De eerste parameter is het *teken* waarmee je de lijn tekent.\
De tweede parameter is het *aantal* tekens in de lijn.\
Je maakt het bestand _tekenlijn.py_:

```python
def tekenLijn(teken, aantal):
    lijn = ""
    for i in range(1, aantal + 1):
        lijn += teken
    print(lijn)


tekenLijn("=", 5)
tekenLijn("-", 10)
```

Je begint met de lege string `lijn`.\
Je voegt, met een `for`, `aantal` keer `teken` aan `lijn` toe.\
Daarna toon je `lijn` op het scherm.\
Je bewaart en voert uit.

![image](images/hardhat.png) Tussen: zie takenbundel\
![image](images/hardhat.png) Machtsverheffing: zie takenbundel

Meerdere parameters
-------------------

Een functie kan *meerdere* parameters hebben. Het *type* van de
parameters kan verschillen.\
Voorbeeld: Je maakt een procedure die een lijn tekent.\
De eerste parameter is het *teken* waarmee je de lijn tekent.\
De tweede parameter is het *aantal* tekens in de lijn.\
Je maakt het bestand _tekenlijn.py_:

```python
def tekenLijn(teken, aantal):
    lijn = ""
    for i in range(1, aantal + 1):
        lijn += teken
    print(lijn)


tekenLijn("=", 5)
tekenLijn("-", 10)
```

Je begint met de lege string `lijn`.\
Je voegt, met een `for`, `aantal` keer `teken` aan `lijn` toe.\
Daarna toon je `lijn` op het scherm.\
Je bewaart en voert uit.

![image](images/hardhat.png) Tussen: zie takenbundel\
![image](images/hardhat.png) Machtsverheffing: zie takenbundel

<a class="btn" href="./20_functies.html">&#9194; Functies</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./22_functiesmetreturn.html">Functies met return &#9193;</a>