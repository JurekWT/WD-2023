import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('licea3.xlsx')
kolory = ['red','green','blue','brown','pink','orange']
plt.bar(df['Nazwa'], df['Wartość'], color=kolory)
plt.xticks(df['Nazwa'], rotation=25, size=5)
plt.title('Ilość liceów w województwach')
plt.ylabel('Liczba liceów')
plt.tight_layout()
plt.savefig('licea.jpg', format='jpg')
plt.show()