rzeczy = ("pisak", "długopis", "szklanka", "portfel", "myszka")
kolory = ("czerwony", "zielony", "niebieski", "fioletowy", )
print(type(rzeczy))
# x jest koloru: y

#while

indeks = 0
dlugosc = min(len(rzeczy), len(kolory))

while indeks <dlugosc:
    print(f"{rzeczy[indeks]} jest koloru: {kolory[indeks]}")
    indeks +=1

#for + zip weźmie krótszą liste pod uwagę

for rzecz, kolor in zip(rzeczy, kolory):
    print(f"{rzecz} jest koloru: {kolor}")
