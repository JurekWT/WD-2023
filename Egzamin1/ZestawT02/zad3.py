import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('rod2.xlsx', header=None)
df = df.transpose()
naglowki = ['rodzaj', 'ogrody', 'rok', 'wartosc', 'jednostka']
df.columns = naglowki
ogrody = df[df['rodzaj']=='ogrody']
dzialki = df[df['rodzaj']=='działki']
ogrody_powierzchnia = ogrody[ogrody['ogrody']=='powierzchnia']
dzialki_liczba = dzialki[dzialki['ogrody']=='liczba']
x = np.arange(2014,2018)
plt.subplot(3,1,1)
plt.plot(ogrody_powierzchnia['rok'], ogrody_powierzchnia['wartosc'])
plt.xticks(x)
plt.xlabel('Rok')
plt.ylabel('Ha')
plt.title('Powierzchnia ogrodów')
plt.subplot(3,1,3)
plt.plot(dzialki_liczba['rok'], dzialki_liczba['wartosc'])
plt.xticks(x)
plt.xlabel('Rok')
plt.ylabel('Liczba')
plt.title('Liczba działek')
plt.savefig('ogrody.pdf', format='pdf')
plt.show()