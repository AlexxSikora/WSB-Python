import math


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True  # czyli cos jak else; w tym przypadku return True jest liczbą pierwszą


def print_result(result):
    if result:
        print("liczba pierwsza")
    else:
        print("Zlozona")

#Pierwszy Sposob
t=int(input("podaj liczbe przypadkow: \n")
while t:
    x=int(input("podaj liczbe do sprawdzenia: \n"))
    result = is_prime(x)
    print_result(result)
    t-=1
#DRUGI SPOSOB
#print_result(is_prime(int(input("podaj liczbe do sprawdzeni \n"))))