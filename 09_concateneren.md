Concateneren
============

Je gebruikt tot nu toe `print()` om iets op het scherm te tonen.\
`print()` toont zijn informatie op het scherm en zorgt ervoor dat de
volgende informatie op een nieuwe regel getoond wordt.\
Je wil soms informatie *naast elkaar* tonen.\
Je gebruikt dan het _+_-teken binnen de haakjes van de
`print()` om verschillende stukken informatie naast elkaar te tonen.\
Dit noemt men **concateneren**.

Concateneren van strings
------------------------

Je maakt een nieuw bestand _concateneren.py_. Je voert
volgende regels in:

    print("Een.")
    print("Twee." + "Drie." + "Vier")
    print("Vijf.")    

Je bewaart en voert uit. Je krijgt volgende uitvoer te zien:

        Een.
        Twee.Drie.Vier.
        Vijf.

[Let op]{.ul}: Als je spaties wil weergeven, ga je deze zelf in je
strings moeten toevoegen.

Concateneren van andere types
-----------------------------

Je voegt een nieuwe regel toe:

    ...
    (*\textcolor{gray}{print("Vijf.")}*)
    print("Zes." + 7 + "Acht.")

Je bewaart en voert uit.\
Je krijgt nu een foutmelding te zien:\
`TypeError: can only concatenate str (not "int") to str`.\
Python kan geen getallen (of logische waarden) concateneren met
strings.\
Je lost dit op door het getal om te zetten naar een string. Dit doe je
met de functie `str()`.\
Je verandert de laatste regel van je programma:

    ...
    (*\textcolor{gray}{print("Vijf.")}*)
    print("Zes." + str(7) + "Acht.")

Je bewaart en voert uit. Je krijgt volgende uitvoer te zien:

        Een.
        Twee.Drie.Vier.
        Vijf.
        Zes.7Acht.

Om de uitvoer leesbaarder te maken, voegen we in de laatste regel
spaties toe aan het einde van `"Zes."` en aan het begin van `"Acht."`:

    ...
    (*\textcolor{gray}{print("Vijf.")}*)
    print("Zes. " + str(7) + " Acht.")

Je bewaart en voert uit. Je krijgt volgende uitvoer te zien:

        Een.
        Twee.Drie.Vier.
        Vijf.
        Zes. 7 Acht.

Een alternatief voor print()
----------------------------

Je kan binnen de instructie `print()` ook een komma gebruiken om
verschillende elementen na elkaar op het scherm te tonen.\
Je hoeft dan getallen en booleans niet om te zetten naar string. Je
hoeft dan ook geen extra spaties te zetten tussen de verschillende
elementen.\
[Let op:]{.ul} dit werkt enkel binnen de instructie `print()`!\
Je verandert de laatste regel van je programma:

        ...
        (*\textcolor{gray}{print("Vijf.")}*)
        print("Zes.", 7, "Acht.")

Je bewaart en voert uit. Je krijgt dezelfde uitvoer te zien.

![image](images/hardhat.png) Vierkant: zie takenbundel.