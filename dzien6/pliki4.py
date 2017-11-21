sciezka = "text1"

with open(sciezka, 'a') as plik:
    print(plik.tell())

    plik.seek(-1)


    #kolejne linijki write
    plik.write("Moja kolejna linijka")