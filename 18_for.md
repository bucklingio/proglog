For
===

Je moet in veel programma's een variabele bij elke iteratie met een
waarde verhogen.\
Voorbeeld: je toont de getallen 1 tot en met 10. Je kan dit uitwerken
met `while`.

    getal = 1
    while getal <= 10:
        print(getal)
        getal += 1

Je kan het korter uitwerken met de `for` instructie.

    for getal in range(1, 11):
        print(getal)    

Let op: de eindwaarde (het tweede getal) in `range()` in Python is
altijd **exclusief**.\
Deze wordt dus nooit uitgevoerd.\
De iteratie stopt als de variabele de eindwaarde bereikt heeft.\
Je kan de instructie `range()` ook met één getal gebruiken. Je begint
dan automatisch van 0 te tellen.\
Voorbeeld: `range(20)` geeft je een bereik van 0 tot en met 19.\
Je kan aan de `range()` nog een derde waarde meegeven: deze waarde
bepaalt met hoeveel je de variabele verhoogt bij elke iteratie.\
Als je de *oneven* getallen tot 10 wil tonen, verhoog je het getal
telkens met 2:

    for getal in range(1, 11, 2):
        print(getal)    

Je kan ook het getal bij 10 starten en telkens met 1 verminderen om de
getallen omgekeerd te tonen.

        for getal in range(10, 0, -1):
            print(getal)    

Je kan hiervoor ook de instructie `reversed()` gebruiken:

    for getal in reversed(range(1, 11)):
        print(getal)    

Je kan binnen een `for` instructie een `if` instructie nesten.\
Je kan binnen een `for` instructie een `while` instructie nesten.\
Je kan ook binnen een `if` een `for` nesten en daarin een `while`,
etc...

![image](images/hardhat.png) Tafel: zie takenbundel.\
![image](images/hardhat.png) Som even: zie takenbundel.\
![image](images/hardhat.png) Vijf getallen: zie takenbundel.\
![image](images/hardhat.png) Termijnrekening: zie takenbundel.\
![image](images/hardhat.png) Rechthoek tekenen: zie takenbundel.\
![image](images/hardhat.png) Kader tekenen: zie takenbundel.\
![image](images/hardhat.png) Driehoek tekenen: zie takenbundel.

<a class="btn" href="./17_nognesten.html">&#9194; Nog nesten</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./19_elif.html">Elif &#9193;</a>