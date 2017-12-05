from zajeciaPyt4.dzien10.zwierze import Zwierze

class Kot(Zwierze):
    def __init___(self, nazwa, kolor):
        super().__init__(nazwa)
        self.kolor = kolor


     def ruszaj_sie(self):
        print(f"Kotek {self.nazwa} ruszy sie!")