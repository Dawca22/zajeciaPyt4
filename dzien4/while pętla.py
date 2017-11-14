# jeżeli jest fałsz to pętla się nie wykona
# Czy nazwisko jest wpisane wielkimi literami?

prawidlowe = False

while not prawidlowe:
    nazwisko = input("Podaj nazwisko drukowanymi literami lub Q aby zakończyć: ")

    if nazwisko.upper() == 'Q':
        print("Do widzenia.")
        quit()
    elif nazwisko.isalpha():
        if  nazwisko.isupper():
            prawidlowe = True

print ("Gratulacje, jesteś zarejestrowany.")





