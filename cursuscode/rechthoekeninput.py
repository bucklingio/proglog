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