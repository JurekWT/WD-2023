import numpy as np

def funk(a,b):
    A = np.logspace(1,b, num=b, base=a)
    return A

print(funk(2,8))