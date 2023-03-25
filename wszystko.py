# Zadanie 1
# a = 1
# b = 8
# c = 'zmienna c'
# d = 'zmienna d'
# e = 23.88
# f = 14.88
# print(a, b, c, d)
# print(e)
# print(f)

# Zadanie 2
# a,b=2,5
# print(a+b)
# print(a/b)
# print(a*b)
# print(a%b)

# Zadanie 3
# from math import *
# print(exp(10))
# print(pow(log(5+pow(sin(8),2)),(1/6)))
# print(floor(3.55))
# print(ceil(4.80))

# Zadanie 4
# imie='JERZY'
# nazwisko='TYMOFIEJCZYK'
# print(capita)

# Zadanie 5
# a='string'
# b=12.50
# c=0x1000
# print('Zmienna a:%(z1)s' % {'z1':a})
# print('Zmienna b:%(z2)f' % {'z2':b})
# print('Zmienna c:%(z3)x' % {'z3':c})

# def zad6():
#     a = "I'm covering my ears like a kid\n" \
#         "When your words mean nothing, I go la la la\n" \
#         "I'm turning up the volume when you speak\n" \
#         "'Cause if my heart can't stop it\n" \
#         "I find a way to block it, I go\n" \
#         "La la, la la la la la na na na na na\n" \
#         "La la na na, la la la la la na na na na na\n" \
#         "I find a way to block it, I go\n" \
#         "La la na na, la la la la la na na na na na\n" \
#         "La la na na, la la la la la na na na na na\n"
#     print('Ilość "la" w tekście:', a.count('la'))
#
#
# zad6()

# def zad10():
#     lista = ['Kiler', 'Kilerów 2-óch', 'Django', 'Hari Pota', 'Interstellar', 'Incepcja', 'Władca Pierścieni',
#              'Zombeavers', 'Sarnie Żniwo']
#     print('Lista ulubionych filmów', lista)
#     lista.sort()
#     print('Lista po sortowaniu:', lista)
#
#
# zad10()

# def zad11():
#     from math import sin, cos, tan, radians
#     kat = [0, 30, 45, 60, 90]
#     s = [sin(radians(i)) for i in kat]
#     c = [cos(radians(i)) for i in kat]
#     t = [tan(radians(i)) for i in kat]
#     t[4] = 0
#     print('Kąt\tSinus\tCosinus\tTang')
#     for i in range(len(kat)):
#         print(f"{kat[i]}\t{s[i]:.2f}\t{c[i]:.2f}\t{t[i]:.2f}")
#
#
# zad11()


# Zadanie 12
# a='Ala ma kota i psa'
# wyrazy=a.split(' ')
# print(wyrazy)

# Zadanie 15
# rzymskie = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5,'VI':6,'VII':7}

# def zad13():
#     ksywy = {'Łysy': 'Łukasz Tymofiejczyk', 'Gruby': 'Jerzy Tymofiejczyk', 'Janek': 'Łukasz Januszewski',
#              'Mały': 'Łukasz Dostatni', 'Kwadrat': 'Arkadiusz Keller', 'Chudy': 'Oskar Głowacki',
#              'Kurak': 'Andrzej Cłapka', 'Peja': 'Ryszard Waldemar Andrzejewski', 'Liliha': 'Julia Wierszelis',
#              'Szop': 'Michał Tanaś'}
#     print(ksywy['Peja'])
#
#
# zad13()

# def zad14():
#     skroty = {'cb': 'ciebie', 'wgl': 'w ogóle', 'kc': 'kocham cię', 'bk': 'beka', 'nwm': 'nie wiem'}
#     slownik = skroty.copy()
#     print(slownik['cb'])
#
#
# zad14()

# def zad16():
#     gry = {"RPG": ["Baldur's Gate", "Fallout 1-4", "Wiedźmin"], "FPS": ["Doom", "Quake"], "MMORPG": "World of Warcraft",
#            "TPP": "Max Payne"}
#     print(len(gry))
#     print(len(gry['RPG']))
#
#
# zad16()


# CW 2


# Zadanie 1

# a = input('Podaj tekst')
# spacje = a.count(' ')
# print(spacje)

# print('Podaj 2 liczby')
# a=sys.stdin.readline()
# b=sys.stdin.readline()
# a=int(a) #rzutowanie zmiennych do intów żeby policzyć
# b=int(b) #rzutowanie zmiennych do intów żeby policzyć
# c=a*b
# c=str(c) #rzutowanie z powrotem do string zeby móc wyświetlić
# sys.stdout.write(c)

