Meerdere bewerkingen
====================

Je opent het programma met de naam _rekenen.py_ .\
Een berekening bevat soms *meerdere* bewerkingen.\
Voorbeeld: _2 + 3 x 4_ bevat een + bewerking en een x
bewerking.\
Je programma voert sommige bewerkingen uit *voor* andere bewerkingen.

1.  Eerst machtsverheffingen (`**`).

2.  Daarna modulo bewerkingen (`%`).

3.  Daarna vermenigvuldigen en delen (`*`, `/` en `//`).

4.  Tenslotte optellen en aftrekken (`+` en `-`).

In het voorbeeld _2 + 3 x 4_ voert je programma dus eerst
_3 x 4_ uit.\
Daarna telt je programma 2 op bij 12 (de uitkomst van _3 x
4_).\
Het eindresultaat bij de berekening is dus 14.\
Je wil soms *zelf* bepalen dat een bewerking *voor* een andere bewerking
wordt uitgevoerd.

Voorbeeld: je wil bij _2 + 3 x 4_ eerst de + uitvoeren,
daarna de x.\
Je drukt dit in wiskunde uit met ronde haakjes: _(2 + 3) x
4_.\
Bewerkingen tussen ronde haakjes worden eerst uitgevoerd.\
Het resultaat is 20: eerst _2 + 3_, daarna dit resultaat
_(5) x 4_.\
Je drukt dit in Python op dezelfde manier uit.

Je voegt volgende regels toe aan je programma:
```python
...
print(2 + 3 * 4)
print((2 + 3) * 4)
```
Je bewaart en voert het programma uit. In je uitvoer zie je onderaan de
getallen 14 en 20.

![image](images/hardhat.png) [Percentage](/taken/percentage.html).

<a class="btn" href="./04_getallen.html">&#9194; Getallen</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./06_variabelen.html">Variabelen &#9193;</a>

