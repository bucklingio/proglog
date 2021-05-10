Tuples
======

Algemeen
--------

Tuples zijn verzamelingen van waarden, net zoals lists. Tuples kan je
echter niet wijzigen, ze zijn **immutable**.\
Je schrijft tuples met ronde haakjes.

      mijnTuple = (45, 60, 75)

Voorbeeld
---------

Je maakt een programma dat

1.  een tuple variabele `voornamen` maakt met 3 elementen: `Ann`, `Jos`
    en `Mia`.

2.  het element met index 0 op het scherm toont.

Je maakt een nieuw bestand [voornamentuple.py]{.sans-serif}:

```python
voornamen = ("Ann", "Jos", "Mia")
print(voornamen[0])
```

Je bewaart en voert uit.

Je wijzigt het programma. Je vraagt een volgnummer aan de gebruiker:

```python
voornamen = ("Ann", "Jos", "Mia")
index = int(input("Volgnummer: "))
if index >= 0 and index <= 2:
    print(voornamen[index])
```

Je bewaart en voert uit.

Immutable
---------

Je maakt een nieuw bestand [werknemerstuple.py]{.sans-serif}.\
Je maakt een tuple met de namen van de werknemers van een firma.

```python
werknemers = ("Joe Jackson", "Donald Duck", "Martha Muffin")
```

Donald Duck gaat met pensioen. Een nieuwe werknemer wordt aangeworven:
Olga Obama.\
Je voegt een regel toe om het tweede element van de list te vervangen.
Dit element heeft als index 1.

```python
werknemers = ("Joe Jackson", "Donald Duck", "Martha Muffin")
werknemers[1] = "Olga Obama"
```

Je toont daarna dit element op het scherm. Je programma ziet er als
volgt uit:

```python
werknemers = ("Joe Jackson", "Donald Duck", "Martha Muffin")
werknemers[1] = "Olga Obama"
print(werknemers[1])
```

Je bewaart en probeert uit te voeren. Je krijgt een foutmelding:

    Traceback (most recent call last):
      File "werknemerstuple.py", line 2, in <module>
        werknemers[1] = "Olga Obama"
    TypeError: 'tuple' object does not support item assignment

Je kan de inhoud van een tuple niet wijzigen.

For in
------

De instructie `for ... in` leest in een iteratie één per één alle tuple
elementen.\
Je maakt een nieuw bestand [for-in-tuple.py]{.sans-serif}

```python
voornamen = ("Ann", "Jos", "Mia")
for voornaam in voornamen:
    print(voornaam)
```

De schrijfwijze is hetzelfde als de `for ... in` instructie die we reeds
geleerd hebben, maar deze keer itereren we over een tuple in plaats van
een list.\
Je bewaart en voert uit. Je ziet één per één de voornamen.\
Je kan `for in` combineren met alle instructies die je al kent.

<a class="btn" href="./29_dictionary.html">&#9194; Dictionary</a>
<a class="btn" href="./index.html">&#9195; Index</a>