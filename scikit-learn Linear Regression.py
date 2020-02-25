import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('Simple linear regression.csv')
x_values = df[['X']]
y_values = df['Y']

lmLR = LinearRegression()
lm = lmLR.fit(x_values, y_values)

prediction = lm.predict(x_values)

plt.scatter(x_values, y_values)
plt.plot(x_values, prediction)
plt.show()