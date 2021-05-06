adres = {
    "straat": "Keizerslaan",
    "huisnummer": "11",
    "gemeente": {"postcode": 1000, "naam": "Brussel"},
}
print(adres.get("gemeente").get("naam"))
print(adres["gemeente"]["naam"])