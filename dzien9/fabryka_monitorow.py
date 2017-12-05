from zajeciaPyt4.dzien9.monitor import Monitor

monitor1 = Monitor("AOK", 19)

print(f"Monitor{monitor1.producent} ma przekątną "
      f" {monitor1.przekatna}  cali" )

monitor1.kolor = "czerwony"

print(monitor1.kolor)


monitor2 = Monitor("Asus", 24)
print(f"Monitor{monitor2.producent} ma przekątną "
      f" {monitor2.przekatna}  cali" )
print(monitor2.przekatna)

