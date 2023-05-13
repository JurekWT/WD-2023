import numpy as np

def funkcja(n):
    A = np.zeros((n,n))
    for i in range(n):
        if i==0:
            A += np.diag([2*(i+1) for j in range(n-i)])
        else
            A += np.diag

    return A

print(funkcja(6))