def dodaj_imie(imie, baza=[]):
    imie = imie.upper()
    baza.append(imie)
    return baza
# imiona = ["ANNA", "DAMIAN"]
# dodaj_imie("andrzej", imiona)
# dodaj_imie("masrek",imiona)
#
# print(imiona)

anglicy = dodaj_imie("john")
print(anglicy)
francuzi = dodaj_imie("antoin")
print(francuzi)

