import matplotlib.plt
import pandas as pandas

df = pd.read_csv('MP.csv')
df.columns = ['y','x','z']

x = df['x'].to_numpy()
y = df['y'].to_numpy()

plt.plot(x,y)
plt.show()
