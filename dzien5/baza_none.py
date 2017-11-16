def dodaj_imie(imie, baza=None):
    """Dodaje imie do bazy, jesli baza nie
    istnieje, tworzy nową bazę
    (str, [list]"""

    if baza == None:
        baza =[]

    imie = imie.upper()
    baza.append(imie)
    return baza

anglicy = dodaj_imie("john")
print(anglicy)
francuzi = dodaj_imie("antoin")
print(francuzi)