Meerdere If Blokken
===================

Je opent het bestand _weer.py_. Je programma bevat zoveel
`if` instructies als je nodig hebt.\
Je breidt je programma uit: je vraagt aan de gebruiker of het zal
regenen.\
Enkel als hij `ja` antwoordt, toon je de tekst `Neem een paraplu mee.`\
Je voegt volgende regels toe:
```python
temperatuur = float(input("Temperatuur: "))
regen = input("Zal het regenen? (tik ja of nee):")
if temperatuur <= 0:
    print("Het vriest.")
    print("Je doet beter een dikke jas aan.")
else:
    print("Een lichte jas volstaat.")
if regen == "ja":
        print("Neem een paraplu mee.")
print("Einde van het programma.")
```

Let op de dubbele `==`.\
Je bewaart en voert uit.

![image](images/hardhat.png) Delen: zie takenbundel.

<a class="btn" href="./12_else.html">&#9194; Else</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./14_orenand.html">Or en And &#9193;</a>