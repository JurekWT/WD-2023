import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv', sep=';')
print(df)
s = df.groupby(['Sprzedawca']).Utarg.agg('sum')
print(s)
