def zad8(*liczby):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
        for i in liczby:
            iloczyn *= i
        print(iloczyn)


zad8(1, 5, 6, 8)


def zad9(suma=0, **produkty):
    for i in produkty:
        suma += produkty[i]
    print('Ilość produktów:', suma)


zad9(cziperki=5, cola=4, monsterki=12)


def zad11(a,b,c):
    from ciagi import arytm, geom
    print(arytm.suma(a, b, c))
    print(arytm.nty(a, b))
    print(geom.nty(a, b, c))
    print(geom.suma(a))
    print(geom.nty(a))


zad11(1,2,4)
