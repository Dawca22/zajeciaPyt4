class Ubrania(object):
    def __init__(self, marka, rozmiar, kolor):
        self.marka = marka
        self.rozmiar = rozmiar
        self.kolor = None


class But(Ubrania):
   def __init__(self, marka, rozmiar, plec):
       super().__init__(marka, rozmiar)
       self.plec = plec


class OdziezWierzchnia(Ubrania):


class Szpilka(But):
    def __init__(self, marka, wysokosc, rozmiar, plec):
        super().__init__(marka, None, "Kobiecy")
        self.wysokosc = wysokosc


class Polbut(But):

class Plaszcz(OdziezWierzchnia):

ubranko = Ubranie("hm", "40")
print(ubranko)

bucik = But("adidas", "43")
print(bucik)