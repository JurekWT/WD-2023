import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('turystyka1.xlsx', header=None)
df2 = df.transpose()
naglowki = ['gwiazdki', 'rok', 'wartosc']
df2.columns = naglowki
df2015 = df2[df2['rok']=='2015']
df2016 = df2[df2['rok']=='2016']
labell = ['5', '4', '3', '2', '1']
plt.plot(df2015['gwiazdki'], df2015['wartosc'], label='2015', linestyle='--')
plt.plot(df2016['gwiazdki'], df2016['wartosc'], label='2016', linestyle='dotted')
plt.xticks(df2015['gwiazdki'], labels=labell)
plt.legend()
plt.xlabel('Ilość gwiazdek')
plt.ylabel('Ilość hoteli')
plt.title('Ilość hoteli w latach 2015 i 2016')
plt.grid()
plt.savefig('Ilość_hoteli.jpg', format='jpg')
plt.show()