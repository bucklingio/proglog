Nog nesten
==========

Je leerde dat je in een `if` nog een `if` kan nesten. De mogelijkheden
van nesten zijn eindeloos:

-   een `if` in een `while`

-   een `while` in een `if`

-   een `while` in een `while`

-   een `while` in een `if` in een `while`

-   ...

Voorbeeld: Een pretpark wil op het einde van de dag weten hoeveel
volwassenen het park bezochten en hoeveel kinderen het park bezochten.\
De gebruiker tikt de leeftijd van elke bezoeker.\
Als de leeftijd hoger of gelijk is aan 18, verhoog je de variabele voor
het aantal volwassenen met 1.\
Anders verhoog je de variabele voor het aantal kinderen met 1.\
Op het einde van de dag tikt de gebruiker `0` als leeftijd om het
invoeren te stoppen.\
Je toont dan het aantal volwassenen en het aantal kinderen.\
Je maakt een nieuw bestand _pretpark.py_. Je schrijft
volgende regels:

```python
aantalVolwassenen = 0
aantalKinderen = 0
leeftijd = int(input("Leeftijd (0 om te stoppen): "))
while leeftijd != 0:
    if leeftijd >= 18:
        aantalVolwassenen += 1
    else:
        aantalKinderen += 1
    leeftijd = int(input("Leeftijd (0 om te stoppen): "))
print("Aantal volwassenen: " + str(aantalVolwassenen))
print("Aantal kinderen: " + str(aantalKinderen))
```

Je ziet in het programma een `while` instructie met een geneste `if`
instructie.\
Je bewaart en test het programma.

![image](images/hardhat.png) [Korting](/taken/korting.html).\
![image](images/hardhat.png) [Temperaturen](/taken/temperaturen.html).\
![image](images/hardhat.png) [Hoger Lager](/taken/hogerlager.html).\
![image](images/hardhat.png) [Priemgetal](/taken/priemgetal.html).\
![image](images/hardhat.png) [KMI](/taken/kmi.html).

<a class="btn" href="./16_while.html">&#9194; While</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./18_for.html">For &#9193;</a>