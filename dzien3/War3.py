#oblicz czy rok jest przestepny

# podzelny przez 4 i  nie podzielny przez 100 ale podzielny przez 400

# rok = input("Podaj rok:\n")
# rok=int(rok)

rok = int(input("Podaj rok:\n "))

#czy jest podzielny przez 400
if rok % 400 == 0:
    print(f"Rok {rok} jest przestępny")

#czy jest podzielny przez 4,% modulo != różne == równe
elif rok % 4 == 0 and rok % 100 != 0:
    print(f"Rok {rok} jest przestępny")

else:
    print(f"Rok {rok} nie jest przestępny")