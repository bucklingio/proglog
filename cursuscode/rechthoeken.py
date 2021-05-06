rechthoeken = [
    {"lengte": 3, "breedte": 2, "kleur": "rood"},
    {"lengte": 7, "breedte": 4, "kleur": "groen"},
]
for rechthoek in rechthoeken:
    print(rechthoek.get("lengte"), rechthoek.get("breedte"), rechthoek.get("kleur"))