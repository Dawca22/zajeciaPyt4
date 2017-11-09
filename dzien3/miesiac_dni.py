# po podaniu nazwy m-ca podaj ilośc dni

miesiac = input("Poodaj nazwę miesiąca: ")

if miesiac == 'kwiecien' or miesiac == 'czerwiec' \
        or miesiac == 'wrzesien' or miesiac == 'listopad':
    print(f'Miesiąc {miesiac} ma 30 dni.')

elif miesiac == 'luty':
    print ('Luty ma 28 lub 29 dni')

else:
    print(f"Miesiąc {miesiac} ma 31 dni.")