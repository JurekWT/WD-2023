import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('mieszkania1.xlsx')
df_2016 = df[df['Rok']==2016]
explozja = [0.1, 0.2, 0.4]
plt.pie(df_2016['Wartość'], labels=df_2016['Formy budownictwa'], autopct='%1.1f%%', startangle=0, shadow=True,
        explode=explozja)
plt.title('Udział formy budownictwa w roku 2016')
plt.savefig('kółeczko.pdf', format='pdf')
plt.show()