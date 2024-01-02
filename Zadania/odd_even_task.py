numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
for n in numbers:
    if n == 0:
        print("Zero jest parzyste")
    elif n % 2 != 0:
        print(n, " Liczba jest parzysta")
    else:
        print(n, " Liczba jest nieparzysta")
