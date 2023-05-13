import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,30,0.1)
plt.plot(x, np.sin(x)+2, label='sin(x)')
plt.plot(x, np.sin(-x), label='sin(x)', color='orange')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='center left')
plt.title('Wykres sin(x) i cos(x)')
plt.show()