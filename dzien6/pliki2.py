sciezka = "text1"

with open(sciezka) as plik:
    print(plik.readline())
    linijka = plik.readline()
    # pozycja = plik.tell()
    # print(f"Kursor znajduje się w pozycji nr{pozycja}")
    print(linijka, end='')
    print("Kolejna linijka")
#read zaczyna od miejsca gdzie jest ustawiony kursor
    print(plik.read())