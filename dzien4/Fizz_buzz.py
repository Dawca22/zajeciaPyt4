#Fizz buzz (jeżeli liczba podzielna przez 3  fiz jeżeli podzielna przez 5 to buzz jeżeli podzielna przez 3 i 5 to FizzBuzz

# zakres = range(101)
#
# for element in zakres:
#    if element % 3 == 0:
#        print("Fizz")
#    if element % 5 == 0:
#        print("Buzz")
#

# zakres = range(1, 101)
#
# for liczba in zakres:
#     if liczba %3 == 0 and liczba % 5 == 0:
#         print("FizzBuzz")
#     elif liczba % 5 == 0:
#         print("Buzz")
#     elif liczba % 3 == 0:
#         print("Fizz")
#     else:
#         print(liczba)


# zakres = range(1, 101)
#
# for liczba in zakres:
#     if liczba % 15 == 0:
#         print("FizzBuzz")
#     elif liczba % 5 == 0:
#         print("Buzz")
#     elif liczba % 3 == 0:
#         print("Fizz")
#     else:
#         print(liczba)

zakres = range(1, 101)

for liczba in zakres:
    if liczba % 3 == 0:
        print("Fizz", end="")
    if liczba % 5 == 0:
        print("Buzz", end="")
    if liczba % 3 != 0 and liczba % 5 != 0:
        print(liczba, end="")

    print("\n", end="")
