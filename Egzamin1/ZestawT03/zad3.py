import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('produkcja3.xlsx', header=None)
df = df.transpose()
df.columns = df.iloc[0]
df = df[1:]
plt.plot(df['Rok'], df['Wartość'], label='mln zł')
plt.grid()
plt.title('Produkcja w latach 2011-2019')
plt.ylabel('Wartość produkcji w mln zł')
plt.legend()
plt.tight_layout()
plt.savefig('produkcja.pdf', format='pdf')
plt.show()