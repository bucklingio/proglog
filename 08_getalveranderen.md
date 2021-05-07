Een getalvariabele veranderen
=============================

Je moet regelmatig een variabele die een getal bevat, met een waarde
verhogen of verlagen.\
Voorbeeld: Je hebt drie kinderen. Je onthoudt dit in een variabele
`aantalKinderen`.\
Als nog een tweeling geboren wordt, verhoog je de variabele met twee.\
Je creëert een nieuw bestand _tweeling.py_. Je voert
volgende regels in:
```
aantalKinderen = 3
aantalKinderen = aantalKinderen + 2
print(aantalKinderen)
```
Je bewaart en voert uit. Je krijgt volgende uitvoer te zien:
```
5
```
Je kan de waarde van een berekening met een variabele, weer in dezelfde
variabele stoppen.\
Er bestaat ook een kortere schrijfwijze.\
Je vervangt de regel `aantalKinderen = aantalKinderen + 2` door volgende
regel:
```
...
aantalKinderen += 2
...
```
Je bewaart en voert uit. Je krijgt dezelfde uitvoer te zien.\
Je kan deze schrijfwijze ook toepassen op delen (`/=`), vermenigvuldigen
(`*=`), en aftrekken (`-=`).

![image](images/hardhat.png) Ticket: zie takenbundel.