import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lijst1 = [1, 2, 3, 4, 5]
lijst2 = [10, 20, 30, 40, 50]

print(lijst1 + lijst2)

nplijst1 = np.array(lijst1)
nplijst2 = np.array(lijst2)

print(nplijst1 + nplijst2)

x = np.arange(0, 10, 0.1)
y = np.sin(x)

print(x)
print(y)

plt.plot(x, y)
plt.show()
