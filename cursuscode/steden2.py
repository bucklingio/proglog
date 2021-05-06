def toonSteden(steden):
    for stad in steden:
        print(stad)


def grootsteStedenVanNederland():
    return ["Amsterdam", "Rotterdam", "Den Haag"]


toonSteden(["Antwerpen", "Gent", "Brugge"])
toonSteden(["Luik", "Charleroi", "Bergen", "Namen"])
toonSteden(grootsteStedenVanNederland())
