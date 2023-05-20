import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = [[6, 33, 1],
        [8, 27, 3]]
labels = ['Hipermarkety', 'Supermarkety', 'Domy handlowe']
x = np.arange(3)
plt.bar(x, dane[0], width=0.30, color='blue', label='Rok 2016')
plt.bar(x + 0.30, dane[1], width=0.30, color='orange', label='Rok 2017')
plt.xticks(x + 0.15, labels=labels)
plt.legend(loc='upper right')
plt.title('Informacje o sklepach')
plt.savefig('słupki.png', format='png')
plt.show()
