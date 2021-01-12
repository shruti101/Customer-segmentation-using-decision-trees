import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
d = pd.read_csv('C:/Users/shrut/Downloads/FBAnum.csv', header= 0)
print(d)
dat = d.to_numpy()
print(dat)
a = dat[:,1]
v = dat[:,6]
cv = d.corr()
print(cv)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cv,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(d.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(d.columns)
ax.set_yticklabels(d.columns)
plt.show()

