import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')
male = df.groupby(['Płeć']).Liczba.agg('sum')
wykres = male.plot.bar()
plt.show()