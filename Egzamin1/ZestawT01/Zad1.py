import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gry = pd.DataFrame(
    {
        'Miesiąc': ['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec'],
        'Zyski': [22, 33, 41, 75, 65, 50]
    }
)
filmy = pd.DataFrame(
    {
        'Miesiąc': ['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec'],
        'Zyski': [50, 41, 38, 23, 24, 30]
    }
)
plt.plot(gry['Miesiąc'], gry['Zyski'], label='Gry', color='green')
plt.plot(filmy['Miesiąc'], filmy['Zyski'], label='Filmy', linestyle='--', color='blue')
plt.xlabel('Miesiąc')
plt.ylabel('Zyski')
plt.title('Zyski z filmów i gier')
plt.legend(loc='upper left')
plt.grid()
plt.ylim(0, 100)
plt.show()
