Nesten
======

Je kan binnen `if`-blokken opnieuw een `if` plaatsen. Men spreekt dan
over 'nesten'.\
Het is aan jou om na te denken over hoe je dit nesten gebruikt naarmate
je grotere programma's maakt.\
Voorbeeld: Je laat de gebruiker een temperatuur intikken. Als de
temperatuur kleiner of gelijk is aan 0 (controle met een `if`) zijn er
nog twee mogelijkheden:

-   Als de temperatuur lager is dan -40, toon je de tekst `Blijf thuis`.

-   Anders toon je de tekst `Doe een dikke jas aan`.

Je nest een `if-else` *binnen* de eerste `if` om de ene of de andere
tekst te tonen.\
Je maakt een nieuw bestand _thuis.py_. Je schrijft volgende
regels:

```python
temperatuur = float(input("Temperatuur: "))
if temperatuur <= 0:
    if temperatuur < -40:
        print("Blijf thuis.")
    else:
        print("Doe een dikke jas aan.")
```

Je bewaart en voert uit.

-   Als je een positieve temperatuur intikt toont je programma niets.

-   Als je een temperatuur intikt lager dan -40 zie je `Blijf thuis.`.

-   Als je een temperatuur intikt tussen 0 en -40 zie je
    `Doe een dikke jas aan.`.

![image](images/hardhat.png) [VDAB](/taken/vdab.html)\
![image](images/hardhat.png) [Grootste](/taken/grootste.html)\
![image](images/hardhat.png) [Examens](/taken/examens.html)\
![image](images/hardhat.png) [Schrikkeljaar](/taken/schrikkeljaar.html)\
![image](images/hardhat.png) [Kindergeld](/taken/kindergeld.html)

<a class="btn" href="./14_orenand.html">&#9194; Or en And</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./16_while.html">While &#9193;</a>
