#kolejna nie ma znaczenia
#1 w przypadku oli to klucz

elementy = { 0:"ala", 1:"ola", 2:"ela"}
print(elementy)

print(elementy[1])\

slownik = {"imie": "Adam","nazwisko": "wczesniak", "wiek":32}
#
# print(slownik.keys())
# print(slownik.values())
# for klucz, wartosc in slownik.items():
#     print(f"Klucz: {klucz} ma wartosc {wartosc}")
#
# if "adres" in slownik.keys():
#     print("Adres dostepny")
# else:
#     print("Adres niedostepny")

print(slownik)
slownik["adres"]= "Gdańsk"
print(slownik)
slownik["adres"] = "Gdynia"
print(slownik)
