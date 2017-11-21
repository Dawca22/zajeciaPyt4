sciezka = "text1"

#usunał całą zawartość bo zapisywał od początku jako w

tekst = """To jest mój tekst. To 
jest kolejna linijka tekstu,
a to kolejna."""

with open(sciezka, 'r+') as plik:
    print(plik.tell())
    plik.seek(0)
    plik.read()
    # plik.write(tekst)