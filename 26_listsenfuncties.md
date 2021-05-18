Lists en functies
==================

Parameter
---------

De parameter van een functie kan een list zijn.\
Je maakt een eenvoudig voorbeeld.\
De functie `toonSteden` heeft een parameter `steden`. Dit is een list.\
De functie itereert over de elementen in de list en toont elk element.\
Je roept in het hoofdprogramma de procedure op met een list van steden
in Vlaanderen.\
Je roept daarna de functie nog eens op met en list vaan steden in
Wallonië.\
Je maakt een nieuw bestand _steden.py_ .

```python
def toonSteden(steden):
    for stad in steden:
        print(stad)


toonSteden(["Antwerpen", "Gent", "Brugge"])
toonSteden(["Luik", "Charleroi", "Bergen", "Namen"])
```

Returnwaarde van functie
------------------------

Een list kan ook de returnwaarde van een functie zijn.\
Je voegt een functie toe aan _steden.py_\
Die geeft een list terug met de grootste steden van Nederland.\
Je roept deze functie op als parameter van de functie `toonSteden()`.

```python
def toonSteden(steden):
    for stad in steden:
        print(stad)


def grootsteStedenVanNederland():
    return ["Amsterdam", "Rotterdam", "Den Haag"]


toonSteden(["Antwerpen", "Gent", "Brugge"])
toonSteden(["Luik", "Charleroi", "Bergen", "Namen"])
toonSteden(grootsteStedenVanNederland())
```

Je bewaart en voert uit.

![image](images/hardhat.png) [Vanaf gemiddelde](/taken/vanafgemiddelde.html).\
![image](images/hardhat.png) [Unieke invoer](/taken/uniekeinvoer.html).\
![image](images/hardhat.png) [Mastermind](/taken/mastermind.html).

<a class="btn" href="./25_toevoegen.html">&#9194; Toevoegen</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./27_string.html">String &#9193;</a>