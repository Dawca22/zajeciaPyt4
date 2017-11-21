sciezka = "text1"

tekst = "Nowa linia"
with open(sciezka, "r+") as plik:

    plik.read()

   pozycja = plik.tell()
   plik.seek(pozycja - 1)

   ostatni_znak = plik.read()
   print(ostatni_znak)