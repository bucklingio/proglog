woord = input("Woord in kleine letters: ")
hoofdletterWoord = ""

for i in range(len(woord)):
    kleineLetter = woord[i]
    getalVanKleineLetter = ord(kleineLetter)
    getalVanHoofdletter = getalVanKleineLetter - 32
    hoofdletter = chr(getalVanHoofdletter)
    hoofdletterWoord += hoofdletter

print(hoofdletterWoord)
