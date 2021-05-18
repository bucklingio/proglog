Dictionary
==========

Algemeen
--------

Je beschrijft met een dictionary (afgekort als **dict**) een verzameling
attributen (key) met hun waarde (value).\
Je beschrijft bijvoorbeeld de eigenschappen van een rechthoek.\
De rechthoek heeft een lengte van 3, een breedte van 2, en een rode
kleur.

```python
rechthoek = {"lengte": 3, "breedte": 2, "kleur": "rood"}

print(rechthoek["lengte"])
rechthoek["lengte"] = 4
print(rechthoek["lengte"])
```

Je maakt een dict als een verzameling **key:value** paren tussen `{ }`.\
Je typt per attribuut de naam (bijvoorbeeld `lengte`) en de waarde
(bijvoorbeeld `3`) van het attribuut.\
Je leest de waarde van een attribuut als `naamDict["naamAttribuut"]` of\
`naamDict.get("naamAttribuut")`.\
Je wijzigt de waarde van een attribuut met
`naamDict["naamAttribuut"] = nieuweWaarde`.\
Je kan complexere dicts leesbaarder schrijven door elk attribuut op een
nieuwe regel te schrijven.

```python
rechthoek = {
    "lengte": 3, 
    "breedte": 2, 
    "kleur": "rood"
}
print(rechthoek["lengte"])
rechthoek["lengte"] = 4
print(rechthoek["lengte"])
```

Je kan de waarde van de attributen ook vragen aan de gebruiker:

```python
rechthoek = {
    "lengte": int(input("Lengte: ")),
    "breedte": int(input("Breedte: ")),
    "kleur": input("Kleur: "),
}

print(rechthoek.get("lengte"), rechthoek.get("breedte"), rechthoek.get("kleur"))
```

Let op met het gebruik van attributen in f-strings! Gebruik in een
f-string nooit dubbele aanhalingstekens voor je key, maar enkele
aanhalingstekens:

      mijnString = f"De value is {mijnDict['mijnKey']}"

Een key in een dictionary is **altijd uniek**.

List
----

Je maakt een verzameling van 2 rechthoeken. Je doet dit door een list te
maken die 2 dicts bevat:

```python
rechthoeken = [
    {"lengte": 3, "breedte": 2, "kleur": "rood"},
    {"lengte": 7, "breedte": 4, "kleur": "groen"},
]
for rechthoek in rechthoeken:
    print(rechthoek.get("lengte"), rechthoek.get("breedte"), rechthoek.get("kleur"))
```

Ook hier kan je de gebruiker de list laten maken:

```python
rechthoeken = []

lengte = int(input("Lengte: "))
while lengte != 0:
    rechthoeken.append(
        {
            "lengte": lengte,
            "breedte": int(input("Breedte: ")),
            "kleur": input("Kleur: "),
        }
    )
    lengte = int(input("Lengte: "))

for rechthoek in rechthoeken:
    print(rechthoek.get("lengte"), rechthoek.get("breedte"), rechthoek.get("kleur"))
```

Dict als attribuut
------------------

Een attribuut van een dict kan zelf een dict zijn:

```python
adres = {
    "straat": "Keizerslaan",
    "huisnummer": "11",
    "gemeente": {"postcode": 1000, "naam": "Brussel"},
}
print(adres.get("gemeente").get("naam"))
print(adres["gemeente"]["naam"])
```

List als attribuut
------------------

Een attribuut van een dict kan ook een list zijn:

```python
persoon = {"familienaam": "Desmet", "voornamen": ["Hans", "Cyriel"]}

for voornaam in persoon.get("voornamen"):
    print(voornaam)
```

![image](images/hardhat.png) [BMI](/taken/bmi.html).

<a class="btn" href="./28_unicode.html">&#9194; Unicode</a>
<a class="btn" href="./index.html">&#9195; Index</a>
<a class="btn" href="./30_tuples.html">Tuples &#9193;</a>