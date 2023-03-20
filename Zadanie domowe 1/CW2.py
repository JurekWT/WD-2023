def zad11():
    print("Podaj wysokość diamentu (w przedziale 3-9): ")
    a = int(input())
    if a < 3 or a > 9:
        print("Zła wysokość")
        return 0
    elif a%2==1:
        for i in range(1, a + 1, 2):
            print(" " * (a - i // 2) + "*" * i)
        for i in range(a - 2, 0, -2):
            print(" " * (a - i // 2) + "*" * i)
    else:
        for i in range(1, a + 1, 2):
            print(" " * (a - i // 2) + "*" * i)
        for i in range(a - 1, 0, -2):
            print(" " * (a - i // 2) + "*" * i)


zad11()


def zad15():
    try:
        liczba = int(input('Podaj liczbę\n'))
    except ValueError:
        print('Nie podano liczby')


zad15()
