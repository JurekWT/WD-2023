def nty(a1, q=1, n=1):
    return a1 * q ** (n - 1)


def suma(a1, q=1, n=1):
    if q == 1:
        return a1 * n
    else:
        return a1 * ((1 - q ** n) / (1 - q))