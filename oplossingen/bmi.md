## BMI

```python
personen = []
naam = input("Naam: ")
while naam != "stop":
    personen.append(
        {
            "naam": naam,
            "lengte": float(input("Lengte in m: ")),
            "gewicht": float(input("Gewicht in kg: ")),
        }
    )
    naam = input("Naam: ")

for persoon in personen:
    bmi = persoon["gewicht"] / (persoon["lengte"] ** 2)
    print(f"{persoon['naam']}: BMI: {round(bmi, 2)}")
```

[Terug naar opdracht](/taken/bmi.html)
[Terug naar cursus](/29_dictionary.html)