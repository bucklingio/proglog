Else
====

Je opent het bestand _weer.py_. Je wil ook iets uitvoeren
als de voorwaarde bij `if` *niet waar* is.\
Voorbeeld: je toont de tekst `Een lichte jas volstaat.` enkel als de
temperatuur *niet* kleiner of gelijk is aan 0.\
Je voegt daartoe een else onderdeel toe aan de if:

```python
temperatuur = float(input("Temperatuur: "))
if temperatuur <= 0:
    print("Het vriest.")
    print("Je doet beter een dikke jas aan.")
else:
    print("Een lichte jas volstaat.")
print("Einde van het programma.")
```

Let goed op de indentering. `else` staat weer naar links, en je `print`
weer naar rechts.\
Je bewaart en voert uit. Enkel als je een temperatuur tikt groter dan 0
zie je de tekst `Een lichte jas volstaat.`

![image](images/hardhat.png) [Kind](/taken/kind.html).\
![image](images/hardhat.png) [Kelvin](/taken/kelvin.html).\
![image](images/hardhat.png) [Even](/taken/even.html).

<a class="btn" href="./11_if.html">&#9194; If</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./13_meerdereif.html">Meerdere if &#9193;</a>