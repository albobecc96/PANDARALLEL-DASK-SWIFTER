import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('bruta.xlsx')

df.set_index('Giorni', inplace=True)
print(df)
print(df['Aldo'])
print('The average number of daily apples by Gianni:',df['Aldo'].mean())
print(df.loc[['Lunedì','Giovedì'],['Gianni','Paolo']])
print(df.loc['Mercoledì','Aldo'])

fig = plt.figure(1)
df['Gianni'].plot.hist(x='Giorni')
plt.grid()
plt.show()
