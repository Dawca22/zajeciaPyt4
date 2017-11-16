def wypisz_dane(imie, nazwisko, kurs="Python", il_dni=15):
    print(f"Kursant {imie} {nazwisko}, kurs: {kurs} trwa {il_dni} dni.")

wypisz_dane("Daniel", "Wcześniak")
wypisz_dane("Anna", "Kowalska", "Java")
wypisz_dane("Adam","Nowak","JS", 60)

wypisz_dane("Marta","K", il_dni=10)