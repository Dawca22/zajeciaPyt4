#sprawdź czy liczba jest w zakresie
liczby = [2,434,25,43,4,5765,756,7,3425,325,364]

# x - tak
# y - nie

def czy_w_zakresie(liczba, zakres=range(100)):
    """

    :param liczba:
    :param zakres:
    :return:
    """
    if liczba in zakres:
        print(f"{liczba} - Yes")
    else:
        print (f"{liczba} - No")

for x in liczby:
    czy_w_zakresie(x)
