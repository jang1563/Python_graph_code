# Heatmap
# original link: https://rfriend.tistory.com/419

import numpy as np
import pandas as pd

import matpolib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.fgsize'] = [10, 8]


# load example dataset
flights = sns.load_dataset('flights')
flights.head()

# make pivot table using pivot() function

df = flights.pivot('month', 'year', 'passengers')
df.head()


# Heatmap by matplotlib
# heatmap by plit.pcolor()

plt.pcolor(df)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.title('Heatmap by plt.pcolor()', fontsize=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Month', fontsize=14)
plt.colorbar()

plt.show()

# Heatmap by seaborn

# heatmap by seaborn

ax = sns.heatmap(df)
plt.title('Heatmap of Flight by seaborn', fontsize=20)
plt.show() 

# Annotate each cell with the numeric value of integer format

sns.heatmap(df, annot=True, fmt='d')
plt.title('Annoteat cell with numeric value', fontsize=20)
plt.show()


# different colormap

sns.heatmap(df, cmap='RdYlGn_r')
plt.title('colormap of cmap=RdYlGn_r', fontsize=20)
plt.show()

# different colormap

sns.heatmap(df, cmap='YlGnBu') # 
plt.title('colormap of cmap=YlGnBu', fontsize=20)
plt.show()

# center the colormap at a specific value

sns.heatmap(df, center=df.loc['January', 1949])
plt.title('Center the colormap at Jan. 1949', fontsize=20)
plt.show()

# heatmap by pandas

df.style.background_gradient(cmap='summer')



