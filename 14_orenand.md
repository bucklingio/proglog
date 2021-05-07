OR en AND
=========

Je leert voorwaarden combineren met _Or_ en met
_And._

Or
--

De toegangsprijs in een pretpark is €5 als je leeftijd lager is dan 7
**of** hoger is dan 80. Anders is de toegangsprijs €10.\
De eerste zin bevat *twee* voorwaarden:

-   leeftijd lager dan 7

-   leeftijd hoger dan 80

De voorwaarden worden gecombineerd met `or` (of).\
Bij _or_ is de combinatie waar (True) als één van de twee
voorwaarden waar (True) is.\
[Voorbeeld 1]{.ul}: een bezoeker met een leeftijd van 4 jaar.

-   De eerste voorwaarde (leeftijd \< 7) is waar.

-   De tweede voorwaarde (leeftijd \> 80) is onwaar.

-   Omdat de eerste voorwaarde waar is, is de combinatie ook waar. De
    bezoeker betaalt €5.

[Voorbeeld 2]{.ul}: een bezoeker met een leeftijd van 90 jaar.

-   De eerste voorwaarde (leeftijd \< 7) is onwaar.

-   De tweede voorwaarde (leeftijd \> 80) is waar.

-   Omdat de tweede voorwaarde waar is, is de combinatie ook waar. De
    bezoeker betaalt €5.

[Voorbeeld 3]{.ul}: een bezoeker met een leeftijd van 45 jaar.

-   De eerste voorwaarde (leeftijd \< 7) is onwaar.

-   De tweede voorwaarde (leeftijd \> 80) is onwaar.

-   Omdat geen enkele voorwaarde waar is, is de combinatie onwaar. De
    bezoeker betaalt €10.

Je maakt dit programma. Je maakt een nieuw bestand
_prijs.py_. Je schrijft volgende regels:

```python
leeftijd = int(input("Leeftijd: "))
if leeftijd < 7 or leeftijd > 80:
    print("Prijs: €5")
else:
    print("Prijs: €10")
```

Je bewaart en test je programma met verschillende leeftijden.

And
---

Je maakt een programma dat je BMI (Body Mass Index) berekent.\
Het BMI bereken je als volgt: gewicht gedeeld door het kwadraat van de
lengte.\
Als je BMI ligt tussen 18.5 **en** 25 heb je een normaal gewicht.\
Deze zin bevat twee voorwaarden:

-   BMI groter of gelijk aan 18.5

-   BMI kleiner of gelijk aan 25

De voorwaarden worden gecombineerd met **en** (`and`). Bij `and` is de
combinatie enkel waar als *alle* voorwaarden waar zijn.\
underlineVoorbeeld 1: een BMI van 15.

-   De eerste voorwaarde (bmi \>= 18.5) is onwaar.

-   De tweede voorwaarde (bmi \<= 25) is waar.

-   Omdat de eerste voorwaarde onwaar is, is de combinatie onwaar. Het
    gewicht is niet ok.

[Voorbeeld 2:]{.ul} een BMI van 30.

-   De eerste voorwaarde (bmi \>= 18.5) is waar.

-   De tweede voorwaarde (bmi \<= 25) is onwaar.

-   Omdat de tweede voorwaarde onwaar is, is de combinatie onwaar. Het
    gewicht is niet ok.

[Voorbeeld 3:]{.ul} een BMI van 23.

-   De eerste voorwaarde (bmi \>= 18.5) is waar.

-   De tweede voorwaarde (bmi \<= 25) is waar.

-   Omdat *alle* voorwaarden waar zijn, is de combinatie waar. Het
    gewicht is ok.

Je maakt een nieuw bestand aan met de naam _bmi.py_ . Je
schrijft volgende regels:

```python
gewicht = float(input("Gewicht in kilogram: "))
lengte = float(input("Lengte in meter: "))
bmi = gewicht / lengte ** 2
if (bmi >= 18.5 and bmi <= 25):
    print("OK")
```

![image](images/hardhat.png) Café: zie takenbundel\
![image](images/hardhat.png) Leeftijd: zie takenbundel