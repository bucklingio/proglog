While
=====

De programma's die je tot nu toe gemaakt hebt, voeren opdrachten één
keer uit.\
Je moet soms bepaalde opdrachten *meerdere* keren uitvoeren zolang aan
een *voorwaarde* voldaan is.

Voorbeeld
---------

Je houdt bij hoeveel geld de mensen storten voor een goed doel.\
Telkens iemand een bedrag stort, tikt de gebruiker dit bedrag en toon je
de opbrengst. Als de actie voorbij is stopt het programma.\
We spreken af dat de gebruiker dan `0` tikt, waar hij normaal een bedrag
tikt.\
Je ziet volgend herhalend patroon: *zolang* (`while`) de gebruiker niet
`0` tikt:

1.  tel je het getikte bedrag bij de totale opbrengst

2.  en toon je de opbrengst.

Je programma *herhaalt* deze stappen zoveel keer als er mensen een
bedrag storten. Je programmeert zo'n herhaling met een nieuwe
instructie: `while`. Je maakt een nieuw bestand
_goededoel.py_.

1.  Je maakt een variabele met de naam `opbrengst`. Je initialiseert de
    variabele op 0. Je vraagt daarna aan de gebruiker een eerste
    gestorte bedrag:
    ```python
    opbrengst = 0
    gestort = float(input("Gestort bedrag (0 om te stoppen): "))
    ```

2.  *Zolang* de variabele `gestort` verschilt van 0, moet je programma
    enkele instructies uitvoeren. Je voegt daarvoor een `while`
    instructie toe. Je geeft de *voorwaarde* aan. *Zolang* deze waar
    (`True`) is, herhaalt je programma enkele instructies:

    -   een instructie die het gestorte bedrag optelt bij de opbrengst.

    -   een instructie die de opbrengst toont.

    -   een instructie waarmee de gebruiker het volgende bedrag kan
        intikken.

    ```python
    ...
    gestort = float(input("Gestort bedrag (0 om te stoppen): "))
    while gestort != 0:
        opbrengst += gestort
        print(opbrengst)
        gestort = float(input("Gestort bedrag (0 om te stoppen): "))
    ```

Je bewaart en voert uit.\
Opmerking: je programma kan *meerdere* `while` en/of `if` instructies
bevatten.\
Opmerking: een synoniem voor herhalen is *itereren*. Een synoniem voor
herhaling is *iteratie*.

![image](images/hardhat.png) [Gemiddelde](/taken/gemiddelde.html).

<a class="btn" href="./15_nesten.html">&#9194; Nesten</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./17_nognesten.html">Nog nesten &#9193;</a>