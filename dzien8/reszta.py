# napisz program wydajacy reszte z zakupów

# zakupy - warosc, place banknotem
#wydać moentami o nominała 5-0.1
# jak najmniej monet wydać

monety ={5:0,2:0,1:0,0.5:0,0.2:0,0.1:0}

wartosc_zak = 11.30
banknot = 20

reszta = round(banknot - wartosc_zak, 2)
print("wydaj:", reszta)

if reszta < 0:
    print ("Za mała warość banknotu")
    quit()
elif reszta == 0:
    print("Bez reszty.")
    quit()

for moneta in monety.keys():
   if reszta >= moneta:
       ilosc = reszta // moneta
       monety[moneta] = ilosc
       reszta = round(reszta - (moneta * ilosc),2)
       print("Tyle reszty jeszcze jest:", reszta)

# print("wydać:")
# for moneta, ilosc in monety.items():
#     print(f"moneta: {moneta:>4} - {ilosc:>4} sztuk.")