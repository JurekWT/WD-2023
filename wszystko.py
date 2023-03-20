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

# Zadanie 10
# lista=['kilera','kilerów 2-óch','django','hari pota','interstellar']
# print('Lista ulubionych filmów',lista)
# lista.append('incepcja')
# lista.insert(1,'wladca pierscieni')
# print('Lista ulubionych filmów',lista)
# lista.sort()
# print('Lista po sortowaniu',lista)

# Zadanie 12
# a='Ala ma kota i psa'
# wyrazy=a.split(' ')
# print(wyrazy)

# Zadanie 15
# rzymskie = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5,'VI':6,'VII':7}

# Zadanie 13
# ksywy = {'Łysy': 'Łukasz Tymofiejczyk', 'Gruby': 'Jerzy Tymofiejczyk', 'Janek': 'Łukasz Tymofiejczyk',
#           'Dostatni': 'Łukasz Dostatni', 'Kwadrat': 'Arkadiusz Keller', 'Chudy': 'Oskar Głowacki'}
# print(ksywy['Łysy'],ksywy['Gruby'],ksywy['Chudy'])

# Zadanie 14
# skroty={'cb':'ciebie','wgl':'w ogóle','kc':'kocham cię','bk':'beka'}

# Zadanie 16
# gry={'RPG':'Baldur Gate','FPS':'Doom','MMORPG':'World of Warcraft','TPP':'Max Payne'}
# print(len(gry))
# print(gry['FPS'])


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

# Zadanie 15
# try:
#     liczba=int(input('Podaj liczbę'))
# except ValueError:
#     print('Nie podano liczby')


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

# Zadanie 8
# def ciag(*liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn = 1
#         for i in liczby:
#             iloczyn *= i
#         return iloczyn
#
#
# print(ciag())
# print(ciag(1,2,4,5,8))

# Zadanie 9
# def zakupy(** lista):
#     if len(lista)==0:
#         return 'Lista zakupów jest pusta'

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

