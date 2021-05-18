Unicode
=======

Een computer onthoudt alle data als getallen.

-   Dit is evident voor de variabele `aantalKinderen`. Als jij `3` in
    deze variabele stopt, onthoudt de computer dit als het getal 3.

-   Dit is minder evident voor de variabele `gehuwd`. Als jij `True` in
    deze variabele stopt, onthoudt de computer dit als 1. Als jij
    `False` in deze variabele stopt, onthoudt de computer dit als 0.

-   Dit is minder evident voor de variabele `voornaam`. Als jij `Mia` in
    deze variabele stopt, onthoudt de computer dit als de getallen 77,
    108 en 97. De tekst `Mia` bestaat uit 3 tekens. De computer onthoudt
    elk teken als een getal.

Er is een internationale standaard die definieert welk getal welk teken
voorstelt. De naam van deze standaard is Unicode.\
Unicode definieert niet enkel getallen voor tekens uit de westerse
wereld, maar ook voor andere tekens (Arabisch, Chinees, Japans, ...)\
Unicode is een uitbreiding van een oudere standaard: ASCII.\
ASCII was beperkt: er waren enkel getallen gedefinieerd voor tekens uit
de westerse wereld.\
Er zijn meer dan 140.000 karakters in Unicode. Het is dus onmogelijk en
onnodig om te onthouden welke getallen bij welke tekens horen.\
Het volgende is wel handig om te weten:

-   De letters A tot en met Z worden voorgesteld door opeenvolgende
    getallen: A=65, B=66, \... Z=90.

-   De letters a tot en met z worden voorgesteld door opeenvolgende
    getallen: a=97, b=98, \... Z=122.

-   De cijfers 0 tot en met 9 worden ook voorgesteld door opeenvolgende
    getallen. 0=48, 1=49, \... 9=57.

CHR
---

Python bevat de instructie `chr()`. Je geeft als parameter een getal
mee. Je krijgt als return waarde de letter terug die volgens Unicode bij
dit getal hoort.\
Voorbeeld: Je toont de hoofdletters in het alfabet. Je moet dus de
letters tonen die horen bij de getallen 65 tot en met 90.\
Je maakt een nieuw bestand _alfabet.py_:

```python
for i in range(65, 91):
    print(chr(i))
```

ORD
---

Python bevat de instructie `ord()`. Je geeft als parameter een teken
mee. Je krijgt als returnwaarde het getal terug dat volgens Unicode bij
dit teken hoort.\
Je maakt een voorbeeld. De gebruiker tikt een woord in kleine letters.
Jij toont dit woord in hoofdletters.\
Voorbeeld: de gebruiker tikt `aap`. Jij zet elke letter om naar zijn
getal: 97, 97, 80.\
Je trekt van elk getal 32 af. Je bekomt de getallen 65, 65, 80. Je zet
deze getallen om naar hun bijhorende tekens, en bewaart ze in een
string.\
Je toont daarna die string op het scherm: `AAP`. Je maakt een nieuw
bestand _hoofdletters.py_:

```python
woord = input("Woord in kleine letters: ")
hoofdletterWoord = ""

for i in range(len(woord)):
    kleineLetter = woord[i]
    getalVanKleineLetter = ord(kleineLetter)
    getalVanHoofdletter = getalVanKleineLetter - 32
    hoofdletter = chr(getalVanHoofdletter)
    hoofdletterWoord += hoofdletter

print(hoofdletterWoord)
```

![image](images/hardhat.png) [Naar kleine letters](/taken/naarkleineletters.html).\
![image](images/hardhat.png) [Letter statistiek](/taken/letterstatistiek.html).

<a class="btn" href="./27_string.html">&#9194; String</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./29_dictionary.html">Dictionary &#9193;</a>