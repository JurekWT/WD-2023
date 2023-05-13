import numpy as np

def funkcja(a):
    A = np.arange(a,0,-1)
    B = np.diag(A)
    return B

print(funkcja(5))