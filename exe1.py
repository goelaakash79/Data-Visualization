from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('population.csv')
print(data.head())
china = data[data.country == 'china']

plt.plot(china.1998, china.2007)
plt.show()