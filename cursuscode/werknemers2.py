werknemers = ["Joe Jackson", "Donald Duck", "Martha Muffin"]
index = int(input("Volgnummer van de werknemer die met pensioen gaat: "))
while index < 0 or index > 2:
    index = int(input("Verkeerd volgnummer, probeer opnieuw: "))
nieuweWerknemer = input("Nieuwe werknemer: ")
werknemers[index] = nieuweWerknemer
print(werknemers[index])