# Zadanie 4
# a=int(input('Podaj liczbę\n'))
# if a<0:
#     print(-a)
# else:
#     print(a)

# Zadanie 5
# print('Podaj liczby\n')
# a=int(input())
# b=int(input())
# c=int(input())
# if a>0 and a<=10 and (a>b or b>c):
#     print('Warunki zostały spełnione')
# else:
#     print('Warunki nie zostały spełnione')

# Zadanie 6
# for i in range(101):
#     if (i%5==0):
#         print(i)

# Zadanie 7
# for i in range(4):
#     a=int(input('Podaj liczbę '))
#     print('Kwadrat liczby',a*a)

# Zadanie 8
# lista = []
# while len(lista) < 10:
#     a = int(input('Podaj liczbę'))
#     lista.append(a)

# Zadanie 9
# suma=0
# licznik=0
# a=input('Podaj liczbe wielocyfrową')
# while licznik<len(a):
#     suma = suma + int(a[licznik])
#     licznik+=1
# print(suma)

# Zadanie 10
# wysokosc = int(input('Podaj wysokosc wiezy'))
# for i in range(1, wysokosc+1):
#     print('A')
#     for j in range(1,wysokosc+1):
#         if j>i:
#             sys.stdout.write(' ')
#         else:
#             sys.stdout.write('A')
#         sys.stdout.write('\n')

# def zad11():
#     print("Podaj wysokość diamentu (w przedziale 3-9): ")
#     a = int(input())
#     if a < 3 or a > 9:
#         print("Zła wysokość")
#         return 0
#     elif a%2==1:
#         for i in range(1, a + 1, 2):
#             print(" " * (a - i // 2) + "*" * i)
#         for i in range(a - 2, 0, -2):
#             print(" " * (a - i // 2) + "*" * i)
#     else:
#         for i in range(1, a + 1, 2):
#             print(" " * (a - i // 2) + "*" * i)
#         for i in range(a - 1, 0, -2):
#             print(" " * (a - i // 2) + "*" * i)
#
#
# zad11()


# Zadanie 12
#
# for i in range(1,11):
#     for j in range(1,11):
#         k=str(i*j)
#         if len(k)<2:
#             k=' '+k
#         sys.stdout.write('| ')

# Zadanie 14
# from math import *
# try:
#     a = int(input('Podaj liczbę '))
#     print(sqrt(a))
# except ValueError:
#     print('Nie można pierwiastkować liczb ujemnych')

# def zad15():
#     try:
#         liczba = int(input('Podaj liczbę\n'))
#     except ValueError:
#         print('Nie podano liczby')
#
#
# zad15()


# CW 3

# Zadanie 1
# A=[1/x for x in range(1,11)]
# B=[2**x for x in range(11)]
# C=[x for x in B if x%4==0]

# Zadanie 2
# import random
# random.seed(4)
# D=[]
# for i in range(4):
#     D.append([])
#     for j in range(4):
#         D[i].append(random.randitn(1,10))

# Zadanie 4
# def monot(a):
#     if (a>0):
#         print('Funkcja rosnąca')
#         return 0
#     elif (a<0):
#         print('Funkcja malejąca')
#         return 0
#     else:
#         print('Funkcja stała')
#         return 0
# monot(4)

# Zadanie 5
# import math
# def pitagoras(a=4,b=3):
#     print(math.sqrt(a**2+b**2))
# pitagoras(4,6)
# pitagoras()

# Zadanie 6

# def zad8(*liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn = 1
#         for i in liczby:
#             iloczyn *= i
#         print(iloczyn)
#
#
# zad8(1, 5, 6, 8)

# def zad9(suma=0, **produkty):
#     for i in produkty:
#         suma += produkty[i]
#     print('Ilość produktów:', suma)
#
#
# zad9(cziperki=5, cola=4, monsterki=12)

# Zadanie 10
# from zespol import *
#
# a, b = 4 + 6j, 8 + 3j
# print(zespolone.rzeczywista(a))
# print(matu.odejmowanie(a,b))

# Zadanie 11
# from ciagi import *
# a,b,c= 3,7,8
# print(arytm.suma(a,b,c))
# print(arytm.nty(a,b))
# print(geom.nty(a,b,c))
# print(geom.suma(a))
# print(geom.nty(a))

# def zad11(a,b,c):
#     from ciagi import arytm, geom
#     print(arytm.suma(a, b, c))
#     print(arytm.nty(a, b))
#     print(geom.nty(a, b, c))
#     print(geom.suma(a))
#     print(geom.nty(a))
#
#
# zad11(1,2,4)


