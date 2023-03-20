def zad6():
    a = "I'm covering my ears like a kid\n" \
        "When your words mean nothing, I go la la la\n" \
        "I'm turning up the volume when you speak\n" \
        "'Cause if my heart can't stop it\n" \
        "I find a way to block it, I go\n" \
        "La la, la la la la la na na na na na\n" \
        "La la na na, la la la la la na na na na na\n" \
        "I find a way to block it, I go\n" \
        "La la na na, la la la la la na na na na na\n" \
        "La la na na, la la la la la na na na na na\n"
    print('Ilość "la" w tekście:', a.count('la'))


zad6()


def zad10():
    lista = ['Kiler', 'Kilerów 2-óch', 'Django', 'Hari Pota', 'Interstellar', 'Incepcja', 'Władca Pierścieni',
             'Zombeavers', 'Sarnie Żniwo']
    print('Lista ulubionych filmów', lista)
    lista.sort()
    print('Lista po sortowaniu:', lista)


zad10()


def zad11():
    from math import sin, cos, tan, radians
    kat = [0, 30, 45, 60, 90]
    s = [sin(radians(i)) for i in kat]
    c = [cos(radians(i)) for i in kat]
    t = [tan(radians(i)) for i in kat]
    t[4] = 0
    print('Kąt\tSinus\tCosinus\tTang')
    for i in range(len(kat)):
        print(f"{kat[i]}\t{s[i]:.2f}\t{c[i]:.2f}\t{t[i]:.2f}")


zad11()


def zad13():
    ksywy = {'Łysy': 'Łukasz Tymofiejczyk', 'Gruby': 'Jerzy Tymofiejczyk', 'Janek': 'Łukasz Januszewski',
             'Mały': 'Łukasz Dostatni', 'Kwadrat': 'Arkadiusz Keller', 'Chudy': 'Oskar Głowacki',
             'Kurak': 'Andrzej Cłapka', 'Peja': 'Ryszard Waldemar Andrzejewski', 'Liliha': 'Julia Wierszelis',
             'Szop': 'Michał Tanaś'}
    print(ksywy['Peja'])


zad13()


def zad14():
    skroty = {'cb': 'ciebie', 'wgl': 'w ogóle', 'kc': 'kocham cię', 'bk': 'beka', 'nwm': 'nie wiem'}
    slownik = skroty.copy()
    print(slownik['cb'])


zad14()


def zad16():
    gry = {"RPG": ["Baldur's Gate", "Fallout 1-4", "Wiedźmin"], "FPS": ["Doom", "Quake"], "MMORPG": "World of Warcraft",
           "TPP": "Max Payne"}
    print(len(gry))
    print(len(gry['RPG']))


zad16()
