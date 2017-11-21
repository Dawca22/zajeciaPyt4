sciezka = "text1"

with open(sciezka) as plik:
    linijki =plik.readlines()

    for linijka in linijki:
        print(linijka)