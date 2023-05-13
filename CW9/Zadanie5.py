import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
print(df)
colors = np.random.randint(10,11,len(df))
size = np.abs(df.sepal)
plt.show()