from zajeciaPyt4.dzien10.czlowiek import Czlowiek

class Stundent(Czlowiek):
    def __init__(self, indeks):
        super().__init__("anonimowy", 19)
        self.indeks = indeks

    def ruszaj_sie(self):
        print("Nie chce mi sie, jestem po imprese")

    def powiedz(self):
        print("Poprosze o tróje!")

    def swieruj_egzamin(self):
        print("Na zdrowie")