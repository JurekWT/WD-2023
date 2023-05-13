import pandas as pd
import numpy as np

# Zadanie 1
df = pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')

# Zadanie 2
print(df[df['Liczba'] > 1000])
print(df[df['Imię'] == 'JERZY'])
print(sum(df.Liczba))
print(sum(df[df.Rok <= 2005].Liczba))
print(df.groupby(['Płeć']).agg({'Liczba': ['sum']}))
print(df.groupby(['Rok', 'Płeć']).agg({'Liczba': ['max'], 'Imię': ['min']}))
