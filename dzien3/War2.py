#nazwisko = "Kowalska"

#if nazwisk[-1] == "a":
#   print('To kobieta')
#else nazwisko[-1] != "a":
#    print ('To mężczyzna')

#print ("Koniec programu")

nazwisko = input("Podaj nazwisko:\n ")

#print(type(nazwisko))

#jeśli w stringu są cyfry napisać komunikat i przerwać program
if not nazwsiko.isalpha():
    print("Muszą być tylko litery")

#usunąć whistpace z początku i końca
naz_czyste = nazwisko.strip()
#nazwisko = nazwisko.strip()
#zamienić wszystkie litery na duże
naz_czyste = nazwisko.upper()

print(naz_czyste)

if naz_czyste [-1] == "A":
    print("Chyba jesteśn kobietą.")

elif naz_czyste.endswith ("SKI"):
    print("Najprawdopodobniej jesteś mężczyzną")

elif naz_czyste.isupper():
    print("Chyba jesteś złośliwa :/")


print ("Koniec programu")

