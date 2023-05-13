import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')

print(df)

etykiety = ['M', 'K']
wartosc = [sum(df[df.Płeć == 'M'].Liczba),
           sum(df[df.Płeć == 'K'].Liczba)]



plt.subplot(1,3,1)
plt.bar(etykiety,wartosc)
plt.ylabel('Ilość narodzin')
plt.xlabel('Płeć')
plt.title('Ilość narodzin')



plt.show()
