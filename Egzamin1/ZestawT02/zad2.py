import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('uczniowie2.xlsx')
x = np.arange(2015, 2020)
print(x)
plt.scatter(x, df['Wartość'], color='red', marker='D', label='Ilość osób' )
plt.xticks(x)
plt.xlabel('Rok')
plt.ylabel('Ilośc osób')
plt.title('Uczniowie w latach 2015-2019')
plt.legend()
plt.grid()
plt.savefig('uczniowie.jpg', format='jpg')
plt.show()