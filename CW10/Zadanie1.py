import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')
lata = df.groupby(['Rok']).Liczba.agg('sum')
plt.plot(lata, marker='o')
plt.title('Ilość narodzin w poszczególnych latach')
plt.xlabel('Lata')
plt.ylabel('Ilość urodzin')
plt.show()