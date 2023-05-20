import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dane = [12,14,17,19,10,11]
labels = ['A','B','C','D','E','F']
eksplozja = [0,0,0.05,0,0,0.05]
plt.pie(dane, labels=labels, explode=eksplozja, startangle=15, autopct='%1.1f%%', colors=['tab:orange','tab:olive',
                                                                                          'tab:blue','teal','tab:cyan',
                                                                                          'tab:green'])
plt.title('Tytuł')
plt.show()