#podane 3 boki trójkąta określ
#     czy uda się narysować trójkąt
#     długość jednego boku musi być < długości sumy dwóch pozostałych
#     czy jest to trójkąt różnoboczny, równoramienny, równoboczny

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

if bok_a < bok_b + bok_c and \
    bok_b < bok_a + bok_c and \
    bok_c < bok_a + bok_b:
    print("Uda się narysować trójkąt")

    if bok_a == bok_b and bok_b == bok_c:
      print('trójkąt równoboczny')
    elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt różnnoboczny")