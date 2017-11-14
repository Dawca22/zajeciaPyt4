#ile jest samogłosek i spółgłosek w stringu

zdanie = input("Podaj jakieś zdanie: ")

samogloski = 0
spolgloski = 0

lista_samoglosek = "aeiouyąęó"

for litera in zdanie:

    #sorawdza czy to w ogóle litera
    if litera.isalpha():
            if litera in lista_samoglosek:
                samogloski += 1
            else:
                spolgloski += 1

print(f"Samogłoski {samogloski}, spółgłoseki: {spolgloski}")

